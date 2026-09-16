# Closure order and learned circle geometry

New study opened 2026-09-14 for the user-authorized theory and numerical investigation of what angular functions emerge under the maintained N=1,3,5 closures, compared with the frozen initial tangent kernel. This is materially different from endpoint-discrimination screening. No prior study results, implementations, or histories are research inputs. Scientific inputs are established docs/code and artifacts generated here.

Root owns this README, the experimental contract, driver, plots and final synthesis. Fresh scoped collaborators contributed separate flat theory, closure-worker, baseline, analysis and verification files; generated products go only under data/generated/closure_circle_spectral_mechanism/. No shared book/code or Git-index changes were made by this study.

Initial question: does closure order impose an angular frequency scale, or instead an initialization-mark approximation scale whose angular consequences depend on training geometry and nonlinear adaptation? Start with two opposite-label points at varying angular distances; add three/four points and label amplitudes through a fixed bounded contract. N=0=NTK is a hypothesis to check, not a convention assumed here.

Completed the fixed first pass: 75/75 GPU trajectories, all mildly settled at physical times100–120; largest final training MSE1.31e-10. Scientific execution took633.4seconds within the1200-second cap. Postprocessing used approximately five minutes; no additional training was started. Generated products total249.1MiB, with2.22GiB free at closeout, within the600MiB and1.5GiB limits. No output cleanup was performed.

The readable synthesis is [INSIGHT.md](INSIGHT.md). The [five-page figure report](../../data/generated/closure_circle_spectral_mechanism/plots_final/spectral_mechanism_report.pdf) includes the radial comparison, spacing/frequency/overshoot, three/four-point shapes, one-parameter reconstructions and Fourier-kernel geometry. The precise measurements and control verdicts are in [analysis_final/summary.json](../../data/generated/closure_circle_spectral_mechanism/campaign_001/analysis_final/summary.json). All raw configurations, complete final states, observations, hashes and environments are retained in [campaign_001](../../data/generated/closure_circle_spectral_mechanism/campaign_001/).

The central internally checked result is that N controls an initialized-mark dictionary, not an angular Fourier cutoff. Every order can generate higher odd harmonics, while antipodal oddness excludes even harmonics. The exact symmetric, matched-ridge model predicts N1/N2 active equivalence; the implemented comparison differs by at most0.0105% relative circle RMS. A normalized tanh–sine curve reconstructs the unit-amplitude,45-degree-midpoint pair sweep within0.34–2.62%. Closing opposite-label spacing increases angular bandwidth substantially at every tested nonlinear order and creates much less off-support overshoot than the frozen NTK.

Feature adaptation is resolved against each closure's own frozen kernel: at pair separation30degrees the relative endpoint discrepancy is53–55%, versus at most0.12% quadrature refinement error and0.000031% time-step error. Both hidden layers move, and their pairwise geometry changes substantially. No universal monotone N1→N3→N5 bandwidth law was demonstrated. Four points15degrees apart provide an exploratory increasing-frequency witness, without matched refinement coverage. The three-point40degree N1 and N5 quadrature controls fail the preset2% circle tolerance (4.18% and2.57%); these order comparisons remain provisional. All other available refinement controls pass. No actual finite-width neural network was trained here, and no improvement in off-support accuracy or general average superiority of higher N is asserted.

[THEORY.md](THEORY.md), [NTK_THEORY.md](NTK_THEORY.md), and [SYNTHESIS_AUDIT.md](SYNTHESIS_AUDIT.md) contain the derivations and qualifications. The audit is a same-study internal consistency check, not an isolated promotion review. Nothing is promoted to established docs/code. The inference scope is the recorded sparse-circle laws and the exact algebraic claims under their stated hypotheses.

Validation: CPU/GPU field, RHS, Heun, tangent-metric and restart checks agree with the maintained NumPy implementation; a separate verifier reconstructed all75 final1440-point outputs directly with maintained NumPy, with maximum absolute discrepancy5.33e-15 ([verification](../../data/generated/closure_circle_spectral_mechanism/verification_final/verification.json)). Analytic NTK quadrature and weighted gradient flow checks and14 synthetic analyzer checks also pass. Implementation correctness is distinct from the two failed quadrature-resolution controls above.

