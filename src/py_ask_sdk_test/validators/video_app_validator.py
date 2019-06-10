from ask_sdk_model.interfaces.videoapp import LaunchDirective

from py_ask_sdk_test.validators.abstract_response_validator import AbstractResponseValidator, TestItem, ResponseEnvelope


class VideoAppValidator(AbstractResponseValidator):
    """
    Validator against the expected VideoItem
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against the expected VideoItem
        Args:
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        if not test_item.expected_video_item:
            return True
        assert response.response.directives
        directives_for_type = {}
        for d in response.response.directives:
            directives_for_type[type(d)] = d
        assert LaunchDirective in directives_for_type
        launch_directive = directives_for_type[LaunchDirective]
        expected_video_item = test_item.expected_video_item
        video_item = launch_directive.video_item
        assert video_item.source.startswith("https://"), "The stream url is not https"
        assert expected_video_item == video_item
        return True
