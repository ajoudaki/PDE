# An odd activation formed by a convex combination under absolute angular separation

This report proves a global two-input theorem for the literal activation
\[
             \psi_e(z)=(1-e)z+e\arctan z.                 \tag{T.1}
\]
It also proves initialization results for three inputs, including sharp
worst-case conditioning of their first feature Gram. The complete global
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

It remains to supply the finite-array premise. The bounded affine
population path in (T.14) has population Euler primal bound \(2U\)
on all sufficiently fine meshes of its own interval \([0,S]\): the
bounded-ball local defect is at most \(45b_r^5h_j^2\), and the sum
of defects tends to zero by Gronwall. At each fixed such mesh, F.1 gives
the field contractions, and the initial finite operator norms are at
most ten with probability tending to one. Exact rank-one unrolling gives
current operator bounds \(10+2S_\delta(2U)^3+o_{\Pr}(1)\) and
\(10+3S_\delta(2U)^3+o_{\Pr}(1)\). First projections and readout
converge at the finitely many nodes. Thus one may take
\[
                    P=11+2U+4S_\delta(2U)^3.            \tag{T.18}
\]
This argument requires width limits only on each fixed mesh. It does not
identify trained matrix operator norms across widths or assume control
of arbitrary coarse Euler meshes.

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
