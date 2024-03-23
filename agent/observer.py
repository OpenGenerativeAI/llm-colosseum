KEN_RED = [227, 49, 34]
KEN_GREEN = [107, 189, 62]
RYU_WHITE = [248, 248, 248]


def detect_position_from_color(observation: dict, color=list) -> tuple:
    """
    Convert the observation from pixels to player coordinates.

    It works by finding the first pixel that matches the color.

    Returns a tuple of (x, y) coordinates.
    """
    frame = observation["frame"]
    # the screen is a np.array of RGB colors (3 channels)
    # Select the frames where the characters play: between 80 vertical and 200 vertical

    frame = frame[:, 80:200]

    # Detect the red color of Ken
    mask = frame == KEN_RED
    # Return the index where the red color is detected
    coordinates = mask.any(axis=2).nonzero()

    first_match = coordinates[0][0], coordinates[1][0]

    # Add back the vertical offset
    first_match[1] = first_match[1] + 80

    return first_match
