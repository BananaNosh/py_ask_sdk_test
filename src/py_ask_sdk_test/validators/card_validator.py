import re

from ask_sdk_model.ui.simple_card import SimpleCard
from ask_sdk_model.ui.standard_card import StandardCard

from py_ask_sdk_test.validators.abstract_response_validator import AbstractResponseValidator


class CardValidator(AbstractResponseValidator):
    """
    Validator against expected CardValues
    """

    def validate(self, test_item, response):
        """
        Validates the given response for the given test_item against expected CardValues
            test_item(TestItem): The TestItem the response was given for
            response(ResponseEnvelope): The response
        Returns: True if the validation was successful otherwise should throw assertion
        """
        if not test_item.expected_card_text and not test_item.expected_card_title \
                and not test_item.expected_card_content and not test_item.expected_small_image_url:
            return True
        card = response.response.card
        assert card is not None
        if test_item.expected_card_title:
            assert type(card) is SimpleCard or type(card) is StandardCard
            assert test_item.expected_card_title == card.title
        if test_item.expected_card_text:
            assert type(card) is StandardCard
            msg = "Card text was wrong"
            card_text = card.text
            expected_card_text = test_item.expected_card_text
            self.assert_text_with_regex(card_text, expected_card_text, msg)
        if test_item.expected_card_content:
            assert type(card) is SimpleCard
            msg = "Card content was wrong"
            card_content = card.content
            expected_card_content = test_item.expected_card_content
            self.assert_text_with_regex(card_content, expected_card_content, msg)
        if test_item.expected_small_image_url is not None:
            assert type(card) is StandardCard
            assert card.image
            assert test_item.expected_small_image_url == card.image.small_image_url
        if test_item.expected_large_image_url is not None:
            assert type(card) is StandardCard
            assert card.image
            assert test_item.expected_large_image_url == card.image.large_image_url
        return True

    @staticmethod
    def assert_text_with_regex(text, expected_text, msg):
        is_regex = False
        if type(expected_text) is tuple:
            is_regex = expected_text[1]
            expected_text = expected_text[0]
        if is_regex:
            match = re.fullmatch(expected_text, text)
            assert match is not None, msg + ": {} instead of {}".format(text, expected_text)
        else:
            assert expected_text == text
