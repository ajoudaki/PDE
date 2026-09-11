# Actual finite-GF data derivatives and their population identification

Author component: `/root/capture`. This file proves the finite-width
identification bridge. Its probability input is the actual-reference weighted
source theorem in `WEIGHTED_SOURCE.md`, not a higher-moment assertion inferred
from the fixed-program theorem. The linear equation is stated explicitly below
so that the bridge can be checked independently of the all-time argument in
`PROPAGATOR.md`. This is an author candidate pending the complete paired review.

## 1. Model, tangent equation, and precise claim

Write `u=x/sqrt(2)`, `phi=tanh`, and use the full first row `w=(w_1,w_2)`.
The model, mean squared loss, stored-weight mobilities `(n,1,n)`, independent
Gaussian initial variances `(1,1/n,1/n^2)`, and actual finite readout are those
of the research contract. The reference has weights `p_1=p_2=1/2`, inputs
`e_1,e_2`, labels `y_1=1,y_2=-1`. The finite reference is its actual GF.
In particular it need not have the population exchange symmetry.

On the canonical spaces `H_i=L2(Omega_i)` put

\[
 \mathcal H=L^2(\Omega_1;\mathbb R^2)
       \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
 \qquad \|v\|_{\mathcal H}^2=\|\xi\|_2^2+\|B\|_{HS}^2+\|d\|_2^2.
 \tag{F1}
\]

For finite arrays `v_n=(xi_n,B_n,d_n)` the corresponding norm is

\[
 \|v_n\|_{\mathcal H_n}^2
   ={\|\xi_n\|_F^2\over n}+\|B_n\|_F^2+{\|d_n\|_2^2\over n}.
 \tag{F2}
\]

The same symbol `B_n` here denotes a tangent matrix, not the reference
matrix. An initialized action has no HS assertion; both its learned increment
and its tangent have the indicated HS norm. A rank action has representative
`ab^T/n`, whose ordinary Frobenius norm is the product of the two RMS norms.

At the reference let

\[
 X_a=F(w_a)-F(g_a),\quad F(z)=z/2+\sinh(2z)/4,
 \quad D_a=\phi'(w_a),\quad w_a=j(X_a,g_a),
 \tag{F3}
\]

where `j_X=phi'(j)`. For a tangent `v=(xi,B,d)` define, at each passive `u`,

\[
\begin{aligned}
 \dot z_v^1(u)&=\sum_a u_aD_a\xi_a,&
 \dot h_v^1(u)&=\phi'(w\cdot u)\dot z_v^1(u),\\
 \dot z_v^2(u)&=B H^1(u)+A\dot h_v^1(u),&
 \dot h_v^2(u)&=\phi'(Z^2(u))\dot z_v^2(u),\\
 e_u(v)&=\langle d,H^2(u)\rangle+\langle c,\dot h_v^2(u)\rangle,\\
 \dot\delta_v^2(u)&=d\phi'(Z^2(u))
                     +c\phi''(Z^2(u))\dot z_v^2(u),&
 \dot Q_v(u)&=B^*\delta^2(u)+A^*\dot\delta_v^2(u).
\end{aligned}                                                     \tag{F4}
\]

Dots carrying a subscript `v` in (F4) mean directional variations, not
physical-time derivatives. All products have the displayed layer type.
Both `A` and `A*` are used literally. For training input `e_a` put

\[
 s_a=(\mathbf e_a Q_a,\delta_a^2\otimes H_a^1,H_a^2),
\quad
 Ds_a[v]=(\mathbf e_a\dot Q_v(e_a),
       \dot\delta_v^2(e_a)\otimes H_a^1
                +\delta_a^2\otimes\dot h_v^1(e_a),
       \dot h_v^2(e_a)),
 \tag{F5}
\]

where `bold e_a Q_a` means a two-component first-row field with only
component `a` nonzero. Define

\[
 G(t)v=-2\sum_{a=1}^2p_a
          \{e_{e_a}(v)s_a+r_a Ds_a[v]\},                         \tag{F6}
\]

and, for a finite signed measure `sigma` on `S1 x [-Y,Y]`,

