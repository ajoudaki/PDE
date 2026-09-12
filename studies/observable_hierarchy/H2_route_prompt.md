# H2 independent prompt-only route: static observable frames and Osgood stability

Frozen on 2026-09-12. Scientific input was only the supervisor's assignment prompt. No repository scientific source, other route, history, or web source was read. The required mathematics and investigation skills, together with their research-contract and adversarial-audit references, were read. No experiment was run.

## 1. Conclusion and exact contract

There is a concrete candidate satisfying the explicitly permitted **matrix of observable coefficients** interpretation: choose finitely many bounded initial observable words, normalize their Gram matrices with a positive ridge, and evolve the coefficients of the current first-layer displacement, readout, and Hilbert–Schmidt perturbation in those fixed features. The initial middle action is a fixed matrix of initial-word contractions. Its transpose implements the other action direction.

Under the prompt's stated strong-flow, initialized-word-law, and uniform-in-time/input exponential-tail premises, the construction below has a complete convergence argument. Its stability uses only the true trajectory's backward-field tails. No corresponding tail estimate for the approximations is assumed. A fixed, explicitly specified clipping function appears only in the approximate readout factor used for backpropagation; its threshold is chosen from the elementary a priori readout bound and is never sent to infinity. It is exactly the identity on the target trajectory.

The main interpretive issue is admissibility: this is finite-rank Galerkin compression in an initial **observable** frame, with a finite coefficient matrix for the Hilbert–Schmidt perturbation. It contains no sampled representative neurons, no original neuron-indexed matrix, and no finite-network approximation. If the intended exclusion prohibits every such finite coefficient matrix despite the prompt's explicit allowance, this witness would be excluded by that additional restriction. That would concern this witness, not establish an impossibility result.

The following assumptions are used precisely as supplied:

1. There are probability spaces with real Hilbert spaces \(L^2_1,L^2_2\), a bounded initialized action \(A_0:L^2_1\to L^2_2\), \(\|A_0\|\le2\), and its actual adjoint.
2. The canonical strong solution exists on \([0,T]\), \(T=1/200\), for each law \(\mu\) in the stated fixed positive ball. The law is a probability measure on \(S^1\times[-Y,Y]\). The initial state is \(w=g\), \(c=0\), \(K=0\).
3. Every fixed finite collection of initialized words using both actions has its complete joint law computable by the supplied finite Gaussian-conditioning procedure, including response corrections. This premise is used for exact initial coefficients and fixed mark laws, never as a runtime action oracle.
4. For each such law, the true \(q(t,u)\) has an exponential or stronger tail uniformly over \((t,u)\in[0,T]\times S^1\). It suffices that constants \(Q,\kappa>0\) exist with
   \[
   \sup_{t,u}\|q(t,u)\mathbf1_{\{|q(t,u)|>R\}}\|_2
      \le Qe^{-\kappa R},\qquad R\ge0.                 \tag{1}
   \]
   An exponential probability tail implies (1), after weakening its exponent and enlarging its constant; a sub-Gaussian tail also implies it. The constants need not be runtime inputs. They may depend on the law when only convergence for each law is required.

The same sequence of static features is used for all laws in this ball. Only the integrations against \(\mu\) in the autonomous equations depend on the law. Complexity may increase with hierarchy order, but is independent of a finite network's widths and of future target states.

The guarantee proved below is
\[
\sup_{t\le T}\bigl(\|w_N-w\|_2+\|c_N-c\|_2
                      +\|K_N-K\|_{\mathrm{HS}}\bigr)\longrightarrow0, \tag{2}
\]
which entails uniform-time, whole-circle prediction convergence and uniform-time \(W_2\) convergence of every separately fixed finite joint word tuple, with the initial/current pairing and both action directions preserved. This is convergence for every law in the given ball; it does not assert a supremum over laws without additional compactness of the law family.

## 2. Bounded initial dictionaries and the space they generate

