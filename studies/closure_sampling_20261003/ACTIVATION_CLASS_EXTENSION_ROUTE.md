# Linear-growth analytic activations: joint budgets and an affine boundary case

2026-10-04. Scoped independent continuation of the current study. This is a
candidate internal theorem, proved below relative to the explicitly supplied
insertion, source-approximation, and runtime lemmas. It is not an independent
promotion review. The complete candidate was frozen before exchanging new
scientific findings. No experiments, Git operations, maintained-book edits,
or writes outside this file were made.

The qualitative all-time compression theorem can be extended beyond bounded
activation values. A sufficient transparent hypothesis is bounded **first
derivative on a complex strip**, together with the value at zero. This
includes identity and genuinely nonlinear functions such as
`z + epsilon tanh(z)`. The proof needs a joint preactivation/carrier budget;
substituting derivative constants into the bounded-activation theorem is not
valid. The conservative source exponent from the original deep proof is
retained here. The latest explicit label cap and spherical/folding constants
are not claimed for the enlarged class.

## 1. Input scope, authorization, and exact target

The current-study scientific inputs read completely are
`INPUT_DIMENSION_REFINEMENT.md`, `GENERAL_ANALYTIC_COMPRESSION.md`,
`GENERAL_WEIGHTED_COMPARISON.md`, `DEEP_COMPLEX_SOURCE.md`,
`DEEP_ACTIVATION_EXTENSION.md`, `LABEL_DEPTH_RESCALING_ROUTE.md`,
`SPHERICAL_SOURCE_DIMENSION_ROUTE.md`, and
`STORAGE_QUADRATIC_IMPROVEMENT.md`.

Initially the only authorized prior-study inputs were
`DEPTH_CAVITY_ROUTE.md`, `DEPTH_INSERTION_CHECK.md`, and
`DEPTH_CAVITY_PROBABILITY_CHECK.md` in
`../dense_cutoff_population_rate_20261001/`. Their appended unbounded
claims identified additional proofs. The supervisor then explicitly extended
the scope, using the user's persistent authorization for relevant prior
proofs, to exactly `UNBOUNDED_INSERTION_CHECK.md`,
`UNBOUNDED_ACTIVATION_CHECK.md`, `DEPTH_EXTENSION_RESULT.md`, and
`DEPTH_TRACKING_CHECK.md`, and subsequently to
`UNBOUNDED_ACTIVATION_CANDIDATE.md`. All five were read completely. No
other prior-study file or reference was followed. Required canonical,
neural-network, rigorous-proof, research-contract, evidence, and adversarial
audit instructions were read.

The complete prior unbounded proof has SHA-256
`e939e971d7a9e1b884b42d73d3ce65f5b1f548d9e25ab9cfe76c0502aa591713`;
its local check has
`bec5707fccc99597570ce51c94d3a487fd0b1ede14578617275cb708fdd95578`;
its probability check has
`12884770ecde1f8de5b503ab7d62dadc1fe4e1541f3cf1cf2c7c3b7e9c5954fd`.
Current `DEEP_COMPLEX_SOURCE.md` has
`7a81a04bb3e52a1c60ee83f479238ea1dec54fe2b70277b4f7d513b5eb84c6f2`,
and `DEEP_ACTIVATION_EXTENSION.md` has
`b5279562acc5d8ffceaad2d8ac744d43e51c4af91d0508e66804ab12954ef141`.

The prior unbounded theorem proves real-time, finite-network joint
preactivation/carrier control and a same-width response-memory comparison.
It retains initialized dense matrices. It does **not** by itself prove
analytic source compression, a complex query tube, the improved spherical
count, or explicit depth constants. Those distinctions are preserved here.

Fix input dimension `d`, hidden depth `L>=2`, sample count `m`, unit training
inputs `v_a=x_a/sqrt(d)`, and labels `y_a`, independently of width `n`.
The canonical network, loss, and physical-time flow are
\[
z^{(1)}=Av,\quad z^{(\ell)}=W^{(\ell)}h^{(\ell-1)},\quad
h^{(\ell)}=\phi_\ell(z^{(\ell)}),\quad f_n(v)=w^\top h^{(L)}(v)/n,
\]
\[
c_a=y_a-f_n(v_a),\quad Y=\|y\|_2/\sqrt m,\quad
\mathcal L=\|c\|_2^2/m,
\]
\[
k_a^{(L)}=w,\quad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot k_a^{(\ell)},\quad
k_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},
\]
\[
\dot A=\frac2m\sum_a c_a\delta_a^{(1)}v_a^\top,\quad
\dot W^{(\ell)}=\frac2{mn}\sum_a
c_a\delta_a^{(\ell)}h_a^{(\ell-1)\top},\quad
\dot w=\frac2m\sum_a c_ah_a^{(L)}.                 \tag{1}
\]
The middle recurrences start at layer two, and the backward recurrence
ends at layer `L-1`. Initialize independent entries
`A_ij~N(0,1)`, `W_ij^(ell)~N(0,1/n)`, independent blocks, and `w(0)=0`.
These are exactly the mobilities `(n,1,...,1,n)` of the supplied model.

