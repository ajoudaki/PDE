# Internal audit of the initialized map for arbitrary input pairs

Date: 2026-09-16. Scope: initialization only; not a promotion review.

**Verdict: PASS.** Sections 1–4 of `arbitrary_pair_local.md` correctly
derive the initialized coefficient map and prove that its scalar function
`Phi` is odd and strictly increasing, with the stated positive derivative
bound. The rational constants `q_0=529/1024` and
`delta_0=34 alpha/529` are valid. The coefficient vectors are linearly
dependent exactly at coincidence or antipodality. The probability-weighted
initialized readout Gram is positive definite for every other pair, with
the stated eigenvalue normalization.

Consequently, the initialized hidden contrast `C_0` is strictly positive
for every distinct pair of unit input directions, including antipodal
pairs. This is an initialization result. For a generic oriented pair it
does not supply preserved opposite predictions, persistent Gram
coercivity, or an all-time convergence theorem.

## Input scope and provenance

Only sections 1–4, lines 20–331, of the assigned route were read for this
audit. Section-heading metadata was read to select that interval. Sections
5–7 and other new route/check files were not read. The permitted canonical
initialization and metric equations already audited earlier provide the
comparison standard. No numerical experiment was run and no source file
was modified.

| Input | SHA256 |
|---|---|
| `arbitrary_pair_local.md`, whole-file identity | `4bdb878378518455ca4e0cf7ea2ded8281d056b7aec98cef36c5ebf337c47b9a` |
| `arbitrary_pair_local.md:20-331`, actual excerpt including original line terminators | `e0a71a968e2831e2dbb65083dfa0e387312540ebfd09a580235dd168054c5bc1` |
| Prior audited `proof.md` | `8cb77d4a1a1f879fa75780efc521f39c63c56feafec4a6c32f15e97ca1621dd0` |
| Canonical `docs/global_nonlinear.md` | `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c` |
| Canonical `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |

The whole-file hash is an identity record, not a claim that the full route
or the full canonical chapter was read. The audit below checks every
estimate and constant in the assigned four sections.

## 1. Exact initialized map and its normalization

The raw lower covariance block and contraction row are respectively
`B=[[v_0,r],[r,ell]]` and
`(alpha*v_0,alpha*r+tau*chi)`. The second term `tau*chi` is the
canonical reverse-response contribution and is retained. The ridge
regression coefficients `(a,b)` in equation (1) and their Schur-complement
formulas in equation (2) follow by solving the two linear equations.
Their denominator is strictly positive because `B+eta I` is positive
definite; the numerator of `b` is positive.

The Cholesky normalization has the exact cancellation

\[
 b_2^T D E_1[b_1\tanh(g\cdot u)]
 =\psi_2^T(G_2+\eta I)^{-1}
       C(G_1+\eta I)^{-1}
       E_1[\psi_1\tanh(g\cdot u)].
\]

Indeed each factor `L^{-T}L^{-1}` equals `(G+eta I)^{-1}`. The
upper raw odd Gram is `tau I_2`, giving one factor `1/(tau+eta)`.
The lower blocks are independent and their constant/cross contractions
vanish. Integrating each block's independent reverse noise replaces
`a X+b Y` by `j(g)=a tanh(g)+b m(tanh(g))`. Thus the displayed
`Phi` formula and
`z_0(u)=Z_1 Phi(u_1)+Z_2 Phi(u_2)` have the correct normalization.
There is no omitted square root or extra factor of `tau`.

For a canonical unit input, `(g_i,g.u)` is a centered Gaussian pair
of unit variances and correlation `u_i`. The representation
`(G,tG+sqrt(1-t^2)Z)` is therefore valid, including the endpoint
degeneracies `t=+/-1`. This uses the Gaussian law of the first weights;
it does not rotate the fixed feature dictionary.

## 2. Rational bounds and positivity of the conditional derivative

Since `sinh^2(x)>=x^2`, monotonicity of `s/(1+s)` gives
`tanh^2(x)>=x^2/(1+x^2)`. For a centered Gaussian of variance
`sigma^2`, the stated Cauchy–Schwarz estimate is

\[
 E\frac{V^2}{1+V^2}
 \ge\frac{(EV^2)^2}{E(V^2+V^4)}
 =\frac{\sigma^2}{1+3\sigma^2}.
\]

The Gaussian fourth moment is `3 sigma^4`; the function
`s/(1+3s)` increases for `s>=0`. Applying the inequality first at
variance one and then at variance `v_0` proves
`v_0>=1/4`, `tau>=1/7`, and `0<alpha<=6/7`.

The Gaussian convolution of `sech^2` is maximal at zero. The level-set
argument in the source proves this directly: the Gaussian probability
of a translated centered interval has derivative
`phi_tau(R+a)-phi_tau(R-a)<=0` for `a>=0`. Tonelli's theorem applies
to its nonnegative level-set representation. This verifies
`beta(x)<=beta_0` without a log-concavity assumption.

For the lower bound, pairing the two signs in the sech-squared addition
formula yields the stated factor
`(1+tanh^2(z)tanh^2(a))/(1-tanh^2(z)tanh^2(a))^2>=1`.
Consequently `beta(x)>=beta_0 sech^2(alpha*x)`. On `|x|<=1`, the
previous `alpha` bound reduces this to `sech^2(6/7) beta_0`.

The factorial estimate `(2n)!>=2*12^(n-1)` holds at `n=1`, with
the inductive multiplier `(2n+2)(2n+1)>=12`. Hence for
`0<=z<=6/7`,

\[
 \cosh z\le1+\frac{z^2/2}{1-z^2/12}
 \le1+\frac{18/49}{46/49}
 =\frac{32}{23}.
\]

Inverting its positive square gives exactly
`q_0=23^2/32^2=529/1024>1/2`, proving both sides of equation (6).

For equation (7), conditional Gaussian integration by parts gives
`Cov(zeta,Y|X=x)=tau*beta(x)`. Conditional Cauchy–Schwarz then gives
`Var(Y|X=x)>=tau*beta(x)^2`. The variance decomposition and the
inequality `E m(X)^2>=r^2/v_0` imply

\[
 \ell+\eta-\frac{r^2}{v_0+\eta}
 \ge\tau E\beta(X)^2+\eta
 \ge\tau\chi^2+\eta,
\]

where `chi=E beta(X)`. Every Gaussian integration by parts has a
bounded tanh factor and bounded derivative, so its boundary and
integrability conditions hold.

Because `m(0)=0` and `0<m'(x)=alpha*beta(x)<=alpha`,
`0<r<=alpha*v_0`. The numerator estimate in equation (8) is valid:

