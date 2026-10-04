# How the q=1 populations learn and select a function

This study treats the autonomous finite-order system as a learning algorithm in its own right. It asks no question about further compression or approximation to another training algorithm. Sections 1--7 retain the earlier finite-width results for two tanh hidden layers, no biases, finitely many equally weighted inputs of norm sqrt(d), labels in {-1,1}, and zero initial readout and value memories. Section 8 records the preceding two-sample population result. The latest request continues **direct infinite-width neuron population dynamics** on a chosen structured finite dataset; Section 9 gives the four-point latent-factor acquisition result. The earlier finite-neuron examples do not establish the population conclusions. Check status is recorded per result in README.md; none is promoted book material. No training experiments were run; the new result uses certified scalar initialization integrals.

The organizing mechanism is: **initial feature–label correlation starts the readout; this signal initially reinforces itself through feature motion; changing feature geometry then influences both fitting and the function selected away from the training inputs.** The first two links have an exact local theorem. The last now has an actual fitted-endpoint theorem: unequal sustained reinforcement can leave a historical readout component that changes both unseen predictions and the decision boundary. The theorem is for two neurons and one training input on an open initialization set; a general multi-input convergence or final implicit-bias theorem is not claimed.

The continuation read the complete current manuscript and its included appendices. [MANUSCRIPT_RECONCILIATION.md](MANUSCRIPT_RECONCILIATION.md) records the exact dictionary k_a=bar h_(a,0)/tau and v_a=-2 bar delta_(a,0), with unchanged physical time and learning rates. The present zero-readout model is exactly the manuscript's q=1 learning-speed instance. It is distinct from a generic small nonzero finite-width readout initialization.

## 1. The object, without an external training reference

Write <a,b>_n=a^T b/n. There are a read-in A, readout w, and for each training input x_a a key k_a and value vector v_a. The fixed matrix W0 mixes the two hidden populations. At any query x,

\[
h(x)=\tanh(Ax/\sqrt d),\qquad
z(x)=W_0h(x)+\frac1m\sum_a v_a\langle k_a,h(x)\rangle_n,
\]
\[
g(x)=\tanh z(x),\qquad f(x)=\langle w,g(x)\rangle_n.
\tag{1}
\]

Initially A and W0 have independent entries N(0,1) and N(0,1/n), respectively; w=v_a=0, k_a=h_0(x_a), and tau=1. Put r_a=f(x_a)-y_a, rho=(mean r_a^2)^(1/2), and

\[
d_a=w\odot(1-g_a^2),\qquad
\ell_a=(1-h_a^2)\odot\left[W_0^Td_a+
\frac1m\sum_b k_b\langle v_b,d_a\rangle_n\right].
\]

The complete intrinsic evolution is

\[
\dot w=-2\operatorname{mean}_a r_ag_a,\quad
\dot A=-2\operatorname{mean}_a r_a\ell_ax_a^T/\sqrt d,
\]
\[
\dot v_a=-2r_ad_a,\qquad
\dot k_a=\frac\rho\tau(h_a-k_a),\qquad \dot\tau=\rho.
\tag{2}
\]

The d and ell fields specify the coupling, and are not additional states. Use B=W0+mean(v_a k_a^T)/n only as a derived algebraic abbreviation when useful.

Integrating the key equation gives

\[
k_a(t)=\frac{h_0(x_a)+\int_0^t\rho(s)h_s(x_a)\,ds}
{1+\int_0^t\rho(s)\,ds}.
\tag{3}
\]

Thus a key is an activity-weighted historical address. The value accumulates error-driven writes, and the scalar <k_a,h(x)>_n determines how strongly that write reaches a query. This scalar need not be positive and is not a probability. Changing A changes current query addresses; changing k changes where previously accumulated values act. Consequently feature movement changes the action of old learning, not only the next update.

The zeroth moment is not a velocity or an acceleration. Its meaning is the average (3). No higher order is needed for the mechanisms established here.

## 2. A precise bootstrap of feature learning

Define the initial label signal and its strength by

\[
b_0=\operatorname{mean}_a y_ag_0(x_a),\qquad
\mathcal F(A,B)=\frac1n\left\|
\operatorname{mean}_a y_a\tanh(B\tanh(Ax_a/\sqrt d))\right\|^2.
\]

