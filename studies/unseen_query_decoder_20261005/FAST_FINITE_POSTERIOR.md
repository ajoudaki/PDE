# Posterior estimates for an actual finite packet source

2026-10-06. Lead-author lemma for the local-precision continuation.
This is not a completed smaller neural decoder. It concerns the finite
scalar channel and prior-block interface under the explicit hypotheses
below. Physical Gaussian-matrix coupling and passive neural moment
representation remain separate obligations.

## 1. Finite source and continuous-noise shadow

Let n independent row packets have finite prior mu, supplied as the
pushforward of a specified fixed-length block of unbiased independent bits
under a deterministic packet map with counted bounded work and workspace.
The entropy and iid-block statements below also hold for arbitrary finite
mu; this stronger sampling interface is needed for the generator claim.
A deterministic finite row program produces P successive tests F_r,
each bounded by B >= 1 on every branch. A test can depend on the earlier
acquired scalar prefix; identical packets and prefixes give identical
finite values. Old fields retain their creation-time arguments.

Fix dyadic 0<h<=eta<=1, a deterministic nearest-grid rule Q_h, and
independent standard Gaussians E_r independent of the packets. The shadow
source acquires

\[
 C_r=Q_h\!\left(\frac1n\sum_i F_r(Z_i;C_{<r})+\eta E_r\right).
 \tag{1}
\]

The actual source substitutes a specified finite sampler Ehat_r in (1),
with the same packets, row algorithm and grid. The shadow Gaussians are
proof variables, not algorithm inputs. Suppose, for 0<alpha<1 and P>=1,

\[
 \Pr\{\max_r\eta|\widehat E_r-E_r|>\zeta\}\le\alpha/2,
 \qquad \zeta=\alpha h/(64P).
 \tag{2}
\]

The checked sampler in FAST_LOCAL_PRECISION_TEST.md supplies such a
coupling with logarithmic precision in P/alpha and eta/h. P=0 is
vacuous. A declared scalar Gaussian cutoff pays for finite word ranges.
No continuity in the finite packet coordinates is assumed.

## 2. Whole-source coupling without conditioning on rare prefixes

Along the shadow source, condition on all packets and earlier scalar
marks. Its next empirical mean is determined and E_r is fresh Gaussian.
The boundary lemma in FAST_LOCAL_PRECISION_TEST.md, (4), gives

\[
 \Pr\{\operatorname{dist}(a+\eta E_r,h(\mathbb Z+1/2))
                           \le2\zeta\}
 \le4\zeta(h^{-1}+\eta^{-1})\le8\zeta/h.
\]

Union over P updates costs alpha/8. Intersect with (2). Inductively the
two scalar prefixes agree: their empirical means then coincide exactly,
and replacing E_r by Ehat_r moves the pre-rounding value by at most zeta,
without changing its rounding cell. Thus the joint laws of packets,
all scalar prefixes, and all deterministically generated row fields
differ in total variation by at most alpha.

Every subsequent algorithm using these objects and independent additional
randomness, or more generally the same conditional postprocessing kernel
in both laws, inherits this whole-law comparison. It holds for
an event involving every coded query simultaneously. No probability of
an individual transcript is used as a denominator.

Posterior conditioning below is only on the acquired scalar prefix, not
on raw noises or a private metric selected from the completed source.
The separately checked finite-tape replay lemma identifies compactly
acquired prefixes with the full source. At query time, private acquisition
objects must influence the answer only through that prefix, as in the
existing response decoder.

## 3. Quantized-channel information and pair constraints

Work first with shadow (1). Conditional on the preceding prefix, each
unrounded channel is a random mean of magnitude at most B plus independent
Gaussian noise of variance eta^2. The Gaussian entropy bound and
deterministic data processing by Q_h imply, by the information chain rule,

\[
 I(Z_{1:n};C_{1:P})\le\frac P2\log(1+B^2/\eta^2).
 \tag{3}
\]

This is a finite packet prior with continuous channel noise. No Gaussian
differential-entropy formula is applied to finite noise Ehat_r.

