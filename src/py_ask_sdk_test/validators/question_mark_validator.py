from py_ask_sdk_test.validators.abstract_response_validator import AbstractResponseValidator, TestItem, ResponseEnvelope


class QuestionMarkValidator(AbstractResponseValidator):
    """
    Validator against question marks at the end of responses for those who have not should_end_session == True
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against question marks
        Args:
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        if not test_item.check_question:
            return True
        output_speech = response.response.output_speech
        if output_speech is None:
            contains_question_mark = False
        else:
            speech_type = output_speech.object_type
            actual_speech = ""
            if speech_type == 'SSML':
                actual_speech = output_speech.ssml[7:-8]
            elif speech_type == 'PlainText':
                actual_speech = output_speech.text
            question_marks = ["?", "\u055E", "\u061F", "\u2E2E", "\uFF1F"]
            contains_question_mark = sum([q in actual_speech for q in question_marks]) > 0
        should_end_session = response.response.should_end_session
        should_end_session = True if should_end_session is None else should_end_session
        assert should_end_session != contains_question_mark
