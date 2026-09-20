# Opposite-label pairs: uniform fitting estimates and the remaining limit gap

2026-09-20. New derivations from the established book. Internally checked by
the lead; not independently reviewed or promoted. This does not establish
the arbitrary-angle exact-network population limit on all finite horizons.

## 1. Exact model, symmetry and scope

Let |x_+|=|x_-|=sqrt(2), x_+ != x_-, and put
k=x_+ dot x_-/2 in [-1,1). Both masses are 1/2 and labels are +1,-1.
The finite model and canonical initialization are exactly those of
global_nonlinear.md C.4: two tanh hidden layers, stored variances
(1,1/n,1/n^2), mobilities (n,1,n), unhalved mean square loss. In particular
finite readouts are not set to zero. On the canonical population carrier,
w(0)=g, c(0)=0 and A(0)=A0, with ||A0||op<=2. Write A=A0+K, with K HS.
The physical increment norm is

\[
 \|(v,B,d)\|_{\rm raw}^2=\|v\|_2^2+\|B\|_{\rm HS}^2+\|d\|_2^2.
\]

Define, for a in {+,-},

\[
 Z_a^1=w\cdot x_a/\sqrt2,\quad H_a^1=\phi(Z_a^1),\quad
 Z_a^2=AH_a^1,\quad H_a^2=\phi(Z_a^2),\quad \phi=\tanh,
\]
\[
 H=(H_+^2-H_-^2)/2,\quad
 b=\langle c,H\rangle_2=(f(x_+)-f(x_-))/2 .
 \tag{1}
\]

The initialized spaces and adjunction are provided by special_data_limits.md
III.F.1--10. The local exact flow exists for every such pair by
global_nonlinear.md C.4.7.10.A, through physical time 1/200.

Let R be the orthogonal reflection swapping x_+ and x_-. Concretely,
R=I-2dd^T/|d|^2 with d=x_+-x_-. Include the R-transformed versions of the
countable initialized words in the common-carrier construction. The
orthogonal invariance of the first Gaussian row and independence of the
initialized middle matrix give joint-law invariance for each finite union.
As in C.4.5.1's coordinate-swap proof, this supplies measure-preserving
involutions U1,U2 on the two generated carriers such that

\[
 U_1g=Rg,\qquad U_2A_0=A_0U_1.
 \tag{2}
\]

They preserve products, scalar functions, expectations, and Lp norms.
One direct construction is to use the law of the countable coordinate
tuple: applying the root reflection twice returns every word, and the
resulting coordinate permutation preserves all cylinder probabilities.
It therefore preserves the generated measure. Linear extension and L2
completion yield (2), including the adjoint identity.

The physical symmetry on state fields is

\[
 (w,K,c)\longmapsto(RU_1w,\ U_2KU_1,\ -U_2c).
 \tag{3}
\]

The initialized state is fixed by (3); predictions transform as
-f(Rx). Direct substitution in the exact gradient equations shows
equivariance, because the two data points exchange and both labels
change sign. Uniqueness of the established local flow implies

\[
 f_t(x_+)=b(t)=-f_t(x_-),\qquad L(t)=(1-b(t))^2.
 \tag{4}
\]

The same statement holds for every unique symmetry-preserving continuation,
and will hold globally for the finite-action approximations in Section 4.
It is not pointwise symmetry of an individual finite iid network.

## 2. The initialized contrast is positive at every noncoincident angle

Let G be standard normal, q=E phi(G)^2, and define

\[
 C(k)=E[\phi(G_+)\phi(G_-)],
 \qquad \operatorname{Cov}(G_+,G_-)=k,\quad E G_\pm^2=1.
\]

At initialization the two upper preactivations have the centered Gaussian
law with variances q and covariance C(k), by the initial forward Gaussian
rule. If (Z_+,Z_-) has this law, put

\[
 \kappa(k)=\frac14 E[\phi(Z_+)-\phi(Z_-)]^2.
 \tag{5}
\]

This is an explicit two-stage Gaussian calculation, using only the inputs.
It equals ||H(0)||2^2. No trained endpoint enters it.

In fact

\[
 \frac{\operatorname{sech}^8(2)}8(1-k)
 \ \le\ \kappa(k)\ \le\ \frac{1-k}{2}.
 \tag{6}
\]

Proof: for a centered Gaussian pair with common variance v and covariance
a in (-v,v), differentiating its density gives partial_a p=partial_xy p.
Twice integrating by parts, with vanishing Gaussian boundary terms, gives

\[
 \frac{d}{da}E[\phi(X)\phi(Y)]=E[\phi'(X)\phi'(Y)].
 \tag{7}
\]

