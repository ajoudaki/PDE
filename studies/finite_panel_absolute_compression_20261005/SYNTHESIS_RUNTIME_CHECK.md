# Runtime check of the finite-panel synthesis

2026-10-05. **PASS for the stated inherited-interface theorem.** No
blocking mathematical defect was found in the autonomous equations,
comparison transfer, full-time endpoint argument, panel variability
comparison, full label allowance, or retained-storage count.

This is an internal check by the author of `PANEL_RUNTIME.md`, not an
independent promotion review. The verdict binds to the complete
`RESULT.md` with SHA-256
`38ca06a2e812d8e2b45c6b7350c0437d710433b11a00b89aa66487a9229b028b`.
The complete final file was read. Its earlier reviewed version was
`4e6d7baa5fa8c0960a462b4270374b8a9181a0d7a5834dc553089a8fb81246a4`;
the final version clarifies the core moving-state count and explicitly
lists the already inherited moment gate. Both changes were verified.
The check used the frozen runtime route and
its authorized integrated sources; no other current route report was
read. No experiment, established-book change or Git-index mutation was
performed. The inherited insertion, selection, coefficient compilation,
and variability inputs were not independently reproved.

## Exact optimizer and passive chains

Let \(H\) denote the selected top training-feature matrix and
\(G=H^TM_LH\). The corrected readout in result (14) obeys
\[
H^TM_L\widehat w_C
=H^TM_Lw_C+GG^{-1}(y-c-H^TM_Lw_C)=y-c.
\]
Thus the independently stored \(c\in\mathbb R^m\) remains exactly
labels minus training predictions. The only inverse is the training
Gram; singularity or duplication in the passive panel introduces no
new inverse or gap assumption.

The update equations (15) have the unchanged factor \(2/m\), metric
rank-one hidden directions, raw readout update, and residual equation
\(\dot c=-2Kc/m\). Each term in \(K\) is the Gram of the corresponding
specified update block. For example, the Hilbert--Schmidt inner product
between two blocks \(\delta_a h_a^TM_{j-1}\) and
\(\delta_b h_b^TM_{j-1}\), as maps between the metric neuron spaces,
is
\(\langle\delta_a,\delta_b\rangle_{M_j}
\langle h_a,h_b\rangle_{M_{j-1}}\). Consequently
\[
\|\dot\theta_C\|_{\rm par}^2=4c^TKc/m^2
=-\frac d{dt}\bigl(\|c\|_2^2/m\bigr).
\]
This identity does not require coordinate gates to be self-adjoint in
\(M_j\), and the result correctly avoids identifying the optimizer
with ordinary gradient flow of the corrected predictor.

The passive chain (16) is the derivative of the current forward
recurrence. Define its consistency errors by
\(z_i^1-A_Cv_i\) and \(z_i^j-B_C^jh_i^{j-1}\). Their derivatives
are zero under (16), and their initial values are zero. Therefore the
passive chain equals recomputation at every time on the unique continued
solution. It has no label or residual and never contributes to (15).
Its endpoint follows from convergence of the trained arrays and
continuity of the forward recurrence. Restartability is on this natural
consistent state manifold.

The headline moving-state formula (4) explicitly counts the core
parameter and residual arrays. If passive preactivations are instead
retained as additional ODE state, the exact count acquires
\((p-m)\sum_jq_j\) coordinates. The final result expressly includes
these in its complete storage count (5), not in the core formula (4).
The simultaneous-buffer calculation below verifies this distinction.

## Polynomial comparison and all-time endpoint

The source interface contains forward features at every declared point,
their initialized forward images, and training backward responses and
reverse images. Source isometry and paired images therefore control
training/training and training/passive feature pairings at different
times, which is exactly what the learned forward action and the selected
dense readout need. A passive label, passive Gram inverse, passive
reverse update, or passive carrier maximum is never used.

For the actual training feature map \(V_C=H/\sqrt m\), its normalized
Gram \(Q_C=V_C^*V_C\), and right inverse \(T_C=V_CQ_C^{-1}\), the
comparison lifts normalized residual error \(e\) to \(T_Ce\).
The identity \(T_CQ_C=V_C\) cancels the leading residual term in
the raw readout error exactly. The energy-scale selected dense readout
and velocity bounds are inherited from the same fixed source spaces;
they do not incur a passive-panel factor.

All subsequent backward subtractions and carrier-coordinate bounds
involve training indices only. A maximum over the finite panel replaces
the old forward query supremum without changing any coefficient.
Therefore the complete common-cap comparison gives exactly result (6),
with numerical constant 10 and \(\beta^{40L}\); the full recurrence
comparison gives result (22), with universal constant, \(\beta^{42L}\),
and the original \((1+\sqrt{\log(en)})e^{32\sqrt{\log(en)}}\) factor.
The result retains both terms of the corrected source forcing through
its import of the full-range comparison.

