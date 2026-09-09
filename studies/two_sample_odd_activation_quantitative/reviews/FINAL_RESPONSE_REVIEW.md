# Independent complete-proof response audit

Date: 2026-09-07.

**Verdict: PASS.** The audited candidate proves the full odd two-input L3 theorem for
`0 < e <= c_poly delta^800`, with the stated absolute positive `c_poly`, and hence
for the convex mixture `theta_delta = c_poly delta^800`. This verdict covers the
source construction and the global population/GF/raw-GD conclusions, rather than
only the affine comparison or nonaffinity components. I found no blocking
mathematical gap in the candidate at the hashes below.

## Scope and candidate identity

I read CONTRACT.md, CANDIDATE_HASHES.json, and all four mathematical candidate
files in full. I independently computed the following SHA-256 hashes; all agree
with the candidate manifest.

| File | Independently computed SHA-256 |
|---|---|
| PROOF.md | `0a7dbd32cb9cc291e706813b59c0142394e6f9532244e52c21a5ab5d89ed4d02` |
| AFFINE_POLYNOMIAL_BOUNDS.md | `8387e2f253063c139dacb282ca9f2372478521f54b33a9ef6c8dbd83f2b521ca` |
| POLYNOMIAL_RESPONSE_LEMMA.md | `51b0f717b33ed618219e086d32b16a95ef4253892171597d1805dd9d37a64f7f` |
| OLD_THRESHOLD_AND_NONAFFINITY.md | `c63753a83e832793c886b8ae8c122e30e0c01864b86a1a5dc9bee030852f9210` |

I used the solve-math-rigorously skill. I did not read other review reports,
status files, or prior conversations; historical status language in mathematical
source documents was not a premise. I made no proof edits, ran no experiments,
delegated no work, and made no commits.

Mathematical dependencies inspected substantively include the old theorem's
model and observable statement, AFFINE_CORE.md, SOURCE_AND_LIMIT_BRIDGE.md,
INITIAL_MOTION_AND_NORMALIZATION.md, and the attached source equations and probe
identity in TWO_SAMPLE_SOURCE_BASELINE.md. I also checked the Gaussian
conditioning, singular-query regularization and common-action/adjunction
construction in L3_LOCAL_COMPLETE_PROOF.md, the full
PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md, and the hypotheses, product-query
argument, deterministic velocity comparison and finite GF/GD limit argument in
FIXED_CAP_VELOCITY_BRIDGE.md.

## 1. Exact coefficient system and Jacobian

The affine equations in response-lemma (2) agree with the original formal-source
convention. For example, with arrays and moments frozen,

    H2 = a xi2 + a^2 A2 (zeta2 + B3 H2),
    delta2 = a (zeta2 + B3 H2).

Their indicated formal derivatives are `V = R a^2 A2` and `W = a^2 B3 R`.
The bottom equation gives `F = (I-K1 B2)^(-1) K1`; the top equation, with its
shared readout and strictly earlier readout update, gives
`T = K3 (I-A3 K3)^(-1)`. There is no extra control factor in a formal return.
The controls occur in K1/K3 and separately in learned-moment additions, exactly
as in baseline equations (7)-(10).

Differentiation yields all four equations of response-lemma (6). In particular,

    dV = a^2 R (dA2) L + V (dB3) V,
    dW = a^2 L (dB3) R + W (dA2) W.

The identity `I+B3 V=L` supplies the first cross term; the corresponding right
identity supplies the other. The learned moments are correctly treated as
external forcing in this Jacobian. Their nonlinear discrepancy is supplied by
the separate raw comparison, so no derivative of a covariance or learned
moment has been silently omitted from the nonlinear coefficient closure.

Although some cross-block terms contain identity factors, every feedback cycle
contains a strict temporal transfer. Consequently the finite-mesh inverse is a
finite chronological expansion. Backward current diagonals are permitted in
the domain of the linearized problem.

## 2. Backward-row forcing and sample sectors

The algebraic shift in response-lemma (7) is exact. Substituting

    Ytilde3 = Y3-J3,
    Ytilde2 = Y2-a^2 L J3 R-J2

