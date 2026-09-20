# Explicit fixed-depth fitting constants: conditional continuation theorem

2026-09-20, supervisor derivation. This proves an initialization bound and
conditional fitting/endpoint estimates. It does not construct the required
long-horizon population flow or its supported-law neighborhood. The distinction
is essential: this file alone does not complete CONTRACT §4.

Scientific inputs: CONTRACT.md; CH3_LOCAL_PROOF.md; maintained
docs/global_nonlinear.md C.1–C.2 and complete C.4.5.1 (R1–R37 and certificate).
The finite-depth directional chain rule is the one already justified in the
local proof from maintained A.4/III.F.9–10. No other study or new external
theorem is used. This is author theory, without numerical experiments.

## 1. An elementary initialization bound

Let G be standard normal, q_0=1, and

    q_l = E tanh²(sqrt(q_(l-1)) G),       l=1,...,L.

At the orthogonal two-anchor initialization, the two preactivations at each
layer are independent centered Gaussians of variance q_(l-1). Induction proves
this: the first two roots are independent standard normals; oddness gives
zero preceding cross covariance; the next independent initialized matrix's
forward Gaussian law therefore has covariance q_(l-1) I_2. Consequently,
for h_0=(H_L(e1)-H_L(e2))/2,

    m_L = ||h_0||² = q_L/2 > 0.

There is a useful fully explicit lower bound:

    q_l >= 1/(1+3l),        m_L >= 1/[2(1+3L)].              (1)

Proof. For every real z, |sinh z|>=|z|, by integrating cosh z>=1.
Since x/(1+x) is increasing for x>=0,

    tanh²z = sinh²z/(1+sinh²z) >= z²/(1+z²).

For Z~N(0,q), q>0, Cauchy–Schwarz applied to
|Z|/sqrt(1+Z²) and |Z|sqrt(1+Z²) gives

    q² <= E[Z²/(1+Z²)] E[Z²(1+Z²)]
        = E[Z²/(1+Z²)] (q+3q²).

The normal fourth moment is 3q² (two integrations by parts in its density).
Thus q_l>=q_(l-1)/(1+3q_(l-1)), or
1/q_l<=1/q_(l-1)+3. Starting at q_0=1 proves (1).
This calculation involves only initialization and is unconditional.

## 2. Exact gradient identities at arbitrary fixed depth

Use the exact model and unit raw mobilities of CONTRACT §2. On the canonical
carrier write v=(w,K_2,...,K_L), c for the readout, and

    h(v)=(H_L(e1)-H_L(e2))/2,       b(v,c)=<c,h(v)>.

For a hidden direction a=(a_w,a_2,...,a_L), set for each input i=1,2

    dz_(1,i)=a_w.e_i,
    dz_(l,i)=a_l H_(l-1,i)+A_l[d_(l-1,i) dz_(l-1,i)],
    J_v a=(d_(L,1) dz_(L,1)-d_(L,2) dz_(L,2))/2,

where d_(l,i)=sech²(Z_(l,i)). This is a bounded directional linear map from
the row/HS hidden Hilbert space to the top L2 population. Bounded actions,
bounded gates and ||H||2<=1 prove boundedness by finite induction. Adjunction
gives exactly the trained hidden blocks of the signed objective b; all edges
retain their own actual adjoints. Thus its feature equation is

    c_s=h(v),       v_s=J_v* c.                              (2)

On any strong solution the curve chain rule yields

    h_s=J_v v_s,       c_ss=J_v J_v* c,
    b_s=||h||²+||J_v* c||²=||(v_s,c_s)||raw².                (3)

No derivative of J is required. The rule for tanh along strong L2 curves
follows by its scalar fundamental theorem and bounded-multiplier continuity;
operator times vector uses the ordinary add/subtract product rule. These
are the same hypotheses verified in the local proof, at each fixed depth.

For s>0 with g(s)=||c(s)||>0,

    g_s=b/g,
    g_ss=(||h||²-g_s²+||J_v* c||²)/g >= 0.                  (4)

Indeed |g_s|=|<c,h>|/||c||<=||h||. Since c(s)=s h_0+o_L2(s),
g_s(0+)=sqrt(m_L). Hence g_s>=sqrt(m_L), g>=s sqrt(m_L),
and the first positive interval cannot end by g returning to zero. Moreover,

    b_s>=||h||²>=g_s²>=m_L.                               (5)

