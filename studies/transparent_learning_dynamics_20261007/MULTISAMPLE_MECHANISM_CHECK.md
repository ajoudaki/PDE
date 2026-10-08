# Bounded empirical check of multi-sample mechanisms

2026-10-07. This check reads the frozen
MULTISAMPLE_MECHANISM_PREDICTIONS.md, multisample_experiment.py, and selected
raw arrays/records under
data/generated/transparent_learning_dynamics_20261007/multisample_v1/.
It recomputes observables from saved trajectories. No training, new scientific
cohort, coefficient fit, or source edit was performed. This is not an
independent reproduction of the full campaign or a full-system accuracy review.
An independently delegated read-only check recomputed the m=8 control tables;
its only inputs were the same prediction note, experiment script, and raw data.

The initialized Gram direction persists through an appreciable early part of
fitting, then rotates, particularly in the lower layer for m=16. Frozen-middle
controls show increased lower-feature displacement and reduced upper displacement
in both tested dense seeds. Removing reciprocal return produces more individual
lower-feature displacement but weaker off-diagonal Gram changes at comparable
loss. The latter is an exploratory diagnosis of discrete ablated runs.
Full-horizon affine comparisons have substantial discretization error and do
not support a controlled late-time activation claim.

## Definitions and numerical conventions

The training set is \(\mathcal T=\{1,\ldots,m\}\), and the four passive indices
form \(\mathcal P\). The feature Gram is
\(C^\ell_{ab}(t)=n^{-1}h_{\ell,a}(t)^\top h_{\ell,b}(t)\), or the corresponding
population expectation in the causal model. Every change below subtracts its
own initialized Gram:
\(\Delta C^\ell(t)=C^\ell(t)-C^\ell(0)\).

TT means **off-diagonal training pairs only**, with both symmetric entries
retained; TP means all \(4m\) training-passive pairs. For either block B,
\[
\operatorname{rms}_B(X)=\left(|B|^{-1}\sum_{(a,b)\in B}X_{ab}^2\right)^{1/2}.
\]
For passive predictions RMS means the root mean square over the four passive
outputs, not a maximum over those outputs.

Saved \(h\) is the step in normalized time \(\tau=2t/m\). Its physical step
is \(hm/2\), and the common endpoint is \(\tau=19.2\). The saved
initial_curvature is \(\ddot C^\ell(0)\) with respect to **physical** time.
It must be multiplied by \((m/2)^2\) to represent curvature in \(\tau\).

Curvature-stage values in the next section use linear interpolation between
the two saved states surrounding the **first** loss-ratio crossing. Later
control-stage tables use the first saved crossing without interpolation,
as explicitly indicated. The root's main analysis uses first saved crossings;
these conventions can differ when the Gram direction turns rapidly.

## 1. Initial curvature direction through 20%, 50%, and 80% fitting

For dense width 512, seed 101, RK4 \(h=0.05\), define \(t_q\) at loss ratio
\(\mathcal L(t_q)/\mathcal L(0)=1-q\). Interpolate loss, time, and the Gram
linearly within that first crossing interval. The reported cosine is
\[
\frac{\langle\Delta C^\ell_B(t_q),\ddot C^\ell_B(0)\rangle_F}
{\|\Delta C^\ell_B(t_q)\|_F\|\ddot C^\ell_B(0)\|_F}.
\]
All denominators in this table are nonzero. No coefficient is refitted.

