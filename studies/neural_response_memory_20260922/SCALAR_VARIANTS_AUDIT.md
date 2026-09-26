# Scalar variants: scoped runner and result audit

2026-09-25. Collaborative internal check by kernel_scalar_design. This is not
an isolated promotion review. The reviewer previously implemented the potential
family; this assignment independently recomputed endpoint scores from the
frozen permitted results, without using the author's score files.

## Scope and conclusion

Inputs were the complete `SCALAR_VARIANTS_PROTOCOL.md`, complete current
`run_scalar_variants.py`, and all 23 `result.json` files immediately within
`data/generated/neural_response_memory_20260922/scalar_variants01/`. No engine,
imported fit implementation, score file, checkpoint, interpolant, history,
other study, or new training run was consulted for this audit. Small arithmetic
recomputations of the saved results were performed. Only this report was added.

The saved width-16 primary results support selecting `basis_r12`. It is the
only genuinely reduced primary candidate that satisfies both internal-output
and decoder gates. Its refinement is stable. The full-rank control reproduces
dense outputs within the required tolerance. The unchanged width-32 branch
**does not meet the original primary-panel gates**, for either readout. This
limitation must remain explicit even though pooled eight-angle RMS errors are
smaller. The analysis code was corrected during this audit to preserve the
primary-panel gates; its current slices and thresholds were inspected.

## Endpoint scores recomputed independently

Scores below use only the three original passive outputs at 30, 60, 90 degrees,
compared with the same-width fitted dense `result.json`. RMS is the square root
of the mean of three squared differences; training inputs are excluded.

| Primary candidate | State count | Internal passive RMS | Internal maximum | Outcome |
|---|---:|---:|---:|---|
| Frozen tail K3 | 92 | 0.16006049 | 0.25594421 | Accuracy failure |
| Frozen tail K5 | — | — | — | Boundary cap reached during preparation |
| Tangent tail K3 | 94 | 0.12109417 | 0.16189011 | Accuracy failure |
| Tangent tail K5 | — | — | — | Boundary cap reached during preparation |
| Basis rank4 | 104 | 0.13169075 | 0.22055952 | Accuracy failure |
| Basis rank8 | 272 | 0.06763356 | 0.07645419 | Intermediate RMS; does not pass |
| Basis rank12 | 504 | 0.03207686 | 0.04748929 | Pass |
| Basis rank16 | 800 | 6.89e-9 | 1.13e-8 | Full-rank implementation control |
| Potential gradient degree1 | 2 | 0.17218658 | 0.21922871 | Accuracy failure |
| Potential gradient degree2 | 2 | 0.34008585 | 0.45402948 | Did not fit by time40 |
| Potential curvature degree2 | 6 | 0.12007535 | 0.17947214 | Accuracy failure |
| Potential curvature degree3 | 6 | 0.14247977 | 0.22955683 | Accuracy failure |

The degree-two gradient potential's numbers are **terminal-time versus fitted
dense** discrepancies, not discrepancies between two fitted models. Its
training RMS is 0.30814706. The runner correctly leaves `internal_pass` false
when `reached_target` is false, but summaries must retain this distinction.

For `basis_r12`, decoded training RMS is 0.04184688, decoded primary passive
RMS is 0.02207464, and decoded maximum error is 0.03035332. These satisfy all
decoder gates. Rank4's seemingly good decoded passive RMS, 0.02727221, cannot
qualify it: decoded training RMS is 0.11715010. Rank8's decoded primary RMS is
0.05291426, also above its gate. None of the polynomial-potential decoders
qualifies. Thus selecting rank12 follows the frozen decoder-preferred rule
without needing the additional-angle or width32 answers.

## Width32 primary-panel nonpass and repaired pooling issue

The original three-angle errors in `basis_r12_n32_extended/result.json` are:

| Readout | Errors at 30,60,90 degrees | Primary RMS | Primary maximum |
|---|---|---:|---:|
| Internal | -0.00092973, +0.12170048, +0.01078454 | 0.07054119 | 0.12170048 |
| Decoded network | -0.01186379, +0.09870976, +0.00349291 | 0.05743566 | 0.09870976 |

Decoded training RMS is 0.03495459. Both readouts miss the primary RMS<=0.05
gate, and the internal readout additionally misses maximum error<=0.10.
These RMS values lie in the protocol's intermediate region rather than its
RMS>=0.10 accuracy-failure category. State precisely that the width32 check
does not pass; it supplies no positive width-generalization result.

Pooling all eight passive angles yields RMS 0.04361290 internally and
0.03555485 after decoding. The five additional angles have RMS 0.00759606
and 0.00658198 respectively. The pooled decoded score would misleadingly
satisfy both passive thresholds. The initially inspected `analyze()` applied
its gate to this pooled score. During the audit the author corrected it:
current lines223–236 compute primary scores from `error[:3]` and
`decoded[2:5]-dense_fit[2:5]`, and gate those quantities. This repair changes
analysis only; the saved endpoint results need no rerun.

