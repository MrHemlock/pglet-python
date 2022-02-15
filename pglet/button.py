""" Module for the Button and MenuItem classes"""

from __future__ import annotations
from typing import Any
from collections.abc import Callable, Iterable
from beartype import beartype
from pglet.control import Control


class Button(Control):
    """ Creates a button on the page.

    :param text: The text displayed on a button, defaults to None.
    :type text: str, optional
    :param id: The id of the button, defaults to None.
    :type id: str, optional
    :param primary: The button with a theme color background (usually, there is
        only one primary button on a form), defaults to None.
    :type primary: bool, optional
    :param compound: Render compound button with primary and secondaryText on a
        second line, defaults to None.
    :type compound: bool, optional
    :param action: Render button as a link without a border, defaults to None.
    :type action: bool, optional
    :param toolbar: Render toolbar-like button, defaults to None.
    :type toolbar: bool, optional
    :param split: If set to true, and if menu items are provided, the button will
        render as a SplitButton,
        defaults to None.
    :type split: bool, optional
    :param secondary_text: Description of the action this button takes
        (only used for compound buttons), defaults to None.
    :type secondary_text: str, optional
    :param url: If provided, the button will be rendered as a link, defaults to None.
    :type url: str, optional
    :param new_window: Whether to open link in a new browser window, defaults to None.
    :type new_window: bool, optional
    :param title: Popup hint for the button, defaults to None.
    :type title: str, optional
    :param icon: Icon shown in the button, defaults to None.
    :type icon: str, optional
    :param icon_color: Icon color, defaults to None.
    :type icon_color: str, optional
    :param focused: Whether the button is focused, defaults to None.
    :type focused: bool, optional
    :param data: data to attach to the button, defaults to None.
    :type data: Any, optional
    :param on_click: function to call when the button is clicked, defaults to None.
    :type on_click: callable, None, optional
    :param on_focus: function to call when the button is focused, defaults to None.
    :type on_focus: callable, None, optional
    :param on_blur: function to call when the button is blurred, defaults to None.
    :type on_blur: callable, None, optional
    :param menu_items: Menu items to show when the button is clicked, defaults to None.
    :type menu_items: iterable of strings, optional
    :param width: Width of the button, defaults to None.
    :type width: int | str | None, optional
    :param height: Height of the button, defaults to None.
    :type height: int | str | None, optional
    :param padding: Padding of the button, defaults to None.
    :type padding: int | str | None, optional
    :param margin: Margin of the button, defaults to None.
    :type margin: int | str | None, optional
    :param visible: Whether the button is visible, defaults to None.
    :type visible: bool, optional
    :param disabled: Whether the button is disabled, defaults to None.
    :type disabled: bool, optional
    """

    def __init__(
        self,
        text: str | None = None,
        id: str | None = None,
        primary: bool | None = None,
        compound: bool | None = None,
        action: bool | None = None,
        toolbar: bool | None = None,
        split: bool | None = None,
        secondary_text: str | None = None,
        url: str | None = None,
        new_window: bool | None = None,
        title: str | None = None,
        icon: str | None = None,
        icon_color: str | None = None,
        focused: bool | None = None,
        data: str | None = None,
        on_click: Callable | None = None,
        on_focus: Callable | None = None,
        on_blur: Callable | None = None,
        menu_items: Iterable[str] | None = None,
        width: int | str | None = None,
        height: int | str | None = None,
        padding: int | str | None = None,
        margin: int | str | None = None,
        visible: bool | None = None,
        disabled: bool | None = None,
    ) -> None:
        """Constructor for the button class."""
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

        self.primary = primary
        self.compound = compound
        self.action = action
        self.toolbar = toolbar
        self.split = split
        self.text = text
        self.secondary_text = secondary_text
        self.url = url
        self.new_window = new_window
        self.title = title
        self.icon = icon
        self.icon_color = icon_color
        self.focused = focused
        self.on_click = on_click
        self.on_focus = on_focus
        self.on_blur = on_blur
        self.__menu_items: list[str] = []
        if menu_items is not None:
            for item in menu_items:
                self.__menu_items.append(item)

    @beartype
    def _get_control_name(self) -> str:
        """ Get the name of the control type.

        :return: The name of the control type.
        :rtype: str
        """
        return "button"

    # menu_items
    @property
    @beartype
    def menu_items(self) -> list[str]:
        """ Get the menu items for the button.

        :return: The menu items
        :rtype: list
        """
        return self.__menu_items

    @menu_items.setter
    @beartype
    def menu_items(self, value: list[str]) -> None:
        """ Set the menu items for the button.

        :param value: The menu items
        :type value: list
        """
        self.__menu_items = value

    # on_click
    @property
    @beartype
    def on_click(self) -> Callable | None:
        """ Get the on_click callback for the button.

        :return: The on_click callback
        :rtype: callable | None
        """
        return self._get_event_handler("click")

    @on_click.setter
    @beartype
    def on_click(self, handler: Callable | None) -> None:
        """ Set the on_click callback.

        :param handler: The on_click callback
        :type handler: callable | None
        """
        self._add_event_handler("click", handler)

    # primary
    @property
    @beartype
    def primary(self) -> bool | None:
        """ Get the primary property for the button.

        :return: The primary property
        :rtype: bool | None
        """
        return self._get_attr("primary")

    @primary.setter
    @beartype
    def primary(self, value: bool | None) -> None:
        """ Set the primary property.

        :param value: The value to set, defaults to None
        :type value: bool | None
        """
        self._set_attr("primary", value)

    # compound
    @property
    @beartype
    def compound(self) -> bool | None:
        """ Get the compound property.

        :return: The compound property
        :rtype: bool | None
        """
        return self._get_attr("compound")

    @compound.setter
    @beartype
    def compound(self, value: bool | None) -> None:
        """ Set the compound property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("compound", value)

    # action
    @property
    @beartype
    def action(self) -> bool | None:
        """ Get the action property.

        :return: The action property
        :rtype: bool | None
        """
        return self._get_attr("action")

    @action.setter
    @beartype
    def action(self, value: bool | None) -> None:
        """ Set the action property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("action", value)

    # toolbar
    @property
    @beartype
    def toolbar(self) -> bool | None:
        """ Get the toolbar property.

        :return: The toolbar property
        :rtype: bool | None
        """
        return self._get_attr("toolbar")

    @toolbar.setter
    @beartype
    def toolbar(self, value: bool | None) -> None:
        """ Set the toolbar property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("toolbar", value)

    # split
    @property
    @beartype
    def split(self) -> bool | None:
        """ Get the split property.

        :return: The split property
        :rtype: bool | None
        """
        return self._get_attr("split")

    @split.setter
    @beartype
    def split(self, value: bool | None) -> None:
        """ Set the split property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("split", value)

    # text
    @property
    @beartype
    def text(self) -> str | None:
        """ Get the text property.

        :return: The text property
        :rtype: str | None
        """
        return self._get_attr("text")

    @text.setter
    @beartype
    def text(self, value: str | None) -> None:
        """ Set the text property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("text", value)

    # secondary_text
    @property
    @beartype
    def secondary_text(self) -> str | None:
        """ Get the secondary_text property.

        :return: The secondary_text property
        :rtype: str | None
        """
        return self._get_attr("secondaryText")

    @secondary_text.setter
    @beartype
    def secondary_text(self, value: str | None) -> None:
        """ Set the secondary_text property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("secondaryText", value)

    # url
    @property
    @beartype
    def url(self) -> str | None:
        """ Get the url property.

        :return: The url property
        :rtype: str
        """
        return self._get_attr("url")

    @url.setter
    @beartype
    def url(self, value: str | None) -> None:
        """ Set the url property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("url", value)

    # new_window
    @property
    @beartype
    def new_window(self) -> bool | None:
        """ Get the new_window property.

        :return: The new_window property
        :rtype: bool | None
        """
        return self._get_attr("newWindow")

    @new_window.setter
    @beartype
    def new_window(self, value: bool | None) -> None:
        """ Set the new_window property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("newWindow", value)

    # title
    @property
    @beartype
    def title(self) -> str | None:
        """ Get the title property.

        :return: The title property
        :rtype: str | None
        """
        return self._get_attr("title")

    @title.setter
    @beartype
    def title(self, value: str | None) -> None:
        """ Set the title property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("title", value)

    # icon
    @property
    @beartype
    def icon(self) -> str | None:
        """ Get the icon property.

        :return: The icon property
        :rtype: str | None
        """
        return self._get_attr("icon")

    @icon.setter
    @beartype
    def icon(self, value: str | None) -> None:
        """ Set the icon property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("icon", value)

    # icon_color
    @property
    @beartype
    def icon_color(self) -> str | None:
        """ Get the icon_color property.

        :return: The icon_color property
        :rtype: str | None
        """
        return self._get_attr("iconColor")

    @icon_color.setter
    @beartype
    def icon_color(self, value: str | None) -> None:
        """ Set the icon_color property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("iconColor", value)

    @beartype
    def _get_children(self) -> list[str]:
        """ Get the menu items of the button.

        :return: The menu items of the button
        :rtype: list
        """
        return self.__menu_items

    # focused
    @property
    @beartype
    def focused(self) -> bool | None:
        """ Get the focused property.

        :return: The focused property
        :rtype: bool | None
        """
        return self._get_attr("focused")

    @focused.setter
    @beartype
    def focused(self, value: bool | None) -> None:
        """ Set the focused property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("focused", value)

    # on_focus
    @property
    @beartype
    def on_focus(self) -> Callable | None:
        """ Get the on_focus function.

        :return: The on_focus function
        :rtype: Callable | None
        """
        return self._get_event_handler("focus")

    @on_focus.setter
    @beartype
    def on_focus(self, handler: Callable | None) -> None:
        """ Set a function to be called when the button is focused.

        :param handler: The function to call
        :type handler: Callable | None
        """
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    @beartype
    def on_blur(self) -> Callable | None:
        """ Get the on_blur function.

        :return: The on_blur function
        :rtype: Callable | None
        """
        return self._get_event_handler("blur")

    @on_blur.setter
    @beartype
    def on_blur(self, handler: Callable | None) -> None:
        """ Set a function to be called when the button is blurred.

        :param handler: The function to call
        :type handler: Callable | None
        """
        self._add_event_handler("blur", handler)


