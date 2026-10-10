# Conditional Gaussian carriers and the missing trajectory lower bound

This is a scoped author derivation for the two-hidden-layer tanh model. It
contains exact conditional Gaussian formulas, exact low-order identifications,
an all-finite-order nonvanishing result, a scalar fluctuation lemma, and a
uniform coefficient bound for the all-first-layer response sector. It does
**not** prove a growing-order accuracy or storage theorem for frozen-top NTH.
In particular, the scalar carrier calculation below is not asserted to be the
complete conditional chaos of the neural prediction error.

Inputs: the supervisor's assignment and subsequent suggested column-carrier
route, the complete same-study `TANH_GENERIC_ROUTE.md` and
`TANH_HIGH_ORDER_ROUTE.md`, and maintained notation. Required proof,
conjecture-audit, and canonical-notation instructions were read. The scalar-star
formula was shared with the same-study averaged-upper author after the
supervisor authorized that exchange. No other study, experiment, or external
theorem was used. This is not an independent review.

## Model and hierarchy

Let fixed inputs $v_a=x_a/\sqrt d\in\mathbb R^d$ satisfy $\|v_a\|_2=1$,
and let $y\in\mathbb R^m\setminus\{0\}$ be fixed. Put $c_a=y_a/m$.
The model is

\[
z_a^{(1)}=W^{(1)}v_a,\quad h_a^{(1)}=\tanh z_a^{(1)},\quad
z_a^{(2)}=W^{(2)}h_a^{(1)},\quad h_a^{(2)}=\tanh z_a^{(2)},\quad
f_a=u^\top h_a^{(2)}/n.
\]

Initialization has independent $W^{(1)}_{ji}\sim N(0,1)$,
$W^{(2)}_{ij}\sim N(0,1/n)$, and $u=0$. The constant parameter mobility
$M$ multiplies the three blocks by $(n,1,n)$. The physical loss is
$\mathcal L=(2m)^{-1}\sum_a(f_a-y_a)^2$. Define

\[
V_a=M\nabla f_a,\qquad F=\sum_a c_af_a,\qquad
V_y=\sum_a c_aV_a=M\nabla F.
\]

Source time $s$ means $d\theta/ds=V_y(\theta)$; physical time means
$\dot\theta=\sum_a(y_a-f_a)V_a/m$. These are different flows.
Write $K^{(1)}_a=f_a$ and
$K^{(r+1)}_{a_1\ldots a_{r+1}}=D K^{(r)}_{a_1\ldots a_r}[V_{a_{r+1}}]$.
Thus the scalar initialized source contraction is

\[
C_k:=\frac{d^{2k+1}}{ds^{2k+1}}F(\theta(s))\bigg|_{s=0}
=\sum_{a_1,\ldots,a_{2k+2}}c_{a_1}\cdots c_{a_{2k+2}}
K^{(2k+2)}_{a_1\ldots a_{2k+2}}(0).
\tag{1}
\]

The frozen-top hierarchy of rank $q\ge2$ stores the actual initialized
tensors through rank $q$, evolves

\[
\dot{\widehat K}^{(r)}_{a_1\ldots a_r}
=\sum_b\widehat K^{(r+1)}_{a_1\ldots a_r b}
\frac{y_b-\widehat f_b}{m},\quad r<q,
\qquad \dot{\widehat K}^{(q)}=0.
\tag{2}
\]

Its prediction is $\widehat f=\widehat K^{(1)}$. Its residual is its own.
The population final-feature gap in the assignment implies that no inputs
coincide up to sign. As proved in `TANH_GENERIC_ROUTE.md`, this implies the
first-feature Gram $Q^{(1)}\succ0$. The lemmas below need this
nondegeneracy, but do not use smallness of the fixed labels.

## An exact one-column Gaussian perturbation

All quantities in this section are initialized. Set

\[
H=[h_a^{(1)}]_{a=1}^m,\quad Z=W^{(2)}H,\quad
P=H(H^\top H)^{-1}H^\top,\quad X_{ja}=W^{(1)}_{j\cdot}v_a,
\]
\[
b_i=\sum_a c_a\tanh Z_{ia},\quad
C_{ia}=b_i\operatorname{sech}^2 Z_{ia},\quad
\Sigma_n=C^\top C/n,\quad g_{ja}=(W^{(2)\top}C)_{ja}.
\tag{3}
\]

