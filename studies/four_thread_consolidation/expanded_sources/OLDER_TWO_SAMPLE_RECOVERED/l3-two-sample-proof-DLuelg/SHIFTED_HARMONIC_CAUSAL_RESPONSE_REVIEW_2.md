# Independent adversarial mathematical audit

Date: 2026-09-06.

**Verdict: PASS for the stated finite causal Gaussian-law conclusions. No required mathematical correction found.** This verdict includes the current-response identities, the full formal retarded identities, the second-update covariance counterexample and its weighted test, and the transfer of the local absolute-response bootstrap. It does not certify a finite-width identification, a continuous-time construction, or global response control.

Candidate audited, exact SHA256:

```text
fbb08acfe9decd7e4797266be32a68b6a5a84e892e50ae1acb958b10353770ae
```

## 1. Inputs, hash verification, and audit boundary

I read both of the following files completely, with line numbers, and no other project, history, review, or mathematical source. No external sources, experiments, or agents were used. The argument below is an independent mathematical check, not an adoption of an earlier review.

| Input | Bytes / lines | SHA256 of the actual input |
|---|---|---|
| `/tmp/l3-two-sample-proof-DLuelg/SHIFTED_HARMONIC_CAUSAL_RESPONSE.md` | 39147 / 878 | `fbb08acfe9decd7e4797266be32a68b6a5a84e892e50ae1acb958b10353770ae` |
| `/tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md` | 14263 / 352 | `9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170` |

The current bootstrap dependency hash agrees exactly with the hash recorded in candidate line 42. Other listed files were neither read nor hashed; their contents and historical attributions are outside this audit. In particular, the bootstrap's external finite-program identification dependency is not imported. References below use `C` for candidate line numbers and `B` for bootstrap line numbers.

As requested, equations (4)–(6) are stipulated. The mathematical question is what follows within that finite Gaussian law, with its specified formal derivatives. This does not establish that this law describes any particular finite-width scheme. The bootstrap's original activation is also not silently retained: its estimates are checked below after replacing the positive-gate assumption by the candidate's absolute gate bounds.

## 2. Required corrections

**None found within the audited scope.** No additional premise is needed for the finite identities, the fixed-parameter small-step counterexample, or the local bounds (34), beyond the explicitly stated law, initialization, smooth cuts, and parameter ranges.

Several premises are essential and must remain attached to the conclusions:

- Source derivatives differentiate the displayed formal maps with all selected deterministic coefficients and covariance parameters fixed. They are neither derivatives of the self-consistent law with respect to its statistics nor physical parameter perturbations.
- The second-update strict-positivity assertion fixes `rho < 1` and a finite cap pair before taking the mesh to zero. It does not assert a common positive lower bound as `rho` approaches 1.
- Pointwise label-weighted damping on a continuous path requires the separately assumed gradient-flow interpretation and nonnegative label-mode prediction. It is not a consequence of a generic capped Euler reference.
- Continuous-time passages, width identification, cap removal, and global continuation remain conditional or unproved, as the candidate states.

These are restrictions already present in the candidate, not hidden repairs supplied by this review.

## 3. Causality, singular slots, and existence of the finite derivatives

The construction order in C209–215 is valid. At time `k`, the bottom fields use only earlier bottom queries. This determines the current second-layer forward response coefficients and forward-source covariance extension; the current second-layer fields then determine the third-layer forward coefficients and forward-source covariance extension. The current top deltas determine the third-layer transpose coefficients and middle reverse-source covariance extension. Current middle queries and deltas then determine the second-layer transpose coefficients and bottom reverse-source covariance extension.

The same-time terms in the reverse equations cause no implicit solve. The corresponding forward features have already been constructed. The source groups remain independent because their covariance parameters are deterministic expectations, not realized fields passed from one population to another.

Every covariance extension is a Gram matrix of already constructed random fields, hence positive semidefinite and consistent with the previously constructed covariance block. Singular extensions pose no problem for this existence argument. No covariance inverse or positive innovation variance is needed.

The formal differentiation convention is coherent even off the support of a singular source law: the displayed recursions specify a smooth map on all formal source coordinates before evaluation on the Gaussian law. It would be incorrect to replace that map by an almost-surely equal reduced expression and then differentiate it. The candidate consistently avoids this mistake.

