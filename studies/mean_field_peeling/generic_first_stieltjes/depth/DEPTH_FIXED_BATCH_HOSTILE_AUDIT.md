# Hostile audit of the joint fixed-depth/fixed-batch GNF

**Audit date:** 2026-08-18

**Primary object:**
[DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md](./DEPTH_FIXED_BATCH_GAUSSIAN_RECURSION.md)

**Verdict:** **PASS for every separately fixed hidden depth \(H\geq1\) and
batch size \(B\geq1\)** under the polynomially-smooth activation envelope
stated in the primary note. The joint recursion is promoted to a theorem at
that scope. I found no omitted \(A/A^T\) response, reversed
batch index, missing fresh covariance, invalid parity cancellation, or
missing terminal Hessian block.

This verdict does not cover \(H=H(n)\), \(B=B(n)\), a fixed positive training
time, a sign or Stieltjes-moment interpretation of the correction, or an
annealed theorem under only finite-order activation regularity.

The audit was independent in three ways.

1. I reconstructed the matrix-use chronology and response rules from the
   exact finite-width frozen-line/Hessian identity before comparing them with
   either joint note.
2. I checked both accepted axes blockwise: \(H=2\) at arbitrary fixed batch,
   and \(B=1\) through \(H=4\).
3. I added a genuinely joint finite-width experiment at \(H=3,B=2\). Its
   frozen-line third derivative is computed by a new ordinary-series route,
   checked at width one against raw third-derivative tensors, and kept
   separate from the Gaussian recursion.

## 1. Finite-width source and complete matrix chronology

For \(v_c=n\nabla g_c\), direct differentiation gives, before taking a width
limit,

\[
 D_c^3g_c=2T_{n,H,c}+4\mathcal H_{n,H,c},
 \qquad
 T_{n,H,c}=\nabla^3g_c[v_c,v_c,v_c],
 \qquad
 \mathcal H_{n,H,c}=n\|\nabla^2g_c\,v_c\|^2.
\]

The factors \(2\) and \(4\) are correct. For each
\(A^\ell=W^\ell/\sqrt n\), \(2\leq\ell\leq H\), the actual program order is:

1. \(A^\ell X_{\ell-1}^{[0]}\), the base forward use;
2. \((A^\ell)^T\Delta_\ell\), the base reverse use;
3. \(A^\ell X_{\ell-1}^{[r]}\), \(r=1,2,3\), the frozen forward uses;
4. \((A^\ell)^T\widetilde\Delta_\ell\), the differentiated reverse use.

The low-rank direction

\[
 \dot A^\ell=n^{-1}\Delta_\ell(X_{\ell-1}^{[0]})^T
\]

is an explicit empirical outer product, not another raw-matrix use. It
produces exactly the two direct terms

\[
 r\dot A^\ell X_{\ell-1}^{[r-1]}
 \longrightarrow
 r\Delta_\ell G_{\ell-1}^{0,r-1},
 \qquad
 (\dot A^\ell)^T\Delta_\ell
 \longrightarrow
 X_{\ell-1}^{[0]}\mathsf P_\ell.
\]

Applying the transpose master rule in the displayed order yields the
following exhaustive ledger.

| raw-matrix use | fresh covariance | every opposite-orientation response |
|---|---|---|
| base transpose | \(\mathsf P_\ell\) | \(X^{[0]}\mathbb E[\partial\Delta/\partial F^0]=0\) |
| frozen forward \(r\) | \(G_{\ell-1}^{rs}\) jointly over \(r,s=0,\ldots,3\) | \(\Delta_\ell J_{\ell-1}^r\) |
| differentiated transpose | \(\boldsymbol\beta_\ell\), jointly with the base innovation through \(S_\ell\) | \(\sum_{r=0}^3X_{\ell-1}^{[r]}\rho_\ell^r\) |

Consequently the fragile forward orientation is

\[
 \boxed{
 Z_\ell^{[r]}=F_\ell^r+\Delta_\ell
 \left(J_{\ell-1}^r+rG_{\ell-1}^{0,r-1}\right),}
\]

not a formula with \(G^{r-1,0}\). The differentiated transpose orientation is

\[
 \boxed{
 \widetilde R_{\ell-1}=\mathcal E_{\ell-1}
 +X_{\ell-1}^{[0]}\mathsf P_\ell
 +\sum_{r=0}^3X_{\ell-1}^{[r]}\rho_\ell^r,}
\]

not one with \(\mathsf P_\ell^T\). These orientations agree independently
with every non-symmetric response array in the accepted \(H=2\) formula.