Here $H,C\in\mathbb R^{n\times m}$; $g_j\in\mathbb R^m$ is a reverse
carrier. On the full-rank event, condition on $W^{(1)},Z$. Gaussian
orthogonal projection gives

\[
W^{(2)}=ZH^++R(I-P),\qquad R_{ij}\stackrel{\rm iid}{\sim}N(0,1/n).
\tag{4}
\]

The matrix $R$ is independent of the conditioning variables. Fix a neuron
$j$ with $d_j=(I-P)e_j\ne0$, and fix $\beta\in\mathbb R^m\setminus\{0\}$
with $C\beta\ne0$. The scalar

\[
G=\beta^\top C^\top R d_j
\]

is centered Gaussian with variance
$\|d_j\|_2^2\beta^\top\Sigma_n\beta$. Its Gaussian regression component
in $W^{(2)}$ is exactly

\[
\Delta W^{(2)}
=G\frac{(C\beta)d_j^\top}{\|C\beta\|_2^2\|d_j\|_2^2}.
\tag{5}
\]

Indeed, the covariance of $R_{il}$ with $G$ is
$(C\beta)_i(d_j)_l/n$; division by $\operatorname{Var}G$ gives (5),
and $d_j^\top(I-P)=d_j^\top$. The remaining Gaussian matrix is
independent of $G$. In particular,

\[
\|\Delta W^{(2)}\|_{\rm op}
=\frac{|G|}{\sqrt{n\beta^\top\Sigma_n\beta}\,\|d_j\|_2},
\qquad
\Delta g_l
=G\frac{\Sigma_n\beta}{\beta^\top\Sigma_n\beta}
\frac{\delta_{lj}-P_{lj}}{1-P_{jj}}.
\tag{6}
\]

Assume $\Sigma_n\succ0$, choose an index $a$ with $c_a\ne0$, and put
$\beta=\Sigma_n^{-1}e_a$. After writing
$\xi=G/(\Sigma_n^{-1})_{aa}$, these identities become

\[
\operatorname{Var}(\xi\mid W^{(1)},Z)
=\frac{1-P_{jj}}{(\Sigma_n^{-1})_{aa}},\quad
\Delta g_j=\xi e_a,\quad
\Delta g_l=-\xi e_a\frac{P_{lj}}{1-P_{jj}}\quad(l\ne j).
\tag{7}
\]

Since every row of $H$ has norm at most $\sqrt m$, boundedness of
$(H^\top H/n)^{-1}$ implies $|P_{lj}|\le C/n$. On conditioning events
where the spectra of $\Sigma_n$ and $H^\top H/n$ stay in fixed positive
compact intervals, (5)--(7) consequently give

\[
\|\Delta W^{(2)}\|_{\rm op}\le C|\xi|/\sqrt n,\qquad
\|\Delta g_l\|_2\le C|\xi|/n\quad(l\ne j).
\tag{8}
\]

Such spectral events have probability tending to one, by the positive
population covariance and conditional laws of large numbers proved in the
generic route. Thus a carrier of size $\sqrt k$ changes the matrix operator
norm by only $O(\sqrt{k/n})$. This is an exact conditioning statement. It
is not yet a statement about a trajectory perturbed by that carrier.

## The first-layer star and its exact low-order occurrence

For a fixed carrier vector $g\in\mathbb R^m$, define the scalar function

\[
\psi_g(w)=\sum_a c_ag_a\tanh(w^\top v_a),\qquad w\in\mathbb R^d.
\tag{9}
\]

At initialization the exact first-layer source acceleration in row $j$ is
$\nabla\psi_{g_j}(W^{(1)}_{j\cdot})$. Consider the auxiliary local equation

\[
\frac{dw}{d\tau}=\nabla\psi_g(w),\qquad
\tau=s^2/2,\qquad w(0)=w_0.
\tag{10}
\]

Equation (10) keeps the background readout velocity equal to $b$ and keeps
the initialized reverse carrier fixed. It is a specified single-neuron
sector; it is **not** the full source flow. Put
$L_g=\nabla\psi_g\cdot\nabla$. Its local response satisfies

\[
\psi_g(w(s))-\psi_g(w_0)
=\sum_{k\ge1}\frac{s^{2k}}{2^k k!}
(L_g^k\psi_g)(w_0)
\tag{11}
\]

inside its finite-dimensional local analytic disk.

