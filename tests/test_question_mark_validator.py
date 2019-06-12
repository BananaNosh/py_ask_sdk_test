import pytest

from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem
from pseudo_handler import handler
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from py_ask_sdk_test.request_builders.launch_request_builder import LaunchRequestBuilder
from test_config import skill_settings


def test_question_mark_validator_wrong():
    """Tests the QuestionMarkValidator for the cases when it should alert"""
    alexa_test = AlexaTest(handler)
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    LaunchRequestBuilder(skill_settings).build(),
                    check_question=True,
                    should_end_session=False
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("NeroIntent", skill_settings).build(),
                    check_question=True,
                    should_end_session=True
                )
            ]
        )


def test_question_mark_validator_correct():
    """Tests the QuestionMarkValidator for the cases when it should not alert"""
    alexa_test = AlexaTest(handler)
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
                IntentRequestBuilder("CatullIntent", skill_settings).build(),
                should_end_session=False
            )
        ]
    )
