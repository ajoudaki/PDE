"""Finite-width run locations, separate from source and retained inputs."""

import argparse
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
GENERATED_ROOT = REPO_ROOT / "data/generated/stieltjes_finite_width"
HISTORICAL_ROOT = REPO_ROOT / "data/historical/studies/stieltjes_finite_width"


def parse_paths(output: Path, argv=None, *, input_dir: Path | None = None,
                historical_input: Path | None = None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path)
    if input_dir is not None:
        group = parser.add_mutually_exclusive_group()
        group.add_argument("--input-dir", type=Path, default=input_dir)
        group.add_argument("--historical", action="store_true",
                           help="Explicitly read retained inputs; write only a fresh review")
    args = parser.parse_args(argv)
    historical = getattr(args, "historical", False)
    if historical:
        if historical_input is None:
            parser.error("this entry point has no historical input binding")
        args.input_dir = historical_input
    args.output_dir = (args.output_dir or
                       (GENERATED_ROOT / "historical_review" / output.name if historical else output)).resolve()
    if args.output_dir.is_relative_to(REPO_ROOT) and not args.output_dir.is_relative_to(GENERATED_ROOT):
        parser.error(f"fresh outputs must be under {GENERATED_ROOT} or external scratch")
    return args
