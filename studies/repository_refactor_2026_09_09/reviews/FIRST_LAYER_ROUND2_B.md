# Independent complete-proof audit

Verdict: **CLEAN**. I found no mathematical correction required for the exact first-layer compact containment theorem in PROOF.md, lines 138–273, under its stated hypotheses. The proof establishes deterministic compact containment over all admissible initial outcomes, the stated Gaussian probability bounds, and the strong consequences along every stipulated Wasserstein-convergent subsequence. This verdict concerns that theorem and its supporting assertions through EOF.

## Inputs and isolation

The complete substantive read scope was exactly:

- `/tmp/pde-first-layer-round2.5KzDckqd/PROOF.md`: all 1,597 lines, through EOF; 66,376 bytes.
- `/tmp/pde-first-layer-round2.5KzDckqd/NOTATION.md`: all 98 lines, through EOF; 5,110 bytes.

SHA-256 hashes of the audited inputs:

```text
02500ea3eee80f9dadd36790a5ccaea6258c06d0c6901564b54417624452ef93  PROOF.md
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  NOTATION.md
```

PROOF.md was read in consecutive, nontruncated blocks 1–400, 401–800, 801–1200, and 1201–1597. NOTATION.md was read in full in one block. No source repositories, studies, previous audits, history, other agents, skill documents, internet resources, or subagents were consulted. No experiments, generators, installations, builds, Git operations, or input edits were performed. This report is the only file created, in a fresh directory returned by `mktemp -d`.

Below, `P` denotes PROOF.md and `N` denotes NOTATION.md. Line ranges refer to these exact inputs. All calculations were checked analytically from their displayed definitions. No additional initial regularity, independence during training, gate lower bound, residual lower bound, or population identification assumption was supplied.

## Audit findings and proof reasons

1. **Canonical normalization and physical time — passed.**

   References: P 3–9, 13–109, 282–308, 407–423; N 10–42, 59–82.

   The prediction is precisely the canonical stored-parameter prediction: the first matrix acts on `x/sqrt(d)`, the middle matrix acts without an additional width factor, and the readout pairing is divided by `n`. The backward fields satisfy `delta = n * partial f / partial z`; residuals enter only through `c = -2r`.

   Differentiating the unhalved sum loss gives the factors `2/(n sqrt(d))`, `2/n`, and `2/n` in its three Euclidean gradients. The raw metric weights are respectively `1/n`, `1`, and `1/n`, so its inverse metric gives block mobilities `n`, `1`, and `n`. This reproduces every equation in (IV.6) and every simultaneous update in (IV.7). In particular, the middle-matrix update carries exactly one explicit factor `1/n`.

   With two samples, the canonical mean loss is half this sum loss. Its flow velocity is half as large, and reproducing a sum-loss GD update requires twice the numerical mean-loss step. The bookkeeping in P 5–9 is consistent with this relation.

   Independently inserting the parameter velocities into the prediction differential produces all three terms of (IV.32): the first has one empirical factor `1/n`, the middle term is the product of two separately normalized pairings, and the readout term has one normalized pairing. The residual equation is `dot r = -2kr`, with no missing sample-average factor.

2. **Actual finite GF, global existence, and query estimates — passed.**

   References: P 291–425.

   The dissipation identity (IV.24) follows from the constant positive raw metric. At fixed finite width and dimension, its integrated action bounds parameter displacement by `sqrt((t-s) L_Sigma(0))`. At a finite terminal time this gives a finite parameter limit. The smooth finite vector field has a local solution from that limit, proving the stated global existence and uniqueness.

   Initially `|r| <= sqrt(2)(B beta + 1)`. Loss monotonicity gives the stated control bound. Integrating the coordinatewise readout update gives `M_F`. The rank-one bound for the middle update gives `A_F`, including its quadratic-in-time term. Operator bounds then give the primal and backward RMS estimates without a coordinate bound on the first matrix or on the first reverse query.

   The product rules for `z^(2)`, `delta^(2)`, and the actual transpose query `q^(1)` are exact. In particular, the derivative of `delta^(2)` is controlled using the readout infinity norm and the second-preactivation RMS velocity. This proves the displayed `D_Z`, `D_delta`, and `D_q` without a higher-moment product assumption. The estimate `sum_a |dot c_a| <= 8 sqrt(2) K_* R_0` follows from `dot c = 4kr` and `||k||_op <= 2K_*`.