Both the feature change and its effect on the readout enter the source
observable. Linearizing their effect on the background $u=sb$ gives the
following precisely defined star response:

\[
F_{\rm star}(s)=\frac1n\left[
s\{\psi_g(w(s))-\psi_g(w_0)\}
 +\int_0^s\{\psi_g(w(t))-\psi_g(w_0)\}\,dt\right].
\tag{12}
\]

To see the integral term, write $\delta u(s)=\int_0^s\delta h(t)dt$ in
$\delta(u^\top h)=sb^\top\delta h+\delta u^\top b$, and use
$b^\top\delta h=\psi_g(w)-\psi_g(w_0)$ for the selected first-layer
column. Substitution of (11) gives

\[
F_{\rm star}^{(2k+1)}(0)
=\frac{(2k+2)(2k)!}{2^k k!\,n}(L_g^k\psi_g)(w_0).
\tag{13}
\]

The expression $(L_g^k\psi_g)(w_0)$ is homogeneous of degree $k+1$ in
$g$. It is not of the maximal possible conditional degree $2k$ of $C_k$.
The latter degree selects locally affine first-layer terms and therefore
misses the repeated first-layer curvature responsible for (13).

There are two exact checks against the complete hierarchy. Let
$B(w)=\sum_a c_a h_a^{(2)}(w)$, where $w$ now denotes both hidden
parameter blocks. Give this space the metric
$\|A\|_{\rm hid}^2=\|A^{(1)}\|_F^2/n+\|A^{(2)}\|_F^2$.
Let $J=DB(w_0)$ and define its adjoint by
$\langle J^*b,A\rangle_{\rm hid}=b^\top JA/n$; put $A=J^*b$.
The exact source identities derived in the high-order route are

\[
C_1=4\|A\|_{\rm hid}^2,\qquad
C_2=16\|JA\|_2^2/n+36b^\top D^2B(w_0)[A,A]/n.
\tag{14}
\]

Because $A^{(1)}_{j\cdot}=\nabla\psi_{g_j}(W^{(1)}_{j\cdot})$, the
first-layer part of $C_1$ is exactly
$4\sum_j\|\nabla\psi_{g_j}\|_2^2/n$, agreeing with (13) at $k=1$.
The part of $D^2B[A,A]$ differentiating the first activation twice is

\[
\frac1n\sum_{j,a}c_ag_{ja}\tanh''(X_{ja})
\big(v_a^\top A^{(1)}_{j\cdot}\big)^2
=\frac1n\sum_j D^2\psi_{g_j}
[\nabla\psi_{g_j},\nabla\psi_{g_j}].
\tag{15}
\]

Thus its contribution to $C_2$ is exactly $36$ times (15), agreeing with
(13), since $L_g^2\psi_g=2D^2\psi_g[\nabla\psi_g,\nabla\psi_g]$.
The other terms in $C_2$ remain present and may have either sign. Equations
(14)--(15) do not assert that their conditional cubic projections vanish.
For $k\ge3$, identifying (13) with a leading part of the **complete**
coefficient uniformly in $k,n$ remains a missing step.

## A proved scalar factorial mechanism

Under the contrast (7), the highest power of $\xi$ in the local expression
(13) comes from replacing $\psi_g$ by
$c_a\xi\tanh(w^\top v_a)$. Since $\|v_a\|_2=1$, write
$x=w^\top v_a$ and define

\[
\mathcal F(x)=x/2+\sinh(2x)/4,\qquad
T(z)=\tanh(\mathcal F^{-1}(z)).
\tag{16}
\]

The inverse is well defined on the real line because
$\mathcal F'(x)=\cosh^2x>0$. The local scalar solution has
$\mathcal F(x(s))=\mathcal F(x(0))+c_a\xi s^2/2$, and

\[
(L_g^k\psi_g)_{\text{degree }k+1\text{ in }\xi}
=(c_a\xi)^{k+1}T^{(k)}(\mathcal F(x(0))).
\tag{17}
\]

Here the subscript refers only to the polynomial defined by (13).
The ODE for the scalar function is particularly simple:

\[
T'(z)=(1-T(z)^2)^2,\qquad T(0)=0.
\tag{18}
\]

**Lemma.** For $X\sim N(0,1)$ there are absolute constants $c,C>0$ such
that, for every positive odd integer $k$,

