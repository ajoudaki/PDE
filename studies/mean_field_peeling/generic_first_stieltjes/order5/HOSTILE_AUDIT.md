# Hostile audit: generic `H=2`, `B=1` through order five

Status: **all mandatory unit-Gram, layer-tagged, and symbolic-`Q0` gates passed**

This audit is independent of both Gaussian-normal-form compilers.  It does
not alter either coefficient map after comparison.  The frozen contract is
[`PROOF_CONTRACT.md`](PROOF_CONTRACT.md), and the independent audit program is
[`audit_hostile.py`](audit_hostile.py).

## 1. Universal differential identity and normalization

The proposed identity

\[
\begin{aligned}
D^5f={}&2V[p^5]+22U[Hp,p^3]+14T[T[p,p],p,p]\\
&+30T[H^2p,p,p]+36T[Hp,Hp,p]+16\lVert H^2p\rVert^2
\end{aligned}
\]

passed three genuinely distinct checks.

1. The tensor product-rule derivation in
   [`FINITE_WIDTH_ORDER5_AUDIT.md`](FINITE_WIDTH_ORDER5_AUDIT.md) gives the
   coefficient vector `(2,22,14,30,36,16)`.
2. The moving-feature jet and raw multivariate Taylor AD agree seedwise for
   four activation families at widths one and two; raw AD's separately
   materialized six contractions agree with its fifth operator iterate.
3. `audit_hostile.py` constructs a dense, inhomogeneous, generic degree-five
   polynomial in two variables using an unrelated exact rational
   sparse-polynomial algebra.  It compares the complete polynomial
   `(grad f dot grad)^5 f`, not samples at selected points, with the six
   tensor contractions and obtains exact equality.

The raw-coordinate form also passes.  With `v=n p_theta`, the six explicit
width prefactors and velocity multiplicities are respectively

\[
(0,5),(1,4),(1,4),(2,3),(2,3),(3,2),
\]

so every term is exactly `n^5` times its raw-gradient contraction.  The
reduction to the active first-layer coordinate is metric-correct: its
Euclidean scale is `sqrt(Q0)`, hence the feature equation contains `Q0`.

**Gate result:** finite-width six-family identity and raw scaling pass.

## 2. Parity

Under the orthogonal involution `a -> -a`, `f` is odd and the operator
`D=n grad(f) dot grad` reverses parity.  Therefore `D^k f` has parity
`(-1)^(k+1)` in the readout.  At every finite width, before any limit,

\[
\mathbb E f=\mathbb E D^2f=\mathbb E D^4f=0.
\]

This argument uses neither a formal Gaussian limit nor a compiler
cancellation.

**Gate result:** parity passes.

## 3. Exact controls

- Constant `phi=c`: direct differentiation gives `E Df=c^2` and all higher
  derivatives zero.
- Linear `phi=x`: the exact Wick enumerator was rerun through additional
  widths four, five, and six, beyond the frozen test panel.  It reproduces
  `A=3`, `B=48+60/n`, and
  `C=1464+4800/n+4320/n^2`, hence `(3,48,1464)`.
- Affine `phi=1+2x`: the exact width-one Wick value and two seedwise finite
  derivative implementations agree.  Direct evaluation of the frozen
  layer-tagged population artifact gives `(A,B,C)=(57,15376,8074496)`.
  The additional affine `phi=1+x` gives `(6,112,4400)`.
- Quadratic `phi=x^2`: the generic finite-width jet agrees with the established
  quadratic compiler, and an independent exact evaluator applied to the
  frozen primary layer-tagged artifact gives exactly
  `(111,1685184,77400633120)`.

The unit-Gram and quadratic controls must not be conflated.  For the
unnormalized quadratic at `Q0=1`,

\[
Q^1=3,\qquad Q^2=27,
\]

so `(111,1685184,77400633120)` must be evaluated in the layer-tagged,
arbitrary-forward-variance form.  It cannot be obtained by substituting
`phi=x^2` into a formula already quotiented by `M_200000=1`.

The exact arithmetic consequence of the accepted quadratic triple was
checked independently:

