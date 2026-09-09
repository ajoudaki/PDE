# Canonical hidden-norm high-order audit

This successor uses the exact canonical Gaussian-program recurrence through
feature order seventeen to compute the two hidden preactivation squared-RMS
jets and their output-coordinate Stieltjes moment candidates.  It also audits
the normalized literal-RMS readouts.

The result is a strict finite-order pass: the first hidden response has nine
moments and positive-definite \(H_4,H_3^+\); the independent second-hidden
companion has eight moments and positive-definite \(H_3,H_3^+\).  Every
accessible principal minor is strictly positive.  This is not an all-order or
positive-time theorem.

Start with [RESULTS.md](RESULTS.md).  Exact machine-readable certificates are
[HIDDEN_MOMENT_HANKEL_AUDIT.json](HIDDEN_MOMENT_HANKEL_AUDIT.json) and the
algebraically separate
[INDEPENDENT_HIDDEN_SCALAR_AUDIT.json](INDEPENDENT_HIDDEN_SCALAR_AUDIT.json).
The two recurrence outputs are
[PRODUCTION_HIDDEN_RESULT.json](PRODUCTION_HIDDEN_RESULT.json) and
[INDEPENDENT_HIDDEN_RESULT.json](INDEPENDENT_HIDDEN_RESULT.json).  The frozen
scope and stop rule are in [PROTOCOL.md](PROTOCOL.md).
