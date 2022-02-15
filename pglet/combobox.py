""" Module for the ComboBox and Option classes """

from __future__ import annotations
from beartype.typing import Literal, Any
from collections.abc import Callable, Iterable
from beartype import beartype
from pglet.control import Control


ITEM_TYPE = Literal[None, "normal", "divider", "header", "selectAll", "select_all"]


class Option(Control):
    """ Class for a single option in a ComboBox

    :param key: Option's key. text value will be used instead if key is not specified. Default is None.
    :type key: str | None, optional
    :param text: Option's display text. key value will be used instead if text is not specified. Default is None.
    :type text: str | None, optional
    :param item_type: Type of the option ("normal", "divider", "header", "selectAll", "select_all").
        Default is "normal".
    :type item_type: ITEM_TYPE, optional
    :param disabled: Whether the option is disabled. Default is False.
    :type disabled: bool | None, optional
    """

    def __init__(
            self,
            key: str | None = None,
            text: str | None = None,
            item_type: ITEM_TYPE = None,
            disabled: bool | None = None
    ) -> None:
        """ Initialize the Option object """

        Control.__init__(self)
        assert key is not None or text is not None, "key or text must be specified"
        self.key = key
        self.text = text
        self.item_type = item_type
        self.disabled = disabled

    @beartype
    def _get_control_name(self) -> str:
        """ Get the control name.

        :return: The control name.
        :rtype: str
        """
        return "option"

    # key
    @property
    @beartype
    def key(self) -> str | None:
        """ Get the option's key.

        :return: The option's key.
        :rtype: str | None
        """
        return self._get_attr("key")

    @key.setter
    @beartype
    def key(self, value: str | None) -> None:
        """ Set the option's key.

        :param value: The option's key.
        :type value: str | None
        """
        self._set_attr("key", value)

    # text
    @property
    @beartype
    def text(self) -> str | None:
        """ Get the option's text.

        :return: The option's text.
        :rtype: str | None
        """
        return self._get_attr("text")

    @text.setter
    @beartype
    def text(self, value: str | None) -> None:
        """ Set the option's text.

        :param value: The option's text.
        :type value: str | None
        """
        self._set_attr("text", value)

    # item_type
    @property
    @beartype
    def item_type(self) -> ITEM_TYPE:
        """ Get the option's item type.

        :return: The option's item type.
        :rtype: ITEM_TYPE
        """
        return self._get_attr("itemtype")

    @item_type.setter
    @beartype
    def item_type(self, value: ITEM_TYPE) -> None:
        """ Set the option's item type.

        :param value: The option's item type.
        :type value: ITEM_TYPE
        """
        self._set_attr("itemtype", value)

    # disabled
    @property
    @beartype
    def disabled(self) -> bool | None:
        """ Get the option's disabled state.

        :return: The option's disabled state.
        :rtype: bool | None
        """
        return self._get_attr("disabled")

    @disabled.setter
    @beartype
    def disabled(self, value: bool | None) -> None:
        """ Set the option's disabled state.

        :param value: The option's disabled state.
        :type value: bool | None
        """
        self._set_attr("disabled", value)


