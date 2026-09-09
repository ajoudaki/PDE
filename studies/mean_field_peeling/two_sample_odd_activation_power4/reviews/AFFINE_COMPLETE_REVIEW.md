# Independent complete mathematical review: affine emphasis

Date: 2026-09-07. Verdict: **PASS for the complete stated odd two-input theorem with `0 < e <= c_poly delta^4` and the unchanged explicit `c_poly`.**

This is a fresh proof audit of the four candidate files and the original mathematical interfaces they invoke. I read all four candidate files completely, checked the relevant original mathematical sources directly, and recomputed all four candidate and 23 dependency SHA-256 digests. No historical/sibling review, status assessment, evidence ledger, or prior review certificate was used as evidence. The dependency titled `AFFINE_SOURCE_CERTIFICATE.md` was read as a mathematical derivation of source identities and normalization. I ran no numerical experiment, spawned no agent, changed no proof/dependency file, and made no commit. The rigorous-math skill informed the audit.

The pass is for the final hashes recorded below, including the explicit placement of the terminal-time maximum outside expectation in the backward defect estimate. It covers the full original odd theorem, not merely the affine calculation or a conditional response lemma. No unresolved mathematical objection was found in that chain.

## 1. Exact scope and source boundary

The authoritative model is `two_sample_odd_activation_theorem/PROOF.md`, Sections 1–2. Inputs have squared norm `d`; all four binary label pairs are allowed; `|rho| <= 1-delta`, `0<delta<=1`; one activation `az+e atan(z)` is used at all three hidden layers; `1/2<=a<=1`; there are no biases or offsets. All parameter blocks are trained with the stated raw metric. The finite initial readout is iid `N(0,n^-2)` and is retained. Raw GD is simultaneous raw Euler at `eta_n=n^-2`, with hidden quantities recomputed from raw interpolation.

The verified scope includes a single autonomous global strong population path on canonical generated action spaces, uniqueness against nonsymmetric bounded-primal strong competitors on those spaces, and continuation from reached states. It includes full-width-sequence joint convergence in probability of GF and GD on every fixed finite physical interval; both orientations and actual adjoints of the initialized/trained actions on generated probes; all four raw kernels including off-diagonal sample entries; same-layer two-sample preactivation/feature path laws in `W2(C)`; the stipulated uniform-time and finite-time-tuple velocity laws; second moments and integrated squared speeds. It also includes positive activation-regression error at every finite physical time, all initial hidden-block/sample/layer acceleration certificates, and the changing projected kernel.

The theorem does not assert one positive coefficient for every `delta>0` at once, endpoint coverage, arbitrary-state local existence on all of `L2`, cross-layer neuron pairing, continuous-path velocity laws, uniform convergence over datasets or the infinite half-line, or a three-input extension. The broader aspiration in the attached historical contract is explicitly distinguished from the later odd theorem's separated-input quantifiers. This is no hidden weakening of the theorem actually claimed by the candidate.

The new proof replaces the previous source-response estimates. In particular, applying the downstream arguments does **not** require the old `delta^10`, `delta^800`, or exponentially small original response threshold. The primal comparison restriction retained from the quantitative source is only `e<=c_* delta^(7/4)`; it is implied by the new selection. I checked the actual downstream hypotheses below rather than inferring their validity from a previous complete theorem's conclusion.

## 2. Raw geometry, endpoint scale, and all four gradient terms

References: candidate `PROOF.md` Sections 2–3; `AFFINE_PROPAGATOR.md` Sections 1–2; original `AFFINE_CORE.md` Sections 1, 3–5; quantitative `AFFINE_POLYNOMIAL_BOUNDS.md` Sections 1–3.

Oddness makes label folding an exact identity of finite losses and raw trajectories. In the active direction, with `v=(1+y1*y2*rho)/2`, `r=sqrt(v)`, `lambda=a^3 r`, the normalized first coordinate `p=P1/r` has exactly the raw `L2` increment metric: an active raw increment satisfies `d ||dw||_2^2=||dP1||_2^2/v`. Directions perpendicular to the active input are annihilated by the affine objective. Thus changing to `t=lambda s` yields the genuine four-component gradient system

```
p'=A*B*D,   A'=B*D tensor p,   B'=D tensor Ap,   D'=BAp,
F=<D,BAp>.
```