The quantity F is the squared correlation of the second hidden population with the labels, with normalization across neurons. Initially w'=2b0, while A'=v'=k'=0. Let D_a=diag(1-g_0(x_a)^2). Differentiating (2) at zero yields

\[
v_a(t)=2t^2y_aD_ab_0+O(t^3),\qquad k_a(t)=k_a(0)+O(t^3),
\tag{4}
\]

and the exact acceleration identities

\[
\ddot A(0)=2n\nabla_A\mathcal F(A_0,W_0),\qquad
\ddot B(0)=2\nabla_B\mathcal F(A_0,W_0).
\tag{5}
\]

Therefore

\[
\mathcal F(A(t),B(t))=\mathcal F(A_0,W_0)
+t^2\left(n\|\nabla_A\mathcal F\|_F^2+
\|\nabla_B\mathcal F\|_F^2\right)+O(t^3).
\tag{6}
\]

All gradients on the right are evaluated at initialization. To verify (5), put s_h=1-h_0^2 and s_g=1-g_0^2. Differentiation gives

\[
\ddot A(0)=4\operatorname{mean}_a y_a
[s_{h,a}\odot W_0^T(b_0\odot s_{g,a})]x_a^T/\sqrt d,
\]
\[
\ddot B(0)=4\operatorname{mean}_a y_a(b_0\odot s_{g,a})h_{0a}^T/n.
\]

Differentiating F gives exactly these expressions divided by 2n and 2, respectively. Since the initial representation velocities are zero, the chain rule gives (6).

This is a supervised positive-feedback mechanism: the readout detects a weak label correlation and the first feature motion increases that same correlation, strictly at this order if either gradient is nonzero. It is not an all-time monotonicity theorem. Representations first move at order t^2; their effect on the output starts at order t^3 because w is of order t.

Equation (4) supplies another exact local result. If b0 is nonzero, then for every pair a,c and sufficiently small positive t,

\[
y_ay_c\,v_a(t)^Tv_c(t)>0.
\]

Indeed its leading coefficient is 4t^4 sum_i b0_i^2 D_a,ii D_c,ii, strictly positive because finite tanh derivatives are positive. Same-class writes initially cooperate; opposite-class writes initially oppose. This concerns values, not collapse of the keys or a guarantee of late-time alignment.

If b0=0, instead, w=v=0, A=A0, k=h0 and tau=1+t solve the entire system and uniqueness makes this its actual trajectory. This is an exact startup obstruction. For fixed finite data independent of initialization, the signed-geometry route proves that a nonsymmetric signed-input law avoids this exact cancellation almost surely; that qualitative statement supplies no lower bound on signal strength.

## 3. Progress, interference, and fitting

The readout has a particularly strong balance that survives arbitrary endogenous feature movement. For any fixed vector u, define f_u,a=u^Tg_a(t)/n and L_u=mean(f_u,a-y_a)^2. Then

\[
\frac d{dt}\frac{\|w-u\|^2}{2n}
=-\mathcal L+\mathcal L_u-operatorname{mean}_a(f_a-f_{u,a})^2.
\tag{7}
\]

Proof: substitute w' from (2) and use 2(f-y)(f-f_u)=(f-y)^2-(f_u-y)^2+(f-f_u)^2. There is no missing derivative of g: only ||w-u||^2 is differentiated. Integrating and discarding nonnegative terms gives

\[
\frac1T\int_0^T\mathcal L\le
\frac1T\int_0^T\mathcal L_u+\frac{\|u\|^2}{2nT}.
\tag{8}
\]

Thus if a fixed readout performs well across the actual feature trajectory, the evolving readout is competitive with it in time-average loss. The existence of such a comparator is a substantive representation condition, not automatic from instantaneous separability.

Setting u=0 gives the unconditional identity

\[
\frac{\|w(t)\|^2}{2n}+
\int_0^t[\mathcal L(s)+\operatorname{mean}_a f_a(s)^2]ds=t.
\tag{9}
\]

In particular ||w||/sqrt(n)<=sqrt(t), tau<=1+t, and ||V||_F/sqrt(mn)<=sqrt(2)t^(3/2). B and A stay bounded on every finite interval by (1)-(2); local Lipschitz continuity on tau>0 therefore implies unique global existence. This is not a bounded all-time state or fitting theorem.

