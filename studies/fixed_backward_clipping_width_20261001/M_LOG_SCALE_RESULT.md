# Growing smooth caps with exponential constants

2026-10-01. Internally checked theorem; see M_LOG_SCALE_CHECK.md. Not
promoted to the paper or book. This strengthens the
conservative triple-exponential argument in M_SCALE_RESULT.md. It stays
within this study's exact smooth q=1 closure. No dense trained comparison
or independently resampled backward matrix is introduced.

## 1. Statement

Use SMOOTH_SETUP.md: two hidden tanh layers, fixed finite training data,
canonical independent Gaussian read-in and mixer, zero readout and value
memories, normalized q=1 keys, and residual-RMS clock. Both recursive
post-gate backward signals use c_M(s)=M tanh(s/M). Suppose the population
initial readout-feature Gram has a positive gap, and let mu be a query
probability law with bounded support.

There is a positive small-label threshold Y_* independent of M>=1.
Fix one nonzero label vector with RMS Y<Y_*; it stays fixed as n and M
vary. There are C,c>0, independent of M,n,t, such that, for every M>=1
and n>=C exp(CM),

\[
 \left(\mathbb E\left[
  \int\sup_{t\ge0}|f_{n,M}(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)
  \;\middle|\;\mathcal G_n\right]\right)^{1/2}
 \le \frac{C e^{CM}}{\sqrt n},
 \qquad \Pr(\mathcal G_n^c)\le Ce^{-cn}.
 \tag{1}
\]

Constants may depend on the fixed dataset, fixed labels, Gram margin,
and query radius. The event G_n is the original initialized fitting
event and does not depend on M. The population is the smooth closure's
own population at the same cap M. For each fixed delta in (0,1), (1)
implies the unconditional probability bound

\[
 \Pr\left\{
  \left(\int\sup_{t\ge0}|f_{n,M}-f_{\infty,M}|^2d\mu\right)^{1/2}
  >\frac{Ce^{CM}}{\sqrt{\delta n}}
 \right\}\le\delta+Ce^{-cn}.
 \tag{2}
\]

The bound includes finite-width mean bias and the entire training
trajectory, including fitted endpoints. It does not assert an
all-initialization all-time second moment, or a simultaneous supremum
over M inside the probability or expectation.

For any fixed 0<alpha<1, the deterministic schedule

\[
 M(n)=[\log(e+n)]^\alpha
 \tag{3}
\]

eventually satisfies the width requirement and gives conditional RMS
error at most

\[
 C\exp(C[\log(e+n)]^\alpha)n^{-1/2}
       =n^{-1/2+o(1)}.
 \tag{4}
\]

In particular M(n)=sqrt(log(e+n)) is a concrete diverging polylogarithmic
cap. Logarithmic growth with a sufficiently small coefficient also works:
for 0<a<1/(2C), set M(n)=max(1,a log n). Then the width requirement holds
eventually and the conditional RMS error is

\[
 O(n^{-1/2+Ca})\longrightarrow0.
 \tag{5}
\]

No claim that the constant a=1 works follows without further control of C.
An even slower M(n)=max(1,log log(e^e+n)) gives an explicit root-width
bound with a power of log(n) as prefactor.

## 2. Why the former bound had three exponentials

The finite vector and Gaussian cavity estimates have constants exp(CM),
as proved in M_UNIFORM_CAVITY_ROUTE.md. The conservative argument put
every random response kernel in a deterministic container of that size.
Solving the scalar feedback equations throughout that entire container
cost another exponential. Comparing the complete laws by causal Gronwall
cost a third one.

The sharper argument uses the physically relevant integrated response
rows. Rare cavity environments with excessively large rows are discarded
before evaluating their scalar response law. Their contribution is
bounded using the original finite-vector moments. Consequently the
scalar law is evaluated only where the accumulated response is small.
No bound on the maximum response density is needed.

## 3. Common-label deterministic estimates

