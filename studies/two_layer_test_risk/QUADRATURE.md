# Deterministic check of the matched cubic coefficient

Agent `quadrature_check`, 10 September 2026. This is an internal implementation
and quadrature check of the fixed witness. It is not a promotion review and
contains no certified sign theorem.

**Outcome:** the three authorized quadratures produce positive coefficients,
`2.9320434e-4`, `2.7768895e-4`, and `2.7307732e-4`. The final change is still
1.6888%, above the preregistered 1% resolution trigger. Thus numerical
convergence remains inconclusive. All allowed resolutions have been used and
computation stops. No integration-error enclosure is claimed, including for
the numerical sign. The coefficient is small and multiplies `t^3`; the check
provides no finite-time effect size or usable time interval.

## Scope and exact calculation checked

The source is [check_coefficient.py](check_coefficient.py), SHA-256
`2f6b9cb2c36415fcd910a4e5e16bb4eaa57ec450a7aef81c95a2a562c35728a3`.
No maintained implementation API was used. The population flow and its
remainder are handled by the other study arguments. This file checks the
finite Gaussian expectation formulas entering their cubic coefficient.

Both initial hidden layers use tanh, input dimension is two, training angles
are `0, pi/5, -pi/5`, labels are `1, (1-sqrt(5))/4, (1-sqrt(5))/4`, and
`p=y/3`. The unit input vectors are `u(alpha)=(cos(alpha),sin(alpha))`,
so `G_ab=u_a dot u_b` is unchanged from the canonical input convention.
The test teacher is `cos(3 alpha)` on the uniform whole circle. All mobility
multipliers are one. No teacher, data, parameter or initialization search
was performed.

Here are the formulas independently reconstructed before implementation.
Indices `a,b` range over the three training examples. For a passive `x`,
include its coordinate in the joint tuple, with `p_x=0`.

- First population: `z_i=u_i dot g`, `g~N(0,I_2)`, `h_i=tanh(z_i)`,
  `e_i=1-h_i^2`, `Q_ij=E_1[h_i h_j]`.
- Upper population: `Y~N(0,Q)`, `H_i=tanh(Y_i)`, `d_i=1-H_i^2`,
  `dd_i=-2 H_i d_i`, `S=sum_a p_a H_a`, `U_i=S d_i`.
- If `P_i=(W_0^(2))* U_i`, the joint reverse responses are
  `P_i=mu_Ui+Gamma_i`, where
  `mu_Ui=sum_j h_j[p_j E_2(d_j d_i)+1_(j=i) E_2(S dd_i)]` and
  `E Gamma_i Gamma_j=V_ij=E_2(U_i U_j)`; Gamma is independent of the
  first population. Thus
  `D_ij=E_1[e_i e_j(V_ij+mu_Ui mu_Uj)]`.
- Put `F_x=sum_b p_b(Q_xb V_xb+G_xb D_xb)`.
- For the reverse query `F_a^test=H_x d_a`, its response mean is
  `mu_Fa=h_x E_2(d_x d_a)+h_a E_2(H_x dd_a)`. The cross covariance with
  the reverse query `U_b` is `C_ab=E_2(H_x d_a U_b)`. Therefore
  `B_x=sum_ab p_a p_b {Q_ab C_ab + G_ab[E_1(e_a e_b) C_ab
  + E_1(e_a e_b mu_Fa mu_Ub)]}`.

These means are obtained by taking named-coordinate derivatives, with the
Gaussian covariance and all deterministic coefficients held fixed. Both
partials are included when `x=a`. Singular passive tuples are allowed; the
source-response form avoids inverting their covariance. The independent
Gaussian term has the full covariance `V`, not `V` minus the response
covariance. This distinction preserves reuse of the same matrix.

For completeness, the factors entering the risk coefficient can be checked
without interpreting any quadrature as a trajectory. Write
`Z_a^(2)(t)-Y_a=2 t^2 R_a+o(t^2)` for the established onset expansion with
`p` in place of labels. The leading readout is `2t S`. Multiplying the
changed upper activation by this readout gives
`4t^3 E_2(S d_x R_x)=4t^3 F_x`. Integrating the changed activation in the
readout equation gives
`(4/3)t^3 sum_a p_a E_2(H_x d_a R_a)=(4/3)t^3 B_x`.
The moving-residual frozen terms are common through this order; their
cancellation, and control of the discarded terms, belong to the main
proof. Hence the candidate extra predictor coefficient is
`J_x=4F_x+(4/3)B_x`, while `a_x=2E_2(S H_x)` is the initial velocity.
The matching coefficient and risk coefficient are

