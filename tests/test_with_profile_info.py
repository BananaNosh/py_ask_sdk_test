from alexa_test import AlexaTest
from classes import TestItem, ProfileInfo
from pseudo_handler import handler
from request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings
import pytest


def test_with_profile_info():
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test([
        TestItem(IntentRequestBuilder("DeiIntent", skill_settings).build(),
                 profile_info=ProfileInfo("Apollo", "Paian", "apollo@olympus.org", "003023520"),
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
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test([
        TestItem(IntentRequestBuilder("DeiIntent", skill_settings).with_slot("remotus", True).build(),
                 profile_info=ProfileInfo("Apollo", "Paian", "apollo@olympus.org", "003023520"),
                 expected_speech=(r"Olympus respondit: \d{3}", True)
                 )
    ])
