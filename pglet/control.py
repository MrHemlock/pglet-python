""" Module for the Control class """

from __future__ import annotations
import datetime as dt
import threading
from typing import Literal, Any, Optional, Type
from collections.abc import Callable
from beartype import beartype
from difflib import SequenceMatcher
from pglet.protocol import Command, PageCommandResponsePayload


BORDER_STYLE = Literal[
    None, "dotted", "dashed", "solid", "double", "groove", "ridge", "inset", "outset"
]

TEXT_SIZE = Literal[
    None,
    "tiny",
    "xSmall",
    "small",
    "smallPlus",
    "medium",
    "mediumPlus",
    "large",
    "xLarge",
    "xxLarge",
    "superLarge",
    "mega",
]

TEXT_ALIGN = Literal[None, "left", "right", "center", "justify"]


class Control:
    """ Control class for all widgets

    :param id: The id of the control
    :type id: str, optional
    :param width: The width of the control
    :type width: int | str | None, optional
    :param height: The height of the control
    :type height: int | str | None, optional
    :param padding: The padding of the control
    :type padding: int | str | None, optional
    :param margin: The margin of the control
    :type margin: int | str | None, optional
    :param visible: Whether the control is visible
    :type visible: bool, optional
    :param disabled: Whether the control is disabled
    :type disabled: bool, optional
    :param data: The data of the control
    :type data: Any, optional
    """

    def __init__(
        self,
        id: str | None = None,
        width: str | int | None = None,
        height: str | int | None = None,
        padding: str | int | None = None,
        margin: str | int | None = None,
        visible: bool | None = None,
        disabled: bool | None = None,
        data: Any = None
    ):
        self.__page: Any = None
        self.__attrs: dict = {}
        self.__previous_children: list = []
        self.id = id
        self.__uid: str | None = None
        if id == "page":
            self.__uid = "page"
        self.width = width
        self.height = height
        self.padding = padding
        self.margin = margin
        self.visible = visible
        self.disabled = disabled
        self.data = data
        self.__event_handlers: dict = {}
        self._lock: threading.Lock = threading.Lock()

    @beartype
    def _get_children(self) -> list:
        """ Returns an empty list of children

        :return: Empty list
        :rtype: list
        """
        return []

    @beartype
    def _get_control_name(self) -> str:
        """ Returns the name of the control """
        raise Exception("_getControlName must be overridden in inherited class")

    @beartype
    def _add_event_handler(self, event_name: str, handler: Callable | None) -> None:
        """ Adds an event handler to the control

        :param event_name: The name of the event
        :type event_name: str
        :param handler: The handler of the event
        :type handler: Callable | None
        """
        self.__event_handlers[event_name] = handler

    @beartype
    def _get_event_handler(self, event_name: str) -> Callable | None:
        """ Returns the event handler of the control

        :param event_name: The name of the event
        :type event_name: str
        :return: The event handler of the control
        :rtype: Callable | None
        """
        return self.__event_handlers.get(event_name)

    @beartype
    def _get_attr(self, name: str, def_value: Any = None, data_type: str = "string") -> Any:
        """ Returns the attribute of the control

        :param name: The name of the attribute
        :type name: str
        :param def_value: The default value of the attribute
        :type def_value: str | None
        :param data_type: The data type of the attribute
        :type data_type: str
        :return: The attribute of the control
        :rtype: Any
        """
        name = name.lower()
        if name not in self.__attrs:
            return def_value

        s_val = self.__attrs[name][0]
        if data_type == "bool" and s_val is not None and isinstance(s_val, str):
            return s_val.lower() == "true"
        elif data_type == "float" and s_val is not None and isinstance(s_val, str):
            return float(s_val)
        else:
            return s_val

    @beartype
    def _set_attr(self, name: str, value: Any, dirty: bool = True) -> None:
        """ Sets the attribute of the control.

        :param name: The name of the attribute
        :type name: str
        :param value: The value of the attribute
        :type value: Any
        :param dirty: Whether the control is dirty
        :type dirty: bool
        """
        self._set_attr_internal(name, value, dirty)

    @beartype
    def _set_attr_internal(self, name: str, value: Any, dirty: bool = True) -> None:
        """ Sets the internal attribute of the control.

        :param name: The name of the attribute
        :type name: str
        :param value: The value of the attribute
        :type value: Any
        :param dirty: Whether the control is dirty
        :type dirty: bool
        """
        name = name.lower()
        orig_val = self.__attrs.get(name)

        if orig_val is None and value is None:
            return

        if value is None:
            value = ""

        if orig_val is None or orig_val[0] != value:
            self.__attrs[name] = (value, dirty)

    # event_handlers
    @property
    @beartype
    def event_handlers(self) -> dict:
        """ Returns the event handlers of the control

        :return: The event handlers of the control
        :rtype: dict
        """
        return self.__event_handlers

    # _previous_children
    @property
    @beartype
    def _previous_children(self) -> list:
        """ Returns the previous children of the control

        :return: The previous children of the control
        :rtype: list
        """
        return self.__previous_children

    # page
    @property
    @beartype
    def page(self) -> Any:
        """ Returns the page of the control

        :return: The page of the control
        :rtype: str | None
        """
        return self.__page

    @page.setter
    @beartype
    def page(self, page: Any) -> None:
        """ Sets the page of the control

        :param page: The page of the control
        :type page: str | None
        """
        self.__page = page

    # id
    @property
    @beartype
    def id(self) -> str | None:
        """ Returns the id of the control

        :return: The id of the control
        :rtype: str | None
        """
        return self._get_attr("id")

    # uid
    @property
    @beartype
    def uid(self) -> str | None:
        """ Returns the uid of the control

        :return: The uid of the control
        :rtype: str | None
        """
        return self.__uid

    @id.setter
    @beartype
    def id(self, value: str | None) -> None:
        """ Sets the id of the control

        :param value: The id of the control
        :type value: str | None
        """
        self._set_attr("id", value)

    # width
    @property
    @beartype
    def width(self) -> str | int | None:
        """ Returns the width of the control

        :return: The width of the control
        :rtype: str | int | None
        """
        return self._get_attr("width")

    @width.setter
    @beartype
    def width(self, value: str | int | None) -> None:
        """ Sets the width of the control

        :param value: The width of the control
        :type value: str | int | None
        """
        self._set_attr("width", value)

    # height
    @property
    @beartype
    def height(self) -> str | int | None:
        """ Returns the height of the control

        :return: The height of the control
        :rtype: str | int | None
        """
        return self._get_attr("height")

    @height.setter
    @beartype
    def height(self, value: str | int | None) -> None:
        """ Sets the height of the control

        :param value: The height of the control
        :type value: str | int | None
        """
        self._set_attr("height", value)

    # padding
    @property
    @beartype
    def padding(self) -> str | int | None:
        """ Returns the padding of the control

        :return: The padding of the control
        :rtype: str | int | None
        """
        return self._get_attr("padding")

    @padding.setter
    @beartype
    def padding(self, value: str | int | None) -> None:
        """ Sets the padding of the control

        :param value: The padding of the control
        :type value: str | int | None
        """
        self._set_attr("padding", value)

    # margin
    @property
    @beartype
    def margin(self) -> str | int | None:
        """ Returns the margin of the control

        :return: The margin of the control
        :rtype: str | int | None
        """
        return self._get_attr("margin")

    @margin.setter
    @beartype
    def margin(self, value: str | int | None) -> None:
        """ Sets the margin of the control

        :param value: The margin of the control
        :type value: str | int | None
        """
        self._set_attr("margin", value)

    # visible
    @property
    @beartype
    def visible(self) -> bool | None:
        """ Returns if the control is visible

        :return: If the control is visible
        :rtype: bool | None
        """
        return self._get_attr("visible")

    @visible.setter
    @beartype
    def visible(self, value: bool | None) -> None:
        """ Sets if the control is visible

        :param value: If the control is visible
        :type value: bool | None
        """
        self._set_attr("visible", value)

    # disabled
    @property
    @beartype
    def disabled(self) -> bool | None:
        """ Returns if the control is disabled

        :return: If the control is disabled
        :rtype: bool | None
        """
        return self._get_attr("disabled")

    @disabled.setter
    @beartype
    def disabled(self, value: bool | None) -> None:
        """ Sets if the control is disabled

        :param value: If the control is disabled
        :type value: bool | None
        """
        self._set_attr("disabled", value)

    # data
    @property
    @beartype
    def data(self) -> Any:
        """ Returns the data of the control

        :return: The data of the control
        :rtype: Any
        """
        return self._get_attr("data")

    @data.setter
    @beartype
    def data(self, value: Any) -> None:
        """ Sets the data of the control

        :param value: The data of the control
        :type value: Any
        """
        self._set_attr("data", value)

    # public methods
    @beartype
    def update(self) -> None:
        """ Updates the control """
        if not self.__page:
            raise Exception("Control must be added to the page first.")
        self.__page.update(self)

    def clean(self) -> PageCommandResponsePayload:
        """ Cleans the control.

        :return: The response payload
        :rtype: PageCommandResponsePayload
        """
        if not self.__page:
            raise Exception("Control must be added to the page first.")
        with self._lock:
            self._previous_children.clear()
            for child in self._get_children():
                self._remove_control_recursively(self.__page.index, child)
            return self.__page._send_command("clean", [self.uid])

    def build_update_commands(self, index: dict[str | None, Any], added_controls: list, commands: list) -> None:
        """ Builds the update commands for the control

        :param index: The index of the control
        :type index: dict[str | None, Page]
        :param added_controls: The added controls
        :type added_controls: list
        :param commands: The commands
        :type commands: list
        """
        update_cmd = self._get_cmd_attrs(update=True)

        if len(update_cmd.attrs) > 0:
            update_cmd.name = "set"
            commands.append(update_cmd)

        # go through children
        previous_children = self.__previous_children
        current_children = self._get_children()

        hashes = {}
        previous_ints = []
        current_ints = []

        for ctrl in previous_children:
            hashes[hash(ctrl)] = ctrl
            previous_ints.append(hash(ctrl))

        for ctrl in current_children:
            hashes[hash(ctrl)] = ctrl
            current_ints.append(hash(ctrl))

        # print("previous_ints:", previous_ints)
        # print("current_ints:", current_ints)

        sm = SequenceMatcher(None, previous_ints, current_ints)

        n = 0
        for tag, a1, a2, b1, b2 in sm.get_opcodes():
            if tag == "delete":
                # deleted controls
                ids = []
                for h in previous_ints[a1:a2]:
                    ctrl = hashes[h]
                    self._remove_control_recursively(index, ctrl)
                    ids.append(ctrl.__uid)
                commands.append(Command(0, "remove", ids, None, None, None))
            elif tag == "equal":
                # unchanged control
                for h in previous_ints[a1:a2]:
                    ctrl = hashes[h]
                    ctrl.build_update_commands(index, added_controls, commands)
                    n += 1
            elif tag == "replace":
                ids = []
                for h in previous_ints[a1:a2]:
                    # delete
                    ctrl = hashes[h]
                    self._remove_control_recursively(index, ctrl)
                    ids.append(ctrl.__uid)
                commands.append(Command(0, "remove", ids, None, None, None))
                for h in current_ints[b1:b2]:
                    # add
                    ctrl = hashes[h]
                    innerCmds = ctrl.get_cmd_str(
                        index=index, added_controls=added_controls
                    )
                    commands.append(
                        Command(
                            0,
                            "add",
                            None,
                            {"to": self.__uid, "at": str(n)},
                            None,
                            innerCmds,
                        )
                    )
                    n += 1
            elif tag == "insert":
                # add
                for h in current_ints[b1:b2]:
                    ctrl = hashes[h]
                    innerCmds = ctrl.get_cmd_str(
                        index=index, added_controls=added_controls
                    )
                    commands.append(
                        Command(
                            0,
                            "add",
                            None,
                            {"to": self.__uid, "at": str(n)},
                            None,
                            innerCmds,
                        )
                    )
                    n += 1

        self.__previous_children.clear()
        self.__previous_children.extend(current_children)

    def _remove_control_recursively(self, index: dict[str | None, Any], control: Any) -> None:
        """ Removes a control from the control

        :param index: The index of the control
        :type index: dict[str | None, Page]
        :param control: The control
        :type control: Any
        """
        for child in control._get_children():
            self._remove_control_recursively(index, child)

        if control.__uid in index:
            del index[control.__uid]

    # private methods
    def get_cmd_str(
            self,
            indent: int = 0,
            index: dict[str | None, Any] = None,
            added_controls: list = None
    ) -> list[Command]:
        """ Returns a list of commands to update the control

        :param indent: The indentation level
        :type indent: int
        :param index: The index of the control
        :type index: dict[str | None, Page]
        :param added_controls: The list of added controls
        :type added_controls: list
        :return: The list of commands
        :rtype: list[Command]
        """

        # remove control from index
        if self.__uid and index is not None and self.__uid in index:
            del index[self.__uid]

        commands = []

        # main command
        command = self._get_cmd_attrs(False)
        command.indent = indent
        command.values.append(self._get_control_name())
        commands.append(command)

        if added_controls is not None:
            added_controls.append(self)

        # controls
        children = self._get_children()
        for control in children:
            childCmd = control.get_cmd_str(
                indent=indent + 2, index=index, added_controls=added_controls
            )
            commands.extend(childCmd)

        self.__previous_children.clear()
        self.__previous_children.extend(children)

        return commands

    def _get_cmd_attrs(self, update: bool = False) -> Command:
        """ Returns the command attribute

        :param update: If the command is an update. Default is False
        :type update: bool, optional
        :return: The command attributes
        :rtype: Command
        """

        command = Command(0, None, [], {}, [], [])

        if update and not self.__uid:
            return command

        for attrName in sorted(self.__attrs):
            attrName = attrName.lower()
            dirty = self.__attrs[attrName][1]

            if (update and not dirty) or attrName == "id":
                continue

            val = self.__attrs[attrName][0]
            sval = ""
            if val is None:
                continue
            elif isinstance(val, bool):
                sval = str(val).lower()
            elif isinstance(val, dt.datetime) or isinstance(val, dt.date):
                sval = val.isoformat()
            else:
                sval = str(val)
            command.attrs[attrName] = sval
            self.__attrs[attrName] = (val, False)

        id = self.__attrs.get("id")
        if not update and id is not None:
            command.attrs["id"] = id
        elif update and len(command.attrs) > 0:
            command.values.append(self.__uid)

        return command
