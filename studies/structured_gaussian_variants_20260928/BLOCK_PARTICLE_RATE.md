# Block population, finite activity, and the quantitative particle boundary

Frozen independent route, 2026-09-28. Scientific inputs were the assignment,
`docs/index.qmd`, `docs/notation.qmd`, and the exact finite gradient identities
in `docs/01-training-geometry.qmd`. No other study or proof route was read.
The supervisor supplied the prescribed old-clock Legendre moment equations.
This is an internally checked research argument, not established book material.

**Main result.** For the prescribed response-memory closure, a fixed small-label
threshold gives global existence, finite total residual activity, convergence
of the state, and fitting, uniformly in block size and memory order, provided
every initialized block has a fixed operator cap. No endpoint Lebesgue estimate
is needed. The proof uses an exact endpoint-error energy identity. A separate,
more restrictive theorem gives a quantitative all-time particle coupling at
each fixed block size and memory order. Its label threshold is not uniform in
those parameters. Thus this route does not establish the requested matched
dense-population compression theorem.

## 1. Model and exact block closure

There are $L\ge2$ hidden layers, $m$ fixed inputs, $n=Bk$ coordinates,
activation $\phi=\tanh$, residual $r_a=f_a-y_a$, and loss

\[
 \mathcal L=m^{-1}\sum_a r_a^2,\qquad
 \rho=\|r\|_2/\sqrt m,\qquad \tau=1+\int_0^t\rho(u)\,du.
\]

The mobilities are exactly those in the notation contract. Write

\[
 \kappa=\max_{1\le\ell\le L+1}\kappa_\ell,
 \qquad G_{ab}=x_a^Tx_b/d,\qquad g=\max_{a,b}|G_{ab}|.
\]

The stored readout is initially zero. A block mark consists of its initial
first-layer Gaussian training panel and its independent hidden matrices

\[
 A_\ell\in\mathbb R^{k\times k},\quad 2\le\ell\le L.
\]

When passive inputs are included, augment that mark by their initial
first-layer values jointly Gaussian with the training panel, with covariance
given by the complete training/passive input Gram. Equivalently, retain the
initial first-layer rows and evaluate all panels from those same rows. A
training-only Gaussian panel does not determine a general passive input's
initial value.

For the positive results below, begin with independent $N(0,1/k)$ entries,
then **condition each matrix separately on** $\|A_\ell\|_{\rm op}\le M$.
Conditioning preserves independence of the separate matrices and marks; it
does not preserve entrywise independence within a conditioned matrix.
This is an explicitly different initializer. First-layer Gaussian values are
not truncated. Blocks are aligned through depth. Learned updates are global;
they are not constrained to remain block diagonal.

Let $\mu$ be either the mark law or its empirical law on $B$ independent
marks. For vectors in one block use the literal norm $\|v\|_2/\sqrt k$ and
pairing $u^Tv/k$. In formulas below $\langle u,v\rangle_k=u^Tv/k$ is only
an abbreviation for this displayed pairing. Expectations contract block marks.

Use $q\ge1$ Legendre modes, numbered $0,\ldots,q-1$. Put

\[
 b_j=\sqrt{2j+1},\qquad
 D_{jj}=-(j+\tfrac12),\qquad
 D_{ji}=-\sqrt{(2j+1)(2i+1)}\ (i<j),\qquad D_{ji}=0\ (i>j).
\]

Then

\[
 D+D^T=-bb^T,\qquad \|b\|_2=q,\qquad \|D\|_{\rm op}\le q^2.
\tag{1}
\]

The orthonormalized moment variables are

\[
 X_{\ell-1,a,j}=\sqrt{2j+1}\,m^1_{\ell-1,a,j}/\sqrt\tau,
 \qquad
 Y_{\ell,a,j}=\sqrt{2j+1}\,m^2_{\ell,a,j}/\sqrt\tau.
\]

Here the forward source is $\rho h$, its prefix on activity interval

$[0,1]$ is (h(0)), the backward source is $r_a\delta_a$, and its
prefix is zero. The moving state consists of first-preactivation increments

$u_a$, readout $c$, $X,Y$, and the single shared scalar $\tau$.
Its equations are

