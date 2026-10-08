# Audit of the causal population simulator

2026-10-07. Independent bounded implementation audit, with small consistency tests only. No production cohort, dense-comparison output, or empirical agreement claim was used as evidence for correctness.

Complete inputs read:

- `causal_population_simulator.py`, 561 lines, SHA-256 `4431bef401087ca0e0f0bd465f1d31d88e7486403ec18d331eab8bbc035e5d76`.
- `CANDIDATE_CLOSURE_CHECK.md`, the complete finite-program equations and their first-tangent construction, SHA-256 `c00e4fb7a511e972831e59b6f523581955cee1f0007201ce7f24dbd77684171d`.

No source code was modified. This report is about the supplied two-training/one-passive, two-hidden-layer tanh implementation, not arbitrary depth or a continuous-time solver.

## Verdict

The intended finite-Euler primal equations, learned-memory orientations, frozen-coefficient tangents, and active-only tangent-coordinate reduction check out. No mathematical implementation correction was found in those parts. The bundled small tests passed, and additional small probes confirmed later-time and passive-coordinate responses, including an exactly dependent passive input.

The numerical result is nevertheless a finite-particle, adaptively coupled approximation to the exact population law. Independent random seed streams do not make its entire realized primitive families mutually independent or jointly Gaussian at finite particle count. Its covariance-factor diagnostic is not a bound on population integration error. The source docstring appropriately disclaims convergence rates; comparisons must retain that qualification.

Two output-interpretation refinements are recommended: describe `maximum_covariance_error` as a factor-versus-empirical-query-Gram error, and interpret `kernel_diagnostic_is_gradient_kernel` as identifying the intended full canonical kernel formula, not certifying an exact loss identity for the finite-particle algorithm.

## 1. Active-only tangents: the omitted coordinates really vanish

Write active indices as $b=1,2$ and the passive index as 3. The derivatives here hold every empirical/population coefficient, other primitive coordinate, and covariance factor fixed. They are not derivatives of the complete self-consistent numerical solver with respect to its random seed.

For the intended causal local circuit, induction in the Euler chronology gives

\[
\frac{\partial h_{1,a}^k}{\partial\xi_3^j}=0
\quad\text{for every }a,j,k,
\tag{1}
\]

and

\[
\frac{\partial\delta_{2,a}^k}{\partial\eta_3^j}
=\mathbf1_{\{a=3\}}\mathbf1_{\{j=k\}}
 w^k T''(z_{2,3}^k).
\tag{2}
\]

To see (1), all first-layer updates sum only active backward signals. Each active backward signal has no passive primitive input because active upper fields and the readout have no passive training force. Therefore even the passive lower feature changes only through active backward fields and its fixed input inner products.

For (2), $w^k$ is a sum of strict-past active upper features. An active upper feature uses active primitive coordinates and active backward histories only. A passive upper preactivation uses its own current $\eta_3^k$ plus active backward histories; it has no past passive backward-history term because (1) makes the corresponding $R^h$ columns zero. Hence a passive upper primitive can affect only its own current passive gated backward field, giving (2).

This reasoning holds for nonorthogonal normalized training inputs as well as the displayed orthogonal example. It also holds for the implemented memory/response masks, since those masks do not introduce a passive training force.

The code implements precisely this structure:

- `z1_tangent` retains all three output rows but only active $\xi$ columns. This is necessary to compute the passive feature's responses to active forces.
- Packed lower histories retain active $h_1$ rows only, because all later history sums use active input columns.
- Upper tangents retain all three output rows with respect to active $\eta$ coordinates, while packed upper histories retain active $\delta_2$ rows only.
- The separately assigned `Rd[k,k,2,2]` is exactly the expectation in (2).
- That diagonal is explicitly added to the passive lower carrier. It is not silently discarded with the other passive columns.

The current passive diagonal is especially important for passive backward/kernel diagnostics, even though the passive backward field itself does not drive the first-layer update. In a singular representation such as a passive input identical to an active input, retaining this term also gives the correct observable equality despite different formal coordinate derivatives.

Thus active-only storage is an exact sparsity reduction of the stated frozen-coefficient circuit. It is not an approximation that assumes passive Gaussian coordinates are uncorrelated with active ones.

## 2. Primal chronology, coefficients, and Gram orientation

The effective step is `dt*(2/m)`, with $m=2$. No additional dense-width factor belongs in the history sums after inner products have already been normalized into $C,D$.

`_record_gram` writes

\[
C[k,j,a,b]=\frac1P\sum_i h_a^k(i)h_b^j(i),
\tag{3}
\]

and writes its transpose into $C[j,k,b,a]$. Here $P$ denotes particle count; the code's local variable `n` is not the width of a dense network. The same convention is used for backward Grams. `_flat_gram` correctly converts time/sample pairs to the chronological order used by the Gaussian-family sampler.

The forward coefficient at lines 256–263 is

\[
R^h_{ab}(k,j)+\Delta\frac2m c_b^j C^1_{ab}(k,j),\qquad j<k,
\tag{4}
\]

