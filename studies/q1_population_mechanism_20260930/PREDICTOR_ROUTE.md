# Independent predictor route: causal selection and its limits

First note frozen independently, 2026-09-30: Sections 1–6 are a prompt-only theoretical derivation of the supplied finite-width, finite-sample q=1 system. No other scientific source, study history, experiment, or other route was consulted for that note. Section 7 is a post-freeze verification and extension of the supervisor's moving-span mechanism, explicitly identified below. Section 8 records two additional identities obtained in this route. The investigate-conjectures and solve-math-rigorously skills supplied process instructions only.

The strongest conclusion is an exact causal representation: readout learning integrates residuals against a moving feature dictionary, while the q=1 memory binds each sample's integrated write vector to a residual-clock average of that sample's address. This factorization gives a precise selection mechanism, including a provable initial alignment of signed values. It does not select a universal endpoint classifier from the labels alone. The whole-circle predictor remains odd, and residual extinction preserves rather than removes its accumulated history.

## 1. Object, scope, and notation

Fix finite n,m,d, training inputs x_a in R^d with ||x_a||^2=d, and labels y_a in {-1,1}. All statements concern the exact ODE in the assignment, for each fixed realization of A_0 and W_0. The Gaussian initialization is needed only for distributional symmetry statements; no width or sample limit is taken. No dense-model replacement is made.

Write E_a for m^{-1} sum_a and set

\[
B=W_0+\mathbb E_a\frac{v_a k_a^\top}{n},\quad
h_t(x)=\tanh(A_t x/\sqrt d),\quad
g_t(x)=\tanh(B_t h_t(x)),\quad
f_t(x)=\frac{w_t^\top g_t(x)}n.
\]

For any query x, define

\[
d_t(x)=w_t\odot(1-g_t(x)^2),\qquad
\ell_t(x)=(1-h_t(x)^2)\odot B_t^\top d_t(x).
\]

The training quantities d_a and ell_a are these fields evaluated at x_a. The error is r_a=f_t(x_a)-y_a, and rho=(E_a r_a^2)^{1/2}. The initial conditions are w_0=v_{a,0}=0, k_{a,0}=h_0(x_a), tau_0=1.

All finite-time formulas below are exact identities. Endpoint statements explicitly give the additional hypotheses needed. The requested observable is the entire function f_t on the sphere, especially the circle when d=2.

## 2. The clock makes keys causal averages, not current similarities

Let

\[
R(t)=\int_0^t\rho(s)\,ds,\qquad \tau(t)=1+R(t).
\]

The key equation has an exact integrating factor:

\[
\frac{d}{dt}(\tau k_a)
=\rho k_a+\tau\frac{\rho}{\tau}(h_a-k_a)
=\rho h_a.
\]

Consequently

\[
k_a(t)=\frac{h_0(x_a)+\int_0^t\rho(s)h_s(x_a)\,ds}{1+R(t)}.
\tag{2.1}
\]

In particular every component of k_a remains in [-1,1]. Define the probability measure on past times

\[
\mu_t(du)=\frac{\delta_0(du)+\mathbf 1_{[0,t]}(u)\rho(u)\,du}{1+R(t)}.
\]

Then retrieval uses the exact history-to-present similarity

\[
q_{a,t}(x)=\frac{k_a(t)^\top h_t(x)}n
=\int\frac{h_u(x_a)^\top h_t(x)}n\,\mu_t(du).
\tag{2.2}
\]

