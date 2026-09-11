# P1 independent scientific review B

**Overall verdict: ACCEPT for the exact proposed scope.**

The supplied packet establishes the finite-width right derivative, identifies
its canonical linear limit on each fixed physical horizon, proves the stated
whole-circle prediction convergence, and separately bounds the population
homogeneous propagator uniformly in physical time. The proof of weighted
forcing uses actual finite cavity estimates before transferring moments to
the canonical reference. The finite tangent identification has a separate
consistency argument; it does not follow merely by differentiating a population
formula. I found no surviving mathematical gap requiring a correction to this
scope. This verdict is a scientific assessment, not approval to edit established
files or a claim about any stronger nonlinear continuation result.

## 1. Reviewer identity, isolation, and authority

- Reviewer: fresh isolated scientific reviewer B for P1.
- Fresh Codex process/thread identity, obtained from `CODEX_THREAD_ID`:
  `01a090ca-1e9e-7482-8804-54261fdfc386`.
- Additional review-session UUID generated at startup:
  `c049d229-2e7f-44eb-859b-e32c428c7823`.
- Startup record: `2026-09-11T14:06:25.192458+00:00`.
- My reusable orchestration role is `/root`. That label is **not** a unique
  reviewer identity and does not identify me with the author called `/root`.
  My thread identity differs from the manifest's original author
  `01a090b5-1a52-7072-a829-cd2aad518558` and selector
  `01a090c0-8a58-7da1-8075-8c0b0f23f959`. The other author/assembler role names
  in the manifest are provenance, not evidence I used to reach the verdict.
- The subprocess that collected the identity reported PID 3 and parent PID 2.
  These namespace-local subprocess numbers are recorded only for provenance;
  they are not the fresh reviewer identifier.

I read only the seven permitted packet files and the two required skills with
their applicable research-contract and adversarial-audit references. I did
not read a study README, author history, earlier round, another review,
integration/build source, live chapter, or unlisted scientific source. I did
not use Git, delegate, contact another task, execute a training trajectory, or
run a parameter sweep. No packet input was edited. Writes were confined to
this exclusive report and the exclusive scratch directory:

`/home/amir/Codes/PDE/data/generated/trained_data_response/scientific_p1_b`.

The standalone check programs were read completely before execution. My
additional program does not import either packet check program. It imports
only installed numerical/standard libraries, reads the allowed dependency
and certificate files for a byte comparison, and writes into its own scratch.
The supplied assignment controls scope; I performed no author startup or
promotion workflow.

## 2. Inputs, hashes, and complete line coverage

All line references below refer to the frozen packet files. `SECTION` means
`P1_SECTION.md`; `DEP` means `P1_DEPENDENCIES.md`; `ANC` means
`P1_ANCILLARY.md`.

The following SHA-256 values were computed before substantive scientific
review and checked again after the review. Every manifest-listed allowed
input agrees with its manifest value. The manifest itself has no self-hash;
its independently recorded hash also remained unchanged.

| Input | Lines | SHA-256 |
|---|---:|---|
| `P1_ASSIGNMENT.md` | 47 | `a9f61d5f27d84e8a9de85d7ba5faaf39c4adb19e7829c27c285a455916488199` |
| `P1_MANIFEST.json` | 83 | `f9f3ac7dd834429f2afd1b2d819e20cf04da37446311405943332300ca4fa53d` |
| `P1_SECTION.md` | 2062 | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| `P1_ANCILLARY.md` | 300 | `649f0ee17af3c0a2f4b995e971929f8e7a62d9d420614baee418af62d6cdd420` |
| `P1_DEPENDENCIES.md` | 3238 | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| `P1_CHECK_IDENTITIES.py` | 197 | `b0bbbde5f1f024dbb46975b2092d3aa2a79cabd0375f4520c05489f934d3902f` |
| `P1_REFERENCE_CERTIFICATE.py` | 56 | `112ce04c6d8e20859b5a778cfdeed42690949af807d421b7db90e82c2576a49e` |

Reading coverage was as follows; ranges are inclusive.

| Material | Completed coverage |
|---|---|
| Assignment and manifest | Entire files, 1–47 and 1–83 |
| SECTION | 1–360, 361–730, 731–1090, 1091–1440, 1441–1780, 1781–2062 |
| ANC, including complete revised guide and navigation replacement | 1–300, with a separate repair read of 100–205 |
| DEP | 1–360, 361–690, 691–965, 966–1190, 1191–1460, 1461–1750, 1751–2030, 2031–2320, 2321–2610, 2611–2910, 2911–3238; repair read 840–880 |
| Both programs | Every line, 1–197 and 1–56; embedded certificate also read at DEP 2677–2732 |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | Entire file |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | Entire file |
| Its `references/research-contract.md` | Entire file |
| Its `references/adversarial-audit.md` | Entire file |

There were repaired truncations, not skipped passages. The first combined
read of SECTION 1–360, DEP 1–360, and ANC 1–300 exceeded the orchestration
output budget. I repeated DEP 1–360 and ANC 1–300. The latter output still
elided part of the long guide table; a separate ANC 100–205 read restored
the complete missing passage. DEP 691–965 exceeded its command output limit
and elided text near 842–868; the separate DEP 840–880 read restored it.
SECTION 1–360 was intact in the original output. All final reading ranges
have been checked for complete coverage.

Both complete guides were read: the original frozen guide at DEP 7–279 and
the revised guide at ANC 5–282. Their historical chapter inventory and
literature orientation were treated as navigation context. Their linked
external sources are explicitly not proof dependencies; I did not open them
or import their theorems. The scientific dependency proofs actually invoked
by C.4.6 are contained in the allowed packet. Manifest build/integration
entries were treated solely as provenance.

## 3. Exact claim contract

