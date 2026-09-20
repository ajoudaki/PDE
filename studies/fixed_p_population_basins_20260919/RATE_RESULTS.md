# Quantitative noisy fitting: results and optimizer tradeoffs

2026-09-19. Synthesis of this study's rate continuation. Internally
checked theory, not promoted material. No numerical evidence is used.

## 1. What changed in the answer

The earlier fractional-progress Gaussian theorem guaranteed eventual
fitting but did not bound the number of rejected proposals. We now have
an explicit finite confidence-time bound for that same rule. Modified
proposals additionally give polynomial or exponential expected-loss
rates. Every result counts unsuccessful proposals; none merely
relabels successful stages as physical time.

| Mechanism | Quantitative conclusion | Exact cost or restriction |
|---|---|---|
| Unchanged full-support additive Gaussian, held-state fractional acceptance | P(tau_epsilon<=B_h(epsilon,delta))>=1-delta, with a finite explicit recursive B_h | Potentially enormous covariance/data-dependent bound; unconditional expected target time not established |
| Occasional absolute Gaussian refresh in an input-defined finite family | E L_k<=C k^(-2/d), E tau_epsilon<=C' epsilon^(-d/2) | Global replacement candidates; d can be reduced to the merged sample count by fixing candidate hidden fields |
| Current-feature readout Gaussian, inverse-free | E L_k<=L0 exp[-q_* kappa^2 k/(4m)] | Small physical perturbations; geometry-dependent rate; explicitly restricted full-GF interval |
| Current-feature Gaussian isotropic in prediction coordinates | E L_k<=L0 exp[-q_* k/(4m)] | Requires current Gram inverse and may make large physical steps when geometry is poor; same restricted full-GF schedule |
| Separate adaptive Gaussian readout search feeding the incumbent | E L_k<=exp[-rho q_* kappa_Q k/(4m Lambda_Q)] | Fixed-feature auxiliary process and global incumbent replacements |

The current-feature variants begin from the unchanged canonical state
for p=1 and p=2 and every finite compatible binary dataset on the circle.
They do not require three inputs, linear independence of the inputs,
or a lower bound on separation. Positive and negative masses need not
balance. Combine exact duplicates and antipodes with compatible signs
before forming the Gram. Contradictory duplicates or same-sign antipodes
are excluded as architectural incompatibilities.

The unchanged-rule and refresh routes hold for canonical p=1,2,3.
At p=3 this study has not established the starting positive-Gram premise
for the current-feature routes on every compatible dataset. An explicit
input-only hidden refresh with readout kept zero supplies that premise
at p=3, but changes the initialized hidden state.

## 2. The inverse-free rate in compact form

For the exact current population features

\[
a_i=E_1[b_1\phi(w\cdot x_i/\sqrt2)],\qquad
H_i=\phi(b_2^TMa_i),\quad f_i=E_2[cH_i],\quad
L=\sum_i\mu_i(f_i-y_i)^2,
\]

define the weighted current Gram

\[
K_{ij}=\sqrt{\mu_i\mu_j}E_2[H_iH_j].
\]

Let m be the number of representatives after the compatible reduction,
and let kappa=lambda_min(K0)/2>0. This positivity is a proved canonical
initialization property at p=1,2, not a trajectory assumption.

At a held state of loss ell draw independent standard Gaussian
G_1,...,G_m and propose

\[
\delta c=\frac{\kappa\sqrt{\ell}}{4m}
 \sum_i\sqrt{\mu_i}G_iH_i.
\tag{1}
\]

Accept only if the new loss is at most
(1-kappa^2/(4m))ell. On acceptance run full original gradient flow
in w,c,M for the explicitly specified fixed positive time h in
RATE_ADAPTED_READOUT.md (3), evaluated with that acceptance fraction.
Rejections leave the state unchanged. All proposals count.

The exact conditional covariance obeys

\[
E[\|\delta c\|_2^2\mid S]\le
\frac{\kappa^2}{16m^2}L(S).
\tag{2}
\]

Thus the perturbation shrinks in the original physical metric.
No Gram inverse, fitted readout, or residual direction is used in (1).
The initial spectral lower bound sets the scale.

The proof has three steps:

1. An accepted readout move has norm at most
   (1+sqrt(theta))sqrt(ell/kappa) while K>=kappa I.
   The accepted losses decrease geometrically, so these bounds sum.
   Exact full-GF speed estimates and the fixed choice of h bound total
   hidden travel by half a neighborhood where K remains positive.
   A first-exit argument therefore proves K>=kappa I for every history.
2. At each trial there is probability at least
   q_*=exp(-2)/(2sqrt(2pi)) that the Gaussian has a modest component
   against the current readout loss gradient and controlled orthogonal
   components. Exact quadratic expansion of the readout loss then
   guarantees the required fractional decrease.
3. Conditional expectation and iteration give

\[
E[L_{k+1}\mid\mathcal F_k]\le
\left(1-\frac{q_*\kappa^2}{4m}\right)L_k,\qquad
E L_k\le L_0e^{-q_*\kappa^2 k/(4m)}.
\tag{3}
\]

