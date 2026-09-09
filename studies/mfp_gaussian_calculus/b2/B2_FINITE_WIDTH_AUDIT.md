# Hostile audit of the \(L=2,B=2\) directional program

**Date:** 2026-08-18  
**Scope:** exact finite-width scalarization, independent finite-width oracles,
the contracted polynomial reference, and the obligations for the subsequent
Gaussian peel  
**Canonical observable:**
\[
g_c=c^Tf,\qquad D_c=n\nabla g_c\mathbin\cdot\nabla,\qquad
C_{n,c}=D_c^3g_c .
\]

## 1. Verdict and claim level

The finite-width program in `FINITE_WIDTH_DIRECTIONAL_PROGRAM.md` is exact.
An independent raw-coordinate derivation confirms:

1. the input Gram appears as the covariant first-layer metric
   \(\dot U=(X_1R)Q^0\), with no inverse and no transpose error;
2. \(\zeta,\sigma,\tau\) are the first three derivatives along the frozen
   raw-parameter direction \(n\nabla g_c\);
3. \(\dot P,\dot R,\dot S\) are the three differentiated gradient blocks;
4. every factor of \(n\), every batch contraction, and all three Hessian-square
   blocks in (4.2)--(4.4) are correct; and
5. the trace orientation in the nonsymmetric middle-block cross term is
   exactly the one implemented.

The maintained Taylor oracle is algorithmically independent of the displayed
third-derivative contraction: it propagates ordinary power-series
coefficients for the complete feature-ascent ODE and never calls the direct
evaluator.  It nevertheless shares the analytically encoded gradient ODE, so
agreement between those two routes alone would not independently certify a
common error in the raw gradient or in the \(Q^0\) metric.  The added
`raw_coordinate_jet_audit.py` closes that loophole.  It differentiates the
original network simultaneously in every raw \((w,W,a)\) coordinate through
order three and contracts the resulting full gradient, Hessian, and third
derivative tensor.  It does not use either directional program's tangent or
gradient-flow equations.

The completed `B2_GAUSSIAN_NORMAL_FORM.md` and the exact-polynomial
contracted-GNF evaluator also pass this audit.  A line-by-line comparison
against Sections 7.1--7.3 found no omitted response direction, covariance, or
parity branch.  In particular, the third-tangent response has the correct
source/output index orientation, and the \(H_U\) block contains both distinct
cross terms with no missing factor two.  Section 7.4 records the complete
dictionary.  The master-theorem bridge is valid under the polynomial-
smoothness hypothesis stated in the GNF note; finite-order regularity retains
the uniform-integrability caveat described below.

The present claim ladder is therefore:

| Claim | Status |
|---|---|
| finite-width equations and normalization | **Proved** |
| equality with the power-series feature ODE | **Proved seedwise** |
| equality with a raw-coordinate third-order derivative tensor | **Proved seedwise** |
| contracted polynomial formula | **Algebraically audited; exact polynomial controls pass** |
| generic-activation Gaussian peel | **Proved under polynomial smoothness; Sections 7.1--7.4** |
| arbitrary-label MSE loss correction from \(C_c\) alone | **False**, but the full local loss jet is proved in Section 9 |

## 2. Independent raw-coordinate derivation

Let the two physical inputs be the columns of
\(\mathsf X\in\mathbb R^{d_0\times2}\), so

\[
Q^0=\frac1{d_0}\mathsf X^T\mathsf X.
\]

For raw first weights \(w\in\mathbb R^{n\times d_0}\), raw middle weights
\(W\in\mathbb R^{n\times n}\), and readout \(a\in\mathbb R^n\), put

\[
U=\frac1{\sqrt{d_0}}w\mathsf X,qquad A=\frac W{\sqrt n},qquad
X_r=\phi^{(r)}(U),qquad Z=AX_0,qquad Y_r=\phi^{(r)}(Z).
\]

With \(C=\operatorname{diag}(c)\), define

\[
v_a=Y_0c,qquad P=(a\mathbf1_2^T)Y_1C,qquad
R=A^TP,qquad S=X_1R,
\tag{2.1}
\]

where unmarked products between \(n\)-by-2 arrays are entrywise.  Direct
differentiation of \(g_c=c^Tf\) gives

\[
\nabla_a g_c=\frac1n v_a,
\qquad
\nabla_Wg_c=\frac1{n\sqrt n}PX_0^T,
\qquad
\nabla_wg_c=\frac1nS\frac{\mathsf X^T}{\sqrt{d_0}}.
\tag{2.2}
\]

Let \(V=n\nabla g_c\) be frozen at initialization.  Its induced velocities
are

\[
\dot a=v_a,qquad
\dot W=\frac1{\sqrt n}PX_0^T,qquad
\dot A=\frac1nPX_0^T,
\tag{2.3}
\]

and, crucially,

\[
\dot U=\dot w\frac{\mathsf X}{\sqrt{d_0}}
=S\frac{\mathsf X^T\mathsf X}{d_0}
=(X_1R)Q^0.
\tag{2.4}
\]

This proves both the side and the normalization on which \(Q^0\) acts.  A
contravariant \((Q^0)^{-1}\), an entrywise multiplication by \(Q^0\), or a
second batch normalization would describe a different optimizer.  Equation
(2.4) remains meaningful for singular \(Q^0\).

## 3. Frozen straight-line derivatives

