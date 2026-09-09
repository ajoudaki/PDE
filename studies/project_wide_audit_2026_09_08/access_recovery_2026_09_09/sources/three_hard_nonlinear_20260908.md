# Nonperturbative same-array source values for the convex mixture

2026-09-08. This note concerns the original three-input, three-hidden-layer raw model with `phi(z)=a z+e atan(z)`, `a=1-e`, `0<e<=1/2`. It does not change the gain, initialization, metric, algorithm, sample geometry or order of limits. The large-gain source note was read only for its mathematical cancellation; no large gain is imported here.

## 1. A new local lemma without an amplitude or clock smallness assumption

The gain note's same-array identity has a stronger transferable value consequence than its small-box proof states. On any fixed finite controlled interval, **finite actual forward and reverse response rows plus actual primal L2 bounds imply subGaussian source values, with no smallness restriction on e, the interval, or their product**. The proof replaces absorption on the entire interval by causal Volterra Gronwall.

This is a conditional value theorem. The response arrays below must be the arrays of the same actual capped source program. They cannot be taken from another trajectory or replaced by their affine counterparts.

Consider a positive time mesh `0=t_0<...<t_N<=S`, with `h_j=t_(j+1)-t_j`. Three-dimensional sample blocks use the induced maximum norm. Let A be a strict causal block array and B a causal block array satisfying

\[
 \|A_{kj}\|_\infty\le\alpha h_j\quad(j<k),
 \qquad\sup_k\sum_{j\le k}\|B_{kj}\|_\infty\le b.
 \tag{1}
\]

Assume that the same-array source equations are

\[
 Z=\xi+A d,\qquad q=\zeta+B h,\qquad
 h=aZ+e\arctan Z,
 \qquad d=aq+e g(Z)\tau_R(q),
 \tag{2}
\]

where `g(z)=(1+z^2)^(-1)`, the clips obey `|tau_R(q)|<=|q|`, and the primitive source arrays xi,zeta are jointly centered Gaussian (their prescribed inter-group independence can be retained but is not needed in this value proof). Coefficients and covariances are deterministic and frozen. Initial repeated Gaussian roots or zero groups are allowed. Suppose separately that the actual fields satisfy

\[
 \max_{k,i}\|q_{k,i}\|_2\le Q,
 \qquad\max_{k,i}\|Z_{k,i}\|_2\le F.
 \tag{3}
\]

These are primal bounds, not source-tail assumptions. Set

\[
 E=\exp(a^2\alpha b S),\qquad
 k_0=e a\alpha b E,\qquad
 d_0=e(\pi/2)bE,
 \qquad V=Q(1+k_0S)+d_0.
 \tag{4}
\]

Then there is an absolute constant, for example 4, such that for every p>=2,

\[
 \max_{k,i}\|q_{k,i}\|_p
 \le [4V+d_0]\exp(k_0S)\sqrt p.
 \tag{5}
\]

All constants depend on S, alpha, b, Q and e but not on the cap, the number of mesh nodes or a minimum step. Thus uniform versions of (1) and (3) give a uniform psi2 bound. A psi1 consequence follows immediately. The constant can grow very rapidly with S; no uniform-halfline moment conclusion is asserted.

### Proof

Since A is strict and B causal, both AB and BA are strict. Their resolvents exist on every finite mesh. Write

\[
 R=(I-a^2AB)^{-1},\quad L=(I-a^2BA)^{-1},\quad U=RA.
 \tag{6}
\]

Both resolvent complete row norms are bounded by E. For R, solve `X=u+a^2 A B X`, take the running maximum, and use

\[
 |X_k|\le |u_k|+a^2\alpha b\sum_{j<k}h_j\max_{r\le j}|X_r|.
\]

The discrete Gronwall product is at most `prod_j(1+a^2 alpha b h_j)<=E`. The same bound for L follows because BA itself has strict density at most `b alpha h_j`. In particular

\[
 \|U_{kj}\|_\infty\le\alpha E h_j,
 \qquad\|(BU)_{kj}\|_\infty\le b\alpha E h_j,
 \qquad\|LB\|_{\rm row}\le bE.
 \tag{7}
\]

