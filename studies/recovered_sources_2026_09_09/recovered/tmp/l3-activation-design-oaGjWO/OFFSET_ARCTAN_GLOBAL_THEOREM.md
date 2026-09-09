# A fixed nonlinear activation with a global three-hidden-layer limit

Status: COMPLETE CANDIDATE PROOF, not yet independently audited as a
whole theorem. The numerical response lemma also has an audit pending.
This is the activation-design branch authorized by the user on
2026-09-05. It does not settle the original activation \(\arctan\).

Explicit proof dependencies:

1. OFFSET_ARCTAN_RESPONSE_BOOTSTRAP.md in this directory, current
   SHA256 65579a94f883f1b9f9240430039f334f5b3b663599cd7ab16bb15c35f7bacc43.
2. /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/L3_LOCAL_COMPLETE_PROOF.md,
   SHA256 f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4.
   We use the actual finite-Gaussian proof and common-action construction,
   not its arctangent-only theorem statement. Their activation-dependent
   hypotheses and the required replacements are verified below.

The proof package is this note together with these two explicit
dependencies. No result about a different initialization, an O(1)
initial readout, or a globally Lipschitz uncut vector field is assumed.

## Model and proposed theorem

Use the SINGLE FIXED activation
\[
 \phi(z)=1+\tfrac1{10}\arctan z
\]
in every hidden layer. The coefficient is independent of width, time,
discretization, and approximation accuracy. There is one input, target
one, and width \(n\) in each of the three hidden layers. Set
\[
 h^{(\ell)}=\phi(z^{(\ell)}),\quad
 z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},\quad
 f_n=\frac{(W^{(4)})^T h^{(3)}}n,\quad r_n=f_n-1.
\]
The first preactivation is a vector. Both hidden matrices are \(n\times n\).
The readout \(W^{(4)}\) is the RESCALED vector throughout. The four
initial blocks are independent, with entries
\[
 z^{(1)}_{0,i}\sim N(0,1),\qquad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\qquad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).                           \tag{1}
\]
Define backward fields with the residual excluded:
\[
 \delta^{(3)}=W^{(4)}\phi'(z^{(3)}),\quad
 q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
 \delta^{(2)}=\phi'(z^{(2)})q^{(2)},\quad
 q^{(1)}=(W^{(2)})^T\delta^{(2)},\quad
 \delta^{(1)}=\phi'(z^{(1)})q^{(1)}.
\]
All products of vectors in these formulas are coordinatewise. Exact raw
GD, with \(\eta_n=n^{-2}\), means
\[
 z^{(1)}_{k+1}=z^{(1)}_k-2\eta_n r_{n,k}\delta^{(1)}_k,
\]
\[
 W^{(\ell)}_{k+1}=W^{(\ell)}_k-
  \frac{2\eta_n r_{n,k}}n\delta^{(\ell)}_k(h^{(\ell-1)}_k)^T,
 \quad \ell=2,3,
\]
\[
 W^{(4)}_{k+1}=W^{(4)}_k-2\eta_n r_{n,k}h^{(3)}_k.        \tag{2}
\]
Physical time is \(t=k\eta_n\). Raw parameters are linearly interpolated,
and hidden objects are recomputed from those parameters. At nodes use
right derivatives, with a left derivative at a terminal node of the
observed interval. Finite gradient flow has the right sides of (2)
divided by \(\eta_n\).

The proposed theorem is that, for every fixed \(T<\infty\), the FULL
sequence of both finite algorithms converges jointly, in probability,
uniformly on \([0,T]\), to one autonomous and uniquely restartable
population gradient flow. Its four evolving objects are
\[
 X^{(1)},\quad W^{(2)},\quad W^{(3)},\quad W^{(4)},
 \qquad X^{(1)}=10[Z^{(1)}+(Z^{(1)})^3/3].              \tag{3}
\]
There are three separate fixed neuron probability spaces. Vectors are
square-integrable fields and the two matrix objects are bounded
operators between adjacent spaces; reverse actions are their adjoints.
The initial operators are the joint Gaussian actions constructed below.
Initially \(Z^{(1)}_0\sim N(0,1)\) and \(W^{(4)}_0=0\).
For a rank-one action we mean, explicitly,
\((U\otimes V)B=U\mathbb E[VB]\), with the expectation in its input layer.

The measured convergence includes every fixed finite same-layer list
formed from the current fields, globally Lipschitz coordinate maps,
bounded products, both orientations of both current matrix operators,
and the named backward fields and hidden velocities. Its meaning is
joint empirical-law convergence in \(\mathcal W_2\); continuous tests
of at most quadratic growth therefore converge in empirical average.
Finitely many specified times can be included jointly. There is no
coordinatewise matching across distinct neuron populations.
In particular predictions, residuals, losses, and all four raw kernel
blocks converge uniformly:
\[
 \frac{\|\delta^{(1)}\|_2^2}{n},\quad
 \frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2},\quad
 \frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2},\quad
 \frac{\|h^{(3)}\|_2^2}{n}.                             \tag{4}
\]
For each hidden layer, preactivation and feature path laws converge
in \(\mathcal W_2(C([0,T]))\), and integrated squared velocities
converge. Using the same initialization, finite GD and finite GF also
approach one another in the same-width state distance: the sum of
\(\|\Delta F(z^{(1)})\|_2/\sqrt n\), both matrix operator-norm
differences, and \(\|\Delta W^{(4)}\|_2/\sqrt n\). We do not compare
operator norms across widths or against operators on a different space.

