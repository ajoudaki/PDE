# Growing-sample deep-linear witness: source and physical-error checks

Status: scoped author derivation and check, not an independent promotion
review. This work began as a search for a fixed nonlinear analytic witness.
The supervisor redirected it to the explicit growing-sample construction
below and supplied the complete same-study files `STRONGER_SOURCE.md` and
`ANALYTIC_ROUTE.md`. Those files, the assignment, and the maintained notation
contract are the scientific inputs. No other study was inspected and no
experiment was run.

The checked conclusion is a width- and sample-uniform geometric lower bound
for the physical-time error of the original frozen-top hierarchy. Combined
with a separately proved dense-pair variability estimate, it gives a
superpolynomial count of literal tensor-array entries when the number of
samples grows as a power of width. It does not provide the originally sought
fixed-dataset nonlinear witness or an information-theoretic lower bound.

## Exact model and inputs

Let the width be $n$, let $4\le m\le\sqrt n$ be divisible by four, and put $d=m+1$. Set $s_a=1$ on the first $3m/4$ samples and $s_a=-1$ on the remaining $m/4$. In

\[
v_a=\frac{e_0+e_a}{\sqrt2}\in\mathbb R^d,
\qquad x_a=\sqrt d\,v_a,
\qquad y_a=\eta s_a,\qquad 0<\eta\le1,
\]

$e_0,e_1,\ldots,e_m$ are the coordinate vectors and $\eta$ is fixed
independently of $n,m$. Both hidden activations are the identity. The
canonical network has stored first matrix $W^{(1)}$, second matrix
$W^{(2)}$, readout $u$, and prediction

\[
f_a=\frac1n u^\top W^{(2)}W^{(1)}v_a.
\]

Its loss is $\mathcal L=(2m)^{-1}\sum_a(f_a-\eta s_a)^2$, and its parameter
mobilities are $(n,1,n)$. Set

\[
B=\frac{W^{(1)}}{\sqrt n},\qquad W=W^{(2)},\qquad
c=\frac u{\sqrt n}.
\]

This is an exact coordinate change: all three normalized blocks have
Euclidean/Frobenius mobility one, and

\[
f(v)=c^\top WBv.
\]

Initially, the entries of $B_0,W_0$ are independent (N(0,1/n)), the
two matrices are independent, and $c_0=0$. Define the residual controls

\[
u_a(t)=\frac{\eta s_a-f_a(t)}m,
\qquad V_a=\nabla f(v_a),
\qquad \dot X=\sum_a u_aV_a,
\quad X=(B,W,c).
\]

The use of $u_a$ for a scalar residual control in this paragraph follows
the supplied analytic proof; the unindexed $u=\sqrt n c$ is the stored
readout. Equivalently, every occurrence of $u_a$ below is the displayed
scalar $(\eta s_a-f_a)/m$.

Define $K_{1,a}=f_a$ and append each new index by

\[
K_{s+1,a_1\ldots a_sb}=D K_{s,a_1\ldots a_s}[V_b].
\]

The order-$q$ approximation copies $K_1,\ldots,K_q$ at initialization,
freezes $K_q$, and evolves lower ranks using its own controls
$(\eta s_a-f^{(q)}_a)/m$. No dense future residual or source trajectory is
supplied to this approximation.

The input Gram and the label-weighted mean input are

\[
G_{ab}=v_a^\top v_b=\frac{1+\delta_{ab}}2,
\qquad \bar v=\frac1m\sum_a s_a v_a,
\qquad \lambda=\|\bar v\|,
\qquad \lambda^2=\frac18+\frac1{2m}\in[1/8,1/4].
\tag{1}
\]

Thus the input Gram has minimum eigenvalue $1/2$; these samples are
correlated and linearly independent. The binary labels have empirical mean $\eta/2$ and variance $3\eta^2/4$. The unit query $\bar v/\lambda$ differs from every training input, since all $m$ of its private coordinates are nonzero.

## One initialization event, independent of hierarchy order

