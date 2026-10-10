# Scoped consistency check of the assembled deep linear argument

Checker: `/root/nth_lower_scalar`, 2026-10-10. This is an internal scoped
consistency check, not an isolated promotion review. The checker authored the
same study's separate scalar route before receiving this assignment.

Scientific inputs read completely for this check:

- `RESULT.md`, SHA256
  `d40c187357f4491a32bb4a8e83d70ded1e11d1df66b716e7c043138df9a36802`;
- `ANALYTIC_ROUTE.md`, SHA256
  `1770611b10f1909c9fcd6540dceafda65bd51e6c97a37845fd2553eca86b1cf4`.

The earlier draft of `RESULT.md` with the weaker coefficient \(1/4\) was
also read, then superseded for this check by the version above. Required
proof, canonical-notation, and research-process instructions were already
current. No external scientific retrieval, established-book reading,
other-study reading, experiment, or numerical reproduction was performed.
The assigned emphasis was Sections 2, 3, and 5, plus the analytic interface
and the added passive-query paragraph.

After the two completion issues below were sent to the supervisor, the
limited amendments in `RESULT.md` were also read and checked at SHA256
`188e68b0f6ca9232ba0d84a17fb0c48e5cec17dcbe3d40dc496c4b8c97ce1969`.
Those amendments add unconditional dense-flow existence and distinguish
declared arrays from the effective even-order moving arrays. The full
read was of the preceding listed version; the follow-up read covered
these changed passages and their surrounding context.

## Findings and remaining limits

No blocking error was found in the normalized-model lower bound, the exact
first unmatched derivative, or the all-time dense-pair estimate. This verdict
is restricted to the model and norm defined in the supplied files. The audit
rederived the substantive estimates below rather than relying on the author's
claimed status.

Two small completion issues were identified in the fully read version
and resolved by the checked amendments:

1. Section 6 calls \(2^q-2\) the moving-coordinate count for every order.
   It is the count of the declared lower-level arrays. When \(q\) is odd,
   the top odd tensor is zero and rank \(q-1\) is also constant, so it is
   not the count of coordinates with nontrivial evolution. Using
   \(q_{\mathrm{eff}}=2\lfloor q/2\rfloor\) gives the nonfrozen array count
   \(2^{q_{\mathrm{eff}}}-2\). The already weakened bounds in Section 1
   and the asymptotic coefficient \(\log 2/2\) remain valid. The wording
   now distinguishes a declared array from actual evolving coordinates.
2. The unconditional definition of \(D_n\) refers to all initialized dense
   trajectories, while Section 5 explicitly proves global existence on its
   good event and neighborhood. This is easily completed without another
   assumption: for every finite initialization, gradient flow gives
   \(d\mathcal L/dt=-\|\dot X\|_H^2\), and hence, before any possible
   finite maximal time,
   
   \[
   \|X\(t\)-X\(0\)\|_H
   \leq\sqrt{t\,\mathcal L\(X(0)\)}.
   \]
   
   This prevents finite-time escape for the polynomial vector field.
   It also gives \(\|f(t)-y\|_2\leq\eta\), so the dense-pair sphere
   discrepancy is finite for all initializations in this linear model.
   The amended file now supplies this energy argument, closing the
   existence point. Fitted-limit claims remain explicitly on the good
   event, as required by the proof.

The claimed identification with the maintained chapter, its activation
constant \(\beta=10\), its small-label condition, and the external paper's
equation numbering were outside the assigned scientific inputs. Their
verification is therefore not supplied by this report. The supervisor
reported separately checking the chapter normalization and small-label
condition; that report is not substituted for independent source inspection
here. This limitation does not affect the self-contained normalized theorem.

The Gaussian good set is nonempty for \(n\geq2\). The asymptotic conclusion
uses this range. At \(n=1\), its two-column singular-value condition is
impossible; an exponential probability lower bound can only be vacuous
there. The final amendment explicitly imposes \(n\geq2\), removing this
harmless finite-width edge case.

Final amendment verification: RESULT.md at SHA256
8ee19b4517f5e90c31f67cc02f143ba62dc35d2794eca7cde961efbacfa55bb1
was checked specifically for the added \(n\geq2\) scope and the two
previously identified corrections. All three are present and mathematically
consistent. None remains open in that version. This final follow-up was
limited to those amendments; the external-source scope limitation above
is unchanged.

## Metric and initialization checks

For the stated original normalization,

\[
f(x)=\frac1n u^\top W^{(2)}W^{(1)}\frac{x}{\sqrt2},
\]

the substitutions \(B=W^{(1)}/\sqrt n\), \(W=W^{(2)}\),
\(c=u/\sqrt n\) give \(f(x)=c^\top WB(x/\sqrt2)\) exactly.
For either rescaled block, division of its mobility \(n\) by the square
of the coordinate scaling \(\sqrt n\) gives mobility one. Thus the stated
Euclidean gradient and half-MSE loss \(\mathcal L=\frac14\|f-y\|_2^2\)
produce the residual factor \(1/2\) used throughout the proof. This is an
algebraic verification for that original normalization; its match to the
unread maintained convention remains the source-interface limitation above.

