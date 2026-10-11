# Isolated check of the trained-probe noncancellation theorem

2026-10-11. Fresh isolated mathematical review. No experiments, Git actions,
candidate edits, prior reviews, other study material, or other reviewers'
findings were used.

**Verdict: PASS for the conditional qualitative theorem and its stated
probability qualification.** I found no substantive mathematical gap or
counterexample under the candidate's stated assumptions. In particular, the
original cap \(0<Y\le\lambda\beta^{-30L}\), where
\(\lambda=\gamma/m\le1\), suffices for both the probe chart and preservation
of two independent lower-feature values. The result concerns the compensated
infinitesimal cavity influence. It does not establish the actual dense-run
endpoint lower bound, and the candidate accurately states this distinction.

The rigorous-proof and canonical-notation skills, including the latter's
neural-network reference, were applied. The candidate and all four authorized
dependency inputs were read completely. No additional scientific input was
needed for the result being checked; references in those dependencies to
other source files were not followed.

## 1. Normalization, endpoint response, and integrability

The cavity deletes one last-hidden-layer neuron and keeps every original
width-\(n\) denominator. Its Euclidean mobility coordinates are
\(\xi=(W^{(1)}/\sqrt n,W^{(2)},\ldots,W^{(L)}_{-i,:},w_{-i}/\sqrt n)\).
Write \(F_v(\xi)\) for its prediction, \(j_v=\nabla_\xi F_v\),
\(h_v=h^{(L-1)}(v)\), and \(r_b=F_{v_b}-y_b\). For the probe's actual
incoming row \(u\), the change of variables
\(U=\sqrt n\,u\), \(H_b=h_{v_b}/\sqrt n\) gives exactly

\[
\dot a=-\frac2m\sum_b r_b\phi_L(U^\top H_b),\qquad
\dot U=-\frac2m\sum_b r_ba\phi_L'(U^\top H_b)H_b.
\]

In particular, there is no missing factor of \(n\) in the second equation.
The multiplicity family has predictor \(F_v+\mu b_v/n\), with
\(b_v=a\phi_L(U^\top H_v)\), and
\(V=n\partial_\mu\xi_\mu|_{\mu=0}\). Differentiation gives the stated
forcing \(-2m^{-1}\sum_b(b_bj_{v_b}+r_b\nabla_\xi b_b)\).
The derivative in its second term holds the current probe coordinates fixed.
Probe-coordinate variations acquire a prefactor \(\mu\) and vanish at
\(\mu=0\). Thus the candidate's endpoint formula

\[
I_v(g)=a_\infty(g)\phi_L(U_\infty(g)^\top h_v(\infty)/\sqrt n)
       +j_v(\infty)^\top V_\infty(g)
\]

uses the correct multiplicity derivative and the full retained-network
response.

The endpoint argument in the cavity dependency is valid. If \(J_\infty\)
has rows \(j_{v_b}(\infty)^\top\), its readout block and the fitting Gram
bound imply \(J_\infty J_\infty^\top\succ0\). The limiting generator
\(2J_\infty^\top J_\infty/m\) is positive semidefinite, with a strictly
positive spectrum on the complement of \(\ker J_\infty\). After subtracting
\(-J_\infty^\top(J_\infty J_\infty^\top)^{-1}b_\infty\), the response
equation has an exponentially decaying coefficient perturbation and forcing.
Its semigroup has norm at most one; integral Gronwall bounds the solution.
The component in the kernel has integrable derivative, and the complementary
component tends to zero by the stable semigroup convolution. This proves
convergence and \(J_\infty V_\infty=-b_\infty\), hence exact cancellation
at every training query. No exchange of the multiplicity derivative and a
nonlinear infinite-time limit is required.

The moment and continuity assertions also hold. At fixed cavity and width,
\(|a|+\|U\|\le C(1+\|g\|)\), since the probe vector field has linear
growth with an integrable coefficient proportional to the residual RMS.
Consequently \(b_v\) and \(\nabla_\xi b_b\) grow at most quadratically
in \(g\). The same quadratic bound holds for \(b_b(t)-b_b(\infty)\)
times an exponentially decaying time factor: differentiating \(b_b\) uses
only products of two probe states or velocities and fixed cavity-feature
bounds. The response's homogeneous coefficients depend only on the cavity,
so the stable/kernel decomposition gives
\(\|V_\infty(g)\|+|I_v(g)|\le C(1+\|g\|^2)\).
These objects therefore belong to Gaussian \(L^2\). On compact root sets
the bounds and exponential tails are uniform, which proves endpoint
continuity from finite-time ODE dependence.

## 2. Probe chart and infinite-time analyticity

