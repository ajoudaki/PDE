# Width n versus width 2n: completed endpoint bridge and remaining bias

2026-10-03. Continuation of this study's original dense width-rate question
and the subsequently proved independent-copy concentration theorem.
No other study, experiment, manuscript edit, or Git write is involved.

**Current status: the requested canonical width-doubling near-root theorem
is not proved.** The same-width concentration result does not imply it.
This continuation proves a new all-time comparison at the split-block
endpoint of a width-doubling interpolation, and an exact equivalence
between the requested quantitative doubling result and a near-root
dense-to-population rate, given the already established concentration
and qualitative population convergence. The missing comparison changes
the Gaussian mixing and its matched learning mobility.

## 1. Exact target and scope

Use the canonical dense network and hypotheses stated completely in
GENERAL_SELF_AVERAGING.md: arbitrary fixed hidden depth \(L\), fixed
finite compatible data, no biases, independent first weights of law
\(N(0,1)\), hidden weights of law \(N(0,1/n)\), exactly zero readout,
squared-loss gradient flow with mobilities \((n,1,\ldots,1,n)\),
and sufficiently small fixed label RMS. Activations are \(C^3\)
with globally bounded first three derivatives; values may grow
linearly. The explicit positive initial feature-Gram hypothesis or its
proved sphere-data compatibility criteria remain as in
DEPTH_EXTENSION_RESULT.md. Fixed positive sample weights handle exact
data quotients.

For predictors \(f,g\), write
\[
 \mathcal E_\mu(f,g)
 =\left(\int\sup_{t\in[0,\infty]}|f(t,x)-g(t,x)|^2\,d\mu(x)\right)^{1/2},
 \qquad
 a_n(K)=n^{-1/2}e^{K\sqrt{\log(e+n)}}.
 \tag{1}
\]
The fixed query law has finite second moment. Endpoints are understood
on the fitting events; all probabilistic comparisons below retain
that qualification.

The requested result would be: for independent canonical networks at
widths \(n\) and \(2n\), for every fixed confidence \(1-\delta\),
\[
 \mathcal E_\mu(f_n,f_{2n})
       \le C_{\delta,\mu}a_n(K)
 \tag{2}
\]
with probability at least \(1-\delta\) for every sufficiently large
\(n\). Constants and the fixed small-label threshold must not depend
on width or physical time. No clipping or assumed response contrast
is allowed as an additional theorem hypothesis.

## 2. Why this is a bias question

The checked same-width theorem supplies deterministic finite-width
centers \(c_n(t,x)\) and
\[
 \mathcal E_\mu(f_n,c_n)=O_{\Pr}(a_n(K_0)).
 \tag{3}
\]
The centers are scalar-extension expectations constructed in
GENERAL_SELF_AVERAGING.md. They are not identified with the autonomous
network mean or with the population predictor. An expectation bound
over every initialization is unnecessary in the argument below.

The triangle inequality gives
\[
 \mathcal E_\mu(f_n,f_{2n})
 \le \mathcal E_\mu(f_n,c_n)
      +\mathcal E_\mu(c_n,c_{2n})
      +\mathcal E_\mu(c_{2n},f_{2n}).
 \tag{4}
\]
The first and third terms have the desired near-root rate. The middle
term is a deterministic displacement and does not cancel.
Conversely, if (2) holds, choose confidence levels below \(1/3\)
for each of its event and the two events in (3). Their intersection
has positive probability. On that intersection,
\[
 \mathcal E_\mu(c_n,c_{2n})
 \le C_\mu a_n(K_1),\qquad K_1=\max(K,K_0),
 \tag{5}
\]
after increasing the constant for \(a_{2n}\).
Because the left side is deterministic, (5) then holds for every
sufficiently large \(n\).

Thus the requested probabilistic statement is equivalent, up to the
existing fluctuations and fixed constants, to this deterministic
width-doubling center estimate. No conditioning or Gaussian
differentiation of a good-event indicator is used.

## 3. Quantitative doubling would imply a population rate

