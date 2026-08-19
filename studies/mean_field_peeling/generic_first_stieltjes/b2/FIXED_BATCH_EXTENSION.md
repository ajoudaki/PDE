# Fixed-batch extension of the two-hidden-layer Gaussian normal form

**Status:** explicit arbitrary-fixed-\(B\) directional normal form and
physical arbitrary-label local MSE jet  
**Date:** 2026-08-18  
**Scope:** two hidden layers, derivative order three, arbitrary fixed
\(B=O(1)\), arbitrary PSD input Gram, a frozen deterministic direction
\(c\in\mathbb R^B\), and arbitrary deterministic labels
\(y\in\mathbb R^B\)  
**Not claimed:** a bound uniform in \(B\), a regime \(B=B(n)\), arbitrary
depth, or a finite-time theorem beyond the coefficientwise initialization
jet

The two-input formulas in
[`B2_GAUSSIAN_NORMAL_FORM.md`](B2_GAUSSIAN_NORMAL_FORM.md) do not use the
fact that the batch index has two values.  Replacing every occurrence of
\(\{1,2\}\) by \(I_B=\{1,\ldots,B\}\) gives a closed Gaussian normal form
for each fixed finite \(B\).  This note states that extension explicitly,
proves that no new matrix-response type appears, and records the finite-DAG
and theorem bounds.  Section 8 separately appends the fixed-program response
scalars needed to convert the frozen directional coefficient into the
physical arbitrary-label local MSE jet.

## 1. Fixed-batch model and atom grammar

Fix an integer \(B\ge1\), a PSD matrix
\(Q^0\in\mathbb R^{B\times B}\), and \(c\in\mathbb R^B\).  At initialization,

\[
 U_{j,:}\stackrel{\mathrm{iid}}\sim N(0,Q^0),\qquad
 A=\frac W{\sqrt n},\qquad X_r=\phi^{(r)}(U),
\tag{1.1}
\]

\[
 Z=AX_0,qquad Y_r=\phi^{(r)}(Z),qquad
 f_s=\frac1n\sum_i a_iY_{0,is}.
\tag{1.2}
\]

The directional observable and feature operator are

\[
 g_c=c^Tf,qquad D_c=n\nabla g_c\mathbin\cdot\nabla,qquad
 C_{n,c}=D_c^3g_c.
\tag{1.3}
\]

For a PSD \(B\)-by-\(B\) matrix \(Q\), index word
\({\bf i}\in I_B^m\), and derivative word
\({\bf r}\in\{0,1,2,3\}^m\), define the literal atom

\[
 \mathcal I_Q({\bf i};{\bf r})
 :=\mathbb E_{G\sim N(0,Q)}
 \prod_{k=1}^m\phi^{(r_k)}(G_{i_k}).
\tag{1.4}
\]

This pushforward definition covers singular \(Q\) and never uses a Gaussian
density or covariance inverse.

For a representative first-layer coordinate, write
\(U\sim N(0,Q^0)\), \(x_{r,a}=\phi^{(r)}(U_a)\), and set

\[
 Q^1_{ab}=\mathbb E_U[x_{0,a}x_{0,b}],qquad
 E^1_{ab}=\mathbb E_U[x_{1,a}x_{1,b}].
\tag{1.5}
\]

For \(Z\sim N(0,Q^1)\), write
\(y_{r,a}=\phi^{(r)}(Z_a)\), and set

\[
 Q^2_{ab}=\mathbb E_Z[y_{0,a}y_{0,b}],qquad
 E^2_{ab}=\mathbb E_Z[y_{1,a}y_{1,b}].
\tag{1.6}
\]

All indices below range independently over \(I_B\).  Every expectation is
an atom (1.4), and every displayed abbreviation is a finite deterministic
sum or product of such atoms.

## 2. Complete arbitrary-fixed-\(B\) formula

### 2.1 First tangent and NTK

Define

