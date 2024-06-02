import datetime
from abc import ABC, abstractmethod
from typing import Any


class Processor(ABC):
    """
    Classes that inherits from Processor are responsible for storing and processing data
    """

    def __init__(self) -> None:
        self.data = []
        self.current_time = datetime.datetime.now()

    @abstractmethod
    def process(self, data: list[Any]) -> list[Any]:
        """
        Process data flow
        """

    @abstractmethod
    def update(self, data: list[Any]) -> None:
        """
        Update internal state of the object
        """