The manuscript proves qualitative convergence in the same all-time
query norm to a deterministic dense population predictor \(f_\infty\)
under the retained physical hypotheses. Equation (3), whose right
side tends to zero, therefore also gives
\[
 \mathcal E_\mu(c_n,f_\infty)\longrightarrow0.
 \tag{6}
\]
To verify the deterministic implication, apply the triangle inequality
through \(f_n\); both random distances tend to zero in probability,
whereas the left side is deterministic.

The sequence \(a_n(K)\) is summable under repeated doubling, at its
own scale:
\[
 \sum_{j=0}^\infty a_{2^j n}(K)
 \le C_K a_n(K).
 \tag{7}
\]
Indeed \(e+2^jn\le2^j(e+n)\) and
\(\sqrt{u+v}\le\sqrt u+\sqrt v\), so the ratio of the \(j\)-th term
to \(a_n(K)\) is at most
\[
 2^{-j/2}e^{K\sqrt{j\log2}}.
\]
Its series converges because the negative exponent linear in \(j\)
dominates the positive square-root exponent.

If (5) were proved, finite telescoping followed by (6)--(7) would give
\[
 \mathcal E_\mu(c_n,f_\infty)\le C_\mu a_n(K_1).
 \tag{8}
\]
Combining with (3) yields the actual canonical dense-to-population
rate
\[
 \mathcal E_\mu(f_n,f_\infty)
       =O_{\Pr}(a_n(K_1)).
 \tag{9}
\]
There is no union of infinitely many random events: telescoping is
performed only on deterministic centers, after using one fixed
confidence level to establish (5).

Conversely, (9) at widths \(n\) and \(2n\), a union bound, and the
triangle inequality imply (2). This proves the stated equivalence
of the two near-root targets in the current scope.
It is a conditional mathematical equivalence, not a proof of either
currently open quantitative assertion.

## 4. A completed nonlinear endpoint comparison

Here is a part of the width-doubling construction that can now be
proved using the new same-width result.

Take two independent canonical width-\(n\) initializations. Let
\(f_1,f_2\) denote their usual autonomous training runs.
From the same respective initializations, run two auxiliary blocks
\(\widetilde f_1,\widetilde f_2\) that use the common residual
\[
 R_a(t)=\frac{\widetilde f_1(t,x_a)
                    +\widetilde f_2(t,x_a)}2-y_a.
 \tag{10}
\]
Each block uses its canonical width-\(n\) parameter equations, with
its own features and gradients but with \(R_a\) in place of its
individual residual. Define their averaged output by
\(F_{\mathrm{split}}=(\widetilde f_1+\widetilde f_2)/2\).
These blocks remain nonlinear and all their parameters train.

This is exactly a width-\(2n\) block-diagonal auxiliary network:
first weights and readouts are stacked, cross-block hidden entries
and mobilities are zero, and diagonal hidden entries have variance
\(1/n\) and mobility factor two relative to canonical width \(2n\).
These factors make each block's hidden update coefficient \(1/n\).
The output normalization \(1/(2n)\) averages their two outputs.
It is not the canonical width-\(2n\) dense network.

**Proved endpoint theorem.** Under the same fixed-data, activation,
and sufficiently small-label assumptions, for every fixed confidence,
\[
 \mathcal E_\mu\left(F_{\mathrm{split}},
                         \frac{f_1+f_2}{2}\right)
       \le C_{\delta,\mu}a_n(K_2).
 \tag{11}
\]
Consequently \(F_{\mathrm{split}}\) is also near-root close to
either canonical width-\(n\) prediction, at the same physical time
and including its fitted endpoint.

The complete deterministic and probability proof is in
WIDTH_DOUBLING_BLOCK_ROUTE.md. Its main steps are recorded here to
identify what is proved rather than assumed.
The two good independent initializations give a positive average
initial feature Gram. A direct small-activity bootstrap for the
coupled blocks preserves it, bounds the physical states, and gives
exponential decay of \(R\). No carrier maximum is assumed for those
coupled blocks.