The obstruction to a simple instantaneous descent law can also be isolated exactly. Put H=[h_a], K=[k_a], V=[v_a], Q=[r_ad_a], Delta=H-K, alpha=rho/tau, and

\[
J=QH^T/(mn),\qquad Z=(2Q+\alpha V)\Delta^T/(mn).
\]

Then

\[
\dot{\mathcal L}=-\|\dot A\|_F^2/n-\|\dot w\|^2/n
-4\|J\|_F^2+2\langle J,Z\rangle_F.
\tag{10}
\]

For verification, B'=-2J+Z and the forward-map derivative of L with respect to B is 2J. The A and w contributions are their displayed negative squares. The last term is the work caused by current features differing from remembered keys. It has no general algebraic sign. This identifies the obstacle; an arbitrary-state increasing-loss example is not evidence that initialized trajectories actually increase loss.

There is a useful explicit sufficient fitting condition. If on [0,T] the normalized readout is bounded by R_*, the smallest eigenvalue of G^TG/(mn) is at least lambda_*>0, and e=||H-K||_F/sqrt(mn), then

\[
\dot{\mathcal L}\le-4(\lambda_*-R_*^2e^2)\mathcal L.
\tag{11}
\]

The proof uses ||Z||_F<=4rho R_* e, completion of the square in (10), and the readout Gram bound. A strict positive gap in (11) yields exponential fitting. These conditions are not proved for arbitrary multiple inputs. The particular full-rank condition cannot hold if m>n; it is sufficient, not necessary.

Data compatibility matters independently. Oddness gives f(-x)=-f(x) at every time, so same-label antipodal inputs cannot both fit. Replacing each labeled input by y_a x_a with label +1 leaves the entire flow invariant after k_a,v_a are multiplied by y_a. This makes the architectural conflict transparent. It does not supply labels for unseen queries.

## 4. How training selects the function outside the data

Integrating the readout equation yields the exact whole-input formula

\[
f_t(x)=2\int_0^t\operatorname{mean}_a
[y_a-f_s(x_a)]\,\langle g_s(x_a),g_t(x)\rangle_n\,ds.
\tag{12}
\]

The past training feature is paired with the present test feature. The final feature map and the historical route through feature space both matter.

There is a sharper geometric statement. Let G_t=[g_t(x_a)], let Pi_t project orthogonally onto its column span, and put w_perp=(I-Pi_t)w. On any constant-rank interval,

\[
\dot w_\perp=-\dot\Pi_t w.
\tag{13}
\]

Although every instantaneous readout update lies in the current training-feature span, rotation of that span can leave part of the accumulated readout outside it. This part is invisible on the current training examples but can affect test predictions. It is not dynamically decoupled from subsequent feature learning.

At a convergent interpolating endpoint define K_*=G_*^TG_*/n and kappa_*(x)=G_*^Tg_*(x)/n. Orthogonal decomposition gives

\[
f_*(x)=\underbrace{\kappa_*(x)^TK_*^\dagger y}_{
\text{minimum-norm readout using the final features}}
+\underbrace{g_*(x)^Tw_{\perp,*}/n}_{
\text{zero on the training set}}.
\tag{14}
\]

Indeed the parallel component is nG_*(G_*^TG_*)^dagger y, and every fitting readout differs from it by an element of ker G_*^T. Equation (14) is valid even when G_* is rank deficient. If integral rho is finite, all states converge and fit, and

\[
w_{\perp,*}=-2\int_0^\infty\operatorname{mean}_a
r_a(s)(I-\Pi_*)[g_a(s)-g_a(*)]ds.
\tag{15}
\]

This displays the source of the additional component: past errors paired with departures from final training-feature geometry.

The mechanism is realized by the actual q1 equations, not only by arbitrary prescribed feature paths. At full-column-rank initialization, with b(t)=mean y_ag_t(x_a),

\[
(I-\Pi_t)w_t=-\frac23t^3(I-\Pi_0)b''(0)+O(t^4).
\tag{16}
\]

A checked two-neuron, one-input circle example has a nonzero coefficient and a nonzero additional prediction at an unseen input; continuity makes this true on an open set of initializations of positive Gaussian probability. The complete expansion and witness are in ROTATING_FEATURE_SPAN.md. That calculation proves generation during training only. The new argument in Section 6 proves persistence at a fitted endpoint for a separate finite-parameter witness and an open neighborhood; it does not infer persistence from the transient expansion.

