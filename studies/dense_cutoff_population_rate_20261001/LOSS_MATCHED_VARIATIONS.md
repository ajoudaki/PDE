# First and second variations at genuinely matched training loss

This is a bounded, internal theoretical assessment in the existing dense-width study. Matching loss cancels a perturbation that changes only traversal speed along the same trajectory. It does not cancel the transverse carrier response in general. In fact, for a physical initialization perturbation of gradient flow, the derivative of the log-loss vector field on loss-tangent directions is a metric reflection of the original Hessian action, times a bounded clock factor. Its norm is unchanged by that reflection. Second matched-loss sensitivities also have an endpoint regularity issue which is absent from a common-time comparison.

The calculations below are exact at fixed finite width on positive-loss intervals. They neither establish nor refute a strict dense finite-to-population root-width estimate. They introduce no activity clock, cutoff algorithm, experiment, or manuscript change.

## 1. Canonical dense system and differentiability scope

Fix width \(n\), depth \(L\), and training pairs \((x_a,y_a)_{a=1}^m\), with \(x_a\in\mathbb R^d\). The parameter state is

\[
\theta=(W^{(1)},\ldots,W^{(L)},w),\qquad
W^{(1)}\in\mathbb R^{n\times d},\quad
W^{(\ell)}\in\mathbb R^{n\times n}\ (\ell\ge2),\quad w\in\mathbb R^n.
\]

The manuscript's forward pass and unhalved mean squared loss are

\[
z_a^{(1)}=W^{(1)}x_a/\sqrt d,\qquad
z_a^{(\ell)}=W^{(\ell)}h_a^{(\ell-1)},\qquad
h_a^{(\ell)}=\phi_\ell(z_a^{(\ell)}),
\]
\[
f_a=\frac{w^\top h_a^{(L)}}n,\qquad
r_a=f_a-y_a,\qquad
\mathcal L(\theta)=\frac1m\sum_a r_a^2=\rho^2.
\tag{1}
\]

Flattening the ordinary Euclidean and Frobenius parameter coordinates, let \(D\) be the constant positive diagonal mobility matrix with block values \((n,1,\ldots,1,n)\). Define

\[
g=\nabla_\theta\mathcal L,\qquad
F=-Dg,\qquad
a=g^\top Dg=-\frac{d\mathcal L}{dt}.
\tag{2}
\]

Then \(\dot\theta=F(\theta)\) is exactly `paper/main.tex`, equation `eq:dense-flow`. The ordinary prediction Jacobian \(J\in\mathbb R^{m\times\dim\theta}\), with row \(\nabla f_a^\top\), gives

\[
K=JDJ^\top,\qquad \Gamma=K/m,
\qquad \dot r=-\frac2mKr=-2\Gamma r,
\]
\[
a=\frac4{m^2}r^\top Kr,
\qquad
\frac a{\mathcal L}=\frac4m\frac{r^\top Kr}{r^\top r}
=4\frac{r^\top\Gamma r}{r^\top r}.
\tag{3}
\]

For first classical parameter variations, assume the activations are \(C^2\). For second variations, assume they are \(C^3\), so that \(F\) is \(C^2\). Tanh satisfies both conditions. The manuscript's general \(C^{1,1}\) activation class alone does not supply these classical second-variation equations; a nonsmooth or finite-difference replacement would require a separate argument. No bound here is asserted uniform over activation smoothings.

Consider a \(C^2\) one-parameter initialization \(\theta_0(\varepsilon)\), preserving \(w_0=0\), and its solutions. At every initialization, \(\mathcal L(\theta_0(\varepsilon))=Y^2\), where \(Y^2=m^{-1}\sum_a y_a^2\). Assume \(Y>0\) and a positive-loss interval with \(a>0\). For statements extending over all positive losses, assume the solution exists, reaches every loss in \((0,Y^2]\), and retains the manuscript's positive tangent-Gram gap. The calculations do not prove these premises anew. For \(Y=0\), the zero-readout flow is stationary and this loss parametrization is unnecessary.

## 2. Exact first and second hitting-time derivatives

It is useful first to allow a representation in which both the vector field and the loss explicitly depend on \(\varepsilon\):

