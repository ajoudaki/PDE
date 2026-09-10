# Explicit maintained dependencies

Complete finite model Sections 1–4 and special-data Parts II–III follow.
The operative dependencies are the finite metric/gradient/kernel, Part II
construction, and III.M/III.F. The rest of III supplies its referenced
proofs, so this packet has no omitted mathematical dependency.

## 1. Model and learning metric

Fix positive integers `L,m,d,n`, data `(x_a,y_a)` for `1<=a<=m`, and positive
constants `kappa_1,...,kappa_(L+1)`. Use the forward equations in NOTATION.md and
the mean squared loss

\[
\mathcal L_n=\frac1m\sum_{a=1}^m r_{n,a}^2,
\qquad r_{n,a}=f_{n,a}-y_a.
\]

Each activation is a real `C^2` function. The finite state consists of all raw
weight entries. Its gradient flow is `dot theta=-D grad mathcal L_n`, where
the constant diagonal operator `D` multiplies the first and last blocks by
`n kappa_1` and `n kappa_(L+1)`, respectively, and middle block `ell` by
`kappa_ell`. Gradients of matrix functions use the ordinary Frobenius pairing.

Backpropagation gives the exact derivatives

\[
\nabla_{W^{(1)}} f_{n,a}
=\frac{\delta_a^{(1)}x_a^T}{n\sqrt d},\qquad
\nabla_{W^{(\ell)}} f_{n,a}
=\frac{\delta_a^{(\ell)}(h_a^{(\ell-1)})^T}{n}\quad(2\le\ell\le L),
\qquad
\nabla_{W^{(L+1)}} f_{n,a}=\frac{h_a^{(L)}}n.
\tag{1}
\]

To verify (1), differentiate the readout first. Its derivative with respect to
`z_a^(L)` is `delta_a^(L)/n`. At a lower layer, differentiating
`z_a^(ell+1)=W^(ell+1) phi^(ell)(z_a^(ell))` multiplies this derivative by
`diag((phi^(ell))'(z_a^(ell))) (W^(ell+1))^T`, giving the stated backward
recursion. A variation of `W^(ell)` produces
`d z_a^(ell)=d W^(ell) h_a^(ell-1)`; at the first layer it produces
`d W^(1) x_a/sqrt(d)`. Taking their scalar products with `delta_a^(ell)/n`
proves all three formulas.

Consequently the exact physical flow is

\[
\begin{aligned}
\dot W^{(1)}&=-\frac{2\kappa_1}{m\sqrt d}
  \sum_a r_{n,a}\delta_a^{(1)}x_a^T,\\
\dot W^{(\ell)}&=-\frac{2\kappa_\ell}{mn}
  \sum_a r_{n,a}\delta_a^{(\ell)}(h_a^{(\ell-1)})^T
  &&(2\le\ell\le L),\\
\dot W^{(L+1)}&=-\frac{2\kappa_{L+1}}m
  \sum_a r_{n,a}h_a^{(L)}.
\end{aligned}
\tag{2}
\]

Exact GD of step `eta` adds `eta` times the right side of (2), with every
quantity evaluated at the same pre-update state. Recomputing one block before
updating the next would be a different algorithm.

## 2. Raw kernel blocks and dissipation

Define the mobility-weighted block kernel by
`K_(n,ab)^(ell)=<grad_(W^(ell)) f_(n,a),D_ell grad_(W^(ell)) f_(n,b)>`.
The identity `<u v^T,p q^T>_F=(u^T p)(v^T q)` and (1) give

\[
\begin{aligned}
K_{n,ab}^{(1)}&=\kappa_1\frac{x_a^Tx_b}{d}
                   \frac{(\delta_a^{(1)})^T\delta_b^{(1)}}n,\\
K_{n,ab}^{(\ell)}&=\kappa_\ell
 \frac{(h_a^{(\ell-1)})^T h_b^{(\ell-1)}}n
 \frac{(\delta_a^{(\ell)})^T\delta_b^{(\ell)}}n
 &&(2\le\ell\le L),\\
K_{n,ab}^{(L+1)}&=\kappa_{L+1}
                    \frac{(h_a^{(L)})^T h_b^{(L)}}n.
\end{aligned}
\tag{3}
\]

Each block is positive semidefinite: for any real sample coefficients `c_a`,
its quadratic form is the squared norm of
`D_ell^(1/2) sum_a c_a grad_(W^(ell)) f_(n,a)`.
With `K_n=sum_ell K_n^(ell)`, the chain rule now gives

\[
\dot f_{n,a}=-\frac2m\sum_b K_{n,ab}r_{n,b},\qquad
\frac{d}{dt}\mathcal L_n=-\frac4{m^2}r_n^T K_n r_n
=-\|D^{-1/2}\dot\theta\|_2^2.
\tag{4}
\]

In particular the last equality is the exact weighted energy identity

\[
\mathcal L_n(t)+\int_0^t\left[
 \frac{\|\dot W^{(1)}\|_F^2}{n\kappa_1}
 +\sum_{\ell=2}^{L}\frac{\|\dot W^{(\ell)}\|_F^2}{\kappa_\ell}
 +\frac{\|\dot W^{(L+1)}\|_2^2}{n\kappa_{L+1}}
\right]du=\mathcal L_n(0).
\tag{5}
\]

There is no factor of the residual inside `delta` or inside (3).

## 3. Global finite-width existence

For every finite initial state the flow (2) has a unique solution for all
`t>=0`. Indeed its vector field is locally Lipschitz: the finite composition
defining the loss is `C^2`. The local existence argument is the contraction
mapping for the integral equation on a closed ball of continuous curves, with
time small enough that the locally bounded Lipschitz field maps the ball into
itself and has contraction constant less than one. This also gives uniqueness.

On any interval of this solution, (5) and Cauchy–Schwarz imply

\[
\|D^{-1/2}(\theta(t)-\theta(s))\|_2
\le\sqrt{t-s}\left(\int_s^t
             \|D^{-1/2}\dot\theta(u)\|_2^2du\right)^{1/2}
\le\sqrt{(t-s)\mathcal L_n(0)}.
\tag{6}
\]

If its maximal forward endpoint were a finite `T`, (6) would make `theta(t)`
Cauchy as `t` tends to `T`. The metric in (6) is equivalent to the Euclidean
metric at fixed `n`, since all mobilities are positive. Its limit is a finite
state. The same local contraction construction at that state extends the
solution past `T`, a contradiction. This proves global existence without a
bounded-activation assumption. It does not assert global stability of GD.

For each `t<=T`, applying (6) blockwise gives

\[
\frac{\|W^{(1)}(t)-W^{(1)}(0)\|_F}{\sqrt n}
\le\sqrt{\kappa_1T\mathcal L_n(0)},\quad
\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_F
\le\sqrt{\kappa_\ell T\mathcal L_n(0)},\quad
\frac{\|W^{(L+1)}(t)-W^{(L+1)}(0)\|_2}{\sqrt n}
\le\sqrt{\kappa_{L+1}T\mathcal L_n(0)}.
\tag{7}
\]

The middle inequality applies to `2<=ell<=L`. It also bounds the operator
norm of each trained middle increment, since operator norm is at most
Frobenius norm. For arbitrary `s<t`, the corresponding bounds hold with
`T` replaced by `t-s`; thus these parameter paths have a uniform square-root
modulus when initial loss is uniformly bounded.

## 4. What is uniform in width

Suppose now the first derivatives of all activations are bounded, the fixed
inputs have bounded RMS norm, and the initial first/readout RMS norms and
middle operator norms are at most a constant independent of `n`. Assume also
`mathcal L_n(0)<=C`. Then on every finite `[0,T]` all preactivation,
activation and backward-vector RMS norms, and every entry of (3), are bounded
by a finite constant independent of `n`.

Here is the complete induction. From (7) the first Frobenius norm divided by
`sqrt(n)`, readout RMS and middle operator norms are bounded. Therefore

\[
\frac{\|z_a^{(1)}\|_2}{\sqrt n}
\le\frac{\|W^{(1)}\|_F}{\sqrt n}\frac{\|x_a\|_2}{\sqrt d},\qquad
\frac{\|z_a^{(\ell)}\|_2}{\sqrt n}
\le\|W^{(\ell)}\|_{\rm op}
       \frac{\|h_a^{(\ell-1)}\|_2}{\sqrt n}.
\]

If `b_ell=sup |(phi^(ell))'|`, the fundamental theorem of calculus gives
`|phi^(ell)(z)|<=|phi^(ell)(0)|+b_ell |z|`. The triangle inequality transfers
each preactivation RMS bound to an activation RMS bound and closes the forward
induction. The reverse induction is

\[
\frac{\|\delta_a^{(L)}\|_2}{\sqrt n}
\le b_L\frac{\|W^{(L+1)}\|_2}{\sqrt n},\qquad
\frac{\|\delta_a^{(\ell)}\|_2}{\sqrt n}
\le b_\ell\|W^{(\ell+1)}\|_{\rm op}
               \frac{\|\delta_a^{(\ell+1)}\|_2}{\sqrt n}.
\]

Cauchy–Schwarz in each pairing in (3) proves the kernel-entry bounds. The
depth is fixed; this argument supplies no depth-uniform constants.

These initial bounds hold with probability tending to one for the independent
Gaussian initialization in NOTATION.md. First-block squared RMS is a sum of
`nd` Gaussian squares divided by `n` and tends to `d` by the elementary law
of large numbers; stored-readout squared RMS tends to zero. For a middle
matrix, a `1/4`-net of the unit sphere has at most `9^n` points, by disjoint
radius-`1/8` balls and a volume comparison. Approximating both vectors in a
bilinear form by net points bounds the operator norm by twice the largest net
bilinear form. Each fixed form is `N(0,1/n)`. The Gaussian exponential bound
and a union bound give

\[
\mathbb P(\|W^{(\ell)}(0)\|_{\rm op}>M)
\le 2\,9^{2n}e^{-nM^2/8}.
\]

Choose fixed sufficiently large `M` and use a union bound over the fixed depth.
The forward induction at time zero then bounds the initial activations, and
`|f_(n,a)(0)|<=||W^(L+1)(0)||_2 ||h_a^(L)(0)||_2/n` bounds initial loss.
This supplies the claimed high-probability initial event.

Uniform RMS bounds do not control multiplication by an unbounded coordinate
function in the population space. Thus (5)–(7) establish useful a priori
estimates but do not replace the source-identification and response-stability
proofs needed for a nonlinear population theorem.



---

## II. Equal labels with three hidden layers

**Theorem II.1.** Fix \(m=2,L=3\), \(\|x_a\|^2=d\),
\(-1\le\rho=G_{12}<1\), and \(y_1=y_2=y\in\{-1,1\}\).
Use the same activation \(\phi(z)=1+\arctan(z)/10\) at all three
hidden layers, the initialization and raw metric above, summed loss,
and exact raw GD with \(\eta_n=n^{-2}\).

There are canonical layer spaces and initialized bounded actions
\(W^{(2)}_0,W^{(3)}_0\), with their genuine adjoints, on which the raw
population gradient flow is global and unique among strong solutions
with bounded primal quantities on every compact interval. It is uniquely
restartable from every reached full state. For every finite \(T\), actual
finite GF and actual raw GD converge jointly in probability along the
full width sequence to this flow. The joint observations include:

- both samples' same-layer preactivation and feature path laws in
  \(\mathcal W_2(C([0,T]))\);
- forward/backward fields, hidden velocities and fixed generated probes,
  jointly within each layer at finitely many times, with second moments;
- predictions, loss, all four raw \(2\times2\) kernel blocks and squared
  velocity norms uniformly on \([0,T]\), and integrated squared speeds.

The parameter increments are Hilbert--Schmidt in the two operator blocks;
their scalar norm and cross-time contraction observations follow from
rank-one integration. No cross-width operator-norm convergence is asserted.

The predictions satisfy \(f_1=f_2=yg\), with
\[
 0\le g(t)<1,\qquad
 1-g(t)\le e^{-25t/9},\qquad
 \mathcal L(t)=2(1-g(t))^2\le2e^{-50t/9}.
 \tag{II.1}
\]
Every sample/layer has strictly positive affine-regression error at
every finite time. Every hidden parameter block, hidden preactivation
and hidden feature has strictly positive speed at every \(t>0\);
the readout does too. Initial hidden speeds are zero, but initial
feature changes and the full label-mode kernel have nonzero quadratic
terms in physical time. The activation and its nonlinear amplitude are
fixed throughout all limits.

The bounds use the feature clock only after constructing its flow:
\[
 g=y(f_1+f_2)/2,\qquad \frac{ds}{dt}=4(1-g),\qquad
 s_* \le 36/25 < 3/2.
 \tag{II.2}
\]
Finite residuals need not lie exactly in the equal-label mode. Section II.C.4
controls their off-mode component directly.

For the proof, \(c_-=5/6\), \(a=7/6\) are scalar activation bounds;
\(m=2\) remains the sample count. Section II.A gives exact two-label
identities before specializing to equal labels. Section II.B establishes
the two-query estimate, II.C constructs and compares the flows, and II.D
proves nonaffinity and motion. The reduction's broader label identities
are not a global opposite-label \(L=3\) theorem.

### II.A. Exact finite geometry and label mode


#### II.A.1. Raw gradient, metric, and four kernel matrices

For self-contained scope, let n,d be positive integers,
V^(1) in R^(n by d), W^(2),W^(3) in R^(n by n), and W^(4) in R^n.
The initialization blocks are independent and have independent entries:
V^(1)_(ij)~N(0,1/d), W^(2)_(ij),W^(3)_(ij)~N(0,1/n),
and the rescaled W^(4)_i~N(0,n^-2). The zero-readout auxiliary
initialization, when specified below, replaces only W^(4)_0 by zero.
The intended population readout starts identically at zero.
Labels y_1,y_2 belong to {-1,1}.
Let x_1,x_2 in R^d obey ||x_a||^2=d, and set
G_ab=x_a^T x_b/d. Then G=[[1,rho],[rho,1]], with -1<=rho<1.
For each sample define z^(1)_a=V^(1)x_a,
z^(2)_a=W^(2)h^(1)_a, z^(3)_a=W^(3)h^(2)_a,
h^(ell)_a=phi(z^(ell)_a), and
f_a=(W^(4))^T h^(3)_a/n. The output weights are rescaled throughout.

For raw variations use the squared metric

    d||dV^(1)||_F^2/n + ||dW^(2)||_F^2 + ||dW^(3)||_F^2
                                        + ||dW^(4)||_2^2/n.

Define the residual-free backward fields for each sample by

    delta^(3)_a=W^(4) phi'(z^(3)_a),
    q^(2)_a=(W^(3))^T delta^(3)_a,
    delta^(2)_a=phi'(z^(2)_a)q^(2)_a,
    q^(1)_a=(W^(2))^T delta^(2)_a,
    delta^(1)_a=phi'(z^(1)_a)q^(1)_a.

Ordinary coordinate differentiation, in reverse layer order, gives

    df_a = (delta^(1)_a)^T dV^(1)x_a/n
         + (delta^(2)_a)^T dW^(2)h^(1)_a/n
         + (delta^(3)_a)^T dW^(3)h^(2)_a/n
         + (h^(3)_a)^T dW^(4)/n.

Therefore the metric gradient of f_a has blocks

    delta^(1)_a x_a^T/d,
    delta^(2)_a (h^(1)_a)^T/n,
    delta^(3)_a (h^(2)_a)^T/n,
    h^(3)_a.

For loss_sum=sum_a(f_a-y_a)^2, the raw update is exactly -eta_n grad loss_sum,
eta_n=n^-2. Multiplying the first update by x_b gives

    z^(1)_{b,+}-z^(1)_b
         =-2 eta_n sum_a G_ba(f_a-y_a)delta^(1)_a.             (II.A.1)

The gradient pairings give the four kernel entries

    K^(1)_ab=G_ab (delta^(1)_a)^T delta^(1)_b/n,
    K^(ell)_ab=[(delta^(ell)_a)^T delta^(ell)_b/n]
               [(h^(ell-1)_a)^T h^(ell-1)_b/n], ell=2,3,
    K^(4)_ab=(h^(3)_a)^T h^(3)_b/n.                           (II.A.2)

Every block matrix is positive semidefinite because it is a Gram matrix
of the corresponding parameter gradients. Thus, writing K=sum_ell K^(ell),

    dot f=-2K(f-y),     dot loss_sum=-4(f-y)^T K(f-y)<=0.             (II.A.3)

Here dots refer to finite GF dot theta=-grad loss_sum in physical time
t=k eta_n, not to an exact discrete prediction update. Differentiability
of phi suffices for the identities along an existing differentiable
solution. For a unique finite GF solution map we assume phi is C^2
(as for the shifted arctan below), hence the finite field is locally
Lipschitz, and restrict to its existence interval. Finite GF is global as well: its squared raw speed equals minus the
loss derivative, so its raw displacement on [0,T] is bounded by
sqrt(T loss_sum(0)). It is therefore Cauchy at any finite endpoint,
and the locally Lipschitz finite vector field continues it there.
At the population
level the formulas remain identities whenever the
displayed products and derivatives are justified in the raw Hilbert
parameter space; they are not substitutes for that justification.

The update to V^(1) has its row vectors in span{x_1,x_2}. Orthogonal
row components never move. For -1<rho<1, a first-layer variation with
sample values v_1,v_2 and no orthogonal component has squared metric

    (1/n) sum_i (v_{1,i},v_{2,i}) G^(-1) (v_{1,i},v_{2,i})^T. (II.A.4)

Indeed the unique in-span row is (v_1,v_2)(X^T X)^(-1)X^T,
where X has columns x_1,x_2 and X^T X=dG. Its ordinary squared norm
is (v_1,v_2)G^(-1)(v_1,v_2)^T/d. This proves (II.A.4) after multiplying
by d/n and summing. At rho=-1, x_2=-x_1 and z^(1)_2=-z^(1)_1
exactly; the in-span squared metric is ||v_1||^2/n.

#### II.A.2. Exact exchange symmetry, and what it does not assert

By the global label/readout sign symmetry it suffices in law to consider
y=(1,sigma), sigma in {1,-1}. Specifically, negating both labels and
W^(4) preserves the loss and all hidden raw updates, and negates the
readout update. The centered Gaussian readout initialization has this
symmetry. No finite realization is asserted to equal its sign transform.

Let v=(x_1-x_2)/||x_1-x_2||, and let R=I-2vv^T. Equality of input norms
gives R x_1=x_2 and R x_2=x_1. Define the parameter isometry

    S(V^(1),W^(2),W^(3),W^(4))
       =(V^(1)R,W^(2),W^(3),sigma W^(4)).                    (II.A.5)

The first three hidden fields on sample a at S(theta) are exactly the
fields on sample 3-a at theta. Therefore

    f_a(S(theta))=sigma f_{3-a}(theta),    loss_sum(S(theta))=loss_sum(theta).

Because S is a linear isometry of the raw metric, differentiating the
last equality gives grad loss_sum(S(theta))=S grad loss_sum(theta). Thus raw GD and
the unique finite GF solution map commute with S on their existence
intervals. The jointly independent initialization law specified above
is invariant under S:
isotropic Gaussian first-layer rows are unchanged by R, the two hidden
matrices are unchanged, and the independent centered readout is
unchanged in law by its optional sign.

Consequently the finite prediction paths obey the equality IN LAW

    (f_1(t),f_2(t))_t  =_law  (sigma f_2(t),sigma f_1(t))_t.  (II.A.6)

This is not a pathwise identity at finite width. If a deterministic
population prediction limit exists, (II.A.6) forces f_2=sigma f_1.
For random non-deterministic subsequential limits, symmetry in law alone
would not force that pathwise relation.

There is also a useful intrinsic population formulation. Write J_ell
also for the pullback on L^2 of a measure-preserving involution of
neuron space ell. It is a self-adjoint isometry and commutes with
coordinate functions. Suppose
J_ell W^(ell)_0=W^(ell)_0 J_(ell-1) for ell=2,3,
J_1 Z^(1)_{1,0}=Z^(1)_{2,0}, and
J_3 W^(4)_0=sigma W^(4)_0; the last condition holds for zero readout.
Consider the full state transformation

    Z^(1)_a -> J_1 Z^(1)_(3-a),
    W^(ell) -> J_ell W^(ell) J_(ell-1), ell=2,3,
    W^(4) -> sigma J_3 W^(4).

Assume the equations and uniqueness class are invariant under this
transformation and the constructed initial-value problem is unique
in that class. The listed premises fix its ENTIRE initial state, so
the transformed solution has the same initial data. Uniqueness proves

    Z^(ell)_2=J_ell Z^(ell)_1,
    J_ell W^(ell)=W^(ell)J_(ell-1), ell=2,3,
    J_3 W^(4)=sigma W^(4),     f_2=sigma f_1.                (II.A.7)

Building such common spaces is compatible with symmetric finite-program
laws, but that construction and the required flow uniqueness are separate
obligations. The construction and uniqueness premises are established for equal labels
in Section II.C below.

#### II.A.3. The normalized label-mode feature field

On a population path satisfying (II.A.7), put

    g=(f_1+sigma f_2)/2=f_1.

Since r_1=g-1 and r_2=sigma(g-1), the physical parameter field is

    dot theta=4(1-g) grad g.                                (II.A.8)

This is an identity of the full parameter gradient, not merely the
gradient of a scalar restriction in an unspecified metric. With feature
time s defined by ds/dt=4(1-g), the reparameterization is valid only
where 1-g is nonzero and is increasing where g<1. For the intended
zero population readout g(0)=0. On an existing regular symmetric
physical trajectory, the chain rule gives

    1-g(t)=(1-g(0))exp{-4 integral_0^t ||grad g(theta(u))||^2 du}.

Thus g<1 persists on each compact interval on which that integral is
finite. Division by the clock there gives the feature field

    theta'=grad g,
    (z^(1)_b)'=(1/2)sum_a G_ba y_a phi'(z^(1)_a)q^(1)_a,
    (W^(ell))'=(1/2)sum_a y_a delta^(ell)_a
                                       (h^(ell-1)_a)^T/n, ell=2,3,
    (W^(4))'=(h^(3)_1+sigma h^(3)_2)/2.                    (II.A.9)

The population versions use the same factors 1/2, expectation rank-one
operators in place of outer products/n, and adjoints in place of
transposes. They have

    g'=||grad g||^2=(1/4)y^T K y.                           (II.A.10)

Thus a scalar clock can indeed be recovered after establishing symmetry.
To use it globally one must construct the feature flow up to its level
g=1 (or otherwise for the required clocks), not merely invoke symmetry.
At finite width the physical residual vector is not exactly in this
mode. Raw GD/GF comparison must control its other component separately;
one cannot assign the finite process the scalar clock (II.A.8) as an identity.

### II.B. Two-query short-interval response estimate

Take phi(z)=1+arctan(z)/10, epsilon=1/10, c_-=5/6, a=7/6.
Thus c_-<phi<a, 0<phi'<=1/10, and |phi''|<=1/5.
Let y_1,y_2 each equal +1 or -1. Let G be the two-sample Gram matrix,
with diagonal one and off-diagonal rho in [-1,1]. The estimates below
even allow rho=1, though nontriviality at that configuration is not
asserted here.

Let tau_R be smooth, odd, equal to its argument on [-R,R], with
|tau_R(q)|<=min(|q|,2R) and 0<=tau_R'<=1.
Use arbitrary finite caps R_1,R_2>=1. The bottom clip affects only
the first-coordinate update, and the middle clip defines delta^(2).
The readout starts at zero. The first coordinate remains RAW; no
componentwise F transform is used.

#### II.B.1. Exact scalar law and derivative convention

Let Delta>0, M a nonnegative integer, S=M Delta<=3/2.
Time index k ranges from 0 to M, sample index a from 1 to 2.
Let (G_1,G_2) be centered Gaussian with covariance G. The scalar law is

    Z^(1)_{ka}=G_a+(Delta/2)sum_(r<k,b) G_ab y_b
                           phi'(Z^(1)_{rb})tau_R1(q^(1)_{rb}),
    H^(1)_{ka}=phi(Z^(1)_{ka}),

    Z^(ell)_{ka}=xi^(ell)_{ka}
                    +sum_(r<k,b) A^(ell)_{ka,rb}delta^(ell)_{rb},
    H^(ell)_{ka}=phi(Z^(ell)_{ka}), ell=2,3,

    W^(4)_k=(Delta/2)sum_(r<k,b)y_b H^(3)_{rb},
    delta^(3)_{ka}=W^(4)_k phi'(Z^(3)_{ka}),

    q^(2)_{ka}=zeta^(2)_{ka}
                         +sum_(r<=k,b) B^(3)_{ka,rb}H^(2)_{rb},
    delta^(2)_{ka}=phi'(Z^(2)_{ka})tau_R2(q^(2)_{ka}),

    q^(1)_{ka}=zeta^(1)_{ka}
                         +sum_(r<=k,b) B^(2)_{ka,rb}H^(1)_{rb}.     (II.B.1)

Each sum over b includes both samples. The four centered Gaussian
source groups xi^(2),xi^(3),zeta^(2),zeta^(1) are mutually independent
and independent of the root pair. Within a group both time and sample
correlations are retained, including singular covariance matrices:

    E[xi^(ell)_{ka}xi^(ell)_{rb}]
                           =E[H^(ell-1)_{ka}H^(ell-1)_{rb}],
    E[zeta^(ell-1)_{ka}zeta^(ell-1)_{rb}]
                           =E[delta^(ell)_{ka}delta^(ell)_{rb}].

The deterministic coefficients are

    A^(ell)_{ka,rb}
       =E[partial H^(ell-1)_{ka}/partial zeta^(ell-1)_{rb}]
                         +(Delta/2)y_b E[H^(ell-1)_{ka}H^(ell-1)_{rb}],
                                                          r<k,
    B^(ell)_{ka,rb}
       =E[partial delta^(ell)_{ka}/partial xi^(ell)_{rb}]
         +(Delta/2)1_(r<k)y_b E[delta^(ell)_{ka}delta^(ell)_{rb}],
                                                          r<=k.  (II.B.2)

All formal partial derivatives hold previously selected deterministic
coefficients and Gaussian covariance parameters fixed. Distinct source
slots remain distinct even at singular covariances.

The finite realization to be identified has iid bottom neuron tuples
(z^(1)_(0,i,1),z^(1)_(0,i,2))~N(0,G); two initial matrices
W^(2)_0,W^(3)_0 with iid N(0,1/n) entries, independent of each other
and all root tuples; and EXACTLY zero initial readout W^(4)_0=0.
Its current forward fields use the current matrices. Its reverse
queries are (W^(3)_k)^T delta^(3)_(ka) and
(W^(2)_k)^T delta^(2)_(ka), with gates and cuts as in (II.B.1).
Its raw bottom and readout updates are the finite vector versions of
(II.B.1); both sample queries are computed before the simultaneous Euler
updates. Identification concerns each fixed M,Delta,R_1,R_2, not a
program whose number of queries grows with width.

To relate this law to that actual finite Euler scheme, unroll each
matrix's updates
W^(ell)_{k+1}=W^(ell)_k+(Delta/2n)sum_b
y_b delta^(ell)_{kb}(h^(ell-1)_{kb})^T.
The learned forward term has coefficient
(Delta/2)y_b E[H^(ell-1)_{ka}H^(ell-1)_{rb}], and the learned reverse
term has coefficient
(Delta/2)y_b E[delta^(ell)_{ka}delta^(ell)_{rb}], precisely as in (II.B.2).
The initial-action forward response is the expected source derivative
in (II.B.2), and the reverse response is its transpose counterpart.
Sections III.F.1--III.F.7 prove these response identities, joint empirical
averages, and removal of singular-Gram query perturbations. Their hypotheses
are checked for this two-matrix program in the next paragraph.

At fixed caps the raw first update is a bounded product of bounded
smooth gates and clipped queries; all required coordinate maps can be
extended to globally Lipschitz C^1 maps with bounded first derivatives.
The readout satisfies |W^(4)_k|<=aS and can be smoothly truncated outside
this known interval in a fixed program without changing values or
derivatives on attained states. Finitely many empirical contractions
can be restored from their deterministic limits by finite Lipschitz
induction. Thus the stated identification uses a fixed finite program,
not an unproved number-of-queries-uniform Gaussian assertion.

#### II.B.2. Claim and induction order

Put

    U_k=max_a sum_(r<=k,b)|B^(2)_{ka,rb}|,
    V_k=max_a sum_(r<=k,b)|B^(3)_{ka,rb}|.

We prove, uniformly in caps, mesh, labels and G,

    V_k<=3067/3200<1,
    U_k<=71063018523/73728000000<97/100,                    (II.B.3)

and for ell=2,3 and r<k,

    |A^(ell)_{ka,rb}| < (3/2)Delta/2.                     (II.B.4)

In particular for j=1,2 and either sample,

    E exp((q^(j)_{ka})^2/16)<2.                            (II.B.5)

Let A=3/2 (a bound on the time-kernel coefficient, not the activation
bound a). At zero time the readout and delta^(3) vanish as formal
expressions, so B^(3)_0=0 and zeta^(2)_0=0 almost surely.
Keep the formal expressions q^(2)_(0a)=zeta^(2)_(0a) and
delta^(2)_(0a)=phi'(xi^(2)_(0a))tau_R2(zeta^(2)_(0a)).
Their FORWARD-source derivatives vanish on the attained Gaussian law,
because tau_R2(0)=0. Hence B^(2)_0=0 and U_0=V_0=0.
Their reverse-source derivatives need not vanish: for example the
derivative of delta^(2)_(0a) in its own reverse-source slot is
phi'(xi^(2)_(0a))>0. No zero-variance source slot is deleted in this
base case or in later formal differentiation.

Assume U_r,V_r<=1 for all r<k. Construct and bound the current objects
in the order

    A^(2), Z^(2), A^(3), Z^(3), delta^(3),
    B^(3), q^(2), delta^(2), B^(2).

The first-coordinate values at time k use only past backward queries.
The following estimates do not use U_k before bounding it.

#### II.B.3. Bottom raw-coordinate sensitivities

