import pytest

from alexa_test import AlexaTest
from classes import TestItem
from pseudo_handler import handler
from request_builders.intent_request_builder import IntentRequestBuilder
from request_builders.launch_request_builder import LaunchRequestBuilder
from request_builders.session_ended_request_builder import SessionEndedRequestBuilder, SessionEndedReason
from test_config import skill_settings


def test_end_session_validator_wrong():
    alexa_test = AlexaTest(handler)
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
    alexa_test = AlexaTest(handler)
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
    alexa_test.test(
        [
            TestItem(
                SessionEndedRequestBuilder(SessionEndedReason.USER_INITIATED, skill_settings).build(),
                should_end_session=True
            )
        ]
    )
