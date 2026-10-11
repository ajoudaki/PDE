# Two-sample escape: exact obstructions and the remaining Gaussian gap

Status: internally derived partial results, 2026-10-11. This is reused-context
work in the assigned study, not a fresh independent attempt. No experiment,
alternate initialization, frozen-layer substitution, or Git operation was used.
The assigned scientific inputs were the model, Section 5 of
UNCONDITIONAL_NEGATIVE_ROUTE.md, GAUSSIAN_POSITIVE_GEOMETRY.md, and maintained
book material. The arguments below are finite-width calculations and do not
invoke a population construction or the finite-bad-point avoidance candidate.

The strong target remains open: neither a fixed-data, fixed-label Gaussian
failure event with asymptotically positive probability, nor arbitrary-ratio
two-sample fitting for arbitrary correlation, is proved here. The positive
result obtained from the escape obstruction is narrower but exact: a
sign-coherent separated-residual tail is impossible for an obtuse or
orthogonal pair. Its proof retains every trained layer. Further exact results
restrict convergent escape predictions and identify a first/middle-layer
balance.

## 1. Model and quantifiers

Fix unit vectors \(x_1,x_2\in\mathbb R^d\) with
\(\rho=x_1^\top x_2\in(-1,1)\), and fixed labels
\(y=(y_1,y_2)^\top\ne0\). At width \(n\), let
\(A\in\mathbb R^{n\times d}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\). For sample \(a\in\{1,2\}\), define

\[
p_a=Ax_a,\qquad u_a=\tanh p_a,\qquad
z_a=Wu_a,\qquad h_a=\tanh z_a,\qquad
f_a=\frac1n w^\top h_a.
\]

Both nonlinearities act coordinatewise. Set \(H=(h_1,h_2)\),
\(f=(f_1,f_2)^\top\), and \(\theta=(A,W,w)\). Write
\[
r_a=f_a-y_a,\qquad
\mathcal L=\frac12(r_1^2+r_2^2),\qquad
D_a=1-u_a^2,\qquad E_a=1-h_a^2,
\qquad b_a=w\odot E_a,\qquad B_a=W^\top b_a .
\]
Here \(D_a,E_a\) are vectors, and \(\odot\) denotes coordinatewise
multiplication. In component formulas the neuron index precedes the sample
index, for example \(p_{ja}=(p_a)_j\) and \(E_{ia}=(E_a)_i\).
The prescribed mobilities \((n,1,n)\) give
\[
\begin{aligned}
\dot w&=-r_1h_1-r_2h_2,\\
\dot W&=-\frac1n(r_1b_1u_1^\top+r_2b_2u_2^\top),\\
\dot A&=-r_1(D_1\odot B_1)x_1^\top
        -r_2(D_2\odot B_2)x_2^\top.
\end{aligned}                                                   \tag{1}
\]
In particular,
\[
\begin{aligned}
\dot p_1&=-r_1D_1\odot B_1-\rho r_2D_2\odot B_2,\\
\dot p_2&=-\rho r_1D_1\odot B_1-r_2D_2\odot B_2 .
\end{aligned}                                                   \tag{2}
\]
The initialization is \(A_{ij}(0)\) iid \(N(0,1)\),
\(W_{ij}(0)\) iid \(N(0,1/n)\), independently, and exactly \(w(0)=0\).
The desired limit order is actual \(t\to\infty\) at each finite \(n\),
followed by \(n\to\infty\). All results below keep that order.

## 2. Energy, the readout identity, and the projection circle

