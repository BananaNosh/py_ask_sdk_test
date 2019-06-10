import abc
import uuid

from ask_sdk_model import RequestEnvelope, Session, Application, User, Context, Device
from ask_sdk_model.interfaces.audioplayer import AudioPlayerState, PlayerActivity
from ask_sdk_model.interfaces.system import SystemState

from py_ask_sdk_test.classes import SkillSettings


class AbstractRequestBuilder(abc.ABC):
    def __init__(self, skill_settings):
        """
        RequestBuilder
        Args:
            skill_settings(SkillSettings):  The settings of the tested Skill
        """
        self.skill_settings = skill_settings
        self.user = User(self.skill_settings.user_id)
        self.application = Application(self.skill_settings.app_id)
        self.request_id = "EdwRequestId.{}".format(uuid.uuid4())

    def build(self):
        """
        Builds a request according to the skillSettings
        Returns: (RequestEnvelope) The request envelope
        """
        envelope = RequestEnvelope(version="1.0", session=self.get_session_data(), context=self.get_context_data(),
                                   request=self.build_request())
        self.modify_request_envelope(envelope)
        return envelope

    def get_session_data(self):
        """
        Create a session according to the skill_settings
        Returns: (Session) the session

        """
        return Session(new=True, session_id="SessionId.{}",
                       user=self.user, attributes={},
                       application=self.application)

    def get_context_data(self):
        """
        Creates a context according to the skill_settings
        Returns: (Context) the context

        """
        context = Context(SystemState(application=self.application, user=self.user,
                                      device=Device(self.skill_settings.device_id,
                                                    self.skill_settings.supported_interfaces),
                                      api_endpoint=self.skill_settings.api_endpoint,
                                      api_access_token=str(uuid.uuid4())),
                          AudioPlayerState(player_activity=PlayerActivity.IDLE))
        return context

    @abc.abstractmethod
    def build_request(self):
        """
        Builds the request
        Returns: (Request) the request
        """
        pass

    def modify_request_envelope(self, request_envelope):
        """
        Modifies the envelope after it has been created (Override if needed)
        Args:
            request_envelope(RequestEnvelope): the in self.build created envelope

        """
        pass
