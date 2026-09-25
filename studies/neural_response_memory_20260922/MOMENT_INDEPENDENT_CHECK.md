# Independent check of the autonomous orthogonal moment experiment

Review scope: the explicitly assigned construction, protocol, engines, tests,
runners, and new/archived numerical artifacts identified below. No study
history, prior verdict, other-study theory, or external scientific source was
consulted. The
`solve-math-rigorously` skill was used. This is a scoped internal check, not an
independent promotion review or an established-material claim.

Status: mathematical construction, both engines, all thirty-four closure
runs, and all eight fresh dense-reference runs checked. The selected
refinements satisfy the prescribed empirical numerical gates. Exact-flow
accuracy is not certified by those gates; the smallest gaps require the
closure and reference sensitivity qualifications below.

## Exact identities and normalizations

Write `w_k=2k+1`, `L=1+s`, and let `A_k,B_k` be the source and forward moments
from the assigned route. Treat each training sample separately. Their activity
equations are

\[
 A'_k=u-kA_k/L-\sum_{j<k}w_jA_j/L,
 \qquad
 B'_k=h-kB_k/L-\sum_{j<k}w_jB_j/L.
\]

Indeed, differentiating the moving history integral gives its endpoint source
minus `L^{-1}` times the integral of `x ell'_k(x)`. The stated Legendre dilation
identity gives precisely these terms. Multiplication by `sdot=rho` gives the
physical-time equations, including `rho u=r delta2`.

The virtual prefix has zero source, so its exact cross integral is zero. Its
constant forward response has only moment `B_0=h(0)`, since its initial length
is one. Thus `A_k(0)=0`, `B_k(0)=1_{k=0}h(0)` are the correct initial values.

For a direct check of the reconstruction derivative, let `D=diag(w_k)` and
`T_kj=k` for `j=k`, `T_kj=w_j` for `j<k`, and zero otherwise. Entrywise,

\[
 T^T D+DT+D=ww^T.
\]

The diagonal entry is `(2k+1)w_k=w_k^2`; each off-diagonal entry is `w_kw_j`.
Consequently, for `S=L^{-1}sum_k w_k A_kB_k^T`, and endpoint projections
`U=L^{-1}sum_k w_k A_k`, `H=L^{-1}sum_k w_k B_k`,

\[
 S'=uH^T+Uh^T-UH^T.
\]

Since the learned middle matrix is `DeltaW=-2 sum_a S_a/(Mn)`, its discrepancy
from the canonical middle-layer velocity at the same current physical state is

\[
 E_2=\dot{\Delta W}+\frac{2\rho}{Mn}\sum_a u_ah_a^T
     =\frac{2\rho}{Mn}\sum_a(u_a-U_a)(h_a-H_a)^T.
\]

The positive sign, transpose, sample normalization, and factor `1/n` are
essential and are correct in the assigned formula. At initialization `H=h`,
so the defect vanishes even though `U=0`. Retaining the same `W0+DeltaW` in
forward and transpose actions makes the outer-layer updates the original
gradient components at the surrogate's current physical state. Substituting a
different transpose or dropping `W0` would invalidate that statement.

The formulas for derivative memories are also consistent: integration by
parts gives `B_k=L(1_{k=0}h-J^h_k)` and
`A_k=L(1_{k=0}u-u(0)q_k(1/L)-J^u_k)`. The `u(0)` term accounts for the jump
from the virtual zero source. Differentiating these two identities gives the
route's displayed derivative-coordinate ODEs; neither introduces an implicit
dependence on an unknown derivative.

## Rational lift and what it does establish

On `rho>0`, the lifted response equations are rational in the current state.
The factors `1-h_l^2` are the exact tanh derivatives on the initialized
manifold. The equation for `h2dot` must use the derivative of the actual moment
reconstruction, including its interval-transport terms. The identity

\[
 \frac{d}{dt}\left(\rho^2-M^{-1}\sum_a r_a^2\right)=0
\]

follows directly from `rhodot=mean(r fdot)/rho`. Activation consistency follows
by differentiating the reconstructed preactivations and matching their tanh
derivatives. Local uniqueness on `rho>0,L>0` preserves these identities for
exact solutions initialized consistently. The stationary zero-residual
initial condition is a separately prescribed boundary case; the division by
`rho` does not define a rational vector field on that boundary.

