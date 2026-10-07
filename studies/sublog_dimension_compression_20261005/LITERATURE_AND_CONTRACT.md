# Literature and research-contract audit

## Bottom line

**Current verdict: open.** I found no theorem that settles the requested class of
complete, whole-sphere trajectories of the canonical trained dense network.
Classical analytic-function entropy and width results make an exponent proportional
to the intrinsic input dimension entirely plausible for a *generic analytic ball*.
Under a bounded-condition (p)-coordinate encoder/decoder, they yield a lower-bound
template of order ([log(1/\varepsilon)]^{d-1}) for static functions on
(S^{d-1}), and order ([log(1/\varepsilon)]^d) for a genuinely free analytic
time--sphere class. They do **not** prove that the much smaller set of trajectories
reachable by the stated gradient flow contains the required packing.

Conversely, none of the located neural, ridge, manifold-width, or mean-field results
constructs a stable, autonomous, restartable compressor of size
(C_{\rm task}[\log(en)]^{o(d)}) for this target. The exact bottleneck is therefore
the one already identified in the study README: either exploit a special low-complexity
property of the reachable nonlinear trajectories, or prove a reachability packing.

Labels used below are **Sourced fact**, **Derivation**, and **Inference**. The last
two are not claims made by the cited papers.

## 1. A non-vacuous statement of the question

For dimension (d), let a task

\[
 \tau_d=(L,m,X,y,\phi_1,\ldots,\phi_L,\gamma,\beta)
\]

satisfy the study assumptions: (L\ge2), (m\ge d), the rows of (X) span
\(\mathbb R^d\), the inputs have norm \(\sqrt d\), the feature-Gram gap is positive,
the label condition holds, and the activations are in the stated analytic non-affine
class. The task is fixed independently of dense width (n). Let \(\omega\) denote
the dense initialization and (f_{n,\omega}(t,x)) its trained predictor.

A sharp positive claim should have the following order of quantifiers.

> There is one nonnegative exponent function (r:\mathbb N\to[0,\infty)) with
> \(\lim_{d\to\infty}r(d)/d=0\). For every (d), every admissible task \(\tau_d\),
> and every confidence (0<\delta<1), there are finite
> (C(\tau_d,\delta)) and (N_0(\tau_d,\delta)), neither depending on (n) or on
> the realized initialization, such that for every (n\ge N_0), with probability
> at least (1-\delta) over \(\omega\), an admissible encoder produces a retained
> descriptor and initial state with total coordinate count
> \[
> p(n,\tau_d,\omega)\le C(\tau_d,\delta)[\log(en)]^{r(d)}.
> \]
> The retained descriptor defines an autonomous, restartable evolution and a
> whole-sphere decoder (f_C(t,x)) satisfying
> \[
> \sup_{t\in[0,\infty]}\sup_{\|x\|_2=\sqrt d}
> |f_C(t,x)-f_{n,\omega}(t,x)|
> \le {c_{\tau_d}\over \sqrt n[\log(en)]^{5/2}}.
> \]

The error constant and whether it may depend on \(\delta\) should be frozen in the
final theorem. A per-width probability statement is enough, but it must not be
silently upgraded to one event for infinitely many independent widths.

### Fixed (d) versus (r(d)=o(d))

**Derivation.** At any one fixed (d), the phrase (r(d)=o(d)) has no content;
little-(o) is a statement about a sequence as (d\to\infty). The mathematically
coherent limit order above is

\[
 d\ \hbox{indexes a family of fixed tasks},\qquad n\to\infty\ \hbox{within each
 task},\qquad {r(d)\over d}\to0.
\]

The theorem can be nonuniform in (d), but then (C(\tau_d,\delta)) and
(N_0(\tau_d,\delta)) may grow arbitrarily quickly with (d). Such a theorem still
has a genuine statement about the exponent of \(\log n\), but it is not a joint
high-dimensional tractability result. Any stronger interpretation needs explicit
dimension bounds on (C), (N_0), (m), \(\gamma^{-1}\), and the activation
envelopes. In particular, the family of tasks used as (d\to\infty) must be stated;
“fixed task” cannot mean one unchanged dataset while (d) changes.