\[
\begin{aligned}
 \dot u_a&=-\frac{2\kappa_1}{m}\sum_c r_c\delta_c^{(1)}G_{ca},
 &\dot c&=-\frac{2\kappa_{L+1}}m\sum_a r_a h_a^{(L)},\\
 \dot X_{\ell-1,a}&=\frac\rho\tau D X_{\ell-1,a}
             +\frac\rho{\sqrt\tau}b h_a^{(\ell-1)},
 &\dot Y_{\ell,a}&=\frac\rho\tau D Y_{\ell,a}
             +\frac{r_a}{\sqrt\tau}b\delta_a^{(\ell)},\\
 \dot\tau&=\rho.
\end{aligned}
\tag{2}
\]

Initially $u=c=Y=0$, $\tau=1$, and $X_{a,0}=h_a(0)$,

$X_{a,j}=0$ for $j>0$. The forward evaluation is

\[
\begin{aligned}
 z_a^{(1)}&=z_a^{(1)}(0)+u_a,\qquad h_a^{(\ell)}=\tanh z_a^{(\ell)},\\
 z_a^{(\ell)}(\omega)&=A_\ell(\omega)h_a^{(\ell-1)}(\omega)
 -\frac{2\kappa_\ell}m\sum_{c,j}Y_{\ell,c,j}(\omega)
       \mathbb E_\mu\langle X_{\ell-1,c,j},h_a^{(\ell-1)}\rangle_k,\\
 f_a&=\mathbb E_\mu\langle c,h_a^{(L)}\rangle_k.
\end{aligned}
\tag{3}
\]

The backward evaluation uses the transpose of the same correction:

\[
\begin{aligned}
 \delta_a^{(L)}&=c\odot\tanh'(z_a^{(L)}),\\
 \delta_a^{(\ell)}(\omega)&=\tanh'(z_a^{(\ell)}(\omega))\odot
 \left[A_{\ell+1}(\omega)^T\delta_a^{(\ell+1)}(\omega)
 -\frac{2\kappa_{\ell+1}}m\sum_{c,j}X_{\ell,c,j}(\omega)
     \mathbb E_\mu\langle Y_{\ell+1,c,j},\delta_a^{(\ell+1)}\rangle_k
 \right].
\end{aligned}
\tag{4}
\]

Equations (2)--(4) are an autonomous block mean-field system. For the empirical
law they are exactly the specified finite-$B$, finite-$q$ closure. They
require (O(Lmnq)) moving scalar state and (O(Lnk)) initialized matrix
storage, with $L,m$ fixed. They do not store an $n\times n$ trained matrix.
Trained blocks are interacting; only the initialized marks and nonlinear
copies driven by the deterministic population solution are independent.

These equations are **not** asserted to equal exact gradient flow at finite

$q$. Their relation to exact gradient flow is the defect identity below.

## 2. Exact passivity and the matrix-velocity defect

For one vector-valued, zero-prefix source $v$, write

\[
 \dot Z=\frac\rho\tau DZ+\frac\rho{\sqrt\tau}bv,
 \qquad Z(0)=0,\qquad \widehat v=\frac{b^TZ}{\sqrt\tau}.
\]

All norms in the next identity can be Euclidean, Euclidean divided by

$\sqrt k$, or averaged over marks. By (1),

\[
 \frac d{dt}\|Z\|_F^2
 =\rho\{-\|\widehat v\|_2^2+2\langle v,\widehat v\rangle\}.
\]

Consequently the exact identity is

\[
 \int_0^T\rho\|v-\widehat v\|_2^2dt
 =\int_0^T\rho\|v\|_2^2dt-\|Z(T)\|_F^2
 \le\int_0^T\rho\|v\|_2^2dt.
\tag{5}
\]

It is an error gain of one, uniformly in $q$, not merely a bounded-state
estimate. Also

\[
 \|Z(T)\|_F^2\le\int_0^T\rho\|v\|_2^2dt.
\tag{6}
\]

The forward constant prefix causes no difficulty. The moments representing
the constant function (h(0)) are $\sqrt\tau e_0h(0)$, since

$De_0+b=e_0/2$. Thus $X-\sqrt\tau e_0h(0)$ obeys the preceding zero-prefix
system with source (h-h(0)). In particular

\[
 \int_0^T\rho\|h-\widehat h\|_2^2dt
 \le\int_0^T\rho\|h-h(0)\|_2^2dt,
 \quad \widehat h=b^TX/\sqrt\tau.
\tag{7}
\]

Set $U_a=(r_a/\rho)\delta_a$ when $\rho>0$, and set it to zero when

