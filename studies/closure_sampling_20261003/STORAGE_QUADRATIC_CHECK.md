# Independent check of the quadratic-storage runtime

2026-10-04. Scoped internal mathematical check, not a promotion review.

**Verdict: the conditional source-to-runtime theorem passes.** The dense
non-diagonal metric, corrected readout, autonomous dynamics, global fitting,
same-physical-time comparison and total retained count are consistent. No
additional label restriction is needed beyond the supplied source regime.
The compressed optimizer is a different, explicitly specified optimizer;
its matrix \(K_C\) is not its parameter-gradient tangent Gram. The conclusion
would not establish the stronger requirement of ordinary gradient flow.

This report derives the estimates needed for that verdict. It also supplies
a dimension-independent tail argument where the candidate appeals to local
smoothness, and records three wording/assumption clarifications at the end.

## Scope and frozen inputs

The only scientific files read were the following complete assigned files:

| File | SHA-256 |
| --- | --- |
| `STORAGE_QUADRATIC_IMPROVEMENT.md` | `b376b2f04da5d80ffaac2c56a1bbbd378f498bc657369cbdd834b5fafcc8993c` |
| `GENERAL_ANALYTIC_COMPRESSION.md` | `4fd314dd28367430cd60fa8b88fe0eb4d9b12f575c61aadd60ff61dff76dec53` |
| `GENERAL_WEIGHTED_COMPARISON.md` | `1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306` |
| `DATASET_MAXIMUM_REFINEMENT.md` | `7bd09a922c5dcaaee1f4dd6ab5af8ce9c8a4991b2d04a1f01017a8d06cde529a` |

Shared instructions and the required canonical-notation and rigorous-math
skills, including the neural-network reference, were also read. No study
history, README, other route report, other study, book, external proof or
experiment was accessed. BSS is assumed in precisely the form authorized
by the assignment; its applicability is checked below.

The deep source construction and its probability proof are inputs, not
reproved here. In particular the candidate's displayed explicit bound on

\[
R\le C\{\lambda^{-1}(\ell_n^a+m\ell_n^b)+d\},\qquad
\ell_n=\log(en),\quad a=d(L+5)+1,\quad b=L+6,
\tag{A}
\]

is treated as a supplied source bound. Its fully parameter-tracked
derivation is not contained in the assigned sources: the candidate names
`DATASET_DEPENDENCE.md` and `DATASET_NORMALIZATION_ASSESSMENT.md`, which
were outside scope. The check below proves the claimed runtime and storage
implication from (A), rather than independently certifying those missing
source calculations. The assigned analytic-compression note supplies the
initialization-only source mechanism and paired-coefficient requirement;
the assigned maximum-refinement note supplies the stated larger label
regime as an input conclusion.

## 1. Model, norms and source hypotheses

Let \(v=x/\sqrt d\), with training vectors \(v_a\) of Euclidean norm one.
The original width-\(n\) network has

\[
z_n^{(1)}=A_nv,\quad z_n^{(\ell)}=W_n^{(\ell)}h_n^{(\ell-1)},
\quad h_n^{(\ell)}=\phi_\ell(z_n^{(\ell)}),\quad
f_n=w_n^\top h_n^{(L)}/n.
\]

Write \(c_{n,a}=y_a-f_n(x_a)\),

\[
\|u\|_n^2=u^\top u/n,\qquad
\|c\|_m^2=c^\top c/m,\qquad Y=\|y\|_m.
\]

Its fixed canonical equations are

\[
\dot A_n=\frac2m\sum_a c_{n,a}\delta_{n,a}^{(1)}v_a^\top,
\quad
\dot W_n^{(\ell)}=\frac2{mn}\sum_a
c_{n,a}\delta_{n,a}^{(\ell)}h_{n,a}^{(\ell-1)\top},
\quad
\dot w_n=\frac2m\sum_a c_{n,a}h_{n,a}^{(L)},
\tag{1}
\]

