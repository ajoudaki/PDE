# Smooth clipping: all-initialization bounds and the unresolved all-time moment

2026-10-01. Fresh scoped theoretical route. The exact smooth-clipped system has global finite-time solutions for every finite initialization. The initialized fitting theorem and finite-horizon exceptional-event bounds transfer to it. A new quantitative bound records the error from incorrectly clipping the true output derivative, and an exact scalar special case has bounded all-time predictors for every initialization. None of these results proves the required all-initialization, all-time second moment at general width. No admissible counterexample to that target was established.

The complete scientific inputs were `SMOOTH_SETUP.md`, `FITTING_AND_THRESHOLD.md`, `UNCONDITIONAL_TAIL_ROUTE.md`, `FULL_ERROR_CHECKPOINT.md`, and `CLIPPED_POPULATION_ROUTE.md` in this study. Required research, rigorous-proof, and canonical-notation instructions, including the neural-network reference, were read. No other study, smooth sibling report, prior review verdict, experiment, manuscript edit, or Git operation was used.

## 1. Exact system and target

There are \(m\) fixed training examples \(x_a\in\mathbb R^d\), labels \(y_a\), width \(n\), and a fixed cap \(M>0\). Put \(u_a=x_a/\sqrt d\), \(X=\max_a\|u_a\|_2\), and \(Y^2=m^{-1}\sum_a y_a^2\). The state consists of \(A\in\mathbb R^{n\times d}\), \(w,v_a,k_a\in\mathbb R^n\), and \(\tau\ge1\). For any input \(x\), define

\[
 h(x)=\tanh(Ax/\sqrt d),\quad
 B=W_0+\frac1{mn}\sum_a v_a k_a^\top,\quad
 z(x)=Bh(x),\quad g(x)=\tanh z(x),\quad
 f_n(t,x)=\frac1n w^\top g(x).
\]

Training-input subscripts mean evaluation at \(x_a\). With \(r_a=f_n(t,x_a)-y_a\), \(\rho^2=m^{-1}\sum_a r_a^2\), and coordinatewise \(c_M(s)=M\tanh(s/M)\), the exact backward fields and updates are

\[
\begin{aligned}
 d_a&=c_M(w\odot\operatorname{sech}^2z_a),\\
 \ell_a&=c_M\bigl(\operatorname{sech}^2(Au_a)\odot B^\top d_a\bigr),\\
 \dot w&=-\frac2m\sum_a r_a g_a,
 &\dot A&=-\frac2m\sum_a r_a\ell_a u_a^\top,\\
 \dot v_a&=-2r_a d_a,
 &\dot k_a&=\frac\rho\tau(h_a-k_a),
 &\dot\tau&=\rho.
\end{aligned}                                                    \tag{1}
\]

Initially \(A_0\) has iid standard Gaussian entries, \(W_0\) has iid \(N(0,1/n)\) entries independently, \(w=v_a=0\), \(k_a=h_a(0)\), and \(\tau=1\). The same matrix and actual transpose are reused. The target is the predictor \(f_{\infty,M}\) of this smooth system's own deterministic population, including its fitted endpoint. For a fixed bounded query law \(\mu\), the desired inequality is

\[
 \mathbb E\int\sup_{t\ge0}|f_n(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)
 \le C/n.                                                        \tag{2}
\]

Labels are fixed and sufficiently small, and the initial population readout Gram has a positive gap. Neither \(Y\) nor \(M\) is sent to zero with width.

## 2. Smooth fitting transfers without top inactivity

Two properties used in the supplied fitting proof hold exactly:

\[
 |c_M(s)|\le\min\{|s|,M\},\qquad |c_M'(s)|\le1.                  \tag{3}
\]

The useful gate-composed map is globally Lipschitz as well. For
\(\Psi_M(z,p)=c_M(p\operatorname{sech}^2z)\), differentiation gives

\[
 |\partial_p\Psi_M|\le1,\qquad
 |\partial_z\Psi_M|
 \le2M|q|\operatorname{sech}^2q\le2M,
 \quad q=p\operatorname{sech}^2z/M.
\]

For the last inequality, \(\cosh^2q\ge1+q^2\ge|q|\). Integrating along the two coordinate directions proves

\[
 |\Psi_M(z,p)-\Psi_M(\widetilde z,\widetilde p)|
 \le2M|z-\widetilde z|+|p-\widetilde p|.                          \tag{4}
\]

Here is a complete transfer of the fitting estimate. Suppose

\[
 \|W_0\|_{\rm op}\le K,
 \qquad \Gamma_0:=\frac{G_0^\top G_0}{mn}\succeq\lambda I_m,
 \qquad G_0=[g_a(0)]_{a=1}^m.
\]

Set

