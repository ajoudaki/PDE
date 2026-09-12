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
limiting dynamics. The main theorem concerns each fixed depth and each finite
physical horizon; it does not take a simultaneous depth and width limit.
Sections C.4.1–C.4.4 separately prove local training-law stability and an
input-population limit for two hidden tanh layers on the normalized input
circle. Section C.4.5 proves fixed-time risk reduction and whole-circle
robustness near one fitted reference, with an explicit extremely small radius.

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

These fragments extend the global nonlinear and special-data chapters. Except for C.4, their probability statements take width to infinity at a fixed depth, fixed finite dataset, fixed activation, and fixed finite physical horizon. C.4.1–C.4.4 prove their stated simultaneous sampling/width/GD-step limit for the fixed two-hidden-tanh circle-input model on a common local interval. C.4.5 separately transfers a fitted reference's predictions and useful risk to a fixed-time finite-network guarantee in an explicit small law neighborhood. Constants uniform over a parameter class do not by themselves assert a probability supremum over that class. Layer populations are separate. Initialized actions and their adjoints are constructed jointly; only trained increments are Hilbert--Schmidt.

The packages are: a global two-hidden-layer activation transform and its affine-first arbitrary-data exception; a local fixed-depth C1,1 theorem and its Gaussian strict-activity corollary; separated two-sample offset, odd, and general-shape theorems; all-fixed-depth odd perturbations; the three-sample odd-gain theorem; and exact moderate-amplitude identities, local limits, finite-algorithm estimates, strong endpoints, and conditional continuation.

The finite Gaussian construction, including rank loss, causal bounded-derivative scalar feedback, common generated spaces, and adjunction, is the contained proof in **special-data Section III.F**. The observation and same-width comparison arguments are **Section III.V**. They are mathematical dependencies within the library. Their coordinate hypotheses are verified below; neither theorem is applied directly to an instruction with unbounded derivative. Equation numbers inside each numbered fragment are local to that fragment.

For the two-sample and odd-gain fragments using first-coordinate notation \(V^1\) or \(w\), the exact conversion to the notation contract is
\[
 V^1=W^{(1)}/\sqrt d,\qquad z_a^1=V^1x_a,
 \qquad \frac d n\|dV^1\|_F^2=\frac1n\|dW^{(1)}\|_F^2.
\]
A displayed first matrix with entry variance \(1/d\), including a locally named \(W^1\), always means this \(V^1\). For finite vectors, any rank-one symbol u tensor v or \(u\otimes v\) means the matrix uv^T/n; its population counterpart is the rank-one action q -> u E[vq]. The stored readout is \(C=W^{(L+1)}\), and \(f_a=C^Th_a^L/n\). The half-sum loss in those fragments is explicitly \(\frac12\sum_a(f_a-y_a)^2\); its raw mobilities in canonical coordinates are \((n,1,\ldots,1,n)\). The broad two-layer theorem instead uses the unhalved sum, and the general local theorem uses its stated weighted mean. Their factors of two are retained. An auxiliary feature time or normalized time is never the raw GD step.

The proof units after the common lemmas are organized as follows.

| Fragments | Result | Destination and exact scope |
|---|---|---|
| A, B | Continuous-value Gaussian specialization; activation transform; affine-first exception | Global nonlinear: L=2, bounded top activation/readout, orthogonal data; arbitrary fixed input geometry for an affine first activation. Exact raw GD uses eta_n sqrt(n)->0, or eta_n->0 in the affine exception. |
| C.1–C.3 | Local C1,1 limit, finite-GF corollary, strict Gaussian activity | Global nonlinear: fixed L,m,d, subGaussian first/readout roots and arbitrary fixed data on one positive interval; activity has its additional stated Gaussian/nondegeneracy assumptions. |
| C.4 | Training-law stability, local input-population limit and fitted-reference transfer | Two hidden tanh layers: C.4.1–C.4.4 give arbitrary bounded-label laws, quantitative local stability and simultaneous limits. C.4.5 gives whole-circle endpoint approximation, risk at most 1/4 at T=40, and early paired hidden activity for binary laws in an explicit extremely small neighborhood; no global perturbed-law population flow. |
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

The local theorem C.1 permits subGaussian first weights and readout, arbitrary fixed data, zero middle variances and frozen blocks as stated. The separate strict-activity corollary C.3 requires Gaussian first weights, positive variances and mobilities, zero population readout, nonzero labels and pairwise nonparallel unit inputs. These are additional hypotheses of that corollary. Section C.4 instead fixes two hidden tanh layers and Gaussian initialization, extends the learning law to every bounded-label law on the normalized input circle, and proves quantitative stability and a simultaneous sampling/width/GD-step limit. Its activity conclusion applies to a specified open family of laws.

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

### C.4. Training-law stability for two hidden tanh layers

Within each C.4.1–C.4.4 proof unit, unqualified section and equation numbers are
local. The typed abbreviations w, A, c denote the full first row, W^(2),
and W^(3), respectively; they do not change the canonical normalization.

Sections C.4.1–C.4.4 prove a local quantitative statement about the actual nonlinear
learning algorithm. The separate fixed-accuracy extension is in C.4.5.
Section C.4.6 identifies actual finite-GF data derivatives at that fitted
reference on each fixed horizon and bounds the population homogeneous
propagator uniformly in time. Section [C.4.7](#c47-nonlinear-training-near-the-fitted-tanh-reference)
constructs nonlinear changed-law population flows in a sufficiently small
neighborhood of that reference through physical time 40, captures actual
finite GF on this interval, and gives a finite-contamination remainder with
a width-first bridge to C.4.6. Section C.4.8 gives the actual centered influence and an L2(circle) Gaussian sampling limit at T=40 for every separately fixed Borel law in a smaller neighborhood, with spatial covariance, a mean-square remainder and a width-first finite-GF bridge.
Section [C.4.9](#c49-nonlinear-prediction-selection-during-a-finite-added-data-episode) constructs a finite nonlinear slow-time episode for an open one-added-atom family, selected from original fixed-mixture training at t=tau/epsilon. It determines the whole-circle prediction, proves positive added-atom risk improvement and paired second-hidden adaptation, and captures actual finite GF with width taken first at each fixed epsilon.
The local C.4.1–C.4.4 theorem retains the
Gaussian matrix action and its adjoint and permits every training law on
the compact observation space.

Fix Y>0. Inputs are `x(alpha)=sqrt(2)(cos(alpha),sin(alpha))` in R²;
`u=x/sqrt(2)` and `G(x,x')=u·u'`. The observation space is
`Z=sqrt(2) S^1 x [-Y,Y]`, with metric
`d_Z((x,y),(x',y'))=|x-x'|/sqrt(2)+|y-y'|`. The Wasserstein distance
`W1(mu,nu)` is the infimum over couplings of the expectation of this metric.
No restriction is imposed on atom counts, atom weights, correlations,
coincident inputs, labels conditional on input, or Gram ranks.

The finite network has equal hidden width n, no biases, and

\[
 z^1(x)=W^{(1)}x/\sqrt2,\quad h^1(x)=\tanh z^1(x),\quad
 z^2(x)=W^{(2)}h^1(x),\quad h^2(x)=\tanh z^2(x),\quad
 f_n(x)=(W^{(3)})^Th^2(x)/n.
\]

All entries and blocks are independent initially, with variances
`W^(1):1`, `W^(2):1/n`, `W^(3):1/n²`, and zero Gaussian means. All blocks
train by mean squared loss, with stored-weight mobilities `(n,1,n)`.
Raw GD updates all blocks from the same preceding state, with physical
step eta. Parameters are interpolated linearly and forward quantities are
recomputed. Initialization is independent of random training observations.

**Theorem.** There exist `T_*>0`, `C<infinity` depending only on Y and this
fixed model, with the following properties.

1. On common canonical Gaussian action spaces there is a strong autonomous
   population flow for every law mu. Its state is a full first-row field
   `w in L²(Omega_1;R²)`, a bounded action
   `A: L²(Omega_1)->L²(Omega_2)` and stored readout `c in L²(Omega_2)`.
   Its initialized action is the actual joint forward/transpose limit of
   the Gaussian middle matrix, and its reverse is the Hilbert adjoint.
   Initial state is `(g,A_0,0)` with `g~N(0,I_2)`; the finite random
   readout is retained and has vanishing normalized RMS. The integral
   equations are (T1)–(T2) and (P5) below. The state is continuously differentiable
   in the sum of full-row L², action operator norm and readout L²; it is
   unique among strong continuous integral solutions on these initialized
   spaces. At reached states it is uniquely restartable on the remaining
   local interval in the stated bounded-state class. Learned action
   increments are Hilbert–Schmidt, while the initialized action need not be.

2. For `0<q=W1(mu,nu)<=1`, the entire state and all forward hidden fields
   obey the modulus `Cq exp(C sqrt(log(e/q)))` in their stated norms,
   uniformly in time, and the forward fields uniformly in input. In
   particular

   \[
   \sup_{t\le T_*,\,x\in\sqrt2S^1}|f_\mu(t,x)-f_\nu(t,x)|
   \le Cq\exp(C\sqrt{\log(e/q)}).
   \]

   For q=0 the flows agree. For q>1 their predictions differ by at most
   2B, where B is the fixed common state bound defined in the proof. No
   logarithmic expression is evaluated beyond its stated domain.

3. Let `mu_S=m^(-1) sum_i delta_(x_i,y_i)` and `f_S=f_mu_S`. Samples
   differing in one observation satisfy

   \[
   \sup_{t\le T_*,x}|f_S(t,x)-f_{S'}(t,x)|
   \le\frac C m\exp(C\sqrt{\log(em)}).
   \]

   Define `R_mu(g)=int (g(x)-y)² dmu` and
   `Rhat_S(g)=m^(-1)sum_i(g(x_i)-y_i)²`. For iid observations from mu,

   \[
   \sup_{t\le T_*}\left|\mathbb E_S
   [R_\mu(f_S(t))-\widehat R_S(f_S(t))]\right|
   \le\frac C m\exp(C\sqrt{\log(em)}).
   \]

   The expectation and time supremum have exactly this order.

4. For every deterministic sequence of empirical laws lambda_k converging
   in W1 to mu, every `n_k->infinity`, and every `eta_k->0`, actual finite
   GD satisfies

   \[
   \sup_{t\le T_*,x}|f_{n_k,\eta_k,\lambda_k}(t,x)-f_\mu(t,x)|
     \longrightarrow0\quad\hbox{in probability}.
   \]

   In particular this holds for iid samples of any sizes m_k tending to
   infinity, independent of initialization. No relative growth restriction
   is required among n_k, m_k and eta_k. The finite empirical training loss
   and population risk both converge uniformly in time, in probability,
   to `R_mu(f_mu(t))`. This assertion also retains the paired initial/current
   activation displacement observations described next.

5. Define

   \[
   J_\ell(\mu,t)=\int\mathbb E_\ell
   |H^\ell_\mu(t,x)-H^\ell_0(x)|^2\,d\mu(x,y),\qquad\ell=1,2.
   \]

   For the reference
   `mu_0=½ delta_(sqrt(2)e1,Y/2)+½ delta_(sqrt(2)e2,Y/2)` there are a
   specified positive time t_0<=T_*, a radius r_0>0 and j_0>0, defined
   from its actual flow in Section C.4.4, such that
   `J_ell(mu,t_0)>=j_0/2` for both layers whenever
   `W1(mu,mu_0)<r_0`. For the finite networks in assertion 4 converging
   to any such mu, both corresponding training-averaged squared RMS
   displacements exceed j_0/4 with probability tending to one. The family
   is open relative to all admissible laws and contains correlated and
   nonatomic laws.

The preceding local theorem concerns finite-time training-law stability with genuine
nonlinear hidden learning. It does not assert activity for every law,
fitting, endpoint selection, a risk reduction, excess-risk control,
feature-learning superiority, global-time control, or quantitative
finite-width replacement or approximation rates.

The proof first compares changed-law vector fields using only weighted
individual reference tails. It builds the common strong flow by completing
finite training laws in the full state topology, then compares actual GD
directly to a fixed finite reference oracle. A ghost-sample exchange proves
the precise statistical assertion. Finally an actual-flow expansion and
positive adjunction identity give nonzero representation displacement,
which state continuity transfers to an open family. The dependencies are the complete [Gaussian-program proofs](special_data_limits.md#iiif-fixed-finite-gaussian-programs-common-actions-and-strong-differentiation)
in special-data III.F.1–9, the value/response extensions A.1–A.2 and weighted
response proof C.2 above, and [finite dynamics §§1–4](finite_dynamics.md)
for the exact raw equations.


#### C.4.1. Full-row transport comparison

##### 1. State, finite interpretation, and exact field

Write `u=x/sqrt(2)`, so `|u|=1`, and put `phi=tanh`. Let
`H_1=L2(Omega_1)` and `H_2=L2(Omega_2)` be real probability Hilbert spaces
with their coordinate operations. A population state is

\[
 \theta=(w,A,c)\in L^2(\Omega_1;\mathbb R^2)
       \times\mathcal B(H_1,H_2)\times H_2.
\]

The vector field preserves the affine class `A=A_0+K` where `K` is a
norm-limit of finite-rank operators: the rank-one integrand in (T2) is
continuous on the compact data support, so finite simple approximations
converge in operator norm, as do their time integrals. Define

\[
\begin{aligned}
 Z^1_\theta(u)&=w\cdot u,& H^1_\theta(u)&=\phi(Z^1_\theta(u)),\\
 Z^2_\theta(u)&=A H^1_\theta(u),& H^2_\theta(u)&=\phi(Z^2_\theta(u)),\\
 f_\theta(u)&=\langle c,H^2_\theta(u)\rangle_{H_2},&
 r_\theta(u,y)&=f_\theta(u)-y,\\
 P^2_\theta(u)&=c,&\delta^2_\theta(u)&=\phi'(Z^2_\theta(u))c,\\
 P^1_\theta(u)&=A^*\delta^2_\theta(u),&
 \delta^1_\theta(u)&=\phi'(Z^1_\theta(u))P^1_\theta(u).
\end{aligned}                                                   \tag{T1}
\]

All pairings use a single neuron population. The population rank-one
operator is `(a tensor b)v=a E_1[bv]`. For a probability law `mu` of `(u,y)`
on `S^1 x [-Y,Y]`, the exact mean-square-loss physical vector field is

\[
 F_\mu(\theta)=\left(
 -2\int r_\theta\delta^1_\theta u\,d\mu,
 -2\int r_\theta\delta^2_\theta\otimes H^1_\theta\,d\mu,
 -2\int r_\theta H^2_\theta\,d\mu\right).                         \tag{T2}
\]

In the first integral the scalar field multiplies the explicit input
vector `u`, producing a two-component row. For a finite network, take
`w=W^(1)`, `A=W^(2)`, `c=W^(3)`, replace field norms by the Euclidean or
Frobenius norm divided by `sqrt(n)`, inner products by `a^T b/n`, and
rank-one actions by `a b^T/n`. Formula (T2) then gives exactly the raw
stored-weight mobilities `(n,1,n)`, as follows from
`docs/finite_dynamics.md` §§1–2. Raw GD is
`theta_(j+1)=theta_j+eta F_mu(theta_j)` with all three blocks evaluated at
the preceding state. Parameter interpolation does not interpolate hidden
features: (T1) is recomputed at the interpolated parameters.

On a common carrier define

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_{L^2(\Omega_1;\mathbb R^2)}
                  +\|A-\bar A\|_{\rm op}+\|c-\bar c\|_{L^2(\Omega_2)}. \tag{T3}
\]

For two networks of the same width, its finite counterpart is

\[
 D_n(\theta,\bar\theta)
 =\frac{\|W^{(1)}-\bar W^{(1)}\|_F}{\sqrt n}
  +\|W^{(2)}-\bar W^{(2)}\|_{\rm op}
  +\frac{\|W^{(3)}-\bar W^{(3)}\|_2}{\sqrt n}.       \tag{T3a}
\]

The finite norms in (T3a) are ordinary Frobenius, operator and Euclidean
norms. This distance controls the full first matrix. No cross-width or
finite-to-population operator distance is used anywhere in this proof.

The bound `|phi|<=1`, `|phi'|<=1`, and `Lip(phi')<=2` will be used throughout.
If every individual state norm is at most `B>=1`, then, for every input,

\[
 \|H^1\|_2,\|H^2\|_2\le1,\quad
 \|\delta^2\|_2\le B,\quad \|P^1\|_2,\|\delta^1\|_2\le B^2,
 \quad |f|\le B,\quad |r|\le B+Y.                                \tag{T4}
\]

Consequently the sum of the three velocity norms is at most
`V=2(B+Y)(B^2+B+1)`. If initial individual norms are at most `S_0`, choose
`B=2S_0+2` and

\[
 T_{\rm ball}=\min\{1,(B-S_0)/(4V)\}>0.                          \tag{T5}
\]

The integral-flow first-exit argument and the sum of Euler increments show
that both stay inside this ball up to `2T_ball` for Euler mesh at most
`T_ball`: before a putative first exit the increment of each norm is at most
`2T_ball V<(B-S_0)`. Piecewise affine interpolants have speed bounded by
`V`. These bounds hold for every probability law and every finite empirical
law, regardless of its cardinality.

For the specified initialization, `||W^(1)_0||_F^2/n` tends in probability
to `2`, and `||W^(3)_0||_2^2/n` has expectation `n^(-2)`. The initialized
middle operator is bounded with probability tending to one by the elementary
sphere-net argument in finite dynamics §4. Thus a fixed `S_0` gives a common
high-probability finite ball, independent of the training data. The population
root is the full row `w_0=(g_1,g_2)` with independent standard normals and
`c_0=0`. Retaining the second root coordinate remains necessary even if a
reference training law sees only the first coordinate.

##### 2. The one-reference transport estimate

For a field `P`, write `tau_R(P)=||P 1_{|P|>R}||_2`. If the reference
state is `bar theta`, set

\[
 \mathfrak T_{\nu,R}(\bar\theta)
 =\tau_R(\bar c)+\int\tau_R(P^1_{\bar\theta}(u'))\,
                                  \nu(du',dy').                    \tag{T6}
\]

At finite width these are individual empirical neuron RMS tails. In
particular, for a finite reference law with weights `omega_b`, the second
term is the weighted sum of the individual reference tails, not a tail of a
maximum over the reference inputs or over the actual dataset.

**Transport lemma.** On the ball above, for every `R>=1`, every two laws
`mu,nu`, and every two states on the same carrier,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{T3}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\mathfrak T_{\nu,R}(\bar\theta).                           \tag{T7}
\]

Here `W1` uses `|u-u'|+|y-y'|`, and `C` depends only on `B,Y`. The same
constant works for the normalized finite-network norms and actions. Only
the reference state requires tails.

**Proof.** Fix any coupling `pi` of the two laws, and abbreviate
`h=|u-u'|`, `D=D(theta,bar theta)`. Keeping the full first row gives

\[
 \|Z^1_\theta(u)-Z^1_{\bar\theta}(u')\|_2
 \le\|w-\bar w\|_2+\|\bar w\|_2 h\le D+Bh.
\]

The activation is 1-Lipschitz. Expanding
`A H^1-bar A bar H^1=(A-bar A)H^1+bar A(H^1-bar H^1)` therefore gives

\[
 \max_{\ell=1,2}\bigl(\|Z^\ell_\theta(u)-Z^\ell_{\bar\theta}(u')\|_2
          +\|H^\ell_\theta(u)-H^\ell_{\bar\theta}(u')\|_2\bigr)
       \le C(D+h),                                                   \tag{T8}
\]
\[
 |f_\theta(u)-f_{\bar\theta}(u')|\le C(D+h),\qquad
 |r_\theta(u,y)-r_{\bar\theta}(u',y')|
                         \le C(D+h)+|y-y'|.                         \tag{T9}
\]

For any two preactivations and any reference field `bar P`, pointwise
splitting at `|bar P|=R` gives

\[
 \|[\phi'(Z)-\phi'(\bar Z)]\bar P\|_2
       \le2R\|Z-\bar Z\|_2+2\tau_R(\bar P).                        \tag{T10}
\]

For the top backward field, split its difference as
`phi'(Z^2)(c-bar c)+[phi'(Z^2)-phi'(bar Z^2)]bar c`. Thus

\[
 \|\delta^2_\theta(u)-\delta^2_{\bar\theta}(u')\|_2
       \le C(1+R)(D+h)+2\tau_R(\bar c).                             \tag{T11}
\]

Expanding the adjoint difference, and using (T4), bounds the corresponding
`P^1` difference by `B` times (T11) plus `BD`. Split the first backward
field in the same way, now applying (T10) to `P^1_bar theta(u')`. The result is

\[
 \|\delta^1_\theta(u)-\delta^1_{\bar\theta}(u')\|_2
 \le C(1+R)(D+h)
       +C\tau_R(\bar c)+2\tau_R(P^1_{\bar\theta}(u')).                \tag{T12}
\]

There is one power of `R`: the earlier backward error is multiplied only
by a bounded operator and bounded activation derivative. The new gate
cutoff adds an `R` term and does not multiply that earlier error by `R`.

For the first-weight integral the exact decomposition is

\[
\begin{aligned}
 r\delta^1u-\bar r\bar\delta^1u'
  &=(r-\bar r)\delta^1u
    +\bar r(\delta^1-\bar\delta^1)u
    +\bar r\bar\delta^1(u-u').
\end{aligned}
\]

The row-field norm of a product `P u` equals `||P||_2 |u|`. Therefore
(T4), (T9), and (T12) bound this difference by
`C(1+R)(D+h+|y-y'|)` plus the two reference tails. This verifies the
explicit changing-input factor in the first-weight gradient.

For the middle integral use the identity

\[
 r\delta^2\otimes H^1-\bar r\bar\delta^2\otimes\bar H^1
 =(r-\bar r)\delta^2\otimes H^1
 +\bar r(\delta^2-\bar\delta^2)\otimes H^1
 +\bar r\bar\delta^2\otimes(H^1-\bar H^1)
\]

and `||a tensor b||_op=||a||_2||b||_2`. Equations (T4), (T8), (T9),
and (T11) give the same bound. The readout integral uses
`rH^2-bar r bar H^2=(r-bar r)H^2+bar r(H^2-bar H^2)` and needs no tail.
Integrate these three estimates against `pi`. Every tail depends only
on the second marginal, so its integral is exactly (T6). Taking the
infimum of the coupling costs proves (T7); existence of an optimal
coupling is unnecessary. All the norm inequalities also hold under the
finite normalized pairings, proving the finite assertion. ∎

The full Gaussian first-row root is not multiplied by a backward field
in this argument. It enters (T8) only through its RMS norm. In particular,
no unproved Gaussian estimate for products of root and backward fields,
no Gaussian maximum over observations, and no Gram inverse is hidden in
(T7).

#### C.4.2. Canonical strong population evolution

##### 1. Initial state and strong equation

Use the fields, exact vector field and full-state topology (T1)–(T3).
Write \(\mathcal H_i=L^2(\Omega_i)\) for the two layer spaces and
\(\mathcal E=L^2(\Omega_1;\mathbb R^2)\times
\mathcal B(\mathcal H_1,\mathcal H_2)\times\mathcal H_2\)
for the complete state space with the sum norm (T3).
Section 2 constructs the two probability spaces, the full first-row Gaussian
root `w_0=(g_1,g_2)~N(0,I_2)`, and the initialized middle action A_0 with
its actual adjoint. Put `theta_0=(w_0,A_0,0)`. The strong equation is

\[
 \theta_\mu(t)=\theta_0+\int_0^t F_\mu(\theta_\mu(s))\,ds.
\tag{P5}
\]

The integral is in full-row L2, middle operator norm and readout L2.
Section 3 proves the required strong integrability and continuity. These
are the same unhalved mean-loss equations and physical clock as (T2).

##### 2. One compatible initialized Gaussian action space

Start the countable language of III.F.7 with the full independent Gaussian
pair \((g_1,g_2)\) at population 1, a zero readout at population 2, constants,
both orientations of one initialized matrix, rational linear combinations,
tanh, smooth clipped products, and a countable family of smooth bounded
globally Lipschitz coordinate functions dense on each finite compact box.
Close under finite composition. The actual finite roots are the two columns
of \(W^{(1)}_0\), and the actual finite action is the same matrix
\(W^{(2)}_0\) in both orientations. They have the required independent laws.

The deterministic finite-program theorem III.F.1, including the proof of
singular-query regularization in III.F.5, identifies the joint limiting law
of every finite collection of these programs. Finite unions share the same
initialized arrays; deleting unused instructions changes no finite vector.
Consequently these joint laws are compatible. The chronological Gaussian
extension construction of III.F.4 and III.F.7 realizes the countable language
on two generated probability spaces. It does not sample a fresh independent
backward answer: independent oriented *source groups* acquire the response
corrections in equations (III.F.9)–(III.F.10).

For clarity, the operator-completion step uses three concrete facts from that
proof. The finite initialized norm obeys

\[
 \mathbb P(\|W^{(2)}_0\|_{\rm op}>10)
 \le2\,9^{2n}e^{-100n/8}\longrightarrow0.
\]

Second-moment convergence passes the inequality
\(\|W^{(2)}_0v\|_2/\sqrt n\le10\|v\|_2/\sqrt n\)
to every rational combination of generated nodes. Exact finite linear
identities and zero squared differences make the limiting assignment
linear and well-defined on its \(L^2\) classes. Generated smooth cylinder
functions are dense in each generated \(L^2\) space: cylinder simple
functions approximate measurable functions, bounded continuous functions
approximate finite-dimensional Borel functions in \(L^2\), and the included
smooth functions approximate those on compact boxes, with tails removed by
truncation. Thus the assignment extends to a bounded map \(A_0\), of norm
at most 10. The reverse assignments extend in the same way. Passing the
exact finite normalized identity

\[
 v^TW^{(2)}_0h/n=((W^{(2)}_0)^Tv)^Th/n
\]

through the finite-program theorem and then through density identifies the
reverse map with \(A_0^*\).

This language can be fixed independently of the training law. Arbitrary
real directions \(u\in S^1\) are limits of rational linear combinations of
the retained root pair; their initial projections have the joint law
\(\mathbb E[(w_0\cdot u)(w_0\cdot v)]=u\cdot v\).
Arbitrary real coefficients in each separately fixed program are obtained
by rational approximation. For continuous coordinate instructions of at
most linear growth, including the backward products in (T1), A.1 supplies
the extension by smooth clipping and \(L^2\) completion. Its proof chooses
one fixed approximation before taking width to infinity and then removes
the approximation, so no growing-program assertion is introduced here.
The response formulas for these fixed neural programs are those in A.2:
bounded derivatives of tanh and its derivative meet the stated hypotheses.

As a result all rational finite laws and rational-mesh Euler calculations,
their finite unions and full first-row updates belong to one common action
realization. A countable list of additional finite laws may equally be
included. Alternatively the preceding completion represents each of their
fixed calculations directly. This construction also includes any finite
list of passive input directions. There is no data-law-dependent arbitrary
extension of the initialized operator and no comparison of a finite matrix
to a population operator in operator norm.

Different causal enumerations have the same finite generated laws because
their finite arrays agree. Their generated spaces are therefore identified
by the \(L^2\) isometry sending each named coordinate expression to its
counterpart. The isometry preserves coordinate operations and intertwines
the actions and adjoints. This is the precise canonical-realization claim.

##### 3. Continuity of the field and integration against a law

Use the common ball B=24, velocity bound V and first-exit interval (T4)–(T5).
The forward state/input comparison, including predictions, is (T8)–(T9).
These estimates hold for all laws and do not involve Gram inverses.

The backward fields are jointly continuous in \((\theta,x)\) with values
in the corresponding \(L^2\) spaces. Here is the necessary product detail.
For \(Z_j\to Z\), \(Q_j\to Q\) in \(L^2\), and bounded continuous \(b\),

\[
 b(Z_j)Q_j-b(Z)Q=b(Z_j)(Q_j-Q)+(b(Z_j)-b(Z))Q.
\]

The first term tends to zero in \(L^2\). For the second, restrict to
\(|Q|\le M\), use bounded convergence in probability there, and bound the
complement by \(2\|b\|_\infty\|Q1_{|Q|>M}\|_2\).
Let \(j\to\infty\) and then \(M\to\infty\). Apply this first to
\(\delta^2\), then use operator/adjoint continuity for \(P^1\), and then
apply it to \(\delta^1\). The same argument works when \(x_j\to x\).
Compactness of the circle shows that for \(\theta_j\to\theta\) this
continuity is uniform over \(x\): a contrary sequence has a subsequence of
inputs converging to one input, contradicting joint continuity.

Each integrand in (T2) is therefore continuous as a Banach-valued function
of \(z=(x,y)\) on the compact data space. Its range is compact and hence
separable; uniform boundedness makes it Bochner integrable. This argument
also resolves measurability despite the possibly nonseparable ambient
operator space. The middle integrand can in fact be integrated in the
Hilbert–Schmidt norm, since
\(\|v\otimes h\|_{\rm HS}=\|v\|_2\|h\|_2\) and the corresponding
rank-one difference bound is the same in that norm. Thus every learned
increment of a strong solution constructed below is Hilbert–Schmidt;
\(A_0\) itself need not be.

We shall use joint continuity

\[
 \theta_j\to\theta,\quad\mathcal W_1(\mu_j,\mu)\to0
 \quad\Longrightarrow\quad
 F_{\mu_j}(\theta_j)\to F_\mu(\theta)\text{ in }\mathcal E.
\tag{P9}
\]

To prove it, uniform continuity just established makes the change in the
integrand caused by \(\theta_j\to\theta\) uniformly small on \(\mathcal Z\).
For the remaining fixed continuous Banach-valued function \(g\), take a
coupling with mean distance \(q_j+o(1)\to0\). If
\(\omega_g(a)=\sup_{d(z,z')\le a}\|g(z)-g(z')\|\), then

\[
 \left\|\int g\,d\mu_j-\int g\,d\mu\right\|
 \le\omega_g(a)+2\|g\|_\infty(q_j+o(1))/a.
\]

First let \(j\to\infty\) and then \(a\downarrow0\). This proves (P9)
without invoking differentiability of a nonlinear map on all of \(L^2\).

##### 4. Finite reference flows and the comparison estimate

For a fixed finite probability law
\(\nu=\sum_{a=1}^m\omega_a\delta_{(x_a,y_a)}\), discard zero weights
and combine identical atoms if desired. For each rational mesh \(\Delta>0\)
construct the full-state Euler recursion

\[
 \theta^\Delta_{\nu,k+1}=\theta^\Delta_{\nu,k}
                 +\Delta F_\nu(\theta^\Delta_{\nu,k}),\qquad
 \theta^\Delta_{\nu,0}=\theta_0,
\tag{P10}
\]

and interpolate the three parameters linearly between its grid points.
At every separately fixed mesh there are finitely many calls. Expanding
the learned middle action as a finite sum of rank-one increments rewrites
these calls using only \(A_0,A_0^*\), coordinate maps and deterministic
population contractions. These are the fixed neural programs represented
in Section 2. Each contraction is computed from earlier generated nodes;
no prospective trajectory value is supplied. The full first-row update
is included literally in this recursion. Projection on \(u_b\) gives
the first equation of C.2, since \(u_a\cdot u_b=G_{ab}\). Thus its
active fields obey precisely the equations to which that lemma applies,
without requiring the active directions to span \(\mathbb R^2\).
All full-row Euler velocities have the bound (T4)–(T5).

The C.2 response bound applies here with \(L=d=2\),
\(|G_{ab}|\le1\), marginal first preactivation variance one, zero population
readout, bounded tanh and its first two derivatives, and all mobilities one.
The preliminary source RMS and residual bounds are (T4). Its complete
weighted argument supplies numbers \(\gamma_0,C_0,T_{\rm response}>0\), depending
only on these bounds and \(Y\), for which every separately fixed finite law
and all its Euler mesh states satisfy

\[
 \sup_{\Delta}\sup_{k\Delta\le T_*}\max_a
 \mathbb E_1 e^{\gamma_0|P^1_{\theta^\Delta_{\nu,k}}(x_a)|^2}\le C_0,
 \qquad \sup_{\Delta}\sup_{k\Delta\le T_*}
 \mathbb E_2 e^{\gamma_0|c^\Delta_{\nu,k}|^2}\le C_0,
\tag{P11}
\]

where
\(0<T_*\le\min(T_{\rm ball},T_{\rm response})\).
The constants do not depend on \(m\), the atom weights or Gram rank.
The C.2 proof uses weighted sums of individual subGaussian marginal bounds;
it makes no estimate of a maximum over a data set or Gaussian history.
The full-row updates change none of its active projected recursions.
C.2's hypotheses therefore remain exactly verified.

For later use, define the *integrated individual tail norm*

\[
 \tau_\nu(\bar\theta,R)=
 \|\bar c1_{|\bar c|>R}\|_2+
 \int\|P^1_{\bar\theta}(x)1_{|P^1_{\bar\theta}(x)|>R}\|_2\,d\nu(x,y).
\tag{P12}
\]

Section C.4.1 proves, at finite width and on these population spaces,

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{\mathcal E}
 \le C(1+R)\bigl(D(\theta,\bar\theta)+\mathcal W_1(\mu,\nu)\bigr)
       +C\tau_\nu(\bar\theta,R).
\tag{P13}
\]

Its proof couples \((x,y)\) with \((x',y')\), uses (T8)–(T9), cuts off only
the reference backward factors, and includes the explicit changed input
factor in \(\delta^1(x)u-\bar\delta^1(x')u'\).
In particular no Gaussian tail bound for \(\theta\) is a hypothesis.
From (P11) the Euler-grid reference tails are bounded by
\(C e^{-cR^2}\). Compare two Euler interpolants for the same finite law.
At time \(t\), each assigned velocity uses its preceding grid state.
Their grid-state distance is at most their interpolant distance plus
\(V(\Delta+\Delta')\), by (T4)–(T5). Apply (P13) at these grid states,
integrate, and use scalar Gronwall. With fixed \(a,c,C>0\),

\[
 \sup_{t\le T_*}D(\theta^\Delta_\nu(t),\theta^{\Delta'}_\nu(t))
 \le Ce^{aR}\bigl((1+R)(\Delta+\Delta')+e^{-cR^2}\bigr).
\tag{P13a}
\]

Fix \(R\), send the meshes to zero, and then send \(R\to\infty\).
The paths are Cauchy in the complete full-state path space. Their limit
\(\theta_\nu\) satisfies the strong integral equation (P5): the
preceding grid states converge uniformly to this continuous path, and
continuity of \(F_\nu\), uniformly on this convergent family of compact
path ranges, passes their integrated assigned velocities to
\(\int_0^t F_\nu(\theta_\nu(s))ds\). This also proves strong \(C^1\)
regularity. At a fixed time, the reference backward fields at preceding
grid states converge in \(L^2\) by Section 3. Taking an almost surely
convergent subsequence and applying Fatou to (P11) transfers its bounds
to the finite-law flow. Hence
\(\tau_\nu(\theta_\nu(t),R)\le C e^{-cR^2}\), uniformly in time.

Integrating (P13) for two resulting finite-law solutions from their common
initial state now gives

\[
 \sup_{t\le T_*}D(\theta_\lambda(t),\theta_\nu(t))
 \le C e^{aR}\bigl((1+R)\mathcal W_1(\lambda,\nu)+e^{-cR^2}\bigr),
 \qquad R\ge1.
\tag{P14}
\]

For completeness, set \(L_R=C(1+R)\) and
\(b_R=C(1+R)q+C e^{-cR^2}\). The integral inequality is
\(D(t)\le\int_0^t(L_RD(s)+b_R)ds\).
Iterating it, or differentiating its scalar upper comparison, gives
\(D(t)\le b_R t e^{L_Rt}\), which is (P14).

##### 5. Completion in the training law and identification of the equation

Every probability measure on the compact \(\mathcal Z\) admits finitely
supported approximations \(\nu_j\) with \(\mathcal W_1(\nu_j,\mu)\le1/j\):
take a finite \(1/j\)-net, partition measurably by the first nearest eligible
net point, and move the measure in each cell to that point. The transport
cost is at most \(1/j\); no boundary-zero assumption is needed. One may
choose the net points from a fixed countable dense set of input angles and
labels. The finite laws' weights need not be rational.

For fixed \(R\), (P14) bounds the limiting Cauchy error by
\(C e^{aR-cR^2}\). Let \(R\to\infty\). Thus \(\theta_{\nu_j}\) is
Cauchy in \(C([0,T_*];\mathcal E)\), which is complete. Let
\(\theta_\mu\) be its limit. It stays in the common ball and its forward
fields converge uniformly in time and input by (T8)–(T9).

The vector fields converge uniformly in time:

\[
 \sup_{t\le T_*}\|F_{\nu_j}(\theta_{\nu_j}(t))-
                         F_\mu(\theta_\mu(t))\|_{\mathcal E}\to0.
\tag{P15}
\]

Indeed a contrary subsequence has times \(t_j\to t\). Uniform state
convergence and continuity of the limiting curve give
\(\theta_{\nu_j}(t_j)\to\theta_\mu(t)\), so (P9) contradicts the
nonvanishing field difference. Equation (P15) passes the finite-law integral
equations to (P5). The field there is continuous in time, so the result is
a strongly \(C^1\) solution. This proves existence of the autonomous
equation, rather than only Cauchy convergence of its scalar predictions.

It remains to transfer the tails in exactly the strength needed for
uniqueness. For fixed \(t\), backward continuity in Section 3 gives

\[
 \sup_x\|P^1_{\nu_j}(t,x)-P^1_\mu(t,x)\|_2\to0,
 \qquad \|c_{\nu_j}(t)-c_\mu(t)\|_2\to0.
\tag{P16}
\]

For \(M<\infty\), the function
\(b_M(s)=\min\{e^{\gamma_0s^2},M\}\) is bounded and globally Lipschitz.
Equation (P16) therefore shows uniform-in-input convergence of its
expectations. The function
\(x\mapsto\mathbb E_1 b_M(P^1_\mu(t,x))\) is continuous, so weak
convergence of \(\nu_j\) passes its integral to \(\mu\). From (P11),

\[
 \int\mathbb E_1 b_M(P^1_\mu(t,x))\,d\mu(x,y)\le C_0.
\]

Let \(M\uparrow\infty\) by monotone convergence. The same argument for
the readout proves

\[
 \sup_{t\le T_*}\int\mathbb E_1 e^{\gamma_0|P^1_\mu(t,x)|^2}\,d\mu(x,y)
 \le C_0,
 \qquad
 \sup_{t\le T_*}\mathbb E_2 e^{\gamma_0|c_\mu(t)|^2}\le C_0.
\tag{P17}
\]

The supremum is legitimate because the preceding argument holds separately
for every \(t\) with the same constants. No common almost-sure bound on
all times or inputs is asserted. In particular (P17) is an *integrated*
input-law bound, not a pointwise continuum-wide subGaussian statement.

The elementary bound
\(s^2 1_{|s|>R}\le C e^{-\gamma_0R^2/2}e^{\gamma_0s^2}\), followed by
Cauchy–Schwarz over \(\mu\), implies

\[
 \sup_{t\le T_*}\tau_\mu(\theta_\mu(t),R)\le C e^{-cR^2}.
\tag{P18}
\]

This is precisely the reference-tail estimate used by (P13).

##### 6. Uniqueness, restart and quantitative law continuity

Let \(\widetilde\theta\) be any other strong solution of (P5) on the
same initialized spaces with initial state \(\theta_0\). Its components
are continuous in the topology (T3), its integrals have the meaning in (T2),
and no tail condition is imposed on it. The first-exit bound (T5)
keeps it in the common ball. Apply (P13) with \(\mu=\nu\), constructed
\(\theta_\mu\) as reference, and (P18). Gronwall gives

\[
 \sup_{t\le T_*}D(\widetilde\theta(t),\theta_\mu(t))
 \le C e^{aR-cR^2}\quad\hbox{for every }R\ge1.
\]

Sending \(R\to\infty\) proves equality. It also proves independence of
the chosen finite-law approximating sequence: (P14) applied across two
approximating sequences gives the same conclusion directly.

For any two arbitrary laws, (P13) and (P18) prove (P14) with
\((\lambda,\nu)\) replaced by \((\mu,\nu)\). For
\(0<q=\mathcal W_1(\mu,\nu)\le1\), choose

\[
 R=K\sqrt{\log(e/q)},\qquad K\ge1,\qquad cK^2\ge2.
\]

Then \(e^{-cR^2}\le q^2\), while
\(1+K\sqrt{\log(e/q)}\le C e^{C\sqrt{\log(e/q)}}\).
Substitution yields

\[
 \sup_{t\le T_*}D(\theta_\mu(t),\theta_\nu(t))
 \le Cq\exp\bigl(C\sqrt{\log(e/q)}\bigr).
\tag{P19}
\]

Constants depend only on \(Y\) and the frozen model and support bounds.
For \(q=0\), the laws coincide and the solutions are identical; the right
side is interpreted as its zero limit. For \(q>1\), the common ball gives
\(D\le6B\), and in particular \(D\le6Bq\). The training-law distance \(\mathcal W_1\) is at most \(2+2Y\).

Equation (T8)–(T9) now proves the requested whole-input prediction bound and,
more strongly, the same modulus for the \(L^2\) displacement between
the two forward hidden fields, uniformly over time and the circle.
For \(q>1\) the prediction difference is at most \(2B\).

The equation depends only on the current \((w,A,c)\), its coordinate
functions and the fixed training law. At a time \(s<T_*\), restrict the
constructed path to \([s,T_*]\). The preceding uniqueness argument applied
on this interval, with initial distance zero and this path as reference,
gives unique restart among strong solutions staying on the common ball.
No extra response history must be supplied. More intrinsically, close the
current full-row coordinates, readout, actions and adjoints under the same
coordinate operations; their generated \(L^2\) spaces contain their
subsequent Euler constructions and limits. To justify this last statement
without presupposing Gaussian tails for restarted Euler trajectories,
compare such an Euler trajectory directly against the existing solution
as reference. At each time its preceding grid state differs from its
interpolated state by at most \(V\Delta\). Equation (P13), with reference
tails (P18) at that time, gives the upper error
\(Ce^{aR}((1+R)\Delta+e^{-cR^2})\). Sending \(\Delta\to0\) and then
\(R\to\infty\) proves convergence to the reference continuation. The
Euler law integrals also stay in the generated spaces: their continuous
integrands are limits of finite weighted sums using a dense countable
set of input directions, and the generated spaces are closed.
Equal current generated joint laws define the isometry described in
Section 2 and intertwine the equation. Uniqueness identifies their future
laws. This is a restart claim
on the constructed local interval, not global-time well-posedness from
every arbitrary operator state.



#### C.4.3. Actual GD, simultaneous limits and statistics

##### 1. Uniform finite initialization and the common ball

Use `S0=11`, `B=24`, the velocity bound V and the first-exit interval
(T5) from Section C.4.1. The event bounding all initialized block norms
has probability tending to one and depends only on the initialization.
In particular the actual finite readout satisfies

\[
 \mathbb E\frac{\|W^{(3)}_{n,0}\|_2^2}{n}=n^{-2}.
\tag{A1}
\]

The bounds (T4)–(T5) apply to every training law and every sufficiently
small actual GD mesh. Use a fixed enlarged comparison ball for the proxy
below, reducing the common T_* if needed. This keeps every constant
independent of the actual dataset, width and step; no finite-GD energy
inequality is assumed.

##### 2. The fixed finite reference proxy

Fix a finite probability law
`nu=sum_(b=1)^J omega_b delta_(u_b,y_b)`, positive weights summing to one,
and a positive rational proof mesh Delta. These remain fixed as n tends
to infinity. Let the population Euler states for nu and Delta be denoted
`Theta^(nu,Delta)_s`. They use zero initial population readout.

Use the same initialized first and middle arrays as actual GD. Construct
the following finite deterministic-coefficient oracle: replace its scalar
residuals and within-layer contractions by the corresponding population
Euler values, expand the trained middle matrix into initialized action
plus accumulated rank-one updates, and perform the resulting finite list
of actions and coordinate operations. Denote its nodes by superscript o.
The oracle readout root is zero. Define actual finite proxy parameters by

\[
\begin{split}
 \bar W^1_{n,k}&=W^1_{n,0}
 -2\Delta\sum_{s<k,b}\omega_b r_{b,s}
               \delta^{1,o}_{b,s}u_b^T,\\
 \bar W^2_{n,k}&=W^2_{n,0}
 -\frac{2\Delta}{n}\sum_{s<k,b}\omega_b r_{b,s}
               \delta^{2,o}_{b,s}(h^{1,o}_{b,s})^T,\\
 \bar W^3_{n,k}&=W^3_{n,0}
 -2\Delta\sum_{s<k,b}\omega_b r_{b,s}h^{2,o}_{b,s}.
\end{split}\tag{A3}
\]

Interpolate these parameters linearly. In particular the proxy and actual
network have exactly the same initial arrays, including the random readout.
The small readout in (A3) is an additive parameter term, and not a change to
the actual algorithm. Its RMS tends to zero by (A1) and Markov's inequality.

At fixed `(nu,Delta)` the program has finitely many instructions. The
fixed-program theorem III.F.1–7 and global-nonlinear A.1–2 apply: tanh is
smooth with bounded first two derivatives, the gates are bounded smooth
functions times L2 fields, and the roots are Gaussian. Every same-layer
tuple and second moment of oracle nodes converges in probability. For a
proxy middle action applied to an oracle node, its discrepancy from the
prescribed oracle action is a finite sum of terms

\[
 -2\Delta\omega_b r_{b,s}\delta^{2,o}_{b,s}
 \left[\frac{(h^{1,o}_{b,s})^Th^{1,o}_{a,k}}n
             -\mathbb E_1(H^1_{b,s}H^1_{a,k})\right].
\tag{A4}
\]

Each bracket tends to zero; each multiplying node has bounded RMS in
probability. The transpose expansion has the same form with the corresponding
backward contraction. First-row oracle consistency is exact for its input
projections, since (A3) retains the whole root row and exact factors u_b.
Forward induction and (A4) give consistency of recomputed proxy forward
fields. Recomputed proxy backward fields converge by descending induction:
for any reference oracle field p, with the fixed activation phi=tanh,

\[
 \|[\phi'(z)-\phi'(\bar z)]p\|_2
 \le 2R\|z-\bar z\|_2+2\|p\mathbf1_{|p|>R}\|_2.
\tag{A5}
\]

For each fixed cutoff take n to infinity using oracle cutoff second moments;
then remove that cutoff. This controls the only unbounded multiplier. The
readout discrepancy in this step includes exactly the vanishing RMS in (A1).
Thus assigned proxy velocities differ from `F_nu(barTheta_n,k)` by o_P(1)
uniformly over the fixed finite coarse grid in D_n's block norm.

More precisely, for each fixed cutoff R, the reference tail sum satisfies

\[
 \max_k\sum_b\omega_b\sum_{\ell=1}^2
 \frac{\|\bar P^\ell_{b,k}
             \mathbf1_{|\bar P^\ell_{b,k}|>R}\|_2}{\sqrt n}
 \le C e^{-cR^2}+o_{\mathbb P}(1).
\tag{A6}
\]

Here and subsequently an inequality with o_P(1) means its positive excess
over the deterministic bound tends to zero in probability. To verify (A6)
without a discontinuous-test assertion, use
`||v 1_|v|>R|| <= 2||v-p|| + 2||p 1_|p|>R/2||`, and dominate the latter
by a continuous positive-part cutoff at R/4. The oracle cutoff moments
converge; C.2 bounds their population values by a Gaussian tail. Constants
are enlarged and c reduced once. These are individual weighted tails.

The proxy full-row and readout norms and its rank-one velocity norms are
bounded, with limiting upper bounds uniform in Delta and nu. For the middle
block use its initial norm plus the sum of the normalized rank-one norms
in (A3); their limiting total is bounded by the integral velocity bound.
For first rows and readout use the same triangle inequality and the full
root-row second moment. These observations place the proxy in a fixed
enlarged comparison ball and bound its interpolation speed independently
of Delta, with probability tending to one at fixed `(nu,Delta)`.

##### 3. Direct comparison with arbitrary growing data and every vanishing step

Let lambda_k be arbitrary deterministic finite probability laws such that
`W1(lambda_k,mu)->0`, let `n_k->infinity`, and let `eta_k->0`. The atom count
and weights of lambda_k are unrestricted. Choose the fixed reference nu above
so that `W1(mu,nu)<=delta`. At each time compare actual GD's preceding fine
state with the proxy's preceding coarse state. Their D_n distance is bounded
by their interpolant distance plus `C(eta_k+Delta)`. The transport estimate
of Section C.4.1, (A6), and the assigned-velocity error give

\[
\begin{split}
\sup_{t\le T_*}D_{n_k}(\Theta^{GD}_{k}(t),\bar\Theta^{nu,\Delta}_{n_k}(t))
\le C e^{aR}\bigl[(1+R)
 \{\eta_k+\Delta+\mathcal W_1(\lambda_k,\nu)\}
 +e^{-cR^2}+o_{\mathbb P}(1)\bigr].
\end{split}\tag{A7}
\]

This follows by integrating assigned velocities and iterating
`E(t)<=C(1+R) integral_0^t E(s)ds + b`; the exponential series bounds E by
`b exp(C(1+R)T_*)`. Initial discrepancy is zero. The o_P(1) is at fixed
`(nu,Delta,R)`. The first-exit ball in section 1 already bounds actual GD
using only initialized arrays; no Gaussian tail theorem is applied to it.
In particular no maximum over lambda_k's observations or fine GD history
occurs. The same proof would cover GF with eta_k=0.

On the comparison ball, all forward fields in RMS and scalar predictions
are uniformly Lipschitz in the full state and in u, and uniformly Lipschitz
in time along parameter interpolants of bounded speed. For instance
`||z1(u)-z1(v)||<=B|u-v|`,
`||z2(u)-z2(v)||<=B²|u-v|`, and `|f(u)-f(v)|<=B³|u-v|`.
The normalized finite versions are identical. A fixed finite input net,
then a fixed finite time net, therefore transfers fixed-program proxy
prediction convergence to

\[
 \sup_{t\le T_*,u\in S^1}
 |\bar f^{nu,\Delta}_n(t,u)-f^{nu,\Delta}(t,u)|
 \longrightarrow0\quad\hbox{in probability}.
\tag{A8}
\]

At each chosen time and passive input, append its forward evaluation to the
same fixed oracle program. Proxy recomputation follows (A4); at an interior
coarse time the parameters have the affine coefficients from (A3). This
identifies precisely the prediction of the population parameter interpolant,
rather than interpolation of predictions. Its Lipschitz bounds justify the
two nets and remove them after the fixed-program width limit.

The population comparison gives

\[
 \sup_t D(\Theta^{nu,\Delta}(t),\Theta_\mu(t))
 \le C e^{aR}\{(1+R)(\Delta+\delta)+e^{-cR^2}\}.
\tag{A9}
\]

Combining (A7)–(A9), `W1(lambda_k,nu)<=W1(lambda_k,mu)+delta`, and forward
Lipschitz continuity proves the required convergence. The order is explicit:
take k to infinity at fixed delta, fixed finite nu, fixed Delta and R;
send Delta to zero; send delta to zero through finite reference laws;
then send R to infinity. Equivalently, for a desired positive error choose
R first sufficiently large for the Gaussian remainder, then delta and Delta
small enough, and only afterwards take k large. No program whose length
grows with k is passed through a fixed-program theorem. There is no
comparison in operator norm between different spaces or different widths.

##### 4. Random observations, the two risks, and their limits

For a law rho and bounded predictor g define

\[
 R_\rho(g)=\int(g(x)-y)^2\,\rho(dx,dy),\qquad
 \widehat R_S(g)=\frac1m\sum_{i=1}^m(g(x_i)-y_i)^2.
\tag{A10}
\]

For any fixed bounded state ball these integrands have a uniform Lipschitz
constant on the joint observation space: if `|g|<=B` and g has input
Lipschitz constant L in u, the difference of squared residuals is at most
`2(B+Y)(L|u-v|+|y-z|)`. Thus for deterministic lambda_k as above, uniformly
on `[0,T_*]`, both the actual empirical training loss
`R_lambda_k(f_(n_k,eta_k,lambda_k)(t))` and its population risk under mu
converge in probability to `R_mu(f_mu(t))`. Indeed predictor uniform error
changes either risk by at most `2(B+Y)` times that error on the initial
high-probability ball; changing lambda_k to mu for the limiting predictor
costs at most `C W1(lambda_k,mu)`. Also
`R_lambda_k(f_lambda_k(t)) -> R_mu(f_mu(t))` and
`R_mu(f_lambda_k(t)) -> R_mu(f_mu(t))` uniformly in time by law stability.

For iid observations of size m from mu, `W1(mu_S,mu)->0` in probability.
Here is an elementary proof sufficient for arbitrary atomic or singular mu.
Partition the compact observation space into finitely many Borel cells of
diameter at most epsilon, and choose a representative in each nonempty cell.
Push both laws to these representatives. Each push costs at most epsilon.
If p_j are true cell masses and p_hat_j empirical masses, their discrete
W1 distance is at most `(diam Z)/2 sum_j |p_hat_j-p_j|`: match the common
mass at each representative and couple remaining masses arbitrarily.
Each empirical cell mass has variance at most 1/(4m), so this finite sum
tends to zero in probability (even in mean). Then let epsilon go to zero.
No boundary-zero partition is needed, since the observations are iid and
the same fixed Borel cells are used for their indicators.

The proof of (A7) is uniform in the actual training law on the event
`W1(mu_S,mu)<=epsilon`: its remaining random errors involve only the fixed
reference program and initialized arrays. Initialization independent of S
has the required unconditional Gaussian law for this reference and the
required joint model. A union bound with the event just proved therefore
extends (A7)–(A10) to arbitrary `n_k,m_k->infinity`, `eta_k->0`. This does
not require a uniform-in-data fixed-program theorem, or a rate for W1.

##### 5. Sample replacement and the exactly ordered expected gap

Let `rho(q)=C q exp(C sqrt(log(e/q)))` for `0<q<=1`, with constants enlarged
as in Section C.4.2, and rho(0)=0. For q>1 use the uniform predictor bound.
The observation space has diameter at most `L_Z=2+2Y`. If S and S' differ
in one observation, match their other m-1 observations and couple the last
two. This gives `W1(mu_S,mu_S')<=L_Z/m`. Law stability and the uniform
predictor bound imply, for every m>=1,

\[
 \sup_{t\le T_*,x\in\sqrt2S^1}|f_S(t,x)-f_{S'}(t,x)|
 \le \beta_m:=\frac{C}{m}\exp(C\sqrt{\log(em)}).
\tag{A11}
\]

For m>=L_Z use the unspecialized cutoff estimate with `q<=L_Z/m`.
Taking `R=K sqrt(log(em))` gives (A11) directly. Finitely many smaller m are
covered by enlarging C. Coincident data, identical replacement and q=0
are included. These are the deterministic infinite-width learning maps
`f_S=f_mu_S`; no quantitative finite-width replacement estimate follows.

For any observation z=(x,y), the squared-loss difference for two such
predictors is at most `2(B+Y) beta_m`, uniformly in z and time. Let
`S=(Z_1,...,Z_m)` be iid from mu and let `Z_i'` be an independent copy.
Write `S^(i)` for S with coordinate i replaced by `Z_i'`. All quantities
are measurable: the law-to-predictor map is continuous by law stability,
empirical-law formation is continuous in each observation, and the risks
are integrals of bounded continuous functions. With
`ell(g,z)=(g(x)-y)^2`, independence gives, at each fixed deterministic t,

\[
\begin{split}
\mathbb E_S[R_\mu(f_S(t))-\widehat R_S(f_S(t))]
 &=\frac1m\sum_i\mathbb E_{S,Z_i'}
      [\ell(f_S(t),Z_i')-\ell(f_S(t),Z_i)]\\
 &=\frac1m\sum_i\mathbb E_{S,Z_i'}
      [\ell(f_{S^{(i)}}(t),Z_i)-\ell(f_S(t),Z_i)].
\end{split}\tag{A12}
\]

The second equality exchanges the iid pair `(Z_i,Z_i')` while leaving all
other observations fixed. It uses the fact that the algorithm is the same
measurable empirical-law map for both samples. Every summand has absolute
value at most `2(B+Y) beta_m` by (A11). Taking absolute value of the
expectation and then the supremum over deterministic t yields

\[
 \sup_{t\le T_*}\left|\mathbb E_S
  [R_\mu(f_S(t))-\widehat R_S(f_S(t))]\right|
 \le\frac{C}{m}\exp(C\sqrt{\log(em)}).
\tag{A13}
\]

No expectation of an absolute gap or a time supremum has been taken.
This conclusion gives neither excess risk, useful risk reduction,
endpoint selection, nor superiority over another learning model.

##### 6. Representation observables in the joint limit

For ell=1,2 let

\[
 J_{\ell,n}(t;\lambda)=\int
 \frac{\|h^\ell_n(t,x)-h^\ell_n(0,x)\|_2^2}{n}\,\lambda(dx,dy).
\tag{A14}
\]

The integrand is bounded by 4, is uniformly Lipschitz in input on the ball,
and its change between two same-width states with the same initialization
is at most C D_n by the forward estimates and
`| ||v||²-||w||² | <= (||v||+||w||)||v-w||`.
For the fixed proxy its value at finitely many inputs and times converges
by joint oracle second moments including time zero. Input and time nets
then give uniform convergence of the whole integrand to the population
Euler integrand, just as in (A8). Coupling the input laws and using (A7)
therefore proves

\[
 \sup_{t\le T_*}|J_{\ell,n_k}(t;\lambda_k)-J_{\ell}(t;\mu)|
 \longrightarrow0\quad\hbox{in probability}.
\tag{A15}
\]

This holds for the deterministic and independent iid cases above. It
supplies the width-persistent representation displacement required by
Section C.4.4. It asserts no convergence of individual finite neurons to
population coordinates and requires no such artificial coupling.


#### C.4.4. An open family with hidden representation motion

##### 1. State and observables

Use the common fields (T1) from Section C.4.1. Write
`H_0^(ell)(x)` for their common initialized activations, and retain the
notation `W^(2)=A`, `W^(3)=c` in this proof unit.
For `ell=1,2` define the training-input averaged squared displacement and RMS
displacement

\[
 J_\ell(\mu,t)=\int_{\mathcal Z}
 \|H_\mu^{(\ell)}(t,x)-H_0^{(\ell)}(x)\|_{L^2(\Omega_\ell)}^2
 \,\mu(dx,dy),\qquad
 A_\ell(\mu,t)=\sqrt{J_\ell(\mu,t)}.                       \tag{1}
\]

The coordinate pairing at the two times is the same neuron population,
not an arbitrary coupling of the two activation marginal laws. Since tanh
is bounded by one, `0<=J_ell<=4`.

The common bounded-state interval supplies a deterministic `B>=1` such that
`||w_mu(t)||_2<=B` and `||W_mu^(2)(t)||_op<=B` for all laws and times under
consideration, including initialization. The 1-Lipschitz property of tanh
then gives, with `rho(x,x')=|x-x'|/sqrt(2)`,

\[
 \|H_\mu^{(1)}(t,x)-H_\mu^{(1)}(t,x')\|_2\le B\rho(x,x'),
 \qquad
 \|H_\mu^{(2)}(t,x)-H_\mu^{(2)}(t,x')\|_2\le B^2\rho(x,x').   \tag{2}
\]

Thus one may use `K=B^2` in both layers, for all laws, times and initialization.
These estimates use the full first-row field; controlling only projections
on a fixed training list would not justify them.

##### 2. An explicit reference law and actual-flow expansion

Fix `y_0=Y/2>0` and

\[
 x_1=\sqrt2(1,0),\qquad x_2=\sqrt2(0,1),\qquad
 \mu_0=\tfrac12\delta_{(x_1,y_0)}+
       \tfrac12\delta_{(x_2,y_0)},\qquad p=y_0/2=Y/4.          \tag{3}
\]

The Gram is `G=I_2`, and `p` is the label multiplied by its atom weight.
All constants below may depend on this reference and on `Y`.
Suppress `mu_0` in the notation. Set

\[
 h_a=\tanh g_a,\qquad q_0=\mathbb E\tanh^2 g_1>0,
 \qquad \xi_a=W_0^{(2)}h_a\quad (a=1,2).
\]

Oddness and independence of the lower Gaussian roots give
`E[h_a h_b]=q_0 1_(a=b)`. The first forward Gaussian calculation gives
independent `xi_1,xi_2~N(0,q_0)` in the second population. This calculation
can also be read directly at finite width: conditioned on the first-layer
arrays, each row output is Gaussian with covariance
`(h_a^T h_b/n)_(a,b)`, which converges to `q_0 I_2`; row averages of bounded
continuous functions concentrate conditionally, and Gaussian second moments
give the same conclusion for quadratic-growth tests. No trained matrix has
been replaced by an independent map.

With `phi=tanh` and `phi'(s)=sech^2(s)`, define the following fields,
each in its displayed layer:

\[
 S=p(\tanh\xi_1+\tanh\xi_2),\qquad U_a=S \phi'(\xi_a)
       \quad\hbox{in }L^2(\Omega_2),
\]
\[
 P_a=(W_0^{(2)})^*U_a,\qquad
 T_a=p \phi'(g_a)P_a,\qquad C_a=p \phi'(g_a)^2P_a
       \quad\hbox{in }L^2(\Omega_1),
\]
\[
 M_a=pq_0U_a,\qquad R_a=M_a+W_0^{(2)}C_a,\qquad
 E_a=\phi'(\xi_a)R_a
       \quad\hbox{in }L^2(\Omega_2).                       \tag{4}
\]

All these fields are well defined: `S,U_a` are bounded, the initial action
and its adjoint are bounded on the generated `L2` spaces, and every remaining
multiplier is bounded. The exact weighted physical equations are

\[
 \dot Z_a^{(1)}=-\sum_b G_{ab}r_b\delta_b^{(1)},\qquad
 \dot W^{(2)}=-\sum_b r_b\delta_b^{(2)}\otimes H_b^{(1)},
 \qquad \dot W^{(3)}=-\sum_b r_bH_b^{(2)},                 \tag{5}
\]

where `r_b=f_b-y_0`, `delta_b^(2)=W^(3)phi'(Z_b^(2))` and
`delta_b^(1)=phi'(Z_b^(1))(W^(2))*delta_b^(2)`. The factors in (5) are
`-2 omega_b=-1`, since this is a two-point mean loss.

The strong integral equations and continuity give

\[
 \begin{aligned}
 W^{(3)}(t)&=2tS+o_{L^2}(t),&
 \delta_a^{(2)}(t)&=2tU_a+o_{L^2}(t),\\
 \delta_a^{(1)}(t)&=2t \phi'(g_a)P_a+o_{L^2}(t),&
 Z_a^{(1)}(t)-g_a&=2t^2T_a+o_{L^2}(t^2),\\
 H_a^{(1)}(t)-h_a&=2t^2C_a+o_{L^2}(t^2),&
 W^{(2)}(t)-W_0^{(2)}
   &=2t^2\sum_b p U_b\otimes h_b+o_{\rm op}(t^2),\\
 Z_a^{(2)}(t)-\xi_a&=2t^2R_a+o_{L^2}(t^2),&
 H_a^{(2)}(t)-\tanh\xi_a&=2t^2E_a+o_{L^2}(t^2).
 \end{aligned}                                                        \tag{6}
\]

Here is the justification of every passage needed for (6). Divide the
readout integral in (5) by `t` and use `r_b(0)=-y_0`, continuity and
`H_b^(2)(0)=tanh xi_b`. The limit is `y_0 sum_b tanh xi_b=2S`.
If `V_t->V` in `L2` and `a_t->a` in probability with uniformly bounded
`a_t`, then `a_t V_t->a V` in `L2`: bound the part multiplying `V_t-V`
by the uniform multiplier bound, and split the part multiplying `V` at
`|V|<=M`, then let `M` increase. Apply this fact to `phi'(Z_a^(2)(t))`, and
then to the continuous adjoint and lower gate. It gives the two backward
limits in (6). Integrating `s` times a field converging in `L2` uses
`integral_0^t s ds=t^2/2`, which proves the lower preactivation and matrix
limits, including their factors `2p`.

For either activation difference use the identity

\[
 \frac{\tanh(z+v_t)-\tanh z}{t^2}
 =\frac{v_t}{t^2}\int_0^1 \phi'(z+s v_t)\,ds.
\]

If `v_t/t^2` converges in `L2`, its right side converges to the limit
multiplied by `phi'(z)`, by the bounded-multiplier argument. Finally expand
`W(t)H_a(t)-W_0h_a` as `(W(t)-W_0)h_a+W_0(H_a(t)-h_a)` plus the product of
the two increments; the latter is `O_L2(t^4)`. The matrix term is
`2t^2 sum_b p U_b E[h_bh_a]=2t^2 M_a`. This gives the upper two limits.
These steps derive (6) along the existing actual flow; no formal power-series
existence argument is used.

##### 3. Strict positivity of both activation displacements

Actual adjunction and independence of the upper initial Gaussian coordinates
give, for each `a`,

\[
 \langle h_a,P_a\rangle_1
 =\langle\xi_a,U_a\rangle_2
 =p\,\mathbb E[\xi_a\tanh\xi_a\,\phi'(\xi_a)]>0.             \tag{7}
\]

The other summand in `S` contributes zero, since its tanh has mean zero and
is independent of `xi_a`. In the remaining expectation the integrand is
strictly positive whenever `xi_a!=0`; the nondegenerate Gaussian gives
probability one to that event. It is integrable because it is at most
`|xi_a|`. Thus `P_a` is nonzero in `L2`. Since `p>0` and `phi'(g_a)>0` almost
surely, `C_a=p phi'(g_a)^2 P_a` is also nonzero. In particular

\[
 c_1^2=\tfrac12\sum_{a=1}^2\|C_a\|_2^2>0.               \tag{8}
\]

For the upper layer, adjunction yields the positive identity

\[
 \begin{aligned}
 p\sum_a\langle U_a,R_a\rangle_2
 &=p^2q_0\sum_a\|U_a\|_2^2
   +p\sum_a\langle P_a,C_a\rangle_1\\
 &=p^2q_0\sum_a\|U_a\|_2^2
   +p^2\sum_a\mathbb E[\phi'(g_a)^2 P_a^2]>0.                \tag{9}
 \end{aligned}
\]

Its left side is `p sum_a E[S E_a]`. Consequently the `E_a` cannot all
vanish in `L2`, and

\[
 c_2^2=\tfrac12\sum_{a=1}^2\|E_a\|_2^2>0.               \tag{10}
\]

This proves precisely the averaged upper-layer assertion needed here; an
individual upper-input activity assertion is unnecessary. Formula (9) also
retains both upper-preactivation contributions, from the moving middle
matrix and from the moving lower representation.

By (6), (8) and (10),

\[
 A_\ell(\mu_0,t)=2c_\ell t^2+o(t^2),\qquad \ell=1,2.     \tag{11}
\]

There exists `tau in (0,T_*]` such that
`A_ell(mu_0,t)>=c_ell t^2` for both layers and all `0<t<=tau`.
For a completely specified choice from the actual reference solution, let
`s_0` be the supremum of `s in (0,T_*]` such that

\[
 \left|t^{-2}A_\ell(\mu_0,t)-2c_\ell\right|\le c_\ell
 \quad(\ell=1,2;\ 0<t\le s).
\]

Equation (11) gives `s_0>0`; take `tau=s_0/2` and the fixed positive
observation time `t_0=tau/2`. No explicit numeric lower bound on `t_0` is
claimed. The constants `c_ell` are the positive Gaussian-action expressions
(8), (10), rather than fitted or numerically selected quantities.

##### 4. Transport continuity and the open family

Section C.4.2 proves this precise state conclusion: on common generated Gaussian spaces, for `q=W_1(mu,nu)<=1`,

\[
 \sup_{t\le T_*}\bigl(\|w_\mu(t)-w_\nu(t)\|_2+
 \|W_\mu^{(2)}(t)-W_\nu^{(2)}(t)\|_{\rm op}\bigr)
 \le C\,\omega(q),\qquad
 \omega(q)=q\exp(C\sqrt{\log(e/q)}),\quad\omega(0)=0.       \tag{12}
\]

It suffices equally to use any established modulus tending to zero in (12).
The forward formulas on the bounded state ball imply

\[
 \sup_{t,x,\ell}
 \|H_\mu^{(\ell)}(t,x)-H_\nu^{(\ell)}(t,x)\|_2
 \le C_H\omega(q).                                      \tag{13}
\]

Indeed the lower difference is bounded by the first-row difference; the
upper preactivation difference is at most the matrix difference times
`||H_mu^(1)||_2<=1`, plus `B` times the lower difference. Applying tanh
preserves these bounds.

To compare (1), first hold the training law fixed and change the evolved
state. Each activation displacement has norm at most two, so its squared
norm changes by at most `4C_H omega(q)`. Next hold the state `nu` fixed
and change the averaging law. Equation (2) bounds the difference of
displacement fields at `x,x'` by `2K rho(x,x')`; therefore their squared
norms differ by at most `8K rho(x,x')`. Integrating against any coupling
of `mu,nu` and taking the infimum gives

\[
 \sup_{t\le T_*}|J_\ell(\mu,t)-J_\ell(\nu,t)|
 \le 4C_H\omega(q)+8Kq,\qquad\ell=1,2.                  \tag{14}
\]

The joint transport cost dominates `rho`; labels need not be deterministic
functions of inputs for this argument. Approximate minimizers suffice, so
existence of an optimal coupling need not be invoked. The same proof is
valid for atoms, coincident inputs and singular Grams.

Set `j_0=min(c_1^2,c_2^2)t_0^4>0`. Choose a radius `r_0 in (0,1)` such
that `4C_H omega(q)+8Kq<j_0/2` for all `0<q<r_0`; such a radius exists
because the displayed expression tends to zero. Then the relative open set

\[
 \mathcal U=\{\mu\in\mathcal P(\mathcal Z):
                  \mathcal W_1(\mu,\mu_0)<r_0\}          \tag{15}
\]

satisfies, at the specified time `t_0`,

\[
 J_\ell(\mu,t_0)\ge j_0/2,
 \qquad A_\ell(\mu,t_0)\ge\sqrt{j_0/2}>0,
 \quad\mu\in\mathcal U,\quad\ell=1,2.                  \tag{16}
\]

The same construction works at any chosen reference time in `(0,tau]`,
with its own neighborhood and positive margin. For example, spreading each
reference atom over a sufficiently short input arc and a sufficiently short
label interval preserves membership in (15), so the open family contains
nonatomic laws. Moving the second reference input through a sufficiently
small nonzero angle gives correlated two-input laws in (15).

##### 5. Transfer to actual finite networks

For a finite network trained on an empirical law `lambda_n`, with its actual
random initial readout, define

\[
 J_{n,\eta,\ell}(t)=\int_{\mathcal Z}\frac1n
 \|h_{n,\eta,\lambda_n}^{(\ell)}(t,x)
       -h_{n,\lambda_n}^{(\ell)}(0,x)\|_2^2\,\lambda_n(dx,dy).
                                                               \tag{17}
\]

Section C.4.3, (A14)–(A15), proves the paired initial/current activation
observable limit, for every deterministic empirical approximation and every
independent iid sample sequence in the theorem:

\[
 \sup_{t\le T_*}|J_{n,\eta_n,\ell}(t)-J_\ell(\mu,t)|
       \longrightarrow0\quad\hbox{in probability}.       \tag{18}
\]

That proof explicitly retains both times in the fixed oracle's joint
second moments; it does not infer (18) from predictor convergence.

For iid empirical laws independent of initialization, use the corresponding
in-probability joint-limit statement with these same observations. In
particular, for every `mu in U` and either deterministic empirical
approximation or iid sampling, (16), (18) imply

\[
 \Pr\{J_{n,\eta_n,\ell}(t_0)\ge j_0/4
                 \text{ for both }\ell=1,2\}\longrightarrow1. \tag{19}
\]

Thus both hidden activation displacements stay bounded away from zero as
width increases, at a physical time and activity margin independent of
width, sample count and GD step. The finite initialization is the one in
the theorem: its readout RMS has squared expectation `1/n^2`, hence tends
to zero in probability and is covered by the initialization-perturbation
comparison. It has not been set to zero in (17).

This result asserts finite-time motion of both hidden representations on an
open family. It asserts no activity for every law, no fitting, no risk
improvement, no endpoint selection and no global-time property. In
particular a law with zero conditional label mean can have the stationary
zero-readout population solution, consistently with the stated scope.

#### C.4.5. Robust whole-circle prediction after substantial learning

This theorem extends the prediction and risk scope of the local C.4 result by comparison with one fitted reference. It does not extend the local population-flow theorem for arbitrary laws. Section [C.4.7](#c47-nonlinear-training-near-the-fitted-tanh-reference) separately constructs nonlinear changed-law population dynamics near the fitted reference through T=40. The raw-GD conclusion below retains its stated step condition and endpoint scope. Equation numbers are local to each of the statement and three proof units below.

##### Exact statement

Use two tanh hidden layers of common width n, input dimension two, no biases,
and the stored-weight forward map
\[
 z^1=W^1x/\sqrt2,\quad h^1=\tanh z^1,\quad
 z^2=W^2h^1,\quad h^2=\tanh z^2,\quad f_n=(W^3)^Th^2/n.
\]
Initialize all entries/blocks independently, centered Gaussian with variances
(1,1/n,1/n²). Train all blocks with mobilities (n,1,n), unhalved mean squared
loss and physical time. Raw GD updates all stored blocks from the preceding
state; interpolate raw weights linearly and recompute activations.
The actual finite initial readout is retained.

Let Z=sqrt(2)S¹ x {-1,+1}, with joint transport cost
|x-x'|/sqrt(2)+|y-y'|, and set
\[
 \nu_*=\tfrac12\delta_{(\sqrt2e_1,1)}
       +\tfrac12\delta_{(\sqrt2e_2,-1)},\qquad
 T=40,\qquad \delta=\exp\{-\exp(3000)\}.                         \tag{1}
\]

The population reference has a unique global autonomous flow on its canonical
Gaussian action spaces. Its whole-circle predictor tends to a continuous
limit f_*^infinity. To characterize this endpoint, solve the autonomous
feature equation in Section C.4.5.1 (R4)–(R5), starting from the full independent
standard Gaussian first row, the actual initialized middle Gaussian action
and its adjoint, and zero limiting readout. Stop at the unique first feature
time s_dagger at which b=<c,(H2_1-H2_2)/2>=1; evaluate that state on every
circle input. Then 0<s_dagger<=10, and
\[
 \sup_x|f_*(t,x)-f_*^\infty(x)|\le17\sqrt{10}e^{-t/5},\qquad
 R_{\nu_*}(f_*(t))\le e^{-2t/5}.                               \tag{2}
\]
The endpoint interpolates the reference labels, is odd under x->-x, and
satisfies f∞(Px)=-f∞(x) when P swaps input coordinates. Its input Lipschitz
constant in x/sqrt(2) is less than 76. This specifies the selected prediction
through the actual dynamics; it asserts no uniqueness among interpolants.

For every fixed law mu with W1(mu,nu_*)<delta, let lambda_k be any deterministic
empirical laws converging to mu in W1. Their observation counts, support
degeneracies and atom weights have no further restrictions. Take n_k->infinity
and eta_k>0 with eta_k sqrt(n_k)->0; put t_k=floor(T/eta_k)eta_k. Then
\[
 \Pr\left\{
 \sup_{x\in\sqrt2S^1}|f_{n_k,\eta_k,\lambda_k}(t_k,x)-f_*^\infty(x)|\le1/4,\
 R_\mu(f_{n_k,\eta_k,\lambda_k}(t_k))\le1/4,\
 R_{\lambda_k}(f_{n_k,\eta_k,\lambda_k}(t_k))\le1/4
 \right\}\longrightarrow1.                                   \tag{3}
\]
Probability here is over initialization. The same conclusion holds for iid
samples of any sizes m_k->infinity from the fixed mu, independent of
initialization, with probability over both samples and initialization.
There is no relative sample/width growth restriction or finite-width rate.
The displayed GD condition is sufficient; no removal is required.

At the fixed physical time t_act=1/200 define the paired, training-averaged
squared RMS displacement
\[
 J_{\ell,k}(t)=\int_Z\frac1{n_k}
 \|h^\ell_{n_k,\eta_k,\lambda_k}(t,x)
                 -h^\ell_{n_k,\lambda_k}(0,x)\|_2^2\,d\lambda_k(x,y).
                                                                    \tag{4}
\]
The two times use the same network and neuron indices, not a coupling chosen
between marginal laws. In both deterministic and iid settings,
\[
 \Pr\{J_{1,k}(t_{\rm act})\ge10^{-13},\
       J_{2,k}(t_{\rm act})\ge10^{-13}\}\longrightarrow1.        \tag{5}
\]
Thus both paired RMS norms exceed sqrt(10^-13) independently of width/sample
count. This holds jointly with (3). One may replace t_act by its preceding
GD node, by the same bounded-velocity estimate. No displacement at T is
claimed. The opposite-label reference itself has each averaged paired RMS
strictly greater than 1/2500000 at t_act.

##### Strict numerical margins and transfer

The exact rational Gaussian certificate gives m>=1/10. The reference proof
gives
\[
 17\sqrt{10}e^{-8}<.019<1/32,\qquad e^{-16}<1/1024.             \tag{6}
\]
In Section C.4.5.3 choose
\[
 B=12,\quad K=40000000,\quad d_0=10^{-18},\quad R=e^{2900},\quad
 M_Q=225400e^{2880}+180,\quad H=16(4+M_Q).                     \tag{7}
\]
The elementary bounds M_Q<e^2893, H<e^2897, K<e^18,
1+R<e^2901 and R²/4096>e^5791 give R>4M_Q+20 and R>101. Therefore
\[
 \log\{KH e^{K(1+R)-R^2/4096}\}
 <2915+e^{2919}-e^{5791}<-100,
\]
\[
 \log\{K(1+R)e^{K(1+R)}\delta\}
 <2919+e^{2919}-e^{3000}<-100.                                \tag{8}
\]
For example e>2 already separates the last exponentials by far more than
3019. Also e^-100<10^-18/4, using the single positive term 100^16/16! in
the series for e^100. These are the two strict bounds in Section C.4.5.3 (15).
The same estimates give
\[
 L_{\rm risk}\delta<1/256,\quad 8B^2\delta<10^{-18},
 \qquad L_{\rm risk}=44928.                                  \tag{9}
\]

Compare actual GD to actual finite GF on nu_* with the same initialized
arrays. Since limsup W1(lambda_k,nu_*)<delta, the stopped comparison gives
\[
 \left(\sup_{t\le40}D_{n_k}(\theta_{GD,k}(t),\bar\theta_{n_k}(t))
                                       -d_0/2\right)_+
 \longrightarrow0\quad\hbox{in probability}.                 \tag{10}
\]
Its complete proof, including the finite actual-state bounds, initial
readout, reference tails, auxiliary-mesh order and stopping argument, is
Section C.4.5.3. The reference is raw GF, so its raw-field defect is zero.
Transformed Euler is used only as an auxiliary width-identification tool.

Whole-circle reference convergence and the full-state estimates imply
\[
 \left(\sup_x|f_k(T,x)-f_*^\infty(x)|-1/16\right)_+
 \longrightarrow0\quad\hbox{in probability},                 \tag{11}
\]
because the deterministic bound is .019+B²d0<1/16. The circle extension uses
the full first row and uniform input Lipschitz bounds. Replacing T by t_k
costs at most a fixed state-speed/prediction constant times eta_k.
The finite predictor is bounded by 12 and Lipschitz in normalized input
with constant 1728 on the comparison event. Its squared-loss integrand has
joint Lipschitz constant Lrisk. At the reference atoms f∞ equals the label.
Thus (9),(11) give
\[
 (R_\mu(f_k(t_k))-1/128)_+\longrightarrow0,\quad
 (R_{\lambda_k}(f_k(t_k))-1/128)_+\longrightarrow0
                      \quad\hbox{in probability}.            \tag{12}
\]
The two deterministic contributions are (1/16)² and Lrisk delta<1/256;
for the empirical risk use W1(lambda_k,nu_*)<=delta+o(1). These strict
bounds prove (3), not just convergence to its thresholds. Both limiting
initial binary-label risks are one, because the initial predictor is
uniformly bounded by the vanishing readout RMS.

For activity, changing the evolved state with initialization fixed changes
the paired squared-displacement integrand by at most 4(B+1)D_n. Changing
its input changes it by at most 8B²|u-v|. These follow from displacement
RMS<=2 and the forward input/state bounds in Section C.4.5.3. Coupling lambda_k
to nu_*, retaining the separate paired-observable reference convergence,
and using its strict RMS margin gives
\[
 J_{\ell,k}(t_{\rm act})\ge(1/2500000)^2-2(B+1)d_0-8B^2\delta
                                            -o_{\mathbb P}(1).       \tag{13}
\]
The deterministic right side exceeds 1.59*10^-13, proving (5) with slack.
The opposite-label activity computation is proved anew in Section C.4.5.1;
C.4's equal-label example is not substituted for it.

For iid samples, compact Borel partitions and the variance bound for each
empirical cell mass prove W1(lambda_k,mu)->0 in probability, as detailed
in Section C.4.5.3. Its other random events involve only the fixed reference
and initialization. Union bounds give (3),(5) in joint probability.
Each claim is for every fixed mu and sequence. No uniform failure probability
over laws, almost-sure joint limit, global population flow for mu or endpoint
for mu is asserted.

##### Geometric meaning, scale and limitations

An admitted nonorthogonal law moves the second reference input by the angle
a=delta/2, retaining its label and the first atom. Its cost is at most
a/2=delta/4; the off-diagonal input Gram is -sin(a), which is nonzero.

For an admitted nonatomic law replace each input atom by uniform arc length
on the arc of angular radius a=delta/4 around it, retaining its associated
label, and then flip each binary label independently with probability
p=delta/8. The coupling costs at most a+2p=delta/2<delta. More generally
a+2p<delta suffices; arbitrary extra contamination of mass rho costs at most
4rho. Thus no orthogonality, two-atom, Gram-inverse or weight-lower-bound
condition is imposed on perturbed laws.

The explicit radius is mathematically positive, but extremely small:
\[
 \log_{10}(1/\delta)=e^{3000}/\log 10,\qquad
 \log_{10}\log_{10}(1/\delta)
 =3000/\log 10-\log_{10}(\log10)\approx1302.52.
\]
This is far below a practically useful neighborhood. The dominant loss is
the fresh-root stability exponential followed by a cutoff comparison.
A bounded targeted improvement used the reference energy path length and
integrated a time-dependent coefficient, reducing the response exponent
to 2880. Its conservatism is likely substantial; its sharpness is not
assessed by this proof. No training experiment or parameter sweep was run.

The theorem establishes whole-circle robustness after substantial risk
reduction for an open family with nonlinear moving hidden features. It
does not show that feature motion causes that reduction, superiority to
linear or frozen-feature learning, or useful risk on a uniform-circle
teacher distribution. It gives no arbitrary-accuracy guarantee for one
fixed perturbed law. A radius shrinking with accuracy would not give that
stronger conclusion.



##### C.4.5.1. The opposite-label reference and its endpoint

###### 1. Full state and exact feature equation

Put `u=x/sqrt(2)`. Work on the canonical generated probability spaces
`H_1=L2(Omega_1)` and `H_2=L2(Omega_2)` with the initialized bounded
Gaussian action `A_0:H_1->H_2` and its actual adjoint. Its operator norm is
at most two, by A.3. The full first row is `w=(w_1,w_2)`, initially
`(g_1,g_2)` with independent standard normal coordinates. The population
readout is `c(0)=0`; this is the limit of the specified finite random
readout, not a modification of finite initialization. Write `A=A_0+K`.
The increment metric is

\[
 \|(v,B,d)\|_{\rm raw}^2
 =\|v\|_{L^2(\Omega_1;\mathbb R^2)}^2+\|B\|_{\rm HS}^2+\|d\|_2^2.       \tag{R1}
\]

Only the increment `K` is Hilbert–Schmidt. Its finite counterpart is exactly
`||dW1||F²/n+||dW2||F²+||dW3||²/n`. This follows because rank-one population
operators have finite representative `uv^T/n` and HS norm `||u||2||v||2`.

Let `phi=tanh`, and, for `a=1,2`, write

\[
 Z_a^1=w_a,\quad H_a^1=\phi(w_a),\quad Z_a^2=AH_a^1,\quad
 H_a^2=\phi(Z_a^2).
\]
\[
 y_1=1,\ y_2=-1,\qquad h=\frac12(H_1^2-H_2^2),\quad
 b=\langle c,h\rangle=\frac12(f_1-f_2).
\]

For hidden increments `(v,B)`, define the bounded linear map into `H_2`

\[
 J(v,B)=\frac12\sum_{a=1}^2y_a \phi'(Z_a^2)
              \{BH_a^1+A(\phi'(Z_a^1)v_a)\}.                          \tag{R2}
\]

This is the directional differential of `h`; an unrestricted Frechet
statement for an L2-valued Nemytskii map is neither used nor true in general.
Pairing each term with a fixed `c` and using the actual adjoint gives

\[
 J^*c=\left(
  (\tfrac12y_a \phi'(Z_a^1)A^*(\phi'(Z_a^2)c))_{a=1,2},\quad
  \tfrac12\sum_a y_a(\phi'(Z_a^2)c)\otimes H_a^1\right).               \tag{R3}
\]

The HS adjunction is
`<q tensor v,B>HS=<q,Bv>2`; thus (R3) uses exactly (R1).
Consider the autonomous feature equation

\[
                 c_s=h,\qquad (w,K)_s=J^*c.                  \tag{R4}
\]

It has a unique global solution for every finite feature horizon. Here is
the necessary specialization of B.1, including the change from its sum loss.
Let `j(X,g)` solve `j_X=phi'(j)`, `j(0,g)=g`. Its scalar vector field is
bounded by one and Lipschitz, so it exists for all real `X`. It obeys
`|j(X,g)-j(Y,g)|<=|X-Y|`. Set `w_a=j(X_a,g_a)` and solve

\[
 (X_a)_s=\tfrac12y_a A^*(\phi'(Z_a^2)c),\quad
 K_s=\tfrac12\sum_a y_a(\phi'(Z_a^2)c)\otimes H_a^1,\quad c_s=h.       \tag{R5}
\]

On bounded clock-L2/operator/readout-supremum sets these equations are
Lipschitz in the sum of clock L2, operator norm, and readout L2 distances:
`H1` is Lipschitz in the clock with constant one; `H2` is Lipschitz in its
preactivation; and
`||phi'(Z2)c-phi'(Z2bar)cbar||2<=||c-cbar||2+2||cbar||infty||Z2-Z2bar||2`.
The rank-one difference estimate and bounded action/adjoint then control
all three right sides. The closed readout-supremum condition is complete
in L2 and its integral update preserves an enlarged bound on a short
interval. Contraction of that integral map gives local existence and
uniqueness. Moreover, directly from (R5),

\[
 \|c(s)\|_\infty\le s,\quad \|K(s)\|_{\rm HS}\le s^2/2,
 \quad \|A(s)\|_{\rm op}\le2+s^2/2,
\]
\[
 \|w(s)-w(0)\|_2
 \le {1\over\sqrt2}\int_0^s(2+v^2/2)v\,dv.                  \tag{R6}
\]

The same bound holds for the clock norm in the last display. These
polynomials prevent escape from the required bounded sets on every finite
horizon; the integrated equations give a strong limit at a finite proposed
endpoint and the same local construction extends it. Rank-one continuity
upgrades `K` to a strongly C1 HS curve. Bounded-multiplier continuity
upgrades `w` to a strongly C1 L2 curve and proves (R4). Conversely, the
scalar equation `w_s=B(s)phi'(w)` has the unique representation
`j(integral B,g)`: Fubini makes `B` integrable at almost every coordinate,
and the scalar integral Lipschitz inequality gives uniqueness. Thus these
are the actual raw feature equations, not an alternative optimizer.

The Gaussian action used here is the canonical common action of B.1:
countably many finite generated programs, their finite unions, both matrix
orientations, and passive input probes are realized jointly before
completion. Continuous at-most-linear value instructions `j` are admitted
by A.1. The same-root Lipschitz estimate just given supplies the empirical
feedback passage. No bounded derivative with respect to the Gaussian root
is required. At a current state, resetting clock zero and retaining the
current raw fields/action gives the same unique continuation, so the raw
reference is autonomous and restartable. This construction supplies a
complete actual-state endpoint characterization below; it encodes no
future trained trajectory in its coefficients.

###### 2. Symmetry, fitting, and the two clocks

Let `P(u_1,u_2)=(u_2,u_1)`. The raw transformation
`(w,A,c)->(wP,A,-c)` maps predictions to `-f(Pu)`. Direct substitution in
(R3)–(R4) shows that it preserves the feature vector field, since `h`
changes sign and the two labels exchange signs. It also preserves the
physical vector field for the probability law
`nu_*=1/2 delta_(e1,+1)+1/2 delta_(e2,-1)` in normalized inputs.
The initial full-row Gaussian law is invariant under swapping its two
coordinates; the independent initialized matrix law is unchanged and
`c0=0` changes to itself. At the generated-action level this statement is
obtained by adjoining the swapped version of every finite program to the
same countable construction. Finite joint laws are invariant; hence the
coordinate swap is a probability-space isometry that respects coordinate
operations, the action and its adjoint. The unique integral construction
commutes with it. Therefore the deterministic predictions satisfy

\[
                 f(Pu)=-f(u),\qquad f_1=b=-f_2.                \tag{R7}
\]

This is symmetry of the population action law, not pointwise symmetry of a
particular finite initialized network. No such finite symmetry is assumed.
Oddness of both activations also gives `f(-u)=-f(u)`.

For the mean squared loss the reference residuals are `(b-1,1-b)`.
The exact physical equations of C.4.1 therefore equal `2(1-b)` times
(R4). The correct clock is

\[
                 {ds\over dt}=2(1-b),\qquad s(0)=0.           \tag{R8}
\]

To prove that this clock is legitimate through all physical times, first
work with the globally defined feature equation. The strong curve chain
rule gives `h_s=J(w,K)_s`. Indeed bounded continuous multiplication is
strongly continuous on a fixed L2 vector after truncating that vector;
the scalar fundamental theorem of calculus then proves
`(phi(z))_s=phi'(z)z_s` for strongly C1 L2 curves. Differentiating a bounded
operator times a strongly C1 vector by adding and subtracting its factors
gives the ordinary product rule. Applied successively to (R2) this gives

\[
 c_{ss}=JJ^*c,\qquad
 b_s=\|h\|_2^2+\|J^*c\|_{\rm hidden}^2
                  =\|\theta_s\|_{\rm raw}^2.                 \tag{R9}
\]

The metric in the second term is the row-L2 plus HS hidden metric from
(R1). No derivative of `J` is taken in (R9).

Set `m=||h(0)||2²`. Initially the two first features are independent odd
functions of independent standard normals, so their Gram is `q I_2`, where

\[
 q=E\tanh^2G,\qquad v=E\tanh^2(\sqrt qG),\qquad m=v/2.        \tag{R10}
\]

The initial second preactivations are independent `N(0,q)` by the initial
forward Gaussian law. The elementary certificate in §5 proves

\[
                         m\ge m_0:=1/10.                     \tag{R11}
\]

On every interval where `g=||c||2>0`, differentiating its scalar norm gives

\[
 g_s=b/g,\qquad
 g_{ss}=\frac{\|h\|_2^2-(g_s)^2+\|J^*c\|_{\rm hidden}^2}{g}
                                                          \ge0.\tag{R12}
\]

Cauchy–Schwarz gives the inequality. Since `c(s)=s h(0)+o_L2(s)` and
`h(s)->h(0)`, one has `g_s(0+)=sqrt(m)`. Consequently on its first
positive interval `g_s>=sqrt(m)` and `g>=s sqrt(m)`. It cannot reach zero
again at a positive endpoint, so this interval is all positive feature
times. Again by Cauchy–Schwarz, `||h||2>=g_s`, and (R9) gives

\[
                         b_s\ge m\ge m_0.                    \tag{R13}
\]

Hence there is exactly one first feature time `s_dagger` with `b=1`, and
`0<s_dagger<=1/m<=10`. On `[0,s_dagger)`, define

\[
 t(s)=\int_0^s\frac{dv}{2(1-b(v))}.                           \tag{R14}
\]

Its integrand is positive. Since `b_s` is continuous and bounded on the
compact feature interval `[0,s_dagger]`, say by `K`,
`1-b(s)<=K(s_dagger-s)`; thus the integral diverges as
`s->s_dagger`. Its inverse is defined for every `t>=0` and obeys (R8).
It is the unique B.1 physical reference by uniqueness of the original raw
equation. Writing `e(t)=1-b(s(t))`, differentiation gives

\[
 e_t=-2b_s e,\quad 0<e(t)\le e^{-2m t}\le e^{-t/5},\qquad
 R_{\nu_*}(f_*(t))=e(t)^2\le e^{-2t/5}.                       \tag{R15}
\]

There is no finite physical time at which the residual first vanishes:
the displayed linear scalar equation with locally bounded coefficient
and initial value one keeps it positive. This also checks the clock sign.

###### 3. Actual endpoint and uniform prediction convergence

By (R9) and Cauchy–Schwarz, for `0<=s_1<=s_2<=s_dagger`,

\[
 \|\theta(s_2)-\theta(s_1)\|_{\rm raw}
 \le\sqrt{(s_2-s_1)(b(s_2)-b(s_1))}.                          \tag{R16}
\]

The state is already globally defined in feature time. Its endpoint is
precisely the solution of (R4)–(R5) stopped at the uniquely characterized
first level `b=1`; denote it `(w_dagger,A_dagger,c_dagger)`. Define on the
whole circle

\[
 f_*^\infty(\sqrt2u)
 =\langle c_\dagger,\tanh(A_\dagger\tanh(w_\dagger\cdot u))\rangle.
                                                                  \tag{R17}
\]

Thus (R17) is a characterization through the actual autonomous dynamics,
including its initialized Gaussian action and adjoint. It is not merely a
name for an unknown prediction limit. It gives `f∞(sqrt2 e1)=1`,
`f∞(sqrt2 e2)=-1` and the two symmetries in (R7).

Equations (R13),(R16) imply

\[
 s_\dagger-s(t)\le e(t)/m,\qquad
 \|\theta(s(t))-\theta(s_\dagger)\|_{\rm raw}\le e(t)/\sqrt m.
                                                                  \tag{R18}
\]

In particular throughout this interval

\[
 \|c\|_2\le\sqrt{10},\quad \|A\|_{op}\le2+\sqrt{10},\quad
 \|w\|_2\le\sqrt2+\sqrt{10},\quad \|c\|_\infty\le10.           \tag{R19}
\]

For any `|u|=1`, strong directional differentiation and the same
adjunction as above give three raw gradient blocks for `f(u)` with norms
at most `||A||op||c||2`, `||c||2`, and one, respectively. Equivalently,
add and subtract the three endpoint factors and use the one-Lipschitz
activations. The straight segment between two reference states retains
(R19). Integrating the scalar derivative along this segment proves

\[
 \sup_{|u|=1}|f_\theta(u)-f_{\bar\theta}(u)|
 \le C\|\theta-\bar\theta\|_{\rm raw},\quad
 C=\sqrt{1+10\{1+(2+\sqrt{10})^2\}}<17.                       \tag{R20}
\]

This holds simultaneously for all inputs; no finite grid substitutes for
the circle. Combining it with (R15),(R18),

\[
 \sup_{x\in\sqrt2S^1}|f_*(t,x)-f_*^\infty(x)|
 \le 17\sqrt{10}\,e^{-t/5}.                                  \tag{R21}
\]

The explicit choice

\[
                              T=40                           \tag{R22}
\]

therefore has endpoint error less than `1/32`: `17 sqrt(10)e^-8<.019<1/32`.
Its reference risk is at most `e^-16<1/1024`. These are strict margins.
For example the elementary Taylor lower sum for `e^8` already proves the
stated inequalities, so no numerical solver for the trained flow is used.

Input regularity also follows directly from the full-row norm:

\[
 |f_\theta(\sqrt2u)-f_\theta(\sqrt2v)|
 \le\sqrt{10}(2+\sqrt{10})(\sqrt2+\sqrt{10})|u-v|<76|u-v|.    \tag{R23}
\]

The endpoint satisfies the same estimate. Also `||f||infty<=sqrt10`.
For binary labels, `(f(u)-y)^2` is therefore Lipschitz in the prescribed
joint transport cost with constant at most
`2(sqrt10+1) max(76,1)<633`; use
`|(a-y)^2-(b-z)^2|<=2(sqrt10+1)(|a-b|+|y-z|)`.
This proves the exact input regularity needed for risk transport.

For a general target error `epsilon>0`, the same reference component gives
`T(epsilon)=max(0,5 log(17 sqrt10/epsilon))`. Changed-law radii for this
choice remain a separate comparison conclusion and may shrink with epsilon.

###### 4. Both hidden activations move at the fixed time 1/200

This section uses the actual opposite-label reference and retains paired
initial/current observations. Put `Y_a=A0 H0_a^1`; let

\[
 h_0=(\tanh Y_1-\tanh Y_2)/2,\quad
 U_a=h_0\phi'(Y_a),\quad P_a=A_0^*U_a,\quad
 V_a=\phi'(g_a)^2P_a,
\]
\[
 R_a=qU_a+A_0V_a,\qquad
 a_0=E\phi'(G)^4,\quad r_0=E\phi'(\sqrt qG)^2.                \tag{R24}
\]

All fields are typed: `U,R` live in layer two, and `P,V` in layer one.
The Gaussian integration certificate proves `q>.39`, `q<.4`,
`v>.2`, `a0>.3`, and `r0>.6`.

Here is a complete fixed initial reuse calculation establishing positivity
and the needed moments. Let `C_ab=E[U_a U_b]`. Gaussian conditioning on
the first two forward calls gives

\[
 P_a=\sum_{b=1}^2p_{ab}\tanh g_b+\Gamma_a,\quad
 p_{ab}=E[Y_bU_a]/q,\quad \Gamma\sim N(0,C),                  \tag{R25}
\]

independently of `(g1,g2)`. This is the actual transpose response, not a
fresh-matrix replacement. For completeness, the finite conditional
Gaussian matrix has its mean fixed on the two forward query directions
and independent Gaussian randomness on their orthogonal complement.
Applying its transpose to `U` gives the first term in (R25) and a Gaussian
with covariance `E[UU^T]`; projections onto the finitely many old first
query directions have expected squared RMS `O(1/n)` and disappear.
The joint initial forward Gram is `q I`, so no inverse at a degeneracy is
involved here. Bounded smooth `U(Y)` permits the fixed-program law and
contractions. Truncating the products by bounded gates and using their
fixed Gaussian moment envelopes permits the same conclusion for `V`.

The matrix `C` is positive definite. If `z1 U1+z2 U2=0` almost surely,
Gaussian full support and continuity give
`(tanh Y1-tanh Y2)(z1 phi'(Y1)+z2 phi'(Y2))=0` everywhere.
On the dense open set `Y1!=Y2` the second factor vanishes and continuity
extends this identity everywhere. Varying each coordinate and using the
nonconstant function `phi'` forces `z1=z2=0`.

Let `alpha_b=E[H0_b^1 V_a]/q`,
`V_a^perp=V_a-sum alpha_b H0_b^1`, and
`sigma_a²=E[(V_a^perp)²]`. Conditioning the same Gaussian matrix on the
forward calls and the reverse calls in (R25) gives

\[
 A_0 V_a=\sum_b\alpha_bY_b+\bar d\,U_a+\sigma_a\gamma_a,
 \quad \bar d=E\phi'(G)^2,                                  \tag{R26}
\]

where `gamma_a` is standard normal independent of the old layer-two
coordinates, for each fixed `a`. Independence between `gamma1,gamma2`
is not claimed. To verify the response coefficient, the conditional
matrix formula gives `C^-1 E[P V_a^perp]` for the coefficient of `U`.
The deterministic part of each `P_b` is in the span of the first forward
inputs and pairs to zero with `V_a^perp`. The remaining pairing is
`E[Gamma_b Gamma_a] E phi'(G)^2=C_ba bar d`; multiplication by `C^-1`
gives `bar d` in coordinate `a`. The unused Gaussian input variance is
`sigma_a²`. Its finite output projection off the two old reverse input
directions again has vanishing RMS. These calculations prove (R26)
without suppressing either reused response term.

Conditional variance in (R25) and projection off functions of the roots
give

\[
 \|V_a\|_2^2\ge C_{aa}a_0,\qquad
 \sigma_a^2\ge C_{aa}a_0,\qquad
 \|\phi'(Y_a)R_a\|_2^2\ge C_{aa}a_0 r_0.                    \tag{R27}
\]

The last inequality conditions on the old second-layer coordinates in
(R26); all its other terms are functions of those coordinates. By
independence and oddness of the initial `Y1,Y2`,

\[
 C_{aa}=\tfrac14 E[(\tanh^2Y_a+v)\phi'(Y_a)^2]
                          \ge vr_0/4>3/100.                  \tag{R28}
\]

Thus each of the two first-order-in-`s²` coefficients has norm at least

\[
 \tfrac14\|V_a\|_2>1/100,\qquad
 \tfrac14\|\phi'(Y_a)R_a\|_2>1/100.                          \tag{R29}
\]

For explicit remainder bounds, (R25) gives `sum_b|p_ab|<=2/sqrt q<4`
and `Caa<=1`. It can be coupled so that `|P_a|<=4+|G|`, and hence
`||P_a||4<6`. For `R>=8` and `z=R-4`, the elementary Gaussian tail
integration yields

\[
 \tau_R(P_a):=\|P_a1_{|P_a|>R}\|_2
 \le\{(4z+68/z)e^{-z^2/2}\}^{1/2}.                           \tag{R30}
\]

Indeed `(|G|+4)^2<=2G²+32`,
`Pr(|G|>z)<=2phi_G(z)/z`, and
`E[G²1_|G|>z]<=2(z+1/z)phi_G(z)`; then drop the density factor
`1/sqrt(2pi)<1`. At `R=10`, the right side is less than `1/1000`.
By bounded action `||V_a||2<=||P_a||2<=2`.
In (R26), the Gaussian linear term has L4 norm at most
`3^(1/4)||V_a||2<3`, the fresh Gaussian term has L4 norm below three,
and `(q+bar d)U_a` has supremum at most two. Therefore `||R_a||4<8`.

We now prove an explicit small-feature-time expansion using only these
fixed initial tails. For `0<=s<=1`, (R6) gives

\[
 \|A\|_{op}\le5/2,\quad \|c\|_\infty\le s,\quad
 \|K\|_{HS}\le s^2/2,\quad
 \|w_a-g_a\|_2\le5s^2/8,
\]
\[
 \|Z_a^2-Y_a\|_2\le7s^2/4,\quad
 \|c-sh_0\|_2\le7s^3/12,\quad
 \|\phi'(Z_a^2)c-sU_a\|_2\le5s^3,
\]
\[
                  \|A^*(\phi'(Z_a^2)c)-sP_a\|_2\le11s^3.           \tag{R31}
\]

For the middle line, `H1` and `H2` are one-Lipschitz, so
`||h(s)-h0||2<=7s²/4`; integrate and then use the two-Lipschitz
second gate. The last line uses `||A||<=5/2`, `||K||<=s²/2`
and the sharper `49s³/12` bound preceding the rounded `5s³`.

Truncate the *fixed initial* `P_a` at `R`. Then

\[
 \|(\phi'(Z_a^1(s))-\phi'(g_a))P_a\|_2
 \le(5R/4)s^2+2\tau_R(P_a).
\]

Subtract `y_a s phi'(g_a)P_a/2` from the first raw feature velocity in
(R3), integrate, and use (R31). The preactivation remainder is bounded by
`(44+5R)s^4/32+tau_R(P_a)s²/2`. For the activation, compare first with
the artificial increment `y_a s² phi'(g_a)P_a/4`; its scalar tanh Taylor
remainder has L2 norm at most `s^4||P_a||4²/16`, since `|phi''|<=2`.
Consequently

\[
 \|H_a^1(s)-H_a^1(0)-y_as^2V_a/4\|_2
 \le\tfrac12\tau_R(P_a)s^2+{116+5R\over32}s^4.                \tag{R32}
\]

The middle velocity differs from
`(s/2)sum y_a U_a tensor H_a^1(0)` by at most `45s³/8` in HS norm:
use (R31), `||U||2<=1`, and `||H1-H10||2<=5s²/8`.
After integration its remainder is at most `45s^4/32`.
Expanding `(A0+K)(H10+Delta H1)` now gives
`Z2_a-Y_a=y_as²(q U_a+A0V_a)/4` with remainder at most
`tau_R(P_a)s²+[2(116+5R)/32+55/32]s^4`. The `55/32` consists of
`45/32` from the middle increment and `5/16` from `K Delta H1`.
The scalar tanh remainder adds `s^4||R_a||4²/16<=4s^4`. Thus

\[
 \|H_a^2(s)-H_a^2(0)-y_as^2\phi'(Y_a)R_a/4\|_2
 \le\tau_R(P_a)s^2+{415+10R\over32}s^4.                      \tag{R33}
\]

At `R=10` and `s<=1/100`, (R29)–(R33) show, for both layers and each
reference input,

\[
           \|H_a^\ell(s)-H_a^\ell(0)\|_2\ge s^2/200.         \tag{R34}
\]

In fact the error coefficient is at most
`.001+(515/32)10^-4<.003<.005`, strictly below half the coefficient
lower bound `.01`.

Choose the fixed **physical** time

\[
                       t_{\rm act}=1/200.                   \tag{R35}
\]

Since `||c(s)||2<=s` and `||h||2<=1`, one has `0<=b(s)<=s`
before the level `b=1`. The clock therefore satisfies
`1-e^-2t<=s(t)<=2t`. At (R35),
`199/20000<=s(t_act)<=1/100`; the lower bound uses
`1-e^-a>=a-a²/2`. Hence the paired RMS averaged over the reference law,

\[
 D_{\ell,*}(t)=\left\{\frac12\sum_{a=1}^2
 E_\ell|H_a^\ell(t)-H_a^\ell(0)|^2\right\}^{1/2},
\]

obeys the explicit strict margin

\[
              D_{\ell,*}(t_{\rm act})>1/2{,}500{,}000,
              \qquad \ell=1,2.                              \tag{R36}
\]

The average uses paired initial and current coordinates on the same layer
population. It is not the Wasserstein distance between separate marginals.
By B.1 the reference finite networks retain this paired observable:
with their actual random initial readout, widths tending to infinity and
actual steps satisfying `eta sqrt(n)->0`, its finite squared value
`(2n)^-1 sum_(a,i)|h_ai^ell(t)-h_ai^ell(0)|²` converges in probability
to `D_(ell,*)²` at this physical time. In particular its RMS exceeds half
(R36) with probability tending to one. Whole-circle law perturbation and
averaging under a nearby `mu`, or its empirical laws, require the separate
transport component; (R36) supplies the positive reference margin for it.
No claim of displacement at time `T=40` is needed or made here.

###### 5. Reproducible rational Gaussian certificate

This is deterministic constant evaluation, not a training experiment.
For `0<=x<=18`, put `S80(x)=sum_(j=0)^80 x^j/j!`. Then

\[
 S_{80}(x)\le e^x\le S_{80}(x)
       +{x^{81}/81!\over1-x/82}.                             \tag{R37}
\]

The upper remainder follows because every subsequent term ratio is at
most `x/82<1`. Quadrature arguments are at most eight; the separate
initial-tail verification uses argument eighteen. Partition `[0,4]` into 1,000 intervals of width `1/250`.
The Gaussian density decreases there and its value at zero lies between
`.3988` and `.3990`; the program certifies the two squared inequalities
using rational alternating bounds for
`pi=16 arctan(1/5)-4 arctan(1/239)`. This identity follows from the tangent
addition formula: `tan(4 arctan(1/5))=120/119`, so subtracting
`arctan(1/239)` gives tangent one at an angle in `(0,pi/2)`.
The alternating arctangent remainder bounds follow by integrating the
finite geometric identity for `1/(1+x²)` from zero to each positive
argument. Use tanh at left endpoints and density at right
endpoints for lower bounds on increasing squared tanh. For decreasing
powers of sech, both right endpoints give lower bounds. For the upper
bound on `q`, use the opposite endpoints and add `1/10000`; the missing
two-sided Gaussian tail beyond four is at most `2phi_G(4)/4<1/10000`.
The function `(E-1)/(E+1)` increases for `E>=1`, whereas
`4E/(E+1)^2` decreases there. Thus (R37) supplies rational bounds for
all required gates. Since `.624²<.39` and `.633²>.4`, the resulting lower
bounds imply the exact `v,a0,r0` bounds used above.

The following complete Python program uses exact rational arithmetic,
rounding each summand outward to denominator `10^12` to prevent growth of
unneeded common denominators. Its assertions are exact integer/rational
comparisons. Decimal output is only a readable summary.

```python
from fractions import Fraction as F
N = 1000
cache = {}
def expb(x):
    if x in cache:
        return cache[x]
    t = S = F(1)
    for j in range(1, 81):
        t = t*x/j
        S += t
    upper = S + t*x/81/(1-x/82)
    cache[x] = (S, upper)
    return S, upper
# Density bounds, with no floating point pi dependency.
def atanb(x):
    lo = sum((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(20))
    return lo, lo+x**41/41
a, b = atanb(F(1,5))
c, d = atanb(F(1,239))
pi_lo, pi_hi = 16*a-4*d, 16*b-4*c
assert 2*pi_hi*F(3988,10000)**2 < 1
assert 2*pi_lo*F(399,1000)**2 > 1
# Two-sided Gaussian tail beyond four is at most phi_G(4)/2.
e8_lo, _ = expb(F(8))
assert F(399,1000)/(2*e8_lo) < F(1,10000)
# Verify the two additional elementary margins used in the proof.
assert F(35334,1000)/expb(F(18))[0] < F(1,1000000)
assert 17*F(3163,1000)/e8_lo < F(1,32)
D = 10**12
def low(z):
    v = z*D
    return F(v.numerator//v.denominator, D)
def high(z):
    return -low(-z)
qlo = qhi = vlo = alo = rlo = F(0)
for j in range(N):
    l, r = F(j,250), F(j+1,250)
    el, _ = expb(2*l)
    _, er = expb(2*r)
    _, dr = expb(r*r/2)
    dl, _ = expb(l*l/2)
    tl, tr = (el-1)/(el+1), (er-1)/(er+1)
    wl = 2*F(3988,10000)/250/dr
    wu = 2*F(399,1000)/250/dl
    qlo += low(wl*tl**2)
    qhi += high(wu*tr**2)
    ev, _ = expb(2*F(624,1000)*l)
    _, ee = expb(2*F(633,1000)*r)
    tv = (ev-1)/(ev+1)
    sa, sr = 4*er/(er+1)**2, 4*ee/(ee+1)**2
    vlo += low(wl*tv**2)
    alo += low(wl*sa**4)
    rlo += low(wl*sr**2)
print([float(z) for z in (qlo, qhi+F(1,10000), vlo, alo, rlo)])
assert qlo > F(39,100) and qhi+F(1,10000) < F(2,5)
assert vlo > F(1,5) and alo > F(3,10) and rlo > F(3,5)
```

Executed with Python 3.10.12, exit zero. Output:

```text
[0.392108947877, 0.396376711612, 0.233120735618,
 0.339792209687, 0.631761866359]
```

The displayed standard-library Python program is the complete reproduction procedure. Its exact rational comparisons certify the weaker bounds m>=.1, a0>.3 and r0>.6 used above. No numerical training solver is needed.


##### C.4.5.2. Quantitative reference response tails

###### 1. Exact feature equations and the bounded reference interval

Put `sigma_1=1`, `sigma_2=-1`, and `phi=tanh`. Let `J` be the global
scalar solution

\[
 J_X(X,g)=\operatorname{sech}^2 J(X,g),\qquad J(0,g)=g,
 \quad H(X,g)=\tanh J(X,g).                                      \tag{R1}
\]

Here `X` is a clock argument; `g` is a fixed Gaussian first-row root.
For each fixed `g`, scalar existence and uniqueness follow from boundedness
and global Lipschitz continuity of `sech²`. In particular
`|J(X,g)|<=|g|+|X|`, `|J(X,g)-J(Y,g)|<=|X-Y|`, and
`H_X=sech⁴ J`, so `|H_X|<=1`. There is no globally bounded derivative
assumption in the root `g`.

The feature equations on the two separate neuron probability spaces are

\[
\begin{aligned}
 H_a^1&=H(X_a,g_a),& Z_a^2&=A H_a^1,&H_a^2&=\phi(Z_a^2),\\
 \delta_a&=c\phi'(Z_a^2),& Q_a&=A^*\delta_a,\\
 X_{a,s}&=\tfrac12\sigma_a Q_a,&
 A_s&=\tfrac12\sum_a\sigma_a\delta_a\otimes H_a^1,&
 c_s&=\tfrac12\sum_a\sigma_a H_a^2 .
\end{aligned}                                                     \tag{R2}
\]

The initialized action and its adjoint are the common Gaussian action,
and `X(0)=0,c(0)=0`. The rank action is
`(v tensor h)z=v E_1[hz]`. At finite width it is `v h^T/n`.
These equations are the actual reference flow under
`ds/dt=2(1-b)`, up to its feature endpoint `s_infty`. They are also a
well-defined auxiliary autonomous feature system beyond that endpoint,
but no estimate below requires that extension.

Write `m=|| (H_1^2(0)-H_2^2(0))/2 ||_2²`. The reference fitting proof
establishes

\[
 m\ge1/10,\quad 0<s_\infty\le1/m\le10,\quad
 \|\theta(s)-\theta(0)\|_{\rm raw}\le\sqrt{s\,b(s)}\le\sqrt{10}
 \quad(0\le s\le s_\infty).                                      \tag{R3}
\]

The raw increment norm is the square sum of the full first-row L2 norm,
the middle Hilbert–Schmidt norm and the readout L2 norm. Therefore
`||A-A_0||HS<=sqrt(10)`, `||c||2<=sqrt(10)`, and (R2) independently gives
`||c(s)||infinity<=s`. The canonical initialized action has norm at most
two; its finite counterpart has norm at most three with probability
tending to one, by the contained proof in global nonlinear A.3.

Only meshes with terminal point at most `s_infty` will be used. For all
sufficiently fine such meshes, their population Euler paths have
`||A-A_0||HS<sqrt(10)+1/10`, `||c||2<sqrt(10)+1/10`.
Here is why the Hilbert–Schmidt assertion follows from the clock proof.
Replace the action difference in B.1's metric by the Hilbert–Schmidt norm
of its learned increment. The forward and adjoint difference bounds still
hold because `||K||op<=||K||HS`; the rank difference bound is identical in
these two norms. The same integrated contraction argument and Euler
recurrence give convergence in this stronger metric on each bounded
interval. This argument applies to (R2), whose controls are fixed signs
instead of residual feedback. Its elementary global finite-feature bounds
are `||c||infinity<=s`, `||A||op<=||A_0||op+s²/2`, and
`sum_a ||X_a||2<=integral_0^s ||A(v)||op v dv`. They provide the bounded
sets needed before using (R3).

At each fixed mesh the finite-program value theorem identifies every
contraction in the finitely many learned ranks. Their HS norm squared is
the finite double sum of the corresponding two Gram entries. Thus the
finite learned increments have the same HS bounds, with an arbitrarily
small slack, with probability tending to one. The finite unforced mesh
therefore lies strictly inside

\[
 \|A\|_{\rm op}<7,\qquad \|c\|_2<4,\qquad
 \|c(s_k)\|_\infty\le s_k .                                      \tag{R4}
\]

The finite initial readout is set to zero only for these auxiliary source
programs. The actual-network reference bridge at the end retains the
specified finite Gaussian readout.

###### 2. The source rule for the tanh clock, including zero forcing

At a fixed mesh with steps `h_k`, set `gamma_ka=h_k sigma_a/2` and make
both forward calls before both reverse calls, followed by simultaneous
updates (R2). On population 1 retain the entire root `(g_1,g_2)`. The scalar
source recursion is

\[
\begin{aligned}
 X_{ka}&=\sum_{r<k}\gamma_{ra} Q_{ra},&H^1_{ka}&=H(X_{ka},g_a),\\
 Z^2_{ka}&=\xi_{ka}+\sum_{r<k,b}a_{ka,rb}\delta_{rb},&
 c_k&=\sum_{r<k,b}\gamma_{rb}\phi(Z^2_{rb}),\\
 \delta_{ka}&=c_k\phi'(Z^2_{ka}),&
 Q_{ka}&=\zeta_{ka}+\sum_{r\le k,b}b_{ka,rb}H^1_{rb},\\
 a_{ka,rb}&=\alpha_{ka,rb}+\gamma_{rb}E_1[H^1_{ka}H^1_{rb}],&
 \alpha_{ka,rb}&=E_1[\partial_{\zeta_{rb}}H^1_{ka}],\\
 b_{ka,rb}&=\beta_{ka,rb}+1_{r<k}\gamma_{rb}E_2[\delta_{ka}\delta_{rb}],&
 \beta_{ka,rb}&=E_2[\partial_{\xi_{rb}}\delta_{ka}].
\end{aligned}                                                     \tag{R5}
\]

The centered source covariances, also between programs sharing the initial
matrix, are

\[
 E_2[\xi_{ka}\xi_{vb}]=E_1[H^1_{ka}H^1_{vb}],\qquad
 E_1[\zeta_{ka}\zeta_{vb}]=E_2[\delta_{ka}\delta_{vb}].             \tag{R6}
\]

The reverse Gaussian group is independent of the full first-row root.
Sources in different orientations belong to independent groups; the actual
matrix answers are dependent through their response terms. Formal
derivatives hold selected expectations, contraction coefficients and
covariances fixed. All named slots are retained even at zero variance.
Their complete chain rules include

\[
\begin{aligned}
 \partial X_{ka}&=\sum_{r<k}\gamma_{ra}\partial Q_{ra},&
 \partial H^1_{ka}&=\operatorname{sech}^4 J(X_{ka},g_a)\partial X_{ka},\\
 \partial c_k&=\sum_{r<k,b}\gamma_{rb}\phi'(Z^2_{rb})\partial Z^2_{rb},&
 \partial\delta_{ka}&=\phi'(Z^2_{ka})\partial c_k
             +c_k\phi''(Z^2_{ka})\partial Z^2_{ka},\\
 \beta_{ka,kb}&=1_{a=b}E_2[c_k\phi''(Z^2_{ka})].
\end{aligned}                                                     \tag{R7}
\]

We justify this source statement, rather than inferring it from values.
Choose a smooth root clipping function `chi_R` equal to the identity on
`[-R,R]`, with bounded image and `|chi_R'|<=1`, and replace `H(X,g)` by
`H(X,chi_R(g))`. Positivity of the scalar gate gives the exact identity

\[
 J_g(X,g)=\frac{\operatorname{sech}^2 J(X,g)}{
                         \operatorname{sech}^2 g}.
\]

One may derive it by differentiating the scalar ODE and solving its scalar
linear variational equation, or by differentiating
`F(J)=F(g)+X`, where `F(z)=z/2+sinh(2z)/4`.
Thus the clipped-root map has bounded first derivatives in both arguments.
Its `X` derivative stays bounded by one uniformly in `R`. Clip the readout
factor smoothly, with the clipping map equal to the identity on an open
neighborhood of the deterministic interval `[-10,10]`; since
`||c||infinity<=s_k<=10`, this changes no program value. All resulting
coordinate instructions now have bounded first derivatives, so III.F.1–5
applies, including its complete Gaussian conditioning proof and its
zero-query-noise argument. Expanding the learned ranks gives exactly (R5).

There is a uniform bound on every first *source* derivative of every fixed
scalar graph while earlier selected coefficients lie in a compact set.
Indeed the recursion has finitely many steps, `H_X` is bounded by one,
`|phi'|<=1`, `|phi''|<=2`, the readout is bounded, and every matrix node
is a source plus a finite linear combination of earlier nodes. Induction
through (R7) gives a finite deterministic bound. This bound is independent
of `R`: derivatives with respect to the root are never taken.

Now remove the root clipping chronologically. A convergent finite
covariance matrix has convergent positive-semidefinite square roots:
boundedness gives subsequential limits, each limit is a nonnegative square
root of the same matrix, and diagonalization gives its uniqueness. Couple
source prefixes using these square roots and fixed standard Gaussians.
At each finite instruction the expressions converge in probability.
The source derivative bound just proved gives uniform integrability of
their derivatives, so expected derivatives converge. Values are bounded or
have a common linear envelope in the finite source/root list, yielding L2
convergence. This closes the chronological induction for both coefficients
and values, even at a singular covariance. In particular the limit of (R7)
is precisely its displayed uncut expression.

These scalar values are the actual finite-program limits. For completeness,
on the same finite arrays the direct change of a first activation caused
by root clipping, at a fixed clock, has RMS at most
`2 [n^(-1) sum_i 1_{|g_ai|>R}]^(1/2)`. The rest of its change is bounded
by the clock RMS change because `|H_X|<=1`. Initial operator bounds and
finite graph subtraction then propagate these errors through every node.
The empirical Gaussian tail frequency converges by the elementary iid
law of large numbers. At each fixed clipping level the finite-program
theorem already applies; first let width grow, then remove clipping.
This identifies the scalar limit above with the uncut value limit.
Scalar contractions are treated in their causal order: their difference
is bounded by the two RMS errors times the bounded RMS factors, so the
same finite induction includes their actual empirical feedback. No
all-moment finite-width theorem or derivative in `g` is used.

Exactly the same argument covers a fresh root added with coefficient
`epsilon` to one complete query answer. For a fixed finite graph its
coefficients and expected source derivatives are continuous as
`epsilon->0`: the causal induction, covariance square-root coupling and
uniform source derivative bounds apply unchanged for `|epsilon|<=1`.
The expression convention fixes derivatives of variance-zero slots.
This continuity is what permits the final zero-forcing limit below.

###### 3. Explicit fresh-root pulse estimates

For two states with the same first roots, use

\[
 d=x+a+z,\quad x=\sum_{a=1}^2\|X_a-\bar X_a\|_2,\quad
 a=\|A-\bar A\|_{\rm op},\quad z=\|c-\bar c\|_2 .              \tag{R8}
\]

At finite width use explicitly
`x_n=sum_a ||X_na-bar X_na||_2/sqrt(n)`,
`a_n=||A_n-bar A_n||op`, and
`z_n=||c_n-bar c_n||_2/sqrt(n)`.
All finite Euclidean norms retain their ordinary meaning.

Suppose both states satisfy `||A||op<=M`, `||c||2<=C`, and
`||c||infinity<=s`. At a feature time `s`, factor subtraction gives

\[
\begin{aligned}
 \sum_a\|\Delta Z_a^2\|_2&\le2a+Mx,\\
 \sum_a\|\Delta\delta_a\|_2&\le2z+4sa+2sMx,\\
 \sum_a\|\Delta Q_a\|_2&\le2Ca+M(2z+4sa+2sMx).
\end{aligned}                                                     \tag{R9}
\]

For example the first term in the final line is the change of action
applied to a backward field of norm at most `C`; both such fields occur.
The three velocity differences, in the order of (R8), are consequently
bounded by

\[
\begin{aligned}
 \Delta F_X&\le sM^2x+(C+2sM)a+Mz,\\
 \Delta F_A&\le(sM+C/2)x+2sa+z,\\
 \Delta F_c&\le(M/2)x+a.
\end{aligned}                                                     \tag{R10}
\]

In the middle line the rank-one difference has norm at most
`||Delta delta||2+C||Delta H^1||2`. This verifies the estimate in
operator norm and also for a HS action difference. With `M=7,C=4`, the
sum is at most `L(s)d`, where

\[
 L(s)=\max\{8,5+16s,11/2+56s\}\le8+56s,
 \qquad E:=\exp(8S+28S^2),\quad S=10.                           \tag{R11}
\]

For a mesh ending by `S`, the subsequent Euler amplification is at most
`prod_k(1+h_k L(s_k))<=exp(sum_k h_k(8+56s_k))<=E`, since the
left Riemann sum of the increasing integrand is no larger than its
integral. Thus `E=exp(2880)`.

The required ball is legitimate for forcing. First choose the unforced
mesh sufficiently fine for (R4). At that fixed mesh and sufficiently
large width, all its state bounds hold with positive slack on an event
whose probability tends to one. Finite same-array subtraction, initially
using the crude global feature bounds, shows that the forced graph stays
within the ball `M=7,C=4` for all sufficiently small fixed `|epsilon|`
on this event and on `||e||2/sqrt(n)<=2`. The permitted epsilon may depend
on the fixed mesh but not on width. All later estimates therefore use
the uniform constants (R11). The readout supremum bound survives every
forcing exactly, because every readout increment is still a difference
of two bounded tanh activations. This is a local forcing argument at
zero, not a claim that arbitrary forcing preserves the energy identity.

Insert `epsilon e` into the complete reverse answer `Q_jb`, keeping all
earlier answers and the matrix fixed and recomputing its descendants.
The only immediate state increment is `h_j sigma_b epsilon e/2` in its
clock. Therefore, for `k>j`,

\[
 \frac{\|H^{1,\epsilon}_{n,ka}-H^{1,0}_{n,ka}\|_2}{\sqrt n}
       \le\tfrac12h_j E|\epsilon|\frac{\|e_n\|_2}{\sqrt n} .     \tag{R12}
\]

Instead insert the fresh root into one complete forward answer `Z^2_jb`.
Its activation changes in RMS by at most
`|epsilon| ||e_n||2/sqrt(n)`, its delta by at most
`2s_j |epsilon| ||e_n||2/sqrt(n)`, and its reverse answer by at most
`2Ms_j |epsilon| ||e_n||2/sqrt(n)`. The three immediate state changes have
total distance at most `h_j P |epsilon| ||e_n||2/sqrt(n)`, where

\[
 P=(M+1)S+1/2=161/2.
\]

At a later node a single delta difference is at most
`z+2s(a+M x)<=K d`, with

\[
 K=\max\{1,2SM\}=140.
\]

Consequently, for `k>j`,

\[
 \frac{\|\delta^\epsilon_{n,ka}-\delta^0_{n,ka}\|_2}{\sqrt n}
           \le h_j P K E |\epsilon|\frac{\|e_n\|_2}{\sqrt n} .  \tag{R13}
\]

We now extract the named coefficients with the precise order of limits.
Fix the mesh and a sufficiently small nonzero epsilon; apply the proved
joint value/source theorem to the forced and unforced graphs and the root,
letting width tend to infinity first. In its own population the new root
enters the complete scalar expression only through replacement of the
specified named source slot by that slot plus `epsilon e`. All Gaussian
source groups are independent of this local root. Their selected
covariances and all selected coefficients may depend on epsilon, but
are deterministic, and are held fixed under coordinate differentiation.
Induction through the expression gives

\[
 \partial_e V^\epsilon=\epsilon\partial_{\rm slot}V^\epsilon,
 \qquad E[eV^\epsilon]=\epsilon E[\partial_{\rm slot}V^\epsilon].  \tag{R14}
\]

The second identity is one-dimensional Gaussian integration by parts
conditional on the other roots and source groups. Its boundary term
vanishes, since these output values and first derivatives are bounded
at a fixed graph. The unused root is independent of the unforced graph,
so `E[eV^0]=0`. Passing the finite Cauchy–Schwarz pairing inequality to
the joint W2 limit in (R12) or (R13), and using `E[e²]=1`, bounds (R14)
after division by `|epsilon|`. Only then let epsilon tend to zero. The
coefficient and derivative continuity proved in Section 2 gives exactly

\[
 |\alpha_{ka,jb}|\le h_j E/2\ (j<k),\qquad
 |\beta_{ka,jb}|\le h_j P K E\ (j<k),\qquad
 |\beta_{ka,kb}|\le2S\,1_{a=b}.                                 \tag{R15}
\]

This order does not infer a derivative transverse to an unforced singular
support from its value law. The fresh root, the finite forcing estimate,
the source-form identity and the zero-forcing continuity each have a
separate role.

###### 4. Explicit Gaussian remainders and their passage to the flow

The two source variances in (R6) are at most `1` and `C²=16`. The
forward response remainder is bounded by
`S²(E+1)`, using (R15), `|delta|<=S` and `|E[H^1 H^1]|<=1`.
For a reverse answer, all past response coefficients have total absolute
sum at most `2S P K E`. Its learned coefficients have total absolute sum
at most `S C²`, since `|E[delta delta']|<=C²`. The two current
source coefficients contribute at most `2S` in total (only the matching
current sample occurs). Since `|H^1|<=1`,

\[
 Z^2_{ka}=\xi_{ka}+B_{ka},\quad |B_{ka}|\le100(E+1),\qquad
 Q_{ka}=\zeta_{ka}+D_{ka},\quad |D_{ka}|\le B_Q,
 \quad B_Q:=225400e^{2880}+180 .                                 \tag{R16}
\]

All constants are independent of the mesh, its number of nodes and width.
Their statements for mesh scalar laws require only sufficiently fine
meshes ending by `s_infty`, as already specified.

For clarity this decomposition passes to the already constructed common
flow, not merely to marginal subsequences. Adjoin a countable refining
mesh family to the common Gaussian language. Cross-program covariance
(R6) gives
`||xi_H-xi_H'||2=||H-H'||2` and
`||zeta_delta-zeta_delta'||2=||delta-delta'||2`.
These Gaussian source assignments extend by isometry to the closures of
their input spans. The transformed Euler convergence, strong multiplier
continuity and the bounded readout give uniform-in-time L2 convergence of
`H` and `delta`; therefore the sources converge too. Subtracting them
from the convergent actual fields shows that the remainders converge in
L2. An L2 limit of variables bounded in absolute value by `B_Q` has that
same bound: take an almost surely convergent subsequence, obtained by
choosing summable squared errors and applying Markov's inequality.
The analogous statement applies to the forward remainder. Hence at every
deterministic `s<=s_infty`,

\[
 Q_a(s)=\zeta_a(s)+D_a(s),\quad |D_a(s)|\le B_Q,\quad
 \operatorname{Var}\zeta_a(s)=\|\delta_a(s)\|_2^2\le10.            \tag{R17}
\]

The final variance improves from 16 to 10 by (R3). The Gaussian process
retains all cross-time/sample covariances and is independent of the whole
first-row root. No independence of the bounded remainder and the Gaussian
part is asserted. Jointly measurable representatives follow from the L2
continuous approximations; Fubini suffices for all time integrals.

For `R>=B_Q`, (R17) yields the explicit tail estimate

\[
 \sup_{s\le s_\infty,a}
 \|Q_a(s)1_{|Q_a(s)|>R}\|_2
 \le 4(\sqrt{10}+B_Q)
          \exp\!\left(-\frac{(R-B_Q)^2}{80}\right).               \tag{R18}
\]

To verify it, put `sigma=sqrt(10)` and write a standard normal `G`.
The relevant second moment is at most
`E[(sigma |G|+B_Q)² 1_{|G|>(R-B_Q)/sigma}]`.
Use `(u+v)²<=2u²+2v²`,
`1_{|G|>a}<=exp((G²-a²)/4)`,
`E exp(G²/4)=sqrt(2)` and
`E G² exp(G²/4)=2sqrt(2)`; these two Gaussian integrals follow by
completing the square and differentiating its elementary integral.
Taking square roots gives a bound no larger than the right-hand side
of (R18). A smaller actual source variance only decreases the original
dominating second moment under the coupling `zeta=sigma_actual G`.
If `R>=10` the readout tail is zero. Thus (R18) supplies the precise
individual reference tails in C.4.1 (T6); no maximum over training data
or whole circle is needed there.

These constants record a bounded targeted improvement. The elementary
global feature estimate `||A||<=3+S²/2` in the same argument gives a
far larger exponent. Restricting to the proved reference feature endpoint,
using its raw energy path length to obtain (R4), and integrating the
time-dependent stability coefficient reduces it to 2880. The resulting
remainder is still enormous: `log B_Q<2893`. This is a mathematical
certificate, with no claim of a useful-size empirical neighborhood.

###### 5. Using actual finite reference GF rather than transformed raw GD

Let `bar theta_n(t)` be the actual finite reference GF, from the stated
Gaussian initialization, including the random readout of variance `1/n²`.
B.1 applies with sum-loss mobilities `kappa_1=kappa_2=kappa_3=1/2`,
which gives exactly the present mean-loss physical equations. Its GF
width conclusion identifies the two active projections, the action
measurements and the readout. The two orthogonal projections determine
the full first row. No infinite-width input-law limit is used here.

For each fixed physical horizon `T`, reference finite GF has a
high-probability bound on the readout supremum, action norm, and all
three raw velocity norms, uniformly on `[0,T]`. One direct source is
finite risk dissipation followed by
`||c'||infinity<=2sqrt(R_n(0))` and the bounded-activation velocity
inequalities. These imply uniform L2 time-Lipschitz bounds for the two
reference backward answers. Indeed

\[
 \dot Q_a=\dot A^*\delta_a+A^*\dot\delta_a,\qquad
 \dot\delta_a=\dot c\,\phi'(Z_a^2)
                    +c\phi''(Z_a^2)\dot Z_a^2,
\]

and
`dot Z_a²=dot A H_a¹+A[phi'(Z_a¹)dot Z_a¹]`.
Every right-hand side has bounded L2 norm using only the stated finite
state and readout-supremum bounds. The population path has the same
continuity. This step needs no Gaussian tail estimate for an input
derivative or root derivative.

Here is a detailed uniform-time tail transfer. Define
`v_R(q)=q-clip_R(q)`; it is 1-Lipschitz. For `R>0`,

\[
 |q|1_{|q|>2R}\le2|v_R(q)|\le2|q|1_{|q|>R}.                    \tag{R19}
\]

At a fixed finite time grid, B.1 gives convergence of the empirical
averages of `|v_R(Q_a)|²`, which are continuous at-most-quadratic
measurements. One may obtain them equally by truncation and the backward
quadratic observable conclusion of that theorem. The time-Lipschitz
estimate extends their RMS norms from the finite grid to every time,
since `| ||v_R(Q(t))||2-||v_R(Q(t_j))||2 |<=||Q(t)-Q(t_j)||2`.
First let width grow at the fixed grid, then refine the grid. From (R18)
and (R19), for every fixed `R>=B_Q` and every positive `epsilon`,

\[
 \Pr\left\{\sup_{t\le T,a}\tau_{2R}(Q_{n,a}(t))
   >8(\sqrt{10}+B_Q)e^{-(R-B_Q)^2/80}+\epsilon\right\}\longrightarrow0.
                                                                    \tag{R20}
\]

The top readout tail vanishes on a high-probability event once its fixed
finite-horizon supremum bound is exceeded. This supplies finite empirical
reference tails for C.4's comparison with arbitrary actual networks.

Using this actual GF reference avoids treating transformed Euler as
exact raw GD. The reference derivative is the raw vector field exactly.
In a comparison with the piecewise affine actual GD path, the sole
algorithmic discrepancy is replacing its preceding state by its current
interpolated state; the raw finite-horizon velocity bound controls that
change. The reference construction's auxiliary meshes are fixed before
width tends to infinity, and removed afterwards. Actual GD steps remain
separate. A sufficient actual-step condition may be retained as
`eta_k sqrt(n_k)->0`, as in B.1; this response component alone claims
neither a rate nor removal of that restriction.

The component concludes a quantitatively bounded Gaussian response tail
for the fixed fitted reference and its finite-GF approximation. It does
not construct a global population flow for perturbed laws, and it does
not claim that whole-circle input derivatives have Gaussian tails.


##### C.4.5.3. Transfer to actual raw GD

###### 1. Exact fields and comparison constants

Put `u=x/sqrt(2)` and `phi=tanh`. On the canonical two population spaces use
the full state `theta=(w,A,c)`, where `w in L2(Omega_1;R2)`,
`A:L2(Omega_1)->L2(Omega_2)` is bounded and `c in L2(Omega_2)`. Set

\[
 Z^1(u)=w\cdot u,\quad H^1(u)=\phi(Z^1(u)),\quad
 Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),\quad
 f(u)=\langle c,H^2(u)\rangle,
\]
\[
 r(u,y)=f(u)-y,\quad \delta^2(u)=c\phi'(Z^2(u)),\quad
 Q(u)=A^*\delta^2(u),\quad \delta^1(u)=\phi'(Z^1(u))Q(u).
\]

The unhalved mean-loss field, with exactly the prescribed mobilities, is

\[
 F_\lambda(\theta)=-2\left(
 \int r\delta^1u\,d\lambda,
 \int r\delta^2\otimes H^1\,d\lambda,
 \int rH^2\,d\lambda\right).                                      \tag{1}
\]

The rank-one action is `(v tensor h)g=v E_1[hg]`. The distance is

\[
 D(\theta,\bar\theta)=\|w-\bar w\|_{L^2(\Omega_1;\mathbb R^2)}
 +\|A-\bar A\|_{op}+\|c-\bar c\|_{L^2(\Omega_2)}.                 \tag{2}
\]

For two networks of the same width replace the three norms respectively by
`||W1-W1bar||F/sqrt(n)`, `||W2-W2bar||op`, and
`||W3-W3bar||2/sqrt(n)`; call this `D_n`. The finite rank is `v h^T/n`.
There is no comparison in operator norm across widths or carriers.

Here is an explicit version of the maintained C.4 transport lemma. Suppose
each individual state norm in (2) is at most `B=12`; the norms in this premise
are of each state component, not of a difference. Define
`tau_R(v)=||v 1_(|v|>R)||2` and

\[
 \mathcal T_R(\bar\theta)
 =\tau_R(\bar c)+\tfrac12\sum_{a=1}^2\tau_R(\bar Q(e_a)).
\]

For any probability law lambda on the binary observation space, any `R>=1`,
and the fixed reference nu_* of the question,

\[
 \|F_\lambda(\theta)-F_{\nu_*}(\bar\theta)\|_{(2)}
 \le 10^6\{(1+R)[D(\theta,\bar\theta)+W_1(\lambda,\nu_*)]
                         +\mathcal T_R(\bar\theta)\}.             \tag{3}
\]

This holds also in the normalized finite norms, with the same constant.
Here are arithmetic details making the constant checkable. For a coupling
pair `(u,y),(v,z)`, set `h=|u-v|`, `d=D`, and `l=|y-z|`. Then

\[
 \|Z^1-\bar Z^1\|_2\le B(d+h),\quad
 \|Z^2-\bar Z^2\|_2\le B(B+1)(d+h),\quad
 |r-\bar r|\le B^3(d+h)+l.                                      \tag{4}
\]

The bounds use `|phi|,|phi'|<=1` and `Lip(phi')<=2`. For any fixed reference
field v, splitting at `|v|=R` gives
`||[phi'(z)-phi'(zbar)]v||2 <=2R||z-zbar||2+2tau_R(v)`.
Writing `a=B(B+1)=156`, successive subtraction therefore gives

\[
 \|\delta^2-\bar\delta^2\|_2
 \le313(1+R)(d+h)+2\tau_R(\bar c),
\]
\[
 \|\delta^1-\bar\delta^1\|_2
 \le3792(1+R)(d+h)+24\tau_R(\bar c)+2\tau_R(\bar Q(v)).           \tag{5}
\]

For the lower, middle and readout integrands, respectively, the coefficients
of `(1+R)(d+h+l)` before the overall factor 2 are at most

\[
 B^2(B^3+1)+(B+1)3792+(B+1)B^2,
\]
\[
 B(B^3+1)+(B+1)313+(B+1)B^2,
 \qquad B^3+1+(B+1)a.
\]

Twice their sum is less than `10^6`. The total reference-tail coefficient
is at most `4(B+1)(B+1)=676`, also below `10^6`. These decompositions include
the explicit changed input vector in `r delta^1 u`. Integrating the estimates
against a coupling and taking the infimum of its cost proves (3).
No maximum over actual observations, positive Gram eigenvalue or atom-weight
bound occurs. The full Gaussian row enters (4) only through its L2 norm.

For same-input prediction and activation comparisons on this ball,

\[
 \sup_u|f_\theta(u)-f_{\bar\theta}(u)|\le2B^2D,
 \quad\sup_u\|H^\ell_\theta(u)-H^\ell_{\bar\theta}(u)\|_2
 \le(B+1)D\quad(\ell=1,2).                                    \tag{6}
\]

Every such predictor has `|f|<=B` and Lipschitz constant at most `B^3` in u.
Thus its binary squared-loss integrand has joint Lipschitz constant

\[
 L_{risk}=2(B+1)B^3=44928,\qquad
 |R_\lambda(f)-R_\rho(f)|\le L_{risk}W_1(\lambda,\rho).           \tag{7}
\]

###### 2. Actual finite reference GF and uniform observable passage

Let `bar theta_n(t)` be the actual finite gradient flow on nu_*, started from
exactly the same three initialized arrays as the network to be compared.
In particular its finite readout is not zero. Finite dynamics §§1–4 gives
global existence and the exact raw-metric energy identity. With probability
tending to one, initialization satisfies

\[
 \|W^1_0\|_F/\sqrt n\le2,\quad\|W^2_0\|_{op}\le3,\quad
 \|W^3_0\|_2/\sqrt n\le1/4,\quad\|W^3_0\|_\infty\le1.
                                                                    \tag{8}
\]

The first/readout assertions follow from Gaussian second moments and the
Gaussian union bound; the sharp matrix bound is proved in global-nonlinear
A.3. Initial loss is at most `25/16`. Up to `T=40`, every block displacement
in its raw metric is at most `sqrt(40*25/16)<8`, by energy and Cauchy–Schwarz.
Consequently each reference component norm is strictly below 11. Its readout
coordinate bound is at most `1+2T sqrt(25/16)=101`, because the mean absolute
residual is bounded by the square root of the nonincreasing loss. These
bounds apply to the actual finite flow, including its nonzero readout.

For this particular reference, B.1 applies with two orthogonal inputs,
sigma_1=sigma_2=1, beta=1, both activations tanh and kappa_i=1/2 to convert
its sum loss into the present mean loss. Its construction uses the same
fixed first Gaussian pair and initialized action with its actual adjoint.
Its unique population flow is the one in Section C.4.5.1. The two active lower
projections determine the full first row since they are precisely its two
columns. Thus all passive circle inputs are evaluated using the same trained
row, without creating extra training observations.

We spell out the additional uniform observations needed here. At fixed
auxiliary transformed mesh Delta, append finitely many passive forward
evaluations and the active queries `Q_a=A* [c phi'(Z2_a)]` to B.1's oracle
program. Its value theorem A.1 and complete III.F fixed-program construction
give the joint node laws and second moments. The readout product can be
clipped beyond its proven coordinate bound, so it is globally Lipschitz in
its varying arguments. The transformed same-root comparison bounds the
finite-flow/mesh error uniformly in width; learned action differences use
operator norm. Its forward estimates also control the passive directions.
The Q difference is bounded in L2 by

\[
 \|A-\widetilde A\|_{op}\|c\|_2+
 \|\widetilde A\|_{op}
 (\|c-\widetilde c\|_2+2\|\widetilde c\|_\infty
                                  \|Z^2-\widetilde Z^2\|_2).
                                                                    \tag{9}
\]

First take width to infinity with Delta fixed, then remove Delta. This proves
the fixed-time joint second-moment limits for Q, the forward fields and paired
initial/current activations. It does not apply a finite-program theorem to
the growing actual GD transcript.

The passage is uniform in physical time. On (8), the reference has uniformly
bounded raw velocities on `[0,40]`, by (1) and the preceding bounds. Strong
curve differentiation gives `dot Z2=dot A H1+A phi'(Z1)dot Z1`, and
`dot delta2=dot c phi'(Z2)+c phi''(Z2)dot Z2`. Their L2 norms are uniformly
bounded using `|c|<=101`. Differentiating `Q=A*delta2` then bounds its L2
time-Lipschitz constant independently of width. The population proof is
identical. Norms of positive-part cutoffs of Q inherit this Lipschitz constant.
A fixed finite time grid followed by its refinement therefore extends every
needed cutoff second-moment comparison uniformly in time. Forward evaluations
are Lipschitz in input with constants bounded by the state norms. A fixed
finite input net, after the time net, proves

\[
 \sup_{t\le40,u\in S^1}|\bar f_n(t,u)-f_*(t,u)|\longrightarrow0
                         \quad\text{in probability}.              \tag{10}
\]

The same argument for the bounded squared displacement integrand, retaining
the same neuron at time zero and current time in the fixed programs, gives

\[
 \sup_{t\le40,u}\left|\frac1n
 \|\bar h^\ell_n(t,u)-h^\ell_n(0,u)\|_2^2
 -\mathbb E_\ell|H^\ell_*(t,u)-H^\ell_0(u)|^2\right|
 \longrightarrow0\quad\text{in probability}.                       \tag{11}
\]

Here no individual finite neuron is coupled with an invented population neuron.

The response proof supplies, on the reference feature segment through its
interpolating endpoint, `Q_a=G_a+E_a`, with `G_a` centered Gaussian of variance
at most 16, `|E_a|<=M_Q`, and

\[
 M_Q=225400e^{2880}+180<e^{2893}.                                  \tag{12}
\]

Also `|c_*|<=10`. For `R>=4M_Q+20`, elementary Gaussian integration gives

\[
 \sup_{t\le40}\mathcal T_R(\bar\theta_n(t))
 \le H e^{-R^2/4096}+o_{\mathbb P}(1),\qquad H=16(4+M_Q).          \tag{13}
\]

Every `o_P(1)` here is at fixed R and on one fixed reference. To check the
constants, if `G` has variance at most `sigma²`, then
`E exp(G²/(4sigma²))<=sqrt(2)`. Splitting `Q=G+E` and using
`x²<=8sigma² exp(x²/(8sigma²))` bounds
`tau_r(Q)<=8(sigma+M_Q)exp(-r²/(64sigma²))` for `r>=2M_Q`.
At finite width `tau_R(Q_n)<=2||(|Q_n|-R/2)_+||2` and this latter norm
converges uniformly in time to its population counterpart by (9) and the
time-grid argument. Take sigma=4 and r=R/2. The readout has no tail at
R>101 at finite width on (8). Our final R is much larger. This proves (13).

###### 3. Raw GD comparison, stopping, and limit order

Actual finite raw GD is exactly
`theta_(j+1)=theta_j+eta F_lambda(theta_j)` for (1). It does not update a
transformed clock. For completeness its states have a width-independent
bound on every fixed horizon, for any probability law. If c_j is its readout
RMS, then `1+c_(j+1)<=(1+2eta)(1+c_j)`. Hence `c_j<=2e^(2(T+1))` for
initial c_0<=1 and nodes through T+eta, eta<=1. Writing this bound as C_T,
the middle norm is at most `3+2(T+1)(C_T+1)C_T=:A_T`, and the full-row RMS
is at most `2+2(T+1)(C_T+1)A_T C_T`. These estimates follow directly from
successive raw increments, not a GD energy inequality.

Sharper constants in the comparison come from stopping at the first time
`D_n(theta_GD(t),bar theta_n(t))=1`. Before that time both states have
individual norms at most B=12. The GD preceding-node state also lies there:
its preceding time has not exited. Both interpolant speeds on this prefix
are bounded by

\[
 V=2(B+1)(B^2+B+1)=4082.
\]

At time t the GD preceding state differs from its interpolant by at most
V eta. Apply (3) against the actual reference GF at t, integrate the velocity
difference, and use (13). Initial distance is exactly zero. With
`K=40*10^6=40000000` and `q=W1(lambda,nu_*)`, Gronwall gives, on the stopped
interval,

\[
 \sup_{t\le40}D_n(\theta_{GD}(t),\bar\theta_n(t))
 \le K e^{K(1+R)}\{(1+R)(q+V\eta)
                           +H e^{-R^2/4096}+o_{\mathbb P}(1)\}.   \tag{14}
\]

The supremum in (14) is first understood up to the stopping time. If its
right side is strictly less than one, continuity excludes that stopping
time, and the estimate holds through 40. All probabilities in (14) come from
initialization and the one fixed reference; the bound otherwise applies to
every actual law with the displayed q. A stochastic actual law is therefore
handled on its event controlling q, without any law-dependent width theorem.

The limit order is: fix T, the reference, the cutoff R and an auxiliary
accuracy; establish the reference GF observations by fixed transformed mesh,
width limit, then mesh removal; use those resulting reference statements in
(14) and send the actual width to infinity and its step to zero. Auxiliary
proof meshes never become actual GD steps. No transformed Euler increment is
claimed to equal a raw GD increment; (14) compares actual raw GD directly to
actual raw GF. The sufficient condition `eta_k sqrt(n_k)->0` requested in
the primary theorem is permissible. In fact this particular final comparison
uses only `eta_k->0`, because B.1 is used for the reference GF, not for an
actual reference GD sequence.

###### 4. Remaining assembly interface

The numerical error tolerance, the exact certified radius, activity time and
positive activity margin are fixed in the theorem above using Section C.4.5.1 and
Section C.4.5.2. For any tolerance d0<1, it suffices to choose R and delta with

\[
 K H\exp(K(1+R)-R^2/4096)\le d_0/4,\qquad
 K(1+R)\exp(K(1+R))\delta\le d_0/4.                             \tag{15}
\]

Then for any deterministic empirical sequence lambda_k with
`W1(lambda_k,mu)->0`, `W1(mu,nu_*)<delta`, the positive excess of the full
time-uniform same-width state distance over d0/2 tends to zero in probability.
There is no assertion that perturbed trajectories converge to a unique global
population trajectory. Equations (6), (7), (10), (11) transfer the observable
conclusions without that assertion.

For iid empirical laws of sizes m_k->infinity, independent of initialization,
`W1(lambda_k,mu)->0` in probability. A direct proof partitions the compact
observation space into finitely many Borel cells of diameter epsilon, moves
each law to the same representatives at cost at most epsilon, and bounds the
remaining transport by half the diameter (at most 4) times the sum of cell
mass discrepancies. Each empirical cell mass has variance at most 1/(4m_k).
First send m_k to infinity at fixed partition, then epsilon to zero. A union
bound with the initialization/reference events proves the same joint limits
for arbitrary width/sample growth rates. This gives probability tending to
one for every fixed mu and sequence. No numerical finite-width rate, almost
sure joint convergence or uniform failure probability over laws is asserted.

#### C.4.6. Trained data response at the fitted tanh reference

This section constructs and controls the response to changed training data
at the nonlinear fitted reference of C.4.5. Finite GF is differentiated
before width tends to infinity. The width theorem holds on each fixed
physical horizon; the homogeneous population propagator has a separate
bound uniform in physical time. The present section is infinitesimal: it
does not construct a nonlinear population flow for a changed law or a
finite-contamination remainder. Section [C.4.7](#c47-nonlinear-training-near-the-fitted-tanh-reference)
separately supplies nonlinear population continuation and actual finite-GF
capture near this reference through physical time 40, with a nonlinear
remainder and a width-first bridge to the response constructed here.

Equation labels C.4.6.T, C.4.6.P, C.4.6.S and C.4.6.F belong respectively
to the statement, propagator proof, source proof and finite-capture proof.
The learned middle increment is K; the two-by-two training Gram is Gamma.

##### C.4.6.1. Model, equation and theorem

###### Model and meaning of the response

Let `Y≥1`, `u=x/sqrt(2)∈S¹`, and use two tanh hidden layers of equal width n,
no biases, and

\[
 z^1=W^1u,\quad h^1=\tanh z^1,\quad z^2=W^2h^1,\quad
 h^2=\tanh z^2,\quad f_n=(W^3)^Th^2/n.
\]

All initialized entries and blocks are independent centered Gaussians, with
stored variances `(1,1/n,1/n²)`. The mobilities are `(n,1,n)` and the loss
is the unhalved mean square. Time t is physical GF time. For a nonatomic
training law the finite loss is integrated exactly against that law.

Fix `nu*=½delta_(sqrt(2)e1,+1)+½delta_(sqrt(2)e2,-1)` and any deterministic
Borel probability law nu on `Z=sqrt(2)S¹×[-Y,Y]`. Set
`mu_epsilon=(1-epsilon)nu*+epsilon nu`, `sigma=nu-nu*`. Use the same three
initialized arrays for every epsilon, retaining the actual finite Gaussian
readout. The observable is the right derivative

\[
 D_\sigma f_n(t,x)=\left.\frac{d}{d\epsilon^+}
                  f_{n,\mu_\epsilon}(t,x)\right|_{\epsilon=0}.
 \tag{C.4.6.T1}
\]

This derivative is taken at each finite n before n tends to infinity.
It is not defined by differentiating a nonlinear population law-to-flow
map. No such perturbed population map through an arbitrary T is assumed.

###### State, exact equation and observations

Use the established canonical reference action spaces
`H_i=L²(Omega_i)` and the actual reference `(w(t),A(t),c(t))`, including its
full first row and both orientations of `A=A0+K`. The initialized action
A0 is bounded and its reverse is its actual Hilbert adjoint; only K is
Hilbert–Schmidt. The fitted endpoint is the established first b=1 state
of the autonomous reference feature equation, at feature time at most ten.

Put `phi=tanh` and `F(z)=z/2+sinh(2z)/4`. Direct differentiation gives
`F'(z)=(1+cosh(2z))/2=cosh²z>0`; its limits at the two infinities
are the corresponding infinities, so its inverse is globally defined. Set
`X_a=F(w_a)-F(g_a)`. Equivalently, `w_a=j(X_a,g_a)` with
`j_X=phi'(j)` and `j(0,g)=g`, so `D_a=phi'(w_a)` and the raw row variation
is
\[
 \delta w_a=D_a\xi_a,\qquad D_a=\phi'(w_a),\quad w_a=j(X_a,g_a).
 \tag{C.4.6.T0}
\]
The tangent Hilbert space and finite same-width norm are

\[
 \mathcal V=L^2(\Omega_1;\mathbb R^2)\oplus
             \mathcal S_2(H_1,H_2)\oplus H_2,\qquad
 \|v\|_{\mathcal V}^2=\|\xi\|_2^2+\|B\|_{HS}^2+\|d\|_2^2,
 \tag{C.4.6.T2}
\]
\[
 \|v_n\|_{\mathcal V_n}^2=\|\xi_n\|_F^2/n+\|B_n\|_F^2+\|d_n\|_2^2/n.
 \tag{C.4.6.T3}
\]

Here `v=(xi,B,d)` and the raw variation is
`((phi'(w_a)xi_a)_a,B,d)`. Thus its raw norm is at most `||v||_V`.
The inverse conversion need not be bounded. The population norm (C.4.6.T2) and
finite norm (C.4.6.T3) are never subtracted across different carriers.

At every passive direction u define

\[
 Z^1(u)=w\cdot u,\quad H^1(u)=\phi(Z^1(u)),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad \delta(u)=c\phi'(Z^2(u)),\quad
 Q(u)=A^*\delta(u),\quad r(u,y)=\langle c,H^2(u)\rangle-y.
 \tag{C.4.6.T4}
\]

For later use, denote by `q(t,u)` the three-component vector inside the
following integral. In integrals written in u, sigma denotes its pushforward under
`(x,y)->(x/sqrt(2),y)`. The forcing, linear in sigma, is

\[
 b_\sigma(t)=-2\int_{S^1\times[-Y,Y]} r(t,u,y)
 \left(
  \left(u_a\frac{\phi'(w(t)\cdot u)}{\phi'(w_a(t))}Q(t,u)\right)_{a=1,2},
  \delta(t,u)\otimes H^1(t,u),\ H^2(t,u)
 \right)\,d\sigma(u,y).
 \tag{C.4.6.T5}
\]

The rank-one action is `(q tensor h)v=q E_1[hv]`; its finite representative
is `q h^T/n`. Formula (C.4.6.T5) includes the loss factor two and the signed
reference subtraction. It also retains the forward and adjoint uses of
the same initialized Gaussian action.

With the exact synthesis, evaluation and residual-curvature operators
defined in C.4.6.2, (C.4.6.P8)–(C.4.6.P11), the forced evolution is

\[
 \dot v_\sigma(t)=\mathcal L(t)v_\sigma(t)+b_\sigma(t),\qquad
 \mathcal L(t)=-2S(t)E(t)+\mathcal C(t),\qquad v_\sigma(0)=0.
 \tag{C.4.6.T6}
\]

All coefficients are computed from the autonomous reference state.
Their source is not a future-trajectory oracle. They define bounded
strongly continuous operators on (C.4.6.T2); no ambient Fréchet differentiability
of an L²-valued nonlinear vector field is asserted.

For a tangent `v=(xi,B,d)` define, at each passive `u`,

\[
\begin{aligned}
 \dot z_v^1(u)&=\sum_a u_aD_a\xi_a,&
 \dot h_v^1(u)&=\phi'(w\cdot u)\dot z_v^1(u),\\
 \dot z_v^2(u)&=B H^1(u)+A\dot h_v^1(u),&
 \dot h_v^2(u)&=\phi'(Z^2(u))\dot z_v^2(u),\\
 e_u(v)&=\langle d,H^2(u)\rangle+\langle c,\dot h_v^2(u)\rangle,\\
 \dot\delta_v^2(u)&=d\phi'(Z^2(u))
                     +c\phi''(Z^2(u))\dot z_v^2(u),&
 \dot Q_v(u)&=B^*\delta(u)+A^*\dot\delta_v^2(u).
\end{aligned}                                                     \tag{C.4.6.T14}
\]

Dots carrying a subscript `v` in (C.4.6.T14) mean directional variations, not
physical-time derivatives. All products have the displayed layer type.
Both `A` and `A*` are used literally. The scalar `e_u(v)` equals
`ell(t,u)v`. 
The prediction derivative produced by (C.4.6.T6) is

\[
 \mathscr D_\sigma f(t,\sqrt2u)=\ell(t,u)v_\sigma(t),
 \quad \ell(t,u)v=\langle d,H^2(u)\rangle+
 \langle\delta(u),BH^1(u)+A[\phi'(w\cdot u)
                   \sum_a u_a\phi'(w_a)\xi_a]\rangle.
 \tag{C.4.6.T7}
\]

The lower hidden response has norm at most `||v||_V`; both the upper
preactivation and activation responses have norm at most `(3+sqrt(10))||v||_V`.
Uniformly in all physical times and circle inputs,
`||ell(t,u)||≤L0<17`, with L0 defined in C.4.6.2, (C.4.6.P12).

###### Theorem and quantitative bounds

The conclusions are proved in C.4.6.2–C.4.6.4. The reference
construction is the one in B.1 and C.4.5.1–2, on the common Gaussian
action spaces of special-data III.F. The fixed-program value and response
extensions are A.1–A.2; their singular-query and adjunction conclusions
are retained throughout.

**Admissible forcing and well-posed evolution.** Let `M_0(Z)` be the real
Banach space of finite signed Borel measures of mass zero, with total
variation *mass* `||sigma||TV=|sigma|(Z)` (no factor one-half).
The integrand in (C.4.6.T5) is a continuous `mathcal V`-valued function and the integral is
a Bochner integral. Its bounded linear extension to `M_0(Z)` is justified
by (C.4.6.T5), rather than by a two-sided probability neighborhood. Equation (C.4.6.T6)
has a unique strong solution for every such sigma and every finite horizon.

The weighted-source proof establishes finiteness of the reference quantity

\[
 M_w=\sup_{t\ge0,\,u\in S^1,\,a=1,2}
          \|\cosh^2(w_a(t))Q(t,u)\|_2<\infty.
 \tag{C.4.6.T8}
\]

In particular, putting

\[
 C_{b,Y}=2(\sqrt{10}+Y)\sqrt{M_w^2+11},
 \qquad \sup_{t\ge0}\|b_\sigma(t)\|_{\mathcal V}
                       \le C_{b,Y}\|\sigma\|_{TV},
 \tag{C.4.6.T9}
\]

is valid: the row norm uses `sum_a u_a²=1`, the middle rank has norm
at most `sqrt(10)`, and the readout factor has norm at most one.
The exact envelope `cosh² w_a≤cosh² g_a+2|X_a|` and actual finite cavity
moments supply the weighted integrability in (C.4.6.T8). RMS value convergence
alone is not the proof of that step.

**Actual finite-GF capture.** For every fixed nu as above and every fixed
`T<infinity`, including `T=40`,

\[
 \sup_{0\le t\le T,\,x\in\sqrt2S^1}
       |D_\sigma f_n(t,x)-\mathscr D_\sigma f(t,x)|
          \longrightarrow0\quad\hbox{in probability}.
 \tag{C.4.6.T10}
\]

The probability is over the initialized arrays. The state is identified
by same-width finite-program approximations in the uniform-in-time norm
(C.4.6.T3), whose canonical counterparts converge in (C.4.6.T2). Their finite rank
expansions identify middle Hilbert–Schmidt inner products and both action
directions. Joint named same-layer fields converge with their second moments
at every finite list of times and passive inputs. Section C.4.6.4 specifies
this topology and proves the stronger comparison needed to justify (C.4.6.T10).
It does not assert operator-norm convergence of finite matrices to operators
on another carrier, or hidden tangent path laws beyond the stated topology.

Every deterministic estimate is independent of the support size, smallest
atom weight and Gram rank of nu. Convergence is for each fixed nu; a failure
probability uniform over all laws is not part of (C.4.6.T10). No rate is asserted.

**Uniform population propagation.** Let U(t,s) be the homogeneous evolution
of (C.4.6.T6). Section C.4.6.2 proves

\[
 \sup_{0\le s\le t<\infty}\|U(t,s)\|\le C_U<\infty,
 \qquad v_\sigma(t)=\int_0^tU(t,s)b_\sigma(s)\,ds,
 \tag{C.4.6.T11}
\]
\[
 \sup_{t\le T}\|v_\sigma(t)\|_{\mathcal V}
       \le C_U C_{b,Y}T\|\sigma\|_{TV},\qquad
 \sup_{t\le T,x}|\mathscr D_\sigma f(t,x)|
       \le L_0 C_U C_{b,Y}T\|\sigma\|_{TV}.
 \tag{C.4.6.T12}
\]

For a strongly measurable general forcing in `L1_loc`, the solution is
strongly absolutely continuous and satisfies its equation almost everywhere.
The data forcing here is continuous, hence its solution is strongly C1.
The admissible general forcing norm is `L¹([0,T];mathcal V)`; (C.4.6.T11) bounds response
by C_U times that norm. In (C.4.6.T12), contamination directions obey `||sigma||TV≤2`.

For conditioning, `Gamma_infty=E_infty S_infty=S_infty*D_infty S_infty`,
where `D_infty` multiplies the row blocks by `phi'(w_a,infty)²` and is
identity on the other blocks. `D_infty` is injective, although it has no
uniform positive lower bound; the finite training Gram may be singular. Hence `ker Gamma_infty=ker S_infty=ker E_infty*`.
Its finite-dimensional pseudoinverse
is well defined and the explicit bound is

\[
 B_\infty=1+\|S_\infty\|\|\Gamma_\infty^+\|\|E_\infty\|,
 \qquad C_U=B_\infty\exp(B_\infty J_0),
 \tag{C.4.6.T13}
\]

with the completely specified finite J0 in C.4.6.2, (C.4.6.P22). The proofs
give finiteness through reference quantities, not an evaluated numerical
certificate for endpoint conditioning or a useful numerical response constant.
They assume no spectral gap or full-rank endpoint Gram. Uniform population
propagation is separate from fixed-horizon finite-width convergence (C.4.6.T10).

##### C.4.6.2. Uniform control of the trained propagator

###### 1. Reference bounds

For the active inputs `e_a`, specialize the shared fields as

\[
 H_a^1=\phi(w_a),\quad Z_a^2=AH_a^1,\quad H_a^2=\phi(Z_a^2),
 \quad\delta_a=c\phi'(Z_a^2),\quad Q_a=A^*\delta_a.
 \tag{C.4.6.P1}
\]

Let `y1=1,y2=-1`, `p1=p2=1/2`. The reference prediction and residual
are `f_a=y_a b(t)` and `r_a=-y_a e(t)`, where `e=1-b>0`.
The established autonomous feature equation has its first `b=1` endpoint
at feature time `s_dagger<=10`; physical time satisfies `ds/dt=2e(t)`.
Its quantitative conclusions, including the endpoint on these same spaces,
are

\[
 e(t)\le e^{-t/5},\qquad
 d_{\rm ref}(t):=\|\theta(t)-\theta_\infty\|_{\rm raw}
       \le\sqrt{10}\,e(t),
 \tag{C.4.6.P2}
\]
\[
 \|A(t)\|\le M:=2+\sqrt{10},\quad
 \|c(t)\|_2\le C:=\sqrt{10},\quad
 \|c(t)\|_\infty\le10.
 \tag{C.4.6.P3}
\]

The endpoint has all the same bounds. Here the raw increment norm is
row `L²` plus middle `HS` plus readout `L²`, combined in a square sum.
The active source result C.4.5.2, (R17), also gives at the endpoint

\[
 Q_{a,\infty}=\zeta_a+R_{Q,a},\qquad
 \zeta_a\sim N(0,v_a),\quad v_a\le10,\quad |R_{Q,a}|\le B_Q,
 \quad B_Q=225400e^{2880}+180.
 \tag{C.4.6.P4}
\]

No independence of `R_Q,a` and `zeta_a` is needed. In particular,

\[
 \max_a\|Q_{a,\infty}\|_4\le
 M_4:=3^{1/4}\sqrt{10}+B_Q<\infty,
 \tag{C.4.6.P5}
\]

by the triangle inequality and `E G^4=3` for a standard normal.
These are reference-only, active-query facts. No passive-query higher
moment claim or finite-width higher moment inference is used here.

###### 2. The typed tangent equation and its bounded coefficients

Use the space and scalar clock relation (C.4.6.T2) and (C.4.6.T0).

The raw variation is the bounded injective image

\[
 R(t)v=((\phi'(w_a)\xi_a)_{a=1,2},B,d),\qquad \|R(t)\|\le1.
 \tag{C.4.6.P7}
\]

Its inverse is not assumed bounded. In particular, (C.4.6.T2) is a stronger
norm than the pulled-back raw norm and is the norm used for the propagator.

For each training datum define the following bounded directional maps:

\[
 h_a[v]=\phi'(w_a)^2\xi_a,\quad
 z_a[v]=BH_a^1+Ah_a[v],\quad
 d_a[v]=d\phi'(Z_a^2)+c\phi''(Z_a^2)z_a[v],
\]
\[
 q_a[v]=B^*\delta_a+A^*d_a[v],\qquad
 \ell_a[v]=\langle d,H_a^2\rangle_2+
                       \langle\delta_a,z_a[v]\rangle_2.
 \tag{C.4.6.P8}
\]

Define synthesis `S(t):R²->mathcal V` and evaluation `E(t):mathcal V->R²` by columns
and components,

\[
 G_a=(\mathbf e_a Q_a,\delta_a\otimes H_a^1,H_a^2),\quad
 S\alpha=\sum_a\sqrt{p_a}\alpha_aG_a,\quad
 (Ev)_a=\sqrt{p_a}\ell_a[v].
 \tag{C.4.6.P9}
\]

The residual-curvature part is the bounded linear map

\[
 \mathcal C(t)v=-2\sum_a p_ar_a(t)T_a(t)v,
\]
\[
 T_av=(\mathbf e_a q_a[v],
             d_a[v]\otimes H_a^1+\delta_a\otimes h_a[v],
             \phi'(Z_a^2)z_a[v]).
 \tag{C.4.6.P10}
\]

The homogeneous generator is exactly

\[
 \mathcal L(t)=-2S(t)E(t)+\mathcal C(t).
 \tag{C.4.6.P11}
\]

Indeed the transformed reference vector field is
`-2 sum_a p_a r_a G_a`: its first block is
`X'_a=-2p_a r_a Q_a`, with no own first gate. The product rule produces
`-2 sum p_a ell_a[v] G_a` and (C.4.6.P10). Equations (C.4.6.P8) follow successively
by scalar differentiation, action differentiation and actual adjunction.
In raw first coordinates differentiating the gate would give
`phi''(w_a) delta w_a Q_a`; differentiating
`delta w_a=phi'(w_a)xi_a` in physical time produces the same term
on the left and cancels it. Thus its absence in (C.4.6.P10) is exact.

All maps in (C.4.6.P8)–(C.4.6.P11) exist on every `v in mathcal V`. Put

\[
 a_1=1+20(1+M),\quad a_q=C+Ma_1,\quad
 a_*=[a_q^2+(a_1+C)^2+(1+M)^2]^{1/2},\quad
 L_0=[1+C^2(1+M^2)]^{1/2}<17.
 \tag{C.4.6.P12}
\]

For a unit `v`, (C.4.6.P3), `|phi'|<=1`, `|phi''|<=2`, and
`||B||op<=||B||HS` give

\[
 \|h_a[v]\|_2\le1,\quad\|z_a[v]\|_2\le1+M,
 \quad\|d_a[v]\|_2\le a_1,\quad\|q_a[v]\|_2\le a_q.
\]

The middle component of `T_a v` has HS norm at most `a1+C`, and
the last has norm at most `1+M`. Consequently

\[
 \|T_a(t)\|\le a_*,\quad
 \|\mathcal C(t)\|\le2a_*e(t),\quad
 \|S(t)\|\le L_0,\quad\|E(t)\|\le L_0.
 \tag{C.4.6.P13}
\]

For the synthesis estimate, each column before its `sqrt(p_a)` factor
has squared norm at most `M²C²+C²+1`; the column Cauchy–Schwarz
inequality gives the operator bound. The evaluation estimate follows
also from (C.4.6.P14) below.

The generator is strongly continuous on `mathcal V`. To see this without an
unjustified operator-norm continuity assertion, first fix `v`. The
reference raw fields are strongly continuous, `A` is HS-continuous in
its increment, and `c` is continuous in supremum norm because
`c_s=(H1²-H2²)/2` is bounded by one pointwise. If bounded continuous
multipliers converge in probability, their product with a fixed L²
vector converges in L²: truncate that fixed vector, then use bounded
convergence on its bounded part. Apply this statement successively
in (C.4.6.P8), using the uniform multiplier bounds and rank-one HS inequality.
It proves strong continuity of (C.4.6.P10); the finitely many fields in (C.4.6.P9)
are L²-continuous by the same argument. General varying multiplier
operators need not converge in operator norm. Nor does this argument
assert ambient Fréchet differentiability of an L² Nemytskii vector field.

###### 3. The canonical metric and the singular endpoint

Set `D(t)=R(t)*R(t)`, explicitly multiplication by `phi'(w_a)^2`
in the row blocks and identity in the other blocks. Adjunction in (C.4.6.P8)
gives the exact identities

\[
 E(t)=S(t)^*D(t),\qquad
 \Gamma(t):=E(t)S(t)=S(t)^*D(t)S(t)\succeq0.
 \tag{C.4.6.P14}
\]

Thus `Gamma` is the raw training-gradient Gram with the square roots of
the training weights in both indices. In particular, if `Ev` is the
weighted training-prediction variation, its Gauss–Newton-only equation
is `(Ev)'=-2Gamma(Ev)` at a frozen state. There is no missing mean-loss factor.

Although `D` has no positive lower operator bound, it is injective:
`phi'(w_a)>0` almost surely since the L² field `w_a` is finite almost
surely. For any `alpha in R²`,

\[
 \alpha^T\Gamma\alpha=\|RS\alpha\|_{\rm raw}^2.
\]

It vanishes if and only if `S alpha=0`. Therefore, at every time,

\[
 \ker \Gamma=\ker S=\ker E^*,\qquad
                    \operatorname{ran}E\subseteq\operatorname{ran}\Gamma.
 \tag{C.4.6.P15}
\]

The second kernel equality uses `E*=DS` and injectivity of `D`.
For the range assertion take orthogonal complements in finite-dimensional
`R²`: `ran E=(ker E*)perp` and `ran Gamma=(ker Gamma)perp`.
This is the required zero-mode compatibility. Positivity of `ES` alone
without (C.4.6.P15) would be insufficient: `ES=0` can coexist with nonzero
nilpotent `SE` for general rectangular maps.

For any fixed pair `S,E` satisfying (C.4.6.P14)–(C.4.6.P15), let `Gamma+` denote the
Moore–Penrose inverse defined by orthogonal diagonalization of the
finite symmetric matrix `Gamma`: invert its positive eigenvalues and
retain zero on its kernel. Directly,

\[
 V_\infty(\tau):=\exp(-2\tau S_\infty E_\infty)
 =I+S_\infty \Gamma_\infty^+
       [\exp(-2\tau \Gamma_\infty)-I]E_\infty,\qquad\tau\ge0.
 \tag{C.4.6.P16}
\]

For completeness, the bounded-operator exponential is its absolutely
convergent power series. For `j>=1`,
`(SE)^j=S Gamma^(j-1) E`. On `ran Gamma`,
`Gamma+ Gamma^j=Gamma^(j-1)`, and (C.4.6.P15) says `E` takes values there. Substituting
these identities in the two absolutely convergent series proves (C.4.6.P16),
also at `tau=0` and also when `Gamma=0`. In the latter case (C.4.6.P15) implies
`S=0`, so both sides are identity.

Since all eigenvalues of `Gamma` are nonnegative,
`||exp(-2tau Gamma)-I||<=1`. Consequently

\[
 \sup_{\tau\ge0}\|V_\infty(\tau)\|\le
 B_\infty:=1+\|S_\infty\|\,\|\Gamma_\infty^+\|\,\|E_\infty\|
       \le1+L_0^2\|\Gamma_\infty^+\|<\infty.
 \tag{C.4.6.P17}
\]

This is a finite precisely defined reference quantity. It is not an
evaluated numerical conditioning certificate and imposes no lower
bound on a positive eigenvalue, no full-rank assumption, and no
continuity assumption on pseudoinverses along the trajectory.

###### 4. Integrability of the actual perturbation of the endpoint

Only the finite-rank fields, rather than all multiplier operators,
need endpoint convergence in operator norm. Factor subtraction using
(C.4.6.P2)–(C.4.6.P3) gives

\[
 \|H_a^1-H_{a,\infty}^1\|_2\le d_{\rm ref},
 \quad\|Z_a^2-Z_{a,\infty}^2\|_2\le(1+M)d_{\rm ref},
\]
\[
 \|\delta_a-\delta_{a,\infty}\|_2\le a_1d_{\rm ref},
 \quad\|Q_a-Q_{a,\infty}\|_2\le a_qd_{\rm ref}.
 \tag{C.4.6.P18}
\]

For example, split the backward product with the endpoint readout
as the fixed factor; its supremum is at most ten. Split the adjoint
product with the endpoint `delta`, whose L² norm is at most `C`.
The rank difference in `G_a` is at most `(a1+C)d_ref`, so

\[
                       \|S(t)-S_\infty\|\le a_*d_{\rm ref}(t).
 \tag{C.4.6.P19}
\]

The evaluation column is `(e_a phi'(w_a)^2Q_a,
delta_a tensor H_a^1,H_a²)`. For its extra first-block difference,
use the exact pointwise bounds

\[
 |\phi'(z)^2-\phi'(\bar z)^2|\le\min(1,4|z-\bar z|).
\]

If the left side is `b`, then `|b|^4<=|b|²<=16|z-bar z|²`.
Hölder's inequality and (C.4.6.P5) thus give

\[
 \|[\phi'(w_a)^2-\phi'(w_{a,\infty})^2]Q_{a,\infty}\|_2
 \le2M_4\|w_a-w_{a,\infty}\|_2^{1/2}.
\]

Combining the finitely many weighted columns yields

\[
 \|E(t)-E_\infty\|\le a_*d_{\rm ref}(t)+2M_4d_{\rm ref}(t)^{1/2}.
 \tag{C.4.6.P20}
\]

No product of two arbitrary L² tangent fields occurs here; the only
unbounded multiplied field is the fixed endpoint `Q_a` with its
proved L⁴ bound. In particular (C.4.6.P20) does not promote L² convergence
of a general multiplication operator to operator-norm convergence.

Set

\[
 \mathcal B(t)=\mathcal L(t)+2S_\infty E_\infty.
\]

Equations (C.4.6.P13), (C.4.6.P19), (C.4.6.P20), and `||S||,||E||<=L0` give

\[
 \|\mathcal B(t)\|
 \le(4L_0a_*\sqrt{10}+2a_*)e(t)
                  +4L_0M_4\,10^{1/4}e(t)^{1/2}.
 \tag{C.4.6.P21}
\]

The norm is measurable: on separable `mathcal V`, it is the supremum of
`||B(t)v||` over a countable dense subset of the unit sphere, each
continuous in `t`. Integration of (C.4.6.P21), using (C.4.6.P2), proves

\[
 J:=\int_0^\infty\|\mathcal B(t)\|\,dt
 \le J_0:=20L_0a_*\sqrt{10}+10a_*
                         +40L_0M_4\,10^{1/4}<\infty.
 \tag{C.4.6.P22}
\]

This includes both integrability of residual curvature and integrable
operator-norm approach of the Gauss–Newton finite-rank part to its
endpoint. The active Gaussian moment enters the latter implication.

###### 5. Construction and uniform estimate for the actual propagator

There is a unique strong evolution `U(t,s)` on `mathcal V`, `0<=s<=t<infinity`,
satisfying

\[
 U(t,s)v=v+\int_s^t\mathcal L(q)U(q,s)v\,dq.
 \tag{C.4.6.P23}
\]

Here and below integrals are strong vector integrals. To construct it
on a compact interval with coefficient bound `L`, set `u0(t)=v` and
successively integrate `u_(j+1)(t)=int_s^t L(q)u_j(q)dq`.
Strong continuity, (C.4.6.P13), and induction give
`||u_j(t)||<=||v|| L^j(t-s)^j/j!`. The sum is uniformly convergent
and satisfies (C.4.6.P23) by the same summable bound. Iterating the integral
inequality for the difference of two solutions makes that difference
zero, since its bound contains `L^j(t-s)^j/j!` for every `j`.
Uniqueness gives `U(t,r)U(r,s)=U(t,s)`. This argument constructs
bounded operators, although the coefficients need not be continuous
in operator norm.

For fixed `v`, differentiating the constant-coefficient exponential
in (C.4.6.P16), or substituting (C.4.6.P23) into its convergent power series and
integrating, gives variation of constants:

\[
 U(t,s)=V_\infty(t-s)+
       \int_s^t V_\infty(t-q)\mathcal B(q)U(q,s)\,dq
 \tag{C.4.6.P24}
\]

as an identity on each vector. Taking norms and iterating the scalar
integral inequality yields

\[
 \|U(t,s)\|\le B_\infty
     \exp\!\left(B_\infty\int_s^t\|\mathcal B(q)\|\,dq\right)
 \le C_U:=B_\infty e^{B_\infty J_0}.
 \tag{C.4.6.P25}
\]

One way to verify the scalar step is to substitute the bound repeatedly;
the `j`th ordered integral of the nonnegative function `||B||`
is at most `(int ||B||)^j/j!`, giving the exponential series.
Thus

\[
                  \sup_{0\le s\le t<\infty}\|U(t,s)\|<\infty.
 \tag{C.4.6.P26}
\]

The conclusion concerns the actual trained homogeneous coefficients,
not solely a frozen endpoint system. All conditioning dependence is
exposed by `||Gamma_infty+||`. The displayed crude constants establish
finiteness; they are not useful numerical magnitudes.

For any strongly measurable forcing `F in L1_loc([0,infinity);mathcal V)`,
the unique strongly absolutely continuous solution with initial value zero,
which satisfies the equation almost everywhere, is

\[
 v(t)=\int_0^tU(t,s)F(s)\,ds,
 \qquad
 \sup_{t\le T}\|v(t)\|_{\mathcal V}
             \le C_U\int_0^T\|F(s)\|_{\mathcal V}\,ds.
 \tag{C.4.6.P27}
\]

Approximation by simple forcing functions and (C.4.6.P25) proves existence
of this integral; substitution using the integrable majorants proves
the equation, and homogeneous uniqueness proves uniqueness.
The data-forcing bound proved in C.4.6.3 is
`sup_s ||b_sigma(s)||_V<=C_b,Y ||sigma||TV`; substituting it in (C.4.6.P27)
gives (C.4.6.T12). For this continuous forcing the solution is strongly C1.

###### 6. Passive evaluation and the endpoint's fitted-prediction kernel

For any normalized `u` on the entire circle define
`H1(u)=phi(w dot u)`, `Z2(u)=A H1(u)`, `H2(u)=phi(Z2(u))`,
`delta(u)=c phi'(Z2(u))`, and `Q(u)=A*delta(u)`. Its tangent response is

\[
 \delta H^1(u)=\phi'(w\cdot u)\sum_a u_a\phi'(w_a)\xi_a,
 \quad\delta Z^2(u)=BH^1(u)+A\delta H^1(u),
\]
\[
 \ell(t,u)v=\langle d,H^2(u)\rangle_2+
               \langle\delta(u),\delta Z^2(u)\rangle_2.
 \tag{C.4.6.P28}
\]

The raw predictor gradient has block norms at most `MC,C,1`;
the first estimate is `||u phi'(w dot u)Q(u)||2<=MC`.
Combining this with (C.4.6.P7) proves, simultaneously for all circle inputs,

\[
 \|R(t)v\|_{\rm raw}\le\|v\|_{\mathcal V},\qquad
 \|\delta H^1(u)\|_2\le\|v\|_{\mathcal V},\qquad
 \|\delta Z^2(u)\|_2,\|\delta H^2(u)\|_2
                         \le(1+M)\|v\|_{\mathcal V},
\]
\[
                 \sup_{|u|=1}|\ell(t,u)v|\le L_0\|v\|_{\mathcal V}.
 \tag{C.4.6.P29}
\]

For each fixed `v`, this predictor response is continuous in `u`.
The raw fields are L²-continuous in `u` by bounded slopes; the
bounded-multiplier argument already proved after (C.4.6.P13) applies to
the fixed row tangent. Formula (C.4.6.P28) then passes continuity through
the bounded action and scalar pairing. Uniform quantitative input
derivative tails are not asserted. Combining (C.4.6.P27) and (C.4.6.P29) gives
the analogous forced whole-circle output bound.

At the fitted endpoint the frozen semigroup has limit

\[
 P_\infty=I-S_\infty \Gamma_\infty^+E_\infty,
 \quad P_\infty^2=P_\infty,
 \quad\operatorname{ran}P_\infty=\ker E_\infty,
 \quad\ker P_\infty=\operatorname{ran}S_\infty.
 \tag{C.4.6.P30}
\]

The square identity uses `Gamma+ Gamma Gamma+=Gamma+`. The range and kernel use
`GammaGamma+E=E` and `S Gamma+Gamma=S`, which follow from (C.4.6.P15).
Furthermore

\[
 D_\infty(I-P_\infty)=E_\infty^*\Gamma_\infty^+E_\infty
\]

is self-adjoint. More explicitly, put `G=R_infty S_infty`, the
weighted raw gradient synthesis. Then `G*G=Gamma_infty` and

\[
 R_\infty P_\infty v
      =(I-G\Gamma_\infty^+G^*)R_\infty v.
 \tag{C.4.6.P31}
\]

Put `Pi_grad=G Gamma_infty+ G*`. This operator is self-adjoint and
idempotent, since `Gamma_infty=G*G` and the finite pseudoinverse identity
gives `Pi_grad²=Pi_grad`. It is identity on `ran G`, by (C.4.6.P15), and zero
on its raw-Hilbert orthogonal complement. Thus `Pi_grad` is the raw
orthogonal projector onto the weighted training-gradient span, whereas
`I-Pi_grad` in (C.4.6.P31) projects onto its orthogonal complement. Thus (C.4.6.P30) separates fitted training-prediction
changes from parameter changes preserving both training predictions
to first order, using the canonical raw metric on the admissible
clock domain. An unseen evaluation `ell(infty,u)P_infty v` may
survive; its value, sign, or usefulness is not determined by (C.4.6.P30).
No assertion that the nonautonomous propagator itself converges
to `P_infty` is required here.

##### C.4.6.3. Actual finite weighted queries and admissible forcing

The field and clock notation is that of C.4.6.1. The following argument
retains the actual finite Gaussian readout throughout physical GF. It uses
one-column deletion only as a comparison, and leaves the learned cavity
flow, its residuals, and both matrix orientations intact.

###### 1. Source theorem

For every fixed finite physical `T`, put

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,
          \|c_{0,n}\|_\infty\le1,
          \|g_n\|_F/\sqrt n\le2\}.
 \tag{C.4.6.S3}
\]

Its probability tends to one. The matrix assertion follows from the
contained sphere-net Gaussian estimate in special-data III.F.2; the root
assertion is the iid second-moment law; and
`P(max_j |c0,j|>1)<=2n exp(-n²/2)`. In particular (C.4.6.S3) retains the actual
small Gaussian readout.

**Finite source theorem.** For each finite `p>=1,T<infinity`, there is a
finite deterministic `C_(p,T)` such that

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_{i=1}^n
       \sup_{t\le T,u\in S^1}|Q_{n,i}(t,u)|^p\right]
       \le C_{p,T},\qquad n\ge1.                         \tag{C.4.6.S4}
\]

The constants can be chosen with `C_(p,T)^(1/p)<=C_T sqrt(p)` for `p>=2`.
The supremum concerns query **values**; it does not assert Gaussian tails
for input derivatives. Set `N_(n,i)=sup_(t<=T,u)|Q_(n,i)(t,u)|`. Then

\[
 \sup_{t\le T}|X_{n,ia}(t)|\le3T N_{n,i},\qquad
 \sup_{t\le T}|w_{n,i}(t)|\le |g_{n,i}|+6T N_{n,i},
 \tag{C.4.6.S5}
\]

and all finite moments, averaged over coordinates and restricted to `E_n`,
of the following envelopes are bounded independently of width:

\[
 N_{n,i},\quad (1+|g_{n,i}|+N_{n,i})^k,\quad
 \{\cosh^2g_{n,ia}+6T N_{n,i}\}N_{n,i},\quad
 (|g_{n,i}|+6T N_{n,i})N_{n,i}.                    \tag{C.4.6.S6}
\]

Here `k` is any separately fixed finite positive integer. Products of a
fixed number of these envelopes have the same property. These are actual
finite-GF estimates, before any width limit.

**Population source theorem.** For the established reference of C.4.5,
there is a finite `M_*` such that

\[
 \sup_{t\ge0,u\in S^1}
 \left(\sum_{a=1}^2
     \|\cosh^2 w_a(t)Q(t,u)\|_{L^2(\Omega_1)}^2\right)^{1/2}
 \le M_* .                                                 \tag{C.4.6.S7}
\]

The proof below gives an entirely explicit, very large upper bound from
`s_dagger<=10`; alternatively (C.4.6.S7) defines the precise reference quantity
consumed by the forcing theorem. It is not a numerical evaluation of the
actual trained endpoint.

For the shared forcing (C.4.6.T5), equivalently `b_sigma=integral b d sigma`
with `b(t,u,y)=-2r(t,u,y)q(t,u)`, the source estimate is as follows.

Then `b_sigma` is continuous in physical time, is linear in `sigma`, and

\[
 \sup_{t\ge0}\|b_\sigma(t)\|_{\mathcal V}
 \le 2(Y+\sqrt{10})\sqrt{M_*^2+11}\,\|\sigma\|_{TV}.
 \tag{C.4.6.S10}
\]

Total variation denotes total mass of the variation measure, with no
factor of one half. The estimate applies in particular to `nu-nu_*`, of
mass at most two. It imposes no support size, atom weight, Gram or
orthogonality restriction on the perturbing law. The same finite forcing
has bounded normalized moments and weighted uniform integrability on
`E_n`, uniformly over `t<=T` and inputs, with constants depending on `T,Y`.

Section C.4.6.3, §8 states the precise width identification and quadrature conclusion.
The actual derivative identification using these source estimates is
proved in C.4.6.4.

###### 2. Exact physical equations and deterministic reference bounds

The mean loss is `R=(r1²+r2²)/2`. From the stored-weight mobilities the exact
finite reference equations, and their population counterparts, are

\[
 \dot w_a=-r_a\phi'(w_a)Q_a,\quad
 \dot X_a=-r_aQ_a,\quad
 \dot K=-\sum_{a=1}^2r_a\delta_a\otimes H_a^1,\quad
 \dot c=-\sum_{a=1}^2r_aH_a^2 .                    \tag{C.4.6.S11}
\]

Here `Q_a=Q(e_a)`; the two factors of the general `-2 integral` cancel the
two atom weights. Since `F'=1/phi'`, the clock identity in (C.4.6.S11) is exact.
For a general law the corresponding first clock field is
`-2 integral r u_a phi'(w.u)Q(u)/phi'(w_a)`, which gives (C.4.6.T5), with its
displayed sign and normalization. No probability-law derivative is used
to establish these identities.

On (C.4.6.S3), initially `|f_a|<=1`, hence `R(0)<=4`. The true raw energy identity
gives `R(t)<=4` and raw path displacement at most `2sqrt(T)` up to time T.
Therefore, simultaneously for all `t<=T`,

\[
 \|A(t)\|_{op}\le B:=10+2\sqrt T,\quad
 \|c(t)\|_2/\sqrt n\le C:=1+2\sqrt T,
 \quad\|w(t)\|_F/\sqrt n\le W:=2+2\sqrt T,
 \tag{C.4.6.S12}
\]

and `||K||F<=2sqrt(T)`. Moreover `sum_a|r_a|<=4`, `|r_a|<=sqrt(8)<3`.
Integration of `dot c` yields

\[
 \|c(t)\|_\infty\le H:=1+4T.                    \tag{C.4.6.S13}
\]

The raw energy identity follows directly by differentiating the finite
loss and substituting its three negative metric gradients; the three
metric terms are `||dot w||F²/n`, `||dot A||F²`, `||dot c||²/n`.
It prevents finite-time escape for the smooth finite-dimensional field.
These statements also hold for the column-deleted flow below, because it
has the same labels and readout, and its initial matrix norm is no larger.

For passive queries all these bounds are independent of u. Directly from
(C.4.6.S11),

\[
 \|\dot w\|_F/\sqrt n\le4BC,\quad
 \|\dot K\|_F\le4C,\quad \|\dot c\|_\infty\le4.
 \tag{C.4.6.S14}
\]

The chain and product rules in finite dimensions give

\[
 \|\partial_t Z^2(u)\|_2/\sqrt n\le4C(1+B^2),\qquad
 \|\partial_t\delta(u)\|_2/\sqrt n
        \le D_t:=4+8HC(1+B^2),
 \tag{C.4.6.S15}
\]

and factor subtraction gives

\[
 \|\delta(t,u)-\delta(t,v)\|_2/\sqrt n
       \le D_u|u-v|,\quad D_u:=2HBW.
 \tag{C.4.6.S16}
\]

Thus `(t,u)->delta(t,u)` is Lipschitz in normalized L², with deterministic
constants on (C.4.6.S3). Only the first-row **RMS** occurs in (C.4.6.S16). This fact,
applied to the independent cavity, is what permits a whole-circle Gaussian
query-value estimate without bounds on pointwise input derivatives.

###### 3. Delete one initialized column, retaining the entire learned flow

Fix neuron i in population 1. Let `a_i=A0 e_i`, an ordinary vector with iid
entries `N(0,1/n)`. Run the full reference GF with the initialized matrix

\[
 \widetilde A_0=A_0-a_i e_i^T
 \tag{C.4.6.S17}
\]

and the same initialized `g,c0`. Denote this flow by tildes. In particular
`tilde K` is trained; no neuron, activation, residual or learned rank is
removed. The flow is independent of the random column `a_i` conditionally
on all remaining initialized variables. Uniqueness of the finite ODE
establishes that measurability and independence.

Define the cavity-good event

\[
 E_n^i=\{\|\widetilde A_0\|_{op}\le10,
            \|c_0\|_\infty\le1,\ \|g\|_F/\sqrt n\le2\}.
 \tag{C.4.6.S18}
\]

It is measurable with respect to the remaining variables, and `E_n` is a
subset of `E_n^i`, because right multiplication by `I-e_i e_i^T` is a
contraction. Conditional Gaussian estimates are always made on (C.4.6.S18),
not by falsely conditioning on an event involving `a_i`.

Set `m_i=||a_i||2`, `epsilon_i=m_i/sqrt(n)` and

\[
 Z_i(t,u)=a_i^T\widetilde\delta(t,u),\qquad
 Z_i^\#=\sup_{t\le T,u\in S^1}|Z_i(t,u)|.
 \tag{C.4.6.S19}
\]

These are scalar probes of the cavity, not replacements for actual query
answers. Their conditional covariance is exactly
`tilde delta(t,u)^T tilde delta(s,v)/n`. Both orientations of the actual
matrix remain in the comparison that follows.

Let

\[
 x=\sum_a\|X_a-\widetilde X_a\|_2/\sqrt n,\quad
 k=\|K-\widetilde K\|_F,\quad
 z=\|c-\widetilde c\|_2/\sqrt n,\quad d=x+k+z.
 \tag{C.4.6.S20}
\]

There is no small operator-norm claim for `A0-tilde A0`. Instead its
forward action on a bounded feature has RMS at most `epsilon_i`. Its
reverse action on a cavity backward field has RMS
`|Z_i(t,e_a)|/sqrt(n)`. With `delta_cav` denoting full minus cavity, add and
subtract factors in precisely this order:

\[
 \delta_{\rm cav} Z_a^2=A\delta_{\rm cav} H_a^1
         +(K-\widetilde K)\widetilde H_a^1
         +a_i\widetilde H_{a,i}^1,
\]
\[
 \delta_{\rm cav} Q_a=A^T\delta_{\rm cav}\delta_a
          +(K-\widetilde K)^T\widetilde\delta_a
          +e_i Z_i(t,e_a).
 \tag{C.4.6.S21}
\]

The second identity deliberately uses the full A in the first term, so
that no uncontrolled column-dependent reverse error appears. On `E_n`,
the deterministic state bounds for both flows yield

\[
 \sum_a\|\delta_{\rm cav} H_a^1\|_2/\sqrt n\le x,
 \quad V:=\sum_a\|\delta_{\rm cav} Z_a^2\|_2/\sqrt n
                      \le Bx+2k+2\epsilon_i,
\]
\[
 D:=\sum_a\|\delta_{\rm cav}\delta_a\|_2/\sqrt n\le2z+2H V,
\]
\[
 P:=\sum_a\|\delta_{\rm cav} Q_a\|_2/\sqrt n
       \le BD+2Ck+\frac1{\sqrt n}\sum_a|Z_i(t,e_a)|,
\]
\[
 R_{\rm cav}:=\sum_a|r_a-\widetilde r_a|\le2z+CV.
 \tag{C.4.6.S22}
\]

For the last inequality use `f-tilde f=<delta_cav c,H2>+
<tilde c,H2-tilde H2>`. The first uses `|j_X|<=1`, with the same roots.
The velocity differences from (C.4.6.S11) satisfy

\[
 \sum_a\|\delta_{\rm cav}\dot X_a\|_2/\sqrt n\le BC R_{\rm cav}+3P,
\]
\[
 \|\delta_{\rm cav}\dot K\|_F\le C R_{\rm cav}+3(D+Cx),\qquad
 \|\delta_{\rm cav}\dot c\|_2/\sqrt n\le R_{\rm cav}+3V.
 \tag{C.4.6.S23}
\]

For example the rank difference is bounded by
`||delta_cav delta||2/sqrt(n)+C||delta_cav H1||2/sqrt(n)` before its residual
factor. These estimates include the changed residuals; the cavity has
not been driven by the full flow's residuals.

Write `D0=1+B+C+H+3`, `L=100D0^4`. Substitution of (C.4.6.S22) into (C.4.6.S23)
gives the explicit overestimate

\[
 \dot d\le Ld+\frac L{\sqrt n}
       \left(m_i+\sum_a|Z_i(t,e_a)|\right)
       \quad\hbox{for almost every }t,\qquad d(0)=0.
 \tag{C.4.6.S24}
\]

To check the constant, `V<=3D0 d+2epsilon_i`,
`D<=8D0² d+4D0 epsilon_i`,
`P<=10D0³d+4D0²epsilon_i+sum|Z_i|/sqrt(n)`,
`R_cav<=5D0²d+2D0epsilon_i`.
The three resulting d coefficients sum to at most `81D0^4`, and the
`epsilon_i` coefficients to at most `36D0³`. Norms of absolutely
continuous finite curves obey the derivative bound by the velocity norm,
which justifies (C.4.6.S24) also at zeros of a component norm. Multiplying its
integral form by the integrating factor gives

\[
 \sqrt n\sup_{t\le T}d(t)
       \le J_T(m_i+2Z_i^\#),\qquad J_T:=LT e^{LT}.
 \tag{C.4.6.S25}
\]

This is the small response to deleting one initialized column that an
operator-norm comparison alone would miss.

For an arbitrary passive input u, the first row still obeys
`||delta_cav(w.u)||2/sqrt(n)<=x`, so the same forward subtraction gives

\[
 \|\delta(t,u)-\widetilde\delta(t,u)\|_2/\sqrt n
            \le4D0^2(d(t)+\epsilon_i).
 \tag{C.4.6.S26}
\]

The learned transpose contribution has an exact, coordinatewise bound:

\[
 (K(t)^T\delta(t,u))_i
   =-\int_0^t\sum_a r_a(v)H_{a,i}^1(v)
       \frac{\delta_a(v)^T\delta(t,u)}n\,dv,
 \qquad |(K(t)^T\delta(t,u))_i|\le4TC^2.
 \tag{C.4.6.S27}
\]

Using `Q_i=a_i^T delta+(K^T delta)_i`, (C.4.6.S25)–(C.4.6.S27), and `m_i<=10` on
`E_n`, gives

\[
 N_{n,i}\le A_T Z_i^\#+B_T\quad\hbox{on }E_n,
\]
\[
 A_T=1+80D0^2J_T,\qquad
 B_T=400D0^2(J_T+1)+4TC^2.
 \tag{C.4.6.S28}
\]

No independence of the actual `delta` and `a_i` has been assumed. Their
dependence is exactly the error controlled in (C.4.6.S26).

###### 4. A contained Gaussian maximum bound

Here are all probability ingredients beyond the initialized operator
bound. If `G_1,...,G_N` are centered jointly Gaussian scalars with
variances at most `v²`, no independence among them is required for

\[
 \Pr\{\max_j|G_j|>r\}\le2N e^{-r^2/(2v^2)}.
 \tag{C.4.6.S29}
\]

This follows by applying the scalar Gaussian exponential moment and
Markov's inequality to each tail and taking a union bound. Consequently,
for `p>=2`,

\[
 \|\max_j|G_j|\|_{L^p}
       \le v\{\sqrt{2\log(2N)}+2\sqrt p\}.
 \tag{C.4.6.S30}
\]

For detail, put `a=v sqrt(2log(2N))` and `V=(max|G_j|-a)_+`.
Equation (C.4.6.S29) implies `P(V>r)<=exp(-r²/(2v²))`.
For `m=ceil(p/2)`, integrating this tail against `2m r^(2m-1)` gives
`E V^(2m)<=(2v²)^m m!`; the integral follows by substituting
`q=r²/(2v²)` and integrating by parts m times. Since `m!<=m^m`,
monotonicity of probability-space Lp norms gives
`||V||p<=||V||_(2m)<=v sqrt(2m)<=v sqrt(2p)`, because
`2m<=p+2<=2p` for `p>=2`. Minkowski gives (C.4.6.S30), with slack in the
constant 2. The case `v=0` is zero.

Suppose a continuous centered Gaussian process `Z(q)`, `q in [0,1]^2`,
has variance at most `C²` and
`||Z(q)-Z(q')||L² <= L0 ||q-q'||_1`. Use square grids of spacing `2^-k`
and round each grid point down to its parent on the preceding grid.
There are at most `4^(k+1)` grid points at level k. Parent increments
have standard deviation at most `2L0 2^-k`. Formula (C.4.6.S30), followed by
Minkowski, bounds the sum over k of their maxima in Lp by

\[
 2L0\sum_{k\ge1}2^{-k}
  \{\sqrt{2\log(2\cdot4^{k+1})}+2\sqrt p\}
       \le60L0\sqrt p.
 \tag{C.4.6.S31}
\]

The inequality follows for instance from `sqrt(k+2)<=k+2` and
`sum_(k>=1) k2^-k=2`, `sum_(k>=1)2^-k=1`. The four level-zero corner
values cost at most `4C sqrt(p)` by (C.4.6.S30). The telescoping sums and
continuity at each q therefore give

\[
 \|\sup_q|Z(q)|\|_{L^p}
                \le64(C+L0)\sqrt p.                    \tag{C.4.6.S32}
\]

This proof works conditionally on arbitrary fixed coefficients. Here,
conditional on all variables except column `a_i`, the process (C.4.6.S19) is
a finite linear combination of independent Gaussians, with continuous
coefficients. On `E_n^i`, (C.4.6.S12), (C.4.6.S15)–(C.4.6.S16) apply to the cavity. Parameterize
`t=T q1`, `u=(cos(2pi q2),sin(2pi q2))`. Thus (C.4.6.S32) gives

\[
 \left(\mathbb E_{a_i}[(Z_i^\#)^p]\right)^{1/p}
       \le C_Z\sqrt p,\qquad
 C_Z:=64\{C+T D_t+2\pi D_u\},\quad\hbox{on }E_n^i.
 \tag{C.4.6.S33}
\]

Since `E_n subset E_n^i`, (C.4.6.S28), conditioning, and then (C.4.6.S33) prove

\[
 \left(\mathbb E[\mathbf1_{E_n}N_{n,i}^p]\right)^{1/p}
     \le (B_T+A_T C_Z)\sqrt p=:C_T\sqrt p.
 \tag{C.4.6.S34}
\]

This bound is the same for every i and n; averaging proves (C.4.6.S4). It has
not inferred empirical moments from RMS convergence or exchangeability.
It used the reached continuous reference flow and its quantitative
column-deletion sensitivity. The selected-column concentrating examples
in special-data J.1 and the three-query obstruction in Gaussian calculus
therefore do not contradict it: those arbitrary adapted queries do not
satisfy (C.4.6.S24) with the present constants.

###### 5. Clock weights, products and actual finite uniform integrability

For each fixed g,

\[
 \partial_X\cosh^2 j(X,g)=2\tanh j(X,g),
 \qquad \cosh^2 j(X,g)\le\cosh^2g+2|X|.
 \tag{C.4.6.S35}
\]

The derivative identity follows from `j_X=sech² j`; its absolute value is
at most two, and integration gives the inequality for either sign of X.
This exact estimate avoids an unnecessary exponential in `|X|`. Integrating
`dot X_a=-r_a Q_a` with `|r_a|<=3` proves (C.4.6.S5). The factor 6 in its row
bound is an upper bound for `3sqrt(2)`.

Every Gaussian root has every polynomial and linear-exponential moment.
In particular
`E exp(q|G|)<=E exp(qG)+E exp(-qG)=2exp(q²/2)`.
For any fixed p, the moment of `cosh²g_a N_i` on `E_n` is bounded by
Hölder using the `2p` moments of both factors. No independence between
the evolved query and g is required. The same reasoning applies to all
products in (C.4.6.S6). For example, with

\[
 P_{n,i,a}:=(\cosh^2g_{n,ia}+6T N_{n,i})N_{n,i},
 \tag{C.4.6.S36}
\]

one obtains

\[
 \sup_n\mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
                          P_{n,i,a}^{p}\right]<\infty.
 \tag{C.4.6.S37}
\]

For the finite source coordinate in (C.4.6.T5), `|r(t,u,y)|<=C+Y` and
`|u_a|,phi'(w.u)<=1`, so its supremum over `t,u,|y|<=Y` is bounded by
`2(C+Y)P_(n,i,a)`. Given any `p>2`,

\[
 \mathbb E\left[\mathbf1_{E_n}\frac1n\sum_i
     P_{n,i,a}^{2}\mathbf1_{P_{n,i,a}>R}\right]
       \le C_{p,T}R^{-(p-2)}.                         \tag{C.4.6.S38}
\]

Markov's inequality shows that these empirical square tails tend to zero
in probability, uniformly in width on `E_n`, as R tends to infinity.
Outside `E_n` the probability tends to zero as n grows. Thus the ordered
statement needed for width passage is

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\left\{\sup_{t,u,|y|\le Y}
       \frac1n\sum_i |b_{X,a,n,i}(t,u,y)|^2
                     \mathbf1_{|b_{X,a,n,i}|>R}>\varepsilon\right\}=0.
 \tag{C.4.6.S39}
\]

One can put the supremum inside the coordinate envelope as in (C.4.6.S38), so
the stated form follows. The same argument proves weighted tails involving
`|w|Q` or any separately fixed polynomial of the displayed envelopes.
These estimates make no assertion that a bounded initialized Gaussian
action maps every Lp input boundedly into Lp.

###### 6. Uniform population bounds from the bounded feature segment

The established physical reference equals the autonomous feature flow

\[
 X_{a,s}=\tfrac12y_a Q_a,\quad
 K_s=\tfrac12\sum_a y_a\delta_a\otimes H_a^1,\quad
 c_s=\tfrac12\sum_a y_aH_a^2,
 \tag{C.4.6.S40}
\]

restricted to `0<=s<s_dagger`, where `s_dagger<=10`, with
`ds/dt=2(1-b)>0`. This is C.4.5.1's actual reference and endpoint, not a
new prescription for physical finite GF. To bound the population sources
uniformly in physical time, apply the preceding cavity argument to the
**auxiliary finite feature equation** (C.4.6.S40) on `0<=s<=S=10`, initialized
with `c0=0`. Only this auxiliary equation has zero finite readout.

Its elementary deterministic bounds, on
`{||A0||op<=10, ||g||F/sqrt(n)<=2}`, are

\[
 \|c(s)\|_\infty\le S,\quad \|K(s)\|_F\le S^2/2,\quad
 B=10+S^2/2,\quad C=H=S+1,
\]
\[
 \|w(s)\|_F/\sqrt n\le
 W:=2+10S^2/2+S^4/8.                               \tag{C.4.6.S41}
\]

Indeed `sum_a |y_a/2|=1`, so `||c_s||infty<=1`,
`||K_s||F<=s`, and
`sum_a ||X_(a,s)||2/sqrt(n)<= (10+s²/2)s`. Integration and
`|j(X,g)-g|<=|X|` give (C.4.6.S41). These bounds prove existence on the entire
finite feature interval as in B.1's transformed integral construction.

The proof of (C.4.6.S21)–(C.4.6.S28) now uses the same fixed controls in both flows;
all residual-difference terms vanish. The retained upper bound `L=100D0^4`
remains valid. The velocity bounds (C.4.6.S14)–(C.4.6.S16) remain upper bounds, since
the absolute sum of feature controls is at most one rather than four.
Consequently the formulas (C.4.6.S28), (C.4.6.S33), (C.4.6.S34), with `T` replaced by S and
the constants (C.4.6.S41), give a number `C_*<infinity` such that

\[
 \mathbb E\left[\mathbf1_{E_n^{feat}}\frac1n\sum_i
      \sup_{s\le S,u}|Q^{feat}_{n,i}(s,u)|^p\right]
         \le(C_*\sqrt p)^p,\qquad p\ge2.             \tag{C.4.6.S42}
\]

Every quantity in this crude bound is explicitly given above. No numerical
flow solution is hidden in `C_*`, and no fitting property of the finite
feature flow is assumed.

We detail how this reaches the *canonical* population flow. On each fixed
transformed Euler mesh, append finitely many passive forward and reverse
queries to the oracle program in B.1. The first-row transform is continuous
with at most linear growth in `(X,g)`, hence global-nonlinear A.1 applies.
Readout products can be clipped outside a fixed open neighborhood of the
bound in (C.4.6.S41), so they meet the fixed-program hypotheses. Both matrix
orientations belong to the same III.F construction. Same-root transformed
stability controls the finite-feature-flow/mesh error uniformly in width.
The corresponding population error tends to zero in clock L², increment
HS and readout L²; the HS assertion is proved in C.4.5.2, §1. Passive Q
errors follow by factor subtraction with bounded readout. Width first at
fixed mesh, then mesh removal, therefore gives the joint empirical W2
limits for every finite list of `(g,X,w,Q(s,u))`.

For a finite list of rational parameter pairs `(s_j,u_j)`, apply this
convergence to the bounded continuous test
`min(R,max_j |Q(s_j,u_j)|^p)`. Its empirical average converges in
probability to the deterministic population expectation; since the test
is bounded, the expectations converge as well. Multiplication by
`1_(E_n^feat)` changes the expectation by at most
`R P((E_n^feat)^c)`, which vanishes. Equation (C.4.6.S42) and monotone convergence,
first in R and then in the finite rational lists, give a population
envelope

\[
 N^\#:=\sup_{(s,u)\in\mathcal D}|Q(s,u)|,
 \qquad\|N^\#\|_{L^p}\le C_*\sqrt p,             \tag{C.4.6.S43}
\]

where `mathcal D` is any fixed countable dense parameter set including
the active directions. This envelope is a statement about simultaneous
representatives on that countable set. For any other fixed deterministic
`(s,u)`, L² continuity of Q supplies an almost surely convergent subsequence
from the dense set; thus `|Q(s,u)|<=N#` in its L² equivalence class.
Fubini gives the bound almost everywhere for any fixed deterministic
observation measure. No assertion of pointwise continuous sample paths
for the population Q, or of Gaussian input-derivative tails, is needed.
The map into L² is jointly continuous and is the canonical action map.

Integration of (C.4.6.S40), followed by Fubini, gives almost surely
`sup_s |X_a(s)|<=S N#/2`, for the absolutely continuous active clocks.
Thus (C.4.6.S35) gives, in every deterministic passive-input equivalence class,

\[
 |\cosh^2w_a(s)Q(s,u)|
          \le(\cosh^2g_a+S N^\#)N^\#.
 \tag{C.4.6.S44}
\]

Hölder, `||N#||4<=2C_*`, and
`||cosh²G||4<=(2e^32)^(1/4)=2^(1/4)e^8` imply the explicit bound

\[
 M_*\le\sqrt2\{2^{5/4}e^8 C_*+4S C_*^2\},\qquad S=10.
 \tag{C.4.6.S45}
\]

The physical path stays in this feature segment, so (C.4.6.S7) holds for all
physical times. The reference quantity M_w in (C.4.6.T8) satisfies
`M_w<=M_*`; using the input weights `sum_a u_a²=1` gives the sharper
forcing constant in (C.4.6.T9). This reasoning establishes a uniform population source
bound, separately from the fixed-physical-horizon finite estimate (C.4.6.S4).
It does not claim uniform-in-time finite-width convergence.

###### 7. Continuity, admissibility and norms of data forcing

The integrand (C.4.6.T5) has all its components in (C.4.6.T2). For the first component,
`phi'(w_a)^(-1)=cosh²w_a` and (C.4.6.S7) apply. For the others,
`||delta tensor H1||HS<=||c||2`, `||H2||2<=1`.
The established feature endpoint bound gives `||c||2<=sqrt(10)` and
`|f(u)|<=sqrt(10)`, hence `|r(u,y)|<=Y+sqrt(10)`. Squaring the three
component bounds gives (C.4.6.S10).

For completeness the integrand is continuous into (C.4.6.T2) jointly in feature
time, input and label. The bounded reference state and its strong velocity
give deterministic L² Lipschitz bounds for `Q(s,u)` by differentiating
`Q=A*delta` in time and using (C.4.6.S16) in input. Their population derivation
uses III.F.9's strong curve chain rule, not ambient Fréchet differentiability.
The envelope (C.4.6.S43) controls all their higher moments. The elementary
interpolation inequality

\[
 \|V\|_4\le\|V\|_2^{1/3}\|V\|_8^{2/3}
 \tag{C.4.6.S46}
\]

follows by Hölder with `1/4=(1/3)/2+(2/3)/8`. Therefore, for any fixed
weight `W0 in L4`,

\[
 \|W0\{Q(s,u)-Q(s',v)\}\|_2
 \le\|W0\|_4\|Q(s,u)-Q(s',v)\|_2^{1/3}
                         (2\|N^\#\|_8)^{2/3}.
 \tag{C.4.6.S47}
\]

For the changing weight use the exact derivative in (C.4.6.S35):
`|cosh²w_a(s)-cosh²w_a(s')|<=2|X_a(s)-X_a(s')|<=N#|s-s'|`.
Also
`|phi'(w(s).u)-phi'(w(s').v)|`
is bounded by a constant times
`N#|s-s'|+(|g|+S N#)|u-v|`.
Every resulting product with Q and the clock weight is integrable in L²
by (C.4.6.S43), Gaussian root moments, and Hölder. Changing the factors of
`r u_a cosh²w_a phi'(w.u)Q` one at a time, (C.4.6.S47) treats the Q difference
and these bounds treat the remaining factors. This proves continuity,
and in fact a deterministic `1/3` Hölder upper bound in `(s,u,y)` on the
compact feature/data parameter set. Middle and readout factors are simpler
Lipschitz differences in L²/HS.

The range of a continuous map from that compact parameter set into the
Hilbert space (C.4.6.T2) is compact and separable. Finite signed Borel measures
therefore admit its Bochner integral, with norm bounded by the integral
of the norm against the variation measure. This proves existence,
linearity, and (C.4.6.S10). Time continuity of the integral follows from uniform
continuity of its compact-domain integrand. Composing with the physical
clock gives continuity for all finite physical intervals, and the same
estimate holds at the fitted endpoint. This construction does not assume
that every signed zero-mass measure is a two-sided probability-law tangent:
it defines a linear forcing operator after the finite right derivatives
have supplied (C.4.6.T5).

The same reasoning at actual finite width uses (C.4.6.S4)–(C.4.6.S6) and the
deterministic normalized L² Lipschitz bound on `Q(t,u)` from (C.4.6.S14)–(C.4.6.S16).
For example its time constant is at most `4C²+B D_t`, and its input
constant at most `B D_u`. On `E_n` there is a random `Z_n` with bounded
fixed moments, uniformly in n, such that

\[
 \|b_n(t,u,y)-b_n(t',v,y')\|_{\mathcal V_n}
 \le Z_n\{|t-t'|+|u-v|+|y-y'|\}^{1/3}.
 \tag{C.4.6.S48}
\]

Here the finite clock-state norm is
`(||xi||F²/n+||B||F²+||d||2²/n)^(1/2)`. To see that `Z_n` has the claimed
moments, use (C.4.6.S47) with normalized empirical norms and the finite envelope
`N_(n,i)`, and bound the remaining factor differences by (C.4.6.S5), (C.4.6.S35).
Every empirical envelope norm involved has bounded moments by (C.4.6.S6),
Jensen, and Hölder. No pointwise-in-input derivative moments are required.
The label term is actually Lipschitz; it is weakened to the displayed
exponent only to use one modulus on the compact set. If its diameter is
larger than one, enlarge `Z_n` by that fixed diameter to cover all pairs.

###### 8. Exact identification and arbitrary Borel laws

We specify what convergence this source proof supplies, rather than
inventing an operator-norm distance between different width carriers.

1. For each finite deterministic list of physical times and passive inputs,
   the actual finite reference tuples consisting of the full Gaussian
   roots, clocks, raw first fields, hidden values, c and passive Q have
   their joint within-population W2 limits, identified by B.1 and the
   complete III.F/A.1 fixed-mesh construction. The append-only passive
   reverse call is legitimate for exactly the same reason as C.4.5.2, §5 active finite-GF call: bounded readout makes `c phi'(Z2(u))` a bounded-derivative
   instruction after an inactive fixed readout clip; its response uses
   the same initialized action and transpose. The passive first argument
   `w.u` retains both root coordinates. Actual finite readout is handled
   by the same-root finite-flow/mesh comparison; its supremum vanishes in
   probability as in B.1, rather than by resetting the finite flow.

2. Any finite tuple of the source first components (C.4.6.T5), roots, clocks,
   and query values has joint empirical Wp convergence in probability
   for every separately fixed finite p. First clip the additional
   coordinate functions at a fixed level. The tuple is a bounded
   continuous function of the identified node tuple, so its law converges.
   For any moment exponent p, (C.4.6.S6) with a larger exponent controls the
   unbounded tails by (C.4.6.S38). The same moment bound passes to the limiting
   tuple by bounded tests and monotone convergence. Removing the clipping
   identifies moments as well as weak laws. The elementary finite-cell
   coupling proof in III.F.1 extends verbatim from squared distance to
   p-th distance using `|a-b|^p<=2^(p-1)(|a|^p+|b|^p)`; hence these two
   conclusions give Wp convergence. Roots use their Gaussian moments,
   and clocks use (C.4.6.S5). A claim of all moments for arbitrary unrelated
   Gaussian programs is neither assumed nor concluded.

3. In particular, the W2 source-tuple comparisons extend uniformly over
   compact physical time/input/label parameter sets for each fixed tuple
   arity. Use (C.4.6.S48) and pair equal finite neuron indices to bound empirical
   W2 changes between nearby parameters. Its random modulus is tight by
   the just-proved moment estimates. The limiting modulus follows from
   Section C.4.6.3, §7 (or the same compact-time physical proof). At a fixed finite
   parameter net every required convergence holds simultaneously by a
   finite union bound. Refine the net after taking width to infinity.
   This proves the asserted uniformity for observable laws, without
   coupling individual finite neurons to invented population neurons.

4. For any fixed Borel probability law nu, choose a deterministic finite
   partition of the compact data space with cells of diameter at most h
   and choose one representative per nonempty cell. Let `pi_h nu` put
   its exact cell mass at that representative. This does not impose a
   lower bound on nonzero masses. Minkowski and (C.4.6.S48) give, uniformly for
   `t<=T`,

   \[
   \|b_{\nu,n}(t)-b_{\pi_h\nu,n}(t)\|_{\mathcal V_n}
          \le Z_n h^{1/3}\quad\hbox{on }E_n.
   \tag{C.4.6.S49}
   \]

   The analogous population bound holds with a deterministic constant.
   For a finite signed measure replace one by its total variation mass
   and partition its positive and negative parts, or retain the fixed
   two reference atoms exactly when forming `nu-nu_*`. At fixed h the
   first forcing field is a finite linear combination of the identified
   source nodes. Middle forcing is a finite sum of ranks; its HS norm
   and its differences are determined by the finite pairwise Gram
   contractions of its factors. All these contractions converge by the
   same-layer tuple statement. Thus fixed-law forcing and any fixed
   finite action/probe extension are obtained in the order: fixed
   quadrature and bounded source clips, width limit, source-clip removal,
   and quadrature refinement. Width-independent tails also allow clips
   and quadrature to be chosen in either prescribed nested order.

For action/probe extensions, a clipped source is first approximated by a
bounded smooth coordinate function on a fixed box of its finite input
tuple. The proof of A.1 permits this fixed approximation. Its normalized
L² error is controlled by (C.4.6.S39) and the corresponding population tail.
The initialized operator norm bound then controls the error after either
matrix orientation; learned ranks use their HS bound. A finite sequence
of such extensions is justified by induction, choosing each fixed smooth
approximation before the width limit. This is the action identification
needed when the linear tangent equation acts on the forcing.

Statements 1–4 provide constants independent of atom count and weights and
convergence for every fixed deterministic nu. They assert no failure
probability supremum over all nu, no convergence rate in width, no
uniform-in-physical-time finite-width approximation, and no convergence
of nonlinear perturbed flows. For nonatomic laws the finite loss and its
forcing are exactly integrated functions; the quadrature above is only a
proof approximation, not an empirical training algorithm.

##### C.4.6.4. Actual finite-GF derivatives and passive predictions

###### 1. Identification framework

We now prove the derivative and width assertion (C.4.6.T10), using the
shared equation (C.4.6.T6), the strong generator of C.4.6.2 and the actual
finite source estimates of C.4.6.3. The finite coefficients have no assumed
sample-exchange symmetry. All comparisons below use same-width arrays.

###### 2. Finite differentiation precedes every width limit

For fixed `n`, the loss integrated against any such Borel probability law
is a smooth finite-dimensional function of its three parameter arrays.
Indeed on a compact parameter set every derivative of the integrand is
continuous and bounded uniformly in `(u,y)`; differentiation of its integral
is justified by the bound on the difference quotient from the scalar mean
value formula. The vector field depends affinely on `epsilon`.

The finite raw energy identity, with squared increment norm
`||dw||F^2/n+||dA||F^2+||dc||2^2/n`, bounds the parameter displacement on
`[0,T]` by `sqrt(T L_n(0))`. Initial losses are uniformly bounded for
`epsilon in [0,1]`, at this fixed initialized network. The resulting compact
finite-dimensional parameter ball excludes finite-time escape. Local smooth
ODE construction and continuation therefore give all these finite flows.
For a nonatomic law this is GF of the exactly integrated loss, not an
empirical training algorithm.

Here is the parameter differentiation argument without invoking a
population law-to-flow map. Subtract the two finite integral equations.
On the preceding compact ball the derivative of the vector field is
bounded, so the scalar integral inequality gives
`sup_t||theta_epsilon-theta_0||<=C_n,T epsilon`.
Divide the subtracted equation by `epsilon`. The exact mean value formula
expresses its first term using the derivative of the reference vector
field on the line between these two paths; those coefficients converge
uniformly in time to their values at `theta_0`. The direct change of the
law is its signed integral against `sigma`. Subtract the claimed limiting
linear integral equation and use the same integral inequality. This proves
uniform-in-time convergence of the difference quotients, hence the right
derivative. All these arguments are at fixed width; their constants may
depend on `n` and are not used in the width passage.

For every finite coordinate `phi'(w_a)>0`, so differentiate the exact
coordinate change (C.4.6.T0). It gives

\[
 \delta w_a=D_a\xi_a.
 \tag{C.4.6.F11}
\]

For an arbitrary law the transformed first velocity is exactly
`-2 integral r u_a phi'(w.u)Q(u)/phi'(w_a) dmu`. At `nu_*` the only
nonzero contribution to row `a` has `u=e_a`; the two gates cancel
identically, before differentiating. Its homogeneous differential is
therefore `-2p_a[ell(t,e_a)[v] Q_a+r_a dot Q_v(e_a)]`. The direct law derivative
is precisely the first block of (C.4.6.T5). The middle and readout equations
differentiate to the other blocks of (C.4.6.P11)-(C.4.6.T5). This verifies every sign,
training weight and factor 2 in (C.4.6.T6). At time zero all array derivatives
vanish, since initialization is identical for all `epsilon`.

The finite output derivative is the scalar pairing (C.4.6.T14), with normalized
finite pairings. Thus (C.4.6.T6) at finite width is the actual derivative already
constructed, by uniqueness of its finite linear equation. The finite
Gaussian readout is present in every coefficient and forcing field.

After this construction, (C.4.6.T5)-(C.4.6.T6) define a linear extension to all finite
signed zero-mass directions. The extension agrees with the finite right
derivative for each probability-law path above. No assertion that arbitrary
signed directions admit a two-sided probability neighborhood is used.

###### 3. Exact probability input and removal of data quadrature

We use the actual-reference source theorem of C.4.6.3 on the event

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,
        \|c_{0,n}\|_\infty\le1,\|g_n\|_F/\sqrt n\le2\}.
 \tag{C.4.6.F12}
\]

It has probability tending to one. On it the actual reference, its clock
state and its velocities have deterministic compact-time RMS/action bounds,
and `||c_n(t)||infinity<=C_T`. If

\[
 Q^\#_{n,i}=\sup_{t\le T,u\in S^1}|Q_{n,i}(t,u)|,
 \quad X^\#_{n,ia}=\sup_{t\le T}|X_{n,ia}(t)|,
 \quad W^\#_{n,ia}=\cosh^2g_{n,ia}+2X^\#_{n,ia},
\]

then for every finite `p>=2` the source theorem gives finite constants
independent of width such that

\[
 E\left[1_{E_n}{1\over n}\sum_i
 \left\{(Q^\#_{n,i})^p+
       \sum_a(W^\#_{n,ia}Q^\#_{n,i})^p+
       (\sup_{t\le T}|w_{n,i}(t)|Q^\#_{n,i})^p\right\}\right]
 \le C_{p,T}.
 \tag{C.4.6.F13}
\]

The exact envelope `cosh^2 w_a(t)<=W^#_a` is part of that argument.
The analogous population bounds, on the canonical reference, are also
proved there. Only fixed finite moments and their uniform integrability
are used below. No Gaussian tail bound for input derivatives is asserted.

To check the measure approximation explicitly, let `chi_R(q)` be clipping
to `[-R,R]`, and let `rho_R(w)=min(cosh^2 w,R)`. In the first component
of (C.4.6.T5), replace `cosh^2 w_a Q(u)` by `rho_R(w_a)chi_R(Q(u))`; leave the
other two components unchanged. Call the resulting integrand `q_R` and
forcing `b_sigma,R`. On the compact-time state bounds, `q_R` times the
residual is globally Lipschitz in the data variable with a constant
`C_T,Y,R`, and is Lipschitz in the same-root clock/HS/readout distance.
For completeness, `rho_R` is bounded by `R` and Lipschitz with constant
at most `2R`; `chi_R` is bounded by `R` and 1-Lipschitz. Forward
differences obey

\[
 \|Z^1(u)-Z^1(v)\|_2\le\|w\|_2|u-v|,\qquad
 \|Z^2(u)-Z^2(v)\|_2\le\|A\|_{op}\|w\|_2|u-v|,
\]

and reverse differences obey the same type of bound because `c` is
bounded pointwise. Adding and subtracting the bounded factors in `q_R`
proves the asserted Lipschitz bounds. The middle rank difference has
the identical estimate in HS norm.

The clipping error tends to zero uniformly in `t,u` in probability at
finite width, in the following ordered sense:

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\{1_{E_n}\sup_{t\le T,u}\|q_n(t,u)-q_{n,R}(t,u)\|_{
                    \mathcal V_n}>a\}=0\quad(a>0).
 \tag{C.4.6.F14}
\]

Indeed the first-block difference is bounded pointwise by
`2 W^#_a Q^# [1_{W^#_a>R}+1_{Q^#>R}]`. Its empirical squared norm has
expectation tending to zero by (C.4.6.F13) and Holder, or by the higher-moment
tail bound `|V|^2 1_{|V|>M}<=|V|^p/M^(p-2)` after splitting the two
factors. The individual moments of `W^#` follow from its envelope and
the `X^#` moment statement in the source theorem. Sum over the two
coordinates and apply Markov. The population version is identical.
Consequently this clipping error also bounds the forcing error by
`2(C_T+Y)||sigma||TV` times its supremum.

Partition the compact data space into finitely many Borel cells of diameter
at most `delta`, and transfer `nu`'s mass in each cell to one point of that
cell. The resulting deterministic finite law `nu^delta` satisfies
`W1(nu,nu^delta)<=delta` and has the same mass. Coupling within the cells
and using the preceding Lipschitz estimate gives

\[
 \sup_{t\le T}\|b_{\nu-\nu_*,R}(t)
               -b_{\nu^\delta-\nu_*,R}(t)\|\le C_{T,Y,R}\delta.
 \tag{C.4.6.F15}
\]

The same bound holds on `E_n`. First choose `R` for (C.4.6.F14), then choose
`delta` for (C.4.6.F15). This proves the required forcing approximation by a
fixed finite list of bounded coordinate instructions and passive queries.
It does not assert total-variation convergence of the quadrature laws.
Constants do not involve the number or weights of the quadrature atoms.

These arguments also prove strong continuity and Bochner measurability
of the uncut forcing: the clipped integrands are continuous on the compact
time/data space into `mathcal V`, and converge uniformly there by the
population version of (C.4.6.F14). Their range is separable, and the uniform norm
bound makes integration against every finite signed measure legitimate.

###### 4. Strong multiplier consistency and fixed-program identification

The only finite-program result used is special-data III.F.1-7, with the
contained value extension global-nonlinear A.1. A fixed finite list of
continuous coordinate instructions of at most linear growth, applications
of the same initial action and its transpose, and causal scalar contractions
has joint empirical same-layer `W2` convergence in probability. The metric
for a finite node tuple is its ordinary Euclidean metric. Singular query
Grams are admitted by III.F.5, whose proof adds fresh query noise at a
fixed program, takes the width limit, and then removes that noise. This
does not require a Gram inverse limit. The source-response extension A.2
is needed in the separate source proof, not as an extra assertion that
finite differentiated trajectories already converge.

We record the product principle used twice below. If arrays `z_n,z_n^h`
on the same indices differ by at most `a_h+o_P(1)` in RMS, `a_h->0`,
and `V_n^h` is a fixed-program node with a second-moment limit, then for
bounded Lipschitz `b`, at fixed cutoff `M`,

\[
 {\|[b(z_n)-b(z_n^h)]V_n^h\|_2\over\sqrt n}
 \le \operatorname{Lip}(b)M
          {\|z_n-z_n^h\|_2\over\sqrt n}
       +2\|b\|_\infty
          {\|V_n^h1_{|V_n^h|>M}\|_2\over\sqrt n}.
 \tag{C.4.6.F16}
\]

For a vector-valued bounded multiplier the identical argument applies.
Continuous positive-part cutoffs transfer the tail in (C.4.6.F16) through the
fixed-program W2 limit. For a compact family in population L2, these
tail norms tend to zero uniformly: approximate the compact family by a
finite L2 net and use
`||V1_{|V|>2M}||2<=2||V-W||2+2||W1_{|W|>M}||2`.
For a merely bounded continuous scalar multiplier, first restrict its
arguments to a compact interval; the same argument uses uniform continuity
there. All multipliers below can instead be taken globally Lipschitz.

Let `theta_n^h` be transformed Euler for the reference on a fixed mesh
of maximum step `h`. It starts from the actual finite readout.
The complete B.1 same-root proof applies with `kappa_a=1/2`, and with
HS distance replacing action distance: a rank difference obeys the same
inequality in HS, while the action of a HS difference is bounded by its
HS norm. It gives, on `E_n`, for sufficiently small `h`,

\[
 \sup_{t\le T}\|\theta_n(t)-\theta_n^h(t)\|_{\rm clock,HS,L2}
        \le C_T h.                                             \tag{C.4.6.F17}
\]

Here and below reference-state distance includes its two clocks and the
learned matrix increment. Its readout supremum is bounded separately.
The population reference has the identical Euler estimate. In particular
the full first row is recovered, not only a projection on a new input.

At fixed `R,delta,h`, build tangent Euler along these reference mesh
states, using (C.4.6.P11) and the clipped forcing for `nu^delta-nu_*` at the
preceding node. Expand each learned reference or tangent matrix as its
finite sum of rank-one updates. Every new matrix query then uses the
initialized matrix in its actual orientation plus finitely many scalar
contractions. Every coordinate instruction is continuous with at most
linear growth. For example `phi'(j(X,g))^2 xi` has a bounded multiplying
factor, while `c phi''(Z2) dot z2` has bounded `c` after clipping outside
the already proved readout bound. The clipping of `c` changes no values.
Each `rho_R(w)chi_R(Q)` is bounded. There is no uncut product of two
independent unbounded varying tangent arguments.

The fixed-program theorem therefore identifies the joint deterministic
population mesh law and all its quadratic contractions. Causal empirical
feedback is recovered instruction by instruction. At a scalar step use
`|<u,v>-<u_o,v_o>|<=||u-u_o||||v||+||u_o||||v-v_o||`. At a matrix step
the discrepancy of a recomputed finite rank action and its prescribed
node is a finite sum of scalar contraction discrepancies times nodes of
bounded RMS. At a coordinate product use (C.4.6.F16), taking width to infinity
first and then removing its auxiliary cutoff. Oracle tails are available
from joint W2 convergence of the fixed preceding tuple. Thus actual
empirical coefficients and recomputed nodes have the same limit even
though the coordinate map need not be globally Lipschitz.

The finite initial readout is not discarded in this assertion. One may
construct the deterministic-coefficient oracle with zero limiting readout
and couple the actual fixed recursion to it. The initial readout discrepancy
is its actual RMS, tending to zero, and its coordinate supremum also tends
to zero by the Gaussian union bound. Finite induction with (C.4.6.F16) propagates
that error through every node. This is a comparison at fixed mesh, not a
change to either actual GF or its derivative.

###### 5. Removing the time mesh without operator-norm multiplier convergence

Fix `R,delta` temporarily. Denote the population tangent mesh by `v^h`
and the forced solution with this clipped finite-law forcing by `v`.
Their generators have a common operator bound `C_T` by (C.4.6.P13). For each
fixed tangent vector `V`,

\[
 \sup_{t\le T}\|[\mathcal L(\theta^h(\pi_h t))-\mathcal L(\theta(t))]V\|
             \longrightarrow0.                                \tag{C.4.6.F18}
\]

Indeed reference clock, HS increment and readout convergence first gives
the forward field and action differences. Every remaining difference
in (C.4.6.T14) and (C.4.6.P11) is a bounded multiplier acting on one fixed L2 field, a
bounded action, a rank pairing, or a bounded finite-rank field. Equation
(C.4.6.F16)'s population proof handles every multiplier. For the evaluation
field use `D_a^2 Q_a`; its change is handled by truncating the fixed
`Q_a`. Strong continuity uniform in time follows by compactness of the
reference path. Bounded operator norms extend (C.4.6.F18) uniformly to compact
sets of `V`, using a finite net.

The set `{v(t):t<=T}` is compact in `mathcal V`. Comparing tangent Euler
with the integral equation on each time cell, (C.4.6.F18), continuity of `v`
and of its forcing make its integrated consistency error tend to zero.
The error recurrence has factor at most `1+C_T h`; its product is at
most `exp(C_T T)`. Therefore

\[
 \sup_{t\le T}\|v^h(t)-v(t)\|\longrightarrow0.                 \tag{C.4.6.F19}
\]

This argument proves consistency on the vectors actually tested; it
does not assert norm convergence of multiplication operators.

It remains to compare actual finite tangents with the finite mesh
proxies. This is a separate step: a finite-program width theorem alone
does not perform it. Let `v_n^h` be the finite mesh from C.4.6.4, §4 and
let `v_n^{R,delta}` solve the actual finite linear equation, with actual
reference generator, but with the clipped finite-law forcing. Its
inhomogeneous defect against the affine interpolant of `v_n^h` is

\[
\begin{split}
 D_{n,h}(t)={}&[\mathcal L_n(t)-\mathcal L_n^h(\pi_h t)]v_n^h(\pi_h t)\\
 &+\mathcal L_n(t)[v_n^h(t)-v_n^h(\pi_h t)]\\
 &+b_{n,R,\delta}(t)-b_{n,R,\delta}^h(\pi_h t).
\end{split}                                                       \tag{C.4.6.F20}
\]

All differences are on the same finite carrier. On `E_n` the operator
bound, (C.4.6.F17), the clipped-forcing Lipschitz bound and the mesh increment
bound control the second and third lines in `L1([0,T];mathcal V_n)` by
`C_T,R,delta h` (with the same conclusion after a fixed-program event
of probability tending to one). The first line is a finite sum of
bounded-action/rank terms and multiplier terms of the form (C.4.6.F16).
For the latter the testing nodes are the mesh tangent components and
their finitely many forward variations, and the reference `Q_a`.

In detail, the first variation of a training hidden feature is
`D_a^2 xi_a`, so its coefficient error is (C.4.6.F16) with test `xi_a^h`.
The upper preactivation adds `(A-A^h)dot h1^h` and
`B^h(H1-H1^h)`, bounded by the action/HS norms and (C.4.6.F17).
The upper backward variation adds a changed bounded gate acting on
`d^h`, and a changed multiplier `c phi''(Z2)` acting on `dot z2^h`.
Both factors in this latter multiplier are bounded; subtract them
separately. In particular `(c-c^h)dot z2^h` uses (C.4.6.F16) with the
identity clipped outside the common readout interval as multiplier.
It uses L2 smallness of `c-c^h`, not a claimed L-infinity smallness.
The reverse variation next adds `(A-A^h)*dot delta2^h` and
`(B^h)*(delta2-delta2^h)`. For its rank block use the two-factor
HS difference inequality, and for the scalar evaluation block use
Cauchy-Schwarz on the finitely many changed L2 representing fields.
The only product in a representing field requiring a tail cutoff
is a changed bounded first gate multiplying `Q_a^h`; it is again
(C.4.6.F16). This list exhausts the directional maps (C.4.6.T14) and the
generator (C.4.6.P11).

Here the order of cutoffs is essential. By (C.4.6.F19) and strong multiplier
continuity, the population testing nodes, along a chosen countable
refining mesh sequence and all its time nodes, form a relatively compact subset of
the appropriate L2 space. For `dot z2`, for example, use HS convergence
of `B^h`, strong convergence of `dot h1^h`, and the bounded continuous
action curve. Thus their L2 tails vanish uniformly as `M->infinity`.
At every separately fixed mesh their finite empirical cutoff moments
converge to the corresponding population moments. Apply (C.4.6.F16) at each
of that mesh's finitely many nodes, multiply by its time-cell length,
and sum. First send width to infinity, then `h->0` at fixed `M`, then
`M->infinity`. This gives

\[
 \lim_{h\downarrow0}\limsup_{n\to\infty}
 \Pr\{1_{E_n}\int_0^T\|D_{n,h}(t)\|_{\mathcal V_n}\,dt>a\}=0
 \quad(a>0).                                                     \tag{C.4.6.F21}
\]

Subtract the two finite linear integral equations and use the actual
generator bound `C_T`, with initial discrepancy zero. Iterating that
inequality bounds their uniform state difference by
`exp(C_T T) integral ||D_n,h||`. This proves strong finite-mesh
approximation of `v_n^{R,delta}`. Finally the same bound compares its
forcing with the original forcing: (C.4.6.F14)-(C.4.6.F15) make that `L1` difference
arbitrarily small, first choosing `R`, then `delta`. This proves capture
for every fixed `nu`, including a nonatomic one, without constructing
any nonlinear perturbed population flow.

The precise state topology is the following. There are fixed finite
programs, indexed by an accuracy `k` (including fixed source cutoff,
data quadrature and time mesh), with population tangent paths `v^[k]`
and finite same-array realizations `v_n^[k]`, such that

\[
 \sup_{t\le T}\|v^{[k]}(t)-v_\sigma(t)\|_{\mathcal V}\to0,
\]
\[
 \lim_{k\to\infty}\limsup_{n\to\infty}
 \Pr\{\sup_{t\le T}\|v_n(t)-v_n^{[k]}(t)\|_{\mathcal V_n}>a\}=0
 \quad(a>0),                                                     \tag{C.4.6.F22}
\]

and at each fixed `k` every finite same-layer node tuple has its joint
W2 limit. The middle tangent in each program is a finite sum of ranks;
its squared HS norm is the sum of products of their two layer Gram
entries. Consequently its Frobenius norm, and its Frobenius pairings
with fixed generated finite-rank tests, converge to their population
HS counterparts. The action of this tangent and of its adjoint on
each finite list of generated test fields is identified by the same
rank expansion and limiting contractions. Passing through (C.4.6.F22)
extends these assertions to the actual tangent.

In particular at any fixed finite list of times and inputs, same-layer
tuples of clocks, readout, raw first-row variations, hidden variations,
and the responses in (C.4.6.T14) converge in W2 with all pairwise contractions.
For products involving a changed bounded gate, uniform L2 tails of the
testing tangent fields follow from (C.4.6.F22) and (C.4.6.F19), and (C.4.6.F16) again
passes the product. No individual-neuron coupling across widths, or
operator-norm comparison between different carriers, is being claimed.
No W2 statement for hidden tangent paths in the coordinate supremum
norm is needed here.

###### 6. Passive output observations and uniformity on the circle

The Riesz field representing `ell(t,u)` in (C.4.6.T2) is

\[
 \ell_u=\left((u_aD_a\phi'(w\cdot u)Q(u))_{a=1,2},
                \delta(u)\otimes H^1(u),H^2(u)\right).
 \tag{C.4.6.F23}
\]

It satisfies `||ell_u||<=C_T` uniformly in `u`, using only bounded gates,
the action bound and `||c||2`. Thus (C.4.6.F22), joint fixed-program second
moments for the reference fields and finite tangent fields, and their
rank pairings prove prediction-derivative convergence at each fixed
time/input. The same argument is uniform in time at a fixed input:
the reference and tangent are approximated uniformly in their stated
Hilbert norms; multiplication against a fixed proxy uses (C.4.6.F16).
At a fixed proxy all remaining time dependence lies in finitely many
continuous interpolated coefficients/coordinate instructions, so a
finite time net and their compact-family L2 tails give uniform
convergence. An equivalent route is the time equicontinuity argument
in the next paragraph.

For clarity the output fields have adequate time regularity without a
hidden tangent higher-moment assumption. Reference `Q(u)` is uniformly
L2 Lipschitz in time: differentiate
`Q=A*delta2`, `delta2=c phi'(Z2)` and
`Z2=A phi(w.u)` and use the compact-time raw velocity and `c` supremum
bounds. Multipliers in (C.4.6.F23) involving `w` are handled by clipping
the reference `Q(u)` and using its tails from (C.4.6.F13). Hence for every
`a>0`, the probability that the modulus
`sup_{|t-s|<=h,u}||ell_n(t,u)-ell_n(s,u)||` exceeds `a` tends to zero
as `h->0`, in the `limsup_n` sense. The tangent itself is equicontinuous
in `mathcal V_n` in probability since (C.4.6.T6), the generator bound and
`sup_t||b_n(t)||=O_P(1)` give `sup_t||v_n'(t)||=O_P(1)`. These two
facts prove the corresponding scalar time equicontinuity of
`<ell_n(t,u),v_n(t)>`.

Whole-circle regularity is a separate estimate. Parametrize
`u(alpha)=(cos alpha,sin alpha)`. Strong curve differentiation gives

\[
 \partial_\alpha H^1=\phi'(w\cdot u)(w\cdot u'),\quad
 \partial_\alpha Z^2=A\partial_\alpha H^1,
\quad
 \partial_\alpha Q=A^*[c\phi''(Z^2)\partial_\alpha Z^2].
 \tag{C.4.6.F24}
\]

The last two derivatives have L2 norms bounded by `C_T||w||2`.
Differentiate the first field in (C.4.6.F23). Its only additional unbounded
product is

\[
 u_aD_a\phi''(w\cdot u)(w\cdot u')Q(u).
 \tag{C.4.6.F25}
\]

Its L2 norm is bounded by twice that of `|w|Q(u)`, supplied by (C.4.6.F13).
This is a strong derivative, not only a formal product rule. Equation
(C.4.6.F24) first makes `Q(alpha)` a strongly C1 L2 curve and, by integrating
its derivative coordinatewise using Fubini, gives almost-everywhere
absolutely continuous coordinate representatives. In the gate difference
quotient the mean value bound is `2|w| |Q(alpha)|`; the source envelope
`|w| sup_alpha |Q(alpha)|` belongs to L2. Dominated convergence therefore
passes that quotient to (C.4.6.F25). The other term is a bounded multiplier
times the strongly convergent difference quotient of `Q`. The same
envelope gives continuity of the resulting derivative where needed;
in particular it justifies the H1 assertion and its fundamental theorem.
The other first-field terms are bounded by `||Q||2` and
`||partial_alpha Q||2`. Differentiating the other two fields in
(C.4.6.F23) uses the rank product rule and (C.4.6.F24); `||c||infinity` suffices.
Consequently

\[
 \|\ell\|_{H^1([0,2\pi];\mathcal V)}\le C_T
 \quad\hbox{in the population},\qquad
 \sup_{t\le T}\|\ell_n(t,\cdot)\|_{H^1([0,2\pi];\mathcal V_n)}
          =O_P(1).                                             \tag{C.4.6.F26}
\]

The finite assertion follows by integrating the squared estimate and
using (C.4.6.F13) for the supremum in time. There is no claimed Gaussian
distribution or Gaussian tail for (C.4.6.F25). For any absolutely continuous
Hilbert-valued field, the fundamental theorem of calculus and
Cauchy-Schwarz give
`||ell_alpha-ell_beta||<=|alpha-beta|^(1/2)||partial_alpha ell||L2`.
Apply this to (C.4.6.F26). The derivative predictors consequently have a
uniform-in-time circle modulus `O_P(1)|alpha-beta|^(1/2)`, because
`sup_t||v_n(t)||=O_P(1)`. Their population counterpart obeys the
deterministic version.

Choose a finite circle net and finite time net. At every point of their
product the scalar convergence follows from C.4.6.4, §5 and (C.4.6.F23).
A finite union bound gives convergence on the net. The two moduli just
proved bound the interpolation error to the whole compact time/circle
domain. First let width tend to infinity at fixed nets, and then refine
the nets. This proves (C.4.6.T10).

###### 7. Scope and limit order

The order is finite-width right differentiation first; then, for each
fixed target accuracy, fix a source cutoff, deterministic data quadrature
and auxiliary time mesh; take width to infinity; remove these auxiliary
approximations using (C.4.6.F14)-(C.4.6.F22). There is no interchange of a derivative
with an unconstructed population law-to-flow map. All physical horizons
are separately fixed, with no restriction near initialization.

The proof supplies actual finite-GF derivative capture, the compatible
clock/HS/L2 state identification, and passive whole-circle observations.
It proves no raw-GD derivative theorem, no finite-contamination remainder,
no sampling CLT, and no uniform-in-time finite-width convergence. The
uniform population propagator is a distinct claim proved
in C.4.6.2. Transport approximation in
C.4.6.4, §3 is used only to construct a fixed Borel forcing integral; it
is not a claimed transport bound for a nonlinear perturbed flow.

###### Interpretation and nonlinear-continuation boundary

At the fitted endpoint,
`P_infty=I-S_infty Gamma_infty+ E_infty` projects onto `ker E_infty`.
Under the raw conversion it is the canonical raw-metric orthogonal
projection off the span of the weighted training gradients. These directions
preserve both fitted predictions to first order; their unseen evaluations
are `ell(infty,u)P_infty v` and need not be determined by training outputs.
This is an exact decomposition of the actual endpoint tangent operator.
It asserts neither a nonzero unseen change for every direction nor a sign
or risk benefit. A changed scalar clock alone does not describe the response.

For nonlinear continuation this theorem supplies an actual trained
propagator, an admissible full-row clock/HS/readout state, a total-variation
data-to-forcing map, and controlled passive observations. A nonlinear
continuation must additionally control products away from the reference,
including changes of off-support inverse-gate factors times reverse queries,
products of readout and hidden increments, and the quadratic remainder of
hidden activation changes. These are not bounded bilinear maps on arbitrary
L² directions merely because the present linear equation is bounded.

No nonlinear perturbed population flow, finite-contamination remainder,
large path of laws, sampling CLT, expected-risk expansion, endpoint
continuity, transport forcing modulus, or raw-GD derivative theorem is
included in C.4.6. Empirical laws of nonatomic distributions do not approach
them in total variation. This is not a convergence claim for a training-time
Taylor series or evidence of superiority of one learning mechanism.

Section [C.4.7](#c47-nonlinear-training-near-the-fitted-tanh-reference) proves
nonlinear changed-law population continuation and actual finite-GF capture
in a sufficiently small neighborhood of the fitted reference through
physical time 40. Its finite-contamination remainder and width-first bridge
to this response have that fixed horizon. The derivative theorem in C.4.6
retains its separate scope on every fixed finite physical horizon.

#### C.4.7. Nonlinear training near the fitted tanh reference

The infinitesimal response in C.4.6 describes actual finite-network
derivatives at the fitted reference. We now construct the nearby nonlinear
population trajectories through the substantial-training time 40, identify
their actual finite GF, and prove that the same response approximates finite
contaminations to first order. The new estimate controls named source
coefficients along raw Euler programs on a positive neighborhood of laws.
Its constants do not depend on how many atoms approximate a law or on their
smallest mass.

##### C.4.7.1. Model, theorem and observation contract

Fix \(Y\ge1\), \(T=40\), and
\[
 \mathcal Z=\sqrt2S^1\times[-Y,Y],\qquad
 d_{\mathcal Z}((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|.
\]
Write \(\mathcal W_1\) for this Wasserstein distance and \(u=x/\sqrt2\).
Use exactly the two-hidden-layer tanh model of C.4: no biases, equal hidden
widths, stored independent centered Gaussian variances \((1,1/n,1/n^2)\),
and mobilities \((n,1,n)\) for the unhalved loss
\(\mathcal L_\mu=\int(f_n(x)-y)^2\,d\mu(x,y)\). Thus
\[
 h_n^{(1)}=\tanh(W_n^{(1)}u),\quad
 h_n^{(2)}=\tanh(W_n^{(2)}h_n^{(1)}),\quad
 f_n(x)=(W_n^{(3)})^Th_n^{(2)}/n.
\]
Every finite Borel-law loss integral is exact. The actual finite initial
readout is retained. The opposite-label reference is
\[
 \nu_*=\tfrac12\delta_{(\sqrt2e_1,+1)}
             +\tfrac12\delta_{(\sqrt2e_2,-1)}.
\]

On the common canonical Gaussian carrier of III.F and C.4, use the typed
aliases \(w=W^{(1)}\), \(A=W^{(2)}=A_0+K\), \(c=W^{(3)}\), and put
\(H_\ell=L^2(\Omega_\ell)\) for the two layer Hilbert spaces. Define
\[
 \mathcal E=L^2(\Omega_1;\mathbb R^2)
       \oplus\mathcal S_2(L^2(\Omega_1),L^2(\Omega_2))
       \oplus L^2(\Omega_2),\qquad \theta=(w,K,c),
\]
\[
 \|\theta-\bar\theta\|_{\rm raw}^2
   =\|w-\bar w\|_2^2+\|K-\bar K\|_{\rm HS}^2+\|c-\bar c\|_2^2.
\]
Only the learned increment K is Hilbert–Schmidt. Retain the initialized
Gaussian action \(A_0\) and its actual Hilbert adjoint, both with their
joint coordinate realization. The prescribed initialization is
\(\theta(0)=(g,0,0)\), \(g\sim N(0,I_2)\).
For \(\phi=\tanh\), define at each state
\[
 H^{(1)}(u)=\phi(w\cdot u),\quad Z^{(2)}(u)=AH^{(1)}(u),\quad
 H^{(2)}(u)=\phi(Z^{(2)}(u)),\quad f(u)=\langle c,H^{(2)}(u)\rangle,
\]
\[
 \Delta^{(2)}(u)=c\phi'(Z^{(2)}(u)),\quad Q(u)=A^*\Delta^{(2)}(u),
 \quad r(u,y)=f(u)-y.
\]
All population pairings contract within the indicated layer. A rank
\(a\otimes b\) sends \(v\) to \(a\langle b,v\rangle\).

**Theorem.** There is \(\delta_Y>0\), independent of width and sample
count, such that the following hold on
\[
 U_Y=\{\mu\in\mathcal P(\mathcal Z):
                         \mathcal W_1(\mu,\nu_*)<\delta_Y\}.
\]
This neighborhood is relative to all probability laws on \(\mathcal Z\).
It imposes no atom-count, minimum-weight, angle, Gram-rank or prescribed
label-function condition.

1. **Strong autonomous training and reached restart.** Each \(\mu\in U_Y\)
   has a solution \(\theta_\mu\in C^1([0,40];\mathcal E)\), with one-sided
   endpoint derivatives, of
   \[
   \theta'_\mu=\mathcal F_\mu(\theta_\mu)
   =-2\left(\int r\phi'(w\cdot u)Q(u)u\,d\mu,
       \int r\Delta^{(2)}(u)\otimes H^{(1)}(u)\,d\mu,
       \int rH^{(2)}(u)\,d\mu\right).
   \tag{C.4.7.NF}
   \]
   These are Bochner integrals in the three raw spaces. The solution is
   unique among strong raw solutions on the same prescribed carrier with
   the same initialization and retained Gaussian primitives. For every
   \(s\in[0,40]\), its restriction to \([s,40]\) is the unique strong
   continuation from its reached state under the same law and primitives.
   No well-posedness from an arbitrary ambient operator state is asserted.
   The constructed path satisfies
   \[
   \mathcal L_\mu(t)+\int_0^t\|\theta'_\mu(v)\|_{\rm raw}^2\,dv
         =\mathcal L_\mu(0)\le Y^2,\qquad
   \|c_\mu(t)\|_\infty\le2Yt.
   \tag{C.4.7.NG}
   \]
   Query tails and weighted moments used below are proved for these
   trajectories; they are not conditions imposed on competing solutions.

2. **Law continuity.** There are \(C_Y,a_Y,q_Y>0\) such that, for
   \(q=\mathcal W_1(\mu,\rho)\le q_Y\) and \(\mu,\rho\in U_Y\),
   \[
   \sup_{t\le40}\|\theta_\mu(t)-\theta_\rho(t)\|_{\rm raw}
             \le C_Yq^{a_Y}.
   \tag{C.4.7.NL}
   \]
   In particular \(\sup_{t\le40,x}|f_\mu(t,x)-f_\rho(t,x)|
   \le\Omega_Y(q)\), where \(\Omega_Y(q)=C_Yq^{a_Y}\) at small q and
   a sufficiently large constant at larger q. Thus \(\Omega_Y(q)\to0\).

3. **Actual finite GF and arbitrary sampling/width limits.** For each
   fixed Borel \(\mu\in U_Y\), actual finite GF exists globally and
   \[
   \sup_{t\le40,x}|f_{n,\mu}(t,x)-f_\mu(t,x)|\longrightarrow0
                                    \quad\hbox{in probability}.
   \tag{C.4.7.NW1}
   \]
   More generally, for every deterministic sequence of empirical laws
   \(\lambda_k\to\mu\) in \(\mathcal W_1\) and every \(n_k\to\infty\),
   \[
   \sup_{t\le40,x}|f_{n_k,\lambda_k}(t,x)-f_\mu(t,x)|
       \longrightarrow0\quad\hbox{in probability}.
   \tag{C.4.7.NW2}
   \]
   The same holds in joint probability for iid samples of any sizes
   \(m_k\to\infty\), independent of initialization. No relative
   sample-count/width rate is required. State and action identification
   has the precise approximation and observation meaning below.

4. **Nonlinear approximation by the C.4.6 response.** For any probability
   law \(\nu\) on \(\mathcal Z\), put \(\sigma=\nu-\nu_*\) and
   \(\mu_\epsilon=(1-\epsilon)\nu_*+\epsilon\nu\). Take
   \[
   \epsilon_Y=\min\{1/2,\delta_Y/[2(2+2Y)]\}.
   \]
   Then \(\mu_\epsilon\in U_Y\) for \(0\le\epsilon\le\epsilon_Y\).
   With exactly the finite-first response
   \(D_\sigma f=\mathscr D_\sigma f\) of C.4.6,
   there is a deterministic modulus \(\omega_Y(\epsilon)\to0\),
   uniform over all \(\nu\), such that
   \[
   \sup_{t\le40,x}|f_{\mu_\epsilon}(t,x)-f_{\nu_*}(t,x)
                       -\epsilon D_\sigma f(t,x)|
                \le\epsilon\omega_Y(\epsilon).
   \tag{C.4.7.NR}
   \]
   The analogous raw-state remainder holds with the raw variation
   obtained from C.4.6's clock tangent. With common initialization across
   epsilon, let \(D_\sigma f_n=\partial_{\epsilon+}
   f_{n,\mu_\epsilon}|_{\epsilon=0}\) be the actual finite GF derivative.
   For every separately fixed \(\nu\) and every \(a>0\),
   \[
   \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
   \Pr\!\left[
    \frac{\sup_{t\le40,x}|f_{n,\mu_\epsilon}-f_{n,\nu_*}
                         -\epsilon D_\sigma f_n|}{\epsilon}>a
   \right]=0.
   \tag{C.4.7.NB}
   \]
   Width is taken first at fixed positive epsilon. Neither a
   width-uniform finite-n remainder nor an arbitrary simultaneous
   epsilon/width rate is asserted.

For the state assertion, fix a target law and required accuracy. Choose a
finite comparison law and a finite raw Euler mesh, and hence one finite
oracle program, before taking width to infinity. The population program
approximates the path in the raw norm. Its realization on the actual
initialized arrays, including the actual initial readout additively,
approximates actual finite GF in the same-carrier distance
\[
 \|w_n-\bar w_n\|_F/\sqrt n+\|K_n-\bar K_n\|_F
                         +\|c_n-\bar c_n\|_2/\sqrt n.
\]
The approximation error can be made arbitrarily small, uniformly through
40, in probability in the stated order of choices. Learned increments
are finite sums of ranks at each oracle. Their HS norms and pairings are
identified by the finite double sums of the two same-layer Gram
contractions. A finite matrix is never subtracted from a population
operator on a different carrier.

An admitted observation starts with a finite list of raw w,c and named
\(H^{(1)},Z^{(2)},H^{(2)},\Delta^{(2)},Q\) fields at specified times
and inputs, together with identified initialized generated fields. It
uses finitely many correctly typed \(A_0,A_0^*,A(t),A(t)^*,K(t),K(t)^*\)
actions, continuous globally Lipschitz coordinate operations, and fixed
bounded continuous gates multiplying named \(L^2\) fields. Its joint
same-layer empirical law converges with second moments, equivalently in
\(\mathcal W_2\) for each finite tuple. Quadratic contractions and paired
initialized/current hidden observations are included. Arbitrary unbounded
coordinate products, nonlinear clocks and inverse-gate fields require
their own moment and approximation proofs. No cross-carrier operator-norm
convergence is claimed.

##### C.4.7.2. Raw bounds and the comparison estimate

Use the equivalent sum distance
\(d(\theta,\bar\theta)=\|w-\bar w\|_2+\|K-\bar K\|_{\rm HS}
+\|c-\bar c\|_2\). It lies between the raw norm and \(\sqrt3\) times
that norm. At finite width use the explicit normalized distance just
displayed. All comparisons share the same initialized primitives.

Every separately finite-law raw Euler program exists by recursion on the
canonical action spaces. Bounded gates preserve \(L^2\), and each middle
update is a Hilbert–Schmidt rank. For any mesh with nonnegative steps
\(\Delta_k\) summing to at most T, let \(C_k=\|c_k\|_\infty\). The
readout update gives
\(C_{k+1}+Y\le(1+2\Delta_k)(C_k+Y)\). Consequently, for
\(C_T=Y(e^{2T}-1)\), \(R_T=Y+C_T\), and a fixed
\(M_0\ge\|A_0\|_{\rm op}\),
\[
 \|c_k\|_\infty\le C_T,\quad
 \|K_k\|_{\rm HS}\le2TR_TC_T=:K_T,\quad
 \|A_k\|_{\rm op}\le M_0+K_T=:A_T,
\]
\[
 \|w_k\|_2\le\sqrt2+2TR_TA_TC_T,
 \qquad \|\mathcal F_\mu(\theta_k)\|_{(1)}
       \le2R_T(A_TC_T+C_T+1)=:V_T.
 \tag{C.4.7.NE}
\]
Here \(\|\cdot\|_{(1)}\) is the sum of the three raw component norms.
The affine interpolants obey the same bounds. Their crude constants are
finite at T=40 and independent of atom counts, weights and meshes; no
discrete energy inequality is used. The same calculation on finite arrays
works when the initial readout supremum is at most one and the initial
row RMS is at most two, with the corresponding enlarged constants.

At fixed width the exact Borel-law vector field is smooth: on each
finite-dimensional compact parameter set every derivative of its
integrand is bounded uniformly in the compact data domain, so
differentiation under the integral follows from the mean-value formula.
The field is the negative gradient in the metric with squared norm
\(\|v\|_F^2/n+\|B\|_F^2+\|d\|_2^2/n\). Thus
\[
 \mathcal L_\mu(t)+\int_0^t
 \bigl(\|\dot w_n\|_F^2/n+\|\dot K_n\|_F^2
                              +\|\dot c_n\|_2^2/n\bigr)\,ds
       =\mathcal L_\mu(0).
 \tag{C.4.7.NEF}
\]
On a finite maximal interval this bounds each parameter displacement by
\(\sqrt{t\mathcal L_\mu(0)}\), and bounds a terminal Cauchy increment
by \(\sqrt{|t-s|\mathcal L_\mu(0)}\). The finite endpoint and local
smoothness extend the solution, proving global finite existence and
uniqueness. On the initialization event
\(\|A_{0,n}\|_{\rm op}\le10\),
\(\|w_{0,n}\|_F/\sqrt n\le2\), \(\|c_{0,n}\|_\infty\le1\),
which has probability tending to one by the Gaussian estimates in C.4.6,
\(\mathcal L_\mu(0)\le(Y+1)^2\) for all laws. The finite raw states
through40 then lie on a common deterministic ball, and
\(\|c_n(t)\|_\infty\le1+2t(Y+1)\).

The same energy calculation gives (C.4.7.NG) for any already existing strong
population solution. For precision, the scalar prediction differential
has the three raw gradient blocks
\(\phi'(w\cdot u)Q(u)u\),
\(\Delta^{(2)}(u)\otimes H^{(1)}(u)\), and \(H^{(2)}(u)\).
The weighted Taylor argument in III.F.10 gives this scalar differential
without asserting Fréchet differentiability of an ambient activation map.
Bounded multiplier continuity, bounded actions and the rank norm identity
make this gradient jointly continuous in state and input. Compactness of
the input domain makes the continuity uniform near any fixed state: a
contrary sequence has a convergent input subsequence. The law integral is
therefore continuously differentiable, with gradient
\(2\int r\nabla f\,d\mu\). Pair it with (C.4.7.NF) and integrate to obtain
(C.4.7.NG). The readout bound follows pointwise from
\(\int|r|\,d\mu\le\sqrt{\mathcal L_\mu(t)}\le Y\).
These are a priori estimates for an existing path, not an existence
theorem from every raw endpoint.

For \(\tau_R(v)=\|v\mathbf1_{|v|>R}\|_2\), C.4.1's full-row
comparison strengthens to
\[
 \|\mathcal F_\mu(\theta)-\mathcal F_\rho(\bar\theta)\|_{(1)}
 \le C(1+R)\{d(\theta,\bar\theta)+\mathcal W_1(\mu,\rho)\}
       +C\left[\tau_R(\bar c)+\int\tau_R(\bar Q(u))\,d\rho\right]
 \quad(R\ge1).
 \tag{C.4.7.NC}
\]
The constant depends only on the common raw/action bounds and Y. Here is
the complete norm upgrade needed from that proof. Every action difference
uses \(\|K-\bar K\|_{\rm op}\le\|K-\bar K\|_{\rm HS}\). Every
middle-velocity difference is a sum of ranks, and
\[
 \|a\otimes b-\bar a\otimes\bar b\|_{\rm HS}
 \le\|a-\bar a\|_2\|b\|_2+\|\bar a\|_2\|b-\bar b\|_2.
\]
This is the same bound used for its operator norm in C.4.1. The only
unbounded gate products there use
\[
 \|[\phi'(z)-\phi'(\bar z)]P\|_2
                 \le2R\|z-\bar z\|_2+2\tau_R(P).
 \tag{C.4.7.NT}
\]
Split \(|P|\le R\) and its complement and use respectively
\(\operatorname{Lip}(\phi')\le2\) and bounded gates. The upper backward
subtraction applies (C.4.7.NT) to \(P=\bar c\); its error subsequently passes
through a bounded adjoint and bounded first gate. The additional lower
gate difference applies (C.4.7.NT) to \(P=\bar Q\). These errors add, so there
is one cutoff factor, not its square. Changing u costs
\(\|\bar w\|_2|u-v|\), as well as the explicit change of the first
gradient's final vector u. Coupling the laws and integrating gives (C.4.7.NC),
with tails only under the comparison marginal. This accounts for every
norm change in the complete C.4.1 proof. The identical normalized
finite-array calculation gives its same-width form.

Finally \(\mathcal F_\mu(\theta)\) is jointly continuous in raw state
and \(\mathcal W_1\) law. A bounded continuous multiplier converging in
measure converges strongly when applied to one fixed \(L^2\) field, by
truncating that field. This proves each backward-field continuity; the
forward actions and rank identity handle the other factors. Compactness
of the data domain again gives uniformity in data. A continuous
Banach-valued integrand G on that domain has compact separable range and
is Bochner integrable. Coupling at mean distance q gives the bound
\(\omega_G(b)+2\|G\|_\infty q/b\) for a law change: split transport
distances at b and use Markov's inequality. Send q to zero and then b to
zero. These facts justify the joint continuity claim and its use below.

##### C.4.7.3. Uniform passive-query tails for raw Euler programs

Fix \(Y\ge1\), \(T=40\), the raw state \(\theta=(w,K,c)\),
\(A=A_0+K\), and the initialization \((g,0,0)\) stated above.
The aliases \(w=W^{(1)}\), \(A=W^{(2)}\), and \(c=W^{(3)}\)
retain their stated population types. Let
\(\lambda=\sum_a p_a\delta_{(\sqrt2u_a,y_a)}\), where
\(p_a>0\), \(\sum_a p_a=1\), \(|u_a|=1\), and \(|y_a|\le Y\).
Consider any finite raw Euler program with deterministic positive steps
\(h_k\), nodes \(t_k=\sum_{j<k}h_j\), and total length at most \(T\).
All residuals are its actual population residuals. Every named-source
derivative below freezes residuals, contractions, covariance laws, and
deterministic response coefficients; it differentiates only the named
coordinate expression. Throughout, \(\phi=\tanh\); unqualified \(L^p\)
norms use the population of their argument. Generic constants \(C\),
\(C_B\), and \(C_{B,p}\) may increase from one estimate to the next and
depend only on \(Y,T\), the fixed model, and the displayed cap and moment
order. The constants \(C_0,R_0\) defined in (C.4.7.N9) remain fixed.

For a passive query \(u\in S^1\), distinguish its one current forward
slot from the earlier training slots, and define
\[
 \mathcal B_k=\sup_{u\in S^1}
 \left\{|\beta_{ku,ku}|+\sum_{s<k,b}|\beta_{ku,sb}|\right\}.
 \tag{C.4.7.N1}
\]
The coefficients are defined below. Each row is obtained by appending a
fresh unused query to a finite program; earlier unused queries contribute
zero response coefficients. The deterministic row functions extend
continuously to the whole circle. The supremum in (C.4.7.N1) is outside every
expectation.

We prove that there are \(\rho>0\), \(h_0>0\), and \(B<\infty\),
depending only on \(Y,T\) and the fixed model, such that
\[
 \mathcal W_1(\lambda,\nu_*)<\rho,\qquad
 h_{\max}:=\max_k h_k\le h_0
 \quad\Longrightarrow\quad
 \sup_{k:t_k\le T}\mathcal B_k\le B.
 \tag{C.4.7.N-cap}
\]
The same constants work for every finite support cardinality, every
positive set of atom weights, every covariance rank, and every admitted
mesh. They will give constants \(a,M>0\) such that every recomputed
passive reverse query, including at affine Euler interpolation times,
satisfies \(\tau_R(Q(u))\le M e^{-aR^2}\) for \(R\ge1\).

The proof first obtains all moment and transport estimates under a
temporary cap. It reduces (C.4.7.N-cap) to a uniform coefficient bound for
reference raw Euler programs. A fresh-query estimate proves a cap for
the reference physical-clock Euler programs; differentiated consistency
transfers it to reference raw Euler. A second causal induction then
transfers that raw reference cap to all nearby finite laws. All constants
are finite; no useful numerical lower bound on \(\rho\) is asserted.

###### 1. Exact source equations and construction order

Set

\[
 m_{ka}=h_kp_a,\qquad \gamma_{ka}=-2m_{ka}r_{ka}.
\]

Use \(H^{(1)}_{ka}=\phi(w_k\cdot u_a)\), \(Z^{(2)}_{ka}=A_kH^{(1)}_{ka}\),
\(H^{(2)}_{ka}=\phi(Z^{(2)}_{ka})\), \(\Delta^{(2)}_{ka}=c_k\phi'(Z^{(2)}_{ka})\), and
\(Q_{ka}=A_k^*\Delta^{(2)}_{ka}\). A subscript ku denotes an arbitrary passive
query at the current node. The exact Euler updates are

\[
 \begin{split}
 w_{k+1}&=w_k+\sum_a\gamma_{ka}\phi'(w_k\cdot u_a)Q_{ka}u_a,\\
 c_{k+1}&=c_k+\sum_a\gamma_{ka}\phi(Z^{(2)}_{ka}),\\
 K_{k+1}&=K_k+\sum_a\gamma_{ka}\Delta^{(2)}_{ka}\otimes H^{(1)}_{ka}.
 \end{split}                                                   \tag{C.4.7.N2}
\]

The two centered Gaussian orientation families are \(\xi\) on population 2
and \(\zeta\) on population 1. Their exact
source covariances are

\[
 \mathbb E_2[\xi_{ka}\xi_{sb}]=\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{sb}],\qquad
 \mathbb E_1[\zeta_{ka}\zeta_{sb}]=\mathbb E_2[\Delta^{(2)}_{ka}\Delta^{(2)}_{sb}].                  \tag{C.4.7.N3}
\]

The orientation families are independent; the lower population uses \(g\)
and \(\zeta\), and the upper population uses \(\xi\). Within each family, times and inputs
need not be independent. Singular covariance is allowed. The two populations
are not paired finite-neuron coordinates.

With all deterministic objects frozen as above, define

\[
 \alpha_{ka,sb}=\mathbb E_1[\partial_{\zeta_{sb}}H^{(1)}_{ka}]\quad(s<k),\qquad
 \beta_{ka,sb}=\mathbb E_2[\partial_{\xi_{sb}}\Delta^{(2)}_{ka}]\quad(s\le k).
 \tag{C.4.7.N4}
\]

Specializing C.2 (6)–(11), with unit initialized variance and unit mobilities, gives

\[
 \begin{split}
 F_{ka,sb}&=\alpha_{ka,sb}+\gamma_{sb}\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{sb}],\quad s<k,\\
 D_{ka,sb}&=\beta_{ka,sb}
              +\mathbf1_{s<k}\gamma_{sb}\mathbb E_2[\Delta^{(2)}_{ka}\Delta^{(2)}_{sb}],\\
 Z^{(2)}_{ka}&=\xi_{ka}+\sum_{s<k,b}F_{ka,sb}\Delta^{(2)}_{sb},\\
 Q_{ka}&=\zeta_{ka}+\sum_{s\le k,b}D_{ka,sb}H^{(1)}_{sb}.
 \end{split}                                                   \tag{C.4.7.N5}
\]

Here \(F,D\) are scalar coefficient arrays representing the displayed
answers of the retained action \(A\) and its actual adjoint \(A^*\).
All current forward calls precede the current reverse calls. In particular

\[
 \beta_{ka,kb}=\mathbf1_{a=b}\mathbb E_2[c_k \phi''(Z^{(2)}_{ka})].                  \tag{C.4.7.N6}
\]

For a freshly appended passive query replace the right side by its one
distinguished current slot. The current \(c,w\) use only earlier steps;
current \(Z^{(2)}\) has only its own direct current \(\xi\). This proves (C.4.7.N6), including at a
singular or duplicated query. There is no sum of unweighted current
coefficients over all the other inputs.

For a fixed past backward pulse \(p=(s,b)\), put
\(v_{k;p}=\partial_{\zeta_p}w_k\). It is zero for \(k\le s\). Differentiating (C.4.7.N2)
and (C.4.7.N5) gives exactly

\[
 \begin{split}
 v_{k+1;p}=v_{k;p}+\sum_a\gamma_{ka}u_a\bigg[
 &\phi''(w_k\cdot u_a)Q_{ka}(u_a\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_a)\bigg\{\mathbf1_{(k,a)=p}
       +\sum_{q\le k}D_{ka,q}\phi'(w_{t(q)}\cdot u_q)
                         (u_q\cdot v_{t(q);p})\bigg\}\bigg],\\
 \alpha_{ku,p}&=\mathbb E_1[\phi'(w_k\cdot u)\,u\cdot v_{k;p}].
 \end{split}                                                   \tag{C.4.7.N7}
\]

The notation \(q\le k\) sums named training slots through time \(k\);
\(t(q)\) is the time index of the slot, and \(u_q\) is its input.
The direct pulse at step \(s\) has magnitude at most \(2R_0m_p\);
this is where both its atom mass and its step enter.

For an upper forward pulse \(p\), define

\[
 U_{ku;p}=\partial_{\xi_p}Z^{(2)}_{ku},\quad
 C_{k;p}=\partial_{\xi_p}c_k,\quad
 V_{ku;p}=\partial_{\xi_p}\Delta^{(2)}_{ku}.
\]

The exact upper equations are

\[
 \begin{split}
 C_{k;p}&=\sum_{q<k}\gamma_q \phi'(Z^{(2)}_q)U_{q;p},\\
 U_{ku;p}&=\mathbf1_{(k,u)=p}+\sum_{q<k}F_{ku,q}V_{q;p},\\
 V_{ku;p}&=\phi'(Z^{(2)}_{ku})C_{k;p}+c_k \phi''(Z^{(2)}_{ku})U_{ku;p},\\
 \beta_{ku,p}&=\mathbb E_2V_{ku;p}.
 \end{split}                                                   \tag{C.4.7.N8}
\]

These are finite causal derivative equations, not a derivative of an
ambient \(L^2\) vector field. No covariance, contraction, residual, \(\alpha\), or
\(\beta\) is differentiated.

Every fixed finite graph is defined before a uniform cap is sought.
Chronological construction gives a finite Gaussian innovation list;
Q is a Gaussian plus finitely many bounded first features with already
finite coefficients. Lower source derivatives at the next instruction
have a finite polynomial envelope in that finite Gaussian list, and the
bounded upper gates/readout preserve their finite moments. This inductive
argument supplies the finite coefficients in (C.4.7.N4), even on a long graph;
it asserts no bound uniform in its number of instructions.

###### 2. Consequences of a temporary backward coefficient cap

The following bounds are useful without assuming an infinite-horizon
bootstrap. They hold for every prefix on which the already constructed
backward rows have a specified cap B. At a new node the lower estimates
use only past rows; the upper estimates then construct the current row.

For all raw Euler programs through T, independently of a coefficient cap,

\[
 \|c_k\|_\infty\le C_0:=Y(e^{2T}-1),\qquad |r_{ka}|\le R_0:=Y+C_0.
 \tag{C.4.7.N9}
\]

Indeed \(\|c_{k+1}\|_\infty\le(1+2h_k)\|c_k\|_\infty+2h_kY\), since
\(|\phi|\le1\) and \(|f|\le\|c\|_2\le\|c\|_\infty\); the product bound
\(\prod_k(1+2h_k)\le e^{2T}\) proves (C.4.7.N9). Together with (C.4.7.NE), this bounds the raw row, Hilbert–Schmidt increment,
action norm, and raw speed on every prefix, without a coefficient cap.

Suppose the \(\beta\) row cap is B. Define

\[
 D_0=B+2R_0C_0^2T.
\]

Then (C.4.7.N5) gives \(\sum_q|D_{ku,q}|\le D_0\), and hence

\[
 Q_{ku}=\zeta_{ku}+J_{ku},\qquad |J_{ku}|\le D_0,
 \qquad \mathbb E_1\zeta_{ku}^2\le C_0^2.                                \tag{C.4.7.N10}
\]

The J in this display includes both response and learned contributions.
For every \(\lambda\ge0\) and every prefix,

\[
 \mathbb E_1\exp\left(\lambda\sum_{j<k,a}h_jp_a|Q_{ja}|\right)
 \le 2\exp\{\lambda TD_0+\lambda^2T^2C_0^2/2\}.                 \tag{C.4.7.N11}
\]

To verify this, use (C.4.7.N10), the scalar bound
\(\mathbb E e^{\lambda|G|}\le2e^{\lambda^2\operatorname{Var}(G)/2}\), and Jensen with weights
\(h_jp_a/\sum_{i<k}h_i\). No temporal or input independence and no maximum of
a Gaussian history is used.

Put \(M_{k;p}=\max_{s<j\le k}|v_{j;p}|\). Since \(|\phi'|\le1\), \(|\phi''|\le2\), (C.4.7.N7)
and discrete Gronwall give

\[
 {M_{k;p}\over m_p}
 \le2R_0\exp\left\{2R_0D_0T+
                      4R_0\sum_{j<k,a}h_jp_a|Q_{ja}|\right\}.
 \tag{C.4.7.N12}
\]

The direct source appears only once, at time s; every later term is
bounded by \(2R_0h_j(D_0+2\sum_a p_a|Q_{ja}|)M_{j;p}\). Iterating this
scalar inequality proves (C.4.7.N12). Thus, for each \(p\ge1\),

\[
 \|M_{k;p_0}/m_{p_0}\|_{L^p}
 \le L_p(B):=4R_0\exp\{6R_0D_0T+8R_0^2pT^2C_0^2\}.                 \tag{C.4.7.N13}
\]

Here \(p_0\) denotes the slot and p the moment order. In particular

\[
 |\alpha_{ku,sb}|\le A_B h_sp_b,\qquad
 |F_{ku,sb}|\le f_Bh_sp_b,\quad
 A_B=L_1(B),\quad f_B=A_B+2R_0.                                \tag{C.4.7.N14}
\]

There is also a **past-source density bound for \(\beta\)**, stronger than its
row bound for handling law transport. Put \(d_0=2R_0T+2C_0\). From (C.4.7.N8), the
full derivative row sum of c is at most
\(2R_0\sum_{j<k}h_j\mathcal U_j\), where
\(\mathcal U_j=\max_{i\le j,a}\sum_p|U_{ia;p}|\). Hence the row sum of V is at most
\(d_0\mathcal U_k\), and

\[
 \mathcal U_k\le1+f_Bd_0\sum_{j<k}h_j\mathcal U_j
       \le e^{f_Bd_0T}.                                    \tag{C.4.7.N15}
\]

These inequalities hold pointwise. Consequently

\[
 \sum_{p\le k}|\beta_{ku,p}|\le d_0e^{f_Bd_0T}.              \tag{C.4.7.N16}
\]

For completeness fix a single past forward slot \(p_0=(s,b)\). At time s
only \(U_{sb;p_0}=1\) is nonzero, so only \(V_{sb;p_0}=c_s\phi''(Z^{(2)}_{sb})\) is
nonzero and its magnitude is at most \(2C_0\). For k>s, (C.4.7.N8) then yields

\[
 |C_{k;p_0}|\le2R_0m_{p_0}
       +2R_0\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|,
\]
\[
 \max_a|U_{ka;p_0}|
 \le f_Bd_0m_{p_0}
       +f_Bd_0\sum_{s<j<k}h_j\max_a|U_{ja;p_0}|.
\]

In the second inequality the c-memory double sum is bounded by T times
the single sum. Thus

\[
 |\beta_{ku,sb}|\le b_Bh_sp_b\quad(s<k),\qquad
 b_B=2R_0+d_0^2f_Be^{f_Bd_0T},\qquad
 |\beta_{ku,ku}|\le2C_0.                                     \tag{C.4.7.N17}
\]

All constants in (C.4.7.N10)--(C.4.7.N17) are independent of the number of atoms,
minimum atom weight, number of steps, and covariance rank. The equations
also give, for each fixed finite p,

\[
 \|\sup_{j\le k}|w_j|\|_{L^p}+\sup_{j,a}\|Q_{ja}\|_{L^p}
       +\sup_{j,a}\|Z^{(2)}_{ja}\|_{L^p}\le C_{B,p}.               \tag{C.4.7.N18}
\]

For \(w\) use its accumulated update, (C.4.7.N10), and Minkowski with weights
\(h_jp_a\). For \(Z^{(2)}\) use \(|\Delta^{(2)}|\le C_0\), (C.4.7.N14), and the forward innovation of
variance at most one. This does not claim a moment bound for a supremum
of \(Q\) or \(Z^{(2)}\) over all times and inputs. All higher moments here
come from named-field decompositions and source recursions; actions and
adjoints are used only with their stated \(L^2\) bounds.

The absolute estimates alone do not continue the C.2 cap to T. For example
they offer only the sufficient inequality

\[
 B\ \ge\ \Psi_T(B):=d_0\exp\{d_0T(L_1(B)+2R_0)\}.             \tag{C.4.7.N19}
\]

With the overestimates (C.4.7.N9) at T=40 the right side already grows faster
than B with a larger positive value at zero; (C.4.7.N19) cannot select a cap.
This is a failure of this absolute estimate, not a demonstration that
the actual coefficients diverge.

###### 3. Weighted law transport of the coefficients

Assume temporarily that some \(h_*>0\) and \(B_*<\infty\) bound
\(\mathcal B_k\le B_*\) for every two-atom reference raw Euler program
through \(T\) with \(h_{\max}\le h_*\). The reference clock argument
below will prove this bound. We first prove its implication for nearby laws,
retaining all source weights and comparing the same passive input.

Take a finite optimal coupling of a finite \(\lambda\) and the two-atom
reference. Split atoms according to its nonzero pairs and write it as
\(p_a,(u_a,y_a),(v_a,z_a)\). Then

\[
 q=\mathcal W_1(\lambda,\nu_*)=\sum_ap_ae_a,\qquad
 e_a=|u_a-v_a|+|y_a-z_a|.                                   \tag{C.4.7.N20}
\]

Both programs now have the same source names and masses. Splitting a
reference atom does not enlarge its \(\beta\) row cap: for every old slot,
its \(\alpha\), F, and \(\beta\) coefficients split in proportion to the new atom
mass, while the current coefficient remains its one distinguished direct
coefficient (C.4.7.N6). To check this claim, the lower pulse in (C.4.7.N7) is linear in
its initial \(\gamma_{sb}\) and identical repeated reference queries have
identical scalar values. Its normalized derivative is therefore unchanged
by splitting. Equation (C.4.7.N5) then splits F in the same proportion. The
single upper pulse equations (C.4.7.N8), starting with its one current impulse,
split every later coefficient in that proportion as well. Induction in
time proves the claim. Zero coupling weights are discarded.

Run both programs on the same mesh and on their joint Gaussian-source
realization. Theorem III.F.1, the source rule (III.F.9)–(III.F.10), and the
fixed neural-product extension A.2, applied to their finite union
gives, for matched slots,

\[
 \|\xi_i-\bar\xi_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|H^{(1)}_i-\bar H^{(1)}_i\|_2,
\quad
 \|\zeta_i-\bar\zeta_i\|_{L^p}
      =\|N(0,1)\|_{L^p}\|\Delta^{(2)}_i-\bar\Delta^{(2)}_i\|_2.          \tag{C.4.7.N21}
\]

Indeed the cross covariances are the corresponding cross contractions;
subtracting them gives the squared source difference in (C.4.7.N21). This is a
coupling by the source covariance rule, not a Lipschitz claim for an
arbitrary matrix square root or an inverse Gram matrix.

Write \(\mathrm d V=V-\bar V\) for a comparison difference, and let
\(\eta\) bound the maximum raw distance between the two programs through
the prefix. The elementary forward/action subtractions on their common
ball give

\[
 |r_{ka}-\bar r_{ka}|
 +\|H^{(1)}_{ka}-\bar H^{(1)}_{ka}\|_2+\|Z^{(2)}_{ka}-\bar Z^{(2)}_{ka}\|_2
 +\|\Delta^{(2)}_{ka}-\bar\Delta^{(2)}_{ka}\|_2+\|Q_{ka}-\bar Q_{ka}\|_2
 \le C(\eta+e_a),
\]
\[
 |\gamma_{ka}-\bar\gamma_{ka}|
                  \le C h_kp_a(\eta+e_a).                  \tag{C.4.7.N22}
\]

For Q subtract \(A^*\Delta^{(2)}\) directly; c is uniformly bounded pointwise,
so the upper gate difference is \(L^2\) Lipschitz. No first-layer multiplier
occurs in Q itself. At the same passive input u replace \(e_a\) by zero.

Define the coefficient discrepancy at a common passive query by

\[
 E_k=\sup_u\left\{|\beta_{ku,ku}-\bar\beta_{ku,ku}|
          +\sum_{s<k,b}|\beta_{ku,sb}-\bar\beta_{ku,sb}|\right\}.
 \tag{C.4.7.N23}
\]

The current slots are paired as distinguished query slots. Earlier
training slots use the coupling (C.4.7.N20). Comparing the current coefficient
of a far contaminant with a reference *axis* current coefficient would
give an O(1) difference even at arbitrarily small contamination mass.
The same-passive-input convention in (C.4.7.N23) avoids that invalid norm.

Here is the quantitative comparison needed for the bootstrap. If both
programs' previously constructed \(\beta\) rows are at most B, then

\[
 E_k\le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.
 \tag{C.4.7.N24}
\]

Constants can be enlarged to cover \(\eta+q\ge1\); only its approach to zero
matters. The current bound in (C.4.7.N24) uses only past nearby-law \(\beta\) caps.
The rest of this section gives the derivative estimates proving (C.4.7.N24).

First, within either capped program the \(\beta\) row is Lipschitz in its
current passive input, with a constant depending only on B. For \(\alpha\),
differentiate only the displayed input in (C.4.7.N7), or use the mean-value
bound
\(|\phi'(w\cdot u)u-\phi'(w\cdot v)v|\le C(1+|w|)|u-v|\) and (C.4.7.N13). This gives
\(|\alpha_{ku,p}-\alpha_{kv,p}|\le C_Bm_p|u-v|\).
The same estimate holds for F by its contraction formula. For the
upper rows, all past V and the row C are identical at the two passive
queries. In (C.4.7.N8), the past part of U differs by at most
\(\sum_p|F_{ku,p}-F_{kv,p}|\sum_l|V_{p;l}|\), which is bounded by
\(C_B|u-v|\) using (C.4.7.N15). The current \(\phi'(Z^{(2)}),\phi''(Z^{(2)})\) factors differ in \(L^2\) by
\(C\|Z^{(2)}(u)-Z^{(2)}(v)\|_2\le C_B|u-v|\); tanh has bounded third derivative.
Multiplying by the pointwise derivative row bound (C.4.7.N15) proves the
asserted \(\beta\) row bound. Thus a matched active-output row costs at most
\(E_k+C_Be_a\), in addition to the learned contraction discrepancy in
(C.4.7.N22).

Second, subtraction of (C.4.7.N7) has a causal linear propagation part using
the nearby-law coefficients and a source part. The propagation coefficient
for the maximum norm of a pulse difference is bounded by

\[
 2R_0h_k\left(D_0+2\sum_ap_a|Q_{ka}|\right).                 \tag{C.4.7.N25}
\]

The source part consists exactly of the differences of \(\gamma\), the two
input vectors, the gates \(\phi',\phi''\), \(Q\), and \(D\), each multiplied by an
unchanged reference pulse. In particular there is no derivative of D in
this subtraction. The D difference is

\[
 \mathrm d  D_{i,p}=\mathrm d \beta_{i,p}
 +\mathbf1_{t(p)<t(i)}\left[
  \mathrm d \gamma_p \mathbb E_2[\bar\Delta^{(2)}_i\bar\Delta^{(2)}_p]
       +\gamma_p\mathrm d  \mathbb E_2[\Delta^{(2)}_i\Delta^{(2)}_p]\right],          \tag{C.4.7.N26}
\]

where unbarred \(\gamma\) is used in the second term. This also verifies that
learned-memory errors retain \(m_p\).

All unchanged normalized pulses have every fixed finite moment by (C.4.7.N13).
Gate and field differences needed in the source part have an \(L^{12}\) bound
\(C_B(\eta+e_a)^{1/16}\). For bounded gates interpolate the \(L^2\) bound (C.4.7.N22)
with their pointwise bound. For w or Q interpolate their \(L^2\) difference
with the uniform \(L^{24}\) bounds (C.4.7.N18); interpolation gives exponent 1/11,
which implies the weaker displayed exponent on a bounded distance range.
For the input factors themselves use \(|u_a-v_a|\le e_a\).
Products of up to three factors are bounded in \(L^4\) by Hölder with \(L^{12}\)
norms. The random integrating factor obtained from (C.4.7.N25) has every fixed
moment by (C.4.7.N11); Cauchy--Schwarz bounds its product with each forcing
term. Minkowski sums the time/atom masses. Discrete Gronwall therefore
gives, for every past pulse p=(s,b),

\[
 {\|\max_{j\le k}|v_{j;p}-\bar v_{j;p}|\|_2\over m_p}
 \le C_B\left\{(\eta+e_b)^{1/16}+q^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{C.4.7.N27}
\]

One way to verify the averaging in this estimate is to retain each
\(e_a^{1/16}\) until the last step and use
\(\sum_ap_ae_a^{1/16}\le q^{1/16}\). The direct pulse uses (C.4.7.N22) and has
the same factor \(m_p\); dividing by it does not leave \(1/p_b\).
In the D term, its row variation multiplies the reference maximum pulse
norm from (C.4.7.N13); its active-output discrepancy is bounded just above.
There is also a term in which D is unchanged and a *past source's* gate
or input changes. This is where (C.4.7.N17) is essential: its old-source
coefficient satisfies \(|D_{ka,sb}|\le C_Bh_sp_b\), so

\[
 \sum_{s<k,b}|D_{ka,sb}|e_b^{1/16}
             \le C_BT\sum_bp_be_b^{1/16}\le C_BTq^{1/16}.
 \tag{C.4.7.N27a}
\]

The one current coefficient costs \(C_Be_a^{1/16}\) and is averaged
with the outside update weight \(p_a\). A row bound without the past-source
density bound would not justify this step.
These account for every term from the two sums in (C.4.7.N7). No
maximum of the \(e_a\) and no unweighted sum over source indices is taken.

By the second line of (C.4.7.N7), (C.4.7.N27), and Hölder for the difference of its
outside gate, at a common passive input

\[
 \sum_{p<k}|\mathrm d \alpha_{ku,p}|
 \le C_B\left\{(\eta+q)^{1/16}
                              +\sum_{j<k}h_jE_j\right\}.   \tag{C.4.7.N28}
\]

Here \(\sum_{p<k}m_p\le T\); the contribution depending on the source
\(e_b\) averages as in (C.4.7.N27). The identical estimate holds for the F-row
difference by (C.4.7.N5) and (C.4.7.N22). For a matched active output add
\(C_Be_a\) using the passive-input estimate. Entrywise versions keep the
factor \(m_p\) and its \(e_b\) term.

For a current output slot \(i=(k,u)\), write \(q<i\) for
\(t(q)<k\); the symbols \(k,i\) in the next display have this relation.
The exact upper differences are

\[
 \begin{split}
 \mathrm d  U_{i;p}
    &=\sum_{q<i}\mathrm d  F_{i,q}\bar V_{q;p}
                       +\sum_{q<i}F_{i,q}\mathrm d  V_{q;p},\\
 \mathrm d  C_{k;p}
    &=\sum_{q<k}\{\mathrm d \gamma_q \phi'(\bar Z^{(2)}_q)\bar U_{q;p}
             +\gamma_q\mathrm d  \phi'(Z^{(2)}_q)\bar U_{q;p}
             +\gamma_q \phi'(Z^{(2)}_q)\mathrm d  U_{q;p}\},\\
 \mathrm d  V_{i;p}
    &=\phi'(Z^{(2)}_i)\mathrm d  C_{k;p}+\mathrm d  \phi'(Z^{(2)}_i)\bar C_{k;p}
          +c_k\phi''(Z^{(2)}_i)\mathrm d  U_{i;p}
          +\{\mathrm d  c_k \phi''(\bar Z^{(2)}_i)+c_k\mathrm d  \phi''(Z^{(2)}_i)\}
                                                        \bar U_{i;p}.
 \end{split}                                               \tag{C.4.7.N29}
\]

The direct U impulses cancel after pairing the distinguished current
slots. To keep output errors weighted, set

\[
 G_k=(\eta+q)^{1/16}+\sum_{j<k}h_jE_j,\qquad
 L_k=\sum_ap_a\left\|\sum_p|\mathrm d  V_{ka;p}|\right\|_2.
\]

Every barred upper derivative row is bounded pointwise by (C.4.7.N15).
The F propagation coefficients have density \(f_Bh_jp_a\), and \(\gamma\)
retains its original mass. Summing (C.4.7.N29) over source indices, taking \(L^2\),
then averaging its active output index gives

\[
 L_k\le C_BG_k+C_B\sum_{j<k}h_jL_j.                         \tag{C.4.7.N29a}
\]

In this estimate the F-row forcing at a matched active output is at most
\(C_B(G_k+e_a)\) by (C.4.7.N28); the field factors at that output cost
\(C_B(\eta+e_a)\) by (C.4.7.N22). Both are averaged with \(p_a\). In the C-row,
which does not depend on the output query, the same factors are already
multiplied by \(h_jp_a\). These are all appearances of an output transport
cost in (C.4.7.N29). Since \(G_k\) is nondecreasing, discrete Gronwall yields
\(L_k\le C_BG_k\) after increasing \(C_B\). For a common passive output there
is no \(e_a\) term, and the same equations give

\[
 \left\|\sum_p|\mathrm d  V_{ku;p}|\right\|_2
                 \le C_BG_k+C_B\sum_{j<k}h_jL_j\le C_BG_k.
 \tag{C.4.7.N29b}
\]

Taking expected absolute values proves (C.4.7.N24). The current diagonal
contributes at most \(C\eta\) directly from (C.4.7.N6). There is no current
unknown \(E_k\) on the right: (C.4.7.N28) uses only earlier lower updates, and all
upper memory terms in (C.4.7.N29) are strictly earlier. No supremum over the
matched active-output costs \(e_a\) was used.

The raw discrepancy \(\eta\) used above is available before the
reference raw coefficient bound has been proved. The raw bound (C.4.7.NE), the Hilbert–Schmidt transport estimate (C.4.7.NC), and
the actual reference tails of C.4.5.2 (R17)–(R18) give, for every finite
raw Euler program with training law \(\lambda\),

\[
 \sup_{k:t_k\le T}d(\theta_{\lambda,k},\theta_*(t_k))
       \le \omega_T(q+h_{\max}),\qquad \omega_T(s)\to0.     \tag{C.4.7.N30}
\]

To see the mesh term, interpolate the Euler path affinely; its speed is
uniformly bounded by the crude raw ball. Apply the transport estimate
with the actual reference as its tail-bearing endpoint. The distance
from the interpolated Euler state to its left endpoint is at most
\(V_Th_{\max}\), so the cutoff inequality acquires
\(C(1+R_{\rm cut})h_{\max}\). Integrating gives
\(C e^{CR_{\rm cut}}\{(1+R_{\rm cut})(q+h_{\max})+e^{-cR_{\rm cut}^2}\}\). Taking the cutoff to be a sufficiently large constant times
\(\sqrt{\log(e/(q+h_{\max}))}\) proves (C.4.7.N30) for small
\(q+h_{\max}>0\); define the modulus to be zero at zero and enlarge
it using the common raw bound outside that range. This is a comparison to one
existing flow, not a construction of a changed-law flow.
Applying (C.4.7.N30) to \(\lambda\) and to the reference raw Euler program gives a
valid \(\eta\) tending to zero with \(q+h_{\max}\) in (C.4.7.N24).

Assume the reference raw coefficient bound stated at the start of this part. Its reference Euler Q tails are Gaussian by (C.4.7.N10).
For the two raw programs on the **same** mesh, the transport estimate
therefore gives, at a fixed cutoff \(R_{\rm cut}\), the recurrence

\[
 d_{k+1}\le[1+Ch_k(1+R_{\rm cut})]d_k
          +Ch_k\{(1+R_{\rm cut})q+e^{-cR_{\rm cut}^2}\}.
\]

Both start at the same state. Iteration and cutoff choice give

\[
 \sup_k d_k\le\Phi_{B_*}(q),\qquad
 \Phi_{B_*}(q)\longrightarrow0\quad(q\downarrow0),          \tag{C.4.7.N30a}
\]

uniformly over admitted meshes; there is no mesh defect in this
comparison. One can take \(\Phi(q)=Cq e^{C\sqrt{\log(e/q)}}\) for small q
after enlarging constants. The crude ball for the nearby program
suffices; only the reference endpoint of the transport estimate
requires tails.

Set \(B=B_*+1\) and use its invariant duplication property.
At the first potential failed row, all prior nearby-law rows are at
most B. Estimates (C.4.7.N10)--(C.4.7.N29) apply in their causal order. Discrete
Gronwall in (C.4.7.N24) gives

\[
 E_k\le C_B e^{C_BT}
                 \{\Phi_{B_*}(q)+q\}^{1/16}.                \tag{C.4.7.N31}
\]

Choose positive \(\rho\) small enough that the right side is at most 1/2
whenever \(q<\rho\), and put \(h_0=h_*\).
The current row is then at most \(B_*+1/2<B\), contradicting first failure.
The zero-readout initialization has \(\beta=0\), so induction starts.
This proves (C.4.7.N-cap), conditional on that reference bound.
Formula (C.4.7.N10) gives a uniform Gaussian marginal tail for every passive
\(Q\), and (C.4.7.N9) controls the readout. This argument has not inferred
convergence of changed-law paths from their fixed positive proximity to
the reference.

More explicitly, once the cap is fixed, \(Q=G+J\), \(\operatorname{Var}(G)\le C_0^2\),
\(|J|\le D_0\). For \(R_{\rm cut}\ge2D_0\), the event \(|Q|>R_{\rm cut}\) implies
\(|G|>R_{\rm cut}/2\). Integrating the scalar Gaussian tail and absorbing its
polynomial prefactor gives \(\tau_{R_{\rm cut}}(Q)\le M e^{-aR_{\rm cut}^2}\) with finite
positive a,M depending only on the fixed caps. Enlarge M to cover the
remaining \(R_{\rm cut}\ge1\) and the bounded readout. Averaging these individual tail bounds over any admitted training law
preserves the same constants, as does restriction to a smaller radius. A state
on an affine Euler segment is obtained by appending one shorter final
step; the same bound applies to its recomputed fields. This is a
marginal-in-time statement, not an exponential bound for a path maximum.

###### 4. Raw-to-clock mesh errors and their named derivatives

The clock change is exact for continuous reference flow. Its raw Euler
defect and the named derivatives of that defect must still be summed;
the following bounds do so under the temporary cap.

Let

\[
 \mathcal F(w)=w/2+\sinh(2w)/4,\quad \mathcal F'(w)=1/\phi'(w),
\quad R_h(w,b_0)=\mathcal F(w+hb_0\phi'(w))-\mathcal F(w)-hb_0.
\]

Here \(b_0\) is a scalar velocity coefficient.
Put \(\vartheta=hb_0\phi'(w)\). Taylor's integral identity gives

\[
 R_h=h^2b_0^2\phi'(w)^2
                \int_0^1(1-s)\mathcal F''(w+s\vartheta)\,ds.
 \tag{C.4.7.N32}
\]

The elementary hyperbolic identities imply

\[
 \phi'(w)^2|\mathcal F''(w+z)|\le2e^{2|z|},\qquad
 \phi'(w)^2|\mathcal F'''(w+z)|\le4e^{2|z|},\qquad |\phi''|\le2\phi'.
\]

For example \(|\sinh(2(w+z))|\le e^{2|z|}\cosh(2w)\) and
\(\phi'(w)^2\cosh(2w)\le2\); the bound for the third derivative follows in
the same way. Differentiating the explicit integral (C.4.7.N32), rather than
separately estimating the large terms before cancellation, yields

\[
 |R_h|\le Ch^2 b_0^2e^{2h|b_0|},
\]
\[
 |\partial_wR_h|\le Ch^2b_0^2(1+h|b_0|)e^{2h|b_0|},\qquad
 |\partial_{b_0}R_h|\le Ch^2|b_0|(1+h|b_0|)e^{2h|b_0|}.
 \tag{C.4.7.N33}
\]

Every named derivative consequently obeys

\[
 |\partial_p R_h|
 \le Ch^2e^{2h|b_0|}(1+h|b_0|)
                \{b_0^2|\partial_p w|+|b_0||\partial_p b_0|\}.
 \tag{C.4.7.N34}
\]

On the reference, including any split representation, the row-coordinate
update has precisely this form with

\[
 b_{0,a,k}=-2\sum_{j:v_j=e_a}p_jr_{kj}Q_{kj}.
 \tag{C.4.7.N35}
\]

Under the temporary cap its scalar marginals have uniformly bounded
Gaussian norms, by (C.4.7.N10) and the total atom mass. Formula (C.4.7.N11) or the
scalar Gaussian exponential moment controls the factor in (C.4.7.N33)--(C.4.7.N34).
Therefore \(\sum_k\|R_{h_k}\|_{L^p}\le C_{B,p}h_{\max}\) for every fixed finite p.

For a backward source \(p_0\)=(s,j), at the direct injection step
\(|\partial_{p_0}b_0|\le2R_0p_j\) and \(\partial_{p_0}w_s=0\).
Dividing that step's estimate (C.4.7.N34) by \(m_{p_0}=h_sp_j\) costs at most
\(C_{B,p}h_s\). At every later step, (C.4.7.N7), (C.4.7.N13), and the D-row cap give

\[
 \|\partial_{p_0}w_k/m_{p_0}\|_{L^p}
 +\|\partial_{p_0}b_{0,a,k}/m_{p_0}\|_{L^p}\le C_{B,p}.
\]

Using Hölder in (C.4.7.N34) and \(\sum_kh_k^2\le Th_{\max}\) now proves

\[
 {1\over m_{p_0}}\sum_{k\ge s}
               \|\partial_{p_0}R_{h_k}\|_{L^p}
                                  \le C_{B,p}h_{\max}.     \tag{C.4.7.N36}
\]

This proves summability of the named backward-pulse clock defect with
its correct mass normalization. A local lower-population function is
independent of the upper \(\xi\) slots when deterministic coefficients are
frozen; there is no additional \(\xi\) derivative of its clock defect.
The c/K updates are the same in raw and clock formulations.

###### 5. The physical reference source anchor and its transfer

**The reference clock coefficient bound.**

Use the two reference clocks \(X_a=\mathcal F(w_a)-\mathcal F(g_a)\) and the scalar solution
\(w_a=J(X_a,g_a)\) of \(J_X=\operatorname{sech}^2J\), \(J(0,g)=g\). Thus
\(|J_X|\le1\). Its active first features have \(|\partial_X\phi(J)|=\operatorname{sech}^4J\le1\).
The physical reference clock equations are

\[
 \dot X_a=-r_aQ_a,\qquad
 \dot K=-\sum_{a=1}^2r_a\Delta^{(2)}_a\otimes H^{(1)}_a,\qquad
 \dot c=-\sum_{a=1}^2r_aH^{(2)}_a.                                \tag{C.4.7.N37}
\]

Their raw fields are the reference flow of C.4.5.1 (R4)–(R8).
The factor \(-r_a\) in (C.4.7.N37) is \(-2p_ar_a\) with \(p_a=1/2\).
On the common
carrier these equations are Lipschitz on the bounded sets used below,
by the explicit subtractions that follow; Euler convergence here needs
no raw first-gate estimate.

For the auxiliary source extraction use finite initialized matrices
with \(\|A_0\|_{\rm op}\le10\) and **zero readout**. This auxiliary fixed program identifies the zero-readout population
coefficients. The actual finite-network initialization in the theorem
retains its specified random readout. In the finite calculation every
field norm is \(\|v_n\|_2/\sqrt n\), and the increment norm is the
ordinary Frobenius norm \(\|K_n\|_F\). These are the finite versions of
population \(L^2\) and Hilbert–Schmidt norms by III.F.8
(III.F.28)–(III.F.31). By (C.4.7.N9) and bounded activations, at all nodes,

\[
 \|c_k\|_\infty\le C_0,\quad |r_{ka}|\le R_0,\quad
 \|K_k\|_{HS}\le2TR_0C_0,\quad \|A_k\|_{op}\le M:=10+2TR_0C_0.
 \tag{C.4.7.N38}
\]

These bounds also hold if a fresh root is added to one forward or
reverse query and all descendants, including residuals, are recomputed.
Forward tanh and its gate remain bounded, so every subsequent c and K
increment obeys the same estimate. Reverse forcing changes only the
clock increment directly. Thus there is no assumption that a forced
program retains a gradient-flow energy identity.

For two unforced subsequent clock states on this ball set
\(x=\sum_a\|\mathrm d  X_a\|_2\), \(\varkappa=\|\mathrm d  K\|_{\rm HS}\), \(z=\|\mathrm d  c\|_2\),
and \(d=x+\varkappa+z\). The same-root scalar bound for J gives

\[
 \begin{split}
 \sum_a\|\mathrm d  H^{(1)}_a\|_2&\le x,\qquad
 V:=\sum_a\|\mathrm d  Z^{(2)}_a\|_2\le Mx+2\varkappa,\\
 D:=\sum_a\|\mathrm d \Delta^{(2)}_a\|_2&\le2z+2C_0V,\qquad
 P:=\sum_a\|\mathrm d  Q_a\|_2\le MD+2C_0\varkappa,\\
 S:=\sum_a|\mathrm d  r_a|&\le2z+C_0V.
 \end{split}                                               \tag{C.4.7.N39}
\]

The three velocity differences in (C.4.7.N37) are at most

\[
 MC_0 S+R_0P,\qquad C_0S+R_0(D+C_0x),\qquad S+R_0V.                    \tag{C.4.7.N40}
\]

For example subtract \(r\Delta^{(2)}\otimes H^{(1)}\) into its residual, upper
field, and lower feature differences; the rank norm is the product of
its \(L^2\) factors. Equations (C.4.7.N39)--(C.4.7.N40) give a bound \(Ld\) with the fixed
overestimate

\[
 L=100(1+M+C_0+R_0)^4,
 \qquad E=\exp(LT).                                        \tag{C.4.7.N41}
\]

Hence any post-pulse Euler difference is amplified by at most E,
independently of width, step count, and step sizes. Splitting an atom
retains these equations after summing its identical descendants.

Insert \(\varepsilon e\), with \(e\) a fresh standard Gaussian root of
the answer's population, into the complete reverse answer at slot \((s,b)\).
Its only immediate state change is in the clock corresponding to
\(v_b=e_a\), with norm at most

\[
 2R_0 h_sp_b|\varepsilon|\|e\|_2.                               \tag{C.4.7.N42}
\]

For a passive first feature
\(H^{(1)}(u)=\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))\), the difference is at most x.
The subsequent passive feature difference is therefore bounded by
\(2R_0Eh_sp_b|\varepsilon|\|e\|_2\).

Instead insert the root into one complete forward answer \(Z^{(2)}_{sb}\).
At that node its activation, \(\Delta^{(2)}\), residual, and reverse answer change
by at most, respectively,

\[
 |\varepsilon|\|e\|_2,\quad 2C_0|\varepsilon|\|e\|_2,\quad
 C_0|\varepsilon|\|e\|_2,\quad 2MC_0|\varepsilon|\|e\|_2.
\]

Use the old Q and the bounded new residual when subtracting the clock
update. The three immediate state increments have total norm at most
\(P_0h_sp_b|\varepsilon|\|e\|_2\), where

\[
 P_0=2\{MC_0^2+2R_0MC_0+C_0^2+2R_0C_0+C_0+R_0\}.                          \tag{C.4.7.N43}
\]

The terms arise from \(\mathrm d (rQ)\), \(\mathrm d (r\Delta^{(2)}\otimes H^{(1)})\), and
\(\mathrm d (rH^{(2)})\), respectively. A passive later \(\Delta^{(2)}\) satisfies

\[
 \|\mathrm d \Delta^{(2)}(u)\|_2\le z+2C_0(Mx+\varkappa)\le K_0d,
 \qquad K_0=1+2C_0(M+1).                                    \tag{C.4.7.N44}
\]

Thus its post-pulse change is at most
\(P_0K_0Eh_sp_b|\varepsilon|\|e\|_2\).

Extract the named coefficients by the full mechanism of C.4.5.2
(R5)--(R15). Here are the hypotheses and the order of limits needed
for this application. At each fixed graph clip the Gaussian first
roots smoothly. The passive feature's derivatives with respect to X
are bounded uniformly in the root clipping level; its root
derivatives are bounded at each fixed level. A readout clip equal to
the identity on a neighborhood of \([-C_0,C_0]\) is inactive. Thus the
fixed-program theorem and its complete source extension apply to
forced and unforced graphs, including singular covariance and
variance-zero slots. At a fixed graph all source derivatives have a
finite deterministic bound independent of root clipping: the clock
derivatives are bounded, the readout is bounded, and every matrix
answer is a source plus a finite sum with fixed coefficients.
Chronological convergence and this derivative bound remove root
clipping and make all coefficients continuous as \(\varepsilon\) tends to
zero, exactly as proved in C.4.5.2, proof part 2, (R5)–(R7). No mesh-uniform source cap was
used in this fixed-graph step.

Fix the mesh and nonzero \(\varepsilon\) and first let width tend to infinity.
The initialization operator event and \(\|e_n\|_2/\sqrt n\to1\) have
probability tending to one, by III.F.2 (III.F.4) and the Gaussian
second-moment calculation. Theorem III.F.1 and its extension just checked transfer
(C.4.7.N42)--(C.4.7.N44) and their pairing with the fresh Gaussian root. In the
source coordinate expression that root enters only in the specified
slot as \(\mathrm{slot}+\varepsilon e\). The selected residuals and covariance laws
may depend on \(\varepsilon\) but are deterministic, and all Gaussian source
groups are independent of this local new root. Conditional
one-dimensional Gaussian integration by parts therefore gives

\[
 \mathbb E[eV^\varepsilon]=\varepsilon\mathbb E[\partial_{\rm slot}V^\varepsilon].
 \tag{C.4.7.N45}
\]

The expectation in (C.4.7.N45) is in the population of the observed field.
The unforced expression is independent of \(e\). Cauchy--Schwarz in the
joint limit, division by \(|\varepsilon|\), then the fixed-graph
zero-forcing continuity just proved yield

\[
 |\alpha^{\rm cl}_{ku,sb}|\le2R_0Eh_sp_b,
 \qquad |\beta^{\rm cl}_{ku,sb}|\le P_0K_0Eh_sp_b\quad(s<k),
 \qquad |\beta^{\rm cl}_{ku,ku}|\le2C_0.                     \tag{C.4.7.N46}
\]

The argument works for each passive u with the same constants.
Consequently every reference physical clock Euler program through T
has the cap

\[
 B_{\rm cl}=2C_0+TP_0K_0E.                                   \tag{C.4.7.N47}
\]

This proves a bound for the specified named coefficients. It does
not infer a derivative transverse to a singular source support from
the unforced value law. The fresh root and the width-first,
forcing-second order in (C.4.7.N45) are essential.

**Transfer from clock Euler to raw reference Euler.**

Compare the reference raw and clock Euler programs on the same mesh
and common Gaussian source carrier. Write
\(X^r_a=\mathcal F(w^r_a)-\mathcal F(g_a)\) for the transformed raw program and \(X^c\)
for clock Euler. The raw program satisfies the exact clock update
with the extra vector of defects (C.4.7.N32). Its lower first-feature
expression is the same function of X and g as in the clock program.

Define \(E_k\) by (C.4.7.N23) for this raw/clock pair, with no change of data
law, and assume a temporary cap B on all preceding raw \(\beta\) rows.
Let \(\eta_h\) bound the raw discrepancy of their fields. There is an
\(\eta_h\) tending to zero with \(h_{\max}\) independently of that cap: (C.4.7.N30)
compares raw Euler with the actual reference, while (C.4.7.N39)--(C.4.7.N41), the
bounded clock speed, and the integrated Euler error compare clock
Euler with the same reference in clock/HS/\(L^2\) norm. The scalar bound
\(|J_X|\le1\) converts the latter distance to raw distance. In particular
all the field differences in (C.4.7.N22) are \(O(\eta_h)\).

For a backward pulse \(p_0\)=(s,b), put
\(\chi^r_{k;p_0}=\partial_{\zeta_{p_0}}X^r_k\), and define \(\chi^c\) similarly.
For a lower first feature let \(J_q^r\) and \(J_q^c\) denote its two
clock derivatives. Each has norm at most two, and their difference
in \(L^2\) is at most \(C\eta_h\), since each is a product of bounded tanh
gates with bounded derivatives. At reference active slots one can
use the sharper bound one. Differentiating the two clock recursions
gives the exact pair

\[
 \chi^r_{k+1;p_0}=\chi^r_{k;p_0}
   +\sum_a\gamma^r_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^r_{ka,q}J_q^r\chi^r_{t(q);p_0}\right\}
   +\partial_{p_0}R_k,
\]
\[
 \chi^c_{k+1;p_0}=\chi^c_{k;p_0}
   +\sum_a\gamma^c_{ka}v_a\left\{\mathbf1_{(k,a)=p_0}
             +\sum_{q\le k}D^c_{ka,q}J_q^c\chi^c_{t(q);p_0}\right\}.
 \tag{C.4.7.N48}
\]

Here \(v_a\) is the reference axis of that atom, and the lower feature
derivative is a row vector applied to \(\chi\). The clock reference cap
(C.4.7.N47) bounds its D rows by \(D_{\rm cl}=B_{\rm cl}+2R_0C_0^2T\). Since the clock gates
are bounded, its pulses satisfy the **pointwise** bound

\[
 \max_{j\le k}|\chi^c_{j;p_0}|/m_{p_0}
                        \le2R_0\exp(4R_0D_{\rm cl}T).         \tag{C.4.7.N49}
\]

Subtract (C.4.7.N48). Its raw propagation coefficients have a deterministic
bound depending only on B and (C.4.7.N9); there is no random Q multiplier.
Differences of \(\gamma\) and the clock gates cost \(C\eta_h\), multiplied
by the bounded normalized reference pulse (C.4.7.N49). The D-row difference
is at most \(E_j+C\eta_h\) by (C.4.7.N26). Finally (C.4.7.N36) bounds the sum of
the normalized defect derivatives in \(L^2\) by \(C_Bh_{\max}\). Discrete
Gronwall gives

\[
 {\|\max_{j\le k}|\chi^r_{j;p_0}-\chi^c_{j;p_0}|\|_2\over m_{p_0}}
    \le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{C.4.7.N50}
\]

The maximum on the left is controlled by the sum of the forcing
norms and a deterministic integrating factor. It does not require
an \(L^2\) bound on a supremum of the raw field discrepancy.

Take expected first-feature derivatives to obtain the same bound for
the \(\alpha\) row difference, after summing its source masses. For a
passive output its derivative outside chi differs in \(L^2\) by
\(C\eta_h\) and is bounded, so the statement remains uniform in u.
The upper source equations (C.4.7.N8) are identical in the two schemes;
subtracting them as in (C.4.7.N29), using the source density bounds and
discrete Gronwall, proves

\[
 E_k\le C_B\left\{\eta_h+h_{\max}
                                  +\sum_{j<k}h_jE_j\right\}.
 \tag{C.4.7.N51}
\]

Set \(B=B_{\rm cl}+1\). At any first potentially failed raw row, all previous
rows obey this cap. The defect estimate (C.4.7.N36) uses only those previous
raw Q fields. The current \(\alpha\) then obeys (C.4.7.N50), and the current
\(\beta\) obeys (C.4.7.N51), whose right side has no current \(\beta\). Gronwall
yields \(E_k\le C_Be^{C_BT}(\eta_h+h_{\max})\). Choose \(h_*\) positive and
small enough that this is at most 1/2 whenever \(h_{\max}\le h_*\).
Then the current raw row is at most \(B_{\rm cl}+1/2<B\), so induction cannot
fail. Both zero-readout initial programs have \(\beta=0\). This proves the reference raw coefficient bound with \(B_*=B_{\rm cl}+1\).
The weighted law-transport induction above now proves (C.4.7.N-cap) and its
uniform passive Gaussian-tail consequence through physical time \(T=40\).

The two bootstraps are separate: the first uses one fixed, independently
proved clock anchor to control reference raw Euler; the second uses
that raw anchor and weighted law transport to control all nearby finite
laws. Neither bootstrap takes a supremum of far-atom transport costs
or assumes the tails of the not-yet-controlled current query.

##### C.4.7.4. Strong completion, law continuity and reached uniqueness

The preceding source argument supplies a radius \(\rho>0\), a mesh
threshold and constants \(a,M>0\) such that all sufficiently fine
finite-law raw Euler programs in \(U_\rho\) satisfy
\[
 \tau_R(c_k)+\int\tau_R(Q_k(u))\,d\mu(u,y)
                      \le M e^{-aR}\quad(R\ge1).
 \tag{C.4.7.NH}
\]
It actually supplies Gaussian tails for every passive query. The weaker
exponential estimate (C.4.7.NH) is enough for the remaining construction.
All constants are uniform on a fixed smaller neighborhood. Choose
\(0<\delta_Y<\rho/4\); further decreases do not affect the argument.

For two Euler interpolants on meshes of maximal steps \(h,h'\), with
laws \(\mu,\nu\) in that smaller neighborhood, put
\[
 s(t)=d(\theta^h_\mu(t),\theta^{h'}_\nu(t))
                     +q+V_T(h+h'),\qquad q=\mathcal W_1(\mu,\nu).
\]
The preceding-node distance is at most the current distance plus
\(V_T(h+h')\). Apply (C.4.7.NC) at these nodes and (C.4.7.NH), and choose
\(R=1+a^{-1}\log(1/s)\). For \(0<s\le1\) this gives almost everywhere
\[
 s'(t)\le Ls(t)\log(e/s(t)),\qquad
 s(t)\le e^{1-\alpha(t)}s(0)^{\alpha(t)},\quad
                         \alpha(t)=e^{-Lt}>0.
 \tag{C.4.7.NO}
\]
To verify the integration, set \(z=\log(e/s)\); then \(z'\ge-Lz\).
Multiplication by \(e^{Lt}\) and integration prove the displayed bound.
At a zero value use \(s+\eta\), the monotonicity of
\(v\log(e/v)\) on \((0,1)\), and then \(\eta\downarrow0\).
For sufficiently small initial s the bound remains below one through T,
so a first-exit argument validates its use on the whole interval. For
larger errors the common raw bound (C.4.7.NE) suffices. No lower bound on the
tail exponent relative to T is needed.

Finite probability laws are dense in \(\mathcal W_1\) on the compact
data domain: partition it into finitely many Borel cells of diameter at
most b, move each cell's mass to a representative, and pay at most b.
For any \(\mu\in U_Y\), take such finite laws \(\nu_j\to\mu\) and
meshes \(h_j\to0\). They eventually lie in a fixed smaller neighborhood
where (C.4.7.NH) is uniform. Formula (C.4.7.NO) makes the Euler paths Cauchy in
\(C([0,T];\mathcal E)\), including the HS component. The same estimate
between any two families makes the limit independent of both choices.
Their preceding-node states have the same limit. Joint field continuity
proved after (C.4.7.NC) now passes their integral equations to
\[
 \theta_\mu(t)=(g,0,0)+\int_0^t\mathcal F_\mu(\theta_\mu(s))\,ds.
 \tag{C.4.7.NI}
\]
The convergence of the integrands is uniform in time. Otherwise a sequence
of discrepant times has a convergent subsequence, and joint continuity at
the corresponding limiting state and law gives a contradiction. Thus
(C.4.7.NI) is a strong \(C^1\) equation in all three raw components, and every
coefficient is computed from the current state and the fixed law. Its
energy and readout bounds are (C.4.7.NG).

The needed tails pass to the constructed paths without a coordinate
supremum assumption. For fixed R the map
\(v\mapsto(|v|-R)_+\) is 1-Lipschitz on \(L^2\), and
\[
 \|v\mathbf1_{|v|>2R}\|_2
                \le2\|(|v|-R)_+\|_2\le2\tau_R(v).
 \tag{C.4.7.NP}
\]
Uniform state convergence and bounded multiplier continuity imply
uniform-in-input Q convergence at a fixed time. The resulting continuous
positive-part norms pass also through the converging law integral.
Consequently (C.4.7.NH), with an enlarged M and exponent \(a/2\), holds for
the constructed path, at every time with the same constants.

Comparing two such paths by (C.4.7.NC), their tails and (C.4.7.NO) proves (C.4.7.NL), with
\(a_Y=e^{-LT}\) after changing constants. The forward formulas give
\[
 \sup_u\|H^{(1)}_\theta(u)-H^{(1)}_{\bar\theta}(u)\|_2
          \le\|w-\bar w\|_2,
\]
\[
 \sup_u\|Z^{(2)}_\theta(u)-Z^{(2)}_{\bar\theta}(u)\|_2
          \le\|A\|_{\rm op}\|w-\bar w\|_2+\|K-\bar K\|_{\rm HS}.
\]
Together with bounded c these give the same type of uniform prediction
modulus. Common raw bounds give its constant large-q branch.

An arbitrary competing strong raw solution on the prescribed carrier
has a bounded path on a compact interval. Apply (C.4.7.NC) with that competitor
as its first endpoint and the constructed solution as its tail-bearing
second endpoint. Only the latter's tails enter. Formula (C.4.7.NO) at zero
initial discrepancy proves equality. Applying this argument on
\([s,40]\) proves the reached-state uniqueness and restart assertion.
Existence for this restart is furnished by the restriction of (C.4.7.NI);
neither new Gaussian roots nor a local theorem from every ambient state
is needed. No extra tail or weighted regularity is imposed on a
competitor.

We will also need the law comparison on one common Euler mesh with no
mesh-error floor. Subtract the two recursions at the same node and use
(C.4.7.NC) and (C.4.7.NH). If \(s_k=d(\theta^h_\mu(t_k),\theta^h_\nu(t_k))+q\),
then
\(s_{k+1}\le s_k+L\Delta_k s_k\log(e/s_k)\) below one. Compare each
step with the scalar increasing solution of
\(v'=Lv\log(e/v)\): its derivative increases while \(v<1\), so its
exact increment dominates the Euler increment. Induction and the same
first-exit bound give
\[
 \sup_k d(\theta^h_\mu(t_k),\theta^h_\nu(t_k))
                      \le Cq^{a_Y}.
 \tag{C.4.7.NLM}
\]
All constants remain uniform on the smaller neighborhood. Bounded c and
the displayed forward inequalities also give
\(\sup_u\|Q_\theta(u)-Q_{\bar\theta}(u)\|_2\le C d(\theta,\bar\theta)\)
for these Euler states: subtract \(A^*\Delta^{(2)}\) and use the
uniform pointwise bound on the comparison readout in its gate product.

##### C.4.7.5. Actual finite GF and the observation limits

The population tail estimate does not by itself assert a finite-width
moment theorem. We therefore give the approximation order explicitly.
Fix one finite comparison law \(\nu\) in the neighborhood and one fine
raw Euler mesh h. The resulting population program has finitely many
instructions. Expand K as its finite sum of ranks, and realize this
program on the actual initialized finite arrays using its deterministic
population residuals and contractions. Include the actual finite initial
readout additively in the proxy parameters, as in C.4.3 (A3). Its assigned
increments are the oracle increments. Actual GF and proxy therefore start
at the same finite arrays.

The complete fixed-program theorem III.F.1–7 and A.1 applies to this
fixed graph. Its roots are the two first-row Gaussians, the two queried
orientations are \(A_0\) and its actual adjoint, and the coordinate
instructions are continuous of at most linear growth. A backward product
is a bounded gate times a named \(L^2\) field. To recover the recomputed
proxy feedback from the oracle instructions, subtract each gate product,
truncate its fixed oracle field as in (C.4.7.NT), take width to infinity and
remove that cutoff using its joint second-moment limit. Scalar
contractions converge by the two-factor RMS inequality. The finite rank
expansion handles learned actions in both orientations. The finite
initial readout RMS and supremum tend to zero; the same finite induction
propagates this additive discrepancy while preserving the actual finite
initialization.

At this fixed \((\nu,h)\), recomputed proxy fields and assigned
velocities consequently differ from their oracle versions by
\(o_{\mathbb P}(1)\). The proxy lies on a deterministic enlargement
of the ball (C.4.7.NE) with probability tending to one. Its increment norm and
pairings have exactly their HS interpretation: if
\(K=\sum_i a_i\otimes b_i\) and
\(\widetilde K=\sum_j\tilde a_j\otimes\tilde b_j\), then
\[
 \langle K,\widetilde K\rangle_{\rm HS}
       =\sum_{i,j}\langle a_i,\tilde a_j\rangle
                    \langle b_i,\tilde b_j\rangle.
 \tag{C.4.7.NK}
\]
The finite Frobenius contraction of ranks \(a_ib_i^T/n\) is the same
sum of normalized pairings. Each is an identified same-layer second
moment, so (C.4.7.NK) involves no cross-carrier subtraction.

For any fixed cutoff R, positive-part second-moment convergence, (C.4.7.NP)
and (C.4.7.NH) imply at the finitely many proxy nodes
\[
 \tau_R(\bar c_n(t_k))+
       \int\tau_R(\bar Q_n(t_k,u))\,d\nu
                         \le M'e^{-a'R}+o_{\mathbb P}(1).
 \tag{C.4.7.NPT}
\]
These are normalized finite RMS tails. The constants \(M',a'>0\) are
independent of the chosen law and mesh in the smaller neighborhood;
fixed cutoff rescaling changes only these constants. No growing
transcript has been submitted to a fixed-program theorem.

Let \(\lambda_j\to\mu\) in \(\mathcal W_1\), with
\(n_j\to\infty\). The actual laws may here be arbitrary Borel laws;
only the proxy law is finite. Compare actual GF with the proxy on their
common finite carrier, using the law-independent finite energy bounds
and (C.4.7.NC). A proxy interpolant differs from its preceding node by at most
\(V'h+o_{\mathbb P}(1)\). On any interval \([b_0,b_1]\) of length
at most \(\ell\), the sum distance E obeys
\[
 \sup_{b_0\le t\le b_1}E(t)
 \le e^{C(1+R)\ell}E(b_0)
   +C\ell e^{C(1+R)\ell}
    \{(1+R)(\mathcal W_1(\lambda_j,\nu)+h)
                     +M'e^{-a'R}+o_{\mathbb P}(1)\}.
 \tag{C.4.7.NAP}
\]
The proxy velocity defect is included in the fixed-program probability
error. Every random error here is for fixed \(\nu,h,R\).

Choose a finite time partition with \(C\ell<a'/2\). On each interval
the amplified tail in (C.4.7.NAP) tends to zero as R increases. For a required
final accuracy, choose the last interval's cutoff and its required
incoming accuracy, then the preceding interval's cutoff and incoming
accuracy, and continue backwards over the finite partition. This produces
finitely many fixed cutoffs and positive tolerances. Next choose the
finite law \(\nu\) close enough to \(\mu\), and h small enough, so
all their deterministic errors meet these tolerances. Finally take
\(j\to\infty\). The finitely many fixed-program probability errors
and \(\mathcal W_1(\lambda_j,\mu)\) vanish together. Forward induction
in (C.4.7.NAP) gives arbitrarily small finite GF/proxy raw error through40.
This choice order is why an arbitrarily small positive tail exponent
suffices. It neither asserts a finite moment bound uniform over all laws
nor requires a relation between sample count and width.

The population proxy converges in raw norm to (C.4.7.NI), while each fixed
proxy's joint node laws, action tests, and pairings converge by the
fixed-program theorem. These two comparisons prove the stated state
identification. Forward/prediction formulas are Lipschitz on the bounded
raw balls, uniformly in u. Full row bounds give input continuity, and
the velocity bound gives the needed time continuity. Finite time/input
nets, with the fixed-program limit at their nodes, yield (C.4.7.NW2).
Holding \(\lambda_j=\mu\) for all j in precisely the same comparison
proves (C.4.7.NW1), including for a nonatomic Borel law with exact loss
integration. No empirical total-variation approximation has been used.

Here are the further observation passages. In any same-carrier
comparison, applying a named bounded action costs its norm times the
input error, plus the input norm times the HS increment error if the
learned action changes. A globally Lipschitz coordinate operation
preserves \(L^2\) approximation. For a fixed bounded continuous gate
times a named \(L^2\) field, first truncate that field and restrict the
gate arguments to a compact box. On the box uniform continuity applies;
off it the joint second-moment limits give tightness and uniform
integrability. Remove the restrictions after the fixed approximation
limit. Induction over a finite observation program proves the joint
same-layer \(\mathcal W_2\) limit and all quadratic contractions in
the theorem. Keeping the initialized and current hidden fields in the
same tuple gives the paired observations. This argument admits no
arbitrary unbounded product and makes no operator-norm comparison
between carriers.

For iid data of size m, the compact partition proof is elementary.
Move both \(\mu\) and its empirical law to the representatives of a
partition with cell diameter b. The two moves cost at most \(2b\).
The remaining distance is at most half the data diameter times the sum
of cell-mass discrepancies. Each empirical cell frequency has variance
at most \(1/(4m)\), so this remaining term tends to zero in probability
for the fixed finite partition. First let m increase, then b decrease.
Thus empirical \(\mathcal W_1\) converges in probability. All proxy
events in (C.4.7.NAP) concern its fixed law and initialization, independent of
the observations. Combining these events and the data-distance event
by a finite union bound proves the iid conclusion for arbitrary
\(m_j,n_j\to\infty\).

##### C.4.7.6. Nonlinear variation and the finite nonlinear limit

Continue with the strong raw flows, common Gaussian carrier, neighborhood,
and finite-GF capture constructed above, on \(T=40\). All field, action,
raw-norm and data-space notation is unchanged. Law integrals written in
\((u,y)\) use the pushforward under \(u=x/\sqrt2\). Put \(D_Y=2+2Y\),
an upper bound for the diameter of \(\mathcal Z\) in its stated metric.

Write \(\theta_*=\theta_{\nu_*}\). Its identification with the reference
of C.4.6 follows from the strong equation, common initialization and
reached-state uniqueness already proved. For every \(\nu\in\mathcal P(\mathcal Z)\),
put \(\sigma=\nu-\nu_*\) and

\[
 \mu_{\epsilon,\nu}=(1-\epsilon)\nu_*+\epsilon\nu,
 \qquad
 \epsilon_Y=\min\{1/2,\delta_Y/(2D_Y)\}>0.
 \tag{C.4.7.NV-radius}
\]

The radius \(\delta_Y\) is chosen below inside the neighborhood on which
the preceding construction has uniform constants. Coupling unchanged
mass to itself gives
\(\mathcal W_1(\mu_{\epsilon,\nu},\nu_*)\le\epsilon D_Y\le\delta_Y/2\).
Thus every \(\nu\), including every nonatomic law, and the whole closed
interval \(0\le\epsilon\le\epsilon_Y\) are admitted.

The conclusions proved here are

\[
 \sup_{\nu\in\mathcal P(\mathcal Z)}\sup_{0\le t\le T}
 \|\theta_{\mu_{\epsilon,\nu}}(t)-\theta_*(t)
                  -\epsilon\dot\theta_\sigma(t)\|_{\rm raw}
       =o(\epsilon),
 \tag{C.4.7.NV-raw-remainder}
\]

\[
 \sup_{\nu\in\mathcal P(\mathcal Z)}
 \sup_{\substack{0\le t\le T\\x\in\sqrt2S^1}}
 |f_{\mu_{\epsilon,\nu}}(t,x)-f_{\nu_*}(t,x)
                   -\epsilon\mathscr D_\sigma f(t,x)|
       \le\epsilon\omega_Y(\epsilon),
 \qquad \omega_Y(\epsilon)\longrightarrow0,
 \tag{C.4.7.NV-prediction-remainder}
\]

where \(\dot\theta_\sigma\) and \(\mathscr D_\sigma f\) are exactly the
raw variation and prediction response of C.4.6. The modulus is deterministic
and independent of \(\nu\). The proof first turns active query tails into
passive tails using a small probe atom. Radial saturation then controls
the unbounded clock weights on the actual paths. The resulting forcing
continuity and compact response family justify Taylor expansion along
those response directions and a comparison with the nonlinear flow.

###### 1. Probe atoms and passive exponential tails

Write \(U_r=\{\mu:\mathcal W_1(\mu,\nu_*)<r\}\). Choose fixed
\(0<r_0<r_1<\rho\), where \(\rho>0\) is the radius of the preceding
source construction, and ultimately take \(\delta_Y\le r_0\).
The already proved active-tail estimate (C.4.7.NH) supplies \(a,M,h_1>0\) such
that every finite law \(\lambda\in U_{r_1}\), every finite raw Euler
mesh of maximal step at most \(h_1\) through \(T\), and every node \(k\)
obey

\[
 \int \tau_R(Q_{\lambda,k}(u))\,d\lambda(u,y)
       \le M e^{-aR},\qquad
 \tau_R(P):=\|P\mathbf1_{|P|>R}\|_{H_1},\qquad R\ge1.
 \tag{C.4.7.NV-active-tail}
\]

The readout and raw state bounds (C.4.7.NE), and the same-mesh law estimate
(C.4.7.NLM), are uniform on this ball. In particular there are \(C_0,q_0>0\)
and \(\alpha>0\), independent of the mesh, such that

\[
 \max_k\|\theta_{\lambda,k}-\theta_{\kappa,k}\|_{\rm raw}
       \le C_0\mathcal W_1(\lambda,\kappa)^\alpha,
 \qquad \mathcal W_1(\lambda,\kappa)\le q_0.
 \tag{C.4.7.NV-same-mesh}
\]

There is no additive mesh error in this estimate: both recursions use
the identical mesh. This permits probe masses tending to zero at a
fixed mesh.

For completeness, \(Q(u)\) is Lipschitz in raw state on these bounded
sets with their common readout supremum bound. At the same input, factor
subtraction gives

\[
 \begin{aligned}
 \|Z^{(2)}-\bar Z^{(2)}\|_2
 &\le\|K-\bar K\|_{\rm HS}
             +\|\bar A\|\|w-\bar w\|_2,\\
 \|\Delta^{(2)}-\bar\Delta^{(2)}\|_2
 &\le\|c-\bar c\|_2
             +2\|\bar c\|_\infty\|Z^{(2)}-\bar Z^{(2)}\|_2,\\
 \|Q-\bar Q\|_2
 &\le\|K-\bar K\|_{\rm HS}\|\Delta^{(2)}\|_2
             +\|\bar A\|\|\Delta^{(2)}-\bar\Delta^{(2)}\|_2.
 \end{aligned}
 \tag{C.4.7.NV-query-comparison}
\]

Fix \(\lambda\in U_{r_0}\) with finite support and any passive
\(u\in S^1\). The label zero is allowed. Define

\[
 \lambda_\eta=(1-\eta)\lambda+\eta\delta_{(\sqrt2u,0)},
 \qquad
 0<\bar\eta<\min\{1,(r_1-r_0)/D_Y,q_0/D_Y\}.
 \tag{C.4.7.NV-probe-law}
\]

For \(0<\eta\le\bar\eta\), the direct mixture coupling gives
\(\mathcal W_1(\lambda,\lambda_\eta)\le D_Y\eta\), so both laws
are in \(U_{r_1}\). On their common mesh, (C.4.7.NV-same-mesh) and
(C.4.7.NV-query-comparison) give
\(\|Q_{\lambda,k}(u)-Q_{\lambda_\eta,k}(u)\|_2\le C_1\eta^\alpha\).
The selected atom has mass at least \(\eta\), even if it coincides with
an old atom. Hence (C.4.7.NV-active-tail), for \(R\ge2\), gives

\[
 \tau_{R/2}(Q_{\lambda_\eta,k}(u))
       \le\eta^{-1}M e^{-aR/2}.
\]

The pointwise alternatives \( |P'|\le R/2\) and \( |P'|>R/2\)
on \( |P|>R\) imply
\(\tau_R(P)\le2\|P-P'\|_2+2\tau_{R/2}(P')\). Therefore

\[
 \tau_R(Q_{\lambda,k}(u))
       \le2C_1\eta^\alpha+2\eta^{-1}M e^{-aR/2}.
 \tag{C.4.7.NV-probe-tail}
\]

Choose \(\eta=\bar\eta\exp\{-aR/[2(1+\alpha)]\}\) and set
\(b=a\alpha/[2(1+\alpha)]>0\). Both terms have the same exponential
decay, so a fixed \(C_2<\infty\) satisfies

\[
 \sup_{\substack{\lambda\in U_{r_0}\text{ finite}\\
                  \text{admitted meshes},\ k,\ u\in S^1}}
 \tau_R(Q_{\lambda,k}(u))\le C_2e^{-bR},\qquad R\ge2.
 \tag{C.4.7.NV-passive-tail}
\]

There was no division by any preexisting atom weight. The only inverse
mass in (C.4.7.NV-probe-tail) is paid for by the quantitative change of law.

The bound \(\Pr(|Q|>R)\le R^{-2}\tau_R(Q)^2\) and the identity

\[
 \mathbb E e^{\beta|Q|}
       =1+\int_0^\infty\beta e^{\beta R}\Pr(|Q|>R)\,dR
\]

show that \(\beta=b\) gives a common finite exponential moment:
the portion \(0\le R\le2\) is bounded directly, and the remaining
integrand is bounded by a constant times \(e^{-bR}\).
For each \(\mu\in U_{r_0}\), take its finite-law, fine-mesh strong
approximations within \(U_{r_0}\). The readout supremum bound passes
to their strong \(L^2\) limit by an almost surely convergent subsequence.
Equation (C.4.7.NV-query-comparison) then passes each passive query to that
limit in \(L^2\). At any deterministic time use preceding mesh nodes;
the vanishing state interpolation error has the same conclusion.
For each fixed time and input, apply convergence in probability to
\(\min(N,e^{\beta|Q|})\), take expectations using boundedness, then
let \(N\to\infty\). The constants are unchanged for all parameters:

\[
 \sup_{\mu\in U_{r_0},\,0\le t\le T,\,u\in S^1}
           \mathbb E_1 e^{\beta|Q_\mu(t,u)|}\le M_Q<\infty.
 \tag{C.4.7.NV-passive-moment}
\]

This is uniformity of individual query marginals. A coordinate
supremum over time and inputs has not been placed inside this moment.

###### 2. Radial saturation and the actual inverse-gate forcing

The strong raw path has square-integrable velocity in time, so Fubini
gives almost surely absolutely continuous row representatives. Since
\(\cosh^2 z=1+\sinh^2z\ge1+z^2\ge2|z|\),
\(|z|\phi'(z)\le1/2\). The exact row equation consequently gives,
for almost every coordinate and time,

\[
 \frac d{dt}|w_\mu(t)|^2
 =-4\int r_\mu(t,u,y)Q_\mu(t,u)
       (w_\mu(t)\cdot u)\phi'(w_\mu(t)\cdot u)\,d\mu
 \le2\int |r_\mu(t,u,y)|\,|Q_\mu(t,u)|\,d\mu.
 \tag{C.4.7.NV-radial}
\]

The preceding energy identity and \(c(0)=0\) give
\(\|c_\mu(t)\|_2\le Y\sqrt T\), so
\(|r_\mu(t,u,y)|\le R_{\rm rad}:=Y(1+\sqrt T)\). Define

\[
 J_\mu=\int_0^T\int|Q_\mu(s,u)|\,d\mu(u,y)\,ds,
 \qquad W_\mu=\sup_{0\le t\le T}|w_\mu(t)|.
\]

The jointly measurable representatives needed here follow from the
strongly continuous query map and its separable \(L^2\) range; finite
simple approximations give representatives on the product of parameter
space and \(\Omega_1\). Equation (C.4.7.NV-passive-moment) and Fubini give
\(J_\mu<\infty\) almost surely. Integrating (C.4.7.NV-radial) yields

\[
 W_\mu^2\le|g|^2+2R_{\rm rad}J_\mu.
 \tag{C.4.7.NV-row-envelope}
\]

For \(0\le\lambda T\le\beta\), Jensen's inequality for the probability
measure \(T^{-1}\,ds\,d\mu\), followed by (C.4.7.NV-passive-moment), gives

\[
 \mathbb E_1e^{\lambda J_\mu}
 \le\frac1T\int_0^T\int
        \mathbb E_1e^{\lambda T|Q_\mu(s,u)|}\,d\mu\,ds
 \le M_Q.
 \tag{C.4.7.NV-integrated-query}
\]

Choose \(0<\gamma\le\min\{1/8,\beta/(8R_{\rm rad}T)\}\). Cauchy–Schwarz,
(C.4.7.NV-row-envelope), and (C.4.7.NV-integrated-query) imply

\[
 \sup_{\mu\in U_{r_0}}\mathbb E_1e^{\gamma W_\mu^2}
 \le(\mathbb E_1e^{2\gamma|g|^2})^{1/2}
      (\mathbb E_1e^{4\gamma R_{\rm rad}J_\mu})^{1/2}
 \le(1-4\gamma)^{-1/2}M_Q^{1/2}=:M_W<\infty.
 \tag{C.4.7.NV-row-square-moment}
\]

Indeed the two independent standard Gaussian root coordinates give
\(\mathbb E e^{2\gamma|g|^2}=(1-4\gamma)^{-1}\), by combining their
normal densities with the exponential. No independence between \(g\)
and the evolved queries was used.

For every separately fixed positive integer \(p\), the exponential
series in (C.4.7.NV-passive-moment) gives
\(\mathbb E_1|Q_\mu(t,u)|^{2p}\le M_Q(2p)!/\beta^{2p}\).
Since \(\cosh^2(w_j)\le e^{2W_\mu}\) and
\(4pW_\mu\le\gamma W_\mu^2+4p^2/\gamma\), Cauchy–Schwarz gives

\[
 \sup_{\mu\in U_{r_0},\,t\le T,\,u\in S^1,\,j=1,2}
 \mathbb E_1\{\cosh^2(w_{\mu,j}(t))|Q_\mu(t,u)|\}^{p}
 \le e^{2p^2/\gamma}M_W^{1/2}
             \{M_Q(2p)!/\beta^{2p}\}^{1/2}<\infty.
 \tag{C.4.7.NV-weighted-moments}
\]

Define the actual inverse-gate forcing field on \(\Omega_1\) by

\[
 \mathcal I_{\mu,j}(t,u)=
 u_j\cosh^2(w_{\mu,j}(t))\phi'(w_\mu(t)\cdot u)Q_\mu(t,u).
 \tag{C.4.7.NV-clock-force}
\]

The factor \(u_j\) retains the zero contribution at the other reference
axis. Taking \(p=3\) in (C.4.7.NV-weighted-moments) proves a common bound
\(\mathbb E_1|\mathcal I_{\mu,j}(t,u)|^3\le C_3\), hence

\[
 \sup_{\mu\in U_{r_0},\,t\le T,\,u\in S^1,\,j=1,2}
 \mathbb E_1\bigl[|\mathcal I_{\mu,j}(t,u)|^2
                   \mathbf1_{|\mathcal I_{\mu,j}(t,u)|>R}\bigr]
       \le C_3/R\longrightarrow0.
 \tag{C.4.7.NV-forcing-UI}
\]

These estimates concern the actual reached family. They assert no
\(L^p\)-bounded action of \(A_0\) or \(A_0^*\) beyond their given
\(L^2\) actions.

###### 3. The exact clock equation

Set

\[
 F(z)=z/2+\sinh(2z)/4,\qquad \psi=F^{-1},\qquad
 F'(z)=\cosh^2z=1/\phi'(z),\qquad
 \psi'(X)=\phi'(\psi(X)).
 \tag{C.4.7.NV-clock}
\]

The positive derivative and limits at infinity make \(F\) a bijection;
\(\psi\) is 1-Lipschitz, with bounded Lipschitz derivative because
\(\psi''=(\phi''\circ\psi)(\phi'\circ\psi)\) is bounded. Write

\[
 \Theta_\mu=(X_\mu,K_\mu,c_\mu),\qquad
 X_{\mu,j}=F(w_{\mu,j}),\qquad
 \mathcal V=L^2(\Omega_1;\mathbb R^2)
             \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
\]

with its square-sum Hilbert norm. The initial clock is \(F(g_j)\in L^2\):
\(|F(g_j)|\le |g_j|/2+e^{2|g_j|}/4\), and
\(\mathbb E e^{a|g_j|}\le2e^{a^2/2}\) for every finite \(a\ge0\).

The clock is justified without assuming an unbounded coordinate map
preserves all of \(L^2\). Apply the scalar chain rule to the almost
surely absolutely continuous raw row. Its transformed derivative is
\(-2\int r_\mu\mathcal I_{\mu,j}\,d\mu\). The residual bound and
(C.4.7.NV-forcing-UI) make this an integrable \(H_1\)-valued velocity on
\([0,T]\). Fubini and the scalar integral identity therefore identify
\(X_{\mu,j}\) with an absolutely continuous \(H_1\) curve starting at
\(F(g_j)\).

At a clock state \(\Theta=(X,K,c)\), recover \(w_j=\psi(X_j)\) and
the forward and backward fields defined above. For the reference axes put \(r_j=f(e_j)-y_j\),
\(y_1=1,y_2=-1\), and define

\[
 \begin{aligned}
 (\mathcal F_0(\Theta))_{X,j}&=-r_jQ(e_j),\\
 (\mathcal F_0(\Theta))_K
    &=-\sum_{j=1}^2r_j\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j),\\
 (\mathcal F_0(\Theta))_c&=-\sum_{j=1}^2r_jH^{(2)}(e_j).
 \end{aligned}
 \tag{C.4.7.NV-reference-field}
\]

Here \(F'(w_j)\phi'(w_j)=1\) cancels the first gate exactly, and the
two atom masses cancel the loss factor two. For an arbitrary probability
law \(\nu\), define on every reached state

\[
 \mathcal Q_\nu(\Theta)=-2\int r(u,y)
 \left((\mathcal I_j(\Theta,u))_{j=1,2},
       \Delta^{(2)}(u)\otimes H^{(1)}(u),H^{(2)}(u)\right)d\nu(u,y),
 \qquad \mathcal B_\nu=\mathcal Q_\nu-\mathcal F_0.
 \tag{C.4.7.NV-law-field}
\]

For reached states all these Bochner integrals exist: the integrands
have separable measurable ranges. For the first component, truncate its
continuous coordinate formula at a fixed level. The resulting bounded
coordinate map is strongly measurable; (C.4.7.NV-forcing-UI) makes these
truncations converge in \(L^2\), uniformly in the input. Their limit is
therefore strongly measurable and has a uniform \(L^2\) bound. The other
components are strongly continuous in the input and obey the raw bounds.
Integration against a probability law is consequently legitimate.
The exact contamination equation is

\[
 \Theta_{\epsilon,\nu}'=
 \mathcal F_0(\Theta_{\epsilon,\nu})
       +\epsilon\mathcal B_\nu(\Theta_{\epsilon,\nu}),
 \qquad \Theta_{\epsilon,\nu}(0)=\Theta_*(0).
 \tag{C.4.7.NV-exact-equation}
\]

The field \(\mathcal F_0\) is defined on all of \(\mathcal V\).
The contaminated field in (C.4.7.NV-law-field) is used only where its
weighted integrals have just been proved to exist.

###### 4. Reference comparison with one bounded readout endpoint

On sets with bounded \(\|K\|_{\rm HS}\) and \(\|c\|_2\), if at
least one of two compared readouts has a fixed \(L^\infty\) bound, then

\[
 \|\mathcal F_0(\Theta)-\mathcal F_0(\widetilde\Theta)\|_{\mathcal V}
       \le L\|\Theta-\widetilde\Theta\|_{\mathcal V}.
 \tag{C.4.7.NV-reference-Lipschitz}
\]

To verify this, let \(M_A\) bound the two action norms and \(M_c\)
bound the \(L^2\) readout norms, and suppose \(\|c\|_\infty\le H_c\).
Uniformly over \(u\in S^1\),

\[
 \|H^{(1)}-\widetilde H^{(1)}\|_2\le\|X-\widetilde X\|_2,
 \quad
 \|Z^{(2)}-\widetilde Z^{(2)}\|_2
       \le M_A\|X-\widetilde X\|_2+\|K-\widetilde K\|_{\rm HS}.
\]

Use the bounded endpoint in the precise factorization

\[
 c\phi'(Z^{(2)})-\widetilde c\phi'(\widetilde Z^{(2)})
 =(c-\widetilde c)\phi'(\widetilde Z^{(2)})
       +c\{\phi'(Z^{(2)})-\phi'(\widetilde Z^{(2)})\}.
\]

Its norm is at most
\(\|c-\widetilde c\|_2+2H_c\|Z^{(2)}-\widetilde Z^{(2)}\|_2\).
The prediction difference is at most
\(\|c-\widetilde c\|_2+M_c\|Z^{(2)}-\widetilde Z^{(2)}\|_2\).
Actual adjunction then bounds

\[
 \|Q-\widetilde Q\|_2
 \le M_A\|\Delta^{(2)}-\widetilde\Delta^{(2)}\|_2
             +M_c\|K-\widetilde K\|_{\rm HS}.
\]

Substitution into (C.4.7.NV-reference-field), and
\(\|a\otimes b-\tilde a\otimes\tilde b\|_{\rm HS}
\le\|a-\tilde a\|_2\|b\|_2+\|\tilde a\|_2\|b-\tilde b\|_2\),
prove (C.4.7.NV-reference-Lipschitz). Its row component contains no product
of an arbitrary clock difference with an unbounded backward query.

The actual readouts obey \(\|c_\mu(t)\|_\infty\le2YT\), and
(C.4.7.NV-forcing-UI) bounds \(\mathcal B_\nu(\Theta_{\epsilon,\nu})\)
uniformly in \(\nu,\epsilon,t\). Subtract (C.4.7.NV-exact-equation) from
the reference equation. Iterating the scalar integral inequality
\(v(t)\le a+L\int_0^tv(s)ds\) gives \(v(t)\le ae^{Lt}\), so

\[
 \sup_{\nu\in\mathcal P(\mathcal Z),\,t\le T}
       \|\Theta_{\epsilon,\nu}(t)-\Theta_*(t)\|_{\mathcal V}
       \le C_{\rm var}\epsilon.
 \tag{C.4.7.NV-clock-first-order}
\]

This first-order displacement bound is a consequence of the reached
forcing estimates.

###### 5. Continuity of the forcing along the actual paths

We claim

\[
 \sup_{\nu,\,t\le T,\,u\in S^1,\,j=1,2}
 \|\mathcal I_j(\Theta_{\epsilon,\nu}(t),u)
             -\mathcal I_j(\Theta_*(t),u)\|_2\longrightarrow0.
 \tag{C.4.7.NV-force-continuity}
\]

If it failed, choose \(\epsilon_m\downarrow0\), laws \(\nu_m\),
times \(t_m\), and inputs \(u_m\) along which the difference is bounded
away from zero. Pass to a subsequence with \(t_m\to t\), \(u_m\to u\)
and a fixed index \(j\). By (C.4.7.NV-clock-first-order) and reference
continuity, \(\Theta_{\epsilon_m,\nu_m}(t_m)\to\Theta_*(t)\)
strongly in \(\mathcal V\). The lower features converge in \(L^2\),
using \(\psi\)'s Lipschitz bound and
\(\|(u_m-u)\cdot w_*(t)\|_2\le|u_m-u|\|w_*(t)\|_2\).
The action and upper features then converge. The bounded readout
factorization in the preceding subsection gives convergence of
\(\Delta^{(2)}\) and \(Q\) in \(L^2\).

The continuous finite-dimensional function
\(u_j\cosh^2(w_j)\phi'(w\cdot u)\) converges in measure under this
convergence of its arguments. Its product with the convergent query
therefore converges in measure to the limiting \(\mathcal I_j\).
Equation (C.4.7.NV-forcing-UI) upgrades this to \(L^2\) convergence.
Explicitly, uniformly integrable squares make the integral of the
squared difference on any set of sufficiently small probability
uniformly small; on the complement of the event that its magnitude
exceeds \(\eta\), its squared integral is at most \(\eta^2\).
Convergence in measure and then \(\eta\downarrow0\) prove the claim.
The same argument applies to the reference sequence \((t_m,u_m)\);
the triangle inequality contradicts the assumed failure.

Residual differences tend to zero uniformly by
(C.4.7.NV-clock-first-order), while their absolute values and all weighted
force norms are uniformly bounded. The remaining components of
(C.4.7.NV-law-field) have the ordinary Lipschitz differences already proved.
Integration against any probability law is bounded by the supremum
of the integrand norm. Thus

\[
 \sup_{\nu,\,t\le T}
 \|\mathcal B_\nu(\Theta_{\epsilon,\nu}(t))
             -\mathcal B_\nu(\Theta_*(t))\|_{\mathcal V}
       \longrightarrow0.
 \tag{C.4.7.NV-source-defect}
\]

With \(\epsilon=0\), the same argument proves joint strong continuity
of the atom forcing in time, input and label. In particular all
reference law integrals below are continuous in time.

###### 6. The linear equation and its compact family of directions

At a reference clock state and for \(v=(\xi,B,d)\in\mathcal V\), define
the following directional fields; the prefix \(\eta\) denotes a
directional variation, not a time derivative:

\[
 \begin{aligned}
 \eta w_j&=\phi'(w_j)\xi_j,&
 \eta H^{(1)}(u)&=\phi'(w\cdot u)\sum_j u_j\eta w_j,\\
 \eta Z^{(2)}(u)&=A\eta H^{(1)}(u)+BH^{(1)}(u),&
 \eta H^{(2)}(u)&=\phi'(Z^{(2)}(u))\eta Z^{(2)}(u),\\
 \eta f(u)&=\langle d,H^{(2)}(u)\rangle
                      +\langle c,\eta H^{(2)}(u)\rangle,\\
 \eta\Delta^{(2)}(u)&=d\phi'(Z^{(2)}(u))
                  +c\phi''(Z^{(2)}(u))\eta Z^{(2)}(u),\\
 \eta Q(u)&=A^*\eta\Delta^{(2)}(u)+B^*\Delta^{(2)}(u).
 \end{aligned}
 \tag{C.4.7.NV-directional-fields}
\]

The bounded linear generator on \(\mathcal V\) is

\[
 \begin{aligned}
 (\mathcal L(t)v)_{X,j}
   &=-(\eta f(e_j))Q(e_j)-r_j\eta Q(e_j),\\
 (\mathcal L(t)v)_K
   &=-\sum_j\bigl[(\eta f(e_j))\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j)
          +r_j\eta\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j)
          +r_j\Delta^{(2)}(e_j)\otimes\eta H^{(1)}(e_j)\bigr],\\
 (\mathcal L(t)v)_c
   &=-\sum_j\bigl[(\eta f(e_j))H^{(2)}(e_j)+r_j\eta H^{(2)}(e_j)\bigr].
 \end{aligned}
 \tag{C.4.7.NV-generator}
\]

Every map is bounded uniformly in \(t\le T\): the only coefficient
multiplying an unrestricted upper preactivation variation is
\(c\phi''(Z^{(2)})\in L^\infty\). The remaining products are bounded
multipliers, Hilbert scalar pairings, or Hilbert–Schmidt ranks.
In particular no \(Q(e_j)\xi_j\) pointwise product occurs.

The family \(\mathcal L(t)\) is strongly continuous. To justify its
multiplier steps, if uniformly bounded functions converge in measure,
their product with a fixed \(L^2\) field converges in \(L^2\): truncate
the fixed field, use bounded convergence in measure on its bounded
part, and then remove its square-integrable tail. The reference fields
are strongly continuous, their action increments are HS-continuous,
and their readout factors are uniformly bounded. Applying this
observation successively in (C.4.7.NV-directional-fields) and
(C.4.7.NV-generator) proves the assertion for each fixed \(v\).

For clarity, a uniformly bounded strongly continuous generator has a
unique strong propagator \(U(t,s)\) on this finite interval. Starting
from \(v\), iterated integrals of the generator have norms at most
\(\|v\|L_*^k(t-s)^k/k!\), where \(L_*=\sup_t\|\mathcal L(t)\|\).
Their uniformly convergent series solves the integral equation and
has norm at most \(e^{L_*(t-s)}\|v\|\). Iterating the difference
equation proves uniqueness with the same factorial bound.
Consequently the solution of

\[
 v_\sigma'=\mathcal L(t)v_\sigma+b_\sigma(t),\qquad
 b_\sigma(t)=\mathcal B_\nu(\Theta_*(t)),\qquad v_\sigma(0)=0
 \tag{C.4.7.NV-response-equation}
\]

is \(v_\sigma(t)=\int_0^tU(t,s)b_\sigma(s)ds\), and the map from
continuous forcing to \(C([0,T];\mathcal V)\) is bounded and linear,
with norm at most \(Te^{L_*T}\). Substitution into the integral equation
is justified by this integrable bound. The forcing is continuous, so
the response is strongly \(C^1\).

The atom map

\[
 z=(x,y)\longmapsto
 \bigl[t\longmapsto
   \mathcal Q_{\delta_z}(\Theta_*(t))-\mathcal F_0(\Theta_*(t))\bigr]
       \quad\hbox{in }C([0,T];\mathcal V)
 \tag{C.4.7.NV-atom-curves}
\]

is continuous on compact \(\mathcal Z\), by the joint continuity proved above.
Its image is compact. Each \(b_{\nu-\nu_*}\) is a Bochner average of
this image and belongs to its closed convex hull. That hull is compact:
cover the image by finitely many balls of radius \(h\); every convex
combination is within \(h\) of the convex hull of their centers. The
latter hull is the continuous image of a finite-dimensional compact
simplex. This gives total boundedness for each \(h>0\), and closure
in the complete curve space gives compactness.

The bounded linear solution map in (C.4.7.NV-response-equation) therefore gives

\[
 \{v_{\nu-\nu_*}:\nu\in\mathcal P(\mathcal Z)\}
       \text{ has compact closure in }C([0,T];\mathcal V),
 \quad
 \mathcal C:=\overline{\{v_{\nu-\nu_*}(t):\nu\in\mathcal P(\mathcal Z),\ t\le T\}}
       \text{ is compact in }\mathcal V.
 \tag{C.4.7.NV-compact-directions}
\]

The second statement uses continuity of evaluation on the product of
the compact closure of the curve family and compact time.

The equation is exactly the C.4.6 equation, rather than a separately
defined response with an unspecified identification. That section
uses \(X_j^{\rm old}=F(w_j)-F(g_j)\); our clock differs by the same
fixed \(L^2\) initial field for every law. Clock differences and tangent
coordinates thus coincide. At the reference axes
(C.4.7.NV-reference-field) is \(X_j'=-r_jQ(e_j)\), and
(C.4.7.NV-directional-fields) agrees term by term with C.4.6.T14. Formula
(C.4.7.NV-generator) is the product differentiation of this field, hence
the operator in C.4.6.T6. Moreover \(\cosh^2(w_j)=1/\phi'(w_j)\), so

\[
 b_\sigma(t)=-2\int r_*(t,u,y)
 \left(
   \left(u_j\frac{\phi'(w_*(t)\cdot u)}{\phi'(w_{*,j}(t))}
                 Q_*(t,u)\right)_{j=1,2},
   \Delta_*^{(2)}(t,u)\otimes H_*^{(1)}(t,u),H_*^{(2)}(t,u)
 \right)d\sigma(u,y),
 \tag{C.4.7.NV-exact-source}
\]

which is C.4.6.T5 including the residual, sign, factor two and reference
subtraction. Uniqueness of the linear equation identifies \(v_\sigma\)
with that section's response. In particular

\[
 \dot\theta_\sigma(t)=
 ((\phi'(w_{*,j}(t))\xi_{\sigma,j}(t))_{j=1,2},B_\sigma(t),d_\sigma(t)),
 \qquad
 \mathscr D_\sigma f(t,\sqrt2u)=\eta f_*(t,u)[v_\sigma(t)].
 \tag{C.4.7.NV-response-identification}
\]

###### 7. Taylor consistency on compact directions

We first prove the needed \(L^2\) fact. Let \(N\) be a scalar or
finite-dimensional function with bounded Lipschitz first derivative,
and let \(v\) range over a relatively compact subset of \(L^2\). Then

\[
 \sup_{a,v}
 \left\|\frac{N(a+\epsilon v)-N(a)}{\epsilon}-DN(a)v\right\|_2
       \longrightarrow0,
 \tag{C.4.7.NV-compact-Taylor}
\]

where bases \(a\) are arbitrary whenever the expressions are defined.
On \( |v|\le R\), the scalar integral remainder is bounded by
\(C\epsilon R|v|\); on \( |v|>R\), it is bounded by \(C|v|\).
Compact \(L^2\) families have uniformly vanishing square tails.
Indeed a finite \(L^2\) net, and
\(\|v\mathbf1_{|v|>2R}\|_2
\le2\|v-v_0\|_2+2\|v_0\mathbf1_{|v_0|>R}\|_2\),
reduce the claim to finitely many square-integrable fields. Choose
\(R\) first and then \(\epsilon\) to prove (C.4.7.NV-compact-Taylor),
uniformly in the bases. The argument works for a family of functions
with a common derivative bound and Lipschitz constant.

Apply it to \(\psi\), to the finite-dimensional map
\(X\mapsto\phi(\sum_j u_j\psi(X_j))\), and to \(\phi\) and
\(\phi'\) at the upper preactivation. Their first derivatives are
bounded and Lipschitz uniformly over \(u\in S^1\); for the second
map use \( |u|=1\), bounded \(\psi',\psi''\), and bounded
\(\phi',\phi''\). The needed further derivatives of tanh are bounded.

At compact reference times and for \(v\in\mathcal C\), the linear
directions in (C.4.7.NV-directional-fields) form compact \(L^2\) families,
also when \(u\) varies over the circle. To check this, the bounded
multiplier argument from the preceding subsection gives joint strong
continuity in \((t,u)\) on each fixed direction. Uniform operator bounds
and a finite net extend that continuity to compact direction sets.
The action \(A(t)\) is norm-continuous because \(K(t)\) is HS-continuous.
For \(BH^{(1)}(t,u)\), continuity follows from the HS action bound.
Thus every successive linear image is the continuous image of the
relevant compact parameter product.

These facts expand the lower and upper features with precisely the
linear terms in (C.4.7.NV-directional-fields), with \(o(\epsilon)\) errors
uniform in \(t,u,v\in\mathcal C\). Bilinear action terms such as
\(\epsilon B[H^{(1)}_{\rm new}-H^{(1)}_*]\) are \(O(\epsilon^2)\)
in \(L^2\). If the upper preactivation already has an \(o(\epsilon)\)
error after its linear term, the Lipschitz bounds for \(\phi,\phi'\)
pass that error before applying (C.4.7.NV-compact-Taylor).

There is one pointwise product requiring a further check. In the
expansion of \((c_*+\epsilon d)\phi'(Z^{(2)}_{\rm new})\), the cross
term divided by \(\epsilon\) is

\[
 d\{\phi'(Z^{(2)}_{\rm new})-\phi'(Z^{(2)}_*)\}.
 \tag{C.4.7.NV-backward-cross-term}
\]

The bracket is uniformly bounded and has \(L^2\) norm \(O(\epsilon)\).
For any fixed \(R\), its product with \(d\mathbf1_{|d|\le R}\)
therefore tends uniformly to zero in \(L^2\). The complementary norm
is at most \(2\|\phi'\|_\infty\|d\mathbf1_{|d|>R}\|_2\),
uniformly small by compactness of the \(d\) directions. This proves
that (C.4.7.NV-backward-cross-term) is \(o(1)\) in \(L^2\). The other upper
backward Taylor remainder is multiplied by the bounded reference
readout. After actual adjunction, the remaining action cross term is
bounded by \(\epsilon\|B\|_{\rm HS}\) times an \(O(\epsilon)\)
backward difference. Prediction products are scalar pairings and
middle-field products are Hilbert–Schmidt ranks; their cross terms
are \(O(\epsilon^2)\) by Cauchy–Schwarz and the rank norm identity.
Residual differences have the same scalar expansion.

Substitution of these expansions into every component of
(C.4.7.NV-reference-field) proves

\[
 \sup_{t\le T,\,v\in\mathcal C}
 \|\mathcal F_0(\Theta_*(t)+\epsilon v)
       -\mathcal F_0(\Theta_*(t))-\epsilon\mathcal L(t)v\|_{\mathcal V}
       =o(\epsilon).
 \tag{C.4.7.NV-field-Taylor}
\]

The same expansions of \(\psi\) and the scalar predictor prove their
corresponding \(o(\epsilon)\) formulas, including the supremum over
all \(u\in S^1\). These are Taylor estimates on compact directions;
no estimate on an arbitrary bounded \(L^2\) direction ball is claimed.

###### 8. Comparison with the nonlinear path and return to raw state

Let \(\widetilde\Theta_{\epsilon,\nu}=
\Theta_*+\epsilon v_{\nu-\nu_*}\), and define

\[
 \rho_{\epsilon,\nu}(t)=
 \mathcal F_0(\widetilde\Theta_{\epsilon,\nu}(t))
       -\mathcal F_0(\Theta_*(t))-\epsilon\mathcal L(t)v_{\nu-\nu_*}(t).
\]

Equations (C.4.7.NV-compact-directions) and (C.4.7.NV-field-Taylor) give
\(\sup_{\nu,t}\|\rho_{\epsilon,\nu}(t)\|=o(\epsilon)\).
Subtracting the response equation from (C.4.7.NV-exact-equation), with
\(e=\Theta_{\epsilon,\nu}-\widetilde\Theta_{\epsilon,\nu}\), yields

\[
 \begin{aligned}
 e'={}&\mathcal F_0(\Theta_{\epsilon,\nu})
           -\mathcal F_0(\widetilde\Theta_{\epsilon,\nu})\\
 &+\epsilon\{\mathcal B_\nu(\Theta_{\epsilon,\nu})
                  -\mathcal B_\nu(\Theta_*)\}
       +\rho_{\epsilon,\nu},\qquad e(0)=0.
 \end{aligned}
 \tag{C.4.7.NV-error-equation}
\]

Both compared curves have uniformly bounded action and \(L^2\)
readout norms, by the raw estimates and compactness of the response
family. The actual curve has the uniform pointwise readout bound
\(2YT\). Thus (C.4.7.NV-reference-Lipschitz) applies although the response
readout need not be bounded pointwise. Equations (C.4.7.NV-source-defect)
and (C.4.7.NV-error-equation), followed by the scalar integral inequality,
give

\[
 \sup_{\nu,t\le T}
 \|\Theta_{\epsilon,\nu}(t)-\Theta_*(t)
                         -\epsilon v_{\nu-\nu_*}(t)\|_{\mathcal V}
       =o(\epsilon).
 \tag{C.4.7.NV-clock-remainder}
\]

For the raw row, first replace \(X_{\epsilon,\nu}\) by
\(X_*+\epsilon\xi_\sigma\), at an \(o(\epsilon)\) cost because
\(\psi\) is 1-Lipschitz. Then (C.4.7.NV-compact-Taylor) gives

\[
 \psi(X_*+\epsilon\xi_\sigma)-\psi(X_*)
       =\epsilon\phi'(w_*)\xi_\sigma+o(\epsilon)
       \quad\text{in }L^2,
\]

uniformly in \(\nu,t\). The other raw blocks equal their clock-state
blocks, proving (C.4.7.NV-raw-remainder) with (C.4.7.NV-response-identification).
The predictor is uniformly Lipschitz in clock state on these bounded
sets, by the forward and pairing bounds used above. Replace the actual
state by \(\widetilde\Theta_{\epsilon,\nu}\) and apply its uniform
compact-direction Taylor formula. This proves
(C.4.7.NV-prediction-remainder). A deterministic modulus can be obtained by
taking the supremum of the normalized error over \(\nu,t,u\) and
\(0<\epsilon'\le\epsilon\), and defining its value at zero to be zero.
The just-proved uniform small-o makes this supremum finite for small
\(\epsilon\) and tending to zero; uniform state and response bounds
extend it to the rest of \(0<\epsilon\le\epsilon_Y\).

###### 9. Exact bridge to finite GF

For each width retain the actual three initialized Gaussian arrays,
including the small stored readout, and use those same arrays for
every \(\epsilon\). At fixed width the exactly integrated finite loss
has a smooth parameter field, affine in \(\epsilon\). The finite
energy bound keeps all paths \(0\le\epsilon\le1\) in one compact
parameter ball on \([0,T]\), whose radius may depend on that initialized
network. On this ball the mean value formula and the scalar integral
inequality first give \(\|\theta_{n,\epsilon}-\theta_{n,0}\|_{C_t}
\le C_n\epsilon\). Dividing the integral-equation difference by
\(\epsilon\), its mean-value coefficients converge uniformly to the
reference derivative coefficients. A second integral comparison gives
the right derivative \(D_\sigma f_n\), with zero initial variation.
This is the finite derivative constructed in C.4.6.4; no width-uniform
constant is used in its construction.

Fix \(\nu\in\mathcal P(\mathcal Z)\) and \(\epsilon\in(0,\epsilon_Y]\).
Write \(\|\cdot\|_\infty\) for the supremum over
\([0,T]\times\sqrt2S^1\). The exact triangle inequality is

\[
 \begin{aligned}
 \frac{\|f_{n,\mu_{\epsilon,\nu}}-f_{n,\nu_*}
                           -\epsilon D_\sigma f_n\|_\infty}{\epsilon}
 \le{}&\omega_Y(\epsilon)\\
 &+\frac{\|f_{n,\mu_{\epsilon,\nu}}-f_{\mu_{\epsilon,\nu}}\|_\infty
            +\|f_{n,\nu_*}-f_{\nu_*}\|_\infty}{\epsilon}\\
 &+\|D_\sigma f_n-\mathscr D_\sigma f\|_\infty.
 \end{aligned}
 \tag{C.4.7.NV-finite-triangle}
\]

At this fixed positive \(\epsilon\), the two prediction errors vanish
in probability by the finite capture established above, since both
laws lie in its neighborhood. The last error vanishes in probability
by C.4.6.T10 with exactly this fixed \(\nu\), this physical horizon,
and the same Gaussian initialization. A finite union bound suffices;
independence of the three errors is unnecessary. For any \(a>0\),
choose \(\epsilon\) small enough that \(\omega_Y(\epsilon)<a/2\),
then take width to infinity at that fixed \(\epsilon\). This proves

\[
 \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
 \Pr\left[
 \frac{\displaystyle
  \sup_{\substack{0\le t\le40\\x\in\sqrt2S^1}}
  |f_{n,\mu_{\epsilon,\nu}}(t,x)-f_{n,\nu_*}(t,x)
                            -\epsilon D_\sigma f_n(t,x)|}{\epsilon}
       >a\right]=0
 \quad\text{for every fixed }\nu\in\mathcal P(\mathcal Z),\ a>0.
 \tag{C.4.7.NV-finite-nonlinear-limit}
\]

The population remainder is uniform over contaminating laws. The finite
statement fixes the law before its probability limit and takes width
before the contamination limit. It gives no uniform finite-width
remainder, no joint rate for \(\epsilon\) and width, and no supremum
over laws of finite failure probabilities. All conclusions concern
physical GF through \(40\), with the stated initialization and exact
Borel-law loss; they assert neither a raw-GD variation theorem nor an
ambient \(L^2\) Fréchet derivative or a quadratic nonlinear remainder.

##### C.4.7.7. Inherited risk and paired hidden activity

On the binary-label subclass and the intersection with the C.4.5 ball
\(\mathcal W_1(\mu,\nu_*)<\exp\{-\exp(3000)\}\), the new population
flow has risk at time40 at most \(1/4\), and both training-averaged
paired squared hidden displacements at time \(1/200\) at least
\(10^{-13}\). These are the existing subclass and times, now attached
to the constructed changed-law population trajectories.

Indeed the complete comparison in C.4.5.3 applies to actual finite GF
with zero discretization defect and gives its strict margins. If f,g
are uniformly bounded in absolute value by B, then
\[
 |\mathcal L_\mu(f)-\mathcal L_\mu(g)|
                  \le2(B+Y)\|f-g\|_\infty.
\]
The fixed-state loss integrand is Lipschitz in the joint normalized
input/label metric, with constant
\(2(B+Y)\max\{\operatorname{Lip}f,1\}\). Thus (C.4.7.NW1)–(C.4.7.NW2) pass
the finite risks to the population risk, including the empirical-law
limit. For a hidden field bounded by one, keeping the same initialized
field in each comparison gives
\[
 \left|\|H-H_0\|_2^2-\|\bar H-H_0\|_2^2\right|
                           \le4\|H-\bar H\|_2.
\]
The paired observation contract retains \(H,H_0\) jointly on their
own carrier; its fixed-program limit identifies the displayed norms.
Uniform input continuity passes their training-law integrals. This
therefore passes the strict finite hidden-activity margins as well.

The new nonlinear theorem concerns the one physical GF interval
\([0,40]\). It gives no all-time changed-law dynamics, endpoint selection
or continuity, universal fitting, activity for every bounded-label law,
activity at time40, or comparison with frozen-feature learning. It does
not extend the earlier raw-GD theorem to this interval. The neighborhood
radius is positive but has no claimed useful numerical size. The
population remainder is uniform over contamination laws; the finite
nonlinear statement takes width first for each fixed contamination law
and fixed positive epsilon, and asserts no simultaneous epsilon/width
rate or uniform finite failure probability over all laws.


#### C.4.8. Sampling fluctuations of the trained prediction

Unqualified equation labels below belong to this proof unit. The finite-source and statistical lemmas state their local notation explicitly.

##### Model and theorem


Use exactly the population carrier, initialization, and physical gradient flow
of C.4.7. Write \(u=x/\sqrt2\), \(\phi=\tanh\), and
\(\theta=(w,K,c)\), with \(A=A_0+K\). The retained fields are
\[
 h_\theta(u)=\phi(w\cdot u),\quad Z_\theta(u)=Ah_\theta(u),\quad
 b_\theta(u)=\phi(Z_\theta(u)),\quad
 \Delta_\theta(u)=c\phi'(Z_\theta(u)),\quad Q_\theta(u)=A^*\Delta_\theta(u),
 \quad f_\theta(u)=\langle c,b_\theta(u)\rangle.
\]
For \(r_\theta(u,y)=f_\theta(u)-y\), the actual population equation is
\[
 \dot\theta=-2\int r_\theta(u,y)
 \bigl(\phi'(w\cdot u)Q_\theta(u)u,
             \Delta_\theta(u)\otimes h_\theta(u),b_\theta(u)\bigr)
 \,d\mu(u,y),\qquad \theta(0)=(g,0,0).                 \tag{C.4.8.P1}
\]
The first state component is the full two-dimensional first row, the second
is the learned Hilbert--Schmidt middle increment, and the third is the trained
readout. The initialized Gaussian action and its actual adjoint in (C.4.8.P1) are
the common prescribed construction, not arbitrary operators with the same
norm. The zero population initial readout is its width limit. At finite width
the actual independent Gaussian stored readout is retained throughout.
Population predictions are deterministic expectations on this prescribed
carrier; no additional random environment is left outside those expectations.

The finite networks have two equal-width bias-free tanh hidden layers, output
divided by \(n\), independent centered Gaussian stored variances
\((1,1/n,1/n^2)\), mobilities \((n,1,n)\), and unhalved squared loss integrated
against the labeled training law. No initialization is reset when laws change.

Fix \(Y\ge1\), \(T=40\), the data space and its metric
\[
 \mathcal Z=\sqrt2S^1\times[-Y,Y],\qquad
 d_{\mathcal Z}((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|,
\]
and \(\nu_*=\tfrac12\delta_{(\sqrt2e_1,1)}+
\tfrac12\delta_{(\sqrt2e_2,-1)}\). Let \(\delta_Y\) be the C.4.7 radius,
\(U_Y=\{\mu:W_1(\mu,\nu_*)<\delta_Y\}\). Its construction chooses this
radius inside the neighborhood with uniform finite-Euler source caps.
Let \(\rho\) be normalized circle arc length,
\(H=L^2(\sqrt2S^1,\rho;\mathbb R)\), and
\(F(\mu)=f_\mu(T,\cdot)\). We also use the stronger output space
\(\mathcal C=C(\sqrt2S^1;\mathbb R)\) with its supremum norm.

Set \(\delta'_Y=\delta_Y/4\). For every separately fixed Borel law
\(\mu\) with \(W_1(\mu,\nu_*)<\delta'_Y\), the following conclusions hold:
there is a bounded continuous \(\mathcal C\)-valued atom response
\(I_\mu(z)\), given by the full source recursion below, such that
\[
 I_\mu(z)=\lim_{\epsilon\downarrow0}
 \frac{F((1-\epsilon)\mu+\epsilon\delta_z)-F(\mu)}{\epsilon},
 \qquad \int I_\mu(z)\,d\mu(z)=0.                       \tag{C.4.8.P2}
\]
The derivative holds in \(\mathcal C\), hence in \(H\), for every \(z\).
For iid observations with empirical law \(\mu_m\), define the bounded
measurable extension
\[
 \overline F(Q)=F(Q)\quad(Q\in U_Y),\qquad
 \overline F(Q)=0\quad(Q\notin U_Y).                    \tag{C.4.8.P3}
\]
Then, with \(r_m=\overline F(\mu_m)-F(\mu)-m^{-1}\sum_i I_\mu(Z_i)\),
\[
 m\,\mathbb E\|r_m\|_H^2\longrightarrow0.              \tag{C.4.8.P4}
\]
In particular \(\sqrt m\,r_m\to0\) in probability. Its covariance and
whole-function limit are
\[
 \Sigma_\mu v=\int\langle I_\mu(z),v\rangle_H I_\mu(z)\,d\mu(z),
 \qquad \sqrt m\,[\overline F(\mu_m)-F(\mu)]
                  \Rightarrow\mathcal N_H(0,\Sigma_\mu).              \tag{C.4.8.P5}
\]
The finite-network conclusion is the width-first assertion
\[
 \lim_{m\to\infty}\limsup_{n\to\infty}
 d_{\rm BL}\!\left(\operatorname{Law}\!\left[
 \sqrt m\,(f_{n,\mu_m}(T,\cdot)-F(\mu))\right],
                  \mathcal N_H(0,\Sigma_\mu)\right)=0,                \tag{C.4.8.P6}
\]
where sampling and initialization are independent and both are included in
the law. Here bounded-Lipschitz tests have absolute value and Lipschitz constant
at most one. No simultaneous width/sample rate is asserted.

##### C.4.8.1. Uniform first and second finite-program responses


Fix \(Y\ge1\), \(T=40\), and the two-hidden-layer tanh model, initialization,
loss normalization and Gaussian action spaces of C.4.7. Choose a fixed smaller
law ball whose closure is contained in the neighborhood of C.4.7.N-cap.
All constants below may depend on this choice, \(Y,T\), and a separately
specified source-derivative or moment order. They do not depend on the number
of atoms, their minimum positive mass, covariance rank, or the number of
Euler steps. Only finitely many low-order moment constants will determine
the step threshold in the conclusion.

Let
\[
 \lambda=\sum_{a=1}^N p_a\delta_{(\sqrt2u_a,y_a)},\qquad
 p_a>0,\quad\sum_ap_a=1,\quad |u_a|=1,\quad |y_a|\le Y,
\]
and let \(f_h(\lambda;t,u)\) denote the prediction of its population raw
Euler program, using its actual population residuals, through time
\(t\le T\). The program may end in a shorter final step. A mass direction
\(\sigma=(s_a)_{a=1}^N\) has \(\sum_as_a=0\) and norm
\(\|\sigma\|_{\rm TV}=\sum_a|s_a|\). Inputs and labels remain fixed when
taking these derivatives. A second direction is denoted \(\tau=(v_a)\).

**Lemma.** There are \(h_*>0\) and \(C<\infty\) such that every program in
this ball with maximum step at most \(h_*\) satisfies
\[
 \sup_{t\le T,\,u\in S^1}
       |\partial_\sigma f_h(\lambda;t,u)|
       \le C\|\sigma\|_{\rm TV},
 \qquad
 \sup_{t\le T,\,u\in S^1}
       |\partial_\sigma\partial_\tau f_h(\lambda;t,u)|
       \le C\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}.             \tag{C.4.8.S1}
\]
On positive masses these are ordinary derivatives on the relative open
probability simplex intersected with the law ball. They extend continuously
to one-sided derivatives on admissible finite-law segments and rectangles
at zero masses. No nonsingularity of a Gaussian covariance is required.
The same bounds hold for the prediction in \(L^2(S^1)\) with normalized
circle measure.

The proof retains both Gaussian source orientations and the response
corrections representing the actual initialized action and its adjoint.
It first bounds source derivatives with deterministic coefficients frozen,
then differentiates the full coefficient and covariance recursions. Short
time intervals supply an absorbable factor for the latter derivatives.

###### 1. Exact finite source recursion and its uniform bounds

Write \(\phi=\tanh\), \(A=A_0+K\), with \(A_0:H_1\to H_2\) and its actual
Hilbert adjoint on the canonical spaces of III.F. The initial state is
\((w_0,K_0,c_0)=(g,0,0)\), with \(g\sim N(0,I_2)\). Only \(K\) is
Hilbert–Schmidt. At a time node \(k\), abbreviate the fields by
\[
 H_{ku}=\phi(w_k\cdot u),\quad Z_{ku}=A_kH_{ku},\quad
 \Delta_{ku}=c_k\phi'(Z_{ku}),\quad Q_{ku}=A_k^*\Delta_{ku},
 \quad f_{ku}=\mathbb E_2[c_k\phi(Z_{ku})],
\]
and put \(r_{ka}=f_{ku_a}-y_a\). For a step \(h_k>0\), set
\(m_{ka}=h_kp_a\) and \(\gamma_{ka}=-2m_{ka}r_{ka}\). The exact Euler updates
are
\[
 \begin{aligned}
 w_{k+1}&=w_k+\sum_a\gamma_{ka}\phi'(w_k\cdot u_a)Q_{ka}u_a,\\
 c_{k+1}&=c_k+\sum_a\gamma_{ka}\phi(Z_{ka}),\\
 K_{k+1}&=K_k+\sum_a\gamma_{ka}\Delta_{ka}\otimes H_{ka}.
 \end{aligned}                                                   \tag{C.4.8.S2}
\]
Here \(a\otimes b\) acts as \(v\mapsto a\mathbb E_1[bv]\).

A source slot is \(i=(k,a)\), or one distinguished current slot \(i=(k,u)\)
for an appended passive query. The notation \(q<i\) means that the time
index of \(q\) is strictly smaller than \(k\). A sum \(q\le i\) includes
the old training slots and the distinguished current slot; other current
slots have zero response coefficient for this output. Earlier unused
passive slots also have coefficient zero. Let \(\xi_i\) be the centered
forward Gaussian source on population 2 and \(\zeta_i\) the centered reverse
Gaussian source on population 1. Their source covariances are
\[
 (C_\xi)_{ij}=\mathbb E_1[H_iH_j],\qquad
 (C_\zeta)_{ij}=\mathbb E_2[\Delta_i\Delta_j].                  \tag{C.4.8.S3}
\]
The two orientation families are independent; the lower root \(g\) has its
fixed independent Gaussian law. These are the source families of the
retained action construction in III.F and C.4.7, not independent replacements
for \(A_0\) and \(A_0^*\).

The coordinate derivatives in the next display freeze all residuals,
contractions, covariance laws and deterministic coefficients. On the full
Euclidean space of named source coordinates define
\[
 \alpha_{i,q}=\mathbb E_1[\partial_{\zeta_q}H_i]\quad(q<i),
 \qquad
 \beta_{i,q}=\mathbb E_2[\partial_{\xi_q}\Delta_i]\quad(q\le i).
\]
The exact source representation is
\[
 \begin{aligned}
 F_{i,q}&=\alpha_{i,q}+\gamma_q(C_\xi)_{iq}\quad(q<i),\\
 D_{i,q}&=\beta_{i,q}+\mathbf1_{q<i}\gamma_q(C_\zeta)_{iq},\\
 Z_i&=\xi_i+\sum_{q<i}F_{i,q}\Delta_q,\\
 Q_i&=\zeta_i+\sum_{q\le i}D_{i,q}H_q.
 \end{aligned}                                                   \tag{C.4.8.S4}
\]
In particular
\[
 \beta_{i,i}=\mathbb E_2[c_k\phi''(Z_i)],                       \tag{C.4.8.S5}
\]
and all other current coefficients are zero, including for duplicated
queries. The slots retain their names even if their Gaussian covariance
has rank zero or two slots agree almost surely. Thus a named derivative
means the derivative of the prescribed coordinate expression, not a
derivative reconstructed from its values on a singular Gaussian support.

For completeness, the first frozen-source equations following from
(C.4.8.S2)–(C.4.8.S4) are as follows. For a reverse pulse \(p\), put
\(v_{k;p}=\partial_{\zeta_p}w_k\), which vanishes up to its injection step.
Then
\[
 \begin{aligned}
 v_{k+1;p}=v_{k;p}+\sum_a\gamma_{ka}u_a\bigg[
 &\phi''(w_k\cdot u_a)Q_{ka}(u_a\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_a)
   \bigg\{\mathbf1_{(k,a)=p}
       +\sum_{q\le(k,a)}D_{ka,q}\phi'(w_{t(q)}\cdot u_q)
                          (u_q\cdot v_{t(q);p})\bigg\}\bigg].
 \end{aligned}                                                   \tag{C.4.8.S6}
\]
For a forward pulse \(p\), put
\(U_{i;p}=\partial_{\xi_p}Z_i\),
\(c_{k;p}=\partial_{\xi_p}c_k\),
\(V_{i;p}=\partial_{\xi_p}\Delta_i\). Their equations are
\[
 \begin{aligned}
 c_{k;p}&=\sum_{q<k}\gamma_q\phi'(Z_q)U_{q;p},\\
 U_{i;p}&=\mathbf1_{i=p}+\sum_{q<i}F_{i,q}V_{q;p},\\
 V_{i;p}&=\phi'(Z_i)c_{k;p}+c_k\phi''(Z_i)U_{i;p}.
 \end{aligned}                                                   \tag{C.4.8.S7}
\]
Equations (C.4.8.S2)–(C.4.8.S7) restate C.4.7.N2–N8 with local notation.

C.4.7.N-cap and N9–N17 give constants \(C_0,R_0,D_0,f_0<\infty\) such that
\[
 \|c_k\|_\infty\le C_0,\quad |r_{ka}|\le R_0,\quad
 |\gamma_{ka}|\le2R_0h_kp_a,\quad
 \sum_q|D_{i,q}|\le D_0,\quad |F_{i,(s,a)}|\le f_0h_sp_a.    \tag{C.4.8.S8}
\]
The D row bound is valid at every passive input. In particular
\[
 Q_i=\zeta_i+J_i,\qquad |J_i|\le D_0,
 \qquad \mathbb E_1\zeta_i^2\le C_0^2.                        \tag{C.4.8.S9}
\]
Write \(q_k=\sum_ap_a|Q_{ka}|\) and \(J=\sum_kh_kq_k\). For every fixed
\(a\ge0\), Jensen's inequality with weights \(h_kp_a/T\), adding a zero
term if the total time is smaller than \(T\), and the scalar Gaussian
exponential moment give
\[
 \mathbb E_1e^{aJ}
       \le2\exp\{aTD_0+a^2T^2C_0^2/2\}.                     \tag{C.4.8.S10}
\]
No independence across times or query inputs is used. Each individual Q
has every finite moment uniformly. The same is true of Z by (C.4.8.S4),
(C.4.8.S8), bounded Delta, and its forward Gaussian of variance at most one.
The raw update and Gaussian root moments also give all finite moments
of \(\max_k|w_k|\).

###### 2. All fixed orders of frozen source derivatives

For a vector-valued coordinate expression \(V\), use its Euclidean norm
inside
\[
 J_j(V)=\sum_{p_1,...,p_j}|\partial_{p_1}\cdots\partial_{p_j}V|
       \quad(j\ge1),\qquad J_0(V)=|V|.                        \tag{C.4.8.S11}
\]
The finite source list can be enlarged with unused coordinates, whose
derivatives are zero. The product and scalar composition inequalities are
\[
 J_j(UV)\le\sum_{r=0}^j{j\choose r}J_r(U)J_{j-r}(V),
\]
\[
 J_j(a(V))\le\sum_{\pi\in\mathfrak P_j}
       \|a^{(|\pi|)}\|_\infty\prod_{B\in\pi}J_{|B|}(V),     \tag{C.4.8.S12}
\]
where \(\mathfrak P_j\) denotes the partitions of \(\{1,...,j\}\).
To verify the second formula, differentiate successively and group the
indices that differentiate the same factor; summing absolute values over
all source indices factors each product into the displayed product of
sums. For a linear projection \(w\cdot u\), every \(J_j\) is at most
\(J_j(w)\) when \(|u|=1\).

For every fixed \(j\ge1\) and finite \(p\ge1\),
\[
 \left\|\max_kJ_j(w_k)\right\|_p+
      \sup_{k,u}\|J_j(H_{ku})\|_p+
      \sup_{k,u}\|J_j(Q_{ku})\|_p\le C_{j,p},                \tag{C.4.8.S13}
\]
and each of \(J_j(c_k),J_j(Z_{ku}),J_j(\Delta_{ku})\) and
\(J_j(\phi(Z_{ku}))\) is bounded pointwise by \(C_j\), uniformly over its
node and input. The pointwise statement means that the bound holds for
every coordinate expression, for all its Gaussian source values. It
requires no jointly continuous version of a passive Gaussian process.

Here is an induction proving these assertions at every fixed order. Put
\(S_j(k)=\max_{l\le k}J_j(w_l)\). The one-block partition in (C.4.8.S12) is the
only term containing \(S_j\), so
\[
 J_j(H_{lu})\le S_j(k)+P_j(S_1(k),...,S_{j-1}(k)),\quad l\le k,
\]
where \(P_j\) is a fixed polynomial with nonnegative coefficients and
\(P_1=0\). It follows from (C.4.8.S4) that
\[
 J_j(Q_{ka})\le\mathbf1_{j=1}
        +D_0\{S_j(k)+P_j(S_1(k),...,S_{j-1}(k))\}.
\]
The two highest-order terms in a derivative of
\(\phi'(w_k\cdot u_a)Q_{ka}\) are bounded by
\((D_0+2|Q_{ka}|)S_j(k)\). Every other term uses lower orders, with a
factor bounded by a constant times \(1+D_0+|Q_{ka}|\). Thus
\[
 S_j(k+1)\le[1+h_k(2R_0D_0+4R_0q_k)]S_j(k)
 +C_jh_k(1+D_0+q_k)P_j^+(S_1(k),...,S_{j-1}(k)).             \tag{C.4.8.S14}
\]
The polynomial \(P_j^+\) may include a constant. At order one the
inhomogeneous term is \(2R_0h_k\). All initial source derivatives vanish.
With
\[
 \mathcal A=2R_0D_0T+4R_0J,
\]
iteration using \(\prod(1+x_i)\le e^{\sum x_i}\) gives
\[
 \max_k S_1(k)\le2R_0Te^{\mathcal A},
\]
\[
 \max_kS_j(k)\le C_je^{\mathcal A}((1+D_0)T+J)
                  P_j^+(\max_kS_1(k),...,\max_kS_{j-1}(k)). \tag{C.4.8.S15}
\]
Equation (C.4.8.S10), induction on \(j\), and Holder's inequality prove all
finite moments in (C.4.8.S15), and hence (C.4.8.S13). This also shows that the lower
feature jets, uniformly in input, have a common pointwise envelope with
every finite moment.

For the upper population, let \(U_j(k)\) be the maximum of
\(J_j(Z_{lu})\) over nodes \(l\le k\) and the query under consideration.
By (C.4.8.S4) and the time/atom density of F,
\[
 J_j(Z_{ku})\le\mathbf1_{j=1}
              +f_0\sum_{s<k}h_s\max_aJ_j(\Delta_{sa}).      \tag{C.4.8.S16}
\]
The highest terms in c and Delta are
\[
 J_j(c_k)\le2R_0\sum_{s<k}h_s
                    [\max_aJ_j(Z_{sa})+P_j^c],
\]
\[
 J_j(\Delta_{ku})\le J_j(c_k)+2C_0J_j(Z_{ku})+P_j^\Delta.
                                                                    \tag{C.4.8.S17}
\]
The polynomials in (C.4.8.S17) use only smaller positive derivative orders and
are pointwise bounded by induction. Inserting (C.4.8.S17) into (C.4.8.S16), and
bounding the double time sum by \(T\) times its single sum, gives
\[
 U_j(k)\le C_j+f_0(2R_0T+2C_0)\sum_{s<k}h_sU_j(s).
\]
Iteration of this scalar inequality bounds it by a finite exponential
series, uniformly in the mesh. Equation (C.4.8.S17) and then (C.4.8.S12) prove all
the other upper assertions. In particular the proof never assigns a
product of masses to repeated old source derivatives: the derivative of
\(h_sp_a\phi(\xi_{sa})\) of any order still has only one factor \(h_sp_a\).

We also need derivatives of lower increments. If \(b\le k\) and
\(\sum_{l=b}^{k-1}h_l\le\ell\), then for every fixed \(j\ge0,p<\infty\),
\[
 \|J_j(w_k-w_b)\|_p+
       \sup_u\|J_j(H_{ku}-H_{bu})\|_p\le C_{j,p}\ell.       \tag{C.4.8.S18}
\]
For w, sum the differentiated updates (C.4.8.S2). Each summand without its
\(h_lp_a\) factor has bounded \(L^p\) norm by (C.4.8.S12)–(C.4.8.S13), (C.4.8.S9), and
Holder. Minkowski costs only \(\sum h_lp_a\le\ell\). For H use
\[
 H_{ku}-H_{bu}=\int_0^1
 \phi'((w_b+v(w_k-w_b))\cdot u)((w_k-w_b)\cdot u)\,dv.
\]
After any fixed number of source derivatives every term contains a jet of
\(w_k-w_b\). The remaining factors are bounded gates and base jets at the
two endpoints. Holder at larger finite moment orders proves (C.4.8.S18).
The estimates also hold for the maximum over k within this interval:
the differentiated sum of absolute update terms bounds that maximum.

For a product \(H_iH_j\), replace every endpoint with time at least b by
\(H_{bu}\) at the same input and retain earlier endpoints. The resulting
boundary product depends only on reverse slots with time strictly below b.
Its difference from \(H_iH_j\) satisfies (C.4.8.S18) at each fixed jet order,
by product subtraction and (C.4.8.S12).

###### 3. Gaussian differentiation at singular covariance

Let \(C(a,b)\) be a twice continuously differentiable positive semidefinite
matrix family on a parameter rectangle, with one-sided derivatives allowed
at its boundary. Let \(G(a,b,x)\) have continuous derivatives twice in
parameters and four times in x, including the mixed derivatives displayed
below. Assume they have a common polynomial growth bound on compact
parameter sets. With \(X\sim N(0,C)\), write \(M=\mathbb E G(a,b,X)\).
Then
\[
 M_a=\mathbb E G_a+\frac12\sum_{ij}C_{a,ij}\mathbb E G_{ij},\tag{C.4.8.S19}
\]
\[
 \begin{aligned}
 M_{ab}={}&\mathbb E G_{ab}
   +\tfrac12\sum_{ij}C_{ab,ij}\mathbb E G_{ij}\\
 &+\tfrac12\sum_{ij}C_{a,ij}\mathbb E G_{bij}
  +\tfrac12\sum_{ij}C_{b,ij}\mathbb E G_{aij}\\
 &+\tfrac14\sum_{ij,lr}C_{a,ij}C_{b,lr}\mathbb E G_{ijlr}.
 \end{aligned}                                                   \tag{C.4.8.S20}
\]
There is no rank assumption. Fixed independent Gaussian roots can be
included as extra arguments of G and integrated as well.

To prove the formulas, first replace C by \(C+\eta I\), \(\eta>0\).
For its density \(p_C(x)\), direct differentiation, with \(L=C^{-1}\),
gives
\[
 \partial_a p_C=\tfrac12p_C
       (x^TLC_aLx-\operatorname{tr}(LC_a)),\qquad
 \partial_{ij}p_C=p_C((Lx)_i(Lx)_j-L_{ij}).
\]
Thus \(\partial_a p_C=\frac12\sum_{ij}C_{a,ij}\partial_{ij}p_C\).
Two integrations by parts prove (C.4.8.S19); polynomial growth and Gaussian
decay remove the boundary terms. Differentiating once more proves (C.4.8.S20),
including both separate mixed terms.

On a compact parameter set, all covariance eigenvalues have a common upper
bound, so every fixed Gaussian moment is uniformly bounded for
\(0<\eta\le1\). Couple the regularized variable as \(X+\sqrt\eta Z\), with
an independent standard Gaussian Z. Restrict the arguments to a fixed
compact set, use uniform continuity there, and use a larger moment for its
complement. This proves uniform convergence, as \(\eta\downarrow0\), of
the expectations in (C.4.8.S19)–(C.4.8.S20) and of M itself. Integrate the regularized
identities over parameter intervals and pass to their uniform limits.
The fundamental theorem of calculus gives both identities at \(\eta=0\),
including one-sided endpoints. The identical argument integrates unchanged
Gaussian roots. No covariance square root has been differentiated.

The dimension-free form used below is, for example,
\[
 \left|\sum_{ij}C_{a,ij}\mathbb E G_{ij}\right|
      \le\|C_a\|_{\max}\mathbb E J_2(G),                     \tag{C.4.8.S21}
\]
where \(\|M\|_{\max}=\max_{ij}|M_{ij}|\). If G already is a first
source derivative and its source index is also summed, the required tensor
orders in (C.4.8.S19) and (C.4.8.S20) are three and five. They are covered by
(C.4.8.S13)–(C.4.8.S17).

These formulas also prove existence of the finite-program mass derivatives.
Induct chronologically in (C.4.8.S2)–(C.4.8.S7). The current lower coordinate
expressions depend on earlier deterministic coefficients. Their
expectations give the current forward covariances and alpha rows. These
give the forward expressions, upper fields, beta, and reverse covariances;
only then is the lower raw state updated. At each fixed stage all coordinate
expressions and their fixed derivatives have polynomial envelopes in the
finite Gaussian source list, locally uniformly in the mass parameters.
Indeed Q is Gaussian plus a finite bounded sum, tanh derivatives are
bounded, and differentiation of each finite lower update makes only finite
products of these quantities. The coefficients already constructed are
smooth by the induction hypothesis. Formulas (C.4.8.S19)–(C.4.8.S20) therefore give
the next derivatives, even at a singular covariance. This is a finite
chronological construction, without a current-node algebraic fixed point.

###### 4. The full first mass-response equations

Superscript \(\sigma\) on a deterministic scalar or coefficient denotes
its full mass derivative. On a coordinate expression it denotes the
explicit mass derivative with all Gaussian source coordinates held fixed.
The distinction is resolved by writing, for each lower or upper expression,
\[
 \mathfrak D_\ell^\sigma[G]
   =\mathbb E_\ell G^\sigma
      +\tfrac12\sum_{pq}(C_\ell^\sigma)_{pq}
                                      \mathbb E_\ell\partial_{pq}G,
 \quad C_1=C_\zeta,\quad C_2=C_\xi.                           \tag{C.4.8.S22}
\]
Thus \(\mathfrak D_\ell^\sigma[G]\) is the full derivative of its
expectation. Put \(W_k^\sigma=w_k^\sigma\) and
\(d_k^\sigma=c_k^\sigma\). The exact explicit recursions are
\[
 \gamma_{ka}^\sigma=-2h_k(s_ar_{ka}+p_ar_{ka}^\sigma),
 \qquad H_i^\sigma=\phi'(w_k\cdot u_i)(W_k^\sigma\cdot u_i),
                                                                    \tag{C.4.8.S23}
\]
\[
 Q_i^\sigma=\sum_{q\le i}
                 (D_{i,q}^\sigma H_q+D_{i,q}H_q^\sigma),
\]
\[
 \begin{aligned}
 W_{k+1}^\sigma=W_k^\sigma
 &+\sum_a\gamma_{ka}^\sigma\phi'(w_k\cdot u_a)Q_{ka}u_a\\
 &+\sum_a\gamma_{ka}u_a
   [\phi''(w_k\cdot u_a)Q_{ka}(W_k^\sigma\cdot u_a)
                      +\phi'(w_k\cdot u_a)Q_{ka}^\sigma],
 \end{aligned}                                                   \tag{C.4.8.S24}
\]
\[
 \begin{aligned}
 Z_i^\sigma&=\sum_{q<i}(F_{i,q}^\sigma\Delta_q+F_{i,q}\Delta_q^\sigma),\\
 d_k^\sigma&=\sum_{q<k}
        [\gamma_q^\sigma\phi(Z_q)+\gamma_q\phi'(Z_q)Z_q^\sigma],\\
 \Delta_i^\sigma&=\phi'(Z_i)d_k^\sigma
                                 +c_k\phi''(Z_i)Z_i^\sigma.
 \end{aligned}                                                   \tag{C.4.8.S25}
\]
There is no \(\xi^\sigma\) or \(\zeta^\sigma\) term in these explicit
equations. The changing source covariance enters through all of
\[
 \begin{aligned}
 (C_\xi^\sigma)_{ij}&=\mathfrak D_1^\sigma[H_iH_j],&
 (C_\zeta^\sigma)_{ij}&=\mathfrak D_2^\sigma[\Delta_i\Delta_j],\\
 \alpha_{i,q}^\sigma&=\mathfrak D_1^\sigma[\partial_{\zeta_q}H_i],&
 \beta_{i,q}^\sigma&=\mathfrak D_2^\sigma[\partial_{\xi_q}\Delta_i],\\
 r_{ku}^\sigma&=\mathfrak D_2^\sigma[c_k\phi(Z_{ku})],&&
 \end{aligned}                                                   \tag{C.4.8.S26}
\]
where a passive residual may use any fixed label, whose derivative is zero.
The deterministic rows are differentiated as
\[
 \begin{aligned}
 F_{i,q}^\sigma
   &=\alpha_{i,q}^\sigma+\gamma_q^\sigma(C_\xi)_{iq}
                                      +\gamma_q(C_\xi^\sigma)_{iq},\\
 D_{i,q}^\sigma
   &=\beta_{i,q}^\sigma+\mathbf1_{q<i}
       [\gamma_q^\sigma(C_\zeta)_{iq}
                                      +\gamma_q(C_\zeta^\sigma)_{iq}].
 \end{aligned}                                                   \tag{C.4.8.S27}
\]
Equations (C.4.8.S22)–(C.4.8.S27), in the chronological order already given, form
the full first response. All expectations include the actual residual
feedback, source covariance changes, and response coefficients.

###### 5. A local bound with constants independent of derivative history

Fix a starting node b and a consecutive interval of nodes with total
length at most \(\ell\). Source slots with time strictly less than b are
called old; all other slots in this interval are new. Assume derivatives
on the old prefix and explicit state derivatives at b have already been
bounded uniformly. The known deterministic bounds comprise residual
derivatives, covariance entry suprema, and the absolute row sums of
derivative F,D,alpha,beta arrays. The known random bounds comprise lower
explicit source jets at every finite moment needed and upper explicit
source jets pointwise. Enlarging a source list leaves all old marginal
Gaussian laws unchanged, so their known bounds remain applicable.

For a fixed finite graph let E be the maximum over the current interval
of the following deterministic quantities: absolute residual derivatives,
entry suprema of the two covariance derivative arrays for pairs with at
least one new endpoint, and absolute row sums of F,D,alpha,beta derivatives
at a new output node. All passive inputs in these quantities are compared
at that same input, not against an old axis. The bound may first be proved
for a fixed finite list of passive queries; its constants are independent
of that list and its query values, so the resulting bound is uniform over
the circle. The fixed graph's quantities are finite by the preceding
derivative construction. Write \(S=\|\sigma\|_{\rm TV}\).

We prove
\[
                         E\le C_{\rm old}+C S+C_*\ell E.  \tag{C.4.8.S28}
\]
The coefficient \(C_*\) depends only on the base constants and finitely
many fixed base moment/jet bounds. It is independent of all derivative
history bounds. The finite additive constant \(C_{\rm old}\) depends on
those bounds and vanishes with them. The following estimates prove this
separation explicitly.

First, for each separately fixed source order j and moment p, the lower
explicit response obeys
\[
 \left\|\max_{b\le k}J_j(W_k^\sigma)\right\|_p
       \le C_{{\rm old},j,p}+C_{j,p}S+C_{j,p}\ell E.          \tag{C.4.8.S29}
\]
For j=0 take the pointwise maximum of \(|W_k^\sigma|\) over current and
earlier nodes in the interval. The coefficient of this unknown maximum
in (C.4.8.S24) is bounded by \(h_k(2R_0D_0+4R_0q_k)\). Its accumulated
propagator is at most \(e^{\mathcal A}\), with every fixed moment by
(C.4.8.S10). Current D-derivative row forcing contributes at most \(C h_kE\),
and the residual derivative part of \(\gamma^\sigma\) contributes at most
\(C h_k E q_k\). Their total over the interval has \(L^p\) norm at most
\(C_p\ell E\), since \(\|\sum_{b\le k}h_kq_k\|_p\le C_p\ell\).
The direct \(s_a\) term is treated with weights \(|s_a|/S\), omitting it
if S=0, and costs \(C_p\ell S\) using the uniform marginal Q moments.
Holder includes its product with the propagator, without an independence
assumption. The initial explicit response and terms involving old
\(W_q^\sigma\) give an additive history bound.

For positive j, apply source derivatives to (C.4.8.S24). The highest response
jet still has the same coefficient \(h_k(2R_0D_0+4R_0q_k)\). Every other
term is a product of a smaller response jet with base jets, or a derivative
D row with base jets, or a derivative gamma with base jets and one Q value.
This assertion follows directly from (C.4.8.S12): the single partition block
containing all response derivatives supplies the highest jet; every other
partition places at least one derivative on a base factor. The direct
source derivative of Q has sum one at order one and zero at larger orders.
Consequently there is no factor equal to the number of source slots.

Induct on j with the same propagator. The dependence on current E is
linear. One may separate the explicit linear recursion into the part with
zero derivative history and forcing from current E, and the part with old
history and direct \(s_a\) forcing. In the former part all terms contain
one interval sum; the product rule, Holder and induction preserve its
\(C_{j,p}\ell E\) bound. For instance the next lower-jet forcing is an
interval sum of base-jet products times a smaller response already bounded
by \(C\ell E\); its extra interval length is at most T and can be absorbed
in the constant. In the latter part the same linear estimates give only
additive old bounds and S. This proves (C.4.8.S29) and proves that its coefficient
of \(\ell E\) uses no derivative history. Products with old random response
jets use their already known higher finite moments, all in the additive
term. The constants in (C.4.8.S29) may increase with p, but p is separately fixed.

By (C.4.8.S12), the same bounds hold for explicit derivatives of \(H_i\), of
\(H_iH_j\), and their required source jets. To close the deterministic
inequality (C.4.8.S28), only source orders zero and one in these explicit
derivatives are required, in expectation. A fixed finite number of larger
base moments suffices for their Holder estimates.

Next consider the lower Gaussian terms in (C.4.8.S26). Split
\(C_\zeta^\sigma\) into its old-old block and its complement. The old-old
entries have the known prefix bound. Contraction against a full absolute
source tensor sum is therefore an additive old term by (C.4.8.S13). On the
complement at least one differentiated source is new. A boundary lower
expression, constructed after (C.4.8.S18), depends only on old sources. Its
derivative in that new source is zero. Hence, for \(G=H_iH_j\),
\[
 \begin{aligned}
 &\left|\sum_{p,q\text{ not both old}}
       (C_\zeta^\sigma)_{pq}\mathbb E_1\partial_{pq}G\right|\\
 &\hspace{12mm}\le E\,\mathbb E_1J_2(G-G_{\rm boundary})
                      \le C\ell E.                          \tag{C.4.8.S30}
 \end{aligned}
\]
For alpha the required row sum is bounded by
\[
 \sum_l\left|\sum_{p,q\text{ not both old}}
       (C_\zeta^\sigma)_{pq}
           \mathbb E_1\partial_{pql}H_i\right|
 \le E\,\mathbb E_1J_3(H_i-H_{bu_i})\le C\ell E.             \tag{C.4.8.S31}
\]
This cancellation also holds when l is old: the pair \(p,q\) still
contains a new source. When l is new its boundary derivative vanishes
as well. Formula (C.4.8.S29) controls the explicit terms in (C.4.8.S26). Together
these estimates give
\[
 \|C_\xi^\sigma\|_{\max}
        +\sup_i\sum_q|\alpha_{i,q}^\sigma|
                  \le C_{\rm old}+CS+C\ell E.               \tag{C.4.8.S32}
\]
The covariance norm here includes old-old entries with their old bound.

Insert (C.4.8.S32) into the first line of (C.4.8.S27). Old gamma derivatives are
bounded in total absolute mass by
\(2T(R_0S+\sup_{q\text{ old}}|r_q^\sigma|)\); old base gamma values have
sum at most \(2R_0T\). Current gamma derivatives have sum at most
\(C\ell(S+E)\) by (C.4.8.S23). Since base lower contractions are at most one,
\[
                     \sup_i\sum_q|F_{i,q}^\sigma|
                  \le C_{\rm old}+CS+C\ell E.               \tag{C.4.8.S33}
\]

For the upper explicit response, use (C.4.8.S25), (C.4.8.S33), and the entrywise
density \(|F_{i,(s,a)}|\le f_0h_sp_a\). Base upper jets are pointwise
bounded. At source order zero the new unknown response obeys a Volterra
inequality with coefficient \(f_0(2R_0T+2C_0)\), after the readout sum
is substituted and its double time sum bounded by T times its single sum.
The F-derivative row forcing has (C.4.8.S33); direct current gamma derivatives
cost \(C\ell(S+E)\), and old terms are known. At a higher source order,
the same highest-order coefficient applies, with bounded lower-order
response contributions. Induction on the source order and iteration of
the scalar Volterra inequality therefore give, pointwise,
\[
 \max_{i\text{ in interval}}
       [J_j(Z_i^\sigma)+J_j(\Delta_i^\sigma)+J_j(d_{t(i)}^\sigma)]
             \le C_{{\rm old},j}+C_jS+C_j\ell E.             \tag{C.4.8.S34}
\]
Linearity again separates the history and current-E contributions. Its
\(\ell E\) coefficient depends only on base upper jets, \(f_0,R_0,C_0,T\),
and the fixed order. Upper repeated source diagonals are covered by their
full tensor sums; they require no product of injection masses.

Apply (C.4.8.S22) to the upper expressions in (C.4.8.S26). The explicit part is
bounded by (C.4.8.S34) with source orders zero and one. The covariance term
uses the entry supremum (C.4.8.S32) and the base upper tensors of order two,
or three for the beta row. Thus
\[
 \sup_{i,u}|r_{iu}^\sigma|+\|C_\zeta^\sigma\|_{\max}
         +\sup_i\sum_q|\beta_{i,q}^\sigma|
                 \le C_{\rm old}+CS+C\ell E.                \tag{C.4.8.S35}
\]
Finally substitute (C.4.8.S35) into the D line of (C.4.8.S27). Base upper
contractions are bounded by \(C_0^2\), base gamma has total mass at most
\(2R_0T\), old gamma derivatives are known, and new gamma derivatives
sum to \(C\ell(S+E)\). This gives
\[
                       \sup_i\sum_q|D_{i,q}^\sigma|
                 \le C_{\rm old}+CS+C\ell E.                \tag{C.4.8.S36}
\]
Equations (C.4.8.S32)–(C.4.8.S36) bound all components defining E and prove (C.4.8.S28).

Only finitely many low-order estimates determine \(C_*\): expectations
of explicit jets through order one, base increment jets through order
three, and upper base tensors through order three. Their Holder steps use
finitely many specified finite base moments. Choose \(\ell>0\) with
\(C_*\ell\le1/2\), using those estimates alone. There is no requirement
that this same \(\ell\) make \(C_{j,p}\ell\) small for all j or p. Once E
is bounded by absorption, (C.4.8.S29) and (C.4.8.S34) furnish any higher separately
fixed moment/order bound without a further absorption step.

Decrease the maximum step to \(\ell/2\). Consecutive groups of steps can
be chosen with total lengths between \(\ell/2\) and \(\ell\), except for
the final group, so their number is at most \(2T/\ell+1\). The first group
has zero derivative history. Absorption in (C.4.8.S28) bounds E there by CS.
Afterward obtain all higher finite moments of explicit lower response
jets through order three and upper response jets through order three
from (C.4.8.S29)–(C.4.8.S34). These give the next group's old bounds. Iterate over
the bounded number of groups. The first derivative system is linear in
\(\sigma\), so every bound remains proportional to S. The number of groups
and all resulting constants are independent of the mesh and support. The
output equation in (C.4.8.S26) proves the first assertion of (C.4.8.S1).

###### 6. The mixed second response and the same absorption constant

Fix the first responses in directions \(\sigma,\tau\), now uniformly
bounded through T. Write \(R=\|\tau\|_{\rm TV}\). The exact weight formula is
\[
 \gamma_{ka}^{\sigma\tau}
    =-2h_k(s_ar_{ka}^\tau+v_ar_{ka}^\sigma+p_ar_{ka}^{\sigma\tau}).
                                                                    \tag{C.4.8.S37}
\]
The first two terms have total absolute size at most \(C\ell SR\) on a
group of length \(\ell\); the last has exactly the first response's
linear unknown coefficient.

For every lower or upper expectation the full mixed derivative is
\[
 \begin{aligned}
 \mathfrak D_\ell^{\sigma\tau}[G]
 ={}&\mathbb E_\ell G^{\sigma\tau}
   +\tfrac12\sum_{pq}(C_\ell^{\sigma\tau})_{pq}
                                      \mathbb E_\ell\partial_{pq}G\\
 &+\tfrac12\sum_{pq}(C_\ell^\sigma)_{pq}
                                      \mathbb E_\ell\partial_{pq}G^\tau
  +\tfrac12\sum_{pq}(C_\ell^\tau)_{pq}
                                      \mathbb E_\ell\partial_{pq}G^\sigma\\
 &+\tfrac14\sum_{pq,lr}(C_\ell^\sigma)_{pq}(C_\ell^\tau)_{lr}
                                      \mathbb E_\ell\partial_{pqlr}G.
 \end{aligned}                                                   \tag{C.4.8.S38}
\]
The last three terms are already bounded by CSR. For alpha and beta,
G is a first source derivative whose index is also summed: the mixed
first-response term uses explicit source order three, and the last term
uses base source order five. Scalar products and output expectations need
no larger orders. All required first response moments were obtained after
the first-order absorption and are now known constants.

Here are the explicit second identities, which specify the highest-order
linear part without dropping product terms:
\[
 H_i^{\sigma\tau}=\phi'(w_k\cdot u_i)(W_k^{\sigma\tau}\cdot u_i)
       +\phi''(w_k\cdot u_i)(W_k^\sigma\cdot u_i)(W_k^\tau\cdot u_i),
\]
\[
 Q_i^{\sigma\tau}=\sum_{q\le i}
 [D_{i,q}^{\sigma\tau}H_q+D_{i,q}H_q^{\sigma\tau}
                    +D_{i,q}^\sigma H_q^\tau+D_{i,q}^\tau H_q^\sigma],
\]
\[
 Z_i^{\sigma\tau}=\sum_{q<i}
 [F_{i,q}^{\sigma\tau}\Delta_q+F_{i,q}\Delta_q^{\sigma\tau}
          +F_{i,q}^\sigma\Delta_q^\tau+F_{i,q}^\tau\Delta_q^\sigma],
                                                                    \tag{C.4.8.S39}
\]
\[
 \begin{aligned}
 d_k^{\sigma\tau}=\sum_{q<k}[&\gamma_q^{\sigma\tau}\phi(Z_q)
            +\gamma_q\phi'(Z_q)Z_q^{\sigma\tau}
            +\gamma_q\phi''(Z_q)Z_q^\sigma Z_q^\tau\\
            &+\gamma_q^\sigma\phi'(Z_q)Z_q^\tau
             +\gamma_q^\tau\phi'(Z_q)Z_q^\sigma],\\
 \Delta_i^{\sigma\tau}={}&\phi'(Z_i)d_k^{\sigma\tau}
              +c_k\phi''(Z_i)Z_i^{\sigma\tau}
              +\phi''(Z_i)(d_k^\sigma Z_i^\tau+d_k^\tau Z_i^\sigma)
              +c_k\phi'''(Z_i)Z_i^\sigma Z_i^\tau.
 \end{aligned}                                                   \tag{C.4.8.S40}
\]
Let \(L_{ka}=\phi'(w_k\cdot u_a)Q_{ka}u_a\). Its explicit first derivative
is the bracketed summand of (C.4.8.S24), and its mixed derivative is
\[
 \begin{aligned}
 L_{ka}^{\sigma\tau}=u_a[&\phi''(w_k\cdot u_a)Q_{ka}
                                      (W_k^{\sigma\tau}\cdot u_a)
                          +\phi'(w_k\cdot u_a)Q_{ka}^{\sigma\tau}\\
 &+\phi'''(w_k\cdot u_a)Q_{ka}
                  (W_k^\sigma\cdot u_a)(W_k^\tau\cdot u_a)\\
 &+\phi''(w_k\cdot u_a)
       ((W_k^\sigma\cdot u_a)Q_{ka}^\tau
                         +(W_k^\tau\cdot u_a)Q_{ka}^\sigma)].
 \end{aligned}
\]
Consequently
\[
 W_{k+1}^{\sigma\tau}=W_k^{\sigma\tau}+\sum_a
 [\gamma_{ka}^{\sigma\tau}L_{ka}+\gamma_{ka}L_{ka}^{\sigma\tau}
       +\gamma_{ka}^\sigma L_{ka}^\tau
       +\gamma_{ka}^\tau L_{ka}^\sigma].                       \tag{C.4.8.S41}
\]
The deterministic coefficients satisfy
\[
 \begin{aligned}
 F_{i,q}^{\sigma\tau}={}&\alpha_{i,q}^{\sigma\tau}
   +\gamma_q^{\sigma\tau}(C_\xi)_{iq}
   +\gamma_q(C_\xi^{\sigma\tau})_{iq}
   +\gamma_q^\sigma(C_\xi^\tau)_{iq}
   +\gamma_q^\tau(C_\xi^\sigma)_{iq},\\
 D_{i,q}^{\sigma\tau}={}&\beta_{i,q}^{\sigma\tau}+\mathbf1_{q<i}
 [\gamma_q^{\sigma\tau}(C_\zeta)_{iq}
   +\gamma_q(C_\zeta^{\sigma\tau})_{iq}
   +\gamma_q^\sigma(C_\zeta^\tau)_{iq}
   +\gamma_q^\tau(C_\zeta^\sigma)_{iq}].
 \end{aligned}                                                   \tag{C.4.8.S42}
\]
Second derivatives of covariances, alpha, beta and residuals are given by
(C.4.8.S26) with \(\mathfrak D^{\sigma\tau}\) from (C.4.8.S38). This completely
specifies the second recurrence.

Every occurrence of a mixed second unknown in (C.4.8.S37)–(C.4.8.S42) is linear,
with exactly the base coefficient occurring in (C.4.8.S23)–(C.4.8.S27). All other
terms contain two first responses or a mass direction times a first
response. Their source-jet norms are bounded by CSR using the first
bounds and Holder; scalar coefficient rows use their absolute row sums.
For terms in raw updates the outside factor is still \(h_kp_a\),
\(h_ks_a\), or \(h_kv_a\). For example, the two coefficient cross terms
in (C.4.8.S42) sum to at most a first covariance supremum times the total
absolute first gamma sum. Thus no source count occurs in these known
inhomogeneous terms.

Let \(E_2\) be the deterministic norm of Section 5 for mixed second
derivatives. Its explicit history needs only source jets through order
one, at all finite moments needed. The first two terms of (C.4.8.S38) form
the same linear Gaussian part as before. For the unknown new block of
\(C_\zeta^{\sigma\tau}\), subtract the same boundary lower expression.
Equations (C.4.8.S30)–(C.4.8.S31) give \(C\ell E_2\), because they use unchanged
base increment tensors. The last three terms of (C.4.8.S38) are known CSR.
The explicit linear propagation and all other deterministic rows have
the same coefficients as Section 5, by (C.4.8.S39)–(C.4.8.S42). Therefore
\[
                     E_2\le C_{{\rm old},2}+CSR+C_*\ell E_2.\tag{C.4.8.S43}
\]
The coefficient of \(\ell E_2\) is a base constant. First-response bounds
enter only the additive term; they do not change the chosen interval
length. Absorb with the same \(\ell\), obtain the necessary higher
explicit moments afterward, and iterate over the same bounded number
of intervals. Initial second derivatives vanish. Bilinearity in
\((\sigma,\tau)\) preserves the factor SR throughout this induction.
The output expectation in (C.4.8.S38) proves the second assertion of (C.4.8.S1).

###### 7. Zero masses and the observation interval

For a fixed support and fixed graph, the derivative expressions obtained
chronologically from (C.4.8.S19)–(C.4.8.S20) extend continuously as positive masses
approach zero while the law stays in the ball. To verify this, use the
finite construction order again. Each coefficient already constructed has
a continuous derivative extension. Its descendants have common polynomial
Gaussian envelopes locally on the closed mass parameter set. Bounded
covariances and the regularization argument in Section 3 pass their
expectations and derivative expressions continuously to the boundary.
Unused zero-mass updates vanish, and introducing their unused source names
does not change the value recursion. Integrating the interior derivative
identities on admissible segments or rectangles and taking the boundary
limit gives their one-sided versions. Constants in (C.4.8.S1) did not depend
on the minimum positive mass. This proves the stated boundary extension,
including adding a new atom. It does not approximate a singular covariance
by a nonsingular law; covariance rank was unrestricted at every step.

At a non-node time, the affine raw Euler state equals the state obtained
by appending the appropriate shorter final Euler step, followed by
recomputation of its observations. C.4.7.N-cap applies to this program as
well. All estimates are uniform over the passive input and over such
final steps. They therefore hold on the whole physical interval
\([0,40]\), and imply the normalized-circle \(L^2\) bounds.

The lemma concerns derivatives of the exact population Euler algorithms,
with all three trained blocks and both orientations of the initialized
Gaussian action. Its proof uses the C.4.7 cap and the III.F source
representation, with source moments derived above. No bounded action of
\(A_0\) or \(A_0^*\) on arbitrary \(L^p\) inputs, no ambient raw-\(L^2\)
Fréchet derivative, and no interchange with a finite-width derivative are
needed.

##### C.4.8.2. Actual influence for Borel laws

###### Finite estimate and actual value completion


Choose a closed law ball of radius \(3\delta_Y/4\). The lemma in C.4.8.1 applies
to all finite laws in a slightly larger ball still inside the C.4.7 source-cap
neighborhood, and all sufficiently fine population raw Euler meshes. It gives
constants \(L,M<\infty\), independent of the mesh, support size, minimum mass,
and covariance rank, such that its endpoint map \(F_h\) obeys
\[
 \|\partial_\sigma F_h(\lambda)\|_{\mathcal C}\le L\|\sigma\|_{\rm TV},
 \qquad
 \|\partial_\sigma\partial_\tau F_h(\lambda)\|_{\mathcal C}
                    \le M\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}.        \tag{C.4.8.P7}
\]
Directions have zero total mass. They are taken in the finite simplex, with
continuous one-sided extensions at zero masses. The total-variation norm is
the total mass of the variation measure, so \(\|\delta_z-\delta_{z'}\|_{\rm TV}
\le2\). The estimates concern only probability-preserving segments and
rectangles lying in the stated region.

C.4.7 gives \(F_h(\lambda)\to F(\lambda)\) in \(\mathcal C\) for every
fixed finite law there. Its proof also gives uniform value completion on
smaller balls, but the first passage below only needs pointwise value
convergence, including at the finitely many law arguments in each comparison.
The actual map \(F:U_Y\to\mathcal C\) is \(W_1\)-continuous and bounded.
Boundedness follows already from \(\|c(t)\|_\infty\le2Yt\) in C.4.7; a
larger Euler bound \(Y(e^{2T}-1)\) would suffice as well.

###### Actual atom response, centering, and general directions

Let \(\mathcal K=\{Q:W_1(Q,\nu_*)\le\delta_Y/2\}\) and
\(D_Y=2+2Y\), an upper bound for the data diameter. Choose
\(\epsilon_0=\min(1/2,\delta_Y/(4D_Y))\). Every contamination of a law
in \(\mathcal K\) of size at most \(\epsilon_0\) remains in the larger
ball described at the start of C.4.8.2. Finite-support Taylor's formula from (C.4.8.P7) gives
\[
 \|F_h((1-\epsilon)\lambda+\epsilon\delta_z)-F_h(\lambda)
       -\epsilon I_{h,\lambda}(z)\|_{\mathcal C}
                  \le2M\epsilon^2,\qquad
 I_{h,\lambda}(z)=\partial_{\delta_z-\lambda}F_h(\lambda).             \tag{C.4.8.P8}
\]
To add a new observation, include its slot with mass zero and use the
one-sided source derivative. No strictly positive lower mass is required.

Fix \(\lambda,z\). Comparing two derivatives to the same forward quotient
in (C.4.8.P8) shows that their limsup difference as both meshes vanish is at most
\(4M\epsilon\). The quotient values converge by C.4.7. Letting \(\epsilon\)
decrease proves that \(I_{h,\lambda}(z)\) has a limit in \(\mathcal C\),
denoted \(I_\lambda(z)\). It satisfies \(\|I_\lambda(z)\|\le2L\), and
passing to the limit in (C.4.8.P8) gives its actual contamination derivative with
the same remainder. This argument uses arbitrary vanishing mesh sequences;
the result does not depend on a chosen sequence.

For arbitrary \(Q\in\mathcal K\), define the continuous forward quotient
\[
 J_\epsilon(Q,z)=
   \epsilon^{-1}\{F((1-\epsilon)Q+\epsilon\delta_z)-F(Q)\}.
\]
For finite \(Q\), (C.4.8.P8) gives
\(\|J_\epsilon(Q,z)-J_\eta(Q,z)\|\le2M(\epsilon+\eta)\).
Finite laws are \(W_1\)-dense in \(\mathcal K\): approximate by finite
quantization and, if necessary, mix a vanishing amount of \(\nu_*\) to move
strictly inside the ball. Continuity of \(F\) passes this inequality to every
\(Q\). Thus the quotients converge uniformly in \((Q,z)\) to
\(I_Q(z)\), with
\[
 \|F((1-\epsilon)Q+\epsilon\delta_z)-F(Q)-\epsilon I_Q(z)\|_{\mathcal C}
                         \le2M\epsilon^2.                            \tag{C.4.8.P9}
\]
The map \((Q,z)\mapsto(1-\epsilon)Q+\epsilon\delta_z\) is continuous in
\(W_1\), by the mixture coupling. Each \(J_\epsilon\) is therefore jointly
continuous. Its uniform limit \(I\) is jointly continuous on the compact
set \(\mathcal K\times\mathcal Z\), and is bounded by \(2L\). In particular
it is a Bochner-measurable, square-integrable \(H\)-valued field.

For each finite law \(\lambda=\sum_a p_a\delta_{z_a}\), linearity of the
finite derivative gives
\[
 \sum_a p_a I_{h,\lambda}(z_a)=
 \partial_{\sum_a p_a(\delta_{z_a}-\lambda)}F_h(\lambda)=0.
\]
The mesh limit preserves this equality. If \(\lambda_j\to Q\) weakly,
joint continuity implies \(I_{\lambda_j}\to I_Q\) uniformly in the atom.
For any continuous Banach-valued function on a compact metric space its
integrals converge in norm under weak convergence of probability laws: choose
a finite continuous partition of unity whose weighted point values uniformly
approximate that function, and apply weak convergence to its finitely many
scalar weights. Applying this fact to \(I_Q\) proves
\[
                         \int I_Q\,dQ=0.                             \tag{C.4.8.P10}
\]
This proves centering for the actual trained response, not just for a formal
linearized equation.

At the reference law this response agrees with C.4.6:
\(I_{\nu_*}(z)=\mathscr D_{\delta_z-\nu_*}f(T,\cdot)\).
Indeed C.4.7 identifies the latter with the same actual contamination
derivative, and a norm limit has only one value. This does not extend the
finite-network derivative conclusions of C.4.6 to other base laws.

The same argument supplies the integral representation in every admissible
law direction. For finite \(\lambda,\nu\), the derivative of a mixture has
value \(\int I_{h,\lambda}\,d(\nu-\lambda)\) and Taylor remainder at most
\(M\epsilon^2\|\nu-\lambda\|_{\rm TV}^2/2\). Pass first through the mesh
limit. Next approximate both laws by the same finite quantization map.
Quantization contracts total variation and has uniformly vanishing transport
error. The displayed integral converges by joint continuity, so
\[
 \left.\frac d{dt}F((1-t)Q+t\nu)\right|_{t=0+}
                  =\int I_Q(z)\,d(\nu-Q)(z).                         \tag{C.4.8.P11}
\]
Here the segment is restricted to the region where the estimate applies;
\(\nu\) need not itself lie there if only a short initial part is used.
Apply this identity at every point of an admissible segment. Joint continuity
of \(I\) makes its directional derivative continuous, hence gives the
fundamental theorem of calculus on that segment. For a general zero-mass
direction \(\eta\) admitting a positive segment length \(a\), set
\(\nu=Q+a\eta\) and rescale (C.4.8.P11). This covers all directions used in
replacement rectangles and in conditional-expectation telescoping.

Likewise the mixed finite-difference bound
\[
 \|F(Q+s\sigma+t\tau)-F(Q+s\sigma)-F(Q+t\tau)+F(Q)\|_{\mathcal C}
             \le Mst\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}              \tag{C.4.8.P12}
\]
passes from (C.4.8.P7) first in mesh and then through common quantization. All laws
on the rectangle must be probabilities in the open ball of radius
\(\delta_Y/2\). Its compact image has positive distance from the boundary;
fine quantizations therefore remain in the larger analytic region. The
argument takes only four value limits. No second derivative of the limiting
population flow is assumed or needed.

###### A usable characterization of the signed field

For a finite law \(\lambda\), the source lemma in C.4.8.1 supplies an explicit
chronological Gaussian recursion for \(I_{h,\lambda}(z)\): append the atom
\(z\), differentiate its mass vector in direction \(\delta_z-\lambda\), and
propagate the displayed lower and upper coordinate responses together with
both covariance responses, all residual responses, and both response
coefficient arrays. Expectations are differentiated by the Gaussian covariance
formula, including at singular covariance. All initial mass responses are
zero. At the last node the resulting full derivative of
\(\mathbb E_2[c\phi(Z(u))]\) is \(I_{h,\lambda}(z)(\sqrt2u)\).

For any finite quantizations \(q_j:\mathcal Z\to\mathcal Z\) with
\(\sup_z d(q_jz,z)\to0\), chosen so the base laws stay in the admitted ball,
the actual field is characterized by
\[
 I_\mu(z)=\lim_{j\to\infty}\lim_{h\to0}
       I_{h,(q_j)_\#\mu}(q_jz)\quad\hbox{in }\mathcal C.             \tag{C.4.8.P13}
\]
The inner limit exists by (C.4.8.P8), and the outer limit follows uniformly in
\(z\) from joint continuity. The result is independent of the quantizations
and meshes by (C.4.8.P9). Thus (C.4.8.P13), with the complete source derivative recursion,
defines a well-posed evolution-and-limit procedure for the influence. It
retains all three trained blocks and both initialized action orientations.
It does not replace those objects by an undetermined endpoint derivative.


##### C.4.8.3. A Hilbert sampling lemma

###### Statement


Let \(\mathcal Z\) be a compact metric space, let \(H\) be a separable real Hilbert space, and let \(\mu\in\mathcal P(\mathcal Z)\). Equip the probability laws with \(W_1\). Let \(U\) be a \(W_1\)-open neighborhood of \(\mu\), and let \(F:U\to H\) be bounded and \(W_1\)-continuous. Use the total-variation norm convention \(\|\delta_z-\delta_{z'}\|_{\rm TV}\le2\).

Assume the following three properties.

1. **Actual first mixture response.** There is a jointly Borel kernel \(I:U\times\mathcal Z\to H\), with \(\int I_Q\,dQ=0\), such that on every affine probability segment \(Q_t=Q+t\eta\) contained in \(U\), \(t\mapsto F(Q_t)\) is continuously differentiable, including one-sided endpoint derivatives, and

   \[
   \frac d{dt}F(Q_t)=\int I_{Q_t}(z)\,\eta(dz).
   \tag{C.4.8.R1}
   \]

   Here \(\eta\) is a zero-mass finite signed measure, and the stated Bochner integrals exist. In particular,

   \[
   I_Q(z)=\left.\frac d{d\epsilon}
   F((1-\epsilon)Q+\epsilon\delta_z)\right|_{\epsilon=0+}.
   \tag{C.4.8.R2}
   \]

2. **Uniform mixed second differences.** There is \(M<\infty\) such that, whenever the affine rectangle \(Q+s\eta+t\xi\), \(0\le s,t\le1\), consists of probability laws in \(U\),

   \[
   \|F(Q+\eta+\xi)-F(Q+\eta)-F(Q+\xi)+F(Q)\|_H
   \le M\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}.
   \tag{C.4.8.R3}
   \]

3. **Continuity at the sampling law.** As \(Q\to\mu\) in \(W_1\), with \(Q\in U\),

   \[
   \|I_Q-I_\mu\|_{L^2(\mu;H)}\longrightarrow0.
   \tag{C.4.8.R4}
   \]

The norm in (C.4.8.R4) uses the fixed law \(\mu\). Joint continuity of \((Q,z)\mapsto I_Q(z)\) near \(\{\mu\}\times\mathcal Z\) is a sufficient condition. The uniform local bounds needed for its integrability follow in the proof. A bounded second derivative in total variation implies (C.4.8.R3), but no second derivative of \(F\) is assumed here.

Let \(Z_1,Z_2,\ldots\) be iid with law \(\mu\), and put \(\mu_m=m^{-1}\sum_{i=1}^m\delta_{Z_i}\). There exist a \(W_1\)-open neighborhood \(V\) of \(\mu\), with \(V\subset U\), and a bounded Borel function \(\widetilde F:\mathcal P(\mathcal Z)\to H\), equal to \(F\) on \(V\), such that

\[
 \widetilde F(\mu_m)-F(\mu)
       =\frac1m\sum_{i=1}^m I_\mu(Z_i)+r_m,
 \qquad m\mathbb E\|r_m\|_H^2\longrightarrow0.
 \tag{C.4.8.R5}
\]

Moreover, \(\mathbb P(\mu_m\notin V)\le c_1e^{-c_2m}\) for constants \(c_1,c_2>0\). Consequently any globally defined finite-valued Borel extension \(\widehat F\) of \(F\) has the same expansion with \(\sqrt m\,r_m\to0\) in probability. The \(L^2\) assertion also holds for \(\widehat F\) if it is bounded, or more generally if

\[
 m\mathbb E\|\widehat F(\mu_m)-\widetilde F(\mu_m)\|_H^2
       \longrightarrow0.
 \tag{C.4.8.R6}
\]

In particular, the assertion for an actual endpoint statistic presupposes that this statistic is defined on all sample outcomes, or that an extension has explicitly been chosen.

The covariance operator of the limiting Gaussian is

\[
 C_\mu h=\int\langle I_\mu(z),h\rangle_H I_\mu(z)\,\mu(dz),
 \qquad \operatorname{tr}C_\mu=\int\|I_\mu(z)\|_H^2\,\mu(dz),
 \tag{C.4.8.R7}
\]

and

\[
 \sqrt m\,[\widetilde F(\mu_m)-F(\mu)]
      \Rightarrow\mathcal N_H(0,C_\mu),\qquad
 m\mathbb E\|\widetilde F(\mu_m)-F(\mu)\|_H^2
      \longrightarrow\operatorname{tr}C_\mu.
 \tag{C.4.8.R8}
\]

The distributional conclusion transfers to every extension above; the second-moment conclusion transfers under (C.4.8.R6).

###### Proof: line estimates and localization

If \(\mathcal Z\) has one point, every empirical law equals \(\mu\), and centering gives \(I_\mu=0\). All conclusions then hold directly. Assume its diameter \(D\) is positive.

First, (C.4.8.R3) gives the required Taylor estimate using only the first derivative. On a segment \(Q_t=Q+t\eta\), write \(f(t)=F(Q_t)\). For \(0\le a<b<1\), apply (C.4.8.R3) to the rectangle with base \(Q_a\) and increments \((b-a)\eta\) and \(h\eta\). Divide by \(h>0\) and let \(h\downarrow0\). Equation (C.4.8.R1) gives

\[
 \|f'(b)-f'(a)\|_H\le M(b-a)\|\eta\|_{\rm TV}^2.
\]

One-sided continuity covers the endpoints. Integrating the inequality proves

\[
 \left\|F(Q+\eta)-F(Q)-\int I_Q\,d\eta\right\|_H
       \le\frac M2\|\eta\|_{\rm TV}^2.
 \tag{C.4.8.R9}
\]

Choose \(r_{\rm loc}>0\) such that \(B_{W_1}(\mu,r_{\rm loc})\subset U\). Write \(B=\sup_U\|F\|_H\) and let \(\tau=\min\{1/2,r_{\rm loc}/(8D)\}\). If \(W_1(Q,\mu)<3r_{\rm loc}/4\), the contaminations \((1-s)Q+s\delta_z\), \(0\le s\le\tau\), stay in \(U\), since their distance from \(Q\) is at most \(sD\). By (C.4.8.R2) and (C.4.8.R9),

\[
 \|I_Q(z)\|_H\le 2B/\tau+2M\tau=:L
 \quad\text{for all such }Q\text{ and all }z.
 \tag{C.4.8.R10}
\]

This also proves the local square integrability used in (C.4.8.R4).

To construct a cutoff, choose a finite \(\epsilon\)-net \(z_1,\ldots,z_N\) in \(\mathcal Z\), with \(\epsilon=r_{\rm loc}/16\), and define

\[
 a_j(z)=(2\epsilon-d(z,z_j))_+,\qquad
 \psi_j(z)=\frac{a_j(z)}{\sum_k a_k(z)}.
\]

The denominator is at least \(\epsilon\). Thus the \(\psi_j\) are continuous, take values in \([0,1]\), and sum to one. Sending \(z\) to \(z_j\) with probabilities \(\psi_j(z)\) couples any law \(Q\) with \(Q^d=\sum_j(Q\psi_j)\delta_{z_j}\) at cost at most \(2\epsilon\). Coupling common discrete mass identically and the remainder at cost at most \(D\) gives

\[
 W_1(Q,\mu)\le4\epsilon+
              \frac D2\sum_j|Q\psi_j-\mu\psi_j|.
 \tag{C.4.8.R11}
\]

Put \(b=r_{\rm loc}/(2DN)\). Choose a smooth \(\chi_0:\mathbb R\to[0,1]\) equal to one on \([-1/2,1/2]\), positive on \((-1,1)\), and zero off that interval. Define

\[
 \chi(Q)=\prod_j\chi_0\bigl((Q\psi_j-\mu\psi_j)/b\bigr),
 \qquad V=\{Q:\max_j|Q\psi_j-\mu\psi_j|<b/2\}.
 \tag{C.4.8.R12}
\]

The support of \(\chi\) is contained in \(\{Q:W_1(Q,\mu)\le r_{\rm loc}/2\}\) by (C.4.8.R11); \(\chi=1\) on \(V\). Its first and second law derivatives have bounded scalar kernels, since they are finite sums of products of the \(\psi_j\) and derivatives of \(\chi_0\). Let \(a_Q(z)\) denote its first kernel. Define

\[
 \widetilde F(Q)=\chi(Q)F(Q)\quad(Q\in U),\qquad
 \widetilde F(Q)=0\quad(Q\notin U).
\]

Its centered first kernel is obtained by subtracting its \(Q\)-mean from

\[
 A_Q(z)=\chi(Q)I_Q(z)+F(Q)a_Q(z)
 \tag{C.4.8.R13}
\]

on \(U\), and setting it to zero elsewhere. This kernel is uniformly bounded by (C.4.8.R10), boundedness of \(F\), and the cutoff derivative bounds. The product and its first derivatives extend across the cutoff boundary because \(\chi\) and its derivatives vanish there and the other factors are uniformly bounded on a larger open neighborhood. Thus the first mixture calculus remains valid globally. On \(V\), the centered first kernel of \(\widetilde F\) is exactly \(I_Q\), so (C.4.8.R4) is preserved.

For completeness, the mixed finite-difference bound also survives this extension without any second derivative of \(F\). On a rectangle whose corners are indexed by \(00,10,01,11\), the exact product identity is

\[
\begin{aligned}
 \Delta_{12}(\chi F)
  ={}&\chi_{11}\Delta_{12}F
    +(\chi_{11}-\chi_{10})(F_{10}-F_{00})\\
   &+(\chi_{11}-\chi_{01})(F_{01}-F_{00})
    +(\Delta_{12}\chi)F_{00}.
\end{aligned}
 \tag{C.4.8.R14}
\]

On any rectangle in \(B_{W_1}(\mu,3r_{\rm loc}/4)\), (C.4.8.R3), the first derivative bound (C.4.8.R10), the bounded first and second derivatives of \(\chi\), and boundedness of \(F\) bound (C.4.8.R14) by

\[
 M_*\|\eta\|_{\rm TV}\|\xi\|_{\rm TV}
 \tag{C.4.8.R15}
\]

for a constant \(M_*\) independent of the rectangle.

For a general probability rectangle, its parameter domain is compact. The inverse images of \(B_{W_1}(\mu,3r_{\rm loc}/4)\) and of the complement of the support of \(\chi\) are an open cover of that domain. A sufficiently fine rectangular grid has every cell inside one member of this cover: choose parameter balls whose doubled balls lie in a member of the cover, take a finite subcover of the original balls, and use cells of diameter smaller than their minimum radius. In the first kind of cell (C.4.8.R15) applies; in the second the extended function is zero. Summing mixed cell differences telescopes to the difference on the whole rectangle. The products of cell side lengths sum to one, giving the global bound (C.4.8.R15). Hence \(\widetilde F\) has globally bounded first kernel and second mixed differences.

Finally, a variable in \([0,1]\) has centered log moment-generating function at most \(\lambda^2/8\): its second derivative is a tilted variance, at most \(1/4\), and its value and first derivative vanish at zero. Exponential Markov and independence therefore give

\[
 \mathbb P\bigl(|\mu_m\psi_j-\mu\psi_j|\ge b/2\bigr)
       \le2e^{-mb^2/2}.
\]

The union bound yields

\[
 \mathbb P(\mu_m\notin V)\le2N e^{-mb^2/2}.
 \tag{C.4.8.R16}
\]

###### Proof: the global sampling calculation

It remains to prove (C.4.8.R5) for a bounded functional defined on all probability laws, with a uniformly bounded centered first kernel and mixed difference bound \(M_*\). In this part write \(G\) for that functional and \(J_Q\) for its first kernel. We will apply the result to \(G=\widetilde F\), whose kernel satisfies \(J_\mu=I_\mu\).

The finite-test construction (C.4.8.R11), repeated with an arbitrarily small \(\epsilon\), shows that empirical laws converge to \(\mu\) in \(W_1\) in probability. Indeed, each finite set of bounded continuous empirical averages converges by its variance bound; (C.4.8.R11) then makes the remaining deterministic error arbitrarily small. The same conclusion holds for \(m^{-1}\mu+m^{-1}\sum_{i=2}^m\delta_{Z_i}\).

###### Bias

Define

\[
 \nu_i=(1-i/m)\mu+m^{-1}\sum_{j=1}^i\delta_{Z_j},
 \qquad 0\le i\le m.
\]

Every segment from \(\nu_{i-1}\) to \(\nu_i\) consists of probability laws. Equation (C.4.8.R9), now with constant \(M_*\), gives

\[
 G(\nu_i)-G(\nu_{i-1})
 =m^{-1}\int J_{\nu_{i-1}}(z)(\delta_{Z_i}-\mu)(dz)+R_i,
 \qquad\|R_i\|_H\le2M_*/m^2.
\]

Conditional on the previous samples, the first term has mean zero. Consequently

\[
 b_m:=\mathbb EG(\mu_m)-G(\mu),\qquad
 \|b_m\|_H\le2M_*/m.
 \tag{C.4.8.R17}
\]

###### Higher-order Hoeffding components

For any square-integrable \(H\)-valued statistic \(T=T(Z_1,\ldots,Z_m)\), define

\[
 T_S=\sum_{A\subset S}(-1)^{|S|-|A|}
                 \mathbb E[T\mid Z_i:i\in A],
 \qquad S\subset\{1,\ldots,m\}.
 \tag{C.4.8.R18}
\]

Finite inclusion--exclusion gives \(T=\sum_ST_S\). Each nonempty component has zero conditional mean when any coordinate in its index set is integrated out: terms in (C.4.8.R18) that include that coordinate cancel the terms that omit it. Choosing a coordinate in the symmetric difference of two distinct index sets proves their orthogonality in \(L^2\). Thus

\[
 R^{\rm H}:=T-\mathbb ET-
       \sum_i(\mathbb E[T\mid Z_i]-\mathbb ET)=\sum_{|S|\ge2}T_S
\]

is orthogonal to constants and to all sums of one-coordinate functions.

Let \(T^{(i)}\) replace \(Z_i\) by an independent copy, and let
\(D_{ij}T=T-T^{(i)}-T^{(j)}+T^{(ij)}\). A double replacement kills components not containing both indices. For a component containing both, the four replacement terms have equal second moments and are pairwise orthogonal, by conditioning on a coordinate where they differ. Components with distinct index sets also remain orthogonal after replacement. Hence

\[
 \mathbb E\|D_{ij}T\|_H^2
       =4\sum_{S\supset\{i,j\}}\mathbb E\|T_S\|_H^2,
\]

and summing over pairs gives

\[
 \mathbb E\|R^{\rm H}\|_H^2
       \le\frac14\sum_{i<j}\mathbb E\|D_{ij}T\|_H^2.
 \tag{C.4.8.R19}
\]

Apply this with \(T_m=G(\mu_m)\). Replacing observations \(i\) and \(j\) gives a probability rectangle with edge measures \(m^{-1}(\delta_{Z_i'}-\delta_{Z_i})\) and \(m^{-1}(\delta_{Z_j'}-\delta_{Z_j})\). Therefore

\[
 \|D_{ij}T_m\|_H\le4M_*/m^2,
 \qquad
 \mathbb E\|R_m^{\rm H}\|_H^2\le2M_*^2/m^2.
 \tag{C.4.8.R20}
\]

###### The first projection

By symmetry, using the version of conditional expectation obtained by integrating over the other samples, write

\[
 h_m(z)=m\{\mathbb E[T_m\mid Z_1=z]-\mathbb ET_m\},
 \qquad \int h_m\,d\mu=0.
\]

Let \(Q_m=m^{-1}\mu+m^{-1}\sum_{j=2}^m\delta_{Z_j}\). The law \(Q_m+m^{-1}(\delta_z-\mu)\) is a probability measure for every \(z\). Its Taylor expansion around \(Q_m\) has remainder at most \(2M_*/m^2\). Averaging over the other samples, subtracting the \(\mu\)-average over \(z\), and multiplying by \(m\) gives

\[
 h_m(z)=\mathbb E\left[J_{Q_m}(z)-\int J_{Q_m}\,d\mu\right]+e_m(z),
 \qquad \sup_z\|e_m(z)\|_H\le4M_*/m.
 \tag{C.4.8.R21}
\]

The laws \(Q_m\to\mu\) in \(W_1\) in probability. Assumption (C.4.8.R4), preserved near \(\mu\) by localization, and the globally bounded first kernel imply

\[
 \mathbb E\|J_{Q_m}-J_\mu\|_{L^2(\mu;H)}^2\longrightarrow0.
\]

To justify the expectation, the norm tends to zero in probability by continuity and is uniformly bounded; splitting at any fixed threshold proves convergence of its expectation. Jensen's inequality in (C.4.8.R21), together with \(\mu J_\mu=0\), now proves

\[
 \|h_m-J_\mu\|_{L^2(\mu;H)}\longrightarrow0.
 \tag{C.4.8.R22}
\]

###### The exact remainder identity

The Hoeffding decomposition gives

\[
 T_m-G(\mu)=b_m+m^{-1}\sum_i h_m(Z_i)+R_m^{\rm H}.
\]

Define \(r_m\) by subtracting \(m^{-1}\sum_iJ_\mu(Z_i)\). The bias, higher-order component, and centered one-coordinate sum are mutually orthogonal in \(L^2\). Independence of the summands gives the exact identity

\[
 m\mathbb E\|r_m\|_H^2
   =m\|b_m\|_H^2+m\mathbb E\|R_m^{\rm H}\|_H^2
                         +\|h_m-J_\mu\|_{L^2(\mu;H)}^2.
 \tag{C.4.8.R23}
\]

The first two terms are at most \(6M_*^2/m\) in total by (C.4.8.R17) and (C.4.8.R20), and the last tends to zero by (C.4.8.R22). This proves (C.4.8.R5). No quantitative modulus in (C.4.8.R4) is needed.

On \(\{\mu_m\in V\}\), any extension \(\widehat F\) in the statement equals \(\widetilde F\). Equation (C.4.8.R16) therefore proves the transfer in probability. If \(\widehat F\) is bounded, multiplying its squared uniform difference from \(\widetilde F\) by \(m\mathbb P(\mu_m\notin V)\) proves (C.4.8.R6). This completes the sampling expansion and its localization claims.

###### Covariance, spatial tests, and the Hilbert CLT

Set \(X=I_\mu(Z)\). It is centered and square integrable by (C.4.8.R10). The operator \(C_\mu h=\mathbb E[\langle X,h\rangle X]\) is positive and self-adjoint. For any orthonormal basis \((e_j)\), Tonelli and Parseval give

\[
 \sum_j\langle C_\mu e_j,e_j\rangle
       =\mathbb E\sum_j|\langle X,e_j\rangle|^2
       =\mathbb E\|X\|_H^2<\infty.
\]

Thus \(C_\mu\) is trace class and has the trace in (C.4.8.R7). Its nonnegative eigenvalues \(\lambda_j\), with an orthonormal eigenbasis supplemented in its kernel if needed, define a centered Gaussian \(\mathcal G=\sum_j\sqrt{\lambda_j}\,N_je_j\), where the \(N_j\) are independent standard normals. Summability of \(\lambda_j\) gives convergence in \(L^2(H)\), and its covariance is \(C_\mu\). Degenerate covariance is allowed.

Here is a direct projection proof of the Hilbert CLT. Put \(S_m=m^{-1/2}\sum_iI_\mu(Z_i)\). For any scalar projection \(Y=\langle X,h\rangle\), centering and finite variance give

\[
 \mathbb E e^{itY/\sqrt m}
       =1-\frac{t^2\mathbb EY^2}{2m}+o(m^{-1}).
\]

For the remainder, set \(q(u)=e^{iu}-1-iu+u^2/2\). Then \(q(u)=o(u^2)\) at zero and \(|q(u)|\le C u^2\) for all real \(u\). For fixed \(t\), \(mq(tY/\sqrt m)\to0\) pointwise and its absolute value is at most \(Ct^2Y^2\); dominated convergence proves the displayed expansion. Taking the \(m\)-th power proves the scalar Gaussian characteristic-function limit. Applied to every linear combination of a fixed finite number of coordinates, this proves the finite-dimensional CLT.

For a finite-dimensional orthogonal projection \(\Pi_N\) increasing to the identity, independence and centering give

\[
 \mathbb E\|(1-\Pi_N)S_m\|_H^2
       =\mathbb E\|(1-\Pi_N)X\|_H^2\longrightarrow0
\]

uniformly in \(m\). The Gaussian has the same tail second moment. For any bounded 1-Lipschitz function on \(H\), replacing its argument by \(\Pi_N\) changes either expectation by at most the square root of that tail second moment. Let \(m\to\infty\) at fixed \(N\), using the finite-dimensional conclusion, and then let \(N\to\infty\). This proves weak convergence \(S_m\Rightarrow\mathcal G\) on the separable Hilbert space. Equation (C.4.8.R5) supplies an error tending to zero in \(L^2\) after multiplication by \(\sqrt m\), so proves the first part of (C.4.8.R8). Cauchy--Schwarz, \(\mathbb E\|S_m\|^2=\operatorname{tr}C_\mu\), and (C.4.8.R5) prove its second part.

If \(H=L^2(\mathbb S^1,\lambda)\) for a finite circle measure \(\lambda\), these statements apply to spatial tests. For \(\psi_1,\ldots,\psi_k\in H\), the limiting covariance matrix of the integrals against these tests is

\[
 \Sigma_{ab}=\int_{\mathcal Z}
   \left(\int_{\mathbb S^1}I_\mu(z)(x)\psi_a(x)\,\lambda(dx)\right)
   \left(\int_{\mathbb S^1}I_\mu(z)(x)\psi_b(x)\,\lambda(dx)\right)
      \mu(dz)=\langle C_\mu\psi_a,\psi_b\rangle_H.
 \tag{C.4.8.R24}
\]

A jointly measurable representative of \(I_\mu\in L^2(\mu;H)\) defines the spatial covariance kernel

\[
 c_\mu(x,x')=\int I_\mu(z)(x)I_\mu(z)(x')\,\mu(dz)
 \tag{C.4.8.R25}
\]

as an element of \(L^2(\lambda\otimes\lambda)\): the integrand's norm in that space is \(\|I_\mu(z)\|_H^2\), which is integrable. Its integral operator is \(C_\mu\), by Fubini and Cauchy--Schwarz. Formula (C.4.8.R24) concerns continuous linear spatial tests; point evaluation requires additional regularity beyond \(L^2\).

All statements treat \(F\) and its kernel as deterministic. If they retain a random initialization environment independent of the samples, the theorem applies conditional on that environment when its hypotheses hold there. An unconditional Gaussian limit additionally requires the conditional covariance to be deterministic; otherwise the conditional limits generally form a Gaussian mixture.

##### C.4.8.4. Covariance and finite-network interpretation

###### Sampling and the mean-square strengthening


Apply the sampling lemma in C.4.8.3 to the actual map on
\(\{Q:W_1(Q,\nu_*)<\delta_Y/2\}\), with kernel (C.4.8.P9)--(C.4.8.P11) and second
difference bound (C.4.8.P12). For each fixed \(\mu\) in the smaller requested
ball, choose a \(W_1\)-ball around \(\mu\) whose closure is inside this
analytic region. The lemma's finite-continuous-test cutoff defines a global
bounded map \(G_\mu\), equal to \(F\) near \(\mu\), with the same actual
influence there. Its proof gives
\[
 m\mathbb E\left\|G_\mu(\mu_m)-F(\mu)
                  -\frac1m\sum_iI_\mu(Z_i)\right\|_H^2\to0,
 \qquad
 \Pr\{G_\mu(\mu_m)\ne\overline F(\mu_m)\}\le C_\mu e^{-c_\mu m}.    \tag{C.4.8.P14}
\]
The mismatch bound refers to the cutoff's finite-test neighborhood, which
lies inside \(U_Y\). Both maps are uniformly bounded, so
\[
 m\mathbb E\|G_\mu(\mu_m)-\overline F(\mu_m)\|_H^2
                         \le C_\mu m e^{-c_\mu m}\to0.
\]
This proves (C.4.8.P4) with exactly the extension (C.4.8.P3). In particular empirical
laws outside \(U_Y\) are exponentially rare and do not change any asserted
limit. No labels on the testing circle have been introduced.

For arbitrary \(g,h\in H\), the covariance acts as
\[
 \langle\Sigma_\mu g,h\rangle_H
   =\int\langle I_\mu(z),g\rangle_H
                \langle I_\mu(z),h\rangle_H\,d\mu(z).                 \tag{C.4.8.P15}
\]
Thus the joint limiting fluctuations of the spatial averages against any
finite collection of tests are centered Gaussian with these covariances.
Since the field is continuous and bounded on the compact atom/input product,
one may equivalently use the continuous kernel
\[
 K_\mu(x,x')=\int I_\mu(z)(x)I_\mu(z)(x')\,d\mu(z),
\quad (\Sigma_\mu g)(x)=\int K_\mu(x,x')g(x')\,d\rho(x').             \tag{C.4.8.P16}
\]
Fubini is justified by boundedness and the finite measures. The operator is
positive, self-adjoint and trace class, with
\(\operatorname{Tr}\Sigma_\mu=\int\|I_\mu(z)\|_H^2d\mu(z)\).
No diagonal form, positive rank, or nondegeneracy is imposed.

The sampling lemma proves the Hilbert CLT, giving (C.4.8.P5). It also gives the
separate strengthening requested here without further label or density
assumptions: put \(S_m=m^{-1}\sum_iI_\mu(Z_i)\). Independence and centering
give \(\mathbb E\|S_m\|_H^2=\operatorname{Tr}\Sigma_\mu/m\). By
Cauchy--Schwarz and (C.4.8.P4),
\[
 m|\mathbb E\langle S_m,r_m\rangle_H|
 \le\sqrt{\operatorname{Tr}\Sigma_\mu}\,
                \sqrt{m\mathbb E\|r_m\|_H^2}\to0.
\]
Expanding the squared norm therefore proves
\[
 \mathbb E\|\overline F(\mu_m)-F(\mu)\|_H^2
                 =\frac{\operatorname{Tr}\Sigma_\mu}{m}+o(m^{-1}).   \tag{C.4.8.P17}
\]
The bounded extension and exponential exceptional-event estimate are essential
parts of this statement. It is not a moment theorem for finite-width errors.

###### Actual finite gradient flow, including exceptional laws

For every finite labeled law and every finite initialized array, the smooth
finite-dimensional physical GF exists through \(T\). The following bounds
also cover laws outside \(U_Y\). Write \(c_{n,0}\) for the actual initialized
readout and \(A_n=A_{n,0}+K_n\). Use ordinary Euclidean vector norms,
Frobenius matrix norms and spectral action norms throughout this finite
paragraph, with all normalization factors displayed. In particular
\(w_n\in\mathbb R^{n\times2}\) contains the full first rows. The exact
middle update and its rank identity give
\[
 \dot K_n=-\frac2n\int r\Delta h^T\,d\mu_m,\qquad
 \left\|\frac{\Delta h^T}{n}\right\|_F
       =\frac{\|\Delta\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n},
\]
and consequently
\[
 \|\dot K_n\|_F\le2\int |r|
       \frac{\|\Delta\|_2}{\sqrt n}\frac{\|h\|_2}{\sqrt n}\,d\mu_m.
\]
The bounded gates imply \(\|h\|_2/\sqrt n\le1\),
\(\|\Delta\|_2/\sqrt n\le\|c_n\|_2/\sqrt n\), and
\(|r|\le\|c_n\|_2/\sqrt n+Y\). Applying the same bounds to the two
end-block equations yields
\[
 \frac{\|\dot c_n\|_2}{\sqrt n}
     \le2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right),\qquad
 \|\dot K_n\|_F
     \le2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right)
                \frac{\|c_n\|_2}{\sqrt n},
\]
\[
 \frac{\|\dot w_n\|_F}{\sqrt n}
 \le2\left(\frac{\|c_n\|_2}{\sqrt n}+Y\right)
       (\|A_{n,0}\|_{\rm op}+\|K_n\|_F)
                      \frac{\|c_n\|_2}{\sqrt n}.             \tag{C.4.8.P18}
\]
The first inequality gives
\[
 \frac{\|c_n(t)\|_2}{\sqrt n}
 \le\left(\frac{\|c_{n,0}\|_2}{\sqrt n}+Y\right)e^{2t}-Y.
\]
Integration then bounds \(K_n\) and \(w_n\) on each finite time interval.
These constants may depend on the initialized array and \(n\); no uniform
bound is needed here. A solution of a locally Lipschitz finite-dimensional
equation that remains bounded on each such interval extends through its
endpoint: on a containing compact ball the vector field is bounded and locally
Lipschitz, giving a Cauchy endpoint and a local continuation. This proves global
finite-time existence. Smooth dependence on the finite data and initialization
gives measurability of the \(H\)-valued prediction statistic; the bounds ensure
the local dependence can be continued through \(T\).

Fix \(m\), and condition on \((Z_1,\ldots,Z_m)\). On the event
\(E_m=\{\mu_m\in U_Y\}\), this is a separately fixed finite training law,
and independence leaves the specified initialization distribution unchanged.
C.4.7.NW1 therefore gives
\[
 \|f_{n,\mu_m}(T,\cdot)-F(\mu_m)\|_H\to0
 \quad\hbox{in initialization probability, conditionally on each such law}.
\]
For every fixed \(m\), bounded convergence after conditioning implies
\[
 \mathbb E\left[\mathbf1_{E_m}
     \min\{2,\sqrt m\|f_{n,\mu_m}(T)-F(\mu_m)\|_H\}\right]\to0.    \tag{C.4.8.P19}
\]
On \(E_m^c\), the difference of any two bounded-Lipschitz test values is at
most two. No width limit on that event is asserted. With
\(X_{n,m}=\sqrt m(f_{n,\mu_m}(T)-F(\mu))\) and
\(X_m=\sqrt m(\overline F(\mu_m)-F(\mu))\), (C.4.8.P19) yields
\[
 \limsup_{n\to\infty}
 d_{\rm BL}(\operatorname{Law}(X_{n,m}),\operatorname{Law}(X_m))
                         \le2\Pr(E_m^c).                             \tag{C.4.8.P20}
\]
The right-hand side tends to zero exponentially by (C.4.8.P14). The triangle
inequality, (C.4.8.P5), and then \(m\to\infty\) prove (C.4.8.P6). This argument keeps
the actual finite random initial readout and invokes no finite-network tangent
limit, no rate in width, and no simultaneous width/sample scaling.

#### C.4.9. Nonlinear prediction selection during a finite added-data episode

This result concerns the whole-circle prediction selected by actual nonlinear
training after a fixed amount of learning from a component whose mixture weight
vanishes. The physical training law is unchanged throughout each run. The
limiting episode is a constrained gradient flow with evolving hidden features;
its initialization is the established fitted reference state, obtained from
the original initialization by a justified initial-layer limit.

##### Model, determining equation and theorem

Use the canonical bias-free network with two tanh hidden layers,

\[
 u=x/\sqrt2\in S^1,\quad h^1_n=\tanh(W^1_nu),\quad
 h^2_n=\tanh(W^2_nh^1_n),\quad f_n=(W^3_n)^Th^2_n/n.
\]

Initialize every entry and block independently, centered Gaussian with stored
variances \((1,1/n,1/n^2)\). Use mobilities \((n,1,n)\), the unhalved mean square,
and physical gradient flow. Keep the actual finite initial Gaussian readout.
Set

\[
 \nu_*={1\over2}\delta_{(\sqrt2e_1,1)}
             +{1\over2}\delta_{(\sqrt2e_2,-1)},\qquad
 \mu_{\epsilon,\alpha,y}=(1-\epsilon)\nu_*+\epsilon\nu_{\alpha,y},
\]
\[
 \nu_{\alpha,y}=\delta_{(\sqrt2u_\alpha,y)},\quad
 u_\alpha=(\cos\alpha,\sin\alpha),\quad
 |\alpha-\pi/4|\le1/1216,\quad 3/8\le y\le5/8.
 \tag{NS1}
\]

This fixed compact parameter rectangle has nonempty interior in location and
label. All its added inputs are nonorthogonal to both reference inputs. Its
labels are admitted for every fixed \(Y\ge1\). All actual mixture flows begin
at the original Gaussian initialization and use that same mixture throughout.

Let \(H_1=L^2(\Omega_1)\) and \(H_2=L^2(\Omega_2)\) be the canonical generated
Gaussian action spaces, with initialized action \(A_0:H_1\to H_2\) and its true
Hilbert adjoint. Their construction is by the joint Gaussian finite-program
law, including the response to every reused forward and transpose call.
The raw state is \(\theta=(w,K,c)\), where
\(w\in L^2(\Omega_1;\mathbb R^2)\), \(K:H_1\to H_2\) is Hilbert–Schmidt,
\(c\in H_2\), and \(A=A_0+K\). Only the increment is Hilbert–Schmidt.
Use the squared metric \(\|\Delta w\|_2^2+\|\Delta K\|_{HS}^2+\|\Delta c\|_2^2\).

The established reference endpoint \(\theta_\dagger\) is explicitly determined
from \((g,A_0,0)\), \(g\sim N(0,I_2)\), by the reference feature equation:
write \(\phi=\tanh\), \(H^1(u)=\phi(w\cdot u)\), \(H^2(u)=\phi(AH^1(u))\),
\(\delta(u)=c\phi'(AH^1(u))\), and \(Q(u)=A^*\delta(u)\). Starting at
\((w,K,c)=(g,0,0)\), solve

\[
 \partial_s w={1\over2}\sum_{a=1}^2 y_a\phi'(w\cdot e_a)Q(e_a)e_a,
 \quad \partial_sK={1\over2}\sum_{a=1}^2y_a\delta(e_a)\otimes H^1(e_a),
 \quad \partial_sc={1\over2}\sum_{a=1}^2y_aH^2(e_a),
\]

where \(y_1=1,y_2=-1\), and stop at the unique first \(s=s_\dagger\le10\)
with \(\langle c,(H^2(e_1)-H^2(e_2))/2\rangle=1\). The global clock construction
in C.4.5 proves well-posedness of this prescription and identifies it with the
physical reference endpoint. Put \(F_*(\sqrt2u)=f_{\theta_\dagger}(u)\).
The zero readout in this population initialization is the limit of the actual
finite readout and imposes no finite-network reset.

For every state used below, define its current raw prediction gradient

\[
 g_\theta(u)=\left(
   \phi'(w\cdot u)Q(u)u,\quad \delta(u)\otimes H^1(u),\quad H^2(u)
                    \right),
\]
\[
 G_\theta=(g_\theta(e_1),g_\theta(e_2)),\quad
 M_\theta=G_\theta^*G_\theta,\quad
 \Pi_\theta=I-G_\theta M_\theta^{-1}G_\theta^*.
 \tag{NS2}
\]

The inverse exists throughout the asserted episode. The determining evolution
and reconstruction are

\[
 {d\bar\theta_{\alpha,y}\over d\tau}
   =-2\big(f_{\bar\theta_{\alpha,y}}(u_\alpha)-y\big)
                  \Pi_{\bar\theta_{\alpha,y}}g_{\bar\theta_{\alpha,y}}(u_\alpha),
 \qquad \bar\theta_{\alpha,y}(0)=\theta_\dagger,
 \tag{NS3}
\]
\[
 P_{\alpha,y}(\tau,\sqrt2u)
   =\left\langle\bar c(\tau),
      \tanh\big((A_0+\bar K(\tau))\tanh(\bar w(\tau)\cdot u)\big)\right\rangle.
 \tag{NS4}
\]

Every coefficient in (NS3) is computed from the specified current state and
the established initialized action. In particular its projection and all
hidden features are recomputed along the evolution. There is no coefficient
supplied by an unknown changed-law trajectory.

**Theorem.** There exist \(\epsilon_0,\tau_0,a,j>0\), uniform over the parameter
rectangle (NS1), with these properties.

1. Equation (NS3) has a unique strong solution on \([0,\tau_0]\) in a fixed
   neighborhood of \(\theta_\dagger\). It is constructed on the canonical
   initialized carrier with its full retained reference history. It preserves
   the two reference predictions exactly. It determines (NS4) over the whole
   circle.

2. For every \(0<\epsilon<\epsilon_0\), the original-initialization mixture
   population GF exists and is unique through \(T_\epsilon=\tau_0/\epsilon\).
   For every \(0<\tau_-<\tau_0\),
   \[
    \sup_{(\alpha,y)}\sup_{\tau_-\le\tau\le\tau_0}
      \|\theta_{\mu_{\epsilon,\alpha,y}}(\tau/\epsilon)
                    -\bar\theta_{\alpha,y}(\tau)\|_{\rm raw}\longrightarrow0.
    \tag{NS5}
   \]
   The same convergence holds for predictions uniformly over the entire
   circle and for the finite named hidden observations stated below.
   The exclusion of \(\tau=0\) records the genuine initial layer; no pretraining
   stage is imposed on any actual run.

3. With \(R_\nu(f)=\int(f(x)-y)^2\,d\nu(x,y)\), the selected finite-episode
   prediction satisfies
   \[
      R_{\nu_{\alpha,y}}(F_*)
       -R_{\nu_{\alpha,y}}(P_{\alpha,y}(\tau_0))\ge a.
    \tag{NS6}
   \]
   This is risk on the added component itself, without its factor \(\epsilon\).
   For \((v_1,v_2,v_3)=(e_1,e_2,u_\alpha)\), its paired upper-hidden change is
   \[
    {1\over3}\sum_{i=1}^3
      \|H^2_{\bar\theta_{\alpha,y}(\tau_0)}(v_i)
                         -H^2_{\theta_\dagger}(v_i)\|_2^2\ge j.
    \tag{NS7}
   \]
   Both states use the same initialized primitives. The hidden displacement
   therefore measures adaptation caused by the added law after reference fitting.

4. For every separately fixed \(\epsilon\in(0,\epsilon_0)\) and law in (NS1),
   actual finite GF converges in probability to the mixture population
   prediction in \(C([0,T_\epsilon]\times\sqrt2S^1)\), with the joint
   same-layer internal observations needed for paired hidden measurements.
   Consequently, for every such fixed law and every \(\eta>0\),
   \[
    \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
     \Pr\!\left\{\sup_x|f_{n,\mu_\epsilon}(T_\epsilon,x)
                       -P_{\alpha,y}(\tau_0,x)|>\eta\right\}=0.
    \tag{NS8}
   \]
   Train a reference network with the same initial arrays, including readout,
   and define the directly paired finite observable
   \[
    J_{2,n,\epsilon}={1\over3n}\sum_{i=1}^3
      \|h^2_{n,\mu_\epsilon}(T_\epsilon,\sqrt2v_i)
                    -h^2_{n,\nu_*}(T_\epsilon,\sqrt2v_i)\|_2^2.
    \tag{NS9}
   \]
   In the same iterated order it converges in probability to (NS7)'s
   population quantity. In particular the probability that the added-risk
   gain is at least \(a/2\) and \(J_{2,n,\epsilon}\ge j/2\) tends to one.

The constants need not be numerically practical. The theorem asserts one fixed,
nonzero slow-time episode, not a final endpoint for the changed law. It gives
no simultaneous width/contamination rate and no raw-GD extension. The scale
\(\tau=\epsilon t\) follows from the stable reference-residual equations and
the remaining tangential force, as proved below.

##### Proof architecture

The proof first establishes a Gaussian source bound for a small perturbation
of the reference in integrated control mass, uniformly in physical horizon.
A protected Gaussian-row argument then proves strict endpoint conditioning.
Together these facts construct (NS3) and continue the actual mixture through
(NS5). An exact residual identity proves selection on the slow clock.
A fixed-readout hidden contrast and the exact risk derivative yield (NS6)–(NS7).
Finally a same-array, one-reference cutoff comparison identifies actual finite
GF and the paired observations in (NS8)–(NS9).

Equation labels and auxiliary constants are local to each proof unit below.
All finite vector norms are ordinary Euclidean norms; normalization factors
are displayed in the finite-state metric.


##### Proof unit A. Uniform source control in accumulated training force

###### A.1. Statement with the exact control and approximation conventions

Keep the canonical two-hidden tanh carrier, Gaussian action \(A_0\)
with its actual adjoint, \(w(0)=g\sim N(0,I_2)\), \(K(0)=0,c(0)=0\),
and \(A=A_0+K\). The raw Hilbert metric is
\[
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\|\Delta K\|_{\rm HS}^2+\|\Delta c\|_2^2.
\]
For each \(u\in S^1\), define
\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad
 H^2(u)=\phi(Z^2(u)),\quad
 \Delta^{(2)}(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^{(2)}(u),
\]
\[
 g_u(\theta)=
 \bigl(\phi'(w\cdot u)Q(u)u,\,
       \Delta^{(2)}(u)\otimes H^1(u),\,H^2(u)\bigr),\qquad\phi=\tanh.
 \tag{CT1}
\]
This is the actual raw gradient of the scalar prediction. It retains
the original architecture and both orientations of the reused matrix.

Fix finitely many directions \(u_1=e_1,u_2=e_2,u_3,\ldots,u_J\)
on the circle. They need not be distinct, separated, or orthogonal.
For a physical interval \(I=[0,T]\), where \(T\) is arbitrary and may
also be infinite, let \(a_j(t)\) be deterministic integrable controls.
The comparison controls are the complete reference history
\[
 a_{*,1}(t)=e_*(t),\qquad a_{*,2}(t)=-e_*(t),\qquad
 a_{*,j}(t)=0\quad(j\ge3),
 \qquad e_*=1-f_*(e_1)>0.
 \tag{CT2}
\]
Its total absolute mass is the reference feature length, at most
\(s_\dagger\le10\). Only finiteness of this bound is necessary below.
The controlled equation is
\[
 \theta'(t)=\sum_{j=1}^J a_j(t)g_{u_j}(\theta(t)).
 \tag{CT3}
\]

**Controlled source-tube theorem.** There are \(\delta>0\), \(h_0>0\),
\(B<\infty\), \(M<\infty\), and \(c>0\), depending only on the
reference feature segment and the canonical model, with the following
properties. They are independent of \(T\), the number of time steps,
and the minimum nonzero control coefficient.

Assume
\[
 q:=\int_I\sum_j|a_j(t)-a_{*,j}(t)|\,dt\le\delta.
 \tag{CT4}
\]
Use the common dominating measure
\[
 ds=\sum_j(|a_j(t)|+|a_{*,j}(t)|)\,dt.
 \tag{CT5}
\]
On a finite partition in this control clock with maximal interval
length at most \(h_0\), take exact integrated coefficients
\[
 \gamma_{kj}=\int_{I_k}a_j(t)\,dt,\qquad
 \bar\gamma_{kj}=\int_{I_k}a_{*,j}(t)\,dt
 \tag{CT6}
\]
and run raw Euler with these coefficients and the same initialization.
Every passive backward-source row at every node satisfies
\[
 |\beta_{ku,ku}|+\sum_{s<k,j}|\beta_{ku,sj}|\le B,\qquad
 \sup_{u\in S^1}\tau_R(Q_k(u))\le M e^{-cR^2},\quad R\ge1.
 \tag{CT7}
\]
The corresponding readout tails have the same bound after enlarging
\(M\). Current passive slots are distinguished as described below.
Zero controls and padding are permitted. The estimate retains all
source slots from the entire reference history.

The assertion here is a finite-program source bound. Proof unit C constructs
the required strong nonlinear trajectories from these bounds; proof unit D
identifies actual finite GF. No probability supremum over random finite-network
feedback controls is asserted by this source estimate.

###### A.2. Why control time is a legitimate common parameter

Set \(L_*=10\), reducing it to the actual reference bound if desired.
From (CT4),
\[
 \int_I\sum_j|a_j|\le L_*+q,\qquad
 S:=\int_I\sum_j(|a_j|+|a_{*,j}|)\le2L_*+q.
 \tag{CT8}
\]
The increasing cumulative distribution of (CT5) is continuous.
Where its density is positive, divide each control by that density;
the resulting coefficients \(b_j(s),\bar b_j(s)\) satisfy
\[
 \sum_j(|b_j(s)|+|\bar b_j(s)|)=1
 \quad\hbox{for almost every }s.
 \tag{CT9}
\]
Flat parts carry zero control and zero state change. A generalized
inverse gives the control-clock integral equations, and substitution
in the Lebesgue integral recovers physical time. Equivalently all
formulas can first be proved for step functions and passed in \(L^1\).
This change introduces no optimizer or future state information:
the controls in this theorem are prescribed deterministic functions.

For coefficient arrays define
\[
 m_{kj}=|\gamma_{kj}|+|\bar\gamma_{kj}|,\quad
 m_k=\sum_jm_{kj},\quad
 q_{\rm disc}=\sum_{k,j}|\gamma_{kj}-\bar\gamma_{kj}|.
 \tag{CT10}
\]
Then \(\sum_km_k\le2L_*+q\), \(q_{\rm disc}\le q\), and
\(m_k\le h_0\). A slot with \(m_{kj}=0\) can be omitted or retained
with zero coefficient. For a nonzero slot \(p=(s,j)\), put
\[
 e_p=\frac{|\gamma_p-\bar\gamma_p|}{m_p}\in[0,1],
 \qquad \sum_pm_pe_p=q_{\rm disc}.
 \tag{CT11}
\]
There is no division by a reference coefficient. In particular
(CT11) handles a genuinely new direction, whose reference control
is zero, and vanishing actual controls.

###### A.3. Exact named-source equations and inactive slots

At each node all active forward calls precede its reverse calls.
Both compared programs use the same training-slot index set.
For a passive current query append one otherwise unused forward and
reverse pair; call its one direct forward slot \(ku\).
Old unused passive queries may be discarded because their values
were never used by an update. Their formal derivatives in every
later state are zero. They do not accumulate a diagonal response
at subsequent times.

With the deterministic controls, contractions, covariances and
response coefficients frozen under named differentiation, the
source equations are
\[
 \begin{aligned}
 w_{k+1}&=w_k+\sum_j\gamma_{kj}
             \phi'(w_k\cdot u_j)Q_{kj}u_j,\\
 c_{k+1}&=c_k+\sum_j\gamma_{kj}\phi(Z^2_{kj}),\\
 K_{k+1}&=K_k+\sum_j\gamma_{kj}\Delta^{(2)}_{kj}\otimes H^1_{kj},
 \end{aligned}                                                   \tag{CT12}
\]
\[
 \begin{aligned}
 Z^2_{ku}&=\xi_{ku}+\sum_{p<k}F_{ku,p}\Delta^{(2)}_p,&
 F_{ku,p}&=\alpha_{ku,p}
                  +\gamma_p\mathbb E_1[H^1_{ku}H^1_p],\\
 Q_{ku}&=\zeta_{ku}+\sum_{p\le k}D_{ku,p}H^1_p,&
 D_{ku,p}&=\beta_{ku,p}
          +{\bf1}_{p<k}\gamma_p\mathbb E_2[\Delta^{(2)}_{ku}\Delta^{(2)}_p],
 \end{aligned}                                                   \tag{CT13}
\]
where \(p<k\) means an earlier time index. At the passive current
time the sum has its one distinguished slot; at an active output
all other current beta coefficients are zero. Specifically
\[
 \alpha_{ku,p}=\mathbb E_1[\partial_{\zeta_p}H^1_{ku}],\qquad
 \beta_{ku,p}=\mathbb E_2[\partial_{\xi_p}\Delta^{(2)}_{ku}],\qquad
 \beta_{ku,ku}=\mathbb E_2[c_k\phi''(Z^2_{ku})].
 \tag{CT14}
\]
An identical input does not merge its formal current name with an
earlier source. A singular covariance also does not merge those
names.

For lower pulses \(v_{k;p}=\partial_{\zeta_p}w_k\),
\[
 \begin{aligned}
 v_{k+1;p}=v_{k;p}+\sum_j\gamma_{kj}u_j\bigg[
 &\phi''(w_k\cdot u_j)Q_{kj}(u_j\cdot v_{k;p})\\
 &+\phi'(w_k\cdot u_j)
 \left({\bf1}_{(k,j)=p}
   +\sum_{q\le k}D_{kj,q}\phi'(w_{t(q)}\cdot u_q)
                                    (u_q\cdot v_{t(q);p})\right)
 \bigg].
 \end{aligned}                                                   \tag{CT15}
\]
For upper pulses,
\[
 \begin{aligned}
 C_{k;p}&=\sum_{q<k}\gamma_q\phi'(Z^2_q)U_{q;p},\\
 U_{ku;p}&={\bf1}_{ku=p}+\sum_{q<k}F_{ku,q}V_{q;p},\\
 V_{ku;p}&=\phi'(Z^2_{ku})C_{k;p}
                   +c_k\phi''(Z^2_{ku})U_{ku;p}.
 \end{aligned}                                                   \tag{CT16}
\]
These formulas follow directly by differentiating (CT12)–(CT13);
they are also C.4.7.N7–N8 without its residual specialization.
They do not differentiate a residual or any covariance.

If \(\gamma_p=0\), a lower pulse has no injection and remains zero.
An upper pulse at that time can affect its own current \(V\), but
its influence on later states is zero: the update coefficient is
zero and its lower F coefficient into all later queries is zero.
Chronological induction in (CT15)–(CT16) proves this assertion.
Thus retaining arbitrarily many zero slots changes neither the cap
nor the later coefficient rows.

The two programs are realized jointly using the same initialized
arrays and the common source construction III.F. The source
covariances, including cross-program entries, satisfy
\[
 \|\xi_i-\bar\xi_i\|_{L^p}
 =\|N(0,1)\|_{L^p}\|H^1_i-\bar H^1_i\|_2,\qquad
 \|\zeta_i-\bar\zeta_i\|_{L^p}
 =\|N(0,1)\|_{L^p}\|\Delta^{(2)}_i-\bar\Delta^{(2)}_i\|_2.
 \tag{CT17}
\]
This is subtraction of the two uncentered-input Gram covariances,
not a Lipschitz assertion about matrix square roots. To construct the
joint law one takes the finite union of the two programs.
The scalar expression of either branch depends only on its own
named slots and shared roots; extra calls in the other branch have
zero formal derivatives there. The cross covariances nevertheless
couple the two Gaussian lists. Their entire old source history is
present in (CT13)–(CT17). No source is refreshed at a splice or restart.

###### A.4. A horizon-independent reference raw anchor

The reference coefficients obey
\(\bar\gamma_{k1}=-\bar\gamma_{k2}\ge0\) and have total mass at most
\(L_*\). Remove zero steps and put \(h_k=2\bar\gamma_{k1}\).
The reference raw program is exactly feature Euler with total
feature length at most \(L_*\); physical pauses have disappeared.

Here is a proof of its uniform raw source cap. This also isolates
the anchor needed below; no nearby-law source estimate enters.
Let \(F'(w)=1/\phi'(w)\), and \(J_X=\phi'(J)\), \(J(0,g)=g\).
Feature clock Euler is
\[
 X_{a,k+1}=X_{a,k}+\tfrac12h_ky_aQ_{ka},\quad
 K_{k+1}=K_k+\tfrac12h_k\sum_ay_a\Delta^{(2)}_{ka}\otimes H^1_{ka},
 \quad c_{k+1}=c_k+\tfrac12h_k(H^2_{k1}-H^2_{k2}),
 \tag{CT18}
\]
with \(w_a=J(X_a,g_a)\), \(y_1=1,y_2=-1\).
Direct sums give \(\|c_k\|_\infty\le L_*\) and
\(\|K_k\|_{\rm HS}\le L_*^2/2\), hence a bounded action.
The lower-feature map has clock derivative norm at most one,
including a passive direction:
\[
 H^1(u)=\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2)).
 \tag{CT19}
\]
Its derivative in \(X\) has components bounded by \(|u_j|\).

Subtract two clock programs after one fresh pulse.
The forward differences are bounded by the clock difference plus
the HS increment difference. The upper gate subtraction obeys
\[
 \|c\phi'(Z)-\bar c\phi'(\bar Z)\|_2
 \le\|c-\bar c\|_2+2L_*\|Z-\bar Z\|_2.
 \tag{CT20}
\]
Actual adjunction and the rank difference identity give a fixed
Lipschitz constant \(L_{\rm cl}<\infty\) for all three clock
velocities. Thus the post-pulse amplification is at most
\(E_{\rm cl}=e^{L_{\rm cl}L_*}\), uniformly in the mesh.
A reverse-answer pulse at old slot \(p\) changes the clock by at
most \(|\bar\gamma_p|\) times its RMS. A forward-answer pulse
changes its activation and gate, and hence all immediate updates,
by at most \(C|\bar\gamma_p|\) times its RMS. The readout supremum
and action bounds survive the forcing: the readout still updates
by bounded tanh functions and the middle updates have norm bounded
by their control mass times \(L_*\).
Consequently the later passive first-feature response and upper
backward response are at most \(C|\bar\gamma_p|\).

At each fixed graph, add a fresh standard Gaussian \(z\) at that
complete answer with amplitude \(q\), take the fixed-program width
limit first, and pair the observed difference with \(z\).
In its source expression, \(z\) occurs only as
\({\rm slot}+qz\); conditional Gaussian integration by parts yields
\(\mathbb E[zV^q]=q\mathbb E[\partial_{\rm slot}V^q]\).
The unforced output is independent of \(z\).
The fixed-graph source coefficients are continuous at zero forcing:
clip the root, use the bounded clock derivatives, retain the
bounded readout, and remove the clip by the finite causal
covariance-square-root argument in C.4.5.2.R5–R7.
Each fixed graph has a deterministic source-derivative bound
independent of the root clip. Hence its derivative expectations
converge. Taking \(q\to0\) after width gives
\[
 |\alpha^{\rm cl}_{ku,p}|+|\beta^{\rm cl}_{ku,p}|
 \le C|\bar\gamma_p|\quad(p<k),\qquad
 |\beta^{\rm cl}_{ku,ku}|\le2L_*.
 \tag{CT21}
\]
This proves a finite \(B_{\rm cl}\) for all prefixes through \(L_*\),
uniformly over passive queries and covariance rank.

Clock Euler converges to the globally existing reference feature
clock equation on \([0,L_*]\), by its bounded-set Lipschitz
comparison and the direct integral equation. The Gaussian source
isometry and (CT21) pass Gaussian-plus-bounded reverse-query
decompositions to this flow. Thus the actual reference feature flow
has active Gaussian tails on this compact feature segment, even
if its length exceeds the fitting endpoint.

Compare reference raw Euler with that existing flow using the
one-reference gradient cutoff estimate. Their discrepancy is
\(\eta_h\to0\) as the largest feature step tends to zero; only
reference-flow tails enter. Clock Euler has the same property.
Under a temporary cap on preceding raw source rows, transform a
raw first-coordinate step to its clock. Its exact defect is
\[
 R_h(w,b)=F(w+hb\phi'(w))-F(w)-hb
 =h^2b^2\phi'(w)^2
       \int_0^1(1-v)F''(w+vhb\phi'(w))\,dv,
 \tag{CT22}
\]
with \(b=y_aQ_a/2\). The elementary hyperbolic bounds give
\[
 |R_h|\le Ch^2b^2e^{2h|b|},\quad
 |\partial_pR_h|
 \le Ch^2e^{2h|b|}(1+h|b|)
       \{b^2|\partial_pw|+|b||\partial_pb|\}.
 \tag{CT23}
\]
The temporary-cap Gaussian decomposition and pulse estimates in
section 5 give all fixed moments of these factors. At the direct
injection step, division by its mass
\(|\bar\gamma_p|=h_s/2\) leaves a bound \(Ch_s\).
At later steps the normalized pulse is bounded in every fixed
moment. Since \(\sum_kh_k^2\le L_*h_{\max}\), the summed
normalized defect is at most \(C_Bh_{\max}\) in \(L^2\).
The summed undifferentiated defect has the same bound.

For completeness the transformed lower pulse recursion has
deterministic propagation
\[
 \chi_{k+1;p}
 =\chi_{k;p}+\sum_a\bar\gamma_{ka}e_a
 \left({\bf1}_{(k,a)=p}
    +\sum_{q\le k}D_{ka,q}J_q\chi_{t(q);p}\right)
    +\partial_pR_k,
 \tag{CT24}
\]
where \(J_q\) is the bounded clock derivative of its first feature.
Clock Euler has the same equation with the last term zero.
Its normalized pulses are pointwise bounded by
\(C\exp(CB_{\rm cl}L_*)\).
Differences of clock gates are \(O(\eta_h)\) in \(L^2\);
the D-row difference is the beta-row difference plus \(C\eta_h\).
Subtract (CT24), divide by \(|\bar\gamma_p|\), sum its defects,
and apply deterministic discrete Gronwall. Summing the resulting
alpha differences over source masses, and then subtracting the
upper equations (CT16), gives
\[
 E_k\le C_B\left(\eta_h+h_{\max}
                   +\sum_{j<k}h_jE_j\right).
 \tag{CT25}
\]
There is no current unknown on the right. Put \(B=B_{\rm cl}+1\);
choose \(h_{\max}\) so that Gronwall makes \(E_k\le1/2\).
At the first potentially failed raw row the past cap suffices
for (CT23)–(CT25), so that row cannot fail.
This proves a reference raw cap \(B_*<\infty\).
Because this argument is on feature length \(\le L_*\), its
constants do not depend on physical horizon or on pauses.
Extra zero-control directions have no past response, by section 3.

###### A.5. Temporary-cap moments and control transport

The estimates here are for arbitrary controlled raw programs,
not just the reference. Set \(M_0=\|A_0\|\le2\), \(L=L_*+1\), and restrict \(q\le1\).
The total absolute coefficient mass is at most \(L\).
Directly from (CT12),
\[
 \|c_k\|_\infty\le L,\quad
 \|K_k\|_{\rm HS}\le L^2/2,\quad
 \|A_k\|\le M_0+L^2/2,\quad
 \|w_k\|_2\le\sqrt2+(M_0+L^2/2)L^2/2.
 \tag{CT26}
\]
These bounds do not assume a cap. Under a temporary cap \(B\),
(CT13) gives
\[
 Q_{ku}=\zeta_{ku}+J_{ku},\qquad
 \mathbb E\zeta_{ku}^2\le L^2,\qquad
 |J_{ku}|\le D_B:=B+L^3.
 \tag{CT27}
\]
For \(Z=\sum_p|\gamma_p||Q_p|\), Jensen and the scalar Gaussian
exponential moment imply
\[
 \mathbb E e^{\lambda Z}
 \le2e^{\lambda LD_B+\lambda^2L^4/2},\qquad\lambda\ge0.
 \tag{CT28}
\]
It follows from (CT15) and \(1+x\le e^x\) that
\[
 \max_{j\le k}|v_{j;p}|
 \le|\gamma_p|\exp(D_BL+2Z).
 \tag{CT29}
\]
Thus all normalized pulses \(v_{\cdot;p}/m_p\) have all fixed
moments, with one common bound. The same holds for the barred
program. In particular
\[
 |\alpha_{ku,p}|\le C_B|\gamma_p|,\qquad
 |F_{ku,p}|\le C_B|\gamma_p|.
 \tag{CT30}
\]
From (CT16), the pointwise sum of the absolute U derivatives is
at most \(e^{C_BL^2}\); the corresponding C and V row sums are
bounded by \(C_B\). For a single old upper pulse, the direct
current V value has size at most \(2L\). Its first later C/F
terms have the factor \(|\gamma_p|\), and the remaining
propagation has total coefficient mass at most \(L\).
Consequently
\[
 |\beta_{ku,p}|\le C_B|\gamma_p|\quad(p<k),\qquad
 \sum_p|V_{ku;p}|+\sum_p|C_{k;p}|+\sum_p|U_{ku;p}|\le C_B.
 \tag{CT31}
\]
The last three bounds are pointwise. The first is deterministic.
These are the single-pulse and row-sum inductions of (CT16);
they do not require a positive lower bound for \(|\gamma_p|\).

Equations (CT27), (CT30), and (CT12) also give all fixed marginal
moments of \(Q,Z^2\) and the time maximum of \(|w|\).
For the latter, use
\(\sup_k|w_k|\le|g|+\sum_p|\gamma_p||Q_p|\).
For \(Z^2\), use its Gaussian source of variance at most one,
(CT30), and \(|\Delta^{(2)}|\le L\).
No \(L^p\) operator estimate beyond \(p=2\) is invoked.

**Raw proximity before the source bootstrap**

For the two programs on the same mesh let
\(d_k=\|\theta_k-\bar\theta_k\|_{(1)}\), the raw sum norm.
Every \(g_u\) has a common raw norm bound by (CT26).
The same-input gradient comparison is
\[
 \|g_u(\theta)-g_u(\bar\theta)\|_{(1)}
 \le C(1+R)d+C\tau_R(\bar Q(u))
 \tag{CT32}
\]
for \(R\ge L\). The upper gate uses bounded \(\bar c\), and
the only unbounded lower gate multiplier is \(\bar Q\).
This is the explicit split on \(|\bar Q|\le R\) and its
complement, followed by the rank difference identity.

Subtract updates as
\[
 \sum_j(\gamma_{kj}-\bar\gamma_{kj})g_{u_j}(\theta_k)
 +\sum_j\bar\gamma_{kj}
                  [g_{u_j}(\theta_k)-g_{u_j}(\bar\theta_k)].
 \tag{CT33}
\]
Only the second term needs tails, and only its two reference axes
occur. Section 4 therefore gives
\[
 \eta:=\max_kd_k\le\Phi(q_{\rm disc}),\qquad
 \Phi(q)\longrightarrow0\quad(q\downarrow0),
 \tag{CT34}
\]
uniformly in admitted meshes. Explicitly before cutoff choice the
bound is \(Ce^{C(1+R)L_*}(q_{\rm disc}+L_*e^{-cR^2})\).
Choose \(R\) proportional to \(\sqrt{\log(e/q_{\rm disc})}\);
at zero discrepancy both recursions are identical.
This proof uses no nearby-program source cap.

**The weighted beta-row comparison**

Define at the same passive output input
\[
 E_k=\sup_u\left(
 |\beta_{ku,ku}-\bar\beta_{ku,ku}|
 +\sum_{p<k}|\beta_{ku,p}-\bar\beta_{ku,p}|\right).
 \tag{CT35}
\]
We prove, under a cap on the preceding rows,
\[
 E_k\le C_B\left(
    \eta^{1/16}+q_{\rm disc}+\sum_{j<k}m_jE_j\right).
 \tag{CT36}
\]
Every constant in this estimate depends on \(B,L\), not on
physical horizon or the number of source slots.

Here are the complete product and mass estimates. Direct
forward/action subtractions and bounded readouts imply uniformly
at matched inputs
\[
 \|\mathrm d H^1\|_2+\|\mathrm d Z^2\|_2
 +\|\mathrm d\Delta^{(2)}\|_2+\|\mathrm d Q\|_2\le C\eta.
 \tag{CT37}
\]
The \(L^{24}\) bounds just proved, interpolated with (CT37), give
an \(L^{12}\) difference bound \(C_B\eta^{1/11}\) for \(w,Q,Z^2\).
For bounded gates their \(L^2\) difference and pointwise bound give
at least \(C_B\eta^{1/6}\). On \(\eta\le1\) each is bounded by
\(C_B\eta^{1/16}\). The explicit products below require at most
three \(L^{12}\) factors, followed by multiplication by an \(L^4\)
integrating factor. No bound on a maximum of query differences
or a larger-moment interpolation exponent is needed.

The D-row difference has the exact decomposition
\[
 \mathrm d D_{i,p}=\Delta\beta_{i,p}
 +{\bf1}_{p<i}\left[
   (\gamma_p-\bar\gamma_p)\mathbb E(\bar\Delta^{(2)}_i\bar\Delta^{(2)}_p)
    +\gamma_p\Delta\mathbb E(\Delta^{(2)}_i\Delta^{(2)}_p)\right].
 \tag{CT38}
\]
Thus its deterministic row sum is at most
\(E_k+C(q_{\rm disc}+\eta)\).

Subtract (CT15). Its linear propagation of the pulse difference
has coefficient at step \(j\) at most
\[
 D_B\sum_a|\gamma_{ja}|
      +2\sum_a|\gamma_{ja}||Q_{ja}|.
 \tag{CT39}
\]
The product of the resulting amplification factors has all fixed
moments by (CT28). Its forcing consists of exactly:
the direct injection difference \(\gamma_p-\bar\gamma_p\);
update coefficient differences; outside gate differences;
the difference of \(Q\); D-row differences (CT38); and the
inside past-gate differences.
An unchanged normalized barred pulse is bounded by the common
random envelope in (CT29). In the first-gate term, subtract
\(\phi''Qv\) as propagation plus
\((\mathrm d\phi'')\bar Q\bar v+\phi''(\mathrm d Q)\bar v\).
In its memory term subtract
\(\phi'\sum D\phi'_qv_q\) into propagation and the three
differences of its outside gate, D, and inside gate.
These exhaust every term.

After division by \(m_p\), the injection cost is \(e_p\).
Coefficient-change costs sum to \(C_Bq_{\rm disc}\), since
every such term is multiplied by \(|\gamma-\bar\gamma|\).
Field/gate costs are bounded by \(C_B\eta^{1/16}\) after
Hölder. For an inside-gate sum, take its \(L^p\) norm by
Minkowski before summing its deterministic D coefficients;
the D-row sum is bounded by \(D_B\).
No maximum of a gate difference over old source slots is taken.
The beta discrepancy cost is
\(C_B\sum_{j<k}m_jE_j\).
Multiplying by the random amplification (CT39) and using
Cauchy–Schwarz proves
\[
 \left\|\frac{\max_{i\le k}|v_{i;p}-\bar v_{i;p}|}{m_p}\right\|_2
 \le C_B\left(e_p+\eta^{1/16}+q_{\rm disc}
                              +\sum_{j<k}m_jE_j\right).
 \tag{CT40}
\]
The required product norms use at most a gate difference, a query,
and a normalized pulse. Their \(L^{12}\) bounds give \(L^4\)
forcing; (CT39) has an \(L^4\) bound, giving the asserted \(L^2\)
product. Coefficient-only and D-row terms require fewer factors.

Taking expected first-feature derivatives in (CT40), subtracting
the outside bounded gate, and summing over \(p\), gives
\[
 \sup_u\sum_{p<k}|\alpha_{ku,p}-\bar\alpha_{ku,p}|
 \le C_B\left(\eta^{1/16}+q_{\rm disc}
                              +\sum_{j<k}m_jE_j\right).
 \tag{CT41}
\]
Here \(\sum_pm_pe_p=q_{\rm disc}\) and
\(\sum_pm_p\le2L_*+1\). This is precisely where normalization by
the common source mass matters. The F-row difference has the same
bound, by (CT13), (CT37), and coefficient variation.

Set \(G_k=\eta^{1/16}+q_{\rm disc}+\sum_{j<k}m_jE_j\) and
\[
 W_k=\max_j\left\|\sum_p|V_{kj;p}-\bar V_{kj;p}|\right\|_2.
 \tag{CT42}
\]
The maximum is over output fields only; there is no random
maximum over Gaussian source history. Subtract (CT16):
\[
 \begin{aligned}
 \mathrm d U_{i;p}
 &=\sum_{q<i}(\mathrm d F_{i,q})\bar V_{q;p}
                 +\sum_{q<i}F_{i,q}\mathrm d V_{q;p},\\
 \mathrm d C_{k;p}
 &=\sum_{q<k}\bigl[
  (\gamma_q-\bar\gamma_q)\phi'(\bar Z_q^2)\bar U_{q;p}
  +\gamma_q\mathrm d\phi'(Z_q^2)\bar U_{q;p}
  +\gamma_q\phi'(Z_q^2)\mathrm d U_{q;p}\bigr],\\
 \mathrm d V_{i;p}
 &=\phi'(Z_i^2)\mathrm d C_{k;p}
       +\mathrm d\phi'(Z_i^2)\bar C_{k;p}
       +c_k\phi''(Z_i^2)\mathrm d U_{i;p}\\
 &\hspace{4mm}
       +\bigl[(c_k-\bar c_k)\phi''(\bar Z_i^2)
                    +c_k\mathrm d\phi''(Z_i^2)\bigr]\bar U_{i;p}.
 \end{aligned}                                                   \tag{CT43}
\]
The direct current U impulses cancel after pairing the distinguished
slots. Use (CT31)'s pointwise barred row bounds, (CT30)'s density
\(|F_{i,q}|\le C_Bm_q\), the coefficient mass bound, and
(CT37), then sum (CT43) over \(p\) and take \(L^2\).
The first line contributes \(C_BG_k+C_B\sum_{q<i}m_qW_{t(q)}\).
The second contributes its coefficient variation \(C_Bq_{\rm disc}\),
its gate variation \(C_B\eta\), and the same integrated U-row
discrepancy; exchanging two finite sums costs at most the total
mass \(2L_*+1\). The third line contributes \(C_B\eta\) and the
same two row errors. Therefore
\[
 W_k\le C_BG_k+C_B\sum_{j<k}m_jW_j.
 \tag{CT44}
\]
Discrete Gronwall in total mass, and monotonicity of \(G_k\), give
\(W_k\le C_BG_k\). A passive output obeys the same (CT43);
its past terms use the active \(W_j\), so its row difference has
the same bound. Taking expectations proves (CT36).
Its diagonal can also be checked directly from (CT14), with
an \(L^2\) difference at most \(C\eta\).

Everything used for the lower estimates at node \(k\) concerns
earlier Q rows. Its current alpha is then constructed; the upper
equations use only earlier V rows and that alpha.
Current \(Z^2\) moments follow from this new F-row and bounded
\(\Delta^{(2)}\), not from a presumed current beta cap.
Thus (CT36) is causal and is valid at the first potentially failed
current beta row.

The row functions extend continuously to all passive directions.
Indeed \(|\phi'(w\cdot u)u-\phi'(w\cdot v)v|
\le C(1+|w|)|u-v|\). Taking expectations against a normalized
lower pulse and using its \(L^2\) bound gives an alpha difference
at most \(C_B|\gamma_p||u-v|\). The contraction term has the
same bound, so the F-row has a summed Lipschitz bound.
In (CT16) the old V rows are unchanged when only the current
passive input varies; the changed F-row and the \(L^2\)-Lipschitz
current upper gates, multiplied by the pointwise old derivative
row bounds, give a beta-row Lipschitz estimate.
Thus a dense countable set of passive inputs suffices for the
common construction, with the asserted supremum supplied by
continuity. This makes no continuity claim for a random
supremum of Gaussian queries.

###### A.6. Closing the uniform cap

Choose \(B=B_*+1\), where section 4 supplied the reference raw cap.
At every preceding prefix satisfying that cap, (CT34) and (CT36)
give
\[
 E_k\le C_B e^{C_B(2L_*+1)}
                      \bigl(\Phi(q)^{1/16}+q\bigr).
 \tag{CT45}
\]
Choose \(\delta>0\) small enough that this is at most \(1/2\)
for \(q\le\delta\). The zero initial readout gives zero initial
beta rows. At the first potential failure the current row is
at most \(B_*+1/2<B\), a contradiction. This proves the
coefficient assertion of (CT7), including every old source slot.

Equation (CT27) then gives Gaussian tails: for \(R\ge2D_B\),
\(|Q|>R\) implies \(|\zeta|>R/2\), and integrating the scalar
Gaussian tail bounds
\(\mathbb E[(|\zeta|+D_B)^2{\bf1}_{|\zeta|>R/2}]\)
by \(Ce^{-cR^2}\). Taking a square root and reducing \(c\)
gives (CT7); enlarge \(M\) for \(1\le R<2D_B\) and for the
bounded readout. No independence of the bounded remainder and
the Gaussian part is needed.

Here \(\mathrm d X=X-\bar X\) denotes a comparison difference;
\(\Delta^{(2)}\) is the typed upper backward field.


###### A-supplement.4. Named-coefficient continuity in the reference raw anchor

The reference anchor (CT21)–(CT25) uses three different limits.
Their order matters:

- At a fixed clock Euler graph and nonzero fresh forcing,
  width tends to infinity.
- At that fixed graph the forcing tends to zero, after
  establishing continuity of its named coefficient.
- Only after a mesh-uniform coefficient bound has been
  proved is the clock/raw Euler mesh refined.

There is no assertion that zero-forcing continuity is uniform
over a growing graph. The finite pulse norm bound is uniform
in the mesh, which is the property used to obtain the final cap.

For the first limit, smoothly clip the Gaussian first roots
and use an inactive smooth readout clip equal to identity on
a neighborhood of the deterministic readout interval.
The clock coordinate map \(J(X,g)\) obeys
\[
 J_X=\phi'(J),\qquad
 J_g=\frac{\phi'(J)}{\phi'(g)}.
 \tag{A9}
\]
After clipping g both derivatives are bounded at each fixed
clip level. The passive first feature is
\(\phi(u_1J(X_1,g_1)+u_2J(X_2,g_2))\), whose source-relevant
X derivatives are bounded independently of the root clip.
Thus the contained finite Gaussian program and its source rule
apply to the clipped forced and unforced graphs.

At any fixed graph, all named source derivatives have a finite
deterministic envelope while previous selected coefficients
remain in a compact set. This follows inductively:
the lower clock feature derivatives are bounded, the upper
tanh derivatives are bounded, the readout is bounded by total
feature length, and each action answer is its source plus a
finite linear combination with fixed coefficients.
Root derivatives are never taken in this induction.

Now remove the root clip chronologically. Earlier second
moments converge, so the next finite covariance matrix
converges. Its nonnegative square root converges even at rank
loss, by bounded subsequences and uniqueness of a nonnegative
square root. Couple on a common finite standard Gaussian list.
Node values and source derivatives converge in probability.
The deterministic derivative envelope gives uniform
integrability of derivatives, so their expectations converge.
The same argument is uniform over forcing amplitudes in a
fixed compact interval at this fixed graph. In particular it
proves coefficient continuity at zero forcing.
This is the complete continuity mechanism used by
C.4.5.2.R5–R7, not continuity of a pseudoinverse.

The fresh root z remains independent of all centered source
groups in the scalar construction. The latter's selected
covariances may depend on forcing amplitude q, but are
deterministic and frozen under differentiation. The only
local root insertion is \({\rm slot}+qz\), so
\[
 \partial_zV^q=q\,\partial_{\rm slot}V^q,\qquad
 \mathbb E[zV^q]=q\,\mathbb E[\partial_{\rm slot}V^q].
 \tag{A10}
\]
This validates the source extraction even for a zero-variance
or duplicated source slot. The unforced value law alone would
not determine such a transverse derivative.

For the raw-to-clock step, transformed raw variables
\(F(w)\) are an analysis device, not extra instructions to
which the at-most-linear value theorem is applied.
At a fixed raw graph each \(w\) has a linear envelope in the
finite Gaussian root/source list; its named derivatives have
polynomial envelopes. Multiplication by \(F'(w)=\cosh^2w\)
therefore has finite moments at that fixed graph.
The uniform defect estimate CT23 is stronger: after cancellation
its only exponential is \(e^{2h|b|}\), with a capped Gaussian
query b. CT28–CT29 give its required fixed moments uniformly
over all prefixes under the temporary cap.
The direct injection step has size \(h_s\), so dividing its
defect by \(|\bar\gamma_p|=h_s/2\) leaves \(O(h_s)\).
All later defect sums use
\(\sum_kh_k^2\le L_*h_{\max}\).

The source comparison CT24–CT25 then uses only:
bounded clock gates, the deterministic clock-pulse envelope,
the raw/clock raw-state difference, D-row coefficient
differences, and the summed normalized defect.
The current alpha is obtained before current beta; its
right side uses only old raw Q rows. Thus the cap bootstrap
does not assume its current conclusion.

The contained III.F source/regularization proof and C.4.5.2 clipping/forcing
argument supply these fixed-graph constructions. No all-orders jet theorem
or uniform derivative convergence of finite GF is needed for this anchor.

##### Proof unit B. Endpoint conditioning and finite nonlinear learning

For the activity implication in this unit, let \(\tau_{ex}>0\) be a common
existence interval for (NS3); proof unit C constructs it. The endpoint
conditioning and continuity estimates do not assume that existence.

###### B.2. Endpoint conditioning, with a complete proof

The supplied C.4.5–C.4.6 facts used here are

\[
 \|A_\dagger\|\le M:=2+\sqrt{10},\quad
 \|c_\dagger\|_2\le C:=\sqrt{10},\quad
 \|c_\dagger\|_\infty\le H:=10,\quad
 \|w_\dagger\|_2\le W:=\sqrt2+\sqrt{10}.
 \tag{2.1}
\]

The endpoint predictor is 76-Lipschitz, vanishes at
`(e1+e2)/sqrt(2)`, and fits `(1,-1)`. Thus, on (NS1),

\[
 |f_\dagger(u_\alpha)|\le76/1216=1/16,
 \qquad 5/16\le y-f_\dagger(u_\alpha)\le11/16.
 \tag{2.2}
\]

In particular the added-law endpoint risk is at least `25/256`, even though
its contribution to the mixture risk is only `epsilon` times that number.

C.4.6.S40–S44 supplies one nonnegative random envelope `N`, with finite
`C_*`, such that on the reference feature segment

\[
 \|N\|_p\le C_*\sqrt p\ (p\ge2),\quad
 \sup_s|X_a(s)|\le5N,\quad
 F(w_a(s))=F(g_a)+X_a(s),\quad F'(z)=\cosh^2z,
 \tag{2.3}
\]

where `g1,g2` are independent standard normals. It also gives
`||Q_dagger(u)||_4<=L4:=2C_*` uniformly over every deterministic circle
input. Its countable-source construction and Fubini supply the simultaneous
active-clock bounds in (2.3). Independence of `N` and `g` is not asserted.

Here is the endpoint first-feature independence argument in full. Fix
`v in R2` with nonzero coordinates. Markov's inequality with
`p=(R/(eC_*))^2>=2` gives

\[
 \Pr(N>R)\le\exp[-R^2/(e^2C_*^2)].
\]

The Gaussian density gives

\[
 \Pr\{|g-rv|_\infty\le1\}
    \ge {2\over\pi}\exp[-(r|v|+\sqrt2)^2/2].
\]

For all sufficiently large `r` this exceeds `Pr(N>r^2)`, so their box
intersected with `{N<=r^2}` has positive probability. On that event put
`rho=min(|v1|,|v2|)/2`; for large `r`, `|g_a|>=rho r`. The minimum of
`F'` on `[g_a-1,g_a+1]` is at least `exp(2(|g_a|-1))/4>5r^2`.
Monotonicity of `F` in (2.3) therefore gives

\[
 \sup_s|w_a(s)-g_a|
    \le20r^2e^{-2(|g_a|-1)}\le20e^2r^2e^{-2\rho r}\longrightarrow0.
 \tag{2.4}
\]

If a finite pairwise distinct, nonantipodal list `u1,...,um` satisfied
`sum a_j tanh(w_dagger.u_j)=0` almost surely, choose such a `v` also
avoiding all lines `v.u_j=0`. On the preceding positive-probability events,
the features tend uniformly to `sign(v.u_j)`. Hence

\[
                   \sum_j a_j\operatorname{sign}(v\cdot u_j)=0.
 \tag{2.5}
\]

Cross the line perpendicular to any `u_k` on the circle of `v` directions.
The pairwise distinct, nonantipodal condition means no other sign changes there. Choose points
on both sides with nonzero coordinates, also when the crossing is on an axis.
Subtracting (2.5) gives `2a_k=0` up to orientation. Thus all `a_k=0`.
The features are linearly independent.

At the endpoint define

\[
 H^1(u)=\tanh(w_\dagger\cdot u),\quad Z^2(u)=A_\dagger H^1(u),
 \quad H^2(u)=\tanh Z^2(u),\quad
 \delta(u)=c_\dagger\operatorname{sech}^2Z^2(u),\quad
 Q(u)=A_\dagger^*\delta(u).
\]

The readout is nonzero since `<c_dagger,H2(e1)>=1`. Because `Z2(u)`
is finite almost surely and its gate is strictly positive, every `delta(u)`
is nonzero in L2. The raw gradient, at this or any admissible state, is

\[
 g_\theta(u)=\big(u\operatorname{sech}^2(w\cdot u)Q(u),
                    \delta(u)\otimes H^1(u),\ H^2(u)\big).
 \tag{2.6}
\]

For a finite list, if `lambda_H` is its first-feature Gram minimum eigenvalue,
then

\[
 \left\|\sum_i a_i\delta_i\otimes H_i^1\right\|_{HS}^2
    \ge\lambda_H\sum_i a_i^2\|\delta_i\|_2^2.
 \tag{2.7}
\]

Indeed at each second-layer coordinate apply the first-feature Gram
inequality to `sum_i a_i delta_i(omega2)H_i^1` and integrate. This also
identifies the integral with the tensor's Hilbert–Schmidt norm. Thus the
middle gradient blocks, hidden gradient blocks and full gradients are
independent. No injectivity of the trained action is assumed.

The first-feature Gram is continuous in the input list by the L2 Lipschitz
bound for tanh. The fields `delta(u)` are L2-continuous: first pass input
continuity through `w_dagger`, tanh and the bounded action, then use the
bounded fixed readout in (2.1). Their nonzero L2 norms therefore have a
positive minimum on the present compact input set. Define

\[
 \kappa:=\min_{\alpha\in I}\lambda_{\min}
     \big(\langle H^1(v_i),H^1(v_j)\rangle\big)_{i,j=1}^3
       \ \min_{\alpha\in I,\,i\le3}\|\delta(v_i)\|_2^2>0.
 \tag{2.8}
\]

Continuity of the minimum eigenvalue follows from the Rayleigh formula,
`|lambda_min(B)-lambda_min(D)|<=||B-D||`; a continuous positive function
on a compact set has positive minimum. This proves every positivity step
in (2.8). It is a precisely defined endpoint constant, not an evaluated
numerical lower bound.

Consequently the endpoint three-input middle Gram is at least `kappa I`.
The full anchor Gram `M_dagger` is at least `kappa I`. Let

\[
 d_\alpha=\Pi_\dagger g_\dagger(u_\alpha),\quad
 \beta_\alpha=M_\dagger^{-1}G_\dagger^*g_\dagger(u_\alpha),\quad
 t_\alpha=(-\beta_{\alpha,1},-\beta_{\alpha,2},1).
 \tag{2.9}
\]

Since `d=sum_i t_i g_dagger(v_i)` and `|t|>=1`, (2.7) implies

\[
 \|d_\alpha\|^2\ge\|d_{\alpha,H}\|^2
       \ge\|d_{\alpha,K}\|_{HS}^2\ge\kappa.
 \tag{2.10}
\]

The hidden block `H` consists of the first row and middle increment; the
`K` subscript means only the middle increment. The upper gradient bound is

\[
 \|g_\dagger(u)\|\le L_0:=\sqrt{1+C^2(1+M^2)}<17.
\]

Therefore `||d_alpha||<=L0`, `||G_dagger||<=G0:=sqrt(2)L0`, and

\[
 |t_\alpha|\le T_0:=\sqrt{1+2L_0^4/\kappa^2}.
 \tag{2.11}
\]

###### B.3. Quantitative gradient continuity from raw distance and endpoint L4 tails

This paragraph verifies input continuity and state continuity together. Put
`d=||theta-theta_dagger||_raw`, `h=|u-v|`, `rho=d+h<=1`. Here `A-A_dagger`
is measured in HS norm, hence also bounded in operator norm. Use endpoint
quantities at `v` as fixed factors. Successive subtraction gives

\[
 \|Z^1_\theta(u)-Z^1_\dagger(v)\|_2\le a_1\rho,
 \quad\|H^1_\theta(u)-H^1_\dagger(v)\|_2\le a_1\rho,
 \quad a_1=1+W,
\]

\[
 \|Z^2_\theta(u)-Z^2_\dagger(v)\|_2,
 \ \|H^2_\theta(u)-H^2_\dagger(v)\|_2\le a_2\rho,
 \quad a_2=1+Ma_1,
\]

\[
 \|\delta_\theta(u)-\delta_\dagger(v)\|_2\le a_\delta\rho,
 \quad a_\delta=1+2Ha_2,
\]

\[
 \|Q_\theta(u)-Q_\dagger(v)\|_2\le a_Q\rho,
 \quad a_Q=C+1+Ma_\delta.
 \tag{3.1}
\]

For the backward product split it as
`(c-c_dagger)phi'(Ztheta)+c_dagger[phi'(Ztheta)-phi'(Zdagger)]`.
This uses the bounded endpoint readout, not an unproved L-infinity smallness
of the evolving readout difference. For the adjoint split use the current
backward field, whose L2 norm is at most `C+1`, in the changed-action term.

The only additional row product is a changed first gate times the fixed
endpoint `Q_dagger(v)`. For gates `b=phi'(z)-phi'(z0)`,
`|b|<=min(1,2|z-z0|)` implies

\[
 \|b\|_4\le\sqrt2\|z-z_0\|_2^{1/2},\qquad
 \|bQ_\dagger(v)\|_2\le\sqrt{2a_1}L_4\rho^{1/2}.
 \tag{3.2}
\]

This is Holder's inequality and the proved endpoint L4 bound. It does not
multiply two uncontrolled L2 increments. Also
`||Q_theta(u)||2<=(M+1)(C+1)=:Q1`. Subtracting the explicit input vector
in the row gradient, the middle rank factors and the final hidden value gives

\[
 \|g_\theta(u)-g_\dagger(v)\|\le C_g\rho^{1/2},
\]

\[
 C_g=Q_1+a_Q+a_\delta+Ca_1+a_2+\sqrt{2a_1}L_4.
 \tag{3.3}
\]

The raw Hilbert norm is bounded above here by the sum of its three component
norms. This proves uniform endpoint state/input continuity, including that
of `beta_alpha`, `t_alpha`, and `d_alpha` in (2.9). No input derivative of a
query is required.

At fixed `u`, prediction subtraction also gives

\[
 |f_\theta(u)-f_\dagger(u)|\le C_f d,
 \qquad C_f=1+Ca_2,
 \tag{3.4}
\]

uniformly on the circle. The scalar differentiation formula (2.6) along
strongly C1 raw curves follows from the strong L2 chain rule: for a fixed
direction the tanh difference quotient is dominated by its L2 direction,
and the error of replacing a C1 increment by that direction is controlled
by the one-Lipschitz activation. Differentiating the bounded action product
and the scalar readout pairing gives the three blocks in (2.6). Bounded
multiplier convergence against fixed L2 fields proves their continuity.
Explicitly, if bounded multipliers `b_k` converge in probability to `b`,
split a fixed `q in L2` at `|q|=R`. The bounded part of
`||(b_k-b)q||2` tends to zero by bounded convergence in probability; its
tail is at most `2 sup_k||b_k||infty ||q 1_(|q|>R)||2`. Let `k` grow
first and then `R` grow. Applying this fact successively to the fixed-state
backward and row factors proves continuity at any state, without requiring
an L4 bound at that state.
An ambient Frechet derivative of an L2-valued hidden map is not used.

For explicit projector estimates set

\[
 a_G=\sqrt2 C_g,\quad G_1=G_0+a_G,\quad
 a_M=(2G_0+a_G)a_G.
\]

Then `||G_theta-G_dagger||<=a_G sqrt(d)` and
`||M_theta-M_dagger||<=a_M sqrt(d)`. If
`a_M sqrt(d)<=kappa/2`, the Rayleigh formula gives
`M_theta>=kappa I/2`, and the inverse identity yields

\[
 \|M_\theta^{-1}-M_\dagger^{-1}\|
       \le(2a_M/\kappa^2)\sqrt d.
\]

Expanding the three changed factors in `G M^-1 G*` proves

\[
 \|\Pi_\theta-\Pi_\dagger\|\le C_\Pi\sqrt d,
 \quad C_\Pi={2a_GG_1\over\kappa}
       +{2G_0a_MG_1\over\kappa^2}+{G_0a_G\over\kappa}.
 \tag{3.5}
\]

Writing `d_theta,alpha=Pi_theta g_theta(u_alpha)`, it follows that

\[
 \|d_{\theta,\alpha}-d_\alpha\|\le C_d\sqrt d,
 \qquad C_d=C_g+C_\Pi L_0.
 \tag{3.6}
\]

All constants are uniform over (NS1).

###### B.4. The hidden contrast and its derivative along the reached path

Keep the endpoint readout and coefficients fixed during the episode:

\[
 O_\alpha(\theta)=\sum_{i=1}^3 t_{\alpha,i}
                 \langle c_\dagger,H^2_\theta(v_i)\rangle.
 \tag{4.1}
\]

This functional depends only on hidden parameters. Its raw gradient is
`o_alpha(theta)=(sum_i t_i h_i^fixed(theta),0)`, where `h_i^fixed` is the
first-row/middle portion of (2.6) with the readout set to `c_dagger`.
The proof is the strong curve chain rule just given, with a fixed bounded
readout in the scalar pairing. In particular

\[
 o_\alpha(\theta_\dagger)=(d_{\alpha,H},0),\qquad
 \|o_\alpha(\theta)-o_\alpha(\theta_\dagger)\|
       \le C_o\sqrt d,\quad C_o=\sqrt3T_0 C_g.
 \tag{4.2}
\]

For the last inequality apply (3.3) to the auxiliary state `(w,A,c_dagger)`
and sum its three hidden-gradient differences using
`sum|t_i|<=sqrt(3)|t|`. Thus derivative continuity of this hidden contrast
uses only raw distance and fixed endpoint L4 tails, even if the evolved
query field is known only through the constructed source-regular flow.

The field in (NS3) is continuous on the neighborhood under consideration:
(3.3) and its fixed-state bounded-multiplier proof give gradient continuity,
and (3.5) gives inverse/projector continuity. A raw-continuous solution of
the strong integral equation therefore has a continuous raw derivative.
Its two hidden maps are strongly C1 by the chain rule above. Consequently

\[
 {d\over d\tau}O_\alpha(\theta(\tau))
       =\langle o_\alpha(\theta(\tau)),V_{\alpha,y}(\theta(\tau))\rangle.
 \tag{4.3}
\]

At the endpoint, writing `r_dagger=f_dagger(u_alpha)-y`, (2.2) and (2.10)
give the uniform strictly positive value

\[
 O_\alpha'(0)=-2r_\dagger\|d_{\alpha,H}\|^2\ge5\kappa/8.
 \tag{4.4}
\]

This explicitly checks hidden representation motion. A nonzero hidden
parameter block is only the input to the identity, not its conclusion.

For a quantitative derivative modulus put

\[
 L_1=\sqrt{1+(C+1)^2(1+(M+1)^2)},\quad
 R_1=C+1+5/8,\quad V_1=2R_1L_1.
\]

On the unit raw ball and the invertible-Gram region, `||g_theta(u)||<=L1`,
`|f_theta(u_alpha)-y|<=R1`, and `||V_alpha,y(theta)||<=V1`, because
an orthogonal projector has norm at most one. Equations (3.4) and (3.6) give

\[
 \|V_{\alpha,y}(\theta)-V_{\alpha,y}(\theta_\dagger)\|
      \le C_V\sqrt d,
 \quad C_V=2C_fL_1+(11/8)C_d.
\]

Use (4.2), `||o_alpha(theta_dagger)||<=L0`, and the last bound in (4.3):

\[
 |O_\alpha'(\theta)-O_\alpha'(\theta_\dagger)|
       \le A_O\sqrt d,
 \qquad A_O=C_oV_1+L_0C_V.
 \tag{4.5}
\]

Here `O'(theta)` means its derivative in the actual field (NS3), not a
derivative of a frozen trajectory. This estimate supplies uniform
continuity along all the reached paths in the family.

###### B.5. A uniform, finite nonlinear episode

Choose the following positive raw radius:

\[
 \rho_0=\min\left\{1,\left({\kappa\over2a_M}\right)^2,
             {\kappa\over4C_d^2},\ {5\over32C_f},
             \left({5\kappa\over16A_O}\right)^2\right\}>0.
 \tag{5.1}
\]

Every denominator is finite and positive by its displayed definition. Let

\[
 \tau_0=\min\{\tau_{ex}/2,\rho_0/(2V_1)\}>0.
 \tag{5.2}
\]

Before a possible first exit from the raw ball of radius `rho0`, the
velocity bound `V1` gives `||theta(tau)-theta_dagger||<=V1 tau`.
If that first exit occurred by `tau0`, this distance would be at most
`rho0/2`, a contradiction. Thus all paths stay in the ball through `tau0`.
The Gram is at least `kappa I/2` there. This is a first-exit estimate for the
existing nonlinear equation, not a conclusion from the initial linear term.

Since `G_theta^*Pi_theta=0`, the chain rule applied to the two anchors proves
the anchor assertion. The choices in (5.1), (2.2), and (3.6) give throughout the interval

\[
 |r(\tau)|\ge5/32,\qquad r(\tau)<0,\qquad
 \|d_{\theta(\tau),\alpha}\|^2\ge\kappa/4.
 \tag{5.3}
\]

The exact added prediction and risk identities are

\[
 f_\theta(u_\alpha)'=-2r\|d_{\theta,\alpha}\|^2,\qquad
 (r^2)'=-4r^2\|d_{\theta,\alpha}\|^2.
 \tag{5.4}
\]

They retain every moving hidden field and the recomputed projector. Integrating
(5.3)–(5.4) gives (NS6) with

\[
 \eta_R={25\kappa\over1024}\tau_0>0,
 \qquad f_{\theta(\tau_0)}(u_\alpha)-f_\dagger(u_\alpha)
                        \ge {5\kappa\over64}\tau_0>0.
 \tag{5.5}
\]

By (4.4)–(4.5) and (5.1), `O_alpha'(theta(tau))>=gamma_O:=5kappa/16`.
Hence `Delta O_alpha>=gamma_O tau` for `0<=tau<=tau0`. Cauchy–Schwarz,
first in the second population and then in the three coefficients, yields

\[
 |\Delta O_\alpha|^2
 \le\|c_\dagger\|_2^2|t_\alpha|^2
             \sum_{i=1}^3\|\Delta H_i^2\|_2^2
 \le30T_0^2 J_{2,\alpha,y}(\tau).
 \tag{5.6}
\]

Thus (NS7) holds with the explicit positive constant

\[
 \eta_H={\gamma_O^2\tau_0^2\over30T_0^2}>0.
 \tag{5.7}
\]

This finite episode has actual upper hidden activation displacement. Its
proof uses derivative continuity of a scalar hidden contrast to retain a
strict sign over a finite interval; it does not extrapolate the initial
velocity as the finite trajectory. The interval and margins have no
`epsilon` dependence.

The whole-circle map is
`P_(alpha,y)(tau,sqrt(2)u)=<c(tau),tanh(A(tau)tanh(w(tau).u))>`.
It is jointly continuous in time and input and has a uniformly bounded input
Lipschitz constant on this episode, since it is bounded by
`||c||2 ||A||op ||w||2`. Equation (3.4) gives a uniform whole-circle
comparison to the endpoint on the local ball. This defines the prediction
to be captured; Its original-mixture identification is proved in proof unit C.

##### Proof unit C. Original-initialization continuation and slow selection

###### C.1. State and source interface

Use the state and initialized carrier in (NS2), and write its raw increment
space as \(\mathcal E\). Throughout this unit inputs in \(f_\theta(u)\)
are normalized; the reconstructed physical prediction is evaluated at
\(x=\sqrt2u\). For clarity the fields used in the comparisons are
\[
 H^1(u)=\phi(w\cdot u),\quad Z^2(u)=AH^1(u),\quad H^2(u)=\phi(Z^2(u)),
 \quad f_\theta(u)=\langle c,H^2(u)\rangle,
\]
\[
 \Delta^{(2)}(u)=c\phi'(Z^2(u)),\quad Q(u)=A^*\Delta^{(2)}(u),\quad
 g_u=(\phi'(w\cdot u)Q(u)u,\Delta^{(2)}(u)\otimes H^1(u),H^2(u)).\tag{1}
\]
The scalar prediction is continuously differentiable in the raw metric by
the contained scalar-gradient argument in A.4. Set
\[
 p=(\alpha,y)\in\mathcal P=I\times[3/8,5/8],\qquad
 I=[\pi/4-1/1216,\pi/4+1/1216].\tag{2}
\]
All constants below are uniform in this compact box. The reference feature
curve is exactly
\[
 \theta_s=\tfrac12g_{e_1}(\theta)-\tfrac12g_{e_2}(\theta),\tag{3}
\]
and C.4.5 proves the raw endpoint and residual bounds
\[
 \|\theta_*(t)-\theta_\dagger\|_{\rm raw}\le\sqrt{10}e^{-t/5},
 \qquad |r_*(t)|\le\sqrt2 e^{-t/5}.\tag{4}
\]
Its physical control is \(a_*=(e_*,-e_*,0)\), with total absolute mass
\(s_\dagger\le10\). For the three inputs \(e_1,e_2,u_\alpha\), raw Euler is
\[
 \theta_{k+1}=\theta_k+\sum_{j=1}^3\gamma_{kj}g_{u_j}(\theta_k).\tag{5}
\]
Let SCT denote the source estimate of proof unit A: there are uniform
\(\delta_{\rm src},h_{\rm src}>0\) and \(B_{\rm src}<\infty\) for all
such finite histories satisfying
\[
 \int|a(t)-a_*(t)|_1dt<\delta_{\rm src}.\tag{6}
\]
The mesh is measured by \((|a|_1+|a_*|_1)dt\). Every passive backward row,
including its distinguished current source and all old training sources,
then has the stated cap. Deterministic feedback coefficients are frozen
under named differentiation, just as in (CT12)–(CT16).

The physical reference keeps running after every finite prefix. A prefix
through \(b\) followed by appended controls has distance at most the
appended absolute mass plus \(s_\dagger-s_*(b)\), including a zero extension
after the episode. This supplies the endpoint interface without a source
reset. All subsequent constructions use this exact full-history condition.

###### C.2. Consequences of SCT and the one-reference modulus

Write \(L=\sum_{k,j}|\gamma_{kj}|\). Under (6),
\(L\le10+\delta_{\rm src}\). The elementary controlled updates give

\[
 \|c\|_\infty\le L,\quad \|K\|_{\rm HS}\le L^2/2,\quad
 \|A\|_{\rm op}\le2+L^2/2,\quad
 \|w\|_2\le\sqrt2+L^2+L^4/8.
 \tag{7}
\]

Indeed the readout increases by at most the current control mass, the middle
increment by at most that mass times the preceding readout bound, and the
row increment by at most that mass times the action/readout bounds.
Summing is bounded by the corresponding integrals in accumulated mass.
Harmless enlarged constants also cover affine interpolants and unequal
simultaneous updates. None depends on physical elapsed time.

The exact source identity C.4.7.N5 is
\(Q_{kv}=\zeta_{kv}+\sum_qD_{kv,q}H^1_q\). Its learned coefficient row has
absolute sum at most \(L\sup\|c\|_\infty^2\); its response row is bounded by
SCT. Also \(\mathbb E\zeta_{kv}^2\le\sup\|c\|_\infty^2\). Thus

\[
 Q_{kv}=\zeta_{kv}+J_{kv},\quad |J_{kv}|\le C,\quad
 \operatorname{Var}(\zeta_{kv})\le C^2,
 \qquad \tau_R(Q_{kv})\le C e^{-cR^2}\quad(R\ge1).
 \tag{8}
\]

The last estimate follows by splitting at \(R>2C\), using
\(\{|Q|>R\}\subset\{|\zeta|>R-C\}\), and integrating the scalar Gaussian
tail; enlarging the constant covers the remaining \(R\). It requires no
independence of \(J\) and \(\zeta\). In particular

\[
 \sup_{k,v}\|Q_{kv}\|_p\le C_p<\infty\qquad(2\le p<\infty).
 \tag{9}
\]

These are separate deterministic input/time bounds, not a moment bound for
an uncountable coordinate supremum.

For two raw states \(\theta,\bar\theta\) on a common bounded raw/action region,
use the equivalent sum distance \(d\). Suppose only the comparison endpoint
\(\bar\theta\) has \(\|\bar c\|_\infty\le C\) and the tails (8).
Subtract the factors in (1). The upper subtraction is

\[
 \Delta^{(2)}-\bar\Delta^{(2)}=(c-\bar c)\phi'(Z^2)
                +\bar c[\phi'(Z^2)-\phi'(\bar Z^2)].
\]

It costs \(Cd\), as do \(Q-\bar Q\) and the middle/readout blocks.
The remaining lower product is bounded by

\[
 \|[\phi'(w\cdot v)-\phi'(\bar w\cdot v)]\bar Q(v)\|_2
 \le 2R\|w-\bar w\|_2+2\tau_R(\bar Q(v)).
 \tag{10}
\]

Changing the input adds \(C|v-\bar v|\) to the forward and upper differences;
apply (10) also to the lower gate with
\(\|w\cdot v-\bar w\cdot\bar v\|_2\le
\|w-\bar w\|_2+\|\bar w\|_2|v-\bar v|\).
Consequently

\[
 \|g_v(\theta)-g_{\bar v}(\bar\theta)\|_{\rm raw}
 \le C(1+R)(d+|v-\bar v|)+C e^{-cR^2}.
 \tag{11}
\]

Only the comparison state's tails appear. Its readout supremum is likewise
the only readout supremum used in this subtraction. An arbitrary competing
strong raw solution therefore need not satisfy a new tail assumption.

For \(0<z\le1\), set
\(\omega(z)=z\sqrt{\log(e/z)}\), and extend it increasingly at larger \(z\).
Choosing \(R\) proportional to \(\sqrt{\log(e/z)}\) in (11) gives the
one-reference bound \(C\omega(z)\). The function is increasing on \((0,1]\),
and

\[
 \int_{0+}\frac{dz}{\omega(z)}=\infty.
 \tag{12}
\]

The following explicit comparison will be used repeatedly. If
\(D(t)\le\eta+C\int_0^t\omega(D(s))ds\), then, while the right side stays
below one,

\[
 D(t)\le {\cal O}_t(\eta):=
 e\exp\!\left[-\left(\sqrt{\log(e/\eta)}-Ct/2\right)^2\right].
 \tag{13}
\]

To prove it, put \(Z(t)=\eta+C\int_0^t\omega(D(s))ds\). Monotonicity gives
\(Z'\le C\omega(Z)\), and
\((\sqrt{\log(e/Z)})'\ge-C/2\). Integrate. For \(\eta=0\), replace it by a
positive number and let that number decrease to zero. For every fixed
bounded interval, \({\cal O}_t(\eta)\to0\) uniformly as \(\eta\to0\).
A first-exit argument validates staying below one when the initial error
is sufficiently small.

###### C.3. Endpoint conditioning and constrained coefficients

Let \(G(\theta):\mathbb R^2\to\mathcal E\) have columns \(g_{e_1},g_{e_2}\).
The endpoint Gram \(M_\dagger=G(\theta_\dagger)^*G(\theta_\dagger)\) is strictly
positive. This follows from proof unit B.

By joint raw gradient continuity there are \(\rho>0,\kappa>0\) such that on

\[
 {\cal N}=\{\|\theta-\theta_\dagger\|_{\rm raw}<\rho\}
 \quad\text{one has}\quad M(\theta):=G^*G\ge4\kappa I_2.
 \tag{14}
\]

Shrink \(\rho\) once and retain an interior ball for all constructed paths.
The neighborhood has bounded raw/action norms, although it need not have
bounded readout supremum. The latter bound comes from controls, not (14).
Put

\[
 B(\theta)=G(\theta)M(\theta)^{-1},\quad
 \Pi(\theta)=I-G(\theta)M(\theta)^{-1}G(\theta)^*,
\]
\[
 r_p(\theta)=f_\theta(u_\alpha)-y,\quad
 v_p(\theta)=r_p(\theta)g_{u_\alpha}(\theta),\quad
 V_p(\theta)=-2\Pi(\theta)v_p(\theta).
 \tag{15}
\]

The inverse in (15) is an ordinary two-by-two matrix inverse. The coefficients
are bounded and continuous on a slightly smaller raw neighborhood, uniformly
in \(p\). In particular

\[
 V_p(\theta)=\sum_{j=1}^3a_j(\theta,p)g_{u_j}(\theta),
 \quad (a_1,a_2)^T=2r_p M^{-1}G^*g_{u_\alpha},\quad a_3=-2r_p,
 \quad |a|_1\le A.
 \tag{16}
\]

The scalar prediction is Lipschitz on bounded raw/action sets. Equations
(11), the identity
\(M^{-1}-\bar M^{-1}=M^{-1}(\bar M-M)\bar M^{-1}\), and the bounded Gram
factors therefore give

\[
 \|V_p(\theta)-V_{\bar p}(\bar\theta)\|_{\rm raw}
 \le C\omega(d(\theta,\bar\theta)+|p-\bar p|)
 \tag{17}
\]

when \(\bar\theta\) is a tail-bearing constructed state. The same estimate
holds for the coefficient vector in (16). It does not assert an ambient
locally Lipschitz field.

###### C.4. Construction from reference prefixes, tails, and uniqueness

Choose reference physical prefixes ending at \(b_m\uparrow\infty\), with
sufficiently fine finite raw Euler approximations using exact integrated
reference controls. Their terminal states
\(\theta_m^0\) converge in raw norm to \(\theta_\dagger\), by the established
reference construction, or by (11)--(13) and SCT. Their controls approximate
the fixed reference controls on that prefix. Immediately after \(b_m\),
append the explicit Euler recursion on an interval of length \(\tau_0\)

\[
 \theta^{m,h}_{k+1}=\theta^{m,h}_k+h_k V_p(\theta^{m,h}_k).
 \tag{18}
\]

Choose once a positive \(\tau_0\) so small that

\[
 A\tau_0<\delta_{\rm src}/8,\qquad
 \tau_0\sup_{{\cal N},p}\|V_p\|_{\rm raw}<\rho/8.
 \tag{19}
\]

Take \(m\) large enough that the prefix state error is below \(\rho/8\),
its control approximation error is below \(\delta_{\rm src}/8\), and the
omitted suffix has mass below \(\delta_{\rm src}/8\). The bound on (18)'s
accumulated speed keeps all its nodes strictly inside \({\cal N}\); the
controls (16) are legitimate throughout. Equations (19) keep the entire
history strictly inside the SCT tube. Decrease its maximal control mesh
as necessary. This proves admissibility before using the tail conclusion.

Compare two appended Euler interpolants. Their preceding-node distance is
at most their current distance plus \(C(h+h')\). Equation (17), with (8)
at the comparison nodes, bounds their velocity difference by the Osgood
modulus of that quantity, plus the parameter discrepancy. Integrating and
using (13) shows they are Cauchy in \(C([0,\tau_0];\mathcal E)\), uniformly in
\(p\), as their prefix errors and meshes tend to zero. The limit is independent
of those choices. One may first use a countable dense parameter/mesh family
and its finite unions on the prescribed carrier, then extend by the same
uniform estimate; no uncountable family of independent carriers is chosen.

The joint continuity of (1) and (15) passes (18)'s integral equation to

\[
 \bar\theta_p(\tau)=\theta_\dagger+
             \int_0^\tau V_p(\bar\theta_p(s))\,ds.
 \tag{20}
\]

The convergence of the integrands is uniform: otherwise choose discrepant
times and parameters, extract a convergent parameter/time subsequence, and
apply continuity at the limiting state. Thus (20) is strongly \(C^1\), jointly
continuous in \(p,\tau\), and has one-sided derivatives at the endpoints.
All coefficients are computed from the current full state, the fixed atom,
and the retained initialized action. The reference prefix is an approximation
of its already specified initial state, not a pretraining stage imposed on
the changed-law optimizer.

The Gaussian tails survive this construction. Raw convergence gives
\(Q_m(v)\to Q(v)\) in \(L^2\), uniformly over compact parameter/time/input sets,
by bounded-multiplier continuity and compactness. For fixed \(R\),
\(q\mapsto(|q|-R)_+\) is \(L^2\)-Lipschitz and

\[
 \tau_{2R}(Q)\le2\|(|Q|-R)_+\|_2.
 \tag{21}
\]

Pass (8) through this continuous positive-part norm; (21) gives
\(\tau_R(Q)\le C e^{-c'R^2}\) with enlarged constants. Similarly
\(\|c\|_\infty\le10+\delta_{\rm src}\) passes through an almost-everywhere
subsequence. All moments (9), particularly \(L^4\) and \(L^8\), follow.
Interpolation between \(L^2\) convergence and the uniform \(L^8\) bounds
makes the query maps jointly continuous into \(L^4\).

Uniqueness requires tails only on this constructed path. If another strong
solution of (20) on the same carrier starts at \(\theta_\dagger\), compare it
with \(\bar\theta_p\) using (17) and (13). On their initial common
neighborhood the initial error is zero, so they coincide. Repeating at the
end of a common subinterval proves equality through \(\tau_0\); an earlier
exit would contradict the constructed path's strict interior bound.
The same argument proves uniqueness from every reached state on the remaining
interval. No arbitrary-state existence assertion is made.

Since the scalar predictions are \(C^1\), (20) gives
\(\partial_\tau(f(e_1),f(e_2))=G^*V_p=0\). Both anchors are fitted exactly
throughout. The whole-circle determining prediction is

\[
 P_p(\tau,\sqrt2v)=
 \langle\bar c_p(\tau),
  \phi((A_0+\bar K_p(\tau))\phi(\bar w_p(\tau)\cdot v))\rangle.
 \tag{22}
\]

The full hidden state evolves in (20). Formula (22) is not a prediction-only
closure or a frozen kernel.

###### C.5. Strong activation derivatives and absolute continuity of B

These derivative statements concern controlled reached curves, not arbitrary
ambient directions. Let a reached raw curve solve

\[
 \theta'(t)=\sum_{j=1}^3a_j(t)g_{u_j}(\theta(t)),\qquad
 m(t)=\sum_j|a_j(t)|\in L^1,
 \tag{23}
\]

and assume the uniform query tails and readout bounds just proved. All constants
below depend only on those reached bounds and the anchor gap.
The first component of (1) gives
\(\|w'(t)\|_4\le C m(t)\). Also
\(\|K'(t)\|_{\rm HS}+\|c'(t)\|_2\le C m(t)\) and the pointwise readout
formula gives \(|c'(t,\omega_2)|\le m(t)\).
Hence, for every deterministic passive input \(v\),

\[
 (H^1(v))'=\phi'(w\cdot v)\,w'\cdot v,\qquad
 (Z^2(v))'=K'H^1(v)+A[\phi'(w\cdot v)\,w'\cdot v],
\]
\[
 (H^2(v))'=\phi'(Z^2(v))(Z^2(v))',\qquad
 \Delta^{(2)}(v)'=c'\phi'(Z^2(v))+c\phi''(Z^2(v))(Z^2(v))',
\]
\[
 Q(v)'=K'^*\Delta^{(2)}(v)+A^*\Delta^{(2)}(v)'.
 \tag{24}
\]

These are strong \(L^2\) absolutely continuous identities and
\(\|Q(v)'\|_2+\|\Delta^{(2)}(v)'\|_2\le Cm(t)\). A direct justification, which
also covers merely integrable controls, is to choose the coordinatewise
absolutely continuous representatives supplied by Fubini, apply the scalar
chain rule almost everywhere, and integrate the displayed \(L^2\)-integrable
derivatives. The uniform pointwise bound on \(c\) handles its product with
\((Z^2)'\). This argument needs no \(L^\infty\) Banach-space derivative of c.

Differentiate the three blocks of (1) along (23):

\[
 (g_v)'_w=
 \{\phi''(w\cdot v)(w'\cdot v)Q(v)+\phi'(w\cdot v)Q(v)'\}\,v,
\]
\[
 (g_v)'_K=\Delta^{(2)}(v)'\otimes H^1(v)+\Delta^{(2)}(v)\otimes(H^1(v))',
 \qquad (g_v)'_c=(H^2(v))'.
 \tag{25}
\]

The only additional unbounded product is the first term in (25). Hölder gives

\[
 \|(w'\cdot v)Q(v)\|_2\le\|w'\|_4\|Q(v)\|_4\le Cm(t).
 \tag{26}
\]

All other terms are controlled by (24), bounded gates, and the rank norm
identity. Thus each anchor gradient is absolutely continuous in raw norm and
\(\|G'(t)\|_{\mathrm{op}}\le Cm(t)\).
The same coordinatewise argument, now using (26), proves the fundamental
theorem for (25); it is not a formal ambient Hessian calculation.

Ordinary finite-matrix absolute continuity and (14) now yield

\[
 M'=G'^*G+G^*G',\qquad
 B'=G'M^{-1}-GM^{-1}M'M^{-1},\qquad
 \|B'\|_{\mathrm{op}}\le Cm(t).
 \tag{27}
\]

Along (20), the coefficients (16), the query \(L^4\) continuity, and bounded
multiplier continuity show that its row velocity is jointly \(L^4\)-continuous
in \((p,\tau)\). Equations (24) show that the strong activation derivatives
are jointly \(L^2\)-continuous in \((p,\tau,v)\), including \(\tau=0\).
For example the multiplier difference is applied to one fixed limiting
velocity, and its varying velocity is subtracted first; compactness makes
this argument uniform. Consequently

\[
 H^2_{\bar\theta_p(\tau)}(v)
 =H^2_{\theta_\dagger}(v)+
   \tau\,D H^2_{\theta_\dagger}(v)[V_p(\theta_\dagger)_h]
   +o_{L^2}(\tau)
 \tag{28}
\]

uniformly on compact parameter/input sets. The derivative is the strong
curve derivative in (24). This is the uniform derivative fact needed for the
paired hidden-activation margin in proof unit B.

###### C.6. Actual original-mixture continuation in the control tube

For an existing reached mixture segment set
\(r=(f(e_1)-1,f(e_2)+1)\). The exact equations, with the two anchor weights
included, are

\[
 \theta'=-(1-\varepsilon)Gr-2\varepsilon v_p,\qquad
 r'=-(1-\varepsilon)Mr-2\varepsilon G^*v_p.
 \tag{29}
\]

The controls in (23) are
\((-(1-\varepsilon)r_1,-(1-\varepsilon)r_2,-2\varepsilon r_p)\).
On the bounded conditioned region, for \(0<\varepsilon\le1/2\),

\[
 |r(t)|\le e^{-2\kappa(t-b)}|r(b)|+C\varepsilon,\qquad
 \int_b^t|r(s)|ds\le C|r(b)|+C\varepsilon(t-b).
 \tag{30}
\]

Indeed pair the residual equation with \(r/|r|\) away from zero, use
\(M\ge4\kappa I\), and bound \(G^*v_p\). Regularization by
\(\sqrt{|r|^2+\eta^2}\) and \(\eta\downarrow0\) covers zero residuals.
In particular the post-b control mass and raw displacement are at most

\[
 \int_b^t m(s)ds+
 C^{-1}\|\theta(t)-\theta(b)\|_{\rm raw}
 \le C|r(b)|+C\varepsilon(t-b).
 \tag{31}
\]

Here and below constants may be enlarged; the sum form of (31) is only an
upper bound, not an equality.

The next two discrete steps construct that existing segment before using
its continuous estimates. In particular (30) is not used to assume the
existence it is meant to control.

**Fixed b prefix, before any changed-program cap**

Every finite raw Euler program for the three-atom mixture exists by finite
recursion. Through a separately fixed b, its elementary readout recurrence
gives \(\|c_k\|_\infty\le e^{2b}-1\); summing its bounded-gate updates gives
finite constants for its raw norm, action norm, and interpolation speed,
depending on b but not on p, \(\varepsilon\), or the mesh. This is the direct
calculation of C.4.7.NE with T replaced by this fixed b, not an extension of
that theorem's source cap.

Compare this arbitrary mixture Euler interpolant with the already existing
actual reference on \([0,b]\), using the latter as the sole tail-bearing
endpoint. Its passive Gaussian tails follow from C.4.6.S43 or SCT. The
cutoff subtraction (11), residual differences, and the preceding-node
error give, for physical maximal mesh h,

\[
 \sup_{t\le b}d(\theta_{\varepsilon,p}^{h}(t),\theta_*(t))
 \le C_b e^{C_b(1+R)b}
       \{(1+R)(\varepsilon+h)+e^{-cR^2}\}.
 \tag{32a}
\]

The law difference at the reference is \(O(\varepsilon)\), uniformly in p;
the proxy's preceding-node error is \(O(h)\). These are the two sources
inside the first brace. No tails of the mixture Euler program enter.
Choose R proportional to \(\sqrt{\log(e/(\varepsilon+h))}\), with its
constant large enough to make the Gaussian term smaller than a fixed power
of \(\varepsilon+h\). The linear-in-R amplification is sub-power.
Thus the right side defines a modulus \(\omega_b(\varepsilon+h)\to0\).

Let \(a^h_{\varepsilon,p}\) be the piecewise constant controls of this
Euler program. Uniform scalar prediction continuity and its node error imply

\[
 D_{\varepsilon,b}^{h}:=
 \int_0^b|a^h_{\varepsilon,p}(t)-a_*(t)|_1dt
 \le C_b\{\varepsilon+h+\omega_b(\varepsilon+h)\}\longrightarrow0.
 \tag{32b}
\]

Thus actual integrated coefficient closeness, not merely a raw norm
comparison, is established before applying SCT. For fixed sufficiently small
\(\varepsilon\) and all sufficiently fine meshes these prefixes lie in a
strict SCT tube. Their subsequent Euler Cauchy completion uses the now
available mixture-program tails. This proves uniform-in-p convergence of
the completed prefix to the reference as \(\varepsilon\to0\), for every
separately fixed b, however large.

**Post-b discrete residual contraction and cap first exit**

Include b as a mesh node. Continue actual-mixture Euler with its own
population residuals. Use inner stopping thresholds \(\rho/2\) for distance
from \(\theta_\dagger\) and \(\delta_{\rm src}/2\) for the integrated control
distance; the outer raw ball and source tube have radii \(\rho\) and
\(\delta_{\rm src}\). Choose the step small enough that one update from an
inner stopped node, and its full affine segment, remains in the outer
regions. Its coefficient size is uniformly bounded there by
\(C(|r_k|+\varepsilon)\); its physical step can also be made small enough
to satisfy the dominating control-mesh threshold.

The whole finite history through each such affine segment is source
admissible, so its recomputed passive queries have uniform \(L^4\) bounds.
Along that segment the constant velocity is
\(V_k=-(1-\varepsilon)G_k r_k-2\varepsilon v_{p,k}\).
Its row \(L^4\) norm, middle HS norm, and pointwise readout derivative
are bounded by \(C(|r_k|+\varepsilon)\). Apply the proof of (24)--(26) along
this affine curve, using its fixed node velocity and its current queried
fields. It gives
\(\|(g_{e_a})'\|_{\rm raw}\le C(|r_k|+\varepsilon)\).
The scalar chain rule and a second integration therefore give the exact
Euler residual expansion

\[
 r_{k+1}=[I-h_k(1-\varepsilon)M_k]r_k
       -2h_k\varepsilon G_k^*v_{p,k}+R_k,\qquad
 |R_k|\le C h_k^2(|r_k|+\varepsilon)^2.
 \tag{32c}
\]

This is a derivative along a controlled affine step; it does not assert
ambient \(C^2\) regularity. Since \(4\kappa I\le M_k\le M_{\max}I\),
choose \(h_kM_{\max}\le1\). Then
\(\|I-h_k(1-\varepsilon)M_k\|\le1-2\kappa h_k\).
The residuals are bounded on the outer region, say by \(R_{\max}\).
Use \((|r_k|+\varepsilon)^2\le(R_{\max}+1)(|r_k|+\varepsilon)\), and
decrease the maximal step so that
\(Ch_k(R_{\max}+1)\le\kappa\). Absorbing the remainder yields

\[
 |r_{k+1}|\le(1-\kappa h_k)|r_k|+C h_k\varepsilon,\qquad
 \sum_{k:\ b\le t_k<t_N}h_k|r_k|
 \le C|r_b|+C\varepsilon(t_N-b).
 \tag{32d}
\]

The sum follows by telescoping the first inequality, not by accumulating
an \(O(hT)\) error. The post-b control mass and raw displacement obey the
same right-hand bound. These estimates are uniform in mesh and horizon
while the stopped construction is in the outer regions.

On the original physical schedule, keep the reference running throughout.
The triangle inequality after b gives, through
\(T=b+\tau_0/\varepsilon\),

\[
 \int_0^T|a^h_{\varepsilon,p}-a_*|_1dt
 \le D_{\varepsilon,b}^{h}+(s_\dagger-s_*(b))
             +C|r_b|+C\tau_0.
 \tag{33}
\]

One may pad the actual program with zero controls after T; the untruncated
reference tail is still bounded by \(s_\dagger-s_*(b)\).
No independent time change of that reference is needed.

Choose b large so that the reference endpoint error, its residual, and its
remaining control mass are much smaller than the inner margins. Then choose
\(\varepsilon+h\) small in (32a)--(32b) so that the mixture prefix has the
same properties. Finally decrease \(\tau_0>0\), uniformly in p, so that
\(C\tau_0\) and its associated raw displacement use less than one quarter of
the inner margins. Equations (32d)--(33) keep a potential first exiting node
strictly inside both inner regions. This contradicts first exit.
Thus all the Euler programs continue through \(b+\tau_0/\varepsilon\) with
uniform source caps and raw bounds.

For each fixed positive \(\varepsilon\) this is a finite physical horizon.
The one-reference Osgood comparison, now with the capped Euler paths,
makes the actual-mixture Euler programs Cauchy as their physical meshes
vanish. The argument of Section 4 passes their equations, Gaussian tails,
and scalar controls to a unique strong solution of (29).
It starts from the original initial state. The physical mesh may depend on
\(\varepsilon\); no simultaneous step/perturbation limit is claimed.
The integrated bounds pass to the limit, and the exact continuous
calculation gives (30)--(31).

The choice of \(\tau_0\) works for every sufficiently large b; only the
required smallness of \(\varepsilon\) and the proof mesh depends on b.
This proves the needed original-mixture continuation rather than assuming
it, and permits the successive limits in the next section.

###### C.7. Residual identity and singular selection

Equations (29) give the exact identity

\[
 \theta'=\varepsilon V_p(\theta)+B(\theta)r'.
 \tag{34}
\]

Indeed multiplying the residual equation by \(B=GM^{-1}\) recovers the
anchor force and subtracts precisely the normal component of the added
force. By (27), on the reached segment,

\[
 \|B'(t)\|_{\mathrm{op}}\le C(|r(t)|+\varepsilon).
\]

Combining with (30) and integrating gives

\[
 \int_b^t\|B'(s)r(s)\|_{\rm raw}ds
 \le C\{|r(b)|^2+\varepsilon|r(b)|+\varepsilon^2(t-b)\}.
 \tag{35}
\]

For example \(|r|\le a e^{-2\kappa(s-b)}+C\varepsilon\); squaring and
integrating bounds \(\int|r|^2\) by
\(Ca^2+C\varepsilon a+C\varepsilon^2(t-b)\), and the additional
\(\varepsilon\int|r|\) has the same bound.

The Hilbert-space absolutely continuous product rule now legitimately yields

\[
 \theta(t)=\theta(b)+B(t)r(t)-B(b)r(b)
       +\varepsilon\int_b^t V_p(\theta(s))ds
       -\int_b^t B'(s)r(s)ds.
 \tag{36}
\]

Set \(\widetilde\theta_{\varepsilon,b,p}(\tau)
=\theta_{\varepsilon,p}(b+\tau/\varepsilon)\).
Uniformly for \(0\le\tau\le\tau_0\), (30), (35), and (36) give

\[
 \widetilde\theta_{\varepsilon,b,p}(\tau)
 =\theta_\dagger+
       \int_0^\tau V_p(\widetilde\theta_{\varepsilon,b,p}(s))ds
       +E_{\varepsilon,b,p}(\tau),
\]
\[
 \sup_{\tau,p}\|E_{\varepsilon,b,p}(\tau)\|_{\rm raw}
 \le C\{\sup_p\|\theta_{\varepsilon,p}(b)-\theta_\dagger\|_{\rm raw}
       +\sup_p|r_{\varepsilon,p}(b)|
       +\sup_p|r_{\varepsilon,p}(b)|^2+\varepsilon\}.
 \tag{37}
\]

At fixed b the right side has limit superior at most \(Ce^{-b/5}\), by
(4) and the completed-prefix consequence of (32a)--(32b). Compare (37) with
(20), putting the constructed constrained
path on the tail-bearing side of (17). Formula (13) then gives

\[
 \limsup_{\varepsilon\downarrow0}
 \sup_{p,\tau\le\tau_0}
 \|\widetilde\theta_{\varepsilon,b,p}(\tau)-\bar\theta_p(\tau)\|_{\rm raw}
 \le {\cal O}_{\tau_0}(Ce^{-b/5}).
 \tag{38}
\]

Send b to infinity. For original, unshifted slow time and any fixed
\(0<\tau_{\min}<\tau_0\), write
\(\sigma=\tau-\varepsilon b\ge0\) for small \(\varepsilon\).
Then
\(\theta_{\varepsilon,p}(\tau/\varepsilon)
=\widetilde\theta_{\varepsilon,b,p}(\sigma)\), while
\(\|\bar\theta_p(\tau)-\bar\theta_p(\sigma)\|\le C\varepsilon b\).
Equation (38) proves

\[
 \lim_{\varepsilon\downarrow0}
 \sup_{p\in\mathcal P}\sup_{\tau_{\min}\le\tau\le\tau_0}
 \|\theta_{\varepsilon,p}(\tau/\varepsilon)-\bar\theta_p(\tau)\|_{\rm raw}=0.
 \tag{39}
\]

The reference path is compared at the same physical times and tends to
\(\theta_\dagger\) uniformly on this interval. The exclusion of \(\tau=0\)
in (39) is necessary: the actual original state at physical zero is not the
fitted endpoint. The reference-prefix decomposition proves the limit and
does not change the optimizer.

The bounds for forward actions and the scalar prediction on bounded raw sets
are uniform in the circle input. They therefore turn (39) into whole-circle
prediction convergence and uniform \(L^2\) activation convergence.
The physical scale is \(t=\tau/\varepsilon\), obtained from the exact
projected force in (34). No finite-order law-response expansion has been
extended to this scale.

##### Proof unit D. Actual finite gradient flow and paired observations

###### D.1. Fixed-horizon population-to-finite bridge

Fix one positive epsilon and one admitted added law, and a finite physical
horizon T (which may equal tau0/epsilon). Suppose controlled population Euler
programs for its actual mixture GF converge strongly on [0,T] to a unique
population path theta, with the following bounds uniform in sufficiently fine
Euler partitions: ordinary raw state ball; readout essential supremum;
passive-query second-moment tails

    tau_R(Q(u)) + tau_R(c) <= C exp(-a R^2),  R>=1,

for every training and finitely named observation input. Constants may depend
on the fixed epsilon and T. Here tau_R(v)=||v 1_{|v|>R}||_2; any equivalent
soft cutoff can be used in intermediate convergence arguments. Assume all these
Euler programs live on the same initialized Gaussian carrier and use its actual
forward action and actual adjoint. Their strong limit determines predictions
by f_theta(u)=<c,tanh((A0+K)tanh(w.u))>.

Then the actual width-n mixture GF, starting at the prescribed independent
Gaussian arrays with their actual nonzero readout, converges in probability to
this prediction in C([0,T]xS1). For every finite list of times and inputs, its
first-row, forward hidden, upper gate, readout, and actual forward/adjoint-query
fields have the joint same-layer observation limits supported by the maintained
finite-program theorem and its second-moment extension. This includes paired
second-hidden activation distances between mixture and reference flows using
the same initialized arrays. No unknown finite-width endpoint is introduced.

###### D.2. Proof

At width n all vector and matrix norms are ordinary Euclidean, Frobenius or
operator norms. The raw state-increment metric is

    d_n^2=||W1-W1bar||_F^2/n+||W2-W2bar||_F^2+||c-cbar||_2^2/n.

For a finite vector q define the empirical RMS hard and soft tails

    tau_(R,n)(q)=||q 1_{|q|>R}||_2/sqrt(n),
    sigma_(R,n)(q)=||(|q|-R)_+||_2/sqrt(n).

These are distinct from the population L2 tails tau_R in D.1. All finite
field errors below use the same explicit RMS normalization. In particular,
tau_(R,n)(q)<=2 sigma_(R/2,n)(q), and sigma_(R,n) is one-Lipschitz for
the normalized Euclidean distance. Its square is a continuous empirical
second-moment observation of a fixed finite program.

The initialized middle action itself is bounded in operator norm, rather than
Frobenius norm; only its increments enter d_n. Work on initial events on which
its operator norm, the first-row second moment and initial loss are bounded.
Their probabilities tend to one by the established Gaussian initialization
bounds and laws of large numbers. The actual initial readout has entries of
standard deviation 1/n. Its maximum tends to zero in probability, because
Pr(max_j |c0,j|>eta)<=2n exp(-n^2 eta^2/2). Its normalized second moment also
tends to zero. It is retained in every finite array and proxy, never set to zero.

The finite GF is global at every n. Its smooth vector field is locally
Lipschitz in finite dimensions; unhalved loss dissipation gives
integral_0^T ||theta_n'||_raw^2 <= L_n(0). Hence its raw displacement is at most
sqrt(T L_n(0)). This bounds the action norm by its initialized norm plus the
Frobenius increment. Also |c_n'(j)|<=2 integral |f_n-y| dmu <=2 sqrt(L_n(0)),
so ||c_n(t)||_infty<=||c_n(0)||_infty+2T sqrt(L_n(0)). These bounds imply a
finite raw velocity bound on [0,T], uniform on the preceding initial events.
They justify continuation and every subsequent comparison; they do not provide
the decisive population query tails.

Fix a finite Euler partition h and freeze the *population Euler program's*
scalar training coefficients. Run that exact finite program on the actual
Gaussian arrays, including their initial readout. Call it the finite proxy.
It uses every actual middle multiplication and its actual transpose; no
independent replacement is made. The fixed-program neural law and its
at-most-quadratic observation extension show convergence of all its finitely
named fields, scalar contractions and second moments to their population
program values. The small initial readout passes by a fixed-oracle cutoff induction, rather
than a dimension-dependent finite-dimensional Lipschitz bound. First construct
the finite oracle with zero limiting readout instructions and the same actual
first/middle arrays. Its fixed nodes have the proved joint second-moment laws.
Compare the actual-readout proxy to that oracle, keeping its Gaussian readout
additively in the former. The initial raw error tends to zero. At a coordinate
update, every changed bounded gate multiplying an oracle L2 field is split at
a fixed cutoff R: its bounded part is controlled by the preceding raw error,
and its remaining normalized error by tau_(R,n) of that oracle field.
Bound this hard tail by twice sigma_(R/2,n); the normalized soft tail
converges at fixed program and R by the node's second-moment law. Its
population limit tends to zero as R tends to infinity. Direct action and rank subtractions handle the other
terms. Induction through the finite number of nodes therefore gives raw error
tending to zero at every node. Readout suprema stay bounded on the initial
events because the update is a sum of bounded tanh values and the actual
initial maximum vanishes. No uniform Lipschitz constant on arbitrary
width-dependent parameter balls is assumed. This is the fixed-program
extension used by C.4.7; the zero-readout object is only a comparison oracle,
never a replacement for an actual finite run or its actual-readout proxy.
In particular, the discrepancy between a proxy prediction at an update input
and its population coefficient's prediction tends to zero. Denote the maximum
of these finitely many discrepancies by zeta_(n,h); then zeta_(n,h)->0 in
probability for fixed h.

For clarity, the comparison can be made at every left Euler endpoint and its
affine interpolation. The interpolation stays on a common raw ball. Its
recomputed normalized soft tails of c and Q converge at a fixed cutoff to
the corresponding population L2 soft tails. One may first name a finite
additional interpolation grid; the forward/action maps are Lipschitz for
normalized finite field norms on this ball with bounded readout, and the
proxy raw interpolation speed is bounded. The soft tails sigma_(R,n)(Q)
and sigma_(R,n)(c) pass to the fixed-program limit and are one-Lipschitz
in the corresponding normalized field distances.
A finer interpolation grid and the elementary inequalities relating hard tails
at R to soft tails at R/2 give the asserted bound uniformly over interpolation
time, with enlarged constants. No growing transcript is taken before width.

Subtract actual GF from the affine proxy. The one-reference product inequality
is elementary: for a bounded Lipschitz gate b and an arbitrary comparison
vector qbar,

    ||(b(z)-b(zbar))qbar||_2/sqrt(n)
                <= C R ||z-zbar||_2/sqrt(n) + C tau_(R,n)(qbar).

Apply it to the lower gate multiplier with the proxy Q as qbar and to the
upper multiplier with proxy c. Direct bounded-operator subtraction handles Q
itself. For finite middle updates the rank identity is

    ||a b^T/n||_F=(||a||_2/sqrt(n))(||b||_2/sqrt(n)).

It is the finite counterpart of the population identity
||a tensor b||_HS=||a||_2||b||_2. Prediction residual subtraction is bounded by
the raw distance on the common ball. The frozen coefficient error contributes
zeta_(n,h), and the interpolation defect contributes O(h_max). Thus, for each
fixed cutoff R and the fixed T,

    sup_[0,T] d_n <= C_T exp(C_T R) [
       (1+R)(h_max+zeta_(n,h))
       + sup_proxy_time (tau_(R,n)(c_proxy)
                          +sum_j p_j tau_(R,n)(Q_proxy(u_j))) ].

The two finite states have identical initial arrays, so there is no initial
state error in this inequality. The actual initial Gaussian readout remains
inside both states and the harmless uniform initial bounds above.

Take n->infinity with the partition and cutoff fixed. Convergence of the
normalized soft tails, the hard-to-soft inequality above and the population
Gaussian tails bound the width limsup of the proxy-tail terms by C exp(-a'R^2);
zeta_(n,h) vanishes. For any desired
comparison error, first choose R large enough that
C_T exp(C_T R-a'R^2) is smaller than that error, then choose h_max small enough
that its amplified interpolation defect is smaller still. Both choices are
finite at every fixed positive epsilon. This proves proximity of finite GF to
the finite proxy in probability, with arbitrarily small prescribed error.
Strong population Euler completion then identifies the unique population path.
One does not send R to infinity at a fixed positive mesh, or claim uniform
width rates as epsilon tends to zero.

On each common raw ball,

    sup_u |f_theta(u)-f_thetabar(u)| <= C_T d(theta,thetabar),
    ||H2_theta(u)-H2_thetabar(u)||_2 <= C_T d(theta,thetabar).

These displays use the population raw metric and population L2 norm. Their
finite counterparts, for the two finite states under comparison, are

    sup_u |f_(n,theta)(u)-f_(n,thetabar)(u)| <= C_T d_n,
    ||h2_(n,theta)(u)-h2_(n,thetabar)(u)||_2/sqrt(n) <= C_T d_n.

The input Lipschitz constants are bounded by products of the readout, action
and first-row norms; at finite width these are ||c||_2/sqrt(n), the middle
operator norm and ||W1||_F/sqrt(n). H1 and H2 satisfy the corresponding
population L2 and finite RMS input estimates.
Consequently finite input nets upgrade proxy prediction convergence to the
whole circle, uniformly in physical time using the same velocity bounds.
This proves the claimed C([0,T]xS1) convergence.

For joint reference/mixture observations, use the union of their finite proxy
programs on the SAME Gaussian arrays and the finite-program joint law. Paired
bounded activation products are permitted second-moment observations. Both
finite flows are close to their proxies in the normalized hidden norms, so
Cauchy–Schwarz passes each mixed inner product and squared distance. Reference
capture is required only on this fixed finite T, where the established result
applies. The endpoint appears only afterwards, through the proved population
reference convergence as epsilon tends to zero and T=tau/epsilon tends to
infinity. Thus the paired finite statistic at time T converges to

    (1/m) sum_i ||H2_theta_mu(T)(u_i)-H2_theta_*(T)(u_i)||_2^2.

Combining the population selection theorem of proof unit C with the already
proved reference endpoint convergence gives its constrained-path versus latent
endpoint limit. This order keeps the actual common initialization intact.

##### Completion of the theorem

Take the common constrained existence time from proof unit C as the
\(\tau_{ex}\) used in proof unit B, and use B's smaller positive time as
our final \(\tau_0\). Decreasing a time already constructed preserves every
source bound, uniqueness statement and mixture continuation estimate. Set
\(a=\eta_R\) from (5.5) and \(j=\eta_H\) from (5.7), both in proof unit B.
They depend only on the fixed reference and parameter rectangle.

Proof unit C proves (NS5) uniformly over that rectangle, in the original
unshifted physical times \(t=\tau/\epsilon\). Its original-mixture Euler
programs verify all the population hypotheses of proof unit D for each fixed
positive \(\epsilon\). Thus D proves (NS8) and the joint same-array
observation contract. At \(T_\epsilon\), the population reference tends
strongly to \(\theta_\dagger\). The forward field inequalities therefore
identify (NS9)'s limit with (NS7), using paired programs on the same initialized
arrays, followed only then by \(\epsilon\downarrow0\).

On the common bounded prediction region, squared loss at the one added atom
is continuous. Hence the probability that
\(R_{\nu}(F_*)-R_{\nu}(f_{n,\mu_\epsilon}(T_\epsilon))\ge a/2\)
and \(J_{2,n,\epsilon}\ge j/2\) tends to one in the displayed iterated order.
This verifies every assertion of the theorem. The state reconstruction retains
the evolving hidden features and actual adjoint throughout the episode.

