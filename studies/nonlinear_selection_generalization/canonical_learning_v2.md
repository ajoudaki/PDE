##### C.4.10.4. Nonlinear approximation, noisy samples and a positive stop

Use the common source neighborhood, constants \(L,C_g,\mathcal K,\rho_s\)
and episode \(T_c>0\) from C.4.10.2, with label bound \(Y_0=1\). Put
\[
 C=\sqrt{10},\quad M_b=2+\sqrt{10},\quad a_b=M_b+1,\quad c_b=C+1,
 \quad B_0=C+1,
\]
\[
 L_0=\sqrt{1+C^2(1+M_b^2)},\quad
 C_d=C_g(1+4L/\sqrt{k}),\quad V=2(c_b+1)L,
 \quad k=\lambda_{\min}(M_\dagger).
 \tag{NGL1}
\]
Thus \(\|g_\dagger(u)\|\le L_0\), while \(\|g_\theta(u)\|\le L\)
and \(|f_\theta(u)|\le c_b\) in the common unit endpoint ball. The constants
\(\lambda_N,\lambda_{H,N}>0\) refer to the finite matrices in C.4.10.3.
Every constant in this subsection is determined by the reference and declared
class parameters. In particular no unknown changed-law solution enters them.

**Population approximation theorem.** Let \(q_N\) truncate (NG5) at index
\(N\), and use either the actual coefficient tail
\(a_N=\sum_{k>N}(|a_k|+|b_k|)\) or its class bound
\(a_N=R/(2N+3)^s\). For a class with declared finite cap \(N\), take
\(a_N=0\). If
\[
 0<T\le T_c,\qquad C_d^2VT\le\lambda_N/8,
 \qquad
 \mathfrak A_N(T)=2(1+2L_0^2/\lambda_N)(a_N+LVT)^2,
 \tag{NGL2}
\]
then the whole-circle reconstruction \(P_\nu\) of the actual constrained
selection satisfies, for \(0\le\tau\le T\),
\[
 \mathcal E_\nu(P_\nu(\tau))
 \le e^{-\lambda_N\tau/2}\mathcal E_\nu(F_*)
       +\mathfrak A_N(T)(1-e^{-\lambda_N\tau/2}).
 \tag{NGL3}
\]
The initial excess risk is at most \(B_0^2\). The floor in (NGL2) bounds
omitted target modes and movement away from the endpoint analysis space. It
is not defined by a trained risk. For fixed \(N\), longer training within
this admitted interval contracts toward this floor. Increasing \(N\) decreases
the target tail but may decrease \(\lambda_N\) and the admitted duration;
there is no assertion that \(a_N^2/\lambda_N\to0\), or of universal
consistency.

To prove the theorem, abbreviate
\(r_\tau=f_{\theta_\nu(\tau)}-q\), \(E(\tau)=\|r_\tau\|_p^2\), and
\[
 T_{\theta,p}r=\int r(u)\Pi_\theta g_\theta(u)p(u)\,d\rho(u).
\]
The scalar gradient rule and bounded Bochner integrands give the exact identity
\[
 E'(\tau)=-4\|T_{\theta_\nu(\tau),p}r_\tau\|^2.
 \tag{NGL4}
\]
Centered label noise has zero population force. The velocity is bounded by
\(V\), so \(\|\theta_\nu(\tau)-\theta_\dagger\|\le V\tau\).
The state comparison in C.4.10.2 and
\(d\sqrt{\log(e/d)}\le\sqrt d\) for \(0\le d\le1\) imply
\[
 \|f_{\theta_\nu(\tau)}-F_*\|_\infty\le LV\tau,
 \qquad
 \|T_{\theta_\nu(\tau),p}-T_p\|\le C_d\sqrt{V\tau}.
 \tag{NGL5}
\]
Here \(T_p=T_{\theta_\dagger,p}\). Let \(P_N\) denote orthogonal
projection onto \(E_N\) in the odd subspace of \(L^2(p\rho)\).
Because \(F_*-q_N\in E_N\),
\[
 \|(I-P_N)r_\tau\|_p\le a_N+LV\tau=:b(\tau).
 \tag{NGL6}
\]
For vectors in any Hilbert space,
\(\|x+y\|^2\ge\frac12\|x\|^2-\|y\|^2\), as follows by completing
the square \(\frac12\|x+2y\|^2\). Apply this first to
\(T_{\theta,p}r=T_pr+(T_{\theta,p}-T_p)r\), then to
\(T_pr=T_pP_Nr+T_p(I-P_N)r\). The operator norm of \(T_p\) is at
most \(L_0\), and its finite-space conditioning gives
\[
 \|T_{\theta,p}r_\tau\|^2
 \ge(\lambda_N/4-C_d^2V\tau)E(\tau)
                -(\lambda_N/4+L_0^2/2)b(\tau)^2.
 \tag{NGL7}
\]
Orthogonality is used in the function space, not between its images under
\(T_p\); thus possible cancellation between modes has been bounded. Under
(NGL2), (NGL4) yields
\[
 E'\le-\lambda_NE/2+(\lambda_N+2L_0^2)(a_N+LVT)^2.
\]
Multiplication by \(e^{\lambda_N\tau/2}\) and integration proves (NGL3).
The training field in this argument always uses the current residual, current
features and current anchor projection.

