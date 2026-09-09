# Independent adversarial audit of the local raw-jet bridge

Date: 2026-09-06.

Verdict: **PASS within the exact modular scope below, conditional on the stated static jet/moment/density theorem. No required mathematical correction found.** This verdict does not certify the proof of that static theorem, its pending audit, or a global two-label mean-field theorem.

## 1. Isolation, exact sources, and premise boundary

The audited candidate is `/tmp/l3-two-sample-proof-DLuelg/SECH_LOCAL_JET_AND_SIGN_BRIDGE.md`, 433 lines, SHA256:

`65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8`.

It exactly matches the version specified in the audit request. Candidate line references below refer to these bytes.

The candidate and all five mathematical dependency files explicitly named in its Section 1 were read completely, including portions outside the imported scope. The source manifest is:

| Mathematical source | Lines | SHA256 |
|---|---:|---|
| `/tmp/l3-two-sample-proof-DLuelg/SECH_LOCAL_JET_AND_SIGN_BRIDGE.md` | 433 | `65fab11c5892afe517fe4289450f0736bb137bb1a118e85f8ea8541e18a017f8` |
| `/tmp/l3-two-sample-proof-DLuelg/SECH_GATE_ACTIVATION_DESIGN.md` | 231 | `c0f67365fbe36af74db9708ce8a32018b30d8164e77c50b068f71299045e4f24` |
| `/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md` | 352 | `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170` |
| `/tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_GLOBAL_ASSEMBLY.md` | 358 | `510fd019c204e0e89e0c6bcb99c031a11de974b05323df1c016c72b263f64a44` |
| `/tmp/l3-two-sample-proof-DLuelg/SECH_ACTUAL_CONTROL_SIGN_TEST.md` | 744 | `43c2e8422f3973a883e4dcab86509bfe97b91a5a001c8189b198c69642f53e51` |
| `/tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md` | 1789 | `bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e` |

The last file is located at the absolute path given by the bootstrap and assembly; it is not present under the candidate's directory. Its hash agrees with the candidate. All source hashes were checked again after reading and before writing this report.

No other review, history, ledger, reduction file, or recursively cited mathematical file was opened. Statements about earlier audit outcomes appearing inside the permitted sources were not treated as evidence. No experiment, numerical simulation, external search, specialized external theorem, or candidate edit was used. The only newly written artifact is this report.

The procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read in full; its SHA256 is `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`. It supplied proof-checking procedure, not an additional mathematical premise.

### Exact imported scope

- Activation design: the explicit activation bounds and initial nondegeneracy. The prescribed fixed-sign characteristic theorem is not imported.
- Short response bootstrap: its finite two-sample, two-cut Gaussian Euler construction and the response estimates on feature time `[0,3/2]`, checked for transfer to the sech activation.
- Same-label assembly: Sections 1–2 and the initial symmetry paragraph of Section 3 only. No same-label fitting, all-time clock, finite physical GD/GF convergence, or nontriviality claim from later sections is imported.
- Standalone proof: the elementary limiting tools, finite Gaussian program argument, and common bounded actions/adjoints construction in Sections 2–3 and 5. Its one-sample coordinate change, response estimates, global theorem, and nonfreezing conclusions are not imported. Where an elementary estimate is needed below, it is derived directly.
- Static sign test: its stated initial query identities, joint static laws, finite mixed moments and empirical moment convergence, and density lower bounds are accepted as the user-authorized premise. Its physical normalization is explicitly available in its Section 2. Its positive-time premise (A), population derivative identification, scalar-path continuity assumption, and conditional physical endpoint theorem (B) are not assumed.

In particular, this is an audit of the new implication from the static theorem to the actual local query remainder and sign obstruction. It is not a second audit of the Gaussian-conditioning proof inside the static source.

## 2. Required and optional findings

### Required findings

None. I found no missing mathematical hypothesis or invalid estimate that prevents the candidate's stated local implication, under the authorized static premise.

The pending status of the static theorem is a boundary of this verdict, not a newly discovered defect. A later failure or weakening of that theorem would require checking the interface again.

### Optional clarifications

**O1 — Make the countable skeleton explicit (candidate lines 61–80).** One can say that truncation levels are positive integers and initially include rational meshes/caps and a countable dense family of probe maps, with real parameters obtained by the approximation argument already supplied in the standalone proof's Section 5. The existing reference to its countable construction supports this interpretation. It is not necessary to place literally every real-parameter program into a countable list.

