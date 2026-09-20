# Canonical stalls and a nonstationary three-point bottleneck

This is a scoped, prompt-only theoretical route. It uses the exact scalar closure,
canonical initialization, and finite-time flow stipulated in the assignment. No
other study inputs, external results, numerical experiments, or surrogate flows
are used. All conclusions below are internal derivations, not promoted results.

## Result and its limit

There is an explicit family of balanced, pairwise-nonparallel three-point datasets
whose canonical initial loss descent is bounded away from zero, but whose loss
stays at least `3/32` until a time of order `epsilon^(-2/3)`. Each member has a
positive definite initial readout Gram matrix, is homogeneously linearly
separable, and is exactly representable by changing only the initial readout.
The obstruction comes from approaching an antipodal
same-label pair, not from approaching the canonical initial-stall locus.

Consequently, initial nonstall magnitude alone cannot supply a uniform
exponential rate from time zero. Any such rate, or its prefactor/delay, must
degenerate in this family. This does **not** establish failure of exponential
convergence for any fixed admissible dataset. A data potential singular near
antipodality can accommodate the lower bound. The existence of an appropriate
potential on every nonstalled genuine three-point instance remains open here.

The canonical initial-stall locus is also classified exactly below.

## 1. Setup

Write `v_i=x_i/sqrt(2)` so that `|v_i|=1`, and let

\[
\phi(s)=\tanh s,\qquad
a_i=\mathbb E_g[b_1(g)\phi(w(g)\cdot v_i)],\qquad
H_i(Z)=\phi(b(Z)M a_i),\qquad
f_i=\mathbb E_Z[c(Z)H_i(Z)].
\]

The canonical initialization is `w_0(g)=g`, `c_0=0`, and the fixed stipulated
`M_0>0`. Its loss is `L(0)=1`. The normalization gives

\[
\|b_1\|_2^2=\frac{\nu}{\nu+\eta}<1,
\qquad
\|b\|_2^2=\frac{\tau}{\tau+\eta}<1.
\]

The exact gradient-flow identity is

\[
-\dot L
=\|\dot w\|_{L^2(g)}^2+\|\dot c\|_{L^2(Z)}^2+|\dot M|^2.
\tag{1}
\]

All estimates below use the exact flow, not a frozen-feature approximation.

## 2. A moving canonical trajectory with an architectural loss floor

Take labels `(+, +, -)`, weights

\[
(p_1,p_2,p_3)=(3/8,1/8,1/2),
\tag{2}
\]

and, initially allowing the architectural boundary,

\[
v_1=e_1,\qquad v_2=-e_1,\qquad v_3=e_2.
\tag{3}
\]

Oddness of both nonlinearities implies, at every state,

\[
a(-v)=-a(v),\qquad H(-v)=-H(v),\qquad f(-v)=-f(v).
\tag{4}
\]

Therefore, with `F=f_1=-f_2`,

\[
L\ge\frac38(F-1)^2+\frac18(-F-1)^2
=\frac12(F-1/2)^2+\frac38
\ge\frac38.
\tag{5}
\]

This canonical trajectory is not initially stationary. Put

\[
A=M_0\frac{\nu}{\sqrt{\nu+\eta}}>0,
\qquad H_A(b)=\tanh(bA).
\]

At initialization, `a_1=nu/sqrt(nu+eta)`, `a_2=-a_1`, and `a_3=0`.
Since `c_0=0`, the initial `w` and `M` velocities vanish, whereas

\[
\dot c_0=\frac12 H_A,
\qquad
-\dot L(0)=\frac14\mathbb E H_A(b)^2>0.
\tag{6}
\]

The strict inequality uses `A>0` and the nondegenerate law of `b`.
Thus this is a genuine moving positive-loss trajectory, although (3) is excluded
by the pairwise-nonparallel requirement. Its role is to identify a boundary
mechanism that survives quantitatively at admissible nearby datasets.

