# src/agents/data_agent.py
import pandas as pd
import json
from pathlib import Path

def load_data(path):
    df = pd.read_csv(path)
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    for col in ['spend','impressions','clicks','ctr','purchases','revenue','roas']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def summarize(df):
    s = {}
    s['rows'] = int(len(df))
    s['date_range'] = [str(df['date'].min().date()), str(df['date'].max().date())] if 'date' in df.columns else None
    s['total_spend'] = float(df['spend'].sum(skipna=True)) if 'spend' in df.columns else None
    s['avg_ctr'] = float(df['ctr'].mean(skipna=True)) if 'ctr' in df.columns else None
    s['roas_quantiles'] = df['roas'].quantile([0.25,0.5,0.75]).to_dict() if 'roas' in df.columns else {}
    s['top_campaigns'] = df['campaign_name'].dropna().unique().tolist()[:10]
    return s

def save_summary(summary, out_path):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w') as f:
        json.dump(summary, f, indent=2)
