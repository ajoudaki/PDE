# Internal check of the reference comparison and response bridge

Reviewer: /root/p2_variation. Date: 2026-09-11.

This is the assigned scoped collaborator check, not a fresh complete independent A–C review. P2_VARIATION.md remains frozen. No other P2 route or report was read.

## Verdict

The raw Hilbert–Schmidt upgrade, finite comparison **to the trained reference**, compactness of the P1 response family, compact-direction Taylor lemma, and conditional width-first finite-remainder bridge are valid in their limited roles. They do not prove nonlinear changed-law population existence through time 40 or the uniform nonlinear population remainder.

The observation contract needs a mathematical clarification: “bounded gates” must mean fixed bounded **continuous** functions of previously identified finite same-layer tuples. Starting fields must be the raw state and displayed feature/backward fields, together with identified initialized generated fields; arbitrary P1 fields such as nonlinear clocks do not automatically belong to this contract.

Two other corrections are needed: the population loss-gradient sentence must retain the factor \(2(f-y)\), and the response bridge must specify the normalized data metric before using diameter \(2+2Y\). Its population-remainder display also has a literal “epsilon” where \(\epsilon\) is intended. These are local corrections; the restricted comparison and conditional bridge survive them.

## Coverage and hashes

The two assigned documents, complete P1 section, complete frozen P1 dependency packet, and complete manifest were read. Current global_nonlinear.md C.4.1–C.4.3 was read completely. Truncated displays were repaired by reading their missing ranges. The dependency packet's rational certificate was read, not executed. No training computation or Git operation was performed.

| Input | Coverage | SHA-256 |
|---|---|---|
| P2_REFERENCE_COMPARISON.md | All 227 lines | 869415030167bf422c5a0a5fad05cd35fafc5bbe5221e40968e8ae4db4cafba3 |
| P2_RESPONSE_BRIDGE.md | All 131 lines | bd055e9dce3c6cafad4c421d5180243e8314b260ba81d1c237cc619f48ba2ba7 |
| P1_SECTION.md | All 2062 lines | 33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38 |
| P1_DEPENDENCIES.md | All 3238 lines | ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79 |
| P1_MANIFEST.json | All 83 lines | f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d |
| Current docs/global_nonlinear.md | C.4.1–C.4.3, lines 3976–4942 | Covered-byte hash: 9d5d24546fc665a23d377729388aec208c824cb0d8f5b147989a479b10335117 |

The full current global_nonlinear.md has 8959 lines and SHA-256 3f32122dea7915e25e4abc7abe9d74017d535badfa5abbe1939e84fe2b100bdf. That full-file hash is metadata, not a claim that its remaining current content was read. Both P1 scientific-input hashes agree with P1_MANIFEST.json. Its historical full-book base hash differs from the current full-book hash; this check uses the frozen dependency proofs and only the authorized current proof units.

P2_CONTRACT.md was outside this added input scope and was not read. The finite bridge is therefore certified below with an explicit quantifier order, rather than by presuming the meaning of the unprovided full A–C contract.

## 1. Energy, existence, and the population gradient correction

The finite field has the correct factor two, normalized readout, first/readout mobility \(n\), and middle mobility one. With normalized layer pairings, the rank \(dh^T/n\) has ordinary Frobenius norm

\[
\|dh^T/n\|_F=(\|d\|_2/\sqrt n)(\|h\|_2/\sqrt n).
\]

Thus the displayed raw metric is exactly the gradient metric. Integrating
\[
L_\lambda'=-\|\dot\theta\|_{n,\mathrm{raw}}^2
\]
and applying Cauchy–Schwarz proves reference-comparison (2). The finite-dimensional endpoint continuation is valid. For an arbitrary Borel law, compactness of the input-label domain bounds all parameter derivatives on every compact finite parameter set, so differentiation under the exact law integral is justified.

On the initialization event, \(|f_n(0,u)|\le1\), hence \(L_\lambda(0)\le(Y+1)^2\) simultaneously for all laws. The common ball and pointwise readout estimate follow directly; no support-size bound or changed-law Gaussian-tail statement is used.