\[
 \frac{\alpha r\eta}{v_0+\eta}
 \le\alpha^2\frac{v_0}{v_0+\eta}\eta
 \le\eta\le\eta/\chi.
\]

Dividing by the lower denominator from equation (7) gives
`b<=(tau*chi+eta/chi)/(tau*chi^2+eta)=1/chi`.
Finally `chi=E beta(X)>=q_0 beta_0`, proving the last bound in (8).

With `R_eta=v_0/(v_0+eta)`, the ridge value and `v_0>=1/4` give
`R_eta>=1024/1025>q_0`. The sharper derivative bound
`m'(x)<=alpha*beta_0` gives `r<=alpha*beta_0*v_0`. For the conditional
combination `k(x)=a x+b m(x)`, its exact derivative satisfies

\[
\begin{aligned}
 k'(x)
 &=\alpha R_\eta
       +b\left(\alpha\beta(x)-\frac r{v_0+\eta}\right)\\
 &\ge\alpha R_\eta-b\alpha\beta_0(R_\eta-q_0)\\
 &\ge\alpha\left[1-R_\eta(q_0^{-1}-1)\right]
 \ge\alpha(2-q_0^{-1})
 =\frac{34\alpha}{529}>0.
\end{aligned}
\]

Both uses of an upper bound have the correct sign:
`R_eta-q_0>0` makes the coefficient of `b` negative, and
`q_0^{-1}-1>0` makes the coefficient of `R_eta` negative. This
checks the central estimate without assuming `a>=0`. Oddness of
`m` gives oddness of `j`, and the chain rule gives exactly
`j'(g)>=delta_0 sech^2(g)>0`.

## 3. Gaussian interpolation and the uniform derivative bound

For `-1<t<1`, write `V=tG+sqrt(1-t^2)Z`. On compact interior
subintervals, differentiation under the expectation is justified by
bounded `j`, bounded gate derivatives, and Gaussian integrability.
Its numerator is

\[
 E[j(G)\tanh'(V)G]
 -\frac{t}{\sqrt{1-t^2}}E[j(G)\tanh'(V)Z].
\]

Gaussian integration by parts in `G` gives
`E[j'(G)tanh'(V)]+t E[j(G)tanh''(V)]`; integration by parts in `Z`
gives `sqrt(1-t^2) E[j(G)tanh''(V)]` for the second expectation.
The latter contributions cancel, leaving exactly equation (11):

\[
 \Phi'(t)=\frac{E[j'(G)\operatorname{sech}^2 V]}{\tau+\eta}>0.
\]