**O2 — Cite the stronger density statement at its point of use (candidate lines 205–207 and 376–382).** The static source's opening summary promises a neighborhood of `(0,1)`, whereas the candidate uses the particular interval `1 <= T <= 9/8`. Static-source lines 464–471 explicitly supply lower bounds on any fixed compact box, so the chosen interval is justified. Citing those lines would avoid the appearance that an unspecified neighborhood is automatically at least `1/8` tall. This is not a missing hypothesis in the present source version.

Neither optional item changes an estimate, a theorem hypothesis actually needed here, or the verdict.

## 3. Does the bridge request more than the static theorem supplies?

No. The required static information is stronger than just a two-dimensional marginal density, but the complete stated premise supplies it.

1. The bridge needs the initial forward fields, the two initial reverse queries, the second raw/feature coefficients, the cubic reverse inputs and outputs, and their same-population joint laws. These are the finite query program in static-source Sections 2–5.
2. It needs arbitrarily high but finite moments of that fixed list, including mixed products. Static-source lines 568–571 and 626–634 state precisely these moment and joint empirical convergence conclusions. The bridge never needs a bound uniform over the order of the moment or over an increasing number of queries.
3. It additionally defines the bottom cubic delta, the fourth raw bottom coefficient, and the fourth matrix coefficients. These are bounded-gate polynomial operations and rank-one constructions on the already supplied list. They require no new Gaussian matrix call. For example,

   `delta^(1)_[3] = phi'(Z^(1)) T^(1) + 3 phi''(Z^(1)) Z^(1)_[2] R^(1)`.

   Hölder's inequality and the supplied joint moments give every finite moment of this field. The raw `Z^(1)_[2]` is computed directly from `C`, the gate, and `R^(1)`; the argument does not recover it by dividing by a small gate.
4. It needs the static coefficients realized with the same operators as the flow, not merely random variables with matching marginal distributions. This is a new obligation, addressed by candidate Section 1 and checked in Section 4 of this report. It is not silently demanded from the static theorem alone.
5. For the crossing event it needs a positive density lower bound on a fixed box containing the thin rectangles used as `t` decreases. Static-source lines 464–471 supply this. Neither independence of `R` and `T` nor independence of either coefficient from a remainder is used.

The bridge does not use the static source's physical cubic formula to infer a positive-time derivative of a limiting path. Its coefficients remain formal static coefficients until the comparison proves the actual feature-time approximation.

## 4. Common-space polynomial truncation

Candidate lines 61–81 address a real issue: products such as a gate times an unbounded static query do not define globally Lipschitz maps of all their inputs. The proposed truncation resolves it.

Here is the finite-program comparison underlying the paragraph. Let `X_j^n` denote a node of the original static program and `X_{j,M}^n` its smoothly truncated version, coupled using the same roots and matrices. For a coordinate operation `F` with polynomial growth of degree at most `d`, its truncated map `F_M` has a Lipschitz bound `C M^k` for some finite `k`. At the exact, untruncated input tuple `X`,

`|F_M(X)-F(X)| <= C(1+|X|)^d 1_{|X|>M}`,

up to harmless fixed rescaling of the cutoff threshold. For `q>2d`,

`||F_M(X)-F(X)||_2 <= C M^{-(q-2d)/2} (E(1+|X|)^q)^(1/2)`.

The same inequality holds for the normalized empirical norm. Its final empirical moment is bounded in probability by the stated static moment convergence. Thus no convergence theorem for a discontinuous tail indicator is needed.

Split the propagated error as

`F_M(X_M)-F(X) = [F_M(X_M)-F_M(X)] + [F_M(X)-F(X)]`.

The first term costs the polynomial Lipschitz constant, and the second term is the static tail just bounded. Every matrix action or transpose costs at most the common finite operator bound, on the event whose probability tends to one. A scalar contraction is controlled by

`|E UV - E U_tilde V_tilde| <= ||U-U_tilde||_2 ||V||_2 + ||U_tilde||_2 ||V-V_tilde||_2`,

with the identical empirical inequality. Static norms are bounded in probability; the induction bounds the truncated norms as well.

