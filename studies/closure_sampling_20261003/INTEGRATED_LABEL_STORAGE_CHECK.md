# Reconstruction of the label-sensitive time radius and storage count

2026-10-04. **PASS within the inherited local insertion, source-selection,
and corrected-readout interfaces.** The new time radius is admissible for
each fixed positive label RMS, its source coefficient is proportional to
the square of the label activity, and its squared storage coefficient has
the displayed fourth power. The retained exact sources, dense metrics,
moving mixers, and sample solve arrays still have quadratic sample
capacity. This is an internal reconstruction, not a promotion review or
a fresh proof of the inherited cavity theorem.

Checked complete candidate: `INTEGRATED_LABEL_STORAGE_ROUTE.md`, 618 lines,
SHA-256 `c6aca596d0248ca709286fff16abf65ce1e204cc0515162377324564a4be2ae9`.
The supplied scientific input boundary was respected. The supervisor
subsequently authorized the two same-study inventory files listed below.
Only this check was written; no source, README, maintained file, or Git
state was changed. Canonical notation, its neural-network reference, and
the rigorous-mathematics skill were applied.

The main analytic clarification is that contractivity applies on the real
solution. Route the contour along the real axis before taking its vertical
piece. No contractivity of an algebraic complex Gram is asserted. This
clarification changes no radius, hypothesis, count, or coefficient.

## 1. Fixed model and activity dependence

The dense network is the candidate's width-\(n\) ordinary-tanh network,
with readout \(f_n=w^\top h^{(L)}/n\), zero initial readout, Gaussian
initialization, mean squared loss, and physical mobilities
\((n,1,\ldots,1,n)\). For residuals \(r_a=f_n(v_a)-y_a\), set
\[
Y=\|y\|_2/\sqrt m>0,\qquad
\lambda=\gamma/m,\qquad u=Y/\lambda,\qquad S=16u,\qquad
\ell_n=\log(en),\qquad T=32\lambda^{-1}\ell_n.
\]
Here \(\gamma\) is the least eigenvalue of the unnormalized limiting
top-feature sample Gram. Its diagonal is at most one, so
\(0<\lambda\le1\). The complete stated label condition supplies
\(S\le1\), the source budget requirements, and the runtime smallness
conditions. No lower bound on an individual label or on its sign is used.
Zero labels are correctly handled separately by the stationary zero
predictor.

The endpoint calculation in `EXPLICIT_SOURCE_CONSTANTS_ROUTE.md`,
Section 4, gives four deterministic forward-response contributions
\[
sK_{\rm src}S\sqrt{\ell_n}
 \{B^2,\ f_{j-1}^2,\ S T_Q,\ S^2Bq_{j-1}\}.
\]
Its centered Gaussian contribution is
\(G_dSq_{j-1}\sqrt{\ell_n}\). Dividing by
\(S\sqrt{\ell_n}\) gives exactly candidate (10)'s \(U_j(S)\),
including its strict remainder allowance. Each angular correction has
one activity integral and one training carrier, hence two factors of
\(S\). This gives the stated \(V_j(S)\). The trace constants do not
divide by \(S\); no inverse activity has been lost. The refined tanh
constants and the first-layer and spherical-query substitutions agree
with the complete activation route and its corrected check.

Thus the inherited stopped endpoint proof supplies
\[
\max|R_a^{(j)}|\le U(S)S\sqrt{\ell_n},\qquad
\max|J^{(j)}|\le V(S)\sqrt{\ell_n}.
\]
The first object is the residual-free parameter response, and the second
is the derivative along a complex great circle. They are not physical
velocities. The physical velocity is obtained by multiplying the first
response by \(-2r_a/m\) and summing over training samples.

## 2. The uncapped coefficient and the complex-domain check

Put
\[
c_t=\frac{a}{64YSU(S)},\qquad
c_q=\min\{1/8,a/[8V(S)]\},\qquad
r_t=c_t/\sqrt{\ell_n},\quad r_q=c_q/\sqrt{\ell_n}.
\]
For fixed admissible data and \(Y>0\), all coefficients are finite and
\(r_t\to0\). Smallness of the actual width, rather than a separate
upper bound on \(c_t\), is what the following estimates require.

