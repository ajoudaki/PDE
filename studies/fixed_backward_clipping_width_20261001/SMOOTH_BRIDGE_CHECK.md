# Internal check of the smooth cavity–mean-map bridge

2026-10-01. Scoped internal mathematical check, not a promotion review.

**Verdict.** The revised deterministic envelopes close the specific
pointwise-fluctuation-to-mean-consistency gap. Together with the paired
deletions and the forced-system cutoff argument, they give a compatible
root-width comparison for the prescribed-history law and its mean velocity.
The response atoms and the distinction between the trained clipped signal
and the actual output derivative are correctly retained. This verdict does
not certify the original all-initialization all-time second-moment theorem.
That theorem still requires the original dynamics' exceptional-event bound;
the forced-system cutoff calculation does not supply it.

## Inputs and claim boundary

I read the complete following files, and no other scientific inputs:

| File | SHA-256 |
|---|---|
| `SMOOTH_SETUP.md` | `a9a2166984c946a5cceebd6f01c168b052e1b74da2b52a2df92c111aa830eee6` |
| `SMOOTH_CAVITY_ROUTE.md` | `9e22c3f455a6c0447a654a9af6154c0a6c38247bacf2f5aaf40a408895982315` |
| `SMOOTH_MEAN_MAP_ROUTE.md` | `9ca3c42741683d9ba37c5dac9a2df6018e606326756b671b89023fbeaba3b95e` |
| `SMOOTH_RESTORATION.md` | `71e68a479072501e9fabee0b7f77256858584a9606ddbd993bb145d46470fc43` |
| `CLIPPED_POPULATION_ROUTE.md` | `63bdd715efc7d05875acd4b591d8d2751f38a4f15246f78b7ebfab44c36b5082` |
| `SMOOTH_FEEDBACK_COMPLETION.md` (additionally authorized) | `02b286e70f292f7815ae20dee5017dc5583ba5127ebd71eb95ef03444424ffef` |

The canonical-notation skill and neural-response reference, rigorous-math
skill, conjecture-audit skill, and adversarial-audit reference were applied.
No experiment, Git write, prior review, other study, or manuscript was read.
The common-action construction in the assigned population route is an input
result; its referenced foundational Gaussian-program proof was outside this
check's source scope and was not independently re-reviewed.

Write \(\psi(z)=\operatorname{sech}^2z\) and
\(F(z,w)=M\tanh(w\psi(z)/M)\). Throughout this check the deterministic
histories \(\theta=(r,\rho,\tau,K,V)\) are prescribed, with
\(\tau=1+\int_0^t\rho\), and their accumulated activity is
\(x=\int_0^t\rho\), of total length \(S\). All response derivatives hold
these supplied histories fixed. This qualification is essential.

## Paired deletion, source impulses, and output velocity

The two deletions use the correct independent variables. After upper-row
deletion, the environment is independent of the removed row and of the
tagged external preactivation at that row. After lower-column deletion,
the environment is independent of both the removed column and the omitted
first-layer Gaussian root. Prescribing \(K,V\) is what removes their
otherwise direct dependence on the omitted coordinate.

The state and derivative estimates in cavity Sections 5, 8, and 9 are
compatible. The first tangent has conditional coordinate moments
\(O(n^{-1/2})\); therefore its coordinatewise quadratic defects have
ordinary Euclidean norm \(O_{L^p}(n^{-1/2})\). The mixed tagged defect uses
the product of two such pure tangents, plus an ordinary-norm remainder
times an ordinary-norm tangent. This uses no false normalized-\(L^2\)
Hessian bound. Operator-bounded propagation and finite activity preserve
these estimates.

A fixed source-time derivative must be understood as the first variation
with a source atom, followed by its causal response tail. There is only
one tagged derivative, so its source atom is multiplied by bounded base
coefficients, not by another distribution. The Taylor-defect calculation
then retains the source mass \(|r_b(s)|\); it does not obtain a response
density by dividing a state-error estimate by a vanishing residual.
Under the activity change of variables this factor becomes
\(|r_b(s)|/\rho(s)\le\sqrt m\) almost everywhere with respect to
\(\rho(s)ds\). Zero-activity times add no integral contribution.

