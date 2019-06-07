import pytest

from alexa_test import AlexaTest
from classes import TestItem
from pseudo_handler import handler
from request_builders.intent_request_builder import IntentRequestBuilder
from request_builders.launch_request_builder import LaunchRequestBuilder
from test_config import skill_settings


def test_dialog_validator_elicit_slot():
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings).build(),
                check_question=False,
                expected_slot_to_elicit="legiones"
            ),
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings).with_empty_slot("legiones").build(),
                check_question=False,
                expected_slot_to_elicit="legiones"
            ),
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "3")
                    .with_slot_with_resolution_no_match("ballistae", "heus", "ballistaeSlotType")
                    .build(),
                check_question=False,
                expected_slot_to_elicit="ballistae"
            ),
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "2")
                    .with_slot("legiones", "3")
                    .build(),
                check_question=False,
                expected_slot_to_elicit="ballistae"
            )
        ]
    )
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "3")
                    .with_slot_with_resolution("ballistae", "magni", "ballistaeSlotType", "magnae")
                    .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                    .build(),
                check_question=False,
                expected_slot_to_elicit="legati"
            ),
        ]
    )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("VarusIntent", skill_settings).build(),
                    check_question=False,
                    expected_slot_to_elicit="legati"
                ),
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    LaunchRequestBuilder(skill_settings).build(),
                    check_question=False,
                    expected_slot_to_elicit="romani"
                ),
            ]
        )


def test_dialog_validator_elicit_intent():
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test([
        TestItem(
            IntentRequestBuilder("VarusIntent", skill_settings)
                .with_slot("legiones", "3")
                .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                .with_slot("legati", 100).build(),
            expected_intent_for_elicitation="DeiIntent"
        )
    ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "3")
                    .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                    .build(),
                expected_intent_for_elicitation="DeiIntent"
            )
        ])


def test_dialog_validator_confirm_slot():
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test([
        TestItem(
            IntentRequestBuilder("VarusIntent", skill_settings)
                .with_slot("legiones", "3")
                .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                .with_slot("legati", 50).build(),
            expected_slot_to_confirm="legati"
        )
    ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "3")
                    .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                    .with_slot("legati", 100).build(),
                expected_slot_to_confirm="legati"
            )
        ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "3")
                    .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                    .with_slot("legati", 50).build(),
                expected_slot_to_confirm="ballistae"
            )
        ])


def test_dialog_validator_confirm_intent():
    alexa_test = AlexaTest(handler, skill_settings)
    alexa_test.test([
        TestItem(
            IntentRequestBuilder("VarusIntent", skill_settings)
                .with_slot("legiones", "3")
                .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                .with_slot("legati", 50).build(),
            should_confirm_intent=False
        )
    ])
    alexa_test.test([
        TestItem(
            IntentRequestBuilder("NeroIntent", skill_settings).build(),
            check_question=False,
            should_confirm_intent=True
        )
    ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "3")
                    .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                    .with_slot("legati", 100).build(),
                expected_slot_to_confirm="legati"
            )
        ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(
                IntentRequestBuilder("VarusIntent", skill_settings)
                    .with_slot("legiones", "3")
                    .with_slot_with_resolution("ballistae", "magnae", "ballistaeSlotType", "magnae")
                    .with_slot("legati", 50).build(),
                expected_slot_to_confirm="ballistae"
            )
        ])
