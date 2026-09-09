# Gaussian-disorder dynamics: theorem and proof applicability audit

2026-09-08. This examines a new route following the direct source impasse. The fixed activation, original Gaussian initialization, physical residual feedback, raw gradient metric, and exactly two hidden layers remain those of CONTRACT.md. No numerical experiment or modified-model theorem is used.

**Conclusion:** none of the inspected theorems establishes the requested limit. The closest deterministic result has a bounded-Jacobian interaction assumption which fails for the true incoming-field gates. The classical spin-glass arguments obtain their stability from special structural assumptions, not merely from energy dissipation or bounded mobility. A useful causal-convolution estimate can nevertheless be proved independently; Section 4 gives its complete proof and identifies the missing neural premise.

## 1. Primary sources, inspected assumptions, and decisive proof steps

Public full-text PDFs were retrieved and converted locally under `/tmp/disorder_lit/`. Those copies are working material, not dependencies of the contract. The stable primary links below identify the inspected versions. No theorem is invoked as a black box to finish the neural problem. Sources rejected at a failed hypothesis do not require importing the remainder of their dependency tree.

### Ben Arous, Dembo, Guionnet: spherical spin-glass CK equations

[Full author manuscript](https://math.nyu.edu/~benarous/Publications/benarous_64.pdf), published as *Cugliandolo–Kurchan equations for dynamics of spin-glasses*, PTRF 136 (2006), 619–660, [publication](https://doi.org/10.1007/s00440-005-0491-y).

Inspected model (1.6)–(1.7), Hypothesis 1.1, Theorem 1.2, and proofs of Proposition 2.1 and Lemmas 2.2 and 2.6. The model has additive Brownian motion, a radial confining force, and a finite Gaussian polynomial Hamiltonian. The theorem identifies correlation and integrated response on every fixed finite horizon. Lemma 2.2 obtains a dimension-uniform Lipschitz bound on bounded empirical-norm balls by telescoping each multilinear interaction and applying its tensor norm. Lemma 2.6 inserts that estimate into a trajectory comparison and Gronwall argument. Proposition 2.1 obtains confinement using the radial force and a martingale estimate.

**Mismatch:** the neural loss is not a Gaussian polynomial Hamiltonian in its raw state. Its local derivative contains the multiplication operators (C\phi''(v_i)) and (q_i\phi''(z_i)), which are not bounded by the raw (L^2) state radius. Thus the essential Lemma 2.2 estimate is unavailable. Removing Brownian motion or replacing radial confinement by physical loss dissipation would not repair this structural failure.

### Ben Arous, Guionnet: symmetric Langevin dynamics

[Full author manuscript](https://cims.nyu.edu/~benarous/Publications/benarous_31.pdf), *Symmetric Langevin spin glass dynamics*, Annals of Probability 25 (1997), 1367–1422.

Inspected the exact model and assumptions in Sections 1–2, and the density construction in Section 2.2. The spins remain in a fixed bounded interval under a singular confining potential; the interaction is linear with a symmetric Gaussian matrix; Brownian noise is nondegenerate. The principal large-deviation/identification argument has a high-temperature or short-time restriction and uses an absolutely continuous path-measure change.

**Mismatch:** unbounded neural coordinates, deterministic dynamics, learned-operator memory, and the nonlinear two-orientation feedback are outside this model. A zero-noise substitution is not justified in the density proof: even scalar deterministic flows with distinct nonzero constant drifts have disjoint path supports when initialized identically.

### Dembo, Lubetzky, Zeitouni: asymmetric soft-spin universality

[Full manuscript](https://arxiv.org/pdf/1911.08001), *Universality for Langevin-like spin glass dynamics*, Annals of Applied Probability 31 (2021), 2864–2880.

Inspected Theorem 1.1, assumptions (1.1), (1.3)–(1.8), the Girsanov comparison, and the complete path-comparison argument in Section 4. The result treats bounded spins, additive Brownian motion, and linear asymmetric random interactions. The approximation comparison uses the interaction operator norm and the finite upper bound on (-U''); that one-sided curvature bound controls the local potential term. Remark 1.4 discusses other bounded-interaction models without proving the needed neural extension.

**Mismatch:** neither bounded spins nor the relevant one-sided curvature bound holds merely from the neural energy estimate. Replacing the true gates by bounded outputs or adding Brownian motion would change the contract. This paper does not remove that substitution.

### Celentano, Cheng, Montanari: deterministic Gaussian-data flows

[Full manuscript](https://arxiv.org/pdf/2112.07572), *The high-dimensional asymptotics of first order methods with random data*.

Inspected equation (12), Assumption 1, Theorems 1–2, response equations (16), Section 5, Appendix A.1.1–A.1.2, and the finite-flow discretization argument. The flow is (\dot\theta=-\theta\Lambda_t^T-\delta^{-1}X^T\ell_t(X\theta;z)), with uniformly Lipschitz (ell_t) and uniformly Lipschitz Jacobian. Its bottom response is deterministic because the corresponding local-state equation is linear. The global response bounds use coupled causal convolutions with deterministic bounded coefficients. The proof of its auxiliary convolution lemma invokes an external Volterra theorem; Section 4 below instead proves the needed elementary convolution statement directly.

**Mismatch:** the neural reverse coordinate map (b_i=C\phi'(v_i)) has derivative (C\phi''(v_i)), while the bottom map has (q_i\phi''(z_i)). Neither meets Assumption 1 uniformly in the cap. Augmenting by the learned (U) history does not put the exact system into equation (12), and it does not make the bottom response deterministic.

### Dembo, Gheissari: random-matrix diffusion universality

[Full manuscript](https://arxiv.org/pdf/2006.13167), *Diffusions interacting through a random matrix: universality via stochastic Taylor expansion*, [publication](https://doi.org/10.1007/s00440-021-01027-7).

Inspected the precise stochastic system (1.2), its coefficient hypotheses, the main universality statements, Section 1.4, and the generator-expansion construction. Zero diffusion is allowed, but the random drift in (1.2) is linear. The Hopfield and spherical applications use that linear system or its specified radial transformation. Their Remark 1.5 explains an unresolved absolute-summability difficulty when trying to extend the generator expansion to higher-order interactions with confinement.

**Mismatch:** allowing zero noise does not supply nonlinear incoming-field gates, and universality alone does not construct a Gaussian limit. The neural system has nonlinear disorder dependence before any time expansion. Its physical energy cancellation cannot be assumed to survive an absolute-value estimate of the generator series. No expansion from this paper is used as a convergence proof here.

## 2. Exact embedding test after eliminating the learned operator

Use (c_i=y_i-f_i), (A=A_0+U), and all actual fields from CONTRACT.md. The exact raw operator equation integrates to

\[
U(t)=\int_0^t\sum_j c_j(s)b_j(s)\otimes h_j(s)\,ds.
\]

Consequently

\[
v_i(t)=A_0h_i(t)+\int_0^t\sum_j c_j(s)b_j(s)
\langle h_j(s),h_i(t)\rangle\,ds,
\tag{1}
\]

\[
q_i(t)=A_0^*b_i(t)+\int_0^t\sum_j c_j(s)h_j(s)
\langle b_j(s),b_i(t)\rangle\,ds,
\tag{2}
\]

\[
\dot z_i=\sum_j\Gamma_{ij}c_j\phi'(z_j)q_j,
\qquad
\dot C=\sum_jc_j\phi(v_j),
\qquad b_i=C\phi'(v_i).
\tag{3}
\]

These preserve the same initialized matrix in both orientations, all learned memory, the activation offset, and physical feedback. They are identities, not an approximation.

The source inputs in (1)–(2) are themselves adapted to both orientations. Calling the two Gaussian answers independent would omit the initialized returns. Treating the learned memory as a prescribed force would omit its state dependence. A finite time discretization produces a finite program, but enlarging its number of memory coordinates with mesh refinement does not meet a theorem whose constants require a fixed-dimensional, uniformly Lipschitz coordinate map.

Differentiating the top preactivation instead gives the exact identity

\[
\dot v_i=\sum_jc_j\langle h_j,h_i\rangle b_j
+A\sum_j\Gamma_{ij}c_j\phi'(z_i)\phi'(z_j)A^*b_j.
\tag{4}
\]

Thus augmenting (v) as a dynamic state replaces an algebraic Gaussian action by a quadratic occurrence of the same disorder, with state-dependent multiplication between the orientations. It does not turn this into a drift linear in independent Gaussian coefficients. Equation (4) uses only the strong chain rule and the genuine adjoint, so this is a concrete embedding failure rather than an analogy-based objection.

Bounded mobility also does not imply the missing stability. For a bounded smooth scalar (m),

\[
m(x)y-m(\tilde x)\tilde y
=m(x)(y-\tilde y)+(m(x)-m(\tilde x))\tilde y.
\]

The second term involves the multiplication operator (\tilde y m'(\cdot)). Its norm on (L^2) is governed by an essential supremum, not by (|\tilde y|_2). In this model (m=\phi'), (\tilde y=C) or (q_i). The numerical lower and upper bounds (3/4\le m\le1) do not remove that term.

## 3. Precisely what the localization proofs suggest

The shared useful mechanism is to establish a dimension-uniform trajectory comparison on the physically relevant localized set, then combine it with a fixed discretization limit. For the spherical Gaussian-polynomial model this follows from a tensor operator norm on an empirical-norm ball. For bounded soft spins the local potential has a one-sided curvature estimate. For deterministic Gaussian-data flows the coordinate derivative is uniformly bounded.

The present neural model has a uniformly energy-bounded approximation family, but none of those three comparison estimates follows from that fact. The sharp replacement would be a reachable-state estimate for the dangerous incoming-field multipliers, preferably in the comparison's quadratic form rather than as an ambient operator norm. Merely assuming that replacement restates the remaining problem.

The source contraction results in SOURCE_ROUTE.md make the primitive Gaussian drivers uniformly controlled on the energy-preserving approximation family. Therefore a possible narrower adaptation is to prove causal response bounds which transmit existing spatial concentration without creating it, and close a Gronwall inequality for that concentration defect. That implication is currently open. The exact rare-event repeated-matrix example in SOURCE_ROUTE.md rules out deriving it from covariance contraction alone.

## 4. A proved global convolution estimate, without an external Volterra theorem

The deterministic-flow literature suggests preserving causal convolution structure instead of closing independent coefficient boxes. The following complete argument shows why that can matter. It is an auxiliary mathematical result, not yet an estimate for the neural responses.

**Lemma.** Let (u_0>0), (\alpha\ge0), and (\beta,\gamma,\delta>0). The equations

\[
u'(t)=\alpha u(t)+\beta(u*v)(t),\qquad u(0)=u_0,
\tag{5}
\]

\[
v(t)=\gamma u(t)+\delta(u*v)(t),\qquad
(u*v)(t)=\int_0^t u(t-s)v(s)\,ds
\tag{6}
\]

have a unique nonnegative continuous solution on ([0,\infty)), with (u\in C^1). There exist finite (K,\lambda), depending only on the displayed constants, such that (u(t)+v(t)\le Ke^{\lambda t}) for every (t\ge0).

**Proof.** Write (|f|_{1,\lambda}=\int_0^\infty e^{-\lambda t}|f(t)|dt). Weighted convolution satisfies

\[
\|f*g\|_{1,\lambda}\le\|f\|_{1,\lambda}\|g\|_{1,\lambda}
\tag{7}
\]

by Fubini and the identity (e^{-\lambda(s+t)}=e^{-\lambda s}e^{-\lambda t}). Choose (\lambda>\alpha), put

\[
a=\frac{2u_0}{\lambda-\alpha},\qquad b=2\gamma a,
\]

and enlarge (\lambda) until

\[
\delta a\le\tfrac18,
\qquad \frac{\beta b}{\lambda-\alpha}\le\tfrac18.
\tag{8}
\]

On the complete closed nonnegative set (|u|_{1,\lambda}\le a, |v|_{1,\lambda}\le b), consider

\[
\mathcal T_1(u,v)=u_0e^{\alpha t}
+\beta e^{\alpha\cdot}*(u*v),
\quad
\mathcal T_2(u,v)=\gamma u+\delta u*v.
\]

Equation (7) gives

\[
\|\mathcal T_1\|_{1,\lambda}\le a/2+a/8<a,
\qquad
\|\mathcal T_2\|_{1,\lambda}\le b/2+b/8<b.
\]

Use the distance (D((u,v),(\tilde u,\tilde v))=\|u-\tilde u\|_{1,\lambda}+(4\gamma)^{-1}\|v-\tilde v\|_{1,\lambda}). Since

\[
\|u*v-\tilde u*\tilde v\|_{1,\lambda}
\le b\|u-\tilde u\|_{1,\lambda}
+a\|v-\tilde v\|_{1,\lambda},
\]

the coefficient of (|u-\tilde u|_{1,\lambda}) in the output distance is at most

\[
\frac18+\frac14+\frac{\delta b}{4\gamma}
\le\frac7{16}.
\]

The coefficient relative to ((4\gamma)^{-1}\|v-\tilde v\|_{1,\lambda}) is at most

\[
\frac{4\gamma\beta a}{\lambda-\alpha}+\delta a
\le\frac14+\frac18=\frac38.
\]

Thus (mathcal T) is a contraction. Its Picard iterates converge to a nonnegative fixed point in the weighted (L^1) space.

For the pointwise estimate use (|f|_{\infty,\lambda}=\operatorname*{ess\,sup}_{t\ge0}e^{-\lambda t}|f(t)|). The mixed convolution bound (|f*g|_{\infty,\lambda}\le|f|_{\infty,\lambda}|g|_{1,\lambda}), proved directly from the integral, shows that the nonnegative Picard iterates started at zero satisfy

\[
\|u_{k+1}\|_{\infty,\lambda}
\le u_0+\frac18\|u_k\|_{\infty,\lambda}.
\]

Hence all these norms are at most (8u_0/7). Also (|v_{k+1}\|_{\infty,\lambda}\le(\gamma+\delta b)8u_0/7). A subsequence converges almost everywhere, so the same bounds hold for the fixed point. The first fixed-point equation implies (u) has a locally absolutely continuous representative. Its convolution with the locally integrable (v) is continuous, because this representative is continuous and bounded on each compact interval. Equations (5)–(6) then give (u\in C^1) and (v) continuous. The exponential bounds hold everywhere by continuity.

For uniqueness among arbitrary continuous solutions on a compact interval, bound their values by a finite number there. Differences of the two convolution terms on an initial interval of length (h) are at most a constant times (h) times the maximum differences of (u,v). Equation (6) bounds the (v)-difference by the (u)-difference plus this convolution difference; absorb the (v)-difference when (h) is small. The integrated equation (5) then absorbs the (u)-difference, making both zero. Repeating on successive intervals of the same sufficiently small length proves uniqueness on the compact interval; when the paths already agree before an interval, the convolution difference only uses times in that interval in one of its two factors. Every finite interval is covered by finitely many steps. ∎

For the neural problem, the corresponding response derivative equations contain products of the random derivatives with (C\phi''(v)) and (q\phi''(z)). Replacing their expectations by a deterministic bound times the expected derivative norm is unjustified: the factors are correlated. The energy estimate bounds the separate (L^2) incoming fields, not those products. Therefore (5)–(6) cannot currently be assigned to the true neural source responses with cap-independent coefficients.

## 5. Registry

| Item | Status |
|---|---|
| Exact learned-(U) elimination, including both initialized orientations | Proved identities (1)–(3) |
| Augmented preactivation equation retains a quadratic repeated-disorder term | Proved identity (4) |
| An inspected external theorem directly supplies the fixed-activation contract | No |
| Global causal-convolution majorant with fixed deterministic coefficients | Proved in Section 4 |
| Cap-independent neural estimate reducing the true response equations to such a majorant | Open |
| Bounded mobility or physical energy alone validates that reduction | Not established; stated arguments do not supply it |
| Global population flow and full actual GF/GD bridge | Still unresolved by this route |

The precise remaining task after this audit is an estimate for the physical reachable family, not further reinterpretation of a bounded-spin or globally Lipschitz theorem. A proof must control the correlated incoming-field multipliers, or replace source sensitivities by another stable observable that still identifies the genuine canonical dynamics.
