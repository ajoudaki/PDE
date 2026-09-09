# The actual primitive energy has no instantaneous diagonal self-pair

Status: exact finite-width identity, not a response bound. This note
identifies which part of the signed energy in
ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md remains after its scalar
cancellation. It applies to the uncut trajectory and to the prescribed
C1 clipped family on the same common primal-bound events. It does not
assume independence of any actual network coefficient and its response.

Use that note's normalization: vector inner products are divided by n;
matrix entries and matrix transposes are ordinary ones. All expectations
below condition on the entire actual trajectory and average only over
the independent Gaussian derivative probe.

Write, solely in this calculation,

    z=z2, D=diag(phi'(z)), beta=phi''(z)/phi'(z),
    K2=W2 D1^2 W2*, A2=m1 I+K2, m1=||H1||_n^2.

Here q2 is the query denoted q in the cited proof, namely W3*delta3.
Thus K2 is symmetric positive semidefinite. Let g=q2 in the uncut
case and g=tau(q2) in the clipped case; the actual backward vector
is delta2=Dg. The full-layer primitive in the cited proof is
a_delta=Dc. Its actual preactivation response has the exact form

    zeta=A2 D c+v,
    v(t)=integral_0^t N0(t,s)D(s)c(s) ds.                 (1)

Here v is the full retained memory response, not an extra independent
source. Every bounded map in (1) is the one constructed in that proof.
The actual primal preactivation satisfies z'=A2 Dg.

The primitive equation therefore has the split-free form

    c'=u+beta (g zeta-z' c).                             (2)

Products without a matrix in (2) are coordinatewise. In the clipped
case u includes the factor diag(tau'(q2)) exactly as in the cited proof.
To check (2), substitute alpha=m1 and r=K2 Dg in its scalar equation
and expand zeta; the two m1 Dg c terms cancel. No derivative of g,
K2, or a conditional covariance is needed for this substitution.

Put

    Sigma_ij=n E_probe[c_i c_j].

The signed part of one half of the conditional energy derivative is

    S_inst+S_mem
      =-<beta K2 Dg,diag(Sigma)>_n
        +<beta g,n E_probe[c (K2 D c)]>_n
        +<beta g,n E_probe[c v]>_n.                     (3)

The ordinary source <c,u> has the already proved energy bound and
is not part of (3). The last term is S_mem and is left intact.
For arctangent, beta_i=-2 z_i D_i. Expanding the first two terms
and then exchanging i and j in half of the sum gives exactly

    S_inst=(1/n) sum_{i,j} (K2)_ij D_i D_j [
        z_i g_j Sigma_ii+z_j g_i Sigma_jj
                    -(z_i g_i+z_j g_j)Sigma_ij ].       (4)

Indeed the unsymmetrized summand, with prefactor 2/n, is

    (K2)_ij D_i D_j [
                  z_i g_j Sigma_ii-z_i g_i Sigma_ij].

The exchange uses both K2_ij=K2_ji and Sigma_ij=Sigma_ji.
Equivalently, (4) is the polarized response product

    S_inst=(1/n) sum_{i,j} (K2)_ij D_i D_j
        n E_probe[
          (g_j c_i-g_i c_j)(z_i c_i-z_j c_j)].           (5)

Every summand with i=j vanishes exactly. Consequently the remaining
instantaneous term does not contain a diagonal own-coordinate
curvature contribution, even when K2's diagonal is not constant.
It contains the actual off-diagonal mobility and the actual
conditional response covariance, together with S_mem from (3).

Positive semidefiniteness of K2 alone does not assign a sign to (4).
For an elementary algebraic check, take n=2, K2 the all-ones
matrix, z=(1,1), D=I/2, g=(-1,1), and c=(xi,0), where
xi is standard Gaussian. Then K2 Dg=0 and direct substitution in
(3) gives S_inst=1/2. Replacing g by -g gives -1/2.
These are only coefficient/covariance tests of an alleged PSD
implication, not asserted canonical network trajectories or
counterexamples to population continuation.

Thus (4)--(5) strengthen the description of the remaining term:
all instantaneous diagonal self-pairs cancel, while off-diagonal
polarized pairs and causal memory remain. At positive times their
coefficients and covariance are coupled through the actual reused
Gaussian matrices. No independence or nonpositive sign is implied,
and no width-uniform response-closing trace bound or global response
estimate has been proved from this identity.