## 3. Explicit long bottleneck for genuine three-point datasets

Keep (2), and for `0<epsilon<pi/4` set

\[
v_1=e_1,\qquad
v_2=(-\cos\varepsilon,-\sin\varepsilon),\qquad
v_3=(\sin\varepsilon,\cos\varepsilon).
\tag{7}
\]

These vectors are pairwise nonparallel. Their class probabilities are balanced.
They are homogeneously linearly separable: for

\[
\theta_\varepsilon=(\sin(\varepsilon/2),-\cos(\varepsilon/2)),
\]

the three signed margins are

\[
\theta_\varepsilon\cdot v_1=\sin(\varepsilon/2)>0,
\quad
\theta_\varepsilon\cdot v_2=\sin(\varepsilon/2)>0,
\quad
-\theta_\varepsilon\cdot v_3=\cos(3\varepsilon/2)>0.
\tag{8}
\]

### 3.1 The initial descent is uniformly positive

For independent standard normal `G,U`, define

\[
h(\rho)=\frac{\mathbb E[\tanh(G)
\tanh(\rho G+\sqrt{1-\rho^2}U)]}{\sqrt{\nu+\eta}},
\qquad -1\le\rho\le1.
\tag{9}
\]

Then `a_i(0)=h(v_{i1})`. This function is odd, continuous on `[-1,1]`, and
strictly increasing. To check the last assertion, for `-1<rho<1` differentiate
under the expectation, which is justified on compact subintervals by bounded
derivatives and Gaussian integrability. Integration by parts in `G` and `U`
cancels the terms containing `tanh''` and gives

\[
h'(\rho)
=\frac{\mathbb E[\operatorname{sech}^2(G)
\operatorname{sech}^2(\rho G+\sqrt{1-\rho^2}U)]}
{\sqrt{\nu+\eta}}>0.
\tag{10}
\]

Continuity at the endpoints follows by dominated convergence. Since
`h(1)=nu/sqrt(nu+eta)`, write

\[
B_\varepsilon=M_0h(\cos\varepsilon),\qquad
D_\varepsilon=M_0h(\sin\varepsilon),\qquad
0<D_\varepsilon<B_\varepsilon<A.
\]

At initialization,

\[
\dot c_0(b)=\frac34\tanh(bA)-\frac14\tanh(bB_\varepsilon)
-\tanh(bD_\varepsilon).
\tag{11}
\]

Put `R=||H_A||_2>0` and `K=M_0/sqrt(nu+eta)>0`. For `b>=0`, the first two
terms in (11) are at least `tanh(bA)/2`. For `b<0`, oddness gives the same
inequality in absolute value. Formula (10) also gives
`h'(rho)<=1/sqrt(nu+eta)`, so

\[
\|\tanh(bD_\varepsilon)\|_2
\le D_\varepsilon\|b\|_2
\le\frac{M_0\sin\varepsilon}{\sqrt{\nu+\eta}}
\le K\varepsilon.
\]

The reverse triangle inequality therefore yields
`||c_dot_0||_2 >= R/2-K epsilon`. Every member of (7) with
`epsilon<=R/(4K)` satisfies

\[
-\dot L_\varepsilon(0)
\ge s_0:=\frac1{16}\mathbb E\tanh^2(bA)>0,
\tag{12}
\]

where `s_0` is independent of `epsilon`.

### 3.2 The loss cannot fall quickly

Integrating (1), using `L(0)=1` and `L(t)>=0`, and applying Cauchy--Schwarz in
time gives

\[
\|c_t\|_2\le\sqrt t,\qquad
|M_t|\le M_0+\sqrt t,\qquad
\|w_t\|_2\le\sqrt2+\sqrt t.
\tag{13}
\]

For example,
`||w_t-w_0||_2 <= integral_0^t ||w_dot||_2 <= sqrt(t)`, and
`||w_0||_2=sqrt(2)`. These component bounds hold for every finite time.

