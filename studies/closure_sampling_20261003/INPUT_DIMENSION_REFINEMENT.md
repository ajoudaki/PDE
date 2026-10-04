# Input dimension: spherical counting and strict root-width folding

2026-10-04. Continuation of the same autonomous sampling/compression study.
This note assembles the new dimension results. They are internally checked
research results relative to the study's already checked training,
insertion, source and runtime theorems, not promoted manuscript claims.
No numerical experiment or maintained-manuscript edit was made.

There are two distinct improvements. First, intrinsic spherical sources
remove the growing dimension-only prefactor even for full-rank data.
Second, a fixed radial preprocessing of queries replaces ambient input
dimension in the expensive source count by training rank plus one,
without the earlier square-root-logarithmic error loss. The latter
changes the representation, while retaining the same realized dense
training problem as the reference.

## 1. Common model and assumptions

For v=x/sqrt(d), the canonical dense reference is
\[
z^{(1)}=Av,\quad z^{(j)}=W^{(j)}h^{(j-1)}\ (j\ge2),\quad
h^{(j)}=\phi_j(z^{(j)}),\quad f_n=w^\top h^{(L)}/n.
\]
All L>=2 hidden layers have width n. Initial entries of A are independent
N(0,1), hidden W entries are independent N(0,1/n), initialized blocks are
independent, and w(0)=0. Train on m fixed inputs of norm sqrt(d), with
mean squared loss and mobilities (n,1,...,1,n), in physical time.

Every activation is real on the real axis, holomorphic on |Im z|<a and
bounded there by B_phi. Put B=max(1,B_phi). Let s,t_phi>=1 bound its
first two derivatives on |Im z|<=a/2, and set
\[
\beta=\max(10,B,s,t_\phi,16/a).
\]
The common bounds apply to every layer. The choices
s=max(1,4B/a), t_phi=max(1,32B/a^2) always suffice. For tanh,
the previously checked choice is beta=16.

Define Q^0_ab=v_a^Tv_b and
Q^j_ab=E[phi_j(Z_a)phi_j(Z_b)], Z~N(0,Q^{j-1}). Let
\[
\gamma=\lambda_{\min}(Q^L)>0,\quad
Y=\|y\|_2/\sqrt m,\quad \ell_n=\log(en).
\]
There is no normalization by m in gamma. Keep exactly the previous
complete sufficient label condition
\[
Y\le(\gamma/m)\beta^{-62L}.                                  \tag{1}
\]
Labels may have arbitrary individual signs and ratios. If Y=0 the exact
stationary zero predictor suffices. The data need not be orthogonal.

Every probability statement below is at any fixed confidence, for each
sufficiently large n with architecture, dataset and labels fixed. All
displayed error constants are independent of width and physical time.
The width threshold is unquantified; this is not a theorem for growing
d,L,m or an event simultaneous over every width.

## 2. A dimension-only prefactor that no longer grows

Let S_C count all retained moving and fixed real coordinates, including
data, metrics and solve caches. The spherical source construction gives
\[
\begin{split}
S_C\le{}&\beta^{82Ld}\frac{(d+3)^d}{(d!)^2}
 (m/\gamma)^2\ell_n^{3d+2}\\
 &+2040(L+1)(2m+d+1)^2+10m(d+1),                              \tag{2}
\end{split}
\]
with the unchanged error
\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
\le\beta^{124L}Y(m/\gamma)^{3/2}/\sqrt n.                     \tag{3}
\]
In (2),
\[
\frac{(d+3)^d}{(d!)^2}\le\frac{25}{4},\qquad
\frac{(d+3)^d}{(d!)^2}\le e^3(e^2/d)^d.                       \tag{4}
\]
Thus no superexponentially growing d^d prefactor survives. This is stronger
than simply absorbing that factor into a larger activation constant.
The exact-initialization polynomial in the second line stays visible
because the factorial coefficient can decay with dimension.

The proof uses a complex great-circle tube of radius
c_q/sqrt(log(en)), with c_q^{-1}<=beta^(32L)sqrt(d+3), and spherical
harmonics instead of independent angular Fourier modes. The count of
joint time/spherical degrees has its natural factor 1/d!. Squaring the
source rank gives exactly (4). The harmonic functions are temporary setup
tools; the autonomous runtime still evaluates selected neurons and its
moving hidden matrices. It retains no harmonic evaluator or source table.

The complete argument is `SPHERICAL_SOURCE_DIMENSION_ROUTE.md`, checked
in `SPHERICAL_SOURCE_DIMENSION_CHECK.md`, with the author's extra storage,
off-grid and elementary completeness checks in
`SPHERICAL_SOURCE_ADDITIONAL_CHECK.md`. An independent proof optimization
that already removes the coarse (d+3)^d factor, without spherical
harmonics, is `EUCLIDEAN_ANGLE_DIMENSION_ROUTE.md`, checked in
`EUCLIDEAN_ANGLE_DIMENSION_CHECK.md`.

