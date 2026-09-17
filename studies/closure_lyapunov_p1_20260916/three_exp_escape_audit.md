# Independent audit of the three-input escape route

Date: 2026-09-16. This is an isolated internal mathematical review, not a
promotion review. No numerical experiment, external source, additional agent,
other study, author history, or previous review was used.

## Verdict

**PASS for the candidate's stated local results in the canonical odd
characteristic chart.** The lower moment submersion, its uniform coercivity
on every fixed bounded-displacement class, ridge-derivative independence,
negative second variation at every positive-loss stationary state with
`M != 0`, strict initial loss decrease, and represented stationary example
of loss `2/3` all reconstruct correctly. No substantive mathematical repair
is needed for those results.

This verdict does not establish deterministic saddle avoidance, a uniform
all-time displacement bound, bounded readout or middle matrix, generic
convergence, or a current-state exponential potential. The candidate
explicitly leaves those implications open, and they are not acceptance
conditions for this review.

Two nonblocking wording points should remain explicit when these results
are reused:

1. Odd perturbations preserve parity when the base row field is odd. This is
   the ambient scope fixed in candidate Section 1; it is not an additional
   conclusion for an arbitrary nonodd field in Proposition 1.
2. The constructed state has bounded `w-g` and `c`, finite `M`, and finite
   raw Hilbert norm. Its `w` is necessarily essentially unbounded because
   `g` is Gaussian. “Bounded odd state” in Proposition 4 must refer to this
   characteristic chart or to the raw norm, not to `w in L-infinity`.

## Frozen inputs, coverage, and version control

The assignment specified candidate SHA-256
`21788168510295cb46998f28ba339bd08039f614d5fed4aa6b06be2cd2bd09b9`.
It matched at initial reading and at the final pre-report check. The
candidate contained 494 lines. I read its complete original Sections 1–6,
including the introduction and source declaration.

During the audit the supervisor, then the author, sent metadata-only notices
that a follow-up section had briefly been appended and was being moved out
of the frozen candidate. I did not read that section. A subsequent direct
hash check confirmed restoration of the original 494-line file byte for
byte. No follow-up claim is included in this verdict.

| Input | Complete assigned coverage | SHA-256 at reading and pre-report check |
|---|---|---|
| `three_exp_escape.md` | Entire original file, lines 1–494 | `21788168510295cb46998f28ba339bd08039f614d5fed4aa6b06be2cd2bd09b9` |
| `docs/NOTATION.md` | Entire file | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `docs/global_nonlinear.md` | Complete C.4.7.9, lines 12084–12554; complete C.4.7.10 B, lines 13161–13430; complete C.1, lines 13431–13786; complete D.3, lines 15146–15528 | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| `arbitrary_pair_local.md` | Introduction and complete Sections 1–4, lines 1–331; no Section 5 or later | `4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a` |
| `generic3_stationary_geometry.md` | Entire file, 225 lines | `170447ad239b991762fd4597a0a52318d04b9c4bad750ad95ca4c0e15dd777db` |
| `generic3_metric_second_pass.md` | Entire file, 233 lines | `104ed0fe6a7ee9e58cbe5d5c9f5c97598523e57649229993e5f7747efb446b4e` |

Required process reading was the complete `solve-math-rigorously/SKILL.md`,
`investigate-conjectures/SKILL.md`, and its
`references/adversarial-audit.md`. Truncated combined tool output was
re-read in bounded sections before treating coverage as complete. The
global chapter's heading metadata was searched only to locate the assigned
sections. No missing scientific input was encountered. No scientific link
in the supplied dependencies was followed outside the assignment.

## 1. Exact state, normalization, metric, and parity

At order one the raw lower list is `(1,X)` with four odd coordinates and
the raw upper list is `(1,Z)` with two odd coordinates. The upper covariance
is `diag(1,tau,tau)` because its Gaussian coordinates are independent and
centered. Thus its odd Cholesky-normalized column is exactly

\[
 \beta=Z/\sqrt{\tau+\eta},\qquad \eta=1/4096.
\]

