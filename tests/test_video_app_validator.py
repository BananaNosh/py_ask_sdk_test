import pytest
from ask_sdk_model.interfaces.videoapp import Metadata

from pseudo_handler import handler
from py_ask_sdk_test.alexa_test import AlexaTest
from py_ask_sdk_test.classes import TestItem, VideoItem
from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings


def test_video_app_validator():
    """Tests the VideoAppValidator"""
    alexa_test = AlexaTest(handler)
    alexa_test.test([
        TestItem(IntentRequestBuilder("OrpheusIntent", skill_settings)
                 .with_slot("pellicula", True).build(),
                 expected_video_item=VideoItem("https://",
                                               Metadata("Orpheus et Eurydike"))
                 )
    ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(IntentRequestBuilder("OrpheusIntent", skill_settings).build(),
                     expected_video_item=VideoItem("https://",
                                                   Metadata("Orpheus et Eurydike"))
                     )
        ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(IntentRequestBuilder("OrpheusIntent", skill_settings)
                     .with_slot("pellicula", True).build(),
                     expected_video_item=VideoItem("https://",
                                                   Metadata("Orpheus sine Eurydiki"))
                     )
        ])
    with pytest.raises(AssertionError):
        alexa_test.test([
            TestItem(IntentRequestBuilder("OrpheusIntent", skill_settings)
                     .with_slot("pellicula", True).build(),
                     expected_video_item=VideoItem("",
                                                   Metadata("Orpheus sine Eurydike"))
                     )
        ])