This normalization does not silently replace the raw algorithm by a different metric. Matrix initial actions are bounded operators, while their learned differences/gradients are Hilbert–Schmidt; no trace of an infinite-dimensional identity is taken.

Write `z=||D||^2`. Differentiating the three balance identities and the scalar norms gives

```
||p||^2=1+z,
A*A=p tensor p+K,
AA*=B*B+J,
BB*=D tensor D+K_B,
z'=2F.
```

The initialized bounds give `-I<=K<=100I`, `-100I<=J<=100I`, `0<=K_B<=100I`. Consequently

```
z(1+z) <= s_A:=||Ap||^2 <= (z+101)(z+1),
z^2 <= s_B:=||B*D||^2 <= z^2+100z.
```

I checked the two less immediate gradient terms independently:

```
||BAp||^2
 = ||A*Ap||^2 - <Ap,J Ap>
 >= s_A^2/(1+z) - 100 s_A
 >= z^2(1+z) - 100(z+101)(z+1)
 = z^3-99z^2-10200z-10100,

||A*B*D||^2
 = ||BB*D||^2 + <B*D,J B*D>
 >= z^3-100(z^2+100z).
```

For the second line, `BB*D=zD+K_B D`; its squared norm is at least `z^3` because the cross term is nonnegative. For the first line, the positive quadratic and negative linear terms in `s_A` are bounded separately; no false monotonicity of their difference is needed.

The two Hilbert–Schmidt gradient norms are respectively `s_B(1+z)` and `z s_A`, each at least `z^3+z^2`. Therefore summing **all four** terms gives exactly

```
F' >= 4z^3-197z^2-20200z-10100.
```

As `F` is increasing from zero, it is nonnegative. With

```
P(z)=z^4-(197/3)z^3-10100z^2-10100z,
```

the derivative of `F^2-P(z)` is `2F(F'-P'(z))>=0`, giving `F^2>=P(z)` without division at the initial zero. The previous middle-gradient bound gives `F>=z^2/sqrt(2)`. For `z<=200`, this dominates `z^2-100z`. For `z>=200`,

```
P(z)-(z^2-100z)^2
 = z^2[(403/3)z-20100-10100/z] > 0,
```

and the proposed lower square root is nonnegative. Hence the asserted global inequality `F>=z^2-100z` is valid.

The inherited radial identity has initial right slope one because the canonical initialization satisfies `||B0 A0 p0||=1`. It gives `c=||D||>=t` and `c'>=c^3/sqrt(2)` for positive times. Together with bounded-operator balances and strong continuation this proves existence through the first target, `T<2`, and `c(T)<=M`, where

```
M=(3/(sqrt(2)lambda))^(1/4)>1,
S=T/lambda <= 2/lambda <= M^4,
r=3 M^-4/(sqrt(2)a^3),
M<=24^(1/4)delta^-1/8.
```

I checked the inequality `2/lambda<=M^4`: its numerical content is `2<=3/sqrt(2)`. The intrinsic `M`, not its uniform upper envelope, is used whenever a negative power of `r` is converted.

## 3. Integrated radius-one Hessian and beta family

At initialization scale `beta`, cubic homogeneity gives `Theta_beta(t)=beta Theta_1(beta^2 t)`, `F_beta=beta^4 F_1(beta^2 t)`. Thus, for `w_beta=sqrt(beta^2+c_beta^2)`,

```
(log w_beta)'=F_beta/(beta^2+c_beta^2)
 >= c_beta^2-101 beta^2.
```

The subtraction leaves the nonnegative remainder `101 beta^4/(beta^2+c_beta^2)`, so the estimate is valid at every nonnegative `c_beta`.

For `R_beta=sqrt(200 beta^2+c_beta^2)`, each raw Hessian cross block is bounded by `R_beta^2`. Each column has three off-diagonal blocks, so the sum-norm Hessian bound is `3R_beta^2`; the full first-layer contraction argument covers the inactive raw directions. On a radius-one raw tube it is `3(R_beta+1)^2`. This is the radius-one expression that has to be integrated accurately.

For `1<=beta<=1.001` and `t-s<2`,

```
integral_s^t 3R_beta^2
 <= 3 log(w_beta(t)/w_beta(s))+903 beta^2(t-s)
 < 3 log(w_beta(t)/w_beta(s))+1810.
```