leaves the homogeneous system unchanged and produces precisely
`F J2 F + a^2 F L J3 R F` and `V J3 V` as additional forward forcing.
No term involving a backward diagonal disappears.

The sandwich estimate is valid on arbitrary positive meshes: a strict kernel
on the right contributes `h_j`, a strict kernel on the left contributes an
integrable row weight, and the middle kernel needs only an absolute row bound.
In particular, `FL=F+F B3 V` and `RF=F+V B3 F` have polynomial strict densities.
At the baseline their densities can be bounded by `2 B^4`; hence the shifted
forward forcing has a bound of order `B^9` times the original mixed forcing
norm. There is no division by the smallest mesh step.

After label folding, exchange symmetry makes the forward arrays diagonal in
the orthonormal sample basis. The affine top backward field is the shared
`a C`, and its formal forward-source dependence is active. Thus B3 has only a
`++` block, and the middle equation gives the same property for B2. Their
learned moments have the same block support. It follows that `T X3 T` and
`W X2 W` vanish in the other three sectors. In each such sector the order
`Y3, Y2, X2, X3` solves the forced equations without feedback. These statements
concern formal source derivatives, including off-support directions, rather
than differentiation along a singular Gaussian support.

## 3. Positive Gaussian scaling bounds the actual coupled inverse

Scaling the initialized active first root and both hidden matrices by beta,
with zero population readout, gives the quartic-gradient homogeneity
`Theta_beta(s)=beta Theta_1(beta^2 s)`. The raw metric, controls, gain and mesh
are unchanged. Scaling matrix variance to `beta^2` multiplies every initialized
matrix return by `beta^2`: this also follows directly by applying the original
source formula to `W=beta G` and expressing its reverse source as beta times
the standard-variance reverse source. The learned terms do not acquire this
additional prefactor. Equations (9)-(10) therefore have the correct scaling.

The active positivity argument is valid. In normalized active raw coordinates
every affine Euler update has positive step and gain factors and uses additions
and products of the initialized centered Gaussian coordinates. Its raw
coordinate polynomials have nonnegative coefficients. Expectations of products
have nonnegative Wick contributions, so the active learned moments are
polynomials in beta with nonnegative coefficients. The strict chronological
source recursion preserves this property for the coefficient arrays. This does
not assert positivity of individual Gaussian weights or of a realization.

For strict times the active leading terms satisfy

    F_kj >= a^2 v h_j,       V_kj >= a^4 v h_j,
    T_kj >= a^2 h_j,         W_kj >= a^4 h_j.

Thus the beta derivative gives nonnegative forcing of at least `h_j/(8B)` in
the needed forward components. Nonnegative coefficient polynomials obey
`f'(1) <= f(beta_*)/(beta_*-1)`, including after summing a backward row.
The enlarged-scale input bound consequently gives `||C'|| <= B^2`.
Entrywise positivity of the chronological inverse then proves the claimed
`8 B^3` bound for forward-density forcing. Combining the shift, reconstruction
and the three acyclic sectors gives the conservative `10^6 B^20` full inverse
bound. It controls arbitrary mixed coefficient forcing; a raw tangent bound
alone would not have established this conclusion.

The enlarged interval is available: the normalized reference has a further
`1/(1000 R_delta^2)` interval in the stated larger ball, whereas
`beta_*^2 T-T <= 6/(10^5 R_delta^2)`. The added integrated Hessian cost is
bounded. Sufficiently fine Euler approximations inherit the margin; no exact
Euler time-dilation identity is assumed.

## 4. Same-array resolvents and nonlinear values

The neighborhood argument uses causal row bounds and strict densities in the
appropriate places. The identities for R1, R, L and R3 are exact. The equations
`F=F0+F0 DeltaB2 F` and
`V=V0+a^2 R0 DeltaA2 L+V0 DeltaB3 V` preserve strict densities by the sandwich
estimate. The bound `D<=1/(100B^6)` suffices for the displayed absorptions.
The resulting row estimates `5B^3`, `9B^3`, and the top strict density `10B^4`
are valid with slack. The displayed first-variation formulas and their second
variations give a polynomial quadratic remainder well below `10^20 B^100 D^2`.