\[
\dot q_\varepsilon=F_\varepsilon(q_\varepsilon),
\qquad \mathcal L_\varepsilon(q).
\]

This includes learned-increment coordinates \(q=\theta-\theta_0(\varepsilon)\). Assume the required \(C^2\) derivatives exist. Fix an absolute loss level \(\ell>0\) reached with nonzero loss derivative, and define \(t_\varepsilon\) and the matched state by

\[
\mathcal L_\varepsilon(q_\varepsilon(t_\varepsilon))=\ell,
\qquad \bar q_\varepsilon=q_\varepsilon(t_\varepsilon).
\tag{4}
\]

All formulas in this section are evaluated at \(\varepsilon=0\) and \(t=t_0\). Let

\[
Z_1=\left.\partial_\varepsilon q_\varepsilon(t)\right|_0,
\qquad Z_2=\left.\partial_\varepsilon^2 q_\varepsilon(t)\right|_0,
\qquad v=\frac{d}{dt}\mathcal L_0(q_0(t))<0.
\]

Here the derivatives defining \(Z_1,Z_2\) keep physical time fixed. Write

\[
A=\partial_\varepsilon\mathcal L_\varepsilon(q_\varepsilon(t))|_0
=\mathcal L_\varepsilon+\mathcal L_q^\top Z_1,
\]
\[
B=\partial_\varepsilon^2\mathcal L_\varepsilon(q_\varepsilon(t))|_0
=\mathcal L_{\varepsilon\varepsilon}
+2\mathcal L_{q\varepsilon}^\top Z_1
+\mathcal L_{qq}[Z_1,Z_1]+\mathcal L_q^\top Z_2.
\tag{5}
\]

Partial derivatives on the right keep \(q\) fixed. Differentiating (4) once and twice gives

\[
t'_0=-\frac A v,
\qquad
t''_0=-\frac{B+2\dot A\,t'_0+\dot v\,(t'_0)^2}{v}.
\tag{6}
\]

The dot in (6) differentiates along the unperturbed physical trajectory. Applying the chain rule to the state gives the exact matched variations

\[
U:=\bar q'_0=Z_1+Ft'_0,
\]
\[
V:=\bar q''_0
=Z_2+2(F_qZ_1+F_\varepsilon)t'_0
+F_qF(t'_0)^2+Ft''_0.
\tag{7}
\]

Define the rank-one projection

\[
P=I-\frac{F\mathcal L_q^\top}{v},
\qquad PF=0,\quad \mathcal L_q^\top P=0.
\tag{8}
\]

Equations (5)–(7) imply

\[
U=PZ_1-\frac Fv\mathcal L_\varepsilon.
\tag{9}
\]

For the second variation, put

\[
R=Z_2+2(F_qZ_1+F_\varepsilon)t'_0+F_qF(t'_0)^2.
\]

Twice differentiating the level constraint directly gives

\[
\mathcal L_q^\top V+
\mathcal L_{qq}[U,U]+2\mathcal L_{q\varepsilon}^\top U
+\mathcal L_{\varepsilon\varepsilon}=0.
\]

Substitute \(V=R+Ft''_0\) and solve for \(t''_0\) to obtain

\[
V=PR-\frac Fv
\left(\mathcal L_{qq}[U,U]
+2\mathcal L_{q\varepsilon}^\top U
+\mathcal L_{\varepsilon\varepsilon}\right).
\tag{10}
\]

Thus a second variation generally has a normal component forced by the curvature of the loss surface. Projecting the common-time second derivative by itself would omit this term and the mixed time derivatives in \(R\).

### Initialization enters the loss in increment coordinates

In physical parameter coordinates, the network and loss functions are independent of \(\varepsilon\), and the parameter enters only through \(\theta_0(\varepsilon)\). In increment coordinates,

\[
\mathcal L_\varepsilon(q)=\mathcal L(\theta_0(\varepsilon)+q),
\qquad
F_\varepsilon(q)=F(\theta_0(\varepsilon)+q).
\tag{11}
\]

Consequently, at fixed \(q\),