The Gaussian initialization event was checked with the following factors:

- A \(1/8\)-net with directional Gram deviations at most \(1/8\) gives
  an operator deviation at most \((1/8)/(1-2/8)=1/6\).
- Conditional on \(B=UR\), the independent matrix \(WU\) has independent
  \(N(0,1/n)\) entries. The two Gram events imply
  \(\sigma_{\min}(WB)\geq\sqrt{5/6}\sqrt{5/6}=5/6\).
- A \(1/4\)-net gives \(\|W\|_{\mathrm{op}}\leq(4/3)\max\|Wv\|\).
  Threshold \(3\) on that net yields the required bound \(4\).
  Its union-bound exponent is
  \((8-\log9)/2-\log9=4-\tfrac32\log9>0\).

There is no growing-order union bound: this one event supplies all orders.

## Exact jet and positive source coefficients

Let \(u_b=(y_b-f_b)/2\) denote the physical driving coefficient, and let
\(e_r=K_r-K_r^{(q)}\), with \(e_1=f-f^{(q)}\). For \(r<q\), the exact error
equation is

\[
\dot e_{r,a_1\ldots a_r}
=\sum_b u_b e_{r+1,a_1\ldots a_r b}
-\frac12\sum_b e_{1,b}K^{(q)}_{r+1,a_1\ldots a_r b}.
\]

For even \(q\), reflection of the readout makes \(K_{q+1}(0)=0\).
Therefore \(e_q(0)=\dot e_q(0)=0\), while

\[
e_q''(0)=\left(\frac\eta2\right)^2
                         K_{q+2}(\,cdot\,,1,1)(0).
\]

Induction on derivative order in the displayed error equations shows
\(e_r^{(k)}(0)=0\) for \(k<q-r+2\). In particular, the feedback term
containing \(e_1\) cannot enter the first discrepancy. At the first nonzero
derivative at each lower rank, only the undifferentiated coefficient
\(u_1(0)=\eta/2\) contributes; \(u_2(0)=0\). The relevant Leibniz coefficient
is one. After \(q-1\) downward steps this gives exactly

\[
(f_1-f^{(q)}_1)^{(q+1)}(0)
=\left(\frac\eta2\right)^{q+1}K_{q+2}(1,\ldots,1)(0).
\]

This calculation checks the closure's own residual feedback rather than
replacing it by the dense residual.

For the source ascent, orthogonal changes of the two hidden coordinates
preserve the Frobenius metric and the prediction. If
\(W_0=Q\Sigma P^\top\), transform \(a\\) by \(P^\top\), \(c\\) by
\(Q^\top\), and \(W\\) by \(Q^\top WP\). A diagonal sign matrix applied
in both hidden spaces then makes \(a_0\\) nonnegative and leaves the
nonnegative diagonal \(\Sigma\) unchanged. The other column of \(B\)
does not enter this source flow.

