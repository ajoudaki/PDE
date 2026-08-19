# Symbolic contraction route: exact partial closure and the surviving order-five obstruction

## Verdict

This route does **not** produce the requested arbitrary-depth formula for the
complete coefficient \(C_H=F_H^{(5)}(0)\). It produces, and freezes, a
strictly smaller result that should not be promoted:

* a seven-scalar bottom-up, nine-scalar top-down deterministic recurrence;
* literal one-dimensional-\(M_\nu\) transitions with no Gaussian,
  covariance table, response derivative, or unnamed evaluator;
* the complete coefficients \(A_H\) and \(B_H\), with zero exact-rational
  discrepancies at \(H=2,3,4\);
* exactly the first three of the six tensor families in \(C_H\).

The other three families require a second Hessian image and remain open.
The frozen manifest is
`FROZEN_SECTOR_MANIFEST.json`, SHA-256
`31e11cae9ed9f347ccbfde6965ee39856af0536b947a58627456101846c0fd9a`.

## 1. Canonical alphabet

Throughout,

\[
M_{\nu_0\ldots\nu_5}
=\mathbb E_{G\sim N(0,1)}
 \prod_{r=0}^5\phi^{(r)}(G)^{\nu_r},
\qquad M_{200000}=1,
\]

\[
d=M_{020000},\qquad
\tau_\ell=\sum_{j=0}^{\ell}d^j,\qquad
b_\ell=d^{H-\ell}.
\]

Every line of the emitted recurrence is a sum or product of rational
numbers, these atoms, and previously declared deterministic scalars. The
complete dependency-first formulas are printed in
`FROZEN_SECTOR_TRANSITIONS.cse.txt`; its SHA-256 is
`d5c6c081f6a953126d29b67ec953a32e26d038327f2b92bda6037098d47ce721`.
The five sections start at lines 1, 17, 113, 215, and 387. Thus the CSE file
is the literal displayed transition, not an instruction to invoke a Wick or
Gaussian evaluator.

## 2. Exact six-tree decomposition and the partial sector

In whitened parameter coordinates put

\[
p=\nabla f,\quad H=\nabla^2f,\quad T=\nabla^3f,\quad
U=\nabla^4f,\quad V=\nabla^5f.
\]

The exact finite-width identity is

\[
\begin{split}
D^5f={}&2V[p,p,p,p,p]+22U[Hp,p,p,p]
 +14T[T[p,p],p,p]\\
&+30T[H^2p,p,p]+36T[Hp,Hp,p]+16\lVert H^2p\rVert^2.
\end{split}
\tag{2.1}
\]

The frozen sector closed here is

\[
C_H^{\rm fr}
=2S_{5,H}+22G_{31,H}+14G_{22,H},
\tag{2.2}
\]

where the three symbols in (2.2) are deterministic contractions emitted by
the recurrence below. Semantically they equal

\[
S_{5,H}=V[p^5],\qquad
G_{31,H}=U[Hp,p,p,p],\qquad
G_{22,H}=T[T[p,p],p,p].
\]

## 3. Seven bottom-up scalars

Use

\[
x_\ell=(P_\ell,V_\ell,Q_\ell,W_\ell,S_\ell,J_\ell,K_\ell).
\tag{3.1}
\]

These are already contracted deterministic scalars. Their initialization is

\[
\begin{array}{lll}
P_1=b_1M_{121000},&V_1=b_1M_{040000},
&Q_1=3b_1^2M_{140010},\\
W_1=3b_1^2M_{050100},&S_1=3b_1^2M_{042000},
&J_1=3b_1M_{030100},\\
&&K_1=15b_1^2M_{050001}.
\end{array}
\tag{3.2}
\]

For \(2\leq\ell\leq H\), substitute

\[
(P,V,Q,W,S,J3,J5)=x_{\ell-1},\qquad
\mathrm{TAU}=\tau_{\ell-1},\qquad
\mathrm{BASE\_B}=b_\ell
\tag{3.3}
\]

in the seven explicitly printed roots `P_NEXT,...,J5_NEXT` in lines
17--111 of the frozen transition file. Set those seven roots equal to
\(x_\ell\) in the order (3.1). No operation other than evaluating the
displayed finite arithmetic DAG is implicit in (3.3).

Two useful projections of those literal lines are

\[
V_\ell=dV_{\ell-1}+\tau_{\ell-1}^2b_\ell M_{040000},
\tag{3.4}
\]