class MenuItem(Control):
    """ Represents a menu item.

    :param text: Text of the menu item. If a standard hyphen (-) is passed
        in, then the item will be rendered as a divider. If a dash must appear
        as text, use an emdash (—), figuredash (‒), or minus symbol (−) instead.
        Defaults to None.
    :type text: str, optional
    :param id: The id of the menu item. Defaults to None.
    :type id: str, optional
    :param secondary_text: Secondary description for the menu item to display. Defaults to None.
    :type secondary_text: str, optional
    :param url: URL to navigate to for this menu item. Defaults to None.
    :type url: str, optional
    :param new_window: Whether to open the URL in a new browser window. Defaults to None.
    :type new_window: bool, optional
    :param icon: An optional icon to display next to the item. Defaults to None.
    :type icon: str, optional
    :param icon_color: The color of the icon. Defaults to None.
    :type icon_color: str, optional
    :param icon_only: Show only an icon for this item, not text. Does not apply if item
        is in the overflow. Defaults to None.
    :type icon_only: bool, optional
    :param split: Whether this menu item is a SplitButton. Defaults to None.
    :type split: bool, optional
    :param divider: Display menu item as a divider. Defaults to None.
    :type divider: bool, optional
    :param on_click: Function to call when the menu item is clicked. Defaults to None.
    :type on_click: callable, optional
    :param sub_menu_items: Sub-menu items to display for this menu item. Defaults to None.
    :type sub_menu_items: list, optional
    :param width: Width of the menu item. Defaults to None.
    :type width: int | str | None, optional
    :param height: Height of the menu item. Defaults to None.
    :type height: int | str | None, optional
    :param padding: Padding of the menu item. Defaults to None.
    :type padding: int | str | None, optional
    :param margin: Margin of the menu item. Defaults to None.
    :type margin: int | str | None, optional
    :param visible: Whether the menu item is visible. Defaults to None.
    :type visible: bool, optional
    :param disabled: Whether the menu item is disabled. Defaults to None.
    :type disabled: bool, optional
    :param data: Arbitrary data to attach to the menu item. Defaults to None.
    :type data: Any, optional
    """

    def __init__(
        self,
        text: str | None = None,
        id: str | None = None,
        secondary_text: str | None = None,
        url: str | None = None,
        new_window: bool | None = None,
        icon: str | None = None,
        icon_color: str | None = None,
        icon_only: bool | None = None,
        split: bool | None = None,
        divider: bool | None = None,
        on_click: Callable | None = None,
        sub_menu_items: list['MenuItem'] | None = None,
        width: int | str | None = None,
        height: int | str | None = None,
        padding: int | str | None = None,
        margin: int | str | None = None,
        visible: bool | None = None,
        disabled: bool | None = None,
        data: Any = None,
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

        self.text = text
        self.secondary_text = secondary_text
        self.url = url
        self.new_window = new_window
        self.icon = icon
        self.icon_color = icon_color
        self.icon_only = icon_only
        self.split = split
        self.divider = divider
        self.on_click = on_click
        self.__sub_menu_items: list['MenuItem'] = []
        if sub_menu_items is not None:
            for item in sub_menu_items:
                self.__sub_menu_items.append(item)

    @beartype
    def _get_control_name(self) -> str:
        """ Get the name of the control type.

        :return: The name of the control type.
        :rtype: str
        """
        return "item"

    # on_click
    @property
    @beartype
    def on_click(self) -> Callable | None:
        """ Get the on_click function.

        :return: The on_click function
        :rtype: Callable | None
        """
        return self._get_event_handler("click")

    @on_click.setter
    @beartype
    def on_click(self, handler: Callable | None) -> None:
        """ Set a function to be called when the menu item is clicked.

        :param handler: The function to call
        :type handler: Callable | None
        """
        self._add_event_handler("click", handler)

    # sub_menu_items
    @property
    @beartype
    def sub_menu_items(self) -> list['MenuItem']:
        """ Get the sub menu items.

        :return: The sub menu items
        :rtype: list
        """
        return self.__sub_menu_items

    @sub_menu_items.setter
    @beartype
    def sub_menu_items(self, value: list['MenuItem']) -> None:
        """ Set the sub menu items.

        :param value: The list of sub menu items
        :type value: list
        """
        self.__sub_menu_items = value

    # text
    @property
    @beartype
    def text(self) -> str | None:
        """ Get the text.

        :return: The text
        :rtype: str | None
        """
        return self._get_attr("text")

    @text.setter
    @beartype
    def text(self, value: str | None) -> None:
        """ Set the text.

        :param value: The text
        :type value: str | None
        """
        self._set_attr("text", value)

    # secondary_text
    @property
    @beartype
    def secondary_text(self) -> str | None:
        """ Get the secondary text.

        :return: The secondary text
        :rtype: str | None
        """
        return self._get_attr("secondaryText")

    @secondary_text.setter
    @beartype
    def secondary_text(self, value: str | None) -> None:
        """ Set the secondary text.

        :param value: The secondary text
        :type value: str | None
        """
        self._set_attr("secondaryText", value)

    # url
    @property
    @beartype
    def url(self) -> str | None:
        """ Get the url.

        :return: The url
        :rtype: str | None
        """
        return self._get_attr("url")

    @url.setter
    @beartype
    def url(self, value: str | None) -> None:
        """ Set the url.

        :param value: The url
        :type value: str | None
        """
        self._set_attr("url", value)

    # new_window
    @property
    @beartype
    def new_window(self) -> bool | None:
        """ Get the new window attribute.

        :return: The new window attribute
        :rtype: bool | None
        """
        return self._get_attr("newWindow")

    @new_window.setter
    @beartype
    def new_window(self, value: bool | None) -> None:
        """ Set the new window attribute.

        :param value: The new window attribute
        :type value: bool | None
        """
        self._set_attr("newWindow", value)

    # icon
    @property
    @beartype
    def icon(self) -> str | None:
        """ Get the icon.

        :return: The icon
        :rtype: str | None
        """
        return self._get_attr("icon")

    @icon.setter
    @beartype
    def icon(self, value: str | None) -> None:
        """ Set the icon.

        :param value: The icon
        :type value: str | None
        """
        self._set_attr("icon", value)

    # icon_color
    @property
    @beartype
    def icon_color(self) -> str | None:
        """ Get the icon color.

        :return: The icon color
        :rtype: str | None
        """
        return self._get_attr("iconColor")

    @icon_color.setter
    @beartype
    def icon_color(self, value: str | None) -> None:
        """ Set the icon color.

        :param value: The icon color
        :type value: str | None
        """
        self._set_attr("iconColor", value)

    # icon_only
    @property
    @beartype
    def icon_only(self) -> bool | None:
        """ Get the icon only attribute.

        :return: The icon only attribute
        :rtype: bool | None
        """
        return self._get_attr("iconOnly")

    @icon_only.setter
    @beartype
    def icon_only(self, value: bool | None) -> None:
        """ Set the icon only attribute.

        :param value: The icon only attribute
        :type value: bool | None
        """
        self._set_attr("iconOnly", value)

    # split
    @property
    @beartype
    def split(self) -> bool | None:
        """ Get the split attribute.

        :return: The split attribute
        :rtype: bool | None
        """
        return self._get_attr("split")

    @split.setter
    @beartype
    def split(self, value: bool | None) -> None:
        """ Set the split attribute.

        :param value: The split attribute
        :type value: bool | None
        """
        self._set_attr("split", value)

    # divider
    @property
    @beartype
    def divider(self) -> bool | None:
        """ Get the divider attribute.

        :return: The divider attribute
        :rtype: bool | None
        """
        return self._get_attr("divider")

    @divider.setter
    @beartype
    def divider(self, value: bool | None) -> None:
        """ Set the divider attribute.

        :param value: The divider attribute
        :type value: bool | None
        """
        self._set_attr("divider", value)

    @beartype
    def _get_children(self) -> list['MenuItem']:
        """ Private function to get the sub menu items.

        :return: The sub menu items
        :rtype: list
        """
        return self.__sub_menu_items
