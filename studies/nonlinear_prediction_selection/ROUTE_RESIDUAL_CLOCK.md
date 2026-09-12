# Coordinator route: integrated controls and constrained slow evolution

Status: candidate proof architecture, not a theorem. Author: coordinator.
Inputs: complete maintained C.4.5–C.4.8, C.1–C.2, C.4.1–C.4.3,
A.1–A.4, B.1, and special-data III.F.1–11. No external theorem used.
The conditioning agent communicated its proposed endpoint independence
argument before this note; that ingredient is not an independent discovery
here. The integrated-control and singular-limit derivation below is the
coordinator's route. Other route files have not yet been read.

## The selected object, if its construction can be proved

On the established Gaussian carrier let `theta=(w,K,c)`, `A=A0+K`,
and write `g_u=grad_raw f_theta(u)`:

```
g_u = (phi'(w.u) Q(u) u,
       [c phi'(A phi(w.u))] tensor phi(w.u),
       phi(A phi(w.u))).
```

Let `G:R²→E` have columns `g_e1,g_e2`, `M=G*G`, and
`Pi=I-G M^-1 G*` whenever `M>0`. For an added law `nu`, put
`v_nu(theta)=integral (f_theta(u)-y) g_u dnu`.
The candidate determining evolution is

```
d theta_bar/d tau = -2 Pi(theta_bar) v_nu(theta_bar),
theta_bar(0)=theta_dagger,
P_nu(tau,sqrt2 u)=<c_bar,tanh((A0+K_bar)tanh(w_bar.u))>.
```

The inverse is the actual two-anchor raw Gram, recomputed from current
features. Coefficients use only the law, current state and established
initialization. This retains hidden feedback. It would preserve the two
anchor predictions, since `G*Pi=0`. It is an infinite-dimensional
constrained evolution, whose well-posedness has not yet been proved here.

## Exact finite or already-existing strong-flow algebra

For the actual mixture flow, write `r=(f(e1)-1,f(e2)+1)`. Then

```
theta' = -(1-epsilon)G r - 2 epsilon v_nu,
r' = -(1-epsilon)M r - 2 epsilon G* v_nu.
```

These follow from the exact raw gradients and the two atom weights.
On a segment where `M>=kappa I` and states are bounded, scalar norm
differentiation gives, for `epsilon<=1/2`,

```
|r(t)| <= exp[-kappa(t-b)/2]|r(b)| + C epsilon,
integral_b^t |r(s)| ds <= 2|r(b)|/kappa + C epsilon(t-b).
```

At a zero residual norm the upper derivative bound follows from the
velocity norm; equivalently regularize the norm by `sqrt(|r|²+eta²)`.
The constant bounds `2|G*v_nu|` on the state region. No spectral gap
for the full ambient Hessian is needed.

Let `B(theta)=G M^-1`. The exact identity is

```
theta' = -2 epsilon Pi v_nu + B r'.
```

If B is absolutely continuous along the reached path, integration by
parts gives

```
theta(t)-B(t)r(t)
 = theta(b)-B(b)r(b)
   -2 epsilon integral_b^t Pi(theta(s))v_nu(theta(s)) ds
   -integral_b^t B'(s)r(s) ds.
```

If actual query fourth moments are uniformly bounded and readout suprema
are bounded on this segment, direct differentiation of the finite list of
gradient columns gives `||B'||<=C(|r|+epsilon)`. The only extra row
product is `phi''(w.u) w'.u Q(u)`, bounded in L² using fourth moments
of the finitely many Q fields. Upper field derivatives use bounded c,
bounded actions, and rank bounds. This claim requires those reached
moment estimates; bounded raw norm alone does not supply them.
The displayed error then obeys

```
integral_b^t ||B'(s)r(s)|| ds
 <= C [|r(b)|² + epsilon |r(b)| + epsilon²(t-b)].
```

On physical intervals of length `tau0/epsilon`, this tends to zero
after `r(b)` tends to zero. This identifies the scale `tau=epsilon t`
from the equations. A fixed nonzero `tau0` permits finite nonlinear motion.

## Candidate missing continuation lemma

Consider controlled training `theta'=sum_j a_j(t) g_uj(theta)`.
The controls are deterministic and integrable; their finite-program
versions freeze them in named-source derivatives. Include the two axes
and finitely many passive/added directions. Compare with the actual
reference control `a_*,a(t)=-r_*,a(t)`, padded by zeros as needed and
reparameterized by its bounded feature clock. Seek constants `delta,C,c>0`
such that every sufficiently fine controlled Euler program satisfying

```
integral sum_j |a_j-a_*,j| dt <= delta
```

has named backward response row sums bounded by C and passive query tails
`tau_R(Q(u))<=C exp(-cR²)`, independently of physical horizon. The common
reference's total control variation is at most ten. Reparameterize by
`d s = sum_j (|a_j|+|a_*,j|) dt`; both coefficient lists are bounded by one
and total s length is bounded. Zero-clock portions have zero state motion.

A possible proof adapts C.4.7.N20–N51: compare controls in integrated
variation in place of the law transport cost, use a common dominating
control measure for every injection weight, and use the reference clock
source anchor. Every control difference must retain its integrated mass,
including when the base coefficient vanishes. Prove the coefficient
bootstrap before using the tails to construct the flow. The bounded
reference feature-time construction can anchor the full physical history.
This lemma is not established by simply renaming T in C.4.7.

Once proved, apply a first-exit argument. For fixed large b the mixture
prefix tends to the reference prefix as epsilon tends to zero. After b,
the residual estimate above bounds the total changed control variation by
`C exp(-b/5)+C tau0`. Choose b large and tau0 small, both independently
of epsilon, to remain in the control tube and the endpoint conditioning
neighborhood. This would supply continuation through `b+tau0/epsilon`.
Population Euler completion, one-reference finite GF comparison and the
joint internal observation contract then require proofs with that same
control tube. Ordinary finite existence is insufficient.

## Remaining singular-limit and activity obligations

The constrained field must have an Osgood comparison estimate on the
constructed reached family. Gaussian Q tails give the plausible modulus
`C d sqrt(log(e/d))`; the finite matrix inverse is locally Lipschitz when
`M>=kappa I`. This needs an actual constructed tail-bearing constrained
flow. The integration-by-parts identity would then show selection from
original initialization, first epsilon to zero at fixed b and then b to
infinity. This is a proof device, not imposed pretraining.

The added risk along a proved constrained flow would satisfy
`d R_nu/dtau=-4||Pi v_nu||²`. A robust positive initial projected-gradient
norm would give a strictly positive short-episode risk gain. A nonzero
hidden parameter block by itself must be converted into a named hidden
representation displacement with common initialization and actual finite
observation capture. Neither margin is yet claimed.

No training experiment or promotion is proposed from this candidate.
