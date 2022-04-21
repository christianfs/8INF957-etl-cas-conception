from src.drivers.collector_factory import CollectorFactory
from src.etl.extract.extract_information import ExtractInformation
from src.etl.transform.transform_raw_data import TransformRawData
from src.etl.load.load_data import LoadData


class Etl:

    @staticmethod
    def run(file_path: str):
        file_collector = CollectorFactory.get_collector(file_path)
        extract_information = ExtractInformation(file_collector)
        extract_contract = extract_information.extract(file_path)
        transform_information = TransformRawData()
        transform_contract = transform_information.transform(extract_contract)
        LoadData().load(transform_contract.load_content)