Reproduction uses the existing environment `/home/amir/miniconda3/bin/python -B` with one BLAS/OpenMP thread and CUDA for `RUN.py`. `RUN.py --prepare --output <fresh-study-generated-campaign>` freezes the75 configurations and producer inputs. Then `RUN.py --wave pairs --output <campaign>` followed by `--wave multi` executes the bounded waves; the second wave must follow the worker correctness gates in [PLAN.md](PLAN.md). `ANALYZE.py --campaign <campaign> --output <fresh-analysis-directory>` and `VERIFY.py --campaign <campaign> --out <fresh-verification-directory>` reproduce the measurements and replay checks without training. `PLOTS.py --campaign <campaign> --analysis <analysis-directory> --output <fresh-plot-directory>` produces the report. Existing output directories are retained.

Contributors: root (contract, scheduling, plots, synthesis); scoped spectral_order_theory (exact theory and internal synthesis audit); spectral_closure_worker (faithful GPU worker and NumPy verification); spectral_ntk_baseline (population NTK and analysis, with a prompt-scoped synthetic-check contributor). Research input boundaries were maintained; coordinator metadata is not scientific evidence. The scientific campaign is closed; unresolved questions are the dynamics selecting the fitted tanh–sine parameter and an a priori mark-resolution criterion for higher-order endpoint accuracy.

## User-requested actual-network validation

The next user request explicitly asked to fit actual network outputs to the same curve family and test whether the closure approximations approach them. This continues the same function-selection investigation; [NET_PLAN.md](NET_PLAN.md) fixes a separate campaign without reopening or modifying the original75-run experiment. The distinction is explicit: N is closure order, while kappa is a fitted shape parameter. The earlier first-pass statements about having no network reference are now supplemented by this comparison.

Completed20 actual dense-network trajectories: widths1024 and4096, three Gaussian seeds each, separations15,30,90degrees, plus same-seed half-step and float64 controls. All settled at T100, largest training MSE6.88e-12. The two-GPU training wave finished in97.6seconds. The fixed8192 branch was statistically triggered but was not started: the recorded reserve for its checkpoint would violate the predeclared minimum free disk. No data were deleted and no budget extended. Final campaign products occupy259.8MiB.

The tanh–sine family fits the4096-neuron ensemble outputs with kappa6.372,4.206,2.151 and heldout relative RMS errors1.80%,1.63%,0.68% at15,30,90degrees respectively. Every individual widest-width seed passes the5% template criterion. Raw closure errors versus the4096 ensemble, in N1/N3/N5 order, are3.986/2.923/2.908% at15degrees;1.892/1.632/1.672% at30degrees; and1.701/0.814/0.661% at90degrees. N1→N3 improves the observed fit throughout this sample; N3→N5 is mixed. Numerical control and finite-width qualifications prevent promoting this into monotone hierarchy convergence. The1024→4096 ensemble shifts are0.141%,0.0646%,0.299% in the same geometry order; seed spread is retained separately.

[NET_COMPARISON.md](NET_COMPARISON.md) gives the readable conclusion and qualification of the small order differences. [The four-page network figure report](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/network_comparison_report.pdf) includes raw curves and residuals, radial plots, template fits and per-seed error comparisons. [Final measurements](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/analysis_final/summary.json) retain source/input hashes, all seed-level fits, normalized-shape comparisons, closure-refinement effects and the actual branch decision. [The raw campaign](../../data/generated/closure_circle_spectral_mechanism/network_comparison_001/) retains every observation and eight complete final networks according to the frozen storage contract; the remaining full states are reproducible from the explicit seeds and producer rather than retained as checkpoints.

CPU/GPU equations, RHS, Heun and autograd metric checks pass with maximum error7.08e-16. Half-step and float64 trajectory differences are at most0.000167% relative circle RMS. [Independent saved-state verification](../../data/generated/closure_circle_spectral_mechanism/network_verification_main/verification.json) checks all20 configurations/observations and replays all eight retained networks on1440 angles using independent NumPy equations: maximum discrepancy2.51e-7. All saved arrays, retained parameters, source/output/initialization hashes and stopping checks pass. [NET_VERIFY.md](NET_VERIFY.md) states the exact scope, including which full states are not retained. Ten synthetic analyzer checks pass; their final evidence is in the raw campaign's `analyzer_selftest_final.json`.

