# C-X3: fixed-depth local raw flow and actual-network capture

Frozen candidate, 2026-09-20. Scoped author proof; internally checked, not
an independent review or established-library addition. No numerical experiment
or training run is used.

## 1. Scope and source audit

This proves CONTRACT §§2–3 clauses 1, 2 and 4, at three hidden layers and
at every separately fixed finite hidden depth. It supplies the common raw
target and stability input needed by the hierarchy branch. It does **not**
prove the strict activity/nonaffinity clause, hierarchy or numerical
implementation clause, substantial-training branch, or a global population
flow. Those remain separate obligations.

The scientific inputs read were CONTRACT §§2,3,5; `docs/NOTATION.md`;
`docs/global_nonlinear.md` C.1–C.2, C.4.1–C.4.3, C-H3 A–B and A.1–A.4;
and the maintained dependencies `docs/special_data_limits.md` III.F.1–10.
The added dependencies are exclusively the common-carrier, finite-program,
rank-norm and scalar-chain-rule foundations. No other study was read.
The solve-math-rigorously and investigate-conjectures skills, including the
contract and adversarial-audit references, were applied.

The maintained source has precisely the following scope, used below.

* C.2 is already a weighted **fixed finite depth** response/tail theorem.
  Its constants are independent of finite input count, positive masses,
  covariance rank and time mesh. Its last paragraph explicitly invokes A.2
  for fixed neural programs; it does not invoke an all-moment scalar-feedback
  theorem. Its bounds do not by themselves prove raw HS existence or law
  completion.
* C.1's main topology retains first preactivations at a fixed input list and
  middle operator norms. Its conclusions cannot simply be renamed full-row
  and HS conclusions. The rank estimates below provide that strengthening.
* III.F.1–5 concern each separately fixed finite program before width tends
  to infinity. Gaussian matrix identities and orientations remain distinct.
  Singular queries are handled by fixed-program regularization, not a
  continuity assertion for pseudoinverses.
* A.1 extends values and second moments to continuous linear-growth maps.
  A.2 supplies the named-source derivatives for the bounded-gate times
  unbounded-field instructions used here. All deterministic contractions,
  source covariances and response coefficients are frozen in such derivatives.
* III.F.7 constructs generated actions with their actual adjoints for every
  fixed depth. III.F.8 gives the raw HS metric, and III.F.9–10 give strong
  curve chain rules and scalar prediction gradients. None of these states
  local Lipschitzness of the neural vector field on all of raw L2.
* C.4.3 supplies the two-layer fixed-reference strategy for arbitrary
  growing datasets and every vanishing GD step. The proof below establishes
  its depth induction, HS strengthening, Borel-law extension and observations.
* C-H3 A has the stronger literal two-layer time 1/200. The present constants
  at L>=3 do not replace that maintained time or any C-H4 assertion.

## 2. Precise local result

Fix L>=2. Use exactly the bias-free tanh network, variances, mobilities,
unhalved probability-weighted loss and physical clock in CONTRACT §2.
For each separately fixed d there are L canonical generated probability
spaces H_l=L2(Omega_l), a full Gaussian row g in H_1^d, and L-1 independently
initialized action labels A_l,0:H_(l-1)->H_l with actual adjoints. Put

\[
 E_d=H_1^d\oplus\bigoplus_{l=2}^L\mathcal S_2(H_{l-1},H_l)
                         \oplus H_L,\qquad
 \theta=(w,K_2,\ldots,K_L,c),\quad A_l=A_{l,0}+K_l.
\]

The raw squared norm is the sum of the squared component norms in E_d.
For estimates let e be the **sum** of those component norms; these two
norms are equivalent with constants depending only on L. The initial state
is (g,0,...,0). Only K_l is HS; A_l,0 need not be HS.

There is T_L>0, specified constructively in §5, such that:

1. Every Borel law on sqrt(2) S1 x [-1,1] has a unique canonical strong C1
   solution of CONTRACT §2 on [0,T_L]. Uniqueness is among all continuous
   strong raw integral solutions on its initialized carrier, with no
   additional tail condition on a competing solution. The reached state
   uniquely determines continuation under the same law for the remaining
   interval.
2. The same conclusion holds for every separately fixed finite d,m, every
   normalized input list, bounded labels |y|<=1 and positive probability
   weights, with the full row retained. Repeated, parallel or antiparallel
   inputs and singular Grams are allowed. For labels bounded by Y replace
   1 by Y in the bounds below. T_L depends only on L and Y, not on d,m,
   masses or rank. Width convergence here is for separately fixed d; no
   assertion for growing dimension is made.
3. On the circle, for q=W1(mu,nu)<=1 in cost |u-v|+|y-z|,
   \[
   \sup_{t\le T_L}e(\theta_\mu(t),\theta_\nu(t))
       \le C_L q\exp(C_L\sqrt{\log(e/q)}),                 \tag{1}
   \]
   with value zero at q=0. Forward fields and predictions have the same
   modulus uniformly in time and direction. Backward fields and every
   fixed admitted same-layer observation graph are continuous in law,
   uniformly on compact time/input query sets. This last continuity need
   not have the displayed quantitative modulus.