The cap-independent fitting proof uses |c_M(s)|<=|s| and gives

\[
 \rho(t)\le Ye^{-\lambda t},\qquad
 S(t)=\int_0^t\rho\le S_0=Y/\lambda,
 \quad \|w\|_\infty\le2S(t),\quad
 \|v_a\|_\infty\le C S(t)^2,\quad \|k_a\|_\infty\le1.
 \tag{6}
\]

Choose Y_* so that this activity bound also satisfies the common
population-law smallness conditions below. These conditions do not
involve M. The exact hidden-motion residual coefficients have values
O(S_0^2), even though their Lipschitz constants grow like 1+M.

M_CAP_SCHEDULE_ROUTE.md retains that distinction in the state/residual
comparison. Integrating the damped residual difference first, followed
by activity Gronwall, gives centered all-time concentration, scalar
freezing, and autonomous-feedback restoration with factors at most
poly(M) exp(CM). Polynomial factors are absorbed into exp(CM) for M>=1.
No residual norm or ratio r/rho is differentiated in a higher variation.

## 4. Strong law-data fluctuations

Freeze the scalar histories at the actual finite-width conditional means,
as in the existing smooth proof. All cavity systems thereafter have
deterministic supplied coefficients. Work in their deterministic activity
coordinate s in [0,S], S<=S_0.

Write Q_h and Q_d for the regular response densities of lower h and
upper d, and D for the upper current response atom. Define

\[
 \|Q\|_{\rm row}
 =\sup_{s\le S}\max_a\sum_b\int_0^s|Q_{ab}(s,u)|\,du.
 \tag{7}
\]

The covariance norm is the maximum over samples and both activity times.
The strengthened estimates in M_ROW_CAVITY_ROUTE.md put the time
suprema inside the L2 norm:

\[
 \left\|\|C_n-\mathbb EC_n\|_\infty
       +\|D_n-\mathbb ED_n\|_\infty
       +\|Q_n-\mathbb EQ_n\|_{\rm row}\right\|_{L^2}
 \le \frac{e^{C(1+M)}}{\sqrt n}.
 \tag{8}
\]

The same order holds for full-versus-cavity differences. To prove the
covariance part, express a two-time covariance through its value at
(0,0), the two boundary integrals, and the double integral of its mixed
derivative. That derivative is the empirical product of two feature
velocities at separate times, so it does not differentiate the possibly
measurable coefficient r/rho. Gaussian gradient bounds and Minkowski
control all four terms. For a response row, use the existing supremum
over target time for each fixed source, then integrate the source with
Minkowski. The atom uses its ordinary velocity estimate.

There is a necessary moment step in this argument. The upper signal
velocity contains W_0 q, where q is the lower feature velocity. Operator
norms alone do not control the Gaussian-root derivative of a product
of two such velocities at root width. The direct passive cavity identity
gives each coordinate of W_0 q every required fixed moment, bounded by
exp(CM), before any population-law comparison. Its cavity Gaussian
variance, finite response traces, and Taylor remainder have those bounds.
Coordinate fourth moments then control the squared-carrier terms in the
root gradient of the velocity product. Upper trace target derivatives
contain only one such unbounded diagonal factor, which is estimated
in Frobenius norm. No unproved coordinate maximum bound is used.

All finite-vector derivatives involved have the original Jacobian bound

\[
 \|L(t)\|_{\rm op}\le C\rho(t)(1+M+\|W_0\|_{\rm op}^2).
 \tag{9}
\]

Thus (8) has one exponential in M. The required Gaussian moments have
a minimum-width threshold independent of M. Covariance variances and
mean-square time increments, unlike response densities, have common
cap-independent bounds directly from normalized signal norms.

## 5. A domain based on integrated response rows

M_ROW_DOMAIN_ROUTE.md proves the needed deterministic population
comparison on inputs satisfying common covariance variance/increment
bounds, a common O(S_0) bound on the upper atom, and