Another exact invariant is A_t P_(span X)^perp=A_0 P_(span X)^perp. Training changes only the input directions it sees. On the circle this is a restriction for points on a single diameter, but ceases to be a nontrivial input-space restriction once the inputs span R^2.

## 5. A fully solved case of useful feature learning

Take n=m=1, x_*=sqrt(2)(1,0), y in {-1,1}, and A0=(a0,beta), with a0 W0 nonzero. Write A(t)=(a(t),beta). Direct sign-cone analysis of (2) proves finite endpoints, strict increase of |a(t)| for t>0, and

\[
\mathcal L(t)\le\exp[-4\tanh^2(|W_0\tanh a_0|)t].
\tag{17}
\]

The whole-circle classification rule, for positive t, is exactly

\[
\operatorname{sign}f_t(\theta)=y\operatorname{sign}
\left(\cos\theta+\frac{\beta}{a(t)}\sin\theta\right).
\tag{18}
\]

For the explicitly specified test truth y_true(theta)=y sign(cos theta) and uniform angle, its exact test error is

\[
R_{\rm cls}(t)=\frac1\pi\arctan\frac{|\beta|}{|a(t)|}.
\tag{19}
\]

Two oriented semicircle classifiers with angular separation delta disagree on arcs of total length 2|delta|, which proves (19). The error strictly decreases if beta is nonzero, although it generally remains positive. If beta=0 it is identically zero. The initial predictor is zero, so the starting classification comparison means the right-hand limit as t decreases to zero.

This is an explicit useful-representation mechanism: strengthening the observed direction reduces the relative influence of the unchanged random unobserved direction. The test truth is an additional assumption, not information recoverable from a single label; another truth can reverse the improvement conclusion.

The scalar proof also gives a permanent positive difference between the magnitude of the fitted current feature and its key. Thus successful learning need not make the key catch up. Finite accumulated activity freezes a historical representation, including a nonzero share of initialization. The complete all-time proof is in SCALAR_CIRCLE_SELECTION.md.

## 6. A historical readout survives fitting and changes the boundary

The complete proof is [ENDPOINT_HISTORY_SELECTION.md](ENDPOINT_HISTORY_SELECTION.md); its check status and evidence are recorded in README.md. Take n=2, m=1, d=2, x_train=sqrt(2)e_1, y=1 and

\[
W_0=\begin{pmatrix}1&0\\0&10\end{pmatrix},\qquad
A_0=\begin{pmatrix}1/2&1\\1&0\end{pmatrix},
\qquad w_0=v_0=0,\ k_0=h_0,\ \tau_0=1.
\tag{20}
\]

These are finite parameters of the actual tanh closure. Its first layer, both memory populations and readout all keep their prescribed dynamics. The second neuron is strongly saturated but is not frozen.

The useful clock for this one-input proof is

\[
s(t)=2\int_0^t[1-f_u(x_{\rm train})]du,\qquad \tau=1+s/2.
\]

In this clock w'=g, v'=w odot(1-g^2), and k'=(h-k)/(2+s), with the full moving read-in equation retained. Positivity makes the training responses nondecreasing. If F(s)=w(s)^Tg(s)/2, then

\[
F'(s)\ge c_0:=\|g_0\|^2/2>0.
\]

Thus the feature path crosses F=1 at a finite s_*, while physical time approaches that crossing asymptotically. All states converge and the training loss obeys L(t)<=exp(-4c_0t). This supplies fitting rather than assuming it.

The endpoint readout is the history integral

\[
w_* =\int_0^{s_*}g(s)ds.
\tag{21}
\]

The first response grows substantially enough that its history integral differs from its endpoint value; the second changes too little to cancel the difference. A finite-interval estimate in the proof gives the strictly negative determinant

\[
D=w_{1,*}g_{2,*}-w_{2,*}g_{1,*}
<-\frac1{11664}+\frac4{10^6}<0.
\tag{22}
\]

Consequently w_* is not parallel to g_*: the perpendicular readout in (14) is nonzero after fitting. Its extra prediction at the fixed unseen input sqrt(2)e_2 is strictly negative. The actual fitted classifier also disagrees on an open circle arc with the minimum-norm interpolating readout using the same final features. The proof of this last assertion uses invertibility of the final A and B, so that a nonzero circle input cannot have zero feature vector, and the two nonparallel readouts cannot share a zero.

