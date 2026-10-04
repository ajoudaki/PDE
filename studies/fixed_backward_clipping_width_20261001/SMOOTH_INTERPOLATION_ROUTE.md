# Smooth clipping: width interpolation and its unsummed response

2026-10-01. Scoped independent route. **The requested all-time root-width theorem is not proved here.** Smooth clipping removes the hard threshold measures, but does not close the signed Gaussian covariance estimate needed for the finite-width mean bias. This report gives an explicit positive calculation for the first feature-learning coefficient of the actual smooth flow and identifies the precise remaining interpolation estimate. It also proves two obstructions to shortcuts based on smoothness: the smooth clipped Gaussian label expansion can have zero convergence radius, and finite residual activity does not imply an integrable second derivative of the residual-norm clock.

The scientific inputs were the complete SMOOTH_SETUP.md, FITTING_AND_THRESHOLD.md, CONCENTRATION_ROUTE.md, BIAS_DIMENSION_ROUTE.md, RESOLUTION_INTERPOLATION_ROUTE.md, and CLIPPED_POPULATION_ROUTE.md in this study. The required rigorous-math, conjecture-investigation, and canonical-notation skills, including the neural conventions and the research-contract, adversarial-audit, and proof-search references, were read. No other study, sibling smooth route, experiment, Git operation, or manuscript change was used. The coordinator supplied two audit questions about the residual-norm clock and normalized second derivatives; the calculations answering them below are contained here. Only this report was written. This is an internal result, not promotion review.

## 1. Exact target and what interpolation would have to prove

Let \(m\) training inputs be fixed, put \(u_a=x_a/\sqrt d\), and let \(Y=(m^{-1}\sum_a y_a^2)^{1/2}>0\) be fixed and sufficiently small. At width \(n\), the first matrix is \(A\in\mathbb R^{n\times d}\), the readout is \(w\in\mathbb R^n\), and the memories are \(v_a,k_a\in\mathbb R^n\). Define

\[
B=W_0+\frac1{mn}\sum_a v_a k_a^\top,\qquad
h(x)=\tanh(Ax/\sqrt d),\qquad z(x)=Bh(x),\qquad
g(x)=\tanh z(x),\qquad f_n(t,x)=w^\top g(x)/n.
\]

Write \(h_a=h(x_a)\), \(z_a=z(x_a)\), \(g_a=g(x_a)\), \(r_a=f_n(t,x_a)-y_a\), and \(\rho=\|r\|_2/\sqrt m\). For fixed \(M>0\), the smooth cap is \(c_M(s)=M\tanh(s/M)\), and the trained backward signals and evolution are exactly

\[
\begin{gathered}
d_a=c_M(w\odot\operatorname{sech}^2z_a),\qquad
\ell_a=c_M\bigl(\operatorname{sech}^2(Au_a)\odot B^\top d_a\bigr),\\
\dot w=-\frac2m\sum_a r_ag_a,\qquad
\dot A=-\frac2m\sum_a r_a\ell_a u_a^\top,\\
\dot v_a=-2r_ad_a,\qquad
\dot k_a=\frac\rho\tau(h_a-k_a),\qquad \dot\tau=\rho.
\end{gathered}                                                     \tag{1}
\]

Initially \(A_0\) has independent standard Gaussian entries, \(W_0\) has independent \(N(0,1/n)\) entries independently of \(A_0\), \(w=v_a=0\), \(k_a=h_a(0)\), and \(\tau=1\). The matrix \(W_0\) is fixed throughout the evolution; \(B^\top\) is the reconstructed action's actual transpose.

The own-population target is

\[
\left(\mathbb E\int\sup_{t\ge0}
 |f_n(t,x)-f_{\infty,M}(t,x)|^2\,d\mu(x)\right)^{1/2}
 \le C_{M,\mu}n^{-1/2},                                           \tag{2}
\]