Construct two countable dictionaries \(\mathcal D_1,\mathcal D_2\) of bounded **initialized** words. Include constants in both and \(\tanh(g_1),\tanh(g_2)\) in the first. Enumerate all finite applications of the following operations, with rational scalar coefficients:

- affine combinations of bounded dictionary entries and finite products of bounded entries;
- \(\sin,\cos,\tanh\) of admitted affine expressions;
- \(\tanh(A_0v/m)\) for bounded first-population words \(v\) and positive integers \(m\);
- \(\tanh(A_0^*v/m)\) for bounded second-population words \(v\) and positive integers \(m\).

All these are permitted initialized words. Other supplied seeds such as \(z_{20}(v)\) can be inserted through their bounded transforms, but are already generated by this construction. An enumeration by expression length and coefficient height gives finite initial segments at every order. None of the words depends on \(\mu\) or on a trained state.

Write \(\mathcal F_i=\sigma(\mathcal D_i)\), and let \(H_i=L^2(\mathcal F_i)\), viewed as a closed subspace of \(L^2_i\). The real linear span of \(\mathcal D_i\) is dense in \(H_i\). Here the exact bounded-algebra fact being used is: the linear span of a bounded, unital algebra of real functions is dense in the \(L^2\) of its generated sigma algebra on a probability space. One proof first approximates continuous functions of finitely many bounded algebra entries by multivariate polynomials on their compact coordinate cube, and then approximates indicators and square-integrable functions. The coordinate polynomials lie in the algebra, and finite-coordinate measurable functions generate the full sigma algebra. Thus there is no moment-determinacy assumption.

The unbounded seed \(g_j\) belongs to \(H_1\): \(\tanh(g_j)\) is measurable there and the inverse \(\operatorname{arctanh}\) is measurable on \((-1,1)\); alternatively \(m\tanh(g_j/m)\to g_j\) in \(L^2\).

These subspaces reduce the initialized action in both directions. If \(v\in\mathcal D_1\),
\[
m\tanh(A_0v/m)\longrightarrow A_0v\quad\hbox{in }L^2_2,
\]
because the pointwise limit is \(A_0v\) and its absolute value is bounded by \(|A_0v|\). Hence \(A_0v\in H_2\), and density plus boundedness gives \(A_0H_1\subset H_2\). The identical argument gives \(A_0^*H_2\subset H_1\).

Let \(P_i\) be conditional expectation onto \(\mathcal F_i\), equivalently the orthogonal projection onto \(H_i\). The two inclusions imply
\[
P_2A_0=A_0P_1=P_2A_0P_1.                              \tag{3}
\]
For example, if \(x\perp H_1\) and \(y\in H_2\), then \(\langle A_0x,y\rangle=\langle x,A_0^*y\rangle=0\), which removes the other off-diagonal block.

## 3. Computable finite frames; no rank-decision oracle

At order \(N\), take finite initial segments \(v_{i,1},\ldots,v_{i,m_i}\) exhausting \(\mathcal D_i\). Let
\[
T_{i,N}a=\sum_{j=1}^{m_i}a_jv_{i,j},\qquad
G_{i,N}=T_{i,N}^*T_{i,N},\qquad \varepsilon_N=1/N.
\]
Define
\[
S_{i,N}=(G_{i,N}+\varepsilon_N I)^{-1/2},\qquad
U_{i,N}=T_{i,N}S_{i,N},\qquad P_{i,N}=U_{i,N}U_{i,N}^*.       \tag{4}
\]
All Gram entries are initial-word expectations. The inverse square root is taken of a strictly positive finite matrix. In particular, this construction never needs to decide whether a Gram determinant is exactly zero. Set \(e_{i,j}=U_{i,N}\mathbf e_j\); these are bounded initial functions, with bounds allowed to depend on \(N\).

