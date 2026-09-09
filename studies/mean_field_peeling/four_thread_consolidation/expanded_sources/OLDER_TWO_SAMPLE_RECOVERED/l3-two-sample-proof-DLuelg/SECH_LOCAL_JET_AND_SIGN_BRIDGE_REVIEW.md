# Fresh-context adversarial audit of the sech local jet bridge

Date: 2026-09-06.

**Exact verdict: PASS WITH MINOR CORRECTIONS (SYMMETRY AND DEPENDENCY PROVENANCE), CONDITIONAL ON THE STATED STATIC JET/MOMENT/DENSITY PREMISE.**

I found no substantive analytical gap in the construction of the approximate path, its cap-uniform defects, the comparison argument, or the endpoint probability calculation. There is one literally incorrect symmetry sentence in candidate lines 115–116: the readout multiplier under sample exchange must be `sigma=y_1 y_2`, so it is a sign reversal only for opposite labels. The stated prediction symmetry and subsequent local clock follow from this corrected transformation. This correction does not change the jet formulas or the exponents in (5)–(13). A later version-provenance update also requires refreshing the bridge's static-dependency citation in its next revision; the exact old version actually read remains the basis of this audit.

This verdict certifies a modular implication, not the pending static premise. In particular, this report does **not** certify an unconditional actual-population sign theorem, the static dependency's Gaussian conditioning proof, a global opposite-label continuation, or the final two-label theorem. The pending independent audit cannot be replaced by this report.

## 1. Source identity, complete read scope, and exclusions

The audited candidate is:

`/tmp/l3-two-sample-proof-DLuelg/SECH_LOCAL_JET_AND_SIGN_BRIDGE.md`

It has 381 lines. SHA256 of the candidate bytes read:

`f01a27e434f03c7cfcca22199b929dd3d1dc97ca807c0c9279378d6a5d9f8d82`

Every mathematical dependency used below is explicitly listed in candidate Section 1. Every one was read completely, including portions not imported into the bridge. Read scope and reliance scope are deliberately distinguished below.

| ID | Exact dependency path | SHA256 | Complete read scope | Mathematical reliance in this audit |
|---|---|---|---|---|
| D1 | `/tmp/l3-two-sample-proof-DLuelg/SECH_GATE_ACTIVATION_DESIGN.md` | `c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24` | Lines 1–231, entire file | Section 1: activation bounds, bounded derivatives, initial nondegeneracy. No prescribed fixed-sign characteristic estimate. |
| D2 | `/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md` | `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170` | Lines 1–352, entire file | Sections 1–6: raw two-sample finite Euler law, response induction, both query envelopes, and finite-program applicability. No global fitting inference. |
| D3 | `/tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_GLOBAL_ASSEMBLY.md` | `510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44` | Lines 1–358, entire file | Sections 1–2, lines 32–183, and the symmetry paragraph at lines 187–194. No same-label fitting, physical global comparison, or nontriviality result is imported. |
| D4 | `/tmp/l3-two-sample-proof-DLuelg/SECH_ACTUAL_CONTROL_SIGN_TEST.md` | `0687a11f279d5b6c2436f127fc48f7e7b73bfd51a6c0fa73c7814aaf242da336` | Lines 1–657, entire file | Its stated finite jet identities, joint static program laws and mixed-moment convergence, all finite moments, and density lower bounds are treated as the authorized premise. Their stated scope is checked against the bridge. Neither remainder (A), positive-time derivative identification, nor its conditional physical crossing theorem is assumed. |
| D5 | `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md` | `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e` | Lines 1–1789, entire file | Sections 2–3 and 5: elementary limiting tools, finite Gaussian programs, common bounded actions and actual adjoints. Its transformed-coordinate dynamics and one-sample global conclusions are not imported. |

All five versions actually read, listed above, match candidate Section 1. D5 is not located beside the candidate; the exact path above is supplied by D2, lines 6–8, and D3, lines 18–21. Only the explicitly named file was opened.

### Version-provenance update received after the mathematical read

The user reported that D4 was revised after its first isolated review. A final SHA256 and line-count check confirms that the file currently at the same path has **744 lines** and SHA256:

`43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51`

That revised text was **not read or audited here**. Only its fingerprint and line count were checked. D4 throughout the mathematical discussion and every D4 line citation below refer to the **657-line version actually read in full**, SHA256 `0687a11f279d5b6c2436f127fc48f7e7b73bfd51a6c0fa73c7814aaf242da336`. This audit is not silently reassigned to the revised bytes.

According to the user's provenance update, the static algebra/laws are unchanged; the revision adds explicit raw physical normalization, expands the elementary empirical moment proof, removes an alternative covariance shortcut, and specifies scalar-path continuity. Those descriptions are recorded as user-supplied provenance, not independently verified mathematical conclusions and not additional premises used below. The fresh audit of the revised full text remains separate. No other review was read.

The candidate's final fingerprint still equals `f01a27e434f03c7cfcca22199b929dd3d1dc97ca807c0c9279378d6a5d9f8d82`. D1, D2, D3, and D5 also retain the table's fingerprints. Candidate lines 37–43 now cite a stale on-disk D4 version; required provenance correction R2 records this for the next candidate revision.

The procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read completely; its SHA256 is `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`. It supplied audit procedure, not a mathematical premise.

No ledger, history file, other review, or additional transitive dependency was opened. References to such files and prior audit statuses inside the allowed documents were not used as mathematical evidence. In particular, `EXACT_TWO_SAMPLE_REDUCTION.md`, `CONTRACT_AND_LEDGER.md`, and `GAUSSIAN_BACKWARD_SIGN_TRANSFER.md` were not read or imported. No external mathematical source, specialized external theorem, numerical experiment, or simulation was used. The candidate and dependencies were not edited.

## 2. Required corrections versus optional improvements

### Required correction R1 — specify the label-dependent exchange symmetry

Location: candidate lines 115–120.

The fixed-label symmetry for `y=(1,sigma)` is

\[
\mathcal S_\sigma(Z^{(1)}_1,Z^{(1)}_2,W^{(2)},W^{(3)},w)
 =(Z^{(1)}_2,Z^{(1)}_1,W^{(2)},W^{(3)},\sigma w).
\]

The initialized root law is invariant under sample exchange; the zero readout is invariant under multiplication by `sigma`. The sample-swap matrix commutes with `C`, and exchanging the label entries multiplies the label vector by `sigma`. The backward fields transform as `q_a -> sigma q_{3-a}`; oddness of the cuts then verifies equivariance of both clipped updates. Predictions transform as

\[
(f_1,f_2)\longmapsto(\sigma f_2,\sigma f_1).
\]

Deterministic empirical limiting predictions therefore satisfy `f_2=sigma f_1`, as claimed.

An unconditional readout sign reversal is not a symmetry for the same-label mode. At zero readout with `y=(1,1)`, the readout derivative is `(H^{(3)}_1+H^{(3)}_2)/2>0`; reversing that derivative gives a negative field, whereas evaluation at the exchanged initial state still gives a positive derivative. Thus the existing sentence is literally false in that mode.

Required replacement: say “sample exchange combined with multiplication of the readout by `sigma=y_1 y_2`,” or equivalently “sample exchange, with a readout sign reversal in the opposite-label case.” This is a minor correction to the stated transformation; the desired symmetry itself is valid. Activation parity is not needed for this argument.

### Required correction R2 — refresh the static-dependency version citation

Location: candidate lines 37–43, with the associated pending-audit descriptions at lines 178–180 and 370–375.

The candidate cites D4 SHA256 `0687a11f279d5b6c2436f127fc48f7e7b73bfd51a6c0fa73c7814aaf242da336`, the old 657-line text this audit actually read. The current 744-line file instead hashes to `43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51`. The bridge's next revision should explicitly select and cite the intended dependency version and attach any audit status only to the exact bytes reviewed. If it adopts the current version, update its hash and read provenance accordingly; do not relabel this audit as a full read of that revision.

This is a provenance correction prompted by a subsequent dependency change, not a discovered mathematical change to the premise. The static result remains a premise in this audit, and the revised dependency's independent audit remains pending.

### Optional improvements — no additional mathematical hypothesis needed

