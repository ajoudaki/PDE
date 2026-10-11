# Independent second check: zero-label extension

## Verdict and audit boundary

**PASS for the precise base theorem (1) in ZERO_LABEL_EXTENSION_RESULT.md.**
The argument proves unconditional high-probability convergence to zero loss
along the actual finite-width, fully trained gradient flow, with an
exponential bound after one deterministic finite time. It does not merely
prove finite-time approximation, a population statement, or a conditional
future kernel gap.

This is an internal mathematical check, not a promotion decision. The
verdict covers only the stated data class: one or two orthonormal active
inputs with labels of a common arbitrary magnitude, and finitely many
pairwise nonantipodal unit passive inputs orthogonal to the active span,
all having label zero. It does not cover the separately mentioned
open-neighborhood extension or an extension to three active inputs.

The candidate and both authorized dependencies were read in full. The
maintained Gaussian-program construction in
docs/12-three-sample-learning.qmd, III.F.1–11, was also checked. No other
review, study, numerical experiment, or open-neighborhood artifact was
used.

Audited SHA-256 identifiers:

- ZERO_LABEL_EXTENSION_RESULT.md:
  018a21bce9967a55ceb9a7f1c442d6a3e4e60c9c4e64184b4ba8e9ca5bf51b1e
- GAUSSIAN_POSITIVE_GEOMETRY.md:
  d220fba99906085e9770aceb33b939b5d0cfa2bb2bc005909f31fe2449afa574
- GAUSSIAN_NONORTHOGONAL_EXTENSION.md:
  37a4f9fea1e64c2404c066358a82f2611f733c6496512d6179bef501424f9b11

## 1. Equations, normalization, and the reference

Write
$U=\tanh(AX)$, $H=\tanh(WU)$, $f=H^\top w/n$,
$r=f-y$, and $\mathcal L=\|r\|_2^2/m$.
For a sample $a$, let
$b_a=w\odot(1-h_a^2)$ and $B_a=W^\top b_a$.
Direct differentiation with mobilities $(n,1,n)$ gives exactly

$$
\dot A=-\frac2m\sum_a r_a[(1-u_a^2)\odot B_a]x_a^\top,\qquad
\dot W=-\frac2{mn}\sum_a r_a b_a u_a^\top,\qquad
\dot w=-\frac2m\sum_a r_a h_a.
$$

Thus the candidate's factors of $m$ and $n$ are correct. With the
normalized neuron norm $\|v\|_{2,n}=\|v\|_2/\sqrt n$, the rank-one
operator is $b\otimes u=bu^\top/n$, and its Hilbert–Schmidt norm is
the ordinary Frobenius norm. The readout and middle kernel blocks are

$$
K_{\mathrm R}=H^\top H/n,\qquad
K_{\mathrm W}=(U^\top U/n)\odot(b^\top b/n).
$$

The full residual dynamics are
$\dot r=-(2/m)Kr$, where $K\succeq K_{\mathrm R}+K_{\mathrm W}$.
The metric in (24) has squared speed $-\dot{\mathcal L}$.
No rate or normalization correction is needed.

Sign absorption is an exact identity of losses as functions of all
parameters. For the active-only reference, retaining denominator $m$
means
$\bar\theta(t)=\theta_{\text{usual }k\text{-sample}}(kt/m)$.
Its scalar feature clock consequently satisfies

$$
\dot s(t)=\frac{2k}{m}(a-g(s(t))).
$$

This agrees with
$(2/m)\int_0^t\sum_{i\le k}|\bar r_i(v)|\,dv=s(t)$ at the
population level. In particular, the bounded-clock argument does not
lose a factor $m/k$.

Global existence at every finite width follows without an assumption:
loss dissipation bounds $\|r\|_2$, which bounds $\|w\|_\infty$ linearly
in time, $\|W-W(0)\|_F$ quadratically, and the normalized first-layer
velocity on every finite interval. These bounds preclude finite-time
escape of the smooth finite-dimensional ODE.

## 2. Gaussian conditioning and passive predictions

Let $P$ project onto the active input span and condition on
$\mathcal F_{\mathrm{act}}=\sigma(A(0)P,W(0))$.
The active reference variables, $\bar W$, and $\bar w$ are measurable
with respect to this sigma-field. The frozen unused first-layer
coordinates are independent of it, by orthogonality and Gaussianity.
For each unit passive input $x_b$,
$g=A(0)x_b$ therefore has iid standard normal coordinates conditionally
on $\mathcal F_{\mathrm{act}}$.

The conditional function
$F(g)=n^{-1}\bar w^\top\tanh(\bar W\tanh g)$ is odd, has mean zero,
and satisfies

$$
\|\nabla_g F\|_2\le
\frac{\|\bar W\|_{\mathrm{op}}\|\bar w\|_2}{n}.
$$

Gaussian Poincare yields exactly the variance bound (7). On the
initialized operator-norm event, the remaining factors are bounded
deterministically on a fixed time interval. Conditional integration,
Cauchy–Schwarz, and Markov's inequality prove both assertions in (8).
No independence between different passive queries, or between
different times, is being used. Conditioning on the matrix-norm event
does not alter the Gaussian passive roots, since that event is
$\mathcal F_{\mathrm{act}}$-measurable.

