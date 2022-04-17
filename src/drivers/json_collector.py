import json
from typing import Dict

from src.drivers.interfaces.information_collector import InformationCollectorInterface


class JsonCollector(InformationCollectorInterface):

    @classmethod
    def collect_information(cls, file_path: str) -> Dict[str, str]:
        data = None
        information = ''
        with open(file_path, "r") as read_file:
            data = json.load(read_file)
        if data:
            try:
                information = {
                    'id': data['id'],
                    'author': data['author'],
                    'title': data['title'],
                    'genre': data['genre'],
                    'price': data['price'],
                    'publish_date': data['publish_date'],
                    'description': data['description'],
                }
            except KeyError as e:
                print(f'Error: {e}')
        return information