1. Expand candidate lines 48–49 with the truncation/common-space explanation in Section 4 below. D5's stated coordinate-program class is globally Lipschitz, whereas some static jet products are not. The supplied static moment premise suffices to bridge this distinction, but it should not be concealed by language suggesting that polynomial products are already globally Lipschitz instructions.
2. State explicitly that all constants in (8)–(12) are independent of `u`, terminal `t` in a fixed sufficiently small interval, and comparison cap, while they may depend on the fixed correlation and label mode. The proofs provide this uniformity.
3. Cite D4, lines 425–432, for the fixed density box used in Section 8. Its statement covers any fixed compact box; this avoids relying on an unspecified neighborhood of `(0,1)` being tall enough to include `T=9/8`.
4. Clarify that (13) is an endpoint sign-reversal probability. The report below explains why it already rules out an almost-everywhere fixed-sign-in-time assertion. A stronger statement about a continuous scalar query hitting zero between these endpoints would need its own path-regularity justification; the bridge does not require that stronger statement.
5. Name the physical inverse clock separately, for example `vartheta(s)`. The physical endpoints are `vartheta(t/2)` and `vartheta(t)`, not necessarily physical times in the ratio one to two.

There are no further required corrections identified by this audit. In particular, the deferred audit of D4 is an explicit premise boundary, not an undisclosed defect charged to this bridge.

## 3. Transfer of the raw local construction to sech

The claimed transfer in candidate Section 2 is supported by the actual arguments in D2 and D3.

D1 proves `|phi|<=7/6`, `|phi'|<=1/10`, `|phi''|<=1/10`, and bounded derivatives of every fixed order. Using the looser constant `1/5` for `|phi''|` is legitimate. D2's raw updates use only these bounds, the odd nonexpansive cuts, the two-sample Gram entries with absolute value at most one, independent initial Gaussian matrices, and zero readout.

In particular:

- D2 Section 3 bounds raw gate variations by `|q||dZ|/5+|dq|/10` and uses the row sum `sum_a |C_ba|/2<=1`. These bounds remain valid for sech and at `rho=-1`.
- D2 Section 4 retains both sample/source indices and uses the same gate bounds. The two update samples cancel the `1/2` in each update; no extra factor of two is lost in the transfer.
- D2 Section 5 retains the learned covariance rows and the current return through the third matrix before estimating the second reverse row. Its constants depend on the preceding bounds, not on an arctangent identity.
- D2 Section 6 needs only `q=zeta+beta`, `|beta|<=7/6`, and the stated marginal Gaussian variances. It does not assume independence of `beta` and `zeta` or independence across time.

Thus the same response induction and exponential-square envelope apply to the sech cut flows. Smooth cut maps at fixed caps admit the bounded-derivative extensions required by D5's finite program argument. Singular source slots are retained by that argument. The raw root pair fits its finite-root-tuple setup even at the antiparallel endpoint.

D3 Sections 1–2 then give the cap-independent primal bounds, the fixed-cap contraction construction, and the asymmetric two-tail comparison. The readout bound is `|w_R(s)|<=as`, valid for both label modes. No positive lower bound on a label-mode output derivative, activation inverse, or prescribed-control estimate is needed.

For completeness, the tail estimate used in that comparison can be checked without importing any additional section of D5. If `E exp(q^2/16)<=2`, then

\[
E[q^2\mathbf1_{|q|>v}]
\le 64e^{-v^2/32},\qquad
\|(|q|-R/2)_+\|_2\le 8e^{-R^2/256}.
\]

Indeed, write `q^2` as `(q^2 exp(-q^2/32)) exp(q^2/16) exp(-q^2/32)` and use the bound `q^2 exp(-q^2/32)<=32`, followed by the assumed exponential moment. There are four reference tails, one for each sample at each reverse layer. Gronwall with coefficient `C(1+R)` gives the asserted form `C exp(CR-R^2/256)`, after absorbing the fixed horizon into constants.

