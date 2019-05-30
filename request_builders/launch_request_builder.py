from request_builders.abstract_request_builder import AbstractRequestBuilder
from ask_sdk_model import Request
import datetime


class LaunchRequestBuilder(AbstractRequestBuilder):
    def build_request(self):
        return Request(object_type="LaunchRequest",
                       request_id=self.request_id,
                       timestamp=datetime.datetime.now(),
                       locale=self.skill_settings.locale)