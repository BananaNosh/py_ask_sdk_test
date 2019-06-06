import logging

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model.ui import SimpleCard
from ask_sdk_model import Response

sb = SkillBuilder()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


speechs = {
    "launch": "Salve, gaudeo te videre!",
    "launch_repromt": "Vin aliquid dicere?"
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




sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TaceIntentHandler())
# sb.add_request_handler(HelpIntentHandler())
# sb.add_request_handler(CancelOrStopIntentHandler())
# sb.add_request_handler(FallbackIntentHandler())
# sb.add_request_handler(SessionEndedRequestHandler())

# sb.add_exception_handler(CatchAllExceptionHandler())

handler = sb.lambda_handler()