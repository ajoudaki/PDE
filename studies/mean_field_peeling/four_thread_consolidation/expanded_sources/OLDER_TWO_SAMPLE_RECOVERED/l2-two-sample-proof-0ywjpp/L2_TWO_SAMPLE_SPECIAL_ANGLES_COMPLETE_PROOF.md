# A complete two-input, two-hidden-layer theorem at the two special angles

This theorem concerns only the input correlations \(\rho=0\) and
\(\rho=-1\). Both activations are \(\arctan\). It establishes the
canonical finite-width limit, a unique autonomous population flow on
every finite physical interval, and persistent nonlinear hidden learning.
It is not an all-angle theorem. All mathematical arguments needed below
are included in this document.

## 1. Model, normalization, and theorem

**1.1. Finite model and physical clock.** Fix a positive integer \(d\), two
deterministic inputs \(x_1,x_2\in\mathbb R^d\) with
\(\|x_1\|_{\mathbb R^d}=\|x_2\|_{\mathbb R^d}=\sqrt d\), and
\[
 C_{ab}=d^{-1}x_a^Tx_b,\qquad C_{12}=\rho\in\{0,-1\},
 \qquad (y_1,y_2)=(1,-1).
 \tag{1}
\]
The case \(\rho=0\) requires \(d\ge2\). At \(\rho=-1\), necessarily
\(x_2=-x_1\). The two hidden widths are both \(n\). Independently initialize
\[
 W^{(1)}_{n,ij}(0)\sim N(0,1/d),\qquad
 W^{(2)}_{n,ij}(0)\sim N(0,1/n),\qquad
 W^{(3)}_{n,i}(0)\sim N(0,n^{-2}),
 \tag{2}
\]
where the shapes are \(n\times d,n\times n,n\), respectively.
\(W^{(3)}_n\) denotes the rescaled readout used in the following prediction;
no further readout rescaling is understood. Put
\[
 \phi(z)=\arctan z,\qquad \phi'(z)=\frac1{1+z^2},
 \qquad \phi''(z)=\frac{-2z}{(1+z^2)^2},\qquad B=\pi/2.
 \tag{3}
\]
For \(a=1,2\),
\[
 \begin{aligned}
 z^{(1)}_{n,a}&=W^{(1)}_nx_a,& h^{(1)}_{n,a}&=\phi(z^{(1)}_{n,a}),\\
 z^{(2)}_{n,a}&=W^{(2)}_nh^{(1)}_{n,a},&h^{(2)}_{n,a}&=\phi(z^{(2)}_{n,a}),\\
 f_{n,a}&=\frac1n(W^{(3)}_n)^Th^{(2)}_{n,a},&r_{n,a}&=f_{n,a}-y_a,\\
 L_n&=r_{n,1}^2+r_{n,2}^2.&&
 \end{aligned}                                                   \tag{4}
\]
All activations act coordinatewise. Define the backward fields without
residual factors by
\[
 \delta^{(2)}_{n,a}=W^{(3)}_n\phi'(z^{(2)}_{n,a}),\qquad
 q^{(1)}_{n,a}=(W^{(2)}_n)^T\delta^{(2)}_{n,a},\qquad
 \delta^{(1)}_{n,a}=\phi'(z^{(1)}_{n,a})q^{(1)}_{n,a}.
 \tag{5}
\]
The raw updates, with every quantity on the right evaluated at step
\(k\), are exactly
\[
 \begin{aligned}
 W^{(1)}_{n,k+1}&=W^{(1)}_{n,k}
       -\frac{2\eta_n}{d}\sum_a r_{n,ka}\delta^{(1)}_{n,ka}x_a^T,\\
 W^{(2)}_{n,k+1}&=W^{(2)}_{n,k}
       -\frac{2\eta_n}{n}\sum_a r_{n,ka}\delta^{(2)}_{n,ka}
                                                   (h^{(1)}_{n,ka})^T,\\
 W^{(3)}_{n,k+1}&=W^{(3)}_{n,k}
       -2\eta_n\sum_a r_{n,ka}h^{(2)}_{n,ka},\qquad \eta_n=n^{-2}.
 \end{aligned}                                                   \tag{6}
\]
Thus physical time is \(t=k\eta_n\), without an additional time change.
Between nodes interpolate these three raw parameter arrays linearly,
and recompute (4)--(5) from the interpolated arrays. Velocities at
interior nodes mean right velocities, and at a terminal node mean left
velocities. The actual Gaussian readout in (2) is retained throughout.

For precision, (6) is gradient descent for loss SUM in the parameter
metric
\[
 \|(E^{(1)},E^{(2)},E^{(3)})\|_{\mathrm{par},n}^2
  =\frac d n\|E^{(1)}\|_F^2+\|E^{(2)}\|_F^2
                                      +\frac1n\|E^{(3)}\|_{\ell^2}^2.
 \tag{7}
\]
Indeed the ordinary Euclidean gradients are respectively
\((2/n)\sum r_a\delta^{(1)}_ax_a^T\),
\((2/n)\sum r_a\delta^{(2)}_a(h^{(1)}_a)^T\), and
\((2/n)\sum r_ah^{(2)}_a\); applying the inverse metric gives (6).
Specifying this metric is essential: ordinary Euclidean descent on all
three displayed rescaled arrays would be a different model. Finite
gradient flow means the right sides of (6) divided by \(\eta_n\).

**1.2. Spaces and the population equations.** The two finite neuron
spaces are separate copies of \(\mathbb R^n\). We use ordinary
Euclidean norms and display empirical normalization explicitly:
\[
 \frac1n v^Tw,\qquad
 \frac1n\|v\|_{\ell^2}^2=\frac1n\sum_i|v_i|^2.
 \tag{8}
\]
In particular \(W^{(2)}_n\) acts by ordinary matrix multiplication;
there is no extra \(1/n\) in its action. Its adjoint is its actual
transpose. For two probability spaces to be constructed, write
\(\mathcal H_\ell=L^2(\Omega_\ell,\mu_\ell)\),
\(\|v\|_{\mathcal H_\ell}^2=\mathbb E_\ell|v|^2\). Products are
pointwise on the indicated space. The rank-one operator
\[
 (v\otimes h)e=v\mathbb E_1[he],\qquad
 \|v\otimes h\|_{\mathrm{op}}=\|v\otimes h\|_{\mathrm{HS}}
                =\|v\|_{\mathcal H_2}\|h\|_{\mathcal H_1}
 \tag{9}
\]
is \(vh^T/n\) at finite width. The finite Hilbert--Schmidt norm is
the ordinary Frobenius norm; the finite operator norm is the ordinary
Euclidean operator norm.
In the infinite spaces, the operator norm is
\(\sup_{\|e\|_2=1}\|We\|_2\), and the squared Hilbert--Schmidt norm
is \(\sum_j\|We_j\|_2^2\) for an orthonormal basis of the domain.
For (9), expansion of \(h\) in that basis gives the asserted norm
identity directly.

The population state consists of a first-row field
\(W^{(1)}(t)\in L^2(\Omega_1;\mathbb R^d)\), a bounded operator
\(W^{(2)}(t):\mathcal H_1\to\mathcal H_2\) with Hilbert--Schmidt
increments, and \(W^{(3)}(t)\in\mathcal H_2\). Set
\[
 \begin{aligned}
 Z^{(1)}_a&=W^{(1)}x_a,&H^{(1)}_a&=\phi(Z^{(1)}_a),\\
 Z^{(2)}_a&=W^{(2)}H^{(1)}_a,&H^{(2)}_a&=\phi(Z^{(2)}_a),\\
 f_a&=\mathbb E_2[W^{(3)}H^{(2)}_a],&r_a&=f_a-y_a,\\
 \delta^{(2)}_a&=W^{(3)}\phi'(Z^{(2)}_a),&
 Q^{(1)}_a&=W^{(2)*}\delta^{(2)}_a,\\
 \delta^{(1)}_a&=\phi'(Z^{(1)}_a)Q^{(1)}_a,&L&=\sum_a r_a^2.
 \end{aligned}                                                   \tag{10}
\]
The star is the actual Hilbert adjoint on these two separate spaces.
The autonomous physical equations are
\[
 \begin{aligned}
 \dot W^{(1)}&=-\frac2d\sum_a r_a\delta^{(1)}_ax_a^T,
 &\dot Z^{(1)}_a&=-2\sum_b C_{ab}r_b\delta^{(1)}_b,\\
 \dot W^{(2)}&=-2\sum_a r_a\delta^{(2)}_a\otimes H^{(1)}_a,
 &\dot W^{(3)}&=-2\sum_a r_aH^{(2)}_a.
 \end{aligned}                                                   \tag{11}
\]
Initialize the first row by independent \(N(0,1/d)\) coordinates,
write \(G_a=W^{(1)}(0)x_a\), and initialize \(W^{(3)}(0)=0\).
The initial \(W^{(2)}(0)\), including its joint law with every generated
field and its adjoint, is constructed in Section 3; an arbitrary bounded
operator does not suffice.

**1.3. The assertion and its observable scope.** There are countably
generated spaces and this canonical operator, with
\(\|W^{(2)}(0)\|_{\mathrm{op}}\le8\), on which (11) has a unique
solution for all finite \(t\ge0\). Its law is deterministic and is the
full-sequence limit in probability of (6), and also of finite gradient
flow from (2), on every fixed \([0,T]\), \(T<\infty\). It is unique
from each reached state, with the entire state retained at restart.

Here is the precise joint meaning of this limit. In each neuron
population separately, empirical same-neuron tuples include both samples
and all their hidden forward and backward fields. Their path laws on
\(C([0,T];\mathbb R^j)\), with the supremum norm, converge in every
fixed Wasserstein order \(1\le p<\infty\). In population 1 the tuple
may contain \(W^{(1)},Z^{(1)}_a,H^{(1)}_a,Q^{(1)}_a,
\delta^{(1)}_a\); in population 2 it may contain
\(W^{(3)},Z^{(2)}_a,H^{(2)}_a,\delta^{(2)}_a\). Finite lists of
times, fields, and continuous polynomial-growth tests converge jointly.
No artificial pairing of neurons in different populations is asserted.
Here the order-\(p\) Wasserstein distance on a metric space is the
infimum, over all couplings of the two probability laws, of
\((\mathbb E[\operatorname{dist}(X,Y)^p])^{1/p}\).

Predictions, loss, and all three kernel blocks converge uniformly in
\(t\in[0,T]\), in probability, to
\[
 \begin{aligned}
 K^{(1)}_{ab}&=C_{ab}\mathbb E_1[\delta^{(1)}_a\delta^{(1)}_b],\\
 K^{(2)}_{ab}&=\mathbb E_2[\delta^{(2)}_a\delta^{(2)}_b]
                      \mathbb E_1[H^{(1)}_aH^{(1)}_b],\\
 K^{(3)}_{ab}&=\mathbb E_2[H^{(2)}_aH^{(2)}_b],\qquad
 K=K^{(1)}+K^{(2)}+K^{(3)}.
 \end{aligned}                                                   \tag{12}
\]
The finite formulas use precisely (8). For either matrix orientation,
the assertion also includes any fixed finite collection of admissible
probes and their joint field laws in Wasserstein order 2. An admissible
probe is formed by a fixed finite program from the initialization, independent
iid roots with every finite moment, deterministic linear combinations,
smooth globally Lipschitz coordinate maps with bounded first derivatives,
empirical products with factor \(1/n\), actions of \(W^{(2)}_n(0)\) or its transpose,
and the learned rank integrals at prescribed times. Its instructions,
scalar coefficients, and additional-root laws are fixed as width varies,
apart from the explicitly specified model normalizations; arbitrary
width-dependent amplification of the vanishing initial readout is not
an admissible instruction. Limits of such
probes are admitted when their approximation errors vanish in ordinary
normalized \(L^2\), uniformly in probability at finite width, and in
population \(L^2\). This definition includes the unbounded velocity
probes proved admissible in Section 4; it does not quantify over arbitrary
width-dependent directions. At population level actions are those of
\(W^{(2)}(t)\) and \(W^{(2)*}(t)\).

Every preactivation and activation velocity in (73) has joint
Wasserstein-2 convergence
at fixed times, convergence in integrated mean square under the
approximations used below, and convergence of its squared normalized
norm uniformly in time in probability. The same holds for the readout
velocity. The raw parameter speeds converge in their metrics
\[
 \frac d n\|\dot W^{(1)}_n\|_F^2,\qquad
 \|\dot W^{(2)}_n\|_F^2,\qquad
 \frac1n\|\dot W^{(3)}_n\|_{\ell^2}^2,                       \tag{13}
\]
and so do their time integrals and the individual hidden-velocity
energies. The squared sizes of parameter increments converge in the
analogous quadratic metrics; the middle statement concerns
\(W^{(2)}(t)-W^{(2)}(0)\),
not a Hilbert--Schmidt norm of the initial operator. There is no claim
of operator-norm convergence between matrices of different dimensions.

At every finite \(t\ge0\), for each \(\ell=1,2\) and sample \(a\),
\[
 \inf_{u,v\in\mathbb R}
  \mathbb E_\ell[(\phi(Z^{(\ell)}_a(t))-uZ^{(\ell)}_a(t)-v)^2]>0.
 \tag{14}
\]
At every physical \(t>0\), all four preactivation speeds, all four
activation speeds, both hidden-parameter speeds and the readout speed
are strictly positive in their stated norms. The limiting population
hidden speeds at zero are zero. The full kernel is nonconstant on every sufficiently short
interval starting at zero: in the label direction its first nonzero
change has a strictly positive quadratic coefficient in physical time.

