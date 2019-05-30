from validators.speech_validator import SpeechValidator
from classes import TestItem, SkillSettings
import uuid
from aws_lambda_context import LambdaContext


class AlexaTest:
    def __init__(self, handler, skill_settings):
        """
        Class for testing an alexa handler
        Args:
            handler(callable): the alexa handler
            skill_settings(SkillSettings): the settings for the skill
        """
        self.handler = handler
        self.skill_settings = skill_settings
        self.validators = [SpeechValidator()]

    def test(self, test_items, description=""):
        """
        Test the sequence of TestItems against self.validators
        Args:
            test_items(list(TestItem)): the sequence of TestItems
            description(str): description of the test

        Returns:

        """
        if len(test_items) == 0:
            raise AttributeError("test_items must not be empty")
        session_attributes = {}
        session_id = test_items[0].request.session_id.format(uuid.uuid4())
        context = LambdaContext()
        for i, item in enumerate(test_items):
            item.request.session.new = i == 0
            item.request.attributes = session_attributes
            item.request.sessionId = session_id

            # TODO withSessionAttr withUserAccessToken


            # TODO invokeFunction
            self.handler(item.request, context)


    # def _run_single_test(self, ):