\[
\mathbb E\big|T^{(k)}(\mathcal F(X))\big|^2
\ge c\,(k!)^2 C^{-k}/(k+1).
\tag{19}
\]

**Proof.** Set $S(z)=-iT(iz)$. Equation (18) becomes
$S'=(1+S^2)^2$, $S(0)=0$. Its odd Taylor coefficients
$S(z)=\sum_{l\ge0}a_lz^{2l+1}$ are nonnegative. Moreover $a_0=1$ and

\[
(2l+1)a_l\ge2\sum_{i=0}^{l-1}a_i a_{l-1-i},\qquad l\ge1.
\]

Induction gives $a_l\ge2^{-l}$: the right side is at least
$4l\,2^{-l}\ge(2l+1)2^{-l}$. Therefore
$|T^{(k)}(0)|\ge k!2^{-(k-1)/2}$ for odd $k$.

For a uniform neighboring bound, the integral equation
$T(z)=\int_0^z(1-T(w)^2)^2dw$ is a contraction on the holomorphic
supremum ball $\|T\|_\infty\le1/2$ in $|z|\le R$, $R=1/16$.
Indeed, its image has norm at most $R(5/4)^2<1/2$ and its Lipschitz
constant is at most $R(5/2)<1$. Cauchy's formula on disks of radius
$R/2$ consequently gives

\[
\sup_{|z|\le R/2}|T^{(k+1)}(z)|
\le\tfrac12(k+1)!(2/R)^{k+1}.
\]

Choose
$\delta_k=2^{-(k-1)/2}(R/2)^{k+1}/(k+1)$.
On $|z|\le\delta_k$, the preceding derivative bound and the real mean
value formula imply
$|T^{(k)}(z)|\ge\tfrac12 k!2^{-(k-1)/2}$.
For $|x|\le\delta_k/2$, $\mathcal F'(x)\le2$ and hence
$|\mathcal F(x)|\le\delta_k$. The standard Gaussian density is bounded
below on this interval, so its probability is at least $c\delta_k$.
Integration on that interval proves (19). $\square$

For example, take $X,G$ independent standard Gaussians and fix
$\xi=\sigma G$, $\sigma>0$. The coefficient of $s^{2k+1}$ in the
degree-$(k+1)$ Gaussian Hermite projection of (12) is exactly

\[
\frac1n\frac{2k+2}{2k+1}\frac{(c_a\sigma)^{k+1}}{2^k k!}
T^{(k)}(\mathcal F(X))\operatorname{He}_{k+1}(G).
\tag{20}
\]

The probabilists' Hermite polynomial satisfies
$\mathbb E\operatorname{He}_r(G)^2=r!$; this follows by comparing
coefficients in
$\mathbb E[e^{tG-t^2/2}e^{uG-u^2/2}]=e^{tu}$.
Combining this identity with (19) gives an $L^2$ lower bound for (20)
of the form

\[
\frac{c}{n}|c_a\sigma|^{k+1}C^{-k}\sqrt{k!}.
\tag{21}
\]

For an average of $n$ independent copies, orthogonality gives the same
bound with $n^{-1/2}$ in place of $n^{-1}$. This demonstrates a
factorial fluctuation mechanism at the desired scale in the specified
scalar sector. The actual neural carriers have projection correlations,
feedback, and additional terms. Independence of replicas in this last
sentence is an auxiliary hypothesis, not an established neural identity.

## Complete finite-order coefficients cannot all cancel

The following conclusion concerns the actual network, but is qualitative.

**Proposition.** Suppose $n\ge m+1$, $Q^{(1)}\succ0$, and $y\ne0$.
With probability one, $C_k\ne0$ for every integer $k\ge1$.

**Proof.** First, $H$ has full column rank almost surely. Otherwise all
$m$-row determinants vanish identically as analytic functions of their
Gaussian rows, which would put every possible feature row in a common
proper subspace and contradict $Q^{(1)}\succ0$. A nonzero real-analytic
function has a Lebesgue-null zero set: this follows from one-variable
isolated zeros and induction using Fubini on Taylor coefficients. Thus a
nonidentically-zero determinant is nonzero almost surely.

Condition on $W^{(1)},Z$. As proved by the tree expansion in the generic
route, $C_k$ is a polynomial of degree at most $2k$ in the unused Gaussian
matrix. To recall the counting: a term has $2k+2$ output vertices and
$2k+1$ derivative-contraction edges. At $u=0$, every output vertex must
receive exactly one readout derivative. Those edges form a perfect
matching, leaving $k$ hidden edges. Each of their endpoints supplies at
most one explicit $W^{(2)}$, giving degree at most $2k$.

