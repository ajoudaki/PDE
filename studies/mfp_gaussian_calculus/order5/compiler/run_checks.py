"""Dependency-free runner for the primary order-five compiler gates."""

from . import test_population_jet


def run() -> None:
    checks = tuple(
        getattr(test_population_jet, name)
        for name in sorted(dir(test_population_jet))
        if name.startswith("test_")
    )
    for check in checks:
        check()
        print(f"PASS {check.__name__}")


if __name__ == "__main__":
    run()