**Sampling theorem with centered noise separated.** For positive failure
allowances \(\delta_I,\delta_\xi\) with sum less than one, define
\[
 \eta_m={2TL\over\sqrt m}
       \left({B_0\over\sqrt{\delta_I}}+
                            {\sigma\over\sqrt{\delta_\xi}}\right),
\]
\[
 \mathcal O_T(\eta)=e\exp\left[-
              \left(\sqrt{\log(e/\eta)}-\mathcal KT/2\right)^2\right].
 \tag{NGL8}
\]
Set \(\mathcal O_T(0)=0\), and require for \(\eta_m>0\) that
\(\sqrt{\log(e/\eta_m)}>1+\mathcal KT/2\). With probability at least
\(1-\delta_I-\delta_\xi\) over the added observations, simultaneously
for \(0\le\tau\le T\),
\[
 \|\theta_{\widehat\nu_m}(\tau)-\theta_\nu(\tau)\|
           \le\mathcal O_T(\eta_m),\qquad
 \|P_{\widehat\nu_m}(\tau)-P_\nu(\tau)\|_\infty
           \le L\mathcal O_T(\eta_m),
 \tag{NGL9}
\]
and therefore
\[
 \sqrt{\mathcal E_\nu(P_{\widehat\nu_m}(\tau))}
 \le\sqrt{e^{-\lambda_N\tau/2}\mathcal E_\nu(F_*)
             +\mathfrak A_N(T)(1-e^{-\lambda_N\tau/2})}
          +L\mathcal O_T(\eta_m).
 \tag{NGL10}
\]
When \(\sigma=0\), omit the noise term and allowance. For fixed episode and
confidence, the statistical error tends to zero as
\(m^{-1/2}\exp(O(\sqrt{\log m}))\). The two separate contributions in
(NGL8) display input sampling and centered label noise.

For proof, evaluate all random forcing on the deterministic population path.
Put \(d_\tau(u)=\Pi_{\theta_\nu(\tau)}g_{\theta_\nu(\tau)}(u)\) and
\[
 I_m(\tau)={1\over m}\sum_i r_\tau(X_i)d_\tau(X_i)
                   -\mathbb E[r_\tau(X)d_\tau(X)],\qquad
 N_m(\tau)={1\over m}\sum_i\xi_i d_\tau(X_i).
\]
Independence and centering eliminate off-diagonal inner products. Since
\(E(\tau)\le E(0)\le B_0^2\),
\[
 \mathbb E\|I_m(\tau)\|^2\le L^2B_0^2/m,\qquad
 \mathbb E[\|N_m(\tau)\|^2\mid X_1,\ldots,X_m]\le L^2\sigma^2/m.
 \tag{NGL11}
\]
The second assertion uses conditional independence of labels in iid pairs,
not independence between empirical trained features and their own labels.
For \(Z_I=2\int_0^T\|I_m\|\,d\tau\) and
\(Z_\xi=2\int_0^T\|N_m\|\,d\tau\), Cauchy–Schwarz in time and Tonelli
give \(\mathbb EZ_I^2\le4T^2L^2B_0^2/m\) and
\(\mathbb EZ_\xi^2\le4T^2L^2\sigma^2/m\). Markov and a union bound
give \(Z_I+Z_\xi\le\eta_m\) with the declared probability.

