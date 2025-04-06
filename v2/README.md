# SECTRAIN TinyLlama RAG Assistant

Repo: https://github.com/Krunal-125/Tinyllama

This project is a lightweight, locally operable Retrieval-Augmented Generation (RAG) assistant powered by TinyLlama, optimized for secure programming education on low-resource devices.

Branch Descriptions
	•	main – This is the current and production-ready version of the SECTRAIN TinyLlama RAG assistant. It uses a small, locally runnable model (TinyLlama-1.1B-Chat-v1.0) and is trained on OWASP_Code_Review_Guide_v2.pdf. This version is optimized for low-resource environments like laptops with 8 GB RAM.
	•	old-version – This branch contains early experimental implementations using large models like Falcon-7B-Instruct and Mistral-7B-Instruct via the HuggingFace Inference API. These tests worked only on small inputs and were limited by API constraints and local memory usage. This branch is preserved for reference.


---

## What's in this Repo?

- A working RAG pipeline with TinyLlama
- Trained on: OWASP_Code_Review_Guide_v2.pdf (converted to text)
- Clean structure with scripts to:
  - Convert PDFs
  - Build FAISS index
  - Ask questions locally (no APIs)
  - Automatically download TinyLlama model

---

## Model Used

Model: TinyLlama/TinyLlama-1.1B-Chat-v1.0  
Link: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0

To download the model automatically into your project, run:

```bash
python scripts/tinyllama_download.py
```

This will download the Model and place it inside the Tinyllama/ folder.


**Current Training Data**

Used Now:
• OWASP_Code_Review_Guide_v2.pdf

Planned Expansion:
• Lecture slides (Markdown/text)
• OWASP documentation (scraped)
• CVE/NVD vulnerability snippets
• Curated code examples (good/bad practice)
• Web scraping of security literature


**Why Not Falcon 7B / Mistral 7B?**

See the old-version branch for early tests using:
• tiiuae/falcon-7b-instruct
• mistralai/Mistral-7B-Instruct

These models were tested with the HuggingFace Inference API and worked only with small toy examples.
They could not handle full OWASP documents due to:
• API token limits
• Token overflow (>2048 tokens)
• Local RAM constraints (too large for 8 GB MacBook)

Final Decision: Use TinyLlama (1.1B) locally via transformers for:
• CPU-only inference
• Full OWASP document support
• Portable setup


**How to Use This Project**

**1. Setup Environment**

```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**2. Download TinyLlama Model**

```
python scripts/tinyllama_download.py
```

**3. Build the Vector Index**

```
python scripts/pdf_to_text.py
python scripts/build.py
```

**4. Ask Your Questions**

```
python scripts/query.py
```




**Sample Output**

```
Question: What is insecure design?

Answer:
Insecure design refers to flaws in system architecture where secure coding principles were not applied...

Word Count: 45
```




**Future Enhancements**
• F1 Score, BERTScore evaluation
• Gradio or Streamlit frontend
• Multi-session chat context memory
• More security sources (CWE, CVE, etc.)


**Repo Branches**
**Branch**
**Description**
main
Clean TinyLlama-based RAG pipeline
old-version
Experiments with Falcon7B, Mistral7B and HF



**Credits**
• TinyLlama by https://huggingface.co/TinyLlama
• OWASP Secure Code Review Guide v2
• LangChain, HuggingFace Transformers, FAISS


