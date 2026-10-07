# Constructive route: no sublinear-in-`d` logarithmic representation obtained

## Verdict

**NO VALID CONSTRUCTION.** None of the examined routes yields a fully
autonomous, restartable, depth-at-least-two feature-learning model with total
retained size

\[
C_{\rm task}[\log(en)]^{r(d)},\qquad r(d)=o(d),
\]

and error at most
\(n^{-1/2}[\log(en)]^{-5/2}\) uniformly over physical time, including the
fitted endpoint, and over the entire radius-\(\sqrt d\) sphere. This is a
negative verdict on the constructive route, not a representation lower bound:
the existence question remains open unless the separate lower-bound route
closes it.

The strongest defensible partial conclusion is structural. The predictor can
be reduced exactly to \(m\) evolving tangent-kernel sections, and every learned
compact mixer has rank at most \(m\) **instantaneous velocity**. Neither fact
gives a finite autonomous closure or a low rank for the accumulated mixer.
Even if every quadratic mixer, metric, and decoder cost were optimistically
reduced to linear cost, the only proved angular regularity still gives a
logarithmic exponent \(3(d-1)/2\), which is linear in \(d\).

## 1. Frozen contract and the existing benchmark

Write

\[
v=x/\sqrt d\in S^{d-1},\qquad \ell_n=\log(en),\qquad
\varepsilon_n=n^{-1/2}\ell_n^{-5/2}.
\]

The target is the realized width-\(n\), hidden-depth-\(L\ge2\) dense gradient
flow on the fixed full-rank data, not its expectation or an independent copy.
Every fixed or moving numerical coordinate needed to initialize, restart,
evolve, or evaluate the reduced model is counted. In particular, a selected
metric, a data-dependent basis or dictionary, both directions of a mixer, a
decoder, and a coefficient table all count. A time-indexed source table,
future-trajectory preprocessing, frozen kernel, or query-time call to the dense
network is inadmissible.

The established compact model already has the stronger error

\[
\|f_{\rm compact,n}-f_n\|_*
\le C_{\rm task}\frac{e^{2\sqrt{\ell_n}}}{n}
=o(\varepsilon_n).
\]

Its source rank and all-retained storage are, at fixed task,

\[
R_n\le C_{\rm task}\ell_n^{3d/2+1},\qquad
q_j\le 9(R_n+2m+d+1),
\]
\[
\operatorname{storage}(f_{\rm compact,n})
\le C_{\rm task}\ell_n^{3d+2}+C_{\rm task}.
\]

Thus accuracy, autonomy, feature motion, the full sphere, and the endpoint are
already attained. The sole target failure is the dimension dependence of the
logarithmic exponent.

Relaxing the source tolerance does not change this exponent. To use the
polynomial comparison at error \(\varepsilon_n\), one may take a source error
of order

\[
\epsilon_{\rm src}
\asymp \varepsilon_n e^{-2\sqrt{\ell_n}}/C_{\rm task}.
\]

But

\[
\log(1/\epsilon_{\rm src})
=\tfrac12\ell_n+2\sqrt{\ell_n}+\tfrac52\log\ell_n+O_{\rm task}(1)
=\Theta(\ell_n),
\]

so the degree and mode-count powers are unchanged.

## 2. The decisive angular count

The supplied source theorem gives a query tube radius and a rescaled-time
strip parameter

\[
r_q=\frac{c_q}{\sqrt{\ell_n}},\qquad
\alpha=\frac{c_t\lambda}{128\ell_n^{3/2}},
\]

where \(c_q,c_t,\lambda\) are fixed-task quantities independent of \(n\). At
source error \(\epsilon_{\rm src}\) above, its coefficient cutoff satisfies
\(H=\Theta(\ell_n)\). Therefore the maximum spherical-harmonic degree is

\[
J_n\asymp H/r_q=\Theta_{\rm task}(\ell_n^{3/2}).
\]

The exact dimension of spherical harmonics through degree \(J\) is

\[
\sum_{j=0}^{J}h_j
=\binom{J+d-1}{d-1}+\binom{J+d-2}{d-1}
=\Theta_d(J^{d-1}).
\]