There are absolute positive constants $c,C$ such that, for sufficiently
large $n$, with probability at least $1-Ce^{-cn}$,

\[
\|B_0\|_{\mathrm{op}},\|W_0\|_{\mathrm{op}}\le4,
\qquad
\|B_0\bar v/\lambda\|^2\ge\frac12,
\qquad
\|W_0B_0\bar v/\lambda\|^2\ge\frac12,
\qquad
\sigma_{\min}(W_0B_0)\ge\frac12.
\tag{2}
\]

Here the last singular value treats $W_0B_0$ as a map from
$\mathbb R^d$ to $\mathbb R^n$. The last inequality is not valid
uniformly under only $d\le n$; the small aspect ratio is relevant.

For completeness, these bounds need only elementary Gaussian concentration
and sphere coverings. For a fixed unit vector $v$,

\[
\|B_0v\|^2\overset{\rm law}=\frac{\chi_n^2}{n},
\qquad
\|W_0B_0v\|^2\overset{\rm law}
=\frac{\chi_n^2}{n}\frac{\widetilde\chi_n^2}{n},
\]

where the two factors on the right are independent. The moment generating
function $\mathbb E e^{t\chi_n^2}=(1-2t)^{-n/2}$, obtained by multiplying
one-dimensional Gaussian integrals, gives exponentially small fixed-factor
upper and lower tails by Markov's inequality. A $1/4$-net of a sphere in
$k$ dimensions has at most $9^k$ points, by the disjoint-ball volume
argument. The upper-tail exponent at $\chi_n^2\ge9n$ is
$(9-1-\log9)n/2>n\log9$. Applying this net to the domain gives each
operator-norm bound in (2), since $d\le n$. For the lower singular value,
use a $1/64$-net in $\mathbb R^d$, with at most $129^d$ points.
At every net point $\|W_0B_0v\|\ge3/4$ except with probability
$Ce^{-cn}$. On the operator-norm event the product norm is at most 16,
so extending from the net loses at most $16/64=1/4$. Since
$d\le\sqrt n+1$, the factor $129^d$ is absorbed by the exponential
tail. The two specified-direction bounds follow directly from their
chi-square laws.

The initial empirical second-hidden-layer feature Gram is

\[
\frac1n h_a^{(2)\top}h_b^{(2)}
=v_a^\top B_0^\top W_0^\top W_0B_0v_b.
\]

Its minimum eigenvalue is at least $1/8$ on (2), because the matrix
$B_0^\top W_0^\top W_0B_0$ is at least (I/4), while the input Gram
is at least (I/2). This supplies a fixed positive feature-Gram gap.

## Factorial source derivatives with no sample-count loss

Consider the label-weighted average prediction

\[
F(X)=\frac1m\sum_a s_a f_a(X)=c^\top WB\bar v.
\]

Use $s$ only to differentiate the exact source equation $X'=\nabla F(X)$,
not to drive the frozen-top approximation. Writing $a=B\bar v$, this gives

\[
a'=\lambda^2W^\top c,\qquad W'=ca^\top,\qquad c'=Wa.
\tag{3}
\]

Put $b=a/\lambda$ and $\tau=\lambda s$. Derivatives with respect to
$\tau$ then satisfy exactly

\[
\frac{db}{d\tau}=W^\top c,\qquad
\frac{dW}{d\tau}=cb^\top,\qquad
\frac{dc}{d\tau}=Wb.
\tag{4}
\]

This is the source system proved in `STRONGER_SOURCE.md`. Its argument can
be checked directly here. Define

\[
A=\|b_0\|^2,\qquad H=\|W_0b_0\|^2,\qquad
Q=W_0W_0^\top,
\qquad \widetilde F(\tau)=c^\top Wb.
\]

The invariants $WW^\top-cc^\top=Q$ and
$\|b\|^2-\|c\|^2=A$ imply

\[
\frac{d^2c}{d\tau^2}=(AI+Q)c+2\|c\|^2c,
\quad c(0)=0,\quad \frac{dc}{d\tau}(0)=W_0b_0.
\tag{5}
\]

