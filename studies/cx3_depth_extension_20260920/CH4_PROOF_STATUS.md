# C-X3 substantial-training extension: partial results and unresolved continuation

2026-09-20. Supervisor synthesis of the authorized substantial-training proof
attempt. **The C-H4 branch is not proved, and C-X3 is not complete.** The
contract is unchanged. The local C-H3 package remains separate from the
long-horizon claims considered here.

The results below substantially narrow the missing continuation estimate;
they do not assume it away. No new experiment, numerical training campaign,
maintained-book edit, or promotion was performed.

## 1. The fixed target and what still must be proved

At each separately fixed tanh hidden depth, initially L=3, CONTRACT §4 asks
for a fixed finite fitting horizon and an explicitly described positive
supported neighborhood of the orthogonal, equally weighted opposite-label
reference. Every admitted Borel law must have its actual canonical strong
flow through that horizon, uniqueness/reached restart, loss strictly below
1/4 with transfer slack, early paired movement in every layer, actual finite
GF/raw-GD identification, and convergence of the same autonomous numerical
hierarchy. The finite random readout and both orientations of every Gaussian
edge remain part of the model. Atomic, nonorthogonal and nonatomic supported
laws all belong to the target class.

The current proof gap already appears for the unperturbed three-layer
reference. The local source estimates do not establish its continuation
through a fitting horizon. Even after that is resolved, quantitative source
stability must justify a positive supported-law radius; small raw distance
from the reference does not supply tails for the changed-law trajectory.

## 2. New quantitative fitting result, with its exact premise

[CH4_FITTING_CONSTANTS.md](CH4_FITTING_CONSTANTS.md) proves

    q_0=1,  q_l=E tanh²(sqrt(q_(l-1))G),
    q_l>=1/(1+3l),  m_L=q_L/2>=1/[2(1+3L)].

The lower bound is unconditional. Its short proof uses
tanh²z>=z²/(1+z²), followed by

    E[Z²/(1+Z²)] >= (E Z²)²/E[Z²(1+Z²)]
                   =q/(1+3q),       Z~N(0,q).

The signed feature dynamics satisfy c_s=h, hidden_s=J*c,
h=(H_L(e1)-H_L(e2))/2, and

    b_s=||h||²+||J*c||²,    (||c||)_ss>=0,    b_s>=m_L.

These identities hold on a strong solution; they do not create that solution.
With a uniquely continued symmetric physical reference, the exact clock is
s_t=2(1-b), yielding

    loss_*(t)<=exp(-4m_L t).

Consequently the fully specified physical time

    T_L=2(1+3L)

would give loss_*(T_L)<=e^-4<1/8, **provided continuation through T_L is
proved**. At L=3 this time is 20. It is derived from a fitting estimate,
not from a numerical trajectory. The same document derives strong endpoint
and whole-circle endpoint estimates under the stronger feature-continuation
premise. Neither premise has been discharged in this attempt.

[CH4_FITTING_CHECK.md](CH4_FITTING_CHECK.md) separately checks that complete
conditional theorem at its recorded hash. It passes the stated implication,
not the missing premise or the C-X3 contract.

## 3. Raw bounds are global; tail control is the separate issue

[CH4_REACHED_ESTIMATES.md](CH4_REACHED_ESTIMATES.md), §2, proves that original
raw Euler programs have width/mesh-independent bounds on every fixed physical
horizon. Bounded tanh first bounds c and the residual. The top hidden action
is then bounded from its rank update; descending through the remaining edges
bounds them all, followed by the full row. This triangular induction does
not use source caps or an assumed population solution.

The same calculation applies to actual simultaneous finite-network raw GD.
The prescribed random readout has supremum at most one with probability
tending to one, and is retained in the network. Thus a width-dependent step
condition is unnecessary merely to keep the raw state bounded on a fixed
horizon. Conditional on the requisite source estimate, the fixed-reference
capture argument can retain every eta_n->0.

For signed feature time, both independent reference routes derive polynomial
raw bounds. The geometric route also constructs autonomous, globally defined
cutoff flows and proves a precise sufficient condition for their removal.
Those cutoff flows are auxiliary proofs of existence; they are not substituted
for the contract's optimizer.