The model is the two-hidden-layer tanh network with input
`u=x/sqrt(2)` on the unit circle, no biases, independent stored Gaussian
variances `(1,1/n,1/n²)`, mobilities `(n,1,n)`, and the unhalved mean-square
loss. The active reference law has equal weights at `(e1,+1)` and `(e2,-1)`.
For each fixed deterministic Borel probability law ν on the compact
input/bounded-label space, the same initialized arrays are used for
`με=(1−ε)ν*+εν`, and the right derivative is taken at each finite n.

The limiting state is a clock row in `L²(Ω1;R²)`, a Hilbert–Schmidt middle
increment, and a readout in `L²(Ω2)`. The initialized action itself remains
bounded and generally non-Hilbert–Schmidt; its reverse is its actual adjoint.
The finite metric is exactly

`||ξ||F²/n + ||B||F² + ||d||²/n`.

The output claim is convergence in probability of the supremum over a
**fixed** physical interval `[0,T]` and the whole circle. State identification
uses same-width program comparisons and canonical limits, not subtraction
of fields on unrelated carriers. The population homogeneous evolution has
a separate uniform bound for all `0≤s≤t<∞`. Forcing is linear in signed
measures with total variation equal to variation **mass**, and the forced
response bound grows linearly with T.

The approximation parameters are source cutoff, deterministic data
quadrature, and proof time mesh. They are fixed before each width limit,
then removed using estimates. They are not optimizer hyperparameters or a
training experiment. Dependence of constants on T and on the fixed reference
is permitted. There is no bound uniform in ν on finite-width failure
probabilities, no numerical conditioning certificate, and no claim for a
growing `T_n`.

The coefficients come from the separately constructed autonomous reference
flow; this is legitimate linearization about a specified reference, not an
encoding of an unknown future perturbed path. No finite-dimensional scalar
closure or compression theorem is claimed.

## 4. Finite calculus and metric: PASS

At a finite state define `h=tanh(wu)`, `z=Ah`, `H=tanh(z)`,
`δ=c φ'(z)`, `Q=Aᵀδ`, and `f=cᵀH/n`. In the stated metric the predictor
gradient has blocks

`(φ'(wu)Q uᵀ, δhᵀ/n, H)`.

Indeed pairing these with `(dw,B,dc)` gives

`Qᵀ[φ'(wu)dw u]/n + δᵀBh/n + Hᵀdc/n`,

which is the ordinary differential of f. Thus the negative loss field is
`−2∫r` times these blocks, with precisely the loss factor two and middle
factor `1/n`. This also gives the dissipation identity and the finite
compact-time displacement bound used in the packet. The finite metric and
HS rank convention agree with DEP 425–505 and 949–1002.

For the clock primitive,

`F'(z)=cosh²z=1/φ'(z)>0`, and `F(z)` tends to the corresponding infinity
at both ends. Therefore `j(X,g)=F⁻¹(F(g)+X)` is globally defined and
`j_X=φ'(j)`. Since initialization is fixed under the law perturbation,
`δw_a=φ'(w_a)ξ_a` without an initial-root variation. At an active axis
input the two first gates in the transformed vector field cancel
**identically** before differentiation:

`Ẋ_a=−2p_a r_a Q_a`.

Its differential is

`ξ̇_a=−2p_a(e_a[v]Q_a+r_a q_a[v])+b_{X,a}`.

Differentiating the middle and readout ranks gives P8–P11. In particular
`δh_a=φ'(w_a)²ξ_a`,
`δz_a=BH_a+Aδh_a`,
`δδ_a=dφ'(Z_a)+cφ''(Z_a)δz_a`, and
`δQ_a=B*δ_a+A*δδ_a`.
These contain both matrix orientations and all three product terms in the
middle update. The absent own-gate curvature term is an exact clock
cancellation, not a dropped Hessian contribution. For a passive datum the
direct law derivative retains
`u_a φ'(w·u)Q(u)/φ'(w_a)` and the subtraction `σ=ν−ν*`.

Finite right differentiation in SECTION 1531–1588 is valid for nonatomic
laws as well as atomic ones. At fixed n, every parameter derivative of the
integrand is uniformly bounded on a compact parameter/data set. Energy
bounds give a common finite parameter ball for `ε∈[0,1]` on `[0,T]`.
The vector field is smooth there and affine in ε. Subtracting its integral
equations first gives `O_n,T(ε)` path differences. The exact mean-value
formula for the divided difference then gives uniformly convergent
coefficient matrices and direct law sources; a second integral inequality
proves convergence to the finite linear tangent equation. No constants
from this fixed-n argument are used to take the width limit.

At time zero the tangent state vanishes because every ε uses the same
arrays. The actual finite Gaussian readout is retained in all coefficients
and sources. The zero limiting readout is justified later by a comparison,
not substituted into the finite problem. The finite output differential
agrees with T14 and T7 by the same normalized pairings.

## 5. Dependency proofs and fitted reference: PASS

I checked the following supplied dependencies in their stated roles.

| Dependency unit | Verified role and relevant qualification |
|---|---|
| Finite dynamics, DEP 388–613 | Raw gradients, kernel normalization, energy, finite continuation, and width-independent initial norm events. The proof uses finite-dimensional norm equivalence only at fixed n. |
| III.F.1–6, DEP 620–905 | Fixed-program empirical W2 convergence; adaptive conditioning; Gaussian source response; singular-query regularization; causal contraction feedback. Instruction counts remain fixed. |
| III.F.7–11, DEP 907–1160 | Countable generated spaces, bounded initialized actions and actual adjoints; HS metric; strong multiplier/curve calculus; scalar gradients and fixed-cap Euler facts. These do not assert unrestricted L2 Nemytskii differentiability. |
| A.1–A.4, DEP 1167–1223 | Continuous at-most-linear value instructions, justified fixed-program source derivatives for admitted products, initialized action norm two, and the scalar/strong differentiation tools. |
| B.1, DEP 1230–1779 | Global orthogonal-reference clock construction, same-root stability, oracle/mesh width identification, and the actual vanishing finite readout. Its separate raw-GD bridge is not promoted to a GD derivative theorem. |
| C.4.1–C.4.2 excerpts, DEP 1786–2109 | Exact full-row fields, one-reference transport comparison, and a training-law-independent generated action realization. No omitted arbitrary-law global theorem is used. |
| C.4.5.1, DEP 2116–2742 | Symmetry, feature flow, fitting clock, endpoint and raw norm approach, initial activity calculation, complete rational constant certificate. |
| C.4.5.2, DEP 2745–3234 | Active-query source derivatives, fresh-root pulse estimates, uniform mesh source remainder, canonical endpoint L4 control, and finite-GF tail transfer. |