The oddness and 1-Lipschitz property of `tanh` imply

\[
\begin{aligned}
|a_1+a_2|
&=\left|\mathbb E b_1\{
\tanh(w\cdot v_1)-\tanh(w\cdot(-v_2))\}\right|\\
&\le |v_1+v_2|\,\mathbb E(|b_1||w|)
\le |v_1+v_2|\,\|b_1\|_2\|w\|_2,
\\
|f_1+f_2|
&\le\|c\|_2\|H_1+H_2\|_2
\le\|c\|_2\|b\|_2|M|\,|a_1+a_2|.
\end{aligned}
\tag{14}
\]

Because `|v_1+v_2|=2 sin(epsilon/2)<=epsilon` and the two normalized feature
norms are less than one, (13)--(14) yield the exact-trajectory estimate

\[
|f_1(t)+f_2(t)|
\le\varepsilon\sqrt t\,(M_0+\sqrt t)(\sqrt2+\sqrt t).
\tag{15}
\]

On the other hand, weighted Cauchy--Schwarz gives

\[
\begin{aligned}
L
&\ge\frac38(f_1-1)^2+\frac18(f_2-1)^2\\
&\ge\frac{(f_1+f_2-2)^2}{8/3+8}
\ge\frac3{32}\bigl(2-|f_1+f_2|\bigr)_+^2.
\end{aligned}
\tag{16}
\]

Let

\[
C=(M_0+1)(\sqrt2+1),\qquad
T_\varepsilon=(C\varepsilon)^{-2/3}.
\tag{17}
\]

If `0<epsilon<=1/C`, then `T_epsilon>=1`. The right side of (15) is increasing
in `t`, and at `t=T_epsilon` it is at most

\[
C\varepsilon T_\varepsilon^{3/2}=1.
\]

Thus for every `0<epsilon<min(pi/4,1/C,R/(4K))` the actual canonical trajectory
obeys

\[
L_\varepsilon(t)\ge\frac3{32}
\quad\text{for every }0\le t\le T_\varepsilon,
\qquad
-\dot L_\varepsilon(0)\ge s_0>0.
\tag{18}
\]

No continuity-in-data theorem or asymptotic approximation is needed for (18).

### 3.3 Consequence for exponential bounds

If a proposed theorem supplies, on every member of (7),

\[
L_\varepsilon(t)\le e^{-\kappa_\varepsilon t}
\quad(t\ge0),
\]

then evaluating at `T_epsilon` in (18) forces

\[
\kappa_\varepsilon
\le\log(32/3)\,C^{2/3}\varepsilon^{2/3}.
\tag{19}
\]

Equivalently, a bound of the form `L(t)<=exp(-t/V(data))` requires

\[
V(\text{data}_\varepsilon)
\ge\frac{(C\varepsilon)^{-2/3}}{\log(32/3)}.
\tag{20}
\]

For a prefactor `P_epsilon>=1`, replace `log(32/3)` in (19) by
`log(32 P_epsilon/3)`. In particular, any uniformly bounded prefactor still
forces rates tending to zero. A theorem asserting only eventual exponential
convergence can instead have an unbounded onset time; (18) does not control the
eventual asymptotic exponent.

Since (12) stays bounded away from zero, a potential controlled only by inverse
initial gradient magnitude cannot satisfy (20). However, a potential that also
diverges as the same-label pair becomes antipodal can satisfy this necessary
condition. The limiting antipodal dataset is outside the genuine-three-point
domain, so divergence towards it is compatible with finiteness at every fixed
admissible `epsilon>0`.

There is a sharper consequence for a fixed common exponential rate. If a
proposed bound has the form

\[
L_\varepsilon(t)
\le\bigl[\Phi_0(\text{data}_\varepsilon)e^{-\lambda t}\bigr]^\alpha,
\qquad \lambda>0,\quad\alpha>0,
\tag{20a}
\]

