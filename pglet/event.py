""" Module for the Event class. """

from __future__ import annotations
from typing import Any
from dataclasses import dataclass
from beartype import beartype


@beartype
@dataclass
class Event:
    """ This dataclass is used to represent an event.

    Attributes:
        target (str): The ID of the target.
        name (str): The name of the event.
        data (Any): The data of the event.
    """
    target: str
    name: str
    data: Any
