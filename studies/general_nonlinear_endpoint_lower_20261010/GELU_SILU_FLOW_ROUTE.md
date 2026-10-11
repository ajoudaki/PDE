# GELU and SiLU: the centered endpoint flow comparison

2026-10-11. Frozen scoped proof attempt. Inputs were the complete
`paper/compact.tex`, `paper/compact_fitting.tex`,
`paper/compact_foundations.tex`, and this study's `NONODD_SCALAR_ROUTE.md`,
`NONODD_MOMENT_ROUTE.md`, and `ODD_DEPTH_ENDPOINT.md`. Required rigorous-math,
conjecture, and canonical-notation instructions and the neural-network
reference were applied. No experiment or manuscript edit was performed.

**Status: the deterministic oracle approximation in Section 6 is proved;
the direct ordinary frozen-feature endpoint comparison remains open.**
Section 6 constructs a polylogarithmic adaptive matrix-oracle simulation
whose physical parameter error at the fitted endpoint is (O(n^{-16})).
The earlier sections prove a useful mixed second/fourth Gaussian moment
estimate, specify a weaker sufficient passive moment bound, and give an
obstruction to an unconditional Gaussian-root Lipschitz argument. That
obstruction concerns a proof mechanism; it is not a counterexample to the
actual fitted-endpoint lower bound.

## 1. Exact target and activation constants

There are (m\ge2) training inputs (v_a=x_a/\sqrt d\in\mathbb R^d),
all of norm one, and (L\ge2) fixed hidden layers of width (n). The actual
network and loss are

\[
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(j)}=W^{(j)}h_a^{(j-1)},\qquad
h_a^{(j)}=\phi(z_a^{(j)}),\qquad
f_a=n^{-1}w^\top h_a^{(L)},\qquad
r_a=f_a-y_a,\qquad \mathcal L=m^{-1}\sum_a r_a^2.
\]

The matrices have shapes (n\times d) at the first layer and (n\times n)
afterward; (w\in\mathbb R^n). In the all-GELU case
\(\phi(x)=x\Phi(x)\), where \(\Phi\) is the standard normal distribution
function. In the all-SiLU case
\(\phi(x)=x\sigma(x)\), where \(\sigma(x)=(1+e^{-x})^{-1}\).
Training is the canonical gradient flow

\[
\begin{aligned}
\dot w&=-\frac2m\sum_a r_a h_a^{(L)},\\
\dot W^{(1)}&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\\
\dot W^{(j)}&=-\frac2{nm}\sum_a
r_a\delta_a^{(j)}h_a^{(j-1)\top}\quad(j\ge2),
\end{aligned}
\]