The proof first constructs the deterministic global flow for a specified
operator. It then proves the finite Gaussian program law, builds the
canonical operator, and obtains global bounded Gaussian remainders by
fresh-root forcing. Deterministic mesh comparisons give the full
observable limit. Finally the exchange symmetry, Gaussian tails, and
an initial expansion prove (14), strict motion, and kernel change.

## 2. Deterministic flow, restart, and the raw discretization

**2.1. The special-angle coordinate.** Introduce the one auxiliary
scalar function and its inverse
\[
 F(z)=z+z^3/3,\qquad U_a=F(Z^{(1)}_a),\qquad Z^{(1)}_a=F^{-1}(U_a).
 \tag{15}
\]
The finite version is \(u_{n,a}=F(z^{(1)}_{n,a})\).
Since \(F'\ge1\), its inverse is defined on all of \(\mathbb R\),
is 1-Lipschitz, and has derivative \(\phi'(F^{-1}(u))\).
The function \(\phi(F^{-1}(u))\) has derivative
\(\phi'(F^{-1}(u))^2\), also bounded by 1. Further,
\(|\phi|\le B\), \(0<\phi'\le1\), and \(|\phi''|\le1\).
All source derivatives used below are continuous; repeated scalar
differentiation of these rational expressions supplies bounded
higher derivatives when needed. The Gaussian root satisfies
\(\mathbb E F(G_a)^2=1+2+15/9=14/3\).
The moments used here follow by scalar Gaussian integration by parts:
\(\mathbb E G^{2j}=(2j-1)\mathbb E G^{2j-2}\), starting with
\(\mathbb E1=1\).

For \(\rho=0\), with prescribed integrable controls \(c_a\), use
\[
 \dot U_a=c_aQ^{(1)}_a,\qquad
 \dot W^{(2)}=\sum_a c_a\delta^{(2)}_a\otimes H^{(1)}_a,
 \qquad \dot W^{(3)}=\sum_a c_aH^{(2)}_a.                    \tag{16}
\]
Physical feedback is \(c_a=-2r_a\). The cancellation
\(F'(Z)\phi'(Z)=1\) makes (16) exactly (11).

For \(\rho=-1\), at every raw parameter state,
\[
 Z^{(\ell)}_2=-Z^{(\ell)}_1,\quad H^{(\ell)}_2=-H^{(\ell)}_1,
 \quad f_2=-f_1,\quad
 \delta^{(\ell)}_2=\delta^{(\ell)}_1,\quad Q^{(1)}_2=Q^{(1)}_1.
 \tag{17}
\]
These identities follow from opposite inputs, odd activations, and even
derivatives, and require no restriction on the readout. Retain one
independent first field in (16), replace the summed control by
\(c=c_1-c_2\), and use sample 1 in every right side. Physical feedback
is \(c=-4r_1\); the factor four is forced by loss SUM. Equivalently,
on the invariant two-sample state,
\(\dot U_a=\sum_b C_{ab}c_bQ^{(1)}_b\).

The first row is reconstructed, including its unchanged orthogonal
component, by
\[
 W^{(1)}(t)=W^{(1)}(0)+\sum_{a=1}^{m_\rho}
             (Z^{(1)}_a(t)-G_a)x_a^T/d,
 \quad m_\rho=2\ (\rho=0),\quad m_\rho=1\ (\rho=-1).
 \tag{18}
\]
Thus \(d\mathbb E_1|\dot W^{(1)}|^2=\sum_{a=1}^{m_\rho}
\|\dot Z^{(1)}_a\|_{\mathcal H_1}^2\); at finite width it is
\((d/n)\|\dot W^{(1)}_n\|_F^2\). Opposite sample fields do not count
the same first-matrix motion twice.

**2.2. Ordinary \(L^2\) stability.** Use the Banach norm
\[
 \sum_{a=1}^{m_\rho}\|\Delta U_a\|_{\mathcal H_1}
   +\|\Delta W^{(2)}\|_p+\|\Delta W^{(3)}\|_{\mathcal H_2},
 \qquad p=\mathrm{op}\text{ or }\mathrm{HS}.                 \tag{19}
\]
For \(p=\mathrm{HS}\) the operator coordinate is its increment from
the fixed initial operator. Suppose two states have operator norms at
most \(a_0'\) and readout essential suprema at most \(M\). Write
\(e_a=\|U_a-\widetilde U_a\|_2\),
\(e_W=\|W^{(2)}-\widetilde W^{(2)}\|_p\), and
\(e_3=\|W^{(3)}-\widetilde W^{(3)}\|_2\), where each unmarked
\(L^2\) norm is on the field's own probability space. Direct subtraction
gives
\[
 \begin{aligned}
 \|Z^{(1)}_a-\widetilde Z^{(1)}_a\|_2,
 \|H^{(1)}_a-\widetilde H^{(1)}_a\|_2&\le e_a,\\
 \|Z^{(2)}_a-\widetilde Z^{(2)}_a\|_2,
 \|H^{(2)}_a-\widetilde H^{(2)}_a\|_2&\le a_0'e_a+Be_W,\\
 \|\delta^{(2)}_a-\widetilde\delta^{(2)}_a\|_2
              &\le e_3+M(a_0'e_a+Be_W),\\
 \|Q^{(1)}_a-\widetilde Q^{(1)}_a\|_2
              &\le a_0'e_3+M(a_0')^2e_a+M(a_0'B+1)e_W,\\
 \|\delta^{(2)}_a\otimes H^{(1)}_a
      -\widetilde\delta^{(2)}_a\otimes\widetilde H^{(1)}_a\|_p
              &\le Be_3+M(Ba_0'+1)e_a+MB^2e_W,\\
 |f_a-\widetilde f_a|&\le Be_3+M(a_0'e_a+Be_W).
 \end{aligned}                                                   \tag{20}
\]
For example, split the delta difference into the readout difference
times \(\phi'\) and the bounded second readout times the difference
of \(\phi'\). Split a rank difference into two rank-one terms and
apply (9). These proofs use neither a bound on \(Q^{(1)}\) in
\(L^\infty\) nor a bounded \(L^p\) action of the operator for \(p\ne2\).
They prove local Lipschitz bounds for the transformed physical field,
depending only on \(a_0',M\), uniformly in width.

To construct a solution despite the \(L^\infty\) ball not being open
in \(L^2\), replace occurrences of the readout in predictions and
deltas by its pointwise clipping to \([-M,M]\). Clipping is
1-Lipschitz in \(L^2\). On a small ball in (19) the resulting vector
field is bounded and Lipschitz. On continuous paths staying in that
ball, its integral map preserves the ball if time times the drift bound
is less than the radius, and contracts if time times the Lipschitz
constant is less than 1. Successive iterates are a geometrically Cauchy
sequence in the complete path space. The limit solves the equation;
the same inequality proves uniqueness. For integrable controls use
their accumulated absolute integral instead of interval length.

The readout integral gives
\[
 \|W^{(3)}(t)-W^{(3)}(0)\|_\infty\le BS(t),\quad
 S(t)=\int_0^t\sum_a|c_a(v)|\,dv,                            \tag{21}
\]
where the reduced case uses \(S=\int|c|\). Choosing \(M\) larger
than the initial readout bound and an initially short interval makes
the clipping inactive. This constructs the original solution. If two
solutions stay in fixed bounds, subtraction of their integral equations
gives
\[
E(t)\le E(0)+C\int_0^t\sum_a|c_a|E
                  +C\int_0^t\sum_a|c_a-\widetilde c_a|.
\]
Iterating this inequality, or multiplying its absolutely continuous
scalar majorant by \(\exp(-C S(t))\), proves
\[
 E(t)\le e^{CS(t)}\left(E(0)+C\int_0^t\sum_a
                                      |c_a-\widetilde c_a|\right).
 \tag{22}
\]
Here \(C\) is a scalar bound depending on the two state bounds,
not the input Gram. For physical feedback, (20) instead gives
\(E(t)\le e^{C_Tt}E(0)\). If the initial operators agree, operator
differences may be measured in Hilbert--Schmidt norm. If they differ,
measure their initial difference in operator norm. Their evolved
increments relative to the respective initial operators may still
be compared in Hilbert--Schmidt norm: in the rank-difference estimate
(20), bound the full operator difference by the initial operator-norm
difference plus the Hilbert--Schmidt difference of those increments,
and apply the same integral inequality.

**2.3. Global extension and energy.** Put
\(a_0=\|W^{(2)}(0)\|_{\mathrm{op}}\),
\(b_2=\|W^{(3)}(0)\|_2\), \(b_\infty=\|W^{(3)}(0)\|_\infty\).
Integration of the rank equation and (21) gives
\[
 \begin{aligned}
 \|W^{(3)}(t)\|_2&\le b_2+BS(t),&
 \|W^{(3)}(t)\|_\infty&\le b_\infty+BS(t),\\
 \|W^{(2)}(t)-W^{(2)}(0)\|_p
     &\le Bb_2S(t)+\tfrac12B^2S(t)^2,&
 \|W^{(2)}(t)\|_{\mathrm{op}}
     &\le a_0+Bb_2S(t)+\tfrac12B^2S(t)^2,\\
 \sum_a\|U_a(t)-U_a(0)\|_2
     &\le\int_0^{S(t)}(a_0+Bb_2v+B^2v^2/2)(b_2+Bv)\,dv.
 \end{aligned}                                                   \tag{23}
\]
These bounds imply extension on any finite interval of finite action:
the derivative is bounded by an integrable scalar times a fixed
constant, so the state has a limit in (19) at any finite candidate
endpoint. The readout is also Cauchy in \(L^\infty\) by (21).
The local construction at that limit extends the solution.

Here and below composition can be differentiated along a \(C^1\)
\(L^2\) curve when the scalar map has bounded continuous derivative.
To prove this, replace \(v(t+h)\) by \(v(t)+h\dot v(t)\); the
Lipschitz bound makes the difference-quotient error tend to zero.
For the fixed direction \(\dot v(t)\), scalar difference quotients
converge pointwise and are bounded by a constant times \(|\dot v(t)|\).
Dominated convergence of their squares proves the \(L^2\) chain rule.
This is a statement along curves, not an assertion of Fréchet
differentiability of every composition map on \(L^2\).

Differentiate (10) and move \(W^{(2)}\) through its actual adjoint.
The three parameter contributions give, respectively, the three blocks
in (12), hence
\[
 \dot f=-2Kr,\qquad
 \dot L=-4r^TKr
  =-\left(\sum_{a=1}^{m_\rho}\|\dot Z^{(1)}_a\|_2^2
       +\|\dot W^{(2)}\|_{\mathrm{HS}}^2
       +\|\dot W^{(3)}\|_2^2\right).                         \tag{24}
\]
Each block is positive semidefinite: it is the Gram of
\((x_a/\sqrt d)\otimes\delta^{(1)}_a\), of
\(\delta^{(2)}_a\otimes H^{(1)}_a\), or of \(H^{(2)}_a\),
respectively. In the antiparallel reduction the first term in (24)
contains one field. For \(R_0=\sqrt{L(0)}\),
\[
 \|r(t)\|_{\mathbb R^2}\le R_0,\quad
 S(t)\le2\sqrt2R_0t,\quad
 \int_0^T\left(\sum_{a=1}^{m_\rho}\|\dot Z^{(1)}_a\|_2^2
  +\|\dot W^{(2)}\|_{\mathrm{HS}}^2+\|\dot W^{(3)}\|_2^2\right)dt
                =L(0)-L(T).                                 \tag{25}
\]
Equations (23)--(25) prove global existence. For population zero
readout, \(L(0)=2\), \(S(t)\le4t\), and in particular
\[
 \|W^{(3)}(t)\|_\infty\le4Bt,\qquad
 \|W^{(2)}(t)\|_{\mathrm{op}}\le8+8B^2t^2.                  \tag{26}
\]

Uniqueness also holds among ordinary \(L^2\) solutions of the original
integral equations, rather than only the transformed class. Such a
solution has continuous residuals; its readout integral gives a local
essential bound. Its first equation has the form
\(\dot Z=c\phi'(Z)Q\), with \(cQ\) integrable in \(L^2\).
Fubini supplies an absolutely continuous scalar representative at
almost every neuron. The scalar chain rule there gives
\[
 F(Z(t))=F(Z(0))+\int_0^t c(v)Q(v)\,dv                       \tag{27}
\]
with right side in \(L^2\). Thus it belongs to the transformed class
and is unique by (22). At every reached state the hypotheses remain
valid. Local uniqueness and concatenation prove autonomous restart
without resetting any field, readout, or operator. For antiparallel
abstract fields, their raw first derivatives sum to zero, so initial
opposition is preserved as well.

**2.4. Euler and raw GD.** Denote the transformed state by \(Y\) and
its physical field by \(\mathcal G\), only in this paragraph. On a
fixed horizon (20)--(25) give a bounded drift and a Lipschitz constant
\(C_T\). Therefore
\[
 \|Y(t+h)-Y(t)-h\mathcal G(Y(t))\|\le C_T h^2.               \tag{28}
\]
For a mesh with largest step \(h\), subtraction of updates and iteration
of \(e_{k+1}\le(1+C_T h_k)e_k+C_T h_k^2+\|d_k\|\) yields
\[
 \max_{t_k\le T+h}e_k\le e^{C_T(T+1)}
                          \left(C_T(T+1)h+\sum_k\|d_k\|\right).
 \tag{29}
\]
These estimates hold for untruncated iterates by the following
first-exit argument. Stop at the first residual norm exceeding
\(R_0+1\). Up to its candidate update, the discrete action is at
most \(2\sqrt2(R_0+1)(T+1)\). The explicit readout and rank updates
give (23) with discrete action: the half coefficient follows from
\(\sum_k\alpha_k\sum_{j<k}\alpha_j
=( (\sum\alpha_k)^2-\sum\alpha_k^2)/2\).
Hence (20) gives fixed constants through that candidate node. When
the right side of (29) is sufficiently small, (20) makes its residual
within \(1/2\) of the exact residual; it cannot exit. This proves
width-independent \(O_T(h)\) transformed Euler convergence, including
transformed velocities, for all sufficiently small \(h\).

At a raw node an independent first coordinate has increment
\(v=\eta c\phi'(z)q\), with \(c=-2r_a\) or \(-4r_1\).
The exact polynomial identity is
\[
 F(z+v)-F(z)=\eta cq+
       \eta^2c^2z\phi'(z)^2q^2+\tfrac13\eta^3c^3\phi'(z)^3q^3.
 \tag{30}
\]
There is no defect in the other two coordinates. On fixed residual,
operator, and readout bounds, \(\frac{\|q\|_{\ell^2}}{\sqrt n}\le C_T\) and
\(\|q\|_\infty\le\sqrt n C_T\). Since
\(|z|\phi'(z)^2\le1\), the defect norm is at most
\(C_T(\eta^2\sqrt n+\eta^3n)\). Its accumulated norm for
\(\eta=n^{-2}\) is \(O_T(n^{-3/2})\). The same first-exit
argument closes these bounds and, by (29), compares raw GD to the
finite flow with exactly the same initialization by
\[
 \sup_{t\le T}\left(\sum_a\frac{\|u^{\rm GD}_{n,a}-u^{\rm GF}_{n,a}\|_{\ell^2}}{\sqrt n}
   +\|W^{(2),\rm GD}_n-W^{(2),\rm GF}_n\|_F
   +\frac{\|W^{(3),\rm GD}_n-W^{(3),\rm GF}_n\|_{\ell^2}}{\sqrt n}\right)
                          =O_T(n^{-3/2}).                    \tag{31}
\]
For the raw interpolation the cubic coordinate differs from the
linear interpolation of its endpoints by
\((\theta^2-\theta)zv^2+(\theta^3-\theta)v^3/3\).
The same bound controls this term. Its derivative error is bounded
by \(C_T(\eta\sqrt n+\eta^2n)\), so transformed velocities in
(31) also converge at that rate.

Original first velocities use a product for which the finite estimate
\[
 \frac{\|\phi'(z)q-\phi'(\widetilde z)\widetilde q\|_{\ell^2}}{\sqrt n}
 \le\frac{\|q-\widetilde q\|_{\ell^2}}{\sqrt n}+
                      \|\widetilde q\|_\infty\frac{\|z-\widetilde z\|_{\ell^2}}{\sqrt n}
 \tag{32}
\]
is sufficient. It gives \(O_T(n^{-1})\), using (31). Apply the same
estimate to \(\dot h^{(1)}=\phi'(z^{(1)})\dot z^{(1)}\), then use
\[
 \dot z^{(2)}=\dot W^{(2)}h^{(1)}+W^{(2)}\dot h^{(1)},\qquad
 \dot h^{(2)}=\phi'(z^{(2)})\dot z^{(2)}.                    \tag{33}
\]
All original hidden-velocity errors are \(O_T(n^{-1})\); rank and
readout velocity errors are \(O_T(n^{-3/2})\). Their norms are uniformly
bounded. The inequality
\(|\|v\|^2-\|w\|^2|\le(\|v\|+\|w\|)\|v-w\|\) transfers these
bounds to energies. Kernels compare at \(O_T(n^{-1})\) for block 1
and \(O_T(n^{-3/2})\) for blocks 2 and 3. The exact energy identity
(24) is a flow identity; no exact loss identity for discrete GD is used.

These comparisons hold with probability tending to one under (2).
Indeed a \(1/4\)-net of the Euclidean unit sphere has at most \(9^n\)
points: disjoint balls of radius \(1/8\) around a maximal separated
set fit in the ball of radius \(9/8\). Approximating both arguments
of a bilinear form gives the norm bound twice its maximum on the net.
Each fixed bilinear form of \(W^{(2)}_n(0)\) has variance \(1/n\).
The Gaussian exponential moment and Markov's inequality give
\(\mathbb P(|N(0,1)|>u)\le2e^{-u^2/2}\). Hence
\[
 \mathbb P(\|W^{(2)}_n(0)\|_{\mathrm{op}}>t)
       \le2\exp(2n\log9-nt^2/8),                            \tag{34}
\]
and
\[
 \mathbb P(\|W^{(3)}_n(0)\|_\infty>1)\le2ne^{-n^2/2},\quad
 \mathbb P(\|W^{(3)}_n(0)\|_\infty>\sqrt{6\log n}/n)
                                                   \le2n^{-2}\ (n\ge2).
 \tag{35}
\]
In particular the events with initial bounds 8 and 1 have probability
tending to one, uniformly supplying all constants in (31).

## 3. Canonical Gaussian construction and global response bounds

**3.1. Fixed meshes and the scalar law to be proved.** Initially use
zero finite readout as an auxiliary comparison, leaving both Gaussian
matrices and the first-row roots unchanged. Fix a finite deterministic
mesh \(0=t_0<\cdots<t_N\), with steps \(h_k=t_{k+1}-t_k\).
At each node compute (10), using finite normalized operations when
appropriate, put \(\gamma_{ka}=-2h_k(f_{ka}-y_a)\), and update
\[
 \begin{aligned}
 U_{k+1,a}&=U_{ka}+\sum_b C_{ab}\gamma_{kb}Q^{(1)}_{kb},\\
 W^{(2)}_{k+1}&=W^{(2)}_k+
                 \sum_b\gamma_{kb}\delta^{(2)}_{kb}\otimes H^{(1)}_{kb},\\
 W^{(3)}_{k+1}&=W^{(3)}_k+\sum_b\gamma_{kb}H^{(2)}_{kb},
 \quad U_{0a}=F(G_a),\quad W^{(3)}_0=0.
 \end{aligned}                                                   \tag{36}
\]
At \(C=I\) this is transformed Euler. At \(\rho=-1\) its unforced
state satisfies (17) by induction, so it is transformed Euler for the
reduced physical system. Away from that invariant state (36) will only
be an auxiliary finite program, with no claim to be the raw flow.

The following recursion specifies the limiting joint law of every
fixed such program. On population 1 take the full Gaussian first row
and a centered jointly Gaussian source family \((\zeta_{ka})\)
independent of that row. On population 2 take a centered jointly
Gaussian source family \((\xi_{ka})\). The source groups are independent;
within a group all sample and time covariances must be retained.
The scalar expressions are
\[
 \begin{aligned}
 U_{ka}&=F(G_a)+\sum_{r<k,b}C_{ab}\gamma_{rb}Q^{(1)}_{rb},
 &H^{(1)}_{ka}&=\phi(F^{-1}(U_{ka})),\\
 Z^{(2)}_{ka}&=\xi_{ka}+
                    \sum_{r<k,b}a_{ka,rb}\delta^{(2)}_{rb},
 &H^{(2)}_{ka}&=\phi(Z^{(2)}_{ka}),\\
 W^{(3)}_k&=\sum_{r<k,b}\gamma_{rb}H^{(2)}_{rb},
 &\delta^{(2)}_{ka}&=W^{(3)}_k\phi'(Z^{(2)}_{ka}),\\
 Q^{(1)}_{ka}&=\zeta_{ka}+\sum_{r\le k,b}b_{ka,rb}H^{(1)}_{rb},
 &f_{ka}&=\mathbb E_2[W^{(3)}_kH^{(2)}_{ka}].
 \end{aligned}                                                   \tag{37}
\]
Here the deterministic coefficients, including learned ranks, are
\[
 \begin{aligned}
 a_{ka,rb}&=\alpha_{ka,rb}+
                  \gamma_{rb}\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{rb}],
 &\alpha_{ka,rb}&=\mathbb E_1[\partial_{\zeta_{rb}}H^{(1)}_{ka}],
 &&r<k,\\
 b_{ka,rb}&=\beta_{ka,rb}+\mathbf1_{r<k}\gamma_{rb}
                         \mathbb E_2[\delta^{(2)}_{ka}\delta^{(2)}_{rb}],
 &\beta_{ka,rb}&=\mathbb E_2[\partial_{\xi_{rb}}\delta^{(2)}_{ka}],
 &&r\le k.
 \end{aligned}                                                   \tag{38}
\]
Their source covariances are the uncentered input second moments
\[
 \mathbb E_2[\xi_{ka}\xi_{vb}]
       =\mathbb E_1[H^{(1)}_{ka}H^{(1)}_{vb}],\qquad
 \mathbb E_1[\zeta_{ka}\zeta_{vb}]
       =\mathbb E_2[\delta^{(2)}_{ka}\delta^{(2)}_{vb}].        \tag{39}
\]
The same rule gives cross-run covariances when different fixed meshes
or probes use the same initial matrix. Both forward answers precede
both reverse answers at a node; all updates follow them. This order
makes the recursion causal, not an implicit fixed-point prescription.

Each formal derivative differentiates the complete earlier coordinate
expression, holding all selected expectations, scalar feedback values,
response coefficients, and covariance parameters fixed. It does not
differentiate their selection. In particular
\[
 \begin{aligned}
 \partial U_{ka}&=\sum_{r<k,b}C_{ab}\gamma_{rb}\partial Q^{(1)}_{rb},\\
 \partial H^{(1)}_{ka}&=\phi'(F^{-1}(U_{ka}))^2\partial U_{ka},\\
 \partial W^{(3)}_k&=\sum_{r<k,b}\gamma_{rb}
                                \phi'(Z^{(2)}_{rb})\partial Z^{(2)}_{rb},\\
 \partial\delta^{(2)}_{ka}&=\phi'(Z^{(2)}_{ka})\partial W^{(3)}_k
                    +W^{(3)}_k\phi''(Z^{(2)}_{ka})\partial Z^{(2)}_{ka},\\
 \beta_{ka,kb}&=\mathbf1_{a=b}
                        \mathbb E_2[W^{(3)}_k\phi''(Z^{(2)}_{ka})].
 \end{aligned}                                                   \tag{40}
\]
The current reverse term and the past readout derivative are both
present. Formally distinct sample slots remain distinct even at
singular covariance. At zero the reverse sources have variance zero,
but their formal slots are retained.

We next prove that (37)--(39) is the full-sequence empirical law of
the finite program against every continuous polynomial-growth test,
and in every finite Wasserstein order. This proof is specialized to
the present one-matrix, arctangent model.

**3.2. Elementary all-order moments for a fixed program.** All constants
in this paragraph may depend on the finite number of instructions.
The readout has a deterministic coordinate bound, independent of the
root values and width, because
\[
 \|W^{(3)}_{k+1}\|_\infty
       \le(1+4B^2h_k)\|W^{(3)}_k\|_\infty+4Bh_k.             \tag{41}
\]
Indeed \(|f_{ka}|\le B\|W^{(3)}_k\|_\infty\), and each summand
in its update is bounded by \(2h_k B(B\|W^{(3)}_k\|_\infty+1)\).
The same bound holds after independent Gaussian query perturbations,
since \(\phi\) stays bounded. Thus the map
\(w\phi'(z)\) can, for graph estimates, be replaced by
\(\tau(w)\phi'(z)\), where a smooth bounded \(\tau\) agrees with
the identity on an interval strictly larger than this deterministic
range. This changes no program value and makes that coordinate map
globally Lipschitz. Store \((W^{(1)}(0),F(G_1),F(G_2))\) as one
iid root tuple. It has every finite moment; no derivative of the cubic
root map with respect to its underlying Gaussian is needed.

Unroll every learned operator into its initial matrix plus finitely
many ranks. The graph now uses globally Lipschitz coordinate maps,
initial matrix actions in either direction, normalized contractions,
and polynomial scalar arithmetic and scalar-times-vector operations.
Adjoin finitely many independent Gaussian roots for the regularizations
below. Conditional on all root arrays \(R\), let
\(K_R=1+\sum_j\frac{\|R_j\|_{\ell^2}}{\sqrt n}\), and write the initial matrix as
\(E/\sqrt n\), with unscaled standard Gaussian entries in \(E\).
For each vector node \(x\) and scalar node \(c\), finite induction
gives a polynomial \(P\), independent of width, such that
\[
 \begin{aligned}
 \frac{\|x\|_{\ell^2}}{\sqrt n}+|c|&\le P(K_R+\|W^{(2)}_n(0)\|_{\mathrm{op}}),\\
 \|\partial_E x[v]\|_{\ell^2}&\le
           P(K_R+\|W^{(2)}_n(0)\|_{\mathrm{op}})\|v\|_{\ell^2},\\
 |\partial_E c[v]|&\le n^{-1/2}
           P(K_R+\|W^{(2)}_n(0)\|_{\mathrm{op}})\|v\|_{\ell^2}.
 \end{aligned}                                                   \tag{42}
\]
Here a matrix direction is vectorized. The induction uses these exact
estimates: an initial action has differential
\(W^{(2)}_n(0)\partial x[v]+n^{-1/2}v x\), whose second term has
Euclidean norm at most \(\|v\|_F\frac{\|x\|_{\ell^2}}{\sqrt n}\). For a contraction,
\[
 |\partial[(1/n)x^Ty][v]|
 \le n^{-1/2}(\frac{\|y\|_{\ell^2}}{\sqrt n}\|\partial x[v]\|_{\ell^2}
                     +\frac{\|x\|_{\ell^2}}{\sqrt n}\|\partial y[v]\|_{\ell^2}).
\]
For a scalar-times-vector node the \(n^{-1/2}\) scalar derivative
cancels the \(\sqrt n\) in the vector norm. Lipschitz coordinate
maps and polynomial scalar operations preserve the estimates. The same
induction gives Euclidean Lipschitz dependence on stored root arrays,
with polynomial constant in their normalized norms and the matrix norm.

We use the following dimension-independent Gaussian inequality, and
include its proof. For a smooth scalar function \(X(E)\), for
\(p\ge1\) and finite right-hand side,
\[
 \mathbb E|X(E)-\mathbb E X(E)|^p
 \le(\pi/2)^p\mathbb E|N(0,1)|^p\,
                                 \mathbb E\|\nabla X(E)\|_{\ell^2}^p.
 \tag{43}
\]
Take an independent copy \(E'\), rotate
\(E_\theta=E\cos\theta+E'\sin\theta\), and integrate the derivative
of \(X(E_\theta)\) from 0 to \(\pi/2\). Its orthogonal velocity
\(-E\sin\theta+E'\cos\theta\) is an independent standard Gaussian.
Integral Hölder, then conditional Gaussian integration of that velocity,
bounds \(\mathbb E|X(E')-X(E)|^p\) by the right side of (43).
Conditional Jensen gives (43). Smooth approximation gives the same
bound for Lipschitz functions. Polynomial domination in the present
finite graphs justifies all integrals. Equation (34), integrated over
its tail, gives uniform moments of every order for the matrix norm.

To control conditional means with the non-Gaussian stored root, put
\(m_i(R)=\mathbb E_E x_i(R,E)\). Transposing two neurons \(i,j\)
of the output population and the corresponding matrix indices gives
\(m_i(R^{ij})=m_j(R)\). The root Lipschitz bound therefore gives
\[
 |m_i(R)-m_j(R)|\le P(K_R)
                  \sum_{l\text{ in this population}}|R_{li}-R_{lj}|.
\]
Also \(\frac{\|m(R)\|_{\ell^2}}{\sqrt n}\le P(K_R)\). Average over \(j\) and use
Cauchy--Schwarz to get
\[
 |m_i(R)|\le P(K_R)\left(1+\sum_l|R_{li}|\right).             \tag{44}
\]
If that population has no roots its conditional means are simply equal.
Apply (43) conditionally on \(R\), use (42) and (44), and integrate
over the roots. Jensen bounds every moment of their normalized norms
by a higher coordinate moment; Hölder handles products. Thus, for each
fixed graph and every finite \(p\),
\[
 \sup_n\mathbb E|x_i|^p<\infty,
 \qquad \sup_n\mathbb E\frac1n\sum_i|x_i|^p<\infty.          \tag{45}
\]
This holds for empirical-feedback graphs, their deterministic-coefficient
versions, and the auxiliary graphs with query-noise coefficient in
\([0,1]\). It concerns random program nodes, not an \(L^p\) norm of
the matrix acting on arbitrary inputs.

**3.3. Gaussian conditioning, projections, and source responses.** For
this paragraph only, write the initial matrix as \(W\), and collect
old forward inputs in a matrix \(V\), old reverse inputs in a matrix
\(J\), with observed answers \(WV=Y\), \(W^TJ=P\). When their
Grams are invertible, conditional on the transcript,
\[
 W\ \overset d=\ Y(V^TV)^{-1}V^T
   +J(J^TJ)^{-1}P^TP_{V^\perp}
   +P_{J^\perp}\widetilde W P_{V^\perp},                    \tag{46}
\]
where \(\widetilde W\) is an independent matrix with the same Gaussian
entry law. To verify this, vectorize the matrix. Orthogonal Gaussian
projection onto the linear constraint space gives its conditional mean;
the orthogonal residual is independent. The displayed mean satisfies
both constraints because \(J^TY=P^TV\), and the residual is exactly
their common null component. Adaptivity adds no further condition:
given earlier answers, a new query is already measurable, so observing
its answer adds just its linear constraint. This proves (46) inductively.

For a new forward input \(h\), put
\[
 \lambda_n=(V^TV)^{-1}V^Th,\quad h_\perp=h-V\lambda_n,
 \quad \nu_n=(J^TJ/n)^{-1}(P^Th_\perp/n),\quad
 \sigma_n=\frac{\|h_\perp\|_{\ell^2}}{\sqrt n}.
\]
Then its answer is conditionally
\(Y\lambda_n+J\nu_n+\sigma_nP_{J^\perp}e\), for a fresh iid
standard Gaussian \(e\). Interchanging the two populations gives the
reverse rule, with the same original matrix. If a projection \(P_0\)
has rank at most the fixed number \(j\) of previous queries, then for
\(p\ge2\)
\[
 \mathbb E[\frac1n\|\sigma_nP_0e\|_{\ell^p}^p\mid\text{transcript}]
  =\frac{\mathbb E|N|^p\sigma_n^p}{n}\sum_i(P_0)_{ii}^{p/2}
  \le\frac{j\mathbb E|N|^p\sigma_n^p}{n},
 \quad \|v\|_{\ell^p}^p=\sum_i|v_i|^p.                 \tag{47}
\]
This follows from \(0\le(P_0)_{ii}\le1\) and
\(\sum_i(P_0)_{ii}\le j\). Equation (45) and
\(\sigma_n\le\frac{\|h\|_{\ell^2}}{\sqrt n}\) make it tend to zero. For \(p<2\) use
the \(p=2\) bound and the probability-space norm inequality.

After this negligible projection is removed, the added coordinates
are independent Gaussians conditional on the transcript. If a test
has growth \(C(1+|x|^d)\), its empirical conditional variance, on an
event bounding both the regression coefficients and the innovation
standard deviation, is at most
\[
 \frac Cn\left(1+\frac1n\sum_i|\text{old tuple}_i|^{2d}\right).
 \tag{48}
\]
For general unbounded probe inputs the latter event can be imposed
first and then removed: \(\sigma_n\le\|h\|_{\ell^2}/\sqrt n\)
and (45) give tightness. Conditional Chebyshev proves concentration.
Its conditional expectation
is the old empirical average of the Gaussian-integrated test. This is
continuous in the old coordinates and coefficients and has uniform
polynomial growth on compact coefficient sets. Uniform continuity on
a ball and the estimate
\[
 \frac1n\sum_i|x_i|^d\mathbf1_{|x_i|>R}
       \le R^{d-q}\frac1n\sum_i|x_i|^q\qquad(q>d)             \tag{49}
\]
justify convergence of those expectations and restoration of the
projection. The root step is Chebyshev's inequality for iid tuples.
Coordinate maps preserve polynomial-growth tests. This proves empirical
induction for nonsingular limiting query Grams.

To identify the source form of this induction, let old forward inputs
be \(h_r\), reverse inputs \(v_s\), with respective Gaussian sources
\(\xi_r,\zeta_s\). The rule is
\[
 Wh=\xi_h+\sum_s v_s\mathbb E[\partial_{\zeta_s}h],\qquad
 W^Tv=\zeta_v+\sum_r h_r\mathbb E[\partial_{\xi_r}v].        \tag{50}
\]
The covariance of any two forward sources is the inner product of
their inputs, and the analogous statement holds for reverse sources.
Here is the calculation. Subtract the least-squares old-forward-input
projection from \(h\), obtaining \(h_\perp\). Every old reverse
answer is \(\zeta_s\) plus a linear combination of old forward inputs.
Thus its inner product with \(h_\perp\) is
\(\mathbb E[\zeta_s h_\perp]\). For a Gaussian vector of covariance
\(\Gamma\),
\[
 \mathbb E[\zeta F_0(\zeta)]=\Gamma\mathbb E[\nabla F_0(\zeta)].
 \tag{51}
\]
Write \(\zeta=Le\) and integrate each independent scalar Gaussian
coordinate by parts to prove (51); polynomial growth and bounded
derivatives make boundary terms vanish. Conditioning on independent
roots is legitimate. More explicitly, let \(\lambda_r\) be the
limiting least-squares coefficients and let
\(\Gamma_v=(\mathbb E[v_sv_{s'}])_{s,s'}\). The limiting coefficient
of the reverse-input columns in (46) is
\[
 \nu=\Gamma_v^{-1}\mathbb E[\zeta h_\perp]
       =\mathbb E[\nabla_\zeta h]
                   -\sum_r\lambda_r\mathbb E[\nabla_\zeta h_r].
\]
The old forward answers have decompositions
\(Wh_r=\xi_r+\sum_s v_s\mathbb E[\partial_{\zeta_s}h_r]\),
with unavailable derivatives zero. Substituting them into
\(\sum_r\lambda_rWh_r+\sum_s\nu_sv_s\) cancels the last sum
in the displayed expression for \(\nu\), giving (50).
The new full source is the old source
projection plus a fresh Gaussian with variance \(\mathbb E h_\perp^2\).
Consequently its full variance is \(\mathbb E h^2\), not that variance
minus a response term. The reverse proof interchanges the populations.
Every source is a deterministic linear combination of older sources
of its own group and a fresh independent Gaussian; the two source
groups remain independent of one another and of all local roots.

**3.4. Singular query Grams and empirical feedback.** Add \(\epsilon\)
times a fresh independent Gaussian root to the input of each initial
matrix query, revealing that root immediately before the query. Keep
the same initial matrix and leave the explicit learned rank factors
unperturbed. At fixed \(\epsilon>0\) every new limiting Gram Schur
complement is at least \(\epsilon^2\), because the fresh root is
independent of the previous same-direction input span and of the
unperturbed new input. At width larger than the number of old queries
the finite Grams are nonsingular almost surely. Thus (46)--(50) apply.

Couple the two actual finite graphs with the same matrix and roots.
Finite graph subtraction, using (42) and the contraction inequality
\[
 |\frac1n x^Ty-\frac1n(x')^Ty'|
 \le\frac{\|x-x'\|_{\ell^2}}{\sqrt n}\frac{\|y\|_{\ell^2}}{\sqrt n}+\frac{\|x'\|_{\ell^2}}{\sqrt n}\frac{\|y-y'\|_{\ell^2}}{\sqrt n},
 \tag{52}
\]
gives \(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^2}}{\sqrt n}\le\epsilon P(K_n)\), where
\(K_n\) includes normalized root norms and the matrix norm and has
all finite moments. For \(p>2\), choose \(q>p\) and
\(1/p=\theta/2+(1-\theta)/q\). Hölder gives
\[
 \left(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^p}}{n^{1/p}}\right)
 \le\left(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^2}}{\sqrt n}\right)^\theta
                    \left(\frac{\|x_n^\epsilon-x_n^0\|_{\ell^q}}{n^{1/q}}\right)^{1-\theta}.
 \tag{53}
\]
Equation (45) bounds the second factor in probability uniformly in
width and \(\epsilon\in[0,1]\). Thus all these empirical errors tend
to zero uniformly in probability as \(\epsilon\downarrow0\). Truncation
by (49) transfers every continuous polynomial-growth test.

On the scalar side use (50), which contains no inverse covariance.
At each causal step, previously selected coefficients converge and
are bounded. Expressions have polynomial growth in the root/source
tuple, continuous dependence on coefficients, and bounded continuous
formal source derivatives on each compact coefficient set. This
follows by the chain rules (40): the cubic root is a stored root,
the other maps are Lipschitz with bounded derivatives, and the readout
factor has the deterministic bound (41). The same statements hold
for the finitely many extra Lipschitz probe instructions.

Positive semidefinite covariance square roots are continuous in fixed
dimension, including at singularity. Indeed their norms are bounded
for a convergent covariance sequence. Each subsequential limit squares
to the limiting covariance and is positive semidefinite; diagonalizing
that covariance shows its nonnegative square root is unique. Therefore
the whole sequence of square roots converges. Couple sources by those
square roots applied to a fixed standard Gaussian vector, independently
of the roots. Dominated convergence proves convergence of coordinate
moments and of the expected formal derivatives. Each next covariance
is an input Gram and remains positive semidefinite. This inductively
proves continuity of the entire finite scalar law as \(\epsilon\to0\).
The positive-noise theorem and (53) then prove the zero-noise theorem
by a triangle inequality, first taking width to infinity, then noise
to zero. This includes exactly zero and redundant queries.

Formal slots must not be deleted at a rank drop. If
\(\Gamma=\mathbb E[vv^T]\) and \(\lambda\in\ker\Gamma\), then
\(\sum_s\lambda_sv_s=0\) almost surely. An ambiguity in a derivative
vector in that null direction changes no contracted response in (50).
The explicit-expression convention fixes individual coefficients; their
use at zero covariance has just been justified by actual perturbed
finite programs, rather than an inverse-Gram assumption.

Finally, learned ranks satisfy the exact identities
\[
 \begin{aligned}
 W^{(2)}_kh&=W^{(2)}_0h+
            \sum_{r<k,b}\gamma_{rb}\delta^{(2)}_{rb}
                                          \mathbb E_1[H^{(1)}_{rb}h],\\
 W^{(2)*}_kv&=W^{(2)*}_0v+
            \sum_{r<k,b}\gamma_{rb}H^{(1)}_{rb}
                                          \mathbb E_2[\delta^{(2)}_{rb}v].
 \end{aligned}                                                   \tag{54}
\]
Select every scalar contraction in causal order by its expectation
under the already constructed scalar law. This defines a deterministic
coefficient program. Its empirical contractions converge by the preceding
proof. Couple it with the actual feedback program. On bounded \(K_n\),
(52), the Lipschitz coordinate inequalities and the matrix norm bound
show by finite induction that every RMS discrepancy is bounded by a
constant times the sum of the finitely many contraction errors. These
vanish in probability. Increase the bound on \(K_n\); its complement
has arbitrarily small probability by the moment bounds. Apply (45),
(49), and (53) to upgrade from RMS to all polynomial-growth tests.
Substituting (50) into (54) gives precisely (37)--(39), with all learned
terms in (38). This proves actual-feedback identification.

For completeness it also proves Wasserstein convergence. Truncate
to a large ball, partition that ball into finitely many cells of small
diameter and zero limiting boundary mass, and approximate cell
indicators by continuous functions. Their empirical masses converge.
Match common mass inside each cell and couple the unmatched bounded
mass arbitrarily. Coupling tail mass through the origin bounds the
remaining cost by a constant times the two \(p\)-tails, which vanish
by (49) with \(q>p\). Sending width, cell diameter, and tail cutoff
to their respective limits proves the stated convergence in probability.

**3.5. One common space and an actual bounded adjoint.** Enumerate a
countable family of finite programs, all using the same initial matrix
and roots. Include dyadic meshes on all integer horizons, intermediate
fields, both initial-matrix orientations applied to every generated
node, rational linear combinations, constants, and a countable dense
family of bounded smooth cylinder functions. Include any fixed countable
collection of requested independent probe roots. Close this list in
stages; every instruction has finitely many parents, and every finite
initial sublist is covered by the finite-program proof. A Gaussian source
itself can be included by subtracting its selected response from its
matrix answer.

Construct sources in this order. Their covariances with earlier sources
are input Grams. Subtract the projection onto the earlier Gaussian span
and use a fresh independent standard Gaussian for the nonnegative
residual variance. At zero variance retain the formal slot without a
new random draw. Countably many independent Gaussian variables and
roots can be realized on a probability space explicitly: split the
independent binary digits of a uniform point of \((0,1)\) into countably
many infinite subsequences to obtain independent uniforms, then use
their quantile maps. Finite binary cylinder probabilities verify this
construction; binary ambiguities form a null set. Use separate spaces
for the first roots/reverse sources and the second roots/forward sources.

For a queried input \(h\), let its limiting initial forward answer be
\(a(h)\); for a reverse input \(v\), let its initial reverse answer be
\(b(v)\), only in this construction. Every finite rational combination
satisfies
\[
 \left\|\sum_i t_i a(h_i)\right\|_2
       \le8\left\|\sum_i t_i h_i\right\|_2,
 \quad
 \left\|\sum_j s_j b(v_j)\right\|_2
       \le8\left\|\sum_j s_j v_j\right\|_2,
 \quad
 \mathbb E_2[a(h)v]=\mathbb E_1[hb(v)].            \tag{55}
\]
The finite identities hold exactly and the inequalities hold on the
event \(\|W^{(2)}_n(0)\|\le8\), whose probability tends to one by
(34). All involved Gram entries converge to deterministic quantities.
A strict violation of (55) would contradict these two facts. Approximate
real coefficients by rationals. In particular a zero-norm relation
among inputs gives a zero-norm relation among answers, so the proposed
linear actions are well defined.

The queried-input spans are dense in the two generated \(L^2\) spaces.
To check this without an implicit density assumption, events approximable
in measure by finite-cylinder events form a class closed under complements
and countable unions: first approximate a finite union, then use
continuity of probability for its increasing limit. They therefore
include the sigma field generated by the countable tuple. Rational
threshold rectangles generate the finite-dimensional Borel sets.
One-sided smooth threshold approximations converge to their indicators,
even when a coordinate has an atom. Products of these approximations
are bounded smooth cylinder functions in the closure of the chosen
countable family. Truncating and approximating simple functions proves
density in \(L^2\).

Extend both linear maps by (55) to their completions. The last identity
in (55), passed to the completions, says that the reverse extension is
exactly the adjoint of the forward extension. Call the forward operator
\(W^{(2)}(0)\). It is bounded by 8 and uniquely specified on these
generated spaces. Adding an unused query changes no earlier marginal:
both constructions give the full-sequence empirical limit of that
same finite marginal. Therefore different enumerations give the same
joint laws, with measure-preserving identifications on the generated
function spaces and the corresponding isometries of \(L^2\).
This is the required canonicity. It does not identify a Gaussian matrix
with an iid continuum kernel or with an operator bounded on every
\(L^p\).

Apply Section 2 on these spaces with \(U_{0a}=F(G_a)\) and zero
readout. This gives a single global autonomous flow. Each of the
constructed finite-mesh scalar programs satisfies its Euler equations
on these same spaces, with this same operator and adjoint, by (54)--(55).
Consequently, for largest mesh step \(h\),
\[
 \sup_{t\le T}\left(\sum_a\|U_a^h(t)-U_a(t)\|_2
       +\|W^{(2),h}(t)-W^{(2)}(t)\|_{\mathrm{HS}}
       +\|W^{(3),h}(t)-W^{(3)}(t)\|_2\right)\le C_T h.
 \tag{56}
\]
Any further fixed mesh can be adjoined to the countable family and
obeys the same bound. The flow is not defined by selecting a width
subsequence, nor by restarting a fresh operator at each mesh.

**3.6. Global expected-response bounds by actual fresh-root forcing.**
This step is needed for the all-time nontriviality assertions; primal
\(L^2\) bounds alone do not imply it. Fix \(T\), and consider every
finite partition through \(T\) with largest step at most 1. Equation
(41) gives the deterministic bound
\[
 \|W^{(3)}_k\|_\infty\le M_T
       :=B^{-1}(e^{4B^2(T+1)}-1).
 \tag{57}
\]
Thus \(|\gamma_{ka}|\le2h_k(BM_T+1)\) and the total absolute
sum of the \(\gamma\)'s is at most
\(4(T+1)(BM_T+1)\). On the event \(\|W^{(2)}_n(0)\|\le8\),
the rank updates bound all operator norms by a deterministic constant
depending only on \(T\). These bounds also hold for the forced programs
below. Subtraction of one step of (36), using (20) and (52), gives a
state Lipschitz factor \(1+C_T h_k\) in (19). For this auxiliary
comparison use the sum over both first-sample coordinates in that norm.
It includes the changes
in residuals and in every rank update. With both sample coordinates
retained it also holds off the antiparallel invariant state, because
\(\|C\|\le2\) and the transformed update is linear in the backward
answers. This auxiliary off-invariant program need not be raw GF.

First add \(\epsilon e\), with a fresh iid \(N(0,1)\) root array
on population 1, to the complete reverse answer \(q^{(1)}_{n,sb}\)
at one node, before its descendants are computed. Keep every matrix
entry and all earlier answers fixed. Only the first state update changes
immediately, by RMS at most \(C_T h_s|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\).
Multiplying the later factors \(1+C_T h_k\) gives, for \(k>s\),
\[
 \frac{\|h^{(1),\epsilon}_{n,ka}-h^{(1),0}_{n,ka}\|_{\ell^2}}{\sqrt n}
                 \le C_T h_s|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}.              \tag{58}
\]
Next perform instead the analogous insertion into the complete forward
answer \(z^{(2)}_{n,sb}\), using a fresh population-2 root. Its
immediate changes in activations, deltas, predictions, and residuals
are at most \(C_T|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\). The actual transpose bounds
the immediate reverse-answer changes by the same quantity. Every
state update has its factor \(h_s\), so at later nodes
\[
 \frac{\|\delta^{(2),\epsilon}_{n,ka}-\delta^{(2),0}_{n,ka}\|_{\ell^2}}{\sqrt n}
                 \le C_T h_s|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\qquad(k>s).
 \tag{59}
\]
At the current node the delta change is at most
\(M_T|\epsilon|\frac{\|e\|_{\ell^2}}{\sqrt n}\), and other current sample deltas have
no direct change. These are finite-width estimates for the actual
empirical-feedback programs, not estimates for arbitrarily extended
functions off a Gaussian support.

We now extract the coefficient with the order of limits specified
explicitly. Fix the mesh and a nonzero \(\epsilon\). Apply the proved
finite-program theorem jointly to the forced and unforced runs and
the new root \(e\), taking \(n\to\infty\) first. In its own population
the new root occurs in the scalar expression only through replacement
of the designated source slot by \(\zeta_{sb}+\epsilon e\), or
\(\xi_{sb}+\epsilon e\), respectively. The construction in (50)
makes all Gaussian source groups independent of the local root \(e\).
Their covariances and the selected response and feedback coefficients
may depend on \(\epsilon\), but are deterministic and constant as
functions of that local coordinate. Induction through the complete
coordinate expression therefore gives, with these selected quantities
held fixed,
\[
 \partial_e X^\epsilon
          =\epsilon\partial_{\mathrm{slot}}X^\epsilon,
 \qquad
 \mathbb E[eX^\epsilon]
          =\epsilon\mathbb E[\partial_{\mathrm{slot}}X^\epsilon].
 \tag{60}
\]
The second equality is one-dimensional Gaussian integration by parts
in the fresh root. It remains valid if the old source covariance is
singular. The unused root is independent of the unforced expression,
so \(\mathbb E[eX^0]=0\). Passing the finite Cauchy--Schwarz inequality
\(|\frac1n e^T(X_n^\epsilon-X_n^0)|
\le\frac{\|e\|_{\ell^2}}{\sqrt n}\frac{\|X_n^\epsilon-X_n^0\|_{\ell^2}}{\sqrt n}\) to the joint limit in
(58)--(59), and using \(\mathbb E e^2=1\), bounds (60) divided by
\(|\epsilon|\) by \(C_T h_s\). Only now let \(\epsilon\to0\).
The fixed-mesh coefficient and formal-derivative continuity proved in
3.4 identifies the limit with exactly (38), including initial slots
of variance zero. We have proved
\[
 |\alpha_{ka,sb}|\le C_T h_s\ (s<k),\qquad
 |\beta_{ka,sb}|\le C_T h_s\ (s<k),\qquad
 |\beta_{ka,kb}|\le M_T\mathbf1_{a=b}.                       \tag{61}
\]
In particular no derivative transverse to the support of an unforced
singular Gaussian law was inferred from that law. The order was fixed
mesh, nonzero forcing, width limit, integration by parts in the fresh
independent root, and finally forcing tending to zero. Feedback was
included in the finite estimates (58)--(59); selected scalar values
were correctly held fixed only in the local derivative (60).

Adding the learned terms in (38) now gives
\[
 |a_{ka,sb}|+|b_{ka,sb}|\le C_T h_s\ (s<k),\qquad
 |b_{ka,kb}|\le M_T\mathbf1_{a=b}.                           \tag{62}
\]
Thus the absolute sums of all complete past and current response rows
are bounded on every finite horizon, uniformly in the number of mesh
queries. No local-in-time response bootstrap is being extended without
an estimate.

**3.7. Bounded Gaussian remainders at every finite time.** From (37),
(39), (57), and (62), all mesh fields have decompositions
\[
 Z^{(2)}_{ka}=\xi_{ka}+S_{ka},\qquad
 Q^{(1)}_{ka}=\zeta_{ka}+R_{ka},\qquad
 |S_{ka}|+|R_{ka}|\le C_T.                                  \tag{63}
\]
Their Gaussian variances are exactly
\(\|H^{(1)}_{ka}\|_2^2\) and \(\|\delta^{(2)}_{ka}\|_2^2\).
Consequently
\[
 U_{ka}=F(G_a)+\sum_{r<k,b}C_{ab}\gamma_{rb}\zeta_{rb}
                                      +E_{ka},\qquad |E_{ka}|\le C_T.
 \tag{64}
\]
The Gaussian sum is independent of the first-row roots, with variance
at most \(C_T\); no independence from its bounded remainder is claimed.
The inverse Lipschitz bound gives
\(|F^{-1}(U_{ka})|\le|G_a|+|\sum C\gamma\zeta|+C_T\).
Thus the first and second preactivations and \(Q^{(1)}\) have uniform
Gaussian upper-tail bounds, and \(U\) has all moments with a
cubic-Gaussian bound.

These decompositions pass to the already constructed common-space
flow, not just to subsequential marginal laws. From the cross-program
version of (39), the source assignments are Gaussian isometries:
\[
 \|\xi_h-\xi_{h'}\|_2=\|h-h'\|_2,
 \qquad \|\zeta_v-\zeta_{v'}\|_2=\|v-v'\|_2.               \tag{65}
\]
They extend by completion on the closed input spans. Equation (56)
and (20) give uniform-in-time \(L^2\) convergence of their inputs,
so their sources converge too. Subtract from the convergent fields in
(63). An \(L^2\) limit of variables bounded by \(C_T\) is bounded
by \(C_T\): choose a subsequence with summable squared errors and
use Markov's inequality to obtain almost-everywhere convergence.
Riemann sums in (64) converge in \(L^2\). Limits of jointly Gaussian
linear combinations remain Gaussian because variances and characteristic
functions converge; independence from the root persists by factorization
of joint characteristic functions. We obtain, for every \(t\le T\),
\[
 \begin{aligned}
 Z^{(2)}_a(t)&=\xi_a(t)+S_a(t),& |S_a(t)|&\le C_T,\\
 Q^{(1)}_a(t)&=\zeta_a(t)+R_a(t),& |R_a(t)|&\le C_T,\\
 \mathbb E_2[\xi_a(t)\xi_b(v)]
       &=\mathbb E_1[H^{(1)}_a(t)H^{(1)}_b(v)],&&\\
 \mathbb E_1[\zeta_a(t)\zeta_b(v)]
       &=\mathbb E_2[\delta^{(2)}_a(t)\delta^{(2)}_b(v)],&&\\
 U_a(t)&=F(G_a)+\sum_b C_{ab}\int_0^t c_b(v)\zeta_b(v)\,dv+E_a(t),
 &|E_a(t)|&\le C_T,
 \quad c_b=-2r_b.
 \end{aligned}                                                   \tag{66}
\]
The representations hold almost surely at each deterministic finite
time. Jointly measurable versions give the product-almost-everywhere
identities used for time integration; no common exceptional-set claim
stronger than these laws and integral statements is needed here.
The sources are centered Gaussian processes with their full time and
sample covariances, and \(\zeta\) is independent of the whole first
row. Their \(L^2\) continuity makes the displayed Gaussian integrals
well defined. Essential remainder bounds are uniform in the horizon;
joint measurable representatives follow from \(L^2\)-continuous
approximations, and Fubini suffices for the time integrals. These are
the global representation properties used below, now proved rather
than imposed as hypotheses.

## 4. Full-sequence observable limits, paths, velocities, and energies

**4.1. Products and uniform integrability.** A bounded gate times an
\(L^2\) field is continuous along the paths here, but is not in general
Lipschitz in the pair of \(L^2\) inputs. The precise estimate used is
\[
 \|(a-a')b\|_2^2\le R^2\|a-a'\|_2^2
                  +4M^2\mathbb E[|b|^2\mathbf1_{|b|>R}],
 \qquad |a|,|a'|\le M.                                     \tag{67}
\]
It follows by splitting at \(|b|=R\), and holds identically for
normalized finite sums. For two products first split
\(ab-a'b'=a(b-b')+(a-a')b'\). Thus convergence follows when the
gates converge in \(L^2\), the fields converge in \(L^2\), and their
squares are uniformly integrable. Also bounded multipliers converging
in measure times a fixed \(L^2\) field converge in \(L^2\): truncate
the field, use bounded convergence in measure for its bounded part,
then bound the tail. This proves continuity of the original velocities
and kernels along the population flow.

We need uniform integrability in the finite-width/time passage as well.
For a moment estimate only, replace the initial matrix by
\[
 \overline W^{(2)}_n(0)=W^{(2)}_n(0)
                       \min(1,8/\|W^{(2)}_n(0)\|_{\mathrm{op}}).
 \tag{68}
\]
This equals the original with probability tending to one by (34).
The radial map is 2-Lipschitz in operator norm. For example, suppose
the first norm is larger, write the difference as the first scale
times the matrix difference plus the difference of scales times the
second matrix, and use the reverse triangle inequality for their norms.
In the case one norm is below 8 the same decomposition bounds the
second term by the excess of the larger norm over 8. Thus changing
the unscaled Gaussian matrix entries by \(E\) changes (68) by at
most \(2\|E\|_F/\sqrt n\) in operator norm.

Use (22), first for zero initial readout. For each of
\[
 U_a,\ Z^{(1)}_a,\ H^{(1)}_a,\ Z^{(2)}_a,\ H^{(2)}_a,
 \ W^{(3)},\ \delta^{(2)}_a,\ Q^{(1)}_a,                    \tag{69}
\]
the uniform-in-time normalized \(L^2\) change is at most a constant
\(C_T\) times the initial operator-norm and stored-root \(L^2\)
changes. Consequently each scalar function
\(\sup_{t\le T}|X_i(t)|\) is \(C_T\)-Lipschitz in the unscaled
Gaussian matrix parameters and in the ordinary Euclidean norm of the
stored root arrays: the factor \(\sqrt n\) to bound one coordinate
cancels the normalized-root or matrix-parameter factor.

Their normalized RMS suprema satisfy
\[
 \left\|\sup_{t\le T}|X(t)|\right\|_2
          \le\|X(0)\|_2+\int_0^T\|\dot X(t)\|_2\,dt
          \le C_T\left(1+\sum_j\|R_j\|_2\right).            \tag{70}
\]
The first inequality is the pointwise integral inequality followed by
the triangle inequality for integrals. All derivatives in the second
inequality have bounded \(L^2\) norms: use (16), (23), (33), and
\[
 \dot\delta^{(2)}_a=\dot W^{(3)}\phi'(Z^{(2)}_a)
              +W^{(3)}\phi''(Z^{(2)}_a)\dot Z^{(2)}_a,
 \qquad
 \dot Q^{(1)}_a=\dot W^{(2)*}\delta^{(2)}_a
                                      +W^{(2)*}\dot\delta^{(2)}_a.
 \tag{71}
\]
Every multiplier here is bounded and each operator acts only in \(L^2\).
The paths have pointwise absolutely continuous representatives by
Fubini, as in (27).

Apply (43) conditionally on the roots to the supremum functionals.
Their Lipschitz constants are uniform; smooth approximation covers
their possible nonsmoothness. The same permutation and conditional-mean
proof (44), now using (70), gives for every finite \(p\)
\[
 \sup_n\mathbb E\frac1n\sum_i\sup_{t\le T}|\overline X_{n,i}(t)|^p
                                                       <\infty.
 \tag{72}
\]
For transformed Euler this proof is uniform over sufficiently small
meshes: use the product of the factors \(1+C_T h_k\) and replace
the integral in (70) by the sum of successive \(L^2\) increments.
At first one can use (41) and the rank bound for any mesh of largest
step at most 1; the resulting constants depend only on \(T\).
To include the actual initial readout, clip its coordinates to
\([-1,1]\) for this moment estimate and treat them as additional
stored iid local roots. Their moments are uniformly bounded, and the
flow stability applies to every such initial readout. The same proof
gives (72); the clipping is absent with probability tending to one
by (35). Thus (72) gives uniform integrability in probability for
the original fields. Since \(|\delta^{(1)}_a|\le|Q^{(1)}_a|\),
it covers their supremum moments too. The first row follows from (18)
and its Gaussian initial root. No modification (68) or readout clipping
is part of the asserted model.

**4.2. Fixed-time probes and the width/time passage.** At a fixed mesh,
Section 3 identifies all the base fields and contractions. It also
identifies \(\delta^{(1)}=\phi'(Z^{(1)})Q^{(1)}\): this is a
continuous polynomial-growth observable of already identified nodes.
For its subsequent use as a query, first smoothly truncate \(Q^{(1)}\)
to \([-R,R]\). This makes
\(\phi'(Z^{(1)})^2 Q^{(1)}\), or the corresponding single-gate
expression, a globally Lipschitz cylinder instruction. The untruncated
input error tends to zero in \(L^2\) uniformly in probability by
(45), or by (72) for time-uniform statements. The operator bound
multiplies this error by at most a fixed constant; the same proof
applies in the reverse direction. This establishes the admissibility
and joint Wasserstein-2 convergence of the probes needed for
\[
 \begin{aligned}
 \dot Z^{(1)}_a&=\phi'(Z^{(1)}_a)\dot U_a,
 &\dot H^{(1)}_a&=\phi'(Z^{(1)}_a)^2\dot U_a,\\
 \dot Z^{(2)}_a&=\dot W^{(2)}H^{(1)}_a+W^{(2)}\dot H^{(1)}_a,
 &\dot H^{(2)}_a&=\phi'(Z^{(2)}_a)\dot Z^{(2)}_a.
 \end{aligned}                                                   \tag{73}
\]
The first line is valid for each independent first field; at
\(\rho=-1\) the other field is its exact negative.

Initially keep zero finite readout. On \(\|W^{(2)}_n(0)\|\le8\),
the deterministic Euler/flow bound (29) compares finite GF with any
fixed small mesh, uniformly in width. On the population space, (56)
gives the same comparison. For every fixed finite list of observation
times, (20) bounds the discrepancy of the base-field tuples by
\(C_T h\) in normalized \(L^2\). Coupling identical finite neuron
indices bounds the Wasserstein-2 error by that normalized discrepancy;
the population comparison uses the common-space coupling. The middle
fixed-mesh width limit holds by Section 3. Given an error tolerance,
choose a fixed mesh making both deterministic discrepancies small,
then choose width making its empirical error small in probability.
Equation (34) removes the exceptional operator event. This proves
full-sequence convergence of finite observations. There is no extraction
of a subsequence of widths. Equation (67) and (72) extend it to all
backward products, and higher moments transfer polynomial-growth tests.

Restore the actual finite initial readout by coupling finite flows from
\(W^{(3)}_n(0)\) and from zero, with exactly the same initial matrices
and first roots. Equations (22) and (35) give a uniform transformed
state discrepancy at most
\(C_T\frac{\|W^{(3)}_n(0)\|_{\ell^2}}{\sqrt n}\to0\) in probability. Product estimates
and (72) transfer every observable just described. This identifies the
zero population readout as a limit of the actual Gaussian readout,
and does not substitute zero for it in (6).

For general admissible probes, perform their finite program after a
fixed comparison mesh, including all requested directions in the same
finite graph. Apply the finite-program theorem jointly. For an \(L^2\)
limit of such probes use its stated approximation property and the
operator bound on both sides. Bounded smooth functions of continuous-time
fields are included by first comparing those fields to the mesh;
unbounded queries require their verified \(L^2\) truncation property.
This proves the probe scope of 1.3 in both matrix orientations.

**4.3. Path laws and scalar outputs.** For an absolutely continuous
scalar path and its polygonal interpolant on an observation grid of
maximum spacing \(\Delta\), Cauchy--Schwarz on each interval gives
\[
 \|X-\Pi_\Delta X\|_\infty^2
                  \le4\Delta\int_0^T|\dot X(t)|^2\,dt.      \tag{74}
\]
Averaging this inequality gives the same transport estimate for
empirical laws. Apply (70)--(71) to the base tuple (69). Convergence
on each fixed observation grid and (74), followed by
\(\Delta\downarrow0\), prove joint same-neuron Wasserstein-2 path
convergence on each population. For \(\delta^{(1)}\), multiplication
is continuous on the finite-dimensional continuous-path space and
its path norm is bounded by that of \(Q^{(1)}\). The latter has
uniformly integrable squared path norms by (72), so truncation gives
the same joint path convergence. Equation (72) with a larger moment
upgrades all these path laws to every fixed finite Wasserstein order.

Predictions and blocks 2 and 3 of (12) depend continuously on bounded
features, readout and delta in \(L^2\), uniformly in the state bounds.
For block 1 use (67) with the uniformly integrable squares of the
suprema of \(Q^{(1)}\). Thus mesh comparison controls the scalar
errors uniformly in time. For the remaining fixed-mesh errors there
are finitely many endpoint contractions; interpolating the states and
using their uniform \(L^2\) time modulus controls the intervals. This
proves the uniform-in-time prediction, loss, and three-block assertions.

**4.4. Original velocities and energies.** Compare finite GF velocities
to (73) evaluated at a fixed mesh approximation. The transformed state
and its transformed vector field have uniform \(L^2\) errors tending
to zero by (20), (29). For the first original velocity, use (67) and
the \(Q^{(1)}\) supremum integrability in (72); the same proof applies
to the first activation velocity. Rank and readout velocities are
Lipschitz in the state by (20). In the second preactivation identity
in (73), subtract the two operators and the two inputs. The operator
norm bound and the preceding \(\dot H^{(1)}\) comparison give
\(L^2\) errors tending to zero, uniformly in time in the width limsup.
Its fixed-mesh law is identified by the truncated query argument in
4.2.

The comparison velocities may be chosen piecewise constant at the
left comparison-mesh nodes. Their change from evaluating the same
vector field at the interpolated comparison state tends to zero in
the same estimates: the transformed state has an O(h) time modulus,
the first products use (67) and (72), and (73) then controls the
second preactivation velocity. Thus only finitely many comparison
velocity laws are required at each fixed mesh.

Explicitly, for any listed scalar-neuron velocity \(v_n\), its
piecewise-constant comparison \(v_n^h\), any \(T<\infty\), and any
\(\epsilon>0\), the comparison just proved has the quantifiers
\[
 \lim_{h\downarrow0}\limsup_{n\to\infty}
 \Pr\!\left(\sup_{t\le T}
   \frac{\|v_n^{\rm GF}(t)-v_n^h(t)\|_{\ell^2}}{\sqrt n}
       >\epsilon\right)=0.
\]
On the common population space the corresponding statement is
\(\sup_{t\le T}\|V(t)-V^h(t)\|_{L^2}\to0\). These imply the
integrated mean-square comparisons by multiplying the squared
supremum bound by \(T\). They do not identify finite neuron labels
with population labels. The second activation velocity uses the
additional uniform-integrability step immediately below; its
comparison has these same quantifiers once that step is completed.

For the final multiplication by \(\phi'(Z^{(2)})\), one more
uniform-integrability argument is necessary. At each fixed mesh,
the just-proved Wasserstein-2 convergence of the finitely many
\(\dot Z^{(2)}\) evaluations gives uniformly integrable squares in
probability. If \(x\) is \(L^2\)-close to such an approximation \(y\),
then
\[
 |x|^2\mathbf1_{|x|>R}
       \le4|x-y|^2+2|y|^2\mathbf1_{|y|>R/2}.                \tag{75}
\]
On the part \(|y|\le R/2<|x|/2\), use \(|x|\le2|x-y|\);
on its complement use \(|x|^2\le2|x-y|^2+2|y|^2\).
First choose a fine fixed comparison mesh, then increase \(R\),
and finally refine the mesh. The uniform \(L^2\) comparison just
proved makes (75) give uniform integrability for finite GF
\(\dot Z^{(2)}\) squares in that iterated limit. On the population
space the same follows from a finite cover of its continuous \(L^2\)
velocity curve by small \(L^2\) balls and (75). Now (67) proves the
last identity's velocity comparison in (73). This establishes all
individual hidden-velocity laws and quadratic norms, uniformly in time
in probability for the norms. It also establishes joint integrated
quadratic tests. No \(C\)-path law of the discontinuous mesh velocities
is asserted.

For the parameter speeds, (18) gives the first metric in (13), and
the middle squared speed is exactly
\[
 4\sum_{a,b}r_ar_b
       \mathbb E_2[\delta^{(2)}_a\delta^{(2)}_b]
       \mathbb E_1[H^{(1)}_aH^{(1)}_b],                      \tag{76}
\]
with finite normalized expectations before taking the limit. All
contractions converge. The readout metric is its normalized field
norm. Integration over the fixed horizon gives convergence of these
energies and of all hidden-velocity energies. The same identities
on the population satisfy the exact loss balance (25). For parameter
increments, integrate the field velocities; for the operator increment
approximate its rank integral by finite sums. The integrand is continuous
in Hilbert--Schmidt norm with width-independent modulus by (20), and
the squared norms of the finite sums are cross-time versions of (76).
Their joint contractions converge by the proved path/observation laws.
Thus increments and their quadratic metrics also converge.

Finally apply (31)--(33) with the actual random initialization. They
transfer every GF statement to the specified raw GD interpolation,
including kernels, velocities, and energies. For the base fields,
the uniform normalized state/field error is \(O_T(n^{-3/2})\), so
its maximal coordinate path error is at most \(\sqrt n\) times
that bound, namely \(O_T(n^{-1})\). For \(\delta^{(1)}\) use (32)
and the coordinate bound to get maximal coordinate path error tending
to zero as well. These same-neuron couplings transfer every finite
path Wasserstein order using the GF moment bounds. Fixed admissible
probes transfer using their Lipschitz instructions and their verified
\(L^2\) approximations. All assertions are on an arbitrary fixed
\(T<\infty\). Larger horizons use the same already constructed flow
and initialization; there is no time-uniform rate as \(T\to\infty\).

## 5. Exchange symmetry, persistent nonlinearity, and strict learning

**5.1. The exchange law and its finite justification.** Let
\(\bar1=2,\bar2=1\). There is an orthogonal reflection \(\mathcal R\)
of \(\mathbb R^d\) that swaps the two inputs. Explicitly,
\[
 v=\frac{x_1-x_2}{\|x_1-x_2\|_{\mathbb R^d}},\qquad
 \mathcal R=I-2vv^T,\qquad \mathcal R x_a=x_{\bar a}.
 \tag{77}
\]
The last identity follows from equal input norms; in the antiparallel
case it sends \(x_1\) to \(-x_1\). Consider the finite parameter map
\[
 (W^{(1)}_n,W^{(2)}_n,W^{(3)}_n)
       \longmapsto(W^{(1)}_n\mathcal R,W^{(2)}_n,-W^{(3)}_n).
 \tag{78}
\]
At any parameter state it sends \(z^{(\ell)}_{n,a},h^{(\ell)}_{n,a}\)
to the corresponding sample-\(\bar a\) fields, and sends
\[
 f_{n,a}\mapsto-f_{n,\bar a},\quad
 r_{n,a}\mapsto-r_{n,\bar a},\quad
 (\delta^{(2)}_{n,a},q^{(1)}_{n,a},\delta^{(1)}_{n,a})
   \mapsto-(\delta^{(2)}_{n,\bar a},q^{(1)}_{n,\bar a},
                                             \delta^{(1)}_{n,\bar a}).
 \tag{79}
\]
For residuals this uses \(y_{\bar a}=-y_a\).

The map preserves loss and the metric (7), and commutes with the finite
gradient equations. This can also be checked directly: the two signs
in \(r_a\delta_a\) cancel; relabeling the sample sum leaves the second
matrix velocity unchanged; the readout velocity changes sign; and
the first-matrix velocity is multiplied on the right by \(\mathcal R\),
using \(x_a^T\mathcal R=x_{\bar a}^T\). Thus it commutes with finite
GF and (6). The Gaussian first-row law is invariant under orthogonal
right multiplication. The initial second matrix is unchanged and
independent. Zero readout is fixed by negation. Consequently (78)
preserves the entire law of the auxiliary finite zero-readout GF,
including all velocities. It also preserves the actual Gaussian
readout initialization law, since that readout is symmetric and
independent, though the zero-readout argument alone suffices.

Pass this finite law symmetry through the full-sequence deterministic
population limit. The limiting predictions must satisfy
\[
 f_2(t)=-f_1(t),\qquad
 \|\dot Z^{(\ell)}_1(t)\|_{\mathcal H_\ell}
       =\|\dot Z^{(\ell)}_2(t)\|_{\mathcal H_\ell},\qquad
 \|\dot H^{(\ell)}_1(t)\|_{\mathcal H_\ell}
       =\|\dot H^{(\ell)}_2(t)\|_{\mathcal H_\ell}.            \tag{80}
\]
For the norm statements, the same finite symmetry exchanges the two
scalar squared norms, and each converges in probability to its
deterministic population value; therefore those values agree. Equivalently
the complete limiting same-neuron path law is invariant under the
corresponding field transformation. At \(\rho=0\) these are law
symmetries, not finite pathwise sample-pair identities. At \(\rho=-1\)
the stronger pathwise identities (17) follow from the opposite inputs.

**5.2. Unbounded field tails and all-time distributional nonaffinity.**
For \(C=I\), (66) reads
\[
 F(Z^{(1)}_a(t))=F(G_a)+\int_0^t c_a(v)\zeta_a(v)\,dv+E_a(t),
 \qquad |E_a(t)|\le C_T.                                   \tag{81}
\]
For antiparallel inputs, the same statement for sample 1 has control
\(c_1-c_2=-4r_1\); sample 2 is its negative. The integral is a
finite-variance Gaussian variable independent of the initial first
row. For a fixed time choose a finite bound \(M\) for which the
event that all the relevant Gaussian integrals have absolute value
at most \(M\) has positive probability. Independently choose \(G_a\)
sufficiently positive that \(F(G_a)-M-C_T>F(R)\). This event also
has positive probability and forces \(Z^{(1)}_a(t)>R\). Choosing
the opposite Gaussian tail proves \(Z^{(1)}_a(t)<-R\) with positive
probability. This holds for every finite \(R\) and every finite time.

For \(C=I\), the initial \(G_1,G_2\) are independent. The same argument
can impose any of the four sign patterns with arbitrarily large
magnitudes. Hence the support of
\((H^{(1)}_1(t),H^{(1)}_2(t))\) approaches all four corners
\((B,B),(B,-B),(-B,B),(-B,-B)\). Its uncentered feature Gram
\[
 \Gamma_1(t)=
       \big(\mathbb E_1[H^{(1)}_a(t)H^{(1)}_b(t)]\big)_{a,b}
 \tag{82}
\]
is positive definite. Indeed if a linear combination vanished almost
surely, continuity would make it vanish at the limiting corners
\((B,B)\) and \((B,-B)\); both coefficients would be zero. At
\(\rho=-1\) the Gram has rank one, and
\(\|H^{(1)}_1(t)\|_2>0\); no inverse of this singular Gram is used.

By (66), each second-layer Gaussian source has strictly positive
variance \(\|H^{(1)}_a(t)\|_2^2\). The bounded remainder implies
\[
 \mathbb P(Z^{(2)}_a(t)>R)
     \ge\mathbb P(\xi_a(t)>R+C_T)>0,
 \quad
 \mathbb P(Z^{(2)}_a(t)<-R)
     \ge\mathbb P(\xi_a(t)<-R-C_T)>0.                        \tag{83}
\]
No independence of the source from the remainder was used. Both
hidden preactivation distributions therefore have both unbounded tails
at every finite time, including zero.

For any of these \(L^2\) variables \(Z\), the span of \(1,Z\) is
closed in \(L^2\). To verify this explicitly, its \(2\)-by-\(2\)
Gram has determinant \(\operatorname{Var}(Z)>0\); its least eigenvalue
is positive, so an \(L^2\)-Cauchy sequence of affine functions has
Cauchy coefficients. If the infimum in (14) were zero, it would
therefore be attained with \(\phi(Z)=uZ+v\) almost surely. The
boundedness of \(\phi\) and an unbounded tail force \(u=0\).
Strict monotonicity of \(\phi\) would then force \(Z\) to be constant,
a contradiction. This proves the strictly positive infimum (14) for
every layer, sample, and finite time.

**5.3. Positive progress and all positive-time speeds.** Define
\[
 \kappa(t)=\tfrac14y^TK(t)y\ge0.
 \tag{84}
\]
By (80), \(r=(f_1-1)y\). Multiplying (24)'s prediction equation by
\(y^T/2\) gives \(\dot f_1=(1-f_1)y^TKy\), without needing an
additional kernel symmetry. Thus
\[
 \dot f_1=4(1-f_1)\kappa,\qquad
 1-f_1(t)=\exp\!\left(-4\int_0^t\kappa(v)\,dv\right)>0.       \tag{85}
\]
The integral is finite on finite horizons by the operator, readout,
and feature bounds. The exponential identity follows by solving the
scalar linear equation for \(1-f_1\), with initial value 1.

Put \(m=\mathbb E[\phi(N(0,1))^2]>0\). Initial Gaussian row conditioning
gives the second-layer pair \(Z^{(2)}(0)\) covariance \(mI\) at
\(\rho=0\), and the pair \((Z^{(2)}_1(0),-Z^{(2)}_1(0))\) with
\(Z^{(2)}_1(0)\sim N(0,m)\) at \(\rho=-1\). This is also (37)--(39)
at the initial forward calls: the first features have Gram \(mI\)
or the corresponding rank-one Gram, and there is no earlier reverse
response. Both hidden kernel blocks vanish at zero, while
\[
 \kappa(0)=\left\|\frac{H^{(2)}_1(0)-H^{(2)}_2(0)}2\right\|_2^2>0.
 \tag{86}
\]
In the orthogonal case the two initial second features are independent
nonconstant centered variables; in the antiparallel case the difference
is twice a nonzero variable. Continuity and (85) first give
\(f_1(t)>0\) for small positive times, and then monotonicity gives
\[
                         0<f_1(t)<1\qquad(t>0).             \tag{87}
\]
In particular \(W^{(3)}(t)\ne0\) in \(L^2\).

Because \(\phi'>0\) everywhere, every
\(\delta^{(2)}_a(t)=W^{(3)}(t)\phi'(Z^{(2)}_a(t))\) is nonzero
for \(t>0\). Equation (66) makes \(\zeta_a(t)\) nondegenerate.
Its bounded remainder then makes \(Q^{(1)}_a(t)\) have unbounded
tails, and in particular nonzero norm. For orthogonal inputs,
\[
 \dot Z^{(1)}_a=2(1-f_1)y_a\phi'(Z^{(1)}_a)Q^{(1)}_a,         \tag{88}
\]
and for antiparallel sample 1 the coefficient is \(4(1-f_1)\).
Each first preactivation speed is therefore strictly positive.
Multiplication by \(\phi'>0\) gives the same for its activation
speed. Equation (18) proves strict first-matrix speed.

For \(C=I\), the second-matrix speed satisfies
\[
 \begin{aligned}
 \|\dot W^{(2)}\|_{\mathrm{HS}}^2
  &=4(1-f_1)^2\sum_{a,b}y_ay_b
       \mathbb E_2[\delta^{(2)}_a\delta^{(2)}_b]\Gamma_1(t)_{ab}\\
  &\ge4(1-f_1)^2\lambda_{\min}(\Gamma_1(t))
                                  \sum_a\|\delta^{(2)}_a\|_2^2>0.
 \end{aligned}                                                   \tag{89}
\]
The inequality applies the positive definite matrix \(\Gamma_1(t)\)
to the pointwise vector \((y_a\delta^{(2)}_a)_a\), then integrates.
For antiparallel inputs the velocity is the nonzero rank-one operator
\(4(1-f_1)\delta^{(2)}_1\otimes H^{(1)}_1\).

To exclude cancellation in each second-layer preactivation velocity,
use the exact adjoint identity
\[
 \sum_a c_a\mathbb E_2[\delta^{(2)}_a\dot Z^{(2)}_a]
       =\|\dot W^{(2)}\|_{\mathrm{HS}}^2
                         +\sum_{a=1}^{m_\rho}\|\dot Z^{(1)}_a\|_2^2,
 \qquad c_a=-2r_a.                                         \tag{90}
\]
Indeed insert
\(\dot Z^{(2)}_a=\dot W^{(2)}H^{(1)}_a+
W^{(2)}\dot H^{(1)}_a\). The first term is the
Hilbert--Schmidt inner product of \(\dot W^{(2)}\) with
\(\sum_a c_a\delta^{(2)}_a\otimes H^{(1)}_a=\dot W^{(2)}\).
Moving the second term through the adjoint gives
\(\sum_a c_a\mathbb E_1[\delta^{(1)}_a\dot Z^{(1)}_a]\).
For \(C=I\) it is the displayed sum of squares. For opposite inputs
it is
\((c_1-c_2)\mathbb E_1[\delta^{(1)}_1\dot Z^{(1)}_1]
=\|\dot Z^{(1)}_1\|_2^2\), with no extra factor two.
The right side of (90) is positive. At least one second-layer
preactivation speed is nonzero, and the equal-norm law (80) makes
both nonzero. Multiplying by the positive gate gives strict second
activation speeds.

Finally
\(\dot W^{(3)}=2(1-f_1)(H^{(2)}_1-H^{(2)}_2)\).
If this vanished, the contrast field would vanish; but
\[
 f_1=\tfrac12\mathbb E_2[W^{(3)}(H^{(2)}_1-H^{(2)}_2)]>0
\]
by (80) and (87), a contradiction. This proves strict readout speed.
All these speeds are continuous and strictly positive for every
physical \(t>0\), so their energies on any nonempty positive-time
interval are positive. At zero the hidden velocities vanish because
the limiting readout and backward fields vanish, as required.

**5.4. The initial reverse law with the reused transpose.** We record
the initial return law explicitly for the kernel expansion. Define
the following initial coefficient fields, not new state variables:
\[
 \widehat W^{(3)}
       =\frac{H^{(2)}_1(0)-H^{(2)}_2(0)}2,\qquad
 \widehat\delta^{(2)}_a=\widehat W^{(3)}\phi'(Z^{(2)}_a(0)),
 \qquad
 \widehat Q^{(1)}_a=W^{(2)*}(0)\widehat\delta^{(2)}_a.
 \tag{91}
\]
For orthogonal inputs their joint first-population law is
\[
 \widehat Q^{(1)}_a
     =\sum_b\frac{\mathbb E_2[\widehat\delta^{(2)}_a
                                      Z^{(2)}_b(0)]}{m}\,\phi(G_b)
           +\eta_a,\qquad
 \mathbb E[\eta_a\eta_b]
       =\mathbb E_2[\widehat\delta^{(2)}_a\widehat\delta^{(2)}_b],
 \tag{92}
\]
where \(\eta\) is centered Gaussian and independent of the full initial
first row. In the antiparallel case use one column:
\[
 \widehat Q^{(1)}_1
   =\frac{\mathbb E_2[\widehat\delta^{(2)}_1 Z^{(2)}_1(0)]}{m}\phi(G_1)
       +\eta_1,\qquad
 \mathbb E\eta_1^2=\mathbb E_2[(\widehat\delta^{(2)}_1)^2]>0.
 \tag{93}
\]

Here is a finite proof, including the normalization. Collect initial
first features in an \(n\)-by-\(m_0\) matrix \(\mathsf H\), with
\(m_0=2\) or \(1\), their forward answers in
\(\mathsf Z=W^{(2)}_n(0)\mathsf H\), and the row functions in (91)
in a matrix \(\widehat{\boldsymbol\delta}\). Let
\(\Gamma_n=\mathsf H^T\mathsf H/n\) and
\(\Sigma_n=\widehat{\boldsymbol\delta}^T
\widehat{\boldsymbol\delta}/n\). Conditional Gaussian row projection
gives
\[
 W^{(2)}_n(0)=\mathsf Z(\mathsf H^T\mathsf H)^{-1}\mathsf H^T
                          +\widetilde W P_{\mathsf H^\perp},
\]
and consequently the conditional reverse law
\[
 (W^{(2)}_n(0))^T\widehat{\boldsymbol\delta}
  =\mathsf H\Gamma_n^{-1}
                (\mathsf Z^T\widehat{\boldsymbol\delta}/n)
       +P_{\mathsf H^\perp}\mathcal G\,\Sigma_n^{1/2},
 \tag{94}
\]
where \(\mathcal G\) has independent standard Gaussian entries,
independently of the old fields. With one column \(m_0=1\), this
is the identical rank-one formula. The empirical first-feature Gram
converges by iid averaging to \(mI\), or to \(m\) in the reduction.
Given \(\mathsf H\), rows of \(\mathsf Z\) are independent Gaussians
of covariance \(\Gamma_n\). Conditional averaging with Gaussian
second moments gives
\(\Sigma_n\to\mathbb E_2[\widehat\delta^{(2)}
(\widehat\delta^{(2)})^T]\) and
\(\mathsf Z^T\widehat{\boldsymbol\delta}/n
\to\mathbb E_2[Z^{(2)}(0)(\widehat\delta^{(2)})^T]\).
The deltas are bounded; for the latter contraction one uses the
Gaussian moments of \(Z^{(2)}(0)\), not a false boundedness claim.
The inverses are bounded with probability tending to one because
the limiting reduced Gram is positive definite.

The removed projection in (94) has conditional empirical \(p\)-moment
at most
\(C_p m_0\|\Sigma_n\|^{p/2}/n\) for \(p\ge2\), by the diagonal
projection calculation (47), applied to its finitely many columns.
After its removal, conditional independent Gaussian coordinates,
(48), and the tail bound (49) prove joint empirical convergence with
the old first-row roots, including every fixed polynomial moment.
This gives (92)--(93) inside the canonical space as well, since this
finite program was among its permissible queries.

Each diagonal variance in (92) is positive:
\(\widehat W^{(3)}\) is nonzero almost surely for the independent
nondegenerate initial Gaussian pair, and \(\phi'>0\).
In fact that \(2\)-by-\(2\) covariance is positive definite.
If a linear combination of the two deltas vanished, the full Gaussian
support and continuity, away from the line of equal coordinates,
would imply
\(\lambda_1\phi'(u)+\lambda_2\phi'(v)=0\) for all \(u\ne v\).
Varying \(u\) with \(v\) fixed and using the nonconstancy of
\(\phi'\) forces \(\lambda_1=0\), then \(\lambda_2=0\).
For (93), \(\phi(Z^{(2)}_1(0))\phi'(Z^{(2)}_1(0))\) is
nonzero except on a Gaussian null set. Thus in both geometries
\[
             \|\phi'(G_a)\widehat Q^{(1)}_a\|_2>0.           \tag{95}
\]
Indeed its conditional Gaussian variance given the first row is
positive and the multiplier is strictly positive. This argument
uses the actual reused transpose and does not assert independence
of finite coordinates after reuse.

**5.5. A strictly changing full kernel.** For this local expansion
only, use the increasing feature time
\[
 s(t)=\int_0^t4(1-f_1(v))\,dv,\qquad s(t)=4t+o(t).
 \tag{96}
\]
This does not change the raw clock of the theorem. A prime below
means \(d/ds\). At orthogonal inputs the feature-time equations are
\[
 U_a'=\tfrac12y_aQ^{(1)}_a,\quad
 (W^{(2)})'=\tfrac12\sum_a y_a\delta^{(2)}_a\otimes H^{(1)}_a,
 \quad (W^{(3)})'=\tfrac12(H^{(2)}_1-H^{(2)}_2).
 \tag{97}
\]
They are the gradient of the prediction contrast
\((f_1-f_2)/2\) in the raw parameter metric; along this trajectory
the contrast equals \(f_1\). At antiparallel inputs the one-field
versions have coefficient one in all three equations.

The integral readout equation gives
\(W^{(3)}(s)/s\to\widehat W^{(3)}\) strongly in \(L^2\).
Bounded continuous gates and operator-norm continuity then give
\[
 \delta^{(2)}_a(s)/s\to\widehat\delta^{(2)}_a,\qquad
 Q^{(1)}_a(s)/s\to\widehat Q^{(1)}_a
 \quad\hbox{strongly in }L^2.                              \tag{98}
\]
To justify each product, a bounded multiplier converging in measure
times a fixed \(L^2\) field converges strongly, as proved after (67).
Split off the strongly convergent field first. Thus no unproved
Fréchet second derivative of a nonlinear \(L^2\) map is needed.

For \(C=I\) define the leading velocity coefficients by
\[
 \begin{aligned}
 \widehat v^{(1)}_a
      &=\tfrac12y_a\phi'(G_a)\widehat Q^{(1)}_a,\\
 \widehat v^{(W,2)}
      &=\tfrac12\sum_a y_a\widehat\delta^{(2)}_a\otimes\phi(G_a),\\
 \widehat v^{(2)}_a
      &=\tfrac12y_a\left[
           m\widehat\delta^{(2)}_a
              +W^{(2)}(0)(\phi'(G_a)^2\widehat Q^{(1)}_a)\right].
 \end{aligned}                                                   \tag{99}
\]
Equations (73), (97), (98) and the initial feature Gram \(mI\)
give
\[
 (Z^{(1)}_a)'/s\to\widehat v^{(1)}_a,\quad
 (W^{(2)})'/s\to\widehat v^{(W,2)},\quad
 (Z^{(2)}_a)'/s\to\widehat v^{(2)}_a,                         \tag{100}
\]
in \(L^2\), Hilbert--Schmidt norm, and \(L^2\), respectively.
For example the rank contribution to the last limit is
\(\tfrac12\sum_b y_b\widehat\delta^{(2)}_b
\mathbb E_1[\phi(G_b)\phi(G_a)]
=y_a m\widehat\delta^{(2)}_a/2\); the first-layer contribution
is the other term in (99). Set
\[
 d_*=\sum_a\|\widehat v^{(1)}_a\|_2^2
                  +\|\widehat v^{(W,2)}\|_{\mathrm{HS}}^2
   =\tfrac14\sum_a\left(
       \|\phi'(G_a)\widehat Q^{(1)}_a\|_2^2
                         +m\|\widehat\delta^{(2)}_a\|_2^2\right)>0.
 \tag{101}
\]
The equality uses (9) and the orthogonal feature Gram. The actual
adjoint gives the useful identity
\[
 y_a\mathbb E_2[\widehat\delta^{(2)}_a\widehat v^{(2)}_a]
      =\tfrac12\left(m\|\widehat\delta^{(2)}_a\|_2^2
                        +\|\phi'(G_a)\widehat Q^{(1)}_a\|_2^2\right).
 \tag{102}
\]

For \(\rho=-1\), use only sample 1 and replace (99)--(101) by
\[
 \begin{aligned}
 \widehat v^{(1)}_1&=\phi'(G_1)\widehat Q^{(1)}_1,\\
 \widehat v^{(W,2)}&=\widehat\delta^{(2)}_1\otimes\phi(G_1),\\
 \widehat v^{(2)}_1&=m\widehat\delta^{(2)}_1+
                  W^{(2)}(0)(\phi'(G_1)^2\widehat Q^{(1)}_1),\\
 d_*&=\|\phi'(G_1)\widehat Q^{(1)}_1\|_2^2
                                  +m\|\widehat\delta^{(2)}_1\|_2^2>0.
 \end{aligned}                                                   \tag{103}
\]
The same strong limits (100) hold; the second sample velocities
are their negatives, and
\(\mathbb E_2[\widehat\delta^{(2)}_1\widehat v^{(2)}_1]=d_*\).
These one-field constants retain the raw factor four through (96).

Split the label-direction kernel as
\[
 \kappa_{\mathrm{hidden}}
      =\tfrac14y^T(K^{(1)}+K^{(2)})y,\qquad
 \kappa_{\mathrm{readout}}
      =\tfrac14y^TK^{(3)}y
      =\left\|\frac{H^{(2)}_1-H^{(2)}_2}2\right\|_2^2.
 \tag{104}
\]
The Gram formulas and feature equations give
\(\kappa_{\mathrm{hidden}}=
\sum_{a=1}^{m_\rho}\|(Z^{(1)}_a)'\|_2^2+
\|(W^{(2)})'\|_{\mathrm{HS}}^2\). Therefore (100)--(103)
imply \(\kappa_{\mathrm{hidden}}(s)=d_*s^2+o(s^2)\).
Differentiate the last expression in (104) along its \(L^2\) curve:
\[
 \kappa_{\mathrm{readout}}'
   =\sum_a y_a\mathbb E_2\!\left[
        \frac{H^{(2)}_1-H^{(2)}_2}2
                   \phi'(Z^{(2)}_a)(Z^{(2)}_a)'\right].
 \tag{105}
\]
Divide by \(s\), use (98)--(100), and then (102). The limit is
\(2d_*\). For antiparallel inputs the two equal contributions in
(105) and (103) give the same limit. Integration gives
\[
 \kappa_{\mathrm{readout}}(s)=\kappa(0)+d_*s^2+o(s^2),\qquad
 \kappa(s)=\kappa(0)+2d_*s^2+o(s^2).
 \tag{106}
\]
Thus the positive hidden contribution is accompanied by a positive
readout contribution, so it cannot be canceled in the full kernel.
Returning to the physical time in (96),
\[
                  \kappa(t)=\kappa(0)+32d_*t^2+o(t^2),
                  \qquad d_*>0.                            \tag{107}
\]
This proves the asserted strict leading change of the full raw kernel
near zero, in addition to all the positive-time motion and all-time
distributional nonaffinity already proved.

**5.6. Scope and proof record.** Sections 2--4 establish the canonical
operator, unique autonomous global finite-time flow, all specified
joint observable limits, both operator orientations, raw interpolation,
and velocity and energy limits. Section 3.6 discharges the global
response bound using identified fresh-root programs; Section 3.7
discharges the bounded Gaussian-remainder premises used in Section 5.
Section 5.1 supplies the exchange-law integration step. The deductions
therefore establish the entire special-angle theorem of 1.3 without
an additional mathematical premise.

The simplification in (15)--(16) has used \(C=I\), or the exact
antiparallel invariant relation. For a nonzero intermediate correlation,
the transformed first equation instead contains, for \(b\ne a\),
\[
 -2C_{ab}r_b\,
       \frac{1+(Z^{(1)}_a)^2}{1+(Z^{(1)}_b)^2}\,Q^{(1)}_b .
\]
The ratio is not a bounded \(L^2\) multiplier in general, and the
present proof supplies no corresponding estimate. No arbitrary-angle
completion, other depth, long-time interchange, or independent
resampling at restart is claimed.

For provenance only, the four mathematical input snapshots were read
in full and their whole-file SHA-256 values checked before construction:

- ORTHOGONAL_ANTIPARALLEL_FLOW_ANCHOR.md:
  c3f147633689050f8d9a4749e23861b02640dd7ba0e201b0f05a609b9c76cf39
- SPECIAL_ANGLE_CANONICAL_BRIDGE.md:
  de061c34befd83240e938c2511adc68168d6c2cbaa45b2c5b4b48e86a7a741c5
- SPECIAL_ANGLE_NONTRIVIALITY.md:
  b14f75e6909b32762aca147f14a6ab7d3bafd6394c2d93e9a4df76ed1b142c3c
- SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md:
  875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603

These are construction records, not citations used as mathematical
premises. In particular no softplus dynamics, cap-removal assertion,
or three-hidden-layer result is imported. Only the elementary Gaussian
mechanisms have been reproved here for the stated arctangent model.
