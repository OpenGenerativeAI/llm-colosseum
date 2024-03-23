import os
from typing import Tuple

import phospho.config as config

try:
    from openai import AsyncOpenAI, OpenAI
except ImportError:
    pass


def get_provider_and_model(model: str) -> Tuple[str, str]:
    """
    Get the provider and model from a string in the format "provider:model"
    If no provider is specified, it defaults to "openai"

    Args:
        model (str): The model string in the format "provider:model"

    Returns:
        tuple: A tuple with the provider and model
    """
    # If the OVERRIDE_WITH_OLLAMA_MODEL environment variable is set, use the Ollama model
    # in all cases. This is used in the preview mode or for tests.
    if config.OVERRIDE_WITH_OLLAMA_MODEL is not None:
        ollama_model = config.OVERRIDE_WITH_OLLAMA_MODEL
        return "ollama", ollama_model

    split_result = model.split(":")
    if len(split_result) == 1:
        return "openai", split_result[0]
    return split_result[0], split_result[1]


def get_async_client(provider: str) -> AsyncOpenAI:
    if provider == "openai":
        return AsyncOpenAI()
    if provider == "mistral":
        return AsyncOpenAI(
            base_url="https://api.mistral.ai/v1/", api_key=os.getenv("MISTRAL_API_KEY")
        )
    if provider == "ollama":
        return AsyncOpenAI(base_url="http://localhost:11434/v1/")
    raise NotImplementedError(f"Provider {provider} is not supported.")


def get_sync_client(provider: str) -> OpenAI:
    if provider == "openai":
        return OpenAI()
    if provider == "mistral":
        return OpenAI(
            base_url="https://api.mistral.ai/v1/", api_key=os.getenv("MISTRAL_API_KEY")
        )
    if provider == "ollama":
        return OpenAI(base_url="http://localhost:11434/v1/")
    raise NotImplementedError(f"Provider {provider} is not supported.")