Subtract the two constrained integral equations by first comparing states
under the empirical law. The population state supplies the source tails for
the one-reference bound in C.4.10.2. The remaining law difference at this
fixed population state is exactly \(-2I_m+2N_m\). Thus, with
\(D(\tau)=\|\theta_{\widehat\nu_m}(\tau)-\theta_\nu(\tau)\|\) and
\(\omega(d)=d\sqrt{\log(e/d)}\),
\[
 D(\tau)\le\eta_m+\mathcal K\int_0^\tau\omega(D(s))\,ds.
 \tag{NGL12}
\]
For the scalar comparison solution, differentiating
\(\sqrt{\log(e/Z)}\) gives derivative \(-\mathcal K/2\).
Its explicit solution is (NGL8) with \(T\) replaced by \(\tau\).
The branch condition keeps it below one, so a first-exit comparison applies.
At zero forcing decrease positive upper errors to zero; equivalently the
Osgood integral diverges at zero. This proves (NGL9). The risk triangle
inequality proves (NGL10); the same event also gives the useful additive bound
\[
 |\mathcal E_\nu(P_{\widehat\nu_m}(\tau))-
       \mathcal E_\nu(P_\nu(\tau))|
       \le2(c_b+1)L\mathcal O_T(\eta_m).
 \tag{NGL13}
\]

**Robust strict learning and paired second-hidden motion.** Fix finite
\(N\ge0\), \(R>0\), \(s\ge1\), and \(D\ge0\). Inside (NG5) take
\[
 a=R/4,\qquad v=a(\cos\alpha+\sin\alpha)+w(\alpha),\qquad
 \sum_{k=0}^N(2k+1)^s(|w_{c,k}|+|w_{s,k}|)\le a/4.
 \tag{NGL14}
\]
Here the target has coefficient cap \(N\): explicitly,
\[
 w(\alpha)=\sum_{k=0}^N\{w_{c,k}\cos((2k+1)\alpha)
                         +w_{s,k}\sin((2k+1)\alpha)\}.
\]
All coefficients above \(N\) are zero.
This has nonempty relative interior in every fixed finite coefficient space,
with budget at most \(9R/16<R\). Retain every \(p\in\mathcal P_D\) and
every noise law (NG6). Its initial excess risk is uniformly bounded below by
\[
 e_*={a^2\over2}\left(\sqrt{3/8}-1/4\right)^2>0.
 \tag{NGL15}
\]
Indeed \(F_*-q_0\) is antisymmetric under the coordinate swap, while
\(\psi=h(\cos\alpha+\sin\alpha)\) is symmetric. Their inner product in
\(L^2(\rho)\) is zero, and
\(\|\psi\|_\rho^2=\int\sin^4(2\alpha)(1+\sin2\alpha)\,d\rho=3/8\).
The odd sine term integrates to zero; the remaining identity follows by
expanding \(\sin^4\). Since \(\|hw\|_\rho\le a/4\), the reverse
triangle inequality and \(p\ge1/2\) prove (NGL15). This uses full-circle
mass and an independently specified symmetric target component.

Here are explicit common stopping and hidden-observation constants. Define
\[
 \gamma=\lambda_{H,N}e_*,\quad G_0=\sqrt2L_0,\quad
 B_\beta=G_0L_0B_0/k,\quad S=B_0+\sqrt2B_\beta,\quad
 B_2=2B_0^2+B_\beta^2,
\]
\[
 C_V=2L^2+2B_0C_d,\qquad A_H=SC_gV+L_0B_0C_V,
\]
\[
 T={1\over2}\min\left\{T_c,\ {\lambda_N\over8C_d^2V},\
 {\sqrt{e_*/[4(1+2L_0^2/\lambda_N)]}\over LV},\
 {\gamma^2\over A_H^2V}\right\}>0,
\]
\[
 a_*={e_*\over2}(1-e^{-\lambda_NT/2}),\qquad
 j_*={\gamma^2T^2\over3C^2B_2}>0.
 \tag{NGL16}
\]
This deterministic stop uses only class and reference information and is
chosen before training. Its physical value is \(T/\varepsilon\). Because
\(a_N=0\), it ensures \(\mathfrak A_N(T)\le e_*/2\), so (NGL3) gives
\(\mathcal E_\nu(F_*)-\mathcal E_\nu(P_\nu(T))\ge a_*\).

