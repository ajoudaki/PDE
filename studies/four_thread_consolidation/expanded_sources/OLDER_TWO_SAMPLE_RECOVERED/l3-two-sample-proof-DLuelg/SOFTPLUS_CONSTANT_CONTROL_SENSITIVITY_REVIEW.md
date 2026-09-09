# Independent adversarial audit: softplus constant-control sensitivity

**Verdict: PASS within the stated deterministic constant-control scope.** I found no incorrect sign-table bound, prefactor, exponent, shooting argument, trajectory identity, tangent lower bound, or invariant formula. The main counterexample is proved at one fixed finite initial point for each fixed negative correlation. No required mathematical correction was identified. One optional clarification concerns the quantifiers in the fixed-time, increasing-amplitude remark.

## 1. Audit identity, restrictions, and disposition

- Candidate: `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_CONSTANT_CONTROL_SENSITIVITY.md`.
- Exact SHA-256, verified from the candidate bytes: `cc61329a498a65da53513a2af948febba35b07d1ee47547de863584f0541e38a`.
- Candidate length: 488 lines. All line references below refer to this exact candidate.
- The candidate was the sole mathematical source inspected. The expressly permitted procedural guidance `/etc/codex/skills/solve-math-rigorously/SKILL.md` was also read.
- No referenced arctangent notes, registry, other research files, reviews, or history were read. No external sources, experiments, numerical shooting, or auxiliary agents were used. The candidate was not edited.
- Assertions about the author's prior reading or the provenance of the suggested invariant are not independently verified; none is needed for the mathematical conclusions.

The audit proceeds by deriving the common energy estimate, checking every control-sign case, testing the zero-tail estimate without assuming coordinate monotonicity, reconstructing the infinite-horizon shooting limit, and checking the full tangent and the invariant independently.

The result being accepted is specifically about

\[
\frac{dz}{ds}=C_\rho\operatorname{diag}(\varepsilon f(z_1),\varepsilon f(z_2))q,
\qquad f(z)=\frac{e^z}{1+e^z},\quad \varepsilon=\frac1{10},
\]

with constant \(q\), constant \(|\rho|<1\), and sensitivity with respect to the initial state. It is not a result about actual trained dynamics, a changing Gram matrix, arbitrary control histories, or Gaussian-averaged sensitivity.

## 2. Flow and the common tangent estimate

**Candidate lines 74–134: valid.** Write \(\tau=\varepsilon s\), \(k=|\rho|\), and

\[
F(z)=C_\rho\operatorname{diag}(f(z_1),f(z_2))q.
\]

The eigenvalues of \(C_\rho\) are \(1\pm\rho\); its smallest and largest eigenvalues are \(1-k\) and \(1+k\). Also

\[
f'=f(1-f),\qquad 0<f<1,\qquad 0<f'\leq\frac14.
\]

Consequently

\[
|F(z)|\leq(1+k)|q|_2,
\qquad
\|DF(z)\|\leq\frac{1+k}{4}|q|_\infty.
\]

