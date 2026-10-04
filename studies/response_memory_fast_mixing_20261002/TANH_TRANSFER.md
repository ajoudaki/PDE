# Finite-step universality for the actual tanh closure

Status: **internally checked theorem; separate internal mathematical audit
PASS** in TANH_TRANSFER_REVIEW.md. The Lipschitz-program lemma and its clipping
bridge are both checked; the polynomial corollary is not substituted for tanh.
The exact reviewed assembly is preserved as TANH_TRANSFER_REVIEW_INPUT.md.
The present update resolves its pending status and adds the review's explicit
finite-prefix and workspace clarifications. This is not promoted material.

## Exact model and theorem statement

Fix input dimension d, m training pairs (x_a,y_a), a finite query list, positive
step size eta and integer J>=0, all independent of hidden width n. Let A in
R^(n x d) be the first matrix, w in R^n the readout, H_a,D_a in R^n the raw
q=1 forward/backward moments, and tau the clock. With <u,v>_n=u^T v/n, define

    B=W0-[2/(mn tau)] sum_a D_a H_a^T,
    h(x)=tanh(Ax/sqrt(d)), g(x)=tanh(Bh(x)), f(x)=<w,g(x)>_n,
    r_a=f(x_a)-y_a, rho=sqrt(mean_a r_a²),
    delta_a=w odot (1-g(x_a)²),
    ell_a=(1-h(x_a)²) odot B^T delta_a.

B is reconstructed, never independently trained. The vector field F is

    dot A=-2 mean_a r_a ell_a x_a^T/sqrt(d),
    dot w=-2 mean_a r_a g(x_a),
    dot H_a=rho h(x_a), dot D_a=r_a delta_a, dot tau=rho.        (1)

Initialize A with iid N(0,1) entries independently of W0, w=D=0,H_a=h0(x_a),
tau=1. This is the manuscript's actual q=1 unit-forward/zero-backward-prefix
system: A=W^(1), H_a=bar h_(a,0), D_a=bar delta_(a,0), and w is its readout.
Labels are any fixed finite real numbers, including +/-1. Apply exact Heun:

    K_k=F(S_k), S_k^*=S_k+eta K_k,
    K_k^*=F(S_k^*), S_(k+1)=S_k+(eta/2)(K_k+K_k^*), k<J.      (2)

Both stage clocks remain at least1. There is no division by rho.

For n=2^b, compare the following initialized environments. Let mathsf H_n be
normalized Hadamard, s_n the midpoint quantiles of density sqrt(4-s²)/pi on
[0,2], normalized to mean square1, and Pi_U,Pi_E,Pi_V,Pi_F independent uniform
signed permutations independent of A. Set

    W0^G(i,j) iid N(0,1/n),
    W0^S=Pi_U mathsf H_n Pi_E diag(s_n) Pi_F^T mathsf H_n^T Pi_V^T.    (3)

**Theorem.** The two runs have common finite deterministic limits
in probability, as n tends to infinity through Hadamard widths, for all
predictions at the finitely many states/stages/queries, all within-layer
feature Gram entries, RMS feature displacements, and continuous functions of
finitely many such scalar averages. Bounded Lipschitz empirical tests of
same-layer retained state channels (A,H on the first layer; w,D on the second)
also qualify as specified by the clipping lemma. This does not automatically
include unbounded intermediate credit fields such as ell.
Under any coupling preserving the marginal assumptions, differences of the
two finite prediction vectors tend to zero in probability.

This is ensemble universality of a fixed numerical program. It asserts no
coordinatewise neuron matching, same-realization matrix approximation,
unbounded read-in moment convergence, finite-width error rate, continuous-time
or all-time transfer. Classification needs a limiting-margin qualification.
Fixed finite precision is separately numerical, not part of this exact theorem.

## Proof and explicit dependency boundary

**Matrix/program step.** The sampler and initialization hypotheses are proved
in POLYNOMIAL_TRANSFER.md using Wang--Zhong--Fan's generalized-invariance
classification. Gaussian and structured matrices have the same limiting
diagonal distribution. Structured operator norms are eventually at most3;
Gaussian norms are eventually at most8 by the summable two-sphere-net bound.

