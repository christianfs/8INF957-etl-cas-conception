from unittest import TestCase

import pytest
from src.errors.transform_error import TransformError
from src.etl.contracts.transform_contract import TransformContract
from src.etl.transform.transform_raw_data import TransformRawData
from tests.etl.mocks.extract_contract import extract_contract_mock


class TransformRawDataTest(TestCase):

    def test_transform(self):
        transform_raw_data = TransformRawData()
        transformed_data_contract = transform_raw_data.transform(extract_contract_mock)

        assert isinstance(transformed_data_contract, TransformContract)
        assert 'author_first_name' in transformed_data_contract.load_content
        assert 'id' in transformed_data_contract.load_content
        assert 'title' in transformed_data_contract.load_content
        assert 'extraction_date' in transformed_data_contract.load_content

    def test_transform_error(self):
        transform_raw_data = TransformRawData()
        
        with pytest.raises(TransformError):
            transform_raw_data.transform('')