4. For n_j->infinity, eta_j->0 and deterministic Borel laws lambda_j->mu
   in W1 on the circle, actual finite simultaneous raw GD, with affine
   interpolation of raw parameters and recomputed fields, converges to
   theta_mu in the observation sense of §9. This includes whole-circle
   predictions, same-layer joint second-moment observations, paired
   initial/current activation laws and their training-averaged RMS motion,
   and risks, uniformly in time. Finite GF has the same conclusion.
   Independent iid empirical laws of any sample counts tending to infinity
   have the same joint-probability conclusion, with no relation between
   sample count, width and eta. Finite laws need no restriction on growing
   count or vanishing atom masses in this circle assertion.
5. For each fixed finite dataset in fixed d the convergence also retains
   C.1's same-layer joint hidden-path W2 laws for the uniform path norm,
   integrated squared hidden speeds, kernels and admissible fixed probes,
   as well as whole-sphere prediction. There is no cross-layer pairing of
   neuron indices and no operator-norm comparison across widths or carriers.

The estimate also proves the same all-Borel statement for each separately
fixed d on its compact sphere. That strengthening is not required for the
circle contract; none of the proof uses a growing-dimension limit.

## 3. Common initialized carrier and exact raw equation

Use III.F.7's countable language with all d first-row coordinates, zero
top readout, constants, rational linear combinations, tanh and its smooth
bounded gates, smooth clipped products, a dense countable family of bounded
smooth cylinder functions, and both orientations of **each** edge label.
Finite unions run on the same initialized finite arrays. III.F.1–5 and
A.1–2 give their compatible limiting same-layer laws. The generated L2
spaces are the completions of their spans. The elementary norm estimate

\[
 \Pr(\|A_{l,0,n}\|_{op}>10)
       \le2\,9^{2n}e^{-100n/8}\longrightarrow0
\]

passes to generated second moments. It makes each assignment a bounded
linear action of norm at most 10. Finite normalized adjunction passes to
the dense generated spans and then to their completions, identifying the
reverse action with A_l,0*. This is one canonical realization up to the
coordinate-preserving L2 isometry, independent of the training law.
Distinct causal enumerations agree because their finite programs agree.
The roots include the full row even if the training inputs do not span Rd.

Real coefficients, directions and bounded continuous linear-growth
instructions are represented by fixed approximations followed by L2
completion, as in A.1. Thus every fixed finite-law Euler program and any
finite passive observation graph live on this carrier. Its action/source
description is not a procedure that samples a new Gaussian answer whenever
an action is reused.

Write phi=tanh. For u on the unit sphere define

\[
 Z_1=w\cdot u,\quad H_1=\phi(Z_1),\qquad
 Z_l=A_lH_{l-1},\quad H_l=\phi(Z_l),\qquad f=\langle c,H_L\rangle_L,
\]
\[
 P_L=c,\quad\Delta_l=\phi'(Z_l)P_l,\qquad
 P_l=A_{l+1}^*\Delta_{l+1}\quad(l<L).
\]

For r=f-y, the vector field is

\[
 F_\mu(\theta)=-2\left(
 \int r\Delta_1u\,d\mu,
 \left(\int r\Delta_l\otimes H_{l-1}\,d\mu\right)_{l=2}^L,
 \int rH_L\,d\mu\right).                                  \tag{2}
\]

Here (a tensor b)v=a E[bv], with b and v in the same population. Its HS
norm equals ||a||2 ||b||2. In finite coordinates (2) is exactly the raw
update: the row/readout have ordinary norms divided by sqrt(n), and the
middle increments have ordinary Frobenius norm; a rank is a b^T/n.
Thus the finite raw squared metric is

\[
 \|\dot W^1\|_F^2/n+\sum_{l=2}^L\|\dot W^l\|_F^2
                                    +\|\dot c\|_2^2/n.       \tag{3}
\]

For a row field w define its directional norm
||w||dir=sup_|u|=1 ||w.u||2. It is bounded by its full-row L2 norm,
but ||g||dir=1 even though ||g||2=sqrt(d). The distinction only improves
constants; state distances always use the full-row L2 norm.

## 4. Uniform preliminary ball and vector-field continuity

Take B=12. Initially the population actions have norm <=10, the row
directional norm is 1 and c=0. At finite width, with probability tending
to one, all actions have norm <=10, the row map W1/sqrt(n) has operator
norm <=2, and ||c0||2/sqrt(n)<=1. The last two assertions follow respectively
from convergence of the fixed d by d sample covariance to I_d and
E||c0||2^2/n=n^-2. The event is independent of the training law.

As long as the sum of raw increments from initialization is <=1, all
action norms, directional row norms and readout norms are <=B. Then