The lower odd Cholesky block is invertible, so `b=L_odd^{-1}X` is an
invertible linear transform of the raw four-vector. The map from `(g,zeta)`
to `X` has the displayed inverse in the candidate. Its derivative is block
triangular with strictly positive tanh derivatives on its diagonal. Since
the four Gaussian roots have positive variances, their joint density is
positive everywhere. Consequently `X` has positive density throughout
`(-1,1)^4`; every nonzero linear form in `b` has a null zero set.
No independence of the four components of `X` is used or true in general.

The canonical Cholesky identity gives

\[
 E[bb^T]\preceq I_4,\qquad E[\beta\beta^T]
       =\frac{\tau}{\tau+\eta}I_2\preceq I_2.
\]

It follows by duality that `|E[b h]| <= ||h||_2`, and hence `|a_i| <= 1`.
The active Frobenius norm is the restriction of the full coefficient
Frobenius norm. Removing zero constant coordinates does not whiten again,
rescale time, or alter the metric.

For three data atoms of masses `1/3`, the exact equations are

\[
 \begin{split}
 w'&=-\frac23\sum_i r_i(b^TM^Td_i)s_i u_i,\\
 c'&=-\frac23\sum_i r_iH_i,\\
 M'&=-\frac23\sum_i r_i d_i a_i^T,
 \end{split}
 \qquad
 d_i=E_2[\beta c\operatorname{sech}^2(Z\cdot v_i)].
\]

They are negative gradients of `L=(1/3)sum r_i^2` for
`L2(Omega_1;R2) x L2(Omega_2) x R^{2x4}` with ordinary Frobenius norm
on the last factor. Thus `L'=-||w'||_2^2-||c'||_2^2-||M'||_F^2`.
All transposes and factors `2/3` in the candidate agree with these equations.

Full lower-mark reversal makes `b` and odd `w` odd, so the lower gates
are even. Full upper-mark reversal makes `H_i` and `c` odd and its gates
even. Consequently the constant entries of `a_i` and `d_i` are zero.
The displayed active subsystem therefore is the full invariant subsystem;
its omitted middle gradients are zero as well. This uses mark parity,
not a reflection symmetry of the input triple.

The fixed-order continuation proof in the assigned canonical sources
bounds `w-g,c,M` in their characteristic existence norms on every finite
interval for bounded-label data. It applies to this triple. It does not
supply a bound uniform over infinite physical time.

## 2. Lower moment submersion

### Derivative and adjoint

Write `B_infty=||b||_infinity`. Bounded `tanh''` gives, for all `h in L2`,

\[
 |\mathcal A(w+h)-\mathcal A(w)-T_wh|
       \le C B_\infty\|h\|_2^2.
\]

This is a genuine Frechet derivative from `L2` to `R^{12}`, not merely
a pointwise derivative. Its operator is bounded by Cauchy–Schwarz.
The Lipschitz derivative of tanh likewise gives
`||T_w-T_v||_op <= C B_infty ||w-v||_2`, so the map is `C1`.
Pairing with `B=(B_1,B_2,B_3)` yields exactly

\[
 T_w^*B=\sum_i (b\cdot B_i)s_i u_i.
\]

### Injectivity of the adjoint

Every pair of directions is linearly independent: they are distinct unit
vectors and not antipodal. Thus the `2 by 3` direction matrix has rank two
and a one-dimensional kernel spanned by `k`, with no zero component.
If `T_w^*B=0`, then `(b dot B_i)s_i/k_i` is independent of `i` almost
surely. If any `B_i=0`, positivity of the gates implies all the linear
forms vanish almost surely, and positive density implies all `B_i=0`.

Otherwise `q_i=(b dot B_i)/k_i` are nonzero linear forms with common
sign almost surely. Two linearly independent linear forms take opposite
signs on a nonempty open subset arbitrarily close to zero. Positive density
on the raw cube prohibits this. Negative scalar multiples also have
opposite signs off a null hyperplane. Hence
`q_i=gamma_i q` for one nonzero form `q` and fixed `gamma_i>0`.
After discarding its null hyperplane,

\[
 \gamma_i\operatorname{sech}^2(w\cdot u_i)
 =\gamma_j\operatorname{sech}^2(w\cdot u_j).
\]

Taking logarithms and using
`log cosh x = |x|+e(x)`, `-log 2 <= e(x) <= 0`, gives precisely