For a supplied population \(C^1\) raw solution, III.F.10 proves scalar prediction differentiability. Gradient continuity jointly in state/input follows by bounded-continuous-multiplier continuity, actual adjunction, and the HS rank identity. Compactness of the input domain makes this uniform near a fixed state. The exact loss gradient is

\[
\nabla L_\mu(\theta)
 =2\int(f_\theta(u)-y)\nabla f_\theta(u)\,d\mu(u,y).
\tag{C1}
\]

**Correction at reference-comparison lines 91–92:** “the law integral of the prediction gradient” omits \(2(f-y)\) literally. Replace it by (C1). The correct weights already occur in the finite derivation and field, so no subsequent estimate changes.

The population energy and \(2TY\) readout bound then hold for that existing solution. They do not give infinite-dimensional existence or continuation at a new endpoint. The draft correctly states this limitation.

## 2. HS transport upgrade and reference-only comparison

The HS upgrade is a valid examination of the complete transport proof, not merely an inference from one norm dominating another. All forward/adjoint differences use

\[
(A-\bar A)h+\bar A(h-\bar h),\qquad
(A-\bar A)^*d+\bar A^*(d-\bar d),
\]

with \(\|A-\bar A\|_{op}\le\|K-\bar K\|_{HS}\) on the same carrier sharing \(A_0\). The middle velocity is the sum

\[
(r-\bar r)d\otimes h
+\bar r(d-\bar d)\otimes h
+\bar r\bar d\otimes(h-\bar h).
\]