Write

\[
M(L,R)=\frac1nL^TR,qquad Q_n=M(X_0,X_0),qquad
\dot X_0=X_1\dot U.
\]

Since \(w+t\dot w\) and \(W+t\dot W\) are affine in the frozen-line
parameter \(t\),

\[
\ddot X_0=X_2\dot U^2,qquad X_0^{(3)}=X_3\dot U^3.
\tag{3.1}
\]

The product rule for \(Z(t)=A(t)X_0(t)\) then gives, without an asymptotic
step,

\[
\zeta=PQ_n+A\dot X_0,
\tag{3.2}
\]

\[
\sigma=2P M(X_0,\dot X_0)+A\ddot X_0,
\tag{3.3}
\]

\[
\tau=3P M(X_0,\ddot X_0)+AX_0^{(3)}.
\tag{3.4}
\]

The coefficients \(2\) and \(3\) are the only cross terms because
\(\ddot A=0\).  The order \(P M(X_0,\dot X_0)\), rather than a transposed
moment matrix, follows directly from
\(\dot A\dot X_0=P(X_0^T\dot X_0)/n\).

For the differentiated gradients,

\[
\dot P=\big[(v_a\mathbf1_2^T)Y_1+(a\mathbf1_2^T)Y_2\zeta\big]C,
\tag{3.5}
\]

\[
\dot R=\dot A^TP+A^T\dot P
=X_0M(P,P)+A^T\dot P,
\tag{3.6}
\]

\[
\dot S=X_2\dot U R+X_1\dot R.
\tag{3.7}
\]

These reproduce equations (2.1)--(3.3) of the maintained program.

## 4. Third derivative and metric factors

For \(p=\nabla g_c\), \(H=\nabla^2g_c\), \(T=\nabla^3g_c\), and
\(V=np\), direct differentiation of \(D_c=n p\cdot\nabla\) gives

\[
D_c^3g_c=2T[V,V,V]+4n\|HV\|^2.
\tag{4.1}
\]

The frozen-line third derivative \(T[V,V,V]\) is

\[
\begin{aligned}
T_{n,c}=\frac1n\sum_i\Big\{&a_i\sum_s c_s
 (Y_{3,is}\zeta_{is}^3+3Y_{2,is}\zeta_{is}\sigma_{is}
 +Y_{1,is}\tau_{is})\\
&+3(v_a)_i\sum_s c_s
(Y_{2,is}\zeta_{is}^2+Y_{1,is}\sigma_{is})\Big\}.
\end{aligned}
\tag{4.2}
\]

The three blocks of \(n\|HV\|^2\) follow from differentiating (2.2):

\[
n\|(HV)_a\|^2
=\frac1n\|(Y_1\zeta)c\|^2,
\tag{4.3}
\]

\[
\begin{aligned}
n\|(HV)_W\|_F^2
={}&\operatorname{tr}\{M(\dot P,\dot P)M(X_0,X_0)\}\\
&+\operatorname{tr}\{M(P,P)M(\dot X_0,\dot X_0)\}\\
&+2\operatorname{tr}\{M(\dot P,P)M(\dot X_0,X_0)\},
\end{aligned}
\tag{4.4}
\]

\[
n\|(HV)_w\|_F^2
=\operatorname{tr}\{M(\dot S,\dot S)Q^0\}.
\tag{4.5}
\]

The orientation of the potentially dangerous cross term in (4.4) is seen
entrywise:

\[
\frac2{n^2}\sum_{i,j,s,t}
 \dot P_{is}P_{it}\dot X_{0,jt}X_{0,js}
=2\operatorname{tr}\{M(\dot P,P)M(\dot X_0,X_0)\}.
\tag{4.6}
\]

Because neither factor in (4.6) need be symmetric, replacing just one by its
transpose is a real error.  The implementation uses (4.6).  Similarly,

\[
\operatorname{tr}\{M(\dot S,\dot S)Q^0\}
=\frac1n\sum_{j,s,t}\dot S_{js}\dot S_{jt}Q^0_{ts},
\]

which is the raw first-weight norm and has no extra \(B^{-1}\) factor.

Combining (4.1)--(4.5) proves

\[
C_{n,c}=2T_{n,c}+4(H_{a,n}+H_{W,n}+H_{U,n}).
\]

## 5. Oracle independence and executed checks

### 5.1 Power-series oracle

`finite_width_jet.py` stores ordinary coefficients of
\(u(t),a(t),W(t)\) and recursively solves the exact feature-ascent ODE

\[
\dot a=Y_0c,qquad
\dot W=\frac1{\sqrt n}PX_0^T,qquad
\dot U=(X_1R)Q^0.
\]

It composes \(\phi\) by generic order-three Taylor rules, rather than using
\(\zeta,\sigma,\tau,\dot P,\dot R,\dot S\) or the Hessian-block formulas.
Thus it independently checks the chain and product rules after the gradient
ODE is granted.  It is not independent evidence for that ODE itself.

### 5.2 Raw-coordinate tensor oracle

`raw_coordinate_jet_audit.py` assigns a third-order multivariate jet to every
raw parameter, evaluates the original network, and obtains its full
\((p,H,T)\).  It compares

\[
n^3\big(4\|Hp\|^2+2T[p,p,p]\big)
\]

