MOVES = {
    "No-Move": 0,
    "Left": 1,
    "Left+Up": 2,
    "Up+Left": 2,
    "Up": 3,
    "Up+Right": 4,
    "Right+Up": 4,
    "Right": 5,
    "Right+Down": 6,
    "Down+Right": 6,
    "Down": 7,
    "Down+Left": 8,
    "Left+Down": 8,
    "Low Punch": 9,
    "Medium Punch": 10,
    "High Punch": 11,
    "Low Kick": 12,
    "Low": 12,
    "Medium Kick": 13,
    "Medium": 13,
    "High Kick": 14,
    "Low Punch+Low Kick": 15,
    "Medium Punch+Medium Kick": 16,
    "High Punch+High Kick": 17,
}
INDEX_TO_MOVE = {v: k for k, v in MOVES.items()}

X_SIZE = 384
Y_SIZE = 224
# TODO : Adds some combos to this
REAL_MOVE_LIST = [
    "No-Move",
    "Left",
    "Left+Up",
    "Up",
    "Right",
    "Right+Down",
    "Down",
    "Down+Left",
    "Low Punch",
    "Medium Punch",
    "High Punch",
    "Low Kick",
    "Medium Kick",
    "High Kick",
    "Low Punch+Low Kick",
    "Medium Punch+Medium Kick",
    "High Punch+High Kick",
]

NB_FRAME_WAIT = 3
