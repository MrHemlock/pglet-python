""" Module for the Page class. """

from __future__ import annotations
import json
import logging
import threading
from typing import Literal, Any
from collections.abc import Callable
from beartype import beartype

from pglet import constants
from pglet.connection import Connection
from pglet.control import Control
from pglet.control_event import ControlEvent
from pglet.protocol import Command
from pglet.protocol import PageCommandResponsePayload
from pglet.event import Event


ALIGN = Literal[
    None,
    "start",
    "end",
    "center",
    "space-between",
    "space-around",
    "space-evenly",
    "baseline",
    "stretch",
]

THEME = Literal[None, "light", "dark"]


class Page(Control):
    """ A Page is a container for Controls.

    :param conn: The Connection to use.
    :type conn: Connection
    :param session_id: The session ID to use.
    :type session_id: str
    """
    def __init__(self, conn: Connection, session_id: str):
        Control.__init__(self, id="page")

        self._conn = conn
        self._session_id = session_id
        self._controls: list[Control] = []  # page controls
        self._index: dict[str | None, 'Page'] = {self.id: self}  # index with all page controls
        self._last_event: ControlEvent | None = None
        self._event_available = threading.Event()
        self._fetch_page_details()

    @beartype
    def __enter__(self) -> 'Page':
        """ Enter the context of the Page.

        :return: The Page.
        :rtype: Page
        """
        return self

    @beartype
    def __exit__(self, type: str, value: str, traceback: str) -> None:
        """ Exit the context of the Page.

        :param type: The type of the exception.
        :type type: str
        :param value: The value of the exception.
        :type value: str
        :param traceback: The traceback of the exception.
        :type traceback: str
        """
        self.close()

    @beartype
    def get_control(self, id: str) -> 'Page':
        """ Get a Page by its ID.

        :param id: The ID of the Control.
        :type id: str
        :return: The Page.
        :rtype: Page
        """
        return self._index.get(id)

    @beartype
    def _get_children(self) -> list[Control]:
        """ Get the children of the Page.

        :return: The children of the Page.
        :rtype: list[Control]
        """
        return self._controls

    @beartype
    def _fetch_page_details(self) -> None:
        """ Fetch the details of the Page. """
        values = self._conn.send_commands(
            self._conn.page_name,
            self._session_id,
            [
                Command(0, "get", ["page", "hash"], None, None, None),
                Command(0, "get", ["page", "winwidth"], None, None, None),
                Command(0, "get", ["page", "winheight"], None, None, None),
                Command(0, "get", ["page", "userauthprovider"], None, None, None),
                Command(0, "get", ["page", "userid"], None, None, None),
                Command(0, "get", ["page", "userlogin"], None, None, None),
                Command(0, "get", ["page", "username"], None, None, None),
                Command(0, "get", ["page", "useremail"], None, None, None),
                Command(0, "get", ["page", "userclientip"], None, None, None),
            ],
        ).results
        self._set_attr("hash", values[0], False)
        self._set_attr("winwidth", values[1], False)
        self._set_attr("winheight", values[2], False)
        self._set_attr("userauthprovider", values[3], False)
        self._set_attr("userid", values[4], False)
        self._set_attr("userlogin", values[5], False)
        self._set_attr("username", values[6], False)
        self._set_attr("useremail", values[7], False)
        self._set_attr("userclientip", values[8], False)

    @beartype
    def update(self, *controls: list[Control] | Control | None) -> None:
        """ Update the Page.

        :param controls: The controls to update.
        :type controls: list[Control] | Control | None
        """
        with self._lock:
            if len(controls) == 0:
                return self.__update(self)
            else:
                return self.__update(*controls)

    @beartype
    def __update(self, *controls: list[Control] | Control | None) -> None:
        """ Update the Page.

        :param controls: The controls to update.
        :type controls: list[Control] | Control
        """
        added_controls: list[Control] = []
        commands: list[Command] = []

        # build commands
        for control in controls:
            control.build_update_commands(self._index, added_controls, commands)

        if len(commands) == 0:
            return

        # execute commands
        results = self._conn.send_commands(
            self._conn.page_name, self._session_id, commands
        ).results

        if len(results) > 0:
            n = 0
            for line in results:
                for id in line.split(" "):
                    added_controls[n]._Control__uid = id
                    added_controls[n].page = self

                    # add to index
                    self._index[id] = added_controls[n]
                    n += 1

    @beartype
    def add(self, *controls: list[Control] | Control) -> None:
        """ Add controls to the Page.

        :param controls: The controls to add.
        :type controls: list[Control] | Control
        """
        with self._lock:
            self._controls.extend(controls)
            return self.__update(self)

    @beartype
    def insert(self, at: int, *controls: list[Control] | Control) -> None:
        """ Insert controls into the Page.

        :param at: The index to insert at.
        :type at: int
        :param controls: The controls to insert.
        :type controls: list[Control] | Control
        """
        with self._lock:
            n = at
            for control in controls:
                self._controls.insert(n, control)
                n += 1
            return self.__update(self)

    @beartype
    def remove(self, *controls: list[Control] | Control) -> None:
        """ Remove controls from the Page.

        :param controls: The controls to remove.
        :type controls: list[Control] | Control
        """
        with self._lock:
            for control in controls:
                self._controls.remove(control)
            return self.__update(self)

    @beartype
    def remove_at(self, index: int) -> None:
        """ Remove a control from the Page at a specific index.

        :param index: The index to remove at.
        :type index: int
        """
        with self._lock:
            self._controls.pop(index)
            return self.__update(self)

    @beartype
    def clean(self) -> PageCommandResponsePayload:
        """ Clean the Page.

        :return: The PageCommandResponsePayload.
        :rtype: PageCommandResponsePayload
        """
        with self._lock:
            self._previous_children.clear()
            for child in self._get_children():
                self._remove_control_recursively(self._index, child)
            self._controls.clear()
            return self._send_command("clean", [self.uid])

    @beartype
    def error(self, message: str = "") -> PageCommandResponsePayload:
        """ Raise an error on the Page.

        :param message: The error message.
        :type message: str
        :return: The PageCommandResponsePayload.
        :rtype: PageCommandResponsePayload
        """
        with self._lock:
            self._send_command("error", [message])

    @beartype
    def on_event(self, e: Event) -> None:
        """ Handle an event.

        :param e: The event.
        :type e: Event
        """
        logging.info(f"page.on_event: {e.target} {e.name} {e.data}")

        with self._lock:
            if e.target == "page" and e.name == "change":
                for props in json.loads(e.data):
                    id = props["i"]
                    if id in self._index:
                        for name in props:
                            if name != "i":
                                self._index[id]._set_attr(
                                    name, props[name], dirty=False
                                )

            elif e.target in self._index:
                self._last_event = ControlEvent(
                    e.target, e.name, e.data, self._index[e.target], self
                )
                handler = self._index[e.target].event_handlers.get(e.name)
                if handler:
                    t = threading.Thread(
                        target=handler, args=(self._last_event,), daemon=True
                    )
                    t.start()
                self._event_available.set()

    @beartype
    def wait_event(self) -> ControlEvent:
        """ Wait for an event.

        :return: The ControlEvent.
        :rtype: ControlEvent
        """
        self._event_available.clear()
        self._event_available.wait()
        return self._last_event

    @beartype
    def show_signin(self, auth_providers: str = "*", auth_groups: bool = False, allow_dismiss: bool = False) -> bool:
        """ Show the signin dialog.

        :param auth_providers: The auth providers to show.
        :type auth_providers: str
        :param auth_groups: Whether to show auth groups.
        :type auth_groups: bool
        :param allow_dismiss: Whether to allow the user to dismiss the dialog.
        :type allow_dismiss: bool
        :return: Whether the user signed in.
        :rtype: bool
        """
        with self._lock:
            self.signin = auth_providers
            self.signin_groups = auth_groups
            self.signin_allow_dismiss = allow_dismiss
            self.__update(self)

        while True:
            e = self.wait_event()
            if e.control == self and e.name.lower() == "signin":
                return True
            elif e.control == self and e.name.lower() == "dismisssignin":
                return False

    @beartype
    def signout(self) -> PageCommandResponsePayload:
        """ Sign out the user.

        :return: The PageCommandResponsePayload.
        :rtype: PageCommandResponsePayload
        """
        return self._send_command("signout", None)

    @beartype
    def can_access(self, users_and_groups: str) -> bool:
        """ Check if the user can access the page.

        :param users_and_groups: The users and groups to check.
        :type users_and_groups: str
        :return: Whether the user can access the page.
        :rtype: bool
        """
        return (
            self._send_command("canAccess", [users_and_groups]).result.lower() == "true"
        )

    @beartype
    def close(self) -> None:
        """ Close the session and connection. """
        if self._session_id == constants.ZERO_SESSION:
            self._conn.close()

    @beartype
    def _send_command(self, name: str, values: list[str]) -> PageCommandResponsePayload:
        """ Send a command to the page.

        :param name: The command name.
        :type name: str
        :param values: The command values.
        :type values: list[str]
        :return: The PageCommandResponsePayload.
        :rtype: PageCommandResponsePayload
        """
        return self._conn.send_command(
            self._conn.page_name,
            self._session_id,
            Command(0, name, values, None, None, None),
        )

    # url
    @property
    @beartype
    def url(self) -> str | None:
        """ Get the url.

        :return: The url.
        :rtype: str | None
        """
        return self._conn.page_url

    # name
    @property
    @beartype
    def name(self) -> str | None:
        """ Get the name.

        :return: The name.
        :rtype: str | None
        """
        return self._conn.page_name

    # connection
    @property
    @beartype
    def connection(self) -> Connection:
        """ Get the connection.

        :return: The connection.
        :rtype: Connection
        """
        return self._conn

    # index
    @property
    @beartype
    def index(self) -> dict[str | None, Control]:
        """ Get the index.

        :return: The index.
        :rtype: dict[str | None, Control]
        """
        return self._index

    # session_id
    @property
    @beartype
    def session_id(self) -> str:
        """ Get the session id.

        :return: The session id.
        :rtype: str
        """
        return self._session_id

    # controls
    @property
    @beartype
    def controls(self) -> list[Control]:
        """ Get the controls.

        :return: The controls.
        :rtype: list[Control]
        """
        return self._controls

    @controls.setter
    @beartype
    def controls(self, value: list[Control]) -> None:
        """ Set the controls.

        :param value: The controls.
        :type value: list[Control]
        """
        self._controls = value

    # title
    @property
    @beartype
    def title(self) -> str:
        """ Get the title.

        :return: The title.
        :rtype: str
        """
        return self._get_attr("title")

    @title.setter
    @beartype
    def title(self, value: str) -> None:
        """ Set the title.

        :param value: The title.
        :type value: str
        """
        self._set_attr("title", value)

    # vertical_fill
    @property
    @beartype
    def vertical_fill(self) -> bool | None:
        """ Get the vertical fill.

        :return: The vertical fill.
        :rtype: bool | None
        """
        return self._get_attr("verticalFill")

    @vertical_fill.setter
    @beartype
    def vertical_fill(self, value: bool | None) -> None:
        """ Set the vertical fill.

        :param value: The vertical fill.
        :type value: bool | None
        """
        self._set_attr("verticalFill", value)

    # horizontal_align
    @property
    @beartype
    def horizontal_align(self) -> ALIGN:
        """ Get the horizontal align.

        :return: The horizontal align.
        :rtype: ALIGN
        """
        return self._get_attr("horizontalAlign")

    @horizontal_align.setter
    @beartype
    def horizontal_align(self, value: ALIGN) -> None:
        """ Set the horizontal align.

        :param value: The horizontal align.
        :type value: ALIGN
        """
        self._set_attr("horizontalAlign", value)

    # vertical_align
    @property
    @beartype
    def vertical_align(self) -> ALIGN:
        """ Get the vertical align.

        :return: The vertical align.
        :rtype: ALIGN
        """
        return self._get_attr("verticalAlign")

    @vertical_align.setter
    @beartype
    def vertical_align(self, value: ALIGN) -> None:
        """ Set the vertical align.

        :param value: The vertical align.
        :type value: ALIGN
        """
        self._set_attr("verticalAlign", value)

    # gap
    @property
    @beartype
    def gap(self) -> int | None:
        """ Get the gap.

        :return: The gap.
        :rtype: int | None
        """
        return self._get_attr("gap")

    @gap.setter
    @beartype
    def gap(self, value: int | None) -> None:
        """ Set the gap.

        :param value: The gap.
        :type value: int | None
        """
        self._set_attr("gap", value)

    # padding
    @property
    @beartype
    def padding(self) -> int | None:
        """ Get the padding.

        :return: The padding.
        :rtype: int | None
        """
        return self._get_attr("padding")

    @padding.setter
    @beartype
    def padding(self, value: int | None) -> None:
        """ Set the padding.

        :param value: The padding.
        :type value: int | None
        """
        self._set_attr("padding", value)

    # bgcolor
    @property
    @beartype
    def bgcolor(self) -> str | None:
        """ Get the background color.

        :return: The background color.
        :rtype: str | None
        """
        return self._get_attr("bgcolor")

    @bgcolor.setter
    @beartype
    def bgcolor(self, value: str | None) -> None:
        """ Set the background color.

        :param value: The background color.
        :type value: str | None
        """
        self._set_attr("bgcolor", value)

    # theme
    @property
    @beartype
    def theme(self) -> THEME:
        """ Get the theme.

        :return: The theme.
        :rtype: THEME
        """
        return self._get_attr("theme")

    @theme.setter
    @beartype
    def theme(self, value: THEME) -> None:
        """ Set the theme.

        :param value: The theme.
        :type value: THEME
        """
        self._set_attr("theme", value)

    # theme_primary_color
    @property
    @beartype
    def theme_primary_color(self) -> str | None:
        """ Get the primary color.

        :return: The primary color.
        :rtype: str | None
        """
        return self._get_attr("themePrimaryColor")

    @theme_primary_color.setter
    @beartype
    def theme_primary_color(self, value: str | None) -> None:
        """ Set the primary color.

        :param value: The primary color.
        :type value: str | None
        """
        self._set_attr("themePrimaryColor", value)

    # theme_text_color
    @property
    @beartype
    def theme_text_color(self) -> str | None:
        """ Get the text color.

        :return: The text color.
        :rtype: str | None
        """
        return self._get_attr("themeTextColor")

    @theme_text_color.setter
    @beartype
    def theme_text_color(self, value: str | None) -> None:
        """ Set the text color.

        :param value: The text color.
        :type value: str | None
        """
        self._set_attr("themeTextColor", value)

    # theme_background_color
    @property
    @beartype
    def theme_background_color(self) -> str | None:
        """ Get the background color.

        :return: The background color.
        :rtype: str | None
        """
        return self._get_attr("themeBackgroundColor")

    @theme_background_color.setter
    @beartype
    def theme_background_color(self, value: str | None) -> None:
        """ Set the background color.

        :param value: The background color.
        :type value: str | None
        """
        self._set_attr("themeBackgroundColor", value)

    # hash
    @property
    @beartype
    def hash(self) -> str | None:
        """ Get the hash.

        :return: The hash.
        :rtype: str | None
        """
        return self._get_attr("hash")

    @hash.setter
    @beartype
    def hash(self, value: str | None) -> None:
        """ Set the hash.

        :param value: The hash.
        :type value: str | None
        """
        self._set_attr("hash", value)

    # win_width
    @property
    @beartype
    def win_width(self) -> int:
        """ Get the window width.

        :return: The window width.
        :rtype: int
        """
        w = self._get_attr("winwidth")
        if w is not None and w != "":
            return int(w)
        return 0

    # win_height
    @property
    @beartype
    def win_height(self) -> int:
        """ Get the window height.

        :return: The window height.
        :rtype: int
        """
        h = self._get_attr("winheight")
        if h is not None and h != "":
            return int(h)
        return 0

    # signin
    @property
    @beartype
    def signin(self) -> bool | None:
        """ Get the signin status.

        :return: The signin status.
        :rtype: bool | None
        """
        return self._get_attr("signin")

    @signin.setter
    @beartype
    def signin(self, value: bool | None) -> None:
        """ Set the signin status.

        :param value: The signin status.
        :type value: bool | None
        """
        self._set_attr("signin", value)

    # signin_allow_dismiss
    @property
    @beartype
    def signin_allow_dismiss(self) -> bool | None:
        """ Get the signin allow to dismiss status.

        :return: The signin allow to dismiss status.
        :rtype: bool | None
        """
        return self._get_attr("signinAllowDismiss")

    @signin_allow_dismiss.setter
    @beartype
    def signin_allow_dismiss(self, value: bool | None) -> None:
        """ Set the signin allow to dismiss status.

        :param value: The signin allow to dismiss status.
        :type value: bool | None
        """
        self._set_attr("signinAllowDismiss", value)

    # signin_groups
    @property
    @beartype
    def signin_groups(self) -> str | None:
        """ Get the signin groups.

        :return: The signin groups.
        :rtype: str | None
        """
        return self._get_attr("signinGroups")

    @signin_groups.setter
    @beartype
    def signin_groups(self, value: str | None) -> None:
        """ Set the signin groups.

        :param value: The signin groups.
        :type value: str | None
        """
        self._set_attr("signinGroups", value)

    # user_auth_provider
    @property
    @beartype
    def user_auth_provider(self) -> str | None:
        """ Get the user auth provider.

        :return: The user auth provider.
        :rtype: str | None
        """
        return self._get_attr("userauthprovider")

    # user_id
    @property
    @beartype
    def user_id(self) -> str | None:
        """ Get the user id.

        :return: The user id.
        :rtype: str | None
        """
        return self._get_attr("userId")

    # user_login
    @property
    @beartype
    def user_login(self) -> str | None:
        """ Get the user login.

        :return: The user login.
        :rtype: str | None
        """
        return self._get_attr("userLogin")

    # user_name
    @property
    @beartype
    def user_name(self) -> str | None:
        """ Get the user name.

        :return: The user name.
        :rtype: str | None
        """
        return self._get_attr("userName")

    # user_email
    @property
    @beartype
    def user_email(self) -> str | None:
        """ Get the user email.

        :return: The user email.
        :rtype: str | None
        """
        return self._get_attr("userEmail")

    # user_client_ip
    @property
    @beartype
    def user_client_ip(self) -> str | None:
        """ Get the user client ip.

        :return: The user client ip.
        :rtype: str | None
        """
        return self._get_attr("userClientIP")

    # on_signin
    @property
    @beartype
    def on_signin(self) -> str | None:
        """ Get the on signin.

        :return: The on signin.
        :rtype: str | None
        """
        return self._get_event_handler("signin")

    @on_signin.setter
    @beartype
    def on_signin(self, handler: Callable | None) -> None:
        """ Set the on signin.

        :param handler: The on signin.
        :type handler: Callable | None
        """
        self._add_event_handler("signin", handler)

    # on_dismiss_signin
    @property
    @beartype
    def on_dismiss_signin(self) -> Callable | None:
        """ Get the on dismiss signin.

        :return: The on dismiss signin.
        :rtype: Callable | None
        """
        return self._get_event_handler("dismissSignin")

    @on_dismiss_signin.setter
    @beartype
    def on_dismiss_signin(self, handler: Callable | None) -> None:
        """ Set the on dismiss signin.

        :param handler: The on dismiss signin.
        :type handler: Callable | None
        """
        self._add_event_handler("dismissSignin", handler)

    # on_signout
    @property
    @beartype
    def on_signout(self) -> Callable | None:
        """ Get the on signout.

        :return: The on signout.
        :rtype: Callable | None
        """
        return self._get_event_handler("signout")

    @on_signout.setter
    @beartype
    def on_signout(self, handler: Callable | None) -> None:
        """ Set the on signout.

        :param handler: The on signout.
        :type handler: Callable | None
        """
        self._add_event_handler("signout", handler)

    # on_close
    @property
    @beartype
    def on_close(self) -> Callable | None:
        """ Get the on close.

        :return: The on close.
        :rtype: Callable | None
        """
        return self._get_event_handler("close")

    @on_close.setter
    @beartype
    def on_close(self, handler: Callable | None) -> None:
        """ Set the on close.

        :param handler: The on close.
        :type handler: Callable | None
        """
        self._add_event_handler("close", handler)

    # on_hash_change
    @property
    @beartype
    def on_hash_change(self) -> Callable | None:
        """ Get the on hash change.

        :return: The on hash change.
        :rtype: Callable | None
        """
        return self._get_event_handler("hashChange")

    @on_hash_change.setter
    @beartype
    def on_hash_change(self, handler: Callable | None) -> None:
        """ Set the on hash change.

        :param handler: The on hash change.
        :type handler: Callable | None
        """
        self._add_event_handler("hashChange", handler)

    # on_resize
    @property
    @beartype
    def on_resize(self) -> Callable | None:
        """ Get the on resize.

        :return: The on resize.
        :rtype: Callable | None
        """
        return self._get_event_handler("resize")

    @on_resize.setter
    @beartype
    def on_resize(self, handler: Callable | None) -> None:
        """ Set the on resize.

        :param handler: The on resize.
        :type handler: Callable | None
        """
        self._add_event_handler("resize", handler)

    # on_connect
    @property
    @beartype
    def on_connect(self) -> Callable | None:
        """ Get the on connect.

        :return: The on connect.
        :rtype: Callable | None
        """
        return self._get_event_handler("connect")

    @on_connect.setter
    @beartype
    def on_connect(self, handler: Callable | None) -> None:
        """ Set the on connect.

        :param handler: The on connect.
        :type handler: Callable | None
        """
        self._add_event_handler("connect", handler)

    # on_disconnect
    @property
    @beartype
    def on_disconnect(self) -> Callable | None:
        """ Get the on disconnect.

        :return: The on disconnect.
        :rtype: Callable | None
        """
        return self._get_event_handler("disconnect")

    @on_disconnect.setter
    def on_disconnect(self, handler):
        self._add_event_handler("disconnect", handler)