There are finitely many nodes. The product of all relevant Lipschitz losses is only a fixed power of `M`. Taking the static moment orders sufficiently high makes the final error `O(M^{-N})` for any prescribed fixed `N`, after the width limit. This argument uses no higher-moment mapping property of a Gaussian operator and no inverse-Gram bound beyond the accepted static theorem.

For fixed `M`, each truncated program belongs to the Lipschitz program class of the standalone proof. Finite unions with other truncations, cut-Euler programs, and permitted probes have joint deterministic limits. Passing the same-width second-moment comparisons gives, on the common spaces,

`||X_M-X_L||_2 <= C_N(M^{-N}+L^{-N})`

for the relevant output fields. Hence their limits exist in `L2` and have the joint static laws by approximation. Coordinate identities pass by convergence in probability and continuity; matrix identities pass by the bounded `L2` actions. Finite transpose pairings pass by strong `L2` convergence.

The separate population spaces are respected throughout. The operators obtained from the countable finite-program laws therefore act on these static limits exactly as required by the jet identities and the flow. This is sufficient joint realization; merely coupling independent copies of the static marginal laws would not have been sufficient.

## 5. Transfer of the local construction and cap estimates

### Activation and finite response proof

For the new activation,

`phi'(z) = sech(z)/10`,

`phi''(z) = -sech(z)tanh(z)/10`.

The activation source gives `|phi| <= 7/6`, `|phi'| <= 1/10`, `|phi''| <= 1/10`, and bounded derivatives of every fixed order. These imply all three bounds used by the bootstrap, with its looser second-derivative constant `1/5`.

I checked the causal response induction against those uses. The bottom sensitivities use the row-sum bound `sum_a |C_ba|/2 <= 1`, the gate bound, and the cut derivative bound. The middle and top recursions use the same bounds and `|W^(4)(s)| <= as`. The two-sample Gaussian maximum estimate and Jensen in time require no temporal independence. The induction closes the current top response before using it in the current middle response; it does not assume the current bottom bound prematurely.

Consequently the numerical bounds `V_k <= 3067/3200`, `U_k < 97/100`, and `|A^(ell)_{ka,rb}| < (3/2) Delta/2` retain their justification. No arctan-specific identity, positive lower gate bound, or inverse change of the first coordinate occurs in this part of the bootstrap. The Gaussian root pair may be singular at `rho=-1`.

The Gaussian-plus-bounded-response description then gives the same exponential-square envelope for both named reverse queries. Fixed-cap Euler convergence and Fatou transfer it to every fixed flow time. This is a supremum of expectations with uniform constants; it does not assert an expectation of a time supremum.

### State comparison and local uncut construction

For states `A,B` with the stated primal bounds and bounded reference readout `w_B`, use

`w_A phi'(Z_A) - w_B phi'(Z_B)`

`= (w_A-w_B) phi'(Z_A) + w_B[phi'(Z_A)-phi'(Z_B)]`.

This gives top-delta and top-query differences bounded by `C d(A,B)`. The bounded pointwise factor is the reference readout, so no pointwise hypothesis on the other readout is hidden here.

At the middle layer,

`||delta_R^(2)(A)-delta_R^(2)(B)||_2`

`<= e ||q^(2)(A)-q^(2)(B)||_2 + 2Rc ||Z^(2)(A)-Z^(2)(B)||_2`.

An adjoint action gives the same `C(1+R)d` bound for the first query. At the bottom, the propagated query difference again has coefficient at most `e`; the separate bottom gate difference costs `R`. These contributions add. They do not multiply into `R^2`. Rank-one velocity differences obey the same bound because their norms are products of separate `L2` norms.

This checks candidate (3) and its use in Picard construction on the closed class of paths with bounded readout. The cap-independent primal bounds follow successively from readout, top matrix, middle matrix, and bottom velocity bounds. The assembly's local construction therefore transfers to both label modes.

For cap removal, with `R' >= R`, split the middle and bottom differences into a query difference, a reference gate difference multiplying `tau_R`, and the cap difference evaluated at the reference query. The last is bounded by `4 b_R(q_B)`, where `b_R(q)=(|q|-R/2)_+`. This gives the asymmetric field estimate with coefficient `C(1+R)` and only reference tails.

The envelope implies the claimed tail rate directly. If `E exp(q^2/16) <= 2`, then

`E[q^2 1_{|q|>v}] <= 64 exp(-v^2/32)`.

