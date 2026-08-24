# Evidence ledger: two-input raw-cubic equal-label MSE channel

## Current research state

| Category | Contents |
|---|---|
| Established | The finite-network MSE evolves through the full tangent-kernel matrix; its exchange-symmetric restriction is the plus channel.  The exact fixed-order symbolic plus-channel jet through order five, the lower-order factorization, the initial full matrix, and the Sturm sign certificates pass all stated gates. |
| Supported | The fixed-order width-first Gaussian-program/detransposition rules correctly represent this two-input model, conditional on the same formal limit assumptions used by the accepted one-input compiler. |
| Falsified | A single scalar kernel is not an exact closed description of a generic finite random two-output realization. |
| Open | Positive-time self-averaging and existence, global output-coordinate invertibility, arbitrary-order closure, and generic asymmetric matrix-valued evolution. |
| Superseded | The pre-audit bottom-flow recurrence that attached \(U_r^2\) to the target sample rather than \(U_q^2\) to the source sample. |

### C-1: full two-example loss dynamics

- Statement: For \(\mathcal L=\tfrac12\sum_{r=1}^2(f_r-1)^2\), \(\Theta_{rs}=n\nabla f_r\cdot\nabla f_s\), and \(\dot\theta=-\eta n\nabla\mathcal L\), the exact finite-network identity is \(\dot f=-\eta\Theta(f-\mathbf1)\) and \(\dot{\mathcal L}=-\eta(f-\mathbf1)^T\Theta(f-\mathbf1)\).
- Claim-ladder rung: exact algebraic identity.
- Status: Proved.
- Scope and assumptions: Any differentiable two-output network with the displayed loss and metric scaling.
- Supporting evidence: Direct chain rule; the model-specific definitions in `PROTOCOL.md`.
- Contrary evidence: None.
- Dependencies: Differentiability only.
- Cheapest decisive resolver: Symbolically differentiate the loss and outputs.
- Concrete falsifier: A differentiable parameter path satisfying the stated gradient flow but violating either identity.
- Supersedes: None.
- Superseded by: None.
- Authoritative sources: `PROTOCOL.md`; `RESULTS.md`.

### C-2: genuine scalar MSE reduction on the plus orbit

- Statement: On the deterministic exchange-symmetric orbit \(f_1=f_2=g\), the genuine two-example MSE obeys \(\dot g=2\eta(1-g)K_+(g;\rho)\) and \(\dot{\mathcal L}=-4\eta K_+(g;\rho)\mathcal L\), where \(K_+=n\|\nabla g\|^2=(\Theta_{11}+\Theta_{12})/2\).
- Claim-ladder rung: exact conditional reduction.
- Status: Exact-under-assumptions.
- Scope and assumptions: Equal labels, equal input norms, exchange-invariant deterministic width-first/formal trajectory, and the stated average-MSE normalization.
- Supporting evidence: Direct projection of C-1; exchange symmetry; reconstruction of the full initial matrix in `audit_order3.json`.
- Contrary evidence: Finite-width sample fluctuations leave the scalar orbit in general; see C-3.
- Dependencies: C-1 and preservation of the exchange-symmetric orbit in the formal limit.
- Cheapest decisive resolver: Compare the matrix flow on \(f_1=f_2\) with the scalar feature-gradient flow.
- Concrete falsifier: A deterministic exchange-invariant solution starting on \(f_1=f_2\) whose two components acquire different derivatives.
- Supersedes: Any interpretation of \(K_+\) as a surrogate loss kernel disconnected from the MSE.
- Superseded by: None.
- Authoritative sources: `PROTOCOL.md`; `RESULTS.md`; `audit_order3.json`.

### C-3: no generic finite-width scalar closure

- Statement: The claim that the plus-channel scalar equation alone exactly describes a generic finite random network trained on the two examples is false.
- Claim-ladder rung: exact scope limitation.
- Status: Falsified, for the blanket claim of generic finite-width scalar closure.
- Scope and assumptions: Generic finite random initialization with distinct inputs and no enforced parameter symmetrization.
- Supporting evidence: Generically \(f_1\ne f_2\) and the two rows of \(\Theta\) need not be exchange-identical in a realization, so C-1 does not close on \(g\) alone.
- Contrary evidence: Special symmetrized finite networks can remain in the plus subspace; this does not establish a generic claim.
- Dependencies: C-1.
- Cheapest decisive resolver: Evaluate \(f_1-f_2\) and the row sums of \(\Theta\) for one generic finite initialization.
- Concrete falsifier: A proof that every finite realization under the protocol has \(f_1=f_2\) and equal kernel row sums for all time.
- Supersedes: None.
- Superseded by: None.
- Authoritative sources: `RESULTS.md` claim boundary.

### C-4: exact fixed-order feature jets