Reproduce with the same Python/environment listed above: `NET_RUN.py --prepare --output <fresh-campaign>` then `NET_RUN.py --wave main --output <campaign>` on the GPUs. The wider branch requires the explicit supervisor gate in NET_PLAN; `NET_BRANCH.py --campaign <campaign>` records the tested gate and resource reserve. `NET_ANALYZE.py --campaign <campaign> --output <fresh-analysis>` reproduces analysis/figures, and `NET_VERIFY.py --campaign <campaign> --output <fresh-verification>` performs the independent CPU replay. Source code stays flat in this study; exact producer bytes are also archived in generated products. Root owns the plan/worker/supervisor/README; scoped network_circle_analysis owns analysis/report and finite_network_metric_check owns independent derivation/audit/verification. This campaign is closed. No infinite-width or infinite-order convergence claim, new off-support teacher accuracy claim, or promotion is made.

## Interactive radial comparison

The user-requested viewer presents this study's 15 main data laws using the supplied screenshot as an interface reference only. It includes the 52 main closure trajectories, 18 individual network trajectories and six network means, and the analytic frozen population NTK for every law. The actual network is available only for the unit-amplitude, 45-degree-midpoint pairs separated by 15, 30 or 90 degrees; missing network experiments are identified in the interface. N=2 is available for the unit-amplitude pair sweep. No other study's scientific data were imported and no training was rerun.

[VIEWER_DATA.py](VIEWER_DATA.py) exports the saved arrays and analytic NTK modes; [RADIAL_VIEWER.html](RADIAL_VIEWER.html) is the literal interface source and [BUILD_VIEWER.py](BUILD_VIEWER.py) embeds the compressed data. Generated data, numerical export checks and the compiled viewer are in [radial_viewer_001](../../data/generated/closure_circle_spectral_mechanism/radial_viewer_001/). The conversation displays an identical compiled fragment in its authorized visualization directory. These presentation sources remain flat in this study.

The radial and angle views support model visibility, network width/seed selection, settled endpoints, physical time and matched training MSE. Settled view uses recorded mildly settled outputs and the exact infinite-time NTK limit. Physical time uses the common saved horizon of the visible models. Playback linearly interpolates output and training-prediction arrays between saved times spaced by ten time units; it does not resolve the early dynamics within those intervals. Matched loss is solved using the squared residuals of those interpolated predictions, with the network-mean loss defined as the average per-seed MSE. The NTK is evaluated analytically at each selected time, including its potentially much longer matched-loss times.

The display uses 240 angular samples. Export verification finds a worst circle reconstruction discrepancy of 0.1824% relative RMS against the dense endpoint arrays and an NTK endpoint discrepancy of 3.18e-12. The radial offset keeps radii positive and the scale remains fixed during playback; changing experiment or visible models recomputes that scale. Training labels are shown only at their supplied angles, with no invented target elsewhere. The existing three-point 40-degree quadrature qualification remains visible in that experiment.

[VIEWER_BROWSER_CHECK.cjs](VIEWER_BROWSER_CHECK.cjs) validates the actual rendered interface with browser networking disabled and the pinned D3 dependency served locally. The recorded browser check covers 130 scenarios across all 15 cases, all three alignment modes, available network widths/seeds, model toggles, playback and hover. Matched losses, positive radii and fixed playback scales pass. Both chart views fit 320- and 736-pixel widths in light and dark themes, with no runtime, console, overflow or clipped-label errors. The same-study export/renderer consistency check is presentation validation, not a new scientific or promotion review.

## Actual networks for the three- and four-point cases

The user explicitly requested the missing actual-network references for all six existing three/four-point experiments and their inclusion in the current viewer. This continues the same investigation. [MULTI_NET_PLAN.md](MULTI_NET_PLAN.md) freezes a separate 48-trajectory campaign: six geometries, two widths, three seeds, and twelve same-seed numerical controls. Every network ends at T120, with dense common-T100 predictions retained for comparisons at the same physical time. A settling flag remains a diagnostic, not an equilibrium assertion. Old campaigns remain frozen.