At growing prefixes, the posterior density of the entire packet array
relative to mu^n is a martingale. Convexity of u log u makes its relative
entropy a nonnegative submartingale; its final expectation is (3).
The first-crossing inequality, relative-entropy subadditivity against a
product prior, and exchangeability therefore imply, outside probability
alpha, at every prefix,

\[
 D(\nu\|\mu)\le\frac{P}{2\alpha n}\log(1+B^2/\eta^2).
 \tag{4}
\]

Here nu is the shadow posterior one-row law at that prefix. For a finite
prior these facts can be checked directly by finite sums: conditional
posterior masses are martingales, convexity is Jensen, and subadditivity
is the entropy chain rule and nonnegative mutual information.

The process E[sum_r E_r^2 | current prefix] is a nonnegative martingale
with initial expectation P. Except on another probability alpha, it
never exceeds P/alpha. For every acquired test r,

\[
 C_r=\frac1n\sum_iF_r(Z_i;C_{<r})+\eta E_r+e_r,
 \qquad |e_r|\le h/2.
\]

Exchangeability and conditional Cauchy--Schwarz then give, simultaneously
for all already acquired tests at all prefixes,

\[
                    |\nu F_r-C_r|\le\eta\sqrt{P/\alpha}+h/2.
 \tag{5}
\]

The test uses its stored creation-time scalar arguments, fixed at the
current prefix. An empirical version follows from sum E_r^2<=P/alpha,
with its separately allocated Markov failure. The common-Gram ridge
budget must include h/2 explicitly.

Probability conclusions based on (4)--(5) transfer to the implemented
finite source by Section 2 at an additional alpha failure. This transfers
the whole event; it does not identify the two conditional posteriors at
every rare scalar value.

## 4. Finite prior blocks require no globally continuous row map

Fix a shadow prefix satisfying (4). For posterior and prior product laws,

\[
 D(\nu^s\|\mu^s)=sD(\nu\|\mu),\qquad
 \|\nu^s-\mu^s\|_{\rm TV}\le\sqrt{sD(\nu\|\mu)/2}.
\]

Consequently the prior-block argument of FAST_UNIFORM_QUERY.md applies
unchanged: Chebyshev under nu uses the supplied posterior moment bound,
the displayed inequality transfers a block to mu, and independent block
medians amplify success. Choose s using the same certified information
bound. This argument needs neither a Gaussian prior nor differentiable
row tests.

The algorithm samples its actual finite mu and executes its same finite
row program exactly. It need not approximate a globally continuous row
function at a newly sampled packet. The fixed-context finite failure
tests can therefore use the existing finite-state generator, with its
actual work, random bits and workspace charged.

This does not grant unit-cost exact transcendental operations. A complete
finite row algorithm must specify deterministic approximate primitive
routines, integer/rational operations and their bit costs. Activation/data
evaluation must use the same fixed finite convention in source generation,
packet replay and prior sampling. Numerical discontinuity is harmless
for this finite-prior lemma but does not prove physical accuracy.

For uniform unseen queries, a physical-reference rounding argument such
as FAST_PHYSICAL_QUERY_GRID.md is a separate requirement. Equations
(3)--(5) alone do not give an all-sphere or all-time guarantee.

## 5. Boundary of the result

The lemma closes finite-noise versus continuous-channel information,
scalar-rounding corrections to posterior pair constraints, and statistical
prior-block estimation with an actual finite packet prior.

A smaller complete decoder still needs one locally precise finite source
coupled to a common physical Gaussian matrix tape in both orientations;
physical scalar-forcing and exact replay for that same schedule; the
passive mean/covariance/common-Gram representation and dense-center
transfer for that law; and a full numerical/resource ledger.

Even if those interfaces close, the statistical block s still has width
scale up to explicit logarithmic factors. This route does not prove
logarithmic query sampling or an impossibility theorem for other decoders.

The lead used the complete current FAST_LOCAL_PRECISION_TEST.md,
its complete scoped check, FAST_UNIFORM_QUERY.md, and
RECALIBRATION_FREE_MOMENTS.md, together with the elementary finite-channel
arguments supplied here. Required research/proof/canonical-notation
instructions remain current. This is author work pending separate
reconstruction, not an upgrade of the checked headline bounds.