\[
 D=K+2,\quad C_h=8+4X^2D^2,\quad
 s_* =\min\{1,\sqrt{\lambda/(4C_h)}\},\qquad
 S(t)=\int_0^t\rho(s)\,ds.
\]

Assume \(Y\le\lambda s_*/2\), and provisionally stop at \(S=s_*\). The exact key formula is

\[
 k_a(t)=\frac{h_a(0)+\int_0^t\rho(s)h_a(s)\,ds}{1+S(t)}.
\]

It gives \(\|k_a\|_\infty\le1\). Equation (1), sample Cauchy–Schwarz, and (3) then give

\[
 \|w\|_\infty\le2S,\qquad \|d_a\|_\infty\le2S,
 \qquad \frac1m\sum_a\|v_a\|_\infty\le2S^2.
\]

The last inequality follows by integrating
\(m^{-1}\sum_a\|\dot v_a\|_\infty\le4S\rho\).
Consequently

\[
 \|B-W_0\|_F\le2S^2,\quad \|B\|_{\rm op}\le D,\quad
 \frac{\|\ell_a\|_2}{\sqrt n}\le2DS,\quad
 \frac{\|\dot A\|_F}{\sqrt n}\le4XD S\rho.
\]

Use \(\|\dot k_a\|_2/\sqrt n\le2\rho/\tau\), differentiate the reconstruction of \(B\), and bound each outer product by the product of its normalized vector norms. This gives

\[
 \|\dot B\|_F\le4S\rho+4S^2\rho/\tau\le8S\rho,
 \qquad
 \max_a\frac{\|\dot z_a\|_2}{\sqrt n}
 \le C_h S\rho.
\]

Since tanh is 1-Lipschitz, the same bound holds for \(\dot g_a\). With \(G=[g_a]\) and \(\Gamma=G^\top G/(mn)\), integration and subtraction of the two Gram products give

\[
 \frac{\|G-G_0\|_F}{\sqrt{mn}}\le C_hS^2/2,
 \qquad \|\Gamma-\Gamma_0\|_{\rm op}\le C_hS^2.
\]

The true prediction derivative is

\[
 \dot r=-2\Gamma r+e,\qquad
 e_a=\frac1n w^\top\dot g_a,
 \qquad \|e\|_m\le2C_hS^2\rho,
 \quad \|b\|_m^2=m^{-1}\sum_a b_a^2.
\]

It follows for positive \(\rho\) that

\[
 \dot\rho\le(-2\lambda+4C_hS^2)\rho\le-\lambda\rho.
\]

At zero residual every state velocity vanishes. Hence the same comparison holds there by uniqueness. We obtain

\[
 \rho(t)\le Ye^{-\lambda t},\qquad
 S(t)\le Y/\lambda\le s_*/2,\qquad
 \sup_{t,x}|f_n(t,x)|\le2Y/\lambda.                              \tag{5}
\]

This strictly excludes the provisional stop. Local Lipschitz continuity on \(\tau>0\) and bounded state coordinates extend the solution globally. Every velocity is integrable, so the state converges and the endpoint fits. The proof never identifies the clipped backward field with an output derivative. It also applies on an already constructed smooth population Hilbert space with its bounded common action; that conditional statement does not independently construct or identify the population.

For \(s\ne0\), \(|c_M(s)|<|s|\). Thus there is no positive threshold at which the smooth top clip becomes exactly inactive. The hard-clipping threshold conclusion must be omitted.

## 3. Quantifying the top-derivative discrepancy

Let \(p_a=w\odot\operatorname{sech}^2z_a\), the true upper derivative factor. For \(u\ge0\),

\[
 u-\tanh u=\int_0^u\tanh^2v\,dv\le u^3/3.
\]

Oddness therefore gives, globally,

\[
 |p-c_M(p)|\le |p|^3/(3M^2).                                    \tag{6}
\]

On the fitting event, \(\|p_a-d_a\|_\infty\le8S^3/(3M^2)\). The actual hidden-motion term is \(e_a=n^{-1}p_a^\top\dot z_a\), so

\[
 \left|e_a-\frac1n d_a^\top\dot z_a\right|
 \le\frac{8C_h}{3M^2}S^4\rho,
\qquad
 \int_0^\infty\left|e_a-\frac1n d_a^\top\dot z_a\right|dt
 \le\frac{8C_hY^5}{15M^2\lambda^5}.                             \tag{7}
\]

The integral uses \(dS=\rho\,dt\) and (5). This is an error bound at the same actual smooth trajectory, not a comparison theorem between two flows. It is nonzero at fixed labels and cannot itself serve as a vanishing width error. In particular, a proof relying on a symmetric Gram after replacing \(p_a\) by \(d_a\) needs both justification of that Gram and the explicit correction (7).

