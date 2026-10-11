# Finite training-source scope and response check

2026-10-10. Scoped proof reconstruction for the Legendre dependency. This
file makes no paper, book, implementation, or Git change. It establishes the
dimension-scope extension and supplies an explicit rectangular-grid completion
of the stopped insertion argument. It is not a review of the remaining
Legendre proof or of either selected compression construction.

The finite training-source argument applies when `m<d`. Its normalized
response is exactly the response used in `DENSE_LEGENDRE_ROUTE.md`. A
training-span reduction proves the scope extension without changing a
Gaussian variance, physical learning rate, width normalization, label, or
population Gram. The full ambient sphere still requires the original
ambient-dimensional fitting event. The stated polynomial source gate already
pays for that event.

The reconstruction covers the complete finite-training dependency chain,
including local insertion, the augmented response, scalar trace absorption,
and finite moment/budget composition. No remaining gap in those two last
steps was identified. The result below uses the displayed proofs and the
explicit grid completion, rather than treating the older source theorem
or a prior review verdict as an assumption. The scope does not include the
other source domains or the new deterministic Legendre history estimate.

There is a detail that should be made explicit when this dependency is
assembled: deterministic grid points must be interpolated inside the common
random stopping prefix. A Gaussian estimate at a fixed endpoint does not
automatically apply after clamping that endpoint by a full-network stop.
Section 4 below supplies an inward tensor grid that closes this issue for
the rectangular, finite-training-query source with its existing grid count.

## 1. Setup and the actual dependency

Use the compact paper's normalized inputs `v_a=x_a/sqrt(d)`, with
`||v_a||=1`, `m>=2`, `d>=1`, and hidden depth `L>=2`. The forward pass is

\[
z_a^{(1)}=W^{(1)}v_a,\qquad
z_a^{(j)}=W^{(j)}h_a^{(j-1)},\qquad
h_a^{(j)}=\phi_j(z_a^{(j)}),\qquad
f_a=w^\top h_a^{(L)}/n.
\]

Here `W^(1)` is `n by d`, each later hidden matrix is `n by n`, and
`w` has length `n`. Initial first-layer entries are independent `N(0,1)`;
later hidden entries are independent `N(0,1/n)`; the blocks are independent;
and `w(0)=0`. For `r_a=f_a-y_a` and loss `m^{-1}sum_a r_a^2`, the
physical mobilities `(n,1,...,1,n)` give

\[
\begin{aligned}
\dot W^{(1)}&=-\frac2m\sum_a r_a\delta_a^{(1)}v_a^\top,\\
\dot W^{(j)}&=-\frac2{mn}\sum_a r_a\delta_a^{(j)}h_a^{(j-1)\top},
\qquad
\dot w=-\frac2m\sum_a r_a h_a^{(L)},
\end{aligned}
\]

where `k_a^(L)=w`, `delta_a^(j)=phi_j'(z_a^(j)) odot k_a^(j)`, and
`k_a^(j)=W^(j+1)T delta_a^(j+1)`. These backward quantities have no
residual factor.

Keep the paper's analytic activation envelope `beta`, population feature
Gram gap `gamma>0`, and label RMS `Y>0`. Put

\[
X=\beta^L\ge100,\qquad \lambda=\gamma/m\le1,\qquad
\chi=1+\lambda^{-1},\qquad S=16Y/\lambda,\qquad
\ell=\log(en).
\]

The paper assumes `Y/lambda<=X^{-30}`. The explicit coefficient calculation
in `compact_foundations.tex`, Claim `cp:src-powers`, proves `S<=X^{-26}`
and all the original source allowances. It preserves the actual source
constants, including

\[
K_{\rm src}\le X^{21},\qquad U_{\rm fin}\le X^{26}.
\tag{1}
\]

It does not redefine these constants as the larger envelopes used in the
finite-width ledger. The fitting allowance also follows: the fitting
recurrences give `H<=X^2`, `F<=X^{10}`, so `8H sqrt(F)<=X^8`, which is
more than sufficient for `Y<=lambda/(8H sqrt(F))`.

For `0<rho<1/4`, define

\[
p=\max\left\{1,\left\lceil
\frac{\log(4emL/\rho)}{\log(64e^2)}\right\rceil\right\},\qquad
\mathcal A_d=X^{2000}\chi^4(m+d+p+1)^4.
\]