In particular, at time zero, `w_0` and the top deltas are identically zero as formal expressions. Consequently `B^(3)_0=0` and the middle reverse source is zero almost surely. Nevertheless,

\[
q^{(2)}_{0a}=\zeta^{(2)}_{0a},\qquad
\delta^{(2)}_{0a}=\gamma(\xi^{(2)}_{0a})\tau_2(\zeta^{(2)}_{0a})
\]

remain the formal expressions. Their forward-source derivatives vanish on the attained law, while

\[
\partial_{\zeta^{(2)}_{0a}}\delta^{(2)}_{0a}
=\gamma(\xi^{(2)}_{0a})
\]

need not vanish or have a positive sign. This gives the claimed base case without deleting zero-variance slots.

The finiteness assertion in C175–182 also checks out. In the uncut case each reverse query is a Gaussian coordinate plus a finite deterministic-coefficient sum of bounded features. First derivatives satisfy finite triangular recursions whose factors are bounded gates, bounded readout factors, deterministic coefficients, and at most polynomial dependence on the Gaussian coordinates. Their moments are finite. Capped laws are easier. This proves finite-prefix integrability, not a uniform bound as the number of time slots or caps changes.

## 4. Symmetry and normalization

The signed sample exchange (7) preserves the stipulated law. Swapping samples preserves the root covariance, changes the label vector's sign, and exchanges the forward-type fields. Readout, deltas, queries, and reverse sources acquire an additional minus sign. Oddness of the cuts is exactly what the bottom and middle equations require.

The coefficient transformation is also correct. A forward-feature derivative with respect to a reverse source changes sign under this transformation, as does a delta derivative with respect to a forward source. The learned terms in both coefficient definitions have the same sign change through `y_b`. Thus

\[
A_{\pi i,\pi j}=-A_{i,j},\qquad B_{\pi i,\pi j}=-B_{i,j}.
\]

The causal construction transports this symmetry inductively, including for singular Gaussian covariances. It yields

\[
\mathbb Ew_k=0,\qquad f_{k1}=-f_{k2}=g_k,
\qquad \mathbb E[w_kh^{(3)}_{ka}]=f_{ka}.
\]

This establishes a symmetry of deterministic expectations. It does not give pathwise equality of finite-width sample predictions.

The displayed physical-to-feature normalization is internally consistent when its stated premises hold: substituting `r_a=y_a(g-1)` into the displayed physical velocity and dividing by `4(1-g)` gives the feature velocity with coefficient `1/2`, hence Euler coefficient `lambda=Delta/2`. This check uses the formulas inside the candidate; it does not verify an external model contract or derive a population gradient representation from (4)–(6).

## 5. Full retarded differentiation and the two learned matrices

Equations (9)–(11) are the full chain and product rules for the stipulated maps. In particular:

- The bottom variation contains both `-h tau(q) P` and `gamma tau'(q) Q`, including the full bottom reverse return.
- The middle variation contains the historical forward return through `A^(2)` and all reverse returns through `B^(3)`, including the current one.
- The top variation differentiates both the gate and the accumulated readout. Its `u_k` term is essential and has the displayed factor `lambda` and sample labels.

The local derivative maps do not acquire derivatives of the deterministic statistics: those are fixed by definition. The statistical feedback is reinstated through (6) and (12). Both trained matrices are retained there, with learned forward terms `lambda y_b E[H_i H_j]` and learned reverse terms `lambda 1_(r<k) y_b E[delta_i delta_j]`. No missing factor of two or omitted learned action was found.

For a top forward-source direction, expectation gives exactly

\[
x=v+A^{(3)}r,\qquad
r=-Fx+\mathcal T-\mathcal C,
\]

because `E[wh P]=f E[P]+Cov(wh,P)`. This proves (19) and (20). Neither the two gates in the readout term nor the curvature factor can be separated from the random sensitivity without an additional argument.

The mean map `v -> x` is lower triangular in time with identity diagonal: no current source affects a strictly earlier delta. It is therefore invertible on a finite prefix, regardless of singularity of the Gaussian source covariance. The weighted balance (21) follows by multiplying each row by `omega_i y_a x_i`. Its weights and directions are formal deterministic tests; sample-label multiplication does not define a positive metric.

