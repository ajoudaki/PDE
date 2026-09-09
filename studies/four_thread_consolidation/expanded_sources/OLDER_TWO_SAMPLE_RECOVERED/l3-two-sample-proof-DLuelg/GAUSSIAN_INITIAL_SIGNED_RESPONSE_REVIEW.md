# Independent adversarial audit of Gaussian initialization and the first response step

## Scope, provenance, and verdict

**Verdict: the initialization theorem and the exact first-step identities are correct in their stated scope. No required mathematical repair was found.** In particular, negative signed curvature does not imply that the full matrix is negative semidefinite: at the actual limiting initialization the full matrix is indefinite in both label modes. The historical and current top-response blocks in (23) have the stated factors and signs, provided the source slots are kept distinct during differentiation.

This review used only the following mathematical inputs:

1. `GAUSSIAN_INITIAL_SIGNED_RESPONSE.md`, in full, 485 lines.
2. `TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md`, literal lines 26--150, for its stipulated scalar law, derivative convention, and zero-time base case.
3. `CONTRACT_AND_LEDGER.md`, literal lines 10--81, for the exact model.

The procedural skill `/etc/codex/skills/solve-math-rigorously/SKILL.md` was read directly and completely. No other mathematical file, task history, review, agent, experiment, or external theorem was used. In particular, the finite-program identification assertion in the supplied bootstrap excerpt is not used as an independently proved theorem: the first-step calculation below is an algebraic calculation in the stipulated scalar law. The initial covariance recursion is also checked directly against the model's Gaussian weight normalization.

SHA-256 hashes of the audited bytes:

| Input | SHA-256 |
|---|---|
| Full candidate | `05708450c2896f62e9ec39beeb67c9b9d1e804ba37a96fa8e342d6cd3692e1f1` |
| Bootstrap, lines 26--150, with their original line endings | `907fd403144823a76631119cab844cba037c156491f55b17bd882907387bed38` |
| Contract, lines 10--81, with their original line endings | `e633994927965510b9c0605d27ed221b33de485caa7cda2bb9029a6343707d0e` |
| Procedural skill, full file | `9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7` |

The two excerpt hashes agree with those recorded by the candidate. All candidate line references below refer to the full-file hash above. The candidate was not edited.

The independent argument proceeds by checking the analytic exchanges, comparing the two contributions to the full matrix, determining the actual covariance parameters, and only then differentiating the first-step formal maps. This order keeps the curvature sign, matrix inertia, and source-response coefficients logically separate.

## 1. Elementary integrals and their endpoints

Set

\[
\varepsilon=\frac1{10},\qquad f(x)=\arctan x,\qquad
\phi(x)=1+\varepsilon f(x),\qquad
h(x)=\frac1{1+x^2},\qquad
f''(x)=h'(x)=-\frac{2x}{(1+x^2)^2}.
\]

Fix \(q>0\). For \(t\in[-q,q]\), let \((X,Y)\) be a centered Gaussian pair with common variance \(q\) and covariance \(t\). There is no need for a joint density: take independent standard normal \(N_1,N_2\) and set

\[
X=\sqrt q\,N_1,\qquad
Y=\frac{t}{\sqrt q}N_1+\sqrt{q-t^2/q}\,N_2.
\]

At \(t=q\), \(Y=X\); at \(t=-q\), \(Y=-X\). This construction remains valid at both endpoints.

### 1.1 Laplace identities

The elementary integral of \(e^{-(1-ix)u}\) on the positive half-line is \((1-ix)^{-1}\), so

\[
\int_0^\infty e^{-u}\cos(ux)\,du=\frac1{1+x^2}=h(x).
\]

Let \(I(x)=\int_0^\infty e^{-u}\sin(ux)/u\,du\). Its integrand is absolutely integrable because

\[
e^{-u}\frac{|\sin(ux)|}{u}\le |x|e^{-u}.
\]

