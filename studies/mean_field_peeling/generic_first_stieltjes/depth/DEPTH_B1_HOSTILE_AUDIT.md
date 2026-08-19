# Hostile audit of the arbitrary fixed-depth, one-sample GNF

**Audit date:** 2026-08-18

**Object audited:** [DEPTH_B1_GAUSSIAN_RECURSION.md](./DEPTH_B1_GAUSSIAN_RECURSION.md)

**Verdict:** **PASS for every fixed hidden depth \(H\) at \(B=1\)** under the
polynomially-smooth activation envelope stated in the theorem. No missing
matrix-reuse response, fresh covariance, parity branch, \(q_0\) factor, or
terminal Hessian block was found. The initially incorrect \(H=2\)
\((\Gamma,\Omega,\Lambda)\) scaling dictionary was corrected during this
audit. The preferred scalar recurrence is a genuine \(O(H)\)-transition
Gaussian-normal-form evaluator; this statement does not concern the size of
a completely flattened symbolic polynomial.

This audit was intentionally independent in two ways. First, the
four-Gaussian proof IR was contracted by hand to a different scalar
recurrence using only one-dimensional activation atoms. Second, that
recurrence was compared both with the proof-IR implementation and with the
exact finite-width moving-flow compiler.

## 1. Claim and normalization under audit

For

\[
 f_n=n^{-1}a^Tx^H,\qquad D_n=n\nabla f_n\mathbin{\cdot}\nabla,
\]

the two requested deterministic limits are

\[
 A_H=\lim_{n\to\infty}D_nf_n,\qquad
 C_H=\lim_{n\to\infty}D_n^3f_n.
\]

Let \(v=n\nabla f_n\), let
\(\widehat f_n(t)=f_n(\theta+tv)\) be the frozen line, and put

