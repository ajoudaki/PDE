# Selected-source energy and metric bounds

These support lemmas use the existing source accuracy \(\epsilon=1/n\),
selected coordinates, metrics, and initialization-only construction. They
add no source family, retained coordinate, training hypothesis, or width gate.
The error theorem is proved in
[COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md).

The useful improvement is that the selected **raw dense readout**, and its
total variation, are at most \(3Y/\sqrt\lambda\). The previous bound
\(O(Y/\lambda)\) is unnecessary. Real selected backward fields likewise
have bounds polynomial in \(\beta^L\) times \(Y/\sqrt\lambda\).
These conclusions follow from source isometry and the existing dense
energy identity. They do not identify the selected optimizer with gradient
flow. Section 7 additionally proves total variation at most
\(3Y/\sqrt\lambda\) for the runtime's effective readout under the common
label cap, or at most \(5Y/\sqrt\lambda\) under the larger runtime
recurrence allowance.

## 1. Inputs, definitions, and scope

The source and selection interfaces are those of
[UNBOUNDED_COMPRESSOR_BRIDGE.md](UNBOUNDED_COMPRESSOR_BRIDGE.md).
The physical bounds come from
[GENERAL_EXPLICIT_FITTING.md](GENERAL_EXPLICIT_FITTING.md) and
[EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md](EXPLICIT_COMPRESSOR_RUNTIME_FITTING.md);
the power envelopes are those of
[SIMPLE_CONSTANTS_SOURCE_CHECK.md](SIMPLE_CONSTANTS_SOURCE_CHECK.md).

Let \(L\ge2\), let the training inputs \(v_a\in\mathbb R^d\) have norm
one, and let
\[
Y=\|y\|_2/\sqrt m>0,\qquad \lambda=\gamma/m>0,\qquad
\beta=\max\{10,1+b,16/a,s,t\},\qquad X=\beta^L.
\]
Here \(b=\max_j|\phi_j(0)|\), and \(s,t\) are the source's first and
second derivative bounds on the safe half-strip. The source's full-strip
holomorphy and bounded-first-derivative assumptions remain in force;
activation values need not be bounded. For the power bounds assume
\[
Y\le\lambda X^{-30},\qquad
\epsilon=1/n\le\min\{1,Y,S\},\qquad S=16Y/\lambda.
\tag{1}
\]
The last condition is already present in source §13. Write
\(z=Y/\lambda\) and \(\alpha=Y/\sqrt\lambda\) only as proof
abbreviations. The actual \(Y\) is retained in every scale below.

For dense neuron vectors, use
\(\langle u,v\rangle_n=u^\top v/n\) and
\(\|u\|_n=\|u\|_2/\sqrt n\). At layer \(j\), let \(R_j\) denote
coordinate restriction, and let the selected metric be \(M_j\), with
positive diagonal metric \(\mathsf D_j\). The construction gives
\[
\mathsf D_j/4\preceq M_j\preceq\mathsf D_j,
\quad \|\mathbf1\|_{M_j}=1,
\quad \|\mathbf1\|_{\mathsf D_j}\le2.
\tag{2}
\]
There is a fixed finite-dimensional source space \(E_j\) on which
\(R_j:E_j\to(\mathbb R^{q_j},M_j)\) is an exact isometry. Each of the
four existing actual source families has an approximant in this space
with coordinate error at most \(\epsilon\). Paired initialized images
are preserved exactly for their approximants. The initialized selected
operators have norm at most eight.

Unless specified otherwise, all selected-source conclusions are for
\(0\le t\le T=32\lambda^{-1}\log(en)\), uniformly over the real query
sphere. This is the domain covered by the existing source approximants.
The actual dense energy and fitting inputs hold for all real time; that
fact alone does not extend selected-source approximation past \(T\).
Zero labels give the separate exact stationary zero predictor.

