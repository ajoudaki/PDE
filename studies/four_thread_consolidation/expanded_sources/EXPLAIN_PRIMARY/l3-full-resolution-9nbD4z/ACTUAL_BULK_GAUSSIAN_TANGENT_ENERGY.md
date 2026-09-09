# Actual-bulk Gaussian tangent energy and the remaining mixed response

Status: exact finite-width response identities and a response-energy reduction. The all-horizon moment bound remains open. No simulation or frozen-bulk substitution is used.

## 1. Full causal derivative with respect to a deleted top column

Work in feature time on [0,S], with the exact uncut network. Use normalized vector norms and the HS/Frobenius norm for matrix variations. Let D_l=phi'(z_l), C=W4, d=D3 C, q=W3* d, delta=D2 q, and H_l=phi(z_l). First-layer state is X1=F(z1), so H1=chi(X1), with chi'=D1^2.

Fix a deterministic middle neuron i. Introduce an auxiliary standard Gaussian probe xi in the top space, independent of the ENTIRE actual initialization and trajectory. Vary only the initial top column through

    K = (xi/sqrt(n)) e_i^T.

The following is the derivative along that variation, with the actual trajectory as coefficient path. Write

    x=dot X1, A=dot W2, B=dot(W3-W3_0), c=dot C,
    y=(x,A,B,c),                y(0)=0.

The total top-matrix variation is K+B. Every trained factor is differentiated:

    u1 = D1^2 x,
    zeta2 = A H1 + W2 u1,                    u2=D2 zeta2,
    zeta3 = (K+B) H2 + W3 u2,               u3=D3 zeta3,
    d_dot = D3 c + C phi''(z3) zeta3,
    q_dot = (K+B)* d + W3* d_dot,
    delta_dot = D2 q_dot + phi''(z2) q zeta2,

    x' = A* delta + W2* delta_dot,
    A' = delta_dot tensor H1 + delta tensor u1,
    B' = d_dot tensor H2 + d tensor u2,
    c' = u3.                                                (1)

A dot denotes initial-data variation; a prime denotes time derivative. In particular u2 is the variation of the actual FULL middle trajectory. No independence between it and the deleted column is asserted.

## 2. Probe averaging improves the forcing by a factor n

On a path with bounded primal norms, define bounded maps

    T_s y = A H1 + W2 D1^2 x,
    R_s v = (W2* v, v tensor H1, 0, 0),
    b_s = phi''(z2) q.

Then (1) has the exact form

    y' = L_s y + R_s M_(b_s) T_s y + f_s(K),             (2)

where ||L_s||, ||R_s||, ||T_s|| are bounded by C_(S,M), independently of width and max|q|. M denotes the finite primal/operator bound. All multiplication coefficients in L_s are bounded; appearances of delta outside the middle multiplier are rank-one factors and are controlled in L2.

The source is explicit:

    d_K = C phi''(z3) K H2,
    v_K = D2 [K* d + W3* d_K],
    f_s(K) = (W2* v_K, v_K tensor H1,
              d_K tensor H2, D3 K H2).

Consequently

    ||f_s(K)|| <= C_(S,M) [||K H2||2 + ||K* d||2].

Conditional on the entire actual path, xi is still independent Gaussian, so exactly

    E_xi ||K H2||2^2 = H2_i^2/n,
    E_xi ||K* d||2^2 = ||d||2^2/n.                      (3)

Thus E_xi||f_s(K)||^2<=C_(S,M)/n. This gain is absent for the worst aligned deterministic direction, where K*d can have order-one normalized size. It uses an independent probe of the derivative, not independence of the actual deleted column.

## 3. Exact covariance term in the scaled response energy

Put

    Lambda_i(s) = n E_xi ||y(s)||^2.

The Hilbert adjoint of R_s in the unweighted transformed state norm is

    R_s* y = W2 x + A H1 =: gamma2,

whereas T_s y=zeta2. Define the mixed probe covariance

    Gamma_(i,j)(s) = n E_xi [gamma2_j(s) zeta2_j(s)].

Taking the energy of (2), using (3) and Young's inequality, gives

    Lambda_i'
      <= C_(S,M)(1+Lambda_i)
          + 2 <phi''(z2) q, Gamma_i>.                   (4)

All inner products here are normalized middle-layer averages. Moreover

    ||Gamma_i||_L1 <= C_(S,M) Lambda_i.                  (5)

The final pairing in (4) is the only coefficient not closed by the existing primal bounds in this transformed tangent calculation. It involves the covariance of a specific zero-initial-data, single-column-seeded Gaussian tangent, rather than an arbitrary variation.

Rank-one training removes part of it entirely. The exact history identity gives

    q = W3_0* d + k,
    ||k||infinity <= a^3 S^3/2.

The k contribution in (4) is bounded by C_(S,M)Lambda_i using (5). Thus the unresolved quantity can be narrowed to

    <phi''(z2) W3_0* d, Gamma_i>.                        (6)

A sufficient spatial estimate would be ||Gamma_i||2<=C Lambda_i; then the already bounded L2 norm of q closes (4). This is a delocalization statement about this particular probe covariance, and has not been proved.

For moment bounds, an even more tailored sufficient estimate is the following full-Gaussian-law inequality, for r>=1. If localization is used to obtain it, its boundary terms must be included rather than discarded:

    E[Lambda_i^(r-1)
      <phi''(z2) W3_0* d, Gamma_i>]
      <= C E[Lambda_i^r]
         + C r log(e+r)^2 E[Lambda_i^(r-1)].             (7)

