# Current research state: finite causal PDEs for dense ResNets

- **Maintained through:** 20 August 2026
- **Scope:** fully connected, fully trained residual networks in the Euclidean
  \(\mu\)P scaling used by this repository
- **Status:** useful finite-cutoff PDE demonstrated; arbitrary-accuracy and
  dense-limit theorems open

This is the authoritative entry point for the three residual-network studies
in this directory. It reconciles their exact mathematics, executed evidence,
incomplete programs, and superseded interpretations. Phase-local reports
remain authoritative for their own frozen protocols and numerical values.

The word “ResNet” here does **not** mean convolutional or arbitrary production
ResNets. It refers to the fully connected residual laboratory defined below.

## Executive verdict

The program has accomplished three different things, and they should not be
collapsed into one claim:

1. [`dense_response`](dense_response/) exposes the exact chronological memory
   structure of a finite dense network and shows numerically that very low
   response order can be extremely accurate. Every tested surrogate there
   still retains the microscopic dense matrices, so it is mechanism evidence,
   not a PDE construction.
2. [`operator_pde`](operator_pde/) gives the only literal width-coordinate-free
   PDE in this three-study chain. Its finite-cutoff equations are explicit and
   autonomous, their projected-gradient geometry is exact internally, and the
   degree-one \(P=5\) cutoff tracks the tested dense networks closely.
   It is the constructive and empirical centerpiece.
3. [`pde_convergence`](pde_convergence/) asks whether that useful low-order PDE
   belongs to an arbitrary-accuracy hierarchy. It establishes exact parity
   equivariance and, assuming uniqueness, the symmetric-flow reduction; it
   also isolates the functional-analytic obstruction. Its last aggregate
   cutoff comparison is adverse rather than contracting. It is a genuine
   executed audit, not a convergence result.

Thus the present result is an **explicit, useful low-order candidate PDE with
exact internal geometry and substantial finite numerical support**. It has
not been proved to be the ordered dense-network limit, its cutoff hierarchy
has not been proved or empirically observed to converge, and no all-time
accuracy theorem exists.

## 1. The research contract

### 1.1 Canonical dense model

The canonical current experiments use

\[
H^0=BX,\qquad
H^{\ell+1}=H^\ell+\frac{\gamma}{L}\sigma(W_\ell H^\ell),
\qquad
f=\frac1n a^\top H^L,
\]

with all of \(B,W_\ell,a\) trained by Euclidean \(\mu\)P gradient flow and

\[
\eta_{W_\ell}=L,\qquad \eta_B=\eta_a=n.
\]

The main activation is \(\tanh\), with separate activation controls and
bounded sine stress tests. The intended limiting order is

\[
n\to\infty\quad\text{at each fixed }L,
\qquad\text{then}\qquad L\to\infty.
\]

Nothing in the current record proves a joint limit or an \(L\)-first limit.
The project-level target emphasizes the output curve and the entire
depth-indexed hidden-Gram field. Some protocols also treat loss as co-primary,
while tangent-kernel quantities are primarily diagnostics; the stronger
`dense_response` formulation also targets the tangent kernel.

[`dense_response/early_audit`](dense_response/early_audit/) used the different
input convention \(H^0=\tanh(BX)\), along with both iid- and smooth-depth
designs. It is a historical exploratory precursor. Its numerical values must
not be silently pooled with the canonical linear-input evidence in
[`dense_response/long_horizon`](dense_response/long_horizon/).

### 1.2 What would count as a finite causal PDE

For a compact training horizon \([0,T]\) and requested accuracy \(\varepsilon\),
the sought approximation must be:

- derived from the architecture, initialization, data, and declared static
  parameters rather than fitted to the already-computed target trajectory;
- autonomous and causal from its declared state;
- independent of the original width \(n\) and layer count \(L\);
- described by finitely many field types over a finite-dimensional source
  coordinate, although it may still be a continuum PDE in depth and state;
