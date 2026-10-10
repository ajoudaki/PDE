# The nonlinear frozen-top upper bound: an exact sufficient condition and its unresolved estimate

Status: bounded author derivation, 2026-10-10; not independently checked or
promoted. The sufficient-condition theorem below is proved in this note. Its
width-uniform source hypothesis is **not proved** for the full Gaussian nonlinear
network. Consequently this note does **not** establish the requested general
quasipolynomial storage upper bound.

Scientific input scope: the supervisor's self-contained assignment and the
complete `FINITE_TIME_TANH.md` and `ANALYTIC_ROUTE.md` in this study. Their linked
scientific dependencies were not retrieved. The canonical-notation skill and
its neural-network reference, rigorous-proof skill, conjecture skill and its
contract/adversarial references, `AGENTS.md`, and repository process instructions
were read. No other study, experiments, external scientific retrieval, or Git
operations were used. This file belongs to agent
`/root/nth_general_upper_scope`.

## 1. Exact model, observable, and tensor norm

Let \(v_a\in\mathbb R^d\), \(\|v_a\|_2=1\), be the training inputs, indexed
by \(a=1,\ldots,m\). Let \(\mathcal E\) be these inputs together with the
fixed test inputs whose predictions are to be controlled. Both hidden widths
are \(n\). The parameter state is
\(\theta=(W^{(1)},W^{(2)},u)\), with shapes \(n\times d,n\times n,n\).
Set

\[
z_a=W^{(1)}v_a,\qquad h_a=\phi_1(z_a),\qquad
Z_a=W^{(2)}h_a,\qquad
f_a(\theta)=\frac1n u^\top\phi_2(Z_a).
\tag{1}
\]

The activations act coordinatewise. Their assumed strip analyticity, at most
linear growth, and bounded positive real first derivatives imply smooth real
vector fields. Initialization is independent
\(W^{(1)}_{ij}\sim N(0,1)\), \(W^{(2)}_{ij}\sim N(0,1/n)\), and \(u_0=0\).
The loss, mobility, and sample source vector fields are

\[
\mathcal L(\theta)=\frac1{2m}\sum_{b=1}^m(f_b-y_b)^2,\qquad
M=\operatorname{diag}(nI,I,nI),\qquad V_b=M\nabla f_b.
\tag{2}
\]

Thus \(\dot\theta=m^{-1}\sum_b(y_b-f_b)V_b\). Put
\(\|c\|_m=(m^{-1}\sum_b|c_b|^2)^{1/2}\) and
\(Y=\|y\|_m\). Dense loss monotonicity gives
\(\|y-f(t)\|_m\le Y\). The dense trajectory exists on every finite real
interval: indeed
\(\dot{\mathcal L}=-\|M^{-1/2}\dot\theta\|_2^2\), so its length in the
fixed finite-dimensional \(M^{-1}\) metric before time \(T\) is at most
\(\sqrt{T\mathcal L(\theta_0)}\). A finite-time maximal solution therefore
has a finite limit, where the smooth vector field extends it. This existence
argument alone gives no useful width-uniform analytic bound.

Define the **ordered**, unsymmetrized hierarchy by

\[
K_{1,a}=f_a,\qquad
K_{k+2,a b_1\ldots b_k b}
=D K_{k+1,a b_1\ldots b_k}[V_b].
\tag{3}
\]

The first index may be any evaluation input in \(\mathcal E\); every later
index is a training input. The following norm specifies exactly which complete
coefficient must be estimated:

\[
\kappa_k(\theta)=
\sup_{\|c_1\|_m,\ldots,\|c_k\|_m\le1}
\max_{a\in\mathcal E}
\left|
\frac1{m^k}\sum_{b_1,\ldots,b_k=1}^m
K_{k+1,a b_1\ldots b_k}(\theta)
\prod_{j=1}^k c_{j,b_j}
\right|,\qquad k\ge1.
\tag{4}
\]

This is a multilinear operator norm of the complete tensor, with a separately
chosen sample control in each slot. It satisfies
\(\kappa_k\le\max_{a,b_1,\ldots,b_k}|K_{k+1,a b_1\ldots b_k}|\), because
\(m^{-1}\sum_b|c_{j,b}|\le\|c_j\|_m\). Thus a maximum-entry estimate is
sufficient, but an estimate of one summand or one chaos component is not.
Tensor entries may cancel inside (4), but all such cancellations must actually
be justified.

