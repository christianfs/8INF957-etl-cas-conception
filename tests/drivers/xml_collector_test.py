from unittest import TestCase

from src.drivers.interfaces.information_collector import \
    InformationCollectorInterface
from src.drivers.xml_collector import XmlCollector


class JsonCollectorTest(TestCase):

    def test_collect_information(self):
        xml_collector: InformationCollectorInterface = XmlCollector()
        information = xml_collector.collect_information('files_to_read/f1.xml')

        assert isinstance(information, dict)
        assert 'id' in information
        assert 'author' in information