Choose any unit $r\in\ker H^\top$ and any second-layer row $i$.
Vary $W^{(2)}$ by $t e_i r^\top$, keeping $Z$ fixed. Define vectors
$A_a\in\mathbb R^{nd}$ by their $j$th blocks
$r_j\operatorname{sech}^2(X_{ja})v_a$, and define

\[
B_i(w)=\sum_a c_a\tanh(Z_{ia}+A_a^\top w).
\]

Let $U'=B_i(w)$, $w'=U\nabla B_i(w)$, with $U(0)=0,w(0)=0$, and
write $d_k=(UB_i(w))^{(2k+1)}(0)$. The coefficient of $t^{2k}$ in
the **complete** polynomial $C_k$ is exactly $d_k/n$.
One way to verify this coefficient without selecting individual trees
is to rescale source time $s=\sigma/t$, readout $u=\widetilde u/t$,
and first-layer displacement $W^{(1)}-W^{(1)}_0=\widetilde w/t$.
The second-layer displacement is $O(t^{-2})$. In the rescaled equations,
$t\{\tanh(X+t^{-1}\widetilde w v)-\tanh X\}$ tends to
$\operatorname{sech}^2(X)\widetilde w v$. Only row $i$ then drives
$\widetilde w$; the other readout coordinates have constant velocities
and contribute only linearly in $\sigma$ to $tF$. The limiting nonlinear
equations are precisely the displayed scalar-readout system. The
rescaled vector fields extend analytically to $1/t=0$ because the
apparent divided difference is removable. Their finite initial jets
therefore converge, giving the asserted leading coefficient.

It remains to exclude $d_k\equiv0$. Set $Z_i=\varepsilon\zeta$ with
$\eta=\sum_a c_a\zeta_a\ne0$, and put $g=\sum_a c_aA_a$.
For almost every $W^{(1)}$, $g\ne0$. Indeed, each vector
$\sum_a c_a\operatorname{sech}^2(X_{ja})v_a$ is the gradient of the
nonconstant analytic function $w\mapsto\sum_a c_a\tanh(w^\top v_a)$;
its simultaneous zero set is null. Since $r\ne0$, at least one
nonzero block survives in $g$.

To second order in $\varepsilon$, the scalar-readout equations reduce to
$U'=\varepsilon\eta+g^\top w$, $w'=Ug$. Their solution gives

\[
U B_i(w)=\frac{\varepsilon^2\eta^2}{2\|g\|_2}
\sinh(2\|g\|_2s)+O(\varepsilon^4),\qquad
d_k=4^k\|g\|_2^{2k}\eta^2\varepsilon^2+O(\varepsilon^4).
\tag{22}
\]

The remainder statement is for each fixed derivative order. It follows
also from oddness of tanh and analytic parameter dependence. Thus $d_k$
is a nonzero analytic function of $Z_i$. Conditional on $W^{(1)}$, the
row $Z_i$ has a nonsingular Gaussian density, so $d_k\ne0$ almost
surely. Finally the unused coordinate $\sqrt n\langle W^{(2)}_{i\cdot},r\rangle$
is Gaussian of variance one. The complete polynomial has a nonzero
leading coefficient in this coordinate, hence vanishes with probability
zero. A countable intersection proves the assertion for every $k$.
$\square$

This proof prevents cancellation of the highest total degree, but does
not give its useful size. The one-coordinate Hermite certificate is only
$\sqrt{(2k)!}|d_k|/n^{k+1}$. For each fixed $k$, $d_k$ has a
width-independent upper bound because $\|A_a\|_2\le1$ and tanh has
bounded derivatives of every fixed order. The certificate alone is thus
well below $n^{-1/2}$. It is the middle degree in (13), rather than this
highest degree, that could carry the rare-neuron obstruction.

## Exact transfer to the first missed physical derivative

All odd initialized tensors vanish by the same readout matching argument.
Consequently rank $2k+1$ in (2) is identical to rank $2k$: its initialized
top tensor is zero and its rank-$2k$ tensor remains frozen.
For either rank define the scalar prediction error

\[
e(t)=\sum_a c_a\{f_a(t)-\widehat f_a(t)\}.
\]