\[
 \big||w\cdot u_i|-|w\cdot u_j|\big|
 \le \tfrac12|\log(\gamma_i/\gamma_j)|+\log2.
\]

The candidate's `delta` is positive. Indeed, if it were zero, compactness
of the unit circle would produce a unit `d` with three equal absolute
projections. For fixed `|d dot u|`, the unit circle has at most two
directions modulo antipodality, contradicting the three distinct such
classes. Homogeneity therefore bounds `|w|` by a finite constant depending
on `B` and the directions. Together with `||w-g||_infinity < infinity`,
this would make `g` essentially bounded, contradicting its Gaussian law.
Thus `T_w^*` is injective.

Since its domain is finite-dimensional, `T_w T_w^*` is a strictly positive
`12 by 12` matrix. The stated right inverse
`R_w=T_w^*(T_wT_w^*)^{-1}` satisfies `T_wR_w=I` exactly. Its range is
bounded because `b` and the gates are bounded. At an odd base `w`, its
range is also odd. This proves surjectivity even with the allowed odd
bounded directions; it does not replace the actual row field by twelve
independent trainable moments.

### Exact local realization

For `F(h)=A(w+R_wh)-A(w)` on `R^{12}`, boundedness of the finitely many
range fields gives `C1` regularity and `DF(0)=I`. On a sufficiently small
closed ball, `||DF-I|| <= 1/2`. For `|k| <= rho/2`, the map
`h -> k+h-F(h)` has Lipschitz constant at most `1/2` and norm at most
`|k|+|h|/2 <= rho`. Its iterates are Cauchy, remain in the complete
closed ball, and converge to a fixed point with `F(h)=k`.
This verifies nonlinear local attainment, rather than only infinitesimal
surjectivity. At an odd base it preserves parity and bounded displacement.

### Uniformity over bounded displacement

The pointwise minimum defining `J_R(B)` is measurable: its infimum equals
the infimum over a fixed countable dense subset of the compact `h`-ball.
Continuity in `h` makes that infimum a minimum. This supplies the implicit
measurability detail without a measurable selection theorem.

For `|B|=|C|=1`, put
`F_B(h)=sum_i(b dot B_i) sech^2((g+h) dot u_i)u_i`. Then

\[
 |F_B(h)|\le\sqrt3|b|,\qquad
 |F_B(h)-F_C(h)|\le\sqrt3|b||B-C|,
\]

so `||F_B(h)|^2-|F_C(h)|^2| <= 6|b|^2|B-C|`, uniformly in `h`.
Taking minima and expectations proves continuity of `J_R` on the
coefficient unit sphere.

If `J_R(B)=0`, the nonnegative pointwise minimum is zero almost surely.
For each such mark there exists some admissible `h` satisfying the
adjoint equation. Its existence suffices: gate positivity again makes
the fixed `q_i` common-sign linear forms and hence positive multiples.
The preceding logarithm/geometry argument bounds every such `g+h` by
one constant depending on `B`, independently of the mark and of which
minimizer was chosen. It follows that `|g|` is bounded by that constant
plus `R` almost surely, a contradiction. The zero-block case forces
`B=0` and also contradicts unit norm.

Therefore `J_R(B)>0` everywhere on the compact sphere, and its minimum
`kappa_R` is positive. Every actual field with `|w-g| <= R` lies above
the pointwise minimum, yielding

\[
 \|T_w^*B\|_2^2\ge\kappa_R|B|^2,
 \qquad T_wT_w^*\succeq\kappa_R I.
\]

This proof requires no compactness of a bounded function ball and no
interchange of minimization and expectation. The constant depends on
the fixed marks, normalization, geometry and `R`; it is neither an
evaluated constant nor an all-time condition number. The candidate
states those restrictions correctly.

Finally, stationarity and the exact row equation imply
`r_i M^T d_i=0` separately for each sample. At row rank two, `M^T` is
injective, so `r_i != 0` implies `d_i=0`. This consequence has no extra
loss factor and does not require any false independence of sample fields.

## 3. Independence of the ridge derivative

Let `S` be the finite span in Lemma 2. Combine duplicate and opposite
nonzero coefficient vectors. Outside finitely many proper lines one can
choose `z` such that `p dot z != 0`, each nonzero group has nonzero
projection, and distinct groups have distinct absolute projections.
The equal-absolute-projection constraints are the two proper lines
`(v_j-v_k) dot z=0` and `(v_j+v_k) dot z=0`.