against the directional program.  This route has no encoded \(Q^0\) hit,
backward recursion, straight tangent, or Hessian block.  Its only shared
calculus input is the universal identity (4.1).

The same oracle now retains the two individual output jets, forms
\(B^{-1}\sum_s(f_s-y_s)^2\) directly in raw coordinates, and contracts the
loss gradient, Hessian, and third tensor under \(\dot\theta=-n\nabla\mathcal
J\).  Its four arbitrary-label checks agree with the separately encoded
residual-dependent formula (9.1), so the coefficients \(-64,-16,128,96\)
are independently covered rather than accepted from the displayed
derivation alone.  Four additional cases compare every component of
\((k,h,q)\) in (9.2) directly with the individual raw output gradients and
Hessians; this audits (9.5)--(9.6) before the terminal channel contractions.

The executed commands and outcomes were

```text
python -m studies.mean_field_peeling.generic_first_stieltjes.b2.run_checks
PASS 12 fixed-batch checks

python -m studies.mean_field_peeling.generic_first_stieltjes.b2.raw_coordinate_jet_audit
PASS 8 feature, 4 response, and 4 MSE independent raw-coordinate
third-jet checks; worst scaled error=1.239e-14
```

The finite-width suite covers widths \(1,3,6\), linear/affine/quadratic/cubic/
sine/tanh activations, correlated/diagonal/singular Grams, symmetric,
antisymmetric, asymmetric, zero, and rescaled channels.  The \(c=(1,0)\)
reduction was strengthened during this audit to include a nonzero
off-diagonal Gram entry.  It remains exactly equal to the audited \(B=1\)
program, as it must: an inactive output source cannot leak through input
correlation.  The same array program and contracted polynomial evaluator also
pass independent \(B=3\) linear and finite-width Taylor checks; this is useful
scope evidence, but the response checklist below remains written explicitly
for the requested \(B=2\) gate.

## 6. Audit of the contracted polynomial reference

The following notation makes the two most delicate parts transparent.  Let

\[
U\sim N(0,Q^0),\quad X_r=\phi^{(r)}(U),\quad
Q_{st}=\mathbb E[X_{0,s}X_{0,t}],
\]

\[
Z\sim N(0,Q),\quad Y_r=\phi^{(r)}(Z),\quad
\Delta_{st}=c_sc_t\mathbb E[Y_{1,s}Y_{1,t}],
\tag{6.1}
\]

and let \(R\sim N(0,\Delta)\), independent of \(U\).  Define

\[
t_a=\sum_pQ^0_{pa}X_{1,p}R_p,qquad
H^{(1)}_a=X_{1,a}t_a,quad
H^{(2)}_a=X_{2,a}t_a^2,quad
H^{(3)}_a=X_{3,a}t_a^3.
\tag{6.2}
\]

### 6.1 Third-tangent response orientation

The response of \(AH^{(3)}_a\) along the earlier source column \(P_s\) is

\[
N_{sa}=\mathbb E\frac{\partial H^{(3)}_a}{\partial R_s}
=3Q^0_{sa}\mathbb E[X_{3,a}X_{1,s}t_a^2].
\tag{6.3}
\]

After expanding \(t_a^2\),

\[
N_{sa}=3Q^0_{sa}\sum_{p,r}Q^0_{pa}Q^0_{ra}\Delta_{pr}
\mathbb E[X_{3,a}X_{1,s}X_{1,p}X_{1,r}].
\tag{6.4}
\]

Thus \(s\) is the source/response row and \(a\) is the output tangent column.
The implementation's `third_response[s][a]` is exactly (6.4).  The full
response in \(\tau_a\) is

\[
\sum_sP_s\{3M_{sa}+N_{sa}\},qquad
M_{sa}=\mathbb E[X_{0,s}H^{(2)}_a],
\tag{6.5}
\]