Let \(B=2H\), \(K=\beta(1+B)^2\), and
\(A=\int_0^\infty2\rho(t)\,dt\le4Y/\lambda\), as in the candidate.
For \(\beta\ge10\) and \(L\ge2\),
\(1+B\le3(2\beta)^L\le\beta^{2L}\), so
\(K\le\beta^{5L}\) and \(AK\le4\beta^{-25L}<1/4\).
For \(\|g\|\le1\), the stated scalar differential inequality gives
\(1+|a|+\|U\|\le2e^{AK}<3\).
The more direct readout integral gives \(|a|\le2AK\): its integrand is
bounded using \(\beta(1+2B)\le2K\).

With \(q=D_ga\) and \(P=D_gU\), the differentiated system is exactly
\(\dot q=-b^\top P\), \(\dot P=-bq-aCP\).
The bounds \(\|b\|,\|C\|\le2\rho K\) use the real-axis bounds on
both \(\phi_L'\) and \(\phi_L''\), which are included in \(\beta\).
The full state Jacobian has norm at most \(2\rho K(1+|a|)\).
Thus \(\|P\|,\|q\|<2\); integrating the first equation improves the
second estimate to \(\|q\|\le2AK\), and integrating the second gives

\[
\|P-I\|\le6(AK)^2<1/2.
\]

The estimates are uniform on compact root subsets and the differentiated
coefficients are integrable. Therefore \(P\) converges locally uniformly,
its limit is \(D_gU_\infty\), and the inverse function theorem applies
throughout the open unit ball.

The candidate's complex-neighborhood argument is sufficient for endpoint
analyticity. For any fixed real root, the real probe trajectory is bounded.
A fixed-radius neighborhood of this trajectory can be chosen so that every
\(U^\top H_b(t)\) stays in the half strip. In that neighborhood the complex
vector field is holomorphic in its state, with derivative bounded by
\(C\rho(t)\). Taking the initial neighborhood smaller by the factor
\(\exp[-C\int_0^\infty\rho]\) closes the difference estimate for all
times and prevents departure from the strip. Its time derivative is also
bounded by \(C\rho(t)\). Finite-time holomorphic solutions consequently
converge uniformly on a smaller complex neighborhood. Their endpoint is
holomorphic there, proving real analyticity at the original real root.
Constants and neighborhood sizes may depend on the root, cavity, and width;
no uniform version is needed for this step.

The nonzero-readout witness is exact: setting the initial probe root equal
to \(\sqrt n\) times a retained top-row initialization reproduces that
neuron's readout and incoming row along the fixed cavity path. Fitting a
nonzero label vector forces at least one retained endpoint readout to be
nonzero. Hence \(a_\infty\) is a nonzero real-analytic function on
connected \(\mathbb R^n\), and cannot vanish on the unit ball. Restricting
around a point where it does not vanish gives the required chart.
Likewise, the real-analytic determinant of \(D_gU_\infty\) is nonzero on
the unit ball. The real-analytic zero-set theorem yields both almost-sure
claims in (10a). This is qualitative and does not control the chart's
Gaussian mass or any lower bound on the readout or singular values.

## 3. Feature richness after training and its probability

The two-query construction avoids a test-dependent gap. Equal input norms
make the diagonal \(q_0=Q^{(L-1)}(v,v)\) constant. Testing
\(Q^{(L)}\succeq\gamma I\) on \((e_a-e_b)/\sqrt2\), then applying the
Lipschitz bound of the last activation, gives exactly

\[
\gamma\le s^2\bigl(q_0-Q^{(L-1)}(v_a,v_b)\bigr),
\qquad \gamma\le2s^2q_0.
\]

Thus \(\kappa=\gamma/(4s^2)\le q_0/2\). The population kernel is
continuous by the finite-query Gaussian covariance construction in the
fitting proof. Connectedness of the sphere supplies a deterministic
\(v_*\) whose cross covariance with \(v_a\) is \(q_0-\kappa\).
The resulting two-query population Gram has smallest eigenvalue
\(\kappa\). Its empirical convergence gives the singular-value bound
\(\sqrt{\gamma/(8s^2)}\) with probability tending to one.

The displacement comparison retains the original label cap. The fitting
recursion has \(F_{L-1}\le F_L=F\), and
\(8H\sqrt F\le\beta^{5L}\), with \(H\ge1\). Hence

\[
\varepsilon=8F_{L-1}Y^2/\lambda^{3/2}
\le\frac{\sqrt\lambda}{8H^2}\beta^{-50L}
\le\frac{\sqrt\lambda}{8}\beta^{-50L}
<\frac{\sqrt\gamma}{8s}.
\]

The two-column perturbation has operator norm at most
\(\sqrt2\varepsilon\), strictly smaller than the initial singular-value
bound. The endpoint lower-feature map therefore has two linearly independent
values. Deleting a top neuron leaves its lower-layer initialization
unchanged; the supplied fitting lemma supplies the cavity's displacement
bound. The intersection of these two events has probability tending to one,
without independence or a new label condition.

At fixed endpoint parameters the lower-feature map is real analytic on
\(S^{d-1}\). Pairwise nonparallel training directions with \(m\ge2\)
imply \(d\ge2\), so this sphere is connected. If one nonempty open patch
had its nonzero image in finitely many lines, their closed preimages would
cover the patch, including its zero-image points. A finite union of closed
sets with empty relative interior cannot cover that open patch. One line's
preimage therefore contains an open subset. Composing the linear equations
defining that line with the feature map, analytic uniqueness extends them
to the whole connected sphere. This contradicts the two independent values.
Thus the nonparallel-richness claim holds on every open patch, on one common
event. No union bound over patches is needed.

## 4. Infinite rank and almost-everywhere variance

The ridge-function lemma is correct. A relation among
\(U\mapsto\phi_L(U^\top z_i)\), for nonzero pairwise nonparallel
\(z_i\), extends from any open set to \(\mathbb R^n\) by real-analytic
uniqueness. Nonaffineness and bounded real derivative imply that
\(\phi_L\) is nonpolynomial, so its Taylor series has a nonzero
coefficient of degree \(k\ge N-1\). The candidate's homogeneous
interpolation polynomial isolates each coefficient in
\(\sum_i c_i z_i^{\otimes k}=0\); nonparallelism is exactly what permits
each required separating linear form. Thus all \(c_i\) vanish.

The open probe chart permits division by the nonzero readout and change of
variables to \(U_\infty\), proving independence of the direct contributions
for arbitrarily large query collections on every patch. Their continuity
and the Gaussian's full support promote pointwise independence to
independence in \(L^2(N(0,I_n))\).

For a fixed cavity, compensation lies in the span of the \(D\) coordinates
of \(V_\infty(g)\), where \(D=\dim\xi<\infty\). Centering adds at
most the one-dimensional space of constant functions. If the centered
influences had finite-dimensional span, then the direct contributions
would lie in the sum of that span, the response-coordinate span, and the
constants, contradicting their infinite-dimensional span. This proves the
conditional covariance kernel has infinite rank on each patch. Selecting
finitely many independent centered influences gives the stated strictly
positive-definite covariance matrices.

Finally, positive variance at some query provides two roots whose influence
difference is nonzero there. That difference is a real-analytic function of
the query directly from the finite endpoint formula: both the endpoint
network and its parameter gradient are analytic. Its zero set has surface
measure zero on the connected sphere. At every other query, continuity in
the root and positive Gaussian mass of root neighborhoods imply positive
variance. The exceptional query set may depend on the cavity and width;
training queries belong to it. The candidate neither identifies this set
nor incorrectly replaces the almost-everywhere assertion by a statement
at each prescribed separated query.

## 5. Scope and minor issue

No additional quantitative hypothesis is missing for the stated
finite-width, conditional infinite-rank result. Its probability statement
is for each fixed admissible problem as width grows, with the candidate's
nonaffine activation and pairwise nonparallel training assumptions. It does
not claim a result for every activation/data configuration allowed by the
more general setup in `paper/compact.tex`.

The candidate correctly leaves open variance bounds uniform in width,
prescribed-query noncancellation, control of the error from replacing an
infinitesimal insertion by full neurons, and a collective anti-concentration
argument for actual dense-copy differences at scale \(n^{-1/2}\).
Finite rank of the compensating response is only useful qualitatively:
its dimension grows with width, and surviving covariance eigenvalues may
shrink. No lower bound of the desired scale follows from this review.

One presentation typo occurs at candidate line 263: `\sigma_{\min}\!left(`
should contain `\left(` after the negative thin space. The intended matrix
and singular-value estimate are unambiguous; this does not affect the proof.
The candidate was not modified.

## Reviewed input fingerprints

| Input | SHA-256 |
| --- | --- |
| `ENDPOINT_PROBE_NONCANCELLATION.md` | `f3cc7fe51f3dd33a15420ed5b88cb78ac236df65c2d0975344d70dcc5396282a` |
| `paper/compact.tex` | `460f29eda118ffe5bbc24be3a04d1a25c5e4a9bddb0744f8235d97a3674cabfe` |
| `paper/compact_fitting.tex` | `6efe077759c846c4b3d79f999c37d2d1478bae549d49fc9666837efbf9f1a01f` |
| `ENDPOINT_SEPARATION_CAVITY.md` | `cb756dd16c0c3eb3e2698945da480ca029059e3f47220b5766a887a4426fb5a7` |
| `NONPARALLEL_INITIAL_VARIABILITY.md` | `017c2dcbd3e3b938099ab7dd748a211f859126bd636767b667ef3432386e33bc` |
