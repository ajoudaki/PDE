# Independent audit of FINAL_RESOLUTION.md

Date: 25 August 2026.

## Verdict

\[
\boxed{\text{PASS as a negative resolution, after the objective corrections listed below.}}
\]

This is **not** a pass for the scalar theorem requested in the original
problem.  The audited document correctly proves the exact paired
factorization and its conditional \(t^4\) Taylor reduction, proves that the
stipulated full same-space product-closed norm cannot exist, and labels the
uniform scalar remainder theorem open.

The no-go theorem has the following exact scope: it excludes a jointly
bounded pointwise product on the whole normed space when that space contains
the initialization atom.  It does not exclude a typed module, a product rule
restricted to actual reachable pairs, or a radius-losing scale.  The
resolution states this caveat.

## Corrections made during this audit

Only objective errors or missing hypotheses were patched:

1. \(\Delta_t(h)=F_{2t}(h)-F_t(2h)\) is now explicitly defined.
2. The domain \(|h|\le\rho/t\) is now attached to implication (1.2).
3. The two fundamental-theorem-of-calculus uses now have an explicit
   absolute-continuity hypothesis.
4. The Taylor step now assumes exactly
   \(A_{j,t}\in C^3[-\rho/t,\rho/t]\), rather than the ambiguous phrase
   “the generated curves are \(C^3\).”
5. The activation in the moment list is explicitly set to
   \(\psi=\psi_\alpha\), and two malformed subscripts
   \(\mathsf S_{psi,2},\mathsf H_{psi,2}\) were corrected.
6. The coefficientwise shift argument now says that its unrestricted
   sequence weights are positive; otherwise the displayed majorant is not
   a norm on single-order jets.
7. The conditional-expectation estimate is restricted to Gaussian source
   subspaces and records the Cameron--Martin projection.
8. The radius-scale calculation now specifies that
   \(\mathcal D^m\) is the unnormalized Malliavin derivative.

## 1. Exact paired factorization

For \(E_hx=x+hg(x)\),

\[
\begin{aligned}
B_hx-C_hx
&=E_h(E_hx)-E_{2h}x\\
&=h\{g(x+hg(x))-g(x)\}\\
&=h^2\int_0^1Dg(x+shg(x))[g(x)]\,ds.
\end{aligned}
\]

The last equality follows under the patched absolute-continuity
hypothesis and is valid for either sign of \(h\).

For

\[
H_j=\mathcal O(C_h^{t-j}B_h^j\theta_0),\qquad
y_j=B_h^{j-1}\theta_0,\qquad m_j=t-j,
\]

the noncommuting order is

\[
H_j-H_{j-1}
=(\mathcal O\circ C_h^{m_j})(B_hy_j)
-(\mathcal O\circ C_h^{m_j})(C_hy_j).
\]

The interpolation from \(C_hy_j\) to \(B_hy_j\) therefore gives

\[
H_j-H_{j-1}=h^2A_{j,t}(h).
\]

Summing from \(j=1\) to \(t\) proves

\[
\Delta_t(h)=h^2\sum_{j=1}^tA_{j,t}(h)
\]

before any absolute value.  The tangent recursion in (2.10)--(2.13) is
the ordinary chain rule for \(D C_h^{m_j}\); its factor order is correct.

**Result:** pass.

## 2. Parity and Taylor coefficient

Let \(S_t=\sum_jA_{j,t}\).  For \(h\ne0\),

\[
S_t(h)=\frac{\Delta_t(h)}{h^2}.
\]

The established annealed sign involution makes \(\Delta_t\) odd.  Since
the patched hypothesis gives \(S_t\in C^3\), oddness extends through zero,
and

\[
S_t(0)=S_t''(0)=0,\qquad \kappa_t=S_t'(0).
\]

The exact integral remainder is

\[
S_t(h)-\kappa_th
=\frac12\int_0^h(h-u)^2S_t'''(u)\,du.
\]

Consequently,

\[
|\Delta_t(h)-\kappa_th^3|
\le\frac{|h|^5}{6}\sup_{|u|\le|h|}|S_t'''(u)|.
\]