## 3. Replace ambient dimension by training rank plus one

Let V=span{x_1,...,x_m}, r=dim(V), and
\[
D=\min(d,r+1)\le m+1.                                       \tag{5}
\]
The rank is an observed property of the given dataset, not an additional
assumption. Choose an orthonormal basis U for V. If r+1<d, use the fixed
query map
\[
v\longmapsto
\left(U^\top v,\sqrt{\|v\|_2^2-\|U^\top v\|_2^2}\right)
\in S^{D-1}.                                                \tag{6}
\]
The last coordinate retains the length of the unobserved component.
The map is well-defined and continuous, including at training inputs,
where that coordinate is zero. It is the only new runtime operation.
No test labels are required. If r+1>=d, omit this map and use (2).

The modified autonomous representation has total retained size
\[
\begin{split}
S_C\le{}&\beta^{82LD}\frac{(D+3)^D}{(D!)^2}
       (m/\gamma)^2\ell_n^{3D+2}\\
 &+2040(L+1)(2m+D+1)^2+10m(d+1)+10d(r+1).                    \tag{7}
\end{split}
\]
The last term is a conservative count for the fixed projection and query
work vectors; omit it when no folding is used. The data allowance bounds
the retained restricted training coordinates and the existing runtime
caches. The original full training inputs need not remain after setup;
retaining them additionally costs m(d+1) coordinates.
In particular, every expensive dimension exponent in (7) uses D rather
than d, and (D+3)^D/(D!)^2 is at most 25/4. At fixed m, the displayed
storage depends on ambient d only polynomially.

For any fixed confidence 1-delta, put
J_delta=d+1+log(1/delta). The error remains strictly
\[
\sup_{t\in[0,\infty]}\sup_{\|x\|=\sqrt d}|f_C(t,x)-f_n(t,x)|
\le[\beta^{124L}+\beta^{44L}J_\delta]
       Y(m/\gamma)^{3/2}/\sqrt n.                            \tag{8}
\]
This compares the same realized initialization at equal physical times,
including the fitted endpoint. A simpler envelope is
beta^(130L) J_delta Y(m/gamma)^(3/2)/sqrt(n). The new folding
contribution is included explicitly; it costs only a linear ambient-d
factor, not an unreported exponential constant. When no folding is used,
retain the sharper dimension-independent coefficient in (3).

The constant calculation is `INTRINSIC_FOLDING_CONSTANT_ROUTE.md`.
Its singleton shift is at most beta^(20L)S. The resulting query carrier
moments grow at most beta^(25L)S sqrt(p), and Gaussian operator moments
are dimension-independent once n>=d+p. Gaussian rotation then gives
increment coefficient beta^(35L)pS. Taking one fixed
p=max(4(d+1),log(2/delta)) makes the exponential net count contribute
only a numerical factor. Folding is bounded by
beta^(40L)S[d+1+log(1/delta)]/sqrt(n). Split the failure probability
between folding and compression and use
S<=beta^(3L)Y(m/gamma)^(3/2); the additional log(2) is absorbed by
one more beta^L. This gives the sharper sum in (8), rather than merely
its beta^(130L) envelope. No stronger label condition is used.

## 4. Why the folding error is root-width through fitting

Complete the active basis U to an orthogonal basis [U,E]. The exact
first-weight update has columns only in V, so
\[
A(t)E=A(0)E=:G.
\]
The full training path is determined by A(0)U, the initialized hidden
mixers and the data; these are independent of the standard Gaussian
matrix G. Let this training information generate the sigma-field F.
Conditional on F, query outputs depend on the unused input component
through GE^Tv. Their conditional mean therefore depends only on U^Tv
and ||E^Tv||. This identity alone does not justify replacing an entire
random function by its mean uniformly at the root-width scale.

The new ingredient is an actual finite-network carrier moment estimate.
Define the passive query backward fields by k^L=w,
delta^j=phi'_j(z^j) odot k^j and k^j=W^{j+1,T}delta^{j+1}. With
lambda=min(1,gamma/m), S=16Y/lambda, there is an F-measurable training
event E_n of probability tending to one such that, for every fixed p,
\[
\sup_{t,v,j}\mathbb E\left[
 \mathbf1_{E_n}\frac1n\sum_i|k_i^j(t,v)|^p\right]\le C_pS^p. \tag{9}
\]
The constant is uniform over the individual query and time. No query
supremum is inside this moment, and E_n contains no restriction on G.

The proof extends singleton Gaussian insertion to passive backward
observables. Its query endpoint needs only a normalized
Hilbert--Schmidt bound, supplied by carrier RMS. In a term with h
training Hessians, give that query endpoint Schatten exponent 2 and the
h+1 training factors exponent 2(h+1). The reciprocal exponents add to
one and the resulting Dyson series converges under the existing label
restriction. No new query exponential budget is assumed.