\[
\begin{split}
 q(t,u,y)&=\left(
   (u_a\cosh^2w_a\,\phi'(w\cdot u)Q(u))_{a=1,2},
      \delta^2(u)\otimes H^1(u),H^2(u)\right),\\
 b_\sigma(t)&=-2\int (f(t,u)-y)q(t,u,y)\,d\sigma(u,y).
\end{split}                                                       \tag{F7}
\]

The symbol `q` does not actually depend on `y`; retaining `y` in its
argument makes the data integral's type explicit. The forced equation is

\[
 v_\sigma'(t)=G(t)v_\sigma(t)+b_\sigma(t),\qquad v_\sigma(0)=0.
 \tag{F8}
\]

The source theorem verifies that (F7) is a Bochner integral in (F1), uniformly
bounded on every compact time interval by a constant times total variation.
The generator is bounded and strongly continuous there. Directly from (F4),
if `||A||op, ||c||2, ||c||infinity` and the two residuals are bounded, then
`||G||op<=C`, independently of the carrier. For example

\[
 \|\dot h_v^1(e_a)\|_2\le\|\xi_a\|_2,\quad
 \|\dot z_v^2(e_a)\|_2\le\|B\|_{HS}+\|A\|_{op}\|\xi_a\|_2,
\]
\[
 \|\dot\delta_v^2(e_a)\|_2
 \le\|d\|_2+2\|c\|_\infty\|\dot z_v^2(e_a)\|_2,
\quad
 \|\dot Q_v(e_a)\|_2
 \le\|B\|_{HS}\|c\|_2+\|A\|_{op}\|\dot\delta_v^2(e_a)\|_2.
 \tag{F9}
\]

The other factors in (F5) have bounded L2 norms, and `e_u` is bounded by
`C||v||` uniformly in `u`. These estimates apply also at finite width.
Successive substitution of (F8)'s integral equation converges: its `k`th
iterated homogeneous integral has norm at most `(CT)^k/k!`. The same bound
on differences proves uniqueness. Thus no ambient Frechet differential of
an L2-valued Nemytskii field is an assumption of (F8).

**Finite-capture theorem.** For every fixed deterministic probability law
`nu` on the stated data space and every fixed `T<infinity`, let
`sigma=nu-nu_*`. Differentiate the finite exactly integrated GF along
`mu_epsilon=(1-epsilon)nu_*+epsilon nu` from the right at zero, using the
same initialized arrays. Then

\[
 \sup_{0\le t\le T,\ u\in S^1}
 \left|\left.\partial_{\epsilon+}f_{n,\mu_\epsilon}(t,\sqrt2u)
                    \right|_{\epsilon=0}-e_u(v_\sigma(t))\right|
       \longrightarrow0\quad\hbox{in probability}.                \tag{F10}
\]

This includes `T=40`. Section 5 gives the state/action topology supporting
this assertion. Constants used in estimates depend on the reference, `T`
and `Y`, and not on a support cardinality, a minimum weight or a Gram
eigenvalue. The convergence assertion fixes `nu` before taking width to
infinity; it is not a probability supremum over all laws.

## 2. Finite differentiation precedes every width limit

For fixed `n`, the loss integrated against any such Borel probability law
is a smooth finite-dimensional function of its three parameter arrays.
Indeed on a compact parameter set every derivative of the integrand is
continuous and bounded uniformly in `(u,y)`; differentiation of its integral
is justified by the bound on the difference quotient from the scalar mean
value formula. The vector field depends affinely on `epsilon`.

The finite raw energy identity, with squared increment norm
`||dw||F^2/n+||dA||F^2+||dc||2^2/n`, bounds the parameter displacement on
`[0,T]` by `sqrt(T L_n(0))`. Initial losses are uniformly bounded for
`epsilon in [0,1]`, at this fixed initialized network. The resulting compact
finite-dimensional parameter ball excludes finite-time escape. Local smooth
ODE construction and continuation therefore give all these finite flows.
For a nonatomic law this is GF of the exactly integrated loss, not an
empirical training algorithm.

Here is the parameter differentiation argument without invoking a
population law-to-flow map. Subtract the two finite integral equations.
On the preceding compact ball the derivative of the vector field is
bounded, so the scalar integral inequality gives
`sup_t||theta_epsilon-theta_0||<=C_n,T epsilon`.
Divide the subtracted equation by `epsilon`. The exact mean value formula
expresses its first term using the derivative of the reference vector
field on the line between these two paths; those coefficients converge
uniformly in time to their values at `theta_0`. The direct change of the
law is its signed integral against `sigma`. Subtract the claimed limiting
linear integral equation and use the same integral inequality. This proves
uniform-in-time convergence of the difference quotients, hence the right
derivative. All these arguments are at fixed width; their constants may
depend on `n` and are not used in the width passage.

For every finite coordinate `phi'(w_a)>0`, so differentiate the exact
coordinate change (F3). It gives

\[
 \delta w_a=D_a\xi_a.
 \tag{F11}
\]

For an arbitrary law the transformed first velocity is exactly
`-2 integral r u_a phi'(w.u)Q(u)/phi'(w_a) dmu`. At `nu_*` the only
nonzero contribution to row `a` has `u=e_a`; the two gates cancel
identically, before differentiating. Its homogeneous differential is
therefore `-2p_a[e_a(v)Q_a+r_a dot Q_v(e_a)]`. The direct law derivative
is precisely the first block of (F7). The middle and readout equations
differentiate to the other blocks of (F6)-(F7). This verifies every sign,
training weight and factor 2 in (F8). At time zero all array derivatives
vanish, since initialization is identical for all `epsilon`.

The finite output derivative is the scalar pairing (F4), with normalized
finite pairings. Thus (F8) at finite width is the actual derivative already
constructed, by uniqueness of its finite linear equation. The finite
Gaussian readout is present in every coefficient and forcing field.

After this construction, (F7)-(F8) define a linear extension to all finite
signed zero-mass directions. The extension agrees with the finite right
derivative for each probability-law path above. No assertion that arbitrary
signed directions admit a two-sided probability neighborhood is used.

## 3. Exact probability input and removal of data quadrature

Here is the specific statement consumed from `WEIGHTED_SOURCE.md`. Put

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,
        \|c_{0,n}\|_\infty\le1,\|g_n\|_F/\sqrt n\le2\}.
 \tag{F12}
