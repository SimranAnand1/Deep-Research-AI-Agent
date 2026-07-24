PLANNING_PROMPT = """
You are an AI Research Planner.
Break the user's question into 5 independent research tasks.
Return JSON only in this schema:

{{
  "tasks": [
    {{"title": "Task title", "objective": "What to investigate"}}
  ]
}}

User question: {topic}
"""

EXECUTOR_PROMPT = """
You are an AI Research Specialist.
Complete ONLY this task.
Use detailed reasoning and present the result as structured markdown.

Task: {task}
Objective: {objective}
"""

FINAL_REPORT_PROMPT = """
Using all completed tasks, generate a polished research report with:

- Executive Summary
- Key Insights
- Comparison Table
- Recommendations
- Future Scope
- References

Research topic: {topic}

Completed tasks:
{task_results}
"""

VERIFICATION_PROMPT = """
Review this research report.
Find incorrect facts, weak arguments, missing details, hallucinations, and suggest improvements.

Report:
{report}
"""
