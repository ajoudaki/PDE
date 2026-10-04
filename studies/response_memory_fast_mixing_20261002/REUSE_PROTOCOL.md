# Forward/transpose reuse discriminator

Freeze before implementation, 2026-10-02.

H1: matching the initialized forward variance is insufficient to match a
nonlinear return through the transpose; matching the fourth singular moment
removes the leading discrepancy for the Gaussian-probe observable below.
H0: all variance-matched flat/diffuse spectral environments give the same
return energy; or any observed discrepancy is only finite-probe numerical noise.

For h~N(0,I_n), W any deterministic matrix with C=W W^T having C_ii=1,
psi=tanh, measure E ||W^T psi(W h)||²/n. Define v=E tanh(Z)² and
a=E Z tanh(Z), Z~N(0,1). Candidate identity:

    energy = v + a²(tr(C²)/n-1) + R,
    0 <= R <= (v-a²) max_{i!=j}|C_ij|² (tr(C²)/n-1).

This requires proof (odd Hermite expansion), not inference from measurements.
It is a deterministic covariance statement, not a trained-neural universality
theorem. Construct W=H diag(s) V^T using normalized Sylvester Hadamard H,
V=H D with independent signs. s is either1 or normalized deterministic
quarter-circle quantiles in a seeded random permutation. Since H is flat,
C has exactly unit diagonal. Derive quantiles by numerical inversion with
reported tolerance. This prescription does not secretly generate a dense
Gaussian matrix or a dense SVD.

Pre-execution amendment: include normalized absolute-Gaussian singular values
(the two-Hadamard Gaussian-diagonal Fastfood core) and row-normalized dense
Gaussian matrices. The latter has exactly unit covariance diagonal, so the
same deterministic identity applies. No experiments preceded this amendment.
Fastfood row rescalings and alternative implementations are not silently
identified with this explicitly specified core.

Widths128,256,512,1024; four cases per width =16 cases. Each uses128 independent Gaussian
probes at fixed seed6101, with up to128 further probes only if confidence
intervals fail to discriminate the predicted O(1) gap. All eight covariance
matrices can be formed for this SMALL mechanism check; production method must
not form them. Compare explicit-matrix and fast actions/transpose to relative
1e-12 in float64. Numeric expectation v,a uses two Gauss-Hermite orders
(128,256) and must agree within1e-9.

Pass: analytic proof checked algebraically; actions satisfy tolerance;
sample means within4 standard errors plus analytic remainder and1e-9 of the
predicted formula; flat-vs-MP gap exceeds5 pooled standard errors at one
width>=512. Fail or inconclusive outcomes retained. No trained-model or
performance conclusion follows even from a pass. Hard stop after16 cases and
256 probes/case or10CPUminutes. Write raw covariance moments, probe energies,
seeds, environment, source hashes and observed runtime to a fresh run directory.
