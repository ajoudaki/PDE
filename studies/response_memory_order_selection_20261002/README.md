# Predicting persistent representation selection from data order

Main investigation selected after the 2026-10-02 significance correction.
Scientific inputs are this study, the current paper and its included material,
maintained docs/code, and targeted primary literature. No other study's
unpromoted results or code are inputs. Root read the complete paper and startup
sources; the scoped author independently screened this question from them.

The consequential question is whether paired feature/credit history can predict
which useful representation survives training when example counts are unchanged.
The target is a persistent, useful decision about data order, beyond what a
cheap ordinary learner, local response model, or colored-noise explanation
already supplies. Observing an order effect is not new; approximation of another
trajectory by itself is not a new consequence. See RESEARCH_SCREEN.md.

The first thrust must establish actual feature competition and a substantial
order effect that survives a common continuation. A nonlinear odd signal and
a dominant linear shortcut respect the bias-free tanh model. Exact train/test
data, prefix, order contrast, horizon, matched exposures, metrics, numerical
checks, ordinary competitors, thresholds and resource cap must be recorded
before outcomes. Begin with a meaningful long block contrast, not an arbitrarily
small one-epoch perturbation whose effect is expected to wash out.

Only a consequential distinction earns response-memory forecasting and causal
history ablations. The response-memory representation of discrete SGD uses
all-sample forward histories and a full-data residual clock. The current
manuscript's smooth-flow theorems do not automatically cover it. Efficiency
cannot be claimed if retained histories cost more than the dense state.

Ownership: stochastic_history_screen writes protocol, producer and results;
root owns this README and research decisions. GPU0 only for the first gate,
at most20 cumulative GPU-process minutes and30 wall minutes. No new packages,
shared code/book/manuscript edits, or Git writes. Products stay in
data/generated/response_memory_order_selection_20261002/.

## Current decision — this ordering witness stops

The first prefix failed its predeclared competition gate: output used the
shortcut without useful invariant prediction. See
[RESULTS_FIRST_GATE.md](RESULTS_FIRST_GATE.md). An explicitly exploratory
[amendment](AMENDMENT_EXTENDED_ACQUISITION.md) then tested acquisition over one
fixed longer horizon, with the original data, learning rate and source blocks.
The nonlinear task proved learnable; an exact fitting cutoff was narrowly missed.

[RESULTS_EXTENDED_ACQUISITION.md](RESULTS_EXTENDED_ACQUISITION.md) records the
substantive negative. Reversing source blocks initially changed shifted risk by
29.54% of the zero-predictor error, but identical continued training reduced the
signed difference to -0.111%. At the lowest training loss attained by both it
was likewise negligible. A smaller ordinary nonlinear learner prospectively
predicted negligible scale (its tiny sign was wrong). No closure forecasts,
extra seeds, further horizons, or proof campaign followed. This is a single
exploratory witness with implementation checks, not a freshly reproduced result
or a theorem rejecting data-order effects. Both GPUs are released.

The [plot producer](plot_order_contrast.py) shows why the initially impressive
effect is insufficient; its figure is under
data/generated/response_memory_order_selection_20261002/order_contrast_figure01/.
Next authorized action here is preservation/correction, not another parameter
search. Reopening requires an independently motivated persistent learning
mechanism and a concrete decision that ordinary alternatives do not explain.
The broader goal remains active and unmet. The distinct supporting alternative
is coordinated separately; its science is not an input here.
