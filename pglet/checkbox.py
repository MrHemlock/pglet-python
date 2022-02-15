""" Module for Checkbox class. """

from __future__ import annotations
from typing import Literal, Any
from collections.abc import Callable
from beartype import beartype
from pglet.control import Control


BOX_SIDE = Literal[None, "start", "end"]


class Checkbox(Control):
    """ Checkbox allows to select one or more items from a group, or switch between two
    mutually exclusive options (checked or unchecked, on or off).

    :param label: Label to display next to the checkbox. Defaults to None.
    :type label: str | None, optional
    :param id: ID of the checkbox. Defaults to None.
    :type id: str | None, optional
    :param value: Current value of the checkbox. Defaults to False.
    :type value: bool | None, optional
    :param value_field: Specify which field to bind the value of checkbox when used
        inside Grid column template. Defaults to None.
    :type value_field: str | None, optional
    :param box_side: Allows you to set the checkbox to be at the before (start) or
        after (end) the label. Defaults to "start".
    :type box_side: str | None, optional
    :param focused: Whether the checkbox is focused. Defaults to False.
    :type focused: bool | None, optional
    :param data: Additional data attached to the control. The value is passed in change
        event data along with a checkbox state. Defaults to None.
    :type data: object | None, optional
    :param width: Width of the checkbox. Defaults to None.
    :type width: int | str | None, optional
    :param height: Height of the checkbox. Defaults to None.
    :type height: int | str | None, optional
    :param padding: Padding of the checkbox. Defaults to None.
    :type padding: int | str | None, optional
    :param margin: Margin of the checkbox. Defaults to None.
    :type margin: int | str | None, optional
    :param on_change: Fires when the state of the checkbox is changed. Defaults to None.
    :type on_change: Callable | None, optional
    :param visible: Whether the checkbox is visible. Defaults to True.
    :type visible: bool | None, optional
    :param disabled: Whether the checkbox is disabled. Defaults to False.
    :type disabled: bool | None, optional
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
        width: int | str | None = None,
        height: int | str | None = None,
        padding: int | str | None = None,
        margin: int | str | None = None,
        on_change: Callable | None = None,
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

    @beartype
    def _get_control_name(self) -> str:
        """ Returns the name of the control.

        :return: The name of the control.
        :rtype: str
        """
        return "checkbox"

    # on_change
    @property
    @beartype
    def on_change(self) -> Callable | None:
        """ Returns the handler for the change event.

        :return: The handler for the change event.
        :rtype: Callable | None
        """
        return self._get_event_handler("change")

    @on_change.setter
    @beartype
    def on_change(self, handler: Callable | None) -> None:
        """ Sets the handler for the change event.

        :param handler: The handler for the change event.
        :type handler: Callable | None
        """
        self._add_event_handler("change", handler)

    # value
    @property
    @beartype
    def value(self) -> bool | None:
        """ Returns the value of the checkbox.

        :return: The value of the checkbox.
        :rtype: bool | None
        """
        return self._get_attr("value", data_type="bool", def_value=False)

    @value.setter
    @beartype
    def value(self, value: bool | None) -> None:
        """ Sets the value of the checkbox.

        :param value: The value of the checkbox.
        :type value: bool | None
        """
        self._set_attr("value", value)

    # value_field
    @property
    @beartype
    def value_field(self) -> str | None:
        """ Return the field that is bound to the value of checkbox when used
        inside Grid column template.

        :return: The value of the checkbox.
        :rtype: str | None
        """
        return self._get_attr("value")

    @value_field.setter
    @beartype
    def value_field(self, value: str | None) -> None:
        """ Sets the field that is bound to the value of checkbox when used
        inside Grid column template.

        :param value: The value of the checkbox.
        :type value: str | None
        """
        self._set_attr("value", value)
        if value is not None:
            self._set_attr("value", f"{{{value}}}")

    # label
    @property
    @beartype
    def label(self) -> str | None:
        """ Returns the label of the checkbox.
        
        :return: The label of the checkbox.
        :rtype: str | None
        """
        return self._get_attr("label")

    @label.setter
    @beartype
    def label(self, value: str | None) -> None:
        """ Sets the label of the checkbox.
        
        :param value: The label of the checkbox.
        :type value: str | None
        """
        self._set_attr("label", value)

    # box_side
    @property
    @beartype
    def box_side(self) -> BOX_SIDE:
        """ Returns the side of the box.
        
        :return: The side of the box.
        :rtype: BOX_SIDE
        """
        return self._get_attr("boxSide")

    @box_side.setter
    @beartype
    def box_side(self, value: BOX_SIDE) -> None:
        """ Sets the box side of the checkbox.
        
        :param value: The box side of the checkbox.
        :type value: BOX_SIDE
        """
        self._set_attr("boxSide", value)

    # focused
    @property
    @beartype
    def focused(self) -> bool | None:
        """ Returns the focused state of the checkbox.
        
        :return: The focused state of the checkbox.
        :rtype: bool | None
        """
        return self._get_attr("focused")

    @focused.setter
    @beartype
    def focused(self, value: bool | None) -> None:
        """ Sets the focused state of the checkbox.
        
        :param value: The focused state of the checkbox.
        :type value: bool | None
        """
        self._set_attr("focused", value)
