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
COMBOS = {
    "Fireball (Hadouken)": {"right": [7, 6, 5, 10], "left": [7, 8, 1, 10]},
    # Refacto with command names
    "Dragon Punch (Shoryuken)": {
        "right": [
            MOVES["Right"],
            MOVES["Down"],
            MOVES["Down+Right"],
            MOVES["High Punch"],
        ],
        "left": [MOVES["Left"], MOVES["Down"], MOVES["Down+Left"], MOVES["High Punch"]],
    },
    "Hurricane Kick (Tatsumaki Senpukyaku)": {
        "right": [MOVES["Down"], MOVES["Down+Left"], MOVES["Left"], MOVES["Low Kick"]],
        "left": [MOVES["Down"], MOVES["Down+Right"], MOVES["Right"], MOVES["Low Kick"]],
    },
}

META_INSTRUCTIONS = {
    "Move closer": {"right": [5, 5, 5, 5], "left": [1, 1, 1, 1]},
    "Move away": {"right": [1, 1, 1, 1], "left": [5, 5, 5, 5]},
    "Normal punch": {"right": [10, 0], "left": [10, 0]},
    "Normal kick": {"right": [13, 0], "left": [13, 0]},
    "Fireball": COMBOS["Fireball (Hadouken)"],
    "Dragon Punch": COMBOS["Dragon Punch (Shoryuken)"],
    "Hurricane Kick": COMBOS["Hurricane Kick (Tatsumaki Senpukyaku)"],
}

for key in MOVES.keys():
    # Check if it's a kick or a punch
    if "Punch" in key:
        META_INSTRUCTIONS[key] = {"right": [MOVES[key], 0], "left": [MOVES[key], 0]}
    elif "Kick" in key and "Punch" not in key:
        META_INSTRUCTIONS[key] = {"right": [MOVES[key], 0], "left": [MOVES[key], 0]}

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
