# Observable geometry: exact responses, missing information, and closure cost

This is an independent, prompt-only theory route. Its inputs are the model and requested scope supplied by the supervisor; no book, other study, or literature was consulted. The precise positive-Gram and small-label hypotheses of the existing compression theorem were not supplied. Consequently, the exact identities and counterexample below are unconditional statements about the stated flow; the approximation statements explicitly list additional hypotheses. None is a promotion claim.

The main conclusion is constructive at the level of mechanism: the first missing information is a Gram matrix of **activation times sensitivity** landmarks. Ordinary activation, preactivation, readout, and initial velocity Grams do not determine it. Adding these landmarks repairs the first missing response, but a generic finite truncation then needs successively higher directional responses. An exact finite multiplication algebra is a different, stronger construction than simply retaining triple moments.

## 1. Model, metric, and label forces

Let \(a=1,\ldots,m\) index training examples, and allow additional indices for a fixed passive validation panel. All driving sums below run only over the training indices. Inputs are \(x_a\in\mathbb R^d\), the hidden width is \(n\), and there are \(L\) hidden layers. Define

\[
\begin{aligned}
z_a^{(1)}&=Ax_a/\sqrt d,&h_a^{(1)}&=\phi(z_a^{(1)}),\\
z_a^{(\ell)}&=W^{(\ell)}h_a^{(\ell-1)},&
h_a^{(\ell)}&=\phi(z_a^{(\ell)}),\qquad 2\leq\ell\leq L,\\
f_a&=n^{-1}w^\top h_a^{(L)},&r_a&=f_a-y_a,\qquad a\leq m,\\
\mathcal L&=m^{-1}\sum_{a=1}^m r_a^2.
\end{aligned}
\]

Here \(A\in\mathbb R^{n\times d}\), \(W^{(\ell)}\in\mathbb R^{n\times n}\), and \(w\in\mathbb R^n\). The activation acts componentwise. The stipulated initialization has independent Gaussian entries with variances \(1\) for \(A\), \(1/n\) for the hidden matrices, and \(w(0)=0\). Define the backward signals by

\[
\delta_a^{(L)}=w\odot\phi'(z_a^{(L)}),\qquad
\delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot
W^{(\ell+1)\top}\delta_a^{(\ell+1)}.
\]

The physical dynamics are exactly

\[
\begin{aligned}
\dot A&=-\frac2m\sum_{b=1}^m r_b\delta_b^{(1)}x_b^\top/\sqrt d,\\
\dot W^{(\ell)}&=-\frac{2}{mn}\sum_{b=1}^m
r_b\delta_b^{(\ell)}h_b^{(\ell-1)\top},\\
\dot w&=-\frac2m\sum_{b=1}^m r_bh_b^{(L)}.
\end{aligned}
\]

To expose their geometry without changing their mobilities, stack the entries of

\[
\xi=(A/\sqrt n,W^{(2)},\ldots,W^{(L)},w/\sqrt n)
\]

into a Euclidean vector. For an evaluated example \(a\), define the vector field \(g_a(\xi)=\nabla_\xi f_a(\xi)\), and define its directional derivative on a scalar or vector observable \(O\) by

\[
D_aO(\xi)=\mathrm dO(\xi)[g_a(\xi)].
\]

Then

\[
\dot\xi=-\frac2m\sum_{b=1}^m r_bg_b,
\qquad
\dot O=-\frac2m\sum_{b=1}^m r_bD_bO.
\tag{1}
\]

For example, in the original coordinates, \(D_bA=\delta_b^{(1)}x_b^\top/\sqrt d\), \(D_bW^{(\ell)}=\delta_b^{(\ell)}h_b^{(\ell-1)\top}/n\), and \(D_bw=h_b^{(L)}\). Thus \(D_b\) is a response per unit label force, not a physical velocity with its residual factor removed by division. It remains well defined at zero residual.

Define the normalized input, activation, and backward Gram matrices by

\[
Q_{ab}=d^{-1}x_a^\top x_b,\qquad
G_{ab}^{(\ell)}=n^{-1}h_a^{(\ell)\top}h_b^{(\ell)},\qquad
B_{ab}^{(\ell)}=n^{-1}\delta_a^{(\ell)\top}\delta_b^{(\ell)}.
\]

Taking inner products of the three parameter blocks of \(g_a\) gives the exact force kernel

\[
K_{ab}=\langle g_a,g_b\rangle
=G_{ab}^{(L)}+Q_{ab}B_{ab}^{(1)}
+\sum_{\ell=2}^L G_{ab}^{(\ell-1)}B_{ab}^{(\ell)}.
\tag{2}
\]

Consequently,

\[
\dot f_a=-\frac2m\sum_{b=1}^mK_{ab}r_b,
\qquad
\dot{\mathcal L}=-\frac4{m^2}r^\top K_{\rm tr}r=-\|\dot\xi\|^2.
\tag{3}
\]

Here \(K_{\rm tr}\) is the training-by-training block. It is positive semidefinite because it is a gradient Gram matrix. Validation rows use the same force fields and do not add labels or forces. Equations (2)–(3) expose how labels act, but do not close the evolution of the Gram matrices.