Diagonalize $Q\succeq0$ and choose the eigenvector signs so that the
initial derivative has nonnegative coordinates. The coefficient recurrence
of (5) then has only nonnegative terms. It coefficientwise dominates
$(W_0b_0)z(\tau)$, where $z''=Az+2Hz^3$, $z(0)=0,z'(0)=1$.
On (2), $A,H\ge1/2$, so that scalar recurrence in turn dominates
$2\tan(\tau/2)$, and therefore dominates

\[
w(\tau)=\frac{\tau}{1-\tau^2/12}.
\]

The last assertion follows by writing
$\tan x=\sum_{k\ge0}t_kx^{2k+1}$: the recurrence from
$(\tan x)'=1+\tan^2x$ gives $t_k\ge3^{-k}$ by induction.
Because $\widetilde F=c^\top dc/d\tau$, multiplying and differentiating
nonnegative series yields, for every $j=2k+1$,

\[
\widetilde F^{(j)}(0)
\ge j!\frac{H(k+1)^2}{12^k}\ge j!8^{-j}.
\tag{6}
\]

In original source time $F(s)=\lambda\widetilde F(\lambda s)$. Consequently

\[
F^{(j)}(0)=\lambda^{j+1}\widetilde F^{(j)}(0)
\ge j!64^{-j},\qquad j\ge1\text{ odd}.
\tag{7}
\]

Indeed $\lambda^{j+1}\ge8^{-(j+1)/2}\ge8^{-j}$. Every estimate holds
simultaneously for all orders on the one event (2).

## The first unmatched physical coefficient uses the closure's own residual

Every $K_s$ is multilinear in its $s$ input vectors for this linear
network. Hence its signed average over sample indices equals its value with
every input replaced by $\bar v$. In particular,

\[
\frac1{m^{j+1}}\sum_{a,b_1,\ldots,b_j}s_a\prod_{i=1}^j s_{b_i}
K_{j+1,a b_1\ldots b_j}(X_0)=F^{(j)}(0).
\tag{8}
\]

Odd-rank tensors are zero at $c_0=0$. To see the parity, $f$ is odd in
$c$, the $B,W$ components of each $V_a$ are odd in $c$, and the
$c$ component is even. Each appended Lie derivative therefore reverses
parity. Thus an odd top rank is initially zero and remains zero, making that
closure equivalent to the preceding even order. Put

\[
Q_q=2\lfloor q/2\rfloor,
\qquad j=Q_q+1,
\qquad
g_{n,m,q}(t)=\frac1m\sum_a s_a\bigl(f_a(t)-f_a^{(q)}(t)\bigr).
\]

Repeated integration expresses each hierarchy output as an ordered Volterra
series with initial $K_{k+1}$ and $k$ factors of its own control
$(\eta s_b-f_b^{(q)})/m$. The dense series has the same coefficients and all
orders. The first omitted even value of $k$ has zero coefficient by parity;
the first possibly nonzero omitted value is $k=j$. Coefficient induction
in these integral equations shows that the predictions match through degree
$j-1$. A change of the control starting at degree $j$ contributes only
at degree at least $j+1$, since every term containing a control has at
least one integration. Therefore the degree-$j$ discrepancy is precisely
the omitted term evaluated with the common initial controls $\eta s_b/m$:

\[
g_{n,m,q}^{(j)}(0)
=\frac{\eta^j}{m^{j+1}}
  \sum_{a,b_1,\ldots,b_j}s_a\prod_{i=1}^j s_{b_i}K_{j+1,a b_1\ldots b_j}(X_0)
=\eta^jF^{(j)}(0)
\ge j!\left(\frac\eta{64}\right)^j.
\tag{9}
\]

This calculation accounts for the distinct residuals. It does not identify
the dense and approximate source clocks. The label average cancels all powers
of $m$ in the source contraction; there is no $(\eta/m)^j$ penalty in
the final bound.

## A common complex disk and a real physical-time error

