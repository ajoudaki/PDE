# From finite source response to whole-function sampling fluctuations

Draft for checking and assembly. The finite-source estimate in the accompanying
canonical source lemma is an input to this section; it must be proved before
the neural conclusion below is accepted.

## 1. Model, spaces, and statement

Use exactly the population carrier, initialization, and physical gradient flow
of C.4.7. Write \(u=x/\sqrt2\), \(\phi=\tanh\), and
\(\theta=(w,K,c)\), with \(A=A_0+K\). The retained fields are
\[
 h_\theta(u)=\phi(w\cdot u),\quad Z_\theta(u)=Ah_\theta(u),\quad
 b_\theta(u)=\phi(Z_\theta(u)),\quad
 \Delta_\theta(u)=c\phi'(Z_\theta(u)),\quad Q_\theta(u)=A^*\Delta_\theta(u),
 \quad f_\theta(u)=\langle c,b_\theta(u)\rangle.
\]
For \(r_\theta(u,y)=f_\theta(u)-y\), the actual population equation is
\[
 \dot\theta=-2\int r_\theta(u,y)
 \bigl(\phi'(w\cdot u)Q_\theta(u)u,
             \Delta_\theta(u)\otimes h_\theta(u),b_\theta(u)\bigr)
 \,d\mu(u,y),\qquad \theta(0)=(g,0,0).                 \tag{P1}
\]
The first state component is the full two-dimensional first row, the second
is the learned Hilbert--Schmidt middle increment, and the third is the trained
readout. The initialized Gaussian action and its actual adjoint in (P1) are
the common prescribed construction, not arbitrary operators with the same
norm. The zero population initial readout is its width limit. At finite width
the actual independent Gaussian stored readout is retained throughout.
Population predictions are deterministic expectations on this prescribed
carrier; no additional random environment is left outside those expectations.

The finite networks have two equal-width bias-free tanh hidden layers, output
divided by \(n\), independent centered Gaussian stored variances
\((1,1/n,1/n^2)\), mobilities \((n,1,n)\), and unhalved squared loss integrated
against the labeled training law. No initialization is reset when laws change.

Fix \(Y\ge1\), \(T=40\), the data space and its metric
\[
 \mathcal Z=\sqrt2S^1\times[-Y,Y],\qquad
 d_{\mathcal Z}((x,y),(x',y'))=|x-x'|/\sqrt2+|y-y'|,
\]
and \(\nu_*=\tfrac12\delta_{(\sqrt2e_1,1)}+
\tfrac12\delta_{(\sqrt2e_2,-1)}\). Let \(\delta_Y\) be the C.4.7 radius,
\(U_Y=\{\mu:W_1(\mu,\nu_*)<\delta_Y\}\). Its construction chooses this
radius inside the neighborhood with uniform finite-Euler source caps.
Let \(\rho\) be normalized circle arc length,
\(H=L^2(\sqrt2S^1,\rho;\mathbb R)\), and
\(F(\mu)=f_\mu(T,\cdot)\). We also use the stronger output space
\(\mathcal C=C(\sqrt2S^1;\mathbb R)\) with its supremum norm.

