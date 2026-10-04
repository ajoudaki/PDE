# Fixed-order q=2 and q=3 terminal scalarization

Independent algebraic check, 2026-09-30, scoped agent
`/root/scalar_aggregate`.

**Conclusion: PASS for the exact finite-width formulas and conditional
fixed-q transfer below.** The same terminal scalar method applies to each
fixed positive integer q, including q=2 and q=3. Its coefficients must be
computed from that order's full reconstructed network. There is no empirical
terminal certificate, width-uniform bound, initialized fitting theorem, or
claim that a higher order necessarily improves a particular trajectory.

Scientific inputs read completely within the assigned scope:

* `paper/main.tex`, lines 311--380 and 1098--1155. Full file SHA256
  `fa44deda090a456640b64080767511003dc8bc385790ccc49fd039c931a67605`.
* `TERMINAL_SCALAR_THEOREM.md`, SHA256
  `fbb93521867a03c8a01ebe8c29f88d04b643cf3d6fa4af53151e13ddf4c6bde5`.
* `TERMINAL_SCALAR_CHECK.md`, SHA256
  `03768e21dc1214e08bfe50a68a69d13f9f65059810a5c6560e124cb023079a4e`.
* After freezing the independent derivation, the complete root candidate
  `HIGHER_ORDER_SCALAR.md`, SHA256
  `848e0903b4a42aafa5c6b24c4e83be4c59531c5b77efa4147113e97e7c17cfe2`,
  was additionally authorized and read for comparison.

No other study, higher-order implementation, empirical result, or external
scientific source was read. Required skills and repository process
instructions were already available in this context. The only computation
was a bounded exact-integer check of the mode identity described below; no
training or simulation was run. Only this report was written.

## 1. Normalized mode equations

Fix finite width n, training sample count m, and memory order q. Use the
two-hidden-layer tanh model and physical clock from the checked terminal
theorem. Write

\[
 \langle u,v\rangle_n=u^Tv/n,\quad I_{ab}=x_a^Tx_b/d,
 \quad r_a=f_a-y_a,\quad \rho=\|r\|/\sqrt m,\quad\dot\tau=\rho.
\]

For each example a and mode k=0,...,q-1 define

\[
 K_{a,k}=\bar h_{a,k}/\tau,\qquad V_{a,k}=-2\bar\delta_{a,k},
 \qquad c_k=2k+1.
\]

In particular, **V is not divided by tau**. Let `K_a,V_a` be n-by-q matrices
whose columns are these mode vectors. Define q-by-q matrices

\[
 \mathsf D=\operatorname{diag}(c_0,\ldots,c_{q-1}),\qquad
 T_{kj}=\begin{cases}
 k,&j=k,\\
 c_j,&j<k,\\
 0,&j>k.
 \end{cases}
\]

The manuscript's raw moment equations and the quotient rule give exactly

\[
 \dot K_{a,k}=\frac\rho\tau
 \left[h_a-(k+1)K_{a,k}-\sum_{j<k}c_jK_{a,j}\right],
 \tag{1}
\]
\[
 \dot V_{a,k}=-2r_ad_a-\frac\rho\tau
 \left[kV_{a,k}+\sum_{j<k}c_jV_{a,j}\right].
 \tag{2}
\]

Here `d_a=w odot (1-g_a^2)` is the current second-layer backward response.
The forcing in (2) occurs in **every** mode, since every shifted Legendre
polynomial equals one at its right endpoint. The extra `+1` in (1) is due to
normalizing the forward moment by tau; it is absent from (2).

Equivalently, with `1` the q-vector of ones,

\[
 \dot K_a=\frac\rho\tau[h_a1^T-K_a(T+I_q)^T],\qquad
 \dot V_a=-2r_ad_a1^T-\frac\rho\tau V_aT^T.
 \tag{3}
\]

The reconstructed middle matrix is