The dense fitting input can be summarized self-containedly as follows.
Put \(q_0=1\),
\(q_j=\mathbb E\phi_j(\sqrt{q_{j-1}}Z)^2\) for \(Z\sim N(0,1)\), and
\[
H=\max(1,\sqrt{q_1},\ldots,\sqrt{q_L}),\quad
D_j=s(9s)^{L-j},
\quad
F=s^2\left[(9s)^{2L-2}+4H^2\sum_{k=0}^{L-2}(9s)^{2k}\right].
\tag{3}
\]
For \(c_a=y_a-f_n(v_a)\), \(\rho=\|c\|_2/\sqrt m\), its proved
conclusions include
\[
\begin{gathered}
\|h^j(t,v)\|_n\le2H,\qquad
\|w(t)\|_n\le2\alpha,\qquad
\|\delta^j(t,v)\|_n\le2D_j\alpha,\\
\rho(t)\le Ye^{-\lambda t/2},\qquad
\int_0^\infty\rho\le2z,\qquad
\int_0^\infty\|\dot\theta\|_{\rm par}\le2\alpha,\qquad
\|w(0)\|_n=0.
\end{gathered}
\tag{4}
\]
The parameter norm in (4) is
\(\|A\|_F^2/n+\sum_{j=2}^L\|W^j\|_F^2+\|w\|_n^2\).
The dense top training-feature Gram divided by \(m\) has gap at least
\(\lambda/4\).

The simple powers needed below are
\[
H\le(2\beta)^L\le X^2,\quad D_j\le X^2,\quad
\lambda\le H^2/m\le X^4,
\quad z\le X^{-30},\quad \alpha\le X^{-28},\quad X\ge100.
\tag{5}
\]
The gap upper bound follows from the diagonal \(q_L\) of the unweighted
covariance. In particular no assumption \(\lambda\le1\) is made.

The estimates stated before replacing constants by powers retain the
larger existing recurrence allowance. That allowance is the intersection
\[
z\le\min\left\{S_*^{\rm src}/16,
                  (8H\sqrt F)^{-1},
                  (16H_c\sqrt{F_c})^{-1}\right\},
\tag{6}
\]
with \(S_*^{\rm src}\) exactly the unchanged source recurrence (10).
For clarity, the runtime constants are
\[
\begin{gathered}
H^c_1=\max(1,2b+16s),\quad
H^c_j=\max(1,2b+18sH^c_{j-1}),\quad H_c=H^c_L,\\
D^c_j=2s(18s)^{L-j},\quad U^c_1=D^c_1,\quad
U^c_j=2H_cD^c_j\ (j\ge2),\\
F^c_1=2sU^c_1,\quad
F^c_j=2s(2H_cU^c_j+9F^c_{j-1}),\quad F_c=F^c_L.
\end{gathered}
\]
The scalar moment recurrence gives \(\sqrt\lambda\le H_c\), so (6)
implies \(\alpha\le1/(16\sqrt{F_c})\le1/16\). The source's power
audit proves that (1)'s label cap implies (6). We do not claim that the
larger interval (6) obeys every small power in (5).

## 2. Two elementary consequences of source isometry

If \(p\in E_j\) and \(\|u-p\|_\infty\le e\), then
\[
\|u-p\|_n\le e,\qquad
\|R_j(u-p)\|_{M_j}\le2e.
\]
The second bound follows by using the diagonal norm and
\(\|\mathbf1\|_{\mathsf D_j}\le2\). Isometry and the triangle
inequality give
\[
\|R_ju\|_{M_j}\le\|u\|_n+3e.
\tag{7}
\]
For vectors \(u,v\), approximants with errors \(e_u,e_v\), and dense
norm bounds \(U,V\), insert the approximants in each pairing. On the
dense side the error is at most
\(e_uV+e_vU+e_ue_v\). On the selected side it is at most
\(2e_uV+2e_vU+8e_ue_v\). Therefore
\[
|\langle R_ju,R_jv\rangle_{M_j}-\langle u,v\rangle_n|
\le3(e_uV+e_vU)+9e_ue_v.
\tag{8}
\]
The same argument works for different times, samples, and queries, since
the source space and metric are fixed.

