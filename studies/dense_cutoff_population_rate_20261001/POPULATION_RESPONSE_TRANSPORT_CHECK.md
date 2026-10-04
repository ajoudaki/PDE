# Internal reconstruction of population response transport

2026-10-03. Bounded internal check of POPULATION_RESPONSE_TRANSPORT.md
at frozen SHA-256
a339eace94acdc797daade3bcc8f58a8c730f720dbb2d9e06c29cba6da3b925c.
The candidate was read completely. The current manuscript's complete
population-construction proof had been read previously; its fixed-program,
completion and strong-flow passages were reread for this check.
No other study, numerical experiment or external scientific source was used.

**Verdict: PASS in the stated common-population scope.** The fixed-space
adjoint formula, causal construction of both orientations, identification
\(W_0=I+J^*\), and defect-stability estimate check under the manuscript's
fixed-program construction. No mathematical correction was required.
The result compares objects already realized on one compatible population
environment. It does not construct that realization for finite trained
neurons, prove a quantitative finite-program coupling, or establish any
dense-to-population width rate.

This checker authored the preceding local internal checks and negative
search, but not the transport candidate. This is collaborative internal
validation, not a promotion review.

## 1. Claim boundary and types

For one initialized hidden matrix, let
\[
 H_-=L^2(\Omega_-),\qquad H_+=L^2(\Omega_+)
\]
be its lower and upper generated population spaces. Their inner products
are the expectations on the respective layer spaces. The proposed maps
have types
\[
 I:H_-\to H_+,\quad J:H_+\to H_-,\quad
 I^*:H_+\to H_-,\quad J^*:H_-\to H_+.
 \tag{1}
\]
Thus \(I+J^*\) has the forward type and \(I^*+J\) the reverse
type. Neither \(I\) nor \(J\) is asserted to be a surjective
isometry. Independence of their primitive Gaussian source groups is
not an assertion that two random operators on pre-existing circular
domains have been selected independently.

The coupled root tuples must be admissible for the manuscript's joint
fixed-program theorem: each layer's two worlds may be coupled in its
root tuple, while the required independence across layers and from the
initialized matrices is retained. The construction does not authorize
an arbitrary coupling that violates those hypotheses.

The checked statements are:

| Claim | Check outcome |
|---|---|
| Response equals the adjoint of an isonormal map | Exact, including singular queried Grams |
| Common causal construction preserves each program's marginal | Checks under the joint finite-program theorem |
| Future-source independence needed for the adjoint identity | Checks for primitive sources after a finite causal extension |
| Two isometries on the completed generated spaces | Checks by zero-variance consistency and completion |
| \(W_0=I+J^*\), with the true adjoint \(I^*+J\) | Checks on a dense span, then on all of the completed spaces |
| Population parameter-defect stability | Checks for existing paths on the shared environment, in the stated tube/gap regime |
| Finite-width realization with a small defect | Not established |

## 2. Fixed-space adjoint identity

Let \(I:H\to L^2(\Omega)\) be isonormal, so
\(\mathbb E[Ih\,Iv]=\langle h,v\rangle_H\). Let
\[
 u=F(Ih_1,\ldots,Ih_q,Z),
\]
where \(Z\) is independent of the entire isonormal family. For a
bounded smooth \(F\), finite-dimensional Gaussian integration by parts,
including a possibly singular covariance, gives
\[
 \mathbb E[(Iv)u]
   =\sum_{r=1}^q\langle v,h_r\rangle_H
                                  \mathbb E\partial_rF
   =\left\langle v,\sum_{r=1}^q
                          h_r\mathbb E\partial_rF\right\rangle_H
 \tag{2}
\]
for every \(v\in H\). One may prove the singular case by writing
the finite Gaussian vector as a linear image of independent standard
Gaussians and applying their one-dimensional integration-by-parts
identity. No covariance inverse occurs.

The definition of the Hilbert adjoint then gives
\[
 I^*u=\sum_r h_r\mathbb E\partial_rF,\qquad
                  \|I^*u\|_H\le\|u\|_2.
 \tag{3}
\]
For the manuscript's finite-program products, its polynomial source
derivative envelopes and finite Gaussian moments justify the same
identity by smooth truncation and uniform integrability.
For general \(u\in L^2\), \(I^*u\) remains defined by continuity;
an integrable derivative formula for that arbitrary \(u\) is not asserted.

If \(E=\operatorname{span}\{h_r\}\), then \(Iv\), for
\(v\perp E\), is independent of the queried Gaussian variables
and of \(Z\), and has zero mean. Thus \(I^*u\in E\).
Projection onto the Gaussian linear span \(I(E)\) can therefore
be removed from the represented response. For two fields represented
using the same full isonormal map,
\[
 \|I^*u-I^*u'\|_H\le\|u-u'\|_2.
 \tag{4}
\]
The crucial hypothesis is the common map on the common feature space.
Closeness of separately supplied covariance matrices does not create it.

