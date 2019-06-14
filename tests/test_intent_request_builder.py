from py_ask_sdk_test.request_builders.intent_request_builder import IntentRequestBuilder
from test_config import skill_settings


def test_intent_request_builder_with_resolutions():
    request_envelope = IntentRequestBuilder("testIntent", skill_settings) \
        .with_slot_with_resolution("test_slot", "bla", "test_slot_type", "bla_id") \
        .with_slot_with_resolution("test2_slot", "foo", "test_slot_type", "foo_id") \
        .with_slot_with_resolution("test3_slot", "blabla", "test2_slot_type", "blabla_id")\
        .with_slot_with_resolution("test3_slot", "blabla2", "test2_slot_type", "blabla2_id")\
        .build()
    print(request_envelope)

    slot1 = request_envelope.request.intent.slots["test_slot"]
    assert len(slot1.resolutions.resolutions_per_authority) == 1
    values1 = slot1.resolutions.resolutions_per_authority[0].values
    assert len(values1) == 1
    assert values1[0].value.name == "bla"
    assert values1[0].value.id == "bla_id"

    slot2 = request_envelope.request.intent.slots["test2_slot"]
    assert len(slot2.resolutions.resolutions_per_authority) == 1
    values2 = slot2.resolutions.resolutions_per_authority[0].values
    assert len(values2) == 1
    assert values2[0].value.name == "foo"
    assert values2[0].value.id == "foo_id"

    slot3 = request_envelope.request.intent.slots["test3_slot"]
    assert len(slot3.resolutions.resolutions_per_authority) == 1
    values3 = slot3.resolutions.resolutions_per_authority[0].values
    assert len(values3) == 2
    assert values3[0].value.name == "blabla"
    assert values3[0].value.id == "blabla_id"
    assert values3[1].value.name == "blabla2"
    assert values3[1].value.id == "blabla2_id"
