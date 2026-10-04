# Predictor lower bounds for independent canonical dense networks

2026-10-04. Scoped theoretical continuation. Internally derived; not a
promotion review. This note concerns dense gradient flow, rather than a
response-memory closure. The unused-input Gaussian argument is adapted from
the same study's `NEURON_GLOBAL_NEGATIVE.md`; the sample-count dependence
and equal-width independent comparison below are derived here.

**Result.** Two independent width-$n$ canonical dense networks with two tanh
hidden layers have a prediction difference at least
$cY/\sqrt{mn}$ at a fixed positive physical time, with fixed positive
probability, on orthogonal $m$-sample data of label RMS $Y\le1$. All
constants can be independent of $m$, and a sufficient conservative width
condition is $n\ge C(m+1)^3\log(e(m+1))$. For one training input and a
sufficiently small fixed nonzero label $y$, the actual fitted query
predictions differ by at least $c|y|/\sqrt n$ with fixed positive
probability. A further rescaling of the complete estimates gives the
stronger actual-prediction bound $c\sqrt m\,Y/\sqrt n$ at time
$t=mt_*$ under the explicit sufficient condition $mY\le1$.
These statements imply lower bounds in the supremum over
all physical time and the entire input sphere. These are actual nonlinear
prediction results; their remainders have the same root-width normalization
as their leading terms.

## 1. Model and precise claims

Let $m\ge1$, $d\ge m+1$, and take inputs and one query

\[
 x_a=\sqrt d\,e_a\quad(1\le a\le m),\qquad
 x_*=\sqrt d\,e_{m+1},\qquad
 y=(y_1,\ldots,y_m)^\top,\qquad
 0<Y=\|y\|_2/\sqrt m\le1.
\tag{1}
\]

At width $n$, the matrices are $A=W^{(1)}\in\mathbb R^{n\times d}$,
$W=W^{(2)}\in\mathbb R^{n\times n}$ and the readout is
$w=W^{(3)}\in\mathbb R^n$. The exact forward pass and loss are

\[
 h_a^{(1)}=\tanh(Ae_a),\qquad h_a^{(2)}=\tanh(Wh_a^{(1)}),
 \quad f_a=w^\top h_a^{(2)}/n,
 \quad r_a=f_a-y_a,
 \quad \mathcal L=m^{-1}\sum_a r_a^2.
\tag{2}
\]

Write $H^{(\ell)}=[h_1^{(\ell)},\ldots,h_m^{(\ell)}]$. With block
mobilities $(n,1,n)$, dense gradient flow is exactly

\[
\begin{aligned}
 \delta_a^{(2)}&=w\odot\tanh'(Wh_a^{(1)}),\\
 \delta_a^{(1)}&=\tanh'(Ae_a)\odot W^\top\delta_a^{(2)},\\
 \dot A&=-\frac2m\sum_a r_a\delta_a^{(1)}e_a^\top,\\
 \dot W&=-\frac2{mn}\sum_a r_a\delta_a^{(2)}h_a^{(1)\top},\\
 \dot w&=-\frac2m H^{(2)}r.
\end{aligned}
\tag{3}
\]

Initialization has independent $A_{ij}(0)\sim N(0,1)$,
$W_{ij}(0)\sim N(0,1/n)$ and $w(0)=0$. The two matrices are independent.
The second network has an independent copy of all initial entries and
follows the same equations and dataset. Its prediction is $\widetilde f_n$.

**Positive-time theorem.** There are universal $C,c,p,t_*>0$ such that,
for (1) and $n\ge C(m+1)^3\log(e(m+1))$,

\[
 \mathbb P\left\{
 |f_n(t_*,x_*)-\widetilde f_n(t_*,x_*)|
       \ge c\frac{Y}{\sqrt{mn}}\right\}\ge p.
\tag{4}
\]

In particular the same bound holds with the left-hand difference replaced
by $\sup_{t\ge0}\sup_{\|x\|_2=\sqrt d}|f_n(t,x)-\widetilde f_n(t,x)|$.
The parameters $m,d,Y$ may vary with $n$ subject to the stated conditions.

**Endpoint theorem.** For $m=1$, there are universal
$y_*,c_\infty,p_\infty>0$ such that, for each fixed
$0<|y|\le y_*$ and all sufficiently large $n$, with probability at least
$p_\infty$ both dense networks converge, interpolate their training input,
and