Consequently a full isotropic angular truncation alone costs

\[
N_{\rm ang}
=\Theta_{\rm task}(\ell_n^{3(d-1)/2}).
\tag{1}
\]

The time modes cost \(H/\alpha=\Theta_{\rm task}(\ell_n^{5/2})\).
The joint weighted-simplex count is accordingly

\[
N_{\rm joint}
\lesssim \frac{H^d}{\alpha r_q^{d-1}}
=C_{\rm task}\ell_n^{3d/2+1},
\tag{2}
\]

which reproduces the established source rank. Squaring selected widths gives
the current \(3d+2\) storage exponent.

Equation (1) is decisive for all refinements based only on the currently
proved isotropic complex tube. Eliminating time modes and reducing every
quadratic retained array to linear cost would still leave exponent
\(3(d-1)/2\), not \(o(d)\). This is a limitation of the available
construction theorem, not a lower bound for the reachable dense trajectories:
the missing possibility is that reachability forces a much smaller structured
subset of harmonic coefficients.

## 3. Route audit

### 3.1 Data-correlation coordinates

Let \(V=[v_1\ \cdots\ v_m]\in\mathbb R^{d\times m}\). Full input rank gives
\(\operatorname{rank}V=d\). The correlation coordinate

\[
g(v)=V^Tv
\]

is injective, because

\[
v=(VV^T)^{-1}Vg(v).
\tag{3}
\]

Thus every query function can indeed be expressed as a function of the data
correlations, at the counted fixed cost of the decoder in (3), but its domain
has intrinsic dimension \(d-1\). Since \(m\ge d\) and the samples span
\(\mathbb R^d\), these coordinates remove no angular dimension. A claim that
the function depends on only a fixed number of correlations would require an
additional inactive-subspace invariant, contradicted by neither the hypotheses
nor the supplied proofs.

**Status:** exact reparameterization; no compression exponent improvement.

### 3.2 Kernel sections and the Volterra hierarchy

Let \(c_a(t)=y_a-f_n(t,v_a)\), and let \(K_n\) be the tangent kernel with
the prescribed block mobilities. The dense gradient flow gives the exact
identity

\[
\partial_t f_n(t,v)
=\frac2m\sum_{a=1}^m c_a(t)K_n(t;v,v_a),\qquad f_n(0,v)=0.
\tag{4}
\]

This reduces output synthesis to \(m\) time-dependent scalar kernel sections.
It does not close their dynamics. Differentiating \(K_n\) introduces Hessian
actions and mixed feature/response fields; repeated differentiation generates
a tangent/Volterra hierarchy. Freezing \(K_n\) gives a kernel surrogate and is
expressly inadmissible. Storing the section trajectories gives oracle replay
and is also inadmissible.

Even under a favorable unproved geometric remainder \(C_{\rm task}S^{p+1}\)
for a \(p\)-level Volterra truncation with fixed \(S<1\), reaching
\(\varepsilon_n\) requires \(p=\Theta_{\rm task}(\ell_n)\). A direct word
expansion then has \((mL)^p=n^{\Theta_{\rm task}(1)}\) terms. Tensorizing the
hierarchy helps only if its separation ranks remain
\(\ell_n^{o(d)}\); no such bound is supplied or derived.

At \(t=0\), since the readout is zero, the first nonzero term of (4) already
contains the realized empirical top-feature Gram section. Replacing it by its
population expectation discards finite-width, generally non-zonal
fluctuations at the scale that the requested comparison must resolve.

**Status:** exact scalar reduction, but no autonomous finite closure.

### 3.3 Tensor trains and separated spherical harmonics

A tensor train would change the count only if every degree block of every
reachable feature, backward field, kernel section, metric, and mixer action had
a stable rank \(\rho_n\) satisfying \(\rho_n=\ell_n^{o(d)}\), uniformly through
training. A single zonal ridge function has favorable separated structure, but
the dense model applies generic initialized mixers, nonlinear coordinate gates,
their metric adjoints, and sums over all neurons. The supplied amplitude,
energy, analyticity, and pairing estimates do not control matricization ranks
of the resulting harmonic tensors. They permit every coefficient in a degree
block of dimension \(h_j\).