To check the normalization in the residual and variational equations,
let \(G\) be the matrix whose sample columns are
\(\nabla_\Theta(nf_n(v_a))\), where
\(\Theta=(A,\sqrt nW^{(2)},\ldots,\sqrt nW^{(L)},w)\).
The readout, first-matrix, and hidden-matrix blocks of each column have
Euclidean norms at most
\[
\sqrt n B,\qquad \sqrt n St_1,\qquad
\sqrt n SBt_j\quad(2\le j\le L).
\]
Consequently, even for complex parameters,
\[
\frac{\|G^\top G\|_{\rm op}}{mn},\quad
\frac{\|GG^\top\|_{\rm op}}{mn}
\le\frac{\|G\|_F^2}{mn}
\le\mathcal K
=B^2+S^2\left[t_1^2+B^2\sum_{j=2}^Lt_j^2\right].
\]
The transpose is algebraic. Positivity of these complex matrices is
neither needed nor assumed. The residual equation is
\(\dot r=-2G^\top G r/(mn)\), while the negative-Gram part of the
parameter variational equation is \(-2GG^\top/(mn)\). This proves
the same norm-growth bound \(2\mathcal K\) for both.

For a complex time \(z\) in the candidate rectangle, let
\(t_0=\min(T,\max(0,\operatorname{Re}z))\). Follow the real
trajectory from zero to \(t_0\), then the real horizontal extension
to \(\operatorname{Re}z\), then the vertical segment to \(z\).
The last two lengths sum to at most \(2r_t\). All long positive-real
segments are on the real solution and have a positive semidefinite
Gram, so their base propagator is contractive. Any backward real piece
and every complex piece are among the last two short segments. Their
combined norm cost is therefore at most
\(e^{4\mathcal K r_t}\). This proves the claimed absence of an
\(e^{\mathcal KT}\) factor. A horizontal path at nonzero imaginary
time would not have this justification and is unnecessary.

Candidate (14) gives
\[
r_t\le1/8,\qquad 4\mathcal Kr_t\le\log2,
\]
so the short-contour residual RMS is at most \(2Y\). Its additional
absolute activity is at most \(8Yr_t\le8Y/\lambda=S/2\).
The inherited real activity is at most \(S/2\), giving total activity
at most \(S\). It follows that \(\|w\|_\infty\le BS\), and
bounded gates and mixers give the backward RMS bounds used above.
These estimates can first be imposed as stops and then improved; at
sufficiently larger width their numerical margins are strict.

Direct integration gives short-contour increments
\[
\|\Delta W^{(j)}\|_{\rm op}\le8BYS t_*r_t\le1/8,\qquad
\|\Delta A\|_{\rm op}/\sqrt n\le8YS t_1r_t\le1/4.
\]
Hence the real caps \(15/4\) and \(5/2\) remain strictly inside
the complex caps four and three. Cauchy--Schwarz in the sample index
gives \(|\partial_tz_i^{(j)}|\le4YSU(S)\sqrt{\ell_n}\), and
the two short time pieces followed by the query segment give
\[
8c_tYSU(S)+c_qV(S)\le a/8+a/8=a/4.
\]
The full-system pole stop \(3a/8\), cavity stop \(7a/16\), and
derivative-strip boundary \(a/2\) have the required fixed separations.
Coordinate-small cavity transfer and the augmented Taylor segments use
these separations without evaluating sharper tanh derivatives outside
their certified strip. The bound \(a/4\) improves the full stop.

The strongest elementary width cost is retained correctly:
\[
\ell_n\ge64c_t^2
=\frac{a^2}{64Y^2S^2U(S)^2}
=\frac{a^2\lambda^2}{16384Y^4U(S)^2}.
\]
Thus this argument is not uniform as \(Y\downarrow0\). A large
coefficient \(c_t\) cannot be used at an unchanged moderate width.

## 3. The complex Gaussian correction still vanishes

