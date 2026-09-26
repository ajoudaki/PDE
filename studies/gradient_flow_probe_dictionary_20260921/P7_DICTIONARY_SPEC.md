# Frozen p7 dictionary specification

This list is fixed before any p7 trajectory or task score is measured. It
implements the complete formal middle-weight expansion through time power
eight derived in P7_DERIVATION.md, including its lower label-degree feedback.
It is a sufficient list of generators, not a minimal Gaussian-span theorem.
All fields depend only on initialization and the two fixed normalized axes.
Formal y1/y2 coefficient extraction does not use a training task's labels.

Coefficient slot j at degree d means [y1^(d-j) y2^j]. Retain the existing
new_dictionary_p45.raw_features(initial,5) lower and upper columns bitwise,
including their original order and scales. The following append operations
are mandatory; do not rescale, prune or select columns using performance.

1. The p6 list has the 14 existing lower columns and 28 upper columns.
   Append to the 24 p5 upper columns: 720 times the degree-five M coefficients
   (axis,j)=(1,1),(1,2),(2,3),(2,4), in that order.
2. For p7, append to the 14 lower columns: 720 times T6_1 slots0..5,
   followed by 720 times T6_2 slots1..6, at degree six.
3. Append to the 28 p6 upper columns: 5040 times tau P_1 slot1,
   then 5040 times tau P_2 slot4, both at degree five.
4. Append 5040 times all eight degree-seven K7_1 slots0..7,
   followed by all eight K7_2 slots0..7.

The p7 result is (K1,K2)=(26,46), 72 total vectors and 1196 middle
coefficients. The total trainable count at n2048 is 3n+1196=7340.
The old45-vector model has 6494 trainable coefficients, so the nearest
available vector-count comparison is not an exact parameter match.

M and tau P are time-six and time-seven factor coefficients respectively,
despite being quintic in the symbolic labels. Their scales therefore use
6! and 7!. T6 and K7 use the same time-derivative scale convention. The
constant matrices and all actions use the actual initial W2 and its actual
transpose. No fresh transpose or empirical population contractions.

Use the Gaussian formulas in P7_GAUSSIAN_CONTRACTIONS.md and the frozen
p7_gaussian_check.population_contractions API. Its default 256-node rule
supplies UK,hT,VV,beta and inherited pairings in ordinary polynomial
coefficient convention. The 192/256 maximum agreement gate is <=1e-9;
the earlier failed128/256 check remains recorded. Quadrature agreement is
a consistency check, not a certified error bound. The builder enforces the
proved beta parity exactly: average the two equivalent diagonal entries,
average the two equivalent off-diagonal entries, and set forbidden slots
to zero. Other moments retain their quadrature values. This projection
uses analytic symmetry only; no task-dependent fitting.

Normalize each raw population with its existing ridge-Cholesky convention,
using eta7=1/(1024*8^2). Preserve both raw prefixes, but recompute each full
p7 ridge basis: normalized prefixes need not match the p5 ridge basis.
Project the original dense middle into those bases using
M0=B2.T@(W2(0)@B1)/n. Use full middle replacement B2 M B1.T/n, without
a retained dense background. Retain the original finite random readout
and train the read-in, middle and readout using the unchanged canonical
physical mobilities and the same adaptive-Heun gradient-flow integrator.

The exact finite Taylor oracle independently checks the complete candidate
under exact initial-Gram fixtures with empirical pairings; the population
moment test separately checks Gaussian substitutions. The implementation
check compares direct polynomial evaluation and the retained raw columns.
GPU preflight checks all 22 archived initializations, raw prefixes, M0,
dimensions, finite fields and ridge conditioning before training. The
producer configurations freeze the executed source/document hashes.

The prior p6=p5 assumption is not adopted: the sufficient nested list
retains four additional feedback factors at p6. Formal collection ranks
do not by themselves establish strict noncontainment against the complete
actual Gaussian p5 span. No standalone p6 training or minimality claim.
