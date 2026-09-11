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


## Nonlinear activation, separation, and continuation additions

These fragments extend the global nonlinear and special-data chapters. Each probability statement takes width to infinity at a fixed depth, fixed finite dataset, fixed activation, and fixed finite physical horizon. Constants uniform over a parameter class do not assert a probability supremum over that class. Layer populations are separate. Initialized actions and their adjoints are constructed jointly; only trained increments are Hilbert--Schmidt.

The packages are: a global two-hidden-layer activation transform and its affine-first arbitrary-data exception; a local fixed-depth C1,1 theorem and its Gaussian strict-activity corollary; separated two-sample offset, odd, and general-shape theorems; all-fixed-depth odd perturbations; the three-sample odd-gain theorem; and exact moderate-amplitude identities, local limits, finite-algorithm estimates, strong endpoints, and conditional continuation.

The finite Gaussian construction, including rank loss, causal bounded-derivative scalar feedback, common generated spaces, and adjunction, is the contained proof in **special-data Section III.F**. The observation and same-width comparison arguments are **Section III.V**. They are mathematical dependencies within the library. Their coordinate hypotheses are verified below; neither theorem is applied directly to an instruction with unbounded derivative. Equation numbers inside each numbered fragment are local to that fragment.

For the two-sample and odd-gain fragments using first-coordinate notation \(V^1\) or \(w\), the exact conversion to the notation contract is
\[
 V^1=W^{(1)}/\sqrt d,\qquad z_a^1=V^1x_a,
 \qquad \frac d n\|dV^1\|_F^2=\frac1n\|dW^{(1)}\|_F^2.
\]
A displayed first matrix with entry variance \(1/d\), including a locally named \(W^1\), always means this \(V^1\). For finite vectors, any rank-one symbol u tensor v or \(u\otimes v\) means the matrix uv^T/n; its population counterpart is the rank-one action q -> u E[vq]. The stored readout is \(C=W^{(L+1)}\), and \(f_a=C^Th_a^L/n\). The half-sum loss in those fragments is explicitly \(\frac12\sum_a(f_a-y_a)^2\); its raw mobilities in canonical coordinates are \((n,1,\ldots,1,n)\). The broad two-layer theorem instead uses the unhalved sum, and the general local theorem uses its stated weighted mean. Their factors of two are retained. An auxiliary feature time or normalized time is never the raw GD step.

There are 46 proof units after the common lemmas. They are organized as follows.

| Fragments | Result | Destination and exact scope |
|---|---|---|
| A, B | Continuous-value Gaussian specialization; activation transform; affine-first exception | Global nonlinear: L=2, bounded top activation/readout, orthogonal data; arbitrary fixed input geometry for an affine first activation. Exact raw GD uses eta_n sqrt(n)->0, or eta_n->0 in the affine exception. |
| C | Local C1,1 limit, finite-GF corollary, strict Gaussian activity | Global nonlinear: fixed L,m,d, subGaussian first/readout roots and arbitrary fixed data on one positive interval; activity has its additional stated Gaussian/nondegeneracy assumptions. |
| D | Offset separation theorem | Special data: L=3,m=2, rho in [-1,1-delta], binary labels, a delta-selected coefficient, full compact-physical-time GF/GD bundle. |
| E | Odd perturbations at e<=c_poly delta^2 | Special data: L=3,m=2, two-sided separation, all binary labels; convex and unit-Gaussian-energy variants. |
| F | General nonodd/linear-growth shapes and affine positivity | Special data: L=3,m=2, e<=c_dyn delta^(31/8); a further shape cutoff gives persistent nonaffinity. Affine positivity is an exact separate lemma. |
| G | Odd perturbations at all fixed depths | Special data: each fixed L>=4; explicit depth-dependent coefficient/exponent, full GF/GD and motion bundle. |
| H | One odd large-gain activation for all fixed depths | Special data: m=3, fixed L>=2, two-sided separation and binary labels; gain depends on separation, not depth. |
| I | Moderate sine initialization/local limit/finite algorithms/endpoints/conditional global construction | Exact calibrated coefficient 2/5; no unconditional global population theorem is asserted. |
| J | Bounded learned memories and simultaneous-coordinate obstruction | Exact identities or conditional necessary inequalities at their displayed model scopes. |

The term “full bundle” in this table means the explicitly stated same-layer path and field/velocity Wasserstein-2 laws, finite collections of times, all true kernel blocks, fixed generated actions/adjoints, predictions, loss, second moments and integrated squared speeds. It excludes cross-layer neuron pairing, cross-width operator-norm convergence, a growing query language and an infinite-time/width interchange. B and C retain their own narrower observable statements.

Fragments A–C are below. Fragments D–J are in the
[special-data chapter](special_data_limits.md), under “Further correlated-data
nonlinear families”. The references to III.F and III.V mean the complete
proofs in that chapter.

## A. Contained probability and continuity specializations

### A.1. Continuous, at-most-linear value instructions

**Lemma.** Extend the finite-program value conclusion of Section III.F to a fixed finite program whose coordinate maps are continuous and satisfy \(|F(x)|\le C(1+|x|)\). Roots are iid finite-second-moment tuples, independent of the initialized Gaussian matrices. Every fixed same-layer tuple converges in probability in \(\mathcal W_2\). The action interpretation is the continuous extension of the actions already constructed in Section III.F. This assertion gives values and second moments, without asserting a formal-derivative formula for these extra instructions.

**Proof.** If \(X_j\to X\) in \(L^2\), continuity and the linear envelope imply \(F(X_j)\to F(X)\) in \(L^2\). Indeed \(|X_j|^2\) is uniformly integrable; uniform continuity on compact balls gives convergence in probability, and the linear envelope supplies uniform integrability of the squared outputs. The same argument proves continuity of pushforward in \(\mathcal W_2\).

