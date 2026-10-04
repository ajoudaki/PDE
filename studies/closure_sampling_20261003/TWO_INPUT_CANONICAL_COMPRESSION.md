# Canonical two-input compression: source-to-autonomous-model construction

2026-10-03. Internally checked research theorem for the orthogonal training inputs
√2e_1 and √2e_2, arbitrary sufficiently small fixed labels, and all
circle queries. The real stability and finite initial-derivative construction
are proved in `TWO_INPUT_STABLE_GEOMETRY.md`. The physical-time complex
source theorem stated in Section 2 is proved in `TWO_INPUT_COMPLEX_SOURCE.md`.
The source argument and complete compression chain were reconstructed in
`TWO_INPUT_COMPLEX_SOURCE_CHECK.md` and
`TWO_INPUT_CANONICAL_COMPRESSION_CHECK.md`. These are internal collaborative
checks, not independent promotion reviews or established manuscript claims.
The theorem below has no unverified complex-regularity assumption.
No experiment, trained-path setup oracle, other study, or Git operation is used.

## 1. Model and theorem

The reference has first weights A∈R^{n×2}, hidden mixer W∈R^{n×n},
and readout w∈R^n. For any x∈R² define

\[
 h(x)=\tanh(Ax/\sqrt2),\quad z(x)=Wh(x),\quad
 g(x)=\tanh z(x),\quad f_n(t,x)=w^\top g(x)/n.
 \tag{1}
\]

Train on x_a=√2e_a, a=1,2, with loss
\(\mathcal L=\tfrac12\sum_a(f_n(x_a)-y_a)^2\) and block
mobilities (n,1,n). Initially A has iid N(0,1) entries, W has iid
N(0,1/n) entries, the arrays are independent, and w=0. Write

\[
 h_a=h(x_a),\quad z_a=z(x_a),\quad g_a=g(x_a),\quad
 c_{n,a}=y_a-f_n(x_a),\quad
 \delta_a=w\odot\operatorname{sech}^2z_a.
\]

The normalization 2/m is exactly one. Thus

\[
 \dot A=\sum_{a=1}^2c_{n,a}
  [\operatorname{sech}^2(Ae_a)\odot W^\top\delta_a]e_a^\top,
\]
\[
 \dot W=\frac1n\sum_{a=1}^2c_{n,a}\delta_ah_a^\top,
 \qquad \dot w=\sum_{a=1}^2c_{n,a}g_a.\tag{2}
\]

There are fixed Y_*,C>0 such that,
for every fixed label vector y with |y|≤Y_*, every fixed confidence
0<η<1/2, and sufficiently large n, an initialization-only construction
produces an autonomous weighted network satisfying, with probability
at least 1−η,

\[
 \sup_{t\in[0,\infty]}\sup_{\theta\in\mathbb R}
 |f_C(t,x_\theta)-f_n(t,x_\theta)|\le Cn^{-1/2},
 \qquad x_\theta=\sqrt2(\cos\theta,\sin\theta),\tag{3}
\]

and using at most

\[
 C[\log(en/\eta)]^{16}=o(n)\tag{4}
\]

moving **and** fixed stored real coordinates after setup. Both models fit
their training labels and converge to the endpoints included in (3).
There is no restriction on the signs or ratio of the labels. The zero
label vector gives the stationary zero-readout solution.

This is a theorem for the displayed orthogonal pair and its common
rotations. It does not claim the nonorthogonal-pair extension. Setup uses
exact real arithmetic and may require enormous intermediate work and
precision. Neither setup efficiency nor a finite-precision complexity
bound is asserted.

## 2. The proved source theorem and the real fitting event

Put ℓ=log(en/η). Choose a fixed large C_T and T=C_Tℓ. The source input
is a common initialization event of probability at least 1−η on which
the actual physical-time solution has the following properties.

For fixed c,C>0, let r=r_θ=c/√ℓ. The functions

\[
 h(t,x_\theta),\quad g(t,x_\theta),\quad W_0h(t,x_\theta),
 \quad \delta_a(t),\quad W_0^\top\delta_a(t),\quad a=1,2,
 \tag{5}
\]

extend holomorphically to a neighborhood of

\[
 -r\le\Re t\le T+r,\quad |\Im t|\le r,
 \qquad |\Im\theta|\le r_\theta,\tag{6}
\]

