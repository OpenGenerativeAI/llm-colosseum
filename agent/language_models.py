import os
import dotenv
from typing import Tuple

dotenv.load_dotenv()

try:
    from openai import AsyncOpenAI, OpenAI
except ImportError:
    pass

# Check we can access the environment variables
assert os.getenv("MISTRAL_API_KEY") is not None


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
    if provider == "solar":
        return AsyncOpenAI(
            base_url="https://api.upstage.ai/v1/solar", api_key=os.getenv("SOLAR_API_KEY")
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
    if provider == "solar":
        print("solar key", os.getenv("SOLAR_API_KEY"))
        return OpenAI(
            base_url="https://api.upstage.ai/v1/solar", api_key=os.getenv("SOLAR_API_KEY")
    )
    if provider == "ollama":
        return OpenAI(base_url="http://localhost:11434/v1/")
    if provider == "groq":
        return OpenAI(
            base_url="https://api.groq.com/openai/v1/",
            api_key=os.getenv("GROK_API_KEY"),
        )
    raise NotImplementedError(f"Provider {provider} is not supported.")


def get_provider_and_model(model: str) -> Tuple[str, str]:
    """
    Get the provider and model from a string in the format "provider:model"
    If no provider is specified, it defaults to "openai"

    Args:
        model (str): The model string in the format "provider:model"

    Returns:
        tuple: A tuple with the provider and model
    """

    split_result = model.split(":")
    if len(split_result) == 1:
        return "openai", split_result[0]
    return split_result[0], split_result[1]
