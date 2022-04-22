from datetime import datetime
from decimal import Decimal
from typing import Dict, List

from errors.transform_error import TransformError
from etl.contracts.extract_contract import ExtractContract
from etl.contracts.transform_contract import TransformContract


class TransformRawData:

    def transform(self, extract_contract: ExtractContract) -> TransformContract:
        try:
            transformed_data = self.__filter_data(extract_contract)
            transformed_data_contract = TransformContract(
                load_content=transformed_data
            )
            return transformed_data_contract
        except Exception as exception:
            raise TransformError(str(exception)) from Exception

    def __filter_data(self, extract_contract: ExtractContract) -> List[Dict]:
        extraction_date = extract_contract.extraction_date
        data_content = extract_contract.raw_information_content
        transformed_data = None

        if not data_content['author']:
            return transformed_data

        names = None
        if ', ' in data_content['author']:
            names = data_content['author'].split(', ')
        else:
            names = [data_content['author']]

        transformed_data = self.__transform_data(names, data_content['price'], data_content['publish_date'])
        transformed_data['id'] = data_content['id']
        transformed_data['title'] = data_content['title']
        transformed_data['genre'] = data_content['genre']
        transformed_data['description'] = data_content['description']
        transformed_data['extraction_date'] = extraction_date

        return transformed_data

    @classmethod
    def __transform_data(cls, names: List, price: str, date: str) -> Dict:
        data = {}
        if len(names) == 2:
            data = {
                'author_name': f'{names[1]} {names[0]}'
            }
        else:
            data = {
                'author_name': names
            }
        data['price'] = Decimal(price)
        data['publish_date'] = datetime.strptime(date, '%Y-%m-%d').date()

        return data