- free of width-sized matrices, an ever-growing response tree, the exact
  uncompressed two-training-time kernel/history, or future-trajectory access;
  finitely many autonomous history/age fields over declared finite-dimensional
  coordinates remain allowed; and
- internally restartable from the full declared PDE state.

“Finite” therefore does not mean a finite global scalar state or a particular
numerical grid. The operator PDE still has continuous depth and a conditional
law; its numerical resolutions \(N,M,R\) are not network width or residual
depth.

Three restart statements must also remain distinct:

1. **Internal PDE restart:** the full PDE state determines its own future.
2. **Serialized solver restart:** saving and restoring the discretized state
   reproduces an uninterrupted numerical run.
3. **Dense-state restart:** a physically reachable positive-time dense state
   can be mapped to the PDE state with controlled future error.

The first is structural, the second is an implementation check, and the third
is the scientifically strong bridge. Only the first two have been exercised;
the dense-state restart theorem is open.

### 1.3 Minimal compact-time umbrella conjecture

For each \(T<\infty\), \(\varepsilon>0\), and declared bounded parameter/data
class, there should exist an architecture-derived autonomous finite-source PDE
whose output and depth-Gram curves approximate the ordered
\(n\to\infty\), then \(L\to\infty\), dense dynamics uniformly on \([0,T]\)
to accuracy \(\varepsilon\). Its complexity may depend on
\(T,\varepsilon\), and the declared class, but not on \(n,L\), or a future
realized trajectory.

The currently executed **specific witness under audit** is the pure
complete-degree operator-Hermite Liouville family. `dense_response` separately
specifies an unimplemented response-enriched \(K/J/N\) family with a stronger
uniform all-time conjecture. The compact-time umbrella conjecture is logically
weaker than either witness: if the pure-Hermite family fails, a finite
response- or history-enriched PDE could still exist.

All-time uniform approximation and restart from positive-time dense states are
strictly stronger conjectures than the compact-time statement.

## 2. Claim ladder

| Level | Current status | What is actually known |
|---|---|---|
| Exact finite dense-network calculus | **Established** | Forward/adjoint, parameter-flow, chronological-response, tangent-kernel, and loss-dissipation identities hold in the declared finite systems |
| Explicit finite-cutoff operator PDE | **Constructed and executed** | The finite-\(P\) conditional Liouville PDE and its characteristic solver are explicit, width-coordinate-free, autonomous, and restartable |
| Internal finite-\(P\) PDE geometry | **Exact under regularity** | Shared forward/transpose pairing, projected Euclidean-gradient identity, PSD tangent blocks, and loss dissipation hold for sufficiently regular candidate solutions |
| General finite-\(P\) well-posedness | **Open** | The repository does not give an existence/uniqueness theory for the full coupled PDE class |
| Accuracy on tested finite networks | **Strong empirical support** | The degree-one \(P=5\) PDE closely tracks finite ensembles on the canonical benchmark and a fixed transfer panel |
| \(P\to\infty\) hierarchy convergence | **Open; last observed rung adverse** | Parity reduction is exact under odd activation, symmetric initialization, and uniqueness, and is verified in the finite solver; aggregate state and observable Cauchy ratios did not contract through the degree-seven comparison |
| Identification with the ordered dense limit | **Open** | Width-first convergence, trained iid-depth homogenization/Onsager identification, and the join to the PDE have not been proved |
| Arbitrary accuracy on compact time intervals | **Open** | Two conditional routes exist: compactness/consistency plus uniqueness, or an infinite solution and vanishing defect plus cutoff-uniform forced stability; neither route is complete |
| Uniform all-time validity | **Open and separate** | Numerical plateaus through finite horizons do not establish it |

## 3. How the three substudies fit together

