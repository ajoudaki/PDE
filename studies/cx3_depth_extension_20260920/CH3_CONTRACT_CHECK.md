# C-X3-H3 author-side assembly and contract check

2026-09-20. **The frozen assembly passes the mathematical integration checks
for the circle label domain [-1,1]. One minor explicit scope repair is needed
for its additional arbitrary bounded finite-label assertion:** the hierarchy
proof states |y|<=1, whereas the master theorem does not restrict finite-data
labels to that interval. Section 6 below gives the exact extension of the
estimates; it changes no architecture, optimizer, normalization or limit order.

This is an internal author-side assembly review, not an independent isolated
review or promotion approval. The checker authored `CH3_LOCAL_PROOF.md` and
previously performed the internal cross-check of `CH3_ACTIVITY_PROOF.md`.
Those relationships are disclosed; this report is not independent evidence
for the local proof.

## 1. Inputs and hashes

Read completely for this task: `CH3_THEOREM.md`, `CH3_HIERARCHY_PROOF.md`
and `CONTRACT.md`. Compared them with the already authored/read frozen
local proof, activity proof and activity check. No other study, implementation,
validation artifact or README was read. Root is handling implementation and
operational evidence. No source proof or master theorem was edited.

Hashes captured before review:

| Frozen input | SHA-256 |
|---|---|
| `CONTRACT.md` | `ab0b818cc82ac709f32f44e26d2760d79c153dad6a631b48e62a12015018ca6b` |
| `CH3_THEOREM.md` | `55c713ff6daa3388204001db8672c99edb619c2e0faae48e827781341c5d68d3` |
| `CH3_HIERARCHY_PROOF.md` | `e7caf06e3b52d68b54a044efa78cfc3ed26efee12a079f0eb9a681d7e66d19c7` |
| `CH3_LOCAL_PROOF.md` | `8d044f2e56c8d5be30a9739cea7aef52aa565b89b21e266061b41db921a4568b` |
| `CH3_ACTIVITY_PROOF.md` | `4858e2d8b3d41eafab3070277799ebcf5441e3f2a0b86491eb162d0e1f2dba23` |
| `CH3_ACTIVITY_CHECK.md` | `83fb719b09491d91359d7e38fe4e1ddab0375d61d63c316c516f98d26626f4b7` |

These identify the reviewed versions. A later assembly amendment is not
silently included in this verdict.

## 2. The open Borel nonlazy family closes the activity gap

The master adds a needed argument beyond the finite-data activity unit.
Its reference law, in normalized coordinates, is

\[
 \mu_0=\tfrac12\delta_{(e_1,+1)}
          +\tfrac12\delta_{((3/5,4/5),-1)}.
\]

This is exactly the original rational ArcLaw with p=1/2 and both parameter
intervals degenerate at zero. Its input correlation is 3/5, strictly between
-1 and 1; its weights are positive and both labels are nonzero. Thus every
hypothesis of the finite-data activity proof is satisfied at every fixed L.
The local theorem and maintained C.1 solution agree on their common interval
by uniqueness. Consequently there is an activity time

\[
 0<t_a\le\min(T_L,T_{act})
\]

for which every layer's reference paired mean-square displacement is positive.
The t^4 expansion supplies this at every sufficiently small positive time,
so further shrinking t_a for the nonaffinity argument is legitimate.

Let

\[
 j_{\ell,\mu}(u)=
   \|H_\ell^\mu(t_a,u)-H_\ell(0,u)\|_2^2,
 \qquad J_\ell(\mu)=\int j_{\ell,\mu}(u)\,d\mu(u,y).
\]

The initialization on the common carrier is independent of the training
law. Since |H|<=1, the norm of each displacement is <=2, and therefore

\[
 \sup_u|j_{\ell,\mu}(u)-j_{\ell,\mu_0}(u)|
 \le4\sup_u\|H_\ell^\mu(t_a,u)-H_\ell^{\mu_0}(t_a,u)\|_2.
\]

The right side tends to zero by the local theorem's uniform-in-input law
continuity. The fixed function j_(ell,mu0) is continuous on the compact
input circle and bounded by four. Thus

\[
 |J_\ell(\mu)-J_\ell(\mu_0)|
 \le\sup_u|j_{\ell,\mu}-j_{\ell,\mu_0}|
      +\left|\int j_{\ell,\mu_0}\,d(\mu-\mu_0)\right|
 \longrightarrow0
\]