```
beta = (sum_a p_a J_a) / (2 E_2 S^2),
C = 2 mean_circle[cos(3 alpha) (J_x-beta a_x)].
```

The identity used as an algebraic check is

```
A1 = p^T (G o D) p,
A2 = p^T (Q o V) p,
p dot J_train = (16/3)(A1+A2),
p dot a_train = 2 E_2 S^2.
```

The first identity follows because summing either `F_x` or `B_x` against
`p_x` gives `A1+A2`: in the second expression the sums turn `H_x` into `S`
and `mu_Fa` into `mu_Ua`. It consequently holds algebraically even after
consistent quadrature. Passing this invariant checks implementation and
normalization, but cannot certify quadrature accuracy.

## Numerical method, validity gates and stopping

Every normal integral uses float64 normalized tensor Gauss--Hermite
quadrature: order `q` uses standard-normal nodes `sqrt(2)*hermgauss(q).nodes`
and weights `hermgauss(q).weights/sqrt(pi)`. The first root has two Gaussian
coordinates; the upper training tuple has three. A fourth conditional
coordinate represents each passive input jointly with the training tuple.
The upper training factor is chosen to preserve the data's reflection
symmetry. Specifically, if

```
q0=Q00, q1=(Q01+Q02)/2, qd=(Q11+Q22)/2, qc=Q12,
b=q1/sqrt(q0), c=sqrt((qd+qc)/2-b^2), d=sqrt((qd-qc)/2),
L=[[sqrt(q0),0,0],[b,c,d],[b,c,-d]],
```

then `Y_train=L gamma` and interchanging the second and third training
inputs flips only `gamma_3`. Tensor quadrature is invariant under that sign
flip. Covariance averaging here removes only roundoff asymmetry; the
code checks `max|L L^T-Q|<=1e-13`. For a passive covariance column `q_x`,
solve `L c_x=q_x` and use
`Y_x=c_x dot gamma+sqrt(Q_xx-|c_x|^2) gamma_4`.
The original rank-two input root is never replaced by independent sample
coordinates, whitened, diagonalized or made nonsingular.

The code checks every four-input covariance eigenvalue against a
`1e-12*max(1,lambda_max)` roundoff tolerance. Only a negative conditional
variance inside that tolerance is clipped to zero. Actual worst deviations
were around `1e-16`, including duplicate or antipodal passive inputs.
Forward and reverse contractions retain all mean-response terms.

The pre-execution study README fixed `(q,N_angles)=(12,64),(20,128)` and
allowed `(28,128)` only if the first pair changed by more than 1% or changed
sign. The first pair changed by 5.5873%, authorizing the final run. The
first and final relative differences are computed against the higher-order
value; using the lower-order denominator also exceeds 1%, so the branch
does not depend on that convention. The code caps each run at 300 CPU
seconds and uses one numerical-library thread. No random sampling, training
integration, GPU work or additional resolutions were performed.

## Results and complete evidence

All three runs used exactly the same source hash above, exited successfully,
and saved the complete numerical output in `result.json` and provenance in
`metadata.json`. The latter includes the source/dependency hashes, command,
working directory, HEAD, environment, precision, thread settings and runtime.
`result.json` includes every passive angle's values, not only the aggregate.
Progress print lines are not separate scientific evidence.

| Hermite order / angles | `C` | Raw teacher projection `2 E(y J)` | Matching subtraction `2 beta E(y a)` | `beta` | CPU seconds |
|---|---:|---:|---:|---:|---:|
| 12 / 64 | 0.00029320434041843317 | 0.00047509807707096227 | 0.00018189373665252904 | 0.03763560026511558 | 0.2272 |
| 20 / 128 | 0.0002776889548020482 | 0.00044814131540169 | 0.00017045236059964178 | 0.03594524887994804 | 3.9674 |
| 28 / 128 | 0.00027307732354152825 | 0.00044110069984558626 | 0.000168023376304058 | 0.0354736257145771 | 16.8483 |