\[
\mathcal L_\varepsilon=g^\top\theta'_0,
\quad
\mathcal L_{q\varepsilon}=\nabla^2\mathcal L\,\theta'_0,
\quad
\mathcal L_{\varepsilon\varepsilon}
=\nabla^2\mathcal L[\theta'_0,\theta'_0]+g^\top\theta''_0.
\tag{12}
\]

They need not vanish after training, even though the initial loss is the same. Setting them to zero would compare different loss observables. Adding the initialization derivatives back to the increment variations recovers exactly the physical-coordinate formulas. For a test prediction \(f_\varepsilon(q,x)\), the matched responses likewise include its explicit derivatives:

\[
\bar f'=f_q^\top U+f_\varepsilon,
\qquad
\bar f''=f_q^\top V+f_{qq}[U,U]
+2f_{q\varepsilon}^\top U+f_{\varepsilon\varepsilon}.
\tag{13}
\]

## 3. Pure speed cancels; physical transverse sensitivity does not

For an exact pure change of speed, let \(F_\varepsilon(q)=c_\varepsilon(q)F_0(q)\), with \(c_\varepsilon>0\), identical initial state, and the same loss function. The trajectories coincide as oriented curves. Their matched states are identical at every reached loss, so \(U=V=0\). This follows also by cancelling \(c_\varepsilon\) in the normalized vector field below. It is a cancellation to every order, not just a first-order estimate.

For the actual dense initialization variation, return to physical coordinates and let

\[
\bar\theta_\varepsilon(s)=\theta_\varepsilon(t_\varepsilon(s)),
\qquad
\mathcal L(\bar\theta_\varepsilon(s))=Y^2e^{-s},
\qquad 0\le s<\infty.
\tag{14}
\]

The common coordinate \(s\) is the negative logarithm of the **same absolute loss divided by the same initial loss**. It is not integrated residual activity. Equations (2)–(3) give

\[
\frac{ds}{dt}=\frac a{\mathcal L},
\qquad
\frac{d\bar\theta}{ds}
=G(\bar\theta):=\frac{\mathcal L F}{a}
=-\frac{\mathcal L Dg}{a}.
\tag{15}
\]

If \(\Gamma\succeq\kappa I\), then \(ds/dt\ge4\kappa\). An upper bound on \(\Gamma\) bounds \(ds/dt\) above as well. These bounds concern the value of the clock rate, not its initialization derivatives.

In physical coordinates,

\[
P=I-\frac{Dg\,g^\top}{a},
\qquad
g^\top U=0,
\qquad
g^\top V+\nabla^2\mathcal L[U,U]=0.
\tag{16}
\]

The projection \(P\) is orthogonal for the mobility inner product
\(\langle u,v\rangle_{D^{-1}}=u^\top D^{-1}v\). Its norm corresponds to the square root of the sum of squared block norms with the manuscript's \(1/n\) factors; it is equivalent, for fixed depth, to the manuscript's sum \(d_n\).

In particular, (9) in physical coordinates gives an exact first-order improvement relative to the common-time response evaluated at the reference hitting time:

\[
U=PZ_1,\qquad \|U\|_{D^{-1}}\le\|Z_1\|_{D^{-1}}.
\tag{16a}
\]

It can remove a large longitudinal response completely. There is no corresponding general contraction statement for the second variation because of (10). The differential calculation that follows concerns evolution of the remaining tangent response; it does not negate (16a).

Write \(H=\nabla^2\mathcal L\). Since \(g^\top U=0\), differentiating (15) gives

\[
\frac{dU}{ds}
=-\frac{\mathcal L}{a}
\left(I-2\frac{Dg\,g^\top}{a}\right)DHU.
\tag{17}
\]

Indeed, \(D\mathcal L[U]=0\), \(Dg[U]=HU\), and \(Da[U]=2g^\top DHU\); substitution proves (17). The matrix \(Q=Dg\,g^\top/a=I-P\) is an orthogonal projection in the mobility metric. Hence \(I-2Q\) is a reflection and

\[
\left\|\frac{dU}{ds}\right\|_{D^{-1}}
=\frac{\mathcal L}{a}\|DHU\|_{D^{-1}}.
\tag{18}
\]

Thus loss normalization does not make the pointwise Hessian action smaller in this norm on loss-tangent directions. Its trajectory-direction correction changes a normal component; it cannot remove an arbitrary transverse gate response. This does not say that long-time sensitivity bounds cannot improve after using dissipation, expectation, or a special observable.