The value equations are compared to affine equations at those same arrays,
rather than to a different covariance realization. At each layer the residual
nonlinearity is bounded by `e pi/2` or `e |q|`. Direct substitution, followed by
the exact resolvent, yields an absorbable `e` times the source norm. The source
Gaussian standard deviations already come from the primal estimate.
The explicit bottom, middle and top inequalities in Section 7 have enough
coefficient slack, and imply `X_p <= 2 Rstar sqrt(p)` for all `p>=2`.
This argument uses only L2 bounded actions for construction; it does not infer
Lp boundedness for arbitrary inputs of a canonical action.

## 5. The derivative exponential contains only perturbative drift

The local derivatives have exactly the three forms in Section 8, with
`G-aI` and `Vgate-aI` bounded by e and `Lgate` bounded by `e Q_r`.
For the middle equation, subtraction at the same coefficient arrays and
application of R gives precisely the displayed substitution at response-lemma
lines 242-243.
The bottom and top substitutions have the corresponding strict transfers.

Every unknown perturbative derivative therefore passes through a strict
transfer, with rate bounded by `10^4 B^6 e(1+Q_r)` and weight `h_r`.
The bounded backward rows control the additional prior-time sums. A single
transpose-source injection retains its `h_j`, whereas a whole forward-source
derivative row is estimated together, including its identity injection. This
explains why the argument does not pay for the number of source slots.

The envelope with `Lstar=10^8 B^50` follows by discrete Gronwall and has exponent
`Lstar e (s_k+sum h_r Q_r)`. Terminal backward outputs have the additional
`1+e Q_k` factor. The current returns are exactly

    B3_kk = diag(E Lgate3_k),
    (B2_kk)_ij = 1_{i=j} E Lgate2_k,i
                 + (B3_kk)_ij E[Vgate2_k,i G2_k,j].

Both terms of the second line are included in the backward-row defect.
Jensen with the deterministic mesh weights, followed by the subGaussian
moment estimate and fixed-order Hölder, bounds the necessary envelope and
endpoint moments. There is no random maximum over all source times and no
nonperturbative exponential `exp(Lstar S)`.

The defect bounds in (22) have ample slack: the explicit products use at most
two Lstar factors, finite powers of Rstar, time sums bounded by S, and the
backward coefficient row. They fit below `10^30 B^200 e` in each required norm.

## 6. Bootstrap arithmetic

Combining the actual learned-moment discrepancy, same-array derivative defect,
quadratic remainder and full coupled inverse gives

    D <= 2*10^36 B^220 e + 10^26 B^120 D^2.

At `d0=(4*10^26 B^120)^(-1)`, the quadratic term is `d0/4`. Under
`e<=10^-70 B^-400`, the ratio of the linear term to `d0/4` is at most
`3.2*10^-7 B^-60`, less than one. The finite-cap, finite-transcript amplitude
homotopy is continuous and starts at zero discrepancy, so it cannot first exit
this neighborhood. The resulting bound `D<=4*10^36 B^220 e` follows.
Also

    e Lstar S Rstar <= 10^-58 B^-329,

which closes the moment prerequisite used above. Thus the proof is not a
circular assertion of the source bounds that it later needs to remove caps.

## 7. Affine geometry, nonaffinity and the input B_delta

The normalization `p=P1/sqrt(v)`, `D=sigma C`, `t=lambda s`, with
`lambda=a^3 sqrt(v)`, preserves the raw active metric. The three operator
balances and `||p||^2=1+c^2` follow by direct differentiation. They imply the
claimed operator bounds. Gradient ascent gives
`Fdot>=2c^4(1+c^2)` and hence `F^2>=(2/3)c^6+(1/2)c^8`.
Radial convexity supplies `c>=t` and `cdot>=c^3/sqrt(2)` after zero.
These prove existence through the target, `T<2`, `c<=M`, and the logarithmic
integrated curvature bound. The Hessian retains its factor lambda in the full
raw metric, including perpendicular first-layer variations.

The radius-one comparison differentiates only the affine field and uses the
cap-uniform `40 e b^3` same-state forcing. The constants C0, Cz and Cg and their
powers of lambda are consistent with the stated Gronwall and forward estimates.
The finite-array path-length certificate follows from the integrals of the HS
update norms and fixed-mesh contraction convergence, with no trained
operator-norm convergence assumption.

