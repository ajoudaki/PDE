# Recovered global L=3 same-label results

## Recovery and coverage

Original directory `/tmp/l3-two-sample-proof-DLuelg` is not readable by this audit identity. It was **not inspected or permission-modified**. Exact historical `fileChange` additions and unified updates are accessible in the read-only database `/home/amir/.codex/thread_history_1.sqlite`. Replaying those recorded text changes, without mathematical edits, recovered the files under `expanded_sources/OLDER_TWO_SAMPLE_RECOVERED/l3-two-sample-proof-DLuelg/`. The index and manifest record each original path, owner task/turn, ordinal, recovered hash, and any failed chain. The owning historical task for the root files is `01a07192-e207-7ab2-8b41-d34600659e7e`.

Read completely for the same-label theorem: `EXACT_TWO_SAMPLE_REDUCTION.md` (376 lines), `TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md` (352), corrected `SAME_LABEL_GLOBAL_ASSEMBLY.md` (358), `SAME_LABEL_NONTRIVIALITY.md` (288), and `SAME_LABEL_ASSEMBLY_REVIEW.md` (576). Read the complete recorded presentation patch between reviewed and corrected assembly. The exact reviewed initial assembly snapshot was separately recovered and hash-matched.

The heavy common-program dependency was also recovered from its own recorded changes as `OLDER_TWO_SAMPLE_RECOVERED/L3_GLOBAL_SELF_CONTAINED_PROOF.md` (1789 lines), matching its cited hash. Read the complete operative Sections 2, 3, 5, and the cited Section 7 tail argument, covering original lines 165–476, 621–791, and 980–1061. Its one-input arctan-specific construction, clock, and nontriviality sections are **not** imported as two-input claims.

For the sech transfer also read the full `SECH_GATE_ACTIVATION_DESIGN.md` (231), `SECH_SAME_LABEL_GLOBAL_TRANSFER.md` (119), and `SECH_SAME_LABEL_GLOBAL_TRANSFER_REVIEW.md` (613); all operative common dependencies were already read above. The full final L3 `NEXT_PROOF_OBLIGATION.md` was read to check supersession and later scope. It says both same-label global results remain accepted; the opposite-label global theorem remains open after later softplus local work.

## SL1: fixed shifted arctangent, global joint population / finite GF / exact raw GD

There are **three hidden layers**, equal width n, exactly two fixed deterministic inputs \(\|x_a\|^2=d\), correlation \(-1\le\rho=x_1^Tx_2/d<1\), and equal labels \((1,1)\) or \((-1,-1)\). No positive separation away from \(\rho=1\) is assumed; constants may depend on the fixed pair. The antipodal endpoint is included. Use the SAME fixed activation \(\phi(z)=1+\arctan(z)/10\) in all hidden layers. It is independent of width, angle, time horizon, mesh, and realized trajectory.

Initialization is mutually independent iid \(W^1_{ij}\sim N(0,1/d)\), \(W^2_{ij},W^3_{ij}\sim N(0,1/n)\), rescaled readout \(W^4_i\sim N(0,n^{-2})\). Preactivations are \(z_a^1=W^1x_a\), \(z_a^\ell=W^\ell h_a^{\ell-1}\). Prediction is \(f_a=n^{-1}(W^4)^Th_a^3\). Loss is the **unaveraged sum** \(\sum_{a=1}^2(f_a-y_a)^2\). All four blocks train under raw metric \((d/n)\|dW^1\|_F^2+\|dW^2\|_F^2+\|dW^3\|_F^2+n^{-1}\|dW^4\|^2\). The certified GD schedule is exactly \(\eta_n=n^{-2}\), on physical clock \(t=k\eta_n\), with linear raw-parameter interpolation and recomputed hidden quantities. Do not silently generalize the certified step schedule.

The proof constructs fixed neuron probability spaces and bounded initial forward actions with their actual adjoints. The autonomous current state contains both raw first-sample fields, both trained bounded operators (with Hilbert–Schmidt increments), and the readout. At \(\rho=-1\), the first fields obey \(Z_2^1=-Z_1^1\) and carry the one-independent-field metric; no inverse singular Gram is used. The population readout starts zero, while the original finite Gaussian readout is controlled as a small perturbation.