Set \(\delta'_Y=\delta_Y/4\). For every separately fixed Borel law
\(\mu\) with \(W_1(\mu,\nu_*)<\delta'_Y\), the conclusion to be assembled is:
there is a bounded continuous \(\mathcal C\)-valued atom response
\(I_\mu(z)\), given by the full source recursion below, such that
\[
 I_\mu(z)=\lim_{\epsilon\downarrow0}
 \frac{F((1-\epsilon)\mu+\epsilon\delta_z)-F(\mu)}{\epsilon},
 \qquad \int I_\mu(z)\,d\mu(z)=0.                       \tag{P2}
\]
The derivative holds in \(\mathcal C\), hence in \(H\), for every \(z\).
For iid observations with empirical law \(\mu_m\), define the bounded
measurable extension
\[
 \overline F(Q)=F(Q)\quad(Q\in U_Y),\qquad
 \overline F(Q)=0\quad(Q\notin U_Y).                    \tag{P3}
\]
Then, with \(r_m=\overline F(\mu_m)-F(\mu)-m^{-1}\sum_i I_\mu(Z_i)\),
\[
 m\,\mathbb E\|r_m\|_H^2\longrightarrow0.              \tag{P4}
\]
In particular \(\sqrt m\,r_m\to0\) in probability. Its covariance and
whole-function limit are
\[
 \Sigma_\mu v=\int\langle I_\mu(z),v\rangle_H I_\mu(z)\,d\mu(z),
 \qquad \sqrt m\,[\overline F(\mu_m)-F(\mu)]
                  \Rightarrow\mathcal N_H(0,\Sigma_\mu).              \tag{P5}
\]
The finite-network conclusion is the width-first assertion
\[
 \lim_{m\to\infty}\limsup_{n\to\infty}
 d_{\rm BL}\!\left(\operatorname{Law}\!\left[
 \sqrt m\,(f_{n,\mu_m}(T,\cdot)-F(\mu))\right],
                  \mathcal N_H(0,\Sigma_\mu)\right)=0,                \tag{P6}
\]
where sampling and initialization are independent and both are included in
the law. Here bounded-Lipschitz tests have absolute value and Lipschitz constant
at most one. No simultaneous width/sample rate is asserted.

## 2. The finite estimate needed for the passage

Choose a closed law ball of radius \(3\delta_Y/4\). The source lemma applies
to all finite laws in a slightly larger ball still inside the C.4.7 source-cap
neighborhood, and all sufficiently fine population raw Euler meshes. It gives
constants \(L,M<\infty\), independent of the mesh, support size, minimum mass,
and covariance rank, such that its endpoint map \(F_h\) obeys
\[
 \|\partial_\sigma F_h(\lambda)\|_{\mathcal C}\le L\|\sigma\|_{\rm TV},
 \qquad
 \|\partial_\sigma\partial_\tau F_h(\lambda)\|_{\mathcal C}
                    \le M\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}.        \tag{P7}
\]
Directions have zero total mass. They are taken in the finite simplex, with
continuous one-sided extensions at zero masses. The total-variation norm is
the total mass of the variation measure, so \(\|\delta_z-\delta_{z'}\|_{\rm TV}
\le2\). The estimates concern only probability-preserving segments and
rectangles lying in the stated region.

C.4.7 gives \(F_h(\lambda)\to F(\lambda)\) in \(\mathcal C\) for every
fixed finite law there. Its proof also gives uniform value completion on
smaller balls, but the first passage below only needs pointwise value
convergence, including at the finitely many law arguments in each comparison.
The actual map \(F:U_Y\to\mathcal C\) is \(W_1\)-continuous and bounded.
Boundedness follows already from \(\|c(t)\|_\infty\le2Yt\) in C.4.7; a
larger Euler bound \(Y(e^{2T}-1)\) would suffice as well.

## 3. Actual atom response, centering, and general directions

Let \(\mathcal K=\{Q:W_1(Q,\nu_*)\le\delta_Y/2\}\) and
\(D_Y=2+2Y\), an upper bound for the data diameter. Choose
\(\epsilon_0=\min(1/2,\delta_Y/(4D_Y))\). Every contamination of a law
in \(\mathcal K\) of size at most \(\epsilon_0\) remains in the larger
ball of Section 2. Finite-support Taylor's formula from (P7) gives
\[
 \|F_h((1-\epsilon)\lambda+\epsilon\delta_z)-F_h(\lambda)
       -\epsilon I_{h,\lambda}(z)\|_{\mathcal C}
                  \le2M\epsilon^2,\qquad
 I_{h,\lambda}(z)=\partial_{\delta_z-\lambda}F_h(\lambda).             \tag{P8}
\]
To add a new observation, include its slot with mass zero and use the
one-sided source derivative. No strictly positive lower mass is required.

Fix \(\lambda,z\). Comparing two derivatives to the same forward quotient
in (P8) shows that their limsup difference as both meshes vanish is at most
\(4M\epsilon\). The quotient values converge by C.4.7. Letting \(\epsilon\)
decrease proves that \(I_{h,\lambda}(z)\) has a limit in \(\mathcal C\),
denoted \(I_\lambda(z)\). It satisfies \(\|I_\lambda(z)\|\le2L\), and
passing to the limit in (P8) gives its actual contamination derivative with
the same remainder. This argument uses arbitrary vanishing mesh sequences;
the result does not depend on a chosen sequence.

For arbitrary \(Q\in\mathcal K\), define the continuous forward quotient
\[
 J_\epsilon(Q,z)=
   \epsilon^{-1}\{F((1-\epsilon)Q+\epsilon\delta_z)-F(Q)\}.
\]
For finite \(Q\), (P8) gives
\(\|J_\epsilon(Q,z)-J_\eta(Q,z)\|\le2M(\epsilon+\eta)\).
Finite laws are \(W_1\)-dense in \(\mathcal K\): approximate by finite
quantization and, if necessary, mix a vanishing amount of \(\nu_*\) to move
strictly inside the ball. Continuity of \(F\) passes this inequality to every
\(Q\). Thus the quotients converge uniformly in \((Q,z)\) to
\(I_Q(z)\), with
\[
 \|F((1-\epsilon)Q+\epsilon\delta_z)-F(Q)-\epsilon I_Q(z)\|_{\mathcal C}
                         \le2M\epsilon^2.                            \tag{P9}
\]
The map \((Q,z)\mapsto(1-\epsilon)Q+\epsilon\delta_z\) is continuous in
\(W_1\), by the mixture coupling. Each \(J_\epsilon\) is therefore jointly
continuous. Its uniform limit \(I\) is jointly continuous on the compact
set \(\mathcal K\times\mathcal Z\), and is bounded by \(2L\). In particular
it is a Bochner-measurable, square-integrable \(H\)-valued field.

For each finite law \(\lambda=\sum_a p_a\delta_{z_a}\), linearity of the
finite derivative gives
\[
 \sum_a p_a I_{h,\lambda}(z_a)=
 \partial_{\sum_a p_a(\delta_{z_a}-\lambda)}F_h(\lambda)=0.
\]
The mesh limit preserves this equality. If \(\lambda_j\to Q\) weakly,
joint continuity implies \(I_{\lambda_j}\to I_Q\) uniformly in the atom.
For any continuous Banach-valued function on a compact metric space its
integrals converge in norm under weak convergence of probability laws: choose
a finite continuous partition of unity whose weighted point values uniformly
approximate that function, and apply weak convergence to its finitely many
scalar weights. Applying this fact to \(I_Q\) proves
\[
                         \int I_Q\,dQ=0.                             \tag{P10}
\]
This proves centering for the actual trained response, not just for a formal
linearized equation.

At the reference law this response agrees with C.4.6:
\(I_{\nu_*}(z)=\mathscr D_{\delta_z-\nu_*}f(T,\cdot)\).
Indeed C.4.7 identifies the latter with the same actual contamination
derivative, and a norm limit has only one value. This does not extend the
finite-network derivative conclusions of C.4.6 to other base laws.

The same argument supplies the integral representation in every admissible
law direction. For finite \(\lambda,\nu\), the derivative of a mixture has
value \(\int I_{h,\lambda}\,d(\nu-\lambda)\) and Taylor remainder at most
\(M\epsilon^2\|\nu-\lambda\|_{\rm TV}^2/2\). Pass first through the mesh
limit. Next approximate both laws by the same finite quantization map.
Quantization contracts total variation and has uniformly vanishing transport
error. The displayed integral converges by joint continuity, so
\[
 \left.\frac d{dt}F((1-t)Q+t\nu)\right|_{t=0+}
                  =\int I_Q(z)\,d(\nu-Q)(z).                         \tag{P11}
\]
Here the segment is restricted to the region where the estimate applies;
\(\nu\) need not itself lie there if only a short initial part is used.
Apply this identity at every point of an admissible segment. Joint continuity
of \(I\) makes its directional derivative continuous, hence gives the
fundamental theorem of calculus on that segment. For a general zero-mass
direction \(\eta\) admitting a positive segment length \(a\), set
\(\nu=Q+a\eta\) and rescale (P11). This covers all directions used in
replacement rectangles and in conditional-expectation telescoping.

Likewise the mixed finite-difference bound
\[
 \|F(Q+s\sigma+t\tau)-F(Q+s\sigma)-F(Q+t\tau)+F(Q)\|_{\mathcal C}
             \le Mst\|\sigma\|_{\rm TV}\|\tau\|_{\rm TV}              \tag{P12}
\]
passes from (P7) first in mesh and then through common quantization. All laws
on the rectangle must be probabilities in the open ball of radius
\(\delta_Y/2\). Its compact image has positive distance from the boundary;
fine quantizations therefore remain in the larger analytic region. The
argument takes only four value limits. No second derivative of the limiting
population flow is assumed or needed.

## 4. A usable characterization of the signed field

For a finite law \(\lambda\), the canonical source lemma supplies an explicit
chronological Gaussian recursion for \(I_{h,\lambda}(z)\): append the atom
\(z\), differentiate its mass vector in direction \(\delta_z-\lambda\), and
propagate the displayed lower and upper coordinate responses together with
both covariance responses, all residual responses, and both response
coefficient arrays. Expectations are differentiated by the Gaussian covariance
formula, including at singular covariance. All initial mass responses are
zero. At the last node the resulting full derivative of
\(\mathbb E_2[c\phi(Z(u))]\) is \(I_{h,\lambda}(z)(\sqrt2u)\).

For any finite quantizations \(q_j:\mathcal Z\to\mathcal Z\) with
\(\sup_z d(q_jz,z)\to0\), chosen so the base laws stay in the admitted ball,
the actual field is characterized by
\[
 I_\mu(z)=\lim_{j\to\infty}\lim_{h\to0}
       I_{h,(q_j)_\#\mu}(q_jz)\quad\hbox{in }\mathcal C.             \tag{P13}
\]
The inner limit exists by (P8), and the outer limit follows uniformly in
\(z\) from joint continuity. The result is independent of the quantizations
and meshes by (P9). Thus (P13), with the complete source derivative recursion,
defines a well-posed evolution-and-limit procedure for the influence. It
retains all three trained blocks and both initialized action orientations.
It does not replace those objects by an undetermined endpoint derivative.

## 5. Sampling, covariance, and the mean-square strengthening

Apply the canonical sampling lemma to the actual map on
\(\{Q:W_1(Q,\nu_*)<\delta_Y/2\}\), with kernel (P9)--(P11) and second
difference bound (P12). For each fixed \(\mu\) in the smaller requested
ball, choose a \(W_1\)-ball around \(\mu\) whose closure is inside this
analytic region. The lemma's finite-continuous-test cutoff defines a global
bounded map \(G_\mu\), equal to \(F\) near \(\mu\), with the same actual
influence there. Its proof gives
\[
 m\mathbb E\left\|G_\mu(\mu_m)-F(\mu)
                  -\frac1m\sum_iI_\mu(Z_i)\right\|_H^2\to0,
 \qquad
 \Pr\{G_\mu(\mu_m)\ne\overline F(\mu_m)\}\le C_\mu e^{-c_\mu m}.    \tag{P14}
\]
The mismatch bound refers to the cutoff's finite-test neighborhood, which
lies inside \(U_Y\). Both maps are uniformly bounded, so
\[
 m\mathbb E\|G_\mu(\mu_m)-\overline F(\mu_m)\|_H^2
                         \le C_\mu m e^{-c_\mu m}\to0.
\]
This proves (P4) with exactly the extension (P3). In particular empirical
laws outside \(U_Y\) are exponentially rare and do not change any asserted
limit. No labels on the testing circle have been introduced.

For arbitrary \(g,h\in H\), the covariance acts as
\[
 \langle\Sigma_\mu g,h\rangle_H
   =\int\langle I_\mu(z),g\rangle_H
                \langle I_\mu(z),h\rangle_H\,d\mu(z).                 \tag{P15}
\]
Thus the joint limiting fluctuations of the spatial averages against any
finite collection of tests are centered Gaussian with these covariances.
Since the field is continuous and bounded on the compact atom/input product,
one may equivalently use the continuous kernel
\[
 K_\mu(x,x')=\int I_\mu(z)(x)I_\mu(z)(x')\,d\mu(z),
\quad (\Sigma_\mu g)(x)=\int K_\mu(x,x')g(x')\,d\rho(x').             \tag{P16}
\]
Fubini is justified by boundedness and the finite measures. The operator is
positive, self-adjoint and trace class, with
\(\operatorname{Tr}\Sigma_\mu=\int\|I_\mu(z)\|_H^2d\mu(z)\).
No diagonal form, positive rank, or nondegeneracy is imposed.

The sampling lemma proves the Hilbert CLT, giving (P5). It also gives the
separate strengthening requested here without further label or density
assumptions: put \(S_m=m^{-1}\sum_iI_\mu(Z_i)\). Independence and centering
give \(\mathbb E\|S_m\|_H^2=\operatorname{Tr}\Sigma_\mu/m\). By
Cauchy--Schwarz and (P4),
\[
 m|\mathbb E\langle S_m,r_m\rangle_H|
 \le\sqrt{\operatorname{Tr}\Sigma_\mu}\,
                \sqrt{m\mathbb E\|r_m\|_H^2}\to0.
\]
Expanding the squared norm therefore proves
\[
 \mathbb E\|\overline F(\mu_m)-F(\mu)\|_H^2
                 =\frac{\operatorname{Tr}\Sigma_\mu}{m}+o(m^{-1}).   \tag{P17}
\]
The bounded extension and exponential exceptional-event estimate are essential
parts of this statement. It is not a moment theorem for finite-width errors.

## 6. Actual finite gradient flow, including exceptional laws

For every finite labeled law and every finite initialized array, the smooth
finite-dimensional physical GF exists through \(T\). Here is a direct bound
that also covers laws outside \(U_Y\). Use the normalized finite norms matching
(P1), write \(c_{n,0}\) for the actual initialized readout, and
\(A_n=A_{n,0}+K_n\). Explicitly, vector and full-row norms below are
\(\|v\|_{(n)}=(n^{-1}\sum_{j=1}^n|v_j|^2)^{1/2}\), with the Euclidean
two-vector norm inside the sum for a first row. The matrix increment norm is
the ordinary Frobenius norm \(\|K_n\|_{\rm HS}=\|K_n\|_F\), and the
action norm is the ordinary spectral norm. These are precisely the finite
raw metric conventions of C.4.7; the middle update is
\(-2n^{-1}\int r\Delta h^T\,d\mu_m\), whose Frobenius norm is bounded by
the product of the two normalized vector norms. Since the gates have absolute
value at most one,
\[
 \|\dot c_n\|\le2(\|c_n\|+Y),\qquad
 \|\dot K_n\|_{\rm HS}\le2(\|c_n\|+Y)\|c_n\|,
\]
\[
 \|\dot w_n\|\le2(\|c_n\|+Y)
             (\|A_{n,0}\|+\|K_n\|_{\rm HS})\|c_n\|.               \tag{P18}
\]
The first inequality gives
\(\|c_n(t)\|\le(\|c_{n,0}\|+Y)e^{2t}-Y\); integration then bounds
\(K_n\) and \(w_n\) on each finite time interval. These constants may
depend on the initialized array and \(n\); no uniform bound is needed here.
A solution of a locally Lipschitz finite-dimensional equation that remains
bounded on each such interval extends through its endpoint: on a containing
compact ball the vector field is bounded and locally Lipschitz, giving a
Cauchy endpoint and a local continuation. This proves global finite-time
existence. Smooth dependence on the finite data and initialization gives
measurability of the \(H\)-valued prediction statistic; the bounds ensure the
local dependence can be continued through \(T\).

Fix \(m\), and condition on \((Z_1,\ldots,Z_m)\). On the event
\(E_m=\{\mu_m\in U_Y\}\), this is a separately fixed finite training law,
and independence leaves the specified initialization distribution unchanged.
C.4.7.NW1 therefore gives
\[
 \|f_{n,\mu_m}(T,\cdot)-F(\mu_m)\|_H\to0
 \quad\hbox{in initialization probability, conditionally on each such law}.
\]
For every fixed \(m\), bounded convergence after conditioning implies
\[
 \mathbb E\left[\mathbf1_{E_m}
     \min\{2,\sqrt m\|f_{n,\mu_m}(T)-F(\mu_m)\|_H\}\right]\to0.    \tag{P19}
\]
On \(E_m^c\), the difference of any two bounded-Lipschitz test values is at
most two. No width limit on that event is asserted. With
\(X_{n,m}=\sqrt m(f_{n,\mu_m}(T)-F(\mu))\) and
\(X_m=\sqrt m(\overline F(\mu_m)-F(\mu))\), (P19) yields
\[
 \limsup_{n\to\infty}
 d_{\rm BL}(\operatorname{Law}(X_{n,m}),\operatorname{Law}(X_m))
                         \le2\Pr(E_m^c).                             \tag{P20}
\]
The right-hand side tends to zero exponentially by (P14). The triangle
inequality, (P5), and then \(m\to\infty\) prove (P6). This argument keeps
the actual finite random initial readout and invokes no finite-network tangent
limit, no rate in width, and no simultaneous width/sample scaling.
