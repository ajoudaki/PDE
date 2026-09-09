# Hostile audit: depth `H=3,4`, `B=1`, through order five

**Final verdict:** **PASS for the fixed-depth `H=3,4`, `B=1`, order-five
deliverable under the theorem hypotheses stated below.**  There is no
unresolved coefficient mismatch, terminal-grammar violation, equality/
transpose branch, or failed mandatory control in this scope.

The authoritative audit contract is [`AUDIT_CONTRACT.md`](AUDIT_CONTRACT.md),
and the typed claim state is [`EVIDENCE_LEDGER.md`](EVIDENCE_LEDGER.md).

The arbitrary-depth deep-linear closed-form interpolant remains conjectural;
it is not used in this verdict.  Growing-depth limits, positive-time flow
convergence, and depth-uniform flat-formula complexity also remain open.

## 1. Frozen bytes and literal formula comparison

The primary producer manifest has exact-file SHA-256

`f4838437c1fb70b14713d39e8438d703434c49ffd72001beeb6fee8d53366b30`,

and the independently frozen producer manifest has SHA-256

`dee0198e119864a90195101466f29f3ab2f248495c6e6a3494f35cafd3f2502b`.

Every manifest entry was rehashed before comparison.  In the common tagged
quotient (`Q0=1`, layer tags retained) and in the unit-Gram quotient, the
exact-rational coefficient-map differences are:

| map | `A` terms / mismatches | `B` terms / mismatches | `C` terms / mismatches |
|---|---:|---:|---:|
| H3 tagged | 4 / 0 | 342 / 0 | 27,421 / 0 |
| H3 unit | 4 / 0 | 160 / 0 | 6,519 / 0 |
| H4 tagged | 5 / 0 | 1,929 / 0 | 462,776 / 0 |
| H4 unit | 5 / 0 | 350 / 0 | 17,641 / 0 |

Both routes have terminal derivative ceilings `(1,3,5)` for `(A,B,C)`.
No terminal leaf other than a rational, explicit `Q0`, or declared
one-dimensional layer activation moment occurs.

The primary symbolic `Q0` coefficients were then compared with fresh exact-
rational independent compilations at six points
`1/2,1,3/2,2,5/2,3`.  The explicit degree bounds are `(1,3,5)`, so six-point
coefficientwise equality proves the complete polynomial identity.  The
unused `Q0=7/2` holdout also has zero discrepancies at both depths.  The
certificate SHA-256 is
`fb7dbab7cea9b6e1a2e18275ee695f6be56e8640199640a2bb1758ea864ee6ef`.

## 2. Exact finite-width and structural gates

Direct differentiation gives, with `M^ell=W^ell/sqrt(n)`,

\[
\dot a=h^H,\qquad
\dot M^\ell=n^{-1}b^\ell(h^{\ell-1})^T,\qquad
\dot z^1=Q^0b^1.
\]

The exact ordinary-series convolution therefore includes every moving
rank-one update before a width limit.  Raw-gradient squaring independently
gives

\[
D_nf_n={\|h^H\|^2\over n}+{Q^0\|b^1\|^2\over n}
 +\sum_{\ell=2}^H{\|b^\ell\|^2\|h^{\ell-1}\|^2\over n^2},
\]

which agrees seedwise with the first moving coefficient.  A raw
multivariate-parameter differentiator and the moving-flow jet agree through
fifth order, including exact-rational affine checks at both depths.  Two
separately written arbitrary-width moving jets additionally agree for
`H=3,4`, widths `1,2,5`, and three normalized-sine seeds per cell; their
worst scaled discrepancy is `2.7440568250379693e-14` against the frozen
`1e-10` threshold.

Readout reflection proves at finite width, without relying on compiler
cancellation,

\[
\mathbb E f_n=\mathbb E D_n^2f_n=\mathbb E D_n^4f_n=0.
\]

For each initialized hidden matrix, the complete order-five leading registry
has 21 forward covariances, 15 reverse covariances, 15 earlier-transpose
responses, and 15 forward responses.  The forward/reverse branch census also
contains every literal integrated rank update.  Additional same-type
equalities lose a free width sum; different layer indices are different
types.  Thus the 66-state registry closes all leading equality and transpose
families.  The precise census is in
[`STRUCTURAL_AUDIT.md`](STRUCTURAL_AUDIT.md).