The right side has a bounded dominating function and extends
continuously to the endpoints. Since `Phi` itself is continuous there,
integration of its bounded derivative up to each endpoint is justified;
in particular its one-sided endpoint derivatives are the continuous
limits of this expression.

On the event `|G|,|Z|<=1`, whose probability is
`Pr(|G|<=1)^2`,

\[
 |V|\le |t|+\sqrt{1-t^2}\le\sqrt2,
 \qquad j'(G)\ge\delta_0\operatorname{sech}^2(1).
\]

This proves the source's uniform bound

\[
 \Phi'(t)\ge
 \frac{\delta_0}{\tau+\eta}
 \Pr(|G|\le1)^2\operatorname{sech}^2(1)
                  \operatorname{sech}^2(\sqrt2)
 =\sigma_0>0.
\]

The same bound passes to the endpoint derivatives. Symmetry of the
independent Gaussian variable `Z` gives `Phi(-t)=-Phi(t)`; at zero
independence and centering give `Phi(0)=0`. Thus the claimed strict
monotonicity on the closed interval is proved with no numerical sign
test.

## 4. Direction injectivity, Gram factors, and all distinct contrasts

For any unit direction `u`, the vector
`nu(u)=(Phi(u_1),Phi(u_2))` is nonzero. If
`nu(v)=lambda nu(u)` with `lambda>1`, then every nonzero coordinate
strictly increases in absolute value, while every zero coordinate
remains zero. This contradicts equality of the input Euclidean norms.
The same contradiction after reversing the roles handles
`0<lambda<1`; `lambda=1` gives `v=u` by coordinatewise injectivity.
For `lambda<0`, apply the positive-scalar result to `-v` using oddness.
It gives `v=-u`. Zero scalar is impossible. The converse follows
immediately from oddness. Thus equation (13) includes all coordinate
zero cases and is correct without rotational symmetry.

The initialized raw upper marks have positive density on `(-1,1)^2`.
If a nontrivial linear combination of the two hidden fields vanished
in upper `L2`, it would vanish almost surely. Continuity and positive
density extend the identity throughout the open square. Differentiating
at zero then yields the same linear dependence of `nu(u),nu(v)`.
For `v!=u,-u`, this contradicts equation (13), so the two-by-two
Gram is positive definite.

The factor in equation (14) is correct. The ordinary Gram is
`[[A_u,B_uv],[B_uv,A_v]]`. With data masses `1/2,1/2`, the readout
operator composed with its data-metric adjoint has matrix one half
of this Gram. Its least eigenvalue is therefore

\[
 \frac{A_u+A_v-sqrt{(A_u-A_v)^2+4B_{uv}^2}}4.
\]

At coincidence the two hidden fields agree; at antipodality they are
negatives because `Phi` and tanh are odd. The weighted Gram has rank
one in both cases. Its nonzero eigenvalue is `A_u>0`, since the
nonzero coefficient vector and positive upper-mark density exclude
an identically zero hidden field. These are exactly the rank exceptions.

The explicit bridge to the contrast needed elsewhere is

\[
 C_0(u,v)=\frac14E(H_0(u)-H_0(v))^2
         =\frac{A_u+A_v-2B_{uv}}4.
\]

For a non-antipodal distinct pair, this is the Rayleigh quotient of
the weighted Gram in the unit vector `(1,-1)/sqrt(2)`, so
`C_0(u,v)>=lambda(u,v)>0`. At antipodality it equals `A_u>0`.
At coincidence it is zero. Hence `C_0>0` holds exactly for distinct
directions; full Gram positivity additionally excludes antipodality.

Continuity of `Phi`, the bounded activation, and dominated convergence
make every Gram entry and its eigenvalue continuous. On a compact
family disjoint from coincidence and antipodality, the minimum of the
positive continuous eigenvalue is strictly positive. Approaching either
exception makes that eigenvalue tend to zero by the same continuity.
Thus the stated compact-family and nonuniformity qualifications are
both valid.

## Corrections and scope boundary

No mathematical correction is required in sections 1–4. When combining
documents, keep the regression coefficients `a,b` distinct from input
coordinates using the same letters elsewhere. The explicit contrast
bridge above is useful to state separately because antipodality is
degenerate for the full Gram but nondegenerate for opposite-label
contrast.

This audit establishes only the initialized structure and constants.
It does not audit the unread local convergence section, assert that a
positive initial full Gram stays positive, or remove the residual-
symmetry condition of the scalar physical-flow theorem. No fatal,
witness-fatal, major, or constant-level objection survives within the
assigned initialization scope.