\[
 \|Q_h\|_{\rm row}\le 2B S_0,\qquad
 \|D\|_\infty+\|Q_d\|_{\rm row}\le 2B S_0.
 \tag{10}
\]

Here B is a sufficiently large fixed number, chosen before S_0 is made
small. Input response densities and their target-time Lipschitz constants
may retain their exp(CM) bounds. The domain is used to compare physical
tuples, whose covariance increments are already controlled; it is not
asserted to be invariant in every covariance regularity seminorm.

The lower carrier is a Gaussian history plus the atom, the integrated
response row, and the bounded memory term. Its supremum therefore has
a common Gaussian envelope of size O(S_0). The complete lower gated
map satisfies, for each fixed derivative order,

\[
 |\partial_\alpha^jF_M(\alpha,p)|\le C_j|p|,
 \qquad |\partial_\alpha^a\partial_p^bF_M|\le C_{a,b} (b\ge1).
 \tag{11}
\]

These estimates give conditional Gaussian-averaged total derivative
bounds independent of M. The upper bounds are uniform because |w|<=2S_0.
Use (8) to bound input-law errors in the strong norm, rather than trying
to obtain uniform deterministic entrywise derivative bounds over all
large response densities.

Two consequences are essential. First, the covariance/response map has
uniform small-activity contraction constants in its original scaled
covariance and integrated-row metric. Second, both OUTPUT regular
response ROW MASSES are at most C_0 S_0, with C_0 independent of M and B
once B S_0 is small. An upper output density can still have a narrow
large peak: its direct term includes D(s)Q_h(s,u)D(u). Only its integral
is bounded here, and only its integral is needed.

## 6. Localization and the first-exit argument

Consider the deterministic finite expected response tuple. Its regular
response rows vanish on the initial zero-length interval and are
continuous in the target-time L1 topology. Stop provisionally at the
first prefix where either the lower running row norm or the upper
running row-plus-atom norm reaches B S_0. This stopping
prefix is deterministic because the tuple is an expectation.

Before the stop, (8) and the full-versus-cavity estimate imply that the
random cavity tuple differs from its full deterministic mean by less
than a fixed row-plus-atom margin B S_0, except with probability at most

\[
 \frac{e^{C(1+M)}}n+Ce^{-cn}.
 \tag{12}
\]

Include the fixed cavity operator cutoff. The resulting event is
cavity measurable, so it preserves independence of the removed Gaussian
row or column. On this event the cavity tuple satisfies (10).
On the complement, replace the auxiliary tuple by one fixed safe
population-law input BEFORE solving a scalar response equation.

The removed coordinate's actual output and tagged responses have the
finite-vector L2 moment bounds exp(CM). Cauchy--Schwarz with (12)
therefore bounds the discarded contribution by exp(CM)/sqrt(n).
This step does not evaluate an ill-controlled scalar equation on the
discarded environments. Fixed removed-vector norm exceptions and
operator exceptions retain their exponentially small contributions.

On the retained environments, the upper scalar reinsertion has a common
small feedback factor by (10) and the O(S_0) upper gate derivative. The
lower scalar reinsertion has factor exp(CM), since its atom and response
ROW mass are bounded and its pure preactivation derivative is O(M).
The original row/column Taylor remainders and their directly calculated
tagged variations therefore give complete finite mean-law consistency,
including response rows, with defect

\[
 \eta_{n,M}\le e^{C(1+M)}/\sqrt n.
 \tag{13}
\]

Strong input-law fluctuations and the uniform conditional Gaussian
comparison in Section 5 replace the retained random tuples by the
deterministic finite mean. The rare replacement also changes their
means by at most the order in (13), using finite-vector moments.

Choose B>4C_0, then choose S_0 sufficiently small for the row-domain
estimates. If n>=C exp(CM), increase C so that (13) is smaller than
B S_0/4. The finite mean output rows are then bounded by