where `lambda` and `alpha` are independent of `epsilon`, then (18) forces

\[
\Phi_0(\text{data}_\varepsilon)
\ge (3/32)^{1/\alpha}
\exp\!\left[\lambda(C\varepsilon)^{-2/3}\right].
\tag{20b}
\]

Thus such a common-rate potential needs at least an essential singularity
of this size; any potential bounded by a fixed power of `1/epsilon` fails.
This is a necessary condition for the precise normalization (20a), not a
refutation of arbitrarily singular potentials or geometry-dependent rates.

### 3.4 The initial readout Gram is positive definite

This verifies that (18) is not a hidden impossibility of interpolation at the
individual admissible datasets, or an initial feature-rank defect. The initial
scalar feature arguments in (7) are

\[
(M_0a_1(0),M_0a_2(0),M_0a_3(0))
=(A,-B_\varepsilon,D_\varepsilon),
\qquad 0<D_\varepsilon<B_\varepsilon<A.
\]

The three initial functions `H_i^0(b)=tanh(bM_0a_i(0))` are linearly independent
in `L^2(Z)`: if a linear
combination vanished, continuity and the interval support of `b` would make it
vanish near zero. Its derivatives of orders `1,3,5` would give a Vandermonde
system in the three distinct positive numbers `(M_0a_i(0))^2`, with nonzero
column factors `M_0a_i(0)`; all coefficients must vanish.

Consequently `G_ij=E[H_i^0 H_j^0]` is positive definite. Taking
`beta=G^{-1}y` and `c_* = sum_j beta_j H_j^0`, while retaining `w_*=w_0` and
`M_*=M_0`, gives `f_i^*=y_i`. All these state variables have finite norm.
This constructs an interpolating state using only the readout, not a convergence
proof for the canonical trajectory.

### 3.5 Earlier axis-negative version and the strengthening

The earlier family kept the same positive pair and weights but used `v_3=e_2`.
It has the same bounds (13)--(20). Its initial derivative is
`c_dot_0=(3/4)H_A-(1/4)H_B`, so its initial descent is at least `R^2/4` without
the smallness condition `epsilon<=R/(4K)`. It is linearly separable, for example
by `(sin(epsilon)/2,-cos(epsilon))`.

In that earlier family the third initial feature is zero, so the initial
three-by-three readout Gram is singular. Replacing `v_3` by
`(sin(epsilon),cos(epsilon))` removes this defect while preserving the positive
pair bottleneck. Sections 3.1--3.4 contain the stronger version and are the main
result. The earlier version is retained only to make the strengthening explicit.

## 4. Exact canonical initial-stall locus for balanced genuine three points

Assume arbitrary pairwise-nonparallel `v_i` on the unit circle, labels
`(+, +, -)`, and weights `(q/2,(1-q)/2,1/2)` with `0<q<1`.

At initialization, `d_i=0`; hence `w_dot=M_dot=0`. The entire gradient vanishes
if and only if

\[
\sum_{i=1}^3 p_i y_i\tanh(bz_i)=0
\quad\text{almost surely},
\qquad z_i=M_0h(v_{i1}).
\tag{21}
\]

Group all nonzero `z_i` by their distinct magnitudes `lambda>0`, and let

\[
\gamma_\lambda
=\sum_{i:|z_i|=\lambda}p_i y_i\operatorname{sign}(z_i).
\]

The law of `b` has positive density on an open interval containing zero.
By continuity, (21) implies `sum_lambda gamma_lambda tanh(b lambda)=0`
throughout that interval. If there are `m<=3` distinct magnitudes, the first
`m` odd Taylor coefficients of `tanh`, which begin
`u-u^3/3+2u^5/15`, imply

\[
\sum_\lambda\gamma_\lambda\lambda^{2k+1}=0,
\qquad k=0,\ldots,m-1.
\]

