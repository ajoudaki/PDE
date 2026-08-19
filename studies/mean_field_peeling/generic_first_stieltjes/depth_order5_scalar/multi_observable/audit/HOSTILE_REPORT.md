# Hostile audit of the amortized multi-observable MFP DAG

## Verdict

**Promote the hidden-activation `Gamma_04` head.**  The promoted object is the
two-dynamic-scalar, one-post-`R3`-sweep, one-dimensional-`M_nu` recurrence in
the [reduced transition table](../independent_route_a/REDUCED_GAMMA04_TRANSITIONS.md).
It is an algebraically
audited Gaussian normal form for arbitrary separately fixed `H` and `B=1` under
unit forward Grams.  The associated annealed statement is theorem-level only
conditional on the fixed-depth convergence and uniform-integrability bridge in
Section 10 below.

Every hard gate in the frozen hostile contract now passes.  In particular:

- three independently frozen local contractions agree on all raw `83/20/1`
  terms;
- after the exact `a43 -> tau` reduction, all three agree on the public
  `64/17` map;
- the reduced recurrence agrees at every layer with the independent
  response-aware reference for `H=2,3,4`, with zero atom discrepancies;
- the complete finite-width, equality-partition, width, and four-branch
  transpose audit closes;
- constant, linear, affine, parity, two-oracle, and smooth nonpolynomial gates
  pass.

The original hostile three-width `H=3` sine panel remains **inconclusive** in
the permanent record because its quadratic-curvature fit was saturated.  A
separately frozen pre-new-results extension added `n=512`, regenerated all old
samples, and passed the unchanged validity and curvature thresholds.  That
extension resolves the hostile empirical gate and permits overall promotion;
it does not rewrite the original decision.

The following are **not** promoted: minimality of the two-state head, growing
depth, positive-time Taylor convergence, any preactivation-RMS head, and every
proposed `F^(7)` closure/state/sweep/derivative-ceiling/complexity claim.

## 1. Independence and freeze chronology

The hostile contract was frozen before any producer `Gamma_04` formula was
read:

```text
AUDIT_CONTRACT.md sha256
50d1118655a0caeaf682612197dcd5359901bbc7586de255955f5829647dd688
```

Route H then produced two local contractions before producer inspection.
Version 1 used a four-forward-slot Wick engine and accidentally identified the
new moving fourth jet with an existing lower-grade slot.  It emitted 82 terms,
and later comparison found 31 `gamma04` and four `a41` discrepancies.  This is
a useful falsifier and remains frozen, not deleted.  Version 2 introduced the
required fifth forward Gaussian slot and emitted `83/20/1` terms.  Its source
and canonical output hashes are frozen in `HOSTILE_CANDIDATE_V2_FREEZE.json`.

Only then were the producer freezes inspected:

```text
Route A FINAL_ROUTE_A_FREEZE.json
5880677b1ea2567c8d44498fb634c4fc4ab771d43d7e5d37959b0df8d9deaab6

Route S FINAL_PRODUCER_FREEZE.json
3a3fd13beeeea4a0947f459d829932f4feb2770ccaac7ea951155e785614f02e
```

The hostile runner verifies these manifests and every still-current core
artifact hash.  Route A's historical pre-reduction manifest correctly has
older hashes for three prose/test files later superseded in its final manifest;
the frozen recurrence, transition table, contraction source, partition ledger,
finite-width source, and numerical control all retain their pre-reduction
hashes.

## 2. Exact identities independently rederived

Let

\[
p=n\nabla f,\qquad D=p\cdot\nabla,\qquad
X_\ell^{(r)}=D^r x^\ell\vert_{s=0}.
\]

The universal parameter-flow jets are, exactly at finite width,

\[
\theta'=p,\qquad \theta''=Dp,\qquad
\theta'''=D^2p,\qquad \theta^{(4)}=D^3p.
\]

For any scalar `C^4` observable `O`, its observable-specific readout is

\[
\begin{aligned}
O'&=O_1[p],\\
O''&=O_2[p,p]+O_1[Dp],\\
O'''&=O_3[p,p,p]+3O_2[p,Dp]+O_1[D^2p],\\
O^{(4)}&=O_4[p,p,p,p]+6O_3[p,p,Dp]+3O_2[Dp,Dp]
       +4O_2[p,D^2p]+O_1[D^3p].
\end{aligned}
\]

