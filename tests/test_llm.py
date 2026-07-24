import unittest
from unittest.mock import patch

from llm import LLMProvider


class LLMTests(unittest.TestCase):
    def test_groq_uses_groq_client_when_available(self):
        provider = LLMProvider(provider="groq", api_key="test-key", model="llama-3.1-8b-instant")

        with patch("llm.Groq") as mock_groq:
            mock_client = mock_groq.return_value
            mock_response = type("Resp", (), {"choices": [type("Choice", (), {"message": type("Message", (), {"content": "ok"})()})()]})()
            mock_client.chat.completions.create.return_value = mock_response

            result = provider.generate("hello")

        self.assertEqual(result, "ok")

    def test_deepseek_uses_openai_compatible_client_when_available(self):
        provider = LLMProvider(provider="deepseek", api_key="test-key", model="deepseek-v4-flash")

        with patch("llm.OpenAI") as mock_openai:
            mock_client = mock_openai.return_value
            mock_response = type("Resp", (), {"choices": [type("Choice", (), {"message": type("Message", (), {"content": "ok"})()})()]})()
            mock_client.chat.completions.create.return_value = mock_response

            result = provider.generate("hello")

        self.assertEqual(result, "ok")


if __name__ == "__main__":
    unittest.main()
