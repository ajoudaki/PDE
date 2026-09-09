# Isolated probability audit of the positive-time middle-curvature argument

## Identification, scope, and verdict

Candidate: `/tmp/l3-two-sample-proof-DLuelg/POSITIVE_TIME_MIDDLE_CURVATURE.md`.

Exact SHA256 verified before the audit:

`0b2999b92442dbbd1f43faff3202eb79a62453271b43f2d10a90e263fa34b78d`

Date: 2026-09-06. Line references below refer to this exact candidate. The candidate was not edited. It was the only mathematical source read. No named dependency, project file, history, ledger, or previous review was read. No experiment or external specialized theorem was used.

**Primary verdict: premise-conditional PASS for the new Gaussian lower-tail implication in Sections 3–6.** Under the Section 1 finite-program, initialization, raw-flow, and local-convergence hypotheses, interpreted with the centered Gaussian source laws used in the proof, the argument establishes

\[
\mathbb P\{Z^{(2)}_a(S)\in I,\ \sigma q^{(2)}_a(S)>R\}
\ge c_I\exp[-C_I(R+1)^2],\qquad R\ge1,
\]

for every fixed sufficiently small positive (S), both samples, both signs, and every interval with nonempty interior. In particular this holds for a fixed compact interval of positive length. The constants can be chosen independently of the sufficiently large common cap and the subsequently sufficiently fine mesh. Singular time/sample covariance matrices cause no failure. No counterexample satisfying these hypotheses was found; the derivation below establishes the implication directly.

This is **not** certification of the imported finite Gaussian program, independence of its two source groups, its response bounds, its relationship to a trained network, or its local convergence. It is not a full-model, finite-width, or global-theorem PASS.

The bounded-direction curvature conclusion is also supported by an elementary calculation, detailed below. There are secondary repairs to make in presenting the remainder estimate and the reliance on sample symmetry. Unique restartability, asserted at lines 135–136 and referenced again at lines 430–432, is not supplied by the explicit local-existence/convergence premises and is not certified here.

## 1. Exact hypothesis use and quantifiers

Write (Q) for the cutoff cap and (R\ge1) for the tail threshold; the candidate uses (R) for both. Fix (T=3/2). The relevant assumptions are:

- The raw equations and actual adjoints in Section 1, bounded initial hidden operators, bounded features and gates, and zero initial readout.
- A finite causal program (2) with deterministic coefficients, 
  \(|A_{ka,rb}|\le(3/4)\Delta\) and \(\sum_{r\le k,b}|B_{ka,rb}|\le1\).
- Independent complete centered Gaussian groups \(\xi\) and \(\zeta\), with the full covariance rules (4). Neither group need have nonsingular covariance.
- Fixed-cap Euler convergence including the named joint second moments, followed by strong cut removal for the named fields and queries.
- For the upper tail only, the explicitly imported exponential moment of the uncut terminal query.

The claimed uniformity has the following order:

\[
\forall S\in(0,S_0],\ a,I,\sigma,\quad
\exists Q_0,c_I,C_I>0,\quad
\forall Q\ge Q_0\ \exists M_0(Q),\quad
\forall M\ge M_0(Q),\ R\ge1,
\]

with a common bound of the form (20). The constants and (Q_0) may depend on the fixed time and configuration; the mesh threshold may depend on the cap. No mesh threshold uniform in all caps, and no constants uniform as (S\downarrow0) or \(\rho\uparrow1\), are needed or established.

“Centered” is the intended reading of the covariance specification and is explicitly used in Sections 3–5. For complete formal precision, Section 1 should say so: arbitrary Gaussian means are not additional free parameters. In particular the regressions use covariance, and (\mathbb E X^2) is used as variance. This review does not interpret the premise as permitting noncentered, possibly deterministic sources with unspecified means.

## 2. Section 3: derive the temporal bound uniformly

All norms in this section are the normalized population/empirical (L^2) norms and their induced operator norms. For (U\otimes V),

\[
\|U\otimes V\|_{\mathrm{op}}
\le \|U\|_2\|V\|_2,
\]

because \(|\mathbb E[VB]|\le\|V\|_2\|B\|_2\). Query cuts are contractions in magnitude, so they can only improve the bounds that follow.

At nodes (t_k\le T), the readout update gives

\[
\|W^{(4)}_k\|_\infty\le at_k,
\qquad \|\delta^{(3)}_{k,a}\|_2\le ea t_k.
\]

Using the two samples and the factor (1/2) in (1),

\[
\|W^{(3)}_{k+1}-W^{(3)}_k\|_{\mathrm{op}}
\le ea^2 t_k\Delta.
\]

Consequently it is enough to choose

\[
N_3=10+ea^2T^2,
\qquad N_2=10+e^2a^2N_3T^2.
\]

Indeed \(\|W^{(3)}_k\|_{\mathrm{op}}\le N_3\),

