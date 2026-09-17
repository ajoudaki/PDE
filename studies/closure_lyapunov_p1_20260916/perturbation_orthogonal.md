# Orthogonal seed: exact transverse-rank criterion

2026-09-16. Frozen independent analytic subtask. No experiments. This is a
study result, not promoted material. Scientific inputs were
`docs/NOTATION.md`, complete `docs/observable_p1.md`, the permitted
state/dynamics/existence material in `docs/global_nonlinear.md` C.4.7.9 and
C.4.7.10 D.3, and complete `three_coordinate_candidate.md`. No other route
report, review, or study history was read.

**Conclusion.** For the orthogonal signed inputs, the evolving actual middle
matrix retains a nonzero component on the two-dimensional standard
representation at every finite auxiliary feature time. The full tangent Gram
has a particularly useful exact decomposition. Its two transverse eigenvalues
are equal, and can vanish only when two explicitly defined current-state
scalars vanish simultaneously. This round does **not** exclude that simultaneous
zero at the fitting endpoint. Initial rank is not used to infer endpoint rank.

## 1. Fixed system and claim

Take the candidate's exact Gaussian population p=1 initialization, normalized
features, physical metric, and full 4-by-7 matrix with its actual transpose.
The label-absorbed directions are (v_i=e_i), so the original data are

\[
 (u_1,u_2,u_3)=(e_1,e_2,-e_3),\qquad (y_1,y_2,y_3)=(1,1,-1).
\]

Write (f_i=f(e_i)), (a_i=a(e_i)), (d_i=d(e_i)),

\[
 z_i=b_2^TMa_i,\quad H_i=\tanh z_i,\quad
 Q_i=b_1^TM^Td_i,\qquad F=\tfrac13\sum_i f_i.
\]

The auxiliary curve is the candidate's exact (X_s=\nabla F), not a changed
physical optimizer. In particular

\[
 c_s=\tfrac13\sum_i H_i,\quad
 M_s=\tfrac13\sum_i d_i a_i^T,\quad
 (w_i)_s=\tfrac13\operatorname{sech}^2(w_i)Q_i.       \tag{1}
\]

The candidate proves global existence at finite (s), permutation invariance,
simultaneous mark-negation invariance, and

\[
 C(s):=E_2[(H_1+H_2+H_3)^2/9]\ge C_0>0.             \tag{2}
\]

It identifies the physical fitting endpoint with a finite (s_*>0), where

\[
 F(s_*)=1,\qquad s_*\le C_0^{-1}.
\]

All statements below concern that exact curve. No finite population rule,
learned-network identification, or rotation of the fixed dictionary is used.

## 2. Full tangent Gram and the orthogonal first-layer contribution

Define the unweighted prediction tangent Gram

\[
 \mathcal G_{ij}=\langle\nabla f_i,\nabla f_j\rangle.
\]

The metric and gradient are exactly those of the candidate:

\[
 \nabla_c f_i=H_i,\quad \nabla_M f_i=d_i a_i^T,\quad
 \nabla_w f_i=\operatorname{sech}^2(w_i)Q_i e_i.
\]

The first-layer gradients for different inputs are orthogonal because their
vector coordinates are different. Hence

\[
 \mathcal G_{ij}
 =E_2[H_iH_j]+(d_i^Td_j)(a_i^Ta_j)
   +\mathbf1_{i=j}E_1[\operatorname{sech}^4(w_i)Q_i^2]. \tag{3}
\]

Permutation invariance gives a common diagonal, common off-diagonal, and a
common last term (R(s)). Thus the eigenvalue on

\[
 \mathbf1^\perp=\{t\in\mathbb R^3:t_1+t_2+t_3=0\}
\]

has multiplicity two and equals

\[
 \begin{split}
 \lambda_\perp
 &=\tfrac12 E_2[(H_1-H_2)^2]
   +\tfrac12\|d_1a_1^T-d_2a_2^T\|_F^2+R,\\
 R&=E_1[\operatorname{sech}^4(w_1)Q_1^2].             \tag{4}
 \end{split}
\]

The eigenvalue on the span of (mathbf1) is