\[
 \|H_l(u)\|_2\le1,\qquad
 \|P_l(u)\|_2,\|\Delta_l(u)\|_2\le B^{L-l+1},\quad
 |r|\le B+1.                                                \tag{4}
\]

The sum norm of (2) is at most

\[
 V_L=2(B+1)\left(1+\sum_{j=1}^L B^j\right),\qquad
 T_{ball}=\min(1,(8V_L)^{-1}).                               \tag{5}
\]

GF and Euler paths of maximal mesh <=T_ball stay in this increment ball
through time 2T_ball: before a first exit their total displacement is at
most 2T_ball V_L<=1/4. At a putative exiting Euler step the same sum
bound uses its preceding state, so also excludes that exit. The same
estimate holds for affine interpolants. This proves a law-independent
bound in the exact HS metric, not by replacing it with operator norm.
Only finitely many initialized matrices occur at fixed L.

The field (2) is continuous in raw state and input. For its one potentially
delicate operation, if z_j->z in probability and v_j->v in L2, and b is
bounded continuous, subtract b(z_j)(v_j-v). For the remaining term use
bounded convergence in probability on |v|<=M and bound the complement by
2||b||infinity ||v 1_|v|>M||2. First j->infinity, then M->infinity.
This proves b(z_j)v_j->b(z)v in L2. Apply it downward through the finitely
many gates, using bounded actions at each step. Forward continuity is
Lipschitz. The rank identity gives HS continuity of every middle integrand.

Compactness of the data space makes this continuity uniform in input
along a convergent state sequence: any contrary input sequence has a
convergent subsequence. Each integrand has compact separable range and is
bounded, so is Bochner integrable in its raw component. For a fixed
continuous Banach-valued integrand G and a coupling of mean distance q,

\[
 \left\|\int G\,d\mu-\int G\,d\nu\right\|
       \le\omega_G(a)+2\|G\|_\infty q/a.                    \tag{6}
\]

Taking q->0 then a->0 proves joint continuity of (mu,theta)->F_mu(theta).
No locally Lipschitz vector field on an ambient L2 ball has been assumed.

## 5. The finite-depth tail input, including passive queries

Apply C.2 with every activation tanh, all sigmas and mobilities one,
|G_ab|<=1, Gaussian first projections of variance one, zero readout root,
residual bound R0=B+1 and source bound S=B^L from (4). Its derivative
formulas apply by A.2 to each **fixed** finite Euler program. In particular
the learned actions are expanded as finite sums of ranks before applying
that source rule.

Here is the depth dependence and the induction needed from that lemma.
Let J=2R0 S^2. For edge l let C_l denote the expected derivative of a
lower forward feature in an edge-l reverse source, and let A_l^resp denote
the expected derivative of an upper delta in an edge-l forward source.
These response symbols are not the weight action A_l. The exact field
representations are

\[
 Z_{a,k,l}=\xi_{a,k,l}+\sum_{b,s<k}F_{ak,bs,l}\Delta_{b,s,l},
 \quad P_{a,k,l-1}=\eta_{a,k,l}+
                 \sum_{b,s\le k}D_{ak,bs,l}H_{b,s,l-1}.       \tag{7}
\]

Each response correction uses the same edge's actual action/adjoint.
Covariances of xi are E[H H] and of eta are E[Delta Delta], in their
respective populations. Distinct oriented source families are independent;
the answers in (7) include the displayed corrections.

With source-time weight h_s omega_b, C.2 constructs finite caps

\[
 |C_{ak,bs,l}|\le c_lh_s\omega_b,\qquad
 \sum_{b,s\le k}|A^{resp}_{ak,bs,l}|\le a_l,
\]
\[
 |F_{ak,bs,l}|\le f_lh_s\omega_b,\quad
 \sum_{b,s\le k}|D_{ak,bs,l}|\le a_l+JT,\qquad
 f_1=1,\ f_l=c_l+J\ (l\ge2).                               \tag{8}
\]

For N(X)=sup_{p>=2}||X||p/sqrt(p), fix constants C>=1,K>=2 from C.2's
elementary derivative inequalities, before choosing any response caps.
They depend only on the bounds just verified and L. The forward-row and
single-reverse-pulse estimates of C.2 are, with d_l=1+a_(l+1) for l<L,
d_L=1, B_H=2K, B_(P,L)=2K and B_(P,l)=4K(1+a_(l+1)),

\[
 \sum|A_l^{resp}|\le
 C(B_{P,l}+d_l)\exp\{Cf_lTd_l+Cf_l^2T^2B_{P,l}^2\},          \tag{9}
\]
\[
 |C_{ak,bs,l}|/(h_s\omega_b)\le
 Cf_{l-1}\exp\{Cf_{l-1}Td_{l-1}
                         +Cf_{l-1}^2T^2B_{P,l-1}^2\}.        \tag{10}
\]