For features write \(h_r^j=R_jh^j\), and for backward responses write
\(\delta_r^j=R_j\delta^j\). Equations (4), (7), and (1) give
\[
\|h_r^j\|_{M_j}\le2H+3\epsilon\le3X^2,
\qquad
\|\delta_r^j\|_{M_j}
\le2D_j\alpha+3\epsilon
\le(2D_j+3\sqrt\lambda)\alpha\le X^3\alpha.
\tag{9}
\]
For the second inequality, the already required \(\epsilon\le Y\)
gives \(\epsilon\le\sqrt\lambda\,\alpha\). This is also the correct
way to cover \(\lambda>1\); replacing \(\epsilon\) by \(\alpha\)
without this factor would be invalid.

Let
\[
V_r:\mathbb R^m\longrightarrow(\mathbb R^{q_L},M_L),\qquad
V_r\xi=m^{-1/2}\sum_a\xi_a h^L_{r,a}.
\]
Then sample Cauchy--Schwarz yields
\[
\|V_r\|\le
\left(m^{-1}\sum_a\|h^L_{r,a}\|_{M_L}^2\right)^{1/2}
\le3X^2.
\tag{10}
\]
There is no extra \(\sqrt m\).

## 3. Selected raw readout and integrated raw velocity

Define \(w_r=R_Lw\). The raw dense readout equation is
\[
\dot w=(2/m)\sum_a c_a h_a^L.
\]
Choose the existing continuous source approximants \(p_a(t)\in E_L\)
of \(h_a^L(t)\). For proof only, define
\[
p_w(t)=\int_0^t(2/m)\sum_a c_a(s)p_a(s)\,ds\in E_L.
\]
Finite-dimensionality and continuity justify membership in the fixed
source space. This is a proof witness, not a new runtime input or retained
array. Cauchy--Schwarz in samples gives
\[
\|w(t)-p_w(t)\|_\infty
\le2\epsilon\int_0^t\rho\le4z\epsilon.
\]
Equation (7) now improves the reference bound to
\[
\|w_r(t)\|_{M_L}\le2\alpha+12z\epsilon.
\tag{11}
\]
The same argument can be applied at each instant to
\(p_{\dot w}(t)=(2/m)\sum_a c_a(t)p_a(t)\). Its coordinate error
is at most \(2\rho(t)\epsilon\). Thus
\[
\|\dot w_r(t)\|_{M_L}
\le\|\dot w(t)\|_n+6\rho(t)\epsilon,
\qquad
\int_0^T\|\dot w_r(t)\|_{M_L}\,dt
\le2\alpha+12z\epsilon.
\tag{12}
\]
This proof uses approximants of the velocity obtained by taking the
residual-weighted combination of feature approximants. It does **not**
differentiate a coordinate approximation error.

Since \(z\epsilon/\alpha=\epsilon/\sqrt\lambda\le\alpha\), the
larger runtime allowance (6) already implies
\[
\sup_{t\le T}\|w_r(t)\|_{M_L}\le3\alpha,
\qquad
\int_0^T\|\dot w_r(t)\|_{M_L}\,dt\le3\alpha.
\tag{13}
\]
Indeed \(2+12\alpha\le11/4<3\). The sharper smallness (5) is not
needed here. The integrated bound is for the raw reference readout;
the effective runtime readout is a different object.

## 4. Selected true carriers