\[
 \lambda_\parallel=3\|\nabla F\|^2\ge3C_0.           \tag{5}
\]

For (4), use

\[
 \lambda_\perp=\tfrac12\|\nabla f_1-\nabla f_2\|^2
\]

and add the squared norms in the three mutually orthogonal metric blocks.
For (5), expand (\|\sum_i\nabla f_i/3\|^2).
The sign change of the original third prediction conjugates the Gram by
\(\operatorname{diag}(1,1,-1)\), preserving its eigenvalues.

## 3. Exact permutation blocks of both hidden layers

Simultaneous negation of all lower marks leaves (w) odd, and simultaneous
negation of all upper marks leaves (c) odd. Thus all constant components of

\[
 a_i,\ d_i,\ M
\]

vanish along the initialized curve. Delete those inactive components solely
for notation. This leaves (a_i\in\mathbb R^6), (d_i\in\mathbb R^3),
and (M=[M_h\ M_k]\in\mathbb R^{3\times6}); every active entry still evolves.

Put

\[
 P_\parallel=\tfrac13\mathbf1\mathbf1^T,
 \qquad P_\perp=I-P_\parallel,
\]

and arrange the columns (a_i) into two 3-by-3 blocks (A_h,A_k).
Permutation equivariance forces each block to have constant diagonal and
constant off-diagonal. Equivalently,

\[
 \begin{array}{ll}
 A_h=a_{h\perp}P_\perp+a_{h\parallel}P_\parallel,&
 A_k=a_{k\perp}P_\perp+a_{k\parallel}P_\parallel,\\
 M_h=m_{h\perp}P_\perp+m_{h\parallel}P_\parallel,&
 M_k=m_{k\perp}P_\perp+m_{k\parallel}P_\parallel.
 \end{array}                                                    \tag{6}
\]

Write the resulting two-vectors as (a_\perp,a_\parallel,m_\perp,m_\parallel),
and define

\[
 \theta_\perp=m_\perp^Ta_\perp,\qquad
 \theta_\parallel=m_\parallel^Ta_\parallel.            \tag{7}
\]

These are contractions of the actual evolving matrix and current lower
features. With the candidate's (Z_i=\tanh\Xi_i) and

\[
 R_Z=\sqrt{\tau+\eta},\qquad S=Z_1+Z_2+Z_3,
\]

the exact upper preactivations are

\[
 z_i=\frac1{R_Z}
       \left[\theta_\perp(Z_i-S/3)+\theta_\parallel S/3\right]. \tag{8}
\]

The upper mark law has a positive density on ((-1,1)^3). Since tanh is
injective and (Z_1-Z_2\ne0) almost surely,

\[
 E_2[(H_1-H_2)^2]=0\quad\Longleftrightarrow\quad
 \theta_\perp=0.                                      \tag{9}
\]

Arrange the (d_i) as columns of a matrix and write

\[
 [d_1\ d_2\ d_3]
       =d_\perp P_\perp+d_\parallel P_\parallel.        \tag{10}
\]

At a time when (\theta_\perp=0), all upper fields coincide, hence

\[
 d_\perp=0,\quad d_i=(d_\parallel/3)\mathbf1,\quad
 d_\parallel=\frac1{R_Z}
 E_2\!\left[S c\operatorname{sech}^2
      \left(\frac{\theta_\parallel S}{3R_Z}\right)\right]. \tag{11}
\]

The last identity follows by summing the three equal coordinates of (d_i).

## 4. Exact criterion for full transverse degeneracy

For every finite feature time on the initialized orthogonal curve,

\[
 \boxed{\lambda_\perp(s)=0
 \quad\Longleftrightarrow\quad
 \theta_\perp(s)=0\ \hbox{and}\ d_\parallel(s)=0.}       \tag{12}
\]

Here (d_\parallel) is always defined by (10); formula (11) evaluates it on
the only locus where its value matters for (12).

Proof: If (\lambda_\perp=0), each nonnegative term in (4) is zero.
Equation (9) gives (\theta_\perp=0). Then (2) and (8) imply

\[
 \theta_\parallel\ne0,\qquad m_\parallel\ne0.          \tag{13}
\]