## 4. A weaker sufficient source estimate

On the common raw ball, the existing comparison has one cutoff factor:

    e'(t)<=C[(1+R)(e(t)+delta)+tau(t,R)].

Here delta is a mesh/law/projection defect, and tau is the sum of RMS tails
of the unchanged reference backward fields. No power R^(L-1) occurs.

The reached-estimates route proves an exact criterion for this inequality.
For a uniform envelope tau(R), set

    omega(s)=inf_(R>=1) [(1+R)s+tau(R)].

If integral_(0+) ds/omega(s) diverges, vanishing input errors force vanishing
trajectory errors on every fixed finite horizon. In particular **exponential
tails suffice**; Gaussian tails are unnecessary. Finitely many chronological
slabs propagate the actual error from one slab to the next without resets.
The same criterion supports the existing hierarchy comparison and fixed-program
finite-network bridge under their stated hypotheses and ordered limits.

There is a further useful relaxation. In the exact reused Gaussian source
representation, a backward field is a Gaussian innovation plus a sum of
bounded tanh features with deterministic response coefficients. Let
B_resp(t) bound the absolute response row sums across the required edges and
passive inputs. The elementary raw bounds already control innovation
variances and learned-rank contributions. A uniform estimate

    sup_(admitted original Euler programs)
        integral_0^T B_resp(t) dt < infinity

therefore suffices: it gives exponential tails with a time-dependent
prefactor M(t) whose log has a bounded integral. The report proves the
corresponding explicit comparison modulus and the required limit passages.

**That integrated response estimate remains unproved through fitting.**
It is a concrete sufficient next target, weaker than the uniform Gaussian
caps used by the local proof. It is not an additional hypothesis silently
added to the C-X3 contract.

## 5. Why the straightforward extensions do not close

The reports retain complete calculations, rather than inferring impossibility
from the failure to find a proof.

- [CH4_REFERENCE_SOURCES.md](CH4_REFERENCE_SOURCES.md) derives the actual
  two-anchor source equations and an improved first-layer clock estimate.
  Its displayed sufficient uniform-cap system is inconsistent for feature
  horizons S>=1/2. Since b<=s, achieving reference risk <=1/8 requires
  s>=1-1/sqrt(8)>1/2. Thus enlarging those particular absolute caps cannot
  prove fitting. This concerns the estimate, not the actual trajectory.
- The same report gives an actual Gaussian-adjoint example with bounded
  adaptive operand and bounded operator/RMS norms but no uniform cutoff-tail
  bound. It retains the reused response term. It excludes a general
  bounded-source shortcut; it is not a reached-reference counterexample.
- [CH4_REFERENCE_GEOMETRY.md](CH4_REFERENCE_GEOMETRY.md) exhibits arbitrarily
  large positive Hessian directions of the signed feature objective on every
  raw neighborhood of initialization, even inside the reference symmetry
  class. Consequently an ambient one-sided Lipschitz bound in the raw metric,
  or a metric changing only the first-row clocks, cannot justify continuation.
- The reached-estimates report constructs an arbitrarily small HS perturbation
  of the top edge at a source-good state that preserves every active forward
  field and risk but destroys even the fourth moment of an intermediate
  backward field. It demonstrates why raw closeness and fitting observations
  cannot replace a theorem specific to reached dynamics.

The focused second round made two further deductions. The geometry report's
§9 computes the exact cutoff energy defect

    d b(theta_N)/ds = ||G_N||² + <G-G_N,G_N>.

Bounding that defect reintroduces the unproved integrated backward tail.
Its symmetric, arbitrarily small HS example preserves both initialized anchor
forward fields and finite energy quantities while giving a backward RMS-tail
lower bound of order R^-1 (log R)^-1/4. Thus instantaneous signed energy
cannot supply the missing exponential estimate by itself.

