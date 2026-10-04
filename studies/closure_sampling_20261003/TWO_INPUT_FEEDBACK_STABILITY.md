# Two-input feedback stability on the entire fitting interval

2026-10-03. Scoped independent lemma for the two orthogonal canonical
training inputs. This note was completed before exchanging its proof with
the supervising task. Its scientific inputs are the assigned equations,
`WEIGHTED_ACTIVITY_STABILITY.md`, `CANONICAL_NEURON_COMPRESSION.md`,
`COMPLEX_ACTIVITY_ROUTE.md`, and `TWO_INPUT_EXTENSION_ASSESSMENT.md`.
No other study, parallel proof, experiment, or Git operation was used.
The canonical-notation/neural reference and rigorous-proof skills apply.

**Result.** Small fixed labels give an all-physical-time, dimension-free
`C epsilon` comparison from two-sided source defects of size `epsilon`.
The proof also holds for complex states and labels on common pole-safe
tubes, with physical time remaining real. It uses the
primitive of the residual discrepancy, rather than differentiating the
tangent-kernel discrepancy. Consequently its constants do not contain a
carrier maximum or a minimum neuron weight. Arbitrary fixed real label
directions have holomorphic fitted endpoints for each finite network;
the elementary radius proved here can depend on the minimum neuron mass.
A width-uniform or logarithmic complex radius is a separate obligation.
No damping estimate along a complex physical-time contour is claimed;
short vertical continuation in physical time requires its own argument.

## 1. Weighted network, norms, and exact physical dynamics

Let the lower and upper neuron masses be positive diagonal matrices
`D_1,D_2` of total mass one. For complex vectors and matrices use

\[
 \|v\|_{D_i}=\|D_i^{1/2}v\|_2,\qquad
 B^*=D_1^{-1}B^\top D_2,\qquad
 \|B\|_{\rm HS}=\|D_2^{1/2}BD_1^{-1/2}\|_F.
 \tag{1}
\]

The star is the algebraic weighted transpose; it has no conjugation.
Hermitian norms are used only in estimates. Its operator norm agrees
with that of `B`, and
`||xy^T D_1||_HS=||x||_{D_2}||y||_{D_1}` also for complex vectors.

The two normalized inputs are `e_1,e_2`. Write `a_a=Ae_a`, for
`a=1,2`, and set

\[
 \Psi(a)=a/2+\sinh(2a)/4,\quad
 u_a=\Psi(a_a),\quad \sigma=\tanh\circ\Psi^{-1},
\]
\[
 h_a=\sigma(u_a),\quad z_a=Bh_a,\quad g_a=\tanh z_a,
 \quad\delta_a=w\odot\operatorname{sech}^2z_a,
 \quad f_a=w^\top D_2g_a,
 \quad c_a=y_a-f_a.
 \tag{2}
\]

The inverse is the real inverse, or its branch on a fixed complex strip
about the real axis. The inverse-strip proof in
`COMPLEX_ACTIVITY_ROUTE.md`, Section 2, gives fixed constants `b,C>0`
such that `Psi^{-1}, sigma`, and their derivatives needed below are
holomorphic with bounded derivatives on `|Im u|<=2b`; `tanh` and
its needed derivatives are bounded on `|Im z|<=2b`. In particular,
on the real axis both `Psi^{-1}` and `sigma` are 1-Lipschitz.

For loss `sum_a(f_a-y_a)^2/2`, the exact canonical physical flow is

\[
 \dot u_a=c_a B^*\delta_a,\qquad
 \dot B=\sum_{a=1}^2c_a\delta_ah_a^\top D_1,\qquad
 \dot w=\sum_{a=1}^2c_ag_a.
 \tag{3}
\]

Thus no scalar activity or fixed residual direction is being substituted.
Let `theta=(u_1,u_2,B,w)` and let `V_a(theta)` be the vector field
with `B^*delta_a` in the `u_a` block, zero in the other `u` block,
and `delta_a h_a^T D_1,g_a` in the matrix and readout blocks. Then
`theta_dot=sum_a c_a V_a(theta)`.
State differences use the norm

\[
 \|\Delta\theta\|
 =\sum_{a=1}^2\|\Delta u_a\|_{D_1}
        +\|\Delta B\|_{\rm HS}+\|\Delta w\|_{D_2}.
 \tag{4}
\]

Constants below depend only on a fixed initialization operator bound `K`,
a fixed initial top-Gram gap `gamma>0`, and, for complex statements, the
fixed pole margin. They never depend on the number of neurons, the minimum
mass, initial first-layer coordinate maxima, or carrier maxima.