| m | Loss reduction | Normalized crossing time | C1 TT | C1 TP | C2 TT | C2 TP |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 20% | 0.652091 | 0.998481 | 0.996803 | 0.998085 | 0.996341 |
| 4 | 50% | 1.585104 | 0.982898 | 0.967126 | 0.977683 | 0.962746 |
| 4 | 80% | 2.651527 | 0.923083 | 0.875195 | 0.899134 | 0.865269 |
| 8 | 20% | 0.449351 | 0.996192 | 0.993829 | 0.996307 | 0.993185 |
| 8 | 50% | 1.119634 | 0.950732 | 0.929649 | 0.949171 | 0.923465 |
| 8 | 80% | 1.940430 | 0.771950 | 0.726654 | 0.760294 | 0.703604 |
| 16 | 20% | 0.916869 | 0.983761 | 0.981070 | 0.984656 | 0.981906 |
| 16 | 50% | 1.943655 | 0.750978 | 0.786767 | 0.805085 | 0.829726 |
| 16 | 80% | 3.158273 | 0.106989 | 0.330236 | 0.492626 | 0.622873 |

This supports persistence of the initialized direction early, not throughout
the learning path. Good directional prediction also does not mean good
magnitude prediction. The ratio
\(2\|\Delta C^\ell_B(t_q)\|_F/(t_q^2\|\ddot C^\ell_B(0)\|_F)\) at 80% loss
reduction, in the same four-column order, is:

| m | C1 TT | C1 TP | C2 TT | C2 TP |
|---:|---:|---:|---:|---:|
| 4 | 0.482146 | 0.548064 | 0.534715 | 0.618798 |
| 8 | 0.304532 | 0.393189 | 0.334380 | 0.431574 |
| 16 | 0.153065 | 0.153446 | 0.163919 | 0.213446 |

Thus the extrapolated initialized \(t^2\) magnitude considerably overpredicts
the change by this stage, even where its direction remains informative.
No universal pairwise label-sign interpretation follows from these matrices.

For m=16 the first **saved** 80% crossing is \(\tau=3.2\), where the lower
TT cosine is 0.088936, rather than the interpolated 0.106989 above.
This is a reporting-convention difference, not contradictory evidence.

### Time-resolution boundary

Direct comparison of \(h=0.1\) with \(h=0.05\) on common saved times gives:

| m | Full-horizon maximum output difference | Maximum C1 entry difference | Maximum C2 entry difference |
|---:|---:|---:|---:|
| 4 | \(6.22\,10^{-8}\) | \(1.49\,10^{-8}\) | \(3.15\,10^{-8}\) |
| 8 | \(1.43\,10^{-6}\) | \(3.63\,10^{-7}\) | \(6.89\,10^{-7}\) |
| 16 | 0.035105 | 0.003303 | 0.008924 |

The m=16 full-horizon refinement fails. It does not supply a controlled
continuous-flow reference over the entire experiment. The early curvature
windows are separately much better resolved: through the last common time
preceding its 80% crossing, the maximum C2 difference is
\(3.70\,10^{-6}\), and the largest difference between the interpolated
crossing cosines at any of its three stages is \(3.31\,10^{-4}\).
These observations support the reported early turning while preserving the
full-horizon limitation. The largest crossing-cosine refinement changes for
m=4 and m=8 are \(1.37\,10^{-4}\) and \(3.94\,10^{-4}\); interpolation on
different saved grids contributes to these stage differences.

The saved initialized curvature arrays are exactly equal between full and
frozen-middle lower layers, and between full and anchored-affine models in
both layers, for dense seeds 101 and 202. This verifies consistency with
the declared control formulas. It is not a separate empirical proof of an
initial-curvature theorem. No continuum initial-curvature estimate is
claimed for the response-off particle law from its single coarse mesh.

## 2. m=8 controls: endpoint feature motion and whole-trajectory differences

Feature displacement is
\[
M_{\ell,\mathcal A}(t)=
\left(|\mathcal A|^{-1}\sum_{a\in\mathcal A}
\|h_{\ell,a}(t)-h_{\ell,a}(0)\|_n^2\right)^{1/2},
\qquad \mathcal A=\mathcal T,\mathcal P.
\]
For causal arrays it is reconstructed from
\(C^\ell_{aa}(t,t)+C^\ell_{aa}(0,0)-2C^\ell_{aa}(t,0)\).
The following endpoint numbers use \(n=N=512\), Euler \(h=0.4\),
and \(\tau=19.2\). Each paired cell lists the two declared seeds:
dense 101/202, causal 1701/1702.

