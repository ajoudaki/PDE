# Isolated adversarial full-proof audit

Verdict: **CLEAN**.

No mathematical correction was identified in Section 8 or in the internal proofs it uses. The supplied argument establishes the exact finite compiler coefficient, the stated explicit fifth-order bound, and the interpretation as width-first expectations for the specified fixed-depth, fixed-step-count feature-ascent network. This verdict is confined to those statements and those inputs.

## Inputs, hashes, and read coverage

Only the following two source files were consulted. SHA-256 hashes and byte/line counts were obtained before the audit and checked again after the substantive reading; both checks agreed exactly.

| Input | Lines | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| `/tmp/pde-quantitative-isolated.8JwnFK8g/PROOF.md` | 2676 | 108754 | `acfee00f63de4f35023521fe5c9baef00d018dae3fe79186ea3d6147ea1e77ce` |
| `/tmp/pde-quantitative-isolated.8JwnFK8g/NOTATION.md` | 98 | 5110 | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

Read coverage was complete: PROOF.md lines 1–2676 and NOTATION.md lines 1–98. The first complete PROOF.md pass used contiguous ranges 1–240, 241–600, 601–1000, 1001–1420, 1421–1830, 1831–2220, and 2221–2676, without a gap or truncated tool response. Targeted rereads checked the stopping/moment estimates and the explicit exponent construction.

In particular, Section 5 was read in full, including all of Sections 5.1–5.11, lines 253–1738; Section 8 was read in full, including all of Sections 8.1–8.7, lines 1814–2676. Sections 1–4 and 6 were also read completely. No Section 7 was sought or assumed.

The actual dependency chain audited was Section 8.7's use of Section 5.1 through the complete proofs in Sections 5.2–5.10, together with Section 8's own chronological construction, Price lemma, differentiation compiler, and majorant proof. Section 4 supplies the finite Gaussian square-root construction and Gaussian moment facts. Section 5.4 proves the adaptive multi-matrix conditioning needed here directly. Sections 1–3 and 6 were not substituted for a missing width or regularity argument.

No project files, studies, history, prior reviews, skill files, internet sources, other agents, or external theorem results were consulted. No experiments, generators, builds, installations, Git operations, or subagents were used. The small checks below are direct algebraic calculations. The source files were read-only. This report is the sole created file, written with apply_patch in the separate directory returned by `mktemp -d /tmp/pde-quantitative-audit.XXXXXXXX`.

## Complete fixed-program width dependency

**Model and normalization.** Equations (5.2.1)–(5.2.8) give first weights of variance one, middle stored weights of variance \(1/n\), stored readout variance one, output \(a^Th/n\), and stored-coordinate mobility \(\operatorname{diag}(nI,I,\ldots,I,nI)\). Differentiating that output produces precisely the displayed simultaneous updates: first-coordinate increment \(h\delta\), middle increment \(h\delta H^T/n\), and readout increment \(hH\). Summing earlier increments gives (5.2.11)–(5.2.13) with \(j<k\), as required. There is no residual multiplier or change to the small-readout initialization.

**Chronology and conditioning.** Sections 5.3–5.4 account for exactly \((2N+1)(L-1)\) initialization-matrix actions. Each forward query is available after the preceding forward layer; each transpose query is available after the preceding backward layer. The terminal sweep is forward only. Conditioning is on the global transcript, so dependence through other matrices or earlier uses of the same transpose is allowed. The residual Gaussian decomposition preserves both observed directions. The new-query regression coefficients and innovation variances in (5.4.4)–(5.4.7) have the correct normalization.

**Response cancellation.** The dimensions and orientations in (5.6.4)–(5.6.13) agree: \(\mathcal R=SQ+KP^T\), \(v=K\rho+Sq\), and \(\omega=Q\sigma+Pk\). Substitution cancels the unwanted old-query response in each direction, leaving precisely (5.5.6) and (5.5.9) after the learned increments are added. Ambient source derivatives hold deterministic coefficients fixed. Gaussian integration by parts is proved for singular covariance, so this cancellation does not assume independent temporal coordinates. The additional column of the backward cross block is explicitly retained in (5.8.1a); no conditioning datum disappears between the two sweeps.

**Strict rank.** The argument in Section 5.7 is chronological and includes every needed extension, including terminal forward innovations. Conditional full support gives positive variance for a nonconstant continuous activation. For a nonconstant derivative, the top cotangent uses the current forward innovation and a readout that is nonzero with positive probability. For the affine case \(\phi(x)=px+c\), the proof correctly uses the preceding top forward innovation: the new top cotangent has coefficient \(hp^2\tau_{L,k-1}\), and all older top cotangents exclude that innovation. Using the current innovation in this affine branch would fail, but the supplied proof does not do so. The descending cotangent induction and bottom feature update use their fresh backward innovations on an event where the activation derivative is nonzero. Every required variance is positive for each fixed nonzero \(h\), including negative \(h\). No gap uniform as \(h\to0\) is claimed or needed.