## 2. Small labels give finite total activity and fitting

Assume `w(0)=0`, `||B(0)||_op<=K`, and that the real initial matrix

\[
 Q_0=(g_a(0)^\top D_2g_b(0))_{a,b=1}^2
 \quad\hbox{satisfies}\quad Q_0\succeq\gamma I_2.
 \tag{5}
\]

Put `s(t)=int_0^t |c(v)|_1 dv`. On any real interval where `s<=S`,
bounded real gates and (3) imply

\[
 \|w(t)\|_\infty\le s(t),\quad
 \|B(t)-B(0)\|_{\rm HS}\le s(t)^2/2,\quad
 \sum_a\|u_a(t)-u_a(0)\|_{D_1}\le C_Ks(t)^2,
 \tag{6}
\]
\[
 \sum_a\big(\|h_a(t)-h_a(0)\|_{D_1}
                 +\|g_a(t)-g_a(0)\|_{D_2}\big)
 \le C_Ks(t)^2.
 \tag{7}
\]

For example, integrate `||delta_a||<=s` against `|c|_1` for the
matrix estimate, then integrate `||B||_op s |c|_1` for the `u`
estimate. The forward difference is
`B(h_a-h_a(0))+(B-B(0))h_a(0)`, which proves (7).

Direct differentiation of (2)--(3) gives

