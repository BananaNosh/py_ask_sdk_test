from ask_sdk_model import RequestEnvelope


class TestItem:
    def __init__(self, request):
        """

        Args:
            request(RequestEnvelope):
        """
        self.request = request


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