\[
 \mathsf D_{ab}=c_ac_bE^2_{ab},\qquad
 \mathsf L_{ab}=Q^0_{ab}E^1_{ab},\qquad
 \mathsf K_{ab}=Q^1_{ab}+\mathsf L_{ab}.
\tag{2.1}
\]

The directional NTK coefficient is

\[
\boxed{
 A_c=\sum_{a,b}c_ac_b
 \bigl(Q^2_{ab}+Q^1_{ab}E^2_{ab}
                  +Q^0_{ab}E^1_{ab}E^2_{ab}\bigr).}
\tag{2.2}
\]

### 2.2 Contracted bottom-layer arrays

Define

\[
\begin{aligned}
 \mathsf G_{ab}
 &:=\sum_{p,q}Q^0_{ap}Q^0_{bq}\mathsf D_{pq}
 \mathbb E_U[x_{1,a}x_{1,p}x_{1,b}x_{1,q}],\\
 \mathsf M_{sa}
 &:=\sum_{p,q}Q^0_{ap}Q^0_{aq}\mathsf D_{pq}
 \mathbb E_U[x_{0,s}x_{2,a}x_{1,p}x_{1,q}],\\
 \mathsf N_{sa}
 &:=3Q^0_{as}\sum_{p,q}Q^0_{ap}Q^0_{aq}\mathsf D_{pq}
 \mathbb E_U[x_{3,a}x_{1,s}x_{1,p}x_{1,q}],\\
 \boldsymbol\kappa_{sa}&:=3\mathsf M_{sa}+\mathsf N_{sa}.
\end{aligned}
\tag{2.3}
\]

No backward Gaussian remains in (2.3); its second and fourth moments have
already been Wick-contracted into \(\mathsf D\).

### 2.3 Contracted top-layer arrays

Use the finite algebraic abbreviations

\[
 h=\sum_i c_i y_{0,i},\qquad
 v_a=\sum_i\mathsf K_{ai}c_i y_{1,i},
\tag{2.4}
\]

\[
 f_a=h y_{1,a},\qquad
 g_a=y_{2,a}v_a,qquad
 w_a=\sum_s\boldsymbol\kappa_{sa}c_sy_{1,s}.
\tag{2.5}
\]

Define the fresh differentiated-transpose covariance

\[
\boxed{
 \beta_{ab}=c_ac_b\mathbb E_Z\!\left[
 f_af_b+f_ag_b+g_af_b+3g_ag_b
 +\mathsf G_{ab}y_{2,a}y_{2,b}
 \right],}
\tag{2.6}
\]

the nested transpose response

\[
\boxed{
 \rho_{sa}=c_a\mathbb E_Z\!\left[
 c_sy_{1,s}y_{1,a}
 +\delta_{sa}\{hy_{2,a}+y_{3,a}v_a\}
 +\mathsf K_{as}c_sy_{2,a}y_{2,s}
 \right],}
\tag{2.7}
\]

and the total differentiated-backward response

\[
 \chi_{sa}=\mathsf D_{sa}+\rho_{sa}.
\tag{2.8}
\]

Expanding the finite sums in (2.4)--(2.5) makes (2.6)--(2.7) literal sums
of atoms (1.4); there is no implicit random field in these definitions.

### 2.4 Straight-line and Hessian blocks

The contracted frozen-line third derivative is

\[
\boxed{
\begin{aligned}
 T_c={}&\sum_a c_a\mathbb E_Z\!\left[
 3y_{3,a}\{v_a^3+v_a\mathsf G_{aa}\}
 +y_{1,a}w_a
 +3hy_{2,a}\{v_a^2+\mathsf G_{aa}\}
 \right]\\
 &+3\sum_{a,s}c_a\mathsf M_{sa}\mathbb E_Z\!\left[
 \delta_{sa}y_{3,a}v_a
 +\mathsf K_{as}c_sy_{2,a}y_{2,s}
 +c_sy_{1,s}y_{1,a}
 +\delta_{sa}hy_{2,a}
 \right].
\end{aligned}}
\tag{2.9}
\]

