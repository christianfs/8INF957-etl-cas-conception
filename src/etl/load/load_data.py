from src.drivers.interfaces.destiny import DestinyInterface
from src.drivers.destiny_factory import DestinyFactory
from typing import Dict


class LoadData:

    @staticmethod
    def load(information: Dict) -> None:
        destiny: DestinyInterface = DestinyFactory.get_destiny(information)
        destiny.load_to_destiny()
