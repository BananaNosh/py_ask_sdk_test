import logging

from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model import Response
from ask_sdk_model.dialog import ElicitSlotDirective, ConfirmIntentDirective, ConfirmSlotDirective
from ask_sdk_model.ui import SimpleCard, StandardCard, Image
from ask_sdk_model.ui.plain_text_output_speech import PlainTextOutputSpeech

from handler_helper import get_most_probable_value_for_slot

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


speechs = {
    "launch": "Salve, gaudeo te videre!",
    "launch_repromt": "Vin aliquid dicere?",
    "dei": "Jupiter magnus est",
    "catull": "Odistine an amas?",
    "catull_repromt": "Odistine an amas?",
    "catull_card": "Da mi basia!",
    "nero": "Nonne pulcherrime canto?",
    "nero_card": "Placetne tibi ignis?",
}

images = {
    "nero": "https://de.wikipedia.org/wiki/Nero#/media/Datei:15-07-05-Schlo%C3%9F-Caputh-RalfR-N3S_1528.jpg"
}


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response

        handler_input.response_builder.speak(speechs["launch"]).ask(speechs["launch_repromt"])
        return handler_input.response_builder.response


class TaceIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("TaceIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        handler_input.response_builder.speak(None).ask(reprompt=None)
        return handler_input.response_builder.response


class DeiIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("DeiIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        handler_input.response_builder.response.output_speech = PlainTextOutputSpeech(text=speechs["dei"])
        handler_input.attributes_manager.session_attributes["sacrificium"] = "tres boves"
        return handler_input.response_builder.response


class CatullIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("CatullIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        handler_input.response_builder\
            .speak(speechs["catull"])\
            .ask(speechs["catull_repromt"])\
            .set_card(SimpleCard("Catull", speechs["catull_card"]))
        return handler_input.response_builder.response


class NeroIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("NeroIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        handler_input.response_builder.speak(speechs["nero"])\
            .add_directive(ConfirmIntentDirective())\
            .set_card(StandardCard("Nero", speechs["nero_card"],
                                   Image(images["nero"], images["nero"])))
        return handler_input.response_builder.response


class VarusIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool
        return is_intent_name("VarusIntent")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        slot_value = get_most_probable_value_for_slot(handler_input, "legiones")
        if slot_value is None:
            return handler_input.response_builder.add_directive(ElicitSlotDirective(slot_to_elicit="legiones")).response
        slot_value = get_most_probable_value_for_slot(handler_input, "ballistae")
        if slot_value is None:
            return handler_input.response_builder.add_directive(ElicitSlotDirective(slot_to_elicit="ballistae"))\
                .response
        slot_value = get_most_probable_value_for_slot(handler_input, "legati")
        if slot_value is None:
            return handler_input.response_builder.add_directive(ElicitSlotDirective(slot_to_elicit="legati")).response
        if int(slot_value) < 100:
            return handler_input.response_builder.add_directive(ConfirmSlotDirective(slot_to_confirm="legati")).response
        updated_intent = handler_input.request_envelope.request.intent
        updated_intent.name = "DeiIntent"
        return handler_input.response_builder.add_directive(ElicitSlotDirective(updated_intent)).response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TaceIntentHandler())
sb.add_request_handler(DeiIntentHandler())
sb.add_request_handler(CatullIntentHandler())
sb.add_request_handler(NeroIntentHandler())
sb.add_request_handler(VarusIntentHandler())
# sb.add_request_handler(HelpIntentHandler())
# sb.add_request_handler(CancelOrStopIntentHandler())
# sb.add_request_handler(FallbackIntentHandler())
# sb.add_request_handler(SessionEndedRequestHandler())

# sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()
