from alexa_test import AlexaTest
from classes import TestItem, VideoItem
from ask_sdk_model.interfaces.videoapp import Metadata
from pseudo_handler import handler
from request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings
import pytest


def test_video_app_validator():
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
