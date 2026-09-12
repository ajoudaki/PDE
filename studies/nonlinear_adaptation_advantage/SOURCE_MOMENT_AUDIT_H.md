# Source-moment audit H

Reviewer: scoped harmonic-route agent, 2026-09-12.

**Verdict: PASS for the proposed population finite-program lemma and its
reached-flow extension, with the scope prerequisites made explicit below.**
The two gate contributions, direct injections, memory contribution and final
L⁴ constant are correct. No corrective constant or missing derivative term
was found. The estimate is a bound on specific generated action inputs, not
an Lᵖ operator bound for the initialized action.

The claim was supplied in the supervisor's assignment, not read from another
current follow-up. Only already permitted established sources were used. No
neural sign search, experiment, Git operation or input-file edit was made.
This is internal checking, not promotion review.

## 1. Exact scope needed for the claim

The historical graph is a controlled raw Euler program of CT12–CT16, with
the canonical limiting zero readout and the same initialized action in both
orientations. Its standard reverse inputs are
$\delta_p=c_p\phi'(Z^2_p)$, so $|\delta_p|\le H$ almost surely.
Here $H$ bounds the total historical absolute update mass. The cap $B$
must bound **all preceding response rows used by CT29, and the appended
current backward rows**, not just the last endpoint row in isolation.
That is exactly the source-tube setting of C.4.9 unit A.

At the fixed endpoint there is no intervening parameter update while the
current queries $Q_i$ and then the probe input $F_u$ are formed. Every
current query has its own formal source name when appended, including
duplicated or antipodal inputs. Named derivatives hold all deterministic
coefficients, expectations and covariance entries fixed, including the
$a_i$ if they were computed from population projector coefficients.

Those conventions do not freeze coefficients in actual time evolution.
If this lemma is later used inside a time-derivative calculation, derivatives
of evolving $a_i$ remain separate terms. The present claim is about the
direction at the specified state:

\[
b=\sum_i a_i g(u_i),\quad \sum_i|a_i|\le M,\qquad
F_u=\phi'(w\cdot u)(b_w\cdot u).
\]

It does not cover arbitrary raw directions, an arbitrary newly differentiated
direction, random neuron-dependent coefficients, or a finite-width moment
bound inferred without a separate approximation argument. The finite-program
source rule is a population law theorem, not an exact finite-array Gaussian
conditioning identity with all learned coefficients replaced by expectations.
No actual finite initial Gaussian readout is set to zero by this claim.

## 2. Complete named-source calculation

Set

\[
D=B+H^3,\qquad Z=\sum_{\text{old }p}|\gamma_p||Q_p|,\qquad
\mathscr E=\exp(DH+2Z).
\]

CT29 gives, at every historical/current first-row state and for each old
reverse-source name $p$,

\[
|\partial_{\zeta_p}w_j|\le|\gamma_p|\mathscr E.
\tag{S1}
\]

A newly appended current reverse source has zero derivative in every such
$w_j$: no state update has used it. A historical zero-control source also
has zero derivative, by the no-injection induction in CT15.
Thus summing (S1) over old names costs at most $H\mathscr E$.

Write

\[
\lambda_i=u\cdot u_i,\quad
v_u=\phi'(w\cdot u),\quad v_i=\phi'(w\cdot u_i),\quad
F_u=\sum_i a_i\lambda_i v_uv_iQ_i.
\]

Here $|\lambda_i|,|v_u|,|v_i|\le1$ and $|\phi''|\le2$.
The current query has the frozen-source expression

\[
Q_i=\zeta_i+\sum_jD_{ij}H^1_j,\qquad
\sum_j|D_{ij}|\le D.
\]

The index $j$ includes its distinguished current forward slot and old
forward slots; an unused prior passive call adds zero coefficient. Since
all $D_{ij}$ are frozen under named differentiation,

\[
\partial_{\zeta_p}Q_i
=\mathbf1_{\{p=i\}}+
\sum_jD_{ij}\phi'(w_{t(j)}\cdot u_j)
                     (\partial_{\zeta_p}w_{t(j)}\cdot u_j).
\tag{S2}
\]