\[
 \dot c=-\mathcal K(\theta)c,
\]
\[
 \mathcal K_{ab}
 =g_a^\top D_2g_b
 +(\delta_a^\top D_2\delta_b)(h_a^\top D_1h_b)
 +\mathbf1_{a=b}\,
 (B^*\delta_a)^\top D_1
          \operatorname{diag}(\sigma'(u_a))B^*\delta_a.
 \tag{8}
\]

On the real axis the last term is the squared norm of
`sech^2(a_a) odot B^*delta_a`, and the middle term is a Gram matrix
of the rank-one parameter gradients. Hence `Kcal>=Q`, where
`Q=(g_a^T D_2g_b)`. Equations (6)--(7) give
`||Q-Q_0||<=C_K S^2`. Choose `S_0>0` so this is at most
`gamma/2`. On this tube,

\[
 |c(t)|_2\le |y|_2e^{-\kappa t},\qquad
 s(t)\le\sqrt2\,|y|_2/\kappa,
 \qquad\kappa=\gamma/2.
 \tag{9}
\]

Choose `y_*>0` with `sqrt2 y_*/kappa<S_0/2`. A first-exit
argument then keeps the real solution in this tube for all physical time.
The increment bounds prevent finite-dimensional escape, so local existence
continues globally. Its state converges because (3) has integrable norm,
and (9) shows `f_a(infinity)=y_a` for both samples. This proof permits
either sign of each label and any real direction of the label vector.

For complex labels and real initialization, the same estimates hold with
fixed larger constants on every interval where all `u_a,z_a` remain in
the stated strips. In this case (8) is a bilinear identity and need not
be positive. However (6)--(7) and bounded gates give the stronger useful
bound

\[
 \|\mathcal K(\theta)-Q_0\|_{\rm op}\le C_Ks(t)^2.
 \tag{10}
\]

The middle and last terms of (8) each have norm `O(s^2)` by the
weighted operator bound; no coordinate maximum of `B^*delta` enters.
Thus the Hermitian part of `Kcal` is at least `kappa I` for smaller
fixed `S_0`, proving (9) on every common complex pole-safe interval.
This establishes residual damping conditional on the pole tube; it does
not by itself establish a width-independent complex pole tube.

## 3. Source defects for a restricted dense reference

Let `theta_n(t)` be a real full dense solution with the same assumptions,
or a complex full solution in its pole tube. Its empirical masses are
`1/n`. Select lower and upper index sets `I,J`, positive retained
masses `D_1,D_2`, and an initial compressed mixer `B_0` of weighted
operator norm at most `K`. Define the comparison state by

\[
 u_{R,a}=(u_{n,a})_I,\quad w_R=(w_n)_J,\quad
 B_R(t)=B_0+\int_0^t\sum_{a=1}^2
       c_{n,a}(v)\delta_{n,a}(v)_J h_{n,a}(v)_I^\top D_1\,dv.
 \tag{11}
\]

Write `h_{R,a}=h_{n,a,I}`. Suppose the supplied source construction
gives, at each time and for both training inputs,

\[
 \|B_Rh_{R,a}-z_{n,a,J}\|_{D_2}\le\epsilon_f,
 \qquad
 \|B_R^*\delta_{n,a,J}-(B_n^*\delta_{n,a})_I\|_{D_1}
       \le\epsilon_b,
 \tag{12}
\]
\[
 |w_R^\top D_2g_{n,a,J}-f_{n,a}|\le\epsilon_p.
 \tag{13}
\]

The analogous forward and pairing defects are assumed for each query to
be compared. All three defects are uniform in the original physical time.
The proof is deterministic conditional on these defects; it does not
construct them or treat a small forward defect as a reverse defect.

Let `G(theta)` have columns `g_1(theta),g_2(theta)`. Evaluate this
map at `theta_R` using its own forward product `B_Rh_R`; denote the
result by `G_R`. Bounded derivatives and (12) give

\[
 \dot\theta_R=\sum_a c_{n,a}\,[V_a(\theta_R)+E_a(t)],
 \qquad \|E_a(t)\|\le C(\epsilon_f+\epsilon_b),
 \tag{14}
\]
\[
 F(\theta_R)=G_R^\top D_2w_R=f_n+\eta(t),
 \qquad |\eta(t)|_2\le C(S\epsilon_f+\epsilon_p),
 \tag{15}
\]

where `F=(f_1,f_2)`. To verify (14), the reconstructed response differs
from the restricted full response by at most `CS epsilon_f`, since
`||w_R||_infinity<=CS`. The `u` defect is therefore at most
`epsilon_b+CS epsilon_f`, the matrix defect at most `CS epsilon_f`,
and the readout defect at most `C epsilon_f`. Equation (15) follows
by one more pairing with `w_R`. The same estimates hold complexly if
both reconstructed and original preactivations lie in the fixed strips.

Initialize the autonomous compressed network by `theta_C(0)=theta_R(0)`
and train it by (3) with its own controls `c_C=y-F(theta_C)`. Assume
its initial top Gram has the same fixed lower bound. Both true networks
then satisfy (9), so their total absolute activities are at most

\[
 S=C_{\gamma}|y|_2.
 \tag{16}
\]

The comparison state has the same operator and readout tube by (11).
In the real setting this requires no further gate assumptions.

## 4. Bounded activity fields and the residual primitive

On all the above tubes, finite differences satisfy

\[
 \|V_a(\theta)-V_a(\widetilde\theta)\|
       \le C\|\theta-\widetilde\theta\|,
 \quad \|V_a(\theta)\|\le C,
 \quad
 \|G(\theta)-G(\widetilde\theta)\|_{\mathbb C^2\to D_2}
       \le C\|\theta-\widetilde\theta\|.
 \tag{17}
\]

For explicit verification, put `U=sum_a||u_a-utilde_a||`,
`M=||B-Btilde||_HS`, and `V=||w-wtilde||`. Bounded scalar
derivatives give `||Delta h_a||<=CU`,
`||Delta z_a||<=C(U+M)`, and
`||Delta delta_a||<=C V+CS(U+M)`. Substitution in the three blocks
of `V_a`, using (1), proves (17). Only the endpoint preactivation
strips and their convexity are used; a line segment in full parameter
space need not stay pole-safe. Taking infinitesimal differences gives
the corresponding derivative bound along a safe solution.
Moreover, along the compressed path,

\[
 \|\dot V_a(\theta_C)\|\le C|c_C|_1,
 \qquad \|\dot G_C\|\le CS|c_C|_1.
 \tag{18}
\]

The second estimate is sharper because both `u_dot` and `B_dot`
contain a response `delta` of size `O(S)`; the forward chain rule
then gives `||g_dot||<=CS |c_C|_1`.

Define the integrated control discrepancy

\[
 p(t)=\int_0^t[c_C(v)-c_n(v)]\,dv\in\mathbb C^2.
 \tag{19}
\]

This is a comparison variable, not an activity parameterization of either
network, and the two activity vector fields need not commute. For a finite
horizon `T`, set
`P_T=sup_{t<=T}|p(t)|_2`,
`D_T=sup_{t<=T}||theta_C(t)-theta_R(t)||`, and
`epsilon=epsilon_f+epsilon_b+epsilon_p`.
Subtract (14) from the compressed equation and integrate the term
`sum_a V_a(theta_C) p_dot_a` by parts. Its exact integral is

\[
 \sum_aV_a(\theta_C(t))p_a(t)
 -\int_0^t\sum_a\dot V_a(\theta_C(v))p_a(v)\,dv.
 \tag{20}
\]

Equations (16)--(18) therefore give

\[
 D_T\le C(1+S)P_T+CS D_T+CS\epsilon.
 \tag{21}
\]

After choosing the fixed label threshold smaller, absorb the middle term:

\[
 D_T\le C(P_T+S\epsilon).
 \tag{22}
\]

No estimate of `int_0^T |c_C-c_n|` has been assumed. Such an
estimate obtained by differentiating tangent kernels can introduce a
carrier maximum through second derivatives of the readout; (20) avoids it.

## 5. Damping the primitive and closing the comparison

Apply the same integration by parts only to the readout block. It gives

\[
 w_C(t)-w_R(t)=G_C(t)p(t)+\xi(t),
 \tag{23}
\]
\[
 \xi(t)= -\int_0^t\dot G_C(v)p(v)\,dv
 +\int_0^t(G_C-G_R)(v)c_n(v)\,dv
 -\int_0^t\sum_a c_{n,a}(v)E_{a,w}(v)\,dv.
\]

Consequently

\[
 \sup_{t\le T}\|\xi(t)\|_{D_2}
       \le CS^2P_T+CS D_T+CS\epsilon.
 \tag{24}
\]

Using (15) and then (23), the actual prediction discrepancy is exactly

\[
 F(\theta_C)-f_n
 =G_C^\top D_2(w_C-w_R)
      +(G_C-G_R)^\top D_2w_R+\eta
 =Q_Cp+q,
 \tag{25}
\]

where `Q_C=G_C^T D_2G_C` and

\[
 \sup_{t\le T}|q(t)|_2
 \le C(S^2P_T+S D_T+\epsilon)
 \le CS P_T+C\epsilon.
 \tag{26}
\]

The last inequality uses (22) and `S<=1`. By (19),

\[
 \dot p=-Q_C(t)p-q(t),\qquad p(0)=0.
 \tag{27}
\]

The real symmetric matrix `Q_C` is bounded below by `kappa I`;
on a complex tube its Hermitian part has the same bound, after reducing
the fixed threshold. This follows from (7) applied to the compressed
network, without differentiating `Q_C`. For the homogeneous equation,
differentiating the squared Hermitian norm proves that its fundamental
solution has norm at most `exp(-kappa(t-v))`. Variation of constants
in (27) and (26) thus gives

\[
 P_T\le\kappa^{-1}(CS P_T+C\epsilon).
 \tag{28}
\]

Choose the fixed label threshold once more so `CS<=kappa/2`.
Absorbing proves, for every finite horizon with the stated hypotheses,

\[
 \sup_{t\le T}|p(t)|_2
 +\sup_{t\le T}\|\theta_C(t)-\theta_R(t)\|
 +\sup_{t\le T}|f_C(t)-f_n(t)|_2
 \le C\epsilon.
 \tag{29}
\]

The constant is independent of `T`, width, neuron masses, and carrier
maxima. Letting `T` increase proves the real estimate on `[0,infinity)`.
Both real networks fit and converge by Section 2. The reference matrix
in (11) also converges, so (29) includes their fitted endpoints.

For a real circle query `x_theta=sqrt(2)(cos(theta),sin(theta))`, its
first preactivation is
`a_1 cos(theta)+a_2 sin(theta)`. Since `Psi^{-1}` and real `tanh`
are 1-Lipschitz, its first-feature discrepancy is bounded by the sum of
the two `u` discrepancies. The query forward defect, operator bound,
readout bound, and query pairing defect then give

\[
 \sup_{t\in[0,\infty],\,\theta\in\mathbb R}
 |f_C(t,x_\theta)-f_n(t,x_\theta)|\le C\epsilon.
 \tag{30}
\]

On complex query domains the same conclusion holds whenever their
first and second preactivations have a fixed pole margin. Training
pole safety alone is not asserted to imply query pole safety.

## 6. Different labels and holomorphy through fitting

The argument also compares two exact networks of the same architecture
and initialization, with different labels `y_C,y_R`. There are then no
source defects, while (27) becomes

\[
 \dot p=(y_C-y_R)-Q_Cp-q,
 \qquad \sup_{t\le T}|q(t)|\le CS P_T.
 \tag{31}
\]

The identical absorption proves

\[
 \sup_{t\le T}\|\theta(t;y_C)-\theta(t;y_R)\|
 \le C|y_C-y_R|_2.
 \tag{32}
\]

This holds for real labels on all physical time, and for complex labels
on common pole-safe time intervals. It requires no invariant residual
direction. In particular it applies to `y=lambda nu` for every fixed
real `nu` of norm one.

For completeness, (32) gives a fully unconditional finite-dimensional
holomorphy statement, though with a weaker radius than a Gaussian cavity
argument may eventually supply. Put

\[
 \mu=\min\{(D_1)_{ii},(D_2)_{jj}\}>0.
 \tag{33}
\]

Fix a real label vector `y_0` strictly inside the small-label ball. For
complex `y` close to `y_0`, solve (3) until the first pole-strip exit.
All estimates above hold on its common prefix with the real solution,
and (32), followed by the forward difference estimate in (17), gives

\[
 \max_a\|\Im u_a(t;y)\|_\infty
 +\max_a\|\Im z_a(t;y)\|_\infty
 \le C\mu^{-1/2}|y-y_0|_2.
 \tag{34}
\]

Choose a complex label ball of radius at most `c sqrt(mu)` and small
enough to stay in the fixed label-norm threshold. Equation (34) is then
strictly inside the pole caps, so a first-exit continuation gives the
complex solution for every physical time. Weighted state increments
bound every coordinate at fixed positive masses, excluding any other
finite-time blow-up. The residual bound (9) remains valid on this ball.

For each finite `t`, holomorphic local ODE iteration and uniqueness give
holomorphic dependence of `theta(t;y)` on `y`. Moreover, (3), (9),
and the bounded fields yield the uniform tail estimate

\[
 \|\theta(\infty;y)-\theta(t;y)\|
       \le C\sup_{y\text{ in the ball}}|y|_2e^{-\kappa t}.
 \tag{35}
\]

Thus the fitted state is a locally uniform limit of holomorphic maps.
Passing to the limit in the Cauchy integral formula on each smaller
polydisk proves that it is holomorphic. Restricting to `y=lambda nu`
shows that the fitted state and every pole-safe query predictor are
holomorphic in the arbitrary fixed label direction, including at
`lambda=0`. There is no division by a residual or a residual norm.

For dense empirical masses the elementary bound in (34) gives radius
`c/sqrt(n)`. The radius is not width-independent, whereas the real and
conditional-complex stability constant in (29) is. A larger complex
radius needs an additional coordinatewise argument, for example a
Gaussian cavity estimate. This distinction is essential if holomorphy
is to supply a sublinear source approximation rather than only analytic
dependence at each finite width.

## 7. What the lemma supplies

The completed conclusion is the deterministic same-physical-time
comparison (29)--(30), including fitting, for arbitrary two-input small
labels and coordinated forward/reverse/pairing defects. Its complex
version and label sensitivity use the same constant on common safe
domains. Equations (34)--(35) additionally prove finite-width label
holomorphy through the fitted endpoint. None of these claims assumes
commuting activity fields, aligned residuals, a shared prescribed control,
or a modified full reference network.

The source construction must still establish its own defects and, when
needed, a sufficiently wide common complex domain. This note supplies
the global feedback estimate needed to compare autonomous cavities with
their own residuals; it does not assert Gaussian independence for a
reference driven by externally copied full-network residuals.

## 8. Post-freeze cross-check and singleton deletion specialization

Sections 1--7 were frozen at SHA-256
`dd4b9b637a33776c4ecd83e961554c34984026e6d7e08539e9b5f61471a2493a`
before the supervisor authorized exposure to `TWO_INPUT_STABLE_GEOMETRY.md`.
The exposed version had SHA-256
`93040bef724cfef765aa26d961c996297e13d67b31dcbc3fc51876ac1212c820`.
The latter's Sections 1--3 were then independently reconstructed. Its
fixed-initial-feature version of the integration-by-parts argument is
valid: `N_a(theta)=w^T D_2(g_a-g_{a,0})` has finite-difference
Lipschitz constant `CS`, because `g-g_0=O(S^2)`, `w=O(S)`, and
the forward map is uniformly Lipschitz in (4). Thus its reduction to
the initial Gram does not require a tangent-kernel derivative or a
carrier maximum. The real convex tube used there is sufficient. For
complex comparisons, the endpoint-strip proof (17) avoids additionally
assuming pole safety of straight parameter segments. No objection was
found to the real all-time argument or its normalization.

Here are explicit rectangular deletion estimates, including their
forcing and observation discrepancies. They also verify the deletion
claims of that note. All retained neuron masses remain `1/n`; a
deleted layer has total mass `(n-1)/n`. Every estimate in Sections
1--5 holds for layer masses at most one, since each use of total mass
only bounds the norm of a coordinatewise bounded vector from above.

It is useful first to record the directly proved generalization of (29).
If the reference discrepancy in the state equation is `e(t)` with
`int_0^infinity ||e(t)||dt<=epsilon_state`, and its observation
discrepancy has supremum `epsilon_obs`, then the same proof gives

\[
 \sup_t\|\theta_C(t)-\theta_R(t)\|
 \le C(\epsilon_{\rm state}+\epsilon_{\rm obs}).
 \tag{36}
\]

Indeed replace `CS epsilon` in (21),(24) by `epsilon_state` and
the standalone observation error in (26) by `epsilon_obs`. Both
absorptions remain identical. A coordinate-dependent or time-dependent
forcing need not be autonomous.

Delete a lower neuron `i`, and call its initialized outgoing column
`x_i=W_{0,:,i}`. The autonomous cavity omits this column and its two
first coordinates, starts from exactly the retained initialization, and
uses its own predictions and residuals. On the full operator event,
the learned column increment obeys

\[
 \|W_{:,i}(t)-x_i\|_2\le CS^2/\sqrt n.
 \tag{37}
\]

This follows directly by integrating
`sum_a c_a delta_a h_{a,i}/n` and using
`||delta_a||_2<=sqrt(n) S`. The retained full state has additional
top input `W_{:,i}h_{a,i}`, of Euclidean norm at most `C_K` and
normalized norm at most `C_K/sqrt(n)`. Hence the residual-free
readout velocity discrepancy is `O(n^{-1/2})`; its `u` and matrix
velocity discrepancies are `O(S n^{-1/2})`. The actual total state
forcing and output discrepancy satisfy

\[
 \epsilon_{\rm state}\le CS/\sqrt n,
 \qquad \epsilon_{\rm obs}\le CS/\sqrt n.
 \tag{38}
\]

The output estimate pairs the bounded-top-gate discrepancy with a
readout of maximum `CS`. Initially, each top feature changes by
normalized norm at most `K/sqrt(n)`, so the initial Gram changes by
at most `C_K/sqrt(n)` in operator norm. A fixed full gap therefore
gives a fixed cavity gap for large `n`. Applying the cavity's own
fitting theorem and then (36) proves

\[
 \sup_t\|\theta^{-i}(t)-\theta_R(t)\|
       \le CS/\sqrt n.
 \tag{39}
\]

Delete an upper neuron `j`, with initialized row `x_j^T=W_{0,j,:}`.
There is no retained forward discrepancy. The only extra full state
velocity is the lower block
`c_a W_{j,:}^T delta_{a,j}`. Its normalized norm is at most
`CS |c_a|/sqrt(n)`, since the learned row increment also obeys
`||W_{j,:}-x_j^T||_2<=CS^2/sqrt(n)`. The missing output is
`w_j g_{a,j}/n`. Thus

\[
 \epsilon_{\rm state}\le CS^2/\sqrt n,
 \qquad \epsilon_{\rm obs}\le CS/n,
\]
\[
 \sup_t\|\theta^{-j}(t)-\theta_R(t)\|
       \le C(S^2/\sqrt n+S/n).
 \tag{40}
\]

Its initial top Gram loses one bounded rank-one summand divided by `n`,
so its gap also persists. The extra `S/n` term in (40) should not
be dropped uniformly as `S` approaches zero; at fixed nonzero labels
and sufficiently large width it is absorbed by `S^2/sqrt(n)`.

Multiplying (39)--(40) by `sqrt(n)` yields the usual unnormalized
state distance with hidden matrix coordinate `H=sqrt(n) W`.
In particular lower deletion costs `CS`, and upper deletion costs
`C(S^2+S/sqrt(n))`. These statements are deterministic, all-time,
and remain valid for complex states and labels on common pole-safe tubes
along real physical time. These deletion estimates alone do not control
continuation along vertical complex-time contours.

The lower cavity depends on neither the omitted Gaussian column nor
the removed first-layer coordinates. The upper cavity depends on
neither the omitted Gaussian row nor its omitted readout coordinate.
Conditioning on all retained initialization therefore preserves the
Gaussian law of the omitted mixer vector. Each cavity uses its own
residuals in (39)--(40), so this independence is not compromised by
copying controls from the full flow.
