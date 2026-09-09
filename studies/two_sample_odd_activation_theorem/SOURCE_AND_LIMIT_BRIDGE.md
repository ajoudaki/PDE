# Offset-free two-input theorem: source and physical bridges

Source and limit lemma, 2026-09-07. This note supplies the source/bridge
extension; it does not assume the old offset activation's scalar symmetry,
affine coercivity, affine variance bound, or initial-motion lemma. Those
are separate obligations for the new theorem.

The sources used are:

- `sources/THREE_SAMPLE_CONTROLLED_RESPONSE_LEMMA.md`, in full;
- `sources/PREVIOUS_TWO_SAMPLE_PROOF.md`;
- its sources `TWO_SAMPLE_SOURCE_BASELINE.md`, especially Sections 3–8;
- `NONLINEAR_RESPONSE_PERTURBATION.md`, including the finite-stage closure;
- `PRIMAL_COMPARISON_AND_CONTINUATION_BRIDGE.md`, in full;
- `FIXED_CAP_VELOCITY_BRIDGE.md`, including its hypotheses, probe and velocity queries, and ordered cap removal;
- the generic finite Gaussian-conditioning, singular-query, common-action, and adjunction portions of `L3_LOCAL_COMPLETE_PROOF.md`.

## 1. Precise extended source statement

Let

\[
\phi_{a,e}(z)=az+e\arctan z,\qquad
\tfrac12\le a\le1,\quad 0\le e\le1,
\]
\[
D_{a,e,R}(z,q)=a q+e g(z)\tau_R(q),\qquad g(z)=(1+z^2)^{-1}.
\]

