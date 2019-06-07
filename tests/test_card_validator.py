import pytest

from alexa_test import AlexaTest
from classes import TestItem
from pseudo_handler import handler, speechs, images
from request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings


def test_test_card_validator():
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("NeroIntent", skill_settings).build(),
                expected_card_title="Nero",
                expected_card_text=speechs["nero_card"],
                expected_small_image_url=images["nero"],
                expected_large_image_url=images["nero"],
                check_question=False
            ),
            TestItem(
                IntentRequestBuilder("CatullIntent", skill_settings).build(),
                expected_card_title="Catull",
                expected_card_content=("[^b]+basia!", True)
            )
        ]
    )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("NeroIntent", skill_settings).build(),
                    expected_card_title="Nero",
                    expected_card_text="Odi ignes.",
                    expected_small_image_url=images["nero"],
                    expected_large_image_url=images["nero"],
                    check_question=False
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("NeroIntent", skill_settings).build(),
                    expected_card_title="Augustus",
                    expected_card_text=speechs["nero_card"],
                    expected_small_image_url=images["nero"],
                    expected_large_image_url=images["nero"],
                    check_question=False
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("NeroIntent", skill_settings).build(),
                    expected_card_title="Nero",
                    expected_card_text=speechs["nero_card"],
                    expected_small_image_url="",
                    expected_large_image_url=images["nero"],
                    check_question=False
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("CatullIntent", skill_settings).build(),
                    expected_card_title="Catull",
                    expected_card_content="Abi"
                )
            ]
        )