$\rho=0$. Write $\widehat U_a=b^TY_a/\sqrt\tau$. Differentiating the
reconstructed learned operator gives, exactly,

\[
 \dot W_\ell^{\rm corr}
 =-\frac{2\kappa_\ell}m\sum_a r_a\delta_a^{(\ell)}\otimes h_a^{(\ell-1)}
 +\frac{2\kappa_\ell}m\sum_a\rho
       (U_a-\widehat U_a)\otimes(h_a^{(\ell-1)}-\widehat h_a^{(\ell-1)}).
\tag{8}
\]

Here $v\otimes w$ maps a block field $g$ to

$v\mathbb E_\mu\langle w,g\rangle_k$, including for empirical $\mu$.
To verify (8), the two drift terms in

$\sum_j\dot Y_j\otimes X_j+Y_j\otimes\dot X_j$ contract by

$D+D^T=-bb^T$. The remaining three terms are

$r\delta\otimes\widehat h+\rho\widehat U\otimes h-
\rho\widehat U\otimes\widehat h$; subtract $r\delta\otimes h$.
This also fixes the sign in (8).

In particular, replacing this closure's prediction derivative by the exact-GF
kernel equation would be incorrect. Identity (8) is the required correction.

## 3. Uniform finite-activity and fitting theorem

Let the initial last-feature Gram

\[
 Q_{ab}(0)=\mathbb E_\mu\langle h_a^{(L)}(0),h_b^{(L)}(0)\rangle_k
\]

satisfy $Q(0)\succeq\lambda I_m$, with $\lambda>0$. The theorem applies
to an arbitrary empirical or population mark law supported on the operator
cap. Define the following explicit constants:

\[
\begin{aligned}
 D_*&=2\kappa(M+1)^{L-1},\\
 J&=2\kappa\sqrt{2m}\,D_*,\qquad
 K=2\kappa\sqrt{m/3}\,D_*,\\
 C_V&=\kappa D_*(g+L)(M+2)^{L-1},\qquad
 \gamma=\kappa_{L+1}\lambda/m,\\
 s_0&=\min\left\{1,J^{-2/3},K^{-1/2},
       \sqrt{\frac\lambda{4mC_V}},
       \sqrt{\frac\gamma{4\kappa\sqrt m C_V}}\right\}.
\end{aligned}
\tag{9}
\]

If

\[
 Y_0:=\|y\|_2/\sqrt m\le\gamma s_0/4,
\tag{10}
\]

then the solution of (2)--(4) is unique and global, and

\[
 S_\infty:=\int_0^\infty\rho(t)dt\le2Y_0/\gamma\le s_0/2,
 \qquad Q(t)\succeq\lambda I_m/2.
\tag{11}
\]

Every moving state coordinate converges at infinity, and $r(t)\to0$.
For each hidden layer and sample,

\[
 \sup_\omega\int_0^\infty
       \frac{\|\dot h_a^{(\ell)}(t,\omega)\|_2}{\sqrt k}dt
 \le C_V S_\infty^2.
\tag{12}
\]

All constants in (9)--(12) are independent of $B,k,q$. No pointwise bound
on a backward coordinate is assumed or used. This theorem asserts fitting
and finite activity, not a uniform exponential decay rate.
Uniformity across a family of block sizes requires the same lower bound
$\lambda>0$ on their initial Grams; positivity separately at each block size
would not supply that uniformity.

### Proof: source bounds on an activity interval

Fix $T$ with $S=S(T):=\int_0^T\rho\le s_0$. Because tanh is bounded,

\[
 \sup_\omega\|c(t,\omega)\|_2/\sqrt k\le2\kappa S(t),
 \qquad
 \sup_\omega\|X_{\ell-1,a}(t,\omega)\|_F/\sqrt k
 \le\sqrt{1+S(t)}\le\sqrt2.
\tag{13}
\]

The first estimate integrates the readout equation. For the second, the
moment energy derivative is at most $\rho\|h\|_2^2$, and its initial
energy is $\|h(0)\|_2^2\le k$.

Backward induction gives

\[
 \sup_\omega\|\delta_a^{(\ell)}(t,\omega)\|_2/\sqrt k
 \le2\kappa(M+1)^{L-\ell}S(t)\le D_*S(t).
\tag{14}
\]

Indeed, it holds at layer $L$. If it holds for an upper layer, (6) and

$|r_a|\le\sqrt m\rho$ give for its backward memory

