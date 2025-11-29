# kasparro-agentic-fb-analyst-akash-babu
# Kasparro — Agentic FB Performance Analyst
Repo: kasparro-agentic-fb-analyst-akash-babu

## Quick start (Windows PowerShell)
1. Create & activate venv
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

2. Install requirements
   pip install -r requirements.txt

3. Run (sample)
   python src\run.py "Analyze ROAS drop between 2025-01-20 and 2025-02-01"

## Data
- Put the full CSV at path set in config/config.yaml or use the provided sample at data/sample_fb_ads.csv

## Outputs
- reports/report.md
- reports/insights.json
- reports/creatives.json
- logs/run.log

## Reproducibility
- Random seed: set in config/config.yaml
Repo: https://github.com/akash15072001/kasparro-agentic-fb-analyst-akash-babu
Commit: 8c5b806
Tag: v1.0
Run command: python -m src.run "Analyze ROAS drop between 2025-01-20 and 2025-02-01"
