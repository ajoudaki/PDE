# Adversarial audit of `UNIFORM_L3.md`

## Verdict

**PASS as an open-result audit; FAIL as a proof of the desired uniform
network theorem.**  The note does not claim otherwise.

## Checks

1. **Limit order:** every network identification is pointwise at fixed
   step size.  No finite-width Taylor expansion or width/step limit
   interchange is used.
2. **Sign and coefficient:** the remainder is written as
   \(D_{t,3}+t(2t-1)J_{\phi,3}h^3/2\), consistent with
   \(\kappa_{\phi,3,t}=-t(2t-1)J_{\phi,3}/2\).
3. **Time factor:** exact local factorization removes \(h^2\); three
   derivatives of each transported defect cost \(t^3\), and there are
   \(t\) defects. The conditional power is therefore \(t^4\).
4. **Causal factorization:** a past transpose source can reach a future
   feature only through its source-time parameter update.  A past forward
   source can reach a future cotangent only through the same update.  The
   factors in (4.1)--(4.5) are therefore exact.  The current backward
   response is correctly left unscaled.
5. **Singular histories:** the directed-path divisibility proof is
   algebraic and does not invert a Gram matrix.
6. **Connector obstruction:** Proposition 7.1 is valid.  The reverse
   triangle inequality and the fact that \(Jc_m\) is standard Gaussian
   show that even identical all-moment input laws do not control the
   target \(L^p\) norm of \(W x_m\).
7. **Embedding in \(L=3\):** the obstruction occurs independently at
   both \(W_2\) and \(W_3\). Adding a third layer does not create an
   ambient \(L^p\) estimate.
8. **No false counterexample claim:** the constructed \(c_m\)'s are not
   asserted reachable.  They disprove the proposed proof shortcut, not
   the network inequality.
9. **General depth:** (8.1) is a genuine layerwise pattern. The map
   \(\Gamma_{\phi,a}\) is explicitly labelled missing, so (8.2)--(8.3)
   are a criterion rather than a claimed induction proof.
10. **Source-derivative hierarchy:** Lemma 5.1 proves only the nodewise
    commutation statement for one fixed local block. The note correctly
    leaves closure of mixed incident-block sensitivities unproved.
11. **Gaussian accumulation:** Lemma 5.2 is valid without independence.
    It controls a weighted linear Gaussian envelope.  The note correctly
    refrains from assuming that every \(L=3\) tangent term already has that
    form; products in matrix-gradient and current-response jets still need
    a subexponential semiring estimate.

## Unclosed obligation

The exact missing theorem is a horizon-independent bound on normalized
source tangents (5.1) and their first three common-step derivatives, strong
enough to imply (6.1)--(6.2).  Neither all-moment membership nor boundedness
of the fixed connectors on \(L^2\) supplies it. Until that theorem is
proved, no activation-only \(C_{\phi,3},c_{\phi,3}\) in the uniform
\(t^4h^5\) estimate has been constructed.