This proves the universal-observable principle at finite width: parameter jets
are reusable, while closure of a small deterministic observable head remains a
separate Wick--Stein obligation.

For the finite-width quantities

\[
Q_\ell=n^{-1}\lVert x^\ell\rVert^2,\qquad
\Gamma^\ell_{rs,n}=n^{-1}
 \langle X_\ell^{(r)},X_\ell^{(s)}\rangle,
\]

Leibniz's rule gives

\[
Q_{\ell,n}^{(k)}(0)=\sum_{r=0}^k {k\choose r}\Gamma^\ell_{r,k-r,n}.
\]

After the separately fixed-depth convergence and uniform-integrability
bridge, define
\(\Gamma^\ell_{rs}=\lim_n\mathbb E\Gamma^\ell_{rs,n}\) and apply the same
identity to the deterministic annealed coefficient limits.

The audited dictionary is

\[
\Gamma_{11}=w_\ell,\quad \Gamma_{02}=q02_\ell,\quad
\Gamma_{22}=q22_\ell,\quad \Gamma_{13}=q13_\ell,
\]

so, with `gamma04_ell=Gamma_04^ell`,

\[
Q_\ell''=2(w_\ell+q02_\ell),\qquad
Q_\ell^{(4)}=2\gamma04_\ell+8q13_\ell+6q22_\ell.
\]

Readout reflection gives

\[
X_\ell^{(r)}(T\theta_0)=(-1)^rX_\ell^{(r)}(\theta_0),
\]

hence odd hidden-feature derivatives vanish after annealed expectation, not
seedwise.  Under unit Gram,

\[
R_\ell''=w_\ell+q02_\ell,
\]

\[
R_\ell^{(4)}=\gamma04_\ell+4q13_\ell+3q22_\ell
 -3(w_\ell+q02_\ell)^2.
\]

Finally, after the separately fixed-depth annealed coefficient limit and
parity reduction, the label-one MSE coefficient germs have `c=2 eta` and the
formal relation `ds/dt=c(1-F(s))`,
`A=F'(0)`, `B=F'''(0)`, `q2=Q''(0)`, and `q4=Q^(4)(0)`, independent series
composition gives

