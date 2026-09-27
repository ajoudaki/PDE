# Eulerian aggregate transport audit

Scoped theoretical work, 2026-09-27. Inputs read completely: `block_scalar_closure.py`, `BLOCK_HIERARCHY_ROUTE.md`, `RESTRICTED_THEOREM.md`, and `GAUSSIAN_HIERARCHY_ASSESSMENT.md`. No other study was read and no training was run. This note applies the rigorous-math and conjecture-audit skills. It is an internal derivation, not an independent promotion review.

## Conclusion and scope

For a fixed Gaussian block size k and fixed memory order H, a conservative Eulerian histogram supplies a genuine aggregate scalar ODE. Its variables are masses in fixed cells of block-state space and one common clock. Its state count is independent of the number of original blocks and of elapsed time. The cells do not move, and there is no representative-neuron trajectory in the runtime state.

Below is a finite-horizon convergence argument, including Gaussian static matrices and Gaussian first-layer labels. The canonical finite-width readout initialization is covered on a width-uniform high-probability event; the population initialization c=0 is covered directly. This is convergence to the specified finite-memory Gaussian-block flow. It proves neither convergence of that memory closure to full training nor identification with the dense Gaussian large-width limit. The grid has a severe dimension cost; there is no useful efficiency conclusion.

## 1. Exact law and fields

Put

\[
z=(G,w,c,(A_j,B_j)_{j<H}),\qquad
D=k^2+3k+2kmH.
\]

Here G is k by k, w is k by 2, c is k, and A_j,B_j are k by m. Give G zero velocity. Let mu be the law of z and retain L as one separate scalar. Every average in `BLOCK_HIERARCHY_ROUTE.md` is an integral against mu, including the factor 1/k within a block.

The finite list of training fields is evaluated in the order

\[
\langle B_j^T h_{1a}/k\rangle
\longrightarrow z_{2a},h_{2a},f_a,r_a
\longrightarrow\langle A_j^T\delta_{2a}/k\rangle.
\]

Consequently the block velocity b(z,mu,L) is explicit. There is no implicit fixed point in one RHS evaluation. The exact transport equation is

\[
\partial_t\mu+\nabla_z\cdot(b(z,\mu,L)\mu)=0,
\qquad \dot L=\rho(\mu,L),\quad L(0)=1.
\tag{1}
\]

For an empirical initial law its characteristics reproduce the original block system exactly, with all dense learned cross-block interactions retained.

## 2. Bounds uniform in block count, with a useful memory improvement

First assume |c_i(0)|<=C_0 and |y_a|<=Y. On [0,T], put

\[
C_T=(C_0+Y)e^{2T}-Y,\quad R_T=C_T+Y,
\quad \Lambda_T=1+TR_T.
\]

Then |c_i|<=C_T, |r_a|,rho<=R_T, and 1<=L<=Lambda_T. These follow by integrating |dot c_i|<=2(max_i|c_i|+Y); the argument applies equally to essential suprema under a law. No bound on G or w is needed.

The memory bounds can be made independent of H. Write P_j for the Legendre polynomial normalized by P_j(1)=1. The polynomial identity

\[
x\frac{d}{dx}P_j(2x-1)
=jP_j(2x-1)+\sum_{r<j}(2r+1)P_r(2x-1)
\tag{2}
\]

gives, by differentiation under the finite-time integral,

\[
A_{ja}(t)=\int_0^t
P_j\!\left(\frac{2L(s)}{L(t)}-1\right)
r_a(s)\delta_{2a}(s)\,ds,
\tag{3}
\]

\[
\begin{split}
B_{ja}(t)=h_{1a}(0)\int_0^1
P_j\!\left(\frac{2\xi}{L(t)}-1\right)d\xi\\
\hspace{12mm}+\int_0^t
P_j\!\left(\frac{2L(s)}{L(t)}-1\right)
\rho(s)h_{1a}(s)\,ds.
\end{split}
\tag{4}
\]

Equation (4) has exactly B_0(0)=h_1(0), B_j(0)=0 for j>0, because the nonconstant Legendre polynomials have zero integral on [-1,1]. Formula (3) has A_j(0)=0. Identity (2) makes the differentiated formulas equal the stated triangular ODE, so uniqueness for a finite triangular linear system proves them. All polynomial arguments lie in [-1,1]. The elementary bound |P_j|<=1 on this interval gives

\[
|A_{ja}(t)|\le TC_TR_T,\qquad
|B_{ja}(t)|\le\Lambda_T.
\tag{5}
\]

