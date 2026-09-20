# C-X3 activity candidate: author-side adversarial cross-check

2026-09-20. **PASS, scoped to the frozen finite-data every-layer onset
candidate. No blocking gap found in the adaptive-conditioning or
noncancellation induction.** This is an internal author cross-check, not
an isolated review, promotion approval, or certification of the complete
C-X3 contract.

## 1. Frozen inputs and scope

The complete frozen `CH3_ACTIVITY_PROOF.md` was read. The maintained inputs
used were `docs/global_nonlinear.md` C.1–C.3, including the final weighted-loss
and activation correction, its A.1–A.2 fixed-program extensions, and
`docs/special_data_limits.md` III.F.1–10. C.1–C.2, A.1–A.2 and III.F.1–10
were read during the preceding local-proof assignment; the conditioning
unit III.F.3–4 was reread for this check. C.3 and the entire activity
candidate were read for this assignment. No other author draft was read
for this cross-check, and neither frozen proof was edited.

The required proof and conjecture skills and their contract/adversarial
audit references remain applicable. Only textual reasoning, source reads,
source hashing and this report were performed; no numerical experiment,
training, or Git operation was used.

Source SHA-256 values captured at the start of this cross-check:

| File | SHA-256 |
|---|---|
| `studies/cx3_depth_extension_20260920/CH3_ACTIVITY_PROOF.md` | `4858e2d8b3d41eafab3070277799ebcf5441e3f2a0b86491eb162d0e1f2dba23` |
| `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `docs/special_data_limits.md` | `5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489` |

The central question was whether candidate (5.6) proves positive residual
activation variance at every fixed depth after all actual forward and
adjoint calls, including neighboring-matrix calls, have been retained.
The following derivation checks that question directly.

## 2. Adaptive conditioning across different edges

Let H_n denote the **complete finite transcript before a new batch**:
all revealed roots, all prior vector answers of every matrix, and all
coordinate operations formed from them. Initially the distinct matrices
are independent Gaussian arrays. If their conditional residual factors
are independent at one stage, then:

1. A coordinate operation is H_n-measurable and adds no constraint.
2. At a call to edge ell, its source is H_n-measurable. With H_n fixed,
   the newly returned vector is a linear observation of that one matrix.
3. Conditioning on this observation updates that factor's Gaussian
   conditional law and leaves all other factors unchanged.

Induction proves the product conditional-law assertion, despite the
unconditional dependence of later sources on several matrices. This is
exactly III.F.3's adaptive argument. It would be invalid to condition
only on an edge's initial inputs while ignoring its earlier transpose
answer; the candidate does not do that.

For the selected edge, write all its old forward/transpose constraints as

\[
 W_nX_n=Y_n,\qquad W_n^TU_n=P_n.
\]

Conditional on the complete transcript its residual is

\[
 (I-\Pi_{U_n})\widetilde W_n(I-\Pi_{X_n}),
\]

where the fresh iid N(0,1/n) matrix can be chosen independent of that
transcript in the conditional-law representation. The conditional mean
is the first two terms of candidate (3.1). The compatibility identity
U_n^T Y_n=P_n^T X_n verifies both constraints. The mean lies in the
orthogonal complement of the residual matrix subspace, proving the
Gaussian projection formula.

Calls to the adjacent upper matrix are therefore important but harmless:
they belong to H_n, and the argument above proves that they do not impose
an unrecorded constraint on the selected edge's residual. This is a
conditional independence statement, not an assertion that an initialized
matrix is independent of its own adaptive inputs.

## 3. Exact call audit at depth three and at arbitrary fixed depth

At depth three the candidate's finite program has this order:

| Stage | Matrix observations added |
|---|---|
| Initial forward pass | A2 H1=Z2, then A3 H2=Z3, for all m inputs |
| Backward pass | A3* B3=P2, then A2* B2=P1, for all m inputs |
| New lower forward batch | A2 E1, for all m inputs |
| New upper forward batch | A3 E2, for all m inputs |

Before the A2 E1 batch, P2 and B2 have already been generated. They are
part of the full transcript used to condition A2. Its own constraints
are exactly A2 H1=Z2 and A2* B2=P1. Thus the new A2 innovation is
independent of the old receiving-population tuple (Z2,P2,B2).

Before the A3 E2 batch, E2 has been generated using the A2 batch. Its
source is consequently transcript-measurable. The latest A2 answer
updated only the A2 factor of the conditional matrix law. A3's own
constraints remain exactly A3 H2=Z3 and A3* B3=P2. The new A3 innovation
is independent of the old top tuple (Z3,B3).

The same argument is a literal induction over ell=2,...,L. When the new
edge-ell forward batch is reached:

* The backward pass is complete, so P_ell and B_ell are already known
  in the receiving population when ell<L.
* The new lower batches have produced every source E_(ell-1),a.
* No new forward batch has previously used edge ell. Its old calls are
  precisely X=H_(ell-1), Y=Z_ell, U=B_ell and P=P_(ell-1).
* The unused Gaussian component on that edge remains independent of
  the complete pre-batch transcript by §2 above.

Hence no additional hidden same-edge calls need to be inserted into the
projection used in candidate (5.5).

## 4. Unused variance and independence of the receiving fields

For clarity, condition on the pre-batch transcript and consider one source
v_n=E_(ell-1),a,n. Define

\[
 \alpha_n=(X_n^TX_n)^{-1}X_n^Tv_n,\quad
 v_{\perp,n}=v_n-X_n\alpha_n,\quad
 \rho_n^2=\|v_{\perp,n}\|_2^2/n,
\]
\[
 \beta_n=(U_n^TU_n/n)^{-1}(P_n^Tv_{\perp,n}/n).
\]

The exact conditional answer is

\[
 W_nv_n=Y_n\alpha_n+U_n\beta_n
              +\rho_n(I-\Pi_{U_n})g_n,                    \tag{C1}
\]

in conditional law, with g_n a fresh standard Gaussian vector. The old
forward Gram Q_(ell-1) and reverse-input Gram D_ell are positive definite
by candidate §§2 and 4. Their empirical versions converge by the fixed
finite program theorem and its A.1 extension. Their inverses and the
displayed coefficients therefore converge on events of probability
tending to one. In particular

\[
 \rho_n^2\longrightarrow
 \|E_{\ell-1,a}-\Pi_{H_{\ell-1}}E_{\ell-1,a}\|_2^2.
                                                               \tag{C2}
\]

The left projection in (C1) does **not** remove an order-one fraction of
this variance. Conditional on the transcript,

\[
 E[\|\rho_n\Pi_{U_n}g_n\|_2^2/n\mid H_n]
         =\rho_n^2\operatorname{rank}(U_n)/n
         \le\rho_n^2 m/n\longrightarrow0
\]

in probability. Here rho_n is bounded in probability and m is fixed.
The surviving new scalar innovation therefore has exactly the variance
in (C2). A reverse observation constrains an output subspace of fixed
rank; it does not project v_perp off the reverse-answer span P_n. The
P_n contraction contributes to beta_n instead. This distinction rules
out the plausible but incorrect objection that all backward information
must be subtracted again from the input variance.

To justify **independence**, rather than only the marginal variance,
include the old receiving tuple (Z_ell,B_ell,P_ell when present) in a
bounded Lipschitz empirical test. After removing the negligible
projection, the g_n coordinates are independent conditional on H_n.
The conditional variance of their test average is O(1/n), while its
conditional mean is the old empirical average of the test integrated
against a scalar Gaussian. The old tuple's empirical convergence and
rho_n's deterministic limit identify the new joint law as the old law
times an independent Gaussian, with the displayed conditional-mean
terms restored. The same conditional expansion of second moments proves
joint W2 convergence. This is the argument of III.F.3 following
(III.F.8), applied to the candidate's actual complete transcript.

All m new sources are known before this batch. Their joint unprojected
Gaussian innovation has covariance
E[v_(a,perp) v_(b,perp)], which may be singular. No inverse of this new
covariance is required. The innovation vector is independent of the
**pre-batch** receiving tuple; its components need not be independent
of each other. Candidate §3 explicitly specifies this batch interpretation.
If the batch is sequentialized, later calls require Gaussian regression
on earlier answers in that batch. One may not use the same marginal
variance as a fresh conditional variance after those answers. The proof
of (5.6) conditions only on the pre-batch sigma-field, so it does not
make this forbidden substitution.

Nor does the needed assertion mean independence from the entire canonical
L2 carrier, which contains subsequent generated observations. It is
independence from the stated finite pre-batch local tuple. That is exactly
the sigma-field F_ell in (5.5)–(5.6).

## 5. Positive Grams and the actual noncancellation induction

The input Gram G may be singular. Nevertheless the maintained bounded
ridge-function argument applies to tanh and pairwise nonparallel inputs,
so Q1 is positive definite. Every higher initial forward tuple is a
Gaussian vector with positive definite covariance Q_(ell-1). Full support
and coordinatewise variation make Q_ell positive definite.

For the top backward Gram, p_a=omega_a y_a is nonzero for every a.
The function S(s)=sum_a p_a tanh(s_a) cannot vanish on an open set, because
every partial derivative p_a sech²(s_a) is nonzero. A putative dependence
S(s) sum_a c_a sech²(s_a)=0 therefore makes the second factor vanish
everywhere by continuity. Varying a coordinate forces c_a=0. Thus D_L>0.

The first reverse batch on each lower edge has not been preceded by a
reverse call to that edge. Formula (3.3), justified by the same complete
transcript conditioning, gives a Gaussian Gamma_ell of covariance
D_(ell+1), independent of Z_ell. Since every d_ell,a=sech²(Z_ell,a)>0,

\[
 c^TD_\ell c\ge
 \lambda_{min}(D_{\ell+1})\sum_a c_a^2 E[d_{\ell,a}^2]>0
 \quad(c\ne0).
\]

This verifies every inverse needed in (C1). No condition uniform in the
smallest eigenvalue is claimed or required for fixed-data activity.

At layer one, the coefficient of Gamma_1,a in E_1,a conditional on g
is p_a d_1,a². Its nonvanishing and D2>0 give precisely

\[
 \rho_{1,a}^2\ge
 \lambda_{min}(D_2)p_a^2 E[d_{1,a}^4]>0.                   \tag{C3}
\]

For ell>=2, (C1)–(C2) give candidate (5.5). Both its mean terms and the
learned-matrix term are measurable in the pre-batch local sigma-field
F_ell, which contains Z_ell and B_ell. Its new Gaussian is independent
of that sigma-field. As d_ell,a is also F_ell-measurable,

\[
 \operatorname{Var}(E_{\ell,a}\mid F_\ell)
             =\rho_{\ell-1,a}^2d_{\ell,a}^2.
\]

Every vector in span(H_ell) is F_ell-measurable. Conditional orthogonality
therefore bounds the squared distance to this span below by the expected
conditional variance. Consequently

\[
 \rho_{\ell,a}^2\ge
 \rho_{\ell-1,a}^2 E[d_{\ell,a}^2]>0.                     \tag{C4}
\]

This is candidate (5.6), with all its independence and positivity
hypotheses verified. It genuinely closes the all-fixed-depth induction.
An arbitrary cancellation between the learned-rank term, known forward
mean and known backward response cannot cancel an independent positive-
variance component. The gate is strictly positive at every finite tanh
preactivation, so it cannot kill that variance either.

## 6. Remaining checks and verdict limits

The normalized derivative expansions in candidate §6 use the unhalved
weighted loss correctly: c(t)/t->2S, Delta_ell(t)/t->2B_ell, raw hidden
parameter velocities divided by t tend to four times their coefficients,
and integration gives the factor two in hidden displacements. The
bounded-multiplier strong chain rule suffices. The finite sums of
continuous rank-one factors are HS-valued, even though initialized
actions are not HS. No ambient L2 Frechet derivative or Taylor analyticity
is needed. Equations (C3)–(C4) prove nonzero activation coefficients
directly, so activation motion is not inferred solely from preactivation
motion. Finite Lm then supplies one positive common activity interval for
the fixed dataset.

The nonaffinity argument in §7 is also valid: each initial marginal is
a nondegenerate Gaussian; tanh cannot equal an affine function on its
full support; and L2 continuity transfers its positive affine-fit error
and variance to a sufficiently small common interval.

| Adversarial issue | Disposition |
|---|---|
| Neighboring matrix calls secretly condition the selected edge's residual | Ruled out by full-transcript conditional product induction |
| Previous adjoint answers eliminate the positive new forward variance | Ruled out by (C1)–(C2); only an output rank-m projection is removed |
| New lower-edge innovation correlates with the old upper-edge backward field | Ruled out by the conditional empirical-law argument retaining that field in the old tuple |
| Later inputs in one batch are incorrectly treated as independent fresh calls | Candidate uses a joint batch and conditions (5.6) on its pre-batch field; no such substitution |
| Singular original input Gram invalidates the inverses | Q and D, not G, are inverted; their strict positivity is proved |
| Positive aggregate energy is substituted for per-input activation motion | No; (C3)–(C4) prove positive residual for every input and every layer |
| Fixed-program scope is enlarged to growing depth, data or transcript | No; all are fixed in this onset proof |

There are no blocking findings within this scoped candidate. The batch
and pre-batch meaning of the independence statements must be retained
verbatim in substance when synthesizing the result; strengthening them
to independence from earlier outputs in the same batch, all future
observables, or the whole canonical carrier would be false and is not
needed.

This PASS does not prove broad-law existence, actual-network capture,
nonlazy open Borel-law families, a determining closure, numerical
realization, substantial training, or promotion eligibility. It confirms
the frozen candidate's finite-data every-layer onset activity and
nonaffinity argument conditional on the maintained C.1 local flow.
