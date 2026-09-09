# Independent adversarial audit

Date: 25 August 2026.

Scope: `ROUTE_PAIRED.md`, Sections 2--4, and the single-space obstruction in
`ROUTE_NORM_NOGO.md` and `SINGLE_SPACE_NORM_NO_GO.md`.

## 1. Verdict

1. **Exact paired factorization: pass, with an explicit regularity
   qualification.**  Equations (3.1)--(3.14) of `ROUTE_PAIRED.md` are exact
   under \(C^1\) regularity along the finitely many displayed line segments.
   The order of the noncommuting maps in the hybrid telescope is correct.
2. **Parity/Taylor reduction: pass conditionally.**  If every
   \(A_{j,t}\in C^3[-\rho/t,\rho/t]\) and the already established annealed
   sign involution is available, then (4.3)--(4.9), including the sign of
   \(\kappa\) and the factor \(1/6\), are correct.  These sections do not prove that
   \(C^3\) regularity or the uniform estimate (4.8) on the actual OMFP DAG;
   they correctly leave that network theorem open.
3. **Full Banach-algebra no-go: pass.**  No norm of the displayed form which
   contains a Gaussian-like unbounded initialization atom can satisfy a
   quantitative same-space product inequality on its whole domain.  The
   proof already closes at source order zero and survives all choices of
   \(w_m,p_m\) for \(m\ge1\).
4. **Reachable-only no-go: not proved.**  The Gaussian-power proof iterates
   multiplication on arbitrary powers.  It does not rule out a nonalgebraic
   module or a grammar-restricted estimate only for pairs that occur in the
   paired OMFP DAG.  `ROUTE_PAIRED.md`, lines 23--28, states this limitation
   correctly.  The stronger wording in `SINGLE_SPACE_NORM_NO_GO.md`, lines
   100--121, that the requested one-step estimate itself necessarily controls
   Gaussian powers is unsupported until a bounded inclusion/projection
   argument isolates a Gaussian multiplication block of \(Dg(\theta_0)\) on
   the claimed reachable domain.

Thus the exact coarse/fine reduction is established, and the requested
**full same-space product-closed norm architecture** is impossible.  The
scalar \(Ct^4|\eta|^5\) theorem, and even a reachable-only all-source
stability theorem, remain open.

## 2. Audit of the paired factorization

Write

\[
 E_hx=x+hg(x),\qquad B_h=E_h\circ E_h,\qquad C_h=E_{2h}.
\]

Direct expansion gives

\[
 B_hx-C_hx
 =h\{g(x+hg(x))-g(x)\}
 =h^2\int_0^1Dg(x+shg(x))[g(x)]\,ds.
\]

This proves the local factorization for either sign of \(h\), provided
\(s\mapsto g(x+shg(x))\) is continuously differentiable (absolute
continuity with the displayed a.e. derivative would also suffice).  Mere
existence of isolated directional derivatives is not sufficient for this
fundamental-theorem-of-calculus step; the prose at lines 51--54 should be
read with this stronger qualification.

For

\[
 H_j=\mathcal O(C_h^{t-j}B_h^j\theta_0),\quad
 y_j=B_h^{j-1}\theta_0,\quad m_j=t-j,
\]

one has, with no commutation assumption,

\[
 H_j-H_{j-1}
 =(\mathcal O\circ C_h^{m_j})(B_hy_j)
  -(\mathcal O\circ C_h^{m_j})(C_hy_j).
\]

The segment formula therefore yields exactly

\[
 H_j-H_{j-1}=h^2A_{j,t}(h),\qquad
 \Delta_t(h)=h^2\sum_{j=1}^tA_{j,t}(h).
\]

The tangent recursion (3.9)--(3.14) is the chain rule for
\(D C_h^m\); its factor order is correct because the rightmost Jacobian acts
first.

Put \(S_t=\sum_jA_{j,t}\).  From the exact annealed parity
\(\Delta_t(-h)=-\Delta_t(h)\) and \(\Delta_t=h^2S_t\), \(S_t\) is odd for
\(h\ne0\).  If \(S_t\in C^3\), continuity gives oddness at zero, whence

\[
 S_t(0)=S_t''(0)=0,\qquad \kappa_t=S_t'(0).
\]

Since

\[
 \Delta_t'''(0)=F_{2t}'''(0)-8F_t'''(0)=6S_t'(0),
\]

equation (4.4) is correct.  The established cubic law for the opposite
orientation \(F_t(2h)-F_{2t}(h)\) is
\(-t(2t-1)J_{\psi,2}/2\); hence the sign in (4.5), for fine minus coarse,
is also correct.

Finally, third-order integral Taylor expansion gives, for either sign of
\(h\),

\[
 S_t(h)-\kappa_th
 =\frac12\int_0^h(h-u)^2S_t'''(u)\,du,
\]

and therefore

