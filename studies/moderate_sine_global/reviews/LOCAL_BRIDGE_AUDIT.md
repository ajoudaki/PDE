# Independent audit of the local moderate-sine observable bridge

Verdict: **PASS for the local bridge invocation; no required mathematical repair found.** This does not certify a global theorem. The source note itself correctly leaves global continuation open.

Audited candidate: `/tmp/sine_source_route.md`, SHA256 `4bfa60f57e8a226ed73ae85c225f28a17562f26b1aa498351e3617069c94be1e`.

Dependencies inspected:

- `studies/mean_field_peeling/two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md`, SHA256 `a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0`: all sections read; the initially truncated product-query passage was re-read in full.
- `studies/mean_field_peeling/two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, SHA256 `99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066`: Sections 1--4 through the path-space/velocity conclusion read in full.
- The exact two-sample raw source and derivative recursions were independently read earlier during this task. No historical review verdict was used as a premise.

## 1. Fixed-cap hypotheses really do apply to Phi

The fixed-cap velocity proof is written using offset arctangent, but the proof uses the following analytic facts only: linear growth of the forward activation; bounded continuous first two activation derivatives; linear growth of the backward gate in its incoming field; and bounded continuous first derivatives of that gate at fixed cap.

For the current candidate,

`Phi(z)=alpha z+beta sin(2z)`,

`D_R(z,q)=alpha q+2 beta cos(2z) tau_R(q)`,

these facts hold exactly. In particular `|D_R|<=2|q|`, `|partial_q D_R|<=2`, and `|partial_z D_R|<=2|q|`. Separately, `|partial_z D_R|=4 beta |sin(2z)| |tau_R(q)|<=8 beta R<4R`. The retained affine term has zero z derivative. No third derivative bound is needed by the fixed-cap bridge.

The forward and raw update maps on bounded primal sets are bounded and Lipschitz at fixed R, including both individual residuals. Matrix differences are controlled by HS norm, and each initial action is used only as a bounded L2 action. This verifies the raw-Lipschitz premise of that bridge without a width-dependent constant.

The fixed-program/common-action premise applies because these are globally Lipschitz C1 coordinate instructions with bounded derivatives. The small finite initial readout is retained until taking each fixed finite-program width limit, exactly as the existing contract requires. No Gaussian identification for a transcript whose length grows with width is invoked.

## 2. Velocity observations require more than the original primary program, but the dependency proves it

The source note's local estimates (14)--(17) are not, by themselves, a claim that arbitrary unbounded-derivative velocity products satisfy the original fixed-program theorem. The named fixed-cap velocity bridge supplies the additional argument needed:

1. At fixed R, a Gaussian probe and raw Lipschitz stability bound the signed expected source-response rows, with the strict source-time factor h_j for past entries. These constants may depend on R.
2. The all-index causal recurrence bounds the full pathwise primary derivative rows at fixed R. This step explicitly distinguishes `sum |E partial F|` from `E sum |partial F|`.
3. The observational input `Phi'(Z)P` is first replaced by `Phi'(Z) tau_M(P)`. Its derivatives are bounded for fixed M. The two new forward matrix queries are then appended after the primary transcript.
4. The derivative identity for that clipped observational input is dominated by `||Phi''||_infinity |P| R(Z)+||Phi'||_infinity R(P)`. The fixed-cap primary derivative/moment bounds make this integrable. Dominated convergence removes the observational clip and identifies the expected-response correction, not just the marginal action output.
5. The second hidden-velocity query is treated only after the first query and its relevant transpose-source derivative rows have been identified.

All five steps remain valid with the sine formulas. Thus the stronger fixed-cap derivative and velocity moment bounds are proved within the cited bridge. They are not missing cap-independent assumptions to be added to the local source note.

## 3. Cap removal does not need cap-independent velocity moments

This distinction is essential and is handled correctly by the cited continuation bridge.

The new local source bounds give cap- and mesh-independent Gaussian tails for the three incoming fields. The asymmetric gate comparison then gives a strong raw-state discrepancy `C exp(CR-cR^2)`. The same estimate for the vector fields gives strong raw-direction convergence as well.

