# Internal audit of the physical proxy and activity-damped transfer

Date: 2026-10-01. Reviewer: fresh scoped agent `width_transfer_audit`.

**Verdict: the downstream transfer is accepted, conditional on the stated quantitative finite-program coupling.** I found no mathematical blocker in the physical proxy construction, its consistency and current-state tail estimates, the activity-damped comparison, or their all-time consequence. The amplification is indeed `exp(CR)`, rather than `exp(CRT)`, once the proxy's integrated residual is bounded. The proxy does not need its own Gram gap. This report does **not** verify the quantitative Gaussian coupling, and is neither a complete acceptance of the explicit-width theorem nor a promotion review.

## Assignment, isolation, and actual read scope

The assignment was to audit physical proxy construction and consistency, activity-damped stability, current-state carrier tails, use of the actual dense Gram, transfer to the original nonlinear finite flow, and the all-time extension. It explicitly permitted treating the quantitative Gaussian coupling in `RESULT.md` as a hypothesis and forbade experiments, Git operations, manuscript edits, the study README, other checks, other studies, and history.

Scientific files actually read:

| File | Read coverage |
| --- | --- |
| `RESULT.md` | Complete, lines 1–268 |
| `DAMPED_TRANSFER.md` | Complete, lines 1–213 |
| `PROGRAM_RATE_ADDENDUM.md` | Complete, lines 1–863 |
| `paper/main.tex` | Setting, population notation, and closure definitions, lines 174–401; a heading/label search of this file only |
| `paper/results.tex` | Complete, lines 1–233 |
| `paper/proof_alltime.tex` | Complete, lines 1–928; the initially truncated middle output was reread in full |
| `paper/proof_tracking.tex` | Complete, lines 1–319 |
| `paper/proof_finite_time.tex` | Complete, lines 1–502 |

Also read the shared `AGENTS.md` and `RESEARCH_WORKFLOW.md`, the required `solve-math-rigorously` and `investigate-conjectures` skills, and the latter's adversarial-audit reference. No study README, `PROGRAM_RATE_CHECK.md`, other review, other study, historical material, external scientific source, or excluded route file was opened. The finite-time proof was checked for compatibility of norms and regularity; its much larger width-dependent stability constant is not used for the all-time logarithmic rate.

Method: read the source proofs, independently expand the forward/reverse proxy actions and three-factor update subtraction, derive the damped integral inequalities, trace each tail transfer and limit, and recompute the mesh/rate/probability arithmetic. No experiment or numerical test was performed. The only output created is this report.

Input SHA-256 hashes, identical at the initial read and final verification:

```text
8050f8ff34f00e1263e422d8b8a51bba85be4ae216cec5bd66299b7b2454c267  RESULT.md
27ee61e6aa1367329e0baf3e1ae41993ead53f323ba98af2942a1f034bd3a96c  DAMPED_TRANSFER.md
a11c6e70204a0202da18075afc6565f6e46205de08865cdbcc5c5c38fccd43b7  PROGRAM_RATE_ADDENDUM.md
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
6e76e83aae3a3e36f588bdf37dddf72ac811bf2644de664fb0b4b83f117704a1  paper/results.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be  paper/proof_tracking.tex
07ebf620943f5e8078e4f7647dfa9df893157f16d29c684e758dcd63d33eacd4  paper/proof_finite_time.tex
```

## Exact conditional boundary

The unverified quantitative input is the coupling in `RESULT.md` lines 114–157, including its empirical pairing/soft-tail observations and its comparison to the original population program. In the notation of the addendum, the input must supply the simultaneous event in lines 145–204: with

\[
\xi=e^{CN^5}n^{-1/8}+Ce^{-cN^2},
\]

the specified empirical contractions differ from **original population** contractions by `C xi`, oracle RMS norms are uniformly bounded, and all specified oracle soft-tail norms are at most `Ce^{-cM²}+C xi`, with the stated failure probability. In particular, an output prediction concentration theorem alone would not suffice. The common-population bias and the final square-root conversion of squared tail tests are part of this conditional input.

The uniform original population Euler carrier tails, physical tube, true initialized adjoints, and strong population flow are supplied by the current paper. Their complete dependency bodies in `proof_alltime.tex` were read: initialized operator construction at lines 488–506, Euler tube at 508–554, response/tail argument at 556–703, and strong-flow construction and regularity passage at 705–815. The transfer below uses these population facts and does not assume a quantitative carrier bound for the actual finite trained network. The general quantitative conditioning proof in the excluded `PROGRAM_RATE_ROUTE.md` was not inferred from a prior review or silently imported.

