# Random inputs and the moving bad basin

Frozen scoped theory route, 2026-09-18. Status: complete candidate proof,
not independently checked or promoted. This route used only the supervisor's
assignment, `docs/observable_p1.md`, and the complete own-study files
`BASIN_RESULTS.md`, `basin_probability_route.md`,
`basin_hilbert_null_extension.md`, `dependent_basin_functional.md`,
`INPUT_PERTURBATION_RESULTS.md`, and `input_perturb_frozen.md`.
Required instructions and the investigate-conjectures and
solve-math-rigorously skills, including research-contract, evidence-ledger,
and adversarial-audit references, were read. No other study, README,
current parallel route, external scientific source, or experiment was used.
This is the only file written. All arguments below were completed before
comparison with parallel routes.

## 1. Result and contract

Random inputs can replace random initial states in a basin-null theorem
**if the canonical data-to-trajectory section is transverse to a joint
parameter/state trapping graph**. This is an additional hypothesis about
the actual initialized trajectory. A complete sufficient test is proved
below, including the motion of the equilibrium and basin. For the exact
p=1 flow, the finite-time input sensitivity exists and obeys an explicit
linear inhomogeneous equation. Joint trapping graphs can also be
constructed at every equilibrium with the individual lower-coefficient
cancellation and a finite-rank strict-saddle Hessian.

The user's premise is that at the special base datum the canonical
trajectory **does converge to the specified bad equilibrium**. This is
assumed throughout the connection-breaking question; proving that premise
is not this route's task. What is not established is the needed nonzero
transverse derivative of this given connection under changed inputs.
In particular, the first-order frozen-state input calculation in
`input_perturb_frozen.md` does not verify it. Section 3 gives the precise
local escape conclusion if that derivative is verified.

The logical inference from thin state basins to thin bad-data sets is
false even for a real-analytic finite-dimensional square-loss gradient
family. Section 7 gives an explicit example with all of the following:

* Every bad equilibrium is a strict saddle with a codimension-one basin.
* Changing the parameter makes each old equilibrium nonstationary.
* The parameter derivative of the vector field at the old equilibrium
  is nonzero and lies entirely in its unstable state direction.
* One fixed initialization follows a nonstationary trajectory to a
  moving positive-loss saddle for every parameter in an open interval.
* Zero loss is attainable, the initial loss is one, and the bad limit
  loss is one half.

This is a counterexample to an inference, **not a p=1 counterexample**.
It proves that even the stronger unstable-forcing check omits necessary
motion terms.

For the p=1 application keep dimension three, exact correlated Gaussian
marks, ridge 1/4096, tanh, all three trainable blocks, the full matrix and
its actual transpose, the odd sector, physical L2/L2/Frobenius gradient
metric, and the unhalved weighted square loss. Labels and positive
probability weights are fixed. Inputs vary on a local chart of
`(S^2)^m`, with physical inputs `sqrt(3) u_i`. For seven inputs the chart
dimension is fourteen. All population expectations are exact; no particle,
network-width, closure-order, or time-discretization limit is substituted.

Write the common physical state space and canonical initialization as

\[
\mathcal H=L^2_{\rm odd}(\Omega_1;\mathbb R^3)
 \oplus L^2_{\rm odd}(\Omega_2)\oplus\mathbb R^{3\times6},
\qquad \theta=(v,c,M),\quad w=g+v,
\qquad \theta_{\rm can}=(0,0,D).
\tag{1}
\]

In these fixed-carrier coordinates the canonical state is independent of
the inputs. This does not assert rotational covariance of the dictionary.
Let `a` denote data-chart coordinates in an open subset `A` of `R^q`, and
let `Phi_t^a` be the exact flow. The sharp event under discussion is

\[
E_{\rm bad}=\{a\in A:\Phi_t^a(\theta_{\rm can})\to e
 \text{ in }\mathcal H\text{ for some bad equilibrium }e\}.
\tag{2}
\]

Nullity means Lebesgue nullity in data charts, equivalently zero local
product sphere area, and hence probability zero under every input law
absolutely continuous with respect to that area. A prescribed singular
noise law requires its own support analysis. Event (2) concerns a point
limit. Positive limiting loss without point convergence remains a
separate question.

## 2. A data-space theorem with the correct countability

The following theorem is stated for a separable real Banach state space
`H`; the physical space (1) is a special case. Assume the finite-time
canonical sections

\[
S_n(a)=(a,\Phi_n^a(\theta_{\rm can}(a)))\in\mathbb R^q\times H,
\qquad n=0,1,2,\ldots
\tag{3}
\]

are C1 on their open existence domains. The initialization may depend
on data in this abstract statement. In (1) it does not.

Let `S` be any set of bad equilibrium pairs `(a,e)`. Suppose every point
of `S` has a product-phase-space neighborhood `U` with a Lipschitz graph
of positive codimension containing the starting point of **every orbit
of the extended flow**

\[
\dot a=0,\qquad \dot\theta=F(a,\theta)
\tag{4}
\]

that remains in `U` for all positive time. The graph must trap tails
converging to any equilibrium in the neighborhood, not only its center.

Then there are countably many such neighborhoods `U_j` and scalar
Lipschitz hypersurfaces

\[
\Gamma_j=\{z:\ell_j z=h_j(P_jz)\},\qquad
P_j=I-e_j\ell_j,\quad\ell_j(e_j)=1,
\tag{5}
\]

