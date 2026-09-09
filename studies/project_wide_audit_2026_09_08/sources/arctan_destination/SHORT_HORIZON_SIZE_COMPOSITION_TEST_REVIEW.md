# Standalone adversarial proof-only audit

## Verdict and audited object

**PASS. Required mathematical corrections: none.**

Candidate:

    /tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/SHORT_HORIZON_SIZE_COMPOSITION_TEST.md

Candidate SHA-256, verified before the audit:

    4e21a57d5f567773ce8cc293e8e2b992c0c563d87eb908405531abc18291dd4d

The candidate has 406 lines. This report audits its displayed scalar hierarchy and every mathematical assertion used to establish its result, for arbitrary real \(T,C>0\), \(C_0\ge1\), \(0\le L<T\), all integers \(n\ge1\), all \(p\in[0,1]\), and all \(t\in[0,T]\).

The requested skill at /etc/codex/skills/solve-math-rigorously/SKILL.md was read in full by the auditor. The only mathematical source read was the candidate itself. No prior proof, review, ledger, or conversation was consulted; no experiment, numerical test, literature search, or delegated audit was used. The candidate's nonmathematical provenance statements about an earlier file were neither used nor independently checked. The candidate was not edited.

The conclusion is exclusively that the displayed scalar inequalities do not force uniform continuity at zero deletion size throughout the prescribed horizon. It is not a network counterexample or a conclusion about realizability by any network dynamics.

The proof below independently reconstructs the result: first validate all parameters and time paths, then verify the forcing and Osgood phases, then derive the radical estimate using the exact finite-grid interpolant on its legitimate domain, and finally check every width and the asserted limits.

## 1. Precise scalar target and construction

Define
\[
h(p)=p\log(e/p)\quad(0<p\le1),\qquad h(0)=0,
\]
\[
\Phi(x)=x\left[1+\tfrac12\log_+(1/x)\right]\quad(x>0),
\qquad \Phi(0)=0,\qquad A(y)=\min\{1,C_0y\}.
\]
Here \(\log_+z=\max\{0,\log z\}\). For \(0\le m<1\), let
\[
k=\lfloor nm\rfloor,\qquad \theta=nm-k,
\]
\[
J_n(m,u)=(1-\theta)\Phi(Y_{k/n,n}(u))
             +\theta\Phi(Y_{(k+1)/n,n}(u)),
\qquad J_n(1,u)=\Phi(Y_{1,n}(u)).
\]
The radical uses the current cutoff at every historical time:
\[
R_{p,n}(t)=
\left[Y_{p,n}(t)t\int_0^t J_n(A(Y_{p,n}(t)),u)\,du\right]^{1/2}.
\]
The target is exactly
\[
Y_{p,n}(t)\le C\left[
t h(p)+\int_0^t\Phi(Y_{p,n}(s))\,ds
+\int_0^t R_{p,n}(s)\,ds
\right].
\tag{H}
\]
No width error occurs in this inequality. No unspecified earlier hierarchy is needed.

Use the candidate's parameters:
\[
a=\frac{L+T}{6},\qquad
\tau=3a=\frac{L+T}{2},\qquad
t_0=\frac{L+3T}{4},
\]
\[
S(v)=
\begin{cases}
0,&v\le0,\\
3v^2-2v^3,&0<v<1,\\
1,&v\ge1,
\end{cases}
\]
\[
\varepsilon=\min\{\tfrac12,Ca/12\},\qquad
\alpha(t)=1-\varepsilon S((t-a)/a),\qquad
\alpha_*=1-\varepsilon,
\]
\[
\gamma=\frac{1+\alpha_*}{2},\qquad
\delta=1-\gamma=\frac{\varepsilon}{2},\qquad
b=\min\{\tfrac18,Ca/6\},
\]
\[
N=\left\lceil b^{-1/\varepsilon}\right\rceil,\qquad
K=a\sqrt{3b/2},
\]
\[
d=\min\left\{
\tfrac18,\frac{C}{4N},
\left(\frac{CK\delta^2}{4}\right)^{1/\delta}
\right\},\qquad
F(s)=
\begin{cases}
d e^{-1/s},&s>0,\\
0,&s\le0.
\end{cases}
\]
For \(p\ge1/n\), set \(r=\lfloor np\rfloor/n\) and
\[
Y_{p,n}(t)=bS(t/a)r^{\alpha(t)}+F(t-\tau).
\tag{Y}
\]
For \(p<1/n\), set \(Y_{p,n}(t)=0\). In particular, the added term is not assigned to empty deletions.