are periodic in real θ when applicable, and have coordinate magnitudes
at most C√ℓ there. The last two sources are training sources, so they
have no θ argument. Their claims concern the actual network (2), with
its own physical residual coefficients, rather than a fixed residual
direction or a population replacement. This source theorem was proved
separately in `TWO_INPUT_COMPLEX_SOURCE.md` and reconstructed in both
check reports named above; it is not inferred from the cubature below.

The same event can include fixed constants K,γ>0 with

\[
 \|W_0\|_{\rm op}\le K,\qquad
 G_0:=\left(g_a(0)^\top g_b(0)/n\right)_{a,b=1}^2
 \succeq\gamma I.\tag{7}
\]

For the canonical orthogonal inputs these initialization properties hold
with probability tending to one. In detail, the two first-layer columns
are independent centered Gaussian vectors. Their bounded odd activations
have empirical covariance tending to qI for q=E tanh²(N(0,1))>0.
Conditional on them, the rows of (z_1(0),z_2(0)) are iid centered
Gaussian pairs with that empirical covariance. Bounded-variable
concentration and continuity of the Gaussian expectation show
G_0→νI, where ν=E tanh²(√q Z)>0. A fixed sphere net and Gaussian
tails give the fixed operator bound. No population training theorem is
used here.

Section 3 of `TWO_INPUT_STABLE_GEOMETRY.md` proves that (7), zero
readout, and sufficiently small |y| imply

\[
 |c_n(t)|\le |y|e^{-\kappa t},\qquad
 \int_0^\infty|c_n(t)|dt\le C|y|,\tag{8}
\]

for a fixed κ>0, with hidden displacement O(|y|²), readout maximum
O(|y|), bounded hidden operator norm, and query prediction tails
C|y|e^{-κt}, uniformly on the real circle. The proof applies equally
to positive weighted networks with (7), using weighted norms. Its
constants do not depend on neuron count or the smallest positive mass.

## 3. Small source spaces computed solely from initialization

Set ε=c_0n^{-1/2}, with a fixed positive c_0. Apply the finite
initial-derivative construction in Section 4 of
`TWO_INPUT_STABLE_GEOMETRY.md` to every source (5), with the same
temporal and angular scalar operations. It gives temporal degree

\[
 p\le C\ell^{5/2},\qquad L\le C\ell^{3/2}\tag{9}
\]

for the angular degree, and uniform coordinate error Cε on
[0,T]×R. Training sources need only the temporal degree.

Concretely, every polynomial coefficient is a finite linear combination
of initialized physical-time derivatives at deterministic real query
angles. Those derivatives follow recursively by differentiating (2)
and the forward pass at t=0. A conformal analytic-continuation map
first forms approximate nodal values from those derivatives, and a
discrete cosine transform then retains only p+1 temporal coefficient
vectors. The angular step is a finite discrete Fourier transform.
Approximate nodal values are evaluations of the resulting initial-jet
formula, not evaluations of a trained network. The possibly enormous
initial derivative list is discarded after these coefficient vectors
have been formed. The scalar combination formulas are deterministic
functions of the stated approximation parameters.

Let S_1⊂R^n contain the h(t,x_θ) coefficient vectors and the
W_0^Tδ_a(t) coefficient vectors. Let S_2⊂R^n contain the
g(t,x_θ), W_0h(t,x_θ), and δ_a(t) coefficient vectors.
Because identical scalar operations are used on paired sources,
each h coefficient v is paired with the exact vector W_0v in S_2;
each δ coefficient d is paired with W_0^Td in S_1.

Include additionally h_a(0) and both columns of A_0 in S_1, and
g_a(0), W_0h_a(0) in S_2. These enforce exact initialization,
independently of approximation accuracy. For the optional exact feature
motion certificate in Section 8, also include the finite initial vectors
listed there. The dimensions satisfy

\[
 r_1:=\dim S_1\le C(p+1)(2L+1)+C,
 \quad r_2:=\dim S_2\le C(p+1)(2L+1)+C
 \le C\ell^4.\tag{10}
\]

On real times, every h or g coordinate has magnitude at most one,
while w and δ have magnitude at most C|y|. Since
w(t)=∫_0^t∑_a c_{n,a}(v)g_a(v)dv, integrating a source-space
approximant to g_a proves that w(t) is within coordinate error
C|y|ε of S_2. This last integral is only a proof of membership up
to error; its trajectory-dependent scalar coefficients are never
computed or stored by the compressed algorithm.

## 4. Positive cubature and the initialized projected mixer

Choose basis matrices V∈R^{n×r_1}, U∈R^{n×r_2} with
V^TV/n=I and U^TU/n=I. Positive empirical cubature selects original
index sets I,J and positive diagonal masses D_1,D_2 of total mass
one satisfying

