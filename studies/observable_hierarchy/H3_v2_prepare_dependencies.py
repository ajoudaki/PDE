"""Freeze only the maintained proof scopes used by the proposed addition."""
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STUDY = Path(__file__).resolve().parent


def extract(text, start, end):
    a = text.index(start)
    b = text.index(end, a+len(start))
    return text[a:b].rstrip()+"\n"


def main():
    global_text = (ROOT/"docs/global_nonlinear.md").read_text()
    old = (STUDY/"dependencies_v1.md").read_text()
    # The seven old proof excerpt bodies were verified byte-for-byte by the
    # recovery auditor. Strip their historical packet introduction only.
    body = old[old.index("Source: `docs/special_data_limits.md`"):]
    extra = extract(global_text, "##### 4. Finite reference flows and the comparison estimate", "##### 4. Random observations, the two risks, and their limits")
    closure = extract(global_text, "##### C.4.7.8.", "#### C.4.8.")
    output = STUDY/"H3_v2_dependencies.md"
    if output.exists():
        raise SystemExit("dependency packet already exists; preserve it and choose a new version")
    header = """# Maintained dependencies of the finite observable closure

Read every proof body in this packet. The selected sources establish the
finite Gaussian program and common-action construction, raw state and scalar
calculus, source comparison/tails, finite GF identification and observable
closure. The separately supplied notation and full guides fix conventions.
No unpromoted result from another study is an input. Source boundaries below
are part of the input contract; no prior review or historical verdict is used.

"""
    output.write_text(header+body+"\n---\n\nSource: `docs/global_nonlinear.md`; complete C.4.2 parts 4–6 and C.4.3 parts 1–3.\n\n"+extra+
                      "\n---\n\nSource: `docs/global_nonlinear.md`; complete C.4.7.8 and C.4.7.9.\n\n"+closure)
    sources = [ROOT/"docs/global_nonlinear.md", ROOT/"docs/special_data_limits.md", STUDY/"dependencies_v1.md", output]
    print(json.dumps({str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}, indent=2))


if __name__ == "__main__":
    main()