\[
 T_{n,H}=\widehat f_n'''(0),\qquad
 \mathcal H_{n,H}=n\|\nabla^2f_n\,v\|^2.
\]

Direct differentiation, before any width limit, gives

\[
 \boxed{D_n^3f_n=2T_{n,H}+4\mathcal H_{n,H}.}
\]

The factors \(2\) and \(4\) are correct. In raw derivatives,
\(T_{n,H}=\nabla^3f_n[v,v,v]\) and
\(\mathcal H_{n,H}=n\|(\nabla^2f_n)v\|^2\); differentiating
\(D_n^2f_n=2n^2\nabla f_n^T(\nabla^2f_n)\nabla f_n\) produces exactly the
displayed identity.

## 2. Raw-matrix chronology and response completeness

For each hidden matrix \(A^\ell=W^\ell/\sqrt n\), the actual use order is

1. the base forward use \(A^\ell X_{\ell-1}^{[0]}\);
2. the base transpose use \((A^\ell)^T\Delta_\ell\);
3. the three frozen forward uses
   \(A^\ell X_{\ell-1}^{[r]}\), \(r=1,2,3\);
4. the differentiated transpose use
   \((A^\ell)^T\widetilde\Delta_\ell\).

The low-rank terms containing \(\dot A^\ell\) are explicit products, not new
uses of the raw Gaussian matrix. Applying the transpose rule in this order
gives the following exhaustive ledger.

| Use | Fresh part | All required response/direct parts |
|---|---|---|
| base forward | \(F_{\ell0}\) | none |
| base transpose | \(R_{\ell-1}\), variance \(p_\ell\) | \(X_{\ell-1}^{[0]}\mathbb E[\partial_{Z_\ell}\Delta_\ell]=0\) |
| frozen forward \(r\) | \(F_{\ell r}\) | \(a^{\ell-1}_r\Delta_\ell+rG^{\ell-1}_{0,r-1}\Delta_\ell\) |
| differentiated transpose | \(E_{\ell-1}\), variance \(\beta_\ell\) | \(p_\ell X_{\ell-1}^{[0]}+\sum_{r=0}^3\rho_{\ell r}X_{\ell-1}^{[r]}\) |

The two pieces of

\[
 \lambda_{\ell r}=a^{\ell-1}_r+rG^{\ell-1}_{0,r-1}
\]

have different origins and both are necessary: the first is the response to
the earlier transpose use, while the second is the literal derivative of
\(A^\ell(t)X_{\ell-1}(t)\). The differentiated transpose sees all four
earlier forward uses, so its sum over \(r=0,1,2,3\) is complete.

The fresh forward block has covariance \(G^{\ell-1}\). The new transpose
innovation has covariance \(\beta_\ell\), and its possible fresh covariance
with the earlier base transpose innovation is
\(\mathbb E[\Delta_\ell\widetilde\Delta_\ell]\). Section 3 proves that this
last scalar is zero. Thus there is no omitted correlated innovation.

## 3. Parity audit

Negate every base reverse carrier and every odd fresh forward coordinate:

\[
 R_\ell\mapsto-R_\ell,\qquad
 F_{\ell r}\mapsto(-1)^rF_{\ell r}.
\]

Induction through the scalar chain rule gives

\[
 Z_\ell^{[r]},X_\ell^{[r]}\mapsto
 (-1)^r Z_\ell^{[r]},(-1)^rX_\ell^{[r]}.
\]

Consequently

\[
 G^\ell_{rs}=0\quad(r+s\ {\rm odd}),\qquad
 a^\ell_r=0\quad(r\ {\rm even}).
\]

The differentiated reverse carrier and source are even under the same
transformation. Hence

\[
 \mathbb E[\Delta_\ell\widetilde\Delta_\ell]=0,\qquad
 \rho_{\ell1}=0.
\]

The remaining \(\rho_{\ell2}\) and \(\rho_{\ell3}\) vanish structurally:
after the top-down induction, \(\widetilde R_\ell\) depends locally only on
\(F_{\ell0}\), and (5.2) uses \(F_{\ell1}\) only through
\(Z_\ell^{[1]}\). Therefore

\[
 \widetilde R_{\ell-1}=E_{\ell-1}
   +(p_\ell+\rho_{\ell0})X_{\ell-1}^{[0]}
\]

contains every nonzero branch. These are symmetry statements about the
joint program, not one-copy mean-zero shortcuts.

## 4. Independent contraction to one-dimensional atoms

The strongest closure check is that the four-dimensional proof IR can be
eliminated analytically. For
\(Z_\ell\sim N(0,q_{\ell-1})\), write
\(\langle r_1,\ldots,r_k\rangle_\ell=\mathbb E\prod_i
\phi^{(r_i)}(Z_\ell)\). Besides
\(q_\ell=\langle0,0\rangle_\ell\) and
\(d_\ell=\langle1,1\rangle_\ell\), only the following distinct local atoms
are needed:

\[
\begin{gathered}
 \langle1,1,1,1\rangle,\quad \langle0,2\rangle,\quad
 \langle0,2,1,1\rangle,\quad \langle3,1\rangle,\quad
 \langle2,2\rangle,\\
 \langle3,1,1,1\rangle,\quad \langle2,2,1,1\rangle,\quad
 \langle0,0,1,1\rangle.
\end{gathered}
\]

Thus there are ten distinct one-dimensional atom types per layer including
\(q_\ell,d_\ell\), and no activation derivative above order three appears
in this contracted form.

Set

\[
 V_\ell=G^\ell_{11},\qquad M_\ell=G^\ell_{02},\qquad
 J_\ell=a^\ell_3.
\]

With the semantic atom names of equations (7.3) in the audited note, the
independently derived bottom-up recurrence is

\[
 V_1=q_0^2b_1u_1,\qquad
 M_1=q_0^2b_1m_1,\qquad
 J_1=3q_0^3b_1j_1,
\]

\[
 V_\ell=d_\ell V_{\ell-1}
 +\Theta_{\ell-1}^2b_\ell u_\ell,
\]

\[
 M_\ell=v_\ell V_{\ell-1}
 +\Theta_{\ell-1}^2b_\ell m_\ell
 +(d_\ell+v_\ell)M_{\ell-1},
\]

\[
\begin{aligned}
 J_\ell={}&3\Theta_{\ell-1}V_{\ell-1}r_\ell
 +3\Theta_{\ell-1}^3b_\ell j_\ell\\
 &+3\Theta_{\ell-1}M_{\ell-1}(r_\ell+s_\ell)
 +(J_{\ell-1}+3M_{\ell-1})d_\ell.
\end{aligned}
\]

In particular, \(T_H=J_H+3M_H\). The terms follow by integrating the
fresh \(F_{\ell1}\) variance and applying the one-dimensional Stein identity
to the sole correlation
\(\operatorname{Cov}(F_{\ell0},F_{\ell2})=M_{\ell-1}\).

For the top-down contraction, initialize
\(\beta_{H+1}=0,\chi_{H+1}=1,V_0=0\). Direct Gaussian contraction gives

\[
\begin{aligned}
 \beta_\ell={}&b_\ell V_{\ell-1}s_\ell
 +3\Theta_{\ell-1}^2b_\ell^2e_\ell
 +d_\ell\beta_{\ell+1}\\
 &+\chi_{\ell+1}^2h_\ell
 +2\Theta_{\ell-1}\chi_{\ell+1}b_\ell w_\ell,
\end{aligned}
\]

\[
 \rho_{\ell0}=\Theta_{\ell-1}b_\ell(r_\ell+s_\ell)
 +\chi_{\ell+1}(v_\ell+d_\ell),\qquad
 \chi_\ell=p_\ell+\rho_{\ell0}.
\]

The factor \(3\) in the second term of \(\beta_\ell\) is
\(\mathbb E R_\ell^4=3b_\ell^2\); the last term is the only surviving cross
contraction. These equations agree term by term with the promoted recurrence
(7.3)--(7.12).

Finally,

\[
 \mathcal H_H=V_H+q_0\beta_1+\sum_{\ell=2}^H
 \left(q_{\ell-1}\beta_\ell+p_\ell V_{\ell-1}\right),\qquad
 \boxed{C_H=2T_H+4\mathcal H_H}.
\]

This proves genuine closure: after the NNGP/NTK and base reverse passes,
each layer transition uses a fixed number of scalar atoms and arithmetic
operations. Evaluation requires \(O(H)\) Gaussian-oracle calls and
\(O(H)\) stored scalars. A flat expansion into a single monomial list need
not have \(O(H)\) size and is not claimed to do so.

The independent evaluator is
[gnf_audit_reference.py](./gnf_audit_reference.py). It does not call or
reimplement the four-Gaussian quadrature in
[gnf_recursion.py](./gnf_recursion.py).

## 5. Terminal Hessian factorization

Differentiating each raw gradient along the frozen direction gives:

\[
 \mathcal H_a=G^H_{11},\qquad
 \mathcal H_{W^1}=q_0\beta_1,
\]

\[
 \mathcal H_{W^\ell}=q_{\ell-1}\beta_\ell
 +p_\ell G^{\ell-1}_{11}\quad(2\leq\ell\leq H).
\]

Before parity, the last line also contains

\[
 2\mathbb E[\Delta_\ell\widetilde\Delta_\ell]
 G^{\ell-1}_{01}.
\]

Both factors vanish independently by the parity certificate. There are no
cross terms between different parameter blocks because the squared Euclidean
norm is the direct sum of their block norms. The first-layer factor is
\(q_0\), rather than \(q_1\), because its raw gradient is contracted against
the original input. The readout factor has no extra \(q_H\), because its
directional derivative is \(X_H^{[1]}/n\). All normalizations therefore
agree with the finite-width identity.

## 6. Exact \(H=1\) and \(H=2\) gates

### \(H=1\)

Independent raw ODE differentiation gives

\[
\begin{aligned}
 C_1=\mathbb E[&4q_0^2\phi'^4+4q_0\phi^2\phi'^2
 +14q_0^2\phi\phi''\phi'^2\\
 &+12q_0^3\phi''^2\phi'^2
 +6q_0^3\phi'''\phi'^3](U),\qquad U\sim N(0,q_0),
\end{aligned}
\]

