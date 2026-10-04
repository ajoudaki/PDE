# Independent internal audit of the smooth population-width theorem

2026-10-01. **Verdict: PASS for SMOOTH_RESULT (1)--(2), at the exact versions
recorded below.** The supplied arguments, read together with the specifically
authorized foundational passages, establish the conditional all-time
mean-square bound and hence the unconditional fixed-confidence
\(O_{\mathbb P}(n^{-1/2})\) error to the smooth system's own population
predictor. The finite-width mean bias is included. I found no remaining
statistical or population-identification hypothesis in that chain.

This is an internal theorem audit, not promotion review. It does not establish
the stronger all-initialization all-time second moment, a matching lower
bound, arbitrary-depth or arbitrary-activation extensions, or a comparison
with a dense or unclipped network.

## Scope and method

The audited system is precisely SMOOTH_SETUP: two tanh hidden layers, q=1
memories, a fixed independent Gaussian mixer and its actual transpose,
Gaussian first-layer rows, zero readout and values, matching initial keys,
clock one, and both post-gate backward signals clipped by
\(c_M(s)=M\tanh(s/M)\). The cap \(M>0\) and sufficiently small nonzero label
vector are fixed as width increases. The initial population readout-feature
Gram has a positive gap. Query laws have bounded support.

Write \(\mathcal G_n\) for the initialized fitting event, \(E_n\) for
conditional expectation on that event, and
\(m_n(t,x)=E_n f_{n,M}(t,x)\). The conclusion checked is

\[
E_n\int\sup_{t\ge0}|f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)
\le C/n,
\qquad \Pr(\mathcal G_n^c)\le Ce^{-cn}.
\]

All ten assigned scientific files were read completely. No prior review
file, other study, Git history, archive, or unassigned scientific source was
read. The required canonical-notation, rigorous-proof and research skills
and their relevant references were used. On encountering the qualitative
population construction's external dependency, I requested its complete
proof rather than assuming it. The supervisor authorized only the two
foundation passages listed in the hash record; both were read completely.
No experiment, source edit, manuscript edit, or Git operation was performed.

## 1. Fitting and centered concentration have the correct scope

The fitting calculation uses cap contraction, not an identity interval for
the cap. Its exact prediction derivative retains
\(p_a=w\operatorname{sech}^2z_a\), whereas the trained upper signal is
\(d_a=c_M(p_a)\). Readout-Gram coercivity absorbs the hidden-motion term
of size \(Cs(t)^2\rho(t)\), where \(s(t)=\int_0^t\rho\). Small fixed labels
therefore give \(\rho(t)\le Ye^{-\lambda t}\) and finite total activity on
\(\mathcal G_n\). The smooth derivative distinction is maintained in all
subsequent residual and velocity calculations.

The initialized exponential tail is consistent with, and stronger than,
the older concentration note's polynomial tail. It requires no trained
coordinate independence: bounded iid first-layer covariance entries have
exponential tails; conditional on them, initial second-layer rows are
independent Gaussians; the tanh covariance map is Lipschitz by its bounded
Hessian and Gaussian interpolation, including singular covariance
matrices. A finite union bound and the fixed matrix-net tail give the stated
event. These arguments concern initialization only.

The centered all-time bound is not inferred from pointwise concentration.
On the fitting event the prediction velocity has Gaussian-root Lipschitz
constant \(Ca(t)/\sqrt n\), with integrable
\(a(t)=(1+t)e^{-ct}\). A bounded Lipschitz extension, Gaussian Poincare,
and Minkowski applied to the integral of the centered velocity prove

\[
E_n\int\sup_t|f_{n,M}(t,x)-m_n(t,x)|^2\,d\mu(x)\le C/n.
\]

That estimate alone does not control population bias; the subsequent
steps supply a separate bias argument.

## 2. The actual mean histories are admissible

Freezing \((r,\rho,\tau,K,V)\) at their conditional means is justified
by scalar Gaussian-root concentration and the state difference inequality
with integrable coefficient \(C\bar\rho\). It does not differentiate the
residual norm. The resulting conditional normalized state RMS error is
\(C/\sqrt n\), uniformly in time.

The cubic bound on \(\bar V\) requires the additional argument in
SMOOTH_FEEDBACK_COMPLETION. On the fitting event,
\(\|\dot r_n\|_m\le C\rho_n\) implies
\(Ye^{-Ct}\le\rho_n(t)\). Consequently

\[
s_n(t)\le Y\min(t,\lambda^{-1}),\qquad
\bar s(t)\ge (Y/C)(1-e^{-Ct}),\qquad s_n(t)\le C_1\bar s(t).
\]

