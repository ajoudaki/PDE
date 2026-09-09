# Failure of the scalar size-composition hierarchy on every positive horizon

## Statement and scope

Fix arbitrary \(T>0\), \(C>0\), \(C_0\ge1\), and \(0\le L<T\).
There exists a uniformly bounded family \(Y_{p,n}(t)\), for every
integer \(n\ge1\), \(p\in[0,1]\), and \(t\in[0,T]\), satisfying the
exact hierarchy in the question with those prescribed constants and
with width error zero. The family is nonnegative, nondecreasing in
deletion size, constant between deletion grid points, zero for
\(p<1/n\), continuously differentiable in time, and satisfies
\[
Y_{p,n}(0)=\partial_tY_{p,n}(0)=0.
\]
It has uniform deletion continuity through time \(L\), but its
small-deletion limit is strictly positive at an explicit time
\(t_0\in(L,T)\). Every nonempty finite-width deletion has positive
distance at every positive time.

The construction below verifies the proposed short-horizon mechanism.
The proposed midpoint \(3a\) is the **onset**, at which the limit is
still zero. We denote that onset by \(\tau\) and use a later time
\(t_0<T\) to witness strict positivity.

This result concerns only the sufficiency of the stated scalar
hierarchy. It is not a canonical-network trajectory, does not refute
the canonical network, and does not assert failure of the weighted-gate
estimate. No experiments, numerical runs, literature search, or agents
were used. All parameter choices and inequalities are exact.

The earlier audited file
SHARP_SIZE_COMPOSITION_HIERARCHY_TEST.md was left untouched.
Its SHA-256, checked before and after creating this companion, is:

    6776b73c5cac41655943dd78fe5d5721400570c26a6b8902eb6d93e8da4c9b54

## Exact hierarchy

Set
\[
h(p)=p\log(e/p)\quad(p>0),\qquad h(0)=0,
\]
\[
\Phi(x)=x[1+\tfrac12\log_+(1/x)]\quad(x>0),
\qquad \Phi(0)=0,\qquad A(y)=\min\{1,C_0y\}.
\]
Here \(\log_+z=\max\{0,\log z\}\). We use \(m\) for the interpolation
size, reserving \(a\) below for a time scale. For \(0\le m<1\), put
\(k=\lfloor nm\rfloor\), \(\theta=nm-k\), and define exactly
\[
J_n(m,u)=(1-\theta)\Phi(Y_{k/n,n}(u))
                  +\theta\Phi(Y_{(k+1)/n,n}(u)),
\qquad J_n(1,u)=\Phi(Y_{1,n}(u)).
\]
Write
\[
R_{p,n}(t)=
\left[Y_{p,n}(t)t\int_0^t J_n(A(Y_{p,n}(t)),u)\,du\right]^{1/2}.
\tag{1}
\]
We will prove the stronger differential inequality
\[
\partial_tY_{p,n}(t)
\le C\,[h(p)+\Phi(Y_{p,n}(t))+R_{p,n}(t)].
\tag{2}
\]
Integration from zero then gives precisely the required hierarchy.

The proof first creates a small linear size profile using the forcing,
then decreases its exponent slightly using the Osgood term. A fixed
interval of this historical profile produces a radical power strictly
below one. A sufficiently small flat positive addition is paid for by
that radical at large widths and by the forcing at the remaining widths.

## Parameters and family