\[
\mu_0=\frac{280864}{4107},\qquad
\mu_1=\frac{38443196932}{5616860517}.
\]

**Gate result:** finite-width and population controls pass in both frozen
coefficient routes.

## 4. Padé and induced loss algebra

Exact rational series reversion independently reproduces

\[
K(y)=A+\frac{B}{2A^2}y^2
+\frac{AC-4B^2}{24A^5}y^4+O(y^6)
=A+\mu_0y^2-\mu_1y^4+O(y^6).
\]

Expansion of

\[
A+\frac{\mu_0y^2}{1+(\mu_1/\mu_0)y^2}
\]

matches those coefficients.  Separating
`ydot=2 eta (1-y) K_[0/1](y)` gives exactly the integral in
[`PADE_AND_LIMIT_AUDIT.md`](PADE_AND_LIMIT_AUDIT.md).

Required caveats are present: `A != 0` for local inversion, `mu0 != 0` for
the displayed one-pole parametrization, and the implicit curve holds only on
the connected interval avoiding denominator zeros/poles.  The rational
approximation is to `K`, and the loss curve is induced by it; no positive-time
neural trajectory theorem is claimed.  Positivity/Stieltjes language also
requires the relevant signs and nondegeneracy, not smoothness alone.

**Gate result:** conditional Padé/loss algebra passes.

## 5. Complete leading-width peel

Write ordinary Taylor coefficients as `[t^k]`.  With `A_0=W/sqrt(n)`,
`h=phi(u)`, `g=phi(z)`, and `b=a phi'(z)`, the exact finite-width feature
flow is

\[
\dot a=g,\qquad \dot A=\frac1n b h^\top,\qquad
\dot u=Q^0\phi'(u)A^\top b.
\]

Consequently, without an asymptotic step,

\[
A_m=\frac1{mn}\sum_{p+q=m-1}b_p h_q^\top,
\]

and hence

\[
\begin{aligned}
z_k&=A_0h_k+
\sum_{m=1}^k\frac1m\sum_{p+q=m-1}
b_p\left(\frac1nh_q^\top h_{k-m}\right),\\
r_k&=[A^\top b]_k=A_0^\top b_k+
\sum_{m=1}^k\frac1m\sum_{p+q=m-1}
h_q\left(\frac1nb_p^\top b_{k-m}\right).
\end{aligned}
\tag{5.1}
\]

This exposes every train-time rank-one branch before the width limit.  There
are no hidden empirical covariances in the terminal artifact.

### 5.1 Width and equality partitions

Row-neuron and column-neuron indices are treated as distinct types even though
both widths equal `n`.  An `A_0` entry has valuation `n^(-1/2)`; coordinate
vectors have valuation one; each explicit rank-one `A_m` has entry valuation
`n^(-1)`; and its subsequent inner product supplies exactly one free typed
index and a factor `n`.  Thus every term retained in (5.1) is order one.

Condition on all program lines preceding the current use of `A_0`.  Wick
pairings of matrix entries have only three leading possibilities:

1. same-orientation pairings create a fresh Gaussian covariance;
2. opposite-orientation pairings attach to one earlier input direction and
   create a transpose response; or
3. a matrix occurrence belongs to one of the explicit rank-one `A_m` terms
   already displayed in (5.1).

An additional equality of free indices within either typed neuron set loses a
factor `n` with no compensating normalization, hence is `O(n^(-1))`.  A
row--column numerical equality is not a legal Wick delta because the two
index types are untied.  These cases exhaust the equality partitions of every
fixed fifth-order coefficient.

### 5.2 Complete transpose-response registry

Let `F_k` be the fresh part of `A_0h_k` and `R_k` the fresh part of
`A_0^T b_k`.  The exhaustive opposite-orientation branches are

\[
A_0h_k=F_k+\sum_{s<k}b_s\alpha_{ks},\qquad
\alpha_{ks}=\mathbb E\,\partial_{R_s}h_k,
\]

\[
A_0^\top b_k=R_k+\sum_{s\le k}h_s\beta_{ks},\qquad
\beta_{ks}=\mathbb E\,\partial_{F_s}b_k.
\tag{5.2}
\]

