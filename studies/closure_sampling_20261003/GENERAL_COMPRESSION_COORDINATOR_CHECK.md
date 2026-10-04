# Coordinator reconstruction of the general analytic compression chain

2026-10-03. Internal research check. This is neither an isolated promotion
review nor an established-book theorem. The coordinator read every source
named below completely before relying on it. The final version table and
completed check status appear below.

## 1. Scientific context and source boundary

This continues `closure_sampling_20261003`, whose completed two-input
theorem supplies the representation and setup contract. The user explicitly
authorized the current manuscript and relevant prior proofs in
`dense_cutoff_population_rate_20261001`. No other study is a scientific
input. The current manuscript, included mathematical proofs, captions,
book entry and notation contract were read in the preceding continuation;
their unchanged relevant hashes were verified again. Current AGENTS and
Part 1 of the research workflow were reread. The canonical-notation and
neural reference, rigorous-proof skill, conjecture-investigation skill
and its required research/audit/orchestration references were applied.

The three axis attempts began in fresh scoped contexts and froze separate
outputs before reading each other's work. The depth route's first artifact
was written before receiving the coordinator's prior-carrier teaser; its
hash was recorded afterward, with no intervening scientific read or edit.
The later deep source proof is explicitly a collaborative development,
not an independent attempt. Checks are internal collaborative
reconstructions, not blind promotion reviews. The activation checker
received the coordinator's preliminary assessment during reconstruction;
its source-specific report records its own derivation. No claim of reviewer
isolation is made.

The complete authorized prior finite-depth input is
`../dense_cutoff_population_rate_20261001/DEPTH_CAVITY_ROUTE.md`,
with its complete `DEPTH_INSERTION_CHECK.md` and
`DEPTH_CAVITY_PROBABILITY_CHECK.md`. Only the bounded-activation
finite-network carrier/insertion theorem is used. Later historical
unbounded-activation discussion in those reports supplies no assumption
or missing step here. No population-training comparison is imported.

## 2. Normalization and quantifiers

The original model has all hidden widths equal to $n$, independent
Gaussian first entries of variance one, hidden entries of variance $1/n$,
zero readout, squared mean loss, and mobilities $(n,1,\ldots,1,n)$.
In mobility coordinates $(A,\sqrt n W^{(2)},\ldots,w)$ the physical
flow is $-(2/m)\sum_a r_a\nabla(nf_a)$. This gives $2/(mn)$ in
each original hidden weight equation, and $2/m$ for first weights and
readout. No residual clock or rescaling of elapsed time is substituted.

The bridge and joint assembly write $c_a=y_a-f_a$. The depth and
activation supplement sometimes put the factor $2/m$ into $c_a$;
their equations display that definition. The maps called $R_b$ in the
deep source are residual-free derivatives in the direction
$\nabla(nf_b)$, not velocities. Their physical velocity contribution
is $-(2/m)\sum_b r_b R_b$. These conventions agree exactly.

The joint result fixes $m,d,L$, activations, data and sufficiently small
labels before taking width large. Every label sign and ratio is allowed.
It uses the existing initialized Gram gap; the gap is proved automatically
for nonconstant bounded analytic activations and pairwise nonproportional
nonzero inputs. No orthogonality is required for the joint theorem.
The error norm is the supremum over all physical time and the full fixed
input sphere. Fixed confidence is obtained from events with probability
tending to one; it is not an event covering all widths at once.

The resource is total retained exact-real coordinates after finite setup.
It includes all smaller learned matrices, first weights, readout, masses,
and fixed data. It excludes setup arithmetic, temporary memory and bit
precision, as the accepted two-input theorem did. This is a dense-route
neuron compression, not a claim that the unchanged $q$-closure has been
resampled or that a population width-bias term has been controlled.

## 3. New source proof: checks of the potentially circular steps

