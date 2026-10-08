# Audit of the finite causal Gaussian response law

Verdict: **PASS for the stated finite-program equivalence.** I found no
correctness defect requiring a revision of the frozen candidate. The
expected-derivative rule is proved equivalent to the complete finite
chronological regression program; it is not merely a formal response
expansion. In particular, the singular-history argument identifies actual
response fields even when individual derivative coefficients depend on an
off-support extension.

This verdict does not cover an increasing-history limit, continuous time,
finite autonomous memory, width rates, numerical stability, or all-time
approximation. None of those conclusions is needed for the theorem audited
here.

## 1. Assignment, read coverage, and independence

The assignment was to audit the inverse-Gram-free formulation, uncentered
primitive covariances, frozen-coefficient total derivatives, all-history
pseudoinverse equivalence, singular integration by parts, layer causality,
and possible missing feedback. I read every line of the following inputs:

| Input | Coverage | SHA256 |
|---|---:|---|
| `RESPONSE_GAUSSIAN_CLOSURE.md` | 352 lines, complete | `2da1253b43750e6d641e26298dee3ba9acd74527d97651bb1c180013a61ea73c` |
| `UNCLIPPED_FINITE_HISTORY.md` | 258 lines, complete | `9d842305cf984f2f5841466faf878e99f8f40815cebbc9f5ec341f9642b9ee81` |
| `FINITE_RESPONSE_MEMORY.md` | 322 lines, complete | `edf19fb88cc1d3b719b3668c575aa6a1316fa30b2c822d277fc84e7428b34c91` |

The candidate hash agrees with the supervisor's frozen assignment. Required
canonical-notation, rigorous-proof, and research-audit instructions were
already read and applied. No other scientific file, prior audit, external
source, numerical experiment, or Git history was consulted for this audit.
All three scientific input hashes were rechecked after the audit and were
unchanged.
The supplied files mention earlier audits and additional sources; those
reports were not opened and their verdicts were not used as evidence.

The reviewer did not author this candidate or the two permitted dependencies.
The reviewer has authored other scoped notes in this study, so this is a
scoped internal audit, not a fresh-context promotion-review certificate.
Only this assigned report was written; the frozen candidate was not edited.

## 2. The exact claim and its boundaries

At each matrix interface, let \(H_t\) be a forward query input in the lower
population and \(D_s\) a reverse query input in the upper population. Let
\(g_t,x_s\) be their respective matrix answers. The proposed law introduces
centered primitive Gaussian families with

\[
\mathbb E[\eta_t\eta_u]=\mathbb E[H_tH_u],\qquad
\mathbb E[\xi_s\xi_r]=\mathbb E[D_sD_r],
\]

and defines

\[
g_t=\eta_t+\sum_{s<t}D_s
\mathbb E[\partial_{\xi_s}H_t],\qquad
x_s=\xi_s+\sum_{t<s}H_t
\mathbb E[\partial_{\eta_t}D_s].
\]

The inequalities refer to the fixed instruction order, not to physical
training time. The derivatives are total derivatives through the local scalar
circuit, with all deterministic population coefficients held fixed. They are
neither direct answer derivatives nor derivatives of whitening variables.

The proved claim is equality with the retained-regression scalar law at every
event and hence throughout the complete fixed program. Its transfer to the
actual neural fixed-program limit uses the supplied unclipped theorem. The
candidate's later reference to quantitative conditions in
`FIXED_HISTORY_RATE.md` is a conditional pointer outside the permitted inputs;
this audit does not independently validate that rate theorem.

The candidate explicitly restricts its circuit class to distinct neuron
populations with no cross-population coordinate identification, \(C^1\)
row operations, and independent primitive/root families with arbitrary
within-family Gaussian covariance. Those restrictions suffice for the proof
and cover the stated canonical neural program. The theorem should not be
read as including arbitrary self-connected or coordinate-identifying
programs without a separate argument.

## 3. Checks of the equivalence proof

The finite-width conditioning identity in the permitted dependency has the
correct orientation and normalization. Its affine mean satisfies both
\(GH=F\) and \(G^\top D=B\), using \(D^\top F=B^\top H\); its
homogeneous Gaussian component is
\((I-P_D)\widehat G(I-P_H)\). Applying it to a new input gives the stated
cross-direction term and a projected innovation with variance
\(\|u_\perp\|^2/n\). Predictable adaptive queries add linear observations
of this remainder and do not reveal additional unobserved entries. This
justifies the regression law used by the candidate.

