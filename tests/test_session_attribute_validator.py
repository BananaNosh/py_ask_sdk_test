import pytest

from pseudo_handler import handler
from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings


def test_session_attribute_validator():
    """Tests the SessionAttributeValidator"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("DeiIntent", skill_settings).build(),
                expected_attributes={"sacrificium": "tres boves"}
            )
        ]
    )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("DeiIntent", skill_settings).build(),
                    expected_attributes={"sacrificium": "tria boves"}
                )
            ]
        )