The linear cap dependence is essential and is correct. Top-delta and top-query differences are bounded by `C d` when the reference readout is bounded pointwise. The middle delta costs `C(1+R)d`. The first reverse action preserves that order. At the bottom, its propagated query difference is multiplied by a bounded gate, while the separate gate difference costs `R d`; these are added, not multiplied. The same statement holds for rank-one velocity differences. No competitor tail estimate enters.

The resulting uncut local feature flow and query limits are therefore supported by these scoped dependencies. The argument does not import D3's same-label global fitting conclusion into the opposite-label case.

## 4. Static premise coverage and identification on the flow spaces

### Exact coverage of the jet factors

The main bridge fields correspond to D4's notation as follows. Expectations in each row concern the appropriate neuron population.

| Bridge field | D4 field or direct algebraic consequence |
|---|---|
| `V`, `delta^(3)_[1]` | `V`, `U`, equation (4) |
| `R^(2)`, `delta^(2)_[1]`, `R^(1)` | `R^(2)`, `D`, `R^(1)`, equation (4) |
| `Z^(1)_[2]`, `H^(1)_[2]` | `c C Y P_1 R^(1)`, `F_1`, equations (3)–(5), with D4's `c=1/2` |
| `Z^(2)_[2]`, `H^(2)_[2]`, `Z^(3)_[2]` | `X_2`, `F_2`, `X_3`, equation (5) |
| `H^(3)_[2]`, `V_2` | `P_3 X_3`, `V_2`, equation (6) |
| `delta^(3)_[3]`, `T^(2)` | `F_{3,*}`, `T^(2)`, equations (6)–(7) |
| `delta^(2)_[3]`, `T^(1)` | `F_{2,*}`, `T^(1)`, equation (8) |
| `delta^(1)_[3]`, `Z^(1)_[4]` | Bounded gates multiplying `T^(1)` and the product `Z^(1)_[2] R^(1)`, followed by the fixed matrix `C Y/2` |
| `W^(ell)_[2]`, `W^(ell)_[4]` | Finite rank-one sums of the preceding fields and hidden second jets |

D4, lines 530–546, states all fixed moments and the needed mixed/polynomial empirical convergence for its finite static list. Hölder then supplies the additional finite products in the last two rows. Those rows require no new Gaussian query, no inverse gate, and no operator bound outside `L2`. Consequently the bridge does not ask D4 for an unstated higher forward or reverse Gaussian query law.

The phrase “exactly ... identities from the static-law dependency” at candidate lines 170–171 is compressed: D4 does not separately display every fourth raw derivative. They follow immediately by differentiating its displayed finite field, and the bridge itself gives their formulas. This is not an additional unproved Gaussian premise.

### Why the common-space assertion is supportable

D5 Sections 3 and 5 directly cover globally Lipschitz coordinate instructions. They do not directly authorize untruncated products of two arbitrary unbounded inputs. Nevertheless, the statement at candidate lines 48–49 follows from D4's stated static mixed-moment convergence together with D5's bounded actions, as follows.

Take the finite static jet program and smoothly truncate the inputs to every polynomial-growth coordinate operation at level `M`. The resulting operations are globally Lipschitz. Their Lipschitz constants grow at most polynomially in `M`, because the static operations are finite products of fields and bounded smooth gates. Fixed scalar contractions can be restored as in D2's finite-program comparison.

For an actual static input tuple `X`, a degree-`d` operation and its truncated version differ in `L2` by at most

\[
C\left(E[(1+|X|)^{2d}\mathbf1_{|X|>M}]\right)^{1/2}.
\]

The stated higher static moments make this smaller than any prescribed inverse power of `M`. The corresponding empirical estimate follows from D4's stated moment convergence. Through a fixed finite program, the polynomial losses from Lipschitz constants are absorbed by choosing a sufficiently high moment. Matrix calls cost only the bounded `L2` operator norm. A fixed finite collection of cut-Euler or Lipschitz probe programs can be appended without altering this argument.

Include all these truncated programs and their finite unions in D5's countable common-program construction. Their approximations are Cauchy in the population `L2` spaces by the same-matrix finite comparisons and passage of second moments. The limits have D4's stated joint static laws. Bounded initial operators commute with these `L2` limits, and the transpose pairing identities pass to the limits as well. Thus the static jets are realized by the same initial actions used by the cut and uncut flows.

