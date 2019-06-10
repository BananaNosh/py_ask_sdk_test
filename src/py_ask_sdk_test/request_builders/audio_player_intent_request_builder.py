from ask_sdk_model.interfaces.audioplayer import PlayerActivity, AudioPlayerState

from py_ask_sdk_test.request_builders.abstract_request_builder import SkillSettings, RequestEnvelope
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder


class AudioPlayerResumeIntentRequestBuilder(IntentRequestBuilder):
    def __init__(self, skill_settings):
        """
        RequestBuilder for an AudioPlayerResumeIntentRequest
        Args:
            skill_settings(SkillSettings): The settings of the tested skill
        """
        super(AudioPlayerResumeIntentRequestBuilder, self).__init__("AMAZON.ResumeIntent", skill_settings)
        self.token = None
        self.offset = None
        self.current_activity = None

    def with_token(self, token):
        """
        Set the token for the request
        Args:
            token(str): the token to be added
        Returns: (AudioPlayerResumeIntentRequestBuilder) self
        """
        self.token = token
        return self

    def with_offset(self, offset):
        """
        Set the offset for the request
        Args:
            offset(int): the offset to be added
        Returns: (AudioPlayerResumeIntentRequestBuilder) self
        """
        self.offset = offset
        return self

    def with_current_activity(self, current_activity):
        """
        Set the current activity for the request
        Args:
            current_activity(PlayerActivity): the activity to be added
        Returns: (AudioPlayerResumeIntentRequestBuilder) self
        """
        self.current_activity = current_activity
        return self

    def modify_request_envelope(self, request_envelope):
        """
        Modifies the envelope after it has been created to set the AudioPlayer properties

        Args:
            request_envelope(RequestEnvelope): the in self.build created envelope

        """
        super(AudioPlayerResumeIntentRequestBuilder, self).modify_request_envelope(request_envelope)
        request_envelope.context.audio_player = AudioPlayerState(self.offset, self.token, self.current_activity)


class AudioPlayerPauseIntentRequestBuilder(IntentRequestBuilder):
    def __init__(self, skill_settings):
        """
        RequestBuilder for an AudioPlayerPauseIntentRequest
        Args:
            skill_settings(SkillSettings): The settings of the tested skill
        """
        super(AudioPlayerPauseIntentRequestBuilder, self).__init__("AMAZON.PauseIntent", skill_settings)
