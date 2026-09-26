# Fixed response bases, frozen dictionaries, and evolving response histories

2026-09-26. Scoped theoretical assessment, with no experiments or new fitted
bases. The only scientific inputs were the complete study-owned files
`scalar_response_basis.py`, `SCALAR_RESPONSE_BASIS_THEORY.md`,
`MOMENT_CONSTRUCTION.md`, `RATIONAL_ORTHOGONAL_MOMENT_ROUTE.md`,
`HARD_BENCHMARK_INPUTS.md`, and `MOMENT_RESULTS.md`. Links in those sources
were not followed. Required process skills were investigate-conjectures and
solve-math-rigorously. This is an internal analysis, not a promotion review.

The user cancelled the proposed new experiments once the fixed-dictionary
restriction was established, before any new neural runs. The width-64,
two-seed stress comparison was not executed. The diagnostic recipes below
are unused possibilities retained for reference, not pending work.

**Conclusion.** The scalar response-basis construction restores the central
restriction of a frozen dictionary: learned matrix increments cannot acquire
left or right directions outside the initialized spaces. It imposes further
fixed-space restrictions on its internal responses and approximates nonlinear
products. A changing positive semidefinite training kernel does not remove
these restrictions. Nevertheless, fixed neuron-space directions do not imply
lazy training, frozen input features, or impossibility of substantial feature
learning. Its prediction accuracy is not settled by the structural
restriction alone. The evolving moment construction has a
different restriction: finitely many history factors, whose neuron-space
directions evolve with the current responses.

## 1. Exact comparison of the three constructions

The historical dictionaries described in `HARD_BENCHMARK_INPUTS.md` use a
two-hidden-layer network. The supplied scalar engine has three hidden layers.
The structural comparison below is meaningful across these architectures;
their historical RMS values are not matched numerical comparisons. No new
matched numerical comparison was performed.

| Property | Historical fixed dictionary | Current scalar response basis | Response-history moments in the supplied notes |
|---|---|---|---|
| Spatial factors | Initialized dictionaries, subsequently fixed | Initial training responses, backward responses, response velocities, products and cubics; one frozen SVD | Neuron vectors driven by current responses and residual-weighted backward responses |
| Learned middle action | Evolving core between fixed spatial factors | Evolving cores between fixed spatial factors | Sum of products of evolving history factors |
| Initialized operator | Entire middle matrix replaced by dictionary factorization | Only its projected actions enter the scalar RHS; full initial matrices occur in the detached validation decoder | Actual full initialized operator and its transpose remain in the dynamics |
| Outer layers | Neuron-resolved moving outer weights | First-weight changes and readout represented in fixed spaces | Neuron-resolved moving outer weights |
| Responses | Responses of the represented physical network | Independently evolved projected response coordinates | Exact response chain rules at the reconstructed network, before numerical integration error |
| Main restriction | Fixed left and right spaces for the entire middle matrix | Fixed spaces for learned increments and all internal response fields, plus product/operator approximations | Finite temporal-history projection, with changing spatial directions |

The scalar decoder uses the full initialized matrices, so its decoded middle
matrix need not have low rank. This does not mean the full initialized
operator is used by the scalar dynamics. The RHS sees only
`C2`, `C3`, the cubic product tensors, and current coefficients. Unlike the
moment construction, it cannot apply the omitted initialized operator to a
new response direction.

The fixed temporal Legendre basis of the moment construction must not be
confused with a frozen neuron-space dictionary. Its scalar polynomial
weights are prescribed, while its neuron-vector integrals evolve.

## 2. The fixed-span obstruction and its exact error floor

Fix one internal layer. Write `Q_L`, `Q_R` for the scalar engine's two bases,
with `Q_L^T Q_L/n=I` and `Q_R^T Q_R/n=I`. Let

\[
 U=Q_L/\sqrt n,\quad V=Q_R/\sqrt n,\quad
 P_L=UU^T,\quad P_R=VV^T.
\]

The decoded learned increment has the form

\[
 \widehat D(t)=\widehat W(t)-W_0=U B(t)V^T.
\]

Consequently, for every coefficient trajectory, however nonlinear,

\[
 (I-P_L)\widehat D=0,\qquad
 \widehat D(I-P_R)=0,\qquad
 \operatorname{rank}\widehat D\le r.
 \tag{1}
\]

