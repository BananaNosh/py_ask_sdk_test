from abstract_response_validator import AbstractResponseValidator
from ask_sdk_model import ResponseEnvelope


class SpeechValidator(AbstractResponseValidator):
    """
    Validator against expected speech
    """
    def validate(self, test_item, response):
        actual_speech = None
        if response.response and response.response.outputSpeech:
            speech_type = response.response.outputSpeech.type
            if speech_type == 'SSML':
                actual_speech = response.response.outputSpeech.ssml[7:-8]
            elif speech_type == 'PlainText':
                actual_speech = response.response.outputSpeech.text