The dependency is the finite training-source assertion at

\[
n\ge\left\lceil(\mathcal A_d/\rho)^{1100}\right\rceil,
\qquad
T=32\ell/\lambda,\qquad
r=\frac1{pX^{100}(1+\lambda)\sqrt\ell}.
\tag{2}
\]

Its source domain is a neighborhood of
`D_1=[-r,T+r]+i[-r,r]`. It gives training forward/backward RMS bounds,
training coordinate maxima, and the preactivation-response bound specified
in Section 3. This domain is smaller than the current paper's displayed
finite-query domain with radius `1/(lambda sqrt(ell))`; those two domains
must not be identified. No complex whole-sphere conclusion is inferred.

## 2. Exact training-span reduction

Let `k=dim span{v_1,...,v_m}` and choose deterministic matrices
`V in R^{d by k}` and `V_perp in R^{d by (d-k)}` so that
`[V,V_perp]` is orthogonal and the columns of `V` span the training inputs.
The unit-norm inputs imply `1<=k<=min(m,d)`. Define

\[
v'_a=V^\top v_a,\qquad x'_a=\sqrt{k}\,v'_a,\qquad
A'=W^{(1)}V,\qquad A_\perp=W^{(1)}V_\perp.
\tag{3}
\]

Then `||v'_a||=1`, `||x'_a||=sqrt(k)`, and
`W^(1)v_a=A'v'_a`. Multiplication by the orthogonal matrix `[V,V_perp]`
preserves a standard Gaussian row. Consequently `A'(0)` has independent
`N(0,1)` entries and is independent of `A_perp(0)` and of all later blocks.
The reduced initialized model has exactly the stipulated distribution,
including in the case `k=1`.

Multiplying the first-layer flow by `V` and `V_perp` gives

\[
\dot A'=-\frac2m\sum_a r_a\delta_a^{(1)}v_a'^\top,
\qquad \dot A_\perp=0.
\tag{4}
\]

The later equations are unchanged. Uniqueness of the finite-dimensional
ODE therefore identifies the two training trajectories, including all
hidden features, carriers, residuals and predictions. The same algebra and
local uniqueness identify their holomorphic continuations before the source
stops. No rescaling of physical time occurs.

Also `v_a'^T v'_b=v_a^T v_b`. The complete population covariance recursion,
its final gap `gamma`, `lambda`, `Y`, `S`, and `beta` are unchanged.
The reduced inputs span `R^k`, so even an unnecessary full-input-rank
hypothesis in a source formulation is met after reduction. The width `n`
stays unchanged; every rectangular cavity retains normalization `n`.

The same transformation commutes with deleting neurons: deleting rows of
the first layer and multiplying its columns by `V` commute, while all
interior row and column roots are unaffected. Thus the source's complete
cavity system, its training budgets, and its training pole/response stops
are the same training objects in either representation.

All learned first-layer increments obey

\[
W^{(1)}(t)-W^{(1)}(s)=[A'(t)-A'(s)]V^\top,
\qquad
\|W^{(1)}(t)-W^{(1)}(s)\|_F=\|A'(t)-A'(s)\|_F.
\tag{5}
\]

Hence the normalized parameter norms used in fitting, insertion and real
trajectory comparison are preserved on every moving direction. Inactive
parameter directions give a zero vector field; the negative-Gram
variational flow remains nonexpansive there. No strict positive parameter
Hessian or full data rank is required.

For a general unit query `v`, the exact original first preactivation is

\[
z^{(1)}(t,v)=A'(t)V^\top v+A_\perp(0)V_\perp^\top v.
\tag{6}
\]

The second term generally does not vanish. Also `||V^T v||` need not be
one. The reduced training network alone therefore does not represent all
ambient-sphere predictions. Preserve this frozen orthogonal block and use
the original `d`-dimensional real fitting/operator event for the whole
sphere. This is a proof reduction, not permission to discard first-layer
storage or change the promised query domain.

## 3. The response and its lower probes are preserved

The Legendre route uses Euclidean mobility coordinates

\[
\theta=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n),
\qquad R_{ba}^{(j)}=D_\theta z_b^{(j)}\nabla_\theta f_a.
\]

