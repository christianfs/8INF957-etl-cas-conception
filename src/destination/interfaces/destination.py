from abc import ABC, abstractmethod
from typing import Dict


class DestinationInterface(ABC):

    @abstractmethod
    def __init__(self, information: Dict) -> None:
        pass

    @abstractmethod
    def load_to_destination(self) -> None:
        pass

    @abstractmethod
    def __str__(self) -> None:
        pass