Action: publish primary, additional, and pooled scores with explicit labels.
The current concise console fields still show pooled `passive_rms` beside a
primary-based pass flag. Use the explicit primary columns in the report, and
keep any earlier pooled-gate score file marked superseded rather than treating
its `decoder_pass` as current.

## Numerical and provenance checks

Maximum changes in all saved fitted outputs under the prescribed refinement:

| Refined object | Maximum output change |
|---|---:|
| Dense reference | 1.79e-9 |
| Selected rank12 basis | 3.95e-9 |
| Best potential: curvature degree2 | 7.64e-10 |
| Best completed tail: tangent K3 | 3.68e-6 |

All are below0.002. The selected basis decoder changes by at most4.06e-9.
Rank16 versus dense has maximum fitted-output discrepancy1.13e-8, below1e-5.
These checks validate the saved endpoint comparisons; no trajectory-wide
refinement or full-rank discrepancy was recomputed in this scope.

The protocol hash is identical in every result and matches the current file:
`a5d9373bc922e9a745db6188cd472a579b674c310a02320914cc71dc8299e219`.
All recorded engine and imported-fit source hashes are stable across the
23 results. Recorded runner hashes split between `214c3cff...` and
`e17573f1...`; every basis run uses the latter. The complete earlier runner
snapshot was outside this assignment, so the historical edit itself was not
independently diffed. This is consistent with the author's stated decoder
dispatch fix before basis runs, not an independent verification of that diff.
The inspected post-audit analysis repair has runner hash
`e01bfb25ba2d59dd62e670d5021ba51cdbbfeb393d23e14f81cbab1b39be75cd`.

## Normalization, information flow, and unverified inputs

The runner uses unit-norm circle inputs, exactly two active labels, and passes
the passive input array separately. It supplies only initialized parameters,
inputs and labels to candidate construction, initialization and fitting.
Dense trajectory access occurs in analysis, after fitting; no dense answer
is passed into a candidate. The decoder is removed from the model before
fitting and is used only for terminal decoding. The runner's physical decoder
readout is three tanh hidden layers followed by `c @ h / len(c)`, with no
additional input or width normalization. RMS and decoded-training scoring
have the correct sample counts.

The selected rank12 model's original outputs change by at most3.21e-9 when
the passive panel expands from three to eight inputs; its saved basis metadata
and active projection diagnostics remain identical. This supports the absence
of passive feedback for that comparison. It does not prove the engines never
use passive inputs in basis selection: that requires the separate engine
audits, which were deliberately outside this review. Canonical mobilities,
exact response product rules, and algebra-check PASS evidence likewise cannot
be certified from this wrapper and endpoint JSON alone.

The width16 dense result stores only the three primary passive outputs.
Therefore the width16 additional-panel dense answers, matched-time endpoint
scores, complete common-time curves, and4096-angle circle scores cannot be
independently reproduced from the assigned JSON inputs. The runner's analysis
obtains these answers from an interpolant; its fit-success and
no-extrapolation checks were inspected, but those interpolants were not read.
The author's separate analysis should supply those metrics without attributing
their numerical verification to this audit.

The five additional angles are not five independent input directions for this
bias-free odd network:210 and270 are antipodes of primary30 and90, while330
is the antipode of additional150. This does not violate the fixed protocol,
but limits how broadly that panel can be interpreted.

## Resource accounting and compression claims

All preparation-plus-solver durations recorded in the23 results sum to
55.85900131 seconds. The largest preparation is19.28987621 seconds and the
largest solver duration is7.95432669 seconds. Both K5 preparations stop at
50001 discovered boundary patterns, recording the first exceeded50000 cap;
neither has a fitted result. Report these as resource-limited cells, not
accuracy failures or successful higher-cutoff tests.

The runner's resource accounting has limits: durations are wall-clock values,
not measured process CPU time; import, artifact serialization and analysis
costs are omitted. `check_budget()` examines completed records, has no atomic
reservation across workers, and checks the global elapsed deadline only before
a cell. It therefore does not by itself enforce the three-worker ceiling or
a hard campaign deadline during a running cell. Single-thread numerical
environment variables are set before NumPy import. No recorded phase duration
approaches its cap, but strict CPU/concurrency/elapsed-budget certification
requires the supervisor's execution record. The imported fit function and
its120-second, state-size and nonfinite guards were not in this audit's input
scope. Future reuse should track reservations and actual process/deadline
measurements centrally; this does not call for new scientific runs here.

Finally, rank12 uses504 moving scalars on the primary panel, compared with560
dense parameters at width16; the extended panel increases it to684. Its fixed
coefficient tables alone occupy44192/44272 bytes, exceeding the4480 bytes of
560 float64 dense parameters, before decoder and runtime-object storage.
At width32 the extended state remains684 versus2144 dense parameters, but
the primary accuracy gate is missed. The evidence supports a limited moving-
state comparison and a width16 accuracy witness, not a demonstrated total-
memory advantage or width-independent accuracy guarantee.