3. **GF row work and moment gain — passed.**

   References: P 426–521.

   For each row, let `u_a = c_a q_a`, `e_a = phi'(z_a) u_a`, and `v = Ge`. Direct multiplication gives

   ```text
   |dot W_i^(1)|^2 = e^T G e = u · dot h_i^(1).
   ```

   This identity is nonnegative even for negative or singular correlations. The derivative bound on `u` gives an envelope `upsilon_i` with uniformly bounded empirical second moment. Integration by parts retains both boundary terms and yields `A_i^F <= 2B upsilon_i`.

   Since the eigenvalues of `G` lie in `[0,2]`, `|v|^2 <= 2 e^TGe` and `|v| <= 2 upsilon_i`. These give `integral |v|^2 <= 4B upsilon_i` and `integral |v|^3 <= 8B upsilon_i^2`. The fourth path moment and fourth moment of the time-L2 norm in (IV.42) follow with the displayed constants. The activation velocity is bounded by the preactivation velocity. The argument has no inverse-Gram assumption and no circular use of the moment gain.

4. **Simultaneous raw GD and closed descent — passed.**

   References: P 91–109, 523–641.

   The stopping argument obtains readout and middle-operator bounds through a candidate exit endpoint by summing old-node updates. Convexity carries those bounds through each raw affine segment. It therefore controls the segment before using descent.

   For raw unit tangents, (IV.44) and the full mixed derivative (IV.45) have the correct normalization. The coordinate product in the last term of (IV.45) can cost `sqrt(n)`. In the second prediction derivative, the readout infinity bound makes the product of two second-preactivation directional derivatives cost only `M J_0^2`. Together these give exactly the sufficient bound `F_**(n)` in (IV.46).

   The segment speed is at most `K_c F_*`. Its prediction differential bounds the segment residual by `R+1` under the first step condition. The sum-loss Hessian bound is then `4F_*^2 + 2 sqrt(2)(R+1) F_**(n)`. Taylor's integral formula gives the half-action descent inequality under `eta H_*(n) <= 1`. Induction rules out the candidate exit and establishes the discrete action bound. This reasoning uses simultaneous old-node directions throughout.

5. **GD recomputed fields, node controls, and discrete row work — passed.**

   References: P 643–788.

   The raw segment velocities give the needed derivative bounds for recomputed nonlinear fields. Their continuity across nodes justifies integration to obtain node differences. The three product-difference identities in (IV.52) include the correct new-endpoint factors, and the controlled-field difference uses `c_(k+1)` exactly as stated.

   The envelope includes precisely the nodes `0,...,N-1` that generate cell velocities. Its empirical second moment implies `max_i upsilon_i <= sqrt(n) V_G`. The row Taylor remainder satisfies

   ```text
   |r_i,k^Tay| <= eta^2 upsilon_i a_i,k.
   ```

   Thus `eta max_i upsilon_i <= 1/2` absorbs the error. Summation by parts has both endpoint terms and the full interior difference sum, giving `A_i^G <= 4B upsilon_i`. All three sufficient threshold conditions in (IV.60) depend only on `T, alpha, beta`; none depends on `b_4`, `d`, or `rho`.

   The subsequent moments use the actual held preactivation velocity and the recomputed identity `s = phi'(z) v`. Integrating through a partial terminal cell is justified by bounding with the nonnegative action through the full final node. The cubic constants `16B V_G^2` and fourth-moment constants in (IV.62) check out.

6. **Antiparallel endpoint — passed.**

   References: P 790–850, 1343–1369, 1511–1524.

   Input normalization at `rho=-1` forces `x_2=-x_1`. Linearity and oddness give opposite forward fields and predictions at every raw parameter state. Evenness of `phi'` gives equal backward fields with the actual arbitrary readout still present. Opposite labels then give `c_2=-c_1`, so both `u` and `e` lie in the antisymmetric subspace.

   On that subspace `G` acts by multiplication by two. Consequently `e=(G/4)v` is exact for GF and held-node GD. There is no unobserved nullspace component in the controlled field. This verifies the endpoint use of `D=G/4` without replacing the readout by zero or taking a limit of interior inverse-Gram constants.

   For `e=(b,-b)`, the actual row energy is `4b^2`, and the controlled kernel contribution is `b^2` times the all-ones matrix. Its four-entry sum is `4b^2`; its trace alone would not be the row energy. The proof uses the correct sum.