\[
\|q^{(2)}_{k,a}\|_2\le N_3ea t_k,
\quad \|\delta^{(2)}_{k,a}\|_2\le e^2aN_3t_k,
\]

and the (W^{(2)}) increment is at most \(e^2a^2N_3t_k\Delta\). Summing it gives the asserted (N_2) bound. Next,

\[
\|q^{(1)}_{k,a}\|_2\le N_2N_3e^2at_k,
\quad \|\delta^{(1)}_{k,a}\|_2\le N_2N_3e^3at_k.
\]

Since \(|C_{ba}|\le1\), each first-field increment is bounded by (K_1\Delta), where

\[
K_1=N_2N_3e^3aT.
\]

This also covers \(\rho=-1\); no inverse of (C) is used in these estimates.

Define per-unit-time matrix bounds

\[
J_2=e^2a^2N_3T,\qquad J_3=ea^2T.
\]

The exact product split at lines 154–155 and the (e)-Lipschitz property of \(\phi\) give forward increment constants

\[
K_2=aJ_2+N_2eK_1,
\qquad K_3=aJ_3+N_3eK_2.
\]

Thus \(\|Z^{(\ell)}_{k+1,a}-Z^{(\ell)}_{k,a}\|_2\le K_\ell\Delta\) for \(\ell=2,3\). Finally,

\[
\begin{aligned}
\|\delta^{(3)}_{k+1,a}-\delta^{(3)}_{k,a}\|_2
&\le e\|W^{(4)}_{k+1}-W^{(4)}_k\|_2
 +aT c\|Z^{(3)}_{k+1,a}-Z^{(3)}_{k,a}\|_2\\
&\le D\Delta,\qquad D=ea+aTcK_3.
\end{aligned}
\]

Telescoping proves (7). These constants have no cap or mesh dependence. The bounds are deliberately loose; their finiteness and uniformity are what matters.

If the finite-width initial norm event invoked at lines 165–167 is used, its high probability can also be checked elementarily. A (1/4)-net of the Euclidean unit sphere can be chosen with at most (9^n) points: take a maximal separated set and compare the volumes of disjoint balls of radius (1/8) inside the ball of radius (9/8). For nets in both arguments,

\[
\|W\|_{\mathrm{op}}\le2\max_{u,v\text{ in the nets}}|u^TWv|.
\]

Each fixed bilinear form is (N(0,1/n)). A union bound therefore gives

\[
\mathbb P\{\|W\|_{\mathrm{op}}>10\}
\le2\,9^{2n}\exp(-25n/2)\longrightarrow0.
\]

Another union bound handles both matrices. At fixed cap and mesh, the imported convergence of empirical joint second moments then transfers (7) to the program: a deterministic limiting second moment cannot exceed a bound that holds with probability tending to one. No unproved interchange of expectations over the exceptional norm event is needed.

By (4), expanding the two squares gives the exact equality

\[
\mathbb E|\zeta_{k,a}-\zeta_{j,a}|^2
=\mathbb E|\delta^{(3)}_{k,a}-\delta^{(3)}_{j,a}|^2.
\]

The zero initial readout gives \(\zeta_{0,a}=0\) almost surely. Linear interpolation preserves the increment bound: within one cell the difference is a scalar multiple of one node increment, and across cells the (L^2) triangle inequality adds segment lengths to exactly \(|t-u|\).

## 3. Section 3: derive the Gaussian maximum estimate

For a centered scalar Gaussian (Y) of variance at most (v^2), integrating its density after completing the square gives

\[
\mathbb E e^{\lambda Y}\le e^{\lambda^2v^2/2}.
\]

Exponential Markov with \(\lambda=u/v^2\), applied to both signs, gives
\(\mathbb P(|Y|>u)\le2e^{-u^2/(2v^2)}\). The zero-variance case is immediate. For any (N) such Gaussians, independence is unnecessary:

\[
\mathbb P\{\max_i|Y_i|>u\}
\le\min\{1,2Ne^{-u^2/(2v^2)}\}.
\]

Integrating the tail of the square, split at \(s_*=2v^2\log(2N)\):

\[
\begin{aligned}
\mathbb E\max_i|Y_i|^2
&\le s_*+\int_{s_*}^{\infty}2Ne^{-s/(2v^2)}\,ds\\
&=2v^2\{\log(2N)+1\}.
\end{aligned}
\]

For a continuous finite Gaussian interpolation (G) starting at zero, approximate each (t<S) by successive dyadic left endpoints. At level (j\ge1), each nonzero refinement increment has length at most (S2^{-j}), and there are at most (2^j) possibilities. If (M_j) is their maximum absolute value, then

\[
\|M_j\|_2\le DS2^{-j}\sqrt{2\{(j+1)\log2+1\}}.
\]

Continuity gives \(\sup_{t\le S}|G(t)|\le |G(S)|+\sum_{j\ge1}M_j\). The sum of the displayed (L^2) bounds is finite. Applying the triangle inequality to partial sums and then monotone convergence to their squares proves

