"""Explicit read-only selection of the generated or retained coefficient map."""

import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from studies._output_paths import StudyPaths

PATHS = StudyPaths(__file__)
NAME = "FULL_L2_PAIRED_ORDER5_MAP.json"


def parse_map_path(argv=None) -> Path:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--map-path", type=Path, help="explicit read-only coefficient map")
    group.add_argument("--historical-inputs", action="store_true")
    args = parser.parse_args(argv)
    return args.map_path or PATHS.input_dir(historical=args.historical_inputs) / NAME


def load_map(path: Path | None = None) -> dict:
    return json.loads((path or PATHS.generated / NAME).read_text())
