# What arbitrary labels do and do not obstruct

2026-10-07. Self-contained finite-network theoretical analysis. The general
arbitrary-label compression theorem is not proved or disproved here.
The unresolved question concerns multiple inputs. The user already has
arbitrary-label one-sample compression; Section 3 reconstructs its fitting
mechanism only as a baseline for explaining why a proposed extension fails.

## 1. Model and exact metric

Let there be `m` training pairs with inputs of Euclidean norm `sqrt(d)`,
hidden width `n`, and `L` hidden layers. Use the forward pass
\[
z_a^{(1)}=Ax_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),\qquad
f_a=w^\top h_a^{(L)}/n.
\]
The parameter blocks have shapes `n by d`, `n by n`, and `n`. Activations
are smooth on the entire real line; the original strip-analytic class is
more than sufficient. First weights are initially independent Gaussian
variables of variance one, hidden weights independent Gaussian variables
of variance `1/n`, and `w(0)=0`. The deterministic statements below do not
need randomness unless explicitly stated.

Set
\[
r_a=f_a-y_a,\qquad
\mathcal L=\frac1m\sum_a r_a^2,\qquad
Y=\frac{\|y\|_2}{\sqrt m}.
\]
Write all parameters together as \(\theta\). Let \(M\) be the positive
block-diagonal mobility matrix with multipliers \((n,1,\ldots,1,n)\).
Thus the physical flow is \(\dot\theta=-M\nabla\mathcal L\). Its metric is
\[
\|\theta\|_{M^{-1}}^2
=\frac{\|A\|_F^2}{n}
+\sum_{\ell=2}^L\|W^{(\ell)}\|_F^2+\frac{\|w\|_2^2}{n}.
\]
Define the unnormalized training tangent Gram by
\[
K_{ab}(t)=\nabla f_a(\theta(t))^\top M\nabla f_b(\theta(t)).
\]
It is positive semidefinite at every real parameter state, without a label
restriction. Differentiation gives the exact identities
\[
\dot r=-\frac2mKr,\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top Kr
=-\|\dot\theta\|_{M^{-1}}^2.
\tag{energy}
\]
Its readout contribution is the current feature Gram
\(K_{ab}^{\rm readout}=h_a^{(L)\top}h_b^{(L)}/n\).
Positivity alone does not give a positive eigenvalue or fitting.

## 2. No finite-time parameter blowup for any label vector

**Proposition.** Every finite initial parameter vector and every finite
label vector have a unique gradient-flow solution for all finite times.
For zero initial readout and \(0\le s<t\),
\[
\|\theta(t)-\theta(s)\|_{M^{-1}}
\le\sqrt{(t-s)(\mathcal L(s)-\mathcal L(t))}
\le Y\sqrt{t-s}.
\tag{finite-time-motion}
\]

**Proof.** Smoothness makes the finite-dimensional vector field locally
Lipschitz, so a unique local solution exists. Integrate (energy), then apply
Cauchy–Schwarz to the parameter path on `[s,t]`. This proves the bound on
any existing solution interval. At a hypothetical finite maximal time the
bound makes the parameters Cauchy, with a finite Euclidean limit because
the metric is fixed and positive definite at fixed width. Local existence
at that limit extends the solution, contradicting maximality. The loss at
initialization is `Y^2` because the readout is zero. This proves the claim.

