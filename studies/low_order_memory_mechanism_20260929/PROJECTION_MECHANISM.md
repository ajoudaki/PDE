# Paired response memory: exact geometry, derivative coordinates and passivity

29 September 2026. Parent derivation from MODEL.md and elementary polynomial
identities. This studies the closure itself, not a dense-reference error.
No population limit or independent-neuron law is assumed.

## 1. One memory channel per sample at q=1

At a hidden link write h_a for the previous-layer feature and delta_a for
the next-layer backward response. Put

\[
 a_a=B_{a,0}/\tau,
 \qquad u_a=-2C_{a,0}.
\]

For any training or passive test feature h,

\[
 Wh=W_0h+\frac1m\sum_a u_a\frac{a_a^Th}{n},\qquad
 W^T\delta=W_0^T\delta+\frac1m\sum_a a_a\frac{u_a^T\delta}{n}.
\tag{1}
\]

The factors obey exactly

\[
 \dot a_a=\frac\rho\tau(h_a-a_a),\qquad
 \dot u_a=-2r_a\delta_a.
\tag{2}
\]

Thus a_a is the feature address at which the accumulated signed error credit
u_a is retrieved. This is a signed linear associative map: the retrieval
weights a_a^T h/n need not be positive or sum to one. The map remains embedded
in a nonlinear deep network. Its transpose supplies reciprocal credit routing.
Both address and credit are neuron-space vectors that evolve; no fixed feature
dictionary is imposed.

The address is the exact activity average

\[
 a_a(t)=\frac{h_a(0)+\int_0^t\rho(s)h_a(s)\,ds}{1+\int_0^t\rho(s)\,ds}.
\tag{3}
\]

It lies in the convex hull of its past forward responses. At rho=0 all raw
updates stop. No division by rho is used by the algorithm.

Differentiating the learned matrix gives

\[
 \dot{\Delta W}=-\frac2{mn}\sum_a r_a\delta_a a_a^T
       +\frac\rho{mn\tau}\sum_a u_a(h_a-a_a)^T.
\tag{4}
\]

The first term adds new credit; the second changes the address of already
accumulated credit. This second term is the precise consequence of allowing
feature addresses to evolve. It is also why this is not ordinary Euclidean
gradient descent on a low-rank factorization. No descent claim follows from
(4) alone.

For a nonzero a_a, with e_a=a_a/||a_a||, its direction changes according to

\[
 \dot e_a=\frac\rho{\tau\|a_a\|}(I-e_ae_a^T)h_a.
\tag{5}
\]

New components of the current feature therefore rotate the remembered
direction. Low instantaneous rank is not a fixed subspace of neuron space.

## 2. What higher orders add

Let h(xi), b(xi) be the actual activity histories (including their prescribed
prefixes), and denote uniform averaging over [0,tau] by E_tau. Define

\[
 \mu_{h,k}=B_k/\tau=\mathbb E_\tau[h(\xi)p_k(\xi/\tau)],\qquad
 \mu_{b,k}=C_k/\tau.
\]

For each sample the reconstructed learned interaction is

\[
 -\frac{2\tau}{mn}\sum_{k<q}(2k+1)\mu_{b,k}\mu_{h,k}^T.
\tag{6}
\]

At q=1 only the product of the mean histories is retained. At q=2 the
additional interaction is -6 tau mu_b,1 mu_h,1^T/(mn); at q=3 the next is
-10 tau mu_b,2 mu_h,2^T/(mn). The complete L2 pairing decomposes exactly into
these modewise products by Parseval, entry by entry; its q=1 omitted part is
the temporal cross-covariance

\[
 \mathbb E_\tau[bh^T]-\mathbb E_\tau[b]\mathbb E_\tau[h]^T.
\tag{7}
\]

This identifies the lost information: q=1 retains persistent forward and
backward responses but not their correlated variation within the history
window. Additional modes resolve that variation. At fixed histories, only
matching temporal modes interact under the history integral. This does not
make spatial neuron modes orthogonal or independent.

### A precise position/velocity/acceleration interpretation

For a sufficiently smooth Hilbert-valued history f on [0,tau], Rodrigues'
formula and k integrations by parts give

\[
 \mu_k=\int_0^1 f(\tau u)p_k(u)\,du
   =\frac{\tau^k}{k!}\int_0^1[u(1-u)]^k f^{(k)}(\tau u)\,du.
\tag{8}
\]

Indeed p_k(u)=(1/k!)(d/du)^k[u^k(u-1)^k]. All boundary terms vanish,
because this polynomial and its derivatives of orders below k vanish at both
endpoints. Its sign (-1)^k cancels the integration-by-parts sign. The formula
also holds for f in H^k by approximation and the weak derivative definition.