with `h_j` Lipschitz on the hyperplane `ker ell_j`, such that every
trajectory in (2) has a late integer-time section in a corresponding
`Gamma_j`, with its entire remaining tail trapped in `U_j`.
Translations of a graph are absorbed in `h_j`. Let `L_j` be its
Lipschitz constant.

**Data-section theorem.** Suppose that for every datum in (2), at least
one such trapping pair `j,n` and a data direction `b in R^q` satisfy

\[
|\ell_j DS_n(a)b|>L_j\|P_j DS_n(a)b\|.
\tag{6}
\]

Then (2) is contained in a Borel Lebesgue-null subset of `A`. It therefore
has outer probability zero for every absolutely continuous data law.
The condition need only hold at one trapping representation of each
bad trajectory. It is sufficient, but stronger than necessary, to check
it at every point of every `S_n^{-1}(Gamma_j)`.

**Proof of the countable selection.** The product `R^q x H` is second
countable. Around each equilibrium pair choose a smaller open
neighborhood whose closure lies in its trapping neighborhood. From this
cover of `S` select a countable subcover: for every element of a countable
basis contained in one cover member, select one such member. Every point
of `S` lies in a selected member. If an extended trajectory converges to
`(a,e)`, choose a selected smaller neighborhood containing that pair.
Convergence places its entire sufficiently late tail in the associated
larger neighborhood. Some integer-time state lies on that graph.

To pass from positive codimension to (5), write a graph as
`y+g(y)` for a bounded direct sum `Y+U`, where `U` is nonzero. Select
`e in U` and `ell` vanishing on `Y` with `ell(e)=1`. Deleting the
`e` coordinate preserves the `Y` coordinate, so `ell(g(y))` is a
Lipschitz scalar function of the deleted-coordinate point on its
projected domain. If its Lipschitz constant is `L`, extend it by
`h(z)=inf_d[h(d)+L||z-d||]`. The Lipschitz inequality makes this
extension finite, Lipschitz, and equal to the original on its domain.
Its graph is a closed scalar hypersurface containing the original graph.

**Proof of nullity.** At a point satisfying (6), replace `b` by `-b`
if necessary. Continuity of `DS_n` gives a small data cylinder
`a=a_0+y+tb`, where `y` lies in a complement of `R b`, and constants
`alpha,beta` such that throughout that cylinder

\[
\ell_j DS_n(a)b\ge\alpha>0,\qquad
\|P_jDS_n(a)b\|\le\beta,\qquad
\delta:=\alpha-L_j\beta>0.
\tag{7}
\]

Define the continuous scalar function
`Q(y,t)=ell_j S_n(a)-h_j(P_j S_n(a))`. Integration of the C1 section
along the `b` direction and the Lipschitz bound for `h_j` give

\[
Q(y,t)-Q(y,s)\ge\delta(t-s)\qquad(t>s).
\tag{8}
\]

There is at most one zero on every line with fixed `y`. Its zero set
in the cylinder is Borel, because `Q` is continuous, and Fubini gives
zero q-dimensional Lebesgue measure. Equivalently, local Lipschitzness
of `S_n` bounds the variation in `y`; comparing two zeros through their
cross point gives a Lipschitz graph over a subset of a `(q-1)`-dimensional
hyperplane. For `q=1`, the local zero set has at most one point.

The data cylinders surrounding the points where a given `j,n` works
have a countable subcover, by second countability of `A`. There are only
countably many `j,n`. The union of their Borel zero sets is the required
null hull. No measurability of the selected endpoints or the event (2)
is needed. This proves the theorem.

The countable objects are **trapping neighborhoods and their graphs**.
The endpoints themselves may be uncountable. Neither taking the union
of the point basins over only a countable dense set of endpoints nor
taking an arbitrary uncountable union of null point basins proves this
theorem. Moreover, separate fiberwise graph covers for each fixed datum
do not supply the required countable joint cover without a parameter
regularity argument.

## 3. The smooth test and the motion terms

If a relevant joint graph has a C1 scalar defining function `Q_j(a,x)`
with a nonzero state derivative, then (6) can be replaced by the weaker
and exact regular-zero test

\[
D_aQ_j(a,x_n)b+D_xQ_j(a,x_n)Z_b(n)\ne0,
\quad x_n=\Phi_n^a(\theta_{\rm can}(a)),
\quad Z_b(t)=D_a\Phi_t^a(\theta_{\rm can}(a))b.
\tag{9}
\]

Here `Z_b` includes differentiation of the initialization. To prove the
claim, the left side is the directional derivative of the scalar C1
function `a -> Q_j(a,x_n(a))`. A nonzero derivative remains one-signed
on a sufficiently small cylinder, so the same one-root/Fubini proof
applies. For a vector-valued graph equation it suffices that one fixed
scalar component have nonzero derivative. Surjectivity onto the entire
unstable space is a stronger codimension statement, unnecessary for
mere nullity and impossible if its dimension exceeds `q`.

For clarity, suppose there is a C1 equilibrium branch `e(a)` and a
local graph over a fixed complementary state splitting, expressed as

\[
P_u(x-e(a))=h(a,P_{cs}(x-e(a))).
\tag{10}
\]

