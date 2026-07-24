import json
from llm import LLMProvider
from prompts import PLANNING_PROMPT
from config import get_provider_settings


def build_plan(topic: str, provider: str) -> list[dict]:
    settings = get_provider_settings(provider)
    llm = LLMProvider(provider=provider, api_key=settings.get("api_key", ""), model=settings.get("model", ""))
    prompt = PLANNING_PROMPT.format(topic=topic)
    output = llm.generate(prompt)

    try:
        parsed = json.loads(output)
        tasks = parsed.get("tasks", [])
        if isinstance(tasks, list) and tasks:
            return tasks
    except (json.JSONDecodeError, TypeError, AttributeError):
        pass

    return [{"title": "Research Overview", "objective": output[:250]}]