The derivative integrand is bounded in absolute value by \(e^{-u}\), uniformly in \(x\). Thus \(I'(x)=h(x)\) and \(I(0)=0\), which identifies \(I(x)=\arctan x\). Differentiating the cosine integral is justified by \(u e^{-u}\), giving

\[
f''(x)=-\int_0^\infty u e^{-u}\sin(ux)\,du.
\]

This checks all three signs and all powers of \(u\) in candidate (2). The bounds control the origin as well as infinity.

### 1.2 Gaussian trigonometric products

For a centered scalar normal variable \(S\) with variance \(s>0\), let \(g(r)=\mathbb E e^{irS}\). Differentiation is permitted by \(\mathbb E|S|<\infty\). Writing its density as \(p_s\), the identity \(p_s'(x)=-xp_s(x)/s\) and integration by parts give

\[
\mathbb E[S e^{irS}]
=-s\int e^{irx}p_s'(x)\,dx
=sir\,g(r).
\]

The boundary term is zero because the Gaussian density tends to zero and \(|e^{irx}|=1\). Hence \(g'(r)=-sr g(r)\), \(g(0)=1\), and \(g(r)=e^{-sr^2/2}\). For \(s=0\), \(S=0\) almost surely, and the same formula holds.

Now \(uX\pm vY\) has variance \(q(u^2+v^2)\pm2tuv\ge0\). The cosine sum and difference formulas give

\[
\begin{aligned}
\mathbb E[\sin(uX)\sin(vY)]
 &=e^{-q(u^2+v^2)/2}\sinh(tuv),\\
\mathbb E[\cos(uX)\cos(vY)]
 &=e^{-q(u^2+v^2)/2}\cosh(tuv).
\end{aligned}
\]

This derivation covers zero variances of \(uX-vY\) or \(uX+vY\); it never differentiates or inverts a singular covariance matrix.

### 1.3 Double integrals and Fubini checks

Define

\[
B_q(t)=\mathbb E[h(X)h(Y)],\qquad
J_q(t)=-\mathbb E[f(Y)f''(X)],\qquad
w_q=e^{-u-v-q(u^2+v^2)/2}.
\]

The absolute cosine-product integrand before taking expectation is at most \(e^{-u-v}\). For the sine product,

\[
\mathbb E|\sin(uX)\sin(vY)|
\le uv\,\mathbb E|XY|
\le uv\,\frac{\mathbb E X^2+\mathbb E Y^2}{2}
=uvq.
\]

Consequently the absolute curvature integrand, including its factor \(u/v\), is at most \(q u^2e^{-u-v}\). Both bounds have finite integrals over \((0,\infty)^2\). Expectation and both integrations can therefore be interchanged, including at \(t=\pm q\). The results are

\[
\begin{aligned}
B_q(t)&=\iint w_q\cosh(tuv)\,du\,dv,\\
J_q(t)&=\iint \frac uv w_q\sinh(tuv)\,du\,dv\\
&=\frac12\iint\left(\frac uv+\frac vu\right)
                   w_q\sinh(tuv)\,du\,dv.
\end{aligned}
\]

The last equality is an exchange of \(u\) and \(v\) in an absolutely integrable expression. In particular, the apparent \(1/v\) or \(1/u\) singularities do not create an omitted boundary term or divergent integral.

### 1.4 Parameter differentiation, including one-sided endpoints

For \(|t|\le q\),

\[
-\frac q2(u^2+v^2)+|t|uv
\le-\frac q2(u-v)^2\le0.
\]

Using \(|\sinh z|\le |z|e^{|z|}\) gives the uniform bounds

\[
\begin{aligned}
w_q\cosh(tuv),\ w_q|\sinh(tuv)|&\le e^{-u-v},\\
\frac uv w_q|\sinh(tuv)|&\le q u^2e^{-u-v},\\
|\partial_t(w_q\cosh(tuv))|&\le uv e^{-u-v},\\
\left|\partial_t\left[
\frac12\left(\frac uv+\frac vu\right)w_q\sinh(tuv)
\right]\right|&\le\frac{u^2+v^2}{2}e^{-u-v}.
\end{aligned}
\]

Every majorant is integrable. Indeed the necessary one-dimensional integrals are \(\int_0^\infty u^m e^{-u}\,du=m!\) for nonnegative integers \(m\), obtained by repeated integration by parts. Difference quotients are bounded by the same derivative majorants by integrating the pointwise derivative along a segment contained in \([-q,q]\). This proves differentiation in the interior, its continuous extension to the endpoints, and the corresponding one-sided derivative assertions. No assertion about extending the Gaussian covariance beyond its admissible interval is needed.

It follows that \(B_q\) is even and positive and \(J_q\) is odd, with

\[
J_q'(t)=\frac12\iint(u^2+v^2)w_q\cosh(tuv)\,du\,dv>0.
\]

The strict inequality holds because the integrand is positive throughout the positive quadrant. Thus \(J_q(q)>0\), and \(-J_q(q)<J_q(c)<J_q(q)\) for \(-q<c<q\). All finite parameter integrations used below obey the same majorants. Candidate (2)--(6) pass the integral and endpoint audit.

## 2. Curvature and the full matrix must be checked separately

Let \(U=Z_1,V=Z_2\) have common variance \(q\) and covariance \(c\), and set \(y=(1,\sigma)\), \(\sigma\in\{-1,1\}\). Write

\[
V_\sigma=\frac{\phi(U)+\sigma\phi(V)}2
=\frac{1+\sigma}2+\frac\varepsilon2(f(U)+\sigma f(V)).
\]

Because \(f''\) is odd and the marginal is centered,

\[
\begin{aligned}
K_\sigma
&=\mathbb E[V_\sigma\phi''(U)]\\
&=\frac{\varepsilon^2}{2}
 \mathbb E[(f(U)+\sigma f(V))f''(U)]\\
&=-\frac{J_q(q)+\sigma J_q(c)}{200}.
\end{aligned}
\]

The constant part of the activation contributes zero to this curvature, but it will contribute to the initial forward covariances below. The Gaussian pair is exchangeable even at its singular endpoints, and \(V_\sigma(V,U)=\sigma V_\sigma(U,V)\). Therefore

\[
\mathbb E[V_\sigma\phi''(Z_a)]=y_aK_\sigma.
\]

These are the coefficients in candidate (7)--(8), with no sign or factor discrepancy. The second unconjugated curvature has sign opposite to the first for opposite labels.

Put

\[
A_q=B_q(q),\qquad D_q=A_q-J_q(q),\qquad T_q(t)=B_q(t)-J_q(t).
\]

Since \(\phi'=\varepsilon h\), the derivative-product matrix is

\[
P=\mathbb E[\phi'(Z_a)\phi'(Z_b)]_{a,b}
=\frac1{100}\begin{pmatrix}A_q&B_q(c)\\B_q(c)&A_q\end{pmatrix}.
\]

The full matrix specified by the candidate is thus

\[
\begin{aligned}
M_{ab}&=\frac{y_ay_b}{2}P_{ab}
       +y_a\mathbf1_{a=b}\mathbb E[V_\sigma\phi''(Z_a)],\\
M&=\frac1{200}
\begin{pmatrix}
D_q-\sigma J_q(c)&\sigma B_q(c)\\
\sigma B_q(c)&D_q-\sigma J_q(c)
\end{pmatrix}.
\end{aligned}
\]

The derivative-product contribution cannot be discarded. To compare it with the curvature, first differentiate \(f h\):

\[
(fh)'=h^2+ff''.
\]

Both \(fh\) and its derivative are bounded. With \(p_q'(x)=-xp_q(x)/q\), direct integration by parts gives

\[
\begin{aligned}
D_q
&=\int (fh)'(x)p_q(x)\,dx\\
&=\frac1q\int \frac{x\arctan x}{1+x^2}p_q(x)\,dx>0.
\end{aligned}
\]

The boundary term \(f(x)h(x)p_q(x)\) vanishes at both infinities, and the last integrand is positive for every \(x\ne0\). A variance-\(q>0\) Gaussian gives probability zero to \(0\). The division by \(q\) is used only in this nonzero-variance case.

Next, the already justified parameter derivatives yield

\[
\begin{aligned}
T_q'(t)
&=\iint w_q\left[uv\sinh(tuv)
        -\frac{u^2+v^2}{2}\cosh(tuv)\right]\,du\,dv\\
&=-\frac14\iint w_q\left[(u-v)^2e^{tuv}
                         +(u+v)^2e^{-tuv}\right]\,du\,dv<0.
\end{aligned}
\]

Expanding the two exponentials checks the coefficient \(1/4\). The second term in brackets is positive everywhere in the integration domain, including when \(u=v\). Since \(T_q(q)=D_q\),

\[
T_q(t)>D_q>0\quad(-q\le t<q).
\]

Direct multiplication by \(e_y=(1,\sigma)/\sqrt2\) and \(e_\perp=(1,-\sigma)/\sqrt2\) gives

\[
\lambda_y=\frac{D_q+T_q(\sigma c)}{200},\qquad
\lambda_\perp=\frac{D_q-T_q(-\sigma c)}{200}.
\]

Consequently, for \(-q<c<q\), the first eigenvalue is strictly positive and the second strictly negative. Also

\[
\lambda_y-\lambda_\perp=\frac{B_q(c)}{100}>0,
\]

so the label direction is indeed the direction of the largest eigenvalue. This independently verifies the full matrix, rather than transferring the curvature sign to it.

For completeness, with \(L_q=-T_q'>0\), the exact signed identities are

\[
\lambda_\perp=-\frac1{200}\int_{-\sigma c}^qL_q(t)\,dt,
\qquad
K_-=-\frac1{200}\int_c^qJ_q'(t)\,dt.
\]

Their limits, integration directions, and factors agree with candidate (15)--(16). The opposite-label cancellation as \(c\uparrow q\) applies to \(K_-\) and \(\lambda_\perp\); it does not make \(\lambda_y\) vanish.

### All covariance degeneracies

For \(q>0\), abbreviate \(J=J_q(q)>0\), \(A=A_q\), and \(D=D_q>0\). The complete endpoint check is:

| Covariance and mode | \(K_\sigma\) | \(\lambda_y\) | \(\lambda_\perp\) |
|---|---:|---:|---:|
| \(-q<c<q\), either mode | \(<0\) | \(>0\) | \(<0\) |
| \(c=-q,\ \sigma=+1\) | \(0\) | \(A/100\) | \(0\) |
| \(c=-q,\ \sigma=-1\) | \(-J/100\) | \(D/100\) | \(-J/100\) |
| \(c=q,\ \sigma=+1\) | \(-J/100\) | \(D/100\) | \(-J/100\) |
| \(c=q,\ \sigma=-1\) | \(0\) | \(A/100\) | \(0\) |

At \(c=-q\), \(V=-U\), so \(V_+=1\) and \(V_-=\varepsilon f(U)\). At \(c=q\), \(V=U\), so \(V_-=0\). These support identities check the curvature column directly. They do not erase ambient partial derivatives. In particular, \(V_-=0\) on the diagonal support at \(c=q\) still has a nonzero derivative normal to that support. The positive eigenvalue in the last row is therefore consistent with the vanishing attained value of \(V_-\).

If \(q=0\), positivity of a covariance matrix forces \(c=0\), and \(U=V=0\) almost surely. Direct evaluation, without the \(1/q\) identity, gives

\[
K_\sigma=0,\qquad P=\frac1{100}\begin{pmatrix}1&1\\1&1\end{pmatrix},
\qquad M=\frac{yy^T}{200}.
\]

Its eigenvalues are \(1/100\) and \(0\). Thus all exceptional cases described in the candidate agree with direct evaluation. No strict claim has been silently extended to a zero-variance or exact-cancellation case.

## 3. Actual initial covariance: correct recursion and a sharper range

For \(s>0\) and \(|t|\le s\), define

\[
F_s(t)=\mathbb E[f(X)f(Y)],\qquad R(s)=F_s(s),
\]

where the common variance is \(s\). Applying the sine-product calculation with the factor \(1/(uv)\) gives

\[
F_s(t)=\iint e^{-u-v-s(u^2+v^2)/2}
                  \frac{\sinh(tuv)}{uv}\,du\,dv.
\]

Before the expectation exchange, the absolute integrand is at most \(s e^{-u-v}\). After expectation it is at most \(|t|e^{-u-v}\), by \(|\sinh z|\le|z|e^{|z|}\). Its \(t\)-derivative is bounded by \(e^{-u-v}\). Thus the representation is absolutely convergent and continuously differentiable, with one-sided endpoint derivatives, and

\[
F_s'(t)=B_s(t)>0,\qquad F_s(-t)=-F_s(t),\qquad
F_s(0)=0,\qquad F_s(\pm s)=\pm R(s).
\]

Also, with \(N\) a standard normal variable,

\[
0<R(s)=\mathbb E[\arctan(\sqrt sN)^2]<\frac{\pi^2}{4}.
\]

For the first strict inequality, the integrand is positive except at \(N=0\); for the second, it is strictly below \(\pi^2/4\) at every finite \(N\). These observations verify candidate (17), including the apparent singularities at \(u=0\) or \(v=0\).

The contract gives a root Gaussian pair with variances \(1\) and covariance \(\rho\in[-1,1)\). Expanding the activation product, the terms linear in the odd function \(f\) vanish. Hence the second moments of the layer-one activations are

\[
q_2=1+\varepsilon^2R(1),\qquad
c_2=1+\varepsilon^2F_1(\rho).
\]

These are uncentered activation second moments. They are the covariance entries of the next *preactivation*, whose conditional mean is zero because the weights are centered. Using centered covariances of the activations would incorrectly delete the constant \(1\), particularly at antiparallel inputs.

To check the normalization directly, one row \(w\) of an initial hidden matrix has independent entries of variance \(1/n\), independent of its input activations. Therefore

\[
\mathbb E[(w\cdot h_a)(w\cdot h_b)\mid h_1,h_2]
=\frac1n\sum_i h_{a,i}h_{b,i}.
\]

The conditional row law is centered Gaussian with these covariance entries. The input activation products at the first such layer are independent bounded variables across neurons, so their empirical average has squared mean error at most \(a^4/n\), where \(a=1+\pi/20\) bounds \(|\phi|\). This gives convergence to the displayed second moments: the probability of an error larger than any fixed \(\eta>0\) is at most \(a^4/(n\eta^2)\).

The same argument applies conditionally at the next layer. Conditional rows are independent, the activation products remain bounded by \(a^2\), and the conditional average differs from its conditional expectation by squared mean error at most \(a^4/n\). The latter expectation is continuous in the covariance near the limiting positive-definite layer-two matrix. For example, represent a covariance matrix \(Q\) there by

\[
X_Q=\sqrt{Q_{11}}N_1,\qquad
Y_Q=\frac{Q_{12}}{\sqrt{Q_{11}}}N_1
+\sqrt{Q_{22}-Q_{12}^2/Q_{11}}N_2.
\]

Its coefficients are continuous near that matrix. Since \(|\phi'|\le\varepsilon\) and \(|\phi|\le a\), differences of activation products have expected absolute value at most

\[
a\varepsilon\bigl(\mathbb E|X_Q-X_{Q_*}|
                   +\mathbb E|Y_Q-Y_{Q_*}|\bigr),
\]

which tends to zero with the coefficients. Thus iteration gives precisely the limiting top preactivation covariance

\[
q=1+\varepsilon^2R(q_2),\qquad
c=1+\varepsilon^2F_{q_2}(c_2).
\]

This direct initialization check uses neither a trained-law assertion nor a finite-program response theorem. The actual finite-width top row is generally a mixture over its random conditional covariance; the Gaussian pair asserted here is the limiting initial scalar pair, as the candidate specifies.

To check positive definiteness and the ranges, \(F_1\) is strictly increasing and odd, with endpoint values \(\pm R(1)\). Consequently

\[
c_2\in[1-\varepsilon^2R(1),q_2)
      =[2-q_2,q_2),\qquad 2-q_2>0.
\]

In particular, \(0<c_2<q_2\). The strict upper inequality also follows directly from

\[
q_2-c_2=\frac{\varepsilon^2}{2}
  \mathbb E[(f(G_1)-f(G_2))^2]>0:
\]

\(G_1-G_2\) has variance \(2(1-\rho)>0\), hence is nonzero almost surely, and \(f\) is strictly increasing. This argument includes \(\rho=-1\). It validates the positive-definiteness condition used in the preceding conditional calculation.

Strict increase of \(F_{q_2}\), together with \(0<c_2<q_2\), now proves the candidate's range

\[
1<c<q<1+\frac{\pi^2}{400}.
\]

There is a useful sharper description. The two marginal variances \(q_2,q\) are fixed independently of the input angle. Define

\[
c_{\min}=1+\varepsilon^2F_{q_2}(2-q_2).
\]

Since \(2-q_2>0\), \(c_{\min}>1\). As the scalar input correlation varies through \([-1,1)\), its continuous strictly increasing image is exactly

\[
c\in[c_{\min},q).
\]

The lower endpoint occurs at antiparallel inputs; the excluded upper endpoint is approached as \(\rho\uparrow1\). For actual vectors with fixed \(d\ge2\), all these correlations can be realized. For \(d=1\), the norm condition only permits correlations \(\pm1\), so after excluding \(1\), the actual covariance is just \(c_{\min}\). This dimensional restriction does not affect any candidate inequality or sign conclusion.

Thus candidate (19) is a correct enclosing range, not a claim that \(q,c\) range independently or that every \(1<c<q\) is attained. At every permitted actual initialization, \(0<c<q\), so the full matrix is indefinite. Moreover,

\[
K_+-K_-=-\frac{J_q(c)}{100}<0,
\]

which verifies \(K_+<K_-<0\). No angle-uniform strict lower bound on either negative quantity is established or required.

## 4. Exact step-one coefficients with all source slots retained

Here \(\Delta>0\), at least one step is present, and the stipulated readout update has coefficient \(\Delta/2\). The candidate states the needed cut conditions \(\tau(0)=0\), \(\tau'(0)=1\). All deterministic response coefficients and all Gaussian covariance parameters are held fixed during the formal partial derivatives, exactly as the supplied bootstrap requires.

### 4.1 Zero time: value zero is not formal zero

The empty readout sum gives \(W^{(4)}_0=0\) as a formal expression. Thus

\[
\delta^{(3)}_{0a}=0\text{ formally},\qquad
B^{(3)}_{0a,0b}=0.
\]

The reverse covariance rule then gives \(\zeta^{(2)}_{0a}=0\) almost surely, but the scalar map is retained as

\[
q^{(2)}_{0a}=\zeta^{(2)}_{0a},\qquad
\delta^{(2)}_{0a}
=\phi'(\xi^{(2)}_{0a})\tau_{R_2}(\zeta^{(2)}_{0a}).
\]

Its forward-source derivative is

\[
\frac{\partial\delta^{(2)}_{0a}}
     {\partial\xi^{(2)}_{0b}}
=\mathbf1_{a=b}\phi''(\xi^{(2)}_{0a})
                     \tau_{R_2}(\zeta^{(2)}_{0a}),
\]

which is zero on the attained law. There is no learned term at zero time, so \(B^{(2)}_0=0\). In turn, \(\zeta^{(1)}_0=0\) almost surely and \(q^{(1)}_0=\zeta^{(1)}_0\) formally. These facts show that both lower reverse fields and both lower backward fields vanish in value at time zero.

In contrast, the historical reverse-source derivative is

\[
\left.\frac{\partial\delta^{(2)}_{0a}}
 {\partial\zeta^{(2)}_{0b}}\right|_{\mathrm{attained}}
=\mathbf1_{a=b}\phi'(\xi^{(2)}_{0a})>0
\quad\text{when }a=b.
\]

Candidate (25) is therefore correct. Deleting this variance-zero coordinate would change the stipulated formal map.

### 4.2 The first forward values and their formal expressions

Since the attained \(q^{(1)}_0=0\), the first bottom update vanishes, giving \(H^{(1)}_1=H^{(1)}_0\) almost surely. The source covariance rule implies, for each sample,

\[
\mathbb E[(\xi^{(2)}_{1a}-\xi^{(2)}_{0a})^2]
=\mathbb E[(H^{(1)}_{1a}-H^{(1)}_{0a})^2]=0.
\]

The layer-two response terms multiply the attained \(\delta^{(2)}_0=0\), so \(H^{(2)}_1=H^{(2)}_0\) almost surely. Repeating the same variance calculation gives \(\xi^{(3)}_1=\xi^{(3)}_0\) almost surely.

These equalities establish candidate (20). Formally, however,

\[
Z^{(2)}_{1a}=\xi^{(2)}_{1a}
 +\sum_b A^{(2)}_{1a,0b}\delta^{(2)}_{0b}
\]

still contains the historical reverse slots. At the top layer the stronger formal equality does hold:

\[
Z^{(3)}_{0a}=\xi^{(3)}_{0a},\qquad
Z^{(3)}_{1a}=\xi^{(3)}_{1a},
\]

because every \(\delta^{(3)}_{0b}\) is identically zero, even before evaluation. A possibly nonzero \(A^{(3)}_{1a,0b}\) has no contribution to this expression or its derivative: it multiplies a formally zero map, whose derivatives are also zero.

### 4.3 Historical and current top derivatives

The exact time-one readout and top backward map are

\[
W^{(4)}_1=\frac\Delta2\sum_d y_d\phi(\xi^{(3)}_{0d}),
\qquad
\delta^{(3)}_{1a}
=\frac\Delta2\sum_d y_d\phi(\xi^{(3)}_{0d})
                           \phi'(\xi^{(3)}_{1a}).
\]

The variables \(\xi^{(3)}_{0b}\) and \(\xi^{(3)}_{1b}\) are distinct formal coordinates. Thus

\[
\begin{aligned}
\frac{\partial\delta^{(3)}_{1a}}
     {\partial\xi^{(3)}_{0b}}
 &=\frac\Delta2 y_b\phi'(\xi^{(3)}_{0b})
                         \phi'(\xi^{(3)}_{1a}),\\
\frac{\partial\delta^{(3)}_{1a}}
     {\partial\xi^{(3)}_{1b}}
 &=\Delta\mathbf1_{a=b}
 V_\sigma(\xi^{(3)}_{01},\xi^{(3)}_{02})
                         \phi''(\xi^{(3)}_{1a}).
\end{aligned}
\]

There is no current-slot derivative of the readout: it only uses historical slots. There is no historical-slot derivative of the current gate: its formal argument is only the current slot. Differentiating after identifying the two times would add these derivatives together and lose the two separate coefficients.

For \(B^{(3)}_{1a,0b}\), the learned term in the scalar law is

\[
\frac\Delta2y_b\mathbb E[
\delta^{(3)}_{1a}\delta^{(3)}_{0b}]=0.
\]

For \(B^{(3)}_{1a,1b}\), the strict-past indicator makes the learned term absent. Only now imposing \(\xi^{(3)}_1=\xi^{(3)}_0\) inside the expectations yields

\[
B^{(3)}_{1a,0b}=\frac\Delta2 y_bP_{ab},\qquad
B^{(3)}_{1a,1b}=\Delta\mathbf1_{a=b}y_aK_\sigma.
\]

These are exact for every permitted positive \(\Delta\); there is no remainder or omitted higher-order term. In fully explicit matrices, set \(S_\sigma=J_q(q)+\sigma J_q(c)\). Then

\[
B^{(3)}_{1,0}=\frac\Delta{200}
\begin{pmatrix}A_q&\sigma B_q(c)\\B_q(c)&\sigma A_q\end{pmatrix},
\qquad
B^{(3)}_{1,1}=-\frac{\Delta S_\sigma}{200}
\begin{pmatrix}1&0\\0&\sigma\end{pmatrix}.
\]

This verifies every sign, the factors \(1/2\), \(\varepsilon^2=1/100\), and the sample indices in candidate (23). At actual initialization \(S_\sigma>0\). The historical entries have the sign of their column label and are all nonzero. The current diagonal entries have sign \(-y_a\) and are nonzero; its off-diagonal entries are exactly zero. For opposite labels, in particular, the current diagonal signs are negative and positive before multiplication by the labels.

With \(Y=\operatorname{diag}(1,\sigma)\),

\[
YB^{(3)}_{1,0}=\frac\Delta2YPY,\qquad
YB^{(3)}_{1,1}=\Delta K_\sigma I,\qquad
Y(B^{(3)}_{1,0}+B^{(3)}_{1,1})=\Delta M.
\]

Thus candidate (24) is exact. The full matrix \(M\) is neither the current block alone nor a statement about the eigenvalues of the unweighted causal family of coefficients. Since \(H^{(2)}_1=H^{(2)}_0\) in value, the reverse query at step one can be evaluated as

\[
q^{(2)}_1=\zeta^{(2)}_1
 +(B^{(3)}_{1,0}+B^{(3)}_{1,1})H^{(2)}_0.
\]

This simplification of attained values is not an equality of the underlying formal maps after future source differentiation.

The exceptional current-block cancellations are also consistent: it vanishes at \(c=-q,\sigma=+1\), at the excluded endpoint \(c=q,\sigma=-1\), and at \(q=c=0\). The historical block remains nonzero in all these cases because \(\phi'(z)>0\) for every finite \(z\). In the \(c=q,\sigma=-1\) case the attained readout is zero, but its ambient historical derivatives are nonzero; this is another reason not to delete slots using support identities.

### 4.4 A retained reverse slot affects a later formal map

Differentiate the displayed formal expression for \(Z^{(2)}_{1a}\) in \(\zeta^{(2)}_{0b}\), holding \(A^{(2)}\) and the Gaussian parameters fixed. The direct source \(\xi^{(2)}_{1a}\) is a different slot. On the attained law,

\[
\left.\frac{\partial H^{(2)}_{1a}}
     {\partial\zeta^{(2)}_{0b}}\right|_{\mathrm{attained}}
=A^{(2)}_{1a,0b}\phi'(\xi^{(2)}_{1a})
                        \phi'(\xi^{(2)}_{0b}),
\]

exactly as in candidate (26). By contrast, \(H^{(2)}_{0a}=\phi(\xi^{(2)}_{0a})\) has zero derivative in every such reverse slot.

One can check that this distinction actually occurs without any experiment. The bottom time-one formal map is

\[
Z^{(1)}_{1a}=G_a+\frac\Delta2\sum_dC_{ad}y_d
                  \phi'(G_d)\tau_{R_1}(\zeta^{(1)}_{0d}),
\]

because \(B^{(2)}_0=0\). Hence the supplied formula for \(A^{(2)}\), evaluated on the attained law, gives

\[
A^{(2)}_{1a,0b}=\frac\Delta2y_b
\left(C_{ab}\mathbb E[\phi'(G_a)\phi'(G_b)]
              +\mathbb E[\phi(G_a)\phi(G_b)]\right).
\]

In particular,

\[
A^{(2)}_{1a,0a}=\frac\Delta2 y_a
\left(\mathbb E[\phi'(G_a)^2]+q_2\right)\ne0.
\]

Thus the diagonal derivative in (26) is nonzero, whereas the corresponding time-zero derivative is zero, despite equality of the two attained activation values. The candidate correctly retains both kinds of degeneracy: equality almost surely between historical and current forward sources, and variance-zero historical reverse sources.

All quantities used in these first-step expectations are finite: \(\phi,\phi',\phi''\) are bounded, the step size is finite, and the only cut evaluations and cut derivatives needed here are at zero. No cap-uniform or later-time response theorem is required for these computations.

## 5. Required repairs, presentation points, and final scope

**Required mathematical repairs: none found.** The independent calculations validate the Laplace and Gaussian integrals, all exchanges actually used, the singular endpoints, the distinction between curvature and full-matrix signs, the actual limiting initial covariance, and the separate exact historical/current \(B^{(3)}\) blocks.

Two presentation refinements would improve precision without changing a formula or a conclusion:

| Candidate location | Presentation point | Suggested wording or clarification |
|---|---|---|
| Lines 390--405, especially 401--402 | \(Y(B_{1,0}+B_{1,1})\) is left multiplication by the label matrix. It is not conjugation of the entire sum, which would be \(Y(B_{1,0}+B_{1,1})Y\). The equations themselves are correct. | Say the sum is **multiplied on the left by the label matrix** and divided by \(\Delta\). The derivative-product subterm is indeed conjugated as \(YPY\). |
| Lines 281--314 | The strict inequalities in (19) enclose the actual covariance parameters. The fixed activation fixes \(q\), and the actual lower covariance is strictly above \(1\). | If an exact attainable range is desired, add \(c\in[c_{\min},q)\), with \(c_{\min}=1+\varepsilon^2F_{q_2}(2-q_2)>1\), and the \(d=1\) restriction described above. The existing bound is already correct. |

The four possible label pairs cause no additional initial-matrix case. If the first label is \(-1\), write the labels as \(y=s(1,\sigma)\), \(s\in\{-1,1\}\). The first readout and the two unweighted first response blocks acquire the factor \(s\), while the row-label multiplication acquires the same factor. Their product and the full matrix are unchanged because \(s^2=1\). The normalization \(y_1=1\) in the candidate therefore covers the two relative-label modes claimed.

Finally, the bootstrap starts with an exactly zero readout and uses prescribed label forcing with coefficient \(\Delta/2\). The contract instead has independent finite-width readout entries of variance \(n^{-2}\), residual forcing, and its stated physical clock. These are not identical finite-width schemes. The candidate expressly makes this distinction in lines 318--323 and 429--434; it is not an unacknowledged gap in the theorem being audited. The contract's readout initialization has no effect on the initial *forward* covariance recursion.

Accordingly, this verdict certifies the centered-Gaussian initialization identities and the first-step algebra of the supplied bootstrap scalar law. It does not certify identification of that law with the full physical training evolution, preservation of signs at later steps, bounds on trained response chains, global existence, or trained-law convergence. The candidate does not claim those conclusions. Its explicit restriction to initialization and the exact first step is mathematically appropriate.