## 2. Parameter validity and prescribed horizon

Because \(0\le L<T\) and \(T>0\),
\[
0<a<2a<3a=\tau<T,\qquad
\tau-L=\frac{T-L}{2}>0,
\]
\[
t_0-\tau=T-t_0=\frac{T-L}{4}>0.
\]
Thus both preparation phases, the entire historical interval \([2a,3a]\), and the witness \(t_0\) fit within the original interval \([0,T]\). This includes \(L=0\) and every \(L\) arbitrarily close to \(T\).

Every minimum defining \(\varepsilon\) and \(b\) has positive finite entries. Consequently,
\[
0<\varepsilon\le\tfrac12,\qquad
\tfrac12\le\alpha_*\le\alpha(t)\le1,\qquad \alpha_*<1,
\]
\[
0<\delta\le\tfrac14,\qquad
\tfrac34\le\gamma<1,\qquad 0<b\le\tfrac18.
\]
In exact real arithmetic,
\[
b^{-1/\varepsilon}
=\exp\!\left(\frac{\log(1/b)}{\varepsilon}\right)
\]
is finite and positive for each fixed allowed choice of parameters. Its ceiling is therefore a finite integer. Moreover,
\[
b^{-1/\varepsilon}\ge8^2=64,\qquad N\ge64.
\]
The quantity \(K\) is positive and finite. Since \(\delta>0\), the third entry in the minimum for \(d\) is also positive and finite:
\[
\left(\frac{CK\delta^2}{4}\right)^{1/\delta}
=\exp\!\left(\frac{\log(CK\delta^2/4)}{\delta}\right)>0.
\]
It follows that \(0<d\le1/8\).

No uniform positive lower bound is imposed on \(Ca\), \(\varepsilon\), \(\delta\), or \(d\), and no uniform finite upper bound is imposed on \(N\). Their possible extreme sizes introduce no limiting assumption. In particular, one must not replace the specified positive real \(d\) by numerical zero or approximate the ceiling in the definition of \(N\).

The following exact budget inequalities hold simultaneously:
\[
b\le Ca/6,\qquad \varepsilon\le Ca/12,\qquad
d\le\frac{C}{4N},\qquad d^\delta\le\frac{CK\delta^2}{4}.
\tag{B}
\]
They use the original prescribed \(C\); no replacement constant or enlarged time horizon is involved.

## 3. Definition, regularity, monotonicity, and initial conditions

For any nonempty deletion, \(1/n\le r\le p\le1\), so every power in (Y) is well defined and positive. At \(p=1\), \(r=1\). For \(n=1\), the only nonempty size is \(p=1\); all \(p<1\) receive the explicitly zero path. The definition therefore covers every width and both size endpoints.

At fixed \(n,t\), increasing \(p\) increases its floor \(r\). Since \(\alpha(t)>0\), \(r^{\alpha(t)}\) is increasing in \(r\). The jump from empty to nonempty deletion is nonnegative. Thus the family is nonnegative, nondecreasing in \(p\), and constant on each interval \([k/n,(k+1)/n)\), with \(p=1\) defined separately. Since \(0\le S\le1\), \(r^{\alpha(t)}\le1\), and \(0\le F\le d\),
\[
0\le Y_{p,n}(t)\le b+d\le\tfrac14<1
\tag{U}
\]
uniformly in all three indices.

