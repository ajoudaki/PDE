# Exact weighted Gaussian formula without activation expansions

Date: 2026-09-21. Author: root. This continues the canonical p=1 initialized
population-kernel calculation. It uses established docs/observable_p1.md in
full, docs/NOTATION.md in full, the complete source/response Section 3 and
contraction C5.27--C5.31 in docs/global_nonlinear.md, and E.1 in
docs/gaussian_calculus.md. The current study's PEEL_DIRECT.md supplies a
separately rechecked normalization calculation. No other study is an input.

Claim type: exact identities proved below. This is a **weighted Gaussian
integral normal form**, with explicit non-activation density weights. It is
not the stronger finite normal form containing only products of the original
tanh and its derivatives at Gaussian arguments. No impossibility of that
stronger form is asserted. No polynomial, Hermite, Chebyshev, or other
activation expansion is used. This is a change of Gaussian integration
measure followed, where useful, by ordinary Stein integration by parts.
It must not be attributed to the book's finite auxiliary-factor elimination
theorem without this additional density transformation.

## 1. Fixed target and notation

Write sigma=tanh. The input is x(theta)=sqrt(2)(cos(theta),sin(theta)).
The population read-in is W^(1)(0)=G, readout W^(3)(0)=0, and W^(2)(0)=D1
is the finite dictionary-coefficient matrix (called M in the maintained
implementation). The population has already been taken to infinite width;
p=1 and eta=1/4096 stay fixed. Only the initial readout/tangent kernel is
calculated. No positive-time training or closure-order limit is asserted.

For independent standard Gaussian variables G,Z, define

    v = E sigma(G)^2,
    tau = E sigma(sqrt(v)G)^2,
    alpha = E sigma'(sqrt(v)G) = 1-tau,
    k = sigma(sqrt(tau)Z + alpha sigma(G)),
    beta = E[sigma(G) k],   s = E[k^2],   gamma = 1-s.

For rho in [-1,1], with an additional independent standard V, put

    A(rho) = E[sigma(G) sigma(rho G+sqrt(1-rho^2)V)],
    B(rho) = E[k sigma(rho G+sqrt(1-rho^2)V)].

The exact initialized matrix/source contraction is

    Gamma = [[v+eta,beta],[beta,s+eta]],
    Lambda(rho) = (alpha v, alpha beta+tau gamma)
                  Gamma^{-1} (A(rho),B(rho))^T / (tau+eta),
    a_theta = Lambda(cos(theta)),
    b_theta = Lambda(sin(theta)).

The raw upper features are sigma(sqrt(v)X_i), for independent standard X_i.
The normalized dictionary features are these divided by sqrt(tau+eta).
Accordingly sqrt(tau+eta)(a_theta,b_theta)^T equals the two active entries
of W^(2)(0) E_1[b_1 H^(1)(0,x(theta))]. The inactive constant entry is zero.
The target is

    K(theta,psi) = E[ sigma(a_theta sigma(sqrt(v)X1)
                           +b_theta sigma(sqrt(v)X2))
                       sigma(a_psi sigma(sqrt(v)X1)
                           +b_psi sigma(sqrt(v)X2)) ].

The reverse-use term tau gamma is retained. Gamma is positive definite
because it is a second-moment Gram of (sigma(G),k), plus eta I. These formulas
come from both directions of the same initialized action and the full
inverse-transpose dictionary normalization, not a new Gaussian connector.

## 2. The elementary change-of-measure identity

Let q>0. Define on the real line

    w_q(z) = 1_{|z|<1}
             exp((z^2-atanh(z)^2)/(2q)) / (1-z^2),

with value zero for |z|>=1. For every bounded measurable F,

    E_{G~N(0,1)} F(sigma(sqrt(q)G))
      = E_{Y~N(0,q)}[w_q(Y) F(Y)].                         (1)

Proof: the substitution z=tanh(sqrt(q)g) gives the probability density

    p_q(z) = 1_{|z|<1} exp(-atanh(z)^2/(2q))
              / (sqrt(2 pi q)(1-z^2)).

Dividing this density by the strictly positive N(0,q) density gives w_q.
This proves (1), E w_q(Y)=1, and integrability for every bounded F. The
identity applies also to integrable unbounded F by the ordinary positive
and negative part decomposition.

The weights extend smoothly by zero at z=+-1. To see this, set z=tanh(t).
As |t| tends to infinity, each fixed-order z derivative contributes at
most exp(C_j |t|) times a polynomial in |t|, whereas the density factor
contains exp(-t^2/(2q)). Thus the weight and all its finite derivatives
vanish at either endpoint. In particular each w_q is a bounded smooth
compactly supported function.

## 3. Exact upper Gaussian formula

Take Y1,Y2 independent N(0,v). Apply (1) separately to the two raw upper
features. This gives

    K(theta,psi) = E[ w_v(Y1) w_v(Y2)
                       sigma(a_theta Y1+b_theta Y2)
                       sigma(a_psi Y1+b_psi Y2) ].          (2)

All arguments of sigma in (2) are linear Gaussian variables. Their joint
covariance is

    v [[a_theta^2+b_theta^2,
        a_theta a_psi+b_theta b_psi],
       [a_theta a_psi+b_theta b_psi,
        a_psi^2+b_psi^2]].

Their covariances with Y_i are v times the corresponding coefficient.
No covariance inverse is needed, so coincident, opposite, zero and
linearly dependent coefficient pairs cause no exceptional case. Absolute
integrability follows from |sigma|<=1 and independence with E w_v(Y_i)=1.

Equation (2) is exact for every finite coefficient pair, even away from
canonical initialization. It does not say the actual upper preactivation
has this Gaussian law: the density weights preserve its actual law inside
the calculation. Omitting them changes the kernel. The weights are fixed
functions determined by v, not trained readout parameters.

