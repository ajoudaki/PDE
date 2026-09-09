# A nonlinear, non-lazy three-hidden-layer joint mean-field/gradient-flow limit

This document proves the result for the single fixed activation
\(\phi(z)=1+\arctan(z)/10\) in all three hidden layers. All arguments
needed for this instance are included below. No result for a different
activation, no external mean-field or tensor-program theorem, and no
external continuation theorem is invoked. The underlying mathematical
background is elementary probability and Gaussian integration, basic
measure theory, and Hilbert/Banach-space analysis. The Gaussian program,
response, comparison, and discretization arguments are proved explicitly.

The theorem concerns each fixed finite physical horizon. It does not
assert an interchange of infinite training time and infinite width,
operator-norm convergence between different spaces, or existence from
arbitrary population initial states. Its unique restart assertion is
from every reached state on the common spaces constructed here.

## 1. Exact model and theorem

There is one input, equal to one, and target one. Each of the three
hidden layers has width \(n\). The first preactivation \(z^{(1)}\)
and the rescaled readout \(W^{(4)}\) are vectors in \(\mathbb R^n\).
The hidden matrices \(W^{(2)},W^{(3)}\) are \(n\) by \(n\). Set
\[
 \phi(z)=1+\frac1{10}\arctan z,\quad
 h^{(\ell)}=\phi(z^{(\ell)}),\quad
 z^{(2)}=W^{(2)}h^{(1)},\quad z^{(3)}=W^{(3)}h^{(2)},
\]
\[
 f_n=\frac{(W^{(4)})^T h^{(3)}}n,\qquad
 r_n=f_n-1,\qquad L_n=r_n^2.
\]
Nonlinearities and vector products are coordinatewise. Define
\[
 \delta^{(3)}=W^{(4)}\phi'(z^{(3)}),\quad
 q^{(2)}=(W^{(3)})^T\delta^{(3)},\quad
 \delta^{(2)}=\phi'(z^{(2)})q^{(2)},
\]
\[
 q^{(1)}=(W^{(2)})^T\delta^{(2)},\qquad
 \delta^{(1)}=\phi'(z^{(1)})q^{(1)}.                    \tag{1.1}
\]
The residual is not included in any \(\delta\).

All four initialization blocks are independent, with independent entries
within each block:
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(2)}_{0,ij},W^{(3)}_{0,ij}\sim N(0,1/n),\quad
 W^{(4)}_{0,i}\sim N(0,n^{-2}).                         \tag{1.2}
\]
The symbol \(W^{(4)}\) always denotes the rescaled readout. With
\(\eta_n=n^{-2}\), exact raw GD is
\[
 z^{(1)}_{k+1}=z^{(1)}_k-2\eta_n r_{n,k}\delta^{(1)}_k,
\]
\[
 W^{(\ell)}_{k+1}=W^{(\ell)}_k-
 \frac{2\eta_n r_{n,k}}n\delta^{(\ell)}_k(h^{(\ell-1)}_k)^T,
 \quad\ell=2,3,
\]
\[
 W^{(4)}_{k+1}=W^{(4)}_k-2\eta_n r_{n,k}h^{(3)}_k.       \tag{1.3}
\]
Physical time is \(t=k\eta_n\). Interpolate RAW parameters linearly;
recompute preactivations and features from these interpolated parameters.
At interior mesh nodes, velocities mean right derivatives; at an observed
terminal mesh node use the left derivative. Finite gradient flow has
derivatives equal to the update increments in (1.3) divided by
\(\eta_n\), evaluated at the current continuous state.

Theorem. There exist three fixed neuron probability spaces
\(\Omega_1,\Omega_2,\Omega_3\), with deterministic bounded initial
Gaussian matrix actions and their adjoints, on which the following
four evolving objects define an autonomous population gradient flow:
\[
 X^{(1)},\quad W^{(2)},\quad W^{(3)},\quad W^{(4)},\qquad
 Z^{(1)}=F^{-1}(X^{(1)}),\quad F(z)=10(z+z^3/3).         \tag{1.4}
\]
Vector fields belong to their layer's \(L^2\) space; matrices are bounded
operators between adjacent \(L^2\) spaces. Expectations always refer to
the layer containing the integrand. Finite transpose is \(T\); population
adjoint is \(*\). Initially \(Z^{(1)}_0\sim N(0,1)\) and
\(W^{(4)}_0=0\). Define the forward/backward objects by (1.1), with
capital preactivations/features and adjoints in place of transposes.
For adjacent-layer fields define
\[
 (U\otimes V)B=U\mathbb E[VB].
\]
The population equations are
\[
 f=\mathbb E[W^{(4)}H^{(3)}],\quad r=f-1,\quad
 \dot X^{(1)}=-2r q^{(1)},\quad
 \dot W^{(2)}=-2r\delta^{(2)}\otimes H^{(1)},
\]
\[
 \dot W^{(3)}=-2r\delta^{(3)}\otimes H^{(2)},\qquad
 \dot W^{(4)}=-2rH^{(3)}.                              \tag{1.5}
\]
For every \(T<\infty\) these equations have a solution, unique among
continuous integral solutions on the same spaces with bounded vector
\(L^2\) norms and matrix operator norms on compact intervals. Uniqueness
also holds for the raw first-coordinate equations. From every reached
state the solution is uniquely restartable for every finite remaining
physical interval. The four present objects determine all derivatives;
no response kernel or history is supplied as an external forcing.

For each fixed \(T\), the full width sequence of GD (1.3) and its
corresponding finite gradient flow converges jointly in probability
to this flow, uniformly on
\([0,T]\), in the following precise sense. For any fixed finite
same-layer list of current fields and probe outputs, their empirical
joint law converges in \(\mathcal W_2\) to its population law. Probe
instructions may use real linear combinations, globally Lipschitz
coordinate functions, products of bounded factors, and either direction
of either current matrix. The class also contains the named backward
fields (1.1) and all hidden preactivation/feature velocities. A finite
number of time arguments can be used jointly; convergence is uniform
over those arguments in \([0,T]\). There is no coordinate pairing
between different neuron populations. Equivalently, every continuous
test of at most quadratic growth on such a finite list converges in
empirical average. Here \(\mathcal W_2\) is the infimum square root
of expected squared Euclidean distance over couplings of two laws.

In particular predictions, residuals, losses, and the four raw kernel
blocks converge uniformly:
\[
 K_n^{(1)}=\frac{\|\delta^{(1)}\|_2^2}{n},\quad
 K_n^{(2)}=\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2},
\]
\[
 K_n^{(3)}=\frac{\|\delta^{(3)}\|_2^2\|h^{(2)}\|_2^2}{n^2},\qquad
 K_n^{(4)}=\frac{\|h^{(3)}\|_2^2}{n}.                 \tag{1.6}
\]
For every hidden layer, the empirical laws of whole preactivation and
feature paths converge in \(\mathcal W_2(C([0,T]))\), using the
supremum norm on paths. Integrated squared velocities converge too.
When GD and GF use the same finite initialization, their state-distance
supremum tends to zero in probability, where this SAME-WIDTH distance is
\[
 \frac{\|F(z^{(1)})-F(\widetilde z^{(1)})\|_2}{\sqrt n}
 +\|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}
 +\|W^{(3)}-\widetilde W^{(3)}\|_{\rm op}
 +\frac{\|W^{(4)}-\widetilde W^{(4)}\|_2}{\sqrt n}.      \tag{1.7}
\]
Across different widths only the empirical/action-law statement is made.

The limit is genuinely nonlinear and non-lazy. Every hidden distribution
has strictly positive best affine-approximation error for \(\phi\),
uniformly on each compact physical interval, including initialization.
Every hidden feature velocity has nonzero \(L^2\) norm at every positive
finite physical time. Initial hidden motion begins at second order,
and the total kernel is nonconstant. The factor \(1/10\) is fixed;
it is never taken to zero in any limit.

Proof architecture. We first prove the finite Gaussian-program law,
including both transposes and singular query covariances, and realize
these laws as bounded actions on fixed spaces. Auxiliary clipped flows
are then constructed. An explicit mesh- and cap-uniform response estimate
on feature time \([0,3/2]\) removes clipping and proves uniqueness.
The positive activation floor confines every finite physical horizon
strictly inside this interval. A separate stopped comparison treats the
exact raw GD. We finish with all observables and nontriviality.

## 2. Elementary bounds and limiting tools

Put \(m=5/6\), \(a=7/6\). Since \(\pi<10/3\),
\[
 m<\phi<a,\quad 0<\phi'(z)=\frac1{10(1+z^2)}\le1/10,
 \quad \phi''(z)=-\frac{z}{5(1+z^2)^2},\quad|\phi''|\le1/5.
\]
The increasing bijection \(F\) has \(F'=1/\phi'\). Its inverse is
\(1/10\)-Lipschitz. For \(\chi=\phi\circ F^{-1}\),
\[
 \chi'(F(z))=(\phi'(z))^2\le1/100.                    \tag{2.1}
\]
The pair \((G,F(G))\), \(G\sim N(0,1)\), has every finite moment.
We will treat it as an initial root pair; \(F\) is not globally Lipschitz.

For an \(n\times n\) matrix with independent \(N(0,1/n)\) entries,
a \(1/4\)-net of the unit sphere has at most \(9^n\) points (compare
volumes of disjoint balls of radius \(1/8\) in a ball of radius \(9/8\)).
Approximating both unit vectors in a bilinear form gives
\(\|W\|_{\rm op}\le2\max_{u,v\text{ in net}}|u^TWv|\).
Every such bilinear form is \(N(0,1/n)\). Therefore
\[
 \mathbb P(\|W\|_{\rm op}>10)
 \le2\,9^{2n}e^{-100n/8}\longrightarrow0.               \tag{2.2}
\]
We use this simultaneously for the two initial matrices. Also
\(\mathbb E\|W^{(4)}_0\|_2^2/n=n^{-2}\), so its vector norm
divided by \(\sqrt n\) is \(O_{\mathbb P}(n^{-1})\).

We record the precise elementary convergence facts used later.

(a) Laws on a fixed finite-dimensional Euclidean space converge in
\(\mathcal W_2\) if and only if they converge weakly and their second
moments converge. Here is the implication needed in our proofs. Weak
convergence and convergence of second moments imply uniformly small
squared tails: subtract the convergent expectations of
\(\min(\|x\|^2,R^2)\) from the second moments, then let \(R\to\infty\).
Restrict to a large ball and partition it into finitely many cells of
diameter at most \(\epsilon\), with boundaries of limiting measure zero.
Weak convergence gives convergence of cell masses. Couple common mass
within matching cells; the unmatched mass on the ball costs at most its
mass times the squared diameter. Couple the tails through the origin,
using \(\|x-y\|^2\le2\|x\|^2+2\|y\|^2\).
First take the sequence limit, then \(\epsilon\to0\) and the ball radius
to infinity. This gives a coupling cost tending to zero. Conversely,
a coupling with mean squared difference tending to zero gives weak
convergence for bounded Lipschitz tests, and convergence of second
moments by the triangle inequality in \(L^2\).

(b) Such convergence implies convergence of continuous tests bounded
in absolute value by \(C(1+\|x\|^2)\). On a large ball approximate
the test uniformly by a bounded Lipschitz function; control the rest
by the squared tails just proved. The same argument gives uniformity
over a compact set of laws in \(\mathcal W_2\). A continuous \(L^2\)
path has compact image and uniformly integrable squared coordinate
tails: approximate that image by finitely many \(L^2\) balls, then
use a squared-triangle tail bound with their finitely many centers.

