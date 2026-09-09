#!/usr/bin/env python3
"""Record reproduction commands; never execute a study or write a product."""
import json
import os
import sys
from pathlib import Path

if sys.argv[1:] == ['-B', '-c', 'from runtime_paths import INPUT_ROOT; print(INPUT_ROOT)']:
    sys.path.insert(0, '/home/amir/Codes/PDE/studies/resnet_operator_core')
    from runtime_paths import INPUT_ROOT
    print(INPUT_ROOT)
    raise SystemExit(0)

print(json.dumps({
    "argv": sys.argv[1:],
    "cwd": str(Path.cwd()),
    "operator_output": os.environ.get("PDE_OPERATOR_OUTPUT_ROOT"),
    "operator_input": os.environ.get("PDE_OPERATOR_INPUT_ROOT"),
}))