The middle identities (22) and (23) have the correct signs and retain the query, cut derivative, random sensitivity, and historical reverse terms. Finally, substituting `P_i=v_i+sum A_ij T_j` into the top covariance gives precisely (24), including its minus sign on the two-time curvature product.

One distinction remains important: (19)–(21) describe `D^(3)`, the expected-derivative component of `B^(3)`. The learned reverse covariance is additional. The candidate explicitly retains it in (6) and limits the counterexample accordingly in C681–686. A conclusion about the total learned transpose action must not erase this distinction.

## 6. Current blocks and accumulated estimate

For the current top slot `xi^(3)_(kb)`, strict causality gives `u_k=0` and `P^(3)_(ka)=1_(a=b)`. Hence

\[
B^{(3)}_{ka,kb}=D^{(3)}_{ka,kb}
=-\mathbf 1_{a=b}\mathbb E[w_kh^{(3)}_{ka}]
=-\mathbf 1_{a=b}f_{ka}.
\]

There is no same-time learned term. This remains correct when current and historical Gaussian coordinates coincide almost surely.

Substituting this diagonal block into the middle reverse variation yields (14). For a current middle forward-source impulse the historical variations vanish, giving exactly (15), including the uncancelled expectation `-E[h^(2) tau_2(q^(2))]`. Mean-zero readout does not eliminate that different mixed moment.

For the accumulated bound, write the candidate's contrast as `V_k=(H^(3)_(k1)-H^(3)_(k2))/2`. Since `|h|<=b`,

\[
|V_k|\le b,\qquad w_{k+1}=w_k+\Delta V_k,
\qquad |w_k|\le bs_k.
\]

Symmetry then gives `|f_ka|<=b^2 s_k=s_k/200`. The Euclidean operator norm of the current two-sample diagonal block is consequently at most `s_k/200`, and its contribution to an individual query is at most `a s_k/200`.

Moreover, `E[w_k V_k]=g_k`, so telescoping the squared readout gives

\[
2\Delta\sum_{k<M}g_k
=\mathbb Ew_M^2-\Delta^2\sum_{k<M}\mathbb EV_k^2.
\]

This is (17), including the sign of its Euler defect. Dropping the nonnegative squared-readout term or the nonnegative defect proves the two sides of (18). For a completely mesh-free two-sided bound one can additionally use `Delta<=S` when `M>=1`; the zero-step case is trivial. Retaining the sharper `S Delta` defect is appropriate.

These facts do not assert `g_k>=0` for every capped or finite-step law. On a separately constructed continuous gradient feature flow the stated gradient identity would imply that sign. Ordinary Euclidean dissipativity is still not implied: the unweighted current block has diagonal entries `-g` and `+g`. The candidate's warning about label weighting is mathematically necessary and correct.

## 7. Second-update covariance and weighted test

### 7.1 Exact finite-step identities

All attained initial deltas and queries vanish, so the first hidden update vanishes. Covariance identity (5) also makes the corresponding time-zero and time-one forward sources equal almost surely. Thus `Z^(ell)_(1a)=Z^(ell)_(0a)`, `w_1=lambda D`, and `w_2=2 lambda D` hold as value identities.

For the formal impulse `e_(1a)` at the top, earlier responses vanish and

\[
P^{(3)}_{1b}=\mathbf 1_{a=b},\quad
T^{(3)}_{1b}=-\mathbf 1_{a=b}w_1h(U_a),\quad
P^{(3)}_{2a}=-A_a w_1h(U_a),\quad
u_2=\lambda y_a\gamma(U_a).
\]

In particular, differentiating the reduced value formula `w_2=2 lambda D` would give the wrong formal derivative. The candidate uses the unreduced recursion and obtains the correct expression.

Substitution proves both lines of (27), and specifically

\[
-\mathcal C_{2a}(e_{1a})
=2\lambda^2 A_a\operatorname{Cov}
  \big(Dh(Z^{(3)}_{2a}),Dh(U_a)\big).
\]

### 7.2 Coefficient and convergence check

For the current bottom reverse source at time one, the bottom coordinate at time one is unaffected by that source. Its sole injection into the next bottom coordinate is