An almost-sure identity among the continuous functions is an identity
on the entire open square, since the upper law has positive density.
Restriction to `Z=t z` gives an interval of equality around zero.
The functions are real analytic for every real `t`. Their difference
vanishes on all of `R`: if an interval of equality had a finite endpoint,
all derivatives would vanish there by continuity, and its convergent
Taylor series would extend the interval. No assertion about the support
of `Z` outside the square is needed.

If `v=0`, the left side becomes the nonzero linear function `t(p dot z)`
and cannot be a finite sum of bounded tanh functions. Otherwise, with
`b=|v dot z|>0`, it has asymptotic
`4(p dot z)t exp(-2bt)(1+o(1))`. After signs are absorbed, the right side
has distinct positive rates `b_j`. Its constant limit must be zero. If
any coefficient remains, its smallest nonzero rate `b_*` has leading term
`-2A_* exp(-2b_*t)(1+o(1))`. No higher-rate term cancels this leading
term, including when rates are integer multiples of one another.

For `b_*<b` the scaled right side has a nonzero limit and the left side
vanishes; for `b_*>b` the opposite comparison follows after division by
`t exp(-2bt)`; for `b_*=b` one side has a factor `t` and the other does
not. All cases contradict equality. Zero right-side coefficients also
cannot equal the nonzero derivative. Lemma 2 is proved for the full stated
finite collection, including zero features, collinear coefficients, and
equal/opposite groups.

## 4. Actual negative second variation

Take a nonzero residual `r_i` and a nonzero `p in range(M)`. Since
`M != 0`, such `p` exists even when `M` has rank one. Choose a lower
moment target with only its `i`th block nonzero and
`M delta a_i=sqrt(tau+eta)p`. Applying `R_w` produces a bounded odd
row field `X_w`, with `delta v_i=p` and all other `delta v_j=0`.
Thus the corresponding upper-feature derivatives are exactly those in
the candidate, including the normalization factor.

Let `e=k_i-P_Sk_i`, `S=span{H_1,H_2,H_3}`. The projection exists even
when the features are dependent, since their span is finite-dimensional.
Lemma 2 makes `e` nonzero. A finite linear combination of bounded odd
functions is bounded and odd, so this is a permitted readout direction.
It satisfies `E[eH_j]=0` for all `j`, whereas
`E[ek_i]=||e||_2^2>0`.

On the two-dimensional parameter plane generated by these directions,
all required derivatives exist and can be integrated. For example

\[
 D^2a_j[X_w,X_w]
   =E_1[b\tanh''(w\cdot u_j)(X_w\cdot u_j)^2]
\]

is bounded; `Z` is bounded, so the two corresponding upper derivatives
are bounded. Multiplication by the base readout is dominated by a
constant times `|c|`, which is integrable even if one interprets the
base domain as only `c in L2`. In the canonical bounded-readout chart
the domination is stronger. Thus this proof needs no unproved global
`C2` assertion about Nemytskii maps on unrestricted `L2` balls.

For any two directions on this plane,

\[
 Q(X,Y)=\frac23\sum_j
       \{Df_j[X]Df_j[Y]+r_jD^2f_j[X,Y]\}.
\]

For the pure readout direction `X_c`, `Df_j[X_c]=0` and
`D^2f_j[X_c,X_c]=0`. The mixed prediction derivative is
`E[e DH_j[X_w]]`, hence

\[
 Q(X_c,X_c)=0,\qquad
 Q(X_w,X_c)=\frac23 r_i\|e\|_2^2\ne0.
\]

Writing `q=Q(X_w,X_c)` and `A=Q(X_w,X_w)`, the finite choice
`a=-sign(q)(|A|+1)/(2|q|)` gives
`Q(X_w+aX_c,X_w+aX_c)=A-|A|-1<0`.
At stationarity the first derivative is zero, so the ordinary one-variable
Taylor expansion produces strict descent for sufficiently small nonzero
amplitude. The perturbations tend to zero in the physical Hilbert metric
and remain in the bounded-displacement odd chart, with `M` fixed.
This excludes local minima and proves the stated sense of strict saddle.
It gives no conclusion about the stable set of deterministic gradient flow.

