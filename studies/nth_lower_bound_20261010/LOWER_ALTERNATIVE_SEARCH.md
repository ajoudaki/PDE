# Alternative lower-bound route: crossing the source-series radius

## Status and scope

This route does **not** establish a stronger lower bound for the requested
random two-hidden-layer network. It proves an exact frozen-top/own-residual
identity, a rigorous mechanism converting failure of source Taylor polynomials
into actual prediction error, and an explicit auxiliary smooth gradient example
where **every order** has error greater than $1/100$ on the fixed interval

\[
0\le t\le 1.
\]

The auxiliary example is not the specified network. Its realization by that
network, uniformly over all potentially useful orders and relative to the dense
iid discrepancy, remains an unresolved substantive gap. In particular, this
file does not claim that Taylor divergence alone proves an NTH lower bound.

This was a fresh, scientifically prompt-only scoped route. Scientific inputs
were the supervisor's assignment and elementary derivations below; no study
artifacts, maintained scientific chapters, external scientific sources, or other
route results were read. Required research/proof/presentation skills and shared
process instructions were read. No experiments or Git mutations were performed.
The only assigned write is this file. The arguments are author-derived and
self-audited; no independent check or promotion is claimed.

The target supplied in the assignment was the canonical network

\[
\begin{aligned}
z_a^{(1)}&=W^{(1)}x_a/\sqrt d,& h_a^{(1)}&=\phi_1(z_a^{(1)}),\\
z_a^{(2)}&=W^{(2)}h_a^{(1)},& h_a^{(2)}&=\phi_2(z_a^{(2)}),\\
f_a&=n^{-1}u^\top h_a^{(2)},&
\mathcal L&=\frac1{2m}\sum_{a=1}^m(f_a-y_a)^2,
\end{aligned}
\]

Here $x_a\in\mathbb R^d$, $W^{(1)}\in\mathbb R^{n\times d}$,
$W^{(2)}\in\mathbb R^{n\times n}$, and $u\in\mathbb R^n$,
with $W^{(1)}_{ij}\sim N(0,1)$, $W^{(2)}_{ij}\sim N(0,1/n)$,
$u(0)=0$, independent Gaussian entries, and mobilities $(n,1,n)$.
Only the original frozen-top hierarchy with its own residual is admissible.
One fixed smooth activation with bounded derivatives of every positive order
and one rich input family with a positive Gram gap would suffice. The target is
actual passive-test prediction error on a fixed finite interval, at an accuracy
comparable with independently initialized dense networks, with all $m,d,n$
dependencies exposed. No restart, continuation, replacement, width-dependent
activation, or storage-representation change is allowed.

## 1. Exact one-driver identity, including the own residual

Let $\theta\in\mathbb R^N$ be parameters, $M$ a fixed symmetric positive
definite mobility matrix, $f(\theta)$ a smooth training prediction, and

\[
V(\theta)=M\nabla f(\theta).
\]

For one training sample with label $y$, half-MSE gradient flow is

\[
\dot\theta=(y-f(\theta))V(\theta),\qquad \theta(0)=\theta_0.
\]

Define the source trajectory $\Theta(s)$ by

\[
\Theta'(s)=V(\Theta(s)),\qquad \Theta(0)=\theta_0,
\]

on an interval where it exists. Define its training and passive-test responses

\[
F(s)=f(\Theta(s)),\qquad G(s)=g(\Theta(s)),
\]

where $g$ is the test prediction. The scalar source clock satisfies

\[
\dot s=y-F(s),\qquad s(0)=0.
\]

The chain rule gives $\theta(t)=\Theta(s(t))$ wherever both exist; uniqueness
of the smooth ODE justifies the identification.

Write $D_VH=\nabla H\cdot V$. The exact hierarchy has training entries
$H_k=D_V^k f$ and passive entries $J_k=D_V^k g$, with

\[
\dot H_k=(y-H_0)H_{k+1},\qquad
\dot J_k=(y-H_0)J_{k+1}.
\]

Here $H_0=f$, $J_0=g$, and every coefficient is evaluated on the dense
trajectory. Along the source curve, $D_V^k f(\theta_0)=F^{(k)}(0)$ and
$D_V^k g(\theta_0)=G^{(k)}(0)$.

For an integer $p\ge0$, freeze the retained top entries $H_p,J_p$ at their
initial values, and evolve the lower entries using the closure's own residual
$y-H_0^{[p]}$. Let