The initially audited version described the “entire trained state” as
measurable with respect to $\mathcal F_{\mathrm{act}}$, although the
full matrix $\bar A$ contains the independent frozen block
$A(0)(I-P)$. The corrected frozen version listed above explicitly
restricts the measurability assertion to
$\bar A(t)P,\bar W(t),\bar w(t)$ and separately identifies the frozen
block. That correction was checked and resolves the wording issue;
the conditional proof uses exactly these evolving variables.

## 3. The finite-width comparison really closes

The cancellation
$\zeta'(z)=1/(1-\tanh^2z)$ gives
$\dot\xi_i=-2r_iB_i/m$ on active coordinates. Orthogonality to passive
inputs removes their residuals from this equation. Passive raw
preactivations have no active force. These are exact finite-width
facts, not limiting symmetries.

For the error $E$ in (10), $\psi$ and tanh are globally Lipschitz.
For example,

$$
\|b_a-\bar b_a\|_{2,n}
\le \|w-\bar w\|_{2,n}
  +2\|\bar w\|_\infty\|h_a-\bar h_a\|_{2,n},
$$

and

$$
\|B_a-\bar B_a\|_{2,n}
\le \|W\|_{\mathrm{op}}\|b_a-\bar b_a\|_{2,n}
  +\|W-\bar W\|_F\|\bar b_a\|_{2,n}.
$$

These estimates establish (11), with constants independent of width
on any fixed horizon. All reference and actual residuals are bounded
there by their respective loss identities.

For passive coordinates the entire actual force is bounded by a
constant times $\|r_{\mathrm{pass}}\|_2$, and
$\|r_{\mathrm{pass}}\|_2
\le C_TE+\|\bar f_{\mathrm{pass}}\|_2$ because the passive labels
are zero. There is no term requiring a Lipschitz estimate on
$(1-u^2)B$ when $B$ is merely controlled in normalized $L^2$.
Active, middle, and readout differences then give (13).
Gronwall proves the stated fixed-horizon
$O_{\mathbb P}(n^{-1/2})$ comparison.

This is the decisive distinction from a generic correlated-data
comparison. The candidate does not silently import a population
existence theorem or a backward-tail bound for the full dataset.

## 4. Dependency and endpoint checks

The orthogonal reference limit used here has the hypotheses needed by
the maintained finite Gaussian-program theorem:

- The transformed initial root $\zeta(G)$ has finite second moment
  (indeed every finite moment), although $\zeta'$ is unbounded.
  The theorem permits such roots directly.
- The transformed coordinate maps and clipped readout-gate product
  have bounded first derivatives.
- Learned middle matrices are unrolled into rank-one increments.
  Their actions and adjoints use only the original Gaussian matrix,
  its transpose, and allowed causal scalar contractions.
- The readout clip is inactive on each prescribed horizon. The
  resulting local Lipschitz and Euler bounds are uniform in width on
  the initialized norm event.
- A fixed Euler transcript is taken to its width limit before mesh
  refinement. The common-space construction supplies a bounded
  initialized action and its actual adjoint, not a resampled reverse
  action.

Consequently the deterministic strong reference, its compact-time
convergence, and its finite scalar feature endpoint are available.
The scalar specialization $k=1$ uses the same construction and the
same readout identity; it does not need a contrast argument.

For $k=2$, permutation symmetry makes the active first-feature Gram
diagonal in common and contrast directions. Its contrast eigenvalue
cannot vanish at a finite feature time: on $[0,s_*]$,

$$
\|(\xi_1-\xi_2)'\|_2
\le C\|\xi_1-\xi_2\|_2,
$$

so reverse Gronwall preserves its initially positive norm. Injectivity
of $\psi$ transfers nonvanishing to $u_1-u_2$. If the common
eigenvalue vanished, $u_1=-u_2$ in the first-layer Hilbert space.
The actual bounded linear middle action and oddness of tanh would
then give $h_1=-h_2$ and $g=0$, contradicting $g(s_*)=a$.
For $k=1$, a zero endpoint first feature gives the same contradiction.
Thus the required endpoint first-feature Gram, not just the tangent
kernel, is positive definite.

The passive covariance proof is valid even when the input Gram is
singular. Distinct nonantipodal unit inputs allow a direction with
nonzero pairwise distinct absolute projections. A linear relation
among the corresponding tanh functions, restricted to that direction,
has zero constant term at infinity; its slowest decaying exponential
forces the smallest-scale coefficient to vanish, and induction
removes all coefficients. Continuity and full Gaussian support justify
passing from a zero Gaussian squared norm to this pointwise relation.

At fixed time, conditional on $\mathcal F_{\mathrm{act}}$, the active
coefficients in an active–passive empirical inner product are fixed
and bounded. The passive rows are independent, centered, and bounded,
so the conditional variance is at most $1/n$. This proves the block
diagonal limit (17). Endpoint continuity gives a strictly positive
lower bound valid for every sufficiently late fixed snapshot.