To express a source condition without prescribing the unknown dense residual,
let \(\mathcal R(S)\) consist of states reachable from \(\theta_0\) under

\[
\dot\theta=\frac1m\sum_b c_b(t)V_b(\theta),\qquad
\int\|c(t)\|_m\,dt\le S,
\tag{5}
\]

where \(c\) is any piecewise continuous real control and the trajectory exists
up to its stated endpoint. Define

\[
\overline\kappa_k(S)=\sup_{\theta\in\mathcal R(S)}\kappa_k(\theta).
\tag{6}
\]

The dense state at time \(t\le T\) belongs to \(\mathcal R(YT)\). Conditions
on (6) are properties of the original known vector fields and initialization;
they neither supply a future trajectory to the closure nor change its
coefficients. They are strong hypotheses which still need a proof.

The order-\(q\) approximation is exactly the specified frozen-top NTH:

\[
\begin{aligned}
\dot K^{(q)}_{s,a b_1\ldots b_{s-1}}
&=\frac1m\sum_b
 K^{(q)}_{s+1,a b_1\ldots b_{s-1}b}(y_b-f_b^{(q)}),
&&1\le s<q,\\
\dot K^{(q)}_q&=0,\qquad
K^{(q)}_s(0)=K_s(\theta_0),\qquad f^{(q)}=K^{(q)}_1.
\end{aligned}
\tag{7}
\]

In particular every driving residual in (7) is the approximation's own.

## 2. Exact source remainder and feedback estimate

For a training residual path \(r:[0,T]\to\mathbb R^m\), define the finite
ordered-integral map

\[
P_{q-1}[r]_a(t)=
\sum_{k=1}^{q-1}\frac1{m^k}
\sum_{b_1,\ldots,b_k}
K_{k+1,a b_1\ldots b_k}(\theta_0)
\int_{0<t_k<\cdots<t_1<t}
\prod_{j=1}^k r_{b_j}(t_j)\,dt_1\cdots dt_k.
\tag{8}
\]

The empty term is absent because \(f_a(\theta_0)=0\). The index \(b_1\)
is attached to the latest time. Reversing the times while retaining the
coefficient order would change this expression.

Repeated integration of (7) gives the exact finite identity

\[
f^{(q)}=P_{q-1}[y-f^{(q)}].
\tag{9}
\]

Repeated integration of the dense hierarchy gives

\[
f=P_{q-1}[y-f]+R_q,
\tag{10}
\]

where, writing \(r=y-f\),

\[
R_{q,a}(t)=\frac1{m^q}\sum_{b_1,\ldots,b_q}
\int_{0<t_q<\cdots<t_1<t}
K_{q+1,a b_1\ldots b_q}(\theta(t_q))
\prod_{j=1}^q r_{b_j}(t_j)\,dt_1\cdots dt_q.
\tag{11}
\]

At each substitution the evolving last tensor is integrated back to its value
at zero, producing the next ordered integral. This proves (10)--(11) after
exactly \(q\) substitutions; no infinite expansion is being presumed.
The symmetry of the scalar majorant over the time cube gives

\[
\max_a|R_{q,a}(t)|
\le\overline\kappa_q(YT)\frac{(Yt)^q}{q!},\qquad t\le T.
\tag{12}
\]

Here the factor \(q!\) is the simplex volume, and the coefficient is the full
evolving rank-\(q+1\) source. An initialized jet estimate by itself does not
bound (12).

The stability estimate also follows directly from the integrals. Let \(r,s\)
have \(\|r(t)\|_m,\|s(t)\|_m\le R\), and set
\(e(t)=\|r(t)-s(t)\|_m\). Expanding a difference of products into one
changed factor at a time yields

\[
\max_a|P_{q-1}[r]_a(t)-P_{q-1}[s]_a(t)|
\le
\left[\sum_{k=1}^{q-1}
\frac{\kappa_k(\theta_0)(Rt)^{k-1}}{(k-1)!}\right]
\int_0^t e(s)\,ds.
\tag{13}
\]

To verify the coefficient, fix the changed time \(s=t_j\). Its remaining
simplex volume is
\((t-s)^{j-1}s^{k-j}/[(j-1)!(k-j)!]\). Summing over \(j\) gives
\(t^{k-1}/(k-1)!\) by the binomial formula. This accounts for all changed
slots without a hidden factor depending on \(m\) or \(q\).

## 3. A sufficient-condition theorem for the original NTH

