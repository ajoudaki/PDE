# Predeclared refinement branch receipts

The first two primary tolerances reached all loss levels for dense, P2 and
P3. P1's second run was still in progress when the now-free GPU0 was used
for the conditional dense refinement. This does not change scientific
configuration, subset, seed, endpoints or the frozen error gates.

At train MSE .001, dense's held-out prediction change from rtol2e-4 to5e-5
is .001230343742759484. P2's corresponding change is .001699034018769629;
its fine closure-dense RMS is .001943664206301043, giving gate .00019436642.
P3's change is .000276701179403527 and its fine closure-dense RMS is
.001328188762374915, giving gate .00013281888. Therefore dense, P2 and P3
all trigger the existing relative numerical-resolution gate. Each receives
the predeclared single rtol1.25e-5 refinement, at most600 seconds. Whether P1
triggers its allowed refinement will be determined from its completed pair,
using the same all-endpoint gate. No additional digit/width/seed/order search.

Dense refinement starts in generated mnist_refined01/dense_level2 onGPU0
after the P3_level1 primary process exits. Other refinements use free GPUs
as primary runs finish. Saved runner arguments and frozen source hashes
remain the complete executed recipe.

The completed P1 pair also triggers the all-endpoint gate: at training MSE
.1 its own refinement RMS is .000624920227 versus the allowed10% of the
fine closure-dense RMS .00285429767, namely .000285429767. Its primary .001
endpoint passes, but the frozen rule covers every reached endpoint. Therefore
the single permitted P1 rtol1.25e-5 run is also executed, queued after P2's
refinement to keep both GPUs occupied without concurrent jobs on one GPU.
All four optional numerical refinements are now committed; no further
refinement or training branch remains afterward.