## 1. Physical proxy and exact consistency

**Accepted.** Addendum lines 118–143 define actual finite parameters using the original initialized arrays and explicit rank-one increments. Their initial state is exactly the actual network initialization. Oracle fields and physical fields are correctly distinguished; the physical backward pass remains unclipped.

For a hidden forward action, direct expansion gives

\[
\widetilde W_k h^p_{a,k}-z^p_{a,k}
=-\epsilon W_0\chi
-\frac2m\sum_{r<k,b}h_r r^o_{b,r}\delta^p_{b,r}
 \left(\frac{\langle h^p_{b,r},h^p_{a,k}\rangle}{n}-C^h_{br,ak}\right).
\]

The transpose expansion has the same form with the feature vector outside and a backward-response pairing inside. These are precisely (A11) and (A13), addendum lines 233–293. Both reuse the actual `W_0` and `W_0^T`; no independent reverse matrix or independence of trained neurons is substituted. The noise terms are retained explicitly. The first matrix uses its Gaussian row roots and deterministic input contractions, so its expanded first-layer identity is exact.

The coefficients obey `sum h_r |r^o_{b,r}| <= C sum h_r rho^o_r <= C`. Hence these action errors are `O(xi)`, without a factor equal to the number of nodes or physical horizon. The bounded oracle RMS norms give the proxy tube and speed bounds in (A9)–(A10), lines 206–231. At fixed `Y`, eventual `xi <= 1` is enough for a fixed enlarged tube; no coordinate maximum of an activation is used.

Forward recomputation through fixed depth consequently costs `C xi`. At a backward gate the exact decomposition in (A15), lines 317–337, is correct. Its changed-gate product obeys

\[
\|[g(\widetilde z)-g(z^p)]p^p\|_n
\le jR\|\widetilde z-z^p\|_n
 +2s\|p^p1_{|p^p|>R}\|_n.
\]

The clipping discrepancy at `N` is bounded by the same carrier tail at `R <= N`. Backward discrepancies propagate through bounded operators and gates. The cutoff is added at each fixed layer; it is not multiplied into `R^L`. This validates (A16), and the readout pairing test validates (A17), lines 345–365. In particular, the physical proxy residual is close to the original Euler residual by `C xi`, even though the proxy does not evolve by the exact physical vector field.

## 2. Residual-weighted interpolation defect and activity

**Accepted.** Put `alpha(t)=(t-t_k)rho^o_k`. The actual segment displacement is `C alpha(t)`, not merely `Ch`. Applying the state-to-oracle estimates (A19)–(A20) at this displacement gives (A27), addendum lines 558–581.

The relevant hidden-block difference is exactly

\[
(r_p-r^o_k)\delta_p h_p^T/n
+r^o_k(\delta_p-\delta^p_k)h_p^T/n
+r^o_k\delta^p_k(h_p-h^p_k)^T/n.
\]

The first term costs `C(alpha+xi)`. The remaining terms retain `rho^o_k`, so

\[
e_p(t)\le C(\alpha+\xi)
+C\rho^o_k\{(1+R)(\alpha+\xi)+e^{-cR^2}\}.
\]

The readout and first-layer blocks obey the same estimate. Since `sum h_k rho^o_k` and `sup rho^o_k` are bounded, integrating proves (A29), lines 602–629:

\[
\varepsilon_p\le C\{(1+R)h+e^{-cR^2}+(T+1+R)\xi\}.
\]

There is no unweighted `T e^{-cR²}` term. A `T xi` term is necessary because oracle residual recomputation need not vanish with `rho^o_k`, and it has been retained. The bound

\[
\rho_p(t)\le(1+Ch)\rho^o_k+C\xi
\]

gives `integral rho_p <= C+CT xi`, as in (A30). Under the eventual choice `T xi <= 1`, the activity is uniform. No fitting theorem for the proxy has been assumed. The slightly looser bound in `DAMPED_TRANSFER.md` lines 99–123 is compatible with this sharper version.

## 3. Current physical carrier tails

**Accepted.** The tail source in the damping estimate concerns the proxy's recomputed, unclipped current carrier. It is not a bound merely on the stored oracle vector. For any current physical carrier `p` and oracle node carrier `p^p`,

\[
\|p1_{|p|>R}\|_n
\le2\|(|p|-R/2)_+\|_n
\le2\|p-p^p\|_n+2\|(|p^p|-R/2)_+\|_n.
\]