Indeed factor `q^2 exp(-q^2/32)`, bounded by `32/e`, from `exp(q^2/16) exp(-q^2/32)` on the tail. Thus

`||b_R(q)||_2 <= 8 exp(-R^2/256)`.

There are four reference tails, one for each layer/sample pair. Their sum is at most `32 exp(-R^2/256)`. Gronwall on `[0,3/2]` gives candidate (2), with finite constants absorbed into `C exp(CR-R^2/256)`. Top queries converge by top stability; middle deltas and first queries acquire at most the additional polynomial factor in `R`. The actual uncut velocities converge as well. No uncut-competitor tail bound is used.

These estimates support local existence, uniqueness among the bounded-primal integral competitors in the imported construction, and restart from reached feature states. They do not supply opposite-label global physical continuation.

## 6. Exact label-dependent symmetry and physical normalization

Let `S` exchange the two sample indices and let `y=(1,sigma)`. Transform a finite state by exchanging its first sample fields, keeping the hidden matrices fixed, and replacing the readout by `sigma w`.

The forward fields exchange. The deltas and reverse queries transform as `delta_a -> sigma delta_{3-a}` and `q_a -> sigma q_{3-a}`. Oddness of the cuts is exactly what is needed to preserve this rule for clipped queries. Since `y_{3-a}=sigma y_a`, the sums in each matrix update are unchanged, the readout update transforms correctly, and the bottom equation transforms by sample exchange. The latter also uses `SC=CS`.

The initialized Gaussian pair is exchangeable, including when `rho=-1`; the zero readout and independent matrix initialization are invariant under this transformation. Therefore the prediction pair has the same law as `(sigma f_2,sigma f_1)`. A deterministic finite-program limit must equal its transform. Hence `f_2=sigma f_1`, first for the cut construction and then after cut removal. This is not a claim of finite samplewise equality.

For same labels the readout is unchanged. For opposite labels it is reversed. No parity identity for the activation is used in this symmetry argument.

Now `g=(f_1+sigma f_2)/2=f_1`, so the residuals are exactly

`r_a=(g-1)y_a`.

The physical raw equations explicitly recorded in the static source use coefficients `-2 r_a`, whereas the feature field uses `y_a/2`. Thus on this constructed curve the physical field is

`4(1-g) V_infinity`.

This verifies the factor `4`, including the opposite-label case. Continuity and `g(0)=0` are sufficient for a local increasing clock; no fitting estimate is used. A simultaneous global label reversal reverses the readout and queries and preserves the sign-change obstruction, with endpoint orientation reversed under that particular coupling.

## 7. Raw polynomial jets and factorials

At zero readout all hidden first derivatives and the deltas vanish, and the first readout coefficient is `V`. The even hidden/odd readout structure can be checked either by differentiation or by the finite field's invariance under reversing feature time and readout sign.

Differentiating the feature equations once gives the second raw and matrix coefficients in candidate lines 167–174. In particular `Z^(ell)_[2]` contains both `W^(ell)_[2] H^(ell-1)` and `W^(ell)_0 H^(ell-1)_[2]`; lower-layer motion is retained.

For a gate `p=phi'`, the cubic coefficient in the top delta is

`V_2 p(Z) + 3 V p'(Z) Z_[2]`.

For a backward action, expansion of

`(W_0 + u^2 W_[2]/2 + ...)^* (u delta_[1] + u^3 delta_[3]/6 + ...)`

gives cubic derivative `W_0^* delta_[3] + 3 W_[2]^* delta_[1]`. Both instances of this trained-matrix term are present. The middle and bottom cubic deltas have the correct extra `3 phi''(Z) Z_[2] R` term.

Finally the coefficient of `u^3/6` in the matrix velocity is

`delta_[3] tensor H + 3 delta_[1] tensor H_[2]`.

Integrating it produces `u^4 W_[4]/24`, exactly as in the raw path. The bottom coefficient is obtained from the same cubic delta with the factor `C_ba y_a/2`. No factorial or label factor is missing.

The finite matrix convention `UV^T/n` agrees with the population map `B -> U E[VB]`, whose operator and Hilbert–Schmidt norms are `||U||_2 ||V||_2`. The increments are therefore well-defined finite-rank operators. At `rho=-1`, the bottom coefficients lie in `range C = span(1,-1)`, so the path preserves the raw first-field constraint.