When the other constants are uniform, (4) and Holder imply

    d/ds ||Lambda_i||_r
       <= C ||Lambda_i||_r + C r log(e+r)^2,

hence ||sqrt(Lambda_i(s))||_p<=C_S sqrt(p)log(e+p), uniformly for s<=S. Equation (7) is not established here.

## 4. Why this response energy controls both deleted-query Jacobians

Let bar d be the copied-top query with neuron i removed from its input, still driven by the actual bulk path. Let J_i=D_(W3_0[:,i]) bar d be its ordinary n-by-n Jacobian. Under the probe above,

    dot bar d = J_i xi/sqrt(n).

Its input derivative is (I-P_i)u2. The bounded copied-top variation equations give, pointwise in the actual initialization,

    ||J_i(s)||HS/sqrt(n)
      = sqrt[n E_xi ||dot bar d(s)||2^2]
      <= C_(S,M) [sqrt(Lambda_i(s))
                    + integral_0^s sqrt(Lambda_i(u)) du]. (8)

This follows by applying the instantaneous-plus-integrated L2 top-response estimate to (I-P_i)u2, followed by Minkowski in xi and the boundedness of T_u. In particular, it requires no exchange between a time supremum and the probe expectation.

Thus

    |Tr J_i|/n <= ||J_i||HS/sqrt(n),
    ||J_i^T g/n||Euclidean
      <= [||J_i||HS/sqrt(n)] [||g||Euclidean/sqrt(n)],    (9)

where g=sqrt(n) W3_0[:,i] is the actual Gaussian column. Both vector norms in (9) are ordinary Euclidean norms, not normalized population norms; the matrix HS norm is the ordinary Frobenius norm. No independence between J_i and g is used in (9). Under the full Gaussian law, |||g||Euclidean/sqrt(n)||_p <=1+C sqrt(p/n). The top-response constants in (8) are polynomial in initial operator norms, whose fixed-degree moment factors are bounded when n is sufficiently large relative to p.

Therefore a uniform-in-time Lp bound C sqrt(p)log(e+p) for sqrt(Lambda_i(s)), with the indicated operator-norm weights and a harmless increase of p, suffices for BOTH normalized-trace and Gaussian-direction targets in DELETED_QUERY_RESPONSE_AND_ENTROPY_AUDIT.md. Minkowski handles the time integral in (8). The reduction uses a normalized HS covariance quantity, not a full Jacobian operator-norm estimate.

## 5. Gaussian integration by parts exposes a mixed second response

There is an exact reason why averaging the original Gaussian disorder does not immediately close (6). For r=1, write phi''_j=phi''(z2_j). Under justified Gaussian integration by parts,

    E <phi''(z2) W3_0* d, Gamma_i>
      = (1/n^2) sum_(a,j) E [
          (partial_(W3_0,aj) d_a) phi''_j Gamma_(i,j)
          + d_a phi'''(z2_j)
              (partial_(W3_0,aj) z2_j) Gamma_(i,j)
          + d_a phi''_j
              partial_(W3_0,aj) Gamma_(i,j) ].          (10)

The last derivative is

    partial_w Gamma_(i,j)
      = n E_xi [
          (partial_w gamma2_j) zeta2_j
          + gamma2_j (partial_w zeta2_j) ].             (11)

These are mixed second derivatives of the actual causal flow: one derivative is the column probe and the other is an initial Gaussian entry. Wick averaging in xi contracts its Gaussian factors but leaves these mixed flow derivatives. For r>1, differentiating Lambda_i^(r-1) introduces further contractions with the same mixed derivatives.

The mixed second variation Z^(v,w) of a finite-dimensional flow obeys

    Z' = DV Z + D^2V[U^v,U^w],       Z(0)=0.

Here the second source contains, among other exact middle-gate terms,

    phi'''(z2) q zeta2^v zeta2^w
      + phi''(z2) [q_dot^v zeta2^w + q_dot^w zeta2^v].

Thus no closure follows merely from the Gaussianity of the probe or the rank-one form of weight training. The uncanceled term (11), with its signed contraction in (10), is a narrower next resolver than a full tangent operator bound.

## 6. Relation to the new pruned-row Wishart geometry

The independent rows in a fully pruned reference can describe the scalar part of rare-layer mobility and may be useful for estimating the specific covariance Gamma_i. They cannot currently replace the actual W2, D1, gamma2, or zeta2 in (4): all of those have been propagated through the original feedback.

There is a real own-site cancellation in the scalar comparison. For z'=a(s)q(s)phi'(z), zero initial tangent, and a variation only of q, the exact derivative satisfies

    zeta(s)=phi'(z(s)) integral_0^s a(u) q_dot(u) du.

The large q multiplier does not amplify this response. With an additional bulk forcing c(s), the integrating-factor equation acquires the coefficient -(phi''/phi')(z)c(s), as well as the variation of c. The rare diagonal approximation therefore isolates a useful principal cancellation, but transferring it to (4) still requires estimating the actual bulk/covariance correction. No such transfer is assumed in this note.

## Conclusion

A new positive fact is the exact 1/n mean-square tangent forcing and the HS bridge (8)--(9). Rank-one learned top history is also harmless in the energy. The remaining obstruction is a specified mixed covariance pairing of the actual causal tangent; original-Gaussian integration by parts converts it into mixed second-response contractions, not independent noise. Closing (7), or the stronger spatial covariance estimate following (6), would advance the global theorem. Neither is proved here.