- Statement: For the frozen raw-cubic, two-hidden-layer, two-input plus-channel protocol,
  \(F_+^{(0)}(0)=F_+^{(2)}(0)=F_+^{(4)}(0)=0\), while \(F_+^{(1)}(0;\rho)\), \(F_+^{(3)}(0;\rho)\), and \(F_+^{(5)}(0;\rho)\) are the exact polynomials recorded in `results_symbolic_order5.json`.  The lower two retain the factorizations \(F_+'(0)=\tfrac{81}{2}(1+\rho)A(\rho)\) and \(F_+^{(3)}(0)=39366(1+\rho)^2P(\rho)\).
- Claim-ladder rung: exact formal coefficient computation.
- Status: Exact-under-assumptions.
- Scope and assumptions: Width first at fixed derivative order, accepted Gaussian-program/detransposition formalism, raw cubic activation in both hidden layers, all blocks trained, unit-RMS Gram matrix \(Q(\rho)\), and plus generator \(n\nabla g\cdot\nabla\).
- Supporting evidence: Exact agreement of ordinary-Taylor and derivative-normalized Gaussian-program assemblers through order five; coefficient-for-coefficient agreement with the independent connected-tree compiler; agreement of two terminal contraction algorithms on all 10,217 color-quotiented order-five terminal keys; independent contracted-GNF matches through order three at five unused rational correlations; fixed-correlation, parity, exchange, endpoint, direct-gradient, normalization, and source-hash gates.
- Contrary evidence: None within the frozen scope.
- Dependencies: Correctness of the fixed-order Gaussian-program limit formalism.
- Cheapest decisive resolver: Re-run the connected-tree order-five audit; optionally rerun both slower Gaussian-program routes for full three-route reproduction.
- Concrete falsifier: One exact rational correlation at which a correctly specified independent calculation disagrees.
- Supersedes: The unvalidated pre-audit recurrence described in U-1.
- Superseded by: None.
- Authoritative sources: `results_symbolic_order5.json`; `ORDER5_SYMBOLIC_RESULTS.md`; `audit_symbolic_order5.json`; `two_input_cubic_plus_jet.py`; `two_input_cubic_connected.cpp`; `audit_symbolic_order5.py`; and the earlier order-three audit artifacts.

### C-5: local output-coordinate kernel and positivity

- Statement: For \(-1<\rho\le1\), \(K_+(0)=\tfrac{81}{2}(1+\rho)A(\rho)>0\), \(K_+'(0)=0\), and \(K_+''(0)=24P(\rho)/A(\rho)^2>0\).
- Claim-ladder rung: exact local consequence of C-4.
- Status: Exact-under-assumptions.
- Scope and assumptions: Nondegenerate plus channel; local formal inverse of \(F_+\).  At \(\rho=-1\), the plus feature vanishes and the output-coordinate inverse is undefined.
- Supporting evidence: Formal inverse-function differentiation and exact Sturm counts showing no roots of \(A\) or \(P\) on \([-1,1]\), together with positive endpoint values.
- Contrary evidence: None.
- Dependencies: C-4 and \(F_+'(0)\ne0\).
- Cheapest decisive resolver: Re-run `audit_two_input_cubic_plus.py`.
- Concrete falsifier: A root or nonpositive value of \(A\) or \(P\) in the certified interval, or an exact jet disagreement.
- Supersedes: None.
- Superseded by: None.
- Authoritative sources: `audit_order3.json`; `RESULTS.md`.

### C-6: positive-time and global conclusions

- Statement: The present local derivative calculation does not establish positive-time width-limit existence, self-averaging, global invertibility, or scalar closure off the plus orbit.
- Claim-ladder rung: theorem obligation.
- Status: Open.
- Scope and assumptions: Any claim beyond the fixed-order local formal jet.
- Supporting evidence: These bridges are not part of the protocol or the exact coefficient audits.
- Contrary evidence: None; local success is not evidence of failure, but it does not prove the bridges.
- Dependencies: Uniform-in-order or positive-time control and the full matrix evolution.
- Cheapest decisive resolver: A rigorous positive-time limit theorem with symmetry preservation, followed by a global/nonlocal analysis.
- Concrete falsifier: A complete proof of all stated bridges under the frozen model assumptions.
- Supersedes: None.
- Superseded by: None.
- Authoritative sources: `PROTOCOL.md`; `RESULTS.md`.

### C-7: order-five Stieltjes moment signs over correlation

- Statement: With \(K_+(y;\rho)=F_+'(0;\rho)+\sum_{r\ge0}(-1)^r\mu_r(\rho)y^{2r+2}\), the accepted order-five jet determines \(\mu_0=F_+^{(3)}/(2(F_+')^2)\) and \(\mu_1=(4(F_+^{(3)})^2-F_+'F_+^{(5)})/(24(F_+')^5)\).  Both are strictly positive for every \(-1<\rho\le1\), so \(H_0=[\mu_0]\) and \(H_0^+=[\mu_1]\) are positive definite throughout the nondegenerate Gram interval.
- Claim-ladder rung: exact finite-prefix symbolic sign certificate.
- Status: Exact-under-assumptions.
- Scope and assumptions: C-4, the local output-coordinate inverse, and \(-1<\rho\le1\).  The antipodal endpoint is excluded because the plus feature is identically degenerate there.
- Supporting evidence: Two independent derivations of the moment formulas; exact forced-factor extraction; Sturm sequences with equal endpoint variation counts for the reduced denominator and numerator polynomials; exact checks at \(\rho=0,1/2,1\).
- Contrary evidence: None at the two accessible one-by-one Hankel levels.
- Dependencies: C-4 and nonvanishing of \(F_+'(0;\rho)\).
- Cheapest decisive resolver: Re-run `two_input_cubic_stieltjes_order5.py` and compare its JSON output with `stieltjes_order5_audit.json`.
- Concrete falsifier: An admissible exact correlation where either reduced moment numerator or denominator has the opposite certified sign.
- Supersedes: No earlier two-input cubic Stieltjes conclusion; this is the first such audit.
- Superseded by: None.
- Authoritative sources: `STIELTJES_ORDER5_PROTOCOL.md`; `two_input_cubic_stieltjes_order5.py`; `stieltjes_order5_audit.json`; `results_symbolic_order5.json`.

### Update U-1

- New evidence: Direct differentiation of the bottom parameter block showed that the induced flow is \(\dot U_r=\tfrac92\sum_q Q_{rq}U_q^2R_q\); the source sample \(q\), not target sample \(r\), belongs on the squared activation derivative factor.
- Validity scope: Two-input recurrence before the accepted order-three production run.
- Mechanism affected: Cross-example bottom-layer response.
- Claims upgraded: C-4 became eligible for exact auditing after correction.
- Claims downgraded: The pre-audit target-indexed recurrence was rejected.
- Claims unchanged and why: C-1 and C-2 follow directly from gradient flow and do not depend on this compiler indexing detail.
- Superseded conclusion: Any coefficients from the target-indexed recurrence are non-authoritative; none are used in `results_order3.json`.
- Newly exposed dependency: Multi-input compilers must preserve the source index through the bottom response.
- Authorized next branch, if any: Extend the full matrix-valued jet beyond the plus channel only under a separately frozen protocol.

### Update U-2

- New evidence: Direct exact \(\mathbb Q[\rho]\) computation reached \(F_+^{(5)}(0;\rho)\).  Ordinary-Taylor and derivative-normalized Gaussian-program routes agree coefficient-for-coefficient, and an independently represented connected-tree compiler reproduces the same polynomial.  Two exact terminal evaluators agree on every reached terminal key through order five.  Exact scalar specializations at \(\rho=0,1/2,1\) and the one-input \(\rho=1\) endpoint also agree.
- Validity scope: The frozen two-input, equal-label, unit-RMS, two-hidden-layer raw-cubic plus channel, with the width limit taken first at each fixed derivative order.
- Mechanism affected: Higher local deformation of the genuine MSE plus-channel kernel; \(F_+^{(5)}\) determines \(K_+^{(4)}(0)=(F_+'F_+^{(5)}-4(F_+^{(3)})^2)/(F_+')^5\).
- Claims upgraded: C-4 is extended from order three to order five with a third, structurally independent coefficient route.
- Claims downgraded: None.
- Claims unchanged and why: C-1--C-3 are exact flow/scope statements independent of jet order; C-6 remains open because finite-order local coefficients do not establish positive-time limits or generic scalar closure.
- Inconclusive branches: Fixed-correlation explicit Gaussian-program attempts through order nine exceeded their frozen caps; unquotiented and color-quotiented connected order-seven attempts reached their respective caps.  A final fixed-endpoint order-seven run was stopped after the user relaxed the target.  No partial order-seven or order-nine value is retained.
- Superseded conclusion: Order three is no longer the highest accepted exact symbolic jet; order five is now authoritative.
- Newly exposed dependency: Higher odd orders require a stronger representation or resource-scaling argument; a timeout is not evidence against existence of the derivatives.
- Authorized next branch, if any: None in the present relaxed scope.  Any renewed order-seven campaign requires a newly frozen method and resource contract.

### Update U-3

- New evidence: Exact reversion and triangular composition give \(\mu_0(\rho)=12P(\rho)/A(\rho)^2\) and \(\mu_1(\rho)=N(\rho)/(27(1+\rho)A(\rho)^5)\).  Exact Sturm certificates prove \(A,P,N>0\) on \([-1,1]\).
- Validity scope: The two accessible moment candidates on the nondegenerate plus channel \(-1<\rho\le1\).
- Mechanism affected: Correlation dependence of the first output-kernel Stieltjes signs.
- Claims upgraded: C-7 is established exact-under-assumptions; neither accessible sign varies with correlation.
- Claims downgraded: None.
- Claims unchanged and why: No \(2\times2\) Hankel determinant is available because \(F_+^{(7)}\) and \(\mu_2\) remain unknown; C-6 therefore remains open.
- Superseded conclusion: None.
- Newly exposed dependency: The first discriminating Hankel determinant requires a successful order-seven symbolic computation.
- Authorized next branch, if any: None under the user's lower-order stopping instruction.