For adaptive Gaussian conditioning the critical distinction is that each
new input is fixed **after** conditioning on the existing transcript. A
matrix call then adds a linear observation of its residual Gaussian matrix.
The finite conditional formula uses the same matrix in the two directions.
The removed finite-rank noise projection has expected squared RMS
`rank(U)/n`. The source groups can be independent while the actual forward
and reverse answers remain dependent through response corrections.

Singular queries are handled without taking a pseudoinverse through a
rank change. A fresh independent input noise at each fixed call gives a
positive limiting Schur complement. Fixed-noise width convergence is
followed by noise removal; continuity of fixed-size positive square roots
and bounded derivative envelopes identifies the zero-noise scalar rule.
Finite same-array action bounds control the regularization error. The
completion argument obtains an actual adjoint by passing normalized finite
pairings through the fixed-program laws and then through density. The
sharp action bound two has a contained Gaussian comparison/Poincaré proof
in A.3; no outside concentration theorem is needed.

The reference feature equation has `c_s=h`, `(w,K)_s=J*c`, where
`h=(H_1²−H_2²)/2` denotes the difference of the **second-layer** features.
The scalar quantity `b=<c,h>` satisfies

`b_s=||h||²+||J*c||²=||θ_s||raw²`.

For `g=||c||`, `g_s=b/g` and
`g_ss=(||h||²−g_s²+||J*c||²)/g≥0` on its positive interval. The expansion
`c(s)=s h(0)+o_L2(s)` gives `g_s(0+)=sqrt(m)`, so that interval cannot end
at a new zero. It follows that `b_s≥m`. The rational certificate proves
`m=v/2≥1/10`. Thus the unique first `b=1` feature time is at most ten.

Population symmetry comes from invariance of the generated initialized
law and uniqueness, not from a samplewise finite-network symmetry.
Consequently the physical residuals are `(-e,e)` and `ds/dt=2e`.
Bounded continuous `b_s` at the feature endpoint makes the integral
`∫ds/[2(1−b)]` diverge there, so every finite physical time lies strictly
before it. Differentiation gives `e_t=−2b_s e` and `e≤exp(−t/5)`.
The raw path-length bound from `b_s=||θ_s||²` gives

`s†−s(t)≤e/m`, and `||θ(t)−θ∞||raw≤e/sqrt(m)≤sqrt(10)e`.

It also gives `||A||≤2+sqrt(10)`, `||c||2≤sqrt(10)`, and
`||c||∞≤10`, including at the endpoint. These are the actual hypotheses
consumed by the new propagator proof.

The active-query endpoint fourth moment is supplied, not inferred from
RMS convergence. In C.4.5.2 the tanh clock's root is first clipped, while
its derivative with respect to the changing clock remains bounded by one.
Readout clips are inactive on an open neighborhood of the reached bound.
The chronological source-derivative argument removes the root clip using
uniform source-derivative bounds; no derivative of the unbounded root map
is used. Fresh-root pulse estimates are at fixed mesh, followed by the
width limit and then the zero-pulse limit. Gaussian integration by parts
extracts precisely the named-source coefficients with deterministic
covariances and coefficients held fixed.

With `M=7,C=4,S=10`, the three stability coefficients sum to at most
`max(8,5+16s,11/2+56s)≤8+56s`, whose integral is 2880. The past reverse
coefficient sum is bounded by `2S P K exp(2880)=225400 exp(2880)`, the
learned contribution by `SC²=160`, and the current contribution by 20.
This verifies the stated `B_Q`. Cross-program Gaussian covariance
isometries pass the decomposition to the common endpoint, and an L2 limit
of remainders bounded by `B_Q` preserves that bound. Therefore
`Q_a,∞=ζ_a+R_a`, with Gaussian variance at most ten and `|R_a|≤B_Q`,
implies `||Q_a,∞||4≤3^(1/4)sqrt(10)+B_Q` without independence of the two
summands. This is the exact fourth-moment input used in P20.

The activity and certificate passages were also read completely. Their
initial reuse calculation retains both response terms in `A0*U` and
`A0V`. The rational exponential bounds, monotone endpoint quadrature,
Gaussian tail bound, and outward rounding have the stated directions.
The standalone certificate is byte-identical to the complete embedded
program. Its exact assertions and independent scalar quadrature both pass.
The numerical quadrature is supplementary; the rational comparisons are
the supplied proof of the constant margins.

## 6. Actual finite cavity and weighted forcing: PASS

This is the main probability bridge. Its proof does not treat a reached
query as independent of the column that helped train it.

On `E_n`, finite energy gives initial risk at most four, displacement at
most `2sqrt(T)`, and the displayed deterministic bounds

`B=10+2sqrt(T)`, `C=1+2sqrt(T)`, `W=2+2sqrt(T)`, `H=1+4T`.

Also `sum_a|r_a|≤4` and each `|r_a|<3`. The readout bound is pointwise,
while W is a full-row RMS bound. These distinctions are needed below.

For column i, the comparison flow starts from `A0−a_i e_iᵀ` and the same
g and actual c0, and it trains its entire middle increment and its own
residuals. It is measurable in the remaining initialized variables and
independent of `a_i`. The event `E_n^i` belongs to that remaining
sigma-field and contains `E_n`. Gaussian conditional bounds are applied
on `E_n^i`; conditioning directly on `E_n` would be invalid here.

The forward subtraction is