The finite-network real carrier estimate alone is insufficient: a hidden
row can turn an RMS forward velocity into a coordinate velocity larger by
$\sqrt n$. The new proof addresses that row action directly.

For a prefix at level $p$, the forward response is
$Q_b^{(p)}=D h^{(p)}\nabla F_b$, where $F_b=nf_b$. Differentiating
gives $D Q_b^{(p)}=D h^{(p)}D^2F_b+D^2h^{(p)}[\cdot,\nabla F_b]$.
The mixed forward recursion has a diagonal of $R_b^{(p)}$ and only
responses from lower levels. Its mixed matrix terms carry $1/\sqrt n$;
their operator norms are bounded by the RMS of the relevant response.
The normalized Schatten-2 estimate uses RMS, whereas higher Schatten
estimates retain the carrier budget and the lower response maximum.
The response at level $p+1$ does not occur in this derivative estimate.

Removing an incoming row at level $p+1$ yields three endpoint terms:
the state variation, the omitted outgoing-column source, and the direct
reverse source $D h_v(D h_b)^\top y\,\delta_{b,i}$. Pairing with the
incoming Gaussian row $y$ leaves a direct trace and a history trace
containing $D Q_b^{(p)}J(D h_a)^\top$. The first costs the carrier
maximum. The second contains two endpoint factors and $h$ residual
Hessian factors in its $h$-th Dyson term. Normalized Schatten Holder
with exponent $h+2$ cancels the normalization even though parameter
dimension is $O(n^2)$. Its only response maximum comes from lower layers.
The exterior factor is residual activity times the omitted response.
This yields an upward, triangular polylogarithmic recursion. The angular
recursion uses the same calculation without the direct reverse observable
term. No future-layer maximum is hidden in a constant.

The additional observables require additional deletion sources. In
particular, differentiating a deleted outgoing contribution gives
$W_{:,i}Q_{b,i}$ and
$\delta_b^{(j+1)}h_{b,i}^{(j)}h_i^{(j)}(x)/n$.
The latter has ordinary Euclidean norm $O(n^{-1/2})$ times fixed
constants; it must not be dropped algebraically. The angular source is
$W_{:,i}\partial_\theta h_i$. The local augmented graph in
`DEEP_ACTIVATION_EXTENSION.md` explicitly includes these sources.
At a top-layer deletion the extra prediction offset is $w_i h_i/n$;
both its ordinary-gradient force and its product with the reverse force
are retained. Its cavity uses its own residual.

The nonlinear graph is acyclic: ordinary forward nodes, backward nodes,
then residual-free forward responses, then angular responses. On the
uniform Gaussian linear event a vector first variation has coordinate
maximum $n^{-1/10}$ and Euclidean norm $n^{1/100}$, up to fixed
logarithmic factors. Products use one maximum and one Euclidean norm;
matrix cross terms retain $1/\sqrt n$; a normalized scalar pairing
times an RMS-bounded response cancels its possible $\sqrt n$ loss.
Reference carrier/response diagonals cost only fixed logarithmic powers.
The largest nonlinear powers at remainder cap $u=n^{-1/25}$ are
$n^{-0.08}$ and $u^2=n^{-0.08}$. Propagation by $n^{1/1000}$ and
integration over $O(\log n)$ leave a strict margin. Forward expansions
also justify the complex joining segments used for gate Taylor formulas.

Every complex terminal is reached by a real segment followed by a short
vertical segment. The negative gradient-Gram propagator is contractive
only on the real part; on the vertical part its norm is bounded by
$e^{Cr}$. In each Dyson term the total vertical length, rather than the
number of insertions, determines that cost. The controls are Lipschitz
functions on this one-dimensional contour. Their net entropy has power
$n^{5/8}$ up to logarithms, below the Gaussian exponent $n^{0.79}$.
Gridding the fixed number of terminal and query coordinates adds only
$O(\log n)$ entropy. No two-dimensional control-function net is used.