\[
 V_I^\top D_1V_I=I,\qquad U_J^\top D_2U_J=I.\tag{11}
\]

One elementary construction matches the constant and all symmetric
basis products. If the number of positive nodes exceeds one plus the
number of products, move the masses along an affine dependence until
one mass vanishes, preserving the matched quantities. Repetition gives

\[
 N_1:=|I|\le1+r_1(r_1+1)/2,\quad
 N_2:=|J|\le1+r_2(r_2+1)/2.\tag{12}
\]

Define

\[
 C_0=U^\top W_0V/n,\qquad
 B_0=U_JC_0V_I^\top D_1,\qquad
 B_0^*=D_1^{-1}B_0^\top D_2.\tag{13}
\]

The selected basis maps are weighted isometries. Hence
\(\|B_0\|_{D_1\to D_2}\le\|W_0\|_{\rm op}\).
If v∈S_1 and W_0v∈S_2, then
\(B_0v_I=(W_0v)_J\). If d∈S_2 and W_0^Td∈S_1, then
\(B_0^*d_J=(W_0^Td)_I\). These statements follow directly by
expanding v and d in V,U and using (11). They preserve both directions
of the same initialized interaction.

The initially retained forward pass therefore has exact training
preactivations z_{a,J}(0) and features g_{a,J}(0). Moreover (11)
preserves all initial training Gram entries, because g_a(0)∈S_2:

\[
 g_a(0)_J^\top D_2g_b(0)_J=G_{0,ab}.\tag{14}
\]

## 5. The complete autonomous compressed network

The moving state is A_C∈R^{N_1×2}, B_C∈R^{N_2×N_1}, and
w_C∈R^{N_2}. Fixed stored data consist of the positive masses,
the two labels, and fixed structural constants. Initialize

\[
 A_C(0)=(A_0)_I,\quad B_C(0)=B_0,\quad w_C(0)=0.
\]

For any query x define

\[
 h_C(x)=\tanh(A_Cx/\sqrt2),\quad
 z_C(x)=B_Ch_C(x),\quad g_C(x)=\tanh z_C(x),\quad
 f_C(x)=w_C^\top D_2g_C(x).
\]

At the training inputs set

\[
 c_{C,a}=y_a-f_C(x_a),\quad
 \delta_{C,a}=w_C\odot\operatorname{sech}^2z_C(x_a),
 \quad B_C^*=D_1^{-1}B_C^\top D_2.
\]

Evolve in physical time by

\[
 \dot A_C=\sum_{a=1}^2c_{C,a}
 [\operatorname{sech}^2(A_Ce_a)\odot B_C^*\delta_{C,a}]e_a^\top,
\]
\[
 \dot B_C=\sum_{a=1}^2c_{C,a}\delta_{C,a}h_C(x_a)^\top D_1,
 \qquad \dot w_C=\sum_{a=1}^2c_{C,a}g_C(x_a).\tag{15}
\]

This is the entire runtime algorithm. It uses its own residuals and
evolving hidden matrix and exact weighted adjoint. No full-width vector,
source coefficient array, original matrix, external residual, trained
snapshot, or time forcing is retained or consulted after setup. The
current state determines its future, so it is restartable.

Equations (13)–(14) verify the initialized operator and Gram hypotheses
of the weighted fitting theorem. Thus the model exists and fits for all
physical time, with its own exponential residual bound and fitted limit.

The moving coordinate count is 2N_1+N_1N_2+N_2. Fixed masses and
the optional stored initial state have no larger order. Equations
(10)–(12) give the total bound Cℓ^{16}. Neither full basis matrix nor
initial derivative list survives setup.

## 6. Exact source defects for the selected reference path

All objects in this section are proof devices. The algorithm (15)
does not evaluate them. For 0≤t≤T define

\[
 B_R(t)=B_0+\int_0^t\sum_{a=1}^2c_{n,a}(v)
             \delta_a(v)_J h_a(v)_I^\top D_1\,dv.\tag{16}
\]

Set u_a=Ψ(Ae_a), with Ψ(a)=a/2+sinh(2a)/4, and use the
retained reference state
\(x_R(t)=(u_1(t)_I,u_2(t)_I,B_R(t),w(t)_J)\).
The actual dense hidden matrix satisfies the identical integral formula
with the original empirical pairing normalized by 1/n.