`ΔZ_a=A ΔH_a+ΔK H̃_a+a_i H̃_ai`,

and the reverse subtraction is

`ΔQ_a=AᵀΔδ_a+ΔKᵀδ̃_a+e_i(a_iᵀδ̃_a)`.

The use of full A on the first reverse difference avoids an extra
uncontrolled column-dependent term. The small forward error is
`||a_i||/sqrt(n)`, not an operator-norm estimate for the removed column.
For `x=sum_a RMS(ΔX_a)`, `k=||ΔK||F`, `z=RMS(Δc)` and `d=x+k+z`,
S22–S23 follow from bounded gates, the readout supremum, and the exact
rank norm. In particular the residual difference is bounded by
`2z+C V`; it is included in all velocity comparisons.

Writing `D0=1+B+C+H+3`, the crude substitutions

`V≤3D0 d+2ε_i`, `D≤8D0²d+4D0ε_i`,
`P≤10D0³d+4D0²ε_i+sum_a|Z_i(t,e_a)|/sqrt(n)`, and
`R_cav≤5D0²d+2D0ε_i`

indeed yield S24 with `L=100D0^4`; summing the displayed coefficients
uses at most `81D0^4` on d and `36D0³` on `ε_i`.
The integrating factor gives

`sqrt(n) sup_t d(t)≤J_T(||a_i||+2Z_i#)`.

The learned transpose term has the exact integral representation S27.
Its coordinate absolute value is at most `4TC²`, since the active feature
is bounded and the normalized backward pairing is at most C². Combining
this with the passive backward difference and `||a_i||≤10` on `E_n`
gives S28 with exactly the displayed `A_T` and `B_T`.

Conditioned on the remaining arrays, `Z_i(t,u)=a_iᵀδ̃(t,u)` is a centered
Gaussian process. Its conditional covariance is the normalized cavity
backward pairing. The RMS Lipschitz constants in time and u use only
the bounds above: `D_t=4+8HC(1+B²)` and `D_u=2HBW`. After the circle
parameterization the increment metric is bounded by
`(T D_t+2πD_u)||q−q'||1`. The dyadic two-parameter grid proof sums
`O(2^−k sqrt(k+p))`; its displayed constants are sufficient. This proves
`||Z_i#||p≤C_Z sqrt(p)` conditionally on `E_n^i`.

Since `1_En≤1_En^i`, S28 can be integrated with this conditional bound.
The result is an actual finite bound

`E[1_En N_ni^p]^(1/p)≤C_T sqrt(p)`

for every i, n and `p≥2`. Averaging yields S4. No independence of the
actual δ and `a_i`, no exchangeability-to-moments inference, and no
universal Lp mapping bound for a Gaussian action is used.

The inverse gate is controlled by the exact identity

`∂X cosh²j(X,g)=2tanh j(X,g)`.

Thus `cosh²w_a≤cosh²g_a+2|X_a|`, for either sign of X. Integrating the
active clock gives `|X_a|≤3T N_i`. Gaussian root exponential moments and
Hölder then give every separately fixed moment of
`(cosh²g_a+6T N_i)N_i`, `|w_i|N_i`, and their fixed products, without
assuming independence of roots and evolved queries. For example the
square tail is bounded by `C_p,T R^(−p+2)`. Markov's inequality and
`P(E_n^c)→0` give the required ordered uniform integrability statement.
RMS convergence alone would not establish this weighted step.

For uniform **population** bounds, the auxiliary finite feature equation
has controls of total absolute mass one, zero auxiliary readout, and
deterministic bounds on the entire interval `[0,10]`. It is used only to
identify and bound the canonical population feature flow. The actual finite
physical trajectory continues to have its actual Gaussian readout. The
same cavity algebra applies to this auxiliary equation, with residual
difference terms removed and with the displayed larger polynomial bounds.

At fixed mesh, A.1 and bounded action comparisons identify joint root,
clock, value, and passive-query laws. Same-root stability removes the
mesh in clock/HS/L2 norms. Applying bounded tests
`min(R,max_j|Q(s_j,u_j)|^p)` to finite rational lists transfers their
expectations; the event complement costs at most `R P(E_n^c)`.
Monotone convergence in R and then in the lists gives the countable
envelope `N#` with `||N#||p≤C_*sqrt(p)`.

For an arbitrary deterministic parameter, strong L2 continuity provides
an almost-surely convergent subsequence from the dense list. Thus the same
envelope bounds its equivalence class. Joint measurability and Fubini
give the assertion needed for each deterministic observation measure.
This step does not assume continuous population query sample paths.
The active clocks have absolutely continuous representatives, yielding
`sup_s|X_a|≤S N#/2`. Consequently

`|cosh²w_a Q(s,u)|≤(cosh²g_a+S N#)N#`.

Hölder with `||N#||4≤2C_*` and
`||cosh²G||4≤2^(1/4)e^8` proves the explicit bound S45. Restricting
the canonical feature flow to the actual physical clock proves T8 for
all physical time. This does not make the finite-width theorem uniform
in physical time.

Continuity of the weighted integrand also has a supplied proof. The
interpolation exponents `1/4=(1/3)/2+(2/3)/8` are correct. They combine
L2 query continuity with the L8 envelope to control a fixed L4 weight.
Changing the clock weight uses its derivative bound two; changing the
passive gate introduces only products of the Gaussian root and N# already
controlled above. This proves Hilbert-valued continuity, with the stated
1/3-Hölder upper estimate, on the compact feature/data set. The rank and
readout blocks are continuous in HS and L2. The continuous compact range
is separable, so every finite signed Borel measure admits its Bochner
integral.

Finally `|r|≤sqrt(10)+Y`, the middle rank norm is at most `sqrt(10)`,
the readout factor norm is at most one, and the row square sum is at most
`M_w² sum_a u_a²=M_w²`. This verifies exactly

`C_b,Y=2(sqrt(10)+Y)sqrt(M_w²+11)`.