Through the required order there are exactly fifteen `alpha` and fifteen
`beta` branches.  The following is the full registry; `N` means a generically
nonzero exact moment polynomial and `0` an identically zero readout-parity
branch:

| row | entries in increasing `s` |
|---|---|
| `alpha_1` | `N` |
| `alpha_2` | `0,N` |
| `alpha_3` | `N,0,N` |
| `alpha_4` | `0,N,0,N` |
| `alpha_5` | `N,0,N,0,N` |
| `beta_0` | `0` |
| `beta_1` | `N,0` |
| `beta_2` | `0,N,0` |
| `beta_3` | `N,0,N,0` |
| `beta_4` | `0,N,0,N,0` |

The covariance registry is also complete: all 21
`H_kl=E[h_k h_l]`, `0<=l<=k<=5`, and all 15
`B_kl=E[b_k b_l]`, `0<=l<=k<=4`, are constructed chronologically.  Exact
parity gives `H_kl=B_kl=0` when `k+l` is odd.  Both implementations materialize
all 66 deterministic registry entries (30 responses and 36 covariances)
before the terminal expectation.

### 5.3 Wick--Stein elimination

The fresh `R` family is centered Gaussian with covariance `B`; ordinary Wick
pairing removes every `R` monomial.  The family `(F_0,F_1,...,F_5)` is centered
Gaussian with covariance `H`, where `F_0` is the second-layer activation
argument.  Picking an explicit `F_i`, `i>0`, gives the exhaustive inverse-free
identity