The theorem additionally asserts genuinely moving hidden features in all
three layers, a nonconstant limiting kernel, and a strictly positive best
affine-approximation error for \(\phi\) under each hidden distribution
at every finite physical time. Those are proved in the final section,
not inferred merely from choosing a fixed coefficient \(1/10\).

## Finite-program identification and one common autonomous state

Write \(m=5/6\), \(a=7/6\). Then
\[
 m<\phi<a,\quad0<\phi'\le1/10,\quad |\phi''|\le1/5.
\]
With \(F(z)=10(z+z^3/3)\), \(F'=1/\phi'\), the map \(F^{-1}\)
is globally \(1/10\)-Lipschitz, and
\(\chi=\phi\circ F^{-1}\) is globally \(1/100\)-Lipschitz.
All coordinate maps needed below are continuously differentiable with
bounded first derivatives after bounded factors are smoothly extended
outside their known range. The initial tuple \((Z^{(1)}_0,F(Z^{(1)}_0))\)
has every finite moment. No global Lipschitz assertion about \(F\) as
a root-generating function is needed.

Here is why the finite Gaussian proof in dependency 2 applies to this
activation without an oddness or centering assumption. The first forward
query, for example, has conditional law
\[
 (W^{(2)}_0 h^{(1)}_0)_i\mid h^{(1)}_0
 \sim N(0,\|h^{(1)}_0\|_2^2/n).
\]
Its limiting variance is \(\mathbb E[\phi(G)^2]\), NOT
\(\operatorname{Var}(\phi(G))\). If \(y=Wh\) and the next transpose
input \(u\) depends on \(y\) and independent roots, conditioning gives
\[
 W^Tu=h\frac{y^Tu/n}{\|h\|_2^2/n}
   +\sqrt{\|u\|_2^2/n}\,P_{h^\perp}g,
\]
with fresh standard Gaussian \(g\). The removed projection has
vanishing mean squared norm after division by \(n\). Thus a reused
output is the response forced by previous queries plus the unexplored
Gaussian part; it is not a fresh independent copy of the first query.

For a general fixed finite transcript with old queries \(WV=Y\),
\(W^TU=Q\), the exact conditional residual is
\(P_{U^\perp}\widetilde W P_{V^\perp}\), with the two deterministic
projection terms displayed in dependency 2. Orthogonality removes old
input responses in the new perpendicular query. Gaussian integration
by parts then gives its coefficient as the expected formal source
derivative. This argument uses bounded first derivatives of coordinate
instructions, finite root moments, and uncentered query second moments.
None uses \(\phi(0)=0\), oddness, or \(\phi'=1/(1+z^2)\).
Those hypotheses have all been verified for the new maps above.

Interleaving the two independent matrices is allowed: each new answer
imposes a linear constraint only on the queried matrix, conditional on
the earlier transcript. Their conditional residuals retain independence.
The two directions for each matrix retain their response coefficients.
Singular Gram matrices are handled at FIXED program length by adding a
fresh independent Gaussian root of size \(\epsilon\) to each query
input. The new limiting Gram Schur complement is at least \(\epsilon^2\).
After proving the conditioning formula, finite-program Lipschitz
stability and bounded initial operator norms remove these auxiliary
roots. Gaussian covariance square roots, coordinate expressions, and
their bounded formal derivatives pass continuously to the singular
limit. No growing-program estimate and no continuity of a pseudoinverse
at a rank change is used.

For each fixed smooth clip \(\tau_R\) with \(|\tau_R'|\le1\),
\(\tau_R(q)=q\) on \(|q|\le R\), \(|\tau_R(q)|\le |q|\) and
\(|\tau_R(q)|\le2R\), apply this finite proof to Euler in the
transformed first coordinate, clipping ONLY \(q^{(2)}\) in
\(\delta^{(2)}\). Unroll every trained matrix as its initial matrix
plus its finite rank-one update sum. First freeze the finite empirical
contractions at their causally constructed population expectations.
The resulting oracle has globally Lipschitz coordinate instructions:
the middle clipped factor is bounded, \(|W^{(4)}_k|\le a k\Delta\),
and the top readout factor can be smoothly extended beyond that bound.
Joint empirical-average convergence from the conditioning induction
then makes each oracle contraction error vanish. Finite induction
through the same Lipschitz instructions proves convergence of the
actual empirical-feedback program. These are joint empirical laws,
not assertions that reused finite coordinates are iid.

The resulting scalar system is EXACTLY the one in dependency 1. Its
Gaussian source groups are independent by orientation and matrix;
its covariance formulas are uncentered second moments. Its response
coefficients retain the same-time return
\[
 b^{(2)}_{kk}=
 \mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
 +b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)].
\]
The finite scalar coefficients are proof devices, not additional
externally prescribed fields in the eventual dynamics.

To put all these programs on fixed spaces, use the countable dense
family and finite-union construction in dependency 2, “Common
population action spaces and clipped flows”. Include constants in each
layer, the new coordinate maps above, smooth clips, rational linear
combinations, both orientations of both matrices, and all finite probe
programs required for the named measurements. Their consistent joint
laws define three probability spaces. Gaussian matrix operator norms
are at most 10 with probability tending to one, by the finite-net
Gaussian estimate in that dependency. Thus, on the countable dense
generated probe classes, the limiting actions satisfy
\(\|W^{(\ell)}_0 U\|_2\le10\|U\|_2\), and similarly backwards.
Extend by continuity to the generated \(L^2\) spaces. Finite adjunction
passes in joint empirical averages, so the backwards extensions are
the adjoints. Arbitrary finite additional Lipschitz probes are obtained
by the same countable approximation. There is no activation-specific
step in this construction beyond the inclusion of its coordinate maps.