The present-time upper response is exactly

\[
 \delta_{ab}F_z(z_a(t),w(t))\,\delta_t,
 \qquad
 F_z(z,w)=-2w\psi(z)\tanh z\,
                 \operatorname{sech}^2(w\psi(z)/M).
\]

It vanishes at initialization because \(w(0)=0\), but not subsequently.
The passive lower velocity \(q_a=\dot h_a/\rho\) has the distinct current
carrier derivative in cavity (35). That atom can be nonzero even when
the actual initial \(q\) is zero. Mean-map ambient derivatives at a
zero-variance Gaussian coordinate correctly retain this possibility.
Neither atom is counted again in its regular past density.

The full state source in cavity (31) is also correct: perturbing \(z_b\)
changes \(w\), \(v_b\), and the lower equation through
\(W_0^\top\operatorname{diag}F_z\). All three paths have the indicated
factor \(r_b\). Exchangeability then identifies the expected normalized
trace with the expected tagged diagonal derivative. It is the tagged
derivative calculation, rather than convergence of state values, that
identifies this derivative with the scalar system's response.

The passive field uses the same initialized matrix. Its direct carrier
response, regular past response, and the full joint covariance of
\((G^h,G^q)\) in cavity (36)–(38) are necessary and are present. Direct
differentiation of the supplied-coefficient forward equation gives (39),
whose upper output factor is \(p_a=w\psi(z_a)\), not \(d_a=F(z_a,w)\).
The linearly growing Gaussian observable \(p_aG^q_a\) is controlled by
conditional Gaussian moments. Its covariance interpolation must use the
joint positive-semidefinite covariance block; the text does so.

## Deterministic envelopes and continuum contraction

Mean-map Section 11 supplies more than a bound on a realized tensor sum.
Its positive partition recursion constructs one deterministic tensor
dominating every individual history derivative, uniformly over the
realized Gaussian histories, the first-layer root, and the admissible
response inputs. Summing this already deterministic tensor gives the
required \(O(S)\) or \(O(S^2)\) masses. Repeated source indices preserve
their single Euler-cell weight, so diagonal source-time measures are
not mistakenly replaced by products of Lebesgue densities.

The refinement for the upper gate is valid. Every pure \(z\) derivative
of \(F(z,w)\) vanishes at \(w=0\), and its additional \(w\) derivative
is uniformly bounded on \(|w|\le cS\). Hence those coefficients are
\(O(S)\). Terms containing a history derivative of \(w\) acquire the
same factor from that derivative. A generic bounded-derivative estimate
without this distinction would not establish the asserted upper scaling.

For a covariance error \(\delta C_{ij}\), conditional interpolation thus
has a deterministic bound

\[
 |\Delta\mathbb E f|
 \le\frac12\sum_{ij} b_f[ij]|\delta C_{ij}|,
 \qquad
 \|\Delta\mathbb E f\|_{L^p}
 \le\frac12\sum_{ij}b_f[ij]\|\delta C_{ij}\|_{L^p}.
\]

The response-input insertion tensors (42)–(46) provide the corresponding
statement for \(D,Q_d,Q_h\). This second step is indispensable: applying
only the deterministic row-norm Lipschitz estimate to a random kernel
would reintroduce an expected supremum over current time. The revision
retains direct current-row insertions and propagates earlier insertions
with deterministic weights before taking expectations. Fixed-source
estimates keep the past response cell factor and separate the atom.
Therefore pointwise \(L^2\) covariance and response fluctuations really
can be integrated here without an \(\mathbb E\sup\) loss.