Thus \(|\bar V(t)|\le C\bar s(t)^3\). This is a valid replacement for
the incorrect Jensen inference that would otherwise be tempting.
The contraction derivatives give
\(|\dot{\bar K}|+|\dot{\bar V}|\le C\bar\rho\), so the supplied
coefficients are Lipschitz in activity. Moreover the frozen total activity
lies between positive constant multiples of the fixed \(Y\). The factors
\(S^{-1},S^{-2}\) in the mean-map norm therefore do not introduce a
width dependence. No claim uniform as \(Y\downarrow0\) is needed.

## 3. The cavity estimates include the required response identification

With the scalar histories fixed, deletion makes the removed Gaussian row
or column independent of the retained environment. The local Taylor
estimate is in ordinary Euclidean norm. A pure tangent coordinate has
conditional \(L^p\) size \(C_p/\sqrt n\); its quadratic defect has size
\(C_p/n\); summing squared defects over the order-n coordinates gives an
ordinary Euclidean remainder of size \(C_p/\sqrt n\). Bounded local
derivatives and the integrable drift propagate this scale. The proof does
not use a false normalized-L2 Hessian bound.

The tagged calculation is needed, and it is supplied. It differentiates
the forced equations before estimating the error. Its source products have
the forms \(t_\eta t_\chi\) and \(e_\eta t_\chi\); coordinate moments
control the first and ordinary Euclidean Holder bounds control the second.
Gaussian quadratic-form centering then gives the trace response.
Exchangeability identifies the expected normalized trace with the expected
tagged diagonal response. This is an identification of the response of the
scalar equation, not differentiation of a state convergence assertion.

The source-time refinement is also essential. For an upper perturbation
at physical time s, the tagged d variation consists of its direct atom and
a bounded causal state-response tail. Inserting the atom into the
variational equation contributes a jump proportional to \(r_b(s)\);
the same projection and product estimates at that source yield
\(C|r_b(s)|/\sqrt n\) for the regular response error. Equivalently one
uses pulses of unit source mass in the linearized equation. One must take
the first variation before the pulse limit; a nonlinear equation driven
by a Dirac mass is not being asserted. The lower tagged state response has
the analogous jump and no direct h atom. These are precisely the source
estimates needed for the response-density norm, including zero residual
components without division by them.

The upper direct atom is
\(E[F_z(z_a,w)]\delta_t\). The passive q field has its distinct direct
carrier atom as well. Both are retained. The two source matrices and
ordinary output factor in the candidate have the correct roles.

## 4. Cutoff cavity laws and deterministic means belong to one domain

The domain issue can be checked from the finite forced equations, without
assuming neuron independence. On a fixed operator cutoff:

- bounded clipped lower velocities make every lower h path Lipschitz in
  activity, so its empirical covariance has the required increment bound;
- bounded normalized forward velocities make d Lipschitz in normalized
  Euclidean norm, giving the upper empirical covariance increment bound;
- \(|w(x)|\le Cx\) gives \(C_d(x,x)\le Cx^2\) and the zero initial atom;
- source, output, and propagator operator bounds give bounded normalized
  response densities;
- normalized Hilbert--Schmidt differences of these factors give Lipschitz
  target-time rows in L1. The moving causal source strip contributes at
  most its length times the density bound. The upper atom's averaged
  increment is controlled separately by the normalized w,z increments.

These estimates have fixed constants. They permit the domain constants
to be chosen to include both full and deleted finite tuples, followed by
the small-activity choice. They also apply to finitely many passive queries.
There is no requirement that an empirical initial lower covariance equal
the deterministic \(C_0\): the domain deliberately leaves it free, while
the lower output resets it to \(C_0\).

For a literal common-dimensional lower-column comparison, the removed
coordinate may be retained as a detached coordinate with the same initial
first-layer row. Its clipped activity speed is bounded and its effect on
the remaining environment is zero because K,V are prescribed. This avoids
an artificial unbounded initial-row difference from padding the first
layer by zero. Equivalently compare only retained state coordinates and
bound the omitted bounded outputs separately. Its normalized trace
contribution is at most \(C/n\). The retained environment and its upper
law data remain independent of the removed initial row.

Outside a cavity-measurable operator cutoff, replace the entire law tuple
by one admissible tuple. Convexity preserves positive semidefiniteness and
all increment/response bounds upon averaging. The moments
\((1+\|W_0\|)^b\exp(CS(1+\|W_0\|^2))\), together with Gaussian
operator tails, make the replacement error exponentially small. The
removed Gaussian vector itself is not conditioned on the fitting event.
Its separate norm exceptional set is handled by moments. Full versus
deleted tuples and their localized versions retain their root-width
entrywise errors.

## 5. The random-law comparison does produce an approximate fixed point

