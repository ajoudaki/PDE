# Independent check of the three circle routes

2026-10-11. Bounded isolated mathematical audit of the complete
`CIRCLE_TRANSPORT_ROUTE.md`, `CIRCLE_FOURIER_ROUTE.md`, and
`CIRCLE_ADVERSARIAL_ROUTE.md`. The substantive dependency inputs read were
`paper/compact.tex`, `paper/compact_fitting.tex`,
`ENDPOINT_SEPARATION_CAVITY.md`, and
`ENDPOINT_PROBE_NONCANCELLATION.md`. The authorized structure note was
searched for dependency context but its results were not used. No study
README, history, review report, other study, experiment, candidate edit,
manuscript edit, or Git operation was used. The rigorous-mathematics and
canonical-notation skills, including the neural-network reference, were
applied.

**Verdict.** The three concrete partial arguments reconstruct, with one
dependency qualification required in the transport and Fourier notes. None
proves or disproves the actual two-network circle endpoint bound
\(c_\delta/\sqrt n\) under the full stated assumptions. The Fourier theorem
proves that bound only under its explicit additional local-limit hypothesis.

## 1. Required qualification of the cited probe result

The transport note, lines 259–260, and the Fourier note, lines 306–307,
attribute infinite covariance rank to **each successful cavity**. The cited
probe theorem is narrower: `ENDPOINT_PROBE_NONCANCELLATION.md`, lines
354–355, requires both successful fitting and its additional two-query
initialization event (13). That event supplies a lower-feature singular-value
bound used to preserve two independent feature values through training.

The faithful statement is: infinite covariance rank holds at every cavity
satisfying the fitting bounds **and the probe note's event (13)**. Their
intersection has probability tending to one. This qualification does not
affect the transport upper bounds or the Fourier conditional theorem, which
do not depend on infinite rank. It does not resolve any quantitative endpoint
gap either.

## 2. Gaussian training paths and the transport differential

Fix the cavity independently of its Gaussian root \(g\sim N(0,I_n)\).
Write \(H_a(t)=h^{(L-1)}(t,v_a)/\sqrt n\). The fitting coefficients give
\(\sup_{a,t}\|H_a(t)\|\le B\) and
\(\int_0^\infty\|\dot H_a(t)\|\,dt\le V\), with \(B,V\)
independent of width. The feature-velocity recurrence is consistent with
the supplied flow and its original normalizations.

For \(M=\max_a\sup_t|g^\top H_a(t)|\), absolute continuity gives

\[
\sup_t|g^\top H_a(t)|
\le |g^\top H_a(0)|+
\int_0^\infty|g^\top\dot H_a(t)|\,dt.
\]

Minkowski's inequality and the one-dimensional Gaussian moment formula
therefore give \(\|M\|_p\le m^{1/p}c_p(B+V)\), where
\(c_p=(\mathbb E|N(0,1)|^p)^{1/p}\). The normalized measure of initial
vectors and path velocities used in the note is legitimate after omitting
zero vectors. Jensen's inequality then gives
\(\mathbb E e^{cM}\le2e^{c^2D^2/2}\) for
\(D=\sum_a(\|H_a(0)\|+\int\|\dot H_a\|)\); the case \(D=0\)
is handled separately. Neither estimate uses the Euclidean size of \(g\).

The probe equations and both displacement estimates follow with
\(k=K\int_0^\infty2\rho(t)\,dt\), where
\(\rho=\|r\|/\sqrt m\) and \(K=\beta(1+B)^2\):

\[
\sup_t(|a|+\|U-g\|)\le2k(1+M),\qquad
\sup_t\|U-g\|\le2k^2(1+M).
\]

For \(P=D_gU\) and \(q=D_ga\), the variational equations in the note
are correct. The derivative of the **vector field with respect to its
state** has block matrix

\[
\begin{pmatrix}0&-b^\top\\-b&-aC\end{pmatrix},
\qquad
\|b\|\le2\rho K,\quad \|C\|_1\le2\rho K.
\]

Its operator norm is at most \(2\rho K(1+|a|)\). This is the intended
meaning of “full state differential” at transport lines 213–214; it is
not a pointwise bound on the flow derivative \(D_g(a,U)\), whose initial
norm is one. With
\(R=\exp\{k[1+2k(1+M)]\}\), the resulting estimates
\(\|P\|_{\mathrm{op}}\le R\), \(\|q\|\le kR\), and

\[
\|P-I\|_1
\le\int_0^\infty
   (\|b\|\|q\|+|a|\|C\|_1\|P\|_{\mathrm{op}})\,dt
\le k^2(3+2M)R
\]

are valid. On each compact root set these integrands have a common
integrable bound. Thus the endpoint derivative exists and the same estimate
holds there. The exponential-moment estimate gives width-independent
moments of this trace-norm bound. It supplies no uniform positive lower
bound on every singular value.

The analytic Fourier-tail example is also correct: after subtracting its
first \(N\) modes, its expected supremum is \(O(2^{-N})\), while its
covariance still has infinite rank on every arc. At
\(N=\lceil\log_2n\rceil\), its supremum is
\(o_{\mathbb P}(n^{-1/2})\). This is a counterexample to the proposed
inference from qualitative properties, not to the canonical network.

## 3. Score identity and Gaussian convolution

The successful-event truncation makes the spatial functional \(X_n\)
bounded. The event is a fixed measurable function of initialization, so
changing its probability under the tilted law creates no extra derivative
term. For the bounded mean-zero, unit-variance row score \(q(g_i)\), put
\(S_n=n^{-1/2}\sum_iq(g_i)\) and
\(T_n(\varepsilon)=\mathbb E_\varepsilon X_n\). Differentiation of the
finite product likelihood gives exactly

