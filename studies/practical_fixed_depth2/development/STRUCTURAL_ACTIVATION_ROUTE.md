# Structural activation route: an exact special-case transformation and its obstruction

2026-09-08. The principal target remains 
\(\phi(z)=\tfrac34(1+z)+\tfrac14\tanh z\) with every input Gram allowed by CONTRACT.md. It is **not resolved here**.

There is a new positive mechanism for the distinct fixed bounded activation

\[
\phi_B(z)=1+\tanh z,
\tag{1}
\]

when the three input vectors are orthonormal after normalization, \(\Gamma=I_3\). A change of first-layer coordinates removes the unbounded bottom incoming-field multiplier from the derivative of the evolution equation. Bounded output then controls the readout pointwise. This proves a global strong population flow in that special case. A Lie-bracket calculation shows why the same change cannot simultaneously flatten the gate fields for general nonorthogonal inputs. Thus (1) is neither silently substituted for the principal activation nor claimed to solve the full input contract.

## 1. Exact transformed equations for the bounded alternative

Let \(H_1,H_2\) be the canonical Gaussian-program layer spaces, with the genuine bounded initialized action \(A_0:H_1\to H_2\). No replacement action or adjoint is used. Suppose \(u_1,u_2,u_3\) are orthonormal. Decompose

\[
w=w_\perp+\sum_{i=1}^3z_i u_i,
\qquad w_\perp\perp\operatorname{span}\{u_i\}.
\]

The perpendicular component is constant under the original raw flow. For (1), put

