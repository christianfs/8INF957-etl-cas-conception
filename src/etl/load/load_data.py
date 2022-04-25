from src.destination.interfaces.destination import DestinationInterface
from src.destination.destination_factory import DestinationFactory
from src.etl.contracts.transform_contract import TransformContract


class LoadData:

    @staticmethod
    def load(transform_contract: TransformContract) -> None:
        destination: DestinationInterface = DestinationFactory.get_destination(transform_contract.load_content)
        destination.load_to_destination()
