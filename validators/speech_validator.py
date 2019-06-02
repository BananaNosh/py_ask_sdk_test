from abstract_response_validator import AbstractResponseValidator
import re


class SpeechValidator(AbstractResponseValidator):
    """
    Validator against expected speech
    """

    def validate(self, test_item, response):
        if not response.response:
            self.fail("No response given")
        if response.response.output_speech:
            expected_speech = test_item.expected_speech
            self._assert_output_speech(response.response.output_speech, expected_speech,
                                       "Not the expected speech output")

        if response.response.reprompt and response.response.reprompt.output_speech:
            expected_repromt = test_item.expected_repromt
            self._assert_output_speech(response.response.reprompt.output_speech, expected_repromt,
                                       "Not the expected repromt output")

    def _assert_output_speech(self, output_speech, expected_speech, msg):
        speech_type = output_speech.object_type
        actual_speech = None
        if speech_type == 'SSML':
            actual_speech = output_speech.ssml[7:-8]
        elif speech_type == 'PlainText':
            actual_speech = output_speech.text
        if expected_speech is not None:
            if len(expected_speech) == 0:
                self.assertIsNone(actual_speech)
            else:
                match = re.match(expected_speech, actual_speech)
                self.assertIsNotNone(match, msg + ": {} instead of {}".format(actual_speech, expected_speech))