The radial bounds separately give `integral c_1 <= 1+sqrt(2)` over any finite subinterval of the entire existence branch. Before its first level one, duration is at most one; afterwards integrate `sqrt(2)c^-2 dc`. Homogeneity changes the integral by `beta^-1`, so the same upper bound works for `c_beta`.

Thus `integral_0^T R_beta < sqrt(200)*1.001*2+1+sqrt(2)<31`. The remaining terms `6R_beta+3` integrate to less than `192`. The total is below the stated constant `2100`, while preserving the exact logarithmic coefficient three:

```
G_beta(t,s) <= exp(2100)[w_beta(t)/w_beta(s)]^3.
```

This verifies the new improvement. A fixed multiplicative enlargement of `R_beta^2` before integrating would not establish this same power; the candidate does not do that.

The common enlargement is also legitimate. At the target, put `R_*^2=200+M^2`. A raw polynomial-field continuation for `1/(1000R_*^2)` keeps primary sizes within `2R_*`. The largest beta displacement is `1/(10^5R_*^2)`, and `beta_far^2 T-T <=6(beta_far-1)` fits inside that continuation. It is the reference extended by this small interval, not the reference spuriously extended to its coarse upper duration bound. Hence the three inner beta scales and `beta_far` share the original interval.

The enlarged terminal bound gives `w_beta(T)<=30M`, while `w_beta(s)>=1`, yielding `G<=10^5 exp(2100)M^3`. Sufficiently fine positive Euler meshes inherit the compact-interval estimates with the stated factor four. The mesh can depend on the fixed dataset and deterministic bounds; there is no minimum step and no assertion of a growing-transcript probabilistic theorem.

The beta gaps satisfy both the lower margin `H^-1 M^-2` and the upper inverse-room bound `3*10^7 M^2`. These are dataset-dependent auxiliary proof scales, not data-selected activations.

## 4. Actual Gaussian probes, both orientations, and numerical envelope

I traced the original `TWO_SAMPLE_SOURCE_BASELINE.md` equations (23)–(25), the generic finite Gaussian conditioning derivation, and the normalized probe constructions in `two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md` Sections 2–5 and 8. The route is an actual independent-root measurement of the frozen formal coefficients:

1. At a fixed mesh and fixed nonzero amplitude, insert an independent standard Gaussian root in the same population as the source/output, at the specified answer instruction, and recompute all subsequent calls and updates.
2. The fixed-program theorem identifies the output pairing with this root. With coefficients and source covariances fixed, the affine scalar output is an affine expression in independent roots; its root coefficient is the amplitude times the desired signed sum of named-source derivatives.
3. A raw finite-difference estimate bounds the pairing. First take width to infinity, and then let the probe amplitude tend to zero using finite causal coefficient/covariance continuity.
4. Deterministic signs chosen from the limiting coefficients bound an absolute time row. A single slot retains its original mesh factor. Direct identity responses are added when the output itself is injected.

This avoids equating an arbitrary raw tangent with a formal source derivative. It also retains formally distinct arguments at singular source covariances, makes no covariance inverse assertion, and never pairs neuron coordinates from different layers.

The normalized injection/output costs are correct. Bottom transpose to `p` and top forward to `D` cost `1*1`. Middle transpose to `Ap`, and middle forward to `B*D`, cost `O(M)*O(M)`. Probing `Z1`, `Z2`, `Z3` and the two backward outputs gives the forward/reverse resolvents with product cost at most `O(M^2)` and a current identity. The top backward-answer probe changes `p,A,B` with cost `O(M^2)`; observing `BAp` adds another `O(M^2)`, proving the top strict transfer `U=R3 A3`. Observing the integrated readout with that same probe gives `L3` with product cost `O(M^2)` plus its current identity. Thus both top orientations are covered by actual probes.

The normalized learned moment densities have powers `2,4,2,4`, below the corresponding response powers `3,5,3,5`. On a fixed positive mesh the active expected coefficients and learned moments are nonnegative polynomials in beta: normalized raw ascent expansions have nonnegative coefficients, and every surviving Gaussian Wick pairing has nonnegative variance weight. This is positivity after expectation, not a sign claim about sampled weights. Differentiation gives `A3_beta'>=2 beta^3 R F L` in normalized variables. Bounding the derivative by the value at `beta_far` divided by beta room gives density power seven for `FL`, `RF`, `RFL`.