The fitted crossing is transverse, which makes its location and endpoint state continuous in the initialization. The strict conclusions persist on an open neighborhood, hence have positive probability under the stated Gaussian law. This is not a quantitative probability estimate or a typical-initialization theorem.

The interpretation is precise: the readout accumulates earlier response ratios, while the final training features reflect later reinforcement. Fitting leaves only finite accumulated activity, so infinite physical time need not erase the mismatch. Universal cancellation of this historical component, and universal minimum-norm readout selection with final features, are therefore false. No test truth was specified, so the different boundary is not claimed to be better.

A separately frozen prompt-only derivation, ENDPOINT_INDEPENDENT_ROUTE.md, obtains endpoint prediction persistence using a different positive two-neuron witness and finite perturbation bounds. It is retained as an alternative candidate and is not a dependency of (20)--(22); its author-check status is distinct from the primary theorem's internal check.

## 7. What has and has not been explained

The general finite-sample equations now supply: an exact initial reinforcement principle; an all-time readout comparison law; an explicit term controlling whether memory lag opposes loss decrease; and a geometric account of how the training path can affect unseen predictions beyond the final training outputs. The solved scalar case shows that these interactions can yield fitting and improving test classification while preserving historical lag.

The remaining central question is whether initial supervised reinforcement develops into a sustained mechanism for general compatible multi-input tasks, and what determines the resulting boundary geometry. Endpoint persistence of the extra term in (14) is now proved possible on an open fitting class. Its typical size, possible cancellation classes, and behavior with multiple genuinely distinct training directions remain open. There is no all-time maximum-margin theorem, and universal final-feature minimum-norm readout selection is refuted by Section 6. These are questions about learning within q1; no higher-order or compression objective is required to state them.

## 8. Two samples directly in the infinite-width population closure

The complete new derivation is
[TWO_SAMPLE_POPULATION_ANALYSIS.md](TWO_SAMPLE_POPULATION_ANALYSIS.md),
with route scope and provenance in
[TWO_SAMPLE_POPULATION_CONTRACT.md](TWO_SAMPLE_POPULATION_CONTRACT.md).
It retains the current manuscript's q=1 normalized memories and canonical
fixed Gaussian source/true adjoint. Population random fields represent joint
laws; there is no independently learned fully connected matrix.

After replacing each normalized input by p_a=y_a x_a/sqrt(d), both targets
are +1. Put c=p_1 dot p_2 in (-1,1). Full population exchange symmetry
synchronizes the two predictions f and gives feature time
s=2 integral(1-f)dt before fitting. For each hidden response H or G, its
common and difference fields are the half-sum and half-difference over the
two signed examples. The four associated squared norms have zero initial
velocity, strictly positive initial acceleration for both common norms,
and strictly negative initial acceleration for both difference norms.
Thus both hidden populations initially become more aligned with the shared
signed target. This is a strict local theorem for every nondegenerate c,
not a pointwise contraction of all neurons or a sustained monotonicity claim.

The key proof is the first reuse of the random mixer. Its reverse answer
contains a conditional mean response and a correlated Gaussian innovation.
The mean response has positive eigenvalue on the common channel and negative
eigenvalue on the difference channel. For the full second-layer contraction,
one must also retain the innovations: the reverse sources for common and
difference energies have strictly negative covariance in both parity channels.
Together with their opposing conditional drifts, this makes the read-in
contribution to difference-energy acceleration negative. The q=1 memory
contribution is negative separately. Deleting the fixed-source response, or
making later calls independently Gaussian, would give a different system.

Both memory channels activate at order s² even though the training residual
is one scalar. Their reconstructed population correction has rank exactly
two near zero. The output obeys f(s)=kappa s+S_2''(0)s³/3+o(s³), where
kappa>0 is the initial common second-layer energy and S_2''(0)>0 its
acceleration. This connects feature learning to increased training progress
per accumulated residual.

The same calculation identifies an actual initialized-flow obstruction to
an all-time proof. Current first-layer difference energy decreases, while
its historical key retains the earlier difference. Consequently the
difference-key-lag contribution to f' is strictly negative at order s⁵;
its cumulative contribution is negative at order s⁶. Positive terms dominate
at startup, so this is not increasing loss. A valid sustained fitting proof
must compensate this term, not assume all memory work nonnegative.