| System | Final relative loss | M1 training | M1 passive | M2 training | M2 passive |
|---|---|---|---|---|---|
| Dense full | \(1.36\,10^{-7}/3.73\,10^{-7}\) | .201145/.206104 | .216175/.223951 | .269416/.269374 | .306817/.301362 |
| Dense frozen middle | \(2.85\,10^{-6}/5.48\,10^{-6}\) | .257361/.257918 | .278325/.283150 | .248881/.246696 | .271735/.265898 |
| Dense anchored affine | \(4.25\,10^{-5}/8.90\,10^{-6}\) | .273870/.281655 | .291064/.292236 | .359917/.359951 | .411334/.407964 |
| Causal full | \(5.77\,10^{-5}/3.50\,10^{-7}\) | .203288/.204677 | .225897/.216597 | .275483/.269628 | .314786/.303068 |
| Causal no middle | \(3.38\,10^{-6}/6.37\,10^{-6}\) | .263346/.258880 | .294569/.278585 | .254814/.249490 | .283321/.271895 |
| Causal no reciprocal | \(2.56\,10^{-6}/6.17\,10^{-6}\) | .243303/.255822 | .273428/.271529 | .257548/.258353 | .297526/.293679 |

All matched controls have identical initial C1 and C2 arrays. The dense
frozen-middle endpoint increases lower motion by 25–28% on training inputs
and 26–29% on passives, while decreasing upper motion by 8% and 11–12%,
respectively. The same direction appears in the causal no-middle runs.
These are finite-cohort observations, not a theorem that freezing W always
redistributes learning this way.

The next entries are maximum over saved times of RMS
\(\Delta C^\ell_{\rm control}-\Delta C^\ell_{\rm full}\), paired within
the same nominal seed. The passive column is the maximum over time of
the RMS output difference.

| System/control | Seed | C1 TT | C1 TP | C2 TT | C2 TP | Passive output |
|---|---:|---:|---:|---:|---:|---:|
| Dense frozen middle | 101 | .015798 | .017188 | .034342 | .037846 | .081512 |
| Dense frozen middle | 202 | .013498 | .015042 | .032015 | .035298 | .078191 |
| Dense anchored affine | 101 | .035500 | .041594 | .089753 | .088780 | .168379 |
| Dense anchored affine | 202 | .039771 | .044911 | .095835 | .092807 | .182734 |
| Causal no middle | 1701 | .015090 | .015555 | .034156 | .037023 | .085347 |
| Causal no middle | 1702 | .013069 | .014495 | .033142 | .036139 | .077862 |
| Causal no reciprocal | 1701 | .029190 | .026530 | .049672 | .045523 | .113916 |
| Causal no reciprocal | 1702 | .029854 | .027223 | .048559 | .044831 | .100429 |

At each model's own first saved 1% loss-ratio crossing, full reaches
\(\tau=4.4\) and frozen middle reaches \(\tau=6.0\) in both dense seeds.
Frozen-minus-full motion differences \((M_{1,T},M_{1,P},M_{2,T},M_{2,P})\)
are (.053216,.057146,-.020625,-.033145) and
(.048935,.055269,-.022020,-.032815). The redistribution therefore persists
after a coarse matching of fitting progress, not only at the common endpoint.
The attained loss ratios differ slightly because these are saved crossings.

### Available control refinements

For dense seed 101 the maximum-time RMS difference between \(h=0.4\) and
\(h=0.2\), sampled on their common grid, is:

| Control | C1 TT | C1 TP | C2 TT | C2 TP | Passive output |
|---|---:|---:|---:|---:|---:|
| Frozen middle | .002794 | .002605 | .003406 | .003100 | .008007 |
| Anchored affine | .029555 | .033039 | .068799 | .074855 | .138751 |

