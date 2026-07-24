from llm import LLMProvider
from prompts import EXECUTOR_PROMPT
from config import get_provider_settings


def execute_task(task: dict, provider: str) -> str:
    settings = get_provider_settings(provider)
    llm = LLMProvider(provider=provider, api_key=settings.get("api_key", ""), model=settings.get("model", ""))
    prompt = EXECUTOR_PROMPT.format(task=task.get("title", "Research Task"), objective=task.get("objective", ""))
    return llm.generate(prompt)