The active original-time transformations are

```
A2=(r/a) A2_hat,   A3=ar A3_hat,
B3=(ar)^-1 B3_hat, B2=(a/r) B2_hat.
```

Strict densities acquire the additional factor `lambda`; complete rows do not. Diagonal-sector resolvents transform by similarity without a sector condition number. It follows exactly that the active density powers are `-5` for `F,A2`, `-3` for `V,A3`, and `-1` for `U,FL,RF,RFL`; the backward row powers are `7,9`; the required resolvent rows have power `5`.

Inactive arrays are evaluated directly: the normalized forward integration kernels have the stated coefficients `1,2 beta^2,2 beta^2,3 beta^4`; inactive backward arrays vanish, and resolvents are identity. Original-time inactive forward densities are proportional to `r_-^2<=1`. This is why full-sample strict transfers are bounded by a constant even when their active bounds decay with `M`. No random gate is diagonalized by this calculation.

The final numerical ledger now has valid rounding. Taking primary bounds `100M`, the largest probe prefactor is bounded by `4*10^14 exp(2100)` before the listed ancillary factors. Their product is

```
(4*10^14)*(10^3)*(3*10^7)*(10^4)=1.2*10^29 < 10^30.
```

The conversion bounds `r^2<=288M^-8`, `r^-1<=M^4`, `a^-1<=2` were checked explicitly. Therefore every displayed original-time affine prefactor is below `10^30 exp(2100)`, which is strictly below the original

```
H=10^30(1+C0+Cz+Cg+exp(1410))^4 >=10^30 exp(5640).
```

No new unspecified constant is absorbed into an already saturated `H`. Subsequent polynomial estimates explicitly use powers of `H`.

## 5. Primal source input and nonlinear response

The quantitative primal proof supplies a cap-uniform raw radius-one tube independently of the new source bootstrap. Its explicit restriction `e<=c_* delta^(7/4)` gives endpoint `g_e(S)>=5/4` and the absolute regression margin. Raw discrepancy is bounded by `HeM^12`. Rank-one/moment differences are bounded by `HeM^15 h_j`; summing a backward row costs at most `HM^4`, giving `H^2 eM^19`.

Actual primary matrix/readout sizes are `O(M)`. Since capped backward gates satisfy `|D(z,q)|<=(a+e)|q|`, the actual incoming source output norms satisfy `q1:L2=O(M^3)`, `q2:L2=O(M^2)`, `C:L2=O(M)`. The fixed-program representation identifies these norms with actual output laws before source bootstrap or cap removal. This argument does not use an invalid assertion that a bounded `L2` action preserves subGaussian tails. The primitive source standard deviations have powers `0,2,1,1,2` in the stated order.

On the outer sector box, the candidate obtains full-sample forward density bounds `H^2`, resolvent rows `H^2 M^5`, and backward rows `H^2 M^9,H^2 M^7`. Exact same-array affine elimination in the value equations yields self coefficients `eH^6 M^13`, `eH^6 M^11`, `eH^6 M^8`, and Gaussian leading powers `6,6,7`. Under `eH^22 M^19<=1` these absorb with ample numerical slack. Incoming `Lp` powers are consequently `15,13,11`, uniformly for `p>=2`. These are suprema of individual deterministic `Lp` norms.

For a local population I verified the identities

```
J-Jaff=U[DeltaV Izeta+P J],
Ddelta-Ddelta_aff=L[DeltaV Izeta+P J],
P=Lgate+a DeltaV B+a B DeltaG+DeltaV B DeltaG.
```

They follow by writing `Ddelta=Vgate Izeta+(Lgate+Vgate B G)J` and eliminating `J-Jaff` with `U=RK`; `I+a^2 B U=L` gives the reverse orientation. This explicitly includes current factors. All gates retain their full two-sample action.

Strictness of `U` bounds a single transpose derivative by `H^3 h_j E_k` and a complete forward derivative row by `H^3 M^5 E_k`, with

```
E_k=exp[eH^6 sum_(r<k) h_r(Q_r+M^b)],   b=(9,7,4).
```

The factor `h_j` survives at every later stage, including arbitrary current diagonals of `B`. The scalar product majorant takes a running maximum of derivatives, but it integrates `Q_r` with `h_r` rather than inserting a random supremum of `Q`.

