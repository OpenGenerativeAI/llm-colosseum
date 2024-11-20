from llama_index.core.llms.function_calling import FunctionCallingLLM
from llama_index.core.multi_modal_llms.base import MultiModalLLM
import os


def get_client(model_str: str, temperature: float = 0.7) -> FunctionCallingLLM:
    split_result = model_str.split(":")
    if len(split_result) == 1:
        # Assume default provider to be openai
        provider = "openai"
        model_name = split_result[0]
    elif len(split_result) > 2:
        # Some model names have :, so we need to join the rest of the string
        provider = split_result[0]
        model_name = ":".join(split_result[1:])
    else:
        provider = split_result[0]
        model_name = split_result[1]

    if provider == "openai":
        from llama_index.llms.openai import OpenAI

        return OpenAI(model=model_name, temperature=temperature)
    elif provider == "anthropic":
        from llama_index.llms.anthropic import Anthropic

        return Anthropic(model=model_name, temperature=temperature)
    elif provider == "mistral":
        from llama_index.llms.mistralai import MistralAI

        return MistralAI(model=model_name)
    elif provider == "groq":
        from llama_index.llms.groq import Groq

        return Groq(model=model_name, temperature=temperature)

    elif provider == "ollama":
        from llama_index.llms.ollama import Ollama

        return Ollama(model=model_name, temperature=temperature)
    elif provider == "bedrock":
        from llama_index.llms.bedrock import Bedrock

        return Bedrock(model=model_name)
    elif provider == "cerebras":
        from llama_index.llms.cerebras import Cerebras

        return Cerebras(model=model_name, temperature=temperature)
    elif provider == "gemini":
        from llama_index.llms.gemini import Gemini

        return Gemini(model=model_name, temperature=temperature)

    elif provider == "anyscale":
        from llama_index.llms.openai import OpenAI

        return OpenAI(
            model=model_name,
            temperature=temperature,
            api_key=os.environ.get("ANYSCALE_API_KEY"),
            api_base="https://api.endpoints.anyscale.com/v1/",
        )

    elif provider == "fireworks":
        from llama_index.llms.openai import OpenAI

        return OpenAI(
            model=model_name,
            temperature=temperature,
            api_key=os.environ.get("FIREWORKS_API_KEY"),
            api_base="https://api.fireworks.ai/inference/v1/",
        )

    elif provider == "together":
        from llama_index.llms.openai import OpenAI

        return OpenAI(
            model=model_name,
            temperature=temperature,
            api_key=os.environ.get("TOGETHER_API_KEY"),
            api_base="https://api.together.xyz/v1/",
        )

    raise ValueError(f"Provider {provider} not found in models")


def get_client_multimodal(model_str: str, temperature: float = 0.7) -> MultiModalLLM:
    split_result = model_str.split(":")
    if len(split_result) == 1:
        # Assume default provider to be openai
        provider = "ollama"
        model_name = split_result[0]
    elif len(split_result) > 2:
        # Some model names have :, so we need to join the rest of the string
        provider = split_result[0]
        model_name = ":".join(split_result[1:])
    else:
        provider = split_result[0]
        model_name = split_result[1]

    if provider == "openai":
        from llama_index.multi_modal_llms.openai import OpenAIMultiModal

        return OpenAIMultiModal(model=model_name, temperature=temperature)

    if provider == "ollama":
        from llama_index.multi_modal_llms.ollama import OllamaMultiModal

        return OllamaMultiModal(model=model_name, temperature=temperature)

    elif provider == "mistral":
        from llama_index.multi_modal_llms.mistralai import MistralAIMultiModal

        return MistralAIMultiModal(model=model_name, temperature=temperature)

    elif provider == "gemini":
        from llama_index.multi_modal_llms.gemini import GeminiMultiModal

        return GeminiMultiModal(model=model_name, temperature=temperature)

    elif provider == "anthropic":
        from llama_index.multi_modal_llms.anthropic import AnthropicMultiModal

        return AnthropicMultiModal(model=model_name, temperature=temperature)

    elif provider == "anyscale":
        from llama_index.multi_modal_llms.openai import OpenAIMultiModal

        return OpenAIMultiModal(
            model=model_name,
            temperature=temperature,
            api_key=os.environ.get("ANYSCALE_API_KEY"),
            api_base="https://api.endpoints.anyscale.com/v1/",
        )

    elif provider == "fireworks":
        from llama_index.multi_modal_llms.openai import OpenAIMultiModal

        return OpenAIMultiModal(
            model=model_name,
            temperature=temperature,
            api_key=os.environ.get("FIREWORKS_API_KEY"),
            api_base="https://api.fireworks.ai/inference/v1/",
        )

    elif provider == "together":
        from llama_index.multi_modal_llms.openai import OpenAIMultiModal

        return OpenAIMultiModal(
            model=model_name,
            temperature=temperature,
            api_key=os.environ.get("TOGETHER_API_KEY"),
            api_base="https://api.together.xyz/v1/",
        )

    raise ValueError(f"Provider {provider} not found in multimodal models")
