# Network-specific constraints on the terminal arctangent gate

This note tests several possible strengthenings of the bare bound
\(|f_m|\le1\) for the terminal multiplier

\[
 f_m=d(Z_3^m),\qquad d(z)=(1+z^2)^{-1}.
\]

## 1. Two exact mesh-uniform constraints

The first true constraint is a componentwise cancellation budget for the
learned top-layer field.  From the exact updates,

\[
 A_i^k=A_i^0+h\sum_{s<k}X_{3,i}^s,qquad
 P_2^k=h\sum_{s<k}B_3^s\otimes X_2^s.
\]

Because arctangent and all normalized feature inner products are bounded,

\[
 |A_i^k|\le |A_i^0|+C T,                            \tag{1}
\]

and

\[
\begin{aligned}
 |(P_2^kX_2^k)_i|
 &=\left|h\sum_{s<k}B_{3,i}^s
        \langle X_2^s,X_2^k\rangle\right|\\
 &\le C h\sum_{s<k}|A_i^s|
 \le C_T(1+|A_i^0|).                               \tag{2}
\end{aligned}
\]

Thus the trained field can cancel a large Ginibre row field only by paying one
Gaussian endpoint mark.  Neither a predictor norm nor a mesh-dependent
constant occurs in (2).

The second exact constraint is the scalar gate inequality

\[
 |x|d(x+y)le \frac12+|y|.                          \tag{3}
\]

Indeed \(|x|\le|x+y|+|y|\),
\(|x+y|/(1+|x+y|^2)\le1/2\), and \(d\le1\).  Applied
to a canonical Gaussian row carrier in \(\Gamma_2X_2^k\), (3) says that the
carrier is either suppressed by \(d(Z_3^k)\), or is canceled by the remaining
Gaussian field plus (2).  The latter alternative exposes at most one other
Gaussian carrier or one endpoint mark.  This is the pointwise form of the
two-carrier audit.

For the *last* fresh forward innovation there is also an exact variation
bound.  Conditional on the chronological past,

\[
 Z_3^k=c+\alpha g,
\]

so, as a function of the scalar fresh coordinate,

\[
 \operatorname{TV}_{g\in\mathbb R}d(c+\alpha g)\le2.          \tag{4}
\]

This follows because an affine function is monotone and \(d\) rises from zero
to one and falls back to zero.  It is independent of \(c,\alpha,h\).

Equations (2)--(4) are genuine network-specific improvements over an arbitrary
bounded terminal multiplier.

## 2. Exact newest-innovation Orlicz estimates

Let \(G\sim N(0,1)\), condition on the chronological past, and put
\(\Delta d=d(c+\alpha G)-d(c)\).  Then

\[
 \|G\Delta d\|_{L^q}
 \le C\min\{ |\alpha|q,\sqrt q\},\qquad q\ge2.       \tag{5}
\]

The first bound uses \(|\Delta d|\le C|\alpha G|\) and
\(\|G^2\|_q\le Cq\); the second uses \(|\Delta d|\le1\) and
\(\|G\|_q\le C\sqrt q\).  If the endpoint mark is integrated as well, then

\[
 \|A^kG\Delta d\|_{L^q}
 \le C_T\min\{|\alpha|q^{3/2},q\}.                  \tag{6}

Although (6) has uniform \(\psi_1\) size, it does not have \(O(\alpha)\)
\(\psi_1\) size.  At moments \(q\asymp\alpha^{-2}\), the rare transition
region of the gate makes the right side order \(q\).  This explains why
triangular summation of the local \(\psi_1\) norms is not mesh-uniform.

There is nevertheless a small-variance Bernstein estimate before multiplying
all local norms.  From (5), for every integer \(p\ge2\),

\[
 \mathbf E|G\Delta d|^p\le p!\,C^p\alpha^2.         \tag{7}

To check (7), if \(|\alpha|\sqrt p\le1\), use the first bound in (5): after
raising to the \(p\)-th power, factor out \(\alpha^2p^p\) and absorb
\((|\alpha|\sqrt p)^{p-2}p\) into \(C^pp! /p^p\).  If
\(|\alpha|\sqrt p>1\), use the second bound and
\(\alpha^2p>1\).  Stirling's lower bound
\(p!\ge(p/e)^p\) absorbs the remaining polynomial factor.  Thus a sum of
*centered newest-query* atoms has variance budget \(\sum\alpha_k^2\) and a
fixed Bernstein scale.  The endpoint mark and old-carrier reuse prevent this
fact alone from proving the desired global estimate.

## 3. Candidate properties that fail

### 3.1 Pathwise monotonicity or bounded variation through all Euler steps

Only (4), the last-query statement, is true without qualification.  Even the
scalar top self-update contains

\[
 F_a(z)=z+h\kappa a d(z),qquad
 F_a'(z)=1+h\kappa a d'(z).                         \tag{8}

When \(h\kappa|a|>\|d'\|_\infty^{-1}\), (8) changes sign and the Euler map
folds.  Iterating such maps can increase the number of monotonicity intervals
at every step.  This is reachable in the network on an open set: saturate the
lower layer so that \(X_2\) is nearly constant, take a scalar top row, and use
the full support of the Gaussian endpoint to make \(|A^0|\gtrsim h^{-1}\).
Therefore neither monotonicity in an old fresh innovation nor a deterministic
mesh-uniform total-variation bound can be used for the exact Euler scheme.
The event is very rare, but pathwise BV does not see that rarity.

### 3.2 An energy-controlled Malliavin contraction

After scalar characteristic dressing, the exact lower-layer response contains

\[
 \sum_{\ell\ne i}K_{i\ell}\frac{d_\ell}{d_i}R_{2,\ell}
 (d_\ell'\eta_\ell-d_i'\eta_i).                    \tag{9}

The two-dimensional near-null construction in
`signed_predictor_abel_note.md` makes (9) arbitrarily large while the base
Euler velocity and output energy remain bounded.  Hence no pathwise
Malliavin-contraction estimate follows from energy.

### 3.3 A deterministic Carleson bound for all canonical residuals

If \(\alpha_k\) is the norm of the new feature residual, bounded feature
states give only

\[
 \sum_k\alpha_k^2\le Cn,                            \tag{10}

because at most \(n\) mutually orthogonal residual directions can occur and
each has bounded norm.  There is no deterministic \(C_T\) independent of the
width: a sequence of bounded orthogonal feature states attains the order in
(10), and the full support of the finite-mesh Gaussian dynamics allows
arbitrarily close finite approximations (at a correspondingly rare cost).
Thus a mesh-uniform Carleson bound would have to be annealed and use the actual
time increments; it is not a geometric consequence of canonicalization.

## 4. Why the true constraints do not yet prove the global bound

For the latest fresh carrier, (2)--(7) give the correct two-carrier
\(Cq\) estimate.  For an old carrier, however, the terminal feature
coefficient and the learned field have already adapted to that carrier.  The
last-query affine representation used in (4) is then lost.  Equation (2)
still limits learned cancellation, and (3) still prevents an exposed carrier
from surviving a gate without another carrier paying for the cancellation,
but the "remaining Gaussian field" in (3) is an anticipating canonical sum.
Controlling all such cancellations simultaneously is exactly the signed
two-carrier decoupling problem.

Thus the first true mesh-uniform structural property is the componentwise
learned-field budget (2), supplemented by the gate inequality (3) and the
one-query BV bound (4).  They prove that no local degree-three carrier can
arise and give the sharp newest-innovation estimates (5)--(7).  They do not,
without an additional causal row-decoupling argument, rule out rare global
alignment of an old canonical carrier with the terminal gates.