The operators obey
\[
\|U_{i,N}\|\le1,\qquad 0\le P_{i,N}\le I,\qquad
P_{i,N}\longrightarrow P_i\quad\hbox{strongly}.             \tag{5}
\]
For the last statement, if \(h=T_{i,N}a\) is a fixed finite dictionary combination, spectral decomposition of \(G_{i,N}\) gives
\[
\|(I-P_{i,N})h\|_2^2
=\sum_\lambda \frac{\lambda\varepsilon_N^2}
                         {(\lambda+\varepsilon_N)^2}|a_\lambda|^2
\le \varepsilon_N\|a\|^2.
\]
For a fixed dictionary combination its coefficient vector can be padded by zeros as \(N\) grows, so the right side vanishes. Density and the contraction bound extend this to \(H_i\). Both sides vanish on \(H_i^\perp\), proving (5).

Precompute the finite contraction matrix
\[
B_N=U_{2,N}^*A_0U_{1,N},\qquad \|B_N\|\le2.                \tag{6}
\]
Equivalently, if \(C_{jk}=\mathbb E_2[v_{2,j}A_0v_{1,k}]\), then \(B_N=S_{2,N}C S_{1,N}\). Every entry uses finitely many initialized words, with \(A_0\) applied only to bounded words. Thus the initialized-word-law premise computes it.

The finite initialized action and its adjoint are
\[
A_{0,N}=U_{2,N}B_NU_{1,N}^*=P_{2,N}A_0P_{1,N},\qquad
A_{0,N}^*=P_{1,N}A_0^*P_{2,N}.                            \tag{7}
\]
From (3)–(5), these converge strongly to the actual actions on \(H_1,H_2\), respectively, and have norm at most two. Strong convergence here is asserted on the generated subspaces, not in operator norm on an infinite-dimensional ball.

The only mark laws retained by order \(N\) are the fixed finite-dimensional laws
\[
\xi=(g_1,g_2,e_{1,1},\ldots,e_{1,m_1}),\qquad
\eta=(e_{2,1},\ldots,e_{2,m_2}).                           \tag{8}
\]
They are the actual joint initial laws, not independent Gaussian replacements for their coordinates. Each has a finite Gaussian-conditioning construction by the supplied premise. All such conditioning is done in the initialization specification; runtime calls evaluate fixed finite-dimensional integrals against these fixed laws.

## 4. Explicit finite autonomous equations

Let
\[
C_0(t)=Y(e^{2t}-1),\qquad C=1+C_0(T),\qquad
\chi_C(s)=\max(-C,\min(C,s)).                             \tag{9}
\]
The clipping threshold is completely specified before evolution. It is not an order-dependent asymptotic cutoff.

The evolving finite state is
\[
a_N\in\mathbb R^{m_1\times2},\qquad
b_N\in\mathbb R^{m_2},\qquad
M_N\in\mathbb R^{m_2\times m_1},
\]
all initialized at zero. Suppressing \(N\) in the equations, define the population fields
\[
w_N(\xi)=g+a^Te_1(\xi),\qquad
c_N(\eta)=e_2(\eta)^Tb,
\]
and the observable-coefficient perturbation
\[
K_N=U_2MU_1^*,\qquad A_N=A_{0,N}+K_N=U_2(B+M)U_1^*.       \tag{10}
\]
For \(u\in S^1\), calculate
\[
\begin{aligned}
h_{1,N}(\xi,u)&=\tanh(w_N(\xi)\cdot u),\\
H(u)&=\mathbb E_1[e_1h_{1,N}(u)],\\
z_{2,N}(\eta,u)&=e_2(\eta)^T(B+M)H(u),\\
h_{2,N}(\eta,u)&=\tanh z_{2,N}(\eta,u),\\
d_{2,N}(\eta,u)&=\chi_C(c_N(\eta))(1-h_{2,N}(\eta,u)^2),\\
D(u)&=\mathbb E_2[e_2d_{2,N}(u)],\\
q_N(\xi,u)&=e_1(\xi)^T(B+M)^TD(u),\\
f_N(u)&=\mathbb E_2[c_Nh_{2,N}(u)],\qquad r_N(u,y)=f_N(u)-y.
\end{aligned}                                                            \tag{11}
\]
In particular, the forward and backward actions share one matrix and are actual Hilbert-space adjoints. The prediction uses the raw \(c_N\); only its backpropagated factor is clipped.

