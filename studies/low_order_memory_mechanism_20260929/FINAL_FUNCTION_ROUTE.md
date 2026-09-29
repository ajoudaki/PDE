# The finite-memory model as a learned function

This scoped theoretical route uses `MODEL.md` in full and the maintained
notation contract. All statements concern the closure's own trajectory at
finite width, with finite memory order `q >= 1`. No dense comparison, width
limit, experiment, or novelty claim is used. The general identities apply to
arbitrary sample count and hidden depth. The explicit terminal example uses
one sample and two hidden layers. The one-sample activity calculation was
cross-checked with the concurrently assigned learning route after the
supervisor authorized that coordination.

The strongest conclusion is that the terminal predictor has an exact
final-feature interpolation component **plus a history-dependent component
invisible on the training set**. The second component can be nonzero at a
converged interpolating endpoint of the specified closure, for every finite
`q >= 1`, on an open set of admissible initializations.

## 1. Exact retrieval of a test input by the temporal memories

Fix a finite stopping time `T` for which the model solution exists. Every
quantity below is evaluated on that solution. For a test input `x`, compute
its features using the current reconstructed weights. With

\[
A_a(T)=\int_0^T r_a(t)\delta_a^{(1)}(t)\,dt,
\]

the first preactivation is exactly

\[
z_T^{(1)}(x)=\frac{W^{(1)}(0)x}{\sqrt d}
-\frac2m\sum_a A_a(T)\frac{x_a^Tx}{d}.
\tag{1}
\]

Thus first-layer learning factors through the input Gram similarities to the
training set. If `x` is perpendicular to every training input, its first
preactivation is unchanged. This does not freeze its later features or its
prediction.

For every hidden link, the exact test recursion is

\[
z_T^{(\ell)}(x)=W_\ell^0h_T^{(\ell-1)}(x)
-\frac2m\sum_{a,k}\frac{2k+1}{\tau(T)}C_{\ell,a,k}(T)
\frac{B_{\ell,a,k}(T)^Th_T^{(\ell-1)}(x)}n.
\tag{2}
\]

The input to the adapter is the vector of similarities to the forward
memories; its output is a linear combination of backward-credit memories.
Consequently the learned increment has rank at most `mq`, annihilates the
orthogonal complement of the forward-memory span, and has image contained
in the backward-memory span. Composition with the fixed operators and
coordinatewise nonlinearities remains essential: rank `mq` at each link
does not make the entire learned function linear or give it an
`mq`-dimensional global function space.

There is a precise temporal interpretation of those similarities. Write
`tau = tau(T)` and let `P_q` be the orthogonal projector in
`L^2([0,tau])` onto polynomials of degree at most `q-1`, acting coordinatewise
on vector histories. Its kernel is

\[
K_q^\tau(\xi,\eta)=\frac1\tau\sum_{k=0}^{q-1}(2k+1)
p_k(\xi/\tau)p_k(\eta/\tau).
\]

For a fixed test feature vector `v`, define the historical similarity
`c_{a,v}(xi)=h_a^{(ell-1)}(xi)^T v/n`, including the model's constant
initial prefix. Substituting the moment integrals into the reconstruction
and interchanging the finite sum and integrals gives

\[
(W_\ell(T)-W_\ell^0)v
=-\frac2m\sum_a\int_0^\tau
b_a^{(\ell)}(\xi)(P_qc_{a,v})(\xi)\,d\xi.
\tag{3}
\]

Equivalently, one can project the backward history and leave the scalar
similarity unprojected, by self-adjointness of `P_q`. Equation (3) says what
the retained temporal modes do to a new input: they filter the *variation
of its similarity to past training features* before retrieving past credit.
For `q=1`, only the average similarity survives. For higher `q`, the retained
similarity is its polynomial projection; its pointwise weights need not be
positive. These identities use historical functions only to interpret the
stored moments and do not introduce additional state into the algorithm.

The readout gives a second exact identity:

\[
f_T(x)=-\frac2m\sum_a\int_0^T r_a(t)
\frac{h_t^{(L)}(x_a)^Th_T^{(L)}(x)}n\,dt.
\tag{4}
\]

The features in the two arguments live at different training times. Hence
(4) is a cross-time representation, not a fixed symmetric-kernel
representer theorem. The next decomposition makes its difference from a
final-feature representer solution explicit.

## 2. Final-feature interpolation and its invisible history component

Set

\[
H_T=[h_T^{(L)}(x_1),\ldots,h_T^{(L)}(x_m)]\in\mathbb R^{n\times m},
\quad G_T=H_T^TH_T/n,
\quad k_T(x)=H_T^Th_T^{(L)}(x)/n.
\]

Let `p_T` be the vector of training predictions, and let `P_T` denote the
Euclidean orthogonal projector onto the column span of `H_T`. Use a
Moore--Penrose pseudoinverse, so no nonsingularity of `G_T` is assumed. Define
`u_T=(I-P_T)w_T`. Then

\[
f_T(x)=k_T(x)^TG_T^\dagger p_T
+\frac{u_T^Th_T^{(L)}(x)}n.
\tag{5}
\]