\[
\partial_{\zeta^{(1)}_{1a}}Z^{(1)}_{2a}
=\lambda y_a\gamma^{(1)}_{1a}\tau'_1(q^{(1)}_{1a}).
\]

For the current middle reverse source, the sole direct derivative of the time-one middle delta is `gamma^(2)_(1a) tau'_2(q^(2)_(1a))`. Propagating through the second matrix gives the second line of (29). These calculations justify the exact formula (29), without ignoring either learned matrix.

The small-step passage is justified at this fixed number of updates. Top deltas at time one and their expected forward derivatives are `O(lambda)`, so the middle query has Gaussian standard deviation and bounded response shift of that order. The time-one middle forward-derivative formula then gives `B^(2)=O(lambda)` and the same query bound at the bottom. Consequently the second bottom displacement is `O_L2(lambda^2)`.

For the needed time-one columns of the forward kernels, (29) and its sample-off-diagonal version directly give `O(lambda)` bounds from bounded gates, features, and cut derivatives. The learned forward corrections at time two are thus `O_L2(lambda^2)`. Also,

\[
\|\xi^{(\ell)}_{2a}-\xi^{(\ell)}_{0a}\|_2^2
=\mathbb E\big(H^{(\ell-1)}_{2a}-H^{(\ell-1)}_{0a}\big)^2.
\]

This identity propagates convergence through both layers without a covariance inverse. Initial-delta corrections vanish as values. Since the cuts are the identity near zero and have bounded first derivative, `tau'_j(q^(j)_(1a)) -> 1` in probability. All products used in (29) are bounded, so their expectations converge. Therefore

\[
\frac{A_a}{\lambda}\longrightarrow
y_a\{F_2+(F_1+J_1)J_2\}=y_aL_0.
\]

The `F_2` term is the learned third-matrix forward action. The `F_1 J_2` term retains the learned second-matrix action, and `J_1 J_2` retains the bottom response. Since `F_2>=m^2`, `L_0>0`.

### 7.3 Strict positivity, including the singular endpoint

At initialization the first feature pair has equal diagonal second moments. Its Gram eigenvalues are half the expected squared sum and difference. The sum is strictly positive. The difference is nonzero with positive probability for `-1<rho<1`; for `rho=-1` it is `2 epsilon sin G`, also nonzero with positive probability. Thus this feature Gram is positive definite even at the singular root endpoint.

The middle initial pair is consequently a nonsingular Gaussian. Repeating the same positive-sum/nonconstant-difference argument shows that the top initial pair `U` has a positive density on all of `R^2`. The continuous function `D h(U_1)` takes the distinct values zero at `(pi/4,pi/4)` and `b^2` at `(pi/4,-pi/4)`. It is not almost surely constant, so its variance is strictly positive. Exchanging samples proves the corresponding assertion for sample two.

The bounded convergence just checked now proves

\[
\lim_{\Delta\downarrow0}
\frac{y_a[-\mathcal C_{2a}(e_{1a})]}{\lambda^3}
=2L_0\operatorname{Var}(Dh(U_a))>0.
\]

The quantifier is correct: for every fixed `rho<1` and fixed finite cap pair there is a positive mesh threshold below which this scalar contribution is positive. The coefficient is independent of the caps. The argument does not claim a uniform positive margin in `rho`, a fixed-positive-time limit, or a width-uniform counterexample. At `rho=1` the contrast degenerates, explaining the exclusion.

### 7.4 The weighted-test direction is valid

For

\[
\widetilde v=e_{1a}+(1+A_af_{1a})e_{2a},
\]

the current addition changes `P^(3)_(2a)` by the deterministic constant `1+A_a f_1a`. Since the mean of its historical part is `-A_a f_1a`, the resulting `x_(2a)` is exactly one. That addition leaves the covariance unchanged. Taking only `omega_(2a)=1` in (21) therefore gives a strictly positive covariance residual in that weighted balance.

The argument is stronger than merely observing a signed matrix entry: it supplies the actual direction and weight required by the asserted universal sign test. It does not establish positivity of the total balance. Nor does it require that the direction belong to the support of the singular source covariance; such a restriction is absent from the stipulated formal derivative test and is expressly disclaimed in C675–677.

