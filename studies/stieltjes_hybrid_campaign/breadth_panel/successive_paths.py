"""Explicit successive-width evidence inputs and fresh analysis outputs."""
from __future__ import annotations

import argparse
from pathlib import Path

PANEL = Path(__file__).resolve().parent
REPO = PANEL.parents[2]
GENERATED_PANEL = REPO / 'data/generated/stieltjes_hybrid_campaign/breadth_panel'
HISTORICAL_PANEL = REPO / 'data/historical/studies/stieltjes_hybrid_campaign/breadth_panel'


def require_output(path: Path) -> Path:
    path = path.resolve()
    if path.is_relative_to(REPO) and not path.is_relative_to(GENERATED_PANEL.parent):
        raise ValueError(f'fresh outputs must be under {GENERATED_PANEL.parent} or external scratch')
    return path


def path_label(path: Path) -> str:
    path = path.resolve()
    return str(path.relative_to(REPO)) if path.is_relative_to(REPO) else str(path)


def parse_analysis_paths(study: str, argv=None, *, panel_inputs: bool = False):
    parser = argparse.ArgumentParser()
    inputs = parser.add_mutually_exclusive_group()
    inputs.add_argument('--input-dir', type=Path)
    inputs.add_argument('--historical', action='store_true')
    parser.add_argument('--manifest-dir', type=Path)
    parser.add_argument('--output-dir', type=Path)
    args = parser.parse_args(argv)
    suffix = '' if panel_inputs else study
    args.input_dir = (args.input_dir or (HISTORICAL_PANEL if args.historical else GENERATED_PANEL)/suffix).resolve()
    # Historical arrays moved to data; their small provenance manifests stayed
    # in source. Fresh producers keep arrays and manifests together.
    args.manifest_dir = (args.manifest_dir or (PANEL/suffix if args.historical else args.input_dir)).resolve()
    output = GENERATED_PANEL/study
    args.output_dir = require_output(args.output_dir or (output/'historical_review' if args.historical else output))
    return args
