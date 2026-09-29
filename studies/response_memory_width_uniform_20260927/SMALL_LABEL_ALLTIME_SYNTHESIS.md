# Small labels: all-time comparison and the remaining finite-width rate

28 September 2026. Continuation of the same investigation. The target is the
unchanged autonomous old-clock closure, at arbitrary fixed depth and finite
correlated data, compared with dense canonical tanh gradient flow from the same
Gaussian arrays. The desired bound is C/P in normalized parameter distance,
simultaneously uniform in elapsed time and finite width, for fixed sufficiently
small labels. A width-first limit or a label size vanishing with width is not
substituted for this target.

**Current status:** the full arbitrary-data, arbitrary-fixed-depth endpoint
rate remains open. The new general proof removes physical time from the
feedback estimate, and the restricted one-input result is treated separately.
No paper or book theorem has been changed.

## 1. General deterministic all-time comparison

Use the sum of first-layer row RMS, hidden-matrix Frobenius norms, and readout
RMS to measure parameter discrepancy, denoted d(t). Work on the initialization
event in LOSS_DECAY_SYNTHESIS.md, with initial readout RMS at most Y, initial
readout Gram at least lambda_0 I, and initialized hidden operator norms at most
K. Depth, inputs, lambda_0 and K are fixed. Take 0<Y<=Y_* sufficiently small.

The full derivation in [SMALL_LABEL_ENERGY.md](SMALL_LABEL_ENERGY.md) establishes

\[
 \int_0^\infty \rho_D(t)\,dt\le 2Y/\lambda_0,\qquad
 \rho_D(t)\le2Y e^{-\lambda_0t},
 \qquad
 \int_0^\infty\|E_P(t)\|_{\rm sum}\,dt
 \le \varepsilon_P:=\frac{C Y^3}{\sqrt{P(P+1)}}.
 \tag{1}
\]

Both dense and closure readout Grams stay at least lambda_0 I/2, and both
physical paths converge. All constants in (1) are independent of n,P,t.

Subtracting residual equations gives, exactly,

\[
 \dot q=-2\widehat\Gamma q
       -2(\widehat\Gamma-\Gamma_D)r_D+\widehat J E_P,
 \qquad q=\widehat f-f_D.
 \tag{2}
\]

The positive Gram damps q. Integrating its norm inequality and substituting
into the parameter difference equations yields the actual-path estimate

\[
 d(t)\le C_0\varepsilon_P+
       C_1\int_0^t\rho_D(u)\,[d(u)+G_P(u)]\,du.
 \tag{3}
\]

Here G_P is the sum, over layers and with a maximum over the finite samples,
of

\[
 \left\|
 [\tanh'(\widehat z_{\ell,a})-\tanh'(z_{\ell,a,D})]\,
 k_{\ell,a,D}
 \right\|_{\rm RMS},
 \quad
 k_{\ell,a,D}=W_{0,\ell+1}^{\top}\delta_{\ell+1,a,D}
 \quad(\ell<L),
 \tag{4}
\]

and k_(L,a,D)=w_0. The dense learned part of every carrier has a bounded
coordinate norm directly from its exact history integral. Equation (4)
contains only the initialized part. Zero readout removes the top term, not
the lower-layer terms.

Gronwall applied in the finite measure rho_D(u)du gives

\[
 \sup_{t\ge0}d(t)
 \le C\left[\varepsilon_P+
              \int_0^\infty\rho_D(u)G_P(u)\,du\right]e^{CY}.
 \tag{5}
\]

This is stronger than a physical-time Lipschitz estimate: no T or unbounded
physical-time integral remains. It isolates a concrete spatial correlation
estimate on the actual paths instead of assuming a flow stability constant.

The elementary bound on (4) gives G_P<=C sqrt(n)Y d and therefore proves

\[
 \sup_{t\ge0}d(t)
 \le \frac{C Y^3}{\sqrt{P(P+1)}}
             e^{CY+C\sqrt n\,Y^2}.
 \tag{6}
\]

For fixed nonzero Y this bound is not width-uniform. It is not evidence
that the actual error grows with width. Neither Gaussian initialization nor
the activity estimate presently proves the sufficient replacement

\[
 \int_0^t\rho_D G_P
 \le a\int_0^t\rho_D d+b\varepsilon_P
 \tag{7}
\]

with a,b independent of width and order. Proving (7), or an alternative
estimate exploiting the actual structured memory error, would complete the
general requested rate.

## 2. A deterministic tail-transfer lemma

There is a separate deduction which upgrades compact-time convergence to
all-time convergence without a new feedback estimate. This deduction does
not preserve an unspecified compact-time rate.

On the common activity cap, let V bound ||F(theta)||_sum/rho along both
paths; let b bound the hidden-block prediction differential, so
||J E||_RMS<=b||E||_sum. These constants are independent of n,P,t.
For t>=T, the closure residual inequality gives

\[
 \lambda_0\int_T^t\widehat\rho(u)\,du
 \le\widehat\rho(T)+b\int_T^t\|E_P(u)\|_{\rm sum}\,du
 \le\widehat\rho(T)+b\varepsilon_P.
 \tag{8}
\]

The dense inequality gives integral_T^infinity rho_D<=rho_D(T)/lambda_0.
Consequently the total parameter motion after T is bounded by