\[
\left\|\sup_{t\le S}|G(t)|\right\|_2\le KDS,
\quad
K=1+\sum_{j\ge1}2^{-j}\sqrt{2\{(j+1)\log2+1\}}<\infty.
\]

This is (9), with no dimension dependence and no limiting Gaussian-process theorem. For two sample paths,

\[
\mathbb E\max_b\sup_t|G_b(t)|^2\le2K^2D^2S^2.
\]

Centering matters to the statement of this auxiliary lemma. Without it, a deterministic process (G(t)=Lt) has zero increment standard deviations and need not satisfy (9). The applications here are to centered sources and centered regression residuals.

## 4. Section 4: terminal variance really is positive

For \(|\rho|<1\), the initial first-field pair has a strictly positive Gaussian density on \(\mathbb R^2\). If a vector (u\) satisfied

\[
\mathbb E\big(u_1\phi(Z^{(1)}_{0,1})+u_2\phi(Z^{(1)}_{0,2})\big)^2=0,
\]

continuity and positive density would make (u_1\phi(x)+u_2\phi(y)=0\) everywhere. Varying (x), then (y), and using that \(\phi\) is nonconstant forces (u=0\). Hence its feature Gram is positive definite.

At \(\rho=-1\), write the features as (1+b(G),1-b(G)\), with (b(G)=0.1\arctan(\sinh G)\). Here \(\mathbb Eb(G)=0\) and \(\beta=\mathbb Eb(G)^2>0\). The Gram is

\[
\begin{pmatrix}1+\beta&1-\beta\\1-\beta&1+\beta\end{pmatrix},
\]

whose eigenvalues are (2\) and (2\beta\). Thus the singular input covariance does not give a singular feature Gram.

The initial forward Gaussian laws used at lines 203–204 follow from the stated independent Gaussian initialization, rather than a new trained-neuron independence assertion. Conditional on previous-layer features, each next-layer row is a centered Gaussian pair whose covariance is their empirical Gram. For bounded features, conditional variances of the empirical Gram entries are at most (a^4/n\), so convergence to their conditional means follows from Markov applied to the squared error. At a positive definite limiting Gram, its two-dimensional Gaussian law can be coupled continuously using the explicit Cholesky factor. Bounded continuous feature functions then have convergent expectations. Applying this successively gives Gaussian forward pairs with the preceding feature Grams as covariance. The positive-density argument above therefore gives a positive definite top feature Gram, say (K^{(3)}_0\).

For either label vector (y\ne0\),

\[
\|V_0\|_2^2=\tfrac14 y^TK^{(3)}_0y>0,
\qquad V_0=\tfrac12\sum_b y_bH^{(3)}_{0,b}.
\]

Continuity of the local fields and the readout equation give

\[
\left\|\frac{W^{(4)}(S)}S-V_0\right\|_2
\le\sup_{0\le s\le S}
\left\|\tfrac12\sum_b y_bH^{(3)}_b(s)-V_0\right\|_2
\longrightarrow0.
\]