where \(k_{n,a}^{(L)}=w_n\),
\(\delta_{n,a}^{(\ell)}=\phi_\ell'(z_{n,a}^{(\ell)})\odot
k_{n,a}^{(\ell)}\), and
\(k_{n,a}^{(\ell)}=W_n^{(\ell+1)\top}\delta_{n,a}^{(\ell+1)}\).
The proposed construction changes none of these equations, their Gaussian
initialization, the zero initial readout, the data or physical time.

The source input supplies fixed spaces \(S_\ell\), of dimensions at most
\(R\), with coordinate error at most \(\epsilon=n^{-1}\) for every
feature, training backward response, and each paired initialized forward
or transpose image on the source horizon \(T=C\lambda^{-1}\ell_n\).
For a paired approximant \(s\), its exact image \(W_0s\) or
\(W_0^\top s\) belongs to the appropriate adjacent space, and *each*
member approximates its corresponding true source to coordinate error
\(\epsilon\). This last condition is essential.

The source input also supplies

\[
\rho_n(t):=\|c_n(t)\|_m\le Ye^{-c\lambda t},\quad
\int_0^\infty\rho_n(t)dt\le S:=CY/\lambda,\quad
M\le1+CS\sqrt{\ell_n},
\tag{2}
\]

where \(M\ge1\) bounds all original training-carrier coordinates through
\(T\). The original operator bounds are structural, and \(S\) is small.
Below \(C\) depends on fixed depth, input dimension, activation bounds and
the fixed initial operator bounds, but not on \(n,m,\lambda,Y\), selected
node count or minimum selected weight unless displayed. We assume the
initialized empirical normalized Gram has gap at least \(c_0\lambda\),
as supplied by the source event.

The activations and their first two derivatives are bounded. This follows
from the assigned strip hypothesis and suffices for the runtime proof.

## 2. Sparse restriction and the non-diagonal metric

In one layer let \(U^\top U/n=I_r\) and include the constant vector in
\(S=\operatorname{range}(U)\). Set \(q_i=U_{i,:}^\top/\sqrt n\).
Then

\[
\sum_{i=1}^n q_iq_i^\top=U^\top U/n=I_r.
\]

These are exactly the hypotheses of the assumed BSS specialization. Its
positive support has \(N\le9r\); with \(P=U_I\) and
\(D=\operatorname{diag}(s_i/n)\), it gives

\[
I\preceq G:=P^\top DP\preceq4I.
\]

The constant vector has coefficient vector of norm one, so
\(1\le\mathbf1^\top D\mathbf1\le4\). All retained diagonal entries
of \(D\) are positive. There is no \(r=0\) case after adding the constant.

Put \(Z=D^{1/2}P\). The columns of \(ZG^{-1/2}\) are orthonormal,
so \(ZG^{-1}Z^\top\) is the orthogonal projection onto
\(\operatorname{range}(Z)\). On this range the operator
\(ZG^{-2}Z^\top\) is orthogonally equivalent to \(G^{-1}\); it is
zero on the orthogonal complement. Therefore

\[
H=D^{1/2}[ZG^{-2}Z^\top+I-ZG^{-1}Z^\top]D^{1/2}
\]

satisfies

\[
\tfrac14D\preceq H\preceq D,\qquad
P^\top HP=GG^{-2}G+G-GG^{-1}G=I.
\tag{3}
\]

Thus \(\|s_I\|_H=\|s\|_n\) for every \(s\in S\), and
\(\|e_I\|_H\le2\epsilon\) whenever \(\|e\|_\infty\le\epsilon\).
For any real diagonal matrix \(J\),

\[
\|Jx\|_H\le\|Jx\|_D\le\|J\|_\infty\|x\|_D
\le2\|J\|_\infty\|x\|_H.
\tag{4}
\]