\[
 \sup_\omega\|Y_{\ell,a}(t,\omega)\|_F/\sqrt k
 \le\sqrt{m/3}\,D_*S(t)^{3/2}
 \le\sqrt m D_*S(t)^{3/2}.
\tag{15}
\]

The adjoint learned correction in (4), as an operator on fields with bounded
block RMS, therefore has norm at most $J S^{3/2}\le1$. Multiplying the
upper backward bound by (M+1) proves the induction. This reasoning proceeds
from layer $L$ downward; it does not assume its own conclusion for a lower
layer.

### Proof: feature variation

Define

\[
 V_\ell(T)=\max_a\sup_\omega\int_0^T
                      \|\dot h_a^{(\ell)}\|_2/\sqrt k\,dt.
\]

The supremum is outside the time integral. This placement matters: no
invalid interchange with the time integral is needed below. Integrating the
first-layer equation and using (14) gives the raw-increment bound

\[
 \max_a\sup_\omega\frac{\|u_a(t,\omega)\|_2}{\sqrt k}
 \le\kappa gD_*S(t)^2.
\tag{16a}
\]

Indeed its velocity is at most $2\kappa gD_*\rho(t)S(t)$ in block RMS,
and $\int_0^t\rho(s)S(s)ds=S(t)^2/2$. The same velocity bound, together
with $\|\tanh'\|_\infty\le1$, implies

\[
 V_1(T)\le\kappa gD_*S^2.
\tag{16}
\]

For a higher layer, differentiate (3). The initialized block contributes

$M V_{\ell-1}$. The term $W_\ell^{\rm corr}\dot h^{(\ell-1)}$
contributes at most $J S^{3/2}V_{\ell-1}$: use the uniform $X,Y$ bounds,
then integrate the expectation of the lower feature speed. The first term
of (8), applied to a current feature of RMS at most one, contributes at most

$\kappa D_*S^2$.

For the defect term, (5), (7), and (14) give, for every source sample,

\[
\begin{aligned}
 \sup_\omega\int_0^T\rho
       \|U_a-\widehat U_a\|_2^2/k\,dt
       &\le mD_*^2S^3/3,\\
 \int_0^T\rho\,\mathbb E_\mu
       \|h_a^{(\ell-1)}-\widehat h_a^{(\ell-1)}\|_2^2/k\,dt
       &\le S V_{\ell-1}(T)^2.
\end{aligned}
\tag{17}
\]

Cauchy--Schwarz in time bounds the action of that rank-one defect on a
bounded current feature by $K S^2V_{\ell-1}$, after the sample sum. Thus

\[
 V_\ell\le(M+J S^{3/2}+K S^2)V_{\ell-1}+\kappa D_*S^2
 \le(M+2)V_{\ell-1}+\kappa D_*S^2.
\tag{18}
\]

Iteration of (16)--(18) proves $V_\ell\le C_V S^2$. There is no circular
derivative estimate: each forward variation is controlled by the preceding
layer's variation. Equations (17)--(18) are also valid for a law of marks;
Tonelli's theorem applies to their nonnegative integrands.

### Proof: readout contraction in integrated form

Bounded features and the variation bound give

\[
 |Q_{ab}(t)-Q_{ab}(0)|\le2C_VS^2,
 \qquad \|Q(t)-Q(0)\|_{\rm op}\le2mC_VS^2\le\lambda/2.
\]

Differentiate only the readout in the prediction first:

\[
 \dot r=-\frac{2\kappa_{L+1}}mQ(t)r+e(t),
 \qquad e_a=\mathbb E_\mu\langle c,\dot h_a^{(L)}\rangle_k.
\tag{19}
\]

The readout term supplies $\dot\rho\le-\gamma\rho+
\|e\|_2/\sqrt m$, understood as an upper Dini derivative at zero. By
(13) and the feature variation estimate,

\[
 \int_0^T\|e(t)\|_2/\sqrt m\,dt
 \le2\kappa\sqrt m\,S V_L(T)
 \le2\kappa\sqrt m C_VS^3.
\]

Integrating (19), dropping the nonnegative terminal residual, and using
the last restriction in (9), gives

\[
 \gamma S\le Y_0+2\kappa\sqrt m C_VS^3
 \le Y_0+\gamma S/2,
 \qquad S\le2Y_0/\gamma\le s_0/2.
\tag{20}
\]

Starting at $S=0$, continuity rules out a first time $S=s_0$.