The uncut flow exists on feature time \([0,3/2]\). Its label-aligned predictor \(g=y(f_1+f_2)/2\) has \(g'=\|\nabla g\|^2\ge25/36\), hence reaches one by \(s_*\le36/25<3/2\). The clock \(ds/dt=4(1-g)\) reaches \(s_*\) only at infinite physical time. Consequently the population gradient flow exists on **every fixed finite physical horizon**. Uniqueness and reached-state restart compare all bounded-primal integral/strong competitors, including nonsymmetric competitors; no Gaussian-tail or symmetry condition is imposed on competitors. The source does not assert unrestricted local Lipschitzness on arbitrary raw L2 balls or existence from arbitrary initial population laws.

Both actual finite GF and raw GD are compared directly to a common finite clipped reference at the population clock; the finite off-mode residual is explicitly controlled. Thus there is an explicit finite-GF bridge, rather than an inference from the GD theorem. Full-sequence convergence in probability holds on each finite physical horizon, jointly for:

- predictions and summed loss; all entries of all four 2-by-2 raw kernel blocks;
- fixed finite Lipschitz forward/adjoint probe programs using either direction of either hidden operator;
- named uncut backward fields/deltas and hidden preactivation/feature velocities, with second moments and integrated squared norms;
- same-layer joint laws including both samples and any finite time list, uniformly in those time arguments;
- same-layer two-sample preactivation and feature path laws in \(\mathcal W_2(C([0,T];\mathbb R^2))\), with the uniform path norm.

The same-width GD/GF state distance also tends to zero, in first-field RMS/readout RMS plus hidden-operator-norm distance. This does not mean operator-norm convergence between different-width neuron spaces, arbitrary cross-layer pairing, arbitrary unbounded probe path laws, or a limit uniform over the infinite time axis.

## Persistent strong nontriviality, distinct from earlier local-only claims

Every hidden marginal has two unbounded preactivation tails at every finite physical time, so its best-affine feature regression error is strictly positive. On each fixed compact time interval each such error has a positive minimum; uniform empirical second-moment convergence transfers smaller positive lower bounds to finite systems with probability tending to one.

For each hidden layer and both samples, the RMS preactivation velocity and feature velocity are nonzero at **every positive finite physical time**. Every hidden raw parameter block has positive speed there. The readout is also nonzero in speed, by the positive feature floor and positive finite-time clock. These assertions are not pointwise motion of every neuron and do not give a positive lower bound as \(t\to\infty\). Hidden velocities vanish at initialization because the population readout is zero.

There is a separate nonzero leading coefficient at initialization. In feature time, let \(V=(H_1^3+H_2^3)/2\), let \(D_0\) be the initial linearized hidden-forward map, and \(B=D_0^*V_0\). Each hidden block has \(\Gamma_\ell=\|B_\ell\|^2>0\), \(\Gamma=\sum\Gamma_\ell\). Hidden parameter displacement is \(s^2B/2+o(s^2)\). In physical time every sample/layer has feature displacement \(8t^2\phi'(Z_{a,0}^\ell)T_a^\ell+o(t^2)\) with nonzero L2 coefficient. The same-label readout-mode kernel changes by \(16\Gamma t^2+o(t^2)\), and total-mode kernel by \(32\Gamma t^2+o(t^2)\). Thus the total kernel matrix is nonconstant; no assertion says every individual entry must change.

## Exact historical review status

The shifted-arctan result has **one complete isolated modular audit**, not three final standalone-document passes. The reviewer read all of A/N/E/B plus the named common-program dependency sections and supplied a full PASS for construction, restart, actual finite-GF/GD comparison, observations, and nontriviality. No required mathematical correction was found. Two presentation corrections were then incorporated: state exactly the clock's bounded continuous second derivative, and include the completed nontriviality supplement in the dependency/scope list.

Verified hashes:

| Component | SHA256 |
|---|---|
| Reviewed assembly snapshot A | `2ad0d70ec48eb56dc4170c90df1075e02c8d208913e2dd4fcb4f77d2702baa57` |
| Corrected assembly | `510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44` |
| Nontriviality N | `76124a7552d67304a7e43212b4461ca53c9d79a214af80761f6560012bdf48b6` |
| Exact reduction E | `432f98ff185c797901a81f83c72e4217395d0100f0804b0e609b98db83182e60` |
| Short bootstrap B | `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170` |
| Common-program dependency | `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e` |
| Complete assembly review | `c1da5e7575f6e38485b9e26c7df9da6d3b72d1aa433452b04785d4190d02ae08` |

The corrected assembly's hash is not silently substituted for the original arctan review input hash. However, the later sech reviewer independently reread the entire corrected assembly and the exact dependencies.

## SL2: fixed sech-gate bounded activation, same global conclusion

Replace the activation in **all three hidden layers** by the single fixed
\(\phi(z)=1+0.1\arctan(\sinh z)\), whose gate is \(0.1\operatorname{sech}z\). All model, initialization, labels, angle range, GD schedule, physical horizon, state/uniqueness, observation, persistent nonaffinity, every-positive-time motion, and initial nonzero kernel/displacement conclusions above remain valid.

This is a distinct activation theorem, supported by a **separate complete isolated modular PASS**. That reviewer read all seven candidate/dependency files (3513 lines), rechecked hashes, and independently verified the inherited proofs plus the two changed numerical inequalities. There were no required repairs. In particular, no fixed-sign-control premise, tangent-loop result, or positivity of Gaussian response means is imported. The same-label global transfer covers \(\rho=-1\), although a separate prescribed-control sensitivity lemma in the activation-design source only treats \(|\rho|<1\).

Verified transfer hash `f7cfaf82de5ba25a7b8429435366a2919c2c82e15cf132d2525e4b260c602302`; activation eligibility dependency hash `c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24`; full transfer-review hash `66291f85fdd377a472febe98d51c1962a68f6a16f4a6b26ad213e5ae80adf940`.

## Boundaries and supersession

Neither same-label result settles opposite labels, arbitrary real label pairs, deeper L, or one common bounded activation giving the entire generic-angle opposite-label global theorem. The source response bootstrap itself covers both binary label modes on the feature interval, but opposite-label fitting is not shown to occur within that interval. Later general C1,1 local existence does not supersede these global conclusions or their persistent nontriviality. Earlier one-sample shifted-arctan global results are inherited prerequisites/history, not replacements for these genuinely two-sample generic-angle results.