The full predictor has an all-defined-times symmetry: it is odd along the
signed-sum direction, even along the signed-difference direction, and radial
in directions perpendicular to their span. It therefore vanishes on
(y_1x_1+y_2x_2) dot x=0. This zero set persists in any pointwise endpoint
limit. On the circle, with angle measured from the signed sum, a C1 endpoint
has F_*(theta)=cos(theta)Q_*(cos²(theta)); fitting fixes Q_*((1+c)/2)
=sqrt(2/(1+c)). The dynamics have not yet determined the full Q_* or excluded
additional zeros. Initial predictor velocity has exactly the signed-sum sign,
but propagation of that sign to the endpoint remains open.

All trajectory statements require the explicitly stated local strong unique
equivariant Gaussian population flow. The manuscript labels its fixed-order
population limit a conjecture; neither this note nor the finite-width results
prove the missing population construction. Global fitting, a regular fitted
endpoint, and its full unseen-input function remain unresolved. The new
theorem explains both-population feature learning and a concrete obstruction
to its continuation; it does not claim to solve those endpoint questions.

## 9. Four points: the label product strengthens its unsupervised constituents

The main new proof is
[STRUCTURED_POPULATION_ANALYSIS.md](STRUCTURED_POPULATION_ANALYSIS.md).
Choose normalized inputs

\[
u_{\sigma\tau}=(\sqrt{1-2\varepsilon^2},\varepsilon\sigma,
\varepsilon\tau),\qquad y_{\sigma\tau}=\sigma\tau,
\qquad\sigma,\tau\in\{-1,1\},
\]

with small but fixed positive epsilon and equal sample weights. Only the
product is supervised: neither primitive bit correlates with the labels.
The common coordinate makes the task compatible with the odd architecture;
ordinary centered planar XOR would have contradictory antipodes. An arbitrary
orthogonal input rotation changes none of the conclusions. This is an exact
nonlinear population q=1 task with the canonical fixed source, not a learned
dense middle layer, a new activation limit, or a finite-neuron simulation.

For either hidden layer, decompose its four responses into context, sigma,
tau and sigma*tau patterns, using their normalized four-point signed means.
The symmetries make these four population fields orthogonal at every time.
If a pattern has squared population norm E, the least squared norm of a
linear population readout exactly decoding that pattern is 1/E. Thus an
increase in E has a precise meaning: the latent variable becomes easier to
read out from the representation.

The new conditional theorem proves that **both primitive bits become easier
to decode in both hidden layers**, while the common context weakens, on a
positive initial interval for every sufficiently small fixed epsilon.
In feature time s=2 integral(1-f)dt, all initial energy velocities vanish.
The factor-energy accelerations have leading coefficients approximately
0.192447 epsilon^6 and 0.201780 epsilon^6 in layers one and two; context
coefficients are -0.047955 epsilon^4 and -0.055941 epsilon^4. The first-layer
label interaction also strengthens, and its ratio to the primitive-factor
energy increases while the factor/context ratio increases. Explicit interval
arithmetic, analytic integration-error bounds and Gaussian tails certify every
needed scalar sign. No ordinary quadrature estimate substitutes for a proof.
Controlled epsilon remainders and trajectory regularity turn these signs
into actual local changes. No explicit epsilon threshold or uniform time
interval is proved.

The mechanism can be seen before the long coefficient calculation. If
v_sigma,v_tau,v_y are the initial first-layer pattern energies, then the
second layer's label energy has the form

\[
J=T_1v_y+T_2v_\sigma v_\tau+O(\varepsilon^6),
\qquad T_1,T_2>0.
\]

The first term transmits an existing label interaction. The second creates
the product response from the two constituent responses. Its derivative
with respect to either factor energy is positive because the other is
present. The canonical reverse source converts this dependency into an
outward conditional drift along each latent readin direction. The full
feature calculation verifies that changing context and tanh saturation do
not cancel the gain. In the second layer the readin conditional drift,
the full true-transpose covariance and q=1 memory writes each increase the
factor energy; each decreases context. This effect cannot be obtained by
treating every pattern orthogonal to labels as nuisance or by omitting the
fixed-source response. Nor does it mean that every neuron becomes a pure
factor detector or that information was absent at initialization.