The determinant is a nonzero product of the column factors `lambda` and the
differences of their squares. Thus every `gamma_lambda` is zero.

No nonzero magnitude group can be a singleton because its weight is positive.
Three nonparallel unit vectors cannot have one common nonzero absolute first
coordinate: for a fixed value in `(0,1)` the four possibilities form two
antipodal pairs, and selecting three selects an antipodal pair; the endpoint
value `1` permits only an antipodal pair. Therefore (21) requires exactly one
`z_i=0` and a cancelling pair with equal nonzero magnitudes. Two zero values
would also give a parallel pair on the second coordinate axis.

The cancelling pair must have equal weights. A positive example has weight
strictly less than `1/2`, so it cannot cancel the negative example's weight
`1/2`. The pair is therefore `(1,2)`, with `q=1/2`, and `z_3=0`. Its labels
coincide, so its signs must be opposite. By the strict monotonicity and oddness
of `h`, this is equivalent to

\[
q=\frac12,\qquad v_{31}=0,\qquad
v_{11}=-v_{21}\ne0.
\tag{22}
\]

Finally the two positive vectors have equal second coordinates: choosing
opposite second coordinates would make them antipodal. Thus, after swapping
the two positive indices if needed, the complete locus is

\[
\begin{gathered}
q=\frac12,\qquad 0<\delta<1,\qquad
s\in\{\sqrt{1-\delta^2},-\sqrt{1-\delta^2}\},\qquad\sigma\in\{1,-1\},\\
v_1=(\delta,s),\qquad v_2=(-\delta,s),\qquad v_3=(0,\sigma).
\end{gathered}
\tag{23}
\]

Conversely every dataset in (23) satisfies (21), so uniqueness makes its
canonical trajectory constant. The choice `sigma=-sign(s)` is linearly
separable even though the canonical flow stalls. Initial linear separability
alone consequently does not exclude the canonical stall locus.

## 5. Audit and remaining gap

* **Established here:** the exact initial-stall classification (23); the moving
  architectural boundary obstruction (5)--(6); the explicit actual-flow
  bottleneck (18) for genuine three-point data with a positive definite initial
  readout Gram; finite-state expressivity of every perturbed instance; and the
  necessary essential singularity (20b) for common-rate bounds of form (20a).
* **Ruled out:** a positive uniform global-from-zero exponential rate, with
  bounded prefactor, derived solely from an initial gradient lower bound or
  canonical nonstationarity. The family (7) has a fixed lower bound (12) on
  initial descent while its necessary time scale diverges.
* **Not ruled out:** instancewise exponential convergence with a data potential
  that is finite on each nonstalled, nonparallel instance and singular near
  initial stalls and architectural boundaries. Nor does (18) rule out a fixed
  eventual asymptotic exponent after a diverging transient.
* **Unresolved:** an exact nonstationary, pairwise-nonparallel three-point
  canonical trajectory with a positive limiting loss or provably subexponential
  convergence at that fixed dataset; and an unconditional convergence/rate
  theorem for all nonstalled genuine three-point data.

The useful distinction is therefore between excluding the exact initial-stall
locus and controlling all other slow mechanisms. Excluding the former is
necessary, but this route shows that the latter still needs independent
geometric dependence. It does not prove that no admissible singular potential
can supply that dependence.

## 6. Algebraic initial-Gram degeneration and readout potential

This section strengthens the comparison with initialized readout potentials.
Sections 1--5 above were frozen before this append. Throughout this section the
dataset is the strengthened family (7), and limits are as `epsilon` decreases
to zero. The constants in all `O` and `Theta` statements are independent of
`epsilon`.

### 6.1 Controlled feature expansions

The Gaussian integration-by-parts calculation behind (10) applies repeatedly.
For `n=1,2,3` and `-1<rho<1`, it gives

