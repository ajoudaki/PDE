# Tanh frozen-top NTH: the upper-bound bridge and a coordinate obstruction

This scoped author derivation concerns the canonical two-hidden-layer tanh
model on general fixed finite inputs. It does **not** prove the requested
width-dependent prediction-accuracy theorem. It proves a conditional
all-trajectory approximation criterion with explicit order and storage,
an unconditional obstruction to a coordinate-strip proof of its hypothesis,
and an unconditional all-time whole-sphere error bound for orders two and
three. The obstruction concerns coordinate-strip analyticity, not the
prediction error of the hierarchy.

The scientific inputs were the supervisor's assignment, `docs/notation.qmd`,
the setup and complete initialization/fitting argument in
`docs/08b-trajectory-compression.qmd` (lines 1--465), that chapter's analytic
source interface and local definitions (lines 512--732), and this study's
`POLYNOMIAL_UPPER.md` and `ANALYTIC_ROUTE.md`. No other study, archived book,
experiment, or external scientific source was used. Required notation,
research, proof, and scoped-work instructions were read. The author is
`/root/tanh_nth_upper`; this is not an independent promotion review.

## 1. Canonical model and exact hierarchy

Let the fixed unit vectors be \(v_a=x_a/\sqrt d\), \(1\le a\le m\),
with arbitrary input Gram \(G_{ab}=v_a^\top v_b\). There may also be \(p\)
passive unit inputs declared before initialization. Put

\[
\begin{aligned}
z_a^{(1)}&=W^{(1)}v_a,&h_a^{(1)}&=\tanh z_a^{(1)},\\
z_a^{(2)}&=W^{(2)}h_a^{(1)},&h_a^{(2)}&=\tanh z_a^{(2)},\\
f_a&=u^\top h_a^{(2)}/n,&r_a&=f_a-y_a,
&\mathcal L&=\frac1{2m}\sum_{a=1}^m r_a^2.
\end{aligned}
\]

The shapes of \(W^{(1)},W^{(2)},u\) are \(n\times d,n\times n,n\).
The independent initial entries have laws \(N(0,1),N(0,1/n)\), and

\[
u_0=0.
\]

The mobility blocks are \(n,1,n\). For a unit residual driving direction
define

\[
\begin{aligned}
\delta_b^{(2)}&=u\odot\tanh'(z_b^{(2)}),\\
\delta_b^{(1)}&=\tanh'(z_b^{(1)})\odot W^{(2)\top}\delta_b^{(2)},\\
V_b&=\left(\delta_b^{(1)}v_b^\top,
       \delta_b^{(2)}h_b^{(1)\top}/n,h_b^{(2)}\right).
\end{aligned}
\]

Thus the exact gradient flow is

\[
\dot\theta=\sum_{b=1}^m c_bV_b(\theta),\qquad
c_b=(y_b-f_b)/m,
\]

where \(\theta=(W^{(1)},W^{(2)},u)\). The letter \(c\) denotes the
residual control and is not a readout. Define

\[
K_{1,a}=f_a,\qquad
K_{s+1,a_1\ldots a_s b}=D K_{s,a_1\ldots a_s}[V_b].
\tag{1}
\]

In particular, directly differentiating the output gives

\[
K_{2,ab}=\frac{h_a^{(2)\top}h_b^{(2)}}n
 +\frac{\delta_a^{(2)\top}\delta_b^{(2)}}n
       \frac{h_a^{(1)\top}h_b^{(1)}}n
 +G_{ab}\frac{\delta_a^{(1)\top}\delta_b^{(1)}}n.
\tag{2}
\]

This is the tangent Gram in the actual mobility metric. At initialization
only its first term survives. For the half-mean loss used here, the
maintained chapter's dense path is traversed at half its stated speed.

The order-\(q\) frozen-top model, \(q\ge2\), initializes every retained
tensor from (1), evolves

\[
\dot K^{(q)}_{s,a_1\ldots a_s}
 =\sum_bK^{(q)}_{s+1,a_1\ldots a_s b}c_b^{(q)}
 \quad(s<q),\qquad \dot K_q^{(q)}=0,
\quad c_b^{(q)}=(y_b-f_b^{(q)})/m.
\tag{3}
\]