Weighted Jensen, the source subGaussian scales, duration `HM^4`, and the condition `eH^22 M^19<=1` give `E E_k^8<=2`. The largest stochastic integrated exponent is `4+15=19`; deterministic ones are `13,11,8`. No temporal independence is required.

Now, for every pair of times, `E[Q_r E_k]<=||Q_r||_2 ||E_k||_2`. Using the **actual primal** norms improves these factors to `H^2 M^(3,2,1)`. The exact error identity contains one explicit `P` insertion, hence only one explicit curvature factor `Q`; all further nonlinear iterations lie inside `E_k`. This is sufficient without a new raw `Lp` hypothesis.

For forward coefficients the two strict transfers cost no positive power of `M`, and the time integral costs `M^4`: the powers are `4+max(3,9)=13` and `4+max(2,7)=11`. The terminal feature gate adds a lower-order bounded term. For backward coefficients the correct reverse resolvent and complete forward-source row each cost `M^5`, so the powers are `5+5+max(2,7)=17` and `5+5+max(1,4)=14`. Bounded gate perturbations times `B` are included; omitting those would give incorrect smaller exponents.

The final candidate explicitly estimates

```
max_k E[sum_(j<=k) |(Ddelta-Ddelta_aff)_kj|],
```

with the terminal maximum outside expectation. For fixed `k`, expand deterministic `L_kr`, sum source slots, and apply the uniform-in-two-times Cauchy–Schwarz bound to each curvature term. This directly gives the displayed powers and dominates the deterministic row norm `max_k sum_j |E error_kj|`. It does not claim an expectation of a random temporal maximum. The earlier ambiguous notation is thus resolved in the final proof, with no new estimate required.

Adding learned moment errors leaves the common forcing bound `q<=H^30 eM^19`, uniformly in cap and sufficiently fine fixed mesh. It compares nonlinear derivatives with affine formulas at exactly the same deterministic coefficient arrays, so no coefficient-displacement term has been omitted.

## 6. Full deterministic sector closure

The exchange-equivariance induction in the original positive supersolution source applies to the **actual deterministic** blocks at every amplitude, cap, and mesh. Frozen formal derivatives transform by conjugation under sample exchange, and so do their expectations and learned moments. Thus both deterministic scalar sectors can be bounded separately. Individual random gates remain full matrices; nonsymmetric physical competitors are not restricted by this construction.

The active outer backward excess radius is `r_a=H^-10 M^-2`. The affine forward rows are `O(M^-1)` and `O(M)`, so their Neumann ratios are at most `H^-8 M^-3` and `H^-8 M^-1`. Strict density bounds persist by left-row multiplication; the reverse resolvent is controlled through `L=L_b+L_b J3 V`, not through a false claim that arbitrary right row multiplication preserves strict density. Top transfers depend only on `A3` and are bounded by monotonicity.

The inactive radius `r_i=H^-10 M^-5` separately controls its duration-sized integration row `O(M^4)`. Using the active `M^-2` radius in that sector would not suffice, but the candidate does not do so. This proves the full-sample transfer table needed by the response estimates throughout the outer box.

For forcing bounded by `q`, the exact inner supersolution is

```
A2*=A2_b, A3*=A3_b, B3*=B3_b+J3,
R*=(I-a^2 A2_b B3*)^-1,
W*=a^2 B3*R*,
B2*=B2_b+(W*-W_b)+J2.
```

Its backward equations dominate immediately from the variance factor `beta^2>=1` and monotone learned moments. For forward equations,

```
W*-W_b=a^2 L_b J3 R*,
F_b(B2*-B2_b)F_b=F_b J2 F_b+a^2(F_b L_b)J3(R*F_b).
```

The strict/row/strict inequality is legitimate on every positive mesh:

```
|U Q V|_d <= S |U|_d |Q|_r |V|_d.
```

To see the crucial mesh bookkeeping, expand `U_kr Q_rs V_sj`; the left strict factor supplies `h_r`, the right strict factor supplies `h_j`, and summing `Q` uses its complete row including `s=r`. No inverse mesh step appears.

The two first-forward sandwich powers are `-5+4-5=-6` and `-1+4-1=2`. Dividing by the positive leading entries `F_kj,V_kj>=H^-2 M^-8 h_j` yields first relative power `10`; beta slack costs two more powers. Positivity permits termwise domination of every subsequent geometric term by the resulting relative factor, with no additional coupled inverse cost. The second-forward ratio has smaller powers. Backward reconstruction costs `M^10 q` and fits inside `r_a` under the same requirement.

