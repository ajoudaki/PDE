"""Study-local routing for fresh products, independent of the launch directory.

Historical inputs are opt-in. Output overrides may use scratch directories,
but cannot target repository source, historical data, or another study's data.
This module does not create directories at import or argument-parsing time.
"""

from __future__ import annotations

import argparse
from itertools import chain
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def reject_output_links(path: str | Path) -> None:
    """Reject existing output aliases without creating anything.

    Check components and children without following directory symlinks. The
    hardlink check is deliberately a simple existing-file check, not protection
    against a malicious process racing validation and publication.
    """
    selected = Path(path).expanduser().absolute()
    for component in (selected, *selected.parents):
        if component.is_symlink():
            raise ValueError(f"output path contains a symlink: {component}")
    children = selected.rglob("*") if selected.is_dir() else ()
    for child in chain((selected,), children):
        if child.is_symlink():
            raise ValueError(f"output directory contains a symlink: {child}")
        if child.is_file() and child.stat().st_nlink > 1:
            raise ValueError(f"output contains an existing hardlink: {child}")


class StudyPaths:
    def __init__(self, source: str | Path):
        relative = Path(source).resolve().relative_to(REPO_ROOT / "studies")
        self.study = relative.parts[0]
        self.relative = relative.parent.relative_to(self.study)
        self.generated = REPO_ROOT / "data/generated" / self.study
        self.historical = REPO_ROOT / "data/historical/studies" / self.study

    def input_dir(self, *, historical: bool = False, relative: str | Path | None = None) -> Path:
        suffix = self.relative if relative is None else Path(relative)
        return (self.historical if historical else self.generated) / suffix

    def require_output(self, path: str | Path) -> Path:
        output = Path(path).expanduser().resolve()
        if output.is_relative_to(REPO_ROOT) and not output.is_relative_to(self.generated):
            raise ValueError(f"fresh output must be under {self.generated} or external scratch, not {output}")
        reject_output_links(path)
        return output

    def add_arguments(
        self, parser: argparse.ArgumentParser, *, inputs: bool = False,
        output_relative: str | Path | None = None,
    ) -> None:
        suffix = self.relative if output_relative is None else Path(output_relative)
        parser.add_argument("--output-dir", type=Path, default=self.generated / suffix,
                            help="fresh output directory (never source or historical data)")
        if inputs:
            group = parser.add_mutually_exclusive_group()
            group.add_argument("--input-dir", type=Path, help="explicit read-only input directory")
            group.add_argument("--historical-inputs", action="store_true",
                               help="read retained historical inputs; still write fresh outputs")

    def resolve_arguments(
        self, args: argparse.Namespace, *, inputs: bool = False,
        input_relative: str | Path | None = None,
    ) -> argparse.Namespace:
        args.output_dir = self.require_output(args.output_dir)
        if inputs:
            args.input_dir = (args.input_dir or self.input_dir(
                historical=args.historical_inputs, relative=input_relative)).resolve()
            if args.output_dir == args.input_dir and args.historical_inputs:
                raise ValueError("historical inputs cannot be an output destination")
        return args

    def parse(
        self, argv: list[str] | None = None, *, inputs: bool = False,
        output_relative: str | Path | None = None,
        input_relative: str | Path | None = None,
    ) -> argparse.Namespace:
        parser = argparse.ArgumentParser(description=__doc__)
        self.add_arguments(parser, inputs=inputs, output_relative=output_relative)
        return self.resolve_arguments(parser.parse_args(argv), inputs=inputs,
                                      input_relative=input_relative)
