# Resolution of the uniform near-identity (L=2) request

Date: 25 August 2026.

## 1. Final claim status

The exact paired-step cancellation and its \(t^4\) reduction are valid.  With

\[
 \Delta_t(h):=F_{2t}(h)-F_t(2h),
\]

one has

\[
 \Delta_t(h)=h^2\sum_{j=1}^t A_{j,t}(h),
 \tag{1.1}
\]

and

\[
 \sup_{j\le t,\ |u|\le \rho/t}|A_{j,t}'''(u)|\le C_A t^3
 \quad\Longrightarrow\quad
 |\Delta_t(h)-\kappa_t h^3|
 \le {C_A\over6}t^4|h|^5,
 \qquad |h|\le\rho/t.
 \tag{1.2}
\]

However, the single-space all-source norm required in the question cannot
exist with the stipulated quantitative product closure.  This is a theorem,
not a missing estimate.  The contradiction occurs in source order zero and
therefore cannot be repaired by changing higher-order weights, moment
exponents, or the aggregation over source histories.

Consequently the literal checklist in the question is inconsistent.  No
activation-only constants \(\alpha_0,\rho,C\) for the scalar remainder have
been obtained from it, and the scalar remainder assertion itself remains
open.  A grammar-restricted radius-loss scale is not ruled out, but it is a
different theorem from the requested same-space construction.

## 2. Exact paired-step factorization

Work on the already established width-first population state.  Write its
recomputed Euler update and observable as

\[
 E_hx=x+h g(x),\qquad F_N(h)=\mathcal O(E_h^N\theta_0),
 \tag{2.1}
\]

and put

\[
 B_h=E_h\circ E_h,\qquad C_h=E_{2h}.
 \tag{2.2}
\]

Assume that \(s\mapsto g(x+shg(x))\) and every interpolation
\(\lambda\mapsto(\mathcal O\circ C_h^m)(c+\lambda d)\) used below are
absolutely continuous, with the displayed directional derivatives as their
almost-everywhere derivatives.  Then

\[
 \begin{aligned}
 B_hx-C_hx
 &=h\{g(x+h g(x))-g(x)\}\\
 &=h^2a_h(x),
 \end{aligned}
 \tag{2.3}
\]

where

\[
 a_h(x)=\int_0^1Dg(x+s h g(x))[g(x)]\,ds.
 \tag{2.4}
\]

For \(1\le j\le t\), set

\[
 y_j=B_h^{j-1}\theta_0,\qquad m_j=t-j,
 \tag{2.5}
\]

\[
 c_j=C_hy_j,\qquad b_j=B_hy_j=c_j+h^2a_h(y_j),
 \tag{2.6}
\]

and

\[
 A_{j,t}(h)=\int_0^1
 D(\mathcal O\circ C_h^{m_j})
 \bigl(c_j+\lambda h^2a_h(y_j)\bigr)[a_h(y_j)]\,d\lambda.
 \tag{2.7}
\]

Define the noncommutative hybrids

\[
 H_j=\mathcal O(C_h^{t-j}B_h^j\theta_0),
 \qquad 0\le j\le t.
 \tag{2.8}
\]

Then \(H_0=F_t(2h)\), \(H_t=F_{2t}(h)\), and, without commuting
\(B_h\) and \(C_h\),

\[
 \begin{aligned}
 H_j-H_{j-1}
 &=(\mathcal O\circ C_h^{m_j})(b_j)
   -(\mathcal O\circ C_h^{m_j})(c_j)\\
 &=h^2A_{j,t}(h).
 \end{aligned}
 \tag{2.9}
\]

Summing (2.9) proves (1.1) before any absolute value is taken.

The propagated form is also exact.  For \(0\le\lambda\le1\), let

\[
 z_{j,0}=c_j+\lambda h^2a_h(y_j),\qquad
 v_{j,0}=a_h(y_j),
 \tag{2.10}
\]

and recurse

\[
 z_{j,r+1}=z_{j,r}+2h g(z_{j,r}),
 \tag{2.11}
\]

\[
 v_{j,r+1}=(I+2hDg(z_{j,r}))v_{j,r},
 \qquad 0\le r<m_j.
 \tag{2.12}
\]

Then

\[
 A_{j,t}(h)=\int_0^1
 D\mathcal O(z_{j,m_j})[v_{j,m_j}]\,d\lambda.
 \tag{2.13}
\]

## 3. Cubic coefficient and the exact Taylor reduction

Let

\[
 S_t(h)=\sum_{j=1}^tA_{j,t}(h).
 \tag{3.1}
\]

The established Gaussian sign involution gives
\(F_N(-h)=-F_N(h)\).  Hence \(\Delta_t\) is odd.  If each
\(A_{j,t}\in C^3[-\rho/t,\rho/t]\) (which requires the corresponding
regularity of \(g\) and \(\mathcal O\) along every generated path), then
(1.1) makes \(S_t\) odd, so

\[
 S_t(0)=S_t''(0)=0,
 \qquad
 \kappa_t=S_t'(0).
 \tag{3.2}
\]

Taylor's integral identity gives, for either sign of \(h\),

\[
 S_t(h)-\kappa_t h
 ={1\over2}\int_0^h(h-u)^2S_t'''(u)\,du.
 \tag{3.3}
\]

