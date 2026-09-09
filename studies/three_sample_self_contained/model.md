# Global limits for three separated inputs in a three-hidden-layer network

## Part M. Model, notation, and theorem

### M.1. Finite network and physical training

All vector spaces in this manuscript are real. Fix an integer \(d\ge1\),
three deterministic vectors \(x_1,x_2,x_3\in\mathbb R^d\), and labels
\(y_1,y_2,y_3\in\{-1,1\}\). The input normalization and separation are
\[
 \|x_i\|_{\mathbb R^d}^2=d,\qquad
 \Gamma_{ij}=d^{-1}x_i^Tx_j,\qquad
 \Gamma_{ij}\le1-\delta\quad(i\ne j),\qquad \delta>0.       \tag{M.1}
\]
Thus \(\Gamma\) is positive semidefinite with unit diagonal. Its rank
may be less than three. A triple satisfying (M.1) exists only if
\(\delta\le3/2\): the squared norm of
\(\sum_i x_i/\sqrt d\) is nonnegative and at most \(9-6\delta\).
All statements quantify only over geometries realizable in the
specified dimension.

We will choose two constants \(a=a_\delta\ge1\) and \(e_\delta>0\).
For any fixed \(e\in(0,e_\delta]\), use the same activation
\[
                   \phi(z)=a(1+z)+e\arctan z                 \tag{M.2}
\]
in all three hidden layers. The constants \(a,e\) never depend on
width or training time. They may depend on the required separation.

For width \(n\), the raw parameters are
\[
 W^1\in\mathbb R^{n\times d},\quad W^2,W^3\in\mathbb R^{n\times n},
 \quad C\in\mathbb R^n.
\]
All initialized entries are mutually independent, with
\[
 W^1_{jk}(0)\sim N(0,d^{-1}),\quad
 W^2_{jk}(0),W^3_{jk}(0)\sim N(0,n^{-1}),\quad
 C_j(0)\sim N(0,n^{-2}).                                   \tag{M.3}
\]
The same initialization is used to couple the two training algorithms
at each width. No assumption about independence between different
widths is needed. Define
\(\langle u,v\rangle_n=n^{-1}u^Tv\) and
\(\|u\|_n=\langle u,u\rangle_n^{1/2}\).
For each sample \(i\),
\[
 \begin{split}
 z_i^1&=W^1x_i,\qquad h_i^1=\phi(z_i^1),\\
 z_i^2&=W^2h_i^1,\qquad h_i^2=\phi(z_i^2),\\
 z_i^3&=W^3h_i^2,\qquad h_i^3=\phi(z_i^3),\\
 f_i&=\langle C,h_i^3\rangle_n,\qquad r_i=f_i-y_i,\qquad
 L=\tfrac12\sum_{i=1}^3r_i^2.
 \end{split}                                                \tag{M.4}
\]
An activation or product of two vector fields is coordinatewise.
Residual-free backward vectors are
\[
 b_i^3=C\phi'(z_i^3),\quad
 b_i^2=\phi'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\phi'(z_i^1)(W^2)^Tb_i^2.                             \tag{M.5}
\]

The raw Hilbert metric on parameter increments is
\[
 \|\Delta\theta\|_{{\rm raw},n}^2
 =\frac dn\|\Delta W^1\|_F^2+
   \|\Delta W^2\|_F^2+\|\Delta W^3\|_F^2+\|\Delta C\|_n^2.
                                                               \tag{M.6}
\]
The physical gradient flow of \(L\) in this metric is
\[
 \begin{split}
 \dot W^1&=-d^{-1}\sum_i r_i b_i^1x_i^T,\\
 \dot W^\ell&=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T,
                     \qquad\ell=2,3,\\
 \dot C&=-\sum_i r_i h_i^3 .
 \end{split}                                                \tag{M.7}
\]
For example, the Euclidean first-block derivative has factor \(1/n\);
the inverse first-block metric multiplies it by \(n/d\), giving
\(1/d\). The readout inverse metric multiplies by \(n\), cancelling
the \(1/n\) in its Euclidean derivative. These calculations verify
all factors in (M.7).