\[
P_\ell=M_{101000}V_{\ell-1}
+\tau_{\ell-1}^2b_\ell M_{121000}
+(d+M_{101000})P_{\ell-1},
\tag{3.5}
\]

\[
\begin{split}
J_\ell={}&3\tau_{\ell-1}V_{\ell-1}M_{010100}
+3\tau_{\ell-1}^3b_\ell M_{030100}\\
&+3\tau_{\ell-1}P_{\ell-1}
  (M_{010100}+M_{002000})
+d(J_{\ell-1}+3P_{\ell-1}).
\end{split}
\tag{3.6}
\]

Equations (3.4)--(3.6) are exactly the three accepted order-three forward
states. The remaining four printed roots are the additional frozen
order-five states.

## 4. Nine top-down scalars

Use the deterministic state

\[
y_\ell=(E^{02}_\ell,E^{11}_\ell,E^{13}_\ell,E^{22}_\ell,
          \kappa^{10}_\ell,\kappa^{21}_\ell,
          \kappa^{30}_\ell,\kappa^{32}_\ell),
\tag{4.1}
\]

together with the explicit base scalar

\[
E^{00}_\ell=d^{H-\ell+1}.
\tag{4.2}
\]

Thus the stored dimension is eight if (4.2) is not counted, and nine when
all live scalar slots are counted. No minimality is claimed.

At the top, substitute \(x_{H-1}\) and
\(\mathrm{TAU}=\tau_{H-1}\) into the nine printed roots
`B00_H,...,K32_H` at lines 113--213. Here \(x_0=0\) when \(H=1\).
Identify

\[
(B00,B02,B11,B13,B22,K10,K21,K30,K32)
=(E^{00},E^{02},E^{11},E^{13},E^{22},
\kappa^{10},\kappa^{21},\kappa^{30},\kappa^{32}).
\tag{4.3}
\]

For \(\ell=H-1,\ldots,1\), substitute the nine entries of
\(y_{\ell+1}\), the seven entries of \(x_{\ell-1}\), and
\(\mathrm{TAU}=\tau_{\ell-1}\) into lines 215--385. At the bottom take
\(x_0=0\) and \(\tau_0=1\). The nine roots ending in `_NEXT` are
\(y_\ell\). These 171 dependency-first arithmetic lines are the complete
contracted transition.

The exact order-three projection is particularly short:

\[
\begin{split}
E^{11}_\ell={}&E^{00}_{\ell+1}V_{\ell-1}M_{002000}
+3\tau_{\ell-1}^2(E^{00}_{\ell+1})^2M_{022000}
+dE^{11}_{\ell+1}\\
&+(\kappa^{10}_{\ell+1})^2M_{220000}
+2\tau_{\ell-1}\kappa^{10}_{\ell+1}
  E^{00}_{\ell+1}M_{121000},
\end{split}
\tag{4.4}
\]

\[
\kappa^{10}_\ell
=dE^{00}_{\ell+1}
+\tau_{\ell-1}E^{00}_{\ell+1}(M_{010100}+M_{002000})
+\kappa^{10}_{\ell+1}(M_{101000}+d).
\tag{4.5}
\]

With \(\beta_\ell=E^{11}_\ell\) and
\(\chi_\ell=\kappa^{10}_\ell\), (4.4)--(4.5) are literally Section 7.1.

## 5. Terminal contractions

Define

\[
S_{3,H}=J_H+3P_H,\qquad S_{5,H}=K_H+5Q_H,
\tag{5.1}
\]

\[
\begin{split}
G_{11,H}={}&V_H+E^{11}_1
+\sum_{\ell=2}^H(E^{00}_\ell V_{\ell-1}+E^{11}_\ell),\\
G_{31,H}={}&W_H+E^{13}_1
+\sum_{\ell=2}^H\bigl(
 E^{00}_\ell W_{\ell-1}+3E^{02}_\ell V_{\ell-1}
 +3E^{11}_\ell P_{\ell-1}+E^{13}_\ell\bigr),\\
G_{22,H}={}&S_H+E^{22}_1
+\sum_{\ell=2}^H\bigl(
 E^{00}_\ell S_{\ell-1}+2E^{02}_\ell P_{\ell-1}
 +4E^{11}_\ell V_{\ell-1}+E^{22}_\ell\bigr).
\end{split}
\tag{5.2}
\]