The top carrier is \(k_r^L=w_r\), already covered by (13). For
\(j<L\), expanding the exact learned dense mixer gives
\[
k^j(t,v)=W_0^{j+1\top}\delta^{j+1}(t,v)
 +\int_0^t\frac2m\sum_b c_b(s)h_b^j(s)
      \langle\delta_b^{j+1}(s),\delta^{j+1}(t,v)\rangle_n\,ds.
\tag{14}
\]
The first term is one existing initialized reverse-image source; all
vector factors in the integral are existing feature sources. Replacing
only these vector factors by their source approximants produces an
element of \(E_j\) with coordinate error at most
\[
e_k=\epsilon[1+16zD_{j+1}^2\alpha^2].
\tag{15}
\]
The scalar coefficients in (14) remain their exact dense values solely
for this proof witness. From (3), \(D_{j+1}^2\le F\), and the dense
allowance in (6) gives \(\alpha^2\le1/(64F)\) and \(z\le1/8\).
Consequently the bracket in (15) is at most \(33/32<2\). Dense
operator bounds give \(\|k^j\|_n\le2(9s)^{L-j}\alpha\). Applying
(7) and then (5) proves
\[
\|R_jk^j(t,v)\|_{M_j}
\le2(9s)^{L-j}\alpha+6\epsilon
\le[2(9s)^{L-j}+6\sqrt\lambda]\alpha
\le X^3\alpha.
\tag{16}
\]
This also does not enlarge the source space.

For training carrier **coordinates**, the different source estimate (23)
remains available:
\[
\max_{a,j,i}|k^j_{a,i}|
\le K_{\rm src}S\sqrt{\log(en)}
\le16X^{21}z\sqrt{\log(en)}.
\tag{17}
\]
RMS bounds (16) cannot replace (17) when an arbitrary changed coordinate
gate multiplies a reference carrier. A passive query carrier coordinate
maximum is not supplied by (17).

## 5. Pairing and product defects with actual label factors

Equation (8) gives, for any two feature sources and any two response
sources,
\[
\begin{aligned}
|\langle h_r,h'_r\rangle_M-\langle h,h'\rangle_n|
 &\le(12H+9\epsilon)\epsilon\le X^3\epsilon,\\
|\langle\delta_r,\delta'_r\rangle_M
      -\langle\delta,\delta'\rangle_n|
 &\le(12D_*\alpha+9\epsilon)\epsilon
 \le X^3\alpha\epsilon,
\end{aligned}
\tag{18}
\]
where \(D_*=\max_jD_j\). The final response estimate uses
\(\epsilon\le\sqrt\lambda\alpha\), not a label-independent bound.
Before the last simplification the coefficient is
\((12D_*+9\sqrt\lambda)\alpha\). This remains a valid finite
recurrence estimate under (6).

For a hidden-layer Gram term use the exact decomposition
\(a_rb_r-ab=(a_r-a)b_r+a(b_r-b)\), with \(a\) a response
pairing and \(b\) a feature pairing. Equations (4), (9), and (18)
then give
\[
|\langle\delta_r,\delta'_r\rangle
     \langle h_r,h'_r\rangle
 -\langle\delta,\delta'\rangle_n\langle h,h'\rangle_n|
\le X^7(9\alpha+4\alpha^2)\epsilon.
\tag{19}
\]
All pairings in a product use their own layer metric. This estimate
preserves the first and second powers of the actual
\(\alpha=Y/\sqrt\lambda\).

Let \(K_r\) be the algebraic dense residual-Gram formula with every
dense feature/response replaced by its restriction and every dense
neuron pairing replaced by the selected metric pairing. Then
\[
\left\|\frac{K_r-K_n}{m}\right\|_{\rm op}
\le\epsilon\left\{
X^3(1+\alpha)+(L-1)X^7(9\alpha+4\alpha^2)\right\}
\le X^4\epsilon.
\tag{20}
\]
The first inequality is an entrywise bound: the top features contribute
\(X^3\epsilon\), the first response pairing contributes
\(X^3\alpha\epsilon\) because \(|v_a^\top v_b|\le1\), and the
remaining terms use (19). A matrix with entries at most \(b\) in
absolute value has norm at most \(mb\); dividing by \(m\) removes
that factor. The final simplification follows from
\(L\le X\), \(\alpha\le X^{-28}\), and \(X\ge100\).