Its residual control is its own. No dense future trajectory is an input.

## 2. A sufficient ordered-derivative estimate, with all constants exposed

Write \(Y=\|y\|_2/\sqrt m>0\), and let \(\gamma>0\) be the population
feature-Gram gap. Work on an initialization event where

\[
K_2(\theta_0)\succeq\frac\gamma2 I_m.
\tag{4}
\]

Suppose the canonical dense trajectory has the maintained chapter's real
fitting guarantee. In the present physical time this gives

\[
\|r(t)\|_2\le\sqrt mY e^{-\alpha t},\qquad
\alpha=\frac\gamma{4m},\qquad
\int_0^\infty\sum_b|c_b(t)|dt\le a:=Y/\alpha.
\tag{5}
\]

Here is the additional hypothesis that is **not proved for tanh**:
there are \(M,R>0\), independent of \(n\), such that for every

\[
k\ge0,\quad j\in\{1,\ldots,m+p\},\quad
b,b_1,\ldots,b_k\in\{1,\ldots,m\},\quad t\ge0,
\]

one has

\[
|K_{k+2,jb b_1\ldots b_k}(\theta(t))|
\le M k!R^{-k}.
\tag{6}
\]

The constants may depend on the fixed problem and confidence, but cannot
shrink their radius with width. In particular (6) includes initialization.
Put

\[
\vartheta=a/R<1,\qquad
H=\frac M{1-\vartheta},\qquad
\ell=\frac M{R(1-\vartheta)^2}.
\]

Assume the explicit smallness conditions

\[
\frac{mM\vartheta}{1-\vartheta}\le\frac\gamma4,
\qquad \frac{\ell Y}{\alpha^2}\le\frac12.
\tag{7}
\]

Then every \(q\ge2\) model (3) is global and has a fitted training limit.
Its passive predictions also converge, and

\[
\sup_{t\in[0,\infty]}\max_{1\le j\le m+p}
 |f_j^{(q)}(t)-f_j(t)|
\le C_*\vartheta^{q-1},\qquad
C_*:=\frac{2YM}{1-\vartheta}
       \left(\frac H{\alpha^2}+\frac1\alpha\right).
\tag{8}
\]

For any fixed \(\varepsilon>0\), choosing

\[
q_n=\max\left\{2,
1+\left\lceil
\frac{(1/2+\varepsilon)\log n+\log C_*}
     {\log(1/\vartheta)}\right\rceil\right\}
\tag{9}
\]

would give an error at most \(n^{-1/2-\varepsilon}\). The explicit array
count is

\[
(m+p)\sum_{s=1}^{q_n}m^{s-1}
=\frac{(m+p)(m^{q_n}-1)}{m-1}
=O\!\left(n^{(1/2+\varepsilon)\log m/\log(1/\vartheta)}\right).
\tag{10}
\]

This counts retained tensors, not dense coefficient-compilation time or
scratch. For whole-sphere error, (6) can be required uniformly over the
first input slot, and the proof of (8) remains valid. However, storing that
continuum of initialized coefficient functions is an additional problem:
(10) is only a finite-panel scalar-storage count. Retaining the dense
initialization to evaluate new query coefficients costs \(O(n^2+nd)\)
additional coordinates.

### Proof of the criterion

For a real control path \(c\), write

\[
A_c(t)=\int_0^t\sum_b|c_b(s)|ds,
\quad
I_{b_1\ldots b_k}[c](t)=
\int_{0\le t_k\le\cdots\le t_1\le t}
\prod_{i=1}^k c_{b_i}(t_i)\,dt_k\cdots dt_1.
\]

The first listed driving index occurs at the latest integration time.
Summing absolute values over all words gives at most \(A_c(t)^k/k!\).
Repeated integration of (3) gives its kernel exactly as

\[
\mathcal K_q[c]_{jb}(t)=
\sum_{k=0}^{q-2}\sum_{b_1,\ldots,b_k}
K_{k+2,jb b_1\ldots b_k}(\theta_0)
I_{b_1\ldots b_k}[c](t).
\tag{11}
\]