under W1 convergence. There are only finitely many layers and each
J_ell(mu0)>0. One common positive W1 radius consequently gives the claimed
lower bounds J_ell(mu)>=J_ell(mu0)/2 for every layer. After any further
reduction of t_a, this radius can be reduced/rechosen by the same argument.
No limit-dependent radius or universal activity for cancellation laws has
been inserted.

The nonatomic assertion is also exact. For a rational epsilon satisfying
0<epsilon<=1/20, use the original ArcLaw with p=1/2 and both parameter
intervals [-epsilon,epsilon]. Couple its two components separately to
the corresponding central atoms. Labels remain identical and
|U(s)-U(0)|<=2|s|, so

\[
 W_1(\mu_\epsilon,\mu_0)
      \le2E|S|=\epsilon,
 \qquad S\sim\mathrm{Unif}[-\epsilon,\epsilon].
\]

Choose a sufficiently small positive rational epsilon below the open
radius. U is injective on this interval and rotation preserves injectivity,
so both components, and hence their mixture, have no atoms. This is a
represented original-family member, not merely an arbitrary Borel law near
the reference. The open family is fixed before width and numerical limits.

The larger original ArcLaw family retains existence and numerical convergence;
the master correctly does not infer strict motion for all its members from
this smaller open-family argument.

## 3. The nonaffinity part of the open-family bridge

For every unit direction u, the initialized first preactivation has variance
one. Inductively, an initialized higher preactivation has variance
q_(ell-1)>0, where

\[
 q_0=1,\qquad
 q_\ell=E\tanh^2(\sqrt{q_{\ell-1}}G)>0.
\]

This marginal law is independent of u: the first Gaussian row is isotropic,
and each initially fresh independent edge has the feature second moment as
its Gaussian variance. The activation is nonconstant and its Gaussian
preactivation has full support, so its initial variance and best-affine-fit
error are positive. With finitely many layers, their minima are positive.

The exact preactivation and activation maps are jointly L2-continuous in
(t,u). Their relevant first, second and cross moments are consequently
continuous. At variance bounded below, the formula

\[
 \operatorname{Var}(\tanh Z)
       -\operatorname{Cov}(Z,\tanh Z)^2/\operatorname{Var}(Z)
\]

is continuous as well. Compactness of the input circle and the identical
strictly positive initial margins give one early reference interval with
uniform positive margins over all u and layers. Uniform raw law continuity
controls Z and H in L2 uniformly over that interval and all inputs, so these
moment margins persist in a sufficiently small W1 neighborhood.

Thus the master does not take an unjustified infimum of arbitrary positive
input-dependent constants. The constant initialization margins, compactness,
and uniform law continuity provide the missing uniformity. Intersecting this
neighborhood with the activity neighborhood in §2 is nonempty and open.

## 4. Hierarchy hypotheses are discharged by the same local target

The hierarchy §5 theorem is conditional on a fixed horizon T, not on its
§6 particular formula for a local time. The local proof discharges each
condition on the master's chosen local interval:

| Hierarchy target premise | Local-proof discharge |
|---|---|
| Strong C1 full-row and readout L2 state, HS increments and derivatives | Raw Euler completion and continuous vector-field passage, local §§4,7 |
| State lies in the initialized generated spaces | Compatible common carrier, Euler invariance, and closedness; local §§3,7 |
| Bounded raw and action norms | The common preliminary ball, local §4; finite d is fixed |
| Bounded readout in L-infinity | Energy identity and the readout equation, local §7: ||c(t)||infinity<=2t for |y|<=1 |
| Uniform individual Gaussian backward tails at every passive input | C.2 depth induction, positive-mass passive extension, and Fatou passage; local §§5,7 |
| Same-law reached-state uniqueness/restart | One-reference estimate against the constructed continuation, local §7 |
| Identification with actual finite GF/GD | Fixed finite-reference proxy comparison, local §8, with the observations in §9 |

The passive-tail distinction matters: the hierarchy's compact-field source
estimate requires all passive directions, not only a finite training list.
The local proof explicitly derives those tails by adding a positive-mass
passive atom, removing its mass at fixed program, and passing the resulting
L2 bounds to the strong limit. No growing-program theorem or tail of a
supremum over inputs is being invoked.