Absolute successive changes are `1.5515385616384977e-5` and
`4.611631260519945e-6`. Relative changes are `5.58732544%` and `1.68876390%`.
The three `p dot J` errors against `(16/3)(A1+A2)`, normalized by
`max(1,|left|,|right|)`, are respectively `4.34e-19`, `3.25e-19`, and
`1.08e-19`; the preregistered failure gate was `1e-9`. The largest parity
error across all quantities and runs is `2.36e-16`. The worst covariance
reconstruction error is `1.67e-16`. At order 28, the activation Gram minimum
eigenvalue is about `0.00905087`, while the input Gram has the intended zero
eigenvalue (`-2.22e-16` in floating point). The largest peak memory was
279904 KiB. Total measured calculation CPU time was 21.0430 seconds.

| Run directory under `data/generated/two_layer_test_risk/` | Result SHA-256 |
|---|---|
| [quadrature_20260910_gh12_a64](../../data/generated/two_layer_test_risk/quadrature_20260910_gh12_a64/) | `92237f9d7e0ea48ebe731cf8850100b96d9b04d73680d5e127c862c4bef225ac` |
| [quadrature_20260910_gh20_a128](../../data/generated/two_layer_test_risk/quadrature_20260910_gh20_a128/) | `fbc918cb54c8e04229469a941428665677c14855793d5afb6b668c2e2e0843d6` |
| [quadrature_20260910_gh28_a128](../../data/generated/two_layer_test_risk/quadrature_20260910_gh28_a128/) | `94ef9f751004aa55fd7ed4f1eba788a245efa869ee25c509e2d33b8295a60409` |

The exact executed commands, from `/home/amir/Codes/PDE`, were:

```sh
python studies/two_layer_test_risk/check_coefficient.py --order 12 --angles 64 --output data/generated/two_layer_test_risk/quadrature_20260910_gh12_a64
python studies/two_layer_test_risk/check_coefficient.py --order 20 --angles 128 --output data/generated/two_layer_test_risk/quadrature_20260910_gh20_a128
python studies/two_layer_test_risk/check_coefficient.py --order 28 --angles 128 --output data/generated/two_layer_test_risk/quadrature_20260910_gh28_a128
```

A future authorized reproduction must use fresh output names; the program
refuses an existing output directory. Its accepted resolution list does not
itself authorize rerunning or bypass the README's terminal stop.

Environment: Python 3.10.12, NumPy 1.26.4, Linux x86_64, float64,
`OMP_NUM_THREADS=OPENBLAS_NUM_THREADS=MKL_NUM_THREADS=NUMEXPR_NUM_THREADS=1`.
Initial/run HEAD was `02af27154186dd3e45f83989a8ddf78e92ebceff`.

## Read scope and remaining obligations

Read root AGENTS and workflow, the study's pre-execution README, both required
skills and their research-contract, evidence-ledger, decisive-experiments,
adversarial-audit and proof-search references. Read `docs/README.md` and
`docs/NOTATION.md`, the complete C.3 strict-activity proof with weighted extension,
the source-response derivation and singular-Gram argument in global nonlinear
Sections 3.1--3.4, its A.2 specialization, and the continuation disposition.
This is not an independent review of all C.1--C.2 flow/remainder dependencies;
no trajectory regularity or width theorem was inferred from this check.

Relevant read hashes:

- `docs/README.md`: `4d3cf63cf09e2effb3342f96272a754e8f8f127aada44179b893f6e1a36df453`.
- `docs/NOTATION.md`: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- `docs/global_nonlinear.md`: `8c575acb99ed713ef688cafb39fe9d8d8430e80815d2a69ac6686bac2cc19101`.
- `CONTINUATION_DISPOSITION.md`: `0dfdfcca323de9f8147529cfd18fa15cc5ff2899143f0af728c625531dea4f48`.
- `solve-math-rigorously/SKILL.md`: `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
- `investigate-conjectures/SKILL.md`: `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de`.

The sign obligation remains rigorous evaluation or bounding of the displayed
Gaussian/angle integral, with errors propagated through `Q`, response means,
`beta`, and both signed projections. A difference between finite quadrature
orders is not such an error bound. Finite tensor rules also have residual
orientation dependence; the symmetry-adapted construction prevents parity
artifacts but does not certify rotational accuracy. The last-order Gram
still has `Q00-Q11` about `7.77e-6`, whereas exact isotropy makes it zero.
A complete finite-time theorem additionally needs the actual predictor/risk
remainder and valid loss matching supplied by the main proof. None of those
obligations is replaced by the positive hidden energy or passing identities.