Combining (1.1) and (3.3),

\[
 |\Delta_t(h)-\kappa_t h^3|
 \le {|h|^5\over6}
 \sup_{|u|\le|h|}|S_t'''(u)|.
 \tag{3.4}
\]

Thus the factor \(t^4\) in (1.2) has exactly one factor \(t\) from the
hybrid sum and three from differentiating one transported local defect.

For the present fine-minus-coarse convention, the already established
width-first cubic computation gives

\[
 \boxed{\displaystyle
 \kappa_t={t(2t-1)\over2}J_{\psi_\alpha,2}.}
 \tag{3.5}
\]

This coefficient is an explicit activation integral.  For completeness,
set \(\psi=\psi_\alpha\) and write, at \(G\sim N(0,1)\),

\[
 g=\psi(G),\quad p=\psi'(G),\quad q=\psi''(G),
 \quad r_3=\psi'''(G),
 \tag{3.6}
\]

and define

\[
 \begin{array}{lll}
 d=\mathbb E p^2,&u=\mathbb E p^4,&v=\mathbb E[gq],\\
 m=\mathbb E[gp^2q],&r=\mathbb E[pr_3],&s=\mathbb E q^2,\\
 j=\mathbb E[p^3r_3],&e=\mathbb E[p^2q^2],
 &\ell=\mathbb E[g^2p^2].
 \end{array}
 \tag{3.7}
\]

Put

\[
 c=1+d,\qquad \beta=v+cr,\qquad
 \delta=d+cs,\qquad k=d+\beta+\delta.
 \tag{3.8}
\]

Then

\[
 \mathsf S_{\psi,2}
 =3c^2m+3c^3j+3du\beta+3dkm+3d^2j,
 \tag{3.9}
\]

\[
 \begin{aligned}
 \mathsf H_{\psi,2}={}&c^2u+c\ell+2c^2m+3c^3e+cuds
 +2ud^2+3d^2e\\
 &+k^2\ell+2dkm,
 \end{aligned}
 \tag{3.10}
\]

and

\[
 J_{\psi,2}=\mathsf S_{\psi,2}+4\mathsf H_{\psi,2}.
 \tag{3.11}
\]

No output derivative or trained trajectory occurs in (3.6)--(3.11).

## 4. No-go theorem for the demanded norm

### Theorem 4.1

Let \(w_m\ge0\), let \(p_m\in[1,\infty]\), and suppose

\[
 \|V\|_{\mathfrak X}
 =\sum_{m\ge0}w_m\|\mathcal D^mV\|_{p_m}
 \tag{4.1}
\]

is a norm containing constants and a Gaussian-like unbounded OMFP atom
\(X\).  Suppose also that multiplication is quantitatively closed on the
same space:

\[
 \|UV\|_{\mathfrak X}
 \le C_\times\|U\|_{\mathfrak X}\|V\|_{\mathfrak X}.
 \tag{4.2}
\]

