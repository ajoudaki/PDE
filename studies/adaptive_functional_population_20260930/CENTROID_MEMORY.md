# A moving ridge representation with a quadratic encoding bound

Internal derivation, 2026-09-30. This is a proved first-layer functional encoding result and a general conditional substitution principle. It is not a complete compression theorem for all deep forward/backward populations. No experiment, population-width limit, or all-time extension is asserted.

## 1. The object and the representation

Let mu be any input probability measure supported on a set X with
sup_X ||x||/sqrt(d) <= R. No density, polynomial structure, or label regularity is required. Let phi be C^2 with |phi''| <= K2. For a neuron with absolutely continuous first-layer weight row a(t) in R^d, put

\[
 h(t,x)=\phi(a(t)^Tx/\sqrt d),\quad
 \tau(t)=1+\int_0^t\rho(s)\,ds,\quad \rho\ge0.
\]

The normalized zeroth forward-history moment is

\[
 u(t,x)=\frac{\phi(a(0)^Tx/\sqrt d)
       +\int_0^t\rho(s)\phi(a(s)^Tx/\sqrt d)ds}{\tau(t)}.
\tag{1}
\]

In particular rho may be the current residual RMS. Its dependence on the rest of the network does not enter the following identity or approximation bound. Equation (1) is the exact functional memory driven by the supplied weight curve, even if that curve comes from an approximate network.

It is useful to regard (1) as a probability mixture of ridge functions:

\[
 \nu_t=\tau(t)^{-1}\left[\delta_{a(0)}+
                   \int_0^t\rho(s)\delta_{a(s)}ds\right],
 \qquad u(t,x)=\int\phi(b^Tx/\sqrt d)\,d\nu_t(b).
\tag{2}
\]

In the weak sense, dot(nu)=(rho/tau)(delta_a-nu). New mass enters at the current learned direction. Old directions are diluted by normalization. The measure lives on the weight trajectory, not on a grid in input space.

Partition [0,t] into consecutive curve segments I_j, including a currently unfinished segment. Each segment has weight-curve arclength at most delta. For every segment with positive mass define

\[
 \alpha_j=\int_{I_j}\rho(s)ds,\qquad
 b_j=\alpha_j^{-1}\int_{I_j}\rho(s)a(s)ds.
\tag{3}
\]

Zero-mass segments contribute nothing and need not store a ridge atom. Define

\[
 \widetilde u(t,x)=\frac{\phi(a(0)^Tx/\sqrt d)+
                    \sum_j\alpha_j\phi(b_j^Tx/\sqrt d)}{\tau(t)}.
\tag{4}
\]

These are genuine nonlinear basis functions: their directions b_j are learned averages. A large direction, narrow transition, or high harmonic content is kept inside phi(b_j^T x/sqrt(d)), without expansion in coordinate polynomials.

## 2. Uniform second-order error

**Proposition 1.** Under the preceding assumptions, simultaneously for every t for which all segments have arclength at most delta,

\[
 \sup_{x\in X}|u(t,x)-\widetilde u(t,x)|
 \le \frac{K_2R^2}{2}\delta^2.
\tag{5}
\]

**Proof.** On a segment, every pair of directions is at distance at most delta. Since b_j is a convex average of these directions, ||a(s)-b_j|| <= delta. Taylor's theorem at b_j gives

\[
 \phi(a(s)^T\xi)=\phi(b_j^T\xi)
    +\phi'(b_j^T\xi)(a(s)-b_j)^T\xi+e_j(s,\xi),
 \quad |e_j|\le\tfrac12K_2R^2\|a(s)-b_j\|^2,
\]

where xi=x/sqrt(d). The weighted linear term integrates to zero because
int_{I_j} rho(s)(a(s)-b_j)ds=0. Thus that segment contributes at most
(K2 R^2/2) alpha_j delta^2 to the unnormalized error. Sum and divide by tau; sum_j alpha_j=tau-1 <= tau. The prefix is retained exactly. This proves (5). Square integration against any input probability measure gives the same upper bound in L^2(mu). No probabilistic or label regularity hypothesis was used. QED.

