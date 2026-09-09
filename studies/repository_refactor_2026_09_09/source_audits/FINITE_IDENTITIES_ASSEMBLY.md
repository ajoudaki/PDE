# Exact finite identities: assembly and source assessment

This is a bounded source assessment and incorporation record, not an acceptance review. The candidate chapter text is in `../FINITE_IDENTITIES_ADDITION.md`. It contains deterministic finite identities and global finite physical gradient flow.


## Source assessment, corrections and dependencies

The primary mixed and RMS documents were read completely. The imported
claims are finite algebra and finite-dimensional continuation. None depends
on the partial-activation Gaussian recurrence, order-seventeen moments,
tensor-program theorems, traffic constructions, simulations, or the RMS
initialization/activity asymptotics. Those are outside this candidate.

The mixed source uses `G=W/sqrt(n)`, normalized neuron pairings, an
order-one Gaussian stored readout for its initialization statements, and
physical clock `2 eta (y-f)`. Here `B` is that already scaled matrix,
the metric is translated explicitly in (8), `eta=1`, and physical time
uses the library sign `r=f-y`. The deterministic statements hold for any
finite readout, including the library's small-readout initialization, but
the source's Gaussian initialization numbers do not transfer to it.

Corrections carried into the candidate:

- The RMS protocol's amendment at lines 142–147 replaces the draft matrix
  metric `n^-1 Tr(dG dG^T)` by `Tr(dG dG^T)`. The pause packet, lines
  14–29, also rejects an additional `1/n` in matrix action. Equation (8)
  retains both corrections.
- The RMS theorem's kernel (2.4), lines 77–91, omits plus signs between
  its three summands. Its own derivation and pause packet lines 58–64
  give the sum used in (26). The omitted plus in the initialization Wick
  expansion at lines 285–288 is recorded but unused.
- The RMS theorem's sentence at lines 167–169 claiming both balance laws
  become invariants at epsilon zero is false for the row law. Equations
  (30) retain the correct displayed drifts and derive them independently.
- The same theorem's lines 332–336 overstate the consequence of positive
  initial hidden speed for tangent linearization. All initialization and
  positive-time nonlazy statements are excluded from this candidate.
- `OLD_NONLINEAR_RESNET_RMS.md` lines 181–202 explicitly record these RMS
  formula/interpretation corrections and the still-open kinetic/source
  bridge. The mixed assessment at `LINEAR_AND_REPRESENTATION.md` lines
  175–193 validates the finite reductions, but does not certify the
  order-seventeen computational certificate or a positive-time limit.

The source is therefore closed for this bounded exact package after the
explicit corrections. The remaining continuum-source, response-domain,
weighted-tail, uniqueness and width-limit gates belong to other claims.
No new proof-search campaign or experiment is needed for these identities.

Source paths below are relative to the repository root. Read ranges are
inclusive; a range other than the entire file is explicitly a partial read.
Hashes are SHA-256 of the entire source file at assessment time.