The three source equations have nonnegative polynomial Taylor recurrences
in these coordinates. Suppressing \(W'=ca^\top\) removes only nonnegative
coefficients. The frozen-\(W\) output is

\[
\frac12a_0^\top\sqrt M\sinh(2s\sqrt M)a_0,
\qquad M=W_0^\top W_0.
\]

Its odd derivative of order \(j\) is
\(2^{j-1}a_0^\top M^{(j+1)/2}a_0\). The good event gives
\(\|a_0\|^2\geq1/2\) and
\(a_0^\top Ma_0/\|a_0\|^2\geq1/4\). Convexity of the spectral moment
therefore yields the lower bound

\[
2^{j-1}\frac12\,4^{-(j+1)/2}=\frac18.
\]

Thus the source bound and every scaling factor in the first unmatched jet
agree with the assembled statement. Odd closure orders reduce exactly to
the preceding even order.

## Uniform analytic interface

The complete supplied analytic route was read. Its ordered-integral
convention differentiates the latest-time outer index first, matching
the hierarchy's appended-index convention. Its fixed-point map uses the
closure's own residual. The norm is an operator/vector block norm, so the
large Frobenius norm of \(W_0\) introduces no width factor.

The factorial bound on ordered derivatives, the simplex factor \(1/k!\),
and the contraction on radius \(1/4096\) give a common prediction disk.
The smaller closed radius \(R=1/8192\) has the analytic neighborhood
required by the scalar coefficient argument. The source lower bound
\(\frac18(\eta/2)^j\) implies \((\eta/16)^j\) for every \(j\geq1\),
so the interfaces match.

The strengthened endpoint estimate retains \(j!\) in its denominator.
With \(a=\eta/16\), \(M=2\), and \(R=1/8192\), its scalar constant is
\(aR/8=\eta/2^{20}\). The supplied tail comparison then gives exactly
the explicit bound \(1a\) in the assembled text, and its leading logarithmic
term is \(-j\log j\). Accordingly the necessary coefficient \(1/2\),
replacing the earlier \(1/4\), follows from the available analytic result.
It is a real-interval supremum estimate, not a claim of a gap at every
fixed positive time.

## Global sensitivity and the probability argument

The inspected revision explicitly keeps the readout zero for every
perturbed initialization. This is necessary for the common initial
residual \(r(0)=(-\eta,0)\) and \(\delta f(0)=0\).

An initialization at distance at most \(1/100\) from the good set,
followed by a trajectory inside its own radius-\(1/100\) ball, is at total
distance at most \(2/100\) from a good point. The displayed product-change
bound is less than \(1/4\), preserving \(\sigma_{\min}(WB)>1/2\).
The bounds \(\|J\|\leq100\) and \(\|DJ\|\leq50\) are conservative:
the direct estimates are \(25\sqrt6\) and \(30\sqrt2\), respectively.
The kernel gap consequently gives residual decay \(e^{-t/8}\), and the
integrated parameter speed is \(400\eta<1/100\). This closes the
neighborhood by a first-exit argument.

For a hidden-initialization variation \(Z\), the negative Gram term in
the linearized parameter flow contributes no growth. The remaining term
gives \(\|Z(t)\|\leq e^{200\eta}\|Z(0)\|\leq2\|Z(0)\|\).
Then

\[
\|\delta K\|
\leq2\|J\|\|DJ[Z]\|
\leq20000\|Z(0)\|.
\]

The evolution operator of \(-K(t)/2\) has norm at most
\(e^{-(t-s)/8}\): this follows from differentiating the squared norm
of a solution, and does not require that matrices at different times
commute. Convolving the forcing with residual decay gives precisely
\(10000\eta t e^{-t/8}\|Z(0)\|\). Substitution back into the output
equation gives a velocity bound no larger than
\((5\cdot10^7t+10^4)\eta e^{-t/8}\|Z(0)\|\), within the stated
\(10^8\eta(1+t)e^{-t/8}\|Z(0)\|\).

The nonconvexity of the good set is handled correctly. For two good
initializations within distance \(1/100\), their connecting line consists
of zero-readout initializations in the proved neighborhood, so the local
derivative bound integrates along it. For more distant pairs, division
by their distance gives at most \(200\eta e^{-t/8}\) for predictions
and \(10^6\eta e^{-t/8}\) for velocities. These fit the envelopes in
\(12\). Standard Gaussian coordinates rescale these constants by
\(1/\sqrt n\), not \(1/n\).

The Lipschitz-extension step does not assert a derivative relation off
the good set. None is needed: on the good pair event both extensions
equal the actual predictions and actual velocities. A single countable
dense subset of the good set makes each infimum extension jointly
measurable in time and Gaussian coordinates. The same deterministic
extension is applied to the independent Gaussian pair, so its pairwise
second moment is twice its variance. Dropping the good-pair indicator
only enlarges the relevant nonnegative integrand.

For the genuine good trajectories, \(g(0)=0\) gives

\[
\sup_{t\geq0}\|g(t)\|^2
\leq\int_0^\infty(\|g(t)\|^2+\|\dot g(t)\|^2)\,dt.
\]

The extensions need not satisfy this inequality; the proof applies it
before passing to extensions. Gaussian variance and Tonelli then yield
the factor \(4/n\) in \(14\): two output components, each with pairwise
second moment at most \(2L(t)^2/n\).
Finally,

\[
4\cdot164\,(10^8+10^{16})\eta^2
=6.5600000656\cdot10^{18}\eta^2
<7\cdot10^{18}\eta^2.
\]

This verifies the stated constant and its independence of width. There
is no hidden union bound over all times or exchange of the width and
time limits. Markov's inequality plus the bad-set probability establishes
the all-time \(O_{\mathbb P}(n^{-1/2})\) conclusion.

## Passive queries and exact claim scope

For \(v_\pm=(e_1\pm e_2)/\sqrt2\), the dense model is linear in \(v\).
The initialized hierarchy is linear in its first, queried input, and
the passive hierarchy evolution preserves that dependence because all
driving indices and residuals are training indices. Its predictions can
therefore be reconstructed from the two training predictions at every
time on which the closure exists. If their errors are \(d_1,d_2\), the
query errors are \((d_1+d_2)/\sqrt2\) and \((d_1-d_2)/\sqrt2\).
Their maximum is at least \(|d_1|/\sqrt2\), by the triangle inequality.
The two query inputs are fixed before initialization and use no query
labels. The dense-pair error on this panel is bounded by the sphere error,
so the same necessary-order conclusion follows.

The result remains a specified-closure lower bound for a deep linear,
orthogonal-data witness. It does not supply a universal state-dimension
lower bound, a statement for every nonlinear activation, or a matching
sufficient order. Those exclusions are correctly maintained in the
inspected assembly.