Then, exactly,

\[
e^{(j)}(0)=0\quad(0\le j\le2k),\qquad
e^{(2k+1)}(0)=C_k.
\tag{23}
\]

For a direct check, the exact top tensor first has a nonzero discrepancy
at its second derivative, namely $K^{(2k+2)}$ contracted twice with $c$.
Each downward hierarchy equation integrates that discrepancy once and
contracts another index with $c$. Differences between the two residuals
first enter at the prediction-error order itself and hence affect a
strictly later prediction derivative. Induction down to rank one gives
(23), including the factorials from successive integrations.

The proposition and (23) imply that every finite frozen rank has nonzero
prediction error on every sufficiently small positive interval, almost
surely. This is an exact nonclosure statement. It is not an
$n^{-1/2}$-accuracy lower bound.

For precision about the missing quantitative transfer, let $r=2k+1$.
If $e$ is holomorphic on $|t|<R$, $|e(t)|\le M$ there, and its first
nonzero Taylor coefficient is $a=e^{(r)}(0)/r!$, put
$A=|a|R^r$. Cauchy's formula and summation of the geometric tail give

\[
\sup_{0\le t\le T}|e(t)|
\ge\frac A2\left[\min\left\{\frac TR,\frac12,\frac A{4M}\right\}\right]^r.
\tag{24}
\]

Indeed, evaluate at $t=R\theta$ for the minimum in brackets. The leading
term has magnitude $A\theta^r$, whereas the remaining terms are bounded
by $M\theta^{r+1}/(1-\theta)\le A\theta^r/2$. Thus a coefficient
small-ball estimate of size $n^{-1/2}$ with an order-one analytic envelope
can lose another factor comparable to $n^{-r/2}$. Merely naming
analyticity does not preserve the fluctuation scale.

## A uniform coefficient lemma for the all-first-layer sector

The following later refinement controls one exact part of the actual tensor
expansion. Let $C_k^{(1)}$ be the part of $C_k$ whose $k$ hidden
parameter-contraction edges all belong to $W^{(1)}$. Equivalently, it is
the initialized source derivative computed with mobility $(n,0,n)$.
This alternative mobility defines a component of the original response
polynomial; it does not replace the requested training model or closure.

Use the single contrast in (7), writing the conditional matrix as

\[
W^{(2)}=D+\xi\alpha d^\top,\qquad
\alpha=C\Sigma_n^{-1}e_a/n,\qquad
d=(I-P)e_j/(1-P_{jj}).
\tag{25}
\]

The sample index $a$ is fixed, the vector $\alpha$ has $n$ coordinates,
and $D$ is independent of $\xi$ under the conditional Gaussian law.
In particular $C^\top\alpha=e_a$ and $d_j=1$.

Assume deterministic bounds

\[
\|D\|_{\rm op}\le B,\quad \|\alpha\|_\infty\le A/n,\quad
\|d\|_1\le D_0,\quad
\max_{l\ne j}|d_l|\le D_0/n,
\tag{26}
\]

and that the conditional standard deviation $\sigma$ of $\xi$ lies in
a fixed positive compact interval. These bounds hold on the conditioning
and matrix-norm events described above; the lemma itself is deterministic
in $D,\alpha,d,X,Z$.

**Sector lemma.** Let $p=k+1$, and project the complete polynomial
$C_k^{(1)}(\xi)$ onto the normalized Hermite polynomial
$\operatorname{He}_p(\xi/\sigma)/\sqrt{p!}$. Its coefficient is

\[
\frac{\sigma^p\sqrt{p!}}n
\frac{(2k+2)(2k)!}{2^k k!}\,
c_a^p T^{(k)}(\mathcal F(X_{ja}))
 +\mathcal R_{k,n},\qquad
|\mathcal R_{k,n}|\le n^{-3/2}(Ck)^{Ck}.
\tag{27}
\]

Here $C$ depends only on the constants in (26), the fixed labels/data,
and the bounds on $\sigma$. It is independent of $k,n$. All higher
ordinary powers of $\xi$ that project into Hermite degree $p$ are
included in $\mathcal R_{k,n}$.

**Proof.** Expand the iterated source derivative into its derivative
contraction trees, as in the preceding proposition. At zero readout,
contract the perfect matching of $k+1$ readout edges. There are then
$I=k+1$ second-layer indices. A first-layer derivative of an outer tanh
is expanded by its set partitions. Each group supplies one explicit
$W^{(2)}$ factor and one derivative of the first activation.

