import pytest

from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem, PlayStreamConfig, PlayBehavior, ClearBehavior, Stream
from pseudo_handler import handler
from py_ask_sdk_test.request_builders.audio_player_intent_request_builder import AudioPlayerPauseIntentRequestBuilder
from py_ask_sdk_test.request_builders.audio_player_intent_request_builder import AudioPlayerResumeIntentRequestBuilder
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings


def test_audio_player_validator_play_directive():
    """Tests the AudioPlayerValidator for a PlayDirective"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("OrpheusIntent", skill_settings).build(),
                expected_play_stream=PlayStreamConfig(
                    PlayBehavior.REPLACE_ALL,
                    Stream(token="cantare_token", url="https://")
                ),
            ),
            TestItem(
                AudioPlayerResumeIntentRequestBuilder(skill_settings).with_token("lyra_token").build(),
                expected_play_stream=PlayStreamConfig(
                    PlayBehavior.REPLACE_ALL,
                    Stream(token="lyra_token", url="https://")
                )
            )
        ]
    )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("OrpheusIntent", skill_settings).build(),
                    expected_play_stream=PlayStreamConfig(
                        PlayBehavior.ENQUEUE,
                        Stream(token="cantare_token", url="https://")
                    ),
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("OrpheusIntent", skill_settings).build(),
                    expected_play_stream=PlayStreamConfig(
                        PlayBehavior.REPLACE_ALL,
                        Stream(token="lyra_token", url="https://")
                    ),
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    AudioPlayerResumeIntentRequestBuilder(skill_settings).with_token("lyra_token").build(),
                    expected_play_stream=PlayStreamConfig(
                        PlayBehavior.REPLACE_ALL,
                        Stream(token="cantare_token", url="https://")
                    )
                )
            ]
        )


def test_audio_player_validator_stop_directive():
    """Tests the AudioPlayerValidator for a StopDirective"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                AudioPlayerPauseIntentRequestBuilder(skill_settings).build(),
                should_stop_stream=True
            )
        ]
    )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("OrpheusIntent", skill_settings).build(),
                    should_stop_stream=True
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    AudioPlayerPauseIntentRequestBuilder(skill_settings).build(),
                    should_stop_stream=False
                )
            ]
        )


def test_audio_player_validator_clear_queue_directive():
    """Tests the AudioPlayerValidator for a ClearQueueDirective"""
    alexa_test = AlexaTest(handler)
    alexa_test.test(
        [
            TestItem(
                IntentRequestBuilder("TaceIntent", skill_settings).build(),
                expected_clear_stream_behaviour=ClearBehavior.CLEAR_ALL,
                check_question=False
            )
        ]
    )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("OrpheusIntent", skill_settings).build(),
                    expected_clear_stream_behaviour=ClearBehavior.CLEAR_ALL
                )
            ]
        )
    with pytest.raises(AssertionError):
        alexa_test.test(
            [
                TestItem(
                    IntentRequestBuilder("TaceIntent", skill_settings).build(),
                    expected_clear_stream_behaviour=ClearBehavior.CLEAR_ENQUEUED
                )
            ]
        )
