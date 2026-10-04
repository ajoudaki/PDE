# Exact temporal rearrangements of dense gradient writes

This is a finite-width dense-trajectory observer and intervention. It is not the
paper's autonomous response-memory closure. The source model is `paper/main.tex`,
Setting and equations dense-flow/exact-history; no manuscript convergence theorem
is invoked. Its temporal clock below is physical time, without an initialization
prefix. This differs explicitly from the activity clock used in the first screen.

For normalized input rows u_a=x_a/sqrt(d), a=1,...,m, let
h_a^(1)=tanh(W^(1)u_a), h_a^(2)=tanh(W^(2)h_a^(1)),
f_a=w^T h_a^(2)/n, r_a=f_a-y_a, and L=m^(-1) sum_a r_a^2.
Here W^(1) is n by d, W^(2) is n by n, and w is n-dimensional.
The backward response is delta_a^(2)=w odot (1-h_a^(2)^2).
The first/hidden/readout block mobilities are (n,1,n). All blocks take
simultaneous Euler steps of size eta. Independent Gaussian initial entries
have variances 1 and 1/n in the first/hidden blocks; w starts at zero.

Record the pre-update values on N consecutive steps. Write h_(a,i)=h_a^(1)
and b_(a,i)=r_a delta_a^(2), at step i=1,...,N. These are n-vectors;
b includes the residual. Define their temporal means
hbar_a=N^(-1)sum_i h_(a,i) and bbar_a=N^(-1)sum_i b_(a,i).
Summing the implemented Euler updates gives the exact identity

    W_end^(2)-W_start^(2)
      = -2 eta/(mn) sum_(a,i) b_(a,i) h_(a,i)^T
      = -2 eta N/(mn) sum_a bbar_a hbar_a^T
        -2 eta/(mn) sum_(a,i) (b_(a,i)-bbar_a)(h_(a,i)-hbar_a)^T.

The last term is the centered temporal pairing. This equality follows by
expanding both centered factors; their centered sums vanish. It remains true
for zero residual and stationary trajectories, without any quotient by RMS.
For phase-weighted training, replace b by m lambda_a r_a delta_a, where the
nonnegative phase weights lambda_a sum to one. All gradients must use these
same weights. Changing phase weights changes the training problem and is not
covered by a fixed-label initialization theorem.

## What an exact permutation preserves

For a permutation pi of {1,...,N}, define a reconstructed increment

    Delta W_pi = -2 eta/(mn) sum_(a,i) b_(a,pi(i)) h_(a,i)^T.

Apply the endpoint edit Delta W_pi - Delta W_identity to W_end^(2).
A single permutation acts on the entire backward array, so sample labels and
cross-sample structure at each backward time are retained. Its empirical
backward distribution, every empirical marginal moment, mean, and Gram matrix
are unchanged. The forward history is unchanged. Applying pi simultaneously
to both histories only reorders a finite sum, so the original increment is
exactly invariant. Reversing time twice also restores it. These statements are
finite algebraic identities; they need no smoothness or closure approximation.

The intervention is a physical weight edit. The first layer/readout retain
their observed endpoint values, which themselves depended on the original
trajectory. The edited state is therefore not the endpoint of ordinary GD
with the shuffled history. Applying this edit at an online block boundary is
a causal optimizer with observed finite memory; its future is a reachable
trajectory of that declared optimizer. Future histories need not retain the
original trajectory's marginals. Calling it a marginal-preserving retraining
counterfactual would be incorrect.

## Mean-only reconstruction is the permutation expectation

Let pi be uniform over all N! permutations. Since pi(i) is uniform,
E b_(a,pi(i))=bbar_a. Therefore

    E_pi Delta W_pi = -2 eta N/(mn) sum_a bbar_a hbar_a^T.

Thus the physical-time q1 observer is exactly the expectation of independently
re-pairing the two histories in time, using one common permutation across all
samples. An expected matrix need not have expected predictions or expected
loss in a nonlinear network. In particular, q1 can perform better than the
unpermuted write without contradicting this identity; the old repair result
is adverse evidence for any claim that exact temporal pairing is always useful.

There is also a closed second-moment identity. Assume N>=2 and let B_i,H_i
be n by m matrices whose columns are centered b_(a,i),h_(a,i). Put
Z_pi=sum_i B_pi(i) H_i^T. Then E Z_pi=0 and

    E ||Z_pi||_F^2 = 1/(N-1) sum_(i,j) ||B_j H_i^T||_F^2.