\[
 C_0 S_0+\eta_{n,M}<\tfrac12 B S_0.
 \tag{14}
\]

They cannot reach the proposed boundary B S_0. The first exit is therefore
absent, and the common row bounds hold on the entire activity interval.
Only a width threshold has grown with M; the label threshold has not.

## 7. Full population error and all-time restoration

The finite mean tuple now has defect (13) in a domain where uniform
law contraction applies. Compare it with the fixed point in the common
population domain constructed in M_UNIFORM_LAW_ROUTE.md. Absorbing the
fixed contraction factor gives distance exp(CM)/sqrt(n), without an
additional exponential. Qualitative fixed-M common-action finite-program
convergence identifies this fixed point's observables with those of the
own forced closure population, as in the original smooth theorem.

The passive lower feature velocity and its same-mixer forward action
give prediction and key-contraction velocity defects bounded by

\[
 \rho(t)e^{C(1+M)}/\sqrt n.
 \tag{15}
\]

Their proof uses the source/target response atoms already retained in
the original cavity calculation and conditional Gaussian moment bounds.
It does not differentiate an approximate state identity. The true
prediction derivative remains w sech^2(z), without replacing it by d.
For this passive step the target time is fixed: only the past h-history
coordinate is put under a covariance supremum, and regular response
sources are integrated. No two-time velocity covariance supremum or
derivative of the residual ratio is needed. Uniformity of the fixed-target
estimate and the integrable factor rho(t) supply the time-uniform result.

Integrating (15) and restoring residual, clock, and moment feedback
costs only the exp(CM) factor from Section 3. Adding centered fluctuations
proves (1), with a larger common C. Passive query constants are uniform
on the bounded query support. Conditional Markov gives (2).

## 8. Scope and unresolved stronger claims

This is an explicit cap-dependence theorem. It permits diverging
polylogarithmic caps and sufficiently small multiples of log(n), while
preserving vanishing full population error uniformly for all training
time. It does not establish a strict C/sqrt(n) bound with C independent
of a diverging M. The factor exp(CM) is a proof upper bound, not a
lower bound or evidence that the sharper statement is false.

The target at width n is f_infinity,M(n). A quantitative comparison with
one unclipped population would additionally require controlling cap
removal in the autonomous population. No such comparison is asserted.
Nor are M=sqrt(n), arbitrary depth, arbitrary activations, removal of the
fitting small-label assumption, or the exceptional-initialization
all-time second moment proved here.

## 9. Evidence status

Complete new proof inputs are M_ROW_CAVITY_ROUTE.md,
M_ROW_DOMAIN_ROUTE.md, M_UNIFORM_CAVITY_ROUTE.md,
M_UNIFORM_LAW_ROUTE.md, and M_CAP_SCHEDULE_ROUTE.md, together with the
fixed-M smooth proof and its explicitly used same-study dependencies.
The two new routes were developed independently from the supervisor's
specified row-norm strategy and exchanged interface clarifications.
A separate complete combined check in M_LOG_SCALE_CHECK.md passed
(1)--(5), including the finite-width mean bias, common label threshold,
exponential minimum-width requirement, and all-time velocity restoration.
It identified the upper-velocity moment gap and checked the explicit
repair now in M_ROW_CAVITY_ROUTE.md Sections 2a--2c, together with the
fixed-target passive scope and specified-source response qualification.
The coordinator read the complete repaired routes and audit.

The checked pre-status synthesis SHA-256 is
e9196f77dbc0a3d212044f57d8db8d3683c11f2049cd00c1cfae6d752ae30db4.
The audit SHA-256 is
6248394d6d76a0165fe007aec300f89d624c154529dc2c006d6db6b995373dd4.
The audit records every frozen scientific input. Subsequent edits to
this synthesis change only the header and this evidence record.
No other study, experiment, manuscript edit, Git mutation, or promotion
is involved.