Each cavity stops on its own retained-initialization domain. Comparison
on the common prefix transfers all carrier, pole and response margins
to its doubled caps, proving that it survives the full-model prefix.
No Gaussian law is conditioned on full-model survival. The independent
cavity references have real activity-modulus Gaussian moments. Their
short vertical increments have vanishing normalized radius and a
two-parameter polynomial-logarithmic covering bound, so their extra
Gaussian exponential moments are uniformly bounded. Fixed-block moment
expansion then removes the exponential carrier budget: choose budget
first, labels small second, take width large at each fixed moment degree,
then take the infimum over those degrees. No growing-deletion estimate
is assumed. The resulting strip radius is $c\log(en)^{-(L+4)}$.

## 4. Source spaces and full feedback comparison

The complex source theorem covers forward activations and both initialized
matrix orientations, plus every training backward response including the
first layer. Polynomial-logarithmic strip width and source magnitude,
with horizon $C\log n$, give tensor degree
$O(\log^{L+6}n)$ in time and $O(\log^{L+5}n)$ in each of $d-1$
angles. A possibly enormous finite list of initial time derivatives,
continued by the explicit disk map, computes those coefficient vectors
without trained snapshots. All angular operations use finitely many real
query nodes. Real and imaginary coefficient parts yield real source spaces.
Paired scalar operations preserve the exact initialized forward/transpose
matrix images. The resulting dimension per layer is
$R=O(\log^{d(L+5)+1}n)$.

Positive cubature matches the constant and basis products with at most
$1+R(R+1)/2$ selected neurons per layer. Their basis maps are isometries,
so projected mixers inherit operator bounds and exact actions on paired
sources. Initialized training features and their Gram are matched exactly.
After setup only small matrices and masses remain; storing their dense
entries costs $O(R^4)$, including fixed coordinates. There is no hidden
original-width decoder or retained basis array.

The weighted model has its own small-label fitting proof with constants
independent of node count and minimum mass. The actual tangent-Gram
residual difference equation damps the integrated residual difference.
One-reference backward subtraction multiplies changed gates by true
selected original carriers. It yields error at most
$C(1+M)e^{CM}\epsilon$, with original $M=O(\sqrt{\log n})$.
Choosing $\epsilon=n^{-1/2}e^{-D\sqrt{\log n}}/\log n$ absorbs
this amplification while leaving $\log(1/\epsilon)=O(\log n)$ and
therefore the same source dimension. The two independent exponential
prediction tails extend the same-physical-time comparison to the endpoint.
All selection and feedback errors are included; no population or
sampling-bias term is omitted.

## 5. Activation and feature-motion boundaries

The all-layer activation replacement uses bounded holomorphy on a fixed
strip, real values on the real axis, and Cauchy derivative bounds on a
narrower strip. No first-layer inverse, oddness, positive slope, or
everywhere nonzero slope is used. The class includes nonmonotone sine.
It does not include every bounded-$C^3$ function, and no generic smooth
polylogarithmic approximation estimate is being asserted.

The prefix energy identity in the activation supplement certifies nonzero
feature curvature in every layer for linearly independent training data,
nonconstant analytic activations, and nonzero labels. The supplement states
it for orthogonal inputs; the assembly proves the linearly independent
extension by the full column rank of the input matrix. The identity itself
does not require orthogonality. Finite additional initialized reverse
vectors preserve this certificate after cubature. Its claim is exact
nonzero feature motion, not a width-independent magnitude lower bound at
arbitrary depth. The earlier two-layer theorem retains its stronger
motion lower bound in its original scope.

## 6. Administrative verification

No experiment was run. No paper, maintained book/code, other study, index,
commit or remote was changed by this continuation. The preexisting dirty
paper PDF and unrelated study README were preserved. The proof files and
complete mathematical reconstructions are the reproduction evidence.
Finite-precision implementation and efficient preprocessing remain open.

