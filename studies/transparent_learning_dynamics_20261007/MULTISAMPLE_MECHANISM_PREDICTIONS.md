# Pre-test mechanisms for correlated multi-sample training

2026-10-07. Analytical predictions declared before the new multi-sample
comparisons. Scope: two-hidden-layer tanh networks with m=4,8,16 training
inputs in d=8, four passive inputs, correlated cluster geometry, and fixed
mixed-sign labels of varied magnitudes. The planned mechanism controls are
at m=8. Inputs: CANDIDATE_SYSTEM.md, UNEQUAL_RESIDUALS_RESULT.md,
PASSIVE_NONLINEARITY_DIAGNOSTICS.md, and the supervisor's assignment.
No experiment, fitted coefficient, two-input cubic reduction, or global
approximation theorem is added here.

The exact initial forecast is a matrix of Gram accelerations computed from
each initial network. Through-learning predictions concern residual-weighted
memory, reciprocal return, redistribution between layers, and passive
activation sensitivity. They are hypotheses to discriminate, not extensions
of the orthogonal two-sample sign rule.

## Setup and exact initial forecast

Let \(\mathcal T=\{1,\ldots,m\}\) and
\(\mathcal P=\{m+1,\ldots,m+4\}\). All fixed inputs
\(v_a\in\mathbb R^8\) have unit norm, and \(S_{ab}=v_a^\top v_b\).
With \(A\in\mathbb R^{n\times8}\), \(W\in\mathbb R^{n\times n}\), and
\(w\in\mathbb R^n\), define

\[
z_{1,a}=Av_a,\quad h_{1,a}=T(z_{1,a}),\quad
z_{2,a}=Wh_{1,a},\quad h_{2,a}=T(z_{2,a}),\quad
f_a=\langle w,h_{2,a}\rangle_n,\qquad
\langle x,z\rangle_n=\frac{x^\top z}{n},
\]