(c) For two finite lists coupled by their neuron indices,
\[
 \mathcal W_2\left(\frac1n\sum_i\delta_{u_i},
                  \frac1n\sum_i\delta_{v_i}\right)
 \le\left(\frac1n\sum_i\|u_i-v_i\|^2\right)^{1/2}.     \tag{2.3}
\]
Lipschitz coordinate maps preserve this comparison. Products of bounded
factors can be smoothly extended outside their bounds to globally
Lipschitz maps. If \(x_j\to x\) in probability, \(v_j\to v\) in
\(L^2\), and \(g\) is bounded continuous, then
\[
 g(x_j)v_j\longrightarrow g(x)v\quad\hbox{in }L^2.     \tag{2.4}
\]
Separate the part containing \(v_j-v\); for the rest first restrict
to \(|v|\le R\) and use bounded convergence in probability, then let
\(R\to\infty\). This also proves the chain rule for \(\phi\) along
an \(L^2\)-differentiable curve: divide its difference by the time
increment and write the activation difference as the increment times
the integral of \(\phi'\) along the connecting segment. It is not a
claim of Frechet differentiability of every nonlinear map \(L^2\to L^2\).

(d) If \(b,c_r\ge0\) and
\(u_j\le b+\sum_{r<j}c_r\max_{v\le r}u_v\), then
\[
 \max_{v\le j}u_v\le b\prod_{r<j}(1+c_r)
                  \le b\exp\left(\sum_{r<j}c_r\right). \tag{2.5}
\]
The product is a nondecreasing comparison sequence satisfying equality
in the preceding summation recursion. Induction proves the assertion.
For the continuous version, iteration of
\(u(t)\le b+C\int_0^t u\) gives the exponential series and hence
\(u(t)\le be^{Ct}\); the same argument includes an integrable forcing
by first bounding its accumulated integral. These are the precise
Gronwall comparisons used below.

## 3. Finite Gaussian calculations with adaptive reuse

We prove the law required for a fixed finite sequence of instructions.
There are three neuron populations, finitely many iid root tuples in
each, independent of the two Gaussian matrices, and coordinate
instructions that are \(C^1\), globally Lipschitz, with bounded first
derivatives. Deterministic real linear combinations are allowed. A
matrix can be queried in either direction, and inputs may depend on
the complete earlier transcript through these instructions. No instruction
mixes coordinates from different populations except through matrix
actions or a separately specified scalar contraction.
Initially the root empirical laws converge with second moments by the
ordinary law of large numbers; our roots have all finite moments.
Scalar contractions will first be deterministic and later restored to
their empirical values.

### 3.1 One forward call, then a transpose

For this introductory calculation assume \(h\ne0\) almost surely.
The zero-query and vanishing-limiting-norm cases for the permitted
programs are covered by Section 3.4.
For an independent input \(h\), the coordinates of \(Wh\) conditioned
on \(h\) are independent centered Gaussians with variance
\(\|h\|_2^2/n\). A nonzero mean of \(h\) is not subtracted. If
\(y=Wh\), rowwise Gaussian orthogonal projection gives
\[
 W\mid(h,y)\ \overset d=\frac{yh^T}{\|h\|_2^2}
                  +\widetilde W P_{h^\perp},           \tag{3.1}
\]
where \(\widetilde W\) is independent with the original entry law.
If \(u\) is known without observing this residual, then
\[
 W^Tu=h\frac{y^Tu/n}{\|h\|_2^2/n}
       +\frac{\|u\|_2}{\sqrt n}P_{h^\perp}g             \tag{3.2}
\]
in conditional law, with fresh standard Gaussian vector \(g\).
The removed projection satisfies
\(\mathbb E\|P_{\operatorname{span}(h)}g\|_2^2/n=1/n\).
Suppose a fixed finite input-population tuple containing \(h\), known
without observing the residual in (3.1), has a joint empirical
\(\mathcal W_2\) limit. Write \(H\) for its limiting \(h\) field and
assume \(\mathbb E[H^2]>0\). Suppose separately that the output-population
pair \((y,u)\) converges empirically in \(\mathcal W_2\) to \((Y,U)\).
Formula (3.2) and conditional Gaussian averaging then give the joint
limit of the old input-population tuple and the new answer
\(cH+\sigma G\). Here \(G\) is independent of that old input-population
tuple, and
\(c=\mathbb E[YU]/\mathbb E[H^2]\) and
\(\sigma^2=\mathbb E[U^2]\). The innovation variance is the FULL
second moment, not that moment minus the response variance. The new
answer equals the response forced by the old use plus unexplored
Gaussian randomness. It is not a fresh iid replacement of the old matrix.

### 3.2 General conditional projection and empirical induction

For one matrix, collect old observations as
\(WV=Y\), \(W^TU=Q\). Suppose first that the input Gram matrices
are invertible. Let \(\mathcal F\) denote the preceding transcript,
including the initial roots and all preceding inputs and answers.
The exact conditional law is
\[
 W\mid\mathcal F\ \overset d=Y(V^TV)^{-1}V^T
   +U(U^TU)^{-1}Q^TP_{V^\perp}
   +P_{U^\perp}\widetilde W P_{V^\perp}.               \tag{3.3}
\]
Here \(\widetilde W\) is independent of \(\mathcal F\), with the
original Gaussian entry law.
To verify it, vectorize the Gaussian matrix in its Euclidean entry
space. The constraints are linear. Its component orthogonal to both
constraint spaces is exactly the last term. The first two terms
satisfy both constraints: \(U^TY=Q^TV\) gives the compatibility for
the overlapping component. Gaussian orthogonal components are independent,
which proves the conditional formula.

Adaptation and the second matrix cause no change to this argument.
Conditional on the preceding transcript, the next query input is known.
The next answer constrains only the queried matrix by a new linear
observation. Inductively the two conditional residual matrices remain
independent. Coordinate instructions reveal no further randomness.

For a new forward input put
\(\alpha_n=(V^TV)^{-1}V^Th\), \(h_\perp=h-V\alpha_n\). Then
\[
 (Wh)\mid\mathcal F\ \overset d=Y\alpha_n+U\beta_n+
           \frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g,
 \quad
 \beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n).                  \tag{3.4}
\]
The vector \(g\) here is a fresh standard Gaussian independent of
\(\mathcal F\); the new input \(h\) is \(\mathcal F\)-measurable.
The reverse formula interchanges the two sides. For a fixed number of
queries the discarded Gaussian projection has expected squared norm
after division by \(n\) at most the fixed rank divided by \(n\).
Its variance multiplier is bounded in probability by earlier second
moments. When all limiting input Grams are positive definite, their
inverses and the coefficients in (3.4) converge.

This proves joint empirical convergence by finite induction. Here are
the averaging details, so independence is not being asserted for reused
coordinates. After dropping the projection, a new coordinate is a known
linear combination of old coordinates plus \(\sigma_n g_i\), with
\(g_i\) independent conditionally on the transcript. For a bounded
Lipschitz test on the old tuple and this coordinate, conditional variance
of its empirical average is at most its squared bound divided by \(n\).
Its conditional expectation is the old empirical average of the test
integrated against a one-dimensional Gaussian. This integrated test is
bounded Lipschitz in the old tuple and continuous in the converging
coefficients and \(\sigma_n\). It converges by the induction hypothesis.
For second moments, conditional Gaussian averaging gives the known
squared mean plus \(\sigma_n^2\); the cross-term variance is bounded
by \(4\sigma_n^2\|\text{mean vector}\|_2^2/n^2\), and the centered
Gaussian-square average has variance \(2\sigma_n^4/n\).
Both vanish on bounded-norm events. Old second moments converge by
induction. Section 2(a) gives joint \(\mathcal W_2\) convergence.
Lipschitz coordinate instructions preserve it. Every contraction is
a continuous quadratic-growth test and converges too.

### 3.3 The exact Gaussian source/response rule

There is a useful representation of those limits. Each oriented initial
matrix has a centered Gaussian source group; the four groups are
mutually independent and independent of roots. Different times within
one group need not be independent. A forward input \(h\) has source
\(\xi_h\), a reverse input \(u_s\) has source \(\zeta_s\), and the
source covariances equal the uncentered second moments of their inputs.
The limiting forward answer is
\[
 \xi_h+\sum_s u_s\,\mathbb E\frac{\partial h}{\partial\zeta_s}.
                                                               \tag{3.5}
\]
Only previously available reverse inputs occur. The transpose rule is
the identical formula with orientations interchanged. Derivatives in
(3.5) are derivatives of the complete explicit coordinate expression,
with all previously selected deterministic coefficients and covariance
parameters held fixed.

We derive the rule. Let old forward inputs be \(v_r\), old reverse
inputs \(u_s\), and \(\Gamma_U=(\mathbb E[u_su_t])_{st}\).
Inductively old forward answers are
\(y_r=\xi_r+\sum_s D_{rs}u_s\), with
\(D_{rs}=\mathbb E\partial_{\zeta_s}v_r\), and old reverse answers
are \(q_s=\zeta_s+\) a linear combination of old forward inputs.
Unavailable source derivatives are zero. Put
\(h_\perp=h-\sum_r\alpha_rv_r\) for the limiting least-squares
projection. Since \(\mathbb E[v_rh_\perp]=0\),
\[
 \mathbb E[q_s h_\perp]=\mathbb E[\zeta_s h_\perp].
\]
For a centered Gaussian vector of covariance \(\Gamma\), integration
of a differentiable function against its Gaussian density gives
\(\mathbb E[\zeta f]=\Gamma\mathbb E\nabla f\).
For a singular covariance write \(\zeta=AG\) and apply the
one-dimensional integration-by-parts identity to each component of
the standard Gaussian \(G\). Bounded derivatives and integrable
roots justify conditioning on the other groups and integration here.
Thus the limit of \(\beta_n\) in (3.4) is
\[
 \beta=\mathbb E\nabla_\zeta h
                  -\sum_r\alpha_r\mathbb E\nabla_\zeta v_r.
\]
Substituting the old forward decompositions in (3.4) cancels the second
term and proves (3.5). The new source is
\(\xi_h=\sum_r\alpha_r\xi_r+\sigma G\), where
\(\sigma^2=\mathbb E h_\perp^2\) and the new scalar Gaussian is
independent of all old sources. Direct expansion gives
\(\mathbb E[\xi_h\xi_r]=\mathbb E[hv_r]\) and
\(\mathbb E\xi_h^2=\mathbb E h^2\).
This also proves the asserted independence of distinct source groups.
The proof includes derivatives passing through previous uses of the
other matrix; it does not differentiate the coefficient selection itself.

### 3.4 Singular Grams without an inverse-limit assumption

Before each matrix call, add to its input \(\epsilon g^{\rm in}\),
where \(g^{\rm in}\) is a new independent standard Gaussian vector,
revealed immediately before that call. It is a root instruction, not
new persistent noise in the final model. At fixed \(\epsilon>0\),
the limiting squared distance of a query from the old same-direction
input span has the additional term \(\epsilon^2\): the fresh root
is independent of that span and of the original new input, so its
cross contractions vanish by conditional averaging. Every limiting
Gram Schur complement is positive. Sections 3.2--3.3 apply.

For this fixed finite program, couple the perturbed and unperturbed
calculations with the same original matrices and roots. On the event
that (2.2) holds and the finitely many noise norms divided by
\(\sqrt n\) are bounded, Lipschitz induction through the finite
instructions bounds every node discrepancy divided by \(\sqrt n\)
by \(C\epsilon\). The constant can depend on the fixed program, but
not on width or \(\epsilon\le1\).

The scalar source recursion converges as \(\epsilon\to0\) as well.
To see this without pseudoinverses, use the causal recursion (3.5).
At each instruction the preceding deterministic coefficients and their
formal source derivatives are bounded on a compact coefficient set.
Composition of the finitely many bounded-derivative coordinate maps
gives a deterministic bound for each formal derivative. Covariance
entries are second moments of already constructed inputs and converge
by induction. Positive-semidefinite covariance square roots are
continuous: uniformly approximate \(\sqrt x\) by polynomials on a
common compact eigenvalue interval and use the spectral decomposition
for each matrix. Couple the finite Gaussian source vectors by these
square roots and common standard Gaussian roots. Coordinate expressions
converge in \(L^2\); their bounded formal derivatives converge by
dominated convergence. Hence the next expected derivative, covariance,
and coordinate law converge. This proves the induction even at a rank
drop. At zero noise the auxiliary input-root coefficients are zero,
leaving exactly the original explicit expression.

