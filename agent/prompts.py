from .robot import MOVES


def build_system_prompt() -> str:
    prompt = "Your are a helpful assistant playing a character in the game Street Fighter. Your goal it to beat the other opponent. You can do the following moves: \n"

    for move in MOVES.keys():
        prompt += f"{move}\n"

    return prompt


def build_main_prompt(context: str, wrong_answer="") -> str:
    """
    TODO: Takes as argument an observation of the world and returns a prompt for the language model
    wrong_answer: str, the wrong answer, to inject in the prompt to ask for a regenrated answer
    """

    prompt = "The context of the game is as follows: \n"
    prompt += context
    prompt += "\n"
    prompt += "Only respond with the move you want to make. It must be only the name of the move in the list of mooves."

    if wrong_answer:
        prompt += f"Your previous answer was {wrong_answer}. It was wrong because you didn't answered with only a moove from the list of mooves. Please provide a move from the list of moves."

    return prompt