On \((0,1)\), \(S'(v)=6v(1-v)\), so
\[
0\le S'\le\tfrac32,\qquad S'(0)=S'(1)=0.
\]
The constant pieces match in value and first derivative. Hence \(S\) is \(C^1\) and nondecreasing. The function \(\alpha\) is \(C^1\), nonincreasing, equal to \(1\) through time \(a\), and equal to \(\alpha_*\) from time \(2a\) onward.

For completeness, smoothness and flatness of \(F\) at zero do not require a regularity theorem. Each derivative for \(s>0\) is \(d e^{-1/s}\) times a polynomial in \(1/s\), by induction under differentiation. For every integer \(j\ge0\) and \(x>0\),
\[
0\le x^j e^{-x}\le\frac{(j+1)!}{x},
\]
using \(e^x\ge x^{j+1}/(j+1)!\). Thus all such polynomial terms tend to zero as \(s\downarrow0\). Their difference quotients at zero also tend to zero, because division by \(s\) only increases the polynomial degree. Inductively the zero extension is \(C^\infty\), with every derivative zero at zero.

For fixed nonempty \(r\), write \(r^{\alpha(t)}=\exp(\alpha(t)\log r)\). This is \(C^1\). Therefore every time path is \(C^1\), including at \(a\), \(2a\), and \(\tau\); the empty paths are identically zero. At time zero, \(S(0)=S'(0)=0\), \(\alpha=1\) on a neighborhood in the time domain, and \(F(t-\tau)=0\). Consequently,
\[
Y_{p,n}(0)=\partial_tY_{p,n}(0)=0
\]
for every \(p,n\), with the derivative at the endpoint understood one-sided, or by the same local extension.

Since \(r\le1\), decreasing \(\alpha\) increases \(r^\alpha\). The factors in the nonnegative product \(S(t/a)r^{\alpha(t)}\) are nondecreasing, as is \(F(t-\tau)\). Every time path is therefore nondecreasing. If \(p\ge1/n\) and \(t>0\), then \(S(t/a)>0\), \(b>0\), and \(r^{\alpha(t)}>0\). Hence \(Y_{p,n}(t)>0\) at every positive time in the prescribed domain, even before \(\tau\).

## 4. Flat-function estimates for every real argument

For \(s>0\), direct differentiation gives
\[
F'(s)=d s^{-2}e^{-1/s},\qquad
\frac{F'(s)}{F(s)^\gamma}
=d^\delta s^{-2}e^{-\delta/s}.
\]
The denominator is positive in this calculation. The elementary inequality
\[
e^z\ge z^2/2,\qquad z^2e^{-z}\le2\quad(z\ge0)
\]
gives, with \(z=1/s\) and \(z=\delta/s\), respectively,
\[
F'(s)\le2d,\qquad
F'(s)\le\frac{2d^\delta}{\delta^2}F(s)^\gamma.
\]
For \(s\le0\), both \(F'\) and \(F\) vanish, and these inequalities remain valid without division. Applying (B) yields the two simultaneous global estimates
\[
F'(s)\le\frac{C}{2N},\qquad
F'(s)\le\frac{CK}{2}F(s)^\gamma.
\tag{F}
\]
These bounds hold without an assumption on \(T-\tau\), and remain valid for arbitrarily small positive \(\delta\).

## 5. Forcing and Osgood preparation

We prove the stronger inequality
\[
\partial_tY_{p,n}(t)
\le C\,[h(p)+\Phi(Y_{p,n}(t))+R_{p,n}(t)].
\tag{D}
\]
All three terms on its right are nonnegative. For \(p\in[0,1]\),
\[
h(p)\ge p,
\]
by the definition at zero and \(\log(e/p)=1+\log(1/p)\ge1\) otherwise.

Fix a nonempty deletion. On \(0<t<a\), the exponent is \(1\) and \(F(t-\tau)=0\). Consequently,
\[
\partial_tY_{p,n}(t)
=\frac{b}{a}S'(t/a)r
\le\frac{3b}{2a}r
\le\frac C4 r
\le\frac C4 h(p).
\]
This verifies (D) using the forcing with the prescribed constant.

On \(a<t<2a\), \(S(t/a)=1\) and the added term is still zero. Put \(B=b r^{\alpha(t)}=Y_{p,n}(t)\). Then
\[
0\le-\alpha'(t)
=\frac{\varepsilon}{a}S'((t-a)/a)
\le\frac{3\varepsilon}{2a}\le\frac C8,
\]
\[
\partial_tY_{p,n}(t)
=(-\alpha'(t))B\log(1/r)
\le\frac C8 B\log(1/r).
\]
Here \(0<B\le b<1\), and
\[
\log(1/B)=\log(1/b)+\alpha(t)\log(1/r)
\ge\alpha_*\log(1/r).
\]
Therefore
\[
\Phi(B)\ge\tfrac12B\log(1/B)
\ge\tfrac{\alpha_*}{2}B\log(1/r)
\ge\tfrac14B\log(1/r).
\]
It follows that \(\partial_tY_{p,n}\le C\Phi(B)/2\). The case \(r=1\), where \(\log(1/r)=0\), is included: its exponent-change derivative is zero.

For \(2a\le t\le3a=\tau\),
\[
Y_{p,n}(t)=b r^{\alpha_*},\qquad \partial_tY_{p,n}(t)=0.
\tag{P}
\]
At \(a\), \(2a\), and \(\tau\), both adjacent expressions have the stated common derivative, which is zero at each join. At \(t=0\) the derivative is also zero. Thus (D) is valid through \(\tau\), including all phase endpoints. There is no overlapping derivative cost from the baseline and \(F\).

## 6. Exact finite-floor interpolation and radical estimate

First, \(\Phi(x)\ge x\) for all \(x\ge0\). For \(0<x<1\),
\[
\Phi'(x)=\tfrac12[1+\log(1/x)]>0,
\]
and for \(x>1\), \(\Phi'(x)=1\). Its values match continuously at \(1\), and continuity at \(0\) follows from \(x\log(1/x)\to0\). Thus \(\Phi\) is increasing on its entire domain; differentiability at \(1\) is not needed.

By (P) and the zero definition at empty size, every historical time \(u\in[2a,3a]\) satisfies
\[
Y_{k/n,n}(u)=b(k/n)^{\alpha_*},\qquad k=0,\ldots,n,
\]
where \(0^{\alpha_*}=0\). This includes \(u=3a\), because \(F(0)=0\).

Let \(1/n\le m<1\). Then \(k=\lfloor nm\rfloor\ge1\), \(0\le\theta<1\), and
\[
nm<k+1\le2k,\qquad k/n\ge m/2.
\]
The two grid values are ordered. The exact convex interpolation therefore obeys
\[
\begin{aligned}
J_n(m,u)
&\ge\Phi(Y_{k/n,n}(u))
\ge b(k/n)^{\alpha_*}\\
&\ge b\,2^{-\alpha_*}m^{\alpha_*}
\ge\frac b2m^{\alpha_*}.
\end{aligned}
\tag{I}
\]
At \(m=1\), the separately defined endpoint gives \(J_n(1,u)=\Phi(b)\ge b\), also implying (I). For \(n\ge2\), at \(m=1/n\), \(k=1\) and \(\theta=0\), so there is no endpoint loss. For \(n=1\), the interval \([1/n,1]\) consists solely of \(m=1\), already checked. All interior grid joins use precisely the stated floor and weights.

The restriction \(m\ge1/n\) is essential and is respected. Below the first grid point, the exact formula is instead
\[
J_n(m,u)=nm\,\Phi(bn^{-\alpha_*}),\qquad 0\le m<1/n.
\]
For fixed \(n\), its ratio to \(m^{\alpha_*}\) tends to zero as \(m\downarrow0\), since \(1-\alpha_*=\varepsilon>0\). Thus extending (I) to all positive \(m\) would be false. The candidate makes no such extension.

Now suppose \(n\ge N\), \(p\ge1/n\), and \(\tau\le t\le T\). Put \(y=Y_{p,n}(t)\). The exact ceiling gives
\[
y\ge b r^{\alpha_*}\ge b n^{-\alpha_*}
=\frac{b n^\varepsilon}{n}\ge\frac1n,
\]
because \(n\ge N\ge b^{-1/\varepsilon}\). By (U), \(y<1\). Since \(C_0\ge1\), both \(1\) and \(C_0y\) are at least \(y\), and hence
\[
1\ge A(y)\ge y\ge1/n.
\]
This is the precise condition needed to apply (I) at the current cutoff, for every \(u\in[2a,3a]\).

The integrand is nonnegative; the historical interval has length \(a\) and is contained in \([0,t]\); and \(t\ge3a\). It follows that
\[
\begin{aligned}
R_{p,n}(t)^2
&=yt\int_0^t J_n(A(y),u)\,du\\
&\ge yt\int_{2a}^{3a}\frac b2 A(y)^{\alpha_*}\,du\\
&=\frac{ab}{2}yt A(y)^{\alpha_*}\\
&\ge\frac{3a^2b}{2}y^{1+\alpha_*}
=K^2y^{2\gamma}.
\end{aligned}
\]
Taking nonnegative square roots yields
\[
R_{p,n}(t)\ge K Y_{p,n}(t)^\gamma.
\tag{R}
\]
The estimate includes \(n=N\), equality at \(y=1/n\), \(t=\tau\), and saturated cutoffs \(A(y)=1\). It uses \(A(y(t))\) as specified in the hierarchy, not a historical or continuously approximated cutoff.

## 7. Every width after the onset

For a nonempty deletion and \(t\ge\tau\), the baseline is stationary, so \(\partial_tY_{p,n}(t)=F'(t-\tau)\).

If \(n\ge N\), apply (F), \(Y_{p,n}(t)\ge F(t-\tau)\), \(\gamma>0\), and (R):
\[
\partial_tY_{p,n}(t)
\le\frac{CK}{2}F(t-\tau)^\gamma
\le\frac{CK}{2}Y_{p,n}(t)^\gamma
\le\frac C2 R_{p,n}(t).
\]

If \(1\le n<N\), a nonempty deletion satisfies
\[
h(p)\ge p\ge1/n>1/N.
\]
The other bound in (F) then gives
\[
\partial_tY_{p,n}(t)
\le\frac{C}{2N}\le\frac C2 h(p).
\]
This includes \(n=1\) and every remaining integer width, whether its cutoff is below, at, or above the first grid point. No interpolation bound is used for these widths.

These two cases exhaust all nonempty deletions after \(\tau\). For every empty deletion \(p<1/n\), including \(p=0\), the path and derivative are zero for all time. Here \(A(0)=0\) and \(J_n(0,u)=0\), so the radical itself is zero as well. Thus (D) also holds for empty deletions.

At the initial time the radical is zero because its integral is over an interval of length zero. At the final time \(T\), the same derivative bounds hold with the endpoint derivative. Together with the preparation check, (D) is established for all quantified \(p,n,t\).

## 8. Well-defined integrals and integration to the exact hierarchy

For fixed \(n\), each grid value \(\Phi(Y_{k/n,n}(u))\) is continuous in \(u\). On each closed size cell the interpolation is continuous jointly in \((m,u)\). At a grid join, the interpolation from either side equals the same grid value; the separately specified value at \(m=1\) also matches. Hence \(J_n\) is jointly continuous on \([0,1]\times[0,T]\).

The uniform bound (U) and monotonicity of \(\Phi\) give
\[
0\le J_n(m,u)\le M,\qquad M=\Phi(1/4)<\infty.
\]
For fixed \(p,n\), write \(m(t)=A(Y_{p,n}(t))\), a continuous function. Joint continuity on the compact rectangle implies uniform continuity. For \(t_j\to t\), splitting the integrals over their common interval gives
\[
\begin{aligned}
&\left|\int_0^{t_j}J_n(m(t_j),u)\,du-
\int_0^t J_n(m(t),u)\,du\right|\\
&\quad\le T\sup_{0\le u\le T}
|J_n(m(t_j),u)-J_n(m(t),u)|+M|t_j-t|\longrightarrow0.
\end{aligned}
\]
Consequently the expression under the square root defining \(R_{p,n}\) is continuous and nonnegative, and so is \(R_{p,n}\). It is also finite; for example,
\[
R_{p,n}(t)^2\le\tfrac14 M T^2.
\]
No differentiation of the radical at zero is needed.

Since \(Y_{p,n}\) is \(C^1\) and all terms of (D) are integrable, the fundamental theorem of calculus and \(Y_{p,n}(0)=0\) give (H) directly, with coefficient exactly \(C\). There is no multiplicative loss from combining phases, since (D) was proved pointwise in each phase.

## 9. Uniform initial deletion continuity and positive limits before \(T\)

For \(0\le t\le\tau\), \(F(t-\tau)=0\). If \(p\le\eta\) is nonempty, then \(r\le p\le\eta\le1\), and therefore
\[
Y_{p,n}(t)
\le b r^{\alpha(t)}
\le b r^{\alpha_*}
\le b\eta^{\alpha_*}.
\]
Empty sizes give zero. Thus, for every \(\eta\in[0,1]\),
\[
\sup_{n\ge1}\sup_{0\le p\le\eta}\sup_{0\le t\le\tau}
Y_{p,n}(t)\le b\eta^{\alpha_*}.
\]
At \(\eta=0\), both sides are zero. Since \(\alpha_*>0\), the right side tends to zero as \(\eta\downarrow0\). This is uniform continuity at zero deletion size, simultaneously in width and time through \(\tau\), and in particular through the prescribed \(L<\tau\). It does not assert continuity across the finite-width deletion jumps.

For each fixed \(p>0\), the deletion is nonempty for all sufficiently large \(n\), and
\[
0\le p-\frac{\lfloor np\rfloor}{n}<1/n.
\]
Continuity of the positive power at fixed \(t\) gives
\[
\lim_{n\to\infty}Y_{p,n}(t)
=bS(t/a)p^{\alpha(t)}+F(t-\tau).
\]
Because \(\alpha(t)\ge\alpha_*>0\), taking \(p\downarrow0\) gives exactly
\[
\lim_{p\downarrow0}\lim_{n\to\infty}Y_{p,n}(t)=F(t-\tau).
\]
There is no interchange of limits in this argument. Independently, singleton deletions obey the exact identity
\[
Y_{1/n,n}(t)
=bS(t/a)n^{-\alpha(t)}+F(t-\tau),
\]
and the first term is bounded by \(b n^{-\alpha_*}\). Thus their limit is also \(F(t-\tau)\), even uniformly in \(t\in[0,T]\).

At the specified \(t_0\),
\[
t_0-\tau=\frac{T-L}{4}>0,
\]
\[
\lim_{p\downarrow0}\lim_{n\to\infty}Y_{p,n}(t_0)
=\lim_{n\to\infty}Y_{1/n,n}(t_0)
=d\exp\!\left(-\frac4{T-L}\right)>0.
\]
Both factors in this product are strictly positive for each allowed fixed parameter choice. This witnesses failure strictly before \(T\), regardless of how small \(T\), \(C\), or \(T-L\) is.

It also directly disproves uniform deletion continuity at \(t_0\): for any \(\eta>0\), arbitrarily large \(n\) have \(1/n\le\eta\), and their singleton values approach the displayed positive number. Accordingly the supremum over widths and sizes at most \(\eta\) cannot tend to zero.

The small-deletion limiting time profile is precisely \(F(t-\tau)\). It is zero through \(\tau\), smooth and flat there, and strictly positive for every \(\tau<t\le T\). The statement that every fixed nonempty finite-width deletion is already positive for every \(t>0\) concerns the baseline and is compatible with the limiting profile being initially zero.

The limit order matters and is correctly respected in the candidate: for each fixed finite \(n\), the limit as \(p\downarrow0\) is zero because sizes below \(1/n\) are empty. No unrestricted positive joint limit over sequences that include empty deletions is asserted or needed. The stated iterated limit and singleton limit suffice.

## 10. Adversarial coverage and disposition

The potentially fatal cases are all resolved within the candidate's own formulas:

| Potential failure | Verified resolution |
|---|---|
| Arbitrarily short \(T\), small \(C\), or \(L\) close to \(T\) | All phases end by \(\tau<T\); \(t_0<T\); budget inequalities (B) use the prescribed \(C\). |
| Tiny exponent change or amplitude, huge ceiling | \(\varepsilon,\delta,d\) are strictly positive finite reals; \(N\) is the exact finite ceiling. |
| Circular creation of the historical profile | Forcing creates the profile on \((0,a)\); the Osgood term pays for its exponent change on \((a,2a)\); the radical is not required in either phase. |
| Invalid fractional interpolation bound below \(1/n\) | The lower bound is restricted to \([1/n,1]\); \(n\ge N\) guarantees its cutoff condition. |
| Missing small widths | The separate forcing estimate covers every \(1\le n<N\), including \(n=1\). |
| Equality at the width threshold or first grid point | All required comparisons are non-strict; \(n=N\) and \(m=1/n\) are included. |
| Saturation and \(C_0=1\) | \(A(y)\ge y\) holds for every \(C_0\ge1\) because \(y<1\); the endpoint \(m=1\) is checked separately. |
| Empty deletion, \(p=0\), or \(p=1\) | The exact definition handles each case; no logarithm of zero or negative power of zero is used. |
| Phase endpoints, \(t=0\), or \(t=T\) | The paths are \(C^1\); all endpoint derivative inequalities and radical values are valid. |
| Confusing onset with a positive witness | The limit is zero at \(\tau\); strict positivity is proved at \(t_0=\tau+(T-L)/4<T\). |
| Confusing scalar insufficiency with a network construction | The conclusion is restricted to the displayed scalar hierarchy. |

Every mathematical assertion needed for the full stated scalar result is valid under the displayed quantifiers. No correction, additional hypothesis, horizon extension, or change of constant is required.

This is the complete report. Its contents are to remain unchanged after the final report hash is computed.