For a parameter displacement use the squared norm
\[
\|(\Delta A,\Delta W,\Delta w)\|_{\rm par}^2
=\frac1n\|\Delta A\|_F^2+\|\Delta W\|_F^2
 +\frac1n\|\Delta w\|_2^2.
\]
The gradient-flow identity is
\[
-\dot{\mathcal L}
=\frac1n\|\dot A\|_F^2+\|\dot W\|_F^2
 +\frac1n\|\dot w\|_2^2.                                       \tag{3}
\]
Thus the squared speed is integrable on every existence interval. On
\([0,T]\), Cauchy--Schwarz bounds the path length by
\(\sqrt{T\mathcal L(0)}\). At fixed \(n\), the parameter norm above is
equivalent to the Euclidean norm. Since the vector field is smooth, this
finite-horizon bound excludes finite-time escape and proves global existence.

In fact,
\[
\|\theta(t)-\theta(0)\|_{\rm par}=o(\sqrt t),
\qquad
R(t):=\frac1n\|w(t)\|_2^2=o(t).                                \tag{4}
\]
To prove the first assertion, split the length integral at a fixed \(T\).
Writing its finite prefix as \(C_T\), for \(t>T\) one obtains
\[
\frac{\|\theta(t)-\theta(0)\|_{\rm par}}{\sqrt t}
\le \frac{C_T}{\sqrt t}
+\sqrt{1-T/t}\left(\int_T^\infty
   \|\dot\theta(s)\|_{\rm par}^2\,ds\right)^{1/2}.
\]
First take \(t\to\infty\), then \(T\to\infty\), using (3). The assertion
about \(R\) follows because the readout displacement is one component of
this norm and \(w(0)=0\).

Taking the inner product of the first equation in (1) with \(2w/n\) gives
the exact identity
\[
\dot R=-2f^\top r=-2(\|r\|_2^2+y^\top r).                      \tag{5}
\]
Write \(\mathcal L_\infty=\lim_{t\to\infty}\mathcal L(t)\).
Integrating (5), dividing by \(T\), and using (4) proves
\[
\lim_{T\to\infty}
y^\top\left(\frac1T\int_0^T r(t)\,dt\right)
 =-2\mathcal L_\infty.                                       \tag{6}
\]
If the predictions converge, \(f(t)\to f_\infty\), then the integrand
\(f^\top r\) converges. Its Cesàro limit and (5) imply
\[
f_\infty^\top(f_\infty-y)=0,
\qquad
\left\|f_\infty-\frac y2\right\|_2^2=\frac14\|y\|_2^2.         \tag{7}
\]
This conclusion does not require bounded parameters or bounded readout.
It restricts a convergent positive-loss escape prediction to a circle; it
does not establish convergence of the predictions or exclude the circle.

There is almost surely a strict initial loss decrease. Indeed,
\(\dot w(0)=H(0)y\). Conditional on an invertible \(W(0)\), which has
probability one, \(AX\) has a density on \(\mathbb R^{n\times2}\)
because \(X=(x_1,x_2)\) has rank two. The successive maps
\(AX\mapsto\tanh(AX)\mapsto W\tanh(AX)\mapsto H\) are
diffeomorphisms onto open images. Hence \(H\) has a density on an open
subset of \(\mathbb R^{n\times2}\), and \(Hy=0\) is null for \(y\ne0\).
Equation (3) then gives \(\dot{\mathcal L}(0)<0\).

After any strict drop, the readout norm cannot return to zero. More
precisely, if \(T\) satisfies \(\mathcal L(T)<\|y\|_2^2/2\), then
for every \(t\ge T\),
\[
\frac{\|w(t)\|_2}{\sqrt n}
\ge
\frac{\|y\|_2-\sqrt{2\mathcal L(T)}}{\sqrt2}>0.                 \tag{8}
\]
This follows from
\(\|f\|_2\ge\|y\|_2-\|r\|_2\) and
\(\|f\|_2\le\sqrt2\|w\|_2/\sqrt n\).

## 3. A conditional classification of full-feature-rank saturation escape

