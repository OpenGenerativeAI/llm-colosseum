"""
Take obesrvations and return actions for the Robot to use
"""

from agent.language_models import get_sync_client  # Change to async later

from .prompts import build_system_prompt, build_main_prompt


def get_actions_from_llm(context_prompt: str) -> int:
    """
    Get actions from the language model
    """
    client = get_sync_client("mistral")

    # Generate the prompts
    system_prompt = build_system_prompt()
    main_prompt = build_main_prompt()

    completion = client.chat.completions.create(
        model="mistral-large-latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": main_prompt},
        ],
    )

    # Validate the completion format

    return completion.choices[0].message