| Substudy | Scientific role | Durable contribution | Main limitation |
|---|---|---|---|
| [`dense_response`](dense_response/) | Finite-matrix mechanism precursor | Exact response/memory anatomy and strong audited low-order response accuracy | Every executed surrogate retains all dense \(W_\ell\); zero compiled Liouville-PDE runs |
| [`operator_pde`](operator_pde/) | Construction and empirical centerpiece | Explicit finite-\(P\) PDE, exact internal geometry, direct dense comparisons, transfer and activation controls | No dense-limit identification, cutoff convergence, general well-posedness, or all-time theorem |
| [`pde_convergence`](pde_convergence/) | Corrective hierarchy/proof audit | Exact parity equivariance and conditional symmetric-flow reduction, real bounded cutoff experiments, and precise compactness/stability reductions and obstructions | No arbitrary-accuracy result; final aggregate trend is noncontracting and narrow |

These are successive parts of one evidence chain, not three independent
replications of the same theorem.

## 4. Exact theory that survives the audits

### 4.1 Finite dense network and response hierarchy

For fixed \(n,L\), the dense forward and adjoint equations, scaled parameter
gradient flow, tangent-kernel identity, and loss dissipation are exact.

The chronological \(q/r\) response hierarchy is also an exact hierarchy; at
full finite-depth order it reproduces the exact derivatives. The low-order
truncations \(K=0,1,2,3\) are accurate **empirically**, not by an all-order
closure theorem.

The dense-memory calculation shows why a one-time Gram field or current row
law is not generically an exact autonomous state: the exact elimination of
trained dense matrices produces two-training-time covariance and causal
response data. A continuation witness uses two dense states that agree on the
proposed current reduced observables but have different microscopic matrices;
it defeats that simplest exact closure. Iid layer matrices also cannot be
silently replaced by a smooth depth path \(W(s)\).

Along a fixed trajectory, the exact-source ordered response tail obeys a
factorial Dyson bound of the form

\[
R_K(\Lambda)\le e^\Lambda
\frac{\Lambda^{K+1}}{(K+1)!}
\]

under its integrated operator-envelope hypothesis. This bound is
noncommutative/nonnormal safe. It does **not** control the additional coupled
backward-source error, nonlinear grammar/cavity terms, the width/depth limits,
or all time. The words in this construction still carry the dense matrices.

### 4.2 Finite-cutoff operator PDE

[`operator_pde/core/theory/operator_galerkin_pde.md`](operator_pde/core/theory/operator_galerkin_pde.md)
specifies a Hermite/isonormal conditional Liouville candidate. At fixed
cutoff \(P\), it contains no network-width coordinate, original layer count,
or \(n\times n\) matrix. The same projected random operator defines the
forward and transpose directions.

For solutions with the required regularity, the following are exact **inside
the candidate PDE**:

- the shared \(W_P/W_P^*\) pairing;
- the projected Euclidean-gradient/output identity
  \(\dot f=-\Theta_P e\);
- positive-semidefinite tangent-kernel blocks;
- loss dissipation; and
- autonomy and restart from the full characteristic state.

These results establish the geometry of the candidate. They do not prove that
its Onsager/conditional terms equal those of the trained dense limit. Nor does
an internally correct finite-\(P\) equation supply a general existence,
uniqueness, or \(P\to\infty\) theorem.

### 4.3 Parity equivariance and the correct cutoff ladder

For odd activation, symmetric Gaussian initialization, and uniqueness of the
operator flow, even source-Hermite shells are identically inert. The
equivariance is exact, and the reduction is verified to roundoff in the finite
characteristic solver. Arbitrary or asymmetric training targets do not break
this source parity.

With four source-label coordinates, the complete spaces of sizes
\(P=5,15,35,70,126\) contain respectively \(4,4,24,24,80\) active odd modes.
Consequently, the symmetrically initialized physical trajectories satisfy

\[
Y_5=Y_{15},\qquad Y_{35}=Y_{70},
\]

and the first physical ladder is \(P=5\to35\to126\). The solver reproduces
the first equality at roughly \(10^{-17}\); the second follows analytically
but was not separately solver-validated. This supersedes every
interpretation of an old \(P=5\to15\) discrepancy as a hierarchy step; that
difference was cubature symmetry leakage.

