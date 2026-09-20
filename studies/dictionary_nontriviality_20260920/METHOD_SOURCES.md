# Primary method sources for neuron-population dictionary baselines

Date: 2026-09-20. Scope: fresh, bounded source review for this study. Scientific
inputs were the supervisor's neutral assignment and the primary papers linked
below; no other study, repository theory, or code was read. This is experimental
design support, with no numerical experiments or imported convergence theorems.
The adaptations and cost cautions below are proposals, not results of these papers
for dense tanh gradient flow. The completed file is frozen; its SHA-256 is reported
to the supervisor separately.

The strongest baseline suite separates **dictionary selection**, **coefficient
evolution**, and **nonlinear evaluation cost**. POD, Fourier features, and Nyström
select representations. Galerkin/LSPG specify coefficient evolution. DEIM changes
how a nonlinear vector is approximated and evaluated; it is not merely a change
of coordinates in the state dictionary.

## Common interpretation

For this survey only, let a population field be a vector in R^N, with entries
indexed by neurons in one specified population, and let a dictionary have r
columns. Its concrete relation to the study's complete state must be supplied by
the lead author. Euclidean formulas below apply after any chosen population-norm
weighting; do not silently mix normalized and unnormalized inner products.

A descriptor z_i in R^d must be an explicitly allowed, permutation-equivariant
summary attached to neuron i. Examples to assess are initialization parameters or
initial forward/backward probe responses. Its dimension, construction cost, and
access to data must be counted. Fourier features of the arbitrary integer label i
impose an artificial geometry. Taking all incoming weights as descriptors may
make d grow with width. Updating z_i during rollout moves the dictionary and
requires the corresponding basis-derivative terms; a frozen dictionary avoids
that additional modeling choice.

## Six primary references and read coverage