7. **Strong translations uniformly across all admissible widths — passed.**

   References: P 852–1041.

   The controlled-query shifts and node-gate shifts have RMS bounds proportional to `tau+eta` in GD; the recomputed position shift has a bound proportional to `tau`. The finite-cell counting and the use of a partial final cell preserve these estimates.

   The arctan logarithmic gate derivative has absolute value at most one. The scalar relative-gate inequality (IV.74) follows directly by adding and subtracting the gated control; taking the maximum of the two gate ratios gives the same two-vector inequality. In both allowed correlation cases, `e=Dv`, so the already established cubic velocity moment supplies the cubic moment of `e`. Hölder with exponents 6 and 3 then proves (IV.75) and (IV.76). No cubic moment of the ungated control, or positive lower bound on a gate or residual, is required.

   The activation-velocity shift uses its recomputed gate, giving the separate estimate (IV.77). For GD shifts shorter than one cell, only starting times crossing an internal node contribute. Their measure is at most `T tau/eta`, and the empirical squared jump is at most `4K_z^2`. Combining this estimate with (IV.76) and splitting at `eta=tau^(3/5)` gives a bound proportional to `tau^(2/5)` for the squared space-time shift norm. This is uniform over every admissible GD width and every initial outcome, rather than merely an estimate along widths tending to infinity. GF satisfies the same weaker exponent.

8. **Strong Wasserstein compact containment — passed.**

   References: P 1043–1196.

   The cell-variance identity has the correct factor `1/(2h)`. Integrating the translation bound gives the velocity projection error `(5C_1/7)h^(2/5)`. Absolute continuity gives each polygonal position error at most `4h T K_z^2` after empirical averaging. Keeping all four fields and both samples together therefore gives (IV.84) by an explicit atom-to-projection coupling.

   The tuple fourth moment is bounded by `4(B_path + 2 A_kin^2 + 4B^4)`. Both projections contract the relevant norms. In a fixed finite-dimensional range, moving mass outside radius `R` to zero costs at most `M_4/R^2`; finite position and mass grids then give total boundedness in Wasserstein distance. The uniform projection error transfers this to the complete union of actual GF and admissible GD laws.

   The successive finite transport tables can be glued by the stated interval subdivision construction. Summable RMS coupling costs give an almost surely Cauchy sequence in the complete path space and convergence in mean squared path distance to a measurable limit with finite second moment. This supplies the required subsequential measure limits. Approximating closure points by union points proves compactness of the closure. The auxiliary construction of a compact subset of the path space also has a summable Markov error, and the fourth moment controls quadratic tails.

   This construction preserves all initial outcomes at each included width. At `T=0`, the separate finite-dimensional argument applies and both velocity spaces and all integrated kernel assertions are trivial, as stated.

