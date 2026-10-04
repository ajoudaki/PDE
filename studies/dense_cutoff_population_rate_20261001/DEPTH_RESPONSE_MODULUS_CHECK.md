# Check of the depth response modulus and reinsertion trace

2026-10-03. Internal collaborator reconstruction, not an isolated promotion
review. The checked source is DEPTH_RESPONSE_MODULUS.md, read-version SHA-256
10691c87fac22a0c43361e0a9a1fdf65c3638a273364921e4625384331882950.
After the coordinator added the regularity qualification identified below,
the complete source was reread and verified at final SHA-256
e32e3608e5a02d6f9aefb88cf77890f9110a8d65bede6faedf2f215d84dc6d24.

The checker reconstructed the complete candidate, equations (1)–(10), from
the current paper's finite forward/backward recursions and physical bounds,
the complete FINITE_MIXED_MOMENT_ROUTE.md and its check, and the complete
Q_ORDER_POSITIVE_ROUTE.md. The mathematical skills and current shared
instructions were applied. No new cavity-extension candidate, experiment,
other study, manuscript edit, or Git write was used.

**Verdict:** the time modulus, Gaussian entropy and subpower budget
dependence check under the stated bounded-slope and Lipschitz-gate
assumptions. The endpoint Schatten and trace estimates check with the
classical $C^2$ activation regularity and bounded continuous second
derivative now explicitly required in that section. Without this
qualification, its named derivatives
and Hessians are not defined at every permitted parameter state. No
additional size, rank, normalization or series-convergence gap was found.
This does not establish an insertion lemma or a finite carrier budget.

## 1. Precise objects and a regularity correction

Let the fixed-depth dense model and fixed finite dataset be those of the
current paper. Set $\mathcal F_a=nf_a=w^\top h_a^{(L)}$ and use the
mobility-Euclidean parameter coordinates

\[
\Theta=(W^{(1)},H^{(2)},\ldots,H^{(L)},w),\qquad
H^{(\ell)}=\sqrt n\,W^{(\ell)}.
\]

The parameter space has its ordinary sum-of-squares norm. Vector RMS
normalizations are always displayed below. Let $S\in(0,1]$ be a fixed
multiple of the small label RMS. The physical tube supplies bounded hidden
operator norms and training-feature RMS, backward/carrier RMS at most
$CS$, and residual activity at most $CS$. The full carriers are

\[
k_a^{(L)}=w,\qquad
k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)}.
\]

The candidate assumes, on the reference interval,

\[
\sup_t\frac1n\sum_{\ell,i}
\exp\{\eta \max_a|k_{a,i}^{(\ell)}(t)|/S\}\le B,\qquad\eta>0.
\tag{C1}
\]

In particular $B\ge L\ge1$. Constants below may depend on the fixed depth,
data and activation bounds and on $\eta$, but not on width or $B$.

For the modulus and Gaussian conclusions, $\phi_\ell\in C^1$ with bounded,
globally Lipschitz $\phi_\ell'$ is sufficient. For the candidate's
$B_a^{(j)}=D_\Theta\delta_a^{(j)}$, its classical Hessians and its
variational propagator, assume additionally $\phi_\ell\in C^2$ with
bounded $\phi_\ell''$. This gives a continuously differentiable vector
field and the ordinary first variational equation at fixed finite width.
No third derivative is needed for the present trace lemma.

The distinction is substantive. For example the softsign activation
$\phi(z)=z/(1+|z|)$ is $C^1$ with bounded Lipschitz derivative, but
$\phi'(z)=(1+|z|)^{-2}$ is not differentiable at zero. At a state with
a nonzero carrier and a zero preactivation, $D_\Theta\delta$ need not
exist. Such states are not excluded by the candidate's tube or budget.
An almost-everywhere or smoothing version would require a separately
stated passage for the response maps; it is not automatic from the
modulus calculation.

## 2. Tail and time modulus

For $x\ge0$,

\[
x^2\mathbf1_{\{x>r\}}
\le \left(\sup_{x\ge0}x^2e^{-\eta x/2}\right)
e^{-\eta r/2}e^{\eta x}.
\]

Apply this with $x=|k_{a,i}^{(\ell)}|/S$, sum coordinates and use (C1).
Taking a square root proves the candidate's tail bound