The readout and middle-weight Hessian-square blocks are

\[
\boxed{
\begin{aligned}
 H_{a,c}
 &:=\mathbb E_Z\!\left[
 \left(\sum_a c_ay_{1,a}v_a\right)^2
 +\sum_{a,b}c_ac_b\mathsf G_{ab}y_{1,a}y_{1,b}
 \right],\\
 H_{W,c}
 &:=\sum_{a,b}\left(Q^1_{ab}\beta_{ab}
                    +\mathsf D_{ab}\mathsf G_{ab}\right).
\end{aligned}}
\tag{2.10}
\]

For the first-weight block, define

\[
 \overline A_a
 :=x_{2,a}\sum_pQ^0_{ap}x_{1,p}\mathsf D_{ap},
 \qquad
 \overline B_a
 :=x_{1,a}\sum_s\chi_{sa}x_{0,s},
\tag{2.11}
\]

\[
\begin{aligned}
 \mathcal A_{ab}
 :=x_{2,a}x_{2,b}\sum_{p,q}Q^0_{ap}Q^0_{bq}x_{1,p}x_{1,q}
 \big(&\mathsf D_{ap}\mathsf D_{bq}
      +\mathsf D_{ab}\mathsf D_{pq}\\
      &+\mathsf D_{aq}\mathsf D_{pb}\big).
\end{aligned}
\tag{2.12}
\]

Then

\[
\boxed{
\begin{aligned}
 H_{U,c}:=\sum_{a,b}Q^0_{ab}\Big\{
 &\mathbb E_U[\mathcal A_{ab}
 +\overline B_a\overline B_b
 +\overline A_a\overline B_b
 +\overline B_a\overline A_b]\\
 &+E^1_{ab}\beta_{ab}\Big\}.
\end{aligned}}
\tag{2.13}
\]

The arbitrary-fixed-batch normal form is

\[
\boxed{
 C_c=2T_c+4\bigl(H_{a,c}+H_{W,c}+H_{U,c}\bigr).}
\tag{2.14}
\]

Equations (1.4)--(2.14) have maximum activation derivative order three and
contain only \(B\)-dimensional Gaussian expectations at covariances
\(Q^0\) and \(Q^1\).  They are identical to the \(B=2\) formula except for
the index set.

## 3. Why no new response type appears

The claim is stronger than a notational extrapolation: the complete response
registry is independent of the number of batch coordinates.

Let \(\mathsf a\sim N(0,1)\), set
\(b_s=\mathsf a c_sy_{1,s}\), and temporarily let
\(R\sim N(0,\mathsf D)\) be independent of \(U\).  Define

\[
 t_a=\sum_pQ^0_{ap}x_{1,p}R_p,qquad
 P_a=x_{1,a}t_a,qquad
 E_a=x_{2,a}t_a^2,qquad
 F_a=x_{3,a}t_a^3.
\tag{3.1}
\]

The exact fixed-width program can be scheduled in the following order.

1. **Initial forward multiplication.**  \(AX_0\) creates
   \(Z\sim N(0,Q^1)\).

2. **First transpose.**  Each column of \(A^Tb\) has possible response
   only along an earlier \(X_{0,s}\).  Its coefficient is
   \[
   \mathbb E[\partial_{Z_s}b_a]
   =\delta_{sa}c_a\mathbb E[\mathsf a y_{2,a}]=0.
   \tag{3.2}
   \]
   Therefore \(A^Tb\rightsquigarrow R\) is fresh with covariance
   \(\mathsf D\), for every \(B\).

3. **Three forward reuses.**  The unrestricted transpose rule gives
   \[
   AP_a\rightsquigarrow\sum_s\mathsf L_{as}b_s+\Gamma_a,
   \qquad AE_a\rightsquigarrow\Omega_a,
   \qquad AF_a\rightsquigarrow\sum_s\mathsf N_{sa}b_s+\Lambda_a.
   \tag{3.3}
   \]
   These exhaust the earlier opposite-orientation family \(b_s\), because
   \[
   \mathbb E[\partial_{R_s}P_a]=\mathsf L_{as},\quad
   \mathbb E[\partial_{R_s}E_a]=0,\quad
   \mathbb E[\partial_{R_s}F_a]=\mathsf N_{sa}.
   \tag{3.4}
   \]

