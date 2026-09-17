# Author validation and evidence scope

2026-09-17. Root authored and then read both complete proof artifacts in a
separate checking pass. This is an internal author check, not an independent
review, promotion gate, numerical experiment or empirical convergence claim.

## Frozen proof versions checked

- extremal_hitting_times.md:
  `911f63476a526298605d638ee7992dffaa239b3d6bc70562fe22669a451b5ce0`
- two_input_anchor.md:
  `9cf5f7f38429af8a7c371c281aaf58ed913f58f02b1788388847d9855e765a1b`
- check_algebra.py:
  `37fbccc01f39c72a7aea2a0e65a2da633fe982c525f5c46a25adea1e3ef88e33`

Canonical versions, also recorded in manifest.sha256:

- docs/global_nonlinear.md:
  `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`
- docs/observable_p1.md:
  `0f9c0ab9d1bcd6acd844cfce52e00d94c063843fcf80d27e7ba2b7ea6ebdfbba`
- docs/NOTATION.md:
  `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`

Read the complete observable_p1.md; complete notation and docs guide; the
complete relevant state/dynamics/existence/energy blocks of C.4.7.9 and D.3.
No closure-to-network convergence theorem is invoked outside its scope.
Truncated combined tool output was repaired with smaller individual reads.

## Mathematical checks and actual outcomes

1. Recomputed the physical prediction gradients with block order (w,c,M),
   actual M transpose and unhalved probability-weighted loss. The readout
   initialization is zero and the only initial moving block is c. All factors
   two and the probability factors in the pair/triple formulas agree.

2. Checked the escape argument without assuming the target is reached. If it
   is, the small correlation bound excludes the target from the entire ball,
   so a first exit exists. Its available dissipation is bounded by 2b_R,
   rather than merely by one. Cauchy--Schwarz gives exactly R^2/(2b_R).
   If it is never reached, the lower bound holds with tau=infinity. The
   b_R=0 case is explicitly separate. No Euclidean law distance is substituted
   for the physical characteristic metric.

3. Reconstructed the angular derivatives through both hidden layers. The
   lower second derivative uses E|w|^2 and the bounded b1 envelope; the upper
   squared derivative uses ||Z'||infty||Z'||2. All these are controlled on a
   physical L2/Frobenius ball. No higher row moments or population L4 bounds
   are silently obtained from L2. The second-difference integral has mass
   delta^2, and its label correlation has the required factor 1/4.

4. Substituted both radius choices in the energy bound. Pair available energy
   is at most 2K1 R delta; triple available energy is at most K2 R delta^2/2.
   The thresholds are at most epsilon/2. Both minimum formulas in (8),(11)
   follow, including their coefficients. A lower bound for one family is not
   used to order its true time relative to another family.

5. Checked the initialized derivatives separately from long-time bounds.
   All Gaussian moments exist at initialization; the same uniform higher-
   derivative control is NOT asserted on general physical balls. Binomial
   finite differences have the sign (-1)^r and normalization 2^-r, so their
   loss-slope coefficient is 4^(1-r). Maximality is a Vandermonde moment
   statement, not a maximizer of actual hitting time or every feature-specific
   initial slope. Nonzero leading derivatives are stated where required.

6. Recomputed the exact initialized map from both D bands. The conditional
   reverse Gaussian is retained. Positivity at r=1, Gaussian-density
   analyticity on (-1,1), and its odd series imply a nonzero kappa near zero
   without assuming kappa'(0)>0. For the axis triple the three feature vectors
   are nonzero and pairwise unequal up to sign. Positive upper density plus
   tanh's first three odd coefficients proves the Gram rank. The resulting
   fixed-hidden readout is only a representability certificate.

7. Checked reflection symmetry on the actual canonical coordinates, including
   T2 D T1=D and the sign of c under the involution. Recomputed auxiliary-time
   growth bounds before invoking fitting. The q/F^2 inequality protects C0,
   gives a finite auxiliary fitting point, and the physical clock reaches it
   only at infinite physical time. The inverse-output clock yields the exact
   hitting-time integral and the small-loss coefficient 1/(4K_*). No limit in
   delta was interchanged with either loss-threshold limit.

8. Checked the direction of every potential implication. Hitting-time LOWER
   bounds force initial-potential LOWER bounds. A constant rescaling can make
   a potential arbitrarily larger, so no upper value follows automatically.
   A fixed-threshold essential singularity follows for any fixed strictly
   increasing h with h(0)=0; a uniform eventual exponential exponent for loss
   requires the separately stated power comparison. A slow tail cannot be
   repaired by increasing a finite initial prefactor. No claim that actual
   tail exponents tend to zero is made.

9. Tested degeneracies logically: exact contradictory collisions; compatible
   antipodal oddness; incompatible even label measures with stationary c=0;
   absent positive leading initialized derivative; possible infinite triple
   hitting time; arbitrarily small but fixed delta; and the order of all
   limits. The representable triple has distinct inputs for delta>0. The
   convergent pair family alone already proves an unbounded supremum among
   problems with finite hitting times at every fixed positive loss threshold.

No blocking error was found within these stated scopes. Global fitting for
the triple, matching delay order and terminal-rate degeneration remain open;
they were not treated as technical consequences of the lower-bound proof.

## Deterministic arithmetic check

Purpose: check signs and normalizations in the binomial stencil and the two
normalized-readout derivative identities against independent exact arithmetic.
Scope: orders 1 through 16, 54 rational parameter points. A single ordinary
Python invocation, expected below one second; no stochastic sampling, training,
or parameter search. Reproduction from repository root:

    python studies/closure_extremal_times_p1_20260917/check_algebra.py

Executed successfully with exit code zero. Output:

    PASS: balanced binomial moments and slope factors, orders 1--16;
    PASS: both normalized-readout derivative identities at 54 rational points.
    Finite arithmetic only; long-time and population arguments require the proofs.

This finite check complements the complete analytical induction; it does not
establish any asymptotic statement by sampling or replace the proofs.

## Workspace and scientific boundary

Only this new flat study was written. No files in established docs/code, other
studies, or the shared Git index were edited. No subagent was spawned and no
other study was read for this investigation. The two-input anchor was derived
again from the canonical equations, not imported from earlier task findings.
HEAD remained 379ede09d8bcc53a8efedfac53672e3d0711ade2; the index remained empty.
The current source and artifact identities are in manifest.sha256. No generated
training products, new experimental campaign or promotion is involved.
