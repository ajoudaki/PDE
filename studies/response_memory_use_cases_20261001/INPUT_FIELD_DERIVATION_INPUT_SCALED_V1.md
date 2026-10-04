# Input-function moments: construction and exact checks

This is a proposed learning algorithm, not a theorem from the source paper.
The baseline correspondence below is exact. Any trajectory or stochastic
performance statement requires separate evidence.

Let x have a fixed probability law mu and label y(x). Use the paper's network
with n neurons per hidden layer, first preactivation W^(1)x/sqrt(d), hidden
preactivations W^(ell)h^(ell-1), tanh activations, and output
f(x)=w^T h^(L)(x)/n. Define r(x)=f(x)-y(x), rho=(E_mu r²)^(1/2), and backward
responses delta^(L)=w elementwise-times phi'(z^(L)) and
delta^(ell)=phi'(z^(ell)) elementwise-times W^(ell+1)^T delta^(ell+1).
The code receives rows x/sqrt(d), so its first matrix multiplication already
includes this normalization. Outer-layer mobilities are n and hidden-matrix
mobilities are one; the loss is unhalved E_mu r².

Choose C fixed real orthonormal functions psi_c in L²(mu):
E_mu[psi_c psi_d]=1[c=d]. The implementation uses an explicitly evaluated
Fourier dictionary on the uniform circle. Time modes p_j are shifted Legendre
polynomials with p_j(1)=1 and integral_0^1 p_j p_k=1[j=k]/(2j+1).
The clock tau starts at one and obeys tau'=rho. On the prefix 0<=xi<=1,
h(x,xi)=h(x,0) and b(x,xi)=0; subsequently b=r delta/rho, understood as a
history representation where rho>0, not a division performed by the algorithm.

For hidden link ell and j=0,...,q-1, define n-vectors

\[
\bar h_{c,j}^{(\ell-1)}=\int_0^\tau
  \mathbb E_\mu[h^{(\ell-1)}(x,\xi)\psi_c(x)]p_j(\xi/\tau)\,d\xi,
\qquad
\bar\delta_{c,j}^{(\ell)}=\int_0^\tau
  \mathbb E_\mu[b^{(\ell)}(x,\xi)\psi_c(x)]p_j(\xi/\tau)\,d\xi.
\]

The state consists of these vectors, W^(1), w and tau. Initialize only the
zeroth forward modes, hbar_(c,0)=E_mu[h(x,0)psi_c(x)]; all other moments are
zero. Fixed W0^(ell) is retained separately. Reconstruct

\[
W^{(\ell)}=W_0^{(\ell)}-\frac{2}{n\tau}
 \sum_{c=1}^C\sum_{j=0}^{q-1}(2j+1)
 \bar\delta_{c,j}^{(\ell)}\bar h_{c,j}^{(\ell-1)\top}.
\]

Compute all current fields through this reconstructed network. Moment updates
then read

\[
\begin{aligned}
\dot{\bar h}_{c,j}&=\rho\mathbb E_\mu[h\psi_c]
 -\frac{\rho}{\tau}\left(j\bar h_{c,j}+\sum_{k<j}(2k+1)\bar h_{c,k}\right),\\
\dot{\bar\delta}_{c,j}&=\mathbb E_\mu[r\delta\psi_c]
 -\frac{\rho}{\tau}\left(j\bar\delta_{c,j}+\sum_{k<j}(2k+1)\bar\delta_{c,k}\right).
\end{aligned}
\]

Keep W^(1)'=-2 E_mu[r delta^(1) x^T/sqrt(d)] and w'=-2 E_mu[r h^(L)].
The raw equations remain defined at rho=0, where every velocity vanishes.
For fixed mu, y and evaluable integrals this is an autonomous finite state
system. Numerical quadrature or fresh minibatches approximate these integrals;
they are additional algorithmic choices, not exact population evaluation.

## Exact sample-indicator normalization

For m uniform atoms x_a, set psi_c(x_a)=sqrt(m)1[a=c]. Orthonormality follows
from (1/m)sum_a psi_c(x_a)psi_d(x_a)=1[c=d]. Both new moments equal the
corresponding baseline per-example moments divided by sqrt(m). Their product
contributes 1/m, exactly recovering the baseline reconstruction
-2/(nm tau)sum_(a,j)(2j+1)deltabar_(a,j) hbar_(a,j)^T. Sources, prefix,
clock and outer updates match under the same coordinate map. This is an
equivalence of the finite autonomous systems, including their Euler steps.
The deterministic float64 check verifies the map in state, derivative,
matrix reconstruction and predictions over twelve steps (maximum error
6.66e-16), not only at the zero-readout initial state.