Use the existing smooth odd clips: \(|\tau_R|\le\min(|q|,2R)\),
\(|\tau_R'|\le1\), and \(\tau_R(q)=q\) for \(|q|\le R\).
Let there be two samples, a PSD unit-diagonal correlation matrix \(\Gamma\),
a deterministic positive mesh of total duration at most \(S>0\), and
frozen controls \(c_k\in\mathbb R^2\) with \(\|c_k\|_1\le1\).
Write \(P_k=\Gamma\operatorname{diag}(c_k)\), so \(|P_k|_\infty\le1\).

Assume the actual affine Euler programs, with activation \(az\), the SAME
control sequence and mesh, obey the finite-array primal hypothesis
\(\mathsf P(P,S)\), with \(P\ge1\), from baseline equation (18). Bounds
are required at each fixed mesh on events of probability tending to one;
a uniform probability assertion over growing transcripts is unnecessary.

There are \(E_*(P,S)>0\) and \(K(P,S)<\infty\), independent of
\(a\in[1/2,1]\), correlation, controls, meshes, and caps, such that, for
\(0\le e\le E_*\), the actual canonical nonlinear source programs have
bounded forward response blocks and backward response time rows, and

\[
\sup_{k,R}\left(\|C_k\|_p+\|q_k^2\|_p+\|q_k^1\|_p\right)
\le K\sqrt p,\qquad p\ge2.
\]

The same holds for the forward fields and deltas. This is a population
source assertion, not a uniform exponential-moment assertion for every
finite-width neuron. The lower gain bound 1/2 is not needed by this lemma;
it is useful in the separate affine/nondegeneracy arguments.

The proof is the controlled response proof with the following verified
changes. No covariance inverse or positive constant offset occurs.

## 2. Source representation and affine coefficients

Keep controlled-response equations (8)–(9) exactly, with two sample slots,
\(H=\phi_{a,e}(Z)\), and \(\delta=D_{a,e,R}(Z,q)\). Covariances are full
second moments of the actual matrix-input fields. A zero feature mean is
allowed; singular source covariances, including the zero initial reverse
sources, are treated by the existing independent-query regularization.
Formal source arguments stay distinct at rank drops. The generic
conditioning theorem requires globally Lipschitz C1 coordinate maps with
bounded first derivatives at fixed cap, and iid initial root tuples with
finite second moments independent of the Gaussian matrices. Here

\[
|\phi'_{a,e}|\le2,\quad |D_q|\le2,\quad |D_z|\le2eR,
\quad |\phi_{a,e}(z)|\le |z|+\pi/2.
\]

These verify the hypotheses. Removing the affine constant does not remove
any source or learned-memory term. In particular the coefficients remain

\[
\mathsf A^\ell_{ki,vj}
=E\partial_{\zeta^{\ell-1}_{v,j}}H^{\ell-1}_{k,i}
+h_v c_{v,j}E[H^{\ell-1}_{k,i}H^{\ell-1}_{v,j}],
\]
\[
\mathsf B^\ell_{ki,vj}
=E\partial_{\xi^\ell_{v,j}}\delta^\ell_{k,i}
+\mathbf1_{v<k}h_vc_{v,j}E[\delta^\ell_{k,i}\delta^\ell_{v,j}].
\]

All deterministic controls, arrays and covariances are frozen in these
formal derivatives. Finite empirical-feedback identification is causal
and uses their converging contractions, not derivatives of the controls.
For the present two-label scalar feature path one simply takes constant
\(c_i=y_i/2\).

At e=0 the equations are linear in the source arguments, with affine
identity gates replaced by aI. For example
\(\delta^3=aC\), \(\delta^2=a^2 B^*C\), and
\(\delta^1=a^3A^*B^*C\). On a primal ball of radius b>=1, every affine
forward/backward norm, state Lipschitz estimate, answer-perturbation
estimate, and output Lipschitz estimate used in baseline Sections 5–7 is
bounded above by its displayed a=1, offset=1 bound. This assertion follows
term by term: the removed affine constant contributed only nonnegative
addends to the norm estimates, and every additional gain is in [0,1].
In particular the raw affine field is 9b^2-Lipschitz and bounded by
10b^3 in the existing sum norm. The four answer perturbation constants
2b, 1, 3b, 1 from the baseline table remain valid. Their Gaussian probe
identity is unchanged: the program is affine in the new independent
Gaussian root, whether its deterministic affine constant is zero or not.
It yields the same mesh factors and row sums.

Put \(F=\exp(36P^2S)\). For constant \(c_i=y_i/2\), admissible block/time-row
bounds are exactly the existing ones:

\[
A_0=2(24P^2F+\tfrac92P^4),\qquad
M_0=2S(8P^2F+P^4).
\tag{1}
\]

For arbitrary frozen controls with \(\|c_k\|_1\le1\), the conservative
choice \(A_0=2(24P^2F+9P^4)\), with the same \(M_0\), avoids the
individual bound \(|c_i|=1/2\) in baseline equation (29). Either choice
is uniform in a. The factor 2 converts scalar output rows into the sum of
maximum row-sum norms of two-by-two time blocks.

If a bounded continuous affine reference has projected primal bound U,
then sufficiently fine population Euler arrays have bound 2U by the
9b^2 bounded-ball Euler estimate. Baseline Section 8 still gives the
finite-array premise with

\[
P=11+2U+4S(2U)^3.
\tag{2}
\]

Indeed initial finite operator norms are at most 10 with probability
approaching one; exact rank-one unrolling bounds learned operator
increments by the finite sums of update-factor RMS products. Their
population limits have the old upper bounds 2S(2U)^3 and 3S(2U)^3, and
are smaller for the zero-offset affine activation. This does not infer
operator-norm convergence of trained matrices.

## 3. Uniform primal perturbation and derivative closure

At a common state of primal size at most b>=1, the original conservative
same-state table remains valid, uniformly in a and cap:

\[
\begin{array}{c|ccc}
 &1&2&3\\ \hline
\|H_e^\ell\|_2&4b&7b^2&10b^3\\
\|H_e^\ell-H_0^\ell\|_2&2e&4eb&6eb^2
\end{array}
\]
\[
\|\delta_e^3\|_2\le2b,\quad
\|\delta_e^2\|_2\le4b^2,\quad
\|\delta_e^1\|_2\le8b^3,
\]
\[
\|\delta_e^3-\delta_0^3\|_2\le eb,\quad
\|\delta_e^2-\delta_0^2\|_2\le3eb^2,\quad
\|\delta_e^1-\delta_0^1\|_2\le7eb^3.
\]

For example the middle backward difference is at most
\(a\|q_e^2-q_0^2\|_2+e\|q_e^2\|_2\le eb^2+2eb^2\).
The four raw-update differences are at most 7,14,11,6 times eb^3,
by the rank-one HS norm inequality. Thus

\[
\|V_{a,e,R,c}(\theta)-V_{a,0,c}(\theta)\|_{\mathcal X}
\le40eb^3,\qquad \|V_{a,e,R,c}\|_{\mathcal X}\le50b^3.
\tag{3}
\]

These also hold in finite normalized norms. Comparison with the affine
field, using only that field's 9b^2 Lipschitz constant, gives

\[
\sup_{s_k\le S}\|\theta^e_k-\theta^0_k\|_{\mathcal X}
\le40eb^3S\exp(9b^2S).
\tag{4}
\]

For the finite-array premise \(\mathsf P(P,S)\), take b=2P. A sufficient
restriction for discrepancy at most P/2 is

\[
e\le [640P^2S\exp(36P^2S)]^{-1}.
\tag{5}
\]

This is a deliberately conservative replacement of the original 480
restriction, consistent with using 40 instead of the sharper 30 in the
perturbation source. For a continuous reference of bound U and b=4U,
(4) supplies the raw strong comparison with
\(Q=40b^3S\exp(9b^2S)\), precisely as in the two-input proof.
All actual source variances are now bounded independently of cap, mesh,
and a; for example the oversized scalar standard-deviation bound
\(\sigma=8b^3\) suffices on the closed primal ball.

For the response induction write A=A_0+1 and M=M_0+1. The derivative
matrices are exactly

\[
G=aI+e\operatorname{diag}(g(Z)),\quad
V=aI+e\operatorname{diag}(g(Z)\tau_R'(q)),\quad
L=e\operatorname{diag}(g'(Z)\tau_R(q)).
\]

Hence \(|G-aI|,|V-aI|\le e\), \(|L|\le eQ_r\), and all upper derivative
bounds are the a=1 bounds with d_a=a+1 replaced by 2. The exact affine
recursions (11) and all-index recursions (17) of the controlled-response
proof remain exact. The offset had derivative zero, so it never occurred
in them. Its moment inequalities (19) remain upper bounds, since the
constant term in \(|H|\) decreases from a+e*pi/2 to e*pi/2. No monotonicity
of an actual trajectory in a is asserted or needed.

More explicitly, choose K0 depending only on sigma large enough to bound
every pair of Gaussian-source coordinates by K0*sqrt(p). The old
Volterra moment bounds may be replaced by the following uniform bounds:

\[
\max_{v\le k}\|H_v^1\|_p
\le K_0(1+2S)e^{2MS}\sqrt p,
\]
\[
\max_{v\le k}\|H_v^2\|_p
\le K_0(1+2AS)e^{2AMS}\sqrt p,
\qquad
\max_{v\le k}\|C_v\|_p
\le K_0 S e^{2AS^2}\sqrt p.
\tag{6}
\]

Enlarge K0 to absorb the bounded arctangent terms. The two q norms then
use \(\|q^i_k\|_p\le K_0\sqrt p+M\max_{v\le k}\|H_v^i\|_p\).
These give a cap/mesh/gain-uniform subGaussian Q_r. The derivative envelope
is \(\exp\{Ks_k+Ke\sum_{r<k}h_rQ_r\}\); backward outputs retain the
necessary current factor \(K(1+eQ_k)\). Its finite moments follow from
these subGaussian bounds and the convexity inequality in Section 3.4 of
the controlled-response proof, without a random supremum over time.

The exact same-array affine bounds (21) in that proof can be replaced by

\[
K_F=e^{MS},\quad K_V=Ae^{AMS},\quad
K_U=e^{AMS},\quad K_T=Se^{AS^2}.
\tag{7}
\]

They dominate their displayed gain-dependent formulas. Likewise each
coefficient in inequalities (22)–(26) is dominated by the expression
obtained by setting all unindexed a and a^2 equal to one. The perturbative
forcing estimates remain Ke*h_j for one transpose-source slot and Ke
for a full forward-source row. All current L_k J_k contributions are
retained and have expectation O(e) by (6) and the envelope moments.

Consequently the literal chronological order

\[
\alpha_k^2,\quad \alpha_k^3,\quad \beta_k^3,\quad \beta_k^2
\]

satisfies, with one K=K(P,S,A_0,M_0)>=1 independent of a,

\[
\alpha_k^2,\alpha_k^3,\beta_k^3,\beta_k^2
\le K(e+I_k),\qquad
I_k=\sum_{r<k}h_r(\beta_r^2+\beta_r^3),
\]
\[
E_k:=\beta_k^2+\beta_k^3
\le Ke+K\sum_{r<k}h_rE_r.
\tag{8}
\]

K is chosen from the finite displayed algebra and the just-bounded
envelope moments with a replaced by its upper bound; it is not a
pointwise threshold later optimized over a. Discrete Gronwall and the
four-stage induction of the supplied proof now apply verbatim. An
admissible uniform response threshold is

\[
E_*(P,S)=\min\left\{1,
\frac1{640P^2S e^{36P^2S}},
\frac1{2K e^{KS}}\right\}>0.
\tag{9}
\]

The current returns still are

\[
(\mathsf B^3_{kk})_{ij}=\mathbf1_{i=j}EL^3_{k,i},
\]
\[
(\mathsf B^2_{kk})_{ij}=\mathbf1_{i=j}EL^2_{k,i}
+(\mathsf B^3_{kk})_{ij}E[V^2_{k,i}G^2_{k,j}].
\]

They are O(e); they are neither discarded nor inverted. This proves the
extended controlled source lemma with the stated quantifiers.

## 4. Cap removal and global physical conversion

For R'>=R, allowing R'=infinity, the exact asymmetric difference is

\[
\begin{aligned}
D_{a,e,R'}(z_A,q_A)-D_{a,e,R}(z_B,q_B)
={}&a(q_A-q_B)\\
&+e g(z_A)[\tau_{R'}(q_A)-\tau_{R'}(q_B)]\\
&+e[g(z_A)-g(z_B)]\tau_R(q_B)\\
&+e g(z_A)[\tau_{R'}(q_B)-\tau_R(q_B)].
\end{aligned}
\]

Its L2 norm is at most

\[
2\|q_A-q_B\|_2+2eR\|z_A-z_B\|_2
+2e\||q_B|\mathbf1_{|q_B|>R}\|_2.
\tag{10}
\]

The original 4eR bound also remains safe. Successive substitution through
forward propagation and the three backward gates yields exactly the
old form

\[
\|V_{R'}(\theta_A)-V_R(\theta_B)\|_{\mathcal X}
\le C_b(1+eR)\|\theta_A-\theta_B\|_{\mathcal X}
+C_be\sum_Q\||Q_B|\mathbf1_{|Q_B|>R}\|_2.
\tag{11}
\]

C_b can be independent of a. There is one factor R, not its third power:
only a forward-state difference gets the R coefficient at a gate; an
incoming backward discrepancy is multiplied by at most 2.
The source lemma gives Gaussian L2 tails for the reference Q. Therefore
cap paths and their raw directions converge strongly on the complete
fixed feature interval, with error bounded by
\(C\exp(C(1+eR)S-cR^2)\). The asymmetric estimate compares any other
bounded-primal uncut strong solution to the cap reference and requires
no tails of the competitor. It proves uniqueness, including restart
from any reached state, on the same generated action spaces.

For the physical bridge the following are sufficient additional inputs
from the new scalar-symmetry argument:

1. The feature flow and every cap feature flow satisfy f_i=y_i*g,
   with g(0)=0, on a bounded interval [0,S].
2. The uniform raw comparison gives g_R(S)>1, for every cap and for
   the uncut path.

**No nonlinear radial lower bound is needed for global physical
existence at this stage.** Let s_R be the first hit of 1. Continuity
implies g_R(s)<1 for s<s_R. Boundedness of its derivative gives
\(1-g_R(s)\le M_R(s_R-s)\). Hence

\[
t_R(s)=\int_0^s\frac{du}{2(1-g_R(u))}
\]

diverges as s approaches s_R. Its inverse solves ds/dt=2(1-g_R), and
reparametrizes the feature path into the exact two-residual physical
field for all finite times. Monotonicity of g_R is unnecessary; the
capped feature field need not be a gradient. The argument equally
applies to the uncut path. Uniform compact primal bounds and reference
incoming tails are inherited from the complete feature interval.
Physical-field local Lipschitzness at fixed cap follows from (11) and
the locally Lipschitz prediction contractions. On every fixed physical
[0,T], (11) has the same form, with constants depending on T. The
Gaussian tail defeats exp(C_T R) for every finite T, without further
smallness of e. Uniqueness against nonsymmetric physical competitors
uses their individual residuals in this physical estimate, and does
not assume their scalar symmetry.

## 5. Finite GF, raw GD, hidden velocities, and path laws

The generic conditioning/common-action construction does not need a
positive activation offset or a gain >=1. Its coordinate hypotheses were
checked in Section 2. The canonical action bounds and actual adjoints
follow from finite Gaussian operator bounds and finite transpose
identities on the countable generated probes. No claim is made that all
uncountably many choices of a have been realized simultaneously.

The physical fixed-cap reference has bounded paths and source moments.
At any fixed physical mesh, the finite source law identifies both actual
finite residuals and every learned contraction. Exact rank-one
unrolling bounds finite current operators by their initial bound plus
sums of products of update-factor RMS norms. A larger finite primal
ball with slack therefore contains the coarse finite reference on
high-probability events. Fixed-cap raw Euler local defects are bounded
by L_R M_R h^2/2, with constants independent of width. Stopped Gronwall
removes the auxiliary mesh and identifies finite fixed-cap GF.

The genuine uncut finite system is compared to that same-width cap
reference by the finite version of (11). Width goes to infinity at
fixed cap, then the cap goes to infinity. The strict bounded-ball
margin precludes exit. Raw GD is simultaneous Euler in the original raw
coordinates; its parameter interpolant has direction equal to the
uncut field at its preceding node. The additional cap-reference error
is C_{R,T}*eta_n. With eta_n=n^{-2}, the same stopped estimate converges,
without requiring an uncut Lipschitz constant uniform in width or a
Gaussian theorem for a growing transcript. The initialized finite
readout remains iid N(0,n^{-2}), whose RMS norm is O_P(n^{-1}); it is not
reset to zero. Its limit is the zero population readout by fixed-program
stability. These are full-width-sequence convergence-in-probability
arguments, not subsequence selection.

Every fixed-cap velocity-lemma hypothesis holds with the same elementary
bounds:

\[
|\phi(z)|\le \pi/2+|z|,\quad |\phi'|\le2,
\quad |\phi''|\le e\le1,
\quad |D|\le2|q|,\quad |D_z|\le2eR,\quad |D_q|\le2.
\]

The source-response and probe derivations use upper bounds only. The
appended forward queries are still W_2*U^1 and W_3*U^2, with
U^ell=phi'(Z^ell)*P^ell and P^ell the actual preactivation velocity.
Their source corrections and learned-memory terms stay present.
Unbounded-product velocity instructions must still first be smoothly
truncated as in Sections 4–5 of the supplied velocity proof; direct
application of the bounded-derivative conditioning theorem to those
products would be invalid. The published truncation argument applies
with the derivative bounds above.

The deterministic hidden-velocity comparison remains

\[
\|\mathcal V-\overline{\mathcal V}\|_{\mathrm{sum},2}
\le K\left[d_1+(1+M)d_0+
\sum_{\ell,i}\|(|\bar P_i^\ell|-M)_+\|_2\right],
\tag{12}
\]

where d_0 and d_1 are raw-state and raw-direction discrepancies. K is
independent of cap and truncation M on bounded primal/direction sets.
It follows by the three-layer product rule and truncating only the
reference preactivation-velocity factor in a gate difference. The
factor is a single M because each such product is added at its layer.

The order of limits is essential. First compare population cap
velocities to the uncut population velocity. The latter is continuous
in L2, by the trajectory chain rule with bounded continuous phi', and
has a compact L2 time image. Such an image has uniformly vanishing
positive-part tail norms: the tail map is 1-Lipschitz, so a finite L2
net reduces this to finitely many fixed L2 variables. Apply (12), take
R to infinity at fixed M, then M to infinity. For finite velocities,
take width first at fixed R,M, use the fixed-cap velocity law/tail
convergence, then R to infinity at fixed M, and finally M to infinity.
This proves uniform-time joint same-layer W2 velocity convergence,
fixed-finite-time joint W2 convergence, squared-speed and integrated
squared-speed convergence. It makes no unsupported estimate on the
growth of cap-dependent fourth-moment constants.

The actual raw-interpolant direction is used at GD times, with right
node derivatives and terminal left derivatives. Products of converging
L2 fields give the four raw kernel blocks and the prediction/loss
contractions. The path-space upgrade uses

\[
\|x-I_hx\|_{C([0,T])}^2\le4h\int_0^T|x'(t)|^2dt,
\]

averaged over neurons/populations, together with the just-proved speed
bounds and fixed-grid joint W2 convergence. The tuple has both samples'
preactivations and features in a given layer. No across-layer neuron
pairing or operator-norm convergence of unrelated finite matrices is
asserted.

## 6. The two requested coefficient families

If the final theorem provides one e_delta for every a in [1/2,1], it
immediately includes the convex family

\[
\phi_e(z)=(1-e)z+e\arctan z,\qquad
0<e\le\min(e_\delta,1/2).
\]

For normalized odd activation let G be standard Gaussian,

\[
\mu=E[G\arctan G],\qquad \nu=E[(\arctan G)^2],
\]
\[
a(r)=(1+2\mu r+\nu r^2)^{-1/2},\qquad e(r)=r a(r).
\]

Then E[phi(G)^2]=1 exactly. Since 0<mu<=1 and 0<nu<=pi^2/4,
for 0<r<=1/2 we have
\(1\le1+2\mu r+\nu r^2\le2+\pi^2/16<4\).
Thus 1/2<a(r)<=1 and 0<e(r)<=r. Consequently the theorem applies
whenever 0<r<=min(e_delta,1/2). Initialization then has unit forward
preactivation variance at every layer: the first variance is one, and
the Gaussian forward covariance recursion preserves it. These facts
use no offset and do not alter any raw parameter normalization.

## 7. Interface with the main theorem

No obstruction was found in the controlled source lemma, generic
conditioning/action construction, cap removal, finite GF/raw-GD bridge,
or hidden-velocity/path-law bridge. The transfer is an actual proof
extension with uniform constants, not a direct invocation of a theorem
whose statement requires a>=1 or offset 1.

The main proof and its other two companion lemmas separately establish the odd activation's
sample/label symmetry (also for the nonlinear caps), a uniformly bounded
affine reference interval under |rho|<=1-delta, its uniform Gaussian
nondegeneracy, an endpoint prediction margin by strong comparison,
and initial hidden motion/kernel change. The old same-label positive
offset argument cannot be cited for any of those facts without the new
proof. Once those inputs are supplied, the source/bridge work above has
no remaining positive-offset premise.
