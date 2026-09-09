# The sharp size-composition hierarchy permits delayed loss of deletion continuity

## Result and scope

For every prescribed \(C>0\) and \(C_0\ge1\), the hierarchy in the
question admits a uniformly bounded, nonnegative family satisfying all
the stated finite-floor conditions, with zero initial values and zero
initial time derivatives, such that:

- deletion continuity holds uniformly on a nonzero initial time interval;
- every nonempty finite-width deletion has a positive distance at every
  positive time, including on that initial interval;
- after a later onset, the small-deletion limit is strictly positive.

The limiting onset is smooth and flat: all its time derivatives vanish
at the onset. The initial interval of deletion continuity can be made
longer than any prescribed finite interval.

This is a counterexample to the sufficiency of the stated **scalar
inequality alone**. It is not a canonical-network trajectory and does
not refute the canonical network, the new weighted-gate estimate, or
any additional dynamical identities. No Hardy integral is used.

All arguments below are elementary analytic inequalities. No experiments,
numerical computations, literature search, or agents were used. Task
work was confined to the requested temporary directory, apart from the
explicitly requested reading of the solve-math-rigorously skill. The
permitted old scalar note was read only for context; no other proof or
master was edited.

## Setup and proof architecture

Use exactly the functions in the question:
\[
h(p)=p\log(e/p),\qquad
\Phi(x)=x\bigl[1+\tfrac12\log_+(1/x)\bigr],
\qquad h(0)=\Phi(0)=0,
\]
and \(A(y)=\min\{1,C_0y\}\). Throughout, \(n\ge1\) is an integer,
\(p\in[0,1]\), and \(t\ge0\). For any family \(V\), write \(J_n^V\)
for the specified interpolation: for \(0\le a<1\), set
\(k=\lfloor na\rfloor\), \(\theta=na-k\), and
\[
J_n^V(a,u)=(1-\theta)\Phi(V_{k/n,n}(u))
                 +\theta\Phi(V_{(k+1)/n,n}(u)),
\qquad J_n^V(1,u)=\Phi(V_{1,n}(u)).
\]
Set
\[
R^V_{p,n}(t)
=\left[V_{p,n}(t)t\int_0^t
J_n^V\bigl(A(V_{p,n}(t)),u\bigr)\,du\right]^{1/2}.
\tag{1}
\]

We first construct a family \(Z\) with
\[
\partial_t Z_{p,n}(t)
\le h(p)+\Phi(Z_{p,n}(t))+R^Z_{p,n}(t).
\tag{2}
\]
The forcing first creates a profile proportional to \(p\). The Osgood
term then changes its exponent to \(1/2\). A fixed interval of this
\(\sqrt p\) profile supplies a lower bound proportional to
\(Z_{p,n}^{3/4}\) for the radical. This pays for a subsequent flat
positive addition. Small widths are handled directly by the forcing.
Finally, time rescaling gives every prescribed \(C>0\).

## The explicit family

