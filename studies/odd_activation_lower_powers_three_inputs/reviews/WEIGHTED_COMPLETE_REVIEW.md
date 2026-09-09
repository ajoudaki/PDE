# Independent complete review of the square-power candidate

2026-09-07. Verdict: **the frozen candidate establishes the complete original two-input theorem for \(0<e\le c_{\rm poly}\delta^2\), with the stated unchanged explicit prefactor.** In particular it includes \(c_{\rm poly}\delta^3\). The three-input file establishes its stated initialization, obstruction, and conditional-clock results, and correctly leaves the complete three-input theorem open.

This is a review of all four candidate mathematical files and their assembly into the original population/GF/raw-GD theorem. Its special focus is the actual weighted source probes, causal products, enlarged coefficient boxes, signed/current-row comparison, and numerical closure. I read the relevant mathematical source arguments directly, including the power-four propagator/response/supersolution, the power-ten normalized source probes and positive supersolution, the quantitative affine comparison/nonaffinity argument, the original odd theorem and its source/limit and initial-motion companions, and the three-input geometry and scalar differentiability sources. Historical reviews, status/evidence ledgers, and review certificates were not used as evidence. No experiment, proof edit, subagent, or commit was performed.

## 1. Frozen objects and integrity

All four candidate files were read in full. Their SHA-256 values match `CANDIDATE_HASHES.json`:

| Candidate | SHA-256 |
|---|---|
| TWO_INPUT_PROOF.md | `1ec4886b450deafb255c60a3e053d5c7c32ef3c02ad9a2aa41e50f0db7f98e7a` |
| WEIGHTED_AFFINE_AND_CLOSURE.md | `17d8bac86024c2dff6344f95d948c9783ad6f64b2fd12441ea5c953c08387076` |
| SECTOR_RESPONSE.md | `2f2e7e66f4d754fca842ebf9524e605ba846c5e2445fc9792e263c859f62d725` |
| THREE_INPUT_ANALYSIS.md | `87327edbd36e63fc40043e5e41783fa6a2e75a0be148af0e41d82337a5bbd2f9` |

All 30 entries of `DEPENDENCY_HASHES.json`, resolved relative to the parent directory, also match their files. These integrity checks identify the reviewed mathematics; they are not mathematical premises.

Final revision check: equation (6) in `TWO_INPUT_PROOF.md`, line 115, restores the missing backslash in its `qquad` spacing command. Reversing that one formatting correction reproduces the previously reviewed SHA-256 `9412514598d92ae96d59e1101f467f7e3f096a760febae1e6d6e96fa6e22e39c`. The other three candidate files and all 30 dependencies are unchanged. The complete affirmative verdict in this report applies to the final main-file hash displayed above.

## 2. Actual probes and weighted time estimates

The intrinsic normalization is essential and is used correctly:

\[
r=\frac{3}{\sqrt2a^3}M^{-4},\qquad
\lambda=a^3r,\qquad \Delta t_j=\lambda h_j.
\]

The dataset envelope \(24^{1/4}\delta^{-1/8}\) is used only as an upper bound for this intrinsic \(M\). It is not substituted into the identity for \(r\).

The weighted certificate uses the actual independent-root answer/coordinate probes of the old source construction. A pulse first enters a raw update with its own source-time step; the injection cost is evaluated at that time and the output cost at the terminal time. The finite-program width limit at fixed nonzero probe amplitude, followed by the amplitude limit, identifies the expected formal derivative with coefficient and covariance arrays frozen. This retains off-support named directions and singular source laws. No derivative of a covariance square root or unproved exchange of derivative and width limits is introduced.

Combining the two-time raw propagator with the respective local injection/output costs gives the stated normalized affine strict weights: \(F,T\) have \(w(t)^3/w(s)^3\), while \(V,W\) and the middle resolvents' strict parts have \(w(t)^4/w(s)^2\). The bottom and top coordinate probes give the additional complete rows needed by the response calculation. The top-backward probe, rather than a beta-positivity shortcut, supplies \(U_{\rm top}\).

The time integrals follow by splitting at the radial level one and using \(dt\le\sqrt2c^{-3}dc\), with the bounded beta rescaling. In particular the tail bound

\[
\int_s^T w(u)^{-2}\,du\le Cw(s)^{-4}
\]

is available, as are the integrals of \(w,w^2,w^3,w^4\). Positive fine meshes inherit these bounds by uniform Riemann approximation on each fixed compact reference interval; a minimum step is unnecessary.

