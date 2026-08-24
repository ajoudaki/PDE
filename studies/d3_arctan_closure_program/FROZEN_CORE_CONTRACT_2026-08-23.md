# Frozen core contract: fully trained depth-three vanilla arctangent

**Frozen:** 23 August 2026, before the new proof search.  This document fixes
what counts as resolving the conjecture.  Auxiliary proof objects may be much
larger, but the final theorem may not weaken or replace this contract.

## 1. Scientific claim and scope

The target is the exact one-sample, bias-free, equal-width MLP with three
nonlinear hidden vectors, activation

\[
\phi(x)=\arctan x,
\]

and all four parameter blocks trained in the mean-field feature-learning
metric.  The theorem must identify its direct infinite-width limit as an
autonomous operator-valued flow with one training-time variable, one immutable
joint Gaussian action source, and the current state

\[
(A,r,P_1,P_2,e).
\]

It must prove well-posedness, restartability, and full-sequence convergence in
probability of the exact continuous finite-width flow, uniformly on every
fixed compact physical-time interval, including the **raw** tangent kernel.

This is an operator-valued Markov limit.  It is not claimed to be a
finite-dimensional scalar compression: the immutable quenched source and the
two current trace-class operators are infinite-dimensional.  The substantive
closure claim is that no explicit history, path law, response kernel, or
two-training-time order parameter is required as evolving state.

Exact unscaled arctangent is part of the core theorem.  This is not a lazy or
linear escape: it is smooth, bounded, nonpolynomial, and leaves the adaptive
reused-adjoint field \(G_2^*B_3\) fully present.  Residual connections,
normalization, leaks, and activation universality are outside the core.

## 2. Canonical finite-width model

For \(j=1,2,3\), let

\[
H_{j,n}=\left(\mathbb R^n,
\langle x,z\rangle_{j,n}=n^{-1}x^{\mathsf T}z\right).
\]

For \(b\in H_{j+1,n}\), \(x\in H_{j,n}\), use the normalized
rank-one action

\[
(b\otimes_n x)v=b\langle x,v\rangle_{j,n}
                =n^{-1}bx^{\mathsf T}v.                 \tag{2.1}
\]

Fix arbitrary \(y_\star\in\mathbb R\) and \(\eta>0\).  Independently
initialize

\[
A_{0,n,i},u_{0,n,i}\stackrel{\mathrm{iid}}\sim N(0,1),\qquad
G_{\ell,0,n}=n^{-1/2}W_{\ell,n},\quad
(W_{\ell,n})_{ij}\stackrel{\mathrm{iid}}\sim N(0,1),\quad \ell=1,2.
                                                               \tag{2.2}
\]

No coupling across different widths is part of the model.  A common coupling
may be introduced in a proof only if it preserves these laws.

At the current state, with all scalar functions applied coordinatewise, set

\[
\begin{aligned}
 Z_{1,n}&=u_n,&X_{1,n}&=\phi(u_n),\\
 Z_{2,n}&=G_{1,n}X_{1,n},&X_{2,n}&=\phi(Z_{2,n}),\\
 Z_{3,n}&=G_{2,n}X_{2,n},&X_{3,n}&=\phi(Z_{3,n}),\\
 D_{\ell,n}&=(1+Z_{\ell,n}^2)^{-1},&&\\
 B_{3,n}&=A_nD_{3,n},&R_{2,n}&=G_{2,n}^*B_{3,n},\\
 B_{2,n}&=D_{2,n}R_{2,n},&Q_{1,n}&=G_{1,n}^*B_{2,n}.
\end{aligned}                                             \tag{2.3}
\]

The predictor, residual, and raw tangent kernel are

\[
 f_n=\langle A_n,X_{3,n}\rangle_{3,n},\qquad
 e_n=y_\star-f_n,                                      \tag{2.4}
\]

\[
\boxed{
K_n=\|X_{3,n}\|_{3,n}^2
+\|B_{3,n}\|_{3,n}^2\|X_{2,n}\|_{2,n}^2
+\|B_{2,n}\|_{2,n}^2\|X_{1,n}\|_{1,n}^2
+\|D_{1,n}Q_{1,n}\|_{1,n}^2.}                       \tag{2.5}
\]

