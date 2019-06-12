import logging

import requests
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.utils import is_request_type, is_intent_name
from ask_sdk_model.dialog import ElicitSlotDirective, ConfirmIntentDirective, ConfirmSlotDirective
from ask_sdk_model.interfaces.audioplayer import PlayDirective, PlayBehavior, AudioItem, Stream, AudioItemMetadata
from ask_sdk_model.interfaces.audioplayer import StopDirective, ClearQueueDirective, ClearBehavior
from ask_sdk_model.interfaces.videoapp import LaunchDirective, VideoItem, Metadata
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
    """Handles the LaunchRequest"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler

        Returns: (bool) If this handler can handle the input

        """
        return is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """

        handler_input.response_builder.speak(speechs["launch"]).ask(speechs["launch_repromt"])
        return handler_input.response_builder.response


class TaceIntentHandler(AbstractRequestHandler):
    """Handles the TaceIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_intent_name("TaceIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        handler_input.response_builder.speak(None).ask(reprompt=None) \
            .add_directive(ClearQueueDirective(ClearBehavior.CLEAR_ALL))
        return handler_input.response_builder.response


class DeiIntentHandler(AbstractRequestHandler):
    """Handles the DeiIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_intent_name("DeiIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """

        is_remote = "remotus" in handler_input.attributes_manager.session_attributes
        if is_remote:
            remote_response = requests.get("https://ptsv2.com/t/olympus")
            return handler_input.response_builder\
                .speak("Olympus respondit: {}".format(remote_response.status_code)).response
        # No clue why the following line is necessary (pycharm does not see that context has a system attribute)
        # noinspection PyUnresolvedReferences
        name_response = requests.get("{}v2/accounts/~current/settings/Profile.name"
                                     .format(handler_input.context.system.api_endpoint))
        name = None
        if name_response.status_code == 200:
            name = name_response.json()

        if name is not None:
            return handler_input.response_builder.speak("{} potens est.".format(name)).response

        handler_input.response_builder.response.output_speech = PlainTextOutputSpeech(text=speechs["dei"])
        handler_input.attributes_manager.session_attributes["sacrificium"] = "tres boves"
        return handler_input.response_builder.response


class CatullIntentHandler(AbstractRequestHandler):
    """Handles the CatullIntent"""

    """Handles the CatullIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler

        Returns: (bool) If this handler can handle the input

        """
        return is_intent_name("CatullIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        handler_input.response_builder \
            .speak(speechs["catull"]) \
            .ask(speechs["catull_repromt"]) \
            .set_card(SimpleCard("Catull", speechs["catull_card"]))
        return handler_input.response_builder.response


class NeroIntentHandler(AbstractRequestHandler):
    """Handles the NeroIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_intent_name("NeroIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        handler_input.response_builder.speak(speechs["nero"]) \
            .add_directive(ConfirmIntentDirective()) \
            .set_card(StandardCard("Nero", speechs["nero_card"],
                                   Image(images["nero"], images["nero"])))
        return handler_input.response_builder.response


class VarusIntentHandler(AbstractRequestHandler):
    """Handles the VarusIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_intent_name("VarusIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        slot_value = get_most_probable_value_for_slot(handler_input, "legiones")
        if slot_value is None:
            return handler_input.response_builder.add_directive(ElicitSlotDirective(slot_to_elicit="legiones")).response
        slot_value = get_most_probable_value_for_slot(handler_input, "ballistae")
        if slot_value is None:
            return handler_input.response_builder.add_directive(ElicitSlotDirective(slot_to_elicit="ballistae")) \
                .response
        slot_value = get_most_probable_value_for_slot(handler_input, "legati")
        if slot_value is None:
            return handler_input.response_builder.add_directive(ElicitSlotDirective(slot_to_elicit="legati")).response
        if int(slot_value) < 100:
            return handler_input.response_builder.add_directive(ConfirmSlotDirective(slot_to_confirm="legati")).response
        updated_intent = handler_input.request_envelope.request.intent
        updated_intent.name = "DeiIntent"
        return handler_input.response_builder.add_directive(ElicitSlotDirective(updated_intent)).response


class OrpheusIntentHandler(AbstractRequestHandler):
    """Handles the OrpheusIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_intent_name("OrpheusIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        pellicula_slot = get_most_probable_value_for_slot(handler_input, "pellicula")
        if pellicula_slot is None:
            handler_input.response_builder.add_directive(
                PlayDirective(PlayBehavior.REPLACE_ALL,
                              AudioItem(Stream(token="cantare_token", url="https://"),
                                        AudioItemMetadata("Highway to hell"))))
        else:
            handler_input.response_builder \
                .add_directive(LaunchDirective(VideoItem("https://", Metadata("Orpheus et Eurydike"))))
        return handler_input.response_builder.response


class ResumeIntentHandler(AbstractRequestHandler):
    """Handles the ResumeIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_intent_name("AMAZON.ResumeIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        handler_input.response_builder.add_directive(
            PlayDirective(PlayBehavior.REPLACE_ALL,
                          AudioItem(Stream(token="lyra_token", url="https://"), AudioItemMetadata("Highway to hell"))))
        return handler_input.response_builder.response


class PauseIntentHandler(AbstractRequestHandler):
    """Handles the PauseIntent"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_intent_name("AMAZON.PauseIntent")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        handler_input.response_builder.add_directive(StopDirective())
        return handler_input.response_builder.response


class SessionEndedRequestHandler(AbstractRequestHandler):
    """Handles the session end of the skill"""

    def can_handle(self, handler_input):
        """
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (bool) If this handler can handle the input
        """
        return is_request_type("SessionEndedRequest")(handler_input)

    def handle(self, handler_input):
        """
        Creates a response for the given input
        Args:
            handler_input(HandlerInput): The input to the handler
        Returns: (Response) The response
        """
        return handler_input.response_builder.response


sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(TaceIntentHandler())
sb.add_request_handler(DeiIntentHandler())
sb.add_request_handler(CatullIntentHandler())
sb.add_request_handler(NeroIntentHandler())
sb.add_request_handler(VarusIntentHandler())
sb.add_request_handler(OrpheusIntentHandler())
sb.add_request_handler(ResumeIntentHandler())
sb.add_request_handler(PauseIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

handler = sb.lambda_handler()