The source report's §7 instead retains covariance-weighted signed responses.
The combined top reverse response is exactly R=I^-1 Pi_1 Delta, where I is
the covariance isometry from lower source features to upper Gaussian sources
and Pi_1 is their Gaussian linear projection. This proves ||R(s)||2<=s and
a square-integrable time envelope. The Gaussian reverse innovation has a
subGaussian time envelope, and the learned-rank shift is deterministically
bounded. Only the transferred response envelope lacks adequate tail control
in this decomposition. The isometry I preserves L2 norms, not exponential
moments. Its exact tangent equation leaves correlated terms E[B C3 Y]
from the middle layer's reverse-source response. Neither swap symmetry nor
the bounded direct top derivative closes them. Setting C3=0 gives a valid
easier conditional bound, explicitly excluded as a replacement for the
actual reference. The benign initial response expansion also leaves only
an L2 remainder and hence does not imply a long-horizon tail bound.

The troublesome term at L=3 is explicitly

    [sech²(Z2)-sech²(Z2_bar)] A3* [c sech²(Z3)].

The bounded readout controls the top operand. It does not bound the reused
adjoint field pointwise. A second scalar clock also introduces the lower
feature-motion term divided by sech²(Z2), so the two-layer clock proof does
not extend verbatim.

None of these calculations proves finite-time breakdown or falsity of the
requested depth extension. They exclude specific unjustified implications.

## 6. Route registry and claim ladder

| Route | Concrete gain | Remaining implication | Status |
|---|---|---|---|
| Gaussian source equations and first-row clock | Exact signed responses; cap obstruction; combined-response L2 contraction and time envelope; controlled innovation and learned shift | Adequate tails for the transferred response, or a bound on its correlated middle-layer feedback | Both rounds leave source production open |
| Gradient geometry and autonomous cutoff construction | Polynomial raw bounds; strong left endpoints; exponential-tail removal criterion; symmetry-preserving Hessian obstruction; exact cutoff energy defect | Uniform or integrated adequate tails of the actual cutoff family | Conditional construction; energy-only shortcut fails |
| Chronological/Osgood estimates | Global raw Euler/GD bounds; exact tail criterion; weaker integrated-response condition; conditional capture/hierarchy bridge | Prove the required envelope for actual reference and nearby-law programs | Propagation proved, source production open |
| Supervisor fitting constants | q_L>=1/(1+3L); explicit conditional T_L=2(1+3L) and endpoint estimates | Strong continuation and supported-law source transfer | Initialization bound proved; training conclusions conditional |

The C-H3 result, the initialization bound, and the raw-bound/conditional
comparison lemmas have different claim levels. None upgrades the open
long-horizon construction, fixed positive radius, final risk guarantee,
long-horizon actual-network identification, or closure convergence into a
completed C-H4 theorem.

The source route can be reopened by a new signed or covariance-sensitive
estimate controlling the displayed middle-layer feedback. The geometry route
needs a path-specific tail invariant beyond the instantaneous raw energy.
The propagation route is ready to use either certificate, but does not produce
one. Further increases of the already inconsistent absolute caps, arbitrary
raw-state Picard arguments, or repeated local restarts with fresh Gaussian
sources do not address the remaining obligation.

## 7. Source screening and check boundary

The supervisor read the new route reports completely and checked their
calculations against the permitted maintained C.1–C.2, complete C.4.5.1,
C-H4 D.1–D.3, and the study's local proof. The exact checked revisions and
any amendments are recorded in [CH4_CHECK.md](CH4_CHECK.md). These are
author-side checks, not independent promotion reviews.

A limited primary-source search screened related results but imported no
external theorem. The abstract of Chen et al.'s
[Global Convergence and Rich Feature Learning](https://arxiv.org/abs/2503.09565)
states a conclusion conditional on training convergence; it does not itself
supply the needed continuous-time construction. Yang and Littwin's
[Tensor Programs IVb](https://arxiv.org/abs/2308.01814) describes adaptive
optimizer limits, and Gerbelot et al.'s
[Rigorous dynamical mean field theory](https://arxiv.org/abs/2210.06591)
describes first-order algorithm asymptotics on Gaussian data. Those abstracts
were screened, not their full proofs or heavy dependencies. No claim that
the literature lacks an applicable theorem is made, and no scientific
step here relies on an unverified external theorem.

The decisive remaining work is to prove a reached backward-field/source
estimate through the fixed fitting horizon, then close its supported-law
perturbation argument with a concrete positive radius. Numerical agreement
or a conditional fitting inequality cannot discharge either obligation.
