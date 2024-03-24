from typing import Optional
from .config import REAL_MOVE_LIST, NB_FRAME_WAIT
import random
from typing import List


def build_system_prompt(character: str) -> str:
    move_list = "\n - ".join(REAL_MOVE_LIST)

    system_prompt = f"""You are the best and most aggressive player in the world. \
    You're playing Street Fighter III 3rd strike with the character {character}. \
You reply the moves you want to do in the next frames"""
    return system_prompt


def build_main_prompt(
    context: str, previous_actions: List[dict], wrong_answer: Optional[str] = None
) -> str:
    """
    TODO: Takes as argument an observation of the world and returns a prompt for the language model
    wrong_answer: str, the wrong answer, to inject in the prompt to ask for a regenrated answer
    """
    # Generate a random float to avoid caching
    random_seed = random.random()

    # Generate the text of the previous actions
    # We remove the frames where we wait

    prompt = f"""Time of the game: {random_seed}
The context of the game is:
{context}
Use the function to answer with the moves you want.  Do not \
include moves that are not in the list of moves. Do not include any other information. Only use the function \
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