Choose smooth compactly supported \(F_R\) converging locally uniformly to \(F\), with a common envelope \(C'(1+|x|)\). Such maps follow by a cutoff on the radius-\(2R\) ball, mollification, and increasing \(R\); each has a finite bounded first derivative. At a fixed limiting input \(X\), \(\|F_R(X)-F(X)\|_2\to0\). Once a prefix has its joint \(\mathcal W_2\) law, its empirical squared approximation error also converges, because \(|F_R-F|^2\) is continuous with at most quadratic growth.

Induct through the finite instructions. Coordinate instructions pass by the pushforward argument. For a matrix instruction, approximate its entire already constructed input prefix by bounded-derivative programs. At finite width the output RMS error is at most the initialized operator bound times the input RMS error; the identical bound holds on the generated population spaces. Thus the matrix outputs are Cauchy in the required law and agree with the extended action. To construct prefix approximants, first choose the current smooth map to achieve its desired limiting error, and only then choose the preceding-prefix tolerance smaller than that error divided by the smooth map's Lipschitz constant. This order avoids any assumption that cutoff Lipschitz constants are uniform. Finite unions of the approximant programs give joint laws, so the induction retains all desired same-layer tuples and both orientations. Let width tend to infinity at each fixed approximant and then remove its approximation. The finite number of instructions completes the proof. \(\square\)

For the activation flow \(J(s,z)\) below, \(|J(s,z)|\le|z|+M|s|\) and joint continuity are sufficient for this lemma. Its possible \(\exp(L|s|)\) sensitivity to the frozen root is not assumed bounded. No response derivative of \(J\) is used. Feedback in that application is transferred separately by the same-root clock stability estimate proved in the two-layer fragment.

### A.2. Fixed neural programs with unbounded backward products

For a **fixed** program with subGaussian root marginals, C2 activations with bounded first and second derivatives, and products \(b(z)q\) with bounded C1 \(b,b'\), the values in A.1 also have the ordinary named-source response formulas obtained by truncating each such product. This is a fixed-program specialization, not an all-moment theorem for arbitrary scalar-feedback programs.

Here are the derivative details. Freeze deterministic coefficients and covariance parameters. Replace each product by \(b(z)\tau_R(q)\), where \(|\tau_R(q)|\le|q|\), \(|\tau_R'|\le1\), and the clip equals the identity on larger and larger compact intervals. At fixed \(R\), every coordinate instruction meets Section III.F's bounded-derivative hypotheses. In the finite scalar recursion, every value has a linear envelope in the finite root/source list, uniformly in the clips while earlier coefficients stay in a compact set. Each first named-source derivative has a polynomial envelope in that list: the only extra factor introduced by differentiating a product is \(|q|\), and there are only finitely many instructions. The clip derivative is bounded by one.

Proceed chronologically in this scalar recursion. Second moments of earlier inputs converge; hence the next finite covariance matrix converges. Couple its Gaussian sources by their positive-semidefinite square roots. The square roots converge even at rank loss, as proved in Section III.F. On this coupling the roots have all moments, and the Gaussian sources have uniformly bounded moments of every fixed order. Local C1 convergence of the clipped expressions and the polynomial derivative envelopes imply convergence in probability and uniform integrability of their first derivatives. Their expectations therefore converge. This identifies the next response coefficient, keeps it bounded, and closes the finite induction. Values agree with A.1 by its same-array RMS approximation and bounded actions. Roots are never differentiated; arbitrary subGaussian iid root tuples are admitted directly as roots. This proves the stated derivative specialization without a quantile-map differentiation or a claim about empirical higher moments.

Locally Lipschitz scalar contractions can be replaced causally by their deterministic limiting values. In the local theorem below their actual finite feedback is recovered by the separately proved one-reference tail comparison. In capped training programs Section III.F already proves this feedback passage directly. No assertion concerning an increasing transcript is needed.

### A.3. Sharp initialized action constant with a contained proof

For an \(n\times n\) matrix \(G\) of independent standard Gaussians,
\[
 E\|G\|_{op}\le2\sqrt n,\qquad
 \Pr\{\|G/\sqrt n\|_{op}>2+\varepsilon\}
 \le (\varepsilon^2n)^{-1}.
\]
Thus every fixed collection of finite initialized actions has norm at most three with probability tending to one, and their canonical generated actions have norm at most two. This supplies the constants used in the odd-gain and fixed-depth affine arguments.

For completeness, compare Gaussian processes \(X_{u,v}=u^TGv\) and \(Y_{u,v}=g^Tu+h^Tv\) on pairs of unit vectors. If \(\alpha=u^Tu'\), \(\beta=v^Tv'\), their increment-variance difference is \(2(1-\alpha)(1-\beta)\ge0\). On a finite net, the Gaussian comparison follows by interpolating the independent processes in \(E[b^{-1}\log\sum_i\exp(bZ_i)]\). Gaussian integration by parts makes the derivative equal to
\(\frac b4 E\sum_{i,j}p_ip_j(d_Y(i,j)^2-d_X(i,j)^2)\ge0\), where the \(p_i\) are softmax weights. Let \(b\to\infty\), then increase the finite nets. Continuity and integrability give \(E\sup X\le E\sup Y=E\|g\|+E\|h\|\le2\sqrt n\).

The Gaussian Poincare inequality needed for the probability bound also has a short proof. For smooth bounded \(f\), let \(P_tf(x)=E f(e^{-t}x+\sqrt{1-e^{-2t}}Z)\). Integration by parts against the Gaussian density gives
\[
 -\frac d{dt}E(P_tf)^2=2E|\nabla P_tf|^2,
 \qquad \nabla P_tf=e^{-t}P_t\nabla f.
\]
Integrate from zero to infinity and apply Jensen and Gaussian invariance to obtain \(\operatorname{Var}f\le E|\nabla f|^2\). Smooth cutoff approximations extend it to Lipschitz \(f\). The spectral norm is one-Lipschitz in the Frobenius coordinates, so \(\operatorname{Var}\|G\|_{op}\le1\); Chebyshev proves the displayed bound. Finite norm inequalities pass to each generated input, then to their countable dense span. Taking rational \(\varepsilon\downarrow0\) gives the canonical constant two. No exponential matrix-concentration theorem is imported.

### A.4. Scalar gradient and strong-chain rules

For bounded continuous \(b\), if \(Z_j\to Z\), \(Q_j\to Q\) in \(L^2\), then
\[
 \|b(Z_j)Q_j-b(Z)Q\|_2\to0.
\]
Subtract the varying \(Q\) first; for the other term truncate the fixed \(Q\) and use bounded convergence. The same proof is uniform over a compact \(L^2\) family using a finite net. Hence bounded activation derivatives give the strong chain rule along C1 \(L^2\) curves, and bounded actions with Hilbert--Schmidt derivatives obey \((WH)'=W'H+WH'\). This does not assert Frechet differentiability of a nonlinear activation map on the whole \(L^2\) space.

For a scalar prediction, Frechet differentiability in the raw Hilbert metric does hold under the bounded-derivative hypotheses used below. For a fixed reverse factor \(q\), the scalar Taylor remainder is bounded by
\[
 \tfrac12 L M\|h\|_2^2+2D\|q\mathbf1_{|q|>M}\|_2\|h\|_2.
\]
Here \(D\) bounds the derivative and \(L\) its Lipschitz constant. First take \(\|h\|_2\downarrow0\), then \(M\to\infty\). Expand the finite number of action/activation products and use \(\|\Delta W\|_{op}\le\|\Delta W\|_{HS}\). This proves the true scalar derivative, its backward-adjoint formula, and continuity of that gradient. Every energy identity below consequently belongs to the specified raw metric.


## B. Global two-layer limits beyond one activation

The theorem below uses the unhalved sum loss and the displayed positive block constants. Orthogonal input projections are essential to its nonlinear first-layer coordinate proof. Its affine-first corollary admits every fixed Gram matrix, including singular matrices. Width identification uses the value lemma A.1; no formal sensitivity formula for the activation transform is invoked.

### B.1. Global two-hidden-layer activation transform

Within this proof unit, unqualified section and equation numbers are local.

#### The theorem and the network

Fix \(m<\infty\) inputs \(x_a\in\mathbb R^d\) satisfying
\[
\frac{x_a^\top x_b}{d}=\mathbf 1_{\{a=b\}},
\qquad 1\le a,b\le m.
\]
Fix labels \(y_a\in\mathbb R\) and positive constants \(\kappa_1,\kappa_2,\kappa_3\), independent of width and step size. Allow different activations in the two hidden layers:

- \(\phi^{(1)}\) is continuously differentiable, and \((\phi^{(1)})'\) is bounded and globally Lipschitz. The activation itself need not be bounded, monotone, or odd.
- \(\phi^{(2)}\) is bounded and continuously differentiable, and \((\phi^{(2)})'\) is bounded and globally Lipschitz.

The dimensions are \(W^{(1)}\in\mathbb R^{n\times d}\), \(W^{(2)}\in\mathbb R^{n\times n}\), and \(W^{(3)}\in\mathbb R^n\). The readout \(W^{(3)}\) is the rescaled readout throughout. Define
\[
\begin{aligned}
z_a^{(1)}&=\frac{W^{(1)}x_a}{\sqrt d},
&
h_a^{(1)}&=\phi^{(1)}(z_a^{(1)}),\\
z_a^{(2)}&=W^{(2)}h_a^{(1)},
&
h_a^{(2)}&=\phi^{(2)}(z_a^{(2)}),\\
f_{n,a}&=\frac{(W^{(3)})^\top h_a^{(2)}}{n},
&
r_{n,a}&=f_{n,a}-y_a,
\qquad L_n=\sum_{a=1}^m r_{n,a}^2.
\end{aligned}
\]
The residual-free backpropagated derivatives are
\[
\delta_a^{(2)}
=
W^{(3)}\odot(\phi^{(2)})'(z_a^{(2)}),
\qquad
\delta_a^{(1)}
=
(\phi^{(1)})'(z_a^{(1)})
\odot(W^{(2)})^\top\delta_a^{(2)}.
\]
Thus \(\delta_a^{(\ell)}=n\,\partial f_{n,a}/\partial z_a^{(\ell)}\). The exact updates are
\[
\begin{aligned}
z_{a,k+1}^{(1)}
&=
z_{a,k}^{(1)}
-2\kappa_1\eta_n r_{n,a,k}\delta_{a,k}^{(1)},\\
W_{k+1}^{(2)}
&=
W_k^{(2)}
-\frac{2\kappa_2\eta_n}{n}
\sum_{a=1}^m
r_{n,a,k}\delta_{a,k}^{(2)}(h_{a,k}^{(1)})^\top,\\
W_{k+1}^{(3)}
&=
W_k^{(3)}
-2\kappa_3\eta_n
\sum_{a=1}^m r_{n,a,k}h_{a,k}^{(2)}.
\end{aligned} \tag{1}
\]
The first equation uses orthogonality. In the original first weights, it follows from
\[
W_{k+1}^{(1)}
=
W_k^{(1)}
-\frac{2\kappa_1\eta_n}{\sqrt d}
\sum_{a=1}^m r_{n,a,k}\delta_{a,k}^{(1)}x_a^\top.
\]

Initialize independently by
\[
W_{0,ij}^{(1)}\sim N(0,\sigma_1^2),
\qquad
W_{0,ji}^{(2)}\sim N(0,\sigma_2^2/n),
\]
where the variances are fixed and finite. The following readout initializations are allowed:

- A vanishing Gaussian readout
  \[
  W_{0,j}^{(3)}\sim N(0,\sigma_3^2n^{-2\beta}),
  \qquad \beta>0.
  \]
  Here \(\beta\) describes the decay of the standard deviation. Gaussian tail bounds give
  \[
  \|W_0^{(3)}\|_\infty
  =
  O_{\mathbb P}(n^{-\beta}\sqrt{\log n})
  \longrightarrow0.
  \]
  The original initialization has \(\beta=1\).
- More generally, an independent readout whose coordinate supremum tends to zero in probability. Its population initialization is zero.
- A fixed bounded readout law: the coordinates are iid with a law supported on \([-B_0,B_0]\), independently of the other initialization. The population starts from that law. A perturbation whose coordinate supremum tends to zero may also be added, giving a finite initial supremum at most \(B_0+o_{\mathbb P}(1)\).

An arbitrary bounded iid law is admitted directly as a root tuple in A.1. The bounded nonvanishing option does **not** include an untruncated \(O(1)\) Gaussian readout: that initialization lacks the population supremum bound used in this proof.

For every fixed \(T<\infty\), the population equations have a unique autonomous gradient-flow solution on \([0,T]\). For every sequence
\[
\eta_n>0,
\qquad
\eta_n\sqrt n\longrightarrow0,
\]
the exact GD trajectories on the clock \(t=k\eta_n\) converge to that solution. Interpolate the finite parameters linearly and recompute the forward pass between steps.

The conclusion includes predictions, summed loss, all kernel-block entries, same-layer joint hidden path laws with their second moments, and fixed finite collections of continuous globally Lipschitz forward/adjoint measurements. Products in these measurement constructions must have bounded varying factors; the unbounded backward fields and their quadratic measurements are included through the tail argument below. Integrated squared hidden speeds converge as well. Convergence is in probability, uniformly in time for the stated pointwise measurements. No claim about arbitrary higher-growth measurements is needed.

The step condition is sufficient, not claimed necessary. These activation assumptions alone do not force nonlinearity or motion: they intentionally include a constant or affine first activation. Additional assumptions for strict feature learning appear at the end.

#### A scalar coordinate that removes the first-layer gate

Let \(J(s,z)\) solve
\[
\frac{\partial J(s,z)}{\partial s}
=
(\phi^{(1)})'(J(s,z)),
\qquad
J(0,z)=z,
\qquad s\in\mathbb R.
\tag{2}
\]
Write
\[
M_1=\|(\phi^{(1)})'\|_\infty,
\qquad
L_1=\operatorname{Lip}((\phi^{(1)})').
\]
The bounded Lipschitz scalar vector field has a unique global solution in both time directions. Integration and the scalar difference inequality give
\[
|J(s,z)-J(t,z)|\le M_1|s-t|,
\qquad
|J(s,z)|\le |z|+M_1|s|,
\tag{3}
\]
\[
|J(s,z)-J(s,w)|
\le e^{L_1|s|}|z-w|.
\]
In particular, \(J\) is jointly continuous. Uniqueness gives the flow identity
\[
J(s,J(t,z))=J(s+t,z),
\]
because both sides solve the same scalar equation as functions of \(s\), with the same value at \(s=0\). Also,
\[
|\phi^{(1)}(J(s,z))-\phi^{(1)}(J(t,z))|
\le M_1^2|s-t|. \tag{4}
\]

For each input introduce a clock displacement \(X_a^{(1)}(0)=0\), keeping the fixed Gaussian root \(Z_{0,a}^{(1)}\), and set
\[
Z_a^{(1)}(t)
=
J(X_a^{(1)}(t),Z_{0,a}^{(1)}).
\tag{5}
\]
The population network is
\[
\begin{aligned}
H_a^{(1)}&=\phi^{(1)}(Z_a^{(1)}),
&
Z_a^{(2)}&=W^{(2)}H_a^{(1)},\\
H_a^{(2)}&=\phi^{(2)}(Z_a^{(2)}),
&
f_a&=\mathbb E[W^{(3)}H_a^{(2)}],
\qquad r_a=f_a-y_a,\\
\delta_a^{(2)}
&=
W^{(3)}(\phi^{(2)})'(Z_a^{(2)}),
&
\delta_a^{(1)}
&=
(\phi^{(1)})'(Z_a^{(1)})
(W^{(2)})^*\delta_a^{(2)}.
\end{aligned}
\]
Its transformed equations are
\[
\begin{aligned}
\dot X_a^{(1)}
&=-2\kappa_1 r_a(W^{(2)})^*\delta_a^{(2)},\\
\dot W^{(2)}
&=-2\kappa_2\sum_{a=1}^m
r_a\delta_a^{(2)}\otimes H_a^{(1)},\\
\dot W^{(3)}
&=-2\kappa_3\sum_{a=1}^m r_aH_a^{(2)}.
\end{aligned} \tag{6}
\]
Here the rank-one action is explicitly
\[
(u\otimes v)V=u\,\mathbb E[vV].
\]
Every expectation pairs coordinates of the same layer. The first-layer and second-layer populations are separate.

The initial \(W_0^{(2)}\) is the bounded forward-and-adjoint action obtained from the joint limits of finite Gaussian matrix calculations, as described below. It is **not** an ordinary continuum matrix or integral kernel with iid Gaussian entries. The notation records its action on generated population fields, together with its adjoint.

The scalar chain rule converts (6) into the ordinary first-layer equation
\[
\dot Z_a^{(1)}=-2\kappa_1 r_a\delta_a^{(1)}.
\tag{7}
\]
Conversely, any solution of (7) in the bounded state class used below has representation (5). Indeed, Cauchy–Schwarz and Fubini make its backward coefficient integrable in time at almost every coordinate. For an integrable scalar coefficient \(b(t)\), the equation
\[
\dot z(t)=b(t)(\phi^{(1)})'(z(t))
\]
has the solution
\[
z(t)=J\!\left(\int_0^t b(s)\,ds,z(0)\right).
\]
Differentiation verifies the equation, and the Lipschitz difference inequality with integrable coefficient \(|b(t)|L_1\) proves uniqueness. Thus the scalar coordinate changes neither the original gradient flow nor its possible solutions.

When \((\phi^{(1)})'>0\), one can use
\[
F'(z)=\frac1{(\phi^{(1)})'(z)},
\qquad
J(s,z)=F^{-1}(F(z)+s).
\]
But the displacement formulation does not require
\(\mathbb E[F(Z_0^{(1)})^2]<\infty\). The rapid growth of this integral for an erf activation therefore places no restriction on its Gaussian initialization variance.

#### Global existence, uniqueness, and autonomy

For a population variable \(U\), write
\[
\|U\|_{L^2}:=\sqrt{\mathbb E[U^2]}.
\]
The operator norm is its largest amplification of this root-mean-square size. Compare two states with the same fixed first-layer roots using
\[
\begin{aligned}
d={}&
\sum_{a=1}^m
\|X_a^{(1)}-\widetilde X_a^{(1)}\|_{L^2}\\
&+\|W^{(2)}-\widetilde W^{(2)}\|_{\mathrm{op}}
+\|W^{(3)}-\widetilde W^{(3)}\|_{L^2}.
\end{aligned} \tag{8}
\]
At finite width replace every population \(L^2\) norm by the ordinary Euclidean norm divided by \(\sqrt n\); denote this distance by \(d_n\).

On sets with bounded clock \(L^2\) norms, matrix operator norms, and readout suprema, the transformed vector field is Lipschitz in (8), with a constant independent of width. The key bounds are as follows. Equation (4) controls first-activation differences, and
\[
\|H_a^{(1)}\|_{L^2}
\le
|\phi^{(1)}(0)|
+M_1\|Z_{0,a}^{(1)}\|_{L^2}
+M_1^2\|X_a^{(1)}\|_{L^2}.
\tag{9}
\]
Adding and subtracting one factor bounds the forward matrix difference. The second-layer backward difference satisfies
\[
\begin{aligned}
\|\delta_a^{(2)}-\widetilde\delta_a^{(2)}\|_{L^2}
\le{}&
\|(\phi^{(2)})'\|_\infty
\|W^{(3)}-\widetilde W^{(3)}\|_{L^2}\\
&+
\|\widetilde W^{(3)}\|_\infty
\operatorname{Lip}((\phi^{(2)})')
\|Z_a^{(2)}-\widetilde Z_a^{(2)}\|_{L^2}.
\end{aligned}
\tag{10}
\]
Its adjoint response is Lipschitz by the operator bound. The output uses boundedness and Lipschitz continuity of \(\phi^{(2)}\). Finally,
\[
\|u\otimes v-\widetilde u\otimes\widetilde v\|_{\mathrm{op}}
\le
\|u-\widetilde u\|_{L^2}\|v\|_{L^2}
+
\|\widetilde u\|_{L^2}\|v-\widetilde v\|_{L^2}.
\]
These estimates prove local existence and uniqueness by contracting the integrated equations on a short interval. A common readout supremum bound defines a closed complete set under (8), and its integral update preserves that bound after the interval is made short enough.

The chain rule and the adjoint identity give
\[
\dot f=-2Kr,
\qquad
\dot L=-4r^\top Kr\le0,
\tag{11}
\]
where
\[
K=\kappa_1K^{(1)}+\kappa_2K^{(2)}+\kappa_3K^{(3)}
\]
and
\[
\begin{aligned}
K_{ab}^{(1)}
&=\mathbf1_{\{a=b\}}\,
\mathbb E[\delta_a^{(1)}\delta_b^{(1)}],\\
K_{ab}^{(2)}
&=\mathbb E[H_a^{(1)}H_b^{(1)}]\,
  \mathbb E[\delta_a^{(2)}\delta_b^{(2)}],\\
K_{ab}^{(3)}
&=\mathbb E[H_a^{(2)}H_b^{(2)}].
\end{aligned}
\tag{12}
\]
Each block is the Gram matrix of the corresponding parameter gradients. Thus \(\|r(t)\|_2\le\|r(0)\|_2\).

Let \(B_2=\|\phi^{(2)}\|_\infty\). The readout equation yields
\[
\|W^{(3)}(t)\|_\infty
\le
\|W^{(3)}(0)\|_\infty
+
2\kappa_3B_2\sqrt m\,\|r(0)\|_2t.
\tag{13}
\]
On any prescribed finite horizon \(T\), this bounds every \(\delta_a^{(2)}\), both in mean square and in supremum. Equations (6) and (9) then give
\[
\|\dot X_a^{(1)}\|_{L^2}
\le C_T\|W^{(2)}\|_{\mathrm{op}},
\qquad
\|\dot W^{(2)}\|_{\mathrm{op}}
\le C_T\left(1+\sum_a\|X_a^{(1)}\|_{L^2}\right).
\tag{14}
\]
The fixed initial root norms are absorbed into \(C_T\). Adding and integrating these inequalities gives a linear Gronwall bound on the clock norms and matrix operator norm throughout \([0,T]\). No finite-time blow-up or loss of the bounded-state conditions is possible. The solution therefore extends uniquely to every finite horizon.

The original state is autonomous as well. At a restart time, take the current \(Z_a^{(1)}\) as the new roots in (5), set the new clocks to zero, and repeat the same argument. The original equations require only current fields and the current matrix action and adjoint. More formally, the closed spaces generated from current fields by the bounded coordinate operations and these actions contain the future integral construction. Equal current joint action laws give an isometry of these spaces that preserves the equations. Uniqueness then gives equal future action laws. Earlier clock values and the original initialization are not additional information needed for the future.

###### Identifying the population action and passing to the width limit

Use A.1 for the fixed finite value programs, jointly for both matrix orientations. The transform is continuous with at most linear growth in (clock, root). Its exponential root sensitivity is not a bounded-derivative hypothesis and no response derivative of that transform is taken. Empirical residual/contraction feedback is identified by the same-root oracle comparison below.

For clarity, the common initial action is constructed before solving the flow. Collect the finite calculations for rational meshes, their finite unions, and a countable closure under the coordinate operations and bounded continuous measurements used here. The fixed-program theorem gives consistent finite joint laws, realized on one coordinate space for each layer. Exact finite linear identities pass to these laws. A Gaussian matrix operator bound implies, with a fixed sufficiently large \(M\),
\[
\|W_0^{(2)}V\|_{L^2}
\le M\|V\|_{L^2}
\]
for every generated \(V\); the same holds for the transpose action. For example the finite bound follows from two \(1/4\)-nets and a union bound,
\[
\mathbb P\!\left(\|W_0^{(2)}\|_{\mathrm{op}}>M\right)
\le
2\,9^{2n}
\exp\!\left(-\frac{nM^2}{8\sigma_2^2}\right)
\longrightarrow0
\]
when \(\sigma_2>0\); the action is zero when \(\sigma_2=0\).
Hence the actions are well-defined on variables equal in mean square and extend to the closures of the generated spans. The finite transpose identity passes to
\[
\mathbb E[U\,W_0^{(2)}V]
=
\mathbb E[((W_0^{(2)})^*U)V].
\tag{15}
\]
This identifies the forward and backward actions as adjoints on the same two fixed spaces. It is the initial object used in (6).

For a proof mesh \(\Delta\), Euler applied to (6) has error \(O_T(\Delta)\), uniformly in width and also in the population space. The bounded vector field and its Lipschitz constant give a one-step error \(C_T\Delta^2\), so
\[
e_{k+1}\le(1+C_T\Delta)e_k+C_T\Delta^2.
\]
Summation gives the stated error. A first-exit argument keeps the clock and matrix inside slightly larger bounds; the readout supremum is controlled separately by its update, as in (13).

At fixed \(\Delta\), expand the trained matrix as its initialization plus finitely many rank-one updates. Construct the oracle using the population residuals and every population contraction in those expansions. The fixed-program theorem identifies all its joint node laws and quadratic contractions. Applying its proxy matrix to an oracle vector differs from the prescribed node by finitely many terms of the form
\[
-2\kappa_2\Delta r_{b,s}\,
\delta_{b,s,\mathrm{oracle}}^{(2)}
\left[
\frac{
(h_{b,s,\mathrm{oracle}}^{(1)})^\top
h_{a,k,\mathrm{oracle}}^{(1)}
}{n}
-
\mathbb E[H_{b,s}^{(1)}H_{a,k}^{(1)}]
\right].
\tag{16}
\]
Each scalar discrepancy vanishes and each vector has bounded root-mean-square norm. The corresponding transpose discrepancies use contractions of two second-layer backward fields. Thus recomputed proxy quantities approach the oracle nodes.

The state estimate (8) transfers this identification to finite Euler with empirical feedback. All factors involving the readout can be clipped beyond its proven supremum bound without changing any oracle value. For comparisons the roots stay fixed: \(J\) and its first activation are uniformly Lipschitz in their changing clock arguments. A joint global Lipschitz bound in the frozen root is neither asserted nor needed.

Consequently, taking \(n\to\infty\) at fixed \(\Delta\), and then \(\Delta\to0\), proves the population limit of the finite continuous flow on every \([0,T]\).

#### The bridge from exact GD

A scalar estimate makes the discrete argument work even when the first derivative vanishes or changes sign. In the following calculation only, write
\[
A=(\phi^{(1)})',
\qquad L=\operatorname{Lip}(A),
\qquad
z^+=z+\eta A(z)b.
\]
If \(L\eta|b|\le1/2\) and \(A(z)\ne0\), then for \(0\le s\le1\),
\[
|A(z+s\eta A(z)b)-A(z)|
\le L\eta|A(z)b|
\le \frac{|A(z)|}{2}.
\]
The whole segment stays in the same interval where \(A\ne0\). Define its exact scalar-flow clock increment by
\[
\Delta X=\int_z^{z^+}\frac{du}{A(u)}.
\]
Then \(z^+=J(\Delta X,z)\). Substitution in the integral gives
\[
\begin{aligned}
|\Delta X-\eta b|
&\le
\eta|b|\int_0^1
\left|
\frac{A(z)}{A(z+s\eta A(z)b)}-1
\right|\,ds\\
&\le L\eta^2b^2.
\end{aligned} \tag{17}
\]
If \(A(z)=0\), the raw step fixes \(z\). Set \(\Delta X=\eta b\); the same exact representation holds because \(J(s,z)=z\) at an equilibrium. If \(L=0\), the derivative is constant and there is no coordinate defect or step restriction.

Apply (17) to each coordinate with
\[
b_a
=
-2\kappa_1r_{n,a}
(W^{(2)})^\top\delta_a^{(2)}.
\tag{18}
\]
The raw GD trajectories themselves have width-independent bounds on \([0,T]\). First,
\[
|r_{n,a}|
\le |y_a|+B_2\|W^{(3)}\|_\infty
\]
and the readout update give a discrete Gronwall bound on its supremum. This bounds \(\delta_a^{(2)}\). The first raw update then has root-mean-square increment at most \(C_T\eta_n\|W^{(2)}\|_{\mathrm{op}}\), while the matrix operator increment is at most
\[
C_T\eta_n
\left(
1+\sum_a\frac{\|z_a^{(1)}\|_2}{\sqrt n}
\right).
\]
Adding these bounds gives a second discrete linear Gronwall estimate. The initial root RMS and matrix operator norm are bounded with probability tending to one, and the allowed readout initializations have the requisite high-probability uniform supremum bound. On these events,
\[
\frac{\|b_a\|_2}{\sqrt n}\le C_T,
\qquad
\|b_a\|_\infty\le C_T\sqrt n.
\tag{19}
\]
Thus \(\eta_n\sqrt n\to0\) enforces the scalar step condition throughout the interval.

Lift the raw iterates recursively by these exact clock increments, starting from \(x_{a,0}^{(1)}=0\). The scalar flow identity ensures
\[
z_{a,k}^{(1)}
=
J(x_{a,k}^{(1)},z_{a,0}^{(1)})
\]
exactly at every step. The lifted first update differs from transformed Euler by at most
\[
\begin{aligned}
L\eta_n^2
\left(\frac1n\sum_i b_{a,i}^4\right)^{1/2}
&\le
L\eta_n^2\|b_a\|_\infty
\frac{\|b_a\|_2}{\sqrt n}\\
&\le C_T\eta_n^2\sqrt n
\end{aligned}
\tag{20}
\]
in root-mean-square norm.

It is important that the clocks themselves stay in the common Lipschitz region, including when \(J\) has equilibria and cannot be inverted. Summing their exact increments gives
\[
\begin{aligned}
\frac{\|x_{a,k}^{(1)}\|_2}{\sqrt n}
&\le
\sum_{j<k}
\left[
\eta_n\frac{\|b_{a,j}\|_2}{\sqrt n}
+
L\eta_n^2\|b_{a,j}\|_\infty
\frac{\|b_{a,j}\|_2}{\sqrt n}
\right]\\
&\le C_T(1+\eta_n\sqrt n),
\qquad k\eta_n\le T.
\end{aligned}
\tag{21}
\]
Thus the transformed stability constant remains width-independent.

The other parameter updates are already Euler updates for (6). Add their ordinary \(O_T(\eta_n^2)\) local flow error and sum the stable recurrence:
\[
\sup_{t\le T}
d_n\!\left(
\text{lifted GD}(t),\text{finite flow}(t)
\right)
\le
C_T(\eta_n+\eta_n\sqrt n).
\tag{22}
\]
At interpolation times, the scalar flow segment and the linear raw segment differ by the same vanishing bound; the state movement inside one step is \(O_T(\eta_n)\). This proves the raw GD bridge without a moment assumption on an unshifted scalar transform.

Combining (22), the fixed-mesh oracle limit, and the two \(O_T(\Delta)\) mesh errors proves the joint width/step conclusion.

For the remaining quadratic measurements, the backward fields
\[
(W^{(2)}(t))^*\delta_a^{(2)}(t)
\]
form a compact time-indexed family in \(L^2\). Their squared tails therefore vanish uniformly as the clipping threshold grows. Clip before multiplying by \((\phi^{(1)})'(Z_a^{(1)})\), pass the resulting bounded Lipschitz measurements through the proved limit, and remove clipping. Fixed-grid second-moment convergence and state continuity give the corresponding finite empirical tail control. This supplies kernel entries and squared hidden velocities without assuming sub-Gaussian tails.

For completeness, uniform velocity-energy bounds also supply the path-law assertion. For a time grid of spacing \(h\), let \(\pi_h t\) be its preceding grid point. Cauchy–Schwarz on each coordinate gives
\[
\frac1n\sum_i
\sup_{t\le T}
|z_i(t)-z_i(\pi_h t)|^2
\le
h\int_0^T
\frac{\|\dot z(t)\|_2^2}{n}\,dt.
\tag{23}
\]
The population counterpart replaces the empirical average by expectation. The parameter bounds above and the bounded activation derivatives bound these integrals uniformly for each hidden layer. Piecewise-linear reconstruction from the same grid satisfies an analogous estimate with a fixed additional factor. At fixed grid size the joint laws converge with second moments; letting \(h\to0\) gives convergence of the hidden path laws with their second moments in the uniform path norm. The clipped backward-field argument likewise identifies the integrated squared speeds.

#### Examples and the input-geometry boundary

Either layer may use arctan, tanh, logistic sigmoid, erf with fixed nonzero input scaling, softsign \(z/(1+|z|)\), or the smooth saturation \(z/\sqrt{1+z^2}\). Sine and cosine also qualify, despite derivative zeros and sign changes. Softsign is not twice continuously differentiable at zero, but
\[
\frac{d}{dz}\frac{z}{1+|z|}
=
\frac1{(1+|z|)^2}
\]
is continuous, bounded, and globally Lipschitz, which is enough.

In the first layer only, affine functions, softplus, GELU, and SiLU also qualify: their derivatives are bounded and globally Lipschitz although the activations are unbounded. ReLU, leaky ReLU, hard tanh, and derivative-jump activations are not covered by this theorem.

For a general input Gram matrix
\[
G_{ab}=\frac{x_a^\top x_b}{d},
\]
the first-layer equation becomes
\[
\dot Z_a^{(1)}
=
-2\kappa_1\sum_b
G_{ab}r_b
(\phi^{(1)})'(Z_b^{(1)})
(W^{(2)})^*\delta_b^{(2)}.
\tag{24}
\]
With a nonlinear first activation, the right side is not the \(a\)-th activation derivative times one scalar backward coefficient. The scalar-coordinate proof therefore does not give a global-time arbitrary-angle theorem.

There is a verified exception. If
\[
\phi^{(1)}(z)=cz+d_0,
\]
then
\[
\dot Z_a^{(1)}
=
-2\kappa_1c\sum_b
G_{ab}r_b(W^{(2)})^*\delta_b^{(2)}.
\tag{25}
\]
The troublesome multiplication by a varying first-layer derivative has disappeared. In the raw state
\((Z_1^{(1)},\ldots,Z_m^{(1)},W^{(2)},W^{(3)})\),
the vector field is Lipschitz on the same bounded sets. The bounds (13)–(14) hold with raw first-layer norms and constants depending on the fixed \(G\). The fixed-program initialization allows the possibly singular Gaussian covariance \(\sigma_1^2G\). The same oracle and mesh proof therefore gives a global population limit for **any fixed finite normalized input configuration**, including singular Gram matrices.

In this affine case, raw GD is already ordinary Euler for the Lipschitz raw vector field, so the sufficient step condition improves to \(\eta_n\to0\). All the preceding readout restrictions remain. This exception does not give a nonlinear first layer: its best affine-fit error is exactly zero.

## C. A local fixed-depth theorem and strict Gaussian activity

The local theorem permits subGaussian first weights and readout, arbitrary fixed data, zero middle variances and frozen blocks as stated. The separate strict-activity corollary requires Gaussian first weights, positive variances and mobilities, zero population readout, nonzero labels and pairwise nonparallel unit inputs. These are additional hypotheses of that corollary.

For fixed C2 Euler programs, A.1–A.2 prove their value and named-source response formulas. Direct iid subGaussian tuples are roots. No Gaussian quantile representation is needed. The response estimates below are uniform over meshes; this uniformity is proved separately from the fixed-program result. Mollification then gives C1,1 activations.

For squared loss, the theorem for every deterministic vanishing GD mesh also gives finite GF: for each fixed width, smooth finite-dimensional Euler convergence allows a deterministic mesh smaller than 1/n with probability of GF/GD discrepancy exceeding 1/n smaller than 1/n. Apply the every-mesh theorem to this diagonal sequence. The finite squared-loss flow exists globally: at fixed width, energy controls its Euclidean parameter length on every finite interval, even with frozen blocks, and its locally Lipschitz field extends from a finite endpoint. The diagonal yields the same local population GF limit, in exactly the observable topologies C.1 states. For the separate general separable-loss extension, use the preliminary local ball on its high-probability initialization event, with stopping outside that event; no global finite-GF claim follows for a loss unbounded below.

### C.1. Local fixed-depth C1,1 theorem

Within this proof unit, unqualified section and equation numbers are local.

#### Statement and exact finite model

Fix integers d,m and L>=2. There are L hidden layers, each of width n. The m
inputs x_a in R^d are fixed, with ||x_a||_2/sqrt(d)<=X and
G_ab=x_a^top x_b/d. Their Gram matrix may be singular and inputs may coincide.
For squared loss assume |y_a|<=Y. Choose positive weights omega_a with
sum_a omega_a=1 and use

    L_n = sum_a omega_a (f_n,a-y_a)^2,       r_n,a=f_n,a-y_a.

This declares a change from summed loss. For summed loss on m examples, the
same statement applies after multiplying physical time by m.

Each activation phi^(ell):R->R is C^1, with bounded derivative and globally
Lipschitz derivative. Fix common finite bounds

    |phi^(ell)(0)|<=D0,
    |phi^(ell)'(s)|<=D1,
    |phi^(ell)'(s)-phi^(ell)'(t)|<=D2 |s-t|.

The activations themselves need not be bounded. In particular their growth is
at most linear. Nonaffinity is not required for existence.

Concrete examples include arctan, tanh, logistic sigmoid, softplus, exact GELU,
and SiLU, with different choices in different layers. For softplus,
phi'=s and phi''=s(1-s), where s is the logistic sigmoid evaluated at the
argument. For exact GELU phi(t)=t Phi(t),
phi'(t)=Phi(t)+t varphi(t) and phi''(t)=(2-t^2)varphi(t), where Phi and
varphi are the standard normal distribution function and density. For SiLU,
phi(t)=t s(t), phi'(t)=s(t)+t s(t)(1-s(t)) and
phi''(t)=2s(t)(1-s(t))+t s(t)(1-s(t))(1-2s(t)). These derivatives are bounded
because Gaussian and logistic tails dominate the displayed polynomial
factors. The C1,1 class also contains a quadratic smoothing of ReLU: zero for
t<=0, t^2/2 for 0<=t<=1, and t-1/2 for t>=1. Its derivative is bounded and
1-Lipschitz although its second derivative does not exist at both junctions.

For the principal initialization take independent Gaussian first weights
W^(1)_0,ij~N(0,sigma_1^2), independent middle matrices
W^(ell)_0,ji~N(0,sigma_ell^2/n), 2<=ell<=L, and independent readout entries
W^(L+1)_0,j distributed as a fixed random variable with

    sup_(p>=2) (E|W^(L+1)_0,j|^p)^(1/p)/sqrt(p) <= B_out < infinity.

Zero, bounded, and nonvanishing Gaussian readout are all allowed. The first
weights may more generally be iid centered subGaussian variables, with a fixed
subGaussian bound B_in. This extension is justified below; the strict-activity
corollary will use Gaussian first weights. All initialization groups are
independent. Sigma values may be zero in the existence theorem.

Define, with coordinatewise activation,

    z^(1)_a=W^(1)x_a/sqrt(d),       h^(1)_a=phi^(1)(z^(1)_a),
    z^(ell)_a=W^(ell)h^(ell-1)_a,  h^(ell)_a=phi^(ell)(z^(ell)_a), 2<=ell<=L,
    f_n,a=(W^(L+1))^top h^(L)_a/n.

W^(L+1) is always the stored rescaled readout. In particular, for L=2 it is
W^(3), and f_n,a=(W^(3))^top h^(2)_a/n.

The backpropagated fields omit the loss derivative:

    delta^(L)_a=W^(L+1) phi^(L)'(z^(L)_a),
    delta^(ell)_a=phi^(ell)'(z^(ell)_a)
                       [(W^(ell+1))^top delta^(ell+1)_a], ell<L.

Thus delta^(ell)_a=n partial f_n,a/partial z^(ell)_a. Choose fixed finite
kappa_ell>=0. Stored-weight gradient-descent rates are

    eta_n (n kappa_1, kappa_2, ..., kappa_L, n kappa_(L+1)).

The exact updates are

    W^(1)_(k+1)=W^(1)_k
        -(2 eta_n kappa_1/sqrt(d)) sum_b omega_b r_n,b,k delta^(1)_b,k x_b^top,
    z^(1)_a,k+1=z^(1)_a,k
        -2 eta_n kappa_1 sum_b omega_b G_ab r_n,b,k delta^(1)_b,k,
    W^(ell)_(k+1)=W^(ell)_k
        -(2 eta_n kappa_ell/n) sum_b omega_b r_n,b,k
                             delta^(ell)_b,k (h^(ell-1)_b,k)^top, 2<=ell<=L,
    W^(L+1)_(k+1)=W^(L+1)_k
        -2 eta_n kappa_(L+1) sum_b omega_b r_n,b,k h^(L)_b,k.                 (1)

Use physical time t=k eta_n, interpolate these parameters linearly, and
recompute forward quantities between grid points.

There is T_*>0 depending only on L, X, Y, D0,D1,D2, the initialization bounds
and the kappa values, such that for EVERY eta_n>0 tending to zero the following
conclusions hold on [0,T_*]:

1. A unique strong population flow exists in the field/operator state described
   below. It is autonomous and retains each matrix together with its adjoint.
2. Predictions, loss, and all kernel entries converge in probability uniformly
   in time to their population values.
3. Separately for each neuron population, empirical laws of the joint m-input
   hidden paths converge in Wasserstein distance of order two for the uniform
   path norm. This applies to both preactivations and activations.
4. Integrated squared hidden speeds converge. Fixed finite, correctly typed
   forward/adjoint probes assembled from Lipschitz coordinate maps, linear
   combinations, and products of a bounded factor and an L2 field also have
   their joint continuous quadratic-growth measurements converge, provided
   the bounded factors are continuous functions of their arguments.

The constants do not depend on n, eta_n, m, d, or a smallest Gram eigenvalue
when the stated bounds remain fixed. Here m,d and the inputs are nevertheless
fixed in the convergence assertion: no uniform convergence rate for growing
datasets or dimension is claimed. Probe length is fixed; arbitrary products of
two unbounded factors are not part of the probe assertion.

#### Population state, construction, and preliminary norm bounds

There is a separate probability space for coordinates in each hidden layer.
The field Z^(1)_a belongs to the first, W^(L+1) to the last. For 2<=ell<=L,
W^(ell) is a bounded linear map from the mean-square space at layer ell-1 to
the one at layer ell. Its adjoint is denoted (W^(ell))^*. Expectations pair
variables belonging to the same population. Define

    (u tensor v)V = u E[v V].

This is the population version of the finite map u v^top/n. The population
forward and backward formulas are those above with uppercase Z,H, expectation
in place of b^top c/n, and * in place of top. In particular

    f_a=E[W^(L+1) H^(L)_a],
    P^(L)_a=W^(L+1),
    P^(ell)_a=(W^(ell+1))^* delta^(ell+1)_a, ell<L,
    delta^(ell)_a=phi^(ell)'(Z^(ell)_a) P^(ell)_a.

The limiting equations are

    dot Z^(1)_a=-2 kappa_1 sum_b omega_b G_ab r_b delta^(1)_b,
    dot W^(ell)=-2 kappa_ell sum_b omega_b r_b
                                  delta^(ell)_b tensor H^(ell-1)_b, 2<=ell<=L,
    dot W^(L+1)=-2 kappa_(L+1) sum_b omega_b r_b H^(L)_b.                    (2)

A strong solution means these integral equations hold in L2 for the fields
and in operator norm for the matrices, continuously in time. The initial first
roots have the law of (W^(1)_0 x_a/sqrt(d))_a for a single row. For Gaussian
weights this is N(0,sigma_1^2 G). The initial operators are constructed from
the joint matrix/transpose limits, not replaced by independent backward maps.

Centered independent subGaussian first entries have uniformly subGaussian projections:
their moment bounds give E exp(t W_ij)<=exp(C B_in^2 t^2); independence then
gives E exp(t sum_j u_j W_ij)<=exp(C B_in^2 t^2 sum_j u_j^2).
Thus each initial Z^(1)_a has a marginal subGaussian bound depending only on
B_in X. No assumption of iid neuron coordinates after matrix reuse is made.

To obtain common spaces for different meshes, take the countable union of the
programs for rational meshes, their finite unions, rational linear
combinations and the coordinate operations needed here (including clipped
products). Their laws are consistent under deletion of instructions. Realize
these countably many laws jointly on each population and take the L2 closure
of the resulting fields. Operator inequalities pass from finite width to each
finite collection. Indeed a 1/4-net in each unit sphere gives

    P(||W^(ell)_0||_op>M)
       <=2*9^(2n)*exp[-n M^2/(8 sigma_ell^2)] -> 0                       (3)

for a sufficiently large fixed M (zero variance needs no bound). Since
||W^(ell)_0 v||_2/sqrt(n)<=M ||v||_2/sqrt(n), second-moment convergence gives
||W^(ell)_0 V||_L2<=M||V||_L2 on the generated span, hence on its closure.
The same argument gives the transpose map. The exact finite adjunction
identity passes to the limit and identifies it with the adjoint. Coordinate
operations extend wherever needed by clipping and L2 limits.

For the following fixed-computation response statements use A.1–A.2, with arbitrary iid subGaussian tuples admitted directly as roots.
For two states on these same spaces use the distance

    d(theta,theta_tilde)=max_a ||Z^(1)_a-Ztilde^(1)_a||_L2
       +sum_(ell=2)^L ||W^(ell)-Wtilde^(ell)||_op
       +||W^(L+1)-Wtilde^(L+1)||_L2.                                    (4)

At finite width replace every field L2 norm by ||b||_2/sqrt(n). No operator
distance between a finite matrix and a population operator is asserted.

Here is an explicit preliminary interval on which these norms stay bounded.
Let S be the maximum of the individual norms entering the state (not the
distance). Choose S0 so the initial norms are <=S0 with probability tending to
one, uniformly in the bound parameters, and are <=S0 in the population.
First-weight concentration is needed only over fixed m. Set B=2S0+2 and

    h_1=D0+D1 B,       h_ell=D0+D1 B h_(ell-1),
    d_ell=D1^(L-ell+1) B^(L-ell+1),
    R0=B h_L+Y.

On S<=B, all ||H^(ell)_a||_L2<=h_ell, ||delta^(ell)_a||_L2<=d_ell,
and |r_a|<=R0. The same inequalities hold at finite width. The norm of each
state velocity is therefore bounded by the corresponding member of

    2 kappa_1 X^2 R0 d_1,
    2 kappa_ell R0 d_ell h_(ell-1) (2<=ell<=L),
    2 kappa_(L+1) R0 h_L.

Let V0>=1 bound their sum. On

    T_ball=min(1,(B-S0)/(4 V0)),                                       (5)

Euler trajectories with mesh <=T_ball remain in S<=B through time 2 T_ball:
up to the first possible exit the cumulative increment is at most 2T_ball V0,
strictly less than B-S0. The same first-exit argument works for integral
solutions. It also bounds interpolation speeds, with a constant depending on
L. This requires only operator and RMS bounds, including for the readout.

#### The additional estimate uniform in the time mesh

The fixed-depth response lemma in Fragment C.2 derives,
on a further interval T_response>0, for every population Euler mesh Delta,

    sup_(k Delta<=T_response) max_(a,ell)
          E exp(c |P^(ell)_a,k|^2) <= C.                                (6)

It proves this for unbounded activations as well as nonvanishing subGaussian
readout. Its precise recurrences and noncircular choice of constants are part
of this proof, not an additional hypothesis of the theorem.

The important bounds in that derivation are entrywise response coefficients
|C^(ell)_(ak,bs)|<=c_ell Delta omega_b and bounded row sums of A^(ell).
SubGaussian norms of the forward fields and backward fields are bootstrapped
together. A derivative in a single backward slot starts with a pulse carrying
Delta omega_b. Every later random growth coefficient appears in a weighted
time sum Delta sum_(s,b) omega_b |P^(ell)_b,s|. Jensen's inequality bounds its
exponential using marginal subGaussian estimates; independence over time is
not assumed and no maximum of Gaussian fields over the mesh is taken.

Set T_*<=min(T_ball,T_response), with any additional reductions specified in
the lemma. The constants are functions of the displayed bounds only. In
particular they do not contain Delta or m.

#### Localization, existence, and uniqueness

Forward fields and predictions are Lipschitz in (4) on the ball S<=B, with
a constant depending on fixed depth and bound parameters. This follows by
expanding W H-Wtilde Htilde=(W-Wtilde)H+Wtilde(H-Htilde), and using
||phi(Z)-phi(Ztilde)||_L2<=D1||Z-Ztilde||_L2.

Backward fields require a cutoff. For any reference field Ptilde,

    ||[phi'(Z)-phi'(Ztilde)] Ptilde||_L2
       <=D2 R ||Z-Ztilde||_L2
           +2D1 ||Ptilde 1_(|Ptilde|>R)||_L2.                            (7)

Write a delta difference as

    phi'(Z)(P-Ptilde)+[phi'(Z)-phi'(Ztilde)]Ptilde.

For ell<L the difference P^(ell)-Ptilde^(ell) is bounded by
B||delta^(ell+1)-deltatilde^(ell+1)||_L2+C d; at ell=L it is a readout
difference. Downward substitution yields

    max_(a,ell)||delta^(ell)_a-deltatilde^(ell)_a||_L2
       <=C(1+R)d+C sum_(ell=1)^L max_a
                  ||Ptilde^(ell)_a 1_(|Ptilde^(ell)_a|>R)||_L2.

Each backward step multiplies the previous difference only by bounded
activation derivatives and bounded operators. The new cutoff term is added;
there is no power R^L. Outer-product differences satisfy
||u tensor v-utilde tensor vtilde||_op
 <=||u-utilde||_L2 ||v||_L2+||utilde||_L2 ||v-vtilde||_L2.
Together with (6), this proves for the vector field in (2)

    ||F(theta)-F(theta_reference)||
       <=C(1+R)d(theta,theta_reference)+C exp(-c R^2),                    (8)

when the reference is a population Euler grid state. Only the reference needs
the tail estimate.

Compare two piecewise linear population Euler interpolants. At time t their
assigned velocities are F evaluated at their respective preceding grid
states. These states differ by at most their interpolant distance plus
C(Delta+Delta'). Apply (8) directly to these grid states and integrate:

    sup_(t<=T_*) d(theta^Delta(t),theta^Delta'(t))
       <=C exp[C(1+R)T_*]
           ((1+R)(Delta+Delta')+exp(-cR^2)).                             (9)

First fix R and send both meshes to zero; then send R to infinity. Since
exp(CRT_*-cR^2)->0, the paths are Cauchy in the complete field/operator spaces.

All coordinate products occurring in F are continuous on these spaces.
For the only subtle product, if Z_j->Z and P_j->P in L2, split
phi'(Z_j)P_j-phi'(Z)P into the bounded multiplier times P_j-P and
[phi'(Z_j)-phi'(Z)]P. The latter converges in L2 by convergence in probability,
boundedness of phi', and uniform integrability against the single integrable
variable P^2. Thus F is continuous; on the compact range of a convergent
sequence of continuous paths this continuity is uniform. The Euler integral
equations pass to (2), giving a strong solution. All P fields converge at
fixed times; Fatou transfers (6) to the solution uniformly in time.

For any other strong solution with the same initial state, (5) bounds its
norms on this interval. Apply (8) with the constructed solution as reference.
Their distance is <=C exp(CRT_*-cR^2) for every R, hence zero. This proves
uniqueness without assuming tails of the competing solution.

Equations (2) use only the current fields, operators, and adjoints. More
precisely, the closed spaces generated by a current state under these
operations and clipped products contain all its subsequent Euler
approximations and their limits. Equal current joint action laws identify
these spaces by an L2 isometry intertwining the operators and coordinate
operations. Uniqueness identifies their subsequent laws. This is autonomy
and restartability on the constructed interval, not a finite scalar closure.

#### From the population flow to every vanishing-step finite GD sequence

Fix a rational coarse mesh Delta, independently of eta_n. Expand

    W^(ell)_k=W^(ell)_0-2 kappa_ell Delta
          sum_(s<k,b) omega_b r_b,s delta^(ell)_b,s tensor H^(ell-1)_b,s.   (10)

Build a finite oracle computation using the same sampled initial arrays as
actual GD. In its expanded matrix actions replace all scalar contractions
and residuals by their deterministic population Euler values. This is a
fixed finite program, so the stated theorem gives joint empirical convergence
of every needed node, contraction, second moment, and continuous quadratic
tail cutoff. Its coefficients are a proof device determined by the population
Euler equations; they are not the coefficients of the final autonomous flow.

Construct proxy parameters from the oracle's first-layer/readout nodes and
the finite rank expansion corresponding to (10), with u v^top/n. Applying a
proxy matrix to an oracle node differs from its prescribed oracle action by
finitely many terms of the form

    -2 kappa_ell Delta omega_b r_b,s delta^(ell)_b,s,oracle
       ((h^(ell-1)_b,s,oracle)^top h^(ell-1)_a,k,oracle/n
                         -E[H^(ell-1)_b,s H^(ell-1)_a,k]),               (11)

and transpose actions have the corresponding delta contractions. At fixed
Delta, their scalar errors vanish and their vector RMS norms are bounded.
Consequently all proxy forward quantities are consistent in RMS. To transfer
backpropagation with an unbounded readout, use (7) against oracle P nodes and
proceed downward through layers. At any fixed cutoff the errors vanish, and
the empirical oracle tails converge to the tails in (6); sending that cutoff
to infinity proves the recomputed proxy delta fields are consistent in RMS.
This also proves consistency of its vector field and residuals.

The proxy grid fields therefore have reference tails with limiting upper
bound C exp(-cR^2), after harmless changes in constants. For example if
||v-u||_2/sqrt(n)=e_n then

    ||v 1_(|v|>2R)||_2/sqrt(n)
       <=2 e_n+2||u 1_(|u|>R)||_2/sqrt(n).

Its grid and interpolated norm/speed bounds have limiting upper bounds
independent of Delta, by (5), (10), and the fixed-mesh consistency. Enlarge
the comparison ball by a fixed amount if necessary.

Compare actual GD and the proxy interpolant using their assigned grid
velocities. The actual preceding fine-grid state and reference preceding
coarse-grid state are at distance at most the interpolant distance plus
C(eta_n+Delta). The actual-to-proxy vector-field difference obeys (8), now
with empirical reference tails and fixed-mesh errors. Thus

    sup_(t<=T_*) d_n(theta_n^GD(t),theta_n^proxy,Delta(t))
       <=C exp[C(1+R)T_*]
          ((1+R)(eta_n+Delta)+exp(-cR^2)+o_P(1)).                         (12)

Here o_P(1) is at fixed R,Delta. Initial distance is zero because the oracle
uses the same roots. A vanishing initialization perturbation contributes its
distance to the right side. The actual GD requires only its RMS/operator
ball, not a maximum coordinate bound or an empirical tail theorem for a
growing number of steps.

The limit order is: n->infinity with R,Delta fixed, then Delta->0, then
R->infinity. Equation (12), (9), and fixed-mesh empirical convergence prove
the joint width/step limit. There is no condition such as eta_n sqrt(n)->0.

Predictions follow by the forward Lipschitz bound. Define the kernel blocks

    K^(1)_ab=G_ab E[delta^(1)_a delta^(1)_b],
    K^(ell)_ab=E[H^(ell-1)_a H^(ell-1)_b]
                      E[delta^(ell)_a delta^(ell)_b], 2<=ell<=L,
    K^(L+1)_ab=E[H^(L)_a H^(L)_b],
    K=sum_(ell=1)^(L+1) kappa_ell K^(ell).

Their finite counterparts use b^top c/n in every contraction. Backward RMS
consistency and Cauchy--Schwarz give uniform convergence of these entries.
For Omega=diag(omega_1,...,omega_m), direct differentiation gives

    dot f=-2 K Omega r,        dot L=-4 (Omega r)^top K (Omega r).         (13)

Each block is positive semidefinite, being a parameter-gradient Gram matrix.

For completeness, the extra observable steps do not demand higher moments
of actual GD. The population parameter velocities converge uniformly in L2
and operator norm by (8). Recursively,

    dot Z^(ell)_a=dot W^(ell) H^(ell-1)_a
                    +W^(ell)[phi^(ell-1)'(Z^(ell-1)_a) dot Z^(ell-1)_a]   (14)

is continuous in the state and parameter velocity in the stated norms.
The bounded-multiplier product is justified by the same fixed-reference
uniform-integrability argument used after (9). On the compact population
time path these velocities form a compact L2 family, hence have uniformly
vanishing L2 tails. For each fixed Delta, oracle evaluations of these
velocities are fixed finite programs and have convergent empirical cutoff
moments. Localizing their bounded-multiplier products, first using (12),
then passing Delta to zero, proves convergence of the integrated squared
hidden speeds. No exponential estimate for these derived velocities is
needed; cutoffs here occur after state stability, outside Gronwall.

At any grid with cell length at most epsilon, each absolutely continuous
coordinate path obeys

    sup_(s,t in one cell)|z(t)-z(s)|^2
         <=epsilon integral_cell |dot z(u)|^2 du.

After averaging over neurons and summing over cells, the error of grid
reconstruction in squared uniform path norm is <=C epsilon, uniformly in n
on the ball. Fixed-time empirical joint laws converge in Wasserstein distance
of order two by fixed-program convergence and their second moments. Combining
this with grid reconstruction proves assertion 3. Activations follow from
their Lipschitz bounds. The same cutoff induction proves assertion 4: an
operator amplifies L2 errors by at most B, Lipschitz functions preserve them,
and bounded-factor products use the compact reference L2 family's uniform
integrability. This explains the stated restriction on products.

#### Removing second differentiability; losses and initialization perturbations

First the proof above is for C2 activations with bounded first two
derivatives. For a C1 activation whose derivative is globally Lipschitz,
convolve with a smooth compactly supported probability density of scale
epsilon. Then

    ||phi_epsilon-phi||_infinity<=C D1 epsilon,
    ||phi_epsilon'-phi'||_infinity<=C D2 epsilon,
    ||phi_epsilon'||_infinity<=D1,    ||phi_epsilon''||_infinity<=D2.

The response lemma and T_* depend only on these bounds, uniformly in
epsilon. Include rational smoothing scales in the common program family.
The comparison (8) between different smoothings has an additional
C(1+R)(epsilon+epsilon') term: forward differences gain O(epsilon), and
backward differences use (7) plus the uniform difference of derivatives.
The same ordered limits construct a strong flow for the original activation,
inherit (6), and prove uniqueness. Compare finite GD for the original
activation with the fixed smooth oracle by the identical estimate, adding
C(1+R)epsilon inside (12). Taking n,Delta,epsilon,R in that order proves the
same joint limit for C1,1 activations. ReLU's discontinuous derivative does
not satisfy this argument.

More general separable losses are allowed: use sum_a omega_a ell_a(f_a),
where every ell_a is C1 and its derivative is locally Lipschitz, with common
finite bounds and Lipschitz constants on bounded prediction intervals.
Replace every 2r_b in (1),(2),(10)--(12) by ell_b'(f_b). The preliminary ball
uses sup_(a,|f|<=B h_L)|ell_a'(f)| in place of 2R0; prediction stability uses
the corresponding local Lipschitz constant. In response differentiation these
oracle coefficients are frozen, so every response estimate uses only their
bound and the pulse still carries Delta omega_b. The proof is unchanged
with exactly these replacements. No convexity or global growth assumption
on the loss is required on this short interval. For this loss,
dot f_a=-sum_b K_ab omega_b ell_b'(f_b), and
dot L=-sum_ab omega_a ell_a'(f_a) K_ab omega_b ell_b'(f_b).

Finally (12) also allows perturbing the sampled initial arrays by an amount
tending to zero in probability in (4), and changing the kappa constants by
vanishing amounts. The actual initial arrays need only the resulting RMS
and operator bounds. In particular zero population readout covers finite
Gaussian readout sigma_out n^(-beta) g for EVERY beta>0, and indeed any
readout perturbation with ||W^(L+1)_0||_2/sqrt(n)->0 in probability. This
does not assert universality for different O(1) non-Gaussian middle matrices:
such a replacement need not be small in operator norm.

### C.2. Complete weighted response and tail proof

Within this proof unit, unqualified section and equation numbers are local.

Fix a finite number \(L\ge2\) of hidden layers and a finite dataset with
weights \(\omega_a>0\), \(\sum_a\omega_a=1\). Suppose
\(|G_{ab}|\le g\). No inverse Gram matrix is used. Each activation
\(\phi^{(\ell)}\) is \(C^2\), with

\[
\max_\ell\bigl(|\phi^{(\ell)}(0)|+
\|\phi^{(\ell)\prime}\|_\infty+
\|\phi^{(\ell)\prime\prime}\|_\infty\bigr)<\infty.
\]

The first-layer root vector has uniformly subGaussian scalar marginals.
The readout root \(W_0^{(L+1)}\) is subGaussian. Roots and initial middle
matrices are independent, and the middle matrices have independent
Gaussian entries with variance \(\sigma_\ell^2/n\).
The lemma below only uses the marginal subGaussian bounds on the resulting
first preactivations and readout.

All constants are independent of the Euler mesh, the number of mesh points,
the number of inputs, the individual weights, and covariance ranks. They
can depend on fixed depth, activation bounds, \(g\), initialization bounds,
learning constants, and the preliminary RMS/residual bounds. A common
existence time across datasets does not imply a width limit for a dataset
whose size increases with width.

#### Exact recursions and hypotheses

For mesh \(\Delta\), write the population forward and backward operations
as

\[
H_{a,k}^{(\ell)}=\phi^{(\ell)}(Z_{a,k}^{(\ell)}),\qquad
P_{a,k}^{(L)}=W_k^{(L+1)},\qquad
\delta_{a,k}^{(\ell)}=
\phi^{(\ell)\prime}(Z_{a,k}^{(\ell)})P_{a,k}^{(\ell)}.
\tag{1}
\]

For \(\ell<L\), \(P_{a,k}^{(\ell)}=
(W_k^{(\ell+1)})^*\delta_{a,k}^{(\ell+1)}\). The Euler updates at the
two ends are

\[
Z_{a,k+1}^{(1)}=Z_{a,k}^{(1)}
-2\kappa_1\Delta\sum_b\omega_bG_{ab}r_{b,k}
\delta_{b,k}^{(1)},
\tag{2}
\]
\[
W_{k+1}^{(L+1)}=W_k^{(L+1)}
-2\kappa_{L+1}\Delta\sum_b\omega_b r_{b,k}H_{b,k}^{(L)}.
\tag{3}
\]

For every middle layer the update is

\[
W_{k+1}^{(\ell)}=W_k^{(\ell)}
-2\kappa_\ell\Delta\sum_b\omega_b r_{b,k}
\delta_{b,k}^{(\ell)}\otimes H_{b,k}^{(\ell-1)}.
\tag{4}
\]

For the lemma, the residuals in these recursions can be any deterministic
numbers with \(|r_{a,k}|\le R\). All deterministic residuals, contractions,
response coefficients, and Gaussian covariance laws are frozen in every
derivative below. There is no derivative through expectations.

Assume on a preliminary time interval \([0,T_{\rm ball}]\) that all source
RMS norms \(\|H_{a,k}^{(\ell)}\|_{L^2}\) and
\(\|\delta_{a,k}^{(\ell)}\|_{L^2}\) are at most \(S\), uniformly in mesh.
In particular the training-memory coefficient bound is

\[
J=2\max_\ell\kappa_\ell R S^2,
\tag{5}
\]

and all Gaussian innovations below have standard deviations at most
\(S\max_\ell\sigma_\ell\).

For each initial middle matrix introduce forward slots
\(\xi_{a,k}^{(\ell)}\) and backward slots
\(\eta_{a,k}^{(\ell)}\). Their covariances are

\[
\mathbb E[\xi_{a,k}^{(\ell)}\xi_{b,s}^{(\ell)}]
=\sigma_\ell^2\mathbb E[H_{a,k}^{(\ell-1)}H_{b,s}^{(\ell-1)}],
\quad
\mathbb E[\eta_{a,k}^{(\ell)}\eta_{b,s}^{(\ell)}]
=\sigma_\ell^2\mathbb E[\delta_{a,k}^{(\ell)}\delta_{b,s}^{(\ell)}].
\tag{6}
\]

Different matrix/orientation families are independent Gaussian families;
each family's own times and inputs are generally dependent. The
coordinate space of hidden population \(\ell\) uses its adjacent slots
\(\xi^{(\ell)}\) and \(\eta^{(\ell+1)}\), with the appropriate root at
the first/last layer. These are distinct neuron populations, not paired
finite-width coordinates.

Define unscaled expected derivatives

\[
A_{ak,bs}^{(\ell)}=
\mathbb E\frac{\partial\delta_{a,k}^{(\ell)}}
{\partial\xi_{b,s}^{(\ell)}},\qquad s\le k,
\quad
C_{ak,bs}^{(\ell)}=
\mathbb E\frac{\partial H_{a,k}^{(\ell-1)}}
{\partial\eta_{b,s}^{(\ell)}},\qquad s<k.
\tag{7}
\]

The exact local response representation is

\[
Z_{a,k}^{(\ell)}=\xi_{a,k}^{(\ell)}+
\sum_{b,s<k}F_{ak,bs}^{(\ell)}\delta_{b,s}^{(\ell)},
\tag{8}
\]
\[
P_{a,k}^{(\ell-1)}=\eta_{a,k}^{(\ell)}+
\sum_{b,s\le k}D_{ak,bs}^{(\ell)}H_{b,s}^{(\ell-1)},
\tag{9}
\]

where

\[
F_{ak,bs}^{(\ell)}=
\sigma_\ell^2 C_{ak,bs}^{(\ell)}
-2\kappa_\ell\Delta\omega_b r_{b,s}
\mathbb E[H_{b,s}^{(\ell-1)}H_{a,k}^{(\ell-1)}],
\tag{10}
\]
\[
D_{ak,bs}^{(\ell)}=
\sigma_\ell^2 A_{ak,bs}^{(\ell)}
-\mathbf1_{s<k}2\kappa_\ell\Delta\omega_b r_{b,s}
\mathbb E[\delta_{b,s}^{(\ell)}\delta_{a,k}^{(\ell)}].
\tag{11}
\]

For compact cap notation only, put
\(\widetilde A^{(\ell)}=\sigma_\ell^2 A^{(\ell)}\) and
\(\widetilde C^{(\ell)}=\sigma_\ell^2 C^{(\ell)}\).
Thus the sigma factors never enter the trained terms.

#### SubGaussian sums without maxima of Gaussian histories

For a scalar random variable define

\[
\mathcal N(U)=\sup_{p\ge2}\frac{\|U\|_{L^p}}{\sqrt p}.
\tag{12}
\]

It is a norm, and \(\mathcal N(U)\le B\) implies

\[
\mathbb E\exp\bigl(U^2/(8eB^2)\bigr)\le4/3,
\quad
\mathbb E e^{\lambda|U|}\le(4/3)e^{2e\lambda^2B^2}.
\tag{13}
\]

Indeed the \(r\)-th term in the first exponential series is at most
\((2r)^r/((8e)^rr!)\le4^{-r}\); the second inequality follows by
\(\lambda|U|\le U^2/(8eB^2)+2e\lambda^2B^2\). The case \(B=0\) is
understood as \(U=0\).

If each \(U_{b,s}\) has \(\mathcal N(U_{b,s})\le B\), Jensen applied
with weights \(\Delta\omega_b/(k\Delta)\) gives

\[
\mathbb E\exp\left(\lambda\Delta
\sum_{s<k}\sum_b\omega_b|U_{b,s}|\right)
\le(4/3)\exp(2e\lambda^2T^2B^2),\qquad k\Delta\le T.
\tag{14}
\]

This requires no independence over time or inputs. The maximum of Gaussian
coordinates or of a Gaussian history is never bounded in this argument.

#### The simultaneous field and response bounds

We prove that there exist fixed finite caps \(a_\ell,c_\ell\), constants
\(B_H,B_{P,\ell}\), and \(T_0>0\), with \(T_0\le T_{\rm ball}\), such
that at every mesh point up to \(T_0\)

\[
\sum_{b,s\le k}|\widetilde A_{ak,bs}^{(\ell)}|\le a_\ell,
\qquad
|\widetilde C_{ak,bs}^{(\ell)}|\le c_\ell\Delta\omega_b,
\tag{15}
\]
\[
\mathcal N(H_{a,k}^{(\ell)})\le B_H,
\qquad
\mathcal N(P_{a,k}^{(\ell)})\le B_{P,\ell}.
\tag{16}
\]

Set \(f_\ell=c_\ell+J\) for \(\ell\ge2\), and \(f_1=1\).
Under the response caps,

\[
|F_{ak,bs}^{(\ell)}|\le f_\ell\Delta\omega_b,
\qquad
\sum_{b,s\le k}|D_{ak,bs}^{(\ell)}|\le a_\ell+JT.
\tag{17}
\]

Choose a constant \(K\ge2\), depending only on the fixed bounds in the
lemma, large enough to dominate every root/innovation \(\mathcal N\)-norm
after applying an activation and every coefficient in (2)--(3). Fix this
\(K\) once. The triangle inequality for \(\mathcal N\), (1)--(3), and
(8)--(9) give the following bounds using only already constructed fields:

\[
\mathcal N(H_{a,k}^{(1)})\le K+KT\sup_{b,s<k}
\mathcal N(P_{b,s}^{(1)}),
\tag{18}
\]
\[
\mathcal N(H_{a,k}^{(\ell)})\le K+Kf_\ell T
\sup_{b,s<k}\mathcal N(P_{b,s}^{(\ell)}),\quad 2\le\ell\le L,
\tag{19}
\]
\[
\mathcal N(P_{a,k}^{(\ell)})\le K+(a_{\ell+1}+JT)
\sup_{b,s\le k}\mathcal N(H_{b,s}^{(\ell)}),\quad\ell<L,
\tag{20}
\]
\[
\mathcal N(W_k^{(L+1)})\le K+KT
\sup_{b,s<k}\mathcal N(H_{b,s}^{(L)}).
\tag{21}
\]

Take

\[
B_H=2K,\qquad B_{P,L}=2K,\qquad
B_{P,\ell}=4K(1+a_{\ell+1})\quad(\ell<L).
\tag{22}
\]

Once response caps have been chosen, (18)--(21) preserve these field caps
if \(JT\le1\), \(2KT\le1\), and
\(f_\ell T B_{P,\ell}\le1\) for every \(1\le\ell\le L\).
For (20), its right side is at most
\(K+2K(a_{\ell+1}+1)\le4K(1+a_{\ell+1})\).
For each finite mesh all \(\mathcal N\)-norms are finite before this
estimate: the causal magnitude recursions bound each field by a finite
deterministic linear combination of absolute roots/innovations, since
\(|\phi(z)|\le M(1+|z|)\) and \(|\delta|\le M|P|\).

#### Full forward-slot derivative rows

Fix a layer \(2\le\ell\le L\). Differentiate only with respect to its
own forward slots \(\xi^{(\ell)}\); hold the adjacent backward slots and
roots fixed. Let

\[
v_{a,k}^{(\ell)}=
\sum_{b,s\le k}\left|
\frac{\partial Z_{a,k}^{(\ell)}}{\partial\xi_{b,s}^{(\ell)}}
\right|,\qquad
V_k^{(\ell)}=\max_{a,u\le k}v_{a,u}^{(\ell)}.
\tag{23}
\]

The maximum here is a maximum of derivative row sums, not of random
backward fields. Write \(d_\ell=1+a_{\ell+1}\) if \(\ell<L\), and
\(d_L=1\). Let \(M\ge1\) dominate all activation bounds.

For \(\ell<L\), direct differentiation of (9) gives

\[
\sum_{b,s}\left|
\frac{\partial P_{a,u}^{(\ell)}}{\partial\xi_{b,s}^{(\ell)}}
\right|
\le M(a_{\ell+1}+JT)V_u^{(\ell)}.
\tag{24}
\]

For the last layer, differentiating the integrated readout update (3)
instead gives a bound \(2\kappa_{L+1}RMTV_u^{(L)}\).
The product rule in (1), with these bounds, proves for a fixed constant
\(C\) depending only on the lemma's data that

\[
\sum_{b,s}\left|
\frac{\partial\delta_{a,u}^{(\ell)}}
{\partial\xi_{b,s}^{(\ell)}}\right|
\le C\bigl(|P_{a,u}^{(\ell)}|+d_\ell\bigr)V_u^{(\ell)}.
\tag{25}
\]

The first term in (8) has derivative row sum exactly one. Its memory has
only earlier times. By the entrywise estimate (17),

\[
V_k^{(\ell)}\le1+Cf_\ell\Delta\sum_{u<k}
\left(d_\ell+\sum_b\omega_b|P_{b,u}^{(\ell)}|\right)V_u^{(\ell)}.
\tag{26}
\]

To justify the prefix maximum, the bound for every earlier time is no
larger than the displayed right side because every summand is nonnegative.
Discrete Gronwall gives

\[
V_k^{(\ell)}\le
\exp\left(Cf_\ell T d_\ell+
Cf_\ell\Delta\sum_{u<k}\sum_b\omega_b|P_{b,u}^{(\ell)}|\right).
\tag{27}
\]

Using (14), then Cauchy--Schwarz in (25), yields

\[
\sum_{b,s\le k}|\widetilde A_{ak,bs}^{(\ell)}|
\le C(B_{P,\ell}+d_\ell)
\exp\left(Cf_\ell T d_\ell+
Cf_\ell^2T^2B_{P,\ell}^2\right).
\tag{28}
\]

Here and in the remaining estimates choose one \(C\ge1\) large enough
for all displayed inequalities, and fix it before choosing response caps.
There are finitely many algebraic bound types; neither \(C\) nor \(K\)
depends on a response cap. Notice that (28) uses
\(\|P_{a,k}^{(\ell)}\|_{L^2}\|V_k^{(\ell)}\|_{L^2}\), not the
\(L^2\)-norm of a maximum over the input index or time.

#### A single backward-slot pulse

Fix \(\ell\ge2\), one input \(b\), one time \(s\), and differentiate
the local coordinate functions of layer \(\ell-1\) with respect to the
single slot \(\eta_{b,s}^{(\ell)}\). Put

\[
D_k=\max_{a,u\le k}\left|
\frac{\partial Z_{a,u}^{(\ell-1)}}
{\partial\eta_{b,s}^{(\ell)}}\right|.
\tag{29}
\]

It vanishes for \(k\le s\). Differentiating (9) and (1) gives, pointwise,

\[
\left|\frac{\partial\delta_{a,u}^{(\ell-1)}}
{\partial\eta_{b,s}^{(\ell)}}\right|
\le M\mathbf1_{a=b,u=s}
+C\bigl(|P_{a,u}^{(\ell-1)}|+d_{\ell-1}\bigr)D_u.
\tag{30}
\]

Indeed the derivative of the direct Gaussian term in (9) is precisely
\(\mathbf1_{a=b,u=s}\); the derivative of its response has magnitude
at most \(M(a_\ell+JT)D_u\). The other product-rule term is bounded by
\(M|P_{a,u}^{(\ell-1)}|D_u\).

For \(\ell=2\), insert (30) in the accumulated update (2). Its direct
pulse has magnitude at most \(2\kappa_1gRM\Delta\omega_b\).
For \(\ell\ge3\), insert it in (8) for layer \(\ell-1\); the direct
pulse has magnitude at most \(Mf_{\ell-1}\Delta\omega_b\).
Both cases therefore obey, for \(k>s\),

\[
D_k\le Cf_{\ell-1}\Delta\omega_b+
Cf_{\ell-1}\Delta\sum_{u<k}
\left(d_{\ell-1}+\sum_a\omega_a|P_{a,u}^{(\ell-1)}|\right)D_u.
\tag{31}
\]

Here \(f_1=1\). Gronwall, (14), and the bounded activation derivative
give

\[
\frac{|\widetilde C_{ak,bs}^{(\ell)}|}{\Delta\omega_b}
\le Cf_{\ell-1}
\exp\left(Cf_{\ell-1}T d_{\ell-1}+
Cf_{\ell-1}^2T^2B_{P,\ell-1}^2\right).
\tag{32}
\]

The factor \(\Delta\omega_b\) is retained from one source pulse. There
is no factor \(1/\omega_b\) in any constant and no sum of unweighted
Gaussian absolute values.

#### Cap selection and literal construction order

First choose the forward-response caps from bottom to top:

\[
c_2=4C,\qquad c_\ell=4C(c_{\ell-1}+J),\quad3\le\ell\le L.
\tag{33}
\]

These use only the \(T=0\) prefactors in (32), which do not contain any
backward cap. Next choose the backward-response caps from top to bottom:

\[
a_L=4C(2K+1),\qquad
a_\ell=4C(4K+1)(1+a_{\ell+1}),\quad 2\le\ell<L.
\tag{34}
\]

These dominate four times the \(T=0\) prefactors of (28), using (22).
All caps are now fixed finite numbers. Choose \(T_0>0\) satisfying

\[
T_0\le\min(T_{\rm ball},1),\quad JT_0\le1,\quad2KT_0\le1,
\quad f_\ell T_0 B_{P,\ell}\le1\quad(1\le\ell\le L),
\tag{35}
\]

and such that every exponent on the right sides of (28) and (32) is at
most \(\log2\) when \(T=T_0\). Each exponent tends to zero with \(T\)
after the caps have been fixed; there are finitely many of them. Thus this
choice gives a strictly positive time depending only on the stated data.
Equations (28) and (32) then improve their respective response caps by a
factor of two.

For completeness, this is an induction on the actual causal construction,
not a bootstrap that assumes all future tails:

1. At time \(k\), \(W_k^{(L+1)}\) and \(Z_{a,k}^{(1)}\) use only
   histories before \(k\). Verify their bounds from (18), (21).
2. Construct the current forward layers in order \(2,\ldots,L\).
   Before constructing layer \(\ell\), its coefficient
   \(\widetilde C^{(\ell)}\) is computed from the already constructed
   \(H^{(\ell-1)}\). Estimate (32) uses only past
   \(P^{(\ell-1)}\), whose tails and backward response caps are known,
   and the current lower-layer forward cap, which is already known.
   Equation (19) then verifies the current \(H^{(\ell)}\) bound using
   only past \(P^{(\ell)}\). This constructs the current innovations'
   source covariances too.
3. Construct the current backward layers in order \(L,\ldots,2\).
   At the top \(P^{(L)}=W^{(L+1)}\) is already bounded. At a lower
   layer \(\ell\), the current \(P^{(\ell)}\) was just constructed
   using the current higher response \(\widetilde A^{(\ell+1)}\);
   (20) verifies its cap. Hence (25)--(28) use known current
   \(P^{(\ell)}\) tails and known upper response coefficients. They
   verify the current \(\widetilde A^{(\ell)}\) cap, after which (9)
   constructs \(P^{(\ell-1)}\).
4. Apply (2)--(3) for the next step and repeat.

At \(k=0\) there is no forward response memory. The same top-down
backward construction starts from the readout root; (28) has \(V_0=1\).
Thus the induction starts without zero-readout or centered-readout
assumptions. Neither a current forward coefficient nor a current backward
coefficient needs its own unconstructed value. This proves (15)--(16).

In particular, for some fixed \(c_*,C_*>0\),

\[
\sup_\Delta\sup_{k\Delta\le T_0}\max_{a,\ell}
\mathbb E\exp\left(c_*|P_{a,k}^{(\ell)}|^2\right)\le C_*.
\tag{36}
\]

The same statement holds for every hidden activation and, by (2) and
(8), every preactivation. It implies the uniform RMS cutoff-tail bound
\(\|P\mathbf1_{|P|>R}\|_{L^2}\le C e^{-cR^2}\), after decreasing
\(c\). No bound on a maximum over neurons, dataset elements, or time was
proved or needed.

The proof also holds for arbitrary deterministic positive step lengths
\(\Delta_s\) with total time at most \(T_0\): replace every source factor
\(\Delta\omega_b\) at time \(s\) by \(\Delta_s\omega_b\), and replace
\(k\Delta\) by \(\sum_{s<k}\Delta_s\). The Jensen weights in (14) become
\(\Delta_s\omega_b/\sum_{u<k}\Delta_u\); the single-slot pulse in (31) is
exactly \(\Delta_s\omega_b\); every Gronwall estimate uses only total
time. Nothing else changes. Consequently (36) also holds for fields
recomputed at an affine Euler-state interpolation time: append one final
Euler update of length \(\theta\Delta\), \(0<\theta<1\), to the preceding
full steps, and evaluate the full forward/backward network there. The
constants are independent of \(\theta\). This bounds each interpolation
time; it is not a tail bound for a supremum of the path.

#### Consequences and boundaries

The depth extension therefore supplies the required Gaussian-tail part of
the reference comparison for smooth globally Lipschitz activations,
including when their values and the initial readout are unbounded. The
remaining proof must provide the preliminary RMS/operator ball, the
common operator realization, the oracle interpolation comparison, and its
order of limits. This proof unit does not certify those separate steps.

The exact same lemma holds when each \(2r_{a,k}\) in (2)--(4) is replaced
by any deterministic coefficient uniformly bounded on the preliminary
ball. This permits a general-loss theorem once that theorem proves the
required boundedness and feedback Lipschitz estimate for the loss
derivative.

The constants only use uniform bounds on \(\phi\)'s value at zero and
its first two derivatives. Thus this lemma is uniform under smooth
mollifications of globally Lipschitz \(C^{1,1}\) activations. Passing from
the mollified flows to the original activation still requires the
separate stability argument. ReLU has discontinuous derivative and is not
covered by this lemma or this mollification statement.

The proof is for every fixed finite depth; its constants can grow rapidly
with depth. It proves neither a depth-uniform interval nor arbitrary-depth
strict feature activity. Those are different claims.

The response rule in (6)–(11) follows from A.2 at each fixed finite C2 program. Named sources and deterministic coefficients are frozen when differentiating. This handles singular covariances and does not invoke an all-moment scalar-feedback theorem.

### C.3. Gaussian strict-activity corollary

Within this proof unit, unqualified section and equation numbers are local.

This proof unit proves the strict nontriviality part of the two-hidden-layer population result. It is conditional on existence of the population gradient flow with the mean-square continuity specified below. It does not, by itself, establish an existence theorem or a width limit for its whole activation class.

The useful conclusion is broad: **bounded, nonconstant, continuously differentiable activations with bounded derivatives are sufficient**, in both hidden layers. Neither activation needs to be odd, analytic, monotone, or strictly monotone. Derivatives may change sign and may vanish on intervals. Thus bounded nonconstant \(C^2\) activations with bounded derivatives certainly qualify. A broader conditional version allows unbounded activations with bounded continuous derivatives, provided both activations are nonaffine.

#### Setup and conclusion

Fix \(m<\infty\) inputs \(x_a\in\mathbb R^d\) with
\[
\frac{\|x_a\|_2^2}{d}=1,
\qquad
G_{ab}=\frac{x_a^\top x_b}{d},
\qquad |G_{ab}|<1\quad(a\ne b).
\]
The Gram matrix \(G\) may be singular. Let every label \(y_a\) be a nonzero real number; arbitrary sign labels are included. Fix \(\sigma_1,\sigma_2,\kappa_1,\kappa_2,\kappa_3>0\).

Use \(\phi^{(1)}\) and \(\phi^{(2)}\) for the two activations. In the simple sufficient class both are bounded, nonconstant, continuously differentiable, with bounded derivatives. Initialize the first-layer population roots by
\[
Z_{0,a}^{(1)}
=\frac{\sigma_1 g^\top x_a}{\sqrt d},
\qquad g\sim N(0,I_d),
\]
the middle action by the joint forward/adjoint limit of an independent matrix with entries \(N(0,\sigma_2^2/n)\), and the rescaled population readout by \(W_0^{(3)}=0\).

The network quantities are
\[
H_a^{(1)}=\phi^{(1)}(Z_a^{(1)}),
\qquad
Z_a^{(2)}=W^{(2)}H_a^{(1)},
\qquad
H_a^{(2)}=\phi^{(2)}(Z_a^{(2)}),
\]
\[
f_a=\mathbb E[W^{(3)}H_a^{(2)}],
\qquad r_a=f_a-y_a,
\qquad L=\sum_a r_a^2,
\]
\[
\delta_a^{(2)}=W^{(3)}(\phi^{(2)})'(Z_a^{(2)}),
\qquad
\delta_a^{(1)}
=(\phi^{(1)})'(Z_a^{(1)})(W^{(2)})^*\delta_a^{(2)}.
\]
Suppose the limiting flow satisfies
\[
\begin{aligned}
\dot Z_a^{(1)}
&=-2\kappa_1\sum_bG_{ab}r_b\delta_b^{(1)},\\
\dot W^{(2)}
&=-2\kappa_2\sum_b r_b\delta_b^{(2)}\otimes H_b^{(1)},\\
\dot W^{(3)}
&=-2\kappa_3\sum_b r_bH_b^{(2)},
\end{aligned}\tag{1}
\]
where \((u\otimes v)V=u\mathbb E[vV]\). Write \(\|U\|_{L^2}=\sqrt{\mathbb E[U^2]}\) for root-mean-square size; the operator norm measures its largest amplification. Require continuity of the field variables in mean square and of the middle action in operator norm, with the corresponding integral equations valid in those norms. The bounded continuous activation derivatives then justify the directional chain rules used below. The two neuron populations remain separate; every expectation pairs coordinates of the same layer.

There is a fixed \(T_*>0\) on which the following hold:

- For every input, both hidden preactivations move nontrivially. Their RMS speeds are positive for every \(0<t\le T_*\), of order \(t\); their squared displacements are of order \(t^4\).
- The trained middle matrix moves nontrivially when applied to each fixed initial first-layer activation.
- All three kernel blocks are positive definite for \(0<t\le T_*\), and each block is nonconstant.
- The summed loss has a uniformly negative slope, including at initialization.
- Every hidden marginal has variance and best-affine-fit error for its activation bounded below by positive constants on \([0,T_*]\).

The time and constants depend on the fixed data, activations, labels, and positive parameters, but not on width or learning rate. Strict positivity is not claimed uniformly as the inputs become parallel, labels approach zero, or other nondegeneracy parameters approach their boundaries.

#### Why the first activation Gram matrix is positive definite

The key geometric fact needs no high derivatives or analyticity.

**Bounded ridge-function independence.** If \(\phi\) is bounded, continuous, and nonconstant, then the functions
\[
w\longmapsto\phi\!\left(\frac{w^\top x_a}{\sqrt d}\right),
\qquad a=1,\ldots,m,
\]
are linearly independent whenever the inputs are pairwise nonparallel.

To prove it, suppose a linear combination with coefficients \(c_a\) is zero for every \(w\), and select \(a\) with \(c_a\ne0\). For every \(b\ne a\), set
\[
\xi_{ab}
=
\frac{x_a/\sqrt d-G_{ab}x_b/\sqrt d}{1-G_{ab}^2}.
\]
Then
\[
\frac{x_a^\top\xi_{ab}}{\sqrt d}=1,
\qquad
\frac{x_b^\top\xi_{ab}}{\sqrt d}=0.
\]
For a vector \(v\), let \(\Delta_v F(w)=F(w+v)-F(w)\). Apply the commuting differences
\[
\prod_{b\ne a}\Delta_{h\xi_{ab}}
\]
to the proposed linear identity. Every term other than the \(a\)-th is killed by one of these differences. Each difference shifts the \(a\)-th scalar argument by \(h\). Therefore
\[
\Delta_h^{m-1}\phi(s)=0
\qquad\text{for every }s,h\in\mathbb R.
\tag{2}
\]
For fixed \(s,h\), the bounded sequence \(a_j=\phi(s+jh)\), \(j\ge0\), has vanishing \((m-1)\)-st differences. This forces it to be constant: its \((m-2)\)-nd difference is constant; if that constant were nonzero, the next lower difference would grow linearly, contradicting boundedness of every difference of a bounded sequence. Repeating gives \(a_{j+1}=a_j\). For \(m=2\) this is immediate from (2), and \(m=1\) is immediate from nonconstancy. Consequently \(\phi(s+h)=\phi(s)\) for every \(s,h\), contradicting nonconstancy. This proves the claim.

Now define
\[
Q_{ab}=\mathbb E[H_{0,a}^{(1)}H_{0,b}^{(1)}].
\tag{3}
\]
If \(c^\top Qc=0\), then \(\sum_a c_a\phi^{(1)}(\sigma_1g^\top x_a/\sqrt d)=0\) almost surely. Continuity and the full support of \(\sigma_1g\) make this an identity for all \(w\). The preceding argument forces \(c=0\). Hence \(Q\) is positive definite, even when \(G\) is singular.

There is a useful broader version. If \(\phi^{(1)}\) is nonaffine and continuously differentiable with bounded derivative, then its derivative is bounded, continuous, and nonconstant. Differentiate a putative ridge identity in a direction \(v\) with \(v^\top x_a\ne0\) for all \(a\); such a direction avoids finitely many proper hyperplanes. It gives a linear identity among the ridge functions of \((\phi^{(1)})'\), with coefficients \(c_a v^\top x_a/\sqrt d\). Bounded ridge-function independence again makes every \(c_a=0\). Thus \(Q\succ0\) also holds for unbounded nonaffine first activations with bounded continuous derivative.

#### Positive response covariances, including activation flat parts

Write
\[
Y_a:=Z_{0,a}^{(2)}.
\]
The tuple \(Y\) is centered Gaussian with covariance \(\sigma_2^2Q\), so it has full support in \(\mathbb R^m\). Define the following recurring quantities:
\[
\begin{aligned}
S&=\sum_a y_a\phi^{(2)}(Y_a),
&U_a&=S(\phi^{(2)})'(Y_a),\\
P_a&=(W_0^{(2)})^*U_a,
&B_a&=(\phi^{(1)})'(Z_{0,a}^{(1)})P_a,\\
V_{ab}&=\mathbb E[U_aU_b],
&D_{ab}&=\mathbb E[B_aB_b].
\end{aligned}\tag{4}
\]

The matrix \(V\) is positive definite. Suppose \(\sum_a c_aU_a=0\) almost surely. Continuity and Gaussian full support imply, for every \(s\in\mathbb R^m\),
\[
\left(\sum_a y_a\phi^{(2)}(s_a)\right)
\left(\sum_a c_a(\phi^{(2)})'(s_a)\right)=0.
\tag{5}
\]
Where the first factor is nonzero, the second is zero. If the first factor is zero and some \((\phi^{(2)})'(s_a)\ne0\), its corresponding partial derivative \(y_a(\phi^{(2)})'(s_a)\) is nonzero; arbitrarily close points have a nonzero first factor, so continuity again makes the second factor zero. If all activation derivatives at that point vanish, the second factor is already zero. Consequently
\[
\sum_a c_a(\phi^{(2)})'(s_a)=0
\qquad\text{for every }s.
\]
The derivative \((\phi^{(2)})'\) is nonconstant, because a bounded nonconstant activation cannot have constant derivative. Varying one coordinate forces each \(c_a=0\). No division by \(S\) was used: \(S\) is allowed to vanish on a set of positive probability.

For the broader conditional class, boundedness of \(\phi^{(2)}\) can be replaced here by nonaffinity and a bounded continuous derivative. The derivative remains nonconstant, and all the necessary moments exist because \(\phi^{(2)}\) has at most linear growth on the Gaussian input.

Conditioning the initial Gaussian matrix on its initial forward calls gives
\[
P_a
=
\sum_c H_{0,c}^{(1)}
\left[Q^{-1}\mathbb E[YU_a]\right]_c
+\Gamma_a,
\qquad
\Gamma\sim N(0,\sigma_2^2V),
\tag{6}
\]
where \(\Gamma\) is independent of the first-layer roots. This is the reused-transpose response, not a replacement of the transpose by an independent matrix. The deterministic response in (6) retains the information from the initial forward uses.

For any deterministic \(c\ne0\), the conditional Gaussian covariance gives
\[
\begin{aligned}
\mathbb E\left[\left(\sum_a c_aB_a\right)^2\right]
&\ge
\sigma_2^2\lambda_{\min}(V)
\sum_a c_a^2
\mathbb E[((\phi^{(1)})'(Z_{0,a}^{(1)}))^2]\\
&>0.
\end{aligned}\tag{7}
\]
Each final expectation is positive: a continuously differentiable nonconstant function has a nonzero derivative on an interval, and every first-layer Gaussian marginal has full support. Therefore \(D\succ0\), even if the derivative is zero on large sets or changes sign.

#### Each input moves in both hidden layers

Set
\[
T_a=\sum_bG_{ab}y_bB_b,
\qquad
M_a=\sum_b y_bQ_{ab}U_b,
\]
\[
A_a=(\phi^{(1)})'(Z_{0,a}^{(1)})T_a,
\qquad
R_a^\kappa
=\kappa_2M_a+\kappa_1W_0^{(2)}A_a.
\tag{8}
\]
Each \(T_a\) is nonzero in mean square. Its coefficient vector against \(B\) has \(a\)-th entry \(G_{aa}y_a=y_a\ne0\), and \(D\succ0\).

Each \(R_a^\kappa\) is also nonzero, but this requires more than positivity of an aggregate sum. Subtract the mean-square projection of \(A_a\) onto \(\operatorname{span}\{H_{0,b}^{(1)}\}\):
\[
\alpha_a=Q^{-1}\mathbb E[H_0^{(1)}A_a],
\qquad
A_a^\perp
=A_a-\sum_b\alpha_{a,b}H_{0,b}^{(1)}.
\tag{9}
\]
Conditional on the first-layer roots, \(A_a\) is linear in \(\Gamma\) with coefficients
\[
c_b
=(\phi^{(1)})'(Z_{0,a}^{(1)})
G_{ab}y_b
(\phi^{(1)})'(Z_{0,b}^{(1)}).
\]
Its \(a\)-th coefficient is
\[
c_a=y_a((\phi^{(1)})'(Z_{0,a}^{(1)}))^2,
\]
which is nonzero with positive probability. Since \(V\succ0\),
\[
\mathbb E[(A_a^\perp)^2]
\ge
\mathbb E\operatorname{Var}(A_a\mid Z_0^{(1)})
=\sigma_2^2\mathbb E[c^\top Vc]>0.
\tag{10}
\]

Conditioning the same initial matrix on both sets of known calls,
\[
W_0^{(2)}H_{0,b}^{(1)}=Y_b,
\qquad
(W_0^{(2)})^*U_b=P_b,
\]
gives the next forward response
\[
W_0^{(2)}A_a
=
\sum_b\alpha_{a,b}Y_b
+\sum_b\beta_{a,b}U_b
+\sigma_2\sqrt{\mathbb E[(A_a^\perp)^2]}\,\gamma_a,
\qquad
\beta_a=V^{-1}\mathbb E[PA_a^\perp].
\tag{11}
\]
Here \(\gamma_a\) is standard Gaussian independent of the previous second-layer coordinates. The formula is the finite Gaussian conditional mean plus the unused matrix randomness: the input component in (9) has the displayed squared norm, while projection of the fresh output off finitely many previous output directions disappears in normalized mean square. Positive definiteness of \(Q,V\) justifies both inverses. A separate marginal calculation for each \(a\) is sufficient; independence between the different \(\gamma_a\) is not claimed.

The term \(M_a\) depends only on \(Y\), and hence cannot cancel this independent Gaussian component. Therefore
\[
\mathbb E[(R_a^\kappa)^2]
\ge
\kappa_1^2\sigma_2^2\mathbb E[(A_a^\perp)^2]
>0.
\tag{12}
\]
The learned-matrix contribution \(M_a\) is separately nonzero: its coefficient vector \((y_bQ_{ab})_b\) against \(U\) has nonzero \(a\)-th entry \(y_aQ_{aa}\), and \(V\succ0\).

At initialization \(r_a(0)=-y_a\) and \(W^{(3)}(0)=0\). Dividing the integral equations by the indicated powers of \(t\) gives
\[
\begin{aligned}
W^{(3)}(t)&=2\kappa_3tS+o_{L^2}(t),\\
\delta_a^{(2)}(t)&=2\kappa_3tU_a+o_{L^2}(t),\\
Z_a^{(1)}(t)-Z_{0,a}^{(1)}
&=2\kappa_1\kappa_3t^2T_a+o_{L^2}(t^2),\\
W^{(2)}(t)-W_0^{(2)}
&=2\kappa_2\kappa_3t^2
\sum_b y_bU_b\otimes H_{0,b}^{(1)}+o_{\mathrm{op}}(t^2),\\
Z_a^{(2)}(t)-Y_a
&=2\kappa_3t^2R_a^\kappa+o_{L^2}(t^2).
\end{aligned}\tag{13}
\]
For example the readout equation first gives its \(t\)-coefficient. Multiplication by the bounded continuous derivative gives the backward \(t\)-coefficient. The first-layer and middle-matrix integrals then start at order \(t^2\). In the last equation, the learned-matrix term is \(\kappa_2M_a\), while the moving first activation gives \(\kappa_1W_0^{(2)}A_a\). Bounded derivatives justify these activation difference quotients by dominated convergence along mean-square converging increments.

Direct substitution in (1) also gives
\[
\frac{\dot Z_a^{(1)}(t)}t
\longrightarrow 4\kappa_1\kappa_3T_a,
\qquad
\frac{\dot Z_a^{(2)}(t)}t
\longrightarrow 4\kappa_3R_a^\kappa
\quad\text{in }L^2.
\tag{14}
\]
Thus every hidden RMS speed is bounded above and below by positive constants times \(t\), on a fixed sufficiently short interval. For the first layer,
\[
\mathbb E[(Z_a^{(1)}(t)-Z_{0,a}^{(1)})^2]
=4\kappa_1^2\kappa_3^2\mathbb E[T_a^2]t^4+o(t^4),
\]
\[
\int_0^t\mathbb E[|\dot Z_a^{(1)}(s)|^2]\,ds
=\frac{16}{3}\kappa_1^2\kappa_3^2\mathbb E[T_a^2]t^3+o(t^3).
\tag{15}
\]
For the second layer replace \(\kappa_1^2\mathbb E[T_a^2]\) by \(\mathbb E[(R_a^\kappa)^2]\). In particular the speed is zero initially, not bounded below by a positive constant as \(t\downarrow0\). It is nonzero at every fixed positive time in the asserted interval.

#### The kernel, loss, and surviving nonlinearity

The physical kernel is \(K=\kappa_1K^{(1)}+\kappa_2K^{(2)}+\kappa_3K^{(3)}\), with
\[
K_{ab}^{(1)}=G_{ab}\mathbb E[\delta_a^{(1)}\delta_b^{(1)}],
\]
\[
K_{ab}^{(2)}
=\mathbb E[H_a^{(1)}H_b^{(1)}]
\mathbb E[\delta_a^{(2)}\delta_b^{(2)}],
\qquad
K_{ab}^{(3)}=\mathbb E[H_a^{(2)}H_b^{(2)}].
\tag{16}
\]
Let \(\circ\) denote entrywise matrix multiplication. Although \(G\) may be singular, \(G\circ D\) is positive definite. Decompose \(G=\sum_j v_jv_j^\top\). Then
\[
G\circ D
=\sum_j\operatorname{diag}(v_j)D\operatorname{diag}(v_j)
\succeq
\lambda_{\min}(D)\operatorname{diag}(G_{11},\ldots,G_{mm})
=\lambda_{\min}(D)I.
\tag{17}
\]
The same argument makes \(Q\circ V\) positive definite, since its diagonal entries \(Q_{aa}\) are positive. Define
\[
A_1=y^\top(G\circ D)y>0,
\qquad
A_2=y^\top(Q\circ V)y>0.
\tag{18}
\]
Adjunction yields
\[
\sum_a y_a\mathbb E[U_aR_a^\kappa]
=\kappa_1A_1+\kappa_2A_2.
\tag{19}
\]
The kernel expansions are therefore
\[
\begin{aligned}
\kappa_1K^{(1)}(t)
&=4\kappa_1\kappa_3^2t^2(G\circ D)+o(t^2),\\
\kappa_2K^{(2)}(t)
&=4\kappa_2\kappa_3^2t^2(Q\circ V)+o(t^2),\\
y^\top K^{(3)}(t)y
&=\mathbb E[S^2]
+4\kappa_3(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2),\\
y^\top K(t)y
&=\kappa_3\mathbb E[S^2]
+8\kappa_3^2(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2).
\end{aligned}\tag{20}
\]
The initial readout block is positive definite: a linear dependence among \(\phi^{(2)}(Y_a)\) would hold for all \(Y\) by full support, and varying one coordinate forces its coefficient to zero. All three blocks are therefore positive definite for sufficiently small positive time. The first two start at zero with positive definite \(t^2\) coefficients, and the third increases in the label direction. Each block, and the total kernel, is nonconstant.

The summed loss satisfies
\[
L(0)=\sum_a y_a^2,
\qquad
-\dot L(0)=4\kappa_3\mathbb E[S^2]>0.
\]
Continuity allows the time interval to be shortened so that
\[
-\dot L(t)\ge2\kappa_3\mathbb E[S^2]>0
\qquad(0\le t\le T_*).
\tag{21}
\]
This does not assert that every individual residual magnitude decreases.

Every initial hidden marginal is a nondegenerate Gaussian. A bounded nonconstant continuous activation cannot agree with an affine function on its full support. Thus the best-affine-fit error
\[
\inf_{\alpha,\beta}
\mathbb E[(\phi^{(\ell)}(Z)-\alpha Z-\beta)^2]
=
\operatorname{Var}(\phi^{(\ell)}(Z))
-\frac{\operatorname{Cov}(Z,\phi^{(\ell)}(Z))^2}
{\operatorname{Var}(Z)}
\tag{22}
\]
is initially positive. The same is true for the broader nonaffine activation class. Bounded derivatives make both activations globally Lipschitz, so these moments vary continuously along the mean-square continuous paths. All \(2m\) variances and all \(2m\) affine-fit errors retain common positive lower bounds on a possibly shorter \([0,T_*]\).

#### Sufficient checks beyond the simple activation class

The positivity argument uses the following concrete sufficient conditions, rather than monotonicity or analyticity:

1. The initial first-activation Gram matrix \(Q\) is positive definite.
2. On the full-support second-layer Gaussian tuple, the Gram matrix \(V\) of \(U_a=S(\phi^{(2)})'(Y_a)\) is positive definite.
3. For every input, \(\mathbb E[((\phi^{(1)})'(Z_{0,a}^{(1)}))^2]>0\).
4. For the separate nonlinear-fit conclusion, each activation is nonaffine on its initial Gaussian support.

These checks are sufficient, not necessary. In conjunction with bounded continuous derivatives and the assumed strong flow, they yield the calculations above. The bounded nonconstant activation class guarantees all of them automatically for pairwise nonparallel inputs and nonzero labels. More broadly, both activations may be unbounded but nonaffine with bounded continuous derivatives: the differentiated ridge argument proves the first check, the proof of (5) proves the second, and Gaussian initialization plus linear growth supplies the required initial moments. This broader statement concerns strict activity conditional on existence; it must not be used to enlarge an independently proved existence theorem without checking that theorem's hypotheses.

Some excluded cases show why nondegeneracy matters. Identical inputs with opposite labels can give \(S=0\) identically and a frozen zero-readout system. Antiparallel inputs with odd activations and equal labels can do the same. A constant first activation has zero first-layer derivative; a constant second activation has zero backward derivative. An affine first activation can make \(Q\) singular when there are more inputs than their linear span dimension. An affine second activation has identical derivative functions, so \(V\) has rank at most one for \(m>1\). Such cases can still have some learning, but the full collection of strict conclusions above is not automatic. Finally, allowing a zero label can invalidate the per-input initial activity assertion, for example for an orthogonal input decoupled from the other labeled inputs.


#### Weighted-loss activity and the exact kernel direction

For the weighted loss in C.1, \(\mathcal L=\sum_a\omega_a(f_a-y_a)^2\), put \(p_a=\omega_a y_a\) in this paragraph. Retain every hypothesis of C.3, including Gaussian first weights, zero population readout and nonzero labels. The unweighted kernel blocks in C.3 are unchanged, and
\[
 \dot f_a=-2\sum_bK_{ab}\omega_b r_b,\qquad
 \dot{\mathcal L}=-4\sum_{a,b}\omega_a r_aK_{ab}\omega_b r_b.
\]
In C.3's definitions of S,U,B,T,M,A and R, and its onset expansions, replace each training label y_b by p_b. Then, with \(D_{ab}=E[B_aB_b]\), \(V_{ab}=E[U_aU_b]\),
\[
 A_1=p^\top(G\circ D)p>0,\qquad A_2=p^\top(Q\circ V)p>0,
\]
\[
 p^\top K(t)p=\kappa_3 ES^2+
 8\kappa_3^2(\kappa_1A_1+\kappa_2A_2)t^2+o(t^2),
 \qquad-\dot{\mathcal L}(0)=4\kappa_3 ES^2>0.
\]
This substitution is justified directly in the raw equations: the factor at initialization is \(-\omega_b r_b(0)=\omega_b y_b\); every first nonzero hidden term is obtained by integrating that factor against the first readout term. All positive-definiteness arguments only require the corresponding p_a to be nonzero, which follows from positive weights and nonzero labels. In the upper-layer acceleration the learned term is a function of the original upper forward tuple, while the forward image of the lower-layer increment has an independent Gaussian component of positive variance. Multiplying by the upper activation derivative preserves a positive squared norm because that derivative is nonzero with positive Gaussian probability. Thus every sample's activation, as well as its preactivation, has nonzero order-t^2 displacement and order-t speed. The quadratic kernel direction is p, not y, for this weighted statement. No initialization variance is inserted in the trained rank-one terms.
