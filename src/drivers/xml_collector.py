from typing import Dict

from bs4 import BeautifulSoup
from src.drivers.interfaces.information_collector import \
    InformationCollectorInterface


class XmlCollector(InformationCollectorInterface):

    @classmethod
    def collect_information(cls, file_path: str) -> Dict[str, str]:
        data = None
        information = ''
        with open(file_path, "r") as read_file:
            data = BeautifulSoup(read_file.read(), 'xml')
        if data:
            try:
                information = {
                    'id': data.find('id').get_text(),
                    'author': data.find('author').get_text(),
                    'title': data.find('title').get_text(),
                    'genre': data.find('genre').get_text(),
                    'price': data.find('price').get_text(),
                    'publish_date': data.find('publish_date').get_text(),
                    'description': data.find('description').get_text(),
                }
            except AttributeError as e:
                print(f'Error: {e}')
        return information
