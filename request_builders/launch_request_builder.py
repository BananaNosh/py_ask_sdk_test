from request_builders.abstract_request_builder import AbstractRequestBuilder
from ask_sdk_model import LaunchRequest
import datetime


class LaunchRequestBuilder(AbstractRequestBuilder):
    def build_request(self):
        return LaunchRequest(request_id=self.request_id,
                             timestamp=datetime.datetime.now(),  # .isoformat(),
                             locale=self.skill_settings.locale)