Define the continuously differentiable function
\[
S(v)=
\begin{cases}
0,&v\le0,\\
3v^2-2v^3,&0<v<1,\\
1,&v\ge1.
\end{cases}
\]
On \([0,1]\), \(S'(v)=6v(1-v)\), so
\[
0\le S\le1,\qquad 0\le S'\le\tfrac32,
\qquad S'(0)=S'(1)=0.
\tag{3}
\]
Put
\[
b=\tfrac18,\qquad d=64^{-4},\qquad
\alpha(t)=1-\tfrac12 S\bigl((t-1)/3\bigr),
\]
\[
F(s)=
\begin{cases}
d e^{-1/s},&s>0,\\
0,&s\le0.
\end{cases}
\tag{4}
\]
Thus \(1/2\le\alpha\le1\), with \(\alpha=1\) on \(t\le1\),
\(\alpha=1/2\) on \(t\ge4\), and
\[
0\le-\alpha'(t)\le\tfrac14.
\tag{5}
\]
For \(p\ge1/n\), let \(r=\lfloor np\rfloor/n\), and define
\[
Z_{p,n}(t)=bS(t)r^{\alpha(t)}+F(t-5).
\tag{6}
\]
For \(p<1/n\), define \(Z_{p,n}(t)=0\).

The family is nondecreasing in deletion size, constant on each
\([k/n,(k+1)/n)\), and zero below \(1/n\). It is also nondecreasing in
time, though that extra property is not required. It satisfies
\[
0\le Z_{p,n}(t)\le b+d<1,
\qquad Z_{p,n}(0)=\partial_t Z_{p,n}(0)=0.
\tag{7}
\]
Each time path is continuously differentiable. The function \(F\) is
smooth and flat at zero: each right derivative is \(e^{-1/s}\) times a
polynomial in \(1/s\), and every such product tends to zero. Indeed,
for any nonnegative integer \(m\), the exponential series gives
\(e^x\ge x^{m+1}/(m+1)!\), so \(x^m e^{-x}\to0\).

Two useful bounds, valid also at \(s=0\), are
\[
0\le F'(s)\le2d,
\qquad F'(s)\le\tfrac12 F(s)^{3/4}.
\tag{8}
\]
For \(s>0\), write \(x=1/s\). The inequality
\(e^x\ge x^2/2\) gives
\(F'(s)=d x^2e^{-x}\le2d\). For the second bound, set
\(z=1/(4s)\) and use \(d^{1/4}=1/64\):
\[
\frac{F'(s)}{F(s)^{3/4}}
=\frac1{64}s^{-2}e^{-1/(4s)}
=\tfrac14 z^2e^{-z}\le\tfrac12.
\]
For \(s<0\), both sides in (8) are zero.

## Generating the size profile using only the stated terms

Fix a nonempty deletion, so \(r\in[1/n,1]\).
For \(0<t<1\), (6) is \(Z_{p,n}(t)=bS(t)r\), and hence
\[
\partial_t Z_{p,n}(t)
\le\tfrac{3}{16}r\le h(p),
\tag{9}
\]
because \(r\le p\le h(p)\) on \([0,1]\).

For \(1<t<4\), write \(B=b r^{\alpha(t)}=Z_{p,n}(t)\). Then
\[
\partial_t Z_{p,n}(t)
=(-\alpha'(t))B\log(1/r)
\le\tfrac14B\log(1/r).
\]
Since \(0<B\le b<1\),
\[
\Phi(B)
\ge\tfrac12B\log(1/B)
\ge\tfrac12\alpha(t)B\log(1/r)
\ge\tfrac14B\log(1/r).
\tag{10}
\]
Thus the Osgood term alone pays for this phase. For \(4\le t\le5\),
the profile is stationary and equals \(b\sqrt r\). At the phase
endpoints the same bounds hold by continuity. In particular, (2)
is established up to time \(5\).

## The exact interpolation bound and the finite floor

The function \(\Phi\) is increasing: its derivative on \((0,1)\) is
\(\tfrac12[1+\log(1/x)]>0\), its derivative on \((1,\infty)\) is
\(1\), and it is continuous at \(0\) and \(1\). Also \(\Phi(x)\ge x\).

For every \(u\in[4,5]\), the grid values are exactly
\[
Z_{k/n,n}(u)=b\sqrt{k/n}\qquad (k=0,\ldots,n).
\tag{11}
\]
For \(1/n\le a<1\), let \(k=\lfloor na\rfloor\ge1\). Since
\(na<k+1\le2k\), we have \(k/n\ge a/2\). The interpolation is a
convex combination of two ordered values of \(\Phi\), so
\[
J_n^Z(a,u)
\ge\Phi(Z_{k/n,n}(u))
\ge b\sqrt{k/n}
\ge\frac b{\sqrt2}\sqrt a.
\tag{12}
\]
At \(a=1\), the separately defined endpoint is \(\Phi(b)\ge b\),
so (12) holds there as well. No version of (12) is asserted for
\(0<a<1/n\).

Now suppose \(n\ge64\), \(p\ge1/n\), and \(t\ge5\). Write
\(y=Z_{p,n}(t)\). The prepared baseline gives
\[
y\ge\frac b{\sqrt n}\ge\frac1n.
\tag{13}
\]
Because \(y<1\) and \(C_0\ge1\),
\[
A(y)=\min\{1,C_0y\}\ge y\ge1/n.
\]
Therefore (12) is applicable at the actual, current cutoff \(A(y)\)
throughout the fixed historical interval \(u\in[4,5]\). Formula (1)
gives
\[
\begin{aligned}
R^Z_{p,n}(t)^2
&\ge yt\int_4^5\frac b{\sqrt2}\sqrt{A(y)}\,du\\
&\ge\frac{5b}{\sqrt2}\,y^{3/2}.
\end{aligned}
\]
Consequently,
\[
R^Z_{p,n}(t)
\ge\sqrt{\frac5{8\sqrt2}}\,y^{3/4}
\ge\tfrac12y^{3/4},
\tag{14}
\]
where the last comparison is equivalent to \(5\ge2\sqrt2\).
As the baseline is now constant, (8) and \(y\ge F(t-5)\) imply
\[
\partial_t Z_{p,n}(t)
=F'(t-5)\le\tfrac12F(t-5)^{3/4}
\le R^Z_{p,n}(t).
\tag{15}
\]

For the remaining widths \(1\le n<64\), and any nonempty deletion,
\(h(p)\ge p\ge1/n>1/64\). Thus (8) gives instead
\[
\partial_t Z_{p,n}(t)=F'(t-5)
\le2d\le1/64\le h(p)\qquad(t\ge5).
\tag{16}
\]
For \(t\ge5\), these small widths include every possible nonempty
below-floor case. This argument uses no below-floor interpolation
estimate.

Together, (9), (10), (15), and (16) prove (2) for every nonempty
deletion and every time. For \(p<1/n\), the derivative and radical
are zero, and (2) holds as well. Integrating (2) from zero proves
the stated integral hierarchy with \(C=1\), with width error exactly
zero. The integrands are continuous in time: finite piecewise-linear
interpolation is continuous in its size argument and in the time paths.

## Every prescribed positive constant

Fix any
\[
0<\lambda\le\min\{1,C\},\qquad
Y_{p,n}(t)=Z_{p,n}(\lambda t).
\tag{17}
\]
The same \(C_0\) is used in both radicals. Interpolation commutes
with this time change:
\[
J_n^Y(a,u)=J_n^Z(a,\lambda u).
\]
The substitution \(v=\lambda u\) in (1) therefore gives the exact
identity
\[
R^Y_{p,n}(t)=\lambda^{-1}R^Z_{p,n}(\lambda t).
\tag{18}
\]
Using (2), \(\lambda\le C\), and \(\lambda^2\le\lambda\le C\),
\[
\begin{aligned}
\partial_t Y_{p,n}(t)
&\le\lambda h(p)+\lambda\Phi(Y_{p,n}(t))
       +\lambda^2R^Y_{p,n}(t)\\
&\le C\bigl[h(p)+\Phi(Y_{p,n}(t))+R^Y_{p,n}(t)\bigr].
\end{aligned}
\]
Since \(Y_{p,n}(0)=0\), integration proves exactly
\[
Y_{p,n}(t)\le C\left[
t h(p)+\int_0^t\Phi(Y_{p,n}(s))\,ds
       +\int_0^tR^Y_{p,n}(s)\,ds\right].
\tag{19}
\]
All floor, boundedness, monotonicity, and initial-derivative properties
are preserved by the time change.

## Delayed continuity and its later failure

Let \(T_*=5/\lambda\). Before and at this onset, \(F(\lambda t-5)=0\).
Since \(\alpha\ge1/2\), for every \(\varepsilon\in[0,1]\),
\[
\sup_{n\ge1}\ \sup_{0\le p\le\varepsilon}\quad
\sup_{0\le t\le T_*}Y_{p,n}(t)
\le b\sqrt\varepsilon.
\tag{20}
\]
For nonempty deletions, this uses
\(r^{\alpha(\lambda t)}\le\sqrt r\le\sqrt p\); empty deletions are zero.
Thus deletion continuity holds uniformly on this entire initial
interval. Nevertheless, for any fixed nonempty finite-width deletion,
\(Y_{p,n}(t)>0\) whenever \(t>0\), because \(S(\lambda t)>0\).
The construction does not assume zero finite-\(p\) distances on the
previously controlled interval.

For fixed \(p>0\), \(\lfloor np\rfloor/n\to p\), and hence
\[
\lim_{n\to\infty}Y_{p,n}(t)
=bS(\lambda t)p^{\alpha(\lambda t)}+F(\lambda t-5).
\]
Taking \(p\downarrow0\) yields
\[
\lim_{p\downarrow0}\lim_{n\to\infty}Y_{p,n}(t)
=F(\lambda t-5)=
\begin{cases}
0,&0\le t\le T_*,\\
d e^{-1/(\lambda t-5)}>0,&t>T_*.
\end{cases}
\tag{21}
\]
The same failure occurs along singleton deletions, since
\[
Y_{1/n,n}(t)
=bS(\lambda t)n^{-\alpha(\lambda t)}+F(\lambda t-5)
\longrightarrow F(\lambda t-5).
\tag{22}
\]
For any prescribed finite initial interval \([0,L]\), take
\(\lambda\le\min\{1,C,5/L\}\) when \(L>0\); then \(T_*\ge L\).
The limiting profile in (21) is smooth and flat at \(T_*\), yet
strictly positive immediately afterward.

The loss of continuity here comes from a size exponent generated by
the Osgood term and then evaluated at the current distance through
the exact size interpolation. It does not require the extra logarithm
of the old Hardy majorant. This establishes insufficiency of the new
scalar hierarchy under precisely the assumptions given; it makes no
claim of failure for the canonical network.
