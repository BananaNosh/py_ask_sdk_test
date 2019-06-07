import pytest

from alexa_test import AlexaTest
from classes import TestItem
from pseudo_handler import handler
from request_builders.intent_request_builder import IntentRequestBuilder
from request_builders.launch_request_builder import LaunchRequestBuilder
from test_config import skill_settings


def test_end_session_validator_wrong():
    alexa_test = AlexaTest(handler, skill_settings)
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    LaunchRequestBuilder(skill_settings).build(),
                    check_question=False,
                    should_end_session=True
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("DeiIntent", skill_settings).build(),
                    should_end_session=False
                )
            ]
        )


def test_end_session_validator_correct():
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test(
        [
            TestItem(
                LaunchRequestBuilder(skill_settings).build(),
                check_question=False,
                should_end_session=False
            )
        ]
    )
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("DeiIntent", skill_settings).build(),
                should_end_session=True
            )
        ]
    )
