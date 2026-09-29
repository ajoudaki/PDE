# Arbitrary-label state bounds for the actual block response closure

This note proves global finite-width existence and bounds on every finite
physical-time interval for the unmodified old-clock response closure. The
constants in the state bounds can be chosen independently of width n,
block size k and moment order q, with fixed confidence under Gaussian block
initialization. This is an a priori state theorem, not a width convergence,
fitting or all-time bounded-error theorem.

Scientific inputs are the explicit model below and elementary derivations.
No other study is a proof dependency.

## Model

Fix L hidden layers, m training inputs, n=Bk neurons per hidden layer, and
label RMS Y=||y||_2/sqrt(m). The first preactivation is W^(1)x/sqrt(d),
subsequent ones are W^(l)h^(l-1), and f=w^T h^(L)/n. Residuals are r=f-y.
The first weights and readout follow canonical gradient flow:

\[
\dot w=-\frac2m\sum_a r_a h_a^{(L)},\qquad
\dot W^{(1)}=-\frac2m\sum_a r_a\delta_a^{(1)}x_a^T/\sqrt d.
\]

Backpropagation uses the actual reconstructed matrices:
\(\delta_a^{(L)}=w\odot\phi_L'(z_a^{(L)})\),
\(\delta_a^{(l-1)}=\phi_{l-1}'(z_a^{(l-1)})\odot
(W^{(l)})^T\delta_a^{(l)}\).

At each hidden layer l>=2, let G_l be its fixed initialized matrix. Its
bth diagonal block G_l,b has size k; all off-block initialized entries
are zero. For each sample a and j=0,...,q-1 retain forward and backward
moment vectors B_l,a,j and C_l,a,j. Write alpha_j=2j+1 and

\[
\rho=\|r\|_2/\sqrt m,\qquad \dot\tau=\rho,\quad\tau(0)=1,
\qquad
(Tv)_j=jv_j+\sum_{i<j}\alpha_i v_i.
\]

The moment equations and reconstruction are

\[
\dot B_{l,a}=\rho h_a^{(l-1)}\mathbf1-(\rho/\tau)TB_{l,a},
\quad
\dot C_{l,a}=r_a\delta_a^{(l)}\mathbf1-(\rho/\tau)TC_{l,a},
\]
\[
W^{(l)}=G_l+A_l,\qquad
A_l=-\frac2{nm\tau}\sum_{a,j}\alpha_j C_{l,a,j}B_{l,a,j}^T.
\tag{1}
\]

Initially B_l,a,0=h_a^(l-1)(0); all other B and all C vanish. The
readout is exactly zero initially. All responses on the right are evaluated
on this autonomous reconstructed network. Its learned matrices are globally
connected even though initialization is block diagonal.

Assume bounded smooth activations with globally bounded first derivative,
and locally Lipschitz first derivative. Write

\[
M=\max(1,\max_l\|\phi_l\|_\infty),\qquad
D=\max(1,\max_l\|\phi_l'\|_\infty),\qquad
R_x=\max_a\|x_a\|_2/\sqrt d.
\]

The local vector field is locally Lipschitz, including at rho=0, since
the Euclidean norm is Lipschitz and tau stays at least one. Thus a unique
local solution exists and continues unless its finite state escapes every
bounded set. These conclusions also follow by the ordinary Picard iteration
and continuation argument for locally Lipschitz finite-dimensional ODEs.

## Exact moment energy bounds

On any interval of local existence set A(t)=int_0^t rho(s)ds, so tau=1+A.
The shifted Legendre moment identities are exact for the closure's own
histories. In the activity coordinate u, the forward history equals its
initial value on [0,1] and then the current h; the backward history is zero
on [0,1] and then equals (r_a/rho)delta_a. Where rho=0 all sources vanish.
These histories produce the equations (1) by differentiation, so uniqueness
of their linear moment equations identifies them with the stored moments.

For the shifted Legendre polynomials p_j on [0,1],
int_0^1 p_i p_j=1_{i=j}/alpha_j. The usual orthogonal projection identity
(or expansion of its nonnegative squared residual) therefore gives,
coordinatewise, on [0,tau],

\[
\sum_{j<q}\alpha_j B_{l,a,j,i}(t)^2\leq M^2\tau(t)^2.
\tag{2}
\]

For backward moments the same identity gives

\[
\sum_{j<q}\alpha_j\frac{\|C_{l,a,j}(t)\|_2^2}{n}
\leq\tau(t)\int_0^t
 \frac{r_a(s)^2}{\rho(s)}\frac{\|\delta_a^{(l)}(s)\|_2^2}{n}ds.
\tag{3}
\]

The integrand is defined as zero when rho=0. Since r_a^2<=m rho^2,
if D_l^*(t)=max_a sup_{s<=t}||delta_a^(l)(s)||_2/sqrt(n), then

\[
\sum_{j<q}\alpha_j\frac{\|C_{l,a,j}(t)\|_2^2}{n}
\leq m\tau(t)^2(D_l^*(t))^2.
\tag{4}
\]

All these bounds hold for every q, without a bound on the norm of the
triangular moment generator. In particular they do not incur its large-q
coordinate condition number.

## Readout and clock: no small-label hypothesis

Let W_*(t)=max_i|w_i(t)|. Bounded activations give

\[
\rho(t)\leq Y+M W_*(t),\qquad
D^+W_*(t)\leq2M\rho(t).
\]

Integrating the scalar comparison equation, with W_*(0)=0, proves on
every finite interval [0,T]

\[
W_*(t)\leq W_T:=\frac YM(e^{2M^2T}-1),\qquad
\rho(t)\leq Ye^{2M^2t},
\quad
\tau(t)\leq\tau_T:=1+\frac{Y(e^{2M^2T}-1)}{2M^2}.
\tag{5}
\]

These hold for any finite Y, n, k and q. They are growth bounds rather
than loss-decay statements. On any interval with activity budget A<=A_*,
one can instead use the sharper elementary bound W_*<=2M A_* and
tau<=1+A_*, irrespective of its physical duration.

## Backward signals: average block norms suffice

Define

\[
S_b=\max_{2\leq l\leq L}\|G_{l,b}\|_{\mathrm{op}},\qquad
H=\frac1B\sum_{b=1}^B(1+S_b)^{2(L-1)}.
\tag{6}
\]

Assume L>=2; the case L=1 has no hidden matrices and is immediate. Let
d_l,b(t)=max_a||delta_l,a restricted to block b||_2/sqrt(k).

First, (2),(4) bound the learned backward action coordinatewise:

\[
|(A_l^T\delta_a^{(l)})_i|
\leq 2M\sqrt m\,\tau_T(D_l^*(T))^2.
\tag{7}
\]

To verify (7), expand (1). Cauchy--Schwarz in j bounds the factors
B_j,i by M tau and the contractions
\(C_j^T\delta/n\) by
\((\sum_j\alpha_j\|C_j\|_2^2/n)^{1/2}\|\delta\|_2/\sqrt n\).
The factor tau cancels its denominator; (4) and the average over m samples
give (7). This proof never replaces a block average by the largest block.

Define constants recursively down the layers:

\[
c_L=D W_T,\qquad
c_{l-1}=D\left(c_l+2M\sqrt m\,\tau_T c_l^2 H\right)
\quad(l=L,L-1,\ldots,2).
\tag{8}
\]

Then the following bounds hold throughout [0,T]:

\[
d_{l,b}(t)\leq c_l(1+S_b)^{L-l},\qquad
D_l^*(T)\leq c_l\sqrt H.
\tag{9}
\]

The top bound follows from |delta_L,i|<=D W_T. If (9) holds at l,
then averaging its square over blocks bounds D_l^* by c_l sqrt(H).
Backward propagation, (7), and ||G_l,b^T delta||_2<=S_b||delta||_2
give

\[
d_{l-1,b}(t)\leq D\left[S_b c_l(1+S_b)^{L-l}
             +2M\sqrt m\,\tau_T c_l^2H\right]
\leq c_{l-1}(1+S_b)^{L-l+1}.
\]

This completes the downward induction. Constants may grow rapidly with
depth and label size; depth is fixed, and no uniform-in-depth claim is made.

The same coefficient Cauchy--Schwarz estimate gives

\[
\|A_l(t)\|_F\leq2M\sqrt m\,\tau_T c_l\sqrt H,
\tag{10}
\]

independent of n,k,q apart from H. For the first-layer weights,

\[
\frac{\|W_b^{(1)}(t)-W_b^{(1)}(0)\|_F}{\sqrt k}
\leq2R_x(\tau_T-1)c_1(1+S_b)^{L-1}.
\tag{11}
\]

Here sum_a |r_a|/m<=rho bounds the first-layer equation before integration.

## Consequences for existence and Gaussian initialization

For any fixed finite initialized matrices, H is finite. Equations
(2)--(11) bound every component of the finite q-state on each finite
interval. The ODE therefore has no finite-time escape and extends uniquely
to all physical times. This is global existence, not an all-time bounded
trajectory or convergence-to-zero-loss statement.

For actual Gaussian blocks with entries N(0,1/k), all moments of S_b are
bounded uniformly in k. Here is an elementary verification. A 1/4-net of
the unit sphere in R^k has at most 9^k points, by the disjoint-ball volume
argument. Approximating both unit vectors in the bilinear definition of
the operator norm gives ||G||op<=2 max_{u,v in net}|u^T Gv|. Each such
bilinear form is N(0,1/k); its Chernoff bound is
P{|u^TGv|>z}<=2exp(-k z^2/2). A union bound yields

\[
\mathbb P\{\|G\|_{\mathrm{op}}>t\}
\leq2\,9^{2k}e^{-kt^2/8}
\leq2e^{-kt^2/16}\quad(t^2\geq32\log9).
\]

A union over the fixed L-1 layers and integration of this tail prove
\(\sup_k\mathbb E(1+S_b)^p<\infty\) for every fixed p.
Consequently E H<=C_L uniformly in B,k. With probability at least 1-p,
H<=C_L/p, by Markov's inequality. Inserting this deterministic bound in
(8)--(11) gives finite-time state bounds depending only on
T,Y,L,m,activation bounds,R_x and p, uniformly in n,k,q. All finite moments
of these upper bounds are also uniform in n,k,q: for r>=1, convexity gives
E H^r<=E(1+S_b)^{2r(L-1)}, and the c_l are polynomials in H.

Gaussian first-layer initial weights have the usual finite normalized
Frobenius moments, so (11) also bounds their total normalized state after
adding initialization. No truncation of Gaussian blocks or modified
optimization is used in this theorem.

## What this resolves, and what it does not

The actual closure is well defined for all finite times for arbitrary
fixed labels. On finite intervals, Gaussian block outliers can be handled
through population moments, with constants uniform in n,k,q. The learned
operator has bounded Frobenius norm there without forming a dense matrix.

This does not prove propagation of sampling error: bounded states and a
bounded learned operator are not a bound on the derivative of the response
map. In particular, Gaussian-block-dependent Lipschitz constants and the
clock dependence of high-order moments must still be controlled. Nor does
(5) prove bounded total activity; its upper bound grows exponentially in T.
An all-time approximation theorem needs a fitting or stability argument
beyond these state estimates.
