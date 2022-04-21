from typing import Dict
from src.drivers.interfaces.destiny import DestinyInterface


class CliDestiny(DestinyInterface):
    def __init__(self, information: Dict):
        self.id = information["id"]
        self.first_name = information["author_first_name"]
        self.last_name = information["author_last_name"]
        self.title = information["title"]
        self.description = information["description"]
        self.genre = information["genre"]
        self.price = information["price"]
        self.publish_date = information["publish_date"]
        self.extraction_date = information["extraction_date"]

    def load_to_destiny(self) -> None:
        print(self)

    def __str__(self):
        return f'''
            Id - {self.id}
            Author\'s first name - {self.first_name}
            Author\'s last name - {self.last_name}
            Title - {self.title}
            Description - {self.description}
            Genre - {self.genre}
            Price (USD)- {self.price}
            Publish date - {self.publish_date}
            Extraction date - {self.extraction_date}
            
            ============================================================'''
