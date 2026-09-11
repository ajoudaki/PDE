##### C.4.7.6. Nonlinear variation and the finite nonlinear limit

Continue with the strong raw flows, common Gaussian carrier, neighborhood,
and finite-GF capture constructed above, on \(T=40\). All field, action,
raw-norm and data-space notation is unchanged. Law integrals written in
\((u,y)\) use the pushforward under \(u=x/\sqrt2\). Put \(D_Y=2+2Y\),
an upper bound for the diameter of \(\mathcal Z\) in its stated metric.

Write \(\theta_*=\theta_{\nu_*}\). Its identification with the reference
of C.4.6 follows from the strong equation, common initialization and
reached-state uniqueness already proved. For every \(\nu\in\mathcal P(\mathcal Z)\),
put \(\sigma=\nu-\nu_*\) and

\[
 \mu_{\epsilon,\nu}=(1-\epsilon)\nu_*+\epsilon\nu,
 \qquad
 \epsilon_Y=\min\{1/2,\delta_Y/(2D_Y)\}>0.
 \tag{NV-radius}
\]

The radius \(\delta_Y\) is chosen below inside the neighborhood on which
the preceding construction has uniform constants. Coupling unchanged
mass to itself gives
\(\mathcal W_1(\mu_{\epsilon,\nu},\nu_*)\le\epsilon D_Y\le\delta_Y/2\).
Thus every \(\nu\), including every nonatomic law, and the whole closed
interval \(0\le\epsilon\le\epsilon_Y\) are admitted.

The conclusions proved here are

\[
 \sup_{\nu\in\mathcal P(\mathcal Z)}\sup_{0\le t\le T}
 \|\theta_{\mu_{\epsilon,\nu}}(t)-\theta_*(t)
                  -\epsilon\dot\theta_\sigma(t)\|_{\rm raw}
       =o(\epsilon),
 \tag{NV-raw-remainder}
\]

\[
 \sup_{\nu\in\mathcal P(\mathcal Z)}
 \sup_{\substack{0\le t\le T\\x\in\sqrt2S^1}}
 |f_{\mu_{\epsilon,\nu}}(t,x)-f_{\nu_*}(t,x)
                   -\epsilon\mathscr D_\sigma f(t,x)|
       \le\epsilon\omega_Y(\epsilon),
 \qquad \omega_Y(\epsilon)\longrightarrow0,
 \tag{NV-prediction-remainder}
\]

where \(\dot\theta_\sigma\) and \(\mathscr D_\sigma f\) are exactly the
raw variation and prediction response of C.4.6. The modulus is deterministic
and independent of \(\nu\). The proof first turns active query tails into
passive tails using a small probe atom. Radial saturation then controls
the unbounded clock weights on the actual paths. The resulting forcing
continuity and compact response family justify Taylor expansion along
those response directions and a comparison with the nonlinear flow.

###### 1. Probe atoms and passive exponential tails

Write \(U_r=\{\mu:\mathcal W_1(\mu,\nu_*)<r\}\). Choose fixed
\(0<r_0<r_1<\rho\), where \(\rho>0\) is the radius of the preceding
source construction, and ultimately take \(\delta_Y\le r_0\).
The already proved active-tail estimate (NH) supplies \(a,M,h_1>0\) such
that every finite law \(\lambda\in U_{r_1}\), every finite raw Euler
mesh of maximal step at most \(h_1\) through \(T\), and every node \(k\)
obey

\[
 \int \tau_R(Q_{\lambda,k}(u))\,d\lambda(u,y)
       \le M e^{-aR},\qquad
 \tau_R(P):=\|P\mathbf1_{|P|>R}\|_{H_1},\qquad R\ge1.
 \tag{NV-active-tail}
\]

The readout and raw state bounds (NE), and the same-mesh law estimate
(NLM), are uniform on this ball. In particular there are \(C_0,q_0>0\)
and \(\alpha>0\), independent of the mesh, such that

\[
 \max_k\|\theta_{\lambda,k}-\theta_{\kappa,k}\|_{\rm raw}
       \le C_0\mathcal W_1(\lambda,\kappa)^\alpha,
 \qquad \mathcal W_1(\lambda,\kappa)\le q_0.
 \tag{NV-same-mesh}
\]

There is no additive mesh error in this estimate: both recursions use
the identical mesh. This permits probe masses tending to zero at a
fixed mesh.

For completeness, \(Q(u)\) is Lipschitz in raw state on these bounded
sets with their common readout supremum bound. At the same input, factor
subtraction gives

\[
 \begin{aligned}
 \|Z^{(2)}-\bar Z^{(2)}\|_2
 &\le\|K-\bar K\|_{\rm HS}
             +\|\bar A\|\|w-\bar w\|_2,\\
 \|\Delta^{(2)}-\bar\Delta^{(2)}\|_2
 &\le\|c-\bar c\|_2
             +2\|\bar c\|_\infty\|Z^{(2)}-\bar Z^{(2)}\|_2,\\
 \|Q-\bar Q\|_2
 &\le\|K-\bar K\|_{\rm HS}\|\Delta^{(2)}\|_2
             +\|\bar A\|\|\Delta^{(2)}-\bar\Delta^{(2)}\|_2.
 \end{aligned}
 \tag{NV-query-comparison}
\]

Fix \(\lambda\in U_{r_0}\) with finite support and any passive
\(u\in S^1\). The label zero is allowed. Define

\[
 \lambda_\eta=(1-\eta)\lambda+\eta\delta_{(\sqrt2u,0)},
 \qquad
 0<\bar\eta<\min\{1,(r_1-r_0)/D_Y,q_0/D_Y\}.
 \tag{NV-probe-law}
\]

