# Assembly of the C-X1 learning and approximation conclusions

Complete author proof unit, using the three named interfaces proved in the
companion units. Independent review of the assembled candidate is pending.
No input estimate below is inferred from successful numerical runs.

## Exact interfaces

Use the model in THEOREM.md. Let theta_* denote the orthogonal reference
for the same m,d and labels, and theta_u the flow at perturbed directions.
The required inputs are:

(R) REFERENCE_PROOF.md supplies T=5m, L_*(T)<1/16, a time t_a in (0,T],
and a number a_m>0 such that the training-averaged paired activation RMS
of EACH reference hidden layer at t_a is at least a_m. The reference is
on the common canonical carrier with the full first row.

(P) PERTURBATION_PROOF.md supplies rho_0>0, strong unique flows through T,
actual finite-network capture, and a deterministic modulus Psi(s) tending
to zero as s decreases to zero, such that

  sup_(t<=T) (||w_u-w_*||2 + ||K_u-K_*||HS + ||c_u-c_*||2)
      <= Psi(s),       s=max_a |u_a-e_a| < rho_0.

It also supplies uniform reached passive query tails for this fixed family.
The constants may depend on fixed m,d,T. These hypotheses require a proof
for the perturbed trajectories, not merely for their linear responses.

(C) CX1_CLOSURE_PROOF.md supplies the specified finite dictionary and
joint initializer, autonomous finite closure, own-state restart, convergence
to each target with the properties in (P), and numerical consistency with
the stated iterated limits. Its proofs and executable code must correspond.

All signs can be handled by uniform constants proved in (R),(P), or by
taking minima/maxima over the finite set of 2^m binary label lists. Such a
finite minimum of positive radii is positive and does not depend on width
or approximation resolution.

## Uniform raw bounds needed for the assembly

The initial population loss is one. The exact raw gradient/energy identity
gives L(t)<=1 and m^-1 sum_a |r_a(t)|<=1. Bounded tanh therefore gives

  ||c(t)||infty <= 2t,
  ||K'(t)||HS <= 2||c(t)||2 <= 4t,
  ||A(t)||op <= 2+2t^2,
  ||w'(t)||2 <= 2||A(t)||op ||c(t)||2 <= 8t+8t^3.

Here the last row norm is L2(Omega1;R^d), |u_a|=1, and Cauchy--Schwarz
is applied separately on the two populations. Integration yields

  ||w(t)||2 <= sqrt(d)+4t^2+2t^4.

These bounds hold for both the reference and every constructed perturbed
gradient flow. Set C=2T, M=2+2T^2 and W=sqrt(d)+4T^2+2T^4. No source-tail
or uniqueness conclusion is being derived from these raw bounds alone.

## Loss margin and paired activity survive input perturbations

For one matched pair u_a,e_a and t<=T put e=Psi(s). Tanh is one-Lipschitz,
so the coupled hidden fields obey

  ||H1_u(u_a)-H1_*(e_a)||2 <= e+Ws,
  ||H2_u(u_a)-H2_*(e_a)||2 <= (M+1)e+MWs.

For the second inequality subtract A_u(H1_u-H1_*)+(K_u-K_*)H1_*, use
||H1_*||2<=1, and then use the outer tanh Lipschitz bound. For predictions,
subtract the readout first and use the bounded reference readout:

  |f_u(u_a)-f_*(e_a)| <= [1+C(M+1)]e+CMWs =: D_f(s).

This scalar bound is uniform over the m inputs. The Euclidean triangle
inequality with weights 1/m gives

  sqrt(L_u(T)) <= sqrt(L_*(T))+D_f(s).

At initialization the common Gaussian row satisfies
||g.(u_a-e_a)||2=|u_a-e_a|<=s, and the initial action has norm at most two.
Consequently initial hidden discrepancies are at most s and 2s in layers
one and two. Applying the triangle inequality to the difference of the
current-minus-initial fields therefore bounds discrepancies of the two
paired displacements by

  D_1(s)=e+(W+1)s,
  D_2(s)=(M+1)e+(MW+2)s.

The same inequalities hold after taking the training-averaged L2 norm:
this is an L2 norm on the product of the counting probability and the
layer population, with the SAME initial/current coordinate at each input.
It is not a distance between independent hidden marginals.

All three D functions tend to zero. Choose a fixed positive rho<rho_0
small enough that, for 0<=s<rho,

  D_f(s)<=1/8,        D_1(s)<=a_m/2,        D_2(s)<=a_m/2.

Such a choice is part of the theorem's constants and is made before
choosing width, dictionary order or numerical resolution. Then

  L_u(T) < (1/4+1/8)^2 = 9/64 < 1/4,
  J_(1,u)(t_a), J_(2,u)(t_a) >= a_m^2/4 > 0.

Thus the prescribed learning and nonlazy-motion conclusions have strict
margins. They do not assert improvement on an unrelated unseen data law
or superiority to any other learning algorithm.

## Nonaffinity at the same activity time

The reference proof also supplies, at t_a and every training anchor, positive
preactivation variance at least q/4 and best-affine tanh error at least
nu_*/2. Here q=E tanh(G)^2 and nu_*=min(N(G),N(sqrt(q)G))>0, where
N(Z)=inf_(a,b) E|tanh(Z)-aZ-b|^2. Its preactivations are within epsilon_*
of the corresponding initial Gaussians, so their standard deviations are
also at most two. These are facts about reached laws, separate from motion.

