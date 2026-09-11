# P2: reached row tails and the missing changed-law cavity estimate

Author: `/root/p2_reached_tails`, independent scoped author attempt, 2026-09-11.
Status: **partial**. The finite deterministic estimates in §§2–3 are proved
below. Sections 4–6 prove a conditional route from one explicitly unproved
finite exponential-query estimate to continuation and a uniform nonlinear
response remainder. Section 7 identifies the failed step in extending the
reference column argument. The required changed-law exponential-query estimate
is **open in this attempt**. No unconditional population continuation through
40, or nonlinear contamination remainder, is claimed.

This report was frozen before its substantive findings were communicated to
the supervisor. It is a study result, not established material or a promotion
review. No training experiment, Git mutation, or other-study retrieval occurred.

## 1. Contract and notation

The network has two hidden width-n tanh layers, no biases, normalized input
u=x/sqrt(2) on S¹, labels in [-Y,Y], Y≥1, independent Gaussian stored
initial variances (1,1/n,1/n²), and block mobilities (n,1,n). The finite
readout is its actual Gaussian array. The loss is the **unhalved** exactly
integrated squared loss for every deterministic Borel training law μ; there
is no sampling or quadrature restriction in the finite dynamics. Set T=40;
formulas below also hold for any separately fixed finite positive T.

Write w=W¹, A=A₀+K=W², c=W³, φ=tanh, and

\[
 h(u)=\phi(w\cdot u),\quad z(u)=Ah(u),\quad H(u)=\phi(z(u)),
 \quad\delta(u)=c\phi'(z(u)),\quad Q(u)=A^*\delta(u),
 \quad r(u,y)=\langle c,H(u)\rangle-y.
 \tag{1}
\]

In a finite formula the adjoint is the actual transpose, scalar pairings
are divided by n, and a rank q⊗h is qhᵀ/n. A first-row or readout L² norm
becomes its Euclidean/Frobenius norm divided by sqrt(n); a middle HS norm
becomes its ordinary Frobenius norm. Comparisons never subtract objects
on different carriers. Only K, not A₀, is Hilbert–Schmidt.

The raw square norm of an increment is

\[
 \|(v,B,d)\|_{\rm raw}^2
   =\|v\|_2^2+\|B\|_{HS}^2+\|d\|_2^2.
 \tag{2}
\]

We sometimes use the equivalent sum of these three norms, denoted d. The
reference is ν*=½δ_(e₁,+1)+½δ_(e₂,-1) in normalized input notation.
Its strong full-row reference, Gaussian action and adjoint, endpoint, and
linear clock response are those in the assigned C.4.5–C.4.6/P1 inputs.
The target is a genuine neighborhood

\[
 \mathcal U_\rho=\{\mu:\mathcal W_1(\mu,\nu_*)<\rho\},\qquad\rho>0,
 \tag{3}
\]

where the transport cost is |u-v|+|y-y'| and μ ranges over all Borel
probability laws. For response, μ_ε=(1-ε)ν*+εν, σ=ν-ν*, with **every**
Borel probability ν on the observation space and constants independent of ν.
As its diameter is D_Z=2+2Y, all these μ_ε lie in (3) for
0≤ε<ρ/D_Z. The reference law is orthogonal; the laws in (3) need not be.

## 2. Uniform finite bounds that do not need a tail theorem

The exact physical equations are

\[
 \dot w=-2\int r\phi'(w\cdot u)Q(u)u\,d\mu,\qquad
 \dot K=-2\int r\delta(u)\otimes h(u)\,d\mu,\qquad
 \dot c=-2\int rH(u)\,d\mu.
 \tag{4}
\]

They retain every learned rank and both orientations of the same A₀.
Use the initialization event

\[
 E_n=\{\|A_{0,n}\|_{op}\le10,\ \|c_{0,n}\|_\infty\le1,
                         \ \|g_n\|_F/\sqrt n\le2\}.
 \tag{5}
\]

Its probability tends to one by the assigned Gaussian operator bound,
the iid second-moment law, and
P(max_j|c₀,j|>1)≤2n exp(-n²/2). It depends on initialization only.

Put l=Y+1 and

\[
 B=10+l\sqrt T,\quad C=1+l\sqrt T,\quad W=2+l\sqrt T,
 \quad H_c=1+2lT,\quad R=C+Y.
 \tag{6}
\]

On (5), for **every** law μ and all t≤T,