Therefore the lift represents the closure exactly on its invariant manifold.
It does not remove the middle-layer closure defect, prove global existence,
or guarantee that a finite-step numerical trajectory stays on the manifold.

## Endpoint estimate and convergence claim

For an endpoint projection of order `P`, define
`F(x)=(ell_P(x)+ell_{P-1}(x))/2`. Its derivative is the endpoint projection
kernel, `F(1)=1`, and `F(0)=0`. Stieltjes integration by parts therefore gives

\[
 g(L)-g^P(L)=\int_0^L F(\tau/L)\,dg(\tau).
\]

The known source jump must be included in `dg`; omitting it would make the
initial source identity false. Since `|ell_k|<=1`, source total variation at
most `V` gives `||u-u^P||_n<=V`. If `h` is activity-Lipschitz with constant
`H`, its constant virtual prefix preserves that bound, and Cauchy--Schwarz
with `integral_0^1 ell_k^2=1/(2k+1)` gives

\[
 \|h-h^P\|_n\le\frac{LH}{2}
 \left((2P+1)^{-1/2}+(2P-1)^{-1/2}\right)
 \le\frac{LH}{\sqrt{2P-1}}.
\]

Here `||v||_n=||v||_2/sqrt(n)`. For a rank-one matrix,
`||ab^T||_F/n=||a||_n||b||_n`. Summing the defect terms over `M` samples hence
gives the stated estimate

\[
 \|E_2\|_F\le\frac{2VH(1+S)}{\sqrt{2P-1}}\rho,
 \qquad \int_0^\infty\|E_2\|_Fdt\le c_PS,
\]

provided total activity is at most `S` and the regularity constants hold
uniformly along the relevant closure solutions. The neuron normalization
eliminates the apparent extra factor of `n`; the matrix norm here is the
ordinary Frobenius norm of `E2`, not the norm of `Kdot`.

The conditional all-time argument is sound with the explicitly required
common bounded smooth forward region, uniform source constants, coercive
loss decay for the original field throughout that region, perturbation-to-loss
bound, physical velocity bound, and justified containment. The decay bootstrap
controls activity; finite-time perturbation convergence and uniformly small
tails then give all-time convergence. Each assumption is substantive. In
particular compatible sample geometry alone supplies neither the required
source variation nor the stability and containment conditions. Bounded
source magnitude does not bound source total variation. The route correctly
does not claim that the hard-task experiments prove these assumptions or a
width-uniform theorem.

## Numerical controller audit

The runner uses the Heun/Euler discrepancy for every state component and for
the induced learned matrix. Its low-rank difference identity is exact:

\[
 L_cR_c^T-L_eR_e^T=(L_c-L_e)R_c^T+L_e(R_c-R_e)^T.
\]

Thus the matrix controller does not merely compare factor coordinates. Its
Frobenius norm is an absolute physical matrix norm with a relative scale based
on the learned increment. This is consistent with the assigned protocol.
The Gram contraction may lose relative accuracy near cancellation and clamps
negative roundoff to zero. Component control and independent trajectory
refinement remain necessary; a small reported matrix ratio alone is not a
certificate.

The runner's `status=fit` records the first located crossing of the **lifted**
training loss. Physical predictions are separately recomputed with tanh.
Therefore success requires postprocessing the saved state with the physical
training loss as well as the lift drift; `status=fit` alone is insufficient.
The loss-crossing location uses linear state interpolation, another finite-step
error covered empirically by refinement, not an exact event solve.

The protocol's drift diagnostics are sampled every 25 accepted steps plus
the endpoint. Their maxima are sampled maxima, not rigorously certified
continuous-time or every-step maxima. A strict claim about the entire
trajectory's maximum drift would require denser checks or a bound. Endpoint
primary/refined comparisons at their respective first-loss crossings test
endpoint numerics but do not by themselves validate intermediate matched-time
errors. Matched-time errors should be compared across refinements where both
trajectories saved the reference time.

The nested 4096/8192 circle calculation checks two quadrature grids. It is an
empirical grid-convergence diagnostic, not a uniform-in-angle error bound.
Unsuccessful or unresolved cells must remain in the report. A dense reference
is itself numerical evidence with inherited validity limits, and comparison
with its endpoint must not be labeled exact canonical-flow error.