which is exactly the recurrence specialization. The reproducible
Gauss--Hermite/finite-width controls in
[audit_h1_control.py](./audit_h1_control.py) are:

| activation | \(q_0\) | Gaussian target | finite-width mean \(\pm\) SE |
|---|---:|---:|---:|
| \(x^2\) | 0.7 | 230.496 | \(229.430674\pm0.674395\) |
| \(\sin x\) | 1.3 | -1.6587969566 | \(-1.6585836362\pm0.0085675\) |
| \(\tanh x\) | 0.9 | -0.6703534507 | \(-0.6755387230\pm0.0054959\) |

### \(H=2\)

The correct accepted-variable dictionary is

\[
 (F_{20},F_{21},F_{22},F_{23})
 =(Z,q_0\Gamma,q_0^2\Omega,q_0^3\Lambda).
\]

The draft initially omitted the three powers of \(q_0\); this was a real
local error and is now fixed. With

\[
\begin{gathered}
 b_1=d_2,\quad \Theta_1=q_1+q_0d_1=c,\\
 V_1=q_0^2d_2e_1,\quad M_1=q_0^2d_2m_1,\quad
 J_1=3q_0^3d_2j_1,
\end{gathered}
\]

the third-response coefficient is
\(J_1+3M_1=\kappa\). The reverse contraction gives