acting on the past active $\delta_{2,b}^j$. The backward coefficient at lines 291–299 is

\[
R^\delta_{ab}(k,j)+\mathbf1_{\{j<k\}}
\Delta\frac2m c_b^j D^2_{ab}(k,j),\qquad j\leq k,
\tag{5}
\]

acting on the past/current active lower feature, with the extra passive diagonal just discussed. Both orientations and the current-versus-strict-past limits are correct.

The lower update uses $S_{ab}c_b^k\delta_{1,b}^k$ with only active $b$. The readout update uses active $c_b^kh_{2,b}^k$. Output evaluation occurs before these updates, so the recorded state at index $k$ is the intended simultaneous Euler state. Stored histories are copied into their own arrays before the evolving state is changed.

The resulting finite-particle output identity

\[
f_a^k=\Delta\frac2m\sum_{j<k,b\leq2}
c_b^j C^2_{ab}(k,j)
\tag{6}
\]

is exact for the numerical readout/history arithmetic, up to floating-point error. Its successful test checks chronology and inner-product orientation; it does not test the accuracy of replacing population expectations by particle averages.

## 3. Tangent propagation and the meaning of its replay tests

At each event the code inserts unit tangents for the newly introduced active primitive coordinates. It then propagates through the full local history using frozen coefficient arrays. The tanh gate formulas are

\[
\partial h=g(z)\partial z,\qquad
\partial\delta=T''(z)b\partial z+g(z)\partial b,
\tag{7}
\]

with $b=w$ at the top. The recorded first tangents implement these formulas, including the readout's dependence on earlier upper features and the lower field's dependence on earlier reverse answers. No differentiation of residuals, $C,D,R$, or Gaussian-factor coefficients occurs.

The coordinate packing is time-major with two active coordinates per time. The reshapes used to construct `Rh` and `Rd` agree with that ordering. Lower feature histories at time $j$ have only $2j$ introduced reverse coordinates; upper backward histories have $2(j+1)$ forward coordinates. The triangular storage sizes and the prefix additions match those causal dimensions.

`replay_frozen_coefficients` is a valid test of the intended response derivative. It reuses every realized primitive field, changes one formal primitive coordinate by a uniform small amount across rows, and keeps the original $c,C,D,R$ arrays fixed. It does not resample or perturb whitened Gaussian seeds. Taking the average central difference therefore tests the average local derivative defining $R$.

It is deliberately not a new self-consistent numerical trajectory. Recomputing moments/residuals after a probe would test a different derivative. Likewise, changing an initial Gaussian innovation and letting the covariance sampling map propagate that change would not test the formal primitive-coordinate derivative in the source.

The bundled probe checks cover only time zero, active sample zero, plus a passive time-zero noninterference check. They are sensible smoke tests, but the passive time-zero check is weak by itself because the initial readout is zero. The supplementary probes below cover nonzero probe times and the passive current diagonal independently through replay.

## 4. Gaussian-family construction: what is exact and what is approximate

The sampler orthogonalizes source query vectors in the empirical inner product $\langle u,v\rangle_P=u^\top v/P$. Its two projection passes and variance normalization are correct. For retained source directions it draws fresh iid target standard-normal seed columns; it correctly does not empirically orthogonalize those Gaussian target samples.

For a fixed query table independent of the target seeds, the coefficient matrix $L$ represents the retained query Gram and the target table has Gaussian covariance $LL^\top$. Exact dependent queries return the corresponding linear combination of past answers. Zero queries return zero, without artificial diagonal jitter. The tests verify both cases.

For adaptive particle queries, the valid conditional statement is narrower: before a newly retained direction is sampled, its coefficient vector and innovation variance are known from the numerical past and source query. Its new seed column is independent standard Gaussian. Thus that event has the prescribed conditional Gaussian innovation and predictable mean from existing seed columns.

However, the whole estimated coefficient table is random and depends on previous Gaussian samples through the evolving moments and fields. Conditioning on that completed table does not generally leave the past seeds iid Gaussian. The complete primitive path need not be Gaussian, nor are the upper and lower *realized primitive families* independent at finite $P$, even though the three RNG seed streams are independent. For example the empirical upper backward Gram sets the next lower noise scale, already coupling the two families statistically.

A simple algebraic example makes the distinction explicit. Let a first constant query produce iid normals $g_i$. Let a later query be the constant vector with value $a=P^{-1}\sum_i g_i$. A Gram-factor reuse returns $a g_i$. Its mean is $1/P$, so it is not a centered Gaussian field with the realized coefficient-Gram law, despite each fresh seed having been generated correctly. This example illustrates the distinction; it is not a claimed error rate for the present neural algorithm.

The finite-particle computation is therefore a self-consistent numerical approximation to the exact deterministic-population-coefficient system, not an exact independent Monte Carlo sample from that system. This is compatible with the code's explicit no-rate disclaimer. A proof of its particle convergence or independence restoration is not supplied by the sampler identities alone.

### Covariance diagnostics

`maximum_covariance_error` at lines 84–95 compares

