# Route B: state-level Osgood sewing for depth-two OMFP

## 1. Verdict

There is a clean state-level sewing argument for the actual width-first,
depth-two population recursion, but one additional estimate is necessary.
The exact sufficient estimate is a mesh- and horizon-uniform subexponential
bound for the reused transpose action

\[
 Q_k=(\Gamma+q_k)^*B_k. \tag{1.1}
\]

More generally, it is enough that, for some \(1/2\leq\alpha\leq1\),

\[
 \sup_{\substack{\pi=(h_0,\ldots,h_{N-1})\\
                  h_j>0,\ \sum_jh_j\leq T,\ \max_jh_j\leq h_*}}
 \ \sup_{0\leq k\leq N}
 \sup_{p\geq2}p^{-\alpha}\|Q_k^\pi\|_p
 \leq K_T<\infty .                                   \tag{1.2}
\]

Here the supremum is over all sufficiently fine positive step partitions
with total feature time at most \(T\), all width limits are taken separately
at each fixed finite partition, and the same immutable pointed Gaussian
action source is used for every partition.

Under (1.2), Sections 6--8 prove:

1. an activation-defined Osgood modulus for the exact population vector
   field on the reachable total-time tube;
2. the summable split estimate
   \[
    d(S_h^2U,S_{2h}U)
    \leq C_T h^2\{\log(e/h)\}^{\alpha};                \tag{1.3}
   \]
3. uniform dyadic convergence of the complete population state;
4. convergence to the restartable autonomous feature-time IDE; and
5. convergence of the predictor.

This implication is rigorous and uses no fifth output derivative.

The present project does **not** prove (1.2) from the bounded \(C^{12}\)
activation hypotheses.  The fixed-operator theorem gives
an \(L^2\)-bounded action, and the fixed-finite-program theorem gives moments
whose constants may depend on the number of steps.  Neither gives a
subexponential bound uniform as the mesh tends to zero.

The arctangent natural coordinate does not remove this missing bridge for
the actual discrete algorithm.  It linearizes the continuous differential
equation, not a finite gradient step.  In that coordinate an exact step
contains \(Q^2\) and \(Q^3\); see Section 9.  Thus the unconditional
continuous arctangent IDE already proved in
nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md must not be
mistaken for a proof that the width-first discrete OMFP converges to it.

Accordingly, the unconditional discrete-to-continuous OMFP theorem remains
open.  Section 10 states the exact fatal gap and a response formulation
which would close it.

## 2. Exact finite-width recursion

Let \(H_n=\mathbb R^n\) with

\[
 \langle v,w\rangle_n=n^{-1}v^{\mathsf T}w.
\]

For the two-hidden-layer network put

\[
 X=\phi(u),\qquad Z=GX,\qquad Y=\phi(Z),               \tag{2.1}
\]

\[
 B=A\phi'(Z),\qquad Q=G^*B,\qquad D=\phi'(u)Q.         \tag{2.2}
\]

All products not explicitly written as inner products are coordinatewise.
The predictor is

\[
 f_n(A,u,G)=\langle A,Y\rangle_n.                     \tag{2.3}
\]

The normalized vector metrics and Frobenius matrix metric give the exact
feature-ascent step

\[
\boxed{
 A^+=A+hY,\qquad
 u^+=u+hD,\qquad
 G^+=G+h\,B\otimes X ,
}                                                       \tag{2.4}
\]

where

\[
 (B\otimes X)v=B\langle X,v\rangle_n
              =n^{-1}BX^{\mathsf T}v.                 \tag{2.5}
\]

At initialization, \(A_0,u_0\) have independent standard Gaussian
coordinates, \(G_0=W_0/\sqrt n\), and the entries of \(W_0\) are independent
standard Gaussians, independent of \(A_0,u_0\).

For arctangent,

\[
 \phi(s)=\arctan s,\qquad c(s)=\phi'(s)=\frac1{1+s^2},
 \qquad d(s)=\phi'(s)=\frac1{1+s^2}.                  \tag{2.6}
\]

Then \(D=c(u)Q\) and \(B=A\,d(Z)\).  Equation (2.4), rather than an
Euler step in a transformed coordinate, is the discrete algorithm to be
sewn.

## 3. Width-first population step and all reused-matrix terms

The pointed-action source theorem in
nonlinear_activation_operator_ide/ARCTAN_THEOREM_AND_PROOF.md constructs

\[
 \mathfrak G=(H_R,H_C;a_0,u_0,\Gamma),\qquad
 \|\Gamma\|_{\mathrm{op}}\leq2,                       \tag{3.1}
\]

