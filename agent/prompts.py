from .robot import MOVES


def build_system_prompt() -> str:
    prompt = "Your are a helpful assistant playing a character in the game Street Fighter. Your goal it to beat the other opponent. You can do the following moves: \n"

    for move in MOVES.keys():
        prompt += f"{move}\n"

    return prompt


def build_main_prompt() -> str:
    """
    TODO: Takes as argument an observation of the world and returns a prompt for the language model
    """

    prompt = "Choose randomly a move to make. "
    prompt += "Only respond with the move you want to make. It must be only the name of the move in the list of mooves."

    return prompt
