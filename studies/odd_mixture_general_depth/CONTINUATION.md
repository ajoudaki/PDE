
# Part II. A conditional continuation criterion that retains curvature decay

This part proves a functional-analytic implication. Its hypotheses are additional requirements, not conclusions of Part I. It proves neither the required bounds for the trained references nor the finite-width trained joint limit.

## II.1. State space and the extra hypothesis

Let \(H_\ell=L^2(\Omega_\ell,\mu_\ell)\) be real probability-space Hilbert spaces for \(1\le\ell\le L\). Fix bounded linear actions \(A_{\ell,0}:H_{\ell-1}\to H_\ell\) for \(2\le\ell\le L\), with their actual Hilbert adjoints. Take the affine parameter space with coordinates
\[
v\in L^2(\Omega_1;\mathbb R^d),\quad
A_\ell\in A_{\ell,0}+\mathcal S_2(H_{\ell-1},H_\ell),\quad C\in H_L.
\]
Here \(\mathcal S_2\) is the space of Hilbert--Schmidt operators. The squared raw increment norm is \(\|\Delta v\|_2^2+\sum_{\ell=2}^L\|\Delta A_\ell\|_{\rm HS}^2+\|\Delta C\|_2^2\); its equivalent sum norm is used for comparison. This is the earlier first-block normalization after \(v=\sqrt d\,w\). The conditional lemma holds on every such collection of spaces and actions. It does not assert that arbitrarily chosen actions are the Gaussian initialized limit of the finite network.

Define \(z_i^1=v\cdot u_i\), \(h_i^\ell=\phi_\theta(z_i^\ell)\), \(z_i^\ell=A_\ell h_i^{\ell-1}\) for \(\ell\ge2\), and \(f_i=\langle C,h_i^L\rangle\), \(r_i=f_i-y_i\). Inner products are always in the specified layer. For a gate \(D\), compute
\[
q_i^L=C,\quad b_i^\ell=D(z_i^\ell,q_i^\ell),\quad
q_i^\ell=A_{\ell+1}^*b_i^{\ell+1}\ (\ell<L),
\]
and use the raw vector field
\[
F_v=-\sum_i r_i b_i^1u_i,\quad
F_{A_\ell}=-\sum_i r_i b_i^\ell\otimes h_i^{\ell-1},\quad
F_C=-\sum_i r_i h_i^L.
\tag{II.1}
\]
For \(a=1-\theta\), the true gate is \(D_\infty(z,q)=(a+\theta/(1+z^2))q\). Rank-one operators are \((b\otimes h)w=b\langle h,w\rangle\); their HS norm is \(\|b\|_2\|h\|_2\).

Choose a smooth odd function \(\tau\) such that \(0\le\tau'\le1\), \(\tau(t)=t\) on \([-1,1]\), and \(\tau'=0\) for \(|t|\ge2\). Such a function is obtained by integrating a smooth even cutoff between zero and one. Put \(s(z)=\sqrt{1+z^2}\) and define the auxiliary gates
\[
D_R(z,q)=a q+\theta\frac R{s(z)}
\tau\left(\frac q{R s(z)}\right),\qquad R\ge1.
\tag{II.2}
\]
These alter only the auxiliary backward fields. The forward activation and every update in (II.1) are unchanged. They have the correct true-gate limit.

**Conditional continuation theorem.** Fix \(L<\infty\), \(0<\theta\le1\), and \(T<\infty\). Suppose the \(D_R\) reference flows exist on \([0,T]\) from the same state and satisfy, with one finite \(B\ge1\),
\[
\sup_{R,t\le T}\max\{\|v_R(t)\|_2,\|C_R(t)\|_2,
\|A_{2,R}(t)\|_{\rm op},\ldots,\|A_{L,R}(t)\|_{\rm op}\}\le B.
\tag{II.3}
\]
Assume also, for some finite \(A\ge1,c>0\),
\[
\sup_{R,t\le T,\ell,i}
\left\|q_{i,R}^\ell(t)
\mathbf1_{\{|q_{i,R}^\ell(t)|/\sqrt{1+z_{i,R}^\ell(t)^2}>u\}}\right\|_2
\le A e^{-cu}\qquad(u\ge1).
\tag{II.4}
\]
Then these references converge uniformly on \([0,T]\), in raw state and raw direction, to a strong \(C^1\) solution of (II.1) with the true gate. It is unique against every strong true-gate solution with the same initialization and bounded primal quantities on compact intervals. If (II.3)--(II.4) hold consistently for every finite horizon, the resulting solution is global and has unique continuation from every reached state in that class. There is no smallness requirement coupling \(\theta\), \(L\), or \(T\) in this implication. Its unproved assumptions may of course depend on those parameters.