Signed mass zero is not used to fake a two-sided probability neighborhood.
The linear extension is defined by this integral after the finite right
derivative has been identified.

## 7. Strong equation and uniform propagator: PASS

Let `R` multiply the row blocks by `D_a=φ'(w_a)`, and act as identity on
the other blocks. Then `||R||≤1`, but its inverse need not be bounded.
The equation is analyzed in the stronger clock norm, not by silently
replacing that norm with the raw norm.

For a unit tangent, bounded gates and the reference bounds give
`||h_a[v]||≤1`, `||z_a[v]||≤1+M`,
`||d_a[v]||≤a1=1+20(1+M)`, and `||q_a[v]||≤a_q=C+Ma1`.
The remaining rank and readout components are bounded by `a1+C` and
`1+M`. These verify P12–P13, including

`||C(t)||≤2a_*e(t)`, and
`||S(t)||,||E(t)||≤L0=sqrt(1+C²(1+M²))<17`.

The finite-rank synthesis/evaluation bounds use the two weights summing
to one; no extra factor of two is missing. The evaluation bound is also
consistent with `E=S*D`, where `D=R*R`.

Strong continuity is enough here. If a bounded multiplier converges in
probability, its product with a fixed L2 vector converges in L2 by
truncating that fixed vector. The reference action increment is
HS-continuous, and the readout is supremum-continuous because its feature
velocity is pointwise bounded. Applying the multiplier fact successively
to P8–P10 proves strong continuity on every fixed tangent. It does not
assert operator-norm continuity of all multiplication operators or
Fréchet differentiability of an arbitrary L2 nonlinear vector field.

At every state, adjunction yields

`E=S*D`, `Γ=ES=S*DS`, and
`αᵀΓα=||RSα||raw²`.

Since each finite-valued tanh preactivation has a strictly positive gate,
D is injective, though noncoercive. Thus

`ker Γ=ker S=ker E*`, and `ran E=ran Γ` in finite-dimensional R².

This compatibility excludes the nilpotent zero-mode problem. Positivity
of Γ alone would not exclude it. In particular if Γ is identically
zero then S, E and SE are zero. No full-rank assumption is needed.

Using `(SE)^j=SΓ^(j−1)E` and the range compatibility in the convergent
exponential series proves

`exp(−2τS∞E∞)=I+S∞Γ∞+[exp(−2τΓ∞)−I]E∞`.

Nonnegative eigenvalues of the finite Γ imply the bracket has norm at
most one. Its finitely many positive eigenvalues can be inverted for this
fixed endpoint without an assumed uniform gap. This proves the stated
finite `B∞`; it gives no useful evaluated condition number and no
continuity of pseudoinverses along a rank-changing family.

The actual nonautonomous perturbation is integrable in **operator norm**.
Factor subtraction gives the L2 field differences P18 and the finite-rank
bound `||S−S∞||≤a_*d_ref`. For E the extra row term is a changing
`φ'(w)²` multiplying the fixed `Q∞`. If that gate difference is b, then
`|b|≤min(1,4|Δw|)` and `E|b|4≤16||Δw||2²`. Hölder with the supplied
endpoint L4 moment therefore gives

`||b Q∞||2≤2M4 ||Δw||2^(1/2)`.

Hence `||E−E∞||≤a_*d_ref+2M4 sqrt(d_ref)`. This uses finitely many
representing fields; it does not elevate L2 convergence of a multiplier
to operator-norm convergence on the full Hilbert space.

Substituting `d_ref≤sqrt(10)e` yields P21. Integrating `e≤e^−t/5`
and `sqrt(e)≤e^−t/10` gives exactly

`J0=20L0 a_*sqrt(10)+10a_*+40L0 M4 10^(1/4)`.

This controls both residual curvature and the approach of the
Gauss–Newton finite-rank term to its endpoint. Merely integrating the
residual curvature would not have sufficed.

The ordered Picard integrals on each vector have the summable bound
`||v||L^j(t−s)^j/j!`, giving a unique strong evolution under bounded,
strongly continuous coefficients. Variation of constants about the
frozen endpoint then gives

`||U(t,s)||≤B∞ exp(B∞∫_s^t||L(q)+2S∞E∞||dq)≤B∞exp(B∞J0)`.

This proves the uniform bound for the actual nonautonomous propagator.
The forcing integral gives the unique strongly absolutely continuous
solution for `L1_loc` forcing and a strong C1 solution for the continuous
data forcing. The state and output bounds proportional to
`T||σ||TV` follow. They are not bounded-in-T forced-response assertions.

The endpoint projection `P∞=I−S∞Γ∞+E∞` is idempotent, has range `ker E∞`
and kernel `ran S∞`. With `G=R∞S∞`,

`R∞P∞=(I−GΓ∞+G*)R∞`.

Since `G*G=Γ∞`, `GΓ∞+G*` is precisely the raw orthogonal projection
onto the training-gradient span. This identity is on the admissible raw
image of the clock space. It neither requires bounded `R∞⁻¹` nor proves
that U itself converges to P∞. Unseen output signs and benefits are not
determined by this decomposition.

## 8. Actual finite tangent identification and limit order: PASS

The crucial consistency proof is present in SECTION 1692–1917. It does
not infer convergence of derivatives from value convergence.

First, clipping the inverse-gate weight and Q makes the source integrand
a bounded/Lipschitz coordinate construction on the reached state class.
The original source is uniformly approximated on `[0,T]×S¹` using the
finite weighted envelopes, in the ordered probability sense F14. A
deterministic partition of the compact data space then replaces ν by a
finite law with exact cell masses. Coupling points within their cells
gives F15. It does not require total-variation convergence of an atomic
law to a nonatomic one; nor does it divide by any atom weight or Gram
eigenvalue. Middle integrals are approximated in HS norm by the same
rank difference inequality.