Suppose, at a fixed width and after a strict loss decrease, that
\[
U(t)=(u_1(t),u_2(t))\to U_\infty,\quad
H(t)\to H_\infty,\quad w(t)\to w_\infty,
\quad \operatorname{rank}U_\infty=2.                         \tag{9}
\]
If \(\mathcal L_\infty>0\), then some \(s\in\{1,-1\}\) satisfies
\[
f_\infty=
\left(\frac{y_1+s y_2}{2},
      s\,\frac{y_1+s y_2}{2}\right),\qquad
r_{\infty,2}=-s r_{\infty,1}\ne0.                            \tag{10}
\]
Every top neuron with \(w_{\infty,i}\ne0\) must be saturated on both
samples:
\[
h_{\infty,i1}\in\{1,-1\},
\qquad h_{\infty,i2}=s h_{\infty,i1}.                        \tag{11}
\]
In particular, \(\|W(t)\|_{\rm op}\to\infty\).

Here is the proof without an assumption of gradient convergence for
unbounded parameters. Under (9), \(f,r,b_1,b_2\) converge. The explicit
formulas for \(\dot w,\dot W\) in (1) therefore have limits. Their
squared norms are integrable by (3), so both limits must be zero:
\[
H_\infty r_\infty=0,\qquad
r_{\infty,1}b_{\infty,1}u_{\infty,1}^\top+
r_{\infty,2}b_{\infty,2}u_{\infty,2}^\top=0.                 \tag{12}
\]
By (8), \(w_\infty\ne0\). The two independent rows on the right of
the second identity imply, for any \(i\) with \(w_{\infty,i}\ne0\),
\[
r_{\infty,a}(1-h_{\infty,ia}^2)=0,\qquad a=1,2.
\]
If exactly one residual coordinate were nonzero, this would force the
corresponding \(h_{\infty,ia}\) to have absolute value one, while the
first identity in (12) would force that same entry to be zero. Therefore
both residual coordinates are nonzero, and both entries in every
nonzero-readout row have absolute value one.

The first identity in (12) now gives
\(|r_{\infty,1}|=|r_{\infty,2}|\). The common ratio
\(s=-r_{\infty,1}/r_{\infty,2}\) equals \(1\) or \(-1\), and
\(h_{\infty,i2}=s h_{\infty,i1}\) for every row that contributes to
\(f_\infty\). Thus \(f_{\infty,2}=s f_{\infty,1}\) and
\(r_{\infty,1}+s r_{\infty,2}=0\), giving (10).
For a nonzero-readout row, (11) implies
\(|z_{ia}(t)|\to\infty\); since \(\|u_a(t)\|_2\le\sqrt n\),
the operator norm of \(W\) tends to infinity.

The assumptions in (9) are essential limitations of this result.
Boundedness of activations does not give their convergence; finite
gradient energy does not give convergence of the readout. Rank collapse
of \(U_\infty\) is excluded here, not disproved.

## 4. Exact first/middle-layer balance and its correlation defect

For a first-layer neuron \(j\), define
\[
\mathcal I_j
=\|W_{:,j}\|_2^2
-\frac1n\{\sinh^2(p_{j1})+\sinh^2(p_{j2})\}.
\]
When \(\rho=0\), \(\mathcal I_j\) is conserved for the full
two-residual flow, with arbitrary labels and arbitrary finite parameters.
Indeed,
\[
\frac{d}{dt}\|W_{:,j}\|_2^2
=-\frac2n\sum_{a=1}^2 r_a u_{ja}B_{ja},
\]
whereas
\[
\frac{d}{dt}\sinh^2(p_{ja})
=2\,\frac{u_{ja}}{D_{ja}}\dot p_{ja}
=-2r_a u_{ja}B_{ja}
\]
when \(\rho=0\). All denominators here are positive at finite time.
In particular, for orthogonal inputs, bounded first preactivations imply
bounded middle weights. Unbounded middle weights force
\(\max_{j,a}|p_{ja}|\) to be unbounded; if \(\|W(t)\|_F\to\infty\),
then \(\max_{j,a}|p_{ja}(t)|\to\infty\).

