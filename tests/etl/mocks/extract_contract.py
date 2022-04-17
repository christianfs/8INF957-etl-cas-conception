from datetime import date

from src.etl.contracts.extract_contract import ExtractContract

extract_contract_mock = ExtractContract(
    raw_information_content={
        'id': 'bk101',
        'author': 'Gambardella, Matthew',
        'title': "XML Developer's Guide",
        'genre': 'Computer',
        'price': '44.95',
        'publish_date': '2000-10-01',
        'description': 'An in-depth look at creating applications with XML.'
    },
    extraction_date=date.today()
)
