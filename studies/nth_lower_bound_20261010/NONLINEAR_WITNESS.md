# A nonlinear first-layer witness with a source blowup and stable real coordinates

Current status: supporting mechanism and parameter-transfer note. The
combined growing-order result is being assembled in
[NONLINEAR_RESULT.md](NONLINEAR_RESULT.md); use that report for the final
theorem, its Gaussian initialized-jet input, and its exact scope. The
successful parameter route uses the original hierarchy's physical jets
and a finite real-time Taylor remainder. It does not use the source-blowup
continuation route or inherit that route's unresolved requirements.

This theory-only scoped route proves an exact nonlinear source-flow mechanism
inside the canonical Gaussian two-hidden-layer architecture. It also proves a
local comparison of its actual two-input training dynamics with a single-source
reference. Sections (22)--(36) supply the fixed-parameter algebraic transfer
and its quantitative error implication. Those sections state the initialized
jet and dense remainder inputs explicitly rather than reproving them here;
the complete assembly belongs to NONLINEAR_RESULT.md.

The model is an explicit alternative witness: its first hidden activation is
genuinely nonlinear and its second activation is the identity. It is not a
theorem about two tanh layers. The Gaussian initialization, mobilities, zero
readout, fixed labels, and positive population feature Gram are retained.
No low-rank initialization, width-dependent activation or labels, numerical
experiment, or Git operation is used.

Scientific inputs were the supervisor's assignment, the complete permitted
RESULT.md, STRONGER_SOURCE.md, POLYNOMIAL_UPPER.md, and
STRONG_NONLINEAR_SEARCH.md, the maintained notation and reading guide, and the
already-read complete setup of the maintained trajectory-compression chapter.
A search of the local-population chapter identified no quantitative theorem
used here. No other study or another new route's report was read.

## The nonlinear canonical model

Fix $\varepsilon=1/4$ and define

\[
\phi(z)=z+\varepsilon\sin z.
\]

Take $m=d=2$, unit inputs $v_1=e_1,v_2=e_2$, and fixed labels
$y=(\eta,0)$, with $0<\eta\le10^{-62}$. The actual input vectors in the book's
normalization are $x_a=\sqrt2v_a$. Use

\[
z_a=W^{(1)}v_a,\qquad
h_a^{(1)}=\phi(z_a),\qquad
h_a^{(2)}=W^{(2)}h_a^{(1)},\qquad
f_a=\frac{u^\top h_a^{(2)}}n.
\]

The activation acts componentwise. The initialized entries of $W^{(1)}$ and
$W^{(2)}$ are independent $N(0,1)$ and $N(0,1/n)$, respectively; $u(0)=0$.
The mobility blocks are $(n,1,n)$ and the loss is
$\mathcal L=((f_1-\eta)^2+f_2^2)/4$.

Both activations satisfy the strip condition. The first is entire and
$|\phi'(z)|\le1+\varepsilon\cosh a$ on $|\operatorname{Im}z|\le a$.
For the chapter's parameter choice $a=2$, all its defining quantities for
$\beta$ are at most ten, so $\beta=10$. On the real line,

\[
\frac34\le\phi'(z)\le\frac54,\qquad
\frac34|z|\le|\phi(z)|\le\frac54|z|.
\tag{1}
\]

Oddness and independence of the two first-layer Gaussian projections give

\[
Q^{(1)}=Q^{(2)}=\mu_2 I_2,\qquad
\mu_2=\mathbb E[\phi(G)^2]\ge9/16,\qquad G\sim N(0,1).
\tag{2}
\]

Thus the population gap is positive, and the stated fixed label range
satisfies the maintained small-label condition.

The nonlinearity is nonzero on the actual initialized distribution. Its
squared distance from the best affine function of a standard Gaussian is

\[
\inf_{\alpha,b}\mathbb E|\phi(G)-\alpha G-b|^2
=\varepsilon^2\left(\frac{1-e^{-2}}2-e^{-1}\right)>0.
\tag{3}
\]

To check this, oddness gives $b=0$, Gaussian integration by parts gives
$\mathbb E[G\sin G]=e^{-1/2}$, and
$\mathbb E\sin^2G=(1-e^{-2})/2$. The constant in (3) is fixed independently
of width.

## Exact transformed coordinates

Define an increasing odd real diffeomorphism and its associated activation by