Every term has the same bound in HS because \(\|a\otimes b\|_{HS}=\|a\|_2\|b\|_2\). The first-row changing-input term retains \(u-u'\). The gate calculation still introduces only one power of the cutoff \(R\). This proves reference-comparison (4), including its output-velocity norm, with only reference tails.

The finite middle metric is ordinary Frobenius, not Frobenius divided by \(\sqrt n\); the draft gets this right. No HS assertion for \(A_0\), cross-carrier subtraction, or \(L^p\) bound on \(A_0\) is used.

Frozen C.4.5.2 proves the active Gaussian-plus-bounded reference decomposition and the actual finite-reference cutoff transfer. Its readout-supremum and time-Lipschitz bounds justify the fixed-time-grid extension. A sufficiently large fixed \(R_0\) turns the shifted Gaussian exponent into \(Ce^{-cR^2}\). This establishes precisely (5), retaining the actual finite random readout.

Using (4) with that one reference and integrating gives (6). Therefore, for deterministic widths \(n_k\to\infty\) and laws \(\lambda_k\) satisfying \(W_1(\lambda_k,\nu_*)\to0\),

\[
\sup_{t\le40}d_{n_k,\mathrm{raw},1}
(\theta_{n_k,\lambda_k}(t),\theta_{n_k,*}(t))
\longrightarrow0\quad\text{in probability}.
\tag{C2}
\]

The order is fixed \(R\), then the width/law-sequence limit, then \(R\to\infty\). Choosing a cutoff depending on a separately fixed radius \(q\) in (7) respects this order. Absorbing \(1+R\) into its exponential and the positive-excess interpretation for \(\limsup W_1\le q\) are valid.

The comparison approaches only \(\nu_*\). At fixed changed \(\mu\), it leaves a fixed \(2\Phi_Y(W_1(\mu,\nu_*))\), so it cannot construct that changed-law population by completion. Also \(\Phi_Y(\varepsilon)/\varepsilon\) diverges, so no bounded difference quotients follow. The draft correctly preserves both limitations.

The empirical-law paragraph is valid for samples from \(\nu_*\). Finite partition frequencies converge and the other errors belong only to the initialized reference. Its pathwise comparison allows arbitrary simultaneous \(n_k,m_k\to\infty\), with no relative rate. This remains reference sampling, not consistency at an arbitrary fixed nearby \(\mu\).

## 3. Observation transfer and its exact contract

The claimed finite typed induction is valid with the following precise grammar: start from the raw \(w,c\), the displayed forward/backward fields \(h,z,H,d,Q\), and identified initialized generated fields; use finitely many fixed globally Lipschitz coordinate maps, fixed bounded continuous gates of identified same-layer tuples, and the displayed typed actions/adjoints. Record finite same-layer joint laws and quadratic contractions.

Lipschitz maps propagate same-carrier RMS error. Actions propagate it by the bounded action norm plus the HS state error times the input norm. For a gate product use

\[
b(z_n)v_n-b(\bar z_n)\bar v_n
=b(z_n)(v_n-\bar v_n)
 +[b(z_n)-b(\bar z_n)]\bar v_n.
\]

Truncate the identified reference field \(\bar v_n\), pass the gate difference on the bounded part, then remove the cutoff by reference \(W_2\) identification and compact-family square tails. If a bounded continuous gate is not uniformly continuous on all arguments, restrict the identified argument tuple to a large compact box first; tightness and uniform integrability of the multiplied reference squares control the excluded event. Quadratic contractions then pass by Cauchy–Schwarz. The equal-index coupling bounds actual/reference tuple \(W_2\) distance by their same-carrier RMS difference.

For each desired accuracy the reference approximation is a fixed finite program before width tends to infinity. Its fixed-program identification and the above induction prove initialized/current action observations in both directions and paired initial/current hidden observables. Arbitrary products of two unbounded varying \(L^2\) fields are excluded.

**Necessary repair at reference-comparison lines 183 and 190:** specify bounded **continuous** gates. Boundedness alone is false even on a one-point probability space: \(z_n=1/n\to0\), \(v_n=1\), and \(b(z)=\mathbf1_{\{z>0\}}\) give \(b(z_n)v_n=1\), while \(b(0)v=0\). Tail truncation does not repair this failure.

**Starting-field clarification at lines 180–181:** “current and initialized fields” should name the raw fields above or fields generated by this grammar. It must not include arbitrary fields solely because P1 names them. In particular (C2) supplies no \(L^2\) control of the unbounded clock \(g(w)-g(w_0)\), \(\cosh^2w\), or inverse-gate-weighted sources. The intended raw observation claim remains valid after this clarification.

## 4. Compact response directions and Taylor lemma

P1 C.4.6.3 §7 supplies the essential premise: joint strong continuity of the atom-forcing integrand, including its weighted first-layer component, on compact feature-time/input/label sets. Composition with the physical clock gives continuity on \([0,40]\times Z\). P1 obtains it from weighted source moments; it is not inferred from the bounded propagator.

Splitting a coupling into distances at most \(h\) and greater than \(h\) proves

\[
\|b_\nu-b_\rho\|_{C_t\mathcal V}
\le\eta(h)+2M W_1(\nu,\rho)/h.
\]

Approximate couplings suffice. At \(W_1=0\), arbitrary \(h\downarrow0\) gives equality. Finite spatial nets and finite nets of the resulting probability simplex prove total boundedness of laws. The displayed forcing map is uniformly continuous, so its image is totally bounded in the complete continuous-curve space. The solution map

\[
b\longmapsto\left[t\longmapsto\int_0^t U(t,s)b(s)\,ds\right]
\]

is bounded into that space, with norm at most \(T\sup\|U\|\). Strong output continuity follows from P1's integral equation. It therefore maps the forcing family to a relatively compact response family, proving response-bridge (2).

The raw conversion and hidden-variation maps in P1 T14 are uniformly bounded and strongly continuous along the reference. Hence they induce continuous maps on compact families of response curves. If passive-input uniformity is required, include \(u\in S^1\) as a compact parameter: the explicit formulas give joint strong continuity in \((t,u)\), so all evaluated directions form a compact family over \((\nu,t,u)\).

The Taylor lemma is correct. On \(|V|\le R\), divide the scalar remainder by \(\varepsilon\) and bound it by the modulus of \(\phi'\) at \(|\varepsilon|R\) times \(|V|\); on the complement use \(2\|\phi'\|_\infty|V|\). Compact \(L^2\) sets have uniformly integrable squares, giving the ordered limit. This works uniformly in the base \(z\) and also for \(\phi'\) when \(\phi=\tanh\).

It proves neither ambient \(L^2\to L^2\) Fréchet differentiability nor compactness of actual nonlinear divided differences. The draft correctly says so.

## 5. Conditional finite bridge and metric correction

In addition to P1, the bridge requires the following unproved population premises:

- Predictions \(f_\mu\) exist on a genuine \(W_1\) neighborhood of \(\nu_*\).
- For every fixed law in that neighborhood, actual finite GF predictions converge in probability in the uniform time/input norm.
- The population remainder (4) holds uniformly in the contaminating law with one \(\omega_Y(\varepsilon)\to0\).

Writing these explicitly would make “Suppose A–B” self-contained; they are not conclusions of either reviewed document.

**Metric clarification:** \(D_Y=2+2Y\) is valid for

\[
d_Z((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|,
\]

equivalently \(|u-u'|+|y-y'|\) on normalized inputs. It is not the diameter for \(|x-x'|+|y-y'|\) on P1's \(Z=\sqrt2S^1\times[-Y,Y]\), whose diameter is \(2\sqrt2+2Y\). Specify the normalized metric at the first \(d_Z/W_1\) occurrence, or use the enlarged diameter for the unnormalized metric. C.4.1 uses the normalized convention.

After this clarification, matching the unchanged mass gives \(W_1(\mu_\varepsilon,\nu_*)\le\varepsilon D_Y\). The selected \(\varepsilon_Y\) lies strictly inside the assumed neighborhood, including its endpoint.

The triangle inequality (5) is exact with the same initialized arrays. For each fixed \(\nu\), fixed positive \(\varepsilon\), and \(a>0\), the two population-approximation errors divided by that fixed \(\varepsilon\) vanish in probability, as does the P1 derivative error. A union bound is sufficient; independence is unnecessary. Choosing \(\varepsilon\) small enough that \(\omega_Y(\varepsilon)<a/2\) proves exactly

\[
\forall\nu,\ \forall a>0:\qquad
\lim_{\varepsilon\downarrow0}\limsup_{n\to\infty}
\Pr\!\left\{
\frac{\|f_{n,\mu_\varepsilon}-f_{n,*}
 -\varepsilon D_{\nu-\nu_*}f_n\|_\infty}{\varepsilon}>a
\right\}=0.
\tag{C3}
\]

No joint width/\(\varepsilon\) rate follows or is needed. A supremum over \(\nu\) of the finite failure probability does **not** follow, since P1's derivative capture is for separately fixed laws. Thus “exactly the user's display” is valid if its law quantifier is (C3); a stronger unprovided display would require additional hypotheses.

The counterexample \(g_n(\varepsilon)=\varepsilon(1-e^{-n\varepsilon})\) correctly refutes an inference from finite derivatives alone: \(g_n'(0)=0\), whereas the width-first limit equals \(\varepsilon\) for \(\varepsilon>0\). It is not a counterexample to the neural model.

Finally, response-bridge line 96 should render its coefficient as \(-\epsilon\), rather than the literal text “-epsilon.”

## Status after the check

| Claim | Status |
|---|---|
| Exact finite arbitrary-Borel-law GF and energy bounds | Valid |
| Population energy for an existing \(C^1\) raw solution | Valid with loss-gradient sentence corrected |
| Same-carrier raw HS transport estimate | Valid |
| Finite convergence along laws tending to the trained reference | Valid |
| Typed raw observation transfer | Valid with continuous-gate and starting-field clarification |
| Compact P1 response family and compact-direction Taylor lemma | Valid |
| Width-first finite nonlinear remainder | Exact under the explicit population premises, for each fixed law |
| Positive-neighborhood nonlinear population existence/consistency through time 40 | Unproved here |
| Uniform population nonlinear remainder | Unproved here |

Retain these partial lemmas with the local corrections above. No result checked here closes either of the last two obligations.