for a fixed bounded query law \(\mu\), including the finite-width mean bias. A positive initial population readout-feature Gram gap and small fixed labels are assumed. Bounds conditioned on an initialized fitting event are weaker than (2); an all-time bound on its complement remains a separate obligation.

The ordinary output derivative contains \(p_a=w\odot\operatorname{sech}^2z_a\), whereas the trained signal is \(d_a=c_M(p_a)\). They are distinct whenever \(p_a\ne0\). No calculation below invokes top-clip inactivity.

## 2. What smooth clipping provides

For the scalar joint gate

\[
F_M(\alpha,p)=M\tanh\bigl(p\operatorname{sech}^2\alpha/M\bigr),
\]

put \(q=\operatorname{sech}^2\alpha\) and \(u=pq/M\). Differentiation gives

\[
|\partial_pF_M|=q\operatorname{sech}^2u\le1,\qquad
|\partial_\alpha F_M|
 =2M|\tanh\alpha|\,|u|\operatorname{sech}^2u\le2M.                 \tag{3}
\]

The last bound uses \(|u|\operatorname{sech}^2u\le1\), immediate for \(|u|\le1\), and following for \(|u|\ge1\) from \(\cosh^2u\ge u^2\ge|u|\). Thus the useful global joint Lipschitz bound survives, and \(|c_M(s)|\le|s|\).

All fixed-order scalar partial derivatives of \(F_M\) are globally bounded. After at least one differentiation, every term is a constant times

\[
M^{1-b}q^b P(\tanh\alpha)u^j\tanh^{(k)}u,\qquad k\ge1,             \tag{4}
\]

where \(b\) is the number of \(p\)-derivatives, \(P\) is a polynomial, and \(j,k\) are finite integers. The rules \(\partial_\alpha u=-2u\tanh\alpha\), \(\partial_pu=q/M\), and \(\partial_\alpha\tanh\alpha=q\) preserve this form. For every \(k\ge1\), \(\tanh^{(k)}u\) is \(\operatorname{sech}^2u\) times a polynomial in \(\tanh u\), by induction. It decays exponentially, so \(u^j\tanh^{(k)}u\) is bounded. The other factors are bounded for fixed \(M>0\). This proves the claim without threshold surface terms.

The deterministic activity proof in the assigned fitting input uses only cap contraction, the bounded forward activation, and the true operator norm of \(B\). It therefore gives the same smooth-flow bounds on the initialized fitting event:

\[
\rho(t)\le Ye^{-\kappa t},\qquad
\int_0^\infty\rho(t)\,dt\le CY,\qquad
\|w\|_\infty\le CY,\qquad \|B-W_0\|_{\rm op}\le CY^2.             \tag{5}
\]

That proof differentiates the prediction as \(\dot r=-2\Gamma_w r+w^\top\dot g/n\); it never substitutes \(d\) for \(p\). The kernel-based first-order stability and independent-block joining arguments in the concentration and width-dimension inputs use (3), cap contraction, bounded trained fields, and the same ordinary output derivative. Their joining step does not use hard-clip inactivity. They transfer to the smooth flow with changed constants, giving centered root-width bounds and comparing the joined block system with two independent width-\(n\) flows. The comparison between the block and fully connected variance profiles is still missing.

These are first-order statements. Equation (4) does not turn them into width-independent second-order estimates on normalized state spaces, or into integrable all-time second responses. Sections 5 and 6 check those distinctions.

## 3. Exact profile interpolation and the missing estimate

Put \(N=2n\). Choose balanced signs \(s_i,t_j\in\{-1,1\}\) on the two physical layers, and let the independent initialized matrix entries have variances

\[
S_{ij}^{\theta}=\frac{1+\theta s_it_j}{N},\qquad 0\le\theta\le1.
                                                                    \tag{6}
\]