## Same-history identity and its limits

Let Q be the orthogonal projection in L²(mu(dx) dxi) onto the tensor-product
span of psi_c(x)p_j(xi/tau), acting separately on each neuron coordinate.
For any one fixed pair of square-integrable histories b,h,

\[
\int_0^\tau\mathbb E_\mu[bh^\top]d\xi
 =\frac1\tau\sum_{c,j}(2j+1)\bar\delta_{c,j}\bar h_{c,j}^\top
 +\int_0^\tau\mathbb E_\mu[((I-Q)b)((I-Q)h)^\top]d\xi.
\]

To verify it, expand b=Qb+(I-Q)b and h=Qh+(I-Q)h. Both cross terms vanish
coordinatewise by orthogonality. The norm of the omitted matrix is bounded
by the product of the two L² norms, by Cauchy--Schwarz. Since dxi=rho dt,
the unprojected integral multiplied by -2/n is the corresponding accumulated
dense hidden-weight update evaluated on those histories. This argument compares
two reconstructions from one history. It does not identify self-consistent
projected trajectories with dense ones; their future fields differ.

The CPU quadrature test checks this tensor-product identity with independent
random vector fields and orthogonal Fourier/Legendre modes. This does not
establish a temporal or dictionary convergence rate for the learned dynamics.

## Streaming implementation and resources

On each Euler step replace E_mu by the average over one fresh uniform batch.
Replace rho by the batch residual RMS. The current batch and basis evaluations
are discarded/replaced; the learner never creates per-observation memory slots.
The prefix uses a finite initial quadrature of inputs and is then discarded.
For L=2 and d=2, moving state has 3n+2Cqn+1 scalars. The fixed dense W0 uses
n² scalars. Predictions also require current-batch activations, Fourier
evaluations and transient operations. The experiment records actual CUDA
allocation, including graph and diagnostic overhead, separately from state.

The deterministic full-sample closure uses 3n+2mqn+1 moving scalars. A matched
rank-R adaptive factor model W0+AB has 3n+2Rn moving scalars with R=Cq,
A(0)=0, B_ij(0)~N(0,1/R), and unit factor mobilities. Equal counts do not
equate optimizers, tangent metrics, wall time, or allocator footprints.

Batch estimates of each linear source would be unbiased conditionally on a
fixed current state if rho were exact. The implemented clock is a nonlinear
batch RMS and is generally biased for population rho. Moreover forward and
backward estimates use common observations, their stored moments become
correlated, and products of moment estimates are not unbiased estimates of
products of exact moments. Even the elementary one-draw variables a=(1,2,4),
b=(3,-1,5) give E[a]E[b]=49/9 while E[ab]=7. There is no stochastic-gradient
or dense-population equivalence claim.

Because the architecture and teachers are odd, deterministic full-circle
quadrature makes constant and even-frequency source coefficients vanish.
The generic Fourier dictionary nevertheless retains those slots; fresh
minibatches can excite them through sampling noise. The stated rank/state
bound includes every allocated slot. An odd-only optimized dictionary is
not tested in this preregistration.

## Primary-literature positioning

[HiPPO (Gu et al., NeurIPS2020)](https://proceedings.neurips.cc/paper_files/paper/2020/hash/102f0bb6efb3a6128a3c750dd16729be-Abstract.html)
establishes online polynomial representations of incoming signals. The source
paper already uses that temporal machinery; this route adds a fixed input
projection and feeds paired response moments back into the current network.
This connection does not transfer a feedback-stability theorem.

[LoRA (Hu et al., ICLR2022)](https://arxiv.org/abs/2106.09685)
trains low-rank corrections to fixed weights. Our baseline shares that
factor structure, but its initialized random network, jointly learned outer
layers, loss and factor mobilities are explicitly specified above. It is a
matched factor control, not a reproduction of language-model fine tuning.

[GaLore (Zhao et al., ICML2024)](https://arxiv.org/abs/2403.03507)
projects gradients to reduce training memory while permitting full-parameter
learning. Its existence prevents inferring novelty from a small optimizer
state alone. The tested object here is a self-consistent product of historical
response moments projected in both input and time; no comparative performance
claim against GaLore is tested. This limited literature check is not an
exhaustive novelty review.