Then this recurrence proves

\[
\boxed{A_H=\tau_H,\qquad
B_H=2S_{3,H}+4G_{11,H},}
\tag{5.3}
\]

and the partial fifth-order sector (2.2). It does **not** prove
\(C_H=C_H^{\rm fr}\).

## 6. Exact audits

The local formulas (3.4)--(3.6) and (4.4)--(4.5) were independently
canonicalized against Section 7.1; all five discrepancy counts are zero.
After the Route-S manifest was frozen, a separately implemented sparse
Wick--Stein derivation was translated into the same atom alphabet. All
seven forward and all nine reverse transition roots agree coefficient by
coefficient: 16 roots, zero discrepancies. The post-freeze result is
`INDEPENDENT_SECTOR_COMPARISON.json`.
Distributing the assembled recurrence gives

| depth | A terms / discrepancies | B terms / discrepancies | partial-C terms | partial C vs full C discrepancies |
|---:|---:|---:|---:|---:|
| 2 | `3 / 0` | `46 / 0` | `451` | `857` |
| 3 | `4 / 0` | `160 / 0` | `3,177` | `5,795` |
| 4 | `5 / 0` | `350 / 0` | `8,898` | `15,612` |

The maximum derivative index in every emitted atom is five. For the linear
activation, the partial sector is \(56,560,2968\) at \(H=2,3,4\), whereas
the accepted full values are \(1464,13888,73240\). This sharp control
prevents accidental promotion of the partial recurrence. The constant
activation gives zero in both the partial and unresolved sectors.

## 7. Exact unresolved branches

The missing deterministic scalar is not an unevaluated Gaussian integral.
It is the still-uncontracted network-depth transfer for

\[
\boxed{
30T[H^2p,p,p],\qquad
36T[Hp,Hp,p],\qquad
16\lVert H^2p\rVert^2.}
\tag{7.1}
\]

Writing \(A=Hp\), \(B=T[p,p]\), \(C=U[p,p,p]\), and letting
\(m_2=B+HA\), \(m_3=C+3T[p,A]+Hm_2\), the exact identity can also be
organized as

\[
D^5f=2V[p^5]+10\langle A,C\rangle
+10\langle B,m_2\rangle+4\lVert m_2\rVert^2
+12\langle A,m_3\rangle.
\tag{7.2}
\]

The present state closes \(V[p^5]\), \(\langle A,C\rangle\), and
\(\lVert B\rVert^2\), but it does not carry the second Hessian image \(HA\)
or the mixed tangent \(T[p,A]\). Propagating either through a reused hidden
matrix introduces a forward-after-reverse matrix use. No complete M-only
transition or terminal contraction for those cross-pairings has been
derived or audited. The linear \(H=1\) control is decisive against the
current terminal formula: every closed frozen tensor family vanishes, but
the full fifth coefficient is \(32\), entirely from (7.1). This does not
prove that some enlargement or nonlinear reuse of the present state is
impossible.

Therefore the exact next proof obligation is a Wick--Stein-contracted
fixed-dimensional transfer for the \(HA,T[p,A]\) cross-pairings, followed by
the mandatory 974/6519/17641-term comparison. Reusing the 66-entry
response-aware compiler would not discharge that obligation.

## 8. Parity and theorem boundary

Negating the initialized readout gives

\[
(D_n^kf_n)(-a)=(-1)^{k+1}(D_n^kf_n)(a),
\]

so \(\mathbb Ef_n=\mathbb ED_n^2f_n=\mathbb ED_n^4f_n=0\) exactly at every
width and depth.

Finite-width differentiation through order five is valid under
\(\phi\in C^5\) with an integrable polynomial envelope for
\(\phi^{(0)},\ldots,\phi^{(5)}\). For the direct annealed fixed-depth tensor
program bridge, a sufficient condition is

\[
\phi\in C^\infty,\qquad
|\phi^{(r)}(x)|\le C_r(1+|x|^{m_r})\quad(r\ge0).
\]

Alternatively, after separately proving convergence in probability, assume
for some \(\epsilon>0\)

\[
\sup_n\mathbb E|D_n^kf_n|^{1+\epsilon}<\infty,
\qquad k\in\{1,3,5\},
\]

to obtain uniform integrability and expectation convergence. These
hypotheses establish the accepted full response-aware formula at fixed
depth; they do not turn the partial scalar contraction above into a full
arbitrary-depth scalar witness.