The parameter metric is part of the model: \(A_n,u_n\) use the normalized
Hilbert metrics and \(G_{1,n},G_{2,n}\) use the ordinary Frobenius metric.
All blocks are trained simultaneously by exact continuous gradient flow for
the full loss

\[
\mathcal L_n=(y_\star-f_n)^2                           \tag{2.6}
\]

at learning-rate multiplier \(\eta\), with no clipping, regularization,
momentum, stopping, or width-dependent rescaling.

Define

\[
\Theta(u)=u+\frac{u^3}{3},\qquad r_n=\Theta(u_n),
\qquad P_{\ell,n}=G_{\ell,n}-G_{\ell,0,n}.             \tag{2.7}
\]

Then the exact physical equations are

\[
\boxed{
\begin{aligned}
 \dot A_n&=2\eta e_nX_{3,n},&
 \dot r_n&=2\eta e_nQ_{1,n},\\
 \dot P_{1,n}&=2\eta e_n(B_{2,n}\otimes_nX_{1,n}),&
 \dot P_{2,n}&=2\eta e_n(B_{3,n}\otimes_nX_{2,n}),\\
 \dot e_n&=-2\eta e_nK_n.
\end{aligned}}                                         \tag{2.8}
\]

At finite width \(e_n(0)=y_\star-f_n(0)\), not \(y_\star\).  Equation
\(K_n=Df_n[V_n]\) refers to the unit feature-ascent vector field \(V_n\);
in physical time \(\dot f_n=2\eta e_nK_n\).  The variable \(r_n\) is an
invertible analytic coordinate for the original \(u_n\)-gradient flow, not
a newly metrized trainable parameter.

For one sample, replacing the literal first-layer weight by its preactivation
\(u_n\) is an exact reduction after unit-normalizing the input; orthogonal
first-layer directions never affect the loss.  It is not a frozen-layer
substitution.

## 3. Immutable joint pointed-action source

Before choosing \(y_\star,\eta,T\), or a trajectory, fix a countable typed
source language \(\mathscr L_0\).  It has three coordinate sorts and contains

1. the endpoint Gaussian marks \(a_0,u_0\), the mark
   \(r_0=\Theta(u_0)\), and constants;
2. two labeled actions \(\gamma_1,\gamma_2\) and repeated uses of their same
   labeled transpose orientations;
3. rational linear combinations with coefficients formed from earlier
   normalized moments;
4. a fixed countable pseudo-Lipschitz coordinate-function core containing
   every model map in (2.3), \(\Theta\), its inverse \(\iota\), rational
   cutoffs, and a convergence-determining bounded-Lipschitz family; and
5. normalized inner products and coordinate empirical tests.

Every source program is a finite syntax tree.  The language contains no
label, learning rate, time, current state, trajectory, state-dependent syntax,
digit decoder, arbitrary Borel oracle, or infinitely deep program.

The theorem must construct the deterministic full-sequence projective master
law of all fixed finite \(\mathscr L_0\)-programs under (2.2), and faithfully
realize it as

\[
\mathfrak G=(H_1,H_2,H_3;\mathcal A_1,\mathcal A_2,\mathcal A_3;
             a_0,r_0,\Gamma_1,\Gamma_2),               \tag{3.1}
\]

where \(H_j=L^2(\Omega_j,\mathbb P_j)\),
\(\mathcal A_j=L^\infty(\Omega_j)\) supplies the coordinate functional
calculus, and

\[
\Gamma_1:H_1\to H_2,\qquad \Gamma_2:H_2\to H_3       \tag{3.2}
\]

are bounded actions whose transpose program letters extend to their **actual
Hilbert adjoints**.  In particular,

\[
\langle\Gamma_\ell x,z\rangle
=\langle x,\Gamma_\ell^*z\rangle                       \tag{3.3}
\]

on the dense program core and hence everywhere.  The Gaussian spectral-norm
theorem, not moment convergence alone, must justify the bounded extensions.

The finite source is random; its limiting marked law is deterministic; a
concrete probability-space realization is a fixed representative of that
law.  Internal probability coordinates in this representative are not
residual finite-width randomness.  All conclusions must be invariant under
marked probability-algebra/operator isomorphism.  No literal iid infinite
matrix is asserted.