There is a useful computable sharper certificate:

\[
 \sup_X|u-\widetilde u|
 \le \frac{K_2R^2}{2\tau}
     \sum_j\left[\int_{I_j}\rho\|a\|^2ds-\alpha_j\|b_j\|^2\right].
\tag{6}
\]

The bracket is nonnegative weighted within-segment variance. Storing one additional second-norm moment per segment makes this certificate available without querying the exact historical function. If two groups are merged, the increase in the unnormalized variance certificate is exactly

\[
 \frac{\alpha_1\alpha_2}{\alpha_1+\alpha_2}\|b_1-b_2\|^2.
\tag{7}
\]

This follows by expanding the squares about the combined mean. Therefore merging can use a real approximation-error budget rather than a rank, frequency, or degree cutoff. A greedy merging rule is implementable but no optimality or global fixed-budget performance guarantee for that rule is claimed here.

Let V(t)=int_0^t ||dot(a)||ds. Closing a segment whenever its arclength reaches delta gives at most 1+V(T)/delta segments on [0,T]. If an a priori bound V(T)<=V_* is known and M>=2 is a prescribed segment budget, take delta=V_*/(M-1). Then

\[
 \sup_{t\le T,x\in X}|u-\widetilde u|
 \le\frac{K_2R^2V_*^2}{2(M-1)^2}.
\tag{8}
\]

Count also one exact prefix atom. The error is quadratic in the number of curve segments. The constant measures weight movement and activation curvature, rather than derivatives with respect to every input coordinate. This is a statement for a bounded-length family; large V_* still costs state.

## 3. Online equations and restartability

For the active segment retain its mass alpha, vector v=int rho a, optional scalar s=int rho ||a||^2, and arclength counter ell. They evolve as

\[
 \dot\alpha=\rho,\quad \dot v=\rho a,\quad
 \dot s=\rho\|a\|^2,\quad \dot\ell=\|\dot a\|.
\tag{9}
\]

The atom direction is b=v/alpha when alpha>0. At alpha=0 its contribution is defined to be zero. Completed segments stop accumulating; at ell=delta, begin an empty segment. Store first moments rather than divide in the evolution equations. The decoder has a continuous zero-mass contribution for bounded directions. The process is a causal, restartable hybrid system, not a globally smooth ODE with fixed atom identities.

For a prescribed finite horizon and known movement budget, preallocate enough slots. No data mesh or saved response table is needed for the encoder. Completed atoms do not grow with the number of numerical steps. Their count grows with accumulated geometric movement, which can be bounded independently of the step count. An all-time fixed-capacity claim would require finite total path length.

The current a, dot(a), and rho are inputs already available to a network evolution. Supplying them from a dense reference would be a driven compression experiment. Evaluating them from an autonomous compressed network is also possible, but then a theorem comparing that network to dense training must separately propagate the encoding defects. Equations (5)-(7) remain valid for its own histories without a teacher.

## 4. A population-wide count from canonical dissipation

For the canonical network in this task, with loss L=E(f-y)^2,

\[
 \dot{\mathcal L}=-\|\dot W_1\|_F^2/n
 -\sum_{\ell=2}^L\|\dot W_\ell\|_F^2
 -\|\dot w\|_2^2/n.
\tag{10}
\]

This follows directly from the stated layer mobilities: W1 and readout have mobility n relative to the Euclidean loss gradient; interior matrices have mobility one. In particular, setting rho0=sqrt(L(0)),

\[
 \frac1n\sum_{i=1}^nV_i(T)^2
 \le\frac{T}{n}\int_0^T\|\dot W_1\|_F^2dt
 \le T\rho_0^2,
 \qquad
 \frac1n\sum_iV_i(T)\le\rho_0\sqrt T.
\tag{11}
\]

A common delta yields error (5) for every neuron, at every input and time. The total number of segments across neurons is at most