The exponent (r(d)) should depend only on (d), not on the task. Task dependence
belongs in (C_{\rm task}). No (n)-dependent data, activation, gap, label, or
“fixed-task” constant may be used.

## 2. What total size must count

The study README has the right coordinate-level rule. The following inventory makes
it operational. Count every retained, task- or realization-dependent real coordinate
in:

1. the restart state, including residual, clock, memory, or auxiliary variables;
2. all moving first-layer, hidden-mixer, and readout coordinates;
3. fixed selected neurons, dictionaries, metrics, bases, quadratures, mixers,
   preconditioners, right inverses, and correction tensors;
4. every coefficient needed to specify the autonomous vector field;
5. every coefficient needed by the decoder at an arbitrary query (x);
6. the training data if it is required after initialization, or the data-dependent
   quantities into which it was compiled;
7. any retained table, spline, polynomial, program constant, seed, or other object
   that depends on the task, (n), or the realized dense initialization.

A fixed activation formula and one dimension-uniform algorithmic rule need not be
counted. Temporary dense arrays and quadrature work may be discarded and need not be
charged as retained size, but their information cannot survive in an uncounted
data-dependent decoder or in a program generated specially for the instance.

**Sourced fact.** The integrated result counts all retained compact coordinates and
gives storage (O([\log(en)]^{3d+2})) at fixed task. The source bridge obtains a
source rank (A_n=O([\log(en)]^{3d/2+1})), selects at most (9R) coordinates per
layer, and then incurs quadratic mixer/metric storage. It also states that dense
arrays, source vectors, jets, and quadratures are discarded, and that the runtime is
the corrected-readout autonomous optimizer with its own residual rather than replay.
Thus the existing construction is a valid baseline coordinate inventory, but its
logarithmic exponent is linear in (d), not (o(d)).

### A stable representation class for a lower bound

Counting exact real coordinates alone is insufficient. A useful lower-bound class is:

\[
 E_n:\mathcal K_{n,\tau_d}\to\Theta_n\subset\mathbb R^p,
 \qquad \dot s=V_{n,\theta}(s),\qquad
 G_n(\theta)(t,x)=D_{n,\theta}(s_\theta(t),x),
\]

where (E_n) is the initialization/task encoder and (G_n) is the full trajectory
decoder. Require:

- a specified norm on \(\Theta_n\), a bounded encoder image of diameter (B_n), and
  Lipschitz (or quantitatively Hölder) (E_n);
- existence, uniqueness, and restartability of the flow on a stated invariant set;
- quantitative conditioning of (V_{n,\theta}), its parameter dependence, and
  (D_{n,\theta}), strong enough that \(\theta\mapsto G_n(\theta)\) is
  (L_n)-Lipschitz in the complete trajectory sup norm;
- a complexity rule such as
  \(\log(B_nL_n)=O_{\tau_d}(\log(1/\varepsilon_n))\), or else an explicit charge for
  \(\log(B_nL_n)\). All-time stability needs dissipativity or a uniform flow estimate,
  not merely a finite-horizon Gronwall bound.

**Derivation.** If every element of a target set \(\mathcal K\) is approximated to
error \(\varepsilon\), a Euclidean covering of the encoder image gives

\[
 H_{2\varepsilon}(\mathcal K)
 \le p\log\!\left(1+{cB_nL_n\over\varepsilon}\right),
 \qquad
 p\ge {H_{2\varepsilon}(\mathcal K)\over
 \log(1+cB_nL_n/\varepsilon)}.                 \tag{1}
\]

This elementary inequality is the appropriate bridge from entropy to retained real
coordinates. If (L_n) is unrestricted, it also shows exactly how ill-conditioning
can hide information and destroy the lower bound.