There is an exact all-time complement. For any first-layer neuron with
four logits x+sigma a+tau b, monotonicity of tanh gives

\[
|H_y|\le\min(|H_\sigma|,|H_\tau|).
\]

The two differences under a sigma flip have the same sign; their difference
forms the product coefficient and their sum forms the sigma coefficient.
This proves the inequality pointwise. Hence throughout every existing
population trajectory, a constituent is at least as accessible as its
product in the first layer. Moreover, at any bounded fitted endpoint,

\[
 E_{1,\mathrm{bit}}\ge
 \frac{1}{2\|W_*\|_2^2\|B_*\|^2}>0.
\]

This follows by applying tanh's Lipschitz bound to bit-flip differences,
then the operator norm and Cauchy--Schwarz. Both unsupervised factors must
therefore survive in a finite fitted representation. It is a necessary
endpoint property, not a proof of fitting or persistence of initial growth.

The entire predictor is odd in each of the three latent coordinates and
symmetric under exchange of the two factors. A C3 fitted endpoint, if it
exists, has

\[
F_*(u)=u_0u_1u_2\Psi_*(u_0^2,u_1^2,u_2^2),\qquad
\Psi_*(1-2\varepsilon^2,\varepsilon^2,\varepsilon^2)
=\frac1{\sqrt{1-2\varepsilon^2}\,\varepsilon^2}.
\]

Here u denotes normalized query coordinates, with manuscript input x=sqrt(3)u.
Its three mandatory zero planes are determined; its amplitude away from the
four samples, possible extra zeros, and test performance are not. Global
fitting and endpoint existence remain open. As with Section 8, all trajectory
claims assume the regular unique equivariant canonical population flow;
the manuscript's population-limit conjecture is not resolved here.

The first/second route proofs and scalar certificates have separate complete
fresh checks, WEAK_FACTOR_FIRST_CHECK.md and WEAK_FACTOR_SECOND_CHECK.md.
The assembled proof has an additional candidate-only check, whose final
status is recorded in README.md. These are internal checks, not promotion
reviews. GLOBAL_MEMORY_ROUTE.md preserves a separate author-checked global
compensation attempt and its explicit remaining obstruction; it is not used
to claim global convergence for the four-point task.

## Evidence and checks

The two-sample population continuation adds the complete
TWO_SAMPLE_POPULATION_ANALYSIS.md and three scoped route files. Its
TWO_SAMPLE_STARTUP_CHECK.md checks the frozen mixing/symmetry sources;
TWO_SAMPLE_POPULATION_CHECK.md checks the complete assembled theorem,
manuscript dictionary and additional endpoint conditions. A source-regularity
wording issue was corrected and the bounded correction check passed. Both
reports retain their full evidence, assumptions, disclosures and hashes.
Root read both completely. README.md records the final internally checked
conditional version; this does not promote the findings or resolve global
population construction and fitting.

The three initial routes were developed from the explicit model before cross-route comparison: ENERGY_ROUTE.md, PREDICTOR_ROUTE.md, and SIGNED_GEOMETRY_ROUTE.md. Root added ROTATING_FEATURE_SPAN.md and SCALAR_CIRCLE_SELECTION.md. Bounded internal checks are recorded in ENERGY_CHECK.md, ROTATING_FEATURE_SPAN_CHECK.md, SIGNED_GEOMETRY_CHECK.md and SCALAR_CIRCLE_SELECTION_CHECK.md. A beta=0 wording exception in the scalar classification statement was corrected after checking. The current continuation adds MANUSCRIPT_RECONCILIATION.md and ENDPOINT_HISTORY_SELECTION.md, with the fresh candidate-only ENDPOINT_HISTORY_CHECK.md and separately frozen ENDPOINT_INDEPENDENT_ROUTE.md. The current README records their exact status. These checks are not independent promotion reviews.

The equations and deductions here do not depend on external learning theorems. For historical context only, outer-product associative memory and recurrent key/value state already appear in Katharopoulos et al., *Transformers are RNNs* (2020), equations (5), (10)-(12), and (18)-(20): https://proceedings.mlr.press/v119/katharopoulos20a/katharopoulos20a.pdf . The full main paper was retrieved and read; that precedent does not establish any of the q1 fitting or feature-motion identities above. No novelty priority is asserted here.