In particular, applying the first line of (18) to the feature Gram and
using \(\epsilon\le Y\le\lambda X^{-30}\) proves
\[
V_r^*V_r\succeq(\lambda/4-X^3\epsilon)I
\succeq\lambda I/8.
\tag{21}
\]
This introduces no new gap-dependent width gate. Consequently
\(\|V_r(V_r^*V_r)^{-1}\|\le\sqrt{8/\lambda}\).

The reference observation defect also keeps the actual label activity:
\[
\sup_v|f_n(t,v)-\langle w_r(t),h_r^L(t,v)\rangle_{M_L}|
\le4zX^3\epsilon.
\tag{22}
\]
Indeed integrate the exact readout equation and apply the first line of
(18) to the feature pairing at \((s,v_a)\) and \((t,v)\). The total
absolute residual activity is at most \(4z\). The same bound holds in
normalized sample norm for the observation-defect vector.

## 6. Exact reference hidden-velocity maps and action defects

Use the proof-only reference arrays from source §13: the exact selected
first weights \(A_r=R_1A\), the readout \(w_r=R_Lw\), and
\[
B_r^j(t)=B_0^j+
 \int_0^t\frac2m\sum_a c_a(s)
       \delta_{r,a}^j(s)\otimes_M h_{r,a}^{j-1}(s)\,ds.
\tag{23}
\]
Here \(u\otimes_M v\) is the rank-one map
\(x\mapsto u\langle v,x\rangle_M\). In the Hilbert--Schmidt norm
between the two metric neuron spaces it has norm \(\|u\|\|v\|\).

Let \(U_r:\mathbb R^m\to\mathcal H_{\rm hidden}\) be the linear
map into the direct sum of first-weight and hidden-matrix Hilbert spaces
whose columns, divided by \(\sqrt m\), are
\[
\left(\delta_{r,a}^1v_a^\top,
       (\delta_{r,a}^j\otimes_Mh_{r,a}^{j-1})_{j=2}^L\right).
\tag{24}
\]
Then the reference equations give exactly
\[
\dot\theta_{r,\rm hidden}=2U_r(c/\sqrt m),\qquad
\dot w_r=2V_r(c/\sqrt m),\qquad
K_r/m=V_r^*V_r+U_r^*U_r.
\tag{25}
\]
The last identity follows by expanding the inner products of the columns
in (24); it does not use a chain-rule identification of \(U_r\).
From (9),
\[
\|U_r\|\le X^3\alpha\sqrt{1+9(L-1)X^4}
\le X^6\alpha,
\quad
\int_0^T\|\dot\theta_{r,\rm hidden}\|
\le4X^6\frac{Y^2}{\lambda^{3/2}}.
\tag{26}
\]
The final power uses \(L\le X\) and \(X\ge100\).

Each reference hidden mixer has norm at most
\(8+12z\alpha X^5<9\) under (1), and the reference first-weight
operator is at most \(8+4z\alpha X^3<9\). These follow directly
from (23), (9), and \(\int2\rho\le4z\); in particular the
reference arrays also have an operator tube without adding a hypothesis.

For the reference forward/reverse action, paired initial approximants
give initial defect \(8(2\epsilon)+2\epsilon=18\epsilon\).
The learned-action formula and (18) then give
\[
\begin{aligned}
\|B_r^jh_r^{j-1}-R_j(W^jh^{j-1})\|_{M_j}
 &\le[18+4z\alpha X^6]\epsilon,\\
\|(B_r^{j+1})^*\delta_r^{j+1}
        -R_j(W^{j+1\top}\delta^{j+1})\|_{M_j}
 &\le[18+12z\alpha X^5]\epsilon.
\end{aligned}
\tag{27}
\]
Both hold for queries in the existing source families. In the first
line, the learned defect is the selected response norm times a forward
pairing defect integrated against \(2\rho\). In the second it is the
selected feature norm times a response pairing defect. The selected
adjoint is always the metric adjoint. These improvements retain
\(z\alpha=Y^2/\lambda^{3/2}\); the initialized action defect remains
\(18\epsilon\).