One way to check the polynomial bound is the integral formula
P_j(cos theta)=pi^{-1} integral_0^pi (cos theta+i sin theta cos phi)^j d phi: the integrand has modulus at most one. The formula and (2) can also be verified coefficientwise from the finite polynomial definition, so no probabilistic regularity assumption enters here.

Since sum_{j<H}(2j+1)=H^2, the first-layer equation now gives

\[
\|w(t)-w(0)\|\le K_T\{1+\|G\|+H^2\}.
\tag{6}
\]

K_T may depend on k,m and the bounded data, but not on original block count or H. Any fixed finite-dimensional norm can be used, with its k-dependent equivalence constants included. This proves nonexplosion of each finite empirical system. It also gives Gaussian tail control of reachable first-layer states when G,w(0) have an exponential quadratic moment.

## 3. A concrete bounded histogram ODE

Fix a radius R and a uniform Cartesian grid of spacing h on [-R,R]^D, including its boundary. Round h down so that 2R/h is an integer. Let z_i be its fixed nodes. Put p_i>=0, sum_i p_i=1, and mu_h=sum_i p_i delta_{z_i}.

Choose a Lipschitz scalar cutoff chi_R equal to one on [-R/2,R/2], zero at and outside [-R,R], and between zero and one elsewhere. Define the compactly supported velocity by multiplying dynamic coordinate j of b by chi_R(z_j). All field arguments are clipped to [-R,R] when extending the formula outside the box. Static G coordinates have zero velocity. Call the resulting velocity b_R. Keep the formula dot L=rho(mu_h,L) and L>=1; no clock grid is needed.

For each dynamic coordinate j put

\[
q_{i,i+e_j}=b_{R,j}(z_i,\mu_h,L)^+/h,
\qquad
q_{i,i-e_j}=(-b_{R,j}(z_i,\mu_h,L))^+/h.
\]

An absent neighbor has rate zero. The boundary cutoff already makes the corresponding outward drift zero. The scalar mass equations are

\[
\dot p_i=\sum_{v\sim i}p_vq_{vi}
-p_i\sum_{v\sim i}q_{iv},
\qquad \dot L=\rho(\mu_h,L).
\tag{7}
\]

Every coefficient is a current fixed-node contraction. Summing (7) proves exact mass conservation. At p_i=0 its derivative is nonnegative, proving positivity. Positive-part, clipping, tanh and L^{-1} on L>=1 are Lipschitz; therefore this finite ODE is locally Lipschitz. The simplex is invariant and rho<=R+Y, so it has a unique global solution. No density smoothness is assumed. Singular and empirical initial laws are allowed.

Initialize by clipping the permitted initial seeds to an interior subbox, lifting to the prescribed initial memory, and accumulating their grid-cell masses in one pass. For a known population law use its cell probabilities. Original blocks can then be discarded. Gaussian probability quadrature, if used, is an additional initialization error, not an exact integration claim. Grid coordinates are generated from indices; they are not retained block samples.

## 4. Direct finite-box convergence proof

Let the bounded velocity b_R have speed bound B_R and Lipschitz constant K_R in state, W_1 law distance and L; the clock has the same enlarged Lipschitz constant. These constants are finite by the explicit arithmetic expression tree. A loose global bound has B_R<=C_{k,m,H,Y}(1+R)^4 and K_R<=C_{k,m,H,Y}(1+R)^6. The dependence on H in these finite expression-tree constants is polynomial.

Represent (7) by a time-inhomogeneous jump chain Z_h with its deterministic self-consistent law mu_h. Each coordinate jump is +/-h, and its conditional drift is exactly b_R. Hence

\[
Z_h(t)=Z_h(0)+\int_0^t b_R(Z_h(s),\mu_h(s),L_h(s))ds+M_h(t),
\]

where M_h has zero mean and

\[
\mathbb E\|M_h(t)\|_2^2
=h\,\mathbb E\int_0^t\sum_j|b_{R,j}|ds
\le hDB_RT.
\tag{8}
\]

This identity follows by summing conditional variances of the compensated coordinate jumps; cross-coordinate jumps do not occur simultaneously. Couple Z_h(0) to the initial state of the deterministic characteristic solution Z of the compact equation. The same initial random seed defines that coupling. With E(t)=E||Z_h(t)-Z(t)||+|L_h(t)-L(t)|, the characteristic integral equations, (8), and W_1(mu_h,mu)<=E||Z_h-Z|| give

\[
\sup_{t\le T}E(t)
\le e^{3K_RT}\{E(0)+\sqrt{hDB_RT}\},
\tag{9}
\]

