#!/usr/bin/env python3
"""Routing spy: records invocation only; never dispatches it."""
import json
import os
import sys
print(json.dumps({"args": sys.argv[1:], "cwd": os.getcwd(),
                  "input": os.environ.get("PDE_OPERATOR_INPUT_ROOT"),
                  "output": os.environ.get("PDE_OPERATOR_OUTPUT_ROOT")}))
