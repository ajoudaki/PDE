# A variational route for one fixed activation

Status: new independent route and proved canonical finite-width estimates;
not a proof of population continuation. The estimates concern the full
two-residual raw GF and exact GD, not a prescribed contrast driver. No
numerical experiments or additional agents were used.

The new mechanism is to control expansion of the **entire raw variational
flow in a trace norm of its logarithmic strain**, then exploit the exact
alignment of that flow with the canonical loss gradient. This avoids
estimating absolute rows of Gaussian history responses as its first step.
It gives a concrete alternative question about the actual discretization
and approximation errors in the few strongly expanding directions.

The principal results are (17), (20), (23), and the exact error reduction
(29). In particular, (17) and (20) hold at every fixed physical horizon
with a single amplitude e=1/10. Their constants can grow with the horizon.
No e <= e_*(data,T) hypothesis appears.

## 1. Contract, authority, and scope

Keep exactly

    phi(z) = 1 + z + e arctan(z),       e = 1/10,

in all three hidden layers, with the independent Gaussian initialization,
raw metric, two residuals, and eta_n=n^-2 from CONTRACT.md. Thus this route
does not require an activation redesign. Its structural change is in the
proof mechanism. Both label sectors and rho=-1 are included.

The intended quantifiers remain

    one phi; every fixed allowed dataset; every finite physical T.

The intended endpoint is the entire MF/GF/exact-GD and observable contract,
including reached-state restart and persistent nonaffinity. None of those
population conclusions is inferred here from finite-width energy bounds.

Read personally and completely: solve-math-rigorously/SKILL.md,
investigate-conjectures/SKILL.md and its research-contract.md,
evidence-ledger.md, adversarial-audit.md, proof-search-orchestration.md;
also CONTRACT.md, READ_ME_FIRST.md, and
DATA_DEPENDENT_CONSTANTS_CLARIFICATION.md in this directory.
Relevant existing notes were inspected to identify the canonical equations
and to avoid duplicating the local-driver and history-restart mechanisms.
No external theorem is used without a derivation below. The certified
angle-specific theorem is left unchanged and is not re-audited.

There is no coordinate-dependent model parameterization: all calculations
below take place intrinsically in the raw metric already in the contract.
No clipping, altered optimizer, new randomness, or paired populations is
introduced. Singular-vector coordinates are used only to state an estimate.

## 2. Raw Hilbert space and a deterministic bounded region

For width n, let H_n be the raw parameter space, of dimension
m_n=nd+2n^2+n, with squared norm

\[
 \|v\|_{H_n}^2={d\over n}\|vW^1\|_F^2
       +\|vW^2\|_F^2+\|vW^3\|_F^2+\|vC\|_n^2,
 \qquad \|u\|_n^2={1\over n}\sum_i u_i^2.                 \tag{1}
\]

Here C is the contract's rescaled W^4. This is a constant Hilbert metric,
and the exact physical equations are

\[
 \dot\theta=-\nabla L(\theta),\qquad
 \theta_{k+1}=\theta_k-\eta_n\nabla L(\theta_k),\qquad
 L={1\over2}\sum_{a=1}^2(f_a-y_a)^2.                     \tag{2}
\]

All gradients, Hessians, adjoints, and Hilbert--Schmidt norms below use
(1). In particular no extra width factor can be inserted into (2).

Fix B>=1 and consider states satisfying

\[
 \max_a\|z^1_a\|_n,\quad
 \|W^2\|_{\rm op},\quad\|W^3\|_{\rm op},\quad\|C\|_n
 \ \le B.                                                \tag{3}
\]

The elementary bounds |phi(z)|<=2+2|z|, |phi'|<=2, and
|phi''|<=e give

\[
 \|h^1_a\|_n\le4B,\quad
 \|h^2_a\|_n\le10B^2,\quad
 \|h^3_a\|_n\le22B^3.                                   \tag{4}
\]

Set b^3_a=C, b^2_a=(W^3)^*delta^3_a, and
b^1_a=(W^2)^*delta^2_a, so delta^l_a=phi'(z^l_a)b^l_a.
These are the actual backwards quantities. Consequently