so `tau_response[s][a]` also has the correct orientation.  Quadratic controls
cannot test (6.3), because \(\phi'''=0\); the derivative calculation above is
the necessary independent audit.

### 6.2 First-weight Hessian block

Let \(\Gamma\) be the fresh field associated to \(AH^{(1)}\), define the
nested source \(B=\dot P\), and put

\[
\beta_{ab}=\mathbb E[B_aB_b],\qquad
\Chi=\Delta+\mathcal S,
\]

where \(\mathcal S\) is the response of \(A^TB\) along \(X_0\).  The symbolic
backward derivative is

\[
\dot R_a=\sum_sX_{0,s}\Chi_{sa}+\Eta_a,qquad
\operatorname{Cov}(\Eta)=\beta.
\tag{6.6}
\]

Writing \(\dot S_a=A_a+B_a^{U}\), with

\[
A_a=X_{2,a}t_aR_a,qquad
B_a^{U}=X_{1,a}\left(\sum_sX_{0,s}\Chi_{sa}+\Eta_a\right),
\]

gives four response/Wick pieces plus the fresh variance:

\[
\begin{aligned}
\mathbb E[A_aA_b]
={}&\sum_{p,r}Q^0_{pa}Q^0_{rb}
(\Delta_{ap}\Delta_{br}+\Delta_{ab}\Delta_{pr}
 +\Delta_{ar}\Delta_{pb})\\
&\hspace{35mm}\times
\mathbb E[X_{2,a}X_{1,p}X_{2,b}X_{1,r}],
\end{aligned}
\tag{6.7}
\]

\[
\mathbb E[B_a^{U}B_b^{U}]
=\sum_{s,t}\Chi_{sa}\Chi_{tb}
 \mathbb E[X_{1,a}X_{0,s}X_{1,b}X_{0,t}]
 +\beta_{ab}\mathbb E[X_{1,a}X_{1,b}],
\tag{6.8}
\]

\[
\mathbb E[B_a^{U}A_b]
=\sum_{s,p}\Chi_{sa}Q^0_{pb}\Delta_{bp}
 \mathbb E[X_{1,a}X_{0,s}X_{2,b}X_{1,p}],
\tag{6.9}
\]

\[
\mathbb E[A_aB_b^{U}]
=\sum_{t,p}\Chi_{tb}Q^0_{pa}\Delta_{ap}
 \mathbb E[X_{1,b}X_{0,t}X_{2,a}X_{1,p}].
\tag{6.10}
\]

Finally

\[
H_U=\sum_{a,b}Q^0_{ab}
\mathbb E[(A_a+B_a^U)(A_b+B_b^U)].
\tag{6.11}
\]

Equations (6.7)--(6.10) agree term-for-term with `aa`, `bb`, `ba`, and `ab`
in `contracted_gnf_polynomial_reference.py`.  There is no global factor two:
the two generally distinct cross orientations (6.9) and (6.10) are already
listed separately.  For \(a=b\) they become equal and automatically supply
the familiar factor two.

The exact evaluator passes constant and linear controls, channel
homogeneity, correlated-inactive \(B=1\) reduction for degrees one through
three, and the accepted quadratic two-input polynomials in Section 8.

## 7. Hostile checklist and discharge of the Gaussian peel

This section was written as a proof checklist before the closed GNF existed.
It is retained as an independent registry and is now discharged line by line
against `B2_GAUSSIAN_NORMAL_FORM.md`.  Every displayed matrix index ranges
over the two batch coordinates.

Define

\[
G_{sa}=\mathbb E[X_{1,s}X_{1,a}],\qquad
L_{sa}=Q^0_{sa}G_{sa},\qquad
\Alpha=Q+L.
\tag{7.1}
\]

Let \(A_0\sim N(0,1)\) denote the local readout and

\[
P_a=A_0c_aY_{1,a}.
\]

The first backward field must be represented as

\[
R\sim N(0,\Delta),qquad
\Delta_{sa}=c_sc_a\mathbb E[Y_{1,s}Y_{1,a}],
\tag{7.2}
\]

independent of the local \((U,A_0,Z)\).  No inverse covariance may be used in
singular equal/opposite/constant cases.

### 7.1 Complete response-direction registry

| multiplication | all earlier opposite-orientation input directions | required coefficient/status |
|---|---|---|
| \(AX_0\) | none | fresh \(Z\), covariance \(Q\) |
| \(A^TP\) | every \(X_{0,s}\) | \(\mathbb E[\partial_{Z_s}P_a]=\delta_{sa}c_a\mathbb E[A_0Y_{2,a}]=0\) |
| \(AH^{(1)}_a\) | every \(P_s\) | \(L_{sa}=Q^0_{sa}\mathbb E[X_{1,s}X_{1,a}]\) |
| \(AH^{(2)}_a\) | every \(P_s\) | \(2Q^0_{sa}\mathbb E[X_{2,a}X_{1,s}t_a]=0\) |
| \(AH^{(3)}_a\) | every \(P_s\) | nonzero \(N_{sa}\) in (6.3) |
| \(A^TB_a\) | every \(X_{0,s}\) | nonzero nested response \(\mathcal S_{sa}\) below |
| same | every \(H^{(1)}_s\) | \(\mathbb E[\partial_{\Gamma_s}B_a]=\delta_{sa}c_a\mathbb E[A_0Y_{2,a}]=0\) |
| same | every \(H^{(2)}_s,H^{(3)}_s\) | exactly zero: \(B\) does not depend on those channels |

The nonzero nested response must use \(\Alpha\), not merely \(Q\).  Put

\[
h_a=\sum_k c_kY_{1,k}\Alpha_{ka},\qquad
v=\sum_kc_kY_{0,k},
\]

\[
B_a=c_a\{vY_{1,a}+A_0Y_{2,a}(A_0h_a+\Gamma_a)\}.
\tag{7.3}
\]

Holding the fresh \(\Gamma\) fixed,

\[
\boxed{
\begin{aligned}
\mathcal S_{sa}=c_a\{&c_s\mathbb E[Y_{1,s}Y_{1,a}]
+\delta_{sa}\mathbb E[vY_{2,a}]
+\delta_{sa}\mathbb E[Y_{3,a}h_a]\\
&+c_s\Alpha_{sa}\mathbb E[Y_{2,s}Y_{2,a}]\}.
\end{aligned}}
\tag{7.4}
\]

Consequently the required symbolic tangent fields are

\[
\zeta=P\Alpha+\Gamma,
\tag{7.5}
\]

\[
M(X_0,H^{(1)})\to0,qquad \sigma\Rightarrow\Omega,
\tag{7.6}
\]

\[
M(X_0,H^{(2)})\to M,quad M_{sa}=\mathbb E[X_{0,s}H^{(2)}_a],
\]

\[
\tau\Rightarrow P(3M+N)+\Lambda,
\tag{7.7}
\]

\[
A^TB\Rightarrow X_0\mathcal S+\Eta,qquad
\dot R\Rightarrow X_0(\Delta+\mathcal S)+\Eta.
\tag{7.8}
\]

### 7.2 Fresh covariance registry

The jointly Gaussian forward fresh fields must have the following complete
covariance table:

\[
\operatorname{Cov}(\Gamma_a,\Gamma_b)=\mathbb E[H^{(1)}_aH^{(1)}_b],
\]

\[
\operatorname{Cov}(\Omega_a,\Omega_b)=\mathbb E[H^{(2)}_aH^{(2)}_b],
\]

\[
\operatorname{Cov}(\Lambda_a,\Lambda_b)=\mathbb E[H^{(3)}_aH^{(3)}_b],
\]

\[
\operatorname{Cov}(Z_s,\Omega_a)=M_{sa},qquad
\operatorname{Cov}(\Gamma_s,\Lambda_a)
=\mathbb E[H^{(1)}_sH^{(3)}_a].
\tag{7.9}
\]

Every other forward cross covariance is zero by centered-\(R\) parity:

\[
\operatorname{Cov}(Z,\Gamma)=
\operatorname{Cov}(Z,\Lambda)=
\operatorname{Cov}(\Gamma,\Omega)=
\operatorname{Cov}(\Omega,\Lambda)=0.
\tag{7.10}
\]

The transpose fresh field has

\[
\operatorname{Cov}(\Eta_a,\Eta_b)=\beta_{ab}=\mathbb E[B_aB_b].
\tag{7.11}
\]

Its only possible earlier same-orientation covariance is

\[
\operatorname{Cov}(R_s,\Eta_a)=\mathbb E[P_sB_a]=0,
\tag{7.12}
\]

by readout parity and centering of \(\Gamma\).  Fresh fields of opposite
matrix orientation are independent after their displayed response pieces are
removed.  A proof must establish this whole joint law in one program, rather
than combining marginal CLTs.

### 7.3 Parity obligations and forbidden shortcuts

The peel must explicitly certify all of the following.

- \(M(X_0,H^{(1)})\to0\) because it is linear in centered \(R\).
- The \(AH^{(2)}\) response is zero because its derivative is linear in
  centered \(R\).
- The cross covariances in (7.10) have odd total \(R\)-degree.
- \(M(B,P)\to0\) by readout parity and
  \(M(H^{(1)},X_0)\to0\) by \(R\)-parity.  Therefore the mixed term in
  \(H_W\) vanishes entrywise on both sides; covariance fluctuations must not
  be used to resurrect it.
- The \(H^{(3)}\) response (6.3), the \(Z\)--\(\Omega\) covariance, and the
  \(\Gamma\)--\(\Lambda\) covariance are generally nonzero.
- In particular, \(\Gamma\)--\(\Lambda\) must be retained until the complete
  straight-line readout contraction is formed.  It vanishes there only
  because the sole \(\Lambda\) occurrence carries one centered \(A_0\), not
  because the fresh fields are independent.
- The \(Z\)--\(\Omega\) covariance generates Stein terms in both
  \(A_0Y_2\zeta\sigma\) and \(vY_1\sigma\).  Treating \(\Omega\) as
  independent of \(Z\) deletes leading terms.
- The scalar branch \(M(X_0,H^{(1)})P\) must be killed as a scalar inside the
  same fixed Tensor Program.  A one-coordinate mean-zero statement is not a
  substitute for joint convergence of its later products.
- Constant, inactive-channel, and coincident-input cases are rank-degenerate;
  the proof route must not assume an invertible limiting Gram.

### 7.4 Line-by-line comparison with the closed GNF

The notation dictionary is

\[
Q=Q^1,\qquad \Delta=\mathsf D,\qquad L=\mathsf L,
\qquad \Alpha=\mathsf K,
\tag{7.13}
\]

\[
\operatorname{Cov}(H^{(1)})=\mathsf G,qquad
M=\mathsf M,qquad N=\mathsf N,qquad
3M+N=\boldsymbol\kappa,
\tag{7.14}
\]

and

\[
\mathcal S=\rho,\qquad \Delta+\mathcal S=\chi,qquad
\operatorname{Cov}(\Eta)=\beta.
\tag{7.15}
\]

The hostile comparison gives the following result.

| Audit row | Closed-GNF location | Verdict |
|---|---|---|
| first transpose response and total tangent (7.1)--(7.5) | (2.1), (4.2)--(4.5) | pass; symmetry of \(\mathsf L\) explains the harmless index reversal in `AP` notation |
| zero quadratic and nonzero cubic forward responses | (3.1), (4.2)--(4.3) | pass; \(\mathsf N_{sa}\) has source \(s\), output \(a\) |
| nested \(A^TB\) response (7.3)--(7.4) | (4.6)--(4.10) | pass; the derivative of \(\zeta\) uses the full \(\mathsf K=Q^1+\mathsf L\) |
| differentiated backward field (7.8) | (4.10)--(4.12) | pass; \(\chi=\mathsf D+\rho\) and \(\operatorname{Cov}(R,\Delta)=0\) |
| complete forward covariance table (7.9)--(7.10) | (3.2)--(3.3), (4.4) | pass; \(Z\)--\(\Omega\) and \(\Gamma\)--\(\Lambda\) are retained |
| \(Z\)--\(\Omega\) Stein contraction | second line of (5.4) | pass; all four derivatives of \(y_{2,a}v_a\) and \(hy_{1,a}\) occur |
| terminal disappearance of \(\Gamma\)--\(\Lambda\) | discussion after (5.4) | pass; it is killed by the single centered readout only at the terminal contraction |
| fresh nested variance | (5.3) | pass; the \(3g_ag_b\) coefficient is \(\mathbb E\mathsf a^4=3\) |
| readout and middle Hessian blocks | (5.5) | pass; the exact mixed middle term is zero by the two scalar parity limits |
| first-weight Hessian block | (6.1)--(6.3) | pass; all `AA`, `BB`, `AB`, and `BA` terms of (6.7)--(6.10) occur once |
| terminal coefficient | (7.1) | pass; \(C_c=2T_c+4(H_{a,c}+H_{W,c}+H_{U,c})\) |

The formulas contain no covariance inverse, so the comparison also passes in
the singular cases explicitly listed in Section 7.3.  Expanding the sums in
the GNF reproduces `contracted_gnf_polynomial_reference.py` term for term:
`source_cov`, `tangent_c`, `tangent_cov`, `second_cross`,
`third_response`, `tau_response`, `nested_response`, and `total_response`
are respectively \(\mathsf D,\mathsf K,\mathsf G,\mathsf M,\mathsf N,
\boldsymbol\kappa,\rho,\chi\).  The remaining `straight_line`,
`hessian_readout`, `hessian_middle`, and `hessian_first` blocks are exactly
(5.4), (5.5), and (6.3).

Finally, the source identity (1.1)--(4.5), all scalar moment lines, both uses
of the same Gaussian middle matrix and its transpose, and the terminal
contractions form one fixed NETSOR\({}^\top+\) program.  Under polynomial
smoothness, Theorem 3.7 of Golikov--Yang, *Non-Gaussian Tensor Programs*,
gives joint almost-sure and every-finite-\(L^p\) convergence, hence the
annealed coefficient.  Tensor Programs III, Theorem E.15, still gives the
almost-sure fixed-program value under the weaker finite-order
pseudo-Lipschitz envelope, but that weaker route alone does not prove uniform
integrability.  This is a regularity boundary, not an unresolved response or
rank issue.

## 8. Exact controls for the Gaussian-limit formula

These are mandatory regression gates for any proposed generic GNF.

### 8.1 Constant activation

For \(\phi=1\),

\[
A_c=D_cg_c=(\mathbf1^Tc)^2,qquad C_c=0.
\tag{8.1}
\]

This is exact already at finite width.

### 8.2 Linear activation

For \(\phi(x)=x\), linearity gives the exact identity

\[
g_c=f(x_{\rm eff}),qquad x_{\rm eff}=\sum_sc_sx_s,qquad
q_{\rm eff}=c^TQ^0c.
\]

Thus the audited one-sample result requires

\[
A_c=3q_{\rm eff},qquad C_c=48q_{\rm eff}^2.
\tag{8.2}
\]

The finite-width suite now checks this reduction block-by-block for generic
nonsymmetric \(c\), correlated and singular \(Q^0\).

### 8.3 Quadratic activation and channel normalization

Let

\[
Q^0=\begin{pmatrix}1&\theta\\\theta&1\end{pmatrix},qquad
t=\theta^2,qquad
c_\pm=\frac12(1,\pm1).
\]

The independent exact Campaign-2 compiler gives

\[
A_+=63+20t+28t^2,
\]

\[
C_+=279680+423312t+788336t^2+143232t^3+50624t^4,
\tag{8.3}
\]

\[
A_-=48-20t-28t^2,
\]

\[
C_-=168192-91904t-270144t^2+143232t^3+50624t^4.
\tag{8.4}
\]

The contracted reference reproduces these polynomials exactly at rational
values of \(\theta\).  At \(t=1\), (8.3) gives
\(A_+=111,C_+=1\,685\,184\), the audited one-input result, while the minus
channel is zero.  The named channels in `model.py` are unnormalized
\((1,\pm1)\); for those, multiply \(A_\pm\) by \(4\) and \(C_\pm\) by
\(16\).  Confusing these conventions is a fatal normalization error.

### 8.4 Active-channel reduction

For \(c=(1,0)\), any PSD

\[
Q^0=\begin{pmatrix}q&\rho\\\rho&q_2\end{pmatrix}
\]

must reduce to the \(B=1\) GNF at variance \(q\), independently of \(\rho\)
and the inactive realization.  This is now checked at finite width with
\(\rho\ne0\) and in the contracted polynomial evaluator for activations of
degrees one, two, and three.

## 9. Physical MSE loss mapping

The arbitrary-label loss is not controlled by \(C_c\) alone.  This section
gives the exact finite-width calculus and closes the two additional response
limits needed for the full local loss jet.

Let

\[
\mathcal J(\theta)=\frac1B\|f(\theta)-y\|^2,qquad
\dot\theta=-n\nabla\mathcal J,
\]

and write \(j_a=\nabla f_a\), \(H_a=\nabla^2f_a\),
\(K_{ab}=n j_a\cdot j_b\).  At the point being differentiated set

\[
r=y-f,qquad d=\frac rB,qquad
g_d=d^Tf\quad(d\text{ held frozen}),
\]

\[
p=\nabla g_d,\qquad H_d=\sum_ad_aH_a,qquad
\mathcal A=\frac1B\sum_a j_a\otimes j_a,qquad
C_d=D_d^3g_d.
\]

Since

\[
\nabla\mathcal J=-2p,qquad
\nabla^2\mathcal J=2(\mathcal A-H_d),
\]

and

\[
\nabla^3\mathcal J[v,v,v]
=-2\nabla^3g_d[v,v,v]
+\frac6B\sum_a(j_a\cdot v)H_a[v,v],
\]

the universal gradient-flow identity gives the exact result

\[
\boxed{
\begin{aligned}
\mathcal J'''(0)={}&-\frac{64}{B^4}r^TK^3r-16C_d\\
&+128n^3p^T\mathcal A H_dp
+\frac{96n^3}{B}\sum_a(j_a\cdot p)H_a[p,p].
\end{aligned}}
\tag{9.1}
\]