There is no hidden use after the differentiated transpose. The first raw
matrix is represented exactly by the Gaussian initial preactivation and
\(Q^0\); its tangent and Hessian contractions require no additional
transpose response.

## 2. Fresh covariances and parity closure

The four fresh forward uses of one matrix form a joint \(4B\)-Gaussian block
with covariance \(G_{\ell-1}^{rs}\). The two transpose innovations have the
complete joint covariance

\[
 \begin{pmatrix}
 \mathsf P_\ell&S_\ell\\
 S_\ell^T&\boldsymbol\beta_\ell
 \end{pmatrix},
 \qquad
 (S_\ell)_{\alpha\beta}
 =\mathbb E[\Delta_{\ell,\alpha}
 \widetilde\Delta_{\ell,\beta}].
\]

Negating the centered readout, every base reverse innovation, and the odd
fresh forward jets gives

\[
 X_\ell^{[r]}\mapsto(-1)^rX_\ell^{[r]},\qquad
 \Delta_\ell\mapsto-\Delta_\ell,\qquad
 \widetilde\Delta_\ell\mapsto\widetilde\Delta_\ell.
\]

It follows jointly, not merely at the level of one-coordinate means, that

\[
 G_\ell^{rs}=0\ (r+s\text{ odd}),\qquad
 J_\ell^r=0\ (r\text{ even}),\qquad S_\ell=0.
\]

The top-down source contains \(F_\ell^1\) but not
\(F_\ell^2,F_\ell^3\). Thus \(\rho_\ell^2=\rho_\ell^3=0\) syntactically,
while

\[
 \frac{\partial\widetilde\Delta_{\ell,\beta}}
 {\partial F_{\ell,\alpha}^1}
 =\mathbf1_{\alpha=\beta}\phi''(F_{\ell,\beta}^0)R_{\ell,\beta}
\]

has zero expectation because \(R_\ell\) is centered and independent of
\(F_\ell^0\). Therefore

\[
 \rho_\ell^1=\rho_\ell^2=\rho_\ell^3=0,
 \qquad
 \widetilde R_{\ell-1}
 =\mathcal E_{\ell-1}
 +X_{\ell-1}^{[0]}(\mathsf P_\ell+\rho_\ell^0).
\]

This also proves that the two transpose innovations are independent after
the \(S_\ell=0\) cancellation. No correlated innovation was silently
dropped.