These are the constants displayed in the candidate. Global Lipschitz continuity gives uniqueness and convergence of the stated integral iteration on every finite interval. Bounded speed precludes finite escape in either time direction. The bounded second derivative \(f''=f'(1-2f)\) supplies the Lipschitz bound on \(DF\) used for the quadratic Taylor remainder. The comparison with the linear integral equation therefore establishes the initial-state derivative required here. There is no unproved differentiability assumption affecting the tangent calculation.

With \(D=\operatorname{diag}(q_1f'(z_1),q_2f'(z_2))\), the tangent equation is \(\dot\eta=C_\rho D\eta\). For \(E=\eta^TC_\rho^{-1}\eta\), symmetry gives the exact identity

\[
\dot E
=\eta^TDC_\rho C_\rho^{-1}\eta
 +\eta^TC_\rho^{-1}C_\rho D\eta
=2\eta^TD\eta.
\]

Moreover

\[
E=\frac{\eta_1^2-2\rho\eta_1\eta_2+\eta_2^2}{1-\rho^2}
=\eta_1^2+\frac{(\eta_2-\rho\eta_1)^2}{1-\rho^2}.
\]

Interchanging the indices proves both \(\eta_1^2\leq E\) and \(\eta_2^2\leq E\). It follows that, for

\[
I(\tau)=\int_0^\tau\sum_{i:q_i>0}q_if'(z_i(r))\,dr,
\]

\[
\dot E\leq2\dot I E,
\qquad E(\tau)\leq e^{2I(\tau)}E(0).
\]

The norm conversion is

\[
\frac{|\eta(\tau)|^2}{1+k}\leq E(\tau),
\qquad E(0)\leq\frac{|\eta(0)|^2}{1-k}.
\]

Taking the supremum over unit initial tangents yields exactly

\[
\|J(s)\|\leq\sqrt{\frac{1+k}{1-k}}\,e^{I(\varepsilon s)}.
\]

There is no missing factor of two in the exponent and no missing eigenvalue factor inside \(I\). The square root of the condition number is the correct prefactor for the displayed argument.

## 3. Every sign-table case and its boundary cases

**Candidate lines 39–67 and 136–151: valid.** Put \(g=1-f\) and \(H(v)=\log(1+e^{-v})\). Then

\[
H'=-g,\qquad f'=fg,\qquad H\geq0.
\]

Coordinate exchange preserves \(C_\rho\) and Euclidean norms, so the relabeling used for mixed signs and a single active positive control is legitimate.

| Configuration | Verified estimate for the positive-curvature integral | Consequence |
| --- | --- | --- |
| \(q_1,q_2\leq0\), any \(\rho\) | \(I=0\), and actually \(\dot E\leq0\) | \(\|J(s)\|\leq\sqrt\kappa\) |
| \(q_1,q_2\geq0\), \(\rho\geq0\) | \(I\leq H(z_{0,1})+H(z_{0,2})\) | Exactly the second table row |
| \(q=(a,-b)\), \(a,b>0\), \(\rho\leq0\) | \(I\leq H(x_0)\) | Exactly the third table row |
| \(q=(a,-b)\), \(a,b>0\), \(\rho=k>0\) | The logarithmic estimate established in Section 4 below | Exactly the fourth table row |
| One positive control and one zero control, any \(\rho\) | \(I\leq H(x_0)\), with \(x\) the active coordinate | Exactly the last table row |
| \(q_1,q_2>0\), \(\rho<0\) | The candidate constructs exponential growth for \(q=(1,1)\) | An existential counterexample for this sign class, not a claim about every such control |

The derivations of the bounded cases are as follows.

For two nonnegative controls and \(\rho\geq0\),

\[
\dot z_i\geq q_if(z_i),\qquad
-\frac{d}{d\tau}\sum_iH(z_i)
=\sum_i g(z_i)\dot z_i
\geq\sum_iq_if'(z_i).
\]

Integration and \(H\geq0\) give the stated integral bound. This also covers zero controls in that row.

For \(q=(a,-b)\) and \(\rho=-k\leq0\),

\[
\dot x=af(x)+kbf(y)\geq af(x),
\qquad -\dot H(x)\geq af'(x).
\]

Only the first coordinate contributes to \(I\). For one positive control and one zero control, \(\dot x=af(x)\) regardless of \(\rho\), so the same conclusion holds, with equality in this last differential identity.

Controls consisting of one negative and one zero component belong to the first row. The zero control gives \(J=\mathrm{Id}\). Correlation \(\rho=0\) is covered without taking any singular limit. All denominators involving \(1-k\) are positive under the stipulated \(|\rho|<1\).

Thus no sign or zero-control configuration has been omitted. The wording at lines 58–60 correctly distinguishes coverage of sign configurations from a classification of every positive control direction when \(\rho<0\).

## 4. Mixed signs, positive correlation, and the zero-tail estimate

**Candidate lines 153–219: valid, including the explicit prefactor.** For \(a,b>0\), \(0<k<1\), and

\[
A=af(x),\qquad B=bf(y),
\]

the equations are

\[
\dot x=A-kB,\qquad \dot y=kA-B.
\]

No monotonicity of \(x\) or \(y\) is needed. Their difference satisfies

\[
w=x-y,\qquad \dot w=(1-k)(A+B)>0.
\]

Since \(-\dot H(x)=Ag(x)-kBg(x)\), integration gives the exact decomposition

\[
I(\tau)=H(x_0)-H(x(\tau))+k\int_0^\tau Bg(x)\,dr.
\]

The product estimate used to control the last term is valid for all real \(x,y\):

\[
f(y)g(x)=\frac{e^y}{(1+e^y)(1+e^x)}\leq e^{y-x}=e^{-w},
\]

because \((1+e^y)(1+e^x)\geq e^x\).

For a fixed final \(\tau\geq0\), set \(W=\log(1+b\tau)\geq0\). If \(w_0>W\), the part of the path with \(w\leq W\) is empty. Otherwise it is an initial interval, and on it

\[
\int B\,dr\leq\frac1{1-k}\int\dot w\,dr
\leq\frac{W-w_0}{1-k}.
\]

This proves the uniform bound \((W-w_0)_+/(1-k)\), including paths that never reach the threshold. On the remaining part of the path,

\[
Bg(x)\leq be^{-W},
\]

so its integral is at most \(b\tau/(1+b\tau)\). Therefore

\[
\int_0^\tau Bg(x)\,dr
\leq\frac{(W-w_0)_+}{1-k}+\frac{b\tau}{1+b\tau}
\leq\frac{\log(1+b\tau)+(-w_0)_+}{1-k}+1.
\]

The last inequality uses \(W\geq0\). Substitution gives

\[
I(\tau)
\leq H(x_0)+k+\frac{k}{1-k}(y_0-x_0)_+
 +\frac{k}{1-k}\log(1+b\tau).
\]

Consequently the verified bound is precisely

\[
\|J(s)\|
\leq\sqrt\kappa\,
\exp\!\left\{H(x_0)+k+\frac{k}{1-k}(y_0-x_0)_+\right\}
(1+\varepsilon bs)^{k/(1-k)}.
\]

In particular, the constant term is \(+k\), and the power is \(k/(1-k)\). Neither requires a factor depending on \(a/b\). The final-time-dependent threshold is permissible: it is an integration device for each fixed observation time, not a time-dependent control or initial point.

Because \(\varepsilon b s\leq |q|_2s=T\), this is a polynomial-growth bound in \(1+T\). The prefactor is finite at every finite initial point and bounded on bounded initial sets for fixed \(k<1\). It is not uniform over all initial points or over correlations approaching one; neither uniformity is claimed.

The instantaneous-balance calculation also checks. At \(A=kB\),

\[
\dot y=-(1-k^2)B,
\]

and differentiating \(\dot x=A-kB\) yields

\[
\ddot x=af'(x)\dot x-kbf'(y)\dot y
=k(1-k^2)B^2g(y)>0.
\]

This is a strict local minimum of \(x\). It does not justify freezing \(y\), and the candidate does not freeze it.

Finally,

\[
\frac{d}{d\tau}(y-kx)=-(1-k^2)B.
\]

If \(x\) stayed in a fixed compact interval after some time, a finite integral of \(B\) would make \(y\) bounded and hence make \(B=bf(y)\) uniformly positive, a contradiction. An infinite integral would imply \(y\to-\infty\), so \(B\to0\) and eventually \(\dot x\geq af(m)/2>0\), also a contradiction. Both branches of this argument are valid. The logarithmic estimate above remains the quantitative justification of the polynomial bound.

## 5. Backward shooting: existence, convergence, and uniqueness

**Candidate lines 221–310: valid.** Fix \(0<k<1\), \(\rho=-k\), and \(q=(1,1)\). The rescaled equations are

\[
\dot x=f(x)-kf(y),\qquad \dot y=f(y)-kf(x).
\]

The proposed constants satisfy

\[
f(L_k)=\frac k2,\qquad f(U_k)=k,\qquad
f(Y_k)=\frac{1+k}{2},\qquad L_k<U_k,
\]

and

\[
d_k=\frac{1+k}{2}-k^2=\frac{(1-k)(1+2k)}2>0.
\]

Throughout \(L_k\leq x\leq U_k\), \(y\geq Y_k\), the denominator

\[
D(x,y)=f(y)-kf(x)
\]

satisfies \(d_k\leq D\leq1\). Hence using \(y\) as an independent variable is legitimate, and

\[
G(X,y)=\frac{f(X)-kf(y)}{D(X,y)}
\]

is smooth in a neighborhood of every point of the strip.

At \(X=L_k\), its numerator is at most

\[
\frac k2-k\frac{1+k}{2}=-\frac{k^2}{2}<0.
\]

At \(X=U_k\), its numerator is \(k(1-f(y))>0\) for every finite \(y\). Since the denominator is positive, these are exactly the claimed boundary signs. They point outward in forward \(y\) and inward when integrating backward.

For each integer \(n\geq1\), solving backward from \(X_n(Y_k+n)=U_k\) therefore keeps \(X_n\) in the strip. The strict boundary signs prevent an exit or a later boundary touch in backward time, so the solution is interior before its terminal endpoint. Uniform bounds on \(G\) and its derivative on the strip give extension to \(Y_k\). The denominator cannot vanish during this construction.

The derivative calculation is

\[
G_X
=\frac{f'(X)\{f(y)-kf(X)+k[f(X)-kf(y)]\}}{D^2}
=\frac{(1-k^2)f'(X)f(y)}{D^2}.
\]

In particular,

\[
0<G_X\leq M_k:=\frac{1-k^2}{4d_k^2}.
\]

For \(m>n\), the longer backward shot satisfies \(X_m(Y_k+n)<U_k=X_n(Y_k+n)\). Scalar uniqueness prevents the graphs from meeting, including when compared backward on their common interval. Thus

\[
\alpha_m:=X_m(Y_k)<X_n(Y_k)=:\alpha_n,
\qquad L_k<\alpha_n<U_k.
\]

The decreasing sequence has a limit \(\alpha_k\geq L_k\). This limit alone would not establish an infinite-horizon trajectory, but the candidate supplies the necessary additional argument: on any fixed \([Y_k,Y_k+R]\), for integer \(m,n\geq R\),

\[
\sup|X_m-X_n|\leq e^{M_kR}|\alpha_m-\alpha_n|.
\]

It follows that the shots are uniformly Cauchy on that interval. The bound on \(G_X\) also bounds the difference of their integrands, so passing to the integral equation is justified. Limits on overlapping intervals agree. This constructs one solution \(X\) on the whole half-line, with

\[
X(Y_k)=\alpha_k,\qquad L_k\leq X(y)\leq U_k\quad(y\geq Y_k).
\]

For uniqueness, define

\[
c_k=\min\left\{\frac k2\left(1-\frac k2\right),\ k(1-k)\right\}>0.
\]

Concavity of \(u(1-u)\) on \([k/2,k]\) proves \(f'(X)\geq c_k\) throughout the strip. Since \(D^2\leq1\) and \(f(y)\geq(1+k)/2\),

\[
G_X\geq\ell_k:=\frac{(1-k^2)c_k(1+k)}2>0.
\]

If two distinct graphs remained in the strip for all \(y\geq Y_k\), their positive difference \(\delta\) would satisfy

\[
\delta'=\left(\int_0^1G_X(X_1+t\delta,y)\,dt\right)\delta
\geq\ell_k\delta.
\]

It would therefore grow at least as \(\delta(Y_k)e^{\ell_k(y-Y_k)}\), contradicting \(\delta\leq U_k-L_k\). This proves uniqueness of the graph that stays in the specified strip. The boundary signs also exclude \(\alpha_k=L_k\) or \(\alpha_k=U_k\).

The uniqueness claim is thus properly supported: it is uniqueness of the initial coordinate at height \(Y_k\) whose future remains in this strip. It is not a claim that no other initial state can have exponential sensitivity.

## 6. Exact two-dimensional trajectory and its limits

**Candidate lines 312–345: valid.** For the graph just constructed, let

\[
\tau(y)=\int_{Y_k}^y\frac{dr}{f(r)-kf(X(r))}.
\]

Then \(1\leq\tau'(y)\leq1/d_k\), so \(\tau\) maps \([Y_k,\infty)\) bijectively onto \([0,\infty)\) and has a differentiable inverse. Setting \(x(\tau)=X(y(\tau))\) gives

\[
\dot y=f(y)-kf(x),
\qquad
\dot x=X'(y)\dot y=f(x)-kf(y).
\]

Both state equations are satisfied exactly. Also

\[
z_0=(\alpha_k,Y_k),\qquad
L_k\leq x(\tau)\leq U_k,\qquad
Y_k+d_k\tau\leq y(\tau)\leq Y_k+\tau.
\]

Neither \(z_0\) nor the resulting trajectory is chosen anew for each observation time. The finite terminal horizons occur only in the definition of a single convergent shooting sequence.

The asserted limit \(x\to U_k\) also follows from the supplied argument. For \(0<h<U_k-L_k\), let \(r_h=k-f(U_k-h)>0\). For all sufficiently large \(\tau\),

\[
kf(y(\tau))\geq k-r_h/2.
\]

If \(x\leq U_k-h\) at such a time, then \(\dot x\leq-r_h/2\) while it remains in that region. The same strict sign at its upper boundary prevents escape upward. It would cross below \(L_k\) in finite time, contradicting the strip construction. Thus eventually \(x>U_k-h\), for every such \(h\), proving the limit.

Consequently

\[
f(x)\to k,
\quad f(y)\to1,
\quad \dot x\to0,
\quad \dot y\to1-k^2.
\]

The second coordinate escapes into the nonzero positive tail; it is not a frozen coordinate. The stated absence of nonzero-control finite equilibria is also correct, because \(C_\rho\) and the finite-state diagonal gate matrix are invertible.

## 7. Full tangent growth and all numerical constants

**Candidate lines 347–384: valid.** Along the exact trajectory, the tangent coefficient matrix is

\[
A(\tau)=
\begin{pmatrix}
f'(x)&-kf'(y)\\
-kf'(x)&f'(y)
\end{pmatrix}.
\]

Reflecting by \(S=\operatorname{diag}(1,-1)\) is orthogonal and gives

\[
\dot v=SASv
=\begin{pmatrix}
f'(x)&kf'(y)\\
kf'(x)&f'(y)
\end{pmatrix}v,
\qquad v(0)=(1,0).
\]

Every coefficient is nonnegative. On every finite interval the convergent ordered integral expansion of the fundamental solution has nonnegative entries term by term. Hence \(v_1,v_2\geq0\), and

\[
\dot v_1=f'(x)v_1+kf'(y)v_2\geq c_kv_1.
\]

Since \(v_1(0)=1\),

\[
\|J(s)\|\geq|J(s)e_1|=|\eta(\varepsilon s)|
=|v(\varepsilon s)|\geq e^{\varepsilon c_ks}.
\]

This is a lower bound for the full two-dimensional initial-state derivative. It does not omit a coupling term or substitute an instantaneous eigenvalue for the accumulated tangent evolution. Nearby nonlinear trajectories need not remain in the strip: the tangent coefficients are evaluated along the one constructed reference trajectory, and finite-time differentiability was established earlier.

At \(k=1/2\), the constants evaluate exactly to

\[
L_k=-\log3,\quad U_k=0,\quad Y_k=\log3,
\quad d_k=\frac12,
\]

\[
c_k=\min\left\{\frac14\frac34,\frac12\frac12\right\}
=\frac3{16}.
\]

Thus

\[
\varepsilon c_k=\frac3{160},\qquad
T=\sqrt2\,s,\qquad
\|J(s)\|\geq\exp\left(\frac{3s}{160}\right)
=\exp\left(\frac{3T}{160\sqrt2}\right).
\]

The initial point is in fact in \((-\log3,0)\times\{\log3\}\), which implies the weaker closed-set inclusion stated in the candidate. No numerical approximation to that point is necessary for the proof.

The sharper asymptotic lower rate is also justified. The same differential inequality gives

\[
v_1(\tau)\geq\exp\left(\int_0^\tau f'(x(r))\,dr\right).
\]

Because \(f'(x(r))\to k(1-k)\), its time average converges to that value. Returning to \(s\) yields

\[
\liminf_{s\to\infty}\frac{\log\|J(s)\|}{s}
\geq\varepsilon k(1-k).
\]

This last statement is a lower bound, not an assertion that the exact growth exponent has been identified. The candidate makes that distinction correctly.

## 8. Pointwise, polynomial, and subexponential quantifiers

**Candidate lines 19–37 and 386–410: the principal claims are valid.** The proved counterexample has the quantifier order

\[
\forall k\in(0,1)\quad
\exists z_k=(\alpha_k,Y_k)\in\mathbb R^2\quad
\forall s\geq0:\quad
\|J_{\rho=-k,q=(1,1)}(s;z_k)\|
\geq e^{\varepsilon c_ks}.
\]

The initial point precedes, and is independent of, the observation time. For this fixed control, \(T=\sqrt2s\) and the positive rate in \(T\) is \(\beta_k=\varepsilon c_k/\sqrt2\).

If a bound at this point had the form \(K B(T)\), with \(0<K<\infty\) fixed and

\[
B(T)>0,
\qquad \limsup_{T\to\infty}\frac{\log B(T)}{T}\leq0,
\]

the lower bound would force

\[
\beta_k\leq\frac{\log K}{T}+\frac{\log B(T)}{T}
\]

for every positive \(T\). Taking the upper limit is a contradiction. Every finite polynomial power is covered because \(N\log(1+T)/T\to0\). Dependence of \(K\), \(N\), or a pointwise subexponential envelope on the fixed \(z_k\), \(\rho\), and even the fixed \(q\), does not remove this contradiction.

The opening negative conclusion concerns a universal bound covering all initial states and the adverse sign configuration. It does not assert failure for every correlation, every positive control ratio, or every initial state. Indeed, for each fixed \(\rho\geq0\), the other table rows provide bounds for all control-sign configurations. This is consistent with the explicitly negative-correlation counterexample.

The scaling identity is exact: if \(\Phi_q(s,z)\) denotes the flow, then for \(\lambda>0\),

\[
\Phi_{\lambda q}(s,z)=\Phi_q(\lambda s,z),
\qquad
D_z\Phi_{\lambda q}(s,z)=D_z\Phi_q(\lambda s,z).
\]

For every fixed positive elapsed time \(s_*\), the same initial point therefore satisfies

\[
\|J_{\lambda(1,1)}(s_*;z_k)\|
\geq e^{\varepsilon c_k\lambda s_*},
\qquad T_\lambda=\sqrt2\lambda s_*.
\]

This disproves an amplitude-uniform subexponential bound at fixed positive time. There is one optional wording clarification: the neighboring sentence allowing a prefactor to depend on a fixed control should not be carried over to permit arbitrary dependence on the varying amplitude \(\lambda\) in this last argument. An unrestricted \(K(\lambda q)\) could itself grow exponentially in \(\lambda\), so amplitude variation alone would then give no contradiction. The original large-time argument with a fixed control still does. Read with the displayed original prefactor \(K(z_0,\rho)\), the candidate's scaling conclusion is correct.

Finally, a derivative lower bound at a single state does not supply a lower bound on a set of positive measure, nor a Gaussian integral lower bound with the claimed growth. The candidate explicitly excludes those conclusions. There is also no supplied relation identifying these externally fixed controls with controls generated by training; no such identification is accepted or needed here.

## 9. Invariant appendix, including \(\rho=0\)

**Candidate lines 412–488: valid.** For \(q=(1,-1)\), \(0\leq\rho<1\), define

\[
u=\frac{z_1+z_2}{2},\qquad
v=\frac{z_1-z_2}{2},\qquad
\gamma=\frac{1+\rho}{1-\rho}\geq1.
\]

Adding and subtracting the original rescaled equations gives exactly

\[
\dot u=\frac{1+\rho}{2}[f(u+v)-f(u-v)],
\qquad
\dot v=\frac{1-\rho}{2}[f(u+v)+f(u-v)]>0.
\]

The common denominator of the logistic functions is

\[
(1+e^{u+v})(1+e^{u-v})
=2e^u(\cosh u+\cosh v).
\]

Their difference has numerator \(2e^u\sinh v\), and their sum has numerator \(2e^u\cosh v+2e^{2u}\). Thus both hyperbolic identities in the candidate are correct, including their factors, and

\[
\frac{du}{dv}=\gamma\frac{\sinh v}{\cosh v+e^u}.
\]

The division uses a strictly positive quantity and does not exclude \(v=0\).

For \(\gamma>1\), direct differentiation of

\[
\mathcal I_\gamma=e^{-u/\gamma}\cosh v
-\frac{e^{(\gamma-1)u/\gamma}}{\gamma-1}
\]

gives

\[
(\mathcal I_\gamma)_u
=-\frac1\gamma e^{-u/\gamma}(\cosh v+e^u),
\qquad
(\mathcal I_\gamma)_v=e^{-u/\gamma}\sinh v.
\]

Their combination \((\mathcal I_\gamma)_u\,du/dv+(\mathcal I_\gamma)_v\) vanishes identically. This proves exact conservation along the state-space trajectory.

For each fixed finite \(v\), the derivative in \(u\) is strictly negative. As \(u\to-\infty\), the first term in \(\mathcal I_\gamma\) tends to \(+\infty\) and the second tends to zero; as \(u\to+\infty\), the first tends to zero and the second to \(-\infty\). Hence it is a continuous bijection from \(\mathbb R\) to \(\mathbb R\), with a unique inverse \(u=U(I,v)\). The nonvanishing derivative gives

\[
U_I=-\frac{\gamma e^{u/\gamma}}{\cosh v+e^u},
\qquad
U_v=\gamma\frac{\sinh v}{\cosh v+e^u}.
\]

The asserted \(|U_v|\leq\gamma\) follows from \(|\sinh v|\leq\cosh v\).

To check the less immediate constant in \(|U_I|\), put \(c=\cosh v\geq1\), \(t=e^u>0\). Then

\[
\frac{d}{dt}\left(\frac{\gamma t^{1/\gamma}}{c+t}\right)
=\frac{t^{1/\gamma-1}[c-(\gamma-1)t]}{(c+t)^2}.
\]

For \(\gamma>1\), the expression being maximized tends to zero at both ends of \((0,\infty)\); its unique maximum is at \(t=c/(\gamma-1)\), with value

\[
\left(\frac{\gamma-1}{c}\right)^{(\gamma-1)/\gamma}.
\]

Since \(c\geq1\), this proves exactly

\[
|U_I|\leq
\left(\frac{\gamma-1}{\cosh v}\right)^{(\gamma-1)/\gamma}
\leq(\gamma-1)^{(\gamma-1)/\gamma}.
\]

At \(\gamma=1\), the separate formula \(\mathcal I_1=e^{-u}\cosh v-u\) is necessary to avoid the singular expression above and is correctly supplied. Its derivatives are

\[
(\mathcal I_1)_u=-e^{-u}\cosh v-1,
\qquad (\mathcal I_1)_v=e^{-u}\sinh v.
\]

They give the same conservation identity, strict monotonicity in \(u\), and limits \(+\infty\) and \(-\infty\). Its inverse satisfies

\[
|U_I|=\frac1{e^{-u}\cosh v+1}\leq1,
\qquad
|U_v|=\frac{|\sinh v|}{\cosh v+e^u}\leq1.
\]

The relation between parameters is

\[
\frac{\gamma-1}{2}=\frac{\rho}{1-\rho},
\]

so the appendix quotes the correct exponent from the mixed-sign tangent bound. Bounds on these invariant-coordinate derivatives alone would not control the initial-state derivative at fixed elapsed time, because \(v\) also evolves. The candidate explicitly acknowledges this and uses the independently proved full tangent estimate for that purpose. No additional fixed-time sensitivity conclusion is smuggled in through the invariant.

## 10. Required and optional fixes; precise accepted scope

**Required fixes: none.** Every substantive mathematical claim requested for this audit is supported within the candidate. In particular, the mixed-sign estimate includes the zero-tail configuration, the shooting limit gives a time-independent initial point with a uniqueness proof, and the exponential estimate applies to the full Jacobian.

**Optional clarification O1 — lines 395–398:** specify positive elapsed time and amplitude-uniform constants in the amplitude-scaling sentence. A precise replacement for that sentence would be:

> For every fixed elapsed time \(s_*>0\), scaling to \(q=\lambda(1,1)\) gives the same exponential lower bound as \(\lambda\to\infty\), and therefore also rules out a subexponential bound in \(T\) whose prefactor and growth envelope are uniform in \(\lambda\).

This clarification separates the valid fixed-control, large-time conclusion, which tolerates arbitrary finite dependence of the prefactor on that fixed control, from the amplitude-uniform version. It does not repair a defect in the principal theorem.

The accepted conclusion is an existential deterministic counterexample for every fixed \(\rho\in(-1,0)\), together with the stated uniform-in-control upper bounds in the other sign configurations and the independently verified balanced-control invariant. The explicit prefactors and exponents are valid bounds; their optimality is not asserted. There is no conclusion here about failure at almost every initial point, positive-measure instability, Gaussian-averaged failure, actual training, or nonconstant controls. The review does not recommend promoting this result beyond that scope.
