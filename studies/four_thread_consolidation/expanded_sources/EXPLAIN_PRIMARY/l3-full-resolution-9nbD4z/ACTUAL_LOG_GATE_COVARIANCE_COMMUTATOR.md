# Actual log-gate commutator: a metric cancellation and the surviving energy

Status: exact finite-width identities for the actual response. The ordered
commutator has a genuine cancellation in the instantaneous mobility metric,
including a positive metric for the corrected response. This does not bound
the complete response energy: symmetric log-derivative, lower-mobility, and
fully transformed source terms remain. No experiment or canonical negative
theorem is asserted, and no frozen source is modified.

Use the actual uncut trajectory, common primal bounds, and uncut coercivity
premise of ACTUAL_LOG_GATE_SECOND_IBP.md, with the primitive and complete
source in ACTUAL_BACKPROP_PRIMITIVE_RESPONSE.md. The identities apply to
zero or prescribed tiny readout. The initialization calculation below is
only for zero readout. No clipped coercivity or clipped extension is claimed.
All matrices, including K2, retain their actual time dependence.
Matrix transposes and traces are ordinary; ||.||_2 is the ordinary
Euclidean norm, while <.,.>_n divides the vector inner product by n.

## 1. Actual conditional covariance and the ordinary trace

Reserve C for the mobility A2/m1, not the readout. Write

    L=diag(log(phi'(z2))),  C=I+K2/m1,  K2=W2 D1^2 W2*,
    B=L C,  B0=L' C,  P=I-B,  a=a_delta,  eta=P a,
    Gamma=n E_probe[a a*].

Thus C=C*>0, C>=I, L=L*<=0, and Gamma=Gamma*>=0. The
expectation conditions on the entire actual initialization and path and
averages only the independent single-column derivative probe. In particular
Gamma need not be scalar or independent of C or L.

Define

    J=L C L'-L' C L,                 J*=-J,
    Q=[B,B0]=J C.

The entries of J are exactly

    J_ij=C_ij(L_i L_j'-L_i' L_j),

so its diagonal vanishes. Its off-diagonal coefficients retain the actual
K2_ij/m1. Ordinary trace cancellation Tr(Q)=0 does not give the response
trace cancellation. The precise identity is

    n E_probe<a,Qa>_n
       =(1/n) Tr(J C Gamma)
       =(1/(2n)) Tr(J[C,Gamma]).                       (1)

Indeed transposing inside the trace gives
Tr(J C Gamma)=-Tr(J Gamma C). Thus the remaining ordinary-energy
contraction is the gate-area skew matrix J paired with the actual covariance
commutator [C,Gamma]. In particular, commutation of C and Gamma would
annul (1), but such commutation is not inferred from probe Gaussianity.

## 2. The mobility metric cancels the same-vector commutator exactly

Since B* C=C B and B0* C=C B0,

    Q* C=-C Q,     C Q=C J C is skew-symmetric.

Consequently, for every realized probe, not merely on average,

    a* C Q a=0.                                       (2)

This is a stronger cancellation than Tr(Q)=0: it uses the correct metric
and holds for the actual adaptive covariance without an independence or
delocalization assumption.

The energy for eta in that same C metric does not have identical vectors
on both sides of Q. Since P* C=C P, (2) instead gives

    n E_probe<eta,C Q a>_n
       =-(1/(2n)) Tr(C[B,Q] Gamma).                   (3)

To verify this, eta* C Q a=a* C(I-B)Q a=-a* C B Q a;
the symmetric part of C B Q is C[B,Q]/2. Therefore C[B,Q] is
symmetric, and the right side of (3) is a surviving double-commutator
response contraction. The term -Q a/2 in the second-IBP equation
contributes +(1/(4n))Tr(C[B,Q]Gamma) to the derivative of
(n/2)E_probe<eta,C eta>_n. This statement includes that equation's
other terms; it does not estimate or discard them.

## 3. A positive eta metric cancels Q but retains symmetric gate work

The double commutator in (3) is not unavoidable under every metric.
Define the time-dependent symmetric positive matrix

    G=C P^{-1}
      =C^{1/2}[I-C^{1/2}L C^{1/2}]^{-1}C^{1/2}.

Since L<=0, 0<G<=C. Moreover

    eta* G eta=a* C P a
       =a* C a+(C a)*(-L)(C a)>=||a||_2^2,
    eta* G Q a=a* C Q a=0.                            (4)

Thus this is a genuine positive energy controlling the primitive, although
G need not be uniformly coercive as an energy for eta itself.

Keep the complete equation and source from the second-IBP note:

    a'=B0 a+F,
    F=D2 u-diag(beta r) C a+diag(b) v,
    r=K2 delta2,   b=phi''(z2)q2,
    v(t)=integral_0^t N0(t,s)a(s)ds,
    H=L C',       eta'=P F-H a-B B0 a.                (5)

Here u contains all response-dependent non-curvature terms. Only its
previously proved unweighted estimate is available; F is not newly bounded.

For the positive energy

    E_G=(n/2) E_probe<eta,G eta>_n
       =(n/2) E_probe<a,C P a>_n,

differentiate the latter expression in (4), using (5). Since
(C P)'=C'-C' L C-C L' C-C L C', the exact result is

    E_G'
      =n E_probe<a,C P F>_n
       +n E_probe<a,C( (1/2)I-B )B0 a>_n
       +(n/2) E_probe<a,
             [C'-C' L C-C L C']a>_n.                  (6)

In particular Q cancels in the middle term's quadratic form, whose exact
symmetric matrix is

    (1/2) C B0-(1/2) C(B B0+B0 B).                    (7)

Equation (7) still contains L'. It is not controlled by the already proved
spatial amplitude tail for L. Equation (6) also retains the log-weighted
complete source C P F and every contribution of C'. In the notation of
the source note,

    C'=A2'/m1-(m1'/m1)C,
    A2'=m1'I+delta2 tensor k+k tensor delta2
       +W2 diag(2 D1^2 phi''(z1)q1)W2*,
    k=W2 D1^2 H1,       q1=W2*delta2.

The lower-gate multiplier in this formula is included in (6). Bounded C
does not bound C', and a bounded inverse for P does not bound C P F.
Integration by parts in (7) also differentiates the actual response, hence
reintroduces (5); it does not make (7) an endpoint-only estimate.

## 4. What Gaussian initialization actually supplies

For the actual probe at a fixed middle site r, write a(t)=M(t)xi with
xi standard Gaussian independent of the path. Exactly

    Gamma(t)=n M(t)M(t)*.

This identity imposes positivity, not isotropy or commutation with C.
The actual zero-readout initial jet makes its geometry more explicit.
Evaluate all quantities below at time zero, and put

    h=H2, d0=D3 H3,
    E3=diag(phi'(z3)^2+phi(z3)phi''(z3)),
    R_r=e_r d0*+h_r W3* E3.

The differentiated actual equations give

    a(0)=a'(0)=0,       a''(0)=D2 R_r xi/sqrt(n),
    Gamma(t)=(t^4/4)D2 R_r R_r* D2+o_n(t^4).          (8)

For example a''(0) follows by differentiating delta2 once in time:
the variation of q2'(0)=W3*D3 H3 is
K*d0+W3*E3 K h, where K=xi e_r*/sqrt(n).
Thus the leading covariance includes the localized contact term
||d0||_2^2 D2_r^2 e_r e_r*, plus its exact cross and distributed
terms. Those other terms are retained in R_r R_r*. No cancellation or
noncancellation of their sum is asserted without computing the actual
joint contraction. The remainder in (8) is at fixed width, not uniform
over n. At zero readout L'(0)=0 and Q(0)=0; there is no initial
nonzero-commutator claim. Formula (8) is not used for tiny readout.

The elementary Gaussian neuron-sign symmetry does not by itself make the
quantity in (1) odd. For a diagonal middle sign matrix S, the actual
network and probe law transform as

    C -> S C S,   J -> S J S,   Gamma -> S Gamma S.

The extra sign of the fixed probe column disappears in Gamma. Hence
Tr(J[C,Gamma]) is invariant under this symmetry. Exchanging middle labels
likewise conjugates the two matrices (and the probe-site label). Therefore
these symmetries supply no automatic vanishing of the signed contraction.
This is not a claim that a more detailed Gaussian average cannot help.

The new proved fact is the exact metric cancellation (2) and its positive
corrected-response version (4). The ordinary covariance obstruction is
precisely (1); in the elementary C energy for eta it becomes (3). The
positive metric replaces that double commutator by the full symmetric
energy (6), which is still unestimated. No response trace moment, global
continuation, or zero-to-tiny transfer is proved by these identities.