The proof of `ANALYTIC_ROUTE.md` extends with its original constants. Its
ordered-derivative bound only uses that each input has norm one and that
$\|B_0\|_{\mathrm{op}},\|W_0\|_{\mathrm{op}}\le4$. In particular,

\[
\max_{a,b_1,\ldots,b_k}|K_{k+1,a b_1\ldots b_k}(X_0)|
\le32\,4^k(k+2)!.
\]

On the unit output ball the sum of absolute control values satisfies

\[
\sum_{b=1}^m\left|\frac{\eta s_b-f_b}m\right|\le2,
\quad
\sum_{b=1}^m\left|\frac{f_b-\widetilde f_b}m\right|
\le\max_b|f_b-\widetilde f_b|.
\]

These are exactly the bounds used in that file's ordered-simplex contraction.
The factors counting sample sequences have already been summed into these
control norms, so the contraction is independent of $m$. The same dense
Picard bound applies as well. Therefore, with

\[
R=\frac1{8192},\qquad T_0=\frac R4=\frac1{32768},
\]

the dense and all frozen-top outputs are holomorphic on a neighborhood of
$|t|\le R$ and bounded by one there, simultaneously in $n,m,q$.
Their averaged discrepancy $g_{n,m,q}$ is bounded by two.

The factorial-derivative analytic lemma proved in `STRONGER_SOURCE.md` now
applies to (9) with $\rho=\eta/64$, $M=2$, and the displayed $R$.
For explicit constants put

\[
\theta_\eta=\frac\eta{2^{22}},\qquad
\kappa_\eta=16\left(1+\log\frac{2^{22}}\eta+\log\frac83\right),
\qquad
C_\eta=\log\frac{8e^2\kappa_\eta^2}{\theta_\eta}.
\]

It gives the deterministic inequality on (2)

\[
\begin{aligned}
\sup_{0\le t\le T_0}\max_{1\le a\le m}|f_a(t)-f_a^{(q)}(t)|
&\ge\sup_{0\le t\le T_0}|g_{n,m,q}(t)|\\
&\ge\frac1{8\kappa_\eta}e^{-C_\eta j}
\ge\frac{e^{-C_\eta}}{8\kappa_\eta}e^{-C_\eta q}.
\end{aligned}
\tag{10}
\]

This is an actual supremum over a fixed finite physical-time interval, with
the original closure and its own residual. It holds on one event whose
probability tends to one, for every finite $q\ge2$.

## Both hidden feature Grams change at order one in width

This witness has linear activations, but its hidden learning is not a pure
parameter gauge. Let $a(t)=B(t)\bar v$, $H(t)=W(t)B(t)\bar v$,
and write $a_0=a(0)$, $h_0=H(0)=W_0a_0$. Both signed mean hidden features
have zero initial velocity. Direct differentiation of the physical gradient
flow gives

\[
c'(0)=\eta h_0,\qquad
B''(0)=\eta^2W_0^\top W_0a_0\bar v^\top,
\qquad W''(0)=\eta^2h_0a_0^\top.
\]

Consequently

\[
a''(0)=\eta^2\lambda^2W_0^\top W_0a_0,
\qquad
H''(0)=\eta^2\bigl(\|a_0\|^2h_0+
                       \lambda^2W_0W_0^\top h_0\bigr).
\tag{11}
\]

For each hidden layer, the signed contraction $m^{-2}\sum_{a,b}s_as_b h_a^\top h_b/n$ of its empirical feature-Gram entries equals the squared norm of the corresponding normalized signed mean feature. Thus

\[
\left.\frac{d^2}{dt^2}\|a(t)\|^2\right|_{t=0}
=2\eta^2\lambda^2\|h_0\|^2\ge\frac{\eta^2}{64},
\tag{12}
\]

and

\[
\left.\frac{d^2}{dt^2}\|H(t)\|^2\right|_{t=0}
=2\eta^2\left(\|a_0\|^2\|h_0\|^2+
                    \lambda^2\|W_0^\top h_0\|^2\right)
\ge\frac{\eta^2}{128}.
\tag{13}
\]

