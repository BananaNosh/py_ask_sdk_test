from alexa_test import AlexaTest
from classes import TestItem
from test_config import skill_settings
from request_builders.launch_request_builder import LaunchRequestBuilder
from request_builders.intent_request_builder import IntentRequestBuilder
from pseudo_handler import handler, speechs
import pytest


def test_speech_validator():
    alexa_test = AlexaTest(handler, skill_settings)
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