### 4.4 What energy and Hilbert-space structure do—and do not—give

Let \(I\) be the unit-covariance isonormal injection. It is an isometry, and
the shared transpose \(T_W=I^*\) is its bounded Hilbert adjoint. The full
frozen component is \(\sigma_w I\), while a trained row also includes its
response part. A Malliavin derivative is therefore not needed merely to define
or bound \(T_W\), or for consistency along one fixed compact trajectory.

The operators \(I\) and \(T_W\) are not compact: an orthonormal source
sequence maps to an orthonormal target sequence. Finite-cutoff energy
dissipation yields
cutoff-independent finite-time state bounds and time equicontinuity for
sufficiently regular states, but it does not force collective Hermite-tail
compactness.

The natural adjoint nonlinearity also contains multiplication by an unbounded
Gaussian readout coordinate. It is therefore not locally Lipschitz on plain
\(L^2\) balls. A convenient cutoff-independent unweighted-\(L^2\)
well-posedness/stability proof route is unavailable.

### 4.5 Conditional convergence reductions

Two theorem routes remain valid:

1. prove collective relative compactness of the reachable cutoff states,
   consistency on compact sets, and uniqueness of the limiting flow; or
2. construct an infinite solution, prove vanishing fixed-trajectory
   projection/source defect, and obtain a cutoff-uniform forced-stability
   modulus.

A source-mode-coercive weighted reachable-regularity estimate would be one
sufficient compactness mechanism. Generic energy, Gaussian Sobolev, or Orlicz
bounds are not automatically enough. These are rigorous reductions, not
completed convergence theorems.

## 5. Numerical studies that actually ran

### 5.1 Dense chronological response

[`dense_response/long_horizon/REPORT.md`](dense_response/long_horizon/REPORT.md)
is the canonical numerical record. It contains 16 primary finite-network
trajectories through \(T=32\), each paired with the exact finite system and
response orders \(K=0,1,2,3\), plus refinement and algebraic controls. All 16
exact curves and all tested response orders passed the study's operational
finite-horizon plateau rule. The recorded-grid errors were:

| Response order | Output median / max | All-depth Gram median / max |
|---:|---:|---:|
| \(K=0\) | \(8.510\times10^{-3}\) / \(1.579\times10^{-2}\) | \(2.501\times10^{-2}\) / \(5.189\times10^{-2}\) |
| \(K=1\) | \(2.378\times10^{-4}\) / \(1.397\times10^{-3}\) | \(1.875\times10^{-3}\) / \(3.616\times10^{-3}\) |
| \(K=2\) | \(1.418\times10^{-5}\) / \(5.711\times10^{-5}\) | \(1.183\times10^{-4}\) / \(5.517\times10^{-4}\) |
| \(K=3\) | \(9.768\times10^{-7}\) / \(6.250\times10^{-6}\) | \(6.083\times10^{-6}\) / \(5.925\times10^{-5}\) |

The exact feature-motion median was \(0.6299\), with range
\([0.02756,0.7869]\). At tolerance \(10^{-5}\), 2 cases needed \(K=2\), 11
needed \(K=3\), and 3 remained unresolved; do not claim uniform
\(10^{-5}\) accuracy at \(K=3\).

The main inference is **chronological response compressibility on these finite
trajectories**. It is not evidence from a compiled PDE because every surrogate
retained \(W_\ell\).

The reconstructed tangent kernel stored for a projected state is a PSD proxy,
but it is not automatically the kernel driving that projected output flow:
the actual rate contains a cross-kernel. Positive proxy eigenvalues therefore
do not by themselves prove that the finite-matrix surrogate is a coercive
gradient flow.

### 5.2 Direct operator-PDE benchmark

[`operator_pde/core/REPORT.md`](operator_pde/core/REPORT.md) directly
integrated the \(P=5,N=16,M=256,R=128\) candidate. Against the canonical
\(n=256,L=32\), 128-network ensemble through \(t=8\), the maximal
Gram-increment gap was