The strengthened Section 11 of SMOOTH_MEAN_MAP_ROUTE resolves the relevant
norm mismatch. Its derivative tensors are deterministic entrywise
majorants constructed by positive causal recurrences. For a mesh
functional f and an environment-measurable covariance error,

\[
\left|E[f(X_1)\mid\mathcal E]-E[f(X_0)\mid\mathcal E]\right|
\le\frac12\sum_{ij}b_f[ij]|\Delta C_{ij}|.
\]

The deterministic coefficients permit expectation before summation. Their
uniform total mass bounds use \(\sup_{ij}E|\Delta C_{ij}|\); they do not
require or assert \(E\sup_{ij}|\Delta C_{ij}|\). The parameter-insertion
tensors provide the corresponding fact for response inputs. Repeated
source slots retain diagonal masses, and one distinguished fixed response
slot retains its source-cell factor. Hence the assertion covers both
response rows and individual regular densities, not only a bounded test
direction.

The mesh construction allows singular Gaussian covariances. Adding
\(\varepsilon I\) is used only to prove the interpolation identity and
then removed by bounded derivatives; no inverse-Gram estimate enters.
Covariance increment bounds give continuous Gaussian versions. The
explicit response equations and the L1 compactness of target-time rows
justify the mesh limit for responses separately from state convergence.

To spell out the combination, let \(\Lambda_n\) be the deterministic
mean of a localized full finite covariance/response tuple, let
\(\Lambda_n^c\) be its random cavity counterpart, and let \(\mathcal M\)
be the prescribed-history map. Cavity reinsertion and tagged derivatives
give, componentwise with fixed target/source indices,

\[
\Lambda_n-E\mathcal M(\Lambda_n^c)=O(n^{-1/2}).
\]

The entrywise moment estimates and deterministic majorants give
\(E\mathcal M(\Lambda_n^c)-\mathcal M(\Lambda_n)=O(n^{-1/2})\)
in the same normalized covariance/response metric. Source errors are
integrated before the deterministic target supremum. Thus
\(\|\Lambda_n-\mathcal M(\Lambda_n)\|\le C/\sqrt n\).
The small-activity weighted contraction places \(\Lambda_n\) within
\(C/\sqrt n\) of its unique fixed point. This is the missing statistical
source/bias mechanism that centered concentration alone would not supply.

## 6. The fixed point is the own common-action population

The additional authorized foundation passages suffice for qualitative
identification; they are not being used for a mesh-uniform rate. A fixed
Euler program for the prescribed smooth q=1 flow uses independent Gaussian
roots, the same Gaussian matrix in both orientations, deterministic
coefficients, and globally bounded-derivative coordinate instructions.
The complete gate F has those derivatives. The readout, values and keys
are bounded by direct integration, so any needed intermediate bounded
products can be extended outside their fixed ranges. The fixed-program
lemma therefore applies, including singular source laws.

Passing its finite matrix bound and transpose identity through the joint
countable program family constructs a bounded action and its actual
adjoint. On the reachable bounded state set the forced equations are
Lipschitz in the population L2 state norm. Fixed-mesh convergence followed
by mesh refinement consequently identifies their finite-width compact-time
limit with that common-action ODE. The quantitative approximate-fixed-point
argument gives the same finite-width observable limits. Uniqueness of limits
identifies the response-law fixed point with this forced population.

Jointly including the required prescribed histories and autonomous Euler
programs in the countable family puts them on the same population spaces
for the final deterministic comparison. This does not define the
population as a finite-width mean. It also does not import a dense-training
population or independent forward/backward actions.

## 7. Velocity consistency closes scalar feedback and all physical time

The passive observable \(q_a=\dot h_a/\rho\) is a bounded smooth lower
output with bounded prescribed ratios \(r_b/\rho\). Those ratios are not
differentiated. Its joint Gaussian carrier uses the full positive
semidefinite covariance block for h and q and retains its direct response
atom. The only unbounded upper velocity term is
\(w\operatorname{sech}^2z_a\,G^q_a\); its derivative envelopes are
linear in \(|G^q_a|\), with uniformly bounded conditional Gaussian
moments. The same comparison therefore yields

\[
|E\dot f_n^\theta(t,x)-\dot f_\infty^\theta(t,x)|
\le C\rho(t)/\sqrt n.
\]

The K velocity uses the bounded observables
\((h_b-k_b)h_a\) and \(k_bq_a\), so it has the same integrable
consistency estimate. Actual-versus-forced velocity comparison is performed
before dividing by rho, using raw residual, state, K and K-velocity
differences. Conditional-to-full forced expectations are controlled by
bounded outputs or the polynomial operator bound on the velocity.
These statements supply all of SMOOTH_FEEDBACK_COMPLETION (5)--(7).