4. **Second transpose.**  Form this line after \(AP\), but before the
   algebraically independent \(AE,AF\) lines.  With
   \[
   \zeta_a=\mathsf a v_a+\Gamma_a,qquad
   B_a=c_a\{hy_{1,a}+\mathsf a y_{2,a}\zeta_a\},
   \tag{3.5}
   \]
   the only earlier forward-input families are \(X_0\) and \(P\).  Their
   response coefficients are
   \[
   \mathbb E[\partial_{Z_s}B_a]=\rho_{sa},qquad
   \mathbb E[\partial_{\Gamma_s}B_a]
   =\delta_{sa}c_a\mathbb E[\mathsf a y_{2,a}]=0.
   \tag{3.6}
   \]
   Thus
   \[
   A^TB_a\rightsquigarrow\sum_s\rho_{sa}x_{0,s}+\Delta_a,
   \qquad \operatorname{Cov}(\Delta_a,\Delta_b)=\beta_{ab}.
   \tag{3.7}
   \]
   The only earlier same-orientation fresh field is \(R\), and
   \(\operatorname{Cov}(R_s,\Delta_a)=\mathbb E[b_sB_a]=0\) by centered
   readout parity.

The fresh forward covariance types are likewise unchanged.  Before terminal
contraction their only potentially nonzero off-diagonal blocks are

\[
 \operatorname{Cov}(Z_s,\Omega_a)=\mathsf M_{sa},
 \qquad
 \operatorname{Cov}(\Gamma_a,\Lambda_b)
 =\mathbb E_U[P_aF_b].
\tag{3.8}
\]

All \(Z\)--\(\Gamma\), \(Z\)--\(\Lambda\),
\(\Gamma\)--\(\Omega\), and \(\Omega\)--\(\Lambda\) blocks vanish by
odd \(R\)-degree.  The generally nonzero second covariance in (3.8) is
retained until the full straight-line contraction; it disappears there only
because the sole \(\Lambda\) term carries one independent centered
\(\mathsf a\).  The \(Z\)--\(\Omega\) block instead survives through
the inverse-free Stein rule

\[
 \mathbb E[\Omega_aF(Z)]
 =\sum_s\mathsf M_{sa}\mathbb E[\partial_{Z_s}F(Z)],
\tag{3.9}
\]

which produces the second line of (2.9).

This list is exhaustive because every occurrence of \(A\) or \(A^T\) in
the exact order-three finite-width program appears in steps 1--4.  Enlarging
\(B\) enlarges each response family from two coordinates to \(B\)
coordinates, but creates neither a new orientation nor a new causal input
family.  No rank-stability or covariance-invertibility shortcut is used.

## 4. Finite atom and DAG bounds

The following counts treat one Gaussian atom evaluation as one oracle call;
they do not claim that generic \(B\)-dimensional numerical integration has
unit cost.

| Stage | Expanded index work / atom occurrences |
|---|---:|
| \(Q^1,E^1,Q^2,E^2,\mathsf D,\mathsf L,\mathsf K\) | \(O(B^2)\) |
| \(\mathsf G,\mathsf M,\mathsf N\) | \(O(B^4)\) |
| \(\beta\), after distributing \(h,v,f,g\) | \(O(B^4)\) |
| \(\rho,\chi\) | \(O(B^2)\) with Kronecker zeros exploited; \(O(B^3)\) naively |
| \(T_c,H_{a,c},H_{W,c},H_{U,c}\) | \(O(B^4)\) |

