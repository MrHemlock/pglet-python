""" Module for the dataclasses of the pglet server. """

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any
from beartype import beartype


class Actions:
    """ 'Enum' for the actions of the pglet server. """
    REGISTER_HOST_CLIENT = "registerHostClient"
    SESSION_CREATED = "sessionCreated"
    PAGE_COMMAND_FROM_HOST = "pageCommandFromHost"
    PAGE_COMMANDS_BATCH_FROM_HOST = "pageCommandsBatchFromHost"
    PAGE_EVENT_TO_HOST = "pageEventToHost"


@beartype
@dataclass
class Command:
    """ Dataclass for the commands of the pglet server.

    Attributes:
        indent (int): The indent of the command.
        name (str | None): The name of the command.
        values (list[str] | None): The values of the command.
        attrs (dict[str, str] | None): The attributes of the command.
        lines (list[str] | None): The lines of the command.
        commands (list[Any] | None): The commands of the command.
    """
    indent: int
    name: str | None
    values: list[str] | None
    attrs: dict[str, str] | None
    lines: list[str] | None
    commands: list[Any] | None


@beartype
@dataclass
class Message:
    """ Dataclass for the messages of the pglet server.

    Attributes:
        id (str): The id of the message.
        action (str): The action of the message.
        payload (Any): The payload of the message.
    """
    id: str
    action: str
    payload: Any


@beartype
@dataclass
class PageCommandRequestPayload:
    """ Dataclass for the payload of the page command request.

    Attributes:
        pageName (str): The name of the page.
        sessionID (str): The id of the session.
        command (Command): The command of the page command request.
    """
    pageName: str
    sessionID: str
    command: Command


@beartype
@dataclass
class PageCommandResponsePayload:
    """ Dataclass for the payload of the page command response.

    Attributes:
        result (str): The result of the page command response.
        error (str): The error of the page command response.
    """
    result: str
    error: str


@beartype
@dataclass
class PageCommandsBatchRequestPayload:
    """ Dataclass for the payload of the page commands batch request.

    Attributes:
        pageName (str): The name of the page.
        sessionID (str): The id of the session.
        commands (list[Command]): The commands of the page commands batch request.
    """
    pageName: str
    sessionID: str
    commands: list[Command]


@beartype
@dataclass
class PageCommandsBatchResponsePayload:
    """ Dataclass for the payload of the page commands batch response.

    Attributes:
        results (list[str]): The result of the page commands batch response.
        error (str): The error of the page commands batch response.
    """
    results: list[str]
    error: str


@beartype
@dataclass
class PageEventPayload:
    """ Dataclass for the payload of the page event.

    Attributes:
        pageName (str): The name of the page.
        sessionID (str): The id of the session.
        eventTarget (str): The target of the page event.
        eventName (str): The name of the page event.
        eventData (str): The data of the page event.
    """
    pageName: str
    sessionID: str
    eventTarget: str
    eventName: str
    eventData: str


@beartype
@dataclass
class RegisterHostClientRequestPayload:
    """ Dataclass for the payload of the register host client request.

    Attributes:
        hostClientID (str | None): The id of the host client.
        pageName (str): The name of the page.
        isApp (bool): Whether the page is an app.
        update (bool): Whether the page is an update.
        authToken (str | None): The auth token of the page.
        permissions (str | None): The permissions of the page.
    """
    hostClientID: str | None
    pageName: str
    isApp: bool
    update: bool
    authToken: str | None
    permissions: str | None


@beartype
@dataclass
class RegisterHostClientResponsePayload:
    """ Dataclass for the payload of the register host client response.

    Attributes:
        hostClientID (str | None): The id of the host client.
        pageName (str): The name of the page.
        sessionID (str): The id of the session.
        error (str): The error of the register host client response.
    """
    hostClientID: str | None
    pageName: str
    sessionID: str
    error: str


@beartype
@dataclass
class PageSessionCreatedPayload:
    """ Dataclass for the payload of the page session created.

    Attributes:
        pageName (str): The name of the page.
        sessionID (str): The id of the session.
    """
    pageName: str
    sessionID: str
