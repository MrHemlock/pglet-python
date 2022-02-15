""" Module for the Connection class. """

from __future__ import annotations
from collections.abc import Callable
import json
import logging
import threading
import uuid
from beartype import beartype
from pglet.protocol import *
from pglet.reconnecting_websocket import ReconnectingWebSocket


class Connection:
    """ A connection to the pglet server. This class is used to connect to the pglet server
    and send and receive

    :param ws: The websocket to use for the connection.
    :type ws: ReconnectingWebSocket
    """

    def __init__(self, ws: ReconnectingWebSocket):
        self._ws = ws
        self._ws.on_message = self._on_message
        self._ws_callbacks: dict = {}
        self._on_event: Callable | None = None
        self._on_session_created: Callable | None = None
        self.host_client_id: str | None = None
        self.page_name: str | None = None
        self.page_url: str | None = None
        self.browser_opened: bool = False
        self.sessions: dict = {}

    @property
    @beartype
    def on_event(self) -> Callable | None:
        """ The event handler. This is called when a new event is received.

        :return: The event handler.
        :rtype: Callable | None
        """
        return self._on_event

    @on_event.setter
    @beartype
    def on_event(self, handler: Callable | None) -> None:
        """ Set the event handler. This is called when a new event is received.

        :param handler: The event handler.
        :type handler: Callable | None
        """
        self._on_event = handler

    @property
    @beartype
    def on_session_created(self) -> Callable | None:
        """ The session created handler. This is called when a new session is created.

        :return: The session created handler.
        :rtype: Callable | None
        """
        return self._on_session_created

    @on_session_created.setter
    @beartype
    def on_session_created(self, handler: Callable | None) -> None:
        """ Set the session created handler. This is called when a new session is created.

        :param handler: The session created handler.
        :type handler: Callable | None
        """
        self._on_session_created = handler

    @beartype
    def _on_message(self, data: str) -> None:
        """ Called when a message is received. This is called by the websocket.

        :param data: The message data.
        :type data: str
        """
        logging.debug(f"_on_message: {data}")
        msg_dict = json.loads(data)
        msg = Message(**msg_dict)
        if msg.id != "":
            # callback
            evt = self._ws_callbacks[msg.id][0]
            self._ws_callbacks[msg.id] = (None, msg.payload)
            evt.set()
        elif msg.action == Actions.PAGE_EVENT_TO_HOST:
            if self._on_event is not None:
                th = threading.Thread(
                    target=self._on_event,
                    args=(
                        self,
                        PageEventPayload(**msg.payload),
                    ),
                    daemon=True,
                )
                th.start()
                # self._on_event(self, PageEventPayload(**msg.payload))
        elif msg.action == Actions.SESSION_CREATED:
            if self._on_session_created is not None:
                th = threading.Thread(
                    target=self._on_session_created,
                    args=(
                        self,
                        PageSessionCreatedPayload(**msg.payload),
                    ),
                    daemon=True,
                )
                th.start()
        else:
            # it's something else
            print(msg.payload)

    @beartype
    def register_host_client(
        self,
        host_client_id: str | None,
        page_name: str,
        is_app: bool,
        update: bool,
        auth_token: str | None,
        permissions: str | None,
    ) -> RegisterHostClientResponsePayload:
        """ Register the host client.

        :param host_client_id: The host client id.
        :type host_client_id: str | None
        :param page_name: The page name.
        :type page_name: str
        :param is_app: Whether the page is an app.
        :type is_app: bool
        :param update: Whether the page is an update.
        :type update: bool
        :param auth_token: The auth token.
        :type auth_token: str | None
        :param permissions: The permissions.
        :type permissions: str | None
        :return: The response payload.
        :rtype: RegisterHostClientResponsePayload
        """
        payload = RegisterHostClientRequestPayload(
            host_client_id, page_name, is_app, update, auth_token, permissions
        )
        response = self._send_message_with_result(Actions.REGISTER_HOST_CLIENT, payload)
        return RegisterHostClientResponsePayload(**response)

    @beartype
    def send_command(self, page_name: str, session_id: str, command: Command) -> PageCommandResponsePayload:
        """ Send a command to the server.

        :param page_name: The name of the page.
        :type page_name: str
        :param session_id: The session id.
        :type session_id: str
        :param command: The command to send.
        :type command: Command
        :return: The response payload.
        :rtype: PageCommandResponsePayload
        """
        payload = PageCommandRequestPayload(page_name, session_id, command)
        response = self._send_message_with_result(
            Actions.PAGE_COMMAND_FROM_HOST, payload
        )
        result = PageCommandResponsePayload(**response)
        if result.error != "":
            raise Exception(result.error)
        return result

    @beartype
    def send_commands(
            self,
            page_name: str,
            session_id: str,
            commands: list[Command]
    ) -> PageCommandsBatchResponsePayload:
        """ Send a list of commands to the server.

        :param page_name: The name of the page.
        :type page_name: str
        :param session_id: The session id.
        :type session_id: str
        :param commands: The list of commands.
        :type commands: list[Command]
        :return: The response payload.
        :rtype: PageCommandsBatchResponsePayload
        """
        payload = PageCommandsBatchRequestPayload(page_name, session_id, commands)
        response = self._send_message_with_result(
            Actions.PAGE_COMMANDS_BATCH_FROM_HOST, payload
        )
        result = PageCommandsBatchResponsePayload(**response)
        if result.error != "":
            raise Exception(result.error)
        return result

    @beartype
    def _send_message_with_result(
            self,
            action_name: str,
            payload: PageCommandsBatchRequestPayload | PageCommandRequestPayload | RegisterHostClientRequestPayload
    ) -> dict:
        """ Send a message to the host and wait for the response.

        :param action_name: The action name.
        :type action_name: str
        :param payload: The payload.
        :type payload: PageCommandsBatchRequestPayload | PageCommandRequestPayload | RegisterHostClientRequestPayload
        :return: The response payload.
        :rtype: dict
        """
        msg_id = uuid.uuid4().hex
        msg = Message(msg_id, action_name, payload)
        j = json.dumps(msg, default=vars)
        logging.debug(f"_send_message_with_result: {j}")
        evt = threading.Event()
        self._ws_callbacks[msg_id] = (evt, None)
        self._ws.send(j)
        evt.wait()
        return self._ws_callbacks.pop(msg_id)[1]

    @beartype
    def close(self) -> None:
        """ Close the connection. """
        logging.debug("Closing connection...")
        if self._ws is not None:
            self._ws.close()