\[
\psi(z)=\int_0^z\frac{ds}{\phi_B'(s)}
=\frac z2+\frac{\sinh(2z)}4,
\qquad p_i=\psi(z_i).
\tag{2}
\]

The function \(\psi\) is a smooth increasing bijection of \(\mathbb R\) onto itself. Write \(Z=\psi^{-1}\) and \(H=\phi_B\circ Z\). Direct differentiation gives

\[
0<Z'(p)=\operatorname{sech}^2(Z(p))\le1,
\qquad
0<H'(p)=\operatorname{sech}^4(Z(p))\le1,
\qquad 0<H(p)<2.
\tag{3}
\]

Use \(A=A_0+U\), and define the actual fields by

\[
h_i=H(p_i),\quad v_i=Ah_i,\quad k_i=\phi_B(v_i),
\quad b_i=C\phi_B'(v_i),\quad q_i=A^*b_i,
\quad f_i=\langle C,k_i\rangle,\quad c_i=y_i-f_i.
\]

The original equations become exactly

\[
\dot p_i=c_iq_i,
\qquad
\dot U=\sum_i c_i b_i\otimes h_i,
\qquad
\dot C=\sum_i c_i k_i.
\tag{4}
\]

Indeed orthogonality gives \(\dot z_i=c_i\phi_B'(z_i)q_i\); multiplying by \(\psi'(z_i)=1/\phi_B'(z_i)\) proves the first equation. The operator and readout updates have not changed. In particular (4) is not gradient flow for a newly chosen metric: reconstructing \(z_i=Z(p_i)\) returns the original raw gradient flow.

The transformed state space is

\[
L^2(\Omega_1;\mathbb R^3)\times\mathrm{HS}(H_1,H_2)\times H_2.
\]

At Gaussian initialization, \(p_i(0)=\psi(G_i)\) lies in \(L^2\). For example \(|\psi(z)|\le |z|/2+e^{2|z|}/4\), and \(E e^{a|G|}<\infty\) for every finite \(a\), by completing the square in the Gaussian density. The variables \(p_i(0)\) are not being called subGaussian.

## 2. Special-case global population theorem

**Theorem.** For activation (1), orthogonal input Gram \(\Gamma=I_3\), the canonical initialized action and adjoint, standard Gaussian first-layer initialization, \(U(0)=0\), and \(C(0)=0\), the original raw population equations have a global autonomous strong solution. It is unique among bounded-primal strong competitors from that initialization on compact intervals. The solution restarts uniquely from every reached state.

**Proof.** Fix a finite horizon \(T\), and initially replace \(C\) in \(b_i\) by a smooth bounded truncation \(\tau_M(C)\), equal to \(C\) on \([-M,M]\). Leave the definitions of \(f,c,k\), and the readout equation unchanged. This is an auxiliary construction only.

For each fixed \(M\), the transformed vector field is locally Lipschitz on the displayed Hilbert space, with constants depending only on its state radius, \(M\), \(\|A_0\|\), and the three labels. Here are the needed estimates. The maps \(Z,H,\phi_B\) are Lipschitz by (3) and \(|\phi_B'|\le1\). The map \((v,C)\mapsto\phi_B'(v)\tau_M(C)\) is jointly Lipschitz because \(|\phi_B''|\le2\), \(\tau_M\) is Lipschitz, and \(\tau_M\) is bounded. Multiplication by bounded operators and their genuine adjoints preserves these bounds. The rank-one estimate

\[
\|b\otimes h-\tilde b\otimes\tilde h\|_{\rm HS}
\le\|b-\tilde b\|_2\|h\|_2
+\|\tilde b\|_2\|h-\tilde h\|_2
\]

controls the operator velocity. Finally, \(f_i=\langle C,k_i\rangle\) is Lipschitz on state balls by Cauchy--Schwarz. These facts give local existence and uniqueness by the integral-map contraction: on a ball with field bound \(B\) and Lipschitz constant \(L\), a time interval satisfying \(tB\) smaller than the ball radius and \(tL<1\) makes the integral map a contraction on continuous paths in the ball.

As long as the auxiliary cap is inactive, (4) reconstructs the true raw field. The bounded-derivative chain rule along its strong curves gives

\[
\frac d{dt}E(t)
=-\|\dot w\|_2^2-\|\dot U\|_{\rm HS}^2-\|\dot C\|_2^2.
\tag{5}
\]

For completeness, \(\dot h_i=\phi_B'(z_i)u_i^T\dot w\), \(\dot v_i=\dot U h_i+A\dot h_i\), and \(\dot k_i=\phi_B'(v_i)\dot v_i\). Differentiating \(f_i=\langle C,k_i\rangle\), moving \(A\) to its genuine adjoint, multiplying by \(-c_i\), and summing gives exactly the three squared raw velocity norms in (5). The curve chain rules are valid in \(L^2\) because the derivatives of the coordinate maps are bounded; the products with an incoming \(L^2\) field use bounded multiplier continuity.

Put \(E_0=E(0)\), \(L_0=\sqrt{6E_0}\), and \(R_T=\sqrt{TE_0}\). Equation (5) gives

\[
\|c(t)\|_1\le L_0,\quad
\|U(t)\|_{\rm HS},\|C(t)\|_2\le R_T,
\quad\|A(t)\|\le\|A_0\|+R_T.
\tag{6}
\]

The bounded activation gives the additional pointwise estimate

\[
|C(t,\omega_2)|
\le\int_0^t2\|c(s)\|_1ds
\le2L_0t.
\tag{7}
\]

Choose \(M=2L_0T+1\). A first activation of the auxiliary cap before time \(T\) contradicts (7). More formally, the integral readout equation makes \(C\) locally Lipschitz in \(L^\infty\), since \(|k_i|\le2\) and \(c_i\) is locally bounded. Thus the first-exit argument is legitimate even though the construction takes place in an \(L^2\) space.

The transformed first-layer norm cannot diverge before \(T\). From (4), (6), and \(\|q_i\|_2\le\|A\|\|C\|_2\),

\[
\|\dot p(t)\|_{L^2(\Omega_1;\mathbb R^3)}
\le L_0(\|A_0\|+R_T)R_T.
\tag{8}
\]

Its norm therefore remains within \(TL_0(\|A_0\|+R_T)R_T\) of its initial norm. Together with (6), this bounds the entire transformed state on \([0,T]\). The fixed-cap field has a bounded norm and a Lipschitz constant on this state ball, so the solution has a strong endpoint at any finite putative terminal time and the same integral-map construction restarts there. Hence it exists through \(T\), with the cap inactive. Since \(T\) was arbitrary, uniqueness on overlaps gives a global solution of the uncapped autonomous raw equations.

Now let a bounded-primal strong competitor start from the same initial state. Its actual raw chain rule gives (5), and its readout equation gives (7). Almost every coordinate path \(z_i(t,\omega_1)\) is absolutely continuous, because the strong velocity is square-integrable on compact time intervals. Applying the scalar chain rule pointwise to \(\psi(z_i)\) gives

\[
\psi(z_i(t))=\psi(z_i(0))+\int_0^t c_i(s)q_i(s)ds.
\tag{9}
\]

The right-hand side is a strong \(L^2\) curve by bounded primal fields. Thus the competitor belongs to the transformed space even though composition by \(\psi\) is not a globally Lipschitz \(L^2\) map. It solves the same inactive-cap transformed equation and equals the constructed solution by local Lipschitz uniqueness.

At a reached state, \(p\in L^2\) by (8) and \(C\in L^\infty\) by (7). Restart the same proof with that state as initial data. Replace (7) by \(\|C(t)\|_\infty\le\|C(0)\|_\infty+2\sqrt{6E(0)}t\), and replace the norm bounds by their initial norms plus \(\sqrt{tE(0)}\). These are finite on each compact interval and prove reached-state continuation and uniqueness. ∎

No assertion in this theorem changes the initialized Gaussian operator, treats reverse calls as independent, or replaces the raw gradient metric.

## 3. Verified raw-Euler coordinate defect; no unproved width-limit claim

At finite width with \(\Gamma=I_3\), an original simultaneous raw GD step of length \(\eta\) has

\[
z_i^+=z_i+\eta g_i\phi_B'(z_i),\qquad g_i=c_iq_i.
\]

It is not exactly an Euler step in \(p\). Nevertheless the discrepancy has a useful deterministic bound.

**Lemma.** For every real \(z,g\) and \(\eta\ge0\),

\[
\left|\psi(z+\eta g\phi_B'(z))-\psi(z)-\eta g\right|
\le2\eta^2g^2e^{2\eta|g|}.
\tag{10}
\]

**Proof.** Since \((\log\psi')'(z)=2\tanh z\), the ratio \(\psi'(z+s\Delta z)/\psi'(z)\) differs from one by at most \(e^{2|\Delta z|}-1\), where \(\Delta z=\eta g\phi_B'(z)\). Write the difference in (10) as

\[
\eta g\int_0^1\left(\frac{\psi'(z+s\Delta z)}{\psi'(z)}-1\right)ds.
\]

Use \(|\Delta z|\le\eta|g|\) and \(e^x-1\le xe^x\) for \(x\ge0\). ∎

For three vectors of width \(n\), if \(\sum_i\|g_i\|_n^2\le K^2\), then \(\max_i\|g_i\|_\infty\le\sqrt nK\) and \(\|g_i^2\|_n\le\sqrt n\|g_i\|_n^2\). Hence the combined normalized \(L^2\) coordinate defect is at most

\[
2\eta^2\sqrt n\,K^2e^{2\eta\sqrt nK}.
\tag{11}
\]

The learned-operator and readout updates are exact Euler updates for the transformed field. On a common transformed state ball with an inactive readout cap, where this field has a dimension-independent Lipschitz constant \(L\), comparison over a horizon \(T\) accumulates (11) by at most

\[
2T\eta\sqrt n\,K^2e^{LT+2\eta\sqrt nK}.
\tag{12}
\]

This is \(O(n^{-3/2})\) for the requested physical step \(\eta=n^{-2}\), before including the ordinary \(O(\eta)\) Euler error. A deterministic bootstrap can keep the comparison in such a ball when the initial transformed \(L^2\) norm, initialized action norm, and initial readout \(L^\infty\) norm have fixed bounds: choose a ball with slack around the finite GF path, bound \(\|c\|_1\le3+6\|C\|_2\) there for \(\{-1,1\}\) labels, and choose the auxiliary readout cap above \(\|C_0\|_\infty+2T\sup\|c\|_1\). Equation (12) prevents the first norm exit for sufficiently large \(n\).

This verifies an algorithm-comparison estimate in the special case. It does **not** by itself prove the full Gaussian width limit. Such a bridge must still justify the compatible finite-program realization with the root \(\psi(G)\), retain the actual finite random readout, identify the true field path laws in \(W_2\), and establish the velocity and second-moment observables. Finite second moments of \(\psi(G)\) were verified above; that fact is only one of these obligations. No full GF/GD joint-limit theorem is claimed in this note.

### Polynomial-transform bounded alternative

The same special-case population argument also applies to the distinct fixed activation

\[
\phi_A(z)=1+\tfrac12\arctan z,
\quad 1-\pi/4<\phi_A(z)<1+\pi/4,
\quad \psi_A(z)=2z+\tfrac23z^3.
\tag{15}
\]

Indeed \(\psi_A'=1/\phi_A'\), the inverse derivative is at most \(1/2\), and the derivative of \(\phi_A\circ\psi_A^{-1}\) is at most \(1/4\). Replace the activation bound 2 in the proof by \(1+\pi/4\). The transformed initialization is now polynomial in a Gaussian root, hence has finite moments of every order. The nonlinear coefficient \(1/2\) is fixed, not sent to zero. This is another bounded alternative, not an affine perturbation matching the principal activation.

Here the raw-GD defect has an exact cubic formula. With \(\Delta=\eta g/[2(1+z^2)]\),

\[
\psi_A(z+\Delta)-\psi_A(z)-\eta g
=2z\Delta^2+\tfrac23\Delta^3.
\]

Using \(|z|/(1+z^2)^2\le1\) gives

\[
|\text{defect}|\le\tfrac12\eta^2g^2+\tfrac1{12}\eta^3|g|^3.
\]

The normalized vector bound is therefore

\[
\|\text{defect}\|_{2,n}
\le\tfrac12\eta^2\sqrt nK^2+\tfrac1{12}\eta^3 nK^3,
\]

because \(\|g_i^3\|_n\le n\|g_i\|_n^3\). This removes the exponential factor in (11), but does not remove the separate finite-program/path-observable obligations just stated.

## 4. Why the transformation does not solve general input geometry

For any smooth activation with \(\phi'>0\), the first-neuron controlled vector fields are

\[
V_i(w)=\phi'(u_i^Tw)u_i.
\]

The true neuron velocity is \(\sum_i c_iq_iV_i(w)\). Their Lie bracket, using \([V_i,V_j]=DV_jV_i-DV_iV_j\), is

\[
[V_i,V_j](w)=\Gamma_{ij}
\left(\phi'(z_i)\phi''(z_j)u_j
-\phi'(z_j)\phi''(z_i)u_i\right).
\tag{13}
\]

**Lemma.** If \(u_i,u_j\) are independent and nonorthogonal, a smooth change of neuron coordinates cannot transform both \(V_i,V_j\) to constant vector fields for a globally nonaffine smooth activation with \(\phi'>0\).

**Proof.** A smooth coordinate change preserves Lie brackets, and constant vector fields commute. Thus the bracket in (13) would have to vanish everywhere. Since \(\Gamma_{ij}\ne0\), the two vectors are independent, and \(\phi'>0\), vanishing forces \(\phi''(z_i)=\phi''(z_j)=0\) at every \(w\). The map \(w\mapsto(z_i,z_j)\) is onto \(\mathbb R^2\), so \(\phi''\equiv0\), contrary to nonaffinity. The bracket-invariance statement can be checked directly by differentiating the transformed fields: the two Hessian terms of the coordinate change cancel because its Hessian is symmetric. ∎

Directly applying (2) when \(\Gamma\ne I\) instead produces

\[
\dot p_i=\sum_j\Gamma_{ij}c_jq_j
\frac{\phi'(z_j)}{\phi'(z_i)}.
\]

For the bounded activation, the ratio is unbounded. Equation (13) explains why another simultaneous scalar straightening does not eliminate the problem. This is an obstruction to that specific transformation method, not a no-go theorem for the full target.

The principal affine-plus-tanh activation has a different failure even for \(\Gamma=I\): the analogous \(\psi\)-transform removes the bottom gate, but its unbounded forward output no longer gives the pointwise readout estimate (7). The top incoming-field multiplier remains uncontrolled by this argument.

## 5. Compact perturbations, compact gates, and offset tests

**Affine plus a compactly supported smooth perturbation.** Localizing \(\phi''\) in a compact interval does not make \((v,C)\mapsto C\phi'(v)\) Lipschitz on an ambient \(L^2\) ball. To see this, choose two finite values \(v_0,v_1\) with \(\phi'(v_0)\ne\phi'(v_1)\). On a nonatomic probability space take events \(E_m\) of probability \(p_m\downarrow0\), set \(C_m=\rho p_m^{-1/2}1_{E_m}\), and change \(v_0\) to \(v_1\) only on \(E_m\). The input difference is \(|v_1-v_0|\sqrt{p_m}\), while the output difference is the fixed positive number \(\rho|\phi'(v_1)-\phi'(v_0)|\). Both states remain in a fixed \(L^2\) ball. The test is inside the curvature-support region, so decay or compact support outside it is irrelevant. This rules out an ambient Lipschitz shortcut, not a physical reachability estimate.

**Bounded activations and compactly supported derivatives.** Bounded activation values give (7), removing the top incoming-field obstruction. They do not in general bound \(q=A^*b\) pointwise. Compact support of the first-layer gate also does not imply that each \(z_i\) stops when its own gate vanishes: at such a point,

\[
\dot z_i=\sum_{j\ne i}\Gamma_{ij}c_j\phi'(z_j)q_j
\]

can be nonzero. A stronger geometric confinement statement for the joint neuron orbit would need a separate proof. It would still not, by itself, identify all reverse-field tails under the initialized action. No such confinement-to-full-limit implication is claimed here.

**Positive offset and monotonicity do not give a statewise kernel floor.** For either the principal activation or (1), consider the legitimate finite-raw-norm state \(w=0,U=0,C=0\). All three first features are the same constant; all three top features therefore coincide. The first two true kernel blocks vanish because \(b_i=d_i=0\). The readout block has every entry equal to one common squared feature norm, so its rank is at most one. Thus offset and monotonicity alone cannot imply a uniform positive three-sample kernel floor on bounded primal states. This state is not asserted to be reached by the actual initialized flow, so the example does not disprove a trajectory-specific kernel statement. A floor whose proof already assumes source continuation would also not construct the missing population flow.

## 6. Quantitative nonaffinity of the bounded alternative

The alternative is not an existence-only tiny perturbation. For \(G\sim N(0,1)\),

\[
\inf_{\alpha,\beta\in\mathbb R}
E[(1+\tanh G-\alpha-\beta G)^2]
\ge\frac{e^{-1/8}}{800\sqrt{2\pi}}>0.
\tag{14}
\]

**Proof.** Odd symmetry makes the optimal constant \(\alpha=1\). The function \(\tanh z/z\) decreases for \(z>0\), since \(\tanh z-z\operatorname{sech}^2z\) has positive derivative \(2z\operatorname{sech}^2z\tanh z\) and vanishes at zero. Also \(\tanh(1/2)>9/20\), because \(e>8/3>29/11\). Therefore on \(1/4\le|G|\le1/2\), if \(\beta\le7/10\),

\[
|\tanh G-\beta G|\ge(9/10-7/10)|G|\ge1/20.
\]

The probability of this event is at least \(e^{-1/8}/(2\sqrt{2\pi})\), giving the right-hand side of (14). If \(\beta\ge7/10\), use \(2\le|G|\le9/4\): the error is at least \(2(7/10)-1=2/5\), and the event probability is at least \(e^{-81/32}/(2\sqrt{2\pi})\). This gives a larger lower bound; the comparison reduces to \(e^{77/32}<64\), which follows from \(77/32<3\) and \(e<3\). ∎

The same calculation also certifies initial scalar nonaffinity of the principal activation: its affine regression error is (1/16) times the left side of (14). This is an initialization statement, not a uniform-in-training nonaffinity claim.

## 7. Status registry

| Assertion | Status |
|---|---|
| Exact coordinate removal of the bottom gate for \(\Gamma=I\), \(\phi_B=1+\tanh\) | Proved |
| Global canonical strong raw population flow, uniqueness, and reached-state restart in that special case | Proved in Section 2, on the canonical action spaces |
| Finite raw-Euler transformed-coordinate defect and conditional finite-GF comparison | Proved in Section 3 |
| Full finite-width Gaussian GF/GD path/kernel/velocity bridge for that special case | Not claimed; additional identification obligations listed |
| The same gate-straightening works for general nonorthogonal inputs | False for any smooth strictly monotone nonaffine activation, by (13) |
| A positive offset gives an unconditional bounded-state kernel floor | False, by the equal-feature state |
| Compact support of curvature or bounded activation alone closes the principal target | Not established |
| Full principal fixed-activation contract | Still open |
