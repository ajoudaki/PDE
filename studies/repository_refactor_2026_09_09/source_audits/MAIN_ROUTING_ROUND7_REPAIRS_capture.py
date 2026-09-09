import hashlib
import json
from pathlib import Path
import sys

REPO = Path('/home/amir/Codes/PDE')
PRIVATE = Path(__file__).parent
OWNED = (
    'studies/mfp_quadratic_compiler/campaign1/run_graded_campaign.py',
    'studies/mfp_quadratic_compiler/centered_depth1_order13/centered_h2_exact.py',
    'studies/resnet_dense_long_horizon/reproduce.sh',
    'studies/repository_refactor_2026_09_09/test_resnet_routing.py',
    'studies/repository_refactor_2026_09_09/test_quadratic_routing.py',
    'studies/repository_refactor_2026_09_09/test_metadata_routing.py',
)
DEPENDENCIES = (
    'studies/_output_paths.py',
    'studies/mfp_quadratic_compiler/campaign_paths.py',
    'studies/resnet_dense_long_horizon/make_manifest.py',
    'studies/mfp_quadratic_compiler/campaign1/graded_sector.cpp',
)
stage = sys.argv[1]
data = {name: {'sha256': hashlib.sha256((REPO / name).read_bytes()).hexdigest(), 'text': (REPO / name).read_text()} for name in (*OWNED, *DEPENDENCIES)}
(PRIVATE / (stage + '.json')).write_text(json.dumps(data, indent=2) + '\n')
if stage == 'before':
    print(json.dumps({name: record['sha256'] for name, record in data.items()}, indent=2))
else:
    before = json.loads((PRIVATE / 'before.json').read_text())
    print(json.dumps({'changed': [name for name in data if data[name] != before[name]], 'dependencies_unchanged': all(data[name] == before[name] for name in DEPENDENCIES)}, indent=2))