The empirical kernel section in the initial derivative is already a necessary
test: a rank theorem must control its realized finite-width coefficient tensor,
not merely the zonal population kernel. No such theorem follows from the
Gaussian insertion or source-energy bounds.

**Status:** conditional possibility only; the required rank invariant is the
main missing lemma, not a routine tensor conversion.

### 3.4 Sparse grids and hyperbolic crosses

Hyperbolic-cross improvement requires coordinatewise mixed-derivative or
product-weighted coefficient decay. The proved query domain is rotationally
invariant and yields total-degree decay \(e^{-r_qj}\). It does not distinguish
coordinate subsets or penalize interaction order. Within that analytic class,
a coefficient may occupy any of the \(h_j\) harmonics at degree \(j\); a
hyperbolic cross omitting most of them has no certified tail bound.

Full data rank also prevents declaring any physical direction inactive.
Therefore the only justified sparse-grid count is the isotropic count (1).
Proving that the *reachable* coefficients obey product weights could change
this conclusion, but that is precisely an absent reachability theorem.

**Status:** fails for lack of mixed regularity/sparsity; using it would add an
unstated hypothesis.

### 3.5 Compositional ridge representations

The dense predictor is compositional, so one may seek a much narrower network
directly. For widths \(q_1,\ldots,q_L\), however, the ordinary retained moving
state already contains

\[
dq_1+\sum_{j=2}^Lq_jq_{j-1}+q_L,
\]

before metrics, data-dependent decoders, and residual coordinates. Available
energy control gives no exponential-in-width uniform approximation theorem for
the realized whole-sphere trajectory. A generic sampling/Barron estimate of
order \(q^{-1/2}\) would require \(q\gtrsim\varepsilon_n^{-2}
=n\ell_n^5\), not polylogarithmic width. Analytic ridge approximation reverts
to the harmonic count (1) unless a low-rank reachable coefficient theorem is
added.

Moreover a ridge model with fixed hidden features is a forbidden relabeling of
a kernel surrogate. Its hidden directions and mixers must evolve and remain
closed from the retained state.

**Status:** no certified polylogarithmic-width nonlinear approximation.

### 3.6 Structured compact mixers

For the corrected compact runtime, each learned hidden mixer has the exact
rank-\(m\) velocity form

\[
\dot B^{(j)}(t)
=\frac2m\sum_{a=1}^m c_{C,a}(t)
\,\delta_{C,a}^{(j)}(t)\otimes_{M_{j-1}}
h_{C,a}^{(j-1)}(t).
\tag{5}
\]

This is the strongest concrete structural improvement found. It does **not**
bound the rank of

\[
B^{(j)}(t)-B^{(j)}(0)=\int_0^t\dot B^{(j)}(s)\,ds.
\]

A continuum of rotating rank-one directions can span the full selected space;
total variation bounds do not control singular-value tails. The fixed
initialized action \(B^{(j)}(0)\) must also act on all runtime feature
directions and its metric adjoint must act on all backward directions. No
low-rank or fast-transform description of both actions is provided.

Factoring only \(B^{(j)}\) is insufficient. The selected metrics \(M_j\), fixed
copies, Gram/solve data, and decoders are counted and are currently quadratic.
Changing to an orthonormal coefficient basis can make a metric trivial, but
then coordinatewise application of \(\phi_j\) requires a dense change-of-basis
map; the quadratic information is moved rather than removed.

If, counterfactually, all quadratic objects admitted stable linear-cost
descriptions, the count would improve from
\(C_{\rm task}\ell_n^{3d+2}\) to at best
\(C_{\rm task}\ell_n^{3d/2+1+O(1)}\). This is a meaningful halving of the
current coefficient of \(d\), but it still violates \(r(d)=o(d)\) by (1).

**Status:** exact low-rank velocity, but no low-rank accumulated state; even
the optimistic count does not meet the target.