First note the general cubature pairing estimate. If two real source
vectors are approximated in coordinate supremum by elements of S_i
with error at most Cε, their empirical and selected weighted pairings
differ by at most Cε. Insert the two approximants: their pairing is
exact by (11), and each remaining term is bounded by Cauchy--Schwarz.
The selected norm of an approximant equals its empirical norm, which
is bounded by the real source norm plus its coordinate remainder.
This introduces no inverse minimum mass. The same proof applies to
the approximant of w obtained after (10).

Applying this estimate and the paired identities (13) gives

\[
 \sup_{t\le T,\theta}
 \|B_R(t)h(t,x_\theta)_I-z(t,x_\theta)_J\|_{D_2}
 \le C\epsilon,\tag{17}
\]
\[
 \sup_{t\le T,a}
 \|B_R(t)^*\delta_a(t)_J-(W(t)^\top\delta_a(t))_I\|_{D_1}
 \le C\epsilon,\tag{18}
\]
\[
 \sup_{t\le T,\theta}
 |w(t)_J^\top D_2g(t,x_\theta)_J-f_n(t,x_\theta)|
 \le C\epsilon.\tag{19}
\]

For (17), the fixed-mixer defect is bounded by the common paired
approximants for h and W_0h. The learned defect is the sum over a
of δ_a(v)_J times the discrepancy between the two pairings of
h_a(v) with h(t,x_θ), integrated against c_{n,a}(v). The residual
length (8) bounds the integral. For (18), the fixed defect uses the
δ_a,W_0^Tδ_a pair, and the learned part pairs δ_b(v) with δ_a(t),
multiplied by h_b(v)_I and integrated against c_{n,b}(v). Formula
(19) is the pairing estimate for w and g(t,x_θ). These calculations
explicitly control both interaction directions and the accumulated
learned matrix.

Bounded real source coordinates in (16) imply
\(\|B_R\|_{\rm op}\le K+C|y|^2\). Also (18) gives

\[
 \|(W^\top\delta_a)_I\|_{D_1}
 \le\|B_R^*\delta_{a,J}\|_{D_1}+C\epsilon
 \le C|y|+C\epsilon.
\]

Integrating the exact equation \(\dot u_a=c_{n,a}W^\top\delta_a\)
therefore bounds the retained u displacement by
C|y|²+C|y|ε. Thus x_R lies in the small real tube needed for
the stability lemma. No sampled carrier maximum is assumed.

Let V_a and F denote the residual-free vector fields and training
observation of the weighted model in the regular coordinates u_a.
Although the retained full features use z_{a,J}, while V_a(x_R)
uses B_Rh_{a,I}, (17) and bounded real gate derivatives give

\[
 \dot x_R=\sum_a c_{n,a}V_a(x_R)+e(t),\qquad
 \|e(t)\|\le C\epsilon |c_n(t)|,\tag{20}
\]
\[
 c_n=y-F(x_R)+d(t),\qquad |d(t)|\le C\epsilon.\tag{21}
\]

Here the norm is the sum of the two D_1 norms, the weighted hidden
Hilbert--Schmidt norm, and the D_2 readout norm. The u-block error
uses (18); the w-block error uses (17); and the B-block error in
(16) is the gate discrepancy in δ. The latter is at most
C|y|ε because w_J is uniformly bounded. Thus
\(\int_0^T\|e(t)\|dt\le C|y|\epsilon\).
Equation (21) follows by adding the gate discrepancy to (19).

## 7. Comparison at the same physical time and through the endpoint

The autonomous compressed state x_C satisfies
\(\dot x_C=\sum_a c_{C,a}V_a(x_C)\) and
c_C=y−F(x_C), with x_C(0)=x_R(0). Both actual residual paths
c_C and c_n have total length at most C|y|. The initialized linear
observation L_0 selects the readout pairing with g_{a,J}(0), and
L_0V_0=G_0 is symmetric with gap γ by (14).

The real structural estimates in `TWO_INPUT_STABLE_GEOMETRY.md`
give bounded DV, V−V_0=O(|y|), and
\(F(x)=L_0(x-x_0)+N(x)\) with Lip(N)=O(|y|) on the tube
containing both paths. The extra retained hidden displacement
C|y|ε above is harmless when ε≤1: the readout has size O(|y|),
and its feature displacement from initialization is still O(|y|).
Equations (20)–(21) therefore verify the perturbation hypotheses of
that lemma on [0,T]. Its constants do not depend on T, so it gives

\[
 \sup_{0\le t\le T}\|x_C(t)-x_R(t)\|\le C\epsilon.
 \tag{22}
\]

