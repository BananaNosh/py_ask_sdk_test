import datetime

from ask_sdk_model import SessionEndedRequest, SessionEndedReason

from py_ask_sdk_test.request_builders.abstract_request_builder import AbstractRequestBuilder, SkillSettings


class SessionEndedRequestBuilder(AbstractRequestBuilder):
    def __init__(self, reason, skill_settings):
        """
        RequestBuilder for a SessionEndedRequest
        Args:
            reason(SessionEndedReason): The reason for the SessionEnd
            skill_settings(SkillSettings): The settings of the tested skill
        """
        super(SessionEndedRequestBuilder, self).__init__(skill_settings)
        self.reason = reason

    def build_request(self):
        """
        Builds the request
        Returns: (SessionEndedRequest) the build SessionRequest
        """
        return SessionEndedRequest(
            request_id=self.request_id,
            timestamp=datetime.datetime.now(),
            locale=self.skill_settings.locale,
            reason=self.reason
        )