Static checks found no control characters, unmatched display delimiters,
or missing local Markdown links in the new main proof, source, comparison,
result and check files. The sample-count route's inline-math formatting was
repaired separately without changing its mathematics. `git diff --stat`
still showed only the two preexisting tracked changes, and
`git diff --cached --stat` was empty. No scientific source was retrieved
from another unauthorized study.

## 7. Final versions and conclusion

The complete source, activation extension, comparison and assembly have
each passed the reconstructions identified above. The coordinator read
all reports, including their final-version confirmations, and reconstructed
the whole chain. The named source theorem in the assembly is supplied by
the separately checked finite-network proof; it is not an added assumption.
The joint bounded-analytic, fixed-$m,d,L$, small-label compression theorem
is therefore **internally checked**, with its stated exact-real resource
contract and probability quantifiers. Promotion has not been requested or
performed.

| Source or report | Final SHA-256 |
|---|---|
| `GENERAL_ANALYTIC_COMPRESSION.md` | `4fd314dd28367430cd60fa8b88fe0eb4d9b12f575c61aadd60ff61dff76dec53` |
| `GENERAL_ANALYTIC_COMPRESSION_CHECK.md` | `f6c667a28ad2c3b0ac9f0b63f8306384157e5baedeec127d1e8fad25e9d63a9c` |
| `GENERAL_WEIGHTED_COMPARISON.md` | `1dcb779135b616aa66be4cd830d2bd2f3217a56eeae8f3cdf7394a52262a4306` |
| `GENERAL_WEIGHTED_COMPARISON_CHECK.md` | `3f2342f18edce87fc27832ce67b11cb36bd85877b16318c6ba692a7a58e7b176` |
| `DEEP_COMPLEX_SOURCE.md` | `7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2` |
| `DEEP_ACTIVATION_EXTENSION.md` | `b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141` |
| `DEEP_COMPLEX_SOURCE_CHECK.md` | `4a595068df83e3ed18389630f4e150aadadbba9a0e22cce93bf0539023872ce5` |
| `ACTIVATION_COMPRESSION_ROUTE.md` | `0e672cdbaf5ffa6909fa14986e0a7476106dcc41d96c61d5654f9fff60853e19` |
| `DEPTH_COMPRESSION_ROUTE.md` | `d5728df96ae2dc711d2aa89fbdb0590a9d1fbd6c45d48b2441b080af0f4fdf96` |
| `M_INPUT_COMPRESSION_ROUTE.md` | `75fb7a40923ecb92b9b7b9e1f346d3c99d6a16f04e2f1d89ef592ab3ff3cd84a` |
| `GENERAL_COMPRESSION_RESULT.md` | `fc5c46c5e539792d83806d69f3dc1ef210228443c3c0ba9239727e2f02416f40` |

The prior bounded-activation input is frozen at
`e8f9f43c137a9c74b751cbd2e54cf5a2b13f090c560d912b4b17994c53bc1478`;
its complete local and probability reports are respectively
`77c51e725629e736a33c16dbe4ec179b5aa859b527539815f55422a818a1e977`
and `e8ec625d60753186ee5a74e67458e1f048c7edc313dc0155de54cf193e307993`.

Current shared scientific context hashes remain:

- `paper/main.tex`: `60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95`.
- `paper/proof_alltime.tex`: `f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d`.
- `paper/proof_tracking.tex`: `e75f8122ab0ed0bc5f8c0b5f979b7e1a1b779c94440367d62d9a98892d3e53be`.
- `docs/index.qmd`: `f7a21b794e21f145ebad87fb1d7bde05f5f55e5877c92440109c1b22232b06de`.
- `docs/notation.qmd`: `78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023`.

The completed deterministic bridge alone originally identified its source
construction as missing. That historical description is superseded by the
checked deep source theorem and final assembly above. The original frozen
depth-route obstruction concerned a stronger uniform vector-field bound;
it is not a contradiction of the new theorem, which permits and absorbs
the explicitly controlled intermediate amplification.