If

\[
 \|X\|_q\ge c_X\sqrt q
 \quad\text{for all sufficiently large }q,
 \tag{4.3}
\]

then (4.1)--(4.2) are impossible.

#### Proof

Constants have no positive-order source derivatives, so \(w_0>0\); if
\(w_0=0\), (4.1) assigns norm zero to \(1\).  If \(p_0=\infty\), the
unbounded atom \(X\) has infinite norm.  Hence \(p_0<\infty\).

Iterating (4.2),

\[
 \|X^n\|_{\mathfrak X}
 \le C_\times^{n-1}\|X\|_{\mathfrak X}^n.
 \tag{4.4}
\]

The source-order-zero term gives

\[
 \|X^n\|_{\mathfrak X}
 \ge w_0\|X^n\|_{p_0}
 =w_0\|X\|_{np_0}^{n}.
 \tag{4.5}
\]

Taking \(n\)-th roots in (4.4)--(4.5) and using (4.3) yields

\[
 w_0^{1/n}c_X\sqrt{np_0}
 \le C_\times^{1-1/n}\|X\|_{\mathfrak X},
 \tag{4.6}
\]

whose left side diverges and whose right side is bounded.  This is a
contradiction. \(\square\)

The theorem applies directly with a raw standard Gaussian source.  It also
applies to the actual activated initialization atom.  Assume the displayed
activation envelope includes \(r=0\), so \(\|\varphi\|_\infty\le M\), and
put

\[
 X_\alpha=\psi_\alpha(G),\qquad
 s_\alpha=\|G+\alpha\varphi(G)\|_2.
 \tag{4.7}
\]

For \(|\alpha|M\le1/2\), \(s_\alpha\in[1/2,3/2]\), and, for every
\(q\ge1\),

\[
 \|X_\alpha\|_q
 \ge {\|G\|_q-|\alpha|M\over1+|\alpha|M}.
 \tag{4.8}
\]

Since \(\|G\|_q\ge c_G\sqrt q\), (4.3) follows for all sufficiently
large \(q\).  Thus the contradiction holds for every fixed nonzero
\(|\alpha|\le(2M)^{-1}\), as well as for \(\alpha=0\).

Theorem 4.1 uses only the \(m=0\) term.  Therefore none of the following
can alter it: changing \(w_m\) or \(p_m\) for \(m\ge1\), changing the
tensor norm, quotienting singular Gaussian directions, or changing the
aggregation over source histories.

If product closure is weakened to joint continuity, bilinearity and local
boundedness recover an inequality of the form (4.2) by rescaling.  Mere
algebraic membership without a quantitative estimate cannot produce the
explicit one-step constants requested in the question.

### The coefficientwise adjoint/product conflict

There is an independent obstruction on the unrestricted positive
source-majorant completion.  All its weights are necessarily positive;
otherwise the majorant is not a norm on jets supported at a zero-weight
order.  For ordinary derivatives, boundedness of the
adjoint shift \((Su)_m=u_{m+1}\) forces

\[
 w_{m-1}\le C_Jw_m.
 \tag{4.9}
\]

Coefficientwise Leibniz closure, tested on jets supported at orders \(1\)
and \(m-1\), forces

\[
 m w_m\le C_Pw_1w_{m-1}.
 \tag{4.10}
\]

Together they imply \(m\le C_PC_Jw_1\) for every \(m\), which is
impossible.  With normalized derivatives, the binomial factor disappears
from (4.10) and the factor \(m+1\) appears in the shift instead, giving the
same contradiction.

This second argument is intentionally narrower than Theorem 4.1: a
grammar-specific cancellation can avoid coefficientwise positive
majorization.  No such qualification is needed for the full same-space
product no-go in Theorem 4.1.

## 5. The radius-loss replacement and why it is not yet the theorem

Let \(\mathcal H\) be the intrinsic Cameron--Martin direct sum of all
exposed source blocks, quotienting covariance-null directions before taking
norms.  With the symmetric projective tensor aggregation, define