\[
 \mathcal L_{n,\mu}(t)\le l^2,\quad
 \|A\|_{op}\le B,\quad \|K\|_F\le l\sqrt T,\quad
 \|c\|_2/\sqrt n\le C,\quad \|w\|_F/\sqrt n\le W,
 \quad \|c\|_\infty\le H_c.
 \tag{7}
\]

Proof: at time zero |f(u)|≤1 for every u, so the loss is ≤l².
Differentiating the exactly integrated finite loss gives

\[
 \mathcal L(t)+\int_0^t
 \left(\|\dot w\|_F^2/n+\|\dot K\|_F^2+\|\dot c\|_2^2/n\right)ds
 =\mathcal L(0).
 \tag{8}
\]

Differentiation under μ is permitted on each finite-dimensional compact
parameter set because the integrand and its derivatives are continuous
and uniformly bounded there over compact (u,y). Cauchy–Schwarz bounds each
block displacement by l sqrt(T). Also ∫|r|dμ≤sqrt(𝓛)≤l and
|ċ_j|≤2∫|r|dμ, giving the last bound in (7). These bounds exclude finite
escape by the finite-dimensional local integral contraction argument and
its Cauchy endpoint extension. In particular all finite GFs used here
exist through T for arbitrary Borel μ.

The passive queries have deterministic Hilbert-space regularity:

\[
 \|\dot w\|_F/\sqrt n\le2lBC,\quad
 \|\dot K\|_F\le2lC,\quad \|\dot c\|_\infty\le2l,
\]
\[
 \|\partial_t z(u)\|_2/\sqrt n\le2lC(1+B^2),\quad
 \|\partial_t\delta(u)\|_2/\sqrt n
       \le D_t:=2l+4lH_cC(1+B^2),
\]
\[
 \|\delta(t,u)-\delta(t,v)\|_2/\sqrt n
       \le D_u|u-v|,\qquad D_u=2H_cBW.
 \tag{9}
\]

For example, differentiate z=Ah, use |φ'|≤1 and (4); next differentiate
δ=cφ'(z), using |φ''|≤2 and c's supremum bound. For the input difference
use ||w·(u-v)||₂≤||w||_F|u-v|, then the bounded action and the upper gate.
No input derivative moment or independent-current-query assertion is used.

The learned increment has an additional bounded-coordinate property:

\[
 |nK_{ji}(t)|\le2lH_cT,
 \qquad |(K(t)^T\delta(t,u))_i|\le2lTC^2.
 \tag{10}
\]

Indeed integrate (4) entrywise for the first estimate. For the second,

\[
 (K(t)^T\delta(t,u))_i
 =-2\int_0^t\int r(s,v,y)h_i(s,v)
                \langle\delta(s,v),\delta(t,u)\rangle\,d\mu\,ds,
\]

and use |h_i|≤1, ||δ||₂/√n≤C and ∫|r|dμ≤l. For any existing strong
population trajectory with the same bounds, K is the integral operator
with kernel obtained by the same time/law integral, bounded by 2lH_cT
on Ω₂×Ω₁. Fubini applies to its bounded measurable integrand. Thus K
also maps L¹ to L∞ there. This does **not** improve the initial A₀ action.

## 3. A reached first-row fourth moment from tanh saturation

This improvement needs only (7), not any higher-moment action bound.
For every finite row i set

\[
 J_i=\int_0^T\int |r(s,u,y)|\,|Q_i(s,u)|\,d\mu\,ds.
\]

Then, pathwise on (5),

\[
 \sup_{t\le T}|w_i(t)|^2\le |g_i|^2+2J_i,
 \quad \left(\frac1n\sum_iJ_i^2\right)^{1/2}\le TlBC,
 \tag{11}
\]
\[
 \left(\frac1n\sum_i\sup_{t\le T}|w_i(t)|^4\right)^{1/2}
 \le\left(\frac1n\sum_i|g_i|^4\right)^{1/2}+2TlBC.
 \tag{12}
\]

To prove (11), use cosh²z=1+sinh²z≥1+z²≥2|z|, so
|z|φ'(z)≤½. The exact radial identity from (4) is

\[
 \frac d{dt}|w_i|^2
 =-4\int r Q_i(w_i\cdot u)\phi'(w_i\cdot u)\,d\mu
 \le2\int|r|\,|Q_i|\,d\mu.
 \tag{13}
\]

Integrate it. Minkowski, ||Q(u)||₂/√n≤BC, and ∫|r|dμ≤l give the
second bound in (11). Minkowski applied to the square of the row length
gives (12). Since E|g_i|⁴=8 for a two-dimensional standard Gaussian,

