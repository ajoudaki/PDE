# Global nonlinear learning at every fixed hidden depth

This chapter proves a global population limit for one training sample and
every separately fixed number of hidden layers \(L\ge3\), with the activation
\[
\phi(z)=1+\frac{\arctan z}{10}
\]
in every hidden layer. The same activation is used independently of depth,
width and physical time. The result includes finite gradient flow, exact
gradient descent, every parameter-gradient kernel block, current operator
actions and adjoints, hidden path laws, and hidden velocities.

We use the [shared notation](NOTATION.md). Finite hidden vectors are
\(z^{(\ell)},h^{(\ell)}\); population random variables are
\(Z^{(\ell)},H^{(\ell)}\). Finite and population weights both use
\(W^{(\ell)}\), with their types stated below. Finite transposes are \(T\);
population adjoints are \(*\). Every finite vector norm is the ordinary
Euclidean norm, with any factor \(1/\sqrt n\) or \(1/n\) displayed explicitly.

The argument constructs its Gaussian actions and proves the required
finite-program limits, response estimates and continuum comparisons here.
Its general background is elementary probability and Gaussian integration,
basic measure theory, and Hilbert and Banach space analysis. Auxiliary clips,
query perturbations and oracle programs are removed before stating the
limiting dynamics. The theorem concerns each fixed depth and each finite
physical horizon; it does not take a simultaneous depth and width limit.

## 1. Exact model and theorem

There is one sample, with \(m=d=1\) and \(x_1=y_1=1\); its sample
index is suppressed. Every hidden layer has width \(n\). The first weight
\(W^{(1)}\in\mathbb R^{n\times1}\) is identified with its column vector,
so \(z^{(1)}=W^{(1)}\). The stored readout
\(W^{(L+1)}\in\mathbb R^n\) is a vector, and each
\(W^{(\ell)}\in\mathbb R^{n\times n}\), \(2\le\ell\le L\), is a
hidden matrix. All fixed mobility multipliers are
\(\kappa_\ell=1\): the Euclidean block mobilities are
\(n,1,\ldots,1,n\). Define
\[
 \phi(z)=1+\arctan(z)/10,\qquad h^{(\ell)}=\phi(z^{(\ell)}),\qquad
 z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\quad(2\le\ell\le L),
\]
\[
 f_n=(W^{(L+1)})^Th^{(L)}/n,\quad r_n=f_n-1,\quad \mathcal L_n=r_n^2.
\]
Products and nonlinearities are coordinatewise. Define backwards,
without including the residual,
\[
 \delta^{(L)}=W^{(L+1)}\phi'(z^{(L)}),\quad
 q^{(\ell)}=(W^{(\ell+1)})^T\delta^{(\ell+1)},\quad
 \delta^{(\ell)}=\phi'(z^{(\ell)})q^{(\ell)}
       \quad(\ell=L-1,\ldots,1).                       \tag{1.1}
\]
All entries and parameter blocks at initialization are independent:
\[
 z^{(1)}_{0,i}\sim N(0,1),\quad
 W^{(\ell)}_{0,ij}\sim N(0,1/n)\ (2\le\ell\le L),\quad
 W^{(L+1)}_{0,i}\sim N(0,n^{-2}).                       \tag{1.2}
\]
Exact raw GD, with \(\eta_n=n^{-2}\), is
\[
 z^{(1)}_{k+1}=z^{(1)}_k-2\eta_n r_{n,k}\delta^{(1)}_k,\quad
 W^{(\ell)}_{k+1}=W^{(\ell)}_k-
       \frac{2\eta_n r_{n,k}}n
                   \delta^{(\ell)}_k(h^{(\ell-1)}_k)^T
                \quad(2\le\ell\le L),
\]
\[
 W^{(L+1)}_{k+1}=W^{(L+1)}_k-2\eta_n r_{n,k}h^{(L)}_k. \tag{1.3}
\]
Physical time is \(t=k\eta_n\). Raw parameters are linearly interpolated,
and hidden preactivations/features are recomputed. At interior mesh
nodes velocities mean right derivatives, and at a terminal mesh node
they mean left derivatives. Finite GF has the corresponding continuous
raw equations.

**Theorem (global joint limit).** For every fixed integer \(L\ge3\), there are \(L\) fixed neuron
probability spaces \((\Omega_\ell,\mathcal F_\ell,\mathbb P_\ell)\).
Write \(E_\ell\) for expectation and
\(\mathcal H_\ell=L^2(\Omega_\ell,\mathbb P_\ell)\).
There are bounded initial Gaussian matrix actions
\(W^{(\ell)}_0:\mathcal H_{\ell-1}\to\mathcal H_\ell\),
\(2\le\ell\le L\), with their actual Hilbert-space adjoints. On these spaces, the
\(L+1\) present objects
\[
 X^{(1)},\quad W^{(2)},\ldots,W^{(L)},\quad W^{(L+1)},
 \qquad Z^{(1)}=F^{-1}(X^{(1)}),\quad F(z)=10(z+z^3/3) \tag{1.4}
\]
define an autonomous population gradient flow, where
\(X^{(1)}\in\mathcal H_1\), \(W^{(L+1)}\in\mathcal H_L\), and
\(W^{(\ell)}:\mathcal H_{\ell-1}\to\mathcal H_\ell\) is bounded.
Each \(Z^{(\ell)},H^{(\ell)},\delta^{(\ell)}\) belongs to
\(\mathcal H_\ell\); each incoming query \(q^{(\ell)}\) belongs to
\(\mathcal H_\ell\), for \(1\le\ell<L\). The backward symbol
\(\delta^{(\ell)}\) is used in both settings with these explicit types.
Initial \(Z^{(1)}\) is standard Gaussian and the initial population readout is zero.
Forward and backward equations are (1.1) with capital \(Z,H\) and
population adjoints \(^{*}\) replacing finite transposes \(^{T}\).
Expectations always refer to the population containing the scalar
integrand. For \(U\in\mathcal H_\ell\), \(V,g\in\mathcal H_{\ell-1}\),
the rank-one action is
\((U\otimes V)g=U E_{\ell-1}[Vg]\).
In generic probability identities below, \(\mathbb E\) denotes expectation
on the stated probability space; for a typed layer integrand it means
\(E_\ell\) on that layer. We abbreviate
\(\|U\|_{L^p(\Omega_\ell)}\) by \(\|U\|_{L^p}\) when the type of
\(U\) fixes the layer. These are population norms, never normalized finite
norms. The equations are
\[
 f=E_L[W^{(L+1)}H^{(L)}],\quad r=f-1,\quad \mathcal L=r^2,\quad
 \dot X^{(1)}=-2r q^{(1)},\quad
 \dot W^{(\ell)}=-2r\delta^{(\ell)}\otimes H^{(\ell-1)}
                  \ (2\le\ell\le L),\quad
 \dot W^{(L+1)}=-2rH^{(L)}.                            \tag{1.5}
\]
For every finite \(T\) there is a solution, unique among continuous
integral solutions on the same spaces with bounded vector \(L^2\) norms
and matrix operator norms on compact intervals. Uniqueness includes
the raw first-coordinate equations. From every reached state the
solution is uniquely restartable for every finite remaining physical
interval. Matrices have Hilbert--Schmidt trained increments, and the
raw equations are the gradient flow of \((f-1)^2\) for the Hilbert
metric specified in Section 9. The number of fields/operators is finite;
their state spaces need not be finite-dimensional.

For every fixed \(T\), the full width sequence of exact GD and its
corresponding finite GF converges jointly in probability to this flow,
uniformly on \([0,T]\), as follows. For any fixed finite same-layer
list of current fields and probe outputs, the joint empirical law
converges in \(\mathcal W_2\) to its population law. Probes may use real
linear combinations, globally Lipschitz coordinate maps, products of
bounded factors, and either direction of any current matrix.
The class additionally contains every backward field (1.1) and every
hidden preactivation/feature velocity. Finitely many time arguments
may be included jointly, with convergence uniform over those arguments.
There is no artificial coordinate pairing between different populations.
Equivalently, all continuous tests of at most quadratic growth on each
such finite list converge in empirical average. Here \(\mathcal W_2\)
is the infimum square root of expected squared distance over couplings.

In particular prediction, residual, loss, and all \(L+1\) raw kernel
blocks converge uniformly:
\[
 K_n^{(1)}=\|\delta^{(1)}\|_2^2/n,\quad
 K_n^{(\ell)}=\|\delta^{(\ell)}\|_2^2\|h^{(\ell-1)}\|_2^2/n^2
                       \ (2\le\ell\le L),\quad
 K_n^{(L+1)}=\|h^{(L)}\|_2^2/n.                        \tag{1.6}
\]
Every hidden preactivation and feature whole-path empirical law
converges in \(\mathcal W_2(C([0,T]))\) for the supremum norm;
integrated squared velocities converge. If finite GD and GF have the
same initialization, their same-width state distance, uniformly in time,
tends to zero in probability, where
\[
 d_n(\Theta,\widetilde\Theta)=
 \frac{\|F(z^{(1)})-F(\widetilde z^{(1)})\|_2}{\sqrt n}
 +\sum_{\ell=2}^L\|W^{(\ell)}-\widetilde W^{(\ell)}\|_{\rm op}
 +\frac{\|W^{(L+1)}-\widetilde W^{(L+1)}\|_2}{\sqrt n}. \tag{1.7}
\]
Across widths, convergence concerns empirical/action laws, not
operator-norm convergence between different spaces.