Completed all 48 dense-network trajectories on both RTX3090 GPUs in 212.77 scientific wall seconds; every run met the mild settling diagnostic at T120, with maximum final training MSE 8.35e-10. The fixed design uses widths1024/4096 and seeds1729/2718/3141, plus one4096 half-step and one1024 float64 control per case. All complete final weights, source/configuration archives and observation arrays are retained in [network_comparison_multi_001](../../data/generated/closure_circle_spectral_mechanism/network_comparison_multi_001/), occupying about1.62GiB before analysis. No old data were removed or training horizons extended.

At common T100, the measured N1/N3/N5 relative circle RMS errors against the width4096 three-seed mean are: triple20,23.68/10.95/7.18%; triple40,33.29/3.97/4.69%; triple60,13.67/4.81/7.26%; quad15,46.46/32.12/21.79%; quad30,7.46/3.89/2.08%; and quad45,9.04/3.02/3.14%. N3 is closer than N1 in all six cases; N5 improves three and has larger error in three. Both tested widths give the same direction of each order comparison. These are descriptive finite-network results: only quad30 passes the complete numerical/seed/closure-control improvement gates for both transitions. Other cases lack matched closure controls or have the previously reported triple40 quadrature failures. Missing controls are not zero uncertainty.

[MULTI_NET_COMPARISON.md](MULTI_NET_COMPARISON.md) presents the measurements and qualifications. [The analysis](../../data/generated/closure_circle_spectral_mechanism/network_comparison_multi_001/analysis_final/summary.json) retains both common-T100 and recorded-endpoint comparisons, all seed errors, width drift, numerical effects and paired order gains. The network numerical-control discrepancy is at most0.00802% relative RMS, while the1024-to4096 mean differences range0.37–1.09%. The largest network T100-to120 circle change is0.000237%. These stability measurements do not establish an infinite-width or infinite-order limit, and there is no off-training teacher target.

Both GPU equation/update checks pass. [Independent NumPy verification](../../data/generated/closure_circle_spectral_mechanism/network_comparison_multi_001/verification_final/verification.json) checks all48 configurations, source/input/output hashes, initializations, losses, settling flags and full retained parameter arrays, and replays every endpoint on144 exact dense-grid angles plus its training inputs. Maximum circle replay discrepancy is3.81e-7; all48 pass. This verifies the saved networks, without independently replaying intermediate weights that were not retained.

The updated viewer includes actual networks in all six three/four-point cases, while preserving every original case/model/time. It now contains52 closure trajectories,54 individual network trajectories and18 means across15 laws. The default is four points15degrees apart, with the actual network visible. Each comparator has a full-circle error readout against the selected width/seed; endpoint errors use original1440-angle arrays, while playback errors use displayed interpolations. Recorded endpoints show their actual times; physical-time and matched-loss modes remain available. [MULTI_VIEWER_DATA.py](MULTI_VIEWER_DATA.py) and [BUILD_VIEWER.py](BUILD_VIEWER.py) produce [radial_viewer_multi_001](../../data/generated/closure_circle_spectral_mechanism/radial_viewer_multi_001/). Its124 displayed models retain240-angle panels, with at most0.2503% endpoint reconstruction error and zero training-loss roundtrip discrepancy. The compiled fragment is790,639bytes.

[MULTI_VIEWER_BROWSER_CHECK.cjs](MULTI_VIEWER_BROWSER_CHECK.cjs) passes180 recorded scenarios plus endpoint-error checks across every available network width/seed, all15 cases, both plot views, playback, matched losses and visibility changes. Both320/736-pixel layouts and light/dark themes pass without runtime, console, overflow or clipped-label errors. Browser inspection uses no network access; the pinned chart library is supplied locally. The final display fragment is identical to the generated compiled viewer.

Reproduction sources are [MULTI_NET_RUN.py](MULTI_NET_RUN.py), [MULTI_NET_ANALYZE.py](MULTI_NET_ANALYZE.py), [MULTI_NET_VERIFY.py](MULTI_NET_VERIFY.py), and the frozen plan. Recorded commands, environment and exact producer bytes are retained with the campaign; prepare/check-batch/wave are separate stages and the completed campaign refuses relaunch/overwrite. A future training reproduction needs a fresh declared output namespace. Analysis and verification accept fresh campaign-child output directories. This campaign is closed, with no additional training authorized or required for the present request.