At \(\theta=0\) this is the canonical width-\(N\) matrix. At \(\theta=1\) it is two independent width-\(n\) diagonal blocks, each with entry variance \(1/n\). Row and column sums of \(S^\theta\) are one. Run (1) with this single matrix and its transpose at every profile.

Use one bounded prediction-velocity extension \(a_N^{\mathrm{ext}}(t,x,A_0,W)\), independent of \(\theta\), as constructed in the assigned concentration and dimension inputs. It agrees with \(\partial_t f_N\) on the fitting event and obeys

\[
|a_N^{\mathrm{ext}}|\le B_x(t),\qquad
\operatorname{Lip}_{W,F}(a_N^{\mathrm{ext}})\le L_x(t),\qquad
\int_0^\infty(B_x(t)+L_x(t))\,dt<\infty.                           \tag{7}
\]

This Lipschitz constant is for the raw matrix Frobenius metric, equivalent to a constant \(N^{-1/2}L_x(t)\) in standard Gaussian root coordinates. Choose the permutation-invariant extension from the dimension input: its good set, original observable, and McShane distance are invariant under independent relabelings of the physical layers. The extension need only be Lipschitz: smooth clipping does not make a McShane extension twice differentiable.

For \(0<\theta<1\), Gaussian density differentiation followed by one integration by parts gives the exact weak identity

\[
\frac d{d\theta}\mathbb E a_N^{\mathrm{ext}}(W^\theta)
 =\frac1{2N}\sum_{ij}s_it_j\,
  \mathbb E\left[
   \frac{W_{ij}^{\theta}}{S_{ij}^{\theta}}
        \partial_{W_{ij}}a_N^{\mathrm{ext}}(W^\theta)\right].       \tag{8}
\]

Time, input, and first-layer arguments are suppressed only in this formula. For a smooth function, the right side is also

\[
\frac1{2N}\mathbb E\sum_{ij}s_it_j
                   \partial_{W_{ij}}^2a_N^{\mathrm{ext}}(W^\theta).
                                                                    \tag{9}
\]

For the Lipschitz extension, (9) means Gaussian pairing with its distributional second derivative, defined by (8). Convolve in raw matrix coordinates, use the unchanged first-derivative bound, and pass to the limit against the Gaussian density on compact subintervals of \(0<\theta<1\) to justify the weak formula.

The crude bound from (7) is

\[
\left|\frac d{d\theta}\mathbb E a_N^{\mathrm{ext}}\right|
 \le\frac{\sqrt N\,L_x(t)}{2\sqrt{1-\theta^2}},                    \tag{10}
\]

because \(\sum_{ij}(S_{ij}^{\theta})^{-1}=N^3/(1-\theta^2)\). This is integrable in \(\theta\), but has no decaying width factor. It justifies extending the integrated identity to the block endpoint.

Block permutation invariance and simultaneous exchange of the blocks leave two expected diagonal Hessian entries in (9). Denote them by \(h_+(t,x,\theta)\) and \(h_-(t,x,\theta)\), according to \(s_it_j=+1\) or \(-1\), using the preceding weak meaning. Each class has \(N^2/2\) entries, so

\[
\frac d{d\theta}\mathbb E a_N^{\mathrm{ext}}(W^\theta)
       =\frac N4(h_+-h_-).                                      \tag{11}
\]

A sufficient **unproved** input for the conditional bias theorem is

\[
\int_0^\infty\int_0^1
 |h_+(t,x,\theta)-h_-(t,x,\theta)|\,d\theta\,dt
 \le C_x N^{-3/2},                                               \tag{12}
\]

uniformly on the required bounded query set. It would bound the endpoint mean-velocity difference integrated over time by \(C_xN^{-1/2}\). Combined with the independent-block joining estimate, it gives the dyadic conditional-mean bound \(\sup_t|m_{2n}(t,x)-m_n(t,x)|\le C_xn^{-1/2}\). Here \(m_n\) is the actual finite-width mean conditioned on the fitting event. Summing the geometric series and using the own-population qualitative identification would give \(\sup_t|m_n-f_{\infty,M}|\le C_xn^{-1/2}\). This is a conditional implication, not a proof of (12) or (2).

