from datetime import date
from typing import Dict

from src.drivers.interfaces.information_collector import \
    InformationCollectorInterface
from src.errors.extract_error import ExtractError
from src.etl.contracts.extract_contract import ExtractContract


class ExtractInformation:

    def __init__(self, information_collector: InformationCollectorInterface) -> None:
        self.__information_collector = information_collector

    def extract(self, file_path: str) -> ExtractContract:
        try:
            information: Dict[str, str] = self.__information_collector.collect_information(file_path=file_path)
            return ExtractContract(
                raw_information_content=information,
                extraction_date=date.today()
            )
        except Exception as exception:
            raise ExtractError(str(exception)) from exception