For learning rate \(\eta\), the right side is multiplied by \(\eta^3\).

The two response terms can be encoded without introducing a new derivative
of \(\phi\).  Freeze an arbitrary deterministic channel \(c\), let
\(p=\nabla g_c\), put \(H_c=\sum_ac_aH_a\), and define, for each output
coordinate \(s\),

\[
 k_s:=n j_s\mathbin\cdot p,
 \qquad h_s:=n^2H_s[p,p],
 \qquad q_s:=n^2j_s\mathbin\cdot H_cp.
\tag{9.2}
\]

Thus \(k=Kc\), and the last two scalars in (9.1) are exactly

\[
 n^3p^T\mathcal A H_cp=\frac1B\sum_s k_s q_s,
 \qquad
 \frac{n^3}{B}\sum_s(j_s\mathbin\cdot p)H_s[p,p]
 =\frac1B\sum_s k_s h_s.
\tag{9.3}
\]

Here is a literal fixed-program encoding.  Write
\(\langle u,v\rangle_n=n^{-1}u^Tv\), put
\(\dot v_{\rm ro}=(Y_1\zeta)c\), and, for each \(s\), define the individual
output source

\[
 P^{[s]}_{ia}=a_iY_{1,is}\mathbf1_{\{a=s\}},\qquad
 R^{[s]}=A^TP^{[s]},\qquad S^{[s]}=X_1R^{[s]}.
\tag{9.4}
\]