\[
 \|b^3_a\|_n\le B,\quad\|b^2_a\|_n\le2B^2,\quad
 \|b^1_a\|_n\le4B^3,\qquad
 \|\delta^3_a\|_n\le2B,\quad\|\delta^2_a\|_n\le4B^2.       \tag{5}
\]

Let T^l_a:H_n -> (R^n,||.||_n) be the derivative of z^l_a at
the current state. For v in H_n the exact first variations are

\[
 T^1_av=(vW^1)x_a,
\]
\[
 T^2_av=(vW^2)h^1_a+W^2D^1_aT^1_av,
 \quad
 T^3_av=(vW^3)h^2_a+W^3D^2_aT^2_av,                     \tag{6}
\]

where D^l_a=diag(phi'(z^l_a)). Since ||x_a||=sqrt(d), (1)
gives ||T^1_a||op<=1. Using
||Mh||_n<=||M||_F||h||_n in (6) gives

\[
 \|T^1_a\|_{\rm op}\le1,\qquad
 \|T^2_a\|_{\rm op}\le6B,\qquad
 \|T^3_a\|_{\rm op}\le22B^2.                            \tag{7}
\]

Thus ||grad f_a||<=66B^3: the two terms in
df_a[v]=<vC,h^3_a>_n+<C,D^3_aT^3_av>_n have bounds 22B^3
and 44B^3. All these estimates use the actual two-sample network and
do not require a nonsingular input Gram matrix.

## 3. Exact Hessian decomposition and its width dependence

Differentiating once more, including both occurrences of each trained
matrix, gives the exact quadratic form

\[
\begin{split}
 d^2 f_a[v,v]={}&2\langle vC,D^3_aT^3_av\rangle_n\\
 &+\sum_{l=1}^3
   \langle b^l_a,\phi''(z^l_a)(T^l_av)^2\rangle_n\\
 &+2\sum_{l=2}^3
   \langle\delta^l_a,(vW^l)D^{l-1}_aT^{l-1}_av\rangle_n.
                                                               \tag{8}
\end{split}
\]

For verification, d^2z^2[v,v] equals
2(vW^2)D^1T^1v+W^2[phi''(z^1)(T^1v)^2]. The corresponding
expression for d^2z^3 has those two terms for layer 3 and additionally
W^3D^2 d^2z^2. Substituting them into d^2<C,phi(z^3)> yields
(8), after moving both trained matrices through the inner products.

Write Hess f_a=S_a+K_a, where S_a contains the first and last lines
of (8), and K_a is the middle line. There are two different bounds:

\[
 \|S_a\|_{\rm op}\le152B^2,
 \qquad
 \|K_a\|_{\rm HS}\le560e\sqrt n B^5.                    \tag{9}
\]

Here is a proof of the scaling in (9), rather than an operator-norm
bound on an arbitrary multiplication operator. For a field q, multiplication
M_q on the normalized neuron Hilbert space has

\[
 \|M_q\|_{\rm HS}^2=\sum_iq_i^2=n\|q\|_n^2.
\]

The l-th curvature operator is
(T^l_a)^*M_{b^l_a phi''(z^l_a)}T^l_a. The ideal inequality for HS
norms follows by summing squared norms on an orthonormal basis, and gives
its bound sqrt(n)e ||b^l_a||_n ||T^l_a||op^2. Their sum is at most

\[
 e\sqrt n(4B^3+72B^4+484B^5)\le560e\sqrt n B^5.
\]

For the mixed term at layer l, the map
R_l v=(vW^l)^*delta^l_a has operator norm <=||delta^l_a||_n.
Hence its symmetric quadratic-form operator has norm at most
2||delta^l_a||_n ||D^{l-1}_a||op ||T^{l-1}_a||op.
For layers 2 and 3 these are 16B^2 and 48B^2. The readout mixed
term has norm <=2*2*22B^2=88B^2. Their sum is 152B^2.

Each curvature term has rank <=n, and each symmetrized mixed term
has rank <=2n. Also ||R_l||HS=sqrt(n)||delta^l_a||_n;
the readout projection has HS norm sqrt(n). The same calculation yields

\[
 \operatorname{rank}(\operatorname{Hess} f_a)\le9n,
 \quad
 \|\operatorname{Hess} f_a\|_{\rm HS}\le800\sqrt n B^5.    \tag{10}
\]

These bounds control a trace of the actual full Hessian. They do not
replace the unresolved multiplication-operator bound by an L2 bound.
Indeed (9) asserts HS control with the stated sqrt(n) factor, not
width-uniform operator control of K_a.

The loss Hessian has the exact decomposition

\[
 H=\operatorname{Hess} L=G+S+K,
 \quad G=\sum_a\nabla f_a\otimes\nabla f_a\succeq0,
 \quad S=\sum_a r_aS_a,\quad K=\sum_a r_aK_a.             \tag{11}
\]

With R(t)=sum_a|r_a(t)|, (9) becomes

\[
 \|S(t)\|_{\rm op}\le a(t):=152B^2R(t),
 \qquad \|K(t)\|_{\rm HS}\le560e\sqrt n B^5R(t).          \tag{12}
\]

This retains the residual signs in (11); the absolute values enter
only its norm bounds. In particular G is positive and will not be
charged as a source of variational expansion.

## 4. A logarithmic strain lemma, including noncommuting generators

Suppose J'=A(t)J, J(s)=I, with A(t) symmetric, and write

    A(t) = -Q(t) + E(t),       Q(t) >= 0.

Define P=JJ^*>0 and

\[
 \mathcal E(P)={1\over4}\operatorname{tr}[\log_+(P)]^2.
                                                               \tag{13}
\]

The eigenvalues of P are the squared singular values of J; hence
E(P)=sum_j (log_+ sigma_j(J))^2. The scalar function
(log_+x)^2 is continuously differentiable on (0,infinity), including
x=1. Its spectral trace has derivative equal to the trace of its
scalar derivative times P'. This can be checked first for polynomials
by cyclicity of trace, and then by approximating the function and its
derivative on a compact interval containing the spectrum locally in time.
Since P'=AP+PA and P commutes with log_+P, this gives

\[
 \mathcal E' =\operatorname{tr}(A\log_+P)
 \le\|E\|_{\rm HS}\|\log_+P\|_{\rm HS}
 =2\|E\|_{\rm HS}\sqrt{\mathcal E}.                     \tag{14}
\]

The dropped term is nonpositive: both Q and log_+P are positive
semidefinite, so tr(Q log_+P)=tr(Q^(1/2) log_+P Q^(1/2))>=0.
Regularizing sqrt(E) by sqrt(E+epsilon), integrating, and letting
epsilon decrease to zero proves

\[
 \left(\sum_j(\log_+\sigma_j(J(t,s)))^2\right)^{1/2}
       \le\int_s^t\|E(u)\|_{\rm HS}\,du.                \tag{15}
\]

No simultaneous diagonalization, commutation between different times,
or normality of J is assumed.

## 5. First canonical global estimate: excess logarithmic response

For raw GF let J_n(t,s) be its full parameter derivative from a state
reached at time s. It solves J'=-HJ. Put

\[
 A_B(t,s)=152B^2\int_s^tR(u)du,
 \qquad \widetilde J_n(t,s)=e^{-A_B(t,s)}J_n(t,s).         \tag{16}
\]

The generator of J-tilde is -(G+S+aI)-K. The first parenthesis is
positive semidefinite because ||S||op<=a. Applying (15) with E=-K
proves the canonical estimate

\[
 {1\over n}\sum_{j=1}^{m_n}
   [\log\sigma_j(J_n(t,s))-A_B(t,s)]_+^2
 \le (560eB^5)^2\left(\int_s^t R(u)du\right)^2.          \tag{17}
\]

This is a fixed-e estimate for the complete two-sample raw GF. It is
valid at every time for which (3) holds; Section 7 supplies such a
bound on every fixed physical interval. It does not assume population
existence, a Gaussian backward tail, or control of any history response.

For example, for every u>0,

\[
 {1\over n}\#\{j:\sigma_j(J_n(t,s))>e^{A_B(t,s)+u}\}
 \le{(560eB^5\int_s^tR)^2\over u^2}.                   \tag{18}
\]

Thus strong expansion above a deterministic affine-size envelope can
occur only in a small fraction, measured on the n-neuron scale, of
raw tangent directions. The state dimension is order n^2; the
normalization in (17)--(18) is n, not m_n. The curvature contribution
vanishes at e=0, when (17) gives ||J||op<=exp(A_B) directly.

## 6. The analogous estimate for the exact GD derivative

At GD nodes set H_k=Hess L(theta_k), R_k=sum_a|r_{k,a}|,
a_k=152B^2R_k. Suppose eta||H_k||op<1, as verified in Section 7.
Then I-eta H_k is positive definite and the exact derivative is

\[
 J^{GD}_{k,l}=(I-\eta H_{k-1})\cdots(I-\eta H_l).
\]

Rescale each factor by 1+eta a_k and put

\[
 A^{GD}_{k,l}=\sum_{j=l}^{k-1}\log(1+\eta a_j).
                                                               \tag{19}
\]

The rescaled factor equals I-eta Hbar_k, where
Hbar_k=(H_k+a_kI)/(1+eta a_k). Its negative part has HS norm
at most ||K_k||HS/(1+eta a_k). To check this last assertion, write
Hbar=Q+E with Q>=0; in an orthonormal eigenbasis for its negative
eigenvalues -mu_i, one has mu_i<=|<v_i,Ev_i>|, whence
sum mu_i^2<=||E||HS^2.

Join these derivative factors mathematically by symmetric generators
eta^-1 log(I-eta Hbar_k). Their positive parts have HS norm at most
||Hbar_k,-||HS, since log(1+eta mu)/eta<=mu for mu>=0.
The resulting product at each node is exactly the GD derivative above,
rescaled by exp(-A^GD). This interpolation is only a proof of a matrix
inequality; it makes no change to the raw GD algorithm or its prescribed
parameter interpolation. Equation (15) therefore gives

\[
 {1\over n}\sum_j
   [\log\sigma_j(J^{GD}_{k,l})-A^{GD}_{k,l}]_+^2
 \le(560eB^5)^2\left(\eta\sum_{j=l}^{k-1}R_j\right)^2.    \tag{20}
\]

The sharper right side with factors 1/(1+eta a_j) is also valid.
Since A^GD<=152B^2 eta sum R_j, (20) has the same useful
finite-horizon form as (17).

## 7. Applicability to the original Gaussian initialization and eta_n

For finite n, smoothness gives local raw GF. Its exact energy identity is

\[
 L(t)+\int_0^t\|\dot\theta(u)\|_{H_n}^2du=L(0),\qquad
 \|\theta(t)-\theta(0)\|_{H_n}\le\sqrt{tL(0)}.            \tag{21}
\]

Every component in (3) changes by at most this displacement. In finite
dimension (21) prevents finite-time escape, so finite GF is global.
This argument is used only to put finite GF in the region required for
the response estimate; it does not construct a population solution.

There are events of probability tending to one on which the initial
sizes in (3) are <=B_0=10 and L(0)<=4. For completeness: each first
preactivation has iid N(0,1) coordinates, so its squared RMS converges
to 1; this is applied to the two marginals without asserting their
independence. The readout RMS tends to zero under its prescribed
variance n^-2. Each initial hidden matrix has op norm <=10 with
probability tending to one: two 1/4-nets of the Euclidean sphere have
size <=9^n each, ||W||op<=2 max_net|u^TWv|, and the Gaussian tail
for u^TWv, of variance 1/n, bounds the failure probability by
2 exp[(2log9-25/2)n]. Equation (4) at initialization then makes f_a(0)
tend to zero and L(0) tend to 1. The Gaussian blocks remain independent
as stipulated; no substitute initialization is used.

Fix T. On these events choose

    B = B_0 + sqrt(8(T+1)) + 1.

This covers GF and, for all sufficiently large n, GD nodes and step
segments through T. Here are the GD details to avoid an implicit
GF-to-GD comparison. On (3), |r_a|<=23B^4, and (7),(10),(11) give
||H||op<=50000 sqrt(n) B^9 on every such segment. At a node with
L<=4, ||grad L||<=264B^3. For sufficiently large n, the step
eta_n=n^-2 has displacement <=1 and eta_n||H||op<=1 throughout
the segment. Taylor's formula then proves

    L_{k+1} <= L_k - (eta_n/2)||grad L_k||^2.

Cauchy--Schwarz bounds the cumulative raw displacement through time
T+1 by sqrt(2(T+1)L_0)<=sqrt(8(T+1)). Inductively this leaves the
unit margin needed for every segment and closes the estimate. Taking
n a little larger makes eta_n||H||op<1 as required in Section 6.

For GF, R(t)<=2sqrt(L_0); for GD the same holds at nodes. Thus
(17) and (20) have finite constants on every fixed T, uniformly in
width on these high-probability events. None of this uses a lower
bound on 1-rho or on 1+rho.

## 8. A second canonical ingredient: gradient alignment

Let g_s=grad L(theta(s)) along finite raw GF. Differentiating along
the flow gives g_s'=-H_s g_s. Therefore the same variational equation
as for J yields the exact identity

\[
                  J_n(t,s)g_s=g_t.                      \tag{22}
\]

For any singular-value decomposition J=U diag(sigma_j)V^*, this says

\[
 \sum_j\sigma_j^2|\langle v_j,g_s\rangle_{H_n}|^2
       =\|g_t\|_{H_n}^2\le(264B^3)^2.                   \tag{23}
\]

In particular, if P_{>M}(t,s) is the orthogonal projection onto the
right singular directions of J with sigma_j>M, then

\[
 \|P_{>M}(t,s)g_s\|_{H_n}\le {264B^3\over M}.            \tag{24}
\]

These are actual reachable-state alignment estimates, with no random
probe and no independence assumption between J and g. They show why a
worst-direction exponential response estimate can misdescribe the
canonical flow. They also suggest a specific way the logarithmic
estimate could become useful: the actual approximation forcing may
inherit part of this suppression in expanding directions.

That inheritance is not proved. Equation (22) concerns the full loss
gradient. It does not separately control a layer projection of that
gradient, its material derivative H_s g_s, a Gaussian query perturbation,
or the averaged Hessian of two different trajectories. Splitting the
gradient into blocks can destroy the cancellation in (22).

## 9. Exact GD/GF error reduction and the unclosed implication

Let theta_h(t) be the contract's linear raw GD interpolation and let
theta(t) be GF with the identical finite-width initialization. Both
have the bounds of Section 7. Put V=-grad L and

\[
 \tau_h(t)=V(\theta_k)-V(\theta_h(t)),\quad k\eta\le t<(k+1)\eta.
                                                               \tag{25}
\]

The Hessian estimate and the actual size of the raw step give

\[
 \sup_{t\le T}\|\tau_h(t)\|_{H_n}
       \le C_{B}\eta_n\sqrt n=C_B n^{-3/2}.             \tag{26}
\]

For e_h=theta_h-theta the fundamental theorem of calculus gives exactly

\[
 e_h'=-\overline H(t)e_h+\tau_h(t),\quad
 \overline H(t)=\int_0^1
  \operatorname{Hess}L(\theta(t)+v e_h(t))\,dv.           \tag{27}
\]

The segment between the two states still satisfies (3). Its averaged
Gauss--Newton term is positive semidefinite; its averaged mixed term
has uniformly bounded operator norm, and its averaged curvature term
has HS norm <=C_B sqrt(n). Thus the proof of (17) applies also to the
propagator Psi_n(t,s) of (27), with finite constants A_T,C_T. A rank
bound on the averaged Hessian is not needed for this step.

For any fixed 0<alpha<3/2, let P_bad(t,s) be the right-singular
projection of Psi_n(t,s) for singular values >n^alpha. For sufficiently
large n, (17) gives

\[
 {\operatorname{rank}P_{bad}(t,s)\over n}
       \le {C_T\over(\alpha\log n-A_T)^2}.              \tag{28}
\]

Duhamel's formula now supplies the exact useful reduction

\[
 \sup_{t\le T}\|e_h(t)\|_{H_n}
 \le C_T n^{\alpha-3/2}
 +\sup_{t\le T}\int_0^t
       \|\Psi_n(t,s)P_{bad}(t,s)\tau_h(s)\|_{H_n}\,ds.   \tag{29}
\]

The first term is proved to vanish. The **exact unclosed canonical
implication for the GD/GF part of this route** is that the last term
in (29) tends to zero in probability for the original Gaussian
initialization. The rank bound (28) alone does not imply it: the
actual forcing and singular spaces are dependent, and the singular
values on the exceptional space have not been bounded. This is not
an appeal to an arbitrary Hilbert-ball counterexample; (25)--(29)
specify the genuine finite-network source and its propagator.

Equation (24) suggests testing suppression of the material-derivative
and block-gradient sources that generate tau_h, using the full
gradient structure. Differentiating (22) without controlling these
additional sources does not close (29).

There is a separate population obligation. Even a proof that (29)
vanishes would only identify same-width GF and eta_n-GD. To construct
the autonomous population state by finite Gaussian programs, one still
needs a mesh-refinement/approximation estimate uniform in width and
uniform integrability of the relevant backward fields. In this route
one would have to prove corresponding weighted exceptional-direction
bounds for the *actual Gaussian-program approximation sources*. A raw
parameter derivative is not automatically a formal derivative with
respect to an independently named matrix-answer source. This distinction
is a substantive missing bridge, not a change of notation.

Likewise, a log-square singular-value tail does not imply an exponential
moment of log singular values, and therefore does not by itself imply
any second moment of the response operator on an isotropic probe.
No subGaussian tail is claimed in this note.

## 10. Why this is a distinct route and its current ledger

The retained mechanism is whole-gradient geometry: finite-rank
second variations on the n-neuron scale, a positive Gauss--Newton term,
matrix logarithmic strain, and canonical gradient alignment. It does
not use pure-q invariants, a fresh-history restart, covariance inversion,
or a small nonlinear perturbation over a data-dependent feature interval.
The route is compatible with the fixed activation already known to have
nonzero initial feature-learning certificates. It does not transfer the
angle-specific proof of all-time nonaffinity to e=1/10 at arbitrary data.

| Claim | Status and rung | Exact support / missing step |
|---|---|---|
| Raw Hessian decomposition and op/HS split | Proved; exact finite construction | (8)--(12), both matrix orientations retained |
| Fixed-e compact-time logarithmic response for canonical GF | Proved; finite canonical estimate | (13)--(18),(21); no population inference |
| Same estimate for raw eta_n-GD | Proved; finite canonical estimate | (19)--(20), descent and step conditions in Section 7 |
| Gradient suppression in expanding right-singular spaces | Proved; reachable-state identity | (22)--(24) for the full GF loss gradient only |
| Canonical Euler error is O(n^-3/2) before propagation | Proved; error production | (25)--(26) |
| Full GD/GF stability from these estimates | Open; error propagation | Last term of (29) |
| Population identification, tails, uniqueness and restart | Open; limit identification and compact horizons | Actual Gaussian-program sources need their own exceptional-direction estimate and uniform integrability |
| Full contract for one activation | Open | Population bridge plus all observables and persistent nonaffinity remain required |

Approach registry: **VLS -- variational logarithmic strain**.
Status: viable new bounded route with a proved canonical estimate and
an exposed propagation bottleneck; not a complete proof candidate.
Highest-leverage next lemma: control the last term of (29) by deriving
the analogue of (23) for its actual material-derivative forcing. An
estimate only for g_s, or only for the rank in (28), is insufficient.
If the material-derivative forcing does not inherit such suppression,
the current alignment mechanism is insufficient; that would not
falsify the universal-activation theorem.

Supersession: none. The certified angle-dependent theorem, the local
driver lemmas, and the unresolved Gaussian history-continuation claims
retain their existing scopes. This note adds finite canonical response
and alignment estimates; it does not upgrade any of those scopes.