In particular, for 0<epsilon<L0,

\[
E N_\epsilon\le
\frac{1+(4m/\kappa^2)\log(L_0/\epsilon)}{q_*},\qquad
P(L_k>\epsilon)\le
\frac{L_0}{\epsilon}e^{-q_*\kappa^2 k/(4m)}.
\tag{4}
\]

The scaled loss (1-q_* kappa^2/(4m))^(-k)L_k is a nonnegative
supermartingale. This is an actual stochastic Lyapunov inequality.
Almost surely the loss obeys every strictly smaller exponential rate
after a random finite onset, and the full population state has a finite
strong limit of zero loss. There is no deterministic upper bound on
the number of early rejections for every noise realization.

If each exact proposal costs Delta>0 units and each successful trial
is followed by h units of physical GF, the elapsed hybrid process obeys

\[
E L(t)\le L_0\exp\left[
-\frac{q_*\kappa^2}{4m}
\left\lfloor\frac{t}{\Delta+h}\right\rfloor\right].
\tag{5}
\]

This clock counts waiting and flow. It is an exact population-oracle
clock, not the computational cost of approximating the integrals.
Infinitely many successes give infinite accumulated physical GF time
because h is fixed and positive.

## 3. What the two exponential current-feature variants explain

The readout map A:z -> (sqrt(mu_i)E[zH_i]) has K=AA*.
The inverse-free proposal is eta sqrt(ell)A*G. Replacing it by
sqrt(ell)A*K^(-1)G/(4m) makes weighted prediction changes isotropic.
With acceptance fraction 1-1/(4m), the same argument replaces
kappa^2/(4m) by 1/(4m) in the proposal rate.

This does not remove geometry from the physical problem: the inverse
can magnify readout perturbations, and the allowable full-GF interval
still depends on initial conditioning. The inverse-free variant is the
more natural choice when small physical perturbations matter. It pays
for poor geometry through a small rate instead.

Both methods maintain the ability to correct every training residual
by a readout change while retaining the original hidden-layer velocities
between kicks. Their proof constrains total hidden displacement. It
does not classify all bad equilibria or prove general stochastic escape
under unrestricted feature motion. In particular, the fitting guarantee
comes from a preserved nondegenerate representation and readout noise;
it does not demonstrate that hidden feature learning is necessary for
fitting this finite dataset.

## 4. What is gained without changing the old fractional rule

RATE_EXISTING_RULE.md replaces the old unspecified success probability
with a finite coordinate Gaussian density product q(R,a)>0. Its rescue
centers lie in one fixed finite-dimensional family even though the
incumbent ranges over an infinite-dimensional physical norm ball.
Gaussian trace-tail bounds justify the remaining coordinates.

For target epsilon, before it is attained every stage's acceptance
threshold exceeds theta epsilon, even when previous stages overshoot.
Use q(R,theta epsilon), a conditional tail bound for the selected
successful Gaussian, and the exact GF displacement bound
sqrt(h times current loss) to propagate finite stage norm envelopes.
The resulting explicit recursion yields B_h(epsilon,delta).

This is a genuine rate strengthening for the same fractional rule,
without a recurrence assumption, change of covariance, state reset,
or unknown infimum over states. It can be extremely large and does not
prove finite unconditional expected hitting time. Numerical evaluation
of its bound requires effective covariance coordinates, certified tails
and population-integral information; the mathematical theorem is stated
for every injective trace-class Gaussian covariance.

The older accept-every-strict-decrease additive-noise rule remains
different. Its all-compatible-data convergence from canonical
initialization is still open in this study.

## 5. Evidence and status

Complete proofs:

- RATE_EXISTING_RULE.md: unchanged fractional algorithm, finite
  confidence-time recursion.
- RATE_RESTART_ROUTE.md: polynomial absolute refresh, exponential
  auxiliary Gaussian readout search, and explicit geometry constants.
- RATE_ADAPTED_READOUT.md: isotropic prediction perturbations,
  deterministic Gram preservation, exact clocks, and strong endpoint.
- RATE_SMALL_READOUT_NOISE.md: inverse-free small physical perturbations,
  geometry-dependent exponential rates, and complete extension proof.

Independent internal reviews are RATE_OTHER_REVIEW.md for the first
two routes, RATE_READOUT_REVIEW.md for the third, and the followup
RATE_SMALL_NOISE_REVIEW.md for the fourth. Initial wording corrections
were explicit binary-label scope, positive target-accuracy range, and
effective-data qualification. No substantive estimate changed.
The small-noise review is an informed followup by the main candidate's
reviewer, not a fresh isolated promotion review.

No simulation, finite-width claim, ordinary-SGD equivalence, established
book edit, or promotion is part of these results. The principal open
problem remains a quantitative fitting theorem for small noise with
unrestricted full hidden flow, without a schedule that preserves the
initial readout Gram.