\[
 n+\delta^{-1}\sum_iV_i(T)
 \le n\left(1+\rho_0\sqrt T/\delta\right).
\tag{12}
\]

Taking delta=sqrt(2 epsilon/(K2 R^2)) when K2 R>0 gives total encoder storage

\[
 O\!\left(nd\left[1+\rho_0R\sqrt{K_2T/\varepsilon}\right]\right),
\tag{13}
\]

with uniform componentwise, normalized population RMS, and input L^2 error at most epsilon in the normalized first-layer zeroth history. Prefix directions can refer to the stored initialization. Constants do not contain sample count or width when R, K2, rho0 are fixed. The n factor in storage is intentional: this encodes a population of n neurons. The d factor pays for the actual directions; there is no epsilon exponent proportional to d. If K2=0 the centroid is exact; no movement subdivision is needed for this encoding.

The uniform componentwise error is obtained by a common segment diameter, with **adaptive allocation among neurons**. It is not a claim that the same fixed number of segments suffices for every neuron using only (11). One unusually mobile neuron may receive more slots. A global pool supplies the bound (12).

For the cube [-1,1]^d, R=1 under the canonical x/sqrt(d) scaling; for a sphere of radius sqrt(d), R=1 as well. The result also covers arbitrary discrete samples on those sets and arbitrary labels compatible with the assumed initial loss and existence of the flow.

Equation (10) belongs to canonical dense GF. It cannot be silently reused as an energy identity for a finite-order response-memory closure. For such a closure, the representation and certificate hold but its path-length budget must be supplied or proved separately.

## 5. Higher temporal moments: local ridge jets

The changing Legendre weights are signed, so the positive centroid argument should not be applied by dividing by an almost-zero signed mass. A safe extension uses a fixed anchor c_j=a(t_j) at the beginning of each segment and the local ridge jet

\[
 \phi(a^T\xi)\approx\phi(c_j^T\xi)
             +\phi'(c_j^T\xi)(a-c_j)^T\xi.
\tag{14}
\]

Its remainder is bounded by K2 R^2 delta^2/2. For k=0,...,q-1 let p_k be the shifted Legendre polynomial on [0,1], |p_k|<=1, and u=the accumulated-activity coordinate. On a completed or active segment retain

\[
 A_{jk}(\tau)=\int_{I_j}p_k(u/\tau)du,\quad
 B_{jk}(\tau)=\int_{I_j}p_k(u/\tau)[a(u)-c_j]du.
\tag{15}
\]

Then the segment's approximate contribution is A_jk phi(c_j^T xi)+phi'(c_j^T xi) B_jk^T xi. After normalization by tau, the same uniform C delta^2 error bound holds separately for each k, because the total integral of |p_k| is at most tau. The constant prefix is encoded exactly via its clock moments and initial direction.

In (15), I_j denotes the segment's image in activity coordinates. Flat-clock periods contribute no mass. The derivatives of A_jk and B_jk use the same finite lower-triangular moment transport as the original construction; the active segment has sources rho and rho(a-c_j), respectively, while completed segments have zero source. Thus these coordinates require O(qd) real numbers per segment. Equivalently, q clock-power integrals determine them algebraically, but raw powers are not recommended numerically. Summed errors across q moments, or errors in the reconstructed interaction with weights 2k+1, carry corresponding q factors. The individual bound must not be read as a q-uniform network theorem.

These Taylor jets are local in **parameter displacement inside a segment**. They are not a temporal Taylor series at initialization and do not require the training trajectory to be analytic in time.

## 6. How a certificate can control feedback

An abstract substitution lemma makes the relevant proof obligation precise. Suppose a reference system dot(S)=F(S) is K-Lipschitz on a bounded tube on [0,T]. Its state contains a driven history H. In an implementation replace H by an encoder value Htilde, while retaining a proof-only exact accumulator Hacc driven by the implementation's own sources. Assume its augmented physical/accumulator state Sacc satisfies

