# Hostile audit of the proposed second-order reduction

**Provenance:** isolated adversarial proof-complexity referee; no repository
access and no communication with other agents.

**Date:** 2026-08-24  
**Verdict:** reject the proposed global theorem as a meaningful reduction.
Its cross-mesh Cauchy clause already contains essentially the missing
continuous-time convergence proof, at a stronger augmented-state level.

## Why the proposed theorem was circular

Let

\[
 \mathcal A_n^\pi=(Z_n^\pi,DZ_n^\pi,D^2Z_n^\pi)
\]

be the state and first two typed source variations on mesh \(\pi\). The
rejected clause required \(\mathcal A_n^\pi\) to be uniformly Cauchy across
all refining meshes. Combined with the already rigorous fixed-grid Tensor
Program limit, moment/UI bounds, and a representation of the raw observables,
this immediately supplies the standard triangle argument

\[
 K_n-K=(K_n-K_n^\pi)+(K_n^\pi-K^\pi)+(K^\pi-K).
\]

Thus it assumes the two difficult uniform terms rather than deriving them.
A \(\sup_n\) Cauchy version is even stronger than the desired width-first
limit. Conversely, convergence of the finite raw-observable list need not
imply coupled \(L^2\) Cauchy convergence of the whole augmented state because
unobserved coordinates, permutations, or rotations may vary while the
observables agree.

A fixed \(p>4\) envelope does not repair the circularity. Ordinary
interpolation yields only

\[
 \|Q[d(Z)-d(\widetilde Z)]\|_2
 \lesssim\|Z-\widetilde Z\|_2^{(p-4)/(p-2)},
\]

whose exponent is below one. That modulus is not Osgood and cannot propagate
a vanishing mesh defect from zero.

## Retained algebraic subclaim

A degree-four representation of a **fixed, explicitly enumerated** raw list
may still be useful, but only if its probes and coefficients are fixed
independently of width, mesh, and target trajectory; its response variables
are actual differentiated dynamics; and its remainder is uniform in time
and mesh in \(L^{1+\epsilon}\). Without those restrictions, the observable
can be hidden inside an auxiliary coordinate or coefficient. Finite network
depth does not bound causal response depth automatically.

## Smallest noncircular replacement

The new target is a **local typed correlated-multiplier/gluing theorem**.
For two admissible same-source D3 configurations, augment their ordinary
state discrepancy by the finite two-copy tangent susceptibilities representing
every surviving normalized trace/Hilbert--Schmidt gluing. One synchronized
Euler increment of size \(a\) must obey

\[
 \mathcal E^+
 \le(1+Ca)\mathcal E
   +Ca\,\omega_{\rm loc}(|\pi|+|\pi'|)
   +a r_n,                                            \tag{1}
\]

where \(\omega_{\rm loc}\) is linear or Osgood, \(r_n\to0\), and all
constants are independent of width and mesh. In particular, (1) must control

\[
 Q_2\{d(Z_2)-d(\widetilde Z_2)\}
\]

and the \(N\)-type two-colour gluing. The factor \(a\) multiplying \(r_n\)
is essential; a width defect emitted once per step without it accumulates as
\(r_n/|\pi|\).

Only after proving (1) may deterministic discrete Grönwall/Bihari derive
cross-mesh Cauchy convergence.

## Concrete leaf program

The referee identified the following genuinely lower-level leaves:

1. exact typed differentiation of one finite-width Euler update;
2. Gaussian probe/polarization identities representing every required
   trace and Hilbert--Schmidt gluing;
3. integration by parts or exact conditional Gaussian decomposition showing
   that derivatives of correlated gates generate precisely the typed first
   and second responses;
4. a derivative-count audit: any unavoidable third response falsifies the
   proposed finite closure;
5. mesh-independent moment and time-increment bounds proved before any mesh
   convergence assertion;
6. simplex/tree summation with total weight \(O(e^{CT})\), rather than a
   constant exponential in the number of Euler steps;
7. concentration/truncation giving the step-summable \(a r_n\); and
8. elimination of susceptibilities into current-time action/trace-class
   readouts so that no response history remains in the final IDE.

The decisive falsifiers are a merely Hölder exponent below one, an
unbounded response hierarchy, a remainder lacking the step-size factor, or
a susceptibility that cannot be eliminated from the final one-time state.

This local theorem remains substantial, but unlike the rejected global
Cauchy statement it does not assume the conclusion it is meant to prove.
