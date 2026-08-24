# Exact nonlinear carrier audit for the signed predictor increments

The purpose of this note is to test the predictor before squaring or Taylor
expanding any arctangent divided difference.  A *carrier* means an exposed
unbounded Gaussian factor.  Bounded nonlinear functions of any number of past
variables do not count as carriers; this is justified only when the bound is
kept pointwise and no derivative expansion re-exposes those variables.

## 1. Exact one-query normal form

At a chronological forward query, let \(g\) be the fresh Gaussian row-space
innovation, let \(\widetilde x=\alpha e\) be the new feature residual, and
write

\[
 z^+=c+\alpha g,qquad
 b^+=a^+d(c+\alpha g),qquad
 \bar b^+=a^+d(c).
\]

Let \(b\) be the previous backward feature and put

\[
 \delta:=\bar b^+-b,qquad
 \Delta d:=d(c+\alpha g)-d(c).
\]

For a fixed predictor coordinate \(j\), let \(v_j\) be the old canonical
row-space functional and \(\xi_j\) the coefficient of the new paired feature
direction.  With the isonormal Gaussian pairing denoted by \(\mathcal I_g\),
extension consistency gives exactly

\[
\begin{aligned}
 \Delta P_j={}&L_{v_j}(\delta)+\xi_j\mathcal I_g(\delta)\\
 &+L_{v_j}(a^+\Delta d)
       +\xi_j\mathcal I_g(a^+\Delta d).             \tag{1}
\end{aligned}
\]

This is the invariant form of the four-term expansion in
`predictor_chronological_decomposition.md`.  It already contains the
two-sided covariance projections in \(v_j\) and in the covariance of \(g\).

## 2. The divided-difference identities that control carrier degree

For a scalar fresh coordinate, put \(q=\alpha g\).  The exact identity

\[
 q\,Dd(c,c+q)=d(c+q)-d(c)=\Delta d               \tag{2}
\]

implies

\[
 |\Delta d|\le1,qquad
 |\alpha gDd(c,c+\alpha g)|\le1,                  \tag{3}
\]

and

\[
 |\alpha g^2Dd(c,c+\alpha g)|
 =|g\Delta d|\le|g|.                              \tag{4}
\]

Thus the term that a frozen-coefficient expansion calls "quadratic Gaussian"
is exactly one fresh Gaussian carrier times a bounded increment.  No power
\(g^2\) survives.

There are also uniform conditional-mean bounds which avoid Stein
differentiation of the random divided difference.  If \(G\sim N(0,1)\), then

\[
 \left|\mathbf E[d(c+\alpha G)-d(c)]\right|
 \le C\min\{\alpha^2,1\},                          \tag{5}
\]

and

\[
 \left|\mathbf E[G\{d(c+\alpha G)-d(c)\}]\right|
 \le C\min\{|\alpha|,1\}.                         \tag{6}
\]

For (5), Taylor's formula with integral remainder gives

\[
 d(c+\alpha G)-d(c)=\alpha Gd'(c)
 +\alpha^2G^2\int_0^1(1-s)d''(c+s\alpha G)\,ds.
\]

The first term has zero mean and \(d''\) is bounded, proving the
\(C\alpha^2\) bound; \(|d|\le1\) proves the bound by a constant.  For (6),
Cauchy--Schwarz and the Lipschitz bound on \(d\) give \(C|\alpha|\), while
\(|\Delta d|\le1\) gives a constant.  The same estimates hold for a projected
fresh Gaussian block after contraction with its covariance projection.