On these spaces, let \(\Theta=(X^{(1)},W^{(2)},W^{(3)},W^{(4)})\).
Use the population versions of all forward and backward equations, with
\(Z^{(1)}=F^{-1}(X^{(1)})\) and finite transpose replaced by adjoint.
The clipped feature vector field is
\[
 \mathcal V_R(\Theta)=
 ((W^{(2)})^*\delta_R^{(2)},\
   \delta_R^{(2)}\otimes H^{(1)},\
   \delta^{(3)}\otimes H^{(2)},\ H^{(3)}),
\quad
 \delta_R^{(2)}=\phi'(Z^{(2)})\tau_R(q^{(2)}).            \tag{5}
\]
Use the sum of the two vector \(L^2\) norms and two operator norms as
state distance \(d\). Its same-width counterpart is \(d_n\), with each
vector norm divided by \(\sqrt n\). On any feature horizon \([0,S]\)
the readout is bounded pointwise by \(aS\) from zero initialization.
Since \(\phi'\le1\), the coarser bounds
\[
 Q_0=aS,
 \quad R_3=10+aQ_0 S,
 \quad R_2=10+aR_3Q_0 S                              \tag{6}
\]
bound the readout and the operator norms uniformly in the clipping
level. With finite nonzero initial readout of norm at most one after
division by \(\sqrt n\), use \(Q_0=1+aS\).
Also \(\|q^{(1)}_R\|_2\le R_2R_3Q_0\). These bounds hold for every
positive-step Euler prefix with total feature step at most \(S\).
They imply a common vector-field bound \(C_S\).

Forward differences, followed by the top backwards difference with
the reference readout in the gate-difference term, give
\[
 \|\delta^{(3)}(A)-\delta^{(3)}(B)\|_2+
 \|q^{(2)}(A)-q^{(2)}(B)\|_2\le C_S d(A,B),             \tag{7}
\]
whenever the reference readout is pointwise bounded. Its counterpart
requires no pointwise bound on the other readout. Since \(\phi'\) is
Lipschitz and the middle clip is bounded, \(\mathcal V_R\) is Lipschitz
with constant \(C_S(1+R)\) on these paths. The readout integral preserves
its pointwise bound, a closed condition in \(L^2\). Picard iteration
and (6) therefore give a global-in-feature-time fixed-clip flow.
Euler error on \([0,S]\) is at most \(C_{R,S}\Delta\), identically
at finite width on the initial operator-bound event. Thus fixed-mesh
identification followed by \(\Delta\downarrow0\) proves fixed-clip
finite-flow convergence, including finite joint measurement lists.

## Removing the auxiliary clip on the entire interval [0,3/2]

Dependency 1 proves, with all numerical constants explicit and uniformly
over meshes and clipping levels, on \(0\le s\le S=3/2\),
\[
 \sum_{v\le k}|b^{(2)}_{kv}|<9/10,\qquad
 \sum_{v\le k}|b^{(3)}_{kv}|\le3067/3200<1,
\]
\[
 q^{(2)}_k=\zeta^{(2)}_k+\beta_k,
 \quad |\beta_k|\le7/6,
 \quad \operatorname{Var}(\zeta^{(2)}_k)\le(7/40)^2.    \tag{8}
\]
The preceding section discharges its scalar-identification premise for
this activation. Enlarging a fixed deterministic \(K\), (8) implies
\(\mathbb E\exp((q^{(2)}_k)^2/K^2)\le2\).
Fixed-clip Euler convergence, (7), a subsequence converging almost
everywhere, and Fatou pass this bound to every fixed-clip flow time:
\[
 \sup_{R,s\le S}\mathbb E\exp((q_R^{(2)}(s))^2/K^2)\le2. \tag{9}
\]

We give the actual stability step, since merely proving moments would
not resolve the uncut problem. Let \(R'\ge R\), allowing \(R'=\infty\).
Compare a state \(A\) using \(R'\) with a reference \(B\) using \(R\).
Add and subtract to obtain exactly
\[
 \begin{split}
 \delta_{R'}^{(2)}(A)-\delta_R^{(2)}(B)
 ={}&\phi'(Z_A^{(2)})[\tau_{R'}(q_A^{(2)})-\tau_{R'}(q_B^{(2)})]\\
 &+[\phi'(Z_A^{(2)})-\phi'(Z_B^{(2)})]\tau_R(q_B^{(2)})\\
 &+\phi'(Z_A^{(2)})[\tau_{R'}(q_B^{(2)})-\tau_R(q_B^{(2)})].
 \end{split}
\]
Put \(b_R(q)=(|q|-R/2)_+\). The last bracket is zero on \(|q|\le R\)
and at most \(2|q|\) elsewhere. Using (7) and rank-one norm inequalities,
\[
 \|\mathcal V_{R'}(A)-\mathcal V_R(B)\|
 \le C(1+R)d(A,B)+C\|b_R(q_B^{(2)})\|_2.                \tag{10}
\]
The constant is independent of \(R'\). From (9),
\[
 \sup_{s\le S}\|b_R(q_R^{(2)}(s))\|_2
 \le2K\exp[-R^2/(16K^2)]=:\varepsilon_R.               \tag{11}
\]
Consequently two clipped solutions with common initial state satisfy
\[
 \sup_{s\le S}d(\Theta_{R'}(s),\Theta_R(s))
 \le CS\exp[C(1+R)S]\varepsilon_R.                    \tag{12}
\]
This tends to zero uniformly in \(R'\ge R\). Completeness produces
an uncut candidate \(\Theta\). It retains (6) and the readout bound.
Equation (7) identifies its actual \(q^{(2)}\), and (10) gives uniform
convergence of the clipped velocities to \(\mathcal V_\infty(\Theta)\),
since even an additional factor \(1+R\) times (12) vanishes.
Passing the integral equations yields a \(C^1\) uncut feature flow on
ALL of \([0,3/2]\). The same estimate proves the Gaussian moment bound
for its actual \(q^{(2)}\), although that extra assertion is not needed
as a premise of the construction.

For ANY other bounded-primal uncut integral solution on the same spaces,
compare it asymmetrically against \(\Theta_R\) using (10).
Its own bounds only change \(C\); no tail assumption on that competing
solution enters. Letting \(R\to\infty\) in Gronwall proves uniqueness.
From a reached state at \(\sigma\le S\), its initial discrepancy from
\(\Theta_R(\sigma)\) is already at most \(C e^{CR}\varepsilon_R\).
A second Gronwall estimate on \([\sigma,S]\) still tends to zero.
Thus the uncut flow is uniquely restartable throughout this feature
interval, without asserting local Lipschitz continuity on an arbitrary
uncut neighborhood.

At finite width let \(\Theta_{n,R}\) be the clipped flow with zero
readout, and set
\[
 a_{n,R}(s)=\left(\frac1n\sum_i b_R(q^{(2)}_{n,R,i}(s))^2\right)^{1/2}.
\]
Fixed-clip \(\mathcal W_2\) convergence gives convergence of this
quantity at each time. Equations (6),(7) make it uniformly Lipschitz
in time. A finite time net proves
\[
 \sup_{s\le S}|a_{n,R}(s)-\|b_R(q_R^{(2)}(s))\|_2|
 \longrightarrow0 \quad\hbox{in probability at each fixed }R.       \tag{13}
\]
The uncut finite feature flow exists on this interval by the polynomial
primal bounds (6). Couple it to this reference with identical hidden
initialization and its prescribed small random initial readout.
Equation (10), in the same-width metric, gives
\[
 \sup_{s\le S}d_n(\Theta_n^{\rm GF}(s),\Theta_{n,R}(s))
 \le e^{C(1+R)S}
 \left[\frac{\|W^{(4)}_0\|_2}{\sqrt n}
                    +C\int_0^S a_{n,R}(u)\,du\right].              \tag{14}
\]
The initial readout term is \(O_{\mathbb P}(n^{-1})\).
First \(n\to\infty\), then \(R\to\infty\), using (11)--(14),
proves uncut finite-feature-flow convergence on the full \([0,3/2]\).

## Gradient structure and a physical clock that never exits

Trained matrix increments are Hilbert--Schmidt: their velocities in
(5) have size \(\|\delta^{(\ell)}\|_2\|H^{(\ell-1)}\|_2\).
The rank-one difference estimate and the velocity convergence just
proved also give HS convergence of their integrals through cutoff
removal. Give raw variations the squared norm
\[
 \mathbb E[(dZ^{(1)})^2]+\|dW^{(2)}\|_{\rm HS}^2
      +\|dW^{(3)}\|_{\rm HS}^2+\mathbb E[(dW^{(4)})^2].
\]
The scalar predictor is continuously differentiable in this affine
space. The needed scalar Taylor estimate, for fixed \(B\in L^2\), is
\[
 |\mathbb E B[\phi(Z+v)-\phi(Z)-\phi'(Z)v]|
 \le C R\|v\|_2^2+
       C\|B\mathbf1_{|B|>R}\|_2\|v\|_2.
\]
After fixing \(R\), taking \(v\to0\), then \(R\to\infty\), this is
\(o(\|v\|_2)\). Expand the scalar output successively backwards;
matrix-change times activation-change terms are quadratic by
\(\|dW\|_{\rm op}\le\|dW\|_{\rm HS}\).
The gradient is exactly
\[
 \nabla f=(\delta^{(1)},\delta^{(2)}\otimes H^{(1)},
             \delta^{(3)}\otimes H^{(2)},H^{(3)}).
\]
Continuity of the gradient follows by truncating fixed \(L^2\) factors
when bounded gates converge in probability. No general Frechet
differentiability of a nonlinear map \(L^2\to L^2\) is claimed.

The coordinate chain rule gives \(dZ^{(1)}/ds=\phi'(Z^{(1)})q^{(1)}\),
because \((F^{-1})'(F(z))=\phi'(z)\). Bounded derivative and the same
fixed-factor truncation justify it in \(L^2\). Thus the raw feature
flow obeys \(d\theta/ds=\nabla f\). In particular,
\[
 \frac{df}{ds}=K^{(1)}+K^{(2)}+K^{(3)}+K^{(4)},
\]
\[
 K^{(1)}=\mathbb E[(\delta^{(1)})^2],\quad
 K^{(2)}=\mathbb E[(\delta^{(2)})^2]\mathbb E[(H^{(1)})^2],
\]
\[
 K^{(3)}=\mathbb E[(\delta^{(3)})^2]\mathbb E[(H^{(2)})^2],\quad
 K^{(4)}=\mathbb E[(H^{(3)})^2]\ge25/36.                \tag{15}
\]
All four terms are continuous and bounded on \([0,3/2]\).
Since \(f(0)=0\), there is a unique \(s_*\le36/25<3/2\) with
\(f(s_*)=1\). The scalar equation
\[
 s'(t)=2[1-f(s(t))],\qquad s(0)=0                      \tag{16}
\]
has a unique global solution, strictly below \(s_*\) for every finite
\(t\). Indeed with \(B=\sup_{[0,s_*]}f'\),
\(s_*-s(t)\ge s_*e^{-2Bt}>0\). This is the crucial margin: one
constructed feature interval covers EVERY finite physical horizon.
Neither clipped predictor monotonicity nor an infinite-feature-time
response bound is needed.

The physical path has
\(d\theta/dt=-2(f-1)\nabla f=-\nabla (f-1)^2\), with
\(d(f-1)^2/dt=-4(f-1)^2\sum_\ell K^{(\ell)}\).
Its four present fields/operators determine all velocities. All learned
memories are already in the current operators. The Gaussian response
coefficients used in the proof are not prescribed inputs.

Raw physical uniqueness and restart follow as well. For a competing
continuous bounded-primal integral solution, the scalar predictor
chain rule gives
\(d(1-f)/dt=-2(1-f)\sum K^{(\ell)}\). The kernel is bounded on
each compact interval, so a positive initial residual cannot vanish at
finite time. Its feature clock is therefore strictly increasing.
The coordinate chain rule gives
\(F(Z^{(1)}(t))=F(Z^{(1)}(t_0))+
 \int_{t_0}^t2(1-f)q^{(1)}\), an \(L^2\) identity.
Feature-time uniqueness identifies it with the constructed solution
until any first attempted exit. Scalar-clock uniqueness then forces
its clock to be (16), which cannot exit \([0,s_*)\) at finite time.
This applies from time zero and from any reached state. It is global
physical restartability, not a claim of existence beyond \(3/2\)
from arbitrary feature-time initial data.

## Exact raw GD on arbitrary compact physical intervals

Fix \(T<\infty\), and consider the population path on \([0,T+1]\).
Set \(\rho=\min_{0\le t\le T+1}(1-f(s(t)))>0\) and
\(S_b=147/100\). We have \(s(t)\le36/25<S_b<3/2\).
For GD define \(s_0=0\) and, as long as the steps are positive,
\[
 \alpha_k=2\eta_n(1-f_{n,k}),\qquad s_{k+1}=s_k+\alpha_k.
\]
Stop at the first node with \(s_k\ge S_b\) or
\(f_{n,k}\ge1-\rho/2\), or after the final node needed for \([0,T]\).
On the initial operator-bound and small-readout event, both thresholds
hold strictly at zero for sufficiently large \(n\).
Before stopping, \(\alpha_k>0\). Bounds (6) apply inductively to the
raw matrix and readout updates at any prefix with \(s_k\le S_b\):
bounded \(\phi,\phi'\) suffice and do not require a transformed Euler
identity. In particular \(|f_{n,k}|\le a(1+aS_b)\), whence
\(\alpha_k\le C\eta_n\). The first stopping endpoint therefore
still lies below \(3/2\) for large \(n\).

The exact correction when transforming a raw first-coordinate step is
\[
 \begin{split}
 F(z+\alpha\phi'(z)q)-F(z)
 ={}&\alpha q+10\alpha^2 z(\phi'(z))^2q^2
                 +\tfrac{10}{3}\alpha^3(\phi'(z))^3q^3.
 \end{split}                                                     \tag{17}
\]
This is not an exact transformed Euler update. Since
\(\|q^{(1)}_{n,k}\|_2/\sqrt n\le C\) and
\(\sup_z|z|(\phi'(z))^2<\infty\), its error after division by
\(\sqrt n\) is at most \(C(\alpha_k^2\sqrt n+\alpha_k^3 n)\).
Its sum on any stopped prefix is at most
\[
 C_S(\eta_n\sqrt n+\eta_n^2n)\longrightarrow0.          \tag{18}
\]
There is no uncontrolled moment of a coordinate power: use directly
\(\|q^2\|_2\le\|q\|_2^2\), \(\|q^3\|_2\le\|q\|_2^3\).

Compare the transformed GD nodes to \(\Theta_{n,R}(s_k)\). Equation
(10), the fixed-clip Euler local error, and (17) give
\[
 d_{k+1}\le[1+C(1+R)\alpha_k]d_k
       +C\alpha_k a_{n,R}(s_k)+C_R\alpha_k^2
       +C(\alpha_k^2\sqrt n+\alpha_k^3n).
\]
The random partition presents no new probabilistic assumption.
The uniform time-Lipschitz bound for \(a_{n,R}\) gives pathwise
\(\sum_k\alpha_k a_{n,R}(s_k)\le
 \int_0^{3/2}a_{n,R}(u)du+C\max_k\alpha_k\).
Discrete Gronwall, (13), (18), and the small initial readout prove
the stopped comparison
\[
 \max_k d_n(\Theta_n^{\rm GD}(s_k),\Theta_{n,R}(s_k))
 \le e^{C(1+R)S}
 \left[\frac{\|W^{(4)}_0\|_2}{\sqrt n}
  +C\int_0^S a_{n,R}(u)du+C_R\eta_n
          +C_S(\eta_n\sqrt n+\eta_n^2n)\right].          \tag{19}
\]
It includes the first stopping node. Thus the predictor at all these
nodes differs from \(f(s_k)\) by a quantity tending to zero in
probability, first using a fixed \(R\) comparison and then taking
\(R\to\infty\). This is a uniform stopped estimate; its constants
do not depend on the number of positive increments.

Interpolate the computational clock linearly in physical time.
Its slope is \(2(1-f_{n,k})\). The population \(f\) is Lipschitz on
\([0,3/2]\), so (19) and scalar Gronwall give, up through that node,
\[
 \sup_t|s_n(t)-s(t)|\longrightarrow0,
 \qquad\max_k|f_{n,k}-f(s(k\eta_n))|\longrightarrow0
 \quad\hbox{in probability}.                            \tag{20}
\]
The physical endpoint is at most \(T+\eta_n<T+1\).
Both stopping alternatives contradict (20): the population clock is
at most \(36/25\), separated from \(S_b\) by \(3/100\), and its
predictor is at most \(1-\rho\), separated from the stopping threshold
by \(\rho/2\). Consequently with probability tending to one there
is no premature stop. This proves the comparison for every fixed \(T\).
It does not assume a positive lower residual uniformly as \(T\to\infty\).

For the prescribed raw interpolation, apply (17) with a fractional
step. The additional same-step discrepancy vanishes by (18); all
other blocks are already linear. This verifies (19)--(20) for the
specified interpolation, not only at nodes.

Finite physical GF is obtained in the same way from its feature flow.
Alternatively, its exact identity \(df_n/ds\ge25/36\) and
\(f_n(0)\to0\) place its root below \(3/2\) with probability tending
to one; the scalar-clock comparison from (14) then applies.
Comparing GD and GF to the SAME finite clipped reference at their
respective clocks proves the asserted same-width state convergence.
Combining with fixed-clip population laws and removing \(R\) proves
full-sequence joint MF/GF/GD convergence on \([0,T]\).

## Measurements, velocities, and paths

The gate-containing quantities require more than the state norm.
Equation (10) first controls the difference of \(\delta^{(2)}\) in
the cutoff comparison; bounded operators then control \(q^{(1)}\).
Thus both have uniformly-in-time joint \(\mathcal W_2\) laws.
For bounded continuous gates multiplying these fields, truncate the
field at a fixed level, pass the bounded Lipschitz approximation, and
remove the truncation using uniformly integrable squared tails.
These tails are uniform in time: the limiting \(L^2\) paths have
compact time image and the finite laws converge uniformly in
\(\mathcal W_2\). The same argument works after each specified bounded
operator call. It gives all four kernels in (4), the predictor, and loss.

The exact feature velocities are
\[
 (Z^{(1)})'=\phi'(Z^{(1)})q^{(1)},
\]
\[
 (Z^{(2)})'=\mathbb E[(H^{(1)})^2]\delta^{(2)}
       +W^{(2)}[(\phi'(Z^{(1)}))^2q^{(1)}],
\]
\[
 (Z^{(3)})'=\mathbb E[(H^{(2)})^2]\delta^{(3)}
       +W^{(3)}[\phi'(Z^{(2)})(Z^{(2)})'] .             \tag{21}
\]
Feature velocities are \((H^{(\ell)})'=\phi'(Z^{(\ell)})(Z^{(\ell)})'\);
physical velocities multiply these formulas by \(2(1-f)\).
All are continuous \(L^2\) paths by the just-described truncation
argument. Their finite joint laws and squared norms converge uniformly.
For GD the raw derivative is the left-node vector field throughout a
step, but derivatives of recomputed hidden states contain current
gates and matrices. On bounded velocity coordinates their discrepancy
from (21) tends uniformly to zero with the step. On the complement
use the uniform integrability of the squared velocity coordinates.
Matrix/readout interpolation discrepancies are controlled by (19)
and their one-step norms. This proves the same velocity statements
for the right-node/terminal-left convention and convergence of the
integrated squared speeds.

Choose jointly measurable velocity versions and integrate them.
Fubini gives absolutely continuous scalar coordinate paths realizing
these \(L^2\) paths. For a scalar absolutely continuous path and its
linear interpolant on a time partition \(\pi\),
\[
 \|z-I_\pi z\|_\infty^2
       \le4|\pi|\int_0^T|\dot z(t)|^2dt.
\]
Apply the inequality to each finite and population path. Joint
finite-grid laws and convergent integrated squared speeds give
\(\mathcal W_2(C([0,T]))\) convergence for every hidden preactivation;
bounded Lipschitz \(\phi\) gives it for the features as well.

## Nontriviality certificate

We first give explicit initial movement, retaining all trained layers.
Let \(m_\ell=\mathbb E[(H^{(\ell)}_0)^2]\), with \(m_0=1\).
The initial forward laws are \(Z^{(\ell)}_0\sim N(0,m_{\ell-1})\)
and
\[
 m_\ell=1+\frac1{100}\mathbb E[
       \arctan(\sqrt{m_{\ell-1}}G)^2]>1,\quad G\sim N(0,1).
\]
The offset is retained in these full second moments. Define
\[
 B^{(3)}=H^{(3)}_0\phi'(Z^{(3)}_0),\qquad
 B^{(2)}=\phi'(Z^{(2)}_0)(W^{(3)}_0)^*B^{(3)},\qquad
 B^{(1)}=\phi'(Z^{(1)}_0)(W^{(2)}_0)^*B^{(2)},
\]
\[
 V^{(1)}=B^{(1)},\quad
 V^{(2)}=m_1B^{(2)}+W^{(2)}_0[\phi'(Z^{(1)}_0)B^{(1)}],
\]
\[
 V^{(3)}=m_2B^{(3)}+W^{(3)}_0[\phi'(Z^{(2)}_0)V^{(2)}].
\]
All are square-integrable on their indicated layers. The initial
transpose formula above gives, jointly with the existing layer-2 data,
\[
 (W^{(3)}_0)^*B^{(3)}=c_3H^{(2)}_0+\sigma_3G_2,
 \quad \sigma_3^2=\mathbb E[(B^{(3)})^2]>0,
\]
\[
 c_3=\frac1{100m_2}\mathbb E\left[
      \frac{Z^{(3)}_0\arctan Z^{(3)}_0}{1+(Z^{(3)}_0)^2}\right]>0.
\]
Here \(G_2\) is independent of \(Z^{(2)}_0\). The offset contribution
\(\mathbb E[Z^{(3)}_0/(1+(Z^{(3)}_0)^2)]/10\) vanishes by the
INITIAL Gaussian symmetry. We do not assert the false pointwise
inequality \(z\phi(z)\phi'(z)>0\) for negative \(z\).
It follows that
\[
 \sigma_2^2:=\mathbb E[(B^{(2)})^2]
 =\mathbb E[(\phi'(Z^{(2)}_0))^2
            (c_3^2\phi(Z^{(2)}_0)^2+\sigma_3^2)]>0.
\]
For the second transpose, condition on the first-layer initialization,
\(Z^{(2)}_0\), and the entire independent \(W^{(3)}_0\). The vector
\(B^{(2)}\) is then determined without exposing the conditional
residual of \(W^{(2)}_0\). The same formula yields
\[
 (W^{(2)}_0)^*B^{(2)}=c_2H^{(1)}_0+\sigma_2G_1,
 \quad
 c_2=\frac{c_3}{100m_1}\mathbb E\left[
      \frac{Z^{(2)}_0\arctan Z^{(2)}_0}{1+(Z^{(2)}_0)^2}\right]>0,
\]
with \(G_1\) independent of \(Z^{(1)}_0\). Each identification is a
fixed initial Gaussian program: projection errors vanish in
\(\|\cdot\|_2/\sqrt n\), bounded gates preserve the errors, and
Cauchy--Schwarz passes the second-moment contractions. Thus it supplies
the required joint empirical-average limits, not a claim of iid reused
coordinates. Set
\[
 \gamma_1=\mathbb E[(B^{(1)})^2]>0,\quad
 \gamma_2=m_1\mathbb E[(B^{(2)})^2]>0,\quad
 \gamma_3=m_2\mathbb E[(B^{(3)})^2]>0,\quad
 \Gamma=\gamma_1+\gamma_2+\gamma_3.
\]
Adjunction gives
\(\mathbb E[B^{(2)}V^{(2)}]=\gamma_1+\gamma_2>0\) and
\(\mathbb E[B^{(3)}V^{(3)}]=\Gamma>0\).
So every \(V^{(\ell)}\) is nonzero, and strict positivity of \(\phi'\)
makes \(\phi'(Z^{(\ell)}_0)V^{(\ell)}\) nonzero as well.

Strong continuity, the readout integral, and bounded-gate truncation
give \(W^{(4)}(s)/s\to H^{(3)}_0\), then
\(\delta^{(\ell)}(s)/s\to B^{(\ell)}\), all in \(L^2\).
Equation (21) consequently gives
\[
 (Z^{(\ell)})'(s)=sV^{(\ell)}+o(s),\quad
 Z^{(\ell)}(s)-Z^{(\ell)}_0=\tfrac12s^2V^{(\ell)}+o(s^2),
\]
\[
 H^{(\ell)}(s)-H^{(\ell)}_0
 =\tfrac12s^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(s^2).
\]
The feature derivative divided by \(s\) tends to the same nonzero
variable. This curve chain rule follows by writing an integral of
\(\phi'\) along the difference quotient, then truncating its fixed
\(L^2\) factor. It requires no additional smoothness in a Banach-space
neighborhood. In addition,
\[
 W^{(\ell)}(s)-W^{(\ell)}_0
 =\tfrac12s^2 B^{(\ell)}\otimes H^{(\ell-1)}_0+o(s^2),
 \quad \ell=2,3,
\]
in HS norm. Both leading rank-one terms have positive size.
No trained block is frozen.

Expanding the four kernels using these strong limits yields
\[
 K^{(\ell)}(s)=\gamma_\ell s^2+o(s^2)\quad(\ell=1,2,3),
 \qquad K^{(4)}(s)=m_3+\Gamma s^2+o(s^2).
\]
Also \((K^{(4)})'(s)=2\Gamma s+o(s)>0\) for sufficiently small
positive \(s\). Since \(s(t)=2t+o(t)\), in physical time
\[
 H^{(\ell)}(t)-H^{(\ell)}_0
      =2t^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t^2),
\]
\[
 K^{(4)}(t)=m_3+4\Gamma t^2+o(t^2),\qquad
 \sum_{\ell=1}^4K^{(\ell)}(t)=m_3+8\Gamma t^2+o(t^2).   \tag{22}
\]
The integrated squared speed of each hidden feature has leading term
\(\frac{16}{3}\mathbb E[(\phi'(Z^{(\ell)}_0)V^{(\ell)})^2]T^3>0\).
In view of the joint convergence already proved, these are fixed
positive width-limit feature changes and kernel changes. Their
coefficients contain no width-vanishing parameter. This is not a
frozen-feature or constant-kernel limit.

To rule out effective linearization at LATER times, we now prove
unbounded tails for every limiting hidden law. This uses the actual
fixed-mesh programs from dependency 1, with \(A=3/2\), \(S=3/2\),
\(|a^{(\ell)}_{kj}|\le A\Delta\), and both backwards row sums at
most one. Denote a standard Gaussian upper tail by
\(\overline\Phi(x)=\mathbb P(G\ge x)\).
The forward sources have variances between \(m^2\) and \(a^2\),
because these are full activation second moments.

At the top, the scalar representation gives the pointwise bound
\[
 |Z^{(3)}_k-\xi^{(3)}_k|
 \le A a S^2/10=63/160.
\]
Regardless of dependence of the correction on the Gaussian, for \(u>0\)
\[
 \mathbb P(\pm Z^{(3)}_k\ge u)
 \ge\overline\Phi((u+63/160)/m)>0.                     \tag{23}
\]
In the middle put \(Q=161/120\) as in dependency 1. Then
\[
 |Z^{(2)}_k-\xi^{(2)}_k|
 \le R_{2,k}:=\frac{A\Delta}{10}
                         \sum_{j<k}(|\zeta^{(2)}_j|+a),
 \qquad \mathbb E R_{2,k}\le ASQ/10=483/1600.
\]
This DOMINATING variable depends only on the backwards source group,
so is independent of \(\xi^{(2)}_k\); the actual correction need not
be independent. Markov and intersection of these independent events give
\[
 \mathbb P(\pm Z^{(2)}_k\ge u)
 \ge\frac{1117}{1600}\overline\Phi((u+1)/m)>0.          \tag{24}
\]
For the bottom, \(\operatorname{Var}(\zeta^{(1)}_j)
=\mathbb E[(\delta^{(2)}_j)^2]\le(Q/10)^2\). Hence
\[
 |X^{(1)}_k-F(Z^{(1)}_0)|
 \le R_{1,k}:=\Delta\sum_{j<k}|\zeta^{(1)}_j|+aS,
 \quad \mathbb E R_{1,k}\le S(Q/10+a)=1561/800<2.
\]
This bound is independent of \(Z^{(1)}_0\), and its probability of
being at most four is at least \(1/2\). Since \(F\) is increasing
and odd, intersecting with the corresponding Gaussian root event yields
\[
 \mathbb P(\pm Z^{(1)}_k\ge u)
 \ge\tfrac12\overline\Phi(F^{-1}(F(u)+4))>0.            \tag{25}
\]
There is no assumption of independence across source times, nor any
estimate of a supremum of a Gaussian path.

Bounds (23)--(25) are uniform in mesh, clipping, and time index. By
Portmanteau for the closed upper and lower half-lines, the limiting
probability is at least the limsup of the approximating probabilities.
Thus they pass first to fixed-clip flows and then to the constructed
uncut flow at every feature time. Every hidden law has unbounded
support in both directions at every reached physical time, including
initialization. In particular its variance is positive.

For any of these \(Z\), elementary least-squares minimization gives
\[
 \inf_{\alpha,\beta\in\mathbb R}
    \mathbb E[(\phi(Z)-\alpha Z-\beta)^2]
 =\operatorname{Var}(\phi(Z))-
       \frac{\operatorname{Cov}(Z,\phi(Z))^2}
            {\operatorname{Var}(Z)}>0.                 \tag{26}
\]
The minimum is attained. If it were zero, boundedness of \(\phi\)
and unbounded support of \(Z\) would force \(\alpha=0\); strict
monotonicity of \(\phi\) would then force \(Z\) to be constant.
This contradicts the tails. All moments in (26) are continuous along
the \(L^2\) paths, so the minimum error has a positive lower bound
on each fixed compact physical interval, simultaneously in all layers.
Joint \(\mathcal W_2\) convergence transfers this positive bound to
the finite empirical least-squares error with probability tending to
one. The activation formula itself is fixed and nonaffine for every
finite width; there is no parameter tending to a linear activation.

One can also exclude later freezing, not merely initial laziness.
At any fixed \(s>0\), \(W^{(4)}(s)\ge ms\) pointwise and
\(\phi'(Z^{(3)}(s))>0\); hence \(\mathbb E[(\delta^{(3)}(s))^2]>0\).
For approximating fixed-mesh programs, their source variances
\(\operatorname{Var}(\zeta^{(2)}_k)=\mathbb E[(\delta^{(3)}_k)^2]\)
therefore have a positive lower bound at indices approaching \(s\).
Use the joint backward-field convergence already established (weak
convergence and lower semicontinuity alone would suffice).
Since \(|q^{(2)}_k-\zeta^{(2)}_k|\le a\), their Gaussian lower
tails and Portmanteau make \(q^{(2)}(s)\) unbounded in law. Strict
positivity of \(\phi'\) implies \(\delta^{(2)}(s)\ne0\).
Now repeat with
\(\operatorname{Var}(\zeta^{(1)}_k)=\mathbb E[(\delta^{(2)}_k)^2]\)
and \(|q^{(1)}_k-\zeta^{(1)}_k|\le a\) to obtain
\(\delta^{(1)}(s)\ne0\). Every hidden kernel is positive at positive
time. Moreover (21) and adjunction give
\[
 \mathbb E[\delta^{(2)}(Z^{(2)})']=K^{(2)}+K^{(1)}>0,
 \qquad
 \mathbb E[\delta^{(3)}(Z^{(3)})']
        =K^{(3)}+K^{(2)}+K^{(1)}>0.
\]
Together with \((Z^{(1)})'=\delta^{(1)}\) and \(\phi'>0\), these
prove nonzero \(L^2\) hidden preactivation and feature velocities at
every positive finite physical time, since the physical residual is
then strictly nonzero. Initial velocities vanish because the limiting
initial readout is zero; the second-order changes (22) are the genuine
feature-learning onset.

This completes the candidate proof of the changed-activation instance.
No clipping remains in the model or limiting equations. The result is
compact-on-every-finite-physical-interval convergence, not a claim of a
width-uniform interchange with infinite training time or a proof for
the original unshifted arctangent activation.