The finite-dimensional covariance interpolation does not require an
inverse covariance. Adding \(\varepsilon I\), integrating by parts,
and then removing \(\varepsilon\) is justified by the bounded derivatives,
or by the stated Gaussian moment envelope for the passive output.
The Gaussian increment bounds yield continuous core histories. The
causal response equations (22)–(23) give the mesh limit of response rows
in uniform \(L^1\); source-cell averaging is uniform because the current
rows form a compact subset of \(L^1\). These arguments handle singular
covariances and measurable residual controls.

The two normalized Lipschitz estimates in (26) consequently give a
contraction after squaring the bipartite map. The domain is complete and
convex, and its constants can be chosen before decreasing \(S\).
The revised initial-covariance domain is necessary: a random empirical
\(C_h(0,0)\) need not equal its population value. The enlarged input
domain permits it, while the lower output sets the fixed point's initial
covariance to the correct population value.

## Domain checks and the combined approximate fixed point

Here is the compatibility argument needed to use the preceding two
routes together, rather than treating them as unrelated conditional lemmas.

On a fixed operator cutoff, empirical cavity covariance kernels are
positive semidefinite. The bounds \(|h|\le1\), \(|d(x)|\le cx\), and
normalized activity-velocity bounds give their required covariance
increment inequalities. The lower feature response density has bounded
operator norm and bounded current-time derivative. For upper responses,
differentiate the output derivative factors in normalized
Hilbert–Schmidt norm: \(\|z'\|_n\le C\), bounded gate derivatives,
and \(\|\Phi\|_{\rm op}+\|\Phi'\|_{\rm op}\le C\) give the
same bound for the normalized trace. Integrating the moving source strip
gives the zero-extended row's \(L^1\)-Lipschitz bound. The current atom's
scalar trace is Lipschitz by the same normalized Cauchy–Schwarz calculation.
Source factors \(r_b/\rho\) are bounded and need no source-time derivative.
Thus the cavity tuples lie in the enlarged map domain after choosing its
fixed constants to include this cutoff family.

Outside the cutoff, replace the entire tuple by one fixed admissible
tuple. This preserves positive semidefiniteness and the deterministic
domain bounds. Take the deterministic mean of the analogously localized
full tuple, denoted \(\Xi_n\); convexity keeps \(\Xi_n\) in the domain.
The choice of this localized mean avoids assuming that an unbounded
random trace lies in a fixed contraction domain.

For each fixed output/source time, normalized-trace concentration and
full-versus-deleted comparison give \(O(n^{-1/2})\) differences between
a cavity tuple and \(\Xi_n\). The deterministic envelopes just checked
replace the random cavity tuple by \(\Xi_n\) inside each scalar
expectation, including a fixed or integrated response source. Paired
tagged reinsertion identifies the other side with the corresponding
finite-width output expectation. The exponentially small localization
errors are absorbed. If \(\mathcal T_\theta\) is the prescribed-history
map, the result is

\[
 d(\Xi_n,\mathcal T_\theta\Xi_n)\le Cn^{-1/2}.
\]

Here \(d\) is the weighted contraction metric derived from mean-map (5),
with fixed positive small \(S\). Its contraction constant is less than
one, so its fixed point \(\Xi^\theta\) satisfies
\(d(\Xi_n,\Xi^\theta)\le Cn^{-1/2}\). The same interpolation and
reinsertion calculation applies to \(\mathbb E[k_bh_a]\),
\(\mathbb E[v_bd_a]\), and the bounded passive statistic
\(\mathbb E[k_bq_a]\). For the prediction velocity it applies to the
joint Gaussian observable already described. Consequently

\[
 \left|\mathbb E\dot f_n^\theta(t)
                  -\dot f_{\rm law}^\theta(t)\right|
       \le C\rho(t)n^{-1/2}
\]

for almost every time, with uniform constants. This is a mean-bias
estimate, not a coupling of an individual finite neuron to an independent
population representative. It supplies an integrable deterministic
source because \(\int\rho=S\). Bounded passive query sets can be
adjoined with the same argument and uniform data constants.

The cutoff removal in cavity Section 12 is adequate for these forced
systems. The Jacobian has at most quadratic dependence on
\(K_W=\|W_0\|_{\rm op}\); each fixed-order variation is bounded by a
polynomial times \(\exp(CS(1+K_W^2))\), not a double exponential.
The stated Gaussian operator tail gives uniform moments for sufficiently
large width and exponentially small cutoff contributions. For velocity,
the separate bound \(C\rho(1+K_W)\) is enough. Conditioning the forced
expectation on the original fitting event is a final restriction of
these integrable variables, not a claim of conditional Gaussian roots.

## Identification and frozen actual histories

The preceding fixed point can be identified with the own forced
common-action population using the assigned population construction.
For each fixed deterministic admissible \(\theta\), its fixed-mesh
Gaussian-program argument applies with these coefficients supplied.
Cell-integrating merely measurable residual controls gives their
\(L^1\) mesh approximation. The vector-field Lipschitz estimate on an
operator cutoff then gives convergence of the forced Euler states as
the mesh is refined. Append \(k_bh_a,v_bd_a,q_a,W_0q_a\) as program
outputs; their local smoothness and the bounded common action give the
same limit. The velocity uses the prescribed bounded value
\(\dot K/\rho\) at its output time, so this step does not differentiate
a convergence assertion. Bounded outputs and the forced velocity moment
bound give uniform integrability.

Thus the finite expectations have the common-action forced population
limit as well as the law-map limit just proved. Uniqueness of limits
identifies the two. This argument is for every deterministic admissible
history, so the uniform statistical bounds can subsequently be applied
to the width-dependent deterministic histories \(\bar\theta_n\).
It relies on the common-action/fixed-program result furnished by the
assigned population source; it is not an independent audit of that
source's outside dependencies.

The admissibility repair in feedback Section 1 is correct. On the original
good event, \(\|\dot r_n\|_m\le C\rho_n\), so
\(Ye^{-Ct}\le\rho_n(t)\le Ye^{-\lambda t}\). Therefore
\(s_n(t)\le C\bar s(t)\), uniformly in time, where
\(\bar s=\mathbb E[s_n\mid\mathcal G_n]\). It follows that

\[
 |\bar V(t)|\le C\mathbb E[s_n(t)^3\mid\mathcal G_n]
                    \le C\bar s(t)^3.
\]

The derivative estimates for \(K,V\) give
\(|\dot{\bar K}|+|\dot{\bar V}|\le C\bar\rho\); their activity
Lipschitz hypothesis and bounded \(\dot{\bar K}/\bar\rho\) follow.
Jensen alone would not have proved the cubic estimate. The lower activity
bound also keeps the normalized metric constants uniform over these
histories for each fixed positive label size.

Combining the forced-law estimates with scalar freezing supplies the
statistical statements (5)–(7) in the additionally assigned feedback
completion, including its \(K\)-velocity statistic. The comparison of
actual and frozen velocities must be made directly in their exact
velocity formulas; residual factors multiply the bounded gates before
differencing. No derivative of \(r/\rho\), and no derivative of the
uniform state-error estimate, is required.

## What this check does not establish

The conditional damped-feedback implication is a separate deterministic
argument, assigned to another checker. This report establishes that the
revised cavity and map inputs are compatible with its stated statistical
hypotheses, under the supplied common-action construction and fitting/
concentration inputs. It does not replace that implication by a claim of
full autonomous convergence solely from Banach contraction.

Finally, the frozen cavity source gives only
\(\Pr(\mathcal G_n^c)\le C/n\) for the original fitting event.
With a conditional mean-square theorem this already yields a
fixed-confidence bound with failure probability \(\delta+C/n\).
The stronger displayed \(\delta+Ce^{-cn}\) in the restoration note
requires its separately stated stronger event assumption. Neither event
probability, by itself, bounds the original dynamics' all-time squared
prediction on that exceptional set. No verdict about the requested
all-initialization second moment should be inferred from this scoped
bridge check.