\[
 B=W_0+\frac1{mn}\sum_a V_a\mathsf D K_a^T
   =W_0+\frac1{mn}\sum_{a,k}c_kV_{a,k}K_{a,k}^T.
 \tag{4}
\]

Current features and true backpropagation are

\[
 h_a=\tanh(Ax_a/\sqrt d),\quad g_a=\tanh(Bh_a),\quad f_a=w^Tg_a/n,
\]
\[
 d_a=w\odot(1-g_a^2),\qquad
 \ell_a=(1-h_a^2)\odot B^Td_a.
\]

The first-layer/readout equations remain

\[
 \dot A=-\frac2m\sum_a r_a\ell_ax_a^T/\sqrt d,
 \qquad \dot w=-\frac2m\sum_a r_ag_a.
 \tag{5}
\]

Initialization is `tau=1`, `K_{a,0}=h_a(0)`, all higher K modes zero, all V
modes zero, and stored readout zero. Equation (4) then gives exactly `B=W0`.
Equations (1)--(2) give zero initial velocity for every K and V mode: the
`j=0` term cancels the forward forcing for every higher mode, and initially
`d=0`. No artificial initial higher-mode excitation is required.

## 2. Exact cancellation of mode dilation

The candidate identity is correct:

\[
 T^T\mathsf D+\mathsf D T+\mathsf D=cc^T.
 \tag{6}
\]

For a diagonal entry k, the left side is `(2k+1)c_k=c_k^2`. If k>j, its
only nonzero off-diagonal contribution is
`(mathsf D T)_{kj}=c_k c_j`. If k<j, that contribution instead comes from
`(T^T mathsf D)_{kj}=c_j c_k`. This proves every matrix entry for every q.

Define the mode sums evaluated at the polynomial endpoint,

\[
 K_a^*=K_ac=\sum_kc_kK_{a,k},\qquad
 V_a^*=V_ac=\sum_kc_kV_{a,k}.
 \tag{7}
\]

Differentiate (4), insert (3), and keep matrix order explicit:

\[
\begin{aligned}
 \dot B={}&-\frac2{mn}\sum_a r_ad_a(K_a c)^T\\
 &+\frac\rho{mn\tau}\sum_a
 \left[V_ac h_a^T
       -V_a(T^T\mathsf D+\mathsf DT+\mathsf D)K_a^T\right].
\end{aligned}
\]

Thus (6) collapses the entire dilation term to

\[
 \boxed{\dot B=-\frac2{mn}\sum_a r_ad_a(K_a^*)^T
       +\frac\rho{mn\tau}\sum_aV_a^*(h_a-K_a^*)^T.}
 \tag{8}
\]

A separate check uses the manuscript's projection defect. When rho>0, its
backward endpoint is `b_a^*=-V_a^*/(2 tau)` and its forward endpoint is
`h_a^*=K_a^*`. Therefore dense middle-layer velocity plus defect is

\[
 -\frac2{mn}\sum_a r_ad_ah_a^T
 +\frac{2\rho}{mn}\sum_a
 \left(\frac{r_a d_a}{\rho}+\frac{V_a^*}{2\tau}\right)
 (h_a-K_a^*)^T,
\]

which simplifies to (8), with the same sign and tau factor. This second
expression is only a check on rho>0. Equation (8) itself is nonsingular and
valid at rho=0.

Crucially, (8) does **not** replace the reconstructed matrix (4) by
`W0+(mn)^-1 sum_a V_a^*(K_a^*)^T`. That product would introduce cross-mode
terms and would change the network. The rank-mq reconstruction and all q
modes remain necessary in the full closure before handoff.

Nor are the endpoint sums themselves a two-field autonomous replacement.
Summing (1)--(2) gives

\[
 \dot K_a^*=\frac\rho\tau\left[
 q^2h_a-\sum_jc_j\{q^2-j(j+1)\}K_{a,j}\right],
\]
\[
 \dot V_a^*=-2q^2r_ad_a-\frac\rho\tau
 \sum_jc_j\{q^2-j(j+1)-1\}V_{a,j}.
 \tag{9}
\]

