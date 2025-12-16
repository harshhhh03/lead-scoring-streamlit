# Lead Generation & Probability Scoring Agent

This project is a demo web agent that identifies, enriches, and ranks potential biotech leads
based on business and scientific intent.

## Features
- Reproducible data pipeline
- Weighted probability scoring (0–100)
- Streamlit dashboard
- CSV export

## Scoring Logic
Signals used:
- Role fit (toxicology, safety, preclinical)
- Company funding stage
- Use of 3D in-vitro models
- Location in biotech hubs
- Recent scientific publications

## Live Demo
https://lead-scoring-agent.streamlit.app

## How to Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