\[
 |\Delta_t(h)-\kappa_th^3|
 \le \frac{|h|^5}{6}\sup_{|u|\le |h|}|S_t'''(u)|.
\]

If \(\sup_{j,u}|A_{j,t}'''(u)|\le C_A t^3\), then
\(\sup_u|S_t'''(u)|\le C_A t^4\), proving (4.9).  No separate fine/coarse
output estimate and no fifth derivative of either output enters.

## 3. Audit of the source-order-zero obstruction

Let a norm of the requested form contain \(1\) and a standard Gaussian
\(G\), and suppose its product is jointly quantitatively closed:

\[
 \|UV\|_{\mathfrak X}
 \le C_\times\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}.
\]

Because \(1\) has no positive-order source derivatives, \(w_0=0\) would
give \(\|1\|_{\mathfrak X}=0\); hence \(w_0>0\).  If \(p_0=\infty\),
\(G\notin\mathfrak X\).  If \(p_0<\infty\), product iteration and the
zeroth-order summand imply

\[
 w_0\|G\|_{np_0}^{n}
 \le \|G^n\|_{\mathfrak X}
 \le C_\times^{n-1}\|G\|_{\mathfrak X}^{n}.
\]

The elementary Gaussian bound \(\|G\|_q\ge c\sqrt q\) makes the
\(n\)-th root of the left side diverge like \(\sqrt n\), whereas the
right side stays bounded.  This is a complete contradiction.  The typo
​`\|G\|_{np_0}^{,n}` in `SINGLE_SPACE_NORM_NO_GO.md` (2.2) should be
​`\|G\|_{np_0}^{n}`; it does not affect the argument.

The raw-source premise can be weakened to the actual normalized activated
Gaussian.  Set

\[
 X_\alpha=\psi_\alpha(G)
 =\frac{G+\alpha\varphi(G)}{s_\alpha},\qquad
 s_\alpha=\|G+\alpha\varphi(G)\|_2.
\]

Since the \(r=0\) hypothesis gives \(\|\varphi\|_\infty\le M\),
the denominator is positive, \(s_\alpha\le1+|\alpha|M\), and
\(X_\alpha\) is essentially unbounded.  For every finite \(q\),

\[
 \|X_\alpha\|_q
 \ge \frac{\|G\|_q-|\alpha|M}{1+|\alpha|M}
 \ge c_\alpha\sqrt q
\]

for all sufficiently large \(q\).  Thus any product-closed same-space norm
containing \(X_\alpha\) yields the identical contradiction by iterating
\(X_\alpha^n\).  This removes the possible objection that the norm might
store activated fields but not the raw coordinate itself.

If "closure" means joint continuity or local boundedness of the bilinear
product, it still yields a global estimate of the displayed form by
bilinearity and rescaling.  Pure algebraic membership, with no quantitative
bound, evades the contradiction but cannot supply the explicit one-step
constant requested in the problem.

## 4. Loopholes and required corrections

### 4.1 Reachable-only multiplication

The preceding argument requires \(X^n\in\mathfrak X\) for every \(n\), as
follows from a product estimate valid for all \(U,V\in\mathfrak X\).  If the
proposed object is instead a module with product estimates only for a
specified list of coefficient/tangent pairs, powers need not belong to its
domain.  Neither no-go note proves that every power is an actual OMFP
reachable history.  Accordingly:

- the no-go **does** refute the literal full same-space product closure
  demanded in item 3;
- it **does not** refute a history/tree-dependent reachable grammar or a
  radius-losing scale;
- statements that the scalar remainder theorem itself is false would be
  invalid (neither note makes that statement).

### 4.2 The one-step multiplier claim

At \(L=2\), differentiating
\(\delta_2=A\psi_\alpha'(z_2)\) produces the block

\[
 \delta\delta_2
 =v_A\psi_\alpha'(z_2)
  +A\psi_\alpha''(z_2)\,\delta z_2.
\]

This displays an unbounded Gaussian coefficient for every nonzero
\(\alpha\) with \(\varphi''\not\equiv0\).  It is strong evidence against
a same-space tangent bound.  It is not by itself a proof that the full
matrix \(Dg(\theta_0)\) contains a boundedly isolated copy of the
multiplication operator \(V\mapsto AV\).  Such a proof must specify the
state norm, bounded component projections/inclusions, the range of
\(\delta z_2\), and the reachable class of \(V\).  Therefore the final
sentence of Section 3 in `SINGLE_SPACE_NORM_NO_GO.md` should be weakened to
a conditional observation.  The full product-algebra no-go does not need
this sentence.

### 4.3 Source-shift versus Leibniz

The contradiction (3.1)--(3.5) in `ROUTE_NORM_NOGO.md` is valid for an
unnormalized derivative hierarchy, coefficientwise absolute Leibniz
estimation, and compatible moment exponents.  It is not a theorem about
every possible history aggregation: normalized derivatives move the
combinatorial factor from the Leibniz rule into the source shift, and a
grammar-specific cancellation can avoid coefficientwise inequalities.
The note mostly records this scope at lines 263--268.  This secondary
argument should not be cited as stronger than the source-order-zero theorem.

### 4.4 Quantifier conclusion

No constants \(\alpha_0,\rho,C\) satisfying the requested scalar theorem
have been constructed by these notes.  What is unconditional is:

\[
 \Delta_t(h)=h^2\sum_{j=1}^tA_{j,t}(h)
\]

and the implication

\[
 \sup_{j\le t,\ |u|\le\rho/t}|A_{j,t}'''(u)|\le C_A t^3
 \quad\Longrightarrow\quad
 |\Delta_t(h)-\kappa_th^3|
 \le \frac{C_A}{6}t^4|h|^5.
\]

The full same-space Banach-algebra route to the premise is impossible; a
reachable-only or radius-loss proof of the premise remains an open bridge.