The positive-part map is 1-Lipschitz, whereas the hard indicator need not be continuous. Combining this inequality with (A27) and the predeclared soft-tail tests proves (A31), lines 645–654. Multiplying by the **current proxy** residual, then using (A30), gives (A32), lines 658–679:

\[
Z_p(R)\le C\{e^{-cR^2}+(1+R)(h+\xi)\}.
\]

The analogous dense current-state comparison in (A20), (A23)–(A25), and lines 813–826 correctly uses distance `D(t)+C alpha(t)` from the node. All integer thresholds `M <= N` are covered by the simultaneous oracle event. For `M>N`, monotonicity leaves at most `Ce^{-cN²}` in addition to the error; this is absorbed into the fixed exponential-bias component of `xi`, as explicitly permitted at lines 482–484. The Gaussian envelope constants must be chosen once. This does not require a union bound over infinitely many cutoffs or an empirical time net.

## 4. Dense Gram and activity-damped stability

**Accepted.** The finite flow satisfies `dot r_D=-2 Gamma_D r_D`. Because `E_p=dot theta_p-F(theta_p)`, the physical proxy satisfies

\[
\dot r_p=-2\Gamma_p r_p+J_pE_p.
\]

Subtracting with `u=r_D-r_p` gives (A33), addendum lines 684–701, and equation (11) of `RESULT.md`:

\[
\dot u=-2\Gamma_Du-2(\Gamma_D-\Gamma_p)r_p-J_pE_p.
\]

This ordering is essential. The damped matrix is the actual dense Gram, whose lower bound is already available. The paper gives `Gamma_D >= lambda I/2` with its initial-margin notation (`proof_alltime.tex` lines 276–320); thus the damping rate may be taken as `lambda`. The generic positive gap named `lambda` at `DAMPED_TRANSFER.md` line 7 can simply be relabelled consistently. No proxy Gram lower bound enters the proof.

One-reference gate subtraction, now with proxy carriers as the reference, gives

\[
\|\Gamma_D-\Gamma_p\|_{op}
\le C\{(1+R)D+H_p\},\qquad
\|J_p E_p\|_m\le C e_p.
\]

The latter holds for **all** parameter blocks in the proxy defect, including first matrix and readout; their prediction differential contributions are bounded by backward/forward RMS norms in the normalized parameter metric. It does not rely on the closure-specific restriction `E_1=E_w=0`.

Writing `v=||u||_m`, integrating

\[
D^+v\le-\lambda_0v+C\rho_p\{(1+R)D+H_p\}+Ce_p,
\qquad v(0)=0,
\]

and dropping the nonnegative terminal value gives (A34). Subtracting the parameter updates in the same residual order gives

\[
D(t)\le C\varepsilon_p(t)+C\int_0^t v
+C\int_0^t\rho_p\{(1+R)D+H_p\}.
\]

Substitution and the integrating factor for `C(1+R)rho_p` yield

\[
\sup_{t\le T}D(t)
\le C\exp\!\left(C(1+R)\int_0^T\rho_p\right)
 [\varepsilon_p+Z_p(R)]
\le Ce^{CR}[\varepsilon_p+Z_p(R)].
\]

This reconstructs (A35), lines 703–759, without an unstated physical-time Gronwall factor. Norm zeros are handled by regularization, and piecewise affine proxy endpoints are harmless because the chain rule and residual identities hold almost everywhere.

## 5. Population comparison, regularity, and initialized sources

**Accepted for the stated source dependencies.** The population comparison (A36), lines 761–785, is the same argument on the common Hilbert spaces with true initialized adjoints. Its original Euler nodes have no empirical/clipping consistency term, so `xi=0`; their interpolation still has a cutoff-controlled defect. The strong population path supplies the gap. The Hilbert–Schmidt rank-one identity is exactly the normalized finite Frobenius identity needed by the update subtraction.

The comparisons use `phi` only through its intercept and bounded slope, and use `g=phi'` through boundedness and its Lipschitz constant. No derivative of `g` is taken in the new transfer argument. The paper justifies the scalar prediction differential without assuming the activation Nemytskii map is Fréchet differentiable from `L²` to `L²` (`proof_alltime.tex` lines 724–737), and provides the mollification passage to the stated `C¹` class with Lipschitz derivative (lines 799–815). Thus the downstream argument does not strengthen the activation assumption to `C²`, bounded activations, or coordinatewise bounded features/readout.

The physical comparison preserves the original initialized-source dependence. Its action discrepancies contain the original `W_0` and its actual transpose, and the conditional coupling controls the necessary same-array empirical contractions. Original deterministic population coefficients may be used in this proof-only oracle without making them accessible to the deployed closure. They enter no altered network evolution. Learned increments remain nonlinear responses to the evolving physical parameters after the comparison is made.