Thus (32) is indeed false in the stipulated finite law, and universal discarding of this covariance as nonpositive is also false. No conclusion about instability or failure of a larger coupled energy follows.

## 8. Independent check of every local-bootstrap transfer estimate

Use `a=7/6`, `e=1/10`, `c=1/5`, and kernel bound `A=3/2`, as in the bootstrap. The harmonic activation satisfies the stronger bounds `|gamma|<=b<e` and `|gamma'|<=b<c`. All estimates below use absolute values. Positivity of the gate is unnecessary; the sign assertion in B139 is the base-case statement that needs the candidate's explicit replacement (33).

### 8.1 Bottom source injection and moments

A single bottom reverse slot injects at most `lambda e` into a later bottom coordinate and hence `lambda e^2=Delta/200` into its feature. The subsequent variation obeys

\[
|d(\gamma\tau(q))|\le c|q||dZ|+e|dq|,
\qquad |dq|\le\mathbf 1_{\rm injection}
 +e\sum|B^{(2)}||dZ|.
\]

The two update samples convert `Delta/2` into `Delta`; they do not produce an additional factor of two. This proves the Gronwall factor in B170–172.

Using only past `U_r,V_r<=1`, the middle query norm is at most `Q_0=161/120`, so the bottom reverse Gaussian standard deviation is at most `Q_0/10`, and its response shift is bounded by `a`. The Gaussian maximum bound and time Jensen therefore give

\[
\mathbb E E^{(1)}_j
\le4\exp\!\left\{\frac{73}{200}
 +\frac9{200}\left(\frac{161}{1200}\right)^2\right\}
<4e^{2/5}<6.
\]

No temporal or sample independence was used. The forward-kernel bound is consequently

\[
|A^{(2)}_{ja,sb}|
<\lambda\left(\frac{49}{36}+\frac3{50}\right)
=\lambda\frac{1279}{900}<\frac32\lambda.
\]

### 8.2 Middle sensitivities and moments

Each current forward-source row has exactly one direct unit derivative. Summing its absolute derivatives gives the factor

\[
E^{(2)}_j
=\exp\!\left\{A\Delta\sum_{r<j}
 (c\max_a|q^{(2)}_{ra}|+e^2V_r)\right\}.
\]

A single middle reverse source contributes at most `A lambda e^2=A Delta/200` to a later feature, multiplied by this factor. With reverse Gaussian standard deviation at most `7/40`, the stated moment estimate is

\[
\mathbb E(E^{(2)}_j)^p
\le4\exp\!\left\{\frac{219p}{400}
 +\frac{3969p^2}{1280000}\right\}.
\]

Its consequences `E E^(2)_j<8` and `||E^(2)_j||_2<7/2` follow from the bootstrap's displayed elementary exponential bounds. Thus

\[
|A^{(3)}_{ja,sb}|
<\lambda\left(\frac{49}{36}+\frac3{25}\right)
=\lambda\frac{1333}{900}<\frac32\lambda.
\]

The small positive margin is real. No sign-changing factor has been treated as positive in obtaining it.

### 8.3 Top row and learned transpose term

Differentiating the accumulated readout contributes `Delta e^2 sum_(r<j) T_r`; differentiating its gate contributes `aSc T_j`. Together these are at most `(73/300)S max_(v<=j)T_v`. The top forward recursion therefore gives

\[
\max_{v\le j}T_v\le e^{657/800}<5/2.
\]

The learned reverse row is bounded by `a^2 S^3/100`, with both sample contributions included. Therefore

\[
V_k\le\frac{73}{80}+\frac{147}{3200}
=\frac{3067}{3200}=V_*<1.
\]

This is a current-row estimate obtained without using `U_k`.

### 8.4 Current middle row and exact rational constant

The improved current query bound is

\[
\|q^{(2)}_{ka}\|_2\le\frac7{40}+\frac76V_*
=\frac{24829}{19200}=Q_*.
\]

Completed induction steps give the same bound at earlier times. The full current reverse return yields the forward-derivative row bound `(c|q^(2)_ka|+e^2 V_k) E^(2)_k`. Cauchy–Schwarz, not an independence assertion, handles its mixed expectation. The learned second-matrix reverse row contributes at most `S e^2 Q_*^2`. Hence