Combining the \(C\epsilon\) finite comparison with these limiting laws,
then sending \(\epsilon\to0\), proves the unperturbed joint empirical
limit. Formally distinct source slots remain distinct when their Gaussian
law is singular. Their derivative convention is the displayed expression.
There is no ambiguity in the contracted answer: if the source covariance
\(\Gamma\) also equals \(\mathbb E[uu^T]\), then every deterministic
\(v\in\ker\Gamma\) obeys \(u^Tv=0\) almost surely, since its squared
expectation is zero. A change of derivative coefficients in this null
space cannot change (3.5).

## 4. The actual clipped Euler program and its scalar law

In Sections 4–8, \(s\) is an auxiliary feature-time variable and
\(\Delta\) is its step size. The equations remove the scalar physical
factor \(2(1-f)\) and use the transformed first coordinate. Primes on
state paths denote \(d/ds\); dots denote derivatives in physical time
\(t\). Primes on scalar functions such as \(\phi\) and \(\tau_R\)
always mean derivatives with respect to their scalar argument.
Section 9 proves that the uncut feature field is the raw gradient
of \(f\), and constructs the physical clock \(ds/dt=2(1-f)\).
The clipped reference equations are auxiliary flows; they are not
asserted to be gradient flows.

Choose smooth odd maps \(\tau_R\), for integers \(R\ge1\), satisfying
\[
 \tau_R(q)=q\ (|q|\le R),\quad
 |\tau_R(q)|\le\min(|q|,2R),\quad 0\le\tau'_R\le1.       \tag{4.1}
\]
For example let \(\tau_R(q)=\int_0^q\rho(u/R)du\), where smooth even
\(\rho\) equals one on \([-1,1]\), zero outside \([-2,2]\), and
lies between zero and one. Only the middle backward query is clipped.
The population initial readout in the proof programs is zero; the
prescribed small finite readout is restored in Sections 8 and 10.

