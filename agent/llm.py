from llama_index.core.llms.function_calling import FunctionCallingLLM
from llama_index.core.multi_modal_llms.base import MultiModalLLM


def get_client(model_str: str) -> FunctionCallingLLM:
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

        return OpenAI(model=model_name)
    elif provider == "anthropic":
        from llama_index.llms.anthropic import Anthropic

        return Anthropic(model=model_name)
    elif provider == "mistral":
        from llama_index.llms.mistralai import MistralAI

        return MistralAI(model=model_name)
    elif provider == "groq":
        from llama_index.llms.groq import Groq

        return Groq(model=model_name)

    elif provider == "ollama":
        from llama_index.llms.ollama import Ollama

        return Ollama(model=model_name)
    elif provider == "bedrock":
        from llama_index.llms.bedrock import Bedrock

        return Bedrock(model=model_name)
    elif provider == "cerebras":
        from llama_index.llms.cerebras import Cerebras

        return Cerebras(model=model_name)

    raise ValueError(f"Provider {provider} not found")


def get_client_multimodal(model_str: str) -> MultiModalLLM:
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

    if provider == "ollama":
        from llama_index.multi_modal_llms.ollama import OllamaMultiModal

        return OllamaMultiModal(model=model_name)

    raise ValueError(f"Provider {provider} not found")
