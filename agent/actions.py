"""
Take observations and return actions for the Robot to use
"""

from agent.language_models import get_sync_client  # Change to async later

from .prompts import build_system_prompt, build_main_prompt
from .robot import MOVES
import time

from loguru import logger


def get_actions_from_llm(
    context_prompt: str,
    model_name: str = "mistral-large-latest",
    temperature: float = 0.1,
    max_tokens: int = 20,
    top_p: float = 1.0,
) -> int:
    """
    Get actions from the language model
    context_prompt: str, the prompt to describe the situation to the LLM. Will be placed inside the main prompt template.
    """
    client = get_sync_client("mistral")

    # Generate the prompts
    system_prompt = build_system_prompt()
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

    logger.debug(f"LLM call to {model_name}: {time.time() - start_time} s")

    llm_response = completion.choices[0].message.content

    # Validate the completion format
    if llm_response not in MOVES.keys():
        logger.warning(f"Invalid completion: {llm_response}")
        prompt_with_correction = build_main_prompt(wrong_answer=llm_response)

        start_time = time.time()

        completion = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_with_correction},
            ],
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
        )

        logger.debug(f"LLM call to {model_name}: {time.time() - start_time} s")

        llm_response = completion.choices[0].message.content

        if llm_response not in MOVES.keys():
            raise ValueError(
                f"Invalid completion (even after one error injection): {llm_response}"
            )

    return llm_response