By (11),

\[
 Q_i=\frac{d_\parallel}{3}
    \left(m_{h\parallel}\sum_j b_{1,h_j}
          +m_{k\parallel}\sum_j b_{1,k_j}\right).       \tag{14}
\]

The six active lower normalized features are linearly independent in (L^2).
To check this without a numerical eigenvalue: the normalization is invertible;
in a linear combination of raw (h_j,k_j), condition on all (G_j).
Each (k_j=\tanh(\zeta_j+\alpha h_j)) has positive conditional variance,
and the reverse noises are independent. Thus all coefficients of (k_j)
must vanish. Independence and positive variance of the (h_j) then force
their coefficients to vanish. Consequently (13) makes the parenthesized
field in (14) nonzero in (L^2).

Every (w_i) is finite almost surely at finite (s), and sech is strictly
positive on finite real numbers. Therefore (R=0) in (4) forces

\[
 Q_i=0\text{ a.s.},\qquad d_\parallel=0.
\]

Conversely, (\theta_\perp=d_\parallel=0) gives identical (H_i) and

\[
 d_i=0,\quad Q_i=0,
\]

so every term in (4) vanishes. This proves (12).

The distinction is substantive: upper-feature coincidence alone does not
destroy full tangent rank. The first layer protects both transverse directions
whenever the scalar upper derivative correlation in (11) remains nonzero.

## 5. The actual middle matrix cannot lose its transverse component

Let (g(z)=\operatorname{sech}^2z). Permuting upper coordinates 1 and 2 leaves

\[
 c\quad\hbox{unchanged},\qquad z_1\leftrightarrow z_2.
\]

Consequently

