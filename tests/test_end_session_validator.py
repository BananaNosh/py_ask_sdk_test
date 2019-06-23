import pytest

from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem
from pseudo_handler import handler
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from py_ask_sdk_test.request_builders.launch_request_builder import LaunchRequestBuilder
from py_ask_sdk_test.request_builders.session_ended_request_builder import SessionEndedRequestBuilder, SessionEndedReason
from test_config import skill_settings


def test_end_session_validator_wrong():
    """Tests the EndSessionValidator when it should alert"""
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
    """Tests the EndSessionValidator when it should not alert"""
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


def test_end_session_validator_with_directive():
    pass  # TODO
