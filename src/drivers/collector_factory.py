from src.drivers.interfaces.information_collector import InformationCollectorInterface
from src.drivers.json_collector import JsonCollector
from src.drivers.xml_collector import XmlCollector
from src.errors.extract_error import ExtractError


class CollectorFactory:
    @staticmethod
    def get_collector(file_path: str) -> InformationCollectorInterface:
        if '.json' in file_path:
            return JsonCollector()
        elif '.xml' in file_path:
            return XmlCollector()
        else:
            raise ExtractError(f'Unsupported format: {file_path}')
