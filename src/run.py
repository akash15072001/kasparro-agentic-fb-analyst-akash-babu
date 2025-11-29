# src\run.py
import sys, json
from pathlib import Path
import yaml

from src.agents.data_agent import load_data, summarize, save_summary
from src.agents.evaluator import corr_impr_ctr, compare_by_creative_type

def run(task_text, config_path="config/config.yaml"):
    cfg = yaml.safe_load(open(config_path))
    data_path = cfg.get('data_path','data/sample_fb_ads.csv')
    output_dir = cfg.get('output_reports_dir','reports')
    Path(output_dir).mkdir(parents=True, exist_ok=True)

    df = load_data(data_path)
    summary = summarize(df)
    save_summary(summary, f"{output_dir}/data_summary.json")

    corr = corr_impr_ctr(df)
    groups = compare_by_creative_type(df)
    insights = [{"id":"h1","hypothesis":"impressions vs ctr correlation","evidence":corr}]
    with open(f"{output_dir}/insights.json","w") as f:
        json.dump(insights, f, indent=2)

    # dummy creatives (empty for now)
    with open(f"{output_dir}/creatives.json","w") as f:
        json.dump([], f, indent=2)

    with open(f"{output_dir}/report.md","w") as f:
        f.write("# Report\n")
        f.write("Task: "+task_text+"\n\n")
        f.write("Summary:\n")
        f.write(json.dumps(summary, indent=2))

    print("Run complete. Check reports/ directory.")

if __name__ == "__main__":
    task = sys.argv[1] if len(sys.argv)>1 else "Analyze ROAS drop"
    run(task)