## Executed identity and implementation checks

- Exact rational-arithmetic checks passed at `P=1,3,7,15` for polynomial
  orthogonality, the dilation identity, `T^TD+DT+D=ww^T`, and the endpoint
  projection kernel identity.
- All eleven CPU tests passed using
  `PYTHONPATH=code /home/amir/miniconda3/bin/python -B -m unittest discover -s studies/neural_response_memory_20260922 -p 'test_*moment_engine.py' -v`.
  This includes six bin checks and five orthogonal checks, executed after
  reading both implementations and test files. An initial attempt with the
  default interpreter lacked `torch`; switching to the assigned interpreter
  resolved that environment issue.
- The orthogonal engine implements the displayed formulas with matching
  derivative factors and a shared transpose. Its inherited `C_j` variables
  are redundant copies of `L`; the executable retains `P` more moving scalars
  than the minimal mathematical state count in the route. Saved
  `moving_scalars` should be used for actual implementation comparisons.

## Independent primary artifact verification

Authorized outputs: `data/generated/neural_response_memory_20260922/orthogonal_primary01/`
and only the two archived `arrays.npz` files named by these runs' summaries.
All six completed primary cells were checked. The independent computation
used NumPy formulas directly, without importing either experiment engine.

The canonical NumPy seed reproduced all three archived initial arrays
bitwise. The selected reference endpoint was the final saved parameter state
at its own MSE `0.001` crossing: time `156.95289234260915` for two outliers and
`237.73297435005725` for quadrant alternating. Reconstructing all 8192 dense
endpoint predictions agreed with the archived prediction arrays within
`4.9e-15`. This confirms reference selection and saved forward evaluation; it
does not independently certify the archived ODE integration accuracy.

For every candidate, independent reconstruction of all 8192 endpoint
predictions agreed with its saved array within `3.3e-13`. Inputs, labels,
endpoint input grid, and source hashes matched. Recomputed circle RMS differed
from the summary by less than `4.4e-16`. All saved matched-time RMS values
recomputed exactly from the assigned reference snapshots, with snapshot times
aligned within `1e-8`. Accepted times were strictly increasing, accepted local
error ratios were finite and at most one, and all stored losses preceding the
endpoint exceeded the first-crossing threshold. The redundant `C=L` drift
was at most `5.7e-14`.

| Task | P | Circle RMS against dense own endpoint | Physical endpoint MSE | Sampled maximum h1 drift | Primary drift gate |
|---|---:|---:|---:|---:|---|
| Two outliers alternating | 1 | 0.2362585323 | 0.001000336727 | 0.002451728 | Fails |
| Two outliers alternating | 3 | 0.07297700234 | 0.001000094455 | 0.001839193 | Fails |
| Two outliers alternating | 7 | 0.004697759517 | 0.001000273489 | 0.001861412 | Fails |
| Quadrant alternating | 1 | 0.3415939162 | 0.001000703494 | 0.002007759 | Fails |
| Quadrant alternating | 3 | 0.04570203220 | 0.001000262453 | 0.001235344 | Fails |
| Quadrant alternating | 7 | 0.001605203919 | 0.001000231343 | 0.001204447 | Fails |

The physical endpoint losses all satisfy the supervisor's pre-outcome
additional gate of lying within 1% of `0.001`. The 4096/8192 circle RMS
differences were below `6.3e-16`, comfortably within `1e-5`. Sampled h2 drift
was below `0.000650` in every primary cell. Nevertheless **all six primary
cells fail the h1 drift threshold** of `0.001`, including quadrant `P=3,7`,
whose endpoint drifts alone would have passed. The prescribed refinement
branch is required before these can be presented as valid approximation
measurements. The table preserves the primary outcomes without treating a
lifted `fit` status as scientific validation.

## Refinement validation

All six cells under `orthogonal_refined01/` were independently reconstructed
and checked in the same way. Predictions matched the saved arrays within
`3.4e-13`, physical loss summaries within `6e-15`, and circle RMS summaries
within `4.4e-16`. Matched-time RMS values again recomputed exactly. Source
hashes, data alignment, finite accepted error ratios, and stored first-loss
crossings passed the same checks.