At fixed cutoff, quadrature, and time mesh, expand every learned reference
and tangent middle matrix into its finite sum of ranks. Matrix calls then
use A0 or its transpose and a finite number of scalar contractions.
All coordinate maps have at most linear growth after an inactive readout
clip: for example `φ'(j(X,g))² ξ` has a bounded multiplier, and
`clip(c)φ''(Z)δz` is bounded times one varying tangent field. There is
no coordinate product of two unconstrained tangent fields. A.1 therefore
identifies the fixed oracle program. Causal empirical feedback is
transferred with scalar contraction inequalities and fixed-node square
tails. Singular query Grams are covered by the supplied fixed-program
regularization proof, not by an inverse-Gram estimate.

Actual finite c0 is retained in the finite mesh. Coupling its fixed
recursion to the zero-limiting-readout oracle starts with vanishing RMS
and supremum discrepancies. A finite induction transfers that error.
No finite physical flow is reset.

Reference Euler errors satisfy F17 in the clock/HS/L2 metric, with
width-independent constants on the initial event. Upgrading the B.1
middle distance from operator norm to HS is justified term by term:
rank differences obey the same bound, and an action of a HS difference
is bounded by its HS norm. The readout supremum is controlled separately,
not assumed to follow from its L2 error.

For the population tangent, the generators along reference meshes
converge **strongly on each fixed vector**, uniformly in time. Bounded
multiplier continuity proves this, and the common operator bound extends
it to the compact set of solution values. The integral consistency error
of tangent Euler tends to zero; multiplication of its error recurrence
by at most `(1+C_T h)` per step gives convergence F19. This first proves
population tangent convergence without assuming the finite tangent
comparison that is still to come.

For that finite comparison, the exact defect F20 is evaluated on the
finite mesh tangent at the preceding node. The second and third lines
are O(h) in integrated norm from the common generator bound, the reference
Euler error, and clipped-source Lipschitz continuity. The first line is
expanded into bounded action/rank errors and multiplier differences.
The complete list of tests includes `ξ^h`, `d^h`, `δz2^h`, and `Q_a^h`.
In particular the term `(c−c^h)δz2^h` is handled as a bounded multiplier
with small L2 argument change, not by an unproved supremum error for c.

For each such multiplier term, F16 gives

`RMS([b(z_n)−b(z_n^h)]V_n^h)`
`≤Lip(b) M RMS(z_n−z_n^h)+2||b||∞ RMS(V_n^h 1_|V_n^h|>M)`.

The population testing nodes over a chosen refining mesh sequence are
relatively compact in their L2 spaces: F19 gives the tangent convergence,
and the reference/action/strong-multiplier maps preserve the required
compact families. Their square tails therefore vanish **uniformly**.
At each separately fixed mesh, finite empirical tail tests converge
using its joint W2 theorem. There are only finitely many time nodes at
that stage. Weight their bounds by cell length and sum. Width goes to
infinity first, then h tends to zero at a fixed M, then M tends to
infinity. This proves F21 without a width theorem for an increasing
program or a width-uniform higher-moment bound on tangent nodes.

The actual finite linear equation has a deterministic operator bound
on `E_n`. Its discrepancy from the mesh is consequently at most
`exp(C_T T)∫||D_n,h||`. Source cutoff and quadrature errors are subsequently
removed with the same linear stability estimate. This establishes F22
for the actual finite derivative. The sequence of proxy choices may be
diagonalized by accuracy; its instruction count is still fixed before
each width limit.

For middle tangents, at fixed proxy

`||sum_j a_j δ_j⊗h_j||HS²`
`=sum_jk a_j a_k <δ_j,δ_k> <h_j,h_k>`.

The finite Frobenius formula is identical with normalized pairings.
Thus the joint fixed-program second moments identify the HS norm and
finite-rank pairings, and the same expansion identifies both actions
of the tangent. F22 passes them to the actual tangent. Products in the
named raw/hidden variations are handled with the same compact-family
square-tail argument. No cross-carrier operator-norm distance or hidden
tangent path-law convergence in coordinate supremum norm is asserted.

## 9. Whole-circle observation and general laws: PASS

The Riesz field for passive prediction evaluation is exactly F23. Its
row is `(u_aD_a φ'(w·u)Q(u))_a`, and the other blocks are `δ⊗H1` and H2.
Its norm is uniformly bounded on each finite reference horizon (and by
L0 in the population). Hence state proxy errors control scalar evaluation
errors. At each fixed time and input the remaining pairings are identified
by the joint finite-program and rank contraction limits.

Time equicontinuity is separately established. `Q=A*δ` is uniformly
L2-Lipschitz using the raw reference velocity, action norm and readout
supremum. Changing its first-layer gates uses its proved uniform square
tails, not a bound on a multiplier operator norm. The finite tangent has
`sup_t||v_n'||=O_P(1)` from its linear equation, common coefficient bound
and `sup_t||b_n||=O_P(1)`. Together these give the required scalar time
modulus.

For the circle parameter α, F24 is a strong curve differentiation:
`∂αH1=φ'(w·u)(w·u')`,
`∂αZ2=A∂αH1`, and
`∂αQ=A*[cφ''(Z2)∂αZ2]`.
The extra product when differentiating the row of the Riesz field is
`u_aD_a φ''(w·u)(w·u')Q(u)`. Its L2 norm is bounded by
`2|| |w|Q(u)||2`, supplied by the weighted finite/source estimates.
Thus no higher moment of the **tangent** itself is needed.

The population differentiation is also justified at the representative
level: the strong Q curve and its square-integrable derivative give
almost-everywhere absolutely continuous coordinate versions by Fubini.
The countable query envelope then bounds the continuous circle versions
at each fixed time. The gate difference quotient is dominated by the
L2-integrable `2|w|N#`; bounded multiplier continuity treats the other
product term. This proves the H1 statement, not merely a formal angular
derivative.

The fundamental theorem and Cauchy–Schwarz now give

`||ell(α)−ell(β)||≤|α−β|^(1/2)||∂αell||L2`.