This is the full derivative. Correlation of two source coordinates does
not create an additional chain rule between their formal names.
At a singular covariance the distinct names remain distinct; III.F's
regularization identifies the contracted correction.

Differentiating $F_u$ has three groups:

1. **Direct query injections.** Only the first term of (S2) contributes.
   Their summed expected absolute contribution is at most
   $\sum_i|a_i|\le M$. If one reuses an identical current source name
   algebraically, the triangle inequality still gives this bound; merely
   identical input geometry is not a reason to merge names.
2. **Two gate derivatives.** Differentiating the outside gate costs at most
   $2H\mathscr E\sum_i|a_i||Q_i|$ pointwise after summing old names.
   Differentiating the gate in $b_w$ costs the same amount. If
   $\sup_i\|Q_i\|_2\le q_2$, Cauchy–Schwarz bounds their total expectation by
   $4HMq_2\|\mathscr E\|_2$. No independence of these factors is used.
3. **Memory derivatives.** The second term of (S2), summed over all source
   names and then over $j$, is bounded by $DH\mathscr E$ for each $i$.
   Multiplying by $|a_i|$, summing, and taking expectation gives
   $MDH\|\mathscr E\|_1$.

Taking absolute values after expectations can only decrease these bounds.
Consequently

\[
\sum_p\left|E\,\partial_{\zeta_p}F_u\right|
\le MC_\alpha,\qquad
C_\alpha=1+4Hq_2\|\mathscr E\|_2+DH\|\mathscr E\|_1.
\tag{S3}
\]

There is no factor proportional to the number of current queries, old slots,
or repeated observations. Their costs enter through $M$, historical control
mass and the response row sums.

## 3. Explicit envelope moments

CT27 gives a Gaussian source of variance at most $H^2$ and a bounded
remainder at most $D$. Thus $q_2=H+D$ is one permitted explicit choice for
all historical and current queries. Any sharper proved common L² bound can
replace it.

For $H>0$, Jensen with weights $|\gamma_p|/H$, padding their missing mass
by a zero term, and the scalar Gaussian exponential moment give

\[
E e^{\lambda Z}\le
2\exp(\lambda HD+\lambda^2H^4/2).
\]

No independence between different historical queries is used. Therefore
for every $r\ge1$,

\[
E\mathscr E^r\le2\exp(3rDH+2r^2H^4),\qquad
\|\mathscr E\|_r\le2^{1/r}\exp(3DH+2rH^4).
\tag{S4}
\]

In particular one may substitute
$\|\mathscr E\|_1\le2e^{3DH+2H^4}$ and
$\|\mathscr E\|_2\le\sqrt2e^{3DH+4H^4}$ in (S3).
If $H=0$, $Z=0$ and $\mathscr E=1$ directly. The displayed bounds remain
valid, but their derivation need not divide by zero.

## 4. Actual reused action and the L⁴ bound

At a fixed graph, $F_u$ is a finite sum of bounded smooth gates times
backward queries. Its coordinate value map has linear growth, and its
named derivatives have the finite polynomial envelopes required by
global_nonlinear A.1–A.2. Thus III.F's source rule applies through that
contained unbounded-product specialization, including singular source Grams.

For the appended action query it gives

\[
A_0F_u=\xi_{F_u}+\sum_p\alpha_p\delta_p,\qquad
\alpha_p=E\,\partial_{\zeta_p}F_u,\quad
E\xi_{F_u}^2=\|F_u\|_2^2.
\tag{S5}
\]

All reverse inputs on this active graph are the old and current bounded
$\delta_p$. An extra, unused branch of the common generated carrier has
zero formal derivative in $F_u$, and adds no correction.
This is the same initialized action and actual adjoint; no independent
surrogate forward operator was substituted.

Minkowski gives $\|F_u\|_2\le Mq_2$. A centered scalar Gaussian has fourth
moment three times the square of its variance, so (S3)–(S5) imply

\[
\|A_0F_u\|_4
\le M\{3^{1/4}q_2+HC_\alpha\}.
\tag{S6}
\]

The response remainder is pointwise bounded by $H\sum_p|\alpha_p|$.
Its possible dependence on the Gaussian term is immaterial to this triangle
inequality.