The fixed polynomial matrix-action theorem in the assigned resolution input proves profile-independent leading Wick forests and an \(O(N^{-1})\) remainder for each separately fixed polynomial program. It retains the exact transpose and has no history-Gram inverse. Its constants grow with the expression, Gaussian pairing count, and root moments. That theorem does not control those constants for approximations to the full trajectory at accuracy \(N^{-1/2}\). Bounded scalar derivatives do not supply the missing summation bound.

## 4. An explicit positive calculation in the actual smooth flow

The first feature-learning term in the initial prediction expansion has an explicit \(O(n^{-1})\) mean-bias estimate. This verifies a nontrivial finite-order cancellation using the actual reused transpose. It does not bound the Taylor remainder uniformly in time.

Take one sample, \(m=d=1\), \(x=1\), and fixed \(y>0\). At initialization put

\[
\alpha_j=(A_0)_j,\quad h_j=\tanh\alpha_j,\quad
\psi_j=\operatorname{sech}^2\alpha_j,\quad
z=W_0h,\quad g=\tanh z,\quad b(z)=\tanh z\operatorname{sech}^2z.
                                                                    \tag{13}
\]

Define

\[
q_n=\frac{h^\top h}{n},\quad q_{2,n}=\frac{g^\top g}{n},\quad
\nu_n=\frac1n\sum_i b(z_i)^2,\quad
Q_n=\frac1n\|\psi\odot W_0^\top b(z)\|_2^2.                       \tag{14}
\]