Indeed `p_T=H_T^Tw_T/n` belongs to the range of `G_T`, and

\[
P_T=\frac1nH_TG_T^\dagger H_T^T,
\qquad P_Tw_T=H_TG_T^\dagger p_T.
\]

Substituting `w_T=P_Tw_T+u_T` proves (5). The first summand is the predictor
from the unique readout of smallest Euclidean norm that has the same
training predictions with these fixed final features. Orthogonality gives

\[
\frac{\|w_T\|_2^2}{n}
=p_T^TG_T^\dagger p_T+\frac{\|u_T\|_2^2}{n}.
\tag{6}
\]

The extra term in (5) vanishes at every training input because
`H_T^T u_T=0`. It is not otherwise forced to vanish. From the stored-readout
equation and `w(0)=0`, it has the exact historical source

\[
u_T=\frac2m\sum_a\int_0^T r_a(t)(I-P_T)
\bigl[h_T^{(L)}(x_a)-h_t^{(L)}(x_a)\bigr]dt.
\tag{7}
\]

This follows by projecting the integral for `w_T` and using
`(I-P_T)h_T^{(L)}(x_a)=0`. In particular, motion of the training features
*outside their final span* is precisely what can produce this component.
If the entire training-feature history lies in the final span, then it is
zero; frozen features are a special case.

Taking norms in (7) and applying Cauchy--Schwarz across samples proves

\[
\frac{\|u_T\|_2}{\sqrt n}
\le 2\int_0^T\rho(t)
\left[\frac1m\sum_a
\frac{\|(I-P_T)(h_T^{(L)}(x_a)-h_t^{(L)}(x_a))\|_2^2}{n}
\right]^{1/2}dt.
\tag{8}
\]

For tanh, `||h_T^{(L)}(x)||_2/sqrt(n) <= 1` for every input, so

\[
\sup_{x\in\mathbb R^d}
\left|f_T(x)-k_T(x)^TG_T^\dagger p_T\right|
\le\frac{\|u_T\|_2}{\sqrt n}.
\tag{9}
\]

At an interpolating terminal state, (5)--(9) hold with `p_T=y` and terminal
quantities. One may apply the finite-state algebra directly to that state;
passing (7) to infinite time additionally requires convergence and an
integrable dominating bound on its integrand. Neither interpolation nor
convergence is presumed for arbitrary datasets.

The minimum in (6) is a minimum *readout* norm for the realized final
features. To identify it with a function-space norm without a quotient,
the feature map must span the relevant parameter space over all inputs.
The example below satisfies that condition and makes the distinction
observable at unseen inputs.

## 3. A converged interpolating endpoint with a nonzero history component

Fix `m=1`, `d=1`, `x_1=1`, `L=2`, and arbitrary finite `q >= 1`. Write the
initial first weights as `p in R^n` and the initial hidden matrix as `M`.
Introduce only for this calculation

\[
h=\tanh p,\quad a=\tanh(Mh),\quad
E=\operatorname{diag}(\operatorname{sech}^2p),\quad
D=\operatorname{diag}(\operatorname{sech}^2(Mh)),
\]

\[
\alpha=\|a\|_2^2/n,\quad k=\|h\|_2^2/n,
\qquad T=D[ME^2M^T+kI]Da.
\tag{10}
\]

Assume `a != 0`. For all sufficiently small positive labels `y`, the physical
flow exists for all time, converges to an interpolating state, and its
terminal invisible component satisfies

\[
u_y=-\frac{y^3}{3\alpha^3}(I-P_a)T+O(y^5),
\tag{11}
\]

where `P_a` projects onto `span{a}`. The constants in the remainder may
depend on the fixed initialization and fixed `q`; no uniformity in `q` is
claimed.

Here is a derivation, including convergence. On an interval with negative
residual, use the activity coordinate

\[
s=2\int_0^t|r(v)|dv,\qquad \tau=1+s/2.
\]

In this coordinate `dw/ds=h^{(2)}` and `dW_1/ds=delta^{(1)}`. The moment
equations become

\[
\frac{dB_k}{ds}=\frac12h^{(1)}-
\frac1{2\tau}\left[kB_k+\sum_{j<k}(2j+1)B_j\right],
\]

\[
\frac{dC_k}{ds}=-\frac12\delta^{(2)}-
\frac1{2\tau}\left[kC_k+\sum_{j<k}(2j+1)C_j\right].
\tag{12}
\]

These equations and their initialization contain no label magnitude. They
are a finite-dimensional smooth ODE near `s=0`, since `tau>0` there and tanh
is smooth. Local existence, uniqueness and smooth dependence therefore
apply to this fixed activity path.

At the origin `w=0`, all weight velocities vanish, and all feature
derivatives in `s` vanish. It follows first that
`w(s)=sa+O(s^3)`, `delta^{(2)}(s)=sDa+O(s^3)`, and consequently

\[
C_0(s)=-s^2Da/4+O(s^4).
\]