where \(\Gamma:H_C\to H_R\) and \(\Gamma^*:H_R\to H_C\)
are the joint limits of \(G_0,G_0^*\).  The source retains adaptive
alternating reuse and is stronger than a one-sided Gaussian law.

Use the population state

\[
 \mathcal X_u
 =H_R\oplus H_C\oplus\mathfrak S_1(H_C,H_R),\qquad
 U=(A,u,q),                                           \tag{3.2}
\]

with metric

\[
 d(U,\widetilde U)
 =\|A-\widetilde A\|_2+\|u-\widetilde u\|_2
   +\|q-\widetilde q\|_1.                             \tag{3.3}
\]

Set \(G=\Gamma+q\), define (2.1)--(2.2) in the two source
probability spaces, and write

\[
 g(U)=(Y,D,B\otimes X),\qquad S_hU=U+h\,g(U).          \tag{3.4}
\]

For every fixed finite step list, the finite-program theorem identifies the
width limit of (2.4) with the corresponding composition of the maps
\(S_h\).  This is a pointwise fixed-step identification: no limit in the
number of steps and no small-step expansion is taken here.

This imports the proved two-sided finite-program theorem and its canonical
pointed-action realization from the cited source; it is not a new proof of
that theorem.  For any fixed dyadic refinement sequence, adjoin its
countably many scalar step constants to the countable program language
(equivalently, approximate by rational constants and use fixed-program
continuity).  Projective consistency then realizes every mesh with the same
immutable \(\Gamma,\Gamma^*\).  The comparison below therefore never
refreshes the Gaussian matrix.

We now derive every reuse term explicitly.  For arbitrary steps
\(h_0,\ldots,h_{N-1}\), iteration of the matrix update gives the exact
finite-width identity

\[
 G_k=G_0+\sum_{j<k}h_jB_j\otimes X_j.                 \tag{3.5}
\]

Therefore

\[
 G_kX_k
 =G_0X_k+\sum_{j<k}h_jB_j\langle X_j,X_k\rangle_n,    \tag{3.6}
\]

\[
 G_k^*B_k
 =G_0^*B_k+\sum_{j<k}h_jX_j\langle B_j,B_k\rangle_n.  \tag{3.7}
\]

Both the direct learned term and the transpose learned term are present.
Passing to the fixed finite-program limit replaces \(G_0,G_0^*\) by
\(\Gamma,\Gamma^*\) and the empirical inner products by source
expectations.

There is also an inverse-free response expansion.  On the fixed Gaussian
realization used by the project, write

\[
 \Gamma=I+J^*,\qquad \Gamma^*=I^*+J.                  \tag{3.8}
\]

Let

\[
 \xi_k=IX_k,\qquad \chi_k=JB_k,                       \tag{3.9}
\]

and define cylindrical response coefficients

\[
 \rho_{kj}=\mathbb E[\partial_{\chi_j}X_k]\quad(j<k),
 \qquad
 \sigma_{kj}=\mathbb E[\partial_{\xi_j}B_k]\quad(j\leq k).
                                                               \tag{3.10}
\]

Gaussian integration by parts on the fixed first-chaos blocks gives

\[
 J^*X_k=\sum_{j<k}\rho_{kj}B_j,\qquad
 I^*B_k=\sum_{j\leq k}\sigma_{kj}X_j.                 \tag{3.11}
\]

Indeed, if \(X_k=\Psi(\chi_0,\ldots,\chi_{k-1},\zeta)\), then for every
\(C\in H_R\),

\[
\begin{aligned}
 \langle C,J^*X_k\rangle
 &=\mathbb E[(JC)X_k] \\
 &=\sum_{j<k}\langle C,B_j\rangle\,
       \mathbb E[\partial_{\chi_j}X_k].
\end{aligned}                                         \tag{3.12}
\]

Since this holds for every \(C\), the first identity in (3.11) follows.
The second is identical with the two sorts reversed.  No covariance inverse
or Gram invertibility is used, so (3.11) remains valid at singular time
Grams.

Combining (3.6)--(3.11) yields the complete population formulas

\[
\boxed{
 Z_k=\xi_k+\sum_{j<k}
 \left\{\rho_{kj}+h_j\langle X_j,X_k\rangle\right\}B_j ,
}                                                       \tag{3.13}
\]

\[
\boxed{
 Q_k=\chi_k+\sum_{j\leq k}\sigma_{kj}X_j
 +\sum_{j<k}h_j\langle B_j,B_k\rangle X_j .
}                                                       \tag{3.14}
\]