The all-query extension is valid at singular histories. Each omitted input
and its answer are the same deterministic combination of retained inputs
and answers. The full-to-retained matrices include identity rows and hence
have full column rank. The identity

\[
T^\top(TQT^\top)^\dagger T=Q^{-1},\qquad Q>0,
\]

follows by writing \(TQ^{1/2}\) and evaluating its singular-vector
decomposition. It preserves both same-direction projection and the
cross-direction regression term. Zero innovation returns the same answer
combination. No continuity of the pseudoinverse at rank changes is needed:
this is an equality at fixed deterministic population Grams.

The decisive cancellation in Section 6 is also correct. For a forward query,
write previous answers as

\[
F=\eta+R_HD,\qquad B=\xi+SH,
\]

with zeros in entries forbidden by chronology. For the projection residual
\(e=h-H^\top a\), one has \(\mathbb E[He]=0\), including for singular
\(Q_H=\mathbb E[HH^\top]\). Indeed, a null combination of \(H\) vanishes
almost surely, so \(\mathbb E[Hh]\) lies in the range of \(Q_H\).
Consequently

\[
\mathbb E[Be]
=\mathbb E[\xi e]
=Q_D\bigl(r-R_H^\top a\bigr),\qquad
r_s=\mathbb E[\partial_{\xi_s}h].
\]

The second equality is Gaussian integration by parts with every deterministic
coefficient frozen. The matrix \(Q_D\) is the covariance of \(\xi\) and
the **uncentered** Gram of \(D\). If \(v\in\ker Q_D\), then
\(\mathbb E(D^\top v)^2=v^\top Q_Dv=0\), so multiplication by \(D\)
removes the pseudoinverse range projection. Therefore

\[
D^\top Q_D^\dagger\mathbb E[Be]
=D^\top(r-R_H^\top a).
\]

This cancels the previous-response contribution in \(F^\top a\). The
remaining Gaussian part \(\eta^\top a+\sigma Z\) has covariance
\(\mathbb E[H_uh]\) with earlier forward primitives and variance
\(\mathbb E[h^2]\). The resulting answer is exactly the proposed one.
The reverse calculation has the same cancellation with the populations
exchanged. Event induction therefore identifies actual row functions under a
common Gaussian construction, not only their first few moments.

The covariance extension is causal: every new input is available before its
answer, so the new covariance row is already determined. It extends a Gram
matrix of known \(L^2\) fields and is positive semidefinite. Appending its
Gaussian coordinate preserves all preceding marginal laws. Other primitive
families remain independent because the covariance coefficients are
deterministic. Operations at neighboring interfaces may depend on several
primitive families in one population; the prescribed total derivative passes
through those already-built local circuits. No forward/reverse sweep requires
a future primitive or an unknown future coefficient.

## 4. Singular support and coefficient freezing

The singular integration-by-parts proof is complete: write the primitive
vector as \(\xi=AU\), with independent standard Gaussian coordinates in
\(U\), apply one-dimensional integration by parts, and multiply by \(A\).
Polynomial growth gives integrability and vanishing boundary terms. This
requires no inverse covariance and also permits singular independent root
families in the remaining arguments.

If two admissible circuit extensions agree almost surely, integration by
parts gives

\[
Q_D\,\mathbb E[\nabla_\xi(F_1-F_2)]=0.
\]

The expected-gradient difference is therefore killed by the actual query
vector \(D\). This proves invariance of the answer, rather than an
unsupported assertion that the individual derivatives are intrinsic. The
induction remains valid after earlier extensions are changed: preceding field
values, moments, and primitive covariance extensions are unchanged under the
common coupling. Causality and the stated smooth-growth requirements exclude
extensions that introduce future variables or nonintegrable derivatives.

Freezing deterministic population coefficients does not ignore a feedback
term in this equivalence. These values are recomputed by the program at the
appropriate chronological events, and both laws use the same values. During
the local integration-by-parts identity they are constants. Differentiating
their population-defining expectations instead would change the meaning of
the probe and would no longer prove the required regression identity.

