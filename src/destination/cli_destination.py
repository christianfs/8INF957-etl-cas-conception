from typing import Dict
from src.destination.interfaces.destination import DestinationInterface


class CliDestination(DestinationInterface):
    def __init__(self, information: Dict):
        self.__id = information["id"]
        self.__author_name = information["author_name"]
        self.__title = information["title"]
        self.__description = information["description"]
        self.__genre = information["genre"]
        self.__price = information["price"]
        self.__publish_date = information["publish_date"]
        self.__extraction_date = information["extraction_date"]

    def load_to_destination(self) -> None:
        print(self)

    def __str__(self):
        return f'''
            Id - {self.__id}
            Author - {self.__author_name}
            Title - {self.__title}
            Description - {self.__description}
            Genre - {self.__genre}
            Price (USD)- {self.__price}
            Publish date - {self.__publish_date}
            Extraction date - {self.__extraction_date}
            
            ============================================================'''