| Task | P | Refined circle RMS | Sampled max h1 drift | Sampled max h2 drift | Primary/refined endpoint max difference |
|---|---:|---:|---:|---:|---:|
| Two outliers alternating | 1 | 0.2363092495 | 0.000617654 | 0.000323785 | 0.000287617 |
| Two outliers alternating | 3 | 0.07296150612 | 0.000478074 | 0.000281989 | 0.000204536 |
| Two outliers alternating | 7 | 0.004669075279 | 0.000508204 | 0.000276110 | 0.000305753 |
| Quadrant alternating | 1 | 0.3414487068 | 0.000673072 | 0.000324052 | 0.000496446 |
| Quadrant alternating | 3 | 0.04569721315 | 0.000478320 | 0.000321823 | 0.000172220 |
| Quadrant alternating | 7 | 0.001647647022 | 0.000350054 | 0.000315570 | 0.000233546 |

Both sampled activation drift maxima decrease under refinement and are below
`0.001` for all six cells. Their physical endpoint MSE values remain within
1% of `0.001`. Nested circle RMS differences are below `8.2e-16`.
Primary/refined endpoint maximum differences are all below `0.000497`, well
inside the predeclared `0.01` gate. The largest primary/refined prediction
change over common saved reference-time snapshots is `0.000403`. Thus the
six **refined** cells pass the stated empirical numerical gates; this does
not erase the primary failures or certify continuous-time error bounds.

Four extra runs under `orthogonal_fine01/` use a further factor-four tolerance
refinement. Each was also independently reconstructed on the full 8192-point
grid. The largest saved-prediction reconstruction discrepancy was `4.0e-13`;
circle RMS and physical-loss summaries again agreed to roundoff. Their
sampled activation drift maxima decrease from level 1, and physical endpoint
losses and nested-grid checks remain within the stated gates.

| Task | P | Finest circle RMS | Sampled max h1 drift | Sampled max h2 drift | Level 1/2 endpoint max difference |
|---|---:|---:|---:|---:|---:|
| Two outliers alternating | 1 | 0.2363128121 | 0.000157931 | 0.000082541 | 0.000060839 |
| Two outliers alternating | 3 | 0.07295306056 | 0.000118904 | 0.000072219 | 0.000043317 |
| Two outliers alternating | 7 | 0.004663067534 | 0.000129075 | 0.000069793 | 0.000053892 |
| Quadrant alternating | 1 | 0.3414071377 | 0.000174987 | 0.000086189 | 0.000122599 |

The largest common-snapshot prediction change between levels 1 and 2 is
`0.000116090`. This additional check strengthens the empirical integration
validation without converting refinement differences into certified bounds.

## Optional third task: quadrant pairs

Both `P=3,7` runs in `orthogonal_primary01/` and their counterparts in
`orthogonal_refined01/` were independently checked. The selected dense
reference's initial arrays match the canonical seed bitwise, and its 8192
endpoint predictions reconstruct from its final saved weights within
`2.9e-15`. Candidate predictions reconstruct within `2.5e-14`; their metric
summaries and matched-time RMS arrays agree to roundoff. Source hashes,
training data, first-loss crossings, and accepted local error ratios pass
the same checks as the primary tasks.

| P | Primary circle RMS | Refined circle RMS | Refined max h1 drift | Refined max h2 drift | Endpoint refinement max difference |
|---:|---:|---:|---:|---:|---:|
| 3 | 0.002807723047 | 0.002815469925 | 0.000028560 | 0.000189208 | 0.000061410 |
| 7 | 0.0001198564180 | 0.0001203830179 | 0.000027857 | 0.000195631 | 0.000071804 |

Both orders pass the activation drift gate already at the primary level;
both activation maxima decrease under refinement. Refined physical training
MSE is `0.0009999455843` for `P=3` and `0.0009999482022` for `P=7`. Nested-grid
RMS differences are below `3.7e-17`; the largest common-snapshot refinement
change is `0.000094334`. These satisfy the prescribed numerical gates.

The `P=7` discrepancy `0.00012038` is smaller than the dense reference's
observed refinement RMS change `0.00021779`. Thus this row measures close
agreement with the selected archived endpoint; its exact canonical-flow
error at that scale is unresolved by the available reference pair.

