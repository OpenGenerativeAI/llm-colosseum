"""
Take observations and return actions for the Robot to use
"""

from agent.language_models import get_sync_client  # Change to async later

from .prompts import build_system_prompt, build_main_prompt
from .robot import MOVES


def get_actions_from_llm(
    context_prompt: str,
    model_name: str = "mistral-large-latest",
    temperature: float = 0.1,
    max_tokens: int = 20,
    top_p: float = 1.0,
) -> int:
    """
    Get actions from the language model
    """
    client = get_sync_client("mistral")

    # Generate the prompts
    system_prompt = build_system_prompt()
    main_prompt = build_main_prompt()

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

    llm_response = completion.choices[0].message.content

    # Validate the completion format
    if llm_response not in MOVES.keys():
        prompt_with_correction = build_main_prompt(wrong_answer=llm_response)

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

        llm_response = completion.choices[0].message.content

        if llm_response not in MOVES.keys():
            raise ValueError(
                f"Invalid completion (even after one error injection): {llm_response}"
            )

    return llm_response
