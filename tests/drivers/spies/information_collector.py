class InformationCollectorSpy():

    def __init__(self) -> None:
        self.collect_information_attributes = {}

    def collect_information(self, file_path: str):
        self.collect_information_attributes['file_path'] = file_path
        return ({
            'id': 'bk101',
            'author': 'Gambardella, Matthew',
            'title': "XML Developer's Guide",
            'genre': 'Computer',
            'price': '44.95',
            'publish_date': '2000-10-01',
            'description': 'An in-depth look at creating applications with XML.'
        })