\[
h^{(n)}(\rho)
=\frac{\mathbb E[\phi^{(n)}(G)
\phi^{(n)}(\rho G+\sqrt{1-\rho^2}U)]}{\sqrt{\nu+\eta}}.
\tag{24}
\]

Indeed, differentiating `E[F(G)F(rho G+sqrt(1-rho^2)U)]` and integrating by
parts in each Gaussian variable gives `E[F'(G)F'(rho G+sqrt(1-rho^2)U)]`:
the two terms involving `F(G)F''` cancel. Apply this identity successively
with `F=phi, phi', phi''`. The derivatives of `tanh` involved here are bounded,
as they are polynomials in `tanh`. Thus differentiation is justified on compact
subintervals and the right sides extend continuously to the endpoints by
dominated convergence. In particular,

\[
h'(1)=\frac{\mathbb E\operatorname{sech}^4(G)}{\sqrt{\nu+\eta}}>0,
\qquad
h'(0)=\frac{(\mathbb E\operatorname{sech}^2(G))^2}{\sqrt{\nu+\eta}}>0.
\tag{25}
\]

The bounded second derivative gives
`h(1)-h(cos epsilon)=h'(1)(1-cos epsilon)+O((1-cos epsilon)^2)`.
At zero, oddness gives `h(0)=h''(0)=0`, and the bounded third derivative gives
`h(sin epsilon)=h'(0) epsilon+O(epsilon^3)`. Set

