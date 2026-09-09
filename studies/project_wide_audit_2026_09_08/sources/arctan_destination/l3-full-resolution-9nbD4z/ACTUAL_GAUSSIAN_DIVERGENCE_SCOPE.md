# Actual Gaussian divergence: exact identity and reference-law mismatch

Status: exact finite-width identities, and a proved obstruction to comparing
the complete trained state with its initialization Gaussian. For the canonical
tiny Gaussian readout, the relative entropy is of order n^3 at each sufficiently
small fixed positive time; its normalization by the ambient dimension also
diverges. The log likelihood itself is of order n^3 with probability tending
to one. These facts do not disprove global mean-field convergence, and do not
exclude a different, quantitatively justified comparison law for a compressed
query. No simulation, zero-to-tiny-readout stability transfer, or response bound
is used.

The target and prior state are CONTRACT_AND_LEDGER.md,
LOGARITHMIC_NETWORK_COMPARISON.md, and
DELETED_QUERY_RESPONSE_AND_ENTROPY_AUDIT.md. This note tests the specific
proposal that actual-flow Liouville/Gaussian divergence supplies the missing
rare-query likelihood estimate.

## 1. Raw state, whitening, and all trained blocks

Use the raw first preactivation, not its nonlinear primitive:

    theta=(z,U,V,C)=(z^(1),W^(2),W^(3),W^(4)).

Write ||x||_n=||x||_Euclidean/sqrt(n), h_l=arctan(z_l),
D_l=diag((1+z_l^2)^(-1)), and a=pi/2. Then

    z_2=U h_1,                 z_3=V h_2,
    delta_3=D_3 C,             q=V^T delta_3,
    delta_2=D_2 q,             v=U^T delta_2,
    delta_1=D_1 v,             f=C^T h_3/n.

The exact uncut feature-time vector field b is

    z'=delta_1,
    U'=delta_2 h_1^T/n,
    V'=delta_3 h_2^T/n,
    C'=h_3.                                                   (1)

The initialization law gamma_n is a nondegenerate Gaussian on
N=2n^2+2n raw coordinates. Its density is proportional to exp(-Q_n), where

    Q_n(theta) = (||z||^2 + n||U||_F^2 + n||V||_F^2
                                      + n^2||C||^2)/2.        (2)

Thus the standard Gaussian coordinates are

    y=(z, sqrt(n) U, sqrt(n) V, n C).                         (3)

In particular, the readout whitening factor is n, not sqrt(n) and not 1.
If A is the linear map in (3), the whitened field is

    beta(y) = A b(A^(-1)y)
            = (delta_1, delta_2 h_1^T/sqrt(n),
                         delta_3 h_2^T/sqrt(n), n h_3).

Ordinary divergence is invariant under this constant conjugation:
div_y beta=div_theta b. Gaussian divergence is instead

    div_gamma beta = div_theta b - DQ_n(theta)[b(theta)].      (4)

This is a density identity for the actual Gaussian law; no conditioning on
an initial operator-norm event occurs in it.

## 2. Exact ordinary and Gaussian divergences

Put m_l=||h_l||_n^2 and

    A_2=m_1 I+U D_1^2 U^T,
    A_3=m_2 I+V D_2 A_2 D_2 V^T.

Direct differentiation of every diagonal coordinate of (1) gives

    div b = sum_j phi''(z_j) v_j
          + sum_i (A_2)_(ii) phi''((z_2)_i) q_i
          + sum_k (A_3)_(kk) phi''((z_3)_k) C_k.              (5)

To check all training contributions, differentiation of z' contributes

    sum_j phi''(z_j)v_j
    + Tr[U D_1^2 U^T diag(phi''(z_2)q)]
    + Tr[V D_2 U D_1^2 U^T D_2 V^T diag(phi''(z_3)C)].

The U-block contributes

    m_1 Tr[diag(phi''(z_2)q)]
    + m_1 Tr[V D_2^2 V^T diag(phi''(z_3)C)],

the V-block contributes m_2 Tr[diag(phi''(z_3)C)], and
the C-block contributes zero. Their sum is (5). In particular the two
matrix-training contributions have not been discarded.

The Gaussian energy derivative is especially simple:

    DQ_n[b] = z^T delta_1 + z_2^T delta_2 + z_3^T delta_3
                                               + n^3 f.     (6)

