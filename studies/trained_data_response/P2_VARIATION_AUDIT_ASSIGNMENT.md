# Neutral assignment: conditional variation lemma

Fresh reviewer: `/root/p2_conditional_audit`; author: `/root/p2_variation`.
This is a scoped adversarial check of one conditional lemma, not a complete
milestone-2 scientific review or a promotion gate.

Read only P2_VARIATION.md, docs/NOTATION.md, the required rigorous-math and
conjecture-investigation skill instructions/references, and shared process
instructions. Do not read other P2 files, README, P1 verdicts, studies or
history. Audit every argument under the stated strong-solution and uniform
integrability assumptions, especially the one-bounded-readout endpoint
comparison, compact-direction Taylor expansion, uncentered Gaussian clock,
and measurability. The neural integrability and existence assumptions are
explicitly conditional; do not accept them as unconditional conclusions.

Write P2_VARIATION_AUDIT.md with input hash, complete read coverage, actual
attacks and any required corrections. Scratch belongs in
`data/generated/trained_data_response/p2_20260911_02/variation_audit/`.
No Git or experiments. No prior verdict is supplied.

## Missing original equation supplied during the audit

The original prompt's physical state is (w,K,c), with A=A₀+K and φ=tanh.
For an input u, z₁=w·u, h₁=φ(z₁), z₂=Ah₁, h₂=φ(z₂), f=⟨c,h₂⟩,
d₂=cφ'(z₂), p₁=A*d₂, and d₁=φ'(z₁)p₁, where A* is the actual
Hilbert adjoint. Its exact vector field is

\[
F_\mu=(-2\int(f-y)d_1u\,d\mu,
       -2\int(f-y)d_2\otimes h_1\,d\mu,
       -2\int(f-y)h_2\,d\mu).
\]

Initialize w as a standard Gaussian pair, K=c=0, and ∥A₀∥≤10.
The prompt also supplies a reference response on a clock L² space with
bounded propagation. The reviewer may verify the lemma's self-defined
response; identification with P1 is the coordinator's separate check.
Record this supplement as an added allowed input. It contains no previous
review result.