The source notes use `Theta=sqrt(n) theta` and `F_a=n f_a`. The chain rule
gives, with no omitted factor,

\[
D_\theta z_b^{(j)}=\sqrt nD_\Theta z_b^{(j)},\qquad
\nabla_\theta f_a=n^{-1/2}\nabla_\Theta F_a,
\qquad
R_{ba}^{(j)}=D_\Theta z_b^{(j)}\nabla_\Theta F_a.
\tag{7}
\]

Define the activated response `Q_{ba}^(j)=phi_j'(z_b^(j)) odot R_{ba}^(j)`
and the feature pairing `c_{ab}^(j)=h_a^(j)T h_b^(j)/n`. Direct
differentiation gives

\[
R_{ba}^{(1)}=\delta_a^{(1)}v_a^\top v_b,\qquad
R_{ba}^{(j)}=\delta_a^{(j)}c_{ab}^{(j-1)}+
W^{(j)}Q_{ba}^{(j-1)}.
\tag{8}
\]

Every quantity on the right is preserved by (3)--(4). This already proves
response invariance without any parameter-space dimension argument.

For the lower probes, let `J` be the isometric embedding of reduced
mobility parameter variations into full variations, replacing the first
block `U` by `UV^T` and keeping all other blocks unchanged. For every
training feature map its derivative annihilates the inactive first-layer
directions. If `C_a=D_Theta h_a^(j-1)` and `C'_a` is its reduced version,
then

\[
C_a=C'_aJ^\top,\qquad C_a^\top=JC_a'^\top,\qquad
C_bC_a^\top=C'_bC_a'^\top.
\tag{9}
\]

In particular the extra observable below a deletion,
`C_b C_a^T bar q_a`, and every forward image of `C_a^T y_i` are unchanged.
The omitted incoming root `y_i` here is an interior hidden-row root with
covariance `I/n`, not an input-space root. In a first-layer deletion there
is no retained reverse source. Its incoming row appears only through its
own Gaussian preactivation, whose training covariance is the unchanged
matrix `(v_a^T v_b)_{ab}`.

The same isometry preserves the nonzero parts of the Hessian and the
variational propagator, all endpoint contractions, and their normalized
traces. Inactive blocks contribute zero to an endpoint contraction.
The trace normalization is `1/n`, not reciprocal parameter dimension;
it is preserved even when `d` is much larger than `m`.

Thus source equation (28) yields exactly

\[
\max_{a,b,j,i,t\in D_1}|R_{ba,i}^{(j)}(t)|
\le S U_{\rm fin}\sqrt\ell
\le16(Y/\lambda)X^{26}\sqrt\ell.
\tag{10}
\]

This is not an ordinary output NTK bound or a bound on an arbitrary
directional derivative. The finite-source proof includes both indices of
this specific response.

## 4. Explicit stopping-prefix grid construction

This supplies a missing geometric specification in the terminal-grid
paragraph of `INSERTION_MAP_MODULI.md`, Section 5. Use the nested
rectangles `D_s=sD_1`, `0<=s<=1`, as in the compact source proof. Let
`sigma_c` be a cavity's own first-stop level. The cavity, `sigma_c`, and
its zero-on-failed-initialization convention depend only on retained
initialization. Let `P_{sigma_c}` clamp the two real coordinates to
`D_{sigma_c}`. Its coefficient paths are extended using this own clamp.

Choose a deterministic tensor grid consisting of the points of `h Z^2`
inside `D_1`, with the origin included, where

\[
h=\frac{n^{-2}}{1+\mathcal A_d\ell^8}.
\tag{11}
\]

For each fixed grid point `g`, use the fixed contour `gamma_g` that runs
from zero along the real axis to `a_0(g)=clip_[0,T] Re(g)`, then to
`Re(g)`, then vertically to `g`. For a stopped cavity, define its tested
linear maps along the clipped contour `P_{sigma_c} gamma_g`, with
integration against the increments of that contour. This contour is
retained-initialization measurable. It is monotone on its real pieces and
has only the same short vertical/horizontal pieces as the original
contour. Freezing a piece reduces its length and activity. The negative-Gram
and residual-Hessian propagator bounds therefore remain the stated ones.