\[
T_n'(0)=\sqrt n\,\operatorname{Cov}(X_n,S_n),\qquad
n\operatorname{Var}(X_n)\ge |T_n'(0)|^2.
\]

The stronger hypothesis (8) is substantive: for every fixed real \(h\),
the law under the tilt \(h/\sqrt n\) must satisfy
\(\sqrt n(X_n-b_n)-h\tau\Rightarrow Z\) with the same limit and
\(\tau\ne0\). The likelihood expansion, its bounded second moments,
and the central limit theorem for \(S_n\) justify passing to a joint
subsequential limit \((Z_*,S)\). The resulting identity is

\[
\mathbb E e^{itZ_*+hS-h^2/2}
   =e^{ith\tau}\mathbb E e^{itZ_*}.
\]

Analytic continuation in \(h\) is justified by the Gaussian marginal of
\(S\), even without moments of \(Z_*\). Substitution of \(h=is\)
and then replacement of \(s\) by \(s-t\tau\) proves that
\(Z_*-\tau S\) and \(S\) are independent. Consequently two independent
limit copies have a difference with density at most
\(1/(2\sqrt\pi|\tau|)\). The displayed choice
\(c_\delta=\delta\sqrt\pi|\tau|/2\) leaves sufficient probability
slack for weak convergence and the two fitting failures. The conditional
every-confidence conclusion is correct.

One distinction should remain explicit: the coefficient \(\tau\) in (8)
is a coefficient in a local weak-limit assertion. Identifying it with a
limit of the mean derivatives \(T_n'(0)\) requires additional control
of expectations; that identification is not used by the theorem. The
Bernoulli example correctly demonstrates why a nonzero score susceptibility
or variance bound alone cannot replace (8).

The short comparison with `ENDPOINT_TRANSVERSE_ROUTE.md` was not independently
reconstructed because that file was outside the assigned dependency set.
The score and convolution proofs do not require it.

## 4. Actual-flow rank and generic-label nonconstancy

The local endpoint lemma is justified at fixed width. In Euclidean mobility
coordinates the fitted set has codimension \(m\), because the final
readout-feature block makes \(DF\) surjective. Analytic coordinates
\((r,q)\), with \(r=F-y\), give
\(\dot r=-A(r,q)r\), \(\dot q=B(r,q)r\), with
\(A=(2/m)DFDF^\top\) positive definite at the fitted point.
On a small complex neighborhood its Hermitian part remains positive;
exponential residual decay keeps a smaller starting neighborhood inside
it and gives locally uniform holomorphic convergence of the endpoint map.
The same construction includes labels as parameters. Pulling this map back
through a finite-time flow, a local analytic diffeomorphism, proves
\(\operatorname{rank}D\pi=p-m\) at the original initial condition.

For the zero-readout tangent space \(S\),
\(\dim S=p-n\) and \(\dim\ker D\pi=m\). Thus
\(\dim D\pi(S)\ge p-n-m\). If the passive function differential has
rank \(r_A\), its kernel has dimension \(p-r_A\), yielding the claimed
lower bound \(r_A-n-m\) on the restricted endpoint-function derivative.
The identity theorem makes \(r_A\) identical on every nonempty arc and
on the circle. The hypotheses do not establish \(r_A>n+m\).

The generic-label theorem's construction also checks out. A nonaffine
analytic activation with bounded real derivative is nonpolynomial.
For \(m+1\) pairwise nonparallel planar directions, a nonzero Taylor
degree \(k\ge m\) and a Vandermonde argument prove first-layer population
Gram positivity. Positive definiteness propagates through the subsequent
Gaussian layers by full support and nonconstancy of each activation.
The fitting proof's finite-panel Gram convergence therefore supplies the
strict initialization event needed for the augmented penultimate matrix.

A top-row perturbation orthogonal to all training penultimate features
keeps the initialized training matrix \(H\) fixed and changes a passive
feature. For the label direction \(\bar y\), at least one component of
\(a=H(H^\top H)^{-1}\bar y\) is nonzero. Perturbing that row produces
a nonzero change in the exact zero-label endpoint derivative
\(h_0^{(L)}(v_*)^\top a\). This derivative is obtained from the actual
flow: first-order hidden motion is zero, and the readout derivative solves
the stated linear system. No fixed positive-label flow has been replaced
by frozen-feature training.

The difference between the two actual endpoints is analytic on a neighborhood
of the compact admissible label interval. At its upper endpoint, this local
extension follows from the endpoint lemma, so no additional global label
cap is needed. Its derivative at zero is nonzero; hence its zeros in the
interval form a finite set. Off that set, the endpoint map is nonconstant
on the connected open ball of strict fitting initializations. Real-analytic
level sets have measure zero, and the ordinary hidden Gaussian law has a
positive density. The conditional scalar endpoint law on that ball is
therefore non-atomic, as claimed.

This establishes only the stated finite-width generic-label result. The
exceptional scales, probability of the witnessing ball, and size of the
variation are uncontrolled as width grows. Neither this result nor the
rank restriction provides the requested uniform fluctuation scale or the
every-confidence bound.

The retained status is: valid partial transport estimates; a valid
conditional fluctuation criterion; valid actual-flow rank and generic-label
nonconstancy statements; one cited-event qualification; and an open
canonical circle endpoint separation theorem.