## 3. How to certify nonlinear feature learning

“The hidden arrays are updated” is not enough: motion can be a gauge symmetry,
vanish below the comparison scale, or have no causal effect on the predictor. Use
three separate claim levels.

1. **Functional feature motion.** Define the retained hidden feature maps
   (H_C^{(\ell)}(t,\cdot)). Modulo only explicitly identified neuron symmetries,
   prove for some \(\ell\le L\) and some time interval
   \[
   \sup_t\inf_{g\in\mathcal G}
   \|H_C^{(\ell)}(t,\cdot)-gH_C^{(\ell)}(0,\cdot)\|>0,
   \]
   preferably with a lower bound exceeding the target error scale.
2. **Mechanism change.** Prove that a feature Gram or tangent kernel changes by a
   quantified amount and that the changed part enters the predictor velocity. This
   excludes a mere reparameterization of one fixed kernel.
3. **Causal necessity for the proposed witness.** Clamp the hidden-feature components
   while keeping the same initialization, decoder, readout law, clock, and legitimate
   nuisance parameters. Show that this matched frozen-feature ablation misses the
   dense trajectory by more than the claimed tolerance. A statement that *no*
   frozen-feature model can succeed is stronger and requires a lower bound over that
   entire comparison class.

**Inference from the integrated artifacts.** The corrected compact runtime is
autonomous and evolves hidden arrays, so it supplies structural feature motion as a
candidate. The two supplied integrated files do not contain the quantitative
non-gauge lower bound or matched frozen-feature separation above. Therefore they do
not, by themselves, certify “feature learning is essential” in the strong sense of
the new study.

## 4. Primary literature and what it actually implies

### Analytic entropy and widths