Taking the inner product of (17) with \(U\), the normal correction vanishes, yielding a more useful exact energy identity:

\[
\frac12\frac d{ds}\|U\|_{D^{-1}}^2
=-\frac{\mathcal L}{a}H[U,U]
=-\frac{2\mathcal L}{ma}
\left\{\sum_a(J_aU)^2+\sum_a r_a\nabla^2f_a[U,U]\right\}.
\tag{19}
\]

The first term is dissipative. The second retains the residual-weighted prediction Hessian. If its negative part could be bounded by \(C\rho\|U\|_{D^{-1}}^2\) after the clock factor, then \(\rho=Ye^{-s/2}\) would be integrable in \(s\). The required width-uniform bound on that Hessian form is an additional assertion: the carrier products below are precisely among its terms.

## 4. The exact second normalized variation

Let \(T[U,U]\) denote the vector defined by
\(v^\top T[U,U]=\nabla^3\mathcal L[v,U,U]\) for every parameter vector \(v\). Along the matched family, define the total derivatives

\[
a_1=2g^\top DHU,
\qquad
a_2=2(HU)^\top D(HU)+2g^\top D(HV+T[U,U]).
\tag{20}
\]

Because the total first and second derivatives of \(\mathcal L(\bar\theta_\varepsilon(s))\) vanish, differentiating \(G=\mathcal L F/a\) twice gives

\[
\frac{dV}{ds}
=-\frac{\mathcal L}{a}D(HV+T[U,U])
+\frac{2\mathcal L a_1}{a^2}DHU
+\frac{\mathcal L a_2}{a^2}Dg
-\frac{2\mathcal L a_1^2}{a^3}Dg.
\tag{21}
\]

The transverse part is consequently

\[
P\frac{dV}{ds}
=-\frac{\mathcal L}{a}PD(HV+T[U,U])
+\frac{2\mathcal L a_1}{a^2}PDHU.
\tag{22}
\]

The left side is \(P(dV/ds)\), not \(d(PV)/ds\); the projection moves along the trajectory. Equation (22) exhibits both a surviving third-derivative source and a product of the relative loss-speed sensitivity \(a_1/a\) with a transverse first response. The normal terms removed by \(P\) cannot cancel these two terms in general. At second order, speed and direction variations therefore interact even though an exactly pure speed perturbation cancels.

## 5. Which dense carrier terms remain

For each training sample, define the actual backward carriers and responses by

\[
p_a^{(L)}=w,\qquad
p_a^{(\ell)}=W^{(\ell+1)\top}\delta_a^{(\ell+1)},\qquad
\delta_a^{(\ell)}=\phi_\ell'(z_a^{(\ell)})\odot p_a^{(\ell)}.
\tag{23}
\]

Here \(\delta_a^{(\ell)}=n\,\partial f_a/\partial z_a^{(\ell)}\), excluding the residual. Differentiate these evaluated quantities along the matched family. Let \(u_z=\partial_\varepsilon z|_0\), \(u_p=\partial_\varepsilon p|_0\), \(v_z=\partial_\varepsilon^2 z|_0\), and \(v_p=\partial_\varepsilon^2p|_0\), suppressing sample and layer indices only within the next formulas. Then