\]

It has probability tending to one. On it the actual reference, its clock
state and its velocities have deterministic compact-time RMS/action bounds,
and `||c_n(t)||infinity<=C_T`. If

\[
 Q^\#_{n,i}=\sup_{t\le T,u\in S^1}|Q_{n,i}(t,u)|,
 \quad X^\#_{n,ia}=\sup_{t\le T}|X_{n,ia}(t)|,
 \quad W^\#_{n,ia}=\cosh^2g_{n,ia}+2X^\#_{n,ia},
\]

then for every finite `p>=2` the source theorem gives finite constants
independent of width such that

\[
 E\left[1_{E_n}{1\over n}\sum_i
 \left\{(Q^\#_{n,i})^p+
       \sum_a(W^\#_{n,ia}Q^\#_{n,i})^p+
       (\sup_{t\le T}|w_{n,i}(t)|Q^\#_{n,i})^p\right\}\right]
 \le C_{p,T}.
 \tag{F13}
\]

The exact envelope `cosh^2 w_a(t)<=W^#_a` is part of that argument.
The analogous population bounds, on the canonical reference, are also
proved there. Only fixed finite moments and their uniform integrability
are used below. No Gaussian tail bound for input derivatives is asserted.

To check the measure approximation explicitly, let `chi_R(q)` be clipping
to `[-R,R]`, and let `rho_R(w)=min(cosh^2 w,R)`. In the first component
of (F7), replace `cosh^2 w_a Q(u)` by `rho_R(w_a)chi_R(Q(u))`; leave the
other two components unchanged. Call the resulting integrand `q_R` and
forcing `b_sigma,R`. On the compact-time state bounds, `q_R` times the
residual is globally Lipschitz in the data variable with a constant
`C_T,Y,R`, and is Lipschitz in the same-root clock/HS/readout distance.
For completeness, `rho_R` is bounded by `R` and Lipschitz with constant
at most `2R`; `chi_R` is bounded by `R` and 1-Lipschitz. Forward
differences obey

\[
 \|Z^1(u)-Z^1(v)\|_2\le\|w\|_2|u-v|,\qquad
 \|Z^2(u)-Z^2(v)\|_2\le\|A\|_{op}\|w\|_2|u-v|,
\]

and reverse differences obey the same type of bound because `c` is
bounded pointwise. Adding and subtracting the bounded factors in `q_R`
proves the asserted Lipschitz bounds. The middle rank difference has
the identical estimate in HS norm.

The clipping error tends to zero uniformly in `t,u` in probability at
finite width, in the following ordered sense:

\[
 \lim_{R\to\infty}\limsup_{n\to\infty}
 \Pr\{1_{E_n}\sup_{t\le T,u}\|q_n(t,u)-q_{n,R}(t,u)\|_{
                    \mathcal H_n}>a\}=0\quad(a>0).
 \tag{F14}
\]

Indeed the first-block difference is bounded pointwise by
`2 W^#_a Q^# [1_{W^#_a>R}+1_{Q^#>R}]`. Its empirical squared norm has
expectation tending to zero by (F13) and Holder, or by the higher-moment
tail bound `|V|^2 1_{|V|>M}<=|V|^p/M^(p-2)` after splitting the two
factors. The individual moments of `W^#` follow from its envelope and
the `X^#` moment statement in the source theorem. Sum over the two
coordinates and apply Markov. The population version is identical.
Consequently this clipping error also bounds the forcing error by
`2(C_T+Y)||sigma||TV` times its supremum.

Partition the compact data space into finitely many Borel cells of diameter
at most `delta`, and transfer `nu`'s mass in each cell to one point of that
cell. The resulting deterministic finite law `nu^delta` satisfies
`W1(nu,nu^delta)<=delta` and has the same mass. Coupling within the cells
and using the preceding Lipschitz estimate gives

\[
 \sup_{t\le T}\|b_{\nu-\nu_*,R}(t)
               -b_{\nu^\delta-\nu_*,R}(t)\|\le C_{T,Y,R}\delta.
 \tag{F15}
\]

The same bound holds on `E_n`. First choose `R` for (F14), then choose
`delta` for (F15). This proves the required forcing approximation by a
fixed finite list of bounded coordinate instructions and passive queries.
It does not assert total-variation convergence of the quadrature laws.
Constants do not involve the number or weights of the quadrature atoms.

These arguments also prove strong continuity and Bochner measurability
of the uncut forcing: the clipped integrands are continuous on the compact
time/data space into `mathcal H`, and converge uniformly there by the
population version of (F14). Their range is separable, and the uniform norm
bound makes integration against every finite signed measure legitimate.

## 4. Strong multiplier consistency and fixed-program identification

The only finite-program result used is special-data III.F.1-7, with the
contained value extension global-nonlinear A.1. A fixed finite list of
continuous coordinate instructions of at most linear growth, applications
of the same initial action and its transpose, and causal scalar contractions
has joint empirical same-layer `W2` convergence in probability. The metric
for a finite node tuple is its ordinary Euclidean metric. Singular query
Grams are admitted by III.F.5, whose proof adds fresh query noise at a
fixed program, takes the width limit, and then removes that noise. This
does not require a Gram inverse limit. The source-response extension A.2
is needed in the separate source proof, not as an extra assertion that
finite differentiated trajectories already converge.

We record the product principle used twice below. If arrays `z_n,z_n^h`
on the same indices differ by at most `a_h+o_P(1)` in RMS, `a_h->0`,
and `V_n^h` is a fixed-program node with a second-moment limit, then for
bounded Lipschitz `b`, at fixed cutoff `M`,

\[
 {\|[b(z_n)-b(z_n^h)]V_n^h\|_2\over\sqrt n}
 \le \operatorname{Lip}(b)M
          {\|z_n-z_n^h\|_2\over\sqrt n}
       +2\|b\|_\infty
          {\|V_n^h1_{|V_n^h|>M}\|_2\over\sqrt n}.
 \tag{F16}
\]

For a vector-valued bounded multiplier the identical argument applies.
Continuous positive-part cutoffs transfer the tail in (F16) through the
fixed-program W2 limit. For a compact family in population L2, these
tail norms tend to zero uniformly: approximate the compact family by a
finite L2 net and use
`||V1_{|V|>2M}||2<=2||V-W||2+2||W1_{|W|>M}||2`.
For a merely bounded continuous scalar multiplier, first restrict its
arguments to a compact interval; the same argument uses uniform continuity
there. All multipliers below can instead be taken globally Lipschitz.

Let `theta_n^h` be transformed Euler for the reference on a fixed mesh
of maximum step `h`. It starts from the actual finite readout.
The complete B.1 same-root proof applies with `kappa_a=1/2`, and with
HS distance replacing action distance: a rank difference obeys the same
inequality in HS, while the action of a HS difference is bounded by its
HS norm. It gives, on `E_n`, for sufficiently small `h`,

\[
 \sup_{t\le T}\|\theta_n(t)-\theta_n^h(t)\|_{\rm clock,HS,L2}
        \le C_T h.                                             \tag{F17}
\]

Here and below reference-state distance includes its two clocks and the
learned matrix increment. Its readout supremum is bounded separately.
The population reference has the identical Euler estimate. In particular
the full first row is recovered, not only a projection on a new input.

At fixed `R,delta,h`, build tangent Euler along these reference mesh
states, using (F6) and the clipped forcing for `nu^delta-nu_*` at the
preceding node. Expand each learned reference or tangent matrix as its
finite sum of rank-one updates. Every new matrix query then uses the
initialized matrix in its actual orientation plus finitely many scalar
contractions. Every coordinate instruction is continuous with at most
linear growth. For example `phi'(j(X,g))^2 xi` has a bounded multiplying
factor, while `c phi''(Z2) dot z2` has bounded `c` after clipping outside
the already proved readout bound. The clipping of `c` changes no values.
Each `rho_R(w)chi_R(Q)` is bounded. There is no uncut product of two
independent unbounded varying tangent arguments.

The fixed-program theorem therefore identifies the joint deterministic
population mesh law and all its quadratic contractions. Causal empirical
feedback is recovered instruction by instruction. At a scalar step use
`|<u,v>-<u_o,v_o>|<=||u-u_o||||v||+||u_o||||v-v_o||`. At a matrix step
the discrepancy of a recomputed finite rank action and its prescribed
node is a finite sum of scalar contraction discrepancies times nodes of
bounded RMS. At a coordinate product use (F16), taking width to infinity
first and then removing its auxiliary cutoff. Oracle tails are available
from joint W2 convergence of the fixed preceding tuple. Thus actual
empirical coefficients and recomputed nodes have the same limit even
though the coordinate map need not be globally Lipschitz.

The finite initial readout is not discarded in this assertion. One may
construct the deterministic-coefficient oracle with zero limiting readout
and couple the actual fixed recursion to it. The initial readout discrepancy
is its actual RMS, tending to zero, and its coordinate supremum also tends
to zero by the Gaussian union bound. Finite induction with (F16) propagates
that error through every node. This is a comparison at fixed mesh, not a
change to either actual GF or its derivative.

## 5. Removing the time mesh without operator-norm multiplier convergence

Fix `R,delta` temporarily. Denote the population tangent mesh by `v^h`
and the forced solution with this clipped finite-law forcing by `v`.
Their generators have a common operator bound `C_T` by (F9). For each
fixed tangent vector `V`,

\[
 \sup_{t\le T}\|[G(\theta^h(\pi_h t))-G(\theta(t))]V\|
             \longrightarrow0.                                \tag{F18}
\]

Indeed reference clock, HS increment and readout convergence first gives
the forward field and action differences. Every remaining difference
in (F4)-(F6) is a bounded multiplier acting on one fixed L2 field, a
bounded action, a rank pairing, or a bounded finite-rank field. Equation
(F16)'s population proof handles every multiplier. For the evaluation
field use `D_a^2 Q_a`; its change is handled by truncating the fixed
`Q_a`. Strong continuity uniform in time follows by compactness of the
reference path. Bounded operator norms extend (F18) uniformly to compact
sets of `V`, using a finite net.

The set `{v(t):t<=T}` is compact in `mathcal H`. Comparing tangent Euler
with the integral equation on each time cell, (F18), continuity of `v`
and of its forcing make its integrated consistency error tend to zero.
The error recurrence has factor at most `1+C_T h`; its product is at
most `exp(C_T T)`. Therefore

\[
 \sup_{t\le T}\|v^h(t)-v(t)\|\longrightarrow0.                 \tag{F19}
\]

This argument proves consistency on the vectors actually tested; it
does not assert norm convergence of multiplication operators.

It remains to compare actual finite tangents with the finite mesh
proxies. This is a separate step: a finite-program width theorem alone
does not perform it. Let `v_n^h` be the finite mesh from Section 4 and
let `v_n^{R,delta}` solve the actual finite linear equation, with actual
reference generator, but with the clipped finite-law forcing. Its
inhomogeneous defect against the affine interpolant of `v_n^h` is

\[
\begin{split}
 D_{n,h}(t)={}&[G_n(t)-G_n^h(\pi_h t)]v_n^h(\pi_h t)\\
 &+G_n(t)[v_n^h(t)-v_n^h(\pi_h t)]\\
 &+b_{n,R,\delta}(t)-b_{n,R,\delta}^h(\pi_h t).
\end{split}                                                       \tag{F20}
\]

All differences are on the same finite carrier. On `E_n` the operator
bound, (F17), the clipped-forcing Lipschitz bound and the mesh increment
bound control the second and third lines in `L1([0,T];mathcal H_n)` by
`C_T,R,delta h` (with the same conclusion after a fixed-program event
of probability tending to one). The first line is a finite sum of
bounded-action/rank terms and multiplier terms of the form (F16).
For the latter the testing nodes are the mesh tangent components and
their finitely many forward variations, and the reference `Q_a`.

In detail, the first variation of a training hidden feature is
`D_a^2 xi_a`, so its coefficient error is (F16) with test `xi_a^h`.
The upper preactivation adds `(A-A^h)dot h1^h` and
`B^h(H1-H1^h)`, bounded by the action/HS norms and (F17).
The upper backward variation adds a changed bounded gate acting on
`d^h`, and a changed multiplier `c phi''(Z2)` acting on `dot z2^h`.
Both factors in this latter multiplier are bounded; subtract them
separately. In particular `(c-c^h)dot z2^h` uses (F16) with the
identity clipped outside the common readout interval as multiplier.
It uses L2 smallness of `c-c^h`, not a claimed L-infinity smallness.
The reverse variation next adds `(A-A^h)*dot delta2^h` and
`(B^h)*(delta2-delta2^h)`. For its rank block use the two-factor
HS difference inequality, and for the scalar evaluation block use
Cauchy-Schwarz on the finitely many changed L2 representing fields.
The only product in a representing field requiring a tail cutoff
is a changed bounded first gate multiplying `Q_a^h`; it is again
(F16). This list exhausts (F4)-(F6).

Here the order of cutoffs is essential. By (F19) and strong multiplier
continuity, the population testing nodes, along a chosen countable
refining mesh sequence and all its time nodes, form a relatively compact subset of
the appropriate L2 space. For `dot z2`, for example, use HS convergence
of `B^h`, strong convergence of `dot h1^h`, and the bounded continuous
action curve. Thus their L2 tails vanish uniformly as `M->infinity`.
At every separately fixed mesh their finite empirical cutoff moments
converge to the corresponding population moments. Apply (F16) at each
of that mesh's finitely many nodes, multiply by its time-cell length,
and sum. First send width to infinity, then `h->0` at fixed `M`, then
`M->infinity`. This gives

\[
 \lim_{h\downarrow0}\limsup_{n\to\infty}
 \Pr\{1_{E_n}\int_0^T\|D_{n,h}(t)\|_{\mathcal H_n}\,dt>a\}=0
 \quad(a>0).                                                     \tag{F21}
\]

Subtract the two finite linear integral equations and use the actual
generator bound `C_T`, with initial discrepancy zero. Iterating that
inequality bounds their uniform state difference by
`exp(C_T T) integral ||D_n,h||`. This proves strong finite-mesh
approximation of `v_n^{R,delta}`. Finally the same bound compares its
forcing with the original forcing: (F14)-(F15) make that `L1` difference
arbitrarily small, first choosing `R`, then `delta`. This proves capture
for every fixed `nu`, including a nonatomic one, without constructing
any nonlinear perturbed population flow.

The precise state topology is the following. There are fixed finite
programs, indexed by an accuracy `k` (including fixed source cutoff,
data quadrature and time mesh), with population tangent paths `v^[k]`
and finite same-array realizations `v_n^[k]`, such that

\[
 \sup_{t\le T}\|v^{[k]}(t)-v_\sigma(t)\|_{\mathcal H}\to0,
\]
\[
 \lim_{k\to\infty}\limsup_{n\to\infty}
 \Pr\{\sup_{t\le T}\|v_n(t)-v_n^{[k]}(t)\|_{\mathcal H_n}>a\}=0
 \quad(a>0),                                                     \tag{F22}
\]

and at each fixed `k` every finite same-layer node tuple has its joint
W2 limit. The middle tangent in each program is a finite sum of ranks;
its squared HS norm is the sum of products of their two layer Gram
entries. Consequently its Frobenius norm, and its Frobenius pairings
with fixed generated finite-rank tests, converge to their population
HS counterparts. The action of this tangent and of its adjoint on
each finite list of generated test fields is identified by the same
rank expansion and limiting contractions. Passing through (F22)
extends these assertions to the actual tangent.

In particular at any fixed finite list of times and inputs, same-layer
tuples of clocks, readout, raw first-row variations, hidden variations,
and the responses in (F4) converge in W2 with all pairwise contractions.
For products involving a changed bounded gate, uniform L2 tails of the
testing tangent fields follow from (F22) and (F19), and (F16) again
passes the product. No individual-neuron coupling across widths, or
operator-norm comparison between different carriers, is being claimed.
No W2 statement for hidden tangent paths in the coordinate supremum
norm is needed here.

## 6. Passive output observations and uniformity on the circle

The Riesz field representing `e_u` in (F1) is

\[
 \ell_u=\left((u_aD_a\phi'(w\cdot u)Q(u))_{a=1,2},
                \delta^2(u)\otimes H^1(u),H^2(u)\right).
 \tag{F23}
\]

It satisfies `||ell_u||<=C_T` uniformly in `u`, using only bounded gates,
the action bound and `||c||2`. Thus (F22), joint fixed-program second
moments for the reference fields and finite tangent fields, and their
rank pairings prove prediction-derivative convergence at each fixed
time/input. The same argument is uniform in time at a fixed input:
the reference and tangent are approximated uniformly in their stated
Hilbert norms; multiplication against a fixed proxy uses (F16).
At a fixed proxy all remaining time dependence lies in finitely many
continuous interpolated coefficients/coordinate instructions, so a
finite time net and their compact-family L2 tails give uniform
convergence. An equivalent route is the time equicontinuity argument
in the next paragraph.

For clarity the output fields have adequate time regularity without a
hidden tangent higher-moment assumption. Reference `Q(u)` is uniformly
L2 Lipschitz in time: differentiate
`Q=A*delta2`, `delta2=c phi'(Z2)` and
`Z2=A phi(w.u)` and use the compact-time raw velocity and `c` supremum
bounds. Multipliers in (F23) involving `w` are handled by clipping
the reference `Q(u)` and using its tails from (F13). Hence for every
`a>0`, the probability that the modulus
`sup_{|t-s|<=h,u}||ell_n(t,u)-ell_n(s,u)||` exceeds `a` tends to zero
as `h->0`, in the `limsup_n` sense. The tangent itself is equicontinuous
in `mathcal H_n` in probability since (F8), the generator bound and
`sup_t||b_n(t)||=O_P(1)` give `sup_t||v_n'(t)||=O_P(1)`. These two
facts prove the corresponding scalar time equicontinuity of
`<ell_n(t,u),v_n(t)>`.

Whole-circle regularity is a separate estimate. Parametrize
`u(alpha)=(cos alpha,sin alpha)`. Strong curve differentiation gives

\[
 \partial_\alpha H^1=\phi'(w\cdot u)(w\cdot u'),\quad
 \partial_\alpha Z^2=A\partial_\alpha H^1,
\quad
 \partial_\alpha Q=A^*[c\phi''(Z^2)\partial_\alpha Z^2].
 \tag{F24}
\]

The last two derivatives have L2 norms bounded by `C_T||w||2`.
Differentiate the first field in (F23). Its only additional unbounded
product is

\[
 u_aD_a\phi''(w\cdot u)(w\cdot u')Q(u).
 \tag{F25}
\]

Its L2 norm is bounded by twice that of `|w|Q(u)`, supplied by (F13).
This is a strong derivative, not only a formal product rule. Equation
(F24) first makes `Q(alpha)` a strongly C1 L2 curve and, by integrating
its derivative coordinatewise using Fubini, gives almost-everywhere
absolutely continuous coordinate representatives. In the gate difference
quotient the mean value bound is `2|w| |Q(alpha)|`; the source envelope
`|w| sup_alpha |Q(alpha)|` belongs to L2. Dominated convergence therefore
passes that quotient to (F25). The other term is a bounded multiplier
times the strongly convergent difference quotient of `Q`. The same
envelope gives continuity of the resulting derivative where needed;
in particular it justifies the H1 assertion and its fundamental theorem.
The other first-field terms are bounded by `||Q||2` and
`||partial_alpha Q||2`. Differentiating the other two fields in
(F23) uses the rank product rule and (F24); `||c||infinity` suffices.
Consequently

\[
 \|\ell\|_{H^1([0,2\pi];\mathcal H)}\le C_T
 \quad\hbox{in the population},\qquad
 \sup_{t\le T}\|\ell_n(t,\cdot)\|_{H^1([0,2\pi];\mathcal H_n)}
          =O_P(1).                                             \tag{F26}
\]

The finite assertion follows by integrating the squared estimate and
using (F13) for the supremum in time. There is no claimed Gaussian
distribution or Gaussian tail for (F25). For any absolutely continuous
Hilbert-valued field, the fundamental theorem of calculus and
Cauchy-Schwarz give
`||ell_alpha-ell_beta||<=|alpha-beta|^(1/2)||partial_alpha ell||L2`.
Apply this to (F26). The derivative predictors consequently have a
uniform-in-time circle modulus `O_P(1)|alpha-beta|^(1/2)`, because
`sup_t||v_n(t)||=O_P(1)`. Their population counterpart obeys the
deterministic version.

Choose a finite circle net and finite time net. At every point of their
product the scalar convergence follows from Section 5 and (F23).
A finite union bound gives convergence on the net. The two moduli just
proved bound the interpolation error to the whole compact time/circle
domain. First let width tend to infinity at fixed nets, and then refine
the nets. This proves (F10).

## 7. Scope and limit order

The order is finite-width right differentiation first; then, for each
fixed target accuracy, fix a source cutoff, deterministic data quadrature
and auxiliary time mesh; take width to infinity; remove these auxiliary
approximations using (F14)-(F22). There is no interchange of a derivative
with an unconstructed population law-to-flow map. All physical horizons
are separately fixed, with no restriction near initialization.

The proof supplies actual finite-GF derivative capture, the compatible
clock/HS/L2 state identification, and passive whole-circle observations.
It proves no raw-GD derivative theorem, no finite-contamination remainder,
no sampling CLT, and no uniform-in-time finite-width convergence. The
uniform population propagator is a distinct claim established, if valid,
by the complete argument in `PROPAGATOR.md`. Transport approximation in
Section 3 is used only to construct a fixed Borel forcing integral; it
is not a claimed transport bound for a nonlinear perturbed flow.