## 4. What holds for every finite initialization

Define \(E_w=\|w\|_2^2/n\), and let \(f_{\rm tr}=(f_n(t,x_a))_a\). The unchanged readout equation gives the exact identity

\[
 \dot E_w=-4\langle r,f_{\rm tr}\rangle_m
 =Y^2-4\|f_{\rm tr}-y/2\|_m^2
 =-4\rho^2-4\langle y,r\rangle_m.                              \tag{8}
\]

It follows that, for finite \(T\ge0\),

\[
 E_w(t)\le Y^2t,
 \qquad \sup_{t\le T,x}|f_n(t,x)|^2\le Y^2T.                     \tag{9}
\]

Integrating the last expression in (8), using \(E_w(T)\ge0\), and then applying time Cauchy–Schwarz gives

\[
 \int_0^T\rho^2\,dt\le YS(T),\qquad
 S(T)^2\le T\int_0^T\rho^2\,dt\le YTS(T).
\]

Divide if \(S(T)>0\), and handle \(S(T)=0\) directly. Then

\[
 S(T)\le YT,\qquad\int_0^T\rho^2\,dt\le Y^2T.                  \tag{10}
\]

Bounded clips and the exact key formula imply

\[
 \tau\le1+Yt,\quad
 \frac1m\sum_a\|v_a\|_\infty\le2MYt,\quad
 \|B-W_0\|_{\rm op}\le2MYt,\quad
 \frac{\|A-A_0\|_F}{\sqrt n}\le2MXYt.
\]

Together with (9) these bounds keep every finite-dimensional state coordinate finite on every bounded time interval. The vector field is locally Lipschitz for \(\tau>0\), even where \(\rho=0\), since the Euclidean norm is Lipschitz. Thus all finite initializations have unique global finite-time solutions. This does not assert convergence or boundedness as \(t\to\infty\).

One exact weaker-than-finite-activity sufficient condition can be stated directly from (8):

\[
 \sup_{t\ge0} E_w(t)
 \le4\int_0^\infty
       \bigl[\langle y-f_{\rm tr}(t),f_{\rm tr}(t)\rangle_m\bigr]_+dt,
                                                                    \tag{11}
\]

where \([a]_+=\max(a,0)\). A suitable moment bound on this positive energy input would suffice to control every passive query. No bound on (11) on the exceptional event follows from (8)–(10).

## 5. Initialized tails and the exact missing estimate

Assume the population initial readout Gram is at least \(2\lambda I_m\), choose a sufficiently large fixed \(K\), and set

\[
 \mathcal G_n=\{\|W_0\|_{\rm op}\le K,\ \Gamma_0\succeq\lambda I_m\}.
\]

Clipping does not affect initialization, so the complete two-layer conditional-Gaussian calculation in `UNCONDITIONAL_TAIL_ROUTE.md` applies unchanged. In particular,

\[
 \Pr(\mathcal G_n^c)\le(4m^2+2)e^{-cn},\quad
 c=\min\{\lambda^2/72,K^2/8-2\log9\}>0.                         \tag{12}
\]

Its proof uses bounded iid first-layer covariance entries, conditionally independent second-layer Gaussian rows, the Lipschitz covariance-to-tanh-covariance map, and a Gaussian matrix net estimate; no trained-neuron independence is needed.

If the own smooth population predictor satisfies the population counterpart of (5), (9) and (12) give, for every finite \(T\),

\[
 \mathbb E\!\left[\mathbf1_{\mathcal G_n^c}
 \int\sup_{t\le T}|f_n(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)\right]
 \le C Y^2(T+\lambda^{-2})e^{-cn}.                              \tag{13}
\]

No query moment condition is needed in (13), because tanh is bounded. For the all-time problem put

\[
 Z_n=\int\sup_{t\ge0}|f_n(t,x)|^2\,d\mu(x),
\]

as a nonnegative extended random variable. The unresolved exceptional-event obligation is

\[
 \mathbb E[Z_n\mathbf1_{\mathcal G_n^c}]\le C/n.                 \tag{14}
\]

For example, a sufficient theorem would be \(\mathbb E Z_n^p\le Cn^a\) for some fixed \(p>1\) and finite \(a\). Hölder and (12) would then imply

\[
 \mathbb E[Z_n\mathbf1_{\mathcal G_n^c}]
 \le C n^{a/p}e^{-c(1-1/p)n}=O(n^{-1}).
\]

Even a moment bound growing exponentially at a sufficiently small rate would suffice. The bounds (9) and (13) instead increase with \(T\); taking \(T\to\infty\) does not prove (14). Smoothness of the vector field is not a Lyapunov or moment estimate.

## 6. An exact actual-model special case: one sample and width one

