# Internal independent audit of the angular-extension route

Date: 2026-09-16. This is an internal mathematical audit, not a promotion
review. The candidate was not edited.

**Verdict: PASS, with minor presentation corrections.** Relative to the
accepted canonical initialization and finite-closure equations, the frozen
candidate proves its stated result for the prescribed initialization and
the specified reflected two-point family. I found no incorrect factor,
unproved necessary estimate, counterexample within that contract, or use
of inaccessible future information. In particular, the positive angular
interval, strict learned upper-hidden separation gain, physical-time loss
rate, and convergence of the complete saved state all follow. This verdict
does not establish the corresponding claims for other orientations, data
laws, initial states, closure orders, or the original neural network.

## Scope, inputs, and provenance

The assignment authorized reading only the frozen candidate, the notation
contract, specified canonical sections, and required skill instructions.
I did not read the study README, other route or audit files, other studies,
study history, or other reviewers' findings. No experiments or numerical
approximations were run. The only programmatic verification computed file
and line-excerpt hashes; all mathematical checks below are analytic.

The candidate hash matched the assignment before the audit:

| Input | SHA256 |
|---|---|
| `route_extension.md`, complete | `2764f92f5ca13308d0e4d8f41b7ac5afc7ee9f7cc86ec1dcd05447c60881a4df` |
| `docs/NOTATION.md`, complete | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md`, whole-file identity only | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `docs/global_nonlinear.md:12237-12401` | `1c1d64f87d26dbe7977c49fc8f60f2c7655a963ba6a12d77cef09621f6ed7c91` |
| `docs/global_nonlinear.md:13177-13469` | `9ca9d676ac6c6cc94c257db39ff1953334c2357f8abb6e059dcbc929dd7a5ed5` |
| `docs/global_nonlinear.md:13469-13630` | `a30a89acb3bea8d61879a0d623f860f0795a197506c45edc35151175d83b8dd9` |
| `docs/global_nonlinear.md:15258-15392` | `6df73ea02aa1f9bc002c9a10ec031da428cec9212b6607468ccf3db2bf6a9fbd` |

Excerpt hashes include the original line terminators and inclusive endpoints.
The whole-file hash does not mean the entire canonical chapter was read.
The actual scientific reading covered the complete relevant saved-state,
equation, and local-existence arguments in C.4.7.9.3–4; the explicit
Gaussian-core initialization, contraction, normalization, and order-one
dictionary in C.4.7.10 B/C.1; the further C.1 metric/input-oddness/core
initialization discussion through the stated excerpt; and D.3's dictionary,
equations, energy, existence, and restart arguments. Adjacent lines present
in those excerpts were not used to import a convergence or neural-limit
claim.

Required process sources were read completely:

| Source | SHA256 |
|---|---|
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `/etc/codex/skills/investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |

There is no missing scientific input for this audit relative to the named
canonical results. The derivation of the canonical Gaussian source rule
and the underlying action norm bound is accepted from those sources; this
report does not independently reprove the entire canonical construction.

## Contract and claim coverage

The object is the exact order-one continuum closure, with the canonical
ridge `eta=1/4096`, exact inverse-Cholesky coefficients, separate lower and
upper Gaussian mark carriers, unhalved probability-weighted squared loss,
and the prescribed initial state `(g,0,D)`. The family has equal masses,
labels `+A,-A` for fixed `A>0`, and normalized directions
`nu_+=(epsilon,sqrt(1-epsilon^2))` and
`nu_-=(epsilon,-sqrt(1-epsilon^2))`. The two physical inputs are `sqrt(2)`
times these directions. All comparisons retain the same full mark
coupling. There is no particle, closure-order, neural-width, or time-step
limit in the theorem.

| Candidate claim | Candidate lines | Result |
|---|---:|---|
| Exact initialization and positive axis seed | 11–47 | Verified |
| Reflection invariance and residual reduction | 73–103 | Verified |
| Auxiliary-flow global finite-time existence | 105–114 | Verified |
| Axis invariant subsystem, cone, and balance | 118–150 | Verified |
| Perturbation estimates and every displayed constant | 155–185 | Verified |
| Positive interval, crossing, and strict separation gain | 191–215 | Verified |
| Physical-time conversion, rate, and finite path length | 219–234 | Verified |
| Full saved-state and joint-law convergence | 233–249 | Verified |
| Scope exclusions | 251–261 | Appropriate |