For example n Tr(U^T U')=delta_2^T U h_1=delta_2^T z_2,
while n^2 C^T C'=n^3 f. Combining (4)--(6) gives the exact
Gaussian-divergence formula. An O(n) ordinary trace estimate does not
bound this expression by O(n).

The alternative coordinate X=F(z), F(z)=z+z^3/3, does not remove this
term. Its initialization density is the pushforward of gamma_n, with
negative log density

    Q_n(F^(-1)(X),U,V,C) + sum_j log(1+z_j^2)

up to a constant. The ordinary divergence changes by

    D[sum_j log(1+z_j^2)][b]
      = -sum_j phi''(z_j)v_j.

This exactly cancels the corresponding density-Jacobian change in
Gaussian divergence. Treating X as Gaussian would give the wrong law.

## 3. What the primal bounds really prove for density transport

Let R_0=||C_0||_n and M=max(||U_0||_op,||V_0||_op). On a fixed feature
interval |s|<=S, the bounded activation and rank-one updates give

    ||C_s||_n <= R_0+aS,
    ||V_s||_op <= M+a R_0 S+a^2 S^2/2,
    ||U_s||_op <= M+a integral_0^S
                   [M+a R_0 u+a^2 u^2/2](R_0+a u) du.        (7)

These estimates apply in either direction of feature time. Together with
the smooth field they give global finite-dimensional existence and an
invertible smooth flow Phi_s. Local invertibility follows from the
variational ODE; the complete backward flow is its inverse.

All constants below can be bounded by polynomials in S, M and R_0.
In particular (5), |phi''|<=2, and
||D_l||_op<=1 give

    |div b(theta_s)| <= n P_S(M,R_0).                       (8)

For example, the three sums in (5) are bounded by 2n times,
respectively, ||v||_n, ||A_2||_op ||q||_n, and
||A_3||_op ||C||_n. These quantities are bounded by (7).

Let Q_H=(||z||^2+n||U||_F^2+n||V||_F^2)/2 denote the hidden part of
the Gaussian energy. Since |x phi'(x)|<=1/2,

    |DQ_H[b]| <= (n/2)(||v||_n+||q||_n+||C||_n)
               <= n P_S(M,R_0).                            (9)

No bound on the initial Frobenius norms or maximum preactivation is
needed to estimate this *change* of hidden energy.

Let mu_s=(Phi_s)_# gamma_n and L_s=dmu_s/dgamma_n. Ordinary change of
variables and the scalar determinant ODE prove exactly

    log L_s(Phi_s(theta_0))
      = Q_n(theta_s)-Q_n(theta_0)
                         - integral_0^s div b(theta_u) du
      = (n^3/2)(||C_s||_n^2-||C_0||_n^2) + E_s(theta_0),   (10)

where

    |E_s(theta_0)| <= n P_S(M,R_0).                         (11)

Equivalently, the derivative of log likelihood along an actual trajectory
is -div_gamma beta. This is the precise connection to the O(n)
log-determinant estimate in the earlier Jacobian note: that estimate
controls only the last integral in the first line of (10).

The Gaussian matrix operator norms have width-uniform moments of every
fixed order (a fixed-radius net and the scalar Gaussian tail prove this),
and E[R_0^p]=O_p(n^(-p)) for every fixed p>0. Hence (10)--(11) are integrable under
the full initialization law, and

    D(mu_s || gamma_n)
       = (n^3/2) E||C_s||_n^2 - n/2 + O_S(n).              (12)

The O_S(n) term is two-sided. This identity uses
E||C_0||_n^2=n^(-2), and involves no Gaussian integration by parts across
the boundary of a high-probability event.

## 4. Actual tiny-readout flow has an n^3 likelihood cost

Here is a self-contained small-time lower bound; it does not infer tiny
readout stability from the zero-readout population theorem.

Define v_0=1 and v_l=E[arctan(sqrt(v_(l-1))G)^2] for l=1,2,3,
where G is standard normal. All v_l are positive. Conditional on the
preceding hidden layer, each new Gaussian matrix gives iid preactivations
with variance ||h_(l-1)||_n^2. The ordinary law of large numbers, applied
successively to the bounded squared activations, yields

    ||h_3(0)||_n^2 -> v_3 > 0 in probability.               (13)

With probability tending to one, M is bounded by a fixed constant,
R_0<=2/n, and ||h_3(0)||_n>=kappa>0. On this event (7) gives uniform
small-time constants. The actual preactivation equations are

    z_2'=A_2 delta_2,
    z_3'=m_2 delta_3+V D_2 A_2 delta_2.

Consequently ||h_3'(u)||_n<=B(R_0+u) for 0<=u<=1, with B independent
of n on this event. Integrating twice gives

    ||C_s-C_0-s h_3(0)||_n <= B(R_0 s^2/2+s^3/6).         (14)

Choose s_*>0 small enough that B s_*^2/6<=kappa/4. For every fixed
0<s<=s_*, and all sufficiently large n, (14) proves

    ||C_s||_n >= kappa s/2                                (15)

on the same high-probability event. Combining (10), R_0<=2/n, and (15),

    log L_s(theta_s) >= (kappa^2 s^2/8)n^3-O_S(n)          (16)

with probability tending to one under the actual law mu_s. Equations
(7), (12), and (15) also imply constants 0<c_s<C_s<infinity such that

    c_s n^3 <= D(mu_s||gamma_n) <= C_s n^3                 (17)

for every sufficiently large n. In particular,

    D(mu_s||gamma_n)/(2n^2+2n) -> infinity.

This refutes an O(n) entropy assertion and even a bounded entropy per raw
coordinate for this particular reference law. It is more than a failure
to deduce query tails from weak entropy: the needed width-uniform
likelihood tail against gamma_n is false. For any epsilon>0,

    E_(gamma_n)[L_s^(1+epsilon)]
       = E_(mu_s)[exp(epsilon log L_s)]
       >= (1-o(1)) exp(c_s epsilon n^3).                  (18)

The weaker width-uniform log-likelihood tail proposed in the deleted-query
audit fails against this reference for the same reason.

These conclusions also hold at sufficiently small fixed *physical*
times for the actual gradient flow. Its field is

    B(theta)=2(1-f)b(theta),
    K=Df[b]=||delta_1||_n^2+m_1||delta_2||_n^2
                         +m_2||delta_3||_n^2+||h_3||_n^2,
    div B=2(1-f) div b-2K.                                (19)

The physical density identity uses DQ_n[B] instead of DQ_n[b], so the
endpoint readout term in (10) is unchanged. On a fixed forward physical
interval the residual decreases in absolute value; therefore the total
absolute feature-clock length is at most 2T(1+aR_0). Equations (7)--(9)
and (19) bound the remainder in (10) in expectation by O_T(n).
On the event used above, for small feature time |f|<=a(R_0+a s)<=1/2,
so 1<=ds/dt<=3. Thus small fixed physical time corresponds to a feature
time between t and 3t, and (14)--(18) apply with changed constants.

## 5. Widening the reference or setting the readout to zero

For comparison, keep the original hidden Gaussian factors but replace
the reference readout by N(0,tau^2 I_n), with a fixed tau>0. Call this
new reference nu_(n,tau); it is not the initialization law. Exactly,

    log(dmu_s/dnu_(n,tau))(theta_s)
      = n log(n tau)
        + (n/(2tau^2))||C_s||_n^2
        - (n^3/2)||C_0||_n^2 + E_s(theta_0).               (20)

Consequently

    D(mu_s||nu_(n,tau)) = n log n+O_(S,tau)(n).            (21)

The proposed time-matched variance v_s=n^(-2)+s^2 gives, for the
reference nu_s=gamma_H tensor N(0,v_s I_n), the exact formula

    D(mu_s||nu_s)
      = (n/2) log(1+n^2 s^2)
        + (n/(2v_s)) E||C_s||_n^2 - n/2 + E E_s.          (21a)

Since ||C_s||_n<=R_0+a s, the middle positive term is O(n), uniformly
over n and 0<=s<=S; (11) has expectation O_S(n). Therefore

    D(mu_s||nu_s) = (n/2) log(1+n^2 s^2)+O_S(n).          (21b)

The lower bound by (n/2)log(1+n^2 s^2)-C_S n requires no lower bound
on the trained readout norm. For every fixed s>0 the leading term is
n log n. This expectation statement is under the full Gaussian law.

Thus the large n^3 term can be changed by changing the reference. It
does not thereby become a query likelihood estimate: even the actual
log likelihood in (20) is n log n+O(n) on the high-probability events
M<=M_* and n R_0<=2 used above.
The entropy per ambient coordinate tends to zero, while the unnormalized
likelihood cost diverges. The earlier bounded-mutual-information example
already rules out inferring uniform query-tail integrability merely from
such a normalized entropy bound.

For exactly zero initial readout, the initial law is supported on the
codimension-n plane C=0. Its image under the smooth flow is a
codimension-n submanifold, so its relative entropy against any
nondegenerate full-state Gaussian is infinite. Relative entropy against
the *initial* singular law is also infinite for positive feature time.
Indeed C'=h_3 and

    <C,C''>_n=||delta_1||_n^2+m_1||delta_2||_n^2
                                      +m_2||delta_3||_n^2 >=0.

For R(s)=||C(s)||_n this implies R''>=0 wherever R>0, and
R'(0+)=||h_3(0)||_n>0 almost surely. Hence
R(s)>=s||h_3(0)||_n>0 for s>0. Thus mu_s({C=0})=0 whereas
mu_0({C=0})=1: the two measures are mutually singular. This is a
statement about full-measure carriers, not disjoint topological supports.
An intrinsic area formula on the moved manifold
is possible, but is not an ambient Gaussian-density comparison.

## 6. Projection and smoothing do not inherit the claimed consequence

The preceding obstruction concerns the complete-state reference. It does
not lower-bound the entropy of a projection. For H=(z,U,V), the exact
chain rule is

    D(mu_s || gamma_H tensor gamma_C)
      = D(mu_(s,H)||gamma_H)
        + E_(mu_(s,H)) D(mu_s(C|H)||gamma_C).               (22)

The readout conditional term can carry the large cost. Data processing
gives an upper bound on the first term, not a license to discard the
second term from the flow formula. For a smooth hidden marginal density,
its continuity equation has velocity E[b_H(theta_s)|H_s=H]; taking its
divergence differentiates this conditional law. Formula (5) alone does
not supply that projected divergence estimate.

There is also a specific reference mismatch for a deleted-column query.
That query retains an *initial* Gaussian column g and an adaptive coefficient
u(g,xi). The law needed to compare g dot u with an independent Gaussian
query is the joint law of (g,u), with the appropriate product reference.
The full current-state Gaussian likelihood in (10) is not this likelihood.
In fact, since Phi_s is invertible, g is a deterministic function of the
full current state theta_s. Therefore

    law(g,theta_s) is singular relative to
                             gamma_g tensor law(theta_s). (23)

To prove (23), take the graph of g=pi_g Phi_s^(-1)(theta_s). The actual
joint law assigns it probability one; the product law assigns it zero
because gamma_g has no atoms. Compressing theta_s to the supplied bulk or
query can remove that singularity, but must be analyzed for that specific
map. Its density and likelihood tail do not follow from Liouville's
full-state determinant identity.

Adding independent noise creates a different law and can regularize such
singularities. It does not give the original deterministic query a density
retroactively. For example, in correctly whitened coordinates, coupling
two random vectors Y,Z and adding independent N(0,sigma^2 I) noise yields

    D(law(Y+noise)||law(Z+noise))
                        <= E||Y-Z||^2/(2sigma^2).          (24)

This follows by conditioning on the coupling, using the exact equal-
covariance Gaussian KL, then forgetting the coupling. For Y=A theta_s,
Z=A theta_0, the readout part of this transport cost is
n^3 E||C_s-C_0||_n^2/(2sigma^2). At a fixed sufficiently small positive
time, reducing this particular cost to O(n) requires whitened sigma
at least of order n; choosing that scale gives raw readout noise of
order one. Equation (24) is an upper bound, not a necessity
theorem for every smoothing construction. Any smaller-noise or projected
argument needs its own quantitative estimate and a limit back to the
actual observable.

The Gaussian *probe covariance entropy* after smoothing, computed in
LOGARITHMIC_NETWORK_COMPARISON.md, is a further different object: it is
the log determinant of a conditional linear Gaussian tangent covariance.
Neither its reference measure nor its random variable is mu_s. It cannot
replace any of (10), (22), or (23).

## Exact scope of the outcome

Proved: the canonical raw/whitened divergence identity, an O(n) bound on
ordinary volume and hidden Gaussian-energy changes, and n^3 full-state
relative entropy and typical log-likelihood cost against the actual tiny-
readout initialization Gaussian at small positive time. A broadened
readout Gaussian instead gives n log n+O(n) entropy; the zero-readout
ambient comparison is singular.

Defeated proposal: deriving the missing width-uniform rare-query
likelihood bound directly from the existing O(n) Liouville trace or
logarithmic singular-distortion estimate against the initialization law.

Unchanged: global canonical mean-field convergence, bulk deletion
stability, and the signed recycled-response bound remain open. A carefully
chosen compressed joint comparison law is not ruled out, but its
absolute continuity and strong likelihood control are new obligations;
they have not been obtained by this test.