All derivatives in the next display are at time zero. Since \(c_M(0)=0\), \(c_M'(0)=1\), and \(w=v=0\), direct differentiation of (1) gives

\[
\begin{gathered}
w'=2yg,\qquad d'=2yb(z),\qquad
\ell'=2y\psi\odot W_0^\top b(z),\\
A''=4y^2\psi\odot W_0^\top b(z),\qquad
v''=4y^2b(z),\qquad k'=k''=0,\\
z''=4y^2\left[q_nb(z)+
 W_0\bigl(\psi^2\odot W_0^\top b(z)\bigr)\right].
\end{gathered}                                                     \tag{15}
\]

The square on \(\psi\) is coordinatewise. Both hidden feature velocities vanish at zero. The prediction product rule, with the ordinary output activation derivative, yields

\[
f_n'''(0)=8yq_{2,n}^3+32y^3(q_n\nu_n+Q_n).                       \tag{16}
\]

Indeed, \(f_n'(0)=2yq_{2,n}\), \(f_n''(0)=-4yq_{2,n}^2\), and \(w'''=8yq_{2,n}^2g+2yg''\). Hence \(f_n'''=8yq_{2,n}^3+8y\,g^\top g''/n\), and (15) proves (16). The positive term \(Q_n\) is the first lower-layer learning contribution. The smooth cap was retained through its exact derivative at zero; higher time coefficients need not be independent of \(M\).

For a standard normal \(G\), define

\[
q=\mathbb E\tanh^2G>0,\qquad
a_*=\mathbb E\operatorname{sech}^4G,\qquad
d_*=\mathbb E[\operatorname{sech}^4G\tanh^2G].                    \tag{17}
\]

For \(Z_s\sim N(0,s)\), \(0\le s\le1\), put

\[
\gamma(s)=\mathbb E\tanh^2Z_s,\qquad
\nu(s)=\mathbb E b(Z_s)^2,\qquad
\kappa(s)=\mathbb E b'(Z_s).                                     \tag{18}
\]

Then the actual initial derivative obeys

\[
\left|\mathbb Ef_n'''(0)-
 \left(8y\gamma(q)^3+
 32y^3\{q\nu(q)+d_*\kappa(q)^2+a_*\nu(q)\}\right)\right|
 \le \frac{C(y+y^3)}n.                                          \tag{19}
\]

No fit-event conditioning is needed for this initial calculation.

To prove the transpose contribution, condition on \(h,z\). The Gaussian rows of \(W_0\), conditioned on their inner products with \(h\), have means \(z_i h/\|h\|_2^2\) and covariances \(n^{-1}(I-hh^\top/\|h\|_2^2)\), independently across rows. Orthogonal Gaussian projection onto the span of \(h\) and its complement proves this decomposition. Thus, with \(T=W_0^\top b(z)\),

\[
\mathbb E[T_j^2\mid h,z]
 =\frac{h_j^2}{\|h\|_2^4}\left(\sum_i z_i b(z_i)\right)^2
  +\nu_n\left(1-\frac{h_j^2}{\|h\|_2^2}\right).                  \tag{20}
\]

The event \(h=0\) has probability zero. Put \(a_n=n^{-1}\sum_j\psi_j^2\) and \(d_n=n^{-1}\sum_j\psi_j^2h_j^2\). Given \(h\), the \(z_i\) are iid \(N(0,q_n)\). Gaussian integration by parts gives \(\mathbb E[Z_sb(Z_s)]=s\kappa(s)\). Sum (20) with weights \(\psi_j^2/n\) and average over \(z\) to obtain the exact formula

\[
\mathbb E[Q_n\mid h]
 =d_n\kappa(q_n)^2+a_n\nu(q_n)
  +\frac{d_n}{n}
   \left\{\frac{\operatorname{Var}(Z_{q_n}b(Z_{q_n}))}{q_n^2}
                         -\frac{\nu(q_n)}{q_n}\right\}.          \tag{21}
\]

The small-\(q_n\) denominators cause no loss: \(|b(z)|\le|z|\) implies \(\nu(s)\le s\) and \(\operatorname{Var}(Z_sb(Z_s))\le\mathbb EZ_s^4=3s^2\). Thus the braces have absolute value at most four for every \(s>0\).

The functions in (18) have bounded first and second derivatives on \([0,1]\). For a bounded smooth scalar function \(F\) with bounded derivatives through order four,

\[
\frac d{ds}\mathbb EF(Z_s)=\tfrac12\mathbb EF''(Z_s),\qquad
\frac {d^2}{ds^2}\mathbb EF(Z_s)=\tfrac14\mathbb EF^{(4)}(Z_s).
                                                                    \tag{22}
\]

For \(s>0\), differentiate the Gaussian density and integrate by parts twice; bounded derivatives justify the integrations. Bounded convergence extends the derivatives and Taylor remainder to zero. Apply this to \(\tanh^2\), \(b^2\), and \(b'\); all required scalar derivatives are bounded.

The vector \((q_n,a_n,d_n)\) is an average of iid bounded vectors, with exactly mean \((q,a_*,d_*)\) and expected squared distance at most \(C/n\). Taylor's formula for \((s,A,D)\mapsto D\kappa(s)^2+A\nu(s)\), whose Hessian is bounded on the relevant compact domain, and (21) give

\[
|\mathbb EQ_n-[d_*\kappa(q)^2+a_*\nu(q)]|\le C/n.                 \tag{23}
\]

Likewise \(\mathbb E(q_n\nu_n\mid h)=q_n\nu(q_n)\), and its mean differs from \(q\nu(q)\) by \(C/n\). Conditional on \(h\), the summands in \(q_{2,n}\) are iid in \([0,1]\), with mean \(\gamma(q_n)\); their average has variance at most \(1/n\). A Taylor estimate for \(u^3\) gives \(|\mathbb E(q_{2,n}^3\mid h)-\gamma(q_n)^3|\le C/n\). Another Taylor estimate in \(q_n\) bounds its mean's difference from \(\gamma(q)^3\) by \(C/n\). Substituting these three bounds into (16) proves (19).

This is a finite-width mean calculation for a nonlinear learned-feature coefficient, with the reused transpose fully retained. It gives no estimate for the repeated descendants needed in (12), and does not interchange an infinite time expansion with expectation or with the width limit.

## 5. The smooth clipped Gaussian label series can still diverge

The hard-cap diagnostic in the assigned resolution input used a flat threshold remainder. Smooth clipping removes that mechanism but does not ensure a convergent label series. Consider

\[
H(\varepsilon)=\mathbb E\tanh^2(\varepsilon G),\qquad G\sim N(0,1).
                                                                    \tag{24}
\]

It is \(C^\infty\) on the real line: every fixed derivative of \(\tanh^2\) is bounded, and the corresponding finite Gaussian moment dominates differentiation under expectation. Write

\[
\tanh^2 z=\sum_{k\ge1}c_kz^{2k}
\]

for the scalar complex Taylor series at zero. Its convergence radius is \(\pi/2\), since \(\cosh z=0\) exactly at \(i\pi/2+i\pi\mathbb Z\), and \(\sinh z\ne0\) at those points. The nearest nonremovable poles of \(\tanh^2\) are therefore at \(\pm i\pi/2\), and the coefficient radius formula gives

\[
\limsup_{k\to\infty}|c_k|^{1/(2k)}=2/\pi.                        \tag{25}
\]

The actual Taylor coefficients of \(H\), by the justified finite-order differentiation, are

\[
\frac{H^{(2k)}(0)}{(2k)!}=c_k\mathbb EG^{2k}
                         =c_k(2k-1)!!.                         \tag{26}
\]

Gaussian integration by parts recursively gives the last equality. The \(2k\)-th roots of these Gaussian moments tend to infinity: the last \(\lfloor k/2\rfloor\) factors in the double factorial are at least \(k\), already giving a diverging lower bound of order \(k^{1/4}\). Along a subsequence on which the roots in (25) are bounded below by a positive constant, the coefficient roots in (26) diverge. The Taylor series of \(H\) consequently has radius zero.

For the actual cap, \(\mathbb E[c_M(\varepsilon G)^2]=M^2H(\varepsilon/M)\), with the same zero-radius conclusion for every fixed \(M>0\). This is a proof-route counterexample, not an asserted formula for the network predictor. It rules out the inference that bounded scalar derivatives, or correct width bias at every fixed coefficient, permit a convergent small-label summation of the smooth flow. An exact nonlinear summation or a quantitative width-dependent remainder bound is necessary.

## 6. Two further second-response checks

First, scalar Hessian bounds do not give a uniform Hessian in the normalized state norm. Set \(\|v\|_{2,n}=\|v\|_2/\sqrt n\). For the coordinatewise cap at \(p_0\mathbf1\), where \(c_M''(p_0)\ne0\), take both directions to be \(u=v=\sqrt n\,e_1\). Their normalized norms are one, but

\[
\|D^2c_M(p_0\mathbf1)[u,v]\|_{2,n}
                         =|c_M''(p_0)|\sqrt n.                  \tag{27}
\]

The joint gate has the same issue at fixed \(\alpha=0\). An arbitrarily small fixed nonzero \(p_0\) suffices. In a probability space, unit \(L^2\) perturbations supported on a set of measure \(\delta\) have product \(L^2\) norm \(\delta^{-1/2}\). The corresponding Nemytskii map thus need not have a bounded second derivative \(L^2\times L^2\to L^2\). Genuine Gaussian entrywise tangent fields may obey better bounds, but those need proof. These perturbations are not asserted to be network responses.

Second, the clock is still driven by \(\rho=\|r\|_2/\sqrt m\), which is not globally smooth at zero. Away from zero its Hessian is

\[
D^2\rho(r)[u,u]
 =\frac{\|u\|_2^2}{m\rho}
       -\frac{(r^\top u)^2}{m^2\rho^3}.                          \tag{28}
\]

With nonzero labels, a finite-dimensional trajectory cannot reach residual zero at a finite time. Every residual-zero state is an equilibrium of (1), and backward local uniqueness would make a trajectory arriving there stationary before arrival. Finite-time local differentiation is therefore not ruled out at the actual trajectory. Nevertheless, (28) has a potentially unbounded cost as fitting proceeds.

A contained example shows why exponential fitting and finite activity do not control that cost. Fix \(0<\alpha<\beta\), and for small \(|a|\) consider

\[
K(a)=\begin{pmatrix}\beta&a\\a&\alpha\end{pmatrix},\qquad
\dot r=-K(a)r,\qquad r(0)=Ye_1.                                 \tag{29}
\]

For \(|a|\le\alpha/2\), \(K(a)\succeq(\alpha/2)I\). Hence residuals decay uniformly exponentially and \(\int_0^\infty\|r(t,a)\|_2dt\le2Y/\alpha\). At \(a=0\),

\[
r=Ye^{-\beta t}e_1,\qquad
u:=\partial_a r
 =-\frac{Y}{\beta-\alpha}(e^{-\alpha t}-e^{-\beta t})e_2.          \tag{30}
\]

Differentiating again gives \(\partial_a^2r=v_1e_1\), where

\[
v_1(t)=\frac{2Y}{\beta-\alpha}
 \left[\frac{e^{-\alpha t}-e^{-\beta t}}{\beta-\alpha}
                             -te^{-\beta t}\right]\ge0.         \tag{31}
\]

Its sign also follows from \(v_1'=-\beta v_1-2u_2\), \(u_2\le0\), and \(v_1(0)=0\). The norm chain rule gives

\[
\left.\partial_a^2\|r(t,a)\|_2\right|_{a=0}
 =v_1(t)+\frac{Y}{(\beta-\alpha)^2}
          e^{\beta t}(e^{-\alpha t}-e^{-\beta t})^2.              \tag{32}
\]

When \(\beta\ge2\alpha\), its integral over all time diverges. For strict inequality the second term grows exponentially; at equality it tends to a positive constant. The first sensitivity (30), however, is integrable. Thus uniform exponential fitting and finite activity do not imply an integrable pathwise second derivative of the activity clock, even with a fixed initial residual and a smooth coercive kernel.

This does not falsify the neural prediction theorem. It tests an alleged general derivative estimate. Weak Gaussian interpolation may retain cancellations lost in a pathwise absolute Hessian bound; averaging over random parameters may remove a singularity at a single parameter. Those would be additional estimates, not consequences of smooth clipping.

## 7. Route verdict

Established here: the scalar all-order smooth-gate bound; continued validity of the first-order activity and interpolation mechanisms; and the explicit \(O(n^{-1})\) initial nonlinear coefficient estimate (19). Formula (21) displays a true reused-transpose finite-width correction without a history-Gram inverse.

Not established: the signed-trace bound (12), a nonlinear matrix-action expansion with summable width-defect constants, or a quantitative approximation that passes from fixed programs to the continuous all-time flow. Smooth clipping removes hard threshold measures but leaves this central statistical obligation. The initial calculation gives no bound on later response contributions. Section 5 prevents summing them merely by invoking fixed small labels; Section 6 prevents inferring the required all-time Hessian estimates from scalar smoothness and fitting.

The full unconditioned estimate (2) also requires an all-time moment bound for the actual trajectory outside the fitting event. A bounded extension used for concentration and interpolation is not such a bound for the original trajectory.

Recommended status: **blocked at the nonlinear signed covariance estimate, with a verified first nonlinear source calculation**. Reopen upon a proof of (12), or a comparably strong exact nonlinear loop-summation estimate with integrable time cost and genuine Gaussian tangent scales. The root-width conjecture for the specified smooth flow remains open in this route; no counterexample to that conjecture has been produced.