There is also finite-horizon, width-uniform operator control. For `t <= T`,
\[
\frac{\|A(t)-A(0)\|_F}{\sqrt n},\quad
\|W^{(\ell)}(t)-W^{(\ell)}(0)\|_{\rm op},\quad
\frac{\|w(t)\|_2}{\sqrt n}\le Y\sqrt T.
\]
If the normalized initial first operator norm and all initial hidden operator
norms are at most eight, and
\(\max_j\{|\phi_j(0)|,\sup_{\mathbb R}|\phi'_j|\}\le\beta\) with
\(\beta\ge1\), forward induction gives
\[
\sup_{\|x\|=\sqrt d}\frac{\|h^{(\ell)}(t,x)\|_2}{\sqrt n}
\le[\beta(9+Y\sqrt T)]^\ell\qquad(t\le T).
\tag{finite-time-features}
\]
For the first layer this follows from linear activation growth and the
normalized first operator bound. At later layers, the preceding bound is
at least one, so the additive activation value at zero is absorbed by the
extra one inside `9+Y sqrt(T)`. No probabilistic assertion is needed for
this conditional operator statement.

Neither estimate controls infinite-time path length or a positive
training-Gram gap. The proposition does not exclude infinite-time escape.

## 3. One-sample baseline and its precise multi-input limitation

**Theorem.** Take one sample, zero initial readout, and any smooth hidden
feature map, including the full deep nonlinear network above. If
\[
H_0=\frac{\|h^{(L)}(0)\|_2^2}{n}>0,
\]
then every real label is fitted, with
\[
|f(t)-y|\le |y|e^{-2H_0t},\qquad
\int_0^\infty\|\dot\theta\|_{M^{-1}}\,dt
\le\frac{|y|}{\sqrt{H_0}}.
\tag{one-sample-fitting}
\]
All parameters converge to a finite interpolating limit. No small-label
condition, small feature motion, or frozen hidden layer is assumed.

**Proof.** Global existence follows from Section 2. If `y=0`, every gradient
is zero at initialization and the result is immediate. Otherwise define,
only in this proof,
\[
g=\operatorname{sgn}(y)f,\qquad R=|y|-g,\qquad u=\|w\|_2^2/n.
\]
The scalar `K` is the tangent Gram defined above. Since its readout part is
the feature norm, Cauchy–Schwarz gives, whenever `u>0`,
\[
K\ge\frac{\|h^{(L)}\|_2^2}{n}\ge\frac{g^2}{u}.
\tag{one-sample-readout}
\]
The exact evolution equations are
\[
\dot g=2RK,\qquad \dot u=4Rg.
\]
On every finite interval,
\(R(t)=|y|\exp(-2\int_0^tK(s)\,ds)>0\). Initially `K(0)=H_0>0`, because
all hidden derivatives of the output vanish at zero readout. Hence `g(t)>0`
and `u(t)>0` for every positive time. Now
\[
\frac d{dt}\frac{g^2}{u}
=\frac{4Rg}{u}\left(K-\frac{g^2}{u}\right)\ge0.
\tag{one-sample-monotonicity}
\]
No division at time zero is used. Smoothness gives
\[
w(t)=2y h^{(L)}(0)t+o(t),\quad
g(t)=2|y|H_0t+o(t),\quad
u(t)=4y^2H_0t^2+o(t^2).
\]
Thus \(g(t)^2/u(t)\to H_0\) as time decreases to zero. Equations
(one-sample-readout)–(one-sample-monotonicity) imply
\[
K(t)\ge\frac{\|h^{(L)}(t)\|_2^2}{n}
\ge\frac{g(t)^2}{u(t)}\ge H_0.
\]
The residual formula proves the exponential bound. Furthermore,
\[
\|\dot\theta\|_{M^{-1}}=2R\sqrt K
=\frac{\dot g}{\sqrt K}\le\frac{\dot g}{\sqrt{H_0}}.
\]
Integration and `g(t) -> |y|` give the total path bound. Finite path length
makes the parameters Cauchy at infinity, so their finite limit interpolates.
This completes the proof.

If `H_0=0` instead, zero readout makes every gradient zero at initialization;
the solution is stationary and cannot fit a nonzero label. The theorem's
nondegeneracy assumption is therefore necessary in this exact form.
For tanh hidden layers and nonzero input, Gaussian initialization has
`H_0>0` almost surely: a nonzero preceding feature vector gives nondegenerate
Gaussian preactivations, and tanh vanishes only at zero. Induction starts
with the nondegenerate first-layer Gaussian projection.

### The exact multi-input matrix identity

For several examples let \(H=[h_1^{(L)},\ldots,h_m^{(L)}]\) and
\(G=H^\top H/n\). The prediction vector is \(f=H^\top w/n\).
For `u=||w||^2/n>0`, define locally \(P=ff^\top/u\). Then
\[
K\succeq G\succeq P,\qquad
\dot f=-\frac2mKr,\qquad
\dot u=-\frac4m r^\top f.
\]
The matrix inequality follows by applying Cauchy–Schwarz to `Hv` and `w`
for each vector `v` in sample space. Direct differentiation gives
\[
\dot P=-\frac{2}{mu}
\left[(K-P)r f^\top+f r^\top(K-P)\right].
\tag{multi-input-readout}
\]
If `(K-P)r` and `f` are linearly independent, the symmetric matrix on the
right has eigenvalues of opposite signs: in their two-dimensional span,
the determinant is the negative squared area of the two vectors, times
the positive scalar prefactor squared. Positive semidefiniteness of `K-P`
does not change this fact. In addition, when `y^T G(0)y>0`, expansion at
zero readout gives
\[
\lim_{t\downarrow0}P(t)
=\frac{G(0)y\,y^\top G(0)}{y^\top G(0)y}.
\]
This is rank one, not a positive-definite floor on a multi-input sample
space. In the actual residual direction the resulting inequality is only
\[
r^\top Kr\ge\frac{(r^\top f)^2}{u}.
\]
A nonzero residual can be orthogonal to the prediction. Thus the scalar
argument does not establish multi-input fitting.

### Initial feature learning is favorable in the label direction

Let `theta_h` collect hidden parameters and let `M_h` be their mobility
matrix. Zero readout gives `dot(theta_h)(0)=0` and `dot(w)(0)=2H(0)y/m`.
Differentiating the hidden gradient once gives
\[
\ddot\theta_h(0)
=\frac{2}{m^2}M_h\nabla_{\theta_h}\bigl[y^\top G(0)y\bigr].
\tag{hidden-initial-acceleration}
\]
Indeed the hidden gradient equation is
\(\dot\theta_h=-(2/(mn))M_h\sum_a r_a(D_{\theta_h}h_a)^\top w\).
Only differentiating `w` contributes at zero readout. Meanwhile
\(\nabla(y^\top Gy)=(2/n)\sum_a y_a(Dh_a)^\top Hy\), giving the
displayed coefficient. Since initial hidden velocity is zero, this implies
\[
y^\top\ddot G(0)y
=\frac{2}{m^2}
\left\|\nabla_{\theta_h}\bigl[y^\top G(0)y\bigr]\right\|_{M_h}^2
\ge0.
\tag{label-direction-improvement}
\]
Here `||v||_{M_h}^2=v^T M_h v`. This exact favorable direction does not
control other sample directions. Section 7 gives an example where the
smallest eigenvalue initially decreases under typical Gaussian initialization.

### Label normalization does not preserve the dynamics

For a fixed positive multiplier `c`, write `y=c y_bar` and `w=c v`.
Linearity in the readout gives
\[
\mathcal L_{c\bar y}(\theta_h,cv)
=c^2\mathcal L_{\bar y}(\theta_h,v).
\]
Consequently the original canonical flow in the new variables is
\[
\dot\theta_h=-c^2M_h\nabla_{\theta_h}\mathcal L_{\bar y},\qquad
\dot v=-n\nabla_v\mathcal L_{\bar y}.
\]
A time change multiplies both mobilities equally and cannot remove their
relative factor `c^2`. Dividing labels is therefore not a proof for the
unchanged training dynamics.

## 4. Local expansion is compatible with successful fitting

The following refers to instantaneous expansion of the parameter
variational equation, not an asymptotic Lyapunov exponent or chaos.

Whiten the constant mobility by the coordinates \(\vartheta=M^{-1/2}\theta\).
In these coordinates the flow is ordinary gradient flow and its linearized
equation is
\[
\dot\xi=-\nabla^2_{\vartheta}\mathcal L(\vartheta(t))\xi.
\]
For one sample, write the whitened readout as `b=w/sqrt(n)` and the hidden
parameters collectively as `v`. Then `f=b^T h(v)/sqrt(n)`. At `b=0`,
the loss Hessian has hidden-hidden block zero, readout-readout block
`2 h h^T/n`, and mixed block
\[
-\frac{2y}{\sqrt n}(D_vh)^\top.
\]
If `y` is nonzero and `D_vh` is nonzero, choose one hidden direction and
one readout direction with nonzero mixed pairing. The restriction of the
Hessian to their span has the form
\[
\begin{pmatrix}0&-c\\-c&d\end{pmatrix},\qquad c\ne0,\quad d\ge0.
\]
Its determinant is `-c^2`, so it has a negative eigenvalue. A variational
vector along that eigenvector has strictly increasing squared norm at time
zero. This is an actual locally expansive direction for every nonzero
label, including arbitrarily small ones.

For example, take two tanh hidden layers. Differentiating a top feature
with respect to its hidden weight gives
\(\partial h_i^{(2)}/\partial W^{(2)}_{ij}
=\operatorname{sech}^2(z_i^{(2)})h_j^{(1)}\), nonzero almost surely at
Gaussian initialization for a nonzero input. Thus this example has local
expansion and, by Section 3, global arbitrary-label fitting. Local expansion
does not imply failed fitting, much less an impossibility of compression.

## 5. Exact bad minima, but not a Gaussian-initialization counterexample

Take two samples in dimension two,
\[
x_1=\sqrt2 e_1,\qquad x_2=\sqrt2 e_2,\qquad
y=(3a,-a),\quad a>0,
\]
and two hidden layers with
\[
\phi_1(z)=z,\qquad \phi_2(z)=\frac{3+\cos z}{2}.
\]
Here `a` is a label amplitude, not an analytic strip width; the label RMS
is `sqrt(5) a`. Both activations are analytic, with bounded derivatives on
any fixed horizontal strip, and `1 <= phi_2 <= 2` on the real axis.

The population covariance after the linear first layer is the identity.
Consequently the initialized top population feature Gram is
\[
Q^{(2)}=vI_2+\mu^2\mathbf1\mathbf1^\top,\qquad
\mu=\frac{3+e^{-1/2}}2,\qquad
v=\frac{1+e^{-2}-2e^{-1}}8=\frac{(1-e^{-1})^2}{8}>0.
\]
These formulas follow from `E cos(G)=exp(-1/2)` and
`E cos(G)^2=(1+exp(-2))/2` for a standard Gaussian, obtained directly from
its characteristic function. In particular the initial population gap is
strictly positive and independent of the label amplitude.

For any width `n>=2`, choose `A` with first column zero and second column
all ones, choose `W^(2)` with every row sum equal to `pi`, and choose
`w=a 1`. These finite parameters give top features `2 1` and `1`, hence
predictions `f_*=(2a,a)`. This state is a nonglobal local minimum.

To prove that assertion, every nearby state retains strictly positive
readout coordinates. At every such state,
\[
f_1-2f_2
=\frac1n\sum_iw_i[\phi_2(z_{1i})-2\phi_2(z_{2i})]\le0.
\]
The Euclidean projection of `y=(3a,-a)` onto this halfspace is precisely
`f_*=(2a,a)`: subtract `a(1,-2)` from `y`. More explicitly, if `f` lies in
the halfspace, then
\[
\|f-y\|_2^2
=\|f-f_*\|_2^2+\|f_*-y\|_2^2
  +2(f-f_*)^\top(f_*-y)
\ge\|f_*-y\|_2^2,
\]
because `f_*-y=-a(1,-2)` and `(1,-2)^T(f-f_*)<=0`.
This proves local minimality. Its mean squared loss is `5a^2/2>0`.
It is nonglobal: use two neurons with top feature vectors `(2,1)` and
`(1,2)` and signed readout to fit both labels exactly; set other readout
coordinates to zero. Such features are realized by taking first-layer
training features `(e_1,e_2)` and suitable second-layer rows `(0,pi)` and
`(pi,0)`. The two feature vectors are linearly independent.

At actual Gaussian initialization with zero readout, the exact mean-loss
equation gives
\[
\dot w_i(0)=a[3h_{1i}^{(2)}(0)-h_{2i}^{(2)}(0)]\ge a>0.
\]
This initial sign does **not** imply that the positive-readout region is
invariant. No claim is made that Gaussian training reaches the displayed
bad minimum. In particular, proving a positive basin probability at one
finite width, or forcing label amplitude to grow with width, would not
disprove a sufficiently-large-width theorem for each fixed problem.

The bad minima exist at every `a>0`, not just for large labels. Their
existence therefore cannot by itself establish the necessity of the
small-label condition in a high-probability Gaussian theorem.
Moreover, choose every row of `W^(2)` equal to `pi/n` in the displayed
realization. Its whole-sphere predictor is simply
\[
f(x)=\frac a2\left(3+\cos\frac{\pi x_2}{\sqrt2}\right).
\]
It has a width-one two-layer representation. Thus even this actual
non-fitting equilibrium is highly compressible; a failure to interpolate
is not by itself a compression lower bound.

## 6. What would resolve the original question

For a nonzero residual, define only here
\[
\kappa(t)=\frac{r(t)^\top K(t)r(t)}{m\|r(t)\|_2^2}.
\]
The exact residual RMS identity gives
\[
\frac{\|r(t)\|_2}{\sqrt m}
=Y\exp\left(-2\int_0^t\kappa(s)\,ds\right)
\]
until residual zero, after which the flow is stationary. Thus divergent
integrated residual-direction coercivity is sufficient and necessary for
fitting along a nonstationary trajectory. A uniform positive lower bound
is stronger, and supplies an exponential tail. Initial Gram positivity
alone is not the missing all-time estimate.

Even proving fitting would not automatically prove the original compression
rates. All-time approximation also needs control of nonlinear response
growth, regularity and the tail, at the specified width-dependent accuracy.
Conversely, non-fitting, an indefinite Hessian, or failure of one stability
estimate does not prove incompressibility. A compression lower bound needs
a specified representation/precision class and a lower bound for its
approximation error or information requirement.

The central multi-input fixed-label extension and its negative remain
open after this bounded theoretical analysis. No external optimization
theorem, empirical test or inaccessible probability statement is used to
close them.

## 7. A typical-Gaussian obstruction to a monotone initial Gram gap

This is a negative result about one proposed invariant, not about fitting,
stability for all time, or compressibility. It holds at every fixed positive
label RMS, including arbitrarily small ones.

Take `m=d=L=2`, arbitrary width `n`, and
\[
x_a=\sqrt2 e_a,\qquad y=(\sqrt2Y,0),\qquad
\phi_1(z)=z,\qquad \phi_2(z)=b+\tanh(z+s).
\]
Here `Y>0` is the label RMS already defined; `s>0` and `b>1` are fixed
activation parameters, independent of width. The top activation and all
its derivatives are bounded on every closed strip strictly narrower than
`|Im z|<pi/2`; the first activation has bounded derivatives and unbounded
values. Thus both are within the stipulated activation class.

**Proposition.** There exist fixed `s>0` and `b>1` such that, at the prescribed
Gaussian initialization,
\[
\mathbb P\!\left\{
\left.\frac{d^2}{dt^2}\lambda_{\min}(G(t))\right|_{t=0}<0
\right\}\longrightarrow1\qquad(n\to\infty).
\tag{initial-gap-decrease}
\]
The limiting population gap is strictly positive. On the event in question,
`lambda_min(G(t))<lambda_min(G(0))` for all sufficiently small positive
times (the time allowance may depend on the initialization and width).

**Proof: exact initial derivatives.** Write `U=[u_1,u_2]=A(0)`, so its
entries are independent standard Gaussians, and let `W=W^(2)(0)` have
independent variance-`1/n` Gaussian entries, independently of `U`.
All quantities in this proof without a time argument are evaluated at
initialization. Set
\[
z_a=Wu_a,\quad h_a=b+\tanh(z_a+s),\quad
p_a=\operatorname{sech}^2(z_a+s),\quad Q_{ab}=u_a^\top u_b/n.
\]
The coordinatewise interpretation of the last two functions is understood.
Zero readout gives `dot(U)=dot(W)=dot(H)=0`. The mean-loss and canonical-
mobility equations give
\[
\ddot z_a
=2Y^2\left[
Q_{a1}(p_1\odot h_1)
+\mathbf1_{\{a=1\}}WW^\top(p_1\odot h_1)\right],
\qquad \ddot h_a=p_a\odot\ddot z_a.
\tag{two-input-acceleration}
\]
To check the coefficient, put `a_0=sqrt(2)Y` just in this calculation.
Then `dot(w)=a_0 h_1`,
\(\ddot U=a_0^2 W^\top(p_1\odot h_1)e_1^\top\), and
\(\ddot W=(a_0^2/n)(p_1\odot h_1)u_1^\top\).
Adding `ddot(W)U+W ddot(U)` proves the formula with `a_0^2=2Y^2`.

**Proof: limiting Gram and curvature.** In this paragraph only, let `Z`
be standard normal and put
\[
g=\tanh(Z+s),\qquad p=\operatorname{sech}^2(Z+s),\qquad
\mu=\mathbb E g.
\]
The conditional Gaussian law of the rows of `WU`, together with `Q -> I`,
gives
\[
G(0)\longrightarrow
\operatorname{Var}(g)I_2+(b+\mu)^2\mathbf1\mathbf1^\top
\quad\text{in probability}.
\]
Thus the limiting smaller eigenvalue is `gamma=Var(g)>0`, is simple,
and has eigenvector `(1,-1)/sqrt(2)`. Also `b>1` makes every feature entry
strictly positive, so `G_12(0)>0`: the two empirical eigenvalues are simple
at every finite width. Since `dot(G)(0)=0`, eigenvalue
differentiation has no first-eigenvector-derivative term. We claim
\[
\left.\frac{d^2}{dt^2}\lambda_{\min}(G(t))\right|_{0}
\longrightarrow
2Y^2\left[
2\mathbb E[(g-\mu)(b+g)p^2]
+\mathbb E[Z(g-\mu)p]\,\mathbb E[Z(b+g)p]
\right]
\tag{limiting-gap-curvature}
\]
in probability. A justification of the dependent Gaussian terms follows;
independent-neuron sampling cannot simply be assumed after a `WW^T` term.

For `n>=2`, `U` has column rank two almost surely. Conditional on `U`,
let `Xi=WU` and let `Pi` be the orthogonal projector
onto the complement of the column span of `U`. Gaussian orthogonal
decomposition gives exactly
\[
W=\Xi(U^\top U)^{-1}U^\top+V\Pi,
\]
where `V` has independent variance-`1/n` Gaussian entries independent of
`Xi` conditional on `U`. The two summands have orthogonal row domains,
so their cross terms in `WW^T` are zero. Define local vectors
\(\alpha=(h_1-h_2)\odot p_1\) and \(\zeta=p_1\odot h_1\).
They have uniformly bounded coordinates for fixed `b,s`. Conditional on
`U,Xi`,
\[
\mathbb E\left[\frac1n\alpha^\top V\Pi V^\top\zeta\right]
=\frac{n-2}{n}\frac{\alpha^\top\zeta}{n},
\]
and the conditional variance is
\[
\frac{n-2}{n^4}
\left(\|\alpha\|^2\|\zeta\|^2+(\alpha^\top\zeta)^2\right)
=O(n^{-1}).
\]
This follows by diagonalizing the rank-`n-2` projector and summing the
independent Gaussian-column bilinear forms. Thus this contribution tends
to `E[(g-mu)(b+g)p^2]`. The projected contribution is
\[
\frac1n\alpha^\top\Xi(U^\top U)^{-1}\Xi^\top\zeta
=\left(\frac{\alpha^\top\Xi}{n}\right)
Q^{-1}\left(\frac{\Xi^\top\zeta}{n}\right).
\]
Conditional row independence, `Q -> I`, and boundedness of the functions
give convergence of these sample averages to their two independent-
Gaussian expectations. The first projected direction contributes
`E[Z(g-mu)p] E[Z(b+g)p]`. The second contributes zero because its factor
`E[Z_2(b+g_1)p_1]` is zero. The direct `Q_11` term in
(two-input-acceleration) contributes another `E[(g-mu)(b+g)p^2]`;
the `Q_21` term tends to zero. This proves (limiting-gap-curvature), since
\[
\frac12(1,-1)\ddot G(0)(1,-1)^\top
=\frac1n(h_1-h_2)^\top(\ddot h_1-\ddot h_2).
\]
For full detail on replacing the limiting eigenvector, the same
conditional decomposition applied with `h_1` or `h_2` in place of their
difference shows every entry of `ddot(G)(0)` is bounded in probability.
The smaller eigenvector of `G(0)` converges, up to sign, to its simple
population counterpart. Their quadratic forms therefore differ by a
quantity tending to zero in probability. Conditional sample-average
variances are `O(1/n)` on any fixed neighborhood of `Q=I`; the required
Gaussian moments are uniformly bounded there. This also justifies the
row-average limits despite the random covariance `Q`.

**Proof: strict negative sign.** The expression in square brackets in
(limiting-gap-curvature) is affine in `b`. Its coefficient of `b` is
\[
2\operatorname{Cov}(g,p^2)
+\mathbb E[Z(g-\mu)p]\,\mathbb E[Zp].
\tag{offset-coefficient}
\]
For every `s>0`, the first term is strictly negative. Indeed, conditional
on `R=|Z+s|`,
\[
\mathbb E[g\mid R]=\tanh R\,\tanh(sR),\qquad
p^2=\operatorname{sech}^4R.
\]
The first function is strictly increasing and the second strictly
decreasing on positive arguments. With `R'` an independent copy,
twice their covariance is the expectation of the product of their
increments between `R` and `R'`, which is strictly negative almost surely.
This proves the covariance claim. Gaussian integration by parts yields
\[
\mathbb E[Zp]=-2\mathbb E[gp]<0,
\]
because `E[gp|R]=tanh(R)tanh(sR)sech^2(R)>0`. At `s=0`,
\[
\mathbb E[Z(g-\mu)p]
=\mathbb E[Z\tanh Z\operatorname{sech}^2 Z]>0.
\]
Continuity preserves this strict positivity for sufficiently small
positive `s`. Fix such an `s`. Then (offset-coefficient) is strictly
negative, so a sufficiently large fixed `b>1` makes the full affine
expression strictly negative. The curvature convergence proves the
proposition. The elementary Gaussian integration-by-parts identity used
here follows by integrating against the normal density; boundedness of
the functions makes its boundary term zero.

**Limits of this result.** An initially decreasing gap need not collapse;
the tangent Gram also contains positive hidden-parameter contributions.
The decrease occurs for every `Y>0`, so it is compatible with small-label
theorems that preserve only a fraction of the initial gap. It refutes
the proposed monotone initial-gap invariant under typical Gaussian
initialization. It does not establish non-fitting, order-one dense-run
variability, or an impossibility of polylogarithmic compression.
