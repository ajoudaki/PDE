# Internal audit of the Gaussian nonorthogonal tanh extension

2026-10-10. This is a reused-context internal mathematical audit, **not an
independent promotion review**. No experiment was run and no proof source was
edited.

## Verdict, frozen inputs, and theorem level

**PASS for the stated open-neighborhood theorem.** I found no substantive
gap in the Gaussian sensitivity, conditional-mean and tail argument,
bounded-feature stability estimate, or finite-width capture transfer.
The proof establishes a genuine nonorthogonal class for the original
tanh/tanh flow; it does not establish the unrestricted full-rank-input,
arbitrary-label theorem.

The complete new input was `GAUSSIAN_NONORTHOGONAL_EXTENSION.md`, SHA256

```text
37a4f9fea1e64c2404c066358a82f2611f733c6496512d6179bef501424f9b11
```

Its complete frozen orthogonal dependency was
`GAUSSIAN_POSITIVE_GEOMETRY.md`, SHA256

```text
d220fba99906085e9770aceb33b939b5d0cfa2bb2bc005909f31fe2449afa574
```

The maintained dependency was `docs/12-three-sample-learning.qmd`,
III.F.1–11, supplied lines 316–1000, previously read completely for the
orthogonal audit. SHA256 of that exact line range is

```text
dfa7caceb02b1acf7c6519ec94b5ce9e2698a97c258e4cb757c5d1b78a764a51
```

These source hashes were verified during this audit. The earlier report
`GAUSSIAN_TANH_ORTHOGONAL_CHECK.md` was available as reused checking context,
not as a substitute mathematical hypothesis. A separate bounded,
prompt-only algebraic subcheck independently confirmed the variational
width factors in (9)–(12).

More precisely, fix the number of inputs \(m\), a positive amplitude
\(a\), and a label sign vector \(\sigma\). There is a deterministic
positive neighborhood radius such that, for every fixed unit-column input
matrix and fixed labels in the stated neighborhood of
\((X^\top X,y)=(I_m,a\sigma)\), canonical Gaussian initialization with
**exactly zero initial readout** has probability tending to one of satisfying

\[
\mathcal L_n(t)\le\mathcal L_n(0)e^{-ct}
\quad\text{for every }t\ge0,
\]

with a positive deterministic rate independent of width. The proof permits
common margins and a common rate after the neighborhood is made small
enough. The stated quantifier is for each fixed geometry and label vector;
the theorem need not be interpreted as one event simultaneously covering an
uncountable family of data sets under an unspecified coupling.

This is actual all-time fitting by the finite-width trained network on
high-probability events, not merely population fitting followed by finite
accuracy at fixed times. The radius need not be numerically useful. Neither
arbitrary correlated Grams nor arbitrary label ratios are covered.

## 1. Exact equations, boundedness, and proof dependencies

Let \(\Gamma=X^\top X\), \(u_a=\tanh(Ax_a)\),
\(h_a=\tanh(Wu_a)\), \(b_a=w\odot(1-h_a^2)\), and
\(B_a=W^\top b_a\). Direct differentiation of the original loss and
mobilities gives

\[
\dot A=-\frac2m\sum_b r_b[(1-u_b^2)\odot B_b]x_b^\top.
\]

Multiplication by \(x_a\), followed by the first tanh derivative, gives
exactly (2); \(\Gamma\) is symmetric, so its displayed index order is
correct. The middle and readout equations (3) have the correct factors of
\(n\) and \(m\). Thus closed feature dynamics do not replace the actual
first-layer optimization.

Zero readout gives \(f(0)=0\), hence loss dissipation implies
\(\|r(t)\|_2\le\|y\|_2\). Set
\(S(t)=2\int_0^t\sqrt{\mathcal L(v)}\,dv\). The exact estimates are

\[
\|w(t)\|_\infty\le S(t),\qquad
\|W(t)-W_0\|_F\le S(t)^2/2.
\]

They imply (4)–(5) on a fixed horizon. The original first-layer velocity
also has a finite bound there, with fixed \(\|X\|_{\mathrm{op}}\).
Consequently finite-dimensional continuation is justified without a
Gaussian tail bound or a population existence assertion for correlated
inputs.

The orthogonal dependency supplies precisely the following ingredients:

- a strong natural-coordinate population ODE and a deterministic Gaussian
  identification for its fixed-time observations;
- compact-time convergence of predictions, loss, and the readout-plus-middle
  tangent kernel, with fixed Euler mesh before the width limit;
