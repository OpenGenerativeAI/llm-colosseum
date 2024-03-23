import os
from typing import Tuple

try:
    from openai import AsyncOpenAI, OpenAI
except ImportError:
    pass


def get_async_client(provider: str) -> AsyncOpenAI:
    """
    Provider can be "openai", "mistral" or "ollama".
    """
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