\[
U_k\le\frac72\left(\frac{Q_*}{5}+\frac{V_*}{100}\right)
 +\frac3{200}Q_*^2
=\frac{71063018523}{73728000000}<\frac{97}{100}.
\]

The rational equality checks exactly. There is no use of the unknown current `U_k` in closing this induction.

### 8.5 Actual-query exponential envelopes

For both reverse layers, the response shift has magnitude at most `a`, and the Gaussian source variance is at most `(7/40)^2`. The elementary inequality `(zeta+beta)^2<=2 zeta^2+2 beta^2` gives, without any independence premise,

\[
\mathbb E e^{q^2/16}
\le e^{49/288}(1-49/6400)^{-1/2}<2.
\]

Thus every estimate asserted in (34) transfers with the published constants, uniformly over the stated meshes, caps, and input correlations on `S<=3/2`. The positive feature floor is available but no positive lower gate bound enters this proof. This is the existing absolute-response bootstrap, not a new signed stability argument or an extension of its time interval.

## 9. Nontransferability and scope checks

The mathematical nontransferability statements in C761–832 are correct independently of whether the historical files used precisely the arguments attributed to them:

- `gamma(z)=b cos(z+pi/4)` has zeros at `pi/4+pi Z` and changes sign. A global smooth coordinate with derivative `1/gamma` is unavailable because of the poles.
- Ordered preactivations do not imply an ordered feature contrast. For example, `z_1=pi/4+2pi` and `z_2=pi/4-2pi` satisfy the indicated opposing tail constraints but give identical features. A positive feature floor controls a same-label sum, not an opposite-label difference.
- Neither an opposite-label readout nor multiplication by the oscillatory gate has the old pointwise sign property. The mean current-response identity does not supply such a pointwise property.
- Query quadrants alone do not determine delta quadrants when the query is multiplied by a correlated gate that can change sign or vanish. Gram positive semidefiniteness survives; strict nondegeneracy needs a separate argument.
- For a nonzero random velocity to remain nonzero after multiplication, its nonzero event must overlap the nonzero-gate event with positive probability. Gaussian initialization supplies zero probability of a gate zero for each marginal, but an arbitrary later attained law needs its own justification.
- Bounded activation and unbounded preactivation support exclude a nonzero affine slope, but permit a constant feature on an unbounded periodic level set. A nonzero absolutely continuous component would exclude any affine almost-sure relation for this analytic nonconstant activation. The candidate does not establish that component at later times.
- The relative-gate inequality fails at the stated exact pair `0,pi/2`: equal activation values and opposite nonzero derivatives give zero on the proposed right-hand side and a positive left-hand side.

The dependency's same-label feature-time fitting statement (B333–341) is explicitly conditional on a correctly constructed uncut gradient feature flow. Under that premise, the readout component alone gives label-mode kernel at least `m^2`, and fitting by `1/m^2=36/25` follows from initial prediction zero. This argument uses positive feature values, not positive gates, and does not supply an opposite-label fitting bound.

The final claim ledger is appropriately limited. The audit certifies the finite identities and the local estimates, not the referenced finite-program theorem, a common probability-space limit, both-cap removal, physical GF/GD comparison, exact-GD stopping, or all-time nonfreezing/nonlinearity. The covariance counterexample invalidates the proposed factorization and universal residual-sign shortcut; it is not an impossibility theorem for another energy estimate or for global continuation.

## 10. Optional improvements, not conditions of acceptance

1. **Make the continuum premise even more explicit at C390–399.** The current wording already says “an existing uncut gradient feature flow.” It could additionally say that the population gradient representation and passage from the finite references are assumptions of that paragraph, not results of (4)–(6). This would make the boundary harder to miss.

2. **Expand the short convergence argument at C604–619 by one line.** Writing `||q^(j)_(1a)||_2=O(lambda)` and the forward-source difference identity beside each layer makes clear that the argument needs neither a historical covariance inverse nor a cap-tail theorem. The present argument is sufficient; the expansion would improve inspectability.

3. **Keep the derivative-component distinction near any future use of (21).** If (21) is later advertised as a bound on the full `B^(3)` response, its learned reverse covariance contribution must be appended explicitly. The current candidate does not make that unsupported extension.

No candidate or dependency edits were made by this audit.
