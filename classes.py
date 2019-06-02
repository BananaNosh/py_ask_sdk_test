from ask_sdk_model import RequestEnvelope
from ask_sdk_model.interfaces.audioplayer import PlayBehavior, Stream, ClearBehavior
from ask_sdk_model.interfaces.videoapp import VideoItem


class TestItem:
    def __init__(self, request, expected_speech=None, expected_repromt=None, should_end_session=None,
                 session_attributes=None, profile_info=None, user_access_token=None,
                 check_question=True, expected_slot_to_elicit=None, expected_intent_for_elicitation=None,
                 should_confirm_slot=None, expected_attributes=None, expected_card_title=None, expected_card_text=None,
                 expected_image_url=None, expected_play_stream=None, should_stop_stream=None,
                 expected_clear_stream_behaviour=None, expected_video_item=None):
        """

        Args:
            request(RequestEnvelope): The request passed to the handler,
            which can be created with an AbstractRequestBuilder
            expected_speech(str): The speech which should be returned with the response (can be regex),
            empty string if nothing should be returned
            expected_repromt(str): The repromt which should be returned with the response (can be regex),
            empty string if nothing should be returned
            should_end_session(bool): The value of should_end_session, the response should contain
            session_attributes(dict): The session_attributes the request should start with
            profile_info(ProfileInfo): The the user's ProfileInfo
            user_access_token(str): the user's access_token
            check_question(bool): If it should be checked, that (speech ends with question mark) != should_end_session
            expected_slot_to_elicit(str): The name of the slot which should be elicit by the response
            expected_intent_for_elicitation: The name of the intent, whose slot should be elicit by the response
            should_confirm_slot(bool): TODO bool or string
            expected_attributes(dict): The attributes which should be returned with the response
            expected_card_title(str): The title of the card which should be returned with the response
            expected_card_text(str): The text of the card, that should be a SimpleCard,
            which should be returned with the response
            expected_image_url(str): The expected image url, which should be returned with a StandardCard
            expected_play_stream(PlayStreamConfig): The expected configuration to be returned with the response
            should_stop_stream(bool): If the stream should be stopped
            expected_clear_stream_behaviour(ClearBehavior): The expected clear behavior for the audio_player stream
            expected_video_item(VideoItem): The expected VideoItem returned with the response
        """
        self.request = request
        self.expected_speech = expected_speech
        self.expected_repromt = expected_repromt
        self.should_end_session = should_end_session
        self.session_attributes = session_attributes
        self.profile_info = profile_info
        self.user_access_token = user_access_token
        self.check_question = check_question
        self.expected_slot_to_elicit = expected_slot_to_elicit
        self.expected_intent_for_elicitation = expected_intent_for_elicitation
        self.should_confirm_slot = should_confirm_slot
        self.expected_attributes = expected_attributes
        self.expected_card_title = expected_card_title
        self.expected_card_text = expected_card_text
        self.expected_image_url = expected_image_url
        self.expected_play_stream = expected_play_stream
        self.should_stop_stream = should_stop_stream
        self.expected_clear_stream_behaviour = expected_clear_stream_behaviour
        self.expected_video_item = expected_video_item


class SkillSettings:
    def __init__(self, app_id, user_id, device_id, locale, debug=False):
        """
        Object to store skill settings
        Args:
            app_id(str): the skill id
            user_id(str): the user id to simulate
            device_id(str): the device id to simulate
            locale(str): the locale
            debug(bool): if in debug mode TODO
        """
        self.app_id = app_id
        self.user_id = user_id
        self.device_id = device_id
        self.locale = locale
        self.debug = debug


class ProfileInfo:
    def __init__(self, name=None, given_name=None, email=None, mobile_number=None):
        """
        Info about the users profile
        Args:
            name(str): the user's name
            given_name(str): the user's given name
            email(str): the user's email
            mobile_number(str): the user's mobile_number
        """
        self.name = name
        self.given_name = given_name
        self.email = email
        self.mobile_number = mobile_number


class PlayStreamConfig:
    def __init__(self, behavior=None, stream=None):
        """
        Config for a playStream
        Args:
            behavior(PlayBehavior): The behavior for the audio_player
            stream(Stream): The audio_player Stream
        """
        self.behavior = behavior
        self.stream = stream