The normalized counting-norm interpolation in the label route is valid
with the retained coefficients. For \(p\ge4\), use the carrier
\(p\)-norm budget and interpolate the time velocity between its RMS
bound \(2\rho_nSr_j\) and coordinate bound
\(2\rho_nSU_j(S)\sqrt{\ell_n}\). With
\(N_* =\max_j(r_j,U_j(S))\), this gives
\[
\|k\odot\dot z\|_{2,n}
\le\frac{2\rho_nS^2N_*}{\eta}
             p(2\mathcal B\ell_n)^{1/p}.
\]
For \(\ell_n\ge\max(e^2,2\mathcal B)\), the choice
\(p=\max(4,\log(2\mathcal B\ell_n))\) satisfies
\(p\le2\log(e+\ell_n)\) and
\((2\mathcal B\ell_n)^{1/p}\le e\). Differentiating the actual
backward recursion gives the terminal contribution \(2sB\rho_n\),
changed-mixer contribution
\(2Bs^3K_{j+1}^2\rho_nS^2\), and changed-gate contribution just
bounded. These are exactly the terms of candidate (18), yielding (19).

The contour length and residual bound then give
\[
\frac{\|\delta(z)-\delta(t_0)\|_{2,n}}S
\le\frac{4Y}{S}r_tJ_*^{\rm time}
 [1+(S^2/\eta)\log(e+\ell_n)]
=D_n.
\]
Here \(4Y/S=\lambda/4\); the candidate retains this factor
correctly. Differentiating with respect to the real and imaginary time
coordinates gives Lipschitz constants at most fixed multiples of
\(\lambda J_*^{\rm time}[1+(S^2/\eta)\log(e+\ell_n)]\).
The projection defining \(t_0\) is 1-Lipschitz, so its two endpoint
corners do not spoil this bound.

For completeness, condition on the autonomous cavity initialization and
pair the correction with its independent Gaussian root. Its canonical
increment distance is bounded by the stated Euclidean distance. A
Euclidean mesh at Gaussian distance \(2^{-k}D_n\) has at most a
fixed power of \(\ell_n\), multiplied by \(2^{2k}\), points.
The elementary Gaussian tail and union bound therefore bound the mean
of its dyadic increments by a constant times
\[
\sum_{k\ge0}2^{-k}D_n\sqrt{\log(C\ell_n^C)+k}
\le C D_n\sqrt{\log(C\ell_n^C/D_n)},
\]
after increasing a fixed constant. The same tail allocation gives a
sub-Gaussian tail scale \(CD_n\). At fixed parameters these scales are
respectively
\[
O\!\left(\frac{[\log(e+\ell_n)]^{3/2}}{\sqrt{\ell_n}}\right),
\qquad
O\!\left(\frac{\log(e+\ell_n)}{\sqrt{\ell_n}}\right),
\]
and tend to zero. Integrating that tail proves that every fixed
exponential moment needed for budget removal tends to one. The constants
may depend badly on the fixed positive \(Y\); the convergence assertion
does not conceal a uniform-in-label estimate.

Because (14) restores a bounded-width rectangle and \(T\le n\)
eventually, the existing spherical net exponent and strict insertion
remainder powers are unchanged. The stopped local interface, followed
in its stated order, therefore supplies holomorphy near the closed time
rectangle times the intrinsic sphere tube. This is a verification of the
new domain under that interface, not an independent proof of its original
Gaussian insertion estimates.

## 4. Exact count, thresholds, and the fourth label power

The four source families have magnitude at most
\(M_0\sqrt n\), with \(M_0=8\max(B,\max_jt_j)\): bounded
activations control forward sources, the initial mixer norm controls
their images, and \(S\le1\) controls backward sources and their
initial transpose images. The passive query contributes no new force.

Set \(\alpha=r_t/(4T)\). For \(\alpha\le1\), the substitution
\(t=T(1+\cos\theta)/2\) stays in the proved rectangle when
\(|\operatorname{Im}\theta|\le\alpha\): its vertical magnitude
is at most \(T\sinh\alpha/2\le T\alpha=r_t/4\), and its
horizontal excess is smaller still. Thus the inherited Fourier and
spherical projection estimates apply jointly with the new radii.