The independent fitting bounds give integrable output speeds on the
declared inputs. At
\(T=32\log(en)/\lambda\), their true residual decay is at least
\(e^{-16\log(en)}\); the imported \(e^{-8\log(en)}\) tail bound is
conservative. Comparing each model to its own value at \(T\) and then
using the compact/dense difference at \(T\) proves the same-time bound
for every later time. Parameter convergence includes the endpoint.
The runtime continues to evolve after \(T\); no source approximation
after \(T\) or derivative of a source error is assumed.

The real dense fitting input can itself be localized to the supplied
panel: the original initialization proof needs only the \(m^2\)
training Gram entries and \(p\) individual feature norms. Its event
and subsequent stopped fitting argument therefore require no query net.
The optional explicit threshold in `PANEL_RUNTIME.md`, (8a), is valid;
its omission from the synthesis does not make the overall inherited
threshold effective or leave a new logical assumption unstated.

## Full label scope and actual panel discrepancy

Result (21) preserves the original dense/compact/source intersection.
The common-cap simplification is explicitly separated. On the full
interval, the localized time coefficient is
\(\chi=\min(1,a/(4S^2U_{\rm fin}(S)))\), and the imported proof gives
the positive activation/depth-only lower bound \(\chi_{\rm act}\).
No small-label constant is tightened to obtain the deterministic
comparison. The activation class still permits unbounded values.

For \(m\ge2\), the imported lower theorem uses a deterministic training
index. That index belongs to every permitted panel, so its lower bound
holds in exactly the denominator norm of result (18). The ratio is
therefore bounded on the intersected events by a fixed task coefficient
times
\[
n^{-1/2}\log(en)^{5/2}e^{2\sqrt{\log(en)}}
\]
on the common cap, and by the same expression with the full-range
additional logarithmic factor and exponent 32. Each tends to zero.
Choosing the lower event and compression event at half the requested
failure probability proves convergence in probability; they need not
be independent. The statement concerns whole-trajectory norms, not
pointwise relative error or endpoint separation. The result states
these distinctions correctly.

The stated \(m=1\) caveat is correct for the full strip class, which
allows effectively constant final features. If the final presentation
seeks to cover the user's narrower requirement that every activation
be nonconstant, the ratio also extends to \(m=1\): Gaussian full
support gives positive intermediate second moments and
\(\operatorname{Var}(\phi_L(\sqrt{q_{L-1}}Z)^2)>0\). The scalar
innovation and the same finite-query trajectory bridge then supply a
positive lower coefficient. The synthesis's restriction to \(m\ge2\)
is a clearly stated scope qualification, not an invalid lower claim.

## Temporal rank and complete simultaneous-panel storage

For the stated radius, \(r/T=\chi/(32\log(en)^{3/2})\le1/32\).
Thus the time substitution used in Section 2 stays inside the
holomorphic rectangle, including the real overhang. With
\(\alpha=\chi/(128\log(en)^{3/2})\), the chosen degree has tail at
most \(1/(16n)\), leaving room for finite coefficient approximation.
The logarithmic gate in result (20) gives the displayed bound
\(K+1\le6\log(en)/\alpha\). Four families at all \(p\) points are
a valid upper count even though passive backward families are unnecessary.
Their total dimension is at most
\(3072p\chi^{-1}\log(en)^{5/2}\), before the exact initial additions.
The resulting \(R\), widths and ceiling estimates are correct.

For simultaneous passive storage, the eight buffers per point and layer
cost at most \(72LpR\le72LR^2\), since \(q_j\le9R\) and \(p\le R\).
This is safely absorbed by the difference between the inherited
\(1020(L+1)R^2\) inventory and the proposed \(2048(L+1)R^2\)
allowance. The latter also has ample margin for \(O(R)\) output
scratch and the stated \(O(m^2)\) solves. The data allowance
\(16p(d+1)\) exceeds the inherited training data plus passive inputs
and outputs. The fixed evaluator is explicitly additional and must
include its implementation and workspace.

The padding inequality
\(2m+d+2\le3p+2\le5p\) yields
\(R\le3077p\chi^{-1}\log(en)^{5/2}\).
Thus \(9R\le27693p\chi^{-1}\log(en)^{5/2}\), and
\(2048\cdot3077^2<2^{36}\). Both headline constants are safe.
The result explicitly excludes preprocessing workspace from its retained
runtime claim, counts finite panel data, states the fixed-parameter
limit, and does not claim bit, time, or precision complexity.

## Inherited width qualification

The source event includes its original moment-removal gate
\[
\log(en)\ge\max(e^2,2\mathcal B)=2048e^2L,
\qquad \mathcal B=1024e^2L.
\]
The final synthesis explicitly lists this gate in (20), in addition to
retaining all source-event conditions. It does not change the exponent,
the error coefficient, the label interval, or the acknowledged
unquantified stochastic success threshold. The supervisor identified
the useful explicit addition during this check; the final displayed
formula was verified against the original source requirement.

No unresolved blocking defect remains for this stated scope and final
hash. The compression statement covers all permitted \(m\); the actual
variability ratio is expressly asserted for \(m\ge2\). The inherited
stochastic interfaces, eventual width, and real-coordinate computational
qualification remain part of the PASS rather than separately certified
new results.