The source is the minimal completion generated by these marks and programs;
unused randomness is quotiented out.  It is accessible only through the
declared coordinate calculus and applications of \(\Gamma_\ell\) and their
true adjoints.  This provenance rule—not an impossible ban on infinite
information in real numbers—excludes trajectory playback and hidden oracles.

## 4. Exact limiting operator IDE

Let \(\iota=\Theta^{-1}\).  The evolving state is

\[
(A,r,P_1,P_2,e)\in H_3\times H_1\times
\mathfrak S_1(H_1,H_2)\times
\mathfrak S_1(H_2,H_3)\times\mathbb R.                \tag{4.1}
\]

Put \(G_\ell=\Gamma_\ell+P_\ell\), \(u=\iota(r)\), and reconstruct all
fields by the typed version of (2.3).  For
\(b\in H_{\ell+1}\), \(x\in H_\ell\),

\[
(b\otimes x)v=b\langle x,v\rangle,qquad
\|b\otimes x\|_1=\|b\|_2\|x\|_2.                    \tag{4.2}
\]

The only admissible limiting equation is

\[
\boxed{
\begin{aligned}
 \dot A&=2\eta eX_3,& \dot r&=2\eta eQ_1,\\
 \dot P_1&=2\eta e(B_2\otimes X_1),&
 \dot P_2&=2\eta e(B_3\otimes X_2),\\
 \dot e&=-2\eta eK,
\end{aligned}}                                         \tag{4.3}
\]

initialized by

\[
(A,r,P_1,P_2,e)(0)=(a_0,r_0,0,0,y_\star).             \tag{4.4}
\]

Here

\[
f=\langle A,X_3\rangle,
\]

and \(K\) is exactly (2.5) with the probability-Hilbert norms.  The theorem
must prove, rather than impose,

\[
f(0)=0,\qquad e=y_\star-f,qquad
\dot f=2\eta eK,qquad
\frac{d}{dt}e^2=-4\eta e^2K.                           \tag{4.5}
\]

The Bochner-integral identities for \(P_\ell\) are equivalent descriptions
of their current values, not extra state.  The future may apply
\(P_\ell(t)\) and \(P_\ell(t)^*\) extensionally; it may not inspect a
time-labeled rank-one decomposition.

## 5. Noncircular solution and restart class

For a compact feature interval \([-S,S]\), define the explicit
middle-tail envelope class \(\mathcal E_S\) by

\[
\begin{aligned}
 &A-a_0\in C([-S,S];L^\infty(H_3)),\qquad
 r\in C([-S,S];H_1),\\
 &P_\ell\in C([-S,S];\mathfrak S_1),\qquad
 \sup_{|s|\le S}\|R_2(s)\|_{\psi_1}<\infty,           \tag{5.1}
\end{aligned}
\]

with all displayed derived fields strongly continuous in the Hilbert spaces
needed by (4.3), and with the integral equations holding.  The Orlicz norm is

\[
\|v\|_{\psi_1}=\inf\{C>0:\mathbb E\exp(|v|/C)\le2\}. \tag{5.2}
\]

This class is fixed from current-state norms and the immutable source.  It is
not defined as a finite-width limit, a cutoff limit, a DMFT solution, or the
particular desired orbit.  The cubic initial mark \(r_0\) is not incorrectly
assumed sub-Gaussian; only the dynamically dangerous field \(R_2\) is assigned
the exponential envelope.

The theorem must prove:

1. a global feature-time solution from the canonical data in every
   \(\mathcal E_S\);
2. uniqueness and Osgood continuous dependence among any two solutions in a
   common bounded \(\mathcal E_S\) envelope;
3. trace-norm absolute continuity of \(P_1,P_2\) and the exact equations;
4. global physical-time existence for every \(y_\star,\eta\); and
5. the restart identity: restricting a solution at any reachable \(t_0\) and
   solving (4.3) in the same explicit envelope with the same source and
   current state reproduces the shifted path.

Thus restartability follows from an explicit autonomous vector field and a
nontrivial uniqueness class, not from matching one precomputed orbit.  The
contract does not demand well-posedness on arbitrary \(L^2\) balls, where
coordinate spikes make the multiplier discontinuous.

