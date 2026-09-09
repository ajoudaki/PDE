# Adversarial audit: signed polynomial activation in the full (L=2) network

## Verdict

For a polynomial activation with arbitrary lower-coefficient signs, the
positive-semiring comparison between the complete two-hidden-layer network
and its frozen top-row subsystem does **not** extend coefficientwise.  There
is an exact normalized quadratic counterexample at the width-first level.

There is nevertheless a useful sign-free fact: if the activation degree is
even, the complete finite-width coefficient at the greatest *possible*
power of the step size is nonnegative from the second step onward.  This
fact is not enough.  That coefficient can vanish after taking width first;
the normalized activation

\[
 \psi(x)=\frac{x^2-3}{\sqrt6}
\]

kills the entire maximal-order source.  At two steps its first surviving
coefficient is twelve orders lower.  No result currently supplies a
uniform-in-time lower bound for that next source, or for its successors.

Consequently:

1. the signed scalar frozen obstruction proved by the Chebyshev argument
   cannot presently be transferred to the full (L=2) network;
2. a theorem claiming that the full arbitrary-signed polynomial network has
   the same uniform no-go is still open;
3. a proof based only on the maximal joint ((h,\text{raw degree})) sector
   is false.

The exact checks below are reproduced by
`audit_signed_full_bridge.py`.

## 1. Exact highest-step factorization before the width limit

Let

\[
 \phi(x)=\lambda x^d+\text{lower powers},\qquad d\ge2,
\]

and let (f_n) be the same (L=2) finite-width network.  The highest
homogeneous part of the objective has degree

\[
 D=1+d+d^2,
 \qquad r=D-1=d(d+1).
\]

For a parameter point (x=(a,W,u)), define

\[
 H=\lambda u^{\circ d},\qquad z=\frac{WH}{\sqrt n},
 \qquad Y=\lambda z^{\circ d},
\]

\[
 C=\lambda d\,a\circ z^{\circ(d-1)},\qquad
 b=\frac{W^TC}{\sqrt n},\qquad
 U=\lambda d\,u^{\circ(d-1)}\circ b.
\]

If (f_{D,n}) denotes the degree-(D) part of (f_n), its scaled
gradient is exactly

\[
 T:=n\nabla f_{D,n},\qquad
 T(a,W,u)=\left(Y,\frac{CH^T}{\sqrt n},U\right).       \tag{1}
\]

Let (g=n\nabla f_n) be the complete vector field and
(E_hx=x+hg(x)).  Put

\[
 \delta_N=\frac{r^N-1}{r-1}.
\]

Induction on (N) gives the exact random top coefficient

\[
 [h^{D\delta_N}]\,f_n(E_h^Nx)
 =f_{D,n}\!\left(T^{N-1}g(x)\right).                \tag{2}
\]

The point that matters for signed lower terms is visible in (2): every
lower activation monomial is confined to the first source (g(x)); every
later top-order node is the leading homogeneous map (T).  This is an
exact statement, not a raw-degree heuristic.

To prove (2), the top (h)-coefficient of (E_hx) is (g(x)).  If the
top coefficient after (N) steps is (V_N) at degree (delta_N), only
the degree-(r) part (T) of the vector field can attain degree
(1+r\delta_N=delta_{N+1}), so (V_{N+1}=T(V_N)).  At the terminal
node, only (f_{D,n}) can attain (D\delta_N).

## 2. A genuine sign-free fact for even degree

At (x'=Tx), put (H'=\lambda U^{\circ d}).  From (1),

\[
 z'=\frac{(CH^T/\sqrt n)H'}{\sqrt n}=CQ,
 \qquad Q=\frac1nH^TH'.
\]

Therefore

\[
 \boxed{
 f_{D,n}(Tx)=\lambda Q^dR,
 \qquad
 R=\frac1n\sum_iY_iC_i^d.}                         \tag{3}
\]