## 1. Initialization and strict positivity

Parity and independence make the lower raw Gram a constant block plus
two identical covariance blocks `[[v,r],[r,v_y]]`, interleaved in the
canonical ordering. The only nonzero Cholesky entry coupling `Y_i` to an
earlier nonconstant feature is its entry for `X_i`. Thus the actual
normalized coordinates, after merely grouping them, are exactly

\[
B_i=\left(\frac{X_i}{\ell},
 \frac{Y_i-rX_i/(v+\eta)}{n}\right),
\quad
\ell^2=v+\eta,\qquad n^2=v_y+\eta-\frac{r^2}{v+\eta}.
\]

The upper normalized odd coordinates are `beta_i=H_i/h`,
`h^2=tau+eta`. The constant coordinate has normalization
`1/sqrt(1+eta)` in each population, but its contraction row and column
vanish. There is no illicit switch from Cholesky normalization to
coordinatewise variance normalization.

Substituting `B=H_i,F=X_i` or `F=Y_i` into the canonical contraction
formula gives, respectively,

\[
 C(H_i,X_i)=\alpha v,
 \qquad C(H_i,Y_i)=\alpha r+\tau\chi.
\]

For the second normalized coordinate, subtracting
`r/(v+eta)` times the first raw contraction leaves
`alpha*r*eta/(v+eta)+tau*chi`. This verifies both entries of `m_0`,
including the easily missed ridge factor. Similarly
`E[B_i X_i]=(v/ell,r*eta/((v+eta)n))`, verifying `a_0`.

All of `v,tau,alpha,chi` are strictly positive. If
`j(x)=E_zeta tanh(zeta+alpha*x)`, then `j` is odd and strictly increasing:
`j'(x)=alpha E_zeta sech^2(zeta+alpha*x)>0`. Hence
`r=E[X_i j(X_i)]>0`. The positive ridge makes `n>0`. Therefore both
entries of `m_0,a_0`, their pairing `k_0`, and
`kappa_0=E tanh^2(beta_2*k_0)` are positive. The last fact also uses that
`beta_2` is nonzero with probability one. The proposed feature envelopes
follow directly from the raw column bounds `sqrt(5)` and `sqrt(3)`.

## 2. Symmetry, gradient factors, and existence

For the indicated sign reversals, normalized features obey
`b_l(S_l omega)=J_l b_l(omega)` and `D=J_2 D J_1`. A change of variables
on each carrier gives

\[
 a_{TX}(u)=J_1a_X(Ru),\qquad
 H_{TX}(u,\omega)=H_X(Ru,S_2\omega),\qquad
 f_{TX}(u)=-f_X(Ru).
\]

Here `R nu_+=nu_-`. Both the loss and the scalar observable `F` are
invariant under the linear raw-metric isometry `T`. Initialization is
fixed, including `R g(S_1 omega)=g(omega)`. Consequently both gradient
vector fields preserve the fixed-point space by uniqueness. On it,
`f_-= -f_+`, `F=f_+`, and the unhalved mean loss is exactly `(A-F)^2`.

The displayed three derivatives of `F` are correct in the population
`L2,L2,Frobenius` metric. In particular the readout derivative is `U`,
so `F_s=||V||_raw^2=K>=E U^2`. On this symmetric trajectory the two
residuals are `-e,+e`, with `e=A-F`. Substitution in the canonical
two-atom equation gives `X_t=2e V` in every block. Therefore
`s_t=2(A-F)` is the correct physical clock: no mass or factor of two
is missing.

The contraction of the coefficient-to-population maps gives
`|a|<=1`, `|d|<=||c||_2`, and `||q||_2<=||M||op ||c||_2`.
Thus the auxiliary readout, matrix, and row speeds are bounded by
`1`, `s`, and `(2+s^2/2)s`. Integrating yields every displayed finite-S
bound. The row supremum speed has the additional factor `B_1`.
These bounds control the actual local-existence variables
`(w-g,c,M)` in `L-infinity,L-infinity,Euclidean`, not just their weaker
raw norms. Bounded speeds supply endpoints at finite continuation times,
so the same contraction argument as in the canonical source applies to
the auxiliary equation for every finite `S`.