This is a population continuation theorem conditional on reference bounds. It contains no assertion about finite-width convergence of trained paths or velocities; those require their own approximation and observation arguments.

## II.2. Exact gate estimates

Write \(N_R(z,q)=R s(z)^{-1}\tau(q/(R s(z)))\). It is even in \(z\), odd in \(q\), and \(|N_R(z,q)|\le |q|/(1+z^2)\). With \(t=q/(Rs(z))\), differentiation gives
\[
\partial_q D_R=a+\theta s(z)^{-2}\tau'(t)\in[a,1],
\quad
\partial_zD_R=-\theta\frac{Rz}{s(z)^3}[\tau(t)+t\tau'(t)].
\tag{II.5}
\]
Since \(|\tau|\le2\) and \(|t\tau'|\le2\), the latter is at most \(4\theta R\) in absolute value. Hence each fixed-cap gate is globally Lipschitz. Alternatively \(|\tau(t)|\le|t|\) yields
\[
|\partial_zN_R(z,q)|\le\frac{2|qz|}{(1+z^2)^2}=|q|\,|g'(z)|,
\qquad g(z)=(1+z^2)^{-1}.
\]
Integrating between \(|z|\) and \(|\bar z|\), where \(g\) is monotone, proves
\[
|N_R(z,q)-N_R(\bar z,q)|\le|q|\,|g(z)-g(\bar z)|.
\]
The exact secant quotient is
\[
\frac{|g(z)-g(\bar z)|}{|z-\bar z|}
=\frac{|z+\bar z|}{(1+z^2)(1+\bar z^2)}
\le\frac{|\bar z|+\sqrt{1+\bar z^2}}{2(1+\bar z^2)}
\le\frac1{s(\bar z)}.
\tag{II.6}
\]
For the middle inequality, the largest value of \(|z+u|/(1+z^2)\) is \((|u|+\sqrt{1+u^2})/2\): it is the largest absolute Rayleigh quotient of the symmetric matrix with entries \(u,1/2,1/2,0\) at vectors \((1,z)\), and is obtained by solving its quadratic characteristic polynomial. The same bound follows by differentiating the rational function. This secant estimate is global, including when \(z\) moves far from \(\bar z\).

For \(R',R\ge M\ge1\), including an infinite cap, first change \(q\) to \(\bar q\) at cost \(|q-\bar q|\). On \(|\bar q|/s(\bar z)\le M\), both caps at the reference point equal the true gate, and (II.6) bounds the remaining difference by \(\theta M|z-\bar z|\). On the complementary event the two nonlinear terms have sum of absolute values at most \(2|\bar q|\). Thus
\[
|D_{R'}(z,q)-D_R(\bar z,\bar q)|
\le |q-\bar q|+\theta M|z-\bar z|
+2\theta|\bar q|\mathbf1_{\{|\bar q|/s(\bar z)>M\}}.
\tag{II.7}
\]
Only the reference point needs the tail estimate. This proof allows clipping at the moved point even when the reference point is not clipped.

## II.3. Propagation through arbitrary fixed depth

For two states with primal sizes bounded by \(B\), let \(d\) be their raw sum distance. Forward induction gives
\[
\|z_i^\ell\|_2,\|h_i^\ell\|_2\le B^\ell,
\quad \|q_i^\ell\|_2,\|b_i^\ell\|_2\le B^{L-\ell+1},
\quad |r_i|\le2B^{L+1},
\]
\[
\|\Delta z_i^\ell\|_2,\|\Delta h_i^\ell\|_2\le B^{\ell-1}d,
\qquad |\Delta r_i|\le2B^L d.
\tag{II.8}
\]
The forward difference bound follows by telescoping one action at a time and using \(\|\Delta A\|_{\rm op}\le\|\Delta A\|_{\rm HS}\). Backward sizes use \(|D_R(z,q)|\le|q|\).

Let \(T_M\) be the largest reference tail norm appearing in (II.7). The incoming and gate differences obey the explicit downward recursions
\[
\|\Delta q_i^L\|_2\le d,
\quad\|\Delta q_i^\ell\|_2
\le B\|\Delta b_i^{\ell+1}\|_2+B^{L-\ell}\|\Delta A_{\ell+1}\|_{\rm HS},
\]
\[
\|\Delta b_i^\ell\|_2
\le\|\Delta q_i^\ell\|_2+\theta M B^{\ell-1}d+2\theta T_M.
\tag{II.9}
\]
In particular, for every \(\ell\), downward substitution gives the sufficient bound
\[
\|\Delta b_i^\ell\|_2
\le (L+1)B^L d+\theta M L B^{2L}d+2\theta L B^L T_M.
\tag{II.10}
\]
Each factor \(M\) multiplies a forward discrepancy already bounded independently of \(M\); it never multiplies a preceding backward discrepancy. There is therefore one power of \(M\), irrespective of depth.

The rank-one identity
\[
\|b\otimes h-\bar b\otimes\bar h\|_{\rm HS}
\le\|b-\bar b\|_2\|h\|_2+\|\bar b\|_2\|h-\bar h\|_2
\]
and \(rU-\bar r\bar U=(r-\bar r)\bar U+r(U-\bar U)\), applied to each update in (II.1), now give
\[
\|F_{R'}(\Theta)-F_R(\bar\Theta)\|_{{\rm raw,sum}}
\le K\big[(1+\theta M)d+\theta T_M\big],
\quad K=100(L+1)^2 B^{4L+4}.
\tag{II.11}
\]
To check the displayed common constant, each matrix update has three residual terms and two rank-one factors; insert (II.8)--(II.10), bound \(B^{\ell-1}\le B^L\), and sum over at most \(L+1\) blocks. The largest power obtained is \(B^{4L+1}\); the coefficient is below \(100(L+1)^2\). The first and readout blocks have fewer factors. This proves (II.11) with slack. Under (II.4), \(T_M\le Ae^{-cM}\).

## II.4. A variable threshold proves convergence and uniqueness

Take two cap paths and let \(R\) be their smaller cap. Let \(d(t)\) be their raw sum distance and set \(\varepsilon_R=Ae^{-cR}\), \(u(t)=d(t)+\varepsilon_R\). The integral equation and (II.11) imply the upper right derivative inequality
\[
D^+u\le K[(1+\theta M)u+\theta A e^{-cM}]
\quad(1\le M\le R).
\]
While \(u\le Ae^{-c}\), choose \(M=c^{-1}\log(A/u)\). It is admissible because \(u\ge\varepsilon_R\), and gives, for a finite \(K_1\) depending only on \(K,c,\theta\),
\[
D^+u\le K_1u\log(eA/u).
\]
The initial distance is zero. Substituting \(v=\log(eA/u)\), or integrating the scalar differential inequality, yields
\[
\sup_{t\le T}d(t)
\le eA\exp[-(1+cR)e^{-K_1T}].
\tag{II.12}
\]
For sufficiently large \(R\) this remains strictly below the stopping threshold throughout \([0,T]\), justifying the estimate on the full interval. It tends to zero for every fixed horizon.

Use \(M=R/2\) in (II.11) for \(R\ge2\). The direction discrepancy is bounded by a linear polynomial in \(R\) times (II.12), plus a constant times \(e^{-cR/2}\); both vanish uniformly in time. Completeness gives uniform limits of the raw states and directions. Their integral identities identify a strong \(C^1\) limiting path. The true field is defined and continuous on primal balls: forward maps are locally Lipschitz; for the gate, decompose a difference into the incoming \(L^2\) discrepancy and a bounded multiplier difference times a fixed \(L^2\) incoming field. The latter tends to zero by convergence in measure and dominated convergence along subsequences. Bounded actions and rank-one continuity complete this finite induction. Applying (II.11) to the limiting state and a reference with the infinite cap on the first state identifies the direction with the true field.

For uniqueness compare any bounded-primal strong true-gate competitor with the same cap references. Enlarge \(B\) to cover the competitor; the tail bound remains required only for the reference. The same estimate (II.12) forces it to equal the limiting path. Starting from a reached state at time \(t_0\), the initial discrepancy from the cap reference is already at most \(C e^{-bR}\) by (II.12), for some \(b>0\). Replacing the initial \(u(0)\) by this bound plus \(\varepsilon_R\) in the same scalar integration still gives convergence to zero on every subsequent compact interval. This proves continuation uniqueness. Solutions constructed on different horizons agree on overlaps; consistent hypotheses therefore yield the stated global path. \(\square\)

## II.5. Why the extra hypothesis is not supplied by a raw norm bound

Full exponential tails for the incoming field imply (II.4), since \(s(Z)\ge1\). The converse is false. An \(L^2\) pair with \(Z=Q\) has \(|Q|/s(Z)<1\), so its tails in (II.4) vanish for \(u\ge1\), even when \(Q\) has only polynomial ordinary tails.

On the other hand, a raw \(L^2\) bound does not imply (II.4). For an explicit state-space example at \(L\ge2\), keep the earlier layers fixed and let \(h\ne0\) be a selected layer-\(L-1\) feature. On an atomless top probability space supporting \(U\) uniform on \((0,1)\), set
\[
A_L=A_{L,0}+(\mathbf1-A_{L,0}h)\otimes h/\|h\|_2^2,
\qquad C=U^{-1/3}.
\]
This is a permitted HS increment, \(A_Lh=\mathbf1\), and \(\|C\|_2^2=3\). All primal quantities are finite. For the selected top pair \(Z=1,Q=C\),
\[
\left\|Q\mathbf1_{\{|Q|/\sqrt{1+Z^2}>u\}}\right\|_2^2
=\int_0^{(\sqrt2u)^{-3}}v^{-2/3}dv
=\frac3{\sqrt2u}\quad(u\ge1).
\]
No exponential bound (II.4) holds. This is an example in the affine state space, not a state proved reachable by the prescribed training.

The same issue appears in a differentiated true gate:
\[
\partial_\eta b
=\phi_\theta'(Z)\partial_\eta Q
+\theta g'(Z)Q\partial_\eta Z.
\tag{II.13}
\]
Even if \(Q,J=\partial_\eta Z\) both have bounded second moment, the term \(g'(Z)QJ\) need not be in \(L^2\). For \(Z=1\), \(Q=J=U^{-1/3}\), both factors are square integrable, whereas their product is not. Curvature decay at large \(|Z|\) does not address this example because \(Z\) stays equal to one. Canonical reached laws may have additional structure excluding it, but that structure must be proved.

# What remains unresolved

The requested theorem would require a strictly positive \(\theta_*(\delta,L)\) for which the exact raw trained systems have the global canonical population flow and all joint finite GF/GD, kernel, path and velocity limits, with the required nonaffinity and motion properties. A depth-uniform version would use one positive \(\theta_*(\delta)\) for every separately fixed \(L\), allowing depth-dependent quantitative constants.

No such sufficient threshold is established in this report. The new exact results locate the distinction:

- Initialization is positive for every \(\theta>0\) at every finite depth, and its worst-case gap has the sharp scale in (A).
- Uniform positive absolute kernel and scalar nonaffinity constants across depth are impossible, already at initialization. This does not rule out a depth-uniform admissible mixture for qualitative fixed-depth training statements.
- The affine comparison cannot control all separated triples because the equilateral equal-label target is outside its prediction space.
- The conditional theorem removes a possible depth-dependent power of the cap and retains preactivation curvature decay, but (II.3)--(II.4) for the canonical references remain to be proved. It also does not supply the separate finite-width trained approximation and velocity-observation arguments or an all-time trained-law nonaffinity bound.

The unresolved issue is a property of the trained joint laws, not another optimization of the initialization constants. No claim here asserts that the positive-mixture global theorem is false.
