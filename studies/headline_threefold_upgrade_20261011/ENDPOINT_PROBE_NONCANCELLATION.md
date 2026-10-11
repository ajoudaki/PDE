# A trained probe has infinitely many surviving sphere modes

2026-10-11. Scoped first-round theoretical result. No experiments, paper edits,
or Git operations. Scientific inputs were exactly `paper/compact.tex`,
`paper/compact_fitting.tex`, `NONPARALLEL_INITIAL_VARIABILITY.md`, and
`ENDPOINT_SEPARATION_CAVITY.md`. The rigorous-proof, conjecture-investigation,
and canonical-notation skills and their relevant references were applied.

The new result concerns the **compensated infinitesimal cavity influence**,
not the fluctuation of the actual fitted network. Under the original label
cap, its covariance as a function of the sphere query has infinite rank at
every sufficiently regular successful cavity. Such cavities have probability
tending to one. Consequently, at each such cavity, the influence has positive
conditional variance at almost every sphere query. This removes complete
functional cancellation as a possible obstruction for this influence.

It does not prove positivity at every prescribed separated query, a
width-uniform variance bound, or an endpoint dense-copy gap of order
\(n^{-1/2}\). In particular, it does not resolve the singleton-panel target.

## 1. Objects and exact scope

Use the canonical network, zero readout initialization, Gaussian hidden
initialization, and physical gradient flow of the supplied paper. Write
\(v=x/\sqrt d\in S^{d-1}\), with \(m\ge2\), \(L\ge2\),
nonzero labels, and

\[
\lambda=\gamma/m\le1,
\qquad 0<Y=\|y\|/\sqrt m\le\lambda\beta^{-30L}.
\tag{1}
\]

The first-layer and later activations are nonaffine, analytic on the given
strip, and have bounded first derivative there. Their values may be
unbounded. Pairwise nonparallel training directions imply \(d\ge2\), so
the sphere is connected. The proof below uses nonpolynomiality of the last
activation and the original training Gram gap; it does not use a positive
test Schur complement or impose a test-dependent label cap.

Remove one last-hidden-layer neuron, retaining the original width \(n\)
in every denominator. Fix a successful cavity. Let \(\xi(t)\) be its
Euclidean mobility coordinates, \(F_v(\xi)\) its output, and

\[
h_v(t)=h^{(L-1)}(t,v),\qquad
j_v(t)=\nabla_\xi F_v(\xi(t)),\qquad
r_a(t)=F_{v_a}(\xi(t))-y_a.
\]

The cavity has finite parameter dimension \(D\). Its residual RMS is
\(\rho(t)=\|r(t)\|/\sqrt m\). The supplied fitting lemma gives

\[
\rho(t)\le Ye^{-\lambda t/2},\quad
\sup_{t,v}\|h_v(t)\|/\sqrt n\le B:=2H,\quad
H\le(2\beta)^L.
\tag{2}
\]

For an independent Gaussian root \(g\sim N(0,I_n)\), the trained probe
has incoming row \(u(0)=g/\sqrt n\) and readout \(a(0)=0\). In the
coordinates \(U=\sqrt n\,u\) and \(H_a(t)=h_{v_a}(t)/\sqrt n\), its
exact equations are

\[
\begin{aligned}
\dot a&=-\frac2m\sum_b r_b\phi_L(U^\top H_b),\\
\dot U&=-\frac2m\sum_b r_ba\phi_L'(U^\top H_b)H_b,
\qquad U(0)=g.
\end{aligned}
\tag{3}
\]

The cavity note proves existence of the compensated endpoint influence

\[
I_v(g)=a_\infty(g)
 \phi_L\!\left(U_\infty(g)^\top h_v(\infty)/\sqrt n\right)
 +j_v(\infty)^\top V_\infty(g).
\tag{4}
\]

Here \(V\) starts at zero and solves the exact multiplicity derivative
equation

\[
\dot V=-D^2\mathcal L_c(\xi(t))V
 -\frac2m\sum_b\left(b_bj_{v_b}+r_b\nabla_\xi b_b\right),
\qquad
b_b=a\phi_L(U^\top H_b).
\tag{5}
\]

The derivative in \(\nabla_\xi b_b\) holds the current probe variables
fixed. Formula (4) is the limit of the finite-time multiplicity derivative;
no exchange of the multiplicity derivative and the nonlinear fitted limit
is asserted. Each training influence is exactly zero.

For this fixed cavity, \(I_v\) is continuous in \(g\), and has finite
Gaussian second moment. The cavity note's polynomial growth bounds prove
the moment assertion. Continuity follows from finite-time ODE dependence
and locally uniform convergence of the probe and the stable/neutral linear
response: on a compact root set their state and forcing bounds are uniform,
and their endpoint tails are bounded by a common exponentially decaying
function.

