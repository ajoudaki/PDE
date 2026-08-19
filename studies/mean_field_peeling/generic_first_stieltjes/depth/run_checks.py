"""Dependency-light runner for the exact fixed-depth program."""

from __future__ import annotations

from . import (
    test_exact_depth_program,
    test_gnf_audit_reference,
    test_gnf_recursion,
)


def main() -> None:
    count = 0
    for module in (
        test_exact_depth_program,
        test_gnf_recursion,
        test_gnf_audit_reference,
    ):
        for name in sorted(vars(module)):
            candidate = getattr(module, name)
            if name.startswith("test_") and callable(candidate):
                print(f"RUN {module.__name__}.{name}")
                candidate()
                count += 1
    print(f"PASS {count} exact fixed-depth checks")


if __name__ == "__main__":
    main()