Let \(r_1,r_2\) be the residuals of the independent runs, and set
\(\bar r=(r_1+r_2)/2\), \(d=(r_1-r_2)/2\),
\(e=R-\bar r\). If \(\Gamma_i\) denotes the training tangent
matrix of the independent block and \(\widetilde\Gamma_i\) that
of the coupled block, their exact residual equations give
\[
 \dot e=-2\widetilde{\bar\Gamma}e
         -2(\widetilde{\bar\Gamma}-\bar\Gamma)\bar r
         +(\Gamma_1-\Gamma_2)d,\qquad e(0)=0,
 \tag{12}
\]
with arithmetic means denoted by bars and the usual conjugation by
square roots of sample weights when necessary.

Compare each coupled block with its independent reference using the
reference's proved carrier envelope
\(M_n=CS\sqrt{\log(e+n)}\), where \(S\) is a fixed multiple of
label RMS. Residual damping in (12) and parameter subtraction give
\[
 \sup_t(D_1(t)+D_2(t))
       \le Ce^{CS(1+M_n)}\int_0^\infty\|d(t)\|\,dt.
 \tag{13}
\]
Here \(D_i\) is the normalized physical parameter distance already
used in the same-width theorem. Only the two independent reference
paths need the carrier maximum.

Apply the same-width concentration theorem with the query law
augmented by the finite training inputs. It gives
\(\sup_t\|d(t)\|\le\varepsilon_n=C_\delta a_n(K_0)\)
at fixed confidence. Independently, the two fitting bounds give
\(\|d(t)\|\le CYe^{-\kappa t}\).
For sufficiently large \(n\) with \(\varepsilon_n<CY\),
\[
 \int_0^\infty\|d(t)\|\,dt
 \le {\varepsilon_n\over\kappa}
            \left[1+\log\left({CY\over\varepsilon_n}\right)\right].
 \tag{14}
\]
This follows by integrating the minimum of the two bounds.
The logarithm and the amplification in (13) are absorbed by a fixed
increase of \(K_0\) in \(a_n(K_2)\).
Forward query subtraction has factor \(1+\|x\|/\sqrt d\);
therefore the finite second query moment suffices for (11).
Zero labels give identical zero predictions and are handled separately.

This closes the shared-residual endpoint issue. Simply declaring the
blocks independent under (10) would have been incorrect.

## 5. What remains between the two canonical widths

For \(N=2n\), consider the balanced profile
\[
 c_{ij}^{(\ell)}(s)=
 \begin{cases}
 2(1-s),&i,j\text{ in the same block},\\
 2s,&i,j\text{ in different blocks},
 \end{cases}
 \qquad 0\le s\le\tfrac12.
 \tag{15}
\]
Initialize hidden edges with variance \(c_{ij}^{(\ell)}(s)/N\)
and use the matching hidden mobility \(c_{ij}^{(\ell)}(s)\).
First weights, readout initialization, loss, and residual feedback
remain canonical. At \(s=0\) this is exactly (10); at \(s=1/2\)
it is a canonical width-\(2n\) dense network.

The remaining estimate is the effect of this change in random
mixing and mobility on the trained prediction. The previous
conditional interpolation identity shows why averaged response size
does not suffice: it needs cancellation between the expected responses
of within-block and cross-block edges. Their absolute sum can be
order one even if normalized response traces are bounded.

WIDTH_DOUBLING_PROFILE_ROUTE.md records the exact autonomous
interpolation, the initial-time contrast, and the attempted
finite-neuron surgery. WIDTH_DOUBLING_COUPLING_ROUTE.md checks
alternative duplicating and rotating couplings. These attempts do
not establish the trained near-root signed response contrast,
the needed profile probability/localization estimates, or a
canonical-network counterexample.

The population bias therefore remains an actual open part of the
requested theorem. It is not being added as a new assumption and
then advertised as a solution.

## 6. Claim and check boundaries

The completed outcomes are the exact rate-equivalence argument in
Sections 2--3 and the unconditional fixed-confidence split-endpoint
theorem in Section 4. The latter uses the already internally checked
same-width concentration and carrier results; its full proof and
check are retained in the block-route artifacts.

The requested canonical width-\(n\) versus canonical width-\(2n\)
near-root estimate is still open. No strict-root, population-bias,
large-label, growing-depth, or unconditional all-time expectation
claim is made. No numerical evidence was used.