At this fixed endpoint and cavity, construct nets of deterministic
one-dimensional control restrictions before integrating any omitted root.
Their resulting linear images and centered quadratic forms have exactly
the conditional Gaussian laws used in the finite-source proof. The
endpoint after the cavity's own clipping may be random in retained
initialization; that is harmless under this conditioning. No endpoint
clamped by the full network is used in these tests.

Let `tau` be any common stopped-prefix level, possibly dependent on all
omitted roots. For any `z in D_tau`, round each coordinate toward zero to
obtain a grid point `g`. Coordinatewise convexity and the inclusion of
zero give

\[
g\in D_\tau,\qquad [g,z]\subset D_\tau,\qquad
|z-g|\le\sqrt2h.
\tag{12}
\]

The entire canonical contour to `g` lies in `D_tau`. On the common prefix
`tau<=sigma_c`, its cavity clamp is therefore the identity. The linear
maps evaluated on actual analytic controls agree with the already tested
ones at `g`; the uniform control event permits these controls to be chosen
after observing the omitted roots. The maps are holomorphic on the common
pre-stop rectangle, so integrate their derivative bound along `[g,z]`.

For the enlarged response maps, the raw derivative bound is
`B sqrt(p n) n^{1/4000} ell^8`, with
`B=X^{1000} chi^2`. On the root-norm event the centered quadratic
interpolation error is at most

\[
10\sqrt2 Bp^{3/2}n^{1/2+1/4000}\ell^8 h
<n^{-1/10}/8,
\tag{13}
\]

under the source gate. This includes the trace correction; the linear
root multiplier is smaller. The original lattice count is bounded by
the same rectangle-count formula, hence by `n^6`. Boundary grid points
depending on `tau` are unnecessary. Choosing `g` after observing `tau`
is valid because the successful event covers every member of the fixed
finite grid. This is the required distinction between uniformity over a
deterministic grid and an unjustified Gaussian claim at a root-dependent
clamped endpoint.

For scalar Gaussian references and common-cavity correction paths, the
references are already extended by their separate own clamps. Their
global Lipschitz bounds and root independence survive those clamps and
the deterministic-ball projection. They can therefore be tested on the
full fixed grid, or treated by the stated rectangle entropy bound, without
any full-network clipping. The identity
`P_sigma a_0(z)=a_0(P_sigma z)` ensures the complex-minus-real correction
uses the correct real anchor even outside the cavity's surviving prefix.

This construction completes the finite rectangular source's interpolation
step. It does not validate arbitrary shapes of expanding domains or
whole-sphere frame meshes; those are outside this dependency.

## 5. Reconstruction of the finite probability chain

The following are mathematical checks of the source composition, not
inferences from prior review labels.

In the budget calculation, `Z_{a,i}` and `K_{a,i}` denote the running
preactivation and carrier maxima on the common prefix. Retain the source's
recurrence-defined absorption and real Gaussian-moment constants `C_abs`
and `W_G`, and set `eta=min{1,(1024 C_abs W_G)^{-1}}` and
`Bcal=1024 e^2 L`. The source recurrences give
`2 eta K_src<1/100`; this numerical inequality is independent of
`p,m,d,Y` and will control repeated indices in the empirical moments.

Initialization is valid for arbitrary `m,d`. The fitting proof separately
tracks empirical standard deviations and training covariance entries:
`Delta_j<=epsilon+s Delta_{j-1}` and
`E_j<=(2K+1)epsilon+s^2 E_{j-1}+D Delta_{j-1}`. Its matrix error is
at most `m E_L`, while its sphere-net entropy is
`d log(1+2/h_fit)`. Its first-layer operator tail has exponent
`-(8-log 9)n+d log 9`. None of these steps compares `m` with `d`.
The gate in fitting equation (12) is at most

\[
X^{32}\chi^2
\left[dL\log\beta+\log\frac{512L(m+1)^2}{\rho}\right]+1.
\tag{14}
\]

On this event, deleting at most `p` neurons produces initialized feature
discrepancy at most `(8s)^L sqrt(p)(b+s Z_0)`. It preserves all cavity
Gram margins after division by `sqrt(n)`. Fresh-row pairing of projected
lower differences gives the stated tail
`2 exp[-n^{4/5}/(2D_init^2)]`, which pays for all same-layer deletions.
This conditioning is before the fresh row's operator-norm restriction.

