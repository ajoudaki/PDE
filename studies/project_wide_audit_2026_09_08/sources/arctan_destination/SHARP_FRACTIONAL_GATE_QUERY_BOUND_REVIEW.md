# Independent proof-only audit of SHARP_FRACTIONAL_GATE_QUERY_BOUND.md

**Verdict: PASS for the full stated result conditional on the explicit common event and the three established input estimates. Required fixes: none.**

This verdict includes the fractional query estimate (5), the actual uncompressed gate estimate (8), its replacement of the actual weight mass by the state-distance bound, and the finite comparison hierarchy (10). It does not assert that the hierarchy closes continuation, forces deletion continuity, removes clipping, or transfers to a positive initial readout.

## Audited files and exact hashes

Candidate, read in full (lines 1–233):

`/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/SHARP_FRACTIONAL_GATE_QUERY_BOUND.md`

SHA-256:

`8e45e97946b2e7c9b6f06c4e1e99fb18e41d9a5fdc7883c858c872941374c1bc`

Sole mathematical dependency, read in full (lines 1–319):

`/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_WEIGHTED_GATE_HARDY_BOUND.md`

SHA-256:

`73b5f44b4fc6796ab08078e2d845d20fc51378107a48bc0233ef81d08359ce41`

Both computed hashes match the requested hashes. The candidate was not edited. This audit uses no experiments, other reviews or ledgers, source agents, conversation history, or external sources. The requested `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read in full.

## 1. Precise scope, state identification, and allowed inputs

Fix a positive integer width \(n\), a finite horizon \(S\), the prescribed primal-event parameters, and one prescribed common clipping map \(\tau:\mathbb R\to\mathbb R\) satisfying

\[
|\tau(x)|\le |x|,
\qquad |\tau(x)-\tau(y)|\le |x-y|.
\]

The identity map is allowed. Fix a realization in the dependency's stated common event, including its operator-bound event. All arguments below are deterministic on this realization. Constants can depend on the fixed horizon and primal-event parameters, but not on \(n\), the deletion set, the subsequently selected weights, or the level of the one prescribed clipping.

The event is simultaneous over deletion sets and times for this prescribed dynamics. Uniform constants in the clipping level do not mean a single event simultaneous over all clipping levels. The candidate preserves this distinction through its requirement of one prescribed common clipping (lines 10–15 and 58–61).

All vectors below use ordinary Euclidean norms; all matrix differences use ordinary Frobenius norms. In particular, writing \(x^{(1)}\) for the dependency's first-layer state coordinate \(X^{(1)}\), the common state distance is exactly

\[
y_E(t)=\frac1n\|x^{(1)}(t)-\widehat x^{(1)}(t)\|_2^2
 +\|W^{(2)}(t)-\widehat W^{(2)}(t)\|_{\rm F}^2
 +\|W^{(3)}(t)-\widehat W^{(3)}(t)\|_{\rm F}^2
 +\frac1n\|W^{(4)}(t)-\widehat W^{(4)}(t)\|_2^2.
\]

Thus the candidate has not changed the matrix normalization or replaced the state in an input estimate by a different distance. The notation \(x^{(1)}=F(z^{(1)})\) does not introduce a claim controlling an additional raw first-layer norm. No property of \(F\) beyond identifying that same state coordinate is used in the new proof.

Each hat refers to the one fully pruned reference for that deletion set. The compared parameter matrices are the raw evolving matrices; the deletion is implemented by the prescribed coordinate masks. Shared initial raw states therefore give \(y_E(0)=0\), despite possible initial differences in intermediate activations caused by a nonempty mask. Empty deletion gives the full network itself, so \(y_{\varnothing}(t)=0\) at every time. Consequently

\[
Y_r(t)=\max_{|F|\le\lfloor nr\rfloor}y_F(t),\qquad 0\le r\le1,
\]

is a finite maximum, is nonnegative and nondecreasing in \(r\), and equals zero for \(0\le r<1/n\). The inclusion of the indexing families proves the monotonicity. This definition includes no time supremum. Distinct layer populations remain distinct: the deletion mask, query, and gate vector all act in the middle population, while \(W^{(3)}\) maps from that population to the top hidden population.

Write

\[
q(t)=(W^{(3)}(t))^T
 [W^{(4)}(t)\odot\phi'(z^{(3)}(t))],
\qquad q_{*,j}(t)=\sup_{0\le u\le t}|q_j(u)|.
\]

This is the actual top-transpose query in the input estimate. Passing from the dependency's normalized vector notation to ordinary vector notation changes its squared vector norms into explicit \(1/n\) sums. It does not introduce an extra factor into the transpose, since both hidden vector spaces have the same normalization. Clipping the middle update does not replace this query by a clipped or independent query.

Define

\[
h(r)=r\log(e/r)\quad(0<r\le1),\qquad h(0)=0,
\]

\[
\Phi(x)=x\left[1+\frac12\log_+(1/x)\right]
\quad(x>0),\qquad \Phi(0)=0,
\qquad A(y)=\min\{1,C_0y\}.
\]

Here \(C_0\ge1\) is explicitly specified by the dependency at lines 141–142. The only substantive analytic/probabilistic estimates taken as premises are the following three.

First, dependency (6), at grid sizes \(k/n\), gives, simultaneously for \(1\le k\le n\) and \(0\le t\le S\),

\[
\max_{|F|\le k}\frac1n\sum_{j\in F}q_{*,j}(t)^2
\le C\left[t^2\{h(k/n)+\epsilon_n^2\}
 +t\int_0^t\Phi(Y_{k/n}(u))\,du\right]. \tag{P1}
\]

For \(k=0\), the sum is exactly zero by definition; an error term need not and must not be inserted when exploiting this exact identity.

Second, dependency (9), for the actual gate weights and \(p_E=|E|/n\), gives

\[
a_E(t)\le A(y_E(t)),\qquad
\frac1n\|q(t)-\widehat q(t)\|_2^2
\le C\{y_E(t)+p_E\}. \tag{P2}
\]

Third, dependency (17) gives

\[
y_E(t)\le C\left[
t\{h(p_E)+\epsilon_n^2\}
 +\int_0^t\Phi(y_E(s))\,ds
 +\int_0^t\sqrt{y_E(s)}\,
       \frac{\|v_E(s)\|_2}{\sqrt n}\,ds
\right]. \tag{P3}
\]

The audit does not reconstruct or assume an additional proof tree behind these granted estimates. In particular, the new derivation below uses neither the dependency's gate bound (14) nor its hierarchy (19).

The proof proceeds by exact finite fractional selection, interpolation of the input bounds, the common-clipping gate comparison, and scalar absorption followed by a finite-set maximum.

## 2. Exact fractional selection and its normalization

Fix \(t\) and sort the \(n\) nonnegative numbers \(q_{*,j}(t)^2\), with their weights reordered by the same permutation, as

\[
b_1\ge b_2\ge\cdots\ge b_n\ge0,
\qquad B_k=\frac1n\sum_{j=1}^k b_j,\quad B_0=0.
\]

Nonnegativity implies that \(B_k\) equals the maximum over sets of size at most \(k\), including when some \(b_j\) vanish or tie. Ties can be ordered arbitrarily.

Let \(0\le w_j\le1\), put \(a=(1/n)\sum_jw_j\), and first suppose \(0\le a<1\). Write \(na=k+\theta\), with \(k=\lfloor na\rfloor<n\) and \(0\le\theta<1\). Then

\[
\sum_{j=1}^n w_jb_j
=(k+\theta)b_{k+1}
 +\sum_{j=1}^n w_j(b_j-b_{k+1}).
\]

For \(j\le k\), the latter summand is at most \(b_j-b_{k+1}\), since its factor in parentheses is nonnegative and \(w_j\le1\). For \(j>k\), the summand is nonpositive, since its factor in parentheses is nonpositive and \(w_j\ge0\). Hence

\[
\frac1n\sum_{j=1}^n w_jb_j
\le\frac1n\sum_{j=1}^k b_j+\frac{\theta}{n}b_{k+1}
=(1-\theta)B_k+\theta B_{k+1}. \tag{A1}
\]

The factor on the fractional coordinate is \(\theta/n\), as required by ordinary norms and the specified empirical mass. Filling the first \(k\) weights with one, the next with \(\theta\), and the rest with zero attains equality. This proves the sharpness actually asserted in candidate (6): sharpness of the selection step given just the fixed mass and coordinatewise constraints.

If \(a=0\), all weights are zero. If \(a=1\), all weights are one, and the result is \(B_n\) with no \(b_{n+1}\). These cases also cover the boundaries for \(n=1\). The later entropy upper bound need not attain equality; the candidate does not assert an optimal constant for that subsequent bound.

## 3. Interpolating the granted prefixes, including the width floor

The continuous extension of \(h\) at zero is valid because \(r\log(1/r)\to0\). On \(0<r\le1\),

\[
h'(r)=\log(1/r)\ge0,\qquad h''(r)=-1/r<0.
\]

It follows, including the endpoint zero by continuity, that

\[
(1-\theta)h(k/n)+\theta h((k+1)/n)\le h(a). \tag{A2}
\]

Apply (P1) to the nonzero grid sizes in (A1), and use \(B_0=0\) exactly. The coefficient of \(t^2\epsilon_n^2\) is

\[
(1-\theta)\mathbf1_{\{k\ge1\}}+\theta
=\begin{cases}
na,&k=0,\\
1,&k\ge1,
\end{cases}
=\min\{1,na\}. \tag{A3}
\]

Because \(\theta\) is fixed at the present \(t\), the history term obtained by adding the two bounds is exactly

\[
t\int_0^t\left[
(1-\theta)\Phi(Y_{k/n}(u))
 +\theta\Phi(Y_{(k+1)/n}(u))
\right]\,du
=t\int_0^t\mathcal I_n(a,u)\,du. \tag{A4}
\]

This is interpolation of the values of \(\Phi\). No interpolation of trajectories and no interchange of \(\Phi\) with interpolation has occurred. In particular, the proof requires no concavity assertion about \(\Phi\).

Combining (A1)–(A4) proves candidate (5):

\[
\frac1n\sum_{j=1}^n w_jq_{*,j}(t)^2
\le C\left[
t^2h(a)+t^2\epsilon_n^2\min\{1,na\}
 +t\int_0^t\mathcal I_n(a,u)\,du
\right]. \tag{A5}
\]

For \(a=1\), this is (P1) with \(k=n\). For \(a=0\), both sides are exactly zero. For \(0<a<1/n\), its actual interpolation is

\[
\mathcal I_n(a,u)=na\,\Phi(Y_{1/n}(u)),
\qquad \min\{1,na\}=na.
\]

The nonzero quantity here comes from taking a fraction of the one-coordinate prefix bound; it does not posit a nonempty deletion of mass below \(1/n\). At every grid point the left and right interpolation definitions agree. At \(a=1\), the separately assigned endpoint agrees with the limit from the last grid interval.

The selection argument is deterministic for every \(w\in[0,1]^n\) on the same event. Sorting the actual query does not change its law or substitute another path. The weights can be selected from the full path, the pruned path, both paths, or further information: no independence assumption, new event, or union bound over weights is needed. There is also no new measurability issue for (A5), which holds for every numerical weight vector at each fixed realization and time. The history integrates in \(u\) while holding the present mass \(a\) fixed.

## 4. Comparison of the actual uncompressed gate vector

For the arctangent activation,

\[
\phi'(x)=\frac1{1+x^2}\in[0,1].
\]

Put

\[
d_j=\mathbf1_{\{j\notin E\}}
 [\phi'(z^{(2)}_j)-\phi'(\widehat z^{(2)}_j)],
\quad w_j=|d_j|^2,\quad
a_E=\frac1n\sum_{j=1}^n w_j.
\]

Then \(|d_j|\le1\), so the weights satisfy all hypotheses of (A5), and \(v_{E,j}=d_j\tau(\widehat q_j)\). Adding and subtracting the same prescribed \(\tau(q_j)\) gives

\[
\begin{aligned}
|v_{E,j}|
&\le |d_j|\,|\tau(q_j)|
 +|d_j|\,|\tau(\widehat q_j)-\tau(q_j)|\\
&\le\sqrt{w_j}\,|q_j|
 +\sqrt{w_j}\,|\widehat q_j-q_j|\\
&\le\sqrt{w_j}\,q_{*,j}(t)+|\widehat q_j-q_j|.
\end{aligned} \tag{A6}
\]

The second line uses domination and the Lipschitz bound, and the third uses \(w_j\le1\) and \(|q_j(t)|\le q_{*,j}(t)\). These estimates remain valid on deleted coordinates, where \(d_j=0\).

Squaring with \((r+s)^2\le2r^2+2s^2\), summing, and retaining the explicit normalization yields

\[
\frac1n\|v_E(t)\|_2^2
\le\frac2n\sum_{j=1}^n w_j(t)q_{*,j}(t)^2
 +\frac2n\|q(t)-\widehat q(t)\|_2^2.
\]

Now (A5) and (P2) give exactly the form of candidate (8):

\[
\begin{aligned}
\frac1n\|v_E(t)\|_2^2\le C\bigg[
&y_E(t)+p_E+t^2h(a_E(t))
 +t^2\epsilon_n^2\min\{1,na_E(t)\}\\
&+t\int_0^t\mathcal I_n(a_E(t),u)\,du
\bigg]. \tag{A7}
\end{aligned}
\]

Thus this is a bound on the whole actual gate vector. No compressed image, second pruning, or separate Gaussian query estimate has entered. The proof uses only the two stated properties of \(\tau\), so it introduces no dependence on its prescribed level. A different clipping in the hatted network would invalidate the subtraction in (A6); the candidate explicitly requires the same clipping.

## 5. Every monotonicity needed for mass replacement

For \(0<x<1\),

\[
\Phi'(x)=\frac12+\frac12\log(1/x)>0.
\]

For \(x>1\), \(\Phi(x)=x\). Its values match at \(x=1\), and its limit at zero is zero. Hence \(\Phi\) is nonnegative, nondecreasing, and continuous on \([0,\infty)\). It also satisfies \(\Phi(x)\ge x\).

Since \(Y_{k/n}(u)\) is nondecreasing in \(k\), the node values \(\Phi(Y_{k/n}(u))\) are nondecreasing. On each open interpolation interval, the slope of \(\mathcal I_n(a,u)\) in \(a\) is

\[
n\{\Phi(Y_{(k+1)/n}(u))-\Phi(Y_{k/n}(u))\}\ge0.
\]

The values agree at all common endpoints, so the interpolant is nonnegative and nondecreasing on all of \([0,1]\), including zero and one. We already verified that \(h\) is nondecreasing on this interval; so are \(a\mapsto\min\{1,na\}\) and \(A\).

Using \(a_E(t)\le A(y_E(t))\) from (P2) therefore enlarges every mass-dependent term of (A7). For the history this gives

\[
\int_0^t\mathcal I_n(a_E(t),u)\,du
\le\int_0^t\mathcal I_n(A(y_E(t)),u)\,du.
\]

The argument of the interpolant on the right is the current-time value \(A(y_E(t))\), held fixed throughout the \(u\)-integral. Replacing it by \(A(y_E(u))\) would be a different assertion and is not done. No monotonicity of \(y_E\) or \(Y_r\) in time is asserted or used.

## 6. Scalar absorption with all endpoint cases

The entropy absorption needed at candidate lines 191–195 holds for every \(y\ge0\), so this step does not require an additional theorem giving a uniformly bounded interval for \(y\).

At \(y=0\), both sides are zero. If \(0<C_0y\le1\), then \(y\le1\). Set \(L=\log(1/y)\ge0\). Since \(C_0\ge1\),

\[
h(A(y))=C_0y\{1+L-\log C_0\}
\le C_0y(1+L).
\]

Furthermore, \((1+L/2)^2\ge1+L\), so

\[
\sqrt y\sqrt{h(A(y))}
\le\sqrt{C_0}\,y\sqrt{1+L}
\le\sqrt{C_0}\,y(1+L/2)
=\sqrt{C_0}\,\Phi(y). \tag{A8}
\]

If \(C_0y\ge1\), then \(A(y)=1\), \(h(A(y))=1\), and \(y\ge1/C_0\). Therefore

\[
\sqrt y\sqrt{h(A(y))}=\sqrt y
\le\sqrt{C_0}\,y\le\sqrt{C_0}\,\Phi(y).
\]

Both arguments agree at \(C_0y=1\). This proves (A8) without a hidden small-distance assumption or division by zero.

After replacing \(a_E(s)\) in (A7), taking a square root term by term is valid because every summand is nonnegative. Writing \(y=y_E(s)\) just within the following display gives

\[
\begin{aligned}
\sqrt y\,\frac{\|v_E(s)\|_2}{\sqrt n}
\le C\bigg[
&y+\sqrt{yp_E}+s\sqrt{y\,h(A(y))}\\
&+s|\epsilon_n|\sqrt y\,
           \sqrt{\min\{1,nA(y)\}}\\
&+\left\{ys\int_0^s\mathcal I_n(A(y),u)\,du\right\}^{1/2}
\bigg]. \tag{A9}
\end{aligned}
\]

There is no missing \(n\) factor: the square root of \((1/n)\|v_E\|_2^2\) is \(\|v_E\|_2/\sqrt n\).

For \(s\le S\), (A8), \(\Phi(y)\ge y\), and the elementary inequalities

\[
\sqrt{yp_E}\le\tfrac12(y+p_E),\qquad
|\epsilon_n|\sqrt y\le\tfrac12(y+\epsilon_n^2),\qquad
\min\{1,nA(y)\}\le1
\]

bound the first four terms in (A9) by

\[
C\{\Phi(y)+p_E+\epsilon_n^2\}.
\]

Since \(h(p_E)\ge p_E\) for \(0\le p_E\le1\), integration and substitution into (P3) yield the individual-set inequality

\[
\begin{aligned}
y_E(t)\le C\bigg[
&t\{h(p_E)+\epsilon_n^2\}
 +\int_0^t\Phi(y_E(s))\,ds\\
&+\int_0^t
 \left\{y_E(s)s\int_0^s
 \mathcal I_n(A(y_E(s)),u)\,du\right\}^{1/2}\,ds
\bigg]. \tag{A10}
\end{aligned}
\]

Only the nonhistory terms used the upper bound \(s\le S\). The factor \(s\), the square root, and the inner time integration in the last term remain intact. Bounding the width factor by one here is a valid weakening for the hierarchy; it does not alter the exact width factor already proved in the direct gate bound.

## 7. Passage to the entire finite comparison hierarchy

Fix any \(p\in[0,1]\), not necessarily a size-grid point. For each set with \(|E|\le\lfloor np\rfloor\), one has \(p_E\le p\), so

\[
h(p_E)\le h(p),\qquad y_E(s)\le Y_p(s),\qquad
\Phi(y_E(s))\le\Phi(Y_p(s)).
\]

For fixed \(s\ge0\), define just for this monotonicity check

\[
G_s(y)=\left\{ys\int_0^s\mathcal I_n(A(y),u)\,du\right\}^{1/2}.
\]

If \(0\le y_1\le y_2\), then \(A(y_1)\le A(y_2)\) and the corresponding integral for \(y_1\) is at most the one for \(y_2\). Both integrals are nonnegative. Thus

\[
y_1\int_0^s\mathcal I_n(A(y_1),u)\,du
\le y_2\int_0^s\mathcal I_n(A(y_1),u)\,du
\le y_2\int_0^s\mathcal I_n(A(y_2),u)\,du.
\]

Multiplication by \(s\ge0\) and taking a square root preserve the inequalities. Hence \(G_s\) is nondecreasing, including across interpolation grid points and the saturation point of \(A\).

Replacing the integrands in (A10) by these common upper bounds gives a right-hand side independent of \(E\). Taking the maximum on the left proves, for every \(p\in[0,1]\),

\[
\begin{aligned}
Y_p(t)\le C\bigg[
&t\{h(p)+\epsilon_n^2\}
 +\int_0^t\Phi(Y_p(s))\,ds\\
&+\int_0^t
 \left\{Y_p(s)s\int_0^s
 \mathcal I_n(A(Y_p(s)),u)\,du\right\}^{1/2}\,ds
\bigg]. \tag{A11}
\end{aligned}
\]

This is candidate (10). No equality interchanging a maximum and an integral is required; the argument gives an inequality for each set before maximizing. Nor must a single set maximize at all times. Finite proxy paths are continuous on the prescribed horizon; finite maxima of their continuous state distances are continuous, and the finite interpolation is continuous at its grid junctions. The integrals used here are consequently well defined without a measurable-selection theorem.

For \(p<1/n\), only the empty deletion occurs, so \(Y_p(s)=0\) for every \(s\). Then \(A(Y_p(s))=0\), the interpolant and both integral terms vanish, and (A11) reads \(0\le Ct\{h(p)+\epsilon_n^2\}\). This includes \(p=0\). At \(t=0\), every term in (A11) is zero. At \(p=1\), and whenever \(A(Y_p(s))=1\), the separately defined endpoint of the interpolant is used. There is no out-of-range deletion size.

The assertions are simultaneous over all \(p\): after the event is fixed, the finite family of state distances defines every such envelope, and \(h(p_E)\le h(p)\) supplies the deterministic extension from grid sizes to arbitrary \(p\). The proof introduces no continuum of new probabilistic events.

## 8. Meaning of the claimed improvement and its limits

The entropy change is a literal reduction of the size functional. With \(L=\log(1/a)\ge0\) and the dependency's displayed older function \(\Psi\),

\[
\Psi(a)-h(a)=\tfrac12aL^2\ge0\qquad(0<a\le1),
\]

and both functions vanish at zero. The exact interpolated entropy before (A2) can be smaller still; that does not impair the stated bound.

One can also verify directly that the new history functional does not exceed the older Hardy functional, without taking that older gate theorem as an input. Let \(J(r)=\Phi(Y_r(u))\), so \(J\) is nonnegative, nondecreasing, and zero for \(r<1/n\). For comparison only, use the dependency's explicit definition

\[
H_{a,n}J=aJ(1)+a\int_{\max\{a,1/n\}}^1\frac{J(r)}{r^2}\,dr,
\qquad H_{0,n}J=0.
\]

If \(0<a<1/n\), monotonicity gives

\[
H_{a,n}J
\ge aJ(1/n)+aJ(1/n)\int_{1/n}^1r^{-2}\,dr
=naJ(1/n)=\mathcal I_n(a,u).
\]

For \(1/n\le a<1\), write \(na=k+\theta\) as before and \(b=(k+1)/n\). Lower-bounding \(J\) by \(J(k/n)\) on \([a,b)\) and by \(J(b)\) on \([b,1]\) gives

\[
H_{a,n}J\ge(1-a/b)J(k/n)+(a/b)J(b).
\]

But

\[
\frac ab=\frac{k+\theta}{k+1}\ge\theta,
\]

and \(J(b)\ge J(k/n)\). Therefore this lower bound is at least

\[
(1-\theta)J(k/n)+\theta J(b)=\mathcal I_n(a,u).
\]

At \(a=0\) and \(a=1\) the comparison is equality. Thus the description of the new estimate as sharper is justified at the level of its entropy and history functionals. No optimality of the overall unspecified constants is claimed or needed.

The history in (A11) nevertheless samples the two size-grid points adjacent to \(A(Y_p(s))\), which need not be adjacent to or bounded above by \(p\). Even when \(A(Y_p(s))<1/n\), the one-deletion history enters multiplied by \(nA(Y_p(s))\). This preserves the width floor but does not by itself prove any limiting continuity statement. None is claimed in the candidate.

The scope remains the canonical zero-initial-readout finite proxies on the granted event. In particular, the small-time factors in (P1) are not rederived for a nonzero initial readout. The proof gives no positive-time transfer from finite-jet information, no simultaneous event over all clipping choices, and no limit theorem removing clipping. Gaussian initialization and the reused matrices enter through the stated model and the granted event; the new deterministic inequalities require no further Gaussian or independence theorem.

## Final determination

Every new implication in candidate (1)–(10) is valid within its stated setup and the three expressly granted estimates. The normalizations, zero and full masses, integer grid boundaries, finite-width floor, arbitrary selection on the common event, interpolation of \(\Phi\)-values, clipping comparison, scalar absorption, and passage to all finite-set envelopes are consistent. The candidate's explicit refusal to infer continuation or population conclusions accurately states the remaining limitation.

**PASS. Required mathematical fixes: none.**