If every summand obeys
\(\sup_{|u|\le\rho/t}|A_{j,t}'''(u)|\le C_At^3\), then

\[
\sup_{|u|\le\rho/t}|S_t'''(u)|
\le t\,C_At^3=C_At^4,
\]

which proves (1.2), including its factor \(1/6\).

For the fine-minus-coarse orientation,

\[
\Delta_t'''(0)
=F_{2t}'''(0)-8F_t'''(0)=6\kappa_t.
\]

The established opposite-orientation coefficient is
\(-t(2t-1)J_{\psi,2}/2\), so the positive sign in

\[
\kappa_t=\frac{t(2t-1)}2J_{\psi_\alpha,2}
\]

is correct.

**Result:** pass, conditional exactly on the displayed \(C^3\) hypothesis.
The document does not claim to have proved that hypothesis uniformly in
\(t\).

## 3. Explicit activation moments

The nine moments in (3.7) and the formulas (3.8)--(3.11) agree with the
established depth-two cubic recursion.  In the older notation, the
identification is

\[
e_{\rm old}=u,\qquad b_{\rm old}=v,\qquad
v_{\rm old}=s,\qquad s_{\rm old}=e.
\]

Under this substitution, the two invariants are exactly

\[
\mathsf S_{\psi,2}
=3c^2m+3c^3j+3du\beta+3dkm+3d^2j
\]

and

\[
\mathsf H_{\psi,2}
=c^2u+c\ell+2c^2m+3c^3e+cuds
 +2ud^2+3d^2e+k^2\ell+2dkm.
\]

As a control, for the identity activation,

\[
d=u=\ell=1,\qquad
v=m=r=s=j=e=0,\qquad c=k=2.
\]

The formulas give

\[
\mathsf S_{x,2}=0,\qquad
\mathsf H_{x,2}=4+2+2+4=12,\qquad J_{x,2}=48,
\]

which agrees with the independent deep-linear specialization.

Every quantity in the displayed formula is a one-dimensional Gaussian
integral of \(\psi_\alpha\) and its first three derivatives.  No output
supremum, trajectory norm, or unknown continuity modulus occurs.

**Result:** pass.

## 4. Normalized-activation lower bound

Let

\[
s_\alpha=\|G+\alpha\varphi(G)\|_2.
\]

Because the \(r=0\) envelope gives
\(\|\varphi(G)\|_2\le M\), reverse and ordinary Minkowski inequalities give

\[
1-|\alpha|M\le s_\alpha\le1+|\alpha|M.
\]

Thus \(s_\alpha\in[1/2,3/2]\) when \(|\alpha|M\le1/2\).  For every
\(q\ge1\),

\[
\|\psi_\alpha(G)\|_q
\ge
\frac{\|G\|_q-|\alpha|M}{1+|\alpha|M}.
\]

If \(\|G\|_q\ge c_G\sqrt q\), then for

\[
q\ge \left(\frac{2|\alpha|M}{c_G}\right)^2
\]

the right side is at least \(c_G\sqrt q/3\).  Hence condition (4.3)
holds; in fact the coefficient \(c_G/3\) can be chosen uniformly for
\(|\alpha|M\le1/2\).

The atom remains essentially unbounded because it is a nonzero multiple of
\(G\) plus a bounded random variable.  Therefore \(p_0=\infty\) cannot
contain it.

**Result:** pass.

## 5. Product no-go

Since the norm contains \(1\), definiteness forces \(w_0>0\).  For finite
\(p_0\), full same-space product closure gives

\[
\|X^n\|_{\mathfrak X}
\le C_\times^{n-1}\|X\|_{\mathfrak X}^n.
\]

The zeroth source term gives

\[
\|X^n\|_{\mathfrak X}
\ge w_0\|X\|_{np_0}^n.
\]

Using \(\|X\|_{np_0}\ge c_X\sqrt{np_0}\) and taking \(n\)-th roots yields

\[
w_0^{1/n}c_X\sqrt{np_0}
\le C_\times^{1-1/n}\|X\|_{\mathfrak X},
\]

an immediate contradiction as \(n\to\infty\).

The proof depends only on \(m=0\); higher source weights, tensor
aggregation, moment exponents, and singular-covariance quotients cannot
repair it.  A jointly continuous bilinear product also has a global bound
of the displayed form by homogeneity.

The quantifier caveat is essential: a typed or grammar-restricted product
which does not permit all powers \(X^n\) is outside this theorem.  The final
resolution states rather than conceals this limitation.

**Result:** pass.

## 6. Coefficientwise adjoint/product conflict

For ordinary derivative jets \(a_m=D^mV\), boundedness of the left shift
\((Sa)_m=a_{m+1}\), tested on a sequence supported at order \(m\), gives

\[
w_{m-1}\le C_Jw_m.
\]

Leibniz multiplication of sequences supported at orders \(1\) and \(m-1\)
gives

\[
mw_m\le C_Pw_1w_{m-1}.
\]

Since the unrestricted majorant norm has positive weights, division and
combination give

\[
m\le C_PC_Jw_1
\]

for arbitrarily large \(m\), a contradiction.

For normalized jets \(\widehat a_m=D^mV/m!\), the Leibniz coefficient is
one while differentiation acts as

\[
(\widehat S\widehat a)_m=(m+1)\widehat a_{m+1}.
\]

Testing at input order \(m\) again produces the same contradiction.  This
is a theorem only for the unrestricted coefficientwise positive
completion, not for a cancellation-aware reachable grammar.

**Result:** pass with the scope stated in the document.

## 7. Radius-loss coefficient

For the unnormalized derivative norm (5.1), a \(k\)-fold shift sends the
order-\(m+k\) derivative to output order \(m\).  Relative to the
order-\(m+k\) coefficient in the radius-\(\rho\) norm, the coefficient
ratio is

\[
R_m
=\rho^{-k}\frac{(m+k)!}{m!}
 \left(\frac{\rho'}{\rho}\right)^m.
\]

Writing \(x=\rho'/\rho\), one has

\[
\sup_mR_m
\le \rho^{-k}\sum_{m\ge0}\frac{(m+k)!}{m!}x^m
=\rho^{-k}\frac{k!}{(1-x)^{k+1}}
=\frac{k!\rho}{(\rho-\rho')^{k+1}}.
\]

This is exactly (5.5).  It is valid, though deliberately not sharp.  At
\(\rho'=\rho\), \(R_m\) grows polynomially in \(m\), so the unrestricted
positive-majorant shift is unbounded.

The chronological inequality

\[
\sum_{i_1<\cdots<i_k}\prod_r|e_{i_r}|
\le\frac{(\sum_i|e_i|)^k}{k!}
\]

is also correct: the expansion of the \(k\)-th power contains \(k!\)
ordered copies of every distinct-index product, plus nonnegative repeated
index terms.

The document does not infer an OMFP theorem from these scale estimates.  It
correctly identifies the still-missing result: simultaneous control of
radius loss, moment-exponent loss, products, and current-time reused
contractions along the actual reachable graph.

**Result:** pass.

## 8. Final quantifier audit

- The width limit is treated as already established at each fixed \(h\);
  no finite-width Taylor expansion or reversal of limits appears here.
- The factorization is exact for every finite \(t\) under its stated
  pathwise regularity.
- The Taylor implication is uniform only if the explicitly displayed
  \(A_{j,t}'''\) premise holds.
- The document constructs no \(\alpha_0,\rho,C\) for the desired scalar
  theorem and does not claim otherwise.
- The no-go is independent of \(t\) and already occurs at \(L=2\).
- No \(L=3\) extension is claimed.

Accordingly, the final three-way status in (6.1) is accurate:

\[
\boxed{
\begin{array}{c}
\text{paired factorization and conditional }t^4\text{ reduction: proved},\\
\text{full same-space product-closed norm: impossible},\\
\text{uniform scalar remainder theorem: open}.
\end{array}}
\]
