# Physical-gradient-flow dictionary at two fixed axis probes

## Statement and scope

This note computes the first three nonzero powers in the middle-weight velocity of the actual two-hidden-layer tanh population gradient flow, and identifies the initialized functions needed to represent them. The finite-order identities are not a convergence theorem for the infinite Taylor series, not an autonomous-closure convergence theorem, and not an empirical comparison of dictionaries.

The canonical network has no biases, input dimension two, preactivation `W^(1)x/sqrt(2)`, and readout pairing `E_2[W^(3)H^(2)]`. The population first row starts at two independent standard Gaussians, the middle action is the original initialized Gaussian operator and its actual adjoint, and the population readout starts at zero. The finite model has stored variances `(1,1/n,1/n^2)` and mobilities `(n,1,n)`. Exactly zero finite readout below is used only for an algebra oracle; it is not silently substituted for the actual finite random initialization in a width theorem.

Take the literal requested inputs `x_1=e_1=(1,0), x_2=e_2=(0,1)`, equal weights, symbolic labels `y_1,y_2`, and unhalved probability loss `L=(r_1^2+r_2^2)/2`. Thus `Z_a^(1)(0)=W^(1)(0)e_a/sqrt(2)`. The earlier book dictionary uses `sqrt(2)e_a`; comparing it at literal axes means the same construction at a different input scale. Structural polynomial and new-query conclusions are unchanged, but variance constants and lower acceleration factors change with this scale.

All initialized fields below are evaluated at time zero. Write

\[
Z_a^{(1)}=W^{(1)}(0)e_a/\sqrt2,\quad
H_a^{(1)}=\phi(Z_a^{(1)}),\quad
Z_a^{(2)}=W^{(2)}(0)H_a^{(1)},\quad
H_a^{(2)}=\phi(Z_a^{(2)}),\qquad \phi=\tanh.
\]

Let

\[
v=E\phi(G/\sqrt2)^2,\qquad
\tau=E\phi(\sqrt vG)^2,\qquad G\sim N(0,1).
\]

The two initialized upper preactivations are independent `N(0,v)`, so
`E_1[H_a^(1)H_b^(1)]=v delta_ab` and `E_2[H_a^(2)H_b^(2)]=tau delta_ab`.

## Exact gradient field

Put `r_a=f_a-y_a`, and use the same population for each product. The equations are