In the notation of Sections 2--4,

\[
\begin{aligned}
k_s={}&\langle v_a,Y_{0,s}\rangle_n
       +\langle a,Y_{1,s}\zeta_s\rangle_n,\\
h_s={}&\langle a,Y_{2,s}\zeta_s^2+Y_{1,s}\sigma_s\rangle_n
       +2\langle v_a,Y_{1,s}\zeta_s\rangle_n,
\end{aligned}
\tag{9.5}
\]

and

\[
\begin{aligned}
q_s={}&\langle Y_{0,s},\dot v_{\rm ro}\rangle_n
       +\operatorname{tr}\{M(P^{[s]},\dot P)M(X_0,X_0)\}\\
&+\operatorname{tr}\{M(P^{[s]},P)M(\dot X_0,X_0)\}
 +\operatorname{tr}\{M(S^{[s]},\dot S)Q^0\}.
\end{aligned}
\tag{9.6}
\]

Equation (9.6) is the readout, middle-weight, and first-weight block
decomposition of \(n j_s\cdot(H_cV)\), where \(V=np\).  In particular, its
second trace has the displayed \(M(\dot X_0,X_0)\) orientation.  Direct
differentiation gives the useful joint checks

\[
 c^Tk=D_cg_c,\qquad c^T(h+q)=D_c^2g_c.
\tag{9.7}
\]

