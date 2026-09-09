# Independent adversarial mathematical audit

## Verdict

**PASS for the stated prescribed-control claim. No required mathematical correction was found.** For every fixed \(0<|\rho|<1\), the indicated four-flow composition has an exact nearby fixed point for every sufficiently small positive \(\tau\). Its derivative has a real expanding eigenvalue, and repetition at that same fixed point gives the stated exponential lower bound. Both control-cost conventions and the fixed-horizon rescaling are correct.

The proof establishes failure of a polynomial tangent bound uniform over the stated class of exogenous sign-changing controls. It does not establish a trained-network counterexample, and that additional claim is neither assumed nor required in this review. Required corrections and optional presentation changes are separated below.

## Provenance and isolation

- Sole mathematical input: `/tmp/l3-two-sample-proof-DLuelg/GAUSSIAN_GATE_SIGN_SWITCHING_TEST.md`.
- Candidate SHA-256: `cd97bafe6125f53e67f05751efb0ffbb9b16368ab88a50fa9f419a258a91cb4d`.
- Candidate size: 6,013 bytes, 134 lines. The complete file was read, with line numbers; references below refer to those lines.
- Procedural skill personally read in full: `/etc/codex/skills/solve-math-rigorously/SKILL.md`.
- Skill SHA-256: `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7`.
- Skill size: 7,593 bytes, 115 lines. Its role was procedural only.
- Candidate hashes agreed at initial inspection and at the pre-write checkpoint, `2026-09-06T16:08:23Z`.
- The candidate hash was checked again after the substantive review was written, at `2026-09-06T16:12:12Z`, and still matched the hash above.
- No project files, history, other candidates, other reviews, mathematical sources, agents, numerical experiments, or symbolic-computation experiments were consulted or used. The calculations below were derived directly from the candidate. Shell operations were limited to reading the permitted inputs, verifying this output, and checking provenance metadata.
- The candidate was not edited. This review was written using `apply_patch` at the requested output path.

## Audit conventions and proof structure

Use the Euclidean state norm and its induced matrix operator norm. Composition acts from right to left. Constants in local remainder estimates may depend on the fixed \(\rho\), the fixed \(\epsilon=1/10\), and a fixed neighborhood, but do not depend on the repetition count \(N\). The period parameter \(\tau>0\) will be selected once and held fixed as \(N\) increases.

The decisive chain is: compute the actual chronological return map; prove its second-order expansion uniformly in the state derivative; find an exact zero of the rescaled displacement by contraction; prove real spectral separation for the rescaled derivative; and then take powers of the single exact return derivative. No large-\(N\) approximation of a drifting trajectory is needed.

## 1. Fields, complete flows, and chronological order

**Candidate lines 8–16 and 19–35: correct.** With \(p_j=p(z_j)\),

\[
X_1=(p_1,\rho p_1)^T,\qquad X_2=(\rho p_2,p_2)^T.
\]

Every derivative of \(p\) is a polynomial times \(\epsilon e^{-z^2}\), hence bounded. In particular,

