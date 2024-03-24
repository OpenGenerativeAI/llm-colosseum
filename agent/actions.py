"""
Take observations and return actions for the Robot to use
"""

import os
import random
import re
import time
from typing import List, Optional

from loguru import logger

from agent.language_models import get_sync_client  # Change to async later

from .config import MOVES
from .prompts import build_main_prompt, build_system_prompt


def call_llm(
    context_prompt: str,
    character: str,
    model_name: str = "mistral-large-latest",
    temperature: float = 0.3,
    max_tokens: int = 20,
    top_p: float = 1.0,
    wrong_answer: Optional[str] = None,
) -> str:
    """
    Get actions from the language model
    context_prompt: str, the prompt to describe the situation to the LLM. Will be placed inside the main prompt template.
    """

    # If we are in the test environment, we don't want to call the LLM
    if os.getenv("DISABLE_LLM", "False") == "True":
        # Choose a random move
        return random.choice(list(MOVES.keys()))

    client = get_sync_client("mistral")

    # Generate the prompts
    system_prompt = build_system_prompt(character)
    main_prompt = build_main_prompt(context_prompt, wrong_answer)
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
    logger.debug(f"LLM call: {system_prompt}\n\n\n{main_prompt}")
    logger.debug(f"LLM call to {model_name}: {time.time() - start_time} s")

    llm_response = completion.choices[0].message.content.strip()

    return llm_response


def get_simple_actions_from_llm(
    context_prompt: str,
    character: str,
    model_name: str = "mistral-large-latest",
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
    model_name: str = "mistral-large-latest",
    temperature: float = 0.1,
    max_tokens: int = 20,
    top_p: float = 1.0,
) -> List[int]:
    """
    Get actions from the language model
    context_prompt: str, the prompt to describe the situation to the LLM.

    Will be placed inside the main prompt template.
    """

    # Filter the moves that are not in the list of moves
    invalid_moves = []
    valid_moves = []
    wrong_answer = None

    while len(valid_moves) == 0 or len(invalid_moves) > 2:
        llm_response = call_llm(
            context_prompt=context_prompt,
            character=character,
            model_name=model_name,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            wrong_answer=wrong_answer,
        )

        # The response is a bullet point list of moves. Use regex
        moves = re.findall(r"- (\w+)", llm_response)
        invalid_moves = []
        valid_moves = []
        for move in moves:
            if move in MOVES.keys():
                valid_moves.append(move)
            else:
                logger.debug(f"Invalid completion: {move}")
                invalid_moves.append(move)

        if len(invalid_moves) > 2:
            logger.warning(f"Too many invalid moves: {invalid_moves}")
            wrong_answer = llm_response

    # Cast the moves to their index
    valid_moves = [MOVES[m] for m in valid_moves]

    return valid_moves