For nonzero correlation the exact defect is instead
\[
\dot{\mathcal I}_j
=\frac{2\rho}{n}\left[
r_2 u_{j1}\frac{D_{j2}}{D_{j1}}B_{j2}
+r_1 u_{j2}\frac{D_{j1}}{D_{j2}}B_{j1}\right].                \tag{13}
\]
There is no fixed sign in (13), and the gate ratios can be unbounded.
Thus this calculation does not supply a conserved coercive quantity at
arbitrary correlation. It identifies exactly where the orthogonal
argument fails.

## 5. A sign-coherent separated-residual tail is impossible

The following proposition answers a concrete attempted saturation
mechanism without replacing the moving network by a scalar or
frozen-feature model. The final contradiction in the proof was suggested
by the supervisor after the bounded-middle-weight argument was derived.

**Proposition.** Suppose \(-1<\rho\le0\), \(w(0)=0\), and the trajectory
has a strict loss decrease. There cannot exist \(T<\infty\) and
\(\delta>0\) such that, for all \(t\ge T\), all the following hold
componentwise:
\[
W(t)\ge0,\quad w(t)\ge0,\quad p_1(t)\ge0,\quad p_2(t)\ge0,
\qquad r_1(t)\le-\delta,\quad r_2(t)\ge\delta.                \tag{14}
\]
No upper bound on the readout is assumed.

Increase \(T\), if necessary, so that the strict loss drop has already
occurred. Set \(R_y=\|y\|_2\); loss monotonicity gives
\(|r_a(t)|\le R_y\). In the cone (14), all \(u_a,h_a,b_a,B_a\)
are nonnegative. Equations (2) give
\[
\dot p_{j1}\ge\delta D_{j1}
                  \sum_iW_{ij}w_iE_{i1}\ge0,\qquad
-\dot p_{j2}\ge\delta D_{j2}
                  \sum_iW_{ij}w_iE_{i2}\ge0.                \tag{15}
\]
Thus \(p_{j1}\) increases, and \(p_{j2}\) decreases within
\([0,p_{j2}(T)]\). In particular,
\[
d_2:=\min_j\operatorname{sech}^2(p_{j2}(T))>0.
\]
Summing and integrating the second inequality in (15) proves
\[
\int_T^\infty
\sum_i w_i(t)E_{i2}(t)\sum_jW_{ij}(t)\,dt<\infty.            \tag{16}
\]

First consider a neuron \(j\) for which \(p_{j1}\) is bounded. Its
monotonicity gives a finite limit and a constant \(d_{1j}>0\) with
\(D_{j1}\ge d_{1j}\). The first inequality in (15) implies
\[
\int_T^\infty\sum_iW_{ij}w_iE_{i1}\,dt<\infty.
\]
On the other hand, the middle-weight equation gives
\[
\frac d{dt}W_{ij}^2
=\frac2nW_{ij}w_i
 \bigl(|r_1|E_{i1}u_{j1}-r_2E_{i2}u_{j2}\bigr)
\le\frac{2R_y}{n}W_{ij}w_iE_{i1}.                           \tag{17}
\]
Integration bounds every entry in this column of \(W\).

For each remaining \(j\), monotonicity means \(p_{j1}\to\infty\).
Therefore \(u_{j1}\to1\), while
\(u_{j2}\le\tanh(p_{j2}(T))<1\). After a common finite time
\(T_1\), these columns satisfy \(u_{j1}\ge u_{j2}\).
The bounded columns already treated can contribute only a bounded
negative amount to
\[
z_{i1}-z_{i2}=\sum_j W_{ij}(u_{j1}-u_{j2}).
\]
As the width is fixed and finite, there is \(C<\infty\) such that
\(z_{i1}\ge z_{i2}-C\) for every row and every \(t\ge T_1\).
Both preactivations are nonnegative, so
\(\cosh z_{i2}\le e^C\cosh z_{i1}\) and consequently
\[
E_{i1}\le e^{2C}E_{i2}.                                    \tag{18}
\]
Summing (17) over all entries, using \(u_{j1}\le1\), and then
using (18) gives
\[
\frac d{dt}\|W\|_F^2
\le\frac{2R_y e^{2C}}n
\sum_i w_iE_{i2}\sum_jW_{ij}.
\]
The right side is integrable by (16). Thus \(W\) is bounded on
the entire tail. This is the first obstruction: the proposed
sign-coherent top-saturation escape cannot make the middle weights
diverge.

