"""The retained FP64 authorization is historical, not a fresh run contract."""


def require_current_authorization() -> None:
    raise RuntimeError(
        "archive-only FP64 runtime: the frozen config, source lock, unlock, "
        "preflight and attempt ledger authorize historical paths only. "
        "No new runtime is authorized by relocating source. Refusing before "
        "GPU imports, watchdog records, attempts or results; do not refresh "
        "seals or reset historical attempts. A fresh generated-data runtime "
        "requires a separately reviewed authorization contract."
    )
