# Shallow all-time response comparison without absorption

Status: internally checked bounded proof, 2026-10-07. The proof-only smallness condition on the residual mass is removed. This is a one-hidden-layer theorem, not completion of the arbitrary-depth or finite-compression target.

Input scope: the supervisor's shallow comparison assignment; complete `KINETIC_OBSERVABLE_ROUTE.md` (SHA-256 `9b27269a8c1e6831aa941b95100d31e0a30baeb3eab6f37e004e65efad1bcd2a`); complete `OSGOOD_RESPONSE_STABILITY.md` (SHA-256 `90e1f9d3ffbd8d72aa5fce21beecee1879b507fdaad969251e37f525d5dde606`); and this author's previously derived finite-response laws. No integrated study, other study, book, literature, experiment, or Git history was read. The Osgood note motivates keeping the residual weight; the present shallow proof uses an ordinary linear Volterra inequality and does not require an Osgood estimate. Its fitting premises are stated and, in a separate explicit small-label corollary, proved directly. No premise from an integrated source is being certified.

## 1. Model and exact response equations

There are \(p\) fixed unit vectors \(v_a\in\mathbb R^d\); the first \(m\le p\) are training inputs. Write
\[
Q_{ab}=v_a^\top v_b,\qquad Q=CC^\top,\qquad
C\in\mathbb R^{p\times r},\quad r=\operatorname{rank}Q,\qquad
\kappa=\frac2m.
\]
The factorization may have \(r<p\). Let \(\xi_i\) be independent \(N(0,I_r)\) vectors. The width-\(n\) shallow feature-learning system is
\[
\begin{aligned}
f_{n,a}&=\frac1n\sum_{i=1}^n w_i\phi(z_{ai}),&
c_{n,b}&=y_b-f_{n,b}\quad(b\le m),&
u_n&=\kappa c_n,\\
\dot w_i&=\sum_{b=1}^m u_{n,b}\phi(z_{bi}),&
\dot z_{ai}&=\sum_{b=1}^m u_{n,b}Q_{ab}w_i\phi'(z_{bi}),&
(w_i,z_i)(0)&=(0,C\xi_i).
\end{aligned} \tag{1}
\]
Thus \(z_{ai}\) are the panel preactivations, not newly sampled auxiliary features. This is the exact shallow specialization of the prescribed physical gradient-flow clock.

