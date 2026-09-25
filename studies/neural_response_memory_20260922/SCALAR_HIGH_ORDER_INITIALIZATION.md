# Exact initialized tensors through order six

2026-09-25. This is a study-local implementation derivation for the frozen
SCALAR_HIGH_ORDER_PROTOCOL.md. It is an exact finite derivative construction
in real arithmetic, subject to floating-point error in execution. It does
not establish accuracy, stability or convergence of the truncated scalar flow.
No later dense state or label enters coefficient initialization.

## Objects and ordering

Keep the canonical three-hidden-layer tanh network, supplied NumPy parameters,
already normalized input rows, output f=c^T h3/n and mobilities (n,1,1,n).
For each training input i let g_i=B grad f_i and D_i=g_i dot grad. For an
ordered word w=(i1,...,ik), define A_w=D_ik ... D_i1 A. A subword keeps the
original relative order of its positions. Repeated indices remain separate
positions; there are no factorial divisions in A_w.

Returned T1[q]=f_q and Tp[q,b,i1,...,i_(p-2)]=(Theta[q,b])_(i1,...,i_(p-2)).
Thus T6 requires field derivatives through word length four. Only training
samples define directions; q is always passive. Every Tp is a NumPy float64
array of shape (number_of_queries,)+(number_of_training_inputs,)*(p-1).

## Exact triangular word recursion

Repeated Leibniz differentiation, without commuting any D operators, gives

    (AB)_w = sum_(S subset positions(w)) A_(w|S) B_(w|S-complement).

The same identity holds for matrix multiplication and elementwise products.
For w=(i,v), differentiating the canonical physical parameter directions gives

    (W1)_w = (delta1_i)_v U_i^T,
    (Well)_w = sum_(S subset positions(v))
                    (deltaell_i)_(v|S) (h_(ell-1,i))_(v|Sc)^T / n, ell=2,3,
    c_w = (h3_i)_v.

The differentiated hidden matrix is a sum of at most 2^(length(w)-1) outer
products: at most eight for this implementation. The initializer applies
these factors directly and never forms a differentiated n-by-n matrix.
This is exact factorization of parameter derivatives, not approximation of
the initialized Gaussian matrices. Actual matrices and transposes remain.

For each word degree, forward propagation computes zell_w from the product
rule for Well*h_(ell-1). Its empty matrix subword is the shared dense action
Well*(h_(ell-1))_w; every other term is a low-rank derivative action. The
first layer uses the constant inputs and the W1 identity above.

Write gate=1-h^2. Starting with D_i h=gate*D_i z and differentiating its
remaining ordered word gives the exact chain recurrence

    h_(i,v) = sum_(S subset positions(v)) gate_(v|S) z_(i,v|Sc).

The empty subset supplies gate0*z_w; all other terms use lower-degree
cached fields. The product rule gives gate_w=-sum_S h_(w|S)h_(w|Sc).
Complementary subsets can be paired since the componentwise product commutes;
the implementation sums the subsets containing the first position and doubles.
This does not symmetrize derivative words.

Backward propagation uses back3=c, backell=W_(ell+1)^T*delta_(ell+1), and
deltaell=gateell*backell, with the same product rule. The current word is
computed from top to bottom after its forward fields are available.

Inductively, degree-k parameter derivatives depend only on training fields
of degrees at most k-1. Current forward fields depend on previous layers,
and current backward fields depend on subsequent layers. Every other field
in these equations has smaller word degree. Consequently the recursion is
triangular and includes all derivatives of the direction g_i itself.

For h or delta, the rectangular Gram derivative is

    Gram_w = sum_S (field_probe)_(w|S)^T (field_train)_(w|Sc) / n.

Applying the same product rule to the original explicit kernel

    Theta = (U_probe U_train^T)*Gram(delta1) + Gram(h3)
              + Gram(h1)*Gram(delta2) + Gram(h2)*Gram(delta3)

produces every requested tensor with its original derivative-axis ordering.

## Implementation, storage and API

`scalar_high_order_initialization.py` exposes:

- `initialize_coefficients(params, inputs, order=6, **controls)` for training.
- `initialize_probe_coefficients(params, train_inputs, probe_inputs, order=6,
  **controls)` for arbitrary passive queries.
- `initialize_antipodal_probe_coefficients(params, train_inputs, half_inputs,
  order=6, **controls)` for the query order `(half_inputs, -half_inputs)`.