Bounded \(W\) and \(\|u_2\|_2\le\sqrt n\) now imply
\(E_{i2}\ge e_2>0\), uniformly in time and row at this fixed
width. Equation (16) strengthens to
\[
\int_T^\infty\sum_i w_i\sum_jW_{ij}\,dt<\infty.
\]
The cone and \(\tanh z\le z\) for \(z\ge0\) imply, for both
samples,
\[
0\le f_a
\le\frac1n\sum_i w_i z_{ia}
\le\frac1n\sum_i w_i\sum_jW_{ij}.
\]
Hence \(\int_T^\infty(f_1+f_2)\,dt<\infty\).

Finally put
\(\Delta=\|y\|_2^2-2\mathcal L(T)>0\). For every later time,
\[
2y^\top f
=\|f\|_2^2+\|y\|_2^2-\|r\|_2^2
\ge\|f\|_2^2+\Delta.
\]
Since \(f_1,f_2\ge0\) and \(y\ne0\),
\[
f_1+f_2\ge\frac{\Delta}{2\|y\|_\infty}>0.
\]
This contradicts the preceding integrability and proves the proposition.

The proposition also applies after a fixed hidden-neuron sign gauge
\[
A\mapsto S_1 A,\quad W\mapsto S_2WS_1,\quad w\mapsto S_2w,
\]
where \(S_1,S_2\) are diagonal matrices with entries in \(\{1,-1\}\).
Oddness of tanh preserves every prediction, and these orthogonal
parameter changes preserve the mobilities and the flow. Input sign
absorption \(x_a\mapsto-x_a,\ y_a\mapsto-y_a\) likewise gives
equivalent variants. None of these equivalences proves that a canonical
Gaussian trajectory eventually has the sign pattern (14).

## 6. What is and is not resolved

The following claims are proved above, for the original finite-width
flow:

- Global existence, finite gradient energy, the sub-\(\sqrt t\)
  displacement bound, and the readout Cesàro identity.
- If predictions converge, their limit obeys the projection-circle
  identity, even with unbounded readout.
- Under the explicit convergence and rank assumptions (9), a
  positive-loss limit must be a common/contrast projection with every
  nonzero-readout top neuron saturated.
- A columnwise first/middle-layer invariant for orthogonal inputs, with
  the exact nonorthogonal defect.
- Impossibility of an eventual sign-coherent, separated-residual tail
  for an obtuse or orthogonal pair.

The last result defeats the naive mechanism in which positive middle
weights grow while a lower-output positive sample remains persistently
underfit and the other positive sample persistently overfit. Corrective
first-layer motion cannot be ignored: its monotone budget first bounds
the middle weights and then forces an integrability contradiction.

The decisive open point is signed cancellation. A dense canonical
Gaussian middle matrix is not nonnegative, nor generally made
nonnegative by a fixed row/column sign gauge. The quantities in (15)
then cease to be nonnegative, so bounded monotone budgets are unavailable.
The balance defect (13), bounded activation ranges, and finite gradient
energy do not replace those budgets. Nor has this work shown convergence
of \(U,H,w\) or prevented first-feature rank collapse.

Consequently this file does not assert unconditional Gaussian fitting,
positive Gaussian probability of failure, or generic avoidance of all
saturation faces at infinity. The finite-bad-point avoidance candidate
from the assigned source is logically separate and is not needed for
any proposition above.