## 3. Causal construction, marginal consistency and completion

At a finite causal stage every new query input is already a computed
field in its source layer. Its \(L^2\) inner products with earlier
inputs are deterministic numbers. Their Gram matrix is positive
semidefinite. Therefore the next source can be appended as a jointly
Gaussian variable with exactly that covariance. A singular conditional
innovation simply has zero variance in some direction.

For two programs, interleave instructions while preserving each
program's internal order. Use the same matrix names and the prescribed
joint layer-root tuples. The finite-array interpretation is a pair of
computations on the same Gaussian matrices and jointly sampled roots.
The manuscript's theorem supplies their joint deterministic limiting
empirical law. Cross-world source covariances are the inner products of
the jointly realized query fields, rather than separately chosen
covariance couplings.

Adding an unused instruction does not alter a program's scalar
expression, root law or previously specified source marginal covariance.
In the unrolled expression a genuinely unused source slot has derivative
zero, even if its Gaussian variable is correlated with used slots.
Consequently the response bookkeeping is consistent under deletion
of unused instructions, including at rank deficiency.

This can be made into one countable causal family without assuming the
completed spaces in advance. Begin with the required finite programs.
Successively include finite unions, rational linear combinations,
a countable dense collection of bounded smooth cylinder functions of
the fields constructed so far, and forward/reverse queries of those
functions. Repeat countably many times. Every individual field and
finite set of sources has finite ancestry and belongs to a finite
causal program. The manuscript's consistency construction realizes
these joint laws on each layer.

For every finite linear combination of lower query fields,
\[
 \mathbb E\left|\sum_r c_r\xi_{h_r}\right|^2
                =\left\|\sum_r c_rh_r\right\|_{H_-}^2.
 \tag{5}
\]
In particular a zero field combination has zero source variance.
Thus \(h\mapsto\xi_h\) is a well-defined linear isometry on the
generated span, independent of its representation. The same argument
defines \(u\mapsto\zeta_u\) on the upper span.
Their continuous extensions are the two maps in (1). Limits of their
finite jointly Gaussian lists remain jointly Gaussian, by \(L^2\)
convergence and convergence of covariance matrices.

Closing under the dense cylinder functions makes the completed spans
the \(L^2\) spaces of the generated sigma fields. This matters:
extending an isometry only on a smaller initial query span would not
justify the full adjoint assertions below.

At every finite stage primitive source groups for distinct
matrix/orientation labels are independent of each other and of the
root tuples, as specified in the manuscript. Since every finite set
belongs to one causal program, independence extends to the corresponding
generated sigma fields. Here a field index such as \(h\in H_-\)
is a deterministic element of a Hilbert space; its coordinates are
random on its layer space, but its inner products used as source
covariances are deterministic. There is no choice of source covariance
conditioned on a realized coordinate value.

## 4. The future-query step and the initialized operator

Take a lower field \(h\) occurring in a finite program. Unroll its
scalar expression in its previously used reverse sources
\(\zeta_{u_1},\ldots,\zeta_{u_q}\), and its root/other primitive
source groups. The latter collection is independent of the reverse
primitive Gaussian group. Previously computed expectations and
response coefficients are deterministic in this unrolling.

For any finite generated upper field \(v\), take a finite union
containing both \(h\) and \(v\), then append the reverse query of
\(v\). Its new source \(Jv\) is jointly Gaussian with the old
reverse sources, with
\[
 \mathbb E[(Jv)\zeta_{u_s}]=\langle v,u_s\rangle_{H_+}.
 \tag{6}
\]
It remains independent of the root/other source groups in the
unrolled expression for \(h\). Applying (2), now with the reverse
isonormal map, gives
\[
 \mathbb E[(Jv)h]
   =\sum_s\langle v,u_s\rangle_{H_+}
                     \mathbb E\partial_{\zeta_s}h
   =\left\langle v,\sum_su_s
                     \mathbb E\partial_{\zeta_s}h\right\rangle_{H_+}.
 \tag{7}
\]
This proves the response identity against every finite generated
upper field, including those computed later. Density then identifies
the response with \(J^*h\) in all of \(H_+\).
The same proof identifies the reverse response with \(I^*u\).

The independence in this argument is independence of primitive
Gaussian source groups. A future *matrix answer* generally depends on
past fields through its response; it is not independent of the past.
Replacing that answer by fresh independent noise would invalidate (7).
Nor may \(v\) be an externally supplied noncausal field without
first placing it in the permitted common construction.

