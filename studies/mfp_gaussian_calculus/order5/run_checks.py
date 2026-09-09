"""Run every maintained finite-width, compiler, and hostile order-five gate."""

ARCHIVE_ONLY_REASON = "archive-only order-five package replay; retained mixed-input gates require a separate replay interface"
if __name__ == "__main__":
    raise RuntimeError(ARCHIVE_ONLY_REASON)

from .audit_hostile import run as run_hostile
from .compiler.run_checks import run as run_compiler
from .finite_width.run_checks import run as run_finite_width


def run() -> None:
    raise RuntimeError(ARCHIVE_ONLY_REASON)
    print("[finite-width]")
    run_finite_width()
    print("[primary compiler]")
    run_compiler()
    print("[hostile audit]")
    run_hostile()


if __name__ == "__main__":
    run()