## 8. Small-jet multiplication and bounded-readout path

### Multiplication estimate

For `J_u=uR+u^3T/6`, the static moments give `sup_{u<=t} ||J_u||_p <= C_p t`. If `A_u` is pointwise bounded and `sup ||A_u||_2 <= Ct^4`, then on `|J_u| <= sqrt(t)` the product norm is at most `Ct^(9/2)`. On its complement,

`||J_u 1_{|J_u|>sqrt(t)}||_2`

`<= (E|J_u|^p)^(1/2) t^{(2-p)/4} <= C_p t^{(p+2)/4}`.

The boundedness of `A_u` controls that contribution. At `p=16` its power is already `9/2`. Dependence between `A_u` and `J_u` is unrestricted. A cut of `J_u` satisfies the identical bound by domination.

For any cap `K>=1`, the separate cutoff error satisfies

`||tau_K(J_u)-J_u||_2 <= 2 K^{1-p/2} ||J_u||_p^{p/2} <= C_p t^{p/2}`.

Choosing `p>=2N` proves (6) uniformly in the cap. This is a bound for the static polynomial, not an assertion of small evolved-query tails.

### Readout cutoff

The comparison path depends on a fixed terminal `t`; both `sqrt(t)` and the eventual comparison cap are held fixed while `u` runs over `[0,t]`. There is no derivative of a time-varying cutoff threshold.

Since `|V|<=a` and `at<=sqrt(t)/2` for sufficiently small `t`, a changed value or derivative of the readout cut implies

`|V_2| >= 3 t^(-5/2)`.

For fixed `p` and any `q>p`,

`||V_2 1_{|V_2|>3t^(-5/2)}||_p <= C_{p,q} t^{(5/2)(q/p-1)}`.

The bounded `V` contribution is controlled by the probability of the same event. Applying these inequalities to the value error and derivative error displayed in candidate lines 268–269 proves arbitrary fixed powers of `t` in every fixed `Lp`. All constants may depend on the chosen exponent. No pointwise bound on `V_2` is assumed.

For each fixed terminal `t`, the readout path is `C1` into `L2`: the bounded scalar derivative of the cutoff and the polynomial `L2` derivative justify the curve chain rule by dominated convergence. The remaining raw state components are polynomial paths. Their primal bounds and the pointwise bound `2sqrt(t)` on the readout are uniform for small terminal `t`.

### Forward graph residuals

The first raw field has its exact polynomial expansion. At layer one the Taylor remainder uses static `L4` bounds of its coefficients. At each subsequent layer, multiply the already obtained feature expansion by `W_P`; every discarded operator/vector term is `O(t^4)` in `L2`. The quadratic coefficient is exactly the previously defined static `Z_[2]`.

Crucially, to expand the next activation, first replace this recomputed preactivation by `Z+u^2 Z_[2]/2` using the global Lipschitz bound of `phi`. Only then apply scalar Taylor expansion, whose remainder is bounded by `C u^4 |Z_[2]|^2`. This uses a static `L4` norm. It does not apply a Gaussian operator to an `Lp` remainder and subsequently assume an `Lp` bound for its output.

This proves both parts of (8), uniformly in `u<=t`. The argument deliberately needs no fourth-order hidden-field coefficient with higher moments.

## 9. Cap-uniform backward graph and velocity residuals

Write `D_{ell}(u)=u delta^(ell)_[1]+u^3 delta^(ell)_[3]/6` for the relevant static delta polynomial.

At the top, replacing the recomputed preactivation by its quadratic approximation changes the gate by `O(t^4)` in `L2`. Multiplication by the bounded comparison readout costs at most `2sqrt(t)`, yielding `O(t^(9/2))`. After that replacement, removing the readout cutoff costs arbitrary powers because the gate is bounded.

Scalar Taylor expansion of the gate against `uV+u^3V_2/6` gives `D_3(u)+O_L2(t^5)`. For instance its quadratic gate remainder times the readout is bounded by products of `u^5 V Z_[2]^2` and `u^7 V_2 Z_[2]^2`; the other discarded cross term has order `u^5 V_2 Z_[2]`. All their norms follow from static moments. Applying `(W_P^(3))^*` yields the top query polynomial with the correct trained-matrix term, with an `O(t^(9/2))` total error.