For fixed $k,q$, (2)--(4) are locally Lipschitz in the Banach space of
bounded block-state increments, with the unbounded initial first Gaussian
panel held fixed. Tanh and its first two derivatives are bounded; the cap
controls all markwise matrix actions. The bounds (13)--(15), the raw increment
bound (16a), and

$1\le\tau\le1+s_0$ keep the state in a bounded region of that space.
They prevent a finite-time escape and provide continuation for all time.
The norm $\rho$ is Lipschitz, so its nondifferentiability at zero causes no
ODE uniqueness problem.
These local Lipschitz statements and the associated scalar RMS comparison
inequalities are asserted for each fixed finite $k,q$; their constants may
depend on both. The activity threshold (9)--(10) and bounds (11)--(12)
remain uniform in $k,q$.

For fixed $k,q$, the bounded region gives $\|\dot{\rm state}\|\le
C_{k,q}\rho$. Finite activity therefore makes the whole state Cauchy as

$t\to\infty$. Predictions and $\rho$ have limits. Their finite integral
forces the residual limit to zero. This completes the proof.

### Passive inputs

A fixed passive input is evaluated using the same trained state and its
joint initial Gaussian panel specified in Section 1; it is absent from the
training updates (2). If $g_*=\max_a|x_a^Tx_*/d|<\infty$, its first variation
obeys $V_{1,*}\le\kappa g_*D_*S^2$. For higher layers the same calculation
gives

\[
 V_{\ell,*}\le(M+1)V_{\ell-1,*}
       +\kappa D_*S^2+K S^2V_{\ell-1}.
\tag{21}
\]

Thus passive features and predictions converge, with constants independent
of $k,q$ for their total variation. For a fixed $k,q$, a tail bound of
the form $C_{k,q,*}[S_\infty-S(t)]$ follows from the bounded-state velocity
equations. No uniform physical-time decay rate or generalization guarantee
is asserted.

## 4. A quantitative all-time particle theorem at fixed $k,q$

This supplementary theorem has a stricter label condition than (10). It is
included to identify exactly what the elementary pointwise-Lipschitz particle
proof accomplishes. It must not replace the uniform fitting threshold above.

Suppose the population initial Gram is at least $\lambda_0 I_m$. Let

\[
 \gamma_0=\kappa_{L+1}\lambda_0/(2m),\qquad
 H=100(L+1)(m+1)(1+M+\kappa+\|G\|_{\rm op})
               (1+\sqrt k)(1+q^2),\qquad
 C=H^{20(L+1)}.
\tag{22}
\]

Use the norm which sums the block RMS norms of all $u_a,c$, the block
Frobenius RMS norms of all $X,Y$, and the absolute $\tau$-difference.
For states within distance one of their initialized states, the constants
below may all be bounded by $C$:

1. the particle velocity divided by $\rho$, and its Lipschitz constant
   in the residual (whose norm is $\|r\|_2/\sqrt m$);
2. its Lipschitz constant in state, after extracting $\rho$;
3. the state Lipschitz constant of the prediction velocity divided by
   $\rho$;
4. the Lipschitz constant in residual of the prediction velocity's remainder
   after subtracting the initialized readout Gram, divided by the distance
   of the state from initialization;
5. the root-mean-square empirical replacement errors for these evaluations,
   multiplied by $\sqrt B$.

Here is an explicit way to check the deliberately loose bound (22).
On the unit state neighborhood, $\|X\|_F/\sqrt k\le2$,

$\|Y\|_F/\sqrt k,\|c\|_2/\sqrt k\le1$, and $1\le\tau\le2$.
Each forward layer has bounded output and propagates first and second state
derivatives with a factor at most $H^2$ per layer. The only pointwise
product estimate needed is

\[
 \|v\odot w\|_2/\sqrt k
 \le\sqrt k(\|v\|_2/\sqrt k)(\|w\|_2/\sqrt k).
\tag{23}
\]

Use $\|\tanh'\|_\infty\le1$, $\|\tanh''\|_\infty\le2$,

$\|D\|\le q^2$, and $\|b\|=q$. Forward/backward values and their
first derivatives are bounded by $H^{4L+4}$; second derivatives of the
prediction by $H^{6L+6}$; differentiating its velocity once costs at most

$H^{12L+14}$. These bounds allow sample sums and the sum defining the
state norm, since their counts are smaller than powers already absorbed in

