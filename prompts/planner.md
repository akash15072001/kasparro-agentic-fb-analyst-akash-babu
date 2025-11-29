Task: {{task}}
Context summary: {{data_summary}}

Return JSON:
{
  "subtasks": [
    {"id":"t1","description":"load and summarise data","inputs":["data_path"], "expected_output":"data_summary.json"},
    {"id":"t2","description":"generate hypotheses","inputs":["data_summary","metric_trends"], "expected_output":"insights.json"},
    {"id":"t3","description":"validate hypotheses","inputs":["insights.json","raw_data"], "expected_output":"insights_validated.json"},
    {"id":"t4","description":"generate creatives for low-CTR campaigns","inputs":["low_ctr_list"], "expected_output":"creatives.json"},
    {"id":"t5","description":"compile report","inputs":["insights_validated.json","creatives.json"], "expected_output":"report.md"}
  ],
  "priority": "high"
}