## 3. Axis reduction, positivity cone, and balance

At the axis, oddness in the input turns the difference of the two
sample gradients into the single `e_2` gradient. To check the invariant
subsystem rather than assume it, take `W` odd in `(g_2,zeta_2)` and `c`
odd in `beta_2`. Then the constant component of `a` vanishes, all its
coordinate-one components vanish by independence, and the constant and
coordinate-one components of `d` vanish by parity/independence. The
matrix derivative has only the coordinate-two row/block. The lower row
derivative has no first input component and depends only on the second
mark block. These properties hold initially and are preserved by the
reduced equations; uniqueness identifies their solution with the full
axis flow.

Differentiating `a=E[B tanh W]` and `k=m.a` gives exactly

\[
 k_s=d\left(|a|^2+E[(m\cdot B)^2\operatorname{sech}^4W]\right).
\]

While `k>0`,
`c(beta,s)=integral_0^s tanh(beta*k(v))dv` has the sign of `beta`,
strictly for `s>0` and `beta!=0`. Consequently `d>=0`, strictly for
`s>0`. Starting at `k_0>0`, a hypothetical first exit below `k_0`
contradicts this nonnegative derivative. Since `m.a=k>0`, `a!=0`,
and the derivative of `k` is strictly positive for `s>0`. This proves
the cone without assuming its conclusion in the continuation step.
Strict increase of `E tanh^2(beta*k)` for `k>0` then gives the asserted
strict axis hidden-separation increase and `F_axis(s)>=kappa_0*s`.

For the balance identity,

\[
 \frac d{ds}|m|^2=2dk,
 \qquad
 \frac d{ds}E\sinh^2W
 =E\left[2\frac{\tanh W}{\operatorname{sech}^2W}
       d(m\cdot B)\operatorname{sech}^2W\right]=2dk.
\]

On a finite interval `W-g_2` is bounded. Gaussian integrability of
`exp(a|g_2|)` for every finite `a` justifies differentiation under this
expectation. This is a valid balance, not a Euclidean contraction claim.

## 4. Perturbation estimates and constants

Use the candidate's `C=S`, `R=2+S^2/2`, and
`W=sqrt(2)+S^2+S^4/8` only in the following bounds. They control the
supremum readout, matrix operator norm, and row `L2` norm along both
flows on the common interval. All feature comparisons use the same
Gaussian carriers, not separately selected or relabeled realizations.

For either input sign, the contraction bounds and
`Lip(tanh)<=1`, `Lip(tanh')<=2` give precisely the five elementary
estimates at candidate lines 163–167. In the backward difference, the
term involving the gate is controlled by `||c_0||infinity<=C`.
In the row difference the gate term is controlled by
`||q_0||infinity<=B_1 R C`; thus no product of two unrestricted `L2`
errors is being estimated in `L2`.

For clarity, writing `E_w,E_c,E_M` for the three error norms and
`T=E_w+W delta` only in this computation, the three velocity estimates
can be bounded as follows:

\[
\begin{aligned}
 \|\delta V_c\|_2&\le E_M+RT,\\
 \|\delta V_M\|_F&\le E_c+2CE_M+(2CR+C)T,\\
 \|\delta V_w\|_2&\le RE_c+C(2R+1)E_M
                    +C(2R^2+2B_1R)T+RC\delta.
\end{aligned}
\]

Their sum has coefficients
`R+1`, `1+C(2R+3)`, and
`R+C(2R^2+2B_1R+2R+1)` on `E_c,E_M,E_w`, respectively, exactly as
listed. Its input coefficient is the last coefficient times `W`, plus
`RC`. The candidate's `L` exceeds each coefficient and its
`P=LW+RC` bounds the input coefficient. Therefore
`D^+E<=LE+P delta` is valid. Since `E(0)=0`, integration gives
`E(s)<=P delta (exp(Ls)-1)/L<=PS exp(LS)delta` on the entire interval.