class ComboBox(Control):
    """ A combination of a drop-down list or list box and a single-line editable textbox,
    allowing the user to either type a value directly or select one or multiple values from
    the list.

    :param label: Descriptive label for the combo box. Default is None.
    :type label: str | None, optional
    :param id: The id of the combo box. Default is None.
    :type id: str | None, optional
    :param value: Key value of the selected option. Default is None.
    :type value: str | None, list[str], optional
    :param placeholder: Placeholder text. Default is None.
    :type placeholder: str | None, optional
    :param error_message: Error message. Default is None.
    :type error_message: str | None, optional
    :param on_change: Fires when the selected option changes. Default is None.
    :type on_change: Callable | None, optional
    :param on_focus: Fires when the combo box receives focus. Default is None.
    :type on_focus: Callable | None, optional
    :param on_blur: Fires when the combo box loses focus. Default is None.
    :type on_blur: Callable | None, optional
    :param options: Options for the combo box. Default is None.
    :type options: Iterable[Option] | None, optional
    :param width: Width of the combo box. Default is None.
    :type width: int | str | None, optional
    :param height: Height of the combo box. Default is None.
    :type height: int | str | None, optional
    :param padding: Padding for the combo box. Default is None.
    :type padding: int | str | None, optional
    :param margin: Margin for the combo box. Default is None.
    :type margin: int | str | None, optional
    :param visible: Whether the combo box is visible. Default is True.
    :type visible: bool | None, optional
    :param disabled: Whether the combo box is disabled. Default is False.
    :type disabled: bool | None, optional
    :param focused: Whether the combo box is focused. Default is False.
    :type focused: bool | None, optional
    :param multi_select: Whether the combo box is multi-select. Default is False.
    :type multi_select: bool | None, optional
    :param allow_free_form: Whether the combo box allows free form text. Default is False.
    :type allow_free_form: bool | None, optional
    :param auto_complete: Whether the combo box auto completes. Default is False.
    :type auto_complete: bool | None, optional
    :param data: Additional data attached to the control. The value is passed in change event data
        along with a ComboBox selected value. Defaults to None.
    :type data: Any, optional
    """

    def __init__(
        self,
        label: str | None = None,
        id: str | None = None,
        value: str | list[str] | None = None,
        placeholder: str | None = None,
        error_message: str | None = None,
        on_change: Callable | None = None,
        on_focus: Callable | None = None,
        on_blur: Callable | None = None,
        options: Iterable[Option] | None = None,
        width: int | str | None = None,
        height: int | str | None = None,
        padding: int | str | None = None,
        margin: int | str | None = None,
        visible: bool | None = None,
        disabled: bool | None = None,
        focused: bool | None = None,
        multi_select: bool | None = None,
        allow_free_form: bool | None = None,
        auto_complete: bool | None = None,
        data: Any = None,
    ) -> None:
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
        self.label = label
        self.value = value
        self.placeholder = placeholder
        self.error_message = error_message
        self.focused = focused
        self.multi_select = multi_select
        self.allow_free_form = allow_free_form
        self.auto_complete = auto_complete
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
        return "combobox"

    # options
    @property
    @beartype
    def options(self) -> list[Option] | None:
        """ Returns the options for the combo box.

        :return: The options for the combo box.
        :rtype: list[Option] | None
        """
        return self.__options

    @options.setter
    @beartype
    def options(self, value: list[Option] | None) -> None:
        """ Sets the options for the combo box.

        :param value: The options for the combo box.
        :type value: list[Option] | None
        """
        self.__options = value

    # on_change
    @property
    @beartype
    def on_change(self) -> Callable | None:
        """ Returns the on change callback.

        :return: The on change callback.
        :rtype: Callable | None
        """
        return self._get_event_handler("change")

    @on_change.setter
    @beartype
    def on_change(self, handler: Callable | None) -> None:
        """ Sets the on change callback.

        :param handler: The on change callback.
        :type handler: Callable | None
        """
        self._add_event_handler("change", handler)

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

    # value
    @property
    @beartype
    def value(self) -> str | list[str] | None:
        """ Returns the value.

        :return: The value.
        :rtype: str | list[str] | None
        """
        v = self._get_attr("value")
        if v and self.multi_select:
            return [x.strip() for x in v.split(",")]
        return v

    @value.setter
    @beartype
    def value(self, value: str | list[str] | None) -> None:
        """ Sets the value.

        :param value: The value.
        :type value: str | list[str] | None
        """
        if isinstance(value, list):
            value = ",".join(value)
        self._set_attr("value", value)

    # placeholder
    @property
    @beartype
    def placeholder(self) -> str | None:
        """ Returns the placeholder.

        :return: The placeholder.
        :rtype: str | None
        """
        return self._get_attr("placeholder")

    @placeholder.setter
    @beartype
    def placeholder(self, value: str | None) -> None:
        """ Sets the placeholder.

        :param value: The placeholder.
        :type value: str | None
        """
        self._set_attr("placeholder", value)

    # error_message
    @property
    @beartype
    def error_message(self) -> str | None:
        """ Returns the error message.

        :return: The error message.
        :rtype: str | None
        """
        return self._get_attr("errorMessage")

    @error_message.setter
    @beartype
    def error_message(self, value: str | None) -> None:
        """ Sets the error message.

        :param value: The error message.
        :type value: str | None
        """
        self._set_attr("errorMessage", value)

    @beartype
    def _get_children(self) -> list[Option] | None:
        """ Returns the options for the combo box.

        :return: The options for the combo box.
        :rtype: list[Option] | None
        """
        return self.__options

    # focused
    @property
    @beartype
    def focused(self) -> bool | None:
        """ Returns the focused state.

        :return: The focused state.
        :rtype: bool | None
        """
        return self._get_attr("focused")

    @focused.setter
    @beartype
    def focused(self, value: bool | None) -> None:
        """ Sets the focused state.

        :param value: The focused state.
        :type value: bool | None
        """
        self._set_attr("focused", value)

    # multi_select
    @property
    @beartype
    def multi_select(self) -> bool | None:
        """ Returns the multi select state.

        :return: The multi select state.
        :rtype: bool | None
        """
        return self._get_attr("multiselect")

    @multi_select.setter
    @beartype
    def multi_select(self, value: bool | None) -> None:
        """ Sets the multi select state.

        :param value: The multi select state.
        :type value: bool | None
        """
        self._set_attr("multiselect", value)

    # allow_free_form
    @property
    @beartype
    def allow_free_form(self) -> bool | None:
        """ Returns the allow free form state.

        :return: The allow free form state.
        :rtype: bool | None
        """
        return self._get_attr("allowfreeform")

    @allow_free_form.setter
    @beartype
    def allow_free_form(self, value: bool | None) -> None:
        """ Sets the allow free form state.

        :param value: The allow free form state.
        :type value: bool | None
        """
        self._set_attr("allowfreeform", value)

    # auto_complete
    @property
    @beartype
    def auto_complete(self) -> bool | None:
        """ Returns the auto complete state.

        :return: The auto complete state.
        :rtype: bool | None
        """
        return self._get_attr("autocomplete")

    @auto_complete.setter
    @beartype
    def auto_complete(self, value: bool | None) -> None:
        """ Sets the auto complete state.

        :param value: The auto complete state.
        :type value: bool | None
        """
        self._set_attr("autocomplete", value)

    # on_focus
    @property
    @beartype
    def on_focus(self) -> Callable | None:
        """ Returns the on focus event.

        :return: The on focus event.
        :rtype: Callable | None
        """
        return self._get_event_handler("focus")

    @on_focus.setter
    @beartype
    def on_focus(self, handler: Callable | None) -> None:
        """ Sets the on focus event.

        :param handler: The on focus event.
        :type handler: Callable | None
        """
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    @beartype
    def on_blur(self) -> Callable | None:
        """ Returns the on blur event.

        :return: The on blur event.
        :rtype: Callable | None
        """
        return self._get_event_handler("blur")

    @on_blur.setter
    @beartype
    def on_blur(self, handler: Callable | None) -> None:
        """ Sets the on blur event.

        :param handler: The on blur event.
        :type handler: Callable | None
        """
        self._add_event_handler("blur", handler)
