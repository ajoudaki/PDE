# An odd activation formed by a convex combination under absolute angular separation

This report proves a global two-input theorem for the literal activation
\[
             \psi_e(z)=(1-e)z+e\arctan z.                 \tag{T.1}
\]
It also proves initialization results for three inputs, including sharp
worst-case conditioning of their first feature Gram, and a conditional
continuation criterion under a separately stated exponential-tail hypothesis. The complete global
three-input extension under pairwise separation alone remains open here.
The distinction is part of the statement, not an omitted hypothesis.

Every specialized mathematical dependency is reproduced in the appendices.
In particular the Gaussian-program, response, and finite-algorithm arguments
in Appendix C are used through their proved intermediate lemmas, with the
changed hypotheses checked below. Its shifted-activation main theorem is
not invoked as a theorem about (T.1).

## 1. Exact two-input theorem

Fix \(0<\delta\le1\), an integer \(d\ge1\), deterministic inputs and labels
\[
 \|x_1\|^2=\|x_2\|^2=d,\qquad
 \rho=x_1^Tx_2/d,\qquad |\rho|\le1-\delta,
 \qquad y_1,y_2\in\{-1,1\}.                             \tag{T.2}
\]
Only realizable configurations are quantified over. The user's strict
interval is a subset of (T.2); its nonempty range is \(0<\delta<1\).
The closed case \(\delta=1\) allows orthogonal inputs.

At width \(n\), take mutually independent entries
\[
 W^1_{jk}(0)\sim N(0,1/d),\quad
 W^2_{jk}(0),W^3_{jk}(0)\sim N(0,1/n),\quad
 C_j(0)\sim N(0,n^{-2}).                                \tag{T.3}
\]
Here \(W^1\) has size \(n\times d\), \(W^2,W^3\) have size
\(n\times n\), and \(C\in\mathbb R^n\). With
\(\langle u,v\rangle_n=n^{-1}u^Tv\), define, for \(i=1,2\),
\[
 z_i^1=W^1x_i,\quad h_i^\ell=\psi_e(z_i^\ell),\quad
 z_i^2=W^2h_i^1,\quad z_i^3=W^3h_i^2,
 \quad f_i=\langle C,h_i^3\rangle_n,
 \quad r_i=f_i-y_i,\quad L=\tfrac12\sum_i r_i^2.
                                                               \tag{T.4}
\]
All activations and gates act coordinatewise. Put
\[
 b_i^3=C\psi_e'(z_i^3),\quad
 b_i^2=\psi_e'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\psi_e'(z_i^1)(W^2)^Tb_i^2.                       \tag{T.5}
\]
The raw metric and its exact negative gradient field are
\[
 \|\Delta\theta\|_{{\rm raw},n}^2
 =\frac dn\|\Delta W^1\|_F^2+\|\Delta W^2\|_F^2+
   \|\Delta W^3\|_F^2+\|\Delta C\|_n^2,
\]
\[
 \dot W^1=-d^{-1}\sum_i r_i b_i^1x_i^T,\quad
 \dot W^\ell=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T
 \ (\ell=2,3),\quad \dot C=-\sum_i r_i h_i^3.           \tag{T.6}
\]
Raw GD means simultaneous explicit Euler for exactly (T.6), with step
\(\eta_n=n^{-2}\) and the same initialization as GF. Interpolate raw
parameters linearly; recompute hidden fields from the interpolated
parameters. Their velocities use the right derivative at a node and the
left derivative at a terminal observation endpoint. The finite readout
in (T.3) is retained throughout.

The canonical population has three separate neuron spaces
\(H_\ell=L^2(\Omega_\ell,\mu_\ell)\), constructed in Appendix C, Part F.
Its state consists of
\[
 w\in L^2(\Omega_1;\mathbb R^d),\quad
 A\in A_0+\mathcal S_2(H_1,H_2),\quad
 B\in B_0+\mathcal S_2(H_2,H_3),\quad C\in H_3,          \tag{T.7}
\]
where the initialized actions have their actual Hilbert adjoints and
norms at most ten. The first root is \(N(0,I_d/d)\), and the population
readout initially vanishes. These are the canonical limits of (T.3),
not freely chosen bounded operators. The raw increment norm is
\(d\|\Delta w\|_2^2+\|\Delta A\|_{\rm HS}^2+
\|\Delta B\|_{\rm HS}^2+\|\Delta C\|_2^2\).
For vectors in the appropriate spaces,
\((u\otimes v)q=u\langle v,q\rangle\). Replace matrices, normalized
sums, and transposes in (T.4)--(T.6) by these actions, expectations, and
adjoints. This specifies the population equation without a trajectory
oracle or externally supplied time-dependent coefficients.

**Theorem T.1.** There is an explicit nondecreasing function
\(e_\delta\in(0,1/4]\), given in the quantitative chapter below,
with \(e_\delta\to0\) as \(\delta\downarrow0\), such that every fixed
\(0<e\le e_\delta\) gives the following conclusions for every dataset
(T.2).

1. The population equation has a global autonomous strong \(C^1\) solution
   in (T.7). It is the raw Hilbert gradient flow of \(L\). It is unique
   among strong solutions with bounded primal quantities on compact
   intervals, including nonsymmetric competitors, and has unique
   continuation from each reached state in that class.
2. On every fixed finite physical interval, GF and raw GD converge jointly
   in probability along the full width sequence to that same solution.
   Predictions, loss, and all entries of the four true kernel blocks
   converge uniformly in time. The blocks are
   \[
   K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_1,\quad
   K^2_{ij}=\langle b_i^2,b_j^2\rangle_2\langle h_i^1,h_j^1\rangle_1,
   \]
   \[
   K^3_{ij}=\langle b_i^3,b_j^3\rangle_3\langle h_i^2,h_j^2\rangle_2,
   \qquad K^4_{ij}=\langle h_i^3,h_j^3\rangle_3.         \tag{T.8}
   \]
   Each layer's joint two-sample preactivation/feature path law converges
   in \(\mathcal W_2(C([0,T];\mathbb R^4))\), using the supremum norm.
   The same-layer joint field/velocity law converges in \(\mathcal W_2\)
   uniformly in time and jointly at every fixed finite set of times.
   Second moments and integrated squared speeds converge. Every fixed
   finite tuple of generated probes, as defined in Appendix C, M.3,
   has its joint same-layer \(\mathcal W_2\) limit, with both orientations
   of initialized and learned actions. There is no cross-layer neuron
   pairing or assertion of cross-width operator-norm convergence.
3. Uniformly in time, sample, and hidden layer,
   \[
   \inf_{t\ge0}\min_{i,\ell}\inf_{\alpha,\beta\in\mathbb R}
   E_\ell[\psi_e(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
   \ge \frac{e^2\delta^3}{196608(1+\delta/8)^3}>0.       \tag{T.9}
   \]
   Every hidden parameter block and every sample's preactivation and
   feature in every hidden layer has a nonzero initial right second
   derivative. With \(p=y/2\),
   \[
   \kappa(t)=p^T\Big(\sum_{\ell=1}^4K^\ell(t)\Big)p
   =\kappa(0)+8t^2\|V\|_{\rm hidden}^2+o(t^2),
   \qquad \|V\|_{\rm hidden}>0,                         \tag{T.10}
   \]
   where Appendix B defines \(V\). The readout has nonzero initial
   velocity. Moreover \(L(t)\le\exp(-\delta t/32)\).

The coefficient is fixed before dimension, input angle, labels, width,
caps, meshes, and physical horizon. Limits are asserted for each fixed
dataset and finite horizon, not as a supremum over datasets or over the
whole half-line. Nonzero hidden initial acceleration and changing kernel
exclude a frozen-feature population trajectory. The positive coefficient
does not tend to zero with width, and (T.9) excludes affine hidden laws.
No assertion of perpetual nonzero velocity is made.

## 2. Proof architecture and the affine reference

For the proof allow \(\phi_{a,e}(z)=az+e\arctan z\), with
\(1/2\le a\le1\), and compare it to \(az\) at the **same** gain.
Numerical upper estimates may set the gain to one. At the end set
\(a=1-e\). Appendix A proves the following ingredients in detail.

Oddness gives the exact finite loss identity under label folding
\((x_i,y_i)\mapsto(y_i x_i,1)\). The reflection exchanging the two
folded inputs preserves initialization, metric, and both vector fields.
At every fixed cap and finite Euler program the limiting contractions
are deterministic, so the population predictions obey
\[
 f_i=y_i g,\qquad g=\tfrac12\sum_i y_i f_i,\qquad
 L=(1-g)^2.                                            \tag{T.11}
\]
This is an identity for the constructed population paths, not for each
finite random realization. It is obtained before invoking uncut uniqueness.
Feature time means \(\Theta'=\nabla g\), where a prime denotes that time.
The physical equation is \(\dot\Theta=2(1-g)\nabla g\).

Write \(y_1=\sigma,y_2=\sigma\tau\), and set
\(u=(x_1+\tau x_2)/2\), \(v=(x_1-\tau x_2)/2\).
The normalized active and inactive variances
\((1+\tau\rho)/2\) and \((1-\tau\rho)/2\) are both at least
\(\delta/2\). On the affine feature-gradient path the inactive
Gaussian contribution is unchanged at all three layers. This is proved
in Appendix A by conditioning on the active finite training transcript:
an independent inactive root \(Q_0\) obeys
\[
 E[\|\Delta A Q_0\|_n^2\mid\text{active data}]
       =\frac{v_v}{n}\|\Delta A\|_F^2\longrightarrow0,   \tag{T.12}
\]
and the same holds for \(BA-B_0A_0\). The Frobenius norm is bounded
by exact rank-one unrolling. This is stronger than a bare bound on a
population operator.

With \(H=\frac12\sum_i y_i h_i^3\) and its hidden directional
linearization \(J\), the affine equations give
\[
 C'=H,\qquad C''=JJ^*C,\qquad
 g'=\|\Theta'\|_{\rm raw}^2\ge\|H(0)\|^2
       =a^6(1+\tau\rho)/2\ge\delta/128.                \tag{T.13}
\]
The lower bound follows from convexity of \(\|C\|\), as derived in
Appendix A. Before the first hit \(S\) of \(g=3/2\), the gradient
energy is at most \(3/2\). Strong endpoint continuation for the locally
Lipschitz affine polynomial field proves that this hit occurs, and gives
\[
 S\le S_\delta=192/\delta,\quad
 \|\Theta(s)-\Theta(0)\|_{\rm raw}\le12\sqrt{2/\delta},
 \quad U=11+12\sqrt{2/\delta}.                          \tag{T.14}
\]
All four primal sizes, using projected first-layer norms, are at most
\(U\). Each affine reference stops at its own hit \(S\); it is not
asserted to remain bounded until the larger number \(S_\delta\).
Every affine sample marginal is a centered Gaussian of standard deviation
at least \(\sqrt{\delta/32}\). Gaussianity follows from linearity of
the fixed source expressions and strong affine Euler convergence.

The quantitative chapter proves a uniform explicit regression margin for
these marginals, a complete response cutoff, and the coefficient choice.
We verify below that these are sufficient for all the claimed limits.

## 3. The sharper affine estimates entering the explicit cutoff

This section proves the initial constants used in the quantitative chapter;
it is not an appeal to an unspecified affine-response theorem. Let a fixed
positive Euler mesh have total feature time at most \(S_0\), controls
\(c_i=y_i/2\), and affine finite primal bound \(P\ge1\). Put
\(b_r=2P\), \(F=\exp(36P^2S_0)\).

Use the sum of the maximum first-projection discrepancy, the two operator
discrepancies, and readout discrepancy. On the primal ball \(b_r\),
the affine field is \(9b_r^2\)-Lipschitz and bounded by \(10b_r^3\).
The same bounds hold in the raw increment sum norm when the first
component is \(\sqrt d\|\Delta w\|_2\) and the learned matrix
components use Hilbert--Schmidt norm. To verify them, let the four
component discrepancies be \(u,v,w,t\). Conservative forward differences
are \(u,\ b_ru+2b_rv,\ b_r^2u+2b_r^2v+3b_r^2w\);
backward differences are \(t,\ b_r(w+t),\ b_r^2(v+w+t)\).
Inserting these into the four rank-one updates bounds their Lipschitz
constants by \(b_r^2,2b_r^2,3b_r^2,3b_r^2\). Removing the affine
offset and multiplying factors by \(a\le1\) only reduces these upper
bounds. Rank-one norms are products of normalized vector norms in either
the operator or Hilbert--Schmidt estimate.

Add errors of norm at most \(v_k\) immediately after a chosen class of
matrix answers. The same-state field error has the following bounds:

| Answer perturbed | Changed update components | Multiplier of \(v_k\) |
| --- | --- | --- |
| Middle forward \(Z^2\) | \(B,C\) | \(2b_r\) |
| Top forward \(Z^3\) | \(C\) | \(1\) |
| Middle reverse \(q^2\) | \(w,A\) | \(3b_r\) |
| Bottom reverse \(q^1\) | \(w\) | \(1\) |

For example a middle forward error changes \(B'\) and \(C'\) by
at most \(b_rv_k\) each. A middle reverse error changes the bottom
update by at most \(b_rv_k\) and \(A'\) by at most \(2b_rv_k\).
The other two rows are direct readout or bottom updates. Gains at most
one preserve every bound. Recompute all subsequent answers and updates.
If the same independent normalized Gaussian probe is inserted with
amplitude \(v\alpha_{ki}\), \(|\alpha_{ki}|\le1\), discrete Gronwall
gives state error at most \(\kappa S_0F|v|\|G_n\|_n\), or
\(\kappa h_jF|v|\|G_n\|_n\) for insertions at one time \(j\).
For small fixed \(v\) a stopped induction keeps the perturbed prefix
strictly inside \(b_r\). No perturbed primal hypothesis is assumed.

Apply Appendix C, F.1, at fixed nonzero \(v\). The frozen affine scalar
program is affine in its Gaussian sources and in the new root \(G\).
The only explicit occurrences of \(G\) are the inserted additions.
Thus for an output \(V\),
\[
 E[GV^v]=v\sum_{k,i}\alpha_{ki}
          \partial_{\mathrm{source}_{ki}}V^v.            \tag{T.15}
\]
All coefficients on the right are deterministic. They are continuous
at \(v=0\): finite affine coefficient and covariance recursions are
continuous and require no inverse covariance. The unperturbed finite
pairing with the independent probe tends to zero. Pair the finite
difference with that probe, take width to infinity at fixed \(v\), then
take \(v\to0\). Cauchy--Schwarz and the preceding stability estimate
bound the absolute derivative row by the output Lipschitz constant times
\(\kappa S_0F\). Choose the deterministic signs of its entries to
obtain the absolute row sum. Restricting the insertions to one time
replaces \(S_0\) by \(h_j\). This also tests separately named singular
source directions; it is not differentiation along a singular support.

For outputs \(H^1,H^2,\delta^2,\delta^3\) in their respective
reverse, reverse, forward, forward source groups, the resulting row
bounds are
\[
 S_0F,\qquad24P^2S_0F,\qquad8P^2S_0F,\qquad S_0F.     \tag{T.16}
\]
Indeed the corresponding output Lipschitz bounds are
\(1,2b_r,b_r,1\), and the forcing multipliers are
\(1,3b_r,2b_r,1\). None of these outputs has an extra direct current
source in the indicated group. For one forward response entry, its
learned moment has weight \(|c_i|=1/2\), and is at most
\(2P^2h_j\) in layer two or \((9/2)P^4h_j\) in layer three.
For a full backward scalar row, learned moments are bounded by
\(S_0P^4\) or \(S_0P^2\). Conversion of a scalar forward entry into
a two-column block costs two, and conversion of maximum scalar backward
row sums into the sum of block row norms costs at most two. Consequently
the actual affine source coefficients satisfy the Appendix C, R.8
convention with
\[
 A_0=2(24P^2F+9P^4/2),\qquad
 M_0=2S_0(8P^2F+P^4).                                  \tag{T.17}
\]
These are the sharper starting constants in (Q.15).

It remains to supply the finite-array premise. We use the norm of the
**total** learned increment, retaining the cross terms between updates.
Let \(R_\delta=12\sqrt{2/\delta}=U-11\). The affine reference obeys
\(\sup_{s\le S}\|\Theta(s)-\Theta(0)\|_{\rm raw}\le R_\delta\)
by (T.14). On the primal ball \(2U\), the affine field is
\(36U^2\)-Lipschitz in the raw increment sum norm and has the local
Euler defect bound \(45(2U)^5h_j^2\). A stopped Euler comparison,
with the same initialized actions, gives
\[
 \max_k\|\Theta^{\rm E}_k-\Theta(s_k)\|_{\rm sum,raw}\le1
                                                        \tag{T.18a}
\]
on every sufficiently fine positive mesh of its own interval \([0,S]\).
The mesh threshold depends only on \(U,S_\delta\), not on the input
dimension, angle, labels, or gain \(a\in[1/2,1]\): the sum of local
defects is bounded by a constant times \(S_\delta\max_jh_j\),
and Gronwall multiplies it by at most \(\exp(36U^2S_\delta)\).
For example,
\[
 \max_jh_j\le
 \frac1{90(2U)^5S_\delta\exp(36U^2S_\delta)}
\]
makes the error at most \(1/2\). Then all Euler nodes remain strictly
inside \(2U\), closing the stopped argument.
In particular every population learned matrix increment has
Hilbert--Schmidt norm at most \(R_\delta+1\).

At a fixed such mesh, write its finite layer-two learned increment as
\[
 \Delta W^2_k=\frac1n\sum_{j<k}\sum_{i=1}^2
       h_jc_i\delta^2_{i,j}(H^1_{i,j})^T.
\]
Its ordinary Frobenius square is exactly
\[
 \|\Delta W^2_k\|_F^2
 =\sum_{j,l<k}\sum_{i,m=1}^2 h_jh_lc_ic_m
  \langle\delta^2_{i,j},\delta^2_{m,l}\rangle_n
  \langle H^1_{i,j},H^1_{m,l}\rangle_n.                 \tag{T.18b}
\]
There are finitely many contractions. The fixed-program theorem F.1
and its causal-contraction extension identify their joint limit.
The Hilbert--Schmidt rank-one identity
\(\langle u\otimes v,\tilde u\otimes\tilde v\rangle_{\rm HS}
=\langle u,\tilde u\rangle\langle v,\tilde v\rangle\)
therefore makes the limit of (T.18b) exactly
\(\|A^{\rm E}_k-A_0\|_{\rm HS}^2\), as also proved in F.8.
The identical calculation with \(\delta^3,H^2\) treats layer three.
Consequently, simultaneously at the finitely many nodes of this mesh,
\[
 \|W^2_k\|_{\rm op},\ \|W^3_k\|_{\rm op}
 \le10+(R_\delta+1)+o_{\Pr}(1)=U+o_{\Pr}(1).          \tag{T.18c}
\]
Here only the initialized operator norm bound and
\(\|\Delta W\|_{\rm op}\le\|\Delta W\|_F\) are used.
The population first projections and readout have norms at most
\(U+1\) by (T.18a); their finite norms converge by F.1. Thus the
strict finite-array primal bound needed in Part R holds with
\[
                         P=11+2U.                      \tag{T.18}
\]
If the small finite random readout is retained in this affine auxiliary
program, its normalized norm tends to zero, and fixed-mesh affine
stability gives the same limits.

This proves one numerical bound for every sufficiently fine fixed mesh.
The probability limit is taken separately on each such mesh; it is not
an assertion of one width event uniform over infinitely many meshes or
of a width-dependent growing program. No nonlinear source response is
used to prove this affine premise. Nor is trained matrix operator-norm
convergence across widths asserted: only total learned Frobenius norms
are identified through the finite contraction identity (T.18b).

## 4. Source control and removal of the auxiliary caps

For a smooth odd clip \(\tau_R\), with \(|\tau_R'|\le1\), identity
on \([-R,R]\), and \(|\tau_R(q)|\le\min(|q|,2R)\), use the auxiliary
backward gate
\[
 D_R(z,q)=aq+e(1+z^2)^{-1}\tau_R(q).                    \tag{T.19}
\]
Forward activations are not clipped. At fixed cap the coordinate maps
have bounded first derivatives:
\(|\phi'|,|D_q|\le2\), \(|D_z|\le2eR\).
Hence all fixed Gaussian calculations satisfy F.1's hypotheses.

The controlled source equations (R.11)--(R.17) apply with two sample
slots, the same formal-source convention, and controls \(c_i=y_i/2\).
They follow from rank unrolling and the exact Gaussian response in Part F.
Full second moments, both matrix orientations, and the current transpose
returns are retained. Removing the activation offset removes no derivative
term or memory. The actual affine reference has gain \(a\); in every
upper estimate its factors \(a,a^2\) can be bounded by one. With the
verified constants (T.17), (T.18), the quantitative chapter reproduces the
entire remaining chronological constant chain, including the restriction
on \(e\). It proves cap- and mesh-independent bounds
\[
 \|C\|_p+\max_i\|q_i^2\|_p+\max_i\|q_i^1\|_p
                         \le K\sqrt p\quad(p\ge2),     \tag{T.20}
\]
on the full feature interval. All forward fields and deltas have the
same type of bound. The finite constant \(K\) depends only on the
specified numerical arguments, not on the cap, mesh, angle, or labels.

Here is the primal comparison independently of those response bounds.
On the ball with each primal size at most \(b=4U\), the four
same-state nonlinear-minus-affine update bounds are at most
\(7eb^3,14eb^3,11eb^3,6eb^3\). They follow by forward propagation
using \(|\arctan z|\le\pi/2\), then backward propagation using
\(|D_R-aq|\le e|q|\), and the rank-one difference inequality.
Their sum is at most \(40eb^3\). The affine field is
\(9b^2\)-Lipschitz, so stopped Gronwall yields
\[
 \sup_{s\le S}\|\Theta_{a,e,R}(s)-\Theta_{a,0}(s)\|_{\rm sum,raw}
 \le Qe,\qquad Q=40b^3S_\delta e^{9b^2S_\delta}.        \tag{T.21}
\]
The cutoff ensures \(Qe\le b/4\); the affine state lies in the
ball \(b/4\), leaving strict slack before the boundary \(b\).
At fixed cap the field is locally Lipschitz there, so these paths exist
through \(S\). For the raw sum norm at initialization, only differences
of first weight fields occur; the dimension-dependent full initial norm
is never inserted into the constants.

For raw discrepancy \(D\) in (T.21), product expansion gives
\[
 \|z_e^1-z_0^1\|_2\le D,\quad
 \|z_e^2-z_0^2\|_2\le5bD+(\pi/2)be,
 \quad \|z_e^3-z_0^3\|_2\le12b^2D+\pi b^2e.           \tag{T.22}
\]
For example use \(\|h_e^1\|\le4b\) in
\((A_e-A_0)h_e^1+A_0(h_e^1-h_0^1)\), and then
\(\|h_e^2\|\le7b^2\) in the next layer. Thus every preactivation
discrepancy is at most \(Je\), with \(J=12b^2Q+\pi b^2\).
The prediction discrepancy is at most \(Oe\), where
\(O=10b^3Q+b(J+\pi/2)\). The chosen coefficient gives
\[
                      g_{a,e,R}(S)\ge5/4.              \tag{T.23}
\]

To remove caps, compare a path with cap \(R'\ge R\), allowing
\(R'=\infty\), to the cap-\(R\) reference. Split its gate difference
as
\[
\begin{split}
 D_{R'}(z_A,q_A)-D_R(z_B,q_B)
 ={}&a(q_A-q_B)
 +e g(z_A)[\tau_{R'}(q_A)-\tau_{R'}(q_B)]\\
 &+e[g(z_A)-g(z_B)]\tau_R(q_B)
 +e g(z_A)[\tau_{R'}(q_B)-\tau_R(q_B)],
 \qquad g(z)=(1+z^2)^{-1}.
\end{split}                                             \tag{T.24}
\]
Its norm is bounded by
\(2\|q_A-q_B\|_2+4eR\|z_A-z_B\|_2+
2e\||q_B|1_{|q_B|>R}\|_2\).
Forward propagation, then successive backward substitution, give
\[
 \|V_{R'}(\Theta_A)-V_R(\Theta_B)\|_{\rm sum,raw}
 \le C_b(1+eR)\|\Theta_A-\Theta_B\|_{\rm sum,raw}
       +C_be\sum_Q\||Q_B|1_{|Q_B|>R}\|_2.              \tag{T.25}
\]
Only a forward-state discrepancy acquires the factor \(R\); an incoming
backward discrepancy is multiplied by bounded gates and actions.
The loss is therefore linear in \(R\), not cubic. Equation (T.20)
gives Gaussian tails in the last term by the exponential-moment argument
(R.42)--(R.43). Gronwall bounds cap differences by
\(C\exp(C(1+eR)S_\delta-cR^2)\to0\). The same inequality controls
their raw directions. They are uniformly Cauchy on \([0,S]\), and
their limit is a strong \(C^1\) uncut solution. The vector field is
identified by taking \(R'=\infty\) in the same reference-only estimate.
The chain rules and scalar Fréchet gradient assertion are those proved
in F.5--F.6. No unrestricted Fréchet differentiability of a nonlinear
Nemytskii map on all of \(L^2\) is asserted.

The endpoint bound (T.23) and uniform preactivation comparison pass to
the limit. Equations (Q.3)--(Q.7) prove the uniform feature-interval
nonaffinity bound (T.9).

## 5. Global physical time, uniqueness, and the finite algorithms

For the nonlinear initialized pair, strict monotonicity and oddness give
\(q_\ell\pm c_\ell\ge a^2(q_{\ell-1}\pm c_{\ell-1})\), where
\(q_\ell,c_\ell\) are diagonal and off-diagonal feature moments.
Consequently \(\|H(0)\|^2\ge\delta/128\). On the uncut feature
path the strong trajectory chain rule yields \(C''=JJ^*C\), so the
convexity argument of Appendix A gives
\(g'=\|\nabla g\|^2\ge\delta/128\). This argument is used after
constructing the path, not to presume its existence.

Let \(s_*<S\) be its first hit of \(g=1\). For \(s<s_*\), define
\[
                      t(s)=\int_0^s\frac{du}{2(1-g(u))}.          \tag{T.26}
\]
The compact feature path has bounded continuous derivative, say
\(|g'|\le M\). Thus \(1-g(s)\le M(s_*-s)\) and (T.26) diverges.
Its inverse produces the physical trajectory for every \(t\ge0\),
inside the same compact feature interval. Equation (T.11) shows that
its field is exactly (T.6). Also
\(\partial_t(1-g)=-2g'_s(1-g)\), proving
\(L(t)\le e^{-\delta t/32}\). The uniform nonaffinity bound survives
the infimum over all physical times.

Each cap path has a first hit of one by (T.23). Before that hit it is
below one and has bounded derivative, so the same clock diverges and
constructs a global physical cap reference. Its feature field need not
be a gradient or have monotone prediction. The argument requires neither.
All caps inherit uniform primal bounds and incoming-field tails from
their closed feature intervals.

On any fixed physical interval, (T.25) extends to the physical fields:
retain both actual residuals, use their boundedness and the locally
Lipschitz prediction contractions, and then the same backward
substitution. Constants may depend on the physical horizon and primal
bound. Comparing any bounded-primal uncut strong competitor to the cap
reference requires tails only from that reference; its error vanishes
like \(C_T\exp(C_TR-cR^2)\). This proves uniqueness even for a
nonsymmetric competitor. At a reached state the already vanishing cap
initial discrepancy is multiplied by at most another \(e^{C_TR}\),
which the Gaussian tail still defeats. This proves unique continuation
from that state without claiming existence from arbitrary ambient states.

All hypotheses of Appendix C, Part V, are now available with two samples:
the canonical fixed Gaussian programs, locally Lipschitz cap fields,
global bounded cap references, common incoming-field tails, and the
reference-only comparison. Its finite-algorithm proof is unchanged in
content for the present maps. For clarity, the actual steps and changed
bounds are recorded next.

At fixed cap and fixed auxiliary mesh, F.1 identifies the finite program
with its two empirical residuals and learned contractions. Exact unrolling
bounds current finite operators from initial norms and finite sums of
update-factor RMS products. A primal ball with slack contains these nodes
on events of probability tending to one. The cap field's Lipschitz and
bounded-field constants on that ball do not depend on width. Integrating
over a step gives the local Euler defect \(LMh^2/2\); stopped Gronwall
removes the auxiliary mesh, after taking width at each fixed mesh.
This gives fixed-cap finite GF and the cap observations.

Compare actual finite GF to its same-width cap reference with (T.25).
Take width first at fixed cap, then the cap to infinity. Convergence of
reference tail norms follows from the already proved fixed-cap joint
\(\mathcal W_2\) laws. The strict stopping margin precludes exit.
For simultaneous raw GD, the interpolant's direction is the uncut field
at its preceding node. The corresponding comparison has the extra
reference local defect \(C_{R,T}\eta_n\to0\). This proves the full
sequence \(\eta_n=n^{-2}\), without applying a Gaussian theorem to
a growing transcript. The actual finite readout has
\(\|C_n(0)\|_n=O_{\Pr}(n^{-1})\). The fixed-program comparison in
F.6 propagates this vanishing root to the zero population readout; actual
finite trajectories and their same-width comparisons retain (T.3).

The full kernel and velocity observations require the additional proofs
in Part V; bounded action norms alone would not suffice. In the present
maps, \(|\phi(z)|\le|z|+\pi/2\), \(|\phi'|\le2\),
\(|\phi''|\le e\), \(|D|\le2|q|\), \(|D_q|\le2\), and
\(|D_z|\le2eR\). These satisfy each of its coordinate and gate
inequalities at numerical gain one. Source derivatives freeze the actual
controls and their covariance parameters. Reparametrizing the feature
reference into physical time leaves their total controlled clock bounded
by \(S_\delta\), so the supplied incoming moments remain available.

The true backward fields at capped states are appended as observations;
their proof uses nested smooth product truncations and retains current
returns, as in V.8 and V.I. Likewise the velocity queries are the actual
forward linearizations, first made bounded-derivative instructions by
nested truncation. The derivative-valid passage for these queries is
proved in V.3--V.5 and V.I. All unbounded factors have the moment
envelopes established there from the controlled source bounds, not an
assumed \(L^p\) bound on an arbitrary operator. These arguments do not
use an activation offset or a positive lower bound on gain beyond those
already supplied. Changing three sample indices to two reduces the
finite sums; the same constants dominate.

For removal of the velocity truncations, the deterministic comparison
for actual raw states and directions has the form
\[
 \|\mathcal V-\overline{\mathcal V}\|_{\rm sum,2}
 \le C\left[d_1+(1+M)d_0+
       \sum_{i,\ell}\|(|\bar P_i^\ell|-M)_+\|_2\right],          \tag{T.27}
\]
where \(d_0,d_1\) are state/direction errors and \(\bar P\) is
the reference preactivation velocity. This follows by expanding each
forward product and truncating only the reference factor multiplied by
a gate difference; each such term has one factor \(M\).
The uncut reference velocity has a compact continuous \(L^2\) time
image by the trajectory chain rule. A finite \(L^2\) net and the
1-Lipschitz positive-part tail map give uniformly vanishing tails.
For population velocities, take cap to infinity at fixed \(M\), then
\(M\to\infty\). For finite velocities, first take width at fixed
cap and \(M\), then cap at fixed \(M\), then \(M\to\infty\).
This is the order used in Part V and proves the stated uniform-time and
finite-joint-time velocity laws without controlling the growth of
cap-dependent fourth moments.

Products of the converging true \(L^2\) observations give all entries
of (T.8). Fixed generated probes are transferred by the same bounded
coordinate maps, contractions, and actions in both orientations.
Finally, for an absolutely continuous coordinate path and fixed-grid
linear interpolation \(I_h\),
\[
 \|x-I_hx\|_\infty^2\le4h\int_0^T|x'(t)|^2dt.          \tag{T.28}
\]
The proved speed bounds give finite path second moments and uniform
average interpolation error. Fixed-grid joint \(\mathcal W_2\) limits,
followed by \(h\downarrow0\), prove the path laws. Uniform-time velocity
convergence also controls squared speeds and their integrals. This
establishes every finite-algorithm assertion of Theorem T.1.

## 6. Initial feature learning and the meaning of the cutoff

Appendix B proves all initial-motion claims for \(az+e\arctan z\)
with \(a\ge1/2\), \(e>0\), and (T.2). The forward Gaussian pairs
are nondegenerate. With \(H=\sum_i(y_i/2)h_i^3\), the top beta
Gram of \(H\phi'(Z_i^3)\) is positive definite: a zero combination
would imply an everywhere identity whose coordinate derivative forces
each coefficient to vanish since \(\phi''\not\equiv0\). Actual
transpose innovations have the full second moments of their reverse
inputs. Conditional variances give strictly positive lower beta Grams
and nonzero hidden parameter blocks. Adjunction and sample reflection
then show that every individual upper-layer sample direction is nonzero.
The bottom sample claim follows directly from conditional variance and
\(\Gamma_{ii}=1\). The source identities used here have their
derivative-valid finite-transcript proof in Appendix C, V.I.

Hidden feature-time velocity divided by \(s\) tends to \(V\), so
the actual initial second derivative is \(V\). The corresponding
field limits follow by bounded-multiplier chain rules. In physical time
\(s'(0)=2\), giving hidden acceleration \(4V\) and (T.10).
For the second-order feature-energy expansion one may use F.41's weighted
scalar remainder, or its identical application in N.6--N.9; it does not
require ambient \(L^2\)-Fréchet differentiability of the feature map.

The quantitative chapter proves that the chosen \(e_\delta\) is
nondecreasing and tends to zero. This is a sufficient choice. It is not
the largest possible coefficient, and its deterioration is not a proved
necessity. To make that distinction precise, let
\[
 E_{\max}(\delta)=\sup\{b\le1/4:
 \text{the qualitative conclusions of T.1 hold for every }0<e\le b
 \text{ and every dataset satisfying (T.2)}\}.          \tag{T.29}
\]
Here qualitative means existence, uniqueness, convergence, some positive all-time nonaffinity margin, and initial motion; the particular numerical rates in (T.9) are not imposed in this definition. The set of datasets shrinks as \(\delta\) increases, so
\(E_{\max}\) is nondecreasing. Theorem T.1 gives
\(E_{\max}(\delta)\ge e_\delta>0\). Neither the theorem nor the
incompatible exact endpoints proves that \(E_{\max}(\delta)\to0\).
Pointwise validity at every strictly nonendpoint angle would be compatible
with failure exactly at an endpoint.

In particular, the proposed polynomial statement means that a universal
\(c>0\) permits **every** \(0<e\le c\delta^2\), for all small
\(\delta\). The much smaller sufficient function proved below does
not establish that statement, even though it is itself \(O(\delta^2)\).
No optimal training-cutoff scaling is claimed.



# Quantitative construction for Theorem T.1

The symbols and equations in this chapter have prefix Q. The sharper affine inputs are proved in Section 3 of the main text; the remaining response equations and estimates are reproduced in Appendix C, Part R.

## 2. An explicit Gaussian margin and a sharper transfer inequality

Write

\[
\mathcal R(Z)=\inf_{\alpha,\beta}
E[\arctan Z-\alpha-\beta Z]^2.
\]

For \(G\sim N(0,1)\), the Hermite polynomial \(H_3(G)=G^3-3G\)
is orthogonal to \(1,G\) and has squared norm six. Thus, by
Cauchy--Schwarz applied to the affine-regression residual,

\[
\mathcal R(\nu G)\ge\frac16
\bigl(E[H_3(G)\arctan(\nu G)]\bigr)^2.                 \tag{Q.1}
\]

Gaussian integration by parts gives

\[
E[H_3(G)\arctan(\nu G)]
=\nu E\frac{G^2-1}{1+\nu^2G^2}.
\]

Use \((1+\nu^2G^2)^{-1}=\int_0^\infty e^{-t}e^{-t\nu^2G^2}\,dt\).
Fubini is justified by the integrable bound \(|G^2-1|\), and the
Gaussian integrals give

\[
E[H_3(G)\arctan(\nu G)]
=-2\nu^3\int_0^\infty
      \frac{t e^{-t}}{(1+2\nu^2t)^{3/2}}\,dt.          \tag{Q.2}
\]

The measure \(t e^{-t}dt\) is a probability measure of mean two.
The integrand factor \((1+2\nu^2t)^{-3/2}\) is convex in \(t\),
so Jensen's inequality yields

\[
\mathcal R(\nu G)\ge
\frac{2\nu^6}{3(1+4\nu^2)^3}.                          \tag{Q.3}
\]

The right side is increasing in \(\nu>0\), since
\(\nu^2/(1+4\nu^2)\) is increasing. With \(m^2=\delta/32\),
one may therefore replace the unspecified Gaussian minimum by

\[
\bar\eta_\delta
=\frac{\delta^3}{49152(1+\delta/8)^3}>0.                \tag{Q.4}
\]

No upper-variance bound is needed for this particular margin.

There is also a uniform regression stability estimate with no inverse
variance loss. Let \(Z'\) be an independent copy of \(Z\). Since
arctangent is increasing and 1-Lipschitz,

\[
0\le\operatorname{Cov}(Z,\arctan Z)
=\tfrac12 E[(Z-Z')(\arctan Z-\arctan Z')]
\le\operatorname{Var}(Z).
\]

For nonconstant \(Z\), its optimal regression slope therefore belongs
to \([0,1]\). For constant \(Z\), choose slope zero. Use the optimal
intercept and slope for \(Z\) as a competitor for \(Z_0\). The
triangle inequality and the Lipschitz bound give

\[
\sqrt{\mathcal R(Z_0)}
\le\sqrt{\mathcal R(Z)}+2\|Z-Z_0\|_2.
\]

Interchanging the variables proves

\[
|\sqrt{\mathcal R(Z)}-\sqrt{\mathcal R(Z_0)}|
\le2\|Z-Z_0\|_2.                                      \tag{Q.5}
\]

Thus the sufficient transfer restriction is simply

\[
\|Z-Z_0\|_2\le\sqrt{\bar\eta_\delta}/4
\quad\Longrightarrow\quad
\mathcal R(Z)\ge\bar\eta_\delta/4.                    \tag{Q.6}
\]

Absorbing \((1-e)Z\) into the affine approximant gives the exact
activation-regression identity

\[
\inf_{\alpha,\beta}E[\psi_e(Z)-\alpha-\beta Z]^2
=e^2\mathcal R(Z).                                    \tag{Q.7}
\]

This improves the variance-dependent transfer coefficient in Appendix A from order
\(\delta^2/J\) to order \(\delta^{3/2}/J\), although the source
cutoff below is much more restrictive overall.

## 3. Literal explicit response chain available without any new estimate

Here is the safest direct specialization of Appendix C's complete (R.90) chain. It is included literally so that no
undefined instruction to enlarge a constant is part of the cutoff.
Fix \(P\ge1,S\ge1\), and define

\[
b_r=2P,\quad q=100b_r^3,\quad F_0=e^{qS},\quad T_0=qSF_0,
\]
\[
A_0=3q^2(F_0+1),\quad M_0=3Sq^2(F_0+1),\quad
\sigma=q,\quad D_0=q(1+T_0),\quad m_0=2qD_0,
\]
\[
A=A_0+1,\qquad M=M_0+1,\qquad k_0=3+6\sigma,
\]
\[
K_1=(k_0+12\sigma S)e^{2MS},\quad
K_2=(k_0+12A\sigma S)e^{2AMS},\quad
K_C=k_0S e^{2AS^2},
\]
\[
K_{q1}=6\sigma+MK_1,\quad K_{q2}=6\sigma+MK_2,\quad
K_q=1+K_C+K_{q1}+K_{q2},\quad
L_q=\sqrt{8\exp(1)}K_q,
\]
\[
H=40(1+A)(1+M)(1+S),\quad
X_0=2(1+2K_q)\exp(HS+H^2S^2L_q^2).                    \tag{Q.8}
\]

For any specified positive \(X\), continue the chain by

\[
R_0=200H^{11}e^{HS}[1+(S+1)X]+m_0(1+S),
\]
\[
K_F=e^{MS},\quad K_V=Ae^{AMS},\quad K_U=e^{AMS},\quad
K_T=S e^{AS^2},
\]
\[
D_2=R_0+K_F e^{M_0S},
\]
\[
C_V=[(1+MSK_V)D_2+A_0K_V]e^{A_0M_0S},\quad D_3=R_0+C_V,
\]
\[
C_T=S^2K_TD_3e^{A_0S^2},\quad E_3=R_0+C_T,
\]
\[
C_U=[MSK_UD_2+A_0K_U]e^{A_0M_0S},
\]
\[
E_2=R_0+K_UE_3+M_0C_U,\qquad
K_*=2\max\{1,D_2,D_3,E_2,E_3\}.                        \tag{Q.9}
\]

Taking \(X=X_0\), a literal valid source cutoff is

\[
E_{\rm lit}(P,S)=
\min\left\{1,\frac{P}{2T_0},
                 \frac1{2K_*\exp(K_*S)}\right\}.       \tag{Q.10}
\]

This is exactly \(\epsilon_*(1,P,S)\) in the manuscript, with its
whole constant chain displayed. The factor three in \(A_0,M_0\) and
the Gaussian maximum constant six safely dominate the two-sample
problem.

### Why the zero-offset/gain change is valid

The actual affine comparison is still with \(az\), at its actual
\(a\in[1/2,1]\). Setting \(a=1\) in the numerical chain is an
upper-bound operation on estimates, not a change in the comparator.
The source equations and derivative recursions contain the same formal
slots and array products. The removed offset has derivative zero and
only decreases the constant term in the growth estimate. Every actual
factor \(a\) or \(a^2\) in a norm estimate is at most one; both
\(|\phi'|\) and \(|D_q|\) are at most two, while
\(|D_z|\le e|q|\) in the response envelopes.

More concretely, on the ball \(b_r\ge2\), the tables (R.20)–(R.22)
at numerical gain one dominate every query and affine derivative of the
zero-offset network. The same-state perturbations obey
\(2e,3b_re,4b_r^2e\) in the forward layers and
\(b_re,b_r^2e,3b_r^2e,3b_r^3e,7b_r^3e\) in the listed backward
queries; these use only actual gain at most one. For example
\(2(1+ab_r)e\le3b_re\) because \(a\le1,b_r\ge2\).
The first-layer root maximum over two samples has the bound used for
three. Control norms remain at most one. Every estimate (R.38)–(R.89)
then holds with the gain-one numerical constants above.

There is no lower-gain premise in those upper estimates. Neither a
covariance inverse nor a positive offset is used. The low-gain bound is
needed separately for the affine variance/coercivity argument, proved
in Appendix A.

## 4. A fully explicit improved source cutoff

Two verified changes sharpen the literal chain. Neither uses an
unspecified replacement constant.

### 4.1 Retain the small coefficient in the exponential envelope

The exact envelope in (R.50) is

\[
\mathcal E_k=\exp\left(Hs_k+He\sum_{r<k}h_rQ_r\right).
\]

The derivation of (R.56), before dropping \(e\le1\), gives

\[
E\mathcal E_k^p\le
2\exp\left(pHS+\frac{p^2H^2e^2S^2L_q^2}{4}\right).
                                                               \tag{Q.11}
\]

Indeed the convexity bound (R.55) followed by
\(Ee^{uQ_r}\le2e^{u^2L_q^2/4}\) uses
\(u=pHeS\). This requires no time independence and no random
supremum. Add the explicit amplitude restriction

\[
e\le(HSL_q)^{-1}.                                      \tag{Q.12}
\]

Then (Q.11) with \(p=2\), Cauchy--Schwarz, and
\(\|1+Q_k\|_2\le1+\sqrt2K_q\) give

\[
E\mathcal E_k\le X_1,\qquad
E[(1+Q_k)\mathcal E_k]\le X_1,
\]
\[
X_1=2(1+2K_q)\exp(HS+1).                               \tag{Q.13}
\]

For the second bound the direct calculation is at most
\(\sqrt2(1+\sqrt2K_q)e^{HS+1/2}\), which is smaller than
\(X_1\). Higher finite moments also remain finite by (Q.11).

All same-array derivative remainders (R.59)–(R.67) use only the two
expectations in (R.58). Consequently the same displayed
\(R_0\) in (Q.9), now with \(X=X_1\), bounds them exactly as before:
the reverse-source remainder has its factor \(e h_j\), and a full
backward time row has its factor \(e\). In particular the current
terms \(L_kJ_k\) in both (R.65) and (R.66) are bounded by
\(eE[Q_k\mathcal E_k]\); they have not been discarded.

The chronological constants (Q.9) and their induction are unchanged.
Thus, even with the literal initial definitions from Section 3,

\[
\min\left\{1,\frac{P}{2T_0},\frac1{HSL_q},
                 \frac1{2K_*\exp(K_*S)}\right\}        \tag{Q.14}
\]

is an explicit valid threshold using \(X_1\). This reduces the tower
height of the crude sufficient dependence by one.

### 4.2 Use the sharper two-input affine estimates already proved

For the actual constant controls \(c_i=y_i/2\), Section 3 of the main text proves sharper affine coefficients, and
(T.21) proves the sharper primal comparison, than the single oversized
\(q\) in Appendix C.
Replace only the initial definitions of Section 3 by

\[
b_r=2P,\quad F=\exp(36P^2S),\quad q=100b_r^3,
\]
\[
T_0=40b_r^3S F,
\quad A_0=2(24P^2F+\tfrac92P^4),
\quad M_0=2S(8P^2F+P^4),
\]
\[
\sigma=q,\quad D_0=q(1+T_0),\quad m_0=2qD_0.           \tag{Q.15}
\]

The initial numerical bound \(q\) still bounds every query,
same-state query perturbation coefficient, and affine query Lipschitz
constant. Therefore \(D_0=q(1+T_0)\) and
\(m_0=2qD_0\) still bound the actual query and learned-moment errors.
The improved \(T_0\) is exactly the proved comparison
\(40b_r^3S e^{9b_r^2S}\). The displayed \(A_0,M_0\) are exactly
the two-input block/time-row bounds, including the factor two needed
for the time-row norm. Thus no inference from operator norm to formal
response norm is introduced here.

Starting with (Q.15), use all subsequent definitions
\(A,M,k_0,K_1,K_2,K_C,K_{q1},K_{q2},K_q,L_q,H\) in (Q.8),
use \(X=X_1\) from (Q.13), and use the entire finite chain (Q.9).
Define

\[
E_{\rm src}(P,S)=
\min\left\{1,\frac{P}{2T_0},\frac1{HSL_q},
                 \frac1{2K_*\exp(K_*S)}\right\}.       \tag{Q.16}
\]

Equations (Q.8), (Q.9), (Q.13), (Q.15), (Q.16) are a fully specified
finite elementary recipe. There is no hidden \(K\), compact
optimization, numerical experiment, or pointwise infimum over gains.

For completeness, the closure uses the exact inequalities
\(\alpha^2_k\le D_2(e+I_k)\),
\(\alpha^3_k\le D_3(e+I_k)\),
\(\beta^3_k\le E_3(e+I_k)\),
\(\beta^2_k\le E_2(e+I_k)\). Since
\(E_k=\beta^2_k+\beta^3_k\le K_*(e+I_k)\), the finite product
identity gives
\(e+I_k\le e\prod_{r<k}(1+K_*h_r)\le e e^{K_*S}\).
The last restriction in (Q.16) makes each new row differ from its
affine bound by at most one half. Construction proceeds in the exact
order \(A^2_k,A^3_k,B^3_k,B^2_k\). The moment and derivative
estimates at each stage require only the rows available at that stage,
as specified in (R.91)–(R.94); the added restriction (Q.12) concerns
only numerical constants and does not change this order.

## 5. One explicit monotone cutoff for the complete theorem

For \(0<\delta\le1\), retain the affine constants proved in Appendix A

\[
S_\delta=192/\delta,\quad
U_\delta=11+12\sqrt{2/\delta},\quad b=4U_\delta,
\]
\[
Q=40b^3S_\delta\exp(9b^2S_\delta),\quad
J=12b^2Q+\pi b^2,
\]
\[
O=10b^3Q+b(J+\pi/2),\quad
P_\delta=11+2U_\delta.                               \tag{Q.17}
\]

These \(Q,J\) are state/forward comparison constants, distinct from
the lower-case \(q\) used inside the source recipe. Define

\[
e_\delta=\min\left\{
\frac14,\ E_{\rm src}(P_\delta,S_\delta),\
\frac{b}{4Q},\ \frac1{4O},\
\frac{\sqrt{\bar\eta_\delta}}{4J}\right\}>0.            \tag{Q.18}
\]

One can also use the fully literal \(E_{\rm lit}\) from (Q.10)
in this formula; the rest of Theorem T.1 and its all-time margin are
unchanged, with a weaker sufficient dependence on \(\delta\).

For every fixed \(0<e\le e_\delta\), choose \(a=1-e\).
Then \(a\in[3/4,1]\subset[1/2,1]\). The raw state comparison
is at most \(Qe\le b/4\), so it closes strictly inside the primal
ball. Its endpoint prediction differs from \(3/2\) by at most
\(Oe\le1/4\), ensuring a hit of one. The forward discrepancy is
at most \(Je\le\sqrt{\bar\eta_\delta}/4\), so (Q.6)–(Q.7)
and the clock yield the explicit theorem conclusion

\[
\inf_{t\ge0}\min_{i=1,2}\min_{\ell=1,2,3}
\inf_{\alpha,\beta}
E[\psi_e(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
\ge\frac{e^2\delta^3}{196608(1+\delta/8)^3}>0.          \tag{Q.19}
\]

The source restriction supplies all other existence, uniqueness,
finite-GF/raw-GD, velocity, kernel, and path-law bridges proved in
Sections 4--6 of the main text. The initial nontriviality proof needs only \(e>0\), not
an additional quantitative lower or upper restriction.

### Monotonicity

The cutoff (Q.18) is nondecreasing in \(\delta\); equivalently it
decreases when the permitted inputs approach the excluded endpoints.
All of \(S_\delta,U_\delta,P_\delta,b,Q,J,O\) are nonincreasing
functions of \(\delta\), whereas \(\bar\eta_\delta\) is
increasing. In the source chain, every constant apart from a displayed
reciprocal is increasing in \(P,S\), through sums, products,
positive powers, exponentials and maxima. The only reciprocal with an
apparently increasing numerator simplifies to

\[
\frac{P}{2T_0}
=\frac1{640P^2S\exp(36P^2S)}
\]

for the improved chain, and to
\([1600P^2S\exp(800P^3S)]^{-1}\) for the literal chain. Both
decrease in \(P,S\). Finally
\(b/(4Q)=[160b^2S_\delta\exp(9b^2S_\delta)]^{-1}\)
also has the required monotonicity. Taking the minimum preserves it.

## 6. What sufficient asymptotic dependence has actually been proved

The explicit improved recipe is very conservative. Its asymptotic
scale can nonetheless be stated precisely as a sufficient bound.
As \(\delta\downarrow0\),

\[
S_\delta=O(\delta^{-1}),\quad
U_\delta=O(\delta^{-1/2}),\quad
P_\delta=O(\delta^{-1/2}),\quad
P_\delta^2S_\delta=O(\delta^{-2}).                       \tag{Q.20}
\]

In the improved source chain (Q.15), \(A_0,M_0,T_0\) and all
primitive constants are bounded by \(\exp(C\delta^{-2})\) for
some universal \(C\), enlarged finitely many times. Hence \(H\)
has that bound, whereas \(K_q,L_q,X_1,R_0,K_F,K_V,K_U,K_T\) and
the complete chronological \(K_*\) are bounded by

\[
\exp\bigl(\exp(C\delta^{-2})\bigr).
\]

The last denominator \(\exp(K_*S)\) adds one more exponential.
The other terms of (Q.18) are larger than a bound of this scale.
Therefore there are numerical constants \(C,\delta_0>0\) such that

\[
e_\delta\ge
\exp\{-\exp[\exp(C\delta^{-2})]\}
\qquad(0<\delta\le\delta_0).                           \tag{Q.21}
\]

In particular the displayed triple-exponentially small function itself
is a sufficient choice after fixing a large enough universal \(C\).
Equivalently the recipe has
\(\log\log\log(1/e_\delta)=O(\delta^{-2})\).
These statements give a sufficient allowed amplitude; they do not
provide an upper bound on the largest amplitude for which the theorem
could hold.

For comparison, the wholly literal chain (Q.8)–(Q.10) has
\(qS=O(\delta^{-5/2})\), and its \(X_0\), which discarded the
small factor \(e\) in the envelope, adds an extra exponential.
It yields the weaker but immediate sufficient scale

\[
\exp\{-\exp[\exp(\exp(C\delta^{-5/2}))]\}.
\]

Retaining the small coefficient as in (Q.11)–(Q.14) alone reduces this
to three exponentials with the same inner power \(5/2\). Using
the proved sharper two-input affine estimates reduces that power to
two, as in (Q.21).

No claim of necessity, optimality, or sharp endpoint behavior follows.
In particular this does not prove that the true admissible coefficient
must vanish at any such rate, that no polynomial lower bound exists,
or that one positive coefficient cannot work for all strictly
nonendpoint input pairs. The exact incompatible endpoint examples
remain valid, but they do not by themselves settle any of these
interior quantitative questions.


The chosen cutoff tends to zero as delta tends to zero: (Q.18) bounds it above by b/(4Q), whose reciprocal is 160 b² S_delta exp(9 b² S_delta) and tends to infinity. Its value is strictly positive at every fixed delta>0 in the nonvacuous range.


# Appendix A. Two-input symmetry and the affine core

This note proves the symmetry, initial-kernel, affine-reference, and
nonaffinity ingredients for the genuinely unshifted family
\[
\phi_{a,e}(z)=a z+e\arctan z,\qquad \tfrac12\le a\le1,\quad e\ge0.
\]
The source and limit arguments for this gate are verified in the main text and quantitative chapter.

Fix \(0<\delta\le1\), \(\|x_1\|^2=\|x_2\|^2=d\), and
\(|\rho|\le1-\delta\), where \(\rho=x_1^Tx_2/d\). Write
\(y_1=\sigma,y_2=\sigma\tau\), with \(\sigma,\tau\in\{-1,1\}\).
All raw metrics, initialization laws, forward actions, and backward
adjoints have the normalizations in Theorem T.1.
The population readout initially vanishes; the finite raw model's
small random readout is retained.

## 1. Exact label folding and population scalar reduction

Every odd differentiable activation has even derivative. At any parameter
state, induction through the forward and backward equations gives
\[
z^\ell(-x)=-z^\ell(x),\quad h^\ell(-x)=-h^\ell(x),\quad
f(-x)=-f(x),\quad b^\ell(-x)=b^\ell(x).
\]
Replace the dataset by
\(\widetilde x_j=y_jx_j,\widetilde y_j=1\). Then
\(\widetilde h_j^\ell=y_jh_j^\ell\),
\(\widetilde f_j=y_jf_j\),
\(\widetilde r_j=y_jr_j\), and
\(\widetilde b_j^\ell=b_j^\ell\). Consequently
\[
\widetilde r_j\widetilde b_j^1\widetilde x_j^T
=r_jb_j^1x_j^T,\qquad
\widetilde r_j\widetilde b_j^\ell
(\widetilde h_j^{\ell-1})^T=r_jb_j^\ell(h_j^{\ell-1})^T,\qquad
\widetilde r_j\widetilde h_j^3=r_jh_j^3.
\]
Thus finite raw GF and simultaneous raw Euler/GD have exactly the same
parameter trajectory after label folding, including the original finite
readout. The folded correlation is \(\widetilde\rho=\tau\rho\).

Let \(R\) be the orthogonal reflection exchanging the folded inputs:
\[
v=\widetilde x_1-\widetilde x_2,\qquad
R=I-2vv^T/\|v\|^2.
\]
The angle condition ensures \(v\ne0\). Acting by \(R\) on the first
weight field exchanges both folded samples through all hidden layers.
The scalar objective
\[
g(\Theta)=\tfrac12\sum_j y_j f_j
         =\tfrac12\sum_j\widetilde f_j
\]
and physical loss are invariant. The reflection is an isometry of the
raw metric, so both gradient vector fields are equivariant. Identical
sample clips and odd clips on sign-changing slots preserve this fact
at fixed-cap finite Euler level. Gaussian initialization is invariant.

The limiting fixed-program predictions are deterministic contractions.
Since their approximating laws are sample-exchange invariant, those
deterministic predictions must be invariant:
\(\widetilde f_1=\widetilde f_2=g\). Explicitly, an exchange-invariant
random pair converging in probability to a deterministic pair forces
that pair to equal its exchange. Canonical population action spaces
closed under the paired queries realize the invariance by
measure-preserving involutions. Euler induction and strong limits
preserve it exactly on the constructed path, as follows from the finite-program construction in Appendix C, Part F. This uses no uniqueness of an unconstructed uncut flow.

Undoing the fold gives \(f_j=y_jg\) and \(\mathcal L=(1-g)^2\)
for both uncut and capped constructed paths. For the uncut gradient
fields it yields
\[
f_j=y_jg,\qquad \mathcal L=(1-g)^2,\qquad
\dot\Theta=2(1-g)\nabla g.
\]
The feature equation is \(\Theta'=\nabla g\), with
\(ds/dt=2(1-g)\) and \(g'=y^TKy/4\). A finite realization generally
does not satisfy this population scalar prediction identity.
For a cap, the feature equation is instead \(\Theta'=V_R\) and the
physical equation is \(\dot\Theta=2(1-g)V_R\); the scalar clock is the
same but the gradient and kernel-derivative identities are not asserted.

## 2. Initial kernels for the odd family

Let \(q_0=1,c_0=\rho\), and let \(q_\ell,c_\ell\) be the initial
diagonal and off-diagonal feature second moments. Gaussian propagation
gives a centered preactivation pair \((U,V)\) with diagonal
\(q_{\ell-1}\) and covariance \(c_{\ell-1}\). Oddness gives
\[
q_\ell\pm c_\ell
=\tfrac12\mathbb E[\phi_{a,e}(U)\pm\phi_{a,e}(V)]^2.
\]
Since \(\phi_{a,e}'\ge a\),
\[
|\phi_{a,e}(u)-\phi_{a,e}(v)|\ge a|u-v|,\qquad
|\phi_{a,e}(u)+\phi_{a,e}(v)|\ge a|u+v|,
\]
the second inequality following by replacing \(v\) by \(-v\).
Therefore
\[
q_\ell\pm c_\ell\ge a^2(q_{\ell-1}\pm c_{\ell-1}),\qquad
q_3\pm c_3\ge a^6(1\pm\rho)>0.
\]
All hidden kernel blocks initially vanish because \(C(0)=0\). Hence
\[
\kappa_{a,e}(0)=\tfrac14y^TK^4(0)y
=\frac{q_3+\tau c_3}{2}
\ge a^6\frac{1+\tau\rho}{2}\ge\frac{\delta}{128}. \tag{A.1}
\]
The two strict moment eigenvalues also verify nonsingularity of every
initial preactivation pair. For \(e=0\) these recursions are exact:
\[
q_\ell=a^{2\ell},\qquad c_\ell=a^{2\ell}\rho,\qquad
\kappa_{a,0}(0)=a^6(1+\tau\rho)/2. \tag{A.2}
\]
Equal labels activate \(a^6(1+\rho)\); opposite labels activate
\(a^6(1-\rho)\). The absolute-angle condition treats both without an
offset: at antipodal inputs an odd network cannot fit equal nonzero
labels, and at identical inputs it cannot fit opposite labels.

## 3. Affine active and inactive equations

Define
\[
u=(x_1+\tau x_2)/2,\quad v=(x_1-\tau x_2)/2,\quad
v_u=(1+\tau\rho)/2,\quad v_v=(1-\tau\rho)/2.
\]
Then \(u\cdot v=0\), \(\|u\|^2/d=v_u\),
\(\|v\|^2/d=v_v\), and \(v_u,v_v\ge\delta/2\).
For the affine activation \(az\), put
\[
P_\ell=(z_1^\ell+\tau z_2^\ell)/2,\qquad
Q_\ell=(z_1^\ell-\tau z_2^\ell)/2.
\]
Their forward identities are
\[
P_1=w\cdot u,\ Q_1=w\cdot v,\quad
P_2=aAP_1,\ Q_2=aAQ_1,\quad
P_3=aBP_2,\ Q_3=aBQ_2. \tag{A.3}
\]
Thus \(H=\frac12\sum_j y_jh_j^3=\sigma aP_3\) and
\(g=\sigma a^3\langle C,BAP_1\rangle\). Taking its gradient in the
raw metric gives exactly
\[
\begin{aligned}
C'&=\sigma aP_3,\\
B'&=\sigma a^2C\otimes P_2=\sigma a^3C\otimes(AP_1),\\
A'&=\sigma a^3B^*C\otimes P_1,\\
P_1'&=\sigma v_u a^3A^*B^*C,\qquad Q_1'=0.
\end{aligned} \tag{A.4}
\]
Indeed \(w'=(\sigma a^3/d)(A^*B^*C)u\); contraction with \(u\)
produces \(v_u\), and contraction with \(v\) vanishes. These equations
depend only on \((P_1,A,B,C)\), never on the inactive root \(Q_1(0)\).

Both label sectors are explicit:

* If \(y_1=y_2\), \(P_\ell\) is the common field and \(Q_\ell\) the
  contrast; \(v_u=(1+\rho)/2,v_v=(1-\rho)/2\).
* If \(y_1=-y_2\), \(P_\ell\) is the contrast and \(Q_\ell\) the common
  field; \(v_u=(1-\rho)/2,v_v=(1+\rho)/2\).

## 4. Uniform affine interval through \(g=3/2\)

The affine objective is a continuous polynomial on the affine raw
Hilbert space. Its gradient is locally Lipschitz, with bounded
derivatives on bounded balls uniformly for \(a\in[1/2,1]\).
Picard contraction on such a ball supplies strong local existence and
uniqueness, including at every finite reached state.

Write the hidden state as \(\vartheta\), and \(J_s\) for the bounded
linearization of \(H\). The gradient equations are
\(C'=H,\vartheta'=J_s^*C\), and the strong chain rule gives
\[
C''=J_sJ_s^*C,\qquad \langle C,C''\rangle=\|J_s^*C\|^2\ge0,
\qquad g'=\|C'\|^2+\|J_s^*C\|^2=\|\Theta'\|_{\rm raw}^2.
\]
Twice differentiating \((\|C\|^2+\epsilon^2)^{1/2}\), using
Cauchy--Schwarz and \(\langle C,C''\rangle\ge0\), proves convexity.
Letting \(\epsilon\downarrow0\) gives convexity of \(\|C\|\).
Its initial right slope is \(\|H(0)\|\), because
\(C(0)=0,C'(0)=H(0)\). Thus \(\|C'(s)\|\ge\|H(0)\|\) and
\[
g'\ge\kappa_0,\qquad
\int_0^s\|\Theta'(r)\|_{\rm raw}^2\,dr=g(s),\qquad
\kappa_0=a^6v_u\ge\delta/128. \tag{A.5}
\]

The first hit \(S\) of \(g=3/2\) exists. Before that hit,
\(s\le3/(2\kappa_0)\), and the energy is at most \(3/2\).
A finite maximal endpoint below the target has a strong limit since
\[
\|\Theta(v)-\Theta(u)\|_{\rm raw}
\le\sqrt{(v-u)[g(v)-g(u)]}\le\sqrt{\tfrac32(v-u)}.
\]
Local existence at that reached state extends the branch. An
arbitrarily long branch below the target contradicts \(g(s)\ge\kappa_0s\).
Cauchy--Schwarz then gives, on the entire closed interval \([0,S]\),
\[
S\le S_\delta:=192/\delta,\qquad
\|\Theta(s)-\Theta(0)\|_{\rm raw}
\le\frac3{2\sqrt{\kappa_0}}
\le R_\delta:=12\sqrt2/\sqrt\delta. \tag{A.6}
\]
Set
\[
U=11+R_\delta. \tag{A.7}
\]
Initial first-layer projected norms are one, action norms are at most
ten, and the readout vanishes. Raw displacement controls each projected
change by \(\|\Delta w\cdot x_j\|_2\le\sqrt d\|\Delta w\|_2\),
and operator changes by Hilbert--Schmidt norms. Consequently
\[
\max_j\|z_j^1(s)\|_2,\ \|A(s)\|_{\rm op},\
\|B(s)\|_{\rm op},\ \|C(s)\|_2\le U. \tag{A.8}
\]
The full initial \(\sqrt d\|w_0\|_2\) need not be dimension-independent;
only its projections and raw displacement enter these constants.
Each reference path stops at its own hit \(S\), never being extended
to the uniform duration upper bound \(S_\delta\).

## 5. Active lower bounds and frozen inactive Gaussian fields

Since \(C'=\sigma aP_3\), the radial bound implies
\(a^2\|P_3\|^2\ge a^6v_u\). Using (A.3) and (A.8) backwards gives
\[
\|P_3\|^2\ge a^4v_u,\qquad
\|P_2\|^2\ge a^2v_u/U^2,\qquad
\|P_1\|^2\ge v_u/U^4. \tag{A.9}
\]
Every active hidden field therefore remains nonzero.

A stronger variance bound comes from exact population freezing of the
inactive fields. This requires independence, not merely bounded learned
Hilbert--Schmidt increments. In a fixed finite affine scalar-Euler
prefix with zero initial readout, let
\(\mathscr F_n=\sigma(P_{1,0},A_0,B_0)\). Equations (A.4) make all
active training fields \(\mathscr F_n\)-measurable. Orthogonality of the
Gaussian input projections makes \(Q_0=Q_{1,0}\) an independent
\(N(0,v_vI_n)\) vector. For an \(\mathscr F_n\)-measurable matrix \(T_n\),
\[
\mathbb E[\|T_nQ_0\|_n^2\mid\mathscr F_n]
=\frac{v_v}{n}\|T_n\|_F^2. \tag{A.10}
\]
On bounded-initial-operator events, each fixed Euler prefix has bounded
field norms and ordinary Frobenius norms of its learned increments.
The normalization is
\(\|\Delta s\,p q^T/n\|_F=\Delta s\|p\|_n\|q\|_n\). Moreover
\[
\|B_sA_s-B_0A_0\|_F
\le\|B_s-B_0\|_F\|A_s\|_{\rm op}
+\|B_0\|_{\rm op}\|A_s-A_0\|_F.
\]
Apply (A.10) to \(A_s-A_0\) and \(B_sA_s-B_0A_0\).
Their normalized actions on \(Q_0\) tend to zero in probability.
The deterministic joint fixed-program limit therefore gives exact
Hilbert-space identities at population Euler nodes:
\[
Q_1(s)=Q_0,\qquad Q_2(s)=aA_0Q_0,\qquad
Q_3(s)=a^2B_0A_0Q_0. \tag{A.11}
\]
Strong bounded-interval Euler convergence for the affine polynomial
field preserves (A.11) at every \(s\in[0,S]\). Initial Gaussian matrix
propagation then gives
\[
Q_\ell(s)\sim N(0,a^{2(\ell-1)}v_v). \tag{A.12}
\]

For \(\mathscr F_n\)-measurable \(p_n,T_n\), conditional Gaussianity gives
\[
\mathbb E[\langle p_n,T_nQ_0\rangle_n\mid\mathscr F_n]=0,\qquad
\mathbb E[\langle p_n,T_nQ_0\rangle_n^2\mid\mathscr F_n]
\le\frac{v_v}{n}\|T_n\|_{\rm op}^2\|p_n\|_n^2. \tag{A.13}
\]
Use \(T_n=I,aA_s,a^2B_sA_s\) and \(p_n=P_\ell(s)\), and also
\(p_n=\mathbf1\). Fixed-program convergence and then strong affine
Euler convergence give
\[
\mathbb E Q_\ell(s)=0,\qquad
\mathbb E[P_\ell(s)Q_\ell(s)]=0. \tag{A.14}
\]
As \(z_1^\ell=P_\ell+Q_\ell\) and
\(z_2^\ell=\tau(P_\ell-Q_\ell)\), one obtains
\[
\operatorname{Var}(z_j^\ell(s))
=\operatorname{Var}(P_\ell(s))+a^{2(\ell-1)}v_v
\ge\delta/32,\qquad j=1,2. \tag{A.15}
\]
Here \(a^4\ge1/16\) and \(v_v\ge\delta/2\). The frozen field is the
contrast for equal labels and the common field for opposite labels.

All affine preactivations are Gaussian, not merely of positive
variance. In a finite affine population Euler prefix, every forward,
reverse, and evolving field is linear in finitely many joint Gaussian
source coordinates in its layer. Inductively, the gate \(a\) is
constant, the activation is linear, unrolled rank-one memories multiply
previous fields only by deterministic scalar contractions, and each
new initialized matrix call is a Gaussian innovation plus linear
Gaussian-conditioning response terms. No product of varying neuron
coordinates occurs outside a scalar contraction. Strong Euler
convergence passes their means, covariances, and Gaussian
characteristic functions to the exact affine path.

Their means vanish: changing \(P_{1,0}\) to its negative sends
\(P_\ell,C\) to their negatives and leaves \(A,B\) fixed in (A.4).
The invariant initialization and deterministic limiting laws force
zero active means; (A.14) supplies zero inactive means. Finally,
\[
\|z_j^1\|_2\le U,\qquad
\|z_j^2\|_2\le aU^2\le U^2,\qquad
\|z_j^3\|_2\le a^2U^3\le U^3. \tag{A.16}
\]
Thus every affine marginal has form \(\nu G\), \(G\sim N(0,1)\), with
\[
m:=\sqrt{\delta/32}\le\nu\le L:=U^3. \tag{A.17}
\]

## 6. Uniform Gaussian nonaffinity and perturbative transfer

For a square-integrable real variable \(Z\) with positive variance, put
\[
\mathcal R(Z)=\inf_{\alpha,\beta}\mathbb E[
\arctan Z-\alpha-\beta Z]^2
=\operatorname{Var}(\arctan Z)
-\frac{\operatorname{Cov}(Z,\arctan Z)^2}{\operatorname{Var}(Z)}.
\]
Define a constant depending only on \(\delta\):
\[
\eta_\delta=\min_{m\le\nu\le L}\mathcal R(\nu G)>0. \tag{A.18}
\]
Coupling by the same \(G\), boundedness and Lipschitzness of arctangent,
and the denominator bound \(m^2\) show continuity on this compact
interval. Zero residual would identify arctangent with an affine
function Gaussian-almost everywhere. Positive density and continuity
would then extend the identity to all of \(\mathbb R\), contradicting
the nonconstant derivative. Thus the minimum is positive and
\[
\inf_{a\in[1/2,1]}\ \inf_{j,\ell,s\le S}
\mathcal R(z_{j,a,0}^\ell(s))\ge\eta_\delta. \tag{A.19}
\]
The endpoint \(S\) in each term is that affine reference's own endpoint.

The transfer estimate needs no Gaussianity of the perturbed variable.
Suppose \(\|Z-Z_0\|_2\le t\),
\(\operatorname{sd}(Z_0)\ge m\), and
\(\mathcal R(Z_0)\ge\eta_\delta\). Then
\[
t\le t_\delta:=
\min\left\{m/2,\frac{\sqrt{\eta_\delta}}{2(1+\pi/m)}\right\}
\quad\Longrightarrow\quad \mathcal R(Z)\ge\eta_\delta/4. \tag{A.20}
\]
Indeed centering is an orthogonal projection, so standard deviation is
1-Lipschitz and \(\operatorname{sd}(Z)\ge m/2\). The optimal slope for
regressing \(\arctan Z\) on \(Z\) has absolute value at most
\(\operatorname{sd}(\arctan Z)/\operatorname{sd}(Z)\le\pi/m\).
Using its intercept and slope as a competitor for \(Z_0\) gives
\[
\sqrt{\mathcal R(Z_0)}
\le\sqrt{\mathcal R(Z)}+(1+\pi/m)t,
\]
proving (A.20). Absorbing \(aZ\) into the free affine approximant gives
the exact identity
\[
\inf_{\alpha,\beta}\mathbb E[
\phi_{a,e}(Z)-\alpha-\beta Z]^2=e^2\mathcal R(Z). \tag{A.21}
\]
Consequently a separately proved comparison
\(\|z_{j,a,e}^\ell-z_{j,a,0}^\ell\|_2\le Je\), uniform on these
reference intervals with \(J\) depending only on \(\delta\), gives
the uniform positive activation-regression margin
\(e^2\eta_\delta/4\) whenever \(0<e\le t_\delta/J\).
The constants in (A.6), (A.7), (A.17), (A.18), and (A.20) precede the slope,
dataset, labels, dimension, width, and physical horizon.



# Appendix B. Initial motion for two inputs

The raw model is Theorem T.1. The Gaussian-program and derivative-valid initialization observations used here are proved in Appendix C, Parts F and V.I; the source specialization is checked in the main text.

Fix
\[
 \phi(z)=az+e\arctan z,\qquad \tfrac12\le a\le1,\quad e>0,
 \qquad |\rho|\le1-\delta,\quad 0<\delta\le1.
\]
Use the raw model and metric (T.3)--(T.7), two labels \(y_i\in\{-1,1\}\), and put \(p_i=y_i/2\), \(\tau=y_1y_2\). The restriction \(\delta\le1\) is the nonvacuous range for this symmetric separation. All second derivatives are identified by their time coordinate below.

## 1. Forward nondegeneracy and a useful initial kernel bound

The first preactivation pair is nondegenerate centered Gaussian. For any nondegenerate centered Gaussian pair \((U,V)\) with equal marginal variance and any \((u_1,u_2)\ne0\), a zero \(L^2\) norm of \(u_1\phi(U)+u_2\phi(V)\) would, by positive Gaussian density and continuity, give the identity
\[
 u_1\phi(s)+u_2\phi(t)=0\quad\text{for every }s,t\in\mathbb R.
\]
Differentiating separately, and using \(\phi'>0\), forces both coefficients to vanish. Thus the feature Gram is positive definite. Induction through the two fresh forward calls makes every initialized preactivation pair nondegenerate Gaussian and every initialized feature Gram positive definite.

Here is a uniform lower bound, which does not require a Gram inverse. Let \(q_0=1,c_0=\rho\) and let \(q_\ell,c_\ell\) be the common feature second moment and cross moment after layer \(\ell\). Since \(\phi'\ge a\) and \(\phi\) is odd,
\[
 |\phi(u)-\phi(v)|\ge a|u-v|,\qquad
 |\phi(u)+\phi(v)|\ge a|u+v|.
\]
Each initialized Gaussian pair is exchangeable, so
\[
 q_\ell\pm c_\ell
 =\tfrac12E[\phi(U)\pm\phi(V)]^2
 \ge a^2(q_{\ell-1}\pm c_{\ell-1}).
\]
Consequently
\[
 q_\ell\pm c_\ell\ge a^{2\ell}(1\pm\rho),\qquad
 \kappa_0:=\left\|\sum_i p_i h^3_{i,0}\right\|_3^2
 =\frac{q_3+\tau c_3}{2}
 \ge\frac{a^6\delta}{2}\ge\frac\delta{128}>0.
\]
These bounds hold for both label sectors. They are lower bounds, not formulas for a shifted activation. For the odd affine reference \(\phi(z)=az\), the exact formula is
\[
 \kappa_{0,\mathrm{aff}}=a^6(1+\tau\rho)/2.
\]

## 2. Full transpose covariances survive oddness

Write \(H_0=\sum_i p_i h^3_{i,0}\), \(D_i^\ell=\phi'(Z^\ell_{i,0})\), and
\[
 \beta_i^3=H_0D_i^3,\qquad S_3=E_3[\beta^3(\beta^3)^T].
\]
The matrix \(S_3\) is strictly positive definite even in the same-label sector. Indeed, a zero quadratic form would imply the everywhere identity
\[
 [p_1\phi(z_1)+p_2\phi(z_2)]
 [u_1\phi'(z_1)+u_2\phi'(z_2)]=0.
\]
For each fixed \(z_2\), the first factor has at most one zero as a function of \(z_1\), because \(p_1\ne0\) and \(\phi'>0\). The second factor vanishes off that point and hence everywhere by continuity. Differentiating it in \(z_1\) gives \(u_1\phi''(z_1)=0\) for every \(z_1\). Since
\[
 \phi''(z)=-2ez/(1+z^2)^2
\]
is not identically zero, \(u_1=0\); positivity of \(\phi'\) then gives \(u_2=0\).

Let \(B_0:H_2\to H_3\) be the initialized top action. The fixed finite-program transpose identity is
\[
 B_0^*\beta_i^3
 =G_i^2+\sum_jh^2_{j,0}\,T_{ij},\qquad
 T_{ij}=E_3[\partial_{z_j}\beta_i^3],
\]
where the joint Gaussian pair \(G^2\) has covariance **\(S_3\) itself**, and is independent of the initialized population-two forward sources. Explicitly,
\[
 \partial_{z_j}\beta_i^3
 =p_j\phi'(z_j)\phi'(z_i)
 +\mathbf1_{i=j}\Big(\sum_kp_k\phi(z_k)\Big)\phi''(z_i).
\]
Replacing \(S_3\) by the covariance remaining after regression on the forward features is incorrect. The finite-rank source-space projection from Gaussian matrix conditioning has negligible normalized coordinate effect in the infinite-width limit; the deterministic response above remains, and the coordinate Gaussian innovation has the full second-moment covariance.

Define
\[
 \beta_i^2=D_i^2\left(G_i^2+\sum_jh^2_{j,0}T_{ij}\right),
 \qquad S_2=E_2[\beta^2(\beta^2)^T].
\]
Conditionally on the initial population-two forward pair,
\[
 \operatorname{Cov}(\beta^2\mid Z^2_0)
 =\operatorname{diag}(D^2)S_3\operatorname{diag}(D^2)
 \succeq a^2\lambda_{\min}(S_3)I.
\]
Thus \(S_2\succeq a^2\lambda_{\min}(S_3)I>0\). The second initialized transpose has the form
\[
 A_0^*\beta_i^2
 =G_i^1+\sum_jh^1_{j,0}E_2[\partial_{\xi_j^2}\beta_i^2],
 \qquad \operatorname{Cov}(G^1)=S_2,
\]
with \(G^1\) independent of the population-one root pair. In this derivative the deterministic coefficients \(T\) and Gaussian covariances are held fixed, and \(G^2\) is an independent named source. The derivative includes the actual \(h^2\)-dependence of the response term. Finally,
\[
 \beta_i^1=D_i^1A_0^*\beta_i^2.
\]
All derivative expectations are finite: the activation grows at most linearly, all positive-order derivatives used here are bounded, and the source variables have Gaussian moments. The derivative-valid single-transcript truncation proof in Appendix C, V.I, therefore applies without a new mesh-uniform assertion. Oddness changes no step of these identities.

## 3. Every hidden block has nonzero feature-time acceleration

Define, in the raw hidden metric,
\[
 V^1=\frac1d\sum_i p_i\beta_i^1x_i,\qquad
 V^2=\sum_i p_i\beta_i^2\otimes h^1_{i,0},\qquad
 V^3=\sum_i p_i\beta_i^3\otimes h^2_{i,0}.
\]
If \(F\) is the relevant initial feature Gram and \(S\) the corresponding beta Gram, then
\[
 \|V^\ell\|_{\mathrm{HS}}^2
 =\operatorname{tr}(S\operatorname{diag}(p)F\operatorname{diag}(p))>0
 \quad(\ell=2,3),
\]
since both matrices in this trace product are positive definite. For the first block, condition on the first forward pair and use the Gaussian innovation of covariance \(S_2\). This gives
\[
 dE_1\|V^1\|_{\mathbb R^d}^2
 \ge a^2\lambda_{\min}(S_2)
       \sum_i p_i^2\frac{\|x_i\|^2}{d}
 =\frac{a^2\lambda_{\min}(S_2)}2>0.
\]
The deterministic conditional means contribute a nonnegative term. No input Gram inverse is used.

On a strong feature-time solution \(\Theta'=\nabla g\) with the stated chain rule and bounded gates,
\[
 C(s)=sH_0+o_{L^2}(s),\qquad
 b_i^\ell(s)=s\beta_i^\ell+o_{L^2}(s).
\]
For example, propagate \(C(s)/s\to H_0\) backwards, using operator-norm continuity of trained actions, bounded gates, and convergence of a bounded multiplier acting on each fixed \(L^2\) factor. The hidden vector field divided by \(s\) tends to \(V\), so integration yields
\[
 \vartheta(s)=\vartheta(0)+\tfrac12s^2V+o_{\mathrm{raw}}(s^2).
\]
Every hidden parameter **block** therefore has nonzero second derivative. This does not claim that every scalar first-layer coordinate changes: directions orthogonal to the input span are unchanged by the raw update.

## 4. Every sample in every hidden layer has nonzero acceleration

Let \(U_i^\ell\) be the initial feature-time preactivation acceleration obtained by applying the forward linearization to \(V\). At the bottom,
\[
 U_i^1=\sum_j\Gamma_{ij}p_j\beta_j^1.
\]
Its conditional variance is bounded below by
\[
 \operatorname{Var}(U_i^1\mid Z^1_0)
 \ge a^2\lambda_{\min}(S_2)\sum_j\Gamma_{ij}^2p_j^2
 \ge a^2\lambda_{\min}(S_2)/4>0.
\]
For the upper layers, product rules and actual adjoints give
\[
 \sum_i p_i\langle\beta_i^2,U_i^2\rangle_2
 =dE\|V^1\|^2+\|V^2\|_{\mathrm{HS}}^2>0,
\]
\[
 \sum_i p_i\langle\beta_i^3,U_i^3\rangle_3
 =\|V\|_{\mathrm{hidden}}^2>0.
\]
For instance \(U_i^2=V^2h_i^1+A_0(D_i^1U_i^1)\); pairing the first term produces \(\|V^2\|^2\), and moving \(A_0\) to its actual adjoint in the second produces the first-block norm. The next layer adds \(\|V^3\|^2\).

Hence at least one sample has nonzero acceleration in each upper layer. To obtain **each** sample, use the existing input reflection \(Qx_1=x_2\), \(Qx_2=x_1\) and the raw isometry
\[
 (w,A,B,C)\longmapsto(Qw,A,B,\tau C).
\]
Its initialization law is invariant, and it preserves the scalar objective. It sends \(\beta_i^\ell\) to \(\tau\beta_{\pi i}^\ell\), \(V^1\) to \(QV^1\), leaves \(V^2,V^3\) unchanged, and sends \(U_i^\ell\) to \(U_{\pi i}^\ell\). Thus the two \(U\)-fields have equal squared population norms. Both must be nonzero. Since \(D_i^\ell\ge a>0\), the feature acceleration \(D_i^\ell U_i^\ell\) is nonzero for every layer and sample as well. This symmetry works for both \(\tau=1\) and \(\tau=-1\); no even component of the activation is used.

## 5. Kernel change and the physical-time factors

Writing \(J_0\) for the bounded directional linearization of \(H\), adjunction gives \(V=J_0^*H_0\). Therefore
\[
 \kappa_4(s)=\|H(s)\|^2
 =\kappa_0+s^2\|V\|^2+o(s^2),
\]
\[
 \kappa(s)=\frac14y^TK(s)y
 =\kappa_0+2s^2\|V\|^2+o(s^2).
\]
The first coefficient follows from \(H(s)=H_0+(s^2/2)J_0V+o(s^2)\). The projected sum of hidden kernel blocks is \(s^2\|V\|^2+o(s^2)\). The total projected kernel thus changes strictly near zero.

The exact population reduction has \(ds/dt=2(1-g)\). Since \(g(0)=0\) and \(g'_s(0)=\kappa_0\),
\[
 s'(0)=2,\qquad s''(0)=-4\kappa_0.
\]
Consequently the physical hidden acceleration is \(4V\), the physical sample preactivation/feature accelerations are respectively \(4U_i^\ell\) and \(4D_i^\ell U_i^\ell\), and
\[
 \kappa_4(t)=\kappa_0+4t^2\|V\|^2+o(t^2),\qquad
 \kappa(t)=\kappa_0+8t^2\|V\|^2+o(t^2).
\]
For the readout, \(C_s'(0)=H_0\ne0\) and \(C_s''(0)=0\), but physical time gives
\[
 \dot C(0)=2H_0,\qquad \ddot C(0)=-4\kappa_0H_0\ne0.
\]
The latter follows directly by differentiating \(\dot C=2(1-g)H\), because the initial hidden velocity and hence \(\dot H(0)\) vanish. Thus **all four parameter blocks have nonzero physical initial acceleration**, while only the three hidden blocks have nonzero feature-time initial acceleration. The finite random readout remains the original one; these statements concern its population-zero initial limit.



# Three-input initialization geometry and remaining global question

In this chapter use the raw model of Appendix C, Part M, with activation phi(z)=a z+e arctan(z), a=1-e and 0<e<=1/2. The lemmas also hold for independent a>=1/2 and e>0 where indicated.

The geometric assumptions are \(u_i=x_i/\sqrt d\), \(\|u_i\|=1\), and
\(|\Gamma_{ij}|\le1-\delta\), where \(\Gamma_{ij}=u_i\cdot u_j\).
Open separation in the requested statement implies these weak inequalities.
All assertions below also hold for independent \(a\ge1/2,e>0\).

## What this establishes, and what it does not

Pairwise absolute separation removes all antipodal/duplicate initialization
obstructions for three inputs, even when their Gram matrix is singular.
There is an explicit strictly positive lower bound on the initialized
nonlinear feature Gram, with matching worst-case scale \(e^2\delta^2\).
The algebraically defined initial acceleration directions are nonzero in
every hidden parameter block and for every individual sample in every
hidden layer. Conditional on a canonical strong solution with the trajectory
chain rule, they are its nonzero physical accelerations, and its projected
total kernel has precisely the coefficient \(18\|V\|^2\). The upper
sample assertion has a direct fresh-Gaussian-innovation proof, requiring
neither permutation symmetry nor a nonzero affine comparison direction.
These conditional trajectory conclusions do not assert existence of the
flow, which remains part of the unresolved complete theorem below.

However, the complete all-time three-input theorem is not established by
these facts. Its existing affine-clock proof has a genuine obstruction:
admissible rank-two triples may have a target component outside the affine
network's output space. The affine residual clock is then infinite. In the
equilateral, equal-label case the entire affine population trajectory is
stationary. This invalidates that proof route; it is not a counterexample
to the positive-\(e\) theorem.

The only imported population machinery in the initial-motion statements is
the fixed finite Gaussian program/action theorem and its derivative-valid
initial transpose observation in Appendix C, Parts F and V.I. Those hypotheses are
checked below for the additional forward queries. The finite Gaussian
conditioning argument for their crucial positive innovation is also given.
No assertion about arbitrary bounded initialized operators is substituted
for the canonical Gaussian initialization.

## 1. Exact odd symmetry and the singular affine obstruction

For every finite parameter state a bias-free odd network satisfies
\(h^\ell(-x)=-h^\ell(x)\) and \(f(-x)=-f(x)\). Its gates are even.
Replacing \((x_i,y_i)\) by \((y_i x_i,1)\) therefore leaves the squared loss,
as a function of all raw parameters, exactly unchanged. GF and GD have
identical parameter trajectories under this label folding. The input Gram
changes to \(D_y\Gamma D_y\), which preserves absolute pairwise separation.

Unlike two folded inputs, three folded inputs need not have an orthogonal
symmetry acting transitively on their indices. A permutation can be induced
by an input isometry only if it preserves their Gram matrix. A transitive
permutation group on three vertices forces all three off-diagonal Gram
entries to coincide. Thus generic folded triples have no symmetry forcing
all predictions or residuals to be equal.

For the affine network \(\phi(z)=az\), the predictor is linear in its input
at every parameter state. Hence its prediction vector belongs to
\(\operatorname{ran}\Gamma\). If \(v\in\ker\Gamma\), then

\[
v^Tf(t)=0,\qquad v^Tr(t)=-v^Ty
\]

at every time and for both algorithms. If \(v^Ty\ne0\),
\(\|r(t)\|_2\ge |v^Ty|/\|v\|_2>0\). In particular any residual clock
\(\int_0^\infty\|r(t)\|_1dt\) diverges. Absolute pairwise separation does
not exclude this case.

For an especially sharp example, take three unit planar vectors with
pairwise inner products \(-1/2\), and labels \(y=(1,1,1)\). This is allowed
whenever \(0<\delta<1/2\) for the requested strict separation. They obey
\(u_1+u_2+u_3=0\). All affine hidden feature sums vanish for every parameter
state. Starting at population \(C=0\), the readout derivative is zero;
the hidden derivatives have a factor \(C\) and are zero. Thus the affine
population solution is stationary with loss \(3/2\).

More generally, \(\Gamma y=0\) with \(y_i\in\{-1,1\}\) is equivalent to
the folded inputs being an equilateral triple: if
\(v_i=y_i u_i\), then \(v_1+v_2+v_3=0\), and
\(\|v_i+v_j\|^2=\|v_k\|^2=1\) gives \(v_i\cdot v_j=-1/2\).
The converse is immediate. A rank-two Gram can also have a kernel vector
with unequal coefficient magnitudes, creating an incompatible affine
target without complete stationarity.

## 2. Cubic lifting is uniformly positive for three separated lines

Let \(T_i=u_i^{\otimes3}\) in the Hilbert tensor product. Their Gram matrix
is \(\Gamma^{\circ3}\), the entrywise cube. Set
\(s_\delta=\delta(2-\delta)\). For each \(i\) and each \(j\ne i\), define

\[
v_{ij}=\frac{u_i-\Gamma_{ij}u_j}{\sqrt{1-\Gamma_{ij}^2}}.
\]

Then \(\|v_{ij}\|=1\), \(v_{ij}\perp u_j\), and
\(u_i\cdot v_{ij}=\sqrt{1-\Gamma_{ij}^2}\ge\sqrt{s_\delta}\).
If \(\{i,j,k\}=\{1,2,3\}\), put
\(R_i=u_i\otimes v_{ij}\otimes v_{ik}\). Its norm is one, and

\[
\langle T_l,R_i\rangle=0\ (l\ne i),\qquad
\langle T_i,R_i\rangle\ge s_\delta.
\]

For \(T=\sum_l c_lT_l\), Cauchy--Schwarz gives
\(|c_i|s_\delta\le\|T\|\). Summing its square over three indices proves

\[
\boxed{\quad\Gamma^{\circ3}\succeq
\frac{\delta^2(2-\delta)^2}{3}I_3.\quad}                 \tag{1}
\]

This proof permits singular \(\Gamma\), uses no covariance inverse, and
works in the actual input dimension. It proves that the cubic ridge
functions corresponding to the three inputs are linearly independent.

## 3. Explicit nonlinear feature-Gram lower bound

Let \(G\sim N(0,1)\), \(H_3(z)=z^3-3z\), and

\[
m=E(1+G^2)^{-1},\qquad b_3=(1-2m)/\sqrt6.
\]

Strict Jensen for the strictly convex function \(t\mapsto(1+t)^{-1}\)
gives \(m>1/2\), so \(b_3\ne0\). Integration by parts once yields

\[
E[\arctan(G)H_3(G)]
=E[(G^2-1)/(1+G^2)]=1-2m.
\]

Write \(Z_i=u_i\cdot g\) for the initialized first Gaussian projections
and \(P_i=H_3(Z_i)/\sqrt6\). Gaussian conditioning gives
\(E[H_3(Z_i)\mid Z_j]=\Gamma_{ij}^3H_3(Z_j)\), obtained directly by
expanding \(Z_i=\Gamma_{ij}Z_j+\sqrt{1-\Gamma_{ij}^2}G'\).
Consequently

\[
E[P_iP_j]=\Gamma_{ij}^3,\qquad
E[\phi(Z_i)P_j]=e b_3\Gamma_{ij}^3.
\]

Thus each residual \(\phi(Z_i)-e b_3P_i\) is orthogonal to every \(P_j\).
Their Gram decomposition and (1) prove

\[
Q_1:=(E[h_i^1h_j^1])_{ij}
\succeq e^2b_3^2\Gamma^{\circ3}
\succeq e^2b_3^2\frac{\delta^2(2-\delta)^2}{3}I_3.       \tag{2}
\]

There is also a direct first-chaos propagation bound. If a centered
Gaussian tuple has common variance \(q>0\) and covariance \(Q\), let
\(c=E[\phi(\sqrt qG)G]/\sqrt q\). Since
\(z\arctan z\ge0\), \(c\ge a\). Conditional Gaussian expectation shows
that \(\phi(Z_i)-cZ_i\) is orthogonal to every \(Z_j\). Therefore its
feature Gram is \(c^2Q\) plus a positive semidefinite matrix, and is at
least \(a^2Q\). The initialized scalar variances agree across samples,
so this applies at each following layer:

\[
Q_2\succeq a^2Q_1\succ0,\qquad Q_3\succeq a^2Q_2\succ0. \tag{3}
\]

For \(p=y/3\) and \(H=\sum_i p_i h_i^3\),

\[
\|H\|^2=p^TQ_3p\ge
a^4e^2b_3^2\delta^2(2-\delta)^2/9>0.                   \tag{4}
\]

This explicitly disproves a proposed exact three-point cancellation for
the positive mixture. In particular the equilateral affine obstruction
is removed already at initialization when \(e>0\).

### 3.1. Matching sharpness of the worst-case initialization scale

The \(e^2\delta^2\) scale in (2) cannot be improved uniformly over the
admissible three-input geometry, up to absolute constant factors. This is
an assertion about the smallest eigenvalue of the first initialized feature
Gram, not a necessary or sufficient bound on the training cutoff
\(e_\delta\).

For \(0<c<1\), order the planar unit inputs as

\[
u_+=(c,\sqrt{1-c^2}),\qquad u_0=(1,0),\qquad
u_-=(c,-\sqrt{1-c^2}).
\]

Their three pairwise inner products are \(c,c,2c^2-1\), and
\(v=(1,-2c,1)^T\) is a Gram-kernel vector because
\(u_+-2cu_0+u_-=0\). For independent standard normals \(G_1,G_2\), let
\(Z_0=G_1\), \(Z_\pm=cG_1\pm\sqrt{1-c^2}G_2\), and write
\(F=\arctan\). The linear part of the activation cancels exactly:

\[
\begin{split}
\sum_i v_i\phi(Z_i)
&=e\{F(Z_+)+F(Z_-)-2cF(G_1)\}\\
&=e\{F(cG_1+h)+F(cG_1-h)-2F(cG_1)\\
&\hspace{34mm}+2[F(cG_1)-cF(G_1)]\},\qquad
h=\sqrt{1-c^2}G_2.
\end{split}
\]

The bounds \(\|F'\|_\infty\le1\), \(\|F\|_\infty\le\pi/2\), and
\(\|F''\|_\infty\le1\) suffice. For the last bound,
\(2|z|/(1+z^2)^2\le1\) follows from \(2|z|\le1+z^2\).
Taylor's formula with integral remainder in both signs gives

\[
|F(x+h)+F(x-h)-2F(x)|\le h^2.
\]

Also
\(|F(cG_1)-cF(G_1)|\le(1-c)(|G_1|+\pi/2)\).
Since \(\|G_2^2\|_2=\sqrt3\) and \(\|G_1\|_2=1\), Minkowski gives

\[
\begin{split}
\|F(Z_+)+F(Z_-)-2cF(G_1)\|_2
&\le(1-c^2)\sqrt3+2(1-c)(1+\pi/2)\\
&\le(1-c)C_0,\qquad C_0=2\sqrt3+2+\pi.
\end{split}
\]

Taking the Rayleigh quotient in direction \(v\), whose squared norm is
\(2+4c^2\), proves

\[
\lambda_{\min}(Q_1)
\le \frac{e^2(1-c)^2C_0^2}{2+4c^2}.                    \tag{4a}
\]

For the closed class \(|\Gamma_{ij}|\le1-\delta\), choose
\(c=1-\delta\), \(0<\delta\le1/4\). The center-to-side inner products
equal \(1-\delta\). The side-to-side inner product is
\(r=1-4\delta+2\delta^2>0\), and
\((1-\delta)-r=\delta(3-2\delta)>0\). Hence all three absolute
pairwise inequalities hold, and

\[
\lambda_{\min}(Q_1)
\le \frac{e^2\delta^2C_0^2}{2+4(1-\delta)^2}.           \tag{4b}
\]

For the requested strict class
\(-1+\delta<\Gamma_{ij}<1-\delta\), choose instead
\(c=1-2\delta\), again with \(0<\delta\le1/4\). The two center-to-side
inner products lie strictly inside the interval since
\((1-\delta)-c=\delta>0\) and \(c-(-1+\delta)=2-3\delta>0\).
For the side-to-side inner product \(r=1-8\delta+8\delta^2\), both
strict inequalities follow from

\[
(1-\delta)-r=\delta(7-8\delta)>0,
\]

\[
r-(-1+\delta)
=2-9\delta+8\delta^2
=(1-4\delta)(2-2\delta)+\delta>0.
\]

Thus this example is strictly admissible and satisfies

\[
\lambda_{\min}(Q_1)
\le \frac{4e^2\delta^2C_0^2}{2+4(1-2\delta)^2}
\le\frac43 C_0^2e^2\delta^2.                           \tag{4c}
\]

These unit vectors can be embedded in every fixed \(d\ge2\); multiplying
them by \(\sqrt d\) gives the model's exact input normalization. Let
\(\Lambda_1(e,\delta;d)\) denote the infimum of \(\lambda_{\min}(Q_1)\)
over all strictly admissible triples in that dimension for
\(\phi(z)=(1-e)z+e\arctan z\). Combining (2) and (4c) gives, for every
\(d\ge2\), \(0<e\le1/2\), and \(0<\delta\le1/4\),

\[
\frac{b_3^2}{3}e^2\delta^2
\le\Lambda_1(e,\delta;d)
\le\frac43 C_0^2e^2\delta^2.                           \tag{4d}
\]

The constants are absolute and independent of dimension, labels, \(e\),
and \(\delta\). This is the precise worst-case
\(\Theta(e^2\delta^2)\) initialization statement. The kernel vector used
in its Rayleigh quotient need not be a binary-label vector; the claim is
about the least eigenvalue, not every binary-label projection of the Gram.
It yields no all-time training, flow-existence, or cutoff sharpness claim.

## 4. Backward positivity and bottom-layer motion

Use the exact initialization notation

\[
D_i^\ell=\phi'(Z_i^\ell),\quad
\beta_i^3=HD_i^3,\quad q_i^2=B_0^*\beta_i^3,
\quad\beta_i^2=D_i^2q_i^2,
\quad q_i^1=A_0^*\beta_i^2,\quad\beta_i^1=D_i^1q_i^1,
\]

and \(S_\ell=(E[\beta_i^\ell\beta_j^\ell])_{ij}\).
By (3), \(Z^3\) is a nondegenerate Gaussian triple. If \(v^TS_3v=0\),
positive density and continuity imply the everywhere identity

\[
\left(\sum_i p_i\phi(z_i)\right)
\left(\sum_i v_i\phi'(z_i)\right)=0.
\]

The first factor has no open zero set, because each of its coordinate
derivatives is \(p_i\phi'(z_i)\ne0\). The second therefore vanishes
everywhere. Its derivative in coordinate \(i\) is
\(v_i\phi''(z_i)=0\). As \(\phi''\) is not identically zero, \(v_i=0\).
Hence \(S_3\succ0\).

Appendix C, Part V.I's exact transpose identities are

\[
q_i^2=\zeta_i^2+\sum_k T_{ik}h_k^2,\qquad
q_i^1=\zeta_i^1+\sum_k R_{ik}h_k^1,                    \tag{5}
\]

where \(T,R\) are deterministic derivative responses,
\(\operatorname{Cov}\zeta^2=S_3\), and
\(\operatorname{Cov}\zeta^1=S_2\). Each reverse group is independent
of all forward groups and roots. The covariances are the full second
moments of the corresponding reverse inputs. The deterministic responses
must not be discarded. Conditioning successively gives

\[
S_2\succeq a^2\lambda_{\min}(S_3)I_3\succ0,\qquad
\operatorname{Cov}(\beta^1\mid Z^1)
\succeq a^2\lambda_{\min}(S_2)I_3.                    \tag{6}
\]

Define the hidden directions exactly as in Appendix C, Part N,

\[
V^1=d^{-1}\sum_i p_i\beta_i^1x_i,\quad
V^2=\sum_i p_i\beta_i^2\otimes h_i^1,\quad
V^3=\sum_i p_i\beta_i^3\otimes h_i^2.
\]

Equations (2), (3), and (6) imply

\[
dE\|V^1\|^2\ge a^2\lambda_{\min}(S_2)\sum_i p_i^2>0,
\]

\[
\|V^\ell\|_{\rm HS}^2
=\operatorname{tr}(\operatorname{diag}(p)S_\ell
                   \operatorname{diag}(p)Q_{\ell-1})>0
\quad(\ell=2,3).
\]

For each sample,
\(U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1\) satisfies

\[
\|U_j^1\|^2\ge a^2\lambda_{\min}(S_2)p_j^2>0.          \tag{7}
\]

No rank assumption on the first Gaussian triple enters these inequalities.

## 5. A direct proof of every upper sample's initial motion

This is the new part of the argument. Set

\[
t_j=D_j^1U_j^1,\qquad
c_{ji}=p_i\{(Q_1)_{ij}+\Gamma_{ji}E[D_j^1D_i^1]\}.
\]

The explicit dependence in (5) gives
\(\partial_{\zeta_i^1}t_j=D_j^1\Gamma_{ji}p_iD_i^1\).
The initialized forward return rule therefore yields

\[
A_0t_j=\xi_{t_j}+\sum_i\beta_i^2\Gamma_{ji}p_iE[D_j^1D_i^1],
\]

and hence the exact forward linearization is

\[
U_j^2=V^2h_j^1+A_0t_j
=\xi_{t_j}+\sum_i c_{ji}\beta_i^2.                     \tag{8}
\]

The new source \(\xi_{t_j}\) belongs to the A-forward Gaussian group.
Regress it on that group's three initialized sources \(Z^2\). Its
independent Gaussian remainder has variance

\[
\sigma_{2,j}^2
=\inf_{b\in\mathbb R^3}\left\|t_j-\sum_i b_i h_i^1\right\|_2^2
\ge E\operatorname{Var}(t_j\mid Z^1)
\ge a^4\lambda_{\min}(S_2)p_j^2>0.                    \tag{9}
\]

The last inequality uses (6) and both factors \(D_j^1,D_i^1\ge a\).
The remainder is independent of \(Z^2\) and of the independent B-reverse
group \(\zeta^2\). Since \(\beta^2\) depends only on those old variables,
(8) has an uncancelled Gaussian component of variance \(\sigma_{2,j}^2\).
Thus \(U_j^2\ne0\) for every \(j\).

For the final layer put \(s_j=D_j^2U_j^2\). From (8),
\(\partial_{\zeta_i^2}s_j=D_j^2c_{ji}D_i^2\), since every A-forward
named source is a separate independent source group. The B-forward
return rule gives

\[
U_j^3=V^3h_j^2+B_0s_j
=\xi_{s_j}+
\sum_i\beta_i^3\{p_i(Q_2)_{ij}+c_{ji}E[D_j^2D_i^2]\}.   \tag{10}
\]

After regressing \(\xi_{s_j}\) on the initial B-forward sources \(Z^3\),
its independent Gaussian remainder has variance

\[
\begin{split}
\sigma_{3,j}^2
&=\inf_b\left\|s_j-\sum_i b_i h_i^2\right\|_2^2\\
&\ge E\operatorname{Var}(s_j\mid Z^2,\zeta^2)
=E[(D_j^2)^2]\sigma_{2,j}^2
\ge a^2\sigma_{2,j}^2>0.
\end{split}                                             \tag{11}
\]

Here (9)'s remainder is independent of \((Z^2,\zeta^2)\), and all the
features \(h_i^2\) are measurable with respect to that tuple. In (10),
\(\beta^3\) is a function of the initialized \(Z^3\) alone. The new
remainder cannot cancel it, proving \(U_j^3\ne0\). Finally the feature
directions \(D_j^\ell U_j^\ell\) are nonzero because \(D_j^\ell\ge a\).

### Why the extra source calls are legitimate

All initialization variables in (5), (8), and (10) are bounded smooth
multipliers times finite sums of Gaussian sources and linear-growth smooth
functions of Gaussian sources. They have every finite moment. The added
inputs \(t_j,s_j\) are not globally bounded-derivative maps of their named
sources, but this is resolved by the same finite-transcript truncation as
Appendix C, Part V.I: truncate every unbounded incoming Gaussian-linear factor with a
smooth clip, apply the fixed-program theorem, and then remove the clips in
the actual action answers using bounded operator norms. The gate and its
derivatives are bounded; the factors appearing in the displayed source
derivatives either are bounded or have a fixed integrable Gaussian-linear
envelope. Dominated convergence therefore passes those response coefficients.
Source Gram convergence and continuous positive-semidefinite square roots
give the joint Gaussian-source limits. This uses finitely many calls only.

One can prove the needed positive innovation without the derivative
formula. Condition the finite initialized matrix A on all previous calls
\(AV=Y\) and \(A^TU=Q\), where the columns of V are the three \(h_i^1\)
and the columns of U are the three \(\beta_i^2\). For the next input
\(t_j\), exact Gaussian conditioning gives an independent new noise term

\[
\|(I-P_V)t_j\|_n\,P_{U^\perp}g_n,
\]

besides transcript-measurable terms. The expected normalized squared
length removed by \(P_U\) is \(\operatorname{rank}U/n\le3/n\).
The residual input norm converges to the positive quantity in (9), because
\(Q_1\succ0\) and all required contractions have fixed-transcript limits.
Therefore the limiting new scalar noise is an independent normal with
strictly positive variance. The B call with input \(s_j\) gives (11) by
the identical argument, now using \(Q_2\succ0\). This also verifies that
reuse of the same matrices cannot silently remove the innovations.

## 6. Physical acceleration and kernel variation need no scalar clock

On any canonical strong solution with the trajectory chain rule,
\(C(0)=0\), \(r(0)=-y\), and \(\dot C(0)=3H\). Thus
\(b_i^\ell(t)=3t\beta_i^\ell+o_{L^2}(t)\) and

\[
\theta_h(t)=\theta_h(0)+\frac92t^2V+o_{\rm raw}(t^2),
\qquad z_j^\ell(t)=Z_j^\ell+\frac92t^2U_j^\ell+o_{L^2}(t^2).
\]

The derivatives of the vector fields, obtained by the same backward
multiplier limits, give the actual right second derivatives
\(9V\), \(9U_j^\ell\), and \(9D_j^\ell U_j^\ell\), respectively.
All are nonzero by the preceding sections. The initial hidden first
derivatives are zero, as dictated by the population-zero readout.

Let \(J\) be the hidden directional linearization of
\(H(\theta_h)=\sum_i p_i h_i^3(\theta_h)\). Adjunction gives
\(V=J^*H\). Consequently

\[
p^TK^4(t)p=\|H(t)\|^2
=\|H\|^2+9t^2\|V\|_{\rm hidden}^2+o(t^2),
\]

while the projected sum of the three hidden kernel blocks is
\(9t^2\|V\|_{\rm hidden}^2+o(t^2)\). Therefore

\[
p^TK(t)p=p^TK(0)p+18t^2\|V\|_{\rm hidden}^2+o(t^2).    \tag{12}
\]

Neither equal predictions nor a feature-time reparameterization was used.
If readout acceleration is also required,
\(\ddot C(0)=-\sum_i(Q_3y)_i h_i^3\ne0\), since \(Q_3\succ0\).

## 7. Remaining analytic bridge

At initialization every scalar preactivation is a centered Gaussian of
positive variance, so its arctangent regression error is positive. For the
convex mixture with \(a\ge1/2\), the three initial standard deviations lie
between \(1/4\) and \(1\). Compactness and continuity give a uniform
strictly positive initial regression gap; continuity in \(L^2\) preserves
it for a sufficiently short interval along any regular solution.
This does not prove a gap at every later physical time.

The complete requested theorem still requires a single positive choice
\(e_\delta\), independent of physical horizon and of the potentially
singular Gram, together with all of the following:

1. A global canonical uncut strong flow and source-tail control sufficient
   to remove backward caps on every compact physical interval.
2. Uniqueness against all bounded-primal strong competitors and unique
   continuation from reached states.
3. A mechanism preventing the sample activation laws from losing their
   affine-regression gap over the whole physical trajectory.
4. The finite-width GF/raw-GD, velocity, path, kernel, and generated-probe
   identifications through those cap-independent reference estimates.

The existing fixed-program and compact-reference limit machinery can be
used once the required reference and tail estimates are supplied. It does
not supply them merely from the positive initial Gram (2).

Two exact diagnostics locate the failure of a direct two-input transplant:

* A generic three-input folded Gram has no transitive symmetry, so a single
  scalar residual and its exact one-dimensional time conversion are absent.
* Even a symmetric equilateral triple has zero affine signal. Its nonlinear
  initial projected kernel is positive but can be of order \(e^2\), whereas
  the affine perturbation bounds require a bounded reference clock independent
  of \(e\). An \(O(e^{-2})\) clock and growing reference bounds cannot be
  inserted into the affine small-\(e\) threshold without a new estimate.

A direct nonlinear source/continuation theorem valid on arbitrary bounded
physical intervals, plus a trained-law nondegeneracy mechanism, would bridge
these gaps. Alternatively a nonlinear reference that retains the cubic
signal in singular directions could replace the affine reference, but
its uniform source estimates and nonaffinity control must be proved.
The present note gives no counterexample to those possible conclusions.


# A conditional continuation criterion for three inputs

**Scope and conclusion.** This note concerns the canonical three-hidden-layer population raw GF with three unit-RMS inputs and the exact odd activation
\[
\phi(z)=az+e\arctan z,\qquad a=1-e,\qquad 0<e<1/4.
\]
It uses the model and local machinery in this report, especially Appendix C, Parts F/R/V; the offset activation appearing in the reproduced Appendix C is replaced throughout by the displayed odd activation. No affine-training assumption, Gram invertibility, global generic-three-input existence, or numerical evidence is used.

The focused route is to retain the decay of arctangent curvature in the nonlinear source equations. It does **not** presently close from the finite-horizon raw energy bound. The precise obstruction is the multiplier \(Q g'(Z)\) in a response equation, where \(g(z)=(1+z^2)^{-1}\): large incoming \(Q\) need not occur at large \(Z\). Below is an explicit raw-state obstruction to an ambient estimate, together with a complete conditional lemma showing that **exponential**, rather than Gaussian, reference tails would already suffice. Neither statement proves that the obstruction occurs along the canonical reached trajectory.

## 1. Exactly what raw energy supplies

On any existing strong uncut solution,
\[
L(t)+\int_0^t\|\dot\theta(s)\|_{\rm raw}^2\,ds=L(0),
\qquad
\|\theta(t)-\theta(0)\|_{\rm raw}\le\sqrt{tL(0)}.
\]
At canonical initialization \(L(0)=3/2\). Consequently, on each finite physical horizon before a possible endpoint, all forward fields and all incoming fields
\[
\mathscr Q=\{C,q_i^2=B^*[C\phi'(z_i^3)],
q_i^1=A^*[\phi'(z_i^2)q_i^2]:1\le i\le3\}
\]
have bounded \(L^2\) norms; the initialized actions are bounded and learned increments are Hilbert–Schmidt. The controls satisfy \(\|r(t)\|_1\le3\), so physical-time source equations have a finite controlled clock on a fixed horizon.

A small additional endpoint conclusion is valid: if a strong solution exists on \([0,T_*)\), \(T_*<\infty\), raw energy makes its state strongly Cauchy as \(t\uparrow T_*\). It therefore has an endpoint \(\theta_*\) in the affine raw Hilbert space. The uncut raw field is continuous there: forward maps are locally Lipschitz, backward multiplication is strongly continuous by F.5, and rank-one products are continuous. Thus \(F(\theta(t))\to F(\theta_*)\), and the solution extends as a \(C^1\) curve to the **closed** interval \([0,T_*]\). This does not construct a solution beyond \(T_*\), nor prove uniqueness from \(\theta_*\). Local existence for a merely continuous vector field in an infinite-dimensional Hilbert space cannot be inserted here.

## 2. The exact nonclosed response term

At a gate \(\delta=\phi'(Z)Q\), with all deterministic source coefficients and covariances frozen as required by F/R,
\[
\partial_\eta\delta
 =\phi'(Z)\partial_\eta Q+e g'(Z)Q\,\partial_\eta Z,
\qquad g'(z)=-\frac{2z}{(1+z^2)^2}.                 \tag{E.1}
\]
This is the uncut version of R.44/R.49. If \(J=\partial_\eta Z\), the backward response coefficient in R.12 contains
\[
                      e E[g'(Z)QJ].                         \tag{E.2}
\]
The current source derivative has \(J=1\), so its curvature contribution is bounded by \(e\|g'\|_\infty\|Q\|_2\). This verifies that the immediate transpose return alone is not the obstruction. Propagating a past response requires (E.1) repeatedly. Cauchy–Schwarz bounds (E.2) using \(\|Q\|_2\|J\|_2\), but the next \(L^2\) response estimate requires
\[
\|g'(Z)QJ\|_2^2
 =4E\left[\frac{Z^2Q^2J^2}{(1+Z^2)^4}\right].       \tag{E.3}
\]
Neither bounded \(\|Q\|_2\) nor bounded \(\|J\|_2\) controls (E.3). A direct Hölder estimate instead asks for \(L^4\) control of both factors, and iterating generates higher moments. Retaining curvature decay simply replaces this by a joint weighted-moment obligation; no available raw-energy identity supplies that obligation.

For the simplest algebraic witness take a uniform \(U\in(0,1)\), \(Z=1\), and \(Q=J=U^{-1/3}\). Then \(Q,J\in L^2\), but \(g'(Z)QJ\notin L^2\). The same obstruction is visible in the pathwise response envelope from R.50: knowing \(E\int_0^T Q(t)^2dt<\infty\) gives \(\int_0^T|Q(t)|dt<\infty\) almost surely, but gives no integrability of
\[
               \exp\left(c e\int_0^T|Q(t)|dt\right).
\]
Such exponential integrability is exactly the step used to take expectations of the response envelope. This is an obstruction to this estimate, not a demonstrated law of an actual canonical response.

The circularity remains even though finite-program source variances are bounded by primal norms. Under already bounded response rows, R.38–R.41 give Gaussian-scale coordinate moments. The raw variance bound does not first bound those rows: their past terms contain (E.2). The finite-cap probe argument in V.3 does bound them, but its raw stability constant depends on the cap through \(eR\).

## 3. Curvature decay does not repair the ambient raw-ball estimate

The preceding separation of \(Z\) and \(Q\) can occur inside the actual affine raw state space, with its canonical initialized actions; arbitrary alternative initialized operators are unnecessary.

Fix a nonzero layer-two feature \(h\in H_2\), for example the initialized feature of one sample. Set
\[
 B=B_0+(\mathbf1-B_0h)\otimes h/\|h\|_2^2.
\]
Then \(B-B_0\) is Hilbert–Schmidt and \(Bh=\mathbf1\). The canonical layer-three space contains a nondegenerate Gaussian initial forward answer, hence a uniform variable \(U\) obtained by its Gaussian distribution function. Choose the permissible raw readout \(C=U^{-1/3}\in H_3\). At this state the selected top preactivation is identically one, whereas its incoming field is \(C\), with polynomial tails. All primal raw quantities are finite, and
\[
                        C\phi''(1)=-(e/2)C
\]
is unbounded. Let \(E_n=\{C>n\}\), fix \(t\ne0\) small with \(\phi'(1+t)\ne\phi'(1)\), and perturb only
\[
                 B_n-B=t\mathbf1_{E_n}\otimes h/\|h\|_2^2.
\]
These perturbations converge to zero in Hilbert–Schmidt norm. Nevertheless, the ratio of the selected top-backward-field change to the raw perturbation satisfies
\[
\frac{\|C[\phi'(1+t\mathbf1_{E_n})-\phi'(1)]\|_2}
 {\|B_n-B\|_{\rm HS}}
\ge n\|h\|_2\frac{|\phi'(1+t)-\phi'(1)|}{|t|}\longrightarrow\infty.
\]
Thus even this backward observation is not locally Lipschitz at every bounded-primal raw state. On the sets causing failure, the preactivation stays at the fixed value one. This construction is **not** a reached-state counterexample and does not disprove canonical global continuation. It does rule out deriving the needed estimate from an ambient raw bound alone without additional canonical structure.

## 4. Conditional lemma: exponential reference tails suffice on any finite horizon

**Lemma E.1.** Fix \(0<e<1/4\) and \(0<T<\infty\). Suppose the canonical finite-cap reference flows \(\theta_R\) exist on \([0,T]\), share initialization and initialized actions, and have a common primal bound. The incoming fields at a cap state are
\[
 q_i^{2,R}=B_R^*D_R(z_i^{3,R},C_R),\qquad
 q_i^{1,R}=A_R^*D_R(z_i^{2,R},q_i^{2,R}),\qquad
 \mathscr Q_R=\{C_R,q_i^{2,R},q_i^{1,R}:1\le i\le3\}.
\]
Assume that the following bound holds for some finite \(A\ge1,c>0\), independent of \(R\):
\[
\sup_{R,t\le T,Q\in\mathscr Q_R(t)}
     \|Q\mathbf1_{\{|Q|>u\}}\|_2\le A \exp(-cu)
                       \qquad(u\ge1).                       \tag{E.4}
\]
Then these references converge uniformly in raw state and raw direction to a strong uncut flow on \([0,T]\). That flow is unique against every bounded-primal strong uncut competitor with the same initialization. The argument imposes no smallness relation between \(e\) and \(T\). Consistent assumptions for all finite horizons yield a global flow and unique continuation from its reached states.

**Proof.** For any two gate caps \(R',R\ge M\ge1\), including an infinite cap, splitting according to \(|\bar q|\le M\) gives
\[
|D_{R'}(z,q)-D_R(\bar z,\bar q)|
\le |q-\bar q|+C eM|z-\bar z|
                  +4e|\bar q|\mathbf1_{\{|\bar q|>M\}}.     \tag{E.5}
\]
Indeed both clips equal the identity on the first set; on the second, their absolute values are at most \(|\bar q|\), and \(g\) is bounded. The map in its incoming variable is 1-Lipschitz because \(a+e=1\) and the clips have derivative bounded by one.

Propagating (E.5) through the three backward stages, with V.8–V.9 for the forward maps and rank-one velocities, gives for the raw sum distance \(d(t)=\|\theta_{R'}(t)-\theta_R(t)\|_{\rm sum,raw}\)
\[
D^+d(t)\le K\big[(1+eM)d(t)+eA \exp(-cM)\big],
              \qquad 1\le M\le\min(R,R').                   \tag{E.6}
\]
Only the reference tails occur. The same inequality holds against an uncut bounded-primal competitor; its primal bound changes \(K\).

Let \(R\) denote the smaller finite cap, set \(\varepsilon_R=A\exp(-cR)\), and put \(u=d+\varepsilon_R\). While \(u\le A\exp(-c)\), choose the admissible moving threshold
\[
                         M=c^{-1}\log(A/u).
\]
Since \(u\ge\varepsilon_R\), this threshold is at most \(R\). Equation (E.6) yields, after increasing a constant depending only on the stated bounds,
\[
                 D^+u\le K_1u\log(\exp(1)A/u).
\]
With identical initialization, \(u(0)=\varepsilon_R\). Integration, or setting \(v=\log(\exp(1)A/u)\), gives
\[
\sup_{t\le T}d(t)
\le \exp(1)A\exp\left[-(1+cR)\exp(-K_1T)\right].             \tag{E.7}
\]
For sufficiently large \(R\), this estimate remains inside the stipulated threshold range on the whole interval, justifying the stopping argument. It tends to zero for every fixed \(T\). This is the Osgood estimate for the modulus \(s\log(1/s)\).

To obtain convergence of directions, use the field version of (E.6) with a fixed threshold \(M=\alpha R\), where \(0<\alpha<\exp(-K_1T)\). The distance contribution is a polynomial factor times the decaying bound (E.7), while the tail term is \(A\exp(-c\alpha R)\). Both vanish uniformly. Completeness gives uniform limits of states and directions; their integral identity proves a strong \(C^1\) path. Applying the same field estimate with the uncut gate identifies its direction. Comparing any strong uncut competitor to these references proves uniqueness.

At a reached time \(t_0\), the discrepancy from the cap reference is already exponentially small in \(R\) by (E.7). The identical Osgood calculation starting with this exponentially small discrepancy still tends to zero on every finite subsequent interval. This proves the asserted continuation uniqueness. ∎

Condition (E.4) follows, for example, from a uniform \(\|Q\|_p\le Kp\) bound for all \(p\ge2\), or a uniform positive exponential moment. Ordinary finite \(L^p\) bounds are insufficient for this particular argument. The constants in (E.4) may depend on \(T\); \(e\) need not.

**Remaining obligation.** Prove at least the exponential-tail property (E.4), or another Osgood modulus, for the canonical references without cap-dependent constants. The curvature-weighted product (E.3) is the concrete nonclosed term in the tested route. Its control would need a reached-state correlation/response estimate beyond finite-horizon raw energy. No global three-input source-regularity claim is established here.


# Appendix C. Full foundational statement and proofs

The following complete manuscript supplies the specialized Gaussian, response, cap-transfer, velocity and initialization proofs used above. Its own main theorem concerns a different activation and is not asserted for the odd mixture. The main text explicitly verifies the specialization of its intermediate lemmas. Its model and equation prefixes M, F, R, G, V and N are local to this appendix. 

# Global limits for three separated inputs in a three-hidden-layer network

## Part M. Model, notation, and theorem

### M.1. Finite network and physical training

All vector spaces in this manuscript are real. Fix an integer \(d\ge1\),
three deterministic vectors \(x_1,x_2,x_3\in\mathbb R^d\), and labels
\(y_1,y_2,y_3\in\{-1,1\}\). The input normalization and separation are
\[
 \|x_i\|_{\mathbb R^d}^2=d,\qquad
 \Gamma_{ij}=d^{-1}x_i^Tx_j,\qquad
 \Gamma_{ij}\le1-\delta\quad(i\ne j),\qquad \delta>0.       \tag{M.1}
\]
Thus \(\Gamma\) is positive semidefinite with unit diagonal. Its rank
may be less than three. A triple satisfying (M.1) exists only if
\(\delta\le3/2\): the squared norm of
\(\sum_i x_i/\sqrt d\) is nonnegative and at most \(9-6\delta\).
All statements quantify only over geometries realizable in the
specified dimension.

We will choose two constants \(a=a_\delta\ge1\) and \(e_\delta>0\).
For any fixed \(e\in(0,e_\delta]\), use the same activation
\[
                   \phi(z)=a(1+z)+e\arctan z                 \tag{M.2}
\]
in all three hidden layers. The constants \(a,e\) never depend on
width or training time. They may depend on the required separation.

For width \(n\), the raw parameters are
\[
 W^1\in\mathbb R^{n\times d},\quad W^2,W^3\in\mathbb R^{n\times n},
 \quad C\in\mathbb R^n.
\]
All initialized entries are mutually independent, with
\[
 W^1_{jk}(0)\sim N(0,d^{-1}),\quad
 W^2_{jk}(0),W^3_{jk}(0)\sim N(0,n^{-1}),\quad
 C_j(0)\sim N(0,n^{-2}).                                   \tag{M.3}
\]
The same initialization is used to couple the two training algorithms
at each width. No assumption about independence between different
widths is needed. Define
\(\langle u,v\rangle_n=n^{-1}u^Tv\) and
\(\|u\|_n=\langle u,u\rangle_n^{1/2}\).
For each sample \(i\),
\[
 \begin{split}
 z_i^1&=W^1x_i,\qquad h_i^1=\phi(z_i^1),\\
 z_i^2&=W^2h_i^1,\qquad h_i^2=\phi(z_i^2),\\
 z_i^3&=W^3h_i^2,\qquad h_i^3=\phi(z_i^3),\\
 f_i&=\langle C,h_i^3\rangle_n,\qquad r_i=f_i-y_i,\qquad
 L=\tfrac12\sum_{i=1}^3r_i^2.
 \end{split}                                                \tag{M.4}
\]
An activation or product of two vector fields is coordinatewise.
Residual-free backward vectors are
\[
 b_i^3=C\phi'(z_i^3),\quad
 b_i^2=\phi'(z_i^2)(W^3)^Tb_i^3,\quad
 b_i^1=\phi'(z_i^1)(W^2)^Tb_i^2.                             \tag{M.5}
\]

The raw Hilbert metric on parameter increments is
\[
 \|\Delta\theta\|_{{\rm raw},n}^2
 =\frac dn\|\Delta W^1\|_F^2+
   \|\Delta W^2\|_F^2+\|\Delta W^3\|_F^2+\|\Delta C\|_n^2.
                                                               \tag{M.6}
\]
The physical gradient flow of \(L\) in this metric is
\[
 \begin{split}
 \dot W^1&=-d^{-1}\sum_i r_i b_i^1x_i^T,\\
 \dot W^\ell&=-n^{-1}\sum_i r_i b_i^\ell(h_i^{\ell-1})^T,
                     \qquad\ell=2,3,\\
 \dot C&=-\sum_i r_i h_i^3 .
 \end{split}                                                \tag{M.7}
\]
For example, the Euclidean first-block derivative has factor \(1/n\);
the inverse first-block metric multiplies it by \(n/d\), giving
\(1/d\). The readout inverse metric multiplies by \(n\), cancelling
the \(1/n\) in its Euclidean derivative. These calculations verify
all factors in (M.7).

Raw gradient descent is the simultaneous explicit Euler update
\(\theta_{k+1}=\theta_k+\eta_n F(\theta_k)\) for precisely (M.7),
where \(\eta_n=n^{-2}\). It uses the actual residuals at that node.
Interpolate the raw parameters linearly at physical times \(k\eta_n\).
All hidden fields at intermediate times are recomputed by (M.4);
hidden fields themselves are not linearly interpolated. Their
velocities are derivatives of those recomputed fields. At a mesh
node take the right derivative; at the endpoint of a closed
observation interval take the left derivative. The finite random
readout in (M.3) is never replaced by zero.

At any fixed width, GF has a global solution. The finite-dimensional
field is smooth and locally Lipschitz. Its energy identity gives
\(\int_0^T\|\dot\theta\|_{{\rm raw},n}^2\le L(0)\).
Hence its displacement before a finite endpoint is at most
\(\sqrt{TL(0)}\), and its increments near that endpoint are strongly
Cauchy by the same Cauchy--Schwarz bound. Local existence from the
finite endpoint extends the solution. GD is defined at every
finite step because its update is a finite composition of the
everywhere-defined smooth maps in (M.4)--(M.7).

### M.2. Population state and the meaning of its initialization

Part F constructs three probability spaces
\((\Omega_\ell,\mu_\ell)\), with \(H_\ell=L^2(\mu_\ell)\), from
the limiting same-layer laws of fixed finite Gaussian calculations.
They are separate neuron spaces: an element of \(H_1\) is never
multiplied coordinatewise by an element of \(H_2\) or \(H_3\).
The constructed initialized actions are
\[
 A_0:H_1\longrightarrow H_2,\qquad
 B_0:H_2\longrightarrow H_3 ,
 \qquad \|A_0\|_{\rm op},\|B_0\|_{\rm op}\le10,              \tag{M.8}
\]
with their actual Hilbert adjoints. The first weight field satisfies
\[
 w_0\in L^2(\Omega_1;\mathbb R^d),\qquad
 w_0\sim N(0,I_d/d),\qquad C_0=0.
                                                               \tag{M.9}
\]
The bound (M.8) and laws (M.9) are consequences of the finite
initialization and the construction in Part F. Arbitrary bounded
operators with these norms are not alternative initializations
for this theorem.

The affine population parameter space is
\[
 \mathcal X=
 L^2(\Omega_1;\mathbb R^d)
 \times\big(A_0+\mathcal S_2(H_1,H_2)\big)
 \times\big(B_0+\mathcal S_2(H_2,H_3)\big)\times H_3,          \tag{M.10}
\]
where \(\mathcal S_2\) denotes Hilbert--Schmidt operators.
Its increment norm is
\[
 \|\Delta\theta\|_{\rm raw}^2
 =d\|\Delta w\|_2^2+\|\Delta A\|_{\rm HS}^2
                    +\|\Delta B\|_{\rm HS}^2+\|\Delta C\|_2^2.
                                                               \tag{M.11}
\]
The equivalent sum norm replaces the square root of the sum
of four squares by the sum of their square roots. Estimates will
state when they use this sum norm. For \(u\in H_j,v\in H_i\),
\(u\otimes v:H_i\to H_j\) means \(q\mapsto u\langle v,q\rangle_i\).
Its Hilbert--Schmidt norm is \(\|u\|_j\|v\|_i\).

The population forward and backward fields are (M.4)--(M.5)
with \(W^1x_i\) replaced by \(w\cdot x_i\), \(W^2,W^3\)
by \(A,B\), transposes by their actual adjoints, and
normalized sums by expectations in the specified layer.
The evolution is
\[
 \dot w=-d^{-1}\sum_i r_i b_i^1x_i,\qquad
 \dot A=-\sum_i r_i b_i^2\otimes h_i^1,\qquad
 \dot B=-\sum_i r_i b_i^3\otimes h_i^2,\qquad
 \dot C=-\sum_i r_i h_i^3.                                 \tag{M.12}
\]
A strong \(C^1\) solution means a \(C^1\) path in the affine
Hilbert space (M.10), satisfying these identities there.
“Bounded primal quantities on compact intervals” means bounded
\(\sqrt d\|w\|_2,\|A\|_{\rm op},\|B\|_{\rm op},\|C\|_2\)
on each such interval. Initialization has
\(\sqrt d\|w_0\|_2=\sqrt d\); the selection of activation parameters
will use only the three normalized projections and raw
displacements, not a dimension-free bound on this full norm.
Components of \(w\) perpendicular to the span of the inputs
stay equal to their initialized values by (M.12).

### M.3. Precise observables

For probability measures with finite second moments on a separable
normed space \(E\), write
\[
 \mathcal W_2(\nu,\widetilde\nu)^2
 =\inf_{\pi\in\Pi(\nu,\widetilde\nu)}
                   \int\|u-v\|_E^2\,d\pi(u,v).
                                                               \tag{M.13}
\]
Here \(\Pi\) is the set of couplings with the specified marginals.
The space \(C([0,T];\mathbb R^k)\) is equipped with the supremum
of its Euclidean norm.

For each layer, let
\[
 X^\ell(t)=(z_1^\ell,h_1^\ell,z_2^\ell,h_2^\ell,
                              z_3^\ell,h_3^\ell)(t)\in\mathbb R^6,
 \qquad
 Y^\ell(t)=(X^\ell(t),\dot X^\ell(t))\in\mathbb R^{12}.
                                                               \tag{M.14}
\]
At width \(n\), the associated empirical law is the average of
the \(n\) Dirac masses at its neuron-row values. For paths, it is
the average of the \(n\) Dirac masses at the entire corresponding
continuous row paths. The population law uses \(\mu_\ell\).
Part V constructs continuous versions and proves their finite
second moments in the path norm.

The four raw kernel blocks are
\[
 \begin{split}
 K^1_{ij}&=\Gamma_{ij}\langle b_i^1,b_j^1\rangle_1,\\
 K^2_{ij}&=\langle b_i^2,b_j^2\rangle_2
                             \langle h_i^1,h_j^1\rangle_1,\\
 K^3_{ij}&=\langle b_i^3,b_j^3\rangle_3
                             \langle h_i^2,h_j^2\rangle_2,\\
 K^4_{ij}&=\langle h_i^3,h_j^3\rangle_3 .
 \end{split}                                                \tag{M.15}
\]
Finite kernels use the normalized finite inner products.
They always use the true backward fields (M.5). When auxiliary
clipped flows are introduced, their update fields are different
objects; Part V proves the needed true-kernel observations
explicitly.

An additional generated probe is a fixed finite, layer-typed
expression formed from the first-row Gaussian roots, constants,
fields at finitely many observation times, deterministic linear
combinations, continuously differentiable coordinate maps with
bounded first derivatives, inner-product contractions, and
applications of any of \(A_0,B_0,A(t),B(t)\) or their adjoints
where domains and codomains match. Each contraction is performed
inside one layer. Its finite version uses exactly the corresponding
finite matrices and their transposes. A probe expression is fixed
before the width limit; its instruction count does not grow
with width. Both orientations of every action are included in
this definition. Named true-backward and velocity observations
are covered separately by the product-truncation proofs in Part V.

### M.4. The theorem

**Theorem M.1.** For each \(0<\delta\le3/2\), there are finite
constants \(a_\delta\ge1\) and \(e_\delta>0\) depending only on
\(\delta\), such that, for every fixed \(e\in(0,e_\delta]\),
every \(d,x_1,x_2,x_3,y_1,y_2,y_3\) satisfying (M.1), and the
network (M.2)--(M.7), the following hold.

1. There is one global autonomous strong \(C^1\) population
   solution (M.12). On the canonical action spaces it is unique
   among strong solutions with bounded primal quantities on
   compact intervals. Its continuation from every reached
   state is unique in that same class. It is the raw Hilbert
   gradient flow of \(L\).
2. For each deterministic \(T<\infty\), GF and raw GD converge
   jointly along the full width sequence in probability to
   that same solution in all the following senses:
   \[
   \sup_{t\le T}|f_{n,i}(t)-f_i(t)|\to0,\quad
   \sup_{t\le T}|L_n(t)-L(t)|\to0,\quad
   \sup_{t\le T}|K^\ell_{n,ij}(t)-K^\ell_{ij}(t)|\to0;
                                                               \tag{M.16}
   \]
   \[
   \mathcal W_2\big(\widehat{\operatorname{Law}}_n
        (X_n^\ell|_{[0,T]}),
          \operatorname{Law}(X^\ell|_{[0,T]})\big)\to0;           \tag{M.17}
   \]
   \[
   \sup_{t\le T}\mathcal W_2\big(
       \widehat{\operatorname{Law}}_n(Y_n^\ell(t)),
                       \operatorname{Law}(Y^\ell(t))\big)\to0.  \tag{M.18}
   \]
   At any fixed finite collection of times the full joint
   same-layer \(Y^\ell\) laws also converge in \(\mathcal W_2\).
   Their second moments and the integrals of each squared
   preactivation or feature speed converge. Every fixed finite
   same-layer tuple of generated probes has the corresponding
   empirical \(\mathcal W_2\) limit. No identification asserting
   operator-norm convergence of unrelated finite matrices
   across widths is intended.
3. There is a positive absolute constant \(\eta_*\), specified
   below, such that every sample and hidden layer obeys
   \[
    \inf_{t\ge0}\inf_{\alpha,\beta\in\mathbb R}
      E_\ell[\phi(z_i^\ell(t))-\alpha-\beta z_i^\ell(t)]^2
                                  \ge e^2\eta_*/4>0.           \tag{M.19}
   \]
   Every hidden population parameter block has nonzero
   initial second derivative in its raw norm. Every sample's
   preactivation and feature field in every hidden layer
   has nonzero initial second derivative in \(L^2\).
   With \(p=y/3\) and
   \(\kappa(t)=p^T(\sum_{\ell=1}^4K^\ell(t))p\), one has
   \[
      \kappa(t)=\kappa(0)+18t^2\|V\|_{\rm hidden}^2+o(t^2),
                   \qquad\|V\|_{\rm hidden}>0,                 \tag{M.20}
   \]
   where \(V\) is explicitly defined in Part N.

All probabilistic limits in this statement refer to each fixed
admissible dataset and fixed finite \(T\). Their constants may
depend on that dataset, \(d,e,T\). The activation selection
does not. This is global population existence together with
compact-time finite-width convergence; it makes no interchange
of infinite-time and infinite-width limits.

Here is an explicit selection rule. For \(G\sim N(0,1)\), put
\[
 \begin{split}
 \mathcal R(Z)&=\inf_{\alpha,\beta}E[\arctan Z-\alpha-\beta Z]^2,\\
 \eta_*&=\inf_{\sigma\ge1}\mathcal R(\sigma G),\qquad
 t_*=\min\{1/2,\sqrt{\eta_*}/[2(1+\pi)]\},\qquad
 \lambda=\delta^2/4,\\
 a_\delta&=\max\left\{2000/\sqrt\lambda,\,
                   (10^{12}/(\lambda^2t_*))^{1/4}\right\},\\
 S&=12/(\lambda a_\delta^6),\\
 e_\delta&=\tfrac12\min\{1,e_*(a_\delta,12,S),
                                      (10^{10}a_\delta)^{-1}\}.
 \end{split}                                                \tag{M.21}
\]
We write \(e_*(a,B,S)=\epsilon_*(a,B,S)\), where (R.90) defines the latter.
Part G proves \(\eta_*>0\); Part R constructs the positive
number \(e_*(a,B,S)\) by a finite chain of estimates.
Consequently (M.21) is a genuine choice from separation alone,
not a pointwise minimum over unknown trained trajectories.

The proof proceeds by constructing the fixed finite Gaussian
calculations and their common action spaces in Part F; proving
the controlled response estimates in Part R; giving one bounded
total residual clock and removing the auxiliary caps in Part G;
proving the finite algorithm and observation limits in Part V;
and proving all initial-motion statements in Part N.

# Part F. Gaussian adaptive programs and the population parameter space

This chapter proves the finite-program and functional-analytic facts needed for a network with three hidden layers and three fixed samples. All widths in the two hidden-to-hidden matrices are the same. The activation is
\[
\phi(z)=a(1+z)+e\arctan z,\qquad a\ge1,\quad 0\le e\le1.
\tag{F.1}
\]
The assertions about finite programs below keep the program length, all numerical coefficients, and every clipping level fixed while width tends to infinity. They do not give estimates uniform in a growing number of steps or in the clipping level. Those estimates must be established separately before taking a time-continuum or unclipping limit.

The proof first establishes the exact conditional law of an adaptively queried Gaussian matrix, derives its response correction, and removes nonsingularity assumptions by perturbing query inputs. It then realizes a countable family of limiting programs on common probability spaces and extends the initialized matrix actions to bounded operators with genuine adjoints. Finally it proves the chain rule and differentiability of the scalar predictor in the raw parameter norm.

## 1. Finite programs and convergence of their empirical laws

There are three types of length-\(n\) vectors, one for each hidden layer. Operations combining coordinates may combine only vectors of the same type. Let
\[
A_n:\mathbb R^n_1\longrightarrow\mathbb R^n_2,
\qquad B_n:\mathbb R^n_2\longrightarrow\mathbb R^n_3
\]
be independent matrices whose entries are independent \(N(0,1/n)\). Their transposes are reused as the reverse actions of these same matrices.

Each layer may have a fixed finite tuple of root vectors. Its coordinate tuples are independent and identically distributed, have finite second moment, and are independent of all matrices. Tuples in different layers are independent. Constants are also allowed. In the network application, the first-layer root is a Gaussian vector \(w_0\in\mathbb R^d\) with covariance \(I_d/d\); the three root preactivations are \(x_i^T w_0\). Additional independent Gaussian roots may be added to any layer when a proof requires probes or regularization.

A deterministic-coefficient program is a fixed finite ordered list of instructions of the following forms:

1. apply a fixed \(C^1\) function \(F:\mathbb R^m\to\mathbb R\) with bounded first partial derivatives, coordinate by coordinate, to previously available vectors of one layer;
2. multiply a previously available vector by \(A_n,B_n,A_n^T\), or \(B_n^T\), with the appropriate types;
3. form a fixed real linear combination of previous same-layer vectors.

The first condition implies a global Lipschitz bound and at most linear growth for each coordinate instruction. The bound may depend on that instruction. Root tuples themselves need not be generated by such functions.

Write
\[
\langle u,v\rangle_n=\frac1n\sum_{\alpha=1}^n u_\alpha v_\alpha,
\qquad \|u\|_n^2=\langle u,u\rangle_n.
\]
For same-layer nodes \(v^1_n,\ldots,v^m_n\), their empirical law is
\[
\widehat\mu_n=\frac1n\sum_{\alpha=1}^n
 \delta_{(v^1_{n,\alpha},\ldots,v^m_{n,\alpha})}.
\]
Here \(\mathcal W_2\) uses the Euclidean distance on \(\mathbb R^m\).

**Theorem F.1 (fixed finite Gaussian program).** Every such program has deterministic joint limiting laws of all its same-layer node tuples, and
\[
\mathcal W_2(\widehat\mu_n,\mu)\longrightarrow0
\quad\hbox{in probability}
\tag{F.2}
\]
along the full width sequence. In particular every within-layer pairwise contraction converges to the corresponding limiting second moment. The scalar laws are given by the source rule in Section 4. Query Grams may be singular. Finite collections of programs sharing the same matrices and roots converge jointly by applying the assertion to their finite union.

We prove this theorem in Sections 2–5. The following elementary facts make explicit the probabilistic mode of convergence used in its proof.

If \(X_\alpha\) are iid and \(E|X_1|<\infty\), their averages converge in probability to their expectation: truncate \(X_\alpha\) at level \(M\), use the variance bound \(O(M^2/n)\) for the bounded variables, and bound the mean absolute truncation error by \(E[|X_1|1_{|X_1|>M}]\). First send \(n\) to infinity and then \(M\) to infinity. This proves the required initial weak convergence and second-moment convergence of root empirical laws.

For probability measures on a finite-dimensional Euclidean space, weak convergence together with convergence of second moments implies \(\mathcal W_2\) convergence. One direct proof is as follows. Continuous truncations of \(|x|^2\) show that the second moments outside sufficiently large balls are uniformly small. Inside a ball partition space into finitely many sets of diameter at most \(\eta\), choosing boundaries of zero limiting measure. Weak convergence makes their masses converge. Couple the common mass within each partition cell, at cost at most \(\eta^2\), and couple the remaining masses arbitrarily. The unmatched mass inside the ball vanishes; its cost is bounded by the squared diameter of the ball times that mass. The tails have arbitrarily small cost by \(|x-y|^2\le2|x|^2+2|y|^2\). Sending the ball radius and then the partition resolution to their limits proves the claim. A countable family of bounded Lipschitz tests determines weak convergence, by approximation on compact balls and tightness. For random measures the same argument applies in probability, or along an almost surely convergent subsubsequence of every subsequence.

Two arrays on the same neuron indices satisfy
\[
\mathcal W_2^2(\widehat\mu_n,\widehat\nu_n)
\le\frac1n\sum_\alpha |X_{n,\alpha}-Y_{n,\alpha}|^2,
\tag{F.3}
\]
using the coupling that pairs equal indices. These facts require no assertion that trained coordinates are independent.

## 2. An explicit Gaussian operator norm bound

**Lemma F.2.** For an \(n\times n\) matrix \(W_n\) with independent \(N(0,1/n)\) entries,
\[
\Pr(\|W_n\|_{\rm op}>10)
\le 2\,9^{2n}e^{-100n/8}\longrightarrow0.
\tag{F.4}
\]

**Proof.** A maximal \(1/4\)-separated subset \(\mathcal N\) of the Euclidean unit sphere is a \(1/4\)-net. Balls of radius \(1/8\) about its points are disjoint and lie in the ball of radius \(9/8\), so volume comparison gives \(|\mathcal N|\le9^n\). For unit \(u,v\), choose \(u_0,v_0\in\mathcal N\) within \(1/4\). Then
\[
|u^TW_nv-u_0^TW_nv_0|
\le\tfrac12\|W_n\|_{\rm op}.
\]
Taking the supremum gives \(\|W_n\|_{\rm op}\le2\max_{u_0,v_0\in\mathcal N}|u_0^TW_nv_0|\). For a fixed pair the displayed scalar is \(N(0,1/n)\). Its exponential moment is \(Ee^{t u_0^TW_nv_0}=e^{t^2/(2n)}\); Markov's inequality optimized at \(t=ns\) yields \(\Pr(|u_0^TW_nv_0|>s)\le2e^{-ns^2/2}\). A union bound at \(s=5\) proves (F.4). The exponent is negative since \(2\log9<12.5\). The same bound applies to transposes, and a finite union bound handles all matrices. ∎

The same argument for a threshold \(t\ge10\) gives
\[
\Pr(\|W_n\|_{\rm op}>t)
\le2\exp\{n(2\log9-t^2/8)\}
\le2e^{-nt^2/16}\le2e^{-t^2/16}.
\tag{F.4a}
\]
Consequently every fixed positive moment is bounded uniformly in width:
\[
\sup_{n\ge1}E\|W_n\|_{\rm op}^p
\le10^p+2p\int_{10}^\infty t^{p-1}e^{-t^2/16}\,dt<\infty.
\tag{F.4b}
\]
The integration formula follows by writing \(X^p=\int_0^Xpt^{p-1}dt\) for nonnegative \(X\) and interchanging nonnegative integrals. Hölder's inequality then gives uniform fixed-order moments for every fixed polynomial in finitely many such operator norms. For a standard Gaussian vector \(g_n\), Jensen's inequality also gives \(E\|g_n\|_n^p\le E|G|^p\) when \(p\ge2\).

A useful consequence identifies normalized traces without a concentration theorem for functions of matrix entries. Let \(T_n\) be any random real \(n\times n\) matrix independent of \(g_n\sim N(0,I_n)\), with \(\sup_nE\|T_n\|_{\rm op}^2<\infty\). Conditional on \(T_n\),
\[
E_g\langle g_n,T_ng_n\rangle_n=\frac1n\operatorname{tr}T_n,
\quad
\operatorname{Var}_g\langle g_n,T_ng_n\rangle_n
=\frac{2}{n^2}\left\|\frac{T_n+T_n^T}{2}\right\|_F^2
\le\frac{2}{n}\|T_n\|_{\rm op}^2.
\tag{F.4c}
\]
To verify the variance, replace \(T_n\) by its symmetric part, diagonalize it orthogonally, and use that the transformed Gaussian coordinates are independent with \(\operatorname{Var}(G^2)=2\). Therefore the difference between this probe and the normalized trace tends to zero in \(L^2\). If the probe is a fixed finite program, Theorem F.1 identifies its deterministic limit and hence the trace limit in probability. A fixed polynomial in the initialized actions and their adjoints satisfies the operator moment hypothesis by (F.4b), and its application to the probe is such a program. Uniform moments of order greater than one upgrade convergence of these normalized traces to convergence of their expectations: split at a large absolute threshold and use the higher-moment bound to make the first-moment tails uniformly small. The same observation supplies uniform integrability of every fixed polynomial expression needed for finite-degree moment calculations.

## 3. Exact adaptive Gaussian conditioning

Let the current transcript consist of all revealed roots and all previously computed vectors. For one matrix \(W\), collect its earlier forward and reverse observations as
\[
WV=Y,\qquad W^TU=Q.
\tag{F.5}
\]
The columns of \(V\) and \(U\) are the respective query inputs, with output columns in \(Y\) and \(Q\). Conditioned on the transcript they are fixed. Empty column lists are allowed; terms involving them are omitted.

It is necessary to justify this conditioning for adaptive inputs. Initially the conditional laws of the matrices are independent Gaussian laws. Suppose this is true, with the linear constraints already observed, at a particular instruction. A coordinate operation is measurable from the transcript and reveals no new randomness. At a matrix call its input is also measurable from the transcript. Conditional on the transcript, the new answer is a linear observation of only the queried matrix. Conditioning a product of the current conditional laws on this observation leaves the other factors unchanged and conditions only the queried factor. Thus induction preserves independence of the residual matrix factors and adds exactly the indicated linear constraint. A freshly revealed independent root likewise does not alter these residual laws. This argument conditions successively, and does not assume that an adaptive input was independent of the matrix before the transcript was fixed.

Suppose first that \(V^TV\) and \(U^TU\) are invertible. Let \(P_V=V(V^TV)^{-1}V^T\), and similarly define \(P_U\). Then
\[
W\mid\mathcal H\ \overset d=
M+P_{U^\perp}\widetilde W P_{V^\perp},
\quad
M=Y(V^TV)^{-1}V^T
 +U(U^TU)^{-1}Q^TP_{V^\perp},
\tag{F.6}
\]
where \(\widetilde W\) is an independent copy of the original matrix.

Here is a direct verification of the Gaussian projection behind (F.6). The compatibility relation is \(U^TY=Q^TV\), because both sides equal \(U^TWV\). It gives \(MV=Y\) and \(M^TU=Q\). The homogeneous solutions of (F.5) are exactly matrices \(K=P_{U^\perp}KP_{V^\perp}\). Both summands defining \(M\) are orthogonal in Frobenius inner product to that subspace. Hence \(M\) is the unique minimum-Frobenius-norm solution. Vectorize \(W\), whose law is an isotropic Gaussian in \(\mathbb R^{n^2}\). In an orthonormal basis adapted to the homogeneous solution subspace its coordinates are independent Gaussians; conditioning on the orthogonal coordinates leaves independent Gaussians on the homogeneous subspace and fixes the other coordinates to those of \(M\). This proves (F.6). It also proves the same assertion with orthogonal projections and minimum-norm solutions when column lists are linearly dependent; the nonsingular formula is the only one whose coefficients we take to a width limit.

For a new forward input \(h\), put
\[
\alpha_n=(V^TV)^{-1}V^Th,
\quad h_\perp=h-V\alpha_n,
\quad
\beta_n=(U^TU/n)^{-1}(Q^Th_\perp/n).
\]
Equation (F.6) becomes
\[
Wh=Y\alpha_n+U\beta_n
 +\|h_\perp\|_nP_{U^\perp}g
\quad\hbox{in conditional law},
\tag{F.7}
\]
with \(g\sim N(0,I_n)\) independent of the transcript. The reverse formula follows by interchanging the two sides.

Assume provisionally that every query Gram has a positive definite limit. Inductively all contractions of old nodes converge. Thus the coefficients in (F.7), and \(\|h_\perp\|_n\), converge in probability to deterministic limits. Inverting a positive definite fixed-size matrix is continuous, for instance by a Neumann-series expansion about its invertible limit.

The projection removed from the fresh noise is negligible:
\[
E[\|P_Ug\|_n^2\mid\mathcal H]
=\frac{\operatorname{rank}U}{n}.
\tag{F.8}
\]
The multiplying variance factor is bounded in probability, so conditional Markov's inequality makes its contribution vanish in normalized mean square. After this removal and replacement of convergent coefficients by their limits, the new coordinate is a deterministic linear combination \(m_\alpha\) of old same-layer nodes plus \(\sigma g_\alpha\).

For a bounded Lipschitz test \(\psi\) of the old tuple and this new coordinate, conditional independence of \(g_\alpha\) gives variance at most \(4\|\psi\|_\infty^2/n\) for its empirical average. Its conditional mean is the old empirical average of the bounded continuous function
\[
x\longmapsto E_G\psi(x,m(x)+\sigma G),
\]
which converges by the induction hypothesis. For the new second moment expand
\[
\frac1n\sum_\alpha(m_\alpha+\sigma g_\alpha)^2
=\|m\|_n^2+\frac{2\sigma}{n}\sum_\alpha m_\alpha g_\alpha
 +\frac{\sigma^2}{n}\sum_\alpha g_\alpha^2.
\]
The middle term has conditional variance \(4\sigma^2\|m\|_n^2/n\), and the last average has variance \(2/n\). All relevant norms are bounded in probability. We obtain weak convergence and second-moment convergence, hence (F.2). Coordinate instructions preserve this convergence because their Lipschitz constants bound the transport cost. This completes the induction under the provisional positive-definiteness assumption.

## 4. Source-response identity and formal derivatives

For every oriented initialized matrix introduce a centered Gaussian source group indexed by its calls. Sources for different orientations, including a matrix and its transpose, are independent groups; they are also independent of the root tuples. Within a forward group for \(W\), the source attached to input \(h\) has covariance with the source attached to input \(v\) equal to \(E[hv]\). Within the reverse group the analogous covariance is \(E[uv]\) for the corresponding reverse inputs. These are uncentered second moments of inputs and centered covariances of sources.

The scalar node of a new forward call is
\[
\mathscr W h=\xi_h+\sum_{s:\,W^Tu_s\text{ already called}}
 u_s\,E[\partial_{\zeta_s}h].
\tag{F.9}
\]
The scalar node of a reverse call is
\[
\mathscr W^*u=\zeta_u+\sum_{r:\,Wv_r\text{ already called}}
 v_r\,E[\partial_{\xi_r}u].
\tag{F.10}
\]
An input is its explicit expression in named source coordinates and roots, obtained by unrolling previous scalar instructions. A derivative in (F.9) or (F.10) differentiates that expression. Previously computed expectations, coefficients, covariance entries, mesh sizes, and any deterministic control values are held fixed. Each named source remains a separate formal argument, including when the joint source covariance is singular. An unavailable source has derivative zero. Derivative paths through other matrices' earlier calls remain part of the expression.

The recursion is causal. At a call, its input and its source derivatives are already defined; their expectations determine the response coefficients. The source covariance extension is the Gram extension of the corresponding input list and is therefore positive semidefinite. A Gaussian group with that extended covariance exists: if the old covariance is \(K\), the new cross-covariance is \(b\), and the new variance is \(v\), positivity implies \(b\in\operatorname{ran}K\) and \(v-b^TK^+b\ge0\). To see the range assertion, test positivity on \((tu,1)\) with \(Ku=0\) and arbitrary \(t\). Completing the square on \(\operatorname{ran}K\) gives the second assertion. Consequently the new coordinate can be represented as \(b^TK^+\xi+\sqrt{v-b^TK^+b}\,G\), with a fresh standard normal \(G\). Here a pseudoinverse is used only to construct one fixed finite Gaussian law; no continuity of pseudoinverses is asserted.

**Lemma F.3 (source rule).** Under the positive-definiteness assumption of Section 3, (F.9) and (F.10) give exactly the scalar laws obtained there.

**Proof.** Consider a forward call and use the notation of (F.7). Write old forward inputs as \(v_r\), old reverse inputs as \(u_s\), and their scalar outputs, by induction, as
\[
y_r=\xi_r+\sum_s D_{rs}u_s,
\qquad D_{rs}=E[\partial_{\zeta_s}v_r],
\]
\[
q_s=\zeta_s+\text{a deterministic linear combination of old }v_r.
\]
All old source lists are padded by zeros for unavailable indices. Let \(\alpha\) be the limiting least-squares coefficient from (F.7), and let \(h_\perp=h-\sum_r\alpha_rv_r\). Orthogonality gives \(E[v_rh_\perp]=0\). Therefore
\[
E[q_sh_\perp]=E[\zeta_sh_\perp].
\tag{F.11}
\]
Let \(G_U=(E[u_su_t])_{st}\), the covariance matrix of \(\zeta\). Gaussian integration by parts gives
\[
E[\zeta h_\perp]=G_U E[\nabla_\zeta h_\perp].
\tag{F.12}
\]
For completeness, the one-dimensional identity \(E[Gf(G)]=E[f'(G)]\) follows by integration by parts against the standard normal density. The boundary term vanishes for a function of at most linear growth with bounded derivative. Represent a possibly singular Gaussian vector as \(\zeta=T G\), apply this identity in each independent standard normal coordinate of \(G\), and sum using \(TT^T=G_U\). Conditioning on independent roots and the other source groups proves (F.12) in the present setting. Every derivative is integrable: at a fixed finite instruction, its norm is bounded by a deterministic finite expression in earlier coefficients and the bounded derivatives of coordinate maps.

The limiting coefficient of \(U\) in (F.7) is consequently
\[
\beta=E[\nabla_\zeta h]-\sum_r\alpha_r E[\nabla_\zeta v_r].
\]
Substitution of the old \(y_r\) decompositions in (F.7) cancels the second term exactly. The answer becomes
\[
\xi_h+\sum_su_sE[\partial_{\zeta_s}h],
\qquad
\xi_h=\sum_r\alpha_r\xi_r+\sigma G,
\quad \sigma^2=E[h_\perp^2].
\]
Since the old \(\xi\) covariance is the Gram of the \(v_r\),
\[
E[\xi_h\xi_r]=E[hv_r],
\quad
E[\xi_h^2]=E\Big(\sum_r\alpha_rv_r\Big)^2+E[h_\perp^2]=E[h^2].
\]
The fresh normal is independent of all old roots and source groups. Thus adjoining it preserves independence of distinct oriented source groups. The reverse calculation is the same after interchanging the two layers. Interleaving calls of different matrices does not alter this calculation, because Section 3 established the conditional independence of their residual factors. ∎

Independence of source groups does not assert that the answers of a matrix and its transpose are independent. Their response terms encode their dependence. Nor does it assert that a source is independent of all later inputs; later scalar inputs can be functions of that source.

## 5. Singular queries without a rank-stability assumption

**Lemma F.4 (regularization of a fixed program).** The conclusions of Theorem F.1 and the formulas (F.9)–(F.10) hold when any of the limiting input Grams is singular.

**Proof.** For every matrix call introduce a new independent standard Gaussian input vector \(\chi\), revealed immediately before that call, and replace its input \(h\) by \(h+\varepsilon\chi\). Each call has a distinct noise vector. The other instructions are unchanged.

At fixed \(\varepsilon>0\), the new noise is independent of the old transcript and of the unperturbed part of the current input. If \(V\) is the list of prior same-orientation inputs, the normalized squared distance from \(h+\varepsilon\chi\) to \(\operatorname{span}V\) is
\[
\|P_{V^\perp}h\|_n^2
 +2\varepsilon\langle P_{V^\perp}h,\chi\rangle_n
 +\varepsilon^2\|P_{V^\perp}\chi\|_n^2.
\]
Conditionally, the cross term has variance \(4\varepsilon^2\|P_{V^\perp}h\|_n^2/n\). The last norm squared has mean \(1-\operatorname{rank}V/n\) and variance at most \(2/n\). Thus every limiting new squared distance is at least \(\varepsilon^2\). Induction gives positive definite limiting query Grams, so Sections 3–4 apply to the perturbed program. Equivalently, in its scalar law the new independent root adds \(\varepsilon^2\) to the Schur complement of the old input Gram.

Couple the perturbed and original finite programs with the same matrices and roots. On the event that the two matrix norms are at most 10 and that all of the finitely many fresh noise vectors have normalized norms at most 2, propagate errors instruction by instruction. A coordinate instruction multiplies the previous error by its fixed Lipschitz constant; a linear combination contributes the sum of coefficient magnitudes times previous errors; a matrix call contributes at most ten times the input error plus \(20\varepsilon\). Consequently
\[
\max_{\text{nodes }v}\|v_n^\varepsilon-v_n\|_n
\le C\varepsilon,
\tag{F.13}
\]
where \(C\) is finite and independent of \(n\) and \(0<\varepsilon\le1\). The event has probability tending to one by Lemma F.2 and the elementary second-moment calculation for Gaussian noise norms.

We next show that the scalar recursion itself is continuous at \(\varepsilon=0\); this step concerns covariances and derivatives, not inverses of empirical Grams. Induct on its finitely many instructions. Each scalar node is a \(C^1\) expression in the finite named source list and roots. If earlier deterministic coefficients remain in a compact set, the expression and its first source derivatives have uniform bounds: the expression has at most linear growth in the root and source coordinates, and its derivatives have a finite deterministic bound. This follows directly by applying the coordinate derivative bounds and the linear response formulas in the previous instructions. The values and first derivatives are continuous in their arguments and in the earlier coefficient list.

By induction, the covariance entries for the next source, which are second moments of old scalar inputs, converge as \(\varepsilon\downarrow0\). If positive semidefinite matrices \(K_j\to K\) have fixed size, then \(K_j^{1/2}\to K^{1/2}\). To verify this without a regularity assumption on eigenvalues, their positive square roots are bounded. Every convergent subsequence of these square roots has a positive semidefinite limit \(T\) with \(T^2=K\). A positive semidefinite matrix has a unique positive semidefinite square root: diagonalize it, observe that any such \(T\) commutes with \(K=T^2\), and restrict to its eigenspaces. Hence every subsequential limit is \(K^{1/2}\), which proves convergence.

Represent the full finite source prefix for each \(\varepsilon\) as \(K_\varepsilon^{1/2}G\) using one standard Gaussian vector for each oriented group, independently of the roots. This couples the source prefixes in \(L^2\). The uniform linear-growth bounds and Lipschitz constants for node expressions then give their \(L^2\) convergence. More explicitly, split the node difference into a change of arguments at fixed coefficients, bounded by the common Lipschitz constant, and a change of coefficients at fixed arguments. The latter converges pointwise and is bounded by a constant times one plus the norm of the finite root/source list, an \(L^2\) dominator. First source derivatives converge in probability and are uniformly bounded, so their expectations converge. This proves convergence of the next response coefficient and closes the induction. At zero noise the resulting expression is exactly (F.9)–(F.10) for the original formal program.

Let \(\mu^\varepsilon\) be the perturbed scalar law of a selected tuple and \(\mu^0\) the zero-noise law just constructed. We have \(\mathcal W_2(\mu^\varepsilon,\mu^0)\to0\). By (F.3), (F.13), and the proved fixed-\(\varepsilon\) limit,
\[
\mathcal W_2(\widehat\mu_n,\mu^0)
\le C_m\varepsilon
 +\mathcal W_2(\widehat\mu_n^\varepsilon,\mu^\varepsilon)
 +\mathcal W_2(\mu^\varepsilon,\mu^0)
\]
on an event of probability tending to one. Choose \(\varepsilon\) first, let \(n\to\infty\), and then let \(\varepsilon\downarrow0\). This proves the full-sequence convergence in probability, including singular Grams, and finishes Theorem F.1. ∎

The derivative convention has a precise invariant meaning on singular supports. If a source vector \(\zeta\) has covariance \(G\), and \(u\) is the vector of the associated reverse inputs with \(E[uu^T]=G\), then
\[
E[\zeta f]=G E[\nabla f],\qquad
u^Tv=0\text{ a.s. for every }v\in\ker G.
\tag{F.14}
\]
The second identity follows from \(E[(u^Tv)^2]=v^TGv=0\). If two admissible smooth formal expressions agree on the Gaussian support, their expected derivative vectors differ by an element of \(\ker G\), by the first identity. Their contracted corrections therefore agree. Individual derivative coefficients need not agree. None of this implies that pseudoinverses converge at rank loss.

## 6. Causal scalar feedback and the three-sample gain network

The deterministic-coefficient theorem also identifies programs with the following causal scalar feedback. At finitely many stages, compute inner products of already available same-layer nodes, apply locally Lipschitz functions to the resulting finite scalar list, and use the resulting numbers as coefficients of subsequent linear combinations. Assume all scalar operations are defined at the deterministic limit values; divisions require a nonzero limiting denominator. Coefficients may multiply unbounded vector nodes, because their perturbations can be estimated by the vector's normalized \(L^2\) norm.

To prove this extension, construct an oracle program by replacing each scalar feedback value by its limiting deterministic value, computed from earlier scalar nodes. The construction is causal and therefore not an implicit fixed-point definition. Theorem F.1 identifies this oracle. At the next scalar step use
\[
|\langle u,v\rangle_n-\langle\bar u,\bar v\rangle_n|
\le\|u-\bar u\|_n\|v\|_n
 +\|\bar u\|_n\|v-\bar v\|_n.
\tag{F.15}
\]
At the next scalar multiplication use
\[
\|c u-\bar c\bar u\|_n
\le |c|\|u-\bar u\|_n+|c-\bar c|\|\bar u\|_n.
\]
All oracle norms and finitely many oracle coefficients are bounded in probability; initial operator norms are bounded with probability tending to one. Inductively, these inequalities show that actual coefficients converge to oracle coefficients, actual node errors vanish in normalized \(L^2\), and actual norms remain bounded in probability. Local Lipschitzness of scalar operations suffices by restricting to a compact neighborhood of their deterministic limiting arguments. Equation (F.3) transfers every oracle empirical law to the actual program.

For the gain network let \(g(z)=(1+z^2)^{-1}\), and choose fixed smooth clips with
\[
\tau_R(q)=q\ (|q|\le R),\quad
|\tau_R(q)|\le\min\{|q|,2R\},\quad |\tau_R'(q)|\le1.
\]
The capped backward gate is
\[
D_R(z,q)=a q+e g(z)\tau_R(q).
\tag{F.16}
\]
Its derivatives satisfy
\[
|\partial_qD_R|\le a+e,\qquad
|\partial_zD_R|\le4eR,
\tag{F.17}
\]
since \(|g|\le1\) and \(|g'|\le2\). Thus this gate is a globally Lipschitz \(C^1\) map at every fixed cap even though its affine part is unbounded. The activation (F.1) has derivative bounded by \(a+e\), so it satisfies the same finite-program regularity requirement. This includes the top gate with incoming field \(C\), as well as the two lower gates. No pointwise bound on \(C\) is required for (F.17).

Write three-sample column vectors at time index \(k\) as \(Z_k^\ell,H_k^\ell,\Delta_k^\ell,Q_k^\ell\). All functions on these triples are applied coordinatewise. For deterministic controls \(c_k\in\mathbb R^3\), step sizes \(h_k>0\), and the fixed input Gram \(\Gamma_{ij}=x_i^Tx_j/d\), put \(P_k=\Gamma\operatorname{diag}(c_k)\). Raw simultaneous Euler has
\[
Z_k^1=Z_0^1+\sum_{r<k}h_rP_r\Delta_r^1,
\quad C_k=\sum_{r<k}h_r c_r^T H_r^3,
\tag{F.18}
\]
\[
H_k^\ell=\phi(Z_k^\ell),\quad
\Delta_k^3=D_R(Z_k^3,\mathbf1 C_k),\quad
\Delta_k^2=D_R(Z_k^2,Q_k^2),\quad
\Delta_k^1=D_R(Z_k^1,Q_k^1).
\]
Unrolling the learned matrices and applying (F.9)–(F.10) gives
\[
Z_k^2=\Xi_k^2+\sum_{r<k}\mathsf a^2_{kr}\Delta_r^2,
\quad
Z_k^3=\Xi_k^3+\sum_{r<k}\mathsf a^3_{kr}\Delta_r^3,
\tag{F.19}
\]
\[
Q_k^1=\mathcal Z_k^1+\sum_{r\le k}\mathsf b^2_{kr}H_r^1,
\quad
Q_k^2=\mathcal Z_k^2+\sum_{r\le k}\mathsf b^3_{kr}H_r^2.
\tag{F.20}
\]
Rows and columns of the coefficient blocks are sample indices, with the explicit entries
\[
(\mathsf a^\ell_{kr})_{ij}
=E\!\left[\frac{\partial H_{k,i}^{\ell-1}}
 {\partial\mathcal Z_{r,j}^{\ell-1}}\right]
 +h_r c_{r,j}E[H_{k,i}^{\ell-1}H_{r,j}^{\ell-1}],
\tag{F.21}
\]
\[
(\mathsf b^\ell_{kr})_{ij}
=E\!\left[\frac{\partial\Delta_{k,i}^{\ell}}
 {\partial\Xi_{r,j}^{\ell}}\right]
 +1_{r<k}h_r c_{r,j}E[\Delta_{k,i}^{\ell}\Delta_{r,j}^{\ell}],
\tag{F.22}
\]
for \(\ell=2,3\). The four source groups are independent and have covariances
\[
E[\Xi_{k,i}^{\ell}\Xi_{r,j}^{\ell}]
=E[H_{k,i}^{\ell-1}H_{r,j}^{\ell-1}],
\qquad
E[\mathcal Z_{k,i}^{\ell-1}\mathcal Z_{r,j}^{\ell-1}]
=E[\Delta_{k,i}^{\ell}\Delta_{r,j}^{\ell}].
\tag{F.23}
\]
These source groups and the first root \(Z_0^1\sim N(0,\Gamma)\) can all be constructed independently before evaluating the scalar expressions.

To check the learned terms, a finite forward action at time \(k\) is
\[
A_kh_{k,i}^1=A_0h_{k,i}^1
 +\sum_{r<k,j}h_rc_{r,j}\delta_{r,j}^2
       \langle h_{r,j}^1,h_{k,i}^1\rangle_n;
\]
the reverse action has the corresponding term
\(\sum_{r<k,j}h_rc_{r,j}h_{r,j}^1
\langle\delta_{r,j}^2,\delta_{k,i}^2\rangle_n\).
This proves the signs, sample positions, and coefficients in (F.21)–(F.22). The same calculation applies to the third layer. At a step, all second-layer forwards precede all third-layer forwards, which precede all third-layer reverses and then all second-layer reverses. Current forward inputs do not depend on current reverse answers. Thus forward responses have \(r<k\), whereas reverse responses include \(r=k\). Within a sample block an input that does not use another current sample's source has zero formal derivative with respect to it.

In particular a current second-layer reverse coefficient can contain a derivative path through the already computed current third-layer reverse answer. The instruction order does not authorize dropping this path. Formulas (F.21)–(F.22), which use the full expression derivative, retain it without an implicit inversion.

For physical Euler, take coefficients \(c_{k,i}=-r_{k,i}\) with \(r_{k,i}=\langle C_k,h_{k,i}^3\rangle_n-y_i\). Their identification follows from the causal-feedback argument. If a population trajectory is reparametrized into a controlled mesh with \(h_k=\Delta t_k\|r_k\|_1\) and \(c_k=-r_k/\|r_k\|_1\), freeze those numerical values in formal source derivatives. At a zero residual the update is zero and the step can be omitted. The theorem does not assert continuity of \(r/\|r\|_1\) at zero, and does not need to differentiate it.

The actual finite readout initialization has independent entries \(C_{0,\alpha}\sim N(0,n^{-2})\). Its normalized norm satisfies \(E\|C_0\|_n^2=n^{-2}\), hence is \(O_{\mathbb P}(n^{-1})\). Couple it to a zero-readout comparator at the same width. The finite instruction comparison just proved, using (F.17), (F.15), and the bounded operator event, propagates this vanishing discrepancy through any fixed capped program. Therefore its population initial readout is zero, while the actual finite training retains the random initialized readout.

## 7. Common generated probability spaces and actual adjoints

We now fix the data and activation parameters. Construct a countable language of finite deterministic-coefficient programs. Include every root coordinate required by the model; constants; rational linear combinations; applications of the initialized matrices in both directions; the activation and fixed integer-level clips; and, for each arity, a countable family of bounded smooth globally Lipschitz functions dense among continuous functions on compact sets. One explicit such family is obtained by taking piecewise polynomial approximations on rational grids, multiplying by smooth compactly supported cutoffs, smoothing with fixed rational-scale mollifiers, and retaining rational coefficients and rational scales. Clipped products may be included in the same family. Close the language under finite composition. Additional countable lists of fixed programs, probes, caps, time meshes, or coefficient values can be included at the start.

This language is countable and admits a causal enumeration with finite stages. Enumerate its root slots, functions, and numerical coefficients first; at stage \(m\), add the finitely many expressions with at most \(m\) instructions using only the first \(m\) listed items, in dependency order. Every finite expression occurs at some stage. Repeated instructions may be treated as separate named copies. Running the scalar construction on this list realizes all its nodes on a product probability space with countably many independent standard Gaussian coordinates, together with the root tuples. Section 4 gives the successive Gaussian extensions, including zero conditional variance. At each layer retain only the sigma-field generated by that layer's node coordinates; call the resulting probability space \((\Omega_\ell,\mu_\ell)\) and put
\[
H_\ell=L^2(\Omega_\ell,\mu_\ell).
\tag{F.24}
\]
One can equivalently take the law of the countable tuple of generated coordinates. Its finite-dimensional marginal laws are those from Theorem F.1: any finite family is part of a finite program, and unused computations change none of the finite-width vectors. Thus different causal enumerations produce the same generated laws up to the coordinate identification. No arbitrary extra Gaussian directions are added to \(H_\ell\).

For every rational combination \(u\) of generated nodes, include its forward and reverse answer nodes. The finite inequality \(\|A_nu_n\|_n\le10\|u_n\|_n\) holds with probability tending to one. Both squared norms have deterministic limits by Theorem F.1, so
\[
\|\mathscr A_0u\|_{H_2}\le10\|u\|_{H_1}.
\tag{F.25}
\]
The same holds for the other three action orientations. Linearity of the finite matrices and convergence of squared differences give linearity of the assignments: for example the limiting squared norm of the difference between the answer to \(u+v\) and the sum of answers is zero. If two expressions represent the same \(L^2\) input, (F.25) shows that their answers represent the same output. Real linearity on the real span follows either from finite real-coefficient probes or from rational approximation.

The span of generated nodes is dense in \(H_\ell\). Here are the measure-theoretic details. Cylinder sets depending on finitely many coordinates generate its sigma-field. The sets whose indicators can be approximated in \(L^2\) by finite linear combinations of cylinder indicators form a monotone class: under increasing unions or decreasing intersections, indicator convergence in \(L^2\) follows from the continuity of probability measures. They contain the cylinder algebra, hence all generated measurable sets. Simple functions and truncation then approximate every \(L^2\) variable by functions of finitely many coordinates. For a finite Borel probability law on \(\mathbb R^m\), bounded continuous functions are dense in \(L^2\): approximate an indicator by a compact subset inside an open superset whose probability difference is small, and use the continuous distance-ratio function that is one on the compact set and zero outside the open set. Such compact/open approximations follow by first restricting to large boxes and then approximating Borel sets using finite unions of rational boxes; their class is again a monotone class. Finally approximate bounded continuous functions on compact boxes by the included smooth family and control the complement by boundedness and its small probability. All approximants are generated nodes or linear combinations of them.

Consequently (F.25) extends uniquely by \(L^2\) completion to a bounded linear map
\[
A_0:H_1\to H_2,\qquad B_0:H_2\to H_3,
\qquad \|A_0\|,\|B_0\|\le10.
\tag{F.26}
\]
The reverse assignments extend in the same way. At finite width,
\(\langle v_n,A_nu_n\rangle_n=\langle A_n^Tv_n,u_n\rangle_n\).
Pass to the limiting pairwise contractions for generated \(u,v\); then use their density and the bounds (F.26). This gives
\[
\langle v,A_0u\rangle_{H_2}
=\langle A_0^*v,u\rangle_{H_1},
\qquad
\langle v,B_0u\rangle_{H_3}
=\langle B_0^*v,u\rangle_{H_2}.
\tag{F.27}
\]
The starred maps are therefore exactly the Hilbert-space adjoints. They are not resampled reverse matrices.

There is no contradiction between these bounded actions and Gaussian initialization. The actions describe all finite generated probes and their joint laws, including adaptive probes. They are not an assertion that every random \(L^2\) input is independent of an initialized action. An adaptive input generally has the response correction in (F.9).

Fixed programs with arbitrary real coefficients and arbitrary globally Lipschitz coordinate instructions are represented on these same spaces. Approximate their coefficients by rationals and their coordinate functions on larger compact sets by the dense family, with bounded truncations outside. At a fixed scalar input, the approximation error tends to zero in \(L^2\) by linear growth and the input's finite second moment. Inductively propagate these errors: every matrix call uses the norm bound 10, and each target coordinate instruction uses its Lipschitz bound to control a change of input before approximating the instruction at the limiting input. The identical finite-array error argument holds in probability by Theorem F.1 and convergence of the required tail second moments. This proves the agreement of the common-space calculation with its fixed-program width limit.

## 8. Hilbert–Schmidt increments and the raw state space

For Hilbert spaces \(H,K\), the Hilbert–Schmidt norm of an operator \(T:H\to K\) is
\[
\|T\|_{\rm HS}^2=\sum_j\|Te_j\|_K^2,
\tag{F.28}
\]
where \((e_j)\) is an orthonormal basis. This value does not depend on the basis: expand each scalar coefficient \(\langle Te_j,f_k\rangle\) in a basis \((f_k)\) of \(K\), use Parseval twice, and interchange the nonnegative double sum. In particular \(\|T\|_{\rm op}\le\|T\|_{\rm HS}\), since for a unit vector completed to an orthonormal basis its image squared norm is one summand of (F.28). The normed space of such operators is complete: a Cauchy sequence has Cauchy matrix coefficients in \(\ell^2\) of two basis indices, whose limit defines an operator by Cauchy–Schwarz and has the limiting Hilbert–Schmidt norm.

For \(u\in K,v\in H\), define
\[
(u\otimes v)q=u\langle v,q\rangle_H.
\]
Parseval gives
\[
\|u\otimes v\|_{\rm HS}=\|u\|_K\|v\|_H,
\quad
(u\otimes v)^*=v\otimes u,
\tag{F.29}
\]
and
\[
\|u\otimes v-\tilde u\otimes\tilde v\|_{\rm HS}
\le\|u-\tilde u\|\|v\|+\|\tilde u\|\|v-\tilde v\|.
\tag{F.30}
\]
For a Hilbert–Schmidt \(T\), expansion in an orthonormal basis also gives
\[
\langle u\otimes v,T\rangle_{\rm HS}=\langle u,Tv\rangle_K.
\tag{F.31}
\]
At width \(n\), using the normalized inner product on both layers, the orthonormal basis is \((\sqrt n\,e_j)_{j=1}^n\); (F.28) is then the ordinary Frobenius norm of the matrix. The rank-one action is \(uv^T/n\). Thus this is the exact population counterpart of the raw matrix metric.

The affine raw parameter space is
\[
\mathcal P=\left\{(w,A_0+U,B_0+V,C):
\ w\in L^2(\Omega_1;\mathbb R^d),\ U\in\mathrm{HS}(H_1,H_2),
\ V\in\mathrm{HS}(H_2,H_3),\ C\in H_3\right\},
\tag{F.32}
\]
with variation norm
\[
\|\dot\theta\|_{\rm raw}^2
=d\|\dot w\|_2^2+\|\dot A\|_{\rm HS}^2
 +\|\dot B\|_{\rm HS}^2+\|\dot C\|_2^2.
\tag{F.33}
\]
Only the learned increments are required to be Hilbert–Schmidt. The initialized actions need not be Hilbert–Schmidt.

Continuous rank-one velocities have integrals in this norm. Indeed their Riemann sums are Cauchy by uniform continuity on a compact time interval and completeness, and the norm of the integral is bounded by the integral of the norm. The derivative of this integral is the continuous integrand, by dividing its integral over a short interval by that interval's length. Formula (F.30) shows that uniform \(L^2\) convergence of its two factors gives convergence of the velocity and its integral in Hilbert–Schmidt norm. The same conclusions hold for Bochner-integrable measurable velocities by approximation by step functions. This identifies trained increments and their reverses on the common spaces.

## 9. Strong multiplier continuity and the chain rule

**Lemma F.5 (bounded multiplier).** Suppose \(z_m\to z\) in probability, \(v_m\to v\) in \(L^2\), and \(b\) is bounded and continuous. Then
\[
b(z_m)v_m\longrightarrow b(z)v\quad\hbox{in }L^2.
\tag{F.34}
\]

**Proof.** The term \(b(z_m)(v_m-v)\) has norm at most \(\|b\|_\infty\|v_m-v\|_2\). For the remaining term first restrict to \(|v|\le M\); bounded convergence in probability implies convergence in \(L^2\) of the bounded multiplier difference there. The complement has squared norm at most \(4\|b\|_\infty^2E[|v|^2 1_{|v|>M}]\). Send \(m\) to infinity and then \(M\) to infinity. Bounded convergence in probability used here follows from the elementary estimate \(E|X_m|^2\le\eta^2+K^2\Pr(|X_m|>\eta)\) when \(|X_m|\le K\). ∎

**Lemma F.6 (strong chain rule along curves).** Let \(z:I\to L^2(\Omega)\) be strongly \(C^1\), and let \(\phi\in C^1(\mathbb R)\) have bounded derivative. Then \(\phi(z(t))\) is strongly \(C^1\), with
\[
\frac d{dt}\phi(z(t))=\phi'(z(t))\dot z(t).
\tag{F.35}
\]

**Proof.** Set \(v_h=(z(t+h)-z(t))/h\to\dot z(t)\) in \(L^2\). The scalar fundamental theorem of calculus gives
\[
\frac{\phi(z(t+h))-\phi(z(t))}{h}
=v_h\int_0^1\phi'(z(t)+rh v_h)\,dr.
\]
The multiplier is bounded by \(\|\phi'\|_\infty\). It converges in probability to \(\phi'(z(t))\): \(|hv_h|\to0\) in probability; restrict \(z(t)\) to a large compact interval and use uniform continuity of \(\phi'\) on a slightly larger interval. The proof of Lemma F.5 applies to this bounded convergent multiplier, and yields the derivative. Lemma F.5 applied to \(z(t),\dot z(t)\) also proves continuity of the resulting velocity. ∎

This conclusion is a curve chain rule, and makes no claim that the pointwise nonlinear map is Fréchet differentiable from all of \(L^2\) to \(L^2\). Bounded \(\phi'\) is sufficient for the curve result. A jointly measurable velocity may also be integrated coordinatewise: Fubini and \(E\int_I|v(t)|^2dt<\infty\) give absolutely continuous coordinate paths almost surely, agreeing with the \(L^2\) integral. This permits the ordinary scalar chain rule almost everywhere for an absolutely continuous \(L^2\) curve with integrable squared speed.

For bounded-operator curves \(A(t)\) differentiable in Hilbert–Schmidt or operator norm and strongly differentiable \(h(t)\in H\),
\[
\frac d{dt}[A(t)h(t)]=\dot A(t)h(t)+A(t)\dot h(t).
\tag{F.36}
\]
Subtract the proposed derivative from the difference quotient. The first error is the operator derivative error applied to fixed \(h(t)\); the second is a uniformly bounded operator applied to the strong derivative error of \(h\); and the cross product is bounded by \(\|A(t+h)-A(t)\|\,\|(h(t+h)-h(t))/h\|\), which tends to zero. This proves (F.36).

## 10. The scalar predictor is continuously Fréchet differentiable

At a raw state (F.32), define for \(i=1,2,3\)
\[
z_i^1=x_i^Tw,\quad h_i^1=\phi(z_i^1),\quad
z_i^2=Ah_i^1,\quad h_i^2=\phi(z_i^2),\quad
z_i^3=Bh_i^2,\quad h_i^3=\phi(z_i^3),\quad
f_i=\langle C,h_i^3\rangle.
\tag{F.37}
\]
All fields belong to their indicated \(L^2\) spaces because \(|\phi(z)|\le|\phi(0)|+\|\phi'\|_\infty|z|\) and the actions are bounded. Put
\[
b_i^3=C\phi'(z_i^3),\quad
q_i^2=B^*b_i^3,\quad b_i^2=\phi'(z_i^2)q_i^2,
\quad q_i^1=A^*b_i^2,\quad b_i^1=\phi'(z_i^1)q_i^1.
\tag{F.38}
\]

**Theorem F.7.** For the activation (F.1), \(f_i:\mathcal P\to\mathbb R\) is continuously Fréchet differentiable in the norm (F.33), and
\[
df_i[\dot\theta]
=\langle b_i^1,x_i^T\dot w\rangle
 +\langle b_i^2,\dot A h_i^1\rangle
 +\langle b_i^3,\dot B h_i^2\rangle
 +\langle h_i^3,\dot C\rangle.
\tag{F.39}
\]
Its raw gradient is
\[
\nabla_{\rm raw}f_i
=\left(d^{-1}b_i^1 x_i,
\ b_i^2\otimes h_i^1,
\ b_i^3\otimes h_i^2,
\ h_i^3\right).
\tag{F.40}
\]

**Proof.** We first prove the scalar weighted Taylor estimate that avoids any unjustified \(L^2\)-to-\(L^2\) Fréchet derivative. Write \(L_1=\|\phi'\|_\infty\) and \(L_2=\|\phi''\|_\infty\), both finite for (F.1). For fixed \(v,z\in L^2\) and an increment \(q\in L^2\), the Taylor remainder \(\rho=\phi(z+q)-\phi(z)-\phi'(z)q\) obeys
\[
|\rho|\le\tfrac12L_2|q|^2,
\qquad |\rho|\le2L_1|q|.
\]
Splitting at \(|v|=M\) gives
\[
|E[v\rho]|
\le\tfrac12L_2 M\|q\|_2^2
 +2L_1\|v1_{|v|>M}\|_2\|q\|_2
=o(\|q\|_2).
\tag{F.41}
\]
The final conclusion follows by first fixing \(M\), dividing by \(\|q\|_2\), letting this norm tend to zero, and then sending \(M\) to infinity.

For a raw perturbation of size \(\eta\), forward differences in every \(z_i^\ell,h_i^\ell\) are \(O(\eta)\) in \(L^2\) on a neighborhood of the fixed state. Start with \(\|x_i^T\Delta w\|_2\le\|x_i\|\|\Delta w\|_2\), use Lipschitzness of \(\phi\), and successively expand
\[
(A+\Delta A)(h_i^1+\Delta h_i^1)-Ah_i^1
=\Delta A h_i^1+A\Delta h_i^1+\Delta A\Delta h_i^1,
\]
using \(\|\Delta A\|_{\rm op}\le\|\Delta A\|_{\rm HS}\); repeat for \(B\).

Expand the scalar prediction from the top down. The term \(\langle\Delta C,\Delta h_i^3\rangle\) is \(O(\eta^2)\). Apply (F.41) to \(\langle C,\Delta h_i^3\rangle\), with fixed weight \(C\), to replace \(\Delta h_i^3\) by \(\phi'(z_i^3)\Delta z_i^3\) at cost \(o(\eta)\). The preceding product expansion gives the linear terms \(\langle b_i^3,\Delta B h_i^2\rangle+\langle B^*b_i^3,\Delta h_i^2\rangle\), while \(\langle b_i^3,\Delta B\Delta h_i^2\rangle=O(\eta^2)\). Apply (F.41) again with fixed weight \(B^*b_i^3=q_i^2\), then expand \(\Delta z_i^2\). The resulting terms are \(\langle b_i^2,\Delta A h_i^1\rangle+\langle A^*b_i^2,\Delta h_i^1\rangle\), with an \(O(\eta^2)\) cross term. One final application of (F.41), now with fixed weight \(q_i^1=A^*b_i^2\), yields \(\langle b_i^1,x_i^T\Delta w\rangle\). These are exactly (F.39), and every discarded error is \(o(\eta)\). Thus this is a Fréchet derivative.

Formula (F.31) and the factor \(d\) in the first block of (F.33) identify (F.40). To prove continuity, forward fields are continuous in \(L^2\). Apply Lemma F.5 successively to the bounded continuous gate \(\phi'\) and the incoming backward fields; combine it with operator-norm continuity of \(A,B\) and their adjoints. This proves \(L^2\) continuity of all fields in (F.38). Formula (F.30) then proves continuity of the Hilbert–Schmidt gradient blocks. ∎

For \(L(\theta)=\frac12\sum_{i=1}^3(f_i-y_i)^2\), Theorem F.7 yields
\[
\nabla_{\rm raw}L=\sum_i r_i\nabla_{\rm raw}f_i.
\]
Thus any constructed strong solution of the uncapped equations
\[
\dot w=-d^{-1}\sum_i r_i b_i^1x_i,
\quad\dot A=-\sum_i r_i b_i^2\otimes h_i^1,
\quad\dot B=-\sum_i r_i b_i^3\otimes h_i^2,
\quad\dot C=-\sum_i r_i h_i^3
\tag{F.42}
\]
is an actual gradient flow in this raw metric. The scalar chain rule along a differentiable curve follows immediately from the Fréchet remainder divided by the time increment. It gives
\[
\dot f_i=-\sum_j K_{ij}r_j,
\qquad
\dot L=-\Big\|\sum_i r_i\nabla_{\rm raw}f_i\Big\|_{\rm raw}^2
=-r^TKr,
\tag{F.43}
\]
where the four blocks are
\[
K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle,
\quad K^2_{ij}=\langle b_i^2,b_j^2\rangle\langle h_i^1,h_j^1\rangle,
\]
\[
K^3_{ij}=\langle b_i^3,b_j^3\rangle\langle h_i^2,h_j^2\rangle,
\quad K^4_{ij}=\langle h_i^3,h_j^3\rangle,
\qquad K=K^1+K^2+K^3+K^4.
\tag{F.44}
\]
Each is a Gram matrix of one block of the raw gradients and is positive semidefinite. The first formula uses \(d\langle d^{-1}b_i^1x_i,d^{-1}b_j^1x_j\rangle=\Gamma_{ij}\langle b_i^1,b_j^1\rangle\). These conclusions require the existence of the strong uncapped solution; this chapter does not supply its global construction or uniqueness.

## 11. Fixed-cap local flow and finite probes

For clarity, the local well-posedness used before removing caps follows from the preceding estimates without assuming differentiability of the activation map on \(L^2\). On a raw ball, forward propagation is Lipschitz in \(L^2\). Equation (F.17) makes each capped backward substitution Lipschitz in its two \(L^2\) arguments; bounded actions and (F.30) make the update field locally Lipschitz in the raw parameter norm. Physical coefficients \(-r_i\) are locally Lipschitz there by (F.15) and forward continuity.

For a continuous autonomous capped field \(F_R\), choose a ball of radius \(\rho\) about the initial state where \(\|F_R\|\le M\) and the Lipschitz constant is \(L\). On continuous paths staying in that ball, the integral map \(\theta\mapsto\theta_0+\int_0^tF_R(\theta(s))ds\) preserves the ball if \(TM\le\rho\) and is a contraction if \(TL<1\). Iterating it gives a uniformly convergent sequence, since successive differences decay by the factor \(TL\); completeness gives a unique fixed point. Its integral equation and continuity of the field give a strong \(C^1\) solution. The same contraction proves uniqueness in that ball. If a solution and its velocity remain bounded on a finite interval within a ball of local Lipschitzness, its endpoint exists by the estimate \(\|\theta(t)-\theta(s)\|\le M|t-s|\), and the argument restarts there. Establishing the requisite primal bounds globally is a separate step.

For measurable deterministic controls with \(\sum_i|c_i(t)|\le1\), the same integral contraction gives a strongly absolutely continuous controlled solution and its equation almost everywhere. It need not be \(C^1\) when the controls jump. This distinction is relevant when using arbitrary controlled paths as an intermediate device.

On a common bounded ball, a fixed-cap autonomous field with bounds \(M,L\) has one-step Euler defect at most \(LMh^2/2\). Indeed integrate \(\|F_R(\theta(t+s))-F_R(\theta(t))\|\le LMs\). If \(E_k\) is the discrepancy at mesh points,
\[
E_{k+1}\le(1+Lh_k)E_k+\tfrac12LMh_k^2.
\]
Iteration and \(\prod_k(1+Lh_k)\le e^{L\sum h_k}\) give
\[
\max_kE_k\le e^{LT}\left(E_0+\tfrac12LMT\max_kh_k\right).
\tag{F.45}
\]
All constants in these raw estimates can be chosen independent of width on the initialized operator event and the prescribed primal ball. At a fixed auxiliary mesh Theorem F.1 identifies the Euler laws; (F.45) then permits width to tend to infinity before the auxiliary mesh is refined. It does not permit applying Theorem F.1 directly with a width-dependent growing program.

A final probe may contain an uncut bounded multiplier, for example \(q\phi'(z)\), whose coordinate derivatives are not globally bounded in \((z,q)\). Its law can nevertheless be identified after the underlying tuple has a \(\mathcal W_2\) limit. The map is continuous and has at most linear growth. More explicitly, replace \(q\) by a fixed bounded smooth truncation. The truncated probe is covered by the finite theorem. Its mean-square error is bounded by a constant times \(E[q^2 1_{|q|>M}]\), or its empirical counterpart. Convergence in \(\mathcal W_2\) supplies uniformly small tail second moments as \(M\to\infty\), so the untruncated probe follows. A finite list of subsequent matrix actions preserves these errors by (F.26) and Lemma F.2. This is a truncation argument for observables; it supplies neither a source-derivative identity with unbounded derivatives nor a cap-uniform trajectory estimate.

The results of this chapter therefore provide: the exact fixed-program laws, all orientation-dependent response corrections, singular-query handling, common bounded initialized actions and actual adjoints, the raw Hilbert parameter structure, and the strong and scalar chain rules. Uniform response tails, removal of backward caps, global continuation, and the full path and velocity limits remain separate mathematical obligations.

# Part R. Controlled source responses for three samples

This part proves the response bound using only the fixed-program Gaussian and common-space Lemma F stated precisely below. A separate primal estimate supplies the affine boundedness hypothesis. The proof identifies the actual source equations, converts affine raw stability to formal response bounds by a Gaussian probe, bounds nonlinear source variances without assuming response estimates, controls coordinate and derivative moments on bounded prefixes, and closes those prefixes in the chronological order of the four query stages.

## R.1. Setup and the Gaussian-program input

Fix \(a\ge1,B\ge1,S>0\), and a positive semidefinite \(3\times3\) matrix \(\Gamma\) with unit diagonal. On any positive mesh \(0=s_0<\cdots<s_N\le S\), put \(h_j=s_{j+1}-s_j\). Choose deterministic controls \(c_j\in\mathbb R^3\) with \(\sum_i|c_{j,i}|\le1\), and set
\[
 P_j=\Gamma\operatorname{diag}(c_j),\qquad \mathbf1=(1,1,1)^T.
 \tag{R.1}
\]
Positive semidefiniteness of two-by-two principal minors gives \(|\Gamma_{im}|\le1\). Thus \(|P_j|\le1\), where, for rectangular matrices and finite rows of time blocks,
\[
 |T|=\max_i\sum_j|T_{ij}|,\qquad
 |T_{k\bullet}|_{\rm r}=\sum_j|T_{kj}|.
 \tag{R.2}
\]
These norms are submultiplicative, \(|I_3|=|\mathbf1|=1\), and \(|c_j^T|\le1\). For a random three-vector use \(\|X\|_p=(E|X|_\infty^p)^{1/p}\). Pad derivative rows by causal zero blocks when necessary.

For \(0\le\epsilon\le1\), take
\[
 \phi_\epsilon(z)=a(1+z)+\epsilon\arctan z,\quad g(z)=(1+z^2)^{-1},
 \quad D_{\epsilon,R}(z,q)=aq+\epsilon g(z)\tau_R(q).
 \tag{R.3}
\]
The finite cap \(R>0\) uses a smooth function satisfying \(|\tau_R(q)|\le\min\{|q|,2R\}\), \(|\tau_R'|\le1\), and \(\tau_R(q)=q\) on \([-R,R]\). Oddness can be imposed but is not used in these estimates. Since \(|g|,|g'|\le1\),
\[
 |D(z,q)|\le(a+1)|q|,\qquad |\phi_\epsilon(z)|\le a|z|+a+2.
 \tag{R.4}
\]
At fixed cap these coordinate instructions are continuously differentiable and globally Lipschitz: the two partial derivatives of \(D\) are bounded by \(2\epsilon R\) and \(a+\epsilon\).

Use normalized finite inner products \(\langle u,v\rangle_n=u^Tv/n\), independent initialized hidden matrices with entries \(N(0,1/n)\), and independent first-layer rows of joint law \(N(0,\Gamma)\). The controlled program in this part has \(C_0=0\). Its population has three separate neuron probability spaces; an expectation of layer-\(\ell\) variables is taken in that layer's space. Initial matrix actions have their actual adjoints, and learned increments are rank-one operators \(u\otimes v:q\mapsto u\langle v,q\rangle\). There is no pairing of coordinates across distinct layers.

The following is the exact version of internal Lemma F required here. For a fixed finite program with finitely many independent normalized Gaussian matrices used in both orientations, interleaved with \(C^1\) globally Lipschitz coordinate instructions with bounded derivatives, independent iid root tuples with finite second moments, and causal empirical inner products, the joint empirical coordinate laws and second moments have a canonical Gaussian-source limit. An initialized forward call on \(h\) has the representation
\[
 \xi_h+\sum_v u_v E\partial_{\zeta_v}h,
 \tag{R.5}
\]
where \(u_v\) are its previously queried reverse inputs. An initialized reverse call on \(u\) has the representation
\[
 \zeta_u+\sum_v h_v E\partial_{\xi_v}u,
 \tag{R.6}
\]
where \(h_v\) are its already queried forward inputs, including those earlier in the same time step. Forward and reverse source covariances are the full second moments of the corresponding matrix inputs. Distinct source groups and independent roots are independent in the canonical representation. Formal differentiation freezes all deterministic coefficients and covariance parameters and treats every named source slot separately, including at singular covariance. The lemma includes extra independent Gaussian roots and joint convergence of finitely many programs sharing initialized matrices and roots, on common action spaces.

This version of Lemma F is an input, not a conclusion about arbitrary bounded operators. Its applicability to empirical contractions is also elementary once its fixed-coefficient assertion is available. Freeze finitely many contractions at their causally constructed limits. Convergence of preceding nodes makes the error of each contraction tend to zero. A finite induction through Lipschitz coordinate instructions, bounded matrix actions, and the rank-one inequality transfers the limit to the actual contractions. The same induction identifies convergent causal scalar feedback values; no derivatives of that feedback enter (R.5)–(R.6).

The affine hypothesis is that, at each fixed mesh under consideration, the actual finite-width affine Euler arrays satisfy
\[
 \max_{k,i}\|Z^{1,0}_{k,i}\|_n\le B,\qquad
 \max_k\{\|W^0_{2,k}\|_{\rm op},\|W^0_{3,k}\|_{\rm op},\|C^0_k\|_n\}
 \le B
 \tag{R.7}
\]
on events of probability tending to one. One bound \(B\) works for the controls and meshes used in the application. An available bound may be enlarged to supply slack. A continuous-flow bound alone does not assert stability of arbitrary coarse Euler meshes.

We will construct explicit finite constants \(\epsilon_*(a,B,S)>0\), \(A,M,K\) such that every actual program with \(0\le\epsilon\le\epsilon_*\) satisfies
\[
 |A^\ell_{kj}|\le Ah_j\quad(j<k),\qquad
 |B^\ell_{k\bullet}|_{\rm r}\le M,\quad\ell=2,3,
 \tag{R.8}
\]
\[
 \sup_{k,R}\bigl(\|C_k\|_p+\|q^2_k\|_p+\|q^1_k\|_p\bigr)
 \le K\sqrt p\qquad(p\ge2).
 \tag{R.9}
\]
The constants are independent of \(\Gamma\), the cap, the mesh size and number of points, and variation of the controls.

## R.2. Deriving the source system

The forward calculation is \(H^\ell_{k,i}=\phi_\epsilon(Z^\ell_{k,i})\), \(Z^2_{k,i}=W_{2,k}H^1_{k,i}\), \(Z^3_{k,i}=W_{3,k}H^2_{k,i}\). The backward calculation is
\[
 \delta^3_{k,i}=D(Z^3_{k,i},C_k),\quad
 q^2_{k,i}=W_{3,k}^T\delta^3_{k,i},\quad
 \delta^2_{k,i}=D(Z^2_{k,i},q^2_{k,i}),
\]
\[
 q^1_{k,i}=W_{2,k}^T\delta^2_{k,i},\quad
 \delta^1_{k,i}=D(Z^1_{k,i},q^1_{k,i}).
\]
The controlled raw Euler updates are
\[
 Z^1_{k+1}=Z^1_k+h_kP_k\delta^1_k,
\]
\[
 W_{\ell,k+1}=W_{\ell,k}
 +h_k\sum_i c_{k,i}\delta^\ell_{k,i}\otimes_n H^{\ell-1}_{k,i},
 \quad \ell=2,3,\qquad
 C_{k+1}=C_k+h_kc_k^TH^3_k.
 \tag{R.10}
\]
For normalized inputs the first equation is exactly the projection of \(w_{k+1}=w_k+h_k\sum_i c_{k,i}\delta^1_{k,i}x_i/d\).

Unrolling the matrix update produces a learned forward addition
\[
 \sum_{j<k,m}h_jc_{j,m}\delta^\ell_{j,m}
       \langle H^{\ell-1}_{j,m},H^{\ell-1}_{k,i}\rangle_n
\]
and a learned reverse addition
\[
 \sum_{j<k,m}h_jc_{j,m}H^{\ell-1}_{j,m}
       \langle\delta^\ell_{j,m},\delta^\ell_{k,i}\rangle_n.
\]
Apply (R.5) and (R.6) to the remaining initialized matrix calls, and pass the displayed contractions to their expectations. Their sum gives
\[
 (A^\ell_{kj})_{im}
 =E\partial_{\zeta^{\ell-1}_{j,m}}H^{\ell-1}_{k,i}
 +h_jc_{j,m}E[H^{\ell-1}_{k,i}H^{\ell-1}_{j,m}],\quad j<k,
 \tag{R.11}
\]
\[
 (B^\ell_{kj})_{im}
 =E\partial_{\xi^\ell_{j,m}}\delta^\ell_{k,i}
 +\mathbf1_{j<k}h_jc_{j,m}E[\delta^\ell_{k,i}\delta^\ell_{j,m}],
 \quad j\le k.
 \tag{R.12}
\]
There is no extra control factor in the response term: controls already appear on its derivative paths through parameter updates.

The four centered Gaussian groups have covariances
\[
 E[\xi^\ell_{k,i}\xi^\ell_{j,m}]
   =E[H^{\ell-1}_{k,i}H^{\ell-1}_{j,m}],\qquad
 E[\zeta^{\ell-1}_{k,i}\zeta^{\ell-1}_{j,m}]
   =E[\delta^\ell_{k,i}\delta^\ell_{j,m}],\quad\ell=2,3.
 \tag{R.13}
\]
All time/sample correlations are retained, including singularities and nonzero feature means. The groups are independent as in Lemma F; coordinates within a group are not made independent. The complete source equations are
\[
 Z^1_k=Z^1_0+\sum_{r<k}h_rP_r\delta^1_r,\qquad
 q^1_k=\zeta^1_k+\sum_{v\le k}B^2_{kv}H^1_v,
 \tag{R.14}
\]
\[
 Z^2_k=\xi^2_k+\sum_{r<k}A^2_{kr}\delta^2_r,\qquad
 q^2_k=\zeta^2_k+\sum_{v\le k}B^3_{kv}H^2_v,
 \tag{R.15}
\]
\[
 Z^3_k=\xi^3_k+\sum_{r<k}A^3_{kr}\delta^3_r,\qquad
 C_k=\sum_{r<k}h_rc_r^TH^3_r,
 \tag{R.16}
\]
with \(Z^1_0\sim N(0,\Gamma)\), \(C_0=0\), and the coordinate maps already specified.

At each time compute all layer-2 forward calls, all layer-3 forward calls, all layer-3 reverse calls, then all layer-2 reverse calls, and finally update parameters. Thus the row construction order is
\[
                         A^2_k,\quad A^3_k,\quad B^3_k,\quad B^2_k.
 \tag{R.17}
\]
Samples within one stage are treated together. Every covariance and response coefficient uses quantities already available in this order. No covariance inverse or differentiation along the Gaussian support is involved.

If a physical population trajectory supplies \(c_k=-r_k/\|r_k\|_1\) and \(h_k=\Delta t_k\|r_k\|_1\), these are deterministic causal numbers. They are frozen in (R.11)–(R.12), and the affine comparator uses those identical numbers. At a zero residual the physical update is zero and the step is omitted. Thus the normalized residual is never differentiated.

## R.3. Raw affine stability and the Gaussian probe

Put
\[
 b=2B,\qquad Q=100a^3b^3,\qquad E_0=e^{QS},\qquad T_0=QSE_0.
 \tag{R.18}
\]
Use the raw distance
\[
 d(\theta,\widetilde\theta)
 =\max_i\|Z^1_i-\widetilde Z^1_i\|_2
 +\|W_2-\widetilde W_2\|_{\rm op}
 +\|W_3-\widetilde W_3\|_{\rm op}
 +\|C-\widetilde C\|_2,
 \tag{R.19}
\]
with normalized finite norms at finite width. On the ball where each primal size is at most \(b\), affine propagation gives
\[
 \|H^1_i\|\le2ab,\quad\|H^2_i\|\le3a^2b^2,\quad\|H^3_i\|\le4a^3b^3,
\]
\[
 \delta^3_i=aC,\qquad \delta^2_i=a^2W_3^TC,\qquad
 \delta^1_i=a^3W_2^TW_3^TC.
 \tag{R.20}
\]
For the four component differences \(u,v,w,t\) in (R.19), subtraction gives
\[
 \|\Delta H^1_i\|\le au,\quad
 \|\Delta H^2_i\|\le a^2b(u+2v),\quad
 \|\Delta H^3_i\|\le a^3b^2(u+2v+3w),
\]
\[
 \|\Delta\delta^3_i\|\le at,\quad
 \|\Delta\delta^2_i\|\le a^2b(w+t),\quad
 \|\Delta\delta^1_i\|\le a^3b^2(v+w+t).
 \tag{R.21}
\]
The rank-one inequality
\[
 \|u\otimes v-\widetilde u\otimes\widetilde v\|
 \le\|u-\widetilde u\|\|v\|+\|\widetilde u\|\|v-\widetilde v\|
 \tag{R.22}
\]
bounds the four update-component Lipschitz constants by \(a^3b^2,2a^3b^2,3a^3b^2,3a^3b^2\). Their sum is at most \(Q\). Every query norm and query Lipschitz constant used below is also at most \(Q\), by (R.20)–(R.21) and the two matrix applications defining the incoming fields.

Insert additive errors after one chosen matrix-answer type, recomputing subsequent calls and parameter updates. Errors with norm at most \(e_j\) in each sample at time \(j\) change the affine raw field at a fixed raw state by at most \(\kappa e_j\), with the following constants.

| Answer type | Affected updates | \(\kappa\) |
|---|---|---:|
| \(Z^2\) | \(W_3,C\) | \(2a^2b\) |
| \(Z^3\) | \(C\) | \(a\) |
| \(q^2\) | \(Z^1,W_2\) | \(3a^2b\) |
| \(q^1\) | \(Z^1\) | \(a\) |

A \(Z^2\) error changes \(H^2\) by \(a e_j\), and each of the \(W_3,C\) updates by at most \(a^2b e_j\). A \(q^2\) error changes \(\delta^2\) by \(a e_j\), contributes at most \(2a^2b e_j\) to the \(W_2\) update and \(a^2b e_j\) to the first-layer update. The two other entries follow directly from their affine gates. Each \(\kappa\le Q\).

Take an independent iid standard Gaussian vector \(g_n\) in the selected answer population, and insert \(\eta\alpha_{j,i}g_n\) with deterministic \(|\alpha_{j,i}|\le1\). The same vector is reused at the chosen times and sample slots. Finite iteration of the comparison recurrence gives
\[
 d(\theta_k^\eta,\theta_k^0)\le QSE_0|\eta|\|g_n\|_n.
 \tag{R.23}
\]
When only time \(j\) is perturbed, replace \(S\) by \(h_j\): the sole forcing in the state update carries \(h_j\), and later factors have product at most \(E_0\). On (R.7) and \(\|g_n\|_n\le2\), choose \(2T_0|\eta|<B/2\). Induction gives (R.23) at each next node and keeps the perturbed state strictly within the ball of radius \(b\).

Apply this to the four source/output pairs
\[
 (\zeta^1,H^1_i),\quad(\zeta^2,H^2_i),\quad
 (\xi^2,\delta^2_i),\quad(\xi^3,\delta^3_i).
 \tag{R.24}
\]
For affine gates the indicated output has no direct current dependence on that answer perturbation at fixed raw state, so its difference is at most \(Q\) times (R.23).

At a fixed probe amplitude Lemma F, with its extra independent root, gives
\[
 \langle g_n,V_n^\eta\rangle_n\longrightarrow E[GV^\eta],
 \tag{R.25}
\]
where \(G\sim N(0,1)\) is independent of the canonical source groups. Freeze the perturbed program's deterministic coefficients. Every affine coordinate is affine in the roots and sources. If \(D_{j,i}(\eta)=\partial_{\mathrm{source}_{j,i}}V^\eta\), the only explicit appearances of \(G\) are the inserted additions at those slots. Hence
\[
 \partial_GV^\eta=\eta\sum_{j,i}\alpha_{j,i}D_{j,i}(\eta),\qquad
 E[GV^\eta]=\eta\sum_{j,i}\alpha_{j,i}D_{j,i}(\eta).
 \tag{R.26}
\]
The second identity follows by writing \(V^\eta=U+tG\), with \(U\) independent of \(G\), and using \(EG=0,EG^2=1\).

At this fixed mesh \(D_{j,i}(\eta)\to D_{j,i}(0)\). Indeed affine coordinate coefficients are polynomial functions of preceding coefficients; their second moments are polynomial in these coefficients and covariance entries; expected formal derivatives are deterministic affine coefficients. Finite induction in order (R.17) proves continuity without inverting covariance matrices.

Conditionally on the unperturbed network, \(\langle g_n,V_n^0\rangle_n\) is centered Gaussian with variance \(\|V_n^0\|_n^2/n\), which tends to zero. Cauchy–Schwarz and (R.23) bound the pairing of the difference, divided by \(|\eta|\), by \(Q^2SE_0\|g_n\|_n^2\). First send width to infinity at fixed nonzero amplitude using (R.25)–(R.26), and then send amplitude to zero by the preceding continuity. This gives
\[
 \left|\sum_{j,i}\alpha_{j,i}D_{j,i}(0)\right|\le Q^2SE_0.
 \tag{R.27}
\]
Choose the signs of this deterministic finite derivative row to obtain its absolute row sum. Restricting signs to one time yields a block bound \(Q^2h_jE_0\). This applies even to coincident or zero-variance source slots, since errors were inserted at separately named finite answer slots. No derivative/width-limit interchange or trace identification is required.

The learned blocks in (R.11)–(R.12) have norm at most \(Q^2h_j\), by Cauchy–Schwarz and \(\sum_i|c_{j,i}|\le1\). Conversion of a maximum of three full scalar output-row sums to a sum of maximum block norms costs at most three. Therefore
\[
 A_0=3Q^2(E_0+1),\qquad M_0=3SQ^2(E_0+1)
 \tag{R.28}
\]
give
\[
 |A^{\ell,0}_{kj}|\le A_0h_j,\qquad
 |B^{\ell,0}_{k\bullet}|_{\rm r}\le M_0,\qquad\ell=2,3.
 \tag{R.29}
\]
The affine current blocks \(B^{\ell,0}_{kk}\) vanish because the corresponding two backward outputs in (R.24) have no direct current forward-source derivative.

## R.4. Nonlinear primal comparison and source variances

On the same raw ball, (R.4) gives
\[
 \|H^1_i\|\le3ab,\quad\|H^2_i\|\le4a^2b^2,\quad
 \|H^3_i\|\le5a^3b^3,
\]
\[
 \|\delta^3_i\|\le2ab,\quad\|q^2_i\|\le2ab^2,\quad
 \|\delta^2_i\|\le4a^2b^2,\quad
 \|q^1_i\|\le4a^2b^3,\quad\|\delta^1_i\|\le8a^3b^3.
 \tag{R.30}
\]
At an identical raw state, the nonlinear forward differences from affine queries are at most
\[
                   2\epsilon,\quad3ab\epsilon,\quad4a^2b^2\epsilon
 \tag{R.31}
\]
in layers 1, 2, 3. The intermediate exact upper bounds are \(2(1+ab)\epsilon\) and \(2(1+ab+a^2b^2)\epsilon\); use \(ab\ge2\). The backward differences in \(\delta^3,q^2,\delta^2,q^1,\delta^1\) are bounded, respectively, by
\[
 b\epsilon,\quad b^2\epsilon,\quad3ab^2\epsilon,\quad
 3ab^3\epsilon,\quad7a^2b^3\epsilon.
 \tag{R.32}
\]
For example \(|D(z,q)-aq|\le\epsilon|q|\), so the middle delta difference is at most \(a b^2\epsilon+2ab^2\epsilon\), using the nonlinear incoming norm in (R.30).

Substituting (R.30)–(R.32) in (R.22) bounds the sum of the four raw-field differences by \(30a^3b^3\epsilon\le Q\epsilon\). Affine raw-field Lipschitzness yields, for identical initialization and controls,
\[
 d_{k+1}\le(1+Qh_k)d_k+Q\epsilon h_k,\qquad d_k\le T_0\epsilon.
 \tag{R.33}
\]
If \(\epsilon\le B/(2T_0)\), stopped induction gives this bound at the next node and keeps the nonlinear path at distance at least \(B/2\) from the boundary. Neither a nonlinear-field Lipschitz constant nor a cap enters this comparison.

Define
\[
 \sigma=Q,\qquad D_0=Q(1+T_0),\qquad m_0=2QD_0.
 \tag{R.34}
\]
Every nonlinear and affine query has norm at most \(Q\). Its same-state difference from (R.31)–(R.32), followed by the affine query Lipschitz bound, gives an actual coupled query difference at most \(D_0\epsilon\). At fixed mesh and cap Lemma F passes these finite-array comparisons to the actual population programs sharing initialized matrices and roots. No comparison of square roots of growing source covariances is used.

Equation (R.13) therefore bounds every scalar source variance by \(\sigma^2\), without any response estimate. For each learned moment,
\[
 |E[UV]-E[U^0V^0]|
 \le\|U-U^0\|_2\|V\|_2+\|U^0\|_2\|V-V^0\|_2
 \le m_0\epsilon.
 \tag{R.35}
\]
Retaining the column control weights gives learned forward-block differences at most \(m_0\epsilon h_j\) and learned backward-row differences at most \(m_0S\epsilon\).


## R.5. Coordinate moments on bounded coefficient prefixes

Fix
\[
                     A=A_0+1,\qquad M=M_0+1,\qquad d_a=a+1.
 \tag{R.36}
\]
Initially assume only that the rows needed for a particular construction prefix satisfy (R.8). Section R.9 closes this assumption stage by stage.

A centered scalar Gaussian of variance at most \(\sigma^2\) satisfies \(\|G\|_p\le2\sigma\sqrt p\) for \(p\ge2\): its Gaussian integral gives \(Ee^{G^2/(4\sigma^2)}\le\sqrt2\), and maximizing \(x^pe^{-x^2/(4\sigma^2)}\) gives the norm bound. The maximum of three such variables consequently has \(L^p\) norm at most \(6\sigma\sqrt p\), regardless of their dependence. The first-layer root has this bound too.

Introduce explicit finite constants
\[
 k_0=a+2+6a\sigma,
\]
\[
 K_1=(k_0+6a d_a\sigma S)e^{a d_a MS},\qquad
 K_2=(k_0+6a d_a A\sigma S)e^{a d_a AMS},
\]
\[
 K_C=k_0S e^{a d_a AS^2},\qquad
 K_{q1}=6\sigma+MK_1,\quad K_{q2}=6\sigma+MK_2,
\]
\[
                         K_q=1+K_C+K_{q1}+K_{q2}.
 \tag{R.37}
\]
For \(U^1_k=\max_{v\le k}\|H^1_v\|_p\), (R.14) and (R.4) yield
\[
 \|q^1_r\|_p\le6\sigma\sqrt p+MU^1_r,\qquad
 U^1_k\le(k_0+6a d_a\sigma S)\sqrt p+a d_a M\sum_{r<k}h_rU^1_r.
 \tag{R.38}
\]
The maximum here is of deterministic norms, not a random maximum over times. For \(U^2_k=\max_{v\le k}\|H^2_v\|_p\), (R.15) yields
\[
 \|q^2_r\|_p\le6\sigma\sqrt p+MU^2_r,\qquad
 U^2_k\le(k_0+6a d_a A\sigma S)\sqrt p+a d_a AM\sum_{r<k}h_rU^2_r.
 \tag{R.39}
\]
At the top,
\(\|H^3_k\|_p\le k_0\sqrt p+a d_a A\sum_{r<k}h_r\|C_r\|_p\).
Substituting this into the readout sum, \(V_k=\max_{v\le k}\|C_v\|_p\) satisfies
\[
                    V_k\le k_0S\sqrt p+a d_a AS\sum_{r<k}h_rV_r.
 \tag{R.40}
\]
For nonnegative sequences, finite iteration of \(x_k\le f+L\sum_{r<k}h_rx_r\) gives \(x_k\le f\prod_{r<k}(1+Lh_r)\le f e^{LS}\). Applying this to (R.38)–(R.40) proves
\[
 \|H^1_k\|_p\le K_1\sqrt p,\quad\|H^2_k\|_p\le K_2\sqrt p,\quad
 \|C_k\|_p\le K_C\sqrt p,
\]
\[
                     \|q^1_k\|_p\le K_{q1}\sqrt p,\qquad
                     \|q^2_k\|_p\le K_{q2}\sqrt p.
 \tag{R.41}
\]
Equations (R.14)–(R.16) and (R.4) then bound all preactivations, top features, and deltas by finite multiples of \(\sqrt p\).

For each population separately let \(Q_k\) denote its incoming-field maximum, respectively \(|q^1_k|_\infty,|q^2_k|_\infty,|C_k|\). Then \(\|Q_k\|_p\le K_q\sqrt p\). Set
\[
                            L_q^2=8\exp(1)K_q^2.
 \tag{R.42}
\]
Expanding the exponential and using \(m!\ge(m/\exp(1))^m\) gives
\[
 Ee^{Q_k^2/L_q^2}
 \le \sum_{m\ge0}\frac{K_q^{2m}(2m)^m}{L_q^{2m}m!}
 \le\sum_{m\ge0}4^{-m}<2.
 \tag{R.43}
\]
The \(m=0\) summand is one. The factorial inequality follows by bounding \(\sum_{j=1}^m\log j\) below by \(\int_1^m\log x\,dx\).

## R.6. Exact nonlinear derivative equations and integrability

At each layer use its incoming \(q\), with \(q=C\mathbf1\) at the top, and define
\[
 G_k=aI+\epsilon\operatorname{diag}(g(Z_k)),
\]
\[
 V_k=aI+\epsilon\operatorname{diag}(g(Z_k)\tau_R'(q_k)),\qquad
 L_k=\epsilon\operatorname{diag}(g'(Z_k)\tau_R(q_k)).
 \tag{R.44}
\]
Then
\[
 |G_k|,|V_k|\le d_a,\quad |G_k-aI|,|V_k-aI|\le\epsilon,\qquad
 |L_k|\le\epsilon Q_k.
 \tag{R.45}
\]
The cap derivative is included explicitly in \(V_k\).

For a bottom reverse source at time \(j\), let
\(J^1_{k,j}=\partial_{\zeta^1_j}Z^1_k\), a \(3\times3\) matrix. Differentiating (R.14) at fixed coefficient arrays gives exactly
\[
 J^1_{k,j}=\sum_{r<k}h_rP_r\left[
 L^1_rJ^1_{r,j}+V^1_r\left(
 I\mathbf1_{r=j}+\sum_{v\le r}B^2_{rv}G^1_vJ^1_{v,j}\right)\right].
 \tag{R.46}
\]
For a middle forward source set \(I_k^\xi=I\mathbf1_{k=j},I_k^\zeta=0\); for a middle reverse source interchange these assignments. Equation (R.15) gives
\[
 J^2_{k,j}=I_k^\xi+\sum_{r<k}A^2_{kr}\left[
 L^2_rJ^2_{r,j}+V^2_r\left(
 I_r^\zeta+\sum_{v\le r}B^3_{rv}G^2_vJ^2_{v,j}\right)\right].
 \tag{R.47}
\]
In both equations the feature derivative is \(G_kJ_k\).
For a top forward source put \(J^3_{k,j}=\partial_{\xi^3_j}Z^3_k\) and \(T_{k,j}=\partial_{\xi^3_j}C_k\), the latter a \(1\times3\) row. The exact equations are
\[
 J^3_{k,j}=I\mathbf1_{k=j}+\sum_{r<k}A^3_{kr}
                 (L^3_rJ^3_{r,j}+V^3_r\mathbf1T_{r,j}),
\]
\[
                     T_{k,j}=\sum_{r<k}h_rc_r^TG^3_rJ^3_{r,j}.
 \tag{R.48}
\]
The backward outputs have derivatives
\[
 \partial_{\xi^2_j}\delta^2_k
   =L^2_kJ^2_{k,j}+V^2_k\sum_{v\le k}B^3_{kv}G^2_vJ^2_{v,j},
\]
\[
 \partial_{\xi^3_j}\delta^3_k
   =L^3_kJ^3_{k,j}+V^3_k\mathbf1T_{k,j}.
 \tag{R.49}
\]
These retain all current terms.

Let
\[
 H=10d_a^2(1+A)(1+M)(1+S),\qquad
 \mathcal E_k=\exp\left(Hs_k+H\epsilon\sum_{r<k}h_rQ_r\right).
 \tag{R.50}
\]
Each equation uses \(Q_r\) in its own population.
For one bottom reverse-source block (R.46) gives
\[
 |J^1_{k,j}|\le d_a h_j+
 \sum_{r<k}h_r(\epsilon Q_r+d_a^2M)\max_{v\le r}|J^1_{v,j}|.
 \tag{R.51}
\]
For a middle reverse-source block the forcing is \(d_a A h_j\) and the coefficient is \(A(\epsilon Q_r+d_a^2M)\). For the whole middle forward-source row, summing (R.47) in \(j\) gives forcing one and the same coefficient. For the top row norms \(u_k=|J^3_{k\bullet}|_{\rm r}\), \(t_k=|T_{k\bullet}|_{\rm r}\), (R.48) gives
\[
 t_k\le d_a\sum_{r<k}h_ru_r,\qquad
 u_k\le1+\sum_{r<k}h_r(A\epsilon Q_r+d_a^2AS)
                                    \max_{v\le r}u_v.
 \tag{R.52}
\]
In the second inequality the inner readout sum is bounded by \(S\max_{v\le r}u_v\).

For a recursion \(x_k\le f+\sum_{r<k}h_r\ell_r\max_{v\le r}x_v\), its equality majorant is increasing and equals \(f\prod_{r<k}(1+h_r\ell_r)\). Induction and \(1+t\le e^t\) bound the original recursion by that product. The definition of \(H\) dominates every forcing prefactor and feedback coefficient in (R.51)–(R.52). Hence
\[
 |J^1_{k,j}|,\ |J^{2,\zeta}_{k,j}|\le Hh_j\mathcal E_k,\qquad
 |J^{2,\xi}_{k\bullet}|_{\rm r},\ |J^3_{k\bullet}|_{\rm r}
                                      \le H\mathcal E_k,
\]
\[
                         |T_{k\bullet}|_{\rm r}\le H^2\mathcal E_k.
 \tag{R.53}
\]
Feature derivatives are bounded by \(H^2\) times the same envelope and source-step factor. Equation (R.49) gives
\[
 |\partial_{\xi^\ell_\bullet}\delta^\ell_k|_{\rm r}
                  \le H^3(1+\epsilon Q_k)\mathcal E_k.
 \tag{R.54}
\]
The terminal multiplier is necessary: \(Q_k\) is absent from the sum defining \(\mathcal E_k\).

Convexity, without independence across times, gives
\[
 \exp\left(\theta\sum_{r<k}h_rQ_r\right)
 \le1-s_k/S+\sum_{r<k}(h_r/S)e^{\theta SQ_r}\qquad(\theta\ge0).
 \tag{R.55}
\]
The scalar inequality \(uQ\le Q^2/L_q^2+u^2L_q^2/4\) and (R.43) imply \(Ee^{uQ}\le2e^{u^2L_q^2/4}\). Consequently, for every fixed finite \(p\ge1\),
\[
 E\mathcal E_k^p\le2\exp(pHS+p^2H^2S^2L_q^2/4).
 \tag{R.56}
\]
Hölder controls the current multiplier too. In particular the explicit constant
\[
                     X=2(1+2K_q)\exp(HS+H^2S^2L_q^2)
 \tag{R.57}
\]
satisfies
\[
                    E\mathcal E_k\le X,\qquad
                    E[(1+Q_k)\mathcal E_k]\le X.
 \tag{R.58}
\]
Indeed apply (R.56) with \(p=2\), and
\(\|1+Q_k\|_2\le1+\sqrt2K_q\). The same calculation at higher exponents gives every fixed finite moment of \(\mathcal E_k\) and \((1+Q_k)\mathcal E_k\). No random time supremum occurs.

## R.7. Same-array derivative perturbation

Keep the deterministic arrays \(A,B\) fixed throughout this section. A superscript \({\rm af}\) means replacing \(G,V,L\) in (R.46)–(R.49) by \(aI,aI,0\) at these same arrays. It does not mean evaluation at the actual affine baseline arrays. These affine derivative solutions are deterministic and need no source coupling.

Subtract the middle affine equation from (R.47). The affine feedback is
\(a^2\sum_{r<k}A^2_{kr}\sum_{v\le r}B^3_{rv}(J_v-J_v^{\rm af})\).
The complete forcing is
\[
 \sum_{r<k}A^2_{kr}\left[
 (V_r-aI)I_r^\zeta+L_rJ_r
 +(V_r-aI)\sum_{v\le r}B^3_{rv}G_vJ_v
 +a\sum_{v\le r}B^3_{rv}(G_v-aI)J_v\right].
 \tag{R.59}
\]
For the bottom subtraction replace \(A^2_{kr}\) by \(h_rP_r\), \(B^3\) by \(B^2\), and take \(I_r^\zeta=I\mathbf1_{r=j}\); these substitutions in the displayed formula specify every term of that subtraction.

Let \(f=h_j\) for one reverse-source block, and \(f=1\) for a full forward-source row. Define
\[
                         W_k=1+\sum_{r<k}h_r(1+Q_r)\mathcal E_r.
 \tag{R.60}
\]
This is increasing. In the reverse-source case the first term of (R.59) occurs only at \(r=j\), with bound \(A\epsilon h_j\). The remaining derivatives vanish through time \(j\), and thereafter carry \(h_j\) by (R.53). Thus every contribution retains \(f\) for arbitrary unequal meshes. Using (R.45), (R.53), and \(\mathcal E_v\le\mathcal E_r\) for \(v\le r\), the total forcing is at most \(4H^4\epsilon fW_k\). For example the three nondirect coefficients are bounded by \(AH\), \(AMd_a H\), and \(AaMH\), all absorbed in \(4H^4\). The bottom has smaller coefficients since \(|P_r|\le1\le A\).

The affine feedback is bounded by \(H\sum_{r<k}h_r\max_{v\le r}|J_v-J_v^{\rm af}|\). Iteration with increasing forcing gives
\[
                    |J_k-J_k^{\rm af}|
                    \le4H^4 e^{HS}\epsilon fW_k.
 \tag{R.61}
\]
The notation denotes the relevant block or time-row norm. Passing to a feature derivative adds \((G_k-aI)J_k\), whose norm is at most \(H\epsilon f\mathcal E_k\).

The top subtraction consists of the exact equations
\[
 \Delta J_k=\sum_{r<k}A^3_{kr}
 [a\mathbf1\Delta T_r+(V_r-aI)\mathbf1T_r+L_rJ_r],
\]
\[
                  \Delta T_k=\sum_{r<k}h_rc_r^T
                                  [a\Delta J_r+(G_r-aI)J_r].
 \tag{R.62}
\]
Substitution of the second into the first bounds affine feedback by
\(a^2AS\sum_{r<k}h_r\max_{v\le r}|\Delta J_v|_{\rm r}\), which is at most the feedback used in (R.61). The direct remainder is bounded by \(A\epsilon\sum h_r(H^2+HQ_r)\mathcal E_r\). The additional remainder from substituting \((G-aI)J\) is at most \(aAS H\epsilon\sum h_r\mathcal E_r\). Their sum is below \(4H^4\epsilon W_k\). Thus (R.61) holds for top \(\Delta J\), with \(f=1\), and the second equation of (R.62) bounds \(\Delta T\).

Set
\[
                             D_1=20H^8e^{HS}.
 \tag{R.63}
\]
Using \(aS\le H\), (R.61)–(R.62) and feature multiplication show that each relevant preactivation, feature, or readout derivative difference is bounded by
\[
                         D_1\epsilon f(W_k+\mathcal E_k).
 \tag{R.64}
\]
For the middle backward output the exact derivative difference is
\[
 L_kJ_k+(V_k-aI)\sum_{v\le k}B^3_{kv}G_vJ_v
 +a\sum_{v\le k}B^3_{kv}(G_v-aI)J_v
 +a^2\sum_{v\le k}B^3_{kv}(J_v-J_v^{\rm af}).
 \tag{R.65}
\]
For the top output it is
\[
                 L_kJ_k+(V_k-aI)\mathbf1T_k+a\mathbf1\Delta T_k.
 \tag{R.66}
\]
The first terms have norm at most \(H\epsilon Q_k\mathcal E_k\) and retain the current returns. The other two direct middle terms sum to at most \(2H^3\epsilon\mathcal E_k\); the final middle term is at most \(a^2MD_1\epsilon(W_k+\mathcal E_k)\). The top remainder is bounded by the same common bound. Therefore
\[
 |\partial_{\xi^\ell_\bullet}\delta^\ell_k
     -\partial_{\xi^\ell_\bullet}\delta^{\ell,{\rm af}}_k|_{\rm r}
 \le10H^3D_1\epsilon[W_k+(1+Q_k)\mathcal E_k].
 \tag{R.67}
\]
Since \(EW_k\le1+SX\), (R.58) proves the expected derivative remainders with an explicit coefficient ready to absorb the learned-moment errors:
\[
             R_0=200H^{11}e^{HS}[1+(S+1)X]+m_0(1+S).
 \tag{R.68}
\]
Specifically, an expected feature derivative differs from its same-array affine derivative by at most \(R_0\epsilon h_j\) for one reverse-source block. The expected norm of a full backward derivative-row difference is at most \(R_0\epsilon\). Adding the learned forward or backward moment errors from (R.35) preserves these respective bounds, because the first summand of (R.68) already dominates all derivative remainders and its second summand dominates all moment errors.


## R.8. Deterministic coefficient stability

At arbitrary fixed bounded arrays denote the affine derivative of \(H^1_k\) with respect to \(\zeta^1_j\) by \(F_{k,j}\), of \(H^2_k\) with respect to \(\zeta^2_j\) by \(V^{\rm f}_{k,j}\), and of \(H^2_k\) with respect to \(\xi^2_j\) by \(U_{k,j}\). Use \(T_{k,j}\) for the affine derivative of \(C_k\) with respect to \(\xi^3_j\). The superscript distinguishes \(V^{\rm f}\) from the local diagonal gate matrix. Specializing the exact random derivative equations gives
\[
 F_{k,j}=a^2h_jP_j\mathbf1_{j<k}
       +a^2\sum_{r<k}h_rP_r\sum_{v\le r}B^2_{rv}F_{v,j},
 \tag{R.69}
\]
\[
 V^{\rm f}_{k,j}=a^2A^2_{kj}\mathbf1_{j<k}
       +a^2\sum_{r<k}A^2_{kr}\sum_{v\le r}B^3_{rv}V^{\rm f}_{v,j},
 \tag{R.70}
\]
\[
 U_{k,j}=aI\mathbf1_{k=j}
       +a^2\sum_{r<k}A^2_{kr}\sum_{v\le r}B^3_{rv}U_{v,j},
 \tag{R.71}
\]
\[
 T_{k,j}=ah_jc_j^T\mathbf1_{j<k}
       +a^2\sum_{r<k}h_rc_r^T\sum_{v<r}A^3_{rv}\mathbf1T_{v,j}.
 \tag{R.72}
\]
The last equation follows by substituting the top preactivation derivative
\(I\mathbf1_{k=j}+a\sum_{v<k}A^3_{kv}\mathbf1T_{v,j}\)
into the readout sum. The two affine backward outputs are \(a\mathbf1T_{k,j}\) and
\[
                             W_{k,j}=a\sum_{v\le k}B^3_{kv}U_{v,j}.
 \tag{R.73}
\]
The coefficient matrix \(A^2\) and scalar gain square \(a^2\) are distinct throughout these formulas.

Finite iteration gives explicit constants
\[
 K_F=a^2e^{a^2MS},\quad K_V=a^2Ae^{a^2AMS},\quad
 K_U=ae^{a^2AMS},\quad K_T=aSe^{a^2AS^2},
 \tag{R.74}
\]
such that
\[
 |F_{k,j}|\le K_Fh_j,\quad |V^{\rm f}_{k,j}|\le K_Vh_j,\quad
 |U_{k\bullet}|_{\rm r}\le K_U,\quad |T_{k\bullet}|_{\rm r}\le K_T.
 \tag{R.75}
\]
For \(F,V^{\rm f}\), the forcing prefactors are \(a^2h_j,a^2Ah_j\) and feedback coefficients \(a^2M,a^2AM\). For \(U\), the time-row forcing is \(a\) and its feedback coefficient \(a^2AM\). For \(T\), exchange the finite time sums in (R.72) to obtain \(t_k\le aS+a^2AS\sum_{v<k}h_vt_v\). Applying the finite-product identity to these four displayed scalar recursions proves (R.74).

Put a superscript 0 on these same deterministic systems at the actual affine baseline arrays. Combining (R.11)–(R.12), the same-array derivative comparison, and the learned moment comparison gives exact difference identities
\[
 \Delta A^2_{kj}=F_{k,j}-F^0_{k,j}+\eta^2_{kj},\qquad
 \Delta A^3_{kj}=V^{\rm f}_{k,j}-V^{\rm f,0}_{k,j}+\eta^3_{kj},
\]
\[
 \Delta B^3_{kj}=a\mathbf1(T_{k,j}-T^0_{k,j})+\nu^3_{kj},\qquad
 \Delta B^2_{kj}=W_{k,j}-W^0_{k,j}+\nu^2_{kj},
 \tag{R.76}
\]
where the quantities already bounded in Sections R.4 and R.7 satisfy
\[
                |\eta^\ell_{kj}|\le R_0\epsilon h_j,\qquad
                |\nu^\ell_{k\bullet}|_{\rm r}\le R_0\epsilon.
 \tag{R.77}
\]
These are derived remainders rather than assumptions on coefficient stability.

Define
\[
 \alpha^\ell_k=\max_{j<k}\frac{|\Delta A^\ell_{kj}|}{h_j},\qquad
 \beta^\ell_k=|\Delta B^\ell_{k\bullet}|_{\rm r},
\]
\[
                     E_k=\beta^2_k+\beta^3_k,\qquad
                     I_k=\sum_{r<k}h_rE_r.
 \tag{R.78}
\]
An empty maximum is zero. Each \(I_k\) uses only completed past rows and is nondecreasing.

For \(f^j_k=|F_{k,j}-F^0_{k,j}|/h_j\), subtract (R.69) and expand
\(B^2F-B^{2,0}F^0=\Delta B^2F+B^{2,0}\Delta F\).
The direct terms cancel because controls and steps are identical. Thus
\[
 f^j_k\le a^2K_F I_k+
                 a^2M_0\sum_{r<k}h_r\max_{v\le r}f^j_v.
 \tag{R.79}
\]
Finite iteration bounds the first term times \(e^{a^2M_0S}\). Set
\[
                         D_2=R_0+a^2K_Fe^{a^2M_0S}.
 \tag{R.80}
\]
Equations (R.76)–(R.77) give \(\alpha^2_k\le D_2(\epsilon+I_k)\).

For \(v^j_k=|V^{\rm f}_{k,j}-V^{\rm f,0}_{k,j}|/h_j\), expand the three factors in (R.70) as
\[
 A^2B^3V^{\rm f}-A^{2,0}B^{3,0}V^{\rm f,0}
 =\Delta A^2B^3V^{\rm f}
  +A^{2,0}\Delta B^3V^{\rm f}
  +A^{2,0}B^{3,0}\Delta V^{\rm f}.
\]
Using \(|\Delta A^2_{kr}|\le\alpha^2_kh_r\) and (R.75) gives
\[
 v^j_k\le a^2(1+MSK_V)\alpha^2_k+a^2A_0K_VI_k
           +a^2A_0M_0\sum_{r<k}h_r\max_{v\le r}v^j_v.
 \tag{R.81}
\]
The first feedback term, for example, is at most
\(a^2\alpha^2_k\sum_{r<k}h_rMK_V\).
It is a forcing term containing a current row already bounded at the preceding stage. Define
\[
 C_V=[a^2(1+MSK_V)D_2+a^2A_0K_V]e^{a^2A_0M_0S},
 \qquad D_3=R_0+C_V.
 \tag{R.82}
\]
Since \(\epsilon+I_r\le\epsilon+I_k\) for \(r\le k\), product iteration of (R.81) and (R.76) gives
\(\alpha^3_k\le D_3(\epsilon+I_k)\).

For \(t_k=|T_{k\bullet}-T^0_{k\bullet}|_{\rm r}\), the direct forcing in (R.72) cancels. Expanding its two factors yields
\[
 t_k\le a^2SK_T\sum_{r<k}h_r\alpha^3_r
                  +a^2A_0S\sum_{v<k}h_vt_v.
 \tag{R.83}
\]
Indeed
\(\sum_{r<k}h_r\sum_{v<r}h_vt_v
=\sum_{v<k}h_vt_v\sum_{v<r<k}h_r\le S\sum_{v<k}h_vt_v\).
Put
\[
                 C_T=a^2S^2K_TD_3e^{a^2A_0S^2},\qquad E_3=R_0+aC_T.
 \tag{R.84}
\]
Use \(\sum_{r<k}h_r(\epsilon+I_r)\le S(\epsilon+I_k)\) and product iteration in (R.83). Equations (R.76)–(R.77) then give
\(\beta^3_k\le E_3(\epsilon+I_k)\).
There is no current \(\alpha^3_k\) in the affine equation (R.83). The nonlinear remainder uses that current row only after it was bounded in the preceding stage.

For \(u_k=|U_{k\bullet}-U^0_{k\bullet}|_{\rm r}\), expansion of all three factors in (R.71) gives
\[
 u_k\le a^2MSK_U\alpha^2_k+a^2A_0K_UI_k
           +a^2A_0M_0\sum_{r<k}h_r\max_{v\le r}u_v.
 \tag{R.85}
\]
The direct source terms cancel. Define
\[
                   C_U=[a^2MSK_UD_2+a^2A_0K_U]e^{a^2A_0M_0S}.
 \tag{R.86}
\]
Then \(u_k\le C_U(\epsilon+I_k)\). Finally the exact current-row product (R.73) has expansion
\(a\Delta B^3_k U+aB^{3,0}_k(U-U^0)\), so
\[
 |W_{k\bullet}-W^0_{k\bullet}|_{\rm r}
             \le aK_U\beta^3_k+aM_0\max_{v\le k}u_v.
 \tag{R.87}
\]
The current \(B^3_k\) was just bounded; current \(U_k\) uses current \(A^2_k\) and only past \(B^3\). Set
\[
 E_2=R_0+aK_UE_3+aM_0C_U,\qquad
                  K_*=2\max\{1,D_2,D_3,E_2,E_3\}.
 \tag{R.88}
\]
The four successive bounds are
\[
 \alpha^2_k,\alpha^3_k,\beta^2_k,\beta^3_k\le K_*(\epsilon+I_k),
 \qquad E_k\le K_*\epsilon+K_*\sum_{r<k}h_rE_r.
 \tag{R.89}
\]
Every constant is now a specified finite function of \((a,B,S)\).

## R.9. Chronological closure and explicit amplitude selection

Take
\[
 \epsilon_*(a,B,S)=
 \min\left\{1,\frac{B}{2T_0},
                  \frac{1}{2K_*\exp(K_*S)}\right\}.
 \tag{R.90}
\]
The finite constant chain is (R.18), (R.28), (R.34), (R.36)–(R.37), (R.42), (R.50), (R.57), (R.68), (R.74), and (R.80)–(R.88). Thus the number is positive and chosen before the mesh, controls, cap, or covariance.

The prefix assumptions close by induction through the actual query stages, rather than a simultaneous assumption on unknown current rows. Suppose all four coefficient rows at times \(r<k\) obey the bounds \((A,M)\) and
\[
                       E_r\le K_*\epsilon\prod_{v<r}(1+K_*h_v).
 \tag{R.91}
\]
The telescoping product identity gives
\[
 \epsilon+I_k
 \le\epsilon\left[1+\sum_{r<k}K_*h_r
                         \prod_{v<r}(1+K_*h_v)\right]
 =\epsilon\prod_{r<k}(1+K_*h_r)
 \le\epsilon e^{K_*S}.
 \tag{R.92}
\]

First construct \(A^2_k\). Its bottom coordinates and reverse-source derivative paths use only \(q^1_r,B^2_r\) with \(r<k\). Equations (R.38), (R.46), and (R.59) therefore establish its remainder before any bound on a new backward row is needed. Equations (R.79)–(R.80) and (R.90)–(R.92) give \(\alpha^2_k\le1/2\), so
\(|A^2_{kj}|\le(A_0+1/2)h_j<Ah_j\).

Next construct \(A^3_k\). The just-bounded \(A^2_k\) constructs \(Z^2_k,H^2_k\), and their reverse-source derivative paths use \(q^2_r,B^3_r\) only for \(r<k\). Equations (R.39), (R.47), and (R.59) give the remainder, and (R.81)–(R.82) yield \(\alpha^3_k\le1/2\). No bound on current \(q^2_k\) was used.

Then construct \(B^3_k\). The available \(C_k,Z^3_k\), their moments, and their derivative paths use \(A^3\) through the current time, now bounded, and no backward rows. Equations (R.40), (R.48), and (R.62), (R.66) provide this remainder; (R.83)–(R.84) give \(\beta^3_k\le1/2\). Hence its row norm is less than \(M\). This new row defines \(q^2_k\), which is bounded from its already constructed middle features by (R.39).

Finally construct \(B^2_k\). Current \(q^2_k,B^3_k\) now satisfy all bounds required for (R.49), (R.65). Equations (R.85)–(R.88) give \(\beta^2_k\le1/2\), hence its row norm is less than \(M\). Only now is current \(q^1_k\) defined and bounded by (R.38). The second inequality in (R.89), with (R.92), proves (R.91) at the new time. All learned moments at every stage were already bounded independently by Section R.4.

At \(k=0\) the forward rows are empty. Because \(C_0=0\), the top delta and its forward-source derivatives vanish; the source covariance of \(\zeta^2_0\) and the coefficient \(B^3_0\) are therefore zero. Thus \(q^2_0=\delta^2_0=0\), and the same computation gives \(B^2_0=0,q^1_0=0\). This starts the induction while retaining all separately named formal source arguments at zero variance.

For completeness the actual current-return blocks are
\[
                 (B^3_{kk})_{ij}=\mathbf1_{i=j}E(L^3_k)_{ii},
 \tag{R.93}
\]
\[
 (B^2_{kk})_{ij}=\mathbf1_{i=j}E(L^2_k)_{ii}
       +(B^3_{kk})_{ij}E[(V^2_k)_{ii}(G^2_k)_{jj}].
 \tag{R.94}
\]
Indeed \(\partial_{\xi^3_k}Z^3_k=I\) and \(\partial_{\xi^3_k}C_k=0\), giving (R.93). In the middle, \(\partial_{\xi^2_k}Z^2_k=I\) and \(\partial_{\xi^2_k}q^2_k=B^3_{kk}G^2_k\); the chain rule gives (R.94), including its column index \(j\) on \(G^2_k\). Equations (R.45) and (R.41) bound both current blocks by a constant times \(\epsilon\). They are diagonal for this explicit Euler schedule, while earlier blocks can be full. Their off-diagonal zeros are consequences of these formal derivatives, not consequences of sample independence. No current block was omitted or inverted.

The induction proves (R.8) and the quantitative stability estimate
\[
 \max_{\ell,k,j<k}\frac{|A^\ell_{kj}-A^{\ell,0}_{kj}|}{h_j}
 +\max_{\ell,k}|B^\ell_{k\bullet}-B^{\ell,0}_{k\bullet}|_{\rm r}
                  \le2K_*e^{K_*S}\epsilon.
 \tag{R.95}
\]
The coordinate argument now applies to the whole program. Thus (R.9) holds with \(K=K_q\). The same proof bounds all displayed forward fields and deltas by finite multiples of \(\sqrt p\). Equations (R.53)–(R.58) additionally give absolute expected response bounds
\[
 E|\partial_{\zeta^{\ell-1}_j}H^{\ell-1}_k|
       \le H^2Xh_j,\qquad
 E|\partial_{\xi^\ell_\bullet}\delta^\ell_k|_{\rm r}
       \le H^3X,\qquad\ell=2,3.
 \tag{R.96}
\]

The only advanced theorem used in this part is internal Lemma F, in the precise form stated in Section R.1. The remaining estimates use finite induction, elementary Gaussian integration, Cauchy–Schwarz, Hölder, the displayed rank-one inequality, finite products, and convexity. The affine hypothesis must be verified in the global-control argument. This part's conclusions concern every finite cap; their transfer to continuous trajectories and removal of caps belong to the subsequent dynamical argument.

## Part G. Uniform geometry, a bounded residual clock, and global dynamics

### G.1. Separation controls the augmented input Gram

**Lemma G.1.** Under (M.1),
\[
              \Gamma+\mathbf1\mathbf1^T\succeq(\delta^2/4)I_3.
                                                               \tag{G.1}
\]
**Proof.** Put \(u_i=x_i/\sqrt d\). For a coefficient vector \(q\),
\[
 q^T(\Gamma+\mathbf1\mathbf1^T)q
             =(\sum_iq_i)^2+\|\sum_iq_iu_i\|^2 .
                                                               \tag{G.2}
\]
If the nonzero coefficients have one sign, the first term is
at least \(\sum_iq_i^2\), which suffices since \(\delta\le2\).
Otherwise, change the overall sign and permute the three indices
to write \(q=(\alpha_1,\alpha_2,-b)\), where
\(\alpha_1,\alpha_2\ge0\), \(A=\alpha_1+\alpha_2>0\), and \(b>0\).
Define
\[
 D=\{\alpha_1(1-u_1^Tu_3)+\alpha_2(1-u_2^Tu_3)\}/A
                         \in[\delta,2].
\]
The projection of \(\sum q_i u_i\) onto the unit vector \(u_3\)
is \((1-D)A-b\). Therefore (G.2) is at least
\[
 (A-b)^2+((1-D)A-b)^2
 =\begin{pmatrix}A&b\end{pmatrix}
   \begin{pmatrix}1+(1-D)^2&-(2-D)\\-(2-D)&2\end{pmatrix}
   \begin{pmatrix}A\\b\end{pmatrix}.
\]
The positive matrix has determinant \(D^2\) and trace
\(D^2-2D+4\le4\). Its smaller eigenvalue is at least its
determinant divided by its trace, hence at least \(\delta^2/4\).
Finally \(A^2+b^2\ge\alpha_1^2+\alpha_2^2+b^2\). This proves
(G.1), including all singular cases of \(\Gamma\). \(\square\)

For scale, the power \(\delta^2\) is sharp. The unit vectors
\[
 u_1=(1-\delta,\sqrt{2\delta-\delta^2}),\quad
 u_2=(1-\delta,-\sqrt{2\delta-\delta^2}),\quad u_3=(1,0)
\]
satisfy the pairwise condition for \(0<\delta\le3/2\).
For \(q=(1,1,-2+\delta)\), the quotient in (G.2) divided by
\(\|q\|^2\) is \(2\delta^2/(6-4\delta+\delta^2)\).
Only the lower bound (G.1), not this example, is used below.

### G.2. Initial features and a positive nonlinear margin

Let \(Z=(Z_1,Z_2,Z_3)\) be centered Gaussian, with a common
positive marginal variance \(v\) and covariance \(Q\).
Write \(Z=Q^{1/2}G_3\), with \(G_3\) a standard Gaussian
three-vector; a singular square root is allowed. Gaussian
integration by parts on the independent coordinates of \(G_3\)
shows that the orthogonal projection in \(L^2\) of
\(\phi(Z_i)=a+aZ_i+e\arctan Z_i\) onto constants and Gaussian
linear functions is
\[
                    a+b_vZ_i,\qquad
 b_v=a+e\,E[Z_i\arctan Z_i]/v\ge a.                         \tag{G.3}
\]
The residuals are orthogonal to both terms of every such
projection, and their Gram is positive semidefinite. Thus
\[
 E[\phi(Z)\phi(Z)^T]\succeq a^2\mathbf1\mathbf1^T+a^2Q.
                                                               \tag{G.4}
\]
All initialized sample marginals at a given layer have the
same variance, by (M.3), equal input norms, and the fresh
Gaussian forward call at that layer. With \(Q_0=\Gamma\),
iteration of (G.4) gives
\[
 K^4(0)=Q_3\succeq a^6\Gamma+(a^6+a^4+a^2)\mathbf1\mathbf1^T
                           \succeq\lambda a^6I_3,
 \qquad \lambda=\delta^2/4.                                \tag{G.5}
\]
The first preactivation variance is one. Later scalar
preactivation variances are at least one because
\(|az+e\arctan z|\ge a|z|\) for \(a\ge1,e\ge0\).

For a variable with positive variance, minimization over an
intercept and slope gives
\[
 \mathcal R(Z)=\operatorname{Var}(\arctan Z)
       -\frac{\operatorname{Cov}(Z,\arctan Z)^2}
                         {\operatorname{Var}(Z)}.             \tag{G.6}
\]
For \(G\sim N(0,1)\), \(\mathcal R(\sigma G)>0\) whenever
\(\sigma>0\): otherwise a zero \(L^2\) residual would make
arctangent affine almost everywhere under a full-support
Gaussian law, and then everywhere by continuity. Its derivative
is not constant. The expression is continuous in \(\sigma>0\)
by coupling with the same \(G\) and dominated convergence.
Symmetry and (G.6) also give
\[
 \mathcal R(\sigma G)
 =E[\arctan(\sigma G)^2]-(E[G\arctan(\sigma G)])^2
 \longrightarrow\frac{\pi^2}{4}(1-2/\pi)>0.                  \tag{G.7}
\]
For the second expectation use the integrable dominator
\(\pi|G|/2\); the limit uses \(E|G|=\sqrt{2/\pi}\).
Continuity on compact positive intervals and the positive
limit in (G.7) prove the strict positivity of \(\eta_*\)
defined in (M.21).

We will use a quantitative stability fact. Suppose
\(\operatorname{sd}(Z_0)\ge1\),
\(\mathcal R(Z_0)\ge\eta_*\), and \(\|Z-Z_0\|_2\le t_*\).
Centering is an orthogonal projection, so standard deviation
is 1-Lipschitz in \(L^2\) and \(\operatorname{sd}(Z)\ge1/2\).
The optimal arctangent regression slope at \(Z\) has magnitude
at most \((\pi/2)/\operatorname{sd}(Z)\le\pi\).
Testing its affine predictor at \(Z_0\), using the triangle
inequality and the 1-Lipschitz property of arctangent, gives
\[
 \sqrt{\mathcal R(Z_0)}
       \le\sqrt{\mathcal R(Z)}+(1+\pi)\|Z-Z_0\|_2.
\]
The definition of \(t_*\) in (M.21) therefore implies
\[
                         \mathcal R(Z)\ge\eta_*/4.          \tag{G.8}
\]
No Gaussian assumption on \(Z\) is needed in this implication.

### G.3. Controlled flows and all positive Euler meshes

Fix a smooth even function \(\chi:\mathbb R\to[0,1]\) equal
to one on \([-1,1]\) and zero outside \([-2,2]\).
For \(R>0\), put
\(\tau_R(q)=R\int_0^{q/R}\chi(v)\,dv\).
It is smooth, odd, 1-Lipschitz, equal to \(q\) on \([-R,R]\),
and satisfies \(|\tau_R(q)|\le\min(|q|,2R)\).
Use the auxiliary gate
\[
 D_R(z,q)=aq+e(1+z^2)^{-1}\tau_R(q)                         \tag{G.9}
\]
at all backward levels, leaving every forward activation
unchanged. The three auxiliary backward fields are
\[
 \delta_i^3=D_R(z_i^3,C),\quad
 q_i^2=B^*\delta_i^3,\quad \delta_i^2=D_R(z_i^2,q_i^2),\quad
 q_i^1=A^*\delta_i^2,\quad \delta_i^1=D_R(z_i^1,q_i^1).
                                                               \tag{G.10}
\]
The map \(D_R\) has bounded continuous first derivatives:
\[
 |(D_R)_q|\le a+e,\qquad |(D_R)_z|\le2eR .
                                                               \tag{G.11}
\]

For a measurable deterministic control \(c:[0,S]\to\mathbb R^3\)
with \(\|c(s)\|_1\le1\), consider the raw controlled equation
\[
 w'=d^{-1}\sum_i c_i\delta_i^1x_i,\quad
 A'=\sum_i c_i\delta_i^2\otimes h_i^1,\quad
 B'=\sum_i c_i\delta_i^3\otimes h_i^2,\quad
 C'=\sum_i c_i h_i^3.                                      \tag{G.12}
\]
Primes denote this control time, not physical time. We also use
its exact Euler updates on any positive mesh, with a control
vector of \(\ell^1\) norm at most one at each node. The affine
comparison sets \(e=0\) and uses the identical mesh and controls.

Let
\[
 D=\sqrt d\|w-w_0\|_2+\|A-A_0\|_{\rm HS}+\|B-B_0\|_{\rm HS}.
                                                               \tag{G.13}
\]
On \(D\le1\), current action norms are at most 11. Population
first projections have norms at most 2; finite initial
projection norms at most 2 give current norms at most 3.
For \(0\le e\le1\), \(|\phi(z)|\le a(3+|z|)\) and
\(|D_R(z,q)|\le2a|q|\). Direct forward and reverse propagation
therefore gives, also in finite normalized norms,
\[
 \begin{array}{c|ccc}
  &1&2&3\\ \hline
  \|h_i^\ell\|&6a&70a^2&800a^3\\
  \|\delta_i^\ell\|&
            968a^3\|C\|&44a^2\|C\|&2a\|C\|
 \end{array} .                                               \tag{G.14}
\]
For example the first backward factor is
\((2a)11(2a)11(2a)=968a^3\).
The three hidden raw speeds in (G.12) sum to at most
\[
 (968+44\cdot6+2\cdot70)a^3\|C\|
                         \le1400a^3\|C\|,
 \qquad \|C'\|\le800a^3.                                   \tag{G.15}
\]
Since the population and the affine comparator have \(C_0=0\),
integration before an exit yields
\[
 \|C(s)\|\le800a^3s,\qquad
 D(s)\le560000a^6s^2\le10^6a^6s^2.                         \tag{G.16}
\]
For Euler, \(\|C_k\|\le800a^3s_k\), and the same estimate follows
from \(\sum_{j<k}h_js_j=(s_k^2-\sum_{j<k}h_j^2)/2\).
This also rules out a first discrete overshoot: every preceding
node satisfies the stopped estimates, and their sum bounds the
alleged first exiting node strictly inside the stopping ball.

Choose \(a,S\) as in (M.21), and write
\[
 C_S=9600/(\lambda a^3),\qquad
 D_S=1.44\cdot10^8/(\lambda^2a^6).
                                                               \tag{G.17}
\]
Since \(a^6\ge6.4\cdot10^{19}\lambda^{-3}\) and
\(0<\lambda\le9/16\), these constants obey
\[
 D_S<\min\{1/2,\lambda/(3\cdot10^7)\},\quad C_S<1,\quad
                  6\cdot10^6C_S^2<\lambda/4.               \tag{G.18}
\]
The second lower bound on \(a\) in (M.21) gives
\[
             615a^2D_S\le0.08856\,t_*<t_* .                \tag{G.19}
\]
Thus every controlled prefix of duration at most \(S\)
stays in these bounds. At fixed \(R\), (G.11), forward
Lipschitzness and bounded bilinear actions give a raw field
bounded and locally Lipschitz on primal balls, uniformly in
control. The integral map is a contraction on a sufficiently
short interval, also for measurable \(c\), because its
Lipschitz bound is uniform in \(s\). Its fixed point is an
absolutely continuous strong controlled path. A strong
endpoint and the same construction continue it through \(S\).
For continuous autonomous physical controls the path is \(C^1\).

These estimates verify the affine finite-array hypothesis of
the response theorem in Part R with \(B=12\). Indeed, at finite
width the initial projection norms are at most 2 and the
initialized action norms at most 10 with probability tending
to one. Set only the auxiliary affine comparator's initial
readout to zero. Bounds (G.14)--(G.18) control its first
projections, current operators, and readout by 12 at every
node, on every admitted positive control mesh. Each finite
operator increment is bounded directly by its rank-one
update lengths. No convergence of trained finite operator
norms is assumed.

### G.4. Readout coercivity dominates the capped hidden contribution

For a controlled state, compare features with their own
initialized features, using the same activation and actions.
The raw hidden distance (G.13) gives
\[
 \begin{split}
 \|\Delta h_i^1\|&\le2aD,\\
 \|\Delta z_i^2\|&\le 6aD+10(2aD)=26aD,\\
 \|\Delta h_i^2\|&\le52a^2D,\\
 \|\Delta z_i^3\|&\le70a^2D+10(52a^2D)\le615a^2D,\\
 \|\Delta h_i^3\|&\le1500a^3D .
 \end{split}                                                \tag{G.20}
\]
Let \(F_3:\mathbb R^3\to H_3\) have columns \(h_i^3\).
Then \(K^4=F_3^*F_3\),
\(\|F_3\|,\|F_3(0)\|\le800\sqrt3a^3\), and
\(\|\Delta F_3\|\le1500\sqrt3a^3D\). Consequently
\[
 \|K^4-K^4(0)\|\le7.2\cdot10^6a^6D,\qquad
                         K^4\succeq(3/4)\lambda a^6I_3.
                                                               \tag{G.21}
\]

Let \(J_h:\mathcal X_h\to\mathbb R^3\) be the true hidden
prediction differential, where \(\mathcal X_h\) is the
three-block hidden raw Hilbert increment space.
Let \(U_{h,R}:\mathbb R^3\to\mathcal X_h\) map coefficients to
the hidden directions in (G.12).
The same bounds (G.14)--(G.15) hold for the true gate
\((a+e/(1+z^2))q\), so
\[
 \|J_h\|,\|U_{h,R}\|\le\sqrt3\,1400a^3\|C\|,\qquad
 \|J_hU_{h,R}\|\le6\cdot10^6a^6C_S^2\le\lambda a^6/4 .
                                                               \tag{G.22}
\]
Part F proves the strong forward chain rule used here.
In the physical capped system the readout direction is
unchanged, while the hidden direction is \(-U_{h,R}r\).
Thus the exact residual equation is
\[
               \dot r=-(K^4+J_hU_{h,R})r.                   \tag{G.23}
\]
The second operator in parentheses need not be symmetric or
positive. Its absolute quadratic contribution is bounded by
(G.22). Combining with (G.21) proves
\[
 \frac{d}{dt}\|r\|_2\le-\frac{\lambda a^6}{2}\|r\|_2
                      \quad\hbox{when }\|r\|_2>0.
\]
At a zero residual all four raw directions vanish, so the
physical path stays stationary there by fixed-cap uniqueness.
Since \(r(0)=-y\),
\[
 \|r(t)\|_2\le\sqrt3e^{-\lambda a^6t/2},\qquad
 \int_0^\infty\|r(t)\|_1dt
          \le\sqrt3\int_0^\infty\|r(t)\|_2dt
          \le\frac6{\lambda a^6}=\frac S2.                  \tag{G.24}
\]

This argument is initially stopped before
\(s(t)=\int_0^t\|r(v)\|_1dv\) reaches \(S\).
Where the residual is nonzero, reparametrization gives
precisely (G.12) with \(c=-r/\|r\|_1\).
Consequently all the preceding controlled bounds are valid
before that stop. Equation (G.24) excludes the stop with
strict slack. Fixed-cap local Lipschitzness, bounded primal
states and bounded raw speeds give a strongly Cauchy limit
at any finite physical endpoint, from which local existence
continues the solution. Every population cap flow is
therefore global, with bounds uniform in its cap. The proof
has not assumed that capped dynamics dissipate energy as
a gradient flow.

### G.5. One response threshold for every physical horizon

Apply the response theorem of Part R at the fixed numerical
arguments \(a,B=12,S\). Choose \(e\le e_*(a,12,S)\).
For a fixed-cap physical Euler program, rewrite each step by
\[
 h_j=\Delta t_j\|r_j\|_1,\qquad
 c_j=-r_j/\|r_j\|_1,                                       \tag{G.25}
\]
omitting zero-residual steps. This reproduces every actual
raw update exactly. In the population program these are
deterministic causal contractions. Fixed-cap strong Euler
convergence and the strict bound \(S/2\) in (G.24) imply
\(\sum_jh_j<S\) on all sufficiently fine physical meshes
on each fixed finite horizon.

The response theorem permits every such positive effective
mesh and every such control sequence. Its affine comparator
uses the identical frozen values in (G.25). Source partial
derivatives never differentiate those controls.
The resulting bounds pass through fixed-cap mesh convergence
by truncated second-moment inequalities. For one finite
constant \(K=K(a,12,S)\),
\[
 \sup_{R>0,t\ge0}
   \{\|C_R(t)\|_p+\|q_R^2(t)\|_p+\|q_R^1(t)\|_p\}
                       \le K\sqrt p,\qquad p\ge2.          \tag{G.26}
\]
Here sample triples use the maximum coordinate norm; the
fixed sample factor is absorbed into \(K\).
The selection of \(e\), and the bound \(K\), do not depend
on the physical horizon.

The moment bound implies a Gaussian \(L^2\) tail bound.
For instance, taking \(p\) proportional to \(R^2/K^2\) in
Markov's inequality gives
\(\Pr(|Q|>R)\le C\exp(-cR^2/K^2)\) for large \(R\).
Integration of this tail, or the same estimate with two
additional powers, yields
\[
       \|Q\mathbf1_{\{|Q|>R\}}\|_2\le C_0e^{-c_0R^2}.
                                                               \tag{G.27}
\]
The constants apply to all incoming fields in (G.26),
uniformly over caps and physical times.

### G.6. Application of the internal cap-transfer argument

Part V proves the following precise implication from the facts
already obtained: global canonical fixed-cap physical paths
with bounded primal quantities and the uniform reference
tails (G.27) have a unique strong uncut limit on every finite
interval, including convergence of raw directions and HS
increments. Its proof uses the asymmetric estimate
\[
 \begin{split}
 |D_{R'}(z_A,q_A)-D_R(z_B,q_B)|
 \le{}&(a+e)|q_A-q_B|+2eR|z_A-z_B|\\
       &+2e|q_B|\mathbf1_{\{|q_B|>R\}},
                         \qquad R'\ge R,                  \tag{G.28}
 \end{split}
\]
where \(R'=\infty\) denotes the true gate. Only the reference
\((z_B,q_B)\) needs tails. Sequential backward substitution
gives a single linear loss in \(R\), and the resulting
compact-time error is \(C_T\exp(C_TR-c_0R^2)\).
Part V includes that derivation, the actual three-residual
coefficient comparison, and the strong forward and
backward passages; it is not an external invocation.

Consequently the cap paths have one consistent uncut
\(C^1\) limit on all integer horizons and hence on
\([0,\infty)\). Their canonical spaces may be chosen
simultaneously by the countable construction in Part F.
Uniqueness against bounded-primal strong competitors and
unique continuation from reached states follow from the
same reference-only estimate, also proved in Part V.
The limiting equations are the autonomous physical equations
(M.12). The scalar prediction differentiation in Part F
identifies their vector field as the raw gradient of \(L\).
Bounds (G.17)--(G.24) pass to this limit.

The fixed-cap finite-program convergence, actual finite GF
and raw GD transfer, true kernels, velocities, generated
probes, and path-space limits are proved in Part V under
exactly these bounds. Thus it supplies all assertions
(M.16)--(M.18), with the stated limit order.

Finally, each initial scalar preactivation is Gaussian with
standard deviation at least one. Equations (G.19)--(G.20)
and the stability estimate (G.8), first for cap paths and
then for their strong limit, give
\(\mathcal R(z_i^\ell(t))\ge\eta_*/4\) for every \(t,i,\ell\).
Absorb \(a(1+Z)\) into the free affine predictor to obtain
\[
 \inf_{\alpha,\beta}E[\phi(Z)-\alpha-\beta Z]^2
                              =e^2\mathcal R(Z).
\]
This proves (M.19). Part N supplies the remaining
initial-acceleration and changing-kernel assertions.

# Part V. Finite raw dynamics, full kernels, hidden velocities, and path laws

We prove the finite-width assertions for three samples and three hidden layers with the fixed activation
\[
 \phi(z)=a(1+z)+e\arctan z,\qquad a\ge1,\quad 0<e\le1,
 \qquad d_\phi=\phi'.
\]
The constants \(a,e\) are those already selected in Parts R and G, independently of width and physical horizon. The proof identifies only fixed finite Gaussian transcripts; mesh refinement, cap removal, and the raw step \(n^{-2}\) are handled by deterministic comparisons.

## V.1. Definitions and exact internal inputs

Let \(x_i\in\mathbb R^d\), \(i=1,2,3\), satisfy \(\|x_i\|^2=d\), let \(y_i\in\{-1,1\}\), and put \(\Gamma_{ij}=x_i^Tx_j/d\). All finite vector norms are normalized RMS, \(\|v\|_n^2=n^{-1}\sum_\alpha v_\alpha^2\); matrix operator and Frobenius norms are ordinary. The rank-one action \(u\otimes_n v=uv^T/n\) has Frobenius norm \(\|u\|_n\|v\|_n\). Population spaces \(H_\ell=L^2(\Omega_\ell,\mu_\ell)\) are separate for the three layers, and \(u\otimes v:q\mapsto u\langle v,q\rangle\). Every inner product belongs to its indicated layer.

The state is \(\theta=(w,A,B,C)\), with \(A:H_1\to H_2\), \(B:H_2\to H_3\); \(A-A_0,B-B_0\) are Hilbert--Schmidt. For differences and directions use
\[
 \|\Delta\theta\|_{\mathcal X}
 =\sqrt d\,\|\Delta w\|_2+\|\Delta A\|_{\rm HS}
             +\|\Delta B\|_{\rm HS}+\|\Delta C\|_2.              \tag{V.1}
\]
At finite width the first term is \(\sqrt{d/n}\|\Delta W^1\|_F\), the two matrix terms are ordinary Frobenius norms, and the readout term is RMS. These compare states on a common population space or at the same width, never operators at unidentified different widths.

For a smooth odd clip with
\[
 |\tau_R(q)|\le\min(|q|,2R),\quad |\tau_R'|\le1,\qquad
 \tau_R(q)=q\quad(|q|\le R),
\]
write
\[
 D_R(z,q)=aq+e(1+z^2)^{-1}\tau_R(q),\qquad
 D_\infty(z,q)=d_\phi(z)q.                                    \tag{V.2}
\]
Thus
\[
 |d_\phi|\le a+e,\quad |d_\phi'|\le ce,\quad
 |D_R(z,q)|\le(a+e)|q|,\quad |(D_R)_q|\le a+e,\quad
 |(D_R)_z|\le ceR.                                           \tag{V.3}
\]
The forward fields are
\[
 z_i^1=w\cdot x_i,\quad h_i^\ell=\phi(z_i^\ell),\quad
 z_i^2=Ah_i^1,\quad z_i^3=Bh_i^2,\quad
 f_i=\langle C,h_i^3\rangle,\quad p_i=y_i-f_i.
\]
The capped backward fields are
\[
 \delta_{R,i}^3=D_R(z_i^3,C),\quad q_{R,i}^2=B^*\delta_{R,i}^3,
 \quad\delta_{R,i}^2=D_R(z_i^2,q_{R,i}^2),
\]
\[
 q_{R,i}^1=A^*\delta_{R,i}^2,\qquad
 \delta_{R,i}^1=D_R(z_i^1,q_{R,i}^1).
\]
Their physical raw field is
\[
 F_{R,w}=d^{-1}\sum_i p_i\delta_{R,i}^1x_i,\quad
 F_{R,A}=\sum_i p_i\delta_{R,i}^2\otimes h_i^1,\quad
 F_{R,B}=\sum_i p_i\delta_{R,i}^3\otimes h_i^2,\quad
 F_{R,C}=\sum_i p_i h_i^3.                                    \tag{V.4}
\]
We reserve \(b_i^\ell=\delta_{\infty,i}^\ell\) for true backward fields, including when evaluated as observations at a capped state.

The finite initialization is exactly
\[
 W^1_{\alpha j}\sim N(0,1/d),\quad
 A_{\alpha\beta},B_{\alpha\beta}\sim N(0,1/n),\quad
 C_\alpha\sim N(0,n^{-2}),                                    \tag{V.5}
\]
independently. Raw GD is simultaneous Euler for \(F_\infty\), with \(\eta_n=n^{-2}\), followed by linear interpolation of the raw parameters. Hidden fields are recomputed from that interpolation. Its raw direction on \([k\eta_n,(k+1)\eta_n)\) is \(F_\infty(\theta_n(k\eta_n))\). At nodes take the right direction, except for the terminal-left convention at a terminal mesh node of an observation interval.

Here are the precise prior conclusions used.

**F: fixed programs and common actions.** For a fixed finite program formed from independent Gaussian roots, the two independent initialized matrices reused in both orientations, \(C^1\) coordinate maps with bounded continuous first derivatives, and causal scalar first/second-moment contractions, every finite within-layer joint empirical tuple converges along the full width sequence in probability in \(\mathcal W_2\). Each oriented matrix has a centered Gaussian source family, with covariance equal to the Gram of its actual inputs. The four oriented families are mutually independent and independent of original scalar roots, while all same-family time/sample covariances are retained. A forward query of an initial matrix on input \(u\) has scalar answer
\[
 \xi_u+\sum_v E[\partial_{\zeta_v}u]\,v,                       \tag{V.6}
\]
where \(v\) ranges over earlier opposite-orientation inputs and \(\zeta_v\) is the named source of their answers; the reverse rule interchanges sides. Derivatives hold all deterministic coefficients, contractions and covariances fixed. Named arguments remain distinct under singular covariance, and unavailable-source derivatives vanish.

The statement remains valid after adjoining finitely many independent Gaussian roots and bounded-derivative query perturbations. At a fixed transcript its source construction, expected first source derivatives, and second moments are continuous under such perturbations with uniformly bounded coordinate first derivatives; the finite chronological proof uses Gaussian covariance square roots, including at rank drops. A countable collection of programs admits common generated \(L^2\) spaces on which \(A_0,B_0\) extend to bounded actions, with norms at most 10 and actual adjoints. Strong \(L^2\) limits of generated inputs have the corresponding action limits. At finite width, \(\|A_0\|_{\rm op},\|B_0\|_{\rm op}\le10\) with probability tending to one.

This lemma has been proved in Part F by finite Gaussian conditioning, independent-query regularization, and Gaussian integration by parts. It asserts neither growing-transcript identification nor an \(L^p\to L^p\) matrix-action bound.

**R and G: global capped bounds and incoming moments.** The selected \(a,e\) give global population physical capped trajectories \(\theta_R\) with common initialization \(C_0=0\) and common initialized actions. Their first projection norms, current action norms, and readout norms have one bound independent of cap and physical time. On every fixed \([0,T]\), their raw directions have a cap-independent bound. For one \(K_*\), independent of \(R,t,p\),
\[
 \sup_{R<\infty,t\ge0,i}
  \{\|C_R(t)\|_p+\|q^2_{R,i}(t)\|_p+\|q^1_{R,i}(t)\|_p\}
                   \le K_*\sqrt p,\qquad p\ge2.               \tag{V.7}
\]
The moment estimate concerns the actual nonlinear incoming fields. It is passed from controlled Euler programs to physical capped flows after freezing each causal physical coefficient in source derivatives; no derivative of a normalized residual is used. The controlled residual-clock bound in Part G makes the constant independent of physical horizon. Only the displayed conclusions of R and G are used below.

## V.2. Raw stability, population cap removal, and uniqueness

On a bounded primal ball, \(\phi\)'s Lipschitz bound and bounded actions give
\[
 \sum_{\ell,i}(\|z_i^\ell-\bar z_i^\ell\|_2+\|h_i^\ell-\bar h_i^\ell\|_2)
       +\sum_i|p_i-\bar p_i|
                \le K\|\theta-\bar\theta\|_{\mathcal X}.       \tag{V.8}
\]
For an upper layer use \(Ah-\bar A\bar h=(A-\bar A)h+\bar A(h-\bar h)\), and for the residual use Cauchy--Schwarz on \(\langle C,h\rangle-\langle\bar C,\bar h\rangle\). Also
\[
 \|u\otimes v-\bar u\otimes\bar v\|_{\rm HS}
 \le\|u-\bar u\|_2\|v\|_2+\|\bar u\|_2\|v-\bar v\|_2.         \tag{V.9}
\]
Successive backward substitution using (V.3) bounds \(F_R\) independently of \(R\) on that ball. At fixed cap it is Lipschitz in \(\mathcal X\), with constant \(K(1+eR)\) independent of width.

More precisely, if \(R'\ge R\), including \(R'=\infty\), then
\[
 |D_{R'}(z,q)-D_R(\bar z,\bar q)|
 \le(a+e)|q-\bar q|+ceR|z-\bar z|
                   +2e|\bar q|\mathbf1_{\{|\bar q|>R\}}.       \tag{V.10}
\]
First change \(q\) to \(\bar q\) inside \(D_{R'}\). The remainder is
\[
 e[(1+z^2)^{-1}-(1+\bar z^2)^{-1}]\tau_R(\bar q)
 +e(1+z^2)^{-1}[\tau_{R'}(\bar q)-\tau_R(\bar q)].
\]
The derivative of \(z\mapsto(1+z^2)^{-1}\) is bounded; \(|\tau_R|\le2R\); and the two clips agree when \(|\bar q|\le R\), while both have absolute value at most \(|\bar q|\). This proves (V.10).

Apply (V.10) successively through the three backward gates. An earlier incoming discrepancy is multiplied only by bounded actions and \(a+e\); a new factor \(R\) multiplies a new forward discrepancy, already controlled by (V.8). Thus only one cap factor occurs:
\[
 \|F_{R'}(\theta)-F_R(\bar\theta)\|_{\mathcal X}
 \le K(1+eR)\|\theta-\bar\theta\|_{\mathcal X}
       +Ke\sum_{Q\in\mathscr Q_R(\bar\theta)}
                   \|Q\mathbf1_{\{|Q|>R\}}\|_2,               \tag{V.11}
\]
where \(\mathscr Q_R=\{C,q^2_{R,i},q^1_{R,i}:1\le i\le3\}\). The sum of backward-field discrepancies satisfies the same bound. Physical residual feedback causes no new cap factor: split \(p_i\delta_i-\bar p_i\bar\delta_i\), then use (V.8), bounded primal quantities and (V.9). The tails in (V.11) belong only to the reference.

For \(Q\) in (V.7), and \(p\ge2\),
\[
 E[Q^2\mathbf1_{\{|Q|>u\}}]\le u^{2-p}E|Q|^p
                  \le u^2(K_*\sqrt p/u)^p.
\]
Choose \(p=(u/(3K_*))^2\ge2\), absorb the prefactor into a smaller exponential rate, and take square roots. Hence
\[
 \sup_{R,t,Q}\|Q\mathbf1_{\{|Q|>u\}}\|_2\le K e^{-cu^2}
                              \quad(u\ge u_0).               \tag{V.12}
\]
No independence of a Gaussian source and a learned shift is needed here.

Integrate (V.11) between two population caps, and use Gronwall:
\[
 \sup_{t\le T}\|\theta_{R'}(t)-\theta_R(t)\|_{\mathcal X}
                      \le K_Te^{K_TR-cR^2}.                  \tag{V.13}
\]
Indeed an inequality \(E(t)\le \epsilon t+L\int_0^tE(s)ds\) gives \(E(t)\le\epsilon t e^{Lt}\) by iterating its integral form. Substitution in (V.11) gives a vanishing bound of the same form, after changing constants, for raw directions and backward fields.

The cap paths and their derivatives are uniformly Cauchy on \([0,T]\). Their limits satisfy \(\theta(t)=\theta_0+\int_0^tV(s)ds\), so \(\theta\in C^1\), \(\dot\theta=V\). Apply (V.11) with the limit state on its left, a cap reference on its right and \(R'=\infty\); (V.12)--(V.13) identify \(V=F_\infty(\theta)\). Bounded multipliers ensure all uncut backward fields are \(L^2\). Integer caps and integer horizons suffice for one countable common-action construction, and the limits agree on overlaps.

Any bounded-primal strong uncut competitor with the same initialization can be compared against \(\theta_R\) by the same estimate. Its bounds may change \(K_T\), but no tails of that competitor are required, so (V.13) still tends to zero. This proves uniqueness. At a reached time \(t_0\), the initial discrepancy from the cap reference already satisfies (V.13); multiplication by another \(e^{K_TR}\) still leaves a vanishing bound. The global trajectory supplies continuation, and its continuation is unique among the stated competitors. No local existence theorem on arbitrary uncut \(L^2\) states is invoked.

## V.3. Fixed-cap source rows from nonlinear Gaussian probes

Fix \(R,T\). Constants in V.3--V.7 may depend on \(R,T,a,e\) and the fixed data, but not on width, mesh, source covariance conditioning, or a moment exponent. Let \(0=t_0<\cdots<t_N=T\), \(h_j=t_{j+1}-t_j\). All sufficiently fine population Euler meshes lie in a fixed enlarged primal ball: this follows from the fixed-cap Lipschitz property, the bounded cap path, and the raw Euler estimate in V.6, whose proof uses no source or velocity bound.

Suppress the subscript \(R\) on capped fields in this section. Freeze the causal \(p_{j,b}=y_b-f_b(\theta_j)\), all other scalar contractions, response coefficients, and covariances in formal derivatives. Exact rank unrolling and F give
\[
 z^1_{k,i}=z^1_{0,i}+\sum_{j<k,b}h_jp_{j,b}\Gamma_{ib}\delta^1_{j,b},
 \qquad C_k=\sum_{j<k,b}h_jp_{j,b}h^3_{j,b},                 \tag{V.14}
\]
\[
 z^\ell_{k,i}=\xi^\ell_{k,i}
                   +\sum_{j<k,b}\mathsf A^\ell_{ki,jb}\delta^\ell_{j,b},
 \qquad
 q^{\ell-1}_{k,i}=\zeta^{\ell-1}_{k,i}
                   +\sum_{j\le k,b}\mathsf D^\ell_{ki,jb}h^{\ell-1}_{j,b},
                                                               \tag{V.15}
\]
for \(\ell=2,3\), with
\[
 \mathsf A^\ell_{ki,jb}
 =E_{\ell-1}\partial_{\zeta^{\ell-1}_{j,b}}h^{\ell-1}_{k,i}
      +h_jp_{j,b}E_{\ell-1}[h^{\ell-1}_{k,i}h^{\ell-1}_{j,b}], \tag{V.16}
\]
\[
 \mathsf D^\ell_{ki,jb}
 =E_\ell\partial_{\xi^\ell_{j,b}}\delta^\ell_{k,i}
      +\mathbf1_{\{j<k\}}h_jp_{j,b}E_\ell[\delta^\ell_{k,i}\delta^\ell_{j,b}].
                                                               \tag{V.17}
\]
Every source variance is the squared norm of its actual initial-matrix input, and is bounded by the primal ball; also \(\sum_b|p_{j,b}|\le K\).

Choose one oriented answer family and a fresh standard Gaussian vector \(g\) in its answer population. Add \(\varepsilon\alpha_{j,b}g\), \(|\alpha_{j,b}|\le1\), at selected answer slots, and recompute all subsequent finite residuals and updates. Lipschitz stability on a larger primal ball gives
\[
 E_{k+1}\le(1+Kh_k)E_k+Kh_k|\varepsilon|\|g\|_n.             \tag{V.18}
\]
Forcing every time gives \(E_k\le K|\varepsilon|\|g\|_n\); forcing only time \(j\) gives \(E_k\le Kh_j|\varepsilon|\|g\|_n\) for \(k>j\). A primary query has the same bounds, with no \(h_j\) for a current answer. The constants include all three recomputed residuals. On \(\|g\|_n\le2\), sufficiently small fixed \(|\varepsilon|\) keeps the perturbed program in the larger ball by first-exit induction. The required finite primal event follows directly from the fixed-mesh primary law and exact update lengths, as established in V.7; it does not require the source-row bounds now being proved.

At fixed mesh and \(\varepsilon\), F gives
\[
 \langle g,V_n^\varepsilon\rangle_n\longrightarrow E[GV^\varepsilon].
\]
In its scalar construction \(G\) is independent of the original roots and source families. The coefficients depend on \(\varepsilon\), but are deterministic. With them frozen, the only explicit occurrences of \(G\) are the answer additions. Thus
\[
 E[GV^\varepsilon]
 =E[\partial_GV^\varepsilon]
 =\varepsilon\sum_{j,b}\alpha_{j,b}
                              E[\partial_{\eta_{j,b}}V^\varepsilon]. \tag{V.19}
\]
For this integration by parts, condition on all other roots and sources. At a fixed finite transcript the scalar expression is Lipschitz in its named Gaussian arguments with a finite deterministic constant, since primary coordinate derivatives are bounded. It has at most linear growth in \(G\), bounded \(G\)-derivative, and a vanishing Gaussian boundary term. Those facts justify both the conditional integral and subsequent expectation.

At this fixed mesh, \(E\partial_\eta V^\varepsilon\to E\partial_\eta V^0\). To verify the continuity premise, induct chronologically: next covariances and learned contractions are second moments of earlier inputs; covariance-square-root coupling passes their \(L^2\) limits, including singular ones. The scalar first derivatives are continuous functions of the preceding finite coefficient list and Gaussian arguments. On a compact neighborhood of that list, bounded coordinate derivatives give deterministic bounds for its finitely many formal derivatives. Dominated convergence passes the next expected derivative; residual contractions pass as continuous inner products. There is no covariance derivative or inverse.

Conditionally on the original unperturbed network, \(\langle g,V_n^0\rangle_n\) is centered Gaussian of variance \(\|V_n^0\|_n^2/n\), hence tends to zero on the bounded-program event. Cauchy--Schwarz and (V.18)--(V.19), first sending width to infinity and then \(\varepsilon\to0\), prove
\[
 \left|\sum_{j,b}\alpha_{j,b}E\partial_{\eta_{j,b}}V_k\right|\le K.
                                                               \tag{V.20}
\]
Choose deterministic signs of the expected derivatives for the absolute expected row. A single strictly past insertion gives \(Kh_j\). Cauchy--Schwarz bounds the learned contractions in (V.16)--(V.17), so
\[
 |\mathsf A^\ell_{ki,jb}|\le Kh_j,\quad
 |\mathsf D^\ell_{ki,jb}|\le Kh_j\ (j<k),\qquad
 |\mathsf D^\ell_{ki,kb}|\le K.                              \tag{V.21}
\]
This has not equated \(|E\partial V|\) and \(E|\partial V|\).

Both current transpose returns are retained. Put
\(a^\ell_{k,i}=(D_R)_z(z^\ell_{k,i},m^\ell_{k,i})\) and
\(v^\ell_{k,i}=(D_R)_q(z^\ell_{k,i},m^\ell_{k,i})\), where
\(m^1=q^1,m^2=q^2,m^3=C\). Then
\[
 \mathsf D^3_{ki,kb}=\mathbf1_{\{i=b\}}Ea^3_{k,i},\qquad
 \mathsf D^2_{ki,kb}=\mathbf1_{\{i=b\}}Ea^2_{k,i}
       +\mathsf D^3_{ki,kb}E[v^2_{k,i}d_\phi(z^2_{k,b})].      \tag{V.22}
\]
Here \(C_k\) and learned forward corrections use strictly past times, and a current forward preactivation contains its own current source with coefficient one. Differentiate the top gate, then the returned current middle gate to obtain (V.22), with all three sample coordinates distinct formal arguments even at singular covariance.

## V.4. Pointwise absolute derivative rows and primary moments

For a scalar field in one population, let
\[
 \mathcal R(F)=\sum_{\eta\ {\rm in\ that\ population}}|\partial_\eta F|, \tag{V.23}
\]
including every primary source through the final mesh time: \(\zeta^1\) in layer 1, \((\xi^2,\zeta^2)\) in layer 2, \(\xi^3\) in layer 3. Future derivatives vanish. Root derivatives could be included at the cost of a constant term. All coefficients are frozen.

Write \(Z^\ell=\mathcal R(z^\ell)\), \(H^\ell=\mathcal R(h^\ell)\),
\(B^\ell=\mathcal R(\delta^\ell)\), \(Q^s=\mathcal R(q^s)\), and
\(C^\partial=\mathcal R(C)\). The coordinate chain rule, (V.14)--(V.15), and (V.21) give pointwise
\[
\begin{aligned}
 Z^1_{k,i}&\le K\sum_{j<k}h_j\sum_bB^1_{j,b},\\
 Z^\ell_{k,i}&\le1+K\sum_{j<k}h_j\sum_bB^\ell_{j,b}\quad(\ell=2,3),\\
 C^\partial_k&\le K\sum_{j<k}h_j\sum_bH^3_{j,b},\\
 H^\ell_{k,i}&\le(a+e)Z^\ell_{k,i},\\
 Q^s_{k,i}&\le1+K\sum_bH^s_{k,b}
                   +K\sum_{j<k}h_j\sum_bH^s_{j,b}\quad(s=1,2),\\
 B^s_{k,i}&\le ceRZ^s_{k,i}+(a+e)Q^s_{k,i}\quad(s=1,2),\\
 B^3_{k,i}&\le ceRZ^3_{k,i}+(a+e)C^\partial_k .
\end{aligned}                                                    \tag{V.24}
\]
Every same-time term in a transpose line is a forward field already determined at that time, so no same-time system needs inversion.

Let \(U_k\) be the maximum of \(C_k^\partial\) and the nine \(Z^\ell_{k,i}\). The last four lines bound each remaining field by \(K(1+U_k+\sum_{j<k}h_jU_j)\). Substitution into the first lines and
\[
 \sum_{j<k}h_j\sum_{r<j}h_rU_r
 =\sum_{r<k}h_rU_r\sum_{r<j<k}h_j
 \le T\sum_{r<k}h_rU_r
\]
give \(U_k\le K+K\sum_{j<k}h_jU_j\). Induction gives
\(U_k\le K\prod_{j<k}(1+Kh_j)\le Ke^{KT}\). Returning to all lines proves
\[
 \mathcal R(F_{k,i})\le K                                    \tag{V.25}
\]
for every primary scalar field. This is a pathwise bound on the absolute derivative row.

The same reduction bounds moments. Replace seminorms by \(L^p\) norms; direct Gaussian sources and first roots have norm at most \(K\sqrt p\); use
\(\|\phi(Z)\|_p\le K+(a+e)\|Z\|_p\) and
\(\|D_R(Z,Q)\|_p\le(a+e)\|Q\|_p\), then Minkowski in the finite sums. Thus
\[
 \sup_{\pi,k,i}\|F^\pi_{k,i}\|_p\le K\sqrt p,\qquad p\ge2,     \tag{V.26}
\]
for all primary fields and \(C\). No independence among time sources is required by Minkowski, and no matrix \(L^p\)-operator bound is used.

## V.5. Appended hidden-velocity queries and their truncations

At an Euler node evaluate instantaneous preactivation and feature velocities in the raw direction \(F_R(\theta_k)\):
\[
 P^1_{k,i}=\sum_b p_{k,b}\Gamma_{ib}\delta^1_{k,b},\qquad
 U^\ell_{k,i}=d_\phi(z^\ell_{k,i})P^\ell_{k,i},                \tag{V.27}
\]
\[
 P^2_{k,i}=\sum_b p_{k,b}\delta^2_{k,b}
                    E_1[h^1_{k,b}h^1_{k,i}]+J^2_{k,i},
 \qquad J^2_{k,i}=A_kU^1_{k,i},                              \tag{V.28}
\]
\[
 P^3_{k,i}=\sum_b p_{k,b}\delta^3_{k,b}
                    E_2[h^2_{k,b}h^2_{k,i}]+J^3_{k,i},
 \qquad J^3_{k,i}=B_kU^2_{k,i}.                              \tag{V.29}
\]
The feature derivative is the true \(d_\phi\), not a capped backward gate.

Append, after the complete primary transcript, all \(A_0U^1_{k,i}\) observations, then all \(B_0U^2_{k,i}\), and add learned rank increments explicitly. They do not feed training. Source derivatives of a time-\(k\) input in later named sources vanish despite this appended order. The source formulas, justified by truncation below, are
\[
 J^\ell_{k,i}=\gamma^\ell_{k,i}
                +\sum_{j\le k,b}\mathsf E^\ell_{ki,jb}\delta^\ell_{j,b},
 \qquad\ell=2,3,                                            \tag{V.30}
\]
\[
 \mathsf E^\ell_{ki,jb}
 =E_{\ell-1}\partial_{\zeta^{\ell-1}_{j,b}}U^{\ell-1}_{k,i}
  +\mathbf1_{\{j<k\}}h_jp_{j,b}
                    E_{\ell-1}[h^{\ell-1}_{j,b}U^{\ell-1}_{k,i}].     \tag{V.31}
\]
The new forward source \(\gamma^\ell\) has variance \(\|U^{\ell-1}_{k,i}\|_2^2\); its covariance with every forward observation is the inner product of their inputs. It is a new named argument. It can be correlated with old sources of the same forward family; the opposite family remains independent.

From (V.25), freezing \(p\) and contractions,
\[
 \mathcal R(P^1_{k,i})\le K,\qquad
 \mathcal R(U^1_{k,i})
 \le |d_\phi'(z^1_{k,i})P^1_{k,i}|\mathcal R(z^1_{k,i})
                      +(a+e)\mathcal R(P^1_{k,i})
 \le K(1+|P^1_{k,i}|).                                      \tag{V.32}
\]
Thus the expected absolute derivative row in (V.31) for \(\ell=2\) is bounded by \(K\), using (V.26). Its learned row is bounded by Cauchy--Schwarz and \(\sum_jh_j=T\). The variance of \(\gamma^2\) is bounded directly by the \(L^2\) norm in (V.27). Source formula (V.30) and Minkowski yield
\[
 \sum_{j\le k,b}|\mathsf E^2_{ki,jb}|\le K,\qquad
 \|J^2_{k,i}\|_p+\|P^2_{k,i}\|_p+\|U^2_{k,i}\|_p\le K\sqrt p. \tag{V.33}
\]
Differentiate (V.30) for \(J^2\) only in layer-2 primary transpose sources \(\zeta^2\). Hold coefficients and the new named forward source \(\gamma^2\) fixed; its formal \(\zeta^2\) derivative is zero, including at singular covariance. Then (V.25), (V.33) give
\[
 \sum_{j,b}|\partial_{\zeta^2_{j,b}}P^2_{k,i}|\le K,\qquad
 \sum_{j,b}|\partial_{\zeta^2_{j,b}}U^2_{k,i}|
                                  \le K(1+|P^2_{k,i}|).     \tag{V.34}
\]
A second use of (V.31) proves
\[
 \sum_{j\le k,b}|\mathsf E^3_{ki,jb}|\le K,\qquad
 \sup_{\pi,k,i,\ell}(\|P^\ell_{k,i}\|_p+\|U^\ell_{k,i}\|_p)
                                  \le K\sqrt p.             \tag{V.35}
\]

We justify this reasoning in the required order. The product map
\((z,P)\mapsto d_\phi(z)P\) has an unbounded \(z\)-derivative and cannot be directly fed to F. Replace it by \(d_\phi(z)\tau_M(P)\). At each fixed \(M\) the coordinate first derivatives are bounded. Its formal derivative is
\[
 \partial_\eta[d_\phi(Z)\tau_M(P)]
 =d_\phi'(Z)\tau_M(P)\partial_\eta Z
                  +d_\phi(Z)\tau_M'(P)\partial_\eta P.       \tag{V.36}
\]
For the bottom query its absolute derivative row is dominated independently of \(M\) by \(K(1+|P^1|)\), integrable by primary bound (V.26). Thus the first-action row estimates and moments are first proved for each truncated action with constants independent of \(M\). Pointwise \(\tau_M(P)\to P\), \(\tau_M'(P)\to1\), and dominated convergence identifies every expected derivative in (V.31).

The empirical passage uses only second moments. If a coupling has \((z_n,p_n)\to(z,p)\) in \(L^2\), then
\[
 \|d_\phi(z_n)p_n-d_\phi(z)p\|_2
 \le(a+e)\|p_n-p\|_2+\|[d_\phi(z_n)-d_\phi(z)]p\|_2\to0.      \tag{V.37}
\]
For the last term, bound the part \(|p|\le L\) by \(ceL\|z_n-z\|_2\) and the rest by \(2(a+e)\|p\mathbf1_{\{|p|>L\}}\|_2\); send \(n\to\infty\), then \(L\to\infty\). Positive-part tails are 1-Lipschitz in \(L^2\), and
\[
 |p|\mathbf1_{\{|p|>L\}}\le2(|p|-L/2)_+.
\]
Hence primary joint \(\mathcal W_2\) convergence makes the empirical bottom clipping error vanish in the iterated width then \(M\) limit. The matrix norm bound transfers it to the actual finite action; common-action continuity transfers it to the population action. Learned contractions converge in \(L^2\), and source covariances converge as input second moments. Covariance-square-root coupling passes the entire finite scalar formula. This proves (V.30)--(V.33) for the first untruncated action and its joint law with the primary transcript.

For the second action, retain an inner clip \(M\) in the first action and an outer clip \(N\) in \(d_\phi(z^2)P^2\). At fixed \(M,N\) the original F applies. As \(M\to\infty\), the first action coefficients converge; its primary \(\zeta^2\) derivative rows obey (V.25), and its new forward source has formal derivative zero. Thus the rows of \(P^2_M\) converge and stay bounded. At fixed \(N\), (V.36) passes the outer expected derivative limits. The \(L^2\) input/action convergence follows from (V.37) and bounded actions. Then send \(N\to\infty\); the domination in (V.34) is \(K(1+|P^2|)\), integrable by the already-proved first-action moments (V.33). This proves (V.30)--(V.35) and joint empirical laws for both actions without a circular velocity-moment premise. Full same-family covariance matrices are retained for any finite set of appended observations.

## V.6. Raw Euler approximation and a deterministic velocity comparison

On a larger primal ball let \(F_R\) have norm at most \(M_0\) and Lipschitz constant \(L_0\), with a bounded reference flow inside it with slack. The local Euler defect on a step \(h_j\) is at most \(L_0M_0h_j^2/2\), because
\[
 \left\|\int_0^{h_j}[F_R(\theta(t_j+s))-F_R(\theta(t_j))]\,ds\right\|_{\mathcal X}
                 \le\int_0^{h_j}L_0M_0s\,ds.
\]
The error recurrence and discrete Gronwall give node error at most
\[
                   \tfrac12 L_0M_0Te^{L_0T}|\pi|.            \tag{V.38}
\]
Linear raw interpolation adds at most \(2M_0|\pi|\). Choosing mesh smaller than the fixed slack closes first-exit induction. The constants are width independent. This proves the bounded population Euler premise used in V.3 from the bounded cap path, without using any source derivative or velocity result.

For states \(\theta,\bar\theta\) on one primal ball and directions \(v,\bar v\) of bounded \(\mathcal X\) norm, put
\(\alpha=\|\theta-\bar\theta\|_{\mathcal X}\) and
\(\beta=\|v-\bar v\|_{\mathcal X}\). Define the actual chain-rule velocities
\[
 P_i^1=v_w\cdot x_i,\quad U_i^\ell=d_\phi(z_i^\ell)P_i^\ell,\quad
 P_i^2=v_Ah_i^1+A U_i^1,\quad P_i^3=v_Bh_i^2+B U_i^2.         \tag{V.39}
\]
For \(\mathcal T_M(X)=\|(|X|-M)_+\|_2\), \(M\ge1\), we claim
\[
 \sum_{\ell,i}(\|P_i^\ell-\bar P_i^\ell\|_2+\|U_i^\ell-\bar U_i^\ell\|_2)
 \le K\left[\beta+(1+M)\alpha+
                       \sum_{\ell,i}\mathcal T_M(\bar P_i^\ell)\right]. \tag{V.40}
\]
The constant depends on the primal/direction bound and fixed activation, not on \(R,M\).

Truncate the reference factor using \(c_M(p)=\operatorname{sgn}(p)\min(|p|,M)\):
\[
 \|[d_\phi(z)-d_\phi(\bar z)]\bar P\|_2
 \le ceM\|z-\bar z\|_2+2(a+e)\mathcal T_M(\bar P).            \tag{V.41}
\]
The first \(P\)-error is at most \(\beta\). For an upper layer expand
\[
\begin{aligned}
 P^\ell-\bar P^\ell={}&
 (v_{W_\ell}-\bar v_{W_\ell})h^{\ell-1}
 +\bar v_{W_\ell}(h^{\ell-1}-\bar h^{\ell-1})\\
 &+(W_\ell-\bar W_\ell)\bar U^{\ell-1}
 +W_\ell(U^{\ell-1}-\bar U^{\ell-1}).
\end{aligned}
\]
The direction and difference operator norms are bounded by their HS norms. Using (V.8), this is at most \(K(\alpha+\beta+\|U^{\ell-1}-\bar U^{\ell-1}\|_2)\) in \(L^2\). The \(U^\ell\)-error is \((a+e)\) times the corresponding \(P^\ell\)-error plus (V.41). Induction proves (V.40). There is a single \(M\): each new \(M\) multiplies a forward discrepancy already controlled by (V.8).

If \(\|\bar P\|_4\le K\), then
\[
 \mathcal T_M(\bar P)\le\|\bar P\mathbf1_{\{|\bar P|>M\}}\|_2
                             \le\|\bar P\|_4^2/M.            \tag{V.42}
\]
Population instantaneous Euler node states and raw directions differ from the flow state/direction at the preceding time by \(K|\pi|\), by (V.38) and fixed-cap Lipschitzness. Use the node as reference in (V.40), apply (V.35), (V.42), and take \(M=|\pi|^{-1/2}\). The hidden velocity error is at most \(K\sqrt{|\pi|}\), uniformly in time. Primary errors are \(K|\pi|\).

Here is the population chain rule needed in that statement. A \(C^1\) \(L^2\)-valued preactivation path has almost-everywhere absolutely continuous coordinate representatives, by its integral representation and Fubini. The scalar chain rule gives derivative \(d_\phi(Z)P\), \(P=\dot Z\). This product is \(L^2\)-continuous by (V.37); its coordinate integral identity holds in \(L^2\) because the multiplier is bounded. Thus \(\phi(Z)\) is \(C^1\) as an \(L^2\) path. Each learned action is \(C^1\) in HS, hence operator norm, so the continuous bilinear product rule gives the next preactivation derivative in (V.39). Repeat through layer 3. This proves the chain rule along both capped and uncut strong trajectories; it assumes no Fréchet differentiability of the activation Nemytskii map on the whole \(L^2\) space.

Strong \(L^2\) node convergence has an almost-sure subsequence for each fixed time. Fatou's lemma passes (V.26), (V.35) to the cap flow:
\[
 \sup_{t\le T}\|X_R(t)\|_p\le K_{R,T}\sqrt p,\qquad p\ge2,    \tag{V.43}
\]
for every primary field and hidden velocity. This is \(\sup_t\|X(t)\|_p\), not \(\|\sup_t|X(t)|\|_p\). The constant is independent of the exponent. Applying (V.40), (V.42) at two flow times also gives a \(K_{R,T}|t-s|^{1/2}\) \(L^2\) velocity modulus, since raw state and direction are Lipschitz in time at fixed cap. No bound on the growth of \(K_{R,T}\) with \(R\) is claimed.

## V.7. Fixed-cap finite GF and fine raw Euler, including the actual readout

At a fixed auxiliary mesh, the primary law in F identifies every node contraction. Exact matrix unrolling gives, for \(\ell=2,3\),
\[
 \max_k\|W_{\ell,k}^{(n)}\|_{\rm op}
 \le\|W_{\ell,0}^{(n)}\|_{\rm op}
  +\sum_{j,b}h_j|p_{j,b}^{(n)}|\|\delta_{j,b}^{\ell,(n)}\|_n
                                    \|h_{j,b}^{\ell-1,(n)}\|_n.       \tag{V.44}
\]
Every term in the finite sum converges, and its limit is bounded uniformly over sufficiently fine population meshes by their primal bound. The first-layer and readout norms at the finitely many nodes converge as well; include the full initial \(d\)-tuple of first weights as a root when its norm is needed. Consequently a deterministic enlarged finite primal ball with slack contains all coarse nodes and raw interpolants with probability tending to one at each fixed sufficiently fine mesh. This proves the finite primal events used in V.3. It uses only the primary fixed-program law, initial operator bounds and update lengths; it is independent of the derivative and velocity estimates.

The finite readout in (V.5) is never reset in training. Its normalized norm is
\[
                       \|C_0^{(n)}\|_n=O_{\Pr}(n^{-1}).       \tag{V.45}
\]
At a fixed cap and fixed transcript, compare it to a same-matrix auxiliary program whose readout root is zero. Stopped finite-step Lipschitz comparison, with the primal slack just established for the zero-root program, gives state and query error \(O_{\Pr}(n^{-1})\); the comparison closes without exit. Thus the actual program has the same fixed-transcript population limit \(C_0=0\). This auxiliary argument justifies the vanishing root within F. Every actual finite GF/GD and every same-width cap comparison below retains the nonzero readout (V.5).

Let \(\theta_{R,n}\) be finite capped flow, or exact raw Euler for \(F_R\) with any deterministic \(\eta_n\to0\). Let \(\theta^\pi_{R,n}\) be the same-width, same-initialization coarse Euler reference. On the event from (V.44), deterministic stopped comparison gives
\[
 \sup_{t\le T}\|\theta_{R,n}(t)-\theta^\pi_{R,n}(t)\|_{\mathcal X}
                                \le K_{R,T}(|\pi|+\eta_n),    \tag{V.46}
\]
where \(\eta_n=0\) denotes flow. To avoid presupposing existence through \(T\), compare until exit. The coarse interpolant has differential-equation defect at most \(L_0M_0|\pi|\), the fine Euler interpolant has defect at most \(L_0M_0\eta_n\), and a flow has zero defect. Integral Gronwall keeps the discrepancy below fixed slack. No exit occurs, and finite-dimensional local existence continues capped GF through \(T\); the same comparison bounds the fine Euler nodes. All constants are width independent at this cap.

At any \(t\), its actual raw direction differs from \(F_R(\theta^\pi_{R,n}(t_k))\), for the preceding coarse node \(t_k\), by at most \(K_{R,T}(|\pi|+\eta_n)\). For fine Euler this uses its preceding fine node and its bounded within-step displacement; it does not substitute the vector field at the interpolated state. Apply (V.40) with the coarse node as reference:
\[
 \sup_{t\le T}\|V_{R,n}(t)-V^\pi_{R,n,k}\|_{\rm sum,2}
 \le K_{R,T}\left[(1+M)(|\pi|+\eta_n)
              +\max_k\sum_{\ell,i}\mathcal T_{M,n}(P^{\ell,\pi}_{R,n,k,i})\right],
                                                               \tag{V.47}
\]
where \(V\) is the full hidden velocity tuple and
\(\mathcal T_{M,n}(v)=\|(|v|-M)_+\|_n\).

For fixed \(\pi,M\), V.5 gives joint empirical \(\mathcal W_2\) convergence of all coarse node velocities. Positive-part tail norms are 1-Lipschitz, so all the finitely many tail norms in (V.47) converge to their population counterparts, bounded by \(K_{R,T}/M\) using (V.35), (V.42). Consequently, for every \(\varepsilon>0\), the probability that the left side exceeds
\(K_{R,T}[(1+M)|\pi|+M^{-1}]+\varepsilon\) tends to zero. At the fixed mesh choose \(M=|\pi|^{-1/2}\), giving width-limit bound \(K_{R,T}\sqrt{|\pi|}\). This is a width-limit upper bound in probability, not an almost-sure uniform finite-width estimate.

Let \(\mu_{R,n,\ell}(t)\) be the empirical law of a same-layer tuple containing all three samples of chosen primary fields and hidden velocities; the readout is included only in layer 3. Coupling actual and coarse observations by their neuron indices gives
\[
\begin{aligned}
 \sup_{t\le T}\mathcal W_2(\mu_{R,n,\ell}(t),\mu_{R,\ell}(t))
 \le{}&\sup_t\|X_{R,n,\ell}(t)-X^\pi_{R,n,\ell,k}\|_n\\
 &+\max_k\mathcal W_2(\mu^\pi_{R,n,\ell,k},\mu^\pi_{R,\ell,k})\\
 &+\sup_t\|X^\pi_{R,\ell,k}-X_{R,\ell}(t)\|_2 .
\end{aligned}                                                    \tag{V.48}
\]
At fixed mesh the middle term vanishes by V.5. The others tend to zero under the subsequent mesh refinement by (V.38), (V.40), (V.47). Therefore
\[
 \sup_{t\le T}\mathcal W_2(\mu_{R,n,\ell}(t),\mu_{R,\ell}(t))
                       \longrightarrow0\quad\hbox{in probability}. \tag{V.49}
\]
For finitely many observation times, concatenate their coordinates and use the same neuron coupling. Squared costs sum over the finitely many times, and the fixed-program law is joint for the complete coarse transcript. This proves joint-time \(\mathcal W_2\) convergence, retaining all correlations within each layer.

The tail functional is also 1-Lipschitz in \(\mathcal W_2\). Under a coupling,
\[
 |\mathcal T_u(X)-\mathcal T_u(Y)|
 \le\|(|X|-u)_+-(|Y|-u)_+\|_2\le\|X-Y\|_2.
\]
Thus all fixed-level empirical tail norms converge uniformly in time. From (V.43) and the moment-to-tail calculation in V.2 one obtains, at a fixed cap,
\[
 \lim_{u\to\infty}\limsup_{n\to\infty}
 \Pr\!\left(\sup_{t\le T}
 \|X_{R,n}(t)\mathbf1_{\{|X_{R,n}(t)|>u\}}\|_n^2>\varepsilon\right)=0. \tag{V.50}
\]
This is asymptotic empirical uniform integrability of second moments; no empirical fourth-moment or finite-width exponential-moment estimate is asserted.

The order throughout V.7 is width at fixed cap, auxiliary mesh and truncation level, followed by mesh refinement. The raw step \(\eta_n\to0\) contributes only its deterministic Euler defect. No Gaussian identification for an increasing transcript length occurs.

## V.8. Full true backward observations and full fixed-cap kernels

On a capped state, true fields \(b_i^\ell=d_\phi(z_i^\ell)q_i^\ell\) are observations distinct from its update fields \(\delta_{R,i}^\ell\). We establish their laws explicitly.

At a fixed finite transcript append, in order, \(b_i^3=d_\phi(z_i^3)C\), the current transpose query \(B^*b_i^3\), the true middle gate, the current transpose query \(A^*b_i^2\), and the true bottom gate. Approximate each gate by \(d_\phi(z)\tau_M(q)\), using nested levels for dependent gates. At fixed levels F applies. Equation (V.37) proves that bounded-gate multiplication preserves joint \(\mathcal W_2\) convergence, and positive-part tail convergence makes its empirical clipping error vanish in the width-limit \(L^2\) sense. A bounded current action transfers input error to output error; learned increments are included as finite rank contractions. Iterate through the finite appended chain. Every true backward observation therefore has its joint empirical \(\mathcal W_2\) limit equal to the corresponding population action and product.

This argument is an observational closure statement only. It does not assert an expected-derivative formula for arbitrary untruncated products without domination. When such formulas are needed at initialization, lemma V.I supplies their separate truncation and domination proof, including the full source covariances and current returns. For the kernel limits here, action continuity suffices.

There is also a trajectory comparison. If \(\alpha=\|\theta-\bar\theta\|_{\mathcal X}\), then
\[
 \sum_{\ell,i}\|b_i^\ell-\bar b_i^\ell\|_2
 \le K\left[(1+M)\alpha+\mathcal T_M(\bar C)
      +\sum_i\{\mathcal T_M(\bar q_i^2)+\mathcal T_M(\bar q_i^1)\}\right], \tag{V.51}
\]
where barred \(q\)'s are true incoming fields. Use (V.41) with \(\bar q\) in place of \(\bar P\), and substitute downwards through the bounded transpose actions. Each new \(M\) multiplies a forward discrepancy controlled by (V.8), so the estimate has a single \(M\).

The true backward map is strongly continuous along converging states on a bounded primal ball: use (V.37) and bounded-action continuity recursively. Along a capped \(C^1\) trajectory the true incoming fields are continuous \(L^2\) paths, with compact time images. Such an image has uniformly vanishing positive-part tails: cover it by finitely many \(L^2\) balls of radius \(\varepsilon\), use the 1-Lipschitz tail property, then send \(M\to\infty\) at the finitely many centers. Hence population coarse Euler true fields converge uniformly to the cap-flow fields, by applying (V.51) with the flow as reference and (V.38). Their tail norms also converge uniformly.

For finite cap GF/fine Euler against the same-width coarse reference, use (V.51). At fixed mesh and \(M\) the coarse empirical tail norms converge by the finite observational closure. Take width, then mesh refinement at fixed \(M\), then \(M\to\infty\), using the compact-tail conclusion. This proves (V.49) and joint-time convergence for the true backward tuple as well.

The four full kernel blocks at any state are
\[
 K^1_{ij}=\Gamma_{ij}\langle b_i^1,b_j^1\rangle,\qquad
 K^2_{ij}=\langle b_i^2,b_j^2\rangle\langle h_i^1,h_j^1\rangle,
\]
\[
 K^3_{ij}=\langle b_i^3,b_j^3\rangle\langle h_i^2,h_j^2\rangle,\qquad
 K^4_{ij}=\langle h_i^3,h_j^3\rangle.                          \tag{V.52}
\]
Finite definitions use normalized inner products. Joint \(\mathcal W_2\) convergence implies convergence of each second moment: under a coupling,
\[
 |E[XY]-E[\bar X\bar Y]|
 \le\|X-\bar X\|_2\|Y\|_2+\|\bar X\|_2\|Y-\bar Y\|_2.
\]
The bounds are uniform in time. Hence every entry of every block, predictions, and loss converge uniformly in time for finite capped GF and fine Euler. In particular all off-diagonals are retained. On a capped trajectory (V.52) is the observed true gradient kernel; it need not be the coefficient matrix of that surrogate trajectory's prediction equation.

## V.9. Same-width comparison for uncut finite GF and exact raw GD

Compare actual uncut finite GF \(\theta_n\) with its same-width physical cap-flow reference \(\theta_{R,n}\), retaining the common nonzero initialization (V.5). By V.7 the reference lies with probability tending to one in a fixed enlarged primal ball containing the population cap path with slack. This comparison ball can be chosen independently of \(R\), using G's cap-independent primal bounds; the width needed for its high-probability containment may depend on the fixed \(R\). Raw direction bounds on that ball are independent of cap.

At fixed \(R\), (V.49) passes reference incoming positive-part tail norms uniformly in time. Since
\[
 |q|\mathbf1_{\{|q|>R\}}\le2(|q|-R/2)_+,
\]
the width-limit upper bound for the reference tail term in (V.11) is at most \(Ke^{-cR^2}\), by (V.12) with adjusted constants. Until uncut exit, Gronwall in (V.11) gives a width-limit state error
\[
                   \varepsilon_R=K_Te^{K_TR-cR^2}\longrightarrow0.   \tag{V.53}
\]
Choose a large fixed cap so this is smaller than primal slack, and then take width. The first-exit comparison rules out exit with probability tending to one. Substitution into (V.11) also gives raw-direction and backward-field error bounds tending to zero with \(R\); polynomial factors are absorbed into a smaller Gaussian rate.

Finite uncut GF exists globally even before this probability argument. Its finite-dimensional field is locally Lipschitz. The exact gradient identity is
\[
 \frac d{dt}\frac12\sum_i(f_i-y_i)^2
 =-\left[\frac dn\|\dot W^1\|_F^2+\|\dot A\|_F^2+
                         \|\dot B\|_F^2+\|\dot C\|_n^2\right].       \tag{V.54}
\]
Its raw Hilbert length on \([0,T]\) is at most \(\sqrt{TL(0)}\), so it cannot escape to infinity in finite-dimensional parameter space in finite time. Local existence therefore continues it globally. The sum norm (V.1) is equivalent to this Hilbert metric up to fixed numerical constants. This identity is used for true finite GF only.

For raw GD let \(t_k=k\eta_n\), \(\eta_n=n^{-2}\), and
\(E(t)=\sup_{s\le t}\|\theta_n(s)-\theta_{R,n}(s)\|_{\mathcal X}\).
Its direction on the interval is \(F_\infty(\theta_n(t_k))\). Apply (V.11) at \(t_k\) against the cap reference there. The additional difference between \(F_R(\theta_{R,n}(t_k))\) and \(F_R(\theta_{R,n}(t))\) is at most \(L_RM_R\eta_n\). Before exit,
\[
 E(t)\le K(1+eR)\int_0^tE(s)\,ds
  +Kt\sup_{s\le T}\sum_{Q\in\mathscr Q_{R,n}(s)}
                           \|Q\mathbf1_{\{|Q|>R\}}\|_n
  +K_{R,T}t\eta_n.                                          \tag{V.55}
\]
The preceding-node discrepancy is bounded by \(E(s)\), since \(t_k\le s\). This yields (V.53) and the same no-exit conclusion. For actual raw directions, use the same pointwise estimate at \(t_k\) and the bounded cap within-step variation. No width-independent Lipschitz bound for the uncut field is used. All finite GD iterates are well defined as finite compositions of algebraic and smooth operations; the comparison supplies the required finite-horizon bound with probability tending to one.

The limits are width at fixed cap after the capped auxiliary-mesh limit, then cap removal. The exact raw step enters solely through \(K_{R,T}\eta_n\). This also proves convergence for any deterministic raw step tending to zero. Both algorithms can use the same initialized cap reference, so their observable limits hold jointly; their same-neuron coupled limiting trajectories agree.

Forward and backward convergence now follow from (V.8), (V.11), (V.53). Population cap fields already converge strongly by V.2. Hence (V.52), predictions, and loss converge uniformly in physical time for the true finite GF and exact raw GD. In this last comparison capped update fields \(\delta_R\) can serve as references, because (V.11) compares them directly to true uncut \(b\). Section V.8 separately supplies the full true kernel assertion for fixed-cap trajectories.

## V.10. Cap removal for hidden velocities with ordered tails

Raw cap states and directions converge uniformly by (V.13). Apply (V.40) using the uncut population velocity as reference. Its preactivation velocities are continuous \(L^2\) paths by V.6, so their compact time images have uniformly vanishing positive-part tails. At fixed \(M\),
\[
 \limsup_{R\to\infty}\sup_{t\le T}\|V_R(t)-V(t)\|_{\rm sum,2}
 \le K\sum_{\ell,i}\sup_{t\le T}\mathcal T_M(P_i^\ell(t)).
\]
Then \(M\to\infty\) proves uniform strong population cap-velocity convergence. The positive-part tail functional is 1-Lipschitz; therefore sufficiently large population caps inherit uniformly vanishing velocity tails from this strong convergence. No estimate for the growth of fixed-cap moment constants in (V.43) is required.

For a finite uncut algorithm versus its same-width cap-flow reference, (V.40) gives
\[
 K\left[\beta_{R,n}+(1+M)\alpha_{R,n}
        +\sum_{\ell,i}\sup_{t\le T}
                      \mathcal T_{M,n}(P^\ell_{R,n,i}(t))\right],     \tag{V.56}
\]
where \(\alpha,\beta\) are raw state and actual direction discrepancies. Their width-limit upper bounds tend to zero with \(R\), by (V.53)--(V.55). The constant in (V.56) depends only on the common primal/direction ball and activation, and is independent of \(R,M\). At fixed \(R,M\), V.7 passes all empirical reference tails to the capped population tails. Send \(R\to\infty\) at fixed \(M\), using the just-proved strong population velocity convergence; then \(M\to\infty\). The bound vanishes.

Neuron-index coupling, capped \(\mathcal W_2\) convergence, and population cap convergence now prove same-layer uncut joint field/velocity \(\mathcal W_2\) convergence uniformly in time. A finite concatenation gives joint laws at any finitely many times. The raw-GD one-sided directions satisfy the same estimates: neighboring reference times differ by at most \(\eta_n\), and its direction is continuous. Node choices do not affect integrated speeds.

The limit orders used are:

1. For product-query identification: fixed transcript and nested clips, width, inner clip removal, outer clip removal.
2. For fixed-cap trajectory identification: fixed cap and auxiliary mesh, width, auxiliary mesh refinement.
3. For population velocity cap removal: cap at fixed velocity-tail level \(M\), then \(M\to\infty\).
4. For finite uncut velocity comparison: width at fixed cap and \(M\), cap at fixed \(M\), then \(M\to\infty\).

In particular, no cap-dependent velocity-moment constant is multiplied by an uncontrolled cap-removal error.

## V.11. Supremum-norm path laws and integrated squared speeds

For layer \(\ell\), let the hidden path tuple be
\[
 X_\ell(t)=(z_1^\ell,h_1^\ell,z_2^\ell,h_2^\ell,z_3^\ell,h_3^\ell)(t).
\]
Its coordinates are almost-everywhere absolutely continuous. Finite recomputed hidden fields along raw interpolation have the same property. The chain rule (V.39), bounded actions and \(\phi'\), and bounded raw directions give a uniform RMS speed bound on the stopped primal/direction ball. The no-exit comparisons remove stopping with probability tending to one. Population speeds are bounded in \(L^2\) on compact horizons.

For an absolutely continuous vector path \(x\) and its linear interpolation \(I_hx\) on a fixed observation grid of maximum interval length \(h\), at \(t\in[u,v]\),
\[
 |x(t)-I_hx(t)|
 \le |x(t)-x(u)|+|x(v)-x(u)|
 \le2\sqrt h\left(\int_u^v|x'(s)|^2\,ds\right)^{1/2}.
\]
Hence
\[
             \|x-I_hx\|_\infty^2
                         \le4h\int_0^T|x'(s)|^2\,ds.         \tag{V.57}
\]
Averaging this same-neuron coupling cost gives a squared path-space \(\mathcal W_2\) approximation cost bounded by \(4h\) times the integrated RMS speed squared, for finite and population laws. Initial second moments and the speed bound also ensure finite second moments of the path supremum norm, so the measures belong to \(\mathcal P_2(C([0,T];\mathbb R^6))\).

At a fixed observation grid, joint node \(\mathcal W_2\) convergence passes through linear interpolation, a Lipschitz map from the finite Euclidean node tuple to the path supremum norm. Apply a triangle inequality with finite and population observation-grid interpolants, first take width at that fixed grid, then let \(h\to0\) in (V.57). Therefore, for both exact algorithms,
\[
 \mathcal W_2\left(\frac1n\sum_{\alpha=1}^n
                  \delta_{X_{\ell,n,\alpha}(\cdot)},
                  \operatorname{Law}(X_\ell(\cdot))\right)
             \longrightarrow0\quad\hbox{in probability},     \tag{V.58}
\]
in \(C([0,T];\mathbb R^6)\) equipped with its supremum norm. This final approximation is necessary: joint fixed-time laws alone do not imply (V.58).

Uniform-time velocity \(\mathcal W_2\) convergence implies uniform convergence of squared norms and all same-layer cross second moments. Under any coupling,
\[
 |\|u\|_2^2-\|v\|_2^2|
                  \le(\|u\|_2+\|v\|_2)\|u-v\|_2,
\]
and the product estimate following (V.52) handles cross moments. The norms are uniformly bounded by the primal/direction bounds. Multiplying the uniform error by \(T\) bounds the error in each time integral. In particular
\[
 \int_0^T\|P^\ell_{n,i}(t)\|_n^2\,dt,\qquad
 \int_0^T\|U^\ell_{n,i}(t)\|_n^2\,dt
\]
converge in probability to their population counterparts, as do their within-layer integrated cross products. These are actual neuron-coordinate speeds from the chain rule, not an assertion that their norms equal metric derivatives of the marginal probability laws.

Raw block speeds converge as well. For uncut GF, (V.4), the rank-one norm identity, and (V.52) give, for each of its four blocks,
\[
                 \|\dot\theta^{(\ell)}(t)\|_{\rm raw}^2
                           =p(t)^TK^\ell(t)p(t).
\]
For exact raw GD the same identity holds with the preceding-node residual and kernel, since that is its actual raw direction. Uniform convergence of predictions and all kernel blocks, together with population continuity and \(\eta_n\to0\), therefore gives convergence of the blockwise squared raw speeds uniformly in time and after time integration. For capped dynamics the identical assertion uses the three capped-update backward Grams in place of the true hidden kernel blocks; those Grams converge by the primary fixed-cap law. Their readout block remains \(K^4\).

Initialized and current action orientations are retained on any fixed finite collection of canonical generated probes. Include the probes and observations in F, or take their common-space \(L^2\) limits. In a same-width or common-population comparison,
\[
 \|Wu-\bar W\bar u\|_2
 \le\|W-\bar W\|_{\rm op}\|u\|_2+\|\bar W\|_{\rm op}\|u-\bar u\|_2,
\]
and the same holds for adjoints. Difference operator norms are bounded by HS differences, and current operator norms were bounded by exact update lengths. Thus both orientations pass through the limits. Population cap increments converge strongly in HS. If finite learned-increment HS contractions are included as scalar observations, exact rank unrolling and Riemann approximation express them through bounded products of the already converging field contractions. No unspecified cross-width operator identification is asserted.

All assertions are full-sequence convergence in probability on every fixed finite physical horizon, for the one fixed activation. The constants may depend on the fixed data and horizon. At each probabilistic application the cap, auxiliary mesh and query truncations are fixed first, and their subsequent removal has been explicitly ordered.

## V.I. A derivative-valid observational extension at initialization

Fix any deterministic three coefficients \(p_j\), and write
\[
 H_0=\sum_{j=1}^3p_j\phi(Z_j^3),\qquad d_j^\ell=\phi'(Z_j^\ell),
 \qquad \beta_i^3=H_0d_i^3.
\]
Here \(Z^2,Z^3\) are the initialized forward Gaussian tuples, and \(h_i^\ell=\phi(Z_i^\ell)\). Their covariances may be singular. All named source coordinates remain distinct formal arguments, with all scalar coefficients and covariances frozen in source derivatives.

The fixed-program lemma of Part F extends to the finite appended chain
\[
 \beta_i^3,\quad q_i^2=B_0^*\beta_i^3,\quad
 \beta_i^2=d_i^2q_i^2,\quad q_i^1=A_0^*\beta_i^2,\quad
 \beta_i^1=d_i^1q_i^1.
\]
The extension has joint empirical \(\mathcal W_2\) convergence and the following exact source formulas:
\[
 q_i^2=\zeta_i^2+\sum_jD^3_{ij}h_j^2,\qquad
 D^3_{ij}=E[p_jd_j^3d_i^3+\mathbf1_{\{i=j\}}H_0\phi''(Z_i^3)],
                                                        \tag{V.I.1}
\]
\[
 q_i^1=\zeta_i^1+\sum_jD^2_{ij}h_j^1,\qquad
 D^2_{ij}=E[\mathbf1_{\{i=j\}}\phi''(Z_i^2)q_i^2
                         +d_i^2D^3_{ij}d_j^2].           \tag{V.I.2}
\]
The reverse source covariances are the full input Grams:
\[
 E[\zeta_i^2\zeta_j^2]=E[\beta_i^3\beta_j^3],\qquad
 E[\zeta_i^1\zeta_j^1]=E[\beta_i^2\beta_j^2].               \tag{V.I.3}
\]
Each reverse source family is independent of the forward source families and the first-layer roots in the source construction. This does not assert independence of \(q_i^\ell\) from its same-layer features: the return terms in (V.I.1)--(V.I.2) remain.

**Proof.** The map \(\beta_i^3=H_0d_i^3\) has an unbounded derivative, so first set \(\beta_{i,M}^3=\tau_M(H_0)d_i^3\). At fixed \(M\), this is a \(C^1\) bounded-derivative function of the top preactivation tuple. The Part F lemma gives its transpose query, with coefficients
\[
 D^{3,M}_{ij}
 =E[\tau_M'(H_0)p_jd_j^3d_i^3+
          \mathbf1_{\{i=j\}}\tau_M(H_0)\phi''(Z_i^3)].
\]
Since \(\phi'\) and \(\phi''\) are bounded, these integrands are bounded in absolute value by \(K(1+|H_0|)\), independently of \(M\), and \(H_0\in L^p\) for every finite \(p\). Dominated convergence gives \(D^{3,M}\to D^3\). Also \(\beta^3_M\to\beta^3\) in \(L^2\); hence their Gram matrices converge. Realize all reverse Gaussian tuples through the positive-semidefinite square roots of these finite Gram matrices on one fresh Gaussian root. Square-root continuity, which does not require invertible covariances, gives \(\zeta^{2,M}\to\zeta^2\) in \(L^2\), jointly with the independent forward tuple. The formulas
\[
 q_i^{2,M}=\zeta_i^{2,M}+\sum_jD^{3,M}_{ij}h_j^2
\]
therefore converge in \(L^2\) to (V.I.1), jointly with all primary observations. Along a coupled almost-sure subsequence they converge pointwise as well. Their formal first derivatives in the named layer-2 forward sources are
\[
 \partial_{\xi_j^2}q_i^{2,M}=D^{3,M}_{ij}d_j^2;
\]
they converge pointwise and are bounded independently of \(M\).

For the second gate set \(\beta_{i,M,N}^2=d_i^2\tau_N(q_i^{2,M})\). At fixed \(M,N\), the original bounded-derivative theorem applies to the whole finite chain. Its expected forward-source derivative is
\[
 E\!\left[
 \mathbf1_{\{i=j\}}\phi''(Z_i^2)\tau_N(q_i^{2,M})
       +d_i^2\tau_N'(q_i^{2,M})D^{3,M}_{ij}d_j^2
 \right].                                                   \tag{V.I.4}
\]
First keep \(N\) fixed and send \(M\to\infty\). The integrand is bounded by a constant depending on \(N\), and is continuous in \(q_i^{2,M},D^{3,M}_{ij}\). Thus (V.I.4) converges to the same expression with \(q^2,D^3\). Now send \(N\to\infty\): the integrand is bounded by \(K(1+|q_i^2|)\), which is integrable because (V.I.1) is a finite sum of Gaussian variables and linear-growth Gaussian functions. Its limit is \(D^2_{ij}\) in (V.I.2). The same ordered limits give \(\beta^2_{M,N}\to\beta^2\) in \(L^2\); source Gram convergence and square-root coupling then give (V.I.2)--(V.I.3). The last gate follows by the same \(L^2\) product argument below; if its expected derivatives are needed, the identical additional truncation has an integrable Gaussian-linear envelope.

For completeness, the empirical passage from truncated to actual gates uses only empirical second moments and bounded operator norms. If \((z_n,q_n)\) converges in joint \(\mathcal W_2\), use a coupling with \(L^2\) convergence and write
\[
 \|\phi'(z_n)q_n-\phi'(z)q\|_2
 \le \|\phi'\|_\infty\|q_n-q\|_2
       +\|[\phi'(z_n)-\phi'(z)]q\|_2.
\]
For the second term, truncate the fixed \(q\) at level \(L\). Its bounded part is at most \(\|\phi''\|_\infty L\|z_n-z\|_2\), and its tail part is at most \(2\|\phi'\|_\infty\|q\mathbf1_{\{|q|>L\}}\|_2\). Let \(n\to\infty\), then \(L\to\infty\). Also \(|q|\mathbf1_{\{|q|>L\}}\le2(|q|-L/2)_+\), and positive-part tail norms converge under \(\mathcal W_2\). Thus the finite truncation discrepancies vanish in the width-limit \(L^2\) sense. The high-probability uniform norm bounds for \(A_0,B_0\) transfer every such input discrepancy to its actual transpose answer. Their population actions are bounded on the common generated \(L^2\) spaces, so the population discrepancy vanishes as well. A triangle inequality proves the joint empirical law of the complete untruncated chain.

The limits are fixed transcript and fixed \(M,N\), then width, then \(M\to\infty\) at fixed \(N\), then \(N\to\infty\). No inverse covariance, arbitrary \(L^p\) operator theorem, or unproved derivative-limit interchange is used.

## Part N. Nonzero initial motion and variation of the projected kernel

This part proves the remaining initial-motion assertions of Theorem M.1. Throughout, \(A=A_0\) and \(B=B_0\) denote the initialized actions when no time argument is shown. Their norms are at most 10, and their stars are their actual adjoints. All products and inner products are taken in the appropriate layer. We use the internal fixed-program theorem F.1, the operator-moment and trace-probe estimates (F.4a)–(F.4c), the bounded multiplier and weighted Taylor lemmas F.5–F.7, and the derivative-valid initialization observation lemma V.I. These statements include the singular input-Gram cases.

The proof first identifies explicit hidden directions, proves positivity of all parameter blocks and every bottom sample using fresh reverse Gaussian sources, and then establishes quantitative affine lower bounds for every upper sample. A direct perturbation estimate preserves the upper bounds for the amplitude in (M.21). The physical equations determine the time factors, and a scalar feature-energy differential determines the kernel expansion.

### N.1. Initial directions and their scalar feature-energy interpretation

Write
\[
 p_i=y_i/3,\qquad m=\sum_{i=1}^3p_i,\qquad
 m\in\{-1,-1/3,1/3,1\},\qquad \sum_i|p_i|=1.
 \tag{N.1}
\]
All \(p_i\) are nonzero, and \(|m|\ge1/3\). Let \(Z_i^\ell,h_i^\ell\) be the initialized forward fields for
\(\phi(z)=a(1+z)+e\arctan z\), and put \(d_i^\ell=\phi'(Z_i^\ell)\).
The activation parameters in this part satisfy \(a\ge1\) and \(0<e\le1\), with the additional quantitative upper bound specified in Section N.5. Define
\[
 H=\sum_i p_i h_i^3,\qquad
 \beta_i^3=H d_i^3,\qquad q_i^2=B^*\beta_i^3,\qquad
 \beta_i^2=d_i^2q_i^2,\qquad q_i^1=A^*\beta_i^2,\qquad
 \beta_i^1=d_i^1q_i^1.
 \tag{N.2}
\]
All these variables lie in the indicated \(L^2\) spaces, because the gates are bounded and the actions are bounded. Lemma V.I identifies their actual finite-array limits and all the response coefficients used below; this is not an application of a bounded-derivative theorem directly to the unbounded products in (N.2).

The three hidden raw directions are
\[
 V^1=d^{-1}\sum_i p_i\beta_i^1x_i,\qquad
 V^2=\sum_i p_i\beta_i^2\otimes h_i^1,\qquad
 V^3=\sum_i p_i\beta_i^3\otimes h_i^2.
 \tag{N.3}
\]
Here \(V^1\in L^2(\Omega_1;\mathbb R^d)\), \(V^2\) and \(V^3\) are Hilbert–Schmidt operators, and
\[
 \|V\|_{\rm hidden}^2
       =d\|V^1\|_2^2+\|V^2\|_{\rm HS}^2+\|V^3\|_{\rm HS}^2.
 \tag{N.4}
\]
For every sample define the preactivation directions
\[
 U_j^1=V^1\cdot x_j=\sum_i\Gamma_{ji}p_i\beta_i^1,
\]
\[
 U_j^2=V^2h_j^1+A(d_j^1U_j^1),\qquad
 U_j^3=V^3h_j^2+B(d_j^2U_j^2).
 \tag{N.5}
\]

The scalar functional needed later is defined on the hidden raw parameter space by
\[
 {\cal E}(\theta_h)=\tfrac12\left\|\sum_i p_i h_i^3(\theta_h)\right\|_3^2,
 \qquad \theta_h=(w,A,B).
 \tag{N.6}
\]
It is continuously Fréchet differentiable in the hidden raw norm, and at initialization its raw gradient is \(V\). We give the argument to specify the exact differentiability assertion.

On a raw neighborhood, all forward differences are \(O(\eta)\) in \(L^2\) for an increment \(\Delta\theta_h\) of raw norm \(\eta\): apply the Lipschitz activation bounds and
\[
 \Delta(Ah)=\Delta A\,h+A\,\Delta h+\Delta A\,\Delta h,
 \qquad \|\Delta A\|_{\rm op}\le\|\Delta A\|_{\rm HS}.
\]
Thus \(\Delta H=O(\eta)\), and
\[
 {\cal E}(\theta_h+\Delta\theta_h)-{\cal E}(\theta_h)
       =\langle H,\Delta H\rangle+\tfrac12\|\Delta H\|^2.
 \tag{N.7}
\]
The second term is \(O(\eta^2)\). For any fixed \(v,z\in L^2\), the weighted Taylor estimate (F.41) says
\[
 E\!\left[v\{\phi(z+q)-\phi(z)-\phi'(z)q\}\right]
                                             =o(\|q\|_2).
 \tag{N.8}
\]
Explicitly the remainder is bounded both by
\(\|\phi''\|_\infty|q|^2/2\) and \(2\|\phi'\|_\infty|q|\).
Split its weighted expectation at \(|v|=M\); the bound is
\(\|\phi''\|_\infty M\|q\|_2^2/2+
2\|\phi'\|_\infty\|v\mathbf1_{|v|>M}\|_2\|q\|_2\).
First send \(\|q\|_2\) to zero and then \(M\) to infinity.

Apply (N.8) in each term \(p_i\langle H,\Delta h_i^3\rangle\), with fixed top weight \(H\). Expanding \(\Delta z_i^3\) and using adjunction gives, up to \(o(\eta)\),
\[
 \sum_i p_i\{\langle\beta_i^3,\Delta B h_i^2\rangle
                         +\langle q_i^2,\Delta h_i^2\rangle\}.
\]
Terms containing \(\Delta B\,\Delta h_i^2\) are \(O(\eta^2)\).
Apply (N.8) with the fixed weights \(q_i^2\), expand \(\Delta z_i^2\), and move \(A\) through the resulting inner product. A last application with fixed weights \(q_i^1\) gives
\[
 d{\cal E}[\Delta\theta_h]
 =\sum_i p_i\{\langle\beta_i^1,x_i\cdot\Delta w\rangle
             +\langle\beta_i^2,\Delta A h_i^1\rangle
             +\langle\beta_i^3,\Delta B h_i^2\rangle\}
 =\langle V,\Delta\theta_h\rangle_{\rm hidden}.
 \tag{N.9}
\]
This proves the Fréchet derivative. Its continuity follows from forward \(L^2\) continuity, the bounded multiplier lemma F.5 applied successively to the gates and incoming fields, and the rank-one Hilbert–Schmidt difference inequality. This is a scalar differentiability result; no Fréchet derivative of the nonlinear map from all of \(L^2\) to \(L^2\) is assumed.

### N.2. Positive backward Grams, hidden blocks, and every bottom sample

Let
\[
 Q_\ell=(\langle h_i^\ell,h_j^\ell\rangle)_{ij},\qquad
 S_\ell=(\langle\beta_i^\ell,\beta_j^\ell\rangle)_{ij}.
 \tag{N.10}
\]
The initial Gaussian projection and augmented-Gram inequality (G.1), (G.4) imply \(Q_1\succeq a^2(\Gamma+\mathbf1\mathbf1^T)\succ0\), and \(Q_2\succeq a^2Q_1\succ0\). The initialized \(Z^3\) is therefore a nondegenerate centered three-dimensional Gaussian, with covariance \(Q_2\), and has a strictly positive density on \(\mathbb R^3\).

For \(v\in\mathbb R^3\), \(v^TS_3v=0\) would imply
\[
 \left[\sum_i p_i\phi(z_i)\right]
       \left[\sum_i v_i\phi'(z_i)\right]=0
                                      \quad\hbox{for every }z\in\mathbb R^3.
 \tag{N.11}
\]
Indeed the identity first holds almost surely, and full support and continuity extend it to every point. The first factor has no open zero set: its derivative in coordinate \(i\) is \(p_i\phi'(z_i)\), which is never zero because \(p_i\ne0\) and \(\phi'\ge a\). Its nonzero set is therefore dense. The second factor vanishes on that dense set and hence everywhere. Differentiate it in coordinate \(i\) to obtain \(v_i\phi''(z_i)=0\) for every \(z_i\). Since \(\phi''(z)=-2ez/(1+z^2)^2\) is not identically zero when \(e>0\), every \(v_i=0\). Thus
\[
                                  S_3\succ0.
 \tag{N.12}
\]

For use in the next step, the exact derivative-valid transpose formulas of Lemma V.I are
\[
 q_i^2=\zeta_i^2+\sum_jD^3_{ij}h_j^2,\qquad
 D^3_{ij}=E[p_jd_j^3d_i^3+\mathbf1_{i=j}H\phi''(Z_i^3)],
 \qquad E[\zeta^2(\zeta^2)^T]=S_3,
 \tag{N.13}
\]
\[
 q_i^1=\zeta_i^1+\sum_jD^2_{ij}h_j^1,\qquad
 D^2_{ij}=E[\mathbf1_{i=j}\phi''(Z_i^2)q_i^2+d_i^2D^3_{ij}d_j^2],
 \qquad E[\zeta^1(\zeta^1)^T]=S_2.
 \tag{N.14}
\]
The families \(\zeta^2,\zeta^1\) are centered Gaussian and independent of the respective forward-source families and first-layer roots. Their return terms are retained. The expected derivative formulas are legitimate precisely because Lemma V.I first truncates the incoming fields, passes their expected derivatives by dominated convergence, and then removes the truncations in their actual matrix answers.

Conditioning on all the layer-two forward sources in (N.13) gives
\(\operatorname{Cov}(\beta^2\mid Z^2)
       =\operatorname{diag}(d_i^2)S_3\operatorname{diag}(d_i^2)\).
Hence, for every \(v\in\mathbb R^3\),
\[
 v^TS_2v\ge E\operatorname{Var}\!\left(\sum_i v_i\beta_i^2\mid Z^2\right)
 \ge a^2\lambda_{\min}(S_3)\|v\|_2^2.
 \tag{N.15}
\]
In particular \(S_2\succ0\). Likewise
\[
 \operatorname{Cov}(\beta^1\mid Z^1)
 =\operatorname{diag}(d_i^1)S_2\operatorname{diag}(d_i^1)
 \succeq a^2\lambda_{\min}(S_2)I_3.
 \tag{N.16}
\]
These lower bounds use fresh reverse Gaussian covariance, not a claim that the full incoming fields are independent of the forward features.

Apply (N.16) to each Euclidean component of \(V^1\), and sum:
\[
 d\|V^1\|_2^2
 \ge\frac{a^2\lambda_{\min}(S_2)}d\sum_i p_i^2\|x_i\|_{\mathbb R^d}^2
 =a^2\lambda_{\min}(S_2)\sum_i p_i^2>0.
 \tag{N.17}
\]
For the two matrix blocks the rank-one inner-product formula yields
\[
 \|V^\ell\|_{\rm HS}^2
   =\sum_{i,j}p_ip_j(S_\ell)_{ij}(Q_{\ell-1})_{ij}
   =\operatorname{tr}\!\left(\operatorname{diag}(p)S_\ell
                         \operatorname{diag}(p)Q_{\ell-1}\right),
 \quad\ell=2,3.
 \tag{N.18}
\]
For positive definite \(S,Q\), the last trace is at least
\(\lambda_{\min}(S)\lambda_{\min}(Q)\sum_i p_i^2>0\).
To see this, the matrix \(\operatorname{diag}(p)S\operatorname{diag}(p)
-\lambda_{\min}(S)\operatorname{diag}(p)^2\) is positive semidefinite; its trace pairing with \(Q\) is nonnegative, by diagonalizing \(Q\). Apply the same reasoning to \(\operatorname{diag}(p)^2\) and \(Q\succeq\lambda_{\min}(Q)I\). Thus all three hidden parameter directions are nonzero.

For any fixed sample \(j\), (N.5) and (N.16) give
\[
 \|U_j^1\|_2^2
 \ge E\operatorname{Var}(U_j^1\mid Z^1)
 \ge a^2\lambda_{\min}(S_2)\sum_i\Gamma_{ji}^2p_i^2
 \ge a^2\lambda_{\min}(S_2)p_j^2>0.
 \tag{N.19}
\]
The last step uses \(\Gamma_{jj}=1\). Since \(d_j^1\ge a\), the corresponding feature direction \(d_j^1U_j^1\) is nonzero as well. This covers singular \(\Gamma\) without its inverse and without requiring nonzero affine bottom motion.

### N.3. Exact affine formulas for the two upper layers

We now set \(e=0\) only for a comparison calculation, on the same initialized actions and roots. Define
\[
 z_p=\sum_i p_iZ_i^1,\qquad \gamma_j=(\Gamma p)_j,\qquad
 k=m\mathbf1_1+z_p,
\]
\[
 v=a^2m\mathbf1_2+a^3Ak,\qquad
 H=am\mathbf1_3+Bv,\qquad Q=B^*H.
 \tag{N.20}
\]
The subscripts on the constant vectors specify their layer. These identities follow by summing the affine forward equations:
\(\sum_i p_ih_i^1=ak\),
\(\sum_i p_ih_i^2=am\mathbf1_2+a^2Ak\), and
\(\sum_i p_ih_i^3=am\mathbf1_3+Bv\).

Affine backward gates give, independently of the sample index,
\[
 \beta_i^3=aH,\qquad \beta_i^2=a^2Q,\qquad
 \beta_i^1=a^3A^*Q,\qquad U_j^1=a^3\gamma_jA^*Q.
 \tag{N.21}
\]
Also \(V^2=a^3Q\otimes k\). The first affine feature Gram is
\(Q_1=a^2(\Gamma+\mathbf1\mathbf1^T)\), so
\(\langle k,h_j^1\rangle=a(m+\gamma_j)\). Substituting in (N.5) gives
\[
 U_j^2=a^4L_jQ,\qquad
               L_j=(\gamma_j+m)I+\gamma_jAA^*.
 \tag{N.22}
\]
At the next layer,
\(Q_2=a^4\Gamma+(a^2+a^4)\mathbf1\mathbf1^T\) and
\(V^3=H\otimes v\). Therefore
\(\langle v,h_j^2\rangle
=a^5[\gamma_j+(1+a^{-2})m]\). The second formula in (N.5) gives
\[
 U_j^3=a^5T_jH,
\]
\[
 T_j=[\gamma_j+(1+a^{-2})m]I
       +(\gamma_j+m)BB^*+\gamma_jBAA^*B^*.
 \tag{N.23}
\]
These formulas hold for every sample individually; no permutation symmetry of the inputs or labels has been used.


### N.4. Finite Gaussian calculations and strictly positive affine lower bounds

We specify carefully how finite Gaussian identities yield deterministic population inequalities. Let \(A_n,B_n\) be the independent initialized square Gaussian matrices and use the corresponding first-layer roots to define \(k_n,v_n,H_n,Q_n\) by (N.20). For a fixed sample, put
\[
 L_{j,n}=(\gamma_j+m)I+\gamma_jA_nA_n^T,
\]
\[
 T_{j,n}=[\gamma_j+(1+a^{-2})m]I
       +(\gamma_j+m)B_nB_n^T+\gamma_jB_nA_nA_n^TB_n^T.
 \tag{N.24}
\]
The numbers \(\gamma_j,m\) are deterministic. The vectors
\(a^4L_{j,n}Q_n\) and \(a^5T_{j,n}H_n\) are fixed finite programs and converge to (N.22)–(N.23), including their squared norms. They can be viewed as proxies for the finite feature directions after empirical Gram contractions are replaced by their limiting deterministic values. The finite-array inner products need not equal their population values exactly; Theorem F.1 justifies this replacement.

For every fixed polynomial matrix expression \(P_n\) in the initialized actions and their transposes, (F.4b) bounds every fixed moment of \(\|P_n\|_{\rm op}\) uniformly in \(n\). The vectors just described have normalized norms bounded by fixed polynomials in \(\|A_n\|_{\rm op},\|B_n\|_{\rm op},\|z_{p,n}\|_n\) and constants. All fixed moments of the last normalized Gaussian norm are uniformly bounded by Jensen. Hölder consequently proves uniform moments of all fixed orders for these vector norms and their squared norms. Their deterministic convergence in probability from F.1 therefore implies convergence of expectations: truncate at a fixed level, pass the bounded part, and bound the tail using a higher moment.

A normalized trace of \(P_n\) also has a deterministic limit. Append an independent standard Gaussian vector \(g_n\); the contraction \(\langle g_n,P_ng_n\rangle_n\) is a fixed finite program, and (F.4c) makes its difference from \(n^{-1}\operatorname{tr}P_n\) tend to zero in \(L^2\). Its trace thus has a deterministic limit in probability, and the preceding operator moment bounds give uniform integrability and convergence of its expectation. Write \(\tau(P)\) for this limiting normalized trace; this symbol does not assert existence of a trace of the infinite-dimensional initialized action. These arguments apply simultaneously to every finite list of traces and contractions below.

For completeness the Gaussian fourth-moment identities used in the calculations follow from differentiating the Gaussian moment-generating function: for centered jointly Gaussian scalars,
\[
 E[X_1X_2X_3X_4]
 =E[X_1X_2]E[X_3X_4]+E[X_1X_3]E[X_2X_4]
                         +E[X_1X_4]E[X_2X_3].
 \tag{N.25}
\]
One can verify this directly by differentiating
\(E e^{t^TX}=\exp(t^T\operatorname{Cov}(X)t/2)\) four times at zero. The same function is even, so centered cubic moments vanish.

Condition on \(A_n,z_{p,n}\), making \(v_n\) fixed and leaving \(B_n\) independent. In coordinates
\[
 (Q_n)_r=am\sum_i(B_n)_{ir}
           +\sum_{i,s}(B_n)_{ir}(B_n)_{is}(v_n)_s.
\]
The first sum is centered Gaussian of covariance \(a^2m^2 I\); the expectation of the second is \(v_n\). Its covariance, by the two non-mean pairings in (N.25), is
\(\|v_n\|_n^2I+v_nv_n^T/n\). The covariance between the first and second sums is zero by the cubic moment identity. Thus exactly at every width
\[
 E_BQ_n=v_n,\qquad
 \operatorname{Cov}_B(Q_n)
 =(a^2m^2+\|v_n\|_n^2)I+v_nv_n^T/n.
 \tag{N.26}
\]
For any fixed matrix \(L\) measurable with respect to \(A_n,z_{p,n}\), taking the trace of \(L\operatorname{Cov}_B(Q_n)L^T\) gives
\[
 E_B\|LQ_n\|_n^2
 =(1+1/n)\|Lv_n\|_n^2
       +(a^2m^2+\|v_n\|_n^2)\frac1n\operatorname{tr}(LL^T).
 \tag{N.27}
\]
In particular this bounds the expectation below by its second summand.

Here are all normalized traces required for (N.22). For \(X_n=A_nA_n^T\), entrywise use of (N.25) gives
\[
 E(X_n)_{ij}=\delta_{ij},\qquad
 E[(X_n)_{ij}(X_n)_{kl}]
 =\delta_{ij}\delta_{kl}
       +n^{-1}(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
 \tag{N.28}
\]
Indeed expand the two entries as sums over the two column indices; the mean pairing contributes the first term, and each of the two cross pairings forces the same column and contributes the displayed factor \(1/n\). Summing \(i=j\) gives \(E\tau_n(X_n)=1\). Summing \(k=j,l=i\) gives
\[
 E\tau_n(X_n^2)
 =\frac1n\sum_{i,j}\{\delta_{ij}+n^{-1}(\delta_{ij}+1)\}
 =2+1/n.
\]
The trace-probe and uniform-integrability argument therefore proves
\[
                    \tau(AA^*)=1,\qquad \tau((AA^*)^2)=2.
 \tag{N.29}
\]
It follows by expanding \(L_j^2\) that
\[
 \tau(L_j^2)
 =(\gamma_j+m)^2+2\gamma_j(\gamma_j+m)+2\gamma_j^2
                         =(m+2\gamma_j)^2+\gamma_j^2.
 \tag{N.30}
\]
The other factor in (N.27) also has a deterministic limit. Since \(A_n\) is independent of \(k_n\), \(E_AA_nk_n=0\) and \(E_A\|A_nk_n\|_n^2=\|k_n\|_n^2\). The first-layer roots are centered, with
\(E\|z_{p,n}\|_n^2=p^T\Gamma p\). Hence for every \(n\)
\[
 E\|v_n\|_n^2=a^4m^2+a^6(m^2+p^T\Gamma p).
\]
The deterministic finite-program limit and uniform integrability identify
\[
                   \|v\|_2^2=a^4m^2+a^6(m^2+p^T\Gamma p).
 \tag{N.31}
\]
The product of the nonnegative factors in (N.27) converges in probability to the product of their deterministic limits, and its higher moments are bounded as above. Thus its expectation converges too. Taking the unconditional expectation in (N.27) with \(L=L_{j,n}\), and then passing to the limits just justified, proves
\[
 \|U_j^2\|_2^2
 \ge a^8[a^2m^2+a^4m^2+a^6(m^2+p^T\Gamma p)]
                               [(m+2\gamma_j)^2+\gamma_j^2].
 \tag{N.32}
\]
Since \(p^T\Gamma p\ge0\) and
\[
 (m+2c)^2+c^2=5(c+2m/5)^2+m^2/5,
\]
we obtain the positive lower bound
\[
                 \|U_j^2\|_2^2
                 \ge\frac{a^8m^4}{5}(a^2+a^4+a^6)>0.
 \tag{N.33}
\]

For (N.23), \(T_{j,n}\) is even under \(B_n\mapsto-B_n\), whereas \(B_nv_n\) is odd. Condition on \(A_n,z_{p,n}\); symmetry of \(B_n\) makes the cross term in
\(\|T_{j,n}(am\mathbf1+B_nv_n)\|_n^2\) have expectation zero. Therefore
\[
 E\|a^5T_{j,n}H_n\|_n^2
 \ge a^{12}m^2 E\|T_{j,n}\mathbf1\|_n^2.
\]
Left orthogonal invariance of \(B_n\), at fixed \(A_n\), makes the conditional expectation of \(T_{j,n}^2\) a scalar multiple of the identity. This can also be checked using only row sign changes to kill off-diagonal entries and row permutations to equalize diagonal entries. Since \(\|\mathbf1\|_n=1\),
\(E_B\|T_{j,n}\mathbf1\|_n^2=E_B\tau_n(T_{j,n}^2)\).
The deterministic limits and uniform integrability thus give
\[
                         \|U_j^3\|_2^2\ge a^{12}m^2\tau(T_j^2).
 \tag{N.34}
\]

We compute that trace in full. Put \(S_n=B_nB_n^T\), \(R_n=B_nA_nA_n^TB_n^T\), and \(M_n=B_n^TB_n\). Equations (N.28)–(N.29), now for \(B_n\), give
\(\tau(S)=1,\tau(S^2)=2\). Conditioning on \(B_n\), \(E_AA_nA_n^T=I\) gives
\[
 E_A\tau_n(R_n)=\tau_n(S_n),\qquad
 E_A\tau_n(S_nR_n)=\tau_n(S_n^2).
\]
Therefore the limiting traces satisfy \(\tau(R)=1,\tau(SR)=2\).
For the final one, expand
\(\operatorname{tr}(X_nM_nX_nM_n)
 =\sum_{i,j,k,l}(X_n)_{ij}(M_n)_{jk}(X_n)_{kl}(M_n)_{li}\).
Each term of (N.28) contributes, respectively,
\(\operatorname{tr}M_n^2\), \(n^{-1}\operatorname{tr}M_n^2\), and
\(n^{-1}(\operatorname{tr}M_n)^2\). Dividing by \(n\) proves the exact formula
\[
 E_A\tau_n(R_n^2)
 =(1+1/n)\tau_n(M_n^2)+\tau_n(M_n)^2.
 \tag{N.35}
\]
The cyclic trace identities give \(\tau_n(M_n^2)=\tau_n(S_n^2)\) and
\(\tau_n(M_n)=\tau_n(S_n)\). Their deterministic limits are 2 and 1, and their squared moments pass by the already proved uniform integrability. Hence
\[
              \tau(S)=\tau(R)=1,\qquad
              \tau(S^2)=\tau(SR)=2,\qquad \tau(R^2)=3.
 \tag{N.36}
\]
Every convergence assertion here follows from F.1 and the trace-probe argument (F.4c), with moment control (F.4b); the finite fourth-moment expectation calculations alone would not prove concentration.

Set \(t_a=a^{-2}\). For
\(u=\gamma_j+(1+t_a)m,\ v=\gamma_j+m,\ w=\gamma_j\),
(N.36) gives
\[
 \tau(T_j^2)=(u+v+w)^2+(v+w)^2+w^2
       =[3\gamma_j+(2+t_a)m]^2+(2\gamma_j+m)^2+\gamma_j^2.
\]
Completing the square in \(\gamma_j\) gives
\[
 \tau(T_j^2)
 =14\left(\gamma_j+\frac{8+3t_a}{14}m\right)^2
                         +\frac{6+8t_a+5t_a^2}{14}m^2.
 \tag{N.37}
\]
Combining this with (N.34) yields
\[
              \|U_j^3\|_2^2
              \ge\frac{a^{12}m^4}{14}(6+8a^{-2}+5a^{-4})>0.
 \tag{N.38}
\]
In particular, using \(a\ge1\) and \(|m|\ge1/3\), the two affine lower bounds imply
\[
             \|U_{j,0}^2\|_2\ge\frac{a^7}{9\sqrt5},\qquad
             \|U_{j,0}^3\|_2\ge\frac{a^6}{9}\sqrt{\frac37}.
 \tag{N.39}
\]
The subscript 0 denotes the affine comparison, and these bounds hold for every upper sample uniformly over admissible input Grams and binary labels.


### N.5. Explicit nonlinear perturbation and a geometry-independent cutoff

Compare nonlinear and affine initial calculations on the same initialized actions and first-layer roots. Use subscript \(e\) for the nonlinear fields, subscript 0 for the affine fields, and \(\Delta\) for their difference. For every layer and sample,
\[
 \|d^\ell_{j,e}\|_\infty\le2a,\qquad
                 \|d^\ell_{j,e}-a\|_\infty\le e.
 \tag{N.40}
\]
The second bound compares with the constant affine gate, so it requires no derivative of a change of preactivation.

The following estimates use \(e\le1\), \(\|A\|,\|B\|\le10\), \(\|Z_j^1\|_2=1\), \(\pi/2<2\), and \(\sum_i|p_i|=1\). All bounds are per sample; the bound on \(h^3\) also bounds \(H\).
\[
\begin{array}{c|c|c}
 \text{field}&\text{nonlinear norm bound}&\text{difference bound}\\ \hline
 h^1&4a&2e\\
 h^2&43a^2&22ae\\
 h^3,\ H&433a^3&222a^2e\\
 \beta^3&866a^4&655a^3e\\
 \beta^2&17320a^5&15210a^4e\\
 \beta^1,\ U_j^1&346400a^6&325300a^5e
\end{array}
 \tag{N.41}
\]
Here is the full scalar derivation. Forward propagation gives
\[
 \|h_e^1\|\le2a+2\le4a,\quad
 \|h_e^2\|\le a+10a(4a)+2\le43a^2,\quad
 \|h_e^3\|\le a+10a(43a^2)+2\le433a^3.
\]
The same initial actions appear in both programs, so
\[
 \|\Delta h^1\|\le2e,\quad
 \|\Delta h^2\|\le10a(2e)+2e\le22ae,\quad
 \|\Delta h^3\|\le10a(22ae)+2e\le222a^2e.
 \tag{N.42}
\]
The affine forward bounds are \(2a,21a^2,211a^3\). Summing with \(|p_i|\) gives the corresponding bounds for \(H_e,H_0,\Delta H\).

The backward difference decompositions are exactly
\[
 \beta_e^3=d_e^3H_e,\qquad
 \Delta\beta^3=a\Delta H+(d_e^3-a)H_e,
\]
\[
 \beta_e^2=d_e^2B^*\beta_e^3,\qquad
 \Delta\beta^2=aB^*\Delta\beta^3+(d_e^2-a)B^*\beta_e^3,
\]
\[
 \beta_e^1=d_e^1A^*\beta_e^2,\qquad
 \Delta\beta^1=aA^*\Delta\beta^2+(d_e^1-a)A^*\beta_e^2.
 \tag{N.43}
\]
Their nonlinear norm coefficients are \(2\cdot433=866\),
\(20\cdot866=17320\), and \(20\cdot17320=346400\), with the powers of \(a\) in (N.41). The difference coefficients are
\[
 222+433=655,\qquad
 10\cdot655+10\cdot866=15210,\qquad
 10\cdot15210+10\cdot17320=325300.
 \tag{N.44}
\]
The respective powers are \(a^3e,a^4e,a^5e\). Since
\(U_j^1=\sum_i\Gamma_{ji}p_i\beta_i^1\), the inequalities
\(|\Gamma_{ji}|\le1\), \(\sum_i|p_i|=1\) give the same norm and difference bounds for each \(U_j^1\).

For the matrix directions, expand
\[
 \Delta(\beta\otimes h)
                 =\Delta\beta\otimes h_e+\beta_0\otimes\Delta h
 \tag{N.45}
\]
and sum with the absolute coefficients \(|p_i|\). The affine backward bounds are \(\|\beta_0^3\|\le211a^4\), \(\|\beta_0^2\|\le2110a^5\). Thus
\[
 \|V_e^2\|_{\rm HS}\le(17320)(4)a^6=69280a^6,\qquad
 \|V_e^3\|_{\rm HS}\le(866)(43)a^6=37238a^6,
\]
\[
 \|V_0^2\|_{\rm HS}\le(2110)(2)a^6=4220a^6,\qquad
 \|V_0^3\|_{\rm HS}\le(211)(21)a^6=4431a^6,
\]
\[
 \|\Delta V^2\|_{\rm HS}
 \le[(15210)(4)+(2110)(2)]a^5e=65060a^5e,
\]
\[
 \|\Delta V^3\|_{\rm HS}
 \le[(655)(43)+(211)(22)]a^5e=32807a^5e.
 \tag{N.46}
\]
This also gives a direct finite norm comparison for the parameter directions, though their positivity was already proved for every \(e>0\) in Section N.2.

For the preactivation directions the exact difference formulas from (N.5) are
\[
 \Delta U_j^2=(\Delta V^2)h_{j,e}^1+V_0^2\Delta h_j^1
                 +A[a\Delta U_j^1+(d_{j,e}^1-a)U_{j,e}^1],
\]
\[
 \Delta U_j^3=(\Delta V^3)h_{j,e}^2+V_0^3\Delta h_j^2
                 +B[a\Delta U_j^2+(d_{j,e}^2-a)U_{j,e}^2].
 \tag{N.47}
\]
The nonlinear middle norm satisfies
\[
 \|U_{j,e}^2\|
 \le[(69280)(4)+10\cdot2\cdot346400]a^7
                                      =7205120a^7.
 \tag{N.48}
\]
Using (N.41), (N.46) in the first line of (N.47) gives
\[
 \|\Delta U_j^2\|
 \le[(65060)(4)+(4220)(2)+10(325300+346400)]a^6e
 =6985680a^6e<7\cdot10^6a^6e.
 \tag{N.49}
\]
The second line, with (N.48)–(N.49), gives
\[
 \|\Delta U_j^3\|
 \le[(32807)(43)+(4431)(22)+10(6985680+7205120)]a^7e
 =143416183a^7e<1.5\cdot10^8a^7e.
 \tag{N.50}
\]
Consequently a common simple bound is
\[
                 \|\Delta U_j^\ell\|\le C(a)e,\quad\ell=2,3,
                 \qquad C(a)=2\cdot10^8a^7.
 \tag{N.51}
\]

Choose
\[
                              0<e\le(10^{10}a)^{-1}.
 \tag{N.52}
\]
Then \(C(a)e\le a^6/50\). The affine lower bounds (N.39) are preserved by more than one half, since \(a\ge1\) and
\[
 \frac{a^6}{50}<\frac{a^7}{18\sqrt5},\qquad
 \frac{a^6}{50}<\frac{a^6}{18}\sqrt{\frac37}.
 \tag{N.53}
\]
For the first scalar inequality, \(18\sqrt5<45<50\); for the second, \(18\sqrt{7/3}<36<50\). The triangle inequality therefore proves \(U_j^2\ne0,U_j^3\ne0\) for every sample at the chosen positive nonlinearity. Their feature directions are nonzero as well because \(\phi'\ge a\). The activation rule (M.21) is smaller than the cutoff (N.52). Together with Section N.2 this proves nonzero preactivation and feature directions in every layer and sample.

### N.6. Physical initial accelerations

Consider the strong uncut physical solution constructed in Parts G and V. At time zero \(C_0=0\), so every residual-free backward field \(b_i^\ell(0)\) and every hidden raw velocity vanish. The initialized predictions are zero and \(r_i(0)=-y_i=-3p_i\). The readout equation gives
\[
                  C'(0)=\sum_i y_i h_i^3=3H,\qquad
                  C(t)/t\longrightarrow3H\quad\text{in }H_3.
 \tag{N.54}
\]
The hidden fields are continuous in their \(L^2\) norms. By Lemma F.5, bounded multiplication by the continuously varying gate gives
\[
 b_i^3(t)/t
     =\phi'(z_i^3(t))\,C(t)/t\longrightarrow3\beta_i^3.
\]
Operator-norm convergence \(B(t)^*\to B^*\), boundedness of these actions, and another application of F.5 then give \(b_i^2(t)/t\to3\beta_i^2\). The identical explicit sequence with \(A(t)^*\) and the first-layer gate gives
\[
                 b_i^\ell(t)/t\longrightarrow3\beta_i^\ell
                 \quad\text{in }H_\ell,\qquad\ell=1,2,3.
 \tag{N.55}
\]
For example split
\(B(t)^*[b_i^3(t)/t]-3B^*\beta_i^3\)
into \(B(t)^*[b_i^3(t)/t-3\beta_i^3]
+3(B(t)^*-B^*)\beta_i^3\); both terms tend to zero. This states every needed incoming-field step without assuming pointwise uniform gates.

Divide the hidden equations (M.12) by \(t\). Use \(r_i(t)\to-3p_i\), (N.55), forward-field continuity, and the rank-one norm inequality. We obtain in the hidden raw Hilbert space
\[
                   \theta_h'(t)/t\longrightarrow9V.
 \tag{N.56}
\]
Thus the right second derivative exists at zero and equals \(9V\) in each block. Integrating the \(o(t)\) remainder in (N.56) yields
\[
                   \theta_h(t)-\theta_h(0)=\tfrac92t^2V+o(t^2).
 \tag{N.57}
\]
The integral estimate follows directly: if the velocity error is bounded by \(\eta s\) for \(0<s<t_\eta\), its integral to \(t<t_\eta\) is bounded by \(\eta t^2/2\).

The strong forward chain and product rules give
\[
 (z_j^1)'=(w')\cdot x_j,\qquad
 (z_j^2)'=A'h_j^1+A[\phi'(z_j^1)(z_j^1)'],
\]
\[
                    (z_j^3)'=B'h_j^2+B[\phi'(z_j^2)(z_j^2)'].
 \tag{N.58}
\]
Divide these identities successively by \(t\), use (N.56) and Lemma F.5, and compare with (N.5). This proves
\[
 \frac{(z_j^\ell)'(t)}t\longrightarrow9U_j^\ell,\qquad
 \frac{(h_j^\ell)'(t)}t
        =\phi'(z_j^\ell(t))\frac{(z_j^\ell)'(t)}t
                                    \longrightarrow9d_j^\ell U_j^\ell.
 \tag{N.59}
\]
All first velocities at zero are zero. Therefore the initial second derivatives are
\[
                      (z_j^\ell)''(0)=9U_j^\ell,\qquad
                      (h_j^\ell)''(0)=9\phi'(Z_j^\ell)U_j^\ell.
 \tag{N.60}
\]
They are nonzero in \(L^2\) by Sections N.2 and N.5. In the half-line time domain these are right derivatives at its initial endpoint. No assertion of a second Fréchet derivative of the ambient nonlinear activation map is involved.

### N.7. The projected total kernel changes

Put \(f_p=\sum_i p_if_i\), and let \(g_h(t)\) be the hidden part of its raw gradient. The scalar prediction differentiability and raw metric identities in Part F give exactly
\[
 \kappa(t)=p^T\Big(\sum_{\ell=1}^4K^\ell(t)\Big)p
           =\|g_h(t)\|_{\rm hidden}^2+\|H(\theta_h(t))\|_3^2.
 \tag{N.61}
\]
The hidden gradient has components
\[
 d^{-1}\sum_i p_i b_i^1(t)x_i,\qquad
 \sum_i p_i b_i^2(t)\otimes h_i^1(t),\qquad
 \sum_i p_i b_i^3(t)\otimes h_i^2(t).
\]
Equation (N.55) and forward continuity consequently imply
\[
                  g_h(t)/t\longrightarrow3V,\qquad
                  \|g_h(t)\|_{\rm hidden}^2
                          =9t^2\|V\|_{\rm hidden}^2+o(t^2).
 \tag{N.62}
\]
At initialization this hidden gradient is zero.

For the readout term in (N.61), use the scalar Fréchet differential (N.9) and the raw displacement (N.57):
\[
 {\cal E}(\theta_h(t))
 ={\cal E}(\theta_h(0))
    +\left\langle V,\tfrac92t^2V+o(t^2)\right\rangle_{\rm hidden}
    +o(t^2)
 ={\cal E}(\theta_h(0))+\tfrac92t^2\|V\|_{\rm hidden}^2+o(t^2).
\]
Since \(\|H\|_3^2=2{\cal E}\), this gives the second contribution
\[
 \|H(\theta_h(t))\|_3^2
       =\|H(\theta_h(0))\|_3^2+9t^2\|V\|_{\rm hidden}^2+o(t^2).
 \tag{N.63}
\]
Adding (N.62) and (N.63) proves
\[
                 \kappa(t)=\kappa(0)+18t^2\|V\|_{\rm hidden}^2+o(t^2),
                 \qquad\|V\|_{\rm hidden}>0.
 \tag{N.64}
\]
For all sufficiently small positive \(t\), the remainder is smaller in magnitude than \(9t^2\|V\|_{\rm hidden}^2\), so \(\kappa(t)>\kappa(0)\). This proves a change of the actual projected total kernel along physical training, and completes all initial-motion assertions.