where
\(\delta_a^{(L)}=w\odot\phi'(z_a^{(L)})\) and
\(\delta_a^{(j)}=\phi'(z_a^{(j)})\odot
W^{(j+1)\top}\delta_a^{(j+1)}\).
Initialization has independent first-layer (N(0,1)) entries, independent
hidden (N(0,1/n)) entries, and (w(0)=0).

Retain precisely the paper's fixed-data assumptions

\[
\gamma=\lambda_{\min}(Q^{(L)})>0,\qquad
\lambda=\gamma/m\le1,\qquad
Y=\|y\|/\sqrt m>0,\qquad
\varepsilon=Y/\lambda\le\beta^{-30L}.
\tag{1}
\]

The training span is proper and the fixed unit query (v) is orthogonal to
it. Condition on the first-layer coordinates in that span and all hidden
matrices. Training is measurable under this conditioning, whereas

\[
Z=W_0^{(1)}v\sim N(0,I_n),\qquad W_t^{(1)}v=Z
\tag{2}
\]

remains independent. No query value enters training.

Both activations satisfy

\[
\phi(x)=x/2+\psi(x),\qquad \psi(-x)=\psi(x),\qquad
|\phi(x)|\le |x|,\qquad
\sup_{\mathbb R}|\phi'|\le2,\qquad
\sup_{\mathbb R}|\phi''|\le1.
\tag{3}
\]

For GELU, with \(\varphi(x)=e^{-x^2/2}/\sqrt{2\pi}\),
\(\phi'=\Phi+x\varphi\) and \(\phi''=(2-x^2)\varphi\).
The derivative bounds follow from
\(|x|\varphi(x)\le1/\sqrt{2\pi e}\) and maximizing the two pieces of
\(|2-x^2|e^{-x^2/2}\). For SiLU,
\(\phi'=\sigma+x\sigma'\) and
\(\phi''=2\sigma'+x\sigma'(1-2\sigma)\).
Use \(\sigma'\le1/4\), \(\sigma'(x)\le e^{-|x|}\), and
\(|x|e^{-|x|}\le1/e\). Thus no bounded-value assumption is needed.

The population diagonals obey

\[
4^{-j}\le Q^{(j)}_{11}\le1,\qquad
H=\max_{0\le j\le L}\sqrt{Q^{(j)}_{11}}=1.
\tag{4}
\]

Indeed, for a centered Gaussian (G) of variance (q), parity in (3) gives
\(\mathbb E\phi(G)^2=q/4+\mathbb E\psi(G)^2\ge q/4\), and
the absolute-value bound gives the reverse upper bound (q).

Define

\[
B_t=[h^{(L)}(t,x_a)]_{a=1}^m/\sqrt n,\qquad
u_t=w_t/\sqrt n,\qquad
u_*=B_0(B_0^\top B_0)^{-1}y,\qquad e=\|u_*\|.
\tag{5}
\]

The ordinary frozen-feature predictor is
\(f_{\rm RF}=u_*^\top h_0^{(L)}(Z)/\sqrt n\).
On the active fitting event, the already proved readout comparison gives

\[
\int_0^\infty\rho(t)\,dt\le2\varepsilon,\qquad
e\le\sqrt2Y/\sqrt\lambda,\qquad
\sup_t\|u_t\|\le3e,\qquad
\|u_\infty-u_*\|\le120Fe\varepsilon^2,
\tag{6}
\]

where \(\rho=\|r\|/\sqrt m\), and (F) is the fitting coefficient
defined below. The target comparison is the conditional centered bound

\[
\|f_n(\infty,\sqrt d\,v)-f_{\rm RF}\|_{2,c}
\le D e\varepsilon^2/\sqrt n,
\tag{7}
\]

with an activation/depth-only coefficient small enough under (1). Here
\(\|X\|_{2,c}^2=\mathbb E_Z|X-\mathbb E_ZX|^2\).

## 2. A mixed Gaussian fourth-moment inequality

Let \(G\sim N(0,I_k)\), let (a_1,\ldots,a_m\in\mathbb R^k) satisfy
\(\|a_b\|\le H_0\), and put

\[
T(G)=\sum_{b=1}^m c_b\phi(a_b^\top G),\qquad
q_c=\mathbb ET^2,\qquad s=\sup_{\mathbb R}|\phi'|.
\]

Then

\[
\mathbb ET^4\le q_c^2+4s^2H_0^2\|c\|_1^2q_c.
\tag{8}
\]

To prove this, differentiation gives
\(\|\nabla T\|\le sH_0\|c\|_1\). Gaussian Poincare applied to (T^2)
therefore yields

\[
\mathbb ET^4-(\mathbb ET^2)^2
\le \mathbb E\|\nabla(T^2)\|^2
=4\mathbb E[T^2\|\nabla T\|^2]
\le4s^2H_0^2\|c\|_1^2q_c.
\]

The functions and derivatives have polynomial Gaussian envelopes because
the activation has linear growth. Truncation therefore justifies Poincare
for (T^2). The needed Poincare inequality itself follows by expanding a
smooth function in Gaussian Hermite polynomials: its variance sums all
positive-degree squared coefficients, while gradient energy weights them
by their positive degrees.

Consequently,

\[
\|T\|_4^2\le q_c+2sH_0\|c\|_1\sqrt{q_c}.
\tag{9}
\]

If \(\sqrt{q_c}\le C_0e\), \(\|c\|_1\le C_1\varepsilon\), and
\(e\le\sqrt2\varepsilon\), this gives
\(\|T\|_4^2\le C e\varepsilon\). This is the useful mixed scale.
It is weaker than, and does not claim, an (O(e^4)) fourth moment.

In a finite-dimensional fixed-data initialized feature model, (8) can also
be made simultaneous over every coefficient vector (c). The empirical
second and fourth moment tensors converge entrywise, conditional on the
preceding layers; their dimensions are fixed. Positivity of the limiting
training Gram converts additive quadratic-form errors into relative
errors. Homogeneity then extends the resulting inequality from a unit
coefficient sphere to all (c). Thus adaptive choices of (c) do not
invalidate the initialized inequality. They do not turn trained features
into initialized features.

For example the actual residual integral defines

\[
c_t=-\frac2m\int_0^t r(s)\,ds,\qquad
v_t=[h_0^{(L)}(x_a)]_{a=1}^m c_t,
\qquad \|c_t\|_1\le4\varepsilon.
\tag{10}
\]

The symbol (v_t\in\mathbb R^n) in (10) is a readout vector, distinct from
the fixed query (v\in\mathbb R^d). The exact relation is

\[
w_t-v_t=-\frac2m\int_0^t
\sum_a r_a(s)[h_a^{(L)}(s)-h_a^{(L)}(0)]\,ds.
\tag{11}
\]

Fitting gives \(\sup_t\|w_t-v_t\|/\sqrt n\le C e\varepsilon^2\),
so (8) bounds (v_t) at the mixed scale uniformly in time. Equation (11)
requires a fourth-moment feature-displacement estimate before the same
conclusion can be asserted for (w_t).

## 3. The precise sufficient passive moment

Here all expectations concern the independent (Z) in (2). Put

\[
\begin{gathered}
D_j=s(9s)^{L-j},\quad U_1=D_1,\quad U_j=2HD_j\ (j\ge2),\\
F_1=sU_1,\quad F_j=s(2HU_j+9F_{j-1}),\quad F=F_L,\\
K_j^+=s(9s)^{j-1},\quad K_L^0=s(8s)^{L-1},\quad
A_L=2\sum_{j=2}^L K_{j-1}^+D_jU_j.
\end{gathered}
\]

Use the fixed terminal readout (a=w_\infty) and the actual intermediate
weights to define

\[
p_t^{(L)}=a,\qquad
p_t^{(j)}=W_t^{(j+1)\top}
[\phi'(z_t^{(j+1)}(Z))\odot p_t^{(j+1)}].
\tag{12}
\]

These are mixed-time passive responses. Define

\[
M_j(t)=\left(\frac1n\mathbb E_Z\sum_i
|p_{t,i}^{(j)}|^2|\dot z_{t,i}^{(j)}(Z)|^2\right)^{1/2}.
\tag{13}
\]

The exact Gaussian Poincare reduction in `NONODD_SCALAR_ROUTE.md` is

\[
\begin{aligned}
\|f_n(\infty,\sqrt d\,v)-f_{\rm RF}\|_{2,c}
\le\frac1{\sqrt n}\bigg[&
(120K_L^0F+18\sqrt2 A_L)e\varepsilon^2\\
&+b_2\sum_{j=2}^L(9s)^{j-1}
\int_0^\infty M_j(t)\,dt\bigg],
\end{aligned}
\tag{14}
\]

where (b_2=\sup|\phi''|\le1). Briefly, differentiating
\(\nabla_Z(a^\top h_t^{(L)})\) produces one term for each changed matrix
and one term for each changed gate. The changed matrices are bounded by
their Frobenius velocities in (6). The layer-(j) gate term contains
\(\phi''(z_t^{(j)})\odot p_t^{(j)}\odot\dot z_t^{(j)}\), whose Gaussian
Euclidean norm is bounded by (b_2\sqrt nM_j(t)). Integration and Gaussian
Poincare give (14). In particular hidden mean shifts are still present in
\(\dot z_t^{(j)}\).

A sufficient bound, weaker than the earlier energy-times-energy target, is

\[
M_j(t)\le C_j\rho(t)e\varepsilon.
\tag{15}
\]

It would prove (7) with

\[
D=120K_L^0F+18\sqrt2 A_L
 +2b_2\sum_{j=2}^L(9s)^{j-1}C_j.
\tag{16}
\]

For example (C_j\le\beta^{45L}) gives the deliberately loose
envelope (D\le\beta^{50L}): bound (9s\le\beta^2), absorb (L)
by \(\beta^L\), and use the already established fitting-coefficient
bounds. Thus the original (arepsilon\le\beta^{-30L}) leaves a
factor \(\beta^{-10L}\) in (D\varepsilon^2). This calculation does
not establish (15).

One sufficient way to prove (15) would be

\[
\left(\frac1n\mathbb E_Z\sum_i|p_{t,i}^{(j)}|^4\right)^{1/4}
 \le P_j\sqrt{e\varepsilon},\qquad
\left(\frac1n\mathbb E_Z\sum_i|\dot z_{t,i}^{(j)}|^4\right)^{1/4}
 \le V_j\rho(t)\sqrt{e\varepsilon},
\tag{17}
\]

because Cauchy--Schwarz gives (C_j=P_jV_j). Only these mixed moments,
or the integrated bound in (14), are needed. Neither a data-independent
(e)-normalized fourth moment nor a bound of order (\rho e^2) is needed.

The existing source budget proves training-coordinate fourth moments at
scale (arepsilon^4). It does not prove (17), even for the contemporaneous
passive response; (12) additionally uses a terminal readout at an earlier
time. Replacing both factors in (17) by (O(\varepsilon)) would give
(O(\varepsilon^3/\sqrt n)) in (14), whose ratio to the desired
(e\varepsilon^2/\sqrt n) is (\varepsilon/e). This ratio is not
bounded by an activation/depth-only constant under (1).

## 4. Why small activity does not give a uniform root Lipschitz bound

The following fully explicit calculation concerns frozen residual controls,
as used in a cavity argument. It does not change or refute the actual-network
target in Section 1.

For either activation there is (a<0) with

\[
\phi'(a)=0,\qquad c=\phi''(a)>0.
\tag{18}
\]

For GELU, \(\phi'(-1)<0<\phi'(0)\), since
\(\Phi(-1)=\int_1^\infty\varphi(x)\,dx<\varphi(1)\), while
\(\phi''>0\) on ((-1,0)). For SiLU, \(\phi'(-2)<0<\phi'(0)\).
At any negative zero of \(\phi'\), the relation
\(a=-1/(1-\sigma(a))\) gives
\(\phi''(a)=\sigma'(a)/(1-\sigma(a))>0\).

Consider two orthogonal training directions for a single scalar neuron with
constant prescribed residuals (-r,-r), where (r>0). The corresponding
controlled equations are

\[
\dot w=r[\phi(z_1)+\phi(z_2)],\qquad
\dot z_j=rw\phi'(z_j),\qquad
w(0)=0,\quad z_1(0)=a,\quad z_2(0)=R.
\tag{19}
\]

Fix any activity \(\tau=rT>0\), however small. Choose
\(R\ge\max(1,-4\phi(a))\). Then (z_1(t)=a). Since
\(\phi'(x)>0\) for (x\ge0\) and \(\phi(x)\ge x/2\) there,
the first-exit argument for (w\ge0,z_2\ge R\) gives

\[
\dot w\ge rR/4,\qquad w(T)\ge R\tau/4.
\tag{20}
\]

These controlled equations have a solution on every finite interval:
bounded activation derivatives and linear growth bound the total state
norm by a constant times its norm plus one.

Differentiate in the initial incoming coordinate (z_1(0)), keeping
(z_2(0)=R). At the trajectory in (19), the first variations of (w)
and (z_2) vanish identically: they solve a homogeneous system with zero
initial values, because \(\phi'(z_1)=0\). The remaining variation
\(\xi=\partial z_1/\partial z_1(0)\) satisfies

\[
\dot\xi=rcw\xi,\qquad \xi(0)=1,\qquad
\xi(T)\ge\exp(cR\tau^2/8).
\tag{21}
\]

The backward response (delta_1=w\phi'(z_1)) therefore has

\[
\left|\frac{\partial\delta_1(T)}{\partial z_1(0)}\right|
=cw(T)\xi(T)
\ge\frac{cR\tau}{4}\exp(cR\tau^2/8).
\tag{22}
\]

Consequently no Lipschitz constant depending only on the activity and
activation can hold uniformly over all incoming Gaussian-root values for
these frozen-control responses. Bounded negative slopes and small activity
do not remove the curvature term (r w\phi''(z_1)\xi). A proof using the
actual fitting residuals, Gaussian averaging, or a weighted derivative
estimate could still succeed; (22) only excludes the unqualified uniform
root-Lipschitz shortcut.

## 5. Remaining implication and boundary

The useful new scale is (e^2\varepsilon^2) for fourth moments, supported
by (8), and the sufficient actual-flow obligation is (15). In the proposed
readout bootstrap (11), the missing ingredient is a reachable-training
feature-displacement estimate at this mixed scale, followed by its passive
mixed-time counterpart. The source's incoming-row expansion suggests a
Gaussian lower-feature increment plus an integral of training backward
coordinates. Its reverse expansion also contains the noncentered term

\[
-\frac2m\sum_b\int_0^t r_b(s)h_{b,i}(s)
\frac{\operatorname{tr}(B_a(t)J(t,s)B_b(s)^\top)}n\,ds,
\]

with the source proof's (B_a=D_\Theta\delta_a) and variational propagator
(J). The readout block of this Hessian pairing need not carry an extra
(e). Taking absolute values supplies an (arepsilon)-scale term and
does not prove the mixed moment. Its cancellation or a weighted estimate
remains unproved here.

The activation identities, mixed Gaussian moment, reduction (14)--(17), and
controlled-flow calculation (18)--(22) are proved. The actual passive moment
(15), the resulting comparison (7), and a full actual-endpoint lower theorem
are not proved by this route. No stronger label cap, bounded activation
surrogate, frozen actual model, or data-independent (e^4) moment has been
substituted.

## 6. Frozen deterministic oracle approximation module

The supervisor subsequently assigned a separate, precise bottleneck: construct
an initialization-only adaptive matrix-oracle algorithm approximating the
actual fitted parameters with (o(n^{-1/2})) error and (o(n)) queries per
Gaussian hidden matrix. This module closes that approximation bottleneck.
It does not depend on (15), a centered frozen-feature comparison, or new
coordinate moment estimates. It applies to the paper's whole activation
class under its existing cap; GELU and SiLU are particular cases.

### Statement and accessible initial information

Use Euclidean physical mobility coordinates

\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\qquad \|\cdot\|_{\rm par}=\|\cdot\|_2.
\tag{23}
\]

The first-layer initialization is accessed only through the training vectors
(W_0^{(1)}v_a). Each hidden initialized matrix is an oracle supporting
(b\mapsto W_0^{(j)}b) and (a\mapsto W_0^{(j)\top}a). The algorithm
retains its learned increments as sums of outer products of known vectors.
It uses labels and activation derivatives, and never uses a true later
trajectory value. Constants below may depend on every fixed problem
parameter; this affects the eventual width threshold, not the label cap.

There is a deterministic exact-arithmetic algorithm returning
\(\widehat\theta_n\) such that, on active-initialization events of probability
tending to one,

\[
\|\widehat\theta_n-\theta(\infty)\|_{\rm par}
\le C_{\rm data} n^{-16},
\qquad
N_{\rm queries}\le C_{\rm data}mL[\log(en)]^{9/2}.
\tag{24}
\]

The count is the total of forward and transpose oracle calls; it in
particular bounds the dimension of the queried input span on either side
of any one hidden matrix. The algorithm is a proof device: no finite-precision
or practical running-time assertion is made.
The returned parameters are represented implicitly as the original
initialized matrices plus the explicitly returned learned increments and
readout. The algorithm does not reconstruct their unobserved entries.

### Source inputs and a complex parameter tube

Put \(\ell_n=\log(en)\), and use the public whole-sphere source radius,
restricted to training inputs,

\[
T_n=32\ell_n/\lambda,\qquad
R_n=\frac{\lambda}{\beta^{30L}Y^2\sqrt{(d+3)\ell_n}}
=c_{\rm data}\ell_n^{-1/2}.
\tag{25}
\]

Apply the fitting and source arguments to the training span alone. The
ambient (d) in (25) gives a radius no larger than the radius with the span
dimension, so the source statement remains valid. The required event is
therefore measurable without any orthogonal first-layer Gaussian coordinate.

The source proposition (i), its proved working whole-sphere estimates, and
`cp:src-improved-maxima` together supply, on a neighborhood of
([-R_n,T_n+R_n]+i[-R_n,R_n]), the following training estimates:

- the training forward and backward fields and parameters are holomorphic;
- hidden operators and the first operator restricted to the training
  span and divided by (\sqrt n) are at most ten, and all relevant
  forward/backward RMS norms are bounded by
  fixed-problem constants;
- training preactivations stay strictly inside the activation strip;
- the maximum training backward carrier is at most
  (C_{\rm data}\sqrt{\ell_n}).

The last item uses the proved intermediate complex maximum, not merely the
public real-time maximum. Parameter holomorphy also follows directly by
integrating the holomorphic products in the canonical flow; this agrees
with the real parameters and with their local ODE continuations.

Write (G(\theta)) for the vector field in coordinates (23), so

\[
G(\theta)=-\frac2m\sum_a r_a\nabla_\theta f_a.
\tag{26}
\]

At complex points the formulas use algebraic transposes; all norm bounds
use the ordinary complex Euclidean norm. There are fixed positive constants
(c_0,C_0) such that, throughout a complex parameter tube of radius

\[
\eta_n=c_0/\sqrt n
\tag{27}
\]

around this true complex trajectory,

\[
\|G\|_{\rm par}\le C_0,
\qquad \|DG\|_{\rm op}\le C_0\sqrt{\ell_n}.
\tag{28}
\]

Here is a verification that does not presume numerical stability. Forward
subtraction gives, for a parameter perturbation of norm \(\eta\),
training preactivation Euclidean increments at most
(C\sqrt n\eta), and feature RMS increments at most (C\eta), as long
as the joining segment stays in the strict derivative strip. Taking (c_0)
small in (27) preserves that strip by a first-exit argument. Operators and
feature RMS bounds then persist with slightly larger fixed constants.
Backward subtraction uses the reference coordinate carrier maximum and

\[
\|\operatorname{diag}(k)(\phi'(z+\Delta z)-\phi'(z))\|_2
\le C\|k\|_\infty\|\Delta z\|_2.
\]

Thus backward Euclidean increments are at most
(C\sqrt{n\ell_n}\eta), and their coordinate maxima remain
(O_{\rm data}(\sqrt{\ell_n})) in the tube. Their RMS norms also remain
bounded. These bounds imply uniformly bounded residuals and gradient norms.

For the derivative in (28), the Hessian identity `cp:src-Hessian` applies.
If \(\Theta=\sqrt n\theta=(W^{(1)},\sqrt nW^{(2)},\ldots,w)\)
and (F_a=nf_a), then exactly

\[
D_\theta^2 f_a=D_\Theta^2F_a.
\tag{29}
\]

The noncurvature blocks have bounded operator norms. Each curvature block
contains one carrier diagonal, so
\(\|D_\theta^2 f_a\|_{\rm op}\le C(1+\max_{b,j,i}|k_{b,i}^{(j)}|)
\le C\sqrt{\ell_n}\).
Differentiating (26) proves (28). This checks the factors of (n): a
spurious factor (n) in (29) would invalidate the argument.

### Taylor algorithm and robust local truncation

Choose the deterministic integers and mesh

\[
J_n=\left\lceil8T_n/R_n\right\rceil,\qquad
h_n=T_n/J_n\le R_n/8,\qquad
q_n=\left\lceil\ell_n^3\right\rceil,\qquad t_j=jh_n.
\tag{30}
\]

Initialize \(\widehat\theta_0=\theta(0)\). At each step compute, from the
current approximate parameters, the first (q_n) Taylor coefficients of
the autonomous ODE (26), and set

\[
\widehat\theta_{j+1}
=\widehat\theta_j+
\sum_{k=1}^{q_n}\frac{h_n^k}{k!}
\left.\frac{d^k\theta}{dt^k}\right|_{\theta=\widehat\theta_j}.
\tag{31}
\]

This uses the approximate initial value at every step. There is no access
to exact Taylor coefficients at a true later state.

To justify (31), suppose
(\delta_j=\|\widehat\theta_j-\theta(t_j)\|_{\rm par})
is smaller than a fixed multiple of (\eta_n). Compare the exact complex
ODE solution started from \(\widehat\theta_j\) with
(z\mapsto\theta(t_j+z)) on the disk (|z|\le R_n/2).
Along a radial segment, (28) bounds the discrepancy by

\[
\delta_j\exp(C_0\sqrt{\ell_n}|z|)
\le C_1\delta_j,
\tag{32}
\]

where (C_1) is independent of (n), because
\(R_n\sqrt{\ell_n}=c_{\rm data}\).
If (C_1\delta_j<\eta_n/2), first exit from the tube is impossible.
The finite-dimensional holomorphic ODE therefore continues throughout
this disk. One can obtain the continuation by solving along radial
segments; local uniqueness and holomorphic dependence on the segment's
complex endpoint glue these solutions. The strict strip margin prevents
an activation singularity during this construction.

Its velocity is bounded by (C_0), so the increment from its initial state
has norm at most (C_0R_n/2) on this disk. Cauchy's coefficient estimate
and (h_n/(R_n/2)\le1/4) give the local Taylor remainder

\[
\|\operatorname{Flow}_{h_n}(\widehat\theta_j)
-\widehat\theta_{j+1}\|_{\rm par}
\le C_2R_n4^{-q_n}.
\tag{33}
\]

Thus the complex-time radius used for the local error has been verified at
the numerical state; it is not silently transferred from the true state.

Real-time comparison and (33) imply

\[
\delta_{j+1}\le
e^{C_0\sqrt{\ell_n}h_n}\delta_j+C_2R_n4^{-q_n}.
\]

Since \(\delta_0=0\), every prefix is bounded by

\[
\max_{j\le J_n}\delta_j
\le C_2J_nR_n
\exp(C_0\sqrt{\ell_n}T_n)4^{-q_n}
\le C_3\ell_n
\exp(C_4\ell_n^{3/2}-(\log4)\ell_n^3).
\tag{34}
\]

For every fixed (K>0), the last expression is at most (n^{-K}) for
sufficiently large (n). In particular it is eventually less than
\(\eta_n/(2C_1)\). Induction closes the tube condition used above and
proves (34) without an assumed accuracy hypothesis.

Fitting supplies the remaining tail:

\[
\|\theta(\infty)-\theta(T_n)\|_{\rm par}
\le2Y\lambda^{-1/2}e^{-\lambda T_n/2}
=2Y\lambda^{-1/2}e^{-16\ell_n}.
\tag{35}
\]

Choose, for example, (K=17) in (34), and set
\(\widehat\theta_n=\widehat\theta_{J_n}\).
Equations (34)--(35) prove the parameter error in (24).

### Matrix-oracle count and learned ranks

The Taylor jets in (31) can be constructed sequentially. If state
coefficients through degree (k) are known, evaluate all forward jets
through that degree, then all backward and residual jets. The degree-(k)
coefficient of (26), divided by (k+1), supplies the next state coefficient.
Activation jets are finite scalar compositions using derivatives at the
known degree-zero preactivation.

Write (W^{(j)}=W_0^{(j)}+E^{(j)}), with (E^{(j)}) stored as known outer
products. For each training sample, layer, and coefficient, forward
evaluation needs only one new product of the form
(W_0^{(j)}h_{a,k}^{(j-1)}). Backward evaluation needs only one new
(W_0^{(j)\top}\delta_{a,k}^{(j)}). All products involving (E^{(j)})
use its stored representation. There is no hidden matrix-matrix oracle
call in differentiating the flow.

The degree-(k) coefficient of a hidden update is a sum of

\[
-\frac2{nm}r_{a,p}\delta_{a,q}^{(j)}h_{a,s}^{(j-1)\top},
\qquad p+q+s=k.
\tag{36}
\]

It therefore lies in the column span of already computed backward jets
and the row span of already computed forward jets. The large number of
scalar convolution terms in (36) does not introduce new oracle directions.
There are at most (2m(L-1)J_nq_n) hidden oracle calls, up to a fixed
boundary convention for the last jet. Equation (30) gives
(J_n=O_{\rm data}(\ell_n^{3/2})) and (q_n=O(\ell_n^3)), proving
(24). Each learned hidden increment is supported in those same two queried
spans. First-layer updates are known sums of
\(\delta_{a,k}^{(1)}v_a^\top\), so require no additional first-layer
initialization access.

All query directions are functions of previous oracle answers, fixed data,
and previously computed jets. This is a valid adaptive oracle transcript.
It does not assume that queried directions are independent of earlier
answers. A deferred-Gaussian-conditioning argument can therefore use this
transcript, but that conditioning argument is a separate module.

### Transfer to the fixed orthogonal query and readout moments

The algorithm preserves
\(\widehat W^{(1)}v=W_0^{(1)}v=Z\) exactly, because every first-layer update
has right factor in the training span. Real forward subtraction using
bounded hidden operators gives, for the endpoint parameters and their
approximation,

\[
|\widehat f_n(\sqrt d\,v)-f_n(\infty,\sqrt d\,v)|
\le C_{\rm data}
\left(1+\frac{\|Z\|}{\sqrt n}\right)
\|\widehat\theta_n-\theta(\infty)\|_{\rm par}.
\tag{37}
\]

To check this, the common first feature has RMS at most
(b+s\|Z\|/\sqrt n). Each successive feature RMS is at most a fixed
multiple of (1+\|Z\|/\sqrt n); its difference is bounded by that
quantity times the accumulated hidden Frobenius discrepancies. Finally
split the output difference into its readout and feature terms and use
the bounded readout RMS. Equation (37) is deterministic for every (Z).
Under its independent Gaussian law it is (o(n^{-1/2})), by (24).

Writing \(\|a\|_{p,n}=(n^{-1}\sum_i|a_i|^p)^{1/p}\), the same parameter
error also gives

\[
\|\widehat w-w_\infty\|_{4,n}
\le n^{1/4}\|\widehat w-w_\infty\|_{2,n}
\le C_{\rm data}n^{-63/4}.
\tag{38}
\]

Thus existing actual-readout fourth-moment bounds pass to the approximant
with a vanishing error. No passive fourth-moment theorem is needed for
this numerical transfer.

This module establishes only the finite-oracle approximation and its error,
rank, provenance, and query-independence properties. A lower fluctuation
theorem for the approximate endpoint must still be supplied separately;
(24) and (37) then transfer it to the actual fitted endpoint.