The primary note expands \(J_\ell^r\) and \(\rho_\ell^0\) explicitly in
equations (5.5)--(5.7) and (6.13). I checked those chain-rule formulas
componentwise. In particular, with
\((U_\ell^r)_{\alpha\beta}
=\phi'(F_{\ell,\alpha}^0)(L_\ell^r)_{\alpha\beta}\),

\[
\begin{aligned}
 (J_\ell^3)_{\alpha\beta}=\mathbb E[{}
 &3\phi'''_\beta(Z_\beta^{[1]})^2(U_\ell^1)_{\alpha\beta}
 +3\phi''_\beta Z_\beta^{[2]}(U_\ell^1)_{\alpha\beta}\\
 &+\phi'_\beta(U_\ell^3)_{\alpha\beta}],
\end{aligned}
\]

and the nonsymmetric matrix indices in the explicit \(\rho_\ell^0\) formula
are correct. The derivative notation in the response definitions is now
semantic shorthand, not an unresolved numerical operation.

## 3. Terminal contractions

Directly differentiating each raw gradient along the frozen direction gives

\[
 T_{H,c}=\mathbb E[R_H(X_H^{[3]})^T]+3c^TG_H^{02}c,
\]

\[
 \mathcal H_{a,c}=c^TG_H^{11}c,\qquad
 \mathcal H_{W^1,c}=\langle\boldsymbol\beta_1,Q^0\rangle_F,
\]

\[
 \mathcal H_{W^\ell,c}
 =\langle\boldsymbol\beta_\ell,Q^{\ell-1}\rangle_F
 +\langle\mathsf P_\ell,G_{\ell-1}^{11}\rangle_F,
 \qquad2\leq\ell\leq H.
\]

Before parity, the last norm contains the two cross orientations generated
by \(S_\ell\) and \(G_{\ell-1}^{01}\). Both vanish independently. Summing the
orthogonal parameter blocks and using the finite-width identity gives

\[
 \boxed{C_{H,c}=2T_{H,c}+4\mathcal H_{H,c}.}
\]

No trace transpose is missing: every covariance in the two surviving
Frobenius products is symmetric, while the nonsymmetric response matrices
have already been consumed inside the local Gaussian expectations.

## 4. Literal Gaussian normal form and complexity

The compact recursion is already a finite Gaussian-expectation DAG. At a
forward layer it integrates a \(4B\)-dimensional forward block together with
a \(B\)-dimensional reverse carrier. A reverse layer can additionally require
a \(B\)-dimensional differentiated-reverse innovation. Its retained state is
\(O(B^2)\) per layer and \(O(HB^2)\) if every layer is stored.

Only \(\phi,\phi',\phi'',\phi'''\) are evaluated in this compact form. The
inverse-free Wick--Stein recursion in equation (8.1) eliminates every
auxiliary Gaussian and leaves literal atoms

\[
 \mathbb E_{Z\sim N(0,Q)}
 \prod_j\phi^{(r_j)}(Z_{i_j}).
\]

The claimed derivative-order bound is safe. After parity, \(F_\ell^2\) is
the only explicit auxiliary forward coordinate that can correlate with the
activation argument \(F_\ell^0\), and each \(X_\ell^{[r]}\) is at most linear
in it. A Gram integrand therefore triggers at most two Stein derivatives,
starting from order at most three. The straight term has at most one
explicit \(F^2\); \(\boldsymbol\beta\) and \(\rho^0\) use only
\(F^0,F^1,R,\mathcal E\); and the terminal Hessian uses \(G^{11}\) and
\(\boldsymbol\beta\). Hence the completely activation-only form uses no
derivative above \(\phi^{(5)}\).

The recursion never inverts a covariance, so singular \(Q^0\), repeated
inputs, and degenerate activation Grams are included. The \(O(B^2)\) claim is
a state-size claim, not a polynomial-time guarantee for high-dimensional
Gaussian quadrature. A flat atom polynomial can grow rapidly in both \(H\)
and \(B\); no linear bound for that expansion is proved or claimed.

## 5. Independent executable gates

The exact sparse-polynomial/Isserlis backend
[fixed_batch_polynomial_reference.py](./fixed_batch_polynomial_reference.py)
does not call either accepted one-axis evaluator. The following all pass:

- \(H=2\): exact blockwise agreement on \(A,T,\mathcal H_a\), both weight
  Hessian blocks, and \(C\), for constant through cubic activations;
- \(B=1\): agreement with the independently contracted depth recurrence
  through \(H=4\);
- deep linear: exact
  \(A_{H,c}=(H+1)c^TQ^0c\) and
  \(C_{H,c}=\frac23H(H+1)^2(H+2)(c^TQ^0c)^2\);
- joint \(H=3,B=2\): exact batch permutation, channel homogeneity,
  inactive-channel isolation, singular repeated-input collapse, and all
  parity zeros.

For the genuinely joint nonlinear fixture

\[
 Q^0=\begin{pmatrix}1&1/3\\1/3&4/3\end{pmatrix},\quad
 c=(2/3,-1/4)^T,\quad\phi(x)=x+x^2/10,
\]

the exact target is

\[
 (A,T,\mathcal H,C)
 \approx(1.87494092079,1.15411417523,13.0120408663,54.3563918157).
\]

The independent finite-width audit
[audit_h3_b2_joint_nonlinear.py](./audit_h3_b2_joint_nonlinear.py) uses the
exact moving-flow compiler and a separately written frozen-line series. A
weighted \(1/n\) extrapolation over widths \(64,128,256,512\) gives

\[
\begin{array}{c|c|c|c}
 &\text{intercept}&\text{standard error}&z\text{ to target}\\\hline
 A&1.87016609&0.0079077&-0.604\\
 T&1.15346928&0.022197&-0.029\\
 \mathcal H&12.9890664&0.12048&-0.191\\
 C&54.2543578&0.52228&-0.195
\end{array}
\]

This is evidence rather than proof, but it probes the first case lying
strictly outside both accepted axes and separates the straight and Hessian
sectors.

Run:

    python -m studies.mean_field_peeling.generic_first_stieltjes.depth.run_fixed_batch_gates
    python -m studies.mean_field_peeling.generic_first_stieltjes.depth.audit_h3_b2_joint_nonlinear

## 6. Tensor-program probability bridge

For fixed \(H,B\), the exact base pass, frozen four-jet, differentiated
reverse pass, and every normalized terminal contraction form one finite
NETSOR\({}^T+\) program:

- every random matrix has iid \(N(0,1/n)\) entries after normalization;
- the \(B\) initial preactivation columns are a finite jointly Gaussian
  family and can be generated from a deterministic square root of
  \(Q^0\succeq0\), including the singular case;
- all reused orientations occur in the chronology of Section 1;
- every matrix-valued Gram entry is a finite collection of moment scalars;
- fixed \(H,B\) make both the number of program lines and the arity of every
  coordinate map independent of \(n\).

Definition 3.1 and Theorem 3.7 of Golikov--Yang,
[*Non-Gaussian Tensor Programs*](https://proceedings.neurips.cc/paper_files/paper/2022/file/8707924df5e207fa496f729f49069446-Paper-Conference.pdf),
permit arbitrary reuse of \(A,A^T\), moment scalars, and polynomially-smooth
coordinate maps. Under \(\phi\in C^\infty\) with every derivative
polynomially bounded, the theorem gives almost-sure and every-finite-
\(L^p\) convergence of every scalar in this fixed program. The master
recursion is exactly the response/covariance ledger above; \(L^1\) convergence
then yields the annealed coefficient.

For a finite-order pseudo-Lipschitz envelope, the corresponding fixed-program
master theorem can still give the quenched Gaussian recursion. It does not,
by itself, supply uniform integrability. Thus the theorem correctly keeps
the finite-order-only annealed statement open.

## 7. Physical MSE mapping

The MSE conclusion is also correct, but it relies on two additional response
scalars, not on \(C_c\) alone. For

\[
 \mathcal L=\frac1B\|y-f\|^2,\qquad d=\frac{y-f}{B},
\]

exact finite-width gradient-flow calculus gives

\[
\begin{aligned}
 \mathcal L'''(0)={}&-\frac{64}{B^4}(y-f)^TK^3(y-f)-16C_{n,d}\\
 &+128n^3p^T\mathcal A H_dp
 +\frac{96n^3}{B}\sum_s(j_s\mathbin\cdot p)H_s[p,p].
\end{aligned}
\]

For a frozen deterministic channel \(c\), write the last two terms through
\(k_s=n j_s\cdot p_c\),
\(h_s=n^2H_s[p_c,p_c]\), and
\(q_s=n^2j_s\cdot H_cp_c\). Readout sign reversal makes \(k_s\) even and
\(h_s,q_s\) odd. Their complete contractions therefore have exactly zero
finite-width expectation, and their deterministic tensor-program limits are
zero. This argument is independent of depth; for fixed \(H,B\), the mixed
derivative programs add only finitely many lines.

The actual residual channel is \(d_n=y/B-f_n/B\). The response scalars are
cubic and \(C_{n,c}\) is quartic in a frozen channel. Since \(f_n\to0\) and
all joint coefficient programs converge in every finite \(L^p\), finite
polarization plus Hölder justifies replacing \(d_n\) by \(y/B\) in \(L^1\).
The same argument replaces the residuals in the kernel term. Consequently,
coefficient by coefficient at \(t=0\),

\[
\begin{aligned}
 \lim_{n\to\infty}\mathcal J_3[\mathbb E\mathcal L_n](t)
 ={}&\frac{y^Ty}{B}
 -\frac{4\eta}{B^2}y^T\Theta^Hy\,t
 +\frac{8\eta^2}{B^3}y^T(\Theta^H)^2y\,t^2\\
 &-\left\{
 \frac{32\eta^3}{3B^4}y^T(\Theta^H)^3y
 +\frac{8\eta^3}{3}C_{H,y/B}
 \right\}t^3\pmod{t^4}.
\end{aligned}
\]

There is no interchange with fixed positive training time in this statement.

## 8. Final claim ledger

| claim | audit status |
|---|---|
| exact \(D_c^3g_c=2T+4\mathcal H\) source | **Pass** |
| all \(A/A^T\) responses and orientations | **Pass** |
| fresh covariance and parity registry | **Pass** |
| terminal \(T,\mathcal H,C\) contractions | **Pass** |
| compact Gaussian DAG, derivatives through order three | **Pass** |
| literal activation atoms, derivatives through order five | **Pass** |
| singular/repeated-input support without an inverse | **Pass** |
| accepted \(H=2\) and \(B=1\) reductions | **Pass** |
| genuinely joint nonlinear \(H=3,B=2\) gate | **Pass** |
| fixed-\(H,B\) annealed theorem under polynomial smoothness | **Pass** |
| physical arbitrary-label MSE cubic jet | **Pass** |
| \(H=H(n)\), \(B=B(n)\), or uniform error bounds | **Open** |
| annealed theorem under only finite-order growth | **Open** |
| flat-expansion or quadrature polynomial-time bound | **Not claimed** |
| fixed positive-time loss limit | **Not claimed** |
| nonnegative/Stieltjes-moment interpretation of \(C_{H,c}\) | **Refuted in general by existing generic-activation controls** |