## 2. The trained root still parametrizes an open set

This is a quantitative consequence of the original cap, independent of the
query geometry. Put

\[
A=\int_0^\infty2\rho(t)\,dt\le4Y/\lambda,
\qquad K=\beta(1+B)^2.
\tag{6}
\]

Since \(\beta\ge10\) and \(L\ge2\),
\(1+B\le3(2\beta)^L\le\beta^{2L}\), hence

\[
K\le\beta^{5L},\qquad AK\le4\beta^{-25L}<1/4.
\tag{7}
\]

For every root with \(\|g\|\le1\), the upper derivative of
\(s(t)=|a(t)|+\|U(t)\|\) obeys

\[
\dot s\le2\rho K(1+s).
\]

This follows from \(|\phi_L(z)|\le\beta(1+|z|)\),
\(|\phi_L'|\le\beta\), \(\|H_b\|\le B\), and sample
Cauchy--Schwarz. Thus \(1+s\le2e^{AK}<3\). Integrating the first
equation of (3) more directly gives

\[
\sup_t|a(t)|\le2AK.
\tag{8}
\]

Let \(P(t)=D_gU(t)\) and let \(q(t)=D_ga(t)\) be a row vector.
Define

\[
b(t)=\frac2m\sum_b r_b\phi_L'(U^\top H_b)H_b,
\qquad
C(t)=\frac2m\sum_b r_b\phi_L''(U^\top H_b)H_bH_b^\top.
\]

These quantities have bounds \(\|b\|,\|C\|\le2\rho K\).
Differentiating (3) gives

\[
\dot q=-b^\top P,\qquad
\dot P=-bq-aCP,\qquad q(0)=0, P(0)=I.
\tag{9}
\]

The full state Jacobian has operator norm at most
\(2\rho K(1+|a|)\le4\rho K\). Consequently
\(\|P\|,\|q\|\le e^{2AK}<2\), and the first equation improves
the second of these bounds to \(\|q\|\le2AK\). Integrating the
second equation now yields

\[
\sup_t\|P(t)-I\|
\le A\left(K(2AK)+(2AK)K\cdot2\right)
=6(AK)^2<1/2.
\tag{10}
\]

All differentiated coefficients are integrable, so \(P(t)\) converges
locally uniformly in the root ball. Therefore
\(D_gU_\infty=P(\infty)\), and (10) shows that
\(g\mapsto U_\infty(g)\) is locally invertible throughout
\(\|g\|<1\). In particular its image contains an open set.

The endpoint map \(g\mapsto a_\infty(g)\) is real analytic on all
of \(\mathbb R^n\). Here an infinite-time assertion needs justification.
For a fixed real root, (3), linear activation growth, and finite \(A\)
bound the real state on the whole half-line. A sufficiently small complex
neighborhood of that root stays in a bounded state neighborhood and keeps
all \(U^\top H_b\) inside the activation strip: the complex difference
estimate is a Gronwall estimate with integrable coefficient \(C\rho(t)\).
The same estimate supplies one neighborhood for all times. The holomorphic
finite-time solutions converge uniformly there, since their derivatives
in time are bounded by \(C\rho(t)\). Cauchy's integral formula, passed
through this uniform limit, proves holomorphy of the endpoint. Restriction
to real roots proves the assertion.

This analytic function is not identically zero. Indeed, initialize the
probe at \(g=\sqrt n\,W^{(L)}_{j,:}(0)^\top\) for any retained
top neuron \(j\). Equation (3) then exactly reproduces that cavity
neuron's incoming row and readout, by uniqueness. Since the cavity fits
\(y\ne0\), some retained readout coordinate has a nonzero fitted value.
For its root, \(a_\infty(g)\ne0\).

A nonzero real-analytic function on connected \(\mathbb R^n\) cannot
vanish on the entire root ball. There is therefore an open ball inside
\(\|g\|<1\) on which \(a_\infty\ne0\) and
\(g\mapsto U_\infty\) is a diffeomorphism onto an open set. The
same complex-neighborhood argument proves real analyticity of
\(U_\infty\). Its Jacobian determinant is nonzero on the unit ball by
(10), and hence is a nonzero real-analytic function. The zero-set theorem
therefore gives, for Gaussian-almost every root,

\[
a_\infty(g)\ne0,\qquad \det D_gU_\infty(g)\ne0.
\tag{10a}
\]

This is qualitative: neither the readout magnitude nor the smallest
Jacobian singular value has a width-uniform lower bound here. The particular
unit-ball chart can also have extremely small Gaussian probability as width
grows.

## 3. The trained lower feature map remains rich on the sphere

We next prove that, with probability tending to one, the map

\[
v\longmapsto h_v(\infty)\in\mathbb R^n
\tag{11}
\]

takes arbitrarily many pairwise nonparallel nonzero values on every
nonempty open sphere patch. This uses a pair of auxiliary sphere queries,
not the user's prescribed test, and is only a sphere-domain argument.

Let \(s\ge1\) bound \(|\phi_L'|\), with \(s\le\beta\), and
put \(q_0=Q^{(L-1)}(v,v)\), which is independent of the unit direction
\(v\). For two distinct training indices \(a,b\), the last-layer
population gap implies

\[
\begin{aligned}
\gamma
&\le Q^{(L)}_{aa}-Q^{(L)}_{ab}\\
&=\tfrac12\mathbb E[\phi_L(Z_a)-\phi_L(Z_b)]^2
\le s^2\left(q_0-Q^{(L-1)}(v_a,v_b)\right).
\end{aligned}
\tag{12}
\]

Here the first inequality tests \(Q^{(L)}\succeq\gamma I\) on
\((e_a-e_b)/\sqrt2\). Covariance Cauchy--Schwarz also gives
\(\gamma\le2s^2q_0\). Set \(\kappa=\gamma/(4s^2)\le q_0/2\).
Along a continuous sphere path from \(v_a\) to \(v_b\), continuity
of the population kernel gives a deterministic direction \(v_*\) with

\[
Q^{(L-1)}(v_a,v_*)=q_0-\kappa.
\]

The corresponding two-query population Gram has smallest eigenvalue
\(\kappa\). The finite-query initialization argument in the supplied
fitting proof therefore gives, with probability tending to one,

\[
\sigma_{\min}\!\left(
 [h_{v_a}(0),h_{v_*}(0)]/\sqrt n\right)
\ge\sqrt{\gamma/(8s^2)}.
\tag{13}
\]

This event concerns two fixed deterministic directions. The top-neuron
cavity has the same lower-layer initialization. The fitting displacement
bound gives, at each of these queries,

\[
\|h_v(\infty)-h_v(0)\|/\sqrt n
\le\varepsilon:=8F_{L-1}Y^2/\lambda^{3/2}.
\tag{14}
\]

The fitting coefficients satisfy \(F_{L-1}\le F_L=F\) and
\(8H\sqrt F\le\beta^{5L}\), with \(H\ge1\). Thus (1) implies

\[
\varepsilon\le\tfrac18\sqrt\lambda\,\beta^{-50L}
<\frac{\sqrt\gamma}{8s}.
\tag{15}
\]

The two-column perturbation has operator norm at most
\(\sqrt2\varepsilon\). Subtracting this from (13) leaves a positive
smallest singular value. Hence \(h_{v_a}(\infty)\) and
\(h_{v_*}(\infty)\) are linearly independent.

For fixed endpoint parameters, (11) is real analytic on the connected
sphere: it is a finite composition of real-analytic activations and linear
maps. If its nonzero values on an open patch belonged to finitely many
lines, the closed preimages of those lines would cover the patch. At least
one would contain an open subpatch. All linear equations defining that
line, composed with (11), would then vanish there and, by analytic
continuation on the sphere, everywhere. This contradicts the two independent
values just proved. Therefore every open patch contains arbitrarily many
pairwise nonparallel nonzero feature values.

The initialization event (13) and the supplied cavity fitting event have
joint probability tending to one. No additional label restriction was used.

## 4. Infinite rank survives the exact compensation

We first record the required ridge-function fact with its proof. Let
\(z_1,\ldots,z_N\in\mathbb R^n\) be nonzero and pairwise nonparallel.
For a nonpolynomial real-analytic \(\phi\), the functions
\(U\mapsto\phi(U^\top z_i)\) are linearly independent on every
nonempty open subset of \(\mathbb R^n\).

To see this, a linear relation on an open set analytically continues to
all real \(U\). Choose a nonzero Taylor coefficient of \(\phi\) of
degree \(k\ge N-1\); such degrees are unbounded. Its homogeneous term
gives \(\sum_i c_i z_i^{\otimes k}=0\). For each \(i\), choose
linear forms \(\ell_{ij}\) vanishing at \(z_j\), nonzero at
\(z_i\), for \(j\ne i\), and a linear form \(\ell_i\) nonzero
at \(z_i\). Contract with the coefficient tensor of

\[
\prod_{j\ne i}\ell_{ij}(z)\,\ell_i(z)^{k-(N-1)}.
\]

Only the \(i\)th term survives and its multiplier is nonzero. Therefore
all \(c_i=0\). The last activation is nonpolynomial because an analytic
polynomial with bounded real derivative would be affine.

Fix any nonempty open sphere patch. By Section 3 choose arbitrarily many
directions \(v_i\) there with pairwise nonparallel feature vectors
\(z_i=h_{v_i}(\infty)/\sqrt n\). Section 2 supplies a root chart
with nonzero \(a_\infty(g)\) and open image under \(U_\infty(g)\).
The preceding ridge-function fact shows that the direct contributions

\[
g\longmapsto
a_\infty(g)\phi_L(U_\infty(g)^\top z_i)
\tag{16}
\]

are linearly independent, for arbitrarily large collections of directions.
Indeed one divides a proposed relation by \(a_\infty\) on this chart
and changes variables to \(U_\infty\). Continuity and full support of
the Gaussian measure make this independence valid also in
\(L^2(N(0,I_n))\).

The compensation in (4), as \(v\) varies, belongs to the span of the
\(D\) scalar functions \(g\mapsto[V_\infty(g)]_k\). Centering
additionally removes only the constant function of \(g\). Subtracting a
finite-dimensional space from the infinite-dimensional span in (16) cannot
leave a finite-dimensional span. We obtain the following exact conclusion.

**Conditional sphere covariance theorem.** At every cavity satisfying the
fitting bounds and (13), the centered influences

\[
\left\{I_v-\mathbb E_g I_v:
      v\text{ in any nonempty open sphere patch}\right\}
\tag{17}
\]

span an infinite-dimensional subspace of \(L^2(N(0,I_n))\). Equivalently,
the conditional covariance kernel

\[
\operatorname{Cov}_g(I_v,I_{v'})
\tag{18}
\]

has infinite rank on every such patch. In particular, for each finite
integer \(N\), some \(N\) queries in that patch have a strictly
positive-definite influence covariance matrix. Those query choices may
depend on the fixed cavity.

There is also a qualitative almost-everywhere consequence. Infinite rank
gives roots \(g_1,g_2\) for which
\(v\mapsto I_v(g_1)-I_v(g_2)\) is not identically zero. This function
is real analytic on the sphere directly from (4), with the endpoint
parameters and the two response vectors held fixed. No analyticity of an
infinite-time limit in the query is needed beyond this finite endpoint
formula. Its zero set has surface measure zero, by the real-analytic
zero-set argument recalled in the supplied initial-variability note.
At any point outside that zero set, continuity in \(g\) and full
Gaussian support give

\[
\operatorname{Var}_g(I_v)>0.
\tag{19}
\]

This proves (19) for almost every query at each fixed successful cavity.
It does not identify the exceptional set with the training directions or
their antipodes. Training queries do belong to it, by exact fitting.

## 5. Audit, status, and remaining gap

The mechanism is finite-dimensional compensation versus infinite ridge
rank. It handles both the endpoint kernel projection and the tangent-memory
term because both are included in the single response vector in (4). It
does not discard hidden-feature training or condition on a future transcript
of the full network. The Gaussian root remains independent of the cavity.

The following distinctions are essential.

| Claim | Status |
| --- | --- |
| Probe endpoint has an open incoming-root chart with nonzero readout | Proved under the original cap and a successful fitting cavity |
| Trained lower-feature image is nonparallel-rich on each sphere patch | Proved on an additional two-query initialization event of probability tending to one |
| Compensated sphere influence covariance has infinite rank | Proved on these events |
| Its conditional variance is positive at almost every query for each cavity | Proved; the exceptional set is not identified |
| Positivity at every fixed separated query | Open |
| Width-uniform positive influence variance at a useful sphere query | Open |
| Actual fitted-network fluctuation of order \(n^{-1/2}\) | Open |

Infinite rank does not control eigenvalue sizes. The tangent dimension grows
with width, and almost-everywhere invertibility of the probe map supplies no
uniform bound on its smallest singular value or on the readout magnitude.
The surviving covariance eigenvalues can in principle tend to zero.
For example, multiplying any fixed infinite-rank analytic random function
by \(e^{-n}\) preserves all qualitative rank and zero-set conclusions while
destroying the desired fluctuation scale. This is a logical warning about
what rank proves, not a counterexample to the canonical model.

Nor does the result transfer an infinitesimal insertion to the fluctuations
from order \(n\) fully inserted neurons. A width-accurate insertion or
replacement expansion and a collective small-ball argument remain necessary.

The route is therefore **proved qualitative noncancellation on the sphere;
open at the quantitative fluctuation step**. A useful next development would
be a width-uniform lower bound on a bounded-complexity sphere functional of
(4). Restating fixed-query initial rank does not supply such a bound. The
present result specifically rules out the stronger claim that training can
cancel the probe's dependence on its root as an entire function of the
query.

The fresh isolated reconstruction is
`ENDPOINT_PROBE_NONCANCELLATION_CHECK.md`. It accepted these qualitative
claims, not the unresolved dense endpoint theorem. After that frozen review,
only the missing backslash in the singular-value display (13) was corrected.