The splitting is fixed in this chart; its change with the parameter is
represented inside `h`. At a point on this graph put
`xi=P_cs(x-e(a))`. The derivative of its vector equation along the
canonical section is

\[
P_u[Z_b-e'(a)b]-D_ah(a,\xi)b
 -D_\xi h(a,\xi)P_{cs}[Z_b-e'(a)b].
\tag{11}
\]

Any scalar component with nonzero value yields (9). The three missing
ingredients in a frozen-basin calculation are the equilibrium motion,
the graph's explicit parameter dependence, and the graph slope acting
on the center-stable part of the trajectory sensitivity. Using moving
projections instead introduces their derivatives as well; it cannot
eliminate these terms.

At the central equilibrium in a chart tangent to the center-stable
spectral subspace, `h(a,0)=0`, `D_ah(a,0)=0`, and
`D_xi h(a,0)=0` at the central parameter. Formula (11) then reduces to
`P_u(Z_b-e'b)`. If `A=D_xF(a,e(a))` and `B=D_aF(a,e(a))`, equilibrium
differentiation gives

\[
A e'(a)b+B b=0,
\qquad P_ue'(a)b=-A_u^{-1}P_uB b.
\tag{12}
\]

Thus even there the relevant expression is
`P_u Z_b+A_u^{-1}P_uB b`, not `B b` or `P_uB b` alone. Away from the
equilibrium all terms in (11) return. The counterexample in Section 7
makes the cancellation exact at every finite time.

Analyticity, when available for the actual composed scalar constraint,
offers a different sufficient test: a real-analytic function on a
connected open data domain which is not identically zero has a null zero
set. Here is the needed proof. At each zero some finite-order derivative
is nonzero; otherwise its analytic power series vanishes on a
neighborhood, and continuation through overlapping balls in the
connected domain makes the function identically zero. If the least such
order is `k>=1`, choose a multi-index `alpha` of order `k` and a
coordinate `j` with `alpha_j>0`. The derivative indexed by
`alpha-e_j` vanishes at that point and has nonzero `j` derivative.
The original zero point therefore lies in a regular zero hypersurface
of one derivative of the function. Countably many derivatives and
countably many local cylinders cover all original zeros, proving
nullity by (8). This observation does not show that basin equations are
analytic, and it still requires ruling out identically zero pullbacks.
The example below has identically zero analytic pullbacks.

### Breaking a given base connection

Assume, as the user stipulates, that at `a_0` the canonical trajectory
converges to the selected bad endpoint. Suppose this endpoint pair has
a joint trapping chart `U,G`, and choose an integer `n` so the entire
base tail from n onward lies in `U`. Suppose a C1 scalar graph equation
`Q(a,x)=0` contains `G` and its pullback

\[
q(a)=Q(a,\Phi_n^a(\theta_{\rm can}))
\quad\text{satisfies}\quad Dq(a_0)\ne0.
\tag{12a}
\]

The base point has `q(a_0)=0`. For each direction `b` outside the
proper hyperplane `ker Dq(a_0)` and each C1 data curve
`a(epsilon)=a_0+epsilon b+o(epsilon)`,

\[
q(a(\epsilon))=\epsilon Dq(a_0)b+o(\epsilon)\ne0
\tag{12b}
\]

for every sufficiently small nonzero amplitude, with a
direction-dependent threshold. Continuity ensures its time-n state is
still inside `U`. Since it is off the trapping graph, its subsequent
trajectory must leave `U` at a finite time. This is a proved generic
small-noise local escape result for the **given connection**, conditional
only on the stated graph and derivative hypotheses. The excluded
direction hyperplane is Lebesgue null. The same C1 regular-zero argument
also shows that almost every perturbed datum in one sufficiently small
data neighborhood has this finite-exit property.

Finite exit is weaker than exclusion of every subsequent positive-loss
endpoint. An excursion followed by reentry, or convergence to another
bad state, is not ruled out by this one time-n graph test. Excluding
all bad endpoint convergence uses the all-hit countable statement in
Section 2, or a separate no-return or basin-exclusion argument. Conversely,
if no unstable trapping graph exists at the base endpoint, (12a) cannot
be assumed merely because that endpoint is stationary. The PSD p=1
endpoints therefore need additional analysis even under the given base
connection premise. The analytic family in Section 7 satisfies that
premise at every base datum yet (12a) fails identically, so assuming the
whole base connection does not by itself remove the obstruction.

## 4. Exact p=1 input sensitivity

Use a C2 local input chart `a -> (u_i(a))`. Fix weights and labels and
write, with `phi=tanh`,

\[
q_i=w\cdot u_i,\quad A_i=E_1[b_1\phi(q_i)],\quad
z_i=MA_i,\quad s_i=b_2\cdot z_i,\quad H_i=\phi(s_i),
\]
\[
f_i=E_2[cH_i],\quad\rho_i=\mu_i(f_i-y_i),\quad
d_i=E_2[b_2c\phi'(s_i)],\quad T_i=\rho_iM^Td_i.
\tag{13}
\]

The exact vector field is

\[
F_v=-2\sum_i\phi'(q_i)(b_1\cdot T_i)u_i,
\quad F_c=-2\sum_i\rho_iH_i,
\quad F_M=-2\sum_i\rho_i d_iA_i^T.
\tag{14}
\]

For a combined state direction `(zeta,chi,N)` and data direction `b`,
put `xi_i=D_a u_i(a)b`. Every first variation is given by

\[
\delta q_i=\zeta\cdot u_i+w\cdot\xi_i,
\qquad \delta A_i=E_1[b_1\phi'(q_i)\delta q_i],
\]
\[
\delta z_i=NA_i+M\delta A_i,\qquad
\delta H_i=\phi'(s_i)(b_2\cdot\delta z_i),
\]
\[
\delta f_i=E_2[\chi H_i+c\delta H_i],\qquad
\delta\rho_i=\mu_i\delta f_i,
\]
\[
\delta d_i=E_2[b_2\chi\phi'(s_i)
 +b_2c\phi''(s_i)(b_2\cdot\delta z_i)],
\]
\[
\delta T_i=(\delta\rho_i)M^Td_i+
 \rho_iN^Td_i+\rho_iM^T\delta d_i.
\tag{15}
\]

Consequently

\[
\begin{split}
\delta F_v=-2\sum_i\{&\phi''(q_i)\delta q_i(b_1\cdot T_i)u_i
 +\phi'(q_i)(b_1\cdot\delta T_i)u_i\\
 &+\phi'(q_i)(b_1\cdot T_i)\xi_i\},
\end{split}
\]
\[
\delta F_c=-2\sum_i[(\delta\rho_i)H_i+\rho_i\delta H_i],
\]
\[
\delta F_M=-2\sum_i[(\delta\rho_i)d_iA_i^T
 +\rho_i(\delta d_i)A_i^T+\rho_i d_i(\delta A_i)^T].
\tag{16}
\]

Setting the data direction to zero gives `D_theta F`; setting the
state direction to zero gives `D_a F`. The canonical sensitivity is the
unique solution of

\[
\dot Z_b(t)=D_\theta F(a,\theta(t))Z_b(t)
              +D_aF(a,\theta(t))b,\qquad Z_b(0)=0.
\tag{17}
\]

For a data-dependent initialization the initial value is instead
`D_a theta_can(a)b`. If `U(t,s)` is the bounded linear state evolution
along the reference finite trajectory, then

\[
Z_b(t)=U(t,0)Z_b(0)
       +\int_0^t U(t,s)D_aF(a,\theta(s))b\,ds.
\tag{18}
\]

This is the response along the whole trajectory. It generally cannot
be replaced by the frozen field derivative at its proposed endpoint.

### Verification of finite-time differentiability

All formulas above are valid on the physical Hilbert space (1), without
requiring bounded lower fields. On bounded product-chart/state sets,
`||w||_2` is bounded. The map `(a,v)->q_i=(g+v).u_i(a)` is locally
Lipschitz into L2. Its directional derivative is the first line of (15).
Bounded first and second derivatives of tanh, bounded marks, and
Cauchy--Schwarz make every finite moment locally Lipschitz. This proves
local Lipschitzness of the extended field (4).

For a fixed product direction, the lower gate difference quotient
converges in L2 to `phi''(q_i)delta q_i`. Scalar differentiation and
the bound `||phi''||_infty |delta q_i|` prove this by dominated
convergence; the vanishing cross term from varying both `v` and `u`
is bounded in L2 by a constant times the parameter increment. This
justifies (16) as the norm Gateaux derivative. Its operator norm is
locally bounded because `delta q_i` has L2 norm bounded by a constant
times the product direction norm and all other operations are bounded
finite-vector maps or integrable pairings.

This derivative is continuous on every fixed product direction.
For the only delicate multiplier, if `q_k->q` and `r_k->r` in L2,

\[
\|\phi''(q_k)r_k-\phi''(q)r\|_2
\le\|\phi''\|_\infty\|r_k-r\|_2
 +\|[\phi''(q_k)-\phi''(q)]r\|_2\to0.
\tag{19}
\]

For the last term, truncate to `|r|<=R`, use the L2 convergence of
the gates there, and use bounded gates with the L2 tail of `r` on
the complement. All finite moments in (15) are continuous by the same
bounds. Thus the derivative is strongly continuous and locally bounded.

For completeness, these properties suffice for differentiating a finite
flow segment. Difference quotients of its integral equation are uniformly
bounded by the local Lipschitz constant and Gronwall. Subtract the solution
of the linear variational equation. The remaining forcing error is a
derivative difference tested on that fixed linear solution. Strong
continuity plus local operator bounds gives joint continuity of derivative
evaluation on state and direction. The linear solution has compact image
on a finite interval, so that forcing error tends uniformly to zero.
Gronwall then gives uniform convergence of the difference quotients to
the linear solution. The same argument at nearby parameters proves
continuity of each derivative column. Since the parameter domain is
finite dimensional, continuity of finitely many columns is operator-norm
continuity for the parameter derivative. Thus `a->theta(t,a)` and (3)
are genuinely C1. No Frechet C1 claim about the field on a full Hilbert
neighborhood is used.

### What the initial first-order response actually controls

At the canonical state, `c=0`, `rho_i=-mu_i y_i`, and `d_i=T_i=0`.
Put `A_i^0=E_1[b_1 phi(g.u_i)]` and `s_i^0=b_2.DA_i^0`. Then

\[
F_v(0)=F_M(0)=0,\qquad
F_c(0)=2\sum_i\mu_i y_i\phi(s_i^0),
\tag{20}
\]

and for a data direction

\[
\delta A_i^0=E_1[b_1\phi'(g\cdot u_i)(g\cdot\xi_i)],
\]
\[
D_aF_v(0)b=D_aF_M(0)b=0,
\qquad
D_aF_c(0)b=2\sum_i\mu_i y_i\phi'(s_i^0)
                      (b_2\cdot D\delta A_i^0).
\tag{21}
\]

These exact formulas show the first response starts in the readout block.
They do not prove that its propagated image crosses any given moving
trapping graph. At time `n`, the graph test uses the full vector
`DS_n b=(b,Z_b(n))`, not only (21). A fourteen-dimensional input law
cannot produce a full-support Gaussian state law on (1); finite-dimensional
transversality is the relevant replacement, not state-law absolute
continuity.

## 5. Joint p=1 trapping graphs where strict saddles are verified

The joint trapping hypothesis of Section 2 can itself be proved at a
p=1 equilibrium pair `(a_*,theta_*)` satisfying

\[
T_i(a_*,\theta_*)=0\quad\text{for every }i,
\qquad A_*:=D_\theta F(a_*,\theta_*)
\text{ is self-adjoint, finite rank, with a positive eigenvalue}.
\tag{22}
\]

These are explicit hypotheses. The assigned basin sources verify them
for independent triples at bad losses in `(0,1)`, and for the bounded
lower-displacement classes with at most one independent input relation
described in `dependent_basin_functional.md`. The full-Hilbert local
seven-input strict-saddle theorem in Section 10 of
`input_perturb_frozen.md` also verifies them at the equilibria to which
that theorem applies. They are not verified for every seven-input bad
equilibrium; the robust PSD states in `INPUT_PERTURBATION_RESULTS.md`
do not have the required positive flow eigenvalue.

Here is a direct joint graph proof, so a smooth equilibrium branch is
not an extra assumption. The finite lower moment map `A_i(a,v)` is
locally C1,1 jointly in the finite parameter and the L2 displacement.
For its `v` derivative use the L2 Lipschitz gate estimate. Its parameter
derivative pairs `b_1 phi'(q_i)w` with a bounded chart derivative;
subtract two such expressions and bound the changed gate times `w`
by Cauchy--Schwarz and the changed `w` directly in L2. Both derivative
differences are bounded by a constant times the product-space distance.
The finite upper operations and their pairings with `c` preserve this
regularity. Thus `T_i,F_c,F_M` are locally C1,1 jointly.

Let `G_i(a,v)t=phi'(q_i)(b_1.t)u_i`. It is a locally Lipschitz map
to bounded operators from `R^6` to lower L2. At (22), subtraction of
`G_i T_i` from its joint linearization has the form

\[
[G_i(a,v)-G_i(a_*,v_*)]T_i(a,\theta)
 +G_i(a_*,v_*)[T_i(a,\theta)-DT_i(a_*,\theta_*)\delta],
\tag{23}
\]

where `delta=(a-a_*,theta-theta_*)`. On a radius-r product ball the
first product has two O(r) factors with bounded Lipschitz constants;
the last bracket has Lipschitz constant O(r) by C1,1 regularity. Hence
the full extended field has the exact local form

\[
\dot\lambda=0,\qquad
\dot x=A_*x+B_*\lambda+R(\lambda,x),
\quad \operatorname{Lip}(R\text{ on }B_r)\le C r,
\quad R(0)=0,
\tag{24}
\]

with `lambda=a-a_*`, `x=theta-theta_*`, and `B_*=D_aF(a_*,theta_*)`.
This proves the requisite Frechet derivative at the pair even though
the field need not be Frechet C1 on its Hilbert neighborhood.

Let `P_u,P_cs` be the orthogonal positive and nonpositive spectral
projections of `A_*`. Its finite-dimensional unstable restriction
`A_u` has smallest eigenvalue `nu>0`. Make the invertible linear change

\[
z_u=P_ux+A_u^{-1}P_uB_*\lambda,
\qquad z_{cs}=(\lambda,P_{cs}x).
\tag{25}
\]

The linear equations are now `z_u'=A_u z_u` and
`z_cs'=C z_cs`, where

\[
C(\lambda,y)=(0,A_{cs}y+P_{cs}B_*\lambda).
\tag{26}
\]

Because `||exp(t A_cs)||<=1`, the explicit integral formula for (26)
gives `||exp(t C)||<=K_0(1+t)`. For every `epsilon>0` it is therefore
at most `K_epsilon exp(epsilon t)`. Also
`||exp(-t A_u)||<=exp(-nu t)`. Nilpotent parameter-to-center coupling
has been retained; no diagonalizability of the full extended operator
is assumed.

After this bounded coordinate change the nonlinear remainder still has
local Lipschitz constant O(r). Compose it with the radial retraction
onto the radius-r ball, a 2-Lipschitz map. This makes a globally
Lipschitz remainder `N`, with Lipschitz constant `L` as small as desired,
and agrees with the original field on the ball. Take
`epsilon=nu/4`, `gamma=nu/2`. For each base coordinate `eta`, solve

\[
z_{cs}(t)=e^{tC}\eta+
 \int_0^t e^{(t-s)C}N_{cs}(z(s))\,ds,
\]
\[
z_u(t)=-\int_t^\infty e^{(t-s)A_u}N_u(z(s))\,ds.
\tag{27}
\]

On continuous paths with norm `sup_(t>=0) exp(-gamma t)||z(t)||`,
the integral operator has Lipschitz constant at most

\[
L\left[\frac{K_\epsilon}{\gamma-\epsilon}
       +\frac{1}{\nu-\gamma}\right].
\tag{28}
\]

Choose r to make (28) less than one. Successive iteration is a
contraction on the complete path space and gives one solution for each
`eta`, Lipschitz in `eta`. Define `h(eta)=z_u(0)`. This is a closed
Lipschitz graph with positive finite codimension. Any original orbit
trapped in the ball is bounded, satisfies the modified equation, and
obeys (27): its unstable variation-of-constants terminal term vanishes
as the terminal time tends to infinity. Uniqueness in the weighted
path space places it on the graph. This proves the joint trapping
hypothesis at (22), for all equilibria in the neighborhood.

Equation (25) is already an explicit correction for moving basins. At
the linearized level its unstable data response is

\[
P_u Z_b(n)+A_u^{-1}P_uB_* b.
\tag{29}
\]

The nonlinear graph in (27) supplies the remaining slope terms. Formula
(29) by itself is not the full finite-time test. Parameter variation is
a center direction of the extended dynamical system, not an independent
unstable random state direction.

Combining this section with Section 2 gives a proved conditional p=1
data-null theorem for canonical trajectories converging to endpoints
of class (22), **provided the section test (6) or (9) is verified**.
No assumption that equilibrium points themselves are countable is
needed. Endpoints lacking an unstable eigenvalue require another local
basin analysis before even this conditional route applies.

## 6. What the existing p=1 perturbation calculations imply

The frozen-state derivative in `input_perturb_frozen.md` proves that a
generic tangent input direction moves the old equilibrium off the zero
set of the field. Its rank-three linear condition, the stronger exact
fixed-state codimension, and its local full-state strict-saddle theorem
concern stationarity and state curvature. None computes `Z_b(n)` along
the canonical trajectory or the derivative of its joint basin equation.

Even in a nearby region where all surviving equilibria are strict saddles,
Section 5 supplies graphs but not (6). The available first-order control
therefore verifies regularity and graph existence under their exact
hypotheses, but **does not verify data-space transversality**. The robust
remote PSD states additionally prevent treating all seven-input bad
endpoints by strict-saddle graphs.

The concrete missing quantity for any proposed strict-saddle endpoint
chart is (9), or its Lipschitz-cone version (6), with `Z_b` computed from
(17). A p=1 theorem would need to show that at each canonical bad hit
some allowed input direction makes this quantity nonzero, or use a
different proved mechanism excluding such hits. Neither a nonzero
`D_aF(a,e)b`, a nonzero unstable projection of that vector, the existence
of some transverse state direction, nor absolute continuity of the
input noise is a substitute.

This route does not establish a canonical failure or a positive-measure
p=1 bad-data set. Conversely it does not establish its nullity. The
canonical data-null conjecture remains open after the exact conditional
theorem and counterexample below.

## 7. An analytic square-loss family defeating the inference

Let a scalar data parameter `a` vary in any open interval. In state
space `R^2` define orthonormal vectors

\[
n(a)=(\cos a,\sin a),\qquad
s(a)=(-\sin a,\cos a),
\quad n'(a)=s(a),\quad s'(a)=-n(a).
\tag{30}
\]

Use the two observations `f_1(a,z)=(n(a).z)^2` and
`f_2(a,z)=s(a).z`, labels `y_1=y_2=1`, equal weights one half, and
the Euclidean negative-gradient flow of their unhalved weighted loss

\[
L_a(z)=\frac12[(n(a)\cdot z)^2-1]^2
             +\frac12[s(a)\cdot z-1]^2.
\tag{31}
\]

This loss is jointly real analytic. Put `x=n(a).z`, `y=s(a).z`.
At a fixed parameter the exact flow is

\[
\dot x=2x(1-x^2),\qquad \dot y=1-y.
\tag{32}
\]

The positive-loss equilibrium is `e(a)=s(a)`, with `x=0,y=1`, loss
one half, and Hessian

\[
D_z^2L_a(e(a))=-2n(a)n(a)^T+s(a)s(a)^T.
\tag{33}
\]

It is a strict saddle. The other two equilibria `s(a)+n(a)` and
`s(a)-n(a)` have exactly zero loss, so the positive loss is not an
architectural minimum.

The full basin of convergence to `e(a)` is the line

\[
B_a=\{z:n(a)\cdot z=0\}.
\tag{34}
\]

Indeed x=0 is invariant, and then y tends to one. If x is initially
nonzero, uniqueness keeps its sign. For `0<|x|<1` its magnitude
increases, and for `|x|>1` it decreases, with a limit equal to one:
a hypothetical limit strictly between zero and one, or strictly larger
than one, would have a nonzero right-hand side in (32), contradicting
convergence. The invariant barriers at magnitude one also give global
existence; y is explicitly global. Thus x cannot tend to zero from a
nonzero initial value, proving (34). Each basin is a closed smooth
codimension-one set and is Lebesgue null in the state space.

Now prescribe the same fixed initialization for every datum,
`z_can=0`. Equation (32) gives the exact nonstationary trajectory

\[
z(t,a)=(1-e^{-t})s(a),\qquad
L_a(z(t,a))=\frac12(1+e^{-2t})\longrightarrow\frac12.
\tag{35}
\]

The loss starts at one and strictly decreases, with
`dL/dt=-exp(-2t)=-||z'||^2`. Nevertheless every parameter in the
open interval belongs to the bad-data event. Randomizing a with any
density supported there gives bad convergence with probability one.

This remains true despite a nonzero unstable frozen input forcing.
For `F=-grad L`, differentiation at the old equilibrium, holding the
state `e(a)` fixed while differentiating the parameter, gives

\[
B(a):=D_aF(a,e(a))=2n(a),\qquad
A(a):=D_zF(a,e(a))=2n(a)n(a)^T-s(a)s(a)^T.
\tag{36}
\]

Thus B is entirely unstable and nonzero. In particular the old point
is nonstationary for every sufficiently small nonzero parameter change:
its field equals the nonzero first-order term plus a smaller remainder.
Its equilibrium branch moves with `e'(a)=-n(a)`, and indeed
`A(a)e'(a)+B(a)=0`.

The actual joint basin equation is the analytic function
`Q(a,z)=n(a).z`. The trajectory sensitivity is
`Z(t,a)=-(1-exp(-t))n(a)`. At every finite time its full derivative is

\[
D_aQ(a,z(t,a))+D_zQ(a,z(t,a))Z(t,a)
 =(1-e^{-t})-(1-e^{-t})=0.
\tag{37}
\]

Consequently the canonical section lies in the moving joint basin
identically. The elementary toy family refutes, simultaneously, the
following abstract implications: ambient null basin implies null
pullback; destruction of each fixed old equilibrium implies avoidance
of moving endpoints; nonzero unstable parameter forcing implies
transversality; analyticity alone rules out a positive-measure bad-data
set. No statement about canonical p=1 failure follows from this family.

## 8. Claim ledger and remaining obligation

| Statement | Status and exact scope |
|---|---|
| Countable joint trapping charts plus transverse canonical sections give a null bad-data set | Proved here, Sections 2--3 |
| Equilibrium families must consist of countably many points | Not required; countability concerns joint trapping neighborhoods |
| Finite-time p=1 input sensitivity is C1 and solves (17) | Proved here from the exact physical equations, Section 4 |
| Joint p=1 trapping graphs exist at coefficient-cancelled finite-rank strict saddles | Proved here under (22), Section 5 |
| Existing frozen p=1 input derivatives verify the canonical section test | Not established; they differentiate a different object |
| A nonzero unstable frozen input forcing suffices for that test | False for analytic square-loss families, equations (35)--(37) |
| Input noise makes canonical p=1 convergence to all bad endpoints a null event | Open; actual trajectory transversality and the PSD endpoint classes remain uncontrolled |
| Nullity of point-convergent bad endpoints would exclude every positive-loss asymptote | Not established; no-limit and escape cases remain separate |

The strongest new p=1 result here is a fully specified conditional
data-null theorem with verified finite-time sensitivity and local joint
graph construction. Its non-vacuous missing hypothesis is the explicit
parameter-to-basin-coordinate test. The analytic example shows why that
hypothesis cannot be inferred from the available state-space or frozen
endpoint statements. No experiments were run, and no result in this file
has yet received an independent check.

## 9. Informed check of the lead's unbounded-response result

This section was added after Sections 1--8 were frozen with SHA256
`5660303f944fb0f637a3e2d3d5ca1f034e351252f32f711d536ed0c49a160ae6`.
The supervisor then supplied the lead's proposed mechanism and authorized
reading the complete `input_connection_response.md`. The checked source
had SHA256
`1f5eba17cbab7a6b5093b3f231d7915e9d06e3c2e9fc427baad0f3a069669426`.
Every scientific line of that source was read, including its regularity
argument and limitations. This is an informed mathematical check, not an
independent rediscovery or a promotion review. The frozen preceding
portion is unchanged. No computation or additional source was used.

**Verdict.** The conditional theorem is valid: given the stipulated
strong Hilbert convergence of the canonical base trajectory to the
specified single-amplitude seven-input bad state, every input direction
with `Delta!=0` has an unbounded-in-time first response. The result does
not prove finite-noise exit or eventual fitting. One compact-cover step
in the lead's finite-horizon differentiability argument benefits from
the explicit fixed-direction continuity verification below.

### 9.1 Endpoint and linearization check

Retain the lead's notation `H=phi(z b_(2,1))`,
`J=b_(2,1)phi'(z b_(2,1))`, and `z=kappa phi(aC)>0`. The single-amplitude
lower field makes every effective upper feature equal H. The scalar
readout conditions give prediction `m=-1/7` and first upper backward
coordinate zero. Each remaining backward coordinate is zero because
its centered canonical upper coordinate is independent of `b_(2,1)`.
Thus every full backward vector vanishes. The equal angular first and
second moments of the triangle and square give
`sum rho_i=0`, `sum rho_i u_i=0`, and `sum rho_i u_i u_i^T=0`.

For arbitrary physical state variations, the first effective-vector
variation is affine in `u_i`; the first prediction variation is only
`<k,H>`. Every residual term in the second prediction variation is
affine or quadratic in `u_i`, except the second effective-vector
variation, whose coefficient is the zero backward vector. The three
residual moment equalities therefore cancel all residual Hessian terms.
The actual loss Hessian and flow linearization are

\[
D^2L[(h,k,N)]^2=2\langle k,H\rangle^2,
\qquad A_*(h,k,N)=(0,-2H\langle k,H\rangle,0).
\tag{38}
\]

Actual Hilbert differentiability, rather than only a directional
calculation, follows from the vanishing individual lower coefficients
`T_i=rho_i M^T d_i=0` and the product remainder estimate (23). This
applies even though `w_*-g` need not be essentially bounded. The
physical Hilbert formulation requires only its square integrability.

### 9.2 Finite-time response and endpoint operator convergence

The equations (15)--(16) provide bounded linear norm Gateaux derivatives
on the extended parameter/state Hilbert space. The needed stronger
statement is continuity on every fixed direction. At fixed inputs the
only problematic term is multiplication of a fixed L2 direction by a
changing bounded gate; (19) proves strong continuity by truncation. For
an input direction the multiplying L2 function is `w.xi`; it changes
continuously in L2 when w changes in L2, and the same estimate applies.
Finite upper operations and their pairings with c are continuous.
Consequently derivative evaluation `(state,direction)->DF(state)direction`
is jointly continuous, by local operator bounds. This is the precise
hypothesis justifying the finite compact covering and Gronwall argument
in the lead's Section 3. It verifies the finite-time first variation
and its equation, with zero initial variation.

For operator-norm convergence at the specified endpoint, decompose the
lower state derivative into its multiplier

\[
h\longmapsto-2\sum_i\phi''(q_i)(h\cdot u_i)
                         (b_1\cdot T_i)u_i
\tag{39}
\]

and the finite-rank term `-2 sum G_i DT_i`. The multiplier norm is at
most a constant times `max_i |T_i|`; these coefficients tend to zero
under strong base convergence because `d_(i,*)=0`. The factors `G_i`
converge in operator norm from their finite-dimensional domain to L2,
by L2 convergence of the gates. The finite moment maps `T_i` are C1,1
at fixed inputs, so `DT_i` converges in operator norm. The upper and
matrix field derivatives also converge in operator norm by their
finite-vector smoothness and L2 pairings. Thus

\[
\|A(t)-A_*\|_{\rm op}\to0.
\tag{40}
\]

The data derivatives converge strongly as well. Their direct lower
terms involve bounded gates times `w(t).xi`; subtract `w(t)-w_*`
and apply the fixed-L2 truncation argument to the remaining multiplier.
All other terms are continuous finite moments. Thus `B(t)->B_*` in H.
No uniform-in-time parameter differentiability and no exchange of
the parameter derivative with the infinite-time limit are assumed.

### 9.3 Neutral forcing and its exact consequence

In the lead's physical-input convention `u_i=x_i/sqrt(3)`, the tangent
variation is `delta u_i=xi_i/sqrt(3)` and
`Delta=sum rho_i xi_(i,1)/sqrt(3)`. At the reference state the input
prediction derivative vanishes because `d_i=0`; hence `delta rho_i=0`.
Direct differentiation gives

\[
(B_*)_c=-2a\kappa\phi'(aC)\Delta J.
\tag{41}
\]

There is no missing factor of sqrt(3), two, or one seventh: all are
accounted for respectively in Delta, the unhalved loss, and rho_i.
Let `k=J-proj_(span H)J` and `K=(0,k,0)`. The source's Taylor
coefficient comparison proves `k!=0` for every `z>0`. Therefore

\[
A_*K=0,\qquad
\langle K,B_*\rangle
 =-2a\kappa\phi'(aC)\Delta\|k\|_2^2\ne0.
\tag{42}
\]

If the solution of `Z'=A(t)Z+B(t)` were globally bounded, (40)--(42)
would imply
`d<K,Z(t)>/dt -> <K,B_*> !=0`. Its scalar projection would then
be unbounded, a contradiction. This proves only
`sup_(t>=0)||Z(t)||=infinity`; it does not assert a growth rate or
that its norm tends monotonically to infinity. Nonzero Delta holds
outside one proper hyperplane of the tangent space, exactly as proved
in the source. No exceptional-amplitude exclusion from the older local
strict-saddle argument enters this proof.

A bound `||theta_epsilon(t)-theta_0(t)||<=C|epsilon|` valid for all
time and all sufficiently small amplitudes would bound every fixed-time
derivative by C, contradicting this conclusion. This is the exact
all-time consequence. Finite-time differentiability supplies no uniform
Taylor remainder on a horizon tending to infinity as the amplitude
vanishes, so the source correctly stops before fixed-amplitude escape.

There is also a direct endpoint-motion corollary. A differentiable
equilibrium branch through this endpoint in a direction with nonzero
Delta would satisfy `A_*e'+B_*=0`. Pairing with K contradicts (42).
Thus a C1 equilibrium continuation in that direction is impossible.
This leaves nonsmooth branches and nearby remote equilibria available;
it does not replace a finite-noise escape theorem.

The lead result strengthens the concrete p=1 information beyond the
frozen Sections 1--8: under the user's given base-connection hypothesis,
one can prove generic unbounded first response at these particular PSD
endpoints. The earlier missing finite-noise transversality/escape step
remains. The two results have different conclusions and are compatible.