An equivalent tail modulus weaker than \(\psi_1\) may replace (5.1) only if
it is frozen before its proof and satisfies the precise Osgood criterion

\[
\omega_S(\delta)=\inf_{L\ge1}\{L\delta+\tau_S(L)\},
\qquad
\int_{0^+}\frac{d\delta}{\delta+\omega_S(\delta)}=\infty,              \tag{5.3}
\]

with \(\tau_S\) an explicit uniform square-tail bound.  A merely qualitative
uniform-integrability assumption is insufficient.

## 6. Current-action topology

Extend \(\mathscr L_0\), once and for all, to a countable current-state
language \(\mathscr L\) by adding the current marks \(A,r,e\), the current
actions \(P_1,P_1^*,P_2,P_2^*\), the exact model coordinate maps, and finite
compositions of all typed operations.  Arbitrary measurable functions,
state-dependent syntax, infinite trees, and history queries remain forbidden.

For every finite same-sort tuple \({\bf U}\) of vector programs, let
\(\mu_n[\mathbf U]\) be its normalized empirical coordinate law and
\(\mu[\mathbf U]\) its law on the corresponding probability space.  Enumerate
all such tuples and all scalar program observables.  Define

\[
d_{\rm act}(S_n,S)=
\sum_{q\ge1}2^{-q-2}\bigl(1\wedge W_2(\mu_n[\mathbf U_q],
                                      \mu[\mathbf U_q])\bigr)
+\sum_{q\ge1}2^{-q-2}\bigl(1\wedge|s_{q,n}-s_q|\bigr)
+d_{\rm nuc}(P_{1,n},P_1)+d_{\rm nuc}(P_{2,n},P_2).    \tag{6.1}
\]

Here \(d_{\rm nuc}\) is not a meaningless cross-space norm difference.  It
enumerates the intrinsic singular values (or equivalently their countable
continuous tests), the trace norm, and the best-rank tails

\[
\tau_m(P)=\sum_{k>m}s_k(P),\qquad m=0,1,\ldots,        \tag{6.2}
\]

while the action programs in the first two sums determine orientation.  The
metric is taken on equality classes of these signatures.  No embeddings of
\(\mathbb R^n\) into \(H_j\), coordinatewise coupling, or operator-norm
convergence of the Ginibre bulk is claimed.

The raw block-gradient energies in (2.5), predictor, residual, and loss are
explicit scalar observables in \(\mathscr L\), but their convergence is also
stated separately below.  This prevents weak empirical convergence from
hiding a one-coordinate square-energy spike.

The nuclear component entails, in particular,

\[
\lim_{m\to\infty}\limsup_{n\to\infty}
\Pr\!\left\{\sup_{t\le T}\tau_m(P_{\ell,n}(t))>\varepsilon\right\}=0,
                                                               \tag{6.3}
\]

and convergence of each fixed intrinsic singular-value test.  Action tests
alone would miss escaping nuclear mass; singular values alone would miss
operator orientation.

## 7. The exact convergence assertion

There exists one source law and one faithful representative (3.1), chosen
independently of all training parameters, such that

\[
\forall y_\star\in\mathbb R\ \forall\eta>0\ \forall T<\infty\
\forall\varepsilon>0:\qquad
\Pr\!\left\{
\sup_{t\in\mathbb Q\cap[0,T]}
d_{\rm act}(S_n(t),S(t))>\varepsilon\right\}\longrightarrow0.          \tag{7.1}
\]

All paths and scalar signatures are continuous, so the rational supremum is
measurable and equals the full time supremum in the induced continuous-path
topology.  The probability is over the raw finite initialization; the limit
signature is deterministic.

In addition, with no clipping, averaging, or renormalization,

\[
\boxed{
\sup_{0\le t\le T}
\left(
|f_n-f|+|K_n-K|+|e_n-e|+|e_n^2-e^2|
\right)\xrightarrow{\mathbb P}0.}                    \tag{7.2}
\]

The final assertion is the direct limit of the exact continuous flows.  A
proof may take ordered limits in meshes, cutoffs, response approximations, or
other auxiliaries, but all such parameters must disappear before (7.1)--(7.2).
No unexplained diagonal sequence is acceptable.