\[
7.243\times10^{-3},
\]

or \(1.143\%\) of the PDE feature motion \(0.6338\). This is close, but the
finite-reference discrepancy is statistically **resolved**; it is not hidden
inside seed noise. The current evidence does not separate finite-width,
finite-depth, cutoff, and cubature contributions to that residual gap.

The available finite-grid width/depth Cauchy diagnostics are unresolved and
too noisy to identify the ordered limit. Paired-weight hidden/adjoint
variances scale approximately as \(1/L\) over the tested grid, which is
necessary evidence for depth homogenization, not a propagation-of-chaos or
Onsager theorem.

The PDE alone was continued from \(t=8\) to \(t=32\) and stayed near a
plateau. The dense comparison ended at \(t=8\). This is a real autonomous
finite-horizon continuation, not a dense-validated \(T=32\) result and not an
all-time theorem.

### 5.3 Fixed transfer panel

[`operator_pde/generalization/FINAL_REPORT.md`](operator_pde/generalization/FINAL_REPORT.md)
ran a preregistered panel of 14 fixed synthetic cases without retuning the
degree-one PDE. Every **observed** normalized curve error was below \(5\%\):

- Gram increment: median \(1.71\%\), maximum \(4.14\%\);
- output: maximum \(1.83\%\); and
- loss: maximum \(1.97\%\).

All cases exhibited nonlazy motion. Nevertheless, the frozen simultaneous
95% critical increment was \(5.94\%\), six cases failed or left numerical
resolution gates unresolved, and four failed the requirement to pass both
plateau windows. The formal verdict is therefore **boundary/unresolved**, not
“uniform transfer proved.”
Only two cases directly test the narrow tanh conjecture; the rest are scoped
extension evidence, not population-level dataset generalization.

### 5.4 Activation and clock controls

[`operator_pde/activation_controls/ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md`](operator_pde/activation_controls/ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md)
shows that the successful nonlinear PDE is not merely the exact identity
dynamics or a scalar change of training clock:

- the nonlinear-versus-identity dense Gram separation was \(36.38\%\), with
  95% lower bound \(35.27\%\), while the matched nonlinear PDE error was about
  \(1.09\%\);
- equal-loss-progress Gram paths remained \(27.14\%\) apart; but
- a gain-matched fixed linear control was only \(3.46\%\) from the nonlinear
  dense Gram curve and stayed inside the \(5\%\) margin.

The correct verdict is **identity-only falsification**. Exact identity
dynamics and a mere clock explanation are rejected; “all linear explanations
are false” is not established. Gram and output reject identity, but the
deliberately stronger loss-only \(S>2E\) rule did not pass; an all-observable
rejection claim would therefore be too strong.

The independent scalar sine stress in
[`pde_convergence/04_scalar_stress`](pde_convergence/04_scalar_stress/) further
shows that activation nonlinearity can matter while source-label complexity
stays low. Fixed-gain and RMS-matched linear controls missed the PDE Gram curve
by \(17.70\%\) and \(8.68\%\), while degree-one and degree-11/13 PDE curves
differed by only \(0.339\%\) and \(0.247\%\). The high-order PDE/dense joint
5% rule was still boundary because the loss error was \(5.54\%\).

### 5.5 The convergence campaign, phase by phase

The endpoint is
[`pde_convergence/05_tail_and_compactness/COMPACTNESS_REPORT.md`](pde_convergence/05_tail_and_compactness/COMPACTNESS_REPORT.md).