The explicit ledger `q<=H^-16 M^-12` gives all forward slack and all backward strict interior inequalities. Inactive reconstruction uses `B3*=J3`, `B2*=a^2J3R*+J2`, with rows at most `3q`; forward additions `H^3 M^4 q` and `H^5 M^4 q` fit inside their fixed density margins. Integrating positive beta derivatives gives a strictly positive inner/outer forward gap `H^-3 M^-10 h_j` at each strict entry, regardless of how small that positive mesh step is.

For signed actual coefficients, the causal polynomial inequality `|T0(C)|<=T0(|C|)` and the true source construction order give finite chronological comparison. At fixed cap/mesh the actual program is continuous along amplitude homotopy. It starts inside the box; at a proposed first exit the source forcing estimate and supersolution place every coordinate strictly inside. This closes the actual program, not merely an externally prescribed affine or symmetric random-gate model.

## 7. Final amplitude arithmetic and retained downstream conclusions

From the intrinsic scale, `M^32<=24^8 delta^-4`, and `24^8<H`. Therefore

```
e<=c_poly delta^4,
c_poly=min(1/4,c_*,10^-70 H^-400)
```

implies

```
eM^32<=10^-70 H^-399,
eH^22 M^19<=10^-70 H^-377<1,
qM^12<=H^30 eM^31<=10^-70 H^-369<H^-16.
```

All uses of `M>1` have the correct direction. Since `delta<=1`, it also implies `e<=c_* delta^(7/4)`. The gain can equal one; for the convex mixture it is `a=1-e>=1/2`. The original Gaussian-energy normalized identity-perturbation family is also retained by its explicit parameter conversion `a(r)=1/||G+r atan G||_2`, `e(r)=r a(r)<=r`.

The directly checked downstream sources were `SOURCE_AND_LIMIT_BRIDGE.md` Sections 4–6, `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md` Sections 2–4, the generic Gaussian/action sections of `L3_LOCAL_COMPLETE_PROOF.md`, and the hypotheses/product-query/comparison/limit arguments of `FIXED_CAP_VELOCITY_BRIDGE.md`. Their needed inputs are now all supplied: bounded raw primal paths, actual incoming subGaussian tails uniform in cap/mesh, and an endpoint prediction above one.

The asymmetric gate difference has one linear cap loss, `C(1+eR)`, and a tail term from the reference only. Gaussian reference tails defeat `exp(CR)` for every fixed finite interval. Hence cap paths and raw directions converge strongly to an autonomous uncut strong path; arbitrary bounded-primal strong competitors need no tail or symmetry premise. The same estimate started at a reached time proves restart uniqueness.

Population exchange symmetry gives `f_i=y_i g`. The first hit of one precedes the affine endpoint. For cap paths, bounded `g_R'` gives `1-g_R(s)<=C_R(s_R-s)` before the first hit, so the scalar clock diverges and produces a global physical path; monotonicity of capped `g_R` is not assumed. In physical comparison both actual residuals are retained. No scalar reduction is imposed on finite-width trajectories.

At each fixed cap/auxiliary mesh, the original finite Gaussian program applies because the capped coordinate maps have bounded continuous derivatives. Singular query regularization and finite causal continuity preserve the named source convention. Countable generated probe spaces, finite operator inequalities, and finite transpose identities construct both bounded actions and genuine adjoints. Fixed-cap Euler comparison removes the auxiliary mesh with width-independent constants. Finite current operator bounds come from exact rank-one unrolling, not cross-width trained operator-norm convergence. The same-width asymmetric cap comparison then gives uncut GF/GD; raw GD contributes only `C_(R,T) n^-2`. The initialized finite readout is coupled and kept; its normalized norm is `O_P(n^-1)` at initialization.

For hidden velocities the required product queries are first smoothly truncated to meet the fixed-program hypotheses, then identified with their Gaussian sources, all response corrections, and learned moments. Deterministic velocity comparison truncates only the reference velocity multiplier. The uncut velocity is a continuous `L2` time path by the bounded-gate trajectory chain rule, and its compact `L2` image has uniformly vanishing tails. Cap removal occurs at fixed reference-velocity truncation, followed by truncation removal. There is no unsupported product of growing cap-dependent moment constants with a cap error. The fixed-grid path interpolation inequality `||x-I_h x||_infty^2<=4h integral |x'|^2` supplies the stated path-space `W2` convergence. All kernel and second-moment conclusions follow from the retained `L2` fields and actions.

