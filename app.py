import os
import streamlit as st
from planner import build_plan
from executor import execute_task
from report_generator import generate_report
from exporter import export_to_pdf
from config import Provider, PROVIDER_LABELS, get_provider_settings

st.set_page_config(page_title="Deep Research AI", page_icon="🧠", layout="wide")

st.title("Deep Research AI")
st.caption("Planner → Executor → Report generator built in pure Python")

with st.sidebar:
    st.header("Provider")
    provider = st.radio("", list(Provider), format_func=lambda p: PROVIDER_LABELS.get(p, p.value), horizontal=False)
    depth = st.selectbox("Research Depth", ["Basic", "Standard", "Advanced"])

st.subheader("Research Topic")
topic = st.text_input("Research topic", placeholder="Ask anything you want to research...")

if st.button("Generate Research", type="primary"):
    if not topic.strip():
        st.error("Please enter a research topic")
        st.stop()

    settings = get_provider_settings(provider.value)
    if not settings.get("api_key"):
        st.error("No API key is configured for this provider. Add it to the backend .env file first.")
        st.stop()

    with st.spinner("Planning research tasks..."):
        tasks = build_plan(topic, provider.value)

    if not tasks:
        st.error("No tasks were generated. The provider may be unavailable or the API key may not have access.")
        st.stop()

    if isinstance(tasks, list) and tasks and isinstance(tasks[0], dict) and "Provider error" in str(tasks[0].get("objective", "")):
        st.warning("The provider returned an error. Please check your backend credentials or billing status.")
        st.stop()

    st.subheader("Research Plan")
    for index, task in enumerate(tasks, start=1):
        st.checkbox(task.get("title", f"Task {index}"), value=True, disabled=True)

    results = []
    progress_bar = st.progress(0)
    status_text = st.empty()

    for index, task in enumerate(tasks, start=1):
        status_text.text(f"Executing task {index}/{len(tasks)}: {task.get('title', '')}")
        result = execute_task(task, provider.value)
        results.append(result)
        progress_bar.progress(index / len(tasks))

    st.success("Research completed")

    with st.spinner("Generating final report..."):
        report = generate_report(topic, results, provider.value)

    st.subheader("Final Report")
    st.markdown(report)

    output_path = os.path.join(os.getcwd(), "research_report.pdf")
    export_to_pdf(report, output_path)
    with open(output_path, "rb") as file_obj:
        st.download_button("Download PDF", data=file_obj.read(), file_name="research_report.pdf", mime="application/pdf")
