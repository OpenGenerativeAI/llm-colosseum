def get_client(model_str):
    provider, model = model_str.split(":")
    if provider == "openai":
        from llama_index.llms.openai import OpenAI

        return OpenAI(model=model)
    elif provider == "anthropic":
        from llama_index.llms.anthropic import Anthropic

        return Anthropic(model=model)
    elif provider == "mixtral" or provider == "groq":
        from llama_index.llms.groq import Groq

        return Groq(model=model)
