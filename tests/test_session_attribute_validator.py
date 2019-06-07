import pytest

from alexa_test import AlexaTest
from classes import TestItem
from pseudo_handler import handler
from request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings


def test_session_attribute_validator():
    alexa_test = AlexaTest(handler, skill_settings)
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
