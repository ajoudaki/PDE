# Polylogarithmic Legendre memory without freezing any layer

Date: 2026-10-10. Internally checked result; see `NO_FREEZE_CHECK.md`.
The fresh check reconstructs the new tail and its assembly with the existing
growing-horizon prefix theorem; it does not re-certify that theorem's full
imported probabilistic source proof. This is not promoted book material.
This note replaces only the readout-only continuation of the online,
prefix-free physical-time construction in `OBLIVIOUS_WINDOWS.md`.
It is not a theorem about the unchanged single-block residual-clock
method. Inputs are that complete note and the current paper's setup,
fitting, source, and Legendre projection interfaces. The new deterministic
tail lemma below is proved directly; it does not import a zero-readout
initialization theorem at a nonzero-readout restart.

## Result and qualification

Keep the original admissible activations (including unbounded values),
fixed depth, general sphere data, positive feature-Gram gap, fixed
positive label RMS \(Y\), and original small-label condition. For each
fixed admissible problem, eventually at each fixed confidence, the
modified online Legendre construction below has

\[
 q=O\bigl((\log(en))^{5/2}\bigr),
 \qquad
 \sup_{t\in[0,\infty],\ \|x\|=\sqrt d}
     |f_{\rm Leg}(t,x)-f_n(t,x)|\le\frac Yn.           \tag{1}
\]

Every physical layer remains active in the evolution equations after the
memory rollover; particular velocities may of course vanish naturally.
There is no phase of readout-only training, no dense rollout or jet
compiler, and no projection onto data-adapted response directions.
The algorithm is a hybrid, online memory method with one rollover,
not one unchanged globally smooth single-block ODE. The rollover can
be triggered by the current training residual rather than a prescribed
training time. The degree and qualification parameters remain fixed
before training; there is no rank search or future-trajectory input.

Counting archived learned factors as well as active factors, retained
learned storage is

\[
 n(d+1)+2(L-1)mn(q+1)+O(1)=n^{1+o(1)}.               \tag{2}
\]

Initialized mixers still cost \((L-1)n^2\) additional fixed entries.
Data, activation evaluators, transient scratch and numerical precision
use the same conventions as the original result. No practical runtime,
Euler step-size, or subquadratic total-storage guarantee is asserted.

## 1. Common network and the first memory block

Use \(v=x/\sqrt d\),

\[
 z^{(1)}=W^{(1)}v,\quad z^{(j)}=W^{(j)}h^{(j-1)},\quad
 h^{(j)}=\phi_j(z^{(j)}),\quad f=w^\top h^{(L)}/n,
 \quad r_a=f(x_a)-y_a,\quad \rho=\|r\|_2/\sqrt m.
\]

