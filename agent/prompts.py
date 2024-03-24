from typing import Optional
from .config import REAL_MOVE_LIST


def build_system_prompt(character: str) -> str:
    system_prompt = f"""You're playing Street Fighter III 3rd strike with the character {character}. \
Your goal it to beat the other opponent. You can do the following moves: \n
{''.join([f'- {move}' for move in REAL_MOVE_LIST])}
You reply with a bullet point list of moves. The format should be: `- move` separated by a new line."""
    return system_prompt


def build_main_prompt(context: str, wrong_answer: Optional[str] = None) -> str:
    """
    TODO: Takes as argument an observation of the world and returns a prompt for the language model
    wrong_answer: str, the wrong answer, to inject in the prompt to ask for a regenrated answer
    """

    prompt = f"""The context of the game is:
{context}
Response with a bullet point list of the moves you want to do. Do not \
include moves that are not in the list of moves. Do not include any other information. \
The format should be: `- move` separated by a new line.
"""

    if wrong_answer:
        prompt += f"""Your previous answer was:
[PREVIOUS ANSWER]
{wrong_answer}
[END PREVIOUS ANSWER]
It was wrong because you answered with too many moves that are not in move list. \
Please provide a move from the list of moves."""

    prompt += "\nYour next moves are:\n"

    return prompt