The H1 norms are bounded in probability uniformly in finite time at
finite width, and deterministically for the population. Multiplication
by the bounded-in-probability tangent norm gives a whole-circle modulus
for the derivative predictor. Convergence on a finite time/circle net,
a finite union bound, and refinement of the two nets prove T10. A finite
list of passive points has not been substituted for the circle.

For nonatomic ν, the finite loss and finite forcing throughout this
argument are exact integrals. Quadrature is only a proof approximation.
The data constants do not depend on support size, a smallest atom mass,
or a perturbing-law Gram rank. The resulting convergence is for each
fixed deterministic ν; these estimates do not claim a supremum of
failure probabilities over all laws.

## 10. Adversarial checks and outcomes

These attacks were assessed against the strongest relevant version of the
claim, rather than against omitted stronger theorems.

| Attack | Failure signature | Actual outcome and claim affected |
|---|---|---|
| Loss/metric mismatch | Extra n or two in raw or clock tangent; wrong HS representative | Exact differential and independent complex-step check agree. Finite identity rung passes. |
| Suppressed transpose reuse | Replacing A* by A or independent noise gives the same result | The derivation requires A*; the fixed nonsymmetric check detects a 0.44144 discrepancy from the wrong orientation. |
| Conditioning on an event involving the removed column | Conditional query ceases to be Gaussian | The proof uses the column-independent event `E_n^i`, then `E_n⊂E_n^i`. Attack is resolved. |
| Frozen cavity or prescribed residuals | Missing residual feedback invalidates deletion error | The cavity trains its full K and own c and residuals; S22–S23 retain residual differences. |
| Weighted tail escape | RMS convergence with divergent inverse-gate source moments | Actual finite subGaussian query-value moments plus the exact linear-in-X gate envelope give higher weighted moments and uniform square tails before width passage. |
| Incorrect canonical population source | Only marginal subsequences or an unrelated feature model | Fixed-mesh common actions, same-root/HS error, finite lists and monotone envelope passage identify the actual canonical feature segment. |
| Singular Γ with nilpotent SE | Γ nonnegative but exponential grows polynomially | This happens in the independent incompatible example, but kernel compatibility follows from injective D for the theorem. |
| Hidden coercivity assumption | D tending to zero destroys the finite-rank argument | The independent infinite noncoercive example has the exact compatible projection. The proof needs injectivity, not coercivity. |
| Nonnormal amplification ignored | Stable eigenvalues falsely imply contraction | A fixed positive ill-conditioned metric has gain about 4323.32; the theorem exposes conditioning in `B∞` and never claims contraction or a useful universal constant. |
| Residual decay alone used for all-time propagation | Uncontrolled moving Gauss–Newton part | P18–P22 separately make the full endpoint perturbation integrable, using the active endpoint L4 moment. |
| Differentiation of a nonexistent population map | Formal source offered as finite derivative capture | Fixed-n parameter differentiation is proved first; F20–F22 separately identify its width limit. |
| Fixed-program/growing-mesh interchange | Uniformity asserted for unbounded transcript length | The proof orders width, mesh, and fixed-vector tail cutoffs explicitly and uses compact population testing families. |
| Incorrect readout substitution | Actual finite c0 replaced by zero | c0 is retained in the actual finite flow and its tangent; zero is used only in a justified oracle/auxiliary-feature comparison. |
| Atomic approximation of nonatomic laws in TV | Claimed convergence is impossible for the chosen topology | The proof approximates the continuous source integrand by within-cell transport and retains exact cell masses. |
| Finite passive list offered as whole-circle convergence | No quantitative observation modulus | F24–F26 supply H1 control through `|w|Q`, followed by finite-net refinement. |
| Endpoint or benefit overclaim | A projection is claimed to control changed-law endpoints or risk | Neither follows and neither is claimed. Uniform population propagation and fixed-horizon finite capture remain separate. |

An explicit independent noncoercive infinite-dimensional check is useful.
On ℓ² let `s_k=2^−k` and `D_kk=4^−k`, for `k≥1`, and set `S=(s,2s)`.
D is bounded and injective but has no positive lower bound. The exact
geometric sums are

`||s||²=1/3`, `<s,Ds>=1/15`, and `||Ds||²=1/63`.

Thus `Γ=(1/15)(1,2)(1,2)ᵀ` has eigenvalues zero and 1/3, and
`Γ+=(3/5)(1,2)(1,2)ᵀ`. The endpoint projection is
`P=I−15s(Ds)*`; its idempotence follows from `15<s,Ds>=1`.
The correction norm is `15/sqrt(189)≈1.09109`. This directly confirms
that noncoercivity does not create a missing endpoint argument in the
stated finite-rank setting.

Conversely, `S=(1,0)ᵀ`, `E=(0,1)` has `ES=0` while SE is nonzero and
nilpotent. Its exponential is `I−2tSE`, with unbounded norm. This rejects
the weaker assertion that positivity of ES alone proves stability; it
does not contradict the packet's stronger compatibility proof.

At zero limiting readout the direct row and middle data sources vanish,
whereas the readout source equals `2∫yH2 dσ`. This boundary follows
directly from the finite formulas and is verified in the independent
fixed-state check. It confirms both the sign and the distinction between
a limiting initial boundary and the actual nonzero finite readout used
in the main test.

## 11. Commands, outcomes, and retained evidence

The exact scientific check commands were:

```text
/usr/bin/python /home/amir/Codes/PDE/studies/trained_data_response/P1_CHECK_IDENTITIES.py --output /home/amir/Codes/PDE/data/generated/trained_data_response/scientific_p1_b/identities
/usr/bin/python /home/amir/Codes/PDE/studies/trained_data_response/P1_REFERENCE_CERTIFICATE.py
/usr/bin/python /home/amir/Codes/PDE/data/generated/trained_data_response/scientific_p1_b/independent_checks.py
```