The deterministic restoration retains the algebraic K,V errors and the
clock argument of Q. Reconstructing actual population moments from the
forced state gives an \(O(\bar\rho/\sqrt n)\) state-velocity defect; the
prediction-velocity defect also contains the already integrated K-velocity
error. With D the state/clock discrepancy and R the residual discrepancy,
the resulting inequalities are

\[
D(t)\le Cn^{-1/2}+C\int_0^t(\bar\rho D+R),\qquad
D^+R\le-\kappa R+C\rho_\infty D+e(t),\qquad
\int_0^\infty e\le Cn^{-1/2}.
\]

Integrating the damped residual inequality first and substituting into
the state inequality proves \(\sup D+\int R\le C/\sqrt n\).
Only total residual activity appears in Gronwall. This step neither
differentiates an approximation bound nor uses a nonsmooth residual-norm
Hessian. It proves the deterministic conditional-mean bias estimate,
including the fitted endpoint.

## 8. Query norm and exact conclusion

A passive query adds a fixed number of lower projections and forward
observables. The estimates involve it only through bounded input norms
and their inner products with the fixed training data. They impose no
query Gram gap. Thus one common constant works over a fixed bounded query
set. The deterministic bias bound is uniform in time with that constant,
and centered concentration places the time supremum inside expectation
by velocity integration. Tonelli then places it inside the query integral
exactly as required. No spatial supremum or continuum-query entropy claim
is being made.

Combining the centered bound with the independently established bias gives
the conditional mean-square conclusion. For every fixed \(\delta>0\),
conditional Markov and the initialized tail give

\[
\Pr\left\{\left(\int\sup_{t\ge0}
 |f_{n,M}-f_{\infty,M}|^2\,d\mu\right)^{1/2}
 >\sqrt{C/\delta}\,n^{-1/2}\right\}
\le\delta+Ce^{-cn}.
\]

This does not need a moment on \(\mathcal G_n^c\). Conversely the
exponential probability of that event does not prove the all-initialization
all-time second moment. SMOOTH_ALLINIT_ROUTE correctly leaves that stronger
statement open. No fixed-label \(Y^3\) or smooth-top-discrepancy remainder
is substituted for the finite-width mean bias in the positive conclusion.

## Exact checked versions

Hashes are SHA-256 of the complete file bytes. The two passage hashes use
the original inclusive line ranges, retaining their original line endings.
The foundational full-file hashes identify provenance; only the authorized
passages were read.

| Assigned file | SHA-256 |
|---|---|
| SMOOTH_SETUP.md | a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6 |
| SMOOTH_RESULT.md | d9f1843268617b6989f8985ea19e8bb17152c15798ca6b726f572eec940eadbd |
| SMOOTH_CAVITY_ROUTE.md | 9e22c3f455a6c0447a654a9af6154c0a6c38247bacf2f5aaf40a408895982315 |
| SMOOTH_MEAN_MAP_ROUTE.md | 9ca3c42741683d9ba37c5dac9a2df6018e606326756b671b89023fbeaba3b95e |
| SMOOTH_FEEDBACK_COMPLETION.md | eb3454d7c13c94ce4a89da8491bca0ff65e207c4d4275a2122ae588cd381d7e2 |
| SMOOTH_RESTORATION.md | 71e68a479072501e9fabee0b7f77256858584a9606ddbd993bb145d46470fc43 |
| SMOOTH_ALLINIT_ROUTE.md | db8b43883fb81c4e1afc3cb9961620bfda5b5ed0933f55ec57e422085b16ee8a |
| CONCENTRATION_ROUTE.md | 4331e895f388b238ced358cfa101390b80681c3797fa36b5b8ba7e319312d8f5 |
| CLIPPED_POPULATION_ROUTE.md | 63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082 |
| FITTING_AND_THRESHOLD.md | edb64134a5a4b5ce620586d0da0d3276ca542b1069b0a48801fa3f5d4cd4d1c2 |

| Specifically authorized foundation | Full-file SHA-256 | Read-passage SHA-256 |
|---|---|---|
| paper/proof_alltime.tex, lines 340--507 | f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d | 5ac48c2bd8eb035b194568608e4143752a546737e73a17ddf4fb4d9198b96047 |
| docs/03-local-population.qmd, lines 3242--3877 | 3a6fc52191f815189337309f70e3fb822663b1532eedc54e4dea9402c3fdaebd | 453b7a383672c0323a20403919220b70cad169a6de1aec1927d8ad254e026dd8 |

The audit does not rely on the prior-verdict references embedded in the
assigned artifacts. Later status-only edits do not change the mathematical
assessment, but are different byte versions from those recorded here.
