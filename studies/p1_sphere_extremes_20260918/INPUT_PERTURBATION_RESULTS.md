# Input noise: local destabilization and robust remote flat equilibria

2026-09-18. Lead synthesis within the existing seven-input basin study.
Proof/check status and exact reviewed versions are recorded in the README.
These are study results, not promoted book material. No new numerical
experiment is used.

## 1. The two conclusions

The proposed input-noise idea has a positive local theorem and a negative
global theorem.

**Local theorem.** For the original regular seven-input flat equilibrium,
at all but two explicitly excluded positive lower amplitudes, almost every
fixed tangent input-perturbation direction has this property: at all
sufficiently small nonzero amplitudes, every equilibrium in a fixed
neighborhood of the original state is a strict saddle. The neighborhood
uses the full physical Hilbert norm and allows arbitrary population-field
and matrix adjustments. A perturbed equilibrium need not exist there.

**Global counterexample.** Every neighborhood of the original seven-input
data contains a nonempty open set of input configurations admitting a
positive-loss equilibrium with an actual rank-one positive-semidefinite
Hilbert Hessian. Its loss is exactly 48/49. This holds after fully free
small changes of all inputs; no exact data reflection, shared latitude,
or moment equality is required in the final open set.

The global counterexample also holds for an open set of fixed tangent
perturbation directions, at every sufficiently small positive amplitude
with a direction-dependent threshold. Along the seed path and shrinking
open neighborhoods of it, the states can be chosen uniformly bounded,
with one fixed matrix and readout, converging to a different equilibrium
of the original data. Its lower support uses two special preactivation
levels. Thus the conclusions are compatible. Input noise removes one
local obstruction, but cannot establish the global premise that every
positive-loss equilibrium has a negative Hessian direction.

Each constructed PSD state at positive noise amplitude has a verified
bounded cubic descent direction, so it is not a local minimum. Neither theorem constructs a
nonparallel bad basin of positive probability or canonical initialized
failure. These same freely perturbed data also admit exact zero-loss fits.

## 2. Exact model and reference data

Keep the canonical p=1, d=3 correlated dictionary marks and odd sector from
docs/observable_p1.md, including the reverse response, ridge 1/4096,
actual transpose, all three trained blocks, and physical L2/L2/Frobenius
gradient metric. Physical inputs are x_i=sqrt(3)u_i, |u_i|=1. Write
phi=tanh and

\[
a_i=E_1[b_1\phi(w\cdot u_i)],\quad v_i=Ma_i,\quad
H_i=\phi(b_2\cdot v_i),\quad f_i=E_2[cH_i],
\quad L=\frac17\sum_i(f_i-y_i)^2.
\]

The state coordinate is theta=(w-g,c,M) in the complete odd physical
Hilbert space. The reference data have

\[
u(\alpha)=(C,S\cos\alpha,S\sin\alpha),\quad
C,S>0,\quad C^2+S^2=1,
\]

with positive labels at 0,2pi/3,4pi/3, negative labels at
pi/4,3pi/4,5pi/4,7pi/4, and equal masses. All points are distinct and
none are antipodal. These properties persist on sufficiently small data
neighborhoods.

At common prediction m=-1/7 the residual coefficients are fixed:

\[
\rho_i=(m-y_i)/7=
\begin{cases}-8/49,&y_i=+1,\\6/49,&y_i=-1.\end{cases}
\qquad L=48/49.
\]

The regular reference state uses q!=0, epsilon_1=sign(q dot b_1),
kappa=E|q dot b_1|>0,

\[
w_*=a_*\epsilon_1e_1,\qquad M_*=e_1q^T,\qquad
v_*=\kappa\phi(a_*C)e_1,
\]

