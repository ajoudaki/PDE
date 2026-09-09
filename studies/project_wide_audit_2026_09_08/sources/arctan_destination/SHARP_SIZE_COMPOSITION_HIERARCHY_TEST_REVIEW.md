# Independent adversarial mathematical audit

**Verdict: PASS for the complete stated scalar result.** No mathematical correction is required. The construction satisfies the explicitly displayed integral hierarchy (19), with width error zero, for every real $C>0$ and $C_0\ge1$, all integers $n\ge1$, every $p\in[0,1]$, and all finite $t\ge0$. Its boundedness, finite-floor properties, zero initial value and first time derivative, positive finite-width distances, delayed uniform deletion continuity, and smooth positive limiting onset all hold.

Audited input:

`/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/SHARP_SIZE_COMPOSITION_HIERARCHY_TEST.md`

Exact SHA-256 of the audited bytes:

```text
6776b73c5cac41655943dd78fe5d5721400570c26a6b8902eb6d93e8da4c9b54
```

I read the complete candidate and the solve-math-rigorously skill. I used no other mathematical sources, earlier counterexamples, ledgers, reviews, agents, or history, and performed no experiments. The input was not edited. This verdict concerns the self-contained scalar statement in the candidate; it makes no assertion about realization by a network or satisfaction of additional dynamical identities.

The proof closes in three stages: the forcing creates a positive size profile, the Φ term changes its exponent, and the exact interpolated history pays for the flat addition. The finite floor is respected in the last stage by treating widths below 64 separately. The time change and the deletion limits can then be checked exactly.

## 1. Domains, regularity, floors, and initial conditions

For a nonempty deletion, $p\ge1/n$, the quantity $r=\lfloor np\rfloor/n$ satisfies

\[
0<1/n\le r\le p\le1.
\]

The formula involving $r^{\alpha(t)}$ is only differentiated when $r>0$; no logarithm of zero is used. The separate branch $p<1/n$ is identically zero. For $p=1$, the definition gives $r=1$, so the final endpoint is covered as well.

On $0<v<1$, $S'(v)=6v(1-v)$ lies between 0 and $3/2$. The polynomial values and first derivatives agree with the constant extensions at both endpoints. Thus (3) is correct, $S\in C^1(\mathbb R)$, and

\[
\alpha'(t)=-\tfrac16 S'((t-1)/3),\qquad
\tfrac12\le\alpha(t)\le1,\qquad
0\le-\alpha'(t)\le\tfrac14.
\]

This verifies (5), including the endpoints $t=1,4$. The exponent is 1 for $t\le1$ and $1/2$ for $t\ge4$.

For each fixed $p,n$, the nonzero branch is $C^1$, because $r^{\alpha(t)}=\exp(\alpha(t)\log r)$, and $F$ is smooth as checked below. Its time derivative is nonnegative: $S'\ge0$, $\alpha'\log r\ge0$, and $F'\ge0$. At each fixed time, $r\mapsto r^{\alpha(t)}$ is increasing. Addition of the same nonnegative $F(t-5)$ to every nonempty grid cell preserves size monotonicity, including the jump from the zero cell. Hence the family is nondecreasing in size, constant on the stated half-open grid cells, zero below $1/n$, and nondecreasing in time.

The bounds $0\le S\le1$, $r^{\alpha}\le1$, and $0\le F\le d$ give $0\le Z\le b+d<1$, independently of $p,n,t,C_0$. Near time zero the nonempty branch is exactly

\[
Z_{p,n}(t)=br(3t^2-2t^3).
\]

Consequently $Z_{p,n}(0)=\partial_tZ_{p,n}(0)=0$; the empty branch has the same initial conditions. At $t=1,4,5$, the vanishing endpoint derivatives of $S$ and the flatness of $F$ give the claimed $C^1$ matching. No higher initial derivatives of finite-width paths are asserted or needed: the initial condition in (7) is explicitly a first-derivative condition. The all-orders flatness claim concerns the limiting onset.

## 2. Flatness and the two bounds on the added term

For $s>0$, write $x=1/s$. Then

\[
F'(s)=d s^{-2}e^{-1/s}=d x^2e^{-x}\ge0.
\]

