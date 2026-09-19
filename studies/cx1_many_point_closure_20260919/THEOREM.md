# C-X1 candidate: many-point computation through nonlinear learning

Status: author assembly in progress. The following is the required statement,
not an accepted theorem. Proof units must supply every assertion before review.

## Model and data

Fix integers `1 <= m <= d`, labels `y_a in {-1,+1}`, and unit directions
`u_a in R^d`. The actual inputs are `x_a=sqrt(d) u_a`. The bias-free network is

`z1=W1 u`, `h1=tanh(z1)`, `z2=W2 h1`, `h2=tanh(z2)`,
`f_n(u)=c^T h2/n`.

All initialized entries are independent: first weights have variance one,
middle entries variance `1/n`, stored readout variance `1/n^2`, and all are
centered Gaussian. The physical block mobilities are `(n,1,n)`. The loss is
`L_n=m^{-1} sum_a (f_n(u_a)-y_a)^2`, without a half. Raw GD is simultaneous
in these stored parameters. Population readout zero is their limit, not a
change to finite initialization.

On the two canonical initialized Gaussian population spaces write
`w in L2(Omega1;R^d)`, `c in L2(Omega2)`, `A=A0+K`, where A0 is the actual
initialized bounded action with its adjoint and only K is Hilbert--Schmidt.
Use the sum raw distance
`||w-wbar||2 + ||K-Kbar||HS + ||c-cbar||2` on a common carrier. For any
unit passive u set

`H1=tanh(w.u)`, `Z2=A H1`, `H2=tanh(Z2)`,
`Delta2=c tanh'(Z2)`, `Q=A* Delta2`, `Delta1=tanh'(w.u) Q`,
`f(u)=E2[c H2]`, `r_a=f(u_a)-y_a`.

The canonical physical equations are

`w'=-2 m^{-1} sum_a r_a Delta1_a u_a`,
`K'=-2 m^{-1} sum_a r_a Delta2_a tensor H1_a`,
`c'=-2 m^{-1} sum_a r_a H2_a`,

where `(b tensor a)v=b E1[a v]`. They retain the full first row, including
coordinates not in the reference training span. Initially `(w,K,c)=(g,0,0)`
with `g~N(0,I_d)`.

## Required conclusion and quantifiers

There must be `rho_(m,d)>0`, `T_m<infinity`, `t_act in (0,T_m]`, and positive
activity margins, independent of width and every numerical resolution, such
that the following hold for every separately fixed set with
`max_a |u_a-e_a| < rho_(m,d)`.

1. The canonical raw equations have a unique strong autonomous solution
   through T_m, with the stated reached-state restart. Actual finite GF
   converges in probability, uniformly in time and over the full input
   sphere, to its prediction. The stated fixed finite same-population joint
   observation tuples converge in W2, including initialized/current hidden
   pairs and both directions of the reused middle action. Any raw-GD claim
   includes a separate proved step condition.
2. `L(T_m)<=1/4`. Both training-averaged squared paired activation
   displacements at t_act have a positive lower bound. These are actual
   nonlinear-flow assertions, separate from finite numerical diagnostics.
3. There is a specified nested, determining current observable hierarchy
   with compatible joint initialization, and a sequence of autonomous
   finite population closures. Each closure is well posed, has an own-state
   restart and has a state dimension fixed during evolution. Its
   initialization and coefficients use no trained trajectory.
4. After removing each fixed-order numerical approximation in its justified
   order, closure-order convergence is uniform in time and on the whole
   input sphere for predictions, and uniform in time in W2 for each declared
   fixed joint observation tuple. Risks and paired displacements converge.
   No approximation-order rate or arbitrary simultaneous limit is asserted.
5. A reusable numerical realization, deterministic semantic checks and
   explicit initialization/evolution/storage accounting accompany the proof.
   Population quadrature counts are not neural widths. Its retained action
   matrix indexes observable features, and its size does not grow with elapsed
   training steps.

The primary result fixes m,d and the data before the width/order limits.
It is not a growing-dimension theorem. For m>=2 the admitted family must
contain genuinely nonorthogonal configurations. For m=d=1, S^0 has no
nontrivial small angular perturbation; this edge case retains its literal
scope and is not described as a correlated family.

## Proof architecture and outstanding verification

- `REFERENCE_PROOF.md`: exact orthogonal reference, symmetry, global feature
  flow, fitting and a positive paired-activity time. Candidate target
  horizon is T_m=5m, subject to its complete proof.
- `PERTURBATION_PROOF.md`: reference coefficient cap, its transfer to raw
  Euler, supported-input perturbation cap, strong completion, actual finite
  approximation and uniform passive observations.
- `CX1_CLOSURE_PROOF.md`: initialized dictionaries, finite autonomous
  equations, error production and propagation, hierarchy sufficiency,
  numerical limits and their implementation correspondence.

These units are currently being authored independently. Their claims and
interfaces will be checked and assembled before any acceptance statement.