The implementation `frozen_mse_responses` evaluates (9.2)--(9.6), and
`mse_loss_third_derivative` evaluates the complete residual-dependent (9.1).
Neither routine inserts a zero response by hand.

It remains to prove, rather than guess, the two zero limits.  Let
\(\mathscr R\) be the orthogonal parameter involution that negates the whole
readout vector and leaves both hidden-weight blocks fixed.  Since
\(f_s(\mathscr R\theta)=-f_s(\theta)\), differentiation gives

\[
 j_s(\mathscr R\theta)=-\mathscr Rj_s(\theta),\qquad
 p(\mathscr R\theta)=-\mathscr Rp(\theta),\qquad
 H_s(\mathscr R\theta)=-\mathscr RH_s(\theta)\mathscr R,
\tag{9.8}
\]

and the same Hessian identity for \(H_c\).  Consequently

\[
 k_s(\mathscr R\theta)=k_s(\theta),\qquad
 h_s(\mathscr R\theta)=-h_s(\theta),\qquad
 q_s(\mathscr R\theta)=-q_s(\theta).
\tag{9.9}
\]

Both complete contractions in (9.3), not merely their one-neuron
integrands, are therefore odd under an exact symmetry of the initialization.
Their expectations are exactly zero at every finite width whenever they are
integrable.  More importantly for a quenched claim, (9.4)--(9.6) append only
finitely many `MatMul`, `Moment`, and scalar-product lines to the already
fixed program.  The master theorem makes each limit deterministic; invariance
under (9.8) forces that deterministic limit to equal its negative, hence to
be zero.  Under polynomial smoothness, Theorem 3.7 supplies convergence in
every finite \(L^p\), so the annealed limits are zero as well.  This is the
required joint-program argument and does not infer a product limit from a
one-copy mean.

