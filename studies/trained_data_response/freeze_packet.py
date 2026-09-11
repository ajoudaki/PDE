"""Freeze a complete scientific review packet; never overwrites a round."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[1]
HASHES = {
    'docs/README.md': '7824df11fe7fa2d89cf2c75dc32716438b20c815a18d1c3809a84a0785d9d34e',
    'docs/NOTATION.md': '199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b',
    'docs/global_nonlinear.md': 'd473d95ee27bc39d484185cea2689b5d3ceed448567a1527488f1003e24f1fa1',
    'docs/special_data_limits.md': '5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489',
    'docs/finite_dynamics.md': 'a57d832a0ce0ad2bf40fa1ec574af787d05bade3264b619a8faca5545bc0012a',
}
SPANS = [
    ('docs/README.md', 1, 273),
    ('docs/NOTATION.md', 1, 98),
    ('docs/finite_dynamics.md', 1, 227),
    ('docs/special_data_limits.md', 3785, 4326),
    ('docs/global_nonlinear.md', 1840, 2453),
    ('docs/global_nonlinear.md', 3972, 4296),
    ('docs/global_nonlinear.md', 5465, 6585),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main(round_name):
    assert round_name.isalnum() and round_name.startswith('R')
    files = ['THEOREM.md', 'PROPAGATOR.md', 'WEIGHTED_SOURCE.md', 'FINITE_CAPTURE.md']
    contents = {p: (BASE/p).read_bytes() for p in files}
    sources = {p: (ROOT/p).read_bytes() for p in HASHES}
    for p, data in sources.items():
        assert sha(data) == HASHES[p], f'Changed dependency: {p}; reread and update explicitly'
    proof = '# Frozen scientific candidate\n\n'
    proof += 'Authors: `/root`, `/root/propagator`, `/root/weighted_source`, `/root/capture`.\n'
    proof += 'Each component below is included verbatim; equation numbers are local to it.\n\n'
    for p, data in contents.items():
        proof += f'\n<!-- BEGIN {p} -->\n\n{data.decode()}\n<!-- END {p} -->\n'
    dependency = '# Complete frozen dependency inputs\n\n'
    dependency += 'These verbatim excerpts contain the invoked mathematical proofs. '
    dependency += 'Chapter equation numbering is local to each source proof unit.\n'
    records = []
    for p, start, end in SPANS:
        span = b''.join(sources[p].splitlines(keepends=True)[start-1:end])
        records.append(dict(source=p, first_line=start, last_line=end,
                            source_sha256=HASHES[p], excerpt_sha256=sha(span)))
        dependency += f'\n<!-- BEGIN {p}:{start}-{end} -->\n\n{span.decode()}\n<!-- END EXCERPT -->\n'
    check = (BASE/'check_identities.py').read_bytes()
    reference = sources['docs/global_nonlinear.md'].decode().split('###### 5. Reproducible rational Gaussian certificate', 1)[1]
    certificate = re.search(r'```python\n(.*?)\n```', reference, flags=re.S).group(1).encode()+b'\n'
    assignment = f'''# Neutral complete scientific review assignment

Review the mathematical validity and exact scope of the frozen candidate for
trained data response at a nonlinear fitted reference. This is an isolated
scientific review, not authorship, a promotion decision, or a search for a
preferred verdict. The candidate proposes a forced clock-state evolution,
actual finite-GF derivative capture on every fixed physical horizon and the
whole input circle, and a uniformly bounded population homogeneous propagator.

Read only this assignment, `{round_name}_MANIFEST.json`, the complete
`{round_name}_PROOF.md`, complete `{round_name}_DEPENDENCIES.md`, and
`{round_name}_CHECK_IDENTITIES.py` and `{round_name}_REFERENCE_CERTIFICATE.py`,
plus required skills. Do not read the study
README, author conversations, history, other rounds, or any reviewer findings.
The coordinator will assign your report path and scratch directory separately.
Write only that report and that scratch; do not edit the candidate or use Git.

Use `/etc/codex/skills/solve-math-rigorously/SKILL.md` and
`/etc/codex/skills/investigate-conjectures/SKILL.md`, with their applicable
research-contract and adversarial-audit references. Read every scientific line
of both proof and dependencies, repairing truncated reads. Verify the frozen
hashes before and after review. Report any missing required proof or input;
do not replace a missing dependency by a remembered specialized theorem.

Independently reconstruct all implications. Attack normalization, the actual
finite Gaussian readout, right differentiation before width, nonatomic exact
loss integration, both reused action directions, clock cancellation, cavity
conditioning and event dependence, Gaussian process bounds, weighted uniform
integrability and limit passage, bounded versus strongly continuous operators,
singular endpoint kernels and conditioning, finite-rank endpoint estimates,
fixed-program approximation versus a growing transcript, whole-circle
observations, support/weight-independent constants versus uniform probabilities,
and the stated nonlinear-continuation boundary. A conditional source equation
alone would not prove the candidate. Failure of an estimate alone is not a
counterexample to its claim.

Run the frozen deterministic identity check with --output under your fresh
scratch directory. Add meaningful independent algebra or boundary checks as
needed; no training experiments or parameter sweeps are authorized. Numerical
checks do not replace proofs. Read and run the complete contained rational
Gaussian certificate used by the reference dependency, saving its output
in your scratch directory.

Retain a full report with: reviewer identity and isolation attestation; exact
input hashes; complete reading coverage by file/line intervals; actual commands
and results; component verdicts and exact surviving gaps; specific required
corrections with proof locations; optional suggestions separately; and an
overall ACCEPT or CORRECTION REQUIRED verdict for the precise proposed scope.
Do not abbreviate a missing proof as routine. Do not claim formal verification.
'''
    outputs = {
        f'{round_name}_PROOF.md': proof.encode(),
        f'{round_name}_DEPENDENCIES.md': dependency.encode(),
        f'{round_name}_CHECK_IDENTITIES.py': check,
        f'{round_name}_REFERENCE_CERTIFICATE.py': certificate,
        f'{round_name}_ASSIGNMENT.md': assignment.encode(),
    }
    manifest = dict(round=round_name,
                    head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),
                    authors=['/root','/root/propagator','/root/weighted_source','/root/capture'],
                    inputs={p: dict(sha256=sha(data), lines=len(data.splitlines())) for p,data in outputs.items()},
                    author_sources={p: sha(data) for p,data in contents.items()},
                    dependency_excerpts=records,
                    check_scope='deterministic mathematical identities; no training experiments')
    outputs[f'{round_name}_MANIFEST.json'] = (json.dumps(manifest,indent=2)+'\n').encode()
    assert all(not (BASE/p).exists() for p in outputs), 'round already exists'
    for p, data in contents.items():
        assert (BASE/p).read_bytes() == data, f'author file changed while freezing: {p}'
    for p, data in sources.items():
        assert (ROOT/p).read_bytes() == data, f'dependency changed while freezing: {p}'
    for p, data in outputs.items():
        (BASE/p).write_bytes(data)
    print(json.dumps({p:sha(data) for p,data in outputs.items()},indent=2))


if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--round',required=True)
    main(parser.parse_args().round)
