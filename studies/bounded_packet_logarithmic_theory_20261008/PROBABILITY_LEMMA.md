# Probability ingredient: a bounded observable on a random sphere

This is a self-contained probability lemma derived from the supervisor's
assignment. It makes no assertion about a dynamical trajectory. Its scientific
inputs are only the random variables and observable defined below.

## Statement

Let \(G,V_1,V_2,\ldots\) be standard real Gaussian random variables, with the
\(V_i\) independent. Define

\[
f(x)=\tanh^2x,\qquad
a=\mathbb E f(G)\in(0,1),\qquad
K_n=\frac1n\sum_{i=1}^n f(V_i).
\]

For an integer \(q\ge2\), let \(U=(U_1,\ldots,U_q)\) be uniform on the unit
sphere \(S^{q-1}\subset\mathbb R^q\), independently of \(K_n\). For a scalar
\(k>0\), write

\[
S_q(k)=\frac1q\sum_{i=1}^q f(\sqrt{qk}\,U_i),\qquad
m(a)=\mathbb E f(\sqrt a\,G),
\]

and define the deterministic coefficient

\[
d(a)=\mathbb E\!\left[
 \sqrt a\,G\tanh(\sqrt a\,G)\operatorname{sech}^2(\sqrt a\,G)
\right]>0.
\]

For every sequence of integers \(q=q(n)\) such that \(q\to\infty\) and
\(q/n\to0\),

\[
\sqrt q\bigl(S_q(K_n)-m(a)\bigr)
\ \Longrightarrow\ \mathcal N(0,\sigma_a^2),
\]

where the exact limiting variance is

\[
\begin{aligned}
\sigma_a^2
&=\mathbb E\!\left[
 \bigl(f(\sqrt a\,G)-m(a)-d(a)(G^2-1)\bigr)^2
\right]\\
&=\operatorname{Var}\bigl(f(\sqrt a\,G)\bigr)-2d(a)^2
>0.
\end{aligned}
\]