This special case tests a possible singular-initialization failure mechanism without replacing the network. Let \(m=n=1\), \(u\ne0\), and \(y>0\). The opposite label sign is handled by replacing \(y,w,r,d,\ell\) by their negatives and leaving \(A,v,k,B\) unchanged. The zero-label state is stationary. If \(W_0=0\) or \(A_0u=0\), the prediction and all trainable states remain zero or at initialization: the initial upper feature and every update except the clock update vanish, and \(\tau(t)=1+yt\).

Otherwise let \(\sigma=\operatorname{sgn}(A_0u)\) and \(\zeta=\operatorname{sgn}W_0\). Until fitting, write

\[
 Au=\sigma\alpha,\quad k=\sigma\kappa,\quad
 w=\zeta\sigma\eta,\quad v=\zeta\sigma\nu,\quad
 B=\zeta\beta,\qquad \beta=|W_0|+\nu\kappa.
\]

Initially \(\alpha>0\), \(\kappa=\tanh\alpha>0\), and \(\eta=\nu=0\). Put
\(z=\beta\tanh\alpha>0\), \(g=\tanh z>0\), and \(q=y-\eta g\). As long as \(q\ge0\), direct substitution into (1) gives

\[
\begin{aligned}
 \dot\eta&=2qg,\\
 \dot\nu&=2q\,c_M(\eta\operatorname{sech}^2z),\\
 \dot\alpha&=2q\|u\|_2^2
 c_M\!\left(\operatorname{sech}^2\alpha\,
       \beta c_M(\eta\operatorname{sech}^2z)\right),\\
 \dot\kappa&=\frac q\tau(\tanh\alpha-\kappa),\qquad
 \dot\tau=q.
\end{aligned}                                                    \tag{15}
\]

The first three quantities are nondecreasing and nonnegative. Since \(\alpha\) is nondecreasing and \(\kappa(0)=\tanh\alpha(0)\), the integrating-factor formula for the key equation gives
\(0<\kappa\le\tanh\alpha\), hence \(\dot\kappa\ge0\). Thus \(\beta,z,g\) are nondecreasing. Differentiating the prediction yields

\[
 \frac d{dt}(\eta g)=\dot\eta g+\eta\dot g\ge2qg(0)^2,
 \qquad \dot q\le-2g(0)^2q.
\]

The residual cannot cross zero: zero residual makes the entire vector field vanish, and uniqueness supplies the stationary continuation from a hitting point. Therefore

\[
 0\le q(t)\le ye^{-2g(0)^2t},\quad
 0\le\eta(t)\le y/g(0),\quad
 \sup_{t\ge0,x}|f_1(t,x)|\le y/g(0).                            \tag{16}
\]

In particular every scalar initialization has bounded all-time predictions, and every nonzero-feature initialization fits, without a small-label restriction. For the latter initializations all state blocks converge because their speeds are bounded by a constant times the integrable residual. This input is admissible: with \(u\ne0\), its one-dimensional population initial Gram is strictly positive.

Equation (16) does not prove even the scalar initialization second moment. For Gaussian \(A_0u\), conditioning \(W_0\in[1,2]\) shows that \(\mathbb E[g(0)^{-2}]=\infty\): near \(A_0u=0\), \(g(0)^2\le4(A_0u)^2\), while the Gaussian density is positive. This is divergence of the displayed upper bound, not divergence of the actual predictor moment. Feature learning may substantially improve it. The special case therefore rules out a scalar pathwise blow-up counterexample, but supplies no general-width deconditioning theorem and no counterexample to (2).

## 7. Claim status and remaining bottleneck

Proved here for the smooth system: the gate-composed Lipschitz estimate; deterministic initialized fitting, convergence, and finite activity with the original width-independent small-label threshold; the nonzero top-derivative correction (7); all-initialization finite-time global existence, energy, and activity bounds; and the exact scalar boundedness result (16). The initialized exponential tail and finite-horizon deconditioning follow from the unchanged initialization law and these bounds.

Not proved: a width-controlled all-time moment on \(\mathcal G_n^c\), or an admissible positive-probability actual-model counterexample to it. No arbitrary feature path, frozen-feature dynamics, generic ODE, zero cap, or impossible Gram configuration is used as a counterexample. A divergent readout norm alone would also be insufficient: the passive prediction, rather than a parameter norm, is the stated observable.

The all-time exceptional-event bridge (14) remains open even if a separate good-event root-width estimate to the correct smooth population is supplied. Smooth clipping removes nondifferentiability and quantifies a small derivative mismatch, but neither property closes this bridge. The next tail-specific mathematical obligation is a global estimate for actual trajectories, such as a moment bound for (11), or a genuine admissible divergent passive predictor on a set of positive Gaussian probability.