\[
\dot W^{(3)}=-\sum_a r_a H_a^{(2)}(t),
\]
\[
\dot W^{(2)}=-\sum_a r_a
 [W^{(3)}\phi'(Z_a^{(2)}(t))]\otimes H_a^{(1)}(t),
\]
\[
\dot W^{(1)}=-\sum_a r_a\phi'(Z_a^{(1)}(t))
 (W^{(2)}(t))^*[W^{(3)}\phi'(Z_a^{(2)}(t))]
 \frac{e_a^T}{\sqrt2}.
\]

Here `u tensor h` acts as `g -> u E_1[hg]`. At finite equal width its representative is `u h^T/n`; the adjoint is the actual transpose. These equations are the established physical gradient field with weights `1/2`, not an update that freezes residuals or hidden blocks.

## Coefficients through cubic middle-weight velocity

Define the first readout coefficient and first middle velocity coefficient:

\[
S=\sum_{b=1}^2y_bH_b^{(2)},\qquad
\mathcal D=\sum_{a=1}^2y_a
 [S\phi'(Z_a^{(2)})]\otimes H_a^{(1)}.
\]

Since `W^(3)(0)=0`, both hidden weights have zero initial velocity. The first corrections to hidden activations and upper preactivations are

\[
V_a=\frac{y_a}{4}\phi'(Z_a^{(1)})^2
 (W^{(2)}(0))^*[S\phi'(Z_a^{(2)})],
\]
\[
R_a=\frac{v y_a}{2}S\phi'(Z_a^{(2)})+W^{(2)}(0)V_a,
\qquad J=\sum_b y_b\phi'(Z_b^{(2)})R_b.
\]

Their meanings are

\[
H_a^{(1)}(t)=H_a^{(1)}+t^2V_a+o_{L^2}(t^2),\quad
Z_a^{(2)}(t)=Z_a^{(2)}+t^2R_a+o_{L^2}(t^2).
\]

The readout and residual coefficients are

\[
W^{(3)}(t)=tS-\frac\tau2t^2S
 +t^3\left(\frac{\tau^2}{6}S+\frac J3\right)+o_{L^2}(t^3),
\]
\[
r_a(t)=-y_a+t\tau y_a-\frac{\tau^2}{2}t^2y_a+o(t^2).
\]

Consequently

\[
\dot W^{(2)}(t)
=\left(t-\frac{3\tau}{2}t^2+\frac{7\tau^2}{6}t^3\right)\mathcal D
 +t^3\mathcal F+o_{\mathrm{HS}}(t^3),
\tag{1}
\]
where

\[
\mathcal F=\sum_a y_a\left\{
 \left[\frac J3\phi'(Z_a^{(2)})
       +S\phi''(Z_a^{(2)})R_a\right]\otimes H_a^{(1)}
 +[S\phi'(Z_a^{(2)})]\otimes V_a
\right\}.
\tag{2}
\]

Thus the first two velocity coefficients use the same feature family. The new reverse-and-forward query chain enters the cubic velocity coefficient, or the quartic coefficient of the weights themselves. Integrating (1) gives the middle-weight increment coefficients `D/2`, `-tau D/2`, and `7 tau^2 D/24 + F/4` at powers two, three, and four.

### Derivation and low-order remainder

On any continuous strong local solution, bounded tanh and residuals imply `W^(3)=O_Linfinity(t)`. The two hidden velocities are `O_L2(t)` and `O_HS(t)`, since the middle operator remains bounded locally. Hence hidden state increments are `O(t^2)`. The readout equation first yields `W^(3)=tS+O_L2(t^2)` and `r_a=-y_a+t E_2[SH_a^(2)]+O(t^2)`. The upper Gram is `tau I`, yielding the stated linear residual coefficient.

Divide the hidden velocities by `t` and pass to the initial state. Bounded gates times a fixed `L2` field converge in `L2`: convergence in probability of the gates, their uniform bound, and integrability of the fixed field's square give this by dominated convergence/uniform integrability. The remaining varying `L2` factor is controlled by the common gate bound. This proves the quadratic coefficients of both hidden weights. In particular

\[
[t^2]W^{(1)}=\frac12\sum_b y_b\phi'(Z_b^{(1)})
 (W^{(2)}(0))^*[S\phi'(Z_b^{(2)})]\frac{e_b^T}{\sqrt2}.
\]

Multiplication by `e_a/sqrt(2)` produces the factor `1/4`, since the literal axis Gram is `delta_ab/2`. Differentiating tanh along that fixed direction gives `V_a`. Also `[t^2]W^(2)=D/2`, and `(D/2)H_a^(1)=(v y_a/2)S phi'(Z_a^(2))`, giving `R_a`.

The required composition fact does not assert Frechet smoothness on all of `L2`: if `X_t=X+t^2B+o_L2(t^2)` and a scalar function has bounded continuous first derivative, then
`F(X_t)=F(X)+t^2F'(X)B+o_L2(t^2)`. Remove the remainder by Lipschitz continuity; for the fixed direction `B`, dominated convergence applies to the difference quotient bounded by `2 Lip(F)|B|`. Apply this to tanh and tanh'.

Substitution into the readout equation gives its quadratic coefficient `-tau S/2` and hence the quadratic residual coefficient `-tau^2 y_a/2`. At the next readout order, `3[t^3]W^(3)=J+tau^2 S/2`. The velocity is a product of the residual, readout, upper gate and lower feature. Collecting those four factors gives (1)--(2), including both gate motion and lower-feature motion. Terms such as a fixed `L2` cubic readout coefficient times the gate difference vanish after rescaling by dominated convergence. Tensor remainders use `||u tensor v||_HS=||u||_2||v||_2`. These arguments establish the displayed finite expansion on the strong flow; they do not sum an all-order Taylor series.

## Explicit dictionary generators and comparison with polynomial degree

Keep labels symbolic. The first upper functions are

\[
U_{ab}=H_b^{(2)}\phi'(Z_a^{(2)})
      =H_b^{(2)}[1-(H_a^{(2)})^2],\qquad a,b\in\{1,2\}.
\]

They lie in the existing upper polynomial span of degree at most three, not generally its first-degree span. The first new lower/upper dependency chain is

\[
U_{ab}\ \longmapsto\ (W^{(2)}(0))^*U_{ab}
\ \longmapsto\ \phi'(Z_a^{(1)})^2 (W^{(2)}(0))^*U_{ab}
\ \longmapsto\ W^{(2)}(0)
 [\phi'(Z_a^{(1)})^2 (W^{(2)}(0))^*U_{ab}].
\]

The lower first-weight velocity uses one lower derivative gate; the lower activation coefficient uses two for these orthogonal probes. General inputs produce mixed lower gates and input-Gram factors, as recorded in ALGEBRA_CHECK.md. Derivative order is not polynomial degree or matrix-pass count.

For a label-independent dictionary, take all initialized scalar fields in the differentiation graph, and separate coefficients in symbolic labels (and input weights if variable). Keeping all displayed factor fields is a finite sufficient superset, not a minimal count: repeated label monomials can combine symmetrically. At fixed time order and two probe indices, there are finitely many such fields. Freezing actual labels to one symmetric pair before extraction can discard useful directions.

### Why higher polynomial degree alone misses new reverse directions

For this comparison only, form the old lower core at the same input scale:
`h_a=H_a^(1)`, `k_a=tanh((W^(2)(0))*H_a^(2))`. The exact initialized reverse rule is

\[
(W^{(2)}(0))^*F
=\zeta_F+\sum_jh_j E_2[\partial_{Z_j^{(2)}}F],
\qquad E[\zeta_F\zeta_B]=E_2[FB],
\]

with jointly Gaussian lower sources independent of the lower input Gaussian row. The old four core entries determine precisely that row and the two sources `zeta_(H_1^(2)), zeta_(H_2^(2))`: apply inverse tanh to `h` and `k` and subtract the known response.

For `a != b`, the orthogonal projection of `U_ab` onto `span(H_1^(2),H_2^(2))` is `(1-tau)H_b^(2)`. Its squared residual norm is

\[
\tau\,\operatorname{Var}((H_a^{(2)})^2)>0.
\]

This is exactly the conditional variance of the unexplored part of the reverse source. For `a=b`, write `m4=E(H_a^(2))^4`; the corresponding positive variance is
`E(H_a^(2))^6-m4^2/tau`, positive by strict Cauchy--Schwarz and interval support. The deterministic source response depends only on the old lower row. Thus each new reverse field retains positive conditional variance given the old four features. Multiplying by the nonzero lower tanh-derivative gates preserves this fact.

Consequently these fields are not measurable functions of the old four-feature core. Finite or infinite polynomial enrichment of that core cannot recover them exactly in `L2`. This does not apply to the full established hierarchy, which also appends new initialized action words. It supplies a specific mathematical reason to prioritize actual gradient-flow queries, not a performance theorem.

## Fixed probes and additional samples

A fixed derivative order and fixed probe set give a feature list independent of the number of training observations. Repetitions at the two probes merely alter their aggregate weights and label means. When new input directions are admitted, the same dictionary is an approximation: already `H^(1)(0,x)=tanh(W^(1)(0)x/sqrt(2))` need not be in the finite lower span, and applying the initialized connector to that new function requires another query.

The obstruction is to universal exactness of a finite linear feature span, not to reconstructing a lower activation nonlinearly from the two input Gaussian coordinates. Arbitrarily many distinct positive first-coordinate input components produce linearly independent tanh ridge functions: an almost-sure relation becomes an everywhere relation by continuity; restrict the second Gaussian coordinate to zero, subtract the limit at positive infinity, and remove the slowest exponential tail successively. This applies even to arbitrarily many unit input directions.

The proposed construction can therefore keep its dictionary fixed while evaluating the actual loss on all samples. General-input approximation quality must be assessed separately, and angular probes or input-polynomial resolution can be enriched independently of sample count. No exact finite closure for all inputs has been asserted.

For exact matching of the two-probe derivatives by a projected model, keep the inputs AND outputs of every initialized action call, including the initial preactivations `W^(2)(0)H_a^(1)`. With orthogonal projections, `P_2 W^(2)(0)|_(V_1)` and its true adjoint reproduce each retained call if both argument and result are in their assigned spaces. Retaining the other required products proves finite differentiation-graph matching inductively. Ridge filtering generally introduces bias into this exact statement. Some retained derivative fields are unbounded; transplanting the established bounded-word closure theorem to this proposed dictionary requires additional work.

## Checks and provenance

The independently derived general coefficients and structural check are in ALGEBRA_CHECK.md and STRUCTURE_CHECK.md. These are internal checks, not promotion reviews. Root verified the source-response rule against established C.4.7.8 (H6), the physical metric against NOTATION.md and (H2), the old polynomial definition against C.4.7.10 B, and low-order hidden-motion structure against C.5 (C5.17)--(C5.21).

`jet_check.py` independently implements truncated scalar/matrix series operations and the entire finite vector field. It compares against the general hand-derived coefficients, including moving residuals, through cubic middle velocity. Four deterministic width-seven cases cover axes, correlated inputs/unequal weights, duplicate inputs, and zero labels. This is an algebra check, not a training experiment or a population numerical test. All errors are below `7e-18`, with declared tolerance `2e-13`. The symmetric population simplification is checked algebraically, not inferred from a finite Gaussian sample.

Established source hashes at derivation:

- `docs/NOTATION.md`: `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b`.
- `docs/global_nonlinear.md`: `81d969a531fc6daee26dbee2041fad8a3425a4b01580351387c5fc376cef412c`.
- `docs/README.md`: `60816cf89cf93abc9d752b7d56a66b3302cd9ca0caff4b247991647dfb49b3ad`.
