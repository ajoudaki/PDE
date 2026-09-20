# A continuous noisy selector with a unique fitted population state

2026-09-19. Lead proof; internal checks are recorded in README.md. This is a new optimizer for
the exact fixed-order closure, not an implicit-bias theorem for its
ordinary loss gradient flow. Its scientific inputs are this study's
MODEL_AND_GEOMETRY.md, its canonical-feature proof, and the established
book model specified there. No older study result is imported.

## 1. A uniquely defined, data-dependent selection principle

Use h=(w,M), h0=(g,D), A_h, K_h, B_h=A_h* K_h^-1, P_h=I-B_hA_h,
Y_i=sqrt(mu_i)y_i, and J(h)=Y^TK_h^-1Y/2 as defined and derived in
MODEL_AND_GEOMETRY.md. Let sigma=lambda_min K_h0>0, and use that note's
explicit r>0 and C_J, so K_h>=sigma I/2 and grad J is C_J-Lipschitz
on the closed hidden ball ||h-h0||<=2r. Choose once from fixed data
and canonical initialization

\[
 \rho=C_J+1+4J(h_0)/r^2,\qquad
 \omega=\rho-C_J>0,\qquad
 F(h)=J(h)+\frac\rho2\|h-h_0\|^2.                 \tag{1}
\]

The selected hidden state is the minimizer of F on ||h-h0||<=r.
The selected readout is its minimum-norm exact interpolant B_hY.
This says explicitly what is being selected: a small-norm readout
fitting the labels, balanced against deviation of the learned hidden
fields from their canonical initialization. It is one additional
selection principle; finite labels alone do not impose it.

**Existence, uniqueness and interiority.** Integrating the Lipschitz
gradient estimate along a line segment gives

\[
 F(k)\ge F(h)+\langle\nabla F(h),k-h\rangle
                     +\frac\omega2\|k-h\|^2.     \tag{2}
\]

The whole ball is convex, so this inequality holds throughout it.
It implies the midpoint inequality
F((h+k)/2)<= (F(h)+F(k))/2-omega||h-k||²/8.
A minimizing sequence is Cauchy by this inequality: its midpoints
cannot have energy below the infimum. The closed Hilbert ball is
complete and F continuous, so its strong limit attains the infimum.
Two minimizers must coincide. Call the minimizer h_*.

On the boundary, F>=rho r²/2>J(h0)=F(h0), because J>=0.
Thus h_* is interior and grad F(h_*)=0, by testing small variations
in every direction. Its definition uses only fixed known functions
and data; the algorithm below never requires h_* as an input.

The same argument shows that F(h)<=F(h0) implies

\[
 \|h-h_0\|\le\sqrt{2J(h_0)/\rho}<r/\sqrt2.        \tag{3}
\]

In particular the sublevel lies strictly inside the region of proved
Gram positivity and regularity. From (2), for h in that region,

\[
 F(h)-F(h_*)\ge\frac\omega2\|h-h_*\|^2,
 \quad \|\nabla F(h)\|^2\ge2\omega[F(h)-F(h_*)].   \tag{4}
\]

For the second inequality put k=h_* in (2) and complete the square
in k-h. Thus no assumed convexity of the original loss or global
hidden objective is involved.

## 2. Explicit noise and evolving-feature transport

For any real Hilbert space and vector v define the bounded operator

\[
 T(v)u=\frac{\|v\|^2u-v\langle v,u\rangle}
                 {1+\|v\|^2}.                   \tag{5}
\]

It is locally Lipschitz, <v,T(v)u>=0, and
||T(v)||<=||v||²/(1+||v||²)<=||v||/2.
This includes v=0, where T=0. The first bound follows by decomposing
u parallel and perpendicular to v; the second is 2||v||<=1+||v||².

Fix a positive physical refresh interval. At each refresh independently
draw bounded symmetric directions U in the hidden Hilbert space and Z
in R^m, each of norm at most one, and hold them fixed until the next
refresh. For example use random signs on a declared finite set of unit
fields of the frozen marks and finite matrix directions, and coordinate
directions in R^m. This introduces no unrecorded neuron marks. Let nu_h,
nu_e>=0 and gamma>0 be fixed. All noise conclusions below hold for
every such bounded direction path, not merely almost surely.

Write G=grad F(h), e=A_h c-Y and q=P_hc. Define the hidden and residual
velocities

\[
 V_h=-G+\nu_h T(G)U_t,
 \qquad V_e=-\gamma e+\nu_e T(e)Z_t.              \tag{6}
\]