This is bounded by one in absolute value. Its training matrix need not be symmetric or positive semidefinite: a past feature and a present feature occur on different sides. The spatiotemporal kernel h_u(x)^T h_t(x')/n is a Gram kernel on pairs (time,input), but fixing different time arguments on its two sides does not produce a symmetric kernel on the training inputs.

On any interval with rho>0, R is an increasing clock and the complete equations become

\[
\frac{dw}{dR}=-2\mathbb E_a e_a g_a,\qquad
\frac{dv_a}{dR}=-2e_a d_a,\qquad
\frac{dA}{dR}=-2\mathbb E_a e_a\ell_a x_a^\top/\sqrt d,
\qquad
\frac{dk_a}{dR}=\frac{h_a-k_a}{1+R},
\tag{2.3}
\]

where e_a=r_a/rho and E_a e_a^2=1. Thus residual magnitude sets the physical speed along the trajectory, whereas the normalized residual direction determines parameter motion per unit accumulated error. Keys perform a Cesaro average in accumulated error. Equivalently dk_a/d(log tau)=h_a-k_a. This exponential averaging is in log tau, not in physical time.

The value equation integrates to

\[
v_a(t)=-2\int_0^t r_a(s)d_s(x_a)\,ds.
\tag{2.4}
\]

Combining (2.1) and (2.4) yields

\[
B_t-W_0
=-\frac2n\mathbb E_a
\int_0^t\!\int
r_a(s)d_s(x_a)h_u(x_a)^\top\,\mu_t(du)\,ds.
\tag{2.5}
\]

This is the specific q=1 organizing principle. Conditional on the sample index a, write time s and address time u are factored. Their only binding is the common sample identity. A write made at one time is subsequently paired with every address represented in that sample's current key, including addresses learned after the write. The predictor is nevertheless causal because both times remain at most t. Equation (2.5) must not be replaced by a single-time integral of r_a(s)d_s(x_a)h_s(x_a)^T: that would change the model.

## 3. The exact moving-dictionary representer formula

Since w_0=0,

\[
w_t=-2\int_0^t\mathbb E_a r_a(s)g_s(x_a)\,ds.
\]

Therefore, simultaneously for every query x,

\[
f_t(x)=-2\int_0^t\mathbb E_a r_a(s)
\underbrace{\frac{g_s(x_a)^\top g_t(x)}n}_{C((s,x_a),(t,x))}\,ds.
\tag{3.1}
\]

C is a positive semidefinite Gram kernel on the enlarged set of time-input pairs: for finitely many pairs z_j=(t_j,x_j) and coefficients c_j,

\[
\sum_{i,j}c_i c_j C(z_i,z_j)
=\frac1n\left\|\sum_i c_i g_{t_i}(x_i)\right\|^2\ge0.
\]

Equation (3.1) is a causal representer identity with an evolving dictionary. It is not a representer theorem in a fixed data kernel: the kernel itself depends on the supervised trajectory. It describes selection by signed residual history, not simply by the final labels or the final feature Gram matrix.

The complete predictor velocity makes the distinction sharper. Let alpha=rho/tau. Direct differentiation gives

\[
\dot B=-2\mathbb E_a r_a\frac{d_a k_a^\top}{n}
+\alpha\mathbb E_a\frac{v_a(h_a-k_a)^\top}{n}.
\tag{3.2}
\]

The chain rule is

\[
\dot f_t(x)=\frac{\dot w^\top g_t(x)}n
+\frac{d_t(x)^\top\dot B h_t(x)}n
+\frac{\ell_t(x)^\top\dot A x}{n\sqrt d}.
\]

Substitution yields

\[
\begin{aligned}
\dot f_t(x)={}&-2\mathbb E_a r_a\left[
\frac{g_t(x)^\top g_a}{n}
+\frac{\ell_t(x)^\top\ell_a}{n}\frac{x^\top x_a}{d}
+\frac{d_t(x)^\top d_a}{n}\frac{k_a^\top h_t(x)}n
\right]\\
&+\alpha\mathbb E_a
\frac{d_t(x)^\top v_a}{n}
\frac{(h_a-k_a)^\top h_t(x)}n.
\end{aligned}
\tag{3.3}
\]

The first two interactions are symmetric positive semidefinite kernels. The third is generally a directed interaction. The last term is address motion acting on stored values.

One can isolate an ordinary instantaneous tangent kernel without discarding the discrepancy. Put delta_a=h_a-k_a and

\[
K_t(x,x_a)=\frac{g_t(x)^\top g_a}{n}
+\frac{\ell_t(x)^\top\ell_a}{n}\frac{x^\top x_a}{d}
+\frac{d_t(x)^\top d_a}{n}\frac{h_t(x)^\top h_a}{n}.
\]

Its three feature maps are g/sqrt(n), (ell tensor x)/sqrt(nd), and (d tensor h)/n, so its training matrix is positive semidefinite. The exact equation is

\[
\dot f_t(x)=-2\mathbb E_a r_a K_t(x,x_a)+E_t(x),
\tag{3.4}
\]

\[
E_t(x)=\mathbb E_a
\frac{d_t(x)^\top(2r_a d_a+\alpha v_a)}n
\frac{\delta_a^\top h_t(x)}n.
\tag{3.5}
\]

For L=E_a r_a^2 this gives

\[
\dot L=-4\mathbb E_{a,b}r_a r_bK_t(x_a,x_b)
+2\mathbb E_a r_aE_t(x_a).
\tag{3.6}
\]

The first term is nonpositive; the second has no sign supplied by these identities. This route therefore does not establish monotonic loss. At a moment when every k_a=h_a the defect vanishes, but this equality is not preserved in general: the key derivative is then zero while the current feature derivative need not be. Treating (3.4) as an ordinary fixed-kernel gradient flow deletes an actual state-dependent term.

## 4. A provable, limited class-alignment mechanism

Let

\[
b=\dot w_0=2\mathbb E_a y_a g_0(x_a),\qquad
D_a=\operatorname{diag}(1-g_0(x_a)^2).
\]

The initial identities are

\[
\dot A_0=\dot v_{a,0}=\dot k_{a,0}=0,\qquad \rho_0=1.
\]

The vector field is smooth near time zero because rho_0>0. Hence w_t=tb+O(t^2), A_t=A_0+O(t^2), v_a=O(t^2), B_t=W_0+O(t^2), and g_t=g_0+O(t^2). Substituting these into the value equation gives

\[
\dot v_a(t)
=-2(-y_a+O(t))(tD_ab+O(t^2))
=2t y_aD_ab+O(t^2),
\]

and therefore

\[
v_a(t)=t^2 y_aD_ab+O(t^3).
\tag{4.1}
\]

For any training pair a,c,

\[
y_a y_c\,v_a(t)^\top v_c(t)
=t^4\sum_i b_i^2(D_a)_{ii}(D_c)_{ii}+O(t^5).
\tag{4.2}
\]

Every diagonal entry of D_a is strictly positive for finite initial weights. If b is nonzero, the leading coefficient in (4.2) is strictly positive. Since there are finitely many pairs, there is a common sufficiently small positive time interval on which all class-signed values have positive pairwise inner products. Thus same-class values initially have positive inner product, and opposite-class values have negative inner product.

This is an actual local-in-time alignment theorem. It concerns values, not keys, and does not imply within-class collapse: the coordinate gates D_a differ by sample. The key equation further gives k_a(t)=h_0(x_a)+O(t^3), because h_a-k_a=O(t^2). The initial retrieval geometry is therefore label independent through order t^2 even though the values already encode the labels at order t^2.

If b=0, an exact arrested solution exists for all time:

\[
w=v_a=0,\quad A=A_0,\quad k_a=h_0(x_a),\quad \tau=1+t.
\tag{4.3}
\]

It solves every equation, so uniqueness makes it the actual trajectory. The local alignment theorem has a substantive nondegeneracy condition; a vanishing initial supervised readout force does not spontaneously restart through another block.

An all-time conditional version is also transparent. Since r_a=y_a(y_af_a-1),

\[
y_av_{a,i}(t)
=2\int_0^t(1-y_af_s(x_a))w_i(s)(1-g_{s,i}(x_a)^2)\,ds.
\tag{4.4}
\]

If every training margin remains at most one and each coordinate w_i has a fixed sign over the interval, then all y_av_a lie in the same closed coordinate orthant. Their pairwise inner products are nonnegative. Overshoot or sign changes invalidate that argument. Neither condition was assumed in the original model, so (4.4) does not justify unconditional late-time alignment.

## 5. What residual extinction selects, and what it leaves free

At a state with r_a=0 for every sample, rho=0 and every state derivative is zero. In particular both keys and values freeze. Interpolation itself imposes only

\[
\frac1nG_*^\top w_*=y,
\quad G_*=[g_*(x_1),\ldots,g_*(x_m)].
\tag{5.1}
\]

It imposes no further algebraic condition on current keys, key-current-feature mismatch, or off-sample predictions.

There is also a useful finite-time qualification. The ODE is locally Lipschitz on tau>0: rho is a norm of a smooth residual vector, hence locally Lipschitz, and all other operations are smooth there. At an interpolating state its constant continuation is a solution. Uniqueness also holds backward locally, by applying the same local uniqueness argument to the negated vector field. A nonstationary trajectory cannot meet such a constant solution at a finite time. Since r_a(0)=-y_a is nonzero, exact residual extinction cannot occur at finite time along this initialization. Discussion of fitting therefore concerns an asymptotic endpoint or an approximate numerical stopping criterion.

For completeness, no finite-time blowup obstructs these statements. From ||g||<=sqrt(n),

\[
\|w_t\|\le2\sqrt n\,R(t),\qquad
\rho(t)\le1+\|w_t\|/\sqrt n\le1+2R(t).
\]

Thus R(t)<=(e^{2t}-1)/2. Also

\[
\mathbb E_a\|v_a(t)\|
\le2\int_0^t\rho(s)\|w_s\|\,ds
\le2\sqrt n\,R(t)^2,
\]

and

\[
\|B_t\|_{op}\le\|W_0\|_{op}+2R(t)^2,\qquad
\|\dot A_t\|_F\le2\rho(t)\|B_t\|_{op}\|w_t\|.
\tag{5.2}
\]

The keys are bounded, and for finite m each value is bounded by its finite sum of norms. These bounds control every state component on compact time intervals, while tau>=1. Local solutions consequently extend to every finite time.

If the accumulated error is finite,

\[
R_\infty=\int_0^\infty\rho(t)\,dt<\infty,
\tag{5.3}
\]

the same estimates prove finite total variation of w, every v_a, and A. For the keys, ||dot k_a||<=2sqrt(n)rho/tau is integrable. All states, including tau, therefore converge. Their residual has a limit by continuity. Its norm must be zero, since a positive limiting rho would contradict (5.3). This is a sufficient convergence theorem, not a proof that (5.3) holds for all data.

Under (5.3), the limiting key is

\[
k_{a,*}=\frac{h_0(x_a)+\int_0^\infty\rho(s)h_s(x_a)\,ds}{1+R_\infty}.
\tag{5.4}
\]

The initial feature retains weight 1/(1+R_infty)>0. There is no requirement that k_{a,*}=h_*(x_a). In contrast, if R(t) tends to infinity and h_t(x_a) converges to h_*(x_a), then (2.1) gives k_a(t)->h_*(x_a). To verify this, split the integral at a time S after which ||h_s-h_*||<epsilon: the finite early contribution divided by 1+R(t) vanishes, and the late contribution is at most epsilon. Residual convergence to zero alone does not determine which clock regime occurs.

Even for a convergent interpolating trajectory, (3.1) is generally not the minimum-norm readout for the final features. Let P_* be orthogonal projection onto the column span of G_*. Assuming (5.3), the endpoint identity gives

\[
(I-P_*)w_*
=-2\int_0^\infty\mathbb E_a
r_a(s)(I-P_*)g_s(x_a)\,ds.
\tag{5.5}
\]

The left side is invisible on the training set, but it can affect a query whose final feature vector has a component in the same direction. For fixed final features, the minimum Euclidean norm interpolating readout is

\[
w_{\min}=nG_*(G_*^\top G_*)^+y,
\]

and every interpolating readout is w_min+w_perp with G_*^T w_perp=0. Equation (5.5) identifies the exact causal source of w_perp. In a genuinely frozen-feature model it is zero because every past feature lies in the final span. Here no such span invariance has been shown. This is not a proof that every trajectory has a nonzero w_perp; it is the missing condition in any minimum-norm claim.

All interpolating states are equilibria, but that fact alone does not characterize which equilibria are reachable from the prescribed random initialization. A stronger implicit-bias theorem would need a reachability or trajectory argument. No maximum-margin or universal fitting conclusion is obtained here.

## 6. Whole-circle geometry: exact restrictions and a clock effect

For every state and every x,

\[
h_t(-x)=-h_t(x),\quad g_t(-x)=-g_t(x),\quad
f_t(-x)=-f_t(x).
\tag{6.1}
\]

This follows from the oddness of tanh and the absence of biases, independently of the labels and training set. On the circle x(theta)=sqrt(2)(cos theta,sin theta),

\[
f_t(\theta+\pi)=-f_t(\theta).
\]

Thus only odd Fourier harmonics occur. Wherever the classifier sign is nonzero, antipodal points receive opposite classes. Equal labels at two antipodal training points cannot both be interpolated.

At a finite state, f_t(theta) is real analytic because it is a finite composition of analytic functions. Unless it vanishes identically, it has finitely many zeros on the compact circle: otherwise some zeros would accumulate, and the local power series at an accumulation point would have every coefficient zero, forcing the function to vanish on the connected circle. Its zero set is antipodally paired. A nonzero value and its negative at the antipode also force at least one zero on each intervening semicircle. These facts constrain the entire decision function, while neither prescribing its boundary locations nor proving the labels determine them.

There is an additional subtlety when the empirical input measure is antipodally symmetric. Assume indices occur in equal-weight pairs a,bar(a), with x_bar(a)=-x_a. Define

\[
y_{o,a}=(y_a-y_{\bar a})/2,\qquad
y_{e,a}=(y_a+y_{\bar a})/2.
\]

The subscripts o and e denote odd and even parts. Since f is odd,

\[
\rho^2=\mathbb E_a(f(x_a)-y_{o,a})^2+\mathbb E_a y_{e,a}^2.
\tag{6.2}
\]

The cross term cancels between antipodal pairs. Moreover k_bar(a)=-k_a for all time by (2.1), while d_bar(a)=d_a. Decomposing values into v_o=(v_a-v_bar(a))/2 and v_e=(v_a+v_bar(a))/2 gives

\[
\dot v_{o,a}=-2(f(x_a)-y_{o,a})d_a,\qquad
\dot v_{e,a}=2y_{e,a}d_a.
\]

The even contribution cancels in the memory matrix:

\[
\mathbb E_a v_a k_a^\top=\mathbb E_a v_{o,a} k_a^\top.
\]

It also cancels directly in the readout and A forces, because g_a and ell_a x_a^T are odd in x_a. Nevertheless it survives in (6.2), hence in the common key clock rho/tau. An unrepresentable even label component can therefore influence evolution of the representable odd predictor indirectly through address timing. It is not generally valid to remove it from the dataset and claim the same training trajectory. This states a dynamical channel, not a claim that it changes the predictor for every instance. If the entire label function is even, the initial force b vanishes and (4.3) applies.

Finally, input rotations produce equivariance only when the initialization is rotated with the data: replacing x by Qx and A by AQ^T for orthogonal Q preserves every activation and equation. The Gaussian law of A_0 is invariant under this transformation, so the randomized algorithm is equivariant in distribution. A single fixed initialization does not make its realized whole-circle predictor rotationally symmetric. Global label reversal is another exact symmetry: y,r,w,d,ell,f reverse sign, while A,k,v,B,tau remain unchanged. In particular feature learning is unchanged by reversing the class names.

## 7. Post-freeze result: training-invisible readout motion changes the whole function

The supervisor supplied the moving-span identity, its proposed cubic expansion, and the two-neuron example after this route's independent first note was frozen. This section checks the derivations and adds an explicit whole-circle consequence. It is not an independent rediscovery.

Let G_t=[g_t(x_1),...,g_t(x_m)], let S_t be its column span, and let P_t be Euclidean orthogonal projection onto S_t. Work on an interval of constant rank on which P_t is differentiable. In particular this holds near zero if G_0 has full column rank. Define

\[
q_t=(I-P_t)w_t.
\]

Because dot w_t belongs to S_t, direct differentiation gives

\[
\dot q_t=-\dot P_t w_t,
\qquad
q_t=-\int_0^t\dot P_s w_s\,ds
\tag{7.1}
\]

when the interval starts at zero. The identity is about a moving subspace: its rotation can leave a component of the accumulated readout outside the current training-feature span, despite every instantaneous readout update being inside that span.

At any time, put F_t=(f_t(x_1),...,f_t(x_m))^T and

\[
K_t=G_t^\top G_t/n,\qquad \kappa_t(x)=G_t^\top g_t(x)/n.
\]

Here kappa_t(x) is a vector of output-feature kernel evaluations. Since G_t^T w_t=nF_t, orthogonal projection gives

\[
P_t w_t=nG_t(G_t^\top G_t)^+F_t.
\]

Using (G_t^T G_t/n)^+=n(G_t^T G_t)^+, the whole function splits exactly as

\[
f_t(x)=\kappa_t(x)^\top K_t^+F_t
+\frac1n g_t(x)^\top q_t.
\tag{7.2}
\]

The first term is the minimum-Euclidean-norm readout that matches the current training outputs with the current features. The second term vanishes at every training input but can survive elsewhere. Thus a changing feature span supplies an explicit causal mechanism by which present training outputs fail to specify the present whole-input function, even after the current features are given.

To determine whether this mechanism actually occurs in the specified flow, write

\[
b_t=\mathbb E_a y_a g_t(x_a),\qquad
H_t=\mathbb E_a g_t(x_a)g_t(x_a)^\top.
\]

Thus the vector called b in Section 4 equals 2b_0 in this section. The readout equation is

\[
\dot w_t=2b_t-\frac2nH_tw_t.
\tag{7.3}
\]

At initialization, dot A_0=dot B_0=0, so dot G_0=dot b_0=dot H_0=0. Repeated differentiation of (7.3) then yields

\[
\dot w_0=2b_0,\quad
\ddot w_0=-\frac4nH_0b_0,\quad
w^{(3)}_0=2\ddot b_0+\frac8{n^2}H_0^2b_0.
\]

Consequently

\[
w_t=2tb_0-\frac2n t^2H_0b_0
+t^3\left(\frac{\ddot b_0}{3}+\frac4{3n^2}H_0^2b_0\right)+O(t^4).
\tag{7.4}
\]

If G_0 has full column rank, its projector is smooth near zero and dot P_0=0. Differentiating P_tG_t=G_t twice gives

\[
\ddot P_0G_0=(I-P_0)\ddot G_0,
\qquad \ddot P_0b_0=(I-P_0)\ddot b_0.
\]

Also b_0,H_0b_0,H_0^2b_0 belong to S_0. Substitution of P_t=P_0+t^2 ddot P_0/2+O(t^3) and (7.4) therefore gives the verified coefficient

\[
q_t=-\frac23t^3(I-P_0)\ddot b_0+O(t^4).
\tag{7.5}
\]

This is nonzero at small times whenever the initial feature acceleration has a component outside the initial training-feature span that survives the label-weighted average.

Here is a concrete nondegenerate q=1 example. Take n=2,m=1,y=1,W_0=I_2, and choose 0<h_1<h_2<1 for the two coordinates of h_0(x_1). Write g_i=tanh(h_i), D_i=1-g_i^2, E_i=1-h_i^2, and s=(h_1^2+h_2^2)/2. The initial equations give

\[
\dot w_0=2g,\qquad
\ddot v_0=4g\odot D,\qquad
\ddot h_0=4E^2\odot g\odot D,
\]

where the last identity follows from dot A x_1/sqrt(d)=diag(1-h^2)B^T dot v for one sample. Since B=W_0+vk^T/n and v_0=dot v_0=0,

\[
\ddot B_0=4(g\odot D)h^\top/n.
\]

Thus dot z_0=0 and

\[
\ddot z_{0,i}=4g_iD_i(E_i^2+s),\qquad
\frac{\ddot g_{0,i}}{g_i}
=4(1-g_i^2)^2\big[(1-h_i^2)^2+s\big].
\tag{7.6}
\]

For fixed s>0, the function

\[
u\longmapsto4\operatorname{sech}^4(u)\big[(1-u^2)^2+s\big]
\]

is strictly decreasing on (0,1): its first factor is positive and strictly decreasing, and its second factor is positive and has derivative -4u(1-u^2)<0. The two ratios in (7.6) are unequal. Hence ddot g_0 is not parallel to g_0, and (I-P_0)ddot b_0 is nonzero because b=g for this one positive sample. Equation (7.5) proves actual training-invisible motion at order t^3 in this exact q=1 trajectory.

The example can be placed on the circle without losing the effect. Take d=2,x_1=sqrt(2)e_1, and choose an invertible A_0 whose first column is (atanh h_1,atanh h_2)^T. Choose a circle query x perpendicular to the first row of A_0. Invertibility ensures that the second row has nonzero inner product with x. Since W_0=I_2,

\[
g_0(x)=(0,\gamma)^\top,\qquad \gamma\ne0.
\]

The nonzero vector c=(I-P_0)ddot g_0 is perpendicular to g_0(x_1), whose two coordinates are positive. Therefore both coordinates of c are nonzero, in particular g_0(x)^T c is nonzero. Combining (7.2) and (7.5) gives

\[
f_t(x)-\kappa_t(x)^\top K_t^+F_t
=-\frac{2}{3n}t^3g_0(x)^\top c+O(t^4),
\tag{7.7}
\]

which is nonzero at this query for all sufficiently small positive t. It vanishes exactly at the training input. This proves a difference in the whole-circle scalar prediction, rather than merely a difference in unobserved parameter coordinates.

The displayed W_0=I_2 is a convenient deterministic witness, not a claim about a positive probability of drawing exactly that matrix. All relevant nonzero coefficients depend continuously on A_0,W_0 near the witness. They persist on an open neighborhood. The prescribed Gaussian initialization has positive density on that neighborhood, so the effect occurs with positive probability under the actual initialization law. This establishes a robust phenomenon; no claim of a particular probability or all-realization behavior is needed.

At a convergent interpolating endpoint, (7.2) becomes

\[
f_*(x)=\kappa_*(x)^\top K_*^+y+g_*(x)^\top q_*/n.
\tag{7.8}
\]

Neither early nonzero q_t nor (7.1) proves q_* is nonzero: subsequent span motion could cancel it. The rigorous outcome is that q=1 generates this component during learning, not a theorem that every final classifier retains it.

## 8. Two further exact selection constraints

Let U=span{x_1,...,x_m}, and let Q be orthogonal projection onto U. Every read-in update has its right factor in U, so

\[
A_t(I-Q)=A_0(I-Q).
\tag{8.1}
\]

More strongly, if Delta A annihilates every training input, then replacing A_0 by A_0+Delta A produces exactly the same training activations and all the same w,v,k,B,tau trajectories, with A_t replaced by A_t+Delta A. Substitution into each ODE verifies this statement, and uniqueness identifies the trajectory. Consequently unobserved input directions retain an initialization-dependent embedding. On a circle this mechanism is available for data supported on one diameter; it is absent once the input vectors span R^2. This is an explicit geometric limit on training-based function identification, not a claim about arbitrary full-span datasets.

There is also a useful exact balance law for one sample at arbitrary n. Put a_t=A_t x_1/sqrt(d) and define Phi componentwise by

\[
\Phi(u)=u/2+\sinh(2u)/4,\qquad \Phi'(u)=\cosh^2u.
\]

The identity dot a=diag(1-h^2)B^T dot v implies

\[
\frac{d}{dt}\Phi(a_t)=B_t^\top\dot v_t
=W_0^\top\dot v_t+k_t\frac{d}{dt}\frac{\|v_t\|^2}{2n}.
\]

Integration by parts, using v_0=0, gives

\[
\Phi(a_t)-\Phi(a_0)
=W_0^\top v_t+k_t\frac{\|v_t\|^2}{2n}
-\int_0^t\frac{\|v_s\|^2}{2n}\dot k_s\,ds.
\tag{8.2}
\]

The last term is an exact address-motion contribution to feature selection. If the keys are artificially frozen, it vanishes and leaves an endpoint invariant. For the actual q=1 flow it must be retained. This provides a concrete balance-law explanation of path dependence in the learned representation, without asserting that arbitrary paths are dynamically reachable.

## 9. Status and the remaining bottleneck

| Claim | Status | Exact limitation |
|---|---|---|
| Residual-clock averaging of keys, factored write/address histories | Proved identities | Finite n,m |
| Whole-query causal representer and tangent-kernel-plus-defect evolution | Proved identities | Trajectory-dependent kernels and a sign-indefinite defect remain |
| Initial alignment of class-signed values | Proved for b nonzero and sufficiently small positive time | Neither key alignment nor late-time class collapse |
| Arrest when the initial supervised readout force vanishes | Proved | Does not classify all nonfitting trajectories |
| Global existence at every finite time | Proved by explicit bounds | Bounds can grow with time |
| Convergence and interpolation under finite accumulated residual | Proved conditional theorem | Integrability of rho is not established universally |
| Odd whole-circle predictor and parity-mediated clock channel | Proved | No unique decision boundary follows |
| Generation of a readout component invisible on the training inputs | Proved with a robust explicit q=1 example | Early nonzero does not imply endpoint nonzero |
| Read-in nullspace conservation and one-sample address-motion balance | Proved exact identities | Nullspace result requires unspanned input directions |
| Minimum norm, maximum margin, universal fitting | Not established | Each needs a new structural argument |

The remaining selected-function bottleneck is endpoint persistence: identify a nondegenerate class of fitting trajectories for which the moving-span contribution in (7.8) provably survives, or prove a cancellation principle under explicit conditions. The early-time witness rules out a mechanism that keeps the readout in the current training-feature span throughout learning. It does not by itself decide that endpoint question. The finite-clock memory in (5.4) and address-motion balance (8.2) are additional exact constraints that an endpoint selection theorem must respect.