Finally, the absolute affine Gaussian regression bound is checked in `AFFINE_POLYNOMIAL_BOUNDS.md`: variances are at least `1,1/404,1/16`, the third Hermite coefficient yields `eta_*=4*404 exp(-1)/(27*pi*405^4)>0`, and the square root of the arctangent regression error is `W2`-Lipschitz. The existing primal restriction therefore gives activation-regression error at least `e^2 eta_*/4` on the whole feature interval, hence at all finite physical times. `INITIAL_MOTION_AND_NORMALIZATION.md` separately proves nonzero hidden/sample accelerations for every positive `e` using full initial Gaussian support, both actual reused-transpose covariances and responses, positivity of the corresponding Grams, adjunction, and exchange symmetry. These arguments impose no additional smallness threshold.

## 8. Objections considered and resolution

| Potential problem | Resolution in the reviewed proof |
|---|---|
| Full-gradient lower bound might mishandle a nonmonotone quadratic | Positive and negative `s_A` terms are bounded separately; displayed polynomial recomputes correctly. |
| Division at zero or unjustified radial substitution | Polynomial-difference derivative avoids division; radial substitution is only after a positive level. |
| Radius-one tube might lose the exponent three | `6R+3` is integrated separately with an absolute bound. |
| Beta references might leave the target interval | Explicit local continuation and `beta_far` gap fit on the common enlarged reference. |
| Raw tangent might be incorrectly substituted for a formal source derivative | Actual independent-root finite differences, named instruction placements, and ordered limits establish the required coefficients. |
| Missing top reverse resolvent or top strict transfer | The top backward-answer probe explicitly supplies `L3` and `U=R3 A3` with their different output costs. |
| Uniform dataset envelope might be treated as exact intrinsic scale | Exact `r=3 M^-4/(sqrt(2)a^3)` is used only for intrinsic `M`; the delta envelope is used only in final selection. |
| Numerical common prefactor might be overrun | Final `10^30 exp(2100)` exceeds the explicit product `1.2*10^29 exp(2100)` and remains below unchanged `H`. |
| Raw `L2` estimate might be used to assert subGaussianity | Separate exact value/resolvent estimates prove subGaussianity; raw `L2` enters only after envelope moments are controlled. |
| Expectation might hide a random time maximum | Final response and sector files explicitly put `max_k` outside expectation and supply the rowwise argument. |
| Random gates might be assumed sample diagonal | Only deterministic expected coefficient blocks are sector diagonal; derivative bounds retain full gates. |
| Arbitrary backward errors might need a strict density/minimum step | Complete causal row bounds, exact reverse identities, and the two strict sandwich factors retain all current diagonals without minimum-step assumptions. |
| Full theorem might still require exponent ten | Old response smallness is replaced; downstream sources require only the newly supplied primal/tail/endpoint premises. |
| Global statement might overclaim finite-width symmetry or arbitrary-state uniqueness | Physical comparisons retain both residuals; restart is from reached states on the same canonical spaces. |

No FAIL or OPEN item remains for the precise theorem at the recorded final hashes. Practical improvement of the very small prefactor and sharpness of the exponent are outside this theorem and are not certified here.

## 9. Exact integrity record

The final candidate manifest has SHA-256 `8439be694a44c71ad06986cdee28e55e20907fe682ead692ff9fe6747567d62d`; the dependency manifest has SHA-256 `1e6427032404b97eeff50bcdabf65350fa9d64680e92639e4c522d8c50464316`. Each file below was hashed from disk and matched its manifest. Candidate paths are relative to this power-four directory. Dependency paths are relative to `studies/mean_field_peeling`.

