from prompts import FINAL_REPORT_PROMPT
from llm import LLMProvider
from config import get_provider_settings


def generate_report(topic: str, task_results: list[str], provider: str) -> str:
    settings = get_provider_settings(provider)
    llm = LLMProvider(provider=provider, api_key=settings.get("api_key", ""), model=settings.get("model", ""))
    prompt = FINAL_REPORT_PROMPT.format(topic=topic, task_results="\n\n".join(task_results))
    return llm.generate(prompt)
