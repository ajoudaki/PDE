# The literal convex activation: an obstruction to uniform conditioning

This note examines the activation
\[
 \phi_\varepsilon(z)=(1-\varepsilon)(1+z)+\varepsilon\psi(z),
       \qquad 0<\varepsilon<\tfrac12,                    \tag{1}
\]
where \(\psi\) is bounded and nonconstant, belongs to
\(C^2(\mathbb R)\), and satisfies
\(\|\psi\|_\infty,\|\psi'\|_\infty,\|\psi''\|_\infty\le1\).
These are the same normalized shape bounds as in the preceding
activation-class question. No overall gain is included or hidden
in the choice of \(\psi\).

The distinction proved below is important. A fixed convex
activation cannot have the depth-uniform initialized kernel
floor that supports the gain-based argument. This does not
prove that no fixed convex activation can have the qualitative
global training theorem at every separately fixed finite depth.
That latter statement is not established in this note.

## 1. Exact initialized network law

There are three deterministic inputs \(x_i\in\mathbb R^d\)
with \(\|x_i\|^2=d\). Put
\(\Gamma_{ij}=x_i^Tx_j/d\), and assume if desired
\(-1+\delta<\Gamma_{ij}<1-\delta\) for \(i\ne j\).
For a depth \(L\) network, first-layer weights have independent
\(N(0,1/d)\) entries, higher-layer weights have independent
\(N(0,1/n)\) entries, and readout coordinates have independent
\(N(0,n^{-2})\) entries. The readout is the normalized average
\(n^{-1}C^Th_i^L\).

The raw metric on parameter increments is explicitly
\[
 \|\Delta\theta\|_{{\rm raw},n}^2
   =\frac dn\|\Delta W^1\|_F^2+
      \sum_{\ell=2}^L\|\Delta W^\ell\|_F^2+
                                   \frac1n\|\Delta C\|^2. \tag{11}
\]
The kernel means the Gram of predictor gradients in this
metric, not in the unnormalized Euclidean parameter metric.
In particular the readout gradient is \(h_i^L\), because
its Euclidean derivative \(h_i^L/n\) is multiplied by the
inverse readout metric \(nI\). Its kernel block is therefore
\(n^{-1}(h_i^L)^Th_j^L\).

At population initialization \(C=0\). The hidden marginal
Gaussian recursion is
\[
 Z^1\sim N(0,\Gamma),\qquad
 h_i^\ell=\phi_\varepsilon(Z_i^\ell),\qquad
 Q_{\ell,ij}=E[h_i^\ell h_j^\ell],\qquad
 Z^{\ell+1}\sim N(0,Q_\ell).                             \tag{2}
\]
Each new centered Gaussian tuple has covariance equal to the
full uncentered feature Gram. To see this finite-width identity,
condition the next independent Gaussian matrix on its three
input vectors. Each output row is centered Gaussian with that
empirical covariance, independently across rows. Its covariance
converges to the deterministic preceding feature Gram. Induction
and the law of large numbers give (2); Lipschitzness supplies
finite second moments at every step. Singular input covariance
causes no difficulty because a positive semidefinite covariance
also defines a Gaussian law.

All coordinates \(Z_i^\ell\) have the same variance
\(\sigma_\ell^2\), with
\[
 \sigma_1=1,\qquad
 \sigma_{\ell+1}=\|\phi_\varepsilon(\sigma_\ell G)\|_2,
                          \quad G\sim N(0,1).             \tag{3}
\]
Let \(m=1-2\varepsilon>0\). The initialized variances stay in
the compact interval
\[
                         m\le\sigma_\ell\le1/\varepsilon
                                 \quad(\ell\ge1).        \tag{4}
\]
Indeed \(E\phi_\varepsilon(\sigma G)
=1-\varepsilon+\varepsilon E\psi(\sigma G)\ge m\), so
its second moment has square root at least \(m\).
For the upper bound, writing \(\alpha=1-\varepsilon\),
\[
 \|\phi_\varepsilon(\sigma G)\|_2
       \le\alpha\sigma+\alpha+\varepsilon
       =\alpha\sigma+1.
\]
The interval \([0,1/\varepsilon]\) is preserved by this
upper recursion and contains \(\sigma_1=1\).

## 2. Strict contraction at initialization for every allowed shape

Define
\[
 \kappa^2=\max_{m\le\sigma\le1/\varepsilon}
            E[\phi_\varepsilon'(\sigma G)^2].
                                                               \tag{5}
\]
Then \(0<\kappa<1\). The derivative lies in \([m,1]\).
The expectation in (5) is continuous in \(\sigma\) by bounded
convergence. At any positive \(\sigma\), equality to one would
force \(\phi_\varepsilon'=1\) almost surely under a full-support
Gaussian law. Continuity would make this equality hold
everywhere. Then \(\psi'=1\) everywhere, contradicting
boundedness of \(\psi\). Compactness of the interval in (4)
therefore gives a maximum strictly below one.

Here is the Gaussian comparison used to turn this derivative
bound into a contraction. If \(X,Y\) are centered jointly
Gaussian with variances \(\sigma^2\) and covariance
\(c\in[-\sigma^2,\sigma^2]\), then
\[
 E[(\phi_\varepsilon(X)-\phi_\varepsilon(Y))^2]
               \le\kappa^2 E[(X-Y)^2]                    \tag{6}
\]
provided \(\sigma\) belongs to (4).

We give the full covariance-differentiation proof. For
\(|c|<\sigma^2\) let \(p_c(x,y)\) be the centered Gaussian
density with covariance matrix
\(\begin{pmatrix}\sigma^2&c\\c&\sigma^2\end{pmatrix}\).
Direct differentiation of this density gives
\(\partial_c p_c=\partial_x\partial_y p_c\).
For verification, put \(D=\sigma^4-c^2\); both derivatives
divided by \(p_c\) equal
\[
 \frac cD+
 \frac{(\sigma^4+c^2)xy-\sigma^2c(x^2+y^2)}{D^2}.
\]
On a compact subinterval of \((-\sigma^2,\sigma^2)\),
Gaussian decay dominates all derivatives times the at-most
linear factors \(\phi_\varepsilon(x),\phi_\varepsilon(y)\).
Differentiation under the integral and two integrations by
parts therefore give, with zero boundary terms,
\[
 \frac d{dc}E_c[\phi_\varepsilon(X)\phi_\varepsilon(Y)]
                   =E_c[\phi_\varepsilon'(X)
                                  \phi_\varepsilon'(Y)].
\]
Cauchy--Schwarz bounds this derivative above by
\(E[\phi_\varepsilon'(\sigma G)^2]\le\kappa^2\).
Integrate from \(c\) to \(\sigma^2\), approaching the latter
from below. The expectation is continuous at both covariance
endpoints: couple
\(X=\sigma G\), \(Y=(c/\sigma)G+
\sqrt{\sigma^2-c^2/\sigma^2}\,H\) for independent standard
Gaussians \(G,H\), and use \(L^2\) convergence and Lipschitzness.
Thus
\[
 E[\phi_\varepsilon(\sigma G)^2]
    -E_c[\phi_\varepsilon(X)\phi_\varepsilon(Y)]
                              \le\kappa^2(\sigma^2-c).
\]
Twice this inequality is (6), including singular endpoint
covariances by the same continuity argument.

Apply (6) to the recursion (2). With
\(\Delta_{\ell,ij}=E[(h_i^\ell-h_j^\ell)^2]\), the input
distance is \(\Delta_{0,ij}=2(1-\Gamma_{ij})\), and
\[
 \Delta_{\ell,ij}\le\kappa^2\Delta_{\ell-1,ij},
 \qquad
 \Delta_{L,ij}\le2(1-\Gamma_{ij})\kappa^{2L}.              \tag{7}
\]
Consequently, using the unit coefficient vector
\((e_i-e_j)/\sqrt2\),
\[
 \lambda_{\min}(Q_L)
 \le\tfrac12\Delta_{L,ij}
 \le(1-\Gamma_{ij})\kappa^{2L}\longrightarrow0.           \tag{8}
\]
Here \(e_i\) are the usual coordinate vectors in
\(\mathbb R^3\), not the mixing coefficient.
This holds for every admissible input triple. Angular
separation at the input does not prevent the deeper initialized
features from approaching one another.

There is also a genuine collapse of normalized conditioning,
not just a common scalar shrinkage of all features. By (4),
each feature second moment is at least \(m^2\), while
\(E h_i^L\ge m\). Testing the Gram against
\(\mathbf1/\sqrt3\) gives
\[
 \lambda_{\max}(Q_L)\ge
 E\left[\left(\frac{\sum_i h_i^L}{\sqrt3}\right)^2\right]
 \ge3m^2.
\]
Together with (8) this shows
\(\lambda_{\min}(Q_L)/\lambda_{\max}(Q_L)\to0\).

## 3. A concrete fixed convex activation

Take \(\varepsilon=1/4\) and
\(\psi(z)=\tfrac14\arctan z\). This shape satisfies all the
normalized bounds: its sup norm is \(\pi/8<1\), first
derivative is at most \(1/4\), and second derivative is at
most \(3\sqrt3/32<1\) in absolute value. The literal activation is
\[
                  \phi(z)=\tfrac34(1+z)
                                      +\tfrac1{16}\arctan z.
                                                               \tag{9}
\]
Its derivative lies between \(3/4\) and \(13/16\). The
pointwise Lipschitz bound alone now proves
\[
 E[(h_i^L-h_j^L)^2]\le
       2(1-\Gamma_{ij})(13/16)^{2L},\qquad
 \lambda_{\min}(Q_L)\le
       (1-\Gamma_{ij})(13/16)^{2L}.                       \tag{10}
\]
This particular example does not need the Gaussian
covariance-differentiation argument in Section 2.

Here are the other kernel blocks and their initialized limit
in metric (11). Write \(\langle v,w\rangle_n=v^Tw/n\),
\(b_i^L=\phi_\varepsilon'(z_i^L)C\), and
\(b_i^\ell=\phi_\varepsilon'(z_i^\ell)
(W^{\ell+1})^Tb_i^{\ell+1}\). Direct differentiation and
metric inversion give
\[
 \begin{split}
 K^1_{n,ij}&=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_n,\\
 K^\ell_{n,ij}&=\langle b_i^\ell,b_j^\ell\rangle_n
             \langle h_i^{\ell-1},h_j^{\ell-1}\rangle_n
                                      \quad(2\le\ell\le L),\\
 K^{L+1}_{n,ij}&=\langle h_i^L,h_j^L\rangle_n.
 \end{split}                                                \tag{12}
\]
For example the raw matrix gradient is
\(b_i^\ell(h_i^{\ell-1})^T/n\), and its Frobenius pairing
is the product in (12); the first metric gives its
indicated \(\Gamma\) factor.

At each fixed finite depth the initialized hidden kernel
blocks tend to zero in probability. Indeed
\(E\|C(0)\|_n^2=n^{-2}\). Each initialized square matrix
has operator norm at most 10 with probability tending to
one: use a \(1/4\)-net of at most \(9^n\) unit vectors on
each side, the inequality
\(\|W\|\le2\max_{\text{net }u,v}|u^TWv|\), and the Gaussian
tail bound to obtain
\(\Pr(\|W\|>10)\le2\,9^{2n}e^{-100n/8}\to0\).
The net cardinality follows by disjoint radius-\(1/8\)
balls inside a radius-\(9/8\) ball. The scalar Gaussian
tail follows by optimizing
\(Ee^{t u^TWv}=e^{t^2/(2n)}\).
A finite union handles all \(L-1\) matrices.
Since \(|\phi_\varepsilon'|\le1\), backward induction
gives \(\|b_i^\ell\|_n=O_P(n^{-1})\) at each fixed layer.
The forward recursion (2) gives
\(\|h_i^\ell\|_n=O_P(1)\). Formula (12) therefore makes
every hidden block vanish, while its readout block
converges to \(Q_L\). This also explains the population
identity: there \(C=0\), so all hidden backward fields
vanish and the total initialized raw kernel is \(Q_L\).

Thus the initialized total population raw kernel obeys
(8), and in the concrete case it obeys (10). No positive
depth-independent lower bound for this kernel is possible
in the stated normalized convex class for
\(0<\varepsilon<1/2\).

## 4. What is and is not settled

The obstruction above rules out importing a proof that requires
the same positive initialized kernel floor at every depth.
It also rules out claiming that dividing a large-gain activation
by the sum of its coefficients preserves that proof: applying
this new function at every layer changes the forward and backward
recursions under the original fixed initialization and raw metric.

It does not refute the following weaker, still substantive
quantifier:
\[
 \exists\varepsilon>0\quad\forall\text{ fixed finite }L\ge2:
 \quad\text{the full global trained-limit theorem holds,
 with quantitative constants allowed to depend on }L.
\]
A kernel can be strictly positive at each fixed depth while
its smallest eigenvalue tends to zero over depths. Therefore
failure of a depth-uniform kernel floor is not a counterexample
to this qualitative trained statement.

In particular this note supplies no unproved implication from
initial separation to all-time separation, no cap-independent
incoming-tail estimate along actual training, and no positive
fixed mixing threshold for the global three-input dynamics.
Those are additional proof obligations for an affirmative answer
to the literal convex-mixture question. The exact convex family
remains the target; no gain-normalized surrogate is substituted.