and a bounded odd readout c_*=c_*(b_{2,1}) satisfying
E[c_* phi(b_2 dot v_*)]=m and
E[c_* b_{2,1} phi'(b_2 dot v_*)]=0.
The known Gram projection constructs it exactly. It has zero backward
vectors and a rank-one PSD Hessian. The previously constructed readout
with cubic descent also qualifies for the local theorem.

## 3. The geometric condition exposed by perturbation

For any changed inputs define the known finite-dimensional residual function

\[
Q(s)=\sum_i\rho_i\phi(s\cdot u_i).
\]

Readout stationarity near the reference state forces all seven effective
vectors to coincide and every prediction to equal m. Indeed distinct tanh
ridge features modulo sign are independent under the actual upper mark
law. Each common-feature group at an equilibrium predicts its label mean.
No proper subset of the three positives and four negatives has mean -1/7:
the required equation 4r=3l forces the entire set.

At a common-nonzero-feature equilibrium with prediction m and M!=0,
PSD second variation requires

\[
\nabla Q(w)=0\quad P_1\text{-almost surely}.
\tag{1}
\]

This is a condition on the support of the full first-layer population.
To see it, vary the lower field by h and write
W=E_1[(Mb_1)(grad Q(w) dot h)]. The upper derivative function
(b_2 dot W)phi'(b_2 dot v) has a nonzero component k orthogonal to the
common feature H unless W=0. The readout direction k has zero pure
quadratic loss curvature, but the mixed lower/readout term is
4t||k||_2^2 along (h,t k,0). PSD therefore forces W=0 for every h.
Choosing h=(Mb_1)_j grad Q(w) in a nonzero row gives (1), because
nonzero b_1 hyperplanes have zero canonical population mass.

Conversely, the following explicit criterion constructs PSD bad equilibria:

> If Q has seven critical points s_j whose evaluation matrix
> V_ij=phi(s_j dot u_i) is invertible, there is an exact equilibrium at
> loss 48/49 with an actual rank-one PSD physical Hessian.

The complete realization is in input_perturb_persist.md, Section 2.
An even partition of |G_2| assigns signed weights alpha_j proportional
to V^{-1}1, and the lower field is sign(G_1) times the assigned signed
critical point. Canonical coordinate-pair independence gives identical
lower moments a_i=lambda A, while grad Q(w)=0 everywhere. No correlation
between the lower dictionary and g is discarded.

A finite upper Gram projection then chooses c with common prediction m
and all first and second upper derivatives zero. This retains every
matrix direction, including transverse components. For arbitrary
(h,k,N),

\[
D^2L[(h,k,N),(h,k,N)]=2(E_2[kH])^2.
\tag{2}
\]

Individual lower critical coefficients vanish, so (2) is an actual
Hilbert Frechet Hessian, not merely a directional calculation.

The same invertible V directly verifies attainability of zero loss: target
the lower interpolation at (1,2,...,7) instead of the constant vector.
The resulting upper features have seven distinct positive scalar tanh
slopes. They are independent, so their exact Gram inverse gives a bounded
readout fitting every label. The positive critical loss is above the
attained architectural minimum.

## 4. Why the old state is locally destroyed

Let xi_i be tangent to the original sphere inputs, and set

\[
u_i(\eta)=\frac{u_i+\eta\xi_i}{\sqrt{1+\eta^2|\xi_i|^2}},
\qquad \Delta=\sum_i\rho_i\xi_{i,1}.
\]

Assume Delta!=0 and

\[
\phi'''(a_*C)\ne0,\qquad
1-2a_*C\tanh(a_*C)\ne0.
\tag{3}
\]

The choice a_*C=1/4 works. With s=a e_1+z, z perpendicular to e_1,
the unperturbed residual function has leading transverse term

\[
Q_0(ae_1+z)
=-\frac{S^3}{49}\phi'''(aC)
 (z_2^3-3z_2z_3^2)+O(|z|^4).
\]

The transverse gradient of this cubic has norm proportional to |z|^2.
A critical point of Q_eta close to the axis would therefore have
|z|=O(sqrt(|eta|)). Its remaining axial equation becomes

\[
0=\eta\phi'(aC)[1-2aC\tanh(aC)]\Delta
  +O(|\eta|^{3/2}),
\]

uniformly near a_*. This is impossible by (3). There are consequently
fixed balls around both old lower-field values with no residual critical
point for sufficiently small nonzero eta.

Full L2 closeness to w_* forces positive population mass in those balls.
Thus (1) is impossible even for arbitrary lower-field changes. At any
remaining nearby equilibrium, lower stationarity additionally implies
M^T d=0, since grad Q_eta(w) is nonzero on positive mass and the lower
marks have no hyperplane atoms. This supplies the actual Hilbert Hessian;
the mixed variation supplies its negative eigenvalue.

The complete theorem and proof are in input_perturb_frozen.md, Section 10.
The linear functional Delta is nonzero on the fourteen-dimensional product
tangent space. Consequently it is nonzero almost surely under any
absolutely continuous tangent noise law. The exact quantifier is
almost every fixed direction, followed by a sufficiently small radius
depending on that direction. The proof does not give an almost-sure
claim at every fixed noise amplitude.

## 5. Why the global statement nevertheless fails

The robust counterexample uses exactly the two preactivation levels at
which the preceding argument cannot work:

\[
t_*=\operatorname{arctanh}(1/\sqrt3),\qquad
2t_0\tanh(t_0)=1.
\]

They satisfy phi'''(t_*)=0 and
(d/dt)[t phi'(t)] at t_0 equals zero.

A specific smooth perturbation raises the first coordinate of the positive
angle-zero input and rotates one reflected negative pair. The rotation
velocity is chosen explicitly; every input remains on the sphere. For
all sufficiently small positive amplitudes epsilon, Q has:

* Five nondegenerate critical points at distance O(epsilon^(1/3)) from
  the axis point with first preactivation t_*.
* Two more at distance O(sqrt(epsilon)) from the axis point with first
  preactivation t_0.

The complete scaled critical equations, roots, nondegeneracy and feature
determinants are derived in input_perturb_persist.md, Sections 3--6.
Reflection splits the seven feature vectors into four even and three
odd components. Both determinant leading coefficients are explicitly
nonzero. Thus the interpolation criterion of Section 3 applies.

Nondegeneracy permits each critical point to continue under all fourteen
free spherical input coordinates. Invertibility of the feature matrix
persists by continuity. This produces a full open set of data, not only
the reflection-preserving seed path. Taking epsilon arbitrarily small
places these open sets arbitrarily close to the original geometry.

A noise distribution with positive density throughout any such small
data neighborhood assigns positive probability to surviving PSD bad
equilibria. Their existence is therefore not confined to a null set of
input configurations.

The complete strengthenings in input_perturb_bounded_continuation.md
also resolve two possible qualifications. First, on the symmetric seed
path the relevant vector V^{-1}1 converges despite the vanishing feature
determinant. A scaled four-dimensional even-coordinate matrix has an
explicit invertible limit. One fixed lower interpolation scale, matrix,
and upper readout therefore works throughout. The lower fields converge
in L2 to a bounded field with positive mass at both magnitudes t_*/C
and t_0/C. Shrinking full open data neighborhoods retain this bounded
continuation. It does not approach any fixed-magnitude two-point state
covered by Section 4.

Second, use the independently perturbed normalized sphere paths from
Section 4 and put tau=epsilon^(1/6). The seven rescaled critical-point
branches and their feature determinant are analytic in tau and the
fourteen input velocities. At the seed velocity the determinant has a
nonzero coefficient at order tau^27. That coefficient remains nonzero
on an open velocity neighborhood. For every fixed direction there,
the determinant is consequently nonzero for all sufficiently small
positive tau. Thus PSD equilibria survive for an open set of fixed free
input directions at every sufficiently small direction-dependent
amplitude. No uniform state bound over this whole direction family is
asserted. This refutes the global almost-every-direction version as well
as the fixed-data-neighborhood version.

## 6. Scope and checking

The frozen-state and restricted-ansatz calculations additionally show
local codimensions seven for preservation of the exact old equilibrium,
four for existence of a nearby two-point-lower-field equilibrium, and
eight for flatness near the projected readout within that ansatz.
These are supporting results in input_perturb_frozen.md, Sections 1--9;
none is substituted for the full-state statements above.

The new states at positive noise amplitude have cubic descent, proved completely in
input_perturb_cubic.md. Choose a lower direction supported on one assigned
critical-point pair, multiply it by a centered even function of the spare
Gaussian coordinate G_3, and pair it with a readout direction orthogonal
to H. Every first lower moment variation vanishes. The first two loss
derivatives vanish, while the third is a nonzero multiple of
r^T D^2Q(s_j)r, with a freely chosen sign. Nondegeneracy of s_j supplies
such an r. This rules out local minimality and attraction of an entire
neighborhood, but does not decide basin measure.

Nonlinear center dynamics and canonical reachability remain uncontrolled.
The finding blocks a universal strict-saddle argument based only on input
genericity. A successful basin theorem could instead exclude these
particular lower-support/readout configurations along reached trajectories,
or control their higher-order dynamics.

The independent frozen routes, post-freeze informed comparison, fresh
review, exact hashes and any repairs are recorded in the README and
linked reports. Neither finite-network simulation nor a closure-order
limit is used in these conclusions.
