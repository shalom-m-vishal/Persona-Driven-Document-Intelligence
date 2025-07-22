def summarize_section(text, persona, job_to_be_done):
    """
    Heuristic summary: return first 3 sentences from section text.
    """
    sentences = text.split('. ')
    summary = '. '.join(sentences[:3]).strip()
    if not summary.endswith('.'):
        summary += '.'
    return summary