## 7. Total variation of the runtime's effective readout

The raw and effective readouts must be distinguished, but the latter also
admits an \(O(Y/\sqrt\lambda)\) total-variation estimate. This additional
argument uses only the already proved runtime fitting bounds and applies
on the entire real-time half-line.

In this section \(V=[h_C^L(v_a)]_a/\sqrt m\) is the **actual runtime**
feature map. Let \(U\) be its hidden velocity map, defined by the same
column formula as (24) using the runtime's actual features and specified
backward responses. Put
\[
q=V^*V,\quad T_V=Vq^{-1},\quad P=T_VV^*,\quad
\xi=c_C/\sqrt m,\quad b_C=(y-c_C)/\sqrt m.
\]
The runtime equations give exact algebraic identities
\[
K_C/m=V^*V+U^*U,\quad
\dot w_C=2V\xi,\quad
\dot b_C=2(V^*V+U^*U)\xi,\quad
\widehat w_C=(I-P)w_C+T_Vb_C.
\tag{28}
\]
They use metric Hilbert adjoints; none asserts that the backward gates
are gradient adjoints. Since \(\dot w_C\in\operatorname{ran}V\),
\((I-P)\dot w_C=0\). Also \(T_VV^*V=V\). Differentiating the last
identity in (28) therefore gives the more useful exact formula
\[
\dot{\widehat w}_C
=\dot w_C-\dot P w_C+\dot T_Vb_C+2T_VU^*U\xi.
\tag{29}
\]
This avoids estimating the entire residual Gram in the last term.

The normalized gap is \(q\succeq\lambda I/4\), hence
\(\|T_V\|\le2/\sqrt\lambda\). Differentiating the inverse and
collecting projectors yields
\[
\dot T_V=(I-P)\dot Vq^{-1}-T_V\dot V^*T_V,\qquad
\dot P=(I-P)\dot VT_V^*+T_V\dot V^*(I-P).
\]
Consequently
\[
\|\dot T_V\|\le8\|\dot V\|/\lambda,\qquad
\|\dot P\|\le4\|\dot V\|/\sqrt\lambda.
\tag{30}
\]
The runtime bounds give \(\|w_C\|\le2\alpha\),
\(\|\widehat w_C\|\le5\alpha\), \(\|b_C\|\le2Y\),
\(\int\|\dot w_C\|\le2\alpha\), and
\(\int\rho_C\le2z\). Its actual forward derivative recurrence gives
\(\|\dot V\|\le10\alpha F_c\rho_C\), so
\[
\int_0^\infty\|\dot V\|\le20\alpha F_cz.
\tag{31}
\]
There is no derivative-of-source-error issue for this actual forward
pass.

Unrolling the runtime recurrence defining \(F_c\) gives the identity
\[
F_c=(D^c_1)^2+4H_c^2\sum_{j=2}^L(D^c_j)^2.
\tag{32}
\]
Indeed the first term is
\(4s^2(18s)^{2L-2}\), and the later forcing terms sum to
\(16s^2H_c^2\sum_{k=0}^{L-2}(18s)^{2k}\). Since runtime features
have norm at most \(2H_c\) and responses at most
\(5\alpha D^c_j\), the column bound gives
\(\|U\|^2\le25\alpha^2F_c\).

Integrate (29). The two projector-derivative terms total at most
\[
\left(\frac{8\alpha}{\sqrt\lambda}
           +\frac{16Y}{\lambda}\right)
\int\|\dot V\|
\le480\alpha F_cz^2.
\]
The hidden Gram term contributes at most
\[
\frac4{\sqrt\lambda}(25\alpha^2F_c)\int\rho_C
\le200\alpha F_cz^2,
\]
where \(\alpha/\sqrt\lambda=z\). We have proved
\[
\int_0^\infty\|\dot{\widehat w}_C\|\,dt
\le\alpha(2+680F_cz^2).
\tag{33}
\]
Under the **larger** runtime allowance in (6),
\(F_cz^2\le1/(256H_c^2)\le1/256\), so (33) is at most
\((149/32)\alpha<5\alpha\). Under the common cap (1), the checked
envelope \(F_c\le X^{15}\) gives the sharper convenient conclusion
\[
\int_0^\infty\|\dot{\widehat w}_C\|\,dt\le3\alpha.
\tag{34}
\]
For completeness, the same runtime estimates give
\(\|V\|\le2X^3\), \(\|U\|\le5X^{15/2}\alpha\); a sharper
direct use of \(D^c_j\le X^3\), \(H_c\le X^3\), and \(L\le X\)
gives \(\|U\|\le X^7\alpha\).