Each ran with the assigned scratch as its working directory and with
`PYTHONDONTWRITEBYTECODE=1`. All three returned exit code zero. There
were no failed checks, retries, discarded cases, or post-outcome tolerance
changes. The independent checklist and tolerances were written before
its execution. All checks are fixed algebra or deterministic constant
evaluation, not optimization trajectories.

| Check | Outcome |
|---|---|
| Supplied tangent central differences | Errors `1.0292819331e−6`, `2.5732050750e−7`, `6.4330121850e−8`, `1.6082636076e−8`; the fourfold reductions and required final threshold pass. |
| Supplied loss/metric pairing | Error `7.9006801101e−12`. |
| Supplied singular semigroup identity | Maximum displayed error `1.5265444420e−14`. |
| Complete rational reference certificate | `[0.392108947877, 0.396376711612, 0.233120735618, 0.339792209687, 0.631761866359]`; all exact rational assertions pass. |
| Independent entire clock-field complex-step derivative with simultaneous signed-law change | Error `6.5393208011e−16` at the fixed nonsymmetric four-neuron fixture with nonzero stored readout. |
| Independent passive predictor and both adjoint/rank pairings | Errors zero at displayed floating precision. |
| Wrong-transpose discriminator | Discrepancy `0.441442235678082`, exceeding its precommitted detection threshold. |
| Initial zero-readout source boundary | Row and middle source exactly zero; readout source norm `0.5417002087005528`. |
| Clock envelope, both signs and roots ±8 | All seven fixed algebraic boundary cases pass; maximum scaled equation residual below `3.1e−16`. |
| Independent compatible singular projection/semigroup | Largest error `5.7606676093e−15`. |
| Ill-conditioned positive metric | `Γ=2e−8`; at the fixed time `1/Γ`, exponential norm `4323.323658353702`, identity error `1.36e−20`. This is a matrix exponential check, not training. |
| Incompatible nilpotent factorization | At the checked time the norm is `20.04987562112089`; exact formula proves unbounded growth. |
| Independent Gaussian scalar quadrature | `q≈0.3942944904`, `v≈0.2364504105`, `a0≈0.3415092073`, `r0≈0.6365445625`; all rational packet bounds are respected. |
| Embedded/standalone certificate | Byte-identical, including all 56 scientific program lines. |

The scalar quadrature integrates `[0,12]` and doubles by symmetry. Its
Gaussian two-sided tail bound beyond 12 is below `3.58e−33`; its floating
results are not presented as an independent exact integration certificate.
The proof rests on the supplied rational enclosure argument, whose
complete executable was run. Runtime versions were Python 3.10.12,
NumPy 1.26.4 and SciPy 1.13.0.

The scratch retains:

- `review_identity.json` and `review_scope_and_coverage.json`;
- `input_hashes_before.json`, `input_hashes_after.json`, and
  `required_skill_hashes.json`;
- `provided_checks_commands.json`, both supplied-program stdout/stderr
  files, and `identities/results.json`;
- `independent_check_plan.md`, `independent_checks.py`,
  `independent_checks_command.json`, its complete stdout/stderr, and
  `independent_checks_results.json`;
- `final_audit.json` recording post-review hash and artifact checks.

The independent script SHA-256 is
`b538b70a128565324a8df5eb71f557fd1123ed67f3aac8de027b9f797e8b72ef`.
The retained machine-readable logs carry exact argument lists, working
directories, return codes, durations, and completion timestamps. Source
reading commands used `cat` for complete short files and
`nl -ba <allowed-file> | sed -n '<start>,<end>p'` for the numbered ranges
recorded above. Hashes were computed with `hashlib.sha256` on raw bytes;
no Git operation was involved.

## 12. Component verdicts, gaps, and optional suggestions

| Component | Verdict |
|---|---|
| Model, initialization, loss and raw/clock metrics | PASS |
| Finite right differentiation and actual finite readout | PASS |
| Fixed-program foundations, canonical action and adjunction | PASS |
| Fitted reference, endpoint estimates and active L4 input | PASS |
| Column-deleted cavity with correct conditioning and residual feedback | PASS |
| Conditional whole-query Gaussian process bound | PASS |
| Actual finite weighted moments and uniform integrability | PASS |
| Canonical population envelope, continuity and signed-law forcing | PASS |
| Strong linear equation on the stated Hilbert space | PASS |
| Singular endpoint compatibility and bounded frozen semigroup | PASS |
| Integrable actual coefficient perturbation and uniform propagation | PASS |
| Actual finite tangent capture with the stated mesh/width order | PASS |
| Fixed Borel laws, including nonatomic laws | PASS |
| Whole-circle observation and compact-time supremum | PASS |
| Proposed guide and navigation changes | PASS for the scoped C.4.6 claims |

**Surviving gaps and required corrections:** none for the exact proposed
claims. In particular I am not making acceptance conditional on an
unlisted specialized theorem, a numerical training result, or a future
proof of the finite tangent identification.

The added guide statements at ANC 159, 267–272 and 294–300 accurately
describe finite-GF derivatives on each fixed horizon and uniform
population homogeneous propagation. They do not turn the latter into an
all-time finite-width theorem. The explicit guide limitation to
linear-in-horizon total-variation response control agrees with T12.
The statement does not establish a nonlinear changed-law population
flow, a finite-contamination remainder, a law-uniform failure bound,
changed-law endpoint continuity, risk benefit, or a GD derivative.
It also does not identify a limit of the nonautonomous U with P∞ or
claim bounded response under permanent forcing. These exclusions are
substantive and remain in force under this ACCEPT verdict.

**Optional suggestions, not conditions of acceptance:**

1. A brief reader-facing cross-reference at F21 to the already proved
   population convergence F19 would help readers notice why its compact
   testing-family argument is not circular. The complete argument is
   already present in SECTION 1857–1867.
2. If the constants are discussed elsewhere, preserve the distinction
   between a finite explicit expression for `C_U` and a computed useful
   numerical bound. The present section makes that distinction correctly.

**Final scientific disposition: ACCEPT.** No established file was changed.