## 6. Rate arithmetic and all-time predictions

**Accepted.** With `K=floor(log(e^e+n)^(1/128))`, `N=ceil(C_0 K³)`, `T=(2/kappa)log K`, `h=T/K`, and `R=A sqrt(log K)`, the eventually small mesh lies in the paper's valid population Euler regime. The constants may be fixed before sending width to infinity. Since

\[
N^5=O((\log n)^{15/128})=o(\log n),
\]

the quantitative coupling error and failure probability are polynomially small in width, and `T xi <= 1`. Choosing the Gaussian exponent so `cA²>2` makes both comparisons

\[
e^{CR}\{(1+R)h+e^{-cR^2}+(T+1+R)\xi\}
=K^{-1+o(1)}.
\]

Dense carrier transfer adds only `1+R`. After `T`, the actual dense carrier RMS is bounded and the remaining dense activity is at most `Ce^{-kappa T}=CK^{-2}`. This proves the stated quantitative excess bound for the dense-only `a_n`. Applying the paper's exact `b_n=C Phi(a_n)` relation (`proof_tracking.tex` lines 233–252) costs only `K^{o(1)}`. The event therefore works for every closure order, rather than requiring a countable union over orders.

For a passive input, normalization by `s_x=1+||x||/sqrt(d)` keeps initial root variances, activation intercepts, forward slopes, and normalized training/probe contractions uniformly bounded. Although the derivative-Lipschitz constant of `phi(s_x u)/s_x` can grow with `x`, no passive backward gate or second derivative is used. The normalized forward instruction needs only the uniform slope bound. This checks the normalization used at `RESULT.md` lines 243–258.

At mesh nodes, combine the finite-to-proxy physical bound, proxy-to-oracle forward recomputation and pairing error, and population Euler-to-strong-flow bound. Between nodes, the segment displacement adds at most `Ch rho^o_k`. After `T`, both actual finite and population predictors vary by at most `Ce^{-kappa T}s_x`, by the paper's fitting/speed bounds. Thus a normalized single-probe estimate of `K^{-1+o(1)}` holds over all time, and the weaker `CK^{-1/2}` used in `RESULT.md` is valid.

On the original physical good event, both normalized predictions are bounded even if the program event fails. Hence the single-input second-moment estimate (17) in `RESULT.md` lines 247–254 follows. Tonelli and Markov at threshold `C_mu K^{-1/4}` give failure at most `C_mu K^{-1/2}` after absorbing the polynomially small width term. Since `K^{-1/4}` is comparable, up to a fixed constant for eventual width, to `log(e^e+n)^(-1/512)`, this is sufficient for the common rate and confidence claimed in (3). The time supremum is already inside the nonnegative integrand. Finite second moment of the fixed test law suffices; no quantitative input-tail assumption is used.

Auxiliary Gaussian roots do not weaken the final probability statement about the original network: the desired dense error and carrier inequalities depend only on its original initialization. The joint initialization/auxiliary event is contained in those desired inequalities, so its failure bound also bounds their marginal failure probability. For test moments, the integrand likewise does not depend on auxiliary roots, so expectation over them leaves it unchanged. This elementary marginalization is implicit in the notes and closes the event-dependence bookkeeping.

On a bounded input set, separate normalized single-probe events on the specified finite net cost a fixed power of `K`, absorbed into `n^{-c}`. The common input Lipschitz bound then extends the estimate across the set. These separate programs need not fit simultaneously into the single program's `N=O(K³)` budget.

## Accepted and blocked scope

Accepted: the physical proxy bridge; residual-weighted source estimate; current physical carrier tails; `exp(CR)` stability using the actual dense Gram; deterministic population Euler upgrade; transfer to the original nonlinear finite flow; and the all-time parameter/prediction rate arithmetic, conditional on the exact quantitative program event stated above and the current paper's population foundations.

No required downstream correction was found. The proxy does not require a positive Gram gap, trained-neuron independence, bounded activation values, or an everywhere-defined second activation derivative. The result remains fixed-depth, small-label, exact-zero-readout, continuous gradient flow and high probability.

Blocked/unassessed by this assignment: unconditional acceptance of the quantitative Gaussian coupling and thus of the complete explicit-width theorem. The excluded quantitative route would have to verify its full simultaneous contraction/tail event and original-program bias under the precise regularity and initialized-source assumptions. This report must not be cited as that verification, as a polynomial-in-width theorem, or as a promotion approval.