\[
 \beta_2=\tau,\qquad \rho_{20}=\alpha,\qquad
 \chi_2=d_2+\alpha=k.
\]

Therefore \(T_2=S_\star\),
\(\mathcal H_2=H_\star\), and
\(C_2=2S_\star+4H_\star\), atom by atom. The independent contracted
evaluator agrees separately on \((A,T,\mathcal H,C)\) with the accepted
normal form for constant, linear, affine, quadratic, cubic, sine, and tanh.
The executable comparisons use nonunit \(q_0\) in every family, so the
agreement does not hide the corrected scaling at \(q_0=1\).
For the quadratic gate at \(q_0=1\), the exact values are

\[
 (A,T,\mathcal H,C)=(111,92232,375180,1685184).
\]

## 7. Deep-linear and nonlinear deep controls

For \(\phi(x)=x\), an independent raw-factor count gives

\[
 A_H=(H+1)q_0,\qquad T_H=0,\qquad
 C_H=\frac23H(H+1)^2(H+2)q_0^2.
\]

Thus \(C_H/q_0^2=8,48,160,400\) for \(H=1,2,3,4\). Both independent
recurrences reproduce these values exactly. The blockwise \(H=3\) limiting
contributions are \((48,32,32,48)q_0^2\), summing to \(160q_0^2\); this
catches a reversed layer index or a missing first/readout block.

The cross-test in
[test_gnf_audit_reference.py](./test_gnf_audit_reference.py) compares the
independent scalar contraction with the proof-IR evaluator through \(H=4\)
for a degenerate \(q_0=0\) affine case and for nondegenerate affine,
quadratic, cubic, sine, and tanh cases. It compares \(A,T,\mathcal H,C\),
all base variances, \(V_\ell,M_\ell,J_\ell\), every \(\beta_\ell,\chi_\ell\),
and every surviving \(\lambda_{\ell r}\). The observed normalized
discrepancies are at quadrature roundoff scale.

For a genuinely nonlinear depth-three gate, the independent recurrence gives

\[
 \phi(x)=\sin x,\quad q_0=1,\quad H=3:\qquad
 (A,T,\mathcal H,C)
 =(1,-6.64022220860,2.43819077139,-3.52768133164).
\]

The exact finite-width moving-flow compiler produced:

| width \(n\) | seeds | mean \(D_n^3f_n\) | SE | \(z\) from target |
|---:|---:|---:|---:|---:|
| 64 | 4000 | -3.652191599 | 0.06982948 | -1.78 |
| 128 | 3000 | -3.582604668 | 0.05280787 | -1.04 |
| 256 | 1200 | -3.568017978 | 0.05689574 | -0.71 |
| 512 | 220 | -3.613915098 | 0.09410781 | -0.92 |

Every width is individually consistent with the prediction. A weighted
affine fit in \(1/n\) has intercept
\(-3.55595293\pm0.06098463\), only \(0.46\) standard errors from the target,
with \(\chi^2/{\rm dof}=0.197\). The exact reproducer is
[audit_h3_nonlinear.py](./audit_h3_nonlinear.py); it obtains its target from
the independent scalar contraction and its samples from the separately
raw-coordinate-audited finite-width compiler.

## 8. Physical one-label loss map