| Phase | What ran | Durable reading |
|---|---|---|
| [`01_proof_audit`](pde_convergence/01_proof_audit/) | Only 2 of 12 initial Phase-A jobs completed, both at \(P=5\); no \(P=15\)/\(P=35\) job and no simultaneous decision | A substantial seven-gate implementation/protocol framework, but no scientific gate passed. Its 128 tests are software/provenance tests, not 128 scientific experiments |
| [`02_lean_salvage`](pde_convergence/02_lean_salvage/) | Four fresh bounded diagnostics—ordered scaling, depth homogenization, same-state attack, and generator/shadow—plus reanalysis of earlier late-time and \(P=5\) cubature trajectories | Real but narrow favorable mechanism evidence. The ad hoc runner is absent; archived arrays/report remain. Its old \(5\to15\to35\) hierarchy ratios are invalidated by parity |
| [`03_bridgeability`](pde_convergence/03_bridgeability/) | Parity-clean bounded odd-shell diagnostics with retained runner and arrays | Parity equivariance and the conditional symmetric-flow reduction are durable. Lifted outgoing residuals contracted strongly, but aggregate feedback and observable ratios grew; the lifted residual is only the velocity of a newly opened shell at a low-order state, not the trained high-shell tail |
| [`04_scalar_stress`](pde_convergence/04_scalar_stress/) | Completed sine and two tanh high-degree stress runs | Strong activation effects need not mean high source-Hermite dependence. The two tanh top-tail ratios, \(0.958\) and \(1.913\), did not replicate a turnover; observable effects were tiny |
| [`05_tail_and_compactness`](pde_convergence/05_tail_and_compactness/) | Common-reference degree-seven audit and one final coupled compactness run | Removed separately trained-reference and parity confounds, established the analytic obstruction, and found no aggregate Cauchy contraction |

In the final run, at \(t=0.25\),

\[
\frac{E^{\mathrm{state}}_{5\to7}}{E^{\mathrm{state}}_{3\to5}}
=1.32193,
\qquad
\frac{E^{\mathrm{obs}}_{5\to7}}{E^{\mathrm{obs}}_{3\to5}}
=1.63581.
\]

At \(t=0.125\), the ratios were \(1.32306\) and \(1.63414\). The realized
shadow-gain ratio was \(0.99862\), so this one forcing direction did not reveal
a large cutoff-dependent amplification change. It is not a worst-case or
cutoff-uniform stability bound.

The final result is adverse **at the last observed rung**, not a divergence
theorem or falsification. It used one seed, \(N=1\), \(R=512\), and
\(t\le0.25\). The absolute observable gaps remained tiny—about
\(2.19\times10^{-5}\) and \(3.58\times10^{-5}\) of the project scale—so
practical low-order utility and absence of observed hierarchy contraction can
both be true.

## 6. Implemented, proposed, and never run

The following must not be cited as completed experiments:

- The `dense_response` \(K/J/N\) Liouville compiler is a formal specification.
  No executable compiler or serialized concrete compilation artifact emitted
  complete tag/history tables, Gaussian kernel, drift DAG, or runnable
  width-independent PDE. There were **zero** compiled Liouville-PDE runs in
  that study.
- Phase 01 of `pde_convergence` implemented an ambitious framework for ordered
  scaling, trained-depth/Onsager, same-state continuation, generator defects,
  worst-direction amplification, and late-time tails. Gates 1–6 produced no
  full scientific archive; only 2 of the 12 initial Phase-A jobs ran, both at
  \(P=5\). Later lean phases are related bounded studies, not completion of
  the frozen certification campaign.
- The conditional convergence arguments have named hypotheses but no proof of
  collective reachable-state compactness, infinite-flow uniqueness, or
  cutoff-uniform forced stability.
- No cofinally resolved nested \(P\) hierarchy with matched \(M/R\)
  refinements, full preregistered ordered-target grid at its intended scales
  and uncertainty, degree-nine follow-up, second-seed final compactness run,
  resolution refinement of that final ledger, or worst-direction gain
  calculation was completed.
- The stored core \(P=35,R=128\) complete-cubic calculation is an
  underresolved directional stress, not a clean third hierarchy level. The
  proposed post-outcome \(P=35,R=256\) refinement was deliberately not run.

An absent raw campaign in this compact checkout does **not** imply that its
experiment never ran; evidence custody is recorded separately below.

## 7. Supersession and interpretation rules

Future summaries should apply all of the following:

1. Never use the phase-02 ratios \(2.54\)–\(26.53\) against Hermite
   convergence. Their \(P=5\to15\) denominator measured cubature parity
   leakage from an inert shell; \(P=35\to70\) is likewise inert for the
   symmetric physical solution.
2. Never call the phase-03 lifted outgoing residual contraction a contraction
   of the trained high-shell tail.
3. The earlier suggestion that an adjoint/Malliavin-tail theorem was the unique
   make-or-break gap is superseded. Riesz boundedness handles the shared
   transpose; Malliavin or other source regularity remains only one possible
   route to the collective compactness actually needed.
4. A projected-energy fraction near one is not a convergence certificate;
   many small modes can have a collective effect.
5. Small per-mode coefficients do not prove a small aggregate tail.
6. Accurate \(P=5\) trajectories do not prove \(P\to\infty\) convergence.
7. Exact finite-\(P\) projected-gradient geometry does not identify the PDE
   with the dense-network limit.
8. A PSD tangent proxy reconstructed from a projected state is not necessarily
   the cross-kernel driving that projected output flow.
9. Fourteen observed errors below 5% do not turn an underpowered simultaneous
   equivalence test into a formal pass or a generalization theorem.
10. A plateau through \(T=8\) or \(T=32\) is not an all-time bound.
11. Passing 8, 12, or 128 implementation tests is not the same as passing a
   scientific limit or equivalence gate.
12. Failure to find a same-state continuation counterexample in one bounded
    search is not proof that the proposed state is sufficient.
13. Rejecting identity dynamics does not reject every gain-matched linear
    explanation.
14. If the pure static Hermite hierarchy fails, that defeats this witness,
    not the broader possibility of a response-enriched finite causal PDE.

## 8. What is genuinely worth remembering

The durable scientific content is:

1. **Exact causal anatomy:** trained dense residual dynamics generate a
   chronological response/memory structure with a necessary shared transpose;
   naive current-Gram closure is not exact in general.
2. **Strong low-response compression:** across 16 tested trajectories, errors
   fall sharply from \(K=0\) to \(K=3\). At \(K=3\), the maximum output and
   all-depth-Gram errors were \(6.250\times10^{-6}\) and
   \(5.925\times10^{-5}\); median feature motion was \(0.6299\), with range
   \([0.02756,0.7869]\).
3. **A literal candidate PDE is explicit and has been numerically integrated:**
   the operator-Hermite conditional Liouville system is autonomous and
   width-coordinate-free; its internal gradient/PSD/dissipation identities
   are exact for sufficiently regular solutions at fixed cutoff.
4. **The degree-one PDE is useful:** \(P=5\) closely tracks the tested
   canonical ensemble and remains descriptively accurate across a fixed
   14-case panel.
5. **The activation mechanism is real but nuanced:** exact identity and
   pure-clock explanations fail, while one gain-matched linear control remains
   close; a separate sine stress exposes stronger nonlinear separation.
6. **Parity reduction is exact under its hypotheses:** odd activation,
   symmetric initialization, and uniqueness make even source-Hermite shells
   inert; the finite solver verifies the first equality to roundoff, and the
   physical ladder is \(5\to35\to126\).
7. **The analytic obstruction is now precise:** energy and bounded transpose
   control do not yield compactness, and plain \(L^2\) local Lipschitzness
   fails because of the unbounded Gaussian boundary multiplier.
8. **The two central bridges remain open:** neither cutoff convergence nor
   identification with the ordered trained dense limit has been established.
   The final finite-level trend is adverse but far too narrow to falsify the
   hierarchy.

## 9. Highest-leverage remaining obligations

The most valuable next analytic result on the PDE side is a cutoff-uniform
source-coercive reachable-tail estimate such as

\[
\sup_{J\ge K}\sup_{t\le T}
\lVert(I-\Pi_K)Y_J(t)\rVert_{\mathcal X}\longrightarrow0,
\]

or an equivalent collective relative-compactness theorem, together with
uniqueness. The alternative route is a cutoff-uniform forced-stability modulus
plus vanishing fixed-trajectory projection defect.