The paired upper-hidden observable is
\[
 J_2(\theta)={1\over3}\left[
  \int\|H^2_\theta(u)-H^2_\dagger(u)\|_2^2\,d\rho(u)
   +\sum_{a=1}^2\|H^2_\theta(e_a)-H^2_\dagger(e_a)\|_2^2\right].
 \tag{NGL17}
\]
Both states use the same initialized carrier. The observation measure here
is uniform circle plus the two anchors, independently of the unknown test
density. The lower bound below is for their sum; it does not assert a lower
bound for its circle-only part.

To prove finite hidden displacement, put \(r_0=F_*-q\) and
\[
 u_0=\int r_0g_\dagger p\,d\rho,\quad
 \beta=M_\dagger^{-1}G_\dagger^*u_0,\quad d_0=\Pi_\dagger u_0.
\]
The hidden block consists of the first-row and middle-increment components.
Since \(r_0\in E_N\), \(\|(d_0)_H\|^2\ge\gamma\), while
\(\|r_0\|_p\le B_0\), \(|\beta|\le B_\beta\), and
\(\|d_0\|\le L_0B_0\). Keep \(r_0,\beta,c_\dagger\) fixed only in
the scalar observation
\[
 O(\theta)=\int r_0(u)\langle c_\dagger,H^2_\theta(u)\rangle p(u)\,d\rho
       -\sum_a\beta_a\langle c_\dagger,H^2_\theta(e_a)\rangle.
 \tag{NGL18}
\]
Its endpoint gradient is \(o_\dagger=((d_0)_H,0)\), and the actual
constrained velocity at the endpoint is \(-2d_0\). Hence
\(O'(0)=-2\|(d_0)_H\|^2\le-2\gamma\).

This derivative remains negative on the declared finite episode. For raw
distance \(d=\|\theta-\theta_\dagger\|\le\rho_s\), the fixed-readout
hidden gradient is the hidden part of the prediction gradient at the
auxiliary state \((w,K,c_\dagger)\). This auxiliary state is in the unit
endpoint ball. Apply the one-reference gradient estimate against the
endpoint, discard its readout component, and use \(\omega(d)\le\sqrt d\).
Integrating absolute contrast coefficients gives
\[
 \|o_\theta-o_\dagger\|\le SC_g\sqrt d.
\]
Subtracting residuals and projected gradients in the actual velocity gives
\(\|V_\nu(\theta)-V_\nu(\theta_\dagger)\|\le C_V\sqrt d\).
Therefore
\[
 |O'(\tau)-O'(0)|\le A_H\sqrt{V\tau}\le\gamma,
                         \qquad 0\le\tau\le T.
\]
Integrating yields \(|O(\theta_\nu(\tau))-O(\theta_\dagger)|\ge\gamma\tau\).
Finally Cauchy–Schwarz in the upper population and in the direct sum of the
circle and two anchor observations, using
\(\int r_0^2p^2\,d\rho\le2B_0^2\), proves
\[
 |O(\theta)-O(\theta_\dagger)|^2\le3C^2B_2J_2(\theta),\qquad
 J_2(\theta_\nu(\tau))\ge{\gamma^2\tau^2\over3C^2B_2}.
 \tag{NGL19}
\]
This establishes \(J_2(\theta_\nu(T))\ge j_*\) for evolving second-hidden
activations, rather than inferring it from parameter motion or an initial
derivative alone.

**An explicit sample threshold and the actual GF conclusion.** Let
\(0<\delta<1\), take \(\delta_I=\delta_\xi=\delta/2\) when \(\sigma>0\),
and take only \(\delta_I=\delta\) when \(\sigma=0\). Put
\[
 H_L=\sqrt{1+a_b^2},\quad
 d_* =\min\{1/2,\ a_*/[8(c_b+1)L],\ j_*/[16H_L]\},
\]
\[
 C_{\rm sample}=2TL\left({B_0\over\sqrt{\delta_I}}
                       +{\sigma\over\sqrt{\delta_\xi}}\right),\quad
 \eta_* = e\exp[-(\sqrt{\log(e/d_*)}+\mathcal KT/2)^2],
\]
\[
 m_* =\max\{1,\lceil(C_{\rm sample}/\eta_*)^2\rceil\}.
 \tag{NGL20}
\]
The noise summand is omitted in the noiseless case. For \(m\ge m_*\),
inverting (NGL8) gives \(\mathcal O_T(\eta_m)\le d_*\); since
\(d_*\le1/2\), the strict branch condition is satisfied.
Factor subtraction gives
\(\sup_u\|H^2_\theta(u)-H^2_{\bar\theta}(u)\|_2\le H_L\|\theta-\bar\theta\|\).
Each displacement from the endpoint has norm at most two, so subtracting
squared norms in (NGL17) gives
\(|J_2(\theta)-J_2(\bar\theta)|\le4H_L\|\theta-\bar\theta\|\).
Together with (NGL13), this proves, with sample probability at least
\(1-\delta\),
\[
 \mathcal E_\nu(F_*)-\mathcal E_\nu(P_{\widehat\nu_m}(T))\ge3a_*/4,
 \qquad J_2(\theta_{\widehat\nu_m}(T))\ge3j_*/4.
 \tag{NGL21}
\]

For actual finite GF, train the empirical mixture and reference on the same
initial arrays, including the Gaussian readout, and evaluate both at the same
physical time \(T/\varepsilon\). Define
\[
 J_{2,n,\varepsilon}={1\over3n}\left[
  \int\|h^2_{n,\widehat\mu_{\varepsilon,m}}(T/\varepsilon,\sqrt2u)
           -h^2_{n,\nu_*}(T/\varepsilon,\sqrt2u)\|_2^2\,d\rho(u)
\right.
\left.\hspace{5mm}+\sum_{a=1}^2
  \|h^2_{n,\widehat\mu_{\varepsilon,m}}(T/\varepsilon,\sqrt2e_a)
           -h^2_{n,\nu_*}(T/\varepsilon,\sqrt2e_a)\|_2^2\right].
 \tag{NGL22}
\]
For every fixed law in (NGL14), every \(m\ge m_*\), and the constants
above, the bounded-law capture and finite-GF theorem in C.4.10.2 imply
\[
 \liminf_{\varepsilon\downarrow0}\liminf_{n\to\infty}
 \Pr_{\rm samples,init}\left\{
  \mathcal E_\nu(F_*)-
     \mathcal E_\nu(f_{n,\widehat\mu_{\varepsilon,m}}(T/\varepsilon))
       \ge a_*/2,\quad J_{2,n,\varepsilon}\ge j_*/2\right\}
 \ge1-\delta.
 \tag{NGL23}
\]
The same conclusion holds with the paired finite reference risk in place
of \(\mathcal E_\nu(F_*)\).

Indeed, for each fixed realized sample and positive \(\varepsilon\), width
first gives its deterministic population-law flow, including joint paired
observations. Sending \(\varepsilon\) to zero then gives its constrained
selection at \(T\); the reference converges to \(\theta_\dagger\).
The bounds hold for every empirical law, including repeated observations.
Conditional failure probabilities are bounded by one, so dominated convergence
integrates them over samples. On (NGL21)'s sample event, the spare margins
allow both transfers. Whole-circle uniform prediction convergence implies
excess-risk convergence, and the same-array hidden limits give (NGL22).
This proves (NGL23) without interchanging the order of limits.

The constants and sample threshold are uniform on the robust class; no width
threshold uniform over that class is asserted. The positive margins are
independent of \(\varepsilon\) and \(n\). With sample size increasing after
the width and contamination limits, the probability tends to one, since
\(\delta\) can be made arbitrarily small. More data reduces the statistical
term; more training within the declared episode reduces the population bound
toward its explicit floor. The result proves a finite nonlinear learning
episode for this class, not arbitrary-accuracy fitting, an all-time endpoint,
or superiority over another architecture or training method.
