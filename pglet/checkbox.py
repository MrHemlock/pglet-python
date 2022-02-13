""" Module for Checkbox class. """

from __future__ import annotations
from typing import Literal, Optional, Callable, Any
from beartype import beartype
from pglet.control import Control


BOX_SIDE = Literal[None, "start", "end"]


class Checkbox(Control):
    """ Checkbox allows to select one or more items from a group, or switch between two
    mutually exclusive options (checked or unchecked, on or off).

    :param label: Label to display next to the checkbox. Defaults to None.
    :type label: str, optional
    :param id: ID of the checkbox. Defaults to None.
    :type id: str, optional
    :param value: Current value of the checkbox. Defaults to False.
    :type value: bool, optional
    :param value_field: Specify which field to bind the value of checkbox when used
        inside Grid column template. Defaults to None.
    :type value_field: str, optional
    :param box_side: Allows you to set the checkbox to be at the before (start) or
        after (end) the label. Defaults to "start".
    :type box_side: str, optional
    :param focused: Whether the checkbox is focused. Defaults to False.
    :type focused: bool, optional
    :param data: Additional data attached to the control. The value is passed in change
        event data along with a checkbox state. Defaults to None.
    :type data: object, optional
    :param width: Width of the checkbox. Defaults to None.
    :type width: int, optional
    :param height: Height of the checkbox. Defaults to None.
    :type height: int, optional
    :param padding: Padding of the checkbox. Defaults to None.
    :type padding: int, optional
    :param margin: Margin of the checkbox. Defaults to None.
    :type margin: int, optional
    :param on_change: Fires when the state of the checkbox is changed. Defaults to None.
    :type on_change: callable, optional
    :param visible: Whether the checkbox is visible. Defaults to True.
    :type visible: bool, optional
    :param disabled: Whether the checkbox is disabled. Defaults to False.
    :type disabled: bool, optional
    """

    def __init__(
        self,
        label: str | None = None,
        id: str | None = None,
        value: bool | None = None,
        value_field: str | None = None,
        box_side: BOX_SIDE = None,
        focused: bool | None = None,
        data: Any = None,
        width: int | None = None,
        height: int | None = None,
        padding: int | None = None,
        margin: int | None = None,
        on_change: Optional[Callable] = None,
        visible: bool | None = None,
        disabled: bool | None = None,
    ) -> None:
        """ Initializes a new instance of the Checkbox class. """
        Control.__init__(
            self,
            id=id,
            width=width,
            height=height,
            padding=padding,
            margin=margin,
            visible=visible,
            disabled=disabled,
            data=data,
        )
        self.value = value
        self.value_field = value_field
        self.label = label
        self.box_side = box_side
        self.focused = focused
        self.on_change = on_change

    def _get_control_name(self) -> str:
        """ Returns the name of the control.

        :return: The name of the control.
        :rtype: str
        """
        return "checkbox"

    # on_change
    @property
    def on_change(self) -> Optional[Callable]:
        """ Returns the handler for the change event.

        :return: The handler for the change event.
        :rtype: callable
        """
        return self._get_event_handler("change")

    @on_change.setter
    def on_change(self, handler: Optional[Callable]) -> None:
        """ Sets the handler for the change event.

        :param handler: The handler for the change event.
        :type handler: callable
        """
        self._add_event_handler("change", handler)

    # value
    @property
    def value(self) -> bool | None:
        """ Returns the value of the checkbox.

        :return: The value of the checkbox.
        :rtype: bool
        """
        return self._get_attr("value", data_type="bool", def_value=False)

    @value.setter
    @beartype
    def value(self, value: bool | None) -> None:
        """ Sets the value of the checkbox.

        :param value: The value of the checkbox.
        :type value: bool
        """
        self._set_attr("value", value)

    # value_field
    @property
    def value_field(self) -> str | None:
        """ Return the field that is bound to the value of checkbox when used
        inside Grid column template.

        :return: The value of the checkbox.
        :rtype: str
        """
        return self._get_attr("value")

    @value_field.setter
    def value_field(self, value: str | None) -> None:
        """ Sets the field that is bound to the value of checkbox when used
        inside Grid column template.

        :param value: The value of the checkbox.
        :type value: str
        """
        self._set_attr("value", value)
        if value is not None:
            self._set_attr("value", f"{{{value}}}")

    # label
    @property
    def label(self) -> str | None:
        """ Returns the label of the checkbox.

        :return: The label of the checkbox.
        :rtype: str
        """
        return self._get_attr("label")

    @label.setter
    def label(self, value: str | None) -> None:
        """ Sets the label of the checkbox.

        :param value: The label of the checkbox.
        :type value: str
        """
        self._set_attr("label", value)

    # box_side
    @property
    def box_side(self):
        return self._get_attr("boxSide")

    @box_side.setter
    @beartype
    def box_side(self, value: BOX_SIDE) -> None:
        """ Sets the box side of the checkbox.

        :param value: The box side of the checkbox.
        :type value: str
        """
        self._set_attr("boxSide", value)

    # focused
    @property
    def focused(self) -> bool | None:
        """ Returns the focused state of the checkbox.

        :return: The focused state of the checkbox.
        :rtype: bool
        """
        return self._get_attr("focused")

    @focused.setter
    @beartype
    def focused(self, value: bool | None) -> None:
        """ Sets the focused state of the checkbox.

        :param value: The focused state of the checkbox.
        :type value: bool
        """
        self._set_attr("focused", value)