Consequently, the fully contracted order-three coefficient has an explicit
DAG with \(O(B^4)\) arithmetic/atom nodes and \(O(B^4)\) cached expanded
storage in a direct implementation.  Streaming the contractions can reduce
temporary storage, but no such optimization is needed for the fixed-\(B\)
theorem.  Every terminal atom contains at most four activation factors and
uses derivatives of order at most three.

If the full audit-only covariance of \((Z,\Gamma,\Omega,\Lambda)\) is
materialized before applying terminal parity, the unused
\(\Omega\)--\(\Omega\), \(\Gamma\)--\(\Lambda\), and
\(\Lambda\)--\(\Lambda\) blocks have naive expansions through
\(O(B^6),O(B^6),O(B^8)\), respectively.  They are not required by the
terminal compiler: (3.8)--(3.9) prove symbolically which blocks survive.

At any separately fixed derivative order \(r\), the same Tensor-Program
unrolling gives a finite \(O(B^{k_r})\) atom DAG for some finite exponent
\(k_r\) determined by that unrolling.  No bound on the growth of \(k_r\) is
asserted.  Only the exact \(r=3\), \(O(B^4)\) bound is established here.
There is no claim uniform in derivative order, batch size, or depth.

## 5. Fixed-program probability theorem

For each fixed finite \(B\), the arrays in
`FINITE_WIDTH_DIRECTIONAL_PROGRAM.md` have shapes \(n\)-by-\(B\) or
\(B\)-by-\(B\).  Expanding each matrix-valued `Moment` into its \(B^2\)
scalar entries gives a finite Tensor Program whose number of lines depends
on \(B\), but not on width \(n\).  It permits every reuse of \(A\) and
\(A^T\) in Section 3.

Assume \(\phi\) is polynomially smooth: \(\phi\in C^\infty(\mathbb R)\),
and every derivative \(\phi^{(k)}\), \(k\ge0\), is bounded in absolute value
by a polynomial whose constants may depend on \(k\).  Theorem 3.7 of Golikov
and Yang, *Non-Gaussian Tensor Programs*, applied separately at this fixed
\(B\), gives

\[
 C_{n,c}\longrightarrow C_c
 \quad\text{almost surely and in }L^p
 \quad(1\le p<\infty),
 \qquad
 \mathbb E C_{n,c}\longrightarrow C_c.
\tag{5.1}
\]

Correlated or singular \(U\) is generated by a deterministic square root of
\(Q^0\); no inverse or limiting-rank assumption is introduced.  Under only
finite-order pseudo-Lipschitz control, Tensor Programs III, Theorem E.15,
still supplies the almost-sure fixed-program limit, but annealed convergence
requires an additional uniform-integrability argument.

Equation (5.1) is pointwise in the fixed integer \(B\).  It gives no uniform
control over \(B\), no simultaneous theorem over all batch sizes, and no
result when \(B\) grows with \(n\).

## 6. Executable and exact gates beyond two inputs

The `b2` directory name is historical.  The maintained implementations are
now batch-dynamic:

- [`finite_width_directional.py`](finite_width_directional.py) evaluates the
  exact order-three contraction, the two MSE response scalars, and the full
  residual-dependent local MSE jet for any nonempty fixed batch;
- [`finite_width_jet.py`](finite_width_jet.py) independently propagates the
  complete feature-ascent Taylor jet for that batch;
- [`model.py`](model.py) accepts any square PSD Gram and samples the
  corresponding correlated first preactivations;
- [`contracted_gnf_polynomial_reference.py`](contracted_gnf_polynomial_reference.py)
  evaluates (2.2)--(2.14) exactly for polynomial activations and any fixed
  batch size.

The executed \(B=3\) finite-width gate uses

\[
 Q^0=\begin{pmatrix}
 1&0.2&-0.1\\
 0.2&0.8&0.25\\
 -0.1&0.25&1.3
 \end{pmatrix},qquad
 c=(0.4,-0.7,0.2),
\tag{6.1}
\]