```text
7e33899649b547e7dcac8a465f2d118518d9db9ef001a3d04d2b9da615aa9485  PROOF.md
88a1bfbaf6fd1fc6fcfea56b25a4490932663090eb01710e9d96ba04d26fe460  AFFINE_PROPAGATOR.md
cf313286d301aa9fe5fb121d0c1fa5351213efbeaa4c087656d205c3156e417a  PRIMAL_L2_RESPONSE.md
e1ce9401b58bcd20384e1b2932d725844fda6904e9c9d70ef4a4f1af0f9ab68d  SECTOR_SUPERSOLUTION.md

a4d6ed0ee99a1e111b5eba068f2219cf561a2281b1828b26227aca7a0a54a050  two_sample_odd_activation_theorem/PROOF.md
634dd3bbc35436e9d1760bee5c11cbf2124b3c42e8920a1bf3a4fcbb15039711  two_sample_odd_activation_theorem/AFFINE_CORE.md
2a140f2a5a39f911b5c2ca51bc79102d20e9209f1450d38005360c88103f6e77  two_sample_odd_activation_theorem/SOURCE_AND_LIMIT_BRIDGE.md
c96316fdc481ef3f9e6fc402514ca9b45bcff12e199023505fbbb86d4e15bf24  two_sample_odd_activation_theorem/INITIAL_MOTION_AND_NORMALIZATION.md
27b2579f27ec14319dd39a93a4942d7b6463860648462d5ccb31b662c7725b75  two_sample_odd_activation_theorem/sources/ANGLE_SPECIFIC_THEOREM_ASSEMBLY.md
e32b52edb2c8061a341b1e93ff237f62f59d03f84b16e5b67a941bdd460c21bd  two_sample_odd_activation_theorem/sources/CONTRACT.md
a2322a8dbacf28244b9fef63e757ba3a915628dbdf31020062f8c5772a1c0aa0  two_sample_odd_activation_theorem/sources/FIXED_CAP_VELOCITY_BRIDGE.md
bd81de0a7ad0cb9bdd1f27f89961f4a3b7a7da6914456ae08596a882fa2ec351  two_sample_odd_activation_theorem/sources/INITIAL_FEATURE_LEARNING.md
f97148f84979ab5b8489927d477b6abb3d919e27fd457455f2e3b98416725de4  two_sample_odd_activation_theorem/sources/L3_LOCAL_COMPLETE_PROOF.md
ef0ea077406a27307bc84e045feebf5099f6f81883bdfed41508035fe4559568  two_sample_odd_activation_theorem/sources/NONLINEAR_RESPONSE_PERTURBATION.md
2891b892667396d64bd747689bcd59aa7ca3ffd224d3579fc3407bca0b623f9a  two_sample_odd_activation_theorem/sources/PREVIOUS_TWO_SAMPLE_PROOF.md
99eb60a64df1bbf4d8b70f351198abced9ef7eaeacf9b39c3997da5700a8f066  two_sample_odd_activation_theorem/sources/PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md
40882fc19e44b4b9245156595bb1071bd4de6007d619fada54c9fce7c37903f4  two_sample_odd_activation_theorem/sources/SYMMETRY_RADIAL_CLOCK.md
49da0f68047b4f516d3ad3c94b7112259838bcebf68e2296a948364232842789  two_sample_odd_activation_theorem/sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md
a84187ecd3639d0c4b7b209255056597326c97f11548faaf9b918659ae07477f  two_sample_odd_activation_theorem/sources/TWO_SAMPLE_SOURCE_BASELINE.md
0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02  two_sample_odd_activation_quantitative/PROOF.md
8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca  two_sample_odd_activation_quantitative/AFFINE_POLYNOMIAL_BOUNDS.md
51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f  two_sample_odd_activation_quantitative/POLYNOMIAL_RESPONSE_LEMMA.md
c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210  two_sample_odd_activation_quantitative/OLD_THRESHOLD_AND_NONAFFINITY.md
37b9e8a27135b95b8dffe05fe2b734229fadedc98bc1609259e365dbb2aeba37  two_sample_odd_activation_power10/PROOF.md
bc55c0f8e25de1f3a4316fe36e86afa25c9486e014192f2eb818358909b048eb  two_sample_odd_activation_power10/AFFINE_SOURCE_CERTIFICATE.md
3622a0f903cd51b712d1d524a140d834471b5eb588611f059535c41f6efd2332  two_sample_odd_activation_power10/REFINED_RESPONSE.md
e2be183521919ce69c7ae41b81f5cd78566c5430a78c2408687f52f1b6d86774  two_sample_odd_activation_power10/POSITIVE_SUPERSOLUTION.md
```