\[
 \begin{split}
 d_\perp
 &=\frac1{2R_Z}E_2[(Z_1-Z_2)c(g(z_1)-g(z_2))]\\
 &=\theta_\perp\,\rho(s),\\
 \rho(s)&=\frac1{2R_Z^2}E_2\!\left[
   (Z_1-Z_2)^2c\int_0^1
   g'(z_2+t(z_1-z_2))\,dt\right].                    \tag{15}
 \end{split}
\]

This formula defines (\rho) continuously even when (\theta_\perp=0).
Since (|g'|\le2), (|Z_1-Z_2|\le2), and (|c(s)|_\infty\le s),

\[
 |\rho(s)|\le4s/R_Z^2.                               \tag{16}
\]

The exact matrix equation (1), evaluated in (6), gives

\[
 (m_\perp)_s=\tfrac13d_\perp a_\perp
    =\tfrac13\rho(s)a_\perp a_\perp^Tm_\perp.        \tag{17}
\]

At initialization (m_\perp) consists of the two strictly positive bands of
the prescribed (D), including its reverse-response term. It is nonzero.
The linear equation (17) cannot take a nonzero vector to zero at finite time.
Explicitly, with (B(s)=\rho(s)a_\perp a_\perp^T/3),

\[
 \frac d{ds}|m_\perp|^2
    \ge-2\|B(s)\|_{\rm op}|m_\perp|^2.
\]

Multiplying by (\exp(2\int_0^s\|B(t)\|_{\rm op}\,dt)) and integrating
gives

\[
 |m_\perp(s)|\ge |m_\perp(0)|
     \exp\left(-\int_0^s\|B(t)\|_{\rm op}\,dt\right)>0. \tag{18}
\]

The integral is finite on each compact interval: (16) holds and the bounded
features make (a_\perp) bounded. No sign for (\rho) is assumed.
Equation (18) protects the actual matrix component, but does not protect its
scalar projection (m_\perp^Ta_\perp).

## 6. Exact first-layer transform

Define the scalar increasing bijection

\[
 T(x)=\frac x2+\frac{\sinh(2x)}4,\qquad T'(x)=\cosh^2x.
\]

The orthogonal row equations (1) give, without approximation,

\[
 T(w_i(s))=T(G_i)+b_1^T\ell_i(s),\qquad
 \ell_i(s)=\tfrac13\int_0^sM(t)^Td_i(t)\,dt.           \tag{19}
\]

This identity uses a proof variable; no history is being supplied to the
autonomous closure. Differentiating the current lower feature coefficients
instead gives a wholly current-state identity:

\[
 (a_i)_s=\tfrac13 B_iM^Td_i,\qquad
 B_i=E_1[b_1b_1^T\operatorname{sech}^4(w_i)].          \tag{20}
\]

Every (B_i) is positive definite on the active six-dimensional feature
space: for nonzero (v), linear independence gives (b_1^Tv\ne0) on a set
of positive measure and the gate there is strictly positive. The integrands
are bounded, so all differentiations are justified by dominated convergence.

Equations (17),(19),(20) expose the remaining coupling. Common-mode motion of
the first layer can change (a_\perp), even when (d_\perp=0). Neither
invertibility of (T), positivity of (B_i), nor nonvanishing of (m_\perp)
alone proves that (m_\perp^Ta_\perp) cannot be zero.

## 7. Why a reachability argument is still necessary

There exist bounded, permutation-invariant, odd, fitting states of this exact
architecture with a full-row-rank actual (M) but rank-one tangent Gram.
They are **not** asserted to be reachable from the prescribed initialization.

Here is an explicit check. Set (w=g), and write its lower coefficient blocks
as (A_h=a_hI,A_k=a_kI), where

\[
 a_h=v/R_h>0,\qquad
 a_k=\frac{\beta\eta}{(v+\eta)R_k}>0.
\]

Fix (k>0) and choose

\[
 M_h=\frac{kR_Z}{a_h}\mathbf1\mathbf1^T+a_kP_\perp,
 \qquad M_k=-a_hP_\perp.                              \tag{21}
\]

Then (m_\perp=(a_k,-a_h)\ne0), the parallel component is nonzero, and

\[
 z_i=kS\quad\hbox{for all }i.
\]

Thus the full 3-by-6 active matrix has row rank three, despite coincident upper
features. Let

\[
 H=\tanh(kS),\qquad J=S\operatorname{sech}^2(kS),
 \qquad V=H-\frac{E_2[HJ]}{E_2[J^2]}J,
 \qquad c=\frac{V}{E_2[V^2]}.                         \tag{22}
\]

Both denominators are positive. The law of (S) has positive density on
\((-3,3)\), while

\[
 H/J=\sinh(2kS)/(2S)
\]

is not constant on any interval. Hence (H,J) are linearly independent and

\[
 E_2[cH]=1,\qquad E_2[cJ]=0.
\]

The resulting (c) is bounded, symmetric under permutations, and odd.
Exchangeability gives

\[
 E_2[Z_jc\operatorname{sech}^2(kS)]
   =\tfrac13E_2[cJ]=0,
\]

so all (d_i,Q_i) vanish. Every hidden gradient is zero, every readout gradient
equals (H), and the tangent Gram has rank one. This example defeats an
argument from architectural symmetry, fitting, and middle-matrix rank alone.
It is not a counterexample to rank preservation on the initialized curve.

## 8. Exact remaining obligation and perturbation use

Endpoint coercivity is now the precise unproved statement

\[
 (\theta_\perp(s_*),d_\parallel(s_*))\ne(0,0).         \tag{23}
\]

Coercivity on every finite auxiliary interval requires the same exclusion at
every (s). If the pair avoids zero on a fixed compact interval, continuity
and (4) give a strictly positive minimum transverse eigenvalue there. If it
avoids zero at (s_*), continuity gives endpoint-neighborhood coercivity.
Neither conclusion follows merely from the initialized rank-three result.

At initialization (c=0), while (8) has

\[
 \theta_\perp(0)=R_Z\kappa(1)>0.
\]

Thus initial positivity and a short interval of positivity are proved. The
candidate's finite endpoint is not shown to lie in that short interval.

For a potential intended to control perturbations away from the equal signed
predictions, (4) identifies the three current mechanisms that matter: upper
feature separation, middle-gradient separation, and first-layer sensitivity.
The common prediction potential only controls the parallel mode (5). A new
argument must control the simultaneous-zero obstruction (23), or control the
transverse residual through a different mechanism. This report supplies no
generic perturbation theorem, global transverse lower bound, or completed new
Lyapunov potential.