## 8. Metric rules and scope

The following points are necessary when using these bounds in a coupled
stability argument.

1. **True restrictions versus a reference forward pass.** The feature
   \(h_r^j=R_jh^j\) and response \(\delta_r^j=R_j\delta^j\) are the
   restrictions of actual dense fields. They need not equal the fields
   obtained by running the selected forward/backward recursions through
   \((A_r,B_r,w_r)\). Their discrepancy is governed by (27). In
   particular (25) does not assert that \(U_r\) is the adjoint derivative
   of this reference forward pass.

2. **A coordinate gate is not self-adjoint in the selected metric.** For
   \(D=\operatorname{diag}(\phi'(z))\),
   \(D^*=M^{-1}DM\), which can differ from \(D\). Metric comparison
   does prove \(\|D\|_{M\to M}\le2s\). If the true reference carrier
   has coordinate maximum \(M_k\), it also proves
   \[
   \|(D(z)-D(z'))k\|_M\le2tM_k\|z-z'\|_M.
   \]
   The specified optimizer uses \(D\), not \(D^*\). Therefore its
   algebraic positive Gram and raw energy identity do not imply a
   cross-trajectory gradient-Hessian cancellation. The comparison in
   [COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md)
   uses its exact readout cancellation and bounds the hidden-Gram term
   in absolute value.

3. **Reference feature derivatives are not supplied by coordinate
   accuracy alone.** Bounds (11)--(12) are valid because the readout
   velocity is an exact residual-weighted combination of feature sources.
   A bound on \(\dot V_r\) cannot be obtained merely by differentiating
   \(\|h-p_h\|_\infty\le\epsilon\). Nor may the reference hidden
   velocities (25) be substituted into a selected chain rule as if the
   reference fields were its own forward pass. A proof requiring
   \(\dot V_r\), a derivative of (27), or a mixed response field needs
   an additional derivation. No such derivative estimate is claimed here;
   the comparison proof does not require it.

4. **Raw versus effective readout.** Equations (13) concern \(w_r\).
   Equations (33)--(34) concern the actual runtime's
   \(\widehat w_C\), and require the exact cancellation in (29).
   Merely integrating its older crude endpoint derivative coefficient
   would not give this conclusion. Neither estimate identifies the
   proof-reference fields with the runtime's forward pass.

5. **General gap and larger label interval.** Use
   \(\sqrt\lambda\le H\le X^2\) and
   \(\epsilon\le\sqrt\lambda\alpha\), rather than imposing
   \(\lambda\le1\). Equations (7)--(8), (11)--(16), and the
   unsimplified versions of (18)--(20), (23)--(27) retain the full
   recurrence allowance (6). The small polynomial envelopes and strict
   margin (21) displayed here use the common cap (1). A final theorem
   must state which allowance its new stability estimate covers.

The source and selection interfaces remain inherited hypotheses on the
existing probability event. This note supplies deterministic estimates
conditional on that event and its already verified fitting bounds. It
does not quantify the stochastic success width, change the source
construction gates. The polynomial-error conclusions and their label ranges
are given in [COMPACT_POLYNOMIAL_COMPARISON.md](COMPACT_POLYNOMIAL_COMPARISON.md)
and [COMPACT_FULL_LABEL_RANGE.md](COMPACT_FULL_LABEL_RANGE.md).
