from abc import ABC, abstractmethod
import requests


class BaseLLMProvider(ABC):
    def __init__(self, api_key: str, model: str):
        self.api_key = api_key
        self.model = model

    @abstractmethod
    def generate(self, prompt: str) -> str:
        raise NotImplementedError


class GroqProvider(BaseLLMProvider):
    def generate(self, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"model": self.model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
        response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]


class OpenRouterProvider(BaseLLMProvider):
    def generate(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://example.com",
            "X-Title": "Deep Research AI",
        }
        payload = {"model": self.model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]


class DeepSeekProvider(BaseLLMProvider):
    def generate(self, prompt: str) -> str:
        headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        payload = {"model": self.model, "messages": [{"role": "user", "content": prompt}], "temperature": 0.2}
        response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]


class GeminiProvider(BaseLLMProvider):
    def generate(self, prompt: str) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
