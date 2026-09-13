"""Compare the complete recomputed analysis with the frozen output."""
import json
from pathlib import Path

ROOT=Path('/home/amir/Codes/PDE/data/generated/observable_hierarchy')
a=json.loads((ROOT/'H4_author_analysis_v1/summary.json').read_text())
b=json.loads((ROOT/'H4_scientific_A_v1/recomputed_analysis/summary.json').read_text())
times=[a.pop('analysis_cpu_seconds'),b.pop('analysis_cpu_seconds')]
assert a==b, 'Complete scientific analysis JSON differs'
assert (ROOT/'H4_author_analysis_v1/summary.md').read_bytes()==(ROOT/'H4_scientific_A_v1/recomputed_analysis/summary.md').read_bytes()
result=dict(status='pass',complete_json_exact_except_measured_analysis_cpu=True,
            complete_markdown_byte_identical=True,analysis_cpu_seconds=times,
            runs=len(a['runs']),comparisons=len(a['comparisons']))
(ROOT/'H4_scientific_A_v1/analysis_comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
