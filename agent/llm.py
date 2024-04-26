def get_client(model_str):
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
    elif provider == "mixtral" or provider == "groq":
        from llama_index.llms.groq import Groq

        return Groq(model=model_name)

    elif provider == "ollama":
        from llama_index.llms.ollama import Ollama

        return Ollama(model=model_name)