The common carrier may be described by the local dense smooth-cylinder
language or the hierarchy's rational bounded-word language. The hierarchy
proves density through Fourier-cylinder tests and L2 clipping, and both
orientations preserve its completed spaces. This represents the same
initialized generated actions, not a separate finite Gaussian core or an
independently resampled interior population.

The filters Q_(ell,N) are positive contractions and converge strongly to
identity. Both orientations of each initialized compressed action therefore
converge on the compact exact forward/backward field families. The HS
projection of K'_ell converges on its compact derivative curve. These are
the three error-production terms in hierarchy (14). The one-reference
comparison (17) propagates them with one cutoff factor, linearly in R.
Exact target Gaussian tails defeat exp(CRT_L). Thus the master correctly
discharges the conditional order theorem locally without assuming tails
of the projected or numerical trajectories.

No mismatch of horizon definitions is forced by the two author proofs
both using the symbol T_L. One may use the local proof's time directly in
the hierarchy's conditional §5 theorem. Alternatively their positive
minimum is valid. The activity time may be reduced independently for its
fixed dataset; the convergence interval does not shrink with N, width,
sample count or numerical refinement.

## 5. Contract and limit-order audit

The assembly preserves the exact model: all hidden activations are tanh;
there is no bias or depth-dependent amplitude change; stored initialization
and mobilities are those in CONTRACT §2; the population alone starts with
zero readout; the finite random readout is retained by the local proxy.
Rows are full rows, learned middle increments are HS, and every edge has
its own actual adjoint.

Existence admits repeated, parallel and antiparallel inputs and singular
Grams. Strict per-input activity separately retains the nonparallel and
nonzero-label hypotheses. The stronger all-Borel result in each separately
fixed dimension is explicitly identified as a strengthening, and there
is no growing-dimension claim.

The actual-network limit and numerical hierarchy limits remain distinct:

* Actual raw GD has only eta_n->0 locally, with affine **raw parameter**
  interpolation and recomputed fields. Deterministic law and independent
  iid sampling limits have no relative sample/width/step restriction.
* The closure uses a fixed-dimensional Heun computation. Its inner
  precision limit precedes time-step convergence; it does not establish
  the original network's raw-GD theorem.
* Hierarchy (25), master §1.6 and CONTRACT §5 have the identical
  outermost-first order N, epsilon->0, Q, P, input quadrature, h->0,
  precision. Each intermediate target is specified in hierarchy §7.4.
  Exact finite data omit input quadrature. No arbitrary diagonal is claimed.

The exact finite-feature state explicitly contains probability laws; the
numerical state replaces them with complete joint finite mark arrays.
Static intermediate populations remain retained. The actual transposes
and source-population weights are used. The finite arrays, coefficient
matrices, exact working values, data and arithmetic metadata suffice for
own-state restart. Neither initialization transcripts nor target-state
resets are passed to the evolution. Costs distinguish initialization,
retained and temporary storage, evolution, precision and law description.

Whole-input predictions, fixed typed same-layer observations and second
moments, initial/current pair laws, RMS motion and risks match the common
contract. The local finite-dataset path/speed/kernel assertions remain
the actual-network assertions supplied by the local proof. No cross-layer
neuron pairing is introduced by the closure's separate population arrays.

The executable scope is every finitely represented dataset and the original
rational ArcLaw family, with its full fixed endpoints and mixture range.
Arbitrary-real finite data and mathematical all-Borel existence do not
supply numerical evaluation or integration oracles. The hierarchy explicitly
requires finite representations or consistent computable evaluators, and
the master refers to that numerical construction.

At L=2 the maintained interval 1/200 and its original family remain intact.
The new depth-dependent times do not replace that existing theorem.
The master explicitly excludes C-H4 substantial training. Therefore it
does not silently treat local C-H3 completion as complete C-X3 completion
under CONTRACT §6. The reference endpoint and fitting-horizon objectives
remain outside this local theorem.

## 6. Exact minor scope issue: arbitrary finite label bounds

**Affected claim.** Master §1.2 admits a bounded finite label list without
fixing |y|<=1; §1.5 and the contract require the closure for every represented
finite dataset in that domain. The local proof explicitly permits a label
bound Y. The hierarchy, however, begins with |y|<=1 and uses loss_N(0)<=1
throughout (8)–(10) and the inner stability argument. Its literal stated
theorem therefore supplies that part only for unit-bounded labels.