For a single past source zeta^(1)_(sb), its first direct contribution
to any Z^(1)_(ja), j>s, has absolute value at most Delta epsilon/2,
because |G_ab|<=1 and |tau_R1'|<=1.
Writing a formal variation as d, the raw first update satisfies

    |d[phi'(Z^(1)_(ra))tau_R1(q^(1)_(ra))]|
      <= |q^(1)_(ra)||dZ^(1)_(ra)|/5 + |dq^(1)_(ra)|/10.

Furthermore

    |dq^(1)_(ra)| <= 1_((r,a)=(s,b))
                 +(1/10)sum_(v<=r,c)|B^(2)_(ra,vc)||dZ^(1)_(vc)|.

The sum over a of the absolute first-update coefficient |G_ba y_a|/2
is at most one. Taking maxima over output samples and preceding times,
the elementary product-form discrete Gronwall induction gives

    |partial H^(1)_(ja)/partial zeta^(1)_(sb)|
                                        <=(Delta/200)E^(1)_j,     (II.B.6)
    E^(1)_j=exp{Delta sum_(r<j)[max_a|q^(1)_(ra)|/5+U_r/100]}.

For completeness, the comparison used here says that
u_j<=u_0+sum_(r<j)c_r max_(v<=r)u_v, c_r>=0, implies
max_(v<=j)u_v<=u_0 product_(r<j)(1+c_r)<=u_0 exp(sum c_r).
The same proof applies when the initial injection begins at s+1.

Past top queries have
||q^(2)_(ra)||_2<=aS/10+a<=161/120=:Q_0, r<k,
because their source variance is at most (aS/10)^2 and response
shift at most aV_r. Hence each bottom Gaussian source has standard
deviation <=Q_0/10. Also
max_a|q^(1)_(ra)|<=max_a|zeta^(1)_(ra)|+a.

For two arbitrarily correlated centered Gaussians with variances <=v,

    E exp(lambda max_a|G_a|)
         <=sum_a E exp(lambda|G_a|)<=4 exp(lambda^2 v/2).   (II.B.7)

Jensen over the time slots requires no independence in time. It gives

    E E^(1)_j
      <=4 exp{S(a/5+1/100)+(S/5)^2(Q_0/10)^2/2}
      <4 exp(2/5)<6.                                     (II.B.8)

The first exponent is at most
73/200 + (9/200)(161/1200)^2 <2/5.
For the last inequality, e<11/4 and
(11/4)^2<(3/2)^5 give e^(2/5)<3/2.
Using (II.B.6) in (II.B.2),

    |A^(2)_(ja,sb)|
      <=(Delta/2)[a^2+(1/100)E E^(1)_j]
      <(Delta/2)(49/36+3/50)<A Delta/2.                   (II.B.9)

This is the replacement for the one-sample natural-coordinate argument.

#### II.B.4. Middle sensitivities with both sample correlations retained

Define the maximum total forward-source derivative row

    R_j=max_a sum_(s<=j,b)
                    |partial Z^(2)_(ja)/partial xi^(2)_(sb)|.

There is exactly one direct derivative in each sample's current row,
not one for every source slot. For a forward-source variation,

    |d delta^(2)_(ra)|<=|q^(2)_(ra)||dZ^(2)_(ra)|/5
                                                 +|dq^(2)_(ra)|/10,
    |dq^(2)_(ra)|<=(1/10)sum_(v<=r,b)
                                      |B^(3)_(ra,vb)||dZ^(2)_(vb)|.

Using (II.B.9), sum over the two update samples. Their factor Delta/2
becomes Delta, not 2 Delta. Discrete Gronwall gives

    max_(v<=j) R_v <= E^(2)_j,
    E^(2)_j=exp{A Delta sum_(r<j)
                             [max_a|q^(2)_(ra)|/5+V_r/100]}.       (II.B.10)

For a single reverse source zeta^(2)_(sb), the first injection into
the forward recursion is at most A Delta/20, since (II.B.9) gives
A Delta/2 and the gate gives 1/10. The same argument yields

    |partial H^(2)_(ja)/partial zeta^(2)_(sb)|
                                    <=(A Delta/200)E^(2)_j.      (II.B.11)

The middle reverse Gaussian variances are <=(aS/10)^2<=(7/40)^2.
Using (II.B.7), time Jensen, and the past V_r<=1, for p>=1 we get

    E(E^(2)_j)^p
      <=4 exp{219p/400 +3969p^2/1280000}.                  (II.B.12)

Thus E E^(2)_j<8: the exponent for p=1 is less than 3/5,
and e^(3/5)<2 follows from e<3 and 3^3<2^5.
For p=2, taking the square root in (II.B.12) gives

    ||E^(2)_j||_2
      <=2 exp{219/400+7938/1280000}<7/2.                  (II.B.13)

Indeed the exponent is less than 5/9; e<68/25 follows from its
series through degree five and a geometric bound on the remaining
tail. The integer inequality (68/25)^5<(7/4)^9 then gives
e^(5/9)<7/4.
Equations (II.B.11)-(II.B.12) now give

    |A^(3)_(ja,sb)|
      <=(Delta/2)[a^2+(A/100)E E^(2)_j]
      <(Delta/2)(49/36+3/25)<A Delta/2.                   (II.B.14)

The strict margin is small but positive: 49/36+3/25=1333/900<3/2.

#### II.B.5. Top response, then current middle response

Let T_j be the maximum, over the two samples, of the total absolute
xi^(3)-derivative row of Z^(3) at time j. Differentiate the readout
sum and the top gate. Since |W^(4)_j|<=aS,

    max_a sum_(s<=j,b)|partial delta^(3)_(ja)/partial xi^(3)_(sb)|
       <=(Delta/100)sum_(r<j)T_r +(aS/5)T_j
       <=(73/300)S max_(v<=j)T_v.

Equation (II.B.14) and the strictly past forward recursion give

    max_(v<=j)T_v<=exp{A(73/300)S^2}
                           <=exp(657/800)<5/2.

For example 657/800<5/6 and e^(5/6)<3^(5/6)<5/2,
the last inequality following from 3^5 2^6<5^6.
Adding the learned covariance row in (II.B.2) proves the CURRENT bound

    V_k<=(73/300)S(5/2)+a^2 S^3/100
                      <=73/80+147/3200=3067/3200=:V_*.    (II.B.15)

We may now sharpen the current query norm, before using any U_k bound:

    ||q^(2)_(ka)||_2<=aS/10+aV_*
                           <=24829/19200=:Q_*.

The same Q_* bound holds for past times, since their completed induction
steps also proved (II.B.15), not merely V_r<=1. The current middle derivative
row obeys, by the full current return in its expression (II.B.1),

    sum_(s<=k,b)|partial delta^(2)_(ka)/partial xi^(2)_(sb)|
                       <=(|q^(2)_(ka)|/5+V_k/100)E^(2)_k.

Cauchy--Schwarz and (II.B.13), followed by the covariance row bound in (II.B.2),
therefore yield

    U_k <= (7/2)(Q_*/5+V_*/100)+(3/200)Q_*^2
          =71063018523/73728000000 <97/100<1.               (II.B.16)

The learned covariance row has factor
(Delta/2) times two samples, and at most S/100 times Q_*^2.
No current U_k entered (II.B.9), (II.B.14), (II.B.15), or (II.B.16).
The induction closes for all meshes and caps and proves (II.B.3)-(II.B.4).

#### II.B.6. Two actual-query Gaussian envelopes

For either reverse layer and either sample, (II.B.1) and (II.B.3) give

    q^(j)_(ka)=zeta^(j)_(ka)+beta^(j)_(ka),
    |beta^(j)_(ka)|<=a.

The variance of zeta^(2) is <=(7/40)^2. The variance of zeta^(1)
is <=(Q_*/10)^2<(7/40)^2. Neither beta is asserted independent
of its source. The elementary squared inequality therefore gives

    E exp(q^2/16)
       <=exp(a^2/8) E exp(zeta^2/8)
       <=exp(49/288)(1-49/6400)^(-1/2)<2,

by the one-dimensional Gaussian integral. For the numerical bound
exp(49/288)<exp(1/5)<=5/4 and the other factor is <4/3.
This proves (II.B.5) for both problematic multipliers.

### II.C. Construction, both-cap removal and physical algorithms

All first-layer fields below are RAW two-sample fields. Finite vector
norms must be divided by sqrt(n). The initial root pair is Gaussian
with covariance G; there is no cubic F root and no F transform.
The activation is the single fixed phi=1+arctan/10.

#### II.C.1. Common state and the two-cut feature vector field

Use the countable common-program construction proved in Sections III.F.1--III.F.7
for three neuron populations and two independent initialized matrices.
Its permitted bottom root tuple is (G_1,G_2), with covariance G. Include
both samples and the smooth two-cut Euler programs of Section II.B.
This is an instance of the theorem as stated: it allows any fixed finite
root tuple and any fixed finite list of adjacent matrices, not only the
three-sample application made later in Part III.
The finite conditioning/averaging proof allows finite root tuples with
arbitrary within-tuple dependence, including G_2=-G_1. Its same-layer
joint second-moment laws define fixed spaces Omega_1,Omega_2,Omega_3.
Passing the finite operator bound 10 for every rational combination and
the exact transpose pairings, then extending by density, defines
W^(2)_0,W^(3)_0 and their actual adjoints. No Gaussian resampling is
performed on later uses.

The state is

    theta=(Z^(1)_1,Z^(1)_2,W^(2),W^(3),W^(4)),

where both first fields belong to L^2(Omega_1), the matrices are bounded
operators, and the readout is in L^2(Omega_3). Use the distance

    d(theta,theta_tilde)=sum_a||Z^(1)_a-Ztilde^(1)_a||_2
                   +sum_(ell=2,3)||W^(ell)-Wtilde^(ell)||_op
                   +||W^(4)-Wtilde^(4)||_2.                       (II.C.1)

At rho=-1 restrict to Z^(1)_2=-Z^(1)_1; the equations preserve it.
For -1<rho<1 this norm is equivalent, for fixed rho, to the raw
first-layer tangent Hilbert norm using G^(-1). Orthogonal first-weight
components are frozen and irrelevant to the two sample fields.

The full first row can be retained without introducing another dynamic field.
Let \(\mathsf X=[x_1\ x_2]\), let
\(g_a=V^{(1)}_0x_a\), and augment the root tuple by the full Gaussian
row \(V^{(1)}_0\). For \(-1<\rho<1\), reconstruct it by
\[
 V^{(1)}(s)=V^{(1)}_0+
       [Z^{(1)}_1(s)-g_1,\ Z^{(1)}_2(s)-g_2]\,
                          G^{-1}\mathsf X^T/d.
 \tag{II.C.r1}
\]
At \(\rho=-1\), use
\[
 V^{(1)}(s)=V^{(1)}_0+
                     (Z^{(1)}_1(s)-g_1)x_1^T/d.
 \tag{II.C.r2}
\]
Multiplication by each input verifies the prescribed sample values.
The added row lies in their span, so the orthogonal component stays
at its initialized value. Formula (II.A.4), or its one-field version,
is exactly the squared first-row metric of this increment. Applying
the bounded linear reconstruction to the first-field convergence gives
the corresponding first-weight observations and speeds; canonical storage
is \(W^{(1)}=\sqrt d\,V^{(1)}\). Enlarging the finite root tuple is
explicitly permitted by III.F.1 and preserves its actual Gaussian joint law.



For R>=1 cut both reverse queries at R. Compute the usual forward
fields and delta^(3)_a=W^(4)phi'(Z^(3)_a), then

    q^(2)_a=(W^(3))^*delta^(3)_a,
    delta^(2)_(R,a)=phi'(Z^(2)_a)tau_R(q^(2)_a),
    q^(1)_(R,a)=(W^(2))^*delta^(2)_(R,a).

Let V_R be the feature field

    (Z^(1)_b)'=(1/2)sum_a G_ba y_a
                            phi'(Z^(1)_a)tau_R(q^(1)_(R,a)),
    (W^(2))'=(1/2)sum_a y_a delta^(2)_(R,a) tensor H^(1)_a,
    (W^(3))'=(1/2)sum_a y_a delta^(3)_a tensor H^(2)_a,
    (W^(4))'=(1/2)sum_a y_a H^(3)_a.                       (II.C.2)

Here U tensor V maps B to U E[VB]. For R=infinity all cuts are removed.
The field is autonomous for each fixed R, though the finite-cut field
is not asserted to be the raw gradient. Its Euler scalar law is exactly
the law in Section II.B with R_1=R_2=R.

Since |phi|<=a=7/6 and |phi'|<=1/10, the readout norm is bounded by
its initial norm+aS. The norm of W^(3) is bounded by its initial norm
plus (a/10)S times this readout bound. The norm of W^(2) is bounded
next using ||delta^(2)||<=||q^(2)||/10. Finally the first-coordinate
velocities are bounded by the product of these operator/readout bounds
and bounded gates. The row sum of |G_ba|/2 is at most one.
Thus all primal norms and all vector-field norms have bounds C_S
independent of width and R on every fixed feature interval [0,S].
For zero readout the pointwise bound |W^(4)(s)|<=as holds.

For fixed R the field is locally Lipschitz on these bounded sets,
provided the reference readout has its attained pointwise bound.
Indeed the forward fields are Lipschitz in (II.C.1). For two such states
A,B, with only B's readout assumed bounded pointwise, the expansion

    delta^(3)_a(A)-delta^(3)_a(B)
      =[W^(4)_A-W^(4)_B]phi'(Z^(3)_(A,a))
        +W^(4)_B[phi'(Z^(3)_(A,a))-phi'(Z^(3)_(B,a))]

bounds both the top delta difference and the q^(2) difference by C_S d.
Middle clipping then bounds its delta difference by C_S(1+R)d.
The q^(1) difference has the same bound, by the reverse operator norm.
Finally bottom clipping gives a C_S(1+R)d bound again, not an R^2 bound:
its query difference has coefficient at most 1/10, and only its separate
gate-difference term costs R. Rank-one differences have the same bound.

Picard contraction in continuous paths with slightly enlarged primal
bounds and |W^(4)(s)|<=as constructs the zero-readout cut flow. The
readout integral preserves that closed constraint. The primal bounds
permit continuation across every finite feature interval.
The same argument works at finite width. Its fixed-R Euler defect is
at most C_(R,S)Delta^2 and its global error at most C_(R,S)Delta,
uniformly on the initial operator-norm event. Combining fixed finite
program convergence with this error proves the fixed-R width limit,
jointly for finite same-layer probe programs and finitely many times.
Uniform time convergence follows from a finite time net and the primal
velocity bounds.

#### II.C.2. Asymmetric comparison with two reference tails

Let A use cap R'>=R (including infinity) and B cap R. Assume common
primal bounds and a pointwise bound only for B's readout. Define
b_R(q)=(|q|-R/2)_+ and

    e_R(B)=sum_a[||b_R(q^(2)_a(B))||_2
                                    +||b_R(q^(1)_(R,a)(B))||_2].

For the middle field insert and subtract values at B inside tau_(R').
The resulting three terms are the query difference with gate at A,
the gate difference multiplying tau_R at B, and
phi'(Z_A)[tau_(R')(q_B)-tau_R(q_B)]. Here the symbol tau_(R') in this
sentence denotes the cap-R' FUNCTION, not its scalar derivative.
The last term is bounded by 4b_R(q_B) times the gate bound.
Consequently

    sum_a||delta^(2)_(R',a)(A)-delta^(2)_(R,a)(B)||_2
         <=C(1+R)d(A,B)+C sum_a||b_R(q^(2)_a(B))||_2.

Reverse multiplication gives this bound also for the q^(1) difference.
Apply the identical three-term split at the bottom, now with that
q^(1) difference. It gives

    ||V_(R')(A)-V_R(B)|| <= C(1+R)d(A,B)+C e_R(B).           (II.C.3)

The norm on fields is the sum of the component norms in (II.C.1), and V_(R')
again denotes the field at cap R', not a derivative. In particular
the coefficient is linear in R, uniformly in the larger cap.
There is no tail hypothesis on A.

On S=3/2, Section II.B and Fatou after fixed-R Euler convergence give

    sup_(R,s<=S,a,j=1,2) E exp((q^(j)_(R,a)(s))^2/16)<=2. (II.C.4)

For j=2 its definition does not depend on the bottom cap; all queries
are evaluated at the actual cut state. If E exp(q^2/16)<=2, the scalar
estimate gives the required bound directly: if E exp(q^2/16)<=2,
then q^2 exp(-q^2/32)<=32/e and
E[q^2 1_(|q|>u)]<=64 exp(-u^2/32). Since
b_R(q)<=(|q|)1_(|q|>R/2), taking square roots gives

    ||b_R(q)||_2<=8 exp(-R^2/256).

It follows that e_R(theta_R(s))<=32 exp(-R^2/256)=:epsilon_R.
Gronwall in (II.C.3) yields

    sup_(s<=S)d(theta_R'(s),theta_R(s))
                           <=CS exp(C(1+R)S)epsilon_R.    (II.C.5)

Thus the cut states converge uniformly in a complete Banach state
space. Their computed q^(2) queries converge strongly by top stability.
The middle three-term bound then gives strong convergence of delta^(2)
and q^(1). The bottom bound gives convergence of the ACTUAL uncut
velocities. Passing the integral equations constructs a C^1 uncut
feature flow on the entire [0,S].

Any bounded-primal uncut competitor compares against the same reference
theta_R by (II.C.3). Its constants may be larger, but exp(CR)epsilon_R
tends to zero for every fixed C. This proves uniqueness. The estimate
also proves restart uniqueness at any reached s_0<S: the discrepancy
from theta_R(s_0) in (II.C.5) only contributes one more factor exp(CR).
No tail bound for a competing flow is required.

The rank-one integrals converge also in Hilbert--Schmidt norm: the
rank-one difference bound uses exactly the same vector-norm products
as the operator bound. Hence the raw parameter increments lie in the
affine Hilbert space specified by the finite metric's population limit.

#### II.C.3. Symmetry and the same-label physical flow

The finite constant-label-mode Euler scheme and the finite cut feature
flow are equivariant under the exchange/sign transformation from
Section II.A. Their initialized empirical predictions and feature
second moments converge to deterministic laws. Hence at every cut
time they have f_2=y_1 y_2 f_1 and equal sample feature second moments.
These properties pass to the uncut flow just constructed. This use of
deterministic limiting scalar laws does not assert finite samplewise
residual equality or require an already proved uncut population symmetry.

By a global readout/label sign flip it suffices for same labels to take
y_1=y_2=1. Let g=(f_1+f_2)/2. The scalar predictor is continuously
Frechet differentiable in the raw Hilbert metric: expand it from the
top down; for a fixed B in L^2 use

    |E B[phi(Z+v)-phi(Z)-phi'(Z)v]|
        <=C R||v||_2^2+C||B 1_(|B|>R)||_2||v||_2.

First fix R and send ||v|| to zero, then remove R. Products containing
two parameter changes have quadratic size; adjunction identifies each
metric gradient. Continuity of the gradient follows by truncating a
fixed old L^2 backward factor when its gate changes. For rho>-1 use
the equivalent first-pair norm with G^(-1); at rho=-1 use its one-field
subspace and the first gradient from Section II.A.
Thus the uncut feature field is exactly grad g and

    g'=||grad g||^2 >= E[((H^(3)_1+H^(3)_2)/2)^2]>=c_-^2.

Initially g=0. There is a unique s_*<=1/c_-^2=36/25<3/2 at which g=1.
The continuous gradient norm is bounded on [0,S]. Hence

    t(s)=integral_0^s du/[4(1-g(u))]

is increasing on [0,s_*) and tends to infinity at s_*:
if B bounds g', then 1-g(s)<=B(s_*-s), and its reciprocal integral
diverges logarithmically. The inverse s(t) is defined at all t>=0,
obeys s_dot=4(1-g), and is strictly below s_* at every finite time.
The time-changed raw flow satisfies dot theta=-grad loss_sum exactly.

Since \(g_s\ge c_-^2=25/36\), the physical residual obeys
\((1-g)_t=-4g_s(1-g)\le-(25/9)(1-g)\).
Integrating gives (II.1). For \(y=-1\), negate the readout and labels;
the aligned predictor \(g=y(f_1+f_2)/2\) and all raw norm conclusions
are unchanged. Moreover \(y(W^{(4)})_s=(H_1^{(3)}+H_2^{(3)})/2
\ge c_-\), so the readout speed is strictly positive after multiplying
by the positive physical clock. This fitting statement concerns the
population and compact-time approximation, not an exchange of the
width limit with an infinite-time finite-optimizer endpoint.


Global physical uniqueness need not assume that a competing solution
is symmetric. Fix its finite horizon and compare it against theta_R(s(t)).
This reference has derivative lambda(t)V_R with lambda=4(1-g(s(t))).
Its actual physical cut-loss field differs from that derivative only
through its prediction error against the uncut reference; by (II.C.5) that
error is at most C exp(CR)epsilon_R. On bounded states prediction
differences are Lipschitz in (II.C.1). The physical analogue of (II.C.3) therefore
has right side C_T(1+R)d+C_T epsilon_R+C_T exp(CR)epsilon_R.
Gronwall removes R. The same argument from a reached time includes the
initial error (II.C.5). This proves unique physical restart without assigning
a scalar clock to the competitor or assuming its residual symmetry.

#### II.C.4. Exact finite physical GD and GF without a false scalar clock

Let theta_(n,R)(s) be the finite zero-readout cut FEATURE flow and
compare actual finite physical GD/GF with
B_(n,R)(t)=theta_(n,R)(s(t)), using the deterministic population clock.
This reference is an analytical comparison path, not the final dynamics.
For fixed R its empirical laws converge uniformly on S. In particular,
at either sample,

    sup_(t<=T)|f_(n,R,a)(s(t))-f_a(s(t))|
        <= o_probability(1)+C exp(CR)epsilon_R.             (II.C.6)

The finite tail measurements e_(n,R) are square roots of empirical
averages of the continuous quadratic-growth function b_R^2.
Their uniform-in-time convergence follows at fixed R from the joint
W_2 laws and the fixed-R query time modulus. Thus

    sup_(s<=S)e_(n,R)(s)<=epsilon_R+o_probability(1).        (II.C.7)

For the finite actual physical vector field, split each residual
difference into the actual/reference prediction difference and (II.C.6).
The latter controls both the label mode and the off-mode residual.
The same-width analogue of (II.C.3) gives a coefficient C_T(1+R) times
state discrepancy, plus the reference tails (II.C.7) and prediction error (II.C.6).
Initial discrepancy is ||W^(4)_0||/sqrt(n)=O_probability(n^-1).
The first weights and both hidden matrices are initialized identically
in the two same-width paths.

For finite GF the integral comparison and Gronwall apply directly
up to a fixed primal stopping bound. For raw GD there is no nonlinear
coordinate transform: each update is EXACT Euler in the raw state.
The reference B_(n,R) has a local step defect at most C_(R,T)eta_n^2,
using its fixed-cap Lipschitz field and the population clock's bounded
first derivative and bounded continuous second derivative on [0,T].
Indeed s'=4(1-g(s)) and s''=-4g'(s)s', with g' continuous.
Consequently the maximal stopped node discrepancy is at most

    exp(C_T(1+R)T)
         [O_probability(n^-1)+C_(R,T)eta_n
             +C_T epsilon_R+C_T exp(CR)epsilon_R
             +o_probability(1)].                         (II.C.8)

The o_probability terms here are taken at fixed R. One first takes
width to infinity and then R to infinity; every surviving term vanishes.

For precision, stop when any actual primal norm exceeds a fixed bound
larger by one than the uniformly bounded reference norms on [0,S].
Before this node all actual raw velocities have width-independent
bounds: bounded activations and gates, bounded readout norm, and the
two bounded operator norms control the residuals and all backward
norms. The step into the first bad node has overshoot at most C eta_n,
so (II.C.8) holds through that endpoint. With probability tending to one
its state discrepancy is less than half the extra margin, contradicting
the stop. Finite GF uses the continuous version of this argument.
Finite GF in fact exists globally by the finite-dimensional loss-energy
identity and local smoothness, independently of this comparison.

Inside a GD step each raw vector changes by O(eta_n) in norm/sqrt(n)
and each matrix by O(eta_n) in operator norm. The recomputed forward
fields therefore change by O(eta_n) in that vector norm; their coordinate
supremum change is at most O(eta_n sqrt(n)).
This controls gate changes and shows recomputed hidden velocities differ
from their node formulas by O(eta_n sqrt(n))=O(n^-3/2), using the
product rule at layers 2 then 3. The same bound covers right-node and
terminal-left conventions. Thus (II.C.8) also holds for raw interpolation.

Comparing both actual GD and GF to this same reference proves their
same-width state-distance convergence. Combining with fixed-R joint
laws and cut removal proves full-sequence joint population convergence,
not merely convergence along a selected width subsequence.

#### II.C.5. Observation transfer

The state comparison controls finite Lipschitz probe programs in either
direction of either operator. The two explicit tail comparisons also
control both named uncut backward fields. A bounded continuous gate
times a strongly convergent L^2 factor converges strongly: truncate the
factor, use bounded convergence on the truncated part, and remove its
uniformly integrable squared tail. Repeat this argument through every
named backward or velocity probe. Same-neuron tuples include BOTH
samples and finitely many times; no cross-layer coordinate pairing is
introduced.

Predictions, loss, and all entries of all four 2-by-2 raw kernel blocks
then converge as continuous quadratic-growth measurements and products
of their scalar limits. The population feature-time velocity formulas are

    (Z^(1)_b)'=(1/2)sum_a G_ba y_a delta^(1)_a,
    (Z^(2)_b)'=(1/2)sum_a y_a delta^(2)_a
                                  E[H^(1)_a H^(1)_b]
                          +W^(2)[phi'(Z^(1)_b)(Z^(1)_b)'],
    (Z^(3)_b)'=(1/2)sum_a y_a delta^(3)_a
                                  E[H^(2)_a H^(2)_b]
                          +W^(3)[phi'(Z^(2)_b)(Z^(2)_b)'].

Physical velocities multiply these by the positive clock derivative.
Feature velocities add a factor phi' at their own layer. The preceding
strong/product argument and the raw interpolation estimate prove their
joint laws and integrated squared norms.

For scalar absolutely continuous paths, with I_pi the linear interpolant
on a mesh pi,

    ||z-I_pi z||_infinity^2
                            <=4|pi| integral_0^T |dot z|^2.

Apply this in empirical average and population expectation. Fixed-grid
joint W_2 convergence and the uniform integrated velocity bounds imply
W_2(C([0,T])) convergence by a triangle inequality and then mesh removal.
The same argument on two-component paths gives the joint two-sample
path law in each neuron population. Lipschitz phi transfers it to
feature paths.


#### II.C.6. Ordered observation closure and uniform velocity limits

Here are the truncation and time-uniform details for Section II.C.5.
They use only the finite-program scope proved in III.F.1--7, bounded
action norms, and elementary strong multiplier continuity. They do not
apply a bounded-derivative theorem directly to an unbounded product.

First fix a training cap and a finite Euler transcript. All primary
fields have their joint same-layer \(\mathcal W_2\) laws by II.B and
III.F. True backward observations are appended from the readout down,
and velocity observations are appended from the first layer up.
For an incoming field \(P\) whose joint law has already been obtained,
replace \(\phi'(Z)P\) by \(\phi'(Z)\tau_M(P)\). At fixed \(M\)
this is a \(C^1\) bounded-derivative coordinate instruction:
its partial derivatives are bounded by
\(2M\|\phi''\|_\infty\) and \(\|\phi'\|_\infty\).
Its error in \(L^2\), or finite RMS, is at most
\[
 2\|\phi'\|_\infty\,
       \|P\mathbf1_{\{|P|>M\}}\|_2
 \le4\|\phi'\|_\infty\|(|P|-M/2)_+\|_2.
 \tag{II.C.o1}
\]
The last norm is a 1-Lipschitz functional of the law in \(\mathcal W_2\).
Consequently its empirical value converges at fixed \(M\), and its
limiting value vanishes as \(M\to\infty\). A bounded action transfers
this input error to the output error. At each later product retain
all earlier observation caps, add the new outer cap, apply the fixed
finite theorem, remove earlier caps while that outer cap stays fixed,
then remove the outer cap. This is a finite induction along the actual
query graph. It proves joint laws for true backward fields and for all
three layers of the velocity recursion in II.C.5. It only identifies
values and second moments; no expected derivative of an untruncated
velocity observation is needed here.

For completeness the deterministic velocity comparison is explicit.
Take two states with common primal bounds, and two raw directions with
common norm bounds. Let \(\alpha\) be their state discrepancy in the
sum of first-field, operator and readout norms, and let \(\beta\)
be the corresponding direction discrepancy. Use \(P_\ell\) for a
preactivation velocity and \(U_\ell=\phi'(Z_\ell)P_\ell\) for its feature
velocity, with a bar denoting the reference state and direction.
At the bottom the \(P\)-difference is bounded by \(\beta\). At either
upper layer the identity
\[
 P_\ell=\dot W^{(\ell)}H^{(\ell-1)}
                         +W^{(\ell)}U_{\ell-1}
\]
gives a difference bounded by
\(C(\alpha+\beta+\|U_{\ell-1}-\bar U_{\ell-1}\|_2)\).
Truncate only the reference multiplier in the next gate:
\[
 \|U_\ell-\bar U_\ell\|_2
 \le\|\phi'\|_\infty\|P_\ell-\bar P_\ell\|_2
 +2M\|\phi''\|_\infty\|Z_\ell-\bar Z_\ell\|_2
 +4\|\phi'\|_\infty\|(|\bar P_\ell|-M)_+\|_2.
\]
The finite upward recursion therefore gives
\[
 \sum_{\ell,a}(\|P_{\ell,a}-\bar P_{\ell,a}\|_2+
                        \|U_{\ell,a}-\bar U_{\ell,a}\|_2)
 \le C\left[\beta+(1+M)\alpha+
             \sum_{\ell,a}\|(|\bar P_{\ell,a}|-M)_+\|_2\right].
 \tag{II.C.o2}
\]
The constant depends on the fixed primal/direction bounds and activation,
not on \(M\) or the training cap. Each new \(M\) multiplies a forward
state difference, not an earlier velocity error. The same inequality
holds for finite arrays with every vector norm divided by \(\sqrt n\).
A downward version proves the analogous comparison for true backward
fields. These comparisons require no \(L^p\) bound for a population
operator with \(p>2\).

Along a strong population flow, the hidden velocities are continuous
in \(L^2\). Indeed bounded continuous multipliers preserve strong
convergence after truncating one fixed \(L^2\) factor; differentiating
the forward action uses its actual bounded adjoint and product rule.
A compact \(L^2\) curve has uniformly vanishing positive-part tails:
cover it by finitely many small \(L^2\) balls and use the 1-Lipschitz
tail functional at their centers.

At a fixed training cap, raw Euler states and directions converge
uniformly to the cap flow, by II.C.1. Apply (II.C.o2) with the
population flow as reference, first refining the mesh at fixed \(M\)
and then removing \(M\). Thus the population Euler velocity tuples
converge uniformly in \(L^2\), and inherit uniform tail removal.
At fixed mesh their finite counterparts and tails converge by the
just-proved finite observational induction. Compare finite capped GF
or fine raw GD to that same-width coarse Euler reference, using the
fixed-cap state/direction estimate, and then apply (II.C.o2).
The order is width, mesh refinement at fixed \(M\), then \(M\to\infty\).
The triangle inequality with the finitely many coarse-node laws proves
uniform-time joint \(\mathcal W_2\) convergence of fields and velocities
at each fixed training cap. Taking finite unions gives joint-time laws.

Finally the feature cap states and directions converge strongly and
uniformly by II.C.2. After the fixed population clock change, apply
(II.C.o2) with the uncut population flow as reference. Its velocity
curve is compact in \(L^2\), so population cap velocities converge
uniformly and inherit its uniformly removable tails. For actual finite
physical GF/GD, II.C.4 and the asymmetric field estimate control both
states and actual raw directions against the finite capped reference.
Apply (II.C.o2) again with that reference, in the order: width at
fixed training cap and \(M\); training cap to infinity at fixed \(M\);
then \(M\to\infty\). The reference tails pass through its fixed-cap
uniform laws to the already controlled population tails. This proves
the claimed uniform-time velocity laws and squared norms without
multiplying a possibly growing cap-dependent moment constant by a
cap-removal error.

For GD these are the recomputed hidden derivatives at the interpolated
state with the preceding-node raw direction. The raw step displacement
vanishes and the fixed-cap reference has a continuous time modulus,
so the same proof covers the stated right/terminal-left conventions.
Uniform squared-norm convergence gives integrated energies. The path
interpolation inequality in II.C.5 gives the stated \(\mathcal W_2\)
path laws for preactivations and features.

For operator increments, the inner product of two rank-one terms is
\(\langle U,\widetilde U\rangle\langle V,\widetilde V\rangle\).
Their integrands are continuous in Hilbert--Schmidt norm, and all these
cross-time within-layer contractions have just been proved to converge.
Finite Riemann sums followed by time refinement give the squared norms
of increments and their cross-time contractions. The first-row reconstruction
(II.C.r1)--(II.C.r2) and the readout integral give the other parameter
increments. These are scalar observations, not a pairing of operators
at different widths.



### II.D. Persistent nonaffinity and all-layer motion

We take both labels +1; simultaneous label/readout sign reversal covers
both labels -1. All times in the first four sections are feature times
s in [0,S], S=3/2. Set epsilon=1/10, c_-=5/6, a=7/6, A=3/2.
The root pair is centered Gaussian with covariance G, rho in [-1,1).
All Gaussian assertions about later fields refer to the explicit source
laws of the cut Euler programs, not to iid trained neuron coordinates.

#### II.D.1. Forward pair separation survives the constructed interval

The response bootstrap gives |A^(ell)_(ka,rb)|<=A Delta/2,
both reverse coefficient row sums <=1, and each q^(j)_(ka) is its
Gaussian source plus a correction of absolute value <=a.
The bottom source standard deviations are <=Q_*/10, with
Q_*=24829/19200<27/20; the middle ones are <=7/40.

For the raw first-layer update, independently of the root pair,

    |Z^(1)_(ka)-G_a| <= R_(1,k),
    R_(1,k)=(epsilon Delta/2)sum_(r<k,b)(|zeta^(1)_(rb)|+a).

Consequently
E R_(1,k)<=epsilon S(Q_*/10+a)<1/5.
The event R_(1,k)<=1 has probability at least 4/5 and is independent
of (G_1,G_2). Since rho<1,

    p_1(rho)=P(G_1>=2,G_2<=-2)>0.

For -1<rho<1 this follows from the positive bivariate Gaussian density;
at rho=-1 it is P(G_1>=2)>0. Intersecting the independent events yields

    P(Z^(1)_(k1)>=1,Z^(1)_(k2)<=-1)>=(4/5)p_1(rho).

On this event H^(1)_(k1)-H^(1)_(k2)>=epsilon*pi/2.
Thus there is an explicit d_1(rho)>0, uniform in caps/mesh/time, with

    E(H^(1)_(k1)-H^(1)_(k2))^2>=d_1(rho).                 (II.D.1)

The finite Euler scheme is invariant in law under sample exchange and
has deterministic limiting same-neuron laws. Its two feature second
moments are therefore equal. The two eigenvalues of the first feature
second-moment matrix are

    (1/2)E(H^(1)_(k1)+H^(1)_(k2))^2 >=2c_-^2,
    (1/2)E(H^(1)_(k1)-H^(1)_(k2))^2 >=d_1(rho)/2.

This matrix is uniformly positive definite for each fixed rho.
The same exchange assertion holds at every layer and later survives
the strong cut/mesh limits.

For the middle preactivations,

    |Z^(2)_(ka)-xi^(2)_(ka)|<=R_(2,k),
    R_(2,k)=(A epsilon Delta/2)
                              sum_(r<k,b)(|zeta^(2)_(rb)|+a).

Its expectation is at most
A epsilon S(7/40+a)=483/1600<1/3. Its source group is independent
of the entire xi^(2) group. Therefore P(R_(2,k)<=1)>=2/3.
The covariance eigenvalues of the pair xi^(2) lie between
c_1=min(2c_-^2,d_1/2)>0 and 2a^2. Its density on the rectangle
[2,3] times [-3,-2] has a positive lower bound depending only on rho.
Indeed the density is at least

    (4*pi*a^2)^(-1) exp(-||x||^2/(2c_1))

there, by the eigenvalue bounds. The independent dominator event
therefore supplies a uniform positive probability that
Z^(2)_(k1)>=1 and Z^(2)_(k2)<=-1.
It follows as above that its feature difference has a uniformly
positive squared norm d_2(rho), and that the second feature
second-moment matrix has eigenvalues bounded below by
c_2=min(2c_-^2,d_2/2)>0.

At the top, |W^(4)_r|<=aS and the top gate is at most epsilon, so

    |Z^(3)_(ka)-xi^(3)_(ka)|
                         <=A a epsilon S^2=63/160=:B_0<2/5.     (II.D.2)

The top Gaussian pair covariance has eigenvalues between c_2 and
2a^2. Its probability on [2,3] times [-3,-2] has a uniform positive
lower bound, without any independence requirement for the bounded
correction (II.D.2). Thus the same opposite-sign feature-separation event
is positive at the top too.

All these are statements about actual cut Euler laws. They pass first
to fixed-cap flows and then to the uncut flow: joint fields converge
strongly in L^2, and the probabilities of the closed rectangles in
question are at least the limsup of the approximating probabilities.
The feature moments converge as well. No joint almost-sure
realization of all Gaussian source processes is required.

#### II.D.2. Every marginal remains genuinely nonlinear

At the bottom, R_1<=1 and G_a>=u+1 (or G_a<=-u-1) give uniform
positive lower tails for Z^(1)_a, for every fixed u>0.
At the middle use R_2<=1, independent of its forward source, and
the marginal Gaussian variance at least c_-^2.
At the top use the bounded correction (II.D.2) and the same variance
lower bound. Thus every marginal preactivation has both unbounded
tails at every reached time. The bounds are uniform over the
constructed feature interval, for fixed tail level u.

For each such square-integrable Z, its variance is positive and

    inf_(alpha,beta) E[(phi(Z)-alpha Z-beta)^2]
       =Var(phi(Z))-Cov(Z,phi(Z))^2/Var(Z) >0.              (II.D.3)

The quadratic minimizer exists. Equality would imply an affine identity
almost surely. Because phi is bounded and Z has unbounded support,
its slope would be zero. Strict monotonicity of phi would then force
Z constant, contrary to its tails.
All moments in (II.D.3) vary continuously along the L^2 state path.
Their positive values have positive minima on compact time intervals.
The already established empirical second-moment convergence transfers
a smaller positive bound to the finite empirical affine errors, uniformly
in time with probability tending to one. The fixed nonlinearity is never
sent to zero as width, time mesh or input angle changes.

#### II.D.3. Backward pair covariance is positive at every positive time

The same-label readout obeys W^(4)(s)>=c_-s pointwise. Fix s_0>0 and
consider cut Euler indices with k Delta>=s_0. Then
delta^(3)_(ka)=W^(4)_k epsilon/(1+(Z^(3)_(ka))^2)>0.

For the top source pair use the rectangle [4,5] times [-1/10,1/10].
Its probability has a positive lower bound p(rho)>0 from the covariance
eigenvalue bounds above. On it, (II.D.2) implies

    |Z^(3)_(k1)|>=18/5,     |Z^(3)_(k2)|<=1/2,
    delta^(3)_(k1)/delta^(3)_(k2)
                        <=(5/4)/(1+(18/5)^2)<1/4,
    delta^(3)_(k2)>= (4/5)c_- s_0 epsilon=:b_0>0.

On the swapped rectangle the two roles are interchanged.
For any unit vector v=(v_1,v_2), choose the rectangle on which
the coordinate associated to max(|v_1|,|v_2|) is the large delta.
Then

    |v_1 delta^(3)_(k1)+v_2 delta^(3)_(k2)|
                         >=(3/4)b_0 max(|v_1|,|v_2|)
                         >=3b_0/(4 sqrt(2)).

Therefore the second-moment matrix of the two top deltas has smallest
eigenvalue at least 9p(rho)b_0^2/32>0. This estimate passes through
the cut/mesh limits by their converging second moments. In particular
that matrix is positive definite at every fixed s>0.

At such a fixed time, choose approximating cut Euler laws with times
approaching s. Their middle reverse source covariance converges to the
positive-definite top-delta second-moment matrix. Each q^(2)_a differs
from its source by at most a. Every signed rectangle

    sign_1 zeta^(2)_1 in [a+1,a+2],
    sign_2 zeta^(2)_2 in [a+1,a+2]

has probability bounded below along sufficiently late approximations,
for each of the four independent choices sign_1,sign_2 in {-1,1}.
Hence each corresponding closed quadrant
sign_1 q^(2)_1>=1, sign_2 q^(2)_2>=1 has positive limiting probability.
Since phi'(Z^(2)_a)>0 almost surely, delta^(2)_a has the same nonzero
sign as q^(2)_a on these quadrants.

No nonzero constant linear combination of the two middle deltas can
vanish almost surely: choose the quadrant aligned with the signs of
its nonzero coefficients. Its combination is then strictly positive.
Thus their second-moment matrix is positive definite.
Apply the same argument to the bottom reverse source, whose covariance
is precisely this matrix and whose response correction is bounded by a.
It proves positive definiteness of the two bottom-delta second moments.

This reasoning uses converging joint empirical laws of reused outputs
and actual covariance identities; it does not replace trained fields
by independent Gaussian neurons.

#### II.D.4. No hidden layer freezes at a positive time

Let K_g^(ell) be the squared raw metric norm of the layer-ell block
of grad g, where g=(f_1+f_2)/2. From the exact kernel formulas,

    K_g^(1)=(1/4)sum_(a,b) G_ab E[delta^(1)_a delta^(1)_b],
    K_g^(ell)=(1/4)sum_(a,b) E[delta^(ell)_a delta^(ell)_b]
                                        E[H^(ell-1)_a H^(ell-1)_b],
                                                   ell=2,3.

Each is strictly positive at s>0. In the first formula the delta
matrix is positive definite and G is positive semidefinite with
trace two, even at rho=-1. Their trace product is at least twice
the delta matrix's smallest eigenvalue. For the other two formulas
the feature Gram matrix is positive semidefinite with positive trace
and the delta matrix is positive definite, giving the same conclusion.

Adjunction and the differentiated forward equations give, for j=1,2,3,

    (1/2)sum_a E[delta^(j)_a (Z^(j)_a)']
                                     =sum_(ell<=j)K_g^(ell)>0.   (II.D.4)

For j=1 this is the first-layer gradient pairing through G.
At j=2 the trained matrix term contributes K_g^(2), and the propagated
lower derivative contributes the j=1 identity. At j=3 the identical
calculation contributes K_g^(3) and the j=2 identity.
Therefore at least one sample's preactivation velocity is nonzero
at each layer. The deterministic joint laws are sample-exchange
symmetric, including their derivative probes, so the two sample
velocity norms are equal. BOTH are nonzero.
The strictly positive gate preserves nonzero L^2 norm of every feature
velocity. The physical clock derivative 4(1-g)>0 at every finite
physical time preserves these conclusions there.

#### II.D.5. Initial nonlazy scale and nonconstant kernel

Write alpha for the three hidden parameter blocks in their raw Hilbert
metric and V(alpha)=(H^(3)_1+H^(3)_2)/2. Then g=E[W^(4)V(alpha)].
Let D_0 be the bounded linearized forward map from hidden variations
to V at initialization, and let B=D_0^*V_0. Its component in each
hidden block is nonzero, as follows without assuming later existence:


At initialization write \(D_a^\ell=\phi'(Z_a^{(\ell)}(0))\),
\(V_0=(H_1^{(3)}(0)+H_2^{(3)}(0))/2\), and
\(\beta_a^3=V_0D_a^3\). The top preactivation pair is nondegenerate
Gaussian by II.D.1, and \(V_0\ge c_-\). The gate-ratio rectangles
of II.D.3, without the training correction, show
\((\mathbb E_3[\beta_a^3\beta_b^3])_{ab}\succ0\).

For clarity, the initialized two-transpose closure is
\[
 \begin{split}
 q_a^2&=\zeta_a^2+\sum_b R^2_{ab}H_b^{(2)}(0),&
 \beta_a^2&=D_a^2q_a^2,\\
 q_a^1&=\zeta_a^1+\sum_b R^1_{ab}H_b^{(1)}(0),&
 \beta_a^1&=D_a^1q_a^1,
 \end{split}
 \tag{II.D.i1}
\]
with
\[
 \begin{split}
 R^2_{ab}
  &=\mathbb E_3\!\left[\tfrac12D_a^3D_b^3+
           \mathbf1_{a=b}V_0\phi''(Z_a^{(3)}(0))\right],\\
 R^1_{ab}
  &=\mathbb E_2\!\left[\mathbf1_{a=b}\phi''(Z_a^{(2)}(0))q_a^2+
                              D_a^2R^2_{ab}D_b^2\right].
 \end{split}
 \tag{II.D.i2}
\]
Here the two reverse source groups are independent of each other and
of the forward groups and bottom roots, and
\[
 \mathbb E[\zeta_a^2\zeta_b^2]=\mathbb E_3[\beta_a^3\beta_b^3],
 \qquad
 \mathbb E[\zeta_a^1\zeta_b^1]=\mathbb E_2[\beta_a^2\beta_b^2].
 \tag{II.D.i3}
\]
These are full input second moments, not response-subtracted variances.

To derive these identities in the proved Gaussian-program class, perform
the ordinary three-layer initialization forward transcript first, then
the two top reverse calls. The coordinate map
\(V_0\phi'(Z_a^{(3)})\) has bounded first derivatives, since
\(\phi,\phi',\phi''\) are bounded. The source rule III.F.4 gives the
first line of (II.D.i1) and the first row of (II.D.i2).
Its \(q^2\) is Gaussian plus a bounded correction, hence belongs
to every finite \(L^p\).

For the next reverse input use \(D_a^2\tau_M(q_a^2)\).
Its derivative in the named current forward source \(Z_b^{(2)}(0)\)
is exactly
\[
 \mathbf1_{a=b}\phi''(Z_a^{(2)}(0))\tau_M(q_a^2)
   +D_a^2\tau_M'(q_a^2)R^2_{ab}D_b^2.
\]
It is dominated, uniformly in \(M\), by a constant times \(1+|q_a^2|\).
Apply III.F at fixed \(M\), then dominated convergence identifies the
second row of (II.D.i2). Strong \(L^2\) convergence of the inputs
identifies their covariance limits; coupling Gaussian vectors by
covariance square roots and bounded action continuity identifies
the actual uncut transpose answer. At finite width the input clip
error vanishes in the width-then-\(M\) order by (II.C.o1) and its
already established joint \(\mathcal W_2\) law. Thus the assertions
are empirical joint limits and canonical action identities, not
only a formal tagged-coordinate calculation. No derivative-valid
extension for an arbitrary unbounded product has been assumed.

Each response in (II.D.i1) is bounded because the two features are
bounded and its coefficients are finite. The nondegenerate
\(\zeta^2\) therefore gives positive probability to each signed
quadrant beyond that bounded shift. Multiplication by \(D_a^2>0\)
preserves signs, so no nonzero fixed linear combination of
\(\beta_1^2,\beta_2^2\) can vanish almost surely. Its second-moment
matrix is positive definite. Repeat with \(\zeta^1\) and \(D_a^1\).
The trace-product argument in II.D.4 then proves every hidden block
of \(B=D_0^*V_0\) is nonzero, including \(\rho=-1\).


Let Gamma_ell=||B_ell||^2>0, and Gamma=sum_(ell=1,2,3)Gamma_ell.
The curve chain rule and continuity of bounded-gate products yield

    W^(4)(s)/s -> V_0,
    alpha'(s)/s -> B,
    alpha(s)-alpha(0)=(s^2/2)B+o(s^2).

Here only convergence of the bounded linearized forward/adjoint maps
on the displayed strongly converging directions is needed, not
operator-norm differentiability of an L^2 Nemytskii map.
It follows that V'(s)=s D_0 B+o(s), and
E[V_0 D_0 B]=||B||^2=Gamma. Consequently

    K_g^(4)(s)=E[V(s)^2]=E[V_0^2]+Gamma s^2+o(s^2),
    sum_(ell=1,2,3)K_g^(ell)(s)=Gamma s^2+o(s^2),
    sum_(ell=1,2,3,4)K_g^(ell)(s)
                               =E[V_0^2]+2Gamma s^2+o(s^2).      (II.D.5)

The total two-by-two kernel therefore cannot be constant: its fixed
same-label quadratic form (II.D.5) changes.

Differentiating the forward equations also gives, in each sample/layer,
(Z^(ell)_a)'(s)=s T^(ell)_a+o(s).
Dividing identity (II.D.4) by s^2 and taking s down to zero shows the
appropriate initial-backward pairing with T^(ell) equals the sum
of the positive Gamma_j for j<=ell. Thus these leading velocities
are nonzero; symmetry makes both sample norms equal.
Integrating and using positive gates gives

    H^(ell)_a(s)-H^(ell)_(a,0)
         =(s^2/2)phi'(Z^(ell)_(a,0))T^(ell)_a+o(s^2).

Since s(t)=4t+o(t), the leading physical feature change is
8t^2 phi'(Z^(ell)_(a,0))T^(ell)_a, with a nonzero fixed L^2 coefficient.
The output-mode kernel change is 16Gamma t^2+o(t^2), and total-mode
kernel change is 32Gamma t^2+o(t^2).
No activation or motion coefficient is sent to zero with width.

The field and kernel convergence already established in Section II.C
transfers these nonzero fixed-time feature changes and kernel changes
to the finite model on each fixed observation horizon.



---

## III. Three samples and bounded-shape activations at every fixed depth

This part includes the full global construction, finite-algorithm and
observation bridge, initial-motion proof and activation-class refinements.
In its equations a bare layer superscript \(\ell\) on a field means the
same layer index as \((\ell)\) in the shared notation.
Only hidden fields are normalized for estimates. Weights, metric,
readout and training step are never normalized away.



### III.M. Model, quantifiers and theorem

All spaces are real. Fix \(0<\delta<1\), a dimension \(d\ge1\),
three inputs \(x_i\in\mathbb R^d\), and three labels \(y_i\in\{-1,1\}\).
Write \(u_i=x_i/\sqrt d\) and assume
\[
 \|u_i\|=1,\qquad G_{ij}=u_i^Tu_j\le1-\delta
       \quad(i\ne j).                                      \tag{III.M.1}
\]
In particular the theorem applies when
\(-1+\delta<G_{ij}<1-\delta\). The weaker one-sided assumption
(III.M.1) is sufficient, and singular input Gram matrices are allowed.
The number of samples is three throughout; depth is the quantity
being generalized.

Choose a nonconstant function \(\psi\in C^2(\mathbb R)\) with
\[
 \max\{\|\psi\|_\infty,\|\psi'\|_\infty,\|\psi''\|_\infty\}\le1.
                                                               \tag{III.M.2}
\]
Any bounded nonconstant \(C^2\) function with bounded first and
second derivatives can be normalized this way by a scalar factor.
The following finite selection depends only on \(\delta,\psi\).
Choose an integer \(r_\psi\ge1\) with
\[
 J_\psi=\inf_{b,c\in\mathbb R}\int_{-r_\psi}^{r_\psi}
                  [\psi(x)-b-cx]^2\,dx>0,\qquad
 c_\psi=\frac{e^{-r_\psi^2/2}}{\sqrt{2\pi}}J_\psi>0.        \tag{III.M.3}
\]
Part III.G proves that such an integer exists. Set
\[
 \lambda=\delta^2/16,\qquad T_0=12/\lambda,\qquad
 a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{c_\psi}}\right)^{2/5}\right\}.
                                                               \tag{III.M.4}
\]
For any one fixed \(e\in(0,1]\), including \(e=1\), use
\[
                     \phi(z)=a(1+z)+e\psi(z).              \tag{III.M.5}
\]
Neither \(a\) nor \(e\) depends on the hidden depth, width, time,
dimension, labels or particular admissible input configuration.
The constants are sufficient bounds, with no claim of sharpness.

#### III.M.1. Exact finite algorithms and their metric

For each separately fixed finite integer \(L\ge2\), a width \(n\)
network has raw parameters \(V^{(1)}\in\mathbb R^{n\times d}\),
\(W^{(\ell)}\in\mathbb R^{n\times n}\) for \(2\le\ell\le L\), and
\(W^{(L+1)}\in\mathbb R^n\). All initial entries are mutually independent,
with
\[
 V^{(1)}_{jk}(0)\sim N(0,1/d),\qquad
 W^{(\ell)}_{jk}(0)\sim N(0,1/n),\qquad
 W^{(L+1)}_j(0)\sim N(0,n^{-2}).                                  \tag{III.M.6}
\]
Use \(\frac{1}{n}\langle v,q\rangle_{\mathbb R^n}=n^{-1}v^Tq\). The physical fields are
\[
 z_i^1=V^{(1)}x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
 z_i^\ell=W^{(\ell)} h_i^{\ell-1}\ (\ell\ge2),\quad
 f_i=\frac{1}{n}\langle W^{(L+1)},h_i^L\rangle_{\mathbb R^n},\quad r_i=f_i-y_i,
 \quad\mathcal L=\tfrac12\sum_i r_i^2.                    \tag{III.M.7}
\]
Coordinate nonlinearities and products occur within one layer.
The true residual-free backward fields are
\[
 \delta_i^L=\phi'(z_i^L)W^{(L+1)},\qquad
 \delta_i^\ell=\phi'(z_i^\ell)(W^{(\ell+1)})^T\delta_i^{\ell+1}.
                                                               \tag{III.M.8}
\]
The original raw metric and its exact gradient flow are
\[
 \|\Delta\theta\|_{{\rm raw},n}^2
 =\frac dn\|\Delta V^{(1)}\|_F^2+
    \sum_{\ell=2}^L\|\Delta W^{(\ell)}\|_F^2+\frac{\|\Delta W^{(L+1)}\|_2^2}{n},
                                                               \tag{III.M.9}
\]
\[
 \dot V^{(1)}=-d^{-1}\sum_i r_i \delta_i^1x_i^T,\qquad
 \dot W^{(\ell)}=-n^{-1}\sum_i r_i \delta_i^\ell(h_i^{\ell-1})^T,
 \qquad\dot W^{(L+1)}=-\sum_i r_i h_i^L.                          \tag{III.M.10}
\]
Indeed the Euclidean first derivative has factor \(1/n\), which
the inverse metric multiplies by \(n/d\); the matrix derivatives
retain \(1/n\); the readout inverse metric cancels its factor
\(1/n\). Thus all updates have the indicated factors.

Raw GD is simultaneous explicit Euler for exactly (III.M.10), with
physical step \(\eta_n=n^{-2}\). Its raw parameters are linearly
interpolated at times \(k\eta_n\). At intermediate times hidden
fields are recomputed from these parameters by (III.M.7). Their
velocities are the derivatives of these recomputed fields, with
the right derivative at nodes and the left derivative at the
final endpoint of an observation interval. GF and GD use the
same actual random initialization (III.M.6). No coupling across
different widths is required.

Finite GF exists globally: its locally Lipschitz field satisfies
\(\int_0^T\|\dot\theta\|_{{\rm raw},n}^2\le\mathcal L(0)\).
Cauchy--Schwarz bounds displacement by
\(\sqrt{T\mathcal L(0)}\), makes a finite endpoint Cauchy and
allows local continuation there. GD is defined at every finite
step because all its functions are everywhere defined.

#### III.M.2. Population state and an exact normalization for the proof

Part III.F constructs one neuron probability space \(\Omega_\ell\)
per hidden layer, with \(\mathcal H_\ell=L^2(\Omega_\ell)\), and initialized
actions \(W^{(\ell)}_0:\mathcal H_{\ell-1}\to \mathcal H_\ell\) of norm at most 10
for \(2\le\ell\le L\), with their genuine adjoints. These are the
canonical joint limits of the finite Gaussian calculations,
including reuse of transposes. Arbitrary bounded actions are
not substitute initializations.

It is convenient to write \(w=\sqrt d V^{(1)}\). This is an isometry
of the first raw block, not a change of training metric. The
population initialization is \(w_0\sim N(0,I_d)\), \(W^{(L+1)}_0=0\), and
the affine state space is
\[
 \mathcal P=L^2(\Omega_1;\mathbb R^d)\times
  \prod_{\ell=2}^L(W^{(\ell)}_0+\mathcal S_2(\mathcal H_{\ell-1},\mathcal H_\ell))
                         \times \mathcal H_L,\qquad
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\sum_{\ell=2}^L\|\Delta W^{(\ell)}\|_{\rm HS}^2
                                           +\|\Delta W^{(L+1)}\|_2^2.
                                                               \tag{III.M.11}
\]
Only learned increments are Hilbert--Schmidt. The original first
weight field is \(V^{(1)}=w/\sqrt d\). In population (III.M.7)--(III.M.10)
replace normalized finite inner products by the appropriate
layer expectations, matrices by their actions and transposes by
their adjoints. In particular \(Z_i^1=w\cdot u_i\) and
\(\dot w=-\sum_i r_i \delta_i^1u_i\).

For proof estimates normalize only hidden fields:
\[
 K_\ell=a^{\ell-1},\quad Y_i^\ell=Z_i^\ell/K_\ell,\quad
 X_i^\ell=H_i^\ell/a^\ell,\quad
 \chi_\ell(v)=v+\frac{1+(e/a)\psi(K_\ell v)}{K_\ell}.
                                                               \tag{III.M.12}
\]
Then \(Y_i^1=w\cdot u_i\), \(Y_i^\ell=W^{(\ell)} X_i^{\ell-1}\),
\(X_i^\ell=\chi_\ell(Y_i^\ell)\), and
\(F_i=\langle W^{(L+1)},X_i^L\rangle\) satisfies \(f_i=a^LF_i\).
No readout rescaling occurs. Therefore
\(\nabla_{\rm raw}f_i=a^L\nabla_{\rm raw}F_i\) in every block.
Part III.F proves this identity as a scalar Fréchet derivative.
The normalized backward variables are
\[
 q_i^L=W^{(L+1)},\quad d_i^\ell=\chi_\ell'(Y_i^\ell)q_i^\ell,
 \quad q_i^\ell=(W^{(\ell+1)})^*d_i^{\ell+1}\quad(\ell<L).
                                                               \tag{III.M.13}
\]
The true raw backward fields obey
\(\delta_i^\ell=a^{L-\ell+1}d_i^\ell\). All scalings are fixed
deterministic constants when taking width or time limits.

For \(v\in \mathcal H_\ell,h\in \mathcal H_{\ell-1}\),
\((v\otimes h)q=v\langle h,q\rangle\), of Hilbert--Schmidt norm
\(\|v\|\|h\|\). Its finite matrix is \(vh^T/n\).
A strong solution is a strong \(C^1\) path in (III.M.11).
Bounded primal quantities on compact intervals means bounded
\(\|w\|_2,\|W^{(\ell)}\|_{\rm op},\|W^{(L+1)}\|_2\) there. Constants for
activation selection use only the three initial projections,
each of norm one, and raw displacements. They never require a
dimension independent bound on \(\|w_0\|_2=\sqrt d\).

#### III.M.3. Observations and the full theorem

The \(L+1\) true raw kernel blocks are
\[
 K^1_{ij}=G_{ij}\langle \delta_i^1,\delta_j^1\rangle_1,\qquad
 K^\ell_{ij}=\langle \delta_i^\ell,\delta_j^\ell\rangle_\ell
             \langle H_i^{\ell-1},H_j^{\ell-1}\rangle_{\ell-1}
       \ (2\le\ell\le L),\qquad
 K^{L+1}_{ij}=\langle H_i^L,H_j^L\rangle_L.                \tag{III.M.14}
\]
Their sum is the Gram of the raw predictor gradients. Auxiliary
capped update fields used in the proof do not replace these true
kernel observations.

Let \(\mathcal Z^\ell=(Z_1^\ell,H_1^\ell,Z_2^\ell,H_2^\ell,
Z_3^\ell,H_3^\ell)\) and
\(\mathcal U^\ell=(\mathcal Z^\ell,\dot{\mathcal Z}^\ell)\).
An empirical law averages the Dirac masses over neuron rows.
For whole paths use \(C([0,T];\mathbb R^6)\) with the supremum
Euclidean norm. For a normed space \(E\),
\(\mathcal W_2(\mu,\nu)^2\) is the infimum of
\(\int\|v-q\|_E^2\,d\pi\) over couplings of the two laws.
All laws below have the required finite second moments.

An additional generated probe is any fixed finite layer-typed
expression in root coordinates, constants, fields at finitely
many times, deterministic linear combinations, \(C^1\) coordinate
maps with bounded first derivatives, same-layer inner products,
and initialized or current actions and their adjoints. Its
instruction count is fixed before width tends to infinity.
Unbounded true backward and velocity products are separately
covered by Part III.V's ordered truncation arguments.

**Theorem III.M.1 (one activation at all finite depths).** With (III.M.1)--(III.M.6),
the same constants (III.M.4) and any one \(e\in(0,1]\) have the following
properties for every separately fixed finite \(L\ge2\).

1. There is a global autonomous strong population raw gradient
   flow. On its canonical action spaces it is unique among
   strong solutions with bounded primal quantities on compact
   intervals. Continuation from every reached state is unique
   in that class. For all physical \(t\ge0\),
   \[
    \|r(t)\|_2\le\sqrt3\,e^{-\lambda a^{2L}t/2},\qquad
    \mathcal L(t)\le\tfrac32e^{-\lambda a^{2L}t},\qquad
    (\langle X_i^L(t),X_j^L(t)\rangle)_{ij}
                                      \succeq3\lambda I_3/4.
                                                               \tag{III.M.15}
   \]
2. For each finite physical \(T\), actual finite GF and actual
   raw GD with step \(n^{-2}\) converge jointly in probability,
   along the full width sequence, to that same population flow.
   Predictions, loss and every true raw kernel entry converge
   uniformly on \([0,T]\). At each layer the empirical full path
   law of \(\mathcal Z^\ell\) converges in \(\mathcal W_2\) for
   the supremum path norm, and
   \[
    \sup_{t\le T}\mathcal W_2\big(
       \widehat{\operatorname{Law}}_n(\mathcal U_n^\ell(t)),
       \operatorname{Law}(\mathcal U^\ell(t))\big)\longrightarrow0.
                                                               \tag{III.M.16}
   \]
   Joint same-layer field and velocity laws at any fixed finite
   list of times also converge in \(\mathcal W_2\). Their second
   moments, integrated squared preactivation and feature speeds,
   and every fixed finite same-layer tuple of generated probes
   converge to their population values or laws as appropriate.
3. For every sample, layer and time,
   \[
    \inf_{b,c\in\mathbb R}E_\ell[(
       \phi(Z_i^\ell(t))-b-cZ_i^\ell(t))^2]
                      \ge\frac{e^2c_\psi}{16a^{L-1}}>0.
                                                               \tag{III.M.17}
   \]
   Every hidden raw parameter block and every sample's hidden
   preactivation and feature at every layer have nonzero strong
   right second derivative at zero. With \(p=y/3\) and
   \(\kappa(t)=p^T(\sum_{\ell=1}^{L+1}K^\ell(t))p\),
   \[
    \kappa(t)=\kappa(0)+18t^2\|\mathscr V\|_{\rm hidden}^2+o(t^2),
                 \qquad \|\mathscr V\|_{\rm hidden}>0,             \tag{III.M.18}
   \]
   where Part III.N defines and proves positivity of every block of \(\mathscr V\).

The activation pair and normalized Gram floor are uniform in \(L\).
The width-convergence constants and width required for a specified
accuracy may depend on \(L,d,a,e,\psi,T\) and the fixed data.
There is no assertion for a joint limit \(L=L(n)\to\infty\), or
an interchange of infinite time and infinite width. The margin
in (III.M.17) may decrease with depth; Part III.A proves that this is
necessary for some allowed functions and gives infinite-dimensional
subclasses with a positive margin uniform in depth as well.

The proof is internal: Part III.F constructs the Gaussian laws and
actions, Part III.S supplies uniform source moments and response
derivatives, Part III.G gives depth-uniform geometry and the bounded
total control clock, Part III.V constructs the uncut population path
and all finite algorithm and observation limits, and Part III.N proves
the initial motion. No external specialized theorem is a premise.

### III.F. Fixed finite Gaussian programs, common actions and strong differentiation

This part treats every fixed finite hidden depth L. All instruction lists and the number of initialized matrices are fixed before width tends to infinity. Its elementary proofs do not assert uniformity for a depth or transcript length growing with width.

#### III.F.1. Finite programs and convergence of their empirical laws

There are \(L\) types of length-\(n\) vectors, one for each hidden layer. Operations combining coordinates may combine only vectors of the same type. For each \(2\le\ell\le L\), let
\[
 W^{(\ell)}_n:\mathbb R^n_{\ell-1}\longrightarrow\mathbb R^n_\ell
\]
be mutually independent matrices with independent \(N(0,1/n)\) entries.
Their transposes are reused as the reverse actions of these same matrices.

Each layer may have a fixed finite tuple of root vectors. Its coordinate tuples are independent and identically distributed, have finite second moment, and are independent of all matrices. Tuples in different layers are independent. Constants are also allowed. In the network application, the first-layer root is a Gaussian vector \(w_0\in\mathbb R^d\) with covariance \(I_d\); the three root preactivations are \(u_i^T w_0\). Here \(w_0=\sqrt d V^{(1)}(0)\) in the isometric bottom coordinates of Part III.M. Additional independent Gaussian roots may be added to any layer when a proof requires probes or regularization.

A deterministic-coefficient program is a fixed finite ordered list of instructions of the following forms:

1. apply a fixed \(C^1\) function \(F:\mathbb R^m\to\mathbb R\) with bounded first partial derivatives, coordinate by coordinate, to previously available vectors of one layer;
2. multiply a previously available vector by \(W^{(\ell)}_n\) or \(W^{(\ell)}_n^T\) for any \(2\le\ell\le L\), with the appropriate types;
3. form a fixed real linear combination of previous same-layer vectors.

The first condition implies a global Lipschitz bound and at most linear growth for each coordinate instruction. The bound may depend on that instruction. Root tuples themselves need not be generated by such functions.

Write
\[
\frac{1}{n}\langle u,v\rangle_{\mathbb R^n}=\frac1n\sum_{\alpha=1}^n u_\alpha v_\alpha,
\qquad \frac{\|u\|_2^2}{n}=\frac{1}{n}\langle u,u\rangle_{\mathbb R^n}.
\]
For same-layer nodes \(v^1_n,\ldots,v^m_n\), their empirical law is
\[
\widehat\mu_n=\frac1n\sum_{\alpha=1}^n
 \delta_{(v^1_{n,\alpha},\ldots,v^m_{n,\alpha})}.
\]
Here \(\mathcal W_2\) uses the Euclidean distance on \(\mathbb R^m\).

**Theorem III.F.1 (fixed finite Gaussian program).** Every such program has deterministic joint limiting laws of all its same-layer node tuples, and
\[
\mathcal W_2(\widehat\mu_n,\mu)\longrightarrow0
\quad\hbox{in probability}
\tag{III.F.2}
\]
along the full width sequence. In particular every within-layer pairwise contraction converges to the corresponding limiting second moment. The scalar laws are given by the source rule in Section III.F.4. Query Grams may be singular. Finite collections of programs sharing the same matrices and roots converge jointly by applying the assertion to their finite union.

We prove this theorem in Sections III.F.2–III.F.5. The following elementary facts make explicit the probabilistic mode of convergence used in its proof.

If \(X_\alpha\) are iid and \(E|X_1|<\infty\), their averages converge in probability to their expectation: truncate \(X_\alpha\) at level \(M\), use the variance bound \(O(M^2/n)\) for the bounded variables, and bound the mean absolute truncation error by \(E[|X_1|1_{|X_1|>M}]\). First send \(n\) to infinity and then \(M\) to infinity. This proves the required initial weak convergence and second-moment convergence of root empirical laws.

For probability measures on a finite-dimensional Euclidean space, weak convergence together with convergence of second moments implies \(\mathcal W_2\) convergence. One direct proof is as follows. Continuous truncations of \(|x|^2\) show that the second moments outside sufficiently large balls are uniformly small. Inside a ball partition space into finitely many sets of diameter at most \(\eta\), choosing boundaries of zero limiting measure. Weak convergence makes their masses converge. Couple the common mass within each partition cell, at cost at most \(\eta^2\), and couple the remaining masses arbitrarily. The unmatched mass inside the ball vanishes; its cost is bounded by the squared diameter of the ball times that mass. The tails have arbitrarily small cost by \(|x-y|^2\le2|x|^2+2|y|^2\). Sending the ball radius and then the partition resolution to their limits proves the claim. A countable family of bounded Lipschitz tests determines weak convergence, by approximation on compact balls and tightness. For random measures the same argument applies in probability, or along an almost surely convergent subsubsequence of every subsequence.

Two arrays on the same neuron indices satisfy
\[
\mathcal W_2^2(\widehat\mu_n,\widehat\nu_n)
\le\frac1n\sum_\alpha |X_{n,\alpha}-Y_{n,\alpha}|^2,
\tag{III.F.3}
\]
using the coupling that pairs equal indices. These facts require no assertion that trained coordinates are independent.

#### III.F.2. An explicit Gaussian operator norm bound

**Lemma III.F.2.** For an \(n\times n\) matrix \(W_n\) with independent \(N(0,1/n)\) entries,
\[
\Pr(\|W_n\|_{\rm op}>10)
\le 2\,9^{2n}e^{-100n/8}\longrightarrow0.
\tag{III.F.4}
\]

**Proof.** A maximal \(1/4\)-separated subset \(\mathcal N\) of the Euclidean unit sphere is a \(1/4\)-net. Balls of radius \(1/8\) about its points are disjoint and lie in the ball of radius \(9/8\), so volume comparison gives \(|\mathcal N|\le9^n\). For unit \(u,v\), choose \(u_0,v_0\in\mathcal N\) within \(1/4\). Then
\[
|u^TW_nv-u_0^TW_nv_0|
\le\tfrac12\|W_n\|_{\rm op}.
\]
Taking the supremum gives \(\|W_n\|_{\rm op}\le2\max_{u_0,v_0\in\mathcal N}|u_0^TW_nv_0|\). For a fixed pair the displayed scalar is \(N(0,1/n)\). Its exponential moment is \(Ee^{t u_0^TW_nv_0}=e^{t^2/(2n)}\); Markov's inequality optimized at \(t=ns\) yields \(\Pr(|u_0^TW_nv_0|>s)\le2e^{-ns^2/2}\). A union bound at \(s=5\) proves (III.F.4). The exponent is negative since \(2\log9<12.5\). The same bound applies to transposes, and a finite union bound handles all matrices. ∎

The same argument for a threshold \(t\ge10\) gives
\[
\Pr(\|W_n\|_{\rm op}>t)
\le2\exp\{n(2\log9-t^2/8)\}
\le2e^{-nt^2/16}\le2e^{-t^2/16}.
\tag{III.F.4a}
\]
Consequently every fixed positive moment is bounded uniformly in width:
\[
\sup_{n\ge1}E\|W_n\|_{\rm op}^p
\le10^p+2p\int_{10}^\infty t^{p-1}e^{-t^2/16}\,dt<\infty.
\tag{III.F.4b}
\]
The integration formula follows by writing \(X^p=\int_0^Xpt^{p-1}dt\) for nonnegative \(X\) and interchanging nonnegative integrals. Hölder's inequality then gives uniform fixed-order moments for every fixed polynomial in finitely many such operator norms. For a standard Gaussian vector \(g_n\), Jensen's inequality also gives \(E\frac{\|g_n\|_2^p}{n^{p/2}}\le E|G|^p\) when \(p\ge2\).

A useful consequence identifies normalized traces without a concentration theorem for functions of matrix entries. Let \(T_n\) be any random real \(n\times n\) matrix independent of \(g_n\sim N(0,I_n)\), with \(\sup_nE\|T_n\|_{\rm op}^2<\infty\). Conditional on \(T_n\),
\[
E_g\frac{1}{n}\langle g_n,T_ng_n\rangle_{\mathbb R^n}=\frac1n\operatorname{tr}T_n,
\quad
\operatorname{Var}_g\!\left(\frac{1}{n}\langle g_n,T_ng_n\rangle_{\mathbb R^n}\right)
=\frac{2}{n^2}\left\|\frac{T_n+T_n^T}{2}\right\|_F^2
\le\frac{2}{n}\|T_n\|_{\rm op}^2.
\tag{III.F.4c}
\]
To verify the variance, replace \(T_n\) by its symmetric part, diagonalize it orthogonally, and use that the transformed Gaussian coordinates are independent with \(\operatorname{Var}(G^2)=2\). Therefore the difference between this probe and the normalized trace tends to zero in \(L^2\). If the probe is a fixed finite program, Theorem III.F.1 identifies its deterministic limit and hence the trace limit in probability. A fixed polynomial in the initialized actions and their adjoints satisfies the operator moment hypothesis by (III.F.4b), and its application to the probe is such a program. Uniform moments of order greater than one upgrade convergence of these normalized traces to convergence of their expectations: split at a large absolute threshold and use the higher-moment bound to make the first-moment tails uniformly small. The same observation supplies uniform integrability of every fixed polynomial expression needed for finite-degree moment calculations.

#### III.F.3. Exact adaptive Gaussian conditioning

Let the current transcript consist of all revealed roots and all previously computed vectors. For one matrix \(W\), collect its earlier forward and reverse observations as
\[
WV=Y,\qquad W^TU=Q.
\tag{III.F.5}
\]
The columns of \(V\) and \(U\) are the respective query inputs, with output columns in \(Y\) and \(Q\). Conditioned on the transcript they are fixed. Empty column lists are allowed; terms involving them are omitted.

It is necessary to justify this conditioning for adaptive inputs. Initially the conditional laws of the matrices are independent Gaussian laws. Suppose this is true, with the linear constraints already observed, at a particular instruction. A coordinate operation is measurable from the transcript and reveals no new randomness. At a matrix call its input is also measurable from the transcript. Conditional on the transcript, the new answer is a linear observation of only the queried matrix. Conditioning a product of the current conditional laws on this observation leaves the other factors unchanged and conditions only the queried factor. Thus induction preserves independence of the residual matrix factors and adds exactly the indicated linear constraint. A freshly revealed independent root likewise does not alter these residual laws. This argument conditions successively, and does not assume that an adaptive input was independent of the matrix before the transcript was fixed.

Suppose first that \(V^TV\) and \(U^TU\) are invertible. Let \(P_V=V(V^TV)^{-1}V^T\), and similarly define \(P_U\). Then
\[
W\mid\mathcal H\ \overset d=
M+P_{U^\perp}\widetilde W P_{V^\perp},
\quad
M=Y(V^TV)^{-1}V^T
 +U(U^TU)^{-1}Q^TP_{V^\perp},
\tag{III.F.6}
\]
where \(\widetilde W\) is an independent copy of the original matrix.

Here is a direct verification of the Gaussian projection behind (III.F.6). The compatibility relation is \(U^TY=Q^TV\), because both sides equal \(U^TWV\). It gives \(MV=Y\) and \(M^TU=Q\). The homogeneous solutions of (III.F.5) are exactly matrices \(K=P_{U^\perp}KP_{V^\perp}\). Both summands defining \(M\) are orthogonal in Frobenius inner product to that subspace. Hence \(M\) is the unique minimum-Frobenius-norm solution. Vectorize \(W\), whose law is an isotropic Gaussian in \(\mathbb R^{n^2}\). In an orthonormal basis adapted to the homogeneous solution subspace its coordinates are independent Gaussians; conditioning on the orthogonal coordinates leaves independent Gaussians on the homogeneous subspace and fixes the other coordinates to those of \(M\). This proves (III.F.6). It also proves the same assertion with orthogonal projections and minimum-norm solutions when column lists are linearly dependent; the nonsingular formula is the only one whose coefficients we take to a width limit.

For a new forward input \(h\), put
\[
\alpha_n=(V^TV)^{-1}V^Th,
\quad h_\perp=h-V\alpha_n,
\quad
\beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n).
\]
Equation (III.F.6) becomes
\[
Wh=Y\alpha_n+U\beta_n
 +\frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g
\quad\hbox{in conditional law},
\tag{III.F.7}
\]
with \(g\sim N(0,I_n)\) independent of the transcript. The reverse formula follows by interchanging the two sides.

Assume provisionally that every query Gram has a positive definite limit. Inductively all contractions of old nodes converge. Thus the coefficients in (III.F.7), and \(\frac{\|h_\perp\|_2}{\sqrt n}\), converge in probability to deterministic limits. Inverting a positive definite fixed-size matrix is continuous, for instance by a Neumann-series expansion about its invertible limit.

The projection removed from the fresh noise is negligible:
\[
E[\frac{\|P_Ug\|_2^2}{n}\mid\mathcal H]
=\frac{\operatorname{rank}U}{n}.
\tag{III.F.8}
\]
The multiplying variance factor is bounded in probability, so conditional Markov's inequality makes its contribution vanish in normalized mean square. After this removal and replacement of convergent coefficients by their limits, the new coordinate is a deterministic linear combination \(m_\alpha\) of old same-layer nodes plus \(\sigma g_\alpha\).

For a bounded Lipschitz test \(\psi\) of the old tuple and this new coordinate, conditional independence of \(g_\alpha\) gives variance at most \(4\|\psi\|_\infty^2/n\) for its empirical average. Its conditional mean is the old empirical average of the bounded continuous function
\[
x\longmapsto E_G\psi(x,m(x)+\sigma G),
\]
which converges by the induction hypothesis. For the new second moment expand
\[
\frac1n\sum_\alpha(m_\alpha+\sigma g_\alpha)^2
=\frac{\|m\|_2^2}{n}+\frac{2\sigma}{n}\sum_\alpha m_\alpha g_\alpha
 +\frac{\sigma^2}{n}\sum_\alpha g_\alpha^2.
\]
The middle term has conditional variance \(4\sigma^2\frac{\|m\|_2^2}{n}/n\), and the last average has variance \(2/n\). All relevant norms are bounded in probability. We obtain weak convergence and second-moment convergence, hence (III.F.2). Coordinate instructions preserve this convergence because their Lipschitz constants bound the transport cost. This completes the induction under the provisional positive-definiteness assumption.

#### III.F.4. Source-response identity and formal derivatives

For every oriented initialized matrix introduce a centered Gaussian source group indexed by its calls. Sources for different orientations, including a matrix and its transpose, are independent groups; they are also independent of the root tuples. Within a forward group for \(W\), the source attached to input \(h\) has covariance with the source attached to input \(v\) equal to \(E[hv]\). Within the reverse group the analogous covariance is \(E[uv]\) for the corresponding reverse inputs. These are uncentered second moments of inputs and centered covariances of sources.

The scalar node of a new forward call is
\[
\mathscr W h=\xi_h+\sum_{s:\,W^Tu_s\text{ already called}}
 u_s\,E[\partial_{\zeta_s}h].
\tag{III.F.9}
\]
The scalar node of a reverse call is
\[
\mathscr W^*u=\zeta_u+\sum_{r:\,Wv_r\text{ already called}}
 v_r\,E[\partial_{\xi_r}u].
\tag{III.F.10}
\]
An input is its explicit expression in named source coordinates and roots, obtained by unrolling previous scalar instructions. A derivative in (III.F.9) or (III.F.10) differentiates that expression. Previously computed expectations, coefficients, covariance entries, mesh sizes, and any deterministic control values are held fixed. Each named source remains a separate formal argument, including when the joint source covariance is singular. An unavailable source has derivative zero. Derivative paths through other matrices' earlier calls remain part of the expression.

The recursion is causal. At a call, its input and its source derivatives are already defined; their expectations determine the response coefficients. The source covariance extension is the Gram extension of the corresponding input list and is therefore positive semidefinite. A Gaussian group with that extended covariance exists: if the old covariance is \(K\), the new cross-covariance is \(b\), and the new variance is \(v\), positivity implies \(b\in\operatorname{ran}K\) and \(v-b^TK^+b\ge0\). To see the range assertion, test positivity on \((tu,1)\) with \(Ku=0\) and arbitrary \(t\). Completing the square on \(\operatorname{ran}K\) gives the second assertion. Consequently the new coordinate can be represented as \(b^TK^+\xi+\sqrt{v-b^TK^+b}\,G\), with a fresh standard normal \(G\). Here a pseudoinverse is used only to construct one fixed finite Gaussian law; no continuity of pseudoinverses is asserted.

**Lemma III.F.3 (source rule).** Under the positive-definiteness assumption of Section III.F.3, (III.F.9) and (III.F.10) give exactly the scalar laws obtained there.

**Proof.** Consider a forward call and use the notation of (III.F.7). Write old forward inputs as \(v_r\), old reverse inputs as \(u_s\), and their scalar outputs, by induction, as
\[
y_r=\xi_r+\sum_s D_{rs}u_s,
\qquad D_{rs}=E[\partial_{\zeta_s}v_r],
\]
\[
q_s=\zeta_s+\text{a deterministic linear combination of old }v_r.
\]
All old source lists are padded by zeros for unavailable indices. Let \(\alpha\) be the limiting least-squares coefficient from (III.F.7), and let \(h_\perp=h-\sum_r\alpha_rv_r\). Orthogonality gives \(E[v_rh_\perp]=0\). Therefore
\[
E[q_sh_\perp]=E[\zeta_sh_\perp].
\tag{III.F.11}
\]
Let \(G_U=(E[u_su_t])_{st}\), the covariance matrix of \(\zeta\). Gaussian integration by parts gives
\[
E[\zeta h_\perp]=G_U E[\nabla_\zeta h_\perp].
\tag{III.F.12}
\]
For completeness, the one-dimensional identity \(E[Gf(G)]=E[f'(G)]\) follows by integration by parts against the standard normal density. The boundary term vanishes for a function of at most linear growth with bounded derivative. Represent a possibly singular Gaussian vector as \(\zeta=T G\), apply this identity in each independent standard normal coordinate of \(G\), and sum using \(TT^T=G_U\). Conditioning on independent roots and the other source groups proves (III.F.12) in the present setting. Every derivative is integrable: at a fixed finite instruction, its norm is bounded by a deterministic finite expression in earlier coefficients and the bounded derivatives of coordinate maps.

The limiting coefficient of \(U\) in (III.F.7) is consequently
\[
\beta=E[\nabla_\zeta h]-\sum_r\alpha_r E[\nabla_\zeta v_r].
\]
Substitution of the old \(y_r\) decompositions in (III.F.7) cancels the second term exactly. The answer becomes
\[
\xi_h+\sum_su_sE[\partial_{\zeta_s}h],
\qquad
\xi_h=\sum_r\alpha_r\xi_r+\sigma G,
\quad \sigma^2=E[h_\perp^2].
\]
Since the old \(\xi\) covariance is the Gram of the \(v_r\),
\[
E[\xi_h\xi_r]=E[hv_r],
\quad
E[\xi_h^2]=E\Big(\sum_r\alpha_rv_r\Big)^2+E[h_\perp^2]=E[h^2].
\]
The fresh normal is independent of all old roots and source groups. Thus adjoining it preserves independence of distinct oriented source groups. The reverse calculation is the same after interchanging the two layers. Interleaving calls of different matrices does not alter this calculation, because Section III.F.3 established the conditional independence of their residual factors. ∎

Independence of source groups does not assert that the answers of a matrix and its transpose are independent. Their response terms encode their dependence. Nor does it assert that a source is independent of all later inputs; later scalar inputs can be functions of that source.

#### III.F.5. Singular queries without a rank-stability assumption

**Lemma III.F.4 (regularization of a fixed program).** The conclusions of Theorem III.F.1 and the formulas (III.F.9)–(III.F.10) hold when any of the limiting input Grams is singular.

**Proof.** For every matrix call introduce a new independent standard Gaussian input vector \(\chi\), revealed immediately before that call, and replace its input \(h\) by \(h+\varepsilon\chi\). Each call has a distinct noise vector. The other instructions are unchanged.

At fixed \(\varepsilon>0\), the new noise is independent of the old transcript and of the unperturbed part of the current input. If \(V\) is the list of prior same-orientation inputs, the normalized squared distance from \(h+\varepsilon\chi\) to \(\operatorname{span}V\) is
\[
\frac{\|P_{V^\perp}h\|_2^2}{n}
 +2\varepsilon\frac{1}{n}\langle P_{V^\perp}h,\chi\rangle_{\mathbb R^n}
 +\varepsilon^2\frac{\|P_{V^\perp}\chi\|_2^2}{n}.
\]
Conditionally, the cross term has variance \(4\varepsilon^2\frac{\|P_{V^\perp}h\|_2^2}{n}/n\). The last norm squared has mean \(1-\operatorname{rank}V/n\) and variance at most \(2/n\). Thus every limiting new squared distance is at least \(\varepsilon^2\). Induction gives positive definite limiting query Grams, so Sections III.F.3–III.F.4 apply to the perturbed program. Equivalently, in its scalar law the new independent root adds \(\varepsilon^2\) to the Schur complement of the old input Gram.

Couple the perturbed and original finite programs with the same matrices and roots. On the event that all initialized matrix norms are at most 10 and that all of the finitely many fresh noise vectors have normalized norms at most 2, propagate errors instruction by instruction. A coordinate instruction multiplies the previous error by its fixed Lipschitz constant; a linear combination contributes the sum of coefficient magnitudes times previous errors; a matrix call contributes at most ten times the input error plus \(20\varepsilon\). Consequently
\[
\max_{\text{nodes }v}\frac{\|v_n^\varepsilon-v_n\|_2}{\sqrt n}
\le C\varepsilon,
\tag{III.F.13}
\]
where \(C\) is finite and independent of \(n\) and \(0<\varepsilon\le1\). The event has probability tending to one by Lemma III.F.2 and the elementary second-moment calculation for Gaussian noise norms.

We next show that the scalar recursion itself is continuous at \(\varepsilon=0\); this step concerns covariances and derivatives, not inverses of empirical Grams. Induct on its finitely many instructions. Each scalar node is a \(C^1\) expression in the finite named source list and roots. If earlier deterministic coefficients remain in a compact set, the expression and its first source derivatives have uniform bounds: the expression has at most linear growth in the root and source coordinates, and its derivatives have a finite deterministic bound. This follows directly by applying the coordinate derivative bounds and the linear response formulas in the previous instructions. The values and first derivatives are continuous in their arguments and in the earlier coefficient list.

By induction, the covariance entries for the next source, which are second moments of old scalar inputs, converge as \(\varepsilon\downarrow0\). If positive semidefinite matrices \(K_j\to K\) have fixed size, then \(K_j^{1/2}\to K^{1/2}\). To verify this without a regularity assumption on eigenvalues, their positive square roots are bounded. Every convergent subsequence of these square roots has a positive semidefinite limit \(T\) with \(T^2=K\). A positive semidefinite matrix has a unique positive semidefinite square root: diagonalize it, observe that any such \(T\) commutes with \(K=T^2\), and restrict to its eigenspaces. Hence every subsequential limit is \(K^{1/2}\), which proves convergence.

Represent the full finite source prefix for each \(\varepsilon\) as \(K_\varepsilon^{1/2}G\) using one standard Gaussian vector for each oriented group, independently of the roots. This couples the source prefixes in \(L^2\). The uniform linear-growth bounds and Lipschitz constants for node expressions then give their \(L^2\) convergence. More explicitly, split the node difference into a change of arguments at fixed coefficients, bounded by the common Lipschitz constant, and a change of coefficients at fixed arguments. The latter converges pointwise and is bounded by a constant times one plus the norm of the finite root/source list, an \(L^2\) dominator. First source derivatives converge in probability and are uniformly bounded, so their expectations converge. This proves convergence of the next response coefficient and closes the induction. At zero noise the resulting expression is exactly (III.F.9)–(III.F.10) for the original formal program.

Let \(\mu^\varepsilon\) be the perturbed scalar law of a selected tuple and \(\mu^0\) the zero-noise law just constructed. We have \(\mathcal W_2(\mu^\varepsilon,\mu^0)\to0\). By (III.F.3), (III.F.13), and the proved fixed-\(\varepsilon\) limit,
\[
\mathcal W_2(\widehat\mu_n,\mu^0)
\le C_m\varepsilon
 +\mathcal W_2(\widehat\mu_n^\varepsilon,\mu^\varepsilon)
 +\mathcal W_2(\mu^\varepsilon,\mu^0)
\]
on an event of probability tending to one. Choose \(\varepsilon\) first, let \(n\to\infty\), and then let \(\varepsilon\downarrow0\). This proves the full-sequence convergence in probability, including singular Grams, and finishes Theorem III.F.1. ∎

The derivative convention has a precise invariant meaning on singular supports. If a source vector \(\zeta\) has covariance \(G\), and \(u\) is the vector of the associated reverse inputs with \(E[uu^T]=G\), then
\[
E[\zeta f]=G E[\nabla f],\qquad
u^Tv=0\text{ a.s. for every }v\in\ker G.
\tag{III.F.14}
\]
The second identity follows from \(E[(u^Tv)^2]=v^TGv=0\). If two admissible smooth formal expressions agree on the Gaussian support, their expected derivative vectors differ by an element of \(\ker G\), by the first identity. Their contracted corrections therefore agree. Individual derivative coefficients need not agree. None of this implies that pseudoinverses converge at rank loss.

#### III.F.6. Causal scalar feedback

The deterministic-coefficient theorem also identifies programs with the following causal scalar feedback. At finitely many stages, compute inner products of already available same-layer nodes, apply locally Lipschitz functions to the resulting finite scalar list, and use the resulting numbers as coefficients of subsequent linear combinations. Assume all scalar operations are defined on a neighborhood of their deterministic limiting arguments; divisions require a nonzero limiting denominator. Require the actual finite operation to be defined everywhere it is used, or assign an arbitrary measurable fallback outside that neighborhood. Convergence of its arguments makes the exceptional event have probability tending to zero. The physical algorithms themselves use no division. Coefficients may multiply unbounded vector nodes, because their perturbations can be estimated by the vector's normalized \(L^2\) norm.

To prove this extension, construct an oracle program by replacing each scalar feedback value by its limiting deterministic value, computed from earlier scalar nodes. The construction is causal and therefore not an implicit fixed-point definition. Theorem III.F.1 identifies this oracle. At the next scalar step use
\[
|\frac{1}{n}\langle u,v\rangle_{\mathbb R^n}-\frac{1}{n}\langle\bar u,\bar v\rangle_{\mathbb R^n}|
\le\frac{\|u-\bar u\|_2}{\sqrt n}\frac{\|v\|_2}{\sqrt n}
 +\frac{\|\bar u\|_2}{\sqrt n}\frac{\|v-\bar v\|_2}{\sqrt n}.
\tag{III.F.15}
\]
At the next scalar multiplication use
\[
\frac{\|c u-\bar c\bar u\|_2}{\sqrt n}
\le |c|\frac{\|u-\bar u\|_2}{\sqrt n}+|c-\bar c|\frac{\|\bar u\|_2}{\sqrt n}.
\]
All oracle norms and finitely many oracle coefficients are bounded in probability; initial operator norms are bounded with probability tending to one. Inductively, these inequalities show that actual coefficients converge to oracle coefficients, actual node errors vanish in normalized \(L^2\), and actual norms remain bounded in probability. Local Lipschitzness of scalar operations suffices by restricting to a compact neighborhood of their deterministic limiting arguments. Equation (III.F.3) transfers every oracle empirical law to the actual program.

#### III.F.7. Common generated probability spaces and actual adjoints

We now fix the data and activation parameters. Construct a countable language of finite deterministic-coefficient programs. Include every root coordinate required by the model; constants; rational linear combinations; applications of the initialized matrices in both directions; the finitely many layer activations and fixed integer-level clips; and, for each arity, a countable family of bounded smooth globally Lipschitz functions dense among continuous functions on compact sets. One explicit such family is obtained by taking piecewise polynomial approximations on rational grids, multiplying by smooth compactly supported cutoffs, smoothing with fixed rational-scale mollifiers, and retaining rational coefficients and rational scales. Clipped products may be included in the same family. Close the language under finite composition. Additional countable lists of fixed programs, probes, caps, time meshes, or coefficient values can be included at the start.

This language is countable and admits a causal enumeration with finite stages. Enumerate its root slots, functions, and numerical coefficients first; at stage \(m\), add the finitely many expressions with at most \(m\) instructions using only the first \(m\) listed items, in dependency order. Every finite expression occurs at some stage. Repeated instructions may be treated as separate named copies. Running the scalar construction on this list realizes all its nodes on a product probability space with countably many independent standard Gaussian coordinates, together with the root tuples. Section III.F.4 gives the successive Gaussian extensions, including zero conditional variance. At each layer retain only the sigma-field generated by that layer's node coordinates; call the resulting probability space \((\Omega_\ell,\mu_\ell)\) and put
\[
\mathcal H_\ell=L^2(\Omega_\ell,\mu_\ell).
\tag{III.F.24}
\]
One can equivalently take the law of the countable tuple of generated coordinates. Its finite-dimensional marginal laws are those from Theorem III.F.1: any finite family is part of a finite program, and unused computations change none of the finite-width vectors. Thus different causal enumerations produce the same generated laws up to the coordinate identification. No arbitrary extra Gaussian directions are added to \(\mathcal H_\ell\).

For every rational combination \(u\) of generated nodes, include its forward and reverse answer nodes. The finite inequality \(\frac{\|W^{(\ell)}_nu_n\|_2}{\sqrt n}\le10\frac{\|u_n\|_2}{\sqrt n}\) holds with probability tending to one. Both squared norms have deterministic limits by Theorem III.F.1, so
\[
\|\mathscr W^{(\ell)}_0u\|_{\mathcal H_\ell}\le10\|u\|_{\mathcal H_{\ell-1}}.
\tag{III.F.25}
\]
The same holds for every other action orientation. Linearity of the finite matrices and convergence of squared differences give linearity of the assignments: for example the limiting squared norm of the difference between the answer to \(u+v\) and the sum of answers is zero. If two expressions represent the same \(L^2\) input, (III.F.25) shows that their answers represent the same output. Real linearity on the real span follows either from finite real-coefficient probes or from rational approximation.

The span of generated nodes is dense in \(\mathcal H_\ell\). Here are the measure-theoretic details. Cylinder sets depending on finitely many coordinates generate its sigma-field. The sets whose indicators can be approximated in \(L^2\) by finite linear combinations of cylinder indicators form a monotone class: under increasing unions or decreasing intersections, indicator convergence in \(L^2\) follows from the continuity of probability measures. They contain the cylinder algebra, hence all generated measurable sets. Simple functions and truncation then approximate every \(L^2\) variable by functions of finitely many coordinates. For a finite Borel probability law on \(\mathbb R^m\), bounded continuous functions are dense in \(L^2\): approximate an indicator by a compact subset inside an open superset whose probability difference is small, and use the continuous distance-ratio function that is one on the compact set and zero outside the open set. Such compact/open approximations follow by first restricting to large boxes and then approximating Borel sets using finite unions of rational boxes; their class is again a monotone class. Finally approximate bounded continuous functions on compact boxes by the included smooth family and control the complement by boundedness and its small probability. All approximants are generated nodes or linear combinations of them.

Consequently (III.F.25) extends uniquely by \(L^2\) completion to a bounded linear map
\[
W^{(\ell)}_0:\mathcal H_{\ell-1}\to \mathcal H_\ell,\qquad
\|W^{(\ell)}_0\|\le10,\qquad 2\le\ell\le L.
\tag{III.F.26}
\]
The reverse assignments extend in the same way. At finite width,
\(\frac{1}{n}\langle v_n,W^{(\ell)}_nu_n\rangle_{\mathbb R^n}=\frac{1}{n}\langle W^{(\ell)}_n^Tv_n,u_n\rangle_{\mathbb R^n}\).
Pass to the limiting pairwise contractions for generated \(u,v\); then use their density and the bounds (III.F.26). This gives
\[
\langle v,W^{(\ell)}_0u\rangle_{\mathcal H_\ell}
=\langle (W^{(\ell)}_0)^*v,u\rangle_{\mathcal H_{\ell-1}},\qquad 2\le\ell\le L.
\tag{III.F.27}
\]
The starred maps are therefore exactly the Hilbert-space adjoints. They are not resampled reverse matrices.

There is no contradiction between these bounded actions and Gaussian initialization. The actions describe all finite generated probes and their joint laws, including adaptive probes. They are not an assertion that every random \(L^2\) input is independent of an initialized action. An adaptive input generally has the response correction in (III.F.9).

Fixed programs with arbitrary real coefficients and arbitrary globally Lipschitz coordinate instructions are represented on these same spaces. Approximate their coefficients by rationals and their coordinate functions on larger compact sets by the dense family. For a Lipschitz target \(g\), select bounded smooth approximants \(g_m\) with accuracy \(1/m\) on the radius-\(m\) ball and a common envelope \(|g_m(x)|\le C(1+|x|)\). Cutting off \(g\) on the radius-\(2m\) ball, mollifying at a sufficiently small scale, and rationally approximating on that ball gives such a sequence with a slightly enlarged fixed envelope. Choose the countable dense family to include these rational cutoff approximants. At a fixed scalar input, the approximation error tends to zero in \(L^2\) by linear growth and the input's finite second moment. Inductively propagate these errors: every matrix call uses the norm bound 10, and each target coordinate instruction uses its Lipschitz bound to control a change of input before approximating the instruction at the limiting input. The identical finite-array error argument holds in probability by Theorem III.F.1 and convergence of the required tail second moments. This proves the agreement of the common-space calculation with its fixed-program width limit.

#### III.F.8. Hilbert–Schmidt increments and the raw state space

For Hilbert spaces \(H,K\), the Hilbert–Schmidt norm of an operator \(T:H\to K\) is
\[
\|T\|_{\rm HS}^2=\sum_j\|Te_j\|_K^2,
\tag{III.F.28}
\]
where \((e_j)\) is an orthonormal basis. This value does not depend on the basis: expand each scalar coefficient \(\langle Te_j,f_k\rangle\) in a basis \((f_k)\) of \(K\), use Parseval twice, and interchange the nonnegative double sum. In particular \(\|T\|_{\rm op}\le\|T\|_{\rm HS}\), since for a unit vector completed to an orthonormal basis its image squared norm is one summand of (III.F.28). The normed space of such operators is complete: a Cauchy sequence has Cauchy matrix coefficients in \(\ell^2\) of two basis indices, whose limit defines an operator by Cauchy–Schwarz and has the limiting Hilbert–Schmidt norm.

For \(u\in K,v\in H\), define
\[
(u\otimes v)q=u\langle v,q\rangle_H.
\]
Parseval gives
\[
\|u\otimes v\|_{\rm HS}=\|u\|_K\|v\|_H,
\quad
(u\otimes v)^*=v\otimes u,
\tag{III.F.29}
\]
and
\[
\|u\otimes v-\tilde u\otimes\tilde v\|_{\rm HS}
\le\|u-\tilde u\|\|v\|+\|\tilde u\|\|v-\tilde v\|.
\tag{III.F.30}
\]
For a Hilbert–Schmidt \(T\), expansion in an orthonormal basis also gives
\[
\langle u\otimes v,T\rangle_{\rm HS}=\langle u,Tv\rangle_K.
\tag{III.F.31}
\]
At width \(n\), using the normalized inner product on both layers, the orthonormal basis is \((\sqrt n\,e_j)_{j=1}^n\); (III.F.28) is then the ordinary Frobenius norm of the matrix. The rank-one action is \(uv^T/n\). Thus this is the exact population counterpart of the raw matrix metric.

The affine raw parameter space in the isometric first coordinates is
\[
 \mathcal P=L^2(\Omega_1;\mathbb R^d)
 \times\prod_{\ell=2}^L
 (W^{(\ell)}_0+\mathcal S_2(\mathcal H_{\ell-1},\mathcal H_\ell))\times \mathcal H_L,
                                                        \tag{III.F.32}
\]
with increment norm
\[
 \|\Delta\theta\|_{\rm raw}^2
 =\|\Delta w\|_2^2+\sum_{\ell=2}^L\|\Delta W^{(\ell)}\|_{\rm HS}^2
                                  +\|\Delta W^{(L+1)}\|_2^2.     \tag{III.F.33}
\]
Only the learned action increments are Hilbert--Schmidt. This is
isometric to the original raw metric because \(w=\sqrt d V^{(1)}\).
Continuous rank-one velocities have strong integrals: their Riemann
sums are Cauchy by uniform continuity on compact intervals and
completeness. The norm of the integral is bounded by the integral of
the norm, and its derivative is the continuous integrand. Formula
(III.F.30) passes uniform factor convergence to HS velocity and integral
convergence. For measurable integrable velocities the same statements
follow by approximation by step functions. Thus learned forward and
reverse increments are actual adjoints throughout.

#### III.F.9. Strong multiplier continuity and the chain rule

**Lemma III.F.5 (bounded multiplier).** Suppose \(z_m\to z\) in probability, \(v_m\to v\) in \(L^2\), and \(b\) is bounded and continuous. Then
\[
b(z_m)v_m\longrightarrow b(z)v\quad\hbox{in }L^2.
\tag{III.F.34}
\]

**Proof.** The term \(b(z_m)(v_m-v)\) has norm at most \(\|b\|_\infty\|v_m-v\|_2\). For the remaining term first restrict to \(|v|\le M\); bounded convergence in probability implies convergence in \(L^2\) of the bounded multiplier difference there. The complement has squared norm at most \(4\|b\|_\infty^2E[|v|^2 1_{|v|>M}]\). Send \(m\) to infinity and then \(M\) to infinity. Bounded convergence in probability used here follows from the elementary estimate \(E|X_m|^2\le\eta^2+K^2\Pr(|X_m|>\eta)\) when \(|X_m|\le K\). ∎

**Lemma III.F.6 (strong chain rule along curves).** Let \(z:I\to L^2(\Omega)\) be strongly \(C^1\), and let \(\phi\in C^1(\mathbb R)\) have bounded derivative. Then \(\phi(z(t))\) is strongly \(C^1\), with
\[
\frac d{dt}\phi(z(t))=\phi'(z(t))\dot z(t).
\tag{III.F.35}
\]

**Proof.** Set \(v_h=(z(t+h)-z(t))/h\to\dot z(t)\) in \(L^2\). The scalar fundamental theorem of calculus gives
\[
\frac{\phi(z(t+h))-\phi(z(t))}{h}
=v_h\int_0^1\phi'(z(t)+rh v_h)\,dr.
\]
The multiplier is bounded by \(\|\phi'\|_\infty\). It converges in probability to \(\phi'(z(t))\): \(|hv_h|\to0\) in probability; restrict \(z(t)\) to a large compact interval and use uniform continuity of \(\phi'\) on a slightly larger interval. The proof of Lemma III.F.5 applies to this bounded convergent multiplier, and yields the derivative. Lemma III.F.5 applied to \(z(t),\dot z(t)\) also proves continuity of the resulting velocity. ∎

This conclusion is a curve chain rule, and makes no claim that the pointwise nonlinear map is Fréchet differentiable from all of \(L^2\) to \(L^2\). Bounded \(\phi'\) is sufficient for the curve result. A jointly measurable velocity may also be integrated coordinatewise: Fubini and \(E\int_I|v(t)|^2dt<\infty\) give absolutely continuous coordinate paths almost surely, agreeing with the \(L^2\) integral. This permits the ordinary scalar chain rule almost everywhere for an absolutely continuous \(L^2\) curve with integrable squared speed.

For bounded-operator curves \(A(t)\) differentiable in Hilbert–Schmidt or operator norm and strongly differentiable \(h(t)\in H\),
\[
\frac d{dt}[A(t)h(t)]=\dot A(t)h(t)+A(t)\dot h(t).
\tag{III.F.36}
\]
Subtract the proposed derivative from the difference quotient. The first error is the operator derivative error applied to fixed \(h(t)\); the second is a uniformly bounded operator applied to the strong derivative error of \(h\); and the cross product is bounded by \(\|A(t+h)-A(t)\|\,\|(h(t+h)-h(t))/h\|\), which tends to zero. This proves (III.F.36).

#### III.F.10. Scalar prediction and feature energy are continuously differentiable

Let \(\rho_\ell\in C^2(\mathbb R)\) have bounded first and second
derivatives for each of the finitely many layers. They may have
nonzero offsets and different bounds at different layers. Define
\(Y_i^1=w\cdot u_i\), \(X_i^\ell=\rho_\ell(Y_i^\ell)\),
\(Y_i^\ell=W^{(\ell)} X_i^{\ell-1}\) for \(\ell\ge2\), and
\(F_i=\langle W^{(L+1)},X_i^L\rangle_L\). Put
\[
 q_i^L=W^{(L+1)},\quad d_i^\ell=\rho_\ell'(Y_i^\ell)q_i^\ell,
 \quad q_i^\ell=(W^{(\ell+1)})^*d_i^{\ell+1}\ (\ell<L).
                                                        \tag{III.F.38}
\]
**Theorem III.F.7.** The scalar map \(F_i:\mathcal P\to\mathbb R\)
is continuously Fréchet differentiable, with
\[
 dF_i[\Delta\theta]
 =\langle d_i^1,u_i\cdot\Delta w\rangle_1
  +\sum_{\ell=2}^L\langle d_i^\ell,
                         \Delta W^{(\ell)} X_i^{\ell-1}\rangle_\ell
  +\langle X_i^L,\Delta W^{(L+1)}\rangle_L,                       \tag{III.F.39}
\]
and raw gradient blocks
\[
 \nabla_w F_i=d_i^1u_i,\qquad
 \nabla_{W^{(\ell)}}F_i=d_i^\ell\otimes X_i^{\ell-1},\qquad
 \nabla_{W^{(L+1)}} F_i=X_i^L.                            \tag{III.F.40}
\]
**Proof.** For a fixed \(v,z\in L^2\), a function \(\rho\) with
\(L_1=\|\rho'\|_\infty,L_2=\|\rho''\|_\infty<\infty\), and
an increment \(q\in L^2\), its scalar Taylor remainder obeys both
\(L_2|q|^2/2\) and \(2L_1|q|\) bounds. Hence
\[
 |E[v\{\rho(z+q)-\rho(z)-\rho'(z)q\}]|
 \le \tfrac12L_2M\|q\|_2^2
   +2L_1\|v\mathbf1_{|v|>M}\|_2\|q\|_2
                         =o(\|q\|_2),                   \tag{III.F.41}
\]
where first \(q\to0\) at fixed \(M\), then \(M\to\infty\).

On a raw neighborhood, forward induction bounds every field
increment by \(O(\eta)\), with \(\eta=\|\Delta\theta\|_{\rm raw}\):
the bottom is linear, every activation is Lipschitz, and
\(\Delta(A X)=\Delta A X+A\Delta X+\Delta A\Delta X\),
with \(\|\Delta A\|_{\rm op}\le\eta\). Start from
\(\Delta F_i=\langle\Delta W^{(L+1)},X_i^L\rangle+
\langle W^{(L+1)},\Delta X_i^L\rangle+O(\eta^2)\).
At level \(\ell\), apply (III.F.41) with fixed incoming weight
\(q_i^\ell\) to replace its weighted feature difference by
\(\langle d_i^\ell,\Delta Y_i^\ell\rangle\), at cost
\(o(\eta)\). If \(\ell\ge2\), expand its action difference;
its mixed term is \(O(\eta^2)\), and adjunction changes the
remaining propagated term to
\(\langle q_i^{\ell-1},\Delta X_i^{\ell-1}\rangle\).
This is the induction invariant for the next lower level. At
\(\ell=1\) the bottom projection is exactly linear. Summing the
finitely many remainders proves (III.F.39). The rank-one identity
(III.F.31) proves (III.F.40). Forward continuity, Lemma III.F.5 at each backward
gate, bounded action continuity and (III.F.30) prove continuity of every
gradient block. This proves the assertion. \(\square\)

For \(H(\theta_h)=\sum_i p_i X_i^L\), the scalar functional
\(\mathcal E=\|H\|^2/2\) is also continuously Fréchet differentiable.
Indeed \(\Delta H=O(\eta)\), so
\(\Delta\mathcal E=\langle H,\Delta H\rangle+O(\eta^2)\).
Apply the same downward weighted expansion with fixed top weight
\(H\) and coefficients \(p_i\). Its gradient is precisely the
backward rank-one expression with readout replaced by \(H\).
The same multiplier continuity proves continuity of this gradient.
No Fréchet derivative of an \(L^2\)-valued Nemytskii map is used.

In the network of Part III.M, take \(\rho_\ell=\chi_\ell\).
The original predictors are \(f_i=a^LF_i\), so their raw gradients
are exactly \(a^L\nabla F_i\). Thus a strong solution of the stated
uncut equations is the raw Hilbert gradient flow of
\(\mathcal L=\tfrac12\sum_i(f_i-y_i)^2\), and
\[
 \dot f=-Kr,\qquad
 \dot{\mathcal L}=-\left\|\sum_i r_i\nabla f_i\right\|_{\rm raw}^2
                =-r^TKr,\quad
 K_{ij}=\langle\nabla f_i,\nabla f_j\rangle_{\rm raw}.
                                                        \tag{III.F.43}
\]
This establishes the true gradient/kernel identities; existence
of the uncut flow is a separate conclusion of Parts III.G and III.V.

#### III.F.11. Fixed-cap local existence and Euler approximation

For each fixed cap, the normalized backward gates in Part III.S are
\(C^1\) with bounded first derivatives. Forward induction and
backward substitution therefore make the raw field locally
Lipschitz on any bounded primal ball. Rank-one updates use (III.F.30),
and physical residual differences use (III.F.15). No derivative of
an uncut \(L^2\)-valued product is needed.

For an autonomous cap field with norm bound \(M_0\) and Lipschitz
constant \(L_0\) on a ball of radius \(b\), its integral map preserves
that ball and is a contraction for \(tM_0\le b\), \(tL_0<1\).
Uniformly converging Picard iterates give a unique strong \(C^1\)
solution. Bounded raw speed gives a strongly Cauchy finite endpoint,
from which the same construction continues whenever a primal bound
is available. For measurable bounded deterministic controls, the
same contraction gives a strongly absolutely continuous path and
its equation almost everywhere.

The one-step Euler defect is at most \(L_0M_0h^2/2\), by integrating
\(\|F(\theta(t+s))-F(\theta(t))\|\le L_0M_0s\).
Iteration of the discrepancy recurrence gives
\[
 \max_k E_k\le e^{L_0T}
        (E_0+\tfrac12 L_0M_0T\max_kh_k).                  \tag{III.F.45}
\]
The constants are width independent on a specified primal ball
and the initialized norm event. This compares a fine raw algorithm
to a fixed auxiliary transcript; the finite-program theorem is
never applied directly to a transcript growing with width.

Whenever the incoming tuple already has its joint \(\mathcal W_2\)
limit, or the later reference estimates give uniformly vanishing
incoming second-moment tails, a final value observation \(q\rho'(z)\)
is treated by clipping \(q\), applying Theorem III.F.1, and removing
the clip using those tails and bounded actions. Mere boundedness
of \(L^2\) norms is not substituted for this tail premise. Whenever a source derivative
of such an unbounded product is needed, the later Parts III.V and III.N
supply the stronger derivative-valid truncation argument explicitly.

### III.S. Direct controlled source estimates at all finite depths

Let psi be C2 with ||psi||infty, ||psi'||infty, ||psi''||infty <= 1. Nonconstancy is not required for this lemma. Let L>=2, 0<=e<=1, T>0, and

    a >= 10^12(1+T),   S = T a^(-L),   K_l = a^(l-1),   eps=e/a.

Use the ORIGINAL raw parameters and metric. Normalize only hidden fields:

    Y_l = Z_l/a^(l-1),   X_l = H_l/a^l,
    chi_l(y) = y + [1+eps psi(K_l y)]/K_l,
    F_i = <Wout,X_(L,i)>,   f_i=a^L F_i.

Thus Y_l=W_l X_(l-1), with the normalized first-layer representation Y_(1,i)=<w,u_i>, ||u_i||=1. For deterministic bounded controls ||c(s)||_1<=3, the normalized controlled raw field is

    Wout'=sum_i c_i X_(L,i),
    W_l'=sum_i c_i d_(l,i) tensor X_(l-1,i)  (2<=l<=L),
    w'=sum_i c_i d_(1,i)u_i,
    q_L=Wout,   q_l=W_(l+1)^* d_(l+1),
    d_l=D_(l,R)(Y_l,q_l),
    D_(l,R)(y,q)=q+eps psi'(K_l y) tau_R(q).

The clip is C1, |tau_R(q)|<=min(|q|,2R), |tau_R'|<=1, and equals q for |q|<=R. All constants below are uniform over R, positive Euler meshes of total length <=S, and deterministic choices of controls satisfying the displayed bound. Population initialization is Wout(0)=0. The actual finite-width random readout must be retained before the fixed-cap bridge, as explained at the end.

The bounds used are exactly

    |chi_l(y)-y|<=2/K_l,  |chi_l'|<=2,
    |D(y,q)|<=2|q|,  |D_q|<=2,
    |D_y|<=eps K_l |q|<=K_l |q|,
    |D_y|<=2 eps K_l R.

In particular psi' and psi'' may change sign.

#### III.S.1. Exact finite-program input and local equations

The input theorem required from Part III.F is this: a fixed finite program built from independent normalized Gaussian adjacent matrices, both orientations of each matrix, independent Gaussian roots, C1 coordinate maps with bounded continuous derivatives, and causal scalar contractions has a canonical scalar Gaussian-source law. A forward answer on input h equals its centered source plus earlier reverse inputs multiplied by their expected named-source derivatives of h. The reverse rule interchanges the two sides and includes current forward calls. Each source covariance is the FULL uncentered input Gram. Distinct oriented Gaussian source groups are independent. Named derivatives freeze all source covariances, scalar contractions, previously produced response coefficients, meshes, and controls; named slots stay distinct at singular covariance. These are the source identities (III.F.9)--(III.F.10) and Lemma III.F.4 proved in Part III.F above. Fixed caps satisfy all of its coordinate hypotheses because psi is C2 and the four displayed gate derivative bounds hold.

Apply this input chronologically to one finite Euler program. At layer l the exact local equations are

    Y_l = xi_l + Acal_l d_l,
    q_l = zeta_l + Bcal_(l+1) X_l,
    X_l = chi_l(Y_l),   d_l = D_(l,R)(Y_l,q_l).

Here Acal_l is strictly lower triangular in time and Bcal_(l+1) is lower triangular, including its diagonal. At the bottom xi_1 is the repeated initialized Gaussian root and

    Acal_(1,kj)=h_j G diag(c_j),   j<k.

At the top zeta_L=0 and Bcal_(L+1) is the strictly past readout integrator, replicated over the three samples. Its full block-row norm is <=3S.

For internal matrices the exact response coefficients, with sample indices u,v, are

    (Acal_(l+1,kj))_(uv)
       = E partial_(zeta_(l,j,v)) X_(l,k,u)
         + h_j c_(j,v) E[X_(l,k,u) X_(l,j,v)] ,  j<k,

    (Bcal_(l,kj))_(uv)
       = E partial_(xi_(l,j,v)) d_(l,k,u)
         + 1_(j<k) h_j c_(j,v) E[d_(l,k,u) d_(l,j,v)] ,  j<=k.

The learned contractions follow by unrolling the rank-one parameter increments. The response terms are the source rule just stated. These identities hold at the actual coefficient arrays; no comparison covariance or replacement transpose law is introduced.

For a three-by-three block use its induced infinity norm. For a row use the SUM of its block norms. Write a local strict density bound as |Acal_(l,kj)|<=alpha h_j, and a full causal row bound as sum_(j<=k)|Bcal_(l+1,kj)|<=b. Set r=alpha S b.

#### III.S.2. Independent primal bounds

Use initialized adjacent action norms <=10 and initial first-layer projection norms <=2. These bounds follow from the elementary net argument proved in Part III.F: a one-quarter net on each unit sphere has cardinality at most 9^n, and the net approximation gives ||W||op <= 2 max_(u,v in nets)|u^T Wv|. Since every fixed bilinear form is N(0,1/n), P(||W||op>10)<=2*9^(2n)*exp(-100n/8), which tends to zero. A finite union bound handles all L-1 matrices, the Gaussian law of large numbers handles the three first-layer projection norms, and passage on a countable dense generated family gives the canonical norm bound 10. No precise asymptotic spectral-norm theorem is required. Stop at hidden joint raw displacement D=1. Then current adjacent action norms are <=11 and ||Y_(1,i)||_2<=3. Put F=32^L. The offset causes no problem:

    ||X_(1,i)||_2<=3+2=5<=32,
    ||X_(l,i)||_2<=11*32^(l-1)+2<=32^l.

Consequently, for s<=S and at every Euler node,

    ||Wout(s)||_2<=3Fs,
    ||q_(l,i)(s)||_2<=Q_l := 32^(L-l) 3FS,
    ||d_(l,i)(s)||_2<=2Q_l,
    ||Y_(l,i)(s)||_2<=F.

Every hidden block speed is <=F||Wout||_2: for an internal block, the coefficient bound is 3*2*32^(L-l)*32^(l-1)=(3/16)F; the bottom is the same. Thus

    D(s)<=3 sqrt(L) F^2 s^2.

For Euler, sum_j h_j s_j <=s_k^2/2 supplies the same bound and excludes even a first overshooting node: the proposed node's update length only uses earlier states inside the stop. With a>=10^12(1+T),

    D(S)<=3 sqrt(L) (1024/a^2)^L T^2 <1/4,
    max_l Q_l <1/2.

Hence the stop is never reached and ||d_l||_2<=1. These bounds are independent of source coefficient estimates; they may be used inside a chronological source induction without circularity.

#### III.S.3. Same-array Gaussian-part estimate, including the offset

Freeze one actual finite local prefix whose coefficient rows obey alpha,b. Write

    u_l = [1+eps psi(K_l Y_l)]/K_l,  |u_l|<=2/K_l,
    v_l = eps psi'(K_l Y_l) tau_R(q_l),  |v_l|<=|q_l|.

Then X=Y+u and d=q+v. Assume r<=1/8 and put

    Rloc=(I-Acal Bcal)^(-1),   U=Rloc Acal,
    Lloc=(I-Bcal Acal)^(-1),
    Y_G=Rloc xi + U zeta,
    q_G=Lloc zeta + Bcal Rloc xi.

These are centered Gaussian combinations of the original frozen source groups. Triangular inverses exist exactly; the geometric row bounds also give

    |Rloc|row, |Lloc|row<=2,
    |U|row<=2alpha S,   |Bcal U|row<=2r,
    |Lloc Bcal|row<=2b.

Exact elimination, with NO replacement of the actual coefficient arrays, yields

    Y-Y_G = U v + U Bcal u,
    q-q_G = Bcal U v + Lloc Bcal u.

Let m_p(q)=max_(k,i)||q_(k,i)||_p on this finite prefix. It is finite before absorption, since fixed-cap finite programs are finite globally Lipschitz Gaussian expressions. The identities imply

    m_p(q-q_G)<=2r m_p(q)+4b/K_l,
    m_2(q_G)<=(1+2r)Q_l+4b/K_l<=2Q_l+4b/K_l.

Each q_G coordinate is Gaussian with its ACTUAL covariance, so ||q_G||_p<=sqrt(p)||q_G||_2 for p>=2. Absorb 2r m_p(q), retaining the bounded non-Gaussian remainder, to obtain

    m_p(q)<=20(Q_l+b/K_l)sqrt(p),   p>=2.                 (III.S.1)

For the local curvature multiplier N_k=K_l max_i|q_(k,i)| this gives

    ||N_k||_p <= Msrc_l sqrt(p),
    Msrc_l=60(n_l+b),   n_l=K_l Q_l.                       (III.S.2)

The factor 3 in Msrc_l merely bounds the norm of the maximum by the sum of the three marginal norms. No random time maximum is used.

The other exact identity and the independent actual bound ||Y||_2<=F likewise give

    max_(k,i)||Y_(k,i)||_p
        <=[F+50alpha S(Q_l+b/K_l)]sqrt(p).               (III.S.3)

Indeed ||Y-Y_G||_p<=2alpha S m_p(q)+4alpha S b/K_l; use this at p=2 to bound the Gaussian variance by F+2alpha S Q_l+4alpha S b/K_l and then use (III.S.1). The coefficient 50 exceeds the resulting coefficients 42 for Q_l and 44+4/sqrt(2) for b/K_l. In the box below the bracket is <=2F, hence ||X_(k,i)||_p<=4F sqrt(p).

This calculation isolates why the offset is harmless: its size is 1/K_l, exactly the inverse scale of the possible curvature K_l. The remainder estimate 4b/K_l therefore gives the displayed constants 20 and 60.

#### III.S.4. Derivative rows and production bounds

Set G=diag chi_l'(Y), V=diag D_q(Y,q), and N=diag D_y(Y,q). Their norms obey |G|,|V|<=2 and |N_k|<=K_l max_i|q_(k,i)|. For any named source, the exact Y-Jacobian satisfies

    J=I_xi + Acal [N J + V(I_zeta+Bcal G J)].

The current Bcal diagonal remains in this identity. Strictness of Acal ensures that J at time k depends on this bracket only at strictly earlier times.

Let E_k denote

    E_k=exp[4alpha b S + alpha sum_(r<k)h_r K_l max_i|q_(r,i)|].

For derivatives in the full xi row, take block-row norms in the exact recurrence and let M_j be the running maximum of preceding Jacobian row norms. This gives

    |J_k|row <=1+alpha sum_(j<k) h_j (N_j+4b) M_j.

The discrete product bound product_(j<k)[1+alpha h_j(N_j+4b)]<=E_k proves

    |partial_xi Y_k|row<=E_k.

For one reverse source slot zeta_j, its direct forcing of d_j is bounded by 2, its first effect on Y_k by 2alpha h_j, and all later effects obey the same Volterra recurrence. Therefore

    |partial_(zeta_j)Y_k|<=2alpha h_j E_k,   j<k,
    |partial_(zeta_j)X_k|<=4alpha h_j E_k,
    |partial_xi d_k|row<=(K_l max_i|q_(k,i)|+4b)E_k.     (III.S.4)

These are pointwise bounds on actual named derivatives.

For completeness, if ||Z||_p<=M sqrt(p) for all p>=2, expansion of exp(Z^2/(4 exp(1)M^2)) and k!>=(k/exp(1))^k gives expectation <=2. Young's inequality then gives, in particular,

    E exp(u|Z|)<=2 exp(2 exp(1)M^2 u^2),   u>=0.

Minkowski applied to the weighted time sum in E_k gives its p-norm <=S Msrc_l sqrt(p). Hence no temporal independence or path-maximum moment is needed. If

    alpha S b<=10^-9,   alpha S Msrc_l<=10^-6,

then

    E E_k <=4,
    [E E_k^2]^(1/2)
      <=sqrt(2) exp[4alpha b S+4 exp(1)alpha^2 S^2 Msrc_l^2].

Taking expectations in (III.S.4) and adding the learned contractions yields

    alpha_(l+1,new)<=3F^2+16alpha,
    b_(l-1,new)<=512(n_l+b)+3S.                          (III.S.5)

For the second bound the response row is at most

    sqrt(2)(sqrt(2)Msrc_l+4b)
       exp[4alpha b S+4 exp(1)alpha^2 S^2 Msrc_l^2]
       <512(n_l+b).

The forward learned density is <=3F^2. The reverse learned row is <=3S because ||d_l||_2<=1. All displayed norms bound the absolute values of signed response coefficients; no coefficient signs have been discarded from the actual identities.

#### III.S.5. Explicit depth-independent gain condition

Keep F=32^L and define

    n_l=3F(T/a)(32/a)^(L-l),   nmax=3FT/a,
    B0=nmax+3S<=4FT/a,
    alpha_l=32^l *3F^2,
    b_l=2048^(L-l+1) B0,   1<=l<=L.

Here alpha_l bounds Acal_l and b_l bounds the incoming Bcal_(l+1), so outgoing reverse production at layer l is compared with b_(l-1). The top row 3S and bottom density 3 lie strictly inside their respective radii. Exact algebra gives

    alpha_l S<=3(32768/a)^L T,
    alpha_l S b_l
       <=24576(67108864/a)^L 64^(-l) T^2/a
       <=384(67108864/a)^L T^2/a.

Since a>=10^12(1+T), L>=2, and l>=1, these imply

    alpha_l S<10^-8,
    alpha_l S b_l<10^-10,
    alpha_l S Msrc_l<10^-8.

For the second assertion one may bound by the L=2 case and use sup_(T>=0)T^2/(1+T)^3=4/27: the bound is <2.57*10^-19. Also n_l<=B0<=b_l/2048, so Msrc_l<=61b_l and the last assertion follows. The forward bracket in (III.S.3) is <=F+25alpha_l S+50alpha_l S b_l<=2F, because Q_l<=1/2 and K_l>=1.

Thus every production estimate is strictly inside the next box:

    3F^2+16alpha_l<=17alpha_l<32alpha_l=alpha_(l+1),
    512(n_l+b_l)+3S<514b_l<2048b_l=b_(l-1).              (III.S.6)

The constants do not require any upper bound on L, and e enters only through eps=e/a<=1.

#### III.S.6. Full chronological induction, without an unknown-current-row premise

Use the actual stage order at each time k:

    Acal_(2,k),...,Acal_(L,k),
    Bcal_(L,k),...,Bcal_(2,k).

The induction invariant is: every completed time row satisfies its alpha_l,b_l radius; its corresponding q_l fields satisfy (III.S.1)--(III.S.2); and the independent primal bounds of Section III.S.2 hold. At a partially completed current row, the radius bound is asserted only for coefficients already constructed.

At k=0 all forward response rows are empty. Wout_0=0, so the top backward field and its xi-derivative vanish. Thus Bcal_(L,0)=0, and successive reverse stages give zero current q and reverse responses down to layer 1. Named zero-variance slots are still retained formally. This starts the invariant.

At the next time k, the bottom Y_1,k is already determined by the initialized root and past d_1. Suppose current forward rows have been built through Acal_(l,k), so Y_l,k and X_l,k are available. To construct Acal_(l+1,k), the response derivative of X_l,k in zeta_l,j with j<k uses q_l,r and Bcal_(l+1,r) ONLY FOR r<k. This is an exact consequence of strictness of Acal_l: every occurrence of q in Y_l,k comes through d_l,r with r<k. Apply the local moment estimate to the fully completed prefix through k-1, then apply the source derivative recurrence at current k. The bound 4alpha_l h_j E_k and its expectation require only this past information. The learned contraction uses the already proved primal bounds. Consequently the first estimate of (III.S.5) constructs Acal_(l+1,k) strictly inside alpha_(l+1). No current Bcal_(l+1,k), q_l,k, or d_l,k estimate has been used. This closes all current forward rows in ascending order.

The current top incoming row is the readout integrator, already bounded by 3S. The current top q_L=Wout is now available. On the complete local prefix through k, all Acal_L and incoming Bcal_(L+1) rows are therefore known and satisfy their bounds. Sections III.S.3--III.S.4 now apply to this prefix and produce Bcal_(L,k) strictly inside b_(L-1). The current q_(L-1) is then available with this newly bounded incoming row. The same complete-prefix calculation produces Bcal_(L-1,k). Continue downward. At every reverse stage, the current Acal_l row was constructed in the forward sweep, and the current incoming Bcal_(l+1) row was constructed in the preceding higher reverse stage. Therefore every hypothesis is established before it is used. The final bottom q_1 estimate completes the invariant.

This proves the actual coefficient box and moment estimates on every finite mesh. It uses no minimum step length and never bootstraps a current unknown row from an estimate that assumes that row.

#### III.S.7. What this gives to the global proof

For every separately fixed finite L,a,T, the constructed incoming and forward fields have marginal subGaussian moments uniformly in mesh, cap, and the bounded deterministic controls. Their formal first source derivatives have integrable envelopes uniformly in mesh and cap. The elementary subGaussian tail consequence of (III.S.1) supplies constants M,c>0, possibly depending on the fixed L,a,T, such that

    sup_(R,k) ||q_(l,k,i) 1_(|q_(l,k,i)|>u)||_2
        <=M exp(-c u^2).

The fixed-cap Gaussian/Euler bridge passes these estimates to controlled capped population paths. Comparing an arbitrary larger cap with a reference cap R uses

    |D_(l,R')(y,q)-D_(l,R)(y',q')|
       <=2|q-q'|+2eps K_l R|y-y'|
                         +2eps |q'|1_(|q'|>R).

Forward discrepancies are controlled first. Backward substitution therefore introduces one factor R multiplying that forward discrepancy; it does not produce R^L. On any fixed controlled interval the raw difference estimate has the form C exp(CR-cR^2). It yields strong cap removal and uniqueness against any bounded-primal uncut competitor, as proved in full in Part III.V below. Measurable controls give a strong absolutely continuous controlled path and the equation almost everywhere; continuous autonomous residual feedback gives the required strong C1 physical path.

The finite random readout is not set to zero in either actual training algorithm: at fixed cap its initial RMS discrepancy is O_P(n^-1), propagated by fixed-cap raw Lipschitz stability. Only after this width limit is the population initialization Wout_0=0 used. The finite-depth true-kernel/velocity/path conclusions still require their ordered observation-truncation and time-compactness bridge, as proved in Part III.V below; the present source calculation does not silently replace that bridge.

### III.G. Uniform geometry, total control time, and all-time nonaffinity

Throughout this part \(F_*=32^L\) is a numerical norm bound, distinct
from the three normalized predictors \(F_i\). All estimates apply
at each separately fixed finite \(L\ge2\). The sufficient conditions
on \(a\) will not depend on \(L\).

#### III.G.1. The initialized Gram loses only a summable amount with depth

First we prove the elementary three-input geometric bound
\[
                  G+\mathbf1\mathbf1^T\succeq
                           \delta^2 I_3/4.                 \tag{III.G.1}
\]
For \(v\in\mathbb R^3\), the left quadratic form is
\((\sum v_i)^2+\|\sum v_iu_i\|^2\). If the nonzero \(v_i\) have
one sign, its first term is at least \(\|v\|^2\), which suffices
as \(\delta<1\). Otherwise change the overall sign and permute
to write \(v=(r_1,r_2,-b)\), \(r_1,r_2\ge0\), \(A=r_1+r_2>0\),
\(b>0\). Set
\[
 D=\frac{r_1(1-G_{13})+r_2(1-G_{23})}{A}
                         \in[\delta,2].
\]
Projection of \(\sum v_i u_i\) onto the unit vector \(u_3\)
gives the lower bound
\[
                    (A-b)^2+((1-D)A-b)^2.
\]
The matrix of this two-variable quadratic form has determinant
\(D^2\), trace \(D^2-2D+4\le4\), and positive eigenvalues.
Its smaller eigenvalue is at least determinant/trace, hence
\(\delta^2/4\). Finally \(A^2+b^2\ge r_1^2+r_2^2+b^2\).
This proves (III.G.1), without requiring an invertible \(G\).

At initialization the raw preactivation tuple at each layer is
centered Gaussian, with a common marginal standard deviation
\(\sigma_\ell\), where \(\sigma_1=1\) and
\(\sigma_{\ell+1}^2=E[\phi(\sigma_\ell G)^2]\).
This follows either directly by the forward-only case of Part III.F
or by conditioning each fresh Gaussian matrix on its inputs.
For a centered Gaussian tuple \(Z\) with equal marginal variance
\(\sigma^2\), Gaussian integration by parts gives
\[
 m_\sigma=E\phi(\sigma G)=a+eE\psi(\sigma G),\qquad
 \beta_\sigma=E\phi'(\sigma G)=a+eE\psi'(\sigma G).
\]
Its residual coordinates
\(\phi(Z_i)-m_\sigma-\beta_\sigma Z_i\) are orthogonal to
constants and every \(Z_j\). Indeed
\(E[Z_j\mid Z_i]=\operatorname{Cov}(Z_j,Z_i)Z_i/\sigma^2\);
this identity follows by subtracting the correlated linear
Gaussian component, and is valid for singular tuples. Integration
by parts against a Gaussian density proves the remaining
one-coordinate identity; linear growth makes its boundary term
zero. Consequently
\[
 (E[\phi(Z_i)\phi(Z_j)])_{ij}
 \succeq m_\sigma^2\mathbf1\mathbf1^T+
                   \beta_\sigma^2\operatorname{Cov}(Z).
                                                               \tag{III.G.2}
\]
In particular, \(m_\sigma,\beta_\sigma\ge a-e\ge a/2\), and
\[
 (a/2)^{\ell-1}\le\sigma_\ell\le4a^{\ell-1}.             \tag{III.G.3}
\]
For the lower bound use the diagonal of the linear projection
in (III.G.2). For the upper bound, Minkowski and \(|\psi|\le1\)
give \(\sigma_{\ell+1}\le a\sigma_\ell+2a\). Dividing by
\(a^\ell\) and summing the geometric series yields
\(\sigma_\ell/a^{\ell-1}\le1+2\sum_{j=0}^{\ell-2}a^{-j}
\le1+2a/(a-1)<4\) for \(a\ge4\).

A worst-case lower derivative bound at each layer would lose
a fixed factor at every layer. Boundedness of \(\psi\) improves
this estimate. Another integration by parts gives
\[
 |E\psi'(\sigma G)|=
       \frac{|E[G\psi(\sigma G)]|}{\sigma}\le\frac1{\sigma}.
                                                               \tag{III.G.4}
\]
Define \(d_\ell=a^{-1}(2/a)^{\ell-1}\). Let \(Q_\ell(0)\)
be the Gram of the normalized initialized features \(X_i^\ell\).
The normalized linear projection coefficient at layer \(\ell\)
is \(\beta_{\sigma_\ell}/a\ge1-d_\ell\); the normalized
constant coefficient at layer 1 is at least \(1-d_1\).
Equation (III.G.2), after dividing the feature Gram by \(a^{2\ell}\),
therefore gives
\[
 Q_1(0)\succeq(1-d_1)^2(G+\mathbf1\mathbf1^T),\qquad
 Q_\ell(0)\succeq(1-d_\ell)^2Q_{\ell-1}(0)\quad(\ell\ge2).
\]
For numbers in \([0,1]\), induction gives
\(\prod_{j=1}^m(1-d_j)\ge1-\sum_{j=1}^m d_j\). Since
\(\sum_{\ell\ge1}d_\ell=1/(a-2)\le1/2\), (III.G.1) proves
\[
                  Q_L(0)\succeq
             \tfrac14(G+\mathbf1\mathbf1^T)
                          \succeq\lambda I_3,\qquad
                  \lambda=\delta^2/16,                    \tag{III.G.5}
\]
uniformly in all finite depths.

#### III.G.2. Controlled primal estimates and their exact scale

Let \(\tau_R\) be an odd \(C^1\) clip, identity on \([-R,R]\),
with \(|\tau_R(q)|\le\min\{|q|,2R\}\), \(|\tau_R'|\le1\).
For example integrate a smooth even cutoff equal to one on
\([-R,R]\), between zero and one, and zero outside \([-2R,2R]\).
Set \(\epsilon=e/a\) and
\[
 D_{\ell,R}(Y,q)=q+\epsilon\psi'(K_\ell Y)\tau_R(q).
\]
The normalized controlled equations, for \(\|c(s)\|_1\le3\), are
\[
 \begin{split}
 (W^{(L+1)})'&=\sum_i c_iX_i^L,&
 w'&=\sum_i c_i d_i^1u_i,&
 (W^{(\ell)})'&=\sum_i c_i d_i^\ell\otimes X_i^{\ell-1},\\
 q_i^L&=W^{(L+1)},&q_i^\ell&=(W^{(\ell+1)})^*d_i^{\ell+1},&
 d_i^\ell&=D_{\ell,R}(Y_i^\ell,q_i^\ell).
 \end{split}                                                \tag{III.G.6}
\]
These use the raw metric. The cap acts only on the nonlinear
part of a backward gate. Its derivatives are bounded at fixed
\(R,L,a\), so Part III.F gives local controlled solutions.

Put \(S=T_0a^{-L}\) and stop at hidden raw displacement
\(\mathfrak D=1\). Then action norms are at most 11 and the
three first projection norms at most 2 (the looser bound 3
also suffices). Induction using
\(|\chi_\ell(Y)-Y|\le2/K_\ell\), \(|\chi_\ell'|\le2\), and
\(|D_{\ell,R}(Y,q)|\le2|q|\), gives
\[
 \|X_i^\ell\|_2\le32^\ell,\quad
 \|W^{(L+1)}(s)\|_2\le3F_*s,\quad
 \|q_i^\ell(s)\|_2\le32^{L-\ell}\|W^{(L+1)}(s)\|_2.
                                                               \tag{III.G.7}
\]
For the first step \(\|X_i^1\|\le3+2\le32\); each later
step is at most \(11\cdot32^{\ell-1}+2\le32^\ell\).
Backward action and gate growth is at most \(22\le32\).
Every hidden block speed is at most \(F_*\|W^{(L+1)}\|\): at a matrix
block its coefficient is at most
\(6\cdot32^{L-\ell}32^{\ell-1}=(3/16)F_*\), and the bottom
satisfies the same bound. There are \(L\) hidden blocks, so
\[
             \mathfrak D(s)\le3\sqrt L F_*^2s^2.           \tag{III.G.8}
\]
The factor 3 is deliberately larger than the integrated factor
\(3/2\). Positive Euler meshes obey the same estimate because
\(\sum_jh_js_j\le s_k^2/2\). Even the first proposed overshooting
node is bounded using only earlier stopped states, so the strict
bound \(\mathfrak D(S)<1/4\) proved below rules out overshooting.
This establishes (III.G.7)--(III.G.8) on the entire controlled interval,
independently of source estimates.

Here are the forward perturbation estimates relative to the
same initialized actions and roots. Write
\(\Delta Y_\ell=Y_\ell-Y_\ell(0)\) and similarly for \(X\).
The bottom norm is at most \(\mathfrak D\). At later layers
use
\[
 \Delta Y_\ell=(W^{(\ell)}-W^{(\ell)}_0)X_{\ell-1}
                               +W^{(\ell)}_0\Delta X_{\ell-1}.
 \]
Thus
\(\|\Delta Y_\ell\|\le32^{\ell-1}\mathfrak D+
20\|\Delta Y_{\ell-1}\|\). Summing this geometric recurrence
gives
\[
 \|\Delta Y_\ell\|\le3\cdot32^{\ell-1}\mathfrak D,\qquad
 \|\Delta X_\ell\|\le32^\ell\mathfrak D.                  \tag{III.G.9}
\]
Indeed the first coefficient is at most
\(\sum_{j\ge0}(20/32)^j=8/3<3\), and \(6<32\).
The bottom also satisfies both inequalities.
In raw preactivation coordinates this implies, for all
samples and \(\ell\le L\),
\[
 \|Z_i^\ell(s)-Z_i^\ell(0)\|_2
 \le a^{L-1}F_*\mathfrak D(S)
 \le d_L:=\frac{3\sqrt L T_0^2}{a}
                         \left(\frac{32768}{a}\right)^L.
                                                               \tag{III.G.10}
\]
The harmless factor \(3\cdot32^{\ell-1}\) in (III.G.9) is at
most \(32^L\); this explains the first inequality.

The top Gram perturbation has every entry bounded by
\(2F_*^2\mathfrak D\). Its operator norm is bounded by the
maximum absolute row sum, hence
\[
 \|Q_L(s)-Q_L(0)\|_{\rm op}
 \le6F_*^2\mathfrak D(S)
 \le18\sqrt L\left(\frac{2^{20}}{a^2}\right)^LT_0^2.
                                                               \tag{III.G.11}
\]
Let \(J_h:\mathcal P_h\to\mathbb R^3\) be the true normalized
hidden predictor differential and \(U_{h,R}:\mathbb R^3\to
\mathcal P_h\) the normalized capped hidden direction map.
Their individual sample/block factors are bounded by
\(F_*\|W^{(L+1)}\|\) using the same backward induction, also for the
true gate. Taking the finite sum of squared factor norms gives
\[
 \|J_h\|,\|U_{h,R}\|\le\sqrt{3L}F_*\|W^{(L+1)}\|,\qquad
 \|J_hU_{h,R}\|\le27L F_*^4 S^2.                         \tag{III.G.12}
\]
There is no assertion that \(J_hU_{h,R}\) is symmetric.

All required strict inequalities follow from the single
depth-independent condition \(a\ge10^{12}(1+T_0)\).
For completeness, if \(0\le q\le1/4\) then
\(Lq^L\le2q^2\) for \(L\ge2\): the consecutive ratio is
\((L+1)q/L\le3/8<1\). Also \(\sqrt L\le L\).
Use \(q=2^{20}/a^2\). The largest of (III.G.11) and (III.G.12)
is at most
\[
                  54\,2^{40}T_0^2/a^4<\lambda/4.         \tag{III.G.13}
\]
Indeed \(a\ge10^{12}T_0\) and \(T_0=12/\lambda\) make
this at most \( (54\,2^{40}/(144\cdot10^{48}))\lambda^2
<4.13\cdot10^{-37}\lambda^2<\lambda/4\).
Use \(q=1024/a^2\) in (III.G.8) to obtain
\(\mathfrak D(S)\le6\cdot2^{20}T_0^2/a^4<1/4\).
Consequently
\[
 Q_L(s)\succeq3\lambda I_3/4,\qquad
                \|J_hU_{h,R}\|<\lambda/4.                \tag{III.G.14}
\]
The same controlled bounds hold for every cap.

#### III.G.3. Capped physical paths and their finite total control time

The physical capped equations are
\[
             \dot\theta=-a^L\sum_i r_i\,\mathcal G_{i,R},
                                                               \tag{III.G.15}
\]
where \(\mathcal G_{i,R}\) has the normalized blocks in (III.G.6) with
unit control \(c_i=1\). Its readout block is \(X_i^L\).
Define the accumulated control time
\[
                    v(t)=a^L\int_0^t\|r(s)\|_1\,ds.
                                                               \tag{III.G.16}
\]
On portions where \(r\ne0\), reparametrization by \(v\)
turns (III.G.15) into (III.G.6) with \(c=-r/\|r\|_1\), of norm one.
If \(r=0\), the whole capped field is zero; fixed-cap uniqueness
makes its continuation stationary. Equivalently the integral
controlled estimates apply directly with the measure
\(dv=a^L\|r(t)\|_1dt\), so no inverse at zero is required.

While \(v\le S\), the scalar chain rule in Part III.F gives the
exact residual equation
\[
                  \dot r=-a^{2L}(Q_L+J_hU_{h,R})r.
                                                               \tag{III.G.17}
\]
Its readout term is the true positive Gram even under a cap.
Using the absolute operator bound for its possibly nonsymmetric
hidden term, (III.G.14) implies
\[
 \frac d{dt}\|r\|_2^2\le-\lambda a^{2L}\|r\|_2^2,\qquad
 \|r(t)\|_2\le\sqrt3 e^{-\lambda a^{2L}t/2}.             \tag{III.G.18}
\]
Here \(r(0)=-y\), since the population readout is zero.
Therefore
\[
 v(t)\le a^L\sqrt3\int_0^\infty
                  \sqrt3e^{-\lambda a^{2L}s/2}\,ds
        =\frac6{\lambda a^L}=\frac S2.                    \tag{III.G.19}
\]
This rules out a first exit at \(v=S\). A finite physical
endpoint has bounded raw speed by (III.G.7) and (III.G.15);
its state is strongly Cauchy there, and fixed-cap local
existence continues it. Thus all capped population paths
are global, with (III.G.7)--(III.G.19) independent of cap and horizon.

To apply Part III.S's Euler source estimates to these paths without
an implicit limit assumption, fix a cap and bounded deterministic
control on \([0,S]\). For a step-function control, fixed-cap
Euler convergence follows separately on its finitely many
constant intervals from Part III.F. For a general measurable bounded
control, choose bounded step controls converging in \(L^1\);
they exist by approximating each integrable coordinate by
simple interval step functions, and projecting onto the closed
\(\ell^1\) ball if needed. The integral difference of the fields
is bounded by \(C\|c-\bar c\|_{L^1}\), in addition to a
fixed-cap Lipschitz state term. Gronwall gives uniform strong
convergence of controlled paths. For each fixed time, an
almost-sure subsequence and Fatou pass Part III.S's moment bounds.
This argument does not sample an arbitrary measurable control
at Euler nodes. In particular it applies to the deterministic
control extracted from any capped population physical path.
The uniform result of Part III.S is
\[
 \sup_{R,t\ge0,\ell,i}\|q_{R,i}^\ell(t)\|_p
                            \le M_*\sqrt p,\qquad p\ge2, \tag{III.G.20}
\]
where \(M_*<\infty\) may depend on fixed \(L,a,\delta\) but
not on cap or physical time. The total interval is always
the same \([0,S]\). These are the sole nonclassical inputs
to cap removal, and Part III.S proves them explicitly.

Part III.V now applies: its one-cap-factor comparison uses
(III.G.20) only on the capped reference, constructs a strong
uncut limit, and proves uniqueness, restart and all actual
finite GF/GD and observation limits. Its fixed-cap
approximations depend only on the already established capped
paths and controlled moments, so the order is not circular.
The bounds (III.G.14), (III.G.18), (III.G.19) pass by strong convergence
to the uncut path and prove (III.M.15).

#### III.G.4. Persistent nonaffinity for one activation at every depth

For a square-integrable real variable \(X\), define
\[
 \mathcal R_\psi(X)=\inf_{b,c\in\mathbb R}
                             E[(\psi(X)-b-cX)^2].
\]
The following stability estimate avoids any variance lower
bound:
\[
 \left|\sqrt{\mathcal R_\psi(X)}
           -\sqrt{\mathcal R_\psi(\widetilde X)}\right|
                            \le2\|X-\widetilde X\|_2.     \tag{III.G.21}
\]
To prove it, if \(\operatorname{Var}X>0\), the optimal slope is
\(c_X=\operatorname{Cov}(X,\psi(X))/\operatorname{Var}X\).
For an independent copy \(X'\), the covariance numerator is
\(\tfrac12 E[(X-X')(\psi(X)-\psi(X'))]\), while the denominator
is \(\tfrac12E[(X-X')^2]\). Since \(\psi\) is 1-Lipschitz,
\(|c_X|\le1\). If \(X\) is constant choose \(c_X=0\) and
the matching intercept. Test the optimal affine fit for \(X\)
as a competitor for \(\widetilde X\), on the given coupling:
the difference of its residuals is at most
 \(2|X-\widetilde X|\). The triangle inequality gives one
direction of (III.G.21); interchanging the variables gives the
other. The best fit exists because the span of \(1,X\) is
finite dimensional and closed; the displayed covariance
calculation also constructs it.

There exists an \(r_\psi\) in (III.M.3). Otherwise \(\psi\) is
affine on every \([-r,r]\) for integer \(r\), since this
finite-dimensional affine subspace is closed in its interval
\(L^2\). Continuity makes each such equality pointwise.
Overlapping intervals force the same two affine coefficients,
so \(\psi\) is affine on \(\mathbb R\), and boundedness would
make it constant, a contradiction. The interval residual is
explicitly
\[
 J_\psi=\int_{-r}^{r}\psi(x)^2dx
       -\frac{(\int_{-r}^{r}\psi(x)dx)^2}{2r}
       -\frac{3(\int_{-r}^{r}x\psi(x)dx)^2}{2r^3}.
                                                               \tag{III.G.22}
\]
For \(\sigma\ge1\), its Gaussian density on \([-r,r]\) is
at least \(e^{-r^2/2}/(\sigma\sqrt{2\pi})\). Restricting
the regression integral to this interval proves
\[
                      \mathcal R_\psi(\sigma G)
                                      \ge c_\psi/\sigma.
                                                               \tag{III.G.23}
\]
In particular \(c_\psi\le\mathcal R_\psi(G)\le1\).
By (III.G.3), at every layer of a depth \(L\) network,
\[
         \mathcal R_\psi(Z_i^\ell(0))
                       \ge\eta_L:=c_\psi/(4a^{L-1}).     \tag{III.G.24}
\]

The raw displacement in (III.G.10) is smaller than
\(\sqrt{\eta_L}/4\) simultaneously for every \(L\ge2\).
Here is the explicit check. The ratio is at most
\[
 \frac{24\sqrt L T_0^2}{\sqrt{c_\psi}a^{3/2}}
                    \left(\frac{32768}{\sqrt a}\right)^L.
\]
The first bound in (III.M.4) ensures
\(q=32768/\sqrt a\le1/2\). For \(L\ge2\),
\(\sqrt L q^L\le2q^2\): the ratio of consecutive terms is
at most \(\sqrt{3/2}/2<1\) and the initial coefficient is
\(\sqrt2\le2\). Thus the displayed ratio is at most
\[
 \frac{3\cdot2^{34}T_0^2}{\sqrt{c_\psi}a^{5/2}}
                         \le\frac34<1                  \tag{III.G.25}
\]
by the second bound in (III.M.4). Apply (III.G.21) to the common-space
coupling of a trained preactivation and its own initialization.
Equations (III.G.10), (III.G.24)--(III.G.25) give
\(\mathcal R_\psi(Z_i^\ell(t))\ge\eta_L/4\).
Adding the affine part of \(\phi\) to a regression target has
no effect on its residual, and multiplying its nonaffine part
by \(e\) multiplies the residual by \(e^2\). Hence
\[
 \mathcal R_\phi(Z_i^\ell(t))
   =e^2\mathcal R_\psi(Z_i^\ell(t))
                       \ge e^2c_\psi/(16a^{L-1}),
\]
as claimed. This holds first for every capped path, then for
the uncut path by (III.G.21) and strong cap convergence.

Parts III.F, III.S, III.G and III.V prove statements 1, 2 and the regression
portion of statement 3 of Theorem III.M.1. Part III.N proves the
remaining motion and kernel assertions with only \(a>e>0\),
which the selected constants satisfy.

### III.V. Population and finite-algorithm bridge at each fixed depth

Fix a finite hidden depth L>=2 and the activation parameters already selected by the theorem. All constants in this part may depend on this fixed L, a, e, dataset, and physical observation horizon T. Such dependence does not enter the selection of a,e. Write

    K_l=a^(l-1), eps=e/a,
    chi_l(y)=y+[1+eps psi(K_l y)]/K_l,
    g_l=chi_l',
    D_(l,R)(y,q)=q+eps psi'(K_l y)tau_R(q).

For each fixed l the functions g_l and g_l' are bounded and continuous. The clipped coordinate map has bounded continuous first derivatives, with

    |g_l|<=2, |g_l'|<=eps K_l,
    |D_(l,R)|<=2|q|, |D_q|<=2, |D_y|<=2eps K_l R.       (III.V.1)

No sign restriction is imposed on psi' or psi''.

We use the normalized hidden fields Y_l=Z_l/a^(l-1), X_l=H_l/a^l. The raw matrices and original readout Wout are unchanged. At the bottom, w=sqrt(d)V^(1) and u_i=x_i/sqrt(d) are an isometric notational representation of the original bottom metric: (d/n)||Delta V^(1)||_F^2=(||Delta w||_F^2/n). Put

    Y_(1,i)=<w,u_i>,
    Y_(l,i)=W_l X_(l-1,i), X_(l,i)=chi_l(Y_(l,i)),
    f_i=a^L<Wout,X_(L,i)>, p_i=a^L(y_i-f_i).

The physical capped raw vector field is exactly

    V_(R,Wout)=sum_i p_i X_(L,i),
    V_(R,W_l)=sum_i p_i delta_(l,i) tensor X_(l-1,i),
    V_(R,w)=sum_i p_i delta_(1,i)u_i,                      (III.V.2)

where

    q_(R,L)=Wout,
    delta_(R,l)=D_(l,R)(Y_l,q_(R,l)),
    q_(R,l)=W_(l+1)^*delta_(R,l+1), l<L.

Thus physical time is used throughout this part. The factor a^L is in p, not in a replacement metric or training step. Reserve b_l=g_l(Y_l)t_l, t_L=Wout, t_l=W_(l+1)^*b_(l+1), for the TRUE normalized backward fields, even when they are observed at a capped state. The original raw backward fields equal a^(L-l+1)b_l.

We use the Hilbert raw norm on the first vector block, all Hilbert--Schmidt increments, and Wout. On finitely many blocks it is equivalent to their sum norm, which may be used in estimates by altering constants. Every comparison below takes place either at the same width with identical initialization or on the common population spaces. No cross-width identification of operators is used.

#### III.V.1. Exact inputs and dependency order

The following results have been proved earlier and are the only inputs to this part.

(F) Every fixed finite Gaussian program with independent initialized adjacent matrices, both orientations, independent root tuples, C1 coordinate maps with bounded continuous derivatives, and causal scalar contractions has full-sequence within-layer empirical W2 convergence, including all second moments. An initialized forward query on h has the scalar representation

    xi_h + sum_v v E[partial_(zeta_v) h],                 (III.V.3)

where v ranges over preceding reverse inputs to that matrix. Its reverse rule includes the current forward inputs. Gaussian source covariances are the full actual input Grams; distinct oriented groups are independent. Named slots are differentiated separately at singular covariance, with all coefficients, contractions, controls, and covariances frozen. The construction is continuous under bounded-derivative finite query perturbations, by positive-semidefinite covariance-square-root coupling. The common initialized action norms are <=10 and their reverses are their genuine adjoints. The finite norm event has probability tending to one. These conclusions apply to any finite number of adjacent matrices because their conditioning proof counts instructions rather than layers.

(G) The capped population physical paths are global. First projections, current action norms, Wout, and physical raw directions have bounds independent of cap on compact horizons. The paths stay in a common primal ball with strict continuation slack.

(S) The direct controlled source estimate and residual-clock bound give, for some M_* and every p>=2,

    sup_(R,t,l,i) ||q_(R,l,i)(t)||_p <= M_* sqrt(p).       (III.V.4)

Here L,a,e are fixed. This includes q_L=Wout, uses the actual capped incoming fields, and has already been transferred from controlled Euler programs to physical capped paths. It does not replace the actual residuals by prescribed controls in training.

The chain and adjunction rules from the foundations apply to bounded g_l and to bounded-action curves with Hilbert--Schmidt derivatives.

The proof order below is deliberate. Raw cap removal uses only (G),(S). Fixed-cap Euler bounds and fixed-mesh primary Gaussian laws supply finite primal events before Gaussian probe estimates use them. Probe estimates supply pointwise source rows; these justify appended velocity queries. Only then are uniform-time empirical velocity laws proved. True backward observations require a separate finite truncation argument. Finally same-width cap comparison transfers everything to actual uncut algorithms.

#### III.V.2. One-cap-factor comparison and population cap removal

On a fixed primal ball, forward propagation gives

    sum_(l,i)(||Y_l-Ybar_l||_2+||X_l-Xbar_l||_2)
       +sum_i|p_i-pbar_i| <= C||Theta-Thetabar||raw.       (III.V.5)

The bottom projection is bounded. Each upper step uses

    W_l X_(l-1)-Wbar_l Xbar_(l-1)
       =(W_l-Wbar_l)X_(l-1)+Wbar_l(X_(l-1)-Xbar_(l-1)),

||W_l-Wbar_l||op<=||W_l-Wbar_l||HS, and the Lipschitz constant of chi_l. The residual estimate follows by expanding the Wout,X_L inner product. For rank-one blocks,

    ||u tensor v-ubar tensor vbar||HS
       <=||u-ubar||_2||v||_2+||ubar||_2||v-vbar||_2.       (III.V.6)

For R'>=R, including infinity,

    |D_(l,R')(y,q)-D_(l,R)(ybar,qbar)|
       <=2|q-qbar|+2eps K_l R|y-ybar|
                       +2eps |qbar|1_(|qbar|>R).         (III.V.7)

To prove it, first change q inside D_(l,R'), costing 2|q-qbar|. Split the remaining perturbation into

    eps[psi'(K_l y)-psi'(K_l ybar)]tau_R(qbar)
      +eps psi'(K_l y)[tau_(R')(qbar)-tau_R(qbar)].

The first term uses |psi''|<=1 and |tau_R|<=2R; the second vanishes for |qbar|<=R and otherwise has absolute value <=2eps|qbar|.

Here is the full depth recursion. Write alpha=||Theta-Thetabar||raw and E_l=||delta_(R',l)-delta_(R,l)(Thetabar)||_2, maximizing over samples. At the top, (III.V.7) gives E_L<=C(1+R)alpha+C Tail_L. At the next level,

    ||q_(R',l)-q_(R,l)(Thetabar)||_2<=C alpha+C E_(l+1),
    E_l<=2C E_(l+1)+C(1+R)alpha+C Tail_l.

Solving this finite downward recursion yields

    sum_l E_l <= C(1+R)alpha+C sum_l Tail_l.

Each new R multiplies a forward difference in (III.V.5), never E_(l+1). Using (III.V.6) and the actual residual difference therefore gives

    ||V_(R')(Theta)-V_R(Thetabar)||raw
       <=C(1+R)||Theta-Thetabar||raw
                     +C sum_(l,i)||qbar_(R,l,i)1_(|qbar_(R,l,i)|>R)||_2.
                                                               (III.V.8)

The same bound controls all backward discrepancies. Its tail terms belong only to the reference.

From (III.V.4), Markov's inequality with moment exponent p=(u/(3M_*))^2, for u large, gives

    sup_(R,t,l,i)||q_(R,l,i)1_(|q_(R,l,i)|>u)||_2
                    <=C exp(-c u^2).                     (III.V.9)

Indeed E[q^2 1_(|q|>u)]<=u^2(M_*sqrt(p)/u)^p, and the polynomial prefactor can be absorbed into a smaller exponential rate. Integrating (III.V.8) and applying its iterated integral inequality yields

    sup_(t<=T)||Theta_(R')(t)-Theta_R(t)||raw
      +sup_(t<=T)||V_(R')(Theta_(R')(t))-V_R(Theta_R(t))||raw
                        <=C_T exp(C_T R-cR^2).           (III.V.10)

The second term follows by substitution in (III.V.8), absorbing factors 1+R. Paths and raw derivatives are uniformly Cauchy. Their limits satisfy the integral equation Theta(t)=Theta(0)+integral_0^t V(s)ds, with continuous V, and (III.V.8) against the limit state identifies V=V_infty(Theta). Hence the limit is a strong C1 raw solution. Integer caps and horizons give a single consistent global construction.

Any bounded-primal strong uncut competitor is compared with the same capped reference by (III.V.8). Its primal bound changes C_T, but no competitor tail is used. The resulting error still vanishes as R tends to infinity. At a reached time t_0 the initial discrepancy from the capped reference is already bounded by (III.V.10); another exp(C_TR) factor leaves a vanishing error. This proves uniqueness and unique continuation from each reached state, without asserting arbitrary-state local Lipschitzness of the uncut field.

#### III.V.3. Raw Euler bounds and finite primal events, before source estimates

For fixed R and a larger primal ball, (III.V.1),(III.V.5),(III.V.6) make V_R locally Lipschitz with width-independent constants M_0,L_0. The autonomous Euler local defect is <=L_0M_0 h_j^2/2. The error recursion gives

    max_k||Theta_R(t_k)-Theta_R^pi(t_k)||raw
       <=(L_0 M_0 T/2)exp(L_0 T)|pi|.                    (III.V.11)

Raw interpolation adds <=2M_0|pi|. Stop at the boundary of the larger ball, choose |pi| sufficiently small, and the strict slack excludes first exit. This proves bounded population Euler arrays without source or velocity estimates.

At a fixed auxiliary mesh, (F) gives every primary finite node law and contraction. Exact rank unrolling gives

    max_k||W_(l,k,n)||op
       <=||W_(l,0,n)||op
          +sum_(j,b)h_j|p_(j,b,n)|
                          (||delta_(l,j,b,n)||_2/sqrt(n)) (||X_(l-1,j,b,n)||_2/sqrt(n)).
                                                               (III.V.12)

The sum is finite. Every summand converges to its population counterpart, whose total is bounded by the population primal and direction bounds, uniformly over the sufficiently fine meshes in (III.V.11). First-layer and readout norms converge too; include the full first-layer Gaussian root vector in the fixed program when its norm is needed. Thus, at each fixed sufficiently fine mesh, a deterministic enlarged finite primal ball with slack contains all finite coarse nodes and interpolants with probability tending to one. This argument uses no velocity or source-row estimate.

The actual finite initialization has (||Wout_(0,n)||_2/sqrt(n))=O_P(n^-1), since E(||Wout_(0,n)||_2^2/n)=n^-2. For fixed cap and transcript, compare it to a same-matrix auxiliary Euler program with zero readout root. Stopped finite-step Lipschitz stability propagates this vanishing norm, and the preceding slack closes the comparison. Thus the actual fixed-program limit has Wout_0=0. Every actual finite GF/GD and every same-width reference comparison below retains the original random Wout_(0,n); no algorithm is reset.

#### III.V.4. Fixed-cap response rows by Gaussian probes

Fix R,T and a sufficiently fine physical Euler mesh. Freeze p, all contractions, covariances, and response coefficients in formal source derivatives. The exact primary source equations are

    Y_(1,k,i)=Y_(1,0,i)+sum_(j<k,b)h_j p_(j,b)G_(ib)delta_(1,j,b),
    Wout_k=sum_(j<k,b)h_j p_(j,b)X_(L,j,b),

    Y_(l,k,i)=xi_(l,k,i)
                      +sum_(j<k,b)Acal_(l,ki,jb)delta_(l,j,b),
    q_(l-1,k,i)=zeta_(l-1,k,i)
                      +sum_(j<=k,b)Bcal_(l,ki,jb)X_(l-1,j,b),
                                                               (III.V.13)

for 2<=l<=L, where

    Acal_(l,ki,jb)
       =E partial_(zeta_(l-1,j,b))X_(l-1,k,i)
                         +h_j p_(j,b)E[X_(l-1,k,i)X_(l-1,j,b)],
    Bcal_(l,ki,jb)
       =E partial_(xi_(l,j,b))delta_(l,k,i)
             +1_(j<k)h_j p_(j,b)E[delta_(l,k,i)delta_(l,j,b)].
                                                               (III.V.14)

They retain every current transpose return. Source variances are bounded by the primal norms of their actual inputs.

Choose one oriented answer family and a fresh independent standard Gaussian vector g in its answer layer. Add epsilon alpha_(j,b)g, |alpha_(j,b)|<=1, at selected answer slots and recompute all subsequent residuals and raw updates. On the enlarged ball the raw discrepancy satisfies

    E_(k+1)<=(1+Ch_k)E_k+Ch_k|epsilon| (||g||_2/sqrt(n)).           (III.V.15)

Thus arbitrary bounded forcing at every time gives E_k<=C|epsilon| (||g||_2/sqrt(n)). A single forcing at time j gives <=Ch_j|epsilon| (||g||_2/sqrt(n)) at all later states. Current query errors have the direct O(|epsilon|) term; strictly later queries have the O(h_j|epsilon|) term. These estimates follow from (III.V.1),(III.V.5),(III.V.6) and include the recomputed residuals. For small fixed epsilon, first-exit and the finite primal event of Section III.V.3 keep this perturbed fixed program in the enlarged ball with probability tending to one.

Let V_k be a selected scalar primary output. At fixed mesh and epsilon, (F) passes (<g,V_(k,n)^epsilon>/n) to E[G V_k^epsilon]. The scalar G is independent of all oriented source groups and original roots. With deterministic coefficients frozen, its only explicit occurrences are the answer additions. Gaussian integration by parts gives

    E[G V_k^epsilon]
        =epsilon sum_(j,b)alpha_(j,b)
                              E partial_(eta_(j,b))V_k^epsilon.    (III.V.16)

At this fixed transcript the expression has bounded first derivatives and linear growth, so the Gaussian boundary term vanishes and differentiation is integrable. Its expected named derivatives converge as epsilon tends to zero: chronologically couple all finite covariance matrices by their positive square roots; earlier inputs and contractions converge in L2; continuous first derivatives with finite deterministic bounds on a compact coefficient neighborhood pass their expectations by dominated convergence. This uses no covariance derivative or inverse.

The unperturbed (<g,V_(k,n)^0>/n) tends to zero: conditionally its variance is (||V_(k,n)^0||_2^2/n)/n. Cauchy--Schwarz and (III.V.15), followed by width then epsilon limits in (III.V.16), give

    |sum_(j,b)alpha_(j,b)E partial_(eta_(j,b))V_k|<=C.

Choose the deterministic signs of the expected derivatives. A single strictly past insertion gives Ch_j instead. Together with the learned contractions in (III.V.14), this proves

    |Acal_(l,ki,jb)|<=Ch_j (j<k),
    |Bcal_(l,ki,jb)|<=Ch_j (j<k),
    |Bcal_(l,ki,kb)|<=C.                                  (III.V.17)

This bounds absolute EXPECTED derivative rows; it has not replaced |E partial V| by E|partial V|.

The current reverse rows have an explicit descending recursion. Put N_(l,k,i)=D_y(Y_(l,k,i),q_(l,k,i)), V_(l,k,i)=D_q(Y_(l,k,i),q_(l,k,i)), and set Bcal_(L+1,ki,kb)=0 for the readout integrator. Then

    Bcal_(l,ki,kb)
      =1_(i=b)E N_(l,k,i)
       +Bcal_(l+1,ki,kb) E[V_(l,k,i)g_l(Y_(l,k,b))],       (III.V.18)

for l=L,L-1,...,2. Indeed the current Y_l has derivative identity in its own current xi_l, while all strictly past corrections have zero current derivative. Differentiate q_l's current return and then its gate. At the top Wout_k uses strictly past X_L, so its current xi derivative is zero. Formula (III.V.18) starts there and keeps the exact signed current returns at every lower level.

#### III.V.5. Pointwise source rows and primary moments

Within layer l let R_l(H) be the sum of absolute derivatives in all primary named sources in that layer through the final mesh time, including its initial root coordinates if desired. Those families are xi_l for l>=2 and zeta_l for l<L; future derivatives vanish. Freeze all coefficients. Using (III.V.13),(III.V.17), coordinate differentiation gives, with maxima over the three samples understood,

    Z_(1,k)<=C+C sum_(j<k)h_j D_(1,j),
    Z_(l,k)<=1+C sum_(j<k)h_j D_(l,j), l>=2,
    H_(l,k)<=2 Z_(l,k),
    Woutpartial_k<=C sum_(j<k)h_j H_(L,j),
    Q_(l,k)<=1+C H_(l,k)+C sum_(j<k)h_j H_(l,j), l<L,
    D_(l,k)<=C_R Z_(l,k)+2Q_(l,k), l<L,
    D_(L,k)<=C_R Z_(L,k)+2Woutpartial_k.                      (III.V.19)

Here Z,H,Q,D denote the corresponding pointwise derivative-row seminorms, not primal values. Every same-time reverse term is a forward field already defined at that time; there is no algebraic same-time loop. Let U_k be the maximum of Z_(l,k) and Woutpartial_k. The last four lines bound the other fields by C(1+U_k+sum_(j<k)h_j U_j). Substitute into the first lines and use

    sum_(j<k)h_j sum_(r<j)h_r U_r
       <=T sum_(r<k)h_r U_r.

It follows that U_k<=C+C sum_(j<k)h_j U_j, hence U_k<=C exp(CT). Returning to (III.V.19) proves a deterministic bound

    R_l(H_(k,i))<=C_(R,T)                                  (III.V.20)

for every primary scalar field, uniformly over all sufficiently fine meshes and times.

Replace these derivative seminorms by Lp norms in the same inequalities. Direct Gaussian sources and roots have norms <=C sqrt(p); chi_l has linear growth and D_(l,R) is bounded by 2|q|. Minkowski and the same discrete inequality give

    sup_(pi,k,l,i)||H_(k,i)||_p<=C_(R,T)sqrt(p), p>=2,       (III.V.21)

for all primary fields and Wout. No temporal independence or Lp operator estimate for an initialized matrix has been used.

#### III.V.6. Ascending velocity queries, with complete induction and nested truncation

At a physical Euler node let P_(l,i),U_(l,i) denote the instantaneous normalized preactivation and feature velocities in direction V_R(Theta_k). Exactly,

    P_(1,k,i)=sum_b p_(k,b)G_(ib)delta_(1,k,b),
    U_(l,k,i)=g_l(Y_(l,k,i))P_(l,k,i),
    P_(l,k,i)=sum_b p_(k,b)delta_(l,k,b)
                                E[X_(l-1,k,b)X_(l-1,k,i)] + J_(l,k,i),
    J_(l,k,i)=W_(l,k)U_(l-1,k,i),  2<=l<=L.                (III.V.22)

The feature multiplier is the TRUE derivative g_l, even for a capped update direction. Append all W_(2,0) velocity queries after the complete primary transcript, then all W_(3,0) queries, and continue up to W_(L,0). No appended query feeds training. At level l, the only preceding opposite-orientation inputs for W_l are the primary delta_l fields; earlier appended levels use different matrices, and other level-l velocity queries use the same forward orientation. The source formula therefore is

    J_(l,k,i)=gamma_(l,k,i)
                       +sum_(j<=k,b)Ecal_(l,ki,jb)delta_(l,j,b),
    Ecal_(l,ki,jb)
       =E partial_(zeta_(l-1,j,b))U_(l-1,k,i)
          +1_(j<k)h_j p_(j,b)E[X_(l-1,j,b)U_(l-1,k,i)].    (III.V.23)

The new forward source gamma_l has covariance with every source of the same orientation equal to the inner product of their actual query inputs, and variance ||U_(l-1,k,i)||_2^2. It is a distinct named argument; its formal derivative in primary zeta_l is zero even if same-family covariance is singular. Sources later than time k have zero derivatives in the time-k input, despite the appended ordering.

Here is the induction invariant before constructing layer l's new action: all lower velocity observations have their joint finite empirical W2 laws, their exact formulas (III.V.23), Lp bounds <=C sqrt(p), and pointwise bounds

    R_(zeta_(m)) P_(m,k,i)<=C,
    R_(zeta_(m)) U_(m,k,i)<=C(1+|P_(m,k,i)|), m<l,        (III.V.24)

where only the primary transpose sources of the indicated layer are differentiated. For the bottom, (III.V.20)--(III.V.22) give the first inequality, and the exact scalar derivative

    partial_eta[g_m(Y_m)P_m]
        =g_m'(Y_m)P_m partial_eta Y_m
                           +g_m(Y_m)partial_eta P_m       (III.V.25)

gives the second. Primary moments (III.V.21) give the base Lp bound.

Assume the invariant through l-1. Its second inequality has an integrable envelope, so the total expected response row in (III.V.23) is bounded by C. Cauchy--Schwarz bounds the learned row by C sum_j h_j<=CT. The actual L2 norm of U_(l-1), already known before the new action, bounds gamma_l's variance. The formula (III.V.23), Gaussian moments, (III.V.21), and Minkowski then give

    sum_(j<=k,b)|Ecal_(l,ki,jb)|<=C,
    ||J_(l,k,i)||_p+||P_(l,k,i)||_p+||U_(l,k,i)||_p
                              <=C sqrt(p).               (III.V.26)

Differentiate (III.V.23) only in the primary zeta_l coordinates: all coefficients are frozen and gamma_l has derivative zero. By (III.V.20) the derivative row of the sum is bounded by the coefficient-row bound times C. The explicit first term in P_l in (III.V.22) is a deterministic linear combination of primary delta_l, so its row is also bounded by C. This proves the first part of (III.V.24) for m=l. Applying (III.V.25) proves its second part. This establishes precisely the invariant needed for the next matrix. Constants may increase with the fixed number of layers; the argument does not assume a future-layer moment estimate.

The formulas just used must be justified before unbounded products enter (F). Replace each multiplier product by g_m(Y_m)tau_M(P_m). It is a bounded-derivative instruction, and its exact named derivative is

    g_m'(Y_m)tau_M(P_m)partial_eta Y_m
             +g_m(Y_m)tau_M'(P_m)partial_eta P_m.          (III.V.27)

At the first action its derivative row is bounded independently of M by C(1+|P_1|), integrable by the already-proved primary bound. Thus (F) applies for fixed M, and the row and moment estimates in (III.V.26) hold independently of this observation cap. Dominated convergence as M tends to infinity identifies every expected coefficient in (III.V.23). Input L2 convergence and bounded initialized actions identify the actual untruncated query; its covariance converges by second-moment convergence and is coupled by covariance square roots.

For clarity, empirical removal uses only second moments. If (Z_n,P_n) converge under an L2 coupling to (Z,P), then

    ||g(Z_n)P_n-g(Z)P||_2
       <=||g||infty||P_n-P||_2+||[g(Z_n)-g(Z)]P||_2 ->0.  (III.V.28)

For the second term split at |P|<=M: that part is <=Lip(g)M||Z_n-Z||_2, and the remaining part is <=2||g||infty||P1_(|P|>M)||_2. Take n first, then M. The positive-part tail functional T_M(P)=||(|P|-M)_+||_2 is 1-Lipschitz under L2 coupling, and |P|1_(|P|>2M)<=2(|P|-M)_+. Consequently fixed-program W2 convergence makes the empirical input clipping error vanish in the width-then-cap order. Bounded action norms transfer it to the output error.

At a general new level l, retain all previous inner observation caps and one outer cap M in g_(l-1)(Y)P_(l-1). At fixed caps, (F) applies to the entire finite appended program. First remove the previously constructed inner caps while M stays fixed. The established lower-level formulas have convergent deterministic coefficients and covariance-square-root couplings, so the rows of P_(l-1) in the relevant primary zeta_(l-1) coordinates converge in probability and remain bounded, by their expression as bounded rows of primary delta. Formula (III.V.27) at fixed M therefore passes expected derivatives by dominated convergence. Formula (III.V.28) and bounded actions pass the corresponding L2 inputs and outputs. Now remove M. The envelope C(1+|P_(l-1)|) from the already established invariant is integrable and independent of M, so dominated convergence gives the untruncated expected response coefficients. The empirical error is removed by the positive-part tail argument. This is the induction step giving both the derivative-valid formula and its joint empirical law. It does not invoke (F) directly for the unbounded product or assume derivative convergence from W2 alone.

The induction reaches L and proves fixed-cap, mesh-uniform marginal C sqrt(p) bounds for every P_l,U_l. All same-family time/sample/source covariances are retained in any finite concatenation of these observations.

#### III.V.7. Deterministic velocity comparison and fixed-cap time limits

For states Theta,Thetabar on one primal ball and raw directions v,vbar in a bounded direction ball, put alpha=||Theta-Thetabar||raw, beta=||v-vbar||raw. Define P_1=v_w u_i, U_l=g_l(Y_l)P_l, and P_l=v_(W_l)X_(l-1)+W_l U_(l-1). Then, for M>=1,

    sum_(l,i)(||P_l-Pbar_l||_2+||U_l-Ubar_l||_2)
      <=C[beta+(1+M)alpha+sum_(l,i)T_M(Pbar_(l,i))].      (III.V.29)

To verify the exact depth recurrence, the bottom P-error is <=C beta. At every upper layer expand

    P_l-Pbar_l=(v_(W_l)-vbar_(W_l))X_(l-1)
       +vbar_(W_l)(X_(l-1)-Xbar_(l-1))
       +(W_l-Wbar_l)Ubar_(l-1)+W_l(U_(l-1)-Ubar_(l-1)).

Its norm is <=C(alpha+beta+||U_(l-1)-Ubar_(l-1)||_2). Moreover

    ||U_l-Ubar_l||_2
       <=2||P_l-Pbar_l||_2+C M||Y_l-Ybar_l||_2
                                         +4T_M(Pbar_l).

The last line follows by clipping Pbar_l at M and using bounded g_l,g_l'. Solve these two finite recurrences upward, using (III.V.5). Each new M multiplies a forward discrepancy already bounded by C alpha, so there is one M. The constant depends only on the fixed activation and the primal/direction ball, and is independent of R,M.

If ||P||_4<=C, then T_M(P)<=C^2/M. Apply (III.V.29) with the Euler node as reference, (III.V.11), the fixed-cap raw Lipschitz bound, and Section III.V.6 moments. Choosing M=|pi|^(-1/2) gives uniform population hidden-velocity error <=C_(R,T)sqrt(|pi|) between the instantaneous Euler node velocities and the cap-flow velocities. The state error is O(|pi|). The foundations' strong chain rule gives the actual flow velocities used here: at each level the bounded multiplier g_l preserves L2 continuity, and differentiating W_l X_(l-1) gives exactly the stated P recurrence. This does not assume ambient L2-to-L2 Frechet differentiability of chi_l.

At each fixed time, strong L2 convergence has an almost-sure subsequence. Fatou passes all mesh moment bounds to the cap-flow fields and velocities, giving sup_(t<=T)||H_R(t)||_p<=C_(R,T)sqrt(p). Apply (III.V.29) at two cap-flow times: raw states and directions are Lipschitz at fixed cap, and the fourth-moment tail estimate gives an L2 velocity modulus C_(R,T)|t-s|^(1/2). Only marginal moments are claimed; no random time-maximum bound is used.

#### III.V.8. Fixed-cap finite GF and raw GD

Let Theta_(R,n)^pi be the same-width, same-initialization coarse Euler reference. On the high-probability primal event of Section III.V.3, compare until exit the actual finite capped GF, or the actual fine raw Euler scheme with deterministic step eta_n=n^-2. The coarse interpolant has vector-field defect <=L_0M_0|pi|, fine Euler has defect <=L_0M_0 eta_n, and GF has zero defect. Gronwall gives

    sup_(t<=T)||Theta_(R,n)(t)-Theta_(R,n)^pi(t)||raw
                           <=C_(R,T)(|pi|+eta_n).         (III.V.30)

Here eta_n=0 denotes GF. Choosing the mesh below slack excludes first exit and continues finite capped GF through T. The actual fine-Euler direction is V_R evaluated at its preceding fine node; it is not replaced by the field at the interpolated state. Its direction error against the preceding coarse-node field is still <=C_(R,T)(|pi|+eta_n), by bounded within-step displacement and fixed-cap Lipschitzness.

Apply (III.V.29) at the same width using the coarse node as reference. At fixed pi,M, Section III.V.6 gives joint empirical W2 convergence of all coarse velocities. Their finitely many empirical positive-part tails converge and are bounded in the limit by C/M. Thus the width-limit upper bound in probability for the velocity discrepancy is

    C_(R,T)[(1+M)|pi|+M^-1].                              (III.V.31)

Choose M=|pi|^(-1/2) at that fixed mesh, take width first, and then refine pi. This gives a vanishing bound. No empirical fourth moment or growing-transcript Gaussian law was invoked.

For each layer, let mu_(R,n,l)(t) denote the empirical law of the same-layer tuple of all three samples of chosen primary fields and hidden velocities. The corresponding population law is mu_(R,l)(t). At each time couple actual and coarse arrays by neuron index. The triangle inequality is

    sup_t W2(mu_(R,n,l)(t),mu_(R,l)(t))
      <=sup_t(||actual finite tuple-coarse finite node tuple||_2/sqrt(n))
        +max_k W2(coarse finite node law,coarse population node law)
        +sup_t||coarse population node tuple-population flow tuple||_2.
                                                               (III.V.32)

At fixed mesh the middle term vanishes by the finite appended program theorem. The outer terms vanish after mesh refinement by (III.V.11),(III.V.29)--(III.V.31). Therefore these same-layer laws converge uniformly in physical time in W2, in probability along the full width sequence. Concatenating coordinates at finitely many requested times gives their joint-time W2 laws with the same proof; all within-layer time/sample correlations are preserved. Predictions and loss are continuous functions of the convergent contractions.

The functional T_M is 1-Lipschitz in W2: apply the pointwise Lipschitz function (|x|-M)_+ under any coupling and then the triangle inequality in L2. Thus all empirical fixed-level primary and velocity tails converge uniformly in time at fixed cap. In particular their second moments are asymptotically uniformly integrable over time; this is a width-limit conclusion, not a uniform finite-width high-moment assertion.

#### III.V.9. Descending true-backward observations and every raw kernel block

At fixed cap and fixed finite primary transcript, append the true chain in descending order:

    t_L=Wout, b_L=g_L(Y_L)t_L,
    t_l=W_(l+1)^*b_(l+1), b_l=g_l(Y_l)t_l, l=L-1,...,1.

For the first gate use g_L(Y_L)tau_M(Wout), a bounded-derivative instruction. At fixed M, (F) gives its joint law. Formula (III.V.28) and positive-part tail convergence remove M. The current action (W^{(L)})^* consists of its initialized adjoint and its explicit learned rank-one sum. Uniform operator bounds and Cauchy--Schwarz transfer the input L2 error through both pieces, so the first true incoming field has the law of the actual population adjoint action. This is the descending induction base.

The induction invariant at level l+1 is joint W2 convergence of all higher true observations and the primary/velocity transcript, hence uniform removal of each of their finite empirical second-moment tails. Retain all inner caps representing this known chain and add an outer cap at t_l in the next product g_l(Y_l)tau_M(t_l). At fixed outer M remove inner caps first using bounded-derivative continuity, their known W2 laws, and bounded current action errors. Then remove M by (III.V.28) and the newly known second-moment tails of t_l. Apply W_l^* to obtain t_(l-1), transferring the error by its bounded action norm. This proves the invariant at level l. The finite chain reaches the bottom. The argument supplies actual observation laws; it does not claim an untruncated expected-derivative formula without separate domination.

For uniform time passage, at two states on a bounded ball downward substitution gives

    sum_(l,i)(||t_l-tbar_l||_2+||b_l-bbar_l||_2)
      <=C[(1+M)||Theta-Thetabar||raw
                            +sum_(l,i)T_M(tbar_l)].       (III.V.33)

This is proved by the same gate splitting as (III.V.29), now followed by bounded adjoint actions. Each M multiplies a forward state difference, so the downward recurrence again has one M. The true backward map is strongly continuous along converging raw states: first use (III.V.28) at the top, then bounded-action continuity and the same multiplier argument at each lower level. Its time image along a strong cap-flow path is consequently compact in L2. A compact L2 set has uniformly vanishing T_M tails: cover it by finitely many epsilon-balls, use the 1-Lipschitz property of T_M, and remove tails at the finitely many centers.

Apply (III.V.33) with the population cap flow as reference to pass coarse population true fields uniformly to the flow. At finite width apply it with the same-width coarse fields as reference. At fixed mesh and M the descending observational closure passes their tails. Take width, then mesh at fixed M, then M to infinity using compact population tails. This extends (III.V.32) and its joint-time form to all true backward observations.

The true ORIGINAL raw kernel blocks are, in the normalized fields used here,

    K^1_(ij)=a^(2L) G_(ij)<b_(1,i),b_(1,j)>,
    K^l_(ij)=a^(2L)<b_(l,i),b_(l,j)><X_(l-1,i),X_(l-1,j)>, 2<=l<=L,
    K^(L+1)_(ij)=a^(2L)<X_(L,i),X_(L,j)>.                 (III.V.34)

The factor follows either by grad_raw f_i=a^L grad_raw F_i or by multiplying the original backward and feature scalings. Every pairing is within its layer, and all off-diagonal entries are retained. Under an L2 coupling,

    |E[UV]-E[Ubar Vbar]|
       <=||U-Ubar||_2||V||_2+||Ubar||_2||V-Vbar||_2.

Thus uniform-time W2 convergence proves uniform convergence of every block entry. At a capped state this is the true gradient kernel observed there; the clipped dynamics need not use it as their prediction coefficient matrix.

#### III.V.10. Same-width cap comparison for actual finite uncut algorithms

The finite uncut GF vector field is locally Lipschitz in its finite-dimensional raw parameters. Its exact energy identity is

    dE_n/dt=-||dot Theta_n||raw^2.

Hence its raw length on [0,T] is <=sqrt(T E_n(0)). A finite-time escape in finite-dimensional parameter space is impossible, and local solutions extend globally. This argument is for actual uncut GF, not for a clipped surrogate.

Compare actual finite uncut GF to its same-width physical capped GF reference with the same nonzero random Wout_(0,n). Section III.V.8 puts that reference, with probability tending to one for every fixed R, in a primal ball chosen independently of R from (G), with fixed slack. Its incoming empirical positive-part tails converge uniformly in time. Since |q|1_(|q|>R)<=2(|q|-R/2)_+, (III.V.9) supplies their width-limit bound C exp(-cR^2). Until uncut exit, the finite version of (III.V.8) and Gronwall give a width-limit state and actual-direction error

    epsilon_R=C_T exp(C_T R-cR^2) ->0.                    (III.V.35)

Choose a large fixed R making this smaller than slack and then take width. The first-exit comparison excludes exit with probability tending to one. Substitution in (III.V.8) also controls all uncut versus capped-update backward fields.

For actual raw GD set t_k=k eta_n, eta_n=n^-2. Its raw direction on [t_k,t_(k+1)) is V_infty(Theta_n(t_k)); its hidden fields are recomputed from the linearly interpolated raw parameters. Let E(t)=sup_(s<=t)||Theta_n(s)-Theta_(R,n)(s)||raw. Apply (III.V.8) at t_k against the capped reference at t_k, then add the capped within-step direction variation <=C_(R,T)eta_n. Before exit,

    E(t)<=C(1+R)integral_0^t E(s)ds
       +Ct sup_(s<=T)sum_(l,i)(||q_(R,l,i,n)(s)1_(|q_(R,l,i,n)(s)|>R)||_2/sqrt(n))
       +C_(R,T)t eta_n.                                  (III.V.36)

The preceding-node discrepancy is bounded by E(s) because t_k<=s. This proves (III.V.35), the same no-exit conclusion, and the same actual-direction estimate. No width-independent Lipschitz estimate on the uncut field is required. All finite GD iterates are well-defined finite compositions; the comparison proves their required finite-horizon boundedness with probability tending to one.

Take width at fixed cap after its fixed-cap auxiliary-mesh limit, and then let R tend to infinity. Population convergence (III.V.10), finite comparison (III.V.35), and the fixed-cap laws give both actual algorithms the same full-sequence prediction, loss, forward-field, and true-backward limits. The latter may be compared directly to capped UPDATE fields by (III.V.8); Section III.V.9 separately establishes true-kernel observations on capped trajectories. Formula (III.V.34) now gives every actual raw kernel block uniformly on the physical horizon. The two algorithms can share their initialized references and all finite unions of observations, so the convergence holds jointly for both algorithms.

#### III.V.11. Velocity cap removal with the necessary tail order

Raw population cap states and directions converge uniformly by (III.V.10). Their uncut limit has continuous normalized preactivation velocities in L2 by the strong chain rule. Those compact time images have uniformly vanishing T_M tails. Apply (III.V.29) using the uncut state/direction as reference. First let R tend to infinity at fixed M and then M tend to infinity. This proves uniform strong convergence of all population capped hidden velocities to the uncut hidden velocities. The Lipschitz tail functional shows that sufficiently large population caps inherit the same uniform tail removal. No estimate of the growth of C_(R,T) in the fixed-cap fourth moments is needed.

For the finite uncut algorithm against its same-width capped-flow reference, (III.V.29) bounds the hidden-velocity error by

    C[beta_(R,n)+(1+M)alpha_(R,n)
                 +sum_(l,i)sup_(t<=T)T_(M,n)(P_(R,l,i,n)(t))],       (III.V.37)

where alpha and beta are their raw state and ACTUAL direction discrepancies. The constant depends only on the common primal/direction ball and fixed L,a,e, and is independent of R,M. At fixed R,M the empirical reference tails pass to their population counterparts by Section III.V.8. Now take the width limit, let R tend to infinity at fixed M using (III.V.35) and the population strong velocity convergence just proved, and finally let M tend to infinity. The expression vanishes.

Neuron-index coupling with the capped laws and population cap limit proves uniform-time same-layer joint W2 convergence for uncut states and velocities, and finite concatenations prove joint-time convergence. For GD the direction is its preceding-node raw direction, and the chain rule is evaluated at its interpolated state with that direction. Its neighboring capped reference times differ by at most eta_n; their continuous moduli make the same estimates apply. Use right directions at nodes, with a terminal-left convention if a terminal node is included. These choices do not affect integrated speeds.

The complete limit order is: (i) fixed transcript and observation caps, width, removal of inner caps while the new outer cap stays fixed, then removal of that outer cap; (ii) fixed training cap and auxiliary mesh, width, auxiliary mesh refinement; (iii) width at fixed training cap and velocity-tail threshold M, training-cap removal at fixed M, and finally M to infinity. This prevents multiplication of an uncontrolled cap-dependent velocity moment by a cap-removal error.

#### III.V.12. W2 path laws, integrated speeds, and fixed generated probes

For each layer define the ORIGINAL hidden path tuple

    Zpath_l(t)=(Z_(l,1),H_(l,1),Z_(l,2),H_(l,2),Z_(l,3),H_(l,3))(t).

Returning from normalized fields multiplies their state and velocity coordinates by the fixed numbers a^(l-1),a^l and therefore preserves every convergence already proved. These population coordinate paths, and the finite hidden fields recomputed along raw interpolation, are almost everywhere absolutely continuous. The chain-rule recursion, bounded current actions and g_l, and bounded raw directions give bounded RMS hidden speeds on the stopped ball. The no-exit comparisons remove stopping with probability tending to one.

For any absolutely continuous vector path x, and its linear interpolation I_h x on a fixed observation grid of maximum interval h, Cauchy--Schwarz on an interval [u,v] gives

    |x(t)-I_hx(t)|
       <=|x(t)-x(u)|+|x(v)-x(u)|
       <=2sqrt(h)(integral_u^v |x'(s)|^2 ds)^(1/2).

Consequently

    ||x-I_hx||infty^2<=4h integral_0^T |x'(s)|^2 ds.       (III.V.38)

Initial second moments and this speed bound give finite second moments of the path supremum norm. Average (III.V.38) over finite neurons and over the population coupling. The squared W2 interpolation cost is <=4h times the corresponding integrated RMS speed squared. At a fixed observation grid, the already-proved joint-node W2 laws pass through the Lipschitz interpolation map into the uniform path norm. A triangle inequality between finite paths, their grid interpolants, the population grid interpolant, and population paths, first taking width and then h to zero, proves

    W2(n^-1 sum_alpha delta_(Zpath_(l,n,alpha)), Law(Zpath_l)) ->0

in probability in C([0,T];R^6) with its supremum norm. This argument supplies the path tightness and second moments that cannot be inferred from fixed-time laws alone.

Uniform-time velocity W2 convergence gives uniform convergence of squared RMS speeds and all within-layer cross second moments. The elementary inequalities

    | ||U||_2^2-||V||_2^2 | <=(||U||_2+||V||_2)||U-V||_2

and the product estimate after (III.V.34) apply under the W2 couplings. The norms have common bounds on the no-exit ball. Multiplying a uniform error by T therefore gives convergence of all integrated squared hidden speeds and their within-layer cross products. These are actual neuron-coordinate velocities, not metric derivatives of marginal probability laws.

For each original raw block, true GF has

    ||dot Theta^(l)(t)||raw^2=(y-f(t))^T K^l(t)(y-f(t)).    (III.V.39)

Raw GD has the same identity with residual and kernel at its preceding node, since this is its actual raw direction. Uniform convergence of predictions and kernel blocks and eta_n to zero therefore give uniform-time and integrated convergence of all blockwise squared raw speeds. For fixed-cap directions use the corresponding capped-update backward Grams in place of true hidden blocks; these are primary contractions and obey the same conclusion.

Finally, take any fixed finite layer-typed generated probe program, formed from bounded-derivative coordinate maps, scalar contractions, specified generated roots, and either orientation of initialized or current adjacent actions. Include its fixed observations in (F), together with the primary and already identified observation transcript. If an input arises as a strong common-space L2 limit of finite generated probes, approximate it first by such a finite program. The propagation inequality is

    ||A u-Abar ubar||_2
       <=||A-Abar||op ||u||_2+||Abar||op||u-ubar||_2,      (III.V.40)

and exactly the same holds for adjoints. In same-width and common-population comparisons, operator differences are bounded by raw Hilbert--Schmidt differences and all current operator norms are bounded. Thus each finite instruction preserves vanishing approximation error. Uniform-time versions follow by a finite time net and the strong L2 continuity of the finite probe graph. Both action orientations, same-layer second moments, and finite joint-time laws are retained. Learned population increments converge strongly in Hilbert--Schmidt norm by (III.V.10); finite learned-increment contractions, when requested as observations, are finite rank unrollings followed by Riemann approximation of already converging bounded contractions.

All probability conclusions are along the full width sequence: every fixed-program theorem is full-sequence convergence in probability, and each subsequent comparison gives a deterministic width-limit error that can be made arbitrarily small in the stated order. The proof neither identifies operators across different widths nor takes a simultaneous infinite-depth or infinite-time limit.

### III.N. Nonzero initial motion and kernel variation at every depth

#### III.N.0. Statement and scope

Let \(L\ge2\) be any fixed finite integer. Let \(u_i=x_i/\sqrt d\), \(i=1,2,3\), satisfy \(\|u_i\|=1\) and \(G_{ij}=\langle u_i,u_j\rangle\le1-\delta\) for \(i\ne j\), where \(\delta>0\). The two-sided separation \(|G_{ij}|\le1-\delta\) is a special case. Let \(y_i\in\{-1,1\}\), \(p_i=y_i/3\), and

\[
\phi(z)=a(1+z)+e\psi(z),\qquad
\psi\in C^2(\mathbb R),\quad \psi\text{ bounded and nonconstant},\quad
\max_{k=0,1,2}\|\psi^{(k)}\|_\infty\le1.
\]

For this activation class assume \(a\ge4\) and \(0<e\le1\). In fact the proof below needs only

\[
                         0<e<a.                         \tag{III.N.1}
\]

For this initial-motion statement alone, any one fixed \(e\in(0,1]\) and any one fixed \(a\ge2\) work at every fixed finite depth. The full global theorem uses the larger gain selected in (III.M.4). Put \(\alpha=a-e>0\), \(B=a+e\). Then

\[
\alpha\le\phi'(z)\le B,\quad |\phi''(z)|\le e,
\quad |\phi(z)|\le a(1+|z|)+e.                          \tag{III.N.2}
\]

Use the canonical initialized Gaussian actions associated with independent stored first-layer \(V^{(1)}\) entries \(N(0,1/d)\), independent higher-layer entries \(N(0,1/n)\), and population readout \(W^{(L+1)}(0)=0\). The actions and their transposes are the same initialized matrices in both orientations; their population extensions have genuine adjoints. All conclusions below concern these actions, not arbitrary bounded substitutions for them.

Every hidden raw block, every sample preactivation at every hidden layer, and every sample feature at every hidden layer has a nonzero initial acceleration along any canonical strong physical gradient flow from this initialization. More precisely, the accelerations are \(9\mathscr V^\ell,9U_j^\ell,9T_j^\ell\), with the directions defined below. For the original raw metric and the sum of all true kernel blocks,

\[
p^TK_{\rm total}(t)p
=p^TK_{\rm total}(0)p+18t^2\|\mathscr V\|_{\rm hidden}^2+o(t^2),
\qquad \|\mathscr V\|_{\rm hidden}>0.                            \tag{III.N.3}
\]

The algebraic initialization statement is within the canonical Gaussian construction. Parts III.G and III.V have supplied the strong global physical solution needed for its interpretation as acceleration. It does prove the relevant chain rule from the stated strong regularity. No uniform positive numerical lower bound over \(L,e,\psi\) is claimed or needed.

The proof uses constant and linear Gaussian projections for forward positivity, fresh reverse sources for bottom motion, and fresh forward innovations for all upper samples. It never compares the nonlinear network with an affine network, and never needs a sign condition on \(\psi'\) or \(\psi''\).

#### III.N.1. All forward Grams are positive definite

Write \(Z_i^1\) for the first Gaussian projection, with covariance \(G\), and recursively

\[
H_i^\ell=\phi(Z_i^\ell),\quad
Z_i^\ell=W^{(\ell)} H_i^{\ell-1}\ (\ell\ge2),\quad
D_i^\ell=\phi'(Z_i^\ell),\quad
Q_\ell=(E[H_i^\ell H_k^\ell])_{ik}.
\]

At initialization every \(Z^\ell\) is a centered Gaussian tuple. Its coordinates have the same marginal variance: this is true at layer 1 and propagates because the diagonal of the next covariance is \(E[\phi(Z_i^\ell)^2]\).

For any centered Gaussian tuple \(Z\) with equal marginal variance \(s^2>0\), define

\[
\mu_s=E\phi(sG)=a+eE\psi(sG),\qquad
b_s=E\phi'(sG)=a+eE\psi'(sG),
\]

where \(G\sim N(0,1)\). Integration by parts gives \(E[Z_i\phi(Z_i)]=s^2b_s\). The boundary term vanishes by linear growth and Gaussian decay. The Gaussian regression identity \(E[Z_k\mid Z_i]=\operatorname{Cov}(Z_k,Z_i)Z_i/s^2\) remains valid for singular tuples. Consequently

\[
r_i=\phi(Z_i)-\mu_s-b_sZ_i
\]

is orthogonal both to constants and to every coordinate \(Z_k\). Therefore the uncentered feature Gram is exactly

\[
Q=\mu_s^2\mathbf1\mathbf1^T+b_s^2\operatorname{Cov}(Z)
       +(E[r_ir_k])_{ik}.
\]

Since \(\mu_s,b_s\ge\alpha\), this proves

\[
Q_1\succeq\alpha^2(G+\mathbf1\mathbf1^T),\qquad
Q_\ell\succeq\alpha^2Q_{\ell-1}\quad(\ell\ge2).          \tag{III.N.4}
\]

Here is a direct quantitative proof that the augmented input Gram is positive, including singular \(G\). For \(c\in\mathbb R^3\),

\[
c^T(G+\mathbf1\mathbf1^T)c
=(\sum_i c_i)^2+\|\sum_i c_i u_i\|^2.
\]

When all nonzero coefficients have one sign, the first square is at least \(\|c\|^2\). Otherwise, after changing overall sign and permuting coordinates, write \(c=(r_1,r_2,-b)\) with \(r_1,r_2\ge0\), \(A=r_1+r_2>0\), \(b>0\). Put

\[
D=\{r_1(1-G_{13})+r_2(1-G_{23})\}/A\in[\delta,2].
\]

Projection onto \(u_3\) bounds the quadratic form below by

\[
(A-b)^2+((1-D)A-b)^2.
\]

The corresponding \(2\times2\) positive matrix has determinant \(D^2\) and trace \(D^2-2D+4\le4\), so its smaller eigenvalue is at least \(\delta^2/4\). Since \(A^2+b^2\ge\|c\|^2\),

\[
G+\mathbf1\mathbf1^T\succeq\delta^2I_3/4,
\qquad Q_\ell\succeq\alpha^{2\ell}\delta^2I_3/4>0.       \tag{III.N.5}
\]

Feasibility implies \(\delta\le2\), which also handles the one-sign case. Thus \(Z^\ell\) has full three-dimensional Gaussian support for every \(\ell\ge2\).

#### III.N.2. Backward sources and every hidden block

Define

\[
H=\sum_i p_i H_i^L,\quad
\beta_i^L=D_i^LH,\quad
q_i^\ell=(W^{(\ell+1)})^*\beta_i^{\ell+1},\quad
\beta_i^\ell=D_i^\ell q_i^\ell\ (\ell<L),\quad
S_\ell=(E[\beta_i^\ell\beta_k^\ell])_{ik}.
\]

The raw hidden directions and sample directions are

\[
\mathscr V^1=d^{-1}\sum_i p_i\beta_i^1x_i,\qquad
\mathscr V^\ell=\sum_i p_i\beta_i^\ell\otimes H_i^{\ell-1}
\quad(2\le\ell\le L),                                  \tag{III.N.6}
\]

\[
U_j^1=\sum_iG_{ji}p_i\beta_i^1,\qquad
T_j^\ell=D_j^\ell U_j^\ell,\qquad
U_j^\ell=\mathscr V^\ell H_j^{\ell-1}+W^{(\ell)} T_j^{\ell-1}
\quad(\ell\ge2).                                      \tag{III.N.7}
\]

Here \(\mathscr V^1\) is a first-row direction in the storage
\(V^{(1)}=W^{(1)}/\sqrt d\), not that stored parameter itself.
Its canonical \(W^{(1)}\) direction is \(\sqrt d\,\mathscr V^1\).
All norms and products are in their own layer probability spaces. In particular

\[
\|\mathscr V\|_{\rm hidden}^2=d\|\mathscr V^1\|_2^2+
                         \sum_{\ell=2}^L\|\mathscr V^\ell\|_{\rm HS}^2.
\]

First \(S_L\succ0\). If \(v^TS_Lv=0\), full support and continuity give

\[
\left[\sum_i p_i\phi(Z_i)\right]
\left[\sum_i v_i\phi'(Z_i)\right]=0
\quad\text{for every }Z\in\mathbb R^3.
\]

The first factor has no open zero set, because its derivative in coordinate \(i\) is \(p_i\phi'(Z_i)\ne0\). Thus its nonzero set is dense, and the second factor vanishes identically by continuity. Differentiating in coordinate \(i\) gives \(v_i\phi''(Z_i)=0\) for every \(Z_i\). Bounded nonconstant \(\psi\) cannot have \(\psi''\equiv0\): such a function would be affine and bounded, hence constant. Since \(e>0\), \(\phi''\not\equiv0\), and \(v=0\).

The exact initialized transpose formulas are

\[
q_i^\ell=\zeta_i^\ell+\sum_k R^\ell_{ik}H_k^\ell,
\qquad \operatorname{Cov}(\zeta^\ell)=S_{\ell+1},        \tag{III.N.8}
\]

where each reverse source group \(\zeta^\ell\) is centered Gaussian and independent of all forward source groups and first-layer roots. The deterministic response coefficients are

\[
R^{L-1}_{ik}=E[p_kD_i^LD_k^L+
                 \mathbf1_{i=k}H\phi''(Z_i^L)],
\]

\[
R^\ell_{ik}=E[\mathbf1_{i=k}\phi''(Z_i^{\ell+1})q_i^{\ell+1}
                    +D_i^{\ell+1}R^{\ell+1}_{ik}D_k^{\ell+1}]
\quad(\ell<L-1).                                      \tag{III.N.9}
\]

Section III.N.4 derives and justifies these formulas. They include both the current curvature term and the next-layer return. Neither return is assumed positive or discarded.

Conditionally on \(Z^\ell\), (III.N.8) gives

\[
\operatorname{Cov}(\beta^\ell\mid Z^\ell)
=\operatorname{diag}(D^\ell)S_{\ell+1}\operatorname{diag}(D^\ell)
\succeq\alpha^2\lambda_{\min}(S_{\ell+1})I_3.
\]

Backward induction from \(S_L\succ0\) proves

\[
S_\ell\succeq\alpha^2\lambda_{\min}(S_{\ell+1})I_3\succ0
\quad(\ell<L).                                        \tag{III.N.10}
\]

The same formula applies at layer 1 even if \(Z^1\) is singular. Applying it componentwise in (III.N.6) and summing gives

\[
d\|\mathscr V^1\|_2^2\ge\alpha^2\lambda_{\min}(S_2)\sum_i p_i^2>0.
\]

For every matrix block,

\[
\|\mathscr V^\ell\|_{\rm HS}^2
=\operatorname{tr}(\operatorname{diag}(p)S_\ell
                  \operatorname{diag}(p)Q_{\ell-1})
\ge\lambda_{\min}(S_\ell)\lambda_{\min}(Q_{\ell-1})
                         \sum_i p_i^2>0.                \tag{III.N.11}
\]

The inequality follows by pairing \(S_\ell\succeq\lambda_{\min}(S_\ell)I\) with the positive matrix \(\operatorname{diag}(p)Q_{\ell-1}\operatorname{diag}(p)\), then using the analogous bound for \(Q_{\ell-1}\).

For the bottom samples,

\[
\|U_j^1\|_2^2\ge\alpha^2\lambda_{\min}(S_2)
                  \sum_iG_{ji}^2p_i^2
\ge\alpha^2\lambda_{\min}(S_2)p_j^2>0,                 \tag{III.N.12}
\]

using \(G_{jj}=1\). This proves every hidden block and every bottom sample is nonzero.

#### III.N.3. Exact return recursion and an innovation at every upper layer

Fix one sample \(j\). Define deterministic coefficients

\[
c^1_{ji}=G_{ji}p_i,
\qquad
c^\ell_{ji}=p_i(Q_{\ell-1})_{ij}
          +c^{\ell-1}_{ji}E[D_j^{\ell-1}D_i^{\ell-1}]
\quad(2\le\ell\le L).                                \tag{III.N.13}
\]

No sign of these coefficients is required. Let \(\xi_{T_j^{\ell-1}}\) denote the primitive source of the added forward query \(W^{(\ell)} T_j^{\ell-1}\), belonging to the same oriented source group as the three original coordinates \(Z_i^\ell\). The exact recursion is

\[
U_j^\ell=\xi_{T_j^{\ell-1}}+\sum_i c^\ell_{ji}\beta_i^\ell
\qquad(2\le\ell\le L).                               \tag{III.N.14}
\]

To prove the base case, (III.N.8) at layer 1 and (III.N.7) show, differentiating in the named reverse source \(\zeta_i^1\),

\[
\partial_{\zeta_i^1}T_j^1=D_j^1c^1_{ji}D_i^1.
\]

The same-matrix forward response rule therefore reads

\[
W^{(2)}T_j^1=\xi_{T_j^1}+\sum_i\beta_i^2
                               c^1_{ji}E[D_j^1D_i^1].
\]

Adding \(\mathscr V^2H_j^1=\sum_i p_i(Q_1)_{ij}\beta_i^2\) proves (III.N.14) for \(\ell=2\).

Now suppose (III.N.14) is proved at some \(2\le\ell<L\). Its primitive forward source belongs to the \(W^{(\ell)}\) forward group, which is independent of the \((W^{(\ell+1)})^*\) reverse group \(\zeta^\ell\). These are distinct named formal slots even if a covariance is singular. Formula (III.N.8) consequently gives the exact derivative

\[
\partial_{\zeta_i^\ell}T_j^\ell
=D_j^\ell c^\ell_{ji}D_i^\ell.
\]

Applying the forward response rule to \(W^{(\ell+1)}T_j^\ell\), then adding \(\mathscr V^{\ell+1}H_j^\ell\), gives (III.N.14) at \(\ell+1\) with exactly (III.N.13). This proves (III.N.14) at every depth, with all transpose returns retained.

Regress the Gaussian source \(\xi_{T_j^{\ell-1}}\) on the three original forward sources \(Z^\ell\). Their covariance is \(Q_{\ell-1}\succ0\). Since oriented source covariances are the full input second moments, the independent regression remainder \(\varepsilon_{\ell j}\) has variance

\[
\sigma_{\ell j}^2
=\inf_{b\in\mathbb R^3}
       \left\|T_j^{\ell-1}-\sum_i b_i H_i^{\ell-1}\right\|_2^2.
                                                               \tag{III.N.15}
\]

This is linear regression without an intercept: the sources are centered, while their covariance is the **uncentered** input Gram. The conditional-variance bounds below hold for this precise regression because every competitor \(\sum_i b_i H_i^{\ell-1}\) is measurable in the conditioning variables.

At \(\ell=2\), all \(H_i^1\) are measurable in \(Z^1\), so (III.N.10) yields

\[
\begin{aligned}
\sigma_{2j}^2
&\ge E\operatorname{Var}(T_j^1\mid Z^1)\\
&\ge\alpha^4\lambda_{\min}(S_2)
                     \sum_iG_{ji}^2p_i^2
\ge\alpha^4\lambda_{\min}(S_2)p_j^2>0.                \tag{III.N.16}
\end{aligned}
\]

The remainder \(\varepsilon_{2j}\) is independent of \(Z^2\) and of the separate reverse group \(\zeta^2\), if present. By (III.N.8), all \(\beta_i^2\) are functions of \((Z^2,\zeta^2)\); at \(L=2\) they are functions of \(Z^2\) alone. Thus (III.N.14), after regression, is

\[
U_j^2=\varepsilon_{2j}+F_{2j}(Z^2,\zeta^2),
\]

with the unused reverse argument omitted at the top. In particular \(\|U_j^2\|_2^2\ge\sigma_{2j}^2\).

For the induction step assume \(2\le\ell<L\) and \(\sigma_{\ell j}^2>0\). Exactly the same regression in (III.N.14) gives

\[
U_j^\ell=\varepsilon_{\ell j}+F_{\ell j}(Z^\ell,\zeta^\ell),
\]

where \(\varepsilon_{\ell j}\) is independent of the displayed pair. Therefore

\[
\operatorname{Var}(T_j^\ell\mid Z^\ell,\zeta^\ell)
                  =(D_j^\ell)^2\sigma_{\ell j}^2.
\]

Testing (III.N.15) for the next layer against this conditional variance proves

\[
\sigma_{\ell+1,j}^2\ge E[(D_j^\ell)^2]\sigma_{\ell j}^2
                          \ge\alpha^2\sigma_{\ell j}^2>0.       \tag{III.N.17}
\]

The new remainder belongs to the next forward source group and is independent of its original forward tuple and separate reverse group; at the top there is no reverse group to condition on. Thus it cannot cancel the other terms of (III.N.14). Combining (III.N.16) and (III.N.17),

\[
\|U_j^\ell\|_2^2\ge\sigma_{\ell j}^2
       \ge\alpha^{2\ell}\lambda_{\min}(S_2)p_j^2>0
\quad(2\le\ell\le L).                                \tag{III.N.18}
\]

Together with (III.N.12), this covers every sample and layer. Finally \(\|T_j^\ell\|_2\ge\alpha\|U_j^\ell\|_2>0\). The three samples' new forward sources may be mutually correlated. No step assumes otherwise; one may prove the result with one fixed augmented transcript per sample and then take their finite union.

#### III.N.4. The same-matrix source formulas and unbounded products

Only the finite Gaussian foundation is needed here. This section states its precise specialization, checks the actual query schedule, and proves its derivative-valid extension for every unbounded product used above. Oddness, monotonicity of the perturbation, and affine perturbation estimates play no role.

The actual finite initialization transcript, with normalized finite inner products, is as follows. First reveal the first-layer roots and calculate all three ordinary forward calls at each layer. Next form \(H\), the three top \(\beta_i^L\), and, descending through the layers, the three calls \((W^{(\ell+1)})^*\beta_i^{\ell+1}\) and the gates \(\beta_i^\ell\). For one fixed sample \(j\), form \(U_j^1=\sum_iG_{ji}p_i\beta_i^1\) and \(T_j^1\). Then ascend through layers \(2,\ldots,L\): make the one added query \(W^{(\ell)} T_j^{\ell-1}\), add \(\sum_i p_i\frac{1}{n}\langle H_i^{\ell-1},H_j^{\ell-1}\rangle_{\mathbb R^n}\beta_i^\ell\), and apply the gate to obtain \(T_j^\ell\). These are all the action probes used. Their empirical contractions converge to the \(Q\) coefficients; replacing these finitely many convergent scalar coefficients by their limits changes the normalized vector errors by \(o_P(1)\), because all participating vector norms are bounded in probability. One may therefore use deterministic limiting coefficients in the source calculation.

Here is the needed finite-program statement and why its use is legitimate. For a fixed finite list of independent \(N(0,1/n)\) matrices, reused in both orientations, fixed finite root tuples with finite second moment, and coordinate instructions that are \(C^1\) with bounded first derivatives, same-layer empirical laws and second moments converge. For an initialized forward query on \(h\), and reverse query on \(u\), their scalar source formulas are

\[
Ah=\xi_h+\sum_s u_sE[\partial_{\zeta_s}h],\qquad
A^*u=\zeta_u+\sum_r v_rE[\partial_{\xi_r}u],             \tag{III.N.19}
\]

where the sums use the previously queried inputs in the opposite orientation. Sources belonging to distinct orientations or matrices are independent; within one group the covariance is the full Gram of its query inputs. Formal derivatives freeze deterministic coefficients and covariance parameters and differentiate distinct named source slots.

The conditioning proof covers any fixed finite number of matrices: condition successively on the current transcript. A coordinate instruction reveals no new matrix randomness. A matrix query conditions only that matrix's residual Gaussian factor on one further linear observation; the other residual factors retain their product conditional law. Induction over the finite instruction list gives the stated conclusion with \(L-1\) matrices.

For explicit verification of (III.N.19), if old calls are \(AV=Y\), \(A^TU=Q\), Gaussian conditioning gives

\[
A\mid\mathcal H=M+P_{U^\perp}\widetilde A P_{V^\perp},
\quad
M=Y(V^TV)^{-1}V^T+U(U^TU)^{-1}Q^TP_{V^\perp},
\]

initially when the indicated Grams are nonsingular. Indeed \(M\) satisfies the two constraints and is orthogonal to all homogeneous solutions \(P_{U^\perp}KP_{V^\perp}\), so isotropic Gaussian projection proves the conditional law. With \(h_\perp=h-P_Vh\), the new answer is a regression term plus an opposite-orientation response and

\[
                     \frac{\|h_\perp\|_2}{\sqrt n}P_{U^\perp}g_n.
\]

The removed Gaussian projection satisfies \(E[\frac{\|P_Ug_n\|_2^2}{n}\mid\mathcal H]=\operatorname{rank}(U)/n\to0\). The response coefficient is obtained from

\[
E[q_sh_\perp]=E[\zeta_sh_\perp],\qquad
E[\zeta h_\perp]=\operatorname{Cov}(\zeta)
                                  E[\nabla_\zeta h_\perp].
\]

The first identity uses the old-return representation of \(q_s\) and orthogonality to \(V\); the second is Gaussian integration by parts. Substituting the old forward source representations cancels the derivatives of the regression projection, leaving exactly (III.N.19). The covariance of the resulting new forward source with old sources is \(E[h v_r]\), and its variance is \(E[h^2]\). This proves (III.N.15), including the fact that conditioning on transpose queries cannot erase its positive innovation.

Singular first-layer roots are allowed and do not need an inverse. In this particular proof all original matrix forward Grams \(Q_\ell\) and backward Grams \(S_\ell\) are positive definite once established; for a separate fixed sample the augmented forward Gram is positive definite by (III.N.16)–(III.N.17). Alternatively Part III.F's singular-query extension uses fresh small input noises, converging finite covariance square roots and bounded action norms; it does not assume continuity of pseudoinverses. No extra probabilistic independence of matrix answers and their inputs is being introduced.

The untruncated coordinate products in the present program are not themselves globally bounded-derivative instructions, so they need a separate justification. Let \(\tau_M\) be smooth, equal to the identity on \([-M,M]\), with \(|\tau_M(q)|\le|q|\), \(|\tau_M'|\le1\), and bounded range. Such clips can be obtained by integrating a smooth cutoff. At the top use

\[
\beta_{i,M}^L=D_i^L\tau_M(H).
\]

Its derivative in the named forward source \(Z_k^L\) is

\[
D_i^L\tau_M'(H)p_kD_k^L
 +\mathbf1_{i=k}\phi''(Z_i^L)\tau_M(H).
\]

This is bounded in absolute value by a fixed constant times \(1+|H|\), independently of \(M\). The top forward fields have all finite moments, so dominated convergence gives the first line of (III.N.9). The clipped fields converge in \(L^2\), their Grams converge, and coupling the resulting Gaussian reverse sources via finite positive-semidefinite covariance square roots gives convergence of the sources and (III.N.8) at layer \(L-1\).

Suppose (III.N.8) has been justified at layer \(\ell+1\). Its explicit expression is a finite Gaussian source plus a deterministic linear combination of linear-growth Gaussian functions. Thus it has all finite moments. Its derivative in \(Z_k^{\ell+1}\) is \(R^{\ell+1}_{ik}D_k^{\ell+1}\). For the next clipped gate \(D_i^{\ell+1}\tau_N(q_i^{\ell+1})\), the required derivative is

\[
\mathbf1_{i=k}\phi''(Z_i^{\ell+1})\tau_N(q_i^{\ell+1})
 +D_i^{\ell+1}\tau_N'(q_i^{\ell+1})R^{\ell+1}_{ik}D_k^{\ell+1}.
\]

At fixed outer cap, remove all earlier caps; then let \(N\to\infty\). The final envelope is a constant times \(1+|q_i^{\ell+1}|\), which is integrable. This proves the second line of (III.N.9), the next source covariance, and (III.N.8) at layer \(\ell\). Repeating this explicit finite step proves the whole backward chain with only \(C^2\) regularity.

Here is an explicit coherent clipping program for all added forward queries. Let the backward caps at layers \(1,\ldots,L-1\) be \(N_1,\ldots,N_{L-1}\), and the top cap be \(N_L\). Thus

\[
\beta_i^{L,N}=D_i^L\tau_{N_L}(H),\quad
q_i^{\ell,N}=(W^{(\ell+1)})^*\beta_i^{\ell+1,N},\quad
\beta_i^{\ell,N}=D_i^\ell\tau_{N_\ell}(q_i^{\ell,N}).
\]

Use these same \(\beta_i^{\ell,N}\) both as reverse query inputs and in the block contributions. Give each added forward gate its own cap \(M_\ell\):

\[
U_j^{1,N,M}=\sum_iG_{ji}p_i\beta_i^{1,N},\qquad
T_j^{\ell,N,M}=D_j^\ell\tau_{M_\ell}(U_j^{\ell,N,M}),
\]

\[
U_j^{\ell,N,M}=W^{(\ell)} T_j^{\ell-1,N,M}
                  +\sum_i p_i(Q_{\ell-1})_{ij}\beta_i^{\ell,N}
\quad(\ell\ge2).
\]

At all fixed caps these are legitimate bounded-derivative coordinate instructions and initialized action calls. Their source formulas have the exact form

\[
U_j^{\ell,N,M}=\xi_{T_j^{\ell-1,N,M}}
                     +\sum_i c^{\ell,N,M}_{ji}\beta_i^{\ell,N},
\]

with \(c^{1,N,M}_{ji}=G_{ji}p_i\). To derive the next coefficient, the previously established backward formula gives

\[
\partial_{\zeta_i^\ell}\beta_k^{\ell,N}
=\mathbf1_{i=k}D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N}).
\]

The current forward primitive source is a different named slot from \(\zeta_i^\ell\), so

\[
\partial_{\zeta_i^\ell}T_j^{\ell,N,M}
=D_j^\ell\tau_{M_\ell}'(U_j^{\ell,N,M})
       c^{\ell,N,M}_{ji}D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N}).
                                                               \tag{III.N.22}
\]

Consequently, for \(\ell<L\),

\[
c^{\ell+1,N,M}_{ji}=p_i(Q_\ell)_{ij}
 +c^{\ell,N,M}_{ji}E[D_j^\ell\tau_{M_\ell}'(U_j^{\ell,N,M})
                          D_i^\ell\tau_{N_\ell}'(q_i^{\ell,N})].
                                                               \tag{III.N.23}
\]

This proves the full capped source recurrence, rather than assuming a limit of the uncapped formula. In particular define finite deterministic bounds

\[
C^1_{ji}=|G_{ji}p_i|,\qquad
C^{\ell+1}_{ji}=|p_i(Q_\ell)_{ij}|+B^2C^\ell_{ji}.
\]

Then \(|c^{\ell,N,M}_{ji}|\le C^\ell_{ji}\), and the derivative in (III.N.22) is bounded by \(B^2C^\ell_{ji}\), uniformly in **all** caps. No smallness of these constants with depth is required.

First remove the backward caps in the descending dependency order established above, at fixed forward caps. Actual action continuity and the bounded gate comparisons give \(L^2\) convergence of \(q,\beta,U,T\) successively; their source Grams converge as well. Couple the finite source vectors through covariance square roots. Along a coupled subsequence their arguments converge almost surely; continuity and the bound \(B^2C^\ell_{ji}\) pass (III.N.22)–(III.N.23) under expectation. Next remove the forward caps in ascending order \(M_1,M_2,\ldots,M_L\), holding later caps fixed. The already identified incoming \(U_j^\ell\) is in \(L^2\), so \(\tau_{M_\ell}(U_j^\ell)\to U_j^\ell\) in \(L^2\). The subsequent initialized answers converge by bounded actions. In (III.N.22), the outer clip derivative tends to one and its integrand remains bounded by \(B^2C^\ell_{ji}\); (III.N.23) therefore converges to (III.N.13) at that layer. This proves the uncapped (III.N.14) and its bounded formal source derivative at every step. Each resulting \(U_j^\ell,T_j^\ell\) is, from its explicit source expression, a bounded gate times finite sums of Gaussian sources and linear-growth Gaussian functions, so it also has all finite moments.

To identify these limiting formulas with the actual uncut action answers, use bounded initialized action norms and bounded multiplier continuity. If \(z_m\to z\) in probability and \(q_m\to q\) in \(L^2\), then

\[
\|D(z_m)q_m-D(z)q\|_2
\le B\|q_m-q\|_2+\|[D(z_m)-D(z)]q\|_2\to0.
\]

For the second term restrict \(q\) to a bounded set, use bounded convergence in probability there, and then make its \(L^2\) tail small. Matrix action errors are bounded by the action norm times their input errors. Explicitly, a gate clipping error obeys

\[
\|D(z)[q-\tau_M(q)]\|_2
\le2B\|q\mathbf1_{|q|>M}\|_2
\le4B\|(|q|-M/2)_+\|_2\longrightarrow0.
\]

The same inequality holds in empirical normalized norm. Joint \(\mathcal W_2\) convergence of an incoming finite-array field implies convergence of the squared norm of \((|q|-M/2)_+\), since this is a 1-Lipschitz transformation followed by its second moment. Thus the empirical clipping tail is small after taking width to infinity and then \(M\to\infty\). The high-probability uniform bounds on the finitely many initialized matrix norms transfer this error to the next actual answer. Apply this gate/action step in the exact finite schedule above. A triangle inequality, with fixed caps first, identifies the full uncut finite-array law and its second moments, as well as its canonical action answers. The source laws, current responses, and input covariances all survive the ordered removal of the clips.

#### III.N.5. Physical acceleration and the coefficient 18

Let a strong physical gradient-flow solution in the original raw Hilbert metric exist on a right neighborhood of zero. Its current hidden actions are their initialized actions plus Hilbert–Schmidt increments. Denote the residual-free physical backward fields by

\[
\delta_i^L(t)=D_i^L(t)W^{(L+1)}(t),\qquad
\delta_i^\ell(t)=D_i^\ell(t)W^{(\ell+1)}(t)^*\delta_i^{\ell+1}(t).
\]

The physical loss is \(\tfrac12\sum_i(f_i-y_i)^2\), so the exact raw updates are

\[
(W^{(L+1)})'=-\sum_i r_i H_i^L,\quad
(\theta_h^1)'=-d^{-1}\sum_i r_i \delta_i^1x_i,\quad
(W^{(\ell)})'=-\sum_i r_i \delta_i^\ell\otimes H_i^{\ell-1}.
\]

Since \(W^{(L+1)}(0)=0\), the initial predictions vanish, \(r_i(0)=-y_i=-3p_i\), all hidden first derivatives vanish, and

\[
(W^{(L+1)})'(0)=3H,\qquad W^{(L+1)}(t)/t\longrightarrow3H.
\]

Strong multiplier continuity from Section III.N.4 and operator-norm continuity of the Hilbert–Schmidt action increments give, successively from the top,

\[
\delta_i^\ell(t)/t\longrightarrow3\beta_i^\ell.
\]

Substitution in the exact raw updates yields

\[
\theta_h'(t)/t\longrightarrow9\mathscr V,\qquad
\theta_h(t)=\theta_h(0)+\tfrac92t^2\mathscr V+o_{\rm raw}(t^2).  \tag{III.N.20}
\]

For a strong \(C^1\) \(L^2\) curve \(z(t)\) and bounded continuous \(\phi'\), the identity

\[
\frac{\phi(z(t+h))-\phi(z(t))}{h}
=\frac{z(t+h)-z(t)}h
  \int_0^1\phi'(z(t)+s[z(t+h)-z(t)])\,ds
\]

and bounded multiplier continuity prove the strong chain rule. Combining it with the product rule for a strongly differentiable field and an operator differentiable in Hilbert–Schmidt norm proves recursively

\[
(Z_j^\ell)'(t)/t\longrightarrow9U_j^\ell,\qquad
(H_j^\ell)'(t)/t\longrightarrow9T_j^\ell.               \tag{III.N.21}
\]

Since the initial first derivatives are zero, (III.N.20)–(III.N.21) are the claimed nonzero strong right second derivatives.

To compute the kernel coefficient without assuming an ambient \(L^2\)-to-\(L^2\) Fréchet derivative of the activation, put

\[
T=\sum_jp_jT_j^L.
\]

Genuine adjunction and (III.N.6)–(III.N.7) give the following exact telescoping identity. At a matrix layer,

\[
\sum_jp_j\langle\beta_j^\ell,U_j^\ell\rangle
=\|\mathscr V^\ell\|_{\rm HS}^2
 +\sum_jp_j\langle q_j^{\ell-1},T_j^{\ell-1}\rangle
=\|\mathscr V^\ell\|_{\rm HS}^2
 +\sum_jp_j\langle\beta_j^{\ell-1},U_j^{\ell-1}\rangle.
\]

The final bottom sum is \(d\|\mathscr V^1\|_2^2\), and the top sum is \(\langle H,T\rangle\). Hence

\[
                         \langle H,T\rangle=\|\mathscr V\|_{\rm hidden}^2.
\]

Writing \(H(t)=\sum_jp_jH_j^L(t)\), (III.N.21) gives

\[
H(t)=H+\tfrac92t^2T+o_{L^2}(t^2),\qquad
\|H(t)\|_2^2=\|H\|_2^2+9t^2\|\mathscr V\|_{\rm hidden}^2+o(t^2).
\]

The hidden part \(g_h(t)\) of the raw gradient of \(\sum_i p_i f_i(t)\) satisfies \(g_h(t)/t\to3\mathscr V\) by the same backward calculation, so

\[
\|g_h(t)\|_{\rm hidden}^2=9t^2\|\mathscr V\|_{\rm hidden}^2+o(t^2).
\]

The true raw kernel identity is

\[
p^TK_{\rm total}(t)p=\|H(t)\|_2^2+\|g_h(t)\|_{\rm hidden}^2.
\]

Adding its two terms proves (III.N.3). All \(L\) hidden blocks occur in \(\|\mathscr V\|_{\rm hidden}^2\), and each is strictly positive by Section III.N.2. The coefficient 18 and the nonzero accelerations therefore persist at every fixed depth with the same fixed activation. No depth-dependent affine-comparison smallness premise is needed for this initial-motion conclusion.

### III.A. Uniform activation classes and depth-uniform nonaffinity

Fix the three-input separation parameter \(\delta>0\), and set
\[
\lambda=\delta^2/16,\qquad T_0=12/\lambda.
\]
Let
\[
\mathcal B=\left\{\psi\in C_b^2(\mathbb R):
          \max_{k=0,1,2}\|\psi^{(k)}\|_\infty\le1\right\},
\qquad
\phi(z)=a(1+z)+e\psi(z),\quad 0<e\le1.
\]
Here \(C_b^2(\mathbb R)\) consists of twice continuously differentiable real functions with bounded derivatives of orders zero, one, and two, and carries the displayed maximum norm. Throughout, \(e\) is fixed when comparing depths.

The main theorem supplies, for each fixed finite hidden depth \(L\ge2\), its global strong physical trajectory and the estimate
\[
\max_{i,\ 1\le\ell\le L}\sup_{t\ge0}
 \|Z_i^\ell(t)-Z_i^\ell(0)\|_2
\le d_L,\qquad
d_L=3\sqrt L\left(\frac{32768}{a}\right)^L\frac{T_0^2}{a}.
                                                               \tag{III.A.1}
\]
Its function-independent dynamical estimates require
\(a\ge10^{12}(1+T_0)\). This appendix proves exactly how one can choose the remaining gain condition uniformly over classes of functions, and when the nonaffinity lower bound can also be uniform over depth. All constants selected below depend only on \(\delta\) and the specified class, and not on \(L\), the dataset, time, or the fixed \(e\in(0,1]\).

#### III.A.1. Elementary regression estimates

For a square-integrable real random variable \(X\), define
\[
\mathcal R_\psi(X)=\inf_{\alpha,\beta\in\mathbb R}
                       E[(\psi(X)-\alpha-\beta X)^2].
\]
The infimum is attained. If \(\operatorname{Var}(X)>0\), direct completion of squares gives an optimal slope
\[
\beta_X=\frac{\operatorname{Cov}(X,\psi(X))}
                     {\operatorname{Var}(X)},\qquad
\alpha_X=E\psi(X)-\beta_XEX.
\]
When \(X\) is almost surely constant, choose \(\beta_X=0\) and
\(\alpha_X=\psi(X)\).

For \(\psi\in\mathcal B\), its Lipschitz constant is at most one. If \(X'\) is an independent copy of \(X\), expansion and independence give
\[
\operatorname{Cov}(X,\psi(X))
=\tfrac12E[(X-X')(\psi(X)-\psi(X'))],
\qquad E[(X-X')^2]=2\operatorname{Var}(X).
\]
Consequently \(|\beta_X|\le1\). In particular optimal slopes need not be positive, but they remain in the fixed interval \([-1,1]\).

For two square-integrable variables \(X,Y\) on a common probability space, use the optimal affine fit at \(Y\) as a competitor at \(X\). The triangle inequality and \(|\beta_Y|\le1\) give
\[
\begin{aligned}
\sqrt{\mathcal R_\psi(X)}
&\le\|\psi(X)-\alpha_Y-\beta_YX\|_2\\
&\le\sqrt{\mathcal R_\psi(Y)}
       +\|\psi(X)-\psi(Y)-\beta_Y(X-Y)\|_2\\
&\le\sqrt{\mathcal R_\psi(Y)}+2\|X-Y\|_2.
\end{aligned}
\]
Interchanging \(X,Y\) proves the useful stability estimate
\[
\left|\sqrt{\mathcal R_\psi(X)}
       -\sqrt{\mathcal R_\psi(Y)}\right|
                         \le2\|X-Y\|_2.                 \tag{III.A.2}
\]

At a fixed \(X\), the corresponding estimate for changing the function is
\[
\left|\sqrt{\mathcal R_\psi(X)}
       -\sqrt{\mathcal R_\chi(X)}\right|
\le\|\psi(X)-\chi(X)\|_2\le\|\psi-\chi\|_\infty.          \tag{III.A.3}
\]
Indeed test each regression problem with an optimal affine fit for the other and use the triangle inequality. This estimate does not require bounds on the derivatives.

Finally the affine part of \(\phi\) can be absorbed exactly into the free regression coefficients. Since \(e>0\), the substitutions
\(\widetilde\alpha=(\alpha-a)/e\) and
\(\widetilde\beta=(\beta-a)/e\) range over all real pairs. Thus
\[
\inf_{\alpha,\beta}E[(\phi(X)-\alpha-\beta X)^2]
                              =e^2\mathcal R_\psi(X).    \tag{III.A.4}
\]

#### III.A.2. Finite-interval margins and a common gain

For \(r\ge1\), put
\[
J_r(\psi)=\inf_{\alpha,\beta}
                   \int_{-r}^r[\psi(x)-\alpha-\beta x]^2\,dx.
\]
The functions \(1,x\) are orthogonal on this interval and have squared norms \(2r,2r^3/3\). Completing squares therefore gives
\[
J_r(\psi)=\int_{-r}^r\psi(x)^2\,dx
 -\frac1{2r}\left(\int_{-r}^r\psi(x)\,dx\right)^2
 -\frac3{2r^3}\left(\int_{-r}^r x\psi(x)\,dx\right)^2.     \tag{III.A.5}
\]
In particular the infimum is attained. It is zero exactly when
\(\psi\) equals an affine function almost everywhere on \([-r,r]\); continuity then gives equality everywhere on that interval.

Every bounded nonconstant \(\psi\in C^2(\mathbb R)\) has some \(r\ge1\) with \(J_r(\psi)>0\). Otherwise its restrictions to all intervals \([-n,n]\), for positive integers \(n\), would be affine. These affine functions agree on their overlapping intervals, so their two coefficients agree. Thus \(\psi\) would be affine on all of \(\mathbb R\), and boundedness would make it constant, a contradiction.

Fix any such interval, and define
\[
c_\psi=\frac{e^{-r^2/2}J_r(\psi)}{\sqrt{2\pi}}>0.         \tag{III.A.6}
\]
For \(G\sim N(0,1)\) and \(\sigma\ge1\), its scaled density on \([-r,r]\) obeys
\[
\frac1{\sigma\sqrt{2\pi}}
        e^{-x^2/(2\sigma^2)}
\ge\frac{e^{-r^2/2}}{\sigma\sqrt{2\pi}}.
\]
Applying this pointwise lower bound to every squared affine-regression error and then taking the infimum proves
\[
                    \mathcal R_\psi(\sigma G)
                                  \ge c_\psi/\sigma.    \tag{III.A.7}
\]

We record the initialized variance bounds used with (III.A.7). Write
\(Z_i^\ell(0)\overset d=\sigma_\ell G\). All samples have the same marginal variance at a fixed layer, and \(\sigma_1=1\). The recursion of the initialized Gaussian program is
\[
\sigma_{\ell+1}=\|\phi(\sigma_\ell G)\|_2.
\]
Integration by parts gives the coefficient of the projection of
\(\phi(\sigma G)\) onto \(G\):
\[
E[G\phi(\sigma G)]
=\sigma E[\phi'(\sigma G)]\ge(a-e)\sigma.
\]
Its absolute value is bounded by the \(L^2\) norm of the feature, because \(\|G\|_2=1\). Thus
\[
\sigma_\ell\ge(a-e)^{\ell-1}
                          \ge(a/2)^{\ell-1}\ge1,         \tag{III.A.8}
\]
where \(a\ge4\) and \(e\le1\) suffice. For an upper bound, the triangle inequality gives
\[
\sigma_{\ell+1}
\le a\sqrt{1+\sigma_\ell^2}+e
\le a\sigma_\ell+2a.
\]
Dividing by \(a^\ell\), summing this scalar recurrence, and using \(a\ge4\) gives
\[
\frac{\sigma_\ell}{a^{\ell-1}}
\le1+2\sum_{k=0}^{\ell-2}a^{-k}
\le1+\frac2{1-a^{-1}}\le\frac{11}{3}<4.
\]
Hence
\[
                     1\le\sigma_\ell\le4a^{\ell-1}.      \tag{III.A.9}
\]
The first-layer upper bound also follows directly from \(\sigma_1=1\).

Select
\[
a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{c_\psi}}\right)^{2/5}\right\}.
                                                               \tag{III.A.10}
\]
Here is the arithmetic that makes this one gain work at every fixed depth. Put \(q=32768/\sqrt a=2^{15}/\sqrt a\). The first condition in (III.A.10) gives \(q<1/2\). For \(L\ge2\), the ratio of consecutive terms of \(\sqrt Lq^{L-2}\) is
\[
q\sqrt{\frac{L+1}{L}}\le\tfrac12\sqrt{\tfrac32}<1.
\]
Therefore \(\sqrt Lq^{L-2}\le\sqrt2\), and (III.A.1) yields
\[
\begin{aligned}
d_La^{(L-1)/2}
&=\frac{3T_0^2}{a^{3/2}}\sqrt Lq^L\\
&\le\frac{3\sqrt2\,2^{30}T_0^2}{a^{5/2}}\\
&\le\frac{3\sqrt2}{64}\sqrt{c_\psi}
 <\frac{\sqrt{c_\psi}}8.
\end{aligned}                                                   \tag{III.A.11}
\]
The last strict inequality is \(3\sqrt2<8\).

By (III.A.7)–(III.A.9), the initialized regression residual at layer \(\ell\) satisfies
\[
\sqrt{\mathcal R_\psi(Z_i^\ell(0))}
                    \ge\frac{\sqrt{c_\psi}}{2a^{(\ell-1)/2}}.
\]
For \(\ell\le L\), (III.A.11) gives
\[
2d_L\le\frac{\sqrt{c_\psi}}{4a^{(L-1)/2}}
       \le\frac{\sqrt{c_\psi}}{4a^{(\ell-1)/2}}.
\]
Apply (III.A.2) to the coupling of the initialized and trained fields in (III.A.1), then use (III.A.4). This proves, for every sample, layer, and time,
\[
\inf_{\alpha,\beta}
 E[(\phi(Z_i^\ell(t))-\alpha-\beta Z_i^\ell(t))^2]
\ge \frac{e^2c_\psi}{16a^{\ell-1}}
\ge \frac{e^2c_\psi}{16a^{L-1}}.                         \tag{III.A.12}
\]

Now let \(\mathcal C\subset\mathcal B\) be any class with a common interval \(r\ge1\) and common margin \(j>0\):
\[
                         J_r(\psi)\ge j
                         \quad(\psi\in\mathcal C).
\]
Set \(c_0=e^{-r^2/2}j/\sqrt{2\pi}\), and use (III.A.10) with \(c_\psi\) replaced by \(c_0\). The density bound, gain arithmetic, and proof of (III.A.12) then hold for every \(\psi\in\mathcal C\), with this same \(a\) and the common lower bound
\[
\frac{e^2c_0}{16a^{\ell-1}}\ge\frac{e^2c_0}{16a^{L-1}}.
\]
More generally it is enough for each member to have a possibly different interval witnessing \(c_\psi\ge c_0>0\); the argument uses only the common constant \(c_0\).

These interval classes contain open neighborhoods of many shapes. To check this without a compactness assertion about the class, choose a bounded nonconstant \(\psi_*\) with \(\|\psi_*\|_{C_b^2}<1\), and choose \(r\) with \(J_r(\psi_*)>0\). Testing an optimal affine fit for one function in the other interval problem gives
\[
\left|\sqrt{J_r(\psi_*+u)}-\sqrt{J_r(\psi_*)}\right|
                       \le\|u\|_{L^2[-r,r]}
                       \le\sqrt{2r}\|u\|_\infty.
\]
Thus any positive radius \(\rho\) satisfying
\[
\rho\le\frac{1-\|\psi_*\|_{C_b^2}}2,\qquad
\rho\le\frac{\sqrt{J_r(\psi_*)}}{2\sqrt{2r}}
\]
gives \(\psi_*+u\in\mathcal B\) and
\(J_r(\psi_*+u)\ge J_r(\psi_*)/4\) whenever
\(\|u\|_{C_b^2}<\rho\). Section III.A.4 below verifies explicitly that such neighborhoods have infinitely many independent directions.

#### III.A.3. Why the broad class cannot have a positive depth-uniform margin

Let \(\psi\) be any nonzero compactly supported \(C^2\) function, normalized into \(\mathcal B\). For every \(\sigma>0\), testing the regression problem with the zero affine function gives
\[
0\le\mathcal R_\psi(\sigma G)
\le E[\psi(\sigma G)^2]
\le\frac1{\sigma\sqrt{2\pi}}\int_{\mathbb R}\psi(x)^2\,dx.
                                                               \tag{III.A.13}
\]
The integral is finite by compact support and continuity. Thus the Gaussian regression residual tends to zero as \(\sigma\to\infty\).

Keep \(a\ge4\) and \(e\in(0,1]\) fixed, and consider networks with increasing depth. Their initialized marginal variances satisfy (III.A.8), so \(\sigma_\ell\to\infty\). At initialization, (III.A.4) and (III.A.13) therefore give
\[
\inf_{\alpha,\beta}
 E[(\phi(Z_i^\ell(0))-\alpha-\beta Z_i^\ell(0))^2]
=e^2\mathcal R_\psi(\sigma_\ell G)\longrightarrow0.
\]
In particular even this single admissible perturbation admits no positive lower bound uniform over all hidden depths and all times: the proposed bound would already fail at \(t=0\). This explains the depth-dependent margin in the broad theorem. It does not assert that the particular numerical lower bound (III.A.12) is optimal.

#### III.A.4. A stronger class with a positive depth-uniform margin

Suppose instead that a class \(\mathcal C\subset\mathcal B\) satisfies
\[
\inf_{\psi\in\mathcal C}\inf_{\sigma\ge1}
                  \mathcal R_\psi(\sigma G)\ge\eta_0>0.  \tag{III.A.14}
\]
Choose the common gain
\[
a=\max\left\{10^{12}(1+T_0),
       \left(\frac{2^{36}T_0^2}{\sqrt{\eta_0}}\right)^{2/5}\right\}.
                                                               \tag{III.A.15}
\]
The arithmetic in (III.A.11), now with \(\eta_0\), gives
\[
d_La^{(L-1)/2}\le\sqrt{\eta_0}/8,
\qquad d_L\le\sqrt{\eta_0}/8<\sqrt{\eta_0}/4.
\]
Since \(\sigma_\ell\ge1\), (III.A.14) supplies an initialized square-root residual at least \(\sqrt{\eta_0}\). By (III.A.1)–(III.A.2), its trained square-root residual is at least
\(\sqrt{\eta_0}-2d_L\ge\sqrt{\eta_0}/2\). Thus (III.A.4) proves
\[
\inf_{t\ge0}\inf_{\alpha,\beta}
 E[(\phi(Z_i^\ell(t))-\alpha-\beta Z_i^\ell(t))^2]
                              \ge e^2\eta_0/4            \tag{III.A.16}
\]
for every fixed \(L\ge2\), every \(1\le\ell\le L\), every sample, and every member of the class. Neither \(\eta_0\) nor the selected \(a\) changes with depth. The same fixed perturbation amplitude \(e\) is used throughout.

We now construct a nonempty infinite-dimensional open \(C_b^2\) ball satisfying (III.A.14).

First consider any bounded continuous nonconstant function \(\psi\) with distinct limits \(\ell_-,\ell_+\) at negative and positive infinity. For \(\sigma>0\), the functions \(1,G\) are orthonormal in Gaussian \(L^2\), and
\(\operatorname{span}\{1,\sigma G\}=\operatorname{span}\{1,G\}\). Direct completion of squares gives
\[
\mathcal R_\psi(\sigma G)
=E[\psi(\sigma G)^2]
 -(E[\psi(\sigma G)])^2
 -(E[G\psi(\sigma G)])^2.                               \tag{III.A.17}
\]
This is strictly positive for every fixed \(\sigma>0\). Indeed a zero residual would give \(\psi(\sigma G)=\alpha+\gamma G\) almost surely. The difference of these continuous functions of \(G\) would then vanish everywhere: if it were nonzero at one point, continuity would make it nonzero on an open interval of positive Gaussian probability. Therefore \(\psi(x)=\alpha+(\gamma/\sigma)x\) on all of \(\mathbb R\). Boundedness forces \(\gamma=0\), contradicting nonconstancy.

The residual in (III.A.17) is continuous in \(\sigma>0\). For any convergent positive scale sequence, continuity of \(\psi\) gives pointwise convergence of the integrands. Boundedness of \(\psi\) bounds the first two integrands by constants and the last by a constant times \(|G|\), which is integrable. Dominated convergence gives the assertion.

Put
\[
m=(\ell_++\ell_-)/2,\qquad b=(\ell_+-\ell_-)/2\ne0.
\]
For every \(G\ne0\), which holds with probability one,
\(\psi(\sigma G)\to m+b\,\operatorname{sgn}(G)\) as
\(\sigma\to\infty\). Boundedness gives convergence in \(L^2\). The limit of (III.A.17) is consequently
\[
b^2\bigl(1-(E|G|)^2\bigr)=b^2(1-2/\pi)>0.              \tag{III.A.18}
\]
Here \(E\operatorname{sgn}(G)=0\) by symmetry and
\[
E|G|=\frac2{\sqrt{2\pi}}
       \int_0^\infty x e^{-x^2/2}\,dx=\sqrt{2/\pi}.
\]
Choose a finite \(M\ge1\) such that the residual for every \(\sigma\ge M\) is at least half its positive limit in (III.A.18). On the compact interval \([1,M]\), the continuous strictly positive residual attains a strictly positive minimum. The smaller of these two positive bounds proves
\[
                       \inf_{\sigma\ge1}
                          \mathcal R_\psi(\sigma G)>0.   \tag{III.A.19}
\]
This argument proves positivity of an actual numerical constant associated with a fixed function; it does not assume a compactness property for an infinite function class.

Apply it to
\[
\psi_0(x)=\tfrac14\arctan x.
\]
Its derivatives are
\[
\psi_0'(x)=\frac1{4(1+x^2)},\qquad
\psi_0''(x)=-\frac{x}{2(1+x^2)^2}.
\]
Thus
\[
\|\psi_0\|_\infty=\pi/8,\quad
\|\psi_0'\|_\infty=1/4,\quad
\|\psi_0''\|_\infty=3\sqrt3/32,
\qquad \|\psi_0\|_{C_b^2}=\pi/8<1.
\]
For the second derivative maximum, differentiating
\(x/(1+x^2)^2\) on \(x\ge0\) gives derivative
\((1-3x^2)/(1+x^2)^3\); its unique positive critical point is \(x=1/\sqrt3\), which yields the displayed value.
The tail limits are \(-\pi/8,\pi/8\), so (III.A.18) has the positive value
\(\pi^2(1-2/\pi)/64\). Define
\[
\eta_b=\inf_{\sigma\ge1}\mathcal R_{\psi_0}(\sigma G)>0,
\qquad
\rho=\min\left\{\frac{1-\pi/8}{2},\frac{\sqrt{\eta_b}}2\right\}>0.
\]
Consider the open ball
\[
\mathcal C_\rho
=\{\psi_0+u:\ u\in C_b^2(\mathbb R),\ \|u\|_{C_b^2}<\rho\}.
\]
It is an open \(C_b^2\) ball contained in \(\mathcal B\), hence also open relative to the normalized admissible class. Indeed its members have norm at most
\(\pi/8+\rho<1\). By (III.A.3), for every \(\sigma\ge1\),
\[
\sqrt{\mathcal R_{\psi_0+u}(\sigma G)}
\ge\sqrt{\eta_b}-\|u\|_\infty
\ge\sqrt{\eta_b}/2.
\]
Thus this entire ball satisfies (III.A.14) with the single constant
\[
                              \eta_0=\eta_b/4>0.         \tag{III.A.20}
\]
In particular all its members are nonconstant. This constant depends only on the displayed fixed center and radius, and is independent of \(\delta\); the gain in (III.A.15) still depends on \(\delta\) through \(T_0\).

For an explicit verification of infinite dimensionality, let
\[
v(x)=c(1-x^2)^3\mathbf1_{\{|x|<1\}},
\]
where \(c>0\) is small enough that \(\|v\|_{C_b^2}\le1\).
The function and its first two derivatives vanish at the endpoints \(\pm1\), so it is a nonzero compactly supported \(C_b^2\) function. The translates \(v_k(x)=v(x-3k)\), \(k\ge1\), have disjoint supports. For every positive integer \(N\) and any real coefficients with \(\max_{k\le N}|s_k|<\rho\),
\[
\left\|\sum_{k=1}^Ns_kv_k\right\|_{C_b^2}
\le\max_{k\le N}|s_k|<\rho.
\]
The translates are linearly independent, since each is nonzero on a support disjoint from all the others. Hence the ball contains parameter families of arbitrarily large finite dimension, proving it has infinitely many independent directions.

Membership in this ball does not require tail limits or oddness. For example a sufficiently small cosine perturbation belongs to the ball and has oscillating tails and breaks oddness. Its common lower bound follows from the uniform norm estimate (III.A.3), even though the tail-limit proof applies only to the fixed center. The full activation remains strictly increasing because
\(\phi'=a+e\psi'\ge a-e>0\).

#### III.A.5. Scope of the uniform conclusions

For a class with a common finite-interval margin, the same gain and all main-theorem conclusions hold for every fixed member and every fixed finite depth, with the common lower bound (III.A.12). For a class satisfying (III.A.14), the same parameter recipe with \(\eta_0\) instead of \(c_\psi\) improves that bound to (III.A.16), uniform also in hidden depth.

The finite-width convergence statements retain their original quantifiers: the function, dataset, finite depth, and observation horizon are fixed before width tends to infinity. Sharing constants across a class does not by itself assert uniform finite-width convergence over that infinite class, simultaneous width/depth limits, or a positive margin independent of \(e\) as \(e\downarrow0\). The construction uses the original raw metric and the displayed affine-plus-perturbation activation throughout.



# Complete linear trace-space dependency

### 2.A. Compact operators and the complete trace-norm space

The following foundations apply to the separable real Hilbert spaces in this
chapter, including finite-dimensional spaces. They also apply to the complex
Hilbert spaces below by taking real and imaginary variations where needed.
For vectors in the output and input spaces, respectively, write
\((u\otimes v)x=u\langle v,x\rangle\). An operator is compact if the image
of its unit ball has compact closure. All operator norms below are ordinary
Hilbert operator norms.

**Lemma 2.A.** A compact operator \(T:H\to K\) has an expansion
\[
 T=\sum_{j\ge1}s_j u_j\otimes v_j,
 \qquad s_1\ge s_2\ge\cdots>0,
 \tag{2.A.1}
\]
with orthonormal vector lists and operator-norm convergence; the list can
terminate. Its singular values are these numbers, padded by zeros as needed.
They satisfy
\[
 s_j(T)=\inf_{\operatorname{rank}R<j}\|T-R\|,
 \qquad |s_j(T)-s_j(S)|\le\|T-S\|.                 \tag{2.A.2}
\]
The compact operators with \(\|T\|_1=\sum_j s_j(T)<\infty\) form a Banach
space. Finite-rank truncations converge in this norm, and
\[
 \|T\|\le\|T\|_1,\qquad
 \|ATB\|_1\le\|A\|\|T\|_1\|B\|,
 \qquad \|u\otimes v\|_1=\|u\|\|v\|.             \tag{2.A.3}
\]
For square trace-class operators the trace is independent of the orthonormal
basis, is linear, obeys \(|\operatorname{Tr}T|\le\|T\|_1\), and satisfies
\(\operatorname{Tr}(AT)=\operatorname{Tr}(TA)\) for bounded \(A\).
Also \(\|T\|_{\mathrm{HS}}=(\sum_j s_j(T)^2)^{1/2}\le\|T\|_1\).

**Proof of the singular expansion.** A bounded sequence in a separable
Hilbert space has a weakly convergent subsequence: choose a countable
orthonormal basis, successively select subsequences on which each coordinate
converges, and take the diagonal subsequence. The sum of squares of the
limiting coordinates is bounded by the common squared norm, by passing to
the limit in every finite partial sum. The resulting Hilbert vector is the
weak limit, because finite-coordinate tests converge and their orthogonal
tails have uniformly small pairings with any fixed test vector. This argument
also covers finite dimension.

If \(T\ne0\) is compact, choose unit vectors with image norms tending to
\(\|T\|\). Pass to a weakly convergent subsequence and then, by compactness,
to a subsequence whose images converge in norm. The image limit is \(Tv\):
testing against \(w\) gives \(\langle w,Tv_i\rangle=\langle T^*w,v_i\rangle\).
Consequently \(\|Tv\|=\|T\|\) and \(\|v\|=1\); a smaller norm would
contradict the definition of \(\|T\|\). Differentiating
\(\|T(v+th)/\|v+th\|\|^2\) at zero for \(h\perp v\) shows
\(T^*Tv=\|T\|^2v\). In the complex case also replace \(h\) by \(ih\).
Set \(s_1=\|T\|\), \(v_1=v\), and \(u_1=Tv_1/s_1\).

The restriction of \(T\) to \(v_1^\perp\) has image in \(u_1^\perp\),
since \(\langle u_1,Th\rangle=s_1\langle v_1,h\rangle\).
Repeat the construction on the successive orthogonal complements. The
restrictions remain compact, and their norms give a nonincreasing sequence
\(s_j\). If infinitely many \(s_j\) were bounded below by \(b>0\), the
images \(Tv_j=s_ju_j\) would be mutually at distance at least \(\sqrt2 b\),
contradicting compactness. Thus \(s_j\to0\). The remainder after \(N\)
terms has norm \(s_{N+1}\), by its construction as the next restriction,
which proves (2.A.1). If a restriction is zero, the series terminates there.

Truncation before term \(j\) proves the upper bound in (2.A.2). Conversely,
if \(\operatorname{rank}R<j\) and \(s_j>0\), some unit vector in
\(\operatorname{span}(v_1,\ldots,v_j)\) lies in \(\ker R\); on this span
\(\|Tx\|\ge s_j\|x\|\). This gives the lower bound. If \(s_j=0\)
the lower bound is automatic. Applying the infimum formula to \(T-R\)
and \(S-R\), then exchanging \(T,S\), proves its Lipschitz assertion.

**The norm and completeness.** For \(m\) not exceeding either Hilbert-space
dimension, the singular expansion gives
\[
 \sum_{j=1}^m s_j(T)
 =\sup_{(e_i),(f_i)}
       \left|\sum_{i=1}^m\langle f_i,Te_i\rangle\right|,   \tag{2.A.4}
\]
where both lists are orthonormal in their respective spaces. To check the
upper bound without a trace theorem, substitute (2.A.1). The coefficient
\(c_j\) of \(s_j\) then satisfies
\[
 |c_j|\le
 \left(\sum_i|\langle f_i,u_j\rangle|^2\right)^{1/2}
 \left(\sum_i|\langle v_j,e_i\rangle|^2\right)^{1/2}\le1,
 \qquad \sum_j|c_j|\le m.
\]
The last inequality is Cauchy--Schwarz in \(j\) followed by Bessel in each
list. A decreasing nonnegative sequence \(s_j\) therefore has
\(\sum_j s_j|c_j|\le\sum_{j\le m}s_j\): move any weight on indices
above \(m\) into unused capacity among the first \(m\) indices.
Equivalently, bound the tail by \(s_m\sum_{j>m}|c_j|\) and use
\(s_j\ge s_m\) for \(j\le m\). The series is absolutely convergent
because \(s_j\le\|T\|\) and \(\sum_j|c_j|\le m\).
Equality is attained by singular vectors, filling a terminated list with
orthonormal vectors in the orthogonal complements. This proves (2.A.4).

Its supremum expression gives the triangle inequality for partial singular
value sums and hence for \(\|\cdot\|_1\) on letting \(m\) increase to the
smaller dimension, or to infinity. Homogeneity and definiteness follow from
(2.A.1) and \(s_1=\|T\|\). Finite-rank operators are compact, and compact
operators are closed in operator norm: for every tolerance, a nearby compact
operator supplies a finite net for the image of the unit ball. The latter
image is consequently totally bounded; its closure is compact in the complete
Hilbert space (successively select subsequences in nets of radii tending to
zero to obtain a Cauchy subsequence).

Let \(T_n\) be trace-norm Cauchy. It is operator-norm Cauchy, so it converges
to a bounded operator \(T\): define \(Tx=\lim_nT_nx\) in the complete
output Hilbert space, and the uniform Cauchy bound gives operator-norm
convergence. The limit is compact by the preceding paragraph. Given
\(\varepsilon>0\), choose \(N\) with \(\|T_n-T_k\|_1\le\varepsilon\)
for \(n,k\ge N\). For each fixed \(m,n\), (2.A.2) lets \(k\to\infty\)
in the finite partial sum to give
\(\sum_{j\le m}s_j(T-T_n)\le\varepsilon\) whenever \(n\ge N\).
Letting \(m\) increase proves \(\|T-T_n\|_1\le\varepsilon\).
In particular \(T-T_N\) and then \(T\) are trace class. This proves
completeness. The tail in (2.A.1) has exactly the remaining singular values,
so its trace norm is \(\sum_{j>N}s_j\), proving finite-rank density.

**Ideals, trace and Hilbert--Schmidt norm.** A rank-one map has just one
nonzero singular value, \(\|u\|\|v\|\), by direct evaluation on
\(v/\|v\|\); zero vectors cause no exception. For a trace-class \(T\),
apply bounded \(A,B\) termwise to (2.A.1). The resulting rank-one norms
sum to at most \(\|A\|\|B\|\sum_j s_j\). Completeness makes this series
converge in trace norm, and its operator-norm limit is \(ATB\). This proves
the ideal inequality, including rectangular compatible spaces.

For square operators and any orthonormal basis \((e_k)\),
\[
 \sum_k|\langle e_k,Te_k\rangle|
 \le\sum_j s_j\sum_k
       |\langle e_k,u_j\rangle\langle v_j,e_k\rangle|
 \le\sum_j s_j.
\]
Cauchy--Schwarz and Parseval justify the last inequality. Absolute summation
permits exchange of \(k,j\), giving
\(\sum_k\langle e_k,Te_k\rangle=\sum_js_j\langle v_j,u_j\rangle\),
independent of the basis. Define this common sum to be \(\operatorname{Tr}T\).
The basis expression proves linearity; the displayed bound gives continuity.
The rank-one formula and the trace-norm convergent series give
\[
 \operatorname{Tr}(AT)
 =\sum_js_j\langle v_j,Au_j\rangle
 =\operatorname{Tr}(TA).
\]
Likewise Parseval and nonnegative summation give
\(\sum_k\|Te_k\|^2=\sum_js_j^2\); this is independent of the basis.
It identifies the Hilbert--Schmidt norm with the norm of the square-summable
column list, so its triangle and Cauchy--Schwarz inequalities are the Hilbert
ones. The inequality \((\sum_js_j^2)^{1/2}\le\sum_js_j\) completes (2.A.3)
and the stated Hilbert--Schmidt bound.

Two consequences used in the width comparisons also follow directly.
If \(V,W\) are finite column maps and \(D\) is a finite coefficient matrix,
the nonzero singular values of \(VDW^*\) are those of
\[
 (V^*V)^{1/2}D(W^*W)^{1/2}.                          \tag{2.A.5}
\]
Indeed the rule \((V^*V)^{1/2}x\mapsto Vx\) is well-defined and isometric
on its range, because both squared norms equal \(x^*V^*Vx\). Extend it
by zero on the orthogonal complement to obtain a partial isometry \(U_V\),
and do the same for \(W\). Then \(V=U_V(V^*V)^{1/2}\), and the middle
matrix in (2.A.5) maps between precisely these isometric support spaces.
Adding zero directions changes no nonzero singular value. No Gram inverse
is involved. In finite dimension positive square roots are continuous:
bounded roots have convergent subsequences; any subsequential limit is
positive and squares to the limiting matrix, whose positive square root is
unique by finite-dimensional diagonalization. This, (2.A.2), and finiteness
of the matrix dimension prove continuity of the trace norm in (2.A.5).

Finally, if \(R\) has rank at most \(m\), adding it to a rank-\(<j\)
approximation of \(T-R\) and using (2.A.2) gives
\(s_{j+m}(T)\le s_j(T-R)\). Thus
\[
 \sum_{j>m}s_j(T)\le\|T-R\|_1.                     \tag{2.A.6}
\]
This controls the full trace-norm tail, not only finitely many singular
values. All completeness and operator-ideal facts needed for the subsequent
integral contractions and continuation arguments have now been proved.


# Complete linear Gaussian-word dependency

## 9. A Gaussian source lemma with contained norm and Wick proofs

For the linear comparisons we need only fixed words in finitely many
independent Gaussian matrices, not a theorem about a growing adaptive
program. The following expands the proof of Lemma 2 in this chapter to an
arbitrary separately fixed finite number of matrix labels. No sharp spectral
edge estimate is needed.

Fix a nonnegative integer \(q\). Let \(B_{j,n}\), \(1\le j\le q\), have mutually
independent \(N(0,1/n)\) entries. Let \(g_{1,n},g_{2,n}\) be independent
\(N(0,I_n/n)\) vectors independent of these matrices. All norms here are
ordinary finite Euclidean or operator norms.
Empty maxima of nonnegative quantities and empty sums below mean zero.

Take the real full word Hilbert space

\[
\mathcal F_q=\mathbb R\Omega\oplus
 \bigoplus_{k\ge1}(\mathbb R^{2q})^{\otimes k}.
\tag{EC9.1}
\]

For \(q=0\) this means \(\mathbb R\Omega\). For \(q>0\), the left
creation operator \(\ell_{j,+}\) (respectively \(\ell_{j,-}\)) prepends
the indicated letter to a word. Its actual Hilbert adjoint deletes that
first letter when it matches and returns zero otherwise. Put

\[
c_j=\ell_{j,+}+\ell_{j,-}^*,\quad
\mathcal H=\mathcal F_q\oplus\mathcal F_q,\quad
\Gamma_j=c_j\oplus c_j,\quad
g_1=(\Omega,0),\quad g_2=(0,\Omega).
\tag{EC9.2}
\]

Creation is an isometry, so \(\|\Gamma_j\|\le2\); both roots have norm
one. For a word \(P\) with transpose letters, \(P(\Gamma)\) uses actual
adjoints at those letters. Set
\(\tau(P)=\langle\Omega,P(c)\Omega\rangle\).

**Lemma EC9.** Every fixed finite collection of rooted Gram entries obeys

\[
\langle P_n g_{i,n},Q_n g_{j,n}\rangle
\xrightarrow{\mathbb P}
\langle P(\Gamma)g_i,Q(\Gamma)g_j\rangle
=\mathbf1_{i=j}\tau(P^*Q).
\tag{EC9.3}
\]

The assertion also holds for typed compatible words between copies of
\(\mathcal H\). Moreover

\[
\mathbb P\{\max_j\|B_{j,n}\|\le12,
                 \|g_{1,n}\|\le2,\|g_{2,n}\|\le2\}\longrightarrow1.
\tag{EC9.4}
\]

**Proof.** A maximal \(1/4\)-separated subset \(\mathcal N\) of the
Euclidean unit sphere is a \(1/4\)-net. Disjoint balls of radius \(1/8\)
around its points fit in the radius-\(9/8\) ball, so
\(|\mathcal N|\le9^n\). Approximating each of the two unit vectors in
a bilinear form shows
\(\|B\|\le2\max_{a,b\in\mathcal N}|a^TBb|\).
Each form is \(N(0,1/n)\). For such a variable \(Z\),
\(\mathbb E e^{tZ}=e^{t^2/(2n)}\); minimizing
\(e^{-tu}\mathbb E e^{tZ}\) over \(t>0\) bounds its upper tail by
\(e^{-nu^2/2}\), and symmetry bounds both tails. Therefore

\[
\mathbb P\{\|B\|>12\}\le2\,81^ne^{-18n}.
\tag{EC9.5}
\]

For a normalized Gaussian vector its squared norm has mean one and
variance \(2/n\), so Chebyshev's inequality and a finite union prove
(EC9.4). This argument asserts boundedness in probability, not convergence
of the largest singular value to two.

For clarity we prove the word law as well. The Gaussian moment-generating
function is \(\exp(t^T\Sigma t/2)\). Differentiating at zero shows that
an even product of centered Gaussian coordinates has expectation equal
to the sum over pairings of covariance products; odd products have zero
mean. This is Wick's identity, including singular finite covariance.
Equivalently it follows by repeated Gaussian integration by parts, as in
Section 4 of `gaussian_calculus.md`.

Expand a normalized trace word of length \(2k\) into entries. Regard the
trace indices as vertices of a closed walk, with one side per matrix
occurrence. A nonzero Wick pair has the same matrix label, contributes
\(1/n\), and identifies the two raw row indices and the two raw column
indices. A transpose letter exchanges which endpoint of its side is the
raw row. After all identifications, the quotient multigraph is connected
and has \(k\) paired edges. If it has \(v\) free index vertices, its
contribution is exactly

\[
n^{v-k-1}.
\tag{EC9.6}
\]

A connected graph with \(k\) edges has at most \(k+1\) vertices, because
a spanning tree uses \(v-1\) edges. Equality holds exactly for a tree.
In that case the original walk uses every edge twice, once in each
direction: removing an edge separates the tree into two components and
a closed walk must enter and leave each component equally often. Since
the raw row and column of paired entries were identified in the same
order, this opposite traversal forces opposite transpose markers.
At a leaf the two occurrences are adjacent in the cyclic walk and can
be removed. Repeating this removal proves that the pairing is noncrossing.
Conversely any noncrossing pairing with matching labels and opposite
transpose markers can be reduced by adjacent-pair removal. Restoring
each removed pair introduces one free index; hence it has \(k+1\)
vertices. These and only these pairings survive as \(n\to\infty\).

Expanding each \(c_j\) and \(c_j^*\) in (EC9.2), an annihilator can
only remove the first currently present letter of its own color. A
vacuum contribution is therefore precisely a nested matching of
annihilators to creations. The two letters available for each label
permit a match exactly between opposite transpose markers of that label.
Every such matching contributes one. This identifies the surviving
pairings in (EC9.6) with \(\tau\) of the word. Odd words vanish on both
sides.

For the variance, use two copies of a trace walk. Pairings with no edge
joining the walks cancel against the product of expectations. Every
remaining quotient graph is connected. If there are \(k\) paired edges
in total, it has at most \(k+1\) vertices; the two trace normalizations
give \(n^{v-k-2}=O(n^{-1})\). There are finitely many pairings at fixed
length. Thus each normalized trace word converges in \(L^2\) to its
vacuum value. Linearity gives the same statement for any fixed polynomial.

Finally let \(T\) be a real matrix independent of the two normalized
Gaussian roots. Wick's identity gives

\[
\mathbb E[g^TTg\mid T]=\operatorname{Tr}T/n,\qquad
\operatorname{Var}(g^TTg\mid T)
=2\|\operatorname{sym}T\|_{\mathrm{HS}}^2/n^2
\le2\|T\|^2/n,
\tag{EC9.7}
\]
\[
\mathbb E[g^TTh\mid T]=0,\qquad
\mathbb E[|g^TTh|^2\mid T]
=\|T\|_{\mathrm{HS}}^2/n^2\le\|T\|^2/n
\quad(g,h\text{ independent}).
\tag{EC9.8}
\]

Use \(T=P_n^TQ_n\). On the matrix-measurable event
\(\max_j\|B_{j,n}\|\le12\),
its norm is bounded by a constant depending only on the fixed words.
Conditional Chebyshev, (EC9.5) for the complement, and the trace limit
give (EC9.3). A finite union gives joint convergence. The direct sum in
(EC9.2) makes the entire two rooted subspaces orthogonal; orthogonality
of just the two roots would not suffice. Typed words form a subset of
these word identities, so restricting to them proves the typed assertion.
\(\square\)