This comparison does not identify endpoint activities with a state and
does not assume their vector fields commute. The stable variable in
the proof is only the difference ∫_0^t(c_C−c_n)dv; integration
by parts and the initial Gram gap control it at shared physical times.

For a real query angle, Ψ^{-1} is 1-Lipschitz and both first-layer
columns are retained. The query map is uniformly Lipschitz on the
bounded real tube. Combining (17), (19), and (22) proves

\[
 \sup_{0\le t\le T,\theta\in\mathbb R}
 |f_C(t,x_\theta)-f_n(t,x_\theta)|\le C\epsilon.\tag{23}
\]

Each model independently has a real-circle query tail bounded by
C|y|e^{-κt}. Choose C_T in Section 2 so C|y|e^{-κT}≤ε.
For t≥T, compare each prediction with its own value at T and use
(23). This adds at most Cε and proves (3), including t=∞.
Neither algorithm is frozen at T; both continue with their own
autonomous gradient equations and fit exactly in the limit.

## 8. Exact nonzero motion in both hidden feature layers

This section certifies nonzero feature learning at finite width. It does
not assert a width-independent lower bound on displacement at a fixed
positive time.

Assume y≠0, the Gram condition (7), and W_0 invertible. The latter
holds almost surely for the square Gaussian mixer. Write

\[
 a_a=A_0e_a,\quad d_a^{(1)}=\operatorname{sech}^2a_a,
 \quad d_a^{(2)}=\operatorname{sech}^2z_a(0),
 \quad v=\sum_a y_ag_a(0).
\]

The Gram gap implies v≠0. Zero initial readout gives
\(\dot A(0)=\dot W(0)=0\), \(\dot w(0)=v\), and direct
differentiation of (2) gives

\[
 \ddot A(0)e_a=y_a d_a^{(1)}\odot
                 W_0^\top(v\odot d_a^{(2)}),
\]
\[
 \ddot h_a(0)=y_a(d_a^{(1)})^{\odot2}\odot
                 W_0^\top(v\odot d_a^{(2)}),\qquad
 \ddot W(0)=\frac1n\sum_a y_a(v\odot d_a^{(2)})h_a(0)^\top.
 \tag{24}
\]

For every a with y_a≠0, the first two vectors are nonzero: all real
gates are strictly positive, v is nonzero, and W_0^T is invertible.
Thus the first hidden feature layer moves for every nonzero label vector.

To see second-layer feature motion directly, differentiate its forward
pass twice and pair with the fixed initial readout velocity v. The
initial feature velocities vanish, so the chain rule yields exactly

\[
 \sum_a y_a\frac{v^\top\ddot g_a(0)}n
 =\frac{\|\ddot A(0)\|_F^2}{n}+\|\ddot W(0)\|_F^2>0.
 \tag{25}
\]

For example, the mixer contribution is
\(\langle\ddot W(0),n^{-1}\sum_a y_a(v\odot d_a^{(2)})
h_a(0)^\top\rangle_F=\|\ddot W(0)\|_F^2\).
The first-layer contribution is the sum of the squared column norms
from (24), divided by n. Hence at least one \(\ddot g_a(0)\) is
nonzero. This derives second-layer feature motion from its own
derivative, rather than inferring it from mixer motion.

The construction can preserve this certificate in the smaller model
by adding only finitely many initialized vectors to the cubature spaces:
put \(d_a^v:=v\odot d_a^{(2)}\) in S_2 and
\(W_0^Td_a^v,\ddot h_a(0)\) in S_1. Then (13) matches the
initial reverse actions, so \(\ddot h_{C,a}(0)=\ddot h_a(0)_I\).
Because (11) preserves the norm of \(\ddot h_a(0)\), every
nonzero such curvature remains nonzero in the reduced network. The
weighted version of (25) then proves that at least one of its second
hidden training features moves as well. All extra vectors are computed
from initialization and labels, and they do not change (10) or (4).

## 9. Claim boundary

The proved actual-network source theorem (5)–(6), combined with
Sections 3–8, supplies the finite initialization-only construction,
total stored-state count, exact initial Gram preservation, both
interaction defects, autonomous own-residual dynamics, shared-physical-time
stability, endpoint transfer, and exact nonzero feature motion. The
complete mathematical chain has passed the two internal reconstructions
named above. It remains research in this study, with orthogonal two-input
geometry, fixed sufficiently small labels, sufficiently large width,
and unrestricted exact-real setup. Neither a nonorthogonal extension,
efficient finite-precision preprocessing, nor promotion into the maintained
book is claimed.