Let \(\mathcal K_\infty\) be the infinite sum. On \(A_c\le a\), (6)
gives absolute convergence, the entry bound \(H\), and

\[
\begin{aligned}
|\mathcal K_q[c]_{jb}-K_{2,jb}(\theta_0)|
 &\le\frac{M\vartheta}{1-\vartheta},\\
|\mathcal K_\infty[c]_{jb}-\mathcal K_q[c]_{jb}|
 &\le\tau_q:=\frac{M\vartheta^{q-1}}{1-\vartheta}.
\end{aligned}
\tag{12}
\]

For two controls with action at most \(a\), interpolation between them
and a single difference insertion in each word give

\[
|\mathcal K_q[c]_{jb}(t)-\mathcal K_q[d]_{jb}(t)|
\le\ell\int_0^t\sum_b|c_b-d_b|ds.
\tag{13}
\]

Indeed the sum over the \(k\) insertion positions is bounded by

\[
\frac{a^{k-1}}{(k-1)!}
\int_0^t\sum_b|c_b-d_b|ds,
\]

and the derivative majorant sums to \(M/[R(1-\vartheta)^2]\).
This argument also proves (13) for \(q=\infty\).

Along the actual dense trajectory, expand its kernel through \(N\)
integrations. The remainder has \(K_{N+3}\) at a moving dense state.
By (6), its absolute value is bounded by

\[
M(N+1)!R^{-N-1}\frac{A_c(t)^{N+1}}{(N+1)!}
\le M\vartheta^{N+1}\longrightarrow0.
\]

Thus its actual kernel equals \(\mathcal K_\infty[c]\), rather than
merely having the same formal coefficients.

The first two slots of \(K_2\) are symmetric on the training panel,
and differentiating preserves that symmetry. Therefore the training
matrix in (11) is symmetric for all real controls. Its displacement
from \(K_2(\theta_0)\) has operator norm at most \(m\) times the first
bound in (12). Equations (4) and (7) imply

\[
\mathcal K_q[c]\succeq\frac\gamma4 I_m.
\]

Until any first exit through \(A_{c^{(q)}}=a\), the residual equation
therefore gives \(\|r^{(q)}(t)\|_2\le\sqrt mY e^{-\alpha t}\), and

\[
A_{c^{(q)}}(t)\le a(1-e^{-\alpha t})<a.
\]

This excludes a finite exit. Formula (11), and its counterpart for
every retained tensor, bound all finite-dimensional coordinates at
fixed \(n,q\); the polynomial ODE consequently continues globally.

Let \(e=f^{(q)}-f\) on the training panel and

\[
E_1(T)=\int_0^T\|e(t)\|_2dt.
\]

The control difference satisfies
\(\sum_b|c_b^{(q)}-c_b|\le\|e\|_2/\sqrt m\).
Equations (12)--(13) imply that the maximum entry of the kernel
discrepancy, including passive rows, is at most

\[
\delta_T:=\ell E_1(T)/\sqrt m+\tau_q\quad(t\le T).
\]

The error equation is

\[
\dot e=-\mathcal K_q[c^{(q)}]e/m
 -(\mathcal K_q[c^{(q)}]-\mathcal K_\infty[c])r/m.
\]

Its homogeneous evolution contracts by \(e^{-\alpha(t-s)}\), and
the forcing norm is at most \(\delta_T\|r\|_2\). Integrating in
time and using (5) gives

\[
E_1(T)\le\frac{\sqrt mY}{\alpha^2}
       (\ell E_1(T)/\sqrt m+\tau_q).
\]

The second inequality in (7) yields

\[
\int_0^\infty\|e(t)\|_2dt\le
\frac{2\sqrt mY\tau_q}{\alpha^2},
\qquad \sup_T\delta_T\le2\tau_q.
\]

For any training or passive row \(j\), the output error starts at zero
and its derivative has absolute value at most

\[
H\|e\|_2/\sqrt m+2\tau_q\|r\|_2/\sqrt m.
\]

