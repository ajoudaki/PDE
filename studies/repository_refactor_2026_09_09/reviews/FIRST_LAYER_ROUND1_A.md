# Isolated adversarial complete-proof review

Verdict: CORRECTIONS REQUIRED. The supplied document is not CLEAN as written: two notation/type defects require the exact corrections below. I found no further substantive obstruction to the stated first-layer compact-containment result after explicitly interpreting the affected formulas as those corrections prescribe. This is not a certification of a full population theorem.

Reviewed inputs, identified by SHA-256:

- `/tmp/pde-first-layer-isolated.D13ZM6gP/PROOF.md`
  - SHA-256: `d45999fc681e4bf66f95392f04f5940be6d3245d88a9eeea33f066560d665adb`
  - 1,596 lines; 66,319 bytes.
- `/tmp/pde-first-layer-isolated.D13ZM6gP/NOTATION.md`
  - SHA-256: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`
  - 98 lines; 5,110 bytes.

Full-read confirmation: I read PROOF.md lines 1–1596 and NOTATION.md lines 1–98 in full. A truncated part of the combined display was separately reread, including PROOF.md lines 801–850. The review used only these two input files and direct mathematical reasoning. I did not read repository material, skill files, source studies, prior reviews, historical evidence, or other agents' work; did not use the internet or subagents; and ran no experiments, generators, builds, installations, or Git operations. Neither input was edited. The only output artifact is this report in a newly created separate temporary directory.

The audited claim is finite-horizon compact containment in the Wasserstein metric built from strong first-layer position/velocity and activation/activation-velocity coordinates, for the actual two-hidden-layer arctangent network, exact GF, and simultaneous raw-parameter GD with sum-loss step `eta = n^-2`. Both the interior correlations and the stated antiparallel endpoint are included.

## Required corrections

1. **Undefined matrix entries occur in the theorem and exact dynamical identities.**

   Locations in PROOF.md: lines **246, 257, 363, 364, 410, 1472, 1474, and 1487**. These include (IV.19), (IV.20), the explanation following (IV.27), (IV.32), (IV.102), and the estimate following (IV.103).

   Every one of these locations uses `C_{ab}`, but neither permitted file defines such a matrix. The input Gram is `G = X^T X/d`, explicitly defined in (IV.1), and NOTATION.md line 13 fixes that same convention. Other decisive identities already use `G`, including `v = Ge`, `DGD = D`, and the full-matrix map (IV.103).

   Correction: replace **each of these eight occurrences of `C_{ab}` by `G_{ab}`**. Do not globally replace the letter C: the continuous-function spaces and the scalar constants `C_0, C_1` are legitimate and unrelated.

   Effect: as supplied, the controlled kernel and its asserted limit are not defined, and their connection to actual parameter motion has not been stated consistently. This is not an optional choice of another matrix: differentiating `z_a = W^(1)x_a/sqrt(d)` forces the coefficient `x_a^T x_b/d = G_{ab}`. The full-entry speed identity likewise requires that same matrix, since the actual row energy is `e^T G e`.

   An analytic check illustrates why the identification matters. Take GF with `n=d=1`, `x_1=1`, `x_2=-1`, `W^(1)=0`, `W^(2)=W^(3)=1`. At that state `c=(2,-2)`, both first-layer deltas equal one, `e=(2,-2)`, and the actual first-row velocity is four. Thus its squared speed is sixteen. Using `G` gives a controlled matrix with all four entries equal to four, whose sum is sixteen. Substituting an unrelated identity matrix for the undefined symbol would instead give sum eight. This is an illustration of the necessary coefficient, not a counterexample to the intended theorem with `G`.

   No new dynamical estimate is needed for this correction. All subsequent audit statements involving the affected formulas refer explicitly to their corrected `G_{ab}` versions.

2. **The compatibility defect map has an incorrect codomain.**

   Location in PROOF.md: **lines 1321–1324**, specifically line **1323**.

   The text says that `z(t)-z(0)-integral_0^t v(u)du` is a continuous map from `C x L^2` “to `G`.” Here `G` is the fixed two-by-two Gram matrix, not a function space or a codomain with the asserted uniform norm.

   Correction: state that this is a map

   `C([0,T]; R^2) x L^2([0,T]; R^2) -> C([0,T]; R^2)`.

   Effect: this repairs the type of the map used to establish the closed compatibility set. The displayed bound `2||z-z'||_infinity + sqrt(T)||v-v'||_2` already proves continuity into this corrected codomain. No missing nontrivial estimate remains at this location.

## Audit of the proof obligations

The following checks cover the substantive chain, including potential circularity, concentrated rows, singular correlation, small shifts at fixed widths, and the difference between node fields and recomputed fields.

1. **Actual equations, clocks, and global GF — lines 58–109 and 282–425.**

   The prediction has exactly one displayed readout factor `1/n`, the stored readout variance is `n^-2`, and the sum loss has no half factor. Direct differentiation gives the gradients in (IV.23); the raw metric gives block mobilities `(n,1,n)`. Hence `c=-2r`, (IV.6), and the dissipation identity (IV.24) are consistent with the notation contract. The corresponding mean-loss trajectory satisfies `W_mean(t)=W_sum(t/2)`; equal parameter updates require `eta_mean=2 eta_sum`. The proved raw GD step is the stated sum-loss step `n^-2`.

   The finite-width existence argument does not rely on first-layer coordinate boundedness. The action bound gives a Cauchy endpoint in the positive-definite raw metric at each fixed width and dimension; local smooth existence then extends any alleged finite endpoint. The readout infinity bound, middle-matrix operator bound, and transpose-query RMS bound follow without a row supremum estimate. The derivative of the actual transpose query in (IV.30) is controlled because the readout is bounded coordinatewise and the first activation velocity is already RMS-bounded. There is no uncontrolled product of two merely L2 fields at this stage.

2. **GD descent before stopping — lines 523–641.**

   The candidate exit segment has readout and matrix bounds before descent is invoked: they follow by summing updates whose old nodes have residual norm at most `R`. Convexity extends those bounds to the whole segment, including the candidate exit endpoint. The first prediction differential then bounds the residual on the segment; its use does not assume loss decrease there.

   For unit raw tangents, (IV.45) has normalized size at most `2+A sqrt(n)`. In the second prediction derivative, the term containing the product of two second-layer preactivation derivatives is bounded by `M J_0^2`, using the coordinatewise readout bound and ordinary Cauchy–Schwarz. The remaining mixed hidden derivative accounts for the `sqrt(n)` growth. Thus the raw loss Hessian bound really is `O(1+sqrt(n))`, with coefficients independent of first-layer initial coordinates. Both segment conditions vanish at `eta=n^-2`. Taylor descent keeps the candidate endpoint below `R`, closing the induction without circularity. The dissipation inequality concerns node updates and is correctly distinguished from loss differentiation inside the affine cells.

3. **GF row-work gain — lines 426–521.**

   The exact row identity is `|dot W_i^(1)|^2=e_i^T G e_i=u_i dot s_i`. Integration by parts, with both boundary terms, bounds the nonnegative row action by `2B upsilon_i`; the envelope has uniformly bounded empirical second moment because the controlled query has an RMS time-derivative bound. This gain is linear in the envelope, not quadratic.

   The explicit spectrum of `G` gives `|v_i|^2 <= 2|dot W_i^(1)|^2` and `|v_i| <= 2 upsilon_i`. Consequently the space-time cubic velocity moment, the fourth moment of its L2 path norm, and the fourth moment of the position supremum have the constants claimed in (IV.41)–(IV.42). These calculations remain valid for a singular Gram matrix and do not assume coordinatewise query bounds or an empirical fourth moment of the query.

4. **Exact GD row work and the width threshold — lines 643–788.**

   Recomputed queries are continuous across nodes and obey the actual product rules along each raw cell. Their node increments, together with those of the controls, establish (IV.54) before row work is used. The envelope includes precisely the old nodes generating velocities. Its deterministic maximum bound `sqrt(n) V_G` is a consequence of its empirical second moment.

   The arctan Taylor remainder obeys `|r_Tay| <= eta^2 upsilon_i a_{k,i}`. It is absorbed using `eta upsilon_i <= 1/2`, established from `eta=n^-2` and the preceding envelope estimate. Discrete summation by parts supplies the `2B upsilon_i` bound, hence the raw action bound `4B upsilon_i`. There is no transformed-coordinate Euler update here. The estimates are taken through the full last update, so restriction to a partial terminal cell is valid. All three conditions defining `n_0` use only `T, alpha, beta`, as claimed.

5. **The singular endpoint and actual readout — lines 790–850.**

   At `rho=-1`, opposite inputs and odd activations enforce opposite forward fields at every raw parameter state, while the even derivative gives equal deltas and equal transpose queries. Opposite labels then give opposite controls. Thus the controlled fields `u,e`, the preactivations, and their velocities lie in the required antisymmetric subspace even for a nonzero readout and throughout a raw affine GD cell. On this subspace `G` acts by two and `D=G/4` recovers `e=Dv`. This removes the otherwise invisible nullspace component needed for full controlled-kernel reconstruction. The proof does not falsely infer that the initialized prediction or readout is exactly zero.

6. **Relative gate estimate and Hölder exponents — lines 852–998.**

   The bounded logarithmic derivative gives the stated relative gate ratio. Inequality (IV.74) holds for arbitrary signed controlled queries; it divides by neither a residual nor a query. Taking the maximum of the two coordinate ratios yields the same vector bound. Since `e=Dv`, the row-work cubic moment controls the L3 norm of the gated query. The sixth power of the gate ratio is bounded by its square, and the position increment estimate bounds the latter. Hölder with `1/2=1/6+1/3` therefore gives the one-third-power L2 translation estimate, or two-thirds power for its square. The recomputed activation derivative uses its own continuous-position gate, exactly as required for raw GD.

7. **Uniformity over every outcome and every admissible width — lines 1000–1041.**

   The proof does not leave a nonvanishing `eta` term in its final modulus. For `tau<=eta`, the held velocity differs from its shift only near internal nodes, whose total contributing length is at most `T tau/eta`; the empirical squared jump is bounded by `4K_z^2`. Taking the minimum with the gate estimate and splitting at `eta=tau^(3/5)` yields a uniform bound proportional to `tau^(2/5)` for the squared translation norm. This applies to the entire admissible family, including arbitrary outcomes at fixed widths. It does not use a large-width limit followed by an unsupported finite-width compactness claim.

8. **Elementary strong W2 compactness — lines 1043–1196.**

   The cell variance identity yields the `h^(2/5)` velocity projection error. Polygonal interpolation of the actual absolutely continuous positions yields the `h` squared supremum error. The projection coupling keeps all four fields and both samples in the same neuron tuple. The fourth moment in (IV.85) follows from the row-work bounds and controls quadratic tails of the full path norm, not just timewise tails.

   At a fixed mesh, truncation, a finite spatial grid, and a finite grid of mass vectors give total boundedness of the projected laws. The uniform projection error transfers it to all admissible empirical laws. The subsequential-limit construction is explicit: finite transport tables are glued by interval splitting, summable expected increments give an almost-sure limit in the complete path space, and the L2 tail estimate gives W2 convergence to its law. Thus neither a probability-measure compactness theorem nor a general disintegration theorem needs to be assumed.

   In the final closure argument the intermediate approximating measure is finite. The relevant triangle inequality can therefore be obtained by the same elementary gluing: for each positive-mass intermediate atom, take the product of the two normalized endpoint conditional measures and weight it by that atom's mass. This remains valid when either endpoint law is not finite and explains why the finite-measure construction suffices for the stated closure argument. No general conditional-probability construction is needed. The open-cover argument and the separate path-space tightness construction then close the compactness claim. The zero-horizon case is correctly separated.

9. **Gaussian event and probability quantifiers — lines 1198–1307.**

   The initial pair has covariance `G`; its fourth moment is `8+4 rho^2<=12`, and its eighth moment is bounded by `1680`. Independence across first rows gives the stated `1680/n` deviation bound at threshold thirteen. The deterministic sphere net has at most `9^n` points; the two-test-vector approximation costs a factor two, and the fixed bilinear Gaussian variance is `1/n`. Threshold four on the net therefore gives exactly `2 exp(-(8-2 log 9)n)` at operator threshold eight. The readout union bound is `2n exp(-n^2/2)`.

   These estimates apply to fixed deterministic inputs, uniformly in their allowed orientation and dimension, without claiming an event for adaptively chosen inputs. The common good event implies simultaneous GF/GD containment with failure probability `b_n`, and a union bound gives `2b_n` for separate initializations. The deterministic threshold depends on the horizon, while the event itself does not. The measurability argument at each finite width is sufficient. The text correctly distinguishes empirical tails controlled on the good event from expectations over initialization on bad events, and does not infer whole-sequence eventual goodness from a nonsummable bound.

10. **Compatibility and actual raw-row reconstruction — lines 1309–1395.**

    After correction 2, all compatibility maps are continuous in the stated strong tuple topology. The distance-to-the-closed-set argument transfers compatibility and the antiparallel constraints to every W2 limit without pointwise evaluations of arbitrary L2 classes. In either correlation case `DGD=D`, so `A_row^T A_row=D` and the exact raw row velocity is `A_row v`. Integration reconstructs increments. The squared Lipschitz bound `4||A_row||_op^2` is valid for the joint increment/velocity map.

    The endpoint check gives raw speed `|v|^2/2`, consistent with the one actual row and the factor `1/sqrt(d)`. The projection formula isolates the constant initial orthogonal row component; full-row reconstruction is appropriately not asserted from two evaluations alone.

11. **Timewise representatives, no kinetic defect, and the full controlled matrix — lines 1397–1550.**

    Time averaging and a summable-increment subsequence provide measurable representatives of the population L2 fields. The finite second moment justifies the integrated formulas. Under the chosen couplings, the L1 difference of squared-speed expectations is bounded by the L2 coupling error times the sum of the two RMS speeds; this proves convergence of densities, not merely total actions. The fixed quadratic form `D` gives the analogous raw-speed estimate.

    After correction 1, the held-node GD kernel is exactly the expectation of `G odot [(Dv)(Dv)^T]`. The outer-product difference estimate controls the entire matrix in time-integrated Frobenius norm, including off-diagonal entries. Its all-entry sum is `v^T D v`, not its trace. The antiparallel example gives four equal entries and the correct total row energy. This argument neither divides by the controls nor requires their separate convergence. The distinction from a kernel recomputed inside a raw GD cell is preserved throughout.

12. **Scope and limiting quantifiers — theorem and lines 1552–1596.**

    The compact set contains all good deterministic outcomes, rather than one realization selected at each width. The consequences apply along any W2-convergent subsequence, including an interleaving of schemes, without claiming that different subsequences or GF and GD have equal limits. The horizon and correlation are fixed; the inverse-Gram constants are not asserted uniform near a singular endpoint. The population expectations are over the limiting neuron law. No identified population dynamics, full-width convergence, full-layer theorem, or convergence of external expected kinetic energies is required for the target result.

The two required corrections are localized and do not change a rate, width threshold, probability bound, or compactness topology. They must nevertheless be made explicitly before this version can receive a CLEAN verdict. I found no additional counterexample or nontrivial missing proof obligation within the stated scope.
