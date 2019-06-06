from abstract_response_validator import AbstractResponseValidator, TestItem, ResponseEnvelope


class EndSessionValidator(AbstractResponseValidator):
    """
    Validator against expected should_end_session
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against should_end_session
        Args:
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        assert test_item.should_end_session is None \
               or test_item.should_end_session == response.response.should_end_session
        return True
