import requests
from groq import Groq
from openai import OpenAI
from config import get_provider_settings, Provider


class LLMProvider:
    def __init__(self, provider: str, api_key: str | None = None, model: str | None = None):
        self.provider = provider.lower()
        self.settings = get_provider_settings(self.provider)
        self.api_key = api_key or self.settings.get("api_key", "")
        self.model = model or self.settings.get("model", "")

    def generate(self, prompt: str) -> str:
        try:
            if self.provider == Provider.GROQ:
                return self._call_groq(prompt)
            if self.provider == Provider.OPENROUTER:
                return self._call_openrouter(prompt)
            if self.provider == Provider.DEEPSEEK:
                return self._call_deepseek(prompt)
            if self.provider == Provider.GEMINI:
                return self._call_gemini(prompt)
        except requests.HTTPError as exc:
            status_code = exc.response.status_code if exc.response is not None else "unknown"
            return (
                f"Provider error for {self.provider}: HTTP {status_code}. "
                f"Check your backend API key, account balance, or model access."
            )
        except requests.RequestException as exc:
            return f"Provider request failed for {self.provider}: {exc}"

        raise ValueError(f"Unsupported provider: {self.provider}")

    def _call_groq(self, prompt: str) -> str:
        client = Groq(api_key=self.api_key)
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content

    def _call_openrouter(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://example.com",
            "X-Title": "Deep Research AI",
        }
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.2,
        }
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"]

    def _call_deepseek(self, prompt: str) -> str:
        client = OpenAI(api_key=self.api_key, base_url="https://api.deepseek.com")
        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
        )
        return response.choices[0].message.content

    def _call_gemini(self, prompt: str) -> str:
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={self.api_key}"
        payload = {"contents": [{"parts": [{"text": prompt}]}]}
        response = requests.post(url, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
