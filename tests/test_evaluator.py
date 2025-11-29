# tests/test_evaluator.py

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.agents.data_agent import load_data, summarize
from src.agents.evaluator import corr_impr_ctr

def test_summary_and_corr():
    df = load_data("data/sample_fb_ads.csv")
    s = summarize(df)
    assert s['rows'] > 0
    corr = corr_impr_ctr(df)
    assert isinstance(corr, dict)