and checks linear, quadratic, sine, and tanh activations at widths
\(1,4,7\) with independent seeds.  The direct finite-width contraction and
the feature-ODE jet agree seedwise.  A separate exact-rational \(B=3\)
linear test verifies

\[
 A_c=3c^TQ^0c,qquad C_c=48(c^TQ^0c)^2.
\tag{6.2}
\]

The full maintained command reports

```text
python -m studies.mean_field_peeling.generic_first_stieltjes.b2.run_checks
PASS 12 fixed-batch checks
```

The independent raw-coordinate tensor audit remains a \(B=2\) gate; it is
not being relabelled as a \(B=3\) audit.  It now checks eight feature jets,
four componentwise \((k,h,q)\) response triples, and four complete
arbitrary-label MSE jets against the batch-dynamic executable.

## 7. Directional tensors by polarization

The scaling of the deterministic arrays is

\[
 \mathsf D,\mathsf G,\mathsf M,\mathsf N,\rho,\chi=O(c^2),qquad
 v,h=O(c),\qquad \beta=O(c^4),
\tag{7.1}
\]

which makes \(A_c\) a homogeneous quadratic polynomial and \(C_c\) a
homogeneous quartic polynomial in \(c\).  Hence there are unique symmetric
multilinear forms \(\mathcal A\) and \(\mathcal C\) such that

\[
 A_c=\mathcal A(c,c),qquad
 C_c=\mathcal C(c,c,c,c).
\tag{7.2}
\]

They are recovered without a new Gaussian peel.  For \(u,v\in\mathbb R^B\),

\[
 \mathcal A(u,v)=\frac14\{A_{u+v}-A_{u-v}\}.
\tag{7.3}
\]

For \(u_1,u_2,u_3,u_4\in\mathbb R^B\), real polarization gives

\[
\boxed{
 \mathcal C(u_1,u_2,u_3,u_4)
 =\frac1{2^4\,4!}
 \sum_{\varepsilon\in\{-1,1\}^4}
 \left(\prod_{j=1}^4\varepsilon_j\right)
 C_{\sum_{j=1}^4\varepsilon_j u_j}.}
\tag{7.4}
\]

Indeed, expanding the quartic polynomial in (7.4), the sign sum kills every
monomial unless each \(u_j\) occurs an odd number of times.  Total degree
four then forces each to occur exactly once, and the \(4!\) permutations
cancel the denominator.

In the standard basis,

\[
 \mathcal A_{ij}=\mathcal A(e_i,e_j),\qquad
 \mathcal C_{ijkl}=\mathcal C(e_i,e_j,e_k,e_l),
\tag{7.5}
\]

and

\[
 A_c=\sum_{i,j}\mathcal A_{ij}c_ic_j,qquad
 C_c=\sum_{i,j,k,l}\mathcal C_{ijkl}c_ic_jc_kc_l.
\tag{7.6}
\]

Thus the scalar compiler determines every mixed directional coefficient.
A symbolic implementation can propagate the quartic coefficient dictionary
directly with \(O(B^4)\) entries; (7.4) is the implementation-independent
definition.

## 8. Physical arbitrary-label MSE corollary

Polarization solves the frozen-direction tensor problem, but does not by
itself solve the physical loss evolution for arbitrary labels.  The two
extra response scalars nevertheless form fixed programs for every fixed
\(B\), and centered-readout parity closes them jointly.

For

\[
 \mathcal J(\theta)=\frac1B\|f(\theta)-y\|^2,
\tag{8.1}
\]

the residual direction changes under gradient flow.  At initialization set

\[
r=y-f,\qquad d=\frac rB,\qquad p=\nabla g_d,\qquad
K_{ab}=n\nabla f_a\mathbin\cdot\nabla f_b,
\tag{8.2}
\]

where \(d\) is held frozen while differentiating.  If
\(H_a=\nabla^2f_a\), \(H_d=\sum_ad_aH_a\), and
\(\mathcal A=B^{-1}\sum_a\nabla f_a\otimes\nabla f_a\), exact finite-width
calculus under \(\dot\theta=-n\nabla\mathcal J\) gives