Assume (d) is even and, after an overall activation sign conjugacy,
(lambda>0).  Then (H,H',Y\ge0), hence (Q\ge0); also
(C_i^d\ge0), hence (R\ge0).  Thus

\[
 f_{D,n}(Tx)\ge0\quad\text{for every real }x.       \tag{4}
\]

Combining (2) and (4), for every (N\ge2), the finite-width maximal
random coefficient is pointwise nonnegative.  Its expectation and every
existing width limit are nonnegative as well.  This survives arbitrary
signs in all lower activation coefficients.

There are two sharp limitations.

* For odd (d), neither (Q^d) nor (R) has a protected sign.
* Even for even (d), (4) does not give strict positivity after
  (n\to\infty).  A nonnegative finite-width quantity may converge to
  zero at the mean-field normalization.

The second limitation actually occurs.

## 3. Exact mean-field collapse for a normalized shifted quadratic

Write

\[
 \psi(x)=a+bx^2,\qquad a^2+2ab+3b^2=1.              \tag{5}
\]

The normalization makes the initialization preactivation (Z) standard
Gaussian.  In the one-step inverse-free OMFP recursion,

\[
 C_0=2bAZ,qquad \operatorname{Var}(\chi_0)=4b^2,
\]

\[
 u_1=U+2bh\chi_0U,qquad H_1=\psi(u_1).
\]

Direct Gaussian integration gives

\[
 Q_{01}=\mathbb E[H_0H_1]
 =1+16b^5(a+3b)h^2,                                \tag{6}
\]

\[
 \rho_{10}=\mathbb E[\partial_{\chi_0}H_1]=4b^2h. \tag{7}
\]

Thus, with

\[
 L=\rho_{10}+hQ_{01}
   =h(1+4b^2)+16b^5(a+3b)h^3,
\]

the updated top preactivation is (z_1=\xi_1+LC_0).  In

\[
 F_1(h)=\mathbb E[(A+h\psi(Z))\psi(z_1)],
\]

the only term capable of reaching degree seven is

\[
 4b^3h(a+3b)L^2.
\]

Consequently

\[
 \boxed{[h^7]F_1(h)=1024b^{13}(a+3b)^3.}            \tag{8}
\]

For the normalized family

\[
 \psi_K(x)=q_K(x^2-K),\qquad
 q_K=(K^2-2K+3)^{-1/2},                             \tag{9}
\]

(8) becomes

\[
 \boxed{[h^7]F_1(h)=1024q_K^{16}(3-K)^3.}           \tag{10}
\]

Hence the integrated maximal coefficient changes sign and vanishes exactly
at (K=3).  This does not contradict (4), which begins at (N=2).

The same cancellation has a structural source.  For even (d), define

\[
 v=\mathbb E\phi'(G)^2,qquad
 m=\mathbb E[\phi(G)\phi'(G)^d],qquad
 \gamma=(d-1)!!.
\]

At the first full-gradient source, the two deterministic rank-one
contractions entering the first leading map (T) converge to

\[
 S=\lambda\gamma v^{d/2}m,
 \qquad R_0=\gamma m.                               \tag{11}
\]

Indeed, if (Y_0=\phi(z_0)), (C_0=a_0\phi'(z_0)),
(H_0=\phi(u_0)), and (B_0=W^TC_0/\sqrt n), then

\[
 R_0^{(n)}=\frac1n\sum_iY_{0,i}C_{0,i}^d
 \longrightarrow\gamma m,
\]

\[
 S^{(n)}=\frac1n\sum_jH_{0,j}
 \lambda\{\phi'(u_{0,j})B_{0,j}\}^d
 \longrightarrow\lambda\gamma v^{d/2}m.           \tag{12}
\]

These are ordinary fixed-program moment limits.  The exact rank-one
identities after applying (T) to the full-gradient source contain the
factors

\[
 z_y=S^{(n)}C_0,qquad
 Y_y=\lambda(S^{(n)})^dC_0^d,
\]

\[
 C_y=\lambda d(S^{(n)})^{d-1}Y_0C_0^{d-1},
\qquad
 b_y=H_0\{\lambda d(S^{(n)})^{d-1}R_0^{(n)}\}.      \tag{13}
\]

Therefore (m=0) makes the first leading map collapse in every finite
(L^p) after the width limit.  For (psi=(x^2-3)/\sqrt6),

\[
 m=\frac{4}{6^{3/2}}\mathbb E[(G^2-3)G^2]=0.        \tag{14}
\]

Thus every greatest-possible-(h) coefficient generated by repeatedly
applying that leading map is zero in the width-first DAG.  This is a direct
counterexample to the proposed “maximal raw sector must survive” lemma.

An independent exact check at (N=2) is especially concrete.  The formal
maximum is

\[
 D\delta_2=7(1+6)=49.
\]

For (psi=(x^2-3)/\sqrt6), the coefficients at degrees
(49,47,45,43,41,39) are all zero, while

\[
 [h^{37}]F_2(h)
 =\frac{25734273826816}{68630377364883}>0.          \tag{15}
\]

So a lower source survives, but it is not the source identified by maximal
bidegree counting.

## 4. Exact failure of coefficientwise frozen/full deletion

Consider the rationally normalized activation

\[
 \psi(x)=\frac{10}{27}\left(x^2-\frac{33}{10}\right)
 =-\frac{11}{9}+\frac{10}{27}x^2.                  \tag{16}
\]

Indeed,

\[
 \left(\frac{10}{27}\right)^2
 \left\{\left(\frac{33}{10}\right)^2
 -2\frac{33}{10}+3\right\}=1.
\]

Let

\[
 \Delta^{\rm full}_1(h)=F_2(h)-F_1(2h)
\]

and let (Delta^{\rm fr}_1) be the same paired defect after deleting the
bottom-feature update.  Exact chronological Gaussian/Wick evaluation of
the width-first DAG gives

\[
\begin{split}
 [h^{11}]\{\Delta^{\rm full}_1-\Delta^{\rm fr}_1\}
 ={}&-
 \frac{50342126934494248177872714327572247743518720000000000}
 {375710212613636260325580163599137907799836383538729}\\
 <{}&0.                                                \tag{17}
\end{split}
\]

Negative coefficients also occur at orders (13,23,25,39,43,47).
Therefore the coefficientwise inequality used for nonnegative activation
coefficients is genuinely false after Gaussian integration for a signed
activation.  This is not merely the absence of a proof.

Equation (17) does **not** prove that
(Delta^{\rm full}_1(h)<\Delta^{\rm fr}_1(h)) at some positive (h):
other powers can dominate the value.  It disproves the coefficientwise
order, which is the exact property needed to retain a frozen coefficient
inside the full defect.

## 5. Why Chebyshev does not close the full theorem

For a degree-(k) polynomial (P(h)=Lh^k+\cdots),

\[
 \sup_{0\le h\le H}|P(h)|
 \ge 2^{1-2k}|L|H^k.                                \tag{18}
\]

Thus signs of *lower powers of (h)* are harmless once a quantitatively
large nonzero full-network coefficient (L) has been found.  This closes
the arbitrary-signed scalar theorem.

For the complete network, the missing input to (18) is precisely:

* an activation-defined rule selecting, for every large (N), a nonzero
  width-first coefficient after all mean-field contractions; and
* a lower bound whose logarithm contains the necessary
  (k_N\log k_N) Gaussian-moment gain.

Equations (10)--(15) show that the formal maximal sector cannot be used as
that rule.  Equation (17) shows that a frozen scalar sector cannot simply be
retained.  A finite-width all-same-index monomial is also insufficient: its
normalization may vanish as (n\to\infty), which is exactly the forbidden
reversal of limits.

The exact source factorization (2) suggests the right future problem: form
a hierarchy of the first nonzero width-limit contractions of (g(x_0))
under the homogeneous map (T), then prove a dimension-free quantitative
lower bound for the first surviving source.  Neither a nonzero-source
theorem nor the required factorial lower bound has yet been proved for all
signed polynomial activations.

## 6. Hostile audit checklist

| Claim | Verdict | Reason |
|---|---|---|
| Full top-(h) factorization (2) | pass | direct homogeneous-degree induction |
| Even-degree pointwise sign (3)--(4) | pass | exact rank-one factorization |
| Strict width-limit positivity of the maximal coefficient | fail | normalized (x^2-3) makes (m=0) |
| Maximal raw-degree sector dominates integrated coefficient | fail | (10)--(15) |
| Coefficientwise full/frozen paired order for signed activations | fail | exact negative coefficient (17) |
| Pointwise full/frozen order for every positive (h) | unresolved | (17) alone does not decide values |
| Chebyshev removal of cancellation among (h)-powers | pass | exact extremal inequality (18) |
| Uniform full-network coefficient lower bound for every signed polynomial | open | first surviving source not controlled |

The scalar signed-polynomial no-go and the full nonnegative-coefficient
no-go remain intact.  What remains open is exactly their combination:
arbitrary signed coefficients in the actual width-first (L=2) network.
