from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem, ProfileInfo
from pseudo_handler import handler
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings
import pytest


def test_with_profile_info():
    """Tests AlexaTest with profile_info"""
    alexa_test = AlexaTest(handler)
    alexa_test.test([
        TestItem(IntentRequestBuilder("DeiIntent", skill_settings).build(),
                 profile_info=ProfileInfo("Apollo", "Paian", "apollo@olympus.org", "003023520"),
                 user_access_token="token",
                 expected_speech="Apollo potens est."
                 )
    ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(IntentRequestBuilder("DeiIntent", skill_settings).build(),
                     profile_info=ProfileInfo("Minerva", "Glaukopis", "minerva@olympus.org", "003023520"),
                     expected_speech="Apollo potens est."
                     )
        ])


def test_other_http_request():
    """Tests that other not profile related http requests still work"""
    alexa_test = AlexaTest(handler)
    alexa_test.test([
        TestItem(IntentRequestBuilder("DeiIntent", skill_settings).build(),
                 profile_info=ProfileInfo("Apollo", "Paian", "apollo@olympus.org", "003023520"),
                 session_attributes={"remotus": True},
                 expected_speech=(r"Olympus respondit: \d{3}", True)
                 )
    ])