## Inherited dense-reference sensitivity

The supervisor additionally authorized exact preceding archived dense arrays
for paired numerical sensitivity checks. Training data and endpoint grids
match across each pair. The measured changes at each dense run's own first
loss crossing are:

| Task | Earlier / selected archive run | Endpoint RMS change | Endpoint maximum change |
|---|---|---:|---:|
| Two outliers alternating | `scaling_discovery_primary01` / `scaling_discovery_refined01` | 0.0004393774 | 0.0009031267 |
| Quadrant alternating | `diverse_refined01` / `diverse_fine_early01` | 0.0006460516 | 0.0021790603 |
| Quadrant pairs | `scaling_discovery_primary01` / `scaling_discovery_refined01` | 0.0002177898 | 0.0007581159 |
| Quadrant center edges | `diverse_primary01` / `diverse_refined01` | 0.0010670533 | 0.0051363088 |
| Equal mixed odd | `diverse_primary01` / `diverse_refined01` | 0.0000303133 | 0.0000757499 |

Each path is under
`data/generated/random_dictionary_learned_circle_20260920/<run>/<task>_full/arrays.npz`.
These are inherited refinement sensitivities, **not certified reference error
bounds or lower bounds**. The quadrant-alternating `P=7` candidate error of
about `0.00165` is only about 2.55 times the dense reference's RMS change. It
supports a small measured discrepancy on this benchmark, but fine numerical
digits or errors much below that reference sensitivity should not be
interpreted as resolved exact-flow accuracy.

## Authorized extension and antipodal reduction

The protocol extension, updated runner, and frozen initial runner were read
after the supervisor authorized two more original tasks and the missing
quadrant-pairs `P=1` comparison. The frozen initial runner's SHA-256 is
`a838a90d903665765a46a2b613c71e8509d5fea2326eed2fe752b29623ed369c`, exactly the
runner hash in the initial-campaign summaries. Later runs record the revised
runner hash; the two versions are distinguishable and reproducible.

For the bias-free tanh network, `f_theta(-x)=-f_theta(x)` for every parameter
state. Differentiating this identity with respect to each parameter gives
`grad_theta f_theta(-x)=-grad_theta f_theta(x)`. For paired labels `-y`, both
the residual and its parameter derivative change sign. Hence the squared
loss and its gradient contribution are identical for the two members of
each antipodal pair. Averaging eight samples is therefore exactly equivalent
to averaging four uniformly weighted representatives on exact antipodal
inputs. The block mobilities do not affect that equivalence.

The closure also respects this reduction: `h1,h2,r,u,A,B` change sign between
opposite samples, while `delta2` is unchanged. Thus both moment factors change
sign, their matrix product is unchanged, and the factor of two in the
eight-sample sum cancels the doubled sample-count denominator. The lifted
responses and the activity clock preserve these relations for exact dynamics.

The archived `equal_mixed_odd` inputs are antipodal to within `1.23e-16` and
their labels are exactly opposite. Direct independent full-eight versus
first-four canonical loss/gradient evaluations at both the initial and final
archived states agree within `4.45e-16` for every gradient component and
`2.4e-18` for the loss. Thus the mathematical equivalence applies up to the
archived coordinate roundoff. The actual executed sample count is four;
history rank bounds are `4P`, and history vector counts are `8P`. Comparisons
must use these actual counts rather than the eight-sample task label.

All twelve added-task primary/refined states were independently reconstructed
on the full circle grid. Their saved predictions agreed within `3.0e-14`;
source hashes, original and used inputs/labels, moment ranks, history vector
counts, actual moving-state sizes, physical-loss summaries, matched-time RMS
arrays, accepted local-error ratios, and first-loss crossings passed the
same checks. Both new dense archive endpoints reconstruct from their final
saved weights within `2.9e-15`, and both initializations match bitwise. For
every equal-mixed endpoint, the recomputed original-eight and used-four
physical losses differ by at most `8.3e-18`.