These expressions generally require the individual modes. Their coefficients
follow by summing `c_k T_{kj}` over k and using `sum_k c_k=q^2`.

## 3. Training and query scalar coefficients

For a fixed query x, compute `h_x,g_x,d_x,ell_x` with the **full** B in (4),
and put `I_{xa}=x^Tx_a/d`. Exact differentiation of
`f_x=w^Tg_x/n` yields

\[
 \dot f_x=\dot w^Tg_x/n+d_x^T\dot B h_x/n
                +\ell_x^T\dot A x/(n\sqrt d).
\]

Substitution of (5) and (8) gives

\[
 \dot f_x=-\sum_a C^{(q)}(x,a)r_a+\|r\|b^{(q)}(x),
 \tag{10}
\]
\[
 C^{(q)}(x,a)=\frac2m\left[
 \langle g_x,g_a\rangle_n
 +I_{xa}\langle\ell_x,\ell_a\rangle_n
 +\langle d_x,d_a\rangle_n\langle K_a^*,h_x\rangle_n\right],
 \tag{11}
\]
\[
 b^{(q)}(x)=\frac1{m\sqrt m\tau}\sum_a
 \langle d_x,V_a^*\rangle_n\langle h_a-K_a^*,h_x\rangle_n.
 \tag{12}
\]

The factor `sqrt(m)` in (12) comes from converting rho to `||r||/sqrt(m)`.
For training queries `x=x_b`, these coefficients give the exact system

\[
 \dot r=-C^{(q)}(X_q)r+\|r\|b^{(q)}(X_q).
 \tag{13}
\]

The current/endpoint cross term can be nonsymmetric, and the norm-drift term
does not generally vanish. Higher order supplies no algebraic PSD guarantee.
Both coefficient arrays use the same fixed `W0` action and its true transpose
inside (4) and backpropagation. No independent mixer resampling is involved.

For implementation with sample columns, the query-by-training matrix's
third summand is precisely
`(d_query.T @ d_train/n) * (h_query.T @ K_star/n)`.
The query drift is the row sum of
`(d_query.T @ V_star/n) * (h_query.T @ (h_train-K_star)/n)`,
divided by `m*sqrt(m)*tau`. This fixes the cross-Gram orientation.

## 4. q=1, q=2, q=3 and stopping checks

At q=1, `c=(1)`, `T=(0)`, `K^*=K_0`, `V^*=V_0`. Equations (1)--(4),
(8), and (11)--(13) reduce exactly to the checked q=1 theorem, including
`Vdot=-2r d` and `Kdot=(rho/tau)(h-K)`.

For q=2 or q=3, put `alpha=rho/tau`. The explicit mode updates are

\[
\begin{array}{ll}
 \dot K_0=\alpha(h-K_0),&\dot V_0=-2rd,\\
 \dot K_1=\alpha(h-K_0-2K_1),&
 \dot V_1=-2rd-\alpha(V_0+V_1),\\
 \dot K_2=\alpha(h-K_0-3K_1-3K_2),&
 \dot V_2=-2rd-\alpha(V_0+3V_1+2V_2).
\end{array}
 \tag{14}
\]

Use only the first two rows at q=2. The reconstruction weights are `(1,3)`
or `(1,3,5)`, and the endpoint sums use these same weights. These formulas
retain physical time; tau is a state with derivative rho, not the integration
variable.

At r=0, rho=0 and every right-hand side in (1), (2), (5), and the clock
equation vanishes, including the triangular higher-mode terms. Therefore
all full-state coordinates stop, (8) vanishes, and every training/query
prediction stops. This conclusion requires no division by rho and no
assumption that stored higher modes, `V^*`, or `h-K^*` vanish.

## 5. Conditional fixed-q transfer of the terminal theorem