## 5. Initialization and loss bounds

The initialization positivity used for three samples follows from the
assigned dependencies together, not from pairwise Gram positivity alone.
The pair source obtains
`nu(u)=(Phi(u_1),Phi(u_2))`, with odd strictly increasing `Phi`, as the
exact canonical raw upper coefficient vector. Its normalization comes
from `(G_2+eta I)^{-1}C(G_1+eta I)^{-1}`, retaining the reverse-response
term in `C`.

I checked the sign-sensitive estimate in that source: `v_0>=1/4`,
`tau>=1/7`, `alpha<=6/7`, and
`q_0 beta_0 <= beta(x) <= beta_0`, `q_0=529/1024`.
The normal equations yield positive regression coefficient `b` with
`b<=1/chi<=1/(q_0 beta_0)`, without assuming its companion `a` positive.
With `R_eta=v_0/(v_0+eta)>q_0`, they give

\[
 \frac{d}{dx}(ax+bm(x))
 \ge\alpha[1-R_\eta(q_0^{-1}-1)]
 \ge\frac{34\alpha}{529}>0.
\]

Gaussian integration by parts then gives the positive derivative
`Phi'(t)=E[j'(G) sech^2(tG+sqrt(1-t^2)Z)]/(tau+eta)`.
The endpoint passage uses bounded domination. Odd monotonicity and
unit input norms prohibit proportional coefficient vectors for distinct
non-antipodal inputs: scaling by a factor greater than one would increase
the magnitude of every nonzero input coordinate and violate unit norm.

For three nonzero coefficient vectors distinct modulo sign, the upper
features are linearly independent. Choose a line with three nonzero
distinct absolute projections. The coefficients of degrees `1,3,5` in
the tanh series give a Vandermonde system in their squared projections;
all three series coefficients are nonzero. Hence the candidate's
initialized `G_H` is positive definite.

Because `c(0)=0`, both `d_i(0)` and the initial row and middle velocities
vanish. Meanwhile `c'(0)=(2/3)sum_i y_iH_i(0)`, so

\[
 L'(0)=-\|c'(0)\|_2^2=-\frac49y^TG_Hy<0,
 \qquad L(0)=1.
\]

Continuity supplies a short interval of strict decrease; the exact energy
identity then gives `L(t)<1` for every `t>0`. At `M=0` all predictions
are zero and the loss is one, so the initialized trajectory never reaches
that stratum at positive finite time.

In the probability-weighted Euclidean norm on predictions, the reverse
triangle inequality gives `1-sqrt(L) <= ||f||`. For each sample,

\[
 |f_i|\le\|c\|_2\|H_i\|_2
 \le\|c\|_2\|\beta^TMa_i\|_2
 \le\|c\|_2\|M\|_{\rm op}|a_i|
 \le\|c\|_2\|M\|_{\rm op}.
\]

This proves (12) with the stated constant one. At times `t>=t_0>0`,
the left side is at least `1-sqrt(L(t_0))>0`. It forbids a vanishing
middle block with bounded readout, but does not bound either block
separately or preserve matrix rank.

## 6. The full stationary state of loss 2/3

At `w=g`, the local moment-attainment result applies in the odd chart.
Full column rank is dense in `R^{4x3}`: for a perturbation `E` having
one invertible `3 by 3` minor, that minor of `A+epsilon E` is a polynomial
in `epsilon` with nonzero cubic coefficient. Arbitrarily small nonzero
choices avoid its finitely many roots. Local attainment therefore gives
an actual odd `w=g+bounded` with independent columns `a_1,a_2,a_3`.

Surjectivity of `A^T:R4->R3` supplies `l` satisfying
`A^Tl=(1,2,1)`. Its one-dimensional kernel supplies nonzero `n` with
`A^Tn=0`. The vectors `l,n` are independent because `l dot a_1=1`.
Choosing the rows of `M` as `sqrt(tau+eta)l` and `n` thus gives row
rank two and raw upper vectors

\[
 v_1=v_3=(1,0),\qquad v_2=(2,0).
\]

The second row needs no extra normalization since all its contractions
with the three columns vanish. Hence `H_1=H_3=H=tanh Z_1` and
`H_2=J=tanh(2Z_1)` exactly.