\[
\frac{\|k_a^{(\ell)}\mathbf1_{\{|k_a^{(\ell)}|>R\}}\|_2}{\sqrt n}
\le C_\eta S\sqrt B\,e^{-\eta R/(4S)}.
\tag{C2}
\]

Choose a monotone activity coordinate $s(t)\in[0,1]$ by dividing
accumulated residual activity by a fixed upper bound $CS$. The physical
speeds then give

\[
d_n(\theta(t),\theta(u))\le CS|s(t)-s(u)|.
\]

The changed-gate term in backward subtraction is bounded by

\[
\frac{\|[\phi_\ell'(z(t))-\phi_\ell'(z(u))]\odot k(u)\|_2}{\sqrt n}
\le jR\frac{\|z(t)-z(u)\|_2}{\sqrt n}
+2s_*\frac{\|k(u)\mathbf1_{\{|k(u)|>R\}}\|_2}{\sqrt n}.
\]

All other multipliers are bounded operators or slopes. Forward
subtraction followed by downward induction yields the candidate's (3).
It has one power of $R$, since an already estimated backward difference
is propagated only through bounded operators and slopes.

Put $v=|s(t)-s(u)|\in(0,1]$ and choose
$R=(4S/\eta)\log(e\sqrt B/v)$. The tail in (C2) becomes $C_\eta Sv$.
After division by $S$, the result is

\[
\frac{\|\delta_a^{(\ell)}(t)-\delta_a^{(\ell)}(u)\|_2}{S\sqrt n}
\le C_\eta v[1+S\log(e+B)+S\log(e/v)].
\tag{C3}
\]

Since $\sqrt v\log(e/v)$ is bounded on $(0,1]$ and $S\le1$, (C3)
is at most $H_B\sqrt v$, where

\[
H_B=C_\eta[1+S\log(e+B)].
\]

At $v=0$ the parameter-speed inequality gives equality of the states,
so the limiting statement is valid. The normalized response also has
uniform norm at most $C$. Freezing the path at any reference-measurable
stop preserves the bound, because $s(t\wedge\sigma)$ remains monotone
and its increments are no larger than those of $s(t)$.

## 3. Gaussian supremum and the dependence on the budget

Condition on a reference path independent of
$x\sim N(0,I_n/n)$. The centered Gaussian process
$X_t=x^\top\delta_a^{(\ell)}(t)/S$ has canonical distance

\[
\left(\mathbb E[|X_t-X_u|^2\mid\text{reference}]\right)^{1/2}
=\frac{\|\delta_a^{(\ell)}(t)-\delta_a^{(\ell)}(u)\|_2}{S\sqrt n}.
\]

Its diameter is bounded by $C$, and (C3) supplies a covering by
$1+CH_B^2/\epsilon^2$ points at metric radius $\epsilon$. This proves
the candidate's (5). There is no dependence on the number of physical
time steps or on the duration of the reference interval.

Here is an explicit dyadic justification of the stated Gaussian tail.
Take metric nets at radii $2^{-j}$, starting at a fixed bounded scale.
There are at most $C H_B^2 4^j$ points at level $j$. Pair every point
with a nearest parent in the previous level. The corresponding centered
Gaussian increments have standard deviations at most $C2^{-j}$ and
there are at most $CH_B^4 16^j$ possible pairs. Gaussian scalar tails
and a union bound imply that, outside an event of probability at most
$Ce^{-cu^2}$, every increment is bounded by

\[
C2^{-j}\left[
\sqrt{\log(e+H_B)}+\sqrt{j+1}+u\sqrt{j+1}\right].
\]

The series over $j$ is summable. A single starting-point Gaussian has
bounded variance from the RMS tube. The path is continuous and separable
in this metric; at finite width its Gaussian realization is a continuous
linear functional of the response path. Passing from the nets to the
complete compactified activity interval is therefore valid. We obtain

\[
\Pr\left\{\sup_t|X_t|>
C_\eta[1+\sqrt{\log(e+S\log(e+B))}]+u
\,\middle|\,\text{reference}\right\}
\le Ce^{-cu^2}.
\tag{C4}
\]

The finite maximum over samples and layers changes only the fixed
constants. Integrating this tail gives, for each fixed $\lambda\ge0$,

\[
\mathbb E\left[e^{\lambda\sup_t|X_t|}
\,\middle|\,\text{reference}\right]
\le C_{\lambda,\eta}
\exp\left\{C_{\lambda,\eta}
\sqrt{\log(e+S\log(e+B))}\right\}.
\tag{C5}
\]

