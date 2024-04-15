import dotenv

dotenv.load_dotenv()

MODELS = {
    "OPENAI": {
        "openai:gpt-4-0125-preview",
        "openai:gpt-4",
        "openai:gpt-3.5-turbo-0125",
        # "openai:gpt-3.5-turbo-instruct", # not a chat model
    },
    "MISTRAL": {
        "mistral:mistral-small-latest",
        "mistral:mistral-medium-latest",
        "mistral:mistral-large-latest",
        # "groq:mistral-8x6b-32768",
    },
    "GROQ": {"groq:gemma-7b-it"},
    "ANTHROPIC": {"anthropic:claude-3-haiku-20240307"},
}


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
MOVES_WITH_LOWER = {
    **MOVES,
    **{key.lower(): value for key, value in MOVES.items()},
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

SPECIAL_MOVES = {
    "EX-Fireball (Hadouken)": {"right": [7, 6, 5, 10, 10], "left": [7, 8, 1, 10, 10]},
    "EX-Dragon Punch (Shoryuken)": {
        "right": [
            MOVES["Right"],
            MOVES["Down"],
            MOVES["Down+Right"],
            MOVES["High Punch"],
            MOVES["High Punch"],
        ],
        "left": [
            MOVES["Left"],
            MOVES["Down"],
            MOVES["Down+Left"],
            MOVES["High Punch"],
            MOVES["High Punch"],
        ],
    },
    "Super Dragon Punch (Shouryuu-Reppa)": {
        "right": [
            MOVES["Right"],
            MOVES["Down"],
            MOVES["Down+Right"],
            MOVES["Right"],
            MOVES["Down"],
            MOVES["Down+Right"],
            MOVES["High Punch"],
        ],
        "left": [
            MOVES["Left"],
            MOVES["Down"],
            MOVES["Down+Left"],
            MOVES["Left"],
            MOVES["Down"],
            MOVES["Down+Left"],
            MOVES["High Punch"],
        ],
    },
    "Shippuu-Jinrai-Kyaku": {
        "right": [
            MOVES["Right"],
            MOVES["Down"],
            MOVES["Down+Right"],
            MOVES["Right"],
            MOVES["Down"],
            MOVES["Down+Right"],
            MOVES["High Punch"],
            MOVES["Low Kick"],
        ],
        "left": [
            MOVES["Left"],
            MOVES["Down"],
            MOVES["Down+Left"],
            MOVES["Left"],
            MOVES["Down"],
            MOVES["Down+Left"],
            MOVES["Low Kick"],
        ],
    },
}

META_INSTRUCTIONS = {
    "Move Closer": {"right": [5, 5, 5, 5], "left": [1, 1, 1, 1]},
    "Move Away": {"right": [1, 1, 1, 1], "left": [5, 5, 5, 5]},
    "Fireball": COMBOS["Fireball (Hadouken)"],
    "Megapunch": COMBOS["Dragon Punch (Shoryuken)"],
    "Hurricane": COMBOS["Hurricane Kick (Tatsumaki Senpukyaku)"],
    "Megafireball": SPECIAL_MOVES["EX-Fireball (Hadouken)"],
    "Super attack 2": SPECIAL_MOVES["EX-Dragon Punch (Shoryuken)"],
    "Super attack 3": SPECIAL_MOVES["Super Dragon Punch (Shouryuu-Reppa)"],
    "Super attack 4": SPECIAL_MOVES["Shippuu-Jinrai-Kyaku"],
    **{
        move_name: {"right": [move_nb, 0], "left": [move_nb, 0]}
        for move_name, move_nb in MOVES.items()
        if "Punch" in move_name or "Kick" in move_name
    },
    "Jump Closer": {"right": [4, 4, 4, 4], "left": [2, 2, 2, 2]},
    "Jump Away": {"right": [2, 2, 2, 2], "left": [4, 4, 4, 4]},
}
META_INSTRUCTIONS_WITH_LOWER = {
    **META_INSTRUCTIONS,
    **{key.lower(): value for key, value in META_INSTRUCTIONS.items()},
    ## Also add the combos for Lower, Medium and High
    "lower": {"right": [12, 0], "left": [12, 0]},
    "medium": {"right": [13, 0], "left": [13, 0]},
    "med": {"right": [13, 0], "left": [13, 0]},
    "high": {"right": [14, 0], "left": [14, 0]},
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

NB_FRAME_WAIT = 1