9. **Gaussian normalization, events, and probability/empirical-law quantifiers — passed.**

   References: P 166–195, 1198–1307, 1553–1597; N 70–82, 90–98.

   The initialization variances are exactly `1`, `1/n`, and `1/n^2` for the stored first matrix, middle matrix, and readout. The readout standard deviation is `1/n`, and the prediction still has its explicit `1/n`. The description of the readout as rescaled in P 63 does not introduce any further scaling into the displayed definitions or calculations.

   Each first-row pair has covariance `G`, with independence across rows. Expanding its Gaussian moments gives `E|z_i(0)|^4=8+4rho^2 <= 12`; the eighth-moment bound is `1680`. Chebyshev at distance one therefore gives the stated `1680/n` bound for exceeding empirical fourth moment 13.

   The two `1/4`-nets have at most `9^n` points each. Replacing both unit test vectors loses at most half the operator norm. Each fixed bilinear form has variance `1/n`, so threshold four yields `2 exp(-(8-2 log 9)n)`. The stored-readout tail at threshold one is `2n exp(-n^2/2)`. Adding the three failure probabilities gives exactly (IV.13).

   Each point of `E_n` satisfies the deterministic hypotheses for both schemes, with the GD threshold understood. Thus common initialization requires only one failure event, while separate initializations admit the stated `2b_n` union bound. The events are independent of the horizon; the compact sets and GD width thresholds may depend on each fixed horizon. The estimates are uniform over deterministic normalized input pairs, and the proof explicitly restricts the compactness argument to a fixed correlation.

   Finite-width dependence on initialization is continuous in the specified strong path topology for both schemes, so the random empirical laws and compact-containment events are measurable. On `E_n`, the whole-tuple quadratic tail is at most `M_4/R^2` and the empirical space-time velocity tail is at most `J^3/R`. These imply precisely the probability statements (IV.91).

   Arbitrarily selected admissible deterministic outcomes need not have a Gaussian limiting initial empirical law. The theorem imposes no such conclusion on them. For the original random initialization, the conclusion is compact containment in probability, with population-neuron expectation distinct from expectation over initialization. The proof correctly makes no expectation-level uniform-integrability claim on bad events and derives no all-width eventual almost-sure assertion from the nonsummable displayed probability bound. Its subsequential conclusions are conditional on the specified Wasserstein convergence and do not identify a unique law or equate GF and GD limits.

10. **Compatibility, actual first-row reconstruction, and all strong consequences — passed.**

    References: P 197–273, 1309–1551.

    The integral-defect maps are continuous from `C x L2` to `C`. Uniform convergence of positions and strong L2 convergence of velocities also give continuity of `(z,v) -> phi'(z)v`. All finite atoms satisfy the resulting closed compatibility set. Coupling to the limit makes its expected truncated distance to that set zero, proving every identity in (IV.15), including the endpoint subspace constraints.

    The identities `DGD=D` and `A_row^T A_row=D` verify both the first-row velocity reconstruction and its energy normalization. Integrating the actual row velocity gives the increment formula. The map to increments and velocities is Lipschitz with the stated sufficient squared constant `4||A_row||_op^2`, so the Wasserstein convergence also holds jointly with the original tuple. The orthogonal component of an initial full row is constant and is correctly outside this reconstruction.

    Time averages yield jointly measurable representatives of the population L2 fields. Their integrability justifies the timewise expectation formulas without treating evaluation at a fixed time as a continuous functional on L2.

    In near-optimal couplings, let the RMS tuple error be `epsilon_n`, and let `M_n` and `M` be the coupled velocity second-moment square roots. Then `|M_n-M| <= epsilon_n`, and Cauchy–Schwarz gives

    ```text
    || E|v_n(.)|^2 - E|V(.)|^2 ||_L1 <= epsilon_n (M_n+M).
    ```

    The same calculation applies to activation speed; inserting `D` costs only `||D||_op` for the row energy. This proves convergence of all three speed densities in L1, and hence of their integrals on every fixed measurable time subset. The first raw-matrix speed is normalized by exactly `1/n`.

    With instantaneous GF fields or held-node GD fields, each controlled kernel entry is exactly `G_ab` times the empirical average of `(Dv)_a(Dv)_b`. The quadratic map `v -> G odot [(Dv)(Dv)^T]` has the Frobenius-L1 difference bound in (IV.104), so its expectations converge with error at most `||D||_op^2 epsilon_n(M_n+M)`. This proves full matrix-valued L1 convergence, including every off-diagonal entry and cases with vanishing residual controls. Summing all four entries gives the raw row speed by `DGD=D`.

    These identities retain the stipulated GD node convention. The actual loss derivative within a raw affine GD cell is the cross-pairing in (IV.106), which is distinguished from a node squared speed. The theorem's L1 limit statement and almost-everywhere formula for its representative have their stated, different quantifiers. Finally, the displayed coupling estimates make the observable maps continuous on the compact set of laws, so their joint images have the additional compact containment and probability bound asserted in P 1539–1551.

No correction, counterexample, or missing hypothesis was found in the audited theorem or its supporting proof. The verdict uses the fixed-input, fixed-correlation, fixed-finite-horizon scope stated in the two inputs.