Raw gradient descent is the simultaneous explicit Euler update
\(\theta_{k+1}=\theta_k+\eta_n F(\theta_k)\) for precisely (M.7),
where \(\eta_n=n^{-2}\). It uses the actual residuals at that node.
Interpolate the raw parameters linearly at physical times \(k\eta_n\).
All hidden fields at intermediate times are recomputed by (M.4);
hidden fields themselves are not linearly interpolated. Their
velocities are derivatives of those recomputed fields. At a mesh
node take the right derivative; at the endpoint of a closed
observation interval take the left derivative. The finite random
readout in (M.3) is never replaced by zero.

At any fixed width, GF has a global solution. The finite-dimensional
field is smooth and locally Lipschitz. Its energy identity gives
\(\int_0^T\|\dot\theta\|_{{\rm raw},n}^2\le L(0)\).
Hence its displacement before a finite endpoint is at most
\(\sqrt{TL(0)}\), and its increments near that endpoint are strongly
Cauchy by the same Cauchy--Schwarz bound. Local existence from the
finite endpoint extends the solution. GD is defined at every
finite step because its update is a finite composition of the
everywhere-defined smooth maps in (M.4)--(M.7).

### M.2. Population state and the meaning of its initialization

Part F constructs three probability spaces
\((\Omega_\ell,\mu_\ell)\), with \(H_\ell=L^2(\mu_\ell)\), from
the limiting same-layer laws of fixed finite Gaussian calculations.
They are separate neuron spaces: an element of \(H_1\) is never
multiplied coordinatewise by an element of \(H_2\) or \(H_3\).
The constructed initialized actions are
\[
 A_0:H_1\longrightarrow H_2,\qquad
 B_0:H_2\longrightarrow H_3 ,
 \qquad \|A_0\|_{\rm op},\|B_0\|_{\rm op}\le10,              \tag{M.8}
\]
with their actual Hilbert adjoints. The first weight field satisfies
\[
 w_0\in L^2(\Omega_1;\mathbb R^d),\qquad
 w_0\sim N(0,I_d/d),\qquad C_0=0.
                                                               \tag{M.9}
\]
The bound (M.8) and laws (M.9) are consequences of the finite
initialization and the construction in Part F. Arbitrary bounded
operators with these norms are not alternative initializations
for this theorem.

The affine population parameter space is
\[
 \mathcal X=
 L^2(\Omega_1;\mathbb R^d)
 \times\big(A_0+\mathcal S_2(H_1,H_2)\big)
 \times\big(B_0+\mathcal S_2(H_2,H_3)\big)\times H_3,          \tag{M.10}
\]
where \(\mathcal S_2\) denotes Hilbert--Schmidt operators.
Its increment norm is
\[
 \|\Delta\theta\|_{\rm raw}^2
 =d\|\Delta w\|_2^2+\|\Delta A\|_{\rm HS}^2
                    +\|\Delta B\|_{\rm HS}^2+\|\Delta C\|_2^2.
                                                               \tag{M.11}
\]
The equivalent sum norm replaces the square root of the sum
of four squares by the sum of their square roots. Estimates will
state when they use this sum norm. For \(u\in H_j,v\in H_i\),
\(u\otimes v:H_i\to H_j\) means \(q\mapsto u\langle v,q\rangle_i\).
Its Hilbert--Schmidt norm is \(\|u\|_j\|v\|_i\).

