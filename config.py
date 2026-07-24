import os
from enum import Enum
from dotenv import load_dotenv

load_dotenv()


class Provider(str, Enum):
    GROQ = "groq"
    OPENROUTER = "openrouter"
    DEEPSEEK = "deepseek"
    GEMINI = "gemini"


PROVIDER_LABELS = {
    Provider.GROQ: "Groq",
    Provider.OPENROUTER: "OpenRouter",
    Provider.DEEPSEEK: "DeepSeek",
    Provider.GEMINI: "Gemini",
}


DEFAULT_MODELS = {
    Provider.GROQ: os.getenv("GROQ_MODEL", "llama-3.1-8b-instant"),
    Provider.OPENROUTER: os.getenv("OPENROUTER_MODEL", "openai/gpt-4o-mini"),
    Provider.DEEPSEEK: os.getenv("DEEPSEEK_MODEL", "deepseek-chat"),
    Provider.GEMINI: os.getenv("GEMINI_MODEL", "gemini-1.5-flash"),
}


def get_provider_settings(provider: str) -> dict:
    provider_name = provider.lower()
    if provider_name == Provider.GROQ:
        return {
            "api_key": os.getenv("GROQ_API_KEY", ""),
            "model": os.getenv("GROQ_MODEL", DEFAULT_MODELS[Provider.GROQ]),
        }
    if provider_name == Provider.OPENROUTER:
        return {
            "api_key": os.getenv("OPENROUTER_API_KEY", ""),
            "model": os.getenv("OPENROUTER_MODEL", DEFAULT_MODELS[Provider.OPENROUTER]),
        }
    if provider_name == Provider.DEEPSEEK:
        return {
            "api_key": os.getenv("DEEPSEEK_API_KEY", ""),
            "model": os.getenv("DEEPSEEK_MODEL", DEFAULT_MODELS[Provider.DEEPSEEK]),
        }
    if provider_name == Provider.GEMINI:
        return {
            "api_key": os.getenv("GEMINI_API_KEY", ""),
            "model": os.getenv("GEMINI_MODEL", DEFAULT_MODELS[Provider.GEMINI]),
        }
    return {"api_key": "", "model": ""}
