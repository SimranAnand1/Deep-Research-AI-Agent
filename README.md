# Deep Research AI

A clean, pure-Python Streamlit app that demonstrates a planner → executor → synthesizer workflow for AI research tasks.

## Features

- Multi-provider support for Groq, OpenRouter, DeepSeek, and Gemini
- Planner that breaks a research topic into independent tasks
- Executor that researches each task in isolation
- Final report generation with executive summaries and recommendations
- PDF export for the completed report
- Simple, teachable architecture for a 2-hour live coding session

## Project structure

```text
deep-research-ai/
├── app.py
├── llm.py
├── planner.py
├── executor.py
├── prompts.py
├── report_generator.py
├── exporter.py
├── config.py
├── requirements.txt
├── providers/
│   ├── __init__.py
│   └── provider.py
└── utils/
    ├── __init__.py
    ├── markdown.py
    └── pdf.py
```

## Setup

1. Create a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Copy `.env.example` to `.env` and add your API keys.
4. Run the app:

```bash
streamlit run app.py
```