\[
 \sup_{n,\mu}\mathbb E\left[1_{E_n}\frac1n\sum_i
                   \sup_{t\le T}|w_i(t)|^4\right]
 \le16+8T^2l^2B^2C^2.
 \tag{14}
\]

The deterministic inequality (12) is simultaneous over μ on (5).
The same argument applies to any already existing strong population flow:
the L²-in-time speed and Fubini give absolutely continuous coordinate
representatives, to which (13) applies. That statement does not construct
such a flow beyond its current existence interval.

The exponent four in (14) is substantive: the raw energy estimate alone
only controls a second moment. It is still insufficient for cosh²(w_a)Q
or for a first-order nonlinear remainder. Polynomial moments do not
justify multiplication by exponential inverse-gate weights.

## 4. A sufficient finite reached-query hypothesis

The following is the unresolved quantitative input for this route.
It is weaker in tail exponent than the subGaussian reference estimate.

**Hypothesis E(ρ,T).** There are γ>0 and M<∞, depending on Y,T,ρ but
independent of n and μ, such that, for the actual finite GF,

\[
 N_{n,i,\mu}=\sup_{t\le T,u\in S^1}|Q_{n,i,\mu}(t,u)|,
\qquad
 \sup_{n\ge1}\sup_{\mu\in\mathcal U_\rho}
 \mathbb E\left[1_{E_n}\frac1n\sum_i e^{\gamma N_{n,i,\mu}}\right]
 \le M.
 \tag{E}
\]

The law supremum is outside expectation. This does not request a supremum
over data laws inside the random event. It does include every fixed Borel
law, the true learned flow, full-circle passive queries and actual finite
Gaussian readout. A separately established pointwise-in-(t,u) version,
with suitable integrated tails and moduli, could be enough; (E) is one
clean sufficient lemma, not claimed necessary.

Here are its consequences, proved without an Lp bound on A₀.
Since J_i≤Tl N_i, (11) implies

\[
 \sup_t|w_i(t)|^2\le |g_i|^2+2TlN_i.
 \tag{15}
\]

Choose 0<η≤min(1/8,γ/(8Tl)). Regard initialization and the uniform
choice of coordinate i as one probability space. Hölder and (E) give

\[
 \mathbb E\left[1_{E_n}\frac1n\sum_i
       e^{\eta\sup_t|w_i(t)|^2}\right]
 \le (1-4\eta)^{-1/2}M^{1/2}.
 \tag{16}
\]

Indeed E exp(2η|g_i|²)=(1-4η)^(-1), and
4ηTl≤γ. Dependence between g and N is harmless under Hölder. In
particular for every separately fixed p<∞,

\[
 \sup_{n,\mu\in\mathcal U_\rho}
 \mathbb E\left[1_{E_n}\frac1n\sum_i
 \sup_{t,u,a}\{\cosh^2(w_{ia}(t))|Q_i(t,u)|\}^p\right]<\infty.
 \tag{17}
\]

For a direct check, cosh²w_a≤exp(2|w|), apply Hölder to its product
with N, use 4p|w|≤η|w|²+4p²/η, and use every polynomial moment
of N supplied by its exponential moment. Any fixed polynomial product
with |w|, N, or this weighted query has the same conclusion. Thus (17)
supplies actual finite weighted square uniform integrability by
V²1_(V>L)≤V^p/L^(p-2), p>2, then Markov.

### 4.1 Why exponential tails already suffice for raw continuation

Under (E) the same-carrier raw comparison of C.4.1 holds with HS in place
of operator distance. Its proof uses the same rank difference bound in
both norms. On a common finite state/readout bound its only unbounded
reference factor is Q, and it gives

\[
 \|F_\mu(\theta)-F_\lambda(\bar\theta)\|_{\rm sum}
 \le L(1+R_0)\{d(\theta,\bar\theta)+\mathcal W_1(\mu,\lambda)\}
       +L\,\tau_{R_0}(\bar Q),
 \tag{18}
\]

with the individual reference-input tails integrated against λ. On
the reference actual finite path those tails are bounded by the empirical
N-envelope. For R₀≥1,

\[
 \mathbb E\left[1_{E_n}\frac1n\sum_i
                    N_i^2 1_{N_i>R_0}\right]
 \le C_{\gamma,M}e^{-\gamma R_0/2}.
 \tag{19}
\]