Indeed multiplication by either complementary projection kills the fixed
factor, and the image of the product has dimension at most `r`. The same
relations hold for the increment velocity. Thus neither nonlinear
coefficient evolution nor longer training can create a missing direction.
For the historical factorization, (1) applies to the entire represented
middle matrix; hence it also applies to the difference between any two of
its states. This is the precise shared limitation.

Let `D=W_dense(t)-W0` be a matched dense increment. Since multiplication by
`P_L` on the left and `P_R` on the right is a self-adjoint idempotent map in
the Frobenius inner product, it is an orthogonal projection. Explicitly,
`U^T(D-P_L D P_R)V=0`, which makes its residual orthogonal to every `UBV^T`.
Therefore

\[
 \|D-UBV^T\|_F^2
 =\underbrace{\|D-P_LDP_R\|_F^2}_{\text{unavoidable fixed-space error}}
   +\|U^TDV-B\|_F^2.
 \tag{2}
\]

The first term has the computable decompositions

\[
 \|D-P_LDP_R\|_F^2
 =\|(I-P_L)D\|_F^2+\|P_LD(I-P_R)\|_F^2
 =\|D\|_F^2-\|U^TDV\|_F^2.
 \tag{3}
\]

For the first equality, the two displayed residual blocks have orthogonal
left ranges. This avoids counting the omitted left/right corner twice.
Equation (2) is an unconditional representation lower bound at that dense
snapshot. It requires neither simulation of an alternative surrogate nor
optimization of a new basis. It does **not** lower-bound output error: a
matrix direction can have little effect on the tested inputs and readout.

The scalar restrictions also give

\[
 \inf_A\|\Delta w_{\rm dense}-Q_1A\|_F
 =\|(I-P_1)\Delta w_{\rm dense}\|_F,
 \qquad
 \inf_b\|c_{\rm dense}-Q_3b\|_n
 =\|(I-P_3)c_{\rm dense}\|_n,
 \tag{4}
\]

where `||z||_n=||z||_2/sqrt(n)`. The readout statement concerns the entire
readout because the implementation initializes it by projection; it does
not retain an unprojected `c0` offset. For every internally represented
response, the analogous exact lower bound is
`||(I-P_l)h_l,dense||_n`. These are additional restrictions absent from the
historical model's unrestricted outer neuron vectors.

Low rank and fixed orientation are different restrictions. If `sigma_j`
are the singular values of `D` in decreasing order, the least possible
squared error among all rank-at-most-`r` matrices is

\[
 E_{\rm rank}^2=\sum_{j>r}\sigma_j^2
 \le E_{\rm fixed}^2:=\|D-P_LDP_R\|_F^2.
 \tag{5}
\]

For completeness, if a candidate matrix has column space `S`, dimension at
most `r`, its error is at least `||(I-P_S)D||_F`. In a left singular basis,
`tr(P_S DD^T)=sum_j sigma_j^2 p_j`, with `0<=p_j<=1` and `sum_j p_j<=r`.
This is at most the sum of the first `r` squared singular values, by moving
weight from smaller to larger entries. Keeping the first `r` singular
components attains the resulting bound. This proves (5).
The nonnegative gap `E_fixed^2-E_rank^2` measures restriction from the
particular initialized spaces beyond the rank budget. A low-rank dense
increment can still have a large fixed-space error.

## 3. What changing coefficients and a changing kernel establish

The scalar model has evolving response matrices, readout, and middle cores.
Its symmetric projected multiplication yields the exact internal identities
proved in `SCALAR_RESPONSE_BASIS_THEORY.md`:

\[
 \dot f=-\frac2M J(t)J(t)^T(f-y),\qquad
 \frac d{dt}\frac{\|f-y\|_2^2}{M}
 =-\frac4{M^2}\|J(t)^T(f-y)\|_2^2\le0.
\]

Here each row of `J` comprises the current response/backward products for
the coefficient blocks. It generally changes as training proceeds. These
identities certify internal loss dissipation and show that the equations
are not defined by a frozen training kernel. They do not certify a large
amount of feature learning on a particular trajectory. They also do not
make `J` the Jacobian of the decoded tanh network, or remove (1).

Fixed neuron-space rank does permit substantial nonlinear feature change.
A simple logical example is a tied population with all neurons having
response `h_i(x)=tanh(a x)` and readout `b`. Every neuron response lies in
the fixed one-dimensional span of the all-ones vector. Nevertheless, for
inputs `x=1,2` and `a!=0`,