The single pulse starts with h_s omega_b. Subsequent multiplicative growth
is bounded by the exponential of a weighted time sum of individual |P|.
Jensen and marginal N(P)<=B_P give

\[
 E\exp\{\lambda\sum_{s,b}h_s\omega_b|P_{b,s}|\}
       \le(4/3)\exp(2e\lambda^2T^2B_P^2).                  \tag{11}
\]

Thus (9) does not bound a maximum of Gaussian fields. Downward source
differentiation bounds the derivative of the next gate by a sum of a
|P|-term and a bounded response-row term. In (10) the direct pulse appears
only once, before the same weighted Gronwall iteration. These are the
mechanisms that keep constants independent of counts and masses.

Choose caps literally in this order:

\[
 c_2=4C,\quad c_l=4C(c_{l-1}+J)\ (3\le l\le L),
\]
\[
 a_L=4C(2K+1),\quad
 a_l=4C(4K+1)(1+a_{l+1})\ (l=L-1,\ldots,2).                \tag{12}
\]

Now define T_L to be any positive number no greater than T_ball and 1,
satisfying JT_L<=1, 2KT_L<=1, f_l T_L B_(P,l)<=1 for every l, and making
every exponent in (9)–(10) at most log 2. This is a finite explicit list
of linear/quadratic inequalities after the caps are fixed. For example
one can successively halve T_ball until all strict inequalities hold.
All their left sides tend to zero as T_L->0, so this procedure terminates.

At depth three this is specifically c2=4C, c3=4C(c2+J),
a3=4C(2K+1), a2=4C(4K+1)(1+a3), with
B_(P,3)=2K, B_(P,2)=4K(1+a3), B_(P,1)=4K(1+a2).
For every further fixed depth the same finite bottom-up c induction and
top-down a induction applies. No depth-uniform lower bound on T_L is asserted.

The causal order is also essential. At time k, first-row and readout roots
of that step use only earlier histories. Construct current forward layers
from bottom to top: their lower source derivatives use already constructed
lower features and only past backward fields. Then construct current
backward layers from top to bottom: the current upper response is already
known when it is used. Estimates (9)–(10) improve the chosen caps by a
factor two. At k=0 the memory is empty and the top-down step starts with
c0=0. This is an induction over actual instructions, not an implicit
assumption of all future tails.

C.2 consequently gives constants gamma,C0>0 such that

\[
 \sup_{\text{finite laws, meshes}}\sup_{t\le T_L}\max_{a,l}
       E_l e^{\gamma |P_l^h(t,u_a)|^2}\le C_0,
\quad
 \|P_l^h(t,u_a)1_{|P_l^h(t,u_a)|>R}\|_2\le C_0e^{-c_0R^2}.
                                                               \tag{13}
\]

The lemma permits arbitrary positive meshes with bounded total length.
An affine raw-state evaluation is an Euler prefix with one shortened
final step, so (13) holds at each interpolant time with recomputed fields.

**Passive-query extension.** C.2 is stated for positive-weight training
inputs; this does not silently make it a passive-query theorem. To obtain
a bound at any fixed passive u, replace a finite training law nu by
(1-epsilon)nu+epsilon delta_(u,0). At a fixed mesh its finitely many raw
Euler states converge on the common carrier to the original states as
epsilon->0, by the joint field continuity in §4 and finite induction.
The passive backward field also converges in L2. Since (13)'s constants
are independent of the added positive mass, an almost-sure subsequence
and Fatou pass (13) to the original passive field. A finite collection
of passive inputs is handled by splitting epsilon among them. This
proves (13) separately at every passive direction with the same constants;
it does not assert a tail bound for a supremum over directions or time.

## 6. The raw one-reference transport estimate

Take two states on the same initialized carrier in a fixed bounded ball,
and couple (u,y) under mu with (v,z) under nu. Write h=|u-v| and e for
their sum raw distance. Put p_l=||Z_l(u)-bar Z_l(v)||2. If the action,
readout and directional-row norms are at most B, forward induction gives

\[
 p_1\le e+Bh,\qquad p_l\le e+Bp_{l-1},\qquad
 \|H_l-\bar H_l\|_2\le p_l\le C_L(e+h),                    \tag{14}
\]
\[
 |r(u,y)-\bar r(v,z)|\le C_L(e+h)+|y-z|.                   \tag{15}
\]

The row estimate uses ||bar w||dir, while e uses the full-row norm.
For tau_R(Q)=||Q 1_|Q|>R||2,

\[
 \|[\phi'(Z)-\phi'(\bar Z)]\bar P\|_2
            \le2R\|Z-\bar Z\|_2+2\tau_R(\bar P).          \tag{16}
\]

Let b_l=||Delta_l-bar Delta_l||2. At the top,
b_L<=e+2Rp_L+2 tau_R(bar c). At every lower layer,

\[
 b_l\le B b_{l+1}+B^{L-l}e+2Rp_l+2\tau_R(\bar P_l(v)).    \tag{17}
\]

