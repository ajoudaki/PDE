# Fixed two-hidden-layer practical global-limit program

2026-09-08. **Research stopped at the user's explicit request.** The user initially authorized pursuing route 1 to resolution, then instructed: "please stop and make sure all results are stored in a persistent doc". The target below records the historical contract; it is not authorization to resume. See [PERSISTENT_HANDOFF.md](PERSISTENT_HANDOFF.md). No numerical experiments, publication, or external messages were performed for this program.

## Fixed target

There are three fixed inputs x_i in R^d with ||x_i||^2=d and -1+delta < x_i^T x_j/d < 1-delta for i!=j, 0<delta<1, and binary labels. Singular input Grams are admitted. L=2 counts hidden layers.

The principal concrete activation is

    phi(z) = (3/4)(1+z) + (1/4) tanh(z).

It is the literal convex mixture with epsilon=1/4, fixed independently of separation, width, dataset and training horizon. It satisfies 3/4 <= phi' <= 1, |phi''| <= 1/2, and affine growth with bounded nonlinear part. No large gain or horizon-dependent perturbation is admissible. Another explicit activation with fixed, comparably moderate coefficients can be considered only with its distinction stated, preserving the intended nonlinearity requirement; a tiny existence-only coefficient does not meet the practical target.

Finite model:

    z_i = W x_i, h_i = phi(z_i), v_i = A h_i,
    k_i = phi(v_i), f_i = <C,k_i>_n,
    r_i = f_i-y_i, E = (1/2) sum_i r_i^2,
    b_i = phi'(v_i) C, q_i = A^T b_i, d_i = phi'(z_i) q_i.

Initial entries independently satisfy W_jk~N(0,1/d), A_jk~N(0,1/n), C_j~N(0,n^(-2)). The finite small random readout is retained. The raw metric is

    (d/n)||Delta W||_F^2 + ||Delta A||_F^2 + ||Delta C||_n^2.

The true raw GF is

    dot W = -(1/d) sum_i r_i d_i x_i^T,
    dot A = -(1/n) sum_i r_i b_i h_i^T,
    dot C = -sum_i r_i k_i.

For joint algorithm conclusions raw GD is simultaneous Euler for this exact field with physical step n^(-2), linearly interpolated parameters and recomputed hidden fields.

## Population and convergence conclusion

Use the canonical Gaussian layer action spaces and genuine adjoints constructed from the actual finite Gaussian programs, not arbitrary substitute bounded operators or an easier mean-field architecture. With w=sqrt(d)W and u_i=x_i/sqrt(d), the population state is (w,A0+U,C), where w is in L2(Omega1;R^d), U is Hilbert-Schmidt from H1 to H2, and C is in H2. Its raw norm is the sum of squared Hilbert norms. Initially w is standard Gaussian, U=0, C=0. Finite initialized operators need not be Hilbert-Schmidt in the population limit.

Prove a global autonomous strong population raw GF, uniqueness among bounded-primal strong competitors on compact intervals and continuation from every reached state. For each finite T, prove full-sequence actual finite-width GF convergence in probability, uniformly in training time, jointly for predictions/loss, all three true kernel blocks, and same-layer field path laws in W2. Retain the earlier actual raw-GD joint limit and true velocity/second-moment/integrated-speed observables as part of the full bridge where available; these must not be silently claimed from primary forward convergence.

Kernel blocks are Gamma_ij <d_i,d_j>, <b_i,b_j><h_i,h_j>, and <k_i,k_j>. Genuine feature training and quantitative initial nonaffinity should be documented for the fixed activation. Uniform-in-time positive nonaffinity, a positive all-time kernel floor, exponential fitting, and a finite all-time residual clock are stronger optional statements, not the main target. Do not trade the fixed activation for one chosen separately for each T.

The population construction and actual finite algorithms must agree. A Galerkin subsequence without canonical strong identification, a clipped training theorem without cap removal, or an existence theorem without the named joint limit does not resolve the step.

## Proof discipline

The exact finite energy identity supplies raw displacement <=sqrt(T E(0)); by itself it supplies neither strong population compactness nor ambient L2 Lipschitzness. Sources, repeated Gaussian matrices, current return coefficients, true adjoints, and physical residual feedback must be retained. Arbitrary bounded-control ascent may blow up and cannot replace physical training.

Internal lemmas must have explicit statements and proofs. Specialized external results require full-text and proof verification, with assumptions checked against this exact model; further dependencies must be followed where needed. Existing local proofs are starting material, not authority for an unproved extension.

A full candidate remains provisional until diversified fresh isolated reviewers each read only the whole self-contained report. Repair substantive objections and repeat with fresh isolated readers until all assertions pass. A rigorous negative result must address the target, not merely a failed proof route. Do not label an unclosed conditional argument a resolution.

## Initial approach registry

1. Direct single-Gaussian-matrix source/Volterra estimates on energy-stopped physical paths.
2. Deterministic reachable-state stability, energy-preserving approximation, curvature decay and Osgood/strong compactness.
3. Finite-width Gaussian cavity/row sensitivity estimates giving joint tails and a direct comparison limit.
4. Root: reconcile exact L2 source chronology, inspect genuinely applicable primary literature, integrate and adversarially test concrete outputs.

The three workers begin independently. Cross-pollination follows concrete mathematical outputs. The decisive missing lemma is a global compact-time source-tail or direct Cauchy/stability bridge for this fixed activation; it is not assumed.