This supplies the identification needed for the comparison with `P`. It uses the full static joint/moment premise, not just a marginal density for `(R,T)`. That fuller premise is expressly available in D4 and identified in candidate Section 1. Adding this paragraph to the candidate would improve transparency, but no new mathematical assumption is required.

## 5. Product rules and learned-matrix terms

At zero readout, the raw hidden and matrix first derivatives vanish, while `w_[1]=V`. Therefore a hidden scalar gate first changes at order `u^2`, and the first two nonzero backward orders are `u` and `u^3`.

For a top gate, direct multiplication gives

\[
\left(uV+\frac{u^3}{6}V_2\right)
\left(\phi'(Z)+\frac{u^2}{2}\phi''(Z)X\right)
=uV\phi'(Z)
+\frac{u^3}{6}\bigl(V_2\phi'(Z)+3V\phi''(Z)X\bigr)
+O_{L^2}(t^5).
\]

This verifies the factor `3` in the top cubic delta. At the middle and bottom gates, replace `(V,V_2)` by the appropriate `(R,T)` and obtain exactly the other displayed cubic deltas.

For each trained matrix,

\[
\left(W_0^*+\frac{u^2}{2}W_{[2]}^*+\frac{u^4}{24}W_{[4]}^*\right)
\left(u\delta_{[1]}+\frac{u^3}{6}\delta_{[3]}\right)
=uW_0^*\delta_{[1]}
+\frac{u^3}{6}\bigl(W_0^*\delta_{[3]}+3W_{[2]}^*\delta_{[1]}\bigr)
+O_{L^2}(t^5).
\]

The bridge keeps `3(W^(3)_[2])^*delta^(3)_[1]` and `3(W^(2)_[2])^*delta^(2)_[1]`. They coincide with D4's learned terms `3c S_3 Y H_2` and `3c S_2 Y H_1`. Neither repeated initial matrix is replaced by a fresh one.

Similarly,

\[
\delta(u)\otimes H(u)
=u\delta_{[1]}\otimes H
+\frac{u^3}{6}\bigl(\delta_{[3]}\otimes H
+3\delta_{[1]}\otimes H_{[2]}\bigr)+\text{remainder}.
\]

Differentiating `W_P=W_0+u^2 W_[2]/2+u^4 W_[4]/24` gives precisely the matching linear and cubic velocity terms. The sample factor `1/2`, the cubic factor `1/6`, and the fourth-order factor `1/24` are consistent throughout. The fourth raw first-field derivative is also the correct derivative of its label-weighted bottom delta.

All displayed matrix jets are finite sums of rank-one operators. Their operator and Hilbert–Schmidt norms are bounded by products of their factors' `L2` norms. The initial matrices themselves are only assumed bounded; the bridge never needs them to be Hilbert–Schmidt.

## 6. Small-jet tail split

Candidate (5) is valid with exactly the exponent claimed. Write `B=sup_u ||A_u||_infinity`. For `p>=2`,

\[
\begin{aligned}
\|A_uJ_u\|_2
&\le \sqrt t\,\|A_u\|_2
+B\left(E[|J_u|^2\mathbf1_{|J_u|>\sqrt t}]\right)^{1/2}\\
&\le C t^{9/2}+B\|J_u\|_p^{p/2}t^{(2-p)/4}\\
&\le C t^{9/2}+C_p t^{(p+2)/4}.
\end{aligned}
\]

Here `sup_(u<=t)||J_u||_p<=C_p t` follows from the two fixed jets. At `p=16`, the second exponent is exactly `9/2`. Dependence between `A_u`, `R`, and `T` is unrestricted. The estimate is a supremum of `L2` norms; it does not assert a moment bound for a pathwise supremum.

For a cap `K>=1`,

\[
\|\tau_K(J_u)-J_u\|_2
\le 2K^{1-p/2}\|J_u\|_p^{p/2}
\le C_p t^{p/2}.
\]

Taking `p/2>=N` proves (6) with constants independent of the cap. A cut of `J_u` also satisfies the first estimate because its magnitude does not exceed `|J_u|`.

Only static jets need these moments. An evolved query remainder is always handled in `L2` with a bounded gate or a bounded operator. This is the claimed protection against an illicit Gaussian `Lp -> Lp` assertion.

## 7. Bounded-readout approximate path and forward graph defects

For each fixed terminal feature time `t`, (7) defines a different comparison path `P=P_t` on `[0,t]`. The cap `sqrt(t)` is fixed while differentiating in `u`; there is no missing derivative of that threshold.

Since `|V|<=a`, choose `t` with `at<=sqrt(t)/2`. If the readout cut changes a value or its derivative at some `u<=t`, then

\[
\frac{u^3}{6}|V_2|\ge \frac{\sqrt t}{2},
\qquad |V_2|\ge 3t^{-5/2}.
\]

The candidate's bounds for the value and derivative errors on this event are valid. For any fixed `p` and arbitrarily large `m>p`,

\[
\|V_2\mathbf1_{|V_2|>3t^{-5/2}}\|_p
\le C_m t^{(5/2)(m/p-1)}.
\]

Together with the bounded `V` contribution, this proves arbitrarily high powers of `t` for both errors in any fixed `Lp`, uniformly over `u<=t`. It does not use exponential moments of `V_2`.

The readout is bounded pointwise by `2sqrt(t)` and is `C1` into `L2`: its derivative is `tau'_(sqrt(t))(bar w(u))(V+u^2V_2/2)`. Boundedness and continuity of the cut derivative, with the fixed integrable polynomial factors, justify continuity by dominated convergence. The other state components are polynomials in their Banach spaces. Thus `P` is an admissible comparison path even though it need not obey the actual flow's sharper pointwise bound `as`.

All its state norms are bounded independently of small `t` and of the comparison cap. At `rho=-1`, both raw derivative pairs are in the image of `C`, so the exact constraint `Z^(1)_2=-Z^(1)_1` is preserved.

The induction proving (8) also checks out. At layer one, the raw increment is `u^2 X/2+u^4 Y/24`, with static `L4` bounds. Its scalar Taylor remainder therefore has `L2` norm `O(t^4)`. At the next layer, expand

\[
\left(W_0+\frac{u^2}{2}W_{[2]}+\frac{u^4}{24}W_{[4]}\right)
\left(H+\frac{u^2}{2}H_{[2]}+E_H(u)\right),
\qquad \|E_H(u)\|_2\le Ct^4.
\]

The order-two coefficient is exactly the displayed `Z_[2]/2`. Every other term is `O(t^4)` in `L2` by bounded operator norms and fixed vector norms. For the subsequent activation, first compare the recomputed `Z_P` with `Z+u^2 Z_[2]/2` using the Lipschitz bound. Only then Taylor-expand this latter, static-jet expression. Its quadratic Taylor error is controlled by `||Z_[2]||_4^2`.

Repeating this step at layer three proves (8). It never requires an `L4` bound on an operator-applied remainder or an `L4` bound on the full recomputed increment.

## 8. Query graph and velocity defects, uniform in the cap

At the top, replacing `phi'(Z_P^(3))` by `phi'(Z^(3)+u^2 Z^(3)_[2]/2)` incurs a gate error of size `O(t^4)` in `L2`. Multiplication by the clipped approximate readout costs at most `2sqrt(t)`, giving `O(t^(9/2))`. Replacing this readout by its polynomial costs arbitrarily high powers of `t` because the gate is bounded.

The remaining scalar Taylor terms are `O(t^5)` in `L2`. For example, they are bounded by constants times

\[
u^5|V||Z^{(3)}_{[2]}|^2,
\quad u^5|V_2||Z^{(3)}_{[2]}|,
\quad u^7|V_2||Z^{(3)}_{[2]}|^2,
\]

all controlled by static mixed moments. Applying `W_P^(3)*` costs only a bounded `L2` operator norm. Its multiplication with the polynomial delta has the cubic coefficient checked in Section 5; the first omitted matrix terms have degree five. This proves (9) for the top reverse query.

At the middle layer, let `J_2(u)=uR^(2)+u^3T^(2)/6` and let `Z_quad` be its preactivation's quadratic approximation. One useful complete decomposition is

\[
\begin{aligned}
\phi'(Z_P)\tau_R(q_P)
={}&\phi'(Z_P)[\tau_R(q_P)-\tau_R(J_2)]\\
&+\phi'(Z_P)[\tau_R(J_2)-J_2]\\
&+[\phi'(Z_P)-\phi'(Z_{quad})]J_2
+\phi'(Z_{quad})J_2.
\end{aligned}
\]

The four terms are handled respectively by nonexpansiveness and the top-query error; the static cut-tail estimate (6); the bounded small-jet multiplication estimate (5); and a scalar Taylor expansion using static moments. The gate difference in the third term is bounded pointwise by `2||phi'||_infinity` and has `L2` norm `O(t^4)`. No product of an uncontrolled `L2` remainder with an unbounded jet is left over.

Applying `W_P^(2)*` now gives (9) for the first query, including its learned-matrix term. The same decomposition at the first gate proves the bottom velocity expansion. Every constant here is independent of `R>=1`; the proof uses no derivative bound for the cap beyond its first-derivative bound by one.

For the rank-one velocity products, write

\[
\delta_P=D+E_\delta,\quad
D=u\delta_{[1]}+u^3\delta_{[3]}/6,
\quad H_P=H+u^2H_{[2]}/2+E_H.
\]

Then `||D||_2=O(t)`, `||E_delta||_2=O(t^(9/2))`, `||H_P||_2<=a`, and `||E_H||_2=O(t^4)`. The rank-one errors are bounded by

\[
\|E_\delta\|_2\|H_P\|_2+\|D\|_2\|E_H\|_2
+C t^5=O(t^{9/2}).
\]

This works in operator norm and Hilbert–Schmidt norm. It confirms that use of vector `L2` norms, rather than pointwise multiplication of the rank-one factors, is legitimate.

The readout derivative defect is `O(t^4)` by (8) and the negligible derivative clipping error. The first-field and both matrix defects have the stronger order `O(t^(9/2))`. Summing them yields (10), uniformly for every comparison cap `R>=1`.

## 9. Cap selection, comparison, and the actual query remainder

With identical initial states, let `e(u)=d(theta_R(u),P_t(u))`. The checked comparison and defect estimates give

\[
e(u)\le C\int_0^u(1+R)e(v)\,dv+C u t^4.
\]

Consequently

\[
\sup_{u\le t}e(u)\le C t^5e^{C(1+R)t}.
\]

For `R=t^(-1/4)`, the exponent is `C(t+t^(3/4))`, bounded as `t` decreases to zero. The readout of `P_t` is uniformly bounded by two, so the reference-readout constants in this application do not diverge. The cap-independent primal bounds also apply to both states. Thus (11) has a constant independent of small terminal `t`.

The top-query comparison costs `O(t^5)`. The middle-delta and first-query comparisons cost

\[
O((1+R)t^5)=O(t^{19/4}).
\]

Since `19/4>9/2`, these errors are smaller than the approximate graph defect at the required scale. For the cut-removal step, any fixed polynomial in `R` times

\[
\exp(Ct^{-1/4}-t^{-1/2}/256)
\]

is smaller than every fixed power of `t`. The negative quadratic in the cap dominates its linear positive term and all polynomial prefactors. The query cut-removal bounds were checked in Section 3 of this report.

The triangle inequality therefore establishes precisely the conditional estimate

\[
\sup_{0\le u\le t}
\left\|q^{(\ell)}_a(u)-uR^{(\ell)}_a
-\frac{u^3}{6}T^{(\ell)}_a\right\|_2
\le C t^{9/2},\qquad \ell=1,2.
\]

Here the queries are recomputed from the actual uncut local feature flow on the common spaces. The time-dependent cap is only selected after the population comparison estimates have been obtained; no finite Gaussian program with a width-dependent number of queries is invoked. The argument establishes this expansion directly and does not differentiate a width limit or infer a positive-time `C4(Lp)` path.

## 10. Endpoint probability and the local physical interpretation

Under D4's stated density premise, choose a lower density bound `m_*>0` on a fixed compact rectangle containing `[-epsilon,0] x [1,9/8]`. D4, lines 425–432, states the stronger compact-box lower bound needed for this choice. Thus, for the candidate's event,

\[
P(E_t)\ge m_*\left(\frac1{10}-\frac1{12}\right)t^2
\left(\frac98-1\right)=\frac{m_*}{480}t^2.
\]

The deterministic polynomial margins are correct:

\[
J(t)\ge(-1/10+1/6)t^3=t^3/15,
\]

\[
J(t/2)\le(-1/24+3/128)t^3=-7t^3/384.
\]

Both margins strictly exceed `t^3/200` in absolute value. If `C` bounds the remainder norm in (12), the union of the two endpoint bad-error events has probability at most

\[
2\frac{C^2t^9}{(t^3/200)^2}=80000C^2t^3=o(t^2).
\]

No independence between the error and `E_t` is needed: subtract this unconditional bad-event probability from `P(E_t)`. This proves the implication (13), with a positive lower constant and sufficiently small `t`. The argument does not use D4's unproved remainder (A) or replace it by an insufficient `o(t^3)` estimate in `L2`.

After correction R1, prediction symmetry gives `f_a=y_a g` for `y=(1,sigma)`, with continuous deterministic `g` and `g(0)=0`. On a short interval choose `|g|<=1/2` and define the physical inverse clock

\[
\vartheta(s)=\int_0^s\frac{dv}{4(1-g(v))}.
\]

It is strictly increasing and satisfies `s/6<=vartheta(s)<=s/2`. In the physical normalization stated by the candidate and its allowed dependencies, multiplying the feature field by `4(1-g)` gives the two-residual physical field: its sample coefficients are `-2(f_a-y_a)=2(1-g)y_a`, compared with the feature coefficients `y_a/2`. No same-label positive fitting rate is required for this local change of time.

The corresponding physical query endpoints are `vartheta(t/2)` and `vartheta(t)`, which are deterministic and tend to zero. The event probability is unchanged by this reparametrization. Residual and label factors have fixed nonzero signs on the short interval, so multiplying by them preserves a sign reversal, possibly reversing its orientation. The same observation applies to globally reversing both labels. This does not assert the stronger physical-time formula with endpoints exactly `T/2` and `T`.

For precision about the fixed-sign discriminator, the constructed queries are continuous into `L2`: forward fields are continuous, the readout is pointwise bounded, and multiplying a fixed `L2` factor by converging bounded gates preserves `L2` convergence by truncation. Bounded current adjoints preserve that continuity through both reverse actions. Suppose a measurable sign `s(omega)` made `s(omega)q(u,omega)>=0` for almost every `(u,omega)` on the interval. The cone `{v in L2: sv>=0}` is closed. Since the continuous `L2` path lies in it for almost every time, it lies in it at every deterministic time. Opposite signs at the two endpoints on a set of positive probability contradict that assertion. Thus the conditional endpoint result is sufficient for the fixed-sign obstruction even without an additional theorem giving continuous scalar versions of the query paths.

No statement about a common neuron set crossing at every small time, infinitely many crossings of an individual neuron, simultaneous crossings at different layers, independence of antiparallel first coordinates, or constants uniform in `rho` follows or is needed.

## 11. Final claim boundary

The following modular implication survives the audit: the permitted raw local construction, combined with the stated joint static jet and moment premise on the same initial operator spaces, yields the actual local feature-query `L2` remainder of order `t^(9/2)`; adding the stated density premise yields the endpoint sign-reversal probability of order at least `t^2`. Required corrections are the label-dependent symmetry transformation in R1 and the dependency-version provenance in R2. The mathematical audit used the old 657-line D4 version in the source table; the revised 744-line text was not read.

The Gaussian jet/moment/density result remains an invoked premise under its separate independent audit. This report neither certifies that premise nor promotes the resulting conditional sign obstruction to an unconditional actual sign theorem. It makes no assertion about completion or failure of the final global two-label theorem.

**Exact verdict: PASS WITH MINOR CORRECTIONS (SYMMETRY AND DEPENDENCY PROVENANCE), CONDITIONAL ON THE STATED STATIC JET/MOMENT/DENSITY PREMISE.**
