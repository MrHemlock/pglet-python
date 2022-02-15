""" Module for ChoiceGroup and Option class. """

from __future__ import annotations
from typing import Iterable, Any
from collections.abc import Callable
from beartype import beartype
from pglet.control import Control


class Option(Control):
    """ Option represents an item within ChoiceGroup.

    :param key: Option's key. text value will be used instead if key is not specified. Default is None.
    :type key: str | None, optional
    :param text: Option's display text. key value will be used instead if text is not specified. Default is None.
    :type text: str | None, optional
    :param icon: Icon name to display with this option. Default is None.
    :type icon: str | None, optional
    :param icon_color: Icon color. Default is None.
    :type icon_color: str | None, optional
    """

    def __init__(
            self,
            key: str | None = None,
            text: str | None = None,
            icon: str | None = None,
            icon_color: str | None = None
    ) -> None:
        """ Initialize Option. """
        Control.__init__(self)
        assert key is not None or text is not None, "key or text must be specified"

        self.key = key
        self.text = text
        self.icon = icon
        self.icon_color = icon_color

    @beartype
    def _get_control_name(self) -> str:
        """ Get control name.

        :return: Control name.
        :rtype: str
        """
        return "option"

    # key
    @property
    @beartype
    def key(self) -> str | None:
        """ Option's key.

        :return: Option's key.
        :rtype: str | None
        """
        return self._get_attr("key")

    @key.setter
    @beartype
    def key(self, value: str | None) -> None:
        """ Set option's key.

        :param value: Option's key.
        :type value: str | None
        """
        self._set_attr("key", value)

    # text
    @property
    @beartype
    def text(self) -> str | None:
        """ Option's text.

        :return: Option's text.
        :rtype: str | None
        """
        return self._get_attr("text")

    @text.setter
    @beartype
    def text(self, value: str | None) -> None:
        """ Set option's text.

        :param value: Option's text.
        :type value: str | None
        """
        self._set_attr("text", value)

    # icon
    @property
    @beartype
    def icon(self) -> str | None:
        """ Icon name to display with this option.

        :return: Icon name.
        :rtype: str | None
        """
        return self._get_attr("icon")

    @icon.setter
    @beartype
    def icon(self, value: str | None) -> None:
        """ Set icon name.

        :param value: Icon name.
        :type value: str | None
        """
        self._set_attr("icon", value)

    # icon_color
    @property
    @beartype
    def icon_color(self) -> str | None:
        """ Icon color.

        :return: Icon color.
        :rtype: str | None
        """
        return self._get_attr("iconColor")

    @icon_color.setter
    @beartype
    def icon_color(self, value: str | None) -> None:
        """ Set icon color.

        :param value: Icon color.
        :type value: str | None
        """
        self._set_attr("iconColor", value)