Fix \(T>0\), assume \(Y>0\), and define

\[
H_T=\sum_{k=1}^{\infty}
\frac{\kappa_k(\theta_0)((Y+1)T)^{k-1}}{(k-1)!},\qquad
\eta_q(T)=\overline\kappa_q(YT)\frac{(YT)^q}{q!}.
\tag{14}
\]

**Theorem.** If \(H_T<\infty\) and
\(\eta_q(T)e^{H_TT}<1\), the solution (7) exists throughout \([0,T]\)
and obeys

\[
\sup_{0\le t\le T}\max_{a\in\mathcal E}
|f_a(t)-f_a^{(q)}(t)|
\le\eta_q(T)e^{H_TT}.
\tag{15}
\]

Only terms through \(q-1\) in \(H_T\) are needed for a theorem at one rank;
the infinite sum is convenient when one wants a bound uniform in rank.

**Proof.** A local solution of the finite polynomial ODE (7) exists and is
unique. Let \(E(t)=\max_{a\in\mathcal E}|f_a(t)-f_a^{(q)}(t)|\).
As long as \(E\le1\), the training residual of the closure has norm at most
\(Y+1\), since training inputs are included in \(\mathcal E\). Its difference
from the dense residual has norm at most \(E\). Equations (9)--(13) imply

\[
E(t)\le\eta_q(T)+H_T\int_0^t E(s)\,ds
\le\eta_q(T)e^{H_Tt}.
\tag{16}
\]

For the last inequality, iteratively substitute the integral inequality;
the resulting series is \(\eta_q\sum_{j\ge0}(H_Tt)^j/j!\), with its
finite-stage remainder tending to zero on each interval where \(E\) is
continuous and bounded. Since the final bound is strictly below one,
continuity excludes a first time with \(E=1\). Bounded training residuals
also bound every stored tensor on \([0,T]\): repeatedly integrate (7), now
starting at any rank, to express it as a finite sum of initialized tensor
entries times bounded ordered integrals. Thus no stored coordinate can
diverge before \(T\), so the local solution extends to \(T\). This proves
(15), including its worst-time and test-prediction quantifiers. If \(Y=0\),
the dense and closure trajectories are stationary with zero predictions,
and the error is zero at every order. \(\square\)

A readily stated, stronger hypothesis is

\[
\overline\kappa_k(YT)\le A B^k k!\quad(k\ge1),
\qquad x=B(Y+1)T<1,
\tag{17}
\]

for constants \(A,B>0\). It implies

\[
H_T\le\frac{AB}{(1-x)^2},\qquad
\eta_q(T)\le A(BYT)^q.
\tag{18}
\]

Thus, for all sufficiently large \(q\),

\[
\sup_{t\le T,a\in\mathcal E}|f_a-f_a^{(q)}|
\le A\exp\!\left(\frac{ABT}{(1-x)^2}\right)(BYT)^q.
\tag{19}
\]

This is a geometric upper bound for the **literal original hierarchy** on
a nonzero interval independent of width whenever \(A,B,Y\) are independent
of width. For example, any fixed \(T\le[2B(Y+1)]^{-1}\) qualifies. No
physical-time Taylor surrogate, altered residual, or restart appears.

For a sequence of widths, suppose (17) holds on events of probability tending
to one with the same \(A,B,Y,T\). Set \(\vartheta=BYT<1\). Taking

\[
q\ge
\frac{\tfrac12\log n+\log(2A)+ABT/(1-x)^2}
{\log(1/\vartheta)}
\tag{20}
\]

and increasing it to at least two gives error at most \(\tfrac12n^{-1/2}\)
on those events. Literal training tensor storage is
\(\sum_{s=1}^q m^s\); each additional test input requires
\(\sum_{s=1}^q m^{s-1}\) entries. For \(m\ge2\) and a fixed number of tests,
this is \(\exp\{O(\log m\log n)\}\). If \(m\) is polynomial in \(n\),
it is \(\exp\{O((\log n)^2)\}\). For \(m=1\), storage is \(O(q)\), so
using \(\log(em)\) avoids the degenerate \(\log m=0\) notation. This counts
stored coefficients and moving coordinates, not the cost of producing the
initialized tensors from the full network.

## 4. Why the supplied tanh theorem does not verify the hypothesis

`FINITE_TIME_TANH.md` proves complete initialized high-order jet estimates
and actual finite Taylor remainders for two orthogonal training inputs, with
a time scale controlled by