Consequently

\[
 \mu_0=\text{uniform average of }f,
 \qquad
 \mu_1=\frac\tau6\int_0^1 6u(1-u)f'(\tau u)\,du,
\]
\[
 \mu_2=\frac{\tau^2}{60}\int_0^1 30u^2(1-u)^2f''(\tau u)\,du.
\tag{9}
\]

The displayed weights integrate to one. Thus the analogy is mathematically
accurate as *weighted historical* position, velocity and acceleration in
activity time, with explicit scale factors. They are not current physical-time
derivatives or a Taylor jet used to extrapolate the future. If a prefix creates
a jump or kink, the relevant smoothness condition must be checked before using
the derivative formula; the integral moment definitions remain valid without it.

## 3. One stable filter shared by every neuron

On intervals of positive activity let a=log(tau); write D=d/da. For either
history f, normalized moments mu_k=M_k/tau obey

\[
 D\mu_k=f-(k+1)\mu_k-\sum_{j<k}(2j+1)\mu_j.
\tag{10}
\]

This follows directly from the raw moment equations and the quotient rule.
In particular,

\[
 (D+1)\mu_0=f,\qquad
 (D+2)\mu_1=D\mu_0,\qquad
 (D+3)\mu_2=(D-1)\mu_1.
\tag{11}
\]

The last two identities follow by subtracting consecutive equations (10).
Generally (D+k+1)mu_k=(D-k+1)mu_(k-1). All homogeneous eigenvalues are
-1,...,-q. For q=1,

\[
 \mu_0(a)=e^{-a}\mu_0(0)+\int_0^a e^{-(a-v)}f(v)\,dv.
\tag{12}
\]

Thus uniform averaging over accumulated activity becomes exponential smoothing
in logarithmic activity. The filter is fixed and identical across neurons;
nonlinear coupling lies in the response f supplied by the current network.
Fixed-filter stability alone is not stability of that feedback interconnection.

## 4. Exact energy balance, stronger than eigenvalue stability

Set z_k=sqrt((2k+1)/tau) M_k and v_k=sqrt(2k+1), k=0,...,q-1.
The triangular matrix A has A_kk=-(k+1/2), A_kj=-sqrt((2k+1)(2j+1))
for j<k and zero entries for j>k. Then

\[
 \frac{dz}{d\tau}=\frac1\tau Az+\frac1{\sqrt\tau}vf,
 \quad A+A^T=-vv^T,
 \quad f_* = v^Tz/\sqrt\tau.
\tag{13}
\]

Here f_* is the endpoint value of the projected history. Taking the energy
derivative gives exactly

\[
 \frac d{d\tau}\sum_{k<q}\|z_k\|^2
 =2\langle f,f_*\rangle-\|f_*\|^2
 =\|f\|^2-\|f-f_*\|^2.
\tag{14}
\]

The proof is multiplication of (13) by 2z and use of A+A^T. It works in any
real Hilbert space, in particular for a single neuron, a whole layer with
its explicit RMS normalization, or jointly over samples and neurons.
Integrating yields

\[
 \sum_k\|z_k(\tau)\|^2+
 \int_1^\tau\|f(\xi)-f_*(\xi)\|^2\,d\xi
 =\sum_k\|z_k(1)\|^2+\int_1^\tau\|f(\xi)\|^2\,d\xi.
\tag{15}
\]

This is a unit-gain energy budget for memory, for every q and with no dimension
factor. The histories are the closure's own, so no external reference is needed.
It proves bounded memory from finite input energy, and an exact accounting of
what energy is retained and omitted. It does not say loss decreases: the
network can supply changing responses using the very interaction reconstructed
from those memories. Stability and fitting of that feedback are separate claims.

## 5. Scientific interpretation and limits

A candidate organizing principle is *adaptive, reciprocal associative memory
with a passive temporal filter*. Each sample provides a small number of
evolving addresses and credit directions per layer. The fixed Gaussian map
mixes these signals with the population, and nonlinear gates reshape the
responses subsequently written into the addresses and credits. Their temporal
energy balance is exact. The learning question becomes whether these address/
credit loops remain sufficiently aligned to dissipate training loss.

This is a mechanistic reformulation supported by equations (1)--(15), not a
claim of unique novelty or a proof that generic nonlinear networks always fit.
The number of vector channels is O(mq) per layer, but there are still n entries
per channel. Removing learned dense matrices does not produce an O(1)-scalar
ODE, eliminate W0 reuse correlations, or make a global all-label theorem automatic.