Hence the expectation of their RMS is at most C exp(-γR₀/4).
On a time slab of length τ with Lτ<γ/8, Gronwall amplifies a tail by
at most exp(L(1+R₀)τ); its expected contribution therefore tends to zero
as R₀→∞. This is why one must subdivide time for exponential tails.
Using a single fixed cutoff through all T and assuming its exponential
beats exp(LTR₀) would be incorrect.

For completeness the construction using this estimate is as follows.
For a fixed finite law, compare its actual finite GF with its raw Euler
scheme on the same arrays. Every finite-horizon Euler state has deterministic
bounds on (5): the readout recursion obeys c_(k+1)≤c_k+2h(c_k+Y),
then the middle and row bounds follow successively from bounded tanh.
Thus the Euler and GF comparison uses one fixed enlarged ball. Its
assigned-velocity defect is controlled by (18), the Euler state increment
O(h), and (19). On the first short slab take h→0 at fixed cutoff, then
remove the cutoff. Induct over finitely many slabs; at each next slab the
initial comparison error has already tended to zero. This proves

\[
 \lim_{h\downarrow0}\limsup_{n\to\infty}
 P\{\sup_{t\le T}d_n(\theta^{GF}_{n,\mu}(t),
                         \theta^{h}_{n,\mu}(t))>a\}=0.
 \tag{20}
\]

At each fixed finite-law mesh, A.1/III.F identifies its generated node
tuples and learned-rank HS contractions. The readout can be clipped outside
its proved mesh bound. Its actual initialized Gaussian readout differs
from its zero limiting root by vanishing RMS and supremum; finite-node
subtraction transfers it as in P1. Apply (20) to two fixed meshes and
use their joint finite-program limit: their canonical population state
distance is the limit of the same finite state distance, including HS
rank contractions. A nonvanishing canonical distance would contradict
the probability bound in (20). Thus the canonical mesh paths are Cauchy.

Their limit satisfies (4): bounded-multiplier continuity, bounded actions,
and continuous rank integrands pass the integral equation to the strong
raw limit. The c supremum bound passes by closedness in L². At a fixed
finite set of times and passive inputs, bounded tests of the jointly
identified GF fields transfer (E); monotone convergence over finite
countable parameter lists gives a population envelope N# with the same
exponential moment. L² continuity extends domination from the countable
set to every fixed passive-input equivalence class, exactly as in P1's
source passage. This needs no coordinate-continuous population Q process.

For law completion, approximate each μ∈Uρ by finite laws remaining in
Uρ. The same slab argument (18)–(19) gives a uniform modulus tending to
zero with their W₁ distance. It proves Cauchy convergence, independence
of the approximating laws, and the strong equation via uniform continuity
of its compact-domain integrands. For uniqueness compare any other
continuous strong solution with this constructed tail-controlled one;
choose a ball containing both compact paths and repeat the small-slab
argument with zero initial and law discrepancy. No tail premise on the
other solution is needed. The same argument gives restart along the
constructed interval. These steps prove **conditionally on (E)** strong
existence and uniqueness on [0,T] throughout the genuine neighborhood.

## 5. Weighted source continuity on the resulting reached family

Continue to assume (E), and use the population family just constructed.
For each row coordinate introduce the exact clock

\[
 F(z)=z/2+\sinh(2z)/4,\qquad X_a=F(w_a)-F(g_a),
 \quad w_a=j(X_a,g_a),\quad j_X=\phi'(j).
 \tag{21}
\]

Equations (16)–(17) show that X and its velocity belong to L².
Coordinatewise scalar differentiation and Fubini therefore identify its
strong integral equation. For a general μ its first block is exactly

\[
 \dot X_a=-2\int r u_a\cosh^2(w_a)\phi'(w\cdot u)Q(u)\,d\mu.
 \tag{22}
\]

There is no reference clock cancellation in (22). Define G_σ(θ) by the
same three transformed integrands integrated against σ. The first is
the integrand in (22); the other two are those in (4). By (17),

\[
 \sup_{\theta\text{ reached},\,\nu}\|G_{\nu-\nu_*}(\theta)\|_
 {L^2\oplus HS\oplus L^2}<\infty.
 \tag{23}
\]

Here θ ranges over t≤T and μ∈Uρ, and ν ranges over **all** probability
laws. This passive-query uniformity is needed: controlling only a μ-average
would cost 1/ε when extracting a ν-average from μ_ε.

There is also a uniform modulus. For two reached states on the common
carrier, at the same or different times and laws, let d be their raw sum
distance. For 0≤d≤1,