Define
\[
a=\frac{L+T}{6},\qquad
\tau=3a=\frac{L+T}{2},\qquad
t_0=\frac{\tau+T}{2}=\frac{L+3T}{4}.
\tag{3}
\]
Since \(T>0\) and \(0\le L<T\), we have \(a>0\) and
\[
L<\tau<t_0<T,\qquad t_0-\tau=\frac{T-L}{4}.
\]
Use the continuously differentiable step
\[
S(v)=
\begin{cases}
0,&v\le0,\\
3v^2-2v^3,&0<v<1,\\
1,&v\ge1.
\end{cases}
\]
Its derivative on \([0,1]\) is \(6v(1-v)\); thus
\[
0\le S\le1,\qquad 0\le S'\le\tfrac32,
\qquad S'(0)=S'(1)=0.
\tag{4}
\]
Choose
\[
\varepsilon=\min\{\tfrac12,Ca/12\},\qquad
\alpha(t)=1-\varepsilon S((t-a)/a),\qquad
\alpha_*=1-\varepsilon,
\]
\[
\gamma=\frac{1+\alpha_*}{2}=1-\frac{\varepsilon}{2},
\qquad \delta=1-\gamma=\frac{\varepsilon}{2},
\qquad b=\min\{\tfrac18,Ca/6\}.
\tag{5}
\]
In particular,
\[
0<\varepsilon\le\tfrac12,\quad
\tfrac12\le\alpha_*<1,\quad
0<\delta\le\tfrac14,\quad
\tfrac34\le\gamma<1,\quad b>0.
\]
Set the integer width threshold and the radical coefficient to be
\[
N=\left\lceil b^{-1/\varepsilon}\right\rceil,
\qquad K=a\sqrt{3b/2},
\tag{6}
\]
and choose the positive amplitude
\[
d=\min\left\{
\tfrac18,\ \frac{C}{4N},\quad
\left(\frac{CK\delta^2}{4}\right)^{1/\delta}
\right\}.
\tag{7}
\]
All quantities in (5)--(7) are finite and strictly positive. In
particular, \(N\) is a finite integer; no rounding other than the
displayed exact ceiling is intended. Since \(b\le1/8\) and
\(\varepsilon\le1/2\), we also have \(N\ge64\).

Define
\[
F(s)=
\begin{cases}
d e^{-1/s},&s>0,\\
0,&s\le0.
\end{cases}
\tag{8}
\]
For \(p\ge1/n\), put \(r=\lfloor np\rfloor/n\) and set
\[
Y_{p,n}(t)=bS(t/a)r^{\alpha(t)}+F(t-\tau).
\tag{9}
\]
For \(p<1/n\), set \(Y_{p,n}(t)=0\).

This defines all widths, including \(n=1\), and the endpoint \(p=1\).
The family is nondecreasing in \(p\), constant on each
\([k/n,(k+1)/n)\), and obeys
\[
0\le Y_{p,n}(t)\le b+d\le\tfrac14<1.
\tag{10}
\]
It is also nondecreasing in time: \(S\) and \(F\) increase,
\(\alpha\) decreases, and \(0<r\le1\).