| Task | P | Primary archive RMS | Refined archive RMS | Refined max h1 drift | Refined max h2 drift | Endpoint refinement max difference |
|---|---:|---:|---:|---:|---:|---:|
| Quadrant center edges | 1 | 0.04561449636 | 0.04560434797 | 0.000097845 | 0.000030018 | 0.000198150 |
| Quadrant center edges | 3 | 0.004876969017 | 0.004872119032 | 0.000040167 | 0.000036667 | 0.000120109 |
| Quadrant center edges | 7 | 0.001296419433 | 0.001302212979 | 0.000040506 | 0.000036878 | 0.000131238 |
| Equal mixed odd | 1 | 0.01238844548 | 0.01239363740 | 0.000020408 | 0.000057403 | 0.000016186 |
| Equal mixed odd | 3 | 0.0005155113645 | 0.0005201302437 | 0.000019195 | 0.000054310 | 0.000012518 |
| Equal mixed odd | 7 | 0.00001652403509 | 0.000009388095008 | 0.000019502 | 0.000053988 | 0.000015004 |

Both primary and refined levels satisfy the activation drift threshold, and
both activation maxima decrease for every order. Refined physical endpoint
MSE ranges from `0.0009998536` to `0.0010000045`, within the 1% gate. Nested
circle RMS changes remain at roundoff. The largest primary/refined change
over common stored reference-time snapshots is `0.000360663`. Thus these
selected refinements pass all prescribed empirical gates.

For both new tasks, `P=7` error is below three times the inherited dense
reference RMS sensitivity, triggering the prospectively specified fresh
dense-reference branch. The equal-mixed archive discrepancy is also smaller
than its own closure endpoint refinement change. No exact-flow claim at the
`1e-5` scale follows from this archived comparison alone.

The added quadrant-pairs `P=1` primary/refined pair also passes all checks.
Its archived-reference circle RMS changes from `0.01927756885` to
`0.01928028895`; the endpoint refinement maximum difference is `0.000105029`
and the common-snapshot maximum change is `0.000270505`. The refined physical
training MSE is `0.0009999476943`; sampled h1/h2 drift maxima decrease to
`0.000034373` and `0.000142543`. Both 8192-point endpoint reconstructions agree
with saved predictions within `1.7e-14`, and all stored metric/source checks
pass. This completes the authorized `P=1,3,7` comparison for all five tasks.

## Fresh dense-reference implementation audit

The explicitly frozen `refine_dense_reference.py` was read completely; its
SHA-256 is
`c1b58a9e604df478237826cc0e19c91dc8815d3922831bd9925aa5accf01d43d`.
It evolves the actual dense weights with fresh tanh evaluation and the
canonical original-eight-sample loss, including all antipodal pairs for equal
mixed odd. The Heun/Euler controller uses the learned dense matrix increment
in its Frobenius scaling. It localizes the physical-loss crossing, saves the
final physical state without a snapshot axis, preserves archived inputs and
grids, and captures initial-array/reference/source hashes. Capped or failed
integrations retain a distinct status. The dense flow's monotonic-loss
rejection is appropriate for its canonical gradient field; it does not alter
the closure runner's allowed nonmonotone behavior.

An independent seven-neuron CPU autograd calculation of the canonical
unhalved MSE, followed by the prescribed block mobilities, agrees with the
dense RHS within `5.6e-17`. A separately written two-stage Heun calculation
matches the dense refiner's candidate bitwise. A bounded three-step smoke
integration ends with a non-fit cap status and finite accepted error ratios
at most one. These checks establish the implemented field and local solver
arithmetic; accuracy of the new dense endpoints remains subject to their
own numerical refinements and artifact checks.

## Fresh dense-reference artifact verification and final accuracy limits

All eight outputs under `dense_reference01/` were checked independently with
NumPy forward evaluation on all 8192 endpoint inputs. Reconstructed endpoint
predictions and the initial/final stored circle snapshots agree within
`4.5e-15`; physical endpoint MSE agrees with each saved summary within
`2.8e-17`. Every run has physical MSE at its located first `0.001` crossing, finite
accepted local-error ratios at most one, increasing stored times, the original
eight inputs/labels, and the expected final-state layout. Canonical initial
array hashes, saved NPZ hashes, selected-reference NPZ hashes, and the frozen
refiner source hash all match. These checks found no mislabeled final state,
reference substitution, loss-normalization mismatch, or antipodal weighting
error.

