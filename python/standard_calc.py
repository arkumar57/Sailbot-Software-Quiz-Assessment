def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """

    upper_bound = 180
    lower_bound = -180

    # Repeatedly shifts the angle until it is between [-180, 180)
    while (angle > upper_bound or angle < lower_bound):
        if (angle > upper_bound):
            angle = angle - 360
        else:
            angle = angle + 360
    return angle


def bound_to_0_to_360(angle):

    """ Helper Function
    Bounds the provided angle to the range [0, 360) degrees.
    Args:
        angle (float): Input angle in degrees.
    Returns:
        float: Angle bounded to [0, 360).
    """
    # Shifts angle upwards if negative
    while (angle < 0):
        angle = angle + 360
    # Shifts angle downwards if >= 360
    while (angle >= 360):
        angle = angle - 360
    return angle


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.
    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False
    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.
    Returns:
        bool: True when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    # bounds first_angle, middle_angle, second_angle between [0, 360)
    first_angle = bound_to_0_to_360(first_angle)
    middle_angle = bound_to_0_to_360(middle_angle)
    second_angle = bound_to_0_to_360(second_angle)
    # computes counter clockwise angles from first_angle to middle and second
    angle_from_first_to_middle = (middle_angle - first_angle) % 360
    angle_from_first_to_second = (second_angle - first_angle) % 360
    # Check if angle between first_angle and second_angle is not reflex angle
    if (angle_from_first_to_second <= 180):
        # return true if middle_angle is between first_angle and second_angle
        return angle_from_first_to_middle <= angle_from_first_to_second
    else:
        # return true if middle_angle lies on shorter arc that cycles around 0 degrees
        return angle_from_first_to_middle >= angle_from_first_to_second