The lower bounds use $\|a_0\|^2,\|h_0\|^2\ge\lambda^2/2\ge1/16$.
The same complex disk supplies uniform Taylor-remainder bounds for $a,H$
and their squared norms. Hence there is one sufficiently small positive
$t_\eta\le T_0$, independent of $n,m$, at which both scalar Gram
averages have increased by a positive constant depending only on $\eta$.
This establishes motion of actual feature covariances at a nonvanishing
width scale in both layers. It does not establish nonlinear activation
behavior; the activation is exactly linear.

## Conditional comparison with dense-pair variability and tensor count

The following final step is conditional on the supervisor's separate
dense-pair sensitivity/concentration proof. Suppose that, for two independent
dense initializations on this same dataset and physical interval,

\[
D_{n,m}=O_{\mathbb P}\!\left(\sqrt{\frac{m+\log n}{n}}\right).
\tag{14}
\]

This is the appropriate proposed whole-unit-sphere benchmark when the input
dimension grows. A fixed-query $n^{-1/2}$ benchmark must not silently be
substituted for it.

Let $E_{n,m}(q)$ denote the left side of (10), or any larger prediction
error. If a deterministic order sequence attains

\[
E_{n,m}(q)=O_{\mathbb P}\!\left(\sqrt{\frac{m+\log n}{n}}\right),
\]

then (10), on events with probability tending to one, implies

\[
q\ge\frac1{2C_\eta}\log\frac{n}{m+\log n}-O_\eta(1).
\tag{15}
\]

Indeed the right side of (10) divided by the target scale would otherwise
be unbounded along a subsequence, contradicting tightness. For a constant
factor comparison with the realized $D_{n,m}$, the same argument gives
failure probability tending to one whenever the ratio of $q$ to
$\log[n/(m+\log n)]$ stays strictly below $1/(2C_\eta)$. No lower
bound or anti-concentration assumption for $D_{n,m}$ is needed.

If the hierarchy is stored as literal arrays, even after removing its zero
odd top rank it retains at least $m^{q-1}$ entries, and its declared
nonfrozen arrays include at least $m^{q-2}$ entries. Thus (15) gives

\[
\log S_{n,m}\ge
\frac{\log m}{2C_\eta}\log\frac{n}{m+\log n}
-O_\eta(\log m).
\tag{16}
\]

For $m=4\lfloor n^\alpha/4\rfloor$, with fixed $0<\alpha\le1/2$,
the right side is

\[
\left(\frac{\alpha(1-\alpha)}{2C_\eta}+o(1)\right)(\log n)^2.
\]

Therefore the literal tensor count is superpolynomial in $n$, conditional
on (14). This is an $\exp(c(\log n)^2)$ bound, not an
$\exp(cn)$ bound. Since these linear-network tensors have algebraic
structure, compressed representations may be substantially smaller. The
argument intentionally makes no claim about such representations or about
other closures.

## Scope and remaining obligations

The source rescaling, own-residual physical coefficient, common analytic
disk, feature-Gram gap, and actual hidden covariance motion are checked here.
The dense-pair variability bound (14) is a separate proof obligation; this
file does not import it as an established theorem.

The inputs, sample count and input dimension vary with width. Both hidden
activations are linear. Accordingly this is a different witness family from
the initial fixed-dataset nonlinear analytic request. A fixed label $\eta$
also eventually violates any earlier hypothesis of the form
$\eta\le C/m$; such a small-label theorem cannot be cited for this
family. The local analysis above uses only $0<\eta\le1$. Whether this
family answers the user's intended activation and dataset contract must be
stated explicitly in the parent synthesis.

The original analytic-activation search remains open. Gaussian return fields
can in principle destroy a width-uniform source Taylor radius, but poles of
an activation alone do not prove this: averaging over an initial Gaussian
can cancel apparent factorial coefficient growth. An admissible fixed
nonlinear dense witness would need a signed high-order estimate for the
actual source flow and a transfer to its own-residual physical evolution.
Neither was obtained in this bounded attempt.
