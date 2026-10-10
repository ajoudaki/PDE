# Finite-time coefficient sharpening: a rigorous obstruction to generic transfer

Status: bounded theory investigation, 2026-10-10. No stronger NTH lower
bound is proved here. The result below identifies what cannot be obtained
from polynomial degree, a linear-activation anchor, and coefficient-size
bounds alone. It does not claim the actual NTH coefficients exhibit the
constructed adverse behavior.

Inputs were the scoped assignment, the complete current
NONLINEAR_RESULT.md, and the author's NONLINEAR_WITNESS.md. No
experiment, Git operation, other study, or external scientific source
was used.

## The existing coefficient problem

Retain the canonical two-hidden-layer model, Gaussian initialization,
zero readout, fixed labels $(\eta,0)$, orthogonal inputs, and mobilities
$(n,1,n)$ from NONLINEAR_RESULT.md. Its activations are

\[
\phi_\varepsilon^{(1)}(z)=z+\varepsilon\sin z,\qquad
\phi^{(2)}(z)=z,\qquad \varepsilon\in I:=[1/8,1/4].
\]

The original rank-$q$ hierarchy freezes its top initialized tensor and
uses its own residual. Set $j=2\lfloor q/2\rfloor+1$. The first unmatched
physical prediction coefficient is

\[
J_{n,q}(\varepsilon)
=\frac{(\eta/2)^j}{j!}K_{j+1}^\varepsilon(1,\ldots,1)(0).
\tag{1}
\]

It has parameter degree at most $j+1$ and a simultaneous linear anchor
$J_{n,q}(0)\ge(\eta/16)^j$ on the stated Gaussian event.
The current parameter transfer and finite-remainder proof yield an
actual early-time prediction lower bound of the form

\[
\exp[-C_\eta q(\log(q+1)+\log\log n)]
\tag{2}
\]

along the specified geometric width sequence. A putative upgrade to
$\exp(-C_\eta q)$ would require information not supplied by generic
polynomial degree and the anchor alone.

## An exact obstruction, even with geometric coefficient bounds

There exists a deterministic sequence of real polynomials $p_r$ such
that, simultaneously:

1. $\deg p_r=r$ and $p_r(0)=1$;
2. the sum of the absolute values of the monomial coefficients of $p_r$
   is at most $9^r$;
3. for every single fixed $\varepsilon\in I$, infinitely many $r$ obey
   $|p_r(\varepsilon)|\le r^{-r}$.

Here is an explicit construction and proof. For each integer $\ell\ge0$
and each $r$ in the block $2^\ell\le r<2^{\ell+1}$, put

\[
a_r=\frac18+
\frac{r-2^\ell+1/2}{8\cdot2^\ell},
\qquad
p_r(\varepsilon)=\left(1-\frac{\varepsilon}{a_r}\right)^r.
\tag{3}
\]

The points $a_r$ in this block are the midpoints of the $2^\ell$
equal subintervals of $I$. Thus every $\varepsilon\in I$ has a
block index $r_\ell$ with

\[
|\varepsilon-a_{r_\ell}|
\le\frac1{16\cdot2^\ell},
\qquad
\left|1-\frac{\varepsilon}{a_{r_\ell}}\right|
\le\frac1{2^{\ell+1}}<\frac1{r_\ell}.
\]

The last strict inequality may be replaced by a weak one without
changing the conclusion. Raising it to $r_\ell$ proves property 3.
These indices lie in disjoint blocks and therefore tend to infinity.
Properties 1--2 follow directly from the binomial formula and
$a_r\ge1/8$:

\[
\sum_{s=0}^r|[\varepsilon^s]p_r|
=\left(1+\frac1{a_r}\right)^r\le9^r.
\]

In particular, for no fixed $\varepsilon\in I$ and no finite constant
$C_\varepsilon$ does
$|p_r(\varepsilon)|\ge e^{-C_\varepsilon r}$ hold for every sufficiently
large $r$. The obstruction persists even though the full coefficient
norm already has a geometric upper bound.

The degree and parity can be matched to (1). For odd $j\ge3$, define

\[
\widetilde p_j(\varepsilon)
=\left(\frac\eta{16}\right)^j
\left(1-\frac{\varepsilon}{a_{(j-1)/2}}\right)^{j+1}.
\tag{4}
\]

Its degree is $j+1$, its anchor equals $(\eta/16)^j$, and its
coefficient norm is at most $(\eta/16)^j9^{j+1}$. For every fixed
$\varepsilon$, infinitely many such $j$ satisfy

\[
|\widetilde p_j(\varepsilon)|
\le\left(\frac\eta{16}\right)^j
     \left(\frac3j\right)^{j+1}.
\tag{5}
\]

Indeed $j=2r+1$ and $1/r\le3/j$ for $r\ge1$.
Thus the additional parity and degree bookkeeping in the initialized
NTH coefficients does not by itself remove the obstruction.

The repeated root in (3) is deliberate: it is the extremal behavior that
a generic sublevel estimate must allow. To remove it in the NTH setting,
one needs specific information about those polynomials, for example a
bound on root multiplicities and clustering, a relation among consecutive
coefficients, or a signed representation. No such property is established
here. The constructed polynomials are not asserted to be NTH tensors.

## What generic interpolation can still prove

A weaker positive conclusion is available. Suppose $p_j$ are polynomials
of degree at most $Aj$ and $|p_j(0)|\ge c^j$, where $A,c>0$ are fixed.
Then, for almost every $\varepsilon\in I$,