$H$. For empirical replacement, expose the finitely many expectations in
the forward/backward evaluation and its differentiated evaluation in their
layer order. Each is an average of independent, bounded scalar or
finite-dimensional Hilbert-valued mark functions on the population path.
Its mean-square error is at most its squared norm bound divided by $B$.
The number of such contractions is at most a constant times

$(L+1)^2(m+1)^3(q+1)^2$, absorbed by the remaining margin in (22).
Propagating these elementary errors through the same layer bounds gives
item 5. This counts dependence on $k,q$; it assumes neither coordinatewise
backward boundedness nor a dimension-independent Lipschitz constant.

Put

\[
 a=\min\{1,\gamma_0/(2C)\},\qquad
 Y_0\le a\gamma_0/(2C),\qquad S_*=Y_0/\gamma_0.
\tag{24}
\]

The finite and population solutions then remain within distance $a/2$
of initialization and have $\rho(t)\le Y_0e^{-\gamma_0t}$, on the initial
empirical Gram event. This follows directly by writing their prediction
velocity as

\[
 \dot r=-\frac{2\kappa_{L+1}}m Q(0)r+R({\rm state},r),
 \quad \|R\|_2/\sqrt m\le C a\rho,
\tag{25}
\]

then integrating the state speed $C\rho$. The empirical event is

$Q_B(0)\succeq\lambda_0 I_m/2$, so the linear contraction in (25) is at
least $2\gamma_0$, leaving the displayed margin.

Couple a finite trained block with the population trajectory using the same
initial mark. Let (e$t$) be the sum of the empirical RMS errors of its
state fields, including the shared clock, and let

$d(t)=\|r_B(t)-r(t)\|_2/\sqrt m$. Both errors start at zero. Subtracting
the two augmented equations (state plus residual) gives

\[
\begin{aligned}
 D^+e&\le C d+C\rho e+\rho\xi_F(t),\\
 D^+d&\le-\gamma_0 d+C\rho e+\rho\xi_R(t),
\end{aligned}
\tag{26}
\]

where the nonnegative sampling errors satisfy

\[
 (\mathbb E\xi_F(t)^2)^{1/2},
 (\mathbb E\xi_R(t)^2)^{1/2}\le C/\sqrt B.
\tag{27}
\]

All expectations underlying (27) concern independent copies of the
**population** trajectory, not the interacting finite particles. Evaluating
the nonlinear empirical recursion at those copies is handled by the
successive replacement calculation just described. The initial Gram
fluctuation is included in $\xi_R$.

Integrate the second inequality before applying Gronwall to the first:

\[
 \int_0^t d\le\frac C{\gamma_0}\int_0^t\rho e
       +\frac1{\gamma_0}\int_0^t\rho\xi_R.
\]

With $A=C+C^2/\gamma_0$, this yields

\[
 \sup_t e(t)\le e^{A S_*}
       \int_0^\infty\rho(t)
          [\xi_F(t)+(C/\gamma_0)\xi_R(t)]dt.
\tag{28}
\]

The residual supremum follows from the integrated second inequality in
(26). Minkowski's inequality, (27), and the deterministic population activity
bound give a valid loose constant

\[
 C_{\mathrm{rate}}=4C(1+C/\gamma_0)(1+CS_*)S_*e^{(C+C^2/\gamma_0)S_*}
\tag{29}
\]

for

\[
 \left\{\mathbb E\left[\mathbf1_E
       (\sup_t e(t)+\sup_t d(t))^2\right]\right\}^{1/2}
 \le C_{\mathrm{rate}}/\sqrt B.
\tag{30}
\]

The rate constant $C_{\mathrm{rate}}$ is separate from the backward-source constant
$D_*$ in (9).

For completeness, each initialized Gram entry is an average of independent
variables in $[-1,1]$. Exponential Markov applied to their centered
moment-generating functions, bounded by $\exp(s^2/2)$, gives

\[
 \mathbb P(E^c)\le2m^2\exp[-B\lambda_0^2/(8m^2)].
\tag{31}
\]

To check the moment-generating bound directly, the second derivative of the
log moment-generating function is the variance under an exponential tilt.
A variable in an interval of length two has variance at most one, also under
that tilt. The log moment-generating function and its first derivative vanish
at zero after centering, so two integrations give the bound $s^2/2$.

The entrywise threshold is $\lambda_0/(2m)$, which bounds the operator
error by $\lambda_0/2$. Hence for $0<\eta<1$, with probability at least

