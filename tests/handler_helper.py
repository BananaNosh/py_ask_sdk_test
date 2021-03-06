import logging

from ask_sdk_core.handler_input import HandlerInput


def get_slot_resolutions_from_handler(handler_input, slot_name):
    """
    Get the resolutions for the slot from the handler_input.
    Args:
        handler_input(HandlerInput): the handler input
        slot_name(str): the slot's name

    Returns: (list(Resolution)|None) the found resolutions or None
    """
    request = handler_input.request_envelope.request
    try:
        resolutions = request.intent.slots[slot_name].resolutions
        return (resolutions.
                resolutions_per_authority[0].values)
    except (AttributeError, ValueError, KeyError, IndexError, TypeError) as e:
        get_logger().info("Couldn't resolve slot {} for request: {}".format(slot_name, request))
        get_logger().info(str(e))
        return None


def get_most_probable_value_for_slot(handler_input, slot_name):
    """
    Get the value for the slot, if necessary, by taking the value from the most probable resolution
    Args:
        handler_input(HandlerInput): the handler input
        slot_name(str): the slot's name

    Returns: (str|None) The value for the slot or None if no value given
    """
    request = handler_input.request_envelope.request
    try:
        slot_values = get_slot_resolutions_from_handler(handler_input, slot_name)
        if slot_values is None:
            slot = request.intent.slots[slot_name]
            if slot.value is not None:
                get_logger().info("value is in slot {}".format(slot_name))
                return slot.value
            return None
        return slot_values[0].value.id
    except (AttributeError, ValueError, KeyError, IndexError, TypeError) as e:
        get_logger().info("Couldn't get value for slot {} for request: {}".format(slot_name, request))
        get_logger().info(str(e))
        return None


def get_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    return logger
