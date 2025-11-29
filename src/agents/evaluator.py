# src/agents/evaluator.py
import pandas as pd
import numpy as np

def corr_impr_ctr(df):
    # simple rule-based fallback if scipy not available
    try:
        from scipy import stats
        df2 = df[['impressions','ctr']].dropna()
        if len(df2) < 3:
            return {"pearson_r": None, "p_value": None}
        r, p = stats.pearsonr(df2['impressions'], df2['ctr'])
        return {"pearson_r": float(r), "p_value": float(p)}
    except Exception:
        df2 = df[['impressions','ctr']].dropna()
        if len(df2) < 2:
            return {"pearson_r": None, "p_value": None}
        r = df2['impressions'].corr(df2['ctr'])
        return {"pearson_r": float(r), "p_value": None}

def compare_by_creative_type(df):
    res = {}
    if 'creative_type' in df.columns and 'ctr' in df.columns:
        groups = df.groupby('creative_type')['ctr'].agg(['mean','count']).reset_index()
        res['groups'] = groups.to_dict(orient='records')
    return res