\[
B_{R,n}=[C_A(R+1)\log(en)]^{C_A}.
\tag{21}
\]

Its trajectory remainder is useful for \(t\lesssim B_{R,n}^{-1}\), which
shrinks when \(R\) grows with \(n\). It does not supply an estimate of
\(\overline\kappa_q(YT)\) for fixed positive \(T\), nor a uniformly summable
sequence in (14). Even treating its rough initialized bound
\(|K_{s}(0)|\le B_{R,n}^{s}\) as a coefficient estimate would leave a
growing majorant. Such an upper estimate does not prove actual divergence;
it simply does not establish the width-independent constants in (17).

The real stability estimates in that source do not fix this issue: stability
controls propagation after an error source is bounded, whereas (11)--(12)
identify the still unbounded omitted source. Its orthogonal-input transformed
coordinates also do not automatically cover correlated input geometry.

`ANALYTIC_ROUTE.md` obtains a dimension-free factorial estimate by a polynomial
expression argument for linear activations. For nonlinear activations,
repeated differentiation also creates higher coordinatewise activation
derivatives and products of backward vectors. The linear expression count
does not bound those new factors. The obstruction is present even for tanh,
as the next two direct calculations show.

## 5. Two exact obstructions to common uniform-analytic proof routes

### 5.1 The normalized Euclidean parameter norm has unbounded higher derivatives

For a normalized first-layer vector \(a=z/\sqrt n\), write
\(\mathcal A_n(a)=\tanh(\sqrt n a)/\sqrt n\). Its second derivative is

\[
D^2\mathcal A_n(a)[h,k]
=\sqrt n\,\tanh''(\sqrt n a)\odot h\odot k.
\tag{22}
\]

As a bilinear map from \(\ell^2\times\ell^2\) to \(\ell^2\), its norm is
exactly \(\sqrt n\max_i|\tanh''(z_i)|\): the upper bound follows by
\(\|h\odot k\|_2\le\|h\|_2\|k\|_2\), and equality follows by taking
both arguments to be the same maximizing coordinate vector. At Gaussian
initialization, some \(z_i\) lie in any fixed interval on which
\(|\tanh''|\) is bounded below with probability tending to one. The norm in
(22) therefore grows at least as \(c\sqrt n\).

Equivalently, a coordinate perturbation of normalized size \(O(n^{-1/2})\)
can move a preactivation to a complex tanh pole. Hence bounded normalized
Euclidean state norms and bounded matrix operator norms do not give a
width-independent holomorphic parameter ball. This blocks that particular
ambient-ball Cauchy argument. The source directions in (3) form a much
smaller class than arbitrary coordinate directions, so (22) is not a
counterexample to (17).

### 5.2 Even a second initialized raw source jet has a Gaussian maximum

There is a stronger obstruction to simply changing to coordinate maximum
norms. Take one unit training input, both activations tanh, and write
\(z=W^{(1)}v\), \(h=\tanh z\), \(W=W^{(2)}\), \(Z=Wh\). Let
\(D= D[\,M\nabla f\,]\) be its single unit-source derivative. The exact
source rules include

\[
Dz=\operatorname{sech}^2z\odot W^\top
       (u\odot\operatorname{sech}^2Z),\qquad
Du=\tanh Z,\qquad
DW=(u\odot\operatorname{sech}^2Z)h^\top/n.
\tag{23}
\]

Since \(u_0=0\), both hidden-layer first source derivatives vanish at
initialization. Differentiating (23) once more therefore gives the complete
identity

\[
D^2z\big|_0
=\operatorname{sech}^2z\odot W_0^\top g,\qquad
g=\tanh Z\odot\operatorname{sech}^2Z.
\tag{24}
\]

**Claim.** There are fixed constants \(0<c<C<\infty\) such that

\[
\Pr\!\left\{
c\sqrt{\log n}\le\|D^2z|_0\|_\infty
\le C\sqrt{\log n}\right\}\longrightarrow1.
\tag{25}
\]

Here is a direct proof preserving the full Gaussian initialization. Put
\(Q=\|h\|_2^2/n\) and \(P=I-hh^\top/\|h\|_2^2\). Conditional on \(z,Z\),
the Gaussian row decomposition of \(W_0\) gives

\[
W_0^\top g\ \overset{d}=\ \mu h+\sigma PG,\qquad
\mu=\frac{Z^\top g}{nQ},\qquad
\sigma^2=\frac{\|g\|_2^2}{n},\qquad G\sim N(0,I_n).
\tag{26}
\]