Compact-time constants may depend on \(T,\eta,|y_\star|\), fixed program
complexity, and fixed Gaussian moments.  They may not depend on width, a
realized initialization, an auxiliary mesh or cutoff after it is removed, a
subsequence, or future trajectory data.  No rate and no uniformity in
\(y_\star,\eta,T\) are required.

## 8. Anti-escape clauses

None of the following resolves the contract:

1. freezing or stopping gradients through any of \(A,u,G_1,G_2\);
2. lazy/NTK linearization, a changed metric, discrete optimizer, or
   width-dependent time rescaling;
3. replacing arctangent, adding residual/skip paths, or adding RMS, layer,
   batch, weight, or spectral normalization;
4. restricting to \(y_\star=0\), small labels, sufficiently small time, or a
   selected initialization event whose probability does not tend to one;
5. refreshing a transpose as an independent Gaussian, changing the source at
   restart, or conditioning it into a new bulk;
6. a source chosen after \(y_\star,\eta,T\), a trajectory, discretization, or
   subsequence is known;
7. retaining a path, time-labeled rank-one list, two-time covariance,
   response kernel, DMFT law, cutoff trajectory, mesh values, or infinite
   moment list as extra final state;
8. predictor-only, fixed-time, finite-time-grid, expectation-only,
   subsequence-only, or clipped-kernel convergence;
9. a topology that ignores \(P_\ell^*\), raw square energies, or escaping
   trace-class mass;
10. a solution class defined by the desired finite-width convergence or a
    proof approximation rather than current-state/source bounds;
11. an unproved propagation-of-chaos, tensor-program, or DMFT statement whose
    conclusion is equivalent to (7.1); or
12. leaving any mesh or cutoff in the final theorem or changing the order of
    the direct \(n\to\infty\) assertion.

Histories, responses, DMFT, cutoffs, and discretizations are permitted as
**proof scaffolding** if they are fully constructed, their hypotheses are
verified, and they are eliminated from the final state and assertion.

## 9. Claim ladder and terminal acceptance

The contract is resolved only if all rungs hold.

| Rung | Required assertion |
|---|---|
| C0 | Exact mixed-metric finite algebra and \(Df_n[V_n]=K_n\) |
| C1 | Full-sequence joint two-matrix source construction with genuine adjoints |
| C2 | Exact autonomous current-state IDE and direct raw readouts |
| C3 | Global canonical existence, envelope uniqueness/continuous dependence, and restart |
| C4 | Tightness and identification of the exact continuous state in the current-action/nuclear topology |
| C5 | Uniform compact-time convergence of every raw block-gradient energy and \(K_n\) |
| C6 | Physical clock and uniform compact-time convergence of \(f_n,K_n,e_n,\mathcal L_n\) |

A candidate proof must independently survive:

- a source/adjoint/provenance reconstruction;
- a middle-tail and raw-square audit;
- a mesh/cutoff/limit-order audit;
- a nuclear-defect and restart audit;
- a line-by-line clean-room proof reconstruction; and
- a search for a reachable iid-Gaussian counterexample or circular lemma.

The strongest concrete falsifier is a canonical iid-Gaussian sequence and a
fixed \(T\) for which \(R_{2,n}\), a raw block energy, or the current-action
state is not tight with nonvanishing probability, or two width subsequences
have incompatible limits.  Failure of bare \(L^2\) Lipschitzness, a cavity
estimate, a tensor-program discretization, or another particular proof route
is only a route falsifier and does not justify changing the architecture.

## 10. Deliberately separate extensions

The following are not required for resolution:

- arbitrary fixed depth \(L>3\) or estimates uniform in depth;
- unequal widths/aspect ratios;
- a general activation class, including scaled arctangent;
- tanh, asinh, softsign, sine, ReLU, or either meaning of leaky arctangent;
- residual/skip networks or architectural normalization;
- multiple samples, biases, vector outputs, or non-Gaussian initialization;
- discrete GD/SGD, rates, fluctuations, or almost-sure convergence; and
- training horizons growing with width or long-time interpolation.

The syntax is nevertheless written layerwise so that a proved one-edge
delocalization/response lemma can later be iterated at any **fixed** depth.
No claim for depth four or general depth is made until that iteration is
separately proved.
