import re

from py_ask_sdk_test.validators.abstract_response_validator import AbstractResponseValidator


class SpeechValidator(AbstractResponseValidator):
    """
    Validator against expected speech and repromt
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against expected speech and repromt
        Args:
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        if not response.response:
            assert False, "No response given"
        if test_item.expected_speech is not None:
            expected_speech = test_item.expected_speech
            self._assert_output_speech(response.response.output_speech, expected_speech,
                                       "Not the expected speech output")

        if test_item.expected_repromt is not None:
            actual_repromt = response.response.reprompt
            actual_repromt = actual_repromt.output_speech if actual_repromt is not None else None
            expected_repromt = test_item.expected_repromt
            self._assert_output_speech(actual_repromt, expected_repromt,
                                       "Not the expected repromt output")
        return True

    @staticmethod
    def _assert_output_speech(output_speech, expected_speech, msg):
        is_regex = False
        if type(expected_speech) is tuple:
            is_regex = expected_speech[1]
            expected_speech = expected_speech[0]
            assert expected_speech is not None
        if output_speech is None:
            assert len(expected_speech) == 0, msg
            return
        speech_type = output_speech.object_type
        actual_speech = None
        if speech_type == 'SSML':
            actual_speech = output_speech.ssml[7:-8]
        elif speech_type == 'PlainText':
            actual_speech = output_speech.text
        if len(expected_speech) == 0:
            assert actual_speech is None or len(actual_speech) == 0
        elif is_regex:
            match = re.fullmatch(expected_speech, actual_speech)
            assert match is not None, msg + ": {} instead of {}".format(actual_speech, expected_speech)
        else:
            assert expected_speech == actual_speech, msg + ": '{}' instead of '{}'".format(actual_speech, expected_speech)