The new \(G\) can be taken independent of the conditioning variables.
Indeed the conditioned row mean is \(Z_i h/\|h\|_2^2\) and its residual
covariance is \(P/n\), independently across rows; summing these rows with
coefficients \(g_i\) proves (26).

Let \(Q_*=\mathbb E\tanh^2(G_1)>0\). Independence and boundedness of the
first-layer variables show \(Q\ge Q_*/2\) with probability tending to
one: the variance of their empirical average is \(O(1/n)\). The set
\(I=\{j:|z_j|\le1\}\) has at least \(c_0n\) indices with probability
tending to one by the same variance calculation. On this set,
\(\operatorname{sech}^2z_j\ge\operatorname{sech}^2(1)>0\).

Conditional on \(z\), the variables \(Z_i\) are independent \(N(0,Q)\).
The continuous positive function
\(Q\mapsto\mathbb E[\tanh^2(\sqrt Q G_1)
\operatorname{sech}^4(\sqrt Q G_1)]\)
has a positive minimum on \([Q_*/2,1]\): continuity follows from bounded
convergence, and positivity from its positive integrand away from zero.
Conditional variance at most \(1/n\) then shows
\(c_1\le\sigma\le1\) with probability tending to one.
Also \(|\mu|\le C_1\) deterministically on \(Q\ge Q_*/2\), because
\(x\tanh x\operatorname{sech}^2x\) is bounded on the real line.

The projection correction obeys

\[
\|G-PG\|_\infty
\le\frac{|h^\top G|}{\|h\|_2^2},\qquad
\mathbb E\!\left[
\frac{|h^\top G|^2}{\|h\|_2^4}\,\middle|\,h\right]
=\frac1{nQ}.
\tag{27}
\]

It is consequently at most one with probability tending to one. For at
least \(c_0n\) independent standard Gaussian coordinates,
\(\max_{j\in I}|G_j|\ge\sqrt{\log n}\) with probability tending to one.
For completeness, integration of the Gaussian density on
\([s,s+s^{-1}]\), \(s\ge1\), gives a lower tail bound
\(\Pr\{G_1>s\}\ge c s^{-1}e^{-s^2/2}\); hence the probability all those
coordinates are at most \(\sqrt{\log n}\) in absolute value is at most
\(\exp[-c\sqrt n/\sqrt{\log n}]\). A union bound on the usual Gaussian
upper tail gives \(\max_j|G_j|\le C\sqrt{\log n}\) with probability tending
to one. Combining these estimates with (26)--(27), and the lower gate bound
on \(I\), proves (25).

Thus no constant independent of width can bound every raw coordinate source
jet even at order two. An argument requiring a fixed analytic majorant for
those coordinates cannot work as stated. This is a failure of that sufficient
proof route, **not** a lower bound on the scalar prediction error: (4)
contains neuron averages and complete contractions, and (25) alone says
nothing decisive about their cancellations or their high-order factorial
growth.

## 6. Precise remaining scope

The conditional implication from (14) to (15), and the Gaussian-coordinate
obstructions (22), (25), are the new results in this note. They separate three
questions that cannot be interchanged:

- **A fixed nonzero interval:** prove complete tensor bounds such as (17),
  with constants independent of \(n\), uniformly through
  \(q\asymp\log n\), on a high-probability initialization event. This would
  establish the requested literal storage upper bound on that interval.
- **An arbitrary prescribed compact interval:** prove the summability and
  geometric source decay in (14) for that interval, or supply a different
  valid source/feedback estimate for the same once-initialized hierarchy.
  Factorial bounds with arbitrary constants \(B_T\) do not suffice when
  \(B_TYT\ge1\). Dividing time into short intervals and reinitializing
  tensors would change the specified approximation and is not a proof.
- **The full nonlinear Gaussian class:** derive these estimates for learned
  hidden layers and the requested data geometry. Bounded scalar activation
  derivatives, fixed-order Gaussian limits, scalar output analyticity, and
  the available shrinking-time Taylor remainder do not establish them.

No impossibility conclusion follows from this bounded attempt. The exact
unresolved estimate is the rank-growing complete source norm in (6), together
with the initialized summability norm in (14). Establishing these in an
averaged norm that survives the Gaussian-coordinate maxima is the decisive
next proof obligation for this upper-bound route.