The tail cutoff and exact lattice count in candidate (21) agree with
the complete spherical theorem. In particular degree zero is retained.
Bounding the harmonic multiplicity by
\(2\binom{j+d-2}{d-2}\) and placing disjoint unit cubes at the
nonnegative weighted lattice points gives
\[
N\le\frac{2[H+\alpha+(d-1)r_q]^d}
             {d!\alpha r_q^{d-1}}.
\]
The enlargement \(\alpha+(d-1)r_q\) is necessary and is retained.
The exact tail logarithm is
\[
H=3\log n+2\log C_d^*+2(d+1)\log\ell_n.
\]
All four conditions in (23) then give \(H\le7\ell_n\) and
\(H+\alpha+(d-1)r_q\le9\ell_n\). Therefore
\[
4N\le\frac{1024\,9^d}{d!}
 \lambda^{-1}c_t^{-1}c_q^{-(d-1)}\ell_n^{3d/2+1}.
\]
The critical substitution is exactly
\[
\lambda^{-1}c_t^{-1}
=\frac{64YSU(S)}{a\lambda}
=\frac{1024U(S)}a\left(\frac Y\lambda\right)^2.
\]
It produces \(2^{20}\) in (6), activity power two in source rank,
and logarithmic power \(3d/2+1\). Squaring gives activity power
four and logarithmic power \(3d+2\), as in (29). Neither inverse
radius was transferred into a width threshold. The threshold handles
only the displayed tail logarithm and lattice rounding, in addition to
the explicitly separate analytic requirements.

For \(d=1\), the two sphere points require eight time families.
The inherited time-only estimate
\(p+1\le514\lambda^{-1}c_t^{-1}\ell_n^{5/2}\) gives exactly
(26), including its factor eight. Its usual eventual logarithmic
requirements remain part of the inherited time-only approximation
threshold; this is not a finite-width assertion without those conditions.

Finite initial-jet continuation remains applicable to every positive
actual radius. Identical scalar continuation and quadrature operations
preserve the initialized image-pair identities exactly, while each member
has its own coordinate error \(n^{-1}\). All original-width source
vectors and temporary approximation coefficients are discarded. Thus the
runtime receives precisely the same interface, with its carrier constant,
exact initialized additions, tolerance, and horizon unchanged. Candidate
(8)'s runtime coefficient is inherited unchanged; it is not rederived by
the new radius argument.

## 5. Retained inventory and the sample-rank obstruction

Write \(\bar R=A_n(Y)+2m+d+1\). This is an upper bound on every
source rank and is at least \(m,d,1\), independently of any claim
about the numerical size of the leading term. The existing selection
construction has \(N_j\le9\bar R\) selected neurons. Its actual
retained arrays include:

| Category | Coordinate count before the common upper bound |
| --- | --- |
| Moving first matrix | \(dN_1\) |
| Moving hidden mixers | \(\sum_{j=2}^L N_jN_{j-1}\) |
| Moving raw readout and internal residual | \(N_L+m\) |
| Fixed neuron metrics, inverses/copies, and any retained mixer copies | A fixed number of \(N_j^2\) and \(N_jN_{j-1}\) arrays |
| Current training features and backward fields | A fixed number of \(mN_j\) arrays per layer |
| Feature Gram, residual Gram, and solve caches | A fixed number of \(m^2\) arrays |
| Training inputs and labels | \(m(d+1)\) |

The authorized architecture inventory gives the conservative total
\(1020(L+1)\bar R^2+10m(d+1)\), including its fixed array-copy
allowance. The source improvement does not introduce an additional
retained evaluator or table. Applying
\((A_n+2m+d+1)^2\le2A_n^2+2(2m+d+1)^2\) proves (7).
Thus the separate quadratic initialized-source term in (29) remains;
the cross term has been bounded, not omitted.

The corrected readout uses
\(Q_C=F_C^\top H_LF_C\succ0\), with
\(F_C\in\mathbb R^{N_L\times m}\) and \(H_L\succ0\).
For any vector \(b\),
\(b^\top Q_Cb=\|H_L^{1/2}F_Cb\|_2^2\). Positivity therefore
forces \(\operatorname{rank}F_C=m\), hence \(N_L\ge m\).
An operator perturbation of the initialized Gram smaller than half its
positive gap preserves that conclusion. Dense storage of the top metric
alone then occupies at least \(m^2\) coordinates in this implementation;
its sample solve arrays also have \(m^2\) entries. Removing a solve
cache, or merely omitting the explicit training-source additions, cannot
by itself turn the stated inventory into a linear-sample inventory.
This is a property of the specified dense-array representation, not a
lower bound on all possible encodings or autonomous constructions.