At centered initialization, \(f_n\to0\) in every finite \(L^p\), so the
actual residual channel \(d_n=(y-f_n)/B\) converges to \(c=y/B\).  The two
responses in (9.3) are cubic polynomials in the frozen channel.  Expanding
\(d_n=c-f_n/B\) and applying Hölder with the same joint \(L^p\) bounds proves
that their residual-dependent versions differ from the frozen-\(c\) versions
by \(o_{L^1}(1)\).  Likewise, homogeneity and finite-dimensional
polarization express \(C_{n,d_n}-C_{n,c}\) as a finite sum of mixed quartic
coefficient programs containing at least one factor of \(f_n\).  The same
joint bounds therefore give

\[
 K_n\longrightarrow\Theta\quad\text{entrywise in every finite }L^p,
\qquad
 \Theta_{ab}=Q^2_{ab}+Q^1_{ab}E^2_{ab}
 +Q^0_{ab}E^1_{ab}E^2_{ab},
\tag{9.10}
\]

and, simultaneously, \(C_{n,d_n}\to C_{y/B}\) in \(L^1\).  Therefore the
full arbitrary-label third loss jet is

\[
\boxed{
 \mathcal J'''(0)\longrightarrow
 -\frac{64}{B^4}y^T\Theta^3y-16C_{y/B}.}
\tag{9.11}
\]

The only extra term in the exact second loss derivative is proportional to
\(n^2p^TH_cp\); it is odd under the same involution and has deterministic
zero limit.  Consequently, the coefficientwise limiting initialization
Taylor jet through order three, for learning rate \(\eta\), is

\[
\begin{aligned}
\mathcal J(t)={}&\frac{\|y\|^2}{B}
-\frac{4\eta t}{B^2}y^T\Theta y
+\frac{8\eta^2t^2}{B^3}y^T\Theta^2y\\
&-\eta^3t^3\left{
\frac{32}{3B^4}y^T\Theta^3y+\frac83C_{y/B}
\right}\pmod{t^4}.
\end{aligned}
\tag{9.12}
\]

Thus the first nonlinear feature term for arbitrary labels is
\(-\frac83\eta^3C_{y/B}\), but it accompanies the full NTK-cube term.  The
latter cannot in general be reconstructed from the one directional scalar
\(A_c=c^T\Theta c\), so \((A_c,C_c)\) alone still is not an arbitrary-label
loss theorem.  Equal/opposite exchange-invariant channels are the scalar
special cases of (9.11)--(9.12), not an assumption used in the proof.

## 10. Final evidence ledger and promotion gate

| Item | Verdict | Falsifier or remaining obligation |
|---|---|---|
| raw \(Q^0\) metric | pass | any raw-coordinate jet mismatch under a nondiagonal Gram |
| straight tangents | pass | missing \(2\dot A\dot X\) or \(3\dot A\ddot X\) branch |
| Hessian metric factors | pass | disagreement with (2.2) and (4.1) |
| middle trace orientation | pass | asymmetric raw-coordinate counterexample |
| finite-width jet oracle | genuinely independent of displayed contraction, but shares the gradient ODE | closed by the third raw-coordinate route |
| raw-coordinate oracle | pass in eight feature, four componentwise response, and four full-MSE cases | nonfinite jet or mismatch above \(10^{-10}\) |
| contracted polynomial evaluator | pass | failure of (6.3), (6.7)--(6.10), or exact controls |
| generic Gaussian joint law | pass | Sections 7.1--7.4; no covariance inverse or rank-stability assumption |
| annealed generic coefficient | pass for polynomially smooth \(\phi\) | finite-order-only hypotheses still require a separate UI proof |
| arbitrary-label MSE cubic jet | pass for polynomially smooth \(\phi\) | exact (9.1), fixed-program responses (9.2)--(9.9), and full kernel limit (9.10) |

Precisely, the finite-width identities and Gaussian atom polynomial use only
\(\phi\in C^3\) with the displayed Gaussian expectations finite.  The
promoted almost-sure fixed-program statement under the weaker route assumes
that the finitely many coordinate maps built from
\(\phi,\phi',\phi'',\phi'''\) satisfy the finite-order pseudo-Lipschitz
hypotheses of Tensor Programs III, Theorem E.15.  The annealed and every-
finite-\(L^p\) statements in Sections 7 and 9 instead use polynomial
smoothness: \(\phi\in C^\infty\), with every derivative bounded by a
polynomial (constants may depend on derivative order), as required by
Non-Gaussian Tensor Programs, Theorem 3.7.  Throughout, \(B\) and the
deterministic labels are fixed, \(Q^0\) is any deterministic PSD Gram
(singular allowed), and all weight blocks have the centered independent
Gaussian initialization specified in the model.

The \(B=2\) stage is therefore promoted under the stated polynomial-
smoothness envelope.  The closed generic-activation GNF matches the hostile
response ledger, the exact evaluator and all independent controls, and the
two additional arbitrary-label MSE response observables have been encoded
and proved to vanish in the joint deterministic limit.  What remains outside
this promotion is the weaker finite-order-only annealed regularity class, not
an algebraic, covariance, rank, or loss-mapping obligation.