\[
 \sup_\nu\|G_{\nu-\nu_*}(\theta)-G_{\nu-\nu_*}(\bar\theta)\|
                  \le C_0 d^{1/3}.
 \tag{24}
\]

Here all constants are uniform on the specified reached family, not on
arbitrary raw balls. Details of the weighted step follow. Ordinary factor
subtraction with bounded c gives ||Q(u)-Q̄(u)||₂≤C d, uniformly in u.
Both Q fields have bounded L⁸ moments, so Hölder interpolation yields
||Q-Q̄||₄≤||Q-Q̄||₂^(1/3)||Q-Q̄||₈^(2/3)≤C d^(1/3).
The same interpolation gives ||w-w̄||₄≤C d^(1/3).
Put b_a(w,u)=cosh²(w_a)φ'(w·u). The scalar mean value formula gives

\[
 |b_a(w,u)|\le e^{2|w|},\qquad
 |b_a(w,u)-b_a(\bar w,u)|
       \le C e^{2(|w|+|\bar w|)}|w-\bar w|.
\]

Consequently

\[
 \|b_a(w,u)(Q-\bar Q)\|_2
 \le\|e^{2|w|}\|_4\|Q-\bar Q\|_4\le C d^{1/3},
\]
\[
 \|(b_a(w,u)-b_a(\bar w,u))\bar Q\|_2
 \le C\|e^{2(|w|+|\bar w|)}\bar Q\|_4
            \|w-\bar w\|_4\le C d^{1/3}.
\]

All weight-product L⁴ norms here follow from (16)–(17) and Hölder,
without independence. Residual differences are O(d), their magnitudes
are bounded, and the other two integrands have ordinary Lipschitz
differences. Integrating against a signed measure of mass ≤2 proves (24).
The same reasoning with input and time differences proves joint continuity
and Bochner integrability. No Lp estimate for A₀ has been used.

## 6. Conditional uniform first-order nonlinear remainder

This section proves why (E) would give the desired o(ε), rather than
merely a conditional O(ε) state displacement.

Let Θ=(X,K,c) and let F₀ denote the clock field for ν*. At **every**
state its two active row gates cancel because the data remain e₁,e₂:

\[
 (F_0)_{{X_a}}=-r_aQ(e_a).
 \tag{25}
\]

This structural identity for F₀ is used only for F₀. The actual perturbed
equation is

\[
 \dot\Theta_\varepsilon=F_0(\Theta_\varepsilon)
       +\varepsilon G_\sigma(\Theta_\varepsilon),\qquad
 \Theta_\varepsilon(0)=\Theta_*(0).
 \tag{26}
\]

On the reached action/L² bounds and a common readout supremum bound, F₀
is Lipschitz in the clock/HS/L² sum norm. To verify this, |j_X|≤1
bounds lower feature differences, action subtraction bounds upper ones,
||cφ'(z)-c̄φ'(z̄)||₂≤||c-c̄||₂+2||c̄||∞||z-z̄||₂
bounds the upper backward difference, and bounded A,A* and the HS rank
difference bound complete all three blocks. In particular the reference
row no longer multiplies a row increment by Q. Equation (23), subtraction
of (26) from the reference equation and Gronwall give

\[
 \sup_{\nu}\sup_{t\le T}\|\Theta_\varepsilon(t)-\Theta_*(t)\|
                                    \le C_1\varepsilon.
 \tag{27}
\]

The derivative of F₀ along fixed clock directions at Θ*(t) is exactly
the bounded operator 𝓛(t) in P1/C.4.6. This is a directional derivative,
not an ambient Fréchet assertion. Let v_σ solve the P1 linear equation

\[
 \dot v_\sigma=\mathcal L(t)v_\sigma+G_\sigma(\Theta_*(t)),
 \qquad v_\sigma(0)=0.
 \tag{28}
\]

Its forcing is the stated full-row inverse-gate forcing, and its readout
is the established population limit of the actual finite derivative.

The family {v_(ν-ν*):ν probability} is relatively compact in
C([0,T];V), where V=L²(row)⊕HS⊕L²(readout). Indeed the P1 weighted
source is jointly continuous in (t,u,y), so the map
z↦[t↦b(t,z)] has compact range in C([0,T];V). Its probability integrals
belong to the closed convex hull of that compact range. That hull is
compact: a finite ε-net reduces its convex combinations to the compact
convex hull of finitely many points, within ε in norm. The bounded linear
solution map b↦∫₀ᵗU(t,s)b(s)ds preserves relative compactness. Subtracting
the single reference forcing changes none of this reasoning.

