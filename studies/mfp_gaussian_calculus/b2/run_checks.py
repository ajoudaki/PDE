"""Dependency-light runner for the exact B=2 finite-width gate."""

from __future__ import annotations

from . import test_contracted_gnf, test_finite_width_directional


def main() -> None:
    count = 0
    for module in (test_finite_width_directional, test_contracted_gnf):
        for name in sorted(vars(module)):
            candidate = getattr(module, name)
            if name.startswith("test_") and callable(candidate):
                print(f"RUN {module.__name__}.{name}")
                candidate()
                count += 1
    print(f"PASS {count} fixed-batch checks")


if __name__ == "__main__":
    main()