| Source | Read range | SHA-256 |
|---|---|---|
| `docs/NOTATION.md` | 1–98, complete | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/finite_dynamics.md` | 1–214, complete | `486a2864738d23c21e14e3830ee4cd9555ef2e909d2054366890a958a3dc626c` |
| `studies/mfp_quadratic_compiler/autonomous_single_source_closure/THEOREM_AND_AUDIT.md` | 1–325, complete | `0a7c7313a447b3f7f5345b5901f189ff6133d22401a4bb6c3f7bad87242e42e0` |
| `studies/mfp_quadratic_compiler/autonomous_single_source_closure/PROTOCOL.md` | 1–91, complete | `28434136bdd2268ab31027446829031dc949c27792b564e1ea3b2bfea056d571` |
| `studies/mfp_quadratic_compiler/autonomous_single_source_closure/EVIDENCE_LEDGER.md` | 1–16, complete | `708f75b474dea8f5bdcc30d6b3fb133ee307d96c0ed111f1f97120e6a2ca4a32` |
| `studies/mfp_quadratic_compiler/rms_normalized_operator_closure/FINITE_WIDTH_THEOREM.md` | 1–337, complete | `a712fb83e09b90c283ad82b44d0026d2749f79db204ad14322a805be4e9a740f` |
| `studies/mfp_quadratic_compiler/rms_normalized_operator_closure/PROTOCOL.md` | 1–147, complete | `4f0db9e8c9ccb306f4d5d5e160d1f7fe6f718310c88105198401bb0ae13a3e6c` |
| `studies/mfp_quadratic_compiler/rms_normalized_operator_closure/EVIDENCE_LEDGER.md` | 1–53, complete | `12cfd0d0b1e36034c2d9adcaff2cc8bd6a7af47fdf4c9c946c04fc12a50e90ee` |
| `studies/mfp_quadratic_compiler/rms_normalized_operator_closure/PAUSE_STATE.md` | 1–95, 211–250 | `b52a953631d9039c16cd99f396a578474b89e659f56b1d9815cf33e77fa39511` |
| `studies/project_wide_audit_2026_09_08/source_audits/OLD_NONLINEAR_RESNET_RMS.md` | 130–225 | `d19b839ad051ede6ac119a6b63c840192874c98cadf32ee5ef36d0e5f577bb46` |
| `studies/project_wide_audit_2026_09_08/source_audits/LINEAR_AND_REPRESENTATION.md` | 175–194 | `0987879f331b5cb42a482fba9ff7def2566f018413f228f87582a08d7fd22681` |
| `code/pde/finite_network.py` | 1–363, complete | `efe694b200b8af2603cbf1bb9d0249f49636e874088c2bafd98f402b5bfbe551` |
| `studies/mfp_quadratic_compiler/rms_normalized_operator_closure/HOSTILE_AUDIT.md` | 1–163, complete | `ec58c6ceca0bfbfc8f059646504c877af227cbd241919a15c0c332c7181b02f5` |
| `studies/mfp_quadratic_compiler/rms_normalized_operator_closure/PRIMARY_SOURCE_AUDIT.md` | 1–47, complete | `21eeffb51576224a0aa49b5cdacf4bd42186ef216980a4cf19680cb3b0982acc` |
| `studies/mfp_quadratic_compiler/rms_normalized_operator_closure/OPERATOR_SOURCE_AUDIT.md` | 92–123 | `9c15e223c3ad0c64005d816d8e82d654f8ab2991d5b0aa250aa7085fc128ce0d` |
| `studies/repository_refactor_2026_09_09/ADVISORY_COVERAGE_DISPOSITION.md` | 205–260 | `2c4c4cbb89b811afcd51977fcbeb08b1d92e67a30e63be4e6b583046a2e36fdc` |
| `code/README.md` | 1–271, complete | `b563a8a4fcebbb5fb634057f6cf09d32475462670002c8fbad0502f5c06482e0` |
| `code/tests/test_finite_network.py` | 1–175 | `a45ddc72c943b85aff63b6c4d49c88d8784100dbed8878cd9bb710b8256b9931` |

The additional fully read RMS `HOSTILE_AUDIT.md` and
`PRIMARY_SOURCE_AUDIT.md` delimit the excluded population claims; neither
is an external theorem dependency of the proposed finite proof. The exact
reduced-source formula in `OPERATOR_SOURCE_AUDIT.md` lines 92–123 was also
checked. The code module is an implementation dependency for the shared
parameter structure, not a mathematical premise.

## Bounded API and validation

`code/pde/finite_reductions.py` supplies `mixed_quadratic(parameters, label,
model=...)`, `mixed_lax(parameters, model=...)`, and
`rms_quadratic(parameters, label, epsilon=...)`. All use the existing
`Parameters` structure and validate exactly depth two and input dimension
one; the input is fixed to one. They evaluate finite current states without
initialization, solver steps, trajectory files or population replacements.
`model` and `epsilon` are keyword arguments; the RMS epsilon is required
and strictly positive. No mobility argument is accepted: these particular
identities use the three unit multipliers.

`ReductionEvaluation` contains output, residual, loss, kernel, three kernel
blocks in first/middle/readout order, physical output/loss velocities,
parameter output-ascent and physical velocities, copied current fields and
their feature-ascent derivatives. QQ and RMS additionally return the row
and column balance-ascent derivatives. RMS uses the public field key
`q_tilde` for the corrected backward vector; `t` is reserved for time in
the mathematical text. `LaxEvaluation` contains the isometric factor,
factor-ascent, Gram, signature, operator, generator and commutator. Its IQ
generator includes the factor two. The main evaluators use `O(n^2)` work
and storage; the explicit dense Lax products use `O(n^3)` work and
`O(n^2)` storage. Returned arrays are fresh; ordinary float64 limitations
and rejection of evaluated nonfinite outputs are explicit.

The dedicated suite passed nine tests after the final notation change:

```text
PYTHONPATH=code PYTHONDONTWRITEBYTECODE=1 OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python -B -m unittest discover -s code/tests -p 'test_finite_reductions.py' -v
Ran 9 tests. OK.
```

It compares all mixed flows/kernel blocks against the independent established
layerwise finite core at widths one and three and both residual signs,
including zero residual. It differentiates the RMS output definition in
every parameter coordinate and independently checks all kernel blocks,
feature derivatives, physical energy, sign/zero-coordinate behavior and
both signed balance drifts. It checks the Lax factor chain rules,
commutators, the explicit orthogonal-conjugacy witness, and QQ balances.
Scope validation and array ownership are checked. These are bounded finite
unit checks, not training experiments or evidence for an asymptotic theorem.
The established full-suite and assembly checks remain the coordinator's
integration responsibility.
