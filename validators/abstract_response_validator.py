import abc
from classes import TestItem
from ask_sdk_model import ResponseEnvelope


class AbstractResponseValidator(abc.ABC):
    @abc.abstractmethod
    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item
        Args:
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        pass
