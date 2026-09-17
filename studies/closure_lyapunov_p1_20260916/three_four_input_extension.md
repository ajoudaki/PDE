# Three or four unit-labelled inputs: exact extension and remaining problem

2026-09-16. Continuation requested by the user in this task. This is a bounded
analytical assessment with an exact four-input corollary and an initialization
rank lemma. It is not a claim of generic multi-input convergence. The same
study is retained because this extends its current potential and data scope.
No experiment, new agent, shared-path edit or promotion was undertaken.

## Contract and dependencies

Keep the exact canonical p=1 closure, full joint Gaussian initialization,
ridge 1/4096, inverse-Cholesky dictionary normalization, actual M transpose,
physical L2/Frobenius metric, and unhalved probability-weighted square loss.
Physical inputs are x=sqrt(2)u with |u|=1. All labels below are exactly +1
or -1; the readout starts at zero and all trainable blocks evolve.

The current scalar theorem is [all_angles_result.md](all_angles_result.md).
The exact initialization calculation is
[arbitrary_pair_local.md](arbitrary_pair_local.md), Sections 1–4, checked
in [arbitrary_initialization_audit.md](arbitrary_initialization_audit.md).
Actual dictionary symmetries are checked in
[antipodal_upgrade_check.md](antipodal_upgrade_check.md).
These are same-study inputs, not promoted results. Their full arguments were
read during this investigation; the relevant symmetry and scalar proof were
reread for this continuation. Canonical equation/normalization sources remain
docs/global_nonlinear.md C.4.7.9.3–4 and C.4.7.10 B/C.1/D.3.

The initialized map used below is precisely the proved representation

\[
 H_0^2(u)=\tanh\bigl(Z_1\varphi(u_1)+Z_2\varphi(u_2)\bigr),
 \qquad Z_i=\tanh\xi_i.
\]

Here the two upper Gaussian coordinates xi_i are independent, so Z has
positive density on (-1,1)^2. The scalar function varphi, called Phi in the
frozen initialization route, is odd and strictly increasing. It is unrelated
to the Lyapunov potential Phi. The same route proves that the nonzero vectors
(varphi(u_1),varphi(u_2)) and (varphi(v_1),varphi(v_2)) are collinear exactly
when v=u or v=-u. This last statement includes coordinate zeros.

## 1. An exact four-input unit-label theorem

Let a,b>0 and a^2+b^2=1. Give equal mass 1/4 to the four distinct directions
and labels

\[
 (u_1,y_1)=((a,b),+1),\quad (u_2,y_2)=((a,-b),-1),
\]
\[
 (u_3,y_3)=((-a,b),+1),\quad (u_4,y_4)=((-a,-b),-1).
\]

The exact closure is odd in its input at EVERY state, since its first tanh,
linear middle contraction and second tanh are odd:

\[
 H^2(-u)=-H^2(u),\qquad f(-u)=-f(u).
\]

Here u_3=-u_2 and u_4=-u_1, with the compatible opposite labels. Consequently
the four-point loss, as a functional of the entire ambient state, is exactly

\[
 \mathcal L(S)=\frac14\sum_{j=1}^4(f(u_j)-y_j)^2
 =\frac12(f(u_1)-1)^2+\frac12(f(u_2)+1)^2.
\]

Because this is an ambient functional identity and the physical metric is
unchanged, its complete w,c,M gradient is identical to that of the established
reflected two-input problem. This proves equality of full-state trajectories,
not only equality of scalar losses on a chosen curve. Physical time has not
been rescaled: the probability factors above account for all four samples.

Define directly from the four labelled inputs

\[
 U=\frac14\sum_{j=1}^4 y_jH^2(u_j),\qquad
 F=\frac14\sum_{j=1}^4 y_j f(u_j)=E_2[cU].
\]

Oddness gives U=(H^2(u_1)-H^2(u_2))/2 and the same equality for F. The
initialized reflection symmetry gives f(u_j)=y_jF along training. The
existing theorem therefore applies without any new dynamical estimate:

\[
 \Phi(S)=\frac{1+E_2[c^2]}{E_2[U_0^2]+F^2},\qquad \dot\Phi\le0,
\]
\[
 E_2[U_t^2]\ge E_2[U_0^2]>0,\qquad
 \mathcal L(t)\le\exp\{-4E_2[U_0^2]t\}.
\]

The complete state has finite remaining physical length, converges with the
same characteristic and joint-law topologies as the scalar theorem, and fits
all four unit labels. The existing strict-gain proof also gives
E_2[U_infty^2]>E_2[U_0^2].

Geometrically, U is half the difference between the average upper hidden
representation of the two positive samples and that of the two negative
samples. Thus this conclusion protects, and strictly improves at the endpoint,
the squared distance between the two class means. It controls neither every
pairwise hidden distance nor a unique representation.

**Necessary qualification:** these four constraints include two antipodal
duplicates. After the exact oddness and reflection reductions there is still
only one independent prediction error. This is a valid four-input theorem,
but it does not settle the new issue of several independent residual modes.
Its restrictions must be stated whenever it is described as an extension.

## 2. Initialization rank for genuinely three or four directions

Let m be 3 or 4, and let u_1,...,u_m be unit directions with u_i!=u_j and
u_i!=-u_j for i!=j. Then the initialized upper functions H_0^2(u_j) are
linearly independent in L2(Omega_2).