\[
 |f_n(\infty,x_*)-\widetilde f_n(\infty,x_*)|
             \ge c_\infty |y|/\sqrt n.
\tag{5}
\]

The endpoint statement is restricted to $m=1$. The present proof does not
infer the fitted $m$-sample rate from its initial velocity.
Section 5a gives an additional finite-time theorem at $t=mt_*$,
uniformly in $m$ when $mY\le1$.

## 2. Uniform deterministic motion bounds

The loss decreases along (3), so $\|r(t)\|_2/\sqrt m\le Y$. Let
$s(t)=\|w(t)\|_2/\sqrt n$; this symbol denotes a norm in this section,
not a changed clock. The estimates below are interpreted using upper
Dini derivatives when a norm vanishes. Suppose initially

\[
 \|W_0\|_{\rm op}\le10,
 \qquad \|H_0^{(2)}\|_{\rm op}/\sqrt n\le2.
\tag{6}
\]

Stop temporarily if $\|W\|_{\rm op}=11$ or
$\|H^{(2)}\|_{\rm op}/\sqrt n=3$. Before that stop,

\[
 s(t)\le6Yt/\sqrt m,
 \quad \|w(t)\|_\infty\le2Yt,
 \quad \|\dot W\|_{\rm op}\le2Ys(t),
 \quad \|\dot H^{(1)}\|_F/\sqrt n
       \le 2Y\|W\|_{\rm op}s(t)/\sqrt m.
\tag{7}
\]

The first inequality follows from
$\|\dot w\|_2/\sqrt n\le2Y\|H^{(2)}\|_{\rm op}/\sqrt{mn}$.
The second follows coordinatewise from the bounded features and
$m^{-1}\sum_a|r_a|\le Y$. For the last bound, the columns of $A$
used in training have disjoint input-coordinate supports, and
$\|\delta_a^{(1)}\|_2\le\|W\|_{\rm op}\|w\|_2$; sum the squared
column speeds and use $\|r\|_2=\sqrt m\,\|r\|_2/\sqrt m$.
The mixer estimate follows directly by summing the rank-one updates.

Differentiating the top features, using $|\tanh'|\le1$ and
$\|H^{(1)}\|_F\le\sqrt{mn}$, gives

\[
 \frac{\|\dot H^{(2)}\|_F}{\sqrt n}
 \le 2Ys(t)\left(\sqrt m+\frac{\|W\|_{\rm op}^2}{\sqrt m}\right).
\tag{8}
\]

Consequently, for
$0\le t\le t_0=1/\sqrt{1464}$, (7)--(8) imply

\[
 \|W(t)-W_0\|_{\rm op}\le6Y^2t^2/\sqrt m,
 \qquad
 \|H^{(2)}(t)-H_0^{(2)}\|_{\rm op}/\sqrt n\le732Y^2t^2.
\tag{9}
\]

Both bounds leave a strict margin before the stopped boundaries, so the
bootstrap holds throughout this interval. Constants here are deliberately
loose. No maximum over individual Gaussian coordinates occurs.

The readout's linear term is $2tH_0^{(2)}y/m$. Subtract it in (3):

\[
 \dot w-2H_0^{(2)}y/m
   =-2H^{(2)}f/m+2(H^{(2)}-H_0^{(2)})y/m.
\tag{10}
\]

Because $f=H^{(2)\top}w/n$, the normalized norm of the first term is
at most $18s(t)/m$. The second is at most
$1464Y^3t^2/\sqrt m$. Integration yields

\[
 \frac{\|w(t)-2tH_0^{(2)}y/m\|_2}{\sqrt n}
 \le\frac{54Yt^2/m+488Y^3t^3}{\sqrt m}
 \le\frac{542Yt^2}{\sqrt m}.
\tag{11}
\]

Dense solutions exist at every finite physical time: the decreasing loss
bounds residual RMS; (3) then bounds $\|w\|_\infty$ linearly in time,
$\|W\|_F$ polynomially in time, and subsequently $\|A\|_F$
on each bounded interval. The smooth finite-dimensional vector field
therefore cannot have a finite-time escape.

## 3. The complete query remainder retains the root-width scale