The residual-free responses are
\(\delta_a^{(L)}=\phi_L'(z_a^{(L)})\odot w\) and
\(\delta_a^{(j)}=\phi_j'(z_a^{(j)})\odot
 W^{(j+1)\top}\delta_a^{(j+1)}\).
The loss is \(m^{-1}\sum_a r_a^2\), with block mobilities
\((n,1,\ldots,1,n)\). The initial matrices and zero readout are exactly
the canonical Gaussian initialization of the paper.

Before rollover use the single-interval, zero-prefix physical-time
construction at the end of `OBLIVIOUS_WINDOWS.md`. Explicitly, for
\(t>0\), each sample, interface and \(0\le j<q\) has moments

\[
 \begin{aligned}
 \dot{\bar h}_{a,j}
 &=h_a-\frac1t\left(j\bar h_{a,j}
                      +\sum_{i<j}(2i+1)\bar h_{a,i}\right),\\
 \dot{\bar\delta}_{a,j}
 &=r_a\delta_a-\frac1t\left(j\bar\delta_{a,j}
                      +\sum_{i<j}(2i+1)\bar\delta_{a,i}\right),\\
 W^{(\ell)}(t)
 &=W^{(\ell)}(0)-\frac2{mnt}
       \sum_{a,j<q}(2j+1)
       \bar\delta_{a,j}^{(\ell)}\bar h_{a,j}^{(\ell-1)\top}.
 \end{aligned}                                               \tag{3}
\]

The first layer and readout always obey

\[
 \dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,
 \qquad \dot w=-\frac2m\sum_a r_a h_a^{(L)}.            \tag{4}
\]

All first-block moments start at zero. At \(t=0\), the regular branch
is defined by the moment integrals
\(t\int_0^1P_j(2u-1)h_a(tu)\,du\) and
\(t\int_0^1P_j(2u-1)r_a(tu)\delta_a(tu)\,du\).
The complete Volterra contraction and uniqueness proof in the cited
note applies unchanged. No finite positive warmup step is required by
the mathematical definition.

For precision the inherited prescribed order is

\[
 \begin{split}
 q=\Big\lceil16\log(en)\max\big\{1,
 32\beta^{30L}Y^2(m/\gamma)^2\sqrt{d+3}
                         [\log(en)]^{3/2}\big\}\Big\rceil,\\
 T=32(m/\gamma)\log(en).
 \end{split}                                                \tag{5}
\]

The already proved finite-stage conclusion is a mobility-parameter
discrepancy \(n^{-16+o(1)}\), uniformly on \([0,T]\), with a
whole-sphere output discrepancy of the same order. It is a theorem on
this particular growing horizon, obtained from the explicit source
rectangle and signed quadratic-defect bootstrap, not an application of
the separate fixed-horizon fifth-power estimate at \(T=T(n)\).
The dense residual at this time is at most \(Y(en)^{-16}\).
These estimates are eventual at fixed positive \(Y\) and fixed other
problem parameters.

Define the rollover time to be the first time that

\[
 \rho(t)\le Y/n^2.                                     \tag{6}
\]

For \(n>1\) it is not time zero. The finite-stage result and continuity
ensure that it occurs by \(T\), for sufficiently large width.
Denote the realized time by \(t_*\). All finite-stage estimates hold
up to it. Equivalently one may use the deterministic time \(T\),
which removes the data-dependent stopping decision and gives an even
smaller initial tail residual. The proof below covers both choices.

## 2. Rollover: archive the past, continue every layer

At \(t_*\), retain the first block's moment arrays and its interval
length. They represent

\[
 W_*^{(\ell)}=W^{(\ell)}(0)-\frac2{mnt_*}
       \sum_{a,j<q}(2j+1)
       \bar\delta_{a,j}^{(\ell)}(t_*)
       \bar h_{a,j}^{(\ell-1)}(t_*)^\top.              \tag{7}
\]

This is a formula for applying a baseline matrix, not an additional
stored dense matrix. Products with \(W_*^{(\ell)}\) use the original
fixed mixer and these retained factors.

Allocate a fresh order-one block for each sample and hidden interface.
In this section bars refer only to these new vectors; archived vectors
in (7) are distinguished by their displayed argument \(t_*\). Set

\[
 \tau(t_*)=1,\qquad
 \bar h_a^{(\ell-1)}(t_*)=h_a^{(\ell-1)}(t_*),\qquad
 \bar\delta_a^{(\ell)}(t_*)=0.
\]

For all later physical times evolve

\[
 \begin{aligned}
 \dot\tau&=\rho,&
 \dot{\bar h}_a^{(\ell-1)}&=\rho h_a^{(\ell-1)},&
 \dot{\bar\delta}_a^{(\ell)}&=r_a\delta_a^{(\ell)},\\
 W^{(\ell)}&=W_*^{(\ell)}-
       \frac2{mn\tau}\sum_a
       \bar\delta_a^{(\ell)}\bar h_a^{(\ell-1)\top}.
 \end{aligned}                                               \tag{8}
\]

Equation (4) remains in force. All current responses are evaluated at
the reconstructed current weights. Nothing uses later dense weights,
future outputs, or an independently fitted response subspace.

This is the original order-one residual-clock memory rule, restarted
from a nonzero readout and a trained baseline. At zero residual all its
velocities vanish; no implemented equation divides by \(\rho\).
At the rollover the represented weights are continuous, and the new
hidden velocities equal their ordinary dense-gradient expressions,
because \(\bar h_a/\tau=h_a\) and \(\bar\delta_a=0\).
There is no imposed zero hidden velocity afterward.

## 3. Deterministic stable tail lemma

The following statement is independent of the preceding approximation
theorem. Suppose a starting network has

\[
 \max\left\{\|W^{(1)}\|_{\rm op}/\sqrt n,
       \max_{2\le j\le L}\|W^{(j)}\|_{\rm op},
       \|w\|_2/\sqrt n\right\}\le B,
 \qquad
 \frac{\mathsf H^\top\mathsf H}{mn}\succeq\lambda_0 I_m,
                                                               \tag{9}
\]

where \(\mathsf H\) contains the top-layer training features. Assume
\(|\phi_j(z)|\le b+s|z|\) and \(|\phi_j'(z)|\le s\) on the real
line, with \(s\ge1\), and take \(B\ge1\), \(b\ge0\). For well-posedness
assume that the activations are continuously differentiable with locally
Lipschitz derivatives, as is true of the original analytic activation
class.
There are explicit positive constants below, depending only on
\(B,b,s,L,\lambda_0\), such that if the starting residual RMS is
sufficiently small, (4), (8) have a global fitted solution and

\[
 \rho(t)\le\rho(t_*)e^{-\lambda_0(t-t_*)/4},\qquad
 \int_{t_*}^{\infty}\|\dot\theta(t)\|_{\rm blocks}\,dt
       \le\frac{4C_v}{\lambda_0}\rho(t_*).             \tag{10}
\]

Here \(\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)\),
and \(\|\cdot\|_{\rm blocks}\) is the sum of its Euclidean/Frobenius
block norms. No constant in this lemma depends on \(n,m,d\) separately
from the displayed normalized gap and starting bounds. It does not
require bounded activation values, a zero starting readout, or a
Gaussian distribution at the restart.

### Explicit tube constants

All notation in this paragraph is private to the lemma. In the tube of
block-distance at most one from the starting network, operators and
readout RMS are at most \(B+1\). Define

\[
 \begin{gathered}
 H_0=1,\quad H_j=b+s(B+1)H_{j-1},\quad
 H=\max_{0\le j\le L}H_j,\\
 D=(B+1)s\max\{1,s(B+1)\}^{L-1},\\
 F_1=s,\quad F_j=s[H+(B+1)F_{j-1}],\quad
 F=\max\{1,F_1,\ldots,F_L\},\\
 J=H+D+(L-1)DH,\\
 C_v=2J+4(L-1)DF,\qquad
 C_E=8\max\{1,L-1\}DF,\qquad C_r=DH C_E,\\
 \eta=\min\left\{1,\frac{\sqrt{\lambda_0}}{2F},
                         \frac{\lambda_0}{4C_r}\right\},\qquad
 \varepsilon_*=
       \frac{\lambda_0}{8}\min\{1,\eta/C_v\}.
 \end{gathered}                                            \tag{11}
\]

It suffices that \(\rho(t_*)\le\varepsilon_*\). These recurrences
make every constant independent of width. They use only real forward
and backward RMS bounds and feature Lipschitz estimates; no coordinate
maximum of a backpropagated field and no Hessian estimate is needed.

Indeed forward recursion gives \(\|h_a^{(j)}\|_2/\sqrt n\le H\)
at every sphere input, and backward recursion gives
\(\|\delta_a^{(j)}\|_2/\sqrt n\le D\). Comparing a tube state
with the starting state by layer subtraction gives

\[
 \frac{\|h^{(j)}(\theta,v)-h^{(j)}(\theta_*,v)\|_2}{\sqrt n}
 \le F\|\theta-\theta_*\|_{\rm blocks}.              \tag{12}
\]

For the first layer use the Frobenius difference divided by \(\sqrt n\).
For a later layer, its changed mixer acts on a starting feature bounded
by \(H\); the unchanged current mixer has operator norm at most \(B+1\).
This is exactly the recurrence in (11). The prediction gradient blocks
are bounded respectively by \(D,DH,H\), so \(J\) also bounds the
whole-sphere prediction Lipschitz constant along the tube's line
segments, and the ordinary gradient-flow block speed is at most
\(2J\rho\).

### Exact defect and length bootstrap

Put \(A(t)=\int_{t_*}^t\rho(u)\,du\), so \(\tau=1+A\), and
let \(V(t)=\int_{t_*}^t\|\dot\theta(u)\|_{\rm blocks}\,du\)
be the actual accumulated parameter length. Stop provisionally while
\(A\le1\) and \(V\le\eta\). The averaged forward memory is

\[
 \frac{\bar h_a(t)}{\tau(t)}
 =\frac{h_a(t_*)+\int_{t_*}^t\rho(u)h_a(u)\,du}{1+A(t)}.
                                                               \tag{13}
\]

It is a convex average of past features, so its RMS is at most \(H\).
Using (12) for current and past features gives, for every sample,

\[
 \frac{\|h_a(t)-\bar h_a(t)/\tau(t)\|_2}{\sqrt n}
 \le2F V(t),\qquad
 \left(\frac1{mn}\sum_a\|\bar\delta_a(t)\|_2^2\right)^{1/2}
 \le D A(t).                                             \tag{14}
\]

The latter inequality is Minkowski followed by
\((m^{-1}\sum_a r_a^2)^{1/2}=\rho\); it loses no factor of \(m\).

Differentiate (8), using
\(\partial_t(\bar h_a/\tau)=
(\rho/\tau)(h_a-\bar h_a/\tau)\). The exact defect from ordinary
gradient flow is

\[
 \mathcal E_\ell
 =\frac2{mn}\sum_a
       \left(r_a\delta_a^{(\ell)}-
                     \frac\rho\tau\bar\delta_a^{(\ell)}\right)
       \left(h_a^{(\ell-1)}-
                     \bar h_a^{(\ell-1)}/\tau\right)^\top.
                                                               \tag{15}
\]

Sample Cauchy--Schwarz and (14) imply

\[
 \sum_{\ell=2}^L\|\mathcal E_\ell\|_F
 \le4(L-1)DF(1+A)\rho V
 \le C_E\rho V.                                         \tag{16}
\]

For a length bound, it is slightly sharper to use the differentiated
reconstruction directly, with \(\bar h/\tau\) in its first term.
Together with (4), this gives

\[
 \|\dot\theta\|_{\rm blocks}
 \le 2J\rho+4(L-1)DF A\rho V
 \le C_v\rho,
 \qquad V(t)\le C_v A(t).                               \tag{17}
\]

### Coercivity, fitting and global continuation

Equation (12) bounds the operator norm of
\((\mathsf H(t)-\mathsf H(t_*))/\sqrt{mn}\) by \(FV\).
Since \(V\le\sqrt{\lambda_0}/(2F)\), (9) preserves the current
readout feature-Gram lower bound \(\lambda_0/4\).
The full tangent Gram includes this positive semidefinite readout
contribution. Thus ordinary gradient flow contracts the residual norm
at rate at least \(\lambda_0/2\).

Each hidden output-gradient block has Frobenius norm at most \(DH\).
The defect contribution to prediction velocity therefore has sample
RMS at most \(DH\sum_\ell\|\mathcal E_\ell\|_F\), bounded by
\(C_r V\rho\). For \(\rho>0\), exact residual differentiation now
gives

\[
 \dot\rho\le-\frac{\lambda_0}{2}\rho+C_rV\rho
          \le-\frac{\lambda_0}{4}\rho.                 \tag{18}
\]

At zero residual all stored-state velocities vanish, so stationary
continuation gives the same bound. Integration of (18) and (17) yields

\[
 A(t)\le\frac{4\rho(t_*)}{\lambda_0}\le\frac12,
 \qquad
 V(t)\le\frac{4C_v\rho(t_*)}{\lambda_0}\le\frac\eta2.
                                                               \tag{19}
\]

Both provisional stops improve strictly. The finite-dimensional vector
field is locally Lipschitz for \(\tau\ge1\); the activation class is
smooth and the residual norm is Lipschitz, with no division by that
norm. Bounded physical variables and (13)--(14) bound every memory.
Therefore the solution exists globally. Equations (18)--(19) prove (10),
physical convergence and exact fitting in the limit. The moments also
converge, since their speeds have integrable bounds \(C\rho\).

Finally the whole-sphere output bound is

\[
 \sup_{t\in[t_*,\infty],\ \|x\|=\sqrt d}
 |f(t,x)-f(t_*,x)|
 \le\frac{4JC_v}{\lambda_0}\rho(t_*).                 \tag{20}
\]

The proof permits all layers to move. For \(L=1\) the hidden-memory
sum is empty and the same argument simply bounds the ordinary flow.

## 4. Assembly with the online first stage

The finite-stage parameter estimate, not just prediction accuracy,
transfers the dense real operator/readout bounds and feature-Gram gap
to the switching state. Eventually these bounds hold uniformly up to
\(T\) with some fixed \(B\), and with
\(\lambda_0=\gamma/(8m)\). This follows from the dense least singular
value lower bound \(\sqrt{\gamma/m}/2\) for the normalized top-feature
matrix and its \(O(n^{-16+o(1)})\) perturbation. For example it suffices
that the perturbation be less than
\((1/2-1/\sqrt8)\sqrt{\gamma/m}\).

All constants in (11) are then fixed as width grows. At the residual
trigger, \(\rho(t_*)=Y/n^2\) by continuity, so the lemma's small-tail
condition holds eventually. It is not a new restriction on the initial
dataset or labels. It only enlarges the already unquantified sufficient
width threshold. With a deterministic rollover at \(T\), use instead
\(\rho(T)\le Y(en)^{-16}+n^{-16+o(1)}\).

At the trigger the dense residual is at most
\(Y/n^2+O(n^{-16+o(1)})\), by first-stage prediction accuracy on
training inputs. The dense flow's all-time tail-length estimate from
its fitting proof implies an output tail bounded by a fixed constant
times this quantity. Combine that estimate with (20) and the discrepancy
at \(t_*\). For all subsequent times, including the fitted endpoints,

\[
 \sup_{\|x\|=\sqrt d}|f_{\rm Leg}(t,x)-f_n(t,x)|
 \le C\bigl(Y/n^2+n^{-16+o(1)}\bigr)\le Y/n          \tag{21}
\]

eventually, since the problem and \(Y>0\) are fixed. Before the trigger
the stronger finite-stage bound holds. This proves (1). Dividing (1)
by the paper's actual dense-variability lower bound
\(cY\sqrt\gamma/[\sqrt n\log(en)^{5/2}]\) gives a ratio tending
to zero in probability, with the usual arbitrary fixed-confidence
qualification. No upper-variability surrogate is substituted.

There are \(2(L-1)mnq\) first-block learned entries and
\(2(L-1)mn\) fresh tail entries. The first layer/readout still use
\(n(d+1)\) entries. Retain the first interval length and tail clock,
plus one discrete phase flag; these cost \(O(1)\). Thus (2) includes
everything retained from training, even though the first-block factors
stop changing. The baseline in (7) is never stored as a learned dense
matrix. Equation (5) also retains the earlier explicit sample, gap,
dimension, label, activation and depth dependence; no use of the label
cap simplifies those factors.

## What is and is not repaired

The old residual-clock method already slows down, converges and fits;
its obstruction concerned sufficiently accurate approximation of dense
training, not a failure to stop moving. Exponential fitting generally
does not reach zero in finite physical time, and reaching an
\(n^{-1/2}\)-scale tail requires a horizon growing like \(\log n\).

This modification removes the imposed freezing of physical layers.
It retains a one-time change in the memory representation: detailed
memory is archived, while a small live block continues learning all
layers. It does not prove polylogarithmic order for the original
single-block residual-clock equations, or for a completely switch-free
smooth memory algorithm. A scalar clock change alone has not been
proved to supply either stronger assertion.
