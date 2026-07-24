def format_sections(title: str, sections: dict[str, str]) -> str:
    lines = [f"# {title}", ""]
    for heading, body in sections.items():
        lines.append(f"## {heading}")
        lines.append("")
        lines.append(body.strip())
        lines.append("")
    return "\n".join(lines).strip()