All derivatives of phi used here are bounded. Density differentiation is
dominated on compact subsets of (-v,v); integration to endpoints follows
from bounded convergence and continuous Gaussian representations.
For v<=1, Chebyshev and a union bound imply
P(|X|<=2,|Y|<=2)>=1-v/2>=1/2. Thus the right side of (7) lies between
A:=sech^4(2)/2 and 1. First use v=1 and integrate from k to 1:
A(1-k)<=q-C(k)<=(1-k). Next use v=q and integrate from C(k) to q.
The resulting upper-feature variance difference is between
A(q-C(k)) and q-C(k). Its half is kappa(k), proving (6).
The endpoints k=-1 and k=1 follow by continuity. In particular kappa>0
exactly when k<1 in this family; k=1 is incompatible opposite labels.

The exact asymptotic is also available:

\[
 \lim_{k\uparrow1}\frac{\kappa(k)}{1-k}
 =\frac12 E[\phi'(G)^2]\ E[\phi'(\sqrt qG)^2]>0.
 \tag{8}
\]

Indeed the expectation on the right of (7) tends to E phi'(sqrt(v)G)^2
as covariance tends to v. Applying that limit twice proves (8).

## 3. Conditional exact-flow theorem: no loss or raw-norm obstruction

On any existing symmetric strong solution, introduce feature time
ds/dt=2(1-b), as long as b<1. For hidden increments define