\[
T(z)=\int_0^z\frac{dr}{\phi'(r)},\qquad
\chi=\phi\circ T^{-1}.
\]

Equation (1) gives

\[
\chi'(x)=\phi'(T^{-1}x)^2,\qquad
\kappa:=9/16\le\chi'(x)\le K:=25/16.
\tag{4}
\]

In particular $\chi$ is globally Lipschitz. At finite width set

\[
q_a=\frac{T(z_a)}{\sqrt n},\qquad
a_a=A_n(q_a):=\frac{\chi(\sqrt n\,q_a)}{\sqrt n},
\qquad c=\frac u{\sqrt n},\qquad W=W^{(2)}.
\]

Every coordinate of $A_n$ has derivative between $\kappa$ and $K$, and
$A_n(0)=0$. Consequently

\[
\|A_n(p)-A_n(q)\|_2\le K\|p-q\|_2
\tag{5}
\]

with no width-dependent constant. The output is
$f_a=c^\top W a_a$.

Let $b_a(t)=(y_a-f_a(t))/2$ denote the actual residual control, not the
readout. Orthogonality of the two chosen inputs makes the full physical flow
exactly

\[
\begin{aligned}
\dot q_a&=b_aW^\top c,\\
\dot W&=c\left(\sum_a b_aa_a\right)^\top,\\
\dot c&=W\sum_a b_aa_a.
\end{aligned}
\tag{6}
\]

For example, the original first-layer equation gives
$\dot z_a=b_a\phi'(z_a)\odot W^\top u$. Multiplying by
$T'(z_a)/\sqrt n$ cancels the gate and gives the first equation of (6).
This is a change of coordinates of the original optimizer. It does not
replace the metric by an Euclidean gradient flow in $q$.

On a set where $\|q_a\|_2,\|a_a\|_2,\|c\|_2,\|W\|_{\rm op}\le R$,
the vector field (6) is Lipschitz, with a constant depending only on $R$,
$K$, and the labels, in the difference norm

\[
\sum_a\|\Delta q_a\|_2+\|\Delta W\|_F+\|\Delta c\|_2.
\tag{7}
\]

Indeed the output differences are bounded by expanding
$c^\top WA_n(q_a)$ into its three factor differences and using (5).
The residual controls are therefore Lipschitz. Expanding each product in
(6) then gives the assertion. Although $\|W_0\|_F$ grows with width, only
$\|W_0\|_{\rm op}$ enters these product bounds. No derivative of $\chi'$,
and no maximum reverse-carrier coordinate, is used.

## Single-source dynamics and finite real blowup

For the source direction $M\nabla f_1$, set the controls in (6) to
$b_1=1,b_2=0$ and write source time as $s$. Then $q_2$ is constant. Put
$a=a_1$ and $D=\operatorname{diag}\phi'(z_1)$. The exact equations become

\[
q_1'=W^\top c,\qquad
a'=D^2W^\top c,\qquad
W'=ca^\top,\qquad
c'=Wa.
\tag{8}
\]

The prime denotes $d/ds$ only in this section. Crucially, the linear
second activation leaves the invariant

\[
WW^\top-cc^\top=W_0W_0^\top=:G_0
\tag{9}
\]

unchanged by the nonlinear first activation. Differentiating $c'=Wa$ gives

\[
c''=\|a\|_2^2c+WD^2W^\top c.
\tag{10}
\]

Let $R(s)=\|c(s)\|_2$ and $h=\|W_0a_0\|_2>0$. For $s>0$ in the solution
interval, $R>0$ and $R'>0$: the derivative of $c^\top c'$ is
$\|c'\|_2^2+c^\top c''\ge0$, and it is initially positive to leading
order because $c'(0)=W_0a_0\ne0$. The norm derivative formula, (4), and (9)
give

\[
\begin{aligned}
R''
&=\frac{\|c'\|_2^2-(R')^2+c^\top c''}{R}\\
&\ge \frac{\kappa\,c^\top WW^\top c}{R}\\
&\ge\kappa R^3.
\end{aligned}
\tag{11}
\]

The omitted term $\|c'\|_2^2-(R')^2$ is nonnegative by Cauchy--Schwarz.
Also $R(0)=0$ and $R'(0+)=h$. Multiplying (11) by $2R'>0$ and integrating
gives