All statements in this section hold wherever the strong feature solution
exists. Neither boundedness of J at each state nor (3) proves its continuation.

## 3. Finite-horizon physical fitting, conditional on continuation

Suppose the canonical orthogonal reference has a unique strong raw solution
through a given finite physical horizon T, so that the coordinate-swap and
readout-sign symmetry is valid there. The symmetry is the extension of R7:
swap the two first-row coordinates, leave hidden action labels unchanged,
and negate c. Adjoining transformed initialized programs preserves their joint
law; equivariance and uniqueness preserve f(e1)=-f(e2)=b. This is population
symmetry, not samplewise symmetry of finite initialized networks.

The mean-square physical vector field is exactly 2(1-b) times (2). In
particular

    b_t=2(1-b)(||h||²+||J_v* c||²).                         (6)

On a compact strong raw path, the coefficient on the right is continuous and
bounded: all action/readout norms are bounded and there are finitely many
layers. The scalar equation for e=1-b has initial value one and gives e>0
at every finite time. Therefore s_t=2e is strictly positive and legitimate;
reparametrization gives (2). Combining (5) with (6) proves

    0<1-b(t)<=exp(-2m_L t),
    loss_*(t)=(1-b(t))²<=exp(-4m_L t).                      (7)

In particular one fully explicit admissible fitting time would be

    T_L^fit = 2(1+3L),                                    (8)

provided the continuation hypothesis holds through that time. From (1),

    loss_*(T_L^fit)<=e^(-4)<1/8<1/4.                       (9)

The strict inequality follows already from e>2. At L=3, (8) is physical
time 20. This is a proved conditional fitting estimate with a fixed time
depending only linearly on depth, not a time selected from a numerical curve.
It does not replace the maintained two-layer time-40 result or its constants.

The slack in (9) is available for a supported-law perturbation theorem if
that theorem is established. Neither a support radius nor existence of a
perturbed strong solution follows from (9) alone.

## 4. Conditional reference endpoint

Suppose, more strongly, that a unique strong feature solution of (2) exists
on [0,1/m_L]. Equation (5) and continuity then imply that it reaches b=1
at a unique first s_dagger in (0,1/m_L]. For s<s_dagger set

    t(s)=integral_0^s [2(1-b(v))]^-1 dv.

The continuous derivative b_s is bounded above by a finite K on this compact
feature interval; hence 1-b(s)<=K(s_dagger-s). The integral diverges at
s_dagger, and its inverse defines all physical times. Equations (6)–(7)
then hold globally. From (3) and Cauchy–Schwarz,

    ||theta(s2)-theta(s1)||raw
        <=sqrt((s2-s1)(b(s2)-b(s1))).                       (10)

Using s_dagger-s<= (1-b(s))/m_L gives

    ||theta(t)-theta_dagger||raw
        <=m_L^-1/2 exp(-2m_L t).                           (11)

This is a strong row/HS/readout endpoint of the actual reference equation,
conditional on the stated construction. The uniform raw distance from
initialization is <=m_L^-1/2. With the maintained initialized action bound
2, every action norm is <=B_L=2+m_L^-1/2 and ||c||2<=m_L^-1/2.
Successive directional forward differentiation at any unit passive input
bounds its prediction gradient by

    C_L²=1+m_L^-1 sum_(j=0)^(L-1) B_L^(2j).

The straight segment between the endpoint and a reference state retains
these bounds. Integrating the scalar prediction derivative along that segment
and using (11) proves whole-circle endpoint convergence

    sup_|u|=1 |f(t,u)-f_dagger(u)|
        <= C_L m_L^-1/2 exp(-2m_L t).                       (12)

The endpoint interpolates the two labels and inherits coordinate-swap/sign
and odd-input symmetries. It is characterized through the feature flow, not
by uniqueness among all interpolating predictors. No perturbed-law endpoint
or one radius valid at all horizons is claimed.

## 5. Exact remaining implication

The unconditional new fact is (1). Equations (2)–(12) rigorously propagate
that fact once the indicated strong continuation and uniqueness exist.
The local C-H3 construction supplies only an initial interval. Extending it
to (8), or extending the feature equation to 1/m_L, still requires a reached
source/tail estimate or another valid strong construction. A strong raw
Cauchy endpoint supplied by energy is insufficient to invoke arbitrary-state
Picard theory: the vector field need not be locally Lipschitz on an L2 ball.
No conclusion in this file eliminates that obligation.
