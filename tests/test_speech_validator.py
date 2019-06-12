import pytest

from pseudo_handler import handler, speechs
from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from py_ask_sdk_test.request_builders.launch_request_builder import LaunchRequestBuilder
from test_config import skill_settings


def test_speech_validator_wrong_speech():
    """Tests the SpeechValidator with wrong speech"""
    alexa_test = AlexaTest(handler)
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    LaunchRequestBuilder(skill_settings).build(),
                    expected_speech="Foo Bar",
                    expected_repromt="Bar",
                    check_question=False
                )
            ]
        )


def test_speech_validator_wrong_reprompt():
    """Tests the SpeechValidator with wrong repromt"""
    alexa_test = AlexaTest(handler)
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    LaunchRequestBuilder(skill_settings).build(),
                    expected_speech=speechs["launch"],
                    expected_repromt="Bar",
                    check_question=False
                )
            ]
        )


def test_speech_validator_no_repromt():
    """Tests the SpeechValidator expecting a None reprompt"""
    alexa_test = AlexaTest(handler)
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    LaunchRequestBuilder(skill_settings).build(),
                    expected_speech=speechs["launch"],
                    expected_repromt="",
                    check_question=False
                )
            ]
        )


def test_speech_validator_correct():
    """Tests the SpeechValidator with correct speech and repromt"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                LaunchRequestBuilder(skill_settings).build(),
                expected_speech=speechs["launch"],
                expected_repromt=speechs["launch_repromt"],
                check_question=False
            )
        ]
    )


def test_speech_validator_no_speech():
    """Tests the SpeechValidator expecting an empty speech"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("TaceIntent", skill_settings).build(),
                expected_speech="",
                expected_repromt="",
                check_question=False
            )
        ]
    )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("TaceIntent", skill_settings).build(),
                    expected_speech="Heus",
                    expected_repromt="",
                    check_question=False
                )
            ]
        )


def test_speech_validator_regex_matched():
    """Tests the SpeechValidator using regex"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                LaunchRequestBuilder(skill_settings).build(),
                expected_speech=(r"Salve.+", True),
                expected_repromt=(speechs["launch_repromt"], False),
                check_question=False
            )
        ]
    )


def test_speech_validator_regex_no_match():
    """Tests the SpeechValidator using regex when it should alert"""
    alexa_test = AlexaTest(handler)
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("TaceIntent", skill_settings).build(),
                    expected_speech=(r".+", True),
                    expected_repromt="",
                    check_question=False
                )
            ]
        )


def test_speech_validator_plain_text():
    """Tests the SpeechValidator for a Plain Text response"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("DeiIntent", skill_settings).build(),
                expected_speech=(r"Jupiter.+", True),
                expected_repromt="",
                check_question=False
            )
        ]
    )