The actual local flow uses `bar u=(Theta-Theta_0)/S` and unscaled forward
ports. Since the readout is initially zero, the scaled output is
`bar F=bar u_w^T h^L`. Thus the scaled Taylor coefficients have no
inverse power of `S`. The residual is still the forward residual; the
linearization retains its rank-one port term, the reverse force, the
learned columns/rows, and the top prediction offset multiplying both
retained terms. The effective-network affine map multiplies hidden
directions by `S<=1` and is a contraction. This verifies the transfer
from the fixed-order remainder to the amplitude-scaled remainder.

For the response specifically, the deletion adds the forward response
port `sum_i x_i bar Q_{ba,i}`, the omitted feature-pairing term, and the
direct lower observable in (9). The last observable requires the forward
images of `C_a^T y_i` in the Gaussian event. The nonlinear difference
splits as

\[
(C_b^1-C_b^0)C_a^{0\top}y_i+
C_b^1(C_a^1-C_a^0)^\top y_i.
\]

The first term uses the coordinate-localized reference forward image;
the second uses the lower adjoint-probe estimate. Their common small
factor is `d_0+n^{-1/2}`, not an arbitrary operator difference of the
two Jacobians. Exact gate subtraction propagates through bounded slopes
and perturbed mixers; reference response maxima occur only in additive
terms. It does not multiply a coordinate cutoff once per layer.

With `N=n^{1/100}`, `d_0=n^{-1/10}`, and `u=n^{-1/25}`, the resulting
integrated nonlinear remainder is bounded by

\[
\mathcal A_d\ell^8n^{1/4000}
\left[n^{-0.08}+u^2+n^{-0.48}+n^{-1/2}\right].
\tag{15}
\]

The enlarged Gaussian maps have coefficient at most
`B sqrt(p) n^{1/4000} ell^5`. Their scalar-control speeds contain one
factor `sqrt(n)`; the gate product in the response speed uses the
coordinate maximum of `bar R` and the RMS speed of `z`. This explains
the `n^{5/8}` control-net entropy and avoids a depth-dependent width
power. Section 4 handles their terminal interpolation at random prefixes.

After (16), these maps have operator norm below `n^{1/200}`; their input
has covariance `I/n` in at most `2pn` dimensions. Gaussian coordinate
tails and centered quadratic-form tails at `n^{-1/10}/8` are bounded by
`4 exp(-n^{0.78})`. The Euclidean image mean is below `n^{1/100}/2`.
There are at most `4p(m+1)^2` scalar controls; their logarithmic covering
count is at most `A_d ell^8 n^{5/8}<=n^{0.626}`. The remaining terminal,
coordinate and deletion counts are at most `pL A_d n^{p+9}`.
Since `p,m,d<=n^{1/4000}`, this union together with the root-norm failure
is below `exp(-n^{0.7})<rho/16`. Thus the local event is quantitative
at the confidence-dependent `p`; no limit at fixed `p` is inserted here.

For completeness, (2) implies the two quantitative absorption conditions

\[
\mathcal A_d\ell^{16}\le n^{1/1000},\qquad
n\ge64mL/\rho.
\tag{16}
\]

To verify the logarithmic one, put `v=log(2 A_d)>9000`.
The factorized gate
`[2 A_d (2000 log(2 A_d))^{16}]^{1000}` has logarithm
`1000[v+16 log(2000v)]<=1050v`. At this point `1+log n<=2000v`
and `A_d ell^{16}<=n^{1/1000}/2`. The difference
`log n/1000-16 log(1+log n)` is increasing afterwards. Since
`1050 log(2 A_d)<=1100 log A_d`, (2) dominates this gate. Also
`A_d>=64mL`. No ordering between `m` and `d` enters this arithmetic.

Equations (15)--(16) improve the parameter remainder stop to `u/2`.
The endpoint Taylor estimates then give all retained coordinate
discrepancies below `n^{-1/30}`, including `bar R`. Thus cavity budgets
are at most `exp(2 eta n^{-1/30}) Bcal+p/n<2 Bcal` on the full stopped
prefix, and the doubled coordinate/response bounds and pole gap transfer
strictly. This is a first-exit comparison, not Gaussian conditioning on
full-network survival.