For fixed finite q,n,m,d let
`X_q=(A,w,(K_{a,k},V_{a,k})_{a,k},tau)`. Equations (1), (2), and (5) have
the exact form

\[
 \dot X_q=\sum_a r_aF_a^{(q)}(X_q)+\|r\|F_0^{(q)}(X_q),
 \tag{15}
\]

with smooth coefficient fields on tau>0. Equations (11)--(12) are also
smooth there. The full vector field is locally Lipschitz, including at
r=0; differentiability of the residual norm at zero is not needed.

At a reached handoff let `R=||r_0||`, `C_0=C^(q)(X_0)`, and
`b_0=b^(q)(X_0)`. In a chosen finite-dimensional state norm suppose a closed
ball of radius a about X_0 lies in tau>0 and obeys

\[
 \|\dot X_q\|\le H\|r\|,\qquad
 \|C^{(q)}(X)-C_0\|_{op}+\|b^{(q)}(X)-b_0\|
 \le J\|X-X_0\|.
\]

Define `lambda=lambda_min((C_0+C_0^T)/2)-||b_0||`. Require

\[
 \lambda>0,\qquad \frac{2HR}{\lambda}<a,
 \qquad \frac{2JHR}{\lambda}<\frac\lambda2.
 \tag{16}
\]

The terminal scalar system is unchanged in form:

\[
 \dot{\widehat r}=-C_0\widehat r+\|\widehat r\|b_0,
 \qquad \widehat r(0)=r_0.
 \tag{17}
\]

All assertions and constants of the checked terminal theorem transfer:

\[
 \|r(t)\|\le Re^{-\lambda t/2},\quad
 \|\widehat r(t)\|\le Re^{-\lambda t},
\]
\[
 \sup_{t\ge0}\|r-\widehat r\|\le\frac{JH}{\lambda^2}R^2,
 \quad\sup_{t\ge0}|L-\widehat L|\le\frac{2JH}{m\lambda^2}R^3,
\]
\[
 \sup_{t\ge0}|\tau-\widehat\tau|
 \le\frac{4JH}{\sqrt m\lambda^3}R^2,
 \qquad \dot{\widehat\tau}=\|\widehat r\|/\sqrt m.
 \tag{18}
\]

To verify the transfer, before ball exit write `z=||r||` and
`u=||X-X_0||`. Equation (13) gives `zdot<=-(lambda-Ju)z`.
Stopping also at `Ju=lambda/2` gives
`z<=R exp(-lambda t/2)` and `u<=2HR/lambda`. The strict conditions (16)
exclude both exits. Finite dimension and local Lipschitz continuity then
give all-time continuation inside a compact admissible set. Integrable
speed yields a limiting full state with zero residual.

For the frozen field `T(r)=-C_0r+||r||b_0`, the reverse triangle inequality
gives `(u-v)^T(T(u)-T(v))<=-lambda||u-v||^2`. The perturbing residual source
is bounded by `(2JH/lambda)R^2 exp(-lambda t/2)`. Convolution with
`exp(-lambda t)` yields

\[
 \|r-\widehat r\|
 \le\frac{4JH}{\lambda^2}R^2
 (e^{-\lambda t/2}-e^{-\lambda t}).
\]

Its supremum and integral prove (18), exactly as in the checked q=1 proof.
No step of that proof otherwise uses q=1. The case R=0 is stationary and
all errors are zero.

Each fixed-query output in (10) is a passive observable with coefficient
vector `p_x=-C^(q)(x,:)` and scalar `q_x=b^(q)(x)`. The checked passive-
observable theorem therefore transfers with its stated query-coefficient
Lipschitz bound, giving the same conditional order-R^2 output error. For a
finite query set this is a finite collection of such bounds. A Fourier
representation introduces an additional approximation error that this
argument does not bound.

## 6. Counts, computability and claim boundaries

At fixed q the terminal residual evaluator retains m moving scalars,
`m^2+m` fixed numbers, and costs `O(m^2)` per RHS. Sharing the integrated
residual and its norm for passive queries uses `2m+1` moving scalars:

\[
 \dot U=\widehat r,\quad \dot s=\|\widehat r\|,\quad U(0)=s(0)=0,
 \qquad\widehat f_x=f_x(X_0)-C^{(q)}(x,:)U+b^{(q)}(x)s.
\]

These terminal counts do not grow with q. With the stipulated 64 real odd
Fourier coefficients for each of the m+2 query functions, the additional
fixed count is `64(m+2)`, hence 712 fixed numbers and 17 moving numbers for
m=8. This is a representation count, not a Fourier accuracy guarantee.

Before handoff, the full order-q system still stores `n(d+1)+2nmq+1` moving
numbers and the n-by-n fixed mixer, and its coefficient construction uses
the actual current fields, all retained modes, and the true adjoint. For
d=2 the moving count is `3n+2nmq+1`. Endpoint sums themselves cost
`O(nmq)` to form. No initialization-only scalar method is supplied here.

All constants in (16)--(18) may depend on q,n, the reached state, data,
initialization and the chosen norm. A measured positive endpoint margin
alone does not verify the tube bounds or small-tail inequalities. Neither
the existence of a fitted endpoint nor q-to-dense accuracy follows from
this calculation. Population, width-uniform, and q-to-infinity conclusions
require separate proofs.

## 7. Check record

The decisive identities were proved entrywise and by direct differentiation.
Equation (8) was independently recovered from the permitted manuscript's
projection-defect formula. The q=1 reduction, q=2/q=3 components, true-adjoint
contractions, sqrt(m) clock factor, initialized higher-mode cancellation,
and zero-residual stopping were checked explicitly above.

A bounded Python exact-integer check constructed `c,T` for q=1,...,9 and
verified every entry of (6), plus both weighted column sums in (9). It
exited 0 with:

> Exact-integer mode identity and endpoint derivative coefficients passed
> for q=1,...,9.

This finite check is a sanity check; the general-q proof is (6)'s entrywise
argument. There was no integration, training experiment, empirical fitting
assessment, or model selection. The report establishes the exact formulas
and the stated conditional finite-dimensional theorem transfer only.

## 8. Complete comparison with the frozen root candidate

The independent derivation above was persisted before receiving the root
candidate, at report SHA256
`4b199c7ef25496803b484a34c7f1d430edd2f26d27a2d217154a03edba27449e`.
The subsequent candidate comparison read every scientific line, including
the initialization, finite-mode identity, scalar-query construction, counts,
and scope of the theorem transfer. No implementation or experimental plan
linked from the candidate was opened.

**Candidate verdict: PASS for the stated exact finite-width identities and
conditional fixed-q terminal theorem transfer.** Candidate equations
(1)--(4) agree with report (1)--(5); candidate endpoint identity (7) agrees
with report (8); candidate query coefficients (8)--(10) agree with report
(10)--(12). The triangular matrix orientation, derivative forcing in every
mode, normalized-key `j+1`, unnormalized-value `j`, signs, factors of n and
m, and the conversion from rho to `||r||/sqrt(m)` all agree.

The candidate's unit-prefix initialization correctly places the initial
feature only in mode zero. Its explicit q=2/q=3 additional equations are
correct. The text correctly distinguishes increasing memory order from
appending modes to an already evolved q=1 path, and distinguishes the two
endpoint sums in `Bdot` from the full reconstruction needed to evaluate B.
It also correctly warns that the endpoint sums need not be convex averages
or bounded by the activation range.

The terminal transfer uses exactly the proved hypotheses of the existing
theorem; it does not claim an empirical tube certificate, automatic fitting,
dense approximation, a Fourier approximation guarantee, or constants
uniform in q or width. Its 17-moving/712-fixed count for m=8 is correct for
the stated terminal predictor and does not include the uncompressed
handoff-production phase. No mathematical or scope correction is required
for this frozen candidate.
