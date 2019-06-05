import json
import uuid

from ask_sdk_core.serialize import DefaultSerializer
from ask_sdk_model import ResponseEnvelope
from aws_lambda_context import LambdaContext

from classes import SkillSettings
from validators.speech_validator import SpeechValidator
from validators.question_mark_validator import QuestionMarkValidator
from validators.session_attribute_validator import SessionAttributeValidator
from validators.end_session_validator import EndSessionValidator
from validators.dialog_validator import DialogValidator
from validators.card_validator import CardValidator
from validators.audio_player_validator import AudioPlayerValidator
from validators.video_app_validator import VideoAppValidator


class AlexaTest:
    def __init__(self, handler, skill_settings):
        """
        Class for testing an alexa handler
        Args:
            handler(callable): the alexa handler
            skill_settings(SkillSettings): the settings for the skill
        """
        self.handler = handler
        self.skill_settings = skill_settings  # TODO check if needed
        self.validators = [
            SpeechValidator(),
            SessionAttributeValidator(),
            EndSessionValidator(),
            QuestionMarkValidator(),
            DialogValidator(),
            CardValidator(),
            AudioPlayerValidator(),
            VideoAppValidator()
        ]

    def test(self, test_items):
        """
        Test the sequence of TestItems against self.validators
        Args:
            test_items(list(TestItem)): the sequence of TestItems
        """
        if len(test_items) == 0:
            raise AttributeError("test_items must not be empty")
        session_attributes = {}
        session_id = test_items[0].request.session.session_id.format(uuid.uuid4())
        context = LambdaContext()
        for i, item in enumerate(test_items):
            item.request.session.new = i == 0
            item.request.attributes = session_attributes
            item.request.session.session_id = session_id

            # TODO withSessionAttr withUserAccessToken

            # TODO invokeFunction
            # request_dict = item.request.to_dict() TODO: remove
            # print(request_dict)
            # request_json = json.dumps(request_dict)
            # with open("test_events/generated.json", "w+") as f:
            #     f.write(request_json)
            # request_json = read("test_events/generated.json", loader=json.loads)
            # print(request_json)
            response_dict = self.handler(item.request, context)
            response = response_from_dict(response_dict)
            if self.skill_settings.debug:
                print(response)
            for validator in self.validators:
                validator.validate(item, response)

    # def _run_single_test(self, ):


def response_from_dict(response_dict):
    serializer = DefaultSerializer()
    response_json = json.dumps(serializer.serialize(response_dict))
    return serializer.deserialize(response_json, ResponseEnvelope)
