"""Dependency-light runner for every base-case regression.

The repository environment need not provide pytest.  This module imports and
calls every plain ``test_*`` function deterministically and exits nonzero on
the first failure.
"""

from __future__ import annotations

from . import test_finite_width_contraction, test_finite_width_jet, test_normal_form


def main() -> None:
    count = 0
    for module in (
        test_normal_form,
        test_finite_width_jet,
        test_finite_width_contraction,
    ):
        for name in sorted(vars(module)):
            if not name.startswith("test_"):
                continue
            candidate = getattr(module, name)
            if not callable(candidate):
                continue
            print(f"RUN {module.__name__}.{name}")
            candidate()
            count += 1
    print(f"PASS {count} checks")


if __name__ == "__main__":
    main()