The \(B_3\) learned-moment term \(Cw(t)w(s)\) is included in both triple products. Expanding \(FL=F+FB_3V\), its second integrand is proportional to \(w(u)^{-2}w(q)^5\); reversing the nonnegative integrations and using the preceding tail bound reduces it to an integral of \(w(q)\). Expanding \(RF=F+VB_3F\), its second integrand is proportional to \(w(u)^{-1}w(q)^4\); integrating \(q\) first again reduces it to an integral of \(w(u)\). Thus the claimed weights

\[
FL\lesssim w(t)^3/w(s)^2,\qquad
RF\lesssim w(t)^4/w(s)^3
\]

retain both the current identities and the full learned memory.

## 3. Enlarged boxes and the resolved density issue

The active radius \(H^{-100}M^3\) becomes \(O(rH^{-100}M^3)\) in normalized backward rows. The weighted Neumann ratios are bounded by this quantity times a fixed numerical coefficient and \(\log(\exp(1)30M)\), hence are uniformly small. The separate inactive radius \(H^{-100}M^{-4}\) controls its \(O(M^4)\) integration duration. The top transfers depend only on the forward coefficient majorant. These facts give the complete rows and forward strict densities actually required by `SECTOR_RESPONSE.md`.

An early version asserted nonlinear strict-density persistence for \(R_1-I\) and \(R_2-I\). That assertion was unjustified for arbitrary backward row errors: the term \(V_bJ_3\) in a forward-resolvent perturbation need not carry the final source-column step. For example, a row error concentrated from a later time into an arbitrarily short earlier column makes division by that earlier step unbounded.

**This issue is resolved in the frozen file.** Section 1 now explicitly excludes those nonlinear strict-density claims, and Section 3 delivers only the required complete rows for these resolvents. The response table does not use the removed assertion. The nonlinear \(L_2\) estimate is separately legitimate because its one-sided identity ends in the strict factor \(V^*\). The affine strict estimates used in the \(FL/RF\) products remain valid.

## 4. Signed supersolution and numerical criterion

The exact reconstruction

\[
W^*-W_b=a^2L_bJ_3R^*
\]

is preserved. Its backward factors include their current identities. For arbitrary nonnegative causal \(J_2,J_3\), the strict right factors in the three relevant sandwiches preserve \(h_j\), even when the forcing has a current diagonal or is concentrated in a past column.

The normalized \(FJ_2F\) and \((FL)J_3(R^*F)\) estimates have an additional \(rJ_i\) factor. Conversion of a forward strict density back to original time adds \(O(r^2)\), yielding the stated \(M^{-9}J_2\) and \(M^{-9}\log(\exp(1)30M)J_3\) bounds. The \(VJ_3V\) term has terminal weight \(w(t)^4\); its larger relative error explains the \(M^3J_3^+\) charge. That term has not been discarded.

After the positive affine lower bounds and beta slack are included, the sufficient typed criterion is

\[
\mathcal D=M^{10}(E_2^++E_3^+)+MJ_2^++M^3J_3^+
+E_2^-+E_3^-+M^4(J_2^-+J_3^-)\le H^{-200}.
\]

Backward reconstruction is then strictly inside the active radius, and the triangular inactive construction is strictly inside both inactive margins. The active forward beta gap remains a positive multiple of \(M^{-10}h_j\) at every strict entry. The finite chronological comparison applies to signed actual coefficients through the positive causal majorant, rather than positivity of the nonlinear coefficients themselves.

## 5. Source response and complete exponent count

The weighted raw comparison differentiates only the affine field and gives \(E(t)\lesssim(e/\lambda)w(t)^3\) on the established radius-one tube. Oddness of the active arctangent combination retains the factors \(r\) in the first two active feature comparisons. The resulting active learned forward densities have the claimed smaller orders. Backward learned rows use the weighted time integrals; inactive backward moments start quadratically in \(e\), since their affine fields vanish.

The Gaussian source scales are obtained from actual raw/source \(L^2\) laws, not from a claim that bounded actions preserve Gaussian tails. Solving the exact value equations with deterministic sector-diagonal coefficient arrays gives incoming subGaussian powers \(M^{10},M^9,M^7\). Random gates remain full two-by-two matrices.

The derivative identities retain \(a\Delta V B\), \(aB\Delta G\), the quadratic gate term, terminal feature gates, and all current returns. The rank-one two-sector majorant bounds the off-diagonal derivative generation. A return into the starting sector pays a second perturbative gate. The cross contributions have the displayed orders \(e^2M^{18},e^2M^{20}\) for active forward forcing and \(e^2M^{19},e^2M^{17}\) for inactive backward forcing. Under \(eH^{200}M^{16}\le1\), their reductions fit the stated forcing table. Single-curvature contributions use the actual raw \(L^2\) bounds only after the exponential moments have been controlled; products containing the cross clock use the available higher source moments.