Root owns this README, interface and browser checks; scoped multi_network_runtime owns the new plan/trainer and raw campaign, multi_network_analysis owns analysis and independent saved-state verification, and multi_viewer_export owns the compact data export. All new handwritten files remain flat here and products use fresh study-generated namespaces. No promotion is proposed.

## Narrow mathematical promotion preparation, 2026-09-16

Following [independent selection](PROMOTION_SELECTION_20260916.md), assembler
/root/author_c prepared the [complete insertion](PROMOTION_INSERTION_20260916.md)
after (H3.N2) in docs/global_nonlinear.md. It proves all-state antipodal
oddness, fixed-order high-frequency representability, conditional
sign-symmetric matched-ridge order-one/order-two equivalence, and the exact
three-block closure kernel with its own frozen-readout comparator. Local
notation maps order p=N, with P_1,P_2 particles, n width and d=2 input dimension.
Representability remains distinct from states reached by prescribed training.

Every empirical result, campaign, fitted shape law, universal accuracy
ordering, endpoint theorem and new convergence scope is excluded. The optional
stationary Gaussian pair example is deferred. No API or guide change is proposed.

The [neutral assignment](PROMOTION_ASSIGNMENT_20260916.md) and
[frozen manifest](PROMOTION_MANIFEST_20260916.json) define the two fresh
scientific reviews. The [assembly record](PROMOTION_ASSEMBLY_RECORD_20260916.md)
records provenance, reproduction and author validation. The generated
target-chapter edition is under
data/generated/closure_circle_spectral_mechanism/promotion_20260916/edition/.
Frozen hashes, placement, equation labels, math delimiters, references and
exact preservation of unchanged chapter bytes pass author/editorial checks;
these are not independent scientific acceptance.

Assembler /root/author_c owns this entry and assembly inputs; coordinator
/root owns review dispatch and subsequent integration. Frozen scientific
inputs remain unchanged during review. Next are the two complete isolated
reviews, combined-edition validation and fresh integration review, then user
approval of the concrete reviewed addition. No live docs/code or Git-index
changes were made.

Both fresh complete scientific reviews now accept the exact frozen insertion,
with no required corrections: [C1](PROMOTION_REVIEW_C1_20260916.md) and
[C2](PROMOTION_REVIEW_C2_20260916.md). The coordinator read both full original
reports and checked their identities and coverage. The insertion and frozen
dependencies are unchanged. Standalone combined-edition validation and a
separate fresh integration review remain distinct; this result is not yet
established and no live book edit or user promotion approval has occurred.

### Consolidation proposal ready for user approval

The complete integrated05 edition passed the required fresh integration review,
with no required corrections. Its source manifest is
`83e0e4b3c1238880e7a8d87fdb251233a41b491462c8fa3e14a0fa3443c6ff3e`.
The separately recorded scientific pairs remain accepted. The integration-only
optional-Torch test-discovery adapter preserves every scientific test body.
[Exact proposal and destinations](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
include the accepted reviews, fresh validation and exclusions. This link is
promotion coordination, not a research dependency. Nothing has yet been
incorporated into established docs/code; concrete user approval is the next gate.

### Approved consolidation incorporated — 2026-09-16

The exact explanatory insertion is incorporated after H3.N2 in docs/global_nonlinear.md: dictionary versus angular-frequency meaning, all-state oddness, conditional matched-rule p=1/p=2 equality and closure tangent-kernel identities.

Tanh–sine fits, fitted kappa values, a general kappa(p) law, training-reachability claims and universal improvement with order remain unpromoted.

User approval: “yes I approve”, for the exact integrated05 proposal.
[Approval, mapping, hashes and commit receipt](../closure_endpoint_discrimination/PROMOTION_INTEGRATION_RECORD.json)
record the completed integration; [accepted reviews and reproduction](../closure_endpoint_discrimination/PROMOTION_PROPOSAL.md)
remain linked with every original adverse report. This is administrative
promotion coordination. Historical study sources/evidence are preserved.