Every derivative of $e^{-1/s}$ on $s>0$ is $e^{-1/s}$ times a polynomial in $1/s$. Indeed, differentiation of $e^{-x}P(x)$, with $dx/ds=-x^2$, gives $e^{-x}x^2(P(x)-P'(x))$, again of this form. For every integer $m\ge0$, the exponential-series inequality yields

\[
0\le x^me^{-x}\le\frac{(m+1)!}{x}\longrightarrow0
\quad(x\to\infty).
\]

These derivative expressions, and their difference quotients at zero, tend to zero. The extension by zero on $s\le0$ is therefore $C^\infty$, with $F^{(j)}(0)=0$ for every integer $j\ge0$.

The inequality $e^x\ge x^2/2$ implies $F'(s)\le2d$. For the other bound, $d^{1/4}=1/64$ and $z=1/(4s)>0$ give exactly

\[
\frac{F'(s)}{F(s)^{3/4}}
=\frac1{64}s^{-2}e^{-1/(4s)}
=\frac14z^2e^{-z}\le\frac12.
\]

At $s=0$ the desired inequality follows from $F(0)=F'(0)=0$, without division; on $s<0$ both sides are zero. Thus all of (8) holds on the full real domain used by the construction.

## 3. The differential hierarchy through time 5

For $0<p\le1$, $h(p)=p[1+\log(1/p)]\ge p$; the value at zero is defined separately as zero.

For $0<t<1$, $\alpha=1$ and $F(t-5)=0$, so

\[
\partial_tZ=bS'(t)r\le\frac3{16}r\le p\le h(p).
\]

This proves (9) for every nonempty deletion, including $n=1,p=1$.

For $1<t<4$, $S(t)=1$ and $F(t-5)=0$. With $B=br^{\alpha(t)}\in(0,b]$,

\[
\partial_t Z=(-\alpha')B\log(1/r)
\le\tfrac14B\log(1/r).
\]

Moreover $B<1$ and

\[
\log(1/B)=\log(1/b)+\alpha(t)\log(1/r)
\ge\alpha(t)\log(1/r).
\]

It follows that

\[
\Phi(B)\ge\tfrac12B\log(1/B)
\ge\tfrac12\alpha(t)B\log(1/r)
\ge\tfrac14B\log(1/r).
\]

All signs in (10) are correct; at $r=1$ the logarithmic derivative is zero. On $4\le t\le5$ the profile is stationary at $b\sqrt r$. At $t=0,1,4,5$, the same differential inequality holds directly, since the relevant derivatives vanish. Thus (2) holds through time 5 without any lower bound on the radical.

## 4. Exact interpolation and the large-width radical bound

For $0<x<1$,

\[
\Phi'(x)=\tfrac12[1+\log(1/x)]>0;
\]

for $x>1$, $\Phi'(x)=1$. The function is continuous at 1 and at 0, with the latter following from $x\log(1/x)\to0$. Thus it is increasing on $[0,\infty)$, although differentiability at 1 is neither true nor needed. Also $\Phi(x)\ge x\ge0$ on this domain.

Throughout $u\in[4,5]$, the grid values are exactly $b\sqrt{k/n}$ for every $k=0,\ldots,n$. The $k=0$ identity uses the empty branch; the remaining identities use $α=1/2$, $S=1$, and $F=0$. There is no grid approximation in (11).

Take $1/n\le a<1$. Then $k=\lfloor na\rfloor\ge1$, $0\le\theta=na-k<1$, and

\[
na<k+1\le2k,\qquad k/n\ge a/2.
\]

The two interpolated values are ordered, so their convex combination is at least its lower endpoint. Consequently

\[
J_n^Z(a,u)
\ge\Phi(b\sqrt{k/n})
\ge b\sqrt{k/n}
\ge\frac b{\sqrt2}\sqrt a.
\]

This proves (12) for every stated interior argument, including grid points. At $a=1$, the separate interpolation definition gives $J_n^Z(1,u)=\Phi(b)\ge b\ge b/\sqrt2$. This also handles saturation of $A$. For $n=1$, the interval $1/n\le a<1$ is empty, and the endpoint argument still applies.

There is no illicit extension below the first grid point. In fact, for $0<a<1/n$ and $u\in[4,5]$, the exact interpolation is

\[
J_n^Z(a,u)=na\,\Phi(b/\sqrt n),
\]

which does not have a uniform positive multiple of $\sqrt a$ as a lower bound all the way to zero. The candidate never uses (12) in this region.

For $n\ge64$, $p\ge1/n$, and $t\ge5$, put $y=Z_{p,n}(t)$. Then

\[
y\ge b\sqrt r\ge\frac1{8\sqrt n}\ge\frac1n,
\]

where the last inequality is equivalent to $\sqrt n\ge8$. Equality is allowed at $n=64$; thus this boundary width is covered. Since $y<1$ and $C_0\ge1$, both 1 and $C_0y$ are at least $y$, and hence

\[
A(y)=\min\{1,C_0y\}\ge y\ge1/n.
\]

The cutoff in the history integral is the current value $A(y)$, held fixed as $u$ varies. Applying the interpolation bound at exactly that cutoff throughout the prepared interval gives

\[
\begin{aligned}
(R^Z_{p,n}(t))^2
&=yt\int_0^t J_n^Z(A(y),u)\,du\\
&\ge yt\int_4^5\frac b{\sqrt2}\sqrt{A(y)}\,du\\
&\ge\frac{5b}{\sqrt2}y^{3/2}.
\end{aligned}
\]

The restriction of the integral is valid because $t\ge5$ and the integrand is nonnegative. Its historical interval has length exactly 1. With $b=1/8$,

\[
R^Z_{p,n}(t)
\ge\sqrt{\frac5{8\sqrt2}}\,y^{3/4}
\ge\tfrac12y^{3/4},
\]

and the last inequality is equivalent, after squaring positive quantities, to $5\ge2\sqrt2$. Since the baseline is constant for these times and $y\ge F(t-5)\ge0$,

\[
\partial_tZ=F'(t-5)
\le\tfrac12F(t-5)^{3/4}
\le\tfrac12y^{3/4}\le R^Z_{p,n}(t).
\]

This checks (13)--(15), including $t=5$, without assuming $C_0>1$ or an unsaturated cutoff.

## 5. Every remaining width, empty deletions, and integration

For $1\le n<64$, a nonempty deletion satisfies

\[
h(p)\ge p\ge1/n>1/64.
\]

The required numerical comparison is exact:

\[
2d=\frac2{64^4}\le\frac1{64}
\quad\Longleftrightarrow\quad 2\le64^3.
\]

Thus, for every such width and $t\ge5$,

\[
\partial_tZ=F'(t-5)\le2d\le1/64\le h(p).
\]

This establishes (16), whether or not $A(Z)$ lies below $1/n$. In particular $n=1,p=1$ is covered directly. All nonempty below-floor cutoff cases at $t\ge5$ must have $n<64$, by the large-width calculation. Earlier times did not require the interpolation estimate at all.

For $p<1/n$, $Z=\partial_tZ=0$, $A(Z)=0$, and $J_n^Z(0,u)=\Phi(Z_{0,n}(u))=0$. Therefore $R^Z=0$, and (2) reduces to $0\le h(p)$. This includes $p=0$.

Combining the time and width cases proves (2) everywhere. Its right-hand side is continuous in time for each $p,n$. To see the only potentially delicate part, finite piecewise-linear interpolation is jointly continuous in $(a,u)$: neighboring cells agree at every grid node and at the separately defined endpoint $a=1$. Composing with the continuous cutoff and integrating a jointly continuous function over a continuously varying finite interval preserves continuity. Multiplication by $Z(t)t\ge0$ and the square root preserve continuity as well. All quantities are finite: writing $M=b+d$, one has $0\le J\le\Phi(M)$ and $R(t)\le t\sqrt{M\Phi(M)}$.

The fundamental theorem of calculus therefore applies to each $C^1$ path. Integration from the zero initial value proves (19) with $C=1$, exactly as claimed, without any width-dependent remainder.

## 6. Time rescaling for all prescribed constants

Fix any real $C>0$ and choose $0<\lambda\le\min\{1,C\}$. Such a choice always exists. The family constructed above works for every $C_0\ge1$; no upper bound or strict lower margin on $C_0$ was used.

For $Y_{p,n}(t)=Z_{p,n}(\lambda t)$, the interpolation weights depend only on $a,n$, so $J_n^Y(a,u)=J_n^Z(a,\lambda u)$, including $a=1$. Setting $\tau=\lambda t$ gives the squared radical identity directly:

\[
\begin{aligned}
(R^Y_{p,n}(t))^2
&=Z_{p,n}(\tau)\frac{\tau}{\lambda}
  \frac1\lambda\int_0^\tau
  J_n^Z(A(Z_{p,n}(\tau)),v)\,dv\\
&=\lambda^{-2}(R^Z_{p,n}(\tau))^2.
\end{aligned}
\]

Both radicals are nonnegative and $\lambda>0$, proving the exact identity (18), also when either side is zero. In particular, the outer time factor and the inner time integration each contribute a factor $\lambda^{-1}$ before taking the square root.

The chain rule and (2) now yield

\[
\partial_tY
\le\lambda h(p)+\lambda\Phi(Y)+\lambda^2R^Y.
\]

Because $\lambda\le C$, $\lambda^2\le\lambda\le C$, and all three terms are nonnegative, this is at most $C[h(p)+\Phi(Y)+R^Y]$. Integration gives exactly (19). The initial derivative is $\partial_tY(0)=\lambda\partial_tZ(0)=0$. The time change preserves the floors, both monotonicities, regularity, and the uniform bound. Thus the claim includes arbitrarily small positive $C$, arbitrarily large $C$, $C_0=1$, and every larger finite $C_0$.

## 7. Uniform deletion continuity, positive distances, and every limit

Set $T_*=5/\lambda>0$. For $0\le t\le T_*$, the added term is zero. If the deletion is nonempty, $0<r\le p\le1$ and $\alpha(\lambda t)\ge1/2$, so

\[
0\le Y_{p,n}(t)
=bS(\lambda t)r^{\alpha(\lambda t)}
\le b\sqrt r\le b\sqrt p.
\]

Empty deletions are zero. Taking all three suprema in (20) gives its stated bound, including $\varepsilon=0$, and sending $\varepsilon\downarrow0$ establishes uniform continuity over all widths, all smaller deletion sizes, and the whole closed initial time interval.

For each fixed nonempty $p,n$ and each $t>0$, $r>0$ and $S(\lambda t)>0$. Indeed, for $0<v<1$, $S(v)=v^2(3-2v)>0$, and for $v\ge1$, $S(v)=1$. Hence $Y_{p,n}(t)>0$ even before the limiting onset. There is no assumption of a finite-size time interval on which these distances vanish.

For any fixed $p\in(0,1]$, the deletion is nonempty for all sufficiently large $n$, and

\[
0\le p-\lfloor np\rfloor/n<1/n.
\]

Continuity of the positive power therefore gives

\[
\lim_{n\to\infty}Y_{p,n}(t)
=bS(\lambda t)p^{\alpha(\lambda t)}+F(\lambda t-5).
\]

At each fixed time the exponent is at least $1/2>0$, so the first term tends to zero as $p\downarrow0$. This proves (21) with the displayed order of limits. For singleton deletions, $p=1/n$ is always in the nonempty branch, with $r=1/n$, so the formula in (22) is exact and its first term is bounded by $b/\sqrt n\to0$.

One can also check the uniform failure directly, beyond these two sequences. For every $\varepsilon\in(0,1]$ and fixed $t\ge0$, define

\[
U_\varepsilon(t)=\sup_{n\ge1}\sup_{0\le p\le\varepsilon}Y_{p,n}(t).
\]

The nonempty formula and $r\le p\le\varepsilon$ give an upper bound, and choosing $p=\varepsilon$ and sending $n\to\infty$ attains that bound as a supremum. Thus the exact identity is

\[
U_\varepsilon(t)
=bS(\lambda t)\varepsilon^{\alpha(\lambda t)}+F(\lambda t-5).
\]

In particular,

\[
0\le U_\varepsilon(t)-F(\lambda t-5)\le b\sqrt\varepsilon
\quad\text{for all }t\ge0.
\]

The uniform small-deletion modulus therefore converges to the same limiting profile, even uniformly in time. For $t>T_*$, its limit is $d\exp[-1/(\lambda t-5)]>0$. By time monotonicity, the corresponding supremum on any finite interval $[0,T]$ has limit $F(\lambda T-5)$, which vanishes for $T\le T_*$ and is positive for $T>T_*$.

The order-of-limits issue is handled correctly: at a fixed finite width, $p\downarrow0$ eventually enters the empty branch and gives zero. The candidate does not assert the opposite. Along any sequence of nonempty deletions with $p\to0$, the baseline is bounded by $b\sqrt p$, so the limit is the stated $F$. Allowing empty deletions would not give a positive limit along every joint sequence, and no such universal joint-limit claim is made.

Finally $t\mapsto F(\lambda t-5)$ is $C^\infty$; its derivative of order $j$ is $\lambda^j F^{(j)}(\lambda t-5)$. All these derivatives vanish at $T_*$, while the function is positive at every later time. For any prescribed finite length $L\ge0$, the allowed choice

\[
\lambda=\min\{1,C,5/(L+1)\}>0
\]

even gives $T_*\ge L+1>L$. Thus the initial interval can be made strictly longer than any prescribed finite interval without changing $C$ or $C_0$.

## Final verdict

**PASS.** Every displayed mathematical inequality, endpoint case, finite-width case, rescaling identity, and stated scalar quantifier is valid. The prepared history legitimately supplies the required radical lower bound at the exact current interpolation cutoff; the small-width forcing argument closes the remaining floor cases. The family is a counterexample to sufficiency of the stated scalar hierarchy for global uniform deletion continuity. No network conclusion follows or is claimed. No fixes are required.