\[
k_2=\frac{M_0h'(1)}2>0,
\qquad k_1=M_0h'(0)>0.
\]

It follows that

\[
A-B_\varepsilon=k_2\varepsilon^2+O(\varepsilon^4),
\qquad
D_\varepsilon=k_1\varepsilon+O(\varepsilon^3).
\tag{26}
\]

The random variable `b` is bounded. Taylor's formula for `tanh`, with bounded
derivatives, therefore makes the following errors uniform in `b`, hence also
valid in `L^2(Z)`:

\[
\begin{aligned}
H_A-H_{B_\varepsilon}
&=k_2\varepsilon^2 b\phi'(bA)+O_{L^2}(\varepsilon^4),\\
H_{D_\varepsilon}
&=k_1\varepsilon b+O_{L^2}(\varepsilon^3).
\end{aligned}
\tag{27}
\]

### 6.2 All three initial Gram eigenvalue orders

Normalize the three feature functions by putting

\[
Q_\varepsilon
=\left(H_A,\frac{H_A-H_{B_\varepsilon}}{\varepsilon^2},
\frac{H_{D_\varepsilon}}{\varepsilon}\right).
\]

By (27), these functions converge in `L^2`, componentwise, to

\[
Q_*=(H_A,k_2 b\phi'(bA),k_1b).
\tag{28}
\]

The three limiting functions are linearly independent. To verify this without
an external function-system result, suppose

\[
u\tanh(Ab)+v b\operatorname{sech}^2(Ab)+w b=0
\]

in `L^2`. Since the law of `b` has positive density near zero, the continuous
left side vanishes on that interval. Its coefficients of `b^3` and `b^5`, using
`tanh z=z-z^3/3+2z^5/15+O(z^7)` and
`sech^2 z=1-z^2+2z^4/3+O(z^6)`, give

\[
-\frac{uA^3}3-vA^2=0,
\qquad \frac{2uA^5}{15}+\frac{2vA^4}3=0.
\]

The first equation gives `v=-uA/3`; substitution in the second gives
`-4uA^5/45=0`. Since `A>0`, both `u` and `v` vanish, and the linear term forces
`w=0`. The positive factors `k_1,k_2` do not change independence.

Consequently the Gram matrix `Ghat_epsilon=E[Q_epsilon Q_epsilon^T]` converges
to a positive definite matrix. There exist constants `m_*,M_*>0` such that,
for all sufficiently small positive `epsilon`,

\[
m_*I\preceq\widehat G_\varepsilon\preceq M_*I.
\tag{29}
\]

The original initial feature vector is `(H_A,-H_B,H_D)=S_epsilon Q_epsilon`,
where

\[
S_\varepsilon=
\begin{pmatrix}1&0&0\\-1&\varepsilon^2&0\\0&0&\varepsilon\end{pmatrix}.
\]

Hence its Gram matrix satisfies

\[
G_\varepsilon=S_\varepsilon\widehat G_\varepsilon S_\varepsilon^T,
\qquad
m_*S_\varepsilon S_\varepsilon^T
\preceq G_\varepsilon
\preceq M_*S_\varepsilon S_\varepsilon^T.
\tag{30}
\]

The two-by-two block of `S_epsilon S_epsilon^T` has trace `2+epsilon^4` and
determinant `epsilon^4`. For `epsilon<=1`, its larger eigenvalue lies between
`1` and `3`, and the smaller is the determinant divided by the larger, hence
between `epsilon^4/3` and `epsilon^4`. The remaining eigenvalue is `epsilon^2`.
Applying the variational eigenvalue characterization to both inequalities in
(30), the eigenvalues of the initial readout Gram, in descending order, satisfy

\[
\lambda_1(G_\varepsilon)=\Theta(1),\qquad
\lambda_2(G_\varepsilon)=\Theta(\varepsilon^2),\qquad
\lambda_3(G_\varepsilon)=\Theta(\varepsilon^4).
\tag{31}
\]

Also `det G_epsilon=epsilon^6 det Ghat_epsilon=Theta(epsilon^6)`. Incorporating
the fixed positive data weights by multiplying the features by `sqrt(p_i)`
preserves these orders.

### 6.3 The least-norm initial readout correction is only algebraic

Define explicitly the initial readout-correction potential by

\[
\Phi_{\mathrm{read},0}
:=\min\left\{\|c-c_0\|_2^2:
\mathbb E[cH_i(0)]=y_i\ \text{for }i=1,2,3\right\}.
\tag{32}
\]

Here `c_0=0`, so this is `y^T G_epsilon^{-1}y`. A convention inserting a fixed
factor such as `1/2` in (32) has the same asymptotic order. The minimum exists:
orthogonal projection onto the span of the three independent feature functions
preserves the constraints and cannot increase the norm; the coefficients of the
minimum are obtained by inverting their Gram matrix.

The first two interpolation constraints read
`<c,H_A>=1` and `<c,H_B>=-1`; therefore

\[
\langle c,H_A-H_{B_\varepsilon}\rangle=2.
\tag{33}
\]

Together with the third constraint `<c,H_D>=-1`, the normalized feature vector
requires

\[
\mathbb E[cQ_\varepsilon]
=z_\varepsilon:=(1,2\varepsilon^{-2},-\varepsilon^{-1})^T.
\]

Consequently, by (29),

\[
\Phi_{\mathrm{read},0}
=z_\varepsilon^T\widehat G_\varepsilon^{-1}z_\varepsilon
=\Theta(\|z_\varepsilon\|^2)
=\Theta(\varepsilon^{-4}).
\tag{34}
\]

This also follows in the lower-bound direction directly from (33) and
Cauchy--Schwarz, since (27) gives
`||c||_2^2>=4/||H_A-H_B||_2^2=Theta(epsilon^-4)`.

For the precise common-rate domination hypothesis (20a), (20b) requires growth
at least `constant * exp(lambda C^(-2/3) epsilon^(-2/3))`. The algebraic
potential (32), and any fixed polynomially bounded function of it or of the
inverse initial Gram eigenvalues, cannot meet that necessary condition.
This conclusion allows a geometry-dependent exponential rate; it also allows
a faster-growing potential, for example an exponential transform of an
algebraically divergent geometric quantity. It therefore excludes particular
readout/Gram potential normalizations at a common rate, not the existence of
all admissible scalar potentials.