**Severity.** Minor assembly quantifier issue. It is not a counterexample
or a new source-control obstruction. No restriction of the contract is
necessary: the following direct parameter extension proves the advertised
scope, and should be stated in the master assembly or appended author
clarification.

Fix any finite Y>=1 with |y|<=Y. Initial c=0 still gives
loss_N(0)=int y²dmu<=Y². The exact finite-feature and finite-array gradient
identities are unchanged, so

\[
 \mathcal L_N(t)+\int_0^t\|\theta_N'(s)\|_{metric}^2ds
       \le Y^2,
\]
\[
 \|c_N(t)\|_\infty\le2Yt,\qquad
 \|w_N(t)-g\|_2^2+\|c_N(t)\|_2^2
       +\sum_\ell\|M_\ell(t)-D_\ell\|_F^2\le Y^2t,
\]
\[
 \|M_\ell(t)\|_{op},\ \|A_{\ell,N}(t)\|_{op}
                  \le10+Y\sqrt t.
\]

The readout bound uses int|r|dmu<=sqrt(loss_N)<=Y, and the displacement
bound is Cauchy–Schwarz applied to the integrated metric velocity. These
replace hierarchy (9) and the corresponding inner bounds. Fixed-N drift
and Lipschitz constants remain finite and may depend on Y. Global fixed-N
continuation, stability (24), all numerical limits and all observations
then follow with those Y-dependent constants. The outer comparison uses
the local target at its already permitted Y-dependent T_L; its residual
and Gaussian-tail bounds have that same Y dependence. No division by Y,
time rescaling, activation change, or normalization of the data is involved.

With this explicit extension recorded, no mathematical assembly blocker
was found in the reviewed C-H3 clauses. This report does not mark that
amendment as already present in the frozen master hash listed in §1.

## 7. Verdict boundary

The open nonlazy Borel/nonatomic ArcLaw bridge, hierarchy target hypothesis
discharge, compatible fixed intervals, observations, and inherited limit
orders pass this author-side integration check. The only exact issue found
is the minor label-bound statement in §6 above, with its repair derived.

Implementation claims in master §4, actual code/proof agreement, primitive
arithmetic code, algebraic tests, operational runs, restart execution,
timing/memory/conditioning records and their preregistered budget were not
inspected here. They remain the supervisor's separate evidence obligation.
No conclusion about their PASS status, full C-X3 completion, long-horizon
training, or promotion follows from this report.

## 8. 2026-09-20 resolution: bounded-label amendment verified

**Current mathematical assembly disposition: PASS within this report's
author-side scope.** This resolution supersedes the outstanding minor issue
in the opening verdict and §6 for the amended master version identified
below. The original frozen-version finding remains recorded as provenance.

The complete amended `CH3_THEOREM.md` was reread. Its SHA-256 is
`954e13c50f5db87d15927eff296da839963677e7c2859351534d90ecf5f38c77`.
The hierarchy proof remains unchanged at
`e7caf06e3b52d68b54a044efa78cfc3ed26efee12a079f0eb9a681d7e66d19c7`.

Master §2 now explicitly sets Y=max(1,max_a|y_a|), states the Y² energy
bound, readout bound 2Yt, squared metric-displacement bound Y²t, and
canonical coefficient/compressed-action bound 10+Y sqrt(t). It derives
the first two consequences from the unchanged gradient identity and
Cauchy–Schwarz, permits fixed-order continuation/stability constants to
depend on Y, and states that the inner limits and outer comparison use
those constants and the local target's Y-dependent time/tails. The later
order-convergence summary now consistently uses Y sqrt(T).

These are precisely the estimates derived in §6. They supply the missing
bounded-label extension without restricting finite labels to [-1,1],
rescaling time or data, or changing the physical equations. As in the
hierarchy proof, the literal operator constant 10 concerns the canonical
contraction frames; inner approximate mark systems use their convergent
fixed-order D and feature-envelope bounds. The energy and displacement
estimates remain valid for those inner systems independently of frame
contraction.

The other reviewed assembly statements remain unchanged in substance.
No further mathematical integration issue was found in this bounded
amendment check. No implementation, code execution, experiments, operational
evidence, long-horizon claim or promotion gate was rechecked or newly certified.
