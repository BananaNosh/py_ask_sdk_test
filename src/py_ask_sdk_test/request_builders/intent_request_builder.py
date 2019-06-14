import datetime

from ask_sdk_model import IntentRequest, Intent, IntentConfirmationStatus, Slot, SlotConfirmationStatus
from ask_sdk_model.slu.entityresolution import Resolutions, Resolution, ValueWrapper, Value, Status, StatusCode

from py_ask_sdk_test.request_builders.abstract_request_builder import AbstractRequestBuilder


class IntentRequestBuilder(AbstractRequestBuilder):
    def __init__(self, intent_name, skill_settings):
        """
        RequestBuilder for an IntentRequest
        Args:
            intent_name(str): The Intent's name
            skill_settings(SkillSettings): The settings of the tested skill
        """
        super(IntentRequestBuilder, self).__init__(skill_settings)
        self.intent_name = intent_name
        self.slots = {}

    def build_request(self):
        """
        Builds the request
        Returns: (IntentRequest) the build IntentRequest
        """
        return IntentRequest(request_id=self.request_id,
                             timestamp=datetime.datetime.now(),
                             locale=self.skill_settings.locale,
                             intent=Intent(self.intent_name, self.slots, IntentConfirmationStatus.NONE))

    def with_empty_slot(self, slot_name):
        """
        Add an empty slot to the intent
        Args:
            slot_name(str): the name of the slot
        Returns: (IntentRequestBuilder) self
        """
        return self.with_slot(slot_name, None)

    def with_slot(self, slot_name, value):
        """
        Add a slot with a value to the intent
        Args:
            slot_name(str): the name of the slot
            value(Any): the value to be added
        Returns: (IntentRequestBuilder) self

        """
        if slot_name in self.slots:
            self.slots[slot_name].value = value
        else:
            self.slots[slot_name] = Slot(slot_name, value, SlotConfirmationStatus.NONE)
        return self

    def with_slot_with_resolution(self, slot_name, value, slot_type, slot_value_id):
        """
        Add a slot with its resolution to the intent
        Args:
            slot_name(str): the name of the slot
            value(Any): the resolved value to be added
            slot_type(str): the name of the slot_type
            slot_value_id(str): the id of the resolved value
        Returns: (IntentRequestBuilder) self
        """
        self.with_slot(slot_name, value)
        authority = "amzn1.er-authority.echo-sdk.{}.{}".format(self.skill_settings.app_id, slot_type)
        value_added = False
        if self.slots[slot_name].resolutions:
            for res in self.slots[slot_name].resolutions.resolutions_per_authority:
                if res.authority == authority:
                    res.values.append(ValueWrapper(Value(value, slot_value_id)))
                    value_added = True
                    break

        else:
            self.slots[slot_name].resolutions = Resolutions([])

        if not value_added:
            self.slots[slot_name].resolutions.resolutions_per_authority\
                .append(Resolution(authority=authority,
                                   status=Status(StatusCode.ER_SUCCESS_MATCH),
                                   values=[
                                       ValueWrapper(Value(value, slot_value_id))
                                   ]))
        return self

    def with_slot_with_resolution_no_match(self, slot_name, value, slot_type):
        """
        Add a slot with a resolution without match to the intent
        Args:
            slot_name(str): the name of the slot
            value(Any): the value to be added
            slot_type(str): the name of the slot_type
        Returns: (IntentRequestBuilder) self
        """
        # noinspection PyTypeChecker
        self.with_slot_with_resolution(slot_name, value, slot_type, None)
        last_added_resolution = self.slots[slot_name].resolutions.resolutions_per_authority[-1]
        last_added_resolution.status = Status(StatusCode.ER_SUCCESS_NO_MATCH)
        last_added_resolution.values = []
        return self