Integration proves (8). Integrability of all residual controls and
the finite sums for the retained state give its limits; (5) and its
closure counterpart give fitting. No common residual clock has been
substituted for physical time.

## 3. An exact Gaussian obstruction to a uniform coordinate strip

Fix any one training input \(v_b\), without imposing assumptions on
its correlations with the other inputs. Consider the auxiliary local
flow in the actual hierarchy direction

\[
\frac{d\theta}{ds}=V_b(\theta),\qquad \theta(0)=\theta_0.
\tag{14}
\]

This is not the trained trajectory and makes no assertion about its
residual. It is the vector field whose repeated application defines
the repeated-\(b\) NTH coefficients.

At \(s=0\), the two hidden-weight derivatives vanish and \(u'=h_b^{(2)}\).
Differentiating the first-layer equation once more gives exactly

\[
\left.\frac{d^2z_b^{(1)}}{ds^2}\right|_{s=0}
=\tanh'(z_{b,0}^{(1)})\odot
 W_0^{(2)\top}
 [\tanh(z_{b,0}^{(2)})\odot\tanh'(z_{b,0}^{(2)})].
\tag{15}
\]

In particular, this quantity is not uniformly bounded coordinatewise
in width. More precisely there are fixed positive constants \(c,C\)
such that, with probability tending to one,

\[
c\sqrt{\log n}\le
\max_i\left|\left.\frac{d^2z_{b,i}^{(1)}}{ds^2}\right|_{s=0}\right|
\le C\sqrt{\log n}.
\tag{16}
\]

Here is a direct proof. Set \(h=h_{b,0}^{(1)}\), \(z=z_{b,0}^{(2)}\),
and \(w_i=\tanh(z_i)\tanh'(z_i)\). Conditional on \(h,z\), Gaussian
row regression gives

\[
W_0^{(2)\top}w
\overset{\mathrm{law}}=
\mu h+\sigma\left(g-h\frac{h^\top g}{\|h\|_2^2}\right),
\quad
\mu=\frac{z^\top w}{\|h\|_2^2},\quad
\sigma^2=\frac{\|w\|_2^2}{n},
\tag{17}
\]

where \(g\sim N(0,I_n)\) is conditionally independent. To obtain (17),
decompose each row of \(W_0^{(2)}\) into its projection on \(h\) and
its perpendicular part. The latter is an independent Gaussian vector
with covariance \(n^{-1}(I-hh^\top/\|h\|_2^2)\), even after the row's
inner product with \(h\) has been conditioned on. Summing with weights
\(w_i\) yields (17).

The first-layer coordinates \(z_{b,0,i}^{(1)}\) are iid \(N(0,1)\), so

\[
\frac{\|h\|_2^2}{n}\longrightarrow
q_1:=\mathbb E\tanh(G)^2>0.
\]

Conditional on \(h\), the coordinates of \(z\) are independent
\(N(0,\|h\|_2^2/n)\). Boundedness of \(w_i\), and bounded second
moments of \(z_iw_i\), give by conditional Chebyshev and continuity

\[
\sigma^2\longrightarrow
\mathbb E[\tanh(Z)^2\tanh'(Z)^2]>0,
\quad
\mu\longrightarrow
\frac{\mathbb E[Z\tanh(Z)\tanh'(Z)]}{q_1},
\quad Z\sim N(0,q_1).
\]

A positive fraction of the first-layer coordinates lie in
\([-1,1]\) with probability tending to one. On this index set
\(\tanh'(z_{b,0,i}^{(1)})\ge\operatorname{sech}^2(1)>0\), whereas
\(|h_i|\le1\) everywhere. The projection correction in (17) has
coordinate maximum at most

\[
\frac{|h^\top g|}{\|h\|_2^2}=O_{\mathbb P}(n^{-1/2}).
\]

The maximum of independent standard Gaussian absolute values on a
set of size at least \(c_0n\) is between fixed positive multiples of
\(\sqrt{\log n}\) with probability tending to one. The upper bound
follows from a Gaussian tail union bound. For the lower bound at
\(x=\sqrt{\log n}\), integrating the Gaussian density over
\([x,x+1/x]\) gives tail probability at least
\(c n^{-1/2}/\sqrt{\log n}\); hence the probability that every one
of \(c_0n\) independent coordinates lies below \(x\) tends to zero.
The bounded common drift \(\mu h\) and the vanishing projection
correction cannot change these orders. This proves (16).

Now suppose (14) has a holomorphic extension on a disk \(|s|<R_n\)
that keeps all first-layer preactivations in a fixed horizontal strip,

\[
|\operatorname{Im}z_{b,i}^{(1)}(s)|\le a_0
\quad (|s|<R_n,;1\le i\le n),
\tag{18}
\]

where \(a_0>0\) is fixed, for example \(a_0=\pi/4\). If a scalar
holomorphic function has imaginary part bounded by \(a_0\) on this
disk, its Taylor coefficient of order two has absolute value at most
\(2a_0/R_n^2\). To verify this, restrict to a circle of radius
\(\rho<R_n\), take the second Fourier coefficient of its imaginary
part, and then let \(\rho\uparrow R_n\). Therefore

\[
\max_i|z_{b,i}^{(1)\prime\prime}(0)|\le4a_0/R_n^2.
\]

Together with (16), this proves the unconditional implication

\[
\text{the coordinate-strip condition (18)}
\quad\Longrightarrow\quad
R_n\le C_{a_0}(\log n)^{-1/4}
\tag{19}
\]

on an event of probability tending to one. This rules out a width-uniform
control disk of this coordinate-strip kind. It does not show that an
output singularity lies at that distance: coordinate cancellations in
the normalized prediction are not excluded.

There is a related simpler obstruction to using unrestricted parameter
balls. The mobility norm is

\[
\|\Delta\theta\|_{\mathrm{par}}^2
=\|\Delta W^{(1)}\|_F^2/n
 +\|\Delta W^{(2)}\|_F^2+\|\Delta u\|_2^2/n.
\]

For a row with \(|z_{b,0,i}^{(1)}|\le1\), changing that row by
\((-z_{b,0,i}^{(1)}+i\pi/2)v_b^\top\) reaches a pole of its
first-layer tanh at mobility distance at most
\(\sqrt{1+\pi^2/4}/\sqrt n\). Thus a complex parameter ball on
which every forward source is holomorphic also cannot have a
width-independent radius. The restricted controlled path is a different
object, which is why (15)--(19) were proved separately.

## 4. An unconditional all-time bound for orders two and three

The following fixed-order result is valid for the actual tanh model and
general correlated inputs. It does not decay with width when the labels
are fixed, so it is a partial result rather than the requested compression
theorem.

Write

\[
\lambda=\gamma/m\le1.
\]

Assume the finite initialization event

\[
\|W_0^{(2)}\|_{\mathrm{op}}\le8,
\qquad K_2(\theta_0)\succeq\frac\gamma2 I_m,
\tag{20}
\]

and \(0<Y\le\lambda/64\). This label range includes the maintained
chapter's range \(Y\le\lambda\beta^{-60}\), since its \(\beta\ge10\).
Event (20) has probability tending to one for the stated initialization
and every fixed data set with the population gap \(\gamma>0\).

Then both the dense flow and the order-two hierarchy are global and fit
the training labels. For every real unit query \(v\), both predictions
have limits, and

\[
\sup_{t\in[0,\infty]}\sup_{\|v\|_2=1}
 |f_v^{(2)}(t)-f_v(t)|
\le7300\,\frac{Y^3}{\lambda^3}.
\tag{21}
\]

The order-three model is exactly the order-two model, so (21) holds for
it as well. These are explicit, unconditional finite-width statements
on (20); there is no derivative-growth premise such as (6).

### Real-flow bootstrap

Let \(\rho=\|r\|_2/\sqrt m\), and stop the dense flow if
\(\|W^{(2)}\|_{\mathrm{op}}\) reaches nine or the smallest singular
value of

\[
\mathsf H/\sqrt{mn},\qquad
\mathsf H=[h_1^{(2)},\ldots,h_m^{(2)}],
\]

reaches \(\sqrt\lambda/2\). Before the stop, the readout part of the
tangent Gram gives \(K_2\succeq\gamma I_m/4\), and hence

\[
\rho(t)\le Ye^{-\lambda t/4},\qquad
\int_0^t\rho(s)ds\le4Y/\lambda.
\tag{22}
\]

The mobility norm defined in Section 3 satisfies the energy identity

\[
\|\dot\theta\|_{\mathrm{par}}^2=-\rho\dot\rho.
\]

Cauchy--Schwarz, applied with factors
\(\|\dot\theta\|_{\mathrm{par}}/\sqrt\rho\) and
\(\sqrt\rho\), gives

\[
\int_0^t\|\dot\theta\|_{\mathrm{par}}ds
\le\sqrt{Y\,4Y/\lambda}=2Y/\sqrt\lambda.
\tag{23}
\]

If \(\rho\) first vanishes, the flow stops, so (23) extends without
division by zero. In particular, \(\|u\|_2/\sqrt n\le2Y/\sqrt\lambda\).
Since \(|\tanh|,|\tanh'|\le1\) on the real line, the backward
formulas yield

\[
\|\dot W^{(2)}\|_F
\le\rho\|u\|_2/\sqrt n,
\quad
\|\dot W^{(1)}\|_F/\sqrt n
\le9\rho\|u\|_2/\sqrt n.
\]

Consequently

\[
\|W^{(2)}-W_0^{(2)}\|_F\le8Y^2/\lambda^{3/2},
\qquad
\|W^{(1)}-W_0^{(1)}\|_F/\sqrt n
\le72Y^2/\lambda^{3/2}.
\tag{24}
\]

For every real unit input, the first-layer feature displacement in RMS
is bounded by the second quantity in (24). In the second layer, write

\[
W^{(2)}h^{(1)}-W_0^{(2)}h_0^{(1)}
=(W^{(2)}-W_0^{(2)})h^{(1)}
 +W_0^{(2)}(h^{(1)}-h_0^{(1)}).
\]

Using \(\|h^{(1)}\|_2/\sqrt n\le1\) and the initialized operator
bound gives

\[
\sup_{\|v\|_2=1}
\|h^{(2)}(t,v)-h_0^{(2)}(v)\|_2/\sqrt n
\le584Y^2/\lambda^{3/2}.
\tag{25}
\]

The label condition bounds this by
\((584/4096)\sqrt\lambda\). Thus the smallest singular value of
\(\mathsf H/\sqrt{mn}\) remains at least

\[
\left(\frac1{\sqrt2}-\frac{584}{4096}\right)\sqrt\lambda
>\frac{\sqrt\lambda}{2}.
\]

The hidden operator norm remains below \(8+8/4096<9\). Both stops
have strict margins. At fixed width, (23)--(24) bound every parameter
coordinate, proving global continuation, parameter convergence and
fitting. This argument derives the needed fitting estimate directly;
it does not impose an additional power of \(\lambda\) on the labels.

### Kernel and prediction comparison

For any two real unit queries, the change of the first term in (2) is
at most twice the right side of (25). The other two terms in (2) are
at most \(\|u\|_2^2/n\) and \(81\|u\|_2^2/n\), respectively.
Hence the full tangent-kernel entry displacement is bounded by

\[
D:=1168Y^2/\lambda^{3/2}+328Y^2/\lambda
\le1496Y^2/\lambda^{3/2}.
\tag{26}
\]

The order-two training residual evolves with the constant positive
matrix \(K_2(\theta_0)/m\), whose gap is \(\lambda/2\). Let
\(e=f^{(2)}-f\) on the training inputs. Subtraction gives

\[
\dot e=-K_2(\theta_0)e/m
 -(K_2(\theta_0)-K_2(\theta(t)))r/m.
\]

Its forcing norm is at most \(D\|r\|_2\). The constant-kernel
propagator contracts at rate \(\lambda/2\), so (22) yields

\[
\frac{\|e(t)\|_2}{\sqrt m}
\le DY\int_0^t e^{-\lambda(t-s)/2}e^{-\lambda s/4}ds
=\frac{4DY}{\lambda}
  (e^{-\lambda t/4}-e^{-\lambda t/2})
\le\frac{DY}{\lambda}.
\tag{27}
\]

For the sphere estimate, define the frozen-feature readout only as a
proof representation of the exact order-two prediction:

\[
\dot u_{\mathrm{fr}}=-\mathsf H_0r^{(2)}/m,
\qquad u_{\mathrm{fr}}(0)=0,
\qquad f_v^{(2)}=u_{\mathrm{fr}}^\top h_0^{(2)}(v)/n.
\]

Let \(P\) be the Euclidean orthogonal projection onto the column
space of \(\mathsf H_0\), put \(w=u_{\mathrm{fr}}-u\), and write
\(D_h=584Y^2/\lambda^{3/2}\). The exact readout difference is

\[
\dot w=-\mathsf H_0e/m
 +(\mathsf H-\mathsf H_0)r/m.
\]

Projection onto the perpendicular space, followed by (22) and (25),
gives

\[
\frac{\|(I-P)w(t)\|_2}{\sqrt n}
\le D_h\int_0^t\rho(s)ds
\le\frac{4D_hY}{\lambda}.
\tag{28}
\]

The component in the column space is determined by its initialized
training pairings. Their exact identity is

\[
\mathsf H_0^\top w/n
=e+(\mathsf H-\mathsf H_0)^\top u/n.
\]

The least singular value of \(\mathsf H_0/\sqrt{mn}\) is at least
\(\sqrt{\lambda/2}\), by (20). On its column space, therefore,

\[
\frac{\|Pw(t)\|_2}{\sqrt n}
\le\sqrt{\frac2\lambda}
 \left(\frac{\|e(t)\|_2}{\sqrt m}
            +D_h\frac{\|u(t)\|_2}{\sqrt n}\right)
\le\sqrt{\frac2\lambda}
 \left(\frac{DY}{\lambda}
                  +\frac{2D_hY}{\sqrt\lambda}\right).
\tag{29}
\]

For a real unit query, \(\|h_0^{(2)}(v)\|_2/\sqrt n\le1\), so

\[
\begin{aligned}
|f_v^{(2)}-f_v|
&\le\frac{\|w\|_2}{\sqrt n}
       +D_h\frac{\|u\|_2}{\sqrt n}\\
&\le\frac{4D_hY}{\lambda}
 +\sqrt{\frac2\lambda}
       \left(\frac{DY}{\lambda}
                  +\frac{2D_hY}{\sqrt\lambda}\right)
 +\frac{2D_hY}{\sqrt\lambda}\\
&\le(3504+2664\sqrt2)\frac{Y^3}{\lambda^3}
 <7300\frac{Y^3}{\lambda^3}.
\end{aligned}
\]

Here the last line uses \(\lambda\le1\), (26), and the definition
of \(D_h\). This proves (21). Dense outputs converge uniformly over the sphere
because the parameter length is finite and the real forward map has
the preceding uniform RMS bounds. The order-two passive derivatives
are integrable because its training residual decays exponentially.
Thus the endpoint in (21) is included.

Finally let \(R\theta=(W^{(1)},W^{(2)},-u)\). The exact identities

\[
f(R\theta)=-f(\theta),\qquad
V_b(R\theta)=-DR\,V_b(\theta)
\]

and induction in (1) give
\(K_s(R\theta)=(-1)^sK_s(\theta)\). Every odd tensor vanishes at
\(u=0\). In the order-three hierarchy, the frozen \(K_3\) is
therefore identically zero and \(K_2\) remains fixed: it is exactly
the order-two prediction. The same reasoning shows that order
\(2j+1\) and order \(2j\) have identical predictions at this zero
readout initialization.

The whole-sphere estimate (21) is an accuracy statement. A finite
implementation on a declared panel stores its initialized
\((m+p)\times m\) kernel. Evaluation at arbitrary later sphere
queries additionally needs its initial query-feature evaluator, which
can retain the dense initialized weights; that cost cannot be omitted.

## 5. What this resolves and what remains open

An attempted Gaussian-integration-by-parts repair did not close (6).
For a scalar standard Gaussian coordinate with density \(\varphi\),
put \(L\psi=\operatorname{sech}^2(z)\psi'(z)\). Direct integration
by parts gives the exact adjoint identity

\[
\int aL\psi\,\varphi\,dz
=\int \psi\,\operatorname{sech}^2(z)
       [(z+2\tanh z)a-a']\,\varphi\,dz.
\tag{30}
\]

It transfers derivatives off an observable but creates derivatives of
the nonlinear coefficient. In the elementary independent-carrier
operator \(gL\), averaging its \(2k\)-fold action still introduces
the exact factor \(\mathbb E g^{2k}=(2k-1)!!\). No estimate was proved
that compensates this factor in the actual neural observable. This
calculation is a diagnostic of the proposed proof method, not a
replacement network or a Gevrey theorem for the network.

Gaussian averaging alone settles neither direction. For example,
\(\mathbb E\tanh(sg)^2\) is smooth at zero but has Taylor coefficients
obtained by multiplying those of \(\tanh(s)^2\) by Gaussian even
moments; its Taylor radius is zero. The unaveraged series has radius
\(\pi/2\), from its nearest double poles, while
\(((2k-1)!!)^{1/(2k)}\) tends to infinity. Fixed-order differentiation
under the expectation is valid because all real tanh derivatives are
bounded and Gaussian moments are finite. In contrast, for independent
standard Gaussians \(Z,g\), the real function
\(\mathbb E\tanh(Z+sg)^2\) is analytic near zero: it equals the
Gaussian density integral with variance \(1+s^2\), whose complex
variance extension is holomorphic near one by domination. Thus neither
the presence of Gaussian carriers nor bounded tanh values justifies
an assertion about the actual model's averaged Taylor radius.

The conditional criterion completely handles ordered simplex factors,
the closure's own residual, preservation of the training Gram gap,
all-time error propagation, passive endpoints, and the explicit finite
tensor count. These steps require no orthogonalization of the inputs
and do not replace the trainable hidden layers.

The unconditional order-two/three result supplies an explicit
\(7300Y^3(m/\gamma)^3\) upper bound on the full sphere and all physical
times, with no additional width-dependent label restriction. Its bound
is fixed as \(n\) grows, so it does not supply the requested dense
variability accuracy or any sufficient growing order.

The remaining scientific bridge is the uniform observable estimate
(6), or a weaker collective ordered-tail estimate strong enough to
replace it. The maintained physical-time analytic strip has a shrinking
width and does not establish this bridge. Equations (16)--(19) show why
the most direct neuronwise complex-control-strip argument cannot repair
it with a fixed label allowance.

Consequently, there is no unconditional \(n^{-1/2}\)-scale upper theorem
for this tanh hierarchy in this note. Replacing \(R\) in (6)--(9) by a
quantity tending to zero and then imposing \(Y/\alpha<R\) would shrink
the labels with width, contrary to the assigned problem. Divergence of
the NTH output series, a Gevrey law for its averaged coefficients, and
a lower bound on prediction error are also **not proved** by the
coordinate calculation. Those would require controlling the normalized
observable and its cancellations, rather than its largest neuron.

Author check: the factor \(1/m\), the two mobility factors \(1/n\) in
(2), the loss's factor two relative to the maintained chapter, the
ordered-integral orientation, the moving-state remainder, and the
conditional Gaussian covariance in (17) were rederived directly. The
order-two bootstrap and readout-projection comparison were developed
from the supervisor's proposed route; their constants and singular-value
normalizations were rederived here. No
numerical experiment was run. The result awaits the supervisor's
mathematical cross-check; it is not marked internally checked.

Deterministic arithmetic check on 2026-10-10:

~~~sh
awk 'BEGIN { print 1/sqrt(2)-584/4096; print 8+8/4096; print 3504+2664*sqrt(2); }'
~~~

The outputs were \(0.564529>1/2\), \(8.00195<9\), and
\(7271.46<7300\), respectively. The displayed exact expressions,
not these rounded values, give the margins used in the proof.
