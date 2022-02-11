""" Module for the Callout class """

from typing import Literal, Optional, Callable, List, Iterable
from beartype import beartype
from pglet.control import Control

POSITION = Literal[
    None,
    "topLeft",
    "topCenter",
    "topRight",
    "topAuto",
    "bottomLeft",
    "bottomCenter",
    "bottomRight",
    "bottomAuto",
    "leftTop",
    "leftCenter",
    "leftBottom",
    "rightTop",
    "rightCenter",
    "rightBottom",
]


class Callout(Control):
    """ An anchored tip that can be used to teach people or guide them through
    the app without blocking them.

    :param id: callout id, defaults to None
    :type id: str, optional
    :param target: Id of the control to which the collout is attached. Defaults
        to None
    :type target: str, optional
    :param position: The position of the callout relative to the target control:
        topLeft, topCenter, topRight, topAuto, bottomLeft, bottomCenter, bottomRight,
        bottomAuto (default), leftTop, leftCenter, leftBottom, rightTop, rightCenter,
        rightBottom. Defaults to BottomAuto
    :type position: str, optional
    :param gap: The gap between the callout and the target control. Defaults to 0
    :type gap: int, optional
    :param beak: Whether the beak is visible. Defaults to True
    :type beak: bool, optional
    :param beak_width: Beak width. Defaults to 16
    :type beak_width: int, optional
    :param page_padding: The minimum distance the callout will be away from the edge
        of the screen. Defaults to 8
    :type page_padding: int, optional
    :param focus: If true then the callout will attempt to focus the first focusable
        element that it contains. If it doesn't find an element, no focus will be set
        and the method will return false. This means that it's the contents responsibility
        to either set focus or have focusable items. Defaults to False.
    :type focus: bool, optional
    :param cover: If true the position returned will have the menu element cover the target.
        If false then it will position next to the target. Defaults to False.
    :type cover: bool, optional
    :param visible: Whether the callout is visible or not. Defaults to False.
    :type visible: bool, optional
    :param controls: List of controls to add to the callout. Defaults to None.
    :type controls: list, optional
    :param on_dismiss: Fires when the callout is dismissed. Callout is dismissed when a
        user clicks outside of the callout area. Defaults to None.
    :type on_dismiss: callable, optional
    :param width: The width of the callout. Defaults to None.
    :type width: int, optional
    :param height: The height of the callout. Defaults to None.
    :type height: int, optional
    :param padding: The padding of the callout. Defaults to None.
    :type padding: int, optional
    :param margin: The margin of the callout. Defaults to None.
    :type margin: int, optional
    :param disabled: Whether the callout is disabled or not. Defaults to False.
    :type disabled: bool, optional
    """

    def __init__(
        self,
        id: Optional[str] = None,
        target: Optional[str] = None,
        position: POSITION = None,
        gap: Optional[int] = None,
        beak: Optional[bool] = None,
        beak_width: Optional[int] = None,
        page_padding: Optional[int] = None,
        focus: Optional[bool] = None,
        cover: Optional[bool] = None,
        visible: Optional[bool] = None,
        controls: Optional[Iterable[str]] = None,
        on_dismiss: Optional[Callable] = None,
        width: Optional[int] = None,
        height: Optional[int] = None,
        padding: Optional[int] = None,
        margin: Optional[int] = None,
        disabled: Optional[bool] = None,
    ) -> None:
        """ Initialize a new Callout. """

        Control.__init__(
            self,
            id=id,
            width=width,
            height=height,
            padding=padding,
            margin=margin,
            visible=visible,
            disabled=disabled,
        )

        self.target = target
        self.position = position
        self.gap = gap
        self.beak = beak
        self.beak_width = beak_width
        self.page_padding = page_padding
        self.focus = focus
        self.cover = cover
        self.on_dismiss = on_dismiss
        self.__controls: List[str] = []
        if controls is not None:
            for control in controls:
                self.__controls.append(control)

    def _get_control_name(self) -> str:
        """ Get the name of the control type.

        :return: The name of the control type.
        :rtype: str
        """
        return "callout"

    # controls
    @property
    def controls(self) -> List[str]:
        """ Get the controls.

        :return: The list of controls.
        :rtype: list
        """
        return self.__controls

    @controls.setter
    def controls(self, value: List[str]) -> None:
        """ Set the controls.

        :param value: The list of controls.
        :type value: list
        """
        self.__controls = value

    # on_dismiss
    @property
    def on_dismiss(self) -> Callable:
        """ Get the on_dismiss callback.

        :return: The on_dismiss callback.
        :rtype: callable
        """
        return self._get_event_handler("dismiss")

    @on_dismiss.setter
    def on_dismiss(self, handler: Callable) -> None:
        """ Set the on_dismiss callback.

        :param handler: The on_dismiss callback.
        :type handler: callable
        """
        self._add_event_handler("dismiss", handler)

    # target
    @property
    def target(self) -> Optional[str]:
        """ Get the target.

        :return: The target.
        :rtype: str
        """
        return self._get_attr("target")

    @target.setter
    def target(self, value: Optional[str]) -> None:
        """ Set the target.

        :param value: The target.
        :type value: str
        """
        self._set_attr("target", value)

    # position
    @property
    def position(self) -> Optional[POSITION]:
        """ Get the position.

        :return: The position.
        :rtype: str
        """
        return self._get_attr("position")

    @position.setter
    @beartype
    def position(self, value: POSITION) -> None:
        """ Set the position.

        :param value: The position.
        :type value: str
        """
        self._set_attr("position", value)

    # gap
    @property
    def gap(self) -> Optional[int]:
        """ Get the gap.

        :return: The gap.
        :rtype: int
        """
        return self._get_attr("gap")

    @gap.setter
    @beartype
    def gap(self, value: Optional[int]) -> None:
        """ Set the gap.

        :param value: The gap.
        :type value: int
        """
        self._set_attr("gap", value)

    # beak
    @property
    def beak(self) -> Optional[bool]:
        """ Get the beak.

        :return: The beak.
        :rtype: bool
        """
        return self._get_attr("beak")

    @beak.setter
    @beartype
    def beak(self, value: Optional[bool]) -> None:
        """ Set the beak.

        :param value: The beak.
        :type value: bool
        """
        self._set_attr("beak", value)

    # beak_width
    @property
    def beak_width(self) -> Optional[int]:
        """ Get the beak_width.

        :return: The beak_width.
        :rtype: int
        """
        return self._get_attr("beakWidth")

    @beak_width.setter
    @beartype
    def beak_width(self, value: Optional[int]) -> None:
        """ Set the beak_width.

        :param value: The beak_width.
        :type value: int
        """
        self._set_attr("beakWidth", value)

    # page_padding
    @property
    def page_padding(self) -> Optional[int]:
        """ Get the page_padding.

        :return: The page_padding.
        :rtype: int
        """
        return self._get_attr("pagePadding")

    @page_padding.setter
    @beartype
    def page_padding(self, value: Optional[int]) -> None:
        """ Set the page_padding.

        :param value: The page_padding.
        :type value: int
        """
        self._set_attr("pagePadding", value)

    # focus
    @property
    def focus(self) -> Optional[bool]:
        """ Get the focus.

        :return: The focus.
        :rtype: bool
        """
        return self._get_attr("focus")

    @focus.setter
    @beartype
    def focus(self, value: Optional[bool]) -> None:
        """ Set the focus.

        :param value: The focus.
        :type value: bool
        """
        self._set_attr("focus", value)

    # cover
    @property
    def cover(self) -> Optional[bool]:
        """ Get the cover.

        :return: The cover.
        :rtype: bool
        """
        return self._get_attr("cover")

    @cover.setter
    @beartype
    def cover(self, value: Optional[bool]) -> None:
        """ Set the cover.

        :param value: The cover.
        :type value: bool
        """
        self._set_attr("cover", value)

    def _get_children(self) -> List[str]:
        """ Get the controls of the callout.

        :return: The controls of the callout.
        :rtype: list
        """
        return self.__controls