The upper-feature difference obeys
`||delta U||_2<=E_M+R E_w+RW delta<=H delta` for the stated
`H=(1+R)Q+RW`. Both `U` fields have norm at most one, yielding
`|delta C|<=2H delta`. Finally
`F=E[cU]` gives `|delta F|<=Q delta+C H delta=J delta`.
All constants are finite and strictly positive where they occur in a
denominator. Their potentially enormous size does not invalidate the
strictly positive mathematical interval.

## 5. Crossing and strict hidden-separation gain

The auxiliary speed bounds give `K<=1+C^2+R^2 C^2=K_*` for both
flows. On the axis `|m|<=||M||op<=R`, `|a|<=1`, hence
`k_0<=k<=R`. Also `|beta_2|<=B_2`. Put
`h_*=E[beta_2 tanh(beta_2 k_0)] sech^2(B_2R)>0`.
Pointwise monotonicity of `beta*tanh(beta*k)` in positive `k` yields

\[
 d(s)\ge s h_*,\qquad
 |a|^2\ge\frac{k^2}{|m|^2}\ge\frac{k_0^2}{R^2},\qquad
 \frac d{dk}E\tanh^2(\beta_2 k)\ge2h_*.
\]

The nonzero denominator `|m|` follows already from `m.a=k>0`.
Combining and integrating the last inequalities gives
`C_axis(s)-kappa_0>=h_*^2 k_0^2 s^2/R^2`; its coefficient has no
missing factor of two.

The direction discrepancy is at most `2epsilon` on `[0,1/2]`.
Each entry in the definition of `delta_*` has a separate valid role:
`1` keeps this original parameter range, `kappa_0/(4H)` gives
`C_e>=kappa_0/2`, `A/(2J)` gives
`F_e(S)>=2A-A/2=3A/2`, and `g_* /(8H)` pays for both separation
comparisons. Thus continuity and strict positivity of `F_s=K` give a
unique crossing `0<s_*<S`, and `A=integral_0^{s_*}K ds<=K_*s_*`
gives `s_*>=A/K_*`. At this time the axis increase is at least `g_*`.
Subtracting at most `2H delta` at the endpoint and another `2H delta`
at initialization gives at least `g_*/2` for the perturbed increase.
Multiplying by four correctly converts this into the asserted `2g_*`
increase in squared `L2` separation.

The time `s_*` is a stopping value in the proof. It is not used in
the operational vector field, the initialization, the fitting set,
or any definition of the separation observable. Every constant defining
the family uses initialized Gaussian integrals, `A`, and finite algebra.

## 6. Physical time and complete-state topology

On `[0,s_*]`, `F` is continuously differentiable and its derivative
`K` is bounded and at least `kappa=kappa_0/2`. The scalar physical
clock therefore cannot cross its equilibrium `s_*`. On its positive
residual interval,

\[
 e_t=-2K(s(t))e,\qquad
 e(t)=A\exp\left(-2\int_0^tK(s(v))\,dv\right).
\]

The upper bound on `K` prevents reaching zero in finite physical time;
the lower bound forces `e(t)->0`. The bounded increasing clock has a
limit, and continuity plus uniqueness of the crossing forces that limit
to be `s_*`. The composed characteristic solution is the canonical
physical solution by uniqueness. Hence the loss estimate
`L(t)<=A^2 exp(-4kappa t)` has the correct unhalved-loss exponent.

Moreover `||X_t||raw=2e sqrt(K)` and `-e_t=2eK`, so

\[
 \int_t^\infty\|\dot X(v)\|_{\rm raw}\,dv
 \le \frac{e(t)}{\sqrt\kappa}.
\]

The raw product Hilbert space is complete. This finite path length gives
a strong limit and bounds its distance from `X(t)` by the displayed
tail length; the stronger feature-time continuity identifies it directly
as `X(s_*)`. Prediction continuity puts it in `Z_A`. The resulting
distance-to-set bound is consequently legitimate and does not presume
that the fitting set is nonempty before proving the crossing.