\[
LL^\top\quad\hbox{with the stored empirical source query Gram}.
\tag{8}
\]

It correctly diagnoses projection/discarding/floating-point error in that factorization. It does not compare the empirical target-seed covariance with its model covariance, and it does not measure error relative to the true population query Gram. It can be tiny while population quadrature error is appreciable.

Discarded innovation variances, retained rank, and factor-Gram error are all recorded. The relative threshold scales against the current query's raw variance. Thresholding can discard a small direction that later queries use; later retention of a related direction does not retroactively repair all old coefficients. The full factor-Gram error is therefore a useful additional diagnostic, not redundant with the largest single discarded variance. Threshold and population refinements remain separate numerical checks.

## 5. Small tests actually performed

I executed the supplied `--self-test` once. It passed all listed checks: dependent/zero-query sampling; stationary zero-label singular dynamics; replay, output-history identity, diagonal curvature and frozen probes for full/no-reciprocal/no-middle variants; and the pre-allocation memory guard. The test reported about 0.073 seconds internally. No production horizon or dense comparison was run.

I also performed a small independent sweep using $P=24$, three Euler steps, $\Delta=0.2$, seed 29, and labels $(0.15,-0.1)$. For each of the two panels below, both primitive families, all four time indices, and all three sample indices were probed. Central differences of mean $h_1$ for $\xi$ probes and mean $\delta_2$ for $\eta$ probes were compared with every corresponding stored response entry.

| Panel | Maximum absolute response error, probe $10^{-4}$ | Maximum absolute response error, probe $10^{-5}$ |
|---|---:|---:|
| $(1,0),(0.6,0.8),(0.8,-0.6)$ | $1.022\times10^{-10}$ | $1.456\times10^{-12}$ |
| $(1,0),(0,1),(1,0)$, duplicate passive input | $1.391\times10^{-10}$ | $1.456\times10^{-12}$ |

The error decrease is consistent with central-difference truncation until floating-point effects matter. It is a finite-program differentiation check, not a time/population convergence estimate.

For the duplicate-passive panel, passive and corresponding active feature paths agreed to $1.11\times10^{-16}$, and lower backward fields to $8.68\times10^{-18}$. This checks the observable singular-coordinate behavior and the separately retained passive diagonal. The tests compare expected response arrays, not every internal rowwise tangent; they do not certify all horizons or rank-threshold regimes.

## 6. Diagnostic semantics, reproducibility, and minor hardening

The assembled `kernel_diagnostic` is the full canonical formula
$C^2+C^1\circ D^2+S\circ D^1$, evaluated on numerical moments. It is a PSD Gram-based diagnostic. In full mode its formula targets the population gradient kernel, but this alone does not give the adaptive finite-particle update an exact gradient realization or exact loss-dissipation identity. The metadata boolean at lines 376–377 should be read as “targets the full canonical gradient-kernel formula,” not as a theorem about this finite-particle trajectory.

With learned middle memory disabled, the intended frozen-middle physical model has no middle-parameter kernel block. The code still returns the full diagnostic expression and marks the boolean false. Thus that returned expression must not be used as the frozen-middle model's exact loss kernel. The one-direction memory switches and response-off mode are clearly documented as modified circuits, with no guaranteed dense gradient model.

The frozen-feature Euler baseline is correctly computed from the same estimated initial top Gram. Its pseudoinverse endpoint additionally uses a fixed `rcond=1e-12`; that threshold is distinct from the Gaussian-family rank tolerance. Report it if an input panel is nearly degenerate. The baseline is a reference calculated from the particle-estimated initial kernel, not automatically the baseline of a separately initialized dense model.

Minor robustness/provenance recommendations, not failures observed in these small tests:

- Reject nonfinite rank tolerances as well as negative ones. A NaN threshold currently fails the retention comparison and can silently discard every innovation.
- The standalone saved output includes detailed configuration but not a source hash or NumPy version. A surrounding experiment harness may supply these; this audit does not assume it does.
- Standalone `--output` uses `np.savez_compressed` without an existing-file guard. Use unique evidence paths or an explicit guard to avoid overwriting earlier runs.
- Treat the memory estimate as a practical preflight estimate, not a formal upper bound on all temporary BLAS/diagnostic allocations. Very long histories can add transient Gram-sized arrays.
- Do not interpret finite-particle symmetry defects as violations of the exact symmetric population law. Conversely, forcing those defects to zero would change this numerical approximation and should be declared.

## 7. Permitted comparison conclusions

At fixed Euler mesh, the audited code computes a plausible and internally consistent particle approximation to the intended closed finite-history population equations. Dense-Euler agreement can then be assessed with independent width, particle-count, timestep, and rank-tolerance controls. Replicates should be complete particle runs, not interacting rows treated as iid samples from the exact target.

Agreement of a cohort is empirical evidence in its tested regime. It cannot establish an exact finite-particle Gaussian law, a particle convergence rate, a dense-width rate, continuum well-posedness, or an all-time accuracy guarantee. None of those claims was needed to validate the active-only derivative reduction or the finite-Euler indexing checked here.
