from distutils.log import info
from unittest import TestCase

from src.drivers.interfaces.information_collector import \
    InformationCollectorInterface
from src.drivers.json_collector import JsonCollector


class JsonCollectorTest(TestCase):

    def test_collect_information(self):
        json_collector: InformationCollectorInterface = JsonCollector()
        information = json_collector.collect_information('files_to_read/f1.json')

        assert isinstance(information, dict)
        assert 'id' in information
        assert 'author' in information