\[
\begin{aligned}
Q_t''&=c^2q2,\\
Q_t'''&=-3c^3Aq2,\\
Q_t^{(4)}&=c^4(q4+7A^2q2),\\
Q_t^{(5)}&=-5c^5\{(3A^3+B)q2+2Aq4\}.
\end{aligned}
\]

`C=F^(5)(0)` first enters the reparametrization jet `s_6`, so its absence
above is required.  The displayed formulas are exact series composition of
the deterministic limiting coefficient germs, not seedwise finite-width
identities or a positive-time limit.

## 3. Semantic audit of the existing order-five graph

Each of `F1,R1,F2,R2,F3,R3` consists of exactly `H` nearest-neighbour cells.
The same local template is reused within one sweep, but the six sweep maps are
different jet-grade maps of dimensions `7,8,4,4,3,3`, totaling 29 propagated
backbone states.  At `d=1`,

\[
b_\ell=1,\qquad \tau_\ell=\ell+1,
\]

and a layer transition can still depend on `ell` through `tau_(ell-1)=ell`
and stored states.

All 29 derivative/covariance meanings were checked individually in
`BACKBONE_SEMANTIC_AUDIT.md`.  Two distinctions are essential:

- `v=G_04` is a frozen-line covariance and is not moving `Gamma_04`;
- in `F3`, `a32` is the response to the moving reverse-grade-two innovation
  `J2`; in `R3`, `d32` is the coefficient of moving feature `X2` in
  `Delta3=J3+d30 X0+d32 X2`.

The order-three graph is the autonomous projection

\[
(w,u,j;\ e11,c10)\subset(F1,R1).
\]

The terminal readings are

\[
A_H=\tau_H,
\]

\[
B_H=2(j_H+3u_H)+4\mathcal H,
\]

\[
C_H=2(k_H+5v_H)+10AC+10Bm2+4M2+12Am3,
\]

where the five named quantities are deterministic terminal folds defined in
the canonical Route-A report.  No new Gaussian evaluation occurs at readout.

## 4. Exact finite-width fourth-jet and transpose audit

For an internal matrix layer,

\[
W^{(r+1)}=n^{-1/2}\sum_{a=0}^r {r\choose a}
 \Delta_aX_{r-a}^{\mathsf T},
\qquad
Z_r=n^{-1/2}\sum_{a=0}^r {r\choose a}W^{(a)}X_{r-a}.
\]

At order four, the four moving weight jets contain `1+2+3+4=10` rank-one
branches.  Exact regrouping gives

\[
Z_4=F_4+(5\widehat\Gamma_{03}+10\widehat\Gamma_{12})\Delta_0
 +(9\widehat\Gamma_{02}+8\widehat\Gamma_{11})\Delta_1
 +7\widehat\Gamma_{01}\Delta_2+\widehat\Gamma_{00}\Delta_3.
\]

Before population parity, all four transpose-response channels are therefore
present:

| reverse jet | direct Gram coefficient | population status |
|---|---|---|
| `Delta0` | `4 Gamma03+6 Gamma12+4 Gamma21+Gamma30` | odd, zero |
| `Delta1` | `6 Gamma02+8 Gamma11+3 Gamma20` | survives |
| `Delta2` | `4 Gamma01+3 Gamma10` | odd, zero |
| `Delta3` | `Gamma00` | survives |

Thus the moving fourth preactivation jet uses

\[
l41=9q02+8w+a41,\qquad l43=1+a43.
\]

The activation Bell polynomial is exactly

\[
X_4=\phi^{(4)}Z_1^4+6\phi^{(3)}Z_1^2Z_2
 +3\phi''Z_2^2+4\phi''Z_1Z_3+\phi'Z_4.
\]

This both enumerates every finite-width branch and proves that the observable
head itself uses activation derivatives only through order four.

## 5. Equality partitions, width counting, and Wick--Stein closure

After forced covariance and transpose identifications are extracted, a product
with `m<=5` free neuron labels and equality partition `pi` has relative width
power

\[
n^{|\pi|-m}.
\]

The complete block-count census is

| `m` | partition counts by decreasing block number |
|---:|---|
| 1 | `1` |
| 2 | `1,1` |
| 3 | `1,3,1` |
| 4 | `1,6,7,1` |
| 5 | `1,10,25,15,1` |

These are the Stirling classes and exhaust all `1,2,5,15,52` set partitions.
Every additional merge loses at least one width power; no diagonal class is
discarded before its exponent is assigned.  Forced `W/W^T` identifications are
peeled first so a leading transpose branch cannot be misclassified as an
accidental diagonal.

The local innovation census exhausts forward and reverse degrees through four.
Forward partial-matching counts are `1,1,2,4,10`; reverse pairing counts are
`1,0,1,0,3`.  Wick--Stein elimination leaves no Gaussian, empirical covariance,
response operator, multivariate atom, or pseudoinverse.  The raw three-state
transition contains

```text
gamma04_next: 83 terms
a41_next:     20 terms
a43_next:      1 term
```

and only one-dimensional `M_nu` atoms.

## 6. Exact two-state reduction and cost

The third response state satisfies

\[
a43_\ell=d(1+a43_{\ell-1}),\qquad a43_0=0.
\]

Since `tau_ell=1+d tau_(ell-1)`, induction gives

\[
a43_\ell=\tau_\ell-1,
\qquad l43=1+a43_{\ell-1}=\tau_{\ell-1}=l1.
\]

The public dynamic state is therefore exactly

\[
(\gamma04_\ell,a41_\ell),\qquad(\gamma04_0,a41_0)=(0,0),
\]

with `64` and `17` transition terms.  This is the smallest state found; no
minimality claim is made.

All inputs are cached backbone nodes at adjacent layers.  Consequently the
head is one bottom-up post-`R3` sweep of exactly `H` nearest-neighbour cells.
One chosen layer costs `O(ell)` after the `O(H)` backbone.  Emitting heads for
all layers still costs one `O(H)` sweep, not `O(H^2)`; storing all outputs costs
`O(H)`.

## 7. Independent atom comparisons

The exact hostile runner reports:

| comparison | `gamma04` | `a41` | `a43` |
|---|---:|---:|---:|
| Route H-v2 vs A, raw | 0 | 0 | 0 |
| Route H-v2 vs S, raw | 0 | 0 | 0 |
| Route A vs S, raw | 0 | 0 | 0 |

After `l43=l1`, all three pairwise comparisons again have zero discrepancies
on the `64/17` public map.

An independent response-aware population compiler was then expanded at every
layer:

| depth | audited layers | total discrepancies |
|---:|---:|---:|
| 2 | 1,2 | 0 |
| 3 | 1,2,3 | 0 |
| 4 | 1,2,3,4 | 0 |

It compared `Gamma02,Gamma04,Gamma11,Gamma13,Gamma22` atom by atom.  Expanded
`Gamma04` term counts ranged from 203 at `(H=2,ell=1)` to 8,005 at
`(H=4,ell=4)`.  The two-state projection also agrees with the unreduced head at
every layer for `H=1,2,3,4`.

## 8. Exact controls and finite-width checks

Two independently implemented finite-width jet oracles agree on 30 cases with
maximum scaled error `1.3765e-15` against tolerance `5e-11`.  A separate raw
multivariate parameter-Taylor oracle agrees seedwise with the ordinary-series
feature-flow implementation for generic quartic activation at
`(H,n)=(1,1),(1,2),(2,1),(2,2),(3,1)`.

At total depth `H=2`, exact linear controls are

| layer | `Gamma04` | `Q''` | `Q^(4)` |
|---:|---:|---:|---:|
| 1 | 17 | 6 | 96 |
| 2 | 53 | 18 | 528 |

The constant activation gives zero for every propagated feature derivative.
For the nonhomogeneous unit-Gram affine control `phi(x)=(3+4x)/5`, exact values
include

| layer | `Gamma04` | `Q''` | `Q^(4)` |
|---:|---:|---:|---:|
| 1 | `1581824/390625` | `33792/15625` | `172045824/9765625` |
| 2 | `103905536/9765625` | `2221344/390625` | `3705931776/48828125` |

This affine test retains a constant term and therefore exercises response
branches invisible to homogeneous linear control.

## 9. Smooth nonpolynomial regression

Two independently preregistered `H=2` normalized-sine panels pass: Route A used
8,000 networks and obtained layer-two z-scores `0.715` for `Gamma04` and
`-1.140` for `Q^(4)`; Route S used 2,550 networks and obtained `z=-1.851` for
`Gamma04`.

The hostile `H=3` panel was more stringent:

1. The original widths `64,128,256`, 1,024 networks per cell, gave all four
   `|z|<1.97`, but remains labelled **inconclusive** because a quadratic fit to
   three points is saturated.
2. Before observing any width-512 value, the extension contract froze 1,024
   networks at `n=512`, exact seeds, and an operational form of the unchanged
   curvature rule.  The runner regenerated all 3,072 old networks and matched
   the old raw values with zero scaled error.
3. The four-width extension passed.  Its four affine z-scores were
   `0.207,0.493,-0.222,-0.114`; no primary fit had both statistically resolved
   and materially intercept-shifting curvature.  The maximum exact identity
   residual over all 4,096 networks was `6.01e-14`, no value was nonfinite, all
   standard-error gates passed, and no confirmatory replication was triggered.

The width-512 runner twice completed its calculation before a NumPy-boolean
JSON serialization bug stopped the report write.  Both reruns reproduced the
same frozen raw SHA-256
`2d2329246d15f1884458c39cae2897e06776fd3aad24d3875c21468175797ad0`.
A serialization-only wrapper was frozen before any raw value was inspected.
This incident and both wrapper hashes are retained in
`H3_CURVATURE_EXTENSION_FREEZE.json`.

## 10. Theorem and regularity boundary

The finite-width fourth-jet identities require a `C^4` flow/activation in a
neighbourhood of initialization and integrability of the displayed finite-width
observables.  The contracted `Gamma04` head uses only `phi,...,phi^(4)`.

A convenient sufficient annealed boundary when attaching the head to the full
audited `F^(5)` backbone is:

1. `H` is fixed before `n -> infinity`;
2. `phi` is `C^infinity`, with every derivative of polynomial growth; and
3. the associated finite tensor program converges in every finite `L^p`.

A weaker tailored bridge may instead prove convergence in probability (or
almost surely) and, for some `epsilon>0`,

\[
\sup_n\mathbb E\left|n^{-1}\langle X_r^\ell,X_s^\ell\rangle\right|^{1+\epsilon}<\infty
\]

for `(r,s)=(1,1),(0,2),(2,2),(1,3),(0,4)`, plus analogous UI for `A_H,B_H`
used in MSE time.  Under either checked bridge, expectation convergence follows
and the promoted normal form is the annealed limit.  No claim here is uniform
for `H=H(n)`, valid on a positive training interval, or all-orders.

## 11. Architecture boundary

The audited architecture is:

1. one reusable 29-state feature-ascent backbone;
2. output readout `A_H,B_H,C_H`;
3. kernel/Stieltjes and loss/time arithmetic heads;
4. hidden-activation `Q/R` heads using the two-state `Gamma04` sweep.

The universal objects are the parameter-flow jets and the 29 contracted
backbone states.  `gamma04,a41` and the final `Q/R` arithmetic are
observable-specific.  A preactivation RMS observable can reuse the parameter
jets, but its contracted scalar head has **not** been derived or audited.  It
must remain open; deleting activation factors from the hidden-activation head
is not a derivation.

## 12. `F^(7)` roadmap only

An independent Prüfer-sequence enumeration and a separate center-canonicalized
growth program both return 23 unlabeled free-tree shapes on eight vertices.
There is a clean abstract induction relating raw `D^k f` contraction shapes to
free trees on `k+1` vertices.  This is strong combinatorial evidence for 23 raw
shape families at order seven.

It is not yet an explicit rank-labelled 23-family tensor identity with
coefficients, a width/equality/transpose audit, or a scalar recurrence.  The
following therefore remain roadmap hypotheses only:

- grade-triangular embedding of the full order-five graph;
- additional `F4/R4` and `F5/R5` sweeps;
- a terminal `phi^(7)` ceiling;
- the promoted statement “raw `D^7f` has exactly 23 audited families”;
- fixed-dimensional `M`-only closure;
- factored `O(H)` evaluation.

## 13. Claim-level ledger

- **Exact finite width:** universal observable chain rule; Gram Leibniz rule;
  fourth feature/preactivation Bell identities; ten rank-one branches;
  readout equivariance; RMS differentiation.
- **Exact deterministic coefficient algebra:** label-one MSE time composition
  after the annealed coefficient limit and parity identities are established.
- **Formal Gaussian normal form:** the raw `83/20/1` three-state head after
  leading-width Wick--Stein contraction.
- **Algebraically audited normal form:** three-route raw comparison, exact
  two-state reduction, pairwise reduced comparison, H2/H3/H4 all-layer
  response-aware comparison, partition/width/transpose closure, and exact
  controls.
- **Empirical:** two passing `H=2` normalized-sine panels and the separately
  frozen passing four-width `H=3` extension; the original three-width panel
  remains inconclusive.
- **Theorem level:** conditional fixed-`H` annealed limit under the explicit
  convergence and UI hypotheses above.

Run the hostile audit with

```bash
python -m studies.mean_field_peeling.generic_first_stieltjes.depth_order5_scalar.multi_observable.audit.run_hostile_checks
```

Its final decision must be `promote_gamma04_head` with every promotion gate
true.