The manuscript's exact finite-program source rule now reads
\[
 W_0h=Ih+J^*h,\qquad W_0^*u=Ju+I^*u
 \tag{8}
\]
on the generated dense spans. The manuscript already constructs a
bounded \(W_0\) and its true adjoint by the finite-array pairing
identity. The right sides of (8) are bounded too, so equality extends
by continuity to the full completed spaces. In particular
\[
 W_0=I+J^*,\qquad W_0^*=I^*+J,\qquad
                         \|W_0\|_{\rm op}\le2.
 \tag{9}
\]
No separate limiting random-matrix norm theorem is needed to obtain
this bound.

As a consistency check, for unit constants in both layers,
\(W_0 1=I1\), since \(J^*1=0\).
Applying the reverse operator gives
\(W_0^*W_0 1=JI1+1\), with the second term the required
response. The reverse action has not become a fresh Gaussian
independent of the original forward call.

For two compatible programs in this same construction, both worlds
use (9). Thus forward/reverse actions have Lipschitz constant at most
two, and each represented response separately has constant one.
These constants require neither a positive queried-Gram eigenvalue
nor bounds on individual response coefficients.

## 5. Reconstruction of the population defect estimate

Use the shared operators (9) in every hidden layer. Let the parameter
Hilbert space be the product of the first-layer \(L^2\) row space,
the Hilbert--Schmidt learned-increment spaces, and the readout \(L^2\)
space. Its Hilbert norm and the candidate's sum norm \(D\) are
equivalent with constants depending only on fixed depth.
The initialized operators themselves need not be Hilbert--Schmidt;
they cancel because the two paths share them.

For clarity, absorb the fixed positive sample weights into the
prediction map and residual:
\[
 \mathcal P(\theta)_a=\sqrt{p_a}\,f_a(\theta),\qquad
 r_a=\sqrt{p_a}\,[f_a(\theta)-y_a],\qquad
 \mathcal J(\theta)=D_\theta\mathcal P(\theta).
 \tag{10}
\]
Here \(r\) in (10) is the weighted residual vector, so its Euclidean
norm is the source's residual RMS \(\rho\).
Canonical population gradient flow is
\[
 \dot\theta=-2\mathcal J(\theta)^*r,\qquad
 \dot r=-2\Gamma r,\qquad
 \Gamma=\mathcal J\mathcal J^*.
 \tag{11}
\]
The true-adjoint identity in (9) is what makes these the actual
population gradient equations.

Assume the exact reference has total residual activity at most \(S\)
and uniform time-marginal Gaussian carrier tails, as proved in the
manuscript. Let a second, existing absolutely continuous path satisfy
\[
 \dot\theta'=-2\mathcal J(\theta')^*r'+\eta(t),\qquad
                  \int_0^\infty\|\eta(t)\|\,dt\le\epsilon.
 \tag{12}
\]
Work initially until its first exit from the enlarged physical tube
or positive tangent-gap region. Both prediction Jacobians are bounded
there, using feature and carrier \(L^2\) bounds.

Forward subtraction costs \(CD\). In a changed-gate term multiply
the difference by the reference carrier \(P\), and split it at
threshold \(R\):
\[
 \|[\phi'(Z')-\phi'(Z)]P\|_2
 \le C R\|Z'-Z\|_2
              +C\|P\mathbf1_{\{|P|>R\}}\|_2
 \le C R D+Ce^{-cR^2}.
 \tag{13}
\]
Other backward differences propagate through bounded gates and
operators. At fixed depth the new changed-gate contributions add;
they do not multiply a factor \(R\) at every layer.
The rank-one formula
\(\|u\otimes v\|_{\rm HS}=\|u\|_2\|v\|_2\)
then gives
\[
 \|\mathcal J'-\mathcal J\|
       \le C[(1+R)D+e^{-cR^2}],\qquad
 \|\Gamma'-\Gamma\|
       \le C[(1+R)D+e^{-cR^2}].
 \tag{14}
\]
Only reference carrier tails have been used.