Choose (S_0\) so this is less than \(\|V_0\|_2/2\) throughout \((0,S_0]\). The readout is nonzero in (L^2\) at every such time. Since (Z^{(3)}_a(S)\) is finite almost surely and \(\phi'(z)>0\) for every finite (z\), multiplying the readout by this gate cannot make it zero almost surely. Thus (v_a(S)>0\) for both samples.

The first feature Gram stays positive definite because

\[
|K_{ab}(S)-K_{ab}(0)|
\le a\|H^{(1)}_a(S)-H^{(1)}_a(0)\|_2
 +a\|H^{(1)}_b(S)-H^{(1)}_b(0)\|_2\to0.
\]

For sufficiently small perturbations, its quadratic form on the unit circle remains at least half the initial minimum. Also \(|f_a(S)|\le a^2S\) and \(|g(S)|\le a^2S\), so the asserted \(|g|<1/2\) follows by shrinking (S_0\).

Fix (S\) and a sample. Strong cut removal gives convergence of the squared (L^2\) norms, since

\[
\big|\|U\|_2^2-\|V\|_2^2\big|
\le(\|U\|_2+\|V\|_2)\|U-V\|_2.
\]

Choose the cap threshold to make the variance error at most (v_a(S)/4\), then the mesh threshold to make the next error at most (v_a(S)/4\). Consequently

\[
v_0:=v_a(S)/2\le \mathbb E\zeta_{M,a}^2\le v_1:=(eaS)^2.
\]

These thresholds are independent of the tail level (R\). This supplies exactly the nested uniformity required later.

## 5. Section 4: reverse regression, independence, and probability

Let (X=\zeta_{M,a}\), (v=\mathbb EX^2\in[v_0,v_1]\), and set

\[
c_i=\frac{\mathbb E[\zeta_iX]}v,
\qquad G_i=\zeta_i-c_iX.
\]

Then \(\mathbb E[G_iX]=0\). For any finite real vector (u\) and scalar (t\), joint Gaussianity gives

\[
\mathbb E e^{i(tX+u\cdot G)}
=\exp\{-\tfrac12(t^2v+u^T\operatorname{Cov}(G)u)\}.
\]

This factors into the two characteristic functions, proving independence of (X\) from the entire residual vector. The calculation requires no density or inverse for \(\operatorname{Cov}(G)\), so it includes all singular cases.

For an interpolated increment,

\[
\operatorname{Var}(G_b(t)-G_b(u))
=\operatorname{Var}(\zeta_b(t)-\zeta_b(u))
 -\frac{\operatorname{Cov}(\zeta_b(t)-\zeta_b(u),X)^2}{v}
\le D^2|t-u|^2.
\]

The residual starts at zero. The preceding maximum bound and Markov therefore give, with (B_0=2KDS\),

\[
\mathbb P\{\max_{k,b}|G_{k,b}|\le B_0\}\ge\tfrac12.
\]

Cauchy–Schwarz also gives

\[
|c_i|\le\sqrt{\mathbb E\zeta_i^2/v}\le eaS/\sqrt{v_0}=:C_\zeta.
\]

The one-unit interval for \(\sigma X\) in (13) has probability at least

\[
\frac1{\sqrt{2\pi v_1}}
\exp\left[-\frac{(R+a+2)^2}{2v_0}\right].
\]

The prefactor uses (v\le v_1\), and the exponent uses (v\ge v_0\). This holds for either sign by symmetry of the centered normal law. Its intersection with the residual-bound event, denoted (E_R\), has at least half this probability by the established independence. Since (R+a+2\le(a+3)(R+1)\), this has the claimed Gaussian lower-bound form.

On (E_R\),

\[
\max_i|\zeta_i|\le C_\zeta(R+a+2)+B_0=:B_R.
\]

For every forward-source realization, the bounded feature memory gives

\[
|q_i-\zeta_i|\le\sum_j|B_{ij}|\,|H_j|\le a.
\]

Therefore \(\sigma q_{M,a}\ge R+1\), and \(|q_i|\le B_R+a\) at every node. This is a statement simultaneous in all forward-source values. It is essential to condition on the source-measurable event (E_R\); the proof is not conditioning on a query-tail event that could select the forward source. Lines 246–248 justify precisely this distinction.

## 6. Section 5: forward conditioning and the quantitative preimage

Let (X_f=\xi_{M,a}\). Bounded positive features give

\[
m^2\le v_f:=\mathbb EX_f^2\le a^2.
\]

Regress \(\xi_i=d_iX_f+F_i\). The same characteristic-function calculation yields independence of (X_f\) and the full (F\), while independence of the original groups yields independence of \((X_f,F)\) and \(\zeta\). Moreover,

\[
|d_i|\le a^2/m^2=:d_0,\qquad d_{M,a}=1,
\qquad F_{M,a}=0\quad\text{almost surely}.
\]

Conditional on an admissible residual value (F\) and a reverse-source value in (E_R\), the remaining scalar retains the law (N(0,v_f)\). “Any (F\)” should mean any value in its support, or almost every value under its law; in particular its terminal coordinate is zero. There is no conditioning on a null event using a joint Gaussian density. The independent product representation provides the conditional kernel directly.

With (X_f=x\), (2) is causal: first compute (Z_k\) using times (r<k\), then (H_k\), then (q_k\) using (r\le k\), then \(\delta_k\). Thus its dependence on (x\) is continuous. Current-time (B\) terms introduce no implicit equation.

Write (Q_R=B_R+a\). Uniformly in (x,F\),

\[
|\delta_{r,b}|\le eQ_R,
\qquad |Z_{M,a}(x)-x|
\le\sum_{r<M,b}\tfrac34\Delta eQ_R
=\tfrac32SeQ_R=:D_R.
\]

The absence of a terminal residual term is crucial. No maximum or small-ball estimate for (F\) is being hidden here.

For two scalar inputs, set
\(E_k=\max_{j\le k,b}|Z_{j,b}(x)-Z_{j,b}(x')|\). Then

\[
|q_{r,b}(x)-q_{r,b}(x')|\le eE_r.
\]

Splitting the product in \(\delta=\phi'(Z)\tau_Q(q)\),

\[
\begin{aligned}
|\delta(x)-\delta(x')|
&\le c|Z(x)-Z(x')|\,|\tau_Q(q(x))|
 +e|\tau_Q(q(x))-\tau_Q(q(x'))|\\
&\le(cQ_R+e^2)E_r=:L_R^0E_r.
\end{aligned}
\]

This uses exactly the two cut inequalities stated in Section 1. Combining the two samples in the (A\)-sum gives

\[
E_k\le d_0|x-x'|+\alpha\Delta\sum_{r<k}E_r,
\qquad \alpha=\tfrac32L_R^0.
\]

Induction gives (E_k\le d_0|x-x'|(1+\alpha\Delta)^k\): substituting this bound in the sum evaluates a geometric series. Hence

\[
|Z_{M,a}(x)-Z_{M,a}(x')|
\le L_R|x-x'|,
\quad L_R=d_0e^{(3/2)SL_R^0}.
\]

Because (B_R\) is affine in (R\), there are fixed positive constants with

\[
D_R\le C_D(R+1),\qquad 1\le L_R\le C_L e^{C_L(R+1)}.
\]

Fix \([b-h,b+h]\subset\operatorname{int}I\), (h>0\). The displacement bound gives

\[
Z_{M,a}(b-D_R-1)\le b-1,
\quad Z_{M,a}(b+D_R+1)\ge b+1.
\]

Continuity therefore supplies a root (x_0\) with output (b\) between these inputs. Monotonicity and a nonzero derivative are unnecessary. For

\[
r_R=\min\{1/2,h/(2L_R)\},
\]

the interval \([x_0-r_R,x_0+r_R]\) maps into
\(J=[b-h/2,b+h/2]\). Also

\[
r_R\ge\min\{1/2,h/(2C_L)\}e^{-C_L(R+1)},
\qquad |x|\le |b|+D_R+3/2
\]

on that input interval. The (N(0,v_f)\) density there is bounded below by

\[
\frac1{\sqrt{2\pi}a}
\exp\left[-\frac{(|b|+D_R+3/2)^2}{2m^2}\right].
\]

Integrating over its length (2r_R\) yields

\[
\mathbb P\{Z_{M,a}\in J\mid F,\zeta\}
\ge\frac{2r_R}{\sqrt{2\pi}a}
\exp\left[-\frac{(|b|+D_R+3/2)^2}{2m^2}\right]
\ge c_f e^{-C_f(R+1)^2}
\]

on (E_R\). To see the last absorption explicitly, bound
\(|b|+D_R+3/2\le(|b|+C_D+3/2)(R+1)\) and use \(R+1\le(R+1)^2\).

A measurable choice of (x_0\) is unnecessary. The recursion is a continuous finite function of its source coordinates, so its fixed closed-set preimage is measurable. The displayed lower bound is a pointwise bound on the Gaussian measure of that preimage. Integrate this bound with respect to the independent laws of (F\) and \(\zeta\), obtaining

\[
\begin{aligned}
\mathbb P\{Z_{M,a}\in J,\ \sigma q_{M,a}\ge R+1\}
&\ge\mathbb E\big[1_{E_R}\,
 \mathbb P\{Z_{M,a}\in J\mid F,\zeta\}\big]\\
&\ge c_fc_\zeta e^{-(C_f+C_\zeta')(R+1)^2}.
\end{aligned}
\]

Here (c_\zeta,C_\zeta'\) denote the reverse-event probability constants, not the regression coefficient bound. This proves (20). The exponentially small preimage length incurs only a linear exponential cost, which is absorbed by the scalar Gaussian density cost. There is no extra mesh-dependent factor.

## 7. Section 6: both limit passages and curvature tails

For fixed (R\), the event

\[
F_R=J\times\{q:\sigma q\ge R+1\}
\]

is closed. If laws \(\mu_n\) converge against bounded continuous functions to \(\mu\), define

\[
f_j(x)=\max\{0,1-j\,\operatorname{dist}(x,F_R)\}.
\]

Then (1_{F_R}\le f_j\), so

\[
\limsup_n\mu_n(F_R)\le\int f_j\,d\mu.
\]

Since (f_j\downarrow1_{F_R}\), bounded convergence gives
\(\limsup_n\mu_n(F_R)\le\mu(F_R)\). Thus a common lower bound on these **closed-event** probabilities survives in the limit; the inequality in the candidate has the correct direction.

First apply this at a fixed sufficiently large cap as (M\to\infty\); then apply it to strong cut removal. Strong (L^2\) convergence implies convergence in probability by Markov. It implies convergence of expectations of bounded continuous functions: from any subsequence choose a further subsequence with summable probabilities of errors exceeding (2^{-j}\); the union bound on the tails of these events gives almost-sure convergence, and bounded convergence applies. This justifies the second use without additional Gaussian path assumptions.

All constants were fixed before the two limits. The final event is contained in \(\{Z\in I,\sigma q>R\}\), due to the interior interval and the extra query margin. No boundary atom must be ruled out. The argument applies to each (R\) with the same constants; uniform convergence in (R\) is not needed.

For a compact interval (J\subset(1,2)\) of positive length, direct differentiation gives

\[
\phi'(z)=0.1\operatorname{sech}z,
\qquad \phi''(z)=-0.1\operatorname{sech}z\tanh z.
\]

Continuity and strict negativity on (J\) give
\(\kappa:=\min_J|\phi''|>0\). For
\(U=y_a\phi''(Z^{(2)}_a(S))q^{(2)}_a(S)\), choosing the query sign \(-\sigma y_a\) and threshold (R/\kappa\) proves a lower bound of Gaussian form for \(\mathbb P\{Z\in J,\sigma U>R\}\). Since \(\kappa\le c<1\), that query threshold is at least one when (R\ge1\).

The upper moment premise gives the explicit bounds

\[
\mathbb P\{|q|>R\}\le2e^{-R^2/16},
\qquad
\mathbb P\{|U|>R\}\le2e^{-R^2/(16c^2)}.
\]

The joint lower bound also implies a lower bound conditional on the positive-probability event \(\{Z\in J\}\), by division by its probability. It does not assert a bound conditional on each individual value (Z=z\), nor independence of (Z\) and (q\).

## 8. Adversarial checks and limits of possible counterexamples

The following checks identify why plausible objections fail, or which premise they would have to violate.

- **Singular source groups:** If all reverse coordinates are multiples of the terminal scalar, then (G=0\) and the residual event has probability one. The forward residual may likewise vanish. Only (v\) and (v_f\) are divided by; no full Gram inverse appears in Sections 3–6. Varying the scalar within the regression representation stays within the Gaussian support.
- **Large or highly correlated forward residuals:** These need not be bounded. The terminal residual vanishes, and the entire learned displacement is bounded by bounded gates, bounded reverse queries, and the (A\)-sum. Their conditional cost is therefore zero.
- **A highly non-monotone forward map:** A continuous map within (D_R\) of the identity must cross (b\). Its upper Lipschitz bound supplies a preimage interval even if its derivative vanishes or it has many roots.
- **Dependence of evolved (Z\) and (q\):** This is allowed. The reverse event supplies a query-tail statement valid for every forward realization. Only the original source groups are assumed independent.
- **Loss of source independence:** As an abstract warning, take terminal (Z=X\), (q=\epsilon X\), and (A=B=0\), where (X\) is a centered Gaussian. On a bounded (Z\)-interval, (q\) is bounded. This toy example violates the independent-source hypothesis; it is not a counterexample to the candidate.
- **Zero reverse variance:** If \(\zeta=0\), then \(|q|\le a\) from the (B\)-bound. At time zero the actual readout and reverse source are zero. For the excluded case \(\rho=1\) with opposite labels, identical samples can keep the readout and the entire flow stationary. The positive-time nondegeneracy and the exclusion of this configuration matter.
- **No temporal covariance estimate:** Independent unit-variance reverse coordinates at increasingly many mesh times have \(\mathbb P(\max|G_i|\le B)=p_B^N\to0\) for fixed (B\), where (p_B<1\). This defeats a mesh-uniform residual-path event if only marginal variances are known. It violates (8); the primal derivation of (8) is an essential part of this proof. This observation by itself does not claim a counterexample to every possible tail theorem without (8).
- **Truncation at a fixed cap:** The quantity whose tail is estimated is the untruncated query (q\), not the bounded value \(\tau_Q(q)\). There is no contradiction in its having an unbounded tail at a fixed cap.
- **Noncentered Gaussian wording:** The auxiliary lemma with increment standard deviations alone is false for nonzero deterministic means, as noted above. Explicit centering removes this wording issue and matches the intended covariance premises.

None of these checks supplies a counterexample under the centered finite-program and local-convergence hypotheses actually used.

## 9. Section 7: derivative audit and an explicit remainder estimate

The dual feature (B_a\) is well defined because the (2\times2\) first feature Gram is positive definite. Direct matrix multiplication gives

\[
\|B_a\|_2^2
=\frac{(K^{-1}KK^{-1})_{aa}}{(K^{-1})_{aa}}=1,
\quad \mathbb E[B_aH^{(1)}_b]=d_a1_{a=b}.
\]

It is bounded, being a fixed finite linear combination of bounded features. Thus (D=v\otimes B_a\) has Hilbert–Schmidt norm one for every bounded (v\) with \(\|v\|_2=1\). It changes only the chosen sample's second preactivation, by (td_av\), and leaves the other sample's entire predictor constant along the line.

For fixed bounded (v\), continuity of \(\phi''\) and its bound (c\) give

\[
H^{(2)}_a(t)=H^{(2)}_a
 +td_a\phi'(Z^{(2)}_a)v
 +\tfrac12t^2d_a^2\phi''(Z^{(2)}_a)v^2+o_{L^2}(t^2).
\]

For justification, the pointwise second Taylor quotient converges, and its error is bounded by a fixed multiple of (v^2\); the square of this dominating function is integrable because (v\) is bounded and in (L^2\). Boundedness of (W^{(3)}\) transfers this expansion to

\[
Z^{(3)}_a(t)=z+tu+\tfrac12t^2w+o_{L^2}(t^2),
\]

where (u,w\) are exactly the two variations in (21).

Let \(\mathcal F(z)=\mathbb E[W^{(4)}\phi(z)]\). For a straight (L^2\) direction (u\), the scalar second quotient is bounded by \(c\|W^{(4)}\|_\infty u^2\), so dominated convergence gives its limit \(\mathbb E[W^{(4)}\phi''(z)u^2]\). No (L^4\) assumption on (u\) is needed.

For full precision in lines 373–375, put
\(r(t)=\tfrac12t^2w+o_{L^2}(t^2)\). The gate Lipschitz bound and scalar Taylor's formula give

\[
\begin{aligned}
&|\mathcal F(z+tu+r)-\mathcal F(z+tu)
       -\mathbb E[W^{(4)}\phi'(z)r]|\\
&\qquad\le c\|W^{(4)}\|_\infty
 \left(|t|\|u\|_2\|r\|_2+\tfrac12\|r\|_2^2\right)
=o(t^2).
\end{aligned}
\]

The factor \(|t|\) is necessary: the bound written in the candidate as (O(\|u\|_2\times\text{correction})\), with (u\) a fixed direction, is only (O(t^2)\) and alone does not establish the asserted second-order coefficient. The stronger estimate above is available under exactly the stated assumptions.

One can verify an ordinary second derivative, rather than only a second-order Peano expansion. The middle curve is twice differentiable in (L^2\) for bounded (v\), and

\[
\frac d{dt}\mathcal F(Z^{(3)}_a(t))
=\mathbb E[W^{(4)}\phi'(Z^{(3)}_a(t))(Z^{(3)}_a)'(t)].
\]

Subtract its value at zero and divide by (t\). The term involving \(((Z^{(3)})'(t)-u)/t\) converges in (L^2\) to (w\). The straight-line gate term paired with (u\) converges by domination by (cu^2\), and replacing (z+tu\) with (z+tu+r(t)\) changes it by at most \(c\|W^{(4)}\|_\infty\|r(t)\|_2\|u\|_2/|t|\to0\). This proves the claimed second derivative.

Actual adjunction now proves (22). Its last term obeys exactly

\[
\left|\tfrac12y_ad_a^2\mathbb E_3
 [W^{(4)}\phi''(Z^{(3)}_a)(W^{(3)}[\phi'(Z^{(2)}_a)v])^2]\right|
\le\tfrac12d_a^2aSc\|W^{(3)}\|_{\mathrm{op}}^2e^2.
\]

If (U=y_a\phi''(Z^{(2)}_a)q^{(2)}_a\) and (A_N=\{Z^{(2)}_a\in J,U>N\}\), the Gaussian lower bound gives (p_N=\mathbb P(A_N)>0\). The direction (v_N=1_{A_N}/\sqrt{p_N}\) is bounded for each (N\), has norm one, and

\[
\mathbb E[Uv_N^2]=p_N^{-1}\mathbb E[U1_{A_N}]>N.
\]

The expectation is finite since (U\in L^2\) and (v_N\) is bounded. The negative event gives the other sign. The directions need not have a common (L^\infty\) bound; the claimed class does not require one. Hence the second directional derivatives of (g\) have both unbounded signs.

For these directions, the necessary first-derivative bound is explicit:

\[
|Df_a[D]|
\le d_a\|W^{(4)}\|_2e\|W^{(3)}\|_{\mathrm{op}}e
\le d_a aS e^2\|W^{(3)}\|_{\mathrm{op}},
\qquad Df_b[D]=0\ (b\ne a).
\]

Thus a broad assertion about all predictor gradients is not needed to bound the first-derivative term in the loss calculation.

## 10. Loss curvature, symmetry, physical time, and restartability

Equation (24) is algebraically correct **at a state satisfying (f_a=y_ag\)**:

\[
D^2L[D,D]
=2\sum_a(Df_a[D])^2+2\sum_a(f_a-y_a)D^2f_a[D,D],
\]

and substituting \(f_a-y_a=y_a(g-1)\) and \(\sum_a y_aD^2f_a=2D^2g\) gives (24). Symmetry is needed at the base state only; the perturbed line need not preserve it.

The Section 1 dependency descriptions mention “sample symmetry,” but the displayed consequences do not actually state the identity used in (24). A dependency title is not a proof of that identity in this isolated audit. The intended elementary justification is available if the finite cut Euler construction is equivariant under the following transformations: for equal labels, swap the samples; for opposite labels, swap the samples and negate the readout. In the latter case the uncut backward fields are negated and swapped, hidden-operator velocities are unchanged, and the readout velocity is negated. The Gaussian initialization is invariant under the corresponding transformation, including the antipodal-input case.

For this opposite-label argument to work at the cut level, every cutoff applied to a sign-reversed query must be odd: tau_Q(-u) = -tau_Q(u). Being smooth, one-Lipschitz, and bounded in magnitude by |u| does not imply oddness. Thus this is an additional property to specify if symmetry is justified through the cut Euler construction. With the appropriate equivariant construction and deterministic population predictor limits, the two predictors are equal for equal labels and negatives for opposite labels, giving the identity used in (24). This route uses finite Euler equivariance and convergence, not an unproved uniqueness theorem for the uncut flow.

If the admitted premises are restricted to the displayed program and convergence without such an explicit equivariant construction, the identity and the physical-clock assertion should be labeled conditional on sample symmetry. They are not consequences of arbitrary deterministic coefficients (A,B\) satisfying just the numerical bounds (3).

The actual **unbounded loss-curvature conclusion does not need sample symmetry**. Shrink (S_0\), if necessary, so (a^2S_0<1/2\). Then \(|f_a(S)|<1/2\), so (f_a(S)-y_a\ne0\). On the sample-isolating line above,

\[
D^2L[D,D]
=2(Df_a[D])^2+2(f_a-y_a)D^2f_a[D,D].
\]

The first term is uniformly bounded, the nonzero residual is fixed, and \(D^2f_a=2y_aD^2g\) on this line has both unbounded signs. This proves both unbounded signs for (D^2L\) directly from the local bounds and the probability conclusion. It supplies a local repair even if sample symmetry is not included as a formal premise.

If the raw loss gradient were Lipschitz with constant (L_0\) on some neighborhood, each fixed unit direction (D\) would satisfy

\[
\left|\frac{\langle\nabla L(\theta+tD)-\nabla L(\theta),D\rangle}{t}\right|
\le L_0.
\]

The second derivatives just proved are the limits of these quotients, a contradiction. Each bounded direction may have its own allowable small line parameter. This argument does not assume a bounded Hessian exists, or claim twice Fréchet differentiability on the whole raw space.

With the symmetry identity supplied, \(-\nabla L=4(1-g)\nabla g\), and (1) is the \(\nabla g\) flow in the stated metric. The time change in lines 415–417 is then correct. Since \(|g|<1/2\),

\[
2<4(1-g)<6,\qquad S/6<t(S)<S/2.
\]

This gives a positive finite deterministic local physical time. Without symmetry, this particular scalar-clock identification has not been proved by the displayed premises.

Finally, existence of a (C^1\) local solution, convergence of a chosen family of cuts, and fixed-time Gaussian tails do not imply uniqueness of every solution restarted at that state. The candidate does not display a comparison estimate or another uniqueness hypothesis sufficient for that conclusion. The mention of an imported Gaussian-tail argument is outside the admitted mathematical input. Unique restartability must remain an explicitly unverified additional premise here.

## 11. Required corrections versus optional improvements

### Required for a formally complete scoped presentation

1. **State centering explicitly** at lines 92–100 and in the auxiliary lemma at lines 178–182. This matches the intended source law; it is not a new covariance nondegeneracy assumption. Literally without centering, the lemma is false and the stated regressions need not be regressions by covariance.
2. **Supply the time factor in the Section 7 correction estimate** at lines 373–375. Use the \(|t|\|u\|_2\|r(t)\|_2+\|r(t)\|_2^2/2\) estimate above. The displayed loose bound alone is insufficient to identify the second derivative. This is a repairable proof-detail gap, not a counterexample to (22).
3. **Make the status of sample symmetry explicit** for (24) and the physical clock. Either state the identity as an additional admitted premise or include the finite-Euler equivariance argument with the required common cuts and their oddness for opposite labels. Oddness is not among the displayed cutoff hypotheses. For the unbounded loss-curvature claim alone, the sample-isolating residual argument above removes the dependency entirely after a harmless shrinking of the time interval.
4. **Separate unique restartability from the certified implication** at lines 135–136 and 430–432. Remove it from what the displayed premises are said to prove, or state the needed additional uniqueness premise. This audit has not read or validated the named argument.

There is **no required change to the core source-event construction, the forward preimage argument, the two probability exponents, or the order and direction of the two limit passages** under the intended centered hypotheses.

### Optional clarity improvements

- Use (Q\) for caps and (R\) for tail thresholds.
- Name (E_R\) as a reverse-source-only event when conditioning in Section 5.
- Replace “ANY (F\)” by “every admissible residual value, hence almost surely under the residual law.”
- Display the nested cap/mesh quantifier and note that it does not claim a common mesh threshold for all caps.
- Add the temporal covariance estimate to the Section 8 summary of ingredients; terminal variance bounds alone do not supply the uniform path event.
- If presenting the upper and lower tails as conditional on a compact (Z\)-interval, state that conditioning is on the interval event, not on an exact preactivation value.
- Record that the unit test directions are individually bounded, with bounds allowed to grow with the tail threshold.

The result established by this audit is the new finite-program-to-local-law Gaussian lower tail and its justified bounded-direction consequences, conditional on the specified premises. It supplies no certification of those premises or of a global model theorem.