1. **Ali Rahimi and Benjamin Recht (2007), “Random Features for Large-Scale
   Kernel Machines,” NeurIPS 20.**
   [Primary proceedings PDF](https://papers.nips.cc/paper/3182-random-features-for-large-scale-kernel-machines.pdf).
   Read coverage: the full RFF method description in section 3, including the
   paired sine/cosine and random-phase constructions and Algorithm 1. Section 4's
   initial random-binning description was also inspected. The entire paper and
   convergence proofs were not audited; this is method-section access, not
   abstract-only access.

   Source method: sample frequencies from the spectral distribution of a chosen
   shift-invariant kernel and evaluate trigonometric features. Proposed adaptation:
   dictionary column j has entries cos(omega_j^T z_i + b_j), with consistent
   scaling, or use paired sine/cosine columns. Count actual columns when matching
   rank. For a Gaussian descriptor kernel, match bandwidth across comparisons.
   Formation takes O(N d r) arithmetic and an explicitly stored dictionary takes
   O(N r) memory; these are direct operation counts for the proposed adaptation.
   No target-trajectory snapshots are needed if descriptors are initialization
   data. Kernel approximation does not itself establish closure accuracy.

2. **Felix X. Yu, Ananda Theertha Suresh, Krzysztof Choromanski, Daniel
   Holtmann-Rice and Sanjiv Kumar (2016), “Orthogonal Random Features,” NeurIPS.**
   [Primary proceedings PDF](https://proceedings.neurips.cc/paper_files/paper/2016/file/53adaf494dc89ef7196d73636eb2451b-Paper.pdf).
   Read coverage: section 3's ORF construction, dimension-block convention,
   equation (2), radial scaling, and QR-generation footnote. The SORF construction
   and complete proofs were not reviewed. This is method-section access.

   Source method: Gaussian-kernel frequencies are rows of sigma^{-1} S Q, with Q
   Haar orthogonal and S containing independent chi_d radii. Use independent
   blocks when more than d frequencies are wanted. Proposed adaptation: evaluate
   those frequencies on the same neuron descriptors used for RFF. Orthogonality
   is in descriptor-frequency space; resulting neuron-index columns need not be
   orthogonal. Omitting the chi scaling changes the frequency distribution. Dense
   feature evaluation has the same O(N d r) count as RFF, plus offline orthogonal
   matrix generation. Do not infer target-dynamics improvement from the paper's
   kernel-error comparison.

3. **Miloš Ilak and Clarence W. Rowley (2008), “Modeling of Transitional Channel
   Flow Using Balanced Proper Orthogonal Decomposition,” Physics of Fluids 20,
   034103.**
   [Primary author preprint](https://arxiv.org/pdf/0707.4112).
   Read coverage: section II, “Model reduction via POD and Balanced POD,” including
   ordinary POD, weighted direct/adjoint snapshots, equations (7)–(9), output
   projection, and equation (13). Fluid experiments and the full appendix proofs
   were not reviewed. This is method-section access.

   Source method: POD takes dominant snapshot modes; BPOD forms weighted direct
   and dynamical-adjoint snapshot matrices X,Y, computes Y*X = U Sigma V*, then
   constructs trial/test bases X V Sigma^{-1/2} and Y U Sigma^{-1/2}. Proposed
   adaptation: neuron-population snapshots can supply ordinary POD. Genuine BPOD
   additionally needs a specified dynamical linearization, perturbation inputs,
   outputs, and their adjoints. Its offline costs include direct and adjoint
   solves, snapshot storage, the cross-Gram product, and its SVD. The source's
   stable linear input-output setting does not automatically describe nonlinear
   training. Network backpropagation vectors alone do not supply those dynamical
   adjoints.

4. **Alex Gittens and Michael W. Mahoney (2016), “Revisiting the Nyström Method
   for Improved Large-scale Machine Learning,” JMLR 17(117), 1–65.**
   [Primary journal PDF](https://www.jmlr.org/papers/volume17/gittens16a/gittens16a.pdf).
   Read coverage: section 2's sketching model and conditioning discussion,
   section 3.2's uniform/leverage sampling and scaling, and the adjacent
   section 3.3 guidance. The complete theoretical development and experimental
   corpus were not reviewed. This is method-section access.

   Source method: for a positive semidefinite K and column-selection sketch S,
   form C = K S, W = S^T K S, and C W^dagger C^T. Proposed adaptation: use
   K_ij = k(z_i,z_j); the landmark columns span neuron-index vectors, with a
   stable rank-truncated factorization defining the dictionary. Compare uniform
   landmarks with leverage landmarks only when leverage-information cost is
   counted. Computing N m descriptor-kernel entries avoids mandatory N^2 storage;
   orthogonalizing m landmark columns costs O(N m^2). Exact leverage scores need
   leading spectral information and are not a free alternative to POD. Fix
   bandwidth and pseudoinverse cutoff using calibration data.

5. **Zlatko Drmač and Serkan Gugercin (2016), “A New Selection Operator for the
   Discrete Empirical Interpolation Method—Improved A Priori Error Bound and
   Extensions,” SIAM Journal on Scientific Computing 38(2), A631–A648.**
   [Primary author preprint](https://arxiv.org/pdf/1505.00370).
   Read coverage: sections 1.3–1.4 on the nonlinear-evaluation problem and DEIM,
   Algorithm 1, section 2.1's QR selection construction, and section 2.1.1's
   implementation including supplied pseudocode. Complete error proofs,
   applications, and randomized-row variants were not audited. This is
   method-section access.

   Source method: nonlinear snapshots generate a basis U; pivoted QR of U^T
   selects neuron rows P, giving f approximately U(P^T U)^{-1}P^T f. Proposed
   adaptation: apply this to specified population nonlinearities, while retaining
   a separately chosen state dictionary B. Precompute B^T U(P^T U)^{-1} where
   permitted. Selection costs O(N m^2), in addition to snapshots/SVD. This is a
   hyper-reduction comparison, not a competing choice of B alone. Cheap sampled
   evaluations require checking the dependency structure; dense couplings can
   preserve width-dependent work. Monitor conditioning of P^T U.

6. **Kevin Carlberg, Matthew Barone and Harbir Antil (2017), “Galerkin v.
   Least-Squares Petrov–Galerkin Projection in Nonlinear Model Reduction,”
   Journal of Computational Physics 330, 693–734.**
   [Primary author preprint](https://arxiv.org/pdf/1504.03749).
   Read coverage: section 3.1's affine trial space, projection equations,
   instantaneous residual objective and evaluation-cost remark; section 4.1.1's
   discrete least-squares problem, weighting, and test-space equations. The
   complete time-integrator theory, error proofs, and fluid experiments were not
   audited. This is method-section access.

   Source method: for an orthonormal B and fixed offset x_*, Galerkin evolves
   a_dot = B^T F(x_* + B a); LSPG minimizes a chosen time-discrete residual in
   the same affine trial space. Proposed adaptation: compare these evolution
   rules on exactly the same admissible population dictionaries. LSPG needs a
   time-discrete scheme and iterative residual/Jacobian evaluations. Reduced
   coordinate dimension alone does not remove the cost of evaluating F or its
   projections. For explicit Euler with identity weighting, the same orthonormal
   B, and exact minimization, the two constructions coincide by direct
   least-squares algebra; that case is not an independent dynamical control.

Access limitation: all six recommended references above had primary full-text
PDF access and the explicitly listed method passages were read. None is claimed
as a full-paper review. The original 2010 Chaturantabut–Sorensen journal DEIM paper
was available here only through its publisher abstract; attempted Rice PDFs did
not open. Its algorithmic details are therefore sourced above to the accessible
Drmač–Gugercin paper, which explicitly gives the DEIM construction. No scientific
conclusion in this survey depends on secondary summaries.

## Recommended comparisons and interpretation

These are design recommendations from this review, not claims made by the cited
authors for the present network.

| Comparison | Information and purpose |
| --- | --- |
| Independent Gaussian and Rademacher neuron vectors | Initialization-only isotropic controls; O(N r) generation/storage. Include the same mandatory offset/constant modes as other dictionaries. |
| Gaussian dictionary before and after QR | Conditioning and coordinate-invariance control. For a full-rank G = Q R, ranges are identical. A projection method implemented with the correct Gram matrix must give the same represented dynamics after changing coordinates; differences need diagnosis. |
| Random tanh features on fixed neuron descriptors | Architecture-matched generic nonlinear dictionary; use the same descriptor and scale-tuning budget as Fourier features. This is a proposed control, not an RFF theorem. |
| RFF versus ORF | Same descriptor, bandwidth, actual rank, and cosine convention; changes frequency sampling while preserving a meaningful kernel target. |
| Forward POD, backward POD, and combined POD | SVD of forward vectors, network-backpropagation vectors, or their concatenation. Normalize/weight the two snapshot blocks by a declared rule so one cannot win through units alone. These are snapshot POD controls, not automatically BPOD. |
| Uniform-landmark Nyström; optionally leverage landmarks | A descriptor-dependent alternative to frequency sampling. Charge spectral information to the leverage variant. |
| POD–Galerkin and the proposed dictionary–Galerkin | Hold coefficient evolution fixed to test representation. Use the same affine-offset convention. |
| Fixed basis with full evaluation versus DEIM/QDEIM | Isolate approximation/evaluation cost from the state span. Match the extra nonlinear basis size m as well as state rank r. |
| LSPG on a selected common basis | A separate evolution-rule stress test if an implicit discretization and its solve budget are in scope. |

Report two different errors: best projection/reconstruction error on held-out
population vectors, and autonomous rollout error. Good reconstruction can coexist
with poor closure. Run the rollout from its retained state without accessing true
future vectors. If snapshots from the evaluated trajectory or its future interval
are allowed for an oracle reconstruction benchmark, label that benchmark separately
from admissible predictive closures. Withhold the tested seeds/inputs/time window
from all basis, bandwidth, rank-cutoff and block-weight tuning under the selected
information contract.

Record basis-generation cost, reference trajectories and adjoint solves,
descriptor construction, nonlinear sample count, online arithmetic, and stored
width-dependent arrays separately. Matching r alone does not match information or
cost. In a dense tanh model, P^T tanh(Ba) is cheap because it equals tanh(P^T B a),
but sampled components of a general dense, changing coupling applied to
tanh(Ba) need additional analysis. DEIM must be applied at an evaluable stage and
its precomputation/storage charged; a generic DEIM label does not establish a
width-independent implementation.

The first useful suite is Gaussian/QR, Rademacher, random tanh, RFF/ORF,
forward/backward/combined POD, and uniform Nyström, all under a common projection
and rollout rule. Add BPOD only after defining the actual dynamical adjoint
problem, and add DEIM/LSPG as separate evaluation/evolution comparisons.