Equations (5)--(6) are preferable to writing the Stein derivative
\(\Delta d+\alpha Gd'(c+\alpha G)\): the two pieces of that derivative can be
large separately although their expectation is bounded by (6).

## 3. Local carrier count

The zero-fresh endpoint difference satisfies the pointwise bound

\[
 |\delta|le |a^+-a|+2|a|,                         \tag{7}
\]

and the actual Euler update gives \(|a^+-a|\le Ch\).  Hence \(\delta\) has at
most the one Gaussian endpoint carrier \(A^0\); all predictor dependence is
inside bounded values of \(d\).  Similarly,

\[
 |a^+\Delta d|\le |a^+|.                           \tag{8}
\]

The four terms in (1) therefore have the following exposed carriers:

\[
\begin{array}{c|c}
\text{term}&\text{exposed carriers}\\ \hline
L_{v_j}(\delta)&\text{one old canonical carrier and }A^0\\
\xi_j\mathcal I_g(\delta)&g\text{ and }A^0\\
L_{v_j}(a^+\Delta d)&\text{one old canonical carrier and }A^0\\
\xi_j\mathcal I_g(a^+\Delta d)&g\text{ and }A^0.
\end{array}                                                   \tag{9}
\]

Thus every exact local term has at most two exposed Gaussian carriers.  The
conditional compensators obtained from (5)--(6) have at most the endpoint
carrier and an old canonical carrier; compensation does not raise the degree.

## 4. Reused transpose and learned terms

The backward query at the same Euler cycle reveals a fresh transpose
innovation only after \(b^+\) has been selected.  Conditional on the enlarged
two-sided history it is Gaussian with variance determined by \(\|b^+\|\), and

\[
 \|b^+\|\le\|A^+\|.                                \tag{10}
\]

At the next forward cycle, this transpose innovation affects the feature only
through an exact activation increment

\[
 \Delta X_2=D\!\atan(Z_2,Z_2^+)\,\Delta Z_2.       \tag{11}
\]

The unbounded transpose response in \(\Delta Z_2\) is not expanded out: (11)
is bounded componentwise by the range of arctangent.  Consequently a later
fresh forward carrier multiplied by this feature direction still has only the
fresh carrier and the endpoint mark.  Differentiating (11) would manufacture
spurious higher products; keeping it as an exact increment does not.

The covariance/Onsager corrections in the two-sided Gaussian formula are
orthogonal projections and Gaussian contractions.  A projection preserves
the number of exposed carriers, and a Wick/Stein contraction removes two
carriers or replaces the fresh pair by (5)--(6); neither operation adds a
carrier.

The trained second-layer part has the exact form

\[
 (P_2^k)^*B_3^k
 =\sum_{s<k}h\,X_2^s\langle B_3^s,B_3^k\rangle.    \tag{12}
\]

Since \(X_2\) is bounded and each \(B_3\) has the single endpoint carrier,
(12) exposes at most two endpoint carriers and no fresh Gaussian carrier.
Products of lower-layer backpropagated quantities can have a higher formal
polynomial degree, but in the predictor response they reach the next layer
only through (11), or through its layer-1 analogue.  The exact identity
\(D\!\atan\,\Delta Z=\Delta X\) hides that amplitude inside a bounded
increment before it is multiplied by a new carrier.

Finally, at layer 3,

\[
 hA^kDd(Z_3^k,Z_3^{k+1})
       [W_2^kV_2^k+\rho_2B_3^k]
 =A^k[d(Z_3^{k+1})-d(Z_3^k)],                       \tag{13}
\]

and the \(A\)-source turns (13) into \(B_3^{k+1}-B_3^k\).  This is the exact
Abel collapse proved separately.  It removes the last place where a formal
expansion would multiply a predictor response by \(A^0\).

## 5. What an exact \(Cq\) induction would still have to prove

For one fresh query, (3)--(9), Gaussian conditioning, and
\(\|A^k\|_q\le C_T\sqrt q\) give the correct \(C_Tq\) scale.  The obstacle is
not a local degree-three term.  It is reuse of an old carrier against a future
bounded multiplier.  In endpoint form the unresolved random variable is of
the type

\[
 Y_{m,j}=\sum_{\ell\le m}\xi_{\ell,j}\,
 \mathcal I_{g_\ell}\!\left(A^m\odot f_m(g_0,\ldots,g_m)
 \right),qquad |f_m|\le1,                          \tag{14}
\]

where \(\xi_{\ell,j}\) is chosen before \(g_\ell\), but the terminal bounded
multiplier \(f_m=d(Z_3^m)\) depends on that carrier through all later Euler
steps.  Bessel gives an \(L^2\) bound for (14).  If \(f_m\) were decoupled from
the carriers, conditioning first on \(A^m,f_m\) and then on the Gaussian
series would give

\[
 \|Y_{m,j}\|_q\le C\sqrt q\,\|A^m\|_q\le C_Tq.      \tag{15}
\]

For the actual anticipating multiplier, (15) is precisely the missing causal
decoupling estimate.  Centering each chronological query does not prove it:
centering breaks the exact Abel telescoping and creates the unusable squared
leverage atom described in `annealed_canonical_leverage_test.md`.

One can state the required induction lemma cleanly as follows.

**Signed two-carrier decoupling lemma (needed).**  Along the actual Euler
filtration, every terminal sum of the form (14), with \(f_m\) generated by the
exact bounded increments (2), (11), and (13), satisfies

\[
 \|Y_{m,j}\|_{L^q}\le C_Tq\qquad(q\ge2),             \tag{SD}
\]

uniformly in all widths and meshes.

The local carrier audit proves that the class in (SD) is closed under one
Euler query and under every Stein/Onsager contraction without increasing the
carrier count.  What it does not prove is stability of (SD) under arbitrary
reuse of an old carrier over \(T/h\) later bounded increments.  Proving that
stability requires a signed decoupling or summation theorem which exploits the
actual response dynamics; it does not follow from carrier count and Bessel
alone.

## 6. Outcome of the audit

No exact degree-greater-than-two fresh carrier survives:

* the apparent \(g^2\) term is reduced to \(g\Delta d\) by (2)--(4);
* Stein compensators are bounded by (5)--(6) without exposing another carrier;
* transpose reuse is absorbed into the bounded activation increment (11);
* learned second-layer terms expose only two endpoint marks;
* the full layer-3 response telescopes by (13).

Therefore there is no local algebraic obstruction of the requested type.  The
remaining issue is the global anticipating dependence in (14).  A claimed
arbitrary-time \(C_Tq\) theorem must supply (SD), or an equivalent signed
decoupling statement; treating the chronological increments separately by
quadratic variation loses an extra Gaussian square and cannot establish it.