## 5. The passive tangent directions have a quantitative gap

If $U^\top U/n\succeq\lambda I$, Schur positivity gives

$$
K_{\mathrm W}\succeq
\lambda\,\operatorname{diag}(\|b_a\|_{2,n}^2).
$$

This use of the Schur product theorem does not require the input Gram
to be nonsingular. At a late reference snapshot,
$\|\bar w\|_{2,n}\ge a/3$ follows from its mean active prediction.
If $\|\bar w\|_\infty\le S$ and $\|\bar W\|_{\mathrm{op}}\le M$, then
for each sample the fraction of coordinates with
$|(\bar W\bar u_a)_j|>R$ is at most $M^2/R^2$. Their squared readout
mass is consequently at most $S^2M^2/R^2$. Choosing
$R=3\sqrt2\,SM/a$ leaves at least $a^2/18$ readout mass on coordinates
where the squared top gate is at least $\operatorname{sech}^4R$.
This proves (20), including for every passive sample.

The actual residual clock gives the pointwise bound on $w$ and the
Frobenius bound on $W-W(0)$ in (22). The same calculation with the
active-only residuals applies to the reference. For each fixed $T$,
compact-time reference convergence and the passive comparison give
both clocks at most $s_*+o_{\mathbb P}(1)$. Thus the same deterministic
$S=s_*+1$ and $M=10+S^2/2$ are available when choosing a late snapshot.
Only the convergence estimates, not these endpoint constants, may
deteriorate with $T$.

The reference kernel gap transfers to the actual kernel using (11)
and the rank-one difference identity. Together with (22), this gives
a deterministic positive actual snapshot gap with probability tending
to one. No $L^\infty$ conclusion is incorrectly inferred from
normalized $L^2$ closeness.

## 6. Explicit verification of all-future capture

Here is a fully quantitative version of the local continuity step in
Section 7. Suppose at time $T$,

$$
K_{\mathrm R}(T)+K_{\mathrm W}(T)\succeq\kappa I,\qquad
\|w(T)\|_\infty\le S,\qquad \|W(T)\|_{\mathrm{op}}\le M.
$$

For the future residual-clock increment
$v=(2/m)\int_T^t\|r(q)\|_1\,dq$, define

$$
D_W(v)=Sv+v^2/2,\qquad
D_A(v)=\int_0^v(S+q)(M+Sq+q^2/2)\,dq.
$$

The exact velocities give
$\|\Delta w\|_{2,n}\le v$,
$\|\Delta W\|_F\le D_W(v)$, and
$\|\Delta A\|_F/\sqrt n\le D_A(v)$.
Because every input is unit, each sample satisfies

$$
\|\Delta u_a\|_{2,n}\le D_A(v),\qquad
\|\Delta h_a\|_{2,n}\le d_h(v):=D_W(v)+M D_A(v),
$$

$$
\|\Delta b_a\|_{2,n}\le d_b(v):=v+2S d_h(v),\qquad
\|\Delta(b_a\otimes u_a)\|_F\le d_b(v)+S D_A(v).
$$

Set
$d(v)=\{d_h(v)^2+[d_b(v)+S D_A(v)]^2\}^{1/2}$.
The combined tangent feature of one sample has snapshot norm at most
$\sqrt{1+S^2}$. Hence its Gram matrix changes in operator norm by at
most

$$
m\,d(v)\bigl(2\sqrt{1+S^2}+d(v)\bigr).
$$

This bound tends to zero as $v\downarrow0$, uniformly in width.
Choose a deterministic $\eta>0$ making it at most $\kappa/2$ for
$0\le v\le\eta$. Until a possible first clock exit,

$$
\frac{d}{dt}\|r(t)\|_2\le-\frac{\kappa}{m}\|r(t)\|_2,\qquad
v'(t)\le\frac2{\sqrt m}\|r(t)\|_2.
$$

Therefore every pre-exit clock increment is at most
$2\sqrt m\,\|r(T)\|_2/\kappa$. If this is strictly less than $\eta$,
continuity rules out the first exit. The bound holds forever, and

$$
\mathcal L(t)\le \mathcal L(T)
\exp\!\left(-\frac{2\kappa}{m}(t-T)\right)
\quad(t\ge T).
$$

This verifies the finite-width all-future conclusion directly,
including the factors in (26)–(27).

## 7. Order of limits and claim level

One first fixes the endpoint feature margin, the common pointwise and
operator bounds, a smaller transferable kernel gap $\kappa$, and its
capture radius $\eta$. One then chooses a single deterministic time
$T$ so that the limiting active residual is strictly within the
capture threshold and the first-feature Gram is within its endpoint
neighborhood. Finally one sends $n$ to infinity at this fixed $T$.
All required snapshot events then hold with probability tending to
one. The deterministic capture argument applies to every width and
initialization in that event for every later time.

Accordingly, theorem (1) is justified as written. Its arbitrary
amplitude is genuine, but its label geometry remains special. The
proof supplies no quantitative useful width threshold, no result for
arbitrary mixed-sign label ratios, and no open-neighborhood conclusion
without a separate argument.