\[
P_p(s)=\sum_{k=0}^p\frac{F^{(k)}(0)}{k!}s^k,
\qquad
Q_p(s)=\sum_{k=0}^p\frac{G^{(k)}(0)}{k!}s^k.
\]

Then the **exact frozen-top solution**, until its maximal existence time, is

\[
\begin{aligned}
\dot s_p&=y-P_p(s_p),&s_p(0)&=0,\\
H_k^{[p]}(t)&=P_p^{(k)}(s_p(t)),&0&\le k\le p,\\
J_k^{[p]}(t)&=Q_p^{(k)}(s_p(t)),&0&\le k\le p.
\end{aligned}
\]

Indeed the top derivatives are constants, the initial derivatives agree with
the required initialization, and differentiating each lower derivative gives
exactly its frozen-hierarchy equation. Smooth finite-dimensional ODE uniqueness
then identifies the solutions. No division by a residual is used, so residual
zeros cause no singularity in this argument. The index $p$ means polynomial
degree; converting it to an NTH convention starting with the order-two kernel
only shifts the order by a fixed integer.

Thus the actual closure prediction is $P_p(s_p(t))$, **not**
$P_p(s(t))$. A source-series argument must handle that distinction.

## 2. A quantitative transfer to actual training error

Fix $T>0$. Suppose both predictions exist on $[0,T]$, and put

\[
E_p=\sup_{0\le t\le T}|P_p(s_p(t))-F(s(t))|.
\]

Subtracting the two clock equations and integrating gives the exact estimate

\[
|s_p(t)-s(t)|
\le\int_0^t|P_p(s_p(v))-F(s(v))|\,dv
\le tE_p.
\tag{1}
\]

If $F$ is $L$-Lipschitz on the interval between $s_p(t_*)$ and
$s(t_*)$, then at any $t_*\le T$,

\[
|P_p(s_p(t_*))-F(s_p(t_*))|
\le(1+LT)E_p.
\tag{2}
\]

Consequently, if $E_p\le\varepsilon$ would force the closure clock into a
set on which

\[
|P_p(s)-F(s)|>(1+LT)\varepsilon,
\]

then the actual own-residual closure cannot attain error $\varepsilon$.
This is an observable-error transfer; it is stronger than merely observing
large Taylor coefficients.

For a test identical to the training observable, this also is passive
prediction error. It does not automatically control a distinct test observable.
With several independent training residuals there is generally no single scalar
clock, so (1) is not an already-proved reduction of the rich-data network.

## 3. An explicit all-orders failure in an auxiliary smooth gradient model

Define a scalar source response

\[
F(s)=2s-\arctan s.
\tag{3}
\]

It is odd and satisfies

\[
F'(s)=2-\frac1{1+s^2}=\frac{1+2s^2}{1+s^2}\in[1,2].
\]

It therefore defines the response of an actual scalar gradient system. To see
this without imposing a response by external forcing, define

\[
A(s)=\int_0^s\sqrt{F'(r)}\,dr,
\qquad
\mathfrak f(\theta)=F(A^{-1}(\theta)).
\tag{4}
\]

Since $1\le A'(s)\le\sqrt2$, $A$ is a smooth increasing diffeomorphism
of $\mathbb R$. The chain rule gives

\[
\mathfrak f'(A(s))=\sqrt{F'(s)}=A'(s).
\]

Thus $\Theta(s)=A(s)$ solves $\Theta'=\mathfrak f'(\Theta)$,
$\Theta(0)=0$, and its prediction is exactly $F(s)$.