Uniformly over $0<S\le1$, this is bounded by
$C_{\lambda,\eta}\exp(C_{\lambda,\eta}\sqrt{\log(e+B)})$.
Consequently its logarithm divided by $\log B$ tends to zero as
$B\to\infty$, which verifies $L_\eta(B)=B^{o(1)}$. In fact the stronger
square-root-logarithm-of-logarithm dependence retained in (C5) is also
available, but not needed for selecting a fixed budget.

For two independently defined cavity paths, the radial projection of
their difference onto a deterministic Euclidean ball is 1-Lipschitz and
remains independent of an omitted column when both paths do. If the two
paths have different activity coordinates, use the monotone sum of those
coordinates to cover their difference; its total range is at most two.
This yields the same polynomial entropy with fixed $B$-dependent
constants. If the projected path has Gaussian radius at most $D_n$,
start the dyadic argument at that radius. Its mean supremum is then

\[
O\!\left(D_n\sqrt{\log(e+H_B/D_n)}\right),
\]

and its tail is sub-Gaussian on scale $D_n$. This verifies the asserted
small-diameter consequence, conditional on a polynomially small radius
having separately been proved. It does not prove that radius.

## 4. The full-depth Hessian and endpoint response maps

Write

\[
Z_{a,\ell}=D_\Theta z_a^{(\ell)}.
\]

For a parameter variation $U$, the forward variations obey