Equivalently, if \(m(k)=\mathbb E f(\sqrt k\,G)\) for \(k>0\), then
\(d(a)=a m'(a)\). The displayed variance is therefore also
\(\operatorname{Var}(\tanh^2(\sqrt aG))-2a^2m'(a)^2\).

For each fixed integer \(q\ge2\) and each \(k>0\), \(S_q(k)\) is nonconstant
and has no atoms. Consequently, for fixed \(q\ge2\),
\(S_q(K_n)\Longrightarrow S_q(a)\), and the limiting law is nonatomic.

## Proof of the Gaussian limit

We first replace \(K_n\) by \(a\), which costs less than the fluctuation scale
under \(q/n\to0\). We then represent a uniform sphere point by normalized
independent Gaussians. A Taylor expansion of that normalization identifies the
single independent summand to which the usual real-valued central limit theorem
applies.

### Bounds and replacement of the random radius

The strict inequality \(0<a<1\) holds because
\(0<\tanh^2G<1\) almost surely. Since \(0\le f\le1\), independence gives

\[
\mathbb E(K_n-a)^2=\frac{\operatorname{Var}(f(G))}{n},
\qquad K_n-a=O_{\mathbb P}(n^{-1/2}).
\]

Here \(X_n=O_{\mathbb P}(r_n)\) means that \(X_n/r_n\) is bounded in
probability, and \(X_n=o_{\mathbb P}(r_n)\) means that this ratio converges to
zero in probability.

Differentiation gives

\[
f'(x)=2\tanh x\operatorname{sech}^2x,\qquad
f''(x)=2\operatorname{sech}^2x\bigl(1-3\tanh^2x\bigr).
\]

The exponential decay of \(\operatorname{sech}^2x\) at both ends of the real
line implies that the constants

\[
M_1=\sup_{x\in\mathbb R}|xf'(x)|,\qquad
M_2=\sup_{x\in\mathbb R}|x^2f''(x)|
\]

are finite. For any fixed sphere point \(U\), any coordinate, and \(k>0\),

\[
\left|\frac{d}{dk}f(\sqrt{qk}\,U_i)\right|
=\left|\frac{zf'(z)}{2k}\right|
\le\frac{M_1}{2k},\qquad z=\sqrt{qk}\,U_i.
\]

On the event \(|K_n-a|\le a/2\), the mean-value theorem therefore gives the
dimension-independent bound

\[
|S_q(K_n)-S_q(a)|\le\frac{M_1}{a}|K_n-a|.
\]

The complementary event has probability tending to zero by the preceding
variance bound. Hence

\[
\sqrt q\bigl(S_q(K_n)-S_q(a)\bigr)
=O_{\mathbb P}(\sqrt{q/n})=o_{\mathbb P}(1).
\tag{1}
\]

This replacement itself does not require independence between the radius and
the sphere point.

### Expansion of Gaussian normalization

Let \(X_1,X_2,\ldots\) be independent standard Gaussians, independent of the
\(V_i\), and put

\[
R_q=\frac1q\sum_{i=1}^qX_i^2.
\]

We can represent the uniform sphere point in distribution as
\(U_i=X_i/\sqrt{qR_q}\). Indeed, in polar coordinates the Gaussian density
times volume element is a constant times
\(e^{-r^2/2}r^{q-1}\,dr\,d\omega\), where \(d\omega\) is surface measure;
the angle is consequently uniform and independent of the radial coordinate.
It suffices to prove the desired distributional assertion in this
representation, in which

\[
S_q(a)=\frac1q\sum_{i=1}^q f(\sqrt{a/R_q}\,X_i).
\]

The Gaussian moments \(\mathbb EX_i^2=1\) and
\(\operatorname{Var}(X_i^2)=2\) give

\[
R_q-1=O_{\mathbb P}(q^{-1/2}),\qquad
\mathbb P(1/2\le R_q\le3/2)\longrightarrow1.
\]

For fixed real \(x\), set \(F(r,x)=f(\sqrt{a/r}\,x)\) for \(r>0\). With
\(z=\sqrt{a/r}\,x\), direct differentiation yields

\[
\partial_rF(r,x)=-\frac{zf'(z)}{2r},\qquad
\partial_r^2F(r,x)=\frac{3zf'(z)+z^2f''(z)}{4r^2}.
\]

For \(1/2\le r\le3/2\), the second derivative has absolute value at most
\(3M_1+M_2\), uniformly over all \(x\). Define the bounded real function

\[
b_a(x)=\sqrt a\,x\tanh(\sqrt a\,x)
                    \operatorname{sech}^2(\sqrt a\,x),
\]

so that \(\partial_rF(1,x)=-b_a(x)\) and
\(\mathbb E b_a(G)=d(a)\). Taylor's theorem, followed by averaging over the
coordinates, gives on \(1/2\le R_q\le3/2\)

\[
S_q(a)=\frac1q\sum_{i=1}^qf(\sqrt a\,X_i)
 -(R_q-1)\frac1q\sum_{i=1}^qb_a(X_i)+\mathcal R_q,
\]

with

\[
|\mathcal R_q|\le\tfrac12(3M_1+M_2)(R_q-1)^2.
\]

The sample mean of \(b_a(X_i)\) converges in probability to \(d(a)\), since
it has variance \(\operatorname{Var}(b_a(G))/q\to0\). Moreover,
\(\sqrt q(R_q-1)^2=o_{\mathbb P}(1)\). Multiplying the expansion by
\(\sqrt q\) and using
\(\sqrt q(R_q-1)=q^{-1/2}\sum_i(X_i^2-1)\), we obtain

\[
\sqrt q\bigl(S_q(a)-m(a)\bigr)
=\frac1{\sqrt q}\sum_{i=1}^q
 \left[f(\sqrt a\,X_i)-m(a)-d(a)(X_i^2-1)\right]
 +o_{\mathbb P}(1).
\tag{2}
\]

All remainder statements hold without conditioning: the event used for the
uniform Taylor estimate has probability tending to one. The replacement of
the sample mean of \(b_a\) costs
\(O_{\mathbb P}(1)o_{\mathbb P}(1)=o_{\mathbb P}(1)\).

For independent, identically distributed, real random variables with mean zero
and finite variance \(v\), the scalar central limit theorem states that their
sum divided by the square root of the number of summands converges in
distribution to \(\mathcal N(0,v)\). The summands in (2) are independent and
identically distributed, have mean zero by their displayed definition, and
have finite second moment because \(f\) is bounded and the Gaussian fourth
moment is finite. The theorem therefore applies with \(v=\sigma_a^2\).
Adding a term that converges to zero in probability preserves a distributional
limit. Combining (1) and (2) proves the asserted convergence.

### Variance identity and nondegeneracy

For \(F(x)=f(\sqrt a\,x)\) and the standard Gaussian density
\(\varphi(x)=(2\pi)^{-1/2}e^{-x^2/2}\), integration by parts gives

\[
\begin{aligned}
\mathbb E[(G^2-1)f(\sqrt a\,G)]
&=-\int_{\mathbb R}F(x)(x\varphi(x))'\,dx\\
&=\int_{\mathbb R}xF'(x)\varphi(x)\,dx
=2d(a).
\end{aligned}
\]

The boundary term vanishes because \(F\) is bounded and
\(x\varphi(x)\to0\); the derivative integrand is integrable because
\(xF'(x)\) is bounded by \(M_1\). Since
\(\mathbb E(G^2-1)^2=2\), expanding the square in the definition of
\(\sigma_a^2\) yields

\[
\sigma_a^2=\operatorname{Var}(f(\sqrt a\,G))
 -2d(a)\,[2d(a)]+2d(a)^2
=\operatorname{Var}(f(\sqrt a\,G))-2d(a)^2.
\]

Also \(d(a)>0\): its integrand is strictly positive whenever \(G\ne0\),
because \(z\tanh z>0\) for nonzero real \(z\), and
\(\operatorname{sech}^2z>0\).

If \(\sigma_a^2=0\), the centered summand in (2) must be zero almost surely.
The Gaussian density is positive on every real interval and that summand is
a continuous function of its argument, so this would imply the identity

\[
f(\sqrt a\,x)-m(a)=d(a)(x^2-1)\qquad\text{for every }x\in\mathbb R.
\]

The left side is bounded, whereas the right side tends to positive infinity
as \(|x|\to\infty\), since \(d(a)>0\). This contradiction proves
\(\sigma_a^2>0\).

Finally, differentiation of \(m(k)=\mathbb E f(\sqrt k\,G)\) is permitted
on any compact subinterval of \((0,\infty)\): the derivative of the integrand
has absolute value at most \(M_1/(2k)\), an integrable bound uniform on such
an interval. Thus

\[
m'(a)=\mathbb E\!\left[
\frac{G}{\sqrt a}\tanh(\sqrt a\,G)
                       \operatorname{sech}^2(\sqrt a\,G)
\right]=\frac{d(a)}a.
\]

## Fixed dimensions: nonconstancy and absence of atoms

Fix \(q\ge2\) and \(k>0\), and define

\[
h(t)=\tanh^2(\sqrt{qkt}),\qquad t\ge0.
\]

For \(t>0\), writing \(z=\sqrt{qkt}\),

\[
h'(t)=qk\,\frac{\tanh z}{z}\operatorname{sech}^2z,
\qquad h'(0)=qk.
\]

The positive function \(\tanh z/z\) is strictly decreasing for \(z>0\).
Indeed,

\[
\frac{d}{dz}\frac{\tanh z}{z}
=\frac{z\operatorname{sech}^2z-\tanh z}{z^2}<0,
\]

because \(p(z)=\tanh z-z\operatorname{sech}^2z\) satisfies \(p(0)=0\) and
\(p'(z)=2z\operatorname{sech}^2z\tanh z>0\). The other positive factor
\(\operatorname{sech}^2z\) is also strictly decreasing. Consequently
\(h'\) is strictly decreasing, including its continuous extension at zero,
and \(h\) is strictly concave on \([0,\infty)\).

At the sphere point \((1,0,\ldots,0)\), the observable is
\(q^{-1}\tanh^2(\sqrt{qk})\); at
\(q^{-1/2}(1,\ldots,1)\), it is \(\tanh^2(\sqrt k)\). These values differ
strictly because \(h(0)=0\) and strict concavity gives
\(h(1/q)>h(1)/q\). Thus \(S_q(k)\) is nonconstant. In fact, concavity gives
the deterministic bounds

\[
\frac1q\tanh^2(\sqrt{qk})
\ \le\ S_q(k)\ \le\ \tanh^2(\sqrt k).
\]

For the lower bound use \(h(t)\ge t h(1)\) for \(0\le t\le1\), then sum
over \(t=U_i^2\); for the upper bound use Jensen's inequality with
\(q^{-1}\sum_iU_i^2=1/q\).

To prove that the distribution has no atoms, use the Gaussian sphere
representation once more and write the first two Gaussian coordinates as

\[
(X_1,X_2)=\rho(\cos\Theta,\sin\Theta).
\]

The planar Gaussian density in polar coordinates shows that
\(\Theta\) is uniform on \([0,2\pi)\), independent of \(\rho\) and of
\(X_3,\ldots,X_q\). Also \(\rho>0\) almost surely. Condition on
\(\rho,X_3,\ldots,X_q\), and define

\[
s=\frac{\rho^2}{\rho^2+\sum_{j=3}^qX_j^2}\in(0,1].
\]

The terms with indices \(3,\ldots,q\) are now fixed, whereas the first two
terms in \(qS_q(k)\) are

\[
h(s\cos^2\Theta)+h(s\sin^2\Theta).
\]

For \(v\in[0,1]\), set \(H_s(v)=h(sv)+h(s(1-v))\). Its derivative obeys

\[
H_s'(v)=s\bigl[h'(sv)-h'(s(1-v))\bigr]
\begin{cases}
>0,&0<v<1/2,\\
<0,&1/2<v<1.
\end{cases}
\]

These strict signs follow from the strict decrease of \(h'\) and \(s>0\).
Every level set of \(H_s\) therefore contains at most two points. Each fixed
value of \(\cos^2\Theta\) has only finitely many preimages in
\([0,2\pi)\), a set of zero probability under the uniform angle. Conditional
on the stated variables, every level set of \(S_q(k)\) consequently has
probability zero. Averaging the conditional probabilities proves

\[
\mathbb P(S_q(k)=c)=0\qquad\text{for every real }c.
\]

This proof also covers \(q=2\), when the sum defining \(s\) is empty and
\(s=1\). For \(q=1\), by contrast, \(S_1(k)=\tanh^2(\sqrt k)\) is
deterministic; the restriction \(q\ge2\) is essential for this claim.

## Consequences for bounded dimension sequences

For fixed \(q\ge2\), couple all \(S_q(K_n)\) to one uniform sphere point
independent of the \(V_i\). The radius replacement bound above, without the
factor \(\sqrt q\), gives
\(S_q(K_n)-S_q(a)\to0\) in probability, and hence convergence in
distribution to the nonatomic law of \(S_q(a)\).

In fact, if \(\delta_n\downarrow0\), then

\[
\sup_{c\in\mathbb R}
\mathbb P\bigl(|S_q(K_n)-c|\le\delta_n\bigr)\longrightarrow0.
\tag{3}
\]

Here is a direct justification of the uniformity in \(c\). For a nonatomic
random variable \(Y\) taking values in \([0,1]\), define
\(Q_Y(r)=\sup_c\mathbb P(|Y-c|\le r)\). Then \(Q_Y(r)\to0\) as
\(r\downarrow0\). Otherwise one can choose radii tending to zero and
centers with interval probabilities bounded below by a positive constant.
The centers can be confined to a fixed compact interval because \(Y\in[0,1]\).
A convergent subsequence of centers, with limit \(c\), would imply
\(\mathbb P(|Y-c|\le\varepsilon)\) is bounded below by the same positive
constant for every \(\varepsilon>0\). Continuity of probability under
decreasing sets would then give \(\mathbb P(Y=c)>0\), a contradiction.

Apply this with \(Y=S_q(a)\). For every \(\varepsilon>0\),

\[
\begin{aligned}
\sup_c\mathbb P(|S_q(K_n)-c|\le\delta_n)
&\le Q_{S_q(a)}(\delta_n+\varepsilon)\\
&\quad+\mathbb P(|S_q(K_n)-S_q(a)|>\varepsilon).
\end{aligned}
\]

For all sufficiently large \(n\), the first term is at most
\(Q_{S_q(a)}(2\varepsilon)\), and the second tends to zero. Letting
\(\varepsilon\downarrow0\) proves (3). The same conclusion holds if
\(q=q(n)\) takes values in any fixed finite set \(\{2,\ldots,Q\}\): take
the maximum of the finitely many limiting concentration functions and use
the radius replacement bound, whose constant does not depend on \(q\).

For completeness, \(S_q(K_n)\) itself is nonatomic for every fixed
\(n\ge1\) and \(q\ge2\). Indeed, \(K_n>0\) almost surely, it is independent
of \(U\), and conditioning on any positive value of \(K_n\) reduces to the
fixed-radius argument above.

No numerical evidence or unproved dynamical assertion is used. The Gaussian
limit requires \(q\to\infty\) and \(q/n\to0\); the separate fixed-dimension
statements require \(q\ge2\), \(a>0\), and \(n\to\infty\) where a limiting
statement is made. No mathematical gap remains within these probability
claims.