\[
 J(v,B)=\frac12\sum_{a=+,-} y_a\phi'(Z_a^2)
 \left[BH_a^1+A\{\phi'(Z_a^1)(v\cdot x_a/\sqrt2)\}\right].
 \tag{9}
\]

This bounded directional map sends the physical hidden increment space to
L2(Omega2). Its actual adjoint, obtained from the same A*, gives precisely
the hidden gradient of b. The feature equations are therefore

\[
 c_s=H,\qquad (w,K)_s=J^*c.
 \tag{10}
\]

The strong curve chain rule in III.F.9 gives

\[
 H_s=JJ^*c,\qquad
 b_s=\|H\|_2^2+\|J^*c\|_{\rm hidden}^2
     =\|S_s\|_{\rm raw}^2.
 \tag{11}
\]

No derivative of J and no ambient twice-Frechet-differentiable L2
activation map is assumed.

Let g(s)=||c(s)||2. Where g>0,

\[
 g_s=b/g,\qquad
 g_{ss}=
 \frac{\|H\|_2^2-(b/g)^2+\|J^*c\|_{\rm hidden}^2}{g}\ge0.
 \tag{12}
\]

Cauchy--Schwarz proves the sign. Since c(s)=sH(0)+o(s),
g_s(0+)=sqrt(kappa). Hence g_s>=sqrt(kappa), g>=s sqrt(kappa),
and g cannot return to zero. A second Cauchy--Schwarz application yields

\[
 \|H(s)\|_2^2\ge (b/g)^2\ge\kappa,\qquad b_s\ge\kappa.
 \tag{13}
\]

Thus the useful contrast cannot collapse. This derivation has no
orthogonality assumption. Equivalently b^2/||c||2^2 is nondecreasing
from kappa, although the more informative identity is (12).

Consequences, valid throughout the existing branch, are

\[
 0<1-b(t)\le e^{-2\kappa t},\qquad L(t)\le e^{-4\kappa t},
 \qquad s(t)\le b(t)/\kappa<1/\kappa.
 \tag{14}
\]

To justify the strict residual sign without presuming continuation:
for any feature prefix before b=1, (11) and Cauchy--Schwarz give

\[
 \int_{s_1}^{s_2}\|S_s\|_{\rm raw}ds
 \le\sqrt{(s_2-s_1)(b(s_2)-b(s_1))}.
 \tag{15}
\]

In particular total prefix travel is at most 1/sqrt(kappa). Also
||c||infinity<=s<=1/kappa. Consequently

\[
 \|c\|_2,\ \|K\|_{\rm HS},\ \|w-g\|_2\le\kappa^{-1/2},
 \qquad \|A\|_{\rm op}\le2+\kappa^{-1/2}.
 \tag{16}
\]

The three gradient blocks of b have norms at most
||A||op ||c||2, ||c||2, 1 respectively. Thus

\[
 b_s\le D_\kappa^2:=
 1+\kappa^{-1}\{1+(2+\kappa^{-1/2})^2\}.
 \tag{17}
\]

The physical residual equation is r_t=-2b_s r for r=1-b; on any prefix
its bounded coefficient gives
exp(-2D_kappa^2 t)<=r(t)<=exp(-2kappa t).
A finite first time with r=0 would contradict the first inequality,
which validates the clock on every finite existing prefix.

If the branch exists for all physical time, (14)--(15) give an actual
strong fitted endpoint and remaining path length

\[
 \int_t^\infty\|\dot S(v)\|_{\rm raw}dv
 \le\frac{1-b(t)}{\sqrt\kappa}
 \le\kappa^{-1/2}e^{-2\kappa t}.
 \tag{18}
\]

For the first inequality, use b(infinity)=1, b_s>=kappa, and (15).
The scalar prediction differential is uniformly bounded on the convex
raw ball (16), so (18) also gives uniform whole-circle convergence.

If instead the constructed branch stops at a finite T*, it has a strong
raw endpoint by (15), or just the bounded speed in (17).
Continuity of the exact field (C.4.7.2) identifies its limiting velocity.
Its residual is still strictly positive, and (13) shows that its loss
gradient is nonzero. Therefore a finite construction failure would not be
raw-norm explosion, loss stagnation, loss of useful contrast, or absence
of a raw state endpoint. It would still be a failure to construct/identify
and uniquely continue the population equation from that reached endpoint.
Continuous vector fields in an infinite-dimensional space do not supply
the missing existence/uniqueness theorem by themselves.

This is an unconditional estimate on the established local branch, and a
conditional estimate on a hypothetical longer branch. It is not the desired
global existence theorem.

## 4. Global approximations with constants uniform in order

There is a stronger approximation-level result without assuming the exact
global flow. Modify only the approximation dictionary of C.4.7.9, not the
target network or optimizer:

At each order take its bounded initialized list together with its U_l image,
paired in a fixed order. Enlarge the underlying common initialized language
by the fixed reflection R, a permissible real linear root instruction.
Let psi_l,N be this doubled column. There is an orthogonal permutation
P_l,N with U_l psi_l,N=P_l,N psi_l,N. Define exactly as in the book

\[
 G_{\ell,N}=E[\psi_{\ell,N}\psi_{\ell,N}^T],\quad
 b_{\ell,N}=(G_{\ell,N}+2^{-N}I)^{-1/2}\psi_{\ell,N}.
 \tag{19}
\]

All marks are bounded at fixed order and preserve their complete initialized
joint laws. G commutes with P because the measure is invariant, so the
inverse square root commutes as well. The resulting positive filters Q_l,N
commute with U_l. They are contractions and tend strongly to the identity on
the generated observable spaces by the unchanged density/ridge argument in
C.4.7.9.2. The doubled lists still contain the original dense lists.

Put

\[
 D_N[i,j]=\langle b_{2,N,i},A_0b_{1,N,j}\rangle,\qquad
 B_N=Q_{2,N}A_0Q_{1,N}.
 \tag{20}
\]

Then ||D_N||op<=2, P_2 D_N=D_N P_1, B_N and its adjoint converge strongly
to A0 and A0*, and B_N intertwines U1 and U2.
Train exactly the book's finite-action equations (H2.4)--(H2.5), with
w0=g, M0=D_N, c0=0. No fit, trajectory or future endpoint is used in (19)--(20).
This is a data-dependent symmetrization of a dense approximation hierarchy;
it is not asserted to be the previously fixed p=1 dictionary.

In feature time its equations are the gradient ascent of b_N in the
physical coefficient norm ||dw||2^2+||dM||F^2+||dc||2^2. This follows
by direct differentiation of

\[
 H_a^2=\phi\!\left(b_{2,N}^TM\,E_1[b_{1,N}\phi(w\cdot x_a/\sqrt2)]\right).
\]

The matrix gradient is the average of the two signed outer products,
and the first-row gradient uses M^T. Thus (10)--(13) apply in this
coefficient metric. The symmetry transformation uses R,U1,U2 and
M -> P_2 M P_1. The Frobenius norm is preserved, initialization is fixed,
and the unique finite-order dynamics preserves it.

For completeness these feature flows are globally defined on every finite
feature interval. The characteristic local field is Lipschitz in the norm
L-infinity for w-g and c, and Frobenius for M, since the fixed dictionary
marks are bounded. The integral map is a contraction for a sufficiently
short interval in a bounded ball. Contraction norms of the dictionary maps
give

\[
 \|c(s)\|_\infty\le s,\quad
 \|M(s)-D_N\|_F\le s^2/2,\quad \|M(s)\|_{\rm op}\le2+s^2/2.
 \tag{21}
\]

Indeed c_s is bounded by one, and each averaged matrix rank has norm
at most ||c||2. The first-row pointwise speed is at most
L_1(N)(2+s^2/2)s, where L_1(N) is the fixed finite mark envelope.
These bounds preclude finite-time escape in the local-existence norms.
Bounded speeds give a Cauchy endpoint and the contraction construction
extends it. Thus the feature curve exists through its first b_N=1 level,
which (13) places at s<=1/kappa_N whenever kappa_N=||H_N(0)||2^2>0.
The physical clock diverges at that level by the bounded derivative
argument used for (17). This proves global physical existence and fitting
for every such finite order.

Strong convergence of B_N on the two fixed initialized first-feature
fields, followed by the Lipschitz activation, gives

\[
 \kappa_N\longrightarrow\kappa(k)>0.
 \tag{22}
\]

Consequently for all sufficiently large N, kappa_N>=kappa/2. Uniformly
over those orders,

\[
 L_N(t)\le e^{-2\kappa t},\qquad
 \int_0^\infty\|\dot S_N(t)\|_{\rm coefficient}dt
 \le\sqrt{2/\kappa}.
 \tag{23}
\]

Each has a fitted endpoint and remaining travel at most
sqrt(2/kappa) exp(-kappa t). The represented learned action increment
has HS norm no larger than its matrix coefficient increment, because
both dictionary synthesis maps are contractions. Thus (23) also controls
travel in the common raw carrier.

### Predictor compactness, without hidden-state identification

Let B=sqrt(2/kappa). Every reached state and endpoint satisfies
||c||2<=B, ||w||2<=sqrt(2)+B, ||A_N||op<=2+B.
The predictors are uniformly bounded by B and have input Lipschitz constant
at most B(2+B)(sqrt(2)+B) in normalized-circle coordinates.
Their scalar gradient norms in coefficient space are bounded by
D=sqrt(1+B^2{1+(2+B)^2}); dictionary contractions justify the same bound
for the matrix block. Equations (11) and (23) give a common physical-time
Lipschitz bound 2D^2 and a uniform endpoint estimate

\[
 \sup_x|f_N(t,x)-f_N(\infty,x)|
 \le DB e^{-\kappa t}.
 \tag{24}
\]

Hence every sequence of orders tending to infinity has a subsequence whose
predictions converge uniformly on the whole circle and all t in [0,infinity],
including the endpoint. Here is an elementary compactness argument:
extract successive subsequences for a countable dense time/input set and
for a countable dense set of endpoint inputs; bounded scalar sequences have
convergent subsequences. Take the diagonal subsequence. On each compact
time interval the common Lipschitz bounds and finite nets make this sequence
uniformly Cauchy. The common bound (24) and the endpoint input nets then
make it uniformly Cauchy on the remaining infinite time interval.
Its limit satisfies the same exponential training-loss bound and fits at
infinite time.

No uniqueness of this subsequential predictor and no identification with
the exact-network population GF is claimed. This result separates fitting
and observable compactness from the missing strong-state/causal estimate.
On the already established local interval, the book's one-reference
comparison does identify the entire approximation sequence with canonical
GF: these filters remain contractions with both strong action limits, so
the proof of (H2.10)--(H2.16) applies using the all-law local source tails.

## 5. Surgical rejection of two tempting proof shortcuts

### 5.1 Physical damping is not a bound on frozen-source response

On a symmetric smooth finite-dimensional realization the full physical
vector field is F=2(1-b) grad b. Its linearization is

\[
 DF[v]=-2\langle\nabla b,v\rangle\nabla b
                  +2(1-b)D^2b[v].
 \tag{25}
\]

The first term damps the prediction-changing direction. The named-source
calculus of III.F.4 holds population contractions, residuals, and already
computed response coefficients fixed. In differentiating the scalar
factor 2(1-b), its derivative is therefore zero in that calculus.
Other frozen coefficients also remove terms. Equation (25) cannot be
substituted for the source-derivative recursion. Even as a physical
identity its explicitly negative part controls only one scalar prediction
mode, leaving the curvature on neutral directions uncontrolled.
This rejects that direct proof route, not every possible energy-based
response estimate.

### 5.2 The correlated lower gates cannot both be straightened

For |k|<1, let z_a=w dot x_a/sqrt(2) and beta=phi'>0. With arbitrary incoming
controls the lower dynamics has vector fields
X_1=beta(z_1)(1,k)^T and X_2=beta(z_2)(k,1)^T. Their bracket is

\[
 [X_1,X_2]
 =k\beta(z_1)\beta'(z_2)(k,1)^T
  -k\beta(z_2)\beta'(z_1)(1,k)^T.
 \tag{26}
\]

If a C2 point-coordinate change made both fields constant, differentiating
the two transformed-field equations and subtracting would give
DF[X_1,X_2]=0. Invertibility and linear independence of (1,k),(k,1)
would force beta'=0 when k!=0, contradicting tanh. This is the book's
J.1 obstruction specialized to the current model. Equal residual magnitudes
do not set the two coordinatewise backward fields equal, so that symmetry
does not evade the obstruction. The case k=-1 is a one-direction
degeneracy; k=0 is the established orthogonal transformation.

## 6. Exact remaining obligation

Finite physical or feature length is not a bound on a causal response row.
In the book's finite-program equations, the reverse field has the form

\[
 Q_i=\zeta_i+\sum_{p\le i}D_{i,p}H_p^1.
 \tag{27}
\]

The centered Gaussian source variance is controlled by the bounded readout.
The learned-rank part of D is controlled by the raw/feature bounds. Its
remaining part contains beta_{i,p}=E[partial_{\xi_p}Delta_i^2].
A sufficient unproved estimate is a finite cap on these actual causal rows
uniform in the refining time mesh on the full feature interval needed for
fitting, for each fixed k<1. The unconditional short-time cap in
C.4.7.10.A proves this only on its stated interval. Its closure uses a
smallness inequality Psi(B)<B, not merely a finite bound on feature time.
Replacing time by a bounded feature horizon does not prove that inequality.

For the common-carrier action approximations another sufficient route is
a uniform marginal backward tail bound, for each finite horizon, such as

\[
 \sup_{N,t,x}\|Q_N(t,x)\mathbf1_{\{|Q_N(t,x)|>R\}}\|_2
 \le C e^{-aR}.
 \tag{28}
\]

Together with a noncircular estimate on omitted-action error production,
this would give the Osgood comparison needed for strong convergence.
If instead one constructs the exact path from uniformly controlled finite
Gaussian programs, their canonical consistency supplies error production;
the finite-network GF bridge still has to be discharged on the enlarged
domain. A bound (28) is a sufficient target, not a proved necessary
condition for every possible construction.

Raw L2 boundedness, finite travel, predictor compactness and exchangeability
do not imply (28). At the purely Hilbert-space level the curves
u_N(t)=(1-e^{-t})e_N in an orthonormal basis have uniform finite length
and smooth time bounds, yet are not strongly precompact at any t>0.
In the actual Gaussian-matrix setting, J.1's bounded adaptive input
v_i=sign(W_iJ) gives (W^T v)_J of order sqrt(n) and nonvanishing
normalized second-moment tails. That example is not asserted reachable
by the neural flow; it rules out ignoring causal origin.

## 7. Partial outcome; exact-network objective not achieved

The existing exact branch obeys a conditional one-residual estimate that
is independent of orthogonality. A symmetry-preserving approximation
hierarchy has uniform fitting estimates. Every sufficiently fine
approximation fits exponentially, and their whole-input predictors are
subsequentially compact even through infinite training time.

The exact arbitrary-angle population limit remains open. The next estimate
must exploit the particular causal backward queries of this pair, rather
than just their energy, operator norm, or physical-flow Hessian. Directly
bounding the contracted response field in (27), rather than the absolute
sum of each source coefficient, was a proposed remaining route; no bound
for it is claimed here. The follow-up in FAILED_FOLLOWUP.md tested the
Gaussian-projection version and failed to obtain more than the existing
second-moment bound. Neither pass achieved the requested exact-network
extension, and these partial calculations should not be presented as doing so.

## Verification and provenance

Lead check: exact unhalved-clock factors, scalar chain rule/adjunction,
Gaussian covariance differentiation including singular endpoints, the
k->1 asymptotic, reflection invariance, ridge/symmetry commutation,
finite-order continuation, contraction of the common-carrier embedding,
all-time predictor compactness, and both failed-route distinctions.
No simulation or empirical claim. No independent-review claim.

Established inputs read completely for the cited units:
global_nonlinear.md C.4 theorem, C.4.5.1.1--3, C.4.6.2.1--5,
C.4.7.2, C.4.7.9.1--5, C.4.7.10.A.1--3, and C.4.9.A.1--2
and A.6. C.4.9.A.5 through (CT32) was read only to locate the temporary-cap
gap; that partial source read is not used to import a theorem.
Also read special_data_limits.md III.F.1--10 and J.1. The original scalar/characteristic
proofs are reused only after the changed direction vectors and symmetrized
lists have been checked above. Unread parts of the broader book are not
used as new theorem premises.

Source SHA-256:

- global_nonlinear.md: 81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c
- special_data_limits.md: 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489
- README.md: 60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad
- NOTATION.md: 199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b