Assume each activation is real on the real axis, holomorphic on
`|Im z|<a`, and
\[
b=\max_\ell|\phi_\ell(0)|<\infty,\qquad
s=\max\left(1,\sup_{\ell,|\Im z|<a}|\phi_\ell'(z)|\right)<\infty.
                                                               \tag{2}
\]
Then throughout the strip
\[
|\phi_\ell(z)|\le b+s|z|,
\qquad
\sup_{|\Im z|\le a/2}|\phi_\ell^{(j)}(z)|
\le (j-1)!s(4/a)^{j-1}\quad(j\ge2).                \tag{3}
\]
The first inequality integrates `phi'` on the straight segment from zero;
that segment stays in the strip. The second is Cauchy's formula applied
to `phi'` on a disk of radius `a/4`. Thus the value bound is replaced by
the tuple `(a,b,s)`, without an infinite constant for identity.

Define the initialized covariance recursively by
\[
Q^{(0)}_{ab}=v_a^\top v_b,\qquad
Q^{(\ell)}_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)],
\quad Z\sim N(0,Q^{(\ell-1)}),
\quad\gamma=\lambda_{\min}(Q^{(L)})>0.             \tag{4}
\]
Linear growth makes these expectations finite. Conditional Gaussian rows,
bounded fourth moments on bounded covariance sets, and conditional
Chebyshev prove empirical covariance convergence inductively. The Gaussian
expectations are continuous on bounded covariance sets, including singular
ones, by the coupling `Z=Q^(1/2)G` and Gaussian moment domination. Hence
the initialized finite top Gram has a strict positive margin with
probability tending to one. No population-training statement is used.

**Candidate theorem.** Under (2)--(4), there is a positive small-label
threshold depending on the fixed architecture, data, and `(a,b,s)`. For
every fixed label vector below that threshold, and each fixed confidence,
for every sufficiently large width there is an initialization-only
autonomous neural compressor with
\[
\sup_{t\in[0,\infty]}\sup_{\|v\|=1}
|f_C(t,v)-f_n(t,v)|\le Cn^{-1/2},                 \tag{5}
\]
including the fitted endpoint. Using the corrected-readout runtime gives
total retained size
\[
C[\log(en)]^{,2[d(L+5)+1]}+Cm(d+1).             \tag{6}
\]
The elementary diagonal-cubature runtime instead gives exponent
`4[d(L+5)+1]` and is ordinary weighted gradient flow. All coefficients,
data, moving matrices, metrics and caches are counted. Constants and the
width threshold are independent of physical time; the threshold is not
quantified. Zero labels give the exact stationary zero predictor.

## 2. Every substantive use of bounded activation values

| Use in supplied proof | What remains true under (2) | What must change |
| --- | --- | --- |
| Real feature and operator tube | Linear-growth RMS recurrence and bounded slopes suffice | Include the first-weight operator/RMS bound and the constant vector |
| `||w||_infty<=B S` | Only `||w||_(2,n)<=H S` follows from RMS | Include the top carrier in the joint budget |
| Omitted forward control `h_i` bounded | `|h_i|<=b+s Z_i` | Budget preactivations and retain actual amplitude in traces |
| Learned outgoing column | `CS^2(1+Z_i)/sqrt(n)` | Its source remainder has an extra polynomial logarithm |
| Hessian and gradient block estimates | Feature RMS cancels each `1/sqrt(n)` matrix factor | Top carrier curvature needs the same Schatten budget as other layers |
| Query activation magnitude | RMS remains bounded on a pole-safe tube | Add a temporary query-preactivation coordinate cap for insertion controls |
| Final spectral source magnitude | Every needed vector has RMS `C` | Coordinate magnitude `C sqrt(n)` suffices; only its logarithm enters degree |
| Weighted/corrected runtime fitting | Linear growth in the selected norm and bounded multipliers suffice | Reprove RMS fitting instead of reusing a readout coordinate cap |

In particular, the phrase “one may assume derivative bounds directly” in
`DEEP_ACTIVATION_EXTENSION.md` does not by itself remove its zeroth-order
bound. Its original proof still invokes bounded `h_i` and bounded `w_i`.
The next sections supply their replacements.

## 3. Real fitting and the actual imported real joint budget

Write `||u||_(2,n)=||u||_2/sqrt(n)`. On a tube with
`||A||_op/sqrt(n)<=K` and `||W^(ell)||_op<=K`, (3) gives
\[
H_1=b+sK,\qquad H_\ell=b+sK H_{\ell-1},\qquad
\sup_{\|v\|\le1}\|h^{(\ell)}(v)\|_{2,n}\le H_\ell.       \tag{7}
\]
Backward propagation gives
`||delta^(ell)||_(2,n)<=s(sK)^(L-ell)||w||_(2,n)`.
The normalized parameter norm is
\[
\|(A,W,w)\|_{\rm par}^2=
\|A\|_F^2/n+\sum_{\ell=2}^L\|W^{(\ell)}\|_F^2+\|w\|_2^2/n.
\]
Equation (1) and the exact gradient Gram give
\[
-\frac d{dt}\rho^2=\|\dot\theta\|_{\rm par}^2,
\qquad \rho=\|c\|_2/\sqrt m.                       \tag{8}
\]
On a stopped normalized readout Gram margin `g>0`,
`-rho'>=2g rho`; hence the path length is at most `Y/sqrt(g)`.
In particular `||w||_(2,n)<=Y/sqrt(g)`. Hidden velocity norms are at
most `C rho ||w||_(2,n)`, by (7). Thus their total displacement is
`CY^2/g^(3/2)`. Bounded slopes propagate this to every sphere feature.
At sufficiently small labels this preserves both the initial singular
value margin and the operator tube. A first-exit argument proves global
existence, exponential fitting, and finite parameter path length. The
query derivative is bounded by `C rho`, so output tails are sphere-uniform.
The same constants work for each fixed-size rectangular cavity, with all
normalizations still `n`, once its strict initial margin is inherited.