Let $M$ be the number of explicit $W^{(2)}$ factors in a term. It obeys
$k+1\le M\le2k$ whenever the term contains a power $\xi^p$ with
$p\ge k+1$. Introduce one group vertex for each of those $M$ factors,
join it to its second-layer vertex, and join groups by the $k$ original
first-parameter contraction edges. This expanded graph is connected and
has $I+M$ vertices and $M+k=I+M-1$ edges; it is a tree. Contract the
$k$ first-parameter edges. The resulting bipartite tree has $I$ vertices
of second-layer type, $M-k$ vertices of first-neuron type, and $M$ matrix
edges. Every first-neuron vertex has degree at least two: every original
group contains at least one contracted first-layer derivative and hence
belongs to a group component with at least two vertices.

For the coefficient of $\xi^r$, mark $r$ of the matrix edges and replace
them by $\alpha_i d_l$; the other $u=M-r$ edges carry $D_{il}$.
All remaining factors belong to vertices. Their absolute values, including
activation derivatives and input inner products, are bounded by constants
depending on their derivative orders but not on $n$. The common scalar
normalization is exactly $1/n$: the $2k+2$ output factors contribute
$n^{-2k-2}$, the readout edges contribute $n^{k+1}$, and the first-layer
edges contribute $n^k$.

Remove the marked edges. The remaining graph is a forest of unmarked
matrix edges. At a second-layer vertex with $r_i$ marked incidences,
the vertex factor has supremum norm at most a constant times
$(A/n)^{r_i}$. Its $\ell^2$ norm is at most a constant times
$A^{r_i}n^{1/2-r_i}$. An isolated such vertex has $r_i\ge1$ and its
summed absolute value is bounded by a constant times
$A^{r_i}n^{1-r_i}$.

At a first-neuron vertex with $s_l$ marked incidences, the extra factor
is $d_l^{s_l}$. A leaf of a nontrivial unmarked component necessarily
has $s_l\ge1$, because its total degree before removing marked edges
was at least two. Its $\ell^2$ norm is therefore bounded independently
of $n$ by $\|d\|_1^{s_l}$. Interior first-neuron factors have bounded
supremum norm. An isolated first-neuron vertex has $s_l\ge2$, and its
absolute sum is likewise bounded by $\|d\|_1^{s_l}$.