The canonical saved laws are `Law(b_1,g,w)` and `Law(b_2,c)`. With the
same static marks in the coupling, their squared `W2` distances are at
most `E|w(t)-w_infinity|^2` and `E|c(t)-c_infinity|^2`, respectively.
All required second moments exist: the marks are bounded, `g` is
Gaussian, and the moving increments are bounded on `[0,S]`.
The finite coefficient matrix converges in Frobenius norm, and `D`
is unchanged. Thus no portion of the saved state is omitted. Bounded
supremum velocities on the compact feature-time interval also give
`L-infinity` convergence of `w-g` and `c`. This conclusion concerns
the common-carrier representative and the indicated joint laws; it does
not assert an intrinsic raw metric between arbitrary differently coupled
representations of those laws.

## Adversarial objections and disposition

| Target / strongest obstruction | Discriminator and validity gate | Finding / consequence |
|---|---|---|
| Ridge or transpose error gives a wrong positive axis seed | Expand actual ordered Cholesky and apply the canonical raw contraction | Ruled out: both residual-coordinate ridge factors and the right transpose agree |
| Reflection fails because the dictionary is not rotation invariant | Check this exact coordinate sign reversal directly, without assuming rotational invariance | Ruled out for this family; arbitrary rotations are not covered |
| Cross-block feedback invalidates the scalar cone | Substitute the parity-restricted full state and inspect all constant and inactive components | Ruled out on the axis; the cone is not asserted for off-axis states |
| Perturbation control secretly uses an unbounded multiplier | Track each gate difference in the actual `L2` estimate | Ruled out: `c_0` and `q_0` have explicit supremum bounds |
| Crossing or the learned gain is circular | Derive global finite-S bounds first, then comparison, then crossing and its lower time bound | Ruled out; no estimate assumes fitting has already happened |
| A frozen-feature readout alone explains the result | Check the endpoint change of the same fixed upper-feature separation functional | Ruled out for this trajectory by the strict `2g_*` squared-separation gain; no claim that every coordinate moves is needed |
| Loss decay leaves an untracked drifting full state | Integrate actual raw speed, then couple all static marks identically | Ruled out for the saved state; stronger convergence is explicitly established |
| Future data, oracle endpoint, hidden history, or changing metric | Inspect all initialization/constants, RHS inputs, and definitions of `C,Z_A` | Ruled out; the auxiliary clock and crossing are proof devices only |
| Small-label or near-coincidence degeneration | Hold `A>0` fixed and inspect the certified input range | Unit labels are included; the theorem is near antipodal and has no near-coincidence claim |
| Numerical artifacts mimic positivity | Identify numerical evidence on which any sign depends | No numerical evidence is used; all positivity is analytic |

The strongest remaining limitation is structural specialization: the
theorem relies on reflected equal-mass opposite-label pairs and the
prescribed initialized trajectory. It does not produce a neighborhood
of convergent initial states, monotonic separation away from the axis,
or a contraction between arbitrary solutions. These are not needed by
the candidate and are expressly excluded where relevant.

## Surviving minor presentation issues

1. Candidate line 52 defines `u_+` and then uses `nu_+`. Rename that
   definition to `nu_+` so the family is literally well-defined.
2. At line 38, replace “All displayed entries are positive” by “All
   entries of `m_0` and `a_0` are positive.” The random feature entries
   displayed just above have both signs; the intended deterministic
   positivity claim is correct.
3. At line 124, say simply `B=B_i at i=2`. The phrase “B_2's lower
   two-coordinate block” competes with the immediately preceding use
   of `B_2` for the upper feature envelope. The following parenthesis
   resolves the meaning, so this is a notation defect only.
4. The phrase “no hidden feature is frozen” at line 56 is best stated
   as “all canonical feature equations remain active.” The axis
   symmetry does leave `w_1` and an inactive initialized matrix row
   unchanged, exactly as the proof later explains. This wording change
   distinguishes absence of an imposed frozen-feature approximation
   from a false assertion that every coordinate must move.

None of these changes alters a mathematical constant or conclusion.
The frozen proof is internally complete after interpreting the obvious
`u_+`/`nu_+` typo. No promotion or establishment claim is made by this
report.