\[
 \int_T^\infty\|\dot{\widehat\theta}\|_{\rm sum}
 \le \frac{V}{\lambda_0}
           [\widehat\rho(T)+b\varepsilon_P]+\varepsilon_P,
 \qquad
 \int_T^\infty\|\dot\theta_D\|_{\rm sum}
 \le \frac{V}{\lambda_0}\rho_D(T).
 \tag{9}
\]

Forward subtraction on the common initialized/learned operator and readout
bounds gives a constant L_f with
||f(theta)-f(vartheta)||_RMS<=L_f d(theta,vartheta).
In particular rho_hat(T)<=rho_D(T)+L_f d(T). The triangle inequality at
time T and (9) therefore prove

\[
 \sup_{t\ge0}d(t)
 \le A\sup_{0\le t\le T}d(t)
             +B Y e^{-\lambda_0T}+D\varepsilon_P,
 \tag{10}
\]

where, for example, A=1+VL_f/lambda_0, B=4V/lambda_0, and
D=1+Vb/lambda_0 work. Every constant is independent of n,P,T.
This also bounds discrepancies between the final fitted parameters.

**Qualitative consequence.** Suppose the established compact-time convergence
theorem is applicable on every prescribed finite interval, with its stated
dense population regularity. Let G_n be the common small-label initialization
event. The precise compact-time premise is equation (5) of
GENERAL_AUTONOMOUS_SYNTHESIS.md: for every finite T and eta>0,
lim_(P_0->infinity) sup_n Pr{sup_(P>=P_0) sup_(t<=T)d_(n,P)(t)>eta}=0.
Its restriction to G_n suffices. Then

\[
 \lim_{P_0\to\infty}\sup_n
  \Pr\!\left\{G_n\ \cap\
       \left[\sup_{P\ge P_0}\sup_{t\ge0}d_{n,P}(t)>\epsilon\right]\right\}
 =0
 \qquad(\epsilon>0).
 \tag{11}
\]

To prove it, first choose one finite T with the exponential term in (10)
less than epsilon/3. Next choose P_0 so that the last term is less than
epsilon/3. The remaining event is contained in the compact-time error event
with tolerance epsilon/(3A), simultaneously over all widths and orders.
Apply that theorem and let P_0 grow. No exchange of infinite-time and width
limits was used. For widths at which G_n is impossible, its intersection
in (11) is empty; no initial full Gram gap for n<m is asserted.

The scope of (11) includes arbitrary joint width/order sequences on these
initialization events, but it supplies no numerical relation P>=C/epsilon.
Choosing T proportional to log P in (10) without controlling the dependence
of the compact-time error constant on T would not prove such a relation.

## 3. What the new results do and do not settle

The width-independent all-time activity and accumulated defect results remain
valid. Equations (3)--(5) remove the physical horizon from the general feedback
argument. Equation (10) rigorously transfers qualitative tracking to all time
when the compact-time theorem's dense regularity is available on each finite
interval. None of these statements asserts the missing finite-width endpoint
rate (7).

The one-input, two-hidden-layer signed-clock construction in
[SMALL_LABEL_STRUCTURED.md](SMALL_LABEL_STRUCTURED.md) proves the full
width- and time-uniform bound C/[P(P+1)] at zero readout. With canonical
small Gaussian readout its bound is C(P^-2+n^-1 P^-3/2) on common
initialization events, simultaneously for every order. It controls the
original physical parameters at the same physical time and predictions
on bounded test-input sets. No dense residuals or histories are supplied
to the closure. Its scalar residual direction and first-layer coordinate
cancellation must not be silently generalized to correlated multiple
inputs or extra hidden layers.

The Gaussian route [SMALL_LABEL_GAUSSIAN.md](SMALL_LABEL_GAUSSIAN.md)
proves that sufficiently small total activity globalizes the maintained
population source bounds. Stopped deterministic population Euler programs
give the physical Gram gap, then Gaussian reference tails, then a relative
Euler residual remainder and an activity bound excluding exit. This constructs
the global dense population and supplies the dense regularity needed for
the compact-time premise of (11) on every finite interval. After reducing
the label threshold accordingly, (11) therefore holds in the canonical
Gaussian model without an additional trained-tail assumption. Population
carrier tails and fixed-program convergence are different from a uniform
finite-width bound for the correlated product (4). In particular no
quantitative finite-width source theorem is inferred merely from Gaussian
population tails.

## 4. Internal checks and provenance

The coordinator read the complete energy, structured and Gaussian candidates,
and the relevant complete C.1--C.2 arguments in the maintained book. The
energy route independently cross-checked (8)--(11), the complete signed-clock
theorem, and its small-readout extension. Its requested explicit compact-time
quantifiers and original-solution coordinate lift were incorporated; the
nonzero-readout bound was written explicitly rather than inheriting the
zero-readout display. The structured route checked the Gaussian candidate's
Sections 1--4 against C.1--C.2. Its clarifications were incorporated: use one
countable family containing all integer physical horizons, and use a stopped
larger-ball comparison for finite-width transfer on arbitrary fixed T.

These were scoped internal mathematical checks, not fresh promotion reviews.
The separate spectral endpoint discussion in the Gaussian candidate and
weighted-history calculation in the structured candidate are not needed
for (11) or the one-input theorem. The coordinator checked their displayed
derivations, but the cross-route checks certified only the scopes above.

All results in this continuation are study-level analytic work. No training
experiment, repository commit, or maintained manuscript change was made.