\[
\boxed{
\begin{aligned}
\mathcal J'''(0)={}&-\frac{64}{B^4}r^TK^3r-16C_{n,d}\\
&+128n^3p^T\mathcal A H_dp
+\frac{96n^3}{B}\sum_a(\nabla f_a\mathbin\cdot p)H_a[p,p].
\end{aligned}}
\tag{8.3}
\]

For a frozen deterministic channel \(c\), define

\[
k_s=n\nabla f_s\mathbin\cdot\nabla g_c,\qquad
h_s=n^2H_s[\nabla g_c,\nabla g_c],\qquad
q_s=n^2\nabla f_s\mathbin\cdot H_c\nabla g_c.
\tag{8.4}
\]

Here \(H_c=\sum_ac_aH_a\).

Then the last two contractions in (8.3) are exactly

\[
\frac1B\sum_s k_s q_s,
\qquad \frac1B\sum_s k_s h_s.
\tag{8.5}
\]

Equations (9.4)--(9.6) of
[`B2_FINITE_WIDTH_AUDIT.md`](B2_FINITE_WIDTH_AUDIT.md) give their literal
`MatMul`/`Moment` encoding; those array equations are batch-dynamic and use
only the same \(B\) source columns already present here.  Thus appending all
\(k_s,h_s,q_s\), \(s\in I_B\), adds finitely many lines for every fixed
\(B\).

Let \(\mathscr R\) negate the complete readout vector and fix both hidden
weight blocks.  The exact identities

\[
\nabla f_s(\mathscr R\theta)=-\mathscr R\nabla f_s(\theta),
\qquad
H_s(\mathscr R\theta)=-\mathscr RH_s(\theta)\mathscr R
\tag{8.6}
\]

make \(k_s\) even and \(h_s,q_s\) odd.  Hence each *complete* scalar in
(8.5), rather than only a one-coordinate integrand, has exactly zero
finite-width expectation.  The fixed-program master theorem also makes its
limit deterministic, so readout-sign invariance forces both almost-sure
limits to be zero.  Under polynomial smoothness, Theorem 3.7 supplies the
joint \(L^p\) convergence needed for the annealed statement.

At centered initialization, \(f_n\to0\) in every finite \(L^p\).  Therefore
the actual residual direction \(d_n=(y-f_n)/B\) converges to \(c=y/B\).
The response scalars are cubic and \(C_{n,c}\) is quartic in its frozen
channel; finite-dimensional expansion and Hölder show that replacing
\(d_n\) by \(c\) costs \(o_{L^1}(1)\).  With

\[
\Theta_{ab}=Q^2_{ab}+Q^1_{ab}E^2_{ab}
+Q^0_{ab}E^1_{ab}E^2_{ab},
\tag{8.7}
\]

the full NTK converges entrywise to \(\Theta\) in every finite \(L^p\), and
the arbitrary-label third jet is

\[
\boxed{
\mathcal J_n'''(0)\longrightarrow
-\frac{64}{B^4}y^T\Theta^3y-16C_{y/B}.}
\tag{8.8}
\]

For learning rate \(\eta\), the coefficientwise initialization Taylor jet
through order three is consequently

\[
\begin{aligned}
\mathcal J(t)={}&\frac{\|y\|^2}{B}
-\frac{4\eta t}{B^2}y^T\Theta y
+\frac{8\eta^2t^2}{B^3}y^T\Theta^2y\\
&-\eta^3t^3\left\{
\frac{32}{3B^4}y^T\Theta^3y+\frac83C_{y/B}
\right\}\pmod{t^4}.
\end{aligned}
\tag{8.9}
\]

Thus the arbitrary-fixed-batch directional theorem and the physical
arbitrary-label *local* MSE theorem are both closed under the probability
hypotheses of Section 5.  This does not assert a uniform-in-\(B\) theorem or
a finite-time interchange of the width and time limits.
