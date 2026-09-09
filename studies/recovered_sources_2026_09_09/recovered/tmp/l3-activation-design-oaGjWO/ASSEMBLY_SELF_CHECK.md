# Main self-check during isolated whole-proof reviews

This is not an independent review. The full candidate currently sent to
two isolated reviewers has SHA256
d50b7708b767f20010437e48a716366ac32b5dd6db6e6e12beb94cd1d15897e5.
Do not modify that candidate during review without recording a new version.

The response-only audit correctly reserves identification: its formal
scalar estimates allow identity clipping, while the finite-program proof
is used only with smooth bounded clips. The full candidate explicitly
imposes those stronger bounds in its identification section. It verifies
the new F, chi and gate constants and retains uncentered covariances.
Thus there is no need to expand the scope of the response lemma.

A useful optional strengthening of the raw-interpolation velocity paragraph:
on a stopped positive prefix the normalized raw block velocities are
bounded by a width-independent constant. At a raw linear interpolation
step, the two matrix operator norms remain bounded by convexity and the
readout RMS remains bounded. The first preactivation derivative has RMS
at most C. Differentiating z2=W2 phi(z1) and then z3=W3 phi(z2) shows each
recomputed hidden preactivation derivative also has RMS at most C,
uniformly throughout the step. Therefore each hidden preactivation changes
by at most C eta in RMS and C eta sqrt(n) in coordinate supremum on a
step. Since phi' is Lipschitz, its coordinatewise gate change is at most
C eta sqrt(n)=C n^-3/2. Consequently its product with any left-node
velocity of bounded RMS has RMS error O(eta sqrt(n)), without a new
moment assumption. Matrix velocity terms contracted with changed bounded
features have error O(eta); recursive differentiation proves the full
recomputed velocity differs from the left-node formula by O(eta sqrt(n)).
The existing candidate uses the more general uniform-integrability
argument from the old proof. The direct finite-width bound can make this
part more explicit in a revision if a reviewer requests it.

The changed activation is small but fixed. All nonlazy coefficients are
strictly positive population quantities with no n dependence. Strict
best-affine error follows from unbounded hidden support, bounded phi,
and strict monotonicity; a full-density or full-support-on-every-interval
result is unnecessary. Gaussian sources need not be temporally independent.

The old goal object literally describes canonical arctan, so a successful
new theorem must not falsely mark that original conjecture achieved.
Latest real-user scope does authorize this new instance and should be
stated prominently when delivering the outcome.