Assume that \(\phi\) is real on the real axis, holomorphic on \(|\operatorname{Im}\zeta|<\rho\), and \(|\phi'(\zeta)|\le L\) there. In particular
\[
|\phi(x)|\le|\phi(0)|+L|x|,\qquad
|\phi'(x)|\le L,\qquad |\phi''(x)|\le 2L/\rho. \tag{2}
\]
Only the real bounds in (2) will be used. The theorem does not require bounded activation values.

For \(X=(w,z)\in\mathbb R^{1+p}\), define the panel output and response observables
\[
o_a(X)=w\phi(z_a),\qquad
k_{ab}(X)=\phi(z_a)\phi(z_b)+Q_{ab}w^2\phi'(z_a)\phi'(z_b), \tag{3}
\]
and the training vector fields
\[
V_b(X)=\bigl(\phi(z_b),\,Q_{:b}w\phi'(z_b)\bigr).
\]
The deterministic kinetic state \(\mu_t\) starts at
\(\mu_0=\delta_0(dw)\otimes N(0,Q)(dz)\) and satisfies
\[
\partial_t\mu_t+\operatorname{div}_X\!\left[
 \left(\sum_{b=1}^m u_b(t)V_b(X)\right)\mu_t
\right]=0,\qquad
f_a(t)=\int o_a\,d\mu_t,\quad u=\kappa(y-f_{1:m}). \tag{4}
\]
Equivalently, for a deterministic control \(u\), let
\[
\dot X^u(t,\xi)=\sum_{b=1}^m u_b(t)V_b(X^u(t,\xi)),
\qquad X^u(0,\xi)=(0,C\xi). \tag{5}
\]
In (4), \(\mu_t\) is the law of \(X^u(t,\xi)\), with the self-consistent control just specified. The empirical measure of (1) satisfies exactly the same weak transport identity. A density in all \(p+1\) coordinates is not assumed.

Define
\[
K_{ab}(t)=\mathbb E\,k_{ab}(X^u(t,\xi)),\qquad
K_{n,ab}(t)=\frac1n\sum_i k_{ab}(X^{u_n}(t,\xi_i)). \tag{6}
\]
Direct differentiation of (3) gives the exact identities
\[
\dot f_a=\sum_{b=1}^m K_{ab}u_b,\qquad
\dot c=-\kappa K_{\mathrm{tr}}c,\qquad
K_{\mathrm{tr}}=K_{1:m,1:m}, \tag{7}
\]
and their empirical versions. These normalizations are important: \(u=\kappa c\), so the integrated control mass below includes \(\kappa\).

Both terms in \(K_{\mathrm{tr}}\) are positive semidefinite. For the second term and \(q\in\mathbb R^m\),
\[
\sum_{a,b\le m}q_aq_bQ_{ab}\mathbb E[w^2\phi'(z_a)\phi'(z_b)]
=\mathbb E\!\left[w^2\left|\sum_{a\le m}q_a\phi'(z_a)v_a\right|^2\right]\ge0.
\]
Consequently \(|c(t)|,|c_n(t)|\le |y|\). All vector norms below are Euclidean, matrix norms marked \(\mathrm F\) are Frobenius, and coercivity concerns only the training block.

## 2. Controlled characteristics and a common Gaussian envelope

For any control \(v\), put
\[
S_v(t)=\int_0^t|v(s)|\,ds,\qquad R(\xi)=1+|C\xi|.
\]
For every fixed \(B<\infty\), there is a deterministic function
\[
P_B(\xi)=C_B R(\xi)^4\exp(C_B R(\xi))\ge1,\qquad
M_B=\mathbb E P_B,\quad V_B=\mathbb E P_B^2<\infty, \tag{8}
\]
with the following bounds. Constants \(C_B\) depend only on \(B,p,m,Q,\phi(0),L,\rho\); they do not depend on \(n\), a particular control, or time. Whenever \(S_v(t),S_{\widetilde v}(t)\le B\), let
\[
D_{v,\widetilde v}(t)=\int_0^t|v(s)-\widetilde v(s)|\,ds.
\]
Then
\[
\begin{aligned}
\|k(X^v(t,\xi))-k(X^{\widetilde v}(t,\xi))\|_{\mathrm F}
&\le P_B(\xi)D_{v,\widetilde v}(t),\\
|o(X^v(t,\xi))-o(X^{\widetilde v}(t,\xi))|
&\le P_B(\xi)D_{v,\widetilde v}(t),\\
\|\partial_t k(X^v(t,\xi))\|_{\mathrm F}
 +|\partial_t o(X^v(t,\xi))|
&\le P_B(\xi)|v(t)|,\\
\|k(X^v(t,\xi))\|_{\mathrm F}+|o(X^v(t,\xi))|
&\le P_B(\xi).
\end{aligned} \tag{9}
\]
The time-derivative statement holds almost everywhere. One can enlarge the same \(P_B\) so that
\[
\left\|\phi(z^v_{1:m}(t,\xi))\phi(z^v_{1:m}(t,\xi))^\top
 -\phi((C\xi)_{1:m})\phi((C\xi)_{1:m})^\top\right\|_{\mathrm F}
\le P_B(\xi)S_v(t)^2. \tag{10}
\]

Here is a derivation, including the unbounded-activation issue. From (2) and (5), with a fixed constant \(a\),
\[
1+|w^v|+|z^v|\le R e^{aS_v},\qquad
|w^v|\le aR e^{aS_v}S_v,\qquad
|z^v-C\xi|\le a^2R e^{aS_v}S_v^2. \tag{11}
\]
The first estimate follows from a scalar linear-growth inequality. Integrating the equation for \(w\), then the equation for \(z\), gives the other two, with an inessential enlargement of \(a\). On these trajectories, the state derivative of \(\sum_b v_b V_b\) is at most \(C_B R|v|\), and its variation with the control is at most \(C_B R|v-\widetilde v|\). Applying Grönwall to the difference of two characteristic equations yields
\[
|X^v(t,\xi)-X^{\widetilde v}(t,\xi)|
\le C_B R(\xi)e^{C_B R(\xi)}D_{v,\widetilde v}(t). \tag{12}
\]
On the same state region, the gradients of \(o\) and \(k\) are bounded by \(C_B R^2\). Equations (9) follow from (11)–(12) and the chain rule. Equation (10) follows from the last bound in (11), the Lipschitz bound for \(\phi\), and the linear growth of each feature. Gaussian tails imply that every fixed moment of \(P_B\), not just the two in (8), is finite.

The envelope is uniform over controls of bounded mass, but no empirical-process concentration uniformly over that control class is being asserted.

For completeness, the characteristic kinetic solution used in (4) exists uniquely on every finite time interval. On a sufficiently short interval the map
\[
v\longmapsto \kappa\left(y-\mathbb E\,o_{1:m}(X^v)\right)
\]
is a contraction on a closed sup-norm control ball: (9), or its time-shifted form, bounds its difference by \(\kappa M_B\) times the interval length and the sup-norm control difference. The same estimate and continuity ensure that a sufficiently short interval maps a ball about the initial control into itself. For a restart after any bounded past control mass, the initial characteristic state is bounded by a constant times \(R\), and the same argument has an integrable envelope of the form (8). The differentiated identities (7) follow by dominated convergence using (9), and give \(|u|\le\kappa|y|\). Thus every finite horizon has a deterministic total-control bound. The characteristic growth and contraction constants on that horizon remain finite, permitting continuation to its endpoint. This proves global existence in the characteristic class and uniqueness by continuation. It does not assert uniqueness among arbitrary weak measure solutions without a moment/characteristic condition. The finite system (1) is likewise globally defined: local uniqueness follows from (2), the energy bound controls \(u_n\), and (11) rules out finite-time escape.

## 3. Uniform sampling along the deterministic population path

Assume for this section that the deterministic population control has finite total mass
\[
S_u(\infty)\le B<\infty.
\]
For any envelope \(P_{\widetilde B}\) with \(\widetilde B\ge B\), set \(V=V_{\widetilde B}\) and define
\[
\begin{aligned}
\zeta_n(t)&=\frac1n\sum_i k(X^u(t,\xi_i))-K(t),&
Z_n&=\sup_{t\ge0}\|\zeta_n(t)\|_{\mathrm F},\\
\eta_n(t)&=\frac1n\sum_i o(X^u(t,\xi_i))-f(t),&
Y_n&=\sup_{t\ge0}|\eta_n(t)|.
\end{aligned} \tag{13}
\]
The control in these quantities is deterministic. The initial samples \(\xi_i\) therefore remain independent when evaluating these prescribed functions. The quantities in (13) are not the fluctuations of the interacting empirical trajectory.

The useful bounds are in mean square:
\[
\|Z_n\|_{L^2(\xi_1,\ldots,\xi_n)}
\le \frac{\sqrt V(1+B)}{\sqrt n},\qquad
\|Y_n\|_{L^2(\xi_1,\ldots,\xi_n)}
\le \frac{\sqrt V B}{\sqrt n}. \tag{14}
\]
To prove them, the variance identity for independent centered vectors or matrices gives
\[
\|\zeta_n(0)\|_{L^2(\mathrm F)}\le \sqrt{V/n},\qquad
\|\dot\zeta_n(t)\|_{L^2(\mathrm F)}\le \sqrt{V/n}|u(t)|.
\]
Absolute continuity, followed by Minkowski's integral inequality, now yields
\[
\|Z_n\|_{L^2}
\le \|\zeta_n(0)\|_{L^2(\mathrm F)}
 +\int_0^\infty\|\dot\zeta_n(t)\|_{L^2(\mathrm F)}dt.
\]
This is the first estimate in (14). Since \(o(X^u(0,\xi))=0\), one has \(\eta_n(0)=0\), giving the second. Differentiation under the Gaussian expectation, integration to infinity, and measurability of the suprema follow from (9), finite \(\int|u|\), and continuity. This proves an all-time sampling estimate without a time mesh, a growing class of tests, or a trajectory-dependent concentration assertion.

## 4. The deterministic comparison: retain the Volterra weight

Consider an interval \([0,T]\) on which:

1. Both controls have mass at most a fixed \(\widetilde B\).
2. \(K_{n,\mathrm{tr}}(t)\succeq\lambda I_m\) for some \(\lambda>0\).
3. The actual sample satisfies \(n^{-1}\sum_i P_{\widetilde B}(\xi_i)\le A\), where \(A>0\).

Set
\[
d(t)=c_n(t)-c(t),\qquad
D_t=\int_0^t|u_n(s)-u(s)|\,ds=\kappa\int_0^t|d(s)|\,ds. \tag{15}
\]
Splitting through the deterministic reference trajectory gives, at each time,
\[
\|K_n(t)-K(t)\|_{\mathrm F}\le A D_t+Z_n,\qquad
|f_n(t)-f(t)|\le A D_t+Y_n. \tag{16}
\]
This uses (9) for the interacting-versus-reference characteristic difference and (13) for the reference sampling error; it does not condition independent neurons on their empirical control.

Subtracting the exact residual equations gives
\[
\dot d=-\kappa K_{n,\mathrm{tr}}d
 -\kappa(K_{n,\mathrm{tr}}-K_{\mathrm{tr}})c,\qquad d(0)=0.
\]
Coercivity implies the propagator bound
\[
|d(t)|\le\kappa\int_0^t e^{-\kappa\lambda(t-s)}
 (A D_s+Z_n)|c(s)|\,ds. \tag{17}
\]
For a time-dependent symmetric kernel, this follows by differentiating the squared norm of a homogeneous solution; simultaneous diagonalization is unnecessary. Multiplying the time integral of (17) by \(\kappa\) and using Tonelli gives
\[
\begin{aligned}
D_t
&\le \frac1\lambda\int_0^t
 \left(1-e^{-\kappa\lambda(t-s)}\right)(A D_s+Z_n)|u(s)|\,ds\\
&\le \frac1\lambda\int_0^t (A D_s+Z_n)|u(s)|\,ds. 
\end{aligned} \tag{18}
\]
In particular, writing \(|c|\) instead of \(|u|\) in the last integral would require the prefactor \(\kappa/\lambda\), not \(1/\lambda\).

Keep \(D_s\) at its own time. With \(q(t)=A D_t+Z_n\), (18) implies
\[
q(t)\le Z_n+\frac A\lambda\int_0^t q(s)|u(s)|\,ds.
\]
The usual integral Grönwall proof applies to the integrable weight \((A/\lambda)|u|\), and proves
\[
\boxed{
\begin{aligned}
D_t&\le \frac{Z_n}{A}
 \left[\exp\!\left(\frac{A S_u(t)}{\lambda}\right)-1\right],\\
\|K_n(t)-K(t)\|_{\mathrm F}
&\le Z_n\exp\!\left(\frac{A S_u(t)}{\lambda}\right),\\
|f_n(t)-f(t)|
&\le Z_n\left[\exp\!\left(\frac{A S_u(t)}{\lambda}\right)-1\right]+Y_n.
\end{aligned}} \tag{19}
\]
If desired, use suprema restricted to \([0,t]\) in (13); the stated global \(Z_n,Y_n\) only simplify notation. Formula (19) also follows by solving the equality for the integral majorant, so it applies when \(Z_n=0\).

No condition \(A S_u(\infty)<\lambda\) is present. Replacing \(D_s\) by \(D_T\) before integrating would produce a spurious absorption condition. The replacement for that restriction is a finite, possibly large exponential constant. The damping operator is empirical, whereas the Grönwall weight is the deterministic reference residual.

## 5. Conditional all-time theorem with empirical fitting obtained by continuation

The following result requires no separate finite-width fitting premise.

**Theorem.** Suppose the deterministic kinetic solution of (4) satisfies, for fixed constants \(\lambda_*>0\) and \(B<\infty\),
\[
K_{\mathrm{tr}}(t)\succeq\lambda_* I_m\quad(t\ge0),\qquad
S_u(\infty)\le B. \tag{20}
\]
These are explicit population fitting/coercivity premises, not consequences of the mere positivity of the initial feature Gram for arbitrary labels. Indeed, the first premise already implies \(S_u(\infty)\le |y|/\lambda_*\), so this latter value is always an admissible choice of \(B\).

Use the envelope \(P_{B+1}\) of Section 2 and set
\[
\begin{gathered}
M=M_{B+1},\quad V=V_{B+1},\quad A=2M,\quad
\lambda=\lambda_*/2,\\
E_*=\exp(AB/\lambda),\qquad
F_*=(E_*-1)/A,\qquad
z_*=\min\left\{\frac{\lambda_*}{4E_*},
                 \frac1{2(1+F_*)}\right\}>0,\\
C_{\mathrm{bad}}=\frac{\operatorname{Var}(P_{B+1})}{M^2}
                  +\frac{V(1+B)^2}{z_*^2}.
\end{gathered} \tag{21}
\]
There is an explicitly defined event \(\mathcal E_n\) of probability at least \(1-C_{\mathrm{bad}}/n\) on which
\[
\begin{gathered}
K_{n,\mathrm{tr}}(t)\succeq \tfrac34\lambda_* I_m
\quad(t\ge0),\qquad
S_{u_n}(\infty)\le B+\tfrac12,\\
D_\infty\le F_*Z_n,\qquad
\sup_{t\ge0}\|K_n(t)-K(t)\|_{\mathrm F}\le E_* Z_n,\qquad
\sup_{t\ge0}|f_n(t)-f(t)|\le (E_*-1)Z_n+Y_n.
\end{gathered} \tag{22}
\]
In particular, all panel outputs, the complete finite-panel response matrix, and the integrated training-control difference have all-time \(O_{\mathbb P}(n^{-1/2})\) error. Their constants can depend on the fixed data, activation bounds, labels, \(B\), and \(\lambda_*\), but not on width or time. No uniformity as \(B\) grows or \(\lambda_*\) vanishes is asserted.

**Proof.** Define
\[
\mathcal E_n=
\left\{\frac1n\sum_iP_{B+1}(\xi_i)\le2M,\quad Z_n\le z_*\right\}.
\]
The variance bound for the empirical envelope and (14) imply the stated probability by Chebyshev's inequality. This event is used only in the proof; it is not advice provided to a simulator.

Fix a sample in \(\mathcal E_n\). At time zero,
\[
K_{n,\mathrm{tr}}(0)\succeq
(\lambda_*-Z_n)I_m\succeq \tfrac34\lambda_* I_m.
\]
Stop at the first time when either \(S_{u_n}=B+1\) or
\(\lambda_{\min}(K_{n,\mathrm{tr}})=\lambda_*/2\). Prior to this time both controls have mass at most \(B+1\), and Section 4 applies with the constants in (21). Therefore throughout the stopped interval,
\[
D_t\le F_*Z_n<\tfrac12,\qquad
S_{u_n}(t)\le S_u(t)+D_t<B+\tfrac12,
\]
and
\[
K_{n,\mathrm{tr}}(t)\succeq
(\lambda_*-E_*Z_n)I_m\succeq\tfrac34\lambda_* I_m.
\]
Both stopping boundaries are separated by a fixed positive margin. Continuity excludes any finite stopping time. Since the finite system already exists on every finite horizon, (19) consequently holds for all time and proves (22). Coercivity additionally gives
\[
|c_n(t)|\le |y|\exp(-3\kappa\lambda_* t/4).
\]
The bound with \(\lambda_*/2\) would suffice; the displayed stronger one follows from the final margin. \(\square\)

Here is an explicit probability version of the output rate. Define
\[
C_f=\sqrt V\bigl[(E_*-1)(1+B)+B\bigr].
\]
For every \(0<\delta<1\),
\[
\mathbb P\!\left\{
\sup_{t\ge0}|f_n(t)-f(t)|>
\frac{C_f}{\sqrt{\delta n}}
\right\}
\le \delta+\frac{C_{\mathrm{bad}}}{n}. \tag{23}
\]
The analogous constants for \(D_\infty\) and the kernel supremum are
\[
C_D=F_*\sqrt V(1+B),\qquad
C_K=E_*\sqrt V(1+B).
\]
Each obeys (23) with its corresponding quantity and constant; replacing \(\delta\) by \(\delta/3\) makes the three estimates simultaneous. Moreover
\[
\mathbb E\!\left[\mathbf1_{\mathcal E_n}
 \sup_{t\ge0}|f_n(t)-f(t)|^2\right]\le C_f^2/n. \tag{24}
\]
This is a good-event mean-square statement for the full panel, not an unconditional mean-square assertion about arbitrary validation outputs on unsuccessful samples. For training outputs alone, the global energy identity bounds the difference by \(2|y|\), even off \(\mathcal E_n\). Hence the unconditional refinement
\[
\mathbb E\sup_{t\ge0}|f_{n,1:m}(t)-f_{1:m}(t)|^2
\le\frac{C_f^2+4|y|^2C_{\mathrm{bad}}}{n} \tag{25}
\]
is valid. The probability statements are useful once \(n\) is large compared with their fixed constants; they remain valid at smaller widths.

## 6. Explicit removal of the old shallow label restriction

One can apply (19) directly to the elementary small-label fitting event, without using the more general continuation constants (21). This gives an unconditional sufficient fitting class and exhibits exactly which old cap is removed.

Let the initial population training feature Gram be
\[
G_{0,ab}=\mathbb E[\phi((C\xi)_a)\phi((C\xi)_b)],\qquad
\lambda_0=\lambda_{\min}(G_0)>0.
\]
For the time-dependent feature Grams use
\[
\begin{aligned}
G_{\mathrm{tr}}(t)
&=\mathbb E\!\left[
\phi(z^u_{1:m}(t,\xi))\phi(z^u_{1:m}(t,\xi))^\top\right],\\
G_{n,\mathrm{tr}}(t)
&=\frac1n\sum_i
\phi(z^{u_n}_{1:m}(t,\xi_i))\phi(z^{u_n}_{1:m}(t,\xi_i))^\top,
\qquad G_{n,0}=G_{n,\mathrm{tr}}(0).
\end{aligned}
\]
Here \(\lambda_0\) is the source kinetic note's initial feature-Gram gap; it is not a retained-history gap. Choose \(P_1\) satisfying (8)–(10), write \(M_1=\mathbb E P_1\), \(V_1=\mathbb E P_1^2\), and put
\[
\lambda=\frac{\lambda_0}{2},\qquad
S_{\mathrm{fit}}=\min\left\{1,\sqrt{\frac{\lambda_0}{8M_1}}\right\},
\qquad
y_{\mathrm{fit}}=\frac{\lambda S_{\mathrm{fit}}}{2}. \tag{26}
\]
Suppose \(|y|\le y_{\mathrm{fit}}\). Define
\[
\mathcal E_{n,\mathrm{fit}}=
\left\{
\|G_{n,0}-G_0\|_{\mathrm{op}}\le\lambda_0/4,\quad
\frac1n\sum_iP_1(\xi_i)\le2M_1
\right\}, \tag{27}
\]
where \(G_{n,0}\) is the initial empirical training feature Gram. Since
\(\|\phi((C\xi)_{1:m})\phi((C\xi)_{1:m})^\top\|_{\mathrm F}\le P_1(\xi)\),
\[
\mathbb P(\mathcal E_{n,\mathrm{fit}}^c)
\le \frac{C_{\mathrm{fit}}}{n},\qquad
C_{\mathrm{fit}}=\frac{16V_1}{\lambda_0^2}
                 +\frac{\operatorname{Var}(P_1)}{M_1^2}. \tag{28}
\]

Until either control reaches mass \(S_{\mathrm{fit}}\), (10) yields
\[
\begin{aligned}
G_{\mathrm{tr}}(t)&\succeq
(\lambda_0-M_1 S_{\mathrm{fit}}^2)I_m\succeq\lambda I_m,\\
G_{n,\mathrm{tr}}(t)&\succeq
(3\lambda_0/4-2M_1 S_{\mathrm{fit}}^2)I_m\succeq\lambda I_m
\quad\hbox{on }\mathcal E_{n,\mathrm{fit}}.
\end{aligned}
\]
The other term of each response kernel is positive semidefinite. Equation (7) therefore gives exponential residual decay with rate \(\kappa\lambda\), and then
\[
S_u(t),S_{u_n}(t)\le\frac{|y|}{\lambda}
 =:B_y\le S_{\mathrm{fit}}/2.
\]
The strict margin excludes the first hit of \(S_{\mathrm{fit}}\). Thus these fitting and mass bounds hold globally, for the population flow and, on (27), the empirical flow.

Apply Section 4 with \(\widetilde B=1\), \(A=2M_1\), and
\[
E_y=\exp(2M_1B_y/\lambda).
\]
The conclusion is
\[
\begin{aligned}
D_\infty&\le \frac{E_y-1}{2M_1}Z_n,\\
\sup_{t\ge0}\|K_n(t)-K(t)\|_{\mathrm F}&\le E_y Z_n,\\
\sup_{t\ge0}|f_n(t)-f(t)|&\le(E_y-1)Z_n+Y_n
\end{aligned} \tag{29}
\]
on \(\mathcal E_{n,\mathrm{fit}}\), where (14) holds with \(V_1\) and \(B_y\). In particular the panel output threshold
\[
\frac{\sqrt{V_1}\bigl[(E_y-1)(1+B_y)+B_y\bigr]}{\sqrt{\delta n}}
\]
has failure probability at most \(\delta+C_{\mathrm{fit}}/n\).

The original shallow route additionally imposed
\(S_{\mathrm{fit}}\le\lambda/(4M_1)\) by including that quantity in its minimum. That cap was used only to absorb the comparison inequality after replacing \(D_s\) by its terminal value. It is absent from (26) and (29), with no replacement assumption. The caps \(1\) and \(\sqrt{\lambda_0/(8M_1)}\) remain solely as convenient sufficient conditions for the separate feature-Gram fitting bootstrap. They are not asserted to be necessary for fitting. For any larger label regime in which (20) is supplied by a valid independent argument, Section 5 applies unchanged and introduces no additional label cap.

## 7. Interpretation and limits

The closure (4) is an autonomous population law; the kernel (6) is an explicit observable of its evolving state. It describes feature learning, not a frozen initial kernel. For example (1) gives
\[
\ddot z_{ai}(0)=\kappa^2
\left(\sum_{b\le m}y_b\phi(z_{bi}(0))\right)
\left(\sum_{b\le m}y_bQ_{ab}\phi'(z_{bi}(0))\right),
\]
which need not vanish. Equations (19) and (29) show that finite residual mass makes the shallow response comparison stable for arbitrarily long physical time.

The rate proved here is \(O_{\mathbb P}(n^{-1/2})\), not \(o_{\mathbb P}(n^{-1/2})\), and not reconstruction of the realized leading fluctuation. For instance,
\[
\operatorname{Var}(\dot f_{n,a}(0))
=\frac{\kappa^2}{n}\operatorname{Var}\!\left[
\phi((C\xi)_a)\sum_{b\le m}y_b\phi((C\xi)_b)\right]
\]
is an exact identity and may be strictly positive. Nothing in the deterministic kinetic replacement retains that particular random coefficient.

The proof is special to one hidden layer: its finite-panel characteristic equation uses the fixed input Gram \(Q\) and no repeatedly traversed trainable Gaussian matrix. It does not provide deep response-memory existence, a finite autonomous spectral approximation, a computational cost bound for Gaussian expectations, or polylogarithmic compression. It also does not verify any integrated source's fitting premises or change the scope of an arbitrary-depth target. The established improvement is the removal of the proof-only absorption cap, together with an all-time shallow kernel/output/control rate and an explicit continuation transfer of coercivity.