Indeed subtract the action first in P_l, and at its gate use (16) only
on the reference factor. Downward substitution in (17) yields

\[
 b_l\le C_L(1+R)(e+h)
                  +C_L\sum_{j=l}^L\tau_R(\bar P_j(v)).     \tag{18}
\]

There is **one** power of R, at every fixed depth. An already formed
backward error is multiplied only by a bounded action and bounded gate;
a new cutoff term is added, not multiplied into that error.

For each middle block use the exact HS identity and difference estimate

\[
 \|a\otimes b-\bar a\otimes\bar b\|_{HS}
       \le\|a-\bar a\|_2\|b\|_2+\|\bar a\|_2\|b-\bar b\|_2.
                                                               \tag{19}
\]

Expand r Delta_l tensor H_(l-1) by first subtracting r, then Delta_l,
then H_(l-1). For the row block additionally subtract the explicit u
factor; its contribution is bounded by |bar r| ||bar Delta_1||2 h.
The readout block needs only (14)–(15). Integrating the resulting estimates
over the coupling and taking its infimum proves

\[
 \|F_\mu(\theta)-F_\nu(\bar\theta)\|_{sum}
 \le C_L(1+R)\{e+W_1(\mu,\nu)\}
          +C_L\sum_{l=1}^L\int\tau_R(\bar P_l(v))\,d\nu.  \tag{20}
\]

It holds identically for the normalized finite arrays with ordinary
Frobenius increments. Only the reference requires tails. No smallest
mass, Gram inverse, or bound on a maximum of data-indexed fields occurs.
For a bounded competitor on a larger ball the same proof holds with a
larger finite C_L. The cutoff still has one power.

## 7. Completion, energy, uniqueness, law continuity and restart

For finite laws nu_i and meshes of maximal step h_i, construct their
Euler paths on the common carrier. A preceding state is within V_L h_i
of its interpolant. Equations (13),(20) and scalar Gronwall give

\[
 \sup_{t\le T_L}e(\theta_i^{h_i}(t),\theta_j^{h_j}(t))
 \le C e^{C(1+R)T_L}
       \big[(1+R)\{W_1(\nu_i,\nu_j)+h_i+h_j\}+e^{-cR^2}\big].
                                                               \tag{21}
\]

Every Borel law on the compact data space has finite approximations in
W1: partition into finitely many Borel cells of diameter <=1/i and move
their exact masses to representatives. No zero-boundary or density
assumption is needed. At fixed R, (21) makes any corresponding h_i->0
sequence Cauchy up to C exp(CRT_L-cR²); then R->infinity removes that
remainder. Completeness of C([0,T_L];E_d) gives a limit theta_mu independent
of the sequence. Joint field/law continuity from §4 passes the Euler
integral equations to

\[
 \theta_\mu(t)=\theta_0+\int_0^t F_\mu(\theta_\mu(s))\,ds.  \tag{22}
\]

Convergence of the integrands is uniform in time: a contrary sequence of
times has a convergent subsequence, and uniform state convergence plus
joint continuity contradicts the discrepancy. Thus theta_mu is strong C1
in the **raw HS** space. At every fixed (t,u), backward continuity and
Fatou transfer (13), using the passive extension, to this solution.
In particular its law-integrated individual tails are <=C exp(-cR²),
uniformly in t. These are not supremum-of-path tails.

III.F.9's curve chain rule applied successively to the forward layers,
and the action product rule, give the gradient blocks in (2). Equivalently
III.F.10's scalar gradient proof applies at this fixed L. The gradients
are jointly continuous in (t,u), bounded on the compact domain and raw
Bochner integrable. Differentiating the loss and substituting (22) yields

\[
 \mathcal L_\mu(t)+\int_0^t\|\theta_\mu'(s)\|_{raw}^2ds
                    =\int y^2\,d\mu\le1.                  \tag{23}
\]

The scalar chain rule used here can also be checked from the remainder
bound at a fixed reverse weight Q:
M||q||2²+2||Q 1_|Q|>M||2 ||q||2=o(||q||2), first q->0 then M->infinity.
This avoids a false Frechet derivative of the activation as an L2-valued map.
Equation (23) implies ||c(t)||infinity<=2t by its bounded readout integrand
and Cauchy–Schwarz in the training law. This extra bound is not needed for
the comparison proof.

Any competing continuous strong raw solution on the compact interval has
finite component and action bounds. Apply (20) with it as the first state
and the constructed solution as reference, using that finite larger ball.
With the same law and initial state, Gronwall bounds the distance by
C exp(CRT_L-cR²) for every R. Letting R->infinity proves uniqueness,
without tails or differentiability assumptions on the competitor.

