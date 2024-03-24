"""
Take observations and return actions for the Robot to use
"""

import os
import random
import re
import time
from typing import List, Optional
from rich import print

from loguru import logger

from agent.language_models import get_sync_client, get_provider_and_model

from .config import MOVES, META_INSTRUCTIONS, META_INSTRUCTIONS_WITH_LOWER
from .prompts import build_main_prompt, build_system_prompt


def call_llm(
    context_prompt: str,
    character: str,
    model: str = "mistral:mistral-large-latest",
    temperature: float = 0.3,
    max_tokens: int = 20,
    top_p: float = 1.0,
    wrong_answer: Optional[str] = None,
) -> str:
    """
    Get actions from the language model
    context_prompt: str, the prompt to describe the situation to the LLM. Will be placed inside the main prompt template.
    """
    # Get the correct provider, default is mistral
    provider_name, model_name = get_provider_and_model(model)
    client = get_sync_client(provider_name)

    # Generate the prompts
    system_prompt = build_system_prompt(
        character=character, context_prompt=context_prompt
    )
    main_prompt = build_main_prompt()

    start_time = time.time()

    completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": main_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
    )
    logger.debug(f"LLM call to {model}: {system_prompt}\n\n\n{main_prompt}")
    logger.debug(f"LLM call to {model}: {time.time() - start_time} s")

    llm_response = completion.choices[0].message.content.strip()

    return llm_response


def get_simple_actions_from_llm(
    context_prompt: str,
    character: str,
    model: str = "mistral:mistral-large-latest",
    temperature: float = 0.1,
    max_tokens: int = 20,
    top_p: float = 1.0,
) -> List[int]:
    """
    Get actions from the language model
    context_prompt: str, the prompt to describe the situation to the LLM.
    Return one action and then wait for the next observation

    Will be placed inside the main prompt template.
    """
    pass


def get_actions_from_llm(
    context_prompt: str,
    character: str,
    model: str = "mistral:mistral-large-latest",
    temperature: float = 0.1,
    max_tokens: int = 20,
    top_p: float = 1.0,
    player_nb: int = 0,  # 0 for unspecified, 1 for player 1, 2 for player 2
) -> List[str]:
    """
    Get actions from the language model
    context_prompt: str, the prompt to describe the situation to the LLM.

    Will be placed inside the main prompt template.
    """

    # Filter the moves that are not in the list of moves
    invalid_moves = []
    valid_moves = []
    wrong_answer = None

    # If we are in the test environment, we don't want to call the LLM
    if os.getenv("DISABLE_LLM", "False") == "True":
        # Choose a random int from the list of moves
        logger.debug("DISABLE_LLM is True, returning a random move")
        return [random.choice(list(MOVES.values()))]

    while len(valid_moves) == 0:
        llm_response = call_llm(
            context_prompt=context_prompt,
            character=character,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            wrong_answer=wrong_answer,
        )

        # The response is a bullet point list of moves. Use regex
        matches = re.findall(r"- ([\w ]+)", llm_response)
        moves = ["".join(match) for match in matches]
        invalid_moves = []
        valid_moves = []
        for move in moves:
            cleaned_move_name = move.strip().lower()
            if cleaned_move_name in META_INSTRUCTIONS_WITH_LOWER.keys():
                if player_nb == 1:
                    print(f"[red] Player {player_nb} move: {cleaned_move_name}")
                elif player_nb == 2:
                    print(f"[green] Player {player_nb} move: {cleaned_move_name}")
                valid_moves.append(cleaned_move_name)
            else:
                logger.debug(f"Invalid completion: {move}")
                logger.debug(f"Cleaned move name: {cleaned_move_name}")
                invalid_moves.append(move)

        if len(invalid_moves) > 2:
            logger.warning(f"Too many invalid moves: {invalid_moves}")
            wrong_answer = llm_response

    logger.debug(f"Next moves: {valid_moves}")

    return valid_moves