For the bound on U, use U=RA and its complete row bound; for BU sum the causal B row. The identity `LB=BR` gives the final bound. It is not necessary that AB itself have strict density `alpha b h_j`; in general it need not, since B may have concentrated old columns.

Put `r=atan Z` and `v=g(Z)tau_R(q)`. Thus `|r|<=pi/2` and `|v|<=|q|`. Exact elimination of (2) at the same arrays gives

\[
 Z_G=R\xi+aU\zeta,
 \qquad q_G=L\zeta+aBR\xi,
\]

\[
 Z-Z_G=eUv+eaUB r,
 \qquad q-q_G=eaBUv+eLB r.
 \tag{8}
\]

The displayed Gaussian parts are centered jointly Gaussian. They are not obtained by setting e=0 in the coefficients or covariances. From (3), (7) and (8), each marginal obeys

\[
 \|(q_G)_{k,i}\|_2\le Q+k_0SQ+d_0=V.
 \tag{9}
\]

No independence between `q_G` and its remainder is needed in (9). The elementary Gaussian moment bound therefore gives `||(q_G)_(k,i)||_p<=4 V sqrt(p)`. Taking Lp norms in (8), using the strict density in (7), and setting `m_k=max_i||q_(k,i)||_p`, one obtains

\[
 m_k\le4V\sqrt p+d_0+k_0\sum_{j<k}h_jm_j.
\]

Discrete Gronwall proves (5). This step, rather than trying to absorb `ea||BU||_row` on the entire interval, is what removes all amplitude/clock smallness.

There is also a forward value estimate. By (8),

\[
 \|(Z_G)_{k,i}\|_2
 \le F+e\alpha ESQ+ea(\pi/2)\alpha bES=:V_Z.
\]

If M denotes the prefactor in (5), then

\[
 \max_{k,i}\|Z_{k,i}\|_p
 \le[4V_Z+e\alpha ES M+ea(\pi/2)\alpha bES]\sqrt p.
 \tag{10}
\]

Since `|phi(z)|<=|z|`, this also controls forward feature values. This completes the finite-mesh lemma.

## 2. Why this is relevant to true energy and compact-time continuation

On a hypothetical true strong GF, the exact energy identity bounds raw displacement by `sqrt(3T/2)` on [0,T]. That gives actual primal L2 bounds F_T,Q_T. If the actual capped or energy-regularized construction supplied response constants alpha_T,b_T independent of its regularization and time mesh, (5) would give source tails for every e in the allowed range, with constants permitted to depend on T. The old condition of the form `e exp(c/e^2)<<1` would not appear in this value step.

The Osgood route needs only psi1 source values. The psi2 estimate above is stronger once its premises are available. In particular it does not repeatedly double a moment exponent: its p dependence is exactly sqrt(p) on each fixed interval, regardless of that interval's length. It also uses the already available *actual* primal L2 scale to bound the Gaussian part rather than adding independent Gaussian variances of large terms that may cancel.

However the energy identity cannot yet be assigned to the usual incoming-field-capped paths. The premise (3) must be proved for the chosen approximation, or the root's energy-preserving construction must supply it. This lemma alone does not close that separate construction step.

## 3. The remaining response-continuation problem is now precise

The value argument has no smallness obstruction once (1) holds. The current source coefficient proof still attempts to prove (1) through expected named-source Jacobians. Locally their exact equations have the form

\[
 J=I_\xi+A\{N J+V_g(I_\zeta+B GJ)\},
\]

where `G=diag phi'(Z)`, `V_g=diag partial_q d`, and
`N=diag[e g'(Z)tau_R(q)]`. The first two diagonal multipliers have norm at most one; `|N|<=e|q|` with an inessential absolute factor. Pointwise Volterra differentiation produces factors of the form

\[
 \exp\left(C\alpha bS+C e\alpha\sum_jh_j\max_i|q_{j,i}|\right).
 \tag{11}
\]

For *fixed* finite alpha,b, (5) makes every required finite moment of (11) finite uniformly in cap and mesh. Thus source differentiation is not blocked by an infinite moment at a fixed response radius. But the resulting coefficient-production bounds depend superlinearly on alpha,b. Plugging their own output radii into the next layer's production estimate does not presently give an a priori bound up to arbitrary T. The short-clock large-gain proof closes these radii using smallness; that step is the part which does not transfer.