For \(0<\eta\le\bar\eta\), the direct mixture coupling gives
\(\mathcal W_1(\lambda,\lambda_\eta)\le D_Y\eta\), so both laws
are in \(U_{r_1}\). On their common mesh, (NV-same-mesh) and
(NV-query-comparison) give
\(\|Q_{\lambda,k}(u)-Q_{\lambda_\eta,k}(u)\|_2\le C_1\eta^\alpha\).
The selected atom has mass at least \(\eta\), even if it coincides with
an old atom. Hence (NV-active-tail), for \(R\ge2\), gives

\[
 \tau_{R/2}(Q_{\lambda_\eta,k}(u))
       \le\eta^{-1}M e^{-aR/2}.
\]

The pointwise alternatives \( |P'|\le R/2\) and \( |P'|>R/2\)
on \( |P|>R\) imply
\(\tau_R(P)\le2\|P-P'\|_2+2\tau_{R/2}(P')\). Therefore

\[
 \tau_R(Q_{\lambda,k}(u))
       \le2C_1\eta^\alpha+2\eta^{-1}M e^{-aR/2}.
 \tag{NV-probe-tail}
\]

Choose \(\eta=\bar\eta\exp\{-aR/[2(1+\alpha)]\}\) and set
\(b=a\alpha/[2(1+\alpha)]>0\). Both terms have the same exponential
decay, so a fixed \(C_2<\infty\) satisfies

\[
 \sup_{\substack{\lambda\in U_{r_0}\text{ finite}\\
                  \text{admitted meshes},\ k,\ u\in S^1}}
 \tau_R(Q_{\lambda,k}(u))\le C_2e^{-bR},\qquad R\ge2.
 \tag{NV-passive-tail}
\]

There was no division by any preexisting atom weight. The only inverse
mass in (NV-probe-tail) is paid for by the quantitative change of law.

The bound \(\Pr(|Q|>R)\le R^{-2}\tau_R(Q)^2\) and the identity

\[
 \mathbb E e^{\beta|Q|}
       =1+\int_0^\infty\beta e^{\beta R}\Pr(|Q|>R)\,dR
\]

show that \(\beta=b\) gives a common finite exponential moment:
the portion \(0\le R\le2\) is bounded directly, and the remaining
integrand is bounded by a constant times \(e^{-bR}\).
For each \(\mu\in U_{r_0}\), take its finite-law, fine-mesh strong
approximations within \(U_{r_0}\). The readout supremum bound passes
to their strong \(L^2\) limit by an almost surely convergent subsequence.
Equation (NV-query-comparison) then passes each passive query to that
limit in \(L^2\). At any deterministic time use preceding mesh nodes;
the vanishing state interpolation error has the same conclusion.
For each fixed time and input, apply convergence in probability to
\(\min(N,e^{\beta|Q|})\), take expectations using boundedness, then
let \(N\to\infty\). The constants are unchanged for all parameters:

\[
 \sup_{\mu\in U_{r_0},\,0\le t\le T,\,u\in S^1}
           \mathbb E_1 e^{\beta|Q_\mu(t,u)|}\le M_Q<\infty.
 \tag{NV-passive-moment}
\]

This is uniformity of individual query marginals. A coordinate
supremum over time and inputs has not been placed inside this moment.

###### 2. Radial saturation and the actual inverse-gate forcing