For the middle delta, let `J` be that query polynomial, let `p_P=phi'(Z_P^(2))`, and let `p_Q=phi'(Z^(2)+u^2 Z^(2)_[2]/2)`. A useful exact split is

`p_P tau_K(q_P) - p_Q J`

`= p_P[tau_K(q_P)-tau_K(J)] + (p_P-p_Q)tau_K(J) + p_Q[tau_K(J)-J]`.

The first term is controlled by bounded `p_P` and the cutoff's Lipschitz constant one. The second uses (5): its gate difference is bounded pointwise and `O(t^4)` in `L2`, and `|tau_K(J)|<=|J|`. The third uses (6) and bounded `p_Q`. Every constant is independent of `K>=1`. Taylor expansion of the remaining static product gives `D_2(u)+O_L2(t^5)`. Applying `(W_P^(2))^*` proves (9) for the first query. The same split at the bottom proves the bottom velocity expansion.

For matrix velocities, write a delta as `D_ell+e_delta` and the preceding feature as `H+u^2H_[2]/2+e_H`. Then

`||e_delta tensor H_P|| <= C t^(9/2)`,

`||D_ell tensor e_H|| <= C t * t^4 = C t^5`.

The polynomial cross terms beyond cubic order are also `O(t^5)`. Keeping the cubic terms gives exactly the fourth matrix coefficients in (4). This argument uses separate `L2` norms for the two populations, so it does not require a pointwise product estimate between the rank-one factors. It works in Hilbert–Schmidt norm too.

The readout derivative is its polynomial derivative up to negligible error, whereas its recomputed velocity is `V+u^2V_2/2+O_L2(t^4)`. It is therefore the weakest component of the velocity defect.

| Quantity | Uniform bound on `0<=u<=t`, all comparison caps `K>=1` |
|---|---|
| Forward raw/feature error after quadratic terms | `O(t^4)` in `L2` |
| Top delta and top query error after cubic terms | `O(t^(9/2))` in `L2` |
| Middle delta and first query error after cubic terms | `O(t^(9/2))` in `L2` |
| Bottom raw velocity defect | `O(t^(9/2))` in `L2` |
| Each trained matrix velocity defect | `O(t^(9/2))` in operator norm and HS norm |
| Readout velocity defect | `O(t^4)` in `L2` |
| Total state velocity defect | `O(t^4)` |

Thus (9)–(10) are justified without any higher-moment claim about a recomputed or evolved Gaussian-query remainder.

## 10. The cap choice and actual-query remainder

Use `K=t^(-1/4)` to distinguish the deterministic comparison cap from the random slope `R`. The paths start at the same raw state. Integrating the uniform velocity defect over length `t` and applying (3) yields

`sup_{u<=t} d(theta_K(u),P(u)) <= Ct^5 exp(C(1+K)t)`.

Here `(1+K)t=t+t^(3/4)` is bounded and tends to zero. The comparison reference readout can be that of `P`, bounded by `2sqrt(t)<=2`, so the constant does not diverge with terminal time. This verifies (11).

The top query comparison costs `C t^5`. The middle delta and first query comparison cost at most

`C(1+K)t^5 = O(t^(19/4))`.

Since `19/4 > 9/2`, this is smaller than the approximate-path query defect.

At this cap, every polynomial multiple of the cut-removal bound has the form

`C t^(-m/4) exp(Ct^(-1/4)-t^(-1/2)/256)`.

For small `t`, the positive exponent is at most half the magnitude of the negative one. The resulting `exp(-t^(-1/2)/512)` dominates every fixed power, even after the prefactor. Consequently both state and query cut-removal errors are negligible at the required order.

A triangle inequality now gives, for each named layer and sample,

`sup_{0<=u<=t} ||q^(ell)_a(u)-uR^(ell)_a-u^3T^(ell)_a/6||_2 <= Ct^(9/2)`.

This is (12) for the actual uncut feature solution. It is a supremum of `L2` errors, not an `L2` bound on a pathwise supremum; the former is exactly sufficient below. No interchange of width limits and time derivatives is used, and no `C4` population path is inferred or needed.

## 11. Event probability and physical/a.e.-time meaning

### Thin event and endpoint errors

Fix one layer/sample pair. A compact-box density lower bound `m_0>0` gives

`P(E_t) >= m_0 * (t^2/60) * (1/8) = (m_0/480)t^2`.