The pointwise mean-value formula and (4) give
\(\|\phi(x)-\phi(y)\|_H\le2\|\phi'\|_\infty\|x-y\|_H\),
and similarly for \(\phi'\). Also
\(\|\phi(x)\|_H\le2\|\phi\|_\infty\). None of these estimates
uses the smallest entry of \(D\), or any entry of \(H^{-1}\) separately.

For adjacent spaces define

\[
C_0=U_\ell^\top W_0^{(\ell)}U_{\ell-1}/n,\qquad
B_0^{(\ell)}=P_\ell C_0P_{\ell-1}^\top H_{\ell-1}.
\]

The normalized full bases \(U_\ell/\sqrt n\) and selected bases
\(P_\ell\) are isometries in their respective norms. Consequently
\(\|B_0^{(\ell)}\|\le\|C_0\|\le\|W_0^{(\ell)}\|\).
If \(s=U_{\ell-1}\alpha\) and \(W_0^{(\ell)}s=U_\ell\beta\),
then \(\beta=C_0\alpha\), so \(B_0^{(\ell)}s_I=(W_0^{(\ell)}s)_I\).
The weighted adjoint equals

\[
B_0^{(\ell)*}=P_{\ell-1}C_0^\top P_\ell^\top H_\ell.
\]

It gives the corresponding exact transpose identity for every exact
paired reverse approximant. Exact initial training features and their
forward images therefore give exact initial selected training passes by
induction, and exact preservation of the initial top Gram.

These exact identities concern vectors in the paired spaces. The actions
on the actual moving sources have an error, derived in Section 5 below.

## 3. Own residual, autonomy and the energy identity

Use the candidate's forward pass and fixed metrics. Let \(F_C\) contain
the current top training features and let \(Q_C=F_C^\top H_LF_C\).
For positive definite \(Q_C\), define

\[
\widehat w_C=w_C+F_CQ_C^{-1}
(y-c_C-F_C^\top H_Lw_C),\qquad
f_C(x)=\widehat w_C^\top H_Lh_C^{(L)}(x).
\tag{5}
\]

Multiplying by \(F_C^\top H_L\) gives
\(F_C^\top H_L\widehat w_C=y-c_C\). Thus \(c_C\) is identically
the residual of this output. In particular \(w_C(0)=0,c_C(0)=y\)
give \(\widehat w_C(0)=0\) and matching initial predictions.

Use \(\widehat w_C\), ordinary pointwise gates, and \(H\)-adjoints
of the mixers to define the training signals. Let \(g_a\) be the tuple
of raw parameter directions

\[
g_a=\left(\delta_{C,a}^{(1)}v_a^\top,
 \bigl(\delta_{C,a}^{(\ell)}h_{C,a}^{(\ell-1)\top}H_{\ell-1}
 \bigr)_{\ell=2}^L,h_{C,a}^{(L)}\right).
\]

Equip this tuple space with the candidate's parameter norm: the first
matrix has norm \(\|H_1^{1/2}A\|_F\), a mixer has norm
\(\|H_\ell^{1/2}BH_{\ell-1}^{-1/2}\|_F\), and the raw readout
has norm \(\|w\|_{H_L}\). Expanding the inner product of \(g_a,g_b\)
gives exactly the candidate's \(K_{C,ab}\), including the factor
\(v_a^\top v_b\) in the first-layer term. In particular \(K_C\)
is a Gram matrix and \(K_C\succeq Q_C\).

The raw parameter tuple \(\theta_C=(A_C,B_C,w_C)\) evolves by
\(\dot\theta_C=(2/m)\sum_a c_{C,a}g_a\), and the extra state evolves
by \(\dot c_C=-(2/m)K_Cc_C\). Therefore

\[
\|\dot\theta_C\|_{\rm par}^2
=\frac4{m^2}\sum_{a,b}c_{C,a}c_{C,b}\langle g_a,g_b\rangle_{\rm par}
=\frac4{m^2}c_C^\top K_Cc_C
=-\frac{d}{dt}\|c_C\|_m^2.
\tag{6}
\]

All cross-sample terms are included. This proves the energy identity
without mistaking the training signals for true output derivatives.
The algebraic formula (5) makes the loss \(\|c_C\|_m^2\), so (6)
is also its actual dissipation identity.

Every quantity in these equations is evaluated from current compressed
state, fixed small matrices and retained training data. The system is a
smooth autonomous ODE on \(Q_C\succ0\). The readout correction is
part of that ODE's output definition, not an externally prescribed
residual or reference prediction.

## 4. Global fitting under the existing label condition

Stop while the mixer operator norms remain in a fixed bounded tube and
\(Q_C/m\succeq gI\), where \(g=c\lambda\) is a fixed fraction of
the preserved initial margin. Put \(\rho_C=\|c_C\|_m\). By (6),

\[
-\dot\rho_C\ge2g\rho_C,\qquad
\|\dot\theta_C\|_{\rm par}^2=2\rho_C(-\dot\rho_C)
\le\frac{(-\dot\rho_C)^2}{g}.
\]

At zero residual the velocities vanish, so the same integrated estimate
holds across that case. Starting with \(\rho_C(0)=Y\),

\[
\rho_C(t)\le Ye^{-2gt},\qquad
\int_0^t\|\dot\theta_C\|_{\rm par}\,ds\le Y/\sqrt g,
\qquad\int_0^t\rho_C(s)ds\le Y/(2g).
\tag{7}
\]

The operator \(P_C=F_CQ_C^{-1}F_C^\top H_L\) is the orthogonal
projection in the \(H_L\) inner product onto \(\operatorname{range}(F_C)\).
Rewrite (5) as

\[
\widehat w_C=(I-P_C)w_C+F_CQ_C^{-1}(y-c_C).
\]

Its two terms are orthogonal, and

\[
\|F_CQ_C^{-1}(y-c_C)\|_{H_L}^2
=(y-c_C)^\top Q_C^{-1}(y-c_C)
\le g^{-1}\|y-c_C\|_m^2\le4Y^2/g.
\]

Together with (7), this gives \(\|\widehat w_C\|_{H_L}\le CY/\sqrt\lambda\).
The bounded diagonal multipliers (4) and bounded mixer adjoints then give
the same bound for every backward signal norm, uniformly in sample and
layer. A rank-one update has parameter norm equal to the product of its
two vector norms. Hence each hidden parameter velocity has norm at most
\(C(Y/\sqrt\lambda)\rho_C\), and

\[
\|A_C(t)-A_C(0)\|+
\sum_{\ell=2}^L\|B_C^{(\ell)}(t)-B_C^{(\ell)}(0)\|_{\rm HS}
\le CY^2/\lambda^{3/2}.
\tag{8}
\]

For the first layer, its preactivation change is bounded by the first
matrix displacement since \(\|v\|_2=1\). At every later layer split

\[
B_C(t)h_C(t)-B_C(0)h_C(0)
=[B_C(t)-B_C(0)]h_C(t)+B_C(0)[h_C(t)-h_C(0)].
\]

The bounded features and (4) propagate (8) through fixed depth. Every
training or sphere-query feature displacement is at most
\(CY^2/\lambda^{3/2}\). For the normalized training feature matrix,

\[
\left\|H_L^{1/2}[F_C(t)-F_C(0)]/\sqrt m\right\|_{\rm op}
\le\left(\frac1m\sum_a
\|h_{C,a}^{(L)}(t)-h_{C,a}^{(L)}(0)\|_{H_L}^2\right)^{1/2}
\le CY^2/\lambda^{3/2}.
\tag{9}
\]

Its initial smallest singular value is at least \(\sqrt{c_0\lambda}\).
If \(Y\le c\lambda\), the right side of (9) is a sufficiently small
fraction of this singular value. Equation (8) also keeps the mixers
strictly inside their tube. A first-exit argument therefore closes both
conditions globally.

The assigned refined source regime

\[
0<Y\le c\lambda e^{-C\sqrt{\log(em)}}
\tag{10}
\]

implies \(Y\le c\lambda\). The runtime requires no further sample or
label penalty. For each fixed selected system, the resulting state bounds
and positive Gram margin prevent finite-time escape from the smooth ODE
domain. The path-length bound in (7) makes every raw parameter converge;
\(c_C\to0\), the limiting Gram remains positive definite, and (5) gives
a convergent effective readout. The limiting output interpolates exactly.
For \(Y=0\) all outputs can remain identically zero.

## 5. Actual source defects in both mixer orientations

Here all unmarked full-width sources belong to the original network.
If \(u=s+e\), with \(s\in S\) and \(\|e\|_\infty\le\epsilon\),
then

\[
\|u_I\|_H\le\|s\|_n+2\epsilon\le\|u\|_n+3\epsilon.
\]

For another source \(v=t+f\), expand the selected and empirical pairings
around \(s,t\). Their \(s,t\) terms agree exactly by (3); every remaining
term contains at least one error vector. Cauchy--Schwarz gives

\[
\bigl|\langle u_I,v_I\rangle_H-\langle u,v\rangle_n\bigr|
\le C\epsilon(\|u\|_n+\|v\|_n+\epsilon).
\tag{11}
\]

This applies at different times as well as at the same time. In the
present regime all required source RMS norms are structurally bounded.
Original backward norms are at most \(CS\), and their selected norms
are at most \(CS+3\epsilon\). Taking the allowed width sufficiently
large to make \(\epsilon\le Y\) keeps them bounded uniformly as well.

For paired approximants \(s,W_0s\), the exact initial action in Section 2
and the separate errors of the two members yield

\[
\|B_0u_I-(W_0u)_I\|_H
\le\|B_0\|\|(u-s)_I\|_H+\|(W_0s-W_0u)_I\|_H
\le C\epsilon.
\tag{12}
\]

The transpose version is identical with \(B_0^*\) and the reverse pair.
It would be invalid to replace the second coordinate-error hypothesis by
an original operator-norm bound; this proof does not make that replacement.

Define \(A_R=A_{n,I_1}\), \(w_R=w_{n,I_L}\) and, for proof only,

\[
B_R^{(\ell)}=B_0^{(\ell)}+
\frac2m\sum_a\int_0^t c_{n,a}(s)
\delta_{n,a}^{(\ell)}(s)_{I_\ell}
h_{n,a}^{(\ell-1)}(s)_{I_{\ell-1}}^\top H_{\ell-1}\,ds.
\tag{13}
\]

The original rank-one integral formula for \(W_n^{(\ell)}\) has the
same expression with empirical pairings. Applying (13) to a true selected
current feature makes the learned difference exactly

\[
\frac2m\sum_a\int_0^t c_{n,a}(s)\delta_{n,a}^{(\ell)}(s)_{I_\ell}
\left[
\langle h_{n,a}^{(\ell-1)}(s)_I,h_n^{(\ell-1)}(t,x)_I\rangle_H
-\langle h_{n,a}^{(\ell-1)}(s),h_n^{(\ell-1)}(t,x)\rangle_n
\right]ds.
\]

Its norm is at most \(CS^2\epsilon\) by (11), Cauchy--Schwarz over
the samples and (2). Adding (12) proves the forward action defect
\(C\epsilon\). For the reverse action, the analogous learned difference
is a past selected feature multiplied by the pairing defect between the
past and present backward responses. Equations (11) and (2) again give
\(C\epsilon\). Thus

\[
\|B_R^{(\ell)}h_n^{(\ell-1)}(t,x)_I-z_n^{(\ell)}(t,x)_I\|_{H_\ell}
\le C\epsilon,
\quad
\|B_R^{(\ell+1)*}\delta_{n,a}^{(\ell+1)}(t)_I-k_{n,a}^{(\ell)}(t)_I\|_{H_\ell}
\le C\epsilon.
\tag{14}
\]

These formulas also bound all \(B_R\) operator norms. For the readout,
use \(w_n(t)=(2/m)\sum_a\int_0^t c_{n,a}(s)h_{n,a}^{(L)}(s)ds\)
and apply (11) directly inside this integral. This avoids any issue with
choosing measurable approximants and gives

\[
|\langle w_R,h_n^{(L)}(t,x)_I\rangle_{H_L}-f_n(t,x)|
\le CS\epsilon\le C\epsilon.
\tag{15}
\]

The selected raw reference readout is bounded by \(CS\), by the same
integral and the selected feature bound.

## 6. Full nonlinear feedback and physical-time comparison

Let \(d(t)\) be the sum of the first-matrix, mixer Hilbert--Schmidt and
raw-readout distances between the compressed state and (13), in the
metrics already defined. Set \(u(t)=\|c_C-c_n\|_m\) and \(E=d+u\).
All these quantities initially vanish. Global fitting already supplies
the compressed Gram and operator bounds used below.

At the first layer, the preactivation difference is at most \(d\).
At later layers, split the forward difference into
\((B_C-B_R)h_{n,I}\), the propagated lower-feature difference through
\(B_C\), and the action defect (14). Equation (4) then gives uniformly
over sphere queries

\[
\max_\ell\{\|z_C^{(\ell)}-z_{n,I}^{(\ell)}\|_{H_\ell}
+\|h_C^{(\ell)}-h_{n,I}^{(\ell)}\|_{H_\ell}\}
\le C(d+\epsilon).
\tag{16}
\]

For \(r=y-c_C-F_C^\top H_Lw_C\), insert the actual original output,
(15), and (16). The selected original readout is bounded, so
\(\|r\|_m\le u+C(d+\epsilon)\). Since

\[
\|F_CQ_C^{-1}r\|_{H_L}^2=r^\top Q_C^{-1}r
\le C\lambda^{-1}\|r\|_m^2,
\]

equation (5) implies

\[
\|\widehat w_C-w_R\|_{H_L}
\le C\lambda^{-1/2}(E+\epsilon).
\tag{17}
\]

For backward subtraction, use precisely

\[
\delta_C-\delta_{n,I}
=\phi'(z_C)\odot(k_C-k_{n,I})
+[\phi'(z_C)-\phi'(z_{n,I})]\odot k_{n,I}.
\]

The second term is a bounded diagonal multiplier of \(z_C-z_{n,I}\),
with multiplier bound \(\|\phi''\|_\infty M\); by (4) it costs
\(CM(d+\epsilon)\). The carrier difference at the next lower layer
splits into the propagated upper-response difference, the matrix
difference applied to the selected true response, and (14). These cost
\(C\|\delta_C^{(\ell+1)}-\delta_{n,I}^{(\ell+1)}\|+Cd+C\epsilon\).
Beginning with (17) and descending through fixed depth gives

\[
\max_{a,\ell}\|\delta_{C,a}^{(\ell)}-\delta_{n,a,I}^{(\ell)}\|_{H_\ell}
\le \beta(E+\epsilon),\qquad
\beta=C\lambda^{-1/2}(1+M).
\tag{18}
\]

The recursion adds one \(M\)-term per layer; it does not multiply by
\(M\) on each downward step. No compressed coordinate-carrier estimate
or minimum-mass bound has been assumed.

The original canonical tangent Gram \(K_n\) has the same formula as
\(K_C\), with empirical pairings and original responses. Direct
differentiation of (1) gives \(\dot c_n=-(2/m)K_nc_n\). Expand every
Gram-pair difference using (11), (16), (18) and the bounded response
norms. Each entry satisfies
\(|K_{C,ab}-K_{n,ab}|\le C\beta(E+\epsilon)\). A matrix whose entries
are bounded by \(b\) has operator norm at most \(mb\), so

\[
\|(K_C-K_n)/m\|_{\rm op}\le C\beta(E+\epsilon).
\tag{19}
\]

Let \(e=c_C-c_n\). Its exact equation is

\[
\dot e=-2(K_C/m)e-2[(K_C-K_n)/m]c_n.
\]

Taking the Euclidean inner product with \(e\), dividing by its RMS
norm, and using the gap gives, in the upper-derivative sense also at zero,

\[
D^+u\le-c\lambda u+C\beta\rho_n(E+\epsilon).
\tag{20}
\]

Integrating with \(u(0)=0\), or first regularizing the norm, gives

\[
\int_0^t u(s)ds\le C\beta\lambda^{-1}
\int_0^t\rho_n(E+\epsilon)ds,
\qquad
u(t)\le C\beta\int_0^t\rho_n(E+\epsilon)ds.
\tag{21}
\]

Subtract each raw velocity from its reference velocity. For a mixer the
exact decomposition is a residual difference times the compressed
rank-one direction, plus the original residual times a response difference
and a feature difference. First-layer and readout updates are the same
decomposition with fewer factors. Their norms are bounded by
\(Cu+C\beta\rho_n(E+\epsilon)\). Integration therefore gives

\[
d(t)\le C\int_0^t u(s)ds+
C\beta\int_0^t\rho_n(E+\epsilon)ds.
\]

Combining with (21), using \(\lambda\le1\), and writing
\(A=C\lambda^{-3/2}(1+M)\) proves

\[
E(t)\le A\int_0^t\rho_n(s)[E(s)+\epsilon]ds,
\qquad
E(t)+\epsilon\le\epsilon\exp\left(A\int_0^t\rho_n(s)ds\right).
\tag{22}
\]

The latter follows by differentiating the integral majorant with initial
value \(\epsilon\). The controlling integral is residual activity,
not physical elapsed time. All actual paired-source errors and the
correction's dependence on the residual state enter this estimate.

Equations (15)--(17) imply the query output estimate

\[
\sup_{t\le T,x}|f_C(t,x)-f_n(t,x)|
\le C\lambda^{-1/2}\epsilon
\exp[C\lambda^{-3/2}(1+M)S].
\tag{23}
\]

Using (2) and \(\epsilon=n^{-1}\) gives exactly the candidate's bound

\[
C\lambda^{-1/2}e^{CY/\lambda^{5/2}}n^{-1}
\exp\{(CY^2/\lambda^{7/2})\sqrt{\ell_n}\}.
\tag{24}
\]

If \(\ell_n\ge C(1+Y^4/\lambda^7)\), with a sufficiently large
structural constant, the final exponential is at most \(C\sqrt n\).
Thus the displayed finite-horizon root-width estimate has the asserted
explicit conditioning dependence. This is a fixed-dataset width threshold;
it is not a growing-dataset theorem or a uniform threshold as \(Y\downarrow0\).

## 7. Uniform tail and the fitted endpoint

The candidate's local-smoothness tail statement can be justified without
Euclidean constants depending on the selected width or minimum weight.
Here is a direct derivation in the preceding norms.

Set \(V=F_C/\sqrt m\), \(q=Q_C/m=V^*V\),
\(b=(y-c_C)/\sqrt m\), where the adjoint is from \(H_L\) to Euclidean
sample space. Then

\[
T_V=Vq^{-1},\quad P_V=T_VV^*,\quad
\widehat w_C=(I-P_V)w_C+T_Vb.
\]

Globally \(\|V\|\le C\), \(q\succeq gI\),
\(\|T_V\|\le g^{-1/2}\), and \(\|P_V\|\le1\).
The actual feature derivative is bounded by forward differentiation and
(4):

\[
\|\dot V\|\le C\|\dot\theta_{C,\mathrm{hidden}}\|_{\rm par}
\le C(Y/\sqrt\lambda)\rho_C.
\]

Consequently \(\|\dot q\|\le2\|V\|\|\dot V\|\), and direct
differentiation of \(q^{-1}\), \(T_V\) and \(P_V\) gives

\[
\|\dot T_V\|+\|\dot P_V\|\le C(g^{-1}+g^{-2})\|\dot V\|.
\]

All constants in these bounds are independent of dimensions. The Gram
formula and the bounded feature/response norms give
\(\|K_C/m\|\le C\), hence \(\|\dot c_C\|_m\le C\rho_C\).
Differentiating the displayed effective-readout formula now yields

\[
\|\dot{\widehat w}_C\|_{H_L}
\le\|\dot w_C\|_{H_L}
+\|\dot P_V\|\|w_C\|_{H_L}
+\|\dot T_V\|\|b\|_2
+\|T_V\|\|\dot c_C\|_m
\le C_{\rm data}\rho_C.
\tag{25}
\]

Here \(C_{\rm data}\) has only fixed-data and Gram-gap dependence, since
\(\|w_C\|\le CY/\sqrt\lambda\) and \(\|b\|_2\le2Y\).
For any sphere query, \(\|h_C^{(L)}(x)\|\le C\) and its derivative
is bounded by \(C(Y/\sqrt\lambda)\rho_C\). Therefore

\[
\sup_x|\partial_t f_C(t,x)|\le C_{\rm data}\rho_C(t),\qquad
\sup_x|f_C(\infty,x)-f_C(t,x)|
\le C_{\rm data}(Y/\lambda)e^{-c\lambda t}.
\tag{26}
\]

This proves both uniform convergence and the needed tail with no source
assumption after \(T\). The original model has its supplied analogous
tail. Choose the structural constant in \(T=C\lambda^{-1}\ell_n\)
large enough to make these tails \(C_{\rm data}n^{-1}\). For \(t\ge T\),
compare both outputs to their values at \(T\) and add their tails to
(23). Thus

\[
\sup_{t\in[0,\infty]}\sup_{x\in\sqrt d S^{d-1}}
|f_C(t,x)-f_n(t,x)|\le C_{\rm data}/\sqrt n.
\tag{27}
\]

Time is the same physical time throughout. Both systems keep evolving;
no stopping, time reparameterization or reference endpoint is supplied to
the compressed system.

## 8. Total retained count and limitations

The moving state requires

\[
dN_1+\sum_{\ell=2}^L N_\ell N_{\ell-1}+N_L+m
\]

real coordinates. Fixed metrics, their optional inverses/factorizations,
and optional small initial-state copies need
\(O(\sum_\ell N_\ell^2+dN_1)\). Data and labels need \(m(d+1)\).
No full-width basis, source vector or initialized full-width matrix need
remain after computing these arrays.

The exact initial Gram is positive definite of rank \(m\). Since it
factors through \(F_C(0)\in\mathbb R^{N_L\times m}\), necessarily
\(m\le N_L\le9R\). Thus all \(m\times m\) Gram/solve arrays and
all \(N_\ell\times m\) training feature/backward caches fit in
\(O(R^2)\) total storage at fixed depth. The construction cannot hide
an uncontrolled training cache in its state count.

It follows that

\[
\operatorname{size}\le C(R^2+dR)+Cm(d+1).
\tag{28}
\]

Substituting the supplied (A), with fixed structural \(d,L\), gives

\[
\operatorname{size}\le
C\lambda^{-2}(\ell_n^{2a}+m^2\ell_n^{2b})+Cm(d+1).
\tag{29}
\]

If \(\lambda=\gamma/m\), this is

\[
C\gamma^{-2}(m^2\ell_n^{2a}+m^4\ell_n^{2b})+Cm(d+1).
\]

The remaining \(m^4\)-term is real. This proves quadratic storage in
the source-space bound \(R\); it does not prove a pure quadratic sample
prefactor. Runtime arithmetic, preprocessing work and finite precision
are not bounded by this exact-real existence theorem. The inverse-Gram
solve is computationally substantive, but its retained arrays have been
counted.

## Clarifications and final disposition

1. In the candidate's Section 2, replace the potentially ambiguous exact
   action statement by: “If \(s\in S_{\ell-1}\) and
   \(W_0^{(\ell)}s\in S_\ell\) are an exact paired approximant, then
   \(B_0^{(\ell)}s_I=(W_0^{(\ell)}s)_I\); actual sources incur the
   \(C\epsilon\) defect proved in the comparison.” An approximately
   represented actual source is not mapped exactly.
2. The older explicit sufficient regime \(Y\le c\lambda/\sqrt m\)
   can be replaced by (10), if the assigned maximum-refinement source
   conclusion is the active input. The new runtime proof uses only
   \(Y\le c\lambda\), so there is no new label loss. Neither this
   report nor the runtime construction independently reproves the
   source theorem under that regime.
3. Section 6's appeal to local smoothness needs its constants understood
   in the weighted parameter and normalized sample norms. Equations
   (25)--(26) supply the missing explicit verification. An arbitrary
   Euclidean-coordinate local-Lipschitz estimate would not suffice to
   justify independence from minimum selected weights.

These are precise qualifications or proof expansions, not counterexamples
to the conditional theorem. The required non-gradient optimizer extension
is explicit, its residuals are its own predictions' residuals, and its
hidden parameters are included in the autonomous update. A claim that
every hidden layer must have nonzero motion for every admissible label
would require a separate nondegeneracy statement; merely being trained
means here that all hidden updates are present. No such stronger motion
claim is needed for the checked storage-and-accuracy theorem.

With the source hypotheses stated explicitly and the qualifications above,
the quadratic total-storage runtime implication is internally verified.