\[
 \frac{h_i(2)}{h_i(1)}
 =\frac{2}{1+\tanh^2(a)},
\]

which varies by order one when `a` changes substantially. Training `a`
therefore changes the input feature shape, rather than merely rescaling a
fixed feature through `b`. This example is not evidence about the random
initialization ensemble; it disproves the blanket implication from a fixed
neuron span to frozen input features. Large nonlinear motion within the
retained spans remains possible in the actual scalar construction.

Conversely, a small or moderate kernel change alone does not settle whether
the dense feature-learning mechanism is captured. Measure changes in
responses, backward responses, and learned actions, and their directions
outside the frozen spaces. Loss fitting without matching those directions
may still produce different passive predictions.

## 4. Why the moment model escapes this particular restriction

In the supplied two-hidden-layer moment formulation,

\[
 \widehat W_2-W_0=-\frac2{nML}
   \sum_{a=1}^M\sum_{k<P}(2k+1)U_{ak}(t)H_{ak}(t)^T.
\]

Its increment rank is at most `MP`, but the factors satisfy

\[
 \dot U_{ak}=r_a\delta_a-\frac\rho L
   \left(kU_{ak}+\sum_{j<k}(2j+1)U_{aj}\right),\qquad
 \dot H_{ak}=\rho h_a-\frac\rho L
   \left(kH_{ak}+\sum_{j<k}(2j+1)H_{aj}\right).
\]

For any fixed neuron-space projector `P`, its omitted forward component
obeys the same transport equation with source `rho(I-P)h_a`; the backward
source is `(I-P)(r_a delta_a)`. Thus a zero omitted component is preserved
only if the relevant current source has no omitted component. There is no
algebraic invariant confining every factor to a prescribed initial dictionary.
The current factor span may rotate or change dimension; the union of spans
over time need not have dimension at most `MP`.

This structural distinction alone does not prove the moment approximation
accurate. It still omits cross-history covariance and imposes a finite rank
at each instant. Its specific physical velocity defect is the endpoint-error
product given in the supplied construction. The older supplied moment notes
state their convergence estimate under uniform activity and response-regularity
assumptions, and record those assumptions as unresolved there. This describes
those sources only; it does not assess later finite-horizon results or the
current study-wide theorem status, which are outside this report's input
scope. The earlier finite numerical success reported in `MOMENT_RESULTS.md`
supports that witness on its tested targets, with the full `W0` storage cost;
it establishes neither a scalar closure nor a matched-total-storage advantage.
This report does not audit later multi-layer population implementations.

## 5. Scalar response closure creates an additional inconsistency

Let `Hhat_l=Q_l h_l` be an internal scalar response and let `Hdec_l` be the
actual tanh activation of the decoded weights. At reduced rank these need
not agree even at initialization, because the former is a projection of
the exact initial response. Subsequent disagreement has two separate
sources:

- Elementwise products are projected after each multiplication. In general
  `P((Pa)(Pb))` does not reproduce the corresponding unprojected composed
  product: omitted components can return to retained directions later.
- Initialized actions retain only `P_l W_l0 P_prev`; the true decoder
  additionally contains complementary actions of `W_l0`.

For example, with an internal first-layer derivative factor constructed
from projected products, `Q_1 dot h_1` need not equal
`(1-Hdec_1^2) elementwise (Q_1 dot dw U_query)`. Hence the response coordinates
are not generally constrained to the tanh manifold of the decoded weights.
The exact output discrepancy is

\[
 f_{\rm internal}-f_{\rm decoded}
 =\langle Q_3c,\,Hhat_3-Hdec_3\rangle_n.
\]

This error is distinct from the inability of the decoded weights to track
dense increments. Full rank removes both projection sources in exact
arithmetic; reduced-rank internal loss descent does not control either one.
Any empirical verdict must retain internal and decoded predictions as
separate observables.

## 6. Unused diagnostic recipes

These possible assessments were not evaluated. The cancelled experiments
are not a proposed continuation. If separately authorized in another
assessment, the recipes would use bases constructed from each matched
initialization and training set before inspecting its future dense states;
they would not fit a replacement basis. Comparisons would use common
physical times, separately report each model's loss-threshold endpoint, and
retain each rank, layer, seed, and case rather than pool away a hard case.

