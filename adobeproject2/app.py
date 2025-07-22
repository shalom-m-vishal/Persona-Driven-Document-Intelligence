import os
import json
import time
import glob
import streamlit as st
from datetime import datetime
from utils import extract_sections_from_pdf
from summarizer import summarize_section

st.set_page_config(page_title="Intelligent Document Analyst", layout="wide")
st.title("📄 Intelligent Document Analyst")

# Input: Upload PDFs
uploaded_files = st.file_uploader("Upload PDF documents", type=["pdf"], accept_multiple_files=True)
persona_input = st.text_area("Persona (e.g. PhD Researcher in Computational Biology)", "PhD Researcher in Computational Biology")
job_input = st.text_area("Job to be Done", "Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks")

if st.button("Analyze Documents") and uploaded_files:
    start_time = time.time()

    os.makedirs("temp_docs", exist_ok=True)
    temp_file_paths = []

    for file in uploaded_files:
        path = os.path.join("temp_docs", file.name)
        with open(path, "wb") as f:
            f.write(file.read())
        temp_file_paths.append(path)

    output_sections = []
    output_subsections = []
    rank = 1

    persona = {"role": persona_input, "focus_areas": []}

    for pdf_file in temp_file_paths:
        sections = extract_sections_from_pdf(pdf_file)
        for sec in sections:
            summary = summarize_section(sec["text"], persona, job_input)
            output_sections.append({
                "document": os.path.basename(pdf_file),
                "page_number": sec["page"],
                "section_title": sec["title"],
                "importance_rank": rank
            })
            output_subsections.append({
                "document": os.path.basename(pdf_file),
                "page_number": sec["page"],
                "refined_text": summary
            })
            rank += 1

    output = {
        "metadata": {
            "input_documents": [os.path.basename(f) for f in temp_file_paths],
            "persona": persona,
            "job_to_be_done": job_input,
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": output_sections,
        "subsection_analysis": output_subsections
    }

    st.success("✅ Analysis Complete!")
    st.download_button("📥 Download JSON Output", json.dumps(output, indent=4), file_name="output.json", mime="application/json")

    end_time = time.time()
    st.write(f"⏱️ Processed in {round(end_time - start_time, 2)} seconds")