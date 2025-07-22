# AdobeProject2 — Intelligent Document Analyst

A lightweight CPU-only Streamlit application that analyzes PDF documents, extracts relevant sections based on a **persona** and **job-to-be-done**, and ranks them by importance.

---

## 🚀 Features

- Upload multiple PDFs
- Provide persona & job-to-be-done input
- Extract and summarize document sections
- JSON output with rankings
- Works offline and without heavy models (no `transformers` used)

---

## 💂 Folder Structure

```
adobeproject2/
├── app.py                  # Streamlit main app
├── utils.py                # PDF text extractor
├── summarizer.py           # Lightweight summarizer
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container configuration
└── sample_input/
    ├── persona.json
    ├── job_description.txt
    └── documents/
        └── *.pdf
```

---

## 💻 Run Locally (Without Docker)

### Prerequisites:

- Python 3.10+
- pip

### Steps:

```bash
cd adobeproject2
pip install -r requirements.txt
streamlit run app.py
```

Open: [http://localhost:8501](http://localhost:8501)

---

## 🐳 Run Using Docker

### 1. Build the Docker image

```bash
docker build -t adobeproject2 .
```

### 2. Run the Docker container

```bash
docker run --rm -p 8501:8501 adobeproject2
```

Then open [http://localhost:8501](http://localhost:8501)

---

## 📝 Input Format

### `sample_input/persona.json`

```json
{
  "role": "PhD Researcher in Computational Biology",
  "focus_areas": ["Graph Neural Networks", "Drug Discovery", "Performance Benchmarks"]
}
```

### `sample_input/job_description.txt`

```
Prepare a comprehensive literature review focusing on methodologies, datasets, and performance benchmarks
```

---

## 🧠 How It Works

1. PDFs are scanned page by page
2. Each section is extracted using title heuristics
3. Sections are summarized (lightweight logic)
4. Summary & rank are exported to `output.json`

---

## 📦 Output

A JSON file named `output.json` is generated with:

- Metadata
- Extracted sections
- Summarized sections

---

## 👨‍💼 Authors

- Built using **Streamlit**, **PyPDF2**
- No large model dependencies — lightweight and fast for CPU use

---

## 📄 License

MIT License