The lower reference variances `1`, `1/404`, `1/16` follow from the balances,
radial bound and the old frozen inactive Gaussian fields. I checked the Hermite
identities and the explicit positive eta_* in the affine companion. The optimal
arctangent regression slope lies in `[0,1]`, giving the claimed 1-Lipschitz
square-root residual transfer in W2. The restriction `e<=c_* delta^(7/4)` therefore
preserves both the endpoint margin and `e^2 eta_*/4` nonaffinity.

The input exponents in PROOF.md Section 4 are sufficient. In particular,
`b_delta=O(delta^-1/8)` and `G_delta=O(delta^-5/8)` give forward density exponent
`7/8` and backward-row exponent `11/8`. Raw and preactivation comparison costs
have exponents `3/2` and `7/4`; the learned-moment entry discrepancy has exponent
`15/8`. The extra backward-row time sum is explicitly paid by `B^2 e` in the
interface. Every input thus fits `B_delta=C_B delta^-2`. The displayed enormous
numerical C_B dominates the elementary constants, enlarged-scale margins,
sample-basis factors and Gaussian probe costs; no delta-dependent constant has
been hidden in it.

Consequently `c_poly=min(1/4,c_*,10^-70 C_B^-400)` is absolute and positive, and
`e<=c_poly delta^800` implies both independently required smallness conditions.
The old deliberately conservative selection and its upper bound
`C delta^6 exp(-c/delta^6)` are also correctly distinguished from a necessary
restriction on the theorem's largest possible coefficient.

## 8. Complete theorem and limits

The new source bounds provide exactly the cap-uniform Gaussian L2 incoming tails
needed by the asymmetric comparison bridge. Its error
`C exp(C(1+eR)S-cR^2)` tends to zero for each fixed admissible delta and e.
The comparison is in the common raw state spaces and also controls directions,
so it gives an autonomous uncut strong C1 feature path. Comparing arbitrary
bounded-primal competitors to the capped reference requires only reference
tails. The same estimate proves uniqueness and restart from reached states.

Label folding and exchange symmetry apply to capped finite programs before
limits. They give the population scalar predictions and the endpoint `g(S)>1`.
The first-hit clock diverges by the bounded derivative of g. This constructs a
single global physical solution while using only a bounded feature interval.
The cap clock does not require a gradient or monotone capped g. Physical
uniqueness uses both actual residuals for a competitor and imposes no symmetry
on that competitor.

Fixed-cap physical finite-program identification and width-independent stopped
Euler comparisons give the full-sequence GF limit. The raw-GD comparison uses
the uncut field at the preceding GD node and the cap reference at that node;
its additional error is `C_{R,T} n^-2`. It needs no uncut Lipschitz constant
uniform in width, no finite-width scalar clock, and no Gaussian theorem for a
growing transcript. The original finite random readout is retained.

The fixed-cap velocity bridge requires only bounded primal paths, fixed-cap
Lipschitz estimates and the finite-program/common-action rule. These hold for
the present gain family. Appended velocity product queries are first truncated;
their expected-response and learned-memory terms remain present. Removing the
cap at fixed reference-velocity truncation, then removing that truncation, uses
the compact L2 time image of the uncut velocity. It avoids any assumption about
the growth of cap-dependent velocity moment constants. The resulting velocity
and second-moment convergence, together with the path interpolation inequality,
gives the stated same-layer path-space W2, uniform-time velocity laws and
integrated squared speeds. Both action orientations, actual adjoints and all
four raw kernels are preserved.

Finally, the old odd-family initial-motion proof applies at every positive e
in the present gain range. Its full initial feature support, positive-definite
transpose second moments, both reused-matrix response terms and sample symmetry
give every stated hidden block/sample acceleration and the changing projected
kernel. No additional angle-dependent amplitude threshold enters there.
The regression margin survives the strong limits at every finite physical
time. The convex and Gaussian-energy-normalized families lie in the proved gain
rectangle as claimed.

The conclusion is a sufficient polynomial coefficient theorem with exponent
800. It establishes neither an optimal exponent nor a practical-size mixing
coefficient, and it asserts finite-interval convergence for each fixed dataset,
as required by the contract.