class ChoiceGroup(Control):
    """ Radio buttons let people select a single option from two or more choices.

    :param label: Descriptive label for the choice group. Defaults to None.
    :type label: str | None, optional
    :param id: ID for the choice group. Defaults to None.
    :type id: str | None, optional
    :param value: key value of the selected option. Defaults to None.
    :type value: str | None, optional
    :param data: Additional data attached to the control. The value is passed in change event data
        along with a ChoiceGroup selected value. Defaults to None.
    :type data: Any, optional
    :param options: Options for the choice group. Defaults to None.
    :type options: Iterable[Option] | None, optional
    :param width: Width of the choice group. Defaults to None.
    :type width: int | str | None, optional
    :param height: Height of the choice group. Defaults to None.
    :type height: int | str | None, optional
    :param padding: Padding for the choice group. Defaults to None.
    :type padding: int | str | None, optional
    :param margin: Margin for the choice group. Defaults to None.
    :type margin: int | str | None, optional
    :param focused: Whether the choice group is focused. Defaults to False.
    :type focused: bool | None, optional
    :param on_change: Fires when the choice has been changed. Defaults to None.
    :type on_change: Callable | None, optional
    :param on_focus: Fires when the choice group has been focused. Defaults to None.
    :type on_focus: Callable | None, optional
    :param on_blur: Fires when the choice group has been blurred. Defaults to None.
    :type on_blur: Callable | None, optional
    :param visible: Whether the choice group is visible. Defaults to True.
    :type visible: bool | None, optional
    :param disabled: Whether the choice group is disabled. Defaults to False.
    :type disabled: bool | None, optional
    """
    def __init__(
        self,
        label: str | None = None,
        id: str | None = None,
        value: str | None = None,
        data: Any = None,
        options: Iterable[Option] | None = None,
        width: int | None = None,
        height: int | None = None,
        padding: int | None = None,
        margin: int | None = None,
        focused: bool | None = None,
        on_change: Callable | None = None,
        on_focus: Callable | None = None,
        on_blur: Callable | None = None,
        visible: bool | None = None,
        disabled: bool | None = None,
    ):
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
        self.label = label
        self.focused = focused
        self.on_change = on_change
        self.on_focus = on_focus
        self.on_blur = on_blur
        self.__options: list[Option] = []
        if options is not None:
            for option in options:
                self.__options.append(option)

    @beartype
    def _get_control_name(self) -> str:
        """ Returns the control name.

        :return: The control name.
        :rtype: str
        """
        return "choicegroup"

    # options
    @property
    @beartype
    def options(self) -> list[Option]:
        """ Returns the options.

        :return: The options.
        :rtype: list[Option] | None
        """
        return self.__options

    @options.setter
    @beartype
    def options(self, value: list[Option]) -> None:
        """ Sets the options.

        :param value: The options.
        :type value: list[Option] | None
        """
        self.__options = value

    # on_change
    @property
    @beartype
    def on_change(self) -> Callable | None:
        """ Returns the on_change callback.

        :return: The on_change callback.
        :rtype: Callable | None
        """
        return self._get_event_handler("change")

    @on_change.setter
    @beartype
    def on_change(self, handler: Callable | None) -> None:
        """ Sets the on_change callback.

        :param handler: The on_change callback.
        :type handler: Callable | None
        """
        self._add_event_handler("change", handler)

    # value
    @property
    @beartype
    def value(self) -> str | None:
        """ Returns the key value.

        :return: The key value.
        :rtype: str | None
        """
        return self._get_attr("value")

    @value.setter
    @beartype
    def value(self, value: str | None) -> None:
        """ Sets the key value.

        :param value: The key value.
        :type value: str | None
        """
        self._set_attr("value", value)

    # label
    @property
    @beartype
    def label(self) -> str | None:
        """ Returns the label.

        :return: The label.
        :rtype: str | None
        """
        return self._get_attr("label")

    @label.setter
    @beartype
    def label(self, value: str | None) -> None:
        """ Sets the label.

        :param value: The label.
        :type value: str | None
        """
        self._set_attr("label", value)

    @beartype
    def _get_children(self) -> list[Option] | None:
        """ Returns the list of options

        :return: The list of options.
        :rtype: list[Option] | None
        """
        return self.__options

    # focused
    @property
    @beartype
    def focused(self) -> bool | None:
        """ Returns whether the choice group is focused.

        :return: Whether the choice group is focused.
        :rtype: bool | None
        """
        return self._get_attr("focused")

    @focused.setter
    @beartype
    def focused(self, value: bool | None) -> None:
        """ Sets whether the choice group is focused.

        :param value: Whether the choice group is focused.
        :type value: bool | None
        """
        self._set_attr("focused", value)

    # on_focus
    @property
    @beartype
    def on_focus(self) -> Callable | None:
        """ Returns the on_focus callback.

        :return: The on_focus callback.
        :rtype: Callable | None
        """
        return self._get_event_handler("focus")

    @on_focus.setter
    @beartype
    def on_focus(self, handler: Callable | None) -> None:
        """ Sets the on_focus callback.

        :param handler: The on_focus callback.
        :type handler: Callable | None
        """
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    @beartype
    def on_blur(self) -> Callable | None:
        """ Returns the on_blur callback.

        :return: The on_blur callback.
        :rtype: Callable | None
        """
        return self._get_event_handler("blur")

    @on_blur.setter
    @beartype
    def on_blur(self, handler: Callable | None) -> None:
        """ Sets the on_blur callback.

        :param handler: The on_blur callback.
        :type handler: Callable | None
        """
        self._add_event_handler("blur", handler)