The singleton scalar expansion retains four nonzero means: the lower
forward trace, the upper residual-Hessian trace, the direct port Hessian,
and the adaptive-residual rank-one trace. The compact foundation explicitly
derives these in equation `cp:src-traces`. Normalized Schatten Holder
with the rank-`n` endpoint blocks bounds the first three with the original
source constants; the last is at most
`A_d ell^8 n^{-1+1/4000}`. The finite local error is below `n^{-1/40}`.
The two sample-RMS inequalities have feedback product at most `1/2`,
giving the original `C_abs` scalar absorption. This also explains why
there is no ambient parameter-dimension factor in the traces.

A scalar Gaussian grid then improves the training coordinate maxima.
For `R_{ba}`, the four noncentered coefficients are the direct pairing,
the direct reverse mean, the integrated mixed-endpoint trace, and the
learned incoming row. After division by `S`, these are

\[
sK_{\rm src}H_{j-1}^2,\quad sK_{\rm src}f_{j-1}^2,\quad
sK_{\rm src}ST_Q,\quad
sK_{\rm src}S^2H_{j-1}q_{j-1}.
\]

The centered incoming pairing has coefficient `64 q_{j-1}`. These are
precisely the terms of source equation (17); its factor two improves the
temporary response cap to (10). The `m^2` training pairs are included in
the finite grid count. The resulting exact velocity equation
`dot z_b=-(2/m)sum_a r_a R_{ba}` improves the full pole stop on (2)'s
small rectangle. This order avoids using the improved response estimate
to assume its own complex continuation.

For the budget removal, singleton/common-cavity differences are extended
by their own stops and projected onto the deterministic Euclidean ball
of radius `4n^{1/100}`. Both omit the paired root. Their Gaussian radius
is consequently `v_n=4n^{-49/100}`. The rectangle moment lemma bounds
their exponential moments with

\[
\mu_n\le256v_n\sqrt{\log(e+
X^{400}\chi\ell^4/v_n)}+2v_n,\qquad
p\mu_n+p^2v_n^2<10^{-3}.
\]

The real reference moments are below four per neuron at exponent
`8 eta`; complex-minus-real corrections have `p`th-root moments at most
`exp(X^{-10})` at the radius in (2). The latter follows from the
derivative estimates under provisional response stops and the explicit
Gaussian rectangle lemma, with no inverse label factor. Conditional
independence is used only for the distinct omitted roots of a common
cavity. Cauchy--Schwarz and Holder, rather than independence, handle
corrections and different samples. Dropping the full-event indicator
after this pathwise domination gives

\[
\mathbb E\left[1_E\prod_{i\in I} B_i\right]\le16^{|I|},
\qquad B_i=e^{\eta(Z_{a,i}+K_{a,i}/S)},\quad |I|\le p.
\]

The coordinate cap gives `B_i<=exp(sqrt(ell)/100)`. Classifying repeated
indices in the empirical `p`th moment yields

\[
\mathbb E\left[1_E(n^{-1}\sum_iB_i)^p\right]
\le16^p\exp\left\{\binom p2
\frac{e^{\sqrt\ell/100}}{16n}\right\}\le e16^p.
\]

Here (16) implies `n>=4p^3`, a sufficient collision gate. Markov and the
sample/layer union give budget-hit probability at most
`emL(64e^2)^{-p}<=rho/4`. The other failure allocations in the source
composition are `<rho/4` for initialization, `<rho/16` for local maps,
and `<rho/16` for both maximum events. Their total is `<5rho/8`.

The finite-source proof therefore does not need `m>=d` in an insertion,
trace, or probability step. Alternatively, apply it in dimension `k`
using Section 2: `A_k<=A_d`. If this black-box application supplies only
the reduced sphere fitting event, intersect it with the original ambient
fitting event at failure `rho/32`, whose gate (14) is dominated by (16).
The total failure remains `<21rho/32<rho`. Thus the original `A_d`
gate (2), with unchanged `p` and radius, is sufficient for both the
training source and the ambient real fitting event.

## 6. Real all-time response extension needed by Legendre

No new probability or late-time complex domain is needed here. Fitting
gives, in the Euclidean mobility norm,

\[
\|\theta(t)-\theta(T)\|
\le2Y\lambda^{-1/2}e^{-16\ell},\qquad t\ge T,
\tag{17}
\]

