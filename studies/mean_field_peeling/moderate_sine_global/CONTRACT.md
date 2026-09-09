# Exact moderate sine activation: strong global limit

2026-09-08. Authorized work: mathematical proof search and independent
adversarial checking. No training experiment or optimizer modification.

Fix the single activation

\[
v=(1-e^{-8})/2-4e^{-4},\qquad
D=\sqrt{1+4v/25},\qquad
\Phi(z)=\big[(1-4e^{-2}/5)z+(2/5)\sin(2z)\big]/D.
\]

Its coefficient 2/5, frequency 2 and normalization are fixed. They may
not be reduced as separation, width, or physical horizon changes.

Use the original model and all observable conventions in
../two_sample_activation_design/PROOF.md, Section 1: two fixed inputs
of squared norm d, binary labels, |rho| <= 1-delta with 0<delta<=1,
three hidden layers, independent Gaussian initialization including the
actual finite readout, the original raw metric, all blocks trained, true
physical GF, and simultaneous raw GD of step n^-2. The population state
must retain both orientations of the initialized Gaussian actions and
their actual adjoints, plus the learned Hilbert--Schmidt increments.

Target: one canonical autonomous global strong population loss flow,
uniqueness and continuation from reached states, jointly identified with
the full finite-width GF/GD sequence on each fixed [0,T], in the original
kernel, hidden path, velocity, second-moment and generated-action
topologies. Constants may depend on T and the fixed data. No probability
supremum over datasets, or uniform limit over the entire infinite time
half-line, is required.

Finite-width global existence, initialization geometry, a local-time
limit, a stopped theorem, conditional tail bounds, and existence for a
smaller nonlinear coefficient are distinct partial results. None resolves
this target. Do not replace Gaussian matrix reuse by fresh independent
actions or restart from newly independent Gaussian roots.

Existing mathematical sources are read-only. New work stays here or in
explicit temporary derivation files. Three independent routes examine
physical energy/continuation, sine-specific source response, and hostile
functional-analytic/causal counterexamples. A positive candidate must be
reconstructed adversarially before it is called proved. A missing
estimate must remain explicit; failure of an ambient bound is not a
counterexample to actual neural training.