The strong raw path has square-integrable velocity in time, so Fubini
gives almost surely absolutely continuous row representatives. Since
\(\cosh^2 z=1+\sinh^2z\ge1+z^2\ge2|z|\),
\(|z|\phi'(z)\le1/2\). The exact row equation consequently gives,
for almost every coordinate and time,

\[
 \frac d{dt}|w_\mu(t)|^2
 =-4\int r_\mu(t,u,y)Q_\mu(t,u)
       (w_\mu(t)\cdot u)\phi'(w_\mu(t)\cdot u)\,d\mu
 \le2\int |r_\mu(t,u,y)|\,|Q_\mu(t,u)|\,d\mu.
 \tag{NV-radial}
\]

The preceding energy identity and \(c(0)=0\) give
\(\|c_\mu(t)\|_2\le Y\sqrt T\), so
\(|r_\mu(t,u,y)|\le R_T:=Y(1+\sqrt T)\). Define

\[
 J_\mu=\int_0^T\int|Q_\mu(s,u)|\,d\mu(u,y)\,ds,
 \qquad W_\mu=\sup_{0\le t\le T}|w_\mu(t)|.
\]

The jointly measurable representatives needed here follow from the
strongly continuous query map and its separable \(L^2\) range; finite
simple approximations give representatives on the product of parameter
space and \(\Omega_1\). Equation (NV-passive-moment) and Fubini give
\(J_\mu<\infty\) almost surely. Integrating (NV-radial) yields

\[
 W_\mu^2\le|g|^2+2R_TJ_\mu.
 \tag{NV-row-envelope}
\]

For \(0\le\lambda T\le\beta\), Jensen's inequality for the probability
measure \(T^{-1}\,ds\,d\mu\), followed by (NV-passive-moment), gives

\[
 \mathbb E_1e^{\lambda J_\mu}
 \le\frac1T\int_0^T\int
        \mathbb E_1e^{\lambda T|Q_\mu(s,u)|}\,d\mu\,ds
 \le M_Q.
 \tag{NV-integrated-query}
\]

Choose \(0<\gamma\le\min\{1/8,\beta/(8R_TT)\}\). Cauchy–Schwarz,
(NV-row-envelope), and (NV-integrated-query) imply

\[
 \sup_{\mu\in U_{r_0}}\mathbb E_1e^{\gamma W_\mu^2}
 \le(\mathbb E_1e^{2\gamma|g|^2})^{1/2}
      (\mathbb E_1e^{4\gamma R_TJ_\mu})^{1/2}
 \le(1-4\gamma)^{-1/2}M_Q^{1/2}=:M_W<\infty.
 \tag{NV-row-square-moment}
\]

Indeed the two independent standard Gaussian root coordinates give
\(\mathbb E e^{2\gamma|g|^2}=(1-4\gamma)^{-1}\), by combining their
normal densities with the exponential. No independence between \(g\)
and the evolved queries was used.

For every separately fixed positive integer \(p\), the exponential
series in (NV-passive-moment) gives
\(\mathbb E_1|Q_\mu(t,u)|^{2p}\le M_Q(2p)!/\beta^{2p}\).
Since \(\cosh^2(w_j)\le e^{2W_\mu}\) and
\(4pW_\mu\le\gamma W_\mu^2+4p^2/\gamma\), Cauchy–Schwarz gives

\[
 \sup_{\mu\in U_{r_0},\,t\le T,\,u\in S^1,\,j=1,2}
 \mathbb E_1\{\cosh^2(w_{\mu,j}(t))|Q_\mu(t,u)|\}^{p}
 \le e^{2p^2/\gamma}M_W^{1/2}
             \{M_Q(2p)!/\beta^{2p}\}^{1/2}<\infty.
 \tag{NV-weighted-moments}
\]

Define the actual inverse-gate forcing field on \(\Omega_1\) by

\[
 \mathcal I_{\mu,j}(t,u)=
 u_j\cosh^2(w_{\mu,j}(t))\phi'(w_\mu(t)\cdot u)Q_\mu(t,u).
 \tag{NV-clock-force}
\]

The factor \(u_j\) retains the zero contribution at the other reference
axis. Taking \(p=3\) in (NV-weighted-moments) proves a common bound
\(\mathbb E_1|\mathcal I_{\mu,j}(t,u)|^3\le C_3\), hence

\[
 \sup_{\mu\in U_{r_0},\,t\le T,\,u\in S^1,\,j=1,2}
 \mathbb E_1\bigl[|\mathcal I_{\mu,j}(t,u)|^2
                   \mathbf1_{|\mathcal I_{\mu,j}(t,u)|>R}\bigr]
       \le C_3/R\longrightarrow0.
 \tag{NV-forcing-UI}
\]

These estimates concern the actual reached family. They assert no
\(L^p\)-bounded action of \(A_0\) or \(A_0^*\) beyond their given
\(L^2\) actions.

###### 3. The exact clock equation

Set

\[
 F(z)=z/2+\sinh(2z)/4,\qquad \psi=F^{-1},\qquad
 F'(z)=\cosh^2z=1/\phi'(z),\qquad
 \psi'(X)=\phi'(\psi(X)).
 \tag{NV-clock}
\]

The positive derivative and limits at infinity make \(F\) a bijection;
\(\psi\) is 1-Lipschitz, with bounded Lipschitz derivative because
\(\psi''=(\phi''\circ\psi)(\phi'\circ\psi)\) is bounded. Write

\[
 \Theta_\mu=(X_\mu,K_\mu,c_\mu),\qquad
 X_{\mu,j}=F(w_{\mu,j}),\qquad
 \mathcal V=L^2(\Omega_1;\mathbb R^2)
             \oplus\mathcal S_2(H_1,H_2)\oplus H_2,
\]

with its square-sum Hilbert norm. The initial clock is \(F(g_j)\in L^2\):
\(|F(g_j)|\le |g_j|/2+e^{2|g_j|}/4\), and
\(\mathbb E e^{a|g_j|}\le2e^{a^2/2}\) for every finite \(a\ge0\).

The clock is justified without assuming an unbounded coordinate map
preserves all of \(L^2\). Apply the scalar chain rule to the almost
surely absolutely continuous raw row. Its transformed derivative is
\(-2\int r_\mu\mathcal I_{\mu,j}\,d\mu\). The residual bound and
(NV-forcing-UI) make this an integrable \(H_1\)-valued velocity on
\([0,T]\). Fubini and the scalar integral identity therefore identify
\(X_{\mu,j}\) with an absolutely continuous \(H_1\) curve starting at
\(F(g_j)\).

At a clock state \(\Theta=(X,K,c)\), recover \(w_j=\psi(X_j)\) and
the forward and backward fields defined above. For the reference axes put \(r_j=f(e_j)-y_j\),
\(y_1=1,y_2=-1\), and define

\[
 \begin{aligned}
 (\mathcal F_0(\Theta))_{X,j}&=-r_jQ(e_j),\\
 (\mathcal F_0(\Theta))_K
    &=-\sum_{j=1}^2r_j\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j),\\
 (\mathcal F_0(\Theta))_c&=-\sum_{j=1}^2r_jH^{(2)}(e_j).
 \end{aligned}
 \tag{NV-reference-field}
\]

Here \(F'(w_j)\phi'(w_j)=1\) cancels the first gate exactly, and the
two atom masses cancel the loss factor two. For an arbitrary probability
law \(\nu\), define on every reached state

\[
 \mathcal Q_\nu(\Theta)=-2\int r(u,y)
 \left((\mathcal I_j(\Theta,u))_{j=1,2},
       \Delta^{(2)}(u)\otimes H^{(1)}(u),H^{(2)}(u)\right)d\nu(u,y),
 \qquad \mathcal B_\nu=\mathcal Q_\nu-\mathcal F_0.
 \tag{NV-law-field}
\]

For reached states all these Bochner integrals exist: the integrands
have separable measurable ranges. For the first component, truncate its
continuous coordinate formula at a fixed level. The resulting bounded
coordinate map is strongly measurable; (NV-forcing-UI) makes these
truncations converge in \(L^2\), uniformly in the input. Their limit is
therefore strongly measurable and has a uniform \(L^2\) bound. The other
components are strongly continuous in the input and obey the raw bounds.
Integration against a probability law is consequently legitimate.
The exact contamination equation is

\[
 \Theta_{\epsilon,\nu}'=
 \mathcal F_0(\Theta_{\epsilon,\nu})
       +\epsilon\mathcal B_\nu(\Theta_{\epsilon,\nu}),
 \qquad \Theta_{\epsilon,\nu}(0)=\Theta_*(0).
 \tag{NV-exact-equation}
\]

The field \(\mathcal F_0\) is defined on all of \(\mathcal V\).
The contaminated field in (NV-law-field) is used only where its
weighted integrals have just been proved to exist.

###### 4. Reference comparison with one bounded readout endpoint

On sets with bounded \(\|K\|_{\rm HS}\) and \(\|c\|_2\), if at
least one of two compared readouts has a fixed \(L^\infty\) bound, then

\[
 \|\mathcal F_0(\Theta)-\mathcal F_0(\widetilde\Theta)\|_{\mathcal V}
       \le L\|\Theta-\widetilde\Theta\|_{\mathcal V}.
 \tag{NV-reference-Lipschitz}
\]

To verify this, let \(M_A\) bound the two action norms and \(M_c\)
bound the \(L^2\) readout norms, and suppose \(\|c\|_\infty\le H_c\).
Uniformly over \(u\in S^1\),

\[
 \|H^{(1)}-\widetilde H^{(1)}\|_2\le\|X-\widetilde X\|_2,
 \quad
 \|Z^{(2)}-\widetilde Z^{(2)}\|_2
       \le M_A\|X-\widetilde X\|_2+\|K-\widetilde K\|_{\rm HS}.
\]

Use the bounded endpoint in the precise factorization

\[
 c\phi'(Z^{(2)})-\widetilde c\phi'(\widetilde Z^{(2)})
 =(c-\widetilde c)\phi'(\widetilde Z^{(2)})
       +c\{\phi'(Z^{(2)})-\phi'(\widetilde Z^{(2)})\}.
\]

Its norm is at most
\(\|c-\widetilde c\|_2+2H_c\|Z^{(2)}-\widetilde Z^{(2)}\|_2\).
The prediction difference is at most
\(\|c-\widetilde c\|_2+M_c\|Z^{(2)}-\widetilde Z^{(2)}\|_2\).
Actual adjunction then bounds

\[
 \|Q-\widetilde Q\|_2
 \le M_A\|\Delta^{(2)}-\widetilde\Delta^{(2)}\|_2
             +M_c\|K-\widetilde K\|_{\rm HS}.
\]

Substitution into (NV-reference-field), and
\(\|a\otimes b-\tilde a\otimes\tilde b\|_{\rm HS}
\le\|a-\tilde a\|_2\|b\|_2+\|\tilde a\|_2\|b-\tilde b\|_2\),
prove (NV-reference-Lipschitz). Its row component contains no product
of an arbitrary clock difference with an unbounded backward query.

The actual readouts obey \(\|c_\mu(t)\|_\infty\le2YT\), and
(NV-forcing-UI) bounds \(\mathcal B_\nu(\Theta_{\epsilon,\nu})\)
uniformly in \(\nu,\epsilon,t\). Subtract (NV-exact-equation) from
the reference equation. Iterating the scalar integral inequality
\(v(t)\le a+L\int_0^tv(s)ds\) gives \(v(t)\le ae^{Lt}\), so

\[
 \sup_{\nu\in\mathcal P(\mathcal Z),\,t\le T}
       \|\Theta_{\epsilon,\nu}(t)-\Theta_*(t)\|_{\mathcal V}
       \le C_T\epsilon.
 \tag{NV-clock-first-order}
\]

This first-order displacement bound is a consequence of the reached
forcing estimates.

###### 5. Continuity of the forcing along the actual paths

We claim

\[
 \sup_{\nu,\,t\le T,\,u\in S^1,\,j=1,2}
 \|\mathcal I_j(\Theta_{\epsilon,\nu}(t),u)
             -\mathcal I_j(\Theta_*(t),u)\|_2\longrightarrow0.
 \tag{NV-force-continuity}
\]

If it failed, choose \(\epsilon_m\downarrow0\), laws \(\nu_m\),
times \(t_m\), and inputs \(u_m\) along which the difference is bounded
away from zero. Pass to a subsequence with \(t_m\to t\), \(u_m\to u\)
and a fixed index \(j\). By (NV-clock-first-order) and reference
continuity, \(\Theta_{\epsilon_m,\nu_m}(t_m)\to\Theta_*(t)\)
strongly in \(\mathcal V\). The lower features converge in \(L^2\),
using \(\psi\)'s Lipschitz bound and
\(\|(u_m-u)\cdot w_*(t)\|_2\le|u_m-u|\|w_*(t)\|_2\).
The action and upper features then converge. The bounded readout
factorization in the preceding subsection gives convergence of
\(\Delta^{(2)}\) and \(Q\) in \(L^2\).

The continuous finite-dimensional function
\(u_j\cosh^2(w_j)\phi'(w\cdot u)\) converges in measure under this
convergence of its arguments. Its product with the convergent query
therefore converges in measure to the limiting \(\mathcal I_j\).
Equation (NV-forcing-UI) upgrades this to \(L^2\) convergence.
Explicitly, uniformly integrable squares make the integral of the
squared difference on any set of sufficiently small probability
uniformly small; on the complement of the event that its magnitude
exceeds \(\eta\), its squared integral is at most \(\eta^2\).
Convergence in measure and then \(\eta\downarrow0\) prove the claim.
The same argument applies to the reference sequence \((t_m,u_m)\);
the triangle inequality contradicts the assumed failure.

Residual differences tend to zero uniformly by
(NV-clock-first-order), while their absolute values and all weighted
force norms are uniformly bounded. The remaining components of
(NV-law-field) have the ordinary Lipschitz differences already proved.
Integration against any probability law is bounded by the supremum
of the integrand norm. Thus

\[
 \sup_{\nu,\,t\le T}
 \|\mathcal B_\nu(\Theta_{\epsilon,\nu}(t))
             -\mathcal B_\nu(\Theta_*(t))\|_{\mathcal V}
       \longrightarrow0.
 \tag{NV-source-defect}
\]

With \(\epsilon=0\), the same argument proves joint strong continuity
of the atom forcing in time, input and label. In particular all
reference law integrals below are continuous in time.

###### 6. The linear equation and its compact family of directions

At a reference clock state and for \(v=(\xi,B,d)\in\mathcal V\), define
the following directional fields; the prefix \(\eta\) denotes a
directional variation, not a time derivative:

\[
 \begin{aligned}
 \eta w_j&=\phi'(w_j)\xi_j,&
 \eta H^{(1)}(u)&=\phi'(w\cdot u)\sum_j u_j\eta w_j,\\
 \eta Z^{(2)}(u)&=A\eta H^{(1)}(u)+BH^{(1)}(u),&
 \eta H^{(2)}(u)&=\phi'(Z^{(2)}(u))\eta Z^{(2)}(u),\\
 \eta f(u)&=\langle d,H^{(2)}(u)\rangle
                      +\langle c,\eta H^{(2)}(u)\rangle,\\
 \eta\Delta^{(2)}(u)&=d\phi'(Z^{(2)}(u))
                  +c\phi''(Z^{(2)}(u))\eta Z^{(2)}(u),\\
 \eta Q(u)&=A^*\eta\Delta^{(2)}(u)+B^*\Delta^{(2)}(u).
 \end{aligned}
 \tag{NV-directional-fields}
\]

The bounded linear generator on \(\mathcal V\) is

\[
 \begin{aligned}
 (\mathcal L(t)v)_{X,j}
   &=-(\eta f(e_j))Q(e_j)-r_j\eta Q(e_j),\\
 (\mathcal L(t)v)_K
   &=-\sum_j\bigl[(\eta f(e_j))\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j)
          +r_j\eta\Delta^{(2)}(e_j)\otimes H^{(1)}(e_j)
          +r_j\Delta^{(2)}(e_j)\otimes\eta H^{(1)}(e_j)\bigr],\\
 (\mathcal L(t)v)_c
   &=-\sum_j\bigl[(\eta f(e_j))H^{(2)}(e_j)+r_j\eta H^{(2)}(e_j)\bigr].
 \end{aligned}
 \tag{NV-generator}
\]

Every map is bounded uniformly in \(t\le T\): the only coefficient
multiplying an unrestricted upper preactivation variation is
\(c\phi''(Z^{(2)})\in L^\infty\). The remaining products are bounded
multipliers, Hilbert scalar pairings, or Hilbert–Schmidt ranks.
In particular no \(Q(e_j)\xi_j\) pointwise product occurs.

The family \(\mathcal L(t)\) is strongly continuous. To justify its
multiplier steps, if uniformly bounded functions converge in measure,
their product with a fixed \(L^2\) field converges in \(L^2\): truncate
the fixed field, use bounded convergence in measure on its bounded
part, and then remove its square-integrable tail. The reference fields
are strongly continuous, their action increments are HS-continuous,
and their readout factors are uniformly bounded. Applying this
observation successively in (NV-directional-fields) and
(NV-generator) proves the assertion for each fixed \(v\).

For clarity, a uniformly bounded strongly continuous generator has a
unique strong propagator \(U(t,s)\) on this finite interval. Starting
from \(v\), iterated integrals of the generator have norms at most
\(\|v\|L_*^k(t-s)^k/k!\), where \(L_*=\sup_t\|\mathcal L(t)\|\).
Their uniformly convergent series solves the integral equation and
has norm at most \(e^{L_*(t-s)}\|v\|\). Iterating the difference
equation proves uniqueness with the same factorial bound.
Consequently the solution of

\[
 v_\sigma'=\mathcal L(t)v_\sigma+b_\sigma(t),\qquad
 b_\sigma(t)=\mathcal B_\nu(\Theta_*(t)),\qquad v_\sigma(0)=0
 \tag{NV-response-equation}
\]

is \(v_\sigma(t)=\int_0^tU(t,s)b_\sigma(s)ds\), and the map from
continuous forcing to \(C([0,T];\mathcal V)\) is bounded and linear,
with norm at most \(Te^{L_*T}\). Substitution into the integral equation
is justified by this integrable bound. The forcing is continuous, so
the response is strongly \(C^1\).

The atom map

\[
 z=(x,y)\longmapsto
 \bigl[t\longmapsto
   \mathcal Q_{\delta_z}(\Theta_*(t))-\mathcal F_0(\Theta_*(t))\bigr]
       \quad\hbox{in }C([0,T];\mathcal V)
 \tag{NV-atom-curves}
\]

is continuous on compact \(\mathcal Z\), by the joint continuity proved above.
Its image is compact. Each \(b_{\nu-\nu_*}\) is a Bochner average of
this image and belongs to its closed convex hull. That hull is compact:
cover the image by finitely many balls of radius \(h\); every convex
combination is within \(h\) of the convex hull of their centers. The
latter hull is the continuous image of a finite-dimensional compact
simplex. This gives total boundedness for each \(h>0\), and closure
in the complete curve space gives compactness.

The bounded linear solution map in (NV-response-equation) therefore gives

\[
 \{v_{\nu-\nu_*}:\nu\in\mathcal P(\mathcal Z)\}
       \text{ has compact closure in }C([0,T];\mathcal V),
 \quad
 \mathcal C:=\overline{\{v_{\nu-\nu_*}(t):\nu\in\mathcal P(\mathcal Z),\ t\le T\}}
       \text{ is compact in }\mathcal V.
 \tag{NV-compact-directions}
\]

The second statement uses continuity of evaluation on the product of
the compact closure of the curve family and compact time.

The equation is exactly the C.4.6 equation, rather than a separately
defined response with an unspecified identification. That section
uses \(X_j^{\rm old}=F(w_j)-F(g_j)\); our clock differs by the same
fixed \(L^2\) initial field for every law. Clock differences and tangent
coordinates thus coincide. At the reference axes
(NV-reference-field) is \(X_j'=-r_jQ(e_j)\), and
(NV-directional-fields) agrees term by term with C.4.6.T14. Formula
(NV-generator) is the product differentiation of this field, hence
the operator in C.4.6.T6. Moreover \(\cosh^2(w_j)=1/\phi'(w_j)\), so

\[
 b_\sigma(t)=-2\int r_*(t,u,y)
 \left(
   \left(u_j\frac{\phi'(w_*(t)\cdot u)}{\phi'(w_{*,j}(t))}
                 Q_*(t,u)\right)_{j=1,2},
   \Delta_*^{(2)}(t,u)\otimes H_*^{(1)}(t,u),H_*^{(2)}(t,u)
 \right)d\sigma(u,y),
 \tag{NV-exact-source}
\]

which is C.4.6.T5 including the residual, sign, factor two and reference
subtraction. Uniqueness of the linear equation identifies \(v_\sigma\)
with that section's response. In particular

\[
 \dot\theta_\sigma(t)=
 ((\phi'(w_{*,j}(t))\xi_{\sigma,j}(t))_{j=1,2},B_\sigma(t),d_\sigma(t)),
 \qquad
 \mathscr D_\sigma f(t,\sqrt2u)=\eta f_*(t,u)[v_\sigma(t)].
 \tag{NV-response-identification}
\]

###### 7. Taylor consistency on compact directions

We first prove the needed \(L^2\) fact. Let \(N\) be a scalar or
finite-dimensional function with bounded Lipschitz first derivative,
and let \(v\) range over a relatively compact subset of \(L^2\). Then

\[
 \sup_{a,v}
 \left\|\frac{N(a+\epsilon v)-N(a)}{\epsilon}-DN(a)v\right\|_2
       \longrightarrow0,
 \tag{NV-compact-Taylor}
\]

where bases \(a\) are arbitrary whenever the expressions are defined.
On \( |v|\le R\), the scalar integral remainder is bounded by
\(C\epsilon R|v|\); on \( |v|>R\), it is bounded by \(C|v|\).
Compact \(L^2\) families have uniformly vanishing square tails.
Indeed a finite \(L^2\) net, and
\(\|v\mathbf1_{|v|>2R}\|_2
\le2\|v-v_0\|_2+2\|v_0\mathbf1_{|v_0|>R}\|_2\),
reduce the claim to finitely many square-integrable fields. Choose
\(R\) first and then \(\epsilon\) to prove (NV-compact-Taylor),
uniformly in the bases. The argument works for a family of functions
with a common derivative bound and Lipschitz constant.

Apply it to \(\psi\), to the finite-dimensional map
\(X\mapsto\phi(\sum_j u_j\psi(X_j))\), and to \(\phi\) and
\(\phi'\) at the upper preactivation. Their first derivatives are
bounded and Lipschitz uniformly over \(u\in S^1\); for the second
map use \( |u|=1\), bounded \(\psi',\psi''\), and bounded
\(\phi',\phi''\). The needed further derivatives of tanh are bounded.

At compact reference times and for \(v\in\mathcal C\), the linear
directions in (NV-directional-fields) form compact \(L^2\) families,
also when \(u\) varies over the circle. To check this, the bounded
multiplier argument from the preceding subsection gives joint strong
continuity in \((t,u)\) on each fixed direction. Uniform operator bounds
and a finite net extend that continuity to compact direction sets.
The action \(A(t)\) is norm-continuous because \(K(t)\) is HS-continuous.
For \(BH^{(1)}(t,u)\), continuity follows from the HS action bound.
Thus every successive linear image is the continuous image of the
relevant compact parameter product.

These facts expand the lower and upper features with precisely the
linear terms in (NV-directional-fields), with \(o(\epsilon)\) errors
uniform in \(t,u,v\in\mathcal C\). Bilinear action terms such as
\(\epsilon B[H^{(1)}_{\rm new}-H^{(1)}_*]\) are \(O(\epsilon^2)\)
in \(L^2\). If the upper preactivation already has an \(o(\epsilon)\)
error after its linear term, the Lipschitz bounds for \(\phi,\phi'\)
pass that error before applying (NV-compact-Taylor).

There is one pointwise product requiring a further check. In the
expansion of \((c_*+\epsilon d)\phi'(Z^{(2)}_{\rm new})\), the cross
term divided by \(\epsilon\) is

\[
 d\{\phi'(Z^{(2)}_{\rm new})-\phi'(Z^{(2)}_*)\}.
 \tag{NV-backward-cross-term}
\]

The bracket is uniformly bounded and has \(L^2\) norm \(O(\epsilon)\).
For any fixed \(R\), its product with \(d\mathbf1_{|d|\le R}\)
therefore tends uniformly to zero in \(L^2\). The complementary norm
is at most \(2\|\phi'\|_\infty\|d\mathbf1_{|d|>R}\|_2\),
uniformly small by compactness of the \(d\) directions. This proves
that (NV-backward-cross-term) is \(o(1)\) in \(L^2\). The other upper
backward Taylor remainder is multiplied by the bounded reference
readout. After actual adjunction, the remaining action cross term is
bounded by \(\epsilon\|B\|_{\rm HS}\) times an \(O(\epsilon)\)
backward difference. Prediction products are scalar pairings and
middle-field products are Hilbert–Schmidt ranks; their cross terms
are \(O(\epsilon^2)\) by Cauchy–Schwarz and the rank norm identity.
Residual differences have the same scalar expansion.

Substitution of these expansions into every component of
(NV-reference-field) proves

\[
 \sup_{t\le T,\,v\in\mathcal C}
 \|\mathcal F_0(\Theta_*(t)+\epsilon v)
       -\mathcal F_0(\Theta_*(t))-\epsilon\mathcal L(t)v\|_{\mathcal V}
       =o(\epsilon).
 \tag{NV-field-Taylor}
\]

The same expansions of \(\psi\) and the scalar predictor prove their
corresponding \(o(\epsilon)\) formulas, including the supremum over
all \(u\in S^1\). These are Taylor estimates on compact directions;
no estimate on an arbitrary bounded \(L^2\) direction ball is claimed.

###### 8. Comparison with the nonlinear path and return to raw state

Let \(\widetilde\Theta_{\epsilon,\nu}=
\Theta_*+\epsilon v_{\nu-\nu_*}\), and define

\[
 \rho_{\epsilon,\nu}(t)=
 \mathcal F_0(\widetilde\Theta_{\epsilon,\nu}(t))
       -\mathcal F_0(\Theta_*(t))-\epsilon\mathcal L(t)v_{\nu-\nu_*}(t).
\]

Equations (NV-compact-directions) and (NV-field-Taylor) give
\(\sup_{\nu,t}\|\rho_{\epsilon,\nu}(t)\|=o(\epsilon)\).
Subtracting the response equation from (NV-exact-equation), with
\(e=\Theta_{\epsilon,\nu}-\widetilde\Theta_{\epsilon,\nu}\), yields

\[
 \begin{aligned}
 e'={}&\mathcal F_0(\Theta_{\epsilon,\nu})
           -\mathcal F_0(\widetilde\Theta_{\epsilon,\nu})\\
 &+\epsilon\{\mathcal B_\nu(\Theta_{\epsilon,\nu})
                  -\mathcal B_\nu(\Theta_*)\}
       +\rho_{\epsilon,\nu},\qquad e(0)=0.
 \end{aligned}
 \tag{NV-error-equation}
\]

Both compared curves have uniformly bounded action and \(L^2\)
readout norms, by the raw estimates and compactness of the response
family. The actual curve has the uniform pointwise readout bound
\(2YT\). Thus (NV-reference-Lipschitz) applies although the response
readout need not be bounded pointwise. Equations (NV-source-defect)
and (NV-error-equation), followed by the scalar integral inequality,
give

\[
 \sup_{\nu,t\le T}
 \|\Theta_{\epsilon,\nu}(t)-\Theta_*(t)
                         -\epsilon v_{\nu-\nu_*}(t)\|_{\mathcal V}
       =o(\epsilon).
 \tag{NV-clock-remainder}
\]

For the raw row, first replace \(X_{\epsilon,\nu}\) by
\(X_*+\epsilon\xi_\sigma\), at an \(o(\epsilon)\) cost because
\(\psi\) is 1-Lipschitz. Then (NV-compact-Taylor) gives

\[
 \psi(X_*+\epsilon\xi_\sigma)-\psi(X_*)
       =\epsilon\phi'(w_*)\xi_\sigma+o(\epsilon)
       \quad\text{in }L^2,
\]

uniformly in \(\nu,t\). The other raw blocks equal their clock-state
blocks, proving (NV-raw-remainder) with (NV-response-identification).
The predictor is uniformly Lipschitz in clock state on these bounded
sets, by the forward and pairing bounds used above. Replace the actual
state by \(\widetilde\Theta_{\epsilon,\nu}\) and apply its uniform
compact-direction Taylor formula. This proves
(NV-prediction-remainder). A deterministic modulus can be obtained by
taking the supremum of the normalized error over \(\nu,t,u\) and
\(0<\epsilon'\le\epsilon\), and defining its value at zero to be zero.
The just-proved uniform small-o makes this supremum finite for small
\(\epsilon\) and tending to zero; uniform state and response bounds
extend it to the rest of \(0<\epsilon\le\epsilon_Y\).

###### 9. Exact bridge to finite GF

For each width retain the actual three initialized Gaussian arrays,
including the small stored readout, and use those same arrays for
every \(\epsilon\). At fixed width the exactly integrated finite loss
has a smooth parameter field, affine in \(\epsilon\). The finite
energy bound keeps all paths \(0\le\epsilon\le1\) in one compact
parameter ball on \([0,T]\), whose radius may depend on that initialized
network. On this ball the mean value formula and the scalar integral
inequality first give \(\|\theta_{n,\epsilon}-\theta_{n,0}\|_{C_t}
\le C_n\epsilon\). Dividing the integral-equation difference by
\(\epsilon\), its mean-value coefficients converge uniformly to the
reference derivative coefficients. A second integral comparison gives
the right derivative \(D_\sigma f_n\), with zero initial variation.
This is the finite derivative constructed in C.4.6.4; no width-uniform
constant is used in its construction.

Fix \(\nu\in\mathcal P(\mathcal Z)\) and \(\epsilon\in(0,\epsilon_Y]\).
Write \(\|\cdot\|_\infty\) for the supremum over
\([0,T]\times\sqrt2S^1\). The exact triangle inequality is

\[
 \begin{aligned}
 \frac{\|f_{n,\mu_{\epsilon,\nu}}-f_{n,\nu_*}
                           -\epsilon D_\sigma f_n\|_\infty}{\epsilon}
 \le{}&\omega_Y(\epsilon)\\
 &+\frac{\|f_{n,\mu_{\epsilon,\nu}}-f_{\mu_{\epsilon,\nu}}\|_\infty
            +\|f_{n,\nu_*}-f_{\nu_*}\|_\infty}{\epsilon}\\
 &+\|D_\sigma f_n-\mathscr D_\sigma f\|_\infty.
 \end{aligned}
 \tag{NV-finite-triangle}
\]

At this fixed positive \(\epsilon\), the two prediction errors vanish
in probability by the finite capture established above, since both
laws lie in its neighborhood. The last error vanishes in probability
by C.4.6.T10 with exactly this fixed \(\nu\), this physical horizon,
and the same Gaussian initialization. A finite union bound suffices;
independence of the three errors is unnecessary. For any \(a>0\),
choose \(\epsilon\) small enough that \(\omega_Y(\epsilon)<a/2\),
then take width to infinity at that fixed \(\epsilon\). This proves

\[
 \lim_{\epsilon\downarrow0}\limsup_{n\to\infty}
 \Pr\left[
 \frac{\displaystyle
  \sup_{\substack{0\le t\le40\\x\in\sqrt2S^1}}
  |f_{n,\mu_{\epsilon,\nu}}(t,x)-f_{n,\nu_*}(t,x)
                            -\epsilon D_\sigma f_n(t,x)|}{\epsilon}
       >a\right]=0
 \quad\text{for every fixed }\nu\in\mathcal P(\mathcal Z),\ a>0.
 \tag{NV-finite-nonlinear-limit}
\]

The population remainder is uniform over contaminating laws. The finite
statement fixes the law before its probability limit and takes width
before the contamination limit. It gives no uniform finite-width
remainder, no joint rate for \(\epsilon\) and width, and no supremum
over laws of finite failure probabilities. All conclusions concern
physical GF through \(40\), with the stated initialization and exact
Borel-law loss; they assert neither a raw-GD variation theorem nor an
ambient \(L^2\) Fréchet derivative or a quadratic nonlinear remainder.

<!-- END CANONICAL SCIENTIFIC BODY -->

## Assembly provenance (outside the canonical subsection)

Assembler: `/root/p2_canonical_variation`, 2026-09-11. This is a scoped
author assembly, ineligible for independent review. It makes no independent
review or promotion claim. Only this assigned source output and its assigned
verification scratch were written; no frozen input, established file, Git
index, or commit was changed by the assembler.

Actual scientific read scope:

- `docs/NOTATION.md`, complete, 98 lines.
- `P2_THEOREM.md`, complete, 320 lines.
- `P2_VARIATION.md`, complete, 430 lines.
- `P2_COMBINED_TAIL_CONTRACT.md`, complete, 523 lines.
- `P2_RESPONSE_BRIDGE.md`, complete, 138 lines.
- `P2_REACHED_TAILS.md`, complete, 784 lines.
- `P1_SECTION.md`, complete, 2,062 lines.
- `P2_DEPENDENCIES.md`: heading inventory and complete C.4.1,
  lines 1053–1278, including its transport proof. Remaining scientific
  proof bodies in this packet were not read for this assembly.
- `P1_DEPENDENCIES.md`: heading inventory and lines 620–1225, containing
  complete III.F.1–11 and A.1–4. A truncated middle output was repaired
  by a complete overlapping read of lines 844–1004. Remaining scientific
  proof bodies in this packet were not read for this assembly.

Required process inputs read completely: `AGENTS.md`, both parts of
`RESEARCH_WORKFLOW.md`, the `solve-math-rigorously` and
`investigate-conjectures` skills, and the latter's `evidence-ledger.md`
and `adversarial-audit.md` references. No review reports, other attempts,
other studies, external scientific sources, or Git history were opened.
Git status, HEAD and the staged path list were inspected as metadata only;
initial observed HEAD was `0772d18e8816c87144948f861022b132c81d9dc9`
and the index had no staged paths.

The supervisor supplies the preceding canonical proofs of the source
estimate, raw construction, energy/readout bounds, same-mesh Hölder
comparison, and finite capture. Their stated interface is used here;
their separate assembly outputs were not read. Thus this subsection's
downstream argument does not independently certify those upstream proofs.
No missing downstream proof obligation was found in the supplied route.

Author verification: the probe-mass exponents, neighborhood margins,
Gaussian-root/Jensen/Hölder constants, loss normalization in the clock
equation, one-bounded-endpoint factorization, compact-family product
remainders, exact C.4.6 identification, and ordered finite triangle
inequality were checked directly. Deterministic document checks verify
unique local equation tags, resolved local references, balanced math
delimiters, canonical population superscripts and the absence of
study/history/status references in the scientific body. The check record
is in the assigned
`data/generated/trained_data_response/p2_20260911_02/canonical_variation/`
scratch namespace. No training or numerical experiment was run.


SHA-256 input snapshots:

| Input | SHA-256 |
|---|---|
| `AGENTS.md` | `7778b7073a02de3e94f8ae9aefe940ebc9eddea7467816662e5cce1020cd98ba` |
| `RESEARCH_WORKFLOW.md` | `8b36d7dfc1ad881fcb6bfe32274a5e50c5125b33d68dbcf7c3937f7f6c21ce12` |
| `docs/NOTATION.md` | `199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b` |
| `P2_THEOREM.md` | `849655c74c7552b874085401ffb4af22fc51d126702bf5bc61b689946cb0854a` |
| `P2_VARIATION.md` | `ef28df6745758adc1c587a4d73442c3a49db575026ac2bee86708a24de44c5fd` |
| `P2_COMBINED_TAIL_CONTRACT.md` | `818d2885fa706d6ceae1101afc3cee2e91afea27ec49c431a4d87f6321e3f994` |
| `P2_RESPONSE_BRIDGE.md` | `7a410d6d5e2fc16a07b4a04ab355878d51ec9940a1d52c1ca506b6288d528e89` |
| `P2_REACHED_TAILS.md` | `837535f363d8140516ed993698f0e48d183dc029fe66cffc1277aff79e328716` |
| `P2_DEPENDENCIES.md` | `35375c597d65df70ca7fcec375357b0fdbca8d06bab3a873e690fda285d290e9` |
| `P1_SECTION.md` | `33c819282d83f7f4704cbd3a90e87b445d17ce161cc922c1ad786b5eb0d9de38` |
| `P1_DEPENDENCIES.md` | `ca696bc4ed14ea337028eb1e6ef9c7f729ed2a0153bc210de8e16dea18f5ee79` |
| `/etc/codex/skills/solve-math-rigorously/SKILL.md` | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |
| `/etc/codex/skills/investigate-conjectures/SKILL.md` | `a0fafd639f54834c58fb05ed30adb0e7fe09e2845ff12aba4395845b7d9528de` |
| `investigate-conjectures/references/evidence-ledger.md` | `9e7573b37cbd954432236bdcb13f6b83b6325e0ff2653a198939842bc81c3a2e` |
| `investigate-conjectures/references/adversarial-audit.md` | `8609b420aa8b5cbd405521bcd9acfdbfd719dfaa3962a23496aac4b3e2de4501` |