The stated space `F` contains `H` and the two backward-derivative
directions. If `J` were in `F`, variation in `Z_2` on the open square
would eliminate its coefficient. Analytic continuation would then give
`tanh(2t)=A tanh t+B t sech^2 t` on `R`.
The limit at positive infinity gives `A=1`; after multiplication by
`exp(2t)`, the difference on the left tends to two, whereas the right
side is `4Bt(1+o(1))`. This is impossible for nonzero `B`, and `B=0`
also contradicts the nonzero limit. Thus `J_perp != 0`.

The readout `c=J_perp/||J_perp||_2^2` is bounded and odd, with

\[
 E[cH]=0,\quad E[cJ]=1,\quad
 E[cZ_1\operatorname{sech}^2Z_1]
 =E[cZ_2\operatorname{sech}^2Z_1]=0.
\]

Therefore the predictions are `(0,1,0)`, the residuals are `(-1,0,1)`,
and `d_1=d_3=0`. Direct substitution in the exact equations gives

\[
 c'=-\tfrac23(-H+H)=0,\qquad
 M'=-\tfrac23\sum_i r_id_ia_i^T=0,\qquad
 w'=-\tfrac23\sum_i r_i(b^TM^Td_i)s_i u_i=0.
\]

The inactive constant backward coordinate is also zero: its integrand
is the product of odd `c` and an even upper gate. The inactive lower
moment coordinate is zero by oddness of `w`. Thus every velocity of
the full `3 by 5` formulation, not just an ad hoc active reduction,
vanishes. The loss is exactly `(1+0+1)/3=2/3`.

This is an actual represented stationary state with the canonical frozen
mark laws, and Proposition 3 supplies its negative second variation.
It is not produced from `w=g,c=0,M=D` by the prescribed trajectory.
It therefore shows that parity, finite chart bounds, full active row rank,
and `L<1` do not exclude every nonfitting stationary state, without
showing any convergence failure from the specified initialization.

## 7. Adversarial checks and claim boundaries

| Target | Strongest obstruction checked | Discriminator and result |
|---|---|---|
| Lower moment surjectivity | Correlated marks permit exact cancellation of three row gradients | Common-sign linear forms, fixed gate ratios, and the positive absolute-projection gap would force a bounded Gaussian field; contradiction |
| Uniform coercivity for fixed `R` | Minimizing fields oscillate or escape without compactness of the function ball | Pointwise finite-dimensional minimization plus compactness only of the coefficient sphere; `J_R>0` proved without selecting a minimizing field |
| New readout direction | Collided, opposite, collinear, or zero upper features absorb the ridge derivative | Finite-group line reduction and the unmatched polynomial factor in its exponential asymptotic exclude all cases |
| Strict saddle | Positive pure row curvature overwhelms the perturbation | A zero pure-readout quadratic term and nonzero mixed term permit a finite coefficient making the quadratic form negative |
| Stationary example | Only the readout gradient cancels, or omitted constant coordinates still move | Direct substitution shows both backward coefficients for nonzero residuals vanish; parity also kills omitted gradients |
| Initialized loss bound | Pairwise initial rank is incorrectly promoted to rank three | Exact initialization monotonicity combined with the three-feature Vandermonde argument establishes full Gram positivity |
| Dynamical conclusion | A deterministic trajectory approaches a saddle stable set or escapes | These alternatives survive; the candidate expressly leaves them open |

There is no hidden future trajectory, additional dynamical memory, new mark
law, independently resampled transpose, changed learning metric, or linear
activation substitution. The arguments concern exact fixed-order nonlinear
population states. They do not infer finite-width convergence or an
all-time identification with the full uncompressed Gaussian system from
the canonical sources' restricted approximation theorems.

The three remaining barriers in the candidate are substantive and properly
separated: stable-set exclusion for the particular deterministic
initialization, infinite-time retention in the bounded-displacement chart,
and control of readout/middle escape. A negative curvature direction alone
does not close any of these. Their presence does not invalidate the local
theorems reviewed here.

Final disposition: all original Sections 1–6 are accepted at their stated
claim level, with the two nonblocking domain-wording clarifications above.
Only this audit report was written; no candidate or dependency was edited.