The growth claim is adequate for the stated neural operations. A globally
Lipschitz activation has at most linear growth; a bounded gate times a field
preserves a linear field-value envelope. A derivative of that product adds a
field factor, but finite repeated chain rules produce only polynomial
Gaussian growth. Bounded strip derivatives provide the needed real-line
bounds on both \(\phi'\) and \(\phi''\). Thus the expected responses exist
and differentiation under expectation is justified at every fixed stage.

## 5. Explicit adversarial program checks

The following checks were done algebraically against the regression rule.
They are finite query programs, not numerical experiments.

### Nonzero means and a population coefficient

Take a constant lower input \(H=1\), so its first answer is
\(g=\eta\), \(\mathbb E\eta^2=1\). Compute a population coefficient
\(a=\mathbb E(1+g)=1\), and reverse-query
\(D=a(1+g)=1+\eta\). The response rule gives

\[
\mathbb E[\partial_\eta D]=1,\qquad
x=\xi+1,\qquad \mathbb E\xi^2=\mathbb E D^2=2.
\]

The regression rule gives exactly the same result because
\(\mathbb E[gD]=1\). Centering the query Gram would incorrectly replace
the backward primitive variance by \(1\); centering the constant forward
input would eliminate its primitive altogether. Differentiating the defining
coefficient \(a\) under a population-wide primitive shift would instead
give expected derivative \(2\), also incorrect. The candidate avoids both
errors.

### Repeated Gaussian coordinates and a null derivative

Send the same forward input twice, \(H_1=H_2=X\), where \(X\) is standard
Gaussian. Then \(\eta_2=\eta_1\) almost surely. Reverse-query the formally
nonzero expression \(D=\eta_2-\eta_1\), whose value is zero. Its formal
derivative vector is \((-1,1)\), while its primitive variance is zero.
The response answer is

\[
x=-H_1+H_2=0.
\]

Replacing the query's off-support extension by the identically zero function
changes that derivative vector to zero and leaves the answer unchanged.
This directly tests the candidate's null-space interpretation.

### Two forward/reverse rounds with indirect response

Start with \(H_1=X\), a standard Gaussian lower root. Successively query

\[
g_1=G H_1,\quad D_1=g_1,\quad x_1=G^\top D_1,
\quad H_2=x_1,\quad g_2=G H_2,\quad D_2=g_2,
\quad x_2=G^\top D_2.
\]

The candidate gives

\[
g_1=\eta_1,\quad x_1=\xi_1+X,\quad
g_2=\eta_2+\eta_1,\quad
x_2=\xi_2+X+H_2,
\]

where
\(\operatorname{Var}\eta_1=\operatorname{Var}\xi_1=1\),
\(\operatorname{Cov}(\eta_2,\eta_1)=1\),
\(\operatorname{Var}\eta_2=2\),
\(\operatorname{Cov}(\xi_2,\xi_1)=2\), and
\(\operatorname{Var}\xi_2=5\). Hence one can write
\(\xi_2=2\xi_1+Z\), with \(Z\) a fresh independent standard Gaussian,
and obtain

\[
x_2=3\xi_1+2X+Z,\qquad
\mathbb E[Xx_2]=2,\qquad \mathbb E[x_2^2]=14.
\]

For a direct regression check, the old forward-input Gram is
\(\left(\begin{smallmatrix}1&1\\1&2\end{smallmatrix}\right)\).
The reverse input \(D_2\) projects onto \(D_1\) with coefficient \(2\),
and its remaining forward-history correction has coefficients \((-1,1)\).
Its fresh variance is \(1\). The resulting answer is
\(2x_1-H_1+H_2+Z=3\xi_1+2X+Z\), exactly as above.
Using only a direct derivative with respect to the latest answer would miss
the extra \(H_1\) term. Treating colored primitives as independent fresh
fields would also fail this test. The candidate's total derivatives and
within-family covariance both pass.

## 6. Final assessment

There are no outstanding material objections to the frozen finite-law
equivalence. The proof properly handles redundant inputs, zero innovations,
nonzero query means, singular roots and covariance, cross-interface local
dependence, and indirect response through earlier answers.

The inverse-free description is mathematical: evaluating its Gaussian
expectations or sampling singular colored families efficiently remains a
separate computational question. The construction retains the finite local
circuits and histories as well as covariance and derivative arrays; it is
not a covariance-only Markov model. The candidate states these limitations
and does not convert finite-program equivalence into a continuum or all-time
claim. No correction to the audited candidate is required for the scoped
verdict above.