\[
\begin{aligned}
p'(z)&=-2zp(z),\\
p''(z)&=(4z^2-2)p(z),\\
p'''(z)&=(12z-8z^3)p(z),\\
p^{(4)}(z)&=(16z^4-48z^2+12)p(z).
\end{aligned}
\]

Thus both fields are globally bounded and globally Lipschitz. One available speed bound is

\[
\|X_a\|_\infty\le v:=\epsilon\sqrt{1+\rho^2},
\]

and one Lipschitz bound is

\[
\|DX_a\|_\infty\le\epsilon\sqrt{2/e}\sqrt{1+\rho^2}.
\]

For completeness, a globally Lipschitz field has a unique local solution by contraction of its integral equation on a sufficiently short time interval. A bounded field satisfies \(\|z(t)-z(0)\|\le v|t|\); at any finite endpoint the solution is Cauchy and has a finite limit, from which the same local construction restarts it. This prevents finite-time loss of existence in either time direction. Uniqueness gives \((\Phi_a^t)^{-1}=\Phi_a^{-t}\). Differentiating the integral equation gives

\[
\partial_t D_z\Phi_a^t(z)
=DX_a(\Phi_a^t(z))D_z\Phi_a^t(z),
\qquad D_z\Phi_a^0=I.
\]

Higher differentiated equations have bounded coefficients and forcing built from bounded field derivatives and previously controlled flow derivatives on compact time intervals. Iterating these equations supplies the smoothness and bounded derivatives used below.

On the four successive time intervals, the controls produce the fields \(X_1,X_2,-X_1,-X_2\), each for duration \(\tau\). Therefore the chronological state maps are

\[
\Phi_1^\tau,\quad\Phi_2^\tau,\quad
\Phi_1^{-\tau},\quad\Phi_2^{-\tau},
\]

and the return map is exactly

\[
P_\tau=\Phi_2^{-\tau}\circ\Phi_1^{-\tau}
\circ\Phi_2^\tau\circ\Phi_1^\tau.
\]

The negative-time maps correctly represent positive-duration evolution under the negative fields. There is no order reversal or missing sign.

## 2. Second-order coefficient and uniform first-derivative remainder

**Candidate lines 37–53: correct.** For a smooth field \(F\), its flow has the local expansion

\[
\Phi_F^h(z)=z+hF(z)+\frac{h^2}{2}DF(z)F(z)+O_{C^1}(h^3).
\]

The second time derivative at zero is \(DF(z)F(z)\), so the quadratic term retains a positive sign for \(h=-\tau\).

Write \(a=X_1(z), b=X_2(z), A=DX_1(z), D=DX_2(z)\), as in the draft. Let \(q_j\) be the point after step \(j\). Expanding the field evaluations at the intermediate points gives

\[
\begin{aligned}
q_1&=z+\tau a+\frac{\tau^2}{2}Aa+O_{C^1}(\tau^3),\\
q_2&=z+\tau(a+b)
 +\tau^2\left(\frac12 Aa+Da+\frac12 Db\right)
 +O_{C^1}(\tau^3).
\end{aligned}
\]

Since \(X_1(q_2)=a+\tau A(a+b)+O_{C^1}(\tau^2)\),

\[
\begin{aligned}
q_3
&=q_2-\tau X_1(q_2)
 +\frac{\tau^2}{2}DX_1(q_2)X_1(q_2)+O_{C^1}(\tau^3)\\
&=z+\tau b+\tau^2\left(Da-Ab+\frac12 Db\right)
 +O_{C^1}(\tau^3).
\end{aligned}
\]

Now \(X_2(q_3)=b+\tau Db+O_{C^1}(\tau^2)\), so

\[
q_4=q_3-\tau X_2(q_3)
 +\frac{\tau^2}{2}DX_2(q_3)X_2(q_3)+O_{C^1}(\tau^3)
=z+\tau^2(Da-Ab)+O_{C^1}(\tau^3).
\]

Thus the coefficient is exactly

\[
B=DX_2X_1-DX_1X_2.
\]

This verifies its sign by actual composition, independently of any convention for naming a Lie bracket.

Here is an explicit justification of the uniform remainder that does not differentiate an unspecified pointwise error. Choose a fixed closed initial ball \(\overline B_r\) and a small fixed time range \(|\tau|\le\tau_*\). All four stages stay in the ball enlarged by \(4v\tau_*\), because each stage moves at most \(v|\tau|\). The flow regularity established above implies joint smoothness of \(P_\tau(z)\). Its third \(\tau\)-derivative and that derivative's first state derivative are bounded on the compact parameter set. The available field derivatives through order four are sufficient; all higher ones are available as well.

The composition calculation gives \(P_0(z)=z\), \(\partial_\tau P_0(z)=0\), and \(\partial_\tau^2P_0(z)=2B(z)\). Taylor's formula with integral remainder therefore gives the exact representation

\[
P_\tau(z)=z+\tau^2B(z)+\tau^3R_\tau(z),
\qquad
R_\tau(z)=\frac12\int_0^1(1-s)^2
 \left.\partial_h^3P_h(z)\right|_{h=s\tau}\,ds.
\]

The continuous, bounded state derivative of the integrand allows differentiation under this finite integral. In particular, there is a finite constant \(K\), independent of \(z\) and \(\tau\) in this parameter set, such that

\[
\sup_{z\in\overline B_r}
\max\{\|R_\tau(z)\|,\|D_zR_\tau(z)\|\}\le K.
\]

For example, \(K\) can be one sixth of the maximum of the corresponding two third-time-derivative bounds, since \(\frac12\int_0^1(1-s)^2ds=1/6\). Consequently,

\[
G(\tau,z)=B(z)+\tau R_\tau(z),\qquad
D_zG(\tau,z)=DB(z)+\tau D_zR_\tau(z).
\]

These expressions justify the asserted continuous extension in the state \(C^1\) topology at \(\tau=0\). A pointwise Taylor estimate alone would not suffice for contraction; the draft correctly requests the stronger estimate and has the regularity needed to obtain it.

## 3. Bracket, Gaussian constants, and nondegeneracy

**Candidate lines 55–66: correct.** The field Jacobians are

\[
DX_1=p'(z_1)Ce_1e_1^T,
\qquad DX_2=p'(z_2)Ce_2e_2^T.
\]

Using \(e_2^TCe_1=e_1^TCe_2=\rho\) yields

\[
B(z)=\rho\left[p(z_1)p'(z_2)Ce_2
 -p(z_2)p'(z_1)Ce_1\right].
\]

Substituting \(p'(z)=-2zp(z)\) makes every sign and factor explicit:

\[
B(z)=2\rho p(z_1)p(z_2)
\begin{pmatrix}z_1-\rho z_2\\ \rho z_1-z_2\end{pmatrix}.
\]

Therefore \(B(0)=0\), and

\[
M=DB(0)=2\rho\epsilon^2
\begin{pmatrix}1&-\rho\\ \rho&-1\end{pmatrix}
=2\rho\epsilon^2 C\operatorname{diag}(1,-1).
\]

In particular,

\[
\operatorname{tr}M=0,\qquad
\det M=-4\rho^2\epsilon^4(1-\rho^2),\qquad
M^2=4\rho^2\epsilon^4(1-\rho^2)I.
\]

The eigenvalues are the two distinct real numbers \(\lambda,-\lambda\), where

\[
\lambda=2|\rho|\epsilon^2\sqrt{1-\rho^2}
=\frac{|\rho|\sqrt{1-\rho^2}}{50}>0.
\]

The absolute value of \(\rho\) in \(\lambda\) is necessary and is present. The proof works for every \(0<|\rho|<1\); no further genericity exception is needed.

For later bounds, the exact Euclidean operator norms are

\[
m:=\|M\|=2|\rho|\epsilon^2(1+|\rho|),\qquad
\alpha:=\|M^{-1}\|
=\frac{1}{2|\rho|\epsilon^2(1-|\rho|)}.
\]

Indeed, right multiplication by \(\operatorname{diag}(1,-1)\) preserves singular values, and the positive definite matrix \(C\) has extreme singular values \(1+|\rho|\) and \(1-|\rho|\). These norms also show why the allowable neighborhoods and time thresholds need not remain uniform as \(\rho\) approaches an excluded endpoint. In particular, at \(\rho=0\) the fields commute and this commutator return is the identity. The draft correctly excludes the degeneracies.

## 4. Exact fixed point and its scale

**Candidate lines 68–82: correct.** The following choices make the contraction and its quantifiers explicit.

Fix \(\rho\) first. By continuity of \(DB\), choose a fixed \(r>0\) such that

\[
\alpha\sup_{z\in\overline B_r}\|DB(z)-M\|\le\frac14.
\]

Use the uniform remainder constant \(K\) on that ball. Reduce the positive upper bound on \(\tau\) so that

\[
\alpha K\tau\le\frac14,
\qquad \alpha K\tau\le\frac r2.
\]

For \(\Psi_\tau(z)=z-M^{-1}G(\tau,z)\),

\[
D\Psi_\tau(z)
=M^{-1}\bigl(M-DB(z)-\tau D_zR_\tau(z)\bigr),
\qquad \|D\Psi_\tau(z)\|\le\frac12.
\]

Integrating this derivative on the segment between any two points of the convex ball gives Lipschitz constant at most \(1/2\). Also,

\[
G(\tau,0)=\tau R_\tau(0),\qquad
\|\Psi_\tau(0)\|\le\alpha K\tau.
\]

For \(\|z\|\le r\),

\[
\|\Psi_\tau(z)\|
\le\tfrac12\|z\|+\|\Psi_\tau(0)\|
\le\tfrac r2+\alpha K\tau\le r.
\]

This verifies the self-map property rather than merely the derivative bound. Iteration from any point in the closed ball stays in the ball, and consecutive differences decrease by a factor at most \(1/2\). The geometric-series bound makes the iterates Cauchy. Completeness of the closed ball and continuity of \(\Psi_\tau\) give a fixed point. Two fixed points would have distance at most half their distance, so they coincide within this ball.

At that point,

\[
\|z_\tau\|
\le\tfrac12\|z_\tau\|+\|\Psi_\tau(0)\|,
\qquad
\|z_\tau\|\le2\alpha K\tau.
\]

This proves the stated \(O(\tau)\) estimate with a constant independent of \(N\). Since \(M\) is invertible, \(\Psi_\tau(z_\tau)=z_\tau\) is equivalent to \(G(\tau,z_\tau)=0\). Since \(\tau>0\), that equation is equivalent to the exact identity

\[
P_\tau(z_\tau)=z_\tau.
\]

Uniqueness is local to the selected ball, as stated. The proof does not replace exact recurrence by recurrence up to a remainder.

## 5. Derivative at the fixed point and real eigenvalues

**Candidate lines 84–93: correct.** Let

\[
L:=\sup_{z\in\overline B_r}\|D^2B(z)\|<\infty.
\]

The first-derivative Taylor estimate and the fixed-point bound imply

\[
DP_\tau(z_\tau)=I+\tau^2A_\tau,\qquad
A_\tau=M+E_\tau,
\]

where

\[
\begin{aligned}
E_\tau&=DB(z_\tau)-M+\tau D_zR_\tau(z_\tau),\\
\|E_\tau\|&\le L\|z_\tau\|+K\tau
\le K(1+2\alpha L)\tau.
\end{aligned}
\]

Thus the \(O(\tau)\) in the brackets in candidate equation (3) is justified. Its constant is fixed before any repetitions are taken.

The eigenvalue perturbation must be performed on \(A_\tau\), whose limiting eigenvalues are distinct. Perturbing the identity without keeping track of the \(\tau^2\) scale would not justify reality. The draft uses the correct matrix.

Here are sufficient quantitative conditions, also addressing possible nonnormality of \(M\). Write \(e=\|E_\tau\|\). For two-by-two matrices,

\[
|\operatorname{tr}A_\tau|\le2e,
\qquad
|\det A_\tau+\lambda^2|\le2me+e^2.
\]

The determinant estimate follows by expanding
\(\det(M+E)=\det M+\operatorname{tr}(\operatorname{adj}(M)E)+\det E\), using \(\operatorname{adj}(M)=-M\), \(|\operatorname{tr}(ME)|\le2me\), and \(|\det E|\le e^2\).

Because \(e\to0\), reduce \(\tau\) so that

\[
2e\le\frac\lambda2,
\qquad 2me+e^2\le\frac{\lambda^2}{4}.
\]

Then \(\det A_\tau\) lies between \(-5\lambda^2/4\) and \(-3\lambda^2/4\). Its characteristic discriminant \(\Delta_\tau\) satisfies

\[
3\lambda^2\le\Delta_\tau
=(\operatorname{tr}A_\tau)^2-4\det A_\tau
\le\frac{21}{4}\lambda^2.
\]

The two real roots are therefore distinct, and the quadratic formula yields

\[
\begin{aligned}
\mu_+&\ge\frac{\sqrt3-1/2}{2}\lambda>\frac\lambda2,\\
\mu_-&\le-\frac{\sqrt3-1/2}{2}\lambda<-\frac\lambda2,\\
|\mu_\pm|&\le\frac{1+\sqrt{21}}4\lambda<2\lambda.
\end{aligned}
\]

These explicit bounds verify the draft's continuity/discriminant argument without assuming symmetry of \(M\). The eigenvalues of \(DP_\tau(z_\tau)\) are exactly

\[
\nu_\pm=1+\tau^2\mu_\pm,
\qquad \nu_+\ge1+\frac{\lambda\tau^2}{2}.
\]

Each real eigenvalue has a real nonzero eigenvector, which can be normalized to unit length. Reducing \(\tau\) further to satisfy \(2\lambda\tau^2<1\) also gives \(0<\nu_-<1<\nu_+\), so the fixed point is a hyperbolic saddle. The weighted determinant calculation below gives an additional exact check on this conclusion.

## 6. Repetition and exponential lower bound

**Candidate lines 95–104: correct.** Fix one sufficiently small \(\tau>0\), and use the fixed point just constructed. Every complete period returns the reference orbit exactly to \(z_\tau\). The chain rule gives

\[
D(P_\tau^N)(z_\tau)
=DP_\tau(P_\tau^{N-1}(z_\tau))\cdots DP_\tau(z_\tau)
=DP_\tau(z_\tau)^N.
\]

In this formula, differentiation is with respect to the initial state. Neither the chosen \(\tau\) nor the schedule is differentiated. The notation does not denote differentiation of the branch \(\tau\mapsto z_\tau\).

Let \(v_\tau\) be a unit eigenvector for \(\nu_+\). For every integer \(N\ge1\),

\[
\|D(P_\tau^N)(z_\tau)\|
\ge\|DP_\tau(z_\tau)^Nv_\tau\|
=\nu_+^N
\ge\left(1+\frac{\lambda\tau^2}{2}\right)^N.
\]

This uses an eigenvector of the actual return derivative. No estimate of a product of different expanding matrices, no eigenvector conditioning estimate, and no inference from an instantaneous generator are involved.

Set \(x=\lambda\tau^2/2\). When \(0\le x\le1\),

\[
\log(1+x)=\int_0^x\frac{ds}{1+s}\ge\frac{x}{2}.
\]

Hence

\[
\|D(P_\tau^N)(z_\tau)\|
\ge\exp\left(\frac{\lambda\tau^2}{4}N\right).
\]

The draft's factor \(1/4\) is correct. A valid explicit choice in its opening claim is

\[
c_\tau=\frac{\lambda\tau^2}{4}
=\frac{|\rho|\sqrt{1-\rho^2}}{200}\tau^2>0.
\]

For each fixed \(\rho\), all smallness conditions in this review can be met by choosing a single positive threshold \(\tau_0(\rho)\). They depend on finitely many fixed constants and on \(\lambda>0\), and none depends on \(N\). Thus the quantifiers are

\[
\forall\rho\ (0<|\rho|<1),\quad
\exists\tau_0>0,\quad
\forall\tau\in(0,\tau_0),\quad
\exists z_\tau,\quad
\forall N\ge1.
\]

In particular, the proof does not require shrinking \(\tau\) as \(N\) grows. The \(O(\tau^3)\) one-period expansion has already been absorbed into a rigorous eigenvalue lower bound for one exact matrix; there is no uncontrolled accumulated Taylor error.

## 7. Costs and exclusion of every finite polynomial bound

**Candidate lines 24–28 and 108–111: correct.** Each unscaled control value is one of \(\pm e_1,\pm e_2\), with \(\ell^1\) norm one. Thus the raw control cost over \(N\) periods is exactly

\[
L_N:=\int_0^{4\tau N}\|u(t)\|_1\,dt=4\tau N,
\]

and the activation-scaled convention gives

\[
U_N:=\epsilon L_N=4\epsilon\tau N.
\]

The derivative lower bound becomes

\[
\|D(P_\tau^N)(z_\tau)\|
\ge\exp\left(\frac{\lambda\tau}{16}L_N\right)
=\exp\left(\frac{\lambda\tau}{16\epsilon}U_N\right).
\]

With \(\epsilon=1/10\), the coefficients are

\[
\frac{\lambda\tau}{16}
=\frac{|\rho|\sqrt{1-\rho^2}}{800}\tau,
\qquad
\frac{\lambda\tau}{16\epsilon}
=\frac{|\rho|\sqrt{1-\rho^2}}{80}\tau.
\]

Both coefficients are strictly positive when \(\rho\) and \(\tau\) are fixed as above. They are not asserted to stay bounded away from zero as \(\tau\to0\) or as \(\rho\) approaches an excluded value.

To spell out the polynomial contradiction, fix this \(\rho,\tau,z_\tau\). A finite polynomial bound would in particular give an upper bound of the form \(A(1+U_N)^d\), with finite \(A>0\) and finite \(d\ge0\) independent of \(N\). These constants may depend on \(\rho,z_\tau\), and may even depend on the already fixed \(\tau\). Let \(a=\lambda\tau/(16\epsilon)>0\) and choose an integer \(k>d\). The exponential series gives \(e^{aU}\ge(aU)^k/k!\), whose ratio to \(A(1+U)^d\) tends to infinity. Since \(U_N\to\infty\), the proposed bound fails on this sequence. A single fixed initial point suffices; a varying-initial-point argument is not being substituted for it.

## 8. Fixed-horizon rescaling and frozen-control differentiation

**Candidate lines 113–118: correct.** Write \(T_N=4\tau N\). For any initial point \(z_0\), let \(z(t;z_0)\) solve the original schedule and set

\[
y_N(s;z_0):=z(T_Ns;z_0),\qquad
u_N(s):=T_Nu(T_Ns),\quad 0\le s\le1.
\]

Away from finitely many switching times,

\[
\frac{dy_N}{ds}
=T_N\sum_{a=1}^2u_a(T_Ns)X_a(y_N)
=\sum_{a=1}^2(u_N)_a(s)X_a(y_N).
\]

Both sides define the same absolutely continuous solution across the switching times, so the equality holds in the integral-equation sense on all of \([0,1]\). Uniqueness on each piece identifies this as the solution driven by the rescaled schedule.

The rescaled schedule has \(4N\) pieces, each of duration \(1/(4N)\), and its values are \(T_N\) times the same four signed coordinate vectors in repeated order. It is piecewise constant and integrable for every finite \(N\). Change of variables gives

\[
\int_0^1\|u_N(s)\|_1\,ds
=\int_0^1T_N\|u(T_Ns)\|_1\,ds
=\int_0^{T_N}\|u(t)\|_1\,dt.
\]

The activation-scaled cost is consequently unchanged as well. Since the endpoint-map identity holds for every initial point under the same fixed schedules,

\[
D_{z_0}y_N(1;z_0)=D_{z_0}z(T_N;z_0).
\]

At \(z_0=z_\tau\) this is exactly the repeated return derivative already bounded below. There is no missing factor of \(T_N\) in the initial-state derivative; that factor appears in the time derivative and is incorporated into the control.

The scaled amplitudes \(\|u_N\|_{L^\infty}=T_N\) are not uniformly bounded as \(N\to\infty\). This does not violate the draft's integrability-only control class. The argument establishes failure on the fixed horizon \([0,1]\) in that class; it does not establish such failure under an additional common amplitude bound on that same horizon. The original, unscaled sequence does have unit amplitude on its increasing horizons.

## 9. Weighted area, contraction of the other direction, and signs

**Candidate lines 120–125: mathematically consistent.** The weighted determinant identity can be checked directly from the given fields, without any external Gaussian-gate result.

Because \(|\rho|<1\), define the positive definite quadratic form and positive density

\[
V(z)=z^TC^{-1}z,
\qquad w(z)=e^{V(z)}.
\]

For a fixed prescribed control, put \(F(t,z)=u_1(t)X_1(z)+u_2(t)X_2(z)\). On each time piece,

\[
\operatorname{div}_zF
=u_1p'(z_1)+u_2p'(z_2)
=-2\sum_{a=1}^2u_az_ap(z_a).
\]

Also \(\nabla V=2C^{-1}z\), and symmetry of \(C^{-1}\) gives

\[
\frac{d}{dt}V(z(t))
=\nabla V(z(t))^TF(t,z(t))
=2\sum_{a=1}^2u_a(t)z_a(t)p(z_a(t)).
\]

The two expressions have opposite signs. For the variational matrix \(J(t)\), the differential equation \(J'=D_zF\,J\) and invertibility of the composed flow maps give

\[
\frac{d}{dt}\log\det J(t)
=\operatorname{tr}(J^{-1}J')
=\operatorname{tr}D_zF
=-\frac{d}{dt}V(z(t)).
\]

The determinant starts at one and stays positive. Integrating on each piece and concatenating yields the exact identity

\[
\det J(t)=e^{V(z_0)-V(z(t))},
\qquad w(z(t))\det J(t)=w(z_0).
\]

At the exact return point, it specializes to

\[
\det DP_\tau(z_\tau)=1.
\]

The two eigenvalues consequently satisfy \(\nu_-\nu_+=1\). Since \(\nu_+>1\), necessarily \(\nu_-=\nu_+^{-1}\in(0,1)\). This is an independent exact consistency check on the saddle conclusion and on the claim that expansion in one direction coexists with contraction in another. The identity concerns a weighted area globally; the ordinary determinant equals one at this return because the initial and final states coincide. No finiteness of the measure with density \(w\) is needed.

The four values \(e_1,e_2,-e_1,-e_2\) are not contained in any one fixed closed sign quadrant. Hence an estimate restricted to one fixed sign quadrant is not contradicted. Literally, these values lie on coordinate axes, rather than inside four open quadrants; the wording issue is listed as optional below.

A determinant constraint does not supply an upper bound on the largest singular value: in this example the return determinant is exactly one while the established operator norm grows exponentially under repetition. The file does not define a particular “initial response sign,” so no separate theorem about such a quantity can be checked from the permitted input. That phrase is not used in any step of the prescribed-control proof.

## 10. Scope and logical boundary

**Candidate lines 3–6 and 127–134: appropriately limited.** The proved mathematical conclusion is that a polynomial bound in total absolute control cost cannot hold uniformly for the initial-state tangents of all integrable exogenous sign-changing controls for these two fields. This conclusion holds at one fixed initial point after \(\rho\) and \(\tau\) have been fixed, including on the fixed horizon after rescaling.

No training equation, backpropagation rule, network parameter coupling, energy constraint, or initialization distribution is part of this construction. Consequently, the proof supplies no assertion that canonical gradient flow realizes the control sequence or that a probabilistic initialization reaches the constructed return point. Those are explicitly excluded claims, not missing hypotheses for the proposition actually proved. No trained-control continuation was sought or audited.

The “requested two-sample theorem” and the “Gaussian-gate strategy” are not defined in the sole permitted mathematical input. Their truth and the status of any actual trained-control continuation cannot be evaluated here. The final methodological conclusion is justified to the extent that it rules out a proposed bridge consisting of a universal polynomial bound over *all* of the exogenous sign-changing controls considered here. It does not rule out a bound for a smaller, training-constrained subclass.

## Required corrections

**None for the stated prescribed-control proposition.** In particular, no correction is required to the chronological flow order, bracket sign, factors involving \(\epsilon\) and \(\rho\), uniform state \(C^1\) remainder, contraction construction, \(O(\tau)\) fixed-point scale, real eigenvalue argument, repeated derivative, exponential constants, cost conversion, or time rescaling.

The explicit estimates supplied in this review expand valid abbreviated arguments in the draft. They do not repair a false step or introduce a new mathematical assumption. Requiring realization by trained controls would change the claim under review and is not a required correction.

## Optional presentation changes

1. **Norm and parameter conventions, lines 18–28.** State once that the tangent norm is an induced operator norm, \(\rho\) is fixed first, and the smallness threshold for \(\tau\) may depend on \(\rho\). Explicitly saying that \(\tau\) and \(z_\tau\) remain fixed as \(N\to\infty\) would make the polynomial contradiction easier to scan. The existing proof already has these quantifiers.
2. **Taylor and contraction details, lines 48–53 and 71–81.** If a fully expanded proof is desired, display \(P_\tau=z+\tau^2B+\tau^3R_\tau\) with a uniform bound on \(R_\tau,D_zR_\tau\), and the two inequalities establishing contraction and ball invariance. Sections 2 and 4 above give suitable details. The globally bounded field derivatives already justify the draft's concise version.
3. **Spectral and determinant checks, lines 88–93 and 122–125.** One can display \(0<\nu_-<1<\nu_+\) and the exact identity \(\det DP_\tau(z_\tau)=1\). This makes the title's hyperbolicity and compatibility with weighted area preservation immediate to a reader. It is not needed to strengthen the expanding-direction proof.
4. **Quadrant wording, line 121.** Replace “It crosses quadrants every quarter-period” with “It cycles through the four signed coordinate directions and is not confined to any fixed sign quadrant.” This avoids suggesting that the controls enter open quadrants or vary continuously at the switches. The mathematical distinction from a fixed-sign class is already correct.
5. **Rescaling and rate, lines 110–118.** Optionally display the exact exponent \((\lambda\tau/(16\epsilon))U_N\) and note that the fixed-horizon amplitudes increase with \(N\). Both facts follow from the displayed formulas; they clarify the applicable control class without changing the result.

## Final assessment

The candidate withstands this isolated mathematical audit as a prescribed-control obstruction to a universal polynomial tangent bound. Every essential proof step has been verified above, including the exact recurrence needed for arbitrarily many repetitions. There is no finding here about whether trained dynamics can generate these controls.