Frozen-middle sensitivity is smaller than its observed control contrast in
these norms. At its refined endpoint its four motion values are
(.257928,.277674,.250520,.271583), retaining the same redistribution.
This is an observed numerical sensitivity check, not a rigorous error bound.
There is no dense full Euler \(h=0.2\) run in this control set; the separate
full RK4 pair supplies a different reference. There is also no own step
refinement of the causal no-middle or no-reciprocal circuits. Full-system
step refinement cannot be assigned to those altered circuits.

Affine refinement is 77–84% of the coarse affine-minus-full contrast in
these maximum-time norms. The coarse affine run has 11 loss-increasing
steps, with maximum relative-loss increase .046386 from \(\tau=10.8\)
to 11.2; the refined affine run has none. Thus the full-horizon affine
contrast is substantially contaminated by numerical error. Its endpoint
motion also changes materially on refinement to
(.241823,.248283,.329181,.370817). The late affine mechanism claim remains
unresolved by these runs.

## 3. Exploratory interpretation of reciprocal removal at matched loss

The following diagnostic was requested after the campaign. It was not a
predeclared discriminator. Use the first saved 1% loss-ratio crossing of
each \(N=512,h=0.4\) causal run: \(\tau=4.4\) for full and 6.0 for no
reciprocal. Actual loss ratios are .009534/.009164 for seed 1701 and
.009033/.009139 for seed 1702.

Let \(X=\Delta C^\ell_{\rm full}\) and \(Y=\Delta C^\ell_{\rm noR}\) at
these respective crossings. The projection coefficient in the last column
is \(\langle X,Y\rangle_F/\|X\|_F^2\); it measures the component of Y
along the full model's Gram-change direction. It is a diagnostic projection,
not a fitted coefficient used to predict training.

| Seed | Block | Full RMS | No-R RMS | Direction cosine | Projection coefficient |
|---:|---|---:|---:|---:|---:|
| 1701 | C1 TT | .046535 | .026484 | .905781 | .515504 |
| 1701 | C1 TP | .048091 | .035502 | .895975 | .661436 |
| 1701 | C2 TT | .103056 | .075244 | .995909 | .727142 |
| 1701 | C2 TP | .101323 | .080190 | .994047 | .786719 |
| 1702 | C1 TT | .046259 | .025708 | .882008 | .490162 |
| 1702 | C1 TP | .047058 | .033791 | .879864 | .631802 |
| 1702 | C2 TT | .100753 | .072651 | .996717 | .718717 |
| 1702 | C2 TP | .101994 | .080225 | .996284 | .783646 |

Yet the training lower-feature displacement increases from .189704 to
.230225 in seed 1701 and from .188867 to .237672 in seed 1702. Passive
lower displacement likewise increases from .209844 to .260178 and from
.198733 to .253855.

Thus the no-R runs have more individual lower-feature movement but weaker
off-diagonal feature associations. Their lower Gram direction is also
moderately rotated; its component in the full direction is roughly halved
on TT and reduced to 63–66% on TP. Upper Gram changes keep nearly the same
direction and shrink mainly in magnitude. Diagonal norm changes alone
cannot account for the reported TT effect because TT excludes diagonals.

This supports distinguishing amount of feature displacement from the
associations it builds. It does not establish an exact loss of microscopic
neuron-motion coherence, a universal reduction of lower learning, or an
accuracy claim about a continuous response-off flow. The comparison is
two discrete particle runs per system with no ablation-specific refinement.

## 4. Activation sensitivity: measured drift and a restricted early contrast

