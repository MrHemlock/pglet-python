""" Module for the Button and MenuItem classes"""

from __future__ import annotations
from typing import Optional, Callable, Iterable, List, Any
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
    :type width: int, optional
    :param height: Height of the button, defaults to None.
    :type height: int, optional
    :param padding: Padding of the button, defaults to None.
    :type padding: int, optional
    :param margin: Margin of the button, defaults to None.
    :type margin: int, optional
    :param visible: Whether the button is visible, defaults to None.
    :type visible: bool, optional
    :param disabled: Whether the button is disabled, defaults to None.
    :type disabled: bool, optional
    """

    def __init__(
        self,
        text: Optional[str] = None,
        id: Optional[str] = None,
        primary: Optional[bool] = None,
        compound: Optional[bool] = None,
        action: Optional[bool] = None,
        toolbar: Optional[bool] = None,
        split: Optional[bool] = None,
        secondary_text: Optional[str] = None,
        url: Optional[str] = None,
        new_window: Optional[bool] = None,
        title: Optional[str] = None,
        icon: Optional[str] = None,
        icon_color: Optional[str] = None,
        focused: Optional[bool] = None,
        data: Optional[str] = None,
        on_click: Optional[Callable] = None,
        on_focus: Optional[Callable] = None,
        on_blur: Optional[Callable] = None,
        menu_items: Optional[Iterable[str]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        padding: Optional[int] = None,
        margin: Optional[int] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
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
        self.__menu_items: List[str] = []
        if menu_items is not None:
            for item in menu_items:
                self.__menu_items.append(item)

    def _get_control_name(self) -> str:
        """ Get the name of the control type.

        :return: The name of the control type.
        :rtype: str
        """
        return "button"

    # menu_items
    @property
    def menu_items(self) -> List[str]:
        """ Get the menu items for the button.

        :return: The menu items
        :rtype: list
        """
        return self.__menu_items

    @menu_items.setter
    def menu_items(self, value: List[str]) -> None:
        """ Set the menu items for the button.

        :param value: The menu items
        :type value: list
        """
        self.__menu_items = value

    # on_click
    @property
    def on_click(self) -> Optional[Callable]:
        """ Get the on_click callback for the button.

        :return: The on_click callback
        :rtype: callable | None
        """
        return self._get_event_handler("click")

    @on_click.setter
    def on_click(self, handler: Optional[Callable]) -> None:
        """ Set the on_click callback.

        :param handler: The on_click callback
        :type handler: callable | None
        """
        self._add_event_handler("click", handler)

    # primary
    @property
    def primary(self) -> Optional[bool]:
        """ Get the primary property for the button.

        :return: The primary property
        :rtype: bool | None
        """
        return self._get_attr("primary")

    @primary.setter
    @beartype
    def primary(self, value: Optional[bool]) -> None:
        """ Set the primary property.

        :param value: The value to set, defaults to None
        :type value: bool | None
        """
        self._set_attr("primary", value)

    # compound
    @property
    def compound(self) -> Optional[bool]:
        """ Get the compound property.

        :return: The compound property
        :rtype: bool | None
        """
        return self._get_attr("compound")

    @compound.setter
    @beartype
    def compound(self, value: Optional[bool]) -> None:
        """ Set the compound property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("compound", value)

    # action
    @property
    def action(self) -> Optional[bool]:
        """ Get the action property.

        :return: The action property
        :rtype: bool | None
        """
        return self._get_attr("action")

    @action.setter
    @beartype
    def action(self, value: Optional[bool]) -> None:
        """ Set the action property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("action", value)

    # toolbar
    @property
    def toolbar(self) -> Optional[bool]:
        """ Get the toolbar property.

        :return: The toolbar property
        :rtype: bool | None
        """
        return self._get_attr("toolbar")

    @toolbar.setter
    @beartype
    def toolbar(self, value: Optional[bool]) -> None:
        """ Set the toolbar property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("toolbar", value)

    # split
    @property
    def split(self) -> Optional[bool]:
        """ Get the split property.

        :return: The split property
        :rtype: bool | None
        """
        return self._get_attr("split")

    @split.setter
    @beartype
    def split(self, value: Optional[bool]) -> None:
        """ Set the split property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("split", value)

    # text
    @property
    def text(self) -> Optional[str]:
        """ Get the text property.

        :return: The text property
        :rtype: str | None
        """
        return self._get_attr("text")

    @text.setter
    def text(self, value: Optional[str]) -> None:
        """ Set the text property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("text", value)

    # secondary_text
    @property
    def secondary_text(self) -> Optional[str]:
        """ Get the secondary_text property.

        :return: The secondary_text property
        :rtype: str | None
        """
        return self._get_attr("secondaryText")

    @secondary_text.setter
    def secondary_text(self, value: Optional[str]) -> None:
        """ Set the secondary_text property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("secondaryText", value)

    # url
    @property
    def url(self) -> Optional[str]:
        """ Get the url property.

        :return: The url property
        :rtype: str
        """
        return self._get_attr("url")

    @url.setter
    def url(self, value: Optional[str]) -> None:
        """ Set the url property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("url", value)

    # new_window
    @property
    def new_window(self) -> Optional[bool]:
        """ Get the new_window property.

        :return: The new_window property
        :rtype: bool | None
        """
        return self._get_attr("newWindow")

    @new_window.setter
    @beartype
    def new_window(self, value: Optional[bool]) -> None:
        """ Set the new_window property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("newWindow", value)

    # title
    @property
    def title(self) -> Optional[str]:
        """ Get the title property.

        :return: The title property
        :rtype: str | None
        """
        return self._get_attr("title")

    @title.setter
    def title(self, value: Optional[str]) -> None:
        """ Set the title property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("title", value)

    # icon
    @property
    def icon(self) -> Optional[str]:
        """ Get the icon property.

        :return: The icon property
        :rtype: str | None
        """
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value: Optional[str]) -> None:
        """ Set the icon property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("icon", value)

    # icon_color
    @property
    def icon_color(self) -> Optional[str]:
        """ Get the icon_color property.

        :return: The icon_color property
        :rtype: str | None
        """
        return self._get_attr("iconColor")

    @icon_color.setter
    def icon_color(self, value: Optional[str]) -> None:
        """ Set the icon_color property.

        :param value: The value to set
        :type value: str | None
        """
        self._set_attr("iconColor", value)

    def _get_children(self) -> List[str]:
        """ Get the menu items of the button.

        :return: The menu items of the button
        :rtype: list
        """
        return self.__menu_items

    # focused
    @property
    def focused(self) -> Optional[bool]:
        """ Get the focused property.

        :return: The focused property
        :rtype: bool | None
        """
        return self._get_attr("focused")

    @focused.setter
    @beartype
    def focused(self, value: Optional[bool]) -> None:
        """ Set the focused property.

        :param value: The value to set
        :type value: bool | None
        """
        self._set_attr("focused", value)

    # on_focus
    @property
    def on_focus(self) -> Optional[Callable]:
        """ Get the on_focus function.

        :return: The on_focus function
        :rtype: callable | None
        """
        return self._get_event_handler("focus")

    @on_focus.setter
    def on_focus(self, handler: Optional[Callable]) -> None:
        """ Set a function to be called when the button is focused.

        :param handler: The function to call
        :type handler: callable | None
        """
        self._add_event_handler("focus", handler)

    # on_blur
    @property
    def on_blur(self) -> Optional[Callable]:
        """ Get the on_blur function.

        :return: The on_blur function
        :rtype: callable | None
        """
        return self._get_event_handler("blur")

    @on_blur.setter
    def on_blur(self, handler: Optional[Callable]) -> None:
        """ Set a function to be called when the button is blurred.

        :param handler: The function to call
        :type handler: callable | None
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
    :param split: Whether or not this menu item is a SplitButton. Defaults to None.
    :type split: bool, optional
    :param divider: Display menu item as a divider. Defaults to None.
    :type divider: bool, optional
    :param on_click: Function to call when the menu item is clicked. Defaults to None.
    :type on_click: callable, optional
    :param sub_menu_items: Sub-menu items to display for this menu item. Defaults to None.
    :type sub_menu_items: list, optional
    :param width: Width of the menu item. Defaults to None.
    :type width: int, optional
    :param height: Height of the menu item. Defaults to None.
    :type height: int, optional
    :param padding: Padding of the menu item. Defaults to None.
    :type padding: int, optional
    :param margin: Margin of the menu item. Defaults to None.
    :type margin: int, optional
    :param visible: Whether or not the menu item is visible. Defaults to None.
    :type visible: bool, optional
    :param disabled: Whether or not the menu item is disabled. Defaults to None.
    :type disabled: bool, optional
    :param data: Arbitrary data to attach to the menu item. Defaults to None.
    :type data: any, optional
    """

    def __init__(
        self,
        text: Optional[str] = None,
        id: Optional[str] = None,
        secondary_text: Optional[str] = None,
        url: Optional[str] = None,
        new_window: Optional[bool] = None,
        icon: Optional[str] = None,
        icon_color: Optional[str] = None,
        icon_only: Optional[bool] = None,
        split: Optional[bool] = None,
        divider: Optional[bool] = None,
        on_click: Optional[Callable] = None,
        sub_menu_items: Optional[List[MenuItem]] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        padding: Optional[int] = None,
        margin: Optional[int] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Optional[Any] = None,
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
        self.__sub_menu_items: List[MenuItem] = []
        if sub_menu_items is not None:
            for item in sub_menu_items:
                self.__sub_menu_items.append(item)

    def _get_control_name(self) -> str:
        """ Get the name of the control type.

        :return: The name of the control type.
        :rtype: str
        """
        return "item"

    # on_click
    @property
    def on_click(self) -> Optional[Callable]:
        """ Get the on_click function.

        :return: The on_click function
        :rtype: callable | None
        """
        return self._get_event_handler("click")

    @on_click.setter
    def on_click(self, handler: Optional[Callable]) -> None:
        """ Set a function to be called when the menu item is clicked.

        :param handler: The function to call
        :type handler: callable | None
        """
        self._add_event_handler("click", handler)

    # sub_menu_items
    @property
    def sub_menu_items(self) -> List[MenuItem]:
        """ Get the sub menu items.

        :return: The sub menu items
        :rtype: list
        """
        return self.__sub_menu_items

    @sub_menu_items.setter
    def sub_menu_items(self, value: List[MenuItem]) -> None:
        """ Set the sub menu items.

        :param value: The list of sub menu items
        :type value: list
        """
        self.__sub_menu_items = value

    # text
    @property
    def text(self) -> Optional[str]:
        """ Get the text.

        :return: The text
        :rtype: str | None
        """
        return self._get_attr("text")

    @text.setter
    def text(self, value: Optional[str]) -> None:
        """ Set the text.

        :param value: The text
        :type value: str | None
        """
        self._set_attr("text", value)

    # secondary_text
    @property
    def secondary_text(self) -> Optional[str]:
        """ Get the secondary text.

        :return: The secondary text
        :rtype: str | None
        """
        return self._get_attr("secondaryText")

    @secondary_text.setter
    def secondary_text(self, value: Optional[str]) -> None:
        """ Set the secondary text.

        :param value: The secondary text
        :type value: str | None
        """
        self._set_attr("secondaryText", value)

    # url
    @property
    def url(self) -> Optional[str]:
        """ Get the url.

        :return: The url
        :rtype: str | None
        """
        return self._get_attr("url")

    @url.setter
    def url(self, value: Optional[str]) -> None:
        """ Set the url.

        :param value: The url
        :type value: str | None
        """
        self._set_attr("url", value)

    # new_window
    @property
    def new_window(self) -> Optional[bool]:
        """ Get the new window attribute.

        :return: The new window attribute
        :rtype: bool | None
        """
        return self._get_attr("newWindow")

    @new_window.setter
    @beartype
    def new_window(self, value: Optional[bool]) -> None:
        """ Set the new window attribute.

        :param value: The new window attribute
        :type value: bool | None
        """
        self._set_attr("newWindow", value)

    # icon
    @property
    def icon(self) -> Optional[str]:
        """ Get the icon.

        :return: The icon
        :rtype: str | None
        """
        return self._get_attr("icon")

    @icon.setter
    def icon(self, value: Optional[str]) -> None:
        """ Set the icon.

        :param value: The icon
        :type value: str | None
        """
        self._set_attr("icon", value)

    # icon_color
    @property
    def icon_color(self) -> Optional[str]:
        """ Get the icon color.

        :return: The icon color
        :rtype: str | None
        """
        return self._get_attr("iconColor")

    @icon_color.setter
    def icon_color(self, value: Optional[str]) -> None:
        """ Set the icon color.

        :param value: The icon color
        :type value: str | None
        """
        self._set_attr("iconColor", value)

    # icon_only
    @property
    def icon_only(self) -> Optional[bool]:
        """ Get the icon only attribute.

        :return: The icon only attribute
        :rtype: bool | None
        """
        return self._get_attr("iconOnly")

    @icon_only.setter
    @beartype
    def icon_only(self, value: Optional[bool]) -> None:
        """ Set the icon only attribute.

        :param value: The icon only attribute
        :type value: bool | None
        """
        self._set_attr("iconOnly", value)

    # split
    @property
    def split(self) -> Optional[bool]:
        """ Get the split attribute.

        :return: The split attribute
        :rtype: bool | None
        """
        return self._get_attr("split")

    @split.setter
    @beartype
    def split(self, value: Optional[bool]) -> None:
        """ Set the split attribute.

        :param value: The split attribute
        :type value: bool | None
        """
        self._set_attr("split", value)

    # divider
    @property
    def divider(self) -> Optional[bool]:
        """ Get the divider attribute.

        :return: The divider attribute
        :rtype: bool | None
        """
        return self._get_attr("divider")

    @divider.setter
    @beartype
    def divider(self, value: Optional[bool]) -> None:
        """ Set the divider attribute.

        :param value: The divider attribute
        :type value: bool | None
        """
        self._set_attr("divider", value)

    def _get_children(self) -> List[MenuItem]:
        """ Private function to get the sub menu items.

        :return: The sub menu items
        :rtype: list
        """
        return self.__sub_menu_items