For two constructed laws, (20) proves (21) with mesh terms absent.
For 0<q<=1 choose R=K0 sqrt(log(e/q)), where cK0²>=2 and K0>=1.
Then exp(-cR²)<=q² and the remaining factors give (1). For q>1 a common
state-increment bound suffices. Equations (14)–(15) give uniform forward
and prediction continuity. The compact-input bounded-multiplier proof
then gives all other asserted observation continuity.

At a reached time s, the restriction of (22) gives existence of a
continuation. The same one-reference estimate on [s,T_L] gives uniqueness
from that state. More intrinsically, close the current full-row/readout
fields under current actions, their adjoints and coordinate operations.
Euler steps from this state, including Bochner law integrals approximated
by finite sums, stay on these generated spaces. Comparing them against
the existing continuation in (20) gives
C exp(CRT_L)[(1+R)h+exp(-cR²)]. Send h->0 then R->infinity.
Consequently continuation is generated by the current state; no response
history or new initialization is an input. Equal current generated joint
action laws identify this construction by the canonical L2 isometry.
This proves same-law reached-state restart, not arbitrary-state or
switched-law well-posedness.

## 8. The actual finite GF/GD bridge

At any fixed width, a Borel-law loss gives a smooth finite-dimensional
vector field on bounded parameter sets. Differentiation under the law
integral is permitted by compact input support and bounded derivatives
on each such set. Picard iteration on a sufficiently short bounded
parameter ball gives local GF existence/uniqueness. Its energy identity
in (3) bounds displacement by sqrt(t L_n(0)), and increments near a finite
endpoint by sqrt(|t-s| L_n(0)). Therefore a finite terminal state exists
and local existence extends it. Finite GF is globally defined. Raw GD is
its actual simultaneous Euler update, with no truncation or modified
optimizer. On [0,T_L] both algorithms obey §4's high-probability ball.

Fix a finite reference law nu=sum_b omega_b delta_(u_b,y_b) and a finite
proof mesh h **before** taking width to infinity. Expand every population
Euler action into A_l,0 plus its accumulated ranks. Realize this finite
program on the same first/middle arrays as the actual network, freezing
only its deterministic population residuals and contractions. Call its
nodes H^o,Delta^o. Define proxy parameters at its grid times by

\[
 \bar w_{n,k}=w_{n,0}-2\sum_{s<k,b}h_s\omega_b r_{b,s}
                                        \Delta^o_{1,b,s}u_b^T,
\]
\[
 \bar A_{l,n,k}=A_{l,n,0}-\frac2n\sum_{s<k,b}h_s\omega_b r_{b,s}
                         \Delta^o_{l,b,s}(H^o_{l-1,b,s})^T,
\]
\[
 \bar c_{n,k}=c_{n,0}-2\sum_{s<k,b}h_s\omega_b r_{b,s}H^o_{L,b,s}.
                                                               \tag{24}
\]

The assigned nodes use zero population readout; the actual finite readout
is retained additively in (24). Thus actual and proxy initial arrays agree
exactly. Its normalized RMS tends to zero because E||c_n,0||²/n=n^-2.
No readout maximum bound is required.

III.F.1–5 and A.1–2 identify every fixed same-layer tuple and contraction
in this fixed graph. All hypotheses were checked in §5. Applying a proxy
action to an oracle field produces only finite sums of errors of the form

\[
 -2h_s\omega_b r_{b,s}\Delta^o_{l,b,s}
 \left\{\frac{(H^o_{l-1,b,s})^T H^o_{l-1,a,k}}n
                   -E[H_{l-1,b,s}H_{l-1,a,k}]\right\}.       \tag{25}
\]

Transpose discrepancies have the corresponding delta contractions.
Each scalar bracket tends to zero and its multiplying RMS is bounded in
probability. Forward induction therefore identifies recomputed proxy
features. Starting with the readout, downward induction identifies
recomputed backward fields: subtract the field error first, and use (16)
on the fixed oracle factor in the remaining gate error. At a fixed cutoff
the node errors vanish; continuous cutoff second moments converge; then
the cutoff is removed. This is a finite-depth induction, valid separately
on its finite grid. The first-row update is exact on the whole row, not
just on the active projections. Its row error is bounded by the same
finite weighted sums because |u_b|=1.

By (19), the recomputed proxy velocity defect in **sum raw norm** is
o_P(1), uniformly over its fixed grid. Reference empirical tails satisfy

\[
 \max_k\sum_{b,l}\omega_b
   \frac{\|\bar P_{l,b,k}1_{|\bar P_{l,b,k}|>R}\|_2}{\sqrt n}
       \le C e^{-cR^2}+o_P(1).                              \tag{26}
\]

To justify a tail without a discontinuous-test claim, use
||v 1_|v|>R||<=2||v-p||+2||p 1_|p|>R/2|| and dominate the latter by
a continuous positive-part cutoff at R/4. Its limiting second moment is
controlled by (13). There are finitely many reference nodes at fixed
(nu,h), and no actual-dataset maximum is used.

Proxy raw bounds follow also from the finite-rank metric identity