A tree of matrices with operator norms at most $B$ contracts to at most
$B^{\#\mathrm{edges}}$ times its leaf $\ell^2$ norms and interior
supremum norms. To prove this, propagate a leaf vector through its edge
using the operator bound, multiply incoming vectors at an interior vertex
using $\|v_1\cdots v_s\|_2\le\prod_b\|v_b\|_2$, and finish at a
vertex of degree at least two with Cauchy--Schwarz. A one-edge tree is
the defining operator-norm inequality.

Let $N$ be the number of nonisolated second-layer vertices in this
forest, and $L$ the number of those that are leaves. The accumulated
power of $n$, before the common $1/n$, is at most

\[
-r+(I-N)+L/2=-(r-k-1)-N+L/2.
\tag{28}
\]

Here $L\le N$. If $u>0$, then $N\ge1$. It follows that the
coefficient of $\xi^{k+1}$ from every term having an unmarked matrix
edge is bounded by $n^{-3/2}$ times its derivative and combinatorial
constants. For $r>k+1$, all terms are bounded by
$n^{-1-(r-k-1)}$ times such constants, with a further $n^{-1/2}$ gain
when an unmarked edge is present.

When $r=k+1$ and $u=0$, the tree has one first-neuron vertex and exactly
one marked edge incident to each second-layer vertex. Every second-layer
sum is precisely a coordinate of $C^\top\alpha=e_a$. Thus all sample
indices in this part equal the selected sample $a$. Summing these trees
gives exactly the single-neuron expression (13), summed over first
neurons with multiplier $d_l^{k+1}$. Equivalently, each readout pair has
one first-feature response and one undifferentiated feature; its two
possible placements give the direct and integrated readout responses in
(12). Therefore the coefficient of $\xi^{k+1}$ in this part is

\[
\frac1n\frac{(2k+2)(2k)!}{2^k k!}\,c_a^{k+1}
\sum_l d_l^{k+1}T^{(k)}(\mathcal F(X_{la})).
\tag{29}
\]

The $l=j$ summand is the term in (27). The remaining sum is bounded by
$n(D_0/n)^{k+1}$ times a width-independent derivative bound, giving
an $O(n^{-2})$ remainder for $k\ge1$.

For completeness, the constants can be bounded in the advertised form.
There are $2k+1$ successive differentiations, each selecting one existing
factor. The set-partition expansions introduce at most
$(Ck)^{Ck}$ choices in total: there are $O(k)$ derivative endpoints and
every endpoint can be assigned a factor or a partition group in at most
$O(k)$ ways. Tanh derivatives of order $r$ are bounded by $C^r r!$,
by Cauchy's formula in a fixed strip, and their total order is $O(k)$.
Their product, the choices of marked edges, and the fixed sample sums
are consequently at most $(Ck)^{Ck}$. The same bound controls
$T^{(k)}(\mathcal F(x))$ uniformly in real $x$, by repeatedly applying
$\operatorname{sech}^2x\,\partial_x$ to tanh.

Finally,

\[
\mathbb E[G^r\operatorname{He}_p(G)]
=\frac{r!}{2^{(r-p)/2}((r-p)/2)!}
\]

when $r\ge p$ and $r-p$ is even, and is zero otherwise. This follows
from the same exponential generating function used above. Terms with
$r=p$ give $\sigma^p\sqrt{p!}$ times their ordinary coefficient;
terms of larger degree have $r\ge p+2$, and their extra powers of
$n^{-1}$ from (28) dominate the factor bounded by $(Ck)^{Ck}$.
Summing at most $2k+1$ degrees proves (27). $\square$

This lemma covers an exact response-polynomial sector and its complete
one-variable Hermite projection. It is stronger than selecting an isolated
monomial. The second-layer parameter-contraction sectors of $C_k$ remain
outside its scope. In those terms, second-layer edges identify readout
indices, carry smaller mobility, and introduce first-index sums or mixed
derivatives. Their net width factors must be counted explicitly; (27)
does not establish that they are negligible.

A possible organization of this missing count is to contract a second-layer
parameter edge before distributing its first-layer derivatives. Its shared
first-index sum contains the factor
$Q^{(1)}_{n,ab}=n^{-1}\sum_l h_{la}^{(1)}h_{lb}^{(1)}$.
An undifferentiated factor is bounded; a derivative hitting it retains a
diagonal first-neuron contraction with its explicit $1/n$. Simultaneously,
the second-layer edge identifies two readout indices. This suggests an
extra width suppression, but a complete proof must handle multiple such
edges and the resulting diagonal identifications together. Simply applying
the forest estimate to the resulting graph without proving it remains a
forest is not justified.

## The precise unfinished bridge

The new candidate mechanism is the middle-degree star, with its
single-neuron $n^{-1}$ normalization and factorial Gaussian fluctuations.
To obtain the requested actual growing-order barrier, the following facts
must still be proved for one common joint range of $k,n$:

1. Extend (27) from the all-first-layer sector to the complete conditional
   Hermite projection of the omitted neural response. The remaining
   second-layer parameter edges, their first-index sums, and mixed
   activation derivatives require their own contraction bound. The
   all-first-layer estimate already includes its background readout terms,
   repeated matrix actions, projection couplings, and Hermite
   down-contractions; those are not additional assumptions in that sector.
2. Summation over neurons retains the fluctuation lower bound with a
   probability adequate for the requested accuracy. Conditional Gaussian
   carriers are weakly correlated rather than independent. An $L^2$
   lower bound alone is not enough; growing-order fourth moments or a
   suitable small-ball bound must be checked.
3. The bound transfers to the complete prediction error under both own
   residuals on a stated physical interval. Identity (23) transfers only
   the first missed derivative. Estimate (24) exposes the loss if the
   remainder is bounded only at order one. A controlled same-scale
   remainder, or a direct projection of the complete prediction error,
   is required.

The available work does not complete any of these three bridges for the
original frozen-top hierarchy.
It therefore supports neither a necessary order $q(n)$ nor a storage lower
bound. The highest-degree nonvanishing theorem, the exact column contrast,
the scalar factorial lemma, and the restricted sector estimate (27) are
intermediate arguments; their scope should not be enlarged to a trajectory
theorem. They have been checked within this derivation but have not received
an independent complete review.