The numerical ledger also preserves the \(H^{40}\) outer transfer cost. In particular the subGaussian coefficient \(H^{94}\) and exponential rate \(H^{81}\) cost \(H^{175}\) before fixed factors, within the \(H^{200}\) condition. Cross terms bounded by \(H^{350}e^2\) reduce to \(H^{150}e\) after that condition. No saturated \(H^{40}\) is silently replaced by \(H\).

The eight contributions to \(\mathcal D\) have powers \(13,15,16,15,13,11,7,5\), respectively, times at most \(H^{200}e\). Therefore

\[
\mathcal D\le8H^{200}eM^{16}
\le8\cdot24^4\cdot10^{-70}H^{-200}<H^{-200}.
\]

Here \(M^{16}\le24^4\delta^{-2}\). Keeping \(24^4\) explicit is sufficient to preserve exactly the old prefactor \(10^{-70}H^{-400}\). The same choice implies the source moment condition and the old primal/nonaffinity condition \(e\le c_*\delta^{7/4}\). The amplitude homotopy therefore closes with strict margins at every fixed cap and sufficiently fine fixed mesh.

## 6. Entire original theorem scope

The new estimates supply the old bridges' actual inputs: bounded capped primal paths through the common feature endpoint, cap/mesh-uniform incoming Gaussian tails, and endpoint prediction at least \(5/4\). Consequently the complete conclusion includes:

- An autonomous uncut global strong population flow on the canonical generated action spaces, with actual adjoints and Hilbert--Schmidt learned increments.
- Uniqueness against nonsymmetric bounded-primal strong competitors and restart from every reached state. The physical comparison retains each actual residual and uses tails only of the reference.
- Joint convergence in probability along the full width sequence for GF and the prescribed simultaneous raw GD with step \(n^{-2}\), retaining the finite initialized Gaussian readout. Width, auxiliary mesh, and cap limits have their original order; no increasing-transcript Gaussian law or trained operator-norm identification is introduced.
- All four full sample kernel matrices, prediction and loss limits, both action orientations on generated probes, same-layer two-sample preactivation/feature path laws, velocity laws uniformly in time and jointly at fixed finite collections of times, second moments, and integrated squared speeds.
- The original velocity product-query truncation and the order of cap removal at fixed reference-velocity truncation. The uncut velocity's compact continuous \(L^2\) time image supplies uniform tails; a cap-dependent higher-moment bound is not used to remove caps.
- Positive activation-regression error at every finite physical time, with the transferred absolute Gaussian margin, and the original nonzero initial hidden-block/sample/layer acceleration and projected-kernel-change statements. The original uncut radial argument also retains the stated physical loss-decay bound.

The scalar physical clock is applied to the constructed symmetric population paths, including separate capped references. It is not applied to finite-width trajectories or assumed for competing nonsymmetric solutions. The normalized identity-perturbation activation family remains within the established gain rectangle. No new restriction depends on physical horizon.

## 7. Three-input claims and final boundary

The three-input cubic lifting argument gives the stated positive initialization Gram, including singular input Grams. The sharp worst-case \(e^2\delta^2\) scale is restricted to the stated small-separation range and is supported by the planar construction in the direct geometry source.

The exact Gram-null identity for the three-layer odd network proves the fitted-state lower bound \(R\ge(\pi e)^{-1/3}-11\), and the fitting-time lower bound follows conditionally from the true gradient-flow energy identity. The equilateral affine stationarity example is an obstruction to an affine reference, not a counterexample at positive \(e\).

The nonlinear scalar-clock lemma is correct under its stated strong-existence and scalar chain-rule assumptions. Its calculation of \(q'= (J'-J^2/\|C\|^2)/\|C\|\ge0\) supplies the conditional hitting/path bounds. The direct source verifies scalar Fréchet differentiability without assuming Fréchet differentiability of the vector-valued Nemytskii map on all of \(L^2\). A bounded strong endpoint is explicitly not promoted to infinite-dimensional local existence. The note also correctly separates this symmetric clock from generic three-residual dynamics.

Thus the two-input square-power result is complete on the frozen mathematical chain. Exponent optimality, a practical-size prefactor, and the full three-input odd-mixture population/GF/raw-GD theorem remain unproved, as the candidate states. There is no unresolved blocking objection to the claims actually made.