For every `k>0`, `B_k(s)=O(s^3)`: the constant initial feature history has
zero such Legendre moments, while its departure is `O(s^2)` on an interval
of length `O(s)`. Also `B_0(s)/tau=h+O(s^3)` and each `C_k(s)=O(s^2)`.
The reconstruction and first-weight equation now give

\[
W_2(s)=M+\frac{s^2}{2n}Da\,h^T+O(s^4),
\qquad
W_1(s)=p+\frac{s^2}{2}EM^TDa+O(s^4).
\]

Thus all finite memory orders have the same second-order feature motion:

\[
h^{(2)}(s)=a+\frac{s^2}{2}T+O(s^4),\qquad
w(s)=sa+\frac{s^3}{6}T+O(s^5).
\tag{13}
\]

The higher memory products `C_k B_k^T`, `k>0`, start at order `s^5` and do
not affect the displayed coefficients. These expansions do not assert an
exact parity symmetry at all orders.

Writing `F(s)=w(s)^Th^{(2)}(s)/n`, (13) yields

\[
F(s)=\alpha s+\frac{2a^TT}{3n}s^3+O(s^5),\qquad F'(0)=\alpha>0.
\tag{14}
\]

Choose `s_0>0` so that the path exists and
`alpha/2 <= F'(s) <= 3alpha/2` on `[0,s_0]`. Every
`0<y<F(s_0)` has a unique root `s_y` there, with
`s_y=y/alpha+O(y^3)`. The physical scalar clock solves

\[
\dot s=2(y-F(s)),\qquad s(0)=0.
\]

It stays below `s_y`. For `e=s_y-s`, the mean value theorem gives
`-3alpha e <= dot e <= -alpha e`. Therefore it approaches `s_y`
exponentially, never crosses it, and generates a global physical solution
with negative residual at every finite time and residual tending to zero.
Every parameter and moment converges by continuity of the smooth activity
path on `[0,s_y]`.

Finally (13) implies

\[
w(s)=s h^{(2)}(s)-\frac{s^3}{3}T+O(s^5).
\]

Projecting perpendicular to `h^{(2)}(s)` and using
`P_{h^{(2)}(s)}=P_a+O(s^2)` gives
`u(s)=-s^3(I-P_a)T/3+O(s^5)`. Substituting `s=s_y` proves (11).

To make (11) nonzero and observable, choose `n=2`, let
`u=artanh(1/2)>0`, and set

\[
p=(u,u)^T,\qquad M=\operatorname{diag}(1,A)
\]

for sufficiently large fixed `A>1`. Then

\[
a=(\tanh(1/2),\tanh(A/2))^T,\qquad
T=\operatorname{diag}(\lambda_1,\lambda_2)a,
\]

\[
\lambda_1=\operatorname{sech}^4(1/2)(1/4+9/16)>0,
\quad
\lambda_2=\operatorname{sech}^4(A/2)(1/4+9A^2/16)\longrightarrow0.
\]

Both entries of `a` are nonzero. Thus for large `A`,
`(I-P_a)T != 0`. The initial feature map on arbitrary inputs is

\[
h_0^{(2)}(x)=
\begin{pmatrix}\tanh(\tanh(ux))\\
\tanh(A\tanh(ux))\end{pmatrix}.
\]

Its linear and cubic Taylor coefficient vectors at zero have determinant

\[
-\frac{u^4}{3}A(A^2-1)\ne0.
\]

Indeed the component with multiplier `b` expands as
`bu x-b(1+b^2)u^3 x^3/3+O(x^5)`. Hence these features span `R^2` over
the input space: no nonzero vector is orthogonal to them for every input.
There is therefore a fixed test input `x` for which
`((I-P_a)T)^T h_0^{(2)}(x) != 0`.

At the converged endpoint, the exact difference between the learned
predictor and the final-feature minimum-readout-norm interpolant is

\[
f_y(x)-y\frac{
h_y^{(2)}(1)^Th_y^{(2)}(x)}{\|h_y^{(2)}(1)\|_2^2}
=-\frac{y^3}{3\alpha^3n}
\bigl((I-P_a)T\bigr)^Th_0^{(2)}(x)+O_x(y^5).
\tag{15}
\]

Here `h_y^{(2)}(x)=h_0^{(2)}(x)+O_x(y^2)` follows from the weight
expansions. For the selected input, (15) is nonzero for all sufficiently
small positive labels. All the nonzero coefficients and the two-input
feature-span determinant persist in an open neighborhood of this
initialization. Independent Gaussian first and hidden weights have a
strictly positive density on that neighborhood, so this is a
positive-probability family within the specified initialization model,
not a property that requires exact diagonal matrices or identical rows.

## 4. What the result identifies and what remains open

The identities describe the whole input-space function at any attained
state, and the example proves that their history term can survive actual
convergence to interpolation. They rule out an automatic theorem that
the closure always selects the minimum-readout-norm interpolant in its
own final feature map. They do not rule out a different variational
principle that includes the evolving features or their history.

The shared cubic effect for all finite `q >= 1` also prevents attributing
every observed learned-function effect to high temporal orders. Larger
`q` can alter later coefficients and the full path; no ordering of
generalization error, no general multi-input convergence theorem, and no
statistical risk statement follows from this route.
