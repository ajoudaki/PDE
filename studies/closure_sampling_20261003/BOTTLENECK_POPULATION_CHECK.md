# Internal reconstruction of the compact bottleneck benchmark

2026-10-03. Scoped mathematical check of the complete
BOTTLENECK_POPULATION_ROUTE.md, including its equal-width lift in Section 4.
The read source SHA-256 is
\`96dd2fc5c16d9a638300836626764c0ab22c69c58698793d3a2fd21e879d26aa\`.
This is an internal reconstruction, not a promotion review. I read only the
assigned route and required instructions for this check. No source edit,
experiment, Git write, or other new route-file read was performed.

**Verdict.** The substantive proof checks: initial polynomial cubature gives
a positive autonomous sampler with \(O((\log n)^{d+k})\) moving coordinates,
and error \(CY/\sqrt n\) against the actual realized finite network,
uniformly in physical time and all queries in the stated ball, including
both fitted endpoints. The equal-width lift exactly matches the original
dense architecture's physical time and mobilities. It has structured
rank-at-most-\(k\) initialization and therefore does not prove compression
for ordinary equal-width iid Gaussian initialization.

There is one minor domain-radius clarification: the analytic-neighborhood
radius in Section 3 must be interpreted in the maximum coordinate norm, or
shrunk by \(\sqrt{d+k}\) before it is used as the common radius of a complex
coordinate polydisc. The proof below makes this harmless fixed-constant
adjustment explicit. No substantive estimate depends on that choice.

## 1. Network equations, metric, and fitting

Let \(n\) be the lower width, \(k\) the fixed upper width, and
\(m\) the number of examples. A lower particle stores
\(a_i\in\mathbb R^d\) and \(b_i\in\mathbb R^k\). For
\(v_a=x_a/\sqrt d\), the forward pass is

\[
 h_{i,a}=\tanh(a_i^\top v_a),\qquad
 z_a=\frac1n\sum_i b_i h_{i,a},\qquad
 g_a=\tanh z_a,\qquad f_a=w^\top g_a/k.
\]

The source defines \(r_a=f_a-y_a\) and
\(\delta_a=w\odot\operatorname{sech}^2z_a\), and uses loss
\(m^{-1}\sum_a r_a^2\). Differentiating \(f_a\) gives

\[
 \partial_{a_i}f_a
  =\frac1{kn}\operatorname{sech}^2(a_i^\top v_a)
            (b_i^\top\delta_a)v_a,\qquad
 \partial_{b_i}f_a=\frac1{kn}\delta_a h_{i,a},\qquad
 \partial_w f_a=g_a/k.
\]

Multiplication by the respective mobilities \(n,nk,k\) proves all three
displayed physical-time equations in Section 1. The physical edge matrix is
\(b_i/n\); changing variables therefore gives its mobility
\((nk)/n^2=k/n\), as stated.

The induced prediction Gram is the sum over these parameter blocks:

\[
 K_{ab}=\frac{g_a^\top g_b}{k}
 +\frac{\delta_a^\top\delta_b}{k}\mathbb E_n[h_a h_b]
 +\frac{v_a^\top v_b}{k^2}
   \mathbb E_n[
    \operatorname{sech}^2(a^\top v_a)
    \operatorname{sech}^2(a^\top v_b)
    (b^\top\delta_a)(b^\top\delta_b)].
\]

Each term is a Gram matrix for the corresponding scaled derivative
features, so \(K\) is positive semidefinite and
\(\dot r=-(2/m)Kr\). In particular, no readout factor \(k\) or particle
factor \(n\) is missing from the source.

Take \(D(t)\) here to be the maximum of the two block displacements over
all particles. If initial \(|b_i|\le B\), and \(D\le1\), then
\(|z_a-z_a(0)|\le(B+1)D\). Let \(G\) be the matrix with rows
\(g_a^\top\). Its rows have norm at most \(\sqrt k\), while
\(\|G-G(0)\|_{\rm op}\le\sqrt m(B+1)D\). Hence

\[
 \left\|\frac{GG^\top-G(0)G(0)^\top}{k}\right\|_{\rm op}
 \le \frac{2m(B+1)}{\sqrt k}D
 \le 2m(B+1)D.
\]

The stated choice \(D_0=\min(1,\kappa/[4m(1+B)])\) consequently preserves
\(K\succeq\kappa I/2\), implying

\[
 |r(t)|\le Y e^{-\kappa t/m},\qquad
 \int_0^\infty|r(t)|dt\le mY/\kappa.
\]

Here \(Y=|y|\) is the Euclidean label norm, consistently with the source.
The readout bound follows from
\(|\dot w|\le2\sqrt{k/m}|r|\). The particle bounds follow from

\[
 |\dot b_i|\le2|r||w|/\sqrt m,\qquad
 |\dot a_i|\le2(B+1)|r||w|/(k\sqrt m).
\]

They give exactly the stated allowable constants \(C_w,C_D\). Strict
small-label margins exclude the first displacement exit. The resulting
bounded state and integrable speeds provide global continuation, finite
total variation, and fitted endpoints. Positive empirical weights replace
all averages without changing any estimate.

## 2. Correlated data, the Gram event, and genuine hidden motion

For \(d=k=m=2\), the two unit inputs
\(v_1=(1,0)\), \(v_2=(1,1)/\sqrt2\) have nonzero correlation
\(v_1^\top v_2=1/\sqrt2\). The two ideal seed atoms in the source yield

\[
 z_1=(\tanh1,\tfrac12\tanh1),\qquad
 z_2=(\tfrac32\tanh(1/\sqrt2),
               \tfrac32\tanh(1/\sqrt2)).
\]

Thus the displayed matrix \(G_*\) is correct. Its determinant
\(h(u-v)>0\) proves a positive smallest singular value \(\sigma_*\).

For a seed in an \(\eta\)-neighborhood of either atom,
each scalar integrand \(b_j\tanh(a^\top v)\) changes by at most
\(\eta+2\eta=3\eta\). A cluster proportion change of at most \(\alpha\)
contributes at most \(2\alpha\). A \(2\)-by-\(2\) matrix whose entries
are bounded by \(3\eta+2\alpha\) has operator norm at most
\(2(3\eta+2\alpha)\). With
\(\eta=\alpha=\sigma_*/64\), this is strictly below
\(\sigma_*/2\), so
\(\lambda_{\min}(GG^\top/2)\ge\sigma_*^2/8\).
The Bernoulli cluster event has the stated probability by the elementary
bounded-variable exponential moment estimate. The continuous within-cluster
sampling law affects none of these deterministic inequalities.

For labels \((\epsilon,0)\), zero initial readout gives
\(\dot w(0)=\epsilon g_1\), vanishing initial hidden velocities, and
\(\dot\delta_1(0)=\epsilon\gamma\), where
\(\gamma=g_1\odot\operatorname{sech}^2z_1\).
Differentiating each hidden equation therefore gives

\[
 \ddot a_i(0)=\frac{\epsilon^2}{k}
   \operatorname{sech}^2(a_i^\top v_1)(b_i^\top\gamma)v_1,
 \qquad
 \ddot b_i(0)=\epsilon^2\gamma h_{i,1}.
\]

Differentiating \(h_{i,1}\) and
\(z_{j,1}=\mathbb E_n[b_j h_1]\), using their vanishing first derivatives,
gives exactly the two acceleration formulas in the source.

All \(b_j\) remain strictly positive in the fixed initial neighborhoods;
the cluster event bounds each initial \(z_{j,1}\) away from zero.
Thus every coordinate of \(\gamma\) is bounded below by a fixed positive
constant. The lower preactivations lie in a fixed compact set, so their
gates have a fixed positive lower bound. Consequently the displayed lower
feature accelerations and upper preactivation accelerations have uniform
positive lower bounds \(c\epsilon^2\), independently of width.

For completeness, these acceleration statements do imply feature motion
at a fixed physical time. On a sufficiently short fixed interval, the
bounded source equations give
\[
 |r|+|\dot r|+|\ddot r|\le C|\epsilon|,\qquad
 |w|+|\dot w|+|\ddot w|\le C|\epsilon|.
\]
The hidden first, second, and third derivatives are then bounded by
\(C\epsilon^2\): every hidden update contains a residual and a readout
factor, and differentiation preserves two factors of order
\(|\epsilon|\). Tanh and its fixed-order derivatives are bounded on the
visited compact sets, and positive averages introduce no width factor.
The same third-derivative bound holds for both hidden feature layers.
Taylor's integral remainder therefore yields
\[
 h_{i,1}(t)-h_{i,1}(0)
 \ge \tfrac12c\epsilon^2t^2-\tfrac16C\epsilon^2t^3,
\]
and the corresponding bound for every upper training feature. Choosing
one sufficiently small \(t_0>0\) makes these positive lower bounds
independent of \(n\), and uniformly proportional to \(\epsilon^2\) for
small labels.

The first cluster has fixed positive mass near preactivation one, and the
upper preactivations are uniformly positive. On those visited compact
sets tanh has nonzero second derivative. The example therefore retains
nonlinearity and hidden feature motion, rather than merely nonzero
parameter derivatives or a changing readout.

## 3. Holomorphic seed dependence through the endpoint

For a fixed realized empirical model, freeze only its common controls
\(r(t),w(t),z_a(t)\) in a proof-only off-support particle equation.
These are the actual controls of that model. The independent seed variable
is \(\theta=(a(0),b(0))\), not the entire trained initialization.

On a fixed bounded complex tube around the real particle trajectories,
the first preactivations stay strictly inside tanh's pole-free strip.
The particle vector field is then holomorphic in \((a,b)\), and its
spatial derivative satisfies
\[
 \|D_{(a,b)}V(t,a,b)\|\le C|r(t)||w(t)|.
\]
The factor \(w\) comes from \(\delta_a\); differentiating the particle
variables does not differentiate the common controls.
Their proved bounds give
\[
 \int_0^\infty C|r(t)||w(t)|dt\le CY^2.
\]

Complex-versus-real particle subtraction and Gronwall show that an
initial perturbation of size \(\rho\) remains at most
\(\rho e^{CY^2}\). Taking \(\rho\) smaller than the chosen complex tube
margin excludes its first exit. Picard iteration on each finite time
interval gives holomorphic seed dependence. On a compact subset of the
allowed complex seed neighborhood, the particle speed is bounded by
\(C|r||w|\), uniformly in the seed. This is integrable through infinite
time, so the holomorphic maps converge locally uniformly to the endpoint
map.

For any passive \(|v|\le1\), the imaginary part of \(a^\top v\) is bounded
by \(|\operatorname{Im}a|\); hence the same tube controls all passive
tanh evaluations. The functions \(F,P,Q\) in Section 2 are consequently
holomorphic and uniformly bounded in one common seed neighborhood, over
all physical times including the endpoint and over the whole passive ball.

This argument also applies to all initial seeds in a fixed containing box.
Off-support \(a,b\) remain bounded because their speeds are at most
\(C|r||w|\); constants may enlarge with the box but remain independent of
width and cubature weights. No inaccessible trajectory data enter the
eventual cubature construction.

## 4. Polynomial cubature and simultaneous source error

Let \(D=d+k\). Choose a common coordinate polydisc radius \(\rho_0>0\)
whose discs centered in the seed box lie inside the holomorphic
neighborhood. If the original neighborhood is specified using Euclidean
distance, take \(\rho_0\le\rho/\sqrt D\). This is the domain-radius
clarification identified in the verdict.

Partition the box into finitely many cells with coordinate diameter at most
\(\rho_0/(2D)\). For a cell center \(c\), Cauchy's formula in each
coordinate bounds a Taylor coefficient by \(M\rho_0^{-|\alpha|}\).
For points with
\(\max_j|\theta_j-c_j|\le\rho_0/(4D)\), the total-degree tail after
degree \(p\) is bounded by
\[
 M\sum_{s>p}\binom{s+D-1}{D-1}(4D)^{-s}\le C_D M2^{-p}.
\]
The last estimate follows because the binomial factor is polynomial in
\(s\) at fixed \(D\), while \((4D)^{-s}\) decays faster than \(2^{-s}\).

For each nonempty cell, the monomial evaluation vector has dimension
\(J=\binom{D+p}{D}\), including the constant. A linear dependence among
more than \(J\) supported nodes has coefficients summing to zero, hence
both signs. Moving the positive weights along that dependence until the
first zero weight preserves every moment and the cell mass. Repetition
leaves at most \(J\) positive nodes in that cell.

The original measure and the resulting cubature measure therefore
integrate each cell's Taylor polynomial identically. Their integration
error for any \(F,P,Q\) is at most twice its uniform Taylor error times
the cell mass; summing masses gives
\(\varepsilon\le CM2^{-p}\). Because the analytic bound is uniform, this
one initial construction works simultaneously for the infinite family of
times and passive queries. Its algorithm matches initial monomials only,
and never computes the Taylor coefficients of a trained source.

The support bound is \(N\le L\binom{D+p}{D}\). Empty cells contribute
nothing. Selecting \(p=\lceil\frac12\log_2n\rceil+p_0\) gives
\(N=O((\log(e+n))^D)\) and source error \(C/\sqrt n\), with \(p_0\)
large enough for the reduced initial Gram margin.

## 5. Feedback and the uniform physical-time comparison

Compare original and reduced off-support particle maps at the same initial
seed. Let \(D(t)\) be their largest summed particle displacement on the
seed box, \(W(t)=|w_\nu-w_\mu|\), and \(E(t)=|r_\nu-r_\mu|\).
Split every integral difference into a difference of particle maps under
one positive measure and an integration defect for the original map.
This gives the source's
\[
 |z_\nu(t,v)-z_\mu(t,v)|\le C(D+\varepsilon).
\]

The readout responses satisfy
\[
 |\delta_\nu-\delta_\mu|
 \le W+CY(D+\varepsilon).
\]
Inserting this into the explicit three-term kernel, with the \(P,Q\)
integration defects, gives
\[
 \|K_\nu-K_\mu\|_{\rm op}
 \le C(D+YW+\varepsilon).
\]
The factor \(Y\) on \(W\) is correct because the last two kernel terms
contain two backward responses, each of size \(O(Y)\). Their weight
differences therefore contain one remaining factor \(O(Y)\).

The reduced positive kernel yields a damped residual difference,
\[
 D^+E\le-\gamma E+CR(D+YW+\varepsilon),
 \quad R(t)=|r_\mu(t)|\le Ye^{-\gamma t},\quad E(0)=0.
\]
Integrating the scalar convolution through a finite terminal time gives
\(\int E\le CY(D_T+YW_T+\varepsilon)\). Subtracting the readout equation
then gives
\[
 W_T\le CYD_T+CY^2W_T+CY\varepsilon.
\]
Subtracting the particle equations gives first
\[
 D_T\le CY\int E+C\int RW+CY\int R(D+\varepsilon),
\]
and hence
\[
 D_T\le CYW_T+CY^2D_T+CY^2\varepsilon.
\]
These estimates use the reduced bounded state only in the terms carrying
the residual difference, and the original decaying residual in the other
terms. No nonintegrable constant forcing is introduced.

All constants are chosen before the label threshold. For small fixed \(Y\),
absorb the \(CY^2\) terms in the first inequality, substitute its result
into the second, and absorb once more. This gives
\[
 W_T\le CY\varepsilon,\qquad D_T\le CY^2\varepsilon
\]
uniformly in \(T\). The query prediction difference is bounded by
\(CW+CY(D+\varepsilon)\), proving the stated \(CY/\sqrt n\)
all-time and whole-input conclusion after cubature.

Both models have integrable parameter speeds, so their fitted endpoint
predictions are limits of the same-time comparison. This proves the
endpoint statement directly. No width limit or exchange of time and width
limits enters the argument.

## 6. Exact equal-width realization and remaining scope

Suppose \(k\) divides \(n\). Clone each upper bottleneck neuron into a group
of \(n/k\) identical rows in the width-\(n\) dense network. Initialize
the row in group \(\ell\) by \(W^{(2)}_{ji}=b_{\ell i}/n\) and all
readouts at zero. Permutation invariance within each group and uniqueness
preserve equality of every row and readout coordinate in the group.

The full dense prediction is therefore
\[
 \frac1n\sum_j w_jg_j=\frac1k\sum_\ell w_\ell g_\ell,
\]
and its exact lower backward action is
\[
 (W^{(2)\top}\delta^{(2)})_i
  =\frac1k\sum_\ell b_{\ell i}\delta_\ell.
\]
The original dense mobilities \(n,1,n\) consequently give precisely the
source's \(a,w\) equations. Its middle equation is
\(\dot W^{(2)}_{ji}=-(2/(mn))\sum_a r_a\delta_{\ell,a}h_{i,a}\);
multiplying by \(n\) gives the bottleneck \(b\) equation. Thus physical
time, training predictions, passive predictions, and endpoints agree
exactly. There is no hidden time rescaling or freezing of trained entries.

For \(k=2\), the construction works for every sufficiently large even
\(n\). Its initialization is rank at most \(2\), and the upper row
symmetry persists. The \(n\) lower particles remain continuously
heterogeneous and learn. Clone reduction by itself leaves
\(n(d+k)+k\) moving coordinates, whereas the initial cubature removes
that remaining linear dependence on \(n\).

The sampling theorem is therefore a genuine positive finite-network
benchmark with two nonlinear learning layers, correlated data, its own
coupled residual dynamics, full-time error control, and no trained-path
oracle. Its conclusion must always retain the compact structured
initialization restriction. It supplies no canonical Gaussian sampler,
no approximation theorem for the original Gaussian response-memory
closure, and no reason to weaken the separate canonical research target.

## 7. Final corrected-version confirmation

I reread the complete corrected route, including the revised scope header,
the explicit maximum-of-blocks definition of \(D\), the short-time third
derivative estimate, the three-preactivation nonaffinity certificate, and
the complex-neighborhood norm. Its final SHA-256 is
6c4e6b3f562176b87ce09564deba9b2f4d57891eef3703e9a6bac1ad50938cf4.
**Final verdict: PASS with the earlier radius clarification resolved.**

The definition
\[
 D(t)=\max_i\max\bigl(
      |a_i(t)-a_i(0)|,\ |b_i(t)-b_i(0)|\bigr)
\]
now agrees explicitly with the constants reconstructed in Section 1.
The third-derivative paragraph supplies the \(C\epsilon^2\) remainder
scale used in the feature-displacement argument reconstructed in
Section 2.

The three displayed positive upper preactivations are distinct. The first
two are \(\tfrac12\tanh1<\tanh1\), while strict concavity of tanh and
\(\tanh0=0\) give
\[
 \tanh1<\sqrt2\,\tanh(1/\sqrt2)
           <\tfrac32\tanh(1/\sqrt2).
\]
Strict concavity also makes the three activation values noncollinear.
This is an open condition on the three preactivation values and their
images, so the stated sufficiently small fixed neighborhood and cluster
perturbations preserve it. Reducing the fixed radii, if necessary, only
strengthens the previous Gram perturbation estimate.

The analytic neighborhood is now explicitly measured in maximum
coordinate distance, and its Euclidean-tube construction includes the
factor \(\sqrt{d+k}\). Hence each coordinate polydisc used for Cauchy
estimates lies in the certified holomorphic neighborhood. This resolves
the only literal domain-radius issue identified in the original check.

The final header accurately identifies the result as a compact bottleneck
benchmark with an exact structured equal-width lift. It remains separate
from the canonical iid Gaussian theorem and supplies no additional claim
about that ensemble.