The extension from literal AMP to finite typed Lipschitz programs is proved
in LIPSCHITZ_PROGRAM_TRANSFER.md. It serializes matrix queries,
adds back deterministic Onsager terms inside same-side coordinate maps,
regularizes covariance degeneracies with fresh Gaussian query innovations,
and removes those innovations by stability of the RAW program. Scalar
empirical feedback must be frozen/unfrozen causally at its deterministic
limits. The complete reduction and its exact published hypotheses were checked
in TANH_TRANSFER_REVIEW.md. A polynomial-only result or empirical agreement
would not have sufficed for this step.

For literal infinite-sequence AMP notation, extend the finite noisy prefix
after its last pair by u_(t+1)=tanh(y_t), v_(t+1)=tanh(z_(t+1)), in the lemma's
AMP notation. Each newest Gaussian field has positive conditional variance
given preceding fields and its independent side roots. Its tanh therefore
cannot lie in the span of preceding messages. Both message Gram matrices
remain positive definite. This supplies an admissible infinite extension
without new side roots or any change to the finite target computation.

**Actual tanh step.** TANH_CLIPPING_REVIEW.md supplies the complete conditional
lemma, including both Heun stages and every reused first-layer velocity buffer.
For Y=max|y_a| every original or partially clipped run has

    M_(k+1)=(1+2eta+2eta²)M_k+(2eta+2eta²)Y, M_0=0,
    |w_i|<=M_J, rho<=M_J+Y,
    1<=tau<=1+J eta(M_J+Y),
    |H_ai|<=1+J eta(M_J+Y), |D_ai|<=J eta M_J(M_J+Y).

All bounds include predictor states and are independent of n and clipping
thresholds. The only unbounded product in a read-in velocity is a bounded
activation derivative times p_a=W0^T delta_a. On ||W0||<=C,
||p_a||²/n<=C²M_J². Therefore at most a fraction m C²M_J²/R² of rows have any
|p_ai|>R, without any independence assumption on this adaptive response.

Measure each read-in matrix AND stored read-in velocity in

    d_c(U,V)²=mean_i min(||U_i-V_i||²,1),

and other bounded channels in normalized Euclidean distance. Clip p only
when writing a read-in velocity. Its local error in this metric is at most
sqrt(m) C M_J/R. Bounded tanh maps are Lipschitz from d_c to feature distance;
Heun's subsequent linear buffer reuse is also Lipschitz in d_c.

Replace velocity writes from LAST to FIRST. At each write, the already-clipped
suffix ending in the finite vector of basic bounded Lipschitz empirical averages
has a finite width-independent Lipschitz constant. Choose the current threshold
after the later ones so its sparse error times that suffix constant is at most
epsilon/(2J). The resulting fully clipped program differs in that basic
observable vector by at most epsilon under either ensemble. Harmless bounded
extensions of w,H,D,tau and all bounded scalar coefficients before products
make this a globally Lipschitz typed finite program. In particular f,r,rho
and the normalized moment contractions have deterministic bounds from the
displayed state bounds; clamping their reads to those bounds changes no valid
trajectory. The read-in itself is not clamped.
The published-program step then gives common limits for each clipped program.
As epsilon decreases these common limits are Cauchy, by comparison with the
same original program. Take n to infinity first, then epsilon to zero. The
exceptional operator-norm event vanishes, giving the claimed convergence in
probability. J=0 requires no clipping. RMS observables follow by continuity
of square root, not a false Lipschitz assertion at zero.

The conditional bridge and the program-universality import are both internally
checked. Their integration proves the displayed finite-step statement. The
review treats the identified published universality theorems as external
theorem inputs; it does not claim to independently reprove all their machinery.

## Computational consequence and proper novelty boundary

The structured source stores O(n) entries. A step uses
O(mn log n+m²n+mnd) arithmetic and n d+n+2mn+1 moving coordinates, plus
O(nd+mn+m²) workspace including Heun stages. No dense n-by-n matrix is required. This is
for fixed finite m,d; sample dependence has not disappeared.

An explicitly unrolled dense training history also falls into the same
finite-program universality class. Its number of rank-one history terms
generally grows with the update count. The response-memory contribution is
that its retained moment count stays fixed through training. The candidate
therefore concerns the paper's particular autonomous learner, not exclusive
access to universality or a proof that q=1 matches unrestricted dense training.
The fast prescribed-spectrum ensemble and AMP universality are prior art.