The missing assertion can therefore be stated without any affine reference:

> On each fixed physical interval [0,T], under the relevant cap/mesh-independent primal bounds, the **actual** expected named-source response arrays of the three-layer convex-mixture dynamics have finite strict forward densities and complete backward row bounds, or a weaker integrated causal bound sufficient to obtain the resolvent and BU bounds (7), uniformly in the regularization and mesh.

Proving this would combine with (5), psi1/Osgood cap stability, the strong construction, and the original finite-program bridges. It is an a priori response-continuation assertion, not another small-theta condition and not an initialization Gram estimate.

The bounds in (1) are a sufficient interface, not a claim that absolute rows are necessary for the desired theorem. A proof using directly controlled query-span transport or a different source representation could bypass them. The earlier inverse-free Gaussian projection estimate controls the combined response only in L2; it does not by itself imply (1), a higher-moment replacement, or the uniform integrability needed to identify the limit.

## 4. Current bounded-search conclusion

The gain family's same-array cancellation gives a genuine nonperturbative improvement for the original convex mixture: conditional on actual finite response rows and primal L2 bounds, source values have cap/mesh-uniform Gaussian tails on an arbitrary finite interval, with no theta smallness. Thus the previous long-clock amplitude obstruction is removed from the value analysis itself.

I have not yet proved response-row continuation from raw energy, nor found a reachable-state invariant which replaces it. Consequently this note is not a complete three-input population theorem and supplies no sufficient theta_delta. Its new theorem is (5)-(10), and its exact remaining proof obligation is the uniform actual-array continuation statement in Section 3.

## 5. One weak input mode, and a sharper initial fast/slow coupling

The root proposed a useful geometric split. If the eigenvalues of Gamma are ordered increasingly, then

\[
 \lambda_2(\Gamma)\ge\delta.
 \tag{12}
\]

Indeed every two-by-two principal Gram has eigenvalues `1+-|rho_ij|`; its smaller eigenvalue is at least delta. Principal-submatrix interlacing places that smaller eigenvalue at or below the second eigenvalue of Gamma. Thus at most one input mode is weak. This includes rank-two Grams, whose two positive eigenvalues are bounded below by delta.

There is a corresponding exact initialization improvement for the full kernel. Let `Q_l` denote the initialized feature Gram at layer l, with `Q_0=Gamma`, and let `q_(l-1)>0` be its predecessor's common diagonal. For the initialized Gaussian preactivation Z at that layer set

\[
 \beta_l=\frac{E[Z_i\arctan Z_i]}{q_{l-1}}
       =E\frac1{1+q_{l-1}G^2}\in(0,1],
 \qquad c_l=a+e\beta_l\in[a,1].
\]

The regression residuals `r_i=atan Z_i-beta_l Z_i` are orthogonal to every Z_j by Gaussian conditional expectation, including singular covariance. Hence, exactly,

\[
 Q_l=c_l^2 Q_{l-1}+e^2 R_l,
 \qquad R_l=\operatorname{Gram}(r_1,r_2,r_3)\succeq0.
 \tag{13}
\]

All initialized feature variances are at most one because phi is 1-Lipschitz and vanishes at zero. Orthogonal projection decreases L2 norm, and `|atan z|<=|z|`, so `tr R_l<=3q_(l-1)<=3`. In particular `||R_l||_op<=3`. Iterating (13) gives

\[
 Q_3(0)=\kappa_e\Gamma+e^2 R_e,
 \quad \kappa_e=c_1^2c_2^2c_3^2\in[a^6,1],
 \quad R_e=c_3^2c_2^2R_1+c_3^2R_2+R_3,
 \quad 0\preceq R_e\preceq9I_3.
 \tag{14}
\]

At the bottom, subtracting the first-chaos projection does not change the third Hermite coefficient. Therefore `R_1>=b_3^2 Gamma^(circ 3)`, and the established cubic-lifting inequality gives