**Moment induction and inverses.** Sections 5.9.1–5.9.4 provide a joint coupling, not just convergence of separate marginals. Independent ideal coordinate marks are assigned to the correct physical populations, and the exact conditional residual shares its fresh Gaussian with the ideal action. A failed Gram is never inverted in the extension; the raw network retains its exact conditional law, with Moore–Penrose conditioning where necessary.

The error decomposition (5.9.8b) includes all four required terms: old-field errors, coefficient errors, innovation-scale errors, and the removed projection. On the tested branch, the inverse difference identity controls coefficient differences by a constant times \(\mathcal Z_n^2\delta_n\); at most two uncontrolled moment factors remain alongside the error. Thus the allocated order \(8\nu\) covers the products needed for a new action. The coordinate bundles' products are covered by order \(4\nu\), and the pair-moment bounds by order \(2\nu\). The finite tower \(R_{j-1}=8R_j\) with at most \(3(2N+1)(L-1)+1\) entries is sufficient. For first-failure estimates, the algebraic Schur bound needs only the already-passed old-Gram tests; it does not require the innovation test it is being used to check.

**Removal of stopping and expectations.** Section 5.10 bounds the raw network directly by a fixed polynomial in initial RMS vector norms and initial matrix operator norms. The supplied Gaussian net argument gives width-uniform moments for the latter. Arbitrarily high fixed polynomial decay of the stopping probability absorbs the possible \(n^{(1/2-1/p)_+}\) conversion to coordinate \(L^p\). Finally (5.10.13) bounds the raw output in moments greater than one, and (5.10.14) gives the required \(L^1\) comparison with the ideal average. This proves convergence of expectations, rather than leaving it to an unproved uniform-integrability assumption. The separate \(L=1\) iid recursion and constant-activation branch are valid and do not require the rank proof.

## Section 8: chronology, singular calculus, and exact coefficient

**Layerwise call order.** Section 8.2 reorganizes the same population assignments. Before an interior forward call, the lower feature Gram and the old upper cotangent Gram are available. The top call produces the current top cotangent data; descending calls then produce the data for the next lower call. The bottom call constructs the feature Gram and forward responses for the next step. New expectations are not inputs to their own integrands or covariances. Full response coefficients are assembled after the associated expectations. Old source marginals agree with earlier calls because their histories and covariance entries are retained. Consequently the chronological Gram constructions remain positive semidefinite even when their rank changes.

The dimensions in (8.2.5) are at most \(D_N=2N+2\), and the call count is exactly \((2N+1)(L-1)\) for \(L\ge2\). The single \(L=1\) call uses the correct simultaneous old-state recursion. No terminal backward call or fictitious connector is inserted.