The stopped query calculation has arbitrarily high fixed polynomial
failure probability *intersected with E_n*. Off that event, the
deterministic RMS bound gives |k_i|<=CSsqrt(n). These two facts prove
(9) without requiring a polynomial rate for Pr(E_n^c), and without
conditioning a Gaussian root on the trained network's survival.

For real z,z', boundedness and Lipschitz continuity of phi' give
\[
\|\phi'(z)-\phi'(z')\|_{4,n}
\le C\|z-z'\|_{2,n}^{1/2}.
\]
Pair this changed gate with a reference carrier in counting-four norm.
The backward difference then has a half-Hölder moment bound in the
query and deterministic proof clock tau=1-exp(-lambda t/4). Gaussian
rotation applied to the exact conditional derivative
\[
\nabla_G f_n(t,v)=n^{-1}\delta^1(t,v)(E^Tv)^\top
\]
gives the same half-Hölder bound for sqrt(n) times the centered output.
One fixed p>2(d+1) makes the resulting finite-dimensional net sum
converge, with no log(n) loss. Integrable residual activity extends the
bound continuously to tau=1, the fitted endpoint.

Choose one fixed unit e in V-perp and fold a query to
P_Vv+||P_{V-perp}v||e. The two conditional means agree exactly, so twice
the centered supremum controls their output difference. Restricting the
same initialized dense model to [U,e] gives an exactly canonical
D-dimensional first matrix, the same training hidden matrices and
readout path, and the same Gram gap gamma. Apply the spherical
compressor in dimension D and add the folding error. The conditional
mean and G are proof objects only; neither is retained at runtime.

The full new argument is `INTRINSIC_STRICT_ROOT_ROUTE.md`. Its new
insertion/moment implication is checked in
`INTRINSIC_STRICT_ROOT_INSERTION_CHECK.md`; the moment-to-chaining and
canonical-restriction implication is separately checked in
`INTRINSIC_STRICT_ROOT_CHAINING_CHECK.md`. Together these close the
previous sqrt(log(n)/n) route's missing estimate. They do not assume the
older unproved high-angular-derivative Sobolev condition.

## 5. What remains expensive

For d=1000 and ten training inputs, D<=11. Thus the storage power
log(en)^(3002) becomes at most log(en)^35, and beta^(82000L)
becomes at most beta^(902L). The fixed projection and data are still
counted. These are improvements in a sufficient asymptotic theorem,
not an assertion that those remaining conservative constants are small.

If the training span fills input space, D=d, and the rank step supplies
no additional reduction. The universal spherical improvement (2)--(4)
still applies. No theorem here makes storage polynomial in the intrinsic
rank or removes beta^(O(LD)). No lower bound proves those remaining
costs necessary for arbitrary autonomous representations.

The companion `DIMENSION_ALTERNATIVE_ROUTE.md` gives exact finite counts
and obstructions for broader analytic source classes. Those are not
neural lower bounds and are not premises of the positive results here.
The old whole-feature source-space obstruction is also consistent with
folding: folding compares scalar predictions first, and only then
compresses a restricted realized network. It does not approximate every
original first-layer feature in a dimension-free subspace.

The optimizer remains the previously specified autonomous system with
fixed neuron metrics, its own moving residual and algebraically corrected
readout; it is not ordinary gradient flow on an iid smaller network.
There is no clipping or trained-trajectory playback. Exact-real setup
work, precision and the sufficiently-large-width threshold remain
unquantified. The manuscript and maintained theorem book are unchanged.

## 6. Check status and source versions

The coordinator read the complete new candidates and reconstruction
reports, checked their composition against the actual runtime interface,
and reconstructed the quantitative folding calculation. The detailed
assembly check is `INPUT_DIMENSION_ASSEMBLY_CHECK.md`. The separate
quantitative check is `INTRINSIC_FOLDING_CONSTANT_CHECK.md`.

The frozen mathematical candidates used here are:

| Candidate | SHA-256 |
| --- | --- |
| SPHERICAL_SOURCE_DIMENSION_ROUTE.md | bba804ec958860eff8eceaeda212a1e6bf391fb82c5b0e0224bfe870d98728a8 |
| EUCLIDEAN_ANGLE_DIMENSION_ROUTE.md | 9f452338619a0c7334bae8944454f71309f2314a65c844f84150b947ba41c9d7 |
| INTRINSIC_STRICT_ROOT_ROUTE.md | c3c1e5d10c32458ca08dbbbe6251efdb0ee400e5301a50aff943d7064d6ad7d1 |
| INTRINSIC_FOLDING_CONSTANT_ROUTE.md | f2c56abd842fe90533cab3f9b0f558f91ac1c1601697c226ea8f3b97082014c4 |

Source files remain frozen; the clarifications in the checks are that
the training event includes the all-time real fitting tube, the moment
failure estimate is Pr(E_n intersect bad)<=C_M n^(-M), and all positive
label-RMS statements allow arbitrary individual label signs. These are
the scopes used above. None is a new scientific assumption.