\[
 \left\|\sum_i a_i\otimes b_i\right\|_{HS}^2
       =\sum_{i,j}\langle a_i,a_j\rangle\langle b_i,b_j\rangle.\tag{27}
\]

For the finite rank matrices a_i b_i^T/n the same expression with
normalized pairings is their **ordinary Frobenius** squared norm.
Fixed-program second moments pass these finite sums to their limits.
Together with their summed rank velocity bounds this places all proxies
in a fixed enlarged ball and bounds assigned interpolation speeds,
with probability tending to one at each fixed (nu,h). Constants can be
chosen independent of nu,h.

Let lambda_j->mu, n_j->infinity and eta_j->0. Use the same-width finite
version of (20) to compare actual GD to (24). At time t their preceding
states differ from their interpolants by at most C(eta_j+h). Include the
proxy velocity defect and (26), then integrate Gronwall. For each fixed
R,nu,h the result is

\[
 \sup_{t\le T_L} e_{n_j}(\theta^{GD}_{j}(t),\bar\theta^{\nu,h}_{n_j}(t))
 \le C e^{C(1+R)T_L}
    \left[(1+R)\{\eta_j+h+W_1(\lambda_j,\nu)\}
                          +e^{-cR^2}+o_P(1)\right].         \tag{28}
\]

Here e_n uses ||row difference||F/sqrt(n), the sum of middle **Frobenius**
differences, and ||readout difference||2/sqrt(n). GF satisfies (28) with
eta_j=0. Borel actual laws are allowed, because (20) integrates directly
against them; only the fixed reference law is finite.

The limit order is: width (and the stipulated eta_j/data-law limits) at
fixed nu,h,R; h->0; nu->mu through finite laws; R->infinity. Equivalently,
for a desired error first choose R to make the amplified Gaussian tail
small, then choose a finite nu close to mu and h small, then take j large.
The fixed-program theorem is never applied to a transcript growing with
width. This proves every eta_j->0 with no eta_j sqrt(n_j) condition and
no relation between atom count and width.

## 9. Observations, paths, kernels and sampling

Forward fields are Lipschitz in raw state and input on the balls, by
(14). Their time-Lipschitz RMS bounds follow from bounded raw speeds and
the forward recursion. At fixed proof mesh, append any fixed finite list
of time/input evaluations to the oracle, evaluating the **affine raw
state** at interior times. The fixed-program limits and (25) identify
these nodes. Finite input/time nets, followed by their deterministic
Lipschitz bounds, give whole-sphere uniform prediction convergence of
the proxy to its population Euler interpolant. Combining (28),(21)
gives the asserted uniform prediction limit for actual GF and GD.

The admitted observation class is exactly finite correctly typed graphs
formed from roots, current/initial forward fields, actions and actual
adjoints, linear combinations, Lipschitz coordinate maps and products of
a bounded continuous factor with a named L2 field. No unrestricted product
of two unbounded factors is included. One proves their stability by graph
induction. Actions amplify RMS differences by a bounded norm plus the
HS increment error times the reference input norm. A bounded-factor
product uses the truncation argument of §4 on its fixed reference factor.
For a compact (t,u) set, the limiting L2 reference fields form a compact
set. Finite nets make their L2 tails uniformly small: choose a finite L2
net, truncate its finite members, and use
||v 1_|v|>2R||2<=2||v-v_i||2+2||v_i 1_|v_i|>R||2.
On the clipped factors the relevant coordinate maps are uniformly
continuous on compact boxes. Fixed-program cutoff moments on a finite
net transfer this estimate to the finite proxies. Induction, refining
the net only after its fixed-program width limit, gives uniform-time
same-layer tuple W2 convergence and all continuous quadratic-growth
measurements. This is an observation comparison outside the Gronwall
estimate; no exponential tail is required for a derived probe.

For paired activations retain time zero and time t in the **same** tuple
at each layer. The equal-index coupling bounds the W2 distance of any
two same-width tuple laws by their tuple RMS discrepancy. Oracle joint
second moments supply their limiting tuple law. This proves initial/current
paired W2 convergence, uniformly in time and fixed query input, and after
training-law averaging. In particular

\[
 J_l(t;\mu)=\int E_l|H_l(t,u)-H_l(0,u)|^2\,d\mu
\]

is the uniform-time limit of its finite counterpart. Its integrand is
bounded by four and uniformly Lipschitz in u; its change under an actual-to-
proxy comparison is <=C e_n. Hence the law-averaged assertion follows
directly also from (28), a finite input net, and transport of lambda_j.
RMS motion is sqrt(J_l), so its convergence follows from continuity of
the square root, without dividing by a possibly vanishing displacement.

For a fixed finite dataset the true kernel blocks are

\[
 K^1_{ab}=(u_a\cdot u_b)E[\Delta_{1,a}\Delta_{1,b}],\quad
 K^l_{ab}=E[H_{l-1,a}H_{l-1,b}]E[\Delta_{l,a}\Delta_{l,b}],
\quad K^{L+1}_{ab}=E[H_{L,a}H_{L,b}].                        \tag{29}
\]