Finite-width derivative counting alone would not control Stein derivative
raising.  Here the Wick--Stein eliminator strictly lowers innovation degree,
and a time-grade invariant bounds any derivative raise by the order of the
removed forward innovation.  Both independently frozen terminal scans then
confirm the sharp ceilings `(1,3,5)`.

## 3. Controls

- Constant activation is proved directly at finite width:
  `(A,B,C)=(c^2,0,0)` at every depth.
- A producer-independent path-copy/union-find/Wick enumeration gives
  `(4,160,13888)` at H3 and `(5,400,73240)` at H4, together with every
  finite-width `1/n` correction recorded in
  [`DEEP_LINEAR_AUDIT.json`](DEEP_LINEAR_AUDIT.json).
- Independent exact Gaussian-polynomial evaluation gives the affine values
  `(10,540,71152)` and `(15,1848,591176)`.  Exact-rational raw/moving jets
  supply a separate finite-width affine check.
- The unnormalized quadratic and normalized-sine analytic evaluations agree
  across the frozen routes.  The unit-Gram quotient is not confused with the
  unnormalized quadratic model.

The preregistered normalized-sine experiment used all 7,700 allowed networks
with no exclusions or nonfinite jets.  Every four-batch stability gate and
both affine-fit chi-square gates pass:

| depth | `z` | chi-square / df | `p` | decision |
|---:|---:|---:|---:|---|
| 3 | 1.2002 | 1.8194 / 2 | 0.4026 | pass |
| 4 | 0.4749 | 2.0174 / 2 | 0.3647 | pass |

This is an empirical discriminator only, not part of the algebraic or
probability proof.

## 4. Probability and claim level

The finite-width identities require only `C^5` plus sufficient integrability,
for example polynomial growth of derivatives through order five.  That tier
does not by itself identify the annealed limit.

For each separately fixed depth, a sufficient theorem tier is

\[
\phi\in C^\infty,\qquad
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r})\quad\text{for every }r\ge0.
\]

The exact jet is then one finite NETSOR-transpose-plus program.  Under Setup
3.6 and Theorem 3.7 of Golikov--Yang, every final scalar converges almost
surely and in every finite `L^p`; `L^1` gives the annealed coefficient.  In a
weaker convergence-in-probability tier, the separately stated bound

\[
\sup_n\mathbb E|D_n^kf_n|^{1+\epsilon}<\infty,
\qquad k=1,3,5,
\]

is sufficient for uniform integrability.  These hypotheses and their fixed-
depth limitation are stated correctly in the final report.

## 5. Recursion and complexity verdict

At fixed order five the compiler has exactly `66(H-1)` independent registry
entries and `O(H)` outer layer transitions.  It retains the full earlier
chronology inside response DAGs; no scalar Markov closure has been smuggled
in.  This does **not** imply `O(H)` total symbolic work or a small flat
formula: the tagged `C` maps grow from 1,045 to 27,421 to 462,776 terms for
depths 2,3,4.  The observed near-linear factored-DAG growth through H4 is not
promoted to an arbitrary-depth complexity theorem.

The proposed deep-linear formulas for arbitrary `H` are explicitly described
as finite-difference discoveries.  Only `A_H=H+1` and the independently
enumerated H3/H4 values are certificates here; the general `B_H,C_H`
interpolants remain conjectural.

## 6. Final document integrity

The canonical report
`primary/H3_H4_ORDER5_SELF_CONTAINED.md` has SHA-256
`ea7730e5dc57c5cf96b9e60d289f1fb5f56797520604919818aa4bd958bd2414`.
Its report-manifest SHA-256 is
`07917e0ad68ea3d8d7f86e1fd3dfecde8f073a30c0e503ac5b748da42d1135e6`.
Deterministic reconstruction is byte-identical, every embedded CSE source and
audit hash matches, and the final top-level evidence ledger uses the same
claim levels and nonclaims.