At fixed \(u,L,d\), the leading coefficient has no separate inverse
gap or sample factor. At fixed unscaled \(Y\), (29) visibly contains
\(Y^4m^4/\gamma^4\), as well as the explicit functions of
\(16Ym/\gamma\); admissibility still restricts such variations.
The existing and new sufficient bounds may both be retained, with their
own thresholds. No uniform finite-width superiority follows.

## 6. Limits and exact input coverage

The real integrated-velocity estimate (28) follows by integrating the
actual response bound against \(2\rho_n\). It does not provide a
nonuniform complex approximation theorem. The compact-clock example is
correct: \(e^{-\mu t}=(1-\tau)^{4\mu/\lambda}\) fails to be
analytic at \(\tau=1\) for a positive noninteger exponent. The
candidate correctly leaves a further logarithmic improvement open.

Ordinary tanh supplies a uniform activation value bound \(B\), used
in the Gram, readout, backward, endpoint, and source-magnitude estimates.
Bounded strip derivatives alone do not replace that hypothesis. No
unbounded-activation extension, new folding label range, population
variance theorem, or uniform shrinking-label theorem is certified here.
The folding composition is an expressly inherited optional interface,
not needed for (5)--(29); its separate error and projection storage have
not been independently audited in this scoped check.

No missing scientific input blocks the new radius/count implication.
The old local insertion/source-selection theorems and runtime comparison
remain inherited premises, with an unquantified stochastic width
threshold. The following records all substantive file reading; section
headings and matching keywords were also searched in these allowed files
to locate the listed passages. No linked dependency outside this list
was opened.

| Input | Read coverage | SHA-256 |
| --- | --- | --- |
| INTEGRATED_LABEL_STORAGE_ROUTE.md | Complete, lines 1--618 | c6aca596d0248ca709286fff16abf65ce1e204cc0515162377324564a4be2ae9 |
| ACTIVATION_CONSTANTS_REFINEMENT_ROUTE.md | Complete, lines 1--691, including evaluator | 407f0b1079c7f65dd09960bc45c78a4f266c30054585c9aa9df8b7ab61859660 |
| ACTIVATION_CONSTANTS_REFINEMENT_CHECK.md | Complete, lines 1--443, including corrected arithmetic | 40b18c9c05a3b657753d30bad4e1b57ff1f813d47b764fca66366c13369b73e6 |
| EXPLICIT_SOURCE_CONSTANTS_ROUTE.md | Lines 247--357 and 591--654 | d4a1bf4bd247d1b93909d4ee001da74c4c6f4573021370800f9c152dae05ab6a |
| LABEL_DEPTH_RESCALING_ROUTE.md | Lines 116--193 and 400--568 | d06ceea6598bf3f86e0843682c5600365ef01b4b80eaad6544ceec1a9d4ec1f1 |
| SPHERICAL_SOURCE_DIMENSION_ROUTE.md | Complete, lines 1--662 | bba804ec958860eff8eceaeda212a1e6bf391fb82c5b0e0224bfe870d98728a8 |
| SPHERICAL_SOURCE_DIMENSION_CHECK.md | Complete, lines 1--198 | c76f413669bb974fb762d730a2d2162d6fcac08b2708a294c275a229784d3df6 |
| RUNTIME_SMALL_ACTIVITY_CONSTANT_ROUTE.md | Complete, lines 1--501 | 061d46972a7b026bd6b6b5176fc411214e82bd1e9d9e18ec5bd8e119fedbeaa2 |
| ARCHITECTURE_CONSTANT_REFINEMENT.md | Lines 315--344 | b33f8b2ebb04eba386f59f125fd4d8f22ff3273bc094f64808db865dd27caba7 |
| STORAGE_QUADRATIC_IMPROVEMENT.md | Lines 104--338 and 571--675 | ec18f54a3e3977bf9c99ce5c26066f48688848f8b5a9c142b75424badeb025e2 |

Verification consisted of mathematical reconstruction and file/hash
checks. No training experiment, numerical evidence for a stochastic
claim, external literature retrieval, or formal proof assistant was used.