\[
\limsup_{j\to\infty}|p_j(\varepsilon)|^{1/j}>0.
\tag{6}
\]

To prove this, suppose the set $E$ where the limsup is zero has
positive measure $\mu$. Fix a sufficiently small $\tau>0$. The sets

\[
E_N=\{\varepsilon\in E:
          |p_j(\varepsilon)|\le\tau^j
          \text{ for every }j\ge N\}
\]

increase to $E$. Hence some $E_N$ has measure at least $\mu/2$.
The already proved sublevel inequality gives, for every $j\ge N$,

\[
\frac\mu2
\le e\left(\frac{\tau^j}{c^j}\right)^{1/(Aj)}
=e(\tau/c)^{1/A}.
\]

Choosing $\tau<c(\mu/(4e))^A$ contradicts this inequality. This proves
(6).

The distinction between limsup and liminf is decisive. Equation (6)
provides some geometrically non-small coefficients at arbitrarily high
orders, but neither controls their spacing nor supplies a lower bound
at the first omitted order of a chosen hierarchy. Construction (3)
shows why an eventual geometric lower cannot be substituted. In the
finite-width problem one must additionally control how these favorable
orders depend on width and initialization.

## Finite physical time does not preserve polynomial parameter degree

The initial tensors have bounded polynomial degree in $\varepsilon$.
The finite-time predictions of the hierarchy do not inherit that degree.
This failure already occurs for the exact rank-two closure in the same
two-input model.

At zero readout its initialized kernel is the readout feature Gram.
Write

\[
A(\varepsilon)
=\frac{\phi_\varepsilon(W_0^{(1)}(e_1,e_2))}{\sqrt n}
=A_0+\varepsilon A_1,\qquad
K(\varepsilon)=A(\varepsilon)^\top W_0^\top W_0A(\varepsilon).
\]

The two-dimensional rank-two prediction vector satisfies exactly

\[
f^{(2)}(t,\varepsilon)
=y-\exp[-tK(\varepsilon)/2]\,y.
\tag{7}
\]

This is the closure with its own residual, not a prescribed-clock
substitution. For $n\ge2$, almost surely $W_0$ is invertible and $A_1$
has column rank two: its entries are independent continuous transforms
of independent Gaussians. Therefore the leading coefficient
$A_1^\top W_0^\top W_0A_1$ is positive definite, and
$\lambda_{\min}K(\varepsilon)\to\infty$ as real
$\varepsilon\to+\infty$. For every fixed $t>0$,

\[
f^{(2)}_1(t,\varepsilon)\longrightarrow\eta.
\]

But at $\varepsilon=0$ the same entry is
$\eta[1-(e^{-tK(0)/2})_{11}]<\eta$, since the exponential of a real
symmetric matrix is positive definite. Thus
$f^{(2)}_1(t,\varepsilon)$ is nonconstant and has a finite limit at
$+\infty$, so it is not a polynomial. It is an entire function of
$\varepsilon$; consequently it cannot agree with a polynomial even
on the nondegenerate interval $I$.

The extension to other real $\varepsilon$ in this argument is only an
algebraic test for polynomiality of (7); it does not alter the activation
parameter in the proposed witness. This example does not prove that
the dense-minus-closure error can never have a special cancellation.
It proves that no finite-degree claim for actual finite-time predictions
follows just from the degree of initialized tensors.

## Fixed finite horizons, fixed times, and the dense benchmark

Three statements must be separated.

First, the proved early-time lower is already a lower on every fixed
window $[0,T]$, $T>0$, because its witness interval eventually lies
inside that window. This restriction does not improve (2).

Second, replacing a dense benchmark $n^{-a_0}$ by a sharper
$n^{-1/2}$ benchmark changes only a constant in the order consequence
of (2). Solving
$C_\eta q(\log(q+1)+\log\log n)\gtrsim a\log n$ still gives the
scale $\log n/\log\log n$ for every fixed $a>0$. A better denominator
is useful but is not by itself a qualitatively stronger storage lower.

Third, a supremum over a fixed time window does not imply a lower
bound at any prescribed positive time. An elementary entire-function
example makes the distinction exact:

\[
g_n(t)=t\exp[-(\log n)^2t],\qquad n>1.
\]

Its supremum on any fixed positive window is eventually
$1/[e(\log n)^2]=n^{-o(1)}$, attained at
$t_n=(\log n)^{-2}$. Yet for every fixed $T>0$ and every $a>0$,
$g_n(T)=o(n^{-a})$. This is a logical counterexample to a time-quantifier
inference, not a claimed network trajectory.

For the actual odd-activation witness, the distinct passive query
$v=-e_1$ has exactly the same error magnitude as the first training
input at every time, as proved in NONLINEAR_RESULT.md. That identity
transfers an early-time or window supremum to the passive query, but
does not turn the supremum into a pointwise-in-time lower.

## Outcome

This investigation supplies a rigorous obstruction to upgrading the
fixed-parameter argument by generic Remez estimates alone, and it rules
out a simple finite-time polynomial-degree shortcut. It does not prove
that the actual NTH coefficients suffer the adverse construction, nor
that $\log n/\log\log n$ is optimal.

A genuine $\Omega(\log n)$ order lower requires additional information
about the actual nonlinear hierarchy: geometric error lower bounds on
a fixed interval or time, or sufficiently strong initialized-coefficient
structure together with a matching cancellation-aware remainder argument.
No such additional property has been established in this note.