## 2. Exact feature motion and acceleration

For an evaluated example \(a\) and a driving example \(b\), define the feature response \(R_{ab}^{(\ell)}=D_bh_a^{(\ell)}\in\mathbb R^n\). The forward derivative recursion is

\[
\begin{aligned}
R_{ab}^{(1)}&=\phi'(z_a^{(1)})\odot\delta_b^{(1)}Q_{ab},\\
R_{ab}^{(\ell)}&=\phi'(z_a^{(\ell)})\odot
\left(\delta_b^{(\ell)}G_{ab}^{(\ell-1)}
+W^{(\ell)}R_{ab}^{(\ell-1)}\right),\quad \ell\geq2.
\end{aligned}
\tag{4}
\]

The first term is the current layer's direct weight write; the second transports the preceding layer's feature motion. The gates \(\phi'(z_a^{(\ell)})\) select which coordinates transmit either effect. The order of evaluation is unambiguous: compute the forward pass and backward signals, then (4) from layer 1 upward. This is an exact evaluation rule from the dense state, not yet a compressed stored-state equation.

Substitution into the time derivative of a feature Gram gives

\[
\dot G_{ab}^{(\ell)}
=-\frac2m\sum_{c=1}^m r_c\left[
\frac1nR_{ac}^{(\ell)\top}h_b^{(\ell)}
+\frac1nh_a^{(\ell)\top}R_{bc}^{(\ell)}\right].
\tag{5}
\]

Thus the next aggregate is a pairing of a position with a directionally driven displacement. It retains three distinct example roles. Neither the response vectors nor their pairings may be symmetrized in the evaluated and driving indices.

For comparison with purely kinematic descriptions, put \(v_a^{(\ell)}=\dot h_a^{(\ell)}\) and \(\alpha_a^{(\ell)}=\ddot h_a^{(\ell)}\). For a fixed layer, define

\[
P_{ab}=n^{-1}h_a^\top v_b,\qquad
V_{ab}=n^{-1}v_a^\top v_b,\qquad
E_{ab}=n^{-1}h_a^\top\alpha_b.
\]

Differentiating gives

\[
\dot G=P+P^\top,\qquad
\dot P=V+E,\qquad
\dot V_{ab}=n^{-1}(\alpha_a^\top v_b+v_a^\top\alpha_b).
\tag{6}
\]

These are useful position–velocity–acceleration identities. They do not determine the accelerations, and differentiating their new pairings introduces higher derivatives. Equation (4) identifies the force and gate information hidden by (6).

There is a parallel scalar description of the curvature of the parameter trajectory. Define

\[
C_{a;bc}=\nabla_\xi^2f_a[g_b,g_c],
\]

which is symmetric in \(b,c\). The derivative of the kernel is

\[
\dot K_{ab}=-\frac2m\sum_{c=1}^m r_c(C_{a;bc}+C_{b;ac}).
\tag{7}
\]

Indeed, differentiating \(\langle g_a,g_b\rangle\) in direction \(g_c\) differentiates each of its two vectors once. If all indices below are training indices, the output acceleration is therefore

\[
\ddot f_a=\frac4{m^2}\left[
(K_{\rm tr}^2r)_a+
\sum_{b,c=1}^m r_br_c(C_{a;bc}+C_{b;ac})\right].
\tag{8}
\]

The first term comes from changing residuals; the second comes from changing the feature geometry. The corresponding parameter acceleration is

\[
\ddot\xi=\frac4{m^2}\left[
\sum_{b=1}^m(K_{\rm tr}r)_bg_b+
\sum_{b,c=1}^m r_br_c\nabla_\xi^2f_b\,g_c\right].
\]

Equations (4)–(8) give mechanisms beyond the kernel identity while displaying their unresolved information explicitly.

## 3. The first information lost by pairwise Grams

The obstruction already occurs with one hidden layer. In this section all quantities on the right of an initialization formula are evaluated at time zero. Write \(h_a=\phi(z_a)\) and \(p_a=\phi'(z_a)\). Since \(w(0)=0\),

\[
K(0)=G(0),\qquad \dot K(0)=0,\qquad
\dot h_a(0)=0,\qquad
\dot w(0)=\frac2m\sum_cy_ch_c.
\]

Differentiate \(\dot z_a=-(2/m)\sum_c r_cQ_{ac}w\odot p_c\). Terms containing \(w(0)\) vanish, leaving

\[
\ddot h_a(0)=\frac4{m^2}
\left(\sum_cy_ch_c\right)\odot p_a\odot
\left(\sum_dQ_{ad}y_dp_d\right).
\tag{9}
\]

Define the mixed activation–sensitivity tensor

\[
\mathcal M_{bc;ad}
=\frac1n\sum_{i=1}^n h_{b,i}h_{c,i}p_{a,i}p_{d,i}.
\tag{10}
\]

For one hidden layer, \(K_{ab}=G_{ab}+Q_{ab}n^{-1}\sum_iw_i^2p_{a,i}p_{b,i}\). Its second derivative at initialization therefore has three sources: the acceleration of \(h_a\), the acceleration of \(h_b\), and the squared readout velocity. Substituting (9) yields

\[
\ddot K_{ab}(0)=\frac4{m^2}\sum_{c,d}y_cy_d
\left[
Q_{ad}\mathcal M_{bc;ad}
+Q_{bd}\mathcal M_{ac;bd}
+2Q_{ab}\mathcal M_{cd;ab}
\right].
\tag{11}
\]

Since \(r(0)=-y\), (3) now gives the first three output derivatives:

\[
\dot f(0)=\frac2mGy,\qquad
\ddot f(0)=-\frac4{m^2}G^2y,\qquad
f^{(3)}(0)=\frac8{m^3}G^3y+\frac2m\ddot K(0)y.
\tag{12}
\]

The nonlinear, label-cubic part of (12) depends on (10). For a single normalized training input, this reduces to

\[
f^{(3)}(0)=8yG^3+32y^3\frac1n\sum_i\phi(z_i)^2\phi'(z_i)^2.
\]

This is a concrete first missing susceptibility, rather than an appeal to an unspecified higher-order kernel.

### A signed two-label counterexample

Take \(L=1\), \(\phi=\sin\), \(m=2\), \(d=2\), \(x_1=\sqrt2e_1\), and \(x_2=\sqrt2e_2\), so \(Q=I_2\). Let \(n=8\), choose \(0<a<1\), and choose the labels \(y=(\eta,-\eta)\) with arbitrarily small \(\eta\ne0\). The two initialization configurations have the following feature vectors:

\[
\begin{array}{c|c|c}
&h_1&h_2\\ \hline
\mathrm A&(a,a,-a,-a,0,0,0,0)&(0,0,0,0,a,a,-a,-a)\\
\mathrm B&(a,a,-a,-a,0,0,0,0)&(a,-a,a,-a,0,0,0,0).
\end{array}
\]

Set \(z_b=\arcsin(h_b)\) componentwise, take the columns of \(A\) to be \(z_1,z_2\), and set \(w=0\). Both configurations have

\[
G=\frac{a^2}{2}I_2.
\]

Moreover, \(z_b=(\arcsin(a)/a)h_b\). Initial hidden velocities vanish, and \(\dot w=\eta(h_1-h_2)\). Hence **every pairwise inner product among the preactivation vectors, activation vectors, readout, and their initial physical velocities agrees** between the two configurations. The outputs, their first and second derivatives, and \(K,\dot K\) also agree.

Nevertheless, because \(p_b^2=1-h_b^2\),

\[
\frac1n\sum_i h_{2,i}^2p_{1,i}^2
=\begin{cases}
a^2/2,&\mathrm A,\\
a^2(1-a^2)/2,&\mathrm B.
\end{cases}
\]

The self-susceptibilities agree, all the cross terms containing \(h_1h_2p_b^2\) vanish, and the analogous expression with samples 1 and 2 exchanged has the same difference. Substitution into (11)–(12) gives

\[
f_{\mathrm B}^{(3)}(0)-f_{\mathrm A}^{(3)}(0)
=-2\eta^3a^4(1,-1).
\tag{13}
\]

Thus no deterministic autonomous state consisting only of these pairwise Grams and the labels can reproduce both exact trajectories: it starts from the same reduced state but would have to produce different third derivatives. The Gram is strictly positive, and the labels may be as small as desired. Replicating the eight-neuron blocks preserves all normalized identities.

The two configurations lie in the support of the stipulated Gaussian initialization. They are not asserted to be typical Gaussian draws; exact configurations have probability zero. Equation (13) therefore establishes failure of universal exact Gram closure, **not** a lower bound ruling out high-probability accuracy of order \(n^{-1/2}\). A probabilistic impossibility result would need a conditional fluctuation argument at the target scale. Also, a larger Gram state containing derivative-feature vectors can distinguish this particular example; (13) does not prove that every finite augmented Gram state fails.

## 4. Semantic landmarks repair the first defect

For the one-layer calculation, define the activation–sensitivity landmark

\[
\psi_{ab}=p_a\odot h_b\in\mathbb R^n.
\]

Then the missing tensor is itself a Gram matrix:

\[
\mathcal M_{bc;ad}=n^{-1}\psi_{ab}^\top\psi_{dc}.
\tag{14}
\]

There are \(m^2\) such landmarks and at most \(m^4\) scalar pairings. The interpretation is direct: a feature of sample \(b\) is measured only in coordinates where sample \(a\) remains sensitive. Configuration A separates the two samples into disjoint active coordinates; configuration B uses the same active coordinates with cancelling signs. An ordinary Gram sees the sign cancellation in both, while (14) detects the different sensitive-coordinate overlap.

The exact derivative of this new landmark shows what is needed next. From \(D_ez_a=Q_{ae}w\odot p_e\),

\[
D_e\psi_{ab}
=w\odot p_e\odot
\left[Q_{ae}\phi''(z_a)\odot h_b+Q_{be}p_a\odot p_b\right].
\tag{15}
\]

Thus the Gram derivative of (14) requires cross pairings with the landmarks in (15). Further differentiation adds higher activation derivatives and products. This is an exact account of the hierarchy; it is not a theorem that the hierarchy cannot have special algebraic relations.

In particular, retaining an arbitrary finite set of triple moments does not by itself specify all these products. A **finite associative multiplication algebra**, with a specified identity and an exact rule for multiplying every pair of represented functions, is stronger. If all the relevant feature functions, gates, products, and layer transports remain in that algebra, the extra moments are reconstructible and the hierarchy closes. The information supplied by the multiplication table is precisely what the counterexample says an ordinary Gram omits. Whether such an algebra is a further scientific reduction, or an exact change of coordinates of an already compressed finite network, depends on its dimension and its construction; these must be disclosed.

## 5. An exact scalar response hierarchy and its finite truncation

Let \(O\) range over a finite requested list of scalar observables: outputs on the training and passive panel, layer Grams, or kernel entries. For a word \(w=(b_1,\ldots,b_k)\) of training indices, define

\[
C_{O,w}(\xi)=D_{b_1}\cdots D_{b_k}O(\xi),
\qquad C_{O,\varnothing}=O.
\]

The operator nearest \(O\) acts first. If \(bw\) denotes prepending \(b\) to the word, (1) gives the exact infinite hierarchy

\[
\dot C_{O,w}=-\frac2m\sum_{b=1}^m r_bC_{O,bw},
\qquad
r_a=C_{f_a,\varnothing}-y_a.
\tag{16}
\]

Each coordinate has a defined interpretation as an ordered sample response of a named observable. There are no residual denominators. Initialize every coordinate by evaluating its displayed derivative at the given initialized network. A finite order-\(q\) approximation evolves (16) for \(|w|<q\) and holds the \(|w|=q\) coordinates at their initial values. This is an autonomous scalar ODE, with no live dense weights and no trajectory data imported after initialization. The approximation first occurs when the last equation is frozen.

The word ordering is needed. At \(w=0\) in a one-layer network,

\[
[g_b,g_c]z_a
=Q_{ac}\phi(z_b)\odot\phi'(z_c)
-Q_{ab}\phi(z_c)\odot\phi'(z_b),
\qquad [g_b,g_c]w=0,
\tag{17}
\]

where \([g_b,g_c]O=D_bD_cO-D_cD_bO\). For two orthogonal inputs, these expressions are generically nonzero. Different orders of label forcing can therefore move the hidden features differently. Storing only the integrated residuals does not provide a general controlled-state description. Equation (17) is not an impossibility theorem for a larger reduced state, nor for the particular feedback-controlled path at fixed labels.

If there are \(P\) base observables, the direct order-\(q\) construction stores

\[
P\sum_{k=0}^{q-1}m^k\quad\text{moving scalars},\qquad
Pm^q\quad\text{fixed highest-order coefficients},
\tag{18}
\]

before symmetry reductions. All their initialization data come from the initialized dense network. Differentiating that network to order \(q\) may itself be expensive, even though subsequent evolution is aggregate-only. For fixed \(m>1\), geometric convergence requiring \(q\asymp\log n\) gives \(m^q\), a power of \(n\), rather than a power of \(\log n\). A polynomial-in-order semantic representation needs additional algebraic structure. Merely calling (16) an observable model does not meet the requested polylogarithmic state bound.

### What would suffice for all-time accuracy

Here is a precise useful stability statement, separating the approximation error from the missing analytic and coercivity estimates. Let \(r\) be the exact training residual and \(\widehat r\) that of an approximate autonomous aggregate model, with the same initial residual. Suppose both solve residual equations of form (3), the exact kernel obeys \(K_{\rm tr}(t)\succeq\kappa I\), and

\[
\int_0^\infty\|\widehat r(t)\|\,dt\leq R_*.
\]

Suppose their kernel discrepancy has been proved to satisfy

\[
\|K_{\rm tr}(t)-\widehat K_{\rm tr}(t)\|
\leq\varepsilon+L_*\int_0^t\|r(s)-\widehat r(s)\|\,ds.
\tag{19}
\]

Writing \(E(t)=\int_0^t\|r-\widehat r\|\), variation of constants for the dissipative exact residual equation gives

\[
E(t)\leq\frac1\kappa\int_0^t
\left(\varepsilon+L_*E(s)\right)\|\widehat r(s)\|\,ds.
\]

The scalar integral inequality, obtained by differentiating its right-hand side and integrating the resulting first-order bound, implies

\[
E(\infty)\leq
\frac{\varepsilon R_*}{\kappa}
\exp\left(\frac{L_*R_*}{\kappa}\right).
\tag{20}
\]

For example, \(\widehat K_{\rm tr}\succeq\widehat\kappa I\) implies \(R_*\leq m\|y\|/(2\widehat\kappa)\). If a validation or Gram observable discrepancy has the analogous bound \(\varepsilon_O+L_OE(t)\), (20) supplies an all-time bound for it as well. Thus infinite physical time need not require infinitely many response orders: the relevant quantity is the finite total residual forcing.

For a prescribed control \(du_b=-(2/m)r_b\,dt\), an elementary iterated fundamental-theorem-of-calculus expansion explains a sufficient geometric error estimate. Suppose all length-\(k\) ordered derivatives needed for the remainder obey

\[
\sup_{\text{reachable states}}|D_{b_1}\cdots D_{b_k}O|
\leq M k!R^{-k},
\]

and the total absolute control variation is \(\Gamma=\sum_b\int|du_b|<R\). The sum of the absolute values of all length-\(k\) iterated-control integrals is at most \(\Gamma^k/k!\); hence the order-\(q\) remainder is at most \(M(\Gamma/R)^{q+1}\). Uniform Lipschitz dependence on the accumulated control discrepancy then gives a bound of the form (19).

These are sufficient hypotheses, not consequences proved here for arbitrary fixed depth and the full stated activation class. Establishing radius and Lipschitz constants uniform at the required dense scale, maintaining the reduced kernel lower bound, and reducing (18) to a polynomial in \(q\) remain separate obligations.

## 6. One-control case and scope of the result

With one training example there is an exact simplification at every depth. Let \(\Phi(s)\) solve \(\Phi'(s)=g_1(\Phi(s))\), \(\Phi(0)=\xi(0)\), and define \(F(s)=f_1(\Phi(s))\). The full training path is exactly

\[
\xi(t)=\Phi(s(t)),\qquad
\dot s=2\bigl(y-F(s)\bigr),\qquad s(0)=0.
\]

Every passive validation or Gram observable is a univariate function \(O(\Phi(s))\), and \(F'(s)=K_{11}(\Phi(s))\). On an interval containing the trajectory, a positive lower bound for this derivative and a uniform analytic radius make polynomial approximation a genuine scalar autonomous closure. An error \(\varepsilon\) in the function produces a uniformly bounded clock error through scalar contraction; approximating the other univariate observables then gives their all-time error. Initial derivatives provide the fixed coefficients, rather than a saved training trajectory. This gives \(O(q)\) coefficients per observable. It does not resolve the multiple-label noncommutativity in (17), and the required uniform analytic interval is not proved here for the entire requested class.

The completed results of this route are therefore: exact force and feature-motion equations for all fixed depths; identification of the first missing activation–sensitivity Gram; an explicit positive-Gram, arbitrarily-small signed-label counterexample to ordinary pairwise closure; and an autonomous response hierarchy with transparent initialization provenance, a conditional all-time stability mechanism, and an explicit unfavorable generic state count. The requested general polylogarithmic autonomous closure requires an additional finite algebra, compression theorem, or response-factorization result beyond these identities.

## 7. Post-freeze assessment of a supplied finite-algebra construction

After the independent route above was frozen, the supervisor supplied another route's proposed construction: on each already compressed finite layer, retain a unital pointwise multiplication algebra invariant under the initialized layer maps and their transposes; choose a fixed semantic basis; store its multiplication table and evolve the layer transport matrices in that basis. The following is an assessment of that supplied description, not an independent derivation of its compression theorem or optimizer.

Let a layer algebra be a subspace of \(\mathbb R^q\), with basis matrix \(E\in\mathbb R^{q\times r}\). Suppose its columns \(e_i\) are orthonormal in a specified positive-definite metric \(M\), so \(E^\top ME=I_r\). Store

\[
T_{ijk}=\langle e_i,e_j\odot e_k\rangle_M.
\]

If \(u=E\alpha\) and \(v=E\beta\), exact multiplication closure means

\[
u\odot v=E\,U(\alpha)\beta,
\qquad U(\alpha)_{ij}=\sum_kT_{ijk}\alpha_k.
\tag{21}
\]

The last two indices of \(T\) are symmetric. Full symmetry requires the additional property \(\langle u,v\odot w\rangle_M=\langle v,u\odot w\rangle_M\); it does not follow for an arbitrary dense \(M\). Thus this construction retains more structure than an undifferentiated symmetric triple-moment tensor.

Let \(c_a\) be the coordinates of the activation \(h_a\), and let \(\pi_a\) be those of \(\phi'(z_a)\). Let \(J\) represent the desired physical Gram pairing in these coordinates. For example, if that pairing is \(q^{-1}u^\top v\), then \(J=q^{-1}E^\top E\); it need not be the identity just because the basis was orthonormalized in \(M\). The exact missing landmark and its Gram are then

\[
\psi_{ab}=E\,U(\pi_a)c_b,
\qquad
\mathcal M_{bc;ad}
=\bigl(U(\pi_a)c_b\bigr)^\top
J\bigl(U(\pi_d)c_c\bigr).
\tag{22}
\]

Equation (22) directly exposes the mechanism in the counterexample: the multiplication table retains which feature coordinates overlap with which sensitivity coordinates. Ordinary Grams discard that multiplication information. Associativity and exact closure allow higher products to be evaluated using the same table, so (15) need not generate an ever-growing list of independent moments.

The same representation also gives exact feature Gram velocities. If \(\mathsf R^{(\ell)}\) is the represented layer transport and \(c_a^{(\ell-1)}\) the previous layer's feature coordinates, the preactivation coordinates are \(\mathsf R^{(\ell)}c_a^{(\ell-1)}\). With fixed bases,

\[
\begin{aligned}
\dot c_a^{(\ell)}&=
U^{(\ell)}(\pi_a^{(\ell)})
\left(\dot{\mathsf R}^{(\ell)}c_a^{(\ell-1)}
+\mathsf R^{(\ell)}\dot c_a^{(\ell-1)}\right),\\
\dot G_{ab}^{(\ell)}&=
\dot c_a^{(\ell)\top}J^{(\ell)}c_b^{(\ell)}
+c_a^{(\ell)\top}J^{(\ell)}\dot c_b^{(\ell)}.
\end{aligned}
\tag{23}
\]

The two terms inside the first line of (23) are the new weight write and transported prior-layer motion from (4). The matrix \(U(\pi_a)\) is the sample's activation gate. Equations (22)–(23) are transparent observable formulas derived from the finite algebra, beyond simply asserting its equivalence to a finite network.

The supplied optimizer still needs exact transport into these coordinates. An orthonormal basis in \(M\) does not authorize replacement of the specified training law by a metric-gradient flow. For example, for ordinary Euclidean transpose, put \(S_\ell=E_\ell^\top E_\ell\). If \(B E_{\ell-1}=E_\ell\mathsf R\) and \(B^\top\) preserves the corresponding algebra subspaces, its represented transpose is

\[
E_{\ell-1}^{-1}\big|_{\operatorname{im}E_{\ell-1}}\,
B^\top E_\ell
=S_{\ell-1}^{-1}\mathsf R^\top S_\ell.
\tag{24}
\]

Here the restricted inverse denotes the unique coefficient map on the indicated subspace. Equation (24) follows by multiplying \(B^\top E_\ell=E_{\ell-1}V\) by \(E_{\ell-1}^\top\), giving \(S_{\ell-1}V=\mathsf R^\top S_\ell\). Similarly, the original dense update \(\dot B=-(2/(mn))\sum_b r_b\delta_bh_b^\top\), with coefficient vectors \(d_b,c_b\), becomes

\[
\dot{\mathsf R}=-\frac2{mn}\sum_b r_b d_bc_b^\top S_{\ell-1}.
\]

These illustrative formulas are for the flow stated in Section 1. The distinct supplied compressed optimizer must be transformed from its actual law, with its own normalizations; its equality to this example has not been assumed.

Finally, exact finite multiplication does not normally reduce the number of neuron coordinates further. If a unital subalgebra of \(\mathbb R^q\) contains one vector \(z\) with pairwise distinct entries, it contains each coordinate indicator, because the pointwise polynomial

\[
\prod_{j\ne i}\frac{z-z_j\mathbf1}{z_i-z_j}
\]

is exactly the \(i\)-th coordinate indicator. Thus the algebra is all of \(\mathbb R^q\). A Gaussian first-layer response to a nonzero input has distinct entries almost surely, so an algebra required to contain that response generically has dimension \(q\). A change to a semantic basis does not remove those \(q\) degrees of freedom.

Accordingly, a full algebra on an already polylogarithmic-width surrogate, with \(O(q^3)\) fixed multiplication data and \(O(q^2)\) moving transports, stays polynomial in \(\log n\) and can inherit accuracy by **exact conjugacy**, if that conjugacy and the underlying compression theorem are established. It also reveals the sensitivity-overlap mechanism through (22)–(23). But it remains an exact coordinate representation of that finite surrogate; it does not alone establish the stronger requirement of a new aggregate state that avoids representing a small network. That distinction is a scientific limitation, separate from the potential explanatory value of the representation.

## 8. Exact sample-response audit for the supplied metric runtime

For this extension, the supervisor explicitly supplied the complete same-study source `RELATIONAL_QUOTIENT.md`; it was read in full. Its compressed metric runtime differs from Section 1 and must not be treated as a gradient flow of its corrected predictor. This section uses that runtime's notation and signs.

Training inputs have fixed vectors \(v_a\), labels \(y_a\), and deficit state \(c_a=y_a-f_a\). A fixed validation panel has input vectors but no labels. The forward pass is

\[
z_a^{(1)}=Av_a,\qquad
z_a^{(\ell)}=B_\ell h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi(z_a^{(\ell)}),
\]

with fixed SPD metrics \(M_\ell\). Put \(\langle u,v\rangle_{M_\ell}=u^\top M_\ell v\), \(Q_{ab}=v_a^\top v_b\), and \(G_{ab}^{(\ell)}=\langle h_a^{(\ell)},h_b^{(\ell)}\rangle_{M_\ell}\). The supplied directions are

\[
\delta_a^{(L)}=\phi'(z_a^{(L)})\odot\widehat w,\qquad
\delta_a^{(\ell)}=\phi'(z_a^{(\ell)})\odot B_{\ell+1}^*\delta_a^{(\ell+1)},
\qquad B_\ell^*=M_{\ell-1}^{-1}B_\ell^\top M_\ell.
\]

Their specified updates are

\[
\begin{aligned}
\dot A&=\frac2m\sum_{s=1}^m c_s\delta_s^{(1)}v_s^\top,\\
\dot B_\ell&=\frac2m\sum_{s=1}^m
c_s\delta_s^{(\ell)}h_s^{(\ell-1)\top}M_{\ell-1},\\
\dot w&=\frac2m\sum_{s=1}^mc_sh_s^{(L)},\qquad
\dot c=-\frac2mKc.
\end{aligned}
\tag{25}
\]

The matrix \(K\) here is the supplied sum of forward/backward Gram products in `RELATIONAL_QUOTIENT.md`. Its positivity follows from its Gram construction, not from identification with derivatives of the corrected predictor. There are no additional width factors in (25); any quadrature or width normalization is already part of the specified metrics and compressed directions.

### Forward responses and the exact similarity equation

Write \(D_a^{(\ell)}=\operatorname{diag}\phi'(z_a^{(\ell)})\). For evaluated input \(a\) and training driver \(s\), define the preactivation response \(J_{as}^{(\ell)}\) by

\[
\begin{aligned}
J_{as}^{(1)}&=\delta_s^{(1)}Q_{as},\\
J_{as}^{(\ell)}&=\delta_s^{(\ell)}G_{as}^{(\ell-1)}
+B_\ell D_a^{(\ell-1)}J_{as}^{(\ell-1)},\qquad \ell\geq2.
\end{aligned}
\tag{26}
\]

The claim is

\[
\dot z_a^{(\ell)}=\frac2m\sum_{s=1}^mc_sJ_{as}^{(\ell)},
\qquad
\dot h_a^{(\ell)}=\frac2m\sum_{s=1}^mc_sD_a^{(\ell)}J_{as}^{(\ell)}.
\tag{27}
\]

For layer 1, substitute \(\dot A\) from (25) into \(\dot A v_a\). For layer \(\ell\), differentiate \(z_a^{(\ell)}=B_\ell h_a^{(\ell-1)}\):

\[
\dot z_a^{(\ell)}=\dot B_\ell h_a^{(\ell-1)}
+B_\ell D_a^{(\ell-1)}\dot z_a^{(\ell-1)}.
\]

The first term supplies \(\delta_s^{(\ell)}G_{as}^{(\ell-1)}\); induction gives the second term in (26). This proves (27) and checks both gate locations: the previous layer's gate is inside propagation in (26), and the current layer's gate is applied afterward in (27). Putting a second current-layer gate into (26) would be incorrect.

Consequently, define the symmetric-in-\(a,b\) response coefficient

\[
\mathcal S_{ab;s}^{(\ell)}=
\langle D_a^{(\ell)}J_{as}^{(\ell)},h_b^{(\ell)}\rangle_{M_\ell}
+\langle h_a^{(\ell)},D_b^{(\ell)}J_{bs}^{(\ell)}\rangle_{M_\ell}.
\]

The exact similarity equation is

\[
\dot G_{ab}^{(\ell)}=\frac2m\sum_{s=1}^m
c_s\mathcal S_{ab;s}^{(\ell)}.
\tag{28}
\]

The positive sign is required because \(c=y-f\), whereas Section 1 used \(r=f-y\). There is no division by \(c_s\), so (26) and (28) are regular when any deficit vanishes. The gates stay in their displayed arguments. For a general SPD metric,

\[
\langle D_a u,v\rangle_M
=\langle u,D_a^*v\rangle_M,
\qquad D_a^*=M^{-1}D_aM,
\]

and generally \(D_a^*\ne D_a\). Moving a coordinatewise gate across a metric pairing without the adjoint would change (28).

### Direct writes, transported motion, and signed geometry

The first term of (26) says that a training sample writes along its backward direction, with strength set by its previous-layer feature similarity to the evaluated sample. The second term carries prior-layer motion through the evaluated sample's gate and the next transport map. Iteration yields a finite decomposition by the layer where the write occurred. Define \(\mathcal T_{a,\ell\leftarrow j}=I\) for \(j=\ell\), and for \(j<\ell\) define

\[
\mathcal T_{a,\ell\leftarrow j}
=B_\ell D_a^{(\ell-1)}B_{\ell-1}D_a^{(\ell-2)}
\cdots B_{j+1}D_a^{(j)}.
\]

Then

\[
J_{as}^{(\ell)}
=\mathcal T_{a,\ell\leftarrow1}\delta_s^{(1)}Q_{as}
+\sum_{j=2}^{\ell}
\mathcal T_{a,\ell\leftarrow j}\delta_s^{(j)}G_{as}^{(j-1)}.
\tag{29}
\]

This distinguishes a direct write at each layer from its subsequent propagation. Pairing the terms of (29) with features gives observable path contributions to (28). It does not turn those path coefficients into an autonomous state: their current values still depend on the evolving gates and transport maps.

No attraction-only or conservation law follows from (28). The deficits can have either sign; the individual response pairings can also have either sign. A concrete illustration satisfying the zero-readout initialization comes from configuration A in Section 3, specialized to \(M=I_8/8\), \(c(0)=(\eta,-\eta)\), and the corrected runtime initialized with \(w(0)=0\). Its readout correction and the first derivative of that correction both vanish initially. Direct substitution into (27) gives

\[
\dot G(0)=0,\qquad
\ddot G(0)=\eta^2a^2
\begin{pmatrix}
1-a^2&-1\\
-1&1-a^2
\end{pmatrix}.
\tag{30}
\]

The off-diagonal similarity begins to decrease. The eigenvalues of \(\ddot G(0)\) are \(-\eta^2a^4\) and \(\eta^2a^2(2-a^2)\), so \(\dot G(t)\) is indefinite for sufficiently small positive time. Reversing the sign of one label reverses the initial off-diagonal change. Thus the exact Gram trajectory is not monotone in the positive-semidefinite ordering, even in this simple positive-Gram, small-label case.

Nevertheless, \(G(t)\succeq0\) at every time when it is computed as a Gram matrix of actual features. This is a factorization property, compatible with an indefinite derivative. A separately truncated scalar equation for \(G\) would need its own argument to preserve that property. There is no universal conservation of feature similarities or their trace. This is distinct from decay of \(\|c\|^2\) under the supplied positive-semidefinite residual kernel.

### Corrected outputs as explicit Gram observables

At the final layer, let \(H=[h_1^{(L)},\ldots,h_m^{(L)}]\), \(G=H^\top M_LH\), and define the raw readout overlaps and training-to-evaluated similarities by

\[
t_a=\langle w,h_a^{(L)}\rangle_{M_L},\qquad
k_a=H^\top M_Lh_a^{(L)}.
\]

Here \(t_{\rm tr}\) is the vector of the first \(m\) overlaps. On the domain where \(G\) is invertible, the source's factors of \(\sqrt m\) cancel exactly, giving

\[
\alpha=G^{-1}(y-c-t_{\rm tr}),\qquad
\widehat w=w+H\alpha,\qquad
f_a=t_a+k_a^\top\alpha.
\tag{31}
\]

The relevant additional scalar response is

\[
\mathcal U_{a;s}
=G_{as}^{(L)}+
\langle w,D_a^{(L)}J_{as}^{(L)}\rangle_{M_L}.
\]

Using (25) and (27), all observable derivatives in (31) obey

\[
\begin{aligned}
\dot t_a&=\frac2m\sum_s c_s\mathcal U_{a;s},\\
\dot k_{a,b}&=\dot G_{ba}^{(L)},\\
\dot\alpha&=G^{-1}(-\dot c-\dot t_{\rm tr}-\dot G\,\alpha),\\
\dot f_a&=\dot t_a+\dot k_a^\top\alpha+k_a^\top\dot\alpha.
\end{aligned}
\tag{32}
\]

For a training index \(a\), \(k_a=Ge_a\) and \(t_a=(t_{\rm tr})_a\), so differentiating \(f_a=y_a-c_a\), or cancelling the terms of (32), gives \(\dot f_a=-\dot c_a\). This is an exact algebraic consequence of the correction. It does not identify the hidden response (26), or the supplied backward directions, with derivatives of the corrected predictor. For validation indices, (32) includes the changing readout correction and supplies the proper prediction derivative.

Validation indices can appear in the evaluated slots \(a,b\) of (26)–(32), but never in the driving slot \(s\) or the training matrix \(H\). They supply no deficits, no labels, and no update terms. This verifies passive validation directly at the observable level.

### What is autonomous, and what remains unmet

The quantities \(G,t,c\) provide a particularly transparent readout: (31) reconstructs every requested training or validation prediction. Equations (28) and (32) then reveal the exact response coefficients that would be sufficient for their evolution. But the equations for \(G,t,c\) do not determine \(\mathcal S,\mathcal U\), the backward Gram products in \(K\), or their subsequent changes. The same-Gram counterexample and (15) show the first such dependency concretely. Naming the missing coefficients does not close the model.

A fixed set of transported-landmark Grams has scientific value when it identifies which features overlap with which gates, which layer wrote a displacement, and how that displacement propagated. Equations (22), (28), and (29) make those relationships precise. Autonomy requires, in addition, a proved finite rule for updating every product and transport needed by the set. The supplied activation algebra plus its complete evolving transfer table provides exactly such a rule. Its \(M\)-orthonormal semantic coordinates give \(J\), \(\mathcal S\), \(\mathcal U\), and the corrected output using the fixed multiplication tensor, the current transfer responses, and residuals.

In the generic full-algebra case, however, that transfer table determines the relevant \(B_\ell\) maps bijectively. Replacing arbitrary matrix entries by their pairings against a semantic basis changes the interpretation and evaluation formulas, but retains their information content. A proper invariant subspace is an actual quotient; generic initialized distinct coordinate responses need not provide one. This route therefore establishes an exact mechanistic observable representation and conditional inheritance of an existing compressed prediction certificate. It does **not** establish a smaller autonomous sample-observable state free of full transfer-operator information, nor a theorem that such a state is impossible.

For the stronger user criterion, the outstanding mathematical step is a finite factorization, invariant statistic, or controlled truncation of the response coefficients that removes that transfer information while retaining the required all-time error. No such factorization is proved here. In particular, a certificate only for predictions does not automatically certify dense feature Gram trajectories, even when the compressed and relational Gram trajectories are exactly equal.