\[
 \|V\|_{\rho,p}
 =\sum_{m\ge0}{\rho^m\over m!}
 \|\mathcal D^mV\|_{L^p(\Omega;
 \mathcal H^{\widehat\otimes_\pi m})}.
 \tag{5.1}
\]

Here \(\mathcal D^m\) is the ordinary, unnormalized \(m\)-th Malliavin
derivative.  This is a scale in \((\rho,p)\), not one same-space Banach
algebra.  For
conditional expectation onto a Gaussian source subspace, Malliavin
derivatives are orthogonally projected onto the retained
Cameron--Martin directions.  Direct Leibniz, Hölder, and Jensen estimates
then give

\[
 \|UV\|_{\rho,p}
 \le\|U\|_{\rho,2p}\|V\|_{\rho,2p},
 \tag{5.2}
\]

\[
 \|\mathbb E_{\mathcal B}V\|_{\rho,p}
 \le\|V\|_{\rho,p},
 \tag{5.3}
\]

and the same estimate as (5.2) for learned projective rank-one products.

For the exact reused-adjoint identity

\[
 J^*V=\mathbb E[D_JV],
 \tag{5.4}
\]

the positive source majorant is the left shift \((Sa)_m=a_{m+1}\).  If
\(0<\rho'<\rho\), then, for every \(k\ge1\),

\[
 \|S^kV\|_{\rho',p}
 \le {k!\rho\over(\rho-\rho')^{k+1}}
 \|V\|_{\rho,p}.
 \tag{5.5}
\]

Indeed, for \(n=m+k\), the ratio of the left coefficient to the right
coefficient is

\[
 \rho^{-k}{n!\over(n-k)!}
 \left({\rho'\over\rho}\right)^{n-k},
 \tag{5.6}
\]

and summing its nonnegative majorant gives

\[
 \sum_{m\ge0}{(m+k)!\over m!}x^m
 ={k!\over(1-x)^{k+1}}.
 \tag{5.7}
\]

At equal radii the unrestricted positive-majorant shift is unbounded.

Chronological step weights obey

\[
 \sum_{i_1<\cdots<i_k}\prod_{r=1}^k|e_{i_r}|
 \le {\tau^k\over k!},
 \qquad \tau=\sum_i|e_i|.
 \tag{5.8}
\]

Thus the simplex factor can cancel the \(k!\) in (5.5), but only after a
strict radius loss.  What is still unproved for the actual OMFP graph is a
composite, reachable theorem showing that all interspersed products and
current-time contractions consume only a total radius proportional to
\(t|h|\), while the moment scale remains controlled.  That graph theorem is
not implied by (5.2)--(5.8).

## 6. Adversarial audit and quantifiers

The proof was independently reconstructed with the following verdict.

1. The order and sign in the noncommutative hybrid telescope pass.
2. The Taylor factor \(1/6\) and the implication (1.2) pass, conditional on
   the stated \(C^3\) generated-curve regularity.
3. The Gaussian-power contradiction passes for both a raw Gaussian and the
   normalized atom \(\psi_\alpha(G)\).
4. The contradiction covers every finite \(p_0\); \(p_0=\infty\) excludes
   the initialization atom, and \(w_0=0\) destroys definiteness of the norm.
5. Higher source weights, moment exponents, and singular-history
   aggregation cannot affect a contradiction located at \(m=0\).
6. The coefficientwise shift/Leibniz theorem is not promoted to a theorem
   about every grammar-restricted reachable module.
7. No claim is made that Theorem 4.1 disproves the scalar remainder bound.
   It disproves the exact single-space proof architecture demanded in the
   question.
8. Since the missing composite radius-loss theorem is unproved already for
   \(L=2\), no \(L=3\) extension is asserted.

The clean claim-level conclusion is therefore

\[
 \boxed{
 \begin{array}{c}
 \text{exact paired factorization and }t^4\text{ reduction: proved},\\
 \text{requested one-norm all-source closure: impossible},\\
 \text{uniform scalar near-identity remainder theorem: open}.
 \end{array}}
 \tag{6.1}
\]