Proof: expand the squared norm into indices i,k and sample/neuron coordinates.
For i=k, the expectation of each product of two entries of B_pi(i) is
N^(-1) times the corresponding sum over j. For i!=k it is
-[N(N-1)]^(-1) times that sum, because sum_j B_j=0.
For each fixed pair of B entries, sum_(i!=k) of the corresponding H entry
products equals minus their i=k sum, because sum_i H_i=0. The combined
coefficient is 1/N+1/[N(N-1)]=1/(N-1), yielding the display after regrouping.
For N=1 both centered histories vanish and Z=0. Multiplication by
[2 eta/(mn)]^2 gives the variance of the permuted increment around q1.
A deterministic enumeration test checks the identity, not Monte Carlo alone.

## Why weak random controls do not identify coordination

For any matrix edit E with singular value decomposition U diag(s) V^T,
U diag(epsilon*s) V^T, epsilon_j in {-1,+1}, has the identical matrices
EE^T and E^T E, as well as the identical norm and singular spectrum.
This follows from epsilon_j^2=1. Such controls preserve learned left/right
singular axes, making them substantially stronger than randomizing both axes.
A harmful chronological edit beating isotropic noise but failing these controls
is evidence for learned directional sensitivity, not specific temporal utility.

For smooth fixed-endpoint loss, the exact one-variable identity

    L(W+E)-L(W) = <grad L(W),E>_F
                 + integral_0^1 (1-s) D^2 L(W+sE)[E,E] ds

follows by applying the fundamental theorem of calculus twice. Tanh and finite
weights make this loss smooth. Consequently every infinitesimal endpoint-loss
effect is an ordinary current-gradient projection. A claim of a novel causal
mechanism cannot be based on that first-order term alone. We report it and
compare norm-matched ascent/descent gradients. Averaging losses at W+E and W-E
cancels odd Taylor terms, but still measures ordinary directional curvature;
it does not by itself identify temporal causality.

## Status and limits

The finite-sum, permutation expectation, variance, and Gram-preservation claims
are exact under their stated hypotheses, with deterministic checks to accompany
the experiment. They establish a representation and intervention family, not
favorable generalization, a new autonomous closure, or a training-counterfactual
identification theorem. Functional usefulness is a separate falsifiable claim.

## Temporal reflection is an odd-mode intervention

Let T=N eta and let h_a(t),b_a(t) be the recorded piecewise constant physical-time
histories on [0,T]. Define orthonormal polynomials
psi_j(t)=sqrt((2j+1)/T) P_j(2t/T-1), where P_j is the ordinary Legendre polynomial.
Their observer coefficients are H_aj=integral h_a psi_j and D_aj=integral b_a psi_j.
These are normalized projection coefficients, distinct from the manuscript's
raw activity moments. Legendre parity P_j(-x)=(-1)^j P_j(x) follows, for example,
from Rodrigues' formula P_j(x)=(2^j j!)^(-1) d^j/dx^j (x^2-1)^j: the polynomial
before differentiation is even, and j differentiations yield parity (-1)^j.
Changing variables u=T-t now gives the reflected-backward coefficient
integral b_a(T-t) psi_j(t) dt=(-1)^j D_aj.

Consequently the projected reversal edit is exactly

    E_q = 4/(mn) sum_a sum_(j<q, j odd) D_aj H_aj^T.

Its q1 value is zero. It can be constructed using the same temporal coefficients
that approximate the ordinary write, without retaining stepwise histories.
At an online block boundary T is the observed block length; the formula uses
only past information. This is an observer-derived causal block edit, not a
proof that moments computed in an autonomous closure match dense histories.