\[
 R_e\succeq\nu_\delta I_3,
 \qquad\nu_\delta=a^4 b_3^2[\delta(2-\delta)]^2/3.
 \tag{15}
\]

At population initialization all hidden raw gradient blocks vanish because C=0, so the complete raw tangent kernel equals Q_3(0). Choose an orthonormal Gamma eigenbasis and split it into the slow minimum-eigenvalue direction and the two fast directions. Write

\[
 K(0)=\begin{pmatrix}K_{ff}&K_{fs}\\K_{sf}&K_{ss}\end{pmatrix}.
\]

Equations (12)-(15) yield

\[
 K_{ff}\succeq\kappa_e\delta I_2\succeq a^6\delta I_2,
 \qquad\|K_{fs}\|\le9e^2,
 \qquad\|K_{ff}^{-1}K_{fs}\|\le\frac{9e^2}{a^6\delta}
 \le\frac{576e^2}{\delta}.
 \tag{16}
\]

The initial fast/slow coupling is consequently **quadratic in e**, not merely linear. The slow Schur complement satisfies

\[
 \sigma_0=K_{ss}-K_{sf}K_{ff}^{-1}K_{fs}
 \ge\kappa_e\lambda_1(\Gamma)+e^2\nu_\delta>0.
 \tag{17}
\]

To verify (17), minimize the quadratic form of K over the fast coordinates while fixing slow coordinate one. By (14)-(15) that form is at least
`kappa_e lambda_1(Gamma)+e^2 nu_delta`, independently of the fast choice. The minimum is precisely the displayed Schur complement. This argument does not estimate a Schur complement by subtracting two coarse bounds which could swamp its small positive margin.

Equations (16)-(17) are initialization statements, not trained invariant statements. They identify a potentially useful small parameter `e^2/delta` for an initial fast/slow decomposition. They do not by themselves justify a global choice `e<=c sqrt(delta)` or any other sufficient threshold.

## 6. The exact fast/slow continuation interface

On an already existing true flow, in the same fixed sample basis write

\[
 \dot r_f=-K_{ff}r_f-K_{fs}r_s,
 \qquad\dot r_s=-K_{sf}r_f-K_{ss}r_s.
 \tag{18}
\]

Whenever K_ff is invertible, put `L=K_ff^(-1)K_fs`, `z=r_f+Lr_s` and `sigma=K_ss-K_sf L`. Direct algebra gives

\[
 \dot r_s=-\sigma r_s-K_{sf}z,
\]

and, if the kernel has the indicated time derivative,

\[
 \dot z=-(K_{ff}+LK_{sf})z+(\dot L-L\sigma)r_s.
 \tag{19}
\]

Thus a normal-hyperbolic or tracking proof needs control of the trained fast block, trained Schur complement, coupling L, and its variation. The initial separation (16) is not enough by itself. These estimates could conceivably replace absolute source rows, but currently require a reachable-state argument which has not been supplied.

There is a further issue in applying the previous scalar readout-linear ascent lemma after fitting the fast modes. Let H_f(v) be the two fast hidden feature columns and h_s(v) the slow column. Suppose their fast readout Gram Q_ff is invertible. The constraint `H_f(v)^*C=y_f` gives

\[
 C=H_f Q_{ff}^{-1}y_f+C_\perp,
 \qquad C_\perp\perp\operatorname{ran}H_f,
\]

and therefore

\[
 f_s=Q_{sf}Q_{ff}^{-1}y_f
       +\langle C_\perp,(I-P_{H_f})h_s\rangle.
 \tag{20}
\]

The first term generally depends on the hidden parameters, while the orthogonal readout space in the second term also moves with those parameters. Thus the constrained scalar objective is not automatically the earlier fixed-Hilbert-space, zero-initial-readout expression `<C,H(v)>`. Ignoring this term or its moving-space derivative would be an unjustified reduction. The symmetric equal-label equilateral case has y_f=0 and is exceptional. A new constrained scalar lemma or direct Schur-complement analysis is needed for generic labels/geometries.

This assessment leaves the fast/slow route open rather than rejecting it. It provides the sharper initial coupling (16), the positive initial Schur bound (17), and the exact trained quantities that a complete proof would have to propagate.