up to a fixed norm-equivalence factor. Integral Gronwall follows by iterating the nonnegative integral inequality. Initial rounding costs at most sqrt(D)h. This proves convergence for fixed R as h tends to zero. Every bound is independent of original block count. The finite-box law equation itself can be constructed by the same Picard iteration given in `RESTRICTED_THEOREM.md`, since clipping supplies the required bounded global Lipschitz constants.

## 5. Gaussian cap removal on every finite horizon

The invalid shortcut would be to multiply a Gaussian tail e^{-aR^2} by e^{C_TR^2} and assert that the result vanishes for arbitrary T. Instead use short-interval continuation.

Assume, deterministically,

\[
|c(0)|_\infty\le C_0,
\qquad
\int e^{a(\|G\|_F^2+\|w(0)\|_F^2)}d\lambda\le M
\tag{10}
\]

for some a>0. All compact approximations use coupled original seeds and clipping maps that do not increase seed norms. Once R exceeds twice the bounds (5) and the readout bound, clipping of c,A,B is inactive on [0,T]. To justify this, stop at a first entry into a cutoff region; before that entry (3)--(5) apply and exclude it. First-layer drift clipping does not affect this argument, because its source h_1 remains bounded by one. Equation (6) also holds for the clipped paths, with the same original seed norm on the right.

Compare two compact approximations. Use the bounded state distance d(z,z')=min(1,||z-z'||) and

