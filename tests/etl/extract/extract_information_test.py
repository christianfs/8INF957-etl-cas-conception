from unittest import TestCase

import pytest
from src.errors.extract_error import ExtractError
from src.etl.contracts.extract_contract import ExtractContract
from src.etl.extract.extract_information import ExtractInformation
from tests.drivers.spies.information_collector import InformationCollectorSpy


class ExtractInformationTest(TestCase):

    def test_extract(self):
        collector_spy = InformationCollectorSpy()

        extract_information = ExtractInformation(collector_spy)
        response = extract_information.extract('file_path')

        assert 'file_path' in collector_spy.collect_information_attributes
        assert isinstance(response, ExtractContract)

    def test_extract_error(self):
        extract_information = ExtractInformation('')

        with pytest.raises(ExtractError):
            extract_information.extract('file_path')