The fixed function $\mathfrak f$ is smooth and has bounded derivatives of
every positive order. For completeness, put $a(s)=\sqrt{F'(s)}$.
The function $a$, its reciprocal, and all their derivatives are bounded:
their formulas are derivatives of a smooth positive rational square root,
with denominator bounded away from zero, and have finite limits at infinity
(zero for positive-order derivatives). Derivatives in the coordinate
$\theta=A(s)$ are produced by $a(s)^{-1}d/ds$. Repeatedly applying that
operator to $\mathfrak f'(A(s))=a(s)$ produces finite sums of products of
those bounded derivatives. This proves the claimed regularity for each order.
No width-dependent function is involved.

Take label $y=4$, mobility $1$, and $\theta(0)=0$. The actual physical
gradient flow is

\[
\dot\theta=(4-\mathfrak f(\theta))\mathfrak f'(\theta).
\]

Its source clock obeys

\[
\dot s=4-F(s),\qquad s(0)=0.
\]

Because $F'\in[1,2]$, this scalar ODE is globally Lipschitz and has a unique
global solution. The clock remains nonnegative. Since $F(s)\le2s$ for
$s\ge0$, integrating $\dot s+2s\ge4$ yields

\[
s(t)\ge2(1-e^{-2t}).
\]

In particular, using $e^2>7$,

\[
s(1)>\frac{12}{7}.
\tag{5}
\]

**Proposition.** For every retained polynomial degree $p\ge0$, the original
frozen-top hierarchy initialized from this scalar gradient model either does
not exist on all of $[0,1]$, or satisfies

\[
\sup_{0\le t\le1}
|H_0^{[p]}(t)-\mathfrak f(\theta(t))|>\frac1{100}.
\tag{6}
\]

**Proof.** For $p=0$, $H_0^{[0]}=0$, whereas (3) and (5) give
$F(s(1))\ge s(1)>12/7$.

For $p\ge1$, let $J=\lfloor(p-1)/2\rfloor$ and define

\[
B_J(s)=\sum_{j=0}^{J}\frac{(-1)^j s^{2j+1}}{2j+1}.
\]

The degree-$p$ Taylor polynomial of (3) is $P_p(s)=2s-B_J(s)$.
The finite geometric-sum identity gives

\[
\begin{aligned}
B_J'(s)-\frac1{1+s^2}
 &=\frac{(-1)^J s^{2J+2}}{1+s^2},\\
B_J(s)-\arctan s
 &=(-1)^J\int_0^s\frac{z^{2J+2}}{1+z^2}\,dz.
\end{aligned}
\tag{7}
\]

This is an exact real-variable remainder identity, with no convergence
assumption. At every $s\ge3/2$ and every $J\ge0$, it implies

\[
\begin{aligned}
|P_p(s)-F(s)|
&\ge\int_{5/4}^{3/2}\frac{z^{2J+2}}{1+z^2}\,dz\\
&\ge\frac14\frac{(5/4)^2}{1+(3/2)^2}
=\frac{25}{208}.
\end{aligned}
\tag{8}
\]

Suppose the closure exists on $[0,1]$ and its error $E_p$ is at most
$1/100$. Equation (1) and (5) imply

\[
s_p(1)>\frac{12}{7}-\frac1{100}>\frac32.
\]

Since $F$ is globally $2$-Lipschitz, (2) gives

\[
|P_p(s_p(1))-F(s_p(1))|\le3E_p\le\frac3{100},
\]

contradicting (8), since $25/208>3/100$. This proves (6). $\square$

The example uses its own residual throughout. It uses a fixed label, function,
and physical horizon. The conclusion covers every finite order, including
orders chosen as a function of another scale, and is not a statement only
about the limit of Taylor polynomials evaluated on the dense clock.

Nevertheless, (4) is a scalar parameterized predictor, not a realization of
the canonical two-hidden-layer architecture. Its mathematical force is a
counterexample to a general inference from smoothness or local hierarchy
correctness to fixed-horizon frozen-top convergence. It does not settle the
specific network question.

## 4. A constraint imposed by the canonical zero readout

The zero readout imposes a local constraint which a candidate embedding must
respect. Let $v$ collect all hidden parameters, let their mobility be the
fixed positive matrix $M_v$, and write a scalar training contrast as

\[
f(u,v)=\frac1n u^\top h(v).
\]

For an individual sample, $h(v)=h_a^{(2)}(v)$. For a fixed signed contrast
$\sum_a c_a f_a$, it is $h(v)=\sum_a c_a h_a^{(2)}(v)$. The readout
mobility is $n$, as in the canonical model. The source equations are

\[
u'=h(v),\qquad
v'=\frac1n M_v Dh(v)^\top u,
\qquad u(0)=0.
\tag{9}
\]

Write $h_0=h(v_0)$ and

\[
b=\frac1nM_vDh(v_0)^\top h_0.
\]

Differentiating (9) at zero gives

\[
u'(0)=h_0,\quad u''(0)=0,\quad u'''(0)=Dh(v_0)b,
\qquad v'(0)=0,\quad v''(0)=b.
\]

For the source response $F(s)=f(u(s),v(s))$, Taylor multiplication therefore
gives

\[
\begin{aligned}
F(s)
&=\frac1n\left(s h_0+\frac{s^3}{6}Dh(v_0)b+o(s^3)\right)^\top
\left(h_0+\frac{s^2}{2}Dh(v_0)b+o(s^2)\right)\\
&=\frac{\|h_0\|^2}{n}s
+\frac{2}{3n}h_0^\top Dh(v_0)b\,s^3+o(s^3).
\end{aligned}
\]

In particular,

\[
F'''(0)=\frac4{n^2}
\left\|M_v^{1/2}Dh(v_0)^\top h_0\right\|^2\ge0.
\tag{10}
\]

Moreover, changing $(s,u,v)$ to $(-s,-u,v)$ preserves (9) and its
initial data. Uniqueness implies that $u$ is odd and $v$ is even in
source time, and consequently $F$ is odd on its local existence interval.

The tempting response $F(s)=\arctan s$ has $F'''(0)=-2$, so it cannot
literally be this canonical source response. This is why the explicit
prototype above uses $2s-\arctan s$, whose third derivative is $2$.
That modification satisfies the necessary third-order sign condition;
satisfying a necessary condition is not an embedding proof.

Equation (10) is deterministic and valid for every width and hidden
initialization under the displayed parameterization. It does not assert that
the residual vector of a rich multi-sample training problem remains in one
fixed contrast direction.

## 5. Decisive unresolved bridges

The route would yield an all-orders lower bound, stronger than a
super-quasipolynomial literal-array bound, if the following bridges were proved
for one admissible network family. They are not proved here.

1. **Canonical response realization.** Find a fixed admitted activation and
   the specified Gaussian initialization for which a relevant scalar source
   response has a lower remainder bound such as (8) on a source interval
   reached in fixed physical time. An arbitrary smooth gradient predictor
   does not supply this. A nonanalytic activation or a finite complex radius
   alone does not supply a lower remainder bound.
2. **Rich data and residual geometry.** Preserve a positive-Gram-gap family
   with explicit $m(n),d(n)$, while either proving a one-driver reduction or
   proving a replacement of (1)–(2) for the actual multiple residuals. Taking
   all training inputs equal or treating the residual path as an externally
   prescribed control does not establish the required result.
3. **A genuine passive test.** Prove the error transfer for the designated
   held-out prediction. Training error controls the clock in (1); accuracy of
   one unrelated passive output need not control the training residual.
   Duplicating the training observable in the auxiliary construction does not
   resolve the intended generalization observable.
4. **All relevant orders at finite width.** An infinite-width response theorem
   plus convergence of each fixed NTH coefficient does not cover an arbitrary
   order $p=p(n)$. High derivatives may have large initialization errors, and
   those errors may alter the closure rather than merely perturb a divergent
   Taylor polynomial. A bound uniform in the orders claimed to fail, or a
   separate argument for all larger orders, is necessary.
5. **Comparison with iid dense discrepancy.** Establish the dense-dense
   fluctuation scale for the same activation, input family, test, time horizon,
   and probability event, then compare the actual closure error with it. No
   concentration or finite-width probability theorem was proved in this route.

In particular there is no admissible $m(n),d(n)$, success probability, or
width-dependent storage lower bound to report from this file. Assigning those
quantities from the auxiliary scalar model would change the research contract.

## 6. What this route establishes

| Claim | Status | Scope |
|---|---|---|
| Frozen-top hierarchy equals source Taylor polynomials evaluated on its own clock | Proved here | One training driver; arbitrary smooth finite-dimensional gradient predictor |
| Small actual training error forces a close residual clock | Proved here | Equation (1), with its exact factor $T$ |
| Fixed-time error $>1/100$ for every frozen order | Proved here | The auxiliary scalar predictor (4), label $4$, $T=1$ |
| Canonical zero readout forces odd source response and nonnegative third derivative | Proved here | Every realization of (9), including the stated network's fixed sample contrasts |
| Stronger width lower bound for the canonical random network | Open | All five bridges above remain relevant |
| Broad matching upper for the canonical class | Not established | No upper theorem is inferred from failure of this lower route |

The most useful retained result is the quantitative own-residual transfer
(1)–(2), together with the explicit remainder mechanism (7)–(8). The most
important limitation is the missing canonical realization, before any claimed
asymptotic storage consequence.
