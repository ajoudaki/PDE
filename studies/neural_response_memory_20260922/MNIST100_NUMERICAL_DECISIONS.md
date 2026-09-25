# MNIST100 numerical branch decision

All eight primary trajectories reached every predeclared training-loss
milestone through .001. Root directly recomputed paired validation RMS and
two-resolution prediction changes from the saved arrays, before final analysis.
Every model passes the strict numerical gate at all five milestones, so none
of the optional rtol7.8125e-7 runs is triggered. Finest executed rtol is3.125e-6.

At training MSE .001, the dense predictor's refinement change is
0.000048104382268823874. Closure refinement changes for P1/P2/P3 are
0.000003931163438179834, 0.000002118397080680962,
0.0000016588603525218262. Closure-dense RMS scores are
0.003247560410434991, 0.001084434749988775, 0.001199224207446615.
All are well above the individual refinement changes under the frozen10%
gate; .005 absolute gates also pass. Observed changes are diagnostics, not
rigorous numerical bounds.

The predeclared dense and P3 repetitions execute at rtol3.125e-6 in fresh
mnist100_reproduction01 directories, with GPU assignments swapped relative
to those primary trajectories. They retain every scientific/numerical
configuration, including data, initialization and stopping. P3 repetition
started as the primary GPU0 queue finished; the dense repetition starts
after P1 completed onGPU1. These are reproducibility checks, not extra
scientific seeds. No scientific refinement branch remains.