\[
 \dot S^{acc}=F(S^{acc})+e(t),\quad
 \|e(t)\|\le B\|\widetilde H-H^{acc}\|,
 \quad S^{acc}(0)=S(0).
\tag{16}
\]

If ||Htilde-Hacc||<=D delta^2, subtracting the integral equations gives

\[
 \sup_{t\le T}\|S^{acc}(t)-S(t)\|
 \le BD\delta^2 T e^{KT}.
\tag{17}
\]

The actual decoded history differs by at most another D delta^2. Equation (16) follows for ordinary smooth state equations by the Lipschitz dependence of their computed sources on the substituted history. It is not an extra guess about the unknown exact solution. Localization and an exit bootstrap can replace a global tube assumption when the reference exists on [0,T] and the required source bounds hold there.

This shows how to use the centroid certificate in a partially compressed moment system without a snapshot/feedback fallacy. It does not prove small B or K in width, depth, or time. Nor does it supply an encoder for all other state fields. For unnormalized H, D includes a bound on tau. The certificate (5) itself is for H/tau.

## 7. The actual remaining deep-network problem

The first-layer atom phi(b^T x/sqrt(d)) has d parameters. A deep response atom generally depends on all preceding trained layers, and a backward atom additionally uses the transposed downstream layers and residual. Applying a generic parametric-curve centroid theorem to a full deep-network snapshot can use O(Ln^2+nd) parameters per atom. This is not an efficient learned-population representation.

The meaningful extension would retain a shared compositional circuit of small learned atoms, certify local replacement errors, and keep the total number of circuit edges and parameters bounded as training proceeds. Old atoms must not point to changing descendants unless that change is part of their certified approximation. Cloning all historical descendants conceals growing memory. Shared nonlinear feature descriptions, rather than only a shared linear span, are needed if full-rank response tables are to remain cheap.

There is a sound next target: prove a bound on accumulated **normal velocity** outside a chosen adaptive compositional family. If U(z) is a finite functional encoding of the whole state and dot(U)=F(U), choose dot(z) to minimize ||D_z U v-F(U)|| in a norm controlling reconstruction. The attained residual, plus numerical quadrature errors, propagates by the same integral comparison as (17). Existing Neural Galerkin theory supplies this projection design, not a guarantee that this particular deep-neural response field has a cheap compositional encoding. The latter is precisely the missing theorem.

The result here therefore establishes an efficient, streamable, first-layer functional memory with a quadratic accuracy/budget tradeoff. It identifies finite movement and local curvature as an alternative to low-degree input bases. It does not establish the complete sample-independent deep population closure requested by the user.

## 8. Arithmetic and primary-source boundary

For the zeroth moment, maintaining active cells costs O(nd) arithmetic per physical RHS evaluation once a, dot(a), and rho are available. Completed cells have no unnormalized updates. A query of all encoded first-layer histories costs O(d times the total number of stored cells). The actual forward/backward network evaluations, retained W0 matrix actions, training-data expectations, and event detection have their additional costs. Exact empirical averages still require access to the dataset. A source-free encoding is not a sample-count-free runtime theorem.

For q moments, the elementary triangular transport costs O(q^2 d) per cell per physical RHS; prefix sums in the lower-order sums reduce it to O(qd). Arithmetic also includes evaluating the q Legendre coordinates. None of this removes the work needed by the unencoded deep and backward fields.

Primary source read in full: Bruna, Peherstorfer, Vanden-Eijnden, *Neural Galerkin Scheme with Active Learning for High-Dimensional Evolution Equations*, arXiv:2203.01360v3, https://arxiv.org/html/2203.01360v3. Equations (3)-(8) supply the velocity-residual minimization and parameter ODE precedent. Section 4 explicitly leaves uniform representability and efficient residual estimation as further questions. This is an ingredient precedent, not a solution of the current neural-closure problem. No novelty priority claim is made for centroid/Taylor quadrature or moving nonlinear approximation.
