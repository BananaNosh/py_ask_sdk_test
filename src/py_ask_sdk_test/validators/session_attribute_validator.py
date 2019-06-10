from py_ask_sdk_test.validators.abstract_response_validator import AbstractResponseValidator, TestItem, ResponseEnvelope


class SessionAttributeValidator(AbstractResponseValidator):
    """
    Validator against expected session attributes
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against the expected session attributes
        Args:
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        if test_item.expected_attributes is None:
            return True
        assert response.session_attributes is not None
        for key, value in test_item.expected_attributes.items():
            assert key in response.session_attributes
            assert response.session_attributes[key] == value
        return True