$1-\eta-2m^2e^{-B\lambda_0^2/(8m^2)}$,

\[
 \sup_{t\ge0}e(t)+\sup_{t\ge0}\|f_B(t)-f(t)\|_2/\sqrt m
 \le C_{\mathrm{rate}}/\sqrt{B\eta}.
\tag{32}
\]

This is a coupling rate for tagged block states and predictions. It does not
assert a $B^{-1/2}$ Wasserstein rate for an empirical law on its full
high-dimensional state space: that distance also contains the empirical-law
sampling error of the independent population copies.

## 5. Exact limitations and the remaining bridge

The constants in (22)--(24) show precisely why the simple rate theorem does
not cover one fixed nonzero label while $k,q\to\infty$. The uniform
fitting theorem removes that obstruction for existence and optimization,
but not yet for the particle comparison.

Two ambient-norm losses are real:

* Block operator norm control does not make backward coordinates uniformly
  bounded. With a unit-RMS vector $v=\mathbf1$, a matrix of norm $M$ can
  satisfy $A^Tv=M\sqrt k e_1$. At a coordinate where
  $\tanh''(z)\ne0$, the derivative of
  $z\mapsto\tanh'(z)\odot A^Tv$, in block RMS norm, is of size
  $cM\sqrt k$. Thus a dimension-independent Lipschitz estimate on the
  whole bounded-energy state neighborhood is false. This is a statement
  about that neighborhood, not a claim about typical reached Gaussian states.
* Although $D$ is dissipative, the endpoint functional has norm $q$,
  and the clock-drift generator has order $q^2$. For the unit vector
  $b/q$,
  \[
   (Db/q)_j=-\frac{\sqrt{2j+1}}q(j^2+j+\tfrac12),\qquad
   \|Db/q\|_2^2\sim q^4/3.
  \]
  A difference of clocks therefore introduces a (D X) term in a naive
  state comparison. Contractivity of the same-clock semigroup does not
  bound that term. Identity (5) resolves the fitting argument, but a
  corresponding two-trajectory estimate is still needed for uniform
  particle stability.

The uniform activity theorem suggests the next precise proof obligation:
derive a two-trajectory analogue of (5)--(18), with different residual clocks,
which bounds integrated hidden prediction error by a small multiple of
integrated residual error plus empirical sampling errors. This could allow
the stable readout part to close (26) for the fixed label threshold (10),
with a rate constant depending on $k,q$ only through a finite-activity
Grönwall factor. That statement is **not proved here**. Neither convergence
as $q\to\infty$ nor identification as $k\to\infty$ with the dense
Gaussian population follows from the proved fitting result.

Finally, the cap is not innocuous at fixed $k$ and $B\to\infty$.
The elementary Gaussian net estimate gives

\[
 p_k:=\mathbb P(\|A\|_{\rm op}>M)
 \le2\exp(2k\log9-kM^2/8).
\]

An elementary coupling of conditioned and unconditioned finite initializers
has disagreement probability at most $B(L-1)p_k$. For fixed $k$,
conditioning all blocks is not a high-probability event as $B\to\infty$.
For a sufficiently large fixed $M$ and growing $k$, the displayed
coupling is useful only under its explicit $B e^{-c_Mk}$ requirement.
A comparison of capped and uncapped *population* dynamics needs an additional
tail-stability theorem. The capped block results are therefore not silently
transferred to ordinary Gaussian blocks or the original dense initializer.

## 6. Claim status

| Claim | Status and scope |
|---|---|
| Autonomous finite-memory block equations and global learned corrections | Exact, (2)--(4) |
| Endpoint-error passivity and matrix-velocity defect | Exact, (5)--(8) |
| Fixed-small-label global fitting and finite total activity | Proved under the block cap and initial Gram gap; constants uniform in $B,k,q$ |
| Passive-input feature/prediction endpoints | Proved for each fixed panel/input under the same assumptions |
| All-time quantitative $B^{-1/2}$ strong particle coupling | Proved with the stricter $k,q$-dependent label condition (24) |
| Same rate under the single uniform label condition (10) | Open; needs a two-trajectory passivity/clock argument |
| Uniform quantitative physical-time tail | Open |
| Unconditioned fixed-$k$ block population | Not covered by the cap theorem |
| Closure convergence and matched dense-population compression | Not established by this route |
