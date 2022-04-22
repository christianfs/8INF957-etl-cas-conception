from src.destination.cli_destination import CliDestination
from src.destination.interfaces.destination import DestinationInterface
from typing import Dict


class DestinationFactory:
    @staticmethod
    def get_destination(information: Dict) -> DestinationInterface:
        return CliDestination(information)