The dependence of \(X_k\) on every reused column through earlier
\(\chi_j=JB_j\) is exactly the \(\rho_{kj}\) term.  Omitting it would replace
the reused transpose action by an incorrectly refreshed Gaussian.

For \(j<k\), chronological differentiation gives the causal factors

\[
 \rho_{kj}=h_j\bar\rho_{kj},\qquad
 \sigma_{kj}=h_j\bar\sigma_{kj}.                      \tag{3.15}
\]

Here is the full divisibility induction.  Expose independent symbolic step
variables and use the inverse-free chronology

\[
 A_s=a_0+\sum_{i<s}h_iY_i,\qquad
 u_s=u_0+\sum_{i<s}h_iD_i,                             \tag{3.15a}
\]

\[
 Z_s=\xi_s+\sum_{i<s}
 \{\rho_{si}+h_i\langle X_i,X_s\rangle\}B_i,           \tag{3.15b}
\]

\[
 Q_s=\chi_s+\sum_{i\leq s}\sigma_{si}X_i
 +\sum_{i<s}h_i\langle B_i,B_s\rangle X_i.             \tag{3.15c}
\]

For a fixed \(j\), mutually induct on \(s\) with the assertions

\[
 \partial_{\chi_j}u_s,\ \partial_{\chi_j}X_s
 \text{ are algebraically divisible by }h_j
 \quad (j<s),                                         \tag{3.15d}
\]

and

\[
 \partial_{\xi_j}A_s,\ \partial_{\xi_j}Z_s,\
 \partial_{\xi_j}B_s
 \text{ are algebraically divisible by }h_j
 \quad (j<s).                                         \tag{3.15e}
\]

Both are vacuous before the source time.  If (3.15d) holds at time \(s\),
the chain rule gives the same factor for
\(\partial_{\chi_j}X_s\), and hence