Controls include device (default cuda:0), batch_size=32, word_chunk_size=16,
max_wall_seconds=600, max_cuda_bytes=12GiB, max_rss_bytes=8GiB, and
return_metadata=False. With return_metadata=True the return is
`(coefficients, metadata)`. CPU is intended for small deterministic checks;
CUDA requests never fall back to CPU. `InitializationLimit` carries a
metadata dictionary when a wall or memory cap is reached; partial tensors
are not returned as complete results. Research callers must archive such
failures. Caps may be tightened, never raised past the memory ceilings.

All supplied float64 NumPy parameter bits are preserved on device and their
hash is checked after transfer. There are no random draws in this module.
It enables deterministic Torch algorithms, disables TF32 and uses float64.
Initialization hashes use the existing shape/dtype/bytes convention.

At order six the training cache and each probe-batch cache retain fields
h,z,delta,back,gate for ordered degrees zero through three, never degree four.
The highest degree is streamed in chunks. Highest training fields are
recomputed for each probe batch rather than storing 4096 full neuron fields.
Lower training fields are cached once. One dense GEMM applies a fixed matrix
to all columns of a word chunk; low-rank terms are processed in groups of
eight. Cached integer word plans avoid repeated host/device index transfers.
There is no self-reference retaining GPU fields after the call returns.

For n=2048,M=8,32 probes, five fields on three layers require approximately
15*2048*(32+8)*585*8=5.75 GB in the lower-field caches, plus initialized
matrices, temporary chunks, scalar tensors and allocator overhead. Leading
dense-action work scales with sum_(k=0)^(P-2) M^k: 73,585,4681 for P=4,5,6.
These are count estimates, not measured time or peak-memory guarantees.
The protocol requires measured bounded training/probe pilots first.

## Exact antipodal construction

For this bias-free network, h_ell(-u)=-h_ell(u), so f_theta(-u)=-f_theta(u)
for every parameter theta. Differentiate this identity with respect to
parameters, then apply any sequence of the same training directions D_i:
every passive Tp changes sign under u -> -u. Training directions are held
unchanged and do not become probe directions. This proves the reconstruction
for every order, not merely for initial predictions.

The antipodal API takes actual first-half input rows and defines the other
rows as their exact floating-point negatives. It does not silently identify
two approximately opposite supplied arrays. For circle grids the second-half
angles represent these antipodes; independently evaluating trigonometric
functions there can differ by rounding. The deterministic tests compare
the reconstruction against explicit full-input evaluation at every order.

## Independent algorithm and deterministic checks

The separate test-only `scalar_high_order_oracle.py` uses full dense parameter
multijets. It does not import this initializer. For w=(i1,...,ik), introduce
k distinct commuting square-zero variables epsilon1,...,epsilonk, start at
theta0, and for j=k,...,1 compose

    theta <- theta + epsilon_j*g_ij(theta).

Each operation is the exact first-order flow pullback modulo epsilon_j^2.
The full mixed coefficient of Theta is D_ik...D_i1 Theta. Evaluating g on the
current parameter jet retains every moving-direction contribution. Repeated
sample indices still have distinct epsilon variables and no extra factorial.
The oracle uses an independent Taylor polynomial of tanh in the nilpotent
increment, with the necessary ordinary Taylor factorials. It is suitable only
for small widths, not for production n=2048 initialization.

Tests cover all words through degree four for (n,M)=(3,2),(7,3), canonical
and non-negligible readouts, both algorithms against the original order-four
producer, repeated indices, derivative noncommutativity, an independent outer
direction finite difference, batching/order-prefix consistency, training
first-pair symmetry, antipodal reconstruction, resource stops and GPU/CPU
agreement. Algorithmic independence is not a claim of independent authorship
or a completed independent scientific review. Actual test outcomes and wide
feasibility measurements must be retained by the supervising campaign.

Scientific inputs read completely: scalar_aggregate_engine.py,
scalar_circle_probe_engine.py, scalar_wide_initialization.py,
SCALAR_AGGREGATE_CANDIDATE_THEORY.md, SCALAR_LONG_TIME_PROTOCOL.md,
SCALAR_WIDE_PROTOCOL.md and SCALAR_HIGH_ORDER_PROTOCOL.md. Earlier dense
adapter work also read deep_moment_engine.py, deep_circle_run.py and their
moment_engine.py dependency. Required solve-math-rigorously and
investigate-conjectures instructions/references were applied. No other
study or external scientific source supplied this construction.
