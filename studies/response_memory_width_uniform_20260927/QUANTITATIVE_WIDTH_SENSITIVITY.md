# Quantitative width: sensitivity, initial bias, and the remaining response bias

Scoped ten-minute theoretical attempt, 28 September 2026. Inputs were
the complete ACTIVATION_NEAR_QUADRATIC_ALLTIME.md,
ACTIVATION_GAUSSIAN_ALLTIME.md, and paper/trial_tracking_proof.tex.
The rigorous-math skill and previously supplied notation contract remain
in force. No other source, study, experiment, agent, or manuscript edit
was used. Only this report was written.

**Outcome.** The existing assumptions imply the finite-width sensitivity
bound (5) and the root-\(n\) initial-Gram estimate (14) below. A finite
trained-carrier maximum bound of order \(\sqrt{\log n}\), if proved,
would give all-time predictor concentration at \(n^{-1/2+o(1)}\).
Concentration alone does not give the population-predictor bias rate.
The exact mean equations isolate a tangent-Gram bias source \(\beta_n\);
their covariance contribution would already be \(n^{-1+o(1)}\).
The required trained bound for \(\beta_n\), and the original dense-carrier
floor \(a_n\), remain unproved. This attempt therefore does **not**
establish the unconditional \(\epsilon^{-5/2+o(1)}\) moving-state theorem.
This is an obstruction to the proposed inference from concentration,
not a counterexample to the desired network theorem.

## 1. Exact sensitivity under the existing assumptions