Let \(e=r'-r\). The exact forced residual comparison is
\[
 \dot e=-2\Gamma'e-2(\Gamma'-\Gamma)r+\mathcal J'\eta.
 \tag{15}
\]
If \(\Gamma'\succeq\lambda I\), differentiating \(\|e\|\)
or using a smooth norm approximation yields
\[
 \frac{d}{dt}\|e\|
 \le-2\lambda\|e\|
       +C\rho[(1+R)D+e^{-cR^2}]+C\|\eta\|.
 \]
Integration gives
\[
 \int_0^t\|e(s)\|\,ds
 \le C\|e(0)\|
   +C\int_0^t\rho(s)[(1+R)D(s)+e^{-cR^2}]\,ds+C\epsilon.
 \tag{16}
\]
This proves source (12), including the additive-force term.

Subtracting (11)--(12) in parameter space gives
\[
 D(t)\le D(0)+C\int_0^t\|e(s)\|\,ds
       +C\int_0^t\rho(s)[(1+R)D(s)+e^{-cR^2}]\,ds+C\epsilon.
 \tag{17}
\]
Insert (16) and apply the integral Gronwall inequality with measure
\(\rho(t)\,dt\), whose total mass is at most \(S\). This yields
\[
 \sup_{t\ge0}D(t)
 \le C e^{CS(1+R)}
       [D(0)+\|e(0)\|+\epsilon+S e^{-cR^2}].
 \tag{18}
\]
For common zero readout and labels, \(e(0)=0\).
For \(a=D(0)+\epsilon>0\) small, choose \(R\ge1\) such that
\(e^{-cR^2}\le a\) and \(R\le C\sqrt{\log(e+1/a)}\).
Then
\[
 \sup_{t\ge0}D(t)\le
                   C a\,e^{C\sqrt{\log(e+1/a)}}.
 \tag{19}
\]
If \(a=0\), send \(R\to\infty\) in (18), obtaining \(D=0\).
For nonmatching initial residuals, include \(\|e(0)\|\) in
the small error parameter instead of omitting it.

The right side of (19) tends to zero with \(a\). Strict reference
tube margins and continuity of the feature Gram therefore exclude
the proposed first exit when the defect is sufficiently small.
No Gaussian tail assumption for the perturbed path is needed.
The statement is stability for an existing path satisfying (12);
it does not by itself prove existence for every arbitrary \(L^1\)
forcing in an infinite-dimensional space.

The manuscript's countable Euler construction realizes its actual
strong population flow on the generated spaces. Hence (19) applies
to that flow and to an admissible comparison path on the same space.
For Euler approximations, their discretization errors must be included
in the integrated defect before passing to a strong limit; the estimate
does not make them vanish without that step.

## 6. Query norm and the missing finite-width statement

For a passive input \(x\), first-layer subtraction costs
\(\|x\|D/\sqrt d\). Linear activation growth and bounded trained
operator norms give feature \(L^2\) envelopes
\(C(1+\|x\|/\sqrt d)\). Propagating differences through the
fixed number of layers and expanding the readout pairing gives
\[
 \sup_t|f(t,x)-f'(t,x)|
 \le C(1+\|x\|/\sqrt d)\sup_t D(t).
 \tag{20}
\]
Consequently (19) transfers to the query norm with the physical-time
supremum inside the integral whenever the fixed query law has a finite
second moment. No query-dependent carrier-tail estimate or higher query
moment is needed at this stability step.

However, (20) presupposes the common physical feature/operator
realization. An empirical covariance estimate alone does not provide
that realization, because its source covariance must equal the Gram
of its physical query fields, including all cross-history pairings.
The candidate's two-query example \((\eta g,g)\) correctly shows
that marginally small changes can coexist with inconsistent future
couplings. It is not a counterexample to (4).

No finite trained network has been placed on this common environment
with integrated parameter defect \(n^{-1/2+o(1)}\) by the
candidate or this check. In particular, the countable completion
does not furnish a quantitative finite-array estimate uniform in
program length. Such a bound cannot be inferred from fixed-program
convergence or from the norm bound (9).

## 7. Source versions and verification record

The candidate remained unchanged during this check. No source
correction was made.

| Source | SHA-256 |
|---|---|
| POPULATION_RESPONSE_TRANSPORT.md | a339eace94acdc797daade3bcc8f58a8c730f720dbb2d9e06c29cba6da3b925c |
| paper/proof_alltime.tex | f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d |
| docs/notation.qmd | 78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023 |
| POPULATION_DIRECT_COUPLING.md | 145895536ea2e006ff444e2ca4eeb8b408ee1adf594dc317e9ea28a05936cb00 |
| GENERAL_SELF_AVERAGING.md | bfbc14cbb3cccf902420db74ca6e3627e341f27a84b52a229362848b376a56d5 |

The latter two study sources had already been read completely in
their relevant scopes; their fixed-space response and feedback
comparisons provide context, not an additional finite-width bridge.
The manuscript proof was previously read completely and its Gaussian
construction and strong-flow sections were reread here. Required
mathematical-notation and research-process instructions were reused.
No diagnostic or synthesis note written concurrently by another agent
was used.

A frozen source copy is retained at
data/generated/dense_cutoff_population_rate_20261001/population_response_transport_check_20261003/POPULATION_RESPONSE_TRANSPORT.frozen.md.
Checks consisted of source reads and hashes, typed operator
reconstruction, finite Gaussian integration by parts, causal-extension
and dense-span arguments, the exact forced residual equation, and
the activity-measure Gronwall calculation written above.
No experiment, GPU probe, Git staging or commit was performed.