\[
Z_{a,1}U=U_{W^{(1)}}v_a,\qquad
Z_{a,\ell}U=\frac{U_{H^{(\ell)}}h_a^{(\ell-1)}}{\sqrt n}
+W^{(\ell)}\operatorname{diag}(\phi_{\ell-1}')Z_{a,\ell-1}U.
\tag{C6}
\]

The training-feature RMS and hidden operator bounds imply
$\|Z_{a,\ell}\|_{\rm op}\le C$ for all fixed layers. This uses
ordinary Euclidean norms in the domain and target, not normalized
parameter norms.

For $B_a^{(j)}=D_\Theta\delta_a^{(j)}$, differentiation gives precisely
the candidate's (7):

\[
\begin{aligned}
B_a^{(j)}U={}&
\operatorname{diag}(\phi_j')W^{(j+1)\top}B_a^{(j+1)}U\\
&+\operatorname{diag}(\phi_j')
\left(U_{H^{(j+1)}}/\sqrt n\right)^\top\delta_a^{(j+1)}
+\operatorname{diag}(k_a^{(j)}\phi_j'')Z_{a,j}U.
\end{aligned}
\tag{C7}
\]

At the top the first two terms are replaced by
$\operatorname{diag}(\phi_L')U_w$. The middle map in (C7) has operator
norm at most $C\|\delta_a^{(j+1)}\|_2/\sqrt n\le CS$ and output rank
at most $n$.

Define normalized Schatten norms by
$\|T\|_{p,n}=n^{-1/p}\|T\|_p$ for every compatible finite rectangular
operator. From $x^p\le(p/(e\eta))^p e^{\eta x}$ and (C1),

\[
\|\operatorname{diag}(k_a^{(j)})\|_{p,n}
\le C_\eta SpB^{1/p},\qquad p\ge2.
\tag{C8}
\]

Multiplication by bounded operators does not increase this norm beyond
their operator factors. The bounded-rank pieces in (C7) have normalized
Schatten norms at most their operator norms. Downward induction therefore
proves

\[
\|B_a^{(j)}\|_{p,n}\le C[1+SpB^{1/p}],
\]

with a constant independent of $p,n,B$.

For completeness, the scalar Hessian at arbitrary fixed depth is

\[
\begin{aligned}
D^2\mathcal F_a[U,V]={}&
U_w^\top\operatorname{diag}(\phi_L')Z_{a,L}V
+V_w^\top\operatorname{diag}(\phi_L')Z_{a,L}U\\
&+\sum_{\ell=1}^L
(Z_{a,\ell}U)^\top\operatorname{diag}(k_a^{(\ell)}\phi_\ell'')
Z_{a,\ell}V\\
&+\sum_{\ell=2}^L\frac{\delta_a^{(\ell)\top}}{\sqrt n}
\left[
U_{H^{(\ell)}}\operatorname{diag}(\phi_{\ell-1}')Z_{a,\ell-1}V
+V_{H^{(\ell)}}\operatorname{diag}(\phi_{\ell-1}')Z_{a,\ell-1}U
\right].
\end{aligned}
\tag{C9}
\]

All gates in these equations are evaluated at their displayed layer
preactivations for sample $a$. Formula (C9) follows by the forward second
variation and then backpropagating each activation curvature. In
particular it retains mixed terms from different parameter blocks through
$Z_{a,\ell-1}$.

Each curvature summand is a bounded forward-map contraction of a
diagonal carrier matrix, with rank at most $n$ and the norm bound (C8).
The readout mixed pair has rank at most $2n$ and bounded operator norm.
Each hidden mixed pair factors through an $n$-dimensional vector space,
has rank at most $2n$, and has operator norm at most $CS$ because
$U_H\mapsto U_H^\top\delta/\sqrt n$ has that norm. Thus the total rank
is $O(n)$, with constants depending only on fixed depth and sample count.
The parameter-space dimension $O(n^2)$ introduces no additional factor.

In the variational flow, write the residual-Hessian coefficient as
$\mathcal H(t)d\mu(t)$, where

\[
d\mu(t)=\frac2m\sum_a|r_a(t)|dt,\qquad
\mathcal H(t)=-\sum_a
\frac{r_a(t)}{\sum_b|r_b(t)|}D^2\mathcal F_a(t)
\]

when the denominator is nonzero, and put $\mathcal H=0$ otherwise.
Since the absolute values of the displayed coefficients sum to one,
(C9) proves

\[
\|\mathcal H(t)\|_{p,n}\le C[1+SpB^{1/p}].
\tag{C10}
\]

This verifies both bounds in candidate (8).

## 5. The endpoint trace series

The exact first variational equation in these coordinates is

\[
\partial_tJ(t,s)=
\left[-\frac2{mn}\sum_a\nabla\mathcal F_a\nabla\mathcal F_a^\top
-\frac2m\sum_a r_a D^2\mathcal F_a\right]J(t,s).
\tag{C11}
\]

Let $U_0(t,s)$ be the propagator of the first, negative-semidefinite
coefficient. Its operator norm is at most one, by differentiating the
squared norm of a solution. This term is the adaptive residual
contribution; it has not been discarded.

Expand $J(t,s)$ in a Duhamel series in the second coefficient around
$U_0$. A term with $r$ residual Hessians contains $r+2$ noncontraction
factors after multiplying by $B_b^{(j)}(t)$ and $B_a^{(j)}(s)^\top$.
Finite rectangular Schatten Hölder at exponent $p=r+2$ gives

\[
\frac1n|\operatorname{tr}(B_bU_0\mathcal H_1U_0\cdots
\mathcal H_rU_0B_a^\top)|
\le
\|B_b\|_{r+2,n}\|B_a\|_{r+2,n}
\prod_{i=1}^r\|\mathcal H_i\|_{r+2,n}.
\tag{C12}
\]

To verify the normalization, the ordinary trace estimate has a product
of $r+2$ Schatten norms, each contributing $n^{1/(r+2)}$. Their
product is exactly $n$, canceling the displayed $1/n$. Intervening
contractions cost at most one. No Schatten norm of the full parameter
identity is taken.

The total activity is $O(S)$, and the outer forcing integral satisfies
$\int|r_a(s)|ds\le CS$ for fixed sample count. The ordered integral
for $r$ insertions is at most $(CS)^r/r!$. Using (C10) and the
endpoint bound therefore proves the candidate's first inequality in
(10):

\[
\frac1n\left|\operatorname{tr}
\int_0^t r_a(s)B_b^{(j)}(t)J(t,s)B_a^{(j)}(s)^\top a(s)ds\right|
\le CS\sum_{r\ge0}\frac{(CS)^r}{r!}
[1+S(r+2)B^{1/(r+2)}]^{r+2}.
\tag{C13}
\]

The control has bounded amplitude; it can change sign. Applying absolute
values before the scalar time integrals justifies that case as well.
The supremum-in-time budget is essential here: a mere integrated budget
does not bound the two endpoint $B$ factors.

For $p=r+2$, $(1+x)^p\le2^{p-1}(1+x^p)$. The part without $x^p$
sums to at most $CS$ for $S\le1$. The other part is bounded by

\[
CS^3B\sum_{r\ge0}(CS^2)^r\frac{(r+2)^{r+2}}{r!}.
\]

For $r\ge1$, $r!\ge(r/e)^r$ and
$(1+2/r)^r\le e^2$, so the ratio is at most
$C e^r(r+2)^2$. The series is therefore bounded by a fixed constant
once $CS^2$ is sufficiently small. Its $r=0$ term is finite separately.
This proves the claimed $CS+CS^3B$ bound, with the smallness threshold
independent of $B$. At each fixed finite width the Duhamel expansion
already converges on compact times by continuity of the coefficients;
the preceding summable majorant justifies the uniform estimate and its
all-time extension.

The rank-one adaptive forcing is a separate term. For an external
preactivation at layer $j$, it is proportional to

\[
P_a=-\frac2{mn}\nabla\mathcal F_a\,\delta_a^{(j)\top},
\qquad \operatorname{rank}P_a\le1,\qquad \|P_a\|_{\rm op}\le CS.
\]

Consequently its normalized trace after applying $B_bJ$ is at most
$CS\,\|B_b\|_{\rm op}\|J\|_{\rm op}/n$ per unit physical time.
On a logarithmic horizon a bound $\|J\|_{\rm op}\le n^\varepsilon$,
$\varepsilon<1$, and a polylogarithmic endpoint bound make its
integral $o(1)$. The candidate correctly states this as depending on
the weak operator estimate; it is not included in (C13).

For the current budget one can also see its compatibility directly:
(C1) implies $\max_{\ell,a,i}|k_{a,i}^{(\ell)}|\le
(S/\eta)\log(nB)$. The Hessian operator bound from (C9) and total
activity give
$\|J\|_{\rm op}\le C\exp(CS^2\log(nB)/\eta)$, and the endpoint
operator norm is $O(1+S\log(nB))$. For fixed $B$ and sufficiently
small fixed $S$, these meet the preceding requirement.

## 6. The direct external derivative

Hold parameters fixed and insert an additive external preactivation
$e\in\mathbb R^n$ at layer $j$. Let
$P_{\ell,j}=D_e z_a^{(\ell)}$ at $e=0$. Then
$P_{j,j}=I$, while for $\ell>j$,

\[
P_{\ell,j}=W^{(\ell)}
\operatorname{diag}(\phi_{\ell-1}')P_{\ell-1,j},
\qquad \|P_{\ell,j}\|_{\rm op}\le C.
\]

Since $D_e\mathcal F_a=\delta_a^{(j)}$, a second forward variation
with the weights and readout fixed gives

\[
D_e\delta_a^{(j)}
=\sum_{\ell=j}^L
P_{\ell,j}^\top\operatorname{diag}(k_a^{(\ell)}\phi_\ell'')
P_{\ell,j}.
\tag{C14}
\]

There are no parameter-weight or readout-variation cross terms in this
particular derivative. For every summand,

\[
\begin{aligned}
\frac1n|\operatorname{tr}(P_{\ell,j}^\top
\operatorname{diag}(k_a^{(\ell)}\phi_\ell'')P_{\ell,j})|
&\le \frac{\|P_{\ell,j}\|_{\rm op}^2}{n}
\sum_i|k_{a,i}^{(\ell)}\phi_\ell''(z_{a,i}^{(\ell)})|\\
&\le C\|k_a^{(\ell)}\|_2/\sqrt n
\le CS.
\end{aligned}
\]

Summing the fixed number of layers proves the direct normalized trace
bound claimed after candidate (10). It needs only the carrier RMS tube,
not the exponential budget, apart from the classical differentiability
qualification already stated.

## 7. What this check establishes

After the $C^2$ qualification, the candidate supplies a complete
conditional deterministic modulus, conditional Gaussian supremum
estimate, and conditional endpoint trace bound. The constants controlling
the Gaussian exponential moment grow subpolynomially in $B$. Therefore
one can choose a sufficiently large fixed budget first and only then
choose $S$ small enough that

\[
L_\eta(B)\exp\{C_\eta(1+S^2B)\}<B
\]

with a strict margin (or the same inequality with any prescribed fixed
multiplicative safety factor). This verifies the proposed order of
constant selection. It does not assert that a finite-network budget
actually satisfies a recursive inequality with this base.

The remaining insertion obligation includes the full retained adaptive
dynamics, both directions of a deleted middle-layer neuron, uniform
control nets, nonlinear remainders, and the correct omitted-root
independence through stopping and projection. None of those is established
by a time modulus or a trace estimate alone. The source expressly retains
that limitation, and this check does likewise.
