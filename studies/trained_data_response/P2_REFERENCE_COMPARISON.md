# A raw-state comparison at the trained reference

Author: `/root`, task `01a09106-41c4-7193-9db9-8068144fd825`.
Status: author-derived partial result; no full milestone-2 theorem is claimed.
Scientific inputs: complete frozen P1_SECTION.md and P1_DEPENDENCIES.md;
current docs/global_nonlinear.md C.2 and C.4.1–C.4.6, and the notation and
reading guides. The frozen dependencies contain finite dynamics §§1–4,
special-data III.F, global-nonlinear A.1–A.4/B.1, and the reference proofs.
No other study or unfinished P2 route was an input to this derivation.

## 1. Exact finite and existing-population bounds for arbitrary laws

Fix Y≥1 and T=40, with the exact model in P2_CONTRACT.md. In normalized
inputs, write φ=tanh, A=W², c=W³, w=W¹. At any state define

\[
h(u)=\phi(wu),\quad z(u)=Ah(u),\quad H(u)=\phi(z(u)),
\quad f(u)=c^T H(u)/n,
\]
\[
d(u)=c\phi'(z(u)),\qquad Q(u)=A^Td(u),\qquad r(u,y)=f(u)-y.
\]

The finite field is exactly

\[
\dot w=-2\int r[\phi'(wu)Q(u)]u^T\,d\lambda,
\quad\dot A=-\frac2n\int r d(u)h(u)^T\,d\lambda,
\quad\dot c=-2\int r H(u)\,d\lambda.                 \tag{1}
\]

These formulas hold for every Borel probability law λ, with its exact
integral. On every finite-dimensional compact parameter set the integrands
and each parameter derivative are bounded uniformly in (u,y), since the
data domain is compact. The mean-value formula justifies differentiation
under the integral. Thus the field is smooth and locally Lipschitz.

In the finite raw metric

\[
\|(v,B,d)\|_{n,\mathrm{raw}}^2
=\|v\|_F^2/n+\|B\|_F^2+\|d\|_2^2/n,
\]

(1) is the negative gradient of Lλ=∫r²dλ. Differentiating Lλ gives

\[
L_\lambda(t)+\int_0^t\|\dot\theta(s)\|_{n,\mathrm{raw}}^2ds
=L_\lambda(0),\qquad
\|\theta(t)-\theta(s)\|_{n,\mathrm{raw}}
\le\sqrt{(t-s)L_\lambda(0)}.                         \tag{2}
\]

Indeed dL[v]=2∫r df[v]dλ and the three negative gradient blocks from
the normalized pairings are exactly (1). Integration and Cauchy–Schwarz
give (2). At fixed width this metric is equivalent to the ordinary
Euclidean parameter metric. A finite maximal endpoint would therefore
have a finite parameter limit; the local integral contraction there
extends the flow. All these finite flows exist globally and uniquely.

On the initialization event

\[
E_n=\{\|A_0\|_{op}\le10,\quad \|c_0\|_\infty\le1,
\quad\|w_0\|_F/\sqrt n\le2\},
\]

which has probability tending to one by P1's Gaussian estimates,
Lλ(0)≤(Y+1)² simultaneously for every λ. Every block displacement
through T is at most (Y+1)√T in its raw norm. Hence each of
\(\|w\|_F/\sqrt n,\|A\|_{op},\|c\|_2/\sqrt n\)
is at most B=11+(Y+1)√T. Also

\[
\|\dot c(t)\|_\infty\le2\int|r|d\lambda
\le2\sqrt{L_\lambda(t)}\le2(Y+1),\qquad
\|c(t)\|_\infty\le1+2T(Y+1).                         \tag{3}
\]

These estimates are independent of support cardinality or positive atom
weights. No sampling approximation has occurred.

On the canonical population carrier the identical assertions hold for
any *already existing* strong solution with C¹ raw state and c(0)=0,
with Lμ(0)=∫y²dμ≤Y². Scalar prediction differentiability is proved in
III.F.10 by weighted Taylor truncation. Its gradient is continuous
jointly in raw state and input: bounded multiplier continuity handles
each gate, bounded actions handle each matrix, and rank differences are
controlled in HS. On a compact input set this continuity is uniform near
any fixed state (otherwise extract a convergent input subsequence).
Thus the scalar loss is C¹ with gradient
\(2\int(f(u)-y)\nabla f(u)\,d\mu(u,y)\), and (2) follows in the population raw metric.
The readout equation integrated pointwise proves (3) with 2TY in place
of 1+2T(Y+1). These are a priori bounds, not existence or continuation
proofs at an arbitrary ambient endpoint.

## 2. Strengthening the transport estimate to HS increments

For states on the same carrier sharing A₀, set

\[
d_{\mathrm{raw},1}(\theta,\bar\theta)
=\|w-\bar w\|_2+\|K-\bar K\|_{HS}+\|c-\bar c\|_2.
\]

This lies between the square-sum raw norm and √3 times that norm. At
finite width its three summands are row Frobenius/√n, middle Frobenius,
and readout Euclidean/√n. There is no comparison across carriers.

On the B-ball just proved, C.4.1's transport estimate holds in this
stronger norm:

\[
\|F_\lambda(\theta)-F_\rho(\bar\theta)\|_{\mathrm{raw},1}
\le C_Y(1+R)(d_{\mathrm{raw},1}(\theta,\bar\theta)
                +\mathcal W_1(\lambda,\rho))
 +C_Y\left[\tau_R(\bar c)+\int\tau_R(\bar Q(u))d\rho\right]. \tag{4}
\]

Here τR(q)=∥q1{|q|>R}∥₂, with normalized empirical norms at finite
width. To verify the norm change rather than assume it, all forward and
adjoint differences use ∥K−Kbar∥op≤∥K−Kbar∥HS. For the middle
velocity the three subtracted rank terms in C.4.1 satisfy the exact same
bound because ∥a⊗b∥HS=∥a∥₂∥b∥₂. The first and last velocity norms
are unchanged. These are all occurrences of operator differences in
that proof. Thus its complete coupling, gate-truncation, and changing-u
calculation proves (4), with constants depending only on B,Y,T=40.

## 3. Comparison to the actual finite reference through time 40

Let θn,* be the actual finite GF on ν*, on the same initialized arrays.
The complete reference proof C.4.5.2 §5 and P1's source/capture proofs
give constants c,C,R₀>0 such that, for each fixed R≥R₀,

\[
\sup_{t\le T}\left[\tau_R(c_{n,*}(t))+
\tfrac12\sum_{a=1}^2\tau_R(Q_{n,*}(t,e_a))\right]
\le C e^{-cR^2}+o_{\mathbb P}(1).                       \tag{5}
\]

An inequality with oP(1) means its positive excess over the displayed
deterministic bound tends to zero in probability. Specifically the
population active Q is a Gaussian of bounded variance plus a bounded
remainder. Increase R₀ beyond four times that remainder bound to obtain
a Gaussian square tail. Fixed-time continuous positive-part cutoff
second moments pass through the reference width theorem. The L² time
Lipschitz bounds on Q extend them to all times by finite grids. Finally
∥q1{|q|>R}∥₂≤2∥(|q|−R/2)+∥₂ and the proved readout supremum bound
give (5). This is a statement at every fixed cutoff, not at a cutoff
growing with width. All reference proofs retain the finite random readout.

Apply (4) against this one reference; (2) already supplies a common ball
for both finite flows, so no existence of a changed-law population is
used. Integrate the velocity difference from the identical initialization.
For every deterministic sequence λn and each fixed R≥R₀,

\[
\sup_{t\le T}d_{n,\mathrm{raw},1}(\theta_{n,\lambda_n},\theta_{n,*})
\le C e^{aR}\{(1+R)\mathcal W_1(\lambda_n,\nu_*)
                         +e^{-cR^2}+o_{\mathbb P}(1)\}.       \tag{6}
\]

Here a,C depend only on Y and fixed T. The scalar inequality used is
E(t)≤∫₀ᵗ[LRE(s)+bR]ds, yielding E(t)≤TbR exp(TLR);
absorb T and exp(CYT) into C,a. The oP term comes only from the
fixed reference (5). Formula (6) also applies to sequences indexed by k
with arbitrary widths nk→∞ and Borel laws λk.

Consequently if W₁(λk,ν*)→0, the left side tends to zero in probability:
first fix R, take k→∞, and then take R→∞. The forward inequalities
give uniform-in-time, whole-circle prediction convergence to f*, and
uniform hidden RMS comparison on the same finite carrier. P1/B.1's
fixed-program reference identification then gives joint named same-layer
observations and second moments, both initialized/current action directions,
and paired initial/current hidden observables. For a backward multiplication,
truncate its reference field first; (5) and reference compact L² families
remove the cutoff. No neuronwise or operator-norm convergence between
finite and population carriers is involved.

Precisely, an admitted observation starts from a finite list of raw
fields w,c and the displayed h,z,H,d,Q at specified times and inputs,
and identified initialized generated fields. It applies finitely
many same-layer continuous globally Lipschitz coordinate operations,
fixed bounded continuous gates times named L² fields, and the actions A₀,A₀*,A(t),A(t)*,
K(t),K(t)* with matching layer types, and records its joint same-layer
law and quadratic contractions. For each fixed accuracy the reference
has a finite-program approximation; use its identical finite-array
realization for the changed flow comparison. Errors of each action
application are bounded by the input error times the bounded action
norm, plus the input norm times the same-carrier HS increment error.
For a bounded continuous gate times a named field use reference-field
truncation and a compact box for the gate arguments. Their identified
joint law and second moments give tightness and uniform integrability
on the complement of that box.
Finite induction proves convergence for this observation contract.
An arbitrary unbounded coordinate product is not an admitted operation.
Nonlinear clocks, inverse gates and their weighted products are not
starting fields unless separate moment and approximation proofs admit them.

One can also read (6) as a quantitative fixed-radius bound. For 0<q≤1
take R=max(R₀,K√log(e/q)) with cK²≥2. Enlarging constants gives

\[
\Phi_Y(q)=C_Y q\exp(C_Y\sqrt{\log(e/q)})\longrightarrow0.       \tag{7}
\]

If limsup W₁(λk,ν*)≤q, the positive excess of the left side of (6)
over ΦY(q) tends to zero in probability. For q>1 use the common raw
displacement bound from (2). Formula (7) compares to ν* only.

For independent samples from ν*, their empirical W₁ distance tends to
zero in probability. To prove this, partition the compact data space
into finitely many cells of diameter h and push both measures to cell
representatives, costing at most 2h. Their remaining cost is bounded
by half the data diameter times the sum of cell-mass discrepancies;
each cell frequency has variance at most 1/(4m). First take m→∞,
then h→0. The pathwise inequality (4) and the initialization-only
reference events give the preceding conclusions for every nk,mk→∞.
There is no relative rate. This paragraph concerns samples from ν*;
it does not establish the requested result for arbitrary μ near ν*.

## 4. Exact limitation

For a fixed changed μ at distance q>0, comparing two approximating laws
via the reference leaves an upper bound 2ΦY(q), which does not tend to
zero as the approximations refine. Thus (6) does not construct θμ.
Also ΦY(ε)/ε=CY exp(CY√log(e/ε)) diverges; it gives no bounded
contamination difference quotients and no first-order remainder.

Transferring reference tails by a fixed raw error η similarly gives only
τR(Qμ)≤2∥Qμ−Q*∥₂+2τR/2(Q*). A fixed positive first term cannot be
removed after multiplication by the exp(aR) comparison factor. This is
the precise failure of this comparison route, not a refutation of A–C.