For fixed \(M,\Delta,R\), Euler in the natural first coordinate is
\[
 x^{(1)}_{k+1}=x^{(1)}_k+\Delta q^{(1)}_{R,k},\quad
 W^{(2)}_{k+1}=W^{(2)}_k+
                 \frac\Delta n\delta^{(2)}_{R,k}(h^{(1)}_k)^T,
\]
\[
 W^{(3)}_{k+1}=W^{(3)}_k+
                 \frac\Delta n\delta^{(3)}_k(h^{(2)}_k)^T,
 \quad W^{(4)}_{k+1}=W^{(4)}_k+\Delta h^{(3)}_k,
\]
where \(h^{(1)}_k=\chi(x^{(1)}_k)\), the other forward equations are
unchanged, \(\delta^{(2)}_{R,k}=\phi'(z^{(2)}_k)\tau_R(q^{(2)}_k)\),
and \(q^{(1)}_{R,k}=(W^{(2)}_k)^T\delta^{(2)}_{R,k}\).
This is a discretization of a continuous transformed equation, not an
exact rewrite of (1.3).

Unrolling a trained matrix gives its initial action plus the finite sum
of its rank-one updates. Thus its forward call has the extra term
\[
 \Delta\sum_{j<k}\delta^{(\ell)}_j
       \frac{(h^{(\ell-1)}_j)^Th^{(\ell-1)}_k}{n},
\]
and its transpose call has the extra term
\[
 \Delta\sum_{j<k}h^{(\ell-1)}_j
       \frac{(\delta^{(\ell)}_j)^T\delta^{(\ell)}_k}{n}.
                                                               \tag{4.2}
\]
The clipped definition is used for \(\delta^{(2)}\) here and below
in scalar programs; the subscript \(R\) may be omitted when unambiguous.
First freeze these finitely many contractions at the expectations
constructed causally by Section 3. This defines an oracle finite program
with deterministic coefficients. It meets all hypotheses there:
\(|W^{(4)}_k|\le aM\Delta\), \(|\delta^{(3)}_k|\le aM\Delta/10\),
\(|\delta^{(2)}_k|\le R/5\). The top product can be smoothly extended
outside a larger readout interval so that it has bounded first derivatives;
its values and derivatives on attained states are unchanged. All other
coordinate maps already have the required bounded derivatives. Roots
include \((z^{(1)}_0,F(z^{(1)}_0))\).

The oracle's joint empirical contractions converge by Section 3. To
restore actual feedback, at every finite instruction use
\[
 \left|\frac{u^Tv-\widetilde u^T\widetilde v}{n}\right|
 \le\frac{\|u-\widetilde u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
   +\frac{\|\widetilde u\|_2}{\sqrt n}
                        \frac{\|v-\widetilde v\|_2}{\sqrt n}.
\]
Initial matrix norms and every finite oracle norm are bounded with
probability tending to one. Finite induction through (4.2) and the
Lipschitz instructions then bounds actual/oracle discrepancies by a
fixed constant times the preceding discrepancies and the finitely many
oracle contraction errors. They tend to zero. No mesh-uniform finite
Gaussian induction is being asserted at this stage.

Consequently the actual program has exactly this limiting scalar law:
\[
 X^{(1)}_k=F(Z^{(1)}_0)+\Delta\sum_{r<k}q^{(1)}_r,
 \quad H^{(1)}_k=\chi(X^{(1)}_k),
\]
\[
 Z^{(\ell)}_k=\xi^{(\ell)}_k+
                \sum_{r<k}a^{(\ell)}_{kr}\delta^{(\ell)}_r,
 \quad H^{(\ell)}_k=\phi(Z^{(\ell)}_k),\quad \ell=2,3,
\]
\[
 W^{(4)}_k=\Delta\sum_{r<k}H^{(3)}_r,\quad
 \delta^{(3)}_k=W^{(4)}_k\phi'(Z^{(3)}_k),
\]
\[
 q^{(2)}_k=\zeta^{(2)}_k+
          \sum_{v\le k}b^{(3)}_{kv}H^{(2)}_v,
 \quad \delta^{(2)}_k=\phi'(Z^{(2)}_k)\tau_R(q^{(2)}_k),
\]
\[
 q^{(1)}_k=\zeta^{(1)}_k+
                  \sum_{v\le k}b^{(2)}_{kv}H^{(1)}_v.   \tag{4.3}
\]
The four centered Gaussian source groups are mutually independent and
independent of \(Z^{(1)}_0\), with
\[
 \mathbb E[\xi^{(\ell)}_k\xi^{(\ell)}_s]
       =\mathbb E[H^{(\ell-1)}_kH^{(\ell-1)}_s],\quad
 \mathbb E[\zeta^{(\ell-1)}_k\zeta^{(\ell-1)}_s]
       =\mathbb E[\delta^{(\ell)}_k\delta^{(\ell)}_s].  \tag{4.4}
\]
These are FULL second moments, not centered activation covariances.
The deterministic coefficients, with the frozen-expression derivative
convention of Section 3, are
\[
 a^{(\ell)}_{ks}=
  \mathbb E\frac{\partial H^{(\ell-1)}_k}
                    {\partial\zeta^{(\ell-1)}_s}
       +\Delta\mathbb E[H^{(\ell-1)}_kH^{(\ell-1)}_s],\quad s<k,
\]
\[
 b^{(\ell)}_{ks}=
  \mathbb E\frac{\partial\delta^{(\ell)}_k}
                    {\partial\xi^{(\ell)}_s}
       +\Delta\mathbf1_{s<k}
                      \mathbb E[\delta^{(\ell)}_k\delta^{(\ell)}_s],
       \quad s\le k.                                  \tag{4.5}
\]
The causal order is forward matrix 2, forward matrix 3, reverse matrix 3,
reverse matrix 2. It makes each covariance extension and coefficient
available when required. In particular forward corrections are strictly
past-time; reverse corrections include the present time. Explicitly,
\[
 b^{(3)}_{kk}=\mathbb E[W^{(4)}_k\phi''(Z^{(3)}_k)],
\]
\[
 b^{(2)}_{kk}=\mathbb E[\phi''(Z^{(2)}_k)\tau_R(q^{(2)}_k)]
       +b^{(3)}_{kk}\mathbb E[(\phi'(Z^{(2)}_k))^2\tau'_R(q^{(2)}_k)].
                                                               \tag{4.6}
\]
The second term on the last line is a current return through the other
matrix and must not be dropped. All past-source derivatives likewise
retain the complete expression.

## 5. Common population actions and fixed-clip flows

Take a countable family of finite programs closed under finite unions,
rational linear combinations, constants in every population, both
directions of both initial matrices, the permitted globally Lipschitz
\(C^1\) coordinate maps used in Sections 2 and 4, and
a countable family of smooth bounded globally Lipschitz coordinate
functions dense among continuous functions on compact subsets of every
finite-dimensional coordinate space. Include clipped products and the
root pair \((Z^{(1)}_0,F(Z^{(1)}_0))\); the closure does not include
arbitrary later applications of the non-Lipschitz cubic \(F\).
Its later appearances in coordinate-change calculations are not
Gaussian-program instructions. The finite laws in Section 3
are consistent: every finite union is the limit of the same finite-width
calculations. Consistent finite-coordinate laws on a countable product
of real lines define a probability measure on that product. This is the
countable probability-measure extension principle; equivalently one
successively samples the conditional law of coordinate \(j+1\) given
the preceding \(j\) coordinates. Consistency makes every finite marginal
the prescribed one. Apply it separately in each layer, using the sigma
field generated by these coordinate slots. This defines \(\Omega_\ell\).

The span of the generated coordinate functions is dense in
\(L^2(\Omega_\ell)\). Indeed conditional expectations on the first
finitely many slots approximate a square-integrable function in \(L^2\);
this follows from orthogonal projection onto the increasing finite-slot
subspaces whose union generates the sigma field (approximate indicators
first, then simple functions). Truncate the resulting finite-slot
function. Bounded continuous functions approximate bounded measurable
functions in a finite Borel probability law: approximate indicator sets
from compact subsets and open supersets, then use continuous distance
cutoffs. Finally approximate the continuous functions on a compact set
by the included dense Lipschitz family. Tail truncation controls the
discarded error. Thus the claimed density holds.

For any finite rational linear combination of generated inputs, pass
the exact finite inequality from (2.2) to its limiting second moment.
It yields
\[
 \|W^{(\ell)}_0 U\|_{L^2(\Omega_\ell)}
                 \le10\|U\|_{L^2(\Omega_{\ell-1})}.    \tag{5.1}
\]
Zero \(L^2\) input difference gives zero output difference, so this
defines a well-defined linear action on equivalence classes. Extend it
by density to a bounded linear action on all of \(L^2\). Construct
the reverse action in the same way. Passing finite transpose pairings
in the joint second-moment laws gives
\[
 \mathbb E[V W^{(\ell)}_0 U]
             =\mathbb E[U(W^{(\ell)}_0)^*V].            \tag{5.2}
\]
Density extends it to all inputs, proving that the reverse action IS
the adjoint. No independent transpose resampling occurs.

Real coefficients and additional fixed Lipschitz functions are obtained
by compact approximation and propagating errors through each finite
program using (5.1). Accordingly all real-step Euler programs (4.3)
live on these same spaces with their proved laws. The operator state
does not grow with the mesh. Its trained increments retain their entire
rank-one integral in the CURRENT operator.

Let \(\Theta=(X^{(1)},W^{(2)},W^{(3)},W^{(4)})\), with distance
\[
 d(\Theta,\widetilde\Theta)=
 \|X^{(1)}-\widetilde X^{(1)}\|_2+
 \|W^{(2)}-\widetilde W^{(2)}\|_{\rm op}+
 \|W^{(3)}-\widetilde W^{(3)}\|_{\rm op}+
 \|W^{(4)}-\widetilde W^{(4)}\|_2.                      \tag{5.3}
\]
Vector norms here are on their own population spaces. At the same
finite width use the identical expression with each vector norm
divided by \(\sqrt n\), denoting it by \(d_n\).
Define the feature-time clipped vector field
\[
 \mathcal V_R(\Theta)=
 (q_R^{(1)},\delta_R^{(2)}\otimes H^{(1)},
       \delta^{(3)}\otimes H^{(2)},H^{(3)}),\quad
 \delta_R^{(2)}=\phi'(Z^{(2)})\tau_R(q^{(2)}).           \tag{5.4}
\]
All other forward and backward quantities are computed from the present
state. Write \(R=\infty\) for the identity map. Clipped flows are not
assumed to be gradient flows.

For a horizon \(S\), initial operator bound \(M_0\), and initial readout
\(L^2\) norm at most one, the following COARSE bounds suffice:
\[
 Q_0=1+aS,\quad R_3=M_0+aQ_0S,\quad
 R_2=M_0+aR_3Q_0S.                                    \tag{5.5}
\]
They bound the readout norm and the two operator norms for a flow or
any positive-step Euler prefix of total length at most \(S\). To prove
them, first integrate/sum \((W^{(4)})'=H^{(3)}\), then use
\(\|\delta^{(3)}\|_2\le\|W^{(4)}\|_2\) and the rank-one bound
\(\|U\otimes V\|=\|U\|_2\|V\|_2\). Next use
\(\|\delta_R^{(2)}\|_2\le\|q^{(2)}\|_2
\le R_3Q_0\). Finally \(\|q_R^{(1)}\|_2\le R_2R_3Q_0\).
The first coordinate is bounded by its initial norm plus the integral
of this last bound. Thus all four velocities are bounded by a finite
constant \(C_S\), independent of clipping and width. From zero
readout there is the stronger pointwise bound
\[
 ms\le W^{(4)}(s)\le as.                              \tag{5.6}
\]

We spell out the stability used below. Bounded activations and (2.1)
give, for two states with these primal bounds,
\[
 \|Z^{(2)}_A-Z^{(2)}_B\|_2
 \le a\|W^{(2)}_A-W^{(2)}_B\|_{\rm op}
              +(R_2/100)\|X^{(1)}_A-X^{(1)}_B\|_2,
\]
and then \(\|Z^{(3)}_A-Z^{(3)}_B\|_2\le C_S d(A,B)\).
If the REFERENCE readout \(W^{(4)}_B\) has pointwise bound \(B_0\),
write the top difference with that readout multiplying the gate
difference. It yields
\[
 \|\delta^{(3)}_A-\delta^{(3)}_B\|_2
 \le\tfrac1{10}\|W^{(4)}_A-W^{(4)}_B\|_2
                +\tfrac{B_0}{5}\|Z^{(3)}_A-Z^{(3)}_B\|_2,
\]
\[
 \|\delta^{(3)}_A-\delta^{(3)}_B\|_2
       +\|q^{(2)}_A-q^{(2)}_B\|_2\le C_S d(A,B).       \tag{5.7}
\]
No pointwise bound on the other readout is needed. For two states
clipped at \(R\),
\[
 \|\delta_R^{(2)}(A)-\delta_R^{(2)}(B)\|_2
 \le\tfrac1{10}\|q_A^{(2)}-q_B^{(2)}\|_2
                       +\tfrac{2R}{5}\|Z_A^{(2)}-Z_B^{(2)}\|_2.
\]
Using reverse operator bounds and
\[
 \|U\otimes V-\widetilde U\otimes\widetilde V\|
 \le\|U-\widetilde U\|_2\|V\|_2+
                  \|\widetilde U\|_2\|V-\widetilde V\|_2,
\]
we obtain \(\|\mathcal V_R(A)-\mathcal V_R(B)\|
\le C_S(1+R)d(A,B)\). Every displayed inequality is valid at finite
width with the same constants and the specified norm factors.

For fixed \(R\), iterate the integral equations on a short time
interval in continuous paths with slightly enlarged primal bounds and
the pointwise constraint (5.6). This set is closed: an \(L^2\)-convergent
sequence has an almost-everywhere convergent subsequence preserving a
common pointwise bound. The readout integral preserves (5.6). The
velocity bound preserves the other enlarged bounds for a short enough
interval; the Lipschitz estimate makes the integral map a contraction
there. Its iterates converge geometrically to a unique fixed point.
Bounds (5.5) permit finitely many such restarts on every fixed \([0,S]\).
Thus the fixed-clip flow exists globally in feature time. The same
proof works at finite width. Uncut finite-dimensional feature flows
also exist on every fixed feature interval: the vector field is smooth,
and (5.5) prevents escape from finite bounded parameter sets.

For fixed clipping, integrating the Lipschitz field along one exact
step bounds its Euler defect by \(C_{R,S}\Delta^2\). Recursion (2.5)
therefore gives
\[
 \sup_{s\le S}d(\Theta_{R,\Delta}(s),\Theta_R(s))
            \le C_{R,S}\Delta,                         \tag{5.8}
\]
with the same finite-width bound on the initial norm event. Values
inside a step are controlled by the velocity bound. Fixed-program
convergence of Section 4, followed by (5.8), proves the fixed-clip width
limit: first fix the mesh, let width tend to infinity, then refine the
mesh. This also holds for any fixed finite probe program and joint time
list, by propagating its Lipschitz and operator-norm bounds. Time
equicontinuity and a finite time net upgrade fixed-time convergence
to uniform convergence in those finitely many time arguments.

## 6. A quantitative response estimate on feature time [0,3/2]

For the exact scalar programs (4.3)--(4.5), put
\[
 U_k=\sum_{s\le k}|b^{(2)}_{ks}|,\qquad
 V_k=\sum_{s\le k}|b^{(3)}_{ks}|.
\]
We prove, for EVERY \(R,M,\Delta\) with \(S=M\Delta\le3/2\),
\[
 U_k<9/10,\qquad V_k\le3067/3200<1,\qquad k\le M.       \tag{6.1}
\]
The point is uniformity in both mesh and clipping. No derivative of a
covariance square root is involved: all the derivatives below hold
the deterministic scalar coefficients fixed as in (4.5).

At time zero the readout is identically zero as a formal expression,
so \(\delta^{(3)}_0\) and its derivatives vanish. Its reverse source
has variance zero and \(b^{(3)}_{00}=0\). Since \(\tau_R(0)=0\),
\(\delta^{(2)}_0=0\), and its \(\xi^{(2)}_0\) derivative also
vanishes. Therefore \(U_0=V_0=0\). This does not set formal
derivatives in a degenerate backwards-source direction to zero merely
because that Gaussian source happens to be zero.

Suppose all rows strictly before \(k\) satisfy \(U_r,V_r\le1\).
Write \(A=3/2\), distinct from the activation upper bound \(a=7/6\).
For a fixed bottom source \(\zeta^{(1)}_s\), differentiating gives
\[
 \left|\frac{\partial X^{(1)}_j}{\partial\zeta^{(1)}_s}\right|
 \le\Delta\mathbf1_{s<j}+
 \frac\Delta{100}\sum_{r<j}\sum_{v\le r}|b^{(2)}_{rv}|
     \left|\frac{\partial X^{(1)}_v}{\partial\zeta^{(1)}_s}\right|.
\]
By (2.5), for \(s<j\le k\),
\[
 \left|\frac{\partial H^{(1)}_j}{\partial\zeta^{(1)}_s}\right|
 \le\frac\Delta{100}e^{S/100},\qquad
 |a^{(2)}_{js}|\le\Delta[a^2+e^{S/100}/100]<A\Delta.    \tag{6.2}
\]
The last inequality uses \(e^{3/200}<2\) and
\(49/36+1/50<3/2\). No bound on a realization of \(q^{(1)}\) is
used; the single source carries a factor of \(\Delta\).

For the middle forward source row set
\[
 \mathcal R_j=\sum_{s\le j}
    \left|\frac{\partial Z^{(2)}_j}{\partial\xi^{(2)}_s}\right|,
 \quad
 E_j=\exp\left\{A\Delta\sum_{r<j}
                 \left(\frac{|q^{(2)}_r|}{5}+\frac{V_r}{100}\right)
          \right\}.
\]
The exact gate derivative satisfies
\[
 |\partial\delta^{(2)}_r|
 \le\tfrac15|q^{(2)}_r||\partial Z^{(2)}_r|
                   +\tfrac1{10}|\partial q^{(2)}_r|.
\]
For a \(\xi^{(2)}\) derivative,
\[
 |\partial q^{(2)}_r|
 \le\tfrac1{10}\sum_{v\le r}|b^{(3)}_{rv}|
                                      |\partial Z^{(2)}_v|.
\]
Thus (6.2), summation over source indices, and (2.5) give
\[
 \mathcal R_j\le1+A\Delta\sum_{r<j}
       (|q^{(2)}_r|/5+V_r/100)\max_{v\le r}\mathcal R_v,
 \quad \max_{v\le j}\mathcal R_v\le E_j.               \tag{6.3}
\]
The direct derivative of \(\xi^{(2)}_j\) contributes one in this
row sum, not one for every past source.
For a single \(\zeta^{(2)}_s\) derivative, the extra term in
\(\partial q^{(2)}_r\) is \(\mathbf1_{r=s}\). Its first contribution
to the forward recursion has size at most \(A\Delta/10\).
The same comparison therefore gives
\[
 \left|\frac{\partial Z^{(2)}_j}{\partial\zeta^{(2)}_s}\right|
 \le\frac{A\Delta}{10}E_j,\qquad
 \left|\frac{\partial H^{(2)}_j}{\partial\zeta^{(2)}_s}\right|
 \le\frac{A\Delta}{100}E_j,\quad s<j\le k.             \tag{6.4}
\]
There is no dependence on \(\zeta^{(2)}_j\) in \(Z^{(2)}_j\).

We bound moments of the envelope, not its pointwise supremum over
neurons. Bounded activation gives
\[
 |W^{(4)}_r|\le aS,\quad |\delta^{(3)}_r|\le aS/10,
 \quad\operatorname{Var}(\zeta^{(2)}_r)\le(aS/10)^2\le(7/40)^2,
\]
and \(|q^{(2)}_r|\le|\zeta^{(2)}_r|+aV_r\).
For a centered scalar Gaussian of variance \(v\),
\(\mathbb E e^{\lambda|G|}\le
\mathbb E(e^{\lambda G}+e^{-\lambda G})=2e^{\lambda^2v/2}\).
For \(j>0\), Jensen over the \(j\) time slots gives
\[
 \exp\left(\frac{pA\Delta}{5}\sum_{r<j}|\zeta^{(2)}_r|\right)
 \le\frac1j\sum_{r<j}\exp(pAj\Delta|\zeta^{(2)}_r|/5).
\]
Consequently for \(p\ge1\),
\[
 \mathbb E E_j^p
 \le2\exp\left\{pAS(a/5+1/100)
             +\tfrac12(pAS/5)^2(aS/10)^2\right\}
 \le2\exp\left\{\frac{219p}{400}
                    +\frac{3969p^2}{1280000}\right\}. \tag{6.5}
\]
For \(j=0\), \(E_0=1\). Temporal correlations and singular covariances
cause no problem: only marginal Gaussian variances were used.
The response shift need not be independent of its source.
For \(p=1,2\), the exponent after taking the \(p\)-th root is
less than \(3/5\). Since \(e<3\) and \(3^3<2^5\), \(e^{3/5}<2\).
Thus
\[
 \|E_j\|_1<4,\quad \|E_j\|_2<3,
 \qquad |a^{(3)}_{js}|\le\Delta(a^2+4A/100)
                         <A\Delta.                   \tag{6.6}
\]
Here the last bound follows from (6.4) and the definition of \(a^{(3)}\);
numerically its coefficient is \(49/36+3/50<3/2\).

For the top forward source row put
\(T_j=\sum_{s\le j}|\partial Z^{(3)}_j/\partial\xi^{(3)}_s|\).
Differentiating the readout sum and the top gate gives
\[
 \sum_{s\le j}\left|
          \frac{\partial\delta^{(3)}_j}{\partial\xi^{(3)}_s}\right|
 \le\frac\Delta{100}\sum_{r<j}T_r+\frac{aS}{5}T_j
 \le\frac{73}{300}S\max_{v\le j}T_v.
\]
Together with (6.6) and the strictly past-time top recursion this yields
\[
 \max_{v\le j}T_v\le\exp\{A(73/300)S^2\}
              \le e^{657/800}<5/2.
\]
For the numerical comparison, \(657/800<5/6\) and
\(e^{5/6}<3^{5/6}<5/2\), since \(3^5 2^6<5^6\).
Adding the learned covariance terms in (4.5) now proves
\[
 V_k\le(73/300)S(5/2)+a^2S^3/100
       \le73/80+147/3200=3067/3200<1.                  \tag{6.7}
\]
This obtains the CURRENT top backwards row using only past rows.
It follows, before any estimate on the current \(U_k\), that
\[
 \|q^{(2)}_k\|_2\le aS/10+aV_k\le161/120=:Q,
 \qquad\|\delta^{(2)}_k\|_2\le Q/10.                  \tag{6.8}
\]
The same bounds apply at every earlier index under the induction.
For the current middle derivative row, (6.3) and the complete current
return in (4.6) give
\[
 \sum_{s\le k}\left|
       \frac{\partial\delta^{(2)}_k}{\partial\xi^{(2)}_s}
                 \right|
 \le (|q^{(2)}_k|/5+V_k/100)E_k.
\]
Cauchy--Schwarz, \(\|E_k\|_1\le\|E_k\|_2<3\), and (6.8) show
\[
 U_k\le3(Q/5+1/100)+SQ^2/100
 \le\frac{167}{200}+\frac{77763}{2880000}
 =\frac{2482563}{2880000}<9/10.                         \tag{6.9}
\]
No current \(U_k\) has been used in (6.7) or (6.9). The induction order
is \(a^{(2)}_{k\cdot},H^{(2)}_k,a^{(3)}_{k\cdot},\delta^{(3)}_k,
b^{(3)}_{k\cdot},q^{(2)}_k,\delta^{(2)}_k,b^{(2)}_{k\cdot}\).
The premises hold at zero and the current conclusions are strictly
below one, completing simultaneous induction and proving (6.1).

In particular the ACTUAL identified scalar query satisfies
\[
 q^{(2)}_k=\zeta^{(2)}_k+\beta_k,\quad
 |\beta_k|\le7/6,\quad \operatorname{Var}(\zeta^{(2)}_k)\le(7/40)^2.
                                                               \tag{6.10}
\]
For \(x>0\), \(\mathbb P(|q^{(2)}_k|>7/6+x)
\le2e^{-x^2/[2(7/40)^2]}\). A convenient explicit exponential-square
bound is
\[
 \mathbb E e^{(q^{(2)}_k)^2/16}
 \le e^{49/288}\mathbb E e^{(\zeta^{(2)}_k)^2/8}
 \le e^{49/288}(1-49/6400)^{-1/2}<2.                   \tag{6.11}
\]
We used \((u+v)^2\le2u^2+2v^2\); the Gaussian integral is obtained
by combining its two quadratic exponents. The last inequality follows
from \(e^{49/288}<e^{1/5}\le5/4\) and the remaining factor \(<4/3\).
It is uniform in mesh, time index and clipping. It is not a bound on
the maximum over all source times.

## 7. Removal of clipping, existence, and restart in feature time

Fix \(S=3/2\). For each fixed \(R\), (5.8) and (5.7) give
\(q^{(2)}_{R,\Delta}(s)\to q_R^{(2)}(s)\) in \(L^2\) at every
fixed time, using mesh nodes approaching that time. Taking an
almost-everywhere convergent subsequence and Fatou in (6.11) gives
\[
 \sup_{R,s\le S}\mathbb E\exp((q_R^{(2)}(s))^2/16)\le2. \tag{7.1}
\]
Subsequences at different times may differ; the deterministic moment
bound holds at every time with the same constant. No joint almost-sure
statement in \(R,s\) is required.

The crucial comparison is asymmetric. Let \(A\) be an uncut state,
or one using a clip \(R'\ge R\); let \(B\) use clip \(R\) and
have the bounded reference readout. Exactly,
\[
 \begin{split}
 \delta_{R'}^{(2)}(A)-\delta_R^{(2)}(B)
 ={}&\phi'(Z_A^{(2)})[\tau_{R'}(q_A^{(2)})-\tau_{R'}(q_B^{(2)})]\\
 &+[\phi'(Z_A^{(2)})-\phi'(Z_B^{(2)})]\tau_R(q_B^{(2)})\\
 &+\phi'(Z_A^{(2)})[\tau_{R'}(q_B^{(2)})-\tau_R(q_B^{(2)})].
 \end{split}                                                    \tag{7.2}
\]
The last bracket vanishes on \(|q_B^{(2)}|\le R\) and elsewhere
has absolute value at most \(2|q_B^{(2)}|\). Put
\(b_R(q)=(|q|-R/2)_+\); then
\(|q|\mathbf1_{|q|>R}\le2b_R(q)\). Section 5's bounds show both
\[
 \|\delta_{R'}^{(2)}(A)-\delta_R^{(2)}(B)\|_2
 \le C(1+R)d(A,B)+C\|b_R(q_B^{(2)})\|_2
\]
and
\[
 \|\mathcal V_{R'}(A)-\mathcal V_R(B)\|
 \le C(1+R)d(A,B)+C\|b_R(q_B^{(2)})\|_2.               \tag{7.3}
\]
The constant depends on primal bounds and the reference readout bound,
not on \(R'\), and requires no tail estimate for \(A\).

If \(\mathbb E e^{q^2/K^2}\le2\), then
\[
 \mathbb E[q^2\mathbf1_{|q|>u}]
 \le4K^2 e^{-u^2/(2K^2)}.
\]
Indeed \(q^2e^{-q^2/(2K^2)}\le2K^2/e\); factor the remaining
exponential on the tail and apply the assumed moment. Since
\(b_R(q)^2\le q^2\mathbf1_{|q|>R/2}\), (7.1), with \(K=4\), gives
\[
 \sup_{s\le S}\|b_R(q_R^{(2)}(s))\|_2
 \le2K e^{-R^2/(16K^2)}=:\varepsilon_R.                \tag{7.4}
\]
Subtract the integral equations for \(\Theta_{R'}\) and \(\Theta_R\)
and apply (2.5)'s continuous version to (7.3). For common initial data,
\[
 \sup_{s\le S}d(\Theta_{R'}(s),\Theta_R(s))
 \le CS e^{C(1+R)S}\varepsilon_R.                      \tag{7.5}
\]
This tends to zero as \(R\to\infty\), uniformly in \(R'\ge R\).
The continuous-path space in the Banach state norm (5.3) is complete,
so there is a uniform limit \(\Theta\). It retains (5.5)--(5.6).
By (5.7) its computed \(q^{(2)}\) is the \(L^2\) limit of the clipped
queries. Evaluate (7.3) with \(A=\Theta\), using \(R'=\infty\),
and \(B=\Theta_R\). The factor \(1+R\) times (7.5) still tends to
zero. Thus the clipped velocities converge uniformly to the ACTUAL
uncut vector field of \(\Theta\). Pass the integral equations to
the limit. It follows that \(\Theta\) is a continuously differentiable
uncut feature flow on the WHOLE interval \([0,3/2]\). This step does
not pass an unbounded product by weak convergence.

Let \(\widetilde\Theta\) be any other continuous bounded-primal uncut
integral solution with the same initial state. Apply (7.3) against
\(\Theta_R\). Its own bounds only change the finite constant in
Gronwall. Since \(e^{CR}\varepsilon_R\to0\) for EVERY fixed \(C\),
the solutions agree. For a restart at feature time \(\sigma<S\),
the initial discrepancy from \(\Theta_R(\sigma)\) is at most
\(C_0 e^{C_0R}\varepsilon_R\) by (7.5). The comparison on
\([\sigma,S]\) adds only another \(e^{C_1R}\), still vanishing.
Thus restart is unique on every remaining part of the constructed
feature interval. There is no assumption of global local-Lipschitzness
of the uncut vector field on arbitrary \(L^2\) neighborhoods.

## 8. The finite uncut feature-flow limit

Let \(\Theta_{n,R}\) be the finite clipped flow with the actual hidden
initialization and ZERO initial readout. Its fixed-clip limit has been
proved in Section 5. Define
\[
 a_{n,R}(s)=\left(\frac1n\sum_i
                b_R(q^{(2)}_{n,R,i}(s))^2\right)^{1/2},
 \quad a_R(s)=\|b_R(q_R^{(2)}(s))\|_2.
\]
For each fixed \(R\), joint \(\mathcal W_2\) convergence gives
\(a_{n,R}(s)\to a_R(s)\) at each time. The state velocity bounds
and (5.7) make the reference query uniformly Lipschitz in time in its
vector norm. Since \(b_R\) is 1-Lipschitz, the same is true of
\(a_{n,R}\) and \(a_R\). A finite time net therefore proves
\[
 \sup_{s\le S}|a_{n,R}(s)-a_R(s)|\longrightarrow0
                  \quad\hbox{in probability}.         \tag{8.1}
\]
This is a continuous quadratic-growth measurement; no discontinuous
tail indicator or finite-width exponential moment is being assumed.

Let \(\Theta_n^{\rm GF}\) be the uncut finite FEATURE flow with
the prescribed small readout. Its existence follows from (5.5) and
finite-dimensional smoothness. Couple it to \(\Theta_{n,R}\) with
the same hidden roots and matrices. The same-width version of (7.3) gives
\[
 \sup_{s\le S}d_n(\Theta_n^{\rm GF}(s),\Theta_{n,R}(s))
 \le e^{C(1+R)S}\left[
     \frac{\|W^{(4)}_0\|_2}{\sqrt n}
                   +C\int_0^S a_{n,R}(u)du\right].      \tag{8.2}
\]
The common initial matrix event has probability tending to one by
(2.2), and the readout term is \(O_{\mathbb P}(n^{-1})\). Only the
ZERO-readout reference must satisfy the pointwise readout bound.
At each fixed \(R\), (8.1) and (7.4) bound the limiting right-hand
side by \(CS e^{C(1+R)S}\varepsilon_R\). Letting \(R\to\infty\),
combining fixed-clip laws with (7.5) and (2.3), proves the uncut
finite-feature-flow limit on \([0,3/2]\).

For later use this comparison also controls \(\delta^{(2)}\), not
just the state: use the first inequality after (7.2). The additional
factor \(1+R\) in its error is still absorbed by the Gaussian tail.
Then bounded reverse operators control \(q^{(1)}\). These two named
backward fields consequently have joint \(\mathcal W_2\) limits,
uniformly in time and for finite joint time lists. Products with bounded
gates follow by truncating the unbounded factor and using Section 2.
This supplies the input for the observable proof in Section 11.

## 9. Actual gradient structure and all finite physical times

The initial Gaussian operators need not be Hilbert--Schmidt. Their
TRAINED increments are: for an orthonormal basis \((e_j)\) of an
operator's input space define
\(\|A\|_{\rm HS}^2=\sum_j\|Ae_j\|_2^2\).
Parseval makes this definition independent of the basis and gives
\(\|U\otimes V\|_{\rm HS}=\|U\|_2\|V\|_2\).
Integrating the continuous rank-one velocities yields finite HS
increments. The rank-one difference inequality holds in HS norm too,
so their clipped integrals converge in HS norm to the same increments
already obtained in operator norm.

In raw coordinates use the affine Hilbert parameter space with squared
variation norm
\[
 \mathbb E[(dZ^{(1)})^2]+\|dW^{(2)}\|_{\rm HS}^2
       +\|dW^{(3)}\|_{\rm HS}^2+\mathbb E[(dW^{(4)})^2].
                                                               \tag{9.1}
\]
The predictor is continuously Frechet differentiable on this affine
space. Here is the needed proof, avoiding a false unrestricted
\(L^2\)-nonlinearity derivative assertion. For fixed \(B\in L^2\),
Taylor's formula and bounded \(\phi',\phi''\) give
\[
 |\mathbb E B[\phi(Z+v)-\phi(Z)-\phi'(Z)v]|
 \le C R\|v\|_2^2+
             C\|B\mathbf1_{|B|>R}\|_2\|v\|_2.         \tag{9.2}
\]
Use the quadratic bound on \(|B|\le R\), the linear remainder bound
on its complement, and Cauchy--Schwarz. First fix \(R\), let
\(\|v\|_2\to0\), then let \(R\to\infty\). The remainder is
\(o(\|v\|_2)\).
Forward differences are \(O(\|d\theta\|)\) in \(L^2\), since
\(\|dW\|_{\rm op}\le\|dW\|_{\rm HS}\) and activations are bounded
and Lipschitz. Expand the scalar predictor from the top down, applying
(9.2) first with the old readout, then with the old reverse coefficient
\((W^{(3)})^*\delta^{(3)}\), then with
\((W^{(2)})^*\delta^{(2)}\). Each belongs to \(L^2\).
Terms with both a matrix change and an activation change, or a readout
change and top activation change, are \(O(\|d\theta\|^2)\).
This proves
\[
 df=\mathbb E[\delta^{(1)}dZ^{(1)}]
       +\mathbb E[\delta^{(2)}dW^{(2)}H^{(1)}]
       +\mathbb E[\delta^{(3)}dW^{(3)}H^{(2)}]
       +\mathbb E[H^{(3)}dW^{(4)}].                    \tag{9.3}
\]
The HS identity \(\langle U\otimes V,A\rangle_{\mathrm{HS}}
=\mathbb E[UAV]\) follows by expanding in an orthonormal basis.
Thus
\[
 \nabla f=(\delta^{(1)},\delta^{(2)}\otimes H^{(1)},
                  \delta^{(3)}\otimes H^{(2)},H^{(3)}). \tag{9.4}
\]
For gradient continuity use forward continuity, then (2.4) on the
fixed old readout and fixed old backward factors, successively in
reverse order. Matrix actions converge in operator norm. This proves
continuity without an uncut local-Lipschitz assertion.

The feature flow constructed in Section 7 obeys
\((Z^{(1)})'=\phi'(Z^{(1)})q^{(1)}\). The inverse-coordinate chain
rule follows from (2.4) or from coordinate absolute continuity and the
bounded derivative of \(F^{-1}\). Together with (5.4), it gives
\(\theta_s=\nabla f\). Consequently
\[
 f_s=K^{(1)}+K^{(2)}+K^{(3)}+K^{(4)},
\]
\[
 K^{(1)}=\mathbb E[(\delta^{(1)})^2],\quad
 K^{(2)}=\mathbb E[(\delta^{(2)})^2]\mathbb E[(H^{(1)})^2],
\]
\[
 K^{(3)}=\mathbb E[(\delta^{(3)})^2]\mathbb E[(H^{(2)})^2],\quad
 K^{(4)}=\mathbb E[(H^{(3)})^2]\ge25/36.                \tag{9.5}
\]
All terms are continuous and bounded on \([0,3/2]\), by the primal
bounds and (2.4). Initially \(f(0)=0\). There is exactly one
\(s_*\in(0,36/25]\) with \(f(s_*)=1\), since \(f_s\ge25/36\).
In particular \(s_*<3/2\).

For \(s<s_*\), define
\[
 t(s)=\int_0^s\frac{du}{2(1-f(u))}.
\]
If \(B_*=\sup_{[0,s_*]}f_s\), then
\(1-f(s)\le B_*(s_*-s)\), so
\(t(s)\ge(2B_*)^{-1}\log(s_*/(s_*-s))\to\infty\).
The increasing function has an inverse for every \(t\ge0\), satisfying
\[
 s_t=2(1-f(s)),\quad s(0)=0,
 \quad s_*-s(t)\ge s_*e^{-2B_*t}>0.                   \tag{9.6}
\]
Uniqueness follows by separation of variables, or the Lipschitz scalar
comparison of Section 2. Thus EVERY finite physical interval stays
inside the single constructed feature interval. In physical time
\[
 \theta_t=-2(f-1)\nabla f=-\nabla (f-1)^2,
 \quad f_t=-2(f-1)\sum_\ell K^{(\ell)},
 \quad L_t=-4(f-1)^2\sum_\ell K^{(\ell)}.              \tag{9.7}
\]
This is the actual gradient flow in (9.1).

Raw physical uniqueness needs verification for competitors not initially
assumed in the transformed class. For any continuous bounded-primal raw
integral solution, (2.4) makes its backward fields continuous in \(L^2\).
The rank-one integral equations put its matrix increments in HS, so
(9.3) applies to its raw parameter curve. Its deficit satisfies
\[
 1-f(t)=(1-f(t_0))\exp\left(-2\int_{t_0}^t
                                        \sum_\ell K^{(\ell)}(u)du\right).
\]
The kernel is bounded on each competing compact interval; a positive
initial deficit cannot vanish at finite time. Choose absolutely
continuous scalar coordinate versions of its first raw field, by
integrating its \(L^2\) velocity and Fubini. The pointwise chain rule gives
\[
 F(Z^{(1)}(t))=F(Z^{(1)}(t_0))+
                   \int_{t_0}^t2(1-f(u))q^{(1)}(u)du.  \tag{9.8}
\]
Its right side is in \(L^2\), proving the required transformed
membership. The strictly increasing feature clock therefore makes it
an uncut feature solution. Section 7 identifies it until any first
attempt to leave \([0,s_*)\); scalar-clock uniqueness and (9.6) exclude
such an exit. This applies from zero and from every reached state, with
the absolute feature start \(\sigma=s(t_0)\). It proves global physical
uniqueness and restart in the theorem's class. All present velocities
are functions of the four present objects. No Gaussian source or
response coefficient in the proof is an extra dynamical input.

## 10. Exact raw GD and the physical finite-width comparison

We first note that finite physical GF exists for every finite horizon.
Its finite raw gradient has squared length \(\sum_\ell K_n^{(\ell)}\)
when vector variations use squared norm \(\|v\|_2^2/n\) and matrix
variations use ordinary squared Frobenius norm. Differentiating the
finite predictor verifies the four entries in (1.3), so the finite
deficit solves \((1-f_n)'=-2(1-f_n)\sum K_n^{(\ell)}\).
On its existence interval \(|r_n(t)|\le|r_n(0)|\). Integrating the
readout equation therefore bounds its vector norm by its initial
norm plus \(2a|r_n(0)|t\). Integrating the matrix-3 norm bound next,
then matrix 2, then the first-vector velocity, gives polynomial bounds
on every finite compact physical interval. At fixed width these bound
all coordinates. The smooth finite-dimensional equations can be
continued by the local contraction construction, so no finite-time
escape occurs. Exact GD is defined at every finite step by (1.3).

On the high-probability event of (2.2) and small initial readout, the
finite FEATURE GF on \([0,S]\), \(S=3/2\), has bounded continuous
kernel and satisfies \(df_n/ds\ge25/36\). Its initial predictor
tends to zero. If \(f_n(0)>-1/24\) and \(f_n(0)<1\), its unique
level-one point occurs before \(S\). The scalar physical clock
therefore stays inside \([0,S]\), by the same nonattainment argument
as (9.6). Section 8 gives uniform feature-predictor convergence.
The output is Lipschitz in (5.3) on bounded states, by expanding
\(\mathbb E[W^{(4)}H^{(3)}]\) and using Cauchy--Schwarz.
It is consequently Lipschitz in feature time with a uniform bound.
The scalar-clock comparison from Section 2, applied to the finite
and population predictors, proves uniform convergence of their clocks
on each fixed \([0,T]\). This identifies finite physical GF.

For exact GD a separate positive-step argument is required. Fix
\(T<\infty\), let \(N_n=\lceil T/\eta_n\rceil\), and use the
population path on \([0,T+1]\). Put
\[
 \rho=\min_{0\le t\le T+1}(1-f(s(t)))>0,
 \quad S_b=147/100,
 \quad \alpha_k=2\eta_n(1-f_{n,k}),\quad s_0=0.
\]
As long as the increments are positive set \(s_{k+1}=s_k+\alpha_k\).
Stop at the first node \(j\le N_n\) with
\(f_{n,j}\ge1-\rho/2\) or \(s_j\ge S_b\); if none occurs,
stop at \(N_n\). Before a bad node, \(\alpha_k>0\).
Initialization is good with probability tending to one, since
\(f_{n,0}\to0\), \(s_0=0\), and \(1-\rho/2\ge1/2\).

The raw matrix and readout updates on a positive prefix satisfy (5.5)
whenever its accumulated step is bounded by \(S_b\); this uses only
bounded activations and gates, not an exact Euler identity for \(F\).
They give \(|f_{n,k}|\le a(1+aS_b)\) and hence
\(0<\alpha_k\le C\eta_n\). The step INTO the first bad node is
therefore positive with endpoint at most \(S_b+C\eta_n<S\) for
large \(n\). Every estimate below includes that endpoint and uses
only the preceding good nodes.

For a raw scalar step \(z_+=z+\alpha\phi'(z)q\), the cubic identity is
\[
 \begin{split}
 F(z_+)-F(z)
 ={}&\alpha q+10\alpha^2z(\phi'(z))^2q^2
                 +\frac{10}{3}\alpha^3(\phi'(z))^3q^3.
 \end{split}                                                    \tag{10.1}
\]
This explicitly shows why raw GD is not transformed Euler. The primal
bounds give \(\|q^{(1)}_{n,k}\|_2/\sqrt n\le C\), while
\(\sup_z|z|(\phi'(z))^2<\infty\).
Since \(\|q^2\|_2\le\|q\|_2^2\) and
\(\|q^3\|_2\le\|q\|_2^3\), the extra vector's norm divided by
\(\sqrt n\) is at most \(C(\alpha_k^2\sqrt n+\alpha_k^3 n)\).
Summing any stopped prefix of total feature time at most \(S\) gives
\[
 C_S(\eta_n\sqrt n+\eta_n^2 n)
       =O(n^{-3/2}+n^{-3})\longrightarrow0.             \tag{10.2}
\]
There is no unproved fourth or sixth empirical-moment assumption here.

Compare the transformed GD nodes with the exact finite clipped reference
\(\Theta_{n,R}(s_k)\). Let their same-width distance be \(d_k\).
Section 7's asymmetric inequality, the clipped local Euler error, and
(10.1) give
\[
 d_{k+1}\le[1+C(1+R)\alpha_k]d_k
       +C\alpha_k a_{n,R}(s_k)+C_R\alpha_k^2
       +C(\alpha_k^2\sqrt n+\alpha_k^3n).               \tag{10.3}
\]
This is valid through the first stopped endpoint. The partition may
be random. Its tail forcing still obeys a PATHWISE bound, because
\(a_{n,R}\) is time-Lipschitz:
\[
 \sum_{k<J}\alpha_k a_{n,R}(s_k)
 \le\int_0^{s_J}a_{n,R}(u)du+CS\max_{k<J}\alpha_k
 \le\int_0^S a_{n,R}(u)du+C_S\eta_n.                  \tag{10.4}
\]
Applying (2.5) to (10.3) yields
\[
 \max_{k\le J}d_k\le e^{C(1+R)S}
 \left[\frac{\|W^{(4)}_0\|_2}{\sqrt n}
       +C\int_0^S a_{n,R}(u)du+C_R\eta_n
       +C_S(\eta_n\sqrt n+\eta_n^2n)\right].           \tag{10.5}
\]
At fixed \(R\), take width to infinity using (8.1); then remove \(R\)
using (7.4). Combining with fixed-clip predictor convergence and (7.5)
proves that the stopped predictor error
\[
 e_n:=\max_{k\le J}|f_{n,k}-f(s_k)|\longrightarrow0
                     \quad\hbox{in probability}.      \tag{10.6}
\]
These estimates are uniform over the stopped prefix and do not assume
that its width-dependent number of queries falls under Section 3.
Section 3 was used only for the fixed-clip, fixed-mesh reference limits.

Linearly interpolate the clock \(s_k\) in physical time. On a step its
slope is \(2(1-f_{n,k})\). If \(L_f\) bounds the feature-time
Lipschitz constant of the population predictor, then up through
\(J\eta_n\le T+\eta_n<T+1\),
\[
 |s_n(t)-s(t)|
 \le2\int_0^t[e_n+C L_f\eta_n+L_f|s_n(u)-s(u)|]du.
\]
Thus \(D_n:=\sup_{t\le J\eta_n}|s_n(t)-s(t)|\to0\) in probability.
At a putative first bad endpoint,
\[
 s_J\le36/25+D_n<147/100,
 \quad f_{n,J}\le1-\rho+e_n+L_fD_n<1-\rho/2
\]
with probability tending to one. Both stop conditions are contradicted.
This includes a first exit at the final interpolation node. The extra
interval \([T,T+1]\) in the definition of \(\rho\) was used for this
endpoint. Hence there is no premature stop with probability tending to
one, and (10.5)--(10.6) hold throughout the requested physical horizon.
Constants may depend on \(T\); no positive lower residual uniform as
\(T\to\infty\) is asserted.

For the specified raw interpolation, use (10.1) with a fractional step
\(0\le\alpha\le\alpha_k\). It bounds the difference between the
transform of the raw linear interpolation and the linear interpolation
of transformed nodes. All other parameter blocks already interpolate
linearly. Consequently the uniform state and predictor comparisons hold
between nodes as well.

Finally compare GD and finite GF to the SAME zero-readout finite clipped
reference at their converging clocks. Its velocity is uniformly bounded
by (5.5), so clock differences contribute only a constant times their
size. Equations (8.2) and (10.5) prove (1.7). Fixed-clip population laws,
(7.5), and these same-width comparisons give joint MF/GF/GD convergence.
For every tolerance one first chooses a sufficiently large \(R\), then
a sufficiently fine fixed reference mesh, then takes all sufficiently
large widths. This proves full-sequence convergence in probability;
the subsequences used in Fatou arguments do not select a final width
subsequence. No infinite-time/width interchange has been used.

## 11. All observations, hidden velocities, and whole paths

We give the additional unbounded-factor details. The state norm directly
controls each finite program of Lipschitz maps, bounded products, and
bounded operator calls. Section 8 and (7.2) additionally control the
middle backward field \(\delta^{(2)}\); the two operator bounds and
their differences then control \(q^{(1)}\). Their joint laws with
the forward fields converge in \(\mathcal W_2\), uniformly in time.
For a bounded continuous gate \(g(Z)\) multiplying a field \(V\),
first replace \(V\) by its clip at a fixed level. The product is
approximable by bounded Lipschitz instructions. The discarded norm is
at most \(\|g\|_\infty\|V\mathbf1_{|V|>R}\|_2\).
Section 2(b) controls this uniformly in time for the limiting compact
\(L^2\) path, and uniform \(\mathcal W_2\) convergence gives the
corresponding finite uniform tail bound in probability. A subsequent
bounded matrix call multiplies this error by at most its operator norm.
Induct through each specified finite program. This proves the additional
gate-containing measurement statements without an extra moment premise.
The same comparisons and finite time nets work for finitely many time
arguments jointly.

The output and all kernels are continuous quadratic-growth tests and
products of such converging scalar expectations. Thus (1.6), prediction,
residual and loss converge uniformly. Their limiting kernel formulas
are exactly (9.5), with no missing normalizing factor.

The exact FEATURE preactivation velocities are
\[
 (Z^{(1)})'=\phi'(Z^{(1)})q^{(1)},
\]
\[
 (Z^{(2)})'=\mathbb E[(H^{(1)})^2]\delta^{(2)}
            +W^{(2)}[(\phi'(Z^{(1)}))^2q^{(1)}],
\]
\[
 (Z^{(3)})'=\mathbb E[(H^{(2)})^2]\delta^{(3)}
            +W^{(3)}[\phi'(Z^{(2)})(Z^{(2)})'].         \tag{11.1}
\]
These follow by differentiating the forward equations, applying the
curve chain rule (2.4), and using
\((\delta^{(\ell)}\otimes H^{(\ell-1)})H^{(\ell-1)}
=\delta^{(\ell)}\mathbb E[(H^{(\ell-1)})^2]\).
Feature velocities are
\(\frac{dH^{(\ell)}}{ds}
=\phi'(Z^{(\ell)})\frac{dZ^{(\ell)}}{ds}\).
Physical velocities multiply all these formulas by \(2(1-f)\).
They are continuous \(L^2\) paths, and the previous truncation argument
gives their finite joint laws and squared norms uniformly in time at
GF times and GD left-node states.

Here is an explicit control of recomputed GD velocities between nodes.
On a good stopped prefix let \(\lambda_k=2(1-f_{n,k})\), which is
bounded independently of width. Each raw block velocity on the step
is constant. The vector velocities divided by \(\sqrt n\) and matrix
operator velocities are bounded by the primal estimates. Current
matrix norms and readout norms remain bounded by convexity of norm
along raw linear interpolation. The first preactivation velocity has
bounded norm divided by \(\sqrt n\). Differentiating
\(z^{(2)}=W^{(2)}\phi(z^{(1)})\), then
\(z^{(3)}=W^{(3)}\phi(z^{(2)})\), gives the same bound for their
recomputed velocities, using bounded features and gates. Hence every
hidden preactivation changes by at most \(C\eta_n\) in that norm
and by at most \(C\eta_n\sqrt n\) in coordinate supremum on a step.
Every gate \(\phi'\) therefore changes in coordinate supremum by at
most \(C\eta_n\sqrt n\).

For example, exactly within that step,
\[
 \dot z^{(2)}(t)=
 \lambda_k\delta^{(2)}_k
                 \frac{(h^{(1)}_k)^Th^{(1)}(t)}n
 +W^{(2)}(t)[\phi'(z^{(1)}(t))\dot z^{(1)}(t)].        \tag{11.2}
\]
The contraction difference from its left-node value is \(O(\eta_n)\)
by bounded features and their vector-norm change. The matrix difference
is \(O(\eta_n)\) in operator norm. The remaining gate difference is
\(O(\eta_n\sqrt n)\) in coordinate supremum and multiplies a left-node
velocity of bounded norm divided by \(\sqrt n\). Thus the discrepancy
from the node formula is \(O(\eta_n\sqrt n)\) in that norm.
For layer 3 repeat this argument with the already bounded layer-2
velocity and its just-controlled discrepancy; for feature velocities
multiply by the current gate and use the same supremum estimate.
This proves that ALL recomputed hidden velocities differ from their
node formulas by \(O(\eta_n\sqrt n)=O(n^{-3/2})\) uniformly on the
physical interval, on its good event. No coordinatewise bound on the
velocity itself beyond the deterministic Euclidean inequality was
assumed. It also covers the terminal-left convention. Thus the claimed
velocity laws, squared norms, and their time integrals converge for
the actual prescribed raw interpolation.

Population velocities admit jointly measurable versions, since they
are continuous into separable \(L^2\). For example approximate them
by step functions on refining time partitions in the product-space
\(L^2\) norm and choose a convergent measurable version. Integrating
them and using Fubini produces absolutely continuous scalar coordinate
paths with the required \(L^2\) values. Their squared supremum norms
have finite expectation by Cauchy--Schwarz in time.
For any absolutely continuous scalar path and its linear interpolant
\(I_\pi z\) on a partition of mesh \(|\pi|\),
\[
 \|z-I_\pi z\|_\infty^2
             \le4|\pi|\int_0^T|\dot z(t)|^2dt.         \tag{11.3}
\]
On each cell, compare the path to each endpoint by the integral of
its derivative and apply Cauchy--Schwarz; taking the maximum gives
the displayed bound. Apply it in expectation for the population and
in empirical average for finite paths. On a fixed grid the joint
\(\mathcal W_2\) laws converge; linear interpolation is a Lipschitz
map from its finite grid values into \(C([0,T])\). The integrals on
the right of (11.3) are uniformly bounded and converge by the velocity
result. A triangle inequality, first taking width to infinity and then
\(|\pi|\to0\), proves \(\mathcal W_2(C([0,T]))\) convergence.
The Lipschitz activation transfers it to feature paths. This proves
all convergence assertions of the theorem.

## 12. Genuine nonlinear feature learning

### 12.1 Initial transpose laws and positive movement coefficients

Let \(m_0=1\), \(m_\ell=\mathbb E[(H^{(\ell)}_0)^2]\).
The initial forward laws from Section 3 are
\[
 Z^{(\ell)}_0\sim N(0,m_{\ell-1}),\quad
 m_\ell=1+\frac1{100}\mathbb E[
         \arctan(\sqrt{m_{\ell-1}}G)^2]>1.              \tag{12.1}
\]
The Gaussian symmetry is used here only at initialization; the constant
term in the full second moment is retained. On the three respective
populations define
\[
 B^{(3)}=H^{(3)}_0\phi'(Z^{(3)}_0),\quad
 B^{(2)}=\phi'(Z^{(2)}_0)(W^{(3)}_0)^*B^{(3)},\quad
 B^{(1)}=\phi'(Z^{(1)}_0)(W^{(2)}_0)^*B^{(2)},
\]
\[
 V^{(1)}=B^{(1)},\quad
 V^{(2)}=m_1B^{(2)}+W^{(2)}_0[\phi'(Z^{(1)}_0)B^{(1)}],
\]
\[
 V^{(3)}=m_2B^{(3)}+W^{(3)}_0[\phi'(Z^{(2)}_0)V^{(2)}]. \tag{12.2}
\]
All these variables are square-integrable by bounded gates and operators.
Apply (3.2) to the initial third matrix, its input \(H^{(2)}_0\),
and reverse input \(B^{(3)}\). In the joint layer-2 law,
\[
 (W^{(3)}_0)^*B^{(3)}=c_3H^{(2)}_0+\sigma_3G_2,
 \quad \sigma_3^2=\mathbb E[(B^{(3)})^2]>0,
\]
\[
 c_3=\frac{\mathbb E[Z^{(3)}_0B^{(3)}]}{m_2}
 =\frac1{100m_2}\mathbb E\frac{Z^{(3)}_0\arctan Z^{(3)}_0}
                                     {1+(Z^{(3)}_0)^2}>0.        \tag{12.3}
\]
Here \(G_2\) is independent of \(Z^{(2)}_0\). The offset term
\(\mathbb E[Z^{(3)}_0/(1+(Z^{(3)}_0)^2)]/10\) vanishes by Gaussian
symmetry; the remaining integrand is positive off zero. It would be
incorrect to assert \(z\phi(z)\phi'(z)>0\) for all negative \(z\).
It follows that
\[
 \sigma_2^2:=\mathbb E[(B^{(2)})^2]
 =\mathbb E[(\phi'(Z^{(2)}_0))^2
            (c_3^2\phi(Z^{(2)}_0)^2+\sigma_3^2)]>0.     \tag{12.4}
\]
For the second transpose, at finite width condition on the first-layer
roots, \(z^{(2)}_0\), and the ENTIRE independent initial third matrix.
Then its actual input \(B^{(2)}_n\) is determined without observing
the conditional residual of the second matrix. Formula (3.2) therefore
applies again. Its pairings converge by the first transpose law and
Section 2(b); multiplication of that Gaussian-plus-bounded field by a
bounded gate preserves its joint \(\mathcal W_2\) limit by truncation.
The resulting joint layer-1 law is
\[
 (W^{(2)}_0)^*B^{(2)}=c_2H^{(1)}_0+\sigma_2G_1,
 \quad
 c_2=\frac{c_3}{100m_1}\mathbb E\frac{Z^{(2)}_0\arctan Z^{(2)}_0}
                                     {1+(Z^{(2)}_0)^2}>0,        \tag{12.5}
\]
with \(G_1\) independent of \(Z^{(1)}_0\). In both steps the
vanishing finite-rank projection and conditional Gaussian averaging
prove joint empirical-average convergence, not iid coordinates after
reuse. The unbounded gated transpose input is covered by truncation
and the already obtained \(\mathcal W_2\) law; it does not require
a globally Lipschitz product on all of \(\mathbb R^2\).

Define
\[
 \gamma_1=\mathbb E[(B^{(1)})^2]>0,\quad
 \gamma_2=m_1\mathbb E[(B^{(2)})^2]>0,\quad
 \gamma_3=m_2\mathbb E[(B^{(3)})^2]>0,\quad
 \Gamma=\gamma_1+\gamma_2+\gamma_3.
\]
The first strict inequality follows, for example, from
\(\mathbb E[(\phi'(Z^{(1)}_0))^2
(c_2^2\phi(Z^{(1)}_0)^2+\sigma_2^2)]>0\).
Adjunction in (12.2) gives
\[
 \mathbb E[B^{(2)}V^{(2)}]=\gamma_2+\gamma_1>0,
 \quad \mathbb E[B^{(3)}V^{(3)}]=\Gamma>0.               \tag{12.6}
\]
Thus every \(V^{(\ell)}\ne0\). Strict positivity of \(\phi'\)
implies \(\phi'(Z^{(\ell)}_0)V^{(\ell)}\ne0\) in \(L^2\) too.

### 12.2 Initial motion and kernel change

The readout integral and strong continuity give
\(W^{(4)}(s)/s\to H^{(3)}_0\). Apply (2.4), then bounded operator
continuity in reverse order, to obtain
\(\delta^{(\ell)}(s)/s\to B^{(\ell)}\) in \(L^2\).
Equations (11.1) and (12.2) consequently give
\[
 (Z^{(\ell)})'(s)=sV^{(\ell)}+o(s),\quad
 Z^{(\ell)}(s)-Z^{(\ell)}_0=\tfrac12s^2V^{(\ell)}+o(s^2),
\]
\[
 (H^{(\ell)})'(s)=s\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(s),\quad
 H^{(\ell)}(s)-H^{(\ell)}_0
        =\tfrac12s^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(s^2).
                                                               \tag{12.7}
\]
Integration of a remainder \(o(s)\) in \(L^2\) is \(o(s^2)\),
by bounding its norm by \(\epsilon s\) on a small initial interval.
This justifies the integrated expansions. Matrix increments likewise
satisfy in HS norm
\[
 W^{(\ell)}(s)-W^{(\ell)}_0
 =\tfrac12s^2 B^{(\ell)}\otimes H^{(\ell-1)}_0+o(s^2),
 \quad\ell=2,3,
\]
whose leading squared sizes are \(s^4\gamma_\ell/4>0\).

The kernel expansions now follow from \(L^2\) convergence and (12.6):
\[
 K^{(\ell)}(s)=\gamma_\ell s^2+o(s^2)\quad(\ell=1,2,3),
 \quad K^{(4)}(s)=m_3+\Gamma s^2+o(s^2),
\]
\[
 (K^{(4)})'(s)=2\Gamma s+o(s)>0
                \quad\hbox{for sufficiently small }s>0.
\]
The output coefficient is
\(\mathbb E[H^{(3)}_0\phi'(Z^{(3)}_0)V^{(3)}]=\Gamma\),
not a coefficient inferred by ignoring lower-layer motion.
Since \(s(t)=2t+o(t)\), in physical time
\[
 H^{(\ell)}(t)-H^{(\ell)}_0
     =2t^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t^2),
\]
\[
 K^{(4)}(t)=m_3+4\Gamma t^2+o(t^2),\quad
 \sum_{\ell=1}^4K^{(\ell)}(t)=m_3+8\Gamma t^2+o(t^2).  \tag{12.8}
\]
The velocity part of (12.7) gives
\(\dot H^{(\ell)}(t)=4t\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t)\)
and \(\dot Z^{(\ell)}(t)=4tV^{(\ell)}+o(t)\) in \(L^2\).
Squaring and integrating gives, for each \(\ell=1,2,3\), as
\(T\downarrow0\),
\[
 \int_0^T\mathbb E[(\dot H^{(\ell)}(t))^2]\,dt
 =\frac{16}{3}
   \mathbb E[(\phi'(Z^{(\ell)}_0)V^{(\ell)})^2]T^3+o(T^3),
\]
\[
 \int_0^T\mathbb E[(\dot Z^{(\ell)}(t))^2]\,dt
 =\frac{16}{3}\mathbb E[(V^{(\ell)})^2]T^3+o(T^3).
\]
These are fixed strictly positive leading population coefficients.
In view of the already proved
joint convergence, at a sufficiently small FIXED positive time each
finite hidden feature's squared change divided by \(n\) tends to
a strictly positive value, and the output kernel change does too.
Width is taken to infinity first; no coefficient in (12.8) vanishes
with width. This is genuine feature learning and a nonconstant kernel.

### 12.3 Hidden laws do not become affine at later times

We prove uniform lower tails using the actual finite scalar programs,
then pass them to the flow. Let \(\overline\Phi(x)=\mathbb P(G\ge x)\)
for a standard Gaussian. By (4.4), each forward source has variance
between \(m^2\) and \(a^2\). Section 6 gives
\(|a^{(\ell)}_{kj}|\le A\Delta\) with \(A=3/2\), and both
backwards row sums at most one. Use \(S=3/2\), \(Q=161/120\).
At the top,
\[
 |Z^{(3)}_k-\xi^{(3)}_k|\le AaS^2/10=63/160.
\]
For either sign and \(u>0\), regardless of dependence of the correction,
\[
 \mathbb P(\pm Z^{(3)}_k\ge u)
          \ge\overline\Phi((u+63/160)/m)>0.            \tag{12.9}
\]
For the middle law, the correction is dominated by
\[
 |Z^{(2)}_k-\xi^{(2)}_k|
 \le R_{2,k}:=\frac{A\Delta}{10}\sum_{j<k}(|\zeta^{(2)}_j|+a),
 \qquad \mathbb E R_{2,k}\le ASQ/10=483/1600.
\]
This DOMINATING variable depends only on the backwards source group,
so it is independent of the forward source \(\xi^{(2)}_k\).
The actual correction need not be independent. Markov's inequality
gives \(\mathbb P(R_{2,k}\le1)\ge1117/1600\). Intersect with the
independent Gaussian event to obtain
\[
 \mathbb P(\pm Z^{(2)}_k\ge u)
    \ge\frac{1117}{1600}\overline\Phi((u+1)/m)>0.       \tag{12.10}
\]
For the bottom, \(\operatorname{Var}(\zeta^{(1)}_j)
=\mathbb E[(\delta^{(2)}_j)^2]\le(Q/10)^2\), so
\[
 |X^{(1)}_k-F(Z^{(1)}_0)|
 \le R_{1,k}:=\Delta\sum_{j<k}|\zeta^{(1)}_j|+aS,
 \qquad \mathbb E R_{1,k}\le S(Q/10+a)=1561/800<2.
\]
This dominator is independent of \(Z^{(1)}_0\), and
\(\mathbb P(R_{1,k}\le4)\ge1/2\). The function \(F\), unlike
the activation, is odd; it is also increasing. The corresponding
independent root event gives
\[
 \mathbb P(\pm Z^{(1)}_k\ge u)
      \ge\tfrac12\overline\Phi(F^{-1}(F(u)+4))>0.       \tag{12.11}
\]
No time-independence or Gaussian path-supremum estimate is used.

All these bounds are uniform in mesh, clipping and time index. They
pass to every fixed-clip flow time and then to the uncut flow. Indeed
the half-lines in (12.9)--(12.11) are closed. Under weak convergence
the limiting probability of a closed set is at least the limsup of
the approximating probabilities. This assertion follows, for example,
by decreasing continuous distance cutoffs to its indicator and using
bounded convergence. Thus both tails remain positive arbitrarily far
out at every reached time, including initialization.

For each such square-integrable \(Z\), \(\operatorname{Var}(Z)>0\).
Minimizing the quadratic first over the intercept and then the slope gives
\[
 \inf_{\alpha,\beta\in\mathbb R}
  \mathbb E[(\phi(Z)-\alpha Z-\beta)^2]
 =\operatorname{Var}(\phi(Z))-
       \frac{\operatorname{Cov}(Z,\phi(Z))^2}{\operatorname{Var}(Z)}>0.
                                                               \tag{12.12}
\]
The minimum is attained since the denominator is positive. If it were
zero, boundedness of \(\phi\) and unbounded support of \(Z\) would
force zero slope. Strict monotonicity of \(\phi\) would then force
\(Z\) to be constant, contradicting the tails. Every moment displayed
in (12.12) is continuous along the \(L^2\) path, by bounded Lipschitz
\(\phi\) and Cauchy--Schwarz. The positive variance and positive
minimum therefore have positive lower bounds on every compact physical
interval, simultaneously over the three layers. Uniform joint
second-moment convergence transfers a smaller positive lower bound
to finite empirical affine-approximation errors with probability
tending to one. The fixed activation itself is nonaffine at every
finite width, and its nonlinearity does not disappear under the limiting law.

### 12.4 No later freezing of hidden features

Fix any feature time \(s>0\) reached at a finite physical time.
By (5.6), \(W^{(4)}(s)\ge ms\) almost surely, and \(\phi'>0\)
at every finite preactivation. Therefore
\(\mathbb E[(\delta^{(3)}(s))^2]>0\).
Choose fixed-clip scalar Euler approximations at indices approaching
this time, first refining the mesh and then removing the clip. Their
backward-field laws converge by Sections 7--8 and 11; in particular
the variances
\(\operatorname{Var}(\zeta^{(2)}_k)=\mathbb E[(\delta^{(3)}_k)^2]\)
eventually have a positive lower bound. Since
\(|q^{(2)}_k-\zeta^{(2)}_k|\le a\), the Gaussian lower tails and
the same closed-half-line passage prove unbounded support of
\(q^{(2)}(s)\). Thus \(\delta^{(2)}(s)\ne0\) in \(L^2\).
Repeat using
\(\operatorname{Var}(\zeta^{(1)}_k)=\mathbb E[(\delta^{(2)}_k)^2]\)
and \(|q^{(1)}_k-\zeta^{(1)}_k|\le a\). It proves
\(\delta^{(1)}(s)\ne0\). These implications are sequential from
top to bottom, not a circular assumption on lower backwards fields.

All three hidden kernels in (9.5) are consequently positive at this
time. Using (11.1), adjunction and the definition of the deltas,
\[
 \mathbb E[\delta^{(2)}(Z^{(2)})']=K^{(2)}+K^{(1)}>0,
 \quad
 \mathbb E[\delta^{(3)}(Z^{(3)})']
                       =K^{(3)}+K^{(2)}+K^{(1)}>0.      \tag{12.13}
\]
Together with \((Z^{(1)})'=\delta^{(1)}\), these exclude zero
\(L^2\) preactivation velocities in every layer. A strictly positive
gate cannot annihilate a nonzero square-integrable variable, so every
hidden feature velocity is nonzero too. Finally the physical multiplier
\(2(1-f)\) is strictly positive at every finite physical time by
(9.6). The same nonzero-velocity statements therefore hold in physical
time for every \(t>0\). Initial hidden velocities vanish exactly because
the population readout starts at zero; their nonzero second-order onset
was proved in (12.7)--(12.8).

All assertions of the theorem are now proved for the one fixed activation.
Auxiliary clips, query perturbations, finite oracle contractions, and
Euler meshes have all been removed in their specified order. The final
state and equations contain none of them. The result has the complete
finite-physical-horizon, joint empirical/action-law, autonomous-restart,
and nonlinear feature-learning scope stated in Section 1.