## 4. Exact lower Gaussian formulas

Let S,Z be independent standard Gaussians and set

    R = alpha S + sqrt(tau) Z.

Thus (S,R) is jointly centered Gaussian with covariance

    [[1,alpha],[alpha,alpha^2+tau]].

Applying (1) at q=1 to the original sigma(G) gives

    beta  = E[w_1(S) S sigma(R)],
    s     = E[w_1(S) sigma(R)^2],
    gamma = E[w_1(S) sigma'(R)].                            (3)

These are exact, and gamma=1-s since E w_1(S)=1. In (3), w_1 restricts S
to [-1,1], so boundedness immediately gives absolute integrability.

If an explicit Gaussian factor S is to be peeled away, scalar Stein gives

    beta = E[w_1'(S) sigma(R)]
              + alpha E[w_1(S) sigma'(R)],                 (4)

where, for |z|<1,

    w_1'(z) = w_1(z) [z+(2z-atanh(z))/(1-z^2)],

and the derivative is zero for |z|>=1. All functions needed for (4) are
smooth with bounded derivatives in S, and sigma and sigma' are bounded;
conditioning on Z and integrating the Gaussian S density by parts has
zero boundary terms. This is an actual finite Stein step, and exposes
the extra density derivative rather than hiding it as an activation atom.

The ordinary A(rho) is already a simple two-Gaussian activation moment.
For B(rho), an additional correlated input must be retained. For |rho|<1
define the explicit weight on (z,y) in R^2 by

    J_rho(z,y) = 1_{|z|<1} / ((1-z^2)sqrt(1-rho^2))
       * exp((z^2+y^2)/2
             -(atanh(z)^2-2rho y atanh(z)+y^2)/(2(1-rho^2))).

Take S,Y,Z independent standard Gaussians and again put
R=alpha S+sqrt(tau)Z. Then

    B(rho) = E[J_rho(S,Y) sigma(R) sigma(Y)].                (5)

Proof: if (G,T) has unit marginal variances and covariance rho, the joint
density of (sigma(G),T) at (z,y) is

    1_{|z|<1} exp(-(atanh(z)^2-2rho y atanh(z)+y^2)
                         /(2(1-rho^2)))
      / (2 pi sqrt(1-rho^2)(1-z^2)).

Divide by the density of independent standard (S,Y) to obtain J_rho.
The reverse noise Z was independent originally and stays independent.
The density ratio is nonnegative with E J_rho(S,Y)=1; this proves (5)
and its absolute integrability. In this reference measure R and Y are
independent Gaussian variables with variances alpha^2+tau and 1. The
weight carries the original nonlinear dependence; discarding it is invalid.

At rho=1 or -1 the density is singular, and (5) is not used. Instead,

    A(1)=v,   A(-1)=-v,
    B(1)=beta,   B(-1)=-beta.                               (6)

These follow directly from the defining original variables and oddness
of sigma. The limits as rho approaches the endpoints agree by bounded
convergence in the original coupled representation. At rho=0, J_0(z,y)
=w_1(z), and (5) vanishes by the independent centered sigma(Y), as it must.

## 4a. A shorter exact lower formula by Gaussian density translation

After the independent canonical attempt froze, its density-translation
identity supplied a simpler alternative to (3)--(6). Keep G,V standard and
T~N(0,tau) independent, and put Y_rho=rho G+sqrt(1-rho^2)V. Define

    L(G,T) = exp(alpha T sigma(G)/tau
                 - alpha^2 sigma(G)^2/(2 tau)).

Then, exactly,

    beta = E[sigma(G) sigma(T) L(G,T)],
    s = E[sigma(T)^2 L(G,T)],
    gamma = E[sigma'(T) L(G,T)],
    B(rho) = E[sigma(T) sigma(Y_rho) L(G,T)].                 (7)

All displayed activation arguments are jointly Gaussian, with

    Cov(G,Y_rho,T) = [[1,rho,0],[rho,1,0],[0,0,tau]].

This includes rho=+-1 without taking a limit. For fixed G, the ratio of
the N(alpha sigma(G),tau) density at T to the N(0,tau) density is precisely
L(G,T). Multiplying by the reference density and translating the integral
proves (7). Moreover E_T[L(G,T)|G]=1; bounded remaining activation factors
give absolute integrability. Directly L is bounded by exp(alpha |T|/tau),
an integrable Gaussian exponential, so elementary Fubini also applies.

The additional terminal is now the explicit exponential L rather than
J_rho. It still contains a nonlinear function of Gaussian roots and is
not a finite product of the original activation derivatives. No series
expansion of L is used or implied. The two versions are exact equivalent
changes of measure, not independent evidence of a product-only identity.

## 5. What this completes, and what it does not

Equation (2), either (3)--(6) or (7), the original simple Gaussian A, and the finite 2x2
linear algebra in Section 1 provide an exact finite Gaussian-integral
evaluation of every coefficient and the kernel, with no nonlinear
activation evaluated at a nonlinear Gaussian expression. There are no
degree cutoffs N,m, no approximation radius, and no polynomial limit.

The added weights w_q,J_rho and w_1' are explicit functions of deterministic
coordinates and known initialization constants. They are not expectations
of the answer, unknown learned populations, or fitting coefficients.

Nevertheless they are additional terminal functions containing atanh and
exponentials. They are not finite products of the original tanh and its
derivatives. Therefore this result does NOT establish the user's stricter
original-activation-only Gaussian normal form. It establishes a nearby,
exact weighted Gaussian form. The strict finite-only target stays open;
failure to derive it is not a proof of impossibility.

No external theorem beyond change of variables, Gaussian conditioning and
integration by parts is imported; proofs are included. No numerical
experiment or training run was used to establish these identities.