At the current state evaluate dot B=D_hB_h[V_h] and
dot P=D_hP_h[V_h]. The actual state equation is

\[
 \dot h=V_h,
 \qquad
 \dot c=\dot B(Y+e)+B_hV_e+\dot P q-\gamma q.     \tag{7}
\]

Every term is a current-state population contraction, finite matrix
solve or derivative of one. B and P depend on the moving hidden
fields; the dot B and dot P terms are essential. Omitting them
would change the residual and invalidate the proof.

The initial state is exactly canonical: h=h0, c=0, hence e=-Y,
q=0. In that case q stays zero, so the last two terms vanish along
the initialized trajectory. They are retained to give an actual
full-state rule and control extra readout directions at a restart.
The rule does not reset c to an already fitted readout: its residual
starts at -Y and evolves continuously by (6).

The gradients of F use the original hidden L2/Frobenius metric, with
the true M transpose, but (7) is explicitly a changed optimizer. The
readout is transported with the moving feature space; (6) is not the
original hidden loss gradient. There is no claim of an arbitrarily
small perturbation of original GF as rho or noise varies.

## 3. Why these are the actual residual and null directions

Equivalently solve (6) together with

\[
 \dot q=\dot P q-\gamma q,\qquad c=B_h(Y+e)+q.    \tag{8}
\]

Differentiating P²=P gives P dot P P=0. Let u=(I-P)q. Equation
(8) gives u'=-P dot P u-gamma u. Since u(0)=0, the integral
equation and its norm Lipschitz bound give u=0 uniquely. Thus q=Pq
and Aq=0 for all times. Because AB=I and PB=0, the reconstructed
readout satisfies Ac-Y=e and Pc=q. Differentiating its definition
is exactly (7). Conversely any solution of (7) has this representation:
the map (h,c)->(h,Ac-Y,Pc) has inverse (8) on the constraint q=Pq,
and the chain rule or local uniqueness identifies its evolution.

Also <q,dot P q>=0, so

\[
 \frac d{dt}|e|^2=-2\gamma|e|^2,\qquad
 \frac d{dt}\|q\|^2=-2\gamma\|q\|^2,
 \frac d{dt}F(h)=-\|\nabla F(h)\|^2.             \tag{9}
\]

The stochastic terms vanish in these identities by their pointwise
orthogonality. This is a colored random ODE, not a Brownian equation;
there is no missing quadratic-variation term. The equalities hold
almost everywhere, with continuous states across refresh times.

In particular the actual unhalved training loss, not a surrogate, is

\[
 L(t)=L(0)e^{-2\gamma t}.                         \tag{10}
\]

At least for m>=2 and nu_e>0, choosing independent random signed
coordinate directions produces nonzero residual noise with positive
probability whenever e!=0: no nonzero vector is parallel to every
coordinate direction. Thus different realizations can have different
intermediate training predictions while sharing the endpoint below.

For a genuinely random state process for every merged data count m>=1,
take nu_h>0 and nu_e>0, draw U uniformly from the signed pairs of two
fixed orthonormal middle-matrix directions, and draw Z from signed
coordinate directions. The preceding argument covers m>=2. For m=1,
write z0=b2^T D a_g(x1). Positive K_h0=E2[tanh²(z0)] implies

 DK_h0[(0,D)]=2 E2[z0 tanh(z0) sech²(z0)]>0.

Differentiation is justified by bounded marks and bounded initialized
preactivation. Since J=1/(2K) for this single binary constraint,
DJ(h0)[(0,D)]<0 and G(h0)=grad J(h0)!=0. At least one of the two
orthonormal matrix directions is not parallel to this nonzero G(h0).
Its signed pair gives distinct values of T(G(h0))U and hence distinct
initial hidden velocities with positive probability. This covers the
one-constraint case without relying on its identically zero scalar
residual tangent noise. The convergence conclusions also hold for
zero noise amplitudes as deterministic special cases.

## 4. A potential with exactly one zero in the declared domain

On ||h-h0||<=r, define

\[
 \Phi(S)=F(h)-F(h_*)+L(S)+\|P_hc\|^2.            \tag{11}
\]

This depends on current state and the fixed variational problem (1).
The additive constant F(h_*) need not be evaluated by the algorithm.
It is a well-defined infimum over a fixed input-defined ball, whose
attainment and uniqueness have been proved independently of the flow.

The potential is nonnegative, dominates L, and vanishes if and only if

\[
 h=h_*,\qquad c=B_{h_*}Y.                        \tag{12}
\]

