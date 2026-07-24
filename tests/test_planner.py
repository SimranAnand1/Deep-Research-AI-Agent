import unittest
from unittest.mock import patch

from planner import build_plan


class PlannerTests(unittest.TestCase):
    def test_build_plan_parses_json_output(self):
        with patch("planner.LLMProvider.generate", return_value='{"tasks":[{"title":"Research","objective":"Investigate"}]}'):
            tasks = build_plan("Best laptops", "groq")

        self.assertEqual(tasks[0]["title"], "Research")
        self.assertEqual(tasks[0]["objective"], "Investigate")


if __name__ == "__main__":
    unittest.main()