where \(T=\tanh\) and \(g=T'=\operatorname{sech}^2\) act componentwise.
The initial A entries are independent \(N(0,1)\), the independent initial
middle matrix \(G=W(0)\) has entries \(N(0,1/n)\), and \(w(0)=0\).
Only training indices have labels. With \(c_b=y_b-f_b\),
\(\mathcal L=m^{-1}\sum_{b\in\mathcal T}c_b^2\), and block mobilities
\((n,1,n)\), the exact flow is

\[
\begin{aligned}
\delta_{2,a}&=g(z_{2,a})\odot w,&
\delta_{1,a}&=g(z_{1,a})\odot W^\top\delta_{2,a},\\
\dot A&=\frac2m\sum_{b\in\mathcal T}c_b\delta_{1,b}v_b^\top,&
\dot W&=\frac2{mn}\sum_{b\in\mathcal T}c_b\delta_{2,b}h_{1,b}^\top,&
\dot w&=\frac2m\sum_{b\in\mathcal T}c_bh_{2,b}.
\end{aligned}
\tag{1}
\]

Define the two-time empirical Grams
\(C^\ell_{ab}(t,s)=\langle h_{\ell,a}(t),h_{\ell,b}(s)\rangle_n\);
write \(C^\ell(t)=C^\ell(t,t)\). In the population model the inner product
is replaced by its own population expectation.

For one actual initial draw, let
\(X_a=z_{1,a}(0)\), \(Z_a=z_{2,a}(0)\), and
\[
Q=\dot w(0)=\frac2m\sum_{b\in\mathcal T}y_bT(Z_b).
\]
Compute the initial feature accelerations without running training:

\[
\begin{aligned}
J_{1,a}:=\ddot h_{1,a}(0)
&=\frac2m\,g(X_a)\odot
\sum_{j\in\mathcal T}y_j S_{aj}\,
g(X_j)\odot G^\top[g(Z_j)\odot Q],\\
J_{2,a}:=\ddot h_{2,a}(0)
&=g(Z_a)\odot\left[
\frac2m\sum_{j\in\mathcal T}y_j C^1_{aj}(0)
\,g(Z_j)\odot Q+GJ_{1,a}\right].
\end{aligned}
\tag{2}
\]

Every term uses initial data. In particular both factors \(2/m\) are present:
one is inside Q. No inverse of S is used; its rank deficiency at m=16 in
d=8 is permitted.

To derive (2), \(w(0)=0\) makes both hidden parameter velocities and all
hidden feature velocities zero. Thus
\(\dot\delta_{2,j}(0)=g(Z_j)\odot Q\) and
\(\dot\delta_{1,j}(0)=g(X_j)\odot G^\top[g(Z_j)\odot Q]\).
Differentiate (1). Terms multiplying an initial hidden velocity or backward
field vanish, including the terms containing \(\dot c(0)\).
Finally \(\ddot z_{2,a}(0)=\ddot W(0)h_{1,a}(0)+G\ddot h_{1,a}(0)\),
which gives the two terms of \(J_{2,a}\).

For every training-training (TT), training-passive (TP), and passive-passive
pair, the exact finite-width prediction is

\[
\dot C^\ell_{ab}(0)=0,\qquad
\ddot C^\ell_{ab}(0)
=\langle J_{\ell,a},h_{\ell,b}(0)\rangle_n
+\langle h_{\ell,a}(0),J_{\ell,b}\rangle_n.
\tag{3}
\]

Consequently
\(C^\ell(t)-C^\ell(0)=t^2\ddot C^\ell(0)/2+O(t^3)\) for this smooth
finite-width ODE at fixed labels. The remainder is a local-in-time statement,
not a uniform width bound or a late-training formula. For a population
forecast take the corresponding joint initial-law expectation of (2)--(3),
not unrelated pairings of neuron coordinates.

Correlated geometry mixes terms \(y_jy_b\) from all training indices in
(2). Therefore neither the sign of a TT entry nor that of a TP entry is
generally determined by a single product \(y_ay_b\). Passive inputs have no
labels at all. The complete initialized matrix is the quantitative sign and
magnitude forecast.

Two control consequences are sharper than a general qualitative prediction.
Freezing W at its same initialized G leaves \(J_1\) unchanged exactly and
removes only the first term in brackets in \(J_2\). Replacing each activation
on the panel by its anchored affine tangent also preserves (2)--(3):
initial values and gates agree, and the terms containing activation
curvature multiply zero initial hidden velocities. Neither control is
predicted to retain the same later feature trajectory.

## What reciprocal removal changes at this order

The candidate's initial reciprocal-return law gives an additional population
check. Let the lower Gaussian panel X have covariance S, put \(H_a=T(X_a)\),
and let the upper Gaussian panel Z have covariance
\(\mathbb E[H_aH_b]\). Define the scalar upper field
\(Q=(2/m)\sum_{b\in\mathcal T}y_bT(Z_b)\). For a training j, its initial
lower backward derivative is

\[
\dot b_{1,j}(0)=\zeta_j+\sum_{c\in\mathcal T}R_{jc}H_c,\qquad
R_{jc}=
\mathbf1_{j=c}\mathbb E[T''(Z_j)Q]
+\frac2m y_c\mathbb E[g(Z_j)g(Z_c)].
\tag{4}
\]

Here \(\zeta\) is centered Gaussian, independent of X, with covariance
\(\mathbb E[\zeta_j\zeta_k]=
\mathbb E[g(Z_j)Q\,g(Z_k)Q]\). Formula (4) is the initial Gaussian
forward/transpose response rule of the candidate: differentiating
\(g(Z_j)Q\) with respect to its formal upper coordinate \(Z_c\) produces
the displayed R. These derivatives do not require invertible panel
covariance.

Substituting (4) in the first line of (2), interpreted as a population
field, gives

\[
\begin{aligned}
\mathbb E[J_{1,a}H_b]
=\frac2m\sum_{j,c\in\mathcal T}
y_jS_{aj}R_{jc}\,
\mathbb E[g(X_a)g(X_j)H_cH_b].
\end{aligned}
\tag{5}
\]

The Gaussian part disappears because it is centered and independent of X.
If both applied reciprocal corrections are removed as in the existing
candidate control, that part remains but the R contribution is absent.
Thus its population lower Gram acceleration is zero for every TT and TP
entry. This does not mean individual lower-feature accelerations are zero:
their Gaussian part remains. It also does not imply zero lower Gram motion
at later times. Finite quadrature produces sampling fluctuations around the
population initialized value. This is a statement about the specified
response-off law, not a dense untied-feedback gradient model.

## Four discriminators for the declared campaign

For a matrix block B, use
\(\operatorname{rms}_B(M)=
(\sum_{(a,b)\in B}M_{ab}^2/|B|)^{1/2}\), with
\(B=\mathcal T\times\mathcal T\) or
\(B=\mathcal T\times\mathcal P\).
Keep diagonal and off-diagonal TT summaries available so diagonal changes
cannot conceal cross-sample differences. Always subtract each run's own
initial Gram. All time grids, fitting stages, and numerical comparison
tolerances are to be fixed in the root's campaign contract.

### 1. Initialized direction and its range of persistence

Compare the measured change with \(t^2\ddot C^\ell(0)/2\), separately for
both layers and both TT/TP blocks. Report the absolute error

\[
\operatorname{rms}_B\!\left(
C^\ell(t)-C^\ell(0)-\frac{t^2}{2}\ddot C^\ell(0)\right)
\]

and, when both matrices are nonzero, their Frobenius cosine and the
amplitude ratio
\[
\frac{2\|C^\ell_B(t)-C^\ell_B(0)\|_F}
{t^2\|\ddot C^\ell_B(0)\|_F}.
\]

The cosine and ratio tend to one as \(t\downarrow0\) when the initialized
curvature block is nonzero. Persistence over a resolved early learning
window is a hypothesis; persistence through late training is not asserted.
Vanishing forecast blocks require absolute errors, not division by zero.
The no-R lower-population cancellation and the common full/frozen-W lower
curvature are additional initialization targets.

For Euler data, do not compare its very first step with the continuous
\(t^2/2\) formula: the first hidden Euler update is exactly zero. Use an
exact initialized derivative calculation, sufficiently resolved continuous
integration, or the corresponding discrete update expansion. A finite-mesh
delay is not evidence against (3).

### 2. Residual-weighted memory and reciprocal return through learning

The exact readout identity for every panel input is
\[
f_a(t)=\frac2m\sum_{b\in\mathcal T}\int_0^t
c_b(s)C^2_{ab}(t,s)\,ds.
\tag{6}
\]
Its discrete counterpart replaces the integral by
\(\Delta\sum_{j<k}c_b^jC^2_{ab}(k,j)\). Current residuals weight new
writes, while current query features reinterpret old writes. In particular
\(\|\dot w\|_n\le(2/m)\sum_b|c_b|\), because \(|T|\le1\).
Small residuals suppress new readout writes without erasing earlier ones.
Hidden writes also contain residuals, but their size additionally depends
on the current backward fields.

Split (6) at the fixed physical cutoff \(t/2\), and record the signed
early-write and recent-write contributions for each passive input. Their
sum must reconstruct its output. Record also their RMS across the four
passives and the accumulated residual budget
\((2/m)\int_0^t\sum_b|c_b(s)|\,ds\). These are model-computed diagnostics;
inserting a measured history into another predictive model would be a
different use of the data. A small signed early contribution can reflect
cancellation, so it is not a claim that no earlier writes occurred.

The through-learning hypothesis is that reciprocal removal changes TT/TP
feature curves and passive predictions beyond numerical/ensemble
uncertainty, even if it also reaches a small training residual. For each
layer and block record
\[
\max_{t\ \mathrm{on\ declared\ grid}}
\operatorname{rms}_B\!\left[
(C^\ell_{\rm noR}(t)-C^\ell_{\rm noR}(0))
-(C^\ell_{\rm full}(t)-C^\ell_{\rm full}(0))\right],
\]
together with maximum entrywise difference, passive output differences,
and each control's residual norm. Compare full and no-R separately against
the matched dense reference. Agreement only in training outputs is not
confirmation of representation dynamics. The size and sign of these
differences are empirical targets, not universal bounds.

### 3. Frozen-middle redistribution at comparable fitting progress

Feature motion itself can be obtained from the two-time Grams. For
\(\mathcal A=\mathcal T\) or \(\mathcal P\), define
\[
M_{\ell,\mathcal A}(t)^2
=\frac1{|\mathcal A|}\sum_{a\in\mathcal A}
\left[C^\ell_{aa}(t,t)+C^\ell_{aa}(0,0)
-2C^\ell_{aa}(t,0)\right].
\tag{7}
\]
This equals the mean squared displacement of the features; it is not
merely a change of their pairwise angles.

The specific hypothesis is increased later lower-layer motion when W is
frozen, with a reduced share of learning attributed directly to the middle
block. Record the signed contrasts
\(M_{1,\mathcal A}^{\rm frozenW}-M_{1,\mathcal A}^{\rm full}\) and
\(M_{2,\mathcal A}^{\rm frozenW}-M_{2,\mathcal A}^{\rm full}\), plus the
TT/TP curve contrasts above. An increase of the first is predicted as a
possible compensation mechanism to test, not an exact necessity for each
label pattern. A decrease of every upper entry or of every upper motion
norm is not implied by deleting the direct middle write.

Compare at the declared final time and at the predeclared first times
each system reaches, for example, \(\mathcal L(t)/\mathcal L(0)=0.1\)
and 0.01. A missing crossing is reported as missing; it is not extrapolated.
This separates redistribution from differing fitting speeds without
fitting any response coefficient. At initialization the lower accelerations
must agree by (2), so a later separation is a nonlinear training effect.

When direct attribution is recorded, use the three exact passive-output
rates
\[
\dot f_a=
\langle\dot w,h_{2,a}\rangle_n+
\langle w,g(z_{2,a})\odot\dot W h_{1,a}\rangle_n+
\langle w,g(z_{2,a})\odot W\dot h_{1,a}\rangle_n.
\tag{8}
\]
Their integrals partition one trajectory. They are not the differences
between the full and frozen-W endpoints.

### 4. Passive activation evolution and the anchored-affine control

For any passive a the exact lower-feature velocity is
\[
\dot h_{1,a}=\frac2m\,g(z_{1,a})\odot
\sum_{b\in\mathcal T}c_b S_{ab}
\,g(z_{1,b})\odot W^\top[w\odot g(z_{2,b})].
\tag{9}
\]
The query gate and the training gates are distinct. Replacing the sum by
a single sample or replacing both gates by the squared query gate would
be incorrect for correlated inputs. The upper velocity is
\(g(z_{2,a})\odot(\dot W h_{1,a}+W\dot h_{1,a})\).

Measure gate drift on passives by
\[
\frac14\sum_{a\in\mathcal P}
\|g(z_{\ell,a}(t))-g(z_{\ell,a}(0))\|_n^2,
\]
and define the actual activation remainder
\[
r_{\ell,a}(t)=h_{\ell,a}(t)-h_{\ell,a}(0)
-g(z_{\ell,a}(0))\odot[z_{\ell,a}(t)-z_{\ell,a}(0)].
\tag{10}
\]
Report its RMS in both layers, together with the four signed upper
projections \(\langle w(t),r_{2,a}(t)\rangle_n\).
The latter give an exact part of the current passive prediction:
\[
f_a=\langle w,h_{2,a}(0)\rangle_n
+\langle w,g(z_{2,a}(0))\odot[z_{2,a}-z_{2,a}(0)]\rangle_n
+\langle w,r_{2,a}\rangle_n.
\tag{11}
\]

The hypothesis is that activation evolution materially affects passive
motion and response later in training, visible in these quantities and
in full-versus-anchored-affine TT/TP and passive-output differences.
The affine model must change forward activations and backward derivatives
consistently on the declared panel. It shares the initial curvature (3)
but is a different transductive gradient model. Neither its intervention
difference nor (11)'s final term is the total causal influence of all gates:
lower nonlinear evolution also changes the fields entering the upper layer.
Replacing an upper gate by its drift in (8) partitions an existing source
and must not be added as a fourth independent source.

## Interpretation boundaries

There is no proposed universal feature-sign rule, shared scalar clock,
monotone passive response, or ordering of full and ablated effects across
all label patterns. With the canonical \(2/m\) factor, identical physical
times also need not represent identical fitting progress across m.
The full TT and TP matrices, their initial forecasts, and the four declared
mechanism comparisons are the targets.

At m=4 in d=8 the four passives need not lie in the training span.
The earlier geometric-mixture defect is therefore optional: apply it only
when its input relation is verified. Equations (2), (3), and (6)--(11)
apply to every passive input without such a relation or a passive label.
All accuracy comparisons still require separate dense-width, population
quadrature, and time-step controls; this note supplies no all-time guarantee.