On the resulting uncut population path the chain rule gives continuous L2 preactivation/feature velocities. Their compact L2 time image has uniformly vanishing tail norms, without any claimed uniform Gaussian velocity constant. Apply the deterministic hidden-velocity comparison with this uncut population velocity as reference, first at fixed observational threshold M and then send M to infinity. This proves strong convergence of population cap velocities to the uncut velocities.

For actual finite uncut GF or raw GD versus its same-width cap reference, the correct order is:

- fix R and M;
- take width to infinity, using the fixed-cap empirical velocity law and tail convergence;
- send R to infinity at fixed M, using population cap-velocity convergence;
- finally send M to infinity.

There is no product of an uncontrolled cap-dependent velocity moment constant with the cap-removal error. Therefore local estimates (14)--(17) need not be strengthened into cap-independent velocity-response or fourth-moment bounds.

The raw-GD comparison keeps its actual preceding-node raw direction and the small `C_{R,T} n^{-2}` error. Right node velocities and terminal-left velocities are included. The actual finite residuals remain separate throughout; the population clock is not applied to finite networks.

## 4. Path-space W2 and the physical interval

Once joint finite-time W2 laws and the hidden velocities have been identified, the dependency's deterministic inequality

`||x-I_h x||_infinity^2 <=4h integral_0^T |x'|^2`

gives the required path-space W2 approximation. The raw bounded-primal directions bound the average squared hidden speeds through the forward product rules. This argument applies to recomputed hidden fields along raw GD interpolation and does not confuse bounded second moments alone with W2 tightness.

For the local physical clock, the source bound `|g_R|<=1/4` gives `3/2<=ds/dt<=5/2`. Hence for `0<=t<=S_0/3`, the feature time is at most `5S_0/6<S_0`. The same conclusion holds for the uncut reference. This is sufficient to apply the fixed-cap physical bridge on that common interval. Odd Phi and odd tau_R preserve the sample/label symmetry used for this scalar population clock. They do not imply exact finite-width symmetry, which the bridge never assumes.

This confirms only `[0,S_0/3]` and restart uniqueness within the already-constructed interval. It gives no generic local existence theorem at a new arbitrary L2 endpoint and no all-finite-time extension.

## 5. Additional checks on the local envelope

I also checked the following portions of Section 3 independently; a separate reviewer is checking the complete local bootstrap.

- On the stated coefficient box, the three value recursions have deterministic Volterra coefficients of order `M_2 S`, `A_2 M_3 S`, or `A_3 S`. The restriction `S^2<=1/(10000 D A^2)` makes their accumulated coefficients small, so the `10D sqrt(p)` bound and the reverse-field `O(S sqrt(p))` bounds are consistent.
- For a forward-source derivative row the direct source contributes exactly one. Substitution of the current backward row adds only known forward derivative rows. The curvature contribution is evaluated at the same past time that carries its h_r factor, so the envelope does not require the supremum of a Gaussian process over time.
- The middle recurrence is majorized by coefficients `2A_2 |q_r^2|+L^2 A_2 M_3 S`; the bottom by `2|q_r^1|+L^2 M_2 S`; and the top by `2A_3 |C_r|+L^2 A_3 S`. Each is dominated after integration by the exponent in (14).
- The moment estimate used in (15) is valid: `||Q||_p<=K sqrt(p)` implies `E exp(Q^2/(4eK^2))<=2`, and then `E exp(u|Q|)<=2 exp(eK^2u^2)` by completing the square. Jensen with time weights is legitimate and does not assume time independence.
- With `K=21 D A S`, the fourth envelope moment has the displayed factor `168 D A^2 S^2`. The last restriction in (10) makes this at most 0.0168. The claimed bound `E E_k^4<16`, and hence `||E_k||_4<2`, has substantial slack.
- The current curvature terms in (16)--(18) remain present and are controlled by Cauchy--Schwarz using the envelope moment. No current source is discarded or inverted.

No required repair to the Section 4 local GF/GD/path/velocity invocation was found. Its scope should remain explicitly local, and the response/tail continuation gap should remain stated as open.