The exact edit has the same formula with the full odd temporal subspace.
For g=h_a or b_a define g^-(t)=[g(t)-g(T-t)]/2, and let Pi_q be orthogonal
projection on modes 0,...,q-1. Reflection is self-adjoint and squares to identity;
its even and odd subspaces are orthogonal (substitution t -> T-t changes an
even-odd inner product's sign). Projection onto Legendre modes commutes with
reflection by parity. Cross terms between Pi_q and I-Pi_q also vanish. Therefore

    E-E_q = 4/(mn) sum_a integral [(I-Pi_q)b_a^-]
                                  [(I-Pi_q)h_a^-]^T dt,
    ||E-E_q||_F <= 4/(mn) sum_a ||(I-Pi_q)b_a^-||_L2
                                     ||(I-Pi_q)h_a^-||_L2.

The inequality follows from triangle inequality and Cauchy-Schwarz, using
||uv^T||_F=||u||_2||v||_2. It holds for arbitrary square-integrable finite histories,
including jumps and zero histories. For recorded data the squared tails equal
integral ||g_a^-||^2 minus sum_(j<q,j odd)||G_aj||^2 by Pythagoras; no unverified
smoothness assumption is used to estimate the right-hand side. Small negative
floating remainders from subtraction are clipped to zero and the test allows
absolute1e-9 roundoff. The bound may be loose; empirical edit accuracy is separate.

To apply E_q to a vector v one may sum D_aj(H_aj^T v) over odd modes, so application
requires stored vectors rather than a preassembled n by n edit. There are
2mn ceil((q-1)/2) scalar odd-mode coefficients (additional even modes are needed
for other operations). Since m=512 in this experiment, these coefficients can
exceed n^2: no memory saving over one dense accumulated edit is claimed here.
The practical compression is of the recorded N-step histories, and the dense
learner plus initialized matrix and common outer parameters still occupy memory.

## Weighted support changes and phase exchange

For the support continuation, let lambda_a(t)>=0 sum to one and use loss
L(t)=sum_a lambda_a(t) r_a(t)^2. The network, residual-free deltas and block
mobilities remain as defined above. On an Euler step with fixed lambda, the
hidden velocity is -2/n sum_a lambda_a r_a delta_a^(2) h_a^(1)T. Defining the
recorded backward history as b_a=m lambda_a r_a delta_a^(2) restores the common
factor -2/(mn); first/readout velocities use the same lambda. The step is
well-defined at a weight-switching boundary by the prescribed next-step weights.
No differentiation of lambda is involved. This is a nonautonomous weighted GD
extension; the manuscript's fixed-objective theorem is not imported.

For disjoint groups of sizes m_A,m_B, define lambda_A=1_A/m_A,
lambda_B=1_B/m_B. Joint training uses (lambda_A+lambda_B)/2 throughout duration T.
A schedule spending exactly T/2 on each group satisfies
integral_0^T lambda_a(t)dt=T/(2m_group(a)), the identical per-example exposure.
This identity follows by integrating each indicator and says nothing about the
resulting trajectory, since the state-dependent gradient is evaluated at
different parameters under different orders.

Let S=T/2 and regard both halves as histories on local coordinate s in[0,S].
Write h_A(s),b_A(s) for the first half and h_B(s),b_B(s) for the second; these
subscripts denote temporal halves, not individual sample groups. The exact
swap edit at a fixed endpoint is

    E_swap = 2/(mn) sum_a integral_0^S
                       [b_(a,A)-b_(a,B)][h_(a,A)-h_(a,B)]^T ds.

To verify the sign, the original interaction is b_A h_A^T+b_B h_B^T, whereas
a backward-half swap gives b_B h_A^T+b_A h_B^T. Their difference is
-(b_A-b_B)(h_A-h_B)^T; multiplication by -2/(mn) gives the display.
No labels are altered. Both full unpaired empirical histories are preserved
by the discrete half-swap bijection. Simultaneously swapping both histories
leaves the accumulated write unchanged.

Expand both phase differences in orthonormal Legendre functions on[0,S]. Let
H_aj and D_aj be their coefficients. Then

    E_swap,q = 2/(mn) sum_a sum_(j<q) D_aj H_aj^T,
    ||E_swap-E_swap,q||_F
       <=2/(mn) sum_a ||(I-Pi_q)(b_(a,A)-b_(a,B))||_L2
                        ||(I-Pi_q)(h_(a,A)-h_(a,B))||_L2.

The proof is the same orthogonal cross-term cancellation followed by
Cauchy-Schwarz as above. Squared tails are exact finite-history energies minus
retained coefficient energies. q1 represents the difference of two phase means;
unlike a single-history reflection, it can therefore represent phase exchange
without any higher temporal mode. A successful phase-swap intervention cannot
establish higher-order coordination if this stronger mean-only baseline already
reproduces its effect. The residual E_swap-E_swap,1 isolates a weight contribution
beyond those means, but is not itself necessarily a marginal-preserving history
permutation. Keeping those two causal scopes separate is part of the test.

The weighted-support observer above is evaluated on the entire fixed union
of inputs, including zero-weight examples. It requires those inputs to remain
available to construct their passive feature histories. This information
contract differs from replay-free continual learning with unavailable old or
future inputs. Weight zero removes a sample from the gradient, not from the
observer's feature queries.
