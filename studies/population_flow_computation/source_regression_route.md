# Causal source regression: second-round candidate

Coordinator derivation, 2026-09-12. This route was developed independently of
the first-round agent reports. Status: candidate identities; no population
solver convergence or practical certification claim.

## Exact regularized Gaussian identity

For a finite named-source program, put a fresh independent numerical output
noise of variance s^2 at every initialized forward and reverse answer, with
s>0. Use the original A0 and A0* in the mathematical comparison process.
Combine each orientation's centered Gaussian source and its independent
output noise into one named Gaussian source vector. Its covariance is
C_H+s^2 I in the forward orientation and C_D+s^2 I in reverse, where
C_H and C_D are uncentered same-layer input Grams. Different orientations
remain independent. A finite scalar expression depends on these sums; the
source response derivatives are derivatives in their named arguments.

For a centered finite Gaussian vector X with positive covariance C and a
smooth integrable F with integrable derivative, Gaussian integration by
parts gives E[X F]=C E[grad F]. Therefore the exact response row is
C^{-1}E[X F]. Apply this to F=H in the lower population and F=Delta^(2)
in the upper population. Expectations use the whole joint source history.
All deterministic feedback, moments, and covariance entries stay frozen
under source differentiation. This is a response computation by Gaussian
integration, not differentiation of feedback.

At zero regularization and singular C, derivatives in ker C need not be
identified by this regression. Their contraction with the associated input
tuple vanishes in L2, as III.F.14 proves. Thus a minimal-norm response can
give the same contracted action; a proof must retain correct source/input
covariance types.

For a fixed true derivative row b and ridge r>0, replacing it by
b_r=(C+r I)^{-1} C b incurs the contracted error
||C^(1/2)(b-b_r)||_2 <= sqrt(r)/2 ||b||_2.
Indeed each spectral factor sqrt(lambda) r/(lambda+r) is at most sqrt(r)/2,
including lambda=0. This is an exact error estimate for a fixed coefficient
and its matched contraction, not a generated-state closure bound.

## Proposed numerical mechanism and open bridge

Use two numerical populations, complete saved H/Delta/source histories,
empirical Grams plus positive diagonal noise, Gaussian conditional extensions
with prefix-consistent factors, and regression responses from the same joint
fields. Reconstruct the learned K only as its saved rank factors. All updates
use the physical Euler coefficients -2 h p (f-y); no raw hidden matrix is
trained or sampled. The regression avoids storing all source derivatives.

Fresh independent numerical batches can alternatively estimate moments at
each instruction by evaluating the stored finite scalar expressions at new
Gaussian prefixes with the already computed deterministic coefficients. This
costs repeated evaluation of available history and must be counted; it is
not replay of an unavailable target trajectory. Which variant has a usable
generated-error proof remains open.

Required audits: exact source identity with per-call output noise; independence
and adaptedness of estimated moments; PSD and conditioning of every extension;
regression error in the input-Gram metric; nonlinear propagation; and the
joint limit of sampling, physical mesh, data quadrature, noise and precision.
A one-reference raw comparison may control the exact noisy-action process
against C.4.7, but it cannot be applied directly to empirical coefficients
without a common-action or joint-observation coupling.