Independently, the dense-network side still needs a fixed-\(L\) trained causal
width theorem followed by trained iid-depth homogenization/Onsager
identification. Only after both branches are established can the limiting PDE
be identified with the ordered dense ResNet dynamics.

If another numerical hierarchy study is undertaken, the clean design is a
common high reference with parity-correct active degrees, multiple cubature
scrambles and numerical refinements, collective weighted state tails, and
state/observable commutators under predeclared gates. Another isolated
low-degree curve match would add little to the present ledger.

## 10. Evidence custody and reproducibility

- `dense_response/long_horizon` retains its declared raw NPZ trajectories,
  processed tables, protocol, environment, and SHA-256 manifest.
- `pde_convergence` phases 03–05 retain the relevant raw arrays and manifests;
  phase 04 retains raw NPZ/JSON results. Phase 02 retains arrays and a report,
  but not its ad hoc runner.
- The original operator core was a 689 MB audited release. This compact
  checkout keeps its code, protocol, processed CSV/JSON evidence, figures, and
  audits, but not the original raw arrays or full-release manifest.
- The generalization and activation campaigns were also completed. Their
  compact releases retain code, protocols, processed evidence, stage seals,
  and raw-file hashes while omitting the raw NPZ collections; generalization
  alone omits 101 NPZ files (about 1.35 GB).
- [`operator_pde/rerun_2026-07-31`](operator_pde/rerun_2026-07-31/) retains a
  later five-file raw NPZ subset. It reproduces central scalar diagnostics but
  is a reproduction/smoke bundle, not new frozen scientific evidence or a
  repeat of the complete campaign.
- Test suites check algebra, implementation, protocol, and provenance. They do
  not certify the scientific approximation or limit claims. The frozen
  environments use newer numerical-library versions than some current local
  checks, so last-bit exact-array differences or a compatibility alias must not
  be presented as scientific discrepancies.

## 11. Authoritative reading order

1. This file for the cross-study claim and supersession ledger.
2. [`dense_response/long_horizon/REPORT.md`](dense_response/long_horizon/REPORT.md)
   for the canonical response experiment, and
   [`dense_response/long_horizon/theory/dense_euclidean_continuous_depth_pde_conjecture.md`](dense_response/long_horizon/theory/dense_euclidean_continuous_depth_pde_conjecture.md)
   for the exact/conjectural response split.
3. [`operator_pde/core/theory/operator_galerkin_pde.md`](operator_pde/core/theory/operator_galerkin_pde.md)
   for the candidate PDE, followed by
   [`operator_pde/core/REPORT.md`](operator_pde/core/REPORT.md),
   the [`core hostile audit`](operator_pde/core/audits/final_adversarial_pde_audit.md),
   the [`core statistical audit`](operator_pde/core/audits/statistical_audit/REPORT.md),
   [`operator_pde/generalization/FINAL_REPORT.md`](operator_pde/generalization/FINAL_REPORT.md),
   the [`activation-control report`](operator_pde/activation_controls/ACTIVATION_LINEARITY_SMOKING_GUN_REPORT.md),
   and
   [`operator_pde/activation_controls/RELEASE_PROVENANCE.md`](operator_pde/activation_controls/RELEASE_PROVENANCE.md)
   for numerical claims and evidence custody. Any old physical
   \(P=5\to15\) interpretation in an audit is superseded by the parity result.
4. [`pde_convergence/03_bridgeability/REPORT.md`](pde_convergence/03_bridgeability/REPORT.md)
   for parity and
   [`pde_convergence/05_tail_and_compactness/COMPACTNESS_REPORT.md`](pde_convergence/05_tail_and_compactness/COMPACTNESS_REPORT.md)
   for the current convergence endpoint.

The dated top-level monograph remains valuable as a historical integrated
baseline. Where its older cutoff interpretation or status language conflicts
with this file and the maintained phase reports above, use this ledger.