- a finite feature-time endpoint \(s_*\), positive endpoint kernel, and a
  positive minimum kernel eigenvalue \(\kappa\) along the compact feature
  path;
- a deterministic local capture theorem for the exact finite-width flow,
  expressed through an initial readout bound, middle operator bound,
  residual size, and readout-plus-middle kernel margin.

The maintained III.F dependency supplies fixed Gaussian programs with
actual reused transposes, deterministic empirical \(W_2\) limits,
singular-query handling, causal scalar feedback, and the common bounded
Gaussian action/adjoint realization used in the orthogonal ODE bridge.
No new theorem about a correlated-input population flow is required.

## 2. Scaled Gaussian sensitivity

The natural-coordinate transformation is used only for the orthogonal
reference. It cancels the first-layer gate and yields (6). Its activation
\(\psi\) is bounded with \(|\psi'|\le1\); thus the size of the fixed
initial natural-coordinate roots does not enter the estimates.

Write \(W_0=Q/\sqrt n\), \(V=W-W_0\), and
\(M=\|W_0\|_{\mathrm{op}}+P^2/2\). For a directional variation in
\(Q\), let \(\eta=\delta\xi\), \(v=\delta w\), and
\(E_V=\delta V\). The important bounds, with unnormalized vector norms,
are

\[
\begin{aligned}
\|\delta H\|_F
&\le M\|\eta\|_F+\sqrt{mn}\|E_V\|_F+F_U,\\
\|\delta b\|_F
&\le\sqrt m\|v\|_2+2P\|\delta H\|_F,\\
\sqrt n\|\delta r\|_2
&\le\sqrt m\|v\|_2+P\|\delta H\|_F,\\
\|\delta B\|_F
&\le F_b+P\sqrt{mn}\|E_V\|_F+M\|\delta b\|_F.
\end{aligned}
\]

In particular the residual variation gains \(n^{-1/2}\); this cancels
the \(\sqrt n\) in the first-layer residual forcing. Differentiating
\(\dot V\) and multiplying its Frobenius norm by \(\sqrt n\) gives
terms controlled by
\(\sqrt n\|\delta r\|_2\), \(\|\delta b\|_F\), and
\(\|\delta U\|_F\), with constants depending only on the fixed horizon,
sample count, and label bound. No width factor remains.

Consequently, for
\(\mathcal R=\|\eta\|_F+\|v\|_2+\sqrt n\|E_V\|_F\), (9) follows
with its quadratic dependence on the initialized operator norm. The
forcing estimates can be written explicitly as

\[
F_U+F_b\le(1+P)\sqrt m\,\|\Delta Q\|_F.
\]

For the single entry \(\Delta Q=e_i e_j^\top\), bounded entries of
\(U\) and \(b\) sharpen this to
\((1+P)\sqrt{m/n}\). These are uniform-in-time bounds. Gronwall
therefore proves both (11) and the essential entrywise estimate (12),
uniformly in conditioned first-layer roots.

There is one harmless wording slip in Section 3.1: the differentiated
readout equation is controlled by \(\sqrt n\|\delta r\|_2\) and
\(\|\delta H\|_F\), not directly by the first and third quantities in
the preceding middle-equation list. Substitution of (7) gives exactly
(9), so the displayed conclusion and all subsequent bounds are unchanged.

## 3. Conditional mean, concentration, and exceptional events

The operator-norm tail (13) is valid: two \(1/4\)-nets have combined
cardinality at most \(9^{2n}\), the bilinear approximation loses at most a
factor two, and for \(x\ge10\),
\(2\log9\le x^2/16\). Integrating this bound verifies the claimed
uniform integrability of \(e^{CL^2}\) for all sufficiently large widths.

The Gaussian integration by parts in (14) is applied only to
\(W_0^\top b\). Each summand derivative is bounded by
\(Ce^{CL^2}/\sqrt n\), so the sum with its outer \(n^{-1/2}\) factor
is uniformly bounded. Gaussian cutoff and dominated convergence are
legitimate for sufficiently large \(n\); small widths are irrelevant to
the limiting theorem.

The learned contribution is retained separately. Integration of the exact
middle-weight equation gives

\[
(V^\top b_a(t))_j
=-\frac2m\int_0^t\sum_c r_c(v)u_{c,j}(v)
                  \langle b_c(v),b_a(t)\rangle_n\,dv.
\]

The bounded factors in this expression give a coordinatewise constant
independent of width, roots, and \(Q\). Thus (15) concerns the full reverse
field, not merely its initialized Gaussian part. No independence between
trained queries and \(W_0\) is assumed.

The concentration proof in Section 3.3 has the correct entropy constant
and Herbst exponent. A scalar coordinate of \(B\) is uniformly Lipschitz
in Euclidean \(Q\)-norm on the convex operator-norm ball by (11).
A same-constant Lipschitz extension exists. The value at \(Q=0\) is indeed
zero: tanh vanishes at zero, and exactly zero readout makes the
\(W_0=0\) reference stationary. Hence the extension has the stated
linear-growth bound.

The correction from the extension to the true coordinate is negligible
both in first moment and in the squared-tail estimate. In particular,

\[
\mathbb E\bigl[B_{a,j}^2\mathbf1_{\{L>10\}}\bigr]
\le P^2n\,\mathbb E\bigl[(L+P^2/2)^2
                         \mathbf1_{\{L>10\}}\bigr]\longrightarrow0.
\]

For the extension, Cauchy--Schwarz and the fourth moment of
\(\|Q\|_F\) leave only a polynomial width factor multiplying an
exponentially small probability. These bounds are uniform in all
conditioned roots, coordinates, samples, and times on the fixed horizon.
The bounded-mean sub-Gaussian tail can therefore be integrated to prove
(17), with constants independent of \(R\) and width. Enlarging its
prefactor covers thresholds below the uniform mean bound.

## 4. Deterministic population tails and uniform-time transfer

For the orthogonal reference, \(B=W^\top b\) is an allowed observation of
the same fixed Gaussian program. In the Euler construction, the initialized
transpose is reused with its true dependence, while learned increments are
finite rank-one sums. On the bounded reference state sets, this observation
is Lipschitz in normalized \(L^2\). The previously verified Euler-to-ODE
bridge therefore transfers its deterministic empirical \(W_2\) limit to
every fixed physical time.

For fixed \(R\), the tail function \((|x|-R)_+\) is 1-Lipschitz, and
\(W_2\) convergence gives convergence of its normalized squared norm.
A subsequence converging almost surely, followed by Fatou, transfers (17)
to the deterministic limiting squared tail norm. This is a valid use of a
nonnegative expectation bound; no unproved uniform integrability of the
trained empirical tail is needed for this direction of the inequality.

Uniform time control is also valid. With \(L\le10\), the reference
equations give width-independent bounds on
\(\|\dot\xi\|_{F,n}\), \(\|\dot U\|_{F,n}\),
\(\|\dot H\|_{F,n}\), \(\|\dot b\|_{F,n}\), and finally
\(\|\dot B\|_{F,n}\). Bounded \(\psi'\), bounded top derivatives, and
the pointwise readout bound are sufficient. A finite grid in time and the
1-Lipschitz tail map then give a uniform tail-norm bound. For every fixed
\(R\), the grid may be chosen fine enough for the small positive
\(R\)-dependent tolerance before width is sent to infinity.

Taking a square root and enlarging the prefactor/shrinking the exponent
with strict slack yields (18). This slack matters because convergence to
an upper bound alone would not justify a high-probability inequality with
exactly the limiting threshold. The candidate explicitly allows this
constant adjustment. No threshold grows with width, and no union bound
over all neurons or continuum of times is being assumed.

## 5. Bounded-feature stability and the exact Gaussian coupling

The forward, upper-backward, and reverse-field differences in (19) follow
from the operator bounds, bounded first and top features, and bounded
readouts. For example, normalized forward differences obey

\[
\|WU-\bar W\bar U\|_{F,n}
\le\sqrt m\|W-\bar W\|_F
       +\|\bar W\|_{\mathrm{op}}\|U-\bar U\|_{F,n}.
\]

The residual difference adds only the label perturbation. The middle and
readout energy estimates therefore have width-independent constants.

The off-diagonal Gram contribution is bounded by \(C\delta\) in the
normalized feature norm. This follows neuronwise from the operator bound
on \(\Gamma-I\), bounded gates, and bounded sample residuals. In the
diagonal part, all differences have ordinary \(L^2\) control except the
displayed gate-difference term multiplied by the reference reverse field.
The polynomial gate \((1-u^2)^2\) is 4-Lipschitz on \([-1,1]\).
Its energy pairing is thus bounded by
\(C\sum_a\langle|u_a-\bar u_a|^2,|\bar B_a|\rangle_n\).

Splitting at \(2R\) gives \(CR E\) on the bounded part. On the tail,
\(|u_a-\bar u_a|\le2\) and
\(|\bar B_a|\mathbf1_{|\bar B_a|>2R}\le2(|\bar B_a|-R)_+\)
give the additive tail term in (20). There is no missing higher moment of
the perturbed trajectory. Gronwall then gives exactly the dependence
\(e^{C_TR}(\delta^2+e^{-c_TR^2})\) in (22).

The initialization coupling has the correct full Gaussian law. It can
also be realized with literally the same initialized first-layer matrix,
if desired: since \(\Gamma\) is positive definite near \(I_m\), put

\[
\bar X=X\Gamma^{-1/2},\qquad Z_0=A_0\bar X.
\]

Then \(\bar X^\top\bar X=I_m\), the entries of \(Z_0\) are iid
standard Gaussian, and
\(A_0X=Z_0\Gamma^{1/2}\). The actual two feature trajectories therefore
have precisely the initial values used in (21), with the same independent
\(W_0\) and zero readout. Components of \(A_0\) outside the respective
input span do not affect the closed sample equations. This supplies an
explicit same-\(A_0\) interpretation of the coupling, not an additional
assumption.

The square-root matrix estimate and the normalized Gaussian law of large
numbers prove (21). Its constants have no ambient-dimension dependence.
Finally, a finite \(R\) can first make
\(e^{C_TR-c_TR^2}\) arbitrarily small; then a fixed positive \(\delta\)
can make the other term small. Only afterward is width increased.
This proves a genuine width-independent neighborhood rather than a
vanishing perturbation scale.

## 6. Capture, rates, and the order of limits

The tangent blocks used here are exactly the normalized readout features
\(h_a\) and middle rank-one features \(b_a\otimes u_a\). Their norms
are uniformly bounded on the horizon. The rank-one difference identity
and (19) therefore control their Gram matrices by \(C_T\sqrt E\).
No first-layer tangent continuity or output-feature-only coercivity is
silently substituted for the readout-plus-middle kernel.

For the finite-width capture theorem, the first-layer displacement bound
contains \(\|X\|_{\mathrm{op}}^2=\|\Gamma\|_{\mathrm{op}}\): one
factor comes from the original \(\dot A\), and the other from conversion
to sample preactivations. Thus (23) is the correct conservative bound
when \(\|\Gamma\|_{\mathrm{op}}\le2\). Every other part of the
capture estimate continues to use bounded tanh derivatives and the same
normalized readout/middle geometry.

Choose a deterministic late reference time with a strict capture margin,
using the positive endpoint kernel. The bounds
\(p=s_*+1\) and \(b=10+p^2/2\) remain fixed as this time is chosen.
Continuity of the integrated residual, not an unproved continuity of a
pointwise readout norm, ensures the perturbed snapshot satisfies these
same bounds. Indeed (19) controls the difference between the two
accumulated residuals on the fixed horizon, and the reference accumulated
residual converges to a number at most \(s_*\).

There is consequently a fixed sufficiently small stability tolerance
which preserves the snapshot residual threshold, kernel lower bound,
and strict capture margin simultaneously. The same tolerance preserves a
positive readout-plus-middle kernel lower bound over the entire earlier
compact interval. Equations (18)–(22), reference compact-time convergence,
the initialized operator event, and the root law of large numbers give
the needed finite intersection of events with probability tending to one.

For clarity, if the earlier kernel is at least \(\kappa/2\), exact loss
dissipation gives rate \(2\kappa/m\). If the snapshot capture uses
kernel parameter \(\lambda\) and retains \(K_{\rm R+W}\succeq
\lambda I_m/4\), the later rate is \(\lambda/m\). Both are positive
and independent of width. Taking the smaller rate and concatenating the
two inequalities gives the stated prefactor \(\mathcal L_n(0)\), not a
larger unspecified constant.

The sequence of choices is therefore: fixed orthogonal endpoint and
strictly capturing finite physical time; fixed approximation tolerance;
fixed tail threshold; fixed geometry/label radius; then large width.
On the resulting finite-width event, the deterministic capture theorem
handles all later times. There is no exchange of width and infinite
training time, no frozen-feature approximation, and no appeal to Gaussian
full support as a substitute for a high-probability estimate.

## Corrections and unresolved scope

No theorem-changing correction is required. The readout-variation wording
in Section 3.1 can be corrected as described above, and explicitly writing
\(\bar X=X\Gamma^{-1/2}\) would clarify the same-initialization coupling.
Neither point changes the proof.

The main-proof PASS supports only the stated open nonorthogonal neighborhood
with labels near a fixed signed common amplitude and exactly zero
readout. Arbitrary full-rank Grams, arbitrary label ratios away from such
neighborhoods, and nonzero initial readout remain outside that frozen
theorem. The separately authorized addendum below checks one restricted
nonzero-readout extension. No promotion approval is implied.

## Separate addendum: vanishing pointwise initial readout

After completing the main audit, the supervisor authorized the complete
separate addendum in `GAUSSIAN_BOUNDARY_RESULT.md`, lines 346–407, headed
“Tiny Gaussian readout: a separate extension of the stated initialization.”
No other part of that synthesis was used. SHA256 of the exact supplied
line range is

```text
9e36069107fae9dab702c645db7744d14101cb9d25502c2c99ebaa40d4b22217
```

**Separate verdict: PASS.** The same neighborhood construction can also
accommodate \(\|w(0)\|_\infty\to0\) in probability, in particular
independent \(w_i(0)\sim N(0,1/n^2)\). This is an extension of the
initialization assumption, not a claim that the frozen main proof already
states it. If common constants are desired, the neighborhood is selected
using the common finite-horizon bounds in this argument; no numerical
radius was fixed by the main theorem.

Write \(p_0=\|w(0)\|_\infty\). Since the top features are bounded,
\(\|f(0)\|_2\le\sqrt m\|w(0)\|_{2,n}\le\sqrt m p_0\).
On the event \(p_0\le1\), which has probability tending to one, initial
residuals are bounded by the deterministic constant
\(\|y\|_2+\sqrt m\). Loss dissipation supplies this same residual bound
on the whole fixed horizon. Thus the common deterministic bounds needed
in (19)–(20) persist after replacing the readout and learned-weight bounds
by

\[
\|w(t)\|_\infty\le p_0+S(t),\qquad
\|W(t)-W_0\|_F\le p_0S(t)+S(t)^2/2.
\]

The orthogonal reference is still initialized with exactly zero readout,
so every conditional-mean and Gaussian-tail estimate in the main proof is
unchanged. The perturbed finite trajectory enters that proof only through
the common finite-horizon bounds and the initial energy difference. Its
extra initial term is
\(\|w(0)\|_{2,n}^2\le p_0^2=o_{\Pr}(1)\). For each already fixed
tail threshold, Gronwall multiplies it by a fixed constant, leaving
\(o_{\Pr}(1)\). No expectation or independence assumption on this term
is required.

The accumulated-residual comparison therefore still gives
\(p_0+S(T)\le s_*+1\) with probability tending to one after the same
strict-margin choices. Furthermore,

\[
p_0S(T)+S(T)^2/2
=\bigl((p_0+S(T))^2-p_0^2\bigr)/2
\le(s_*+1)^2/2.
\]

This verifies the capture operator bound as well as the readout bound.
Kernel continuity over the earlier compact interval and deterministic
capture afterward give the same type of positive width-independent
exponential rate. The prefactor is the actual initial loss
\(\mathcal L_n(0)\), which is random here; the proof does not replace it
by \(\|y\|_2^2/m\).

For the stated Gaussian initialization, a union bound gives, for each
fixed \(u>0\),

\[
\Pr\{p_0>u\}\le2n\exp(-n^2u^2/2)\longrightarrow0.
\]

Thus its variance normalization is exactly the one needed by the
addendum. The abstract vanishing-pointwise-readout argument in fact does
not require readout independence if the hidden initialization retains its
canonical Gaussian marginal law: the finite intersection of
high-probability events is enough. The independently initialized Gaussian
case stated in the addendum is therefore safely covered. Order-one
stored readout variance is not covered by this check.

### Final editorial reconciliation

The complete final addendum in `GAUSSIAN_BOUNDARY_RESULT.md`, now lines
347–410, was reread after the documentation update. Its current slice
SHA256 is

```text
90899b3ad1ae4a1fd10a7c092c2c83dd092369141eeae8680086f2e3df42db60
```

The original audited slice hash above is retained for traceability. The
final wording explicitly permits shrinking the unquantified neighborhood
while retaining the same input and label class, and replaces the pending
status with a link to this separate PASS. The equations and proof argument
are unchanged. This clarification agrees with the common-constant
qualification already recorded in the addendum verdict; the PASS and its
scope are unchanged. No unrelated synthesis passage was read for this
reconciliation.