## 4. Endpoint, autonomy, and hidden-feature audit

None of the rejected routes fails merely because of the fitted endpoint. If a
candidate matched the dense and compact flows through

\[
T=32\lambda^{-1}\ell_n
\]

while preserving their independent residual gaps, the established
exponential tail argument would extend the comparison to all later time and
the endpoint. The unresolved issue is building that finite-horizon autonomous
state without a trajectory oracle.

Similarly, small labels do not license freezing features. The feature motion
is small in a fixed-task norm but does not vanish with \(n\). Since
\(\varepsilon_n\to0\), a fixed nonzero feature-learning correction eventually
dominates the target. A valid construction must evolve hidden features and
both forward and reverse mixer actions; matching only (4) with a frozen kernel
does not qualify.

All constants used above are fixed-task constants. No proposed improvement is
allowed to hide \(J_n\), a tensor rank, a time-order \(p\), a dictionary size,
or a mixer factor count in \(C_{\rm task}\), because each of those depends on
\(n\).

## 5. Precise missing invariant

A constructive proof would become possible from the following genuinely new
reachability statement.

There must exist initialization- and data-computable spaces or nonlinear
tensor manifolds \(\mathcal E_{j,n}\), with total stable coordinate count

\[
P_n\le C_{\rm task}\ell_n^{s(d)},\qquad s(d)=o(d),
\tag{6}
\]

such that, uniformly for \(0\le t\le T\) and \(v\in S^{d-1}\):

1. the realized forward features, backward responses, initialized forward
   images, and initialized transpose images have approximation error at most
   \(C_{\rm task}\varepsilon_ne^{-2\sqrt{\ell_n}}\);
2. the manifolds are stably closed under the current forward mixer, its metric
   adjoint, coordinatewise \(\phi_j\) and \(\phi_j'\), and the rank-\(m\)
   updates (5);
3. the induced metrics, dictionaries, decoders, and both mixer directions have
   descriptions of total size \(C_{\rm task}\ell_n^{o(d)}\), with condition
   numbers controlled independently of \(n\);
4. the retained coordinates determine an autonomous, restartable vector field
   and preserve the residual Gram gap needed for the all-time tail; and
5. (6) holds for the **realized finite-width** initialization, not only for its
   population expectation.

This is a stable low-separation-rank invariant for the reachable nonlinear
tangent hierarchy. It is strictly stronger than analyticity, small total
parameter motion, instantaneous rank-\(m\) mixer velocity, or population
rotational symmetry. No supplied result proves any substitute with
\(s(d)=o(d)\). Conversely, a proof of this invariant would feed into the
existing source-selection and coupled readout/residual comparison: quadratic
retained arrays would cost \(P_n^2=\ell_n^{2s(d)}\), still with exponent
\(o(d)\), and the existing tail mechanism would deliver the endpoint.

## 6. Claim boundary

Established here:

- the existing autonomous nonlinear construction beats the requested error but
  uses exponent \(3d+2\);
- relaxing its source tolerance to the variability scale does not change that
  exponent;
- full-rank correlation coordinates retain intrinsic dimension \(d-1\);
- the kernel-section identity (4) and rank-\(m\) mixer velocity (5) are exact;
- isotropic analyticity alone yields the angular count (1), so sparse grids,
  harmonics, and an ideal linear-cost mixer remain linear-in-\(d\) in their
  logarithmic exponent.

Open:

- a reachable-state tensor/separation-rank bound of the form (6);
- a finite autonomous closure of the tangent/Volterra hierarchy;
- simultaneous structured representations of metrics, decoders, initialized
  mixer actions, accumulated learned mixers, and their adjoints;
- any construction with \(r(d)=o(d)\).

Accordingly, this route supplies neither a positive answer nor an impossibility
theorem. Its unequivocal constructive verdict is **failure: no admissible
sublinear-in-\(d\) logarithmic representation has been constructed.**

## Process note

The repository-required `explain-with-canonical-notation` skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` was
inaccessible because of filesystem permissions, including after an approved
read attempt. The maintained notation contract in `docs/notation.qmd` was
applied directly.