The ODE is
\[
\begin{aligned}
\dot a&=-2\int r_N(u,y)\,
       \mathbb E_1[e_1(1-h_{1,N}(u)^2)q_N(u)]u^T\,d\mu(u,y),\\
\dot b&=-2\int r_N(u,y)\,\mathbb E_2[e_2h_{2,N}(u)]\,d\mu(u,y),\\
\dot M&=-2\int r_N(u,y)\,D(u)H(u)^T\,d\mu(u,y).
\end{aligned}                                                            \tag{12}
\]
These are complete equations with no unclosed higher-order term. At any intermediate time, the current triple \((a,b,M)\), the fixed mark laws, and \(B\) determine the next derivative. Restarting from this state preserves the trajectory. No clock variable, path, stored response history, new feature, or operator query is added during evolution.

Equations (12) are equivalently projected field equations: the \(w\) and \(c\) derivatives are projected by \(P_{1,N},P_{2,N}\), and the Hilbert–Schmidt derivative is
\[
\dot K_N=-2\int r_N\,(P_{2,N}d_{2,N})\otimes(P_{1,N}h_{1,N})\,d\mu.          \tag{13}
\]
This follows directly from \(P_{i,N}=U_iU_i^*\); orthonormality of the frame is not assumed.

## 5. Finite-order well-posedness and uniform bounds

For each fixed \(N\), all \(e_{i,j}\) are bounded functions. Although \(g\) is unbounded, it enters through fixed initial marks and through \(\tanh(g+a^Te_1)\); variation in the finite coefficients has bounded derivatives on each bounded coefficient set. The clipping map is 1-Lipschitz. Thus the finite vector field is locally Lipschitz in \((a,b,M)\). This is the precise condition used for unique local ODE solutions.

