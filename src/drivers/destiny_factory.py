from src.drivers.cli_destiny import CliDestiny
from src.drivers.interfaces.destiny import DestinyInterface
from typing import Dict


class DestinyFactory:
    @staticmethod
    def get_destiny(information: Dict) -> DestinyInterface:
        return CliDestiny(information)