| Task | Dense level 1/2 RMS change | Dense level 1/2 max change | Selected archive / dense level 2 RMS change |
|---|---:|---:|---:|
| Quadrant alternating | 0.00007443041 | 0.0001891730 | 0.0004203214 |
| Quadrant pairs | 0.00006269332 | 0.0002190677 | 0.00004651018 |
| Quadrant center edges | 0.00001279272 | 0.00006124361 | 0.0002775780 |
| Equal mixed odd | 0.0000003213610 | 0.0000006758799 | 0.000006712147 |

Recomputing the selected closure endpoint discrepancies against the finer
fresh dense endpoint gives:

| Task | P=1 RMS | P=3 RMS | P=7 RMS |
|---|---:|---:|---:|
| Quadrant alternating | 0.3413178440 | 0.04561127769 | 0.001552335372 |
| Quadrant pairs | 0.01928125565 | 0.002817610427 | 0.0001185023490 |
| Quadrant center edges | 0.04558160604 | 0.004877763091 | 0.001307644507 |
| Equal mixed odd | 0.01239954308 | 0.0005256654313 | 0.000003707871743 |

All corresponding 4096/8192 RMS changes are below `8.1e-16`. These are new
reference comparisons, kept separate from all archived-reference tables
above. No old baseline score can be compared against this changed target
without recomputing that baseline's predictions against the same fresh
reference. This audit does not reinterpret old baseline scores as fresh-target
scores.

The selected closure's own previous-to-selected endpoint RMS changes at `P=7`
are `0.00001819737` for two outliers, `0.00008117215` for quadrant alternating,
`0.00002242560` for quadrant pairs, `0.00002740811` for quadrant center edges,
and `0.000008593672` for equal mixed odd. These are empirical sensitivities,
not certified error bounds. In particular:

- Equal mixed odd's measured fresh-reference gap `0.000003708` is smaller
  than its closure refinement change `0.000008594`. The computation supports
  close agreement, but does not resolve its exact-flow error to those digits.
- Quadrant pairs' measured gap `0.0001185` is only about 1.9 times its fresh
  dense refinement change `0.00006269`; its precise exact-flow error remains
  unresolved at this scale as well.
- The larger high-order gaps on quadrant alternating and center edges exceed
  the observed closure and fresh-reference sensitivities, supporting the
  reported finite numerical order trend without establishing an asymptotic
  rate or a rigorous error bound.

All forty-two runs are accounted for: thirty-four closure runs and eight
dense references. Summing closure-reported wall time and dense-reported
integration time gives a conservative integration total of `973.36` seconds;
the sum of all reported wall times is `981.37` seconds. These are within the
prospectively authorized 44-run and 3600-integration-second caps.

## Canonical-notation construction check

The separately authorized `MOMENT_CONSTRUCTION.md` was read completely. Its
identifications `m1=B`, `m2=A`, `Q_rms=rho`, `Q_length=L`, and `W2=W0+K/n`
match the independently checked equations. The displayed `E` has the correct
sample/width factors and sign. Its initial zero-defect claim holds for each
initialization separately and consequently also under a Gaussian average;
it certifies only the initial derivative.

For precision about its conditional all-time argument, on the assumed common
bounded smooth region let the physical canonical vector field have Lipschitz
constant `Lambda` in a norm controlling the defect block. On a fixed interval
`[0,T]`, the same initial condition gives

\[
 \sup_{t\le T}\|\widehat\theta_P(t)-\theta(t)\|
 \le e^{\Lambda T}\int_0^T C\|E_P(t)\|_Fdt
 \le C e^{\Lambda T}c_PS.
\]

The assumed perturbed loss-decay estimate and velocity bound give uniformly
vanishing parameter tails after time `T`. First taking `P` large for fixed
`T`, then taking `T` large, yields uniform-in-time convergence under those
assumptions. The construction note keeps these assumptions conditional and
does not infer them from compatible geometry or the finite experiments.

No mathematical or implementation blocker was found within the assigned
scope. The supported outcome is an explicit autonomous rational closure,
an exact physical-defect identity and conditional convergence result, and
refinement-checked finite benchmark evidence with the accuracy qualifications
above. It is not a compatibility-only global theorem or established-material
promotion.