Use the assigned fixed data, depth, zero readout, fixed small positive
labels, positive limiting initial feature Gram, and
\[
 |\phi_\ell(0)|\le a,\qquad \|\phi_\ell'\|_\infty\le s,\qquad
 \operatorname{Lip}(\phi_\ell')\le j,\qquad
 \phi_\ell\in C^{1,1}(\mathbb R).
 \tag{1}
\]
On the common good event, all-time fitting supplies bounded hidden
operators, forward RMS, backward RMS \(CY\), positive Gram, and
\(\rho(t)\le Ye^{-\kappa t}\), \(\int\rho\le CY\).

Let \(G=(G_1,\ldots,G_L)\) contain independent standard Gaussians. Then
\[
 W_1(0)=G_1,\quad W_\ell(0)=G_\ell/\sqrt n\ (\ell\ge2),\quad w(0)=0,
 \tag{2}
\]
so the sum of canonical parameter-block distances satisfies
\[
 d_n(\theta_0(G),\theta_0(G'))\le
                    \sqrt{L/n}\,\|G-G'\|_2.
 \tag{3}
\]
The first-block normalization is also \(1/\sqrt n\), despite its
unscaled Gaussian entries.

For one dense reference path set
\[
 k_{L,a}=w,\quad k_{\ell,a}=W_{\ell+1}^T\delta_{\ell+1,a},\quad
 K_n(t)=\max_{\ell,a}\|k_{\ell,a}(t)\|_\infty,\quad
 \Lambda_n=\int_0^\infty\rho(t)[1+jK_n(t)]\,dt.
 \tag{4}
\]
For any two good dense initializations,
\[
 \sup_{t\ge0}d_n(\theta(t;G),\theta(t;G'))
 \le C e^{C\Lambda_n(G')}
                     d_n(\theta_0(G),\theta_0(G')).
 \tag{5}
\]
Here and below constants are independent of width. To prove (5), write
\(d(t)\) for parameter distance, \(v(t)\) for prediction discrepancy in
sample RMS, and \(Q(t)=\int_0^t v\). Forward differences cost \(Cd\).
The only unbounded-coordinate product in backward subtraction is
\([\phi_\ell'(z)-\phi_\ell'(z')]\odot k'_{\ell,a}\); its RMS is at most
\(CjK_n(t;G')d\). All other terms use bounded operators/slopes and RMS.
Induction through fixed depth and expansion of the tangent Gram give
\[
 \max_{\ell,a}\frac{\|\delta_{\ell,a}-\delta'_{\ell,a}\|_2}{\sqrt n}
       +\|\Gamma-\Gamma'\|_{\rm op}
       \le C[1+jK_n(t;G')]d(t).
 \tag{6}
\]
Both initial predictions vanish. The exact equation
\(\dot u=-2\Gamma u-2(\Gamma-\Gamma')r'\), with the positive Gram gap,
implies \(Q(t)\le C\int_0^t\rho'(1+jK_n)d\).
Subtracting parameter equations gives
\(d(t)\le d(0)+CQ(t)+C\int_0^t\rho'(1+jK_n)d\).
An integral integrating factor proves (5). Norm derivatives at zero
follow by regularization. This proof has no growing physical-time factor.

Whole-input forward/readout subtraction then gives
\[
 \sup_t|f(t,x;G)-f(t,x;G')|
 \le \frac{C(1+\|x\|/\sqrt d)e^{C\Lambda_n(G')}}{\sqrt n}
                                                \|G-G'\|_2.
 \tag{7}
\]
The directly available deterministic bound is only
\[
 K_n(t)\le C\sqrt nY,\qquad \Lambda_n\le CY+Cj\sqrt nY^2.
 \tag{8}
\]
For fixed positive labels this does not yield a useful width rate.
The assigned population marginal tails and qualitative finite-array
transfer do not already prove \(\Lambda_n=O_{\Pr}(\sqrt{\log n})\).

## 2. What a quantitative carrier bound would give

Suppose separately that measurable events \(\mathcal E_n\), contained in
the good initialization events, obey
\[
 p_n:=\Pr(\mathcal E_n)\to1,\qquad
 \sup_{G\in\mathcal E_n}\Lambda_n(G)\le B_n=O(\sqrt{\log n}).
 \tag{9}
\]
Equation (7) is a pairwise Lipschitz bound on this set. A scalar predictor
therefore admits an extension to the full Gaussian space with constant
\(L_{n,x}=C(1+\|x\|/\sqrt d)e^{CB_n}/\sqrt n\).
For example take the infimum over \(H\in\mathcal E_n\) of
\(f(t,x;H)+L_{n,x}\|G-H\|\). No segment joining initializations need
stay in the event.

The precise Gaussian inequalities used are
\[
 \operatorname{Var}F\le L^2,\qquad
 \Pr(|F-\mathbb EF|>u)\le2e^{-u^2/(2L^2)}
 \tag{10}
\]
for \(L\)-Lipschitz \(F\). A short derivation avoids any neuron-independence
claim. For the Gaussian Ornstein--Uhlenbeck semigroup \(P_s\), integration
by parts and \(\nabla P_s=e^{-s}P_s\nabla\) give
\(\operatorname{Var}F=2\int_0^\infty\mathbb E|\nabla P_sF|^2ds
\le\mathbb E|\nabla F|^2\).
For positive \(h\) the entropy identity and Cauchy--Schwarz give
\[
 \operatorname{Ent}(h)
 =\int_0^\infty\mathbb E\frac{|\nabla P_sh|^2}{P_sh}ds
 \le\frac12\mathbb E\frac{|\nabla h|^2}{h}.
\]
Apply this to \(h=e^{\lambda F}\). Integrating
\(\lambda\psi'-\psi\le\lambda^2L^2/2\), where
\(\psi=\log\mathbb Ee^{\lambda F}\), and exponential Markov prove
(10). Smooth truncations justify the formulas for Lipschitz extensions.

Ordinary Gaussian Poincare must not be applied directly to a conditioned
Gaussian law. Instead, for any such extension,
\[
 |\mathbb E[F\mid\mathcal E_n]-\mathbb EF|
 \le L\sqrt{(1-p_n)/p_n},\qquad
 \operatorname{Var}(F\mid\mathcal E_n)\le L^2/p_n.
 \tag{11}
\]
The first bound follows by writing its numerator as
\(\operatorname{Cov}(F,\mathbf1_{\mathcal E_n})\); the second follows
by centering first at the unconditional mean. Thus concentration holds
around \(\mu_n(t,x)=\mathbb E[f_n(t,x)\mid\mathcal E_n]\).

The time change \(u=e^{-\kappa t}\in[0,1]\) and the supplied speed bound
make predictors uniformly Lipschitz in \(u\); their spatial Lipschitz
constant is uniform on a bounded input domain. A mesh of spacing
\(n^{-1/2}\) in \(u\) and a fixed-dimensional bounded input domain has
polynomially many points. Apply (10)--(11), a union bound with threshold
\(CL_{n,x}\sqrt{\log n}\), and the interpolation modulus to obtain
\[
 \sup_{t\ge0,x\in K}|f_n(t,x)-\mu_n(t,x)|
 =O_{\Pr}(n^{-1/2}e^{CB_n}\sqrt{\log n})
 =n^{-1/2+o_{\Pr}(1)}.
 \tag{12}
\]
The exceptional probability includes \(1-p_n\).
For a test law with finite second moment, use only the time mesh at each
\(x\), integrate its squared-maximum expectation with the bound
\(C(1+\|x\|/\sqrt d)^2\), and apply Markov. This gives the same
near-root-\(n\) concentration scale for the norm with time supremum
inside the test integral; no quantitative input-tail truncation is needed.

These conclusions concern the finite-width mean. They do not bound its
bias to the population. The elementary variables
\[
 F_n=f_\infty+1/\log(e+n)+G_1/\sqrt n
 \tag{13}
\]
have the desired Gaussian sensitivity and variance, and converge to
\(f_\infty\), but have much slower bias. This is a counterexample only
to that logical inference, not to the neural-network theorem.

## 3. A root-\(n\) initialization bias lemma under exactly \(C^{1,1}\)

For a fixed finite list of training and passive test inputs, let
\(Q_{\ell,n}\) be the initial feature Gram with normalization \(1/n\).
Set \(Q_{0,n}=Q_0\) and
\(\Psi_\ell(Q)_{ab}=\mathbb E[\phi_\ell(Z_a)\phi_\ell(Z_b)]\) for
\(Z\sim N(0,Q)\), with
\(Q_{\ell,\infty}=\Psi_\ell(Q_{\ell-1,\infty})\).
For each fixed \(p\ge1\),
\[
 \|Q_{\ell,n}-Q_{\ell,\infty}\|_{L^p}\le C_{p,\ell}n^{-1/2}.
 \tag{14}
\]
Here any fixed-sample matrix norm is admissible.

Gaussian covariance interpolation first gives
\[
 \|\Psi_\ell(Q)-\Psi_\ell(Q')\|
 \le C(1+\sqrt{\operatorname{tr}Q}+\sqrt{\operatorname{tr}Q'})
                                                    \|Q-Q'\|.
 \tag{15}
\]
Indeed, along \(Q_\theta=(1-\theta)Q+\theta Q'\),
\[
 \frac d{d\theta}\mathbb EF(Z_\theta)
  =\tfrac12\sum_{ij}(Q'-Q)_{ij}
                                \mathbb E\,\partial_{ij}F(Z_\theta).
 \tag{16}
\]
For positive definite covariances this follows by differentiating the
density and integrating by parts twice. For
\(F(z)=\phi_\ell(z_a)\phi_\ell(z_b)\), its weak second derivatives
involve only \(\phi_\ell'\phi_\ell'\) and
\(\phi_\ell''\phi_\ell\). Their expected magnitudes are bounded by the
factor in (15), since the weak second derivative is bounded by \(j\)
and activations have linear growth. Mollify the activation, add
\(\eta I\) to both covariances, apply (16), and pass to the limits
using these common Gaussian moment bounds. Thus (15) allows singular
input covariances and needs no third activation derivative.

At initialization, conditional on preceding-layer features, new Gaussian
rows are independent with covariance \(Q_{\ell-1,n}\). Hence
\[
 Q_{\ell,n}=\Psi_\ell(Q_{\ell-1,n})+\xi_{\ell,n},\qquad
 \mathbb E[\xi_{\ell,n}\mid Q_{\ell-1,n}]=0,\qquad
 \|\xi_{\ell,n}\|_{L^p}
 \le C_p n^{-1/2}\|1+\operatorname{tr}Q_{\ell-1,n}\|_{L^p}.
 \tag{17}
\]
To verify the moment rate, expand an even \(2k\)-th moment of a centered
empirical entry. Terms with an index occurring only once vanish. At most
\(k\) distinct indices remain, leaving \(O_k(n^k)\) terms. Conditional
Gaussian moments and linear growth bound each term by
\(C_k(1+\operatorname{tr}Q_{\ell-1,n})^{2k}\). Divide by \(n^{2k}\).
Higher even moments and Holder give every fixed \(p\).

Jensen, linear growth, and fixed-depth induction bound all moments of
\(Q_{\ell,n}\) uniformly in width. Equations (15)--(17) and Holder imply
\[
 \|Q_{\ell,n}-Q_{\ell,\infty}\|_{L^p}
 \le C_p n^{-1/2}
       +C_p\|Q_{\ell-1,n}-Q_{\ell-1,\infty}\|_{L^{2p}}.
 \tag{18}
\]
Induction asserting all fixed \(p\) at each layer proves (14).
In particular the initial Gram bias is \(O(n^{-1/2})\).
Zero readout makes all backward responses vanish initially, so
\[
 \dot f_n(0)=2\Gamma_{w,n}(0)y,\qquad
 \|\dot f_n(0)-\dot f_\infty(0)\|_{L^p}\le C_pY n^{-1/2}.
 \tag{19}
\]
The same argument applies to a fixed test query's cross feature Gram.
No independence after initialization has been used.

## 4. An exact all-time trained-bias source lemma

Condition on a fixed good initialization event \(\mathcal E_n\) with
probability at least \(1/2\); all conditional expectations below use that
one event. Let \(\Gamma_n\) be the training tangent Gram, and \(K_n^x\)
the training-to-test row normalized by
\[
 \dot r_n=-2\Gamma_n r_n,\qquad \dot f_n(t,x)=-2K_n^x r_n.
 \tag{20}
\]
Suppose the mean tangent-Gram errors satisfy
\[
 \sup_t\|\mathbb E_{\mathcal E}\Gamma_n-\Gamma_\infty\|
 +\sup_t\|\mathbb E_{\mathcal E}K_n^x-K_\infty^x\|\le\beta_n,
 \tag{21}
\]
and the RMS fluctuations of \(\Gamma_n,K_n^x,r_n\) around their
conditional means are bounded by \(l_n\), uniformly in time.
Then, for \(0<l_n\le1\),
\[
 \sup_t|\mathbb E_{\mathcal E}f_n(t,x)-f_\infty(t,x)|
 \le C_x[\beta_n+l_n^2\log(e/l_n)].
 \tag{22}
\]
This is a conditional implication with the unproved source (21) displayed,
not an assumption smuggled into the original theorem.

Write \(\bar r_n=\mathbb E_{\mathcal E}r_n\),
\(\bar\Gamma_n=\mathbb E_{\mathcal E}\Gamma_n\), and
\(C_n=\mathbb E_{\mathcal E}[(\Gamma_n-\bar\Gamma_n)(r_n-\bar r_n)]\).
Cauchy--Schwarz and the deterministic residual envelope give
\[
 \|C_n(t)\|\le C l_n\min(l_n,Ye^{-\kappa t}),\qquad
 \int_0^\infty\|C_n(t)\|dt\le C l_n^2\log(e/l_n).
 \tag{23}
\]
Split at \(\kappa^{-1}\log_+(Y/l_n)\) to obtain the integral bound.
The identical estimate applies to the cross-Gram covariance \(C_n^x\).
For \(b=\bar r_n-r_\infty\), the exact mean equation is
\[
 \dot b=-2\Gamma_\infty b
       -2(\bar\Gamma_n-\Gamma_\infty)\bar r_n-2C_n,\quad b(0)=0.
 \tag{24}
\]
Population Gram damping, (21), finite activity, and (23) yield
\(\int_0^\infty\|b\|\le C[\beta_n+l_n^2\log(e/l_n)]\).
The test mean difference obeys
\[
 \dot b_x=-2K_\infty^x b
 -2(\mathbb E_{\mathcal E}K_n^x-K_\infty^x)\bar r_n-2C_n^x,\quad
 b_x(0)=0.
 \tag{25}
\]
Integrating, using bounded cross-Gram and the preceding estimates, proves
(22). Finite-horizon differentiation under conditional expectation follows
from the common velocity bounds; infinite-horizon passage uses the
integrable majorants just displayed.

If a separate finite-carrier theorem supplied a uniform-in-time
\(M_n=O(\sqrt{\log n})\), including carriers of the finitely many passive
queries, equations (5)--(7), the Gram subtraction (6), and Lipschitz
extension/Poincare would give
\[
 l_n\le C(1+M_n)e^{CM_n}/\sqrt n=n^{-1/2+o(1)}.
 \tag{26}
\]
Thus the covariance source in (22) would be \(n^{-1+o(1)}\).
The leading missing input would be the trained mean bias \(\beta_n\).
Equation (14) controls it at time zero, not throughout training.

## 5. Stein identifies an order-one response, not a negligible error

For a reused hidden matrix \(W=G/\sqrt n\), Gaussian integration by
parts gives the exact identity
\[
 \mathbb E\frac{U^TWV}{n}
   =\frac1{n^2}\sum_{ij}
             \mathbb E\,\partial_{W_{ij}}(U_iV_j).
 \tag{27}
\]
It applies when the fields and weak derivatives are integrable; smooth
truncation proves the usual extension from smooth fields. These derivative
terms cannot be discarded as small fluctuations. With deterministic \(u\),
\(U=u\), \(V=W^Tu\), the right side is
\(n^{-2}\sum_{ij}u_i^2=\|u\|^2/n\), so
\[
 \mathbb E[u^TWW^Tu/n]=\|u\|^2/n.
 \tag{28}
\]
For RMS-order-one \(u\) the mean is order one. Treating \(V\) as
independent of the reused matrix would incorrectly give zero, regardless
of how well the scalar contraction concentrates.

The population construction retains such terms in its response
coefficients. Its named-source derivatives freeze deterministic
population covariances and scalar feedback coefficients. They are not
automatically the derivatives of the actual finite random feedback with
respect to all initialization coordinates. To prove (21), a quantitative
Stein/cavity argument must compare those finite response contractions with
the population coefficients. Predictor concentration alone does not do so.

There is a specific regularity obstruction to differentiating every
response coefficient again for Poincare. The first tangent-flow equation
contains bounded weak \(\phi''\), but a further derivative may need a
derivative of \(\phi''\), absent from the hypotheses. For example
\(\phi'(x)=\min(|x|,1)\) is bounded and globally Lipschitz, whereas
\(\phi''(x)=\operatorname{sign}(x)\) for \(0<|x|<1\) has distributional
jumps. Its derivative is not an ordinary Gaussian \(L^2\) function.
An \(L^2\)-gradient Poincare estimate for such a response observable
cannot simply be assumed. The initialization lemma avoids this via
covariance interpolation using only two weak derivatives.

This example does not prove slow network bias. Gaussian smoothing or
a cavity argument could bypass the extra derivative, but the positive
training feature Gram is not a lower bound on every growing
history-innovation covariance. No extra history nondegeneracy assumption
is introduced here.

## 6. Status of the moving-state exponent

The moving-state count is \(O(nq)\). If the required actual finite-width
predictor and closure certificates were \(n^{-1/2+o(1)}\), then
\(n=\epsilon^{-2+o(1)}\), \(q=\epsilon^{-1/2+o(1)}\) would indeed give
\(\epsilon^{-5/2+o(1)}\).

This attempt establishes sensitivity (5), a conditional concentration
consequence with its all-time/event details, unconditional root-\(n\)
initialization bias (14), and the exact trained-bias reduction (22).
It leaves a quantitative finite-carrier/response estimate and the trained
mean source (21) unresolved. If the original bound
\(D_n(q)\le C\Phi(q^{-2}+a_n)\) is used unchanged, its dense tail floor
\(a_n\) also requires a quantitative certificate. None is replaced here
by trained-neuron independence, a presumed central limit theorem, or
qualitative convergence.

The coordinator also proposed a small-label Picard expansion whose
successive *increments* might have geometric factors \( (CY^2)^k \),
with width-error constants growing only exponentially in \(k\).
Such a summable increment estimate would be useful, but neither factor
has been proved here for the reused Gaussian response law. The available
carrier-cutoff comparison has a Lipschitz coefficient growing with its
cutoff; choosing a cutoff of order \(\sqrt{\log n}\) does not give a
width-independent Banach contraction at fixed \(Y>0\). A Volterra
iteration could instead exploit factorial time ordering, but it would
still require quantitative finite-program errors with controlled
dependence on iteration count and potentially degenerate history Gram
matrices. The trained feature-Gram gap does not supply that control.
No Picard contraction, summable width-error series, or geometric
increment estimate is claimed.