The population forward and backward fields are (M.4)--(M.5)
with \(W^1x_i\) replaced by \(w\cdot x_i\), \(W^2,W^3\)
by \(A,B\), transposes by their actual adjoints, and
normalized sums by expectations in the specified layer.
The evolution is
\[
 \dot w=-d^{-1}\sum_i r_i b_i^1x_i,\qquad
 \dot A=-\sum_i r_i b_i^2\otimes h_i^1,\qquad
 \dot B=-\sum_i r_i b_i^3\otimes h_i^2,\qquad
 \dot C=-\sum_i r_i h_i^3.                                 \tag{M.12}
\]
A strong \(C^1\) solution means a \(C^1\) path in the affine
Hilbert space (M.10), satisfying these identities there.
“Bounded primal quantities on compact intervals” means bounded
\(\sqrt d\|w\|_2,\|A\|_{\rm op},\|B\|_{\rm op},\|C\|_2\)
on each such interval. Initialization has
\(\sqrt d\|w_0\|_2=\sqrt d\); the selection of activation parameters
will use only the three normalized projections and raw
displacements, not a dimension-free bound on this full norm.
Components of \(w\) perpendicular to the span of the inputs
stay equal to their initialized values by (M.12).

### M.3. Precise observables

For probability measures with finite second moments on a separable
normed space \(E\), write
\[
 \mathcal W_2(\nu,\widetilde\nu)^2
 =\inf_{\pi\in\Pi(\nu,\widetilde\nu)}
                   \int\|u-v\|_E^2\,d\pi(u,v).
                                                               \tag{M.13}
\]
Here \(\Pi\) is the set of couplings with the specified marginals.
The space \(C([0,T];\mathbb R^k)\) is equipped with the supremum
of its Euclidean norm.

For each layer, let
\[
 X^\ell(t)=(z_1^\ell,h_1^\ell,z_2^\ell,h_2^\ell,
                              z_3^\ell,h_3^\ell)(t)\in\mathbb R^6,
 \qquad
 Y^\ell(t)=(X^\ell(t),\dot X^\ell(t))\in\mathbb R^{12}.
                                                               \tag{M.14}
\]
At width \(n\), the associated empirical law is the average of
the \(n\) Dirac masses at its neuron-row values. For paths, it is
the average of the \(n\) Dirac masses at the entire corresponding
continuous row paths. The population law uses \(\mu_\ell\).
Part V constructs continuous versions and proves their finite
second moments in the path norm.

The four raw kernel blocks are
\[
 \begin{split}
 K^1_{ij}&=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_1,\\
 K^2_{ij}&=\langle b_i^2,b_j^2\rangle_2
                             \langle h_i^1,h_j^1\rangle_1,\\
 K^3_{ij}&=\langle b_i^3,b_j^3\rangle_3
                             \langle h_i^2,h_j^2\rangle_2,\\
 K^4_{ij}&=\langle h_i^3,h_j^3\rangle_3 .
 \end{split}                                                \tag{M.15}
\]
Finite kernels use the normalized finite inner products.
They always use the true backward fields (M.5). When auxiliary
clipped flows are introduced, their update fields are different
objects; Part V proves the needed true-kernel observations
explicitly.

An additional generated probe is a fixed finite, layer-typed
expression formed from the first-row Gaussian roots, constants,
fields at finitely many observation times, deterministic linear
combinations, continuously differentiable coordinate maps with
bounded first derivatives, inner-product contractions, and
applications of any of \(A_0,B_0,A(t),B(t)\) or their adjoints
where domains and codomains match. Each contraction is performed
inside one layer. Its finite version uses exactly the corresponding
finite matrices and their transposes. A probe expression is fixed
before the width limit; its instruction count does not grow
with width. Both orientations of every action are included in
this definition. Named true-backward and velocity observations
are covered separately by the product-truncation proofs in Part V.

### M.4. The theorem

**Theorem M.1.** For each \(0<\delta\le3/2\), there are finite
constants \(a_\delta\ge1\) and \(e_\delta>0\) depending only on
\(\delta\), such that, for every fixed \(e\in(0,e_\delta]\),
every \(d,x_1,x_2,x_3,y_1,y_2,y_3\) satisfying (M.1), and the
network (M.2)--(M.7), the following hold.

1. There is one global autonomous strong \(C^1\) population
   solution (M.12). On the canonical action spaces it is unique
   among strong solutions with bounded primal quantities on
   compact intervals. Its continuation from every reached
   state is unique in that same class. It is the raw Hilbert
   gradient flow of \(L\).
