# Hostile audit of the probabilistic bridge

**Date:** 2026-08-18  
**Scope:** the exact (L=2,B=1) initialization observable (C_n=D_n^3f_n)  
**Primary object audited:** `PEELING_AND_PROBABILITY_LEDGER.md`

## 1. Verdict

The fixed-width observable is an exact, finite
NETSOR\({}^\top+\) scalar program.  Under the explicit assumption

\[
\phi,\phi',\phi'',\phi'''\quad\text{are pseudo-Lipschitz},
\tag{1.1}
\]

Theorem E.15 of Yang's
[*Tensor Programs III: Neural Matrix Laws*](https://arxiv.org/pdf/2009.10685)
does certify all of the following:

1. the complete joint symbolic law of the forward, backward, and tangent
   channels;
2. every nonzero transpose/Onsager response and every zero response listed in
   the peeling ledger;
3. deterministic replacement of every empirical `Moment` scalar;
4. almost-sure convergence
   \[
   C_n\longrightarrow C_{\rm GNF},
   \tag{1.2}
   \]
   including singular-covariance and exactly degenerate activations.

There is consequently no remaining joint-CLT, equality-sector, covariance-
replacement, or typical-limit gap for this fixed program under (1.1).  A
separate multi-copy argument would be needed for a quantitative variance rate
or a different observable not represented by one program scalar, but not for
the deterministic almost-sure limit (1.2).

The annealed conclusion has three different scopes.  A later master theorem
is decisive for the smoothest one.

- If \(\phi\) is **polynomially smooth** in the sense that it is
  \(C^\infty\) and every derivative of every order is polynomially bounded,
  Theorem 3.7 of Golikov--Yang,
  [*Non-Gaussian Tensor Programs*](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf),
  applies to the same exact scalar program and gives
  \[
  C_n\longrightarrow C_{\rm GNF}
  \quad\text{almost surely and in }L^p
  \quad\text{for every }1\le p<\infty.
  \tag{1.3}
  \]
  This covers unbounded polynomial activations as well as bounded activations
  whose derivatives of every order obey the stated polynomial envelope.  It
  closes the annealed bridge without a separate UI assumption under this
  all-orders regularity envelope.

- If \(\phi,\phi',\phi'',\phi'''\) are bounded in addition to (1.1), a direct
  normalized-moment argument below proves
  \[
  \sup_n\mathbb E|C_n|^p<\infty
  \quad\text{for every fixed }p<\infty.
  \tag{1.4}
  \]
  Hence \(C_n\to C_{\rm GNF}\) in \(L^1\) and
  \(\mathbb EC_n\to C_{\rm GNF}\).  The bounded-activation bridge is closed.

- If only the four functions through \(\phi'''\) satisfy (1.1) and have
  polynomial growth, but the all-orders polynomial-smoothness hypothesis is
  unavailable, Theorem E.15 gives (1.2), not convergence of expectations.
  Tensor Programs III leaves even the underlying NETSOR\({}^\top\)
  polynomial-growth convergence-in-mean extension as Conjecture A.4; it does
  not provide uniform integrability for this more general scalar-feedback
  program.  Thus the original annealed polynomial-growth contract still needs
  either
  \[
  \sup_n\mathbb E|C_n|^{1+\epsilon}<\infty
  \tag{1.5}
  \]
  for some \(\epsilon>0\), or a proved activation-specific substitute.

The current peeling ledger's exact program, response registry, and Theorem
3.7 uniform-integrability bridge pass this audit.  An earlier draft's
coefficient-tensor justification of uniform integrability was not
sufficiently detailed: a naive Hilbert--Schmidt induction through
coordinatewise products can introduce a hidden factor of \(n\).  The current
ledger no longer relies on that argument.  Section 6 below records an
independent bounded-envelope proof that also avoids this issue.

## 2. Exact program audit

Put \(A=W/\sqrt n\), let

\[
x_r=\phi^{(r)}(u),\qquad z=Ax_0,\qquad
y_r=\phi^{(r)}(z),\qquad b=a\odot y_1,\qquad r=A^\top b,
\tag{2.1}
\]

and write \(M_n(v)=n^{-1}\sum_i v_i\).  Direct substitution into the finite
directional derivatives gives

\[
\zeta=Q_nb+qA(x_1^2r),
\qquad Q_n=M_n(x_0^2),
\tag{2.2}
\]

\[
\sigma=2qc_nb+q^2A(x_2x_1^2r^2),
\qquad c_n=M_n(x_0x_1^2r),
\tag{2.3}
\]

\[
\tau=3q^2m_nb+q^3A(x_3x_1^3r^3),
\qquad m_n=M_n(x_0x_2x_1^2r^2),
\tag{2.4}
\]

and, with

\[
B=y_0y_1+a y_2\zeta,
\qquad D_n^{\rm b}=M_n(b^2),
\tag{2.5}
\]

\[
\dot r=D_n^{\rm b}x_0+A^\top B.
\tag{2.6}
\]

All products here and below are coordinatewise.  Equations (2.2)--(2.6)
agree exactly with equations (3.2)--(3.5) of the peeling ledger.

The straight third derivative is

\[
\mathcal T_n=M_n\!\left[
a(y_3\zeta^3+3y_2\zeta\sigma+y_1\tau)
+3y_0(y_2\zeta^2+y_1\sigma)
\right].
\tag{2.7}
\]

For the middle-weight acceleration, the entry before its factor
\(n^{-1/2}\) is

\[
x_{0,j}B_i+q b_i x_{1,j}^2r_j.
\]

Therefore its normalized squared Frobenius norm factorizes exactly as

\[
\begin{aligned}
\mathcal H_{W,n}={}&Q_nM_n(B^2)
+q^2M_n(b^2)M_n(x_1^4r^2)\\
&+2qM_n(bB)M_n(x_0x_1^2r).
\end{aligned}
\tag{2.8}
\]

The other two blocks are

\[
\mathcal H_{a,n}=M_n[(y_1\zeta)^2],
\tag{2.9}
\]

\[
\mathcal H_{u,n}
=qM_n[(qx_2x_1r^2+x_1\dot r)^2].
\tag{2.10}
\]

Thus

\[
C_n=2\mathcal T_n
+4(\mathcal H_{a,n}+\mathcal H_{W,n}+\mathcal H_{u,n})
\tag{2.11}
\]

is an exact identity, not an asymptotic representation.  Every operation in
(2.1)--(2.11) is `MatMul`, `Nonlin+`, `Moment`, or continuous scalar
arithmetic.  The program length is independent of \(n\).  I found no missing
metric factor, product-rule term, or unfactorized matrix observable in the
ledger's equations (3.1)--(3.10).

## 3. The theorem hypotheses, precisely

The relevant result is Tensor Programs III, Theorem E.15, rather than a
forward-only Gaussian-process theorem.  Its setup permits an iid Gaussian
matrix with variance \(1/n\), iid jointly Gaussian initial-coordinate
slices, both orientations of the same matrix, `Moment` scalars, and
scalar-parametric coordinate maps.  It concludes almost-sure convergence of
pseudo-Lipschitz empirical tests and of every generated scalar, without rank
stability.

The hypothesis map is exact:

| Theorem requirement | Present program |
|---|---|
| Gaussian matrix, variance \(1/n\) | \(A=W/\sqrt n\) |
| iid Gaussian initial slices | \((u_i,a_i)\sim N(0,\operatorname{diag}(q,1))\) |
| finitely many lines | (2.1)--(2.11) |
| arbitrary reuse of both orientations | \(A,A^\top,A,A,A^\top\) |
| `Moment` and scalar parameters | \(Q_n,D_n^{\rm b},c_n,m_n\) and the final contractions |
| pseudo-Lipschitz maps | follows from (1.1), since finite sums, products, and compositions remain pseudo-Lipschitz of finite degree |

A useful sufficient regularity statement is

\[
\phi\in C^3,\qquad
\phi^{(r)}\text{ pseudo-Lipschitz for }0\le r\le3.
\tag{3.1}
\]

Alternatively, \(\phi\in C^4\) with polynomially bounded derivatives through
order four implies (3.1) by the mean-value theorem.  Merely saying
"\(C^3\), and \(\phi,\ldots,\phi'''\) have polynomial growth" is not enough
to invoke Theorem E.15: polynomial growth of \(\phi'''\) does not make
\(\phi'''\) pseudo-Lipschitz.  Likewise, bounded \(C^3\) derivatives make
\(\phi,\phi',\phi''\) globally Lipschitz but do not by themselves make the
continuous function \(\phi'''\) pseudo-Lipschitz.  One must either assume it
directly, add a fourth-derivative envelope, or supply a mollification and
stability extension.

The rank-stable Theorem E.5 can trade pseudo-Lipschitz tests for more general
polynomially bounded tests, but it is not a shortcut here: this is a
NETSOR\({}^\top+\) program with scalar parameters, and rank stability would
have to be checked for every family of inputs to \(A\) and \(A^\top\).
Constant, linear, affine, and other special activations make several limiting
Gram matrices singular.  Theorem E.15 is therefore the correct robust route.

### 3.1 The all-orders \(L^p\) theorem

Theorem 3.7 of
[*Non-Gaussian Tensor Programs*](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf)
does more than extend initialization universality.  Its Definition 3.1 permits

- each matrix instruction to use \(A_j\) or \(A_j^\top\);
- arbitrary repeated use of the same orientation or the transpose;
- a coordinate function depending on every earlier vector and scalar; and
- a scalar \(c_i=n^{-1}\sum_\alpha x^i_\alpha\) at each line.

The paper explicitly states that this language is equivalent to
NETSOR\({}^\top+\).  Consequently, empirical `Moment` values, their reuse as
`Nonlin+` parameters, products of earlier scalars, and the final value
\(C_n\) in (2.11) are all literal instances of its scalar type; there is no
language mismatch.

Its Setup 3.6 requires independent matrix entries of mean zero, variance
\(1/n\), and scaled moments
\(\mathbb E|A_{ij}|^k\le\nu_kn^{-k/2}\) for every \(k\), Gaussian initial
vectors, initial scalars with all moments, and polynomially smooth program
nonlinearities.  The present initialization satisfies these assumptions:

| Setup 3.6 object | Present object |
|---|---|
| matrix moment condition | \(A_{ij}\sim N(0,1/n)\), with \(\nu_k=\mathbb E|N(0,1)|^k\) |
| standard Gaussian vectors | \(a\), and a standard \(g\) with \(u=\sqrt q\,g\) produced coordinatewise |
| initial scalars with all moments | deterministic \(q\) and constants |
| polynomially smooth nonlinearities | all sums/products/compositions in (2.1)--(2.11), provided \(\phi\) is polynomially smooth |

If \(\phi\) is polynomially smooth, then every \(\phi^{(r)}\), including the
four functions actually appearing in the program, is polynomially smooth;
finite arithmetic and composition preserve the property.  Theorem 3.7 then
states that **every scalar in the program converges almost surely and in
\(L^p\) for every finite \(p\)** to the same recurrent Gaussian limit as the
Gaussian master theorem.  Applied to (2.11), this is exactly (1.3).

Thus there is no mismatch involving Gaussian versus non-Gaussian matrices:
Gaussian matrices are a special case of Setup 3.6.  There is also no
forward-only or no-transpose restriction; that restriction occurs only in a
later neural-network corollary, not in Definition 3.1 or Theorem 3.7.

The genuine limitation is regularity.  The theorem requires derivatives of
the program nonlinearities of **all orders** to be polynomially bounded.  It
does not turn a merely \(C^3\) activation with polynomial growth through
\(\phi'''\) into an \(L^p\) theorem.  Gaussian smoothing mentioned in that
paper produces an approximating polynomially smooth program, not equality
with the original activation; removing the smoothing still needs a stability
argument.

## 4. Rank and covariance degeneracies

The no-rank-stability version of the theorem covers degenerate Gaussian laws.
In particular:

- a constant activation makes all tangent channels exactly zero;
- a linear or affine activation creates exact linear dependencies among
  several program vectors;
- special activations may make a fresh variance or a displayed covariance
  matrix singular;
- \(Q=\mathbb E\phi(U)^2\) may vanish, in which case the outer Gaussian is
  degenerate at zero.

None of these cases invalidates (1.2).  The additional condition \(A_{\rm
NTK}>0\) is needed only to define \(\mu_0=C/(2A_{\rm NTK}^2)\), not to define
or prove the limit of \(C_n\).

## 5. Independent response/equality audit

Let \(U\sim N(0,q)\), \(Z\sim N(0,Q)\), \(A_0\sim N(0,1)\), and
\(R\sim N(0,D)\), where

\[
Q=\mathbb E\phi(U)^2,\qquad
D=\mathbb E\phi'(Z)^2,\qquad
d=\mathbb E\phi'(U)^2.
\]

The ZDot rule says that a new use of \(A\) or \(A^\top\) consists of a fresh
joint Gaussian channel plus a response in the span of all earlier inputs in
the opposite orientation.  Applying that rule to the exact program gives the
following exhaustive registry.

| New multiplication | Opposite-orientation direction | Coefficient |
|---|---|---:|
| \(A^\top(a y_1)\) | \(x_0\) | \(\mathbb E[A_0\phi''(Z)]=0\) |
| \(A(x_1^2r)\) | \(b=a y_1\) | \(\mathbb E\phi'(U)^2=d\) |
| \(A(x_2x_1^2r^2)\) | \(b\) | \(2\mathbb E[\phi''(U)\phi'(U)^2R]=0\) |
| \(A(x_3x_1^3r^3)\) | \(b\) | \(3D\mathbb E[\phi'''(U)\phi'(U)^3]\) |
| \(A^\top B\) | \(x_0\) | \(S_0+\alpha S_1\) |
| \(A^\top B\) | \(x_1^2r\) | \(q\mathbb E[A_0\phi''(Z)]=0\) |
| \(A^\top B\) | second/third tangent inputs | \(0\), since \(B\) does not depend on their fresh channels |

Here

\[
\alpha=Q+qd,
\]

\[
S_0=\mathbb E[\phi'(Z)^2+\phi(Z)\phi''(Z)],
\qquad
S_1=\mathbb E[\phi''(Z)^2+\phi'(Z)\phi'''(Z)].
\]

The corresponding symbolic fields are

\[
r\Rightarrow R\sim N(0,D),
\tag{5.1}
\]

\[
A(x_1^2r)\Rightarrow dA_0\phi'(Z)+\Gamma,
\qquad \Gamma\sim N(0,r_4D),
\tag{5.2}
\]

\[
\zeta\Rightarrow \alpha A_0\phi'(Z)+q\Gamma,
\tag{5.3}
\]

\[
c_n\to0,\qquad m_n\to Dm,
\tag{5.4}
\]

where

\[
r_4=\mathbb E\phi'(U)^4,\qquad
m=\mathbb E[\phi(U)\phi''(U)\phi'(U)^2].
\]

The fresh second-tangent channel \(\Omega\) satisfies

\[
\operatorname{Cov}(Z,\Omega)=Dm,\qquad
\operatorname{Cov}(\Gamma,\Omega)=0.
\tag{5.5}
\]

For the third tangent, the fresh channel \(\Lambda\) can have the nonzero
covariance

\[
\operatorname{Cov}(\Lambda,\Gamma)
=3D^2\mathbb E[\phi'''(U)\phi'(U)^5].
\tag{5.6}
\]

The peeling ledger correctly retains this covariance until the full readout
contraction; it disappears there by the single centered readout factor, not
by an invalid independence assertion.

Finally, with

\[
\mathsf B=\phi(Z)\phi'(Z)
+A_0\phi''(Z)(\alpha A_0\phi'(Z)+q\Gamma),
\]

the line \(A^\top B\) has fresh variance
\(\beta=\mathbb E\mathsf B^2\), nested response
\(S_0+\alpha S_1\), and zero fresh covariance with the earlier backward
channel because

\[
\mathbb E[A_0\phi'(Z)\mathsf B]=0.
\]

Consequently

\[
\dot r\Rightarrow
\chi\phi(U)+\Eta,\qquad
\chi=D+S_0+\alpha S_1,\qquad
\Eta\sim N(0,\beta),
\tag{5.7}
\]

with \(\Eta\) independent of \((U,R)\).  This reproduces every field used by
the two closed-form derivations.  I found no omitted Onsager direction or
unregistered same-matrix covariance.

The manual leave-one-row counts in Section 6 of the peeling ledger agree with
this registry.  In particular, the equality term in \(A(x_1^2r)\) and the
quadratic equality term in \(A(x_3x_1^3r^3)\) are both order one; the analogous
term for \(A(x_2x_1^2r^2)\) is centered and order \(n^{-1/2}\).  The nonlinear
transpose remainder is rigorously covered by the theorem's conditional
Gaussian projection, so a separate infinite Taylor expansion is neither
needed nor being suppressed.

## 6. Direct uniform-integrability proof for bounded derivatives

This section records a dimension-free alternative for the bounded envelope,
tailored to the exact program.  It replaces a coefficient-tensor sketch from
an earlier ledger draft; the current ledger instead invokes Theorem 3.7 under
its all-orders hypothesis.

Assume

\[
M:=1+\max_{0\le j\le3}\|\phi^{(j)}\|_\infty<\infty,
\qquad K=\|A\|_{\rm op},
\tag{6.1}
\]

and define the normalized empirical norm

\[
\|v\|_{s,n}=\left(M_n(|v|^s)\right)^{1/s}.
\]

Condition on \(\mathscr F_n=\sigma(A,u)\).  The readout \(a\) remains a
standard Gaussian vector.  Both \(r\) and \(\zeta\) are linear functions of
it:

\[
r=L_ra,\qquad L_r=A^\top\operatorname{diag}(y_1),
\tag{6.2}
\]

\[
\zeta=L_\zeta a,
\quad
L_\zeta
=Q_n\operatorname{diag}(y_1)
+qA\operatorname{diag}(x_1^2)A^\top\operatorname{diag}(y_1).
\tag{6.3}
\]

Hence

\[
\|L_r\|_{\rm op}\le MK,\qquad
\|L_\zeta\|_{\rm op}\le M^3(1+qK^2).
\tag{6.4}
\]

For any deterministic matrix \(L\), \(g=La\), and \(t\ge s\ge1\), convexity
and the Gaussian moment formula give

\[
\begin{aligned}
\mathbb E_a\|g\|_{s,n}^{t}
&=\mathbb E_a\left(M_n|g|^s\right)^{t/s}\\
&\le M_n\mathbb E_a|g_i|^t
\le \gamma_t^t\|L\|_{\rm op}^t,
\end{aligned}
\tag{6.5}
\]

where \(\gamma_t=(\mathbb E|N(0,1)|^t)^{1/t}\).  The same bound holds for
\(a\) with \(L=I\).  This is the only probabilistic moment lemma needed.

The exact program now gives the following pathwise inequalities, with
constants depending only on \(q,M\):

\[
|c_n|\le M^3\|r\|_{2,n},
\qquad
|m_n|\le M^4\|r\|_{2,n}^2,
\tag{6.6}
\]

\[
\|\sigma\|_{2,n}
\le 2qM^4\|r\|_{2,n}\|a\|_{2,n}
+q^2KM^3\|r\|_{4,n}^2,
\tag{6.7}
\]

\[
\|\tau\|_{2,n}
\le 3q^2M^5\|r\|_{2,n}^2\|a\|_{2,n}
+q^3KM^4\|r\|_{6,n}^3,
\tag{6.8}
\]

\[
\|B\|_{2,n}
\le M^2+M\|a\|_{4,n}\|\zeta\|_{4,n},
\tag{6.9}
\]

\[
\|\dot r\|_{2,n}
\le M^3\|a\|_{2,n}^2+K\|B\|_{2,n}.
\tag{6.10}
\]

Here (6.7)--(6.10) use only
\(\|Av\|_{2,n}\le K\|v\|_{2,n}\) and empirical Holder.  No operator bound
for a Hadamard product is asserted.

The terminal contractions obey

\[
\begin{aligned}
|\mathcal T_n|\le{}&
M\|a\|_{4,n}\|\zeta\|_{4,n}^3
+3M\|a\|_{4,n}\|\zeta\|_{4,n}\|\sigma\|_{2,n}\\
&+M\|a\|_{2,n}\|\tau\|_{2,n}
+3M^2\big(\|\zeta\|_{2,n}^2+\|\sigma\|_{2,n}\big),
\end{aligned}
\tag{6.11}
\]

\[
\mathcal H_{a,n}\le M^2\|\zeta\|_{2,n}^2,
\tag{6.12}
\]

\[
\begin{aligned}
|\mathcal H_{W,n}|\le{}&
M^2\|B\|_{2,n}^2
+q^2M^6\|a\|_{2,n}^2\|r\|_{2,n}^2\\
&+2qM^4\|a\|_{2,n}\|B\|_{2,n}\|r\|_{2,n},
\end{aligned}
\tag{6.13}
\]

and

\[
\mathcal H_{u,n}
\le qM^2\big(qM\|r\|_{4,n}^2+\|\dot r\|_{2,n}\big)^2.
\tag{6.14}
\]

Equations (6.6)--(6.14) bound \(|C_n|\) by a fixed polynomial in

\[
K,\quad \|a\|_{4,n},\quad \|r\|_{6,n},
\quad \|\zeta\|_{4,n}.
\]

Combining (6.4)--(6.5) with Holder therefore yields, for every fixed
\(p\ge2\), a deterministic polynomial \(P_p\), independent of \(n\), such
that

\[
\mathbb E_a[|C_n|^p\mid A,u]\le P_p(K).
\tag{6.15}
\]

For an iid \(N(0,1/n)\) matrix, the operator norm has uniformly bounded
moments of every fixed order (see, for example, Fact A.3 in Tensor Programs
III).  Integrating (6.15) proves (1.4).  This proof is dimension-free and
contains no coefficient-array norm whose behavior under a Hadamard product
has been left implicit.

## 7. Loss-jet moment conditions under the bounded envelope

The sufficient conditions in `AUDIT_REPORT.md` can also be verified without a
new probabilistic theorem.  The first two feature derivatives have the exact
program forms

\[
K_n=D_nf_n
=M_n(y_0^2)+Q_nM_n(b^2)+qM_n(x_1^2r^2),
\tag{7.1}
\]

\[
J_n=D_n^2f_n
=2M_n[2y_0y_1\zeta+a(y_2\zeta^2+y_1\sigma)].
\tag{7.2}
\]

Also \(f_n=M_n(ay_0)\).  Conditional on \((A,u)\), \(f_n\) is centered
Gaussian with variance at most \(M^2/n\).  Equations (6.5)--(6.10), (7.1),
and (7.2) give uniform moments of every fixed order for \(K_n,J_n,C_n\).
The master theorem supplies their almost-sure deterministic limits; Vitali's
theorem then gives, in particular,

\[
f_n\to0\text{ in }L^8,\qquad
K_n\to A_{\rm NTK}\text{ in }L^6,
\]

\[
\sup_n\|J_n\|_{L^3}<\infty,\qquad
\sup_n\|C_n\|_{L^2}<\infty.
\tag{7.3}
\]

Thus the finite-width cubic loss conversion is also probabilistically
certified for bounded pseudo-Lipschitz derivatives.

## 8. Audit of the maintained ledger and claim status

The audit findings for `PEELING_AND_PROBABILITY_LEDGER.md` are:

| Item | Verdict |
|---|---|
| Exact program (3.1)--(3.10) | Pass; all metric, product-rule, and factorization terms agree |
| Theorem E.15 applicability | Pass under direct pseudo-Lipschitz assumptions (1.1) |
| Response registry | Pass; exhaustive ZDot direction list, including the nonzero \(\Gamma\)--\(\Lambda\) covariance |
| Rank/degeneracy treatment | Pass via Theorem E.15; no full-rank assumption is needed |
| Almost-sure deterministic coefficient | Pass; no multi-copy proof is needed for this scalar |
| Bounded-class UI | Pass independently by Section 6's normalized-norm proof |
| Polynomially smooth annealed limit | Pass by Non-Gaussian Tensor Programs, Theorem 3.7, in every finite \(L^p\) |
| Only third-order polynomial-growth annealed limit | Open unless (1.5) or an activation-specific moment proof is supplied |
| Regularity wording | Must not identify \(C^3\)+polynomial growth with pseudo-Lipschitz \(\phi'''\) |

Accordingly, the claim ladder should be recorded as follows.

1. **Exact finite-width scalarization:** proved.
2. **Explicit 17-atom Gaussian normal form:** algebraically audited.
3. **Joint Gaussian/Onsager and covariance-replacement bridge:** proved
   almost surely under (1.1) by Theorem E.15 and the exact program encoding.
4. **Annealed bounded-activation theorem:** proved by Section 6.
5. **Annealed polynomially smooth theorem:** proved in every finite \(L^p\)
   by Non-Gaussian Tensor Programs, Theorem 3.7.
6. **Only third-order polynomial-growth theorem:** still conditional on
   (1.5); exact polynomial activations are already included in item 5 and
   also admit finite Wick checks.
7. **Positive-time, arbitrary-batch, and arbitrary-depth closure:** untouched
   by this audit.

For the bounded pseudo-Lipschitz activation class, this is enough evidence to
call the (L=2,B=1) Gaussian normal form and its first loss correction fully
audited.  The same is true for the unbounded polynomially smooth class, by
Theorem 3.7.  For an activation assumed only \(C^3\), with polynomial growth
specified only through \(\phi'''\), the almost-sure statement additionally
needs pseudo-Lipschitz regularity (or a proved approximation extension), and
the annealed statement additionally needs (1.5).

The 2026-08-18 amendment to `PROOF_CONTRACT.md` resolves the three contract
issues found by this audit: it names all-orders polynomial smoothness as the
theorem-level class, admits \(L^1/L^p\) convergence of the exact finite-width
scalar as a valid route to the annealed coefficient, and removes the unnecessary
multi-copy requirement for this particular almost-sure scalar limit.