Condition on the training initialization
$\mathcal F=\sigma(A_0e_1,\ldots,A_0e_m,W_0)$. The flow changes only
the first $m$ columns of $A$, so
$g=A(t)e_{m+1}=A_0e_{m+1}\sim N(0,I_n)$ remains independent of the
whole training path. Its query prediction is

\[
 F(t,g)=n^{-1}w(t)^\top\tanh(W(t)\tanh g).
\tag{12}
\]

Define the initialized label-weighted query kernel and full remainder by

\[
 K_y(g)=\frac1{mn}(H_0^{(2)}y)^\top\tanh(W_0\tanh g),
 \qquad R(t,g)=F(t,g)-2tK_y(g).
\tag{13}
\]

All three functions are odd in $g$. Their conditional means are zero.
The exact gradient of the first is

\[
 \nabla_gF=\frac1n\operatorname{diag}(\tanh'g)W^\top
          [w\odot\tanh'(W\tanh g)].
\tag{14}
\]

On the training-only event (6), (7)--(11) give, uniformly in $g$,

\[
 \|\nabla_gF\|_2\le\frac{66Yt}{\sqrt{mn}},
 \qquad
 \|\nabla_gR\|_2\le\frac{7000Yt^2}{\sqrt{mn}}.
\tag{15}
\]

For the second inequality, put $v=2tH_0^{(2)}y/m$. Its normalized
Euclidean norm is at most $4Yt/\sqrt m$, and
$\|v\|_\infty\le2Yt$. Subtracting gradients yields three terms:
the readout difference, the mixer difference, and the top-gate difference.
After division by $n$, their bounds are respectively

\[
 \frac{5962Yt^2}{\sqrt{mn}},\qquad
 \frac{24Y^3t^3}{m\sqrt n},\qquad
 \frac{240Y^3t^3}{\sqrt{mn}}.
\tag{16}
\]

The last term uses $\|\tanh''\|_\infty\le2$ and
$\|\tanh g\|_2\le\sqrt n$. These prove (15).

For an odd smooth function $U$ of a standard Gaussian vector with
$\sup\|\nabla U\|_2\le L$, Gaussian Poincare gives
$\mathbb EU^2\le L^2$. Applying that inequality to $U^2$ gives
$\mathbb EU^4\le5L^4$. One proof of the needed Poincare inequality is
to expand in orthonormal Gaussian Hermite polynomials: variance sums the
squared nonconstant coefficients, and mean squared gradient multiplies
each such coefficient by its positive total degree. Polynomial
approximation in Gaussian Sobolev norm extends the identity to these
bounded smooth functions. Applying this argument conditionally gives

\[
 \mathbb E_g R(t,g)^2\le\frac{7000^2Y^2t^4}{mn},
 \qquad
 \mathbb E_g F(t,g)^4\le\frac{5\cdot66^4Y^4t^4}{m^2n^2}.
\tag{17}
\]

Thus the error after integrating the initial velocity is controlled at
$Yt^2/\sqrt{mn}$, not merely by a width-independent deterministic error.

## 4. Initial lower variance, with constants uniform in sample count

Let $G\sim N(0,1)$ and define fixed positive constants

\[
 Q=\mathbb E\tanh^2G,\qquad
 q=\mathbb E\tanh^2(\sqrt Q\,G),\qquad
 \varepsilon=\min\left\{\frac Q2,
       \frac{q\sqrt Q}{4(1+\sqrt3)}\right\}.
\tag{18}
\]

Here $q$ is a scalar Gaussian moment, not a memory order. Set $p=m+1$
only in this section. Form the $n\times p$ lower-feature matrix with
columns $\tanh(A_0e_a)$ and the query column $\tanh g$. Its empirical
Gram $C$ satisfies

\[
 \mathbb P\{\max_{a,b}|C_{ab}-Q\delta_{ab}|
                  >\varepsilon/p^{3/2}\}
 \le2p^2\exp\{-n\varepsilon^2/(2p^3)\}.
\tag{19}
\]

This is the union bound and Hoeffding's inequality for independent rows
of bounded products in $[-1,1]$. On its good event,
$\|C-QI\|_{\rm op}\le\varepsilon/\sqrt p$.

Conditionally on this entire lower-feature matrix, the upper preactivation
rows are independent copies of $Z\sim N(0,C)$. Let
$Z_0=\sqrt Q\,\xi$ and $Z=C^{1/2}\xi$ for $\xi\sim N(0,I_p)$.
Since $QI$ commutes with $C$, diagonalization and the scalar square-root
identity give

\[
 \|C^{1/2}-\sqrt Q I\|_{\rm op}
       \le\varepsilon/\sqrt{pQ},
 \quad
 \|C^{1/2}-\sqrt Q I\|_F\le\varepsilon/\sqrt Q.
\tag{20}
\]

Define $\Psi(Z)=(\sum_{a=1}^m y_a\tanh Z_a)\tanh Z_p$.
At the diagonal covariance, all coordinates are independent and centered,
so $\mathbb E\Psi(Z_0)=0$ and
$\|\Psi(Z_0)\|_{L^2}=q\|y\|_2$. Splitting the product difference
and using the 1-Lipschitz property of tanh gives

\[
 \|\Psi(Z)-\Psi(Z_0)\|_{L^2}
 \le (1+\sqrt3)\varepsilon\|y\|_2/\sqrt Q
 \le q\|y\|_2/4.
\tag{21}
\]

For the first product term, use
$\|y\|_2\|Z-Z_0\|_{L^2(\mathbb R^m)}$. For the second use
Cauchy--Schwarz in fourth moments. Independence and centering show
$\mathbb E(\sum_a y_a\tanh Z_{0,a})^4\le3\|y\|_2^4$;
the Gaussian coordinate difference has fourth moment equal to three
times its variance squared. These facts and (20) prove (21).
Centering is an orthogonal projection in $L^2$, so

\[
 \operatorname{Var}(\Psi(Z))\ge q^2\|y\|_2^2/4.
\tag{22}
\]

Now $K_y$ is $1/m$ times the average of $n$ conditionally independent
copies of $\Psi$. If the right side of (19) is at most $1/2$, conditional
variance followed by expectation yields

\[
 \mathbb E K_y^2\ge\frac{q^2Y^2}{8mn}.
\tag{23}
\]

This derivation does not assume that a larger correlation can only
increase variance. It compares the complete row function to independent
coordinates in $L^2$.

## 5. A training-only good event and the probability conclusion

Let $\mathcal T$ be the event (6). It is measurable from $\mathcal F$.
For $c_W=100/8-2\log9>0$,

\[
 \mathbb P(\mathcal T^c)
 \le2e^{-c_Wn}+4m^2e^{-n/(32m^2)}.
\tag{24}
\]

The mixer bound follows from a $1/4$-net of each unit sphere with at most
$9^n$ points: $\|W_0\|_{\rm op}\le2\max|u^\top W_0v|$, and
each bilinear form is $N(0,1/n)$. For the feature bound, first restrict
the off-diagonal entries of the lower training Gram to magnitude
$1/(4m)$ using Hoeffding. Given this lower matrix, top rows are Gaussian
before tanh. For a centered Gaussian pair with variances fixed, the
derivative of $\mathbb E\tanh Z_a\tanh Z_b$ with respect to its
covariance is $\mathbb E\tanh'Z_a\tanh'Z_b$, whose magnitude is at
most one. This identity follows by differentiating the Gaussian density
and integrating by parts twice; approximation handles singular endpoints.
At zero covariance the expectation is zero. Hence the conditional
top-feature second-moment matrix has diagonal at most one and each
off-diagonal at most $1/(4m)$. Its operator norm is at most $5/4$.
A second conditional Hoeffding bound puts every empirical top-Gram entry
within $1/(4m)$ of its conditional expectation, giving operator norm at
most $3/2<4$. The two union bounds give (24).

Require the two explicit width conditions

\[
 2(m+1)^2e^{-n\varepsilon^2/(2(m+1)^3)}\le\frac12,
 \qquad
 2e^{-c_Wn}+4m^2e^{-n/(32m^2)}\le\frac{q^2}{16mn}.
\tag{25}
\]

They hold whenever $n\ge C(m+1)^3\log(e(m+1))$ for a sufficiently
large universal constant $C$. To see uniformity, substitute that lower
threshold in the exponentials; $n e^{-n/(32m^2)}$ is decreasing once
$n\ge32m^2$, and the remaining powers of $m$ are dominated after
increasing $C$. The finitely bounded small-$m$ case is covered by the
same increase.

Since $|K_y|\le m^{-1}\sum_a|y_a|\le Y$, (23)--(25) imply

\[
 \|K_y\mathbf1_{\mathcal T}\|_{L^2}
       \ge qY/(4\sqrt{mn}).
\tag{26}
\]

Choose explicitly

\[
 t_* =\min\{1/\sqrt{1464},q/28000\}.
\tag{27}
\]

The reverse triangle inequality in (13), followed by (17),(26), gives

\[
 \mathbb E[F(t_*,g)^2\mathbf1_{\mathcal T}]
      \ge\frac{q^2t_*^2Y^2}{16mn}.
\tag{28}
\]

Let $D=F(t_*,g)-\widetilde F(t_*,\widetilde g)$ for the independent
second network, and let $\widetilde{\mathcal T}$ be its good event.
Odd conditional symmetry gives
$\mathbb E[F\mathbf1_{\mathcal T}]=0$ exactly. Independence therefore
gives

\[
 \mathbb E[D^2\mathbf1_{\mathcal T\cap\widetilde{\mathcal T}}]
   =2\mathbb P(\mathcal T)
       \mathbb E[F^2\mathbf1_{\mathcal T}]
   \ge\frac{q^2t_*^2Y^2}{16mn},
\tag{29}
\]

where (25) ensures $\mathbb P(\mathcal T)\ge1/2$. The fourth moment is

\[
 \mathbb E[D^4\mathbf1_{\mathcal T\cap\widetilde{\mathcal T}}]
   \le\frac{80\cdot66^4Y^4t_*^4}{m^2n^2}.
\tag{30}
\]

For nonnegative $Z$, splitting its mean at $\mathbb EZ/2$ and applying
Cauchy--Schwarz gives
$\mathbb P\{Z\ge\mathbb EZ/2\}\ge(\mathbb EZ)^2/(4\mathbb EZ^2)$.
Apply this to $Z=D^2\mathbf1_{\mathcal T\cap\widetilde{\mathcal T}}$.
Equations (29)--(30) prove (4), for example with

\[
 c=\frac{qt_*}{4\sqrt2},\qquad
 p=\frac{q^4}{81920\cdot66^4}.
\tag{31}
\]

These constants are small and not optimized, but positive, explicit in
fixed one-dimensional Gaussian integrals, and independent of $m,n,Y$.

## 5a. The stronger sample factor at time proportional to sample count

**Further theorem.** Under the same model and width condition, assume
$0<Y\le1/m$. With exactly the constants $t_*,c,p$ above,

\[
 \mathbb P\left\{
 |f_n(mt_*,x_*)-\widetilde f_n(mt_*,x_*)|
        \ge c\frac{\sqrt m\,Y}{\sqrt n}\right\}\ge p.
\tag{31a}
\]

This is an actual positive-time predictor bound and therefore an
all-time sphere-supremum lower bound. The physical time grows as $m$
because the loss is averaged over $m$ examples. Labels remain fixed
independently of width for each fixed $m$. The displayed sufficient
label condition is conservative; no necessity is claimed.

To verify the statement, write $t=m\tau$, with
$0\le\tau\le t_0$. Reapply the stopped bootstrap of Section 2.
Its exit margins depend on $Y^2t^2=(mY)^2\tau^2$, so the assumed
$mY\le1$ proves the same bounds (7)--(9) throughout this larger physical
interval. In particular

\[
 \frac{\|w(m\tau)\|_2}{\sqrt n}\le6\sqrt m\,Y\tau,
 \qquad
 \|W(m\tau)-W_0\|_{\rm op}\le6(mY)^2\tau^2/\sqrt m.
\tag{31b}
\]

Retain the first inequality of (11), rather than its coarser last one.
The three gradient-subtraction terms in (16) are then bounded by

\[
 \frac{\sqrt m\,Y}{\sqrt n}
       [594\tau^2+5368(mY)^2\tau^3],\qquad
 \frac{\sqrt m\,Y}{\sqrt n}
       \frac{24(mY)^2\tau^3}{\sqrt m},\qquad
 \frac{\sqrt m\,Y}{\sqrt n}
       240(mY)^2\tau^3.
\tag{31c}
\]

Since $\tau\le1$ and $mY\le1$, these imply

\[
 \sup_g\|\nabla_gR(m\tau,g)\|_2
     \le\frac{7000\sqrt m\,Y\tau^2}{\sqrt n},
 \qquad
 \sup_g\|\nabla_gF(m\tau,g)\|_2
     \le\frac{66\sqrt m\,Y\tau}{\sqrt n}.
\tag{31d}
\]

The leading term is now $2m\tau K_y$. Equation (26) gives its
$L^2$ lower bound $q\sqrt m\,Y\tau/(2\sqrt n)$ on $\mathcal T$.
Conditional Gaussian Poincare and (31d), at $\tau=t_*$, preserve at
least half of that lower bound. The independent-copy second- and
fourth-moment argument (29)--(31), with $Y/\sqrt m$ replaced by
$\sqrt m\,Y$, proves (31a). This controls the complete nonlinear
remainder through time $mt_*$ and does not extrapolate an onset slope.

## 6. A self-contained dense fitted-endpoint proof for one input

Take $m=1$ and first $y>0$. Let $a=Ae_1$ and
$G_n=\|h_0^{(2)}\|_2^2/n$. Define the positive universal constant
$g_0=\tfrac12\mathbb E\tanh^2(\sqrt{Q/2}\,G)$, where $Q$ and
$G$ were defined in (18), and use the training-only event

\[
 \mathcal T_\infty=
 \{\|W_0\|_{\rm op}\le10,\ G_n\ge g_0\}.
\tag{32}
\]

Its complement satisfies the explicit bound

\[
 \mathbb P(\mathcal T_\infty^c)
 \le2e^{-c_Wn}+e^{-nQ^2/2}+e^{-2ng_0^2}.
\tag{32a}
\]

Indeed
$\|\tanh(A_0e_1)\|_2^2/n\ge Q/2$ except with exponentially small
probability at most $e^{-nQ^2/2}$, by Hoeffding's inequality on
$[0,1]$. Conditional on that column, the top preactivations are
independent Gaussian variables of variance at least $Q/2$. Their squared
tanh means are at least
$2g_0$, since tanh squared increases
with the magnitude of its argument. A further bounded-variable
concentration estimate gives the upper-feature failure probability
$e^{-2ng_0^2}$. The mixer tail was proved above. In addition to the
initialized lower-variance width condition from (19), require $n$ large
enough that the right side of (32a) is at most $q^2/(16n)$.

Until fitting, use the feature clock
$u(t)=2\int_0^t(y-f(s))\,ds$. Here $u$ is a scalar clock, distinct from
the norm used in Section 2. The autonomous feature-clock equations are

\[
 \frac{da}{du}=\delta^{(1)},\qquad
 \frac{dW}{du}=\delta^{(2)}h^{(1)\top}/n,\qquad
 \frac{dw}{du}=h^{(2)}.
\tag{33}
\]

For $0\le u\le1$, direct integration gives

\[
 \|w\|_\infty\le u,
 \quad\|W-W_0\|_{\rm op}\le u^2/2,
 \quad\frac{\|a-a_0\|_2}{\sqrt n}\le\frac{11}{2}u^2,
 \quad\frac{\|h^{(2)}-h_0^{(2)}\|_2}{\sqrt n}\le61u^2.
\tag{34}
\]

For example, the first velocity in (33) has RMS at most $11u$, and the
second has operator norm at most $u$; differentiation of
$\tanh(W\tanh a)$ bounds its normalized speed by
$u+11\cdot11u=122u$. Thus its displacement is at most $61u^2$.
Choose $u_0=g_0^{1/4}/16<1$. For $u\le u_0$, this displacement
is at most $61\sqrt{g_0}/256\le\sqrt{g_0}/4$. Therefore the
top-feature RMS remains at least $3\sqrt{g_0}/4$, and its squared
RMS remains above $g_0/2$.
The prediction derivative along (33) is exactly

\[
 \frac{df}{du}
 =\frac{\|h^{(2)}\|_2^2}{n}
  +\frac{\|\delta^{(1)}\|_2^2}{n}
  +\frac{\|\delta^{(2)}\|_2^2\|h^{(1)}\|_2^2}{n^2}
 \ge g_0/2.
\tag{35}
\]

For $0<y\le g_0u_0/2=g_0^{5/4}/32$, continuity and strict
monotonicity give a unique $u_\infty\in(0,2y/g_0]$ with
$f(u_\infty)=y$.
The scalar ODE $\dot u=2(y-f(u))$, $u(0)=0$, stays below this point
and converges to it. Its residual obeys
$0<y-f(t)\le y e^{-g_0t}$. This proves existence, convergence
and interpolation of the actual dense flow on (32).

Integrating the last equation in (33), then using (34), gives

\[
 w_\infty=u_\infty h_0^{(2)}+e,
 \quad\|e\|_2/\sqrt n\le\frac{61}{3}u_\infty^3,
 \quad\|W_\infty-W_0\|_{\rm op}\le\frac{2y^2}{g_0^2},
 \quad\|w_\infty\|_\infty\le\frac{2y}{g_0}.
\tag{36}
\]

Interpolation and the top-feature motion imply
$|y-u_\infty G_n|\le(244/3)u_\infty^3$: the two product-error
terms are bounded by $61u_\infty^3$ and
$(61/3)u_\infty^3$. Therefore, with the training-measurable
coefficient $\alpha_n=y/G_n$,

\[
 y\le\alpha_n\le y/g_0,
 \qquad
 \|w_\infty-\alpha_n h_0^{(2)}\|_2/\sqrt n
       \le\frac{2440}{3g_0^4}y^3.
\tag{37}
\]

For the second inequality, the bound before replacing $u_\infty$ is
$(61/3+244/(3g_0))u_\infty^3$. Use $g_0\le1$ and
$u_\infty\le2y/g_0$ to obtain the displayed coefficient.

For this section define
$K(g)=n^{-1}h_0^{(2)\top}\tanh(W_0\tanh g)$, without a label
factor. The fitted prediction has the exact decomposition

\[
 F_\infty(g)=\alpha_nK(g)+R_\infty(g).
\tag{38}
\]

It is still an odd function of the untouched independent Gaussian $g$.
Subtracting the gradients as in (16), and using (36)--(37), gives

\[
 \sup_g\|\nabla_gR_\infty(g)\|_2
        \le\frac{9000y^3}{g_0^4\sqrt n},
 \qquad
 \sup_g\|\nabla_gF_\infty(g)\|_2
        \le\frac{22y}{g_0\sqrt n}.
\tag{39}
\]

For the first gradient bound, the three subtraction terms are at most
$[11\cdot2440/(3g_0^4)]y^3/\sqrt n$,
$2y^3/(g_0^3\sqrt n)$ and $40y^3/(g_0^3\sqrt n)$.
Since $g_0\le1$, their sum is smaller than the stated coefficient.
Hence, conditionally on the training path,
$\mathbb E_gR_\infty^2\le9000^2y^6/(g_0^8n)$ and
$\mathbb E_gF_\infty^4\le5\cdot22^4y^4/(g_0^4n^2)$.
Section 4 with $m=1$ and label one gives
$\mathbb EK^2\ge q^2/(8n)$. Restricting to (32) preserves
$\|K\mathbf1_{\mathcal T_\infty}\|_{L^2}\ge q/(4\sqrt n)$,
by $|K|\le1$ and the specified bound after (32a).
Since $\alpha_n\ge y$ pointwise,

\[
 \|F_\infty\mathbf1_{\mathcal T_\infty}\|_{L^2}
 \ge\frac{y}{\sqrt n}\left(\frac q4-\frac{9000y^2}{g_0^4}\right).
\tag{40}
\]

Choose explicitly

\[
 y_*=\min\left\{\frac{g_0^{5/4}}{32},
                 g_0^2\sqrt{\frac q{72000}}\right\}.
\tag{40a}
\]

Then (40) is at least $qy/(8\sqrt n)$. Two independent copies
are conditionally centered. Repeating (29)--(30) and the second-moment
lower-tail argument proves (5), with the explicit constants

\[
 c_\infty=\frac q{8\sqrt2},\qquad
 p_\infty=\frac{q^4g_0^4}{1310720\cdot22^4}.
\tag{40b}
\]

Indeed, the second moment of the difference on the intersection of good
events is at least $q^2y^2/(64n)$, while its fourth moment is at most
$80\cdot22^4y^4/(g_0^4n^2)$.
All endpoint quantities are used only on their training-good events,
where convergence was proved. For negative labels the transformation
$(y,w)\mapsto(-y,-w)$ leaves the feature path unchanged and reverses
predictions, so the conclusion holds with $|y|$.

## 7. What the results do and do not establish

The lower bounds concern the same deep nonlinear architecture, Gaussian
initialization, zero readout, mobility convention, and averaged squared
loss as the dense target. The entire nonlinear remainder was bounded;
neither an initial slope alone nor an assumed Gaussian trained response
was substituted for a predictor. At the endpoint, every trajectory on
the probability event fits the training value exactly.

Independence of the two dense runs is essential to the equal-width
comparison. A coupling that sets their initialization equal makes their
difference identically zero. The lower bound therefore cannot hold for
arbitrary equal-width couplings. The one-input endpoint proof also gives
a fluctuation lower bound for a single run against its zero conditional
mean at the orthogonal query.

The $Y/\sqrt m$ factor is established at a fixed positive physical time
for orthogonal data, with the averaged loss in (2). It is not a universal
dataset factor or a fitted endpoint claim. At time proportional to $m$,
Section 5a instead establishes the factor $\sqrt m\,Y$ for $mY\le1$.
The full fitted endpoint for general $m$ remains outside this proof.
If repeated identical samples
are permitted, $m$ identical copies of the one-input datum induce exactly
the same averaged-loss flow, and (5) remains of size $|y|/\sqrt n$
regardless of their count. Data geometry and the physical time convention
therefore matter in any proposed universal sample-count rate.

The proof provides a nontrivial two-hidden-layer tanh class, not arbitrary
depth or all finite data. It gives no lower bound for a coordinated,
initialization-dependent compression using noncanonical weighted
coefficients. No code experiment, maintained-book edit, Git-index write,
or cross-study promotion was performed.

## 8. Read scope and frozen scientific inputs

This was a scoped research subagent assignment. The scientific starting
inputs were the supervisor's canonical dense equations and permitted
study boundary, the complete sources below, and the supervisor's proposed
endpoint constants, which were checked term by term before incorporation.
The complete nonlinear dense proofs above do not invoke a theorem from
the manuscript through a secondary citation. In particular, the endpoint
existence and fitting argument is derived directly from (33)--(35).

| Fully read scientific source | SHA-256 |
|---|---|
| `NEURON_GLOBAL_NEGATIVE.md` | `ddfca55aaaddd6bb80d74d0664038539ed8d7d1ee5ea52240eeee3d97de47e1c` |
| `NEURON_GLOBAL_NEGATIVE_CHECK.md` | `69001c76899af93a0e5d16bc7a975a20788ad4e330a4e2191521fa45d161ceeb` |
| `NEURON_GLOBAL_COORDINATOR_CHECK.md` | `62ad12a68ddb0f47f6ec5c82c19d17c83e2f172d9ee4365c8d4341c5a3988793` |
| `docs/notation.qmd` | `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023` |

The first three paths are relative to this study. Discovery also used
filename listings in this study and the explicitly authorized
`studies/dense_cutoff_population_rate_20261001` study, plus targeted
keyword search output from this study's README and the authorized prior
study's lower-route notes. No proof from those search snippets is used
as a premise. No other study, archived book, maintained-code source,
external paper, or browser source was read for this route.

The complete process instructions read were the canonical-notation skill
and its neural-response-memory reference, the rigorous-math skill, and
the conjecture-investigation skill with its research-contract and
adversarial-audit references. The task's shared instructions were supplied
in the assignment context. These skill-source hashes were:

| Skill source | SHA-256 |
|---|---|
| `explain-with-canonical-notation/SKILL.md` | `daac37e41dca5e618c5baf2a65689000e526930f059b822ebec61aafbfd1abfc` |
| `explain-with-canonical-notation/references/neural-response-memory.md` | `c2d570aac8950b5766513d81dd2dada4a9babeba92bbb554f1042107207a52b1` |
| `investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `investigate-conjectures/references/research-contract.md` | `7641d9418ab0065f29e6f25d6e78dd0005e436b0d1ab3970de4b1982bc95338e` |
| `investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
| `solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |

The canonical-notation files were read under
`/home/amir/.codex/skills/`; the other listed skills were read under
`/etc/codex/skills/`. Validation consisted of mathematical reconstruction,
explicit constant arithmetic, source hashing, and delimiter checks.
Only this assigned report was written.