**Singular Price lemma.** The determinant/exponent calculation, two spatial integrations by parts, factor \(1/2\), and ordered off-diagonal contraction in (8.3.2)–(8.3.4) are correct. Repeated differentiation includes derivatives of covariance coefficients, not merely repeated multiplication by \(C'\).

The regularization \(C_\epsilon=C+\epsilon I\) is adequate across rank changes. Its positive-order derivatives equal those of \(C\), and the uniform square-root difference is at most \(\sqrt\epsilon\). Compact uniform continuity plus a common Gaussian polynomial tail bound gives uniform convergence of all six expectations, for orders zero through five. Passing to the limit in the fundamental-theorem identities then identifies the derivatives. No differentiability of \(C^{1/2}\), and no inverse bound for the singular covariance, is being assumed.

An elementary rank-change check is \(C(h)=h^2\), \(\psi(x)=x^2\): the expectation is \(h^2\), and the recursion gives its second derivative as 2 even though \(C'(0)=0\). The supplied recursion retains exactly this \(C''\) contribution. Evenness of the network covariances is therefore not being mistaken for vanishing of all their jets.

**Derivative budget and envelopes.** An unexpanded local integrand has activation atoms of order at most one; a response's preliminary source derivative raises that ceiling to two. The guarded mixed array adds at most \(2r+j+q\le10\) ordinary derivatives. Thus activation order 12 suffices. No step differentiates \(\phi^{(12)}\), advances an earlier scalar token beyond order five, or asks for a sixth covariance derivative. Earlier scalar response tokens remain fixed under spatial differentiation, preventing a hidden accumulation of source derivatives through previous calls.

The guard in (8.4.5) provides every child required by the recursion, including \(q+2\) and \(j+1\). The entrywise absolute covariance bounds and ordered spatial aggregation safely overcount off-diagonal contributions. Finite syntax, the activation growth bound, and the previously bounded scalar jets provide the common polynomial envelopes required by Lemma 8.2. This closes the regularity induction through the actual chronology.

**Exact coefficient.** Equation (8.4.8) constructs jets from earlier scalar jets and finite Gaussian expectations at \(C(0)\), before identifying them with output derivatives. The later Price induction supplies that identification, so the definition is not circular. Source differentiation precedes the identification of coalesced temporal coordinates. Collapsing them earlier would alter individual source derivatives, but that operation is expressly excluded.

At zero, the collapsed source law and vanishing responses yield the stated activation-integral reduction. Independent carrier powers with odd expectation vanish; surviving powers of their variances are integer powers of \(\mu_{\phi'}\). Hence the compiler is a finite expression in the Gaussian moments and integrals (8.4.12). No unproved compact moment formula is needed. Since the jets are ordinary derivatives, the coefficient

\[
\mathcal C^{\mathrm{cmp}}_{\phi,L,N}
=\frac{8\mathcal J^{\mathrm{cmp}}_{3,N,L}-\mathcal J^{\mathrm{cmp}}_{3,2N,L}}6
\]

has both the correct doubling factor and the correct factorial.

## Explicit exponent, cancellations, and final identification

**Explicit one-call bound.** The size estimate in Section 8.5 has sufficient allowance. The raw local history is bounded by the \(8(N+1)\) iterations in (8.5.1). Product/output formation fits below \(c_{N,0}\). A formal derivative is bounded by \(2(|e|+1)^2\). Ten mixed-derivative levels, one preliminary response derivative, one ordered-index aggregation, five Price combination levels, and two assembly levels require at most 19 enlargements; the recurrence provides 24. Expanded integer multiplicities, covariance contractions, and dimension factors are included. The construction treats earlier scalar outputs as incoming tokens, which is essential to this local size count.

For \(C=C_N\), the coefficient bound is \((2B_\phi)^C S^C\), while Gaussian integration costs at most \(S^{C/2}\nu_N\). Coefficient and covariance-bound assembly involve sums, so a single common Gaussian-moment bound suffices. Using \(S\ge2\), \(p_N=2C_N\), and \(2^{C_N}\nu_N\le B_\phi^{\alpha_N}\) proves the stated \(B_\phi^{r_N}S^{p_N}\) bound with no missing multiplicative constant. Initialization bounds only constant input functions by \(B_\phi^{2L}\); higher jets of later histories are actually compiled.

Iterating over \(M_{L,N}\) calls therefore gives exactly

\[
E_{L,N}=2L p_N^{M_{L,N}}
+r_N\sum_{i=0}^{M_{L,N}-1}p_N^i,
\]

which agrees with (8.5.13). Every defining recurrence or sum terminates at a specified finite index. Monotonicity in \(N\) follows from the displayed recurrences and Gaussian-coordinate coupling, including the special case \(M_{1,N}=1\).

**Parity and linear cancellation.** Simultaneously reversing \(h,A,\chi\) gives the stated parity without any parity assumption on \(\phi\). The feature and cotangent Grams are even, responses are odd, and \(C'(0)=0\). Differentiating the ambient source expressions before coalescence yields

\[
b_{2,kj}=\mu_{\phi'},\qquad
b_{\ell+1,kj}=\mu_{\phi'}(1+b_{\ell,kj}),\qquad
F'_{N,L}(0)=N\sum_{a=0}^{L}\mu_{\phi'}^a.
\]

The forward response contribution is present in this calculation. Thus doubling the step for \(N\) updates and doubling the count at step \(h\) cancel linearly. Oddness removes orders zero, two, and four.

A direct algebraic check is \(\phi(x)=x\), \(L=N=1\). The simultaneous scalar recursion gives \(F_{1,1}(h)=2h\) and \(F_{2,1}(h)=4h+4h^3\). Therefore \(F_{1,1}(2h)-F_{2,1}(h)=-4h^3\), agreeing with the compiler combination \((8\cdot0-24)/6=-4\). This checks the step convention, sign, and factorial without a width-limit differentiation or an experiment.

**Fifth-order remainder.** Taylor's integral remainder through degree four needs only the proved \(C^5\) regularity. Its magnitude is at most \(\sup|F^{(5)}|\,|u|^5/120\) for either sign of \(u\). The two outputs consequently give the numerator \(32\overline{\mathcal J}_5(F_{N,L})+\overline{\mathcal J}_5(F_{2N,L})\). Monotonicity of the explicit exponent and \(33/120<1\) yield precisely (8.1.5) on \(|h|\le1/2\). No sixth derivative is needed.

**Actual width-first expectations and scope.** The stronger activation assumptions imply Section 5's hypotheses with \(M=2M_\phi\). Applying its proved expectation theorem separately at \((L,N,2h)\) and \((L,2N,h)\), for each fixed nonzero \(h\), gives (8.1.6). The argument at \(h=0\) is separate and valid: unchanged hidden features are independent of the centered initial readout. The constant branch gives \(F_{N,L}(h)=Nh\), with zero comparison and coefficient. Nonconstant affine activations are covered by the rank proof and the compiler.

The result uses the order-one stored readout and feature-ascent clock throughout. Equality \(N(2h)=(2N)h\) is equality of accumulated feature steps. No trained-network theorem, physical-time gradient flow, growing-N width result, uniform-in-h regression gap, or exchange of a finite-width derivative with a width limit is imported.

Required corrections: **none identified**.