Set `S` to a fixed multiple of `Y/g`, large enough that total residual
activity `(2/m) sum_a int |c_a|` is at most `S/2`; restrict `S<=1`.
The authorized unbounded theorem supplies, on events tending to one,
\[
\max_{a,\ell,i,t\ge0}|z_{a,i}^{(\ell)}(t)|\le C\sqrt{\ell_n},
\quad
\max_{a,\ell,i,t\ge0}|k_{a,i}^{(\ell)}(t)|\le CS\sqrt{\ell_n},
\quad \ell_n=\log(en).                              \tag{9}
\]
The second includes `w`. Its proof does not assume a trained moment law.
For reference, its essential actual-amplitude inequalities, on a joint
budget of size `B`, are
\[
K_i/S\le G_{\delta,i}/S+C(1+S^2B)(1+Z_i)+o(1),
\qquad
Z_i\le G_{h,i}+CS^2(1+S^2\sqrt B)K_i/S+o(1).        \tag{10}
\]
Here `Z_i` and `K_i` are running maxima across the fixed training set;
`G_h` and `G_delta` are incoming-row forward and outgoing-column backward
Gaussian suprema from the independently stopped singleton cavity. At
the first layer `G_h` is its initialized Gaussian row; at the top
`K_i/S<=C(1+Z_i)` and only the forward inequality is needed.
Choosing `B` first and `S` sufficiently small makes the feedback product
less than `1/2` and gives
\[
Z_i+K_i/S\le C(1+G_{h,i}+G_{\delta,i}/S)+o(1),        \tag{11}
\]
with a coefficient independent of budget and empirical moment degree.
The complete prior local and probability proofs supply its required
coordinate comparison, common-cavity independence, and fixed-degree
moment closure. They are used as proved inputs, with their fixed-data
quantifiers. They provide no explicit `beta^-62L` threshold.

## 4. Complex extension: the joint budget is necessary

Take `T=C_T ell_n`, with `C_T` depending on the real decay rate, and
\[
r_n=c\ell_n^{-(L+4)}.                               \tag{12}
\]
Use the time rectangle and product query-angle strip of
`DEEP_COMPLEX_SOURCE.md`, with this common radius. All gradients and
transposes in complex equations are algebraic; norms are complex norms.

For training coordinates, replace that source's carrier-only budget by
\[
\mathcal H=\frac1n\sum_{\ell=1}^L\sum_i
\exp\{\eta[Z_i^{(\ell)}+K_i^{(\ell)}/S]\},          \tag{13}
\]
where `Z_i` and `K_i` are suprema of absolute training preactivation and
carrier values on the current complex time rectangle. Fix `eta>0`.
Stop the full budget at `B`, cavities at `2B`. Include the original
training/query pole caps, the original forward/angular response caps,+and a passive-query preactivation cap `C_q ell_n^(L+2)`. The latter
controls deleted query activation amplitudes; it is not put into an
empirical exponential budget. Cavities have twice each coordinate cap.

On a common pole-safe prefix, (7) still holds with enlarged `K`, by (3).
The algebraic residual Gram has bounded norm because forward and backward
RMS norms are bounded. Extending from each real time only along its short
vertical segment, and the short negative real segment at initialization,
therefore gives `||c(t)||_m<=C Y exp(-g max(Re t,0))`, activity at most
`S`, bounded hidden operators, `||A||_op/sqrt(n)<=C`, and
`||w||_(2,n)<=CS`. No complex growth is integrated over the whole horizon.
This supplies an RMS tube; it does not assert a readout coordinate bound.

Budget (13) gives training coordinate caps `Z_i<=C log n` and
`K_i<=CS log n`, and
\[
\|k_a^{(\ell)}\|_{p,n}\le CS p(2B)^{1/p},\qquad p\ge2,       \tag{14}
\]
for every layer, including `L`. Constants here may depend on the fixed
`eta`. The exact Hessian is a fixed sum of bounded-rank bounded terms and
\[
D z_a^{(\ell)\top}
 \operatorname{diag}(\phi_\ell'' k_a^{(\ell)})D z_a^{(\ell)}.
\]
The forward derivative maps have bounded operator norm because a hidden
variation is `U_H h/sqrt(n)` and (7) bounds its coefficient RMS. Thus
the supplied normalized Schatten estimates are now
`C[1+Sp(2B)^(1/p)]` at every layer; their `p=2` bounds use RMS alone.
This is precisely the top-carrier repair missing from a derivative-only
substitution in the bounded proof.

The negative-Gram variational base contracts on positive real time. All
non-real/backward portions cost one bounded factor, since their total
length is `O(r_n)`. The residual-Hessian part has operator bound
`C(1+S log n)` and total activity `S`. Taking fixed labels small enough
gives the same `n^(1/1000)` propagator bound as the supplied insertion
lemma. Adding `(13)` changes neither its numerical powers nor its entropy
comparison.

