"""
Take observations and return actions for the Robot to use
"""

import os
import random
import json
import re
import time
from typing import List, Optional

from loguru import logger

from agent.language_models import get_sync_client, get_provider_and_model

from .config import MOVES
from .prompts import build_main_prompt, build_system_prompt


tool = [
    {
        "type": "function",
        "function": {
            "name": "get_next_move",
            "description": "Get the next two moves the street fighter will do",
            "parameters": {
                "type": "object",
                "properties": {
                    "move1": {
                        "type": "string",
                        "enum": ["right", "left"],
                        "description": "The first move that will be done",
                    },
                },
                "required": ["move1"],
            },
        },
    },
]


def call_llm(
    context_prompt: str,
    character: str,
    model: str = "mistral:mistral-large-latest",
    temperature: float = 0.0,
    max_tokens: int = 200,
    wrong_answer: Optional[str] = None,
    top_p: float = 1.0,
) -> str:
    """
    Get actions from the language model
    context_prompt: str, the prompt to describe the situation to the LLM. Will be placed inside the main prompt template.
    """
    # Get the correct provider, default is mistral
    provider_name, model_name = get_provider_and_model(model)
    client = get_sync_client(provider_name)

    # Generate the prompts
    system_prompt = build_system_prompt(character)
    main_prompt = build_main_prompt(context_prompt, wrong_answer)

    start_time = time.time()

    completion = client.chat.completions.create(
        model=model_name,
        tools=tool,
        tool_choice="auto",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": main_prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    logger.debug(f"LLM call: {system_prompt}\n\n\n{main_prompt}")
    logger.debug(f"LLM call to {model}: {time.time() - start_time} s")

    llm_response = completion.choices[0].message

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

    # If we are in the test environment, we don't want to call the LLM
    if os.getenv("DISABLE_LLM", "False") == "True":
        # Choose a random int from the list of moves
        logger.debug("DISABLE_LLM is True, returning a random move")
        return [random.choice(list(MOVES.values()))]

    while len(valid_moves) == 0 or len(invalid_moves) > 2:
        llm_response = call_llm(
            context_prompt=context_prompt,
            character=character,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            wrong_answer=wrong_answer,
        )
        logger.info(f"LLM response: {llm_response}")

        moves = []
        # Get the moves from the response
        tool_called = llm_response.tool_calls[0]
        # Extract the function
        function = tool_called.function
        try:
            # Check if the function name is 'get_next_move'
            if function.name == "get_next_move":
                # Parse the arguments JSON string into a dictionary
                arguments = json.loads(function.arguments)

                # Extract the moves
                moves.append(arguments["move1"])
        except Exception as e:
            logger.error(f"Error parsing the LLM response: {e}")

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

    logger.debug(f"Next moves: {valid_moves}")

    return valid_moves