\[
e(t)=\mathbb E d(Z(t),Z'(t))+|L(t)-L'(t)|.
\]

For original seeds satisfying ||G||+||w(0)||<=r, both compact systems use the original formula once their caps exceed K_T(1+r+H^2). On this good set, direct subtraction of the formulas gives a Lipschitz constant at most C_{T,H}(1+r^2). The quadratic power comes from the pair G and G^T in differentiated backpropagation. All remaining H dependence is polynomial, using (5) and sum_j(2j+1)=H^2.

For clarity about order dependence, use the maximum coordinate norm for the bounded state distance. Let Q=1+r+H^2. Subtracting h_1 and the B overlaps costs C_T; subtracting z_2,h_2,delta_2 and each A overlap costs C_T Q; the transpose backpropagation and residual multiplication cost C_T Q^2. A row of either triangular memory equation has total absolute coefficient at most H^2, so it costs at most C_T H^2 Q. Thus a common pointwise/law Lipschitz bound is C_T(1+H)^4(1+r^2). Constants may depend on fixed k,m and the data. If using the sum coordinate norm, the extra factor D is at most a fixed constant times 1+H, so C_T(1+H)^8(1+r^2) is a safe deliberately loose choice.

The observable integrands B_j h_1, c h_2, A_j delta_2 are bounded independently of G,w. On the bad set their differences cost only its probability mass. Its contribution to a dynamic-state derivative is bounded by C_{T,H}(1+||G||); (10) bounds this weighted tail by C_{T,H}M e^{-a' r^2}, for some a'>0 depending only on a and norm equivalence. Consequently, for s<=t<=T,

\[
e(t)\le e(s)+C_{T,H}\int_s^t
\{(1+r^2)e(v)+M e^{-a'r^2}\}\,dv.
\tag{11}
\]

The constants are uniform over both caps and over original block count. They can be enlarged to absorb powers of r into a smaller a'. The derivative of min(1,||Z-Z'||) is bounded by the difference velocity below its saturation threshold and zero above it; this justifies using a bounded metric despite unbounded w.

Choose Delta>0 so C_{T,H}Delta<a'/2. Gronwall on [s,s+Delta] gives a bound of the form

\[
\sup_{s\le t\le s+\Delta}e(t)
\le C e^{C_{T,H}r^2\Delta}e(s)
+CM e^{-(a'-C_{T,H}\Delta)r^2}.
\tag{12}
\]

For each fixed r, first send both caps to infinity. Their initial clipped laws are Cauchy in the bounded metric, so the first term vanishes on the initial interval. Then send r to infinity; the second term vanishes. This proves uniform Cauchy convergence on that interval. Repeat the same argument on finitely many intervals, keeping the original-label tail estimate (10). The limit exists on all of [0,T]. The same inequality applied to two uncapped solutions with identical initial law proves uniqueness. Passage to the characteristic equations follows by restricting to the good labels, where convergence is uniform and the vector field is Lipschitz, and then removing the tail using its integrable velocity bound.

Training fields and outputs converge as well: their difference is bounded by C_{T,H}(1+r)(e(t)+|L-L'|)+C_{T,H}M e^{-a'r^2}. The constants are uniform for every test input ||u||<=1, because tanh(wu) is Lipschitz in w with that uniform constant. No test-input grid or spatial differentiability assumption is required for this comparison.

There is also a quantitative version. Suppose (11) is valid for 0<=r<=r_* and the initial error is at most a constant times delta=M exp(-a' r_*^2). Increase M to absorb that constant, set d=e+delta, and choose r^2=(a')^{-1}log(M/d) while d<=M. This choice is admissible because d>=delta. Absorbing fixed constants gives

\[
d'\le C_{T,H}d\{1+\log(M/d)\}.
\]

Writing v=1+log(M/d) gives v'>=-C_{T,H}v. Integration and inversion yield

\[
e(t)\le C_M\exp\{-c r_*^2 e^{-C_{T,H}t}\}.
\tag{12a}
\]

For the finitely many early cases where d is not below M, enlarge the harmless prefactor. In constructing a limit, apply this inequality to two compact approximations, then pass to the already established fixed-H limit. If seeds are clipped at radius r_seed and the state box radius B obeys B>2K_T(1+r_seed+H^2), one may take r_* to be a fixed fraction of r_seed. This separates the Gaussian cutoff scale from the reachable-state box.

This proves an actual fixed-H Gaussian law and cap removal, rather than assuming its existence. It also proves uniform convergence over empirical laws satisfying (10), hence width-independent approximation after initialization from the empirical histogram.

## 6. Canonical Gaussian probability statement

For iid G_ij~N(0,1/k) and standard Gaussian entries of w(0), choose any 0<a<min(k/2,1/2). The Gaussian integral E exp(aX^2)=(1-2a sigma^2)^{-1/2} proves that the expectation M_* of the integrand in (10) is finite and depends only on k,a. Markov's inequality gives

\[
\Pr\left\{b^{-1}\sum_{\beta=1}^b
e^{a(\|G_\beta\|_F^2+\|w_\beta(0)\|_F^2)}
>2M_*/\eta\right\}\le\eta/2
\]

for every b, without any maximum-G requirement. For canonical c_i(0)=g_i/n and n=bk,

\[
\Pr\{\max_i|c_i(0)|>C_\eta\}
\le2n e^{-n^2 C_\eta^2/2}\le\eta/2
\]

when C_eta=max(1,sqrt(2 log(4/eta))). Thus (10) and the readout bound hold with probability at least 1-eta, with constants independent of width. This is a statement at every fixed width; it does not assert one event simultaneously over an unspecified coupling of all widths. For the population law c(0)=0, no readout event is needed. A general unscaled Gaussian readout law is not covered by the bounded-readout proof and should not be silently substituted.

## 7. Dimension and combining the two approximation indices

For fixed H and a grid with J intervals per coordinate, the state count is

\[
N=1+(J+1)^{k^2+3k+2kmH}.
\tag{13}
\]

The simplex constraint removes one redundant scalar if desired. G coordinates have no flux, but remain essential fixed cell labels. The current state is only all cell masses and L; cell positions are fixed coefficients. Reaching a longer elapsed time never adds cells or memories.

Initially the proof separates memory order H and aggregate refinement. They may be tied to a single order P by prescribing H(P), R(P), h(P) in advance; this yields N(k,m,P). It is not legitimate simply to set H=P,R=P and reuse a fixed-H convergence assertion: its constants depend on H.

A deliberately extravagant explicit schedule separates the seed cutoff r(P), state box B(P), and spacing:

\[
H(P)=P,\qquad r(P)=e^{P^{20}},\qquad
B(P)=e^{P^{40}},\qquad h(P)\le e^{-e^{P^{80}}},
\tag{14}
\]

with h rounded down to fit the box. For every fixed T, the seed trajectories in the good set stay in the inner half box eventually, by (6). Bound (12a), with C_{T,H}<=C_T(1+H)^8, tends to zero because r(P)^2 exp[-C_T(1+P)^8 T] tends to infinity. The global finite-box Lipschitz factor has the form exp[poly(P) B(P)^6 C_T], whereas sqrt(h(P)) is at most exp[-exp(P^80)/2]; the latter dominates. Initial rounding is even smaller. The output Lipschitz factor on the box adds only a polynomial in P,B and does not change this conclusion. These prescriptions depend on k,m,P and fixed numerical rules, not on elapsed time, original width, or future outputs. They are existence-scale prescriptions with astronomical storage.

Therefore the aggregate transport error relative to the matching order-P memory flow tends to zero along (14) on every fixed finite horizon, in the stated width-uniform probability mode. Neither this diagonalization nor transport convergence supplies the separate memory-order convergence theorem. A correct final error statement still separates aggregate transport, memory closure, Gaussian-block/dense identification, initial quadrature, and numerical time integration.
