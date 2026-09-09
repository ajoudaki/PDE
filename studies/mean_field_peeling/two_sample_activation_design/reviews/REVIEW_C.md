# Independent adversarial review C

Date: 2026-09-08.

**Verdict: PASS for Theorems A and B, the stated initial-motion conclusion,
and the proved supporting lemmas, at the frozen hashes below. No required
mathematical repair was found.** The verdict does not certify moderate
nonlinear amplitudes, one fixed positive amplitude for all separations,
or any provisional closure estimate in the supporting notes.

This was an independent proof-only review. I read the seven new mathematical
files in full, checked the mathematical dependencies actually needed by
their argument, and used the rigorous-math skill. I did not read previous
or sibling reviews, status files, README files, preparation notes, ledgers,
or historical work directories. Historical verdicts appearing inside the
permitted mathematical sources were not used as premises. No experiment,
delegation, or proof-file edit was performed. The only new file is this
review. Hash computations were integrity checks, not mathematical evidence.

## 1. Frozen candidate and dependency integrity

All eight entries of `CANDIDATE_HASHES.json` match their current files:

| File | SHA-256 |
|---|---|
| PROOF.md | c36d92166c65affeb7974c5fe07ddfaa8697399b56d3c4322e89db51a02748ce |
| SHAPE_SYMMETRY.md | 58432555e59bc191e98cb7fda7e1063d22410933c2cb5816003f6e5bbe061540 |
| LINEAR_GROWTH.md | 5e06d3414959abef70cfbe569f1b393df689ad3826e31d391149d556ad861bd9 |
| AFFINE_POSITIVITY.md | d87609ed88ed1d31ee3a9a32363e813ad4f30721b455737aa208db1c9bfaba81 |
| BOUNDED_ACTIVATION_ROUTE.md | 018e912b6b6e434c26eea0ea9a4c499952f9ffbff4c2cb4b235f18a2f61fa381 |
| RELATIVE_NONLINEARITY.md | bcaa95026a90736f32cd4e2cdd8f2a662439afa20051abb9522918becab2070f |
| SINE_INITIALIZATION.md | 55be13083cc6a61967e7e993a819c92a1e8ef981de858294a99e67e6fe335e72 |
| DEPENDENCIES.json | 3f5916ff969e28e8fb3b899d91813a654802ab00c346baff82f1dede2d38d012 |

All 28 source-file hashes listed in `DEPENDENCIES.json` also match, using
its parent-directory base. A hash match is not treated as a proof verdict.

## 2. Mathematical coverage

The main dependency audit included the complete power-four
`AFFINE_PROPAGATOR.md`, `PRIMAL_L2_RESPONSE.md`, and
`SECTOR_SUPERSOLUTION.md`, and the full power-four assembly. I also read
the complete power-ten `AFFINE_SOURCE_CERTIFICATE.md`,
`REFINED_RESPONSE.md`, `POSITIVE_SUPERSOLUTION.md`, and
`NORMALIZED_GATES_AND_PRIMALS.md`; the quantitative
`AFFINE_POLYNOMIAL_BOUNDS.md` and the quantitative assembly's source/probe
interface; and the complete odd-theorem `AFFINE_CORE.md`,
`SOURCE_AND_LIMIT_BRIDGE.md`, and `INITIAL_MOTION_AND_NORMALIZATION.md`.