## 5. Local insertion with unbounded values: all changed terms

At an interior deleted neuron let `x_i` be its outgoing initialized
column and `y_i` its incoming initialized row transposed. They are
independent `N(0,I/n)` conditional on retained initialization. The exact
retained equation is the supplied forward source plus reverse force,
with its own forward residual, and actual controls `h_i` and `delta_i`.
On (13), their amplitudes are `C(1+Z_i)` and `C K_i`; the temporary
query cap also bounds every passive-query `h_i` by a polynomial logarithm.
The learned column and row obey, on each contour,
\[
\|\Delta W^{(j+1)}_{:,i}\|_2\le CS^2(1+Z_i)/\sqrt n,
\qquad
\|\Delta W^{(j)\top}_{i,:}\|_2\le CSK_i/\sqrt n.       \tag{15}
\]
These follow directly by integrating (1): the other factor in each
rank-one update has bounded RMS. Multiplication by its omitted control
leaves `n^(-1/2) polylog(n)` source remainders. At passive queries the
extra factor is also polynomial logarithmic by the temporary query cap.

All retained feature multipliers in vector and gradient-block estimates
use RMS. A reference activation multiplying `U_H/sqrt(n)` costs
`C||U_H||_F`; a difference obeys `||Delta h||_2<=s||Delta z||_2`;
products of two changed hidden factors retain `1/sqrt(n)`. Scalar Taylor
remainders use (3). The existing augmented-graph proof therefore applies
to `z,h,k,delta,R,Q,J`: any reference activation coordinate used as a
coordinate multiplier has at most a polynomial logarithm, and all its
derivatives have fixed strip bounds. This replaces each formerly bounded
zeroth-order gate use and introduces no power of width.

In detail, the linear response has Euclidean radius `n^alpha`,
`alpha=1/100`, and vector-coordinate radius `n^(-beta)`, `beta=1/10`.
For nonlinear state remainder `u<=n^(-1/25)`, every augmented vector
remainder is bounded by a fixed polynomial logarithm times
\[
n^{\alpha-\beta}+n^{-\beta}u+u^2
+n^{-1/2}(n^{2\alpha}+n^\alpha u+u^2)+n^{-1/2}.        \tag{16}
\]
This is obtained node by node: `||v^2||_2<=||v||_infty||v||_2`,
mixed `v,u` terms use the small linear coordinate norm, and matrix cross
terms retain the displayed `n^(-1/2)`. Independent incoming-row probes
have the same small coordinate norm. Their changed-gate products give
the additional `n^(2alpha-beta)` reverse remainder. The adaptive scalar
residual remainder contributes the existing unweighted matrix-cross term,
because its scalar normalization is `1/n` and the gradient norm is
`C sqrt(n)`. No full residual is supplied to the cavity.

Controls have amplitudes `polylog(n)` and Lipschitz constants
`sqrt(n) polylog(n)`. Their one-dimensional contour net has log cardinality
`n^(5/8) polylog(n)`. Real/imaginary Gaussian splitting gives the same
`exp(-c n^0.79)` coordinate and centered quadratic tails; polynomial
time/query grids add only `O(log n)` entropy. Uniformity is established
before substituting actual root-dependent controls. After integration
and the `n^0.001` propagator, (16) and the reverse `n^-0.08` term are
`o(n^-0.04)`. Thus the same bootstrap closes, and retained preactivations,
carriers, and augmented response coordinates differ by `O_r(n^-1/30)`.
The joining scalar segments stay in the safe strip because these
coordinate increments vanish. This proves the modified local interface.

At the top the exact omitted offset is
`d_a=sum_i w_i h_(a,i)^L/n`, and the retained velocity is
\[
-\frac2m\sum_a(r_a^0+d_a)
 [\nabla F_a^0+D h_a^{(L-1)\top}q_a],\qquad
q_a=\sum_i W_{i,:}^{(L)\top}\delta_{a,i}^{(L)}.        \tag{17}
\]
Here `r_a^0=f_a^0-y_a` and `F_a^0=n f_a^0`. The offset multiplies
both terms. Budget (13) gives `|d_a|<=n^-1 polylog(n)`, so its gradient
contribution is `n^-1/2 polylog(n)` and its reverse contribution is
`n^-1 polylog(n)`. Both fit (16). There is no outgoing Gaussian root
at this layer; its independent incoming root and reverse force remain.

## 6. Complex reciprocal traces and removal of the joint budget

The backward scalar reinsertion trace must keep its actual forward
amplitude. The supplied two-endpoint Schatten argument, with (14) also
at the top, bounds it by
`CS(1+S^2B) sup|h_i|`. The direct external trace uses carrier RMS;
the learned-column term in (15) costs `CS^3(1+Z_i)`. Incoming/outgoing
cross forms are centered on the uniform event. Consequently the first
inequality in (10) holds with complex-domain suprema.

