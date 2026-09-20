# Hash-specific check of the fixed-depth fitting constants

2026-09-20. Scoped mathematical check, not a complete independent C-X3
review or a promotion recommendation.

Reviewed target: `CH4_FITTING_CONSTANTS.md`, complete file.

SHA-256:
`d9e305c82f65860c010a922ae5d016732acadb3010852822488759971a1d8e96`.

The read scope was the complete target plus the scientific inputs already
authorized for this route: CONTRACT.md, CH3_LOCAL_PROOF.md,
docs/NOTATION.md, and maintained global_nonlinear.md B.1 lines 2100–2453,
C.1–C.2 lines 2454–3440, and C.4.5.1 lines 5475–6103. No other route
outputs or studies were consulted. No experiment or numerical evaluation
was used.

**Verdict: the target's stated unconditional and conditional claims pass
this scoped check.** No correction to its fitting constant or gradient
bound is required. Its continuation assumptions remain substantive and
unproved; this verdict does not discharge them.

## 1. Initialization lower bound

For z real, sinh²z>=z² and the increasing map a/(1+a) give
tanh²z>=z²/(1+z²). With Z~N(0,q), q>0, the two factors
|Z|/sqrt(1+Z²) and |Z|sqrt(1+Z²) are square-integrable. Their product
has expectation q. Therefore Cauchy–Schwarz gives

\[
 E\frac{Z^2}{1+Z^2}\ge\frac{q^2}{q+3q^2}
 =\frac q{1+3q}.
\]

Every q_l is positive, so reciprocation is legitimate. Induction yields
1/q_l<=1/q_0+3l=1+3l. No Jensen inequality with the wrong direction,
small-q approximation, or numerical Gaussian estimate is used. The
Gaussian fourth moment supplies the coefficient three exactly.

The orthogonal forward covariance induction is also valid: the first
roots are independent, each new initialized edge is independent of its
lower forward queries, and oddness makes the cross covariance zero.
The resulting pair is jointly Gaussian with diagonal covariance, hence
independent at its own population. Thus m_L=q_L/2 and the lower bound
m_L>=1/[2(1+3L)] are unconditional initialization facts.

## 2. Directional identities and radial argument

The stated map J uses the row L2 metric and the HS metric for each
learned increment. Adjunction produces precisely the signed hidden
gradient, with no extra width or probability-weight factor. Its value
chain rule along a strong raw curve requires only bounded tanh gates,
actual bounded action/adjoint pairs, and strong multiplier continuity.
It does not assume an L2-valued Frechet derivative or differentiate J.

The equations c_ss=JJ*c and b_s=||h||²+||J*c||² therefore hold wherever
the strong feature solution exists. The radial second derivative has
the correct minus sign on g_s². Cauchy–Schwarz proves it nonnegative.
The initial expansion c(s)=s h_0+o(s), together with continuity of h,
gives g_s(0+)=sqrt(m_L). The positive lower bound g>=s sqrt(m_L)
prevents a later zero, which justifies continuing the radial estimate
through every existing positive feature time. Consequently b_s>=m_L.

These facts do not supply local continuation at an arbitrary reached
L2/HS state. The target says so explicitly.

## 3. Physical clock and fixed fitting time

The physical hypothesis includes uniqueness on the initialized carrier.
That permits the swap/sign isometry of the canonical initialized law
to identify the transformed solution, giving f(e_1)=-f(e_2)=b. The
probability-weighted unhalved loss has residuals b-1 and 1-b. Its vector
field is therefore exactly 2(1-b) times the signed feature field.

On a compact strong physical path the scalar coefficient
||h||²+||J*c||² is bounded and continuous. Solving e_t=-2a(t)e with
e(0)=1 gives e(t)>0 at every finite time. Thus feature reparametrization
is valid without assuming in advance that b never reaches one.
Combining it with b_s>=m_L yields loss<=exp(-4m_L t).

For T=2(1+3L),

\[
 4m_LT\ge
 4\frac{1}{2(1+3L)}\,2(1+3L)=4.
\]

Hence the asserted loss bound exp(-4)<1/8 is correct, with strict
slack to 1/4. The time is 20 when L=3. It remains conditional on
existence and uniqueness through that fixed physical horizon, and it
does not rewrite the maintained two-layer constants. No supported-law
radius or finite-network claim is smuggled into this estimate.

## 4. Endpoint and whole-input gradient

The stronger endpoint hypothesis is separately stated: a unique strong
feature solution on the closed interval [0,1/m_L]. Since b(0)=0 and
b_s>=m_L, it has exactly one first level b=1 on that interval. The
bounded upper derivative gives 1-b(s)<=K(s_dagger-s), with the needed
inequality direction for divergence of the physical-clock integral.

The raw length estimate is

\[
 \|\theta(s_2)-\theta(s_1)\|raw^2
 \le(s_2-s_1)\int_{s_1}^{s_2}\|\theta_s\|raw^2ds
 =(s_2-s_1)(b(s_2)-b(s_1)).
\]

Using s_dagger-s<=(1-b(s))/m_L gives the endpoint rate in the target.
Setting s_1=0 also bounds the raw displacement from initialization by
m_L^(-1/2). The initialized action bound two is a maintained Gaussian
action input explicitly cited in C.4.5.1; applying that same bound to
each of finitely many edge labels gives B_L=2+m_L^(-1/2). The gradient
argument works unchanged with any proved initialized action bound,
including the conservative bound ten used in CH3.

For a unit passive input u, its full-row gradient has norm at most
||c||2 B_L^(L-1), because ||u||=1. The l-th middle HS gradient is
Delta_l tensor H_(l-1), so its norm is at most
||c||2 B_L^(L-l), l=2,...,L. The readout gradient has norm at most one.
Adding the squares therefore gives exactly

\[
 1+m_L^{-1}\sum_{j=0}^{L-1}B_L^{2j}.
\]

There is no missing first-row dimension factor or extra middle-layer
factor. A straight raw segment between the state and endpoint retains
the readout and action bounds by norm convexity. The scalar prediction
chain rule integrated over that segment is consequently uniform for
every unit input. It proves the displayed whole-circle estimate, and
indeed the same calculation holds on the whole unit sphere if the
reference is embedded with the full first row retained.

The endpoint is characterized by this feature trajectory and its first
b=1 level. The target correctly avoids uniqueness among arbitrary
interpolating predictors, a perturbed-law endpoint, or one radius valid
for all physical horizons.

## 5. Exact scope of this check

The only unconditional quantitative addition is the initialization lower
bound. The remaining statements are valid implications under their
separately stated physical or feature continuation assumptions. This
check does not establish those assumptions, backward tails, actual GF/GD
capture through fitting, or the common executable closure. No defect
was found in the checked implication.