1. **Response escape.** For training and predeclared passive inputs, report
   `||(I-P_l)H_l(t)||_F/sqrt(n J)` and
   `||(I-P_l)(H_l(t)-H_l(0))||_F/sqrt(n J)`; do the same for backward
   responses when available. The increment version separates new motion
   from initial projection error. Also give relative escape divided by
   the corresponding total norm when that denominator is resolved above
   numerical noise. At zero motion, mark the relative ratio undefined.

2. **Learned-matrix floor.** Report (3) for each `D_l(t)`, both absolutely
   and relative to `||D_l(t)||_F`. Give the two orthogonal block terms, and
   compare against (5). Available full-state snapshots would make this direct.
   An SVD used only to diagnose singular values or angles is not used to
   define, tune, initialize, or run a replacement basis.

3. **Dominant-direction leakage.** If
   `D=sum_j sigma_j u_j v_j^T`, report
   `sum_j sigma_j^2||(I-P_L)u_j||^2/||D||_F^2` and the analogous right
   quantity. These equal the relative one-sided Frobenius escape and are
   invariant under choices within degenerate singular clusters. For a
   predeclared `k<=r`, principal angles between the leading singular
   subspace and the frozen basis have cosines equal to the singular
   values of `U^T[u_1,...,u_k]` (and similarly on the right). Report the
   largest sine or `||(I-P_L)[u_1,...,u_k]||_F/sqrt(k)`. At a tied cutoff,
   include the complete singular cluster or flag the angle as ambiguous;
   energy-weighted leakage remains well defined. There is no reason for
   a new SVD on dense data to enter the dynamics.

4. **Relevance to actions.** Apply the omitted block
   `D-P_L D P_R` to current dense forward responses and its transpose to
   current dense backward responses. Normalize by total learned action
   only when nonzero, and retain absolute empirical-neuron norms. These
   connect matrix escape to the actual forward/backward channels. They
   still do not give an output-error lower bound, because later layers
   and readout may cancel or suppress a discrepancy.

5. **Initialized action and decoder consistency.** Measure actual-vector
   leakage, such as `||(I-P_l)W_l0 P_prev H_prev(t)||`, alongside the
   complementary input action `||W_l0(I-P_prev)H_prev(t)||`. Do not infer
   dynamic accuracy from the unweighted whole-basis leakage Frobenius
   norm alone. For scalar trajectories, separately record
   `||Hhat_l-Hdec_l||_n`, internal/decoded output RMS, and both training
   losses. Compare those changes under the prescribed solver refinement.

A resolved large fixed-space floor and small unrestricted-rank floor
identify an orientation bottleneck for this scalar witness's state tracking.
A large rank floor identifies a rank-budget bottleneck even if directions
could adapt. Small floors leave its dynamic coefficient law, product
closure, and accumulated error as possible problems. Neither large floor
alone proves passive predictions inaccurate, and neither small floor
alone proves them accurate. The rank trend of nonlinear trajectory errors
need not be monotone, even though the best projection error of each fixed
dense snapshot decreases for nested spaces.

## 7. Claim status

| Claim | Status and scope |
|---|---|
| Frozen scalar increments have fixed left/right spaces and rank at most `r` | Proved by (1), for every existing coefficient trajectory |
| Dense snapshots give an exact fixed-space representation floor | Proved by (2)--(4), for state norms only |
| This repeats the historical dictionary's directional restriction | Proved structural comparison from the supplied descriptions; the full models differ |
| Fixed neuron-space rank forbids substantial feature learning | False as a general implication; the explicit tied-population example disproves it |
| The scalar equations can have changing PSD training kernels | Exact internal identity; the magnitude and fidelity of change require measurement |
| Moment factors are confined to one initialized neuron-space dictionary | No such invariant is imposed; their current source terms can create omitted components |
| Small scalar internal loss certifies a fitted decoded network | Not established; the independent response coordinates create a separate consistency defect |
| Rank 12, 24, or 40 captures the proposed width-64 stresses | Not tested; the user cancelled the comparison before any new neural runs |
| Failure of this fixed-basis witness rules out autonomous finite scalar approximations | Unsupported; the representation class is much broader |

The exact structural conclusion is the fixed-direction restriction proved
above. The unused diagnostics could distinguish escape from initial spaces
from a rank-budget limitation without training a new basis on dense
trajectories. They are not needed to establish that structural conclusion,
and no numerical prediction-fidelity verdict is claimed here.