For completeness the covariance argument in reference (7.10d--f) does not
require the comparison variable X to be Gaussian. If its standard deviation
sigma lies in (0,2] and ||Z-X||2=epsilon<=sigma/2, centering and the bounded
one-Lipschitz tanh give

  Var(Z)>=(sigma-epsilon)^2,
  |N(Z)-N(X)| <= 2epsilon
       +(2sigma+epsilon)(2+sigma)epsilon/(sigma-epsilon)^2
       <=64epsilon/sigma.

This follows by subtracting Var(tanh Z) and Cov(Z,tanh Z)^2/Var(Z), as in
that displayed argument; the final bound uses
2sigma+10(2+sigma)<=44 for sigma<=2. No higher moment is needed.
Set delta_N=nu_*sqrt(q)/512. Shrink the fixed rho further so that

  e+Ws<=delta_N,  (M+1)e+MWs<=delta_N  for s<rho.

These are also the preactivation differences before the outer tanh. For
either reference preactivation sigma>=sqrt(q)/2; delta_N<=sigma/2. The
preceding inequality therefore gives, on every perturbed training anchor,

  Var(Z_l,u(t_a,u_a))>=q/16,
  N(Z_l,u(t_a,u_a))>=nu_*/4>0,  l=1,2.

The variance/covariance formula is continuous under the declared joint W2
limits with these positive denominators. Thus finite networks and the
successively refined closures inherit strictly positive margins as well.
This is not a uniform relative-strength or superiority claim.

## An explicit choice of the final geometric radius

The preceding shrinkages need not leave an unnamed continuity neighborhood.
Let a=a_m and delta_N be as above, and put

  F=1+C(M+1)+CMW,
  zeta=min{1, 1/(8F), a/[2(W+2)], a/[2(M+1+MW+2)],
                   delta_N/(W+1), delta_N/(M+1+MW)} >0.

All required inequalities follow whenever the raw error e and input
displacement s are at most zeta. Take the explicit reference-tail constants
Gamma,H,S,D_*,C from PERTURBATION_PROOF (P37)--(P38); in this paragraph these
names have exactly that proof's meaning, distinct from the energy constants
used to form zeta. Define

  Z_L=max{1,log(4/zeta)}, A_L=1+Gamma+H+Z_L,
  b_L=4S A_L, X_L=Gamma(1+b_L),
  r_L=exp(-Z_L-4-2X_L),
  rho_final=min{rho_cap/2,r_L},

where rho_cap is the explicit (P39) radius at T=5m. The elementary bounds
following (P39), with Z replaced by Z_L, show that each of the two terms
on the right of (P38) is below exp(-Z_L)/4 when s<=r_L. Thus
e<exp(-Z_L)/2<=zeta/8 and s<zeta/8. The same estimate passes to strong
flow limits. This proves all loss, motion and nonaffinity inequalities for
s<rho_final. Every constant is defined by fixed elementary expressions and
initial one-dimensional Gaussian integrals. A numerical evaluation or a
useful lower bound for this very conservative radius is not asserted.

## Whole-sphere observations and the two distinct approximation limits

For each fixed reached state and unit v,v', the same factorizations give

  |f(v)-f(v')| <= ||c||2 ||A||op ||w||2 |v-v'| <= CMW |v-v'|.

The finite-network analogue replaces field norms by RMS and uses the
ordinary finite matrix operator norm. Its high-probability raw bounds
therefore give a common finite Lipschitz constant. Cover the compact
sphere by a finite epsilon-net. For any prescribed accuracy choose the
net first, apply the proved joint finite-program/finite-flow convergence
on its finitely many points, and then use this Lipschitz bound. This is
the finite-net passage to uniform input prediction whenever required by
the finite-network proof; no uniform rate in d or net cardinality is claimed.

The full finite-network approximation is that of (P). It retains the
actual random finite readout and its stated probability/step conditions.
The closure approximation is separately that of (C): first remove each
fixed-order numerical error in the justified order, then send dictionary
order to infinity. Both identify the SAME theta_u, but these two limits
do not imply arbitrary simultaneous growth of neural width and closure
order. Predictions pass to risks by their uniform bounds. The declared
joint W2 convergence passes the paired squared displacements by second-
moment convergence; both initial and current fields occur in the tuple.

## The correlated family is nonempty

If m>=2, take u_1=(e_1+t e_2)/sqrt(1+t^2), all other u_a=e_a, and any
0<t<rho/2. The identity

  |u_1-e_1|^2 = 2-2/sqrt(1+t^2) <= t^2

follows from 1/sqrt(1+x)>=1-x/2 for x>=0 (differentiate the difference,
which is zero at x=0 and has nonnegative derivative). Thus this is in
the admitted family and u_1.u_2=t/sqrt(1+t^2)>0. Nearby choices give
further nonorthogonal configurations. No whitening has occurred.

For exact rational numerical inputs one may instead use the stereographic
map about e_a: for a rational vector z in its orthogonal coordinate plane,

  u_a(z) = ((1-|z|^2)e_a+2z)/(1+|z|^2).

Orthogonality z.e_a=0 gives |u_a(z)|=1 by expanding the numerator square,
and |u_a(z)-e_a|=2|z|/sqrt(1+|z|^2)<=2|z|. Rational z therefore gives
exact rational unit inputs; sufficiently small nonzero rational z exists
for every positive rho. This is a mathematical representation argument,
not a claim that a particular working precision resolves the proved radius.