For the forward scalar trace the endpoint maps `D h` are bounded.
Expand the propagator minus its negative-Gram base. Assign Schatten
exponent `2h` to its `h>=1` residual Hessians. Its normalized
Hilbert--Schmidt norm is bounded by
\[
\sum_{h\ge1}\frac{(CS)^h}{h!}
[1+2Sh(2B)^{1/(2h)}]^h\le C(S+S^2\sqrt B),          \tag{18}
\]
at sufficiently small `S`. The bounded terms sum exponentially and the
carrier terms form a geometric series, using `h^h/h!<=e^h`.
The short complex base factors only enlarge the fixed constant.
The base trace itself is bounded because the endpoints factor through
a width-dimensional space; no Hilbert--Schmidt norm of the full
parameter-space identity is used. Integrating the actual reverse
amplitude `|delta_i|<=C K_i` and adding the learned-row term yields
the second inequality in (10), again with complex suprema. First and
top layers have the same exact endpoint relations stated after (10).
Thus the scalar absorption (11) holds on the complex domain as well.

It remains to check the Gaussian reference moments on this domain;
a real maximum alone would not do so. Parameterize real paths by
normalized residual activity `u`. Forward physical speeds give
\[
\|h_a(u)-h_a(u')\|_{2,n}\le CS^2|u-u'|.             \tag{19}
\]
The backward cutoff calculation applies at every layer including the
top. At a changed gate split the reference carrier at `S R`. The low
part costs `CS^3 R |u-u'|`; (13) bounds the high part by
`CS sqrt(2B) exp(-c_eta R)`. Choose
`R=C_eta[1+log(e+B)+log(1/|u-u'|)]` and impose
`S^2 log(e+B)<=1`. Downward propagation gives
\[
\|\delta_a(u)-\delta_a(u')\|_{2,n}/S
\le C\sqrt{|u-u'|},                               \tag{20}
\]
with constants independent of `B` after that restriction. The top
readout increment in this argument uses RMS (7), while its changed-gate
term uses the top term of (13). No readout coordinate cap is reused.

Conditional Gaussian chaining for (19)--(20) gives all fixed exponential
moments of real `G_h` and `G_delta/S`, independent of width and budget.
This follows directly from dyadic activity grids: their covering numbers
are `C/epsilon` and `C/epsilon^2`, and summing the Gaussian increments
`C 2^-k(sqrt(k+1)+z)` gives a Gaussian tail. The initial forward
Gaussian value also has fixed exponential moments; the backward starts
at zero.

For the complex-minus-real correction, differentiate the actual backward
recursion on the stopped domain. The operator/RMS tube and (13) give
\[
\|\dot h_a\|_{2,n}\le C\rho S,\qquad
\|\dot\delta_a\|_{2,n}\le C\rho(1+S^2\ell_n).       \tag{21}
\]
For example the changed-gate term is bounded by
`C ||dot z||_(2,n) max|k| <= C rho S^2 ell_n`; changed hidden matrices
give `C rho S^2`, and the readout derivative uses (7). Thus a short
complex segment gives Gaussian coefficient radii
`C r_n` for the forward correction and `C r_n ell_n` for the backward
correction divided by `S`. Their two real time-parameter Lipschitz
constants are polynomial logarithmic by the same differentiated graph.
The time interval length is `O(ell_n)`. Dyadic nets therefore bound their
mean Gaussian suprema by
\[
C r_n\ell_n\sqrt{\log(e+\ell_n)}=o(1),              \tag{22}
\]
and their Gaussian fluctuation scales also tend to zero. Every fixed
exponential moment of the correction tends to one. Independently stopped
cavity references are extended/frozen on their own scaled rectangles,
as in the supplied complex-source proof; failed own initialization gives
the zero reference. No root-dependent full survival event is conditioned
on. This proves the required complex Gaussian moments.

The local coordinate comparison transfers the full budget to each cavity:
`H_cavity<=exp[eta o(1)(1+1/S)]H_full+O(r/n)<2B` while `H_full<=B`.
Pole, query-preactivation, and response caps transfer with their doubled
margins. Common-cavity differences are projected as entire independent
paths onto their deterministic Euclidean balls of radius `C_p n^0.01`.
Their Gaussian radius is `C_p n^-0.49`; (19)--(22) or a polynomial
grid give vanishing suprema with all fixed exponential moments. This
preserves independence from the omitted root before restricting to the
successful full prefix.

Expanding the `p`th empirical moment of each layer of (13), for fixed
integer `p`, now gives a base independent of `p` from (11) and the
common-cavity Gaussian moments. Distinct neurons have independent root
pairs conditional on the common cavity. Collision tuples are
`O_p(n^(p-1))` and their higher fixed exponential moments make their
normalized contribution vanish. The stopped budget bounds exceptional
contributions. Remove full-event indicators only after obtaining the
nonnegative independent-reference upper bound. Choose `B` larger than
the resulting fixed layer-summed base and the initialized budget limit,
then choose `S` for all scalar, trace, modulus and variational restrictions.
Markov gives a limiting budget-hit probability at most `q^p`, `q<1`.
First send width to infinity at fixed `p`, then take the infimum over
fixed `p`. This removes the joint budget without a moment-degree-dependent
label threshold.

The initialized budget and all fixed-deletion starts are precisely the
ones proved in the authorized unbounded source: conditional Gaussian
moments on bounded preceding covariances, plus coordinate-small deletion
transfer. The new complex suprema reduce to those real initialized values
at scale zero. Thus no new initialization moment premise was inserted.

## 7. Passive query caps and spectral source magnitude

Define the residual-free forward responses and angular responses by
\[
R_a^{(\ell)}(v)=D_\Theta z^{(\ell)}(v)\nabla_\Theta(n f_n(v_a)),
\quad Q_a^{(\ell)}=\phi_\ell'(z^{(\ell)})\odot R_a^{(\ell)},
\quad J_j^{(\ell)}=\partial_{\theta_j}z^{(\ell)}(v(\theta)),
\]
where `Theta=(A,sqrt(n)W^(2),...,sqrt(n)W^(L),w)`.
Their exact recurrences are unchanged:
\[
R_a^{(1)}=\delta_a^{(1)}v_a^\top v,\quad
R_a^{(\ell)}=\delta_a^{(\ell)}
\frac{h_a^{(\ell-1)\top}h^{(\ell-1)}(v)}n
+W^{(\ell)}Q_a^{(\ell-1)},
\]
\[
J_j^{(1)}=A\partial_{\theta_j}v,\quad
J_j^{(\ell)}=W^{(\ell)}
[\phi_{\ell-1}'(z^{(\ell-1)})\odot J_j^{(\ell-1)}].       \tag{23}
\]
Their RMS bounds use (7), bounded derivative gates, and bounded input
derivatives. The mixed endpoint recursions in the supplied source use
reference features only in normalized matrix actions or pairings. Hence
their Hilbert--Schmidt and higher Schatten bounds remain valid. Every
Hessian occurrence now uses (14) at all layers.

Row reinsertion at level `p+1` has the same two means: the direct reverse
observable trace and the mixed endpoint trace. Its training reverse
amplitude is `K_i<=CS ell_n`. The learned row has norm
`CS K_i/sqrt(n)` by (15), and its query-feature or response pairing uses
RMS. Query forward-source amplitudes enter only the already controlled
linear Gaussian fluctuations and remainders. They do not become a new
same-root reverse trace. Thus, if `A_p` bounds the lower response,
the exact triangular bounds remain
\[
\max|R_a^{(p+1)}|
\le C\{S\ell_n+S\sqrt{\ell_n}
       +S^2\ell_n(1+A_p)+S^3\ell_n\}+o(1),
\]
\[
\max|J_j^{(p+1)}|
\le C\{\sqrt{\ell_n}+S^2\ell_n(1+A_p)+S^2\ell_n\}+o(1).
                                                               \tag{24}
\]
These are exactly the supplied source's upper recurrences after replacing
bounded feature coefficients by the fixed RMS constants in (7). They
involve lower-level query gates only. Increasing the fixed layer constants
gives strict bounds `C_ell S ell_n^(ell+1)` and
`C_ell ell_n^(ell+1)`, respectively. At the first layer integrate its
coordinate update and use the initialized row maximum, giving the
required `C ell_n` angular cap and the first response cap.

For completeness the whole real initial query sphere has preactivation
maximum `C sqrt(ell_n)` with probability tending to one. At each layer
condition on lower initialized features; their normalized norms are
bounded by (7). Gaussian row tails on a fixed polynomial query mesh
therefore suffice. Between mesh points, the deterministic coordinate
Lipschitz bound from initialized operators and bounded slopes is a fixed
power of `n`; a finer polynomial mesh controls the interpolation. This
argument is performed conditionally before intersecting the current
matrix operator event. The first layer is the same Gaussian-row estimate.

Integrating (24) against real residual activity, then along the short
complex time/query segments, bounds every query preactivation by
`C ell_n^(L+1)`. This improves the temporary `C_q ell_n^(L+2)` cap.
Its imaginary part is at most
\[
C(1+YS)r_n\ell_n^{L+1}=O(\ell_n^{-3}),              \tag{25}
\]
which improves the fixed pole cap. The doubled cavity caps cannot be
reached first by the local coordinate comparison. Thus the response,
preactivation and pole stops are removed in layer order before the final
joint-budget argument. This closes their apparent dependence on each
other; no query pole was assumed to prove itself.

Now use whole-query passive backward recursions as source families too.
They impose no training force. On the proved pole-safe domain their
holomorphy is immediate from the finite recursion, and their RMS is at
most `CS` by operator bounds and `||w||_(2,n)<=CS`. Consequently all four
families
\[
h^{(\ell)}(t,v),\quad W_0^{(\ell)}h^{(\ell-1)}(t,v),\quad
\delta^{(\ell)}(t,v),\quad
W_0^{(\ell+1)\top}\delta^{(\ell+1)}(t,v)              \tag{26}
\]
have coordinate magnitude at most `C sqrt(n)`, uniformly on the complex
domain. This bound follows from RMS, so it does not require a query
carrier exponential budget. Joint holomorphy includes a neighborhood of
the closed domain because all cap inequalities are strict.

The inherited time/angle polynomial construction at source tolerance
`epsilon=n^-1` now uses temporal degree `C ell_n^(L+6)` and each angular
degree `C ell_n^(L+5)`. Indeed the error logarithm contains
`log(C sqrt(n)/epsilon)=O(ell_n)`, while `T/r_n=O(ell_n^(L+5))`.
Four whole-query families therefore have real source rank at most
\[
R\le C\ell_n^{d(L+5)+1}+2m+d+1.                    \tag{27}
\]
The initialized training vectors, their paired images, first-weight
columns, and the constant are included exactly. Apply identical scalar
initial-jet continuation and coefficient operations to each source and
its initialized image. Their matrix-image identities are exact while
both members have their own coordinate error. This is the supplied
initialization-only construction; no trained values are used. Its
temporary jets and original-width coefficient vectors are discarded.

## 8. Runtime bridge under linear growth

For diagonal cubature, total mass one gives directly
`||phi(z)||_D<=b+s||z||_D`. For the corrected-readout metric of
`STORAGE_QUADRATIC_IMPROVEMENT.md`, its proved relations are
`D/4<=H<=D` and exact isometry on each source space. Since the constant
belongs to that space, `||1||_H=1` and `||1||_D<=2`. Therefore
\[
\|\phi(z)\|_H\le2b+2s\|z\|_H,\qquad
\|\operatorname{diag}(\phi'(z))\|_{H\to H}\le2s.     \tag{28}
\]
The initial first-weight operator is controlled exactly because all its
columns belong to the source space. The initial hidden operators are
contractive projections of the original ones. Recurrence (7), with
the factors in (28), hence supplies uniform sphere feature norms in a
fixed selected-operator tube, independently of minimum selected mass.

The corrected runtime's raw-parameter energy identity and orthogonal
readout decomposition give `||widehat w_C||_H<=CY/sqrt(g)` on its
stopped Gram margin, exactly as in its source. Hidden updates have norm
at most `C rho_C ||widehat w_C||_H` using (28). Their integrated
displacement is `CY^2/g^(3/2)`. Forward Lipschitz propagation and the
initial singular-value margin close the tube at small fixed labels.
This proves its independent all-time fitting and RMS bounds without
bounded activation values or a coordinate readout estimate.

Every pairing and initialized-action defect uses RMS and coordinate
approximation, so the existing `C epsilon` defects are unchanged. The
changed-gate term is bounded by the actual reference training-carrier
maximum (9), which includes the readout. The runtime comparison hence
retains the bound
\[
\sup_{t\le T,v}|f_C-f_n|
\le C\epsilon\exp[C(1+M)S],\qquad
M\le1+CS\sqrt{\ell_n},                              \tag{29}
\]
where fixed Gram-conditioning factors have been included in `C`.
At `epsilon=n^-1`, its right side is at most `C n^-1/2` for sufficiently
large width. No fixed coefficient multiplying `sqrt(log n)` is claimed
to disappear; that subpolynomial factor is explicitly absorbed by the
extra half power in source accuracy.

For both flows the sphere feature norms and their time derivatives are
bounded by the same RMS recurrences. The corrected readout derivative
uses only its bounded feature matrix, inverse Gram, and parameter speed,
as in the supplied runtime proof. Thus their sphere-uniform tails are
`C exp(-g t)`. Take `C_T` large enough in (12); both tails are
`O(n^-1/2)` beyond `T`, while each model continues autonomously. Combining
with (29) proves (5), including exact fitting and convergence at infinity.
The retained inventory is `C(R^2+dR)+Cm(d+1)` for that runtime, giving
(6). The diagonal alternative uses `C R^4` and the same proof with its
actual gradient Gram. Neither construction retains original dense matrices.

## 9. Identity is included, but is a different scientific boundary case

For `phi_ell(z)=z`, (2) holds with `b=0`, `s=1` and any fixed strip
width. Equation (4) reduces exactly to
\[
Q^{(L)}=Q^{(0)}=(v_a^\top v_b)_{ab}.                 \tag{30}
\]
Thus the gap condition is exactly linear independence of the training
inputs, necessarily `m<=d`. The output remains linear in `v` throughout
training. This identity specialization is an actual theorem for the
canonical finite deep linear reference, at the same physical times;
it does not turn the broad nonaffine theorem into a linear theorem or
claim arbitrary labels can be fitted when (30) is singular.

There is also a stronger elementary affine source bound. Suppose every
`phi_ell(z)=alpha_ell z+b_ell`. Each feature is affine in `v`, and each
backward response is independent of `v`. All activation gates are scalar
constant matrices, so changed-gate terms vanish. On the physical RMS
tube, the polynomial vector field (1) has width-independent local bounds
and Lipschitz constants in the norm consisting of normalized first-weight
operator norm, hidden operator norms, and readout RMS. Picard iteration on
a fixed complex disk around each real time therefore gives a fixed-width
time strip, with bounded normalized source norms. Overlapping disks agree
by uniqueness. There are no activation poles.

Time Chebyshev approximation on `[0,T]`, `T=C log(en)`, at normalized
vector error `n^-1` consequently has degree `C log(en)^2`. Its coefficient
vectors for the `d+1` affine feature coefficients and one backward vector
per layer span a space of dimension
\[
R_{\rm aff}\le C(d+2)\log(en)^2+2d+2.               \tag{31}
\]
Include the constant, exact initialized affine feature coefficients, and
initialized first-weight columns. These spaces
can use orthogonal projection directly, without neuron sampling. To verify
that this still gives the same activation architecture, let `T_ell` be an
isometry from the reduced counting norm `1/r_ell` to the original norm
`1/n`, with range the source space and `T_ell 1=1`. Such an isometry exists
by choosing orthonormal bases taking the normalized constant to the
normalized constant. Then
\[
T_\ell\phi_\ell(u)=\phi_\ell(T_\ell u),\qquad
T_\ell^*\phi_\ell(z)=\phi_\ell(T_\ell^*z).          \tag{32}
\]
Both identities use the scalar slope and constant-preservation property.
Initialize `A_C=T_1^*A_0`, `B_C^ell=T_ell^*W_0^ell T_(ell-1)`,
and zero readout. Use ordinary weighted gradient flow with masses
`1/r_ell` and its own residuals.

For proof only set `A_R=T_1^*A`, `w_R=T_L^*w`, and
`B_R^ell=T_ell^*W^ell T_(ell-1)`. Projection of (1) gives exactly the
same rank-one equations driven by projected original features, responses,
and original residual. The forward action defect is
\[
-T_\ell^*W^\ell(I-T_{\ell-1}T_{\ell-1}^*)h^{\ell-1},
\]
whose reduced norm is at most `C n^-1`. The reverse defect has the
same form with `W^T` and the projected upper response. The readout belongs
within `C n^-1` of its source space by integrating top training features.
Hence its observation defect is also `C n^-1`. All initial training
features and the initialized Gram are exact if those finitely many vectors
are included. Equation (32) and constant gates give forward/backward
comparison error `C(d_state+n^-1)` with no coordinate carrier maximum.

Subtracting the two exact residual Gram equations and integrating their
positive damping yields
`int ||c_C-c_n||_m <= C int rho_n(d_state+n^-1)`. Parameter subtraction
then gives the same right side for `d_state`. Residual activity is bounded,
so integral Gronwall yields `sup d_state<=C n^-1` through `T`. The
independent energy/Gram argument from Section 3 applies to both reduced
and original affine systems, and their sphere tails are `O(n^-1)` after
increasing `C_T`. Thus this affine construction has error `C/n` and total
retained storage `C(R_aff^2+d R_aff)+Cm(d+1)=O(log(en)^4)` at fixed data.
Its coefficients use the same finite initial-jet continuation as above;
its runtime contains only the projected neural matrices and data.

This affine refinement is separate from the nonlinear extension. For
`phi(z)=alpha z+b+psi(z)` with nonconstant bounded analytic `psi`, (32)
usually fails. The affine projection theorem is therefore not an argument
for the nonlinear class.

## 10. A genuinely nonlinear unbounded class and the quantitative boundary

If `psi_ell` is bounded and holomorphic on a strip wider than the one
retained, then
\[
\phi_\ell(z)=\alpha_\ell z+b_\ell+\psi_\ell(z)
\]
satisfies (2) by Cauchy's derivative bound for `psi`. A concrete family is
\[
\phi_\ell(z)=z+\varepsilon_\ell\tanh z,
\qquad \varepsilon_\ell\ne0.                         \tag{33}
\]
On `|Im z|<pi/4`, `|tanh z|<=1` and `|sech^2 z|<=2`, as follows
from `|cosh(x+iy)|^2=sinh^2 x+cos^2 y`. Thus (2) holds with
`a=pi/4`, `b=0`, `s=max_ell(1+2|epsilon_ell|)`. These activations are
unbounded and nonaffine. They satisfy the nonlinear theorem (5)--(6),+under the explicit gap and sufficiently small fixed labels; they do not
use the affine shortcut.

For nonaffine activations with bounded derivative, the supplied
finite-difference argument for nonproportional inputs still supplies an
automatic first-layer gap. A vanishing feature combination implies the
activation is a polynomial of degree at most `m-2`; a polynomial with
bounded derivative is affine, contradicting nonaffinity. For `m=1,2`
the same argument simply excludes the zero or constant function. After
the first positive definite covariance, full Gaussian support and
nonconstancy propagate the gap. Thus (33) permits arbitrary fixed numbers
of pairwise nonproportional sphere inputs, including `m>d`. This is a
substantive difference from identity. The explicit gap (4) is sufficient
and is the only condition used in the theorem.

The following claims are deliberately **not** inferred:

* The existing numerical envelope `Y<=(gamma/m) beta^(-62L)` has not been
  recomputed for the joint budget. Real feature RMS grows with depth under
  (7), and the reciprocal feedback coefficients and initial joint-budget
  moments must appear in any transparent replacement.
* The improved radius `c/sqrt(log n)`, spherical storage coefficient,
  and strict root-width folding constants need their own quantitative
  joint-budget reconstruction. This file proves the conservative radius
  (12); it does not substitute `(a,b,s)` into the latest numerical beta.
* The broad class is strip-analytic with uniformly bounded strip derivative.
  A merely real bounded-derivative `C^3` hypothesis supplies the imported
  real theorem but not the analytic compressor.
* The affine `O(log^4 n)` construction and its `C/n` error do not extend
  by declaring a small nonlinear perturbation harmless at fixed amplitude.

The decisive check for the candidate nonlinear extension is the combination
of Sections 5--7: both actual-amplitude complex traces, the top-carrier
budget and offset, vanishing complex Gaussian moments, and triangular
query-pole removal. Everything after that is the supplied deterministic
runtime with the explicit RMS replacement (28). A successful review of
those interfaces would establish the qualitative unbounded nonlinear
extension; it would leave the listed quantitative improvements open.