The function \(F\) is smooth and flat at zero. Indeed, each of its
right derivatives is an exponential \(e^{-1/s}\) times a polynomial
in \(1/s\). For each integer \(j\ge0\),
\(x^j e^{-x}\to0\) as \(x\to\infty\), because
\(e^x\ge x^{j+1}/(j+1)!\). Thus these derivatives match the zero
derivatives on the left. Together with (4), this proves that every
time path in (9) is continuously differentiable, including at
\(a,2a,\tau\). At zero, \(S(0)=S'(0)=0\),
\(\alpha=1\) near zero, and \(F(t-\tau)=0\); hence both initial
values and initial time derivatives vanish.

## Flat-function bounds

For \(s>0\), direct differentiation and \(\gamma=1-\delta\) give
\[
F'(s)=d s^{-2}e^{-1/s},\qquad
\frac{F'(s)}{F(s)^\gamma}
=d^\delta s^{-2}e^{-\delta/s}.
\]
The elementary exponential-series inequality \(e^z\ge z^2/2\)
implies \(z^2e^{-z}\le2\) for \(z\ge0\). Applying this first at
\(z=1/s\), then at \(z=\delta/s\), yields
\[
F'(s)\le2d,\qquad
F'(s)\le\frac{2d^\delta}{\delta^2}F(s)^\gamma.
\tag{11}
\]
For \(s\le0\), \(F'(s)=F(s)=0\), so both inequalities also hold.
The amplitude choice (7) therefore ensures
\[
F'(s)\le\frac{C}{2N},\qquad
F'(s)\le\frac{CK}{2}F(s)^\gamma.
\tag{12}
\]
For the second bound, raising (7) to the positive power \(\delta\)
gives \(d^\delta\le CK\delta^2/4\).

## The forcing and Osgood preparation phases

Fix \(p\ge1/n\). On \(0<t<a\), we have
\(\alpha(t)=1\) and \(F(t-\tau)=0\), so
\[
\partial_tY_{p,n}(t)
=\frac b a S'(t/a)r
\le\frac{3b}{2a}r
\le\frac C4 r
\le\frac C4 h(p).
\tag{13}
\]
Here \(r\le p\le h(p)\) on \([0,1]\).

On \(a<t<2a\), the step in the amplitude is already one. Write
\(B=b r^{\alpha(t)}=Y_{p,n}(t)\). Since
\(\varepsilon\le Ca/12\),
\[
0\le-\alpha'(t)
=\frac{\varepsilon}{a}S'((t-a)/a)
\le\frac{3\varepsilon}{2a}\le\frac C8.
\]
Consequently,
\[
\partial_tY_{p,n}(t)
=(-\alpha'(t))B\log(1/r)
\le\frac C8 B\log(1/r).
\tag{14}
\]
On the other hand, \(0<B\le b<1\) and \(\alpha(t)\ge\alpha_*\)
give
\[
\Phi(B)
\ge\tfrac12 B\log(1/B)
\ge\tfrac{\alpha_*}{2}B\log(1/r)
\ge\tfrac14 B\log(1/r).
\tag{15}
\]
Thus (14) is at most \(C\Phi(B)/2\).
For \(2a\le t\le\tau=3a\), the profile is stationary:
\[
Y_{p,n}(t)=b r^{\alpha_*}.
\tag{16}
\]
These arguments establish (2) through time \(\tau\). The phase
endpoints are included by continuous differentiability.

## Exact interpolation and the width threshold

We first prove the needed interpolation bound without imposing it
below the first grid point. The function \(\Phi\) is increasing:
on \(0<x<1\) its derivative is
\(\tfrac12[1+\log(1/x)]>0\); on \(x>1\) its derivative is one;
and the function is continuous at zero and one. Also \(\Phi(x)\ge x\).

For \(u\in[2a,3a]\), including both endpoints, (16) gives
\[
Y_{k/n,n}(u)=b(k/n)^{\alpha_*}
\qquad (k=0,\ldots,n).
\tag{17}
\]
For \(1/n\le m<1\), let \(k=\lfloor nm\rfloor\ge1\). The
inequality \(nm<k+1\le2k\) implies \(k/n\ge m/2\). The two
values being interpolated are ordered, so
\[
\begin{aligned}
J_n(m,u)
&\ge \Phi(Y_{k/n,n}(u))
\ge b(k/n)^{\alpha_*}\\
&\ge b\,2^{-\alpha_*}m^{\alpha_*}
\ge \frac b2 m^{\alpha_*}.
\end{aligned}
\tag{18}
\]
The final comparison uses \(\alpha_*\le1\). At \(m=1\), the
separate endpoint definition gives \(J_n(1,u)=\Phi(b)\ge b\),
which also implies (18). Thus (18) holds on the entire interval
\([1/n,1]\), including the first grid point and the last endpoint.
No lower bound (18) is asserted for \(0<m<1/n\).

Suppose now that \(n\ge N\), \(p\ge1/n\), and \(t\ge\tau\).
Writing \(y=Y_{p,n}(t)\), the ceiling in (6) implies
\[
y\ge b n^{-\alpha_*}
=\frac{b n^\varepsilon}{n}
\ge\frac1n,
\tag{19}
\]
because \(n\ge N\ge b^{-1/\varepsilon}\). By (10) and \(C_0\ge1\),
\[
A(y)\ge y\ge1/n.
\]
We may therefore apply (18) at the current cutoff \(A(y)\) for
every historical time \(u\in[2a,3a]\). This interval has length
\(a\), lies inside \([0,t]\), and \(t\ge3a\). Formula (1) yields
\[
\begin{aligned}
R_{p,n}(t)^2
&\ge yt\int_{2a}^{3a}\frac b2 A(y)^{\alpha_*}\,du\\
&\ge\frac{3a^2b}{2}y^{1+\alpha_*}
=K^2 y^{2\gamma}.
\end{aligned}
\]
Hence
\[
R_{p,n}(t)\ge K Y_{p,n}(t)^\gamma
\qquad(n\ge N,\ p\ge1/n,\ t\ge\tau).
\tag{20}
\]
This includes saturation \(A(y)=1\) and the threshold width
\(n=N\); neither requires a strict inequality in (19).

For \(t\ge\tau\), the baseline is constant in time. Equations (12)
and (20) show, for \(n\ge N\),
\[
\partial_tY_{p,n}(t)
=F'(t-\tau)
\le\frac{CK}{2}F(t-\tau)^\gamma
\le\frac C2 R_{p,n}(t).
\tag{21}
\]
For the remaining integer widths \(1\le n<N\), every nonempty
deletion satisfies \(h(p)\ge p\ge1/n>1/N\). Therefore the other
bound in (12) gives
\[
\partial_tY_{p,n}(t)
=F'(t-\tau)
\le\frac C{2N}\le\frac C2 h(p).
\tag{22}
\]
All possible nonempty below-floor cutoff cases after \(\tau\)
are covered by these small widths; (22) uses no interpolation
bound. In particular, there is no omission at any integer width.

## Verification and failure within the prescribed horizon

Equations (13)--(16), (21), and (22) prove (2) at every nonempty
size and time, including the phase endpoints. At \(p<1/n\),
the path and its derivative are zero and the right side of (2)
is nonnegative. For fixed \(n\), interpolation is jointly continuous
in size and time, so the radical is continuous in time; all
integrals below are well defined. Using the zero initial values,
integration of (2) proves
\[
Y_{p,n}(t)\le C\left[
t h(p)+\int_0^t\Phi(Y_{p,n}(s))\,ds
       +\int_0^tR_{p,n}(s)\,ds
\right],\qquad 0\le t\le T.
\tag{23}
\]
The constant is the prescribed \(C\), without time rescaling.

For \(0\le t\le\tau\), the added term is zero and
\(\alpha(t)\ge\alpha_*>0\). Thus for every \(0\le\eta\le1\),
\[
\sup_{n\ge1}\ \sup_{0\le p\le\eta}\ \sup_{0\le t\le\tau}
Y_{p,n}(t)\le b\eta^{\alpha_*}.
\tag{24}
\]
Indeed, at nonempty sizes,
\(r^{\alpha(t)}\le r^{\alpha_*}\le p^{\alpha_*}\); empty sizes
are zero. Letting \(\eta\downarrow0\) proves uniform deletion
continuity through \(\tau\), and therefore through the prescribed
\(L<\tau\). Nevertheless, for each fixed nonempty deletion and
every \(t>0\), the baseline in (9) is positive since \(S(t/a)>0\).

For fixed \(p>0\), the floors satisfy \(\lfloor np\rfloor/n\to p\),
so
\[
\lim_{n\to\infty}Y_{p,n}(t)
=bS(t/a)p^{\alpha(t)}+F(t-\tau).
\]
Since \(\alpha(t)\ge\alpha_*>0\), taking \(p\downarrow0\) gives
\[
\lim_{p\downarrow0}\lim_{n\to\infty}Y_{p,n}(t)
=F(t-\tau).
\tag{25}
\]
The same limit holds along singleton deletions, directly from
\[
Y_{1/n,n}(t)
=bS(t/a)n^{-\alpha(t)}+F(t-\tau),
\qquad \alpha(t)\ge\alpha_*>0.
\tag{26}
\]
At the specified witness \(t_0=(L+3T)/4\in(L,T)\), (3) and (8) give
\[
\lim_{p\downarrow0}\lim_{n\to\infty}Y_{p,n}(t_0)
=\lim_{n\to\infty}Y_{1/n,n}(t_0)
=d\exp\left(-\frac4{T-L}\right)>0.
\tag{27}
\]
The limiting profile is zero through \(\tau\), is smooth and flat
at \(\tau\), and is positive for every \(\tau<t\le T\).

Thus every prescribed positive horizon and every prescribed positive
hierarchy constant admit this scalar failure, while preserving
deletion continuity on any prescribed shorter initial interval.
The potentially tiny exponent change, very large finite width
threshold, and very small positive amplitude introduce no limiting
assumption: they are fixed finite parameters once \(T,C,L\) are fixed.
No conclusion about realizability by canonical-network dynamics is
made.