For \(L_n=(y_\star-f_n)^2\) and
\(\dot\theta=2\eta(y_\star-f_n)n\nabla f_n\), direct finite-width product
rules give

\[
\begin{aligned}
 L_n'''={}&-64\eta^3r_n^2K_n^3
 +112\eta^3r_n^3K_nJ_n
 -16\eta^3r_n^4C_n,
\end{aligned}
\]

where \(r_n=y_\star-f_n\), \(K_n=D_nf_n\), and \(J_n=D_n^2f_n\). The
coefficient \(112=64+48\) is correct. Under readout sign flip,
\((f,K,J,C)\mapsto(-f,K,-J,C)\). The terms in
\(r_n^3K_nJ_n\) without a vanishing factor \(f_n\) are exactly odd; the
remaining terms vanish in \(L^1\) because \(f_n\to0\) in every finite
\(L^p\). This validates the scalar-label Taylor coefficient

\[
 -\frac{32}{3}\eta^3y_\star^2A_H^3
 -\frac83\eta^3y_\star^4C_H.
\]

No positive-time loss convergence is implied.

## 9. Probability and regularity boundary

There are three different regularity levels and they must not be conflated.

1. The finite-width derivative identities and the displayed contracted
   algebra use only \(\phi,\phi',\phi'',\phi'''\), together with finiteness of
   the displayed Gaussian moments.
2. The almost-sure recurrent Gaussian/transpose limit can be obtained for an
   appropriate finite-program pseudo-Lipschitz envelope, including singular
   limiting Grams; no covariance inverse or rank-stability assumption is
   used here.
3. The stated almost-sure and every-finite-\(L^p\) theorem, and hence the
   annealed limit \(\mathbb E D_n^3f_n\to C_H\), uses the stronger assumption
   \(\phi\in C^\infty\) with every derivative polynomially bounded. This is
   the polynomial-smooth hypothesis of Non-Gaussian Tensor Programs,
   Theorem 3.7.

Merely assuming \(C^3\) and polynomial growth through order three is not
enough to invoke that all-\(L^p\) theorem. A separate uniform-integrability
or approximation argument would be needed for the annealed claim in that
weaker class. This is the same boundary proved in
[PROBABILISTIC_BRIDGE_AUDIT.md](../PROBABILISTIC_BRIDGE_AUDIT.md).

For fixed \(H\), the exact jet is a finite NETSOR\({}^T+\) program with
reused matrices and transposes, moment scalars, and polynomially-smooth
coordinate maps. Adding finitely many layers changes only the finite program
length, so the theorem applies separately to each fixed \(H\). Degenerate
activation Grams are allowed; the \(q_0=0\) executable gates exercise this
boundary.

## 10. Exact nonclaims and final claim ledger

| Claim | Audit status |
|---|---|
| finite-width \(D_n^3f_n=2T+4\mathcal H\) | **Pass** |
| every \(A/A^T\) response direction at fixed \(H,B=1\) | **Pass** |
| fresh covariance and parity-zero ledger | **Pass** |
| terminal Hessian factorization and every \(q_0\) factor | **Pass** |
| literal one-dimensional-atom recurrence | **Pass** |
| genuine \(O(H)\) oracle-transition evaluation | **Pass** |
| atomwise accepted \(H=2\) reduction | **Pass after the documented scaling fix** |
| deep-linear \(H=1,2,3,4\) controls | **Pass** |
| nonlinear \(H=3\) finite-width control | **Pass** |
| fixed-\(H\) annealed theorem under all-orders polynomial smoothness | **Pass** |
| annealed theorem under only \(C^3\)+finite-order polynomial growth | **Open** |
| flat symbolic atom count \(O(H)\) | **Not claimed** |
| depth \(H=H(n)\) growing with width | **Open** |
| depth-uniform constants, error bounds, or numerical conditioning | **Open** |
| arbitrary fixed batch \(B>1\) together with arbitrary fixed \(H\) | **Open in this audit** |
| fixed positive training time | **Not claimed** |

The fixed-\(H\), \(B=1\) Gaussian normal form is therefore fully audited at
the stated theorem level. The contracted scalar recurrence, rather than the
four-Gaussian proof IR, is the preferred computational presentation.