The population fits the label, with
\(\mathcal L(t)\le \exp(-25t/9)\).
Every hidden law has strictly positive best affine-approximation error
for \(\phi\), uniformly on each compact physical interval including
initialization. Every hidden feature velocity has nonzero \(L^2\) norm
at every positive finite physical time. All trained blocks move, hidden
motion begins at second order, and the total kernel is nonconstant.
The coefficient \(1/10\) is fixed independently of depth, width, and time.

Proof architecture. Finite Gaussian calculations identify clipped Euler
laws and fixed-space bounded actions. Section 6 proves a response bound
by a time induction whose forward pass goes up the layers and backward
pass goes down. The same numerical bounds hold at every interior layer.
A comparison linear in the clipping level then removes all clips.
The positive activation floor keeps every finite physical horizon inside
one feature-time interval. Raw GD and all nontriviality obligations are
treated separately.

## 2. Elementary bounds and limiting tools

Let \(c_-=5/6\) and \(a=7/6\) be fixed lower and upper activation
bounds; \(m=1\) continues to denote the sample count. The letter \(a\)
in these bounds is a scalar constant, distinct from a suppressed sample
index. Since \(\pi<10/3\),
\[
 c_-<\phi<a,\quad 0<\phi'(z)=\frac1{10(1+z^2)}\le1/10,
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
We use this simultaneously for the finitely many initial matrices. Also
\(\mathbb E\|W^{(L+1)}_0\|_2^2/n=n^{-2}\), so its vector norm
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

(d) If \(b,c_i\ge0\) and
\(u_j\le b+\sum_{i<j}c_i\max_{v\le i}u_v\), then
\[
 \max_{v\le j}u_v\le b\prod_{i<j}(1+c_i)
                  \le b\exp\left(\sum_{i<j}c_i\right). \tag{2.5}
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
There are finitely many neuron populations, finitely many iid root tuples in
each, independent of the finitely many Gaussian matrices, and coordinate
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
\(\sigma^2=\mathbb E[U^2]\). The innovation variance is the full
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

Adaptation and additional independent matrices cause no change to this argument.
Conditional on the preceding transcript, the next query input is known.
The next answer constrains only the queried matrix by a new linear
observation. Inductively the conditional residual matrices remain
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
matrix has a centered Gaussian source group; the \(2(L-1)\) groups are
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

We derive the rule in the limiting scalar coordinates. Here
\(h,v_i,u_s,y_i,q_s\) are square-integrable scalar coordinate expressions
on the input or output population dictated by the queried orientation;
they are not finite vectors. The coefficients \(\alpha_i\) are
deterministic coefficients of the \(L^2\) projection onto the old forward
inputs. Let old forward inputs be \(v_i\), old reverse
inputs \(u_s\), and \(\Gamma_U=(\mathbb E[u_su_t])_{st}\).
Inductively old forward answers are
\(y_i=\xi_i+\sum_s D_{is}u_s\), with
\(D_{is}=\mathbb E\partial_{\zeta_s}v_i\), and old reverse answers
are \(q_s=\zeta_s+\) a linear combination of old forward inputs.
Unavailable source derivatives are zero. Put
\(h_\perp=h-\sum_i\alpha_i v_i\) for the limiting least-squares
projection. Since \(\mathbb E[v_i h_\perp]=0\),
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
                  -\sum_i\alpha_i\mathbb E\nabla_\zeta v_i.
\]
Substituting the old forward decompositions in (3.4) cancels the second
term and proves (3.5). The new source is
\(\xi_h=\sum_i\alpha_i\xi_i+\sigma G\), where
\(\sigma^2=\mathbb E h_\perp^2\) and the new scalar Gaussian is
independent of all old sources. Direct expansion gives
\(\mathbb E[\xi_h\xi_i]=\mathbb E[hv_i]\) and
\(\mathbb E\xi_h^2=\mathbb E h^2\).
This also proves the asserted independence of distinct source groups.
The proof includes derivatives passing through previous uses of the
other matrices; it does not differentiate the coefficient selection itself.

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

Here \(s\) is feature time and \(\Delta>0\) is an auxiliary Euler
mesh. Query and step indices \(i,j,k,u,v\) below are integers; \(r=f-1\)
is reserved for the residual. Primes on paths
mean \(d/ds\), dots mean physical derivatives, and primes on scalar
functions mean scalar derivatives. The uncut feature field removes
\(2(1-f)\) and transforms only the first coordinate. Section 9 verifies
its raw gradient structure and the physical clock.

For each integer \(R\ge1\) choose a smooth odd map
\[
 \tau_R(q)=q\ (|q|\le R),\quad
 |\tau_R(q)|\le\min(|q|,2R),\quad0\le\tau'_R\le1.       \tag{4.1}
\]
For example integrate a smooth even cutoff, equal to one on \([-R,R]\)
and zero outside \([-2R,2R]\), with values in \([0,1]\).
Clip every interior backwards query, but not the bottom transformed
query or the readout:
\[
 \delta_R^{(L)}=W^{(L+1)}\phi'(Z^{(L)}),\quad
 q_R^{(\ell)}=(W^{(\ell+1)})^*\delta_R^{(\ell+1)},\quad
 \delta_R^{(\ell)}=\phi'(Z^{(\ell)})\tau_R(q_R^{(\ell)})
                    \quad(\ell=L-1,\ldots,2),
 \quad q_R^{(1)}=(W^{(2)})^*\delta_R^{(2)}.
\]
Set \(X^{(1)}_{k+1}=X^{(1)}_k+\Delta q^{(1)}_{R,k}\),
\(W^{(\ell)}_{k+1}=W^{(\ell)}_k+
\Delta\delta^{(\ell)}_{R,k}\otimes H^{(\ell-1)}_k\),
and \(W^{(L+1)}_{k+1}=W^{(L+1)}_k+\Delta H^{(L)}_k\).
The finite version uses \(\delta h^T/n\), the same forward equations,
and the typed transformed vector \(x^{(1)}=F(z^{(1)})\in\mathbb R^n\),
so \(h^{(1)}=\chi(x^{(1)})\).
These are transformed Euler approximations, not exact rewrites of raw
GD. In proof programs the initial readout is zero.

Unroll each matrix into its initial action plus its rank memories.
At time \(k\), its extra forward and reverse terms are, respectively,
\[
 \Delta\sum_{j<k}\delta^{(\ell)}_j
       (h^{(\ell-1)}_j)^Th^{(\ell-1)}_k/n,\qquad
 \Delta\sum_{j<k}h^{(\ell-1)}_j
       (\delta^{(\ell)}_j)^T\delta^{(\ell)}_k/n.        \tag{4.2}
\]
First freeze these finitely many scalar contractions at their limiting
expectations, constructed in causal forward/backward order by Section 3.
For fixed \(M,\Delta,R,L\) this oracle program meets its hypotheses:
\(|W^{(L+1)}_k|\le aM\Delta\), \(|\delta^{(L)}_k|\le aM\Delta/10\),
and every interior \(|\delta_{R,k}^{(\ell)}|\le R/5\).
Extend the top product smoothly outside a larger readout interval to a
globally Lipschitz \(C^1\) map, unchanged with its derivatives on all
attained values. Include the initial root pair \((Z^{(1)}_0,F(Z^{(1)}_0))\).
Clipped products already have bounded derivatives.

Oracle contractions converge by Section 3. Restore actual feedback
using, at every finite instruction,
\[
 |(u^Tv-\widetilde u^T\widetilde v)/n|
 \le \frac{\|u-\widetilde u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
   +\frac{\|\widetilde u\|_2}{\sqrt n}
                       \frac{\|v-\widetilde v\|_2}{\sqrt n}.
\]
On the initial matrix norm event, finite induction through the Lipschitz
instructions bounds actual/oracle node differences by constants times
previous differences and the finitely many oracle contraction errors.
All oracle vector norms divided by \(\sqrt n\), and all oracle matrix
operator norms, are bounded in probability. Thus the vector differences
divided by \(\sqrt n\) vanish. This is a fixed-program result, not a mesh-uniform induction.

The exact resulting scalar law, omitting \(R\) on its backwards fields,
is
\[
 X^{(1)}_k=F(Z^{(1)}_0)+\Delta\sum_{i<k}q^{(1)}_i,\quad
 H^{(1)}_k=\chi(X^{(1)}_k),
\]
\[
 Z^{(\ell)}_k=\xi^{(\ell)}_k+
            \sum_{i<k}a^{(\ell)}_{ki}\delta^{(\ell)}_i,\quad
 H^{(\ell)}_k=\phi(Z^{(\ell)}_k)\quad(2\le\ell\le L),
\]
\[
 W^{(L+1)}_k=\Delta\sum_{i<k}H^{(L)}_i,\quad
 \delta^{(L)}_k=W^{(L+1)}_k\phi'(Z^{(L)}_k),
\]
\[
 q^{(\ell)}_k=\zeta^{(\ell)}_k+
       \sum_{v\le k}b^{(\ell+1)}_{kv}H^{(\ell)}_v
                                  \quad(1\le\ell<L),
 \quad
 \delta^{(\ell)}_k=\phi'(Z^{(\ell)}_k)\tau_R(q^{(\ell)}_k)
                                  \quad(2\le\ell<L).  \tag{4.3}
\]
The \(2(L-1)\) centered Gaussian source groups are mutually independent
and independent of the root, with full uncentered input second moments
\[
 \mathbb E[\xi^{(\ell)}_k\xi^{(\ell)}_i]
       =\mathbb E[H^{(\ell-1)}_kH^{(\ell-1)}_i],\quad
 \mathbb E[\zeta^{(\ell-1)}_k\zeta^{(\ell-1)}_i]
       =\mathbb E[\delta^{(\ell)}_k\delta^{(\ell)}_i].
                                                               \tag{4.4}
\]
Temporal covariances may be singular. The deterministic coefficients are
\[
 a^{(\ell)}_{ki}=
 \mathbb E\frac{\partial H^{(\ell-1)}_k}
                  {\partial\zeta^{(\ell-1)}_i}
       +\Delta\mathbb E[H^{(\ell-1)}_kH^{(\ell-1)}_i]\quad(i<k),
\]
\[
 b^{(\ell)}_{ki}=
 \mathbb E\frac{\partial\delta^{(\ell)}_k}{\partial\xi^{(\ell)}_i}
       +\Delta\mathbf1_{i<k}
                   \mathbb E[\delta^{(\ell)}_k\delta^{(\ell)}_i]
                                                     \quad(i\le k).
                                                               \tag{4.5}
\]
Formal differentiation holds the already selected deterministic
coefficients and covariances fixed, and differentiates the complete
explicit expression. Distinct source slots stay formally distinct even
when their covariance is singular. Sections 3.3--3.4 justify this rule.

At each time the order is forward \(2,\ldots,L\), then reverse
\(L,\ldots,2\). All forward memories are strictly past-time; reverse
memories include the current time. In particular,
\[
 b^{(L)}_{kk}=\mathbb E[W^{(L+1)}_k\phi''(Z^{(L)}_k)],
\]
\[
 b^{(\ell)}_{kk}
 =\mathbb E[\phi''(Z^{(\ell)}_k)\tau_R(q^{(\ell)}_k)]
 +b^{(\ell+1)}_{kk}
     \mathbb E[(\phi'(Z^{(\ell)}_k))^2\tau'_R(q^{(\ell)}_k)]
                      \quad(2\le\ell<L).             \tag{4.6}
\]
Thus the current return through every upper layer is retained,
recursively. There is no missing current response in the depth induction.

## 5. Common spaces, bounded actions, and fixed-clip flows

Take a countable family of finite programs closed under finite unions,
rational linear combinations, constants in each population, both
directions of all initial matrices, the coordinate maps used above, and
a countable smooth bounded Lipschitz family dense among continuous
functions on compact sets in each finite-dimensional coordinate space.
Include the root pair \((Z^{(1)}_0,F(Z^{(1)}_0))\), but not arbitrary
later applications of the non-Lipschitz cubic \(F\).
The finite joint laws of Section 3 are consistent because every finite
union is the limit of the same finite-width calculations. The elementary
countable probability-measure extension principle gives a measure on
the countable coordinate product for each layer. Equivalently, sample
successive coordinates from their conditional distributions, whose
finite marginals are consistent. Let \(\Omega_\ell\) carry this measure
and the sigma field generated by its slots.

Generated coordinate functions have dense linear span in
\(L^2(\Omega_\ell)\). To verify this, conditional expectations onto the
first finitely many slots approximate any \(L^2\) function: orthogonal
projection onto increasing subspaces converges to projection onto their
closed union, which contains indicators and then simple functions of
the generated sigma field. Truncate the resulting finite-slot function.
In a finite-dimensional Borel probability measure, bounded continuous
functions approximate bounded measurable functions in \(L^2\):
approximate measurable sets between compact subsets and open supersets,
then use continuous distance cutoffs. The included Lipschitz family
approximates those continuous functions on compact sets; tails are
removed by truncation.

For rational combinations of generated inputs, pass the high-probability
finite bound (2.2) and the exact transpose pairing to their limiting
second moments. They give
\[
 \|W^{(\ell)}_0U\|_{L^2}\le10\|U\|_{L^2},\quad
 \mathbb E[VW^{(\ell)}_0U]
       =\mathbb E[U(W^{(\ell)}_0)^*V]\quad(2\le\ell\le L).
                                                               \tag{5.1}
\]
Zero \(L^2\) input difference has zero output difference; hence each
action is well-defined on equivalence classes. Extend by density.
Construct reverse actions identically; the displayed pairing proves
they are the adjoints. Real coefficients and other fixed Lipschitz
maps follow by compact approximation and propagation with the bounded
actions. All real-step Euler programs therefore live on these same
spaces. No independent transpose resampling or growing number of
state operators is used. The entire trained rank memory remains in
the current operator.

For \(\Theta=(X^{(1)},W^{(2)},\ldots,W^{(L)},W^{(L+1)})\), use
\[
 d(\Theta,\widetilde\Theta)=
 \|X^{(1)}-\widetilde X^{(1)}\|_{L^2}+
 \sum_{\ell=2}^L\|W^{(\ell)}-\widetilde W^{(\ell)}\|_{\rm op}
 +\|W^{(L+1)}-\widetilde W^{(L+1)}\|_{L^2}.                \tag{5.2}
\]
The corresponding vector-field norm is the sum of its block norms.
At finite width, vector norms are divided by \(\sqrt n\), giving (1.7).
The clipped feature field is
\[
 \mathcal V_R(\Theta)=
 (q_R^{(1)},(\delta_R^{(\ell)}\otimes H^{(\ell-1)})_{\ell=2}^L,
 H^{(L)}).                                           \tag{5.3}
\]

Here are explicit coarse primal bounds, independent of cap and width,
for any feature flow or positive-step Euler prefix of total length
at most \(S\). The population initial bounds are
\(\|W^{(L+1)}_0\|_{L^2}\le1\) and
\(\|W^{(\ell)}_0\|_{\rm op}\le M_0\).
At finite width the readout assumption is explicitly
\(\|W^{(L+1)}_0\|_2/\sqrt n\le1\), with the same matrix bound. Set
\[
 Q_0=1+aS,\quad D_L=Q_0/10,\quad R_L=M_0+aSD_L,
\]
and, going down from \(\ell=L-1\) to 2, set
\[
 D_\ell=R_{\ell+1}D_{\ell+1}/10,\qquad
 R_\ell=M_0+aSD_\ell.                                \tag{5.4}
\]
These bound the population readout \(L^2\) norm, backwards-field
\(L^2\) norms, and matrix operator norms by \(Q_0,D_\ell,R_\ell\),
respectively. Their finite counterparts are
\(\|W^{(L+1)}\|_2/\sqrt n\le Q_0\),
\(\|\delta_R^{(\ell)}\|_2/\sqrt n\le D_\ell\), and
\(\|W^{(\ell)}\|_{\rm op}\le R_\ell\).
To prove the bounds, integrate or sum the bounded readout velocity, then use
\(\|\delta_R^{(\ell)}\|_{L^2}\le\|q_R^{(\ell)}\|_{L^2}/10\)
and the rank-one norm identity \(\|U\otimes V\|=\|U\|_{L^2}\|V\|_{L^2}\)
successively down the layers. Finally
\(\|q_R^{(1)}\|_{L^2}\le R_2D_2\) bounds the first-coordinate velocity.
All state velocities are bounded by a finite \(C_{L,S}\).
These constants may grow with \(L\), which is fixed.
From zero readout there is the stronger pointwise bound
\[
 c_-s\le W^{(L+1)}(s)\le as.                            \tag{5.5}
\]

We spell out cap dependence in stability. Forward induction gives
\[
 \|Z_A^{(2)}-Z_B^{(2)}\|_{L^2}
 \le a\|W_A^{(2)}-W_B^{(2)}\|_{\rm op}
       +(R_2/100)\|X_A^{(1)}-X_B^{(1)}\|_{L^2},
\]
\[
 \|Z_A^{(\ell)}-Z_B^{(\ell)}\|_{L^2}
 \le a\|W_A^{(\ell)}-W_B^{(\ell)}\|_{\rm op}
       +(R_\ell/10)\|Z_A^{(\ell-1)}-Z_B^{(\ell-1)}\|_{L^2}.
                                                               \tag{5.6}
\]
Thus all forward differences are at most \(C_{L,S}d(A,B)\),
independent of the cap. If the reference readout \(W_B^{(L+1)}\)
has pointwise bound \(B_0\), the top backwards difference is at most
\[
 \|\delta_A^{(L)}-\delta_B^{(L)}\|_{L^2}
 \le \tfrac1{10}\|W_A^{(L+1)}-W_B^{(L+1)}\|_{L^2}
                  +\tfrac{B_0}{5}\|Z_A^{(L)}-Z_B^{(L)}\|_{L^2}.
                                                               \tag{5.7}
\]
No pointwise bound on the competitor readout is needed.
For any lower query,
\[
 \|q_A^{(\ell)}-q_B^{(\ell)}\|_{L^2}
 \le R_{\ell+1}\|\delta_A^{(\ell+1)}-\delta_B^{(\ell+1)}\|_{L^2}
             +D_{\ell+1}\|W_A^{(\ell+1)}-W_B^{(\ell+1)}\|_{\rm op}.
\]
At a common cap,
\[
 \|\delta_R^{(\ell)}(A)-\delta_R^{(\ell)}(B)\|_{L^2}
 \le\tfrac1{10}\|q_A^{(\ell)}-q_B^{(\ell)}\|_{L^2}
             +\tfrac{2R}{5}\|Z_A^{(\ell)}-Z_B^{(\ell)}\|_{L^2}.
                                                               \tag{5.8}
\]
The coefficient of the preceding backwards error is independent of
\(R\); the \(R\) term multiplies a forward difference already controlled
by (5.6). Downward induction therefore gives a bound
\(C_{L,S}(1+R)d(A,B)\), not \(R^{L-2}d(A,B)\), for every backwards
field and query. Rank-one differences satisfy
\[
 \|U\otimes V-\widetilde U\otimes\widetilde V\|
 \le\|U-\widetilde U\|_{L^2}\|V\|_{L^2}+
                          \|\widetilde U\|_{L^2}\|V-\widetilde V\|_{L^2}.
\]
Consequently \(\mathcal V_R\) has the same Lipschitz bound on these
bounded-primal, bounded-reference-readout sets. Every inequality also
holds at finite width with the specified norm factors.

For fixed \(R\), iterate the integral equations in continuous paths on
a short interval, with slightly enlarged primal bounds and pointwise
readout bounds (5.5). This set is closed: an \(L^2\)-convergent sequence
has an almost-everywhere convergent subsequence preserving a common
pointwise bound. The readout integral preserves its bounds; the velocity
bound preserves the remaining bounds on a short enough interval, and
the Lipschitz estimate makes the integral map a contraction. Its
iterates converge geometrically to a unique fixed point. Bounds (5.4)
allow finitely many restarts on every fixed interval, hence global
fixed-clip feature flows. Finite-dimensional uncut flows also exist
globally in feature time, since the field is smooth and (5.4) prevents
finite-time escape.

Along a fixed-clip flow, integrate its Lipschitz velocity over one
Euler step. The local defect is at most \(C_{R,L,S}\Delta^2\).
Discrete Gronwall (2.5) gives, in both finite and population state norms,
\[
 \sup_{s\le S}d(\Theta_{R,\Delta}(s),\Theta_R(s))
                       \le C_{R,L,S}\Delta.           \tag{5.9}
\]
The finite bound holds on the initial norm event. Fixing a mesh, taking
width to infinity by Section 4, and then refining the mesh proves the
fixed-clip width limit. Finite probe instructions preserve the
comparison by bounded operator and Lipschitz bounds. A finite time net,
using uniform time continuity at fixed cap, proves convergence uniform
in finitely many joint time arguments.

## 6. The depth-independent response estimate

For the exact scalar programs (4.3)--(4.5), put
\[
 B_{\ell,k}=\sum_{i\le k}|b^{(\ell)}_{ki}|\quad(2\le\ell\le L),
 \qquad S=M\Delta\le3/2,\quad A=3/2,\quad Q=161/120.
\]
We prove simultaneously at every time index, for every finite depth,
mesh and cap,
\[
 |a^{(\ell)}_{ki}|\le A\Delta\ (i<k),\quad
 B_{L,k}\le3067/3200<1,\quad
 B_{\ell,k}<9/10\ (2\le\ell<L),\quad
 \|\delta^{(\ell)}_k\|_{L^2}\le7/40\ (2\le\ell\le L).
                                                               \tag{6.1}
\]
The interior norm actually satisfies \(Q/10=161/1200<7/40\).
Bounds are on the actual identified response, not an arbitrary
Gaussian action on all bounded inputs.

At zero, the readout and top delta vanish identically as formal
expressions, so its reverse variance and response row vanish. Downward
induction gives the same for all deltas and rows, using \(\tau_R(0)=0\).
This does not discard derivatives in a degenerate Gaussian source
direction merely because that source happens to be zero.

Suppose all rows and delta norms strictly before \(k\) satisfy the
bounds \(B_{\ell,i}\le1\), \(\|\delta^{(\ell)}_i\|_{L^2}\le7/40\).
The following forward pass constructs all current forward coefficients
using only those past bounds.

For a single bottom source \(\zeta^{(1)}_i\), differentiating the
complete bottom expression gives
\[
 |\partial_{\zeta^{(1)}_i}X^{(1)}_j|
 \le\Delta\mathbf1_{i<j}
 +\frac{\Delta}{100}\sum_{u<j}\sum_{v\le u}|b^{(2)}_{uv}|
                    |\partial_{\zeta^{(1)}_i}X^{(1)}_v|.
\]
By (2.5), for \(i<j\le k\),
\[
 |\partial_{\zeta^{(1)}_i}H^{(1)}_j|
       \le(\Delta/100)e^{S/100},\quad
 |a^{(2)}_{ji}|
       \le\Delta[a^2+e^{S/100}/100]<A\Delta.            \tag{6.2}
\]
Indeed \(e^{3/200}<2\) and \(49/36+1/50<3/2\).

Consider an interior layer \(2\le\ell<L\), assuming the forward pass
has established \(|a^{(\ell)}_{ji}|\le A\Delta\) for \(j\le k\).
Define its forward derivative row and its nondecreasing envelope by
\[
 \mathcal R_{\ell,j}
 =\sum_{i\le j}|\partial_{\xi^{(\ell)}_i}Z^{(\ell)}_j|,
 \quad
 E_{\ell,j}=\exp\left\{A\Delta\sum_{u<j}
            (|q^{(\ell)}_u|/5+B_{\ell+1,u}/100)\right\}.
\]
For either kind of source derivative,
\[
 |\partial\delta^{(\ell)}_u|
 \le |q^{(\ell)}_u||\partial Z^{(\ell)}_u|/5
                                  +|\partial q^{(\ell)}_u|/10.
\]
For a forward-source derivative,
\[
 |\partial q^{(\ell)}_u|
 \le\frac1{10}\sum_{v\le u}|b^{(\ell+1)}_{uv}|
                                      |\partial Z^{(\ell)}_v|.
\]
Summing over the source row and applying (2.5) proves
\[
 \mathcal R_{\ell,j}
 \le1+A\Delta\sum_{u<j}
 (|q^{(\ell)}_u|/5+B_{\ell+1,u}/100)
                         \max_{v\le u}\mathcal R_{\ell,v},
 \qquad \max_{v\le j}\mathcal R_{\ell,v}\le E_{\ell,j}. \tag{6.3}
\]
The direct derivative of \(\xi^{(\ell)}_j\) contributes one in the row.
For a single reverse source \(\zeta^{(\ell)}_i\), the extra derivative
of \(q^{(\ell)}_u\) is \(\mathbf1_{u=i}\).
Its first forward contribution has size at most \(A\Delta/10\).
The same comparison yields
\[
 |\partial_{\zeta^{(\ell)}_i}H^{(\ell)}_j|
       \le(A\Delta/100)E_{\ell,j}\quad(i<j\le k).       \tag{6.4}
\]
There is no current \(\zeta^{(\ell)}_j\) dependence in \(Z^{(\ell)}_j\).

For \(u<j\le k\), the induction hypotheses imply
\[
 |q^{(\ell)}_u|\le|\zeta^{(\ell)}_u|+a,\qquad
 \operatorname{Var}(\zeta^{(\ell)}_u)
       =\|\delta^{(\ell+1)}_u\|_{L^2}^2\le(7/40)^2.
\]
For any centered Gaussian \(G_v\) of variance \(v\),
\(\mathbb E e^{\lambda|G_v|}\le2e^{\lambda^2v/2}\).
Jensen over the \(j\) time slots, with no temporal independence
assumption, gives for \(p\ge1\)
\[
 \mathbb E E_{\ell,j}^p
 \le2\exp\{pAS(a/5+1/100)
                 +\tfrac12(pAS/5)^2(7/40)^2\}
 \le2\exp\{219p/400+3969p^2/1280000\}.                 \tag{6.5}
\]
At \(j=0\) the envelope is one. For \(p=1,2\), the exponent after
taking the \(p\)-th root is less than \(3/5\).
Since \(e<3\) and \(3^3<2^5\), \(e^{3/5}<2\). Therefore
\[
 \|E_{\ell,j}\|_{L^1}<4,\quad\|E_{\ell,j}\|_{L^2}<3,\qquad
 |a^{(\ell+1)}_{ji}|
 \le\Delta(a^2+4A/100)
 =\Delta(49/36+3/50)<A\Delta.                         \tag{6.6}
\]
This completes the forward induction through every interior layer,
up to \(a^{(L)}\), without using any current backwards row or delta.

Now start the backward pass at the top.
Let \(T_j=\sum_{i\le j}|\partial_{\xi^{(L)}_i}Z^{(L)}_j|\).
Differentiating the readout sum and top gate gives
\[
 \sum_{i\le j}|\partial_{\xi^{(L)}_i}\delta^{(L)}_j|
 \le\frac{\Delta}{100}\sum_{u<j}T_u+\frac{aS}{5}T_j
 \le(73/300)S\max_{v\le j}T_v.
\]
The strictly past-time top recursion and (6.6) imply
\[
 \max_{v\le j}T_v\le\exp\{A(73/300)S^2\}
                \le e^{657/800}<5/2.
\]
For the last comparison, \(657/800<5/6\) and
\(e^{5/6}<3^{5/6}<5/2\), since \(3^5 2^6<5^6\).
The top delta is pointwise bounded by \(aS/10\le7/40\).
Adding its learned covariance row in (4.5) proves
\[
 B_{L,k}\le(73/300)S(5/2)+a^2S^3/100
          \le73/80+147/3200=3067/3200<1.              \tag{6.7}
\]

For an interior \(\ell\), suppose the current upper row and delta have
just been bounded by \(1\) and \(7/40\).
Then, before bounding the current row at layer \(\ell\),
\[
 \|q^{(\ell)}_k\|_{L^2}
 \le\|\delta^{(\ell+1)}_k\|_{L^2}+aB_{\ell+1,k}
 \le7/40+7/6=Q,\qquad
 \|\delta^{(\ell)}_k\|_{L^2}\le Q/10<7/40.                \tag{6.8}
\]
This also holds at past indices by their already completed backward
passes. Including the current return in (4.6), (6.3) gives
\[
 \sum_{i\le k}|\partial_{\xi^{(\ell)}_i}\delta^{(\ell)}_k|
 \le (|q^{(\ell)}_k|/5+B_{\ell+1,k}/100)E_{\ell,k}.
\]
Cauchy--Schwarz, (6.5), (6.8), and the learned covariance term give
\[
 B_{\ell,k}
 \le3(Q/5+1/100)+SQ^2/100
 \le167/200+77763/2880000
 =2482563/2880000<9/10.                              \tag{6.9}
\]
Thus the backward pass proceeds all the way to layer 2, reproducing
the same bounds at each new layer. This closes the time induction.
At \(L=4\), the two interior passes are exactly \(\ell=2,3\)
forward and \(\ell=3,2\) backward; there is no new inequality at either.
The argument is identical for any fixed number of inserted layers.

For every query \(1\le\ell<L\), (6.1) implies
\[
 q^{(\ell)}_k=\zeta^{(\ell)}_k+\beta_{\ell,k},\quad
 |\beta_{\ell,k}|\le7/6,\quad
 \operatorname{Var}(\zeta^{(\ell)}_k)\le(7/40)^2.
\]
The shift need not be independent of its source.
Using \((u+v)^2\le2u^2+2v^2\) and a one-dimensional Gaussian integral,
\[
 \mathbb E e^{(q^{(\ell)}_k)^2/16}
 \le e^{49/288}\mathbb E e^{(\zeta^{(\ell)}_k)^2/8}
 \le e^{49/288}(1-49/6400)^{-1/2}<2.                 \tag{6.10}
\]
Indeed \(e^{49/288}<e^{1/5}\le5/4\) and the remaining factor is
less than \(4/3\). This bound is independent of depth, mesh, time index,
and cap. It is not a Gaussian path-supremum claim.

## 7. Removing every clip and uniquely restarting

Fix \(S=3/2\). At a fixed cap, (5.9) and the fixed-cap backwards
Lipschitz bounds give \(L^2\) convergence of each scalar-program query
at mesh nodes approaching any chosen time. Almost-everywhere
subsequences and Fatou in (6.10) imply
\[
 \sup_{R,s\le S}\mathbb E e^{(q_R^{(\ell)}(s))^2/16}\le2
                       \quad(1\le\ell<L).            \tag{7.1}
\]
The deterministic bound holds at every time; no common almost-sure
subsequence over all times is required.

For the asymmetric comparison let state \(A\) use cap \(R'\ge R\),
including \(R'=\infty\), and state \(B\) use cap \(R\) with bounded
reference readout. Each state's backwards queries are computed with
its own recursively clipped upper deltas. For \(2\le\ell<L\), exactly,
\[
\begin{split}
 \delta_{R'}^{(\ell)}(A)-\delta_R^{(\ell)}(B)
 ={}&\phi'(Z_A^{(\ell)})
          [\tau_{R'}(q_A^{(\ell)})-\tau_{R'}(q_B^{(\ell)})]\\
 &+[\phi'(Z_A^{(\ell)})-\phi'(Z_B^{(\ell)})]\tau_R(q_B^{(\ell)})\\
 &+\phi'(Z_A^{(\ell)})
          [\tau_{R'}(q_B^{(\ell)})-\tau_R(q_B^{(\ell)})].
\end{split}                                                     \tag{7.2}
\]
The last bracket vanishes for \(|q_B^{(\ell)}|\le R\) and is elsewhere
at most \(2|q_B^{(\ell)}|\). Put \(b_R(q)=(|q|-R/2)_+\); then
\(|q|\mathbf1_{|q|>R}\le2b_R(q)\).
Starting with (5.7), downward induction using (5.6), (7.2), and the
query difference inequality after (5.7) gives
\[
 \|\mathcal V_{R'}(A)-\mathcal V_R(B)\|
 +\sum_{\ell=2}^L
       \|\delta_{R'}^{(\ell)}(A)-\delta_R^{(\ell)}(B)\|_{L^2}
 +\sum_{\ell=1}^{L-1}\|q_{R'}^{(\ell)}(A)-q_R^{(\ell)}(B)\|_{L^2}
 \le C(1+R)d(A,B)
        +C\sum_{\ell=2}^{L-1}\|b_R(q_R^{(\ell)}(B))\|_{L^2}.           \tag{7.3}
\]
Here and below \(C\) can depend on the fixed depth and primal bounds,
but not \(R'\) or \(R\). Explicitly, at each downward step the previous
backwards error is multiplied by at most \(R_{\ell+1}/10\);
one adds \(C R\,d(A,B)\) and \(C\|b_R(q_B^{(\ell)})\|_{L^2}\).
There are finitely many such steps. No term multiplies an existing
backwards error by \(R\), proving the asserted linear cap dependence.
The final rank-one estimates give the vector-field part of (7.3).
No competitor tail or pointwise competitor readout bound was used.

If \(\mathbb E e^{q^2/K^2}\le2\), then
\[
 \mathbb E[q^2\mathbf1_{|q|>u}]
                  \le4K^2e^{-u^2/(2K^2)}.
\]
To prove it, use \(q^2e^{-q^2/(2K^2)}\le2K^2/e\), factor off the
tail exponential, and integrate the remaining \(e^{q^2/K^2}\).
Thus (7.1), with \(K=4\), gives
\[
 \sup_{s\le S}\|b_R(q_R^{(\ell)}(s))\|_{L^2}
      \le8e^{-R^2/256}=:\varepsilon_R
                   \quad(2\le\ell<L).               \tag{7.4}
\]
Absorb the finite layer sum into \(C\).
Subtract the clipped integral equations and use Gronwall:
\[
 \sup_{s\le S}d(\Theta_{R'}(s),\Theta_R(s))
             \le CS e^{C(1+R)S}\varepsilon_R.         \tag{7.5}
\]
It vanishes as \(R\to\infty\), uniformly in \(R'\ge R\). The continuous
path space in norm (5.2) is complete, so there is a uniform limit
\(\Theta\), retaining the primal and pointwise readout bounds.
All uncut backwards fields computed from that state are in \(L^2\),
by bounded gates and bounded operators. Evaluate (7.3) with
\(A=\Theta,R'=\infty\) and \(B=\Theta_R\). The factor \(1+R\) times
(7.5) still tends to zero. Hence clipped velocities and all backwards
fields converge uniformly to the actual uncut field and backwards
fields of \(\Theta\). Passing the integral equations proves a \(C^1\)
uncut feature flow on the whole interval \([0,3/2]\). No unbounded
product is passed using weak convergence.

For any other bounded-primal continuous uncut integral solution from
the same state, apply (7.3) against \(\Theta_R\). Its bounds only change
the finite Gronwall constant. Since \(e^{CR}\varepsilon_R\to0\) for
every finite \(C\), it must equal \(\Theta\). For a restart at
\(\sigma<S\), the initial discrepancy from \(\Theta_R(\sigma)\) is
at most \(C_0e^{C_0R}\varepsilon_R\). The new interval adds another
finite exponential factor, still vanishing. This proves existence
along the constructed remaining path and uniqueness from every reached
feature state. It does not assume local Lipschitzness of the uncut
field on arbitrary \(L^2\) neighborhoods.

## 8. The finite uncut feature-flow limit

Let \(\Theta_{n,R}\) be the finite clipped feature flow with the actual
hidden initialization but zero readout. Its fixed-clip limit was proved
in Section 5. Define
\[
 a_{n,R}(s)=\sum_{\ell=2}^{L-1}
       \left(\frac1n\sum_i b_R(q_{n,R,i}^{(\ell)}(s))^2\right)^{1/2},
 \quad
 a_R(s)=\sum_{\ell=2}^{L-1}\|b_R(q_R^{(\ell)}(s))\|_{L^2}.
\]
Joint \(\mathcal W_2\) convergence gives convergence of these quantities
at every time. At fixed cap, backwards queries are time-Lipschitz
by the state velocity and fixed-cap field estimates of Section 5.
The constants may depend on \(R,L,S\), but not width. Since \(b_R\)
is 1-Lipschitz, a finite time net gives
\[
 \sup_{s\le S}|a_{n,R}(s)-a_R(s)|\longrightarrow0
                       \quad\hbox{in probability}.   \tag{8.1}
\]
This measures continuous quadratic-growth tails; it does not assert a
finite-width exponential moment or use a discontinuous tail indicator.

The finite uncut feature GF with its prescribed small readout exists
by (5.4). Couple it to the zero-readout reference with the same hidden
initialization. The finite version of (7.3) gives
\[
 \sup_{s\le S}d_n(\Theta_n^{\rm GF}(s),\Theta_{n,R}(s))
 \le e^{C(1+R)S}\left[
 \frac{\|W^{(L+1)}_0\|_2}{\sqrt n}
                          +C\int_0^S a_{n,R}(u)\,du\right].      \tag{8.2}
\]
The initial norm event holds in probability, and the readout term is
\(O_{\mathbb P}(n^{-1})\). Only the zero-readout reference requires a
pointwise readout bound. At fixed cap, (8.1) and (7.4) control the
limiting right side by \(CSe^{C(1+R)S}\varepsilon_R\).
Let \(R\to\infty\), using (7.5), the fixed-clip laws, and (2.3).
This proves the full-sequence finite uncut feature-flow limit.

The backwards and query terms in (7.3) supply the same conclusion for
all backwards fields, uniformly in time and finite joint time lists.
Their extra factor \(1+R\) is absorbed by the Gaussian tail. Products
with bounded continuous gates follow by truncating their unbounded
factor as in Section 2. These observations will be used in Section 11.

## 9. Raw gradient structure and all finite physical times

The initial actions need not be Hilbert--Schmidt. Their trained
increments are: for an orthonormal basis \((e_j)\) of the input space,
\(\|A\|_{\rm HS}^2=\sum_j\|Ae_j\|_{L^2}^2\). Parseval proves independence
of the basis and \(\|U\otimes V\|_{\rm HS}=\|U\|_{L^2}\|V\|_{L^2}\).
Integrating the continuous rank-one velocities gives HS increments.
The rank-one difference estimate also holds in HS norm, so the clipped
integrals converge in HS to the same increments obtained in operator
norm.

Use raw coordinates in the affine Hilbert space with squared variation
norm
\[
 E_1[(dZ^{(1)})^2]
    +\sum_{\ell=2}^L\|dW^{(\ell)}\|_{\rm HS}^2
    +E_L[(dW^{(L+1)})^2].                       \tag{9.1}
\]
The predictor is continuously Frechet differentiable there.
For clarity, this is a scalar differentiability assertion, not an
unrestricted \(L^2\) Nemytskii differentiability claim.
For fixed \(B\in L^2\), bounded \(\phi',\phi''\) give
\[
 |\mathbb E B[\phi(Z+v)-\phi(Z)-\phi'(Z)v]|
 \le C R\|v\|_{L^2}^2+
             C\|B\mathbf1_{|B|>R}\|_{L^2}\|v\|_{L^2}.         \tag{9.2}
\]
Use the quadratic Taylor remainder where \(|B|\le R\), and the linear
remainder bound and Cauchy--Schwarz elsewhere. First fix \(R\) and
let \(\|v\|_{L^2}\to0\), then remove \(R\); the remainder is \(o(\|v\|_{L^2})\).

Forward differences are \(O(\|d\theta\|)\) in \(L^2\), by bounded
features/gates and \(\|dW\|_{\rm op}\le\|dW\|_{\rm HS}\), inductively
over the finitely many layers. Expand the scalar predictor from the
top down using (9.2), first with the old readout and then with each
old reverse field \(q^{(\ell)}\). They all belong to \(L^2\).
Terms with two varying factors are \(O(\|d\theta\|^2)\).
The finite sum of remainders is \(o(\|d\theta\|)\), giving
\[
 df=E_1[\delta^{(1)}dZ^{(1)}]
   +\sum_{\ell=2}^L E_\ell[\delta^{(\ell)}dW^{(\ell)}H^{(\ell-1)}]
   +E_L[H^{(L)}dW^{(L+1)}].
\]
The identity
\(\langle U\otimes V,A\rangle_{\rm HS}=\mathbb E[UAV]\)
follows by expansion in the input basis. Hence
\[
 \nabla f=(\delta^{(1)},
             (\delta^{(\ell)}\otimes H^{(\ell-1)})_{\ell=2}^L,
             H^{(L)}).                              \tag{9.3}
\]
Gradient continuity follows from forward continuity and (2.4) applied
to each fixed old backwards factor successively from the top down;
operator actions converge in operator norm. No Lipschitz assertion is
needed.

The inverse-coordinate chain rule, from (2.4) and bounded
\((F^{-1})'\), gives \((Z^{(1)})'=\phi'(Z^{(1)})q^{(1)}\).
Thus the uncut raw feature curve satisfies \(\theta_s=\nabla f\).
Consequently
\[
 f_s=\sum_{\ell=1}^{L+1}K^{(\ell)},\qquad
 K^{(1)}=E_1[(\delta^{(1)})^2],\quad
 K^{(\ell)}=E_\ell[(\delta^{(\ell)})^2]
             E_{\ell-1}[(H^{(\ell-1)})^2]\ (2\le\ell\le L),
 \quad K^{(L+1)}=E_L[(H^{(L)})^2]\ge25/36.        \tag{9.4}
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
 \quad s_*-s(t)\ge s_*e^{-2B_*t}>0.                   \tag{9.5}
\]
Uniqueness follows by separation of variables, or the Lipschitz scalar
comparison of Section 2. Thus every finite physical interval stays
inside the single constructed feature interval. In physical time
\[
 \theta_t=-2(f-1)\nabla f=-\nabla (f-1)^2,
 \quad f_t=-2(f-1)\sum_\ell K^{(\ell)},
 \quad \frac{d\mathcal L}{dt}=-4(f-1)^2\sum_\ell K^{(\ell)}.              \tag{9.6}
\]
This is the actual gradient flow in (9.1). Since
\(K^{(L+1)}\ge25/36\), the loss satisfies
\[
 \frac{d\mathcal L}{dt}\le-\frac{25}{9}\mathcal L,\qquad
 \mathcal L(0)=1,\qquad \mathcal L(t)\le e^{-25t/9}.
\]
Indeed, differentiate \(e^{25t/9}\mathcal L(t)\) using (9.6);
its derivative is nonpositive. Thus \(f(t)\to1\).

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
                   \int_{t_0}^t2(1-f(u))q^{(1)}(u)du.  \tag{9.7}
\]
Its right side is in \(L^2\), proving the required transformed
membership. The strictly increasing feature clock therefore makes it
an uncut feature solution. Section 7 identifies it until any first
attempt to leave \([0,s_*)\); scalar-clock uniqueness and (9.5) exclude
such an exit. This applies from zero and from every reached state, with
the absolute feature start \(\sigma=s(t_0)\). It proves global physical
uniqueness and restart in the theorem's class. All present velocities
are functions of the \(L+1\) present objects. No Gaussian source or
response coefficient in the proof is an extra dynamical input.

## 10. Exact raw GD and the physical finite-width comparison

We first note that finite physical GF exists for every finite horizon.
Its finite raw gradient has squared length \(\sum_\ell K_n^{(\ell)}\)
when vector variations use squared norm \(\|v\|_2^2/n\) and matrix
variations use ordinary squared Frobenius norm. Differentiating the
finite predictor verifies all \(L+1\) entries in (1.3), so the finite
deficit solves \((1-f_n)'=-2(1-f_n)\sum K_n^{(\ell)}\).
On its existence interval \(|r_n(t)|\le|r_n(0)|\). Integrating the
readout equation therefore gives
\(\|W^{(L+1)}(t)\|_2/\sqrt n
\le\|W^{(L+1)}_0\|_2/\sqrt n+2a|r_n(0)|t\).
Integrating the matrix operator-norm bounds successively from layer \(L\)
down to 2, then the first-vector velocity, gives polynomial bounds
on every finite compact physical interval. At fixed width these bound
all coordinates. The smooth finite-dimensional equations can be
continued by the local contraction construction, so no finite-time
escape occurs. Exact GD is defined at every finite step by (1.3).

On the high-probability event of (2.2) and small initial readout, the
finite feature GF on \([0,S]\), \(S=3/2\), has bounded continuous
kernel and satisfies \(df_n/ds\ge25/36\). Its initial predictor
tends to zero. If \(f_n(0)>-1/24\) and \(f_n(0)<1\), its unique
level-one point occurs before \(S\). The scalar physical clock
therefore stays inside \([0,S]\), by the same nonattainment argument
as (9.5). Section 8 gives uniform feature-predictor convergence.
The output is Lipschitz in (5.2) on bounded states, by expanding
\(\mathbb E[W^{(L+1)}H^{(L)}]\) and using Cauchy--Schwarz.
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

The raw matrix and readout updates on a positive prefix satisfy (5.4)
whenever its accumulated step is bounded by \(S_b\); this uses only
bounded activations and gates, not an exact Euler identity for \(F\).
They give \(|f_{n,k}|\le a(1+aS_b)\) and hence
\(0<\alpha_k\le C\eta_n\). The step into the first bad node is
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
be random. Its tail forcing still obeys a pathwise bound, because
\(a_{n,R}\) is time-Lipschitz at fixed cap:
\[
 \sum_{k<J}\alpha_k a_{n,R}(s_k)
 \le\int_0^{s_J}a_{n,R}(u)du+C_{R,L,S}\max_{k<J}\alpha_k
 \le\int_0^S a_{n,R}(u)du+C_{R,L,S}\eta_n.                  \tag{10.4}
\]
Applying (2.5) to (10.3) yields
\[
 \max_{k\le J}d_k\le e^{C(1+R)S}
 \left[\frac{\|W^{(L+1)}_0\|_2}{\sqrt n}
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

Finally compare GD and finite GF to the same zero-readout finite clipped
reference at their converging clocks. Its velocity is uniformly bounded
by (5.4), so clock differences contribute only a constant times their
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
bounded operator calls. Section 8 and (7.3) additionally control all backwards fields and
queries at every layer. Their joint laws with
the forward fields converge in \(\mathcal W_2\), uniformly in time.
For a bounded continuous gate \(g(Z)\) multiplying a field \(V\),
first replace \(V\) by its clip at a fixed level. The product is
approximable by bounded Lipschitz instructions. The discarded norm is
at most \(\|g\|_\infty\|V\mathbf1_{|V|>R}\|_{L^2}\).
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
are exactly (9.4), with no missing normalizing factor.

The exact feature preactivation velocities are
\[
 (Z^{(1)})'=\phi'(Z^{(1)})q^{(1)}=\delta^{(1)},\qquad
 (Z^{(\ell)})'=E_{\ell-1}[(H^{(\ell-1)})^2]\delta^{(\ell)}
       +W^{(\ell)}[\phi'(Z^{(\ell-1)})(Z^{(\ell-1)})']
                         \quad(2\le\ell\le L).        \tag{11.1}
\]
These follow by differentiating the forward equations, applying the
curve chain rule (2.4), and using
\((\delta^{(\ell)}\otimes H^{(\ell-1)})H^{(\ell-1)}
=\delta^{(\ell)}E_{\ell-1}[(H^{(\ell-1)})^2]\).
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
matrix operator norms and readout norms divided by \(\sqrt n\)
remain bounded by convexity along raw linear interpolation. The first preactivation velocity has
bounded norm divided by \(\sqrt n\). Differentiating successively
\(z^{(\ell)}=W^{(\ell)}\phi(z^{(\ell-1)})\), for
\(\ell=2,\ldots,L\), gives the same bound for every
recomputed velocity, using bounded features and gates. Hence every
hidden preactivation increment \(v\in\mathbb R^n\) satisfies
\(\|v\|_2/\sqrt n\le C\eta_n\), and hence
\(\|v\|_\infty\le C\eta_n\sqrt n\), on a step.
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
by bounded features and their Euclidean norm changes divided by \(\sqrt n\). The matrix difference
is \(O(\eta_n)\) in operator norm. The remaining gate difference is
\(O(\eta_n\sqrt n)\) in coordinate supremum and multiplies a left-node
velocity of bounded norm divided by \(\sqrt n\). Thus the discrepancy
from the node formula has Euclidean norm divided by \(\sqrt n\)
of order \(O(\eta_n\sqrt n)\).
For each layer \(\ell=3,\ldots,L\), repeat this argument with the
already bounded layer-\(\ell-1\) velocity and its just-controlled
discrepancy. This is a finite induction; its constants may depend on
\(L\). For feature velocities
multiply by the current gate and use the same supremum estimate.
This proves that all recomputed hidden velocities differ from their
node formulas, in Euclidean norm divided by \(\sqrt n\), by
\(O(\eta_n\sqrt n)=O(n^{-3/2})\) uniformly on the physical interval,
on its good event. No coordinatewise bound on the
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

## 12. Genuine nonlinear feature learning at every layer

### 12.1 Initial transposes and strictly positive movement

Let \(\nu_0=1\) and
\(\nu_\ell=E_\ell[(H^{(\ell)}_0)^2]\), \(1\le\ell\le L\),
be the initialized uncentered activation second moments.
The initial forward laws from Section 3 are
\[
 Z^{(\ell)}_0\sim N(0,\nu_{\ell-1}),\qquad
 \nu_\ell=1+\tfrac1{100}\mathbb E[
          \arctan(\sqrt{\nu_{\ell-1}}G)^2]>1
                         \quad(1\le\ell\le L).        \tag{12.1}
\]
The full uncentered moments include the constant term.
On the separate layer spaces define, backwards,
\[
 B^{(L)}=H^{(L)}_0\phi'(Z^{(L)}_0),\qquad
 B^{(\ell)}=\phi'(Z^{(\ell)}_0)(W^{(\ell+1)}_0)^*B^{(\ell+1)}
                                    \quad(1\le\ell<L).
\]
Then define forwards
\[
 V^{(1)}=B^{(1)},\qquad
 V^{(\ell)}=\nu_{\ell-1}B^{(\ell)}
       +W^{(\ell)}_0[\phi'(Z^{(\ell-1)}_0)V^{(\ell-1)}]
                                    \quad(2\le\ell\le L).        \tag{12.2}
\]
All are square-integrable by bounded gates and operators.

Here is the complete initial transpose induction.
Put \(\sigma_\ell^2=E_\ell[(B^{(\ell)})^2]\) and
\[
 \vartheta_\ell=\frac1{100\nu_{\ell-1}}
     \mathbb E\frac{Z^{(\ell)}_0\arctan Z^{(\ell)}_0}
                     {1+(Z^{(\ell)}_0)^2}>0\quad(2\le\ell\le L).
\]
Start with \(c_L=\vartheta_L\) and \(\sigma_L^2>0\).
For each \(\ell=L,L-1,\ldots,2\), the joint layer-\(\ell-1\) law is
\[
 (W^{(\ell)}_0)^*B^{(\ell)}
     =c_\ell H^{(\ell-1)}_0+\sigma_\ell G_{\ell-1},     \tag{12.3}
\]
where \(G_{\ell-1}\) is independent of \(Z^{(\ell-1)}_0\).
For \(\ell<L\), its coefficients satisfy
\[
 c_\ell=\vartheta_\ell c_{\ell+1}>0,\quad
 \sigma_\ell^2=
 \mathbb E[(\phi'(Z^{(\ell)}_0))^2
       (c_{\ell+1}^2\phi(Z^{(\ell)}_0)^2+\sigma_{\ell+1}^2)]>0.
                                                               \tag{12.4}
\]
To prove these claims, at the top apply the forward-then-transpose
calculation (3.2), with input \(H^{(L-1)}_0\) and reverse input
\(B^{(L)}\). The coefficient is
\(\mathbb E[Z^{(L)}_0B^{(L)}]/\nu_{L-1}=\vartheta_L\):
the odd offset contribution vanishes by Gaussian symmetry and the
remaining \(z\arctan z/(1+z^2)\) is positive off zero.

At any next matrix, condition at finite width on all earlier-layer
roots and matrices, its forward answer \(z^{(\ell)}_0\), and all
independent upper matrices. Its reverse input \(B^{(\ell)}_n\) is
then determined without seeing that matrix's conditional residual.
Thus (3.2) applies again. The preceding transpose law gives convergence
of the output-population pairings and full second moments.
Multiplication by a bounded gate follows by truncation, Section 2(b);
a subsequent operator call preserves the discarded \(L^2\) error.
This proves joint empirical-average convergence, including the old
input-population tuple. The independent Gaussian term in the preceding
transpose has zero contribution to \(\mathbb E[Z^{(\ell)}_0B^{(\ell)}]\);
Gaussian symmetry gives \(c_\ell=\vartheta_\ell c_{\ell+1}\).
The full input second moment is exactly (12.4), not a variance after
subtracting the response. The rank-one residual projection in (3.2)
has vanishing squared Euclidean norm divided by \(n\), and conditional Gaussian
averaging gives the innovation jointly with the old tuple.
This proves the induction without claiming iid reused coordinates.

In particular \(B^{(1)}\ne0\), since (12.3) for \(\ell=2\),
multiplied by the strictly positive gate, has strictly positive
second moment. Define
\[
 \gamma_1=E_1[(B^{(1)})^2]>0,\quad
 \gamma_\ell=\nu_{\ell-1}E_\ell[(B^{(\ell)})^2]>0
                     \ (2\le\ell\le L),\quad
 \Gamma=\sum_{\ell=1}^L\gamma_\ell>0.
\]
Adjunction and the definitions yield, by a forward induction,
\[
 E_\ell[B^{(\ell)}V^{(\ell)}]
             =\sum_{j=1}^\ell\gamma_j>0.              \tag{12.5}
\]
Indeed the matrix term in (12.2) pairs as
\(E_{\ell-1}[B^{(\ell-1)}V^{(\ell-1)}]\).
Therefore each \(V^{(\ell)}\) and
\(\phi'(Z^{(\ell)}_0)V^{(\ell)}\) is nonzero in \(L^2\).

### 12.2 Initial motion and nonconstant kernels

The readout integral gives \(W^{(L+1)}(s)/s\to H^{(L)}_0\).
Applying (2.4) and bounded operator continuity successively backwards
gives \(\delta^{(\ell)}(s)/s\to B^{(\ell)}\) in \(L^2\).
Equations (11.1)--(12.2) then give for every hidden layer
\[
 (Z^{(\ell)})'(s)=sV^{(\ell)}+o(s),\quad
 Z^{(\ell)}(s)-Z^{(\ell)}_0=\tfrac12s^2V^{(\ell)}+o(s^2),
\]
\[
 (H^{(\ell)})'(s)=s\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(s),\quad
 H^{(\ell)}(s)-H^{(\ell)}_0
       =\tfrac12s^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(s^2).
                                                               \tag{12.6}
\]
All remainders are in \(L^2\). Integrating an \(o(s)\) remainder gives
\(o(s^2)\), by bounding its norm by \(\epsilon s\) near zero.
Likewise, in HS norm, each trained matrix has
\[
 W^{(\ell)}(s)-W^{(\ell)}_0
   =\tfrac12s^2B^{(\ell)}\otimes H^{(\ell-1)}_0+o(s^2),
                         \quad 2\le\ell\le L,
\]
with positive leading squared size \(s^4\gamma_\ell/4\).
The readout has nonzero first-order motion and the raw first vector
has nonzero second-order motion.

Using (12.5), square-integrable convergence and bounded features,
\[
 K^{(\ell)}(s)=\gamma_\ell s^2+o(s^2)\ (1\le\ell\le L),\quad
 K^{(L+1)}(s)=\nu_L+\Gamma s^2+o(s^2),\quad
 (K^{(L+1)})'(s)=2\Gamma s+o(s)>0
\]
for sufficiently small \(s>0\). The last coefficient includes all
lower-layer motion because
\(\mathbb E[H^{(L)}_0\phi'(Z^{(L)}_0)V^{(L)}]=\Gamma\).
Since \(s(t)=2t+o(t)\), in physical time
\[
 H^{(\ell)}(t)-H^{(\ell)}_0
       =2t^2\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t^2),\qquad
 K^{(L+1)}(t)=\nu_L+4\Gamma t^2+o(t^2),
\]
\[
 \sum_{\ell=1}^{L+1}K^{(\ell)}(t)
                         =\nu_L+8\Gamma t^2+o(t^2).    \tag{12.7}
\]
Also \(\dot Z^{(\ell)}(t)=4tV^{(\ell)}+o(t)\) and
\(\dot H^{(\ell)}(t)=4t\phi'(Z^{(\ell)}_0)V^{(\ell)}+o(t)\).
For example the integrated squared feature velocity as \(T\downarrow0\)
is
\[
 \int_0^T\mathbb E[(\dot H^{(\ell)}(t))^2]dt
  =\tfrac{16}{3}\mathbb E[
       (\phi'(Z^{(\ell)}_0)V^{(\ell)})^2]T^3+o(T^3)>0.
\]
The preactivation formula replaces the gated variable by \(V^{(\ell)}\).
The population coefficients are strictly positive at each fixed depth,
independently of width. Thus at sufficiently small fixed positive time
the finite hidden squared changes divided by \(n\) converge to positive
values, and so does the kernel change. This is non-lazy feature learning,
not an \(\epsilon\to0\) or frozen-layer limit.

### 12.3 Hidden laws remain strictly non-affine at every finite time

Prove lower tails in the actual finite scalar programs, then pass them
to the flow. Let \(\overline\Phi(u)=\mathbb P(G\ge u)\).
Each forward source variance lies between \(c_-^2\) and \(a^2\).
At the top, Section 6 implies
\[
 |Z^{(L)}_k-\xi^{(L)}_k|\le AaS^2/10=63/160,\quad
 \mathbb P(\pm Z^{(L)}_k\ge u)
       \ge\overline\Phi((u+63/160)/c_-)>0.              \tag{12.8}
\]
No independence of the bounded correction is needed.

At every interior layer \(2\le\ell<L\),
\[
 |Z^{(\ell)}_k-\xi^{(\ell)}_k|
 \le R_{\ell,k}:=\frac{A\Delta}{10}
                    \sum_{j<k}(|\zeta^{(\ell)}_j|+a),\quad
 \mathbb E R_{\ell,k}\le ASQ/10=483/1600.
\]
The dominator depends only on the backwards source group, hence is
independent of \(\xi^{(\ell)}_k\). The correction itself need not be.
By Markov and that independence, for either sign and \(u>0\),
\[
 \mathbb P(\pm Z^{(\ell)}_k\ge u)
 \ge\frac{1117}{1600}\overline\Phi((u+1)/c_-)>0.          \tag{12.9}
\]
At the bottom, since \(L\ge3\) the layer-2 delta is an interior delta,
so its norm is at most \(Q/10\). Therefore
\[
 |X^{(1)}_k-F(Z^{(1)}_0)|
 \le R_{1,k}:=\Delta\sum_{j<k}|\zeta^{(1)}_j|+aS,\quad
 \mathbb E R_{1,k}\le S(Q/10+a)=1561/800<2.
\]
This dominator is independent of the root. Since \(F\) is odd and
increasing, the independent root event and
\(\mathbb P(R_{1,k}\le4)\ge1/2\) yield
\[
 \mathbb P(\pm Z^{(1)}_k\ge u)
       \ge\tfrac12\overline\Phi(F^{-1}(F(u)+4))>0.      \tag{12.10}
\]

Bounds (12.8)--(12.10) are uniform in time index, mesh and cap.
They pass first to every fixed-clip flow time, then to the uncut flow:
under weak convergence the limiting probability of a closed half-line
is at least the limsup of its approximating probabilities. This follows
by decreasing continuous distance cutoffs to its indicator. Thus every
hidden law has both tails arbitrarily far out, at every reached time.

For any such \(Z\), \(\operatorname{Var}(Z)>0\), and minimizing over
the affine coefficients gives
\[
 \inf_{\alpha,\beta}\mathbb E[(\phi(Z)-\alpha Z-\beta)^2]
 =\operatorname{Var}(\phi(Z))-
       \frac{\operatorname{Cov}(Z,\phi(Z))^2}{\operatorname{Var}(Z)}
 >0.                                                         \tag{12.11}
\]
The minimum is attained. If it were zero, boundedness of \(\phi\)
and the unbounded support would force zero slope; strict monotonicity
would then force \(Z\) constant, a contradiction.
All displayed moments are continuous along the \(L^2\) path by bounded
Lipschitz \(\phi\) and Cauchy--Schwarz. The positive variance and positive
affine error have positive minima on every compact physical interval,
simultaneously over the finitely many layers. Uniform joint
second-moment convergence transfers a smaller positive bound to finite
empirical errors with probability tending to one. The fixed activation
is nonaffine at every width, and its nonlinearity does not disappear
under any hidden limiting law.

### 12.4 No hidden layer freezes at a later finite time

At any reached feature time \(s>0\), (5.5) gives
\(W^{(L+1)}(s)\ge c_-s\) almost surely. Since \(\phi'>0\),
\(\mathbb E[(\delta^{(L)}(s))^2]>0\).
Approximate this time by fixed-clip Euler programs, first refining
their mesh and then removing their cap. Their backwards laws converge,
so the source variances
\(\operatorname{Var}(\zeta^{(L-1)}_k)
 =\mathbb E[(\delta^{(L)}_k)^2]\)
eventually have a positive lower bound.
As \(|q^{(L-1)}_k-\zeta^{(L-1)}_k|\le a\), Gaussian lower tails
and the closed-half-line passage prove unbounded support of
\(q^{(L-1)}(s)\), hence nonzero \(\delta^{(L-1)}(s)\).
Repeat downward, using the just established nonzero upper delta to
bound the next reverse-source variance away from zero. This proves
nonzero \(\delta^{(\ell)}(s)\) for every hidden layer, including 1.
It is sequential, not circular.

All hidden kernels are consequently positive. Formula (11.1) and
adjunction give, by forward induction,
\[
 E_\ell[\delta^{(\ell)}(Z^{(\ell)})']
            =\sum_{j=1}^{\ell}K^{(j)}>0
                          \quad(1\le\ell\le L).      \tag{12.12}
\]
The base is \((Z^{(1)})'=\delta^{(1)}\); the next matrix term pairs
to the preceding layer by the backwards definition.
Thus no hidden preactivation velocity is zero in \(L^2\).
Strictly positive gates preserve nonzero feature velocities.
The physical multiplier \(2(1-f)\) is strictly positive at every
finite physical time by (9.5), so every hidden physical velocity is
nonzero for \(t>0\). Initial hidden velocities vanish because the
population readout is zero; their strictly nonzero second-order onset
was proved above.

This completes all assertions for every fixed \(L\ge3\), with the same
single activation. The model has no auxiliary caps, source jitters,
oracle coefficients, or Euler meshes left in its equations.
The response bound is uniform in depth; other constants can depend on
the chosen finite depth. No joint \(L,n\) limit or unshifted-arctan
theorem is asserted.