- **Sourced fact.** Kolmogorov and Tikhomirov proved that the uniform metric entropy
  of a bounded holomorphic class in (s) complex variables, restricted to a smaller
  compact domain, has order
  \(H_\varepsilon\asymp[\log(1/\varepsilon)]^{s+1}\) under their regularity
  hypotheses. See A. N. Kolmogorov and V. M. Tikhomirov,
  [“\(\varepsilon\)-entropy and \(\varepsilon\)-capacity of sets in function
  spaces,” *Uspekhi Mat. Nauk* 14(2), 3--86 (1959)](https://www.mathnet.ru/eng/rm7289).
  This is a generic analytic-ball result, not a neural reachability theorem.

- **Sourced fact.** Chen and Wang determine approximation numbers, including their
  dependence on dimension, for Sobolev and Gevrey-type embeddings on spheres and
  balls into (L_2). For a fixed intrinsic dimension (s), the analytic member of
  their spectral scale has stretched-exponential linear widths of the form
  \(\exp[-\Theta_s(N^{1/s})]\); their paper also treats the important
  preasymptotic regime (N\lesssim2^s), where fixed-dimension asymptotics are
  misleading. See J. Chen and H. Wang,
  [*J. Complexity* 50 (2019), 1--24](https://doi.org/10.1016/j.jco.2018.08.002),
  [arXiv:1701.03545](https://arxiv.org/abs/1701.03545).
  Their sphere is denoted (S^s\); the present input sphere (S^{d-1}) has
  (s=d-1). Their error norm is (L_2), not the present supremum norm.

- **Sourced fact.** Aleans and Tozoni obtain order-sharp Kolmogorov-width estimates
  in several regimes for multiplier classes on complex spheres, including analytic
  multipliers \(\lambda(k)=e^{-\gamma k^r}\) with (r\ge1). See D. J. Aleans and
  S. A. Tozoni,
  [“Estimates for (n)-widths of sets of smooth functions on complex spheres”
  (2019)](https://arxiv.org/abs/1903.06843). This corroborates the spectral
  dimension mechanism but concerns a complex sphere and static multiplier balls.

- **Derivation.** Apply Kolmogorov--Tikhomirov locally to a fixed-radius analytic
  atlas on (S^{d-1}). A generic static class has
  \(H_\varepsilon\asymp[\log(1/\varepsilon)]^d\). Combining with (1) and
  \(\log(B_nL_n)=O(\log(1/\varepsilon))\) gives
  \(p\gtrsim[\log(1/\varepsilon)]^{d-1}\). Allowing one freely varying analytic
  time coordinate raises these powers to (d+1) and (d), respectively. At
  \(\varepsilon_n\asymp n^{-1/2}[\log(en)]^{-5/2}\),
  \(\log(1/\varepsilon_n)=\Theta(\log n)\).

- **Inference.** This is the correct generic obstruction scale and explains why
  spherical-harmonic truncations naturally have a log exponent proportional to
  (d). It is **not** a lower bound for the present reachable set until a stable
  analytic ball or comparable packing is embedded in the dense training
  trajectories with the required probability and task constraints.

### Stable nonlinear and neural/ridge approximation

- **Sourced fact.** Cohen, DeVore, Petrova, and Wojtaszczyk define stable manifold
  widths using Lipschitz encoders and decoders and prove entropy inequalities for
  them. See [“Optimal Stable Nonlinear Approximation,” *Found. Comput. Math.* 22
  (2022), 607--648](https://doi.org/10.1007/s10208-021-09494-z),
  [arXiv:2009.09907](https://arxiv.org/abs/2009.09907). Their formalism is the
  closest off-the-shelf model for excluding arbitrary real encodings, but it does
  not impose autonomous dynamics or prove the entropy of this reachable set.

- **Sourced fact.** DeVore, Howard, and Micchelli introduced a continuous
  encoder/decoder manifold width and computed it for Sobolev balls. See
  [“Optimal nonlinear approximation,” *Manuscripta Math.* 63 (1989),
  469--478](https://doi.org/10.1007/BF01171759). Continuity is topological control;
  the newer stable widths add quantitative conditioning.

- **Sourced fact.** Maiorov proved that the worst-case (L_2) error of sums of
  (N) arbitrary ridge functions on the Sobolev ball (W_2^{r,d}) has order
  \(N^{-r/(d-1)}\). See V. E. Maiorov,
  [“On Best Approximation by Ridge Functions,” *J. Approx. Theory* 99 (1999),
  68--94](https://doi.org/10.1006/jath.1998.3304). This is a sharp curse-of-
  dimensionality result for a shallow static class, not for a depth-(L\) autonomous
  trained trajectory and not for an analytic reachable class.

- **Sourced fact / warning.** Maiorov and Pinkus constructed a special analytic,
  monotone sigmoidal activation for which a two-hidden-layer network with a fixed
  finite number of units can approximate every continuous function on a compact
  domain arbitrarily well. See V. Maiorov and A. Pinkus,
  [“Lower bounds for approximation by MLP neural networks,” *Neurocomputing* 25
  (1999), 81--91](https://doi.org/10.1016/S0925-2312(98)00111-8). This does not
  match the canonical activation assumptions and is not a stable uniform
  construction. It is direct evidence that neuron/real-coordinate counts without
  activation-specific and stability restrictions can be vacuous.

- **Sourced fact.** Bölcskei, Grohs, Kutyniok, and Petersen connect metric entropy
  to lower bounds on connectivity and memory for deep networks with quantized,
  controlled weights. See
  [“Optimal Approximation with Sparsely Connected Deep Neural Networks”
  (2018)](https://arxiv.org/abs/1705.01714). Their bit/weight restrictions are a
  useful alternative to Lipschitz widths, but their target classes and (L_2)
  static approximation problem differ from the present one.

**Literature conclusion.** These results justify the proposed stability contract
and the expected generic exponent. None supplies the missing reachable-trajectory
packing, whole-sphere sup norm, complete time interval, canonical deep gradient
flow, or initialization-conditioned autonomous representation. Known results do
not answer “yes” or “no” for the exact requested class.

## 5. Loophole audit

| Loophole | Why it invalidates a claim | Required closure |
|---|---|---|
| Infinite-precision real | One coordinate can encode an arbitrary table or trajectory. | Lipschitz/Hölder encoder and full-flow decoder with charged condition number, or explicit bit precision/quantized weights. |
| Clocked playback | Adding \(\dot u=1\) makes any stored nonautonomous trajectory formally autonomous. | Count the trajectory-specific decoder/forcing and require it be produced by the allowed dimension-uniform rule from retained state, not future target values. |
| One realized trajectory | A scalar clock plus (D(u,x)=f_{n,\omega}(u,x)) “compresses” one path only by hiding it in (D). | Uniform encoder/decoder class over a positive-probability set of initializations; all data-dependent decoder coordinates counted and stable. |
| Finite training set | Matching (m) residual coordinates says nothing about the supremum over the sphere. Full input span is not a norming set for unrestricted analytic functions. | Whole-sphere bound, or a proved bandlimit/analytic norm that makes a stated sample set norming. |
| Initialization-dependent dictionary | Instance adaptation is legitimate, but it can hide the dense model in selected atoms, metrics, or a seed. | Encoder uses only permitted initialization/data; every selected atom and coefficient is retained and counted; stability and a high-probability size bound are uniform in \(\omega\). |
| Uncounted generated code | A “fixed rule” generated separately for each task can contain an arbitrary table. | Only one task-independent algorithm is free; generated constants/code are descriptor coordinates or bits. |
| Merely moving weights | Gauge motion or (o(\varepsilon_n)) feature motion can coexist with a frozen effective kernel. | Functional-motion, kernel-change, and matched-ablation certificates from Section 3. |
| Compact-time only | A finite-horizon flow estimate does not cover the fitted endpoint. | Uniform dissipative/restartable all-time flow and continuous endpoint decoder. |
| Generic analytic lower bound | The analytic ball may be vastly larger than the reachable network set. | A packing inside reachable trajectories, with the same task assumptions and probability mode. |
| Worst-case rare initialization | A packing made of zero-probability or exponentially rare initializations does not contradict a (1-\delta) compressor. | Packing/entropy on a set carrying probability (>\delta), or a distributional rate-distortion lower bound. |
| Hidden (n)-dependence | (C_{\rm task}), the task itself, or the sufficient-width threshold can encode an (n)-dependent cost. | Freeze tasks before (n\to\infty); display all dependencies and use constants uniform in (n). |

## 6. The decisive missing lemma

For a negative result, the highest-leverage target is a **reachable packing lemma**.
For some admissible task family, construct a set \(\mathcal P_{n,d}\) of dense
initializations with nonnegligible Gaussian probability such that their complete
trajectories are pairwise separated by (c\varepsilon_n) in the study norm and

\[
 \log |\mathcal P_{n,d}|
 \gtrsim [\log n]^{d-o(d)}\log n.
\]

Equation (1) would then force (p\gtrsim[\log n]^{d-o(d)}) for bounded-condition
representations. A packing only of arbitrary analytic functions is insufficient.
An endpoint-only or training-sample-only packing is also insufficient unless it is
already separated in the full norm.

For a positive result, the corresponding decisive lemma is a reachable-structure
theorem: prove that every high-probability trajectory belongs to a stable model
class whose entropy after division by one scalar-quantization factor is
\([\log n]^{o(d)}\), and realize that class by a counted autonomous nonlinear
state. Merely improving the harmonic counting constant or one of the two quadratic
storage factors cannot change a linear-in-(d) log exponent.

## 7. Process limitation

The required `explain-with-canonical-notation` skill at
`/home/amir/.codex/skills/explain-with-canonical-notation/SKILL.md` was inaccessible
to this scoped agent (`Permission denied`). I therefore followed the visible
`docs/notation.qmd` contract directly. No other study or route output was read.