\[
\mathbb E\left[F_i\prod_{j>0}F_j^{m_j}P(F_0)\right]
=\sum_{j>0}m_jH_{ij}\,
\mathbb E\left[F_j^{-1}\prod_{\ell>0}F_\ell^{m_\ell}P(F_0)\right]
+H_{i0}\mathbb E\left[\prod_{j>0}F_j^{m_j}P'(F_0)\right],
\tag{5.3}
\]

where `F_j^{-1}` denotes lowering that monomial exponent by one, not a random
inverse.  Repeated application ends in literal `Y_nu` atoms; readout Wick
pairing and reverse-family Wick pairing end in `X_nu` atoms.  The base first-
and second-layer Gaussians are independent, so the terminal expressions are
products of one-dimensional atoms.  No covariance inverse or nonsingularity
assumption occurs.

Equations (5.1)--(5.3), the 66-entry registry, and the exact DAG traversal
cover every leading equality, low-rank, Wick, Stein, and transpose branch.
Both independently written eliminators produce the identical unit-Gram
coefficient map reported below.

**Gate result:** complete leading-width peel passes; there are no unresolved
branches.

## 6. Probability and regularity boundary

The theorem tier must encode the final fifth-order observable as a fixed
finite NETSOR-transpose-plus scalar program.  Under polynomial smoothness
(`phi in C-infinity` and every derivative polynomially bounded), the cited
all-finite-`Lp` tensor-program theorem supplies uniform integrability and the
annealed limit.  With only finite-order assumptions, the exact finite-width
algebra requires `C^5` locally and integrability of all contractions, but an
annealed limit additionally needs an explicit condition such as

\[
\sup_n \mathbb E |D_n^5 f_n|^{1+\epsilon}<\infty.
\]

The pseudo-Lipschitz almost-sure tier does not by itself justify expectation
convergence.  No Hermite approximation is used in any tier.

The finite chronological construction (5.1)--(5.3) uses a number of vector,
matrix, coordinatewise nonlinearity, and empirical-moment lines independent
of `n`; it is therefore the required fixed scalar program.

**Gate result:** the theorem envelope and exact fixed-program mapping pass.

## 7. Frozen coefficient comparison

Both producers were frozen before the hostile comparison.  The common unit
quotient identifies `X_nu,Y_nu -> M_nu`, sets `Q0=1`, and imposes
`M_200000=1`.  No integration-by-parts or other moment identity was used in
the diff.  Direct expansion of the primary arithmetic DAG and literal exact-
rational comparison with the independent sparse map gives

| root | primary monomials | independent monomials | discrepancies |
|---|---:|---:|---:|
| `A` | 3 | 3 | 0 |
| `B` | 46 | 46 | 0 |
| `C` | 974 | 974 | 0 |

The same independent comparison before the unit quotient, retaining distinct
`X` and `Y` atoms at `Q0=1`, gives

| root | primary monomials | independent monomials | discrepancies |
|---|---:|---:|---:|
| `A` | 3 | 3 | 0 |
| `B` | 50 | 50 | 0 |
| `C` | 1,045 | 1,045 | 0 |

The primary unit artifact SHA-256 is
`3be176963679c40127ac4f94305eeb7e4ef684a06910ae99a68a0f3528333214`.
The independent exact-file-byte SHA-256 is
`fa3b4a6f7dc665e63e2c02355a14122f89f56bdfd34f0fe7402be4cab0ff2878`.
The independent layer-tagged exact-file-byte SHA-256 is
`52832afc4f9e1cf27f5b8465f2f5373bcb3e9f5c56b0686c9366162da2e17c11`.
The first independent freeze used a content hash excluding the terminal
newline; that was corrected.  A final, explicitly authorized metadata-only
rewrite then removed a falsely labelled duplicate `layer_tagged` object;
`unit_gram.A/B/C` did not change.  The hash above is the final exact-file hash,
and the literal diff was rerun after that rewrite.

Every terminal atom is one-dimensional, uses one of the six declared slots,
and has maximum derivative exactly five.  No `F`, `R`, response, covariance,
pseudoinverse, or empirical object survives.  The first independent JSON's
`layer_tagged` metadata section accidentally duplicated its unit quotient and
is not used; the separately hashed layer-tagged artifact above replaces it.

As a transcription-specific gate, equations (2.2)--(2.5) of
[`PRIMARY_GAUSSIAN_NORMAL_FORM.md`](PRIMARY_GAUSSIAN_NORMAL_FORM.md) were
encoded independently and distributed.  The result has 46 monomials and is
exactly the frozen `B` coefficient dictionary, with zero mismatch.

The fully symbolic `Q0` powers received a separate post-freeze audit.  Treating
the `X` and `Y` atoms as formal degree-zero generators, the exact feature
vector field contains explicit `Q0` only in
`udot=Q0 phi'(u) A^T b`.  Induction on the number of directional derivatives
therefore bounds the explicit degrees of `A,B,C` by `1,3,5`.  The independent
compiler was evaluated in exact `Fraction` arithmetic at the six points
`Q0=1/2,1,3/2,2,5/2,3`, before the primary symbolic map was loaded.  Lagrange
interpolation reconstructed every graded activation-monomial coefficient;
the observed maximum degrees were exactly `1,3,5`.  The unused exact holdout
`Q0=7/2` had zero discrepancies.

Only after that reconstruction was serialized and frozen was the primary
symbolic map expanded.  A literal comparison with key
`(sorted X/Y atom tuple,Q0 power)` gives zero discrepancies in all
`3/50/1,045` graded terms.  `audit_hostile.py` independently reparses both
frozen JSON files, rejects duplicate or malformed graded keys, checks the
degree and derivative ceilings, and repeats this literal dictionary diff.
The independent symbolic exact-file SHA-256 is
`e682c708fedadc577b7446a7b9c07b79262c945fbae5726918436153876f889a`.
Earlier specialization checks at `Q0=1/2,1,2`, the exact finite-width feature
ODE at `Q0=0.73`, and the exact linear evaluations
`(A,B,C)=(3Q0,48Q0^2,1464Q0^3)` at `Q0=2/3,7/10,5/2` remain additional
controls, not inputs to the symbolic comparison.

The hostile protocol was:

1. preserve the primary symbolic-`Q0` map, independently reconstruct the
   graded map from six exact rational points with a seventh unused holdout,
   freeze it, and only then perform the full symbolic dictionary comparison;
2. map both unit formulas to the declared canonical grammar;
3. impose `M_200000=1` identically on both, with no further identities or
   integration-by-parts simplifications;
4. compare exact rational coefficient dictionaries for `A`, `B`, and `C`;
5. reject any atom containing a derivative above five or any undeclared
   auxiliary variable;
6. evaluate both frozen layer-tagged maps on constant, linear, affine, and
   unnormalized quadratic activations; and
7. run the preregistered normalized-sine regression only after a common
   theoretical `C` is frozen.

No discrepancy was repaired after the coefficient comparison.

### 7.1 Preregistered nonpolynomial control

For normalized sine, exact finite Fourier sums (not quadrature, Hermite, or a
polynomial approximation) evaluate the common map as

\[
(A,B,C)=(4.037096946465644,-103.25733114677432,
29944.43234293731).
\]

The frozen 1,280-network panel gives an extrapolated intercept
`26949.75169061648` with standard error `2326.2945580581186`, so the
prediction differs by `1.2873` standard errors.  The regression diagnostics
are valid (`chi^2=0.7734` for 3 degrees of freedom), and the preregistered
decision is **pass**.  The exact finite-width pre-gate discrepancy was
`2.92e-14`.  The complete record is
[`SINE_REGRESSION_RESULT.json`](SINE_REGRESSION_RESULT.json).

## 8. Self-contained delivery audit

The designated deliverable is
[`H2_B1_ORDER5_SELF_CONTAINED.md`](H2_B1_ORDER5_SELF_CONTAINED.md).  It
contains the exact network, initialization, `D_n` and annealed-limit
definitions; the moment alphabets; compact `A` and `B`; the complete finite
`C` DAG; all six finite-width tensor families; the equality/response/Wick--
Stein ledger; controls; `mu_0,mu_1`; the kernel series; the one-pole Padé
kernel; the separated loss curve; and the precise two-tier regularity/UI
statement.

Both terminal arithmetic DAGs are embedded byte-for-byte.  Independent marker
extraction reproduces the frozen unit and layer-separated artifacts exactly,
with SHA-256 values

\[
\begin{aligned}
\text{unit}&:\quad
\mathtt{3be176963679c40127ac4f94305eeb7e4ef684a06910ae99a68a0f3528333214},\\
\text{layer-separated}&:\quad
\mathtt{5219b3558aec52a2065b93ba7d6ce0e350ee930c2048518fcd012ba61f605ec9}.
\end{aligned}
\]

The final report's own SHA-256 is
`3ee1f31b34768e47d9ec15011c2955a365c8d888fcd7663c2bba2cc1aa483390`,
matching [`SELF_CONTAINED_MANIFEST.json`](SELF_CONTAINED_MANIFEST.json).
The integrated Padé/loss formulas passed the independent exact-rational
series test.  The document also states explicitly that a positive one-pole
Stieltjes interpretation needs `A>0`, `mu0>0`, `mu1>=0`, and the relevant
nondegeneracy/no-pole conditions.

**Gate result:** self-contained formula and byte-integrity gate pass.

## 9. Final gate table

| Gate | Result |
|---|---|
| Six contraction families | pass |
| Raw/whitened width scaling | pass |
| Finite-width route equality | pass |
| Parity | pass |
| Constant/linear/affine finite controls | pass |
| Unit versus unnormalized-quadratic scope | pass |
| Padé and loss algebra | pass |
| Literal unit coefficient-map diff | pass, 0/1023 discrepancies |
| Layer-tagged `Q0=1` coefficient-map diff | pass, 0/1098 discrepancies |
| Fully symbolic `Q0` coefficient-map diff | pass, 0/1098 discrepancies; unused `7/2` holdout passes |
| Derivative ceiling and terminal atom grammar | pass |
| Generic linear/quadratic substitutions | pass independently |
| Preregistered nonpolynomial regression | pass |
| Complete response/equality/Wick--Stein ledger | pass |
| Self-contained report and embedded-byte integrity | pass |
| Theorem-level annealed formula | pass for polynomially smooth activations |

**Promotion decision:** the unit-Gram, layer-separated, and full
symbolic-`Q0` `A,B,C` maps are algebraically audited with no unresolved
coefficient or peeling mismatch.  Under the stated polynomial-smooth
fixed-program hypotheses their annealed limits are theorem-level.  The
Padé/loss curve remains exactly the curve induced by the rational kernel and
is not promoted to an exact positive-time neural trajectory.