\[
(R')^2\ge h^2+\frac\kappa2R^4.
\tag{12}
\]

Thus the positive source solution cannot persist for a time exceeding

\[
\int_0^\infty\frac{dr}{\sqrt{h^2+\kappa r^4/2}}
\le2^{5/4}\kappa^{-1/4}h^{-1/2}.
\tag{13}
\]

For the elementary bound, split the integral at
$r_0=(2h^2/\kappa)^{1/4}$; bound the first denominator below by $h$
and the second below by $\sqrt{\kappa/2}\,r^2$.

This finite-time obstruction is an actual norm blowup. If $R$ stayed bounded
on a finite source interval, (9) would bound $\|W\|_{\rm op}$.
Then $q_1'=W^\top c$ and (5) would bound $q_1,a$ and every finite-width
coordinate. Local smoothness would continue the solution. Therefore, at
its finite maximal positive source time $S_n$, $R(s)\to\infty$.
The source output is

\[
F_n(s)=f_1(s)=c^\top Wa=c^\top c'=RR',
\tag{14}
\]

so (12) implies $F_n(s)\to+\infty$ as $s\uparrow S_n$.
This proves a real source singularity of the actual observable, without
coefficientwise Taylor positivity.

There are absolute $c_0,C_0>0$ such that an initialization event of probability
at least $1-C_0e^{-c_0n}$ satisfies

\[
\|W_0\|_{\rm op}\le4,\qquad
\|a_0\|_2\le2,\qquad \|q_1(0)\|_2\le2,\qquad
h\ge1/4.
\tag{15}
\]

For the vector bounds use (1), the bounds on $T'$ following from (1),
and fixed-deviation chi-square tails for $\|z_1(0)\|_2^2/n$.
Conditional on $a_0$, $\|W_0a_0\|_2^2/\|a_0\|_2^2$ has law
$\chi_n^2/n$; together with $\|a_0\|_2\ge(3/4)\|z_1(0)\|_2/\sqrt n$,
another such tail gives $h\ge1/4$. A sphere-net Gaussian bound gives
the operator event, as in the permitted linear witness.

On (15), (13) is less than six. Hence $S_n<6$ on this one
high-probability event, independently of width.

There is a second useful invariant, suggested by the supervisor. Define

\[
\Psi(z)=2\int_0^z\frac{\phi(r)}{\phi'(r)}\,dr,\qquad
I_0=\frac1n\sum_j\Psi(z_{1,j}(0)).
\]

The original source equation is
$z_1'=\sqrt n\,D W^\top c$. Hence

\[
\frac d{ds}\frac1n\sum_j\Psi(z_{1,j})
=2a^\top W^\top c
=\frac d{ds}\|c\|_2^2,
\qquad
\frac1n\sum_j\Psi(z_{1,j})=I_0+R^2.
\tag{15a}
\]

Oddness of $\phi$ makes both $\Psi$ and $\phi^2$ even, and comparison of
their derivatives on the positive half-line gives
$\kappa\Psi(z)\le\phi(z)^2\le K\Psi(z)$ for all real $z$.
Consequently

\[
\kappa(I_0+R^2)\le\|a\|_2^2\le K(I_0+R^2).
\tag{15b}
\]

This strengthens (11) to
$R''\ge\kappa I_0R+2\kappa R^3$, and hence $R'\ge\sqrt\kappa R^2$.
On (15), $I_0\le\|a_0\|_2^2/\kappa<8$ and $\|G_0\|_{\rm op}\le16$.
When $R\ge1$, equations (9) and (15b) also give

\[
R'\le\|c'\|_2\le
\sqrt K\sqrt{16+R^2}\sqrt{8+R^2}<16R^2.
\]

Integrating the differential inequalities for $1/R$ up to $S_n$ yields
the uniform real profile

\[
\frac1{16(S_n-s)}\le R(s)\le\frac4{3(S_n-s)},\qquad
\frac3{16384(S_n-s)^3}\le F_n(s)
\le\frac{1024}{27(S_n-s)^3},
\tag{15c}
\]

whenever $R(s)\ge1$. This prevents the finite-width blowup from being merely
a singularity with a vanishing coefficient on its own terminal scale.
It still does not imply a lower bound for approximation on the much smaller
source interval visited while fitting the fixed small label.

Both hidden layers actually move. At source time zero,

\[
a''(0)=D_0^2W_0^\top W_0a_0,\qquad
W''(0)=(W_0a_0)a_0^\top.
\]

Using (15),
$\|a''(0)\|_2\ge\kappa h^2/\|a_0\|_2\ge\kappa/32$ and
$\|W''(0)\|_F=h\|a_0\|_2\ge h^2/\|W_0\|_{\rm op}\ge1/64$.
The first inequality uses $\|D_0^2x\|_2\ge\kappa\|x\|_2$ and
$\|W_0^\top W_0a_0\|_2\ge h^2/\|a_0\|_2$.
The corresponding physical initial accelerations are multiplied by
$(\eta/2)^2$, a positive width-independent factor.

## A quantitative inactive-input estimate

There is a common short source interval on which all normalized state sizes
are bounded. Let

\[
S=1/32,\qquad
M(s)=\max\{\|a(s)\|_2,\|W(s)\|_{\rm op},\|c(s)\|_2\}.
\]

Equation (8) gives
$M(s)\le4+K\int_0^sM(r)^2\,dr$ on (15). Therefore
$M(s)\le4/(1-4Ks)<5$ on $[0,S]$.

The initialized second first-layer feature vector
$a_2=\phi(z_2(0))/\sqrt n$ is independent of this source path. Its coordinates
are independent with mean zero and variance $\mu_2/n$. The source prediction
on input two is

\[
B_n(s)=a_2^\top w(s),\qquad w(s)=W(s)^\top c(s).
\]

Conditional on the entire first-source initialization,

\[
\mathbb E[B_n(s)^2]=\frac{\mu_2}{n}\|w(s)\|_2^2,\qquad
\mathbb E[B_n'(s)^2]=\frac{\mu_2}{n}\|w'(s)\|_2^2.
\]

Here $\|w\|_2\le25$ and
$w'=(\|c\|_2^2I+W^\top W)a$ has norm at most $250$. Since $B_n(0)=0$,
integrating $(B_n^2)'$ and using $2|bb'|\le b^2+(b')^2$ gives

\[
\mathbb E\!\left[
\sup_{0\le s\le S}|B_n(s)|^2
\,\middle|\,W_0,z_1(0)\right]
\le \frac{3100}{n}
\tag{16}
\]

on (15). The numerical constant follows from
$\mu_2\le25/16$ and
$(25/16)(1/32)(25^2+250^2)<3100$.
Thus the unused-input source prediction is
$O_{\mathbb P}(n^{-1/2})$ uniformly on this fixed interval.
This conditional argument uses the true Gaussian bulk, not a population
symmetry substituted for the finite network.

## Comparison with the actual two-residual physical flow

Consider a reference physical trajectory that trains only the first loss
term, so its controls are
$b_1=(\eta-f_1)/2,b_2=0$. It is exactly the source solution (8) evaluated at
its own source clock

\[
\dot s_{\rm ref}=(\eta-F_n(s_{\rm ref}))/2,\qquad s_{\rm ref}(0)=0.
\tag{17}
\]

Because $F_n'>0$ on the positive source branch and $F_n(0)=0$, the scalar
residual in (17) stays nonnegative and at most $\eta$. For a sufficiently
small fixed physical interval, for example one contained in $[0,1/32]$,
its source clock remains within $[0,S]$.

The actual two-input flow and this reference have the same initialization.
The reference's residual in its omitted second equation is $-B_n(s_{\rm ref})$.
On the bounded state region, the difference between their vector fields is
therefore at most a fixed constant times $|B_n(s_{\rm ref})|$, plus the
width-independent Lipschitz constant from (7) times their state difference.
Gronwall's inequality gives

\[
\sup_{0\le t\le T}
\left(\sum_a\|q_a(t)-q_{a,\rm ref}(t)\|_2+
\|W(t)-W_{\rm ref}(t)\|_F+
\|c(t)-c_{\rm ref}(t)\|_2\right)
\le C_T\sup_{0\le s\le S}|B_n(s)|
\tag{18}
\]

for one fixed $T>0$, independent of width.

For clarity, the bounded-region condition is not circular. The initial
second vector satisfies $\|q_2(0)\|_2,\|a_2(0)\|_2\le2$ with exponentially
high probability. For the full loss, $\sum_a|b_a|\le\|r\|_2/\sqrt2\le
\eta/\sqrt2\le1$ by energy decay; for the reference,
$|b_1|\le\eta/2\le1$. The product bounds from (6), together with
$a_a'=b_a\chi'(\sqrt n q_a)W^\top c$, give a common scalar norm bound
of the same form used above. Taking a smaller fixed $T$ if necessary keeps
both trajectories inside one fixed region. On that region every output is
also Lipschitz in (7).

Equations (16)--(18) establish the actual local prediction comparison

\[
\sup_{0\le t\le T}
\left(
|f_1(t)-F_n(s_{\rm ref}(t))|+|f_2(t)|
\right)
=O_{\mathbb P}(n^{-1/2}).
\tag{19}
\]

The reference clock uses its own first prediction. Equation (19) is not yet
a comparison with a truncated NTH.

## Two precise approximation lemmas for the remaining bridge

First, own-clock feedback does not obstruct a polynomial lower bound once
a scalar reduction has been justified. Let
$f(t)=F(s(t))$ and $g(t)=P(s_q(t))$, with

\[
\dot s=a(y-f),\qquad
\dot s_q=a(y-g),\qquad s(0)=s_q(0)=0,\quad a>0.
\]

Suppose $y-f(t)\ge c>0$ on $[0,T]$, $f$ is $L$-Lipschitz there, and
$\|f-g\|_\infty\le e<c/2$. Then
$\|s-s_q\|_\infty\le aTe$, and both clocks are strictly increasing.
On every common clock interval contained in both ranges, inversion gives

\[
|s^{-1}(x)-s_q^{-1}(x)|\le Te/c.
\]

It follows directly that

\[
|F(x)-P(x)|\le(1+LT/c)e.
\tag{20}
\]

This proof does not use a derivative bound for $P$. A fixed interval such
as $[0,s(T)/2]$ is contained in both ranges when $aTe\le s(T)/2$.

Second, let $F$ be a fixed continuous function on a nondegenerate compact
real interval. If there are polynomials $P_n$ with

\[
\deg P_n=o(\log n),\qquad
\|F-P_n\|_\infty\le Cn^{-\alpha},\quad \alpha>0,
\tag{21}
\]

then $F$ is the restriction of an entire function. Here is an elementary
proof. For any fixed $B>0$, choose $n_k=\lceil e^{Bk}\rceil$. For large $k$,
$\deg P_{n_k}\le k$, and the best degree-$k$ error is at most
$Ce^{-\alpha Bk}$. Since $B$ is arbitrary, that error has $k$th root
tending to zero. After mapping the interval to $[-1,1]$, its Chebyshev
coefficient of degree $j$ has absolute value at most twice the best
degree-$(j-1)$ error, by subtracting that polynomial in the defining
cosine integral. These coefficients therefore decay faster than every
geometric sequence. The Chebyshev polynomials grow at most geometrically
on each compact complex set, by their recurrence. Their series converges
uniformly on every such set, defines an entire function, and equals $F$
on the original interval.

Lemma (21) explains why a quantitative approximation to a fixed nonentire
source curve would rule out every $q_n=o(\log n)$ construction, without
isolating one Taylor coefficient. Its fixed-target and quantitative-error
hypotheses cannot be discarded.

## A polynomial-parameter transfer for the actual omitted physical jet

There is another route that avoids a source-clock or population-curve
reduction at the jet stage. In this section only, vary the fixed activation
over the family

\[
\phi_\varepsilon(z)=z+\varepsilon\sin z,\qquad
\varepsilon\in I:=[1/8,1/4].
\tag{22}
\]

All the real bounds above hold uniformly on this interval. This family is
used to select one deterministic, width-independent, genuinely nonlinear
activation; the parameter may not be selected after seeing the Gaussian
initialization. The conclusions below apply to almost every fixed member
of the family, not specifically to the previously displayed value $1/4$.

Let $K_r^\varepsilon$ be the standard metric NTH tensors and let
$f_{n,1}^{(q),\varepsilon}$ be the original order-$q$ frozen-top closure,
using its own residual. Define its actual physical-time error and the first
potentially nonzero omitted order by

\[
g_{n,q}^\varepsilon(t)
=f_{n,1}^\varepsilon(t)-f_{n,1}^{(q),\varepsilon}(t),
\qquad j=2\lfloor q/2\rfloor+1.
\]

At every fixed parameter value, $f_a^\varepsilon$ and the source vector
field $M\nabla f_a^\varepsilon$ are affine in $\varepsilon$. The recursion
$K_{r+1}^\varepsilon=D K_r^\varepsilon[M\nabla f_a^\varepsilon]$
therefore proves inductively that every initialized rank-$r$ entry is a
polynomial in $\varepsilon$ of degree at most $r$. The mobility is constant
and does not change this count.

Readout parity gives $K_r^\varepsilon(0)=0$ for odd $r$, since $u(0)=0$.
Successive differentiation of the triangular exact and truncated
hierarchies shows that all physical error derivatives below order $j$
vanish, and that

\[
J_{n,q}(\varepsilon)
:=\frac{(g_{n,q}^\varepsilon)^{(j)}(0)}{j!}
=\frac{(\eta/2)^j}{j!}
  K_{j+1}^\varepsilon(1,\ldots,1)(0).
\tag{23}
\]

In this differentiation the dense and truncated residual derivatives agree
until the first unmatched tensor is encountered; every residual-feedback
term of smaller order therefore cancels. The surviving word has only
index one because the initial second residual is zero. Thus (23) includes
the hierarchy's own-residual feedback. It is not a same-clock
approximation. In particular, $J_{n,q}$ is a polynomial of degree at most
$j+1$.

At $\varepsilon=0$ use the permitted linear-witness coefficient proof.
Writing $B_0=W^{(1)}_0/\sqrt n$, its one simultaneous Gaussian event is

\[
\tfrac12 I\preceq B_0^\top B_0\preceq2I,\qquad
\|W_0\|_{\rm op}\le4,\qquad
\sigma_{\min}(W_0B_0)\ge3/4.
\tag{24}
\]

It has probability at least $1-Ce^{-cn}$, and on it that proof gives

\[
J_{n,q}(0)\ge(\eta/16)^j
\quad\text{simultaneously for every }q\ge2.
\tag{25}
\]

Only this initialized linear coefficient bound is used; no linear
holomorphic-flow estimate is transferred to the nonlinear family.

### Elementary sublevel estimate

For a polynomial $p$ of degree at most $D\ge1$, $p(0)\ne0$, and
$0<\tau<|p(0)|$, the following elementary estimate suffices:

\[
\left|\{\varepsilon\in I:|p(\varepsilon)|\le\tau\}\right|
\le e\left(\frac{\tau}{|p(0)|}\right)^{1/D}.
\tag{26}
\]

Here vertical bars around a set denote Lebesgue measure. To prove it, let
the sublevel set have measure $\mu>0$. Select $D+1$ of its closure points
$x_0<\cdots<x_D$ at equally spaced measure quantiles. They can be chosen
so that $x_k-x_i\ge(k-i)\mu/(D+1)$. Lagrange interpolation at zero, using
$|x_i|\le1/4$, gives

\[
|p(0)|
\le \tau
 \left(\frac{D+1}{4\mu}\right)^D
 \sum_{i=0}^D\frac1{i!(D-i)!}
=\tau\left(\frac{D+1}{2\mu}\right)^D\frac1{D!}
\le\tau(e/\mu)^D.
\]

The last step uses $D!\ge(D/e)^D$ and $(D+1)/(2D)\le1$.
Continuity allows the use of closure points. This proves (26), including
when the actual degree is smaller than $D$.

### One fixed nonlinear parameter, growing orders, and wide Gaussian runs

Let $n_k=\lceil e^k\rceil$, $k\ge2$. For every $2\le q\le k$ put

\[
L_{k,q}
:=(\eta/16)^j(8e\,k^4)^{-(j+1)},
\qquad j=2\lfloor q/2\rfloor+1.
\tag{27}
\]

For each Gaussian initialization satisfying (24), (26) shows that
the parameter set where $|J_{n_k,q}|<L_{k,q}$ has measure at most
$1/(8k^4)$. Summing over $q\le k$ and then over $k$ is finite. The
failure probabilities of (24) along $n_k$ are summable as well.
Apply the elementary first Borel--Cantelli lemma on the product of
Lebesgue measure on $I$ and any joint coupling of the Gaussian
initializations. Fubini's theorem then proves the following assertion:

For Lebesgue-almost every single fixed $\varepsilon\in I$, almost surely
in that coupling, all sufficiently large $k$ satisfy

\[
\left|(g_{n_k,q}^\varepsilon)^{(j)}(0)\right|
\ge j! L_{k,q}
\quad\text{simultaneously for every }2\le q\le k.
\tag{28}
\]

In particular the probability of this simultaneous event tends to one.
The selected activation parameter is independent of width, order, and
the realized initialization. No uniformity in the random onset width is
asserted. The quantitative exponent in (27) is
$-\log L_{k,q}=O_\eta((q+1)(1+\log k))$.

An eventual probability bound can also be extracted. Let
$p_k(\varepsilon)$ be the probability that (24) fails or one of the
inequalities (28), $2\le q\le k$, fails at width $n_k$. The sublevel
estimate gives

\[
\int_I p_k(\varepsilon)\,d\varepsilon
\le |I|Ce^{-cn_k}+\frac1{8k^3}.
\]

Consequently the measures of
$\{\varepsilon:p_k(\varepsilon)>1/k\}$ are summable. Another application
of Borel--Cantelli, now on $I$ alone, shows that for almost every fixed
$\varepsilon$ there is a deterministic $k_0(\varepsilon)$ such that
the simultaneous event (28) has probability at least $1-1/k$ for
every $k\ge k_0(\varepsilon)$.

Equation (28) is a genuine fixed-nonlinearity growing-order result about
the first omitted **physical jet**, but not yet a prediction-error lower
bound. It does not assert that a prescribed value such as $1/4$ lies
outside the exceptional set.

## A precise real-remainder bridge, and the part supplied by the NTH ODE

The derivative-to-error step needs only one further real derivative.
Suppose a $C^{j+1}$ real function $g$ on $[0,T]$ has
$g^{(r)}(0)=0$ for $r<j$, $|g^{(j)}(0)|/j!\ge L>0$, and

\[
H=\sup_{0\le t\le T}\frac{|g^{(j+1)}(t)|}{(j+1)!}<\infty.
\]

Taylor's theorem with its integral remainder gives, for
$\tau=\min\{T,L/(2H)\}$, with the second entry omitted when $H=0$,

\[
|g(\tau)|\ge \frac L2\,\tau^j.
\tag{29}
\]

Consequently, a sufficient missing estimate is the following:
with probability tending to one, uniformly over the required orders,

\[
T_{n,q}\ge
\exp[-P(q,\log\log(n+e^e))],
\qquad
\sup_{0\le t\le T_{n,q}}
\frac{|(g_{n,q}^\varepsilon)^{(j+1)}(t)|}{(j+1)!}
\le \exp[P(q,\log\log(n+e^e))],
\tag{30}
\]

where $P$ is one fixed polynomial with nonnegative coefficients.
Combine (27), (29), and (30). Along $n_k$ and for every
$q\le C\log k$, the resulting prediction lower bound is
$\exp[-\operatorname{poly}(\log k)]$, which is much larger than
$n_k^{-1/2}$. A fixed bounded physical horizon can be imposed by also
including it in the minimum defining $\tau$; this changes only a
constant in the polynomial.

Thus (30), if proved, would rule out every fixed-power polylogarithmic
literal tensor budget: for $m=2$, storing a rank-$q$ training array uses
$2^q$ entries, and a bound $2^q\le(\log n)^C$ forces
$q=O(\log\log n)$. This statement is conditional on (30), not a theorem
that (30) holds.

The frozen-top ODE itself supplies one part of (30). Define its
initialized training-array envelope

\[
H_q=\max\left\{1,\,
 \max_{2\le r\le q}\ \max_{a_1,\ldots,a_r\in\{1,2\}}
 |K_r^\varepsilon(a_1,\ldots,a_r)(0)|\right\}.
\tag{31}
\]

Augment the hierarchy state by a constant coordinate equal to one.
Each coordinate equation is quadratic, with total absolute coefficient
sum at most two, because the residual control is $(y_a-f_a)/2$,
$m=2$, and $|y_a|\le1$. If $X(t)$ is the maximum absolute state
coordinate, the usual integral majorant gives

\[
X(t)\le\frac{H_q}{1-2H_qt}\le2H_q
\qquad (0\le t\le1/(4H_q)).
\tag{32}
\]

At any real time $t\le1/(8H_q)$, the Taylor coefficient recurrence of
this quadratic ODE is majorized by that of
$w'=2w^2$, $w(0)=2H_q$. Hence for every derivative order $r\ge0$,

\[
\frac{|(f_{n,1}^{(q),\varepsilon})^{(r)}(t)|}{r!}
\le 2H_q(4H_q)^r.
\tag{33}
\]

This recurrence also proves convergence of the local Taylor series,
so no unproved analyticity claim is used in (33). Neither (32) nor
(33) depends on the number of tensor entries. Therefore an estimate
$H_q\le\exp[\operatorname{poly}(q,\log\log n)]$ supplies the entire
truncated-hierarchy contribution to (30). What remains is an
initialized all-word tensor estimate of that strength and the matching
$(j+1)$st real derivative bound for the actual dense nonlinear flow.
The dimension-independent first-derivative Lipschitz bound (7) alone
does not provide either high-order assertion.

There is an equivalent finite-Taylor version that does not assume a bound
on derivatives of the actual flow away from zero. Suppose the dense output
has a Taylor remainder through degree $j$ bounded by $A_{\rm d}t^{j+1}$
for $0\le t\le T_{\rm d}$. At zero the same quadratic recurrence used for
(33) bounds the truncated output coefficient of degree $r$ by
$H_q(2H_q)^r$. Its tail through degree $j$ is therefore at most

\[
2H_q(2H_q)^{j+1}t^{j+1}
\qquad (0\le t\le1/(4H_q)).
\tag{34}
\]

Since the lower physical jets match exactly, this proves
$|g(t)-J_{n,q}(\varepsilon)t^j|\le A t^{j+1}$ with
$A=A_{\rm d}+2H_q(2H_q)^{j+1}$ on the intersection of the two time
intervals. Formula (29) applies with this $A$ in place of $H$.

For a more explicit quantitative target, suppose the missing dense and
initialized-tensor estimates imply, on events of probability tending to
one and for the orders in question,

\[
|g(t)-J_{n_k,q}(\varepsilon)t^j|
\le B_{k,q}t^{j+1}\quad(0\le t\le B_{k,q}^{-1}),\qquad
B_{k,q}=\exp[Cq^2\Lambda_{k,q}],
\quad
\Lambda_{k,q}=\log(q+1)+\log(k+1),
\tag{35}
\]

where $C\ge1$ is fixed. This condition follows, for example, from a
state-jet envelope whose logarithm is
$O(q(\log q+\log\log n))$, together with a dense finite-jet residual
lemma giving a degree-$j$ remainder coefficient of order the
$(j+1)$st power of that envelope. That latter lemma and the Gaussian
state-jet estimate are separate obligations; they are not proved here.

Take $\tau=L_{k,q}/(2B_{k,q})$. It lies in the interval of (35), since
$0<L_{k,q}<1$, and the exact calculation gives

\[
\begin{aligned}
|g(\tau)|
&\ge
\frac{L_{k,q}^{j+1}}{2^{j+1}B_{k,q}^{j}}\\
&\ge
\exp[-C_\eta q^3\Lambda_{k,q}],
\qquad
C_\eta:=2C+10+\log(16/\eta).
\end{aligned}
\tag{36}
\]

To check the safe constant, use $j\le3q/2$, $j+1\le2q$ for $q\ge2$.
The negative logarithm of the first line of (36) equals

\[
(j+1)\log2
+j(j+1)\log(16/\eta)
+(j+1)^2(\log(8e)+4\log k)
+jCq^2\Lambda_{k,q}.
\]

The last term is at most $(3C/2)q^3\Lambda_{k,q}$.
Since $\log(8e)+4\log k\le4\Lambda_{k,q}$, the third term is at
most $8q^3\Lambda_{k,q}$. The first is at most
$q^3\Lambda_{k,q}$, and the second is at most
$\log(16/\eta)q^3\Lambda_{k,q}$, because
$q\Lambda_{k,q}\ge2\log9>3$.
These estimates imply (36).

Conditional on (35), (36) excludes
$q=o((\log n/\log\log n)^{1/3})$ from attaining any fixed polynomial
accuracy $O_{\mathbb P}(n^{-a})$, $a>0$, along $n_k$.
Indeed its error lower is $n_k^{-o(1)}$. More explicitly, for

\[
q\le
\left(\frac{a}{4C_\eta}\right)^{1/3}
\left(\frac{k}{\log(k+1)}\right)^{1/3},
\]

and $q\le k$, equation (36) is at least $e^{-ak/2}$, which is larger
than every fixed multiple of $n_k^{-a}$ for large $k$.
The corresponding necessary literal-array growth would be
$\exp[\Omega((\log n/\log\log n)^{1/3})]$ along this sequence.
It is superpolylogarithmic but still subpolynomial in width.
Neither a polynomial storage lower bound nor the unconditional hypothesis
(35) is established by this calculation.

### Geometric-envelope sharpening: a higher-degree real polynomial transfer

The cubic-order exponent in (36) is not intrinsic to the parameter
transfer. A geometric initialized-jet envelope permits a sharper
remainder. This subsection proves the exact transfer needed to use it.
It supersedes the quantitative order consequence following (36) whenever
the sharper remainder assumption below is available.

First, if $P$ is a polynomial of degree at most $R$, $t>0$, and
$[s^j]P$ denotes its coefficient of $s^j$, then

\[
|[s^j]P|\,t^j
\le 3\cdot7^R\sup_{0\le s\le t}|P(s)|
\qquad (0\le j\le R).
\tag{37}
\]

Here is a complete proof, valid also for complex coefficients. Write
$p(x)=P(tx)$ on $[0,1]$ and let $M=\|p\|_{[0,1]}$. Its shifted
Chebyshev expansion is
$p(x)=\sum_{r=0}^R a_r T_r(2x-1)$. The cosine integral formulas give
$|a_0|\le M$ and $|a_r|\le2M$ for $r\ge1$. Define
$S_r(x)=T_r(2x-1)$ and let $N_r$ be the sum of the absolute values of
its monomial coefficients. The recurrence

\[
S_{r+1}=(4x-2)S_r-S_{r-1},\qquad S_0=1,\quad S_1=2x-1
\]

gives $N_{r+1}\le6N_r+N_{r-1}$, with $N_0=1$ and $N_1=3$.
Induction yields $N_r\le7^r$. Therefore the absolute value of every
monomial coefficient of $p$ is at most

\[
M\left(1+2\sum_{r=1}^R7^r\right)
=M\frac{7^{R+1}-4}{3}
\le3\cdot7^R M.
\]

The coefficient of $x^j$ is $t^j[s^j]P$, proving (37).

Now retain the Remez notation $n_k=\lceil e^k\rceil$ and
$j=2\lfloor q/2\rfloor+1$, and set $R=2j$. Suppose the degree-$R$
Taylor polynomial $P$ of the actual error $g=g_{n_k,q}^\varepsilon$
satisfies

\[
[s^j]P=J_{n_k,q}(\varepsilon),\qquad
|J_{n_k,q}(\varepsilon)|\ge L_{k,q},\qquad
\sup_{0\le s\le t}|g(s)-P(s)|
\le C(Bt)^{2j+1}
\quad(0\le t\le B^{-1}),
\tag{38}
\]

where $B\ge1$, $C>0$, and $L_{k,q}$ is exactly (27).
Put $C_+=\max\{1,C\}$ and choose

\[
\tau=\frac{L_{k,q}^{1/(j+1)}}{64C_+B^2}.
\tag{39}
\]

Since $0<L_{k,q}<1$, this time lies within the interval in (38).
By (37), $\|P\|_{[0,\tau]}\ge
L_{k,q}\tau^j/(3\cdot49^j)$. The remainder is at most half that
quantity because

\[
\frac{C B^{2j+1}\tau^{j+1}}{L_{k,q}}
=\frac{C}{64^{j+1}C_+^{j+1}B}
\le64^{-(j+1)}
\le\frac1{6\cdot49^j}.
\]

The triangle inequality therefore proves the explicit prediction lower
bound

\[
\begin{aligned}
\sup_{0\le s\le\tau}|g(s)|
&\ge\frac{L_{k,q}\tau^j}{6\cdot49^j}\\
&=\frac{L_{k,q}^{\,2-1/(j+1)}}{
        6(3136C_+B^2)^j}\\
&\ge\frac{L_{k,q}^{\,2}}{6(3136C_+B^2)^j}.
\end{aligned}
\tag{40}
\]

No sign or size assumption on the intervening Taylor coefficients is
needed. The proof uses the polynomial norm on the real interval, not
evaluation of the leading term at its endpoint.

The chosen time is only polynomially small when $B$ is polynomial in
$q$ and $k$. In fact,

\[
L_{k,q}^{1/(j+1)}
=\frac{(\eta/16)^{j/(j+1)}}{8e k^4}
\ge\frac{\eta}{128e k^4},
\qquad
\tau\ge\frac{\eta}{8192e C_+ k^4B^2}.
\tag{41}
\]

Suppose $\log B\le d_B\Lambda_{k,q}$ for a fixed $d_B\ge1$, where
$\Lambda_{k,q}=\log(q+1)+\log(k+1)$. For $2\le q\le k/4$ the
negative logarithm of the last line in (40) is bounded by

\[
\begin{aligned}
&\log6+2j\log(16/\eta)
+2(j+1)(\log(8e)+4\log k)\\
&\hspace{2em}
+j\bigl(\log3136+\log C_++2\log B\bigr)
\le C_\eta q\Lambda_{k,q},
\end{aligned}
\]

with the safe explicit choice

\[
C_\eta=64+3\log(16/\eta)+3d_B+2\log C_+.
\tag{42}
\]

For the bound, use $j\le3q/2$, $j+1\le2q$,
$\Lambda_{k,q}\ge1$, and $\log k\le\Lambda_{k,q}$.
The constant contributions are bounded by
$17+4\log(8e)+(3/2)\log3136<64$ after division by
$q\Lambda_{k,q}$; the displayed coefficients of the remaining
terms dominate their respective contributions.
Thus

\[
\sup_{0\le s\le\tau}|g_{n_k,q}^\varepsilon(s)|
\ge\exp[-C_\eta q(\log(q+1)+\log(k+1))].
\tag{43}
\]

Here the restriction $q\le\lfloor k/4\rfloor$ ensures
$R=2j\le3q\le3k/4<\lfloor\log(en_k)\rfloor$, so a simultaneous
initialized-jet estimate through logarithmic order covers the degree-$R$
dense remainder. The hierarchy itself still retains rank $q$; taking
more physical-time Taylor coefficients of that same finite ODE does
not change its truncation order.

For completeness, the sharpened dense and weighted-hierarchy remainders
fit (38) with a polynomial $B$. Let $B_0\ge1$ be a geometric initialized
envelope, let the dense remainder be at most
$C_{\rm d}(D B_0t)^{R+1}$ for $t\le(2D B_0)^{-1}$, and let the
original hierarchy remainder be at most
$4B_0(4B_0^2t)^{R+1}$ for $t\le(8B_0^2)^{-1}$.
Take $C_{\rm d},D\ge1$ by enlargement and set

\[
B=2\max\{C_{\rm d}D,16\}\,B_0^3.
\tag{44}
\]

Each remainder is at most $(Bt/2)^{R+1}$, and $B^{-1}$ lies in
both validity intervals. Their sum is at most $(Bt)^{R+1}$.
Thus (38) holds with $C=1$. If
$B_0=[C_0(R+1)\log(en_k)]^{C_0}$ for fixed $C_0$, (44) has
$\log B\le d_B\Lambda_{k,q}$ with a fixed $d_B$.
This supplies the precise interface to the geometric-envelope
remainder lemma; no analytic continuation closure is introduced.

On the intersection of the Remez and initialized-jet events, (43) is
simultaneous in $2\le q\le\lfloor k/4\rfloor$. For every fixed $a>0$,
any order satisfying

\[
q\le \frac{a}{4C_\eta}\,
       \frac{k}{\log(k+1)}
\]

has error at least $e^{-ak/2}$, and therefore cannot attain
$O_{\mathbb P}(n_k^{-a})$ accuracy. An order larger than $k/4$
already exceeds a constant multiple of $k/\log k$.
Consequently the sharpened necessary order is
$\Omega(\log n_k/\log\log n_k)$, with literal-array storage at least

\[
\exp\!\left[
\Omega\!\left(\frac{\log n_k}{\log\log n_k}\right)
\right].
\tag{45}
\]

The result remains along the stated geometric width sequence, for almost
every one fixed nonlinear activation parameter. This lower bound is
superpolylogarithmic but not polynomial in width. For the full
unconditional combination of the independently proved initialized-jet
and remainder inputs with this algebraic transfer, use
NONLINEAR_RESULT.md.

For example, fixed jets and even excellent real Lipschitz bounds do
not imply a useful error lower bound in isolation: the entire functions
$h_N(t)=L t^j e^{-N^2t^2}$ satisfy
$h_N^{(j)}(0)=j!L$, whereas
$\sup_{t\ge0}|h_N(t)|=L(j/(2eN^2))^{j/2}\to0$.
They illustrate why (28) cannot be reported as an error theorem without
a remainder estimate.

## Superseded source-route gaps, not used by the parameter route

This section records why the original source-blowup approximation route
was not completed. It is retained to prevent a finite-width singularity
from being mistaken for a prediction approximation theorem. These are
not outstanding obligations of the later parameter route: the latter uses
(23), (28), and (34)--(36), together with the separate initialized-jet
and finite-Taylor lemmas, in the combined NONLINEAR_RESULT.md assembly.
The old source-approximation route had three distinct missing assertions.

1. **The finite hierarchy is still a two-control word polynomial.** Freezing
   rank $q$ makes it a finite ordered-integral expansion in its own two
   residuals. If its predictions approximate the dense predictions, (19)
   makes its second residual small on the short interval. But a proof must
   bound, uniformly for growing $q$, the sum of all initialized words
   containing that small control. Small residual size alone does not control
   large tensor coefficients. Only after this estimate can one replace the
   hierarchy by a scalar polynomial in its own first source clock and invoke
   (20). The later physical-jet route does not make this replacement.
2. **A finite-width singularity is not a quantitative fixed population
   singularity.** Equations (11)--(15) prove blowup of every finite-width
   source observable on the good event. They do not establish
   $\|F_n-F\|=O_{\mathbb P}(n^{-\alpha})$ on an interval for one fixed
   nonentire $F$. Qualitative convergence alone is insufficient for (21).
   Nor may the singularity be passed to a limit without a continuation
   and observable-amplitude argument. Even the uniform profile (15c) does
   not by itself show that an entire extension of a limiting curve on the
   small training interval agrees with its actual source evolution all the
   way to blowup. That identity needs real analyticity, a suitable
   quasianalyticity theorem, or another continuation principle for the
   population observable. A merely smooth evolution is insufficient.
3. **The requested dense-variability comparison needs its own norm and
   horizon estimate.** Equation (19) is a local comparison to a coupled
   source reference. It is not an all-time whole-sphere
   $O_{\mathbb P}(n^{-1/2})$ bound for two independent nonlinear dense runs.
   The separate SINE_DENSE_VARIABILITY.md argument supplies an all-time,
   whole-circle $O_{\mathbb P}(n^{-1/64000})$ benchmark instead. This
   deliberately nonsharp polynomial rate suffices for the later
   $n^{-o(1)}$ lower-bound comparison; no sharp root-width dense-pair
   theorem is being inferred from (19).

A fixed small perturbation of the linear activation does not automatically
repair these points: constants controlling $q$ derivatives may deteriorate
with $q$, even though the real transformed vector field is uniformly
Lipschitz. These source-flow arguments alone do not establish a
growing-order prediction or storage lower bound. This limitation does
not apply to the separately assembled parameter-transfer argument.

The useful new proved mechanism is the combination of a genuine nonlinear
first layer, a surviving matrix invariant, a finite real source-output
singularity with the uniform profile (15c), and the dimension-independent
real coordinate transform. The hidden primitive (15a) sharpens the real
growth comparison but supplies no sign control on higher Taylor coefficients:
derivatives of $\phi'$ still enter later coefficients with both signs. The
last transform also closes the local dense two-input reduction (19). These
are stronger inputs for a future prediction-level argument than an isolated
complex pole or an unsigned high-order derivative, but they do not replace
that argument. Separately, the parameter-transfer argument (22)--(28)
handles a fixed genuine nonlinearity and the closure's own-residual
physical jet at growing orders. Equations (29) and (34)--(36) give the
precise deterministic bridge used with the separately proved finite-jet
remainder and Gaussian initialized-jet estimates in NONLINEAR_RESULT.md.
