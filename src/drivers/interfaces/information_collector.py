from abc import ABC, abstractmethod
from typing import Dict

class InformationCollectorInterface(ABC):

    @abstractmethod
    def collect_information(self, file_path: str) -> Dict[str, str]:
        pass