They converge uniformly in time by the backward RMS comparison and
Cauchy–Schwarz. Their sum is the raw gradient Gram, giving f'=-2K Omega r
and L'=-4(Omega r)^T K(Omega r). All block mobilities here equal one.

To recover C.1's speed and path observations, first use (20),(28) against
the fixed reference to compare raw assigned velocities. The same ordered
limits make their raw discrepancy tend to zero, uniformly away from the
irrelevant choice of grid-point derivative. Strong curve chain rules give

\[
 \dot Z_1=\dot w\cdot u,\qquad
 \dot Z_l=\dot A_l H_{l-1}
              +A_l[\phi'(Z_{l-1})\dot Z_{l-1}],\qquad
 \dot H_l=\phi'(Z_l)\dot Z_l.                              \tag{30}
\]

For raw GD these identities hold almost everywhere along its affine
parameter interpolation with the assigned raw velocities. Every norm in
(30) is bounded by a fixed depth-dependent multiple of the raw speed;
therefore integral squared coordinate speeds are uniformly bounded.
The exact population velocities in (30) form a compact L2 family as t
varies, by the strong multiplier continuity proof. Fixed-mesh oracle
evaluations of (30) are fixed finite programs. Their cutoff second
moments converge; truncating the compact reference factors, then applying
raw-state/velocity convergence in (30), proves convergence of the
integrated squared hidden speeds. These cutoffs occur after stability,
so uniform integrability, rather than a Gaussian derivative-tail bound,
is sufficient.

Finally, on a time cell of length epsilon each absolutely continuous
coordinate satisfies

\[
 \sup_{s,t\text{ in cell}}|z(t)-z(s)|^2
                 \le\epsilon\int_{cell}|\dot z(v)|^2dv.   \tag{31}
\]

Average over neurons (or the population), then sum over cells. The squared
uniform-path error from a grid reconstruction is <=C epsilon. At the
finite grid, joint same-layer W2 convergence holds by the preceding
oracle and state comparisons. Let width increase first and then epsilon
decrease. This proves W2 convergence of joint input preactivation and
activation paths for the uniform path norm. No same-neuron identification
between different hidden populations has entered any argument.

On the common balls the squared-loss integrand is uniformly bounded and
uniformly Lipschitz in (u,y), since predictions are uniformly bounded and
input-Lipschitz. Uniform prediction convergence and W1(lambda_j,mu)->0
therefore imply uniform-time convergence of both the training risk under
lambda_j and the population risk under mu to L_mu(t).

For iid samples independent of initialization, empirical laws tend to mu
in W1 in probability. To see this with arbitrary Borel mu, partition the
compact data space into finitely many cells of diameter epsilon and move
both laws to their representatives. Each move costs <=epsilon. The
remaining finite discrete transport is bounded by half the data diameter
times the sum of absolute cell-mass errors; every cell frequency has
variance <=1/(4m). First m->infinity, then epsilon->0. The only other
events in (28) concern the fixed reference program and the initialized
arrays. A union bound with the data-distance event proves the simultaneous
sample/width/GD limit, without any relative growth restriction.

## 10. Claim ladder and hostile checks

| Claim | Status in this candidate | Evidence/limitation |
|---|---|---|
| Exact full-row, HS, forward/adjoint equations | Proved | (2)–(3), same action labels and rank identity |
| Uniform local raw population existence | Proved | Weighted finite-depth tails, (20)–(22), HS completeness |
| All-Borel law continuity and same-law reached restart | Proved | (1), one-reference uniqueness, generated-current-state Euler comparison |
| Actual finite GF and every vanishing-step raw GD capture | Proved locally | Fixed reference (24)–(28), no growing-program invocation |
| Whole-input, paired, joint-second-moment and fixed-data path observations | Proved locally | §9, compact-reference cutoffs, (30)–(31) |
| Strict paired motion and nonaffinity at every layer | Not addressed | Existence or a positive kernel does not imply hidden motion |
| Determining finite hierarchy and actual finite numerical realization | Not addressed | A countable carrier is not a finite scalar array |
| Substantial training, positive supported neighborhood and global reference conclusions | Not addressed | T_L is an onset interval only |

The strongest local structural objections are addressed at their actual
failure points: HS is used in every rank comparison; cutoff accumulation
is linear in R at each fixed depth; C.2 is applied only after its preliminary
bounds and source hypotheses are checked; its passive extension is proved
by positive-mass approximation; fixed Gaussian programs are fixed before
width limits; the finite random readout is retained additively; and no
ambient L2 local-Lipschitz assertion or trained independent-Gaussian-call
replacement occurs. The source constants may deteriorate arbitrarily with
fixed depth. No tail or stability statement here supplies any of the
remaining activity, closure, implementation or substantial-training clauses.