Proof. For this proof only write v_j=(varphi(u_{j,1}),varphi(u_{j,2})). By
the initialization result above they are nonzero and pairwise noncollinear.
Suppose sum_j t_j tanh(v_j dot Z)=0 in L2. Continuity and positive density
extend the identity to the open square (-1,1)^2. Evaluating at Z=s z near
zero, differentiating three times in s, and using tanh'''(0)=-2 gives

\[
                 \sum_j t_j(v_j\cdot z)^3=0
                 \quad\hbox{for every }z\in\mathbb R^2.
\]

Choose an algebraic coordinate basis e,e' with v_j dot e!=0 for every j;
such an e avoids finitely many lines. Put A_j=v_j dot e and
B_j=v_j dot e'. The slopes B_j/A_j are pairwise distinct, because the
v_j are pairwise noncollinear. Set z=x e+y e'. The coefficients of
x^(3-k)y^k, for k=0,...,m-1, in the zero polynomial above give

\[
 \sum_j (t_j A_j^3)(B_j/A_j)^k=0,\qquad k=0,\ldots,m-1.
\]

All binomial coefficients divided out here are nonzero and m-1<=3.
The matrix of these equations is Vandermonde, with determinant
the product of all distinct slope differences. Therefore t_j A_j^3=0
for every j and t_j=0. The coordinate basis change is only a way of reading
a polynomial identity; no rotation of the dictionary or dynamics is used.

It follows that the ordinary initialized Gram

\[
 B_{ij}=E_2[H_0^2(u_i)H_0^2(u_j)]
\]

is positive definite. In particular every unit-label assignment y_j is
representable while retaining the initialized hidden state: choose

\[
 c_{\rm fit}=\sum_j(B^{-1}y)_j H_0^2(u_j),\qquad w=g,\quad M=D.
\]

Direct substitution gives f(u_i)=y_i. The finite linear combination is
bounded, so it is an admissible readout. This is a data-defined existence
certificate, not a change to the prescribed zero-readout training, not an
assertion that training freezes the features, and not a convergence proof.

The probability-weighted initial Gram is B/m and is also positive definite.
The prior local-basin argument extends to this finite m with the same bound
on normalized readout-map perturbations. It consequently gives a small-label
theorem, but this does not establish the requested unit-label conclusion.
No small amplitude is silently substituted for the user's labels.

## 3. Exact obstruction to simply repeating the scalar proof

For any m equally weighted labels y_j in {+1,-1}, set

\[
 U=\frac1m\sum_jy_j H^2(u_j),\qquad
 F=\frac1m\sum_j y_jf(u_j)=E_2[cU].
\]

By the definition of F, sum_j y_j(f(u_j)-y_jF)=0. Expanding squares gives
the exact ambient identity

\[
 \mathcal L=(1-F)^2+
       \frac1m\sum_j(f(u_j)-y_jF)^2.
\]

In the four-point theorem the second term and its gradient vanish along
the symmetric trajectory. For genuine multiple residuals they need not.
The physical velocity is then

\[
 2(1-F)\nabla F
 -\nabla\left[\frac1m\sum_j(f(u_j)-y_jF)^2\right].
\]

The extra gradient contributes cross terms to the derivative of the
normalized-readout potential; the scalar Cauchy-Schwarz proof gives no sign
for those terms. Thus positive initial Gram rank, representability of all
unit labels, and scalar noncollapse are three distinct facts. The first
two are proved here; the scalar theorem alone does not supply the required
all-time multi-residual geometry.

## 4. A concrete three-input target beyond the scalar reduction

For a substantive next theorem, a particularly simple canonical family
member is the equally weighted unit-label dataset

\[
 ((1,0),+1),\qquad ((0,1),+1),\qquad
 ((1,1)/\sqrt2,-1).
\]

All directions are distinct and non-antipodal. The preceding Gram lemma
proves representability from the exact initialized hidden features. The
actual coordinate-swap symmetry preserves the dataset and labels, so
f(1,0)=f(0,1) along training. This symmetry uses the plus-readout version
of the established isometry: c goes to c composed with the upper mark
swap. It fixes zero readout and transforms f(u) to f(Pu). No arbitrary
rotation is assumed.

Its loss is therefore

\[
 \mathcal L=\frac23(f(1,0)-1)^2+
            \frac13(f((1,1)/\sqrt2)+1)^2.
\]

There remain two independent prediction constraints. Their independence
also follows from the positive initial Gram; no symmetry equates the
axis prediction with the negative of the diagonal prediction. This is a
genuine extension target beyond one scalar error. It is especially useful
because a linear predictor positive at both axes cannot be negative at
their positive diagonal, whereas the exact initialized nonlinear features
already represent these labels. This observation concerns representability,
not a proved advantage or a convergence mechanism.

**Status:** global unit-label fitting, a suitable multi-residual potential,
and full-state convergence for this three-point example remain OPEN.
The four-point theorem is proved but symmetry-reduced. It is plausible to
pursue the three-point case next; success is not guaranteed by the existing
argument. This assessment launches no unbounded research campaign.

## Internal analytical checks and preservation

Root checked the complete new argument: ambient oddness of both hidden
layers, all four probability factors, equality of full gradients, exact
four-sample U and F, the two class means, the cubic derivative, Vandermonde
rank including coordinate-zero cases, readout interpolation, the loss
decomposition, and the actual swap symmetry of the three-point example.
The two-label proof and initialization source are unchanged. This is an
author-side internal check, not an independent or promotion review.

Stress checks: a,b>0 excludes repeated rectangle vertices; b down to zero
allows a degenerating opposite-label contrast and no uniform rate is
claimed. Same labels at antipodes would violate input oddness and are not
included. The generic rank lemma excludes precisely the coincidence and
antipodal exceptions needed by its noncollinearity premise. It does not
infer persistent rank from initial rank. No evolution term of a changing
metric is discarded: all metrics remain the original physical metric.

All relevant instruction and canonical-source hashes were rechecked
unchanged from the existing continuation contract. No numerical evidence
is needed. Exact file identities for this addition and its dependencies
are recorded in three_four_input_manifest.sha256; earlier manifests remain
historical and are not overwritten.