\[
\partial_\varepsilon\delta
=\phi''(z)\odot p\odot u_z
+\phi'(z)\odot u_p,
\tag{24}
\]
\[
\partial_\varepsilon^2\delta
=\phi'''(z)\odot p\odot u_z^{\odot2}
+\phi''(z)\odot p\odot v_z
+2\phi''(z)\odot u_z\odot u_p
+\phi'(z)\odot v_p.
\tag{25}
\]

These are evaluated at matched loss already. The identity \(\sum_a r_a\partial_\varepsilon f_a=0\) imposes one scalar training constraint; it does not set the componentwise products in (24)–(25) to zero. Differentiating the reused-matrix carrier still gives

\[
\partial_\varepsilon p_a^{(\ell)}
=(\partial_\varepsilon W^{(\ell+1)})^\top\delta_a^{(\ell+1)}
+W^{(\ell+1)\top}\partial_\varepsilon\delta_a^{(\ell+1)}.
\tag{26}
\]

For example, the first-layer velocity variation contains exactly

\[
-\frac2m\sum_a r_a
\left[\phi_1''(z_a^{(1)})\odot p_a^{(1)}\odot u_{z,a}^{(1)}\right]
\frac{x_a^\top}{\sqrt d}.
\tag{27}
\]

There are other product-rule terms as well. Passing to (17) only adds a scalar multiple of the full velocity to its scaled derivative. Its projection cannot generally eliminate the projection of (27). Bounding (24) in empirical mean square still asks for quantities of the form

\[
\frac1n\sum_i |p_i|^2|u_{z,i}|^2,
\tag{28}
\]

and (25) introduces higher mixed products. Loss matching changes the response directions that must be estimated; it does not algebraically replace these products by unweighted RMS responses.

The energy identity (19) offers a weaker target than a full squared-response estimate. To make it explicit, write the physical parameter direction as \(U=(\Delta W^{(1)},\ldots,\Delta W^{(L)},\Delta w)\), and define \(\xi_a^{(\ell)}=Dz_a^{(\ell)}[U]\), \(\eta_a^{(\ell)}=Dh_a^{(\ell)}[U]=\phi_\ell'(z_a^{(\ell)})\odot\xi_a^{(\ell)}\). Along the affine parameter line \(\theta+\varepsilon U\), the first preactivation has zero second derivative, while for \(\ell\ge2\) its second derivative is
\(2\Delta W^{(\ell)}\eta_a^{(\ell-1)}+W^{(\ell)}D^2h_a^{(\ell-1)}[U,U]\).
Applying the chain rule and recursively pairing the latter term with the backward response gives the exact formula

\[
\begin{aligned}
\nabla^2f_a[U,U]
={}&\frac1n\sum_{\ell=1}^L\sum_i
p_{a,i}^{(\ell)}\phi_\ell''(z_{a,i}^{(\ell)})
\bigl(\xi_{a,i}^{(\ell)}\bigr)^2\\
&+\frac2n\sum_{\ell=2}^L
\delta_a^{(\ell)\top}\Delta W^{(\ell)}\eta_a^{(\ell-1)}
+\frac2n\Delta w^\top\eta_a^{(L)}.
\end{aligned}
\tag{28a}
\]

The first term in (28a) is a signed carrier-weighted square, appearing with an additional residual weight in (19). Controlling that signed quadratic form can be weaker than controlling (28). No such width-uniform mixed expectation is proved here; the point is to retain the more favorable precise target rather than infer that the whole route is ruled out.

For one sample, there is a stronger, useful exact cancellation. On an interval with fixed residual sign, matching positive loss also matches the scalar training prediction \(f\). Therefore \(J U=0\) exactly. With \(j=\nabla f\) and \(k=j^\top Dj>0\), the path can be parametrized directly by the training prediction:

\[
\frac{d\bar\theta}{df}=\frac{Dj}{k},
\qquad
P=I-\frac{Dj\,j^\top}{k},
\qquad
P\frac{dU}{df}=\frac1kPD\nabla^2 f\,U.
\tag{29}
\]

The residual factor cancels from the path equation; the transverse prediction Hessian remains. Every training-prediction variation at fixed loss is zero on the branch, while a test prediction can have \(\nabla f(x)^\top U\ne0\). A cancellation observed only in the scalar training prediction is therefore not a bound on the learned function.

## 6. Endpoint singularity: log loss helps but does not prove uniform second sensitivity

The inverse-loss hitting-time formula (6) divides by \(a\), which is of order \(\rho^2\) under upper and lower Gram bounds. The normalized field (15) removes this explicit singular clock factor because \(\mathcal L/a\) stays bounded. At any fixed positive loss all the preceding equations are regular. At interpolation, however, \(g=0\), the projector \(P\) is undefined by its displayed quotient, and its limiting direction can depend on the residual direction.

The second level constraint in (16) reads

\[
g^\top V=-\frac2m\left\{\|JU\|_2^2+
\sum_a r_a\nabla^2 f_a[U,U]\right\}.
\tag{30}
\]

For multiple samples, a first loss-tangent response need not have \(JU=0\): it is only perpendicular to \(r\). Unless it decays appropriately relative to \(\rho\), the normal component of \(V\) can grow as the loss surface shrinks. The value of a uniformly positive Gram gap does not by itself control this relative response.

The following completely explicit example verifies that this issue can occur even with smooth linear predictions, a common zero initial prediction, and a uniform gap. It is a parameterized linear feature model, **not** the canonical all-layer-trained dense network, so it is not a counterexample to the study's width target.

Let \(m=2\), let \(\theta\in\mathbb R^2\) be the trained state with unit mobility, and fix \(\alpha>2\beta>0\) and \(c>0\). Let \(R_\varepsilon\) be the two-dimensional rotation matrix and set

\[
A_\varepsilon=R_\varepsilon
\begin{pmatrix}\sqrt\alpha&0\\0&\sqrt\beta\end{pmatrix}
R_\varepsilon^\top,
\qquad f_\varepsilon=A_\varepsilon\theta,
\qquad y=(c,0)^\top,
\qquad\theta(0)=0.
\]

For \(\mathcal L=\|f_\varepsilon-y\|_2^2/2\), gradient flow gives

\[
\dot r_\varepsilon=-A_\varepsilon^2r_\varepsilon,
\qquad
r_\varepsilon(t)=-cR_\varepsilon
\begin{pmatrix}e^{-\alpha t}&0\\0&e^{-\beta t}\end{pmatrix}
R_\varepsilon^\top e_1.
\tag{31}
\]

The kernel eigenvalues are \(\alpha,\beta\) for every \(\varepsilon\). The initial loss \(c^2/2\) is common, and \(c\) may be arbitrarily small. Put \(u=e^{-\alpha t}\), \(v=e^{-\beta t}\). At \(\varepsilon=0\), common-time derivatives are

\[
r_0=(-cu,0)^\top,
\qquad \partial_\varepsilon r|_0=(0,c(v-u))^\top,
\qquad \partial_\varepsilon^2 r|_0=(-2c(v-u),0)^\top.
\tag{32}
\]

Both derivatives are bounded uniformly for all \(t\ge0\). The state satisfies \(\theta_\varepsilon=A_\varepsilon^{-1}(y+r_\varepsilon)\); since \(A_\varepsilon^{-1}\) and its first two derivatives are bounded locally in \(\varepsilon\), the same-time state sensitivities are uniformly bounded too.

Now match each trajectory to the reference loss \(c^2u^2/2\). At \(\varepsilon=0\), its hitting-time first derivative is zero because \(r_0^\top\partial_\varepsilon r=0\). Thus the matched first residual derivative is still \((0,c(v-u))^\top\). Twice differentiating the equal-norm constraint yields

\[
r_0^\top\bar r''_0+\|\bar r'_0\|_2^2=0,
\qquad
(\bar r''_0)_1=c\frac{(v-u)^2}{u}
\sim c e^{(\alpha-2\beta)t}\longrightarrow\infty.
\tag{33}
\]

For a direct check, the fixed-time second loss derivative is \(c^2(v^2-u^2)\), the loss velocity is \(-\alpha c^2u^2\), and (6) gives \(t''_0=((v/u)^2-1)/\alpha\). Adding \(\dot r_0t''_0\) to the second derivative in (32) yields (33).

Replacing the loss level by its logarithm does not alter (33): the same matched states are selected, and \(s=2\alpha t\) on the reference path. Every matched prediction converges to \(y\), so its derivative taken **after** passage to the endpoint is zero. Its second derivative taken first at finite matched loss is unbounded as the endpoint approaches. Uniform convergence of the predictions does not justify exchanging these operations.

This example distinguishes an obstruction to a uniform second-sensitivity proof from a lower bound on finite-width prediction error. Here the common-time first and second derivatives stay bounded, and the fitted endpoint depends smoothly on the feature parameter. No slow-width claim follows.

Indeed, even the finite matched-loss differences in this example are uniformly Lipschitz in \(\varepsilon\). More generally, suppose both residual paths obey \(\dot r=-2\Gamma r\), share the same initial residual RMS, fit to zero, and satisfy \(\lambda I\preceq\Gamma\preceq\Lambda I\). With \(\rho=\|r\|_2/\sqrt m>0\),

\[
\frac{\|\dot r\|_2}{\sqrt m}\le2\Lambda\rho,\qquad
-\dot\rho=\frac{2r^\top\Gamma r}{m\rho}\ge2\lambda\rho,
\qquad
\frac1{\sqrt m}\left\|\frac{dr}{d\rho}\right\|_2\le\frac\Lambda\lambda.
\]

At reference time \(t\), put \(e(t)=\|r_\varepsilon(t)-r_0(t)\|_2/\sqrt m\). The difference of their residual RMS values is at most \(e(t)\). Move the perturbed residual along its own path to the time \(t_\varepsilon\) at residual RMS \(\rho_0(t)\). Integrating the last display and applying the triangle inequality gives

\[
\frac{\|r_\varepsilon(t_\varepsilon)-r_0(t)\|_2}{\sqrt m}
\le\left(1+\frac\Lambda\lambda\right)e(t).
\tag{34}
\]

For the rotation model, (31) gives \(\sup_t e(t)\le Cc|\varepsilon|\), and \(\Lambda/\lambda=\alpha/\beta\). Thus (34) proves a uniform \(O(|\varepsilon|)\) matched-residual comparison despite (33). The divergence tests second smoothness, not even failure of a first-order finite-difference bound.

## 7. What this assessment establishes and leaves open

The exact first and second matched-loss formulas are (6)–(13), with all explicit initialization dependence of the observable included. For a physical dense initialization variation, (17)–(22) give the corresponding normalized differential equations. Pure speed changes cancel exactly. The surviving first-order transverse Hessian and second-order third-derivative and speed–direction products are explicit.

Loss matching therefore does not, by algebra alone, close the finite mixed carrier-response estimates in `WEIGHTED_MOMENT_STATUS.md`. A useful next estimate could exploit the dissipative term and residual weight in (19), or special structure of the actual initialization directions, rather than demand a uniform worst-direction Hessian bound. Such an estimate is not proved here. Nor is it proved impossible: the reflection identity tests universal pointwise cancellation, not probabilistic cancellation of the actual Gaussian response.

For a finite-to-population theorem one still needs a comparison that identifies population bias, controls adapted Gaussian responses, and specifies whether the target is common physical time, common loss, or the fitted endpoint. A matched-loss theorem alone would not give the study's common-time metric without controlling the remaining difference in traversal speed. Conversely, the linear example does not rule out direct matched-loss comparison bounds that avoid a uniform second derivative.

### Inputs and audit scope

This scoped calculation used the dense setting in `paper/main.tex` (lines 175–205), the tangent-Gram/fitting statements and regularity scope in `paper/proof_alltime.tex` (lines 1–20, 276–339, 697–820), `docs/notation.qmd`, and this study's complete `README.md`, `RESULT.md`, and `WEIGHTED_MOMENT_STATUS.md`. Links from those study notes were not followed. After the initial derivation was frozen, the coordinator suggested the signed Hessian expansion (28a) and finite-difference observation (34); their full derivations are included here. No other study, numerical experiment, or external theorem was a scientific input. Required canonical-notation and rigorous-math skills, including the neural-network reference, were applied.

Source SHA-256 at reading:

```text
60c43aa3a5a53a04a94cec27d72858f1a28b35ee6c17c52001c83612a396aa95  paper/main.tex
f3f0a0f5d0f553ced7c7334863bc04734033d00ecef48cd2031194dda374035d  paper/proof_alltime.tex
78e11eb3dafc5321a8a3923742993c0bad78df53b0e80b6319f16e48f0131023  docs/notation.qmd
7336adc83d44f99a13e772b0359c071527b5d73754d9a021bf469c4e3d504b0d  studies/dense_cutoff_population_rate_20261001/README.md
aaea301f9563980706e967811a44306c6a5156d9a8bb45f9c2e39d5f3debb8c8  studies/dense_cutoff_population_rate_20261001/RESULT.md
4e3447ef9ecb53109aa1354354316cf28192d01f0123e6c0e94f1a2d4b356f23  studies/dense_cutoff_population_rate_20261001/WEIGHTED_MOMENT_STATUS.md
```
