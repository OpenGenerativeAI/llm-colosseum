import numpy as np

KEN_RED = [248, 0, 0]
KEN_GREEN = [88, 176, 40]


def detect_position_from_color(
    observation: dict, color: list, epsilon=1, save_frame: bool = False
) -> tuple:
    """
    Convert the observation from pixels to player coordinates.

    It works by finding the first pixel that matches the color.

    Returns a tuple of (x, y) coordinates.
    - x is between 0 and 384
    - y is between 0 and 224
    """
    frame = observation["frame"]
    # the screen is a np.array of RGB colors (3 channels)
    # Select the frames where the characters play: between 80 vertical and 200 vertical

    # dump the observation to a file for debugging
    if save_frame:
        np.save("observation.npy", frame)

    frame = frame[100:200, :]

    # Detect the red color of Ken
    diff = np.linalg.norm(np.array(frame) - np.array(color), axis=2)
    mask = diff < epsilon

    # Return the index where the red color is detected
    coordinates = mask.nonzero()

    if len(coordinates[0]) == 0:
        return None

    # Add back the vertical offset
    first_match = (coordinates[1][0], coordinates[0][0] + 100)

    return first_match