Dense full \(h=0.4\) runs at m=8 have nonzero passive gate evolution:
the two-seed mean squared gate drifts are .0297266 in layer 1 and .0500946
in layer 2, corresponding to RMS drifts .172414 and .223818. For seed 101,
the refined full RK4 endpoint gives .169581 and .222094. These quantities
measure actual changes of \(\tanh'\), not an intervention effect by themselves.

A narrower affine comparison survives the available early refinements.
At each model's first saved 1% loss-ratio crossing in seed 101:

| Model | Normalized time | Actual loss ratio |
|---|---:|---:|
| Full Euler .4 | 4.4 | .008236 |
| Full RK4 .05 | 4.25 | .009946 |
| Anchored affine Euler .4 | 4.0 | .007021 |
| Anchored affine Euler .2 | 3.8 | .008279 |

RMS differences at those states, in the order
\((C1\ {\rm TT},C1\ {\rm TP},C2\ {\rm TT},C2\ {\rm TP},f_{\mathcal P})\),
are:

- Coarse affine minus coarse full:
  (.017099,.019526,.027692,.046509,.057827).
- Affine .2 minus affine .4:
  (.001353,.001472,.004079,.003562,.008753).
- Full Euler .4 minus full RK4 .05:
  (.001522,.001718,.004797,.004086,.013809).
- Affine .2 minus full RK4 .05:
  (.017723,.019850,.027452,.046186,.058879).

The early contrast remains after both available refinements and exceeds
their observed changes in these norms. This supports a restricted qualitative
effect around this fitting stage. It does not resolve the late affine
instability, provide a certified numerical bound, or remove the mismatch
between attained losses. Earlier coarse crossing comparisons can have much
larger threshold overshoot and are less discriminating.

The saved experiment records gate drift and feature displacement, but not
the activation remainders or their readout projections proposed in the
prediction note. Those specific decompositions cannot be reported as measured
here. The full-versus-affine contrast changes the complete forward/backward
dynamics and must not be called a pure upper-gate contribution.

## 5. Retained readout history is directly reconstructible

For each full causal \(N=512,h=0.4\) run with seed 1701 or 1702, the exact
discrete readout identity is
\[
f_a^k=h\sum_{j<k,b\in\mathcal T}c_b^j C^2_{ab}(k,j),
\]
since \(h=2\Delta t/m\). Direct reconstruction from saved C2 histories
agrees with all panel outputs at all times within \(2.0\,10^{-15}\).

At the final \(\tau=19.2\), split writes at \(\tau=9.6\), as in the
predeclared half-horizon diagnostic. The table reports RMS across the
four **signed passive-output contributions**, with the two seeds separated
by slashes:

| m | Writes before 9.6 | Writes at/after 9.6 |
|---:|---:|---:|
| 4 | .356088/.370488 | .001543/.001245 |
| 8 | .502559/.500141 | .002356/.002632 |
| 16 | .306155/.485740 | .281026/.079569 |

Early writes dominate the fitted m=4 and m=8 passive endpoints in these
runs. In m=16, recent contributions are larger and much more variable.
The accumulated residual budgets \(h\sum_{j,b}|c_b^j|\) are
5.4717/5.0566, 8.1679/7.8101, and 73.9031/67.8241 for m=4,8,16.
This is consistent with the exact residual weighting of new writes and
with persistence of older information. Signed cancellations prevent these
RMS values from measuring total write activity, and the m=16 coarse
history is not a validated continuous-flow history.

## Scope and provenance

The script's initial-curvature formula uses the correct physical \(2/m\)
normalization. Its controls freeze the middle velocity or replace activations
and derivatives consistently by their initialized affine values. The numerical
comparisons above do not import two-input cubic coefficients or fit future
trajectories. All findings remain conditional on the fixed datasets and the
small listed ensembles.

Source snapshots read for this check:

- MULTISAMPLE_MECHANISM_PREDICTIONS.md:
  9d56c076afc7406080679324c902417f372ac904812c56b5e596d66d075a05b6.
- multisample_experiment.py:
  eb58b62ca466649989067cd1287aa199b99b41899b59536cec02baa186c78b2d.

Read-only computations used NumPy in a single-thread process and left the
raw arrays unchanged. The reviewed scope was mechanistic prediction, selected
controls, and their numerical sensitivity. Full-system ensemble accuracy,
all-time bounds, and an independent campaign reproduction are outside this
check.