The following coefficient estimates prevent finite-time escape. Since \(\|U_i\|\le1\),
\[
\|\dot b\|\le2(\|b\|+Y),\qquad \|b(t)\|\le C_0(t).                         \tag{14}
\]
Indeed \(|f_N|\le\|c_N\|_2\le\|b\|\), while \(\|U_2^*h_{2,N}\|\le1\). Also
\[
\|\dot M\|_F\le2(\|b\|+Y)C,
\qquad \|M(t)\|_F\le C C_0(t).                                           \tag{15}
\]
Here \(\|D\|\le\|d_{2,N}\|_2\le C\) and \(\|H\|\le1\). Consequently
\[
\|A_N(t)\|\le2+C C_0(t),\qquad
\|q_N(t,u)\|_2\le(2+C C_0(t))C.                                          \tag{16}
\]
Finally,
\[
\|a(t)\|_F\le 2C C_0(t)+\tfrac12 C^2C_0(t)^2.                            \tag{17}
\]
To verify (17), bound its derivative by
\(2(C_0(t)+Y)C(2+C C_0(t))\) and use \(C_0'=2(C_0+Y)\).
The bounds are independent of \(N\). A finite-dimensional locally Lipschitz ODE continues across every time at which its coefficient state stays bounded, so each solution exists through \(T\) (in fact for every finite time).

The canonical readout bound needed below also follows from its equation, independently of any interpretation of the supplied sharper bound:
\[
\|c(t)\|_2\le C_0(t),\qquad \|c(t)\|_\infty\le C_0(t).                    \tag{18}
\]
The first inequality follows by the same scalar Gronwall estimate. For the second, integrate the pointwise equation for \(c\) from zero and use \(|h_2|\le1\) and \(|r|\le C_0(s)+Y\). Hence \(\chi_C(c(t))=c(t)\) throughout the target interval. The clipping modification is therefore exact at the target and satisfies
\[
\|\chi_C(c_N)-c\|_2\le\|c_N-c\|_2.                                      \tag{19}
\]

## 6. The logarithmic product estimate

This is the step replacing the invalid assertion that multiplication is Lipschitz in a common \(L^2\) norm.

Let \(s(x)=1-\tanh^2x\). It has absolute value at most one and Lipschitz constant at most two. If \(q\) obeys (1) and \(\|x-x'\|_2\le\delta\), then for every \(R\ge0\)
\[
\|(s(x)-s(x'))q\|_2
\le2R\delta+Qe^{-\kappa R}.                                               \tag{20}
\]
This splits the product into \(|q|\le R\), where the Lipschitz estimate applies, and its complement, where \(|s(x)-s(x')|\le1\). For small positive \(\delta\), choosing \(R=\kappa^{-1}\log(Q/\delta)\) gives
\[
\|(s(x)-s(x'))q\|_2\le C_1\delta\log(eL/\delta).                           \tag{21}
\]
Here \(L\) can be any fixed sufficiently large bound on the errors and tail constants, with a corresponding fixed \(C_1\). The zero-error case is exact. Larger errors can be absorbed by enlarging the constant. On \([0,L]\), write
\[
\rho(\delta)=\delta\log(eL/\delta),\quad \rho(0)=0.
\]
This function is increasing and satisfies
\[
\int_{0+}\frac{d\delta}{\rho(\delta)}=\infty.                              \tag{22}
\]
Only the true \(q\) needs the tail bound. Approximate \(q_N\) is never placed in the tail term. Neither exponential integrability of \(w_N\) nor any same-norm multiplication rule is used.

## 7. The actual reached trajectory belongs to the word spaces

This step is needed: density in the word-generated subspace would not by itself show density along the actual trajectory.

Project the true state by
\[
\bar w=P_1w,\qquad \bar c=P_2c,\qquad \bar K=P_2KP_1.
\]
Conditional expectation gives \(\|\bar c\|_\infty\le\|c\|_\infty\). By (3), every field calculated from the projected state is measurable in its corresponding \(\mathcal F_i\), and its vector-field value lies in
\[
H_1^2\times H_2\times\mathrm{HS}(H_1,H_2).                               \tag{23}
\]
The initial projection error is zero.

The difference of the original vector fields at the true and projected states is bounded by a constant times \(\rho(E)\), where
\[
E=\|w-\bar w\|_2+\|c-\bar c\|_2+\|K-\bar K\|_{\mathrm{HS}}.
\]
Here are the substantive estimates. Forward differences obey
\(\|\delta h_1\|_2\le\|\delta w\|_2\) and
\(\|\delta z_2\|_2\le C_2(\|\delta w\|_2+\|\delta K\|_{\mathrm{HS}})\).
Bounded readouts and bounded tanh give
\(\|\delta d_2\|_2\le\|\delta c\|_2+2C\|\delta z_2\|_2\), and boundedness of the operators gives \(\|\delta q\|_2\le C_3E\). The first backward factor is split in the order
\[
s(\bar z_1)\bar q-s(z_1)q
=s(\bar z_1)(\bar q-q)+(s(\bar z_1)-s(z_1))q.                              \tag{24}
\]
The first term is bounded in \(L^2\) by \(\|\bar q-q\|_2\); (21) bounds the second. Residual differences are linear in \(E\), since the true readout is bounded. Rank-one tensor differences obey
\(\|a\otimes b-a'\otimes b'\|_{\mathrm{HS}}
 \le\|a-a'\|_2\|b\|_2+\|a'\|_2\|b-b'\|_2\).
These estimates prove the stated vector-field bound after integration over \(\mu\).

Taking the orthogonal-complement components of the true strong-flow equation, and subtracting the zero complementary component of the projected-state vector field, gives
\[
E(t)\le C_4\int_0^t\rho(E(s))\,ds.                                      \tag{25}
\]
To see why this forces \(E=0\), replace the right-side initial value by \(a>0\). The scalar comparison equation \(v'=C_4v\log(eL/v)\), \(v(0)=a\), has
\[
v(t)=eL\exp\{-\log(eL/a)e^{-C_4t}\}.
\]
For a fixed finite horizon this tends to zero as \(a\downarrow0\). Scalar integral comparison gives \(E\le v\), then \(E=0\). This is the needed Osgood uniqueness argument, derived here rather than assumed for arbitrary ambient states.

Thus the reached \(w,c,K\) lie in (23). No predictive-sufficiency assertion about arbitrary nonreached hierarchy states is needed.

## 8. Consistency and convergence

Let
\[
E_N(t)=\|w_N(t)-w(t)\|_2+\|c_N(t)-c(t)\|_2
                                  +\|K_N(t)-K(t)\|_{\mathrm{HS}}.
\]
All these errors are bounded independently of \(N\) on \([0,T]\). The initialized action errors needed in the comparison are
\[
\alpha_N(t)=\sup_{u\in S^1}\bigl(
 \|(A_{0,N}-A_0)h_1(t,u)\|_2+
 \|(A_{0,N}^*-A_0^*)d_2(t,u)\|_2\bigr).                                  \tag{26}
\]
They tend to zero uniformly in time. Indeed \((t,u)\mapsto h_1(t,u)\) is continuous in \(L^2_1\), by strong continuity of \(w\) and the tanh Lipschitz bound. The analogous map to \(d_2\) is continuous in \(L^2_2\), by (18), the Lipschitz nonlinearities, and operator-norm continuity of \(K\), which follows from its Hilbert–Schmidt continuity. Their images of the compact set \([0,T]\times S^1\) are compact. Uniformly bounded operators converging strongly converge uniformly on a compact set: cover it by a finite \(\epsilon\)-net, use pointwise convergence on the net, and use the uniform operator bound on the remainder. Apply this fact to (7).

The remaining consistency terms are
\[
\beta_N(t)=\|(I-P_{1,N})\dot w(t)\|_2
 +\|(I-P_{2,N})\dot c(t)\|_2
 +\|\dot K(t)-P_{2,N}\dot K(t)P_{1,N}\|_{\mathrm{HS}}.                     \tag{27}
\]
They tend to zero in \(L^1([0,T])\). For almost every time the derivatives belong to (23), so strong convergence of the projections gives the first two limits. For the Hilbert–Schmidt term, first verify convergence on a rank-one operator by the rank-one norm identity, extend to finite rank, and then use density of finite-rank operators in Hilbert–Schmidt norm and the contraction bounds. The true derivatives have an integrable norm majorant from the strong equation, the readout bound, and the uniform \(L^2\) bound on \(q\); dominated convergence now applies. No continuity of the derivatives is needed.

For completeness, the approximate-versus-true field comparison is as follows, uniformly over \(u\):
\[
\begin{aligned}
\|h_{1,N}-h_1\|_2&\le E_N,\\
\|z_{2,N}-z_2\|_2&\le C_5E_N+\alpha_N,\\
\|d_{2,N}-d_2\|_2&\le C_6E_N+2C\alpha_N,\\
\|q_N-q\|_2&\le C_7(E_N+\alpha_N),\\
|f_N-f|&\le\|c_N-c\|_2+C_0(T)\|h_{2,N}-h_2\|_2
                    \le C_8(E_N+\alpha_N).
\end{aligned}                                                            \tag{28}
\]
The third inequality uses (19). The fourth uses the actual adjoint and splits the action error on the **true** \(d_2\). For the last line, write
\(f_N-f=\langle c_N-c,h_{2,N}\rangle+\langle c,h_{2,N}-h_2\rangle\).
For \(d_1\), the decomposition (24), now with \(N\) in place of the bar, gives
\[
\|d_{1,N}-d_1\|_2\le C_9\rho(E_N)+C_{10}\alpha_N.                         \tag{29}
\]
Combining (12)–(13), (27)–(29), and the rank-one tensor estimate yields
\[
E_N(t)\le a_N+C_{11}\int_0^t\rho(E_N(s))\,ds,
\qquad
a_N=C_{12}\int_0^T(\alpha_N(s)+\beta_N(s))\,ds\longrightarrow0.            \tag{30}
\]
The initial error is zero because \(w_N(0)=g\), \(c_N(0)=0\), and \(K_N(0)=0\). The same explicit scalar comparison used after (25) gives
\[
\sup_{t\le T}E_N(t)\longrightarrow0.                                     \tag{31}
\]
This proves (2). In particular, there is a vanishing truncation source as well as a stability estimate; neither is being substituted for the other.

## 9. Prediction and joint-word guarantees

From (26), (28), and (31),
\[
\sup_{t\le T}\sup_{u\in S^1}|f_N(t,u)-f(t,u)|\longrightarrow0.             \tag{32}
\]
No input quadrature or dense-input interpolation is involved in this whole-circle assertion.

For word observations, retain the exact initial Gaussian seed \(g\) in (8), use \(w_N,c_N\) for current raw seeds, and replace initialized/current actions by \(A_{0,N},A_N\), with their actual adjoints. For example, the approximate initialized field is
\[
z_{20,N}(v)=A_{0,N}\tanh(g\cdot v).
\]
It is evaluated by the same fixed \(B_N\) used in the current action. It is not independently resampled.

Every separately fixed finite word converges in \(L^2\), uniformly in \(t\), by induction over its expression:

1. The raw seeds converge by (31); the initial Gaussian seed is exact.
2. Affine operations and the Lipschitz nonlinearities preserve the convergence.
3. Products of uniformly bounded factors preserve \(L^2\) convergence by the telescoping product identity. If a permitted product has one unbounded \(L^2\) factor and bounded factors, write the difference as the strong \(L^2\) error times a bounded multiplier plus the fixed limiting \(L^2\) factor times a bounded multiplier tending to zero in probability. Truncating the fixed factor proves the second term tends to zero. No multiplication theorem for arbitrary \(L^2\) factors is claimed.
4. For a bounded first-population word \(v_N(t)\to v(t)\),
   \[
   \|A_Nv_N-Av\|_2\le \|A_N\|\|v_N-v\|_2
      +\|(A_{0,N}-A_0)v\|_2+\|K_N-K\|_{\mathrm{HS}}\|v\|_2.
   \]
   The true finite word path \(v(t)\) is continuous in \(L^2\), so its image is compact; strong convergence of the initialized actions is uniform on that image. The identical estimate handles the adjoint direction and initialized actions.

For any fixed tuple \(V=(V_1,\ldots,V_k)\) whose entries are on the same population space, the natural common-space coupling gives
\[
W_2(\operatorname{Law}(V_N(t)),\operatorname{Law}(V(t)))^2
 \le\sum_{j=1}^k\|V_{j,N}(t)-V_j(t)\|_2^2.                               \tag{33}
\]
This proves the required uniform-time joint-law convergence, including tuples mixing initial and current words. The two population spaces do not by themselves specify a cross-population pointwise coupling; if a tuple means independent samples from the two populations, use their product coupling and (33). A different cross-population coupling would have to be specified by the scientific input.

The quantifier is “for every fixed tuple, as \(N\to\infty\).” No finite order is asserted to resolve all words, all word lengths, or all action queries at once.

## 10. Non-vacuity and hostile checks

| Attack | Check and consequence |
|---|---|
| Future replay or hidden history | The dictionary and all Gram/action coefficients use time-zero words only. The finite state is exactly \((a,b,M)\); (12) is autonomous. No future trajectory enters initialization. |
| Disguised original middle matrix | \(M\) indexes fixed observable features, with initial contraction matrix (6), and does not index neurons. There is no sampled finite neural network or ambient width. Its admissibility relies on the prompt's explicit allowance for observable coefficient matrices. |
| Arbitrary action oracle | At fixed \(N\), only the finitely many contractions in (6) are used. Every runtime action is (10), and its reverse is its transpose. The infinite dictionary is an order-indexed specification, not a runtime service. |
| Hidden full parameter density | The state has finitely many real coefficients and fixed finite-dimensional mark laws supplied by finite initialized-word recipes. There is no evolving density of \((w,c,A)\) and no field over a neuron-pair index representing the full operator. |
| Lost Gaussian response correlations | The mark law and contractions must be the supplied complete joint initial law, including response correction. Independently sampling purported Gaussian coordinates would invalidate the construction. |
| Exact Gram-rank decision | Ridge normalization (4) avoids a noncomputable zero-eigenvalue decision. Duplicate or zero features cause no singularity. |
| Loss of the pointwise readout bound under projection | This is real for arbitrary finite frames. The explicit fixed clipping in \(d_{2,N}\), together with (18)–(19), repairs the necessary estimate. Raw predictions still use \(c_N\). |
| Unresolved cutoff | There is no cutoff limit. \(C=1+Y(e^{2T}-1)\) is fixed, and the true flow lies strictly inside its identity region. If the admissible runtime language disallows any explicitly specified Lipschitz clipping map, that would be an additional representation restriction on this witness. |
| Approximate backward tails may escape | No approximate tail bound is used. The decomposition (24) places only the true \(q\) in the nonlinear product-tail term. |
| Uniform boundedness mistaken for compactness | Compactness is invoked only for continuous images of \([0,T]\times S^1\) or \([0,T]\) along the reached true state, never for an ambient norm ball. |
| Word space may omit the actual trajectory | Section 7 proves invariance using the actual tail estimate and zero-error Osgood uniqueness. It does not assume full hierarchy sufficiency off the reached set. |
| High modes feed low modes | The resulting source is explicitly (26)–(27); it vanishes along compact reached families and in time-integrated derivative norm. Nonlinear propagation is controlled by (30). |
| Wrong product topology | Section 6 handles the only unbounded backward multiplier. Word products require their stated boundedness; no generic \(L^2\) algebra claim is used. |
| Quantifier inversion | The dictionary, ridge schedule, and clipping constant are fixed from the model and horizon, before any law's future trajectory is known. The proof is for every law in the given ball. |
| Time regularity assumption smuggled in | Strong flow and \(L^2\)-continuous finite-word operations suffice; derivative projection consistency uses dominated convergence in time. There is no temporal power series or analyticity argument. |
| Failure of moments to determine laws | Initialization uses complete finite joint laws, and the final comparison uses an explicit \(L^2\) coupling. No Stieltjes or moment-determinacy argument appears. |

## 11. Claim status and supplied-input limits

| Claim | Rung | Status and dependency |
|---|---|---|
| Explicit finite equations (12) with actual adjoint | A | Derived exactly from the frame definitions. |
| Finite-order uniqueness and continuation | B | Proved using bounded features, locally Lipschitz coefficients, and (14)–(17). |
| Initialized coefficients have permitted provenance | A | Follows from the supplied finite initialized-word-law premise. The prompt does not contain its Gaussian-conditioning formulas, so this route does not independently rederive or implement that premise. |
| Reached-state word-space invariance | D/E bridge | Proved in Section 7 using the supplied canonical backward-tail estimate. |
| State convergence on the stated horizon | D/E | Proved conditionally on the supplied strong-flow and tail premises, by the explicit consistency sources and Osgood comparison. |
| Whole-circle predictions and fixed finite joint words | D/E | Proved consequences of state convergence and paired actions. |
| Uniformity over the entire law ball | Stronger claim | Not claimed. Pointwise-in-law convergence uses the same construction; a supremum-over-laws rate would require uniform tail constants and compactness/approximation control across the law family. |
| Practical rate or moderate complexity | Stronger claim | Open. The strong-convergence source has no quantitative rate from the prompt, and the initial word dictionaries may be very large. |
| Absolute admissibility under an unstated ban on all finite operator coefficient matrices or on clipping | Contract issue | Not resolvable from a stricter interpretation absent from the supplied prompt. Under the explicit observable-contraction-matrix allowance, the construction is within the stated class. |

No independent numerical evidence is claimed. The missing scientific implementation input is the explicit finite Gaussian-conditioning/response-correction algorithm for the selected initial words; its existence and computability were given as a premise. The proof does not require fetching additional research results. The highest-value independent check is to audit the admissibility of the static observable-frame matrix representation and the projected-state Osgood invariance argument; all later convergence claims depend on those two points.