2. For each deterministic \(T<\infty\), GF and raw GD converge
   jointly along the full width sequence in probability to
   that same solution in all the following senses:
   \[
   \sup_{t\le T}|f_{n,i}(t)-f_i(t)|\to0,\quad
   \sup_{t\le T}|L_n(t)-L(t)|\to0,\quad
   \sup_{t\le T}|K^\ell_{n,ij}(t)-K^\ell_{ij}(t)|\to0;
                                                               \tag{M.16}
   \]
   \[
   \mathcal W_2\big(\widehat{\operatorname{Law}}_n
        (X_n^\ell|_{[0,T]}),
          \operatorname{Law}(X^\ell|_{[0,T]})\big)\to0;           \tag{M.17}
   \]
   \[
   \sup_{t\le T}\mathcal W_2\big(
       \widehat{\operatorname{Law}}_n(Y_n^\ell(t)),
                       \operatorname{Law}(Y^\ell(t))\big)\to0.  \tag{M.18}
   \]
   At any fixed finite collection of times the full joint
   same-layer \(Y^\ell\) laws also converge in \(\mathcal W_2\).
   Their second moments and the integrals of each squared
   preactivation or feature speed converge. Every fixed finite
   same-layer tuple of generated probes has the corresponding
   empirical \(\mathcal W_2\) limit. No identification asserting
   operator-norm convergence of unrelated finite matrices
   across widths is intended.
3. There is a positive absolute constant \(\eta_*\), specified
   below, such that every sample and hidden layer obeys
   \[
    \inf_{t\ge0}\inf_{\alpha,\beta\in\mathbb R}
      E_\ell[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
                                  \ge e^2\eta_*/4>0.           \tag{M.19}
   \]
   Every hidden population parameter block has nonzero
   initial second derivative in its raw norm. Every sample's
   preactivation and feature field in every hidden layer
   has nonzero initial second derivative in \(L^2\).
   With \(p=y/3\) and
   \(\kappa(t)=p^T(\sum_{\ell=1}^4K^\ell(t))p\), one has
   \[
      \kappa(t)=\kappa(0)+18t^2\|V\|_{\rm hidden}^2+o(t^2),
                   \qquad\|V\|_{\rm hidden}>0,                 \tag{M.20}
   \]
   where \(V\) is explicitly defined in Part N.

All probabilistic limits in this statement refer to each fixed
admissible dataset and fixed finite \(T\). Their constants may
depend on that dataset, \(d,e,T\). The activation selection
does not. This is global population existence together with
compact-time finite-width convergence; it makes no interchange
of infinite-time and infinite-width limits.

Here is an explicit selection rule. For \(G\sim N(0,1)\), put
\[
 \begin{split}
 \mathcal R(Z)&=\inf_{\alpha,\beta}E[\arctan Z-\alpha-\beta Z]^2,\\
 \eta_*&=\inf_{\sigma\ge1}\mathcal R(\sigma G),\qquad
 t_*=\min\{1/2,\sqrt{\eta_*}/[2(1+\pi)]\},\qquad
 \lambda=\delta^2/4,\\
 a_\delta&=\max\left\{2000/\sqrt\lambda,\,
                   (10^{12}/(\lambda^2t_*))^{1/4}\right\},\\
 S&=12/(\lambda a_\delta^6),\\
 e_\delta&=\tfrac12\min\{1,e_*(a_\delta,12,S),
                                      (10^{10}a_\delta)^{-1}\}.
 \end{split}                                                \tag{M.21}
\]
We write \(e_*(a,B,S)=\epsilon_*(a,B,S)\), where (R.90) defines the latter.
Part G proves \(\eta_*>0\); Part R constructs the positive
number \(e_*(a,B,S)\) by a finite chain of estimates.
Consequently (M.21) is a genuine choice from separation alone,
not a pointwise minimum over unknown trained trajectories.

The proof proceeds by constructing the fixed finite Gaussian
calculations and their common action spaces in Part F; proving
the controlled response estimates in Part R; giving one bounded
total residual clock and removing the auxiliary caps in Part G;
proving the finite algorithm and observation limits in Part V;
and proving all initial-motion statements in Part N.
