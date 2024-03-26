from .config import META_INSTRUCTIONS


def build_system_prompt(character: str, context_prompt: str) -> str:
    move_list = "- " + "\n - ".join([move for move in META_INSTRUCTIONS])

    system_prompt = f"""You are the best and most aggressive Street Fighter III 3rd strike player in the world. 
Your character is {character}. Your goal it to beat the other opponent. You respond with a bullet point list of moves.
{context_prompt}
The moves you can use are:
----
{move_list}
----
Reply with a bullet point list of moves. The format should be: `- <name of the move>` separated by a new line.
Example if the opponent is close:
- Move closer
- Medium Punch

Example if the opponent is far:
- Fireball
- Move closer
"""
    return system_prompt


def build_main_prompt() -> str:
    """
    TODO: Takes as argument an observation of the world and returns a prompt for the language model
    wrong_answer: str, the wrong answer, to inject in the prompt to ask for a regenrated answer
    """

    prompt = "Your next moves are:"

    return prompt