Indeed the three nonnegative terms force h=h_*, e=0 and q=0, and
the decomposition (4) of MODEL_AND_GEOMETRY gives exactly (12).
Thus it selects one population state on the canonical mark carrier,
not merely the whole set of training interpolants.

Combining (4) and (9) gives the pathwise inequality

\[
 \dot\Phi=-\|\nabla F\|^2-2\gamma(L+\|q\|^2)
 \le-2\min\{\omega,\gamma\}\Phi.                 \tag{13}
\]

All terms from the moving feature geometry have been included in (7)--(9).
The potential's coercivity is not supplied by a metric that collapses:
with d=||h-h_*||,

\[
 \|c-B_{h_*}Y\|
 \le C_B d+\sqrt{2/\sigma}|e|+\|q\|,
 \quad d\le\sqrt{2\Phi/\omega}.                 \tag{14}
\]

Hence the physical state distance to (12) is at most C sqrt(Phi),
with a finite explicit constant obtained from (14) and |Y|=1.
The original physical distance converges exponentially with exponent
min{omega,gamma}, for every allowed noise realization.

## 5. Global existence and uniqueness of the process

On ||h-h0||<2r, all operators and derivatives used in (6)--(8) are
locally Lipschitz by MODEL_AND_GEOMETRY. For each held direction path,
the integral map is a contraction on sufficiently short bounded
continuous-path balls; this proves local existence and uniqueness.
The same estimates are uniform on the smaller balls and bounded
e,q sets used below. There are only finitely many noise switches on
each finite interval, and paths are joined continuously.

Before any possible exit, (9) gives F<=F(h0); therefore (3) keeps h
strictly inside the certified Gram-positive ball. The residual and
q norms are bounded by their initial norms. By (9) and bounded grad F,
V_h and V_e are bounded there. DB and DP are bounded, so (8) and (7)
give bounded velocities on every finite interval. Cauchy endpoints
exist in the complete Hilbert spaces at finite maximal times; their
states remain in the larger open existence domain. Local existence
then continues them. This excludes finite-time blowup or Gram loss.

Equations (13)--(14) prove strong convergence of the complete state
to (12). They also give finite total travel: grad F(h_*)=0 and its
Lipschitz bound imply ||V_h||<=C||h-h_*||, while ||V_e||<=C|e|;
the dot P q and dot B(Y+e) terms have the same integrable exponential
upper bounds. Thus the law characteristics have finite physical
length and a finite strong endpoint. No compactness of Hilbert balls,
state convergence assumption, future endpoint or inverse-Gram moment
condition was inserted.

The full state is restartable from its saved populations, M, fixed
selection parameters, and current noise value/refresh phase. The
noise directions are fields of the existing frozen marks. The
population law velocities therefore require no additional evolving
neuron coordinate or erased joint correlation.

## 6. The selected function and the scope of uniqueness

The deterministic selected predictor is explicitly characterized by

\[
 f_*(x)=\sum_{i=1}^m\sqrt{\mu_i}
     (K_{h_*}^{-1}Y)_i E_2[H_{h_*}(x_i)H_{h_*}(x)].\tag{15}
\]

It fits every training label. The features are evaluated at the unique
learned hidden optimizer h_* of (1), not frozen at initialization.
Changing labels generally changes this hidden variational problem.
If h0 already minimizes it, no hidden movement is forced; no theorem
claims every dataset requires strictly positive feature displacement.

On any bounded set of query inputs, direct subtraction of (1) in the
model note bounds predictor differences by C times physical state
distance on this bounded state region. Thus (14) implies uniform
exponential convergence f_t->f_* on the entire normalized circle,
and locally uniformly on R2. The limit is independent of all allowed
optimization noise realizations. No query label or held-out location
is used in the training rule. A mesh is unnecessary once this uniform
state-to-predictor bound is supplied; PASSIVE_LIMITS.md gives its full
derivation and distinguishes its weaker per-run implication.

The guarantee is unconditional from canonical p=1 initialization once
the book-derived positive-Gram theorem is established for the stated
finite compatible data; all optimization constants are explicit input
quantities. The proof does impose a strong hidden anchor and keeps the
hidden fields in a certified neighborhood by its selection objective.
It proves uniqueness for this chosen rule, not uniqueness among every
zero-loss closure state, agreement of different selection parameters,
or uniqueness of the original GF/noisy-loss-GF endpoint. No rho->0,
all-p, finite-width, numerical complexity or finite-step claim is made.