For any compact set of such directions and compact reference times,
the fixed-direction differentiation is uniform:

\[
 \sup_{t,\nu}\|F_0(\Theta_*(t)+\varepsilon v_\sigma(t))
  -F_0(\Theta_*(t))-\varepsilon\mathcal L(t)v_\sigma(t)\|
                                      =o(\varepsilon).
 \tag{29}
\]

Here is the product justification. For j and φ the difference quotient
is a bounded multiplier times its fixed direction, and that multiplier
converges in probability to its scalar derivative. Truncating the fixed
L² direction proves strong convergence. The proof remains uniform over
compact sets by finite L² nets and the uniform multiplier bounds. Matrix
increments use bounded actions and the HS inequality. In the upper
backward field cφ'(z), the additional term is εd[φ'(z+Δz)-φ'(z)];
after division by ε it tends to zero by the same compact-direction
multiplier argument. The reference c is bounded, so the other derivative
term is an L² field. Rank and residual product terms are treated by
Cauchy–Schwarz. This verifies (29) for every constituent of F₀.

One must still handle that Θ*+εv may have unbounded readout. Choose a
fixed cap H'>H_c+10+1 and clip only that comparison readout to [-H',H'].
Its discrepancy from the unclipped readout is bounded by

\[
 \varepsilon\|d_\sigma(t)
          1_{|d_\sigma(t)|>(H'-10)/\varepsilon}\|_2
                         =o(\varepsilon)
 \tag{30}
\]

uniformly in t,ν, since compact L² families have uniformly vanishing
square tails. At fixed X,K the F₀ difference caused by changing c is
Lipschitz on bounded L² readout sets: Q is linear in c, r is affine,
and the finite products are bounded using their L² norms. Combining this
with F₀'s Lipschitz estimate for the two capped readouts gives

\[
 \|F_0(\Theta_\varepsilon)-F_0(\Theta_*+\varepsilon v_\sigma)\|
 \le L\|\Theta_\varepsilon-\Theta_*-\varepsilon v_\sigma\|
                                                   +o(\varepsilon).
 \tag{31}
\]

Thus no L∞ bound on the P1 tangent readout was inserted.
Use (27), |j_X|≤1 and (24) in (26): the forcing change has size
ε C||Θ_ε-Θ*||^(1/3)=O(ε^(4/3)). Subtract the integrated equation
for Θ*+εv_σ, use (29)–(31), and apply the scalar integral inequality.
It yields

\[
 \sup_{\nu}\sup_{t\le T}
 \|\Theta_\varepsilon(t)-\Theta_*(t)-\varepsilon v_\sigma(t)\|_V
                                           =o(\varepsilon).
 \tag{32}
\]

Finally convert to raw coordinates. The first conversion error from (32)
is no larger in L² because |j_X|≤1. The Taylor remainder of
j(X*+εξ,g) along the compact row-direction family is o(ε) in L² by
the same bounded-multiplier proof. Hence

\[
 \sup_\nu\sup_{t\le40}
 \|\theta_{\mu_\varepsilon}(t)-\theta_*(t)
       -\varepsilon((\phi'(w_{*,a})\xi_{\sigma,a})_a,B_\sigma,d_\sigma)
 \|_{\rm raw}=o(\varepsilon).
 \tag{33}
\]

Equation (33) is a **conditional conclusion requiring (E)**. Compactness
of the linear forcing family, by itself, supplies neither (23) nor (27)
for nonlinear changed-law trajectories. It cannot remove that premise.

## 7. The exact column-removal bottleneck

The P1 cavity is still a useful finite comparison. For a fixed row i in
population one let a_i=A₀e_i, and replace only the initialized matrix by
Ã₀=A₀-a_ie_iᵀ. Run the full changed-law GF with the same μ,g,c₀;
retain every learned rank and the actual cavity residuals. The resulting
cavity is independent of a_i conditional on the remaining initialized
variables. Its good event E_n^i is (5) with Ã₀ instead of A₀; E_n⊂E_n^i.

The deterministic bounds (7)–(9) hold for both flows. Thus

\[
 Z_i(t,u)=a_i^T\widetilde\delta(t,u),\qquad
 Z_i^\#=\sup_{t\le T,u}|Z_i(t,u)|
\]

is a conditional centered Gaussian process whose variance is ≤C² and
whose increment standard deviation is bounded by
D_t|t-s|+D_u|u-v|. Applying the contained dyadic-grid Gaussian maximum
proof in P1.S29–S33 on E_n^i gives

\[
 \|1_{E_n}Z_i^\#\|_{L^p}
 \le64(C+TD_t+2\pi D_u)\sqrt p,
 \qquad p\ge2.
 \tag{34}
\]

The constant is independent of μ and its support. Gaussian conditioning
is performed on E_n^i, not on the column-dependent E_n.

Let

\[
 d_i(t)=\|w-\widetilde w\|_F/\sqrt n
       +\|K-\widetilde K\|_F+\|c-\widetilde c\|_2/\sqrt n,
 \quad m_i=\|a_i\|_2.
\]

Forward subtraction and bounded c give, uniformly in passive u,

\[
 \|\delta(u)-\widetilde\delta(u)\|_2/\sqrt n
 \le C_d\{d_i(t)+m_i/\sqrt n\},\quad C_d=1+2H_c(B+1).
\]

Since Q_i=a_iᵀδ+(Kᵀδ)_i, (10) and m_i≤10 on E_n imply

\[
 N_{n,i,\mu}\le Z_i^\#+10C_d\sqrt n\sup_{t\le T}d_i(t)
                           +100C_d+2lTC^2.
 \tag{35}
\]

Therefore the following specific sensitivity lemma would imply (E):

\[
 \sup_{n,i,\mu\in\mathcal U_\rho}
 \left\|1_{E_n}\sqrt n\sup_{t\le T}d_i(t)\right\|_{L^p}
                       \le C_{\rho,T}p\quad(p\ge2).
 \tag{CAV}
\]

Indeed (34)–(35) give ||1_E N_i||p≤C'p. Expand exp(γN_i) into
nonnegative terms; k!≥(k/e)^k makes the k-th term ≤(γeC')^k for
k≥2. Choose γeC'<1/2 and bound the first two terms separately.
Averaging coordinates yields (E). This is a finite reached-sensitivity
problem with measurable cavity coefficients and a normalized O(n^-1/2)
state displacement, rather than a hypothetical Lp action estimate.

**CAV is not proved.** The precise raw equation term missing from P1's
reference calculation is exposed by the identity, for a same input u,

\[
 \phi'(w\cdot u)Q-\phi'(\widetilde w\cdot u)\widetilde Q
 =\phi'(w\cdot u)(Q-\widetilde Q)
  +[\phi'(w\cdot u)-\phi'(\widetilde w\cdot u)]\widetilde Q.
 \tag{36}
\]

All remaining raw difference terms are bounded by C d_i plus the small
forward insertion m_i/√n and reverse insertion Z_i/√n. The second term
in (36), however, gives the unresolved contribution

\[
 2\int |\widetilde r(u,y)|
 \|[\phi'(w\cdot u)-\phi'(\widetilde w\cdot u)]
                                       \widetilde Q(u)\|_2/\sqrt n\,d\mu.
 \tag{37}
\]

A cutoff bounds it by C R₀d_i plus the cavity Q tail. A pointwise norm
bound instead uses max_j,u|Q̃_j(u)|, which is not width independent.
The fourth moment (14) does not control the product with a normalized
cavity deviation. In reference clocks (37) cancels only for active
e₁,e₂. For general μ, differentiating the ratio in (22) produces the
uncontrolled weighted multiplication again. P1.S24 consequently cannot
be reused with the same constant for correlated laws.

These failures do not refute E or CAV. They identify the extra reached
weighted-response argument needed to prove either one. A bound on CAV
with constants growing arbitrarily fast in p would not imply (E).

## 8. Adversarial checks and limits of the route

* **All-law quantifiers.** Every unconditional finite bound uses only the
  exact integrated loss and compact label/input bounds. Cavity constants
  are independent of atom number, weights and Gram rank. E and CAV retain
  precisely those quantifiers; no finite sample restriction is hidden.
* **No cancellation transfer.** Formula (22) is used for changed laws;
  cancellation is used only in the separated reference operator (25).
  Small ε multiplies an unbounded source, so its smallness alone does not
  establish (23).
* **Absolute tails versus relative errors.** Reference comparison gives
  small raw distance, but a small L² error can be concentrated on rare
  coordinates. For an unbounded Gaussian weight e^(2G), take
  v_M=a_M 1_(M<G<M+1)/sqrt(P(M<G<M+1)). Then ||v_M||₂=a_M
  while ||e^(2G)v_M||₂≥e^(2M)a_M. Thus raw smallness alone controls
  no inverse-gate source. This is an ambient multiplication obstruction,
  not a counterexample to the actual reached neural flow.
* **Lp action.** Every action use in the proved parts is L² boundedness.
  Higher moments in §§4–6 are conditional moments of actual query fields;
  they are not deduced from A₀:Lp→Lp.
* **Compact linear family.** Its role in (29) is uniform consistency along
  the specified response family. It does not imply that a nonlinear
  L²-valued activation map is Fréchet differentiable on an ambient ball.
* **Finite versus population.** Equations (7)–(14) hold for actual finite
  GF. Equations (32)–(33) describe the nonlinear population family only
  after the conditional construction. No raw-GD derivative/remainder,
  simultaneous ε/width limit, finite-width nonlinear rate, or claim
  uniform over all physical time is asserted.
* **No empirical conclusion.** No training experiment was run. Formula
  (14) and the conditional implications are analytic, and do not claim
  that the required exponential-query estimate was observed numerically.

The smallest high-leverage next obligation for this route is CAV or a
weaker sufficient reached-query tail estimate. Directly iterating the
reference Lipschitz cavity bound fails at (37); replacing it by an
assumed all-Lp action bound would change the problem.

## 9. Input coverage, provenance, and checks

The explicit assignment allowed only docs/NOTATION.md, established
global-nonlinear C.4.1–C.4.6 and their invoked established dependencies,
and frozen P1_SECTION.md, P1_DEPENDENCIES.md, P1_MANIFEST.json. No study
README, study history, prior reviews, other P2 attempt or other study
scientific file was opened. Global Git status was inspected as metadata
only; concurrent paths were not opened or modified.

Read completely:

* AGENTS.md (47 lines); RESEARCH_WORKFLOW.md (224 lines).
* `/etc/codex/skills/solve-math-rigorously/SKILL.md`;
  `/etc/codex/skills/investigate-conjectures/SKILL.md` and its
  research-contract, adversarial-audit, proof-search-orchestration references.
* docs/NOTATION.md (98 lines).
* P1_SECTION.md (2062 lines), P1_DEPENDENCIES.md (3238 lines),
  P1_MANIFEST.json (83 lines). Truncated tool output was repaired by
  smaller overlapping reads before this report was written.
* Live docs/global_nonlinear.md C.4 introductory statement and C.4.1–6,
  lines 3836–8959. Duplicated complete proof bodies were read from the
  frozen packet and checked byte-for-byte as described next. Also read
  the complete C.2 weighted proof, live lines 2924–3440, when testing
  whether its local cap mechanism could extend this route.

The full frozen dependency packet contains docs/README.md:1–273,
NOTATION.md:1–98, finite_dynamics.md:1–227,
special_data_limits.md:3785–4326 (complete III.F), and
global_nonlinear.md:1840–2453 (complete A/B.1), :3972–4296,
:5465–6585 in the frozen edition. These were read in full, including
proof bodies. A Python exact-content check confirmed every scientific
dependency excerpt occurs unchanged in the live established sources.
The frozen README excerpt does not occur unchanged in current README;
its navigation is not a scientific dependency used by the derivations.
The live C.4.6 substring equals P1_SECTION.md byte-for-byte. Live line
offsets for the two last global excerpts are +4 relative to the frozen
packet. No unprovided scientific dependency was imported.

Hashes observed before report writing:

| Input | SHA-256 |
|---|---|
| AGENTS.md | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| RESEARCH_WORKFLOW.md | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| docs/NOTATION.md | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| docs/global_nonlinear.md | `3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf` |
| P1_SECTION.md | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| P1_DEPENDENCIES.md | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| P1_MANIFEST.json | `f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d` |

The mathematical checks were the explicit radial inequality (13), the
normalization in (8)/(10), Hölder/exponential moment calculation (16),
the small-time-slab condition in (19)–(20), the source product estimates
leading to (24), compact-family linearization with readout clipping in
(29)–(31), and the explicit uncanceled term (37). No external specialized
theorem is invoked. The Gaussian maximum argument and fixed-program
proofs are the complete assigned dependencies, not citations to unseen
papers. This is an author check, not an independent acceptance review.

Initial HEAD was `96e02035386b24d058b623dcd53186ff5afbca45`; the pre-edit
metadata check found concurrent HEAD `ae37dfe5400cc4fbc1c260e29272b7667a92ab87`
and an empty index. Neither change was made by this author. Only this
assigned report and its assigned generated scratch namespace are writable
outputs of the attempt. No Git commit was made.
