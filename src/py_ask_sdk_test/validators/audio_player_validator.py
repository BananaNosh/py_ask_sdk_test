from ask_sdk_model.interfaces.audioplayer import PlayDirective, StopDirective, ClearQueueDirective

from py_ask_sdk_test.validators.abstract_response_validator import AbstractResponseValidator, TestItem, ResponseEnvelope


class AudioPlayerValidator(AbstractResponseValidator):
    """
    Validator against the expected AudioPlayer behaviour and stream
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against the expected AudioPlayer behaviour and stream
        Args:
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        expected_play_config = test_item.expected_play_stream
        if not expected_play_config and test_item.should_stop_stream is None \
                and not test_item.expected_clear_stream_behaviour:
            return True
        assert response.response.directives
        directives_for_type = {}
        for d in response.response.directives:
            directives_for_type[type(d)] = d
        if expected_play_config:
            assert PlayDirective in directives_for_type
            play_directive = directives_for_type[PlayDirective]
            stream = play_directive.audio_item.stream
            assert stream.url.startswith("https://"), "The stream url is not https"
            if expected_play_config.stream:
                assert expected_play_config.stream == stream
            assert play_directive.play_behavior == expected_play_config.behavior
        if test_item.should_stop_stream is not None:
            assert test_item.should_stop_stream == (StopDirective in directives_for_type)
        if test_item.expected_clear_stream_behaviour:
            assert ClearQueueDirective in directives_for_type
            clear_queue_directive = directives_for_type[ClearQueueDirective]
            assert test_item.expected_clear_stream_behaviour == clear_queue_directive.clear_behavior
        return True
