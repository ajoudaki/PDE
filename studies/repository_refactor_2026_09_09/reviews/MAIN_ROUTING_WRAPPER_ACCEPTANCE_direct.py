import json
from pathlib import Path
import sys
sys.path.insert(0, '/tmp/resnet-patch-acceptance.7tppNkr4')
from runtime import install_audit, load_real_guards
install_audit()
load_real_guards()
from make_manifest import validate_output_root
from studies._output_paths import reject_output_links

if sys.argv[1] == 'validate':
    print(json.dumps({'normalized': str(validate_output_root(Path(sys.argv[2])))}))
elif sys.argv[1] == 'links':
    reject_output_links(Path(sys.argv[2]))
    print(json.dumps({'accepted': True}))
else:
    raise SystemExit(99)

