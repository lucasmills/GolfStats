# Utility function to scale values

def scale_value(value, orig_min, orig_max, new_min, new_max):
    """
    Scales a value from an original range to a new range.

    :param value: The value to scale
    :param orig_min: The minimum value of the original range
    :param orig_max: The maximum value of the original range
    :param new_min: The minimum value of the new range
    :param new_max: The maximum value of the new range
    :return: Scaled value in the new range
    """
    return ((value - orig_min) / (orig_max - orig_min)) * (new_max - new_min) + new_min