\[
 \rho_{sj}
 =\mathbb E[\partial_{\chi_j}X_s]
 =h_j\mathbb E[\phi'(u_s)p_s^j]
\]

for the algebraically defined quotient
\(p_s^j=h_j^{-1}\partial_{\chi_j}u_s\).  No numerical division is used at
\(h_j=0\).

Next fix \(j<s\) and differentiate the first equation in (3.15a) with
respect to \(\xi_j\).  The \(i=j\) summand has the explicit factor \(h_j\);
terms with \(i>j\) have it by induction, and earlier terms are independent
of \(\xi_j\).  Thus \(\partial_{\xi_j}A_s\) has the factor.  In
(3.15b), the raw \(\xi_s\) is held fixed.  The \(i=j\) coefficient
\(\rho_{sj}+h_j\langle X_j,X_s\rangle\) has the factor just proved;
terms with \(i>j\) inherit it through \(B_i\), and earlier terms are
independent of \(\xi_j\).  Hence
\(\partial_{\xi_j}Z_s\), and then
\(\partial_{\xi_j}B_s\), have the factor.  Taking expectation proves the
second identity in (3.15).

It remains to advance (3.15d).  Differentiate (3.15c) with respect to an
older \(\chi_j\).  The \(i=j\) response coefficient has the factor \(h_j\)
from (3.15e), the \(i=j\) learned coefficient has an explicit \(h_j\),
and every later \(X_i\) derivative has the factor by induction.  Earlier
terms are independent of \(\chi_j\), while the raw current source
\(\chi_s\) is held fixed.  Thus
\(\partial_{\chi_j}Q_s\) has the factor.  The chain rule for
\(D_s=\phi'(u_s)Q_s\) preserves it, and
\(u_{s+1}=u_s+h_sD_s\) advances every old source.  For the new source,
\(\partial_{\chi_s}u_{s+1}=h_s\phi'(u_s)\), because the coefficient of
the raw \(\chi_s\) in \(Q_s\) is one.  This closes the mutual induction.

At fixed finite horizon, every node is a \(C^1\), polynomially bounded
function of finitely many Gaussian source coordinates; bounded activation
derivatives and Gaussian moments dominate every derivative above.  Thus
the chain rules and expectations are justified.  The construction uses
the fixed \(I,J\) realization, so it remains valid at singular source
Grams.

At the current time there is instead

\[
 \sigma_{kk}
 =\mathbb E[A_k\phi''(Z_k)].                           \tag{3.16}
\]

Thus (3.13)--(3.14) can equivalently be written

\[
 Z_k=\xi_k+\sum_{j<k}h_j
 \{\bar\rho_{kj}+\langle X_j,X_k\rangle\}B_j,          \tag{3.17}
\]

\[
 Q_k=\chi_k+\sigma_{kk}X_k
 +\sum_{j<k}h_j
 \{\bar\sigma_{kj}+\langle B_j,B_k\rangle\}X_j.        \tag{3.18}
\]

These formulas display precisely which estimate is missing: the step
weights control the historical sums only if the normalized responses have a
uniform total-variation or moment bound.

## 4. Dimension-free reachable tubes

For arctangent put \(a=\pi/2\).  Along every positive-step recursion with
elapsed feature time \(\tau_k=\sum_{j<k}h_j\leq T\),

\[
 |X_k|,|Y_k|\leq a,\qquad |B_k|\leq|A_k|.             \tag{4.1}
\]

Consequently

\[
 \|A_k\|_2\leq A_T:=\|a_0\|_2+aT,                     \tag{4.2}
\]

\[
 \|q_k\|_1
 \leq a\left(\|a_0\|_2T+\frac a2T^2\right)=:q_T,      \tag{4.3}
\]

\[
 \|G_k\|_{\mathrm{op}}\leq 2+q_T=:g_T,                \tag{4.4}
\]

\[
 \|Q_k\|_2\leq g_TA_T,\qquad
 \|D_k\|_2\leq g_TA_T,                                \tag{4.5}
\]

and

\[
 \|u_k\|_2\leq \|u_0\|_2+Tg_TA_T.                    \tag{4.6}
\]

Moreover,

\[
 A_k=a_0+\alpha_k,\qquad \|\alpha_k\|_\infty\leq aT. \tag{4.7}
\]

The same estimates hold at finite width on the event controlling the
initial normalized norms and \(\|G_0\|_{\mathrm{op}}\).  They use only
Hilbert norms, trace norm, and the initialization spectral bound, and are
therefore dimension free.

Equations (4.2)--(4.7) give a uniform bound

\[
 \|g(U_k)\|_{\mathcal X_u}\leq M_T.                   \tag{4.8}
\]

They do not imply (1.2): an \(L^2\) bound is not a subexponential-tail
bound.

## 5. The exact bad multiplier

All vector-field differences except one are controlled by the existing
Gaussian envelope.  On the tube above,

\[
 \|X-\widetilde X\|_2+\|Z-\widetilde Z\|_2
 +\|Y-\widetilde Y\|_2
 \leq C_T d(U,\widetilde U).                          \tag{5.1}
\]

Since \(A=a_0+\alpha\), with \(a_0\) Gaussian and \(\alpha\) bounded,
the Gaussian multiplier lemma gives

\[
 \|B-\widetilde B\|_2
 \leq C_T\,d(U,\widetilde U)
 +C_T\,d(U,\widetilde U)
       \sqrt{\log\!\frac{e}{d(U,\widetilde U)}}        \tag{5.2}
\]

for small distances.  Hence

\[
 \|Q-\widetilde Q\|_2
 \leq C_T\,d(U,\widetilde U)
 +C_T\,d(U,\widetilde U)
       \sqrt{\log\!\frac{e}{d(U,\widetilde U)}}.        \tag{5.3}
\]

For the bottom update,

\[
\begin{aligned}
 D-\widetilde D
 &=c(u)(Q-\widetilde Q)
   +\widetilde Q\{c(u)-c(\widetilde u)\}.              \tag{5.4}
\end{aligned}
\]

The first term is controlled by (5.3).  The second is the obstruction.
The fixed pointed action gives only \(\widetilde Q\in L^2\).
Multiplication \(L^2\times L^2\to L^2\) is not bounded.

This is not merely a missing convenient inequality.  Let \(E_m\) have
probability \(m^{-2}\), put \(Q_m=m\,\mathbf1_{E_m}\), and choose a point
\(s_0\) with \(c'(s_0)\ne0\).  For a fixed sufficiently small
\(\varepsilon\ne0\), set

\[
 u_m=s_0+\varepsilon\mathbf1_{E_m},\qquad
 \widetilde u_m=s_0.
\]

Then

\[
 \|Q_m\|_2=1,\qquad
 \|u_m-\widetilde u_m\|_2=|\varepsilon|m^{-1}\to0,     \tag{5.5}
\]

but

\[
 \|Q_m\{c(u_m)-c(\widetilde u_m)\}\|_2
 =|c(s_0+\varepsilon)-c(s_0)|>0.                      \tag{5.6}
\]

Thus the exact vector field is not uniformly continuous on an \(L^2\)
state ball.  The example is a topology obstruction, not a claim that these
particular fields are reachable OMFP states.  To use reachable structure,
one must prove a uniform reachable-tail estimate such as (1.2).

## 6. Multiplier estimate under the minimal Osgood tail hypothesis

The following lemma explains why (1.2) is the right scale.

### Lemma 6.1

Let \(1/2\leq\alpha\leq1\), let

\[
 \sup_{p\geq2}p^{-\alpha}\|R\|_p\leq K,               \tag{6.1}
\]

and let \(h\) be bounded and Lipschitz.  Then, for
\(\delta=\|v-\widetilde v\|_2\leq1/2\),

\[
 \|R\{h(v)-h(\widetilde v)\}\|_2
 \leq C_{\alpha,K,h}\,
 \delta\{\log(e/\delta)\}^{\alpha}.                   \tag{6.2}
\]

#### Proof

Put \(w=h(v)-h(\widetilde v)\).  For \(p\geq2\), Hölder and interpolation
between \(L^2\) and \(L^\infty\) give

\[
\begin{aligned}
 \|Rw\|_2
 &\leq\|R\|_{2p}\|w\|_{2p/(p-1)}\\
 &\leq K(2p)^\alpha
 (L_h\delta)^{1-1/p}(2\|h\|_\infty)^{1/p}.            \tag{6.3}
\end{aligned}
\]

Choose \(p\) to be the least integer at least
\(\log(e/\delta)\).  The two factors raised to \(1/p\) are bounded by
constants depending only on \(h\), and (6.2) follows. \(\square\)

Define, for \(0<r\leq1\),

\[
 \omega_\alpha(r)=r\{\log(e/r)\}^{\alpha},            \tag{6.4}
\]

with \(\omega_\alpha(0)=0\), and extend it past \(1\) by its nonnegative
tangent line (by the constant \(1\) when \(\alpha=1\)).  This is increasing
and concave, hence subadditive.  It is an Osgood modulus precisely for
\(\alpha\leq1\):

\[
 \int_{0^+}\frac{dr}{\omega_\alpha(r)}=\infty.         \tag{6.5}
\]

### Proposition 6.2

Assume the reachable-tail bound (1.2).  There is a constant \(C_T\),
depending only on the activation data, \(T\), the initialization moments,
and \(K_T\), such that any two reachable states on the tube satisfy

\[
 \|g(U)-g(\widetilde U)\|_{\mathcal X_u}
 \leq C_T\omega_\alpha(C_Td(U,\widetilde U)).          \tag{6.6}
\]

#### Proof

Equations (5.1)--(5.3) control \(X,Z,Y,B,Q\).  The rank-one identity

\[
 \|B\otimes X-\widetilde B\otimes\widetilde X\|_1
 \leq\|B-\widetilde B\|_2\|X\|_2
 +\|\widetilde B\|_2\|X-\widetilde X\|_2              \tag{6.7}
\]

controls the operator component.  Apply Lemma 6.1 to the second term in
(5.4), with \(R=\widetilde Q\) and \(h=c\).  Since
\(\alpha\geq1/2\), the Gaussian-envelope modulus in (5.2)--(5.3) is
bounded by a constant multiple of \(\omega_\alpha\).  Summing the three
state components proves (6.6). \(\square\)

### Lemma 6.3 (tail inheritance by reachable closure)

Suppose \(U_m\to U\) in (3.3), every \(U_m\) is reachable, and

\[
 \|Q(U_m)\|_p\leq K_Tp^\alpha\qquad(p\geq2).           \tag{6.8}
\]

Then \(Q(U_m)\to Q(U)\) in \(L^2\), and

\[
 \|Q(U)\|_p\leq K_Tp^\alpha\qquad(p=2,3,\ldots).       \tag{6.9}
\]

For real \(p\geq2\), the same estimate holds with \(K_T\) replaced by
\(2^\alpha K_T\).

#### Proof

Equation (5.3) gives \(L^2\) convergence.  Choose an almost-sure
subsequence and diagonalize over the countably many integer \(p\)'s.
Fatou's lemma gives, for each such \(p\),

\[
 \mathbb E|Q(U)|^p
 \leq\liminf_m\mathbb E|Q(U_m)|^p
 \leq(K_Tp^\alpha)^p.
\]

For real \(p\), use monotonicity of \(L^p\) norms with the next integer
\(m<2p\).  This proves the claim. \(\square\)

Subexponential growth, \(\alpha=1\), is therefore sufficient; a
sub-Gaussian estimate is stronger than necessary.  Moment growth
\(\|Q\|_p\lesssim p^\alpha\) with \(\alpha>1\) produces a non-Osgood
modulus and does not close this route.

## 7. Exact split defect and forced discrete Osgood lemma

Because (3.4) is the actual update in the original \(u\) coordinate,

\[
\begin{aligned}
 S_h^2U-S_{2h}U
 &=h\{g(S_hU)-g(U)\}.                                 \tag{7.1}
\end{aligned}
\]

Using (4.8) and (6.6),

\[
 d(S_h^2U,S_{2h}U)
 \leq C_T h\,\omega_\alpha(C_TM_Th)
 \leq C_T h^2\{\log(e/h)\}^{\alpha}.                  \tag{7.2}
\]

This is the desired local split defect.  Local summability alone is not
enough; it must be propagated through an Osgood, rather than Lipschitz,
flow.  The following elementary lemma does that.

### Lemma 7.1 (forced discrete Osgood)

Let \(\Omega:[0,\infty)\to[0,\infty)\) be continuous and increasing,
\(\Omega(r)>0\) for \(r>0\), and

\[
 \int_{0^+}\frac{dr}{\Omega(r)}=\infty.
\]

Suppose

\[
 d_{k+1}\leq d_k+h_k\Omega(d_k)+e_k,\qquad e_k\geq0.   \tag{7.3}
\]

Put \(E_k=\sum_{\ell\geq k}e_\ell\) and \(z_k=d_k+E_k\).
If \(\Gamma_s(r)\) is the unique nonnegative scalar flow of

\[
 y'=\Omega(y),\qquad y(0)=r,                          \tag{7.4}
\]

then

\[
 d_k\leq z_k\leq\Gamma_{\sum_{\ell<k}h_\ell}
                    (d_0+E_0).                       \tag{7.5}
\]

#### Proof

From (7.3),

\[
 z_{k+1}\leq z_k+h_k\Omega(d_k)
          \leq z_k+h_k\Omega(z_k).                    \tag{7.6}
\]

The reciprocal-integral condition gives uniqueness at zero by Osgood;
for a positive initial value, separation of variables gives uniqueness
because \(\Omega>0\).  Hence this flow has the semigroup property.  Since
\(\Omega\) is increasing, the exact scalar flow over time \(h_k\)
lies above its left Euler chord:

\[
 \Gamma_{h_k}(z_k)
 =z_k+\int_0^{h_k}\Omega(\Gamma_s(z_k))\,ds
 \geq z_k+h_k\Omega(z_k).                             \tag{7.7}
\]

Induction and the scalar semigroup property give (7.5). \(\square\)

## 8. Conditional state convergence and the IDE

### Theorem 8.1

Assume (1.2) for every finite \(T\), with the same bound after restart from
every state in the closure of the reachable tube before time \(T\).  Then
the width-first dyadic
recursions

\[
 U^{(j)}_k=S_{h_j}^kU_0,\qquad h_j=h_02^{-j},          \tag{8.1}
\]

with piecewise affine interpolation, converge uniformly on compact
feature-time intervals in the metric (3.3).  Their limit is the unique
restartable solution of

\[
\boxed{
 A'=Y,\qquad u'=\phi'(u)Q,\qquad q'=B\otimes X,
}                                                       \tag{8.2}
\]

where \(X,Z,Y,B,Q\) are (2.1)--(2.2) with \(G=\Gamma+q\).
Moreover,

\[
 F(t)=\langle A(t),Y(t)\rangle                         \tag{8.3}
\]

is the uniform compact-time limit of the width-first dyadic predictors.

#### Proof

Compare a fine \(h\)-trajectory with a coarse \(2h\)-trajectory on the
common half-grid.  Affinely interpolate each coarse update: on its first
half-step use \(g(V_{2j})\), and on its second half-step use the same frozen
value \(g(V_{2j})\).  Let \(d_k\) be the state distance on this half-grid.
On a first half-step, (6.6) gives

\[
 d_{k+1}\leq d_k+h\Omega_T(d_k).                      \tag{8.4}
\]

On a second half-step, the coarse slope is evaluated one half-step earlier.
Using (4.8), concavity, and subadditivity of \(\omega_\alpha\),

\[
\begin{aligned}
 d_{k+1}
 &\leq d_k+h\Omega_T(d_k+hM_T)\\
 &\leq d_k+h\Omega_T(d_k)+h\Omega_T(hM_T).             \tag{8.5}
\end{aligned}
\]

Thus Lemma 7.1 applies with total forcing

\[
 E_0\leq \frac{T}{2}\Omega_T(hM_T)
 \leq C_T h\{\log(e/h)\}^{\alpha}=:\varepsilon_h.     \tag{8.6}
\]

For \(0\leq\alpha<1\), the scalar equation
\(y'=C_Ty\{\log(e/y)\}^{\alpha}\) obeys, while \(y\leq1\),

\[
 \{\log(e/y(s))\}^{1-\alpha}
 =\{\log(e/y(0))\}^{1-\alpha}
 -C_T(1-\alpha)s.                                     \tag{8.7}
\]

For \(\alpha=1\),

\[
 \log(e/y(s))=e^{-C_Ts}\log(e/y(0)).                  \tag{8.8}
\]

It follows from (8.6)--(8.8), with \(h=h_j\), that consecutive-mesh
differences are bounded respectively by

\[
 C_T2^{-j}(1+j)^\alpha
       \exp\{C_T(1+j)^\alpha\}\quad(\alpha<1),          \tag{8.9}
\]

or

\[
 C_T\{2^{-j}(1+j)\}^{e^{-C_TT}}\quad(\alpha=1).         \tag{8.10}
\]

Both series over \(j\) converge.  Hence the affine state paths are uniformly
Cauchy on the common half-grids.  Between adjacent half-grid points both
affine paths move at speed at most \(M_T\), so their distance is at most
the preceding grid distance plus \(2M_Th_j\).  Since
\(\sum_j2M_Th_j<\infty\), they are uniformly Cauchy on all of \([0,T]\).

Their slopes are bounded by \(M_T\), so the limit \(U\) is Lipschitz in
time.  If \(\overline U^{(j)}\) is the left-step interpolation, then

\[
 U^{(j)}(t)=U_0+\int_0^t g(\overline U^{(j)}(s))\,ds,  \tag{8.11}
\]

and

\[
 \sup_{s\leq T}d(\overline U^{(j)}(s),U(s))\to0.
\]

Equation (6.6) implies uniform convergence of the integrands in the Banach
state norm.  Passing the Bochner integral in (8.11) proves (8.2).

Lemma 6.3 shows that every state in the limit path inherits (1.2).  If
\(U,\widetilde U\) are two integral solutions in this inherited
reachable-tail closure with the same initial state, (6.6) gives

\[
 d(U(t),\widetilde U(t))
 \leq\int_0^t C_T\omega_\alpha
 \{C_Td(U(s),\widetilde U(s))\}\,ds.                  \tag{8.12}
\]

Bihari--Osgood and (6.5) force this distance to vanish.  Thus uniqueness
is proved only in the stated inherited reachable-tail class.  Autonomy,
the restart version of (1.2), and retention of the same immutable source
\(\Gamma\) give the restart semigroup property in that class.

For arctangent this limit also agrees with the already proved
natural-coordinate IDE.  Indeed, (1.2) and Minkowski's inequality give
finite \(L^p\) moments of \(u(t)\) on compact intervals.  Hence
\(r(t)=u(t)+u(t)^3/3\) lies in \(L^2\), the Banach-valued chain rule gives
\(r'=Q\), and the transformed state satisfies that IDE.  Its established
Gaussian-envelope uniqueness gives the same restart identification.

Finally, \(U\mapsto\langle A,\phi((\Gamma+q)\phi(u))\rangle\) is continuous
on the tube in (3.3).  Indeed, the forward field converges in \(L^2\), and
Cauchy--Schwarz controls the readout.  This proves (8.3). \(\square\)

The order of limits is the required one.  For each \(j\) and each finite
time, first take \(n\to\infty\) for the fixed finite recursion by the
pointed-action theorem.  Only the resulting population states are compared
as \(j\to\infty\).  No finite-width Taylor expansion and no exchange of
width and learning-rate limits occurs.

## 9. Why the arctangent natural coordinate does not prove (1.2)

For arctangent define

\[
 \Theta(u)=u+\frac{u^3}{3},\qquad r=\Theta(u).         \tag{9.1}
\]

At the differential level,

\[
 u'=c(u)Q,\qquad \Theta'(u)=\frac1{c(u)}
\quad\Longrightarrow\quad r'=Q.                      \tag{9.2}
\]

This is the decisive simplification in the proved continuous arctangent
IDE.  For an actual discrete step, however,

\[
 u^+=u+h\,c(u)Q,
\]

and direct cubic algebra gives

\[
\boxed{
 r^+
 =r+hQ
 +h^2\frac{u}{(1+u^2)^2}Q^2
 +\frac{h^3}{3(1+u^2)^3}Q^3.
}                                                       \tag{9.3}
\]

Thus \(r^+=r+hQ\) is an auxiliary Euler discretization of the continuous
IDE, not the transformed actual gradient step.

The proved state estimates give \(Q\in L^2\).  An \(L^4\) bound for \(Q\)
guarantees that the second correction in (9.3) lies in \(L^2\), and an
\(L^6\) bound guarantees the same for the third.  The proved \(L^2\)
control alone guarantees neither statement; special correlations with the
bounded coefficients could still improve integrability.  Every fixed
finite Gaussian program
has these moments, but the available constants depend on its horizon.  The
project explicitly does not assert such a bound uniformly over an
increasing number of program steps.

Consequently, applying the Osgood sewing proof directly to

\[
 E_h(A,r,q)=(A,r,q)+h(Y,Q,B\otimes X)                  \tag{9.4}
\]

would prove convergence of the auxiliary Euler scheme (9.4).  It would not
identify the limit of the actual OMFP maps \(S_h\).  This distinction is the
central audit failure of the otherwise tempting natural-coordinate route.

The same issue persists for a general monotone activation.  A global
coordinate

\[
 \Theta(u)=\int_0^u\frac{d\xi}{\phi'(\xi)}             \tag{9.5}
\]

linearizes the differential equation, but a finite step has nonlinear
Taylor corrections involving powers of \(Q\).  In addition, bounded
\(C^{12}\) data do not ensure that (9.5) is a global \(L^2\) coordinate:

* a normalized sine has zeros of \(\phi'\);
* for
  \[
   \phi(x)=C\int_0^x e^{-s^4}\,ds,
  \]
  the activation is bounded and \(C^\infty\), all its derivatives are
  bounded, and \(\phi'>0\), but
  \[
   \Theta'(x)=C^{-1}e^{x^4},
  \]
  so \(\Theta(G)\notin L^2\) for a standard Gaussian \(G\).

Hence bounded \(C^{12}\) activation assumptions do not ensure the natural
coordinate.  Independently, the estimates currently proved in this project
do not establish the uniform tail bound needed for discrete sewing.

## 10. Exact remaining obligation

The route becomes unconditional if one proves either of the following
restart-stable statements.

### Tail form

For some \(1/2\leq\alpha\leq1\) and every \(T<\infty\), prove (1.2)
uniformly over all positive finite partitions of total mass at most \(T\),
with constants depending only on the activation envelope, \(T\), and the
initial Gaussian moments.

### Response form

Using (3.18), it is sufficient for arctangent to prove

\[
 \sup_{\pi,k}
 \sum_{j<k}h_j|\bar\sigma_{kj}|\leq C_T.              \tag{10.1}
\]

Indeed, \(\chi_k=JB_k\) is Gaussian with variance
\(\|B_k\|_2^2\leq A_T^2\), \(|X_j|\leq a\), the current coefficient
\(\sigma_{kk}\) is bounded by
\(A_T\|\phi''\|_\infty\), and the learned sum in (3.18) is pointwise
bounded by \(aT A_T^2\).  Equation (10.1) would therefore make \(Q_k\)
uniformly sub-Gaussian and imply (1.2) with \(\alpha=1/2\).

The causal identities (3.15) provide the step weights in (10.1), but they
do not bound the normalized coefficients.  Differentiating their
chronological formulas generates coupled source tangents through both
\(\Gamma\) and \(\Gamma^*\).  The available \(L^2\) action bound controls
the resulting vectors only in \(L^2\); products with the adaptive
back-propagated field force higher source derivatives or stronger tails.
No restart-uniform closure of that hierarchy is presently proved.

A weighted Gaussian-Sobolev formulation moves, but does not remove, the
same obligation.  To deduce a subexponential bound from Gaussian
concentration one would need a uniform Cameron--Martin derivative bound for
\(Q_k\).  Differentiating \(Q_k\) differentiates the response coefficients
and the transported queries in (3.18), producing exactly the mixed
forward/transpose tangent hierarchy above.  The fixed \(L^2\) operator
bridge supplies no dimension-free Sobolev operator estimate of this kind.

Therefore:

\[
\boxed{\text{state-level Osgood sewing is proved conditional on (1.2),
but (1.2) is open for the actual OMFP.}}
\]

The obstruction already occurs at depth two.  Any general-depth induction
must first close this depth-two reused-response tail estimate; adding layers
only adds further forward/transpose tangent families.