For the population and algorithm conclusions I checked the exact original
theorem/model and observable statement, `CONTRACT.md`, the complete
`TWO_SAMPLE_SOURCE_BASELINE.md`,
`PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, and
`FIXED_CAP_VELOCITY_BRIDGE.md`. I read the full generic finite Gaussian
conditioning, singular-query regularization, common generated-action and
adjunction proofs in `L3_LOCAL_COMPLETE_PROOF.md`, and the strong radial
and raw gradient/chain-rule proofs in `SYMMETRY_RADIAL_CLOCK.md`.

This coverage follows the operative proof chain. Superseded arctangent
thresholds, old bounded-activation local bootstrap results, and older
assembly conclusions are not additional premises of this verdict.

## 3. Exact model, symmetry, and singular geometry

The raw metric produces the displayed factors $1/d$, $1/n$, and one
in the four update blocks. The initial finite readout has normalized
size $O_P(n^{-1})$ and remains present in GF and GD. The new theorem
does not replace the actual two finite residuals by a scalar clock.

For nonodd activations the sample exchange/readout-sign transformation is
valid: after absorbing the first label into the readout, it sends forward
fields by $P$, backward fields by $\tau P$, and predictions by
$\tau P$. The scalar feature objective and initialized law are invariant.
Deterministic fixed-program prediction contractions therefore give
$f_i=y_i g$ before uncut uniqueness is invoked. The odd clipping map
preserves this symmetry even when the activation is nonodd.

The two distinct bases are essential and correct. Direct multiplication
gives

\[
Q_f\Gamma\operatorname{diag}(y/2)Q_b^{-1}
=\operatorname{diag}(v,1-v),\qquad
Q_b^TQ_f=Y/2.
\]

These identities verify the first-layer coupling and both learned tensor
updates, including all factors of two. Forward-from-backward and
backward-from-forward response blocks have the stated different
intertwiners. In the typed bases their deterministic coefficients are
sector diagonal. Individual random gate matrices remain full matrices.
For opposite labels, replacing these intertwiners by ordinary commutation
in one common basis would be wrong; the candidate does not do that.

No estimate used in the final closure divides by the inactive sample
variance. In particular, when $v\to1$, the intrinsic $M$ can stay
bounded while $1-v\to0$; the prohibited inference
$e/\sqrt\delta\lesssim eM^4$ is explicitly replaced. Singular temporal
source covariances are handled by formal named slots and independent
query regularization, not inverses of limiting Gram matrices.

## 4. Affine reference, perturbation, and the coefficient

The affine balance identities and radial estimate imply continuation to
the actual first hit $g=3/2$, with normalized duration below two,
original duration $S\le M^4$, and

\[
M=\left(\frac3{\sqrt2\lambda}\right)^{1/4},\qquad
\lambda=a^3\sqrt v,\qquad
M\le24^{1/4}\delta^{-1/8}.
\]

The enlarged beta family uses only the proved $O(M^{-2})$ extra
continuation interval. It is not extended to a fixed beta interval
independent of $M$.

The linearly growing shape estimates are sufficient. In particular the
four same-state update discrepancies sum to

\[
\left(\frac{61}{16}+\frac{43}{8}+\frac{53}{8}
+\frac{61}{8}\right)eb^3=\frac{375}{16}eb^3<40eb^3.
\]

Only the affine vector field is differentiated in the comparison. The
normalized active first root is controlled by the raw first-layer
distance with constant one, so retaining $\lambda$ in the affine
prediction difference is justified. The extra growth terms fit within
the displayed $C_z=1500C_0$ and $C_g=14400C_0$, without changing
their exponents.

The direct raw Gram argument is valid: the largest learned discrepancy
is bounded by $32(b^3E+eb^4)h_j$, giving $KeM^{15}h_j$, and a
backward row sum adds at most $M^4$. The bound includes both typed
sample sectors and the learned backward memories.

The affine propagator proof retains all four gradient terms and obtains
the weighted exponent three. Its independent-root probe argument measures
the actual frozen formal source coefficients, with width taken before
the probe amplitude is removed. The affine source certificate includes
the top reverse resolvent and the strict top transfer; neither is replaced
by a product of crude row bounds.

The nonlinear value equations acquire only the additional affine-growth
self terms displayed in `LINEAR_GROWTH.md`. Their powers are $13,11,8$
at the three populations. The condition $eK^{22}M^{19}\le1$ absorbs
them and controls the exponential derivative envelope. The subsequent
Cauchy--Schwarz estimate uses actual primal $L^2$ sizes $M^3,M^2,M$;
it does not assert that a bounded Gaussian action preserves arbitrary
$L^p$ norms.

The same-array derivative identities retain one explicit curvature
multiplier, the current returns, and every source-time contribution.
Consequently $q_{\rm def}\le K^{30}eM^{19}$ has the stated meaning:
strict density for forward defects and complete causal row norm for
backward defects. The supersolution allows arbitrary backward current
diagonals and concentration on arbitrarily short source steps. Its valid
strict/row/strict sandwich inequality supplies the remaining $M^{12}$.

The final arithmetic is correct:

\[
e\le\tfrac12 24^{-31/4}K^{-46}\delta^{31/8}
\quad\Longrightarrow\quad
eM^{31}\le\tfrac12K^{-46},
\]
\[
eK^{22}M^{19}<1,\qquad
q_{\rm def}\le\tfrac12K^{-16}M^{-12}.
\]

The other entries of $c_{\rm dyn}$ close the primal tube and endpoint
margin. No additional shape nonaffinity or physical-horizon restriction
is needed for Theorem A. Replacing the inherited envelope $H$ by
$K=H^2$ consistently weakens its numerical inequalities.

## 5. Population construction and full observable scope

At a fixed cap, the required coordinate maps are globally Lipschitz
$C^1$ with bounded first derivatives. For the present class,
$|\phi(z)|\le(5/4)|z|+1/4$, $|\phi'|\le5/4$, and the cap derivatives
have the required bounds. $C^2$ regularity of the shape supplies
continuous first derivatives of the cap gate; no third derivative is
used.

The fixed-program conditioning proof retains both orientations of each
Gaussian matrix. Its query-noise argument treats rank drops without a
pseudoinverse limit. Countably generated probes, the finite Gaussian
operator bound, and finite adjunction give bounded population actions
and actual adjoints. Learned increments are Hilbert--Schmidt rank-one
integrals. This establishes the intended infinite-dimensional state.

The cap comparison is asymmetric, with amplification at most
$\exp(CR)$, and uses tails only of its reference. The proved Gaussian
tails therefore yield strong cap removal and uniqueness against
nonsymmetric bounded-primal strong competitors, including reached-state
restart. The uncut gradient structure follows from the strong trajectory
chain rule and adjunction; it does not require a false global Fréchet
differentiability assertion for the feature Nemytskii map on $L^2$.

The first-fitting clock diverges because the feature path has bounded
derivative up to its first hit of one. The physical flow consequently
exists for every finite time. The initialized odd/even decomposition gives
$\kappa(0)\ge\delta/8192$, radial coercivity gives
$g_s'\ge\kappa(0)$, and

\[
\dot{\mathcal L}=-4g_s'\mathcal L
\le-\frac{\delta}{2048}\mathcal L.
\]

The algorithm bridge uses width at fixed cap and auxiliary mesh,
deterministic Euler error to remove that mesh, and then cap removal.
Raw GD contributes $C_{R,T}n^{-2}$ through comparison with the same-width
cap reference. No theorem for a transcript growing with width is used.

The velocity proof appends the two actual reused forward-action queries,
first truncates their product inputs, and removes those truncations using
the proved $L^2$ laws and source derivatives. For uncut velocities, cap
removal precedes removal of a fixed reference-velocity truncation. The
compact $L^2$ time image of the uncut velocity supplies uniform tails.
This supports the full joint same-layer velocity and second-moment claims.
The integrated-speed interpolation estimate then supplies
$\mathcal W_2(C([0,T];\mathbb R^4))$ for the two-sample
preactivation/feature paths. All four true raw kernel blocks follow from
their same-layer $L^2$ contractions. No cross-layer neuron pairing or
cross-width operator-norm convergence is being inferred.

## 6. Nonaffinity and initial motion

The new affine marginal upper bounds check algebraically:
$6,636,66780<260^2$. Together with the old lower bound they put every
actual affine marginal standard deviation in
$[1/\sqrt{404},260]$, independently of separation.

For every continuous globally nonaffine shape, positive Gaussian density
makes each regression residual positive. Linear growth supplies dominated
convergence in the Gaussian regression formula on this compact interval,
so $\eta_\psi>0$. The optimal regression slope of a one-Lipschitz
shape has absolute value at most one, including the appropriate
zero-variance convention. Testing the residual maps across a coupling
proves the factor-two Lipschitz bound for square-root regression error.
The specified $c_{\rm NL}(\psi)$ therefore leaves the stated
$e^2\eta_\psi/4$ margin. This bound is absolute, not a moderate relative
nonlinearity claim.

Initial motion requires no quantitative lower bound on $\eta_\psi$.
Since $\phi'\ge1/4$ and $\phi''\not\equiv0$, the top beta Gram is
strictly positive definite. The inherited initialized transpose formula
uses its full second-moment covariance, not a regression remainder.
Conditional variance then makes the middle and bottom beta Grams
positive. The block adjunction identities and input/readout-sign symmetry
give nonzero acceleration for each sample and each hidden layer. Bounded
positive $\phi'$ transfers this to features. The projected kernel's
quadratic expansion has positive coefficient.

The affine-shape adversarial test is passed: $\psi(z)=z$, a constant,
or any other admissible affine shape is included in Theorem A and is
excluded from Theorem B and from the asserted nonaffine initial-motion
certificate. Thus $\eta_\psi=0$ in this case causes no contradiction.
The theorem also does not assert perpetual hidden velocity or trained
Gaussianity.

## 7. Supporting lemmas and overclaim checks

`AFFINE_POSITIVITY.md`: the covariance lower bound is entrywise, so it
works for singular or perfectly correlated source groups. Independence
of the distinct named Gaussian groups makes their variance contributions
add. Positivity then bounds the actual response rows. The identity
$FB_2=R_1-I$ justifies the special $FL$ estimate and avoids an invalid
right-row-multiplier density estimate. The normalized table and its
original-time powers are correct. The proposed improved nonlinear
closure is expressly provisional and is not used in Theorems A or B.

`BOUNDED_ACTIVATION_ROUTE.md`: the readout, top learned-kernel, and learned
reverse-memory estimates follow from their displayed rank-one integrals.
The energy bound is restricted to actual gradient flow. The selected
Gaussian column/sign example has a coordinate of order $\sqrt n$,
giving its nonvanishing empirical second-moment tail; exchangeability
does not remove this obstruction. It is correctly identified as an
obstruction to an overgeneral tail lemma, not a neural-flow counterexample.
The two-control Lie bracket gives the claimed obstruction to a global
coordinate straightening when $\rho\ne0$ and $\phi$ is nonaffine.

`RELATIVE_NONLINEARITY.md`: the independent-copy variance identities
prove $\mathcal N_\phi(Z)\le(e/(a-e))^2$ for the normalized class.
The sine residual is orthogonal to both constants and the standard
Gaussian coordinate, so its normalized nonlinear fraction is exactly
$b^2v/(1+b^2v)$. This exposes, rather than conceals, the very small
relative nonlinearity certified by the perturbative theorem.

`SINE_INITIALIZATION.md`: the Gaussian trigonometric identity gives
$R(c)=e^{-\omega^2}[\sinh(\omega^2c)-\omega^2c]$. Its positive
power series proves $|F(c)|<|c|$ for $0<|c|<1$, and unit variance
propagates through all three initial hidden layers. The top kernel and
its separation lower bound therefore have the stated normalization.
At $\omega=2,b=2/5$, the approximately 6.4 percent fraction is an
initialization calculation only; no trained-flow persistence is claimed.

I also checked the narrow literature-boundary statements directly against
the linked primary sources. Tensor Programs IV's Appendix A distinguishes
the discrete-width limit from the additional continuous-time
well-posedness problem and distinguishes its Gaussian middle matrices
from the discussed multilayer mean-field initializations.
[Yang and Hu, supplement, Appendix A](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf).
The cited Chen et al. Corollary 4.6 explicitly assumes parameters stop
changing after a finite discrete time; the candidate does not replace
that assumption by arbitrary asymptotic convergence.
[Chen et al., v2, Corollary 4.6](https://arxiv.org/html/2503.09565v2).

The final theorem states convergence for every fixed shape, dataset and
finite physical horizon, with one shape-uniform dynamics coefficient.
It does not assert a probability supremum over the class, a uniform limit
on the infinite time half-line, or a practical moderate-amplitude theorem.
Those boundaries are mathematically necessary and are respected.