including the limit. The block-sum norm is at most `sqrt(L+1)` times
this. The source's backward-only subtraction bounds the coordinate
increment by `X^{20} n` times (17). This is at most
`S K_src sqrt(ell)` under the polynomial gate
`n^{15}>=X^{20}/8`, using `lambda<=1`, `K_src>=1` and `sqrt(ell)>=1`.
The much stronger gate (2) already implies it. Thus

\[
\max_{a,j,i,t\ge0}|k_{a,i}^{(j)}(t)|
\le2S K_{\rm src}\sqrt\ell
\le32X^{21}(Y/\lambda)\sqrt\ell.
\tag{18}
\]

For the response, use the state at `T` as the fixed reference in (8).
Forward subtraction bounds RMS preactivation differences by `X^5` times
the block-sum parameter difference. Backward subtraction uses

\[
\delta_t-\delta_T=
\phi'(z_t)\odot(k_t-k_T)+
[\phi'(z_t)-\phi'(z_T)]\odot k_T.
\]

Only the reference coordinate cap for `k_T` is needed in the second term.
In the response recursion subtract the feature pairings and the mixer
separately, and use

\[
Q_t-Q_T=\phi'(z_t)\odot(R_t-R_T)+
[\phi'(z_t)-\phi'(z_T)]\odot R_T.
\]

Here the reference coordinate cap (10) multiplies the RMS preactivation
difference. All homogeneous propagation uses the real operator caps and
bounded activation slope. Summing at most `L` terms gives the conservative
RMS Lipschitz coefficient `X^{100} chi^2(1+sqrt(ell))` for both response
families. Conversion to a coordinate maximum now costs only one
`sqrt(n)`. With (17), the response tail is at most

\[
Y X^{103}\chi^3(1+\sqrt\ell)n^{-31/2}.
\tag{19}
\]

For example `n^{31/2}>=2X^{103} chi^2` makes this at most
`Y chi sqrt(ell)`. Gate (2) already implies this polynomial condition.
Combining it with (10) gives the loose all-time bound used in the new
Legendre argument,

\[
\max_{a,b,j,i,t\ge0}|R_{ba,i}^{(j)}(t)|
\le Y X^{110}\chi^3(1+\sqrt\ell).
\tag{20}
\]

Only training inputs appear in (18)--(20). Whole-sphere output comparison
continues to use ordinary real forward subtraction in the ambient
parameter space, including (6)'s frozen orthogonal contribution. No
whole-sphere response maximum is being substituted for a training one.

## 7. Input and claim boundary

Read completely for this dependency: `FULL_FINITE_SOURCE_PROBABILITY.md`,
`WIDTH_GATE_REFINEMENT.md`, `EXPLICIT_FITTING_WIDTH.md`,
`QUANTITATIVE_INSERTION_WIDTH.md`, `FIXED_ORDER_INSERTION_JETS.md`,
`SCALED_INSERTION_REMAINDER.md`, `INSERTION_MAP_MODULI.md`,
`POLYNOMIAL_SOURCE_WIDTH.md`, and `FINITE_COMPLEX_MOMENT_GATE.md` in the
expressly assigned `unseen_query_decoder_20261005` source packet. Required
rigorous-math and canonical-notation skills, including the neural reference,
were read. The scalar trace, coefficient and stopping details were checked
against the allowed `paper/compact_foundations.tex`, through its finite-query
and real carrier-extension proof. The setup in `paper/compact.tex`, the
mobility comparison in `paper/compact_legendre.tex`, and Section 1 of the
new `DENSE_LEGENDRE_ROUTE.md` specify the receiving interface.

No review reports, histories, or additional studies were read. Older
out-of-study references named by these notes were not used as evidence;
the needed scalar trace and stop formulas are present in the allowed
compact foundation. Earlier notes' explicit open statements are retained
at their historical conditional scope; the finite-source composition is
what supplies their missing finite probability estimates.

The positive conclusion is the finite training-source dependency (2),
including the named response, arbitrary `m,d`, the explicit rectangular
interpolation completion, and the real all-time extensions (18)--(20).
This establishes no result for the selected methods, no stronger original
dense lower coefficient, and no claim of practical polynomial degree.
The new Legendre history/defect estimates still require their separate
review. No promotion is requested or performed by this file.