The candidate's rectangle is therefore of the claimed order. On it,

`J(t) >= (-1/10+1/6)t^3 = t^3/15`,

`J(t/2) <= (-1/24+9/384)t^3 = -7t^3/384`.

Both margins exceed `t^3/200` in magnitude. At each of the two deterministic endpoints, squared `L2` error is at most `C t^9`. Markov and the union bound give

`P(either endpoint error > t^3/200) <= C' t^3 = o(t^2)`.

Subtracting this unconditional bad-event probability from `P(E_t)` proves (13). No conditional remainder estimate, coefficient/remainder independence, or conditioning on `R=0` is required.

### Physical time

On an interval with `|g|<=1/2`, the clock derivative satisfies

`1/6 <= vartheta'(s)=1/[4(1-g(s))] <= 1/2`.

It is a deterministic strictly increasing change of time, with `s/6 <= vartheta(s) <= s/2`. The same population variables and event occur at physical times `vartheta(t/2)` and `vartheta(t)`. The candidate correctly does not identify them with a prescribed physical pair `(h/2,h)`.

The physical residuals are `(g-1)y_a` and retain nonzero signs. Multiplication by a residual, its negative, a constant label, or the strictly positive activation gate preserves the existence of a sign reversal, though it may reverse its orientation. The argument concerns the named query/control components; it does not assert a sign reversal for every sum entering a parameter velocity.

### Fixed signs almost everywhere in time

The constructed queries are continuous as `L2`-valued paths. For the top delta, split a readout difference and a fixed old readout times a gate difference; bounded gates and convergence in probability control the latter by truncating its fixed `L2` factor. Apply operator continuity. Repeat this bounded-gate product argument at the middle delta and the next adjoint. This proves the asserted query continuity without a scalar continuous representative.

If a measurable `b(omega)` taking values in `{−1,1}` made `b q(u,omega)>=0` for almost every `(u,omega)`, the negative-part map is 1-Lipschitz on `L2`, so

`u -> ||(bq(u))_-||_2`

would be continuous. Fubini makes it zero for almost every `u`; continuity makes it zero at every deterministic `u`. At the two endpoints, outside the union of two null sets, the signed queries would both be nonnegative. Their strictly opposite signs on the positive-probability event (13) contradict this.

There is no measurable-selection gap if the sign is initially described path by path: the continuous `L2` path admits a jointly measurable representative, and its time integral is finite almost surely by `L2` integrability on a finite interval. On a path that has one sign almost everywhere, the sign of that integral selects it; zero integral means the path is zero almost everywhere. Assigning `+1` there gives a measurable selection. The local clock and its inverse have bounded derivatives, so time-null sets are also preserved under the physical reparametrization.

This excludes an almost-sure fixed-sign assignment on any initial interval of positive length. It does not rely on arbitrary values assigned at two exceptional times. It also does not assert a scalar intermediate-value zero crossing for `q^(1)` without further scalar-path regularity.

## 12. Exact certified conclusion and exclusions

Under the stated static theorem, the transferred local construction and the new comparison argument establish the actual uncut feature-flow estimate (12) and the positive-probability sign event (13), separately for each of the two reverse-query layers and each sample, for both normalized label modes `y=(1,sigma)` and every fixed `rho in [-1,1)`. Global label reversal preserves the obstruction. Constants and the sufficiently small time interval may depend on the correlation and label mode; no uniformity as `rho` approaches an endpoint is claimed.

The same event survives at the corresponding deterministic local physical times and rules out the assertion that almost every neuron has a fixed sign almost everywhere in time. It does not say that almost every neuron changes sign. At `rho=-1`, the statement is about the named query components on their respective neuron populations and is compatible with the exact one-field constraint on the bottom raw pair.

This report does not certify: the internal proof of the pending static theorem; its premise (A); the exact physical-time endpoint ratio in its separate statement (B); a common event on which all four queries cross simultaneously; infinitely many crossings of one neuron; scalar continuity or an intermediate zero for the first query; finite-width physical GF/GD convergence; all-finite-time opposite-label continuation; or the complete two-label theorem and its nonlinear/nonfreezing conclusions.

The rigorous-math procedure influenced this audit by requiring the joint-realization interface, every use of high moments, the cap losses, and the almost-everywhere quantifiers to be checked explicitly. Within that scope, none of those checks produced a required correction to this candidate version.
