from src.destination.interfaces.destination import DestinationInterface
from src.destination.destination_factory import DestinationFactory
from typing import Dict


class LoadData:

    @staticmethod
    def load(information: Dict) -> None:
        destination: DestinationInterface = DestinationFactory.get_destination(information)
        destination.load_to_destination()
