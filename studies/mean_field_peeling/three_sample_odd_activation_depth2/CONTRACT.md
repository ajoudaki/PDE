# Three inputs and two hidden layers: research contract

2026-09-08. The user requests an analogue of the preceding explicit
polynomial activation threshold, now at L=2 with three samples satisfying
absolute pairwise cosine separation. New mathematical proof search and
adversarial checks are authorized; no experiments or old-file edits.

L continues to count hidden layers. The architecture is
z_i^1=W^1 x_i, h_i^1=phi(z_i^1), z_i^2=A h_i^1,
h_i^2=phi(z_i^2), f_i=<C,h_i^2>_n. Use
phi(z)=(1-theta)z+theta atan(z), 0<theta<=1/2,
||x_i||^2=d, |x_i^T x_j/d|<=1-delta, 0<delta<=1,
and arbitrary binary labels. Initialization, raw metric and exact
simultaneous raw GD step n^-2 remain as in the previous theorem:
W^1 entries N(0,1/d), A entries N(0,1/n), finite C entries N(0,n^-2),
metric (d/n)||dW^1||_F^2+||dA||_F^2+||dC||_n^2.
The loss is one half the sum of three squared residuals.

The target is one activation threshold depending only on delta, ideally
theta<=c delta^p, that proves the complete global canonical strong
population/GF/raw-GD theorem: uniqueness including nonsymmetric bounded
primal competitors, reached-state restart, both adjacent action
orientations and genuine adjunction, all three raw kernels, compact-time
full-sequence width limits, same-layer path and velocity W2 limits,
second moments and integrated speeds, activation nonaffinity and initial
feature motion. Training-loss conclusions must explicitly state their
dependence on theta. A theta-dependent rate is admissible for a similar
result; disproving a theta-independent rate does not settle the target.

Width is taken for each fixed dataset and finite horizon. The finite
random readout is retained before taking its zero population limit.
One hidden layer, a different large-gain activation, an offset, frozen
hidden weights, noisy GF, a different mean-field normalization, or
assuming a positive input-Gram eigenvalue are not substitutions for this
question. Pairwise separation permits singular three-input Grams.

Initial Gram positivity, finite-dimensional GF existence, conditional
population identities and failures of the affine proof method must be
kept separate from the complete population theorem. A failed proof
route is not a counterexample at positive theta.

Parallel routes: L2 source-tail/energy continuation; initialization
geometry and necessary dynamics scales; nonlinear reference or trained
Gram structure. Root reconciles exact results and audits the full chain.