Historical ranks and current middle gradients give, pointwise in population 2,

\[
|KF_u|
\le\sum_p|\gamma_p||\delta_p|
                           |\langle H^1_p,F_u\rangle|
\le H^2\|F_u\|_2,
\]
\[
|b_KH^1(u)|\le
\sum_i|a_i||\delta_i||\langle H^1_i,H^1(u)\rangle|
\le MH.
\]

Thus the proposed first directional upper-preactivation bound is correct:

\[
\|b_KH^1(u)+(A_0+K)F_u\|_4
\le M\{H+3^{1/4}q_2+HC_\alpha+H^2q_2\}.
\tag{S7}
\]

Only an L² action bound on $A_0$ is used later for convergence; (S6) itself
comes from this generated-input source formula. It asserts no extension
$A_0:L^4\to L^4$ on arbitrary population inputs.

## 5. Passage to reached curves and continuum forces

For a fixed finite direction combination, take the source-admissible raw
Euler approximants from C.4.9–C.4.10. Their history caps and mass bounds can
be chosen uniformly. Strong raw convergence, bounded readouts and the
one-reference query comparison give $Q_i^{(n)}\to Q_i$ in L².
Bounded-multiplier continuity then gives
$F_u^{(n)}\to F_u$ in L². Here $n$ labels approximants, not neural width.
The argument also permits convergent deterministic coefficients with the
same absolute-sum bound.

Since $A_0$ is bounded on the canonical L² spaces,
$A_0F_u^{(n)}\to A_0F_u$ in L². The uniform L⁴ bound (S6), followed by
an almost surely convergent subsequence and Fatou, proves the same L⁴
bound at the reached state. It does not require convergence of a growing
list of individual response derivatives.
Rank subtraction gives strong L² convergence of the $K F_u$ and
$b_KH^1(u)$ terms; their uniform pointwise bounds pass by the same argument.
This proves (S7) for the reached curve.

For a deterministic signed spatial force measure of total variation at most
$M$, approximate its compact-input integrals by finite sums. The current
gradient factors are continuous into their L²/HS spaces, so these sums
converge strongly with uniformly bounded absolute coefficient mass.
The same strong-L²/Fatou argument extends (S6)–(S7) to that force.
Projector coefficients are legitimate here because they are deterministic
population scalars and the anchor gap bounds their resulting force mass.

The estimate is uniform over deterministic passive inputs $u$, through the
same constants. It is a supremum of individual L⁴ norms, not an L⁴ bound
on a random supremum over all inputs. It also does not automatically give
source-row caps for arbitrary later probes built from the new action output.

## 6. Checks, provenance and remaining limits

The exact source-moment claim was the supervisor's prompt reproduced in
mathematical form above. I reread global_nonlinear lines 13312–13408
(CT12–CT17), 13554–13614 (CT26–CT31 and its surrounding moment statements),
and special_data_limits lines 3960–4054 (formal-source convention,
source-rule proof and singular-query extension). Their full surrounding
required sections, A.1–A.2, and NSC25–NSC28 had already been read within the
permitted scope and are recorded in the earlier internal checks.

| Scientific input | SHA-256 |
|---|---|
| docs/global_nonlinear.md | 5c7f4cd85eebe73f497ff91cca4f3c525f158727c28b8a187a09add94e756483 |
| docs/special_data_limits.md | 5b7b48aa5deab320042217a6f284002366a683bf0f7f0b63c05d8167c526a489 |

Boundary checks: $M=0$ makes all claimed action values zero. At $H=0$ the
population readout, backward fields and hidden direction are zero, although
formal derivatives at a zero-variance current source need not be zero.
The source correction still vanishes because its $\delta_p$ inputs are zero.
Duplicated inputs preserve named derivatives; negative coefficients use
absolute mass; no singular input-Gram inverse or minimum nonzero control is
introduced.

The finite-program constants and continuum argument pass. The explicit
scope prerequisite is historical/current row-cap control, not merely an
endpoint-row cap. The conclusion is useful first-directional source regularity;
it contains no sign information, higher directional derivative theorem,
finite-width fourth-moment assertion, or E₀ advantage.
