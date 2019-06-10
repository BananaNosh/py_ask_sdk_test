from ask_sdk_model.dialog import ElicitSlotDirective, ConfirmSlotDirective, ConfirmIntentDirective

from py_ask_sdk_test.validators.abstract_response_validator import AbstractResponseValidator


class DialogValidator(AbstractResponseValidator):
    """
    Validator against elicitation and confirmation of slots
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against elicitation and confirmation of slots
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        if not test_item.expected_slot_to_elicit and not test_item.expected_intent_for_elicitation \
                and not test_item.expected_slot_to_confirm and test_item.should_confirm_intent is None:
            return True
        assert response.response.directives
        directives_for_type = {}
        for d in response.response.directives:
            directives_for_type[type(d)] = d
        if test_item.expected_slot_to_elicit or test_item.expected_intent_for_elicitation:
            assert ElicitSlotDirective in directives_for_type
            elicit_slot_directive = directives_for_type[ElicitSlotDirective]
            if test_item.expected_slot_to_elicit:
                assert test_item.expected_slot_to_elicit == elicit_slot_directive.slot_to_elicit
            if test_item.expected_intent_for_elicitation:
                assert elicit_slot_directive.updated_intent is not None
                assert test_item.expected_intent_for_elicitation == elicit_slot_directive.updated_intent.name
        if test_item.expected_slot_to_confirm:
            assert ConfirmSlotDirective in directives_for_type
            confirm_slot_directive = directives_for_type[ConfirmSlotDirective]
            assert test_item.expected_slot_to_confirm == confirm_slot_directive.slot_to_confirm
        if test_item.should_confirm_intent is not None:
            assert test_item.should_confirm_intent == (ConfirmIntentDirective in directives_for_type)
        return True
