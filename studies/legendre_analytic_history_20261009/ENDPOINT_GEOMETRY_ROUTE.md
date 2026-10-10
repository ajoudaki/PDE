# Terminal residual-clock geometry of the original Legendre construction

Date: 2026-10-10. Scoped theoretical route. Status: exact scalar spectral
calculation and an actual neural endpoint tensor calculation; no lower bound
for the nonlinear closure's prediction error is proved.

Scientific inputs were `paper/compact.tex`, `paper/compact_legendre.tex`,
`paper/compact_fitting.tex`, the public analytic-source proposition in
`paper/compact_foundations.tex`, and this study's `CLOCK_ANALYSIS.md` and
`SHARPER_UPPER_ROUTE.md`. No other study, archived source, experiment, or paper
edit was used. The required rigorous-mathematics and canonical-notation skills
were applied. This note is not a promotion candidate or an independently
reviewed result.

The conclusion is narrower than a counterexample. The terminal fractional
powers can occur in an admissible neural model, and their leading paired
tensor survives both the sample sum and the instantaneous output Jacobian.
Consequently those two algebraic operations do not furnish a general
cancellation that would establish a fifth-order bound. Passing this tensor
calculation to the original autonomous closure, uniformly when its order and
the width grow, remains unproved here.

## 1. An exact endpoint cross-tail calculation

Fix an interval length \(A>0\). Let \(\Pi_q^A\) be the degree-below-\(q\)
orthogonal Legendre projection on \([0,A]\). For \(\nu\in(0,1/4)\), set

\[
g(\xi)=(A-\xi)^\nu,\qquad h(\xi)=(A-\xi)^{1+\nu}.
\]

Then

\[
\int_0^A[(I-\Pi_q^A)g](\xi)[(I-\Pi_q^A)h](\xi)\,d\xi
=-C_\nu(A)q^{-4-4\nu}(1+o(1)),                         \tag{1}
\]

where the positive constant is

\[
C_\nu(A)=
\frac{2A^{2\nu+2}\Gamma(\nu+1)^2\Gamma(\nu+2)^2
\sin^2(\pi\nu)}{\pi^2(4\nu+4)}.
\]

In particular, the sign does not oscillate and the exponent is less than
five. This is a signed pairing result, rather than a product of norm bounds.

Here is a direct proof. Write

\[
\psi_j^A(\xi)=\sqrt{\frac{2j+1}{A}}P_j(2\xi/A-1),
\qquad
a_j(\eta)=\int_0^A(A-\xi)^\eta\psi_j^A(\xi)\,d\xi.
\]

Rodrigues' formula, integration by parts, and the beta integral give

\[
a_j(\eta)=A^{\eta+1/2}\sqrt{2j+1}
\frac{(-1)^j\Gamma(\eta+1)^2}
{\Gamma(\eta-j+1)\Gamma(\eta+j+2)}.                      \tag{2}
\]

One can first perform the integrations by parts for real \(\eta>j-1\),
where every boundary term vanishes, and then extend the identity to
\(\operatorname{Re}\eta>-1\) by analyticity. Both the integral and the
gamma expression are holomorphic there; reciprocal gamma factors remove
the apparent poles in the denominator.

For a noninteger real \(\eta>-1/2\), the reflection identity rewrites (2) as

\[
a_j(\eta)=
-A^{\eta+1/2}\sqrt{2j+1}
\frac{\Gamma(\eta+1)^2\sin(\pi\eta)}\pi
\frac{\Gamma(j-\eta)}{\Gamma(j+\eta+2)}.
\]

The ratio in this formula is asymptotic to \(j^{-2\eta-2}\). For the
positive exponents needed here this also follows directly, without an
asymptotic expansion of gamma: use

\[
\frac{\Gamma(j-\eta)}{\Gamma(j+\eta+2)}
=\frac1{\Gamma(2\eta+2)}
\int_0^1 t^{j-\eta-1}(1-t)^{2\eta+1}\,dt,
\]

put \(u=j(1-t)\), and apply dominated convergence. For sufficiently large
\(j\), the transformed integrand is bounded by
\(e^{-u/2}u^{2\eta+1}\). Thus

\[
a_j(\eta)=
-\frac{\sqrt2 A^{\eta+1/2}\Gamma(\eta+1)^2\sin(\pi\eta)}\pi
j^{-2\eta-3/2}(1+o(1)).                                  \tag{3}
\]

In (3), the signs for \(\eta=\nu\) and \(\eta=1+\nu\) are opposite.
Orthogonality expresses the left side of (1) as
\(\sum_{j\ge q}a_j(\nu)a_j(1+\nu)\). Comparing the resulting positive
power series with its integral proves (1).

The same leading term holds if both functions are multiplied by a fixed
smooth cutoff equal to one near \(\xi=A\). Indeed the difference from
each uncut function is smooth on the entire closed interval. With

\[
\mathcal D u=-\partial_\xi[\xi(A-\xi)\partial_\xi u],
\qquad \mathcal D\psi_j^A=j(j+1)\psi_j^A,
\]

repeated integration by parts gives, for every integer \(k\ge1\),

\[
|\langle u,\psi_j^A\rangle|
\le[j(j+1)]^{-k}\|\mathcal D^k u\|_{L^2}
\quad(u\in C^\infty([0,A])).
\]

The coefficient \(\xi(A-\xi)\) kills all boundary terms. Smooth changes
therefore alter (1) by a term smaller than every fixed inverse power of
\(q\). This localized version isolates a terminal contribution; it does
not say that arbitrary nonsmooth remainders elsewhere in a history have
the same property.

## 2. The relevant fractional germs in an actual neural model

Take two hidden layers with identity activations. This is within the
paper's activation class: the activations are entire, their first
derivatives are bounded, and their values may be unbounded. Put

\[
U=W^{(1)}\in\mathbb R^{n\times d},\qquad
V=W^{(2)}\in\mathbb R^{n\times n},\qquad
p=V^\top w\in\mathbb R^n.
\]

These are local abbreviations for the paper's existing matrices and
backward carrier. At a normalized input \(v=x/\sqrt d\),

\[
h^{(1)}(v)=Uv,\qquad h^{(2)}(v)=VUv,\qquad
f(v)=\frac{w^\top VUv}{n},\qquad
\delta_a^{(2)}=w,
\]

with \(r_a=f(v_a)-y_a\) and loss \(m^{-1}\sum_a r_a^2\). Define the
input-space residual combination

\[
g=\frac1m\sum_a r_av_a\in\mathbb R^d.
\]

The paper's exact dense gradient flow becomes

\[
\dot U=-2pg^\top,\qquad
\dot V=-\frac2n w(Ug)^\top,\qquad
\dot w=-2VU g.                                           \tag{4}
\]

For this paragraph, take an actual fitted dense trajectory whose residual
has two distinct leading modes

\[
r(t)=c_s e^{-\alpha t}u+c_f e^{-\beta t}z
       +O(e^{-(2\alpha-\eta)t}),                          \tag{5}
\]

where \(u,z\in\mathbb R^m\) are orthonormal,
\(c_s>0\), \(c_f\ne0\), \(\beta=\alpha(1+\nu)\),
\(0<\nu<1/4\), and \(\eta>0\) can be chosen small enough that the
remainder in (5) is smaller than the displayed modes and the clock
corrections used below. Choosing the sign of \(u\) makes \(c_s>0\) without
restricting the residual. Section 3 explains why such trajectories occur
under the Gaussian initialization assumptions.

Let

\[
\rho(t)=\|r(t)\|_2/\sqrt m,\qquad
A_\infty=1+\int_0^\infty\rho(t)\,dt,\qquad
s=A_\infty-\tau(t),\quad
\tau(t)=1+\int_0^t\rho(u)\,du,
\]

and define

\[
k=\frac{c_s}{\sqrt m\alpha},\qquad
v_u=\sum_a u_av_a,\qquad v_z=\sum_a z_av_a.
\]

The vectors \(v_u,v_z\in\mathbb R^d\) are input-space combinations;
\(z\) here is a sample-space eigenvector, not a network preactivation.
All limits carrying a subscript \(\infty\) belong to this dense
trajectory. From (5), with \(x=e^{-\alpha t}\),

\[
\begin{aligned}
s&=kx[1+O(x^{2\nu})],\\
\frac{r_a(t)}{\rho(t)}
 &=\sqrt m\,u_a
   +\sqrt m\,\frac{c_f}{c_s}z_ax^\nu+O(x^{2\nu}).
\end{aligned}                                            \tag{6}
\]

The estimates and all formulas below refer to a fixed finite-width
trajectory. Their leading terms do not require the compressed system.
Since \(w(t)-w_\infty=O(x)\), the backward history at the only compressed
interface has the expansion

\[
b_a(\tau(t))=\frac{r_a(t)}{\rho(t)}w(t)
 =\sqrt m\,u_aw_\infty+B_a s^\nu+O(s^{2\nu}),
\qquad
B_a=\sqrt m\,\frac{c_f}{c_s}k^{-\nu}z_aw_\infty.
                                                               \tag{7}
\]

Integrating the first equation in (4) from \(t\) to infinity yields

\[
U(t)-U_\infty=
\frac{2c_s}{m\alpha}p_\infty v_u^\top x
+\frac{2c_f}{m\beta}p_\infty v_z^\top x^{1+\nu}
+O(x^{2-\eta/\alpha}).                                  \tag{8}
\]

Here the product of a parameter tail and a residual is of second order
in \(x\). Reversion of the first equation of (6) gives
\(x=s/k+O(s^{1+2\nu})\). Consequently

\[
h_a^{(1)}(\tau(t))
=U_\infty v_a+
\frac2{\sqrt m}p_\infty(v_u^\top v_a)s
+H_a s^{1+\nu}+O(s^{1+2\nu}),
\qquad
H_a=\frac{2c_f}{m\beta}k^{-1-\nu}
p_\infty(v_z^\top v_a).                                 \tag{9}
\]

Thus the exponents used in (1) are generated by the neural gradient flow
itself. They are not imported from an unrelated residual ODE. In (7)--(9),
the big-\(O\) statements establish the leading germs; they should not be
silently treated as complete global spectral bounds on the remainders.

## 3. Why the two-mode case is compatible with Gaussian initialization

For a concrete admissible family take \(m=d=2\),
\(v_1^\top v_2=c=1/20\), and labels \(y=\varepsilon(2,1)\), with

\[
Y=\sqrt{5/2}\,\varepsilon
\le\frac{1-c}{2}\,\beta_{\rm act}^{-60}.
\]

Here \(\beta_{\rm act}\) denotes the paper's activation envelope, to
distinguish it from the fast decay rate \(\beta\). Identity activations
have \(Q^{(2)}=Q^{(0)}\), whose eigenvalues are \(1-c\) and \(1+c\),
so \(\gamma=1-c>0\). The labels are nonzero in both population
eigendirections. One may choose \(\varepsilon\) still smaller than the
displayed cap; this defines one fixed admissible problem.

To see the actual residual generator, define

\[
M(t)=\frac{\|p(t)\|_2^2}{n}I_d+
\frac1n U(t)^\top
\left[V(t)^\top V(t)+\frac{\|w(t)\|_2^2}{n}I_n\right]U(t).
\]

Differentiating the effective linear predictor
\(U^\top V^\top w/n\) using (4) gives exactly

\[
\dot r=-K(t)r,
\qquad
K_{ab}(t)=\frac2m v_a^\top M(t)v_b.                        \tag{10}
\]

At initialization, \(w=0\), and hence

\[
K_{ab}(0)=\frac2{mn}h_{0,a}^{(2)\top}h_{0,b}^{(2)}
\xrightarrow{\mathbb P}Q^{(0)}_{ab}
\quad(m=2).
\]

The real fitting estimates give \(\|w\|/\sqrt n=O(\varepsilon)\),
\(\|U-U_0\|_F/\sqrt n=O(\varepsilon^2)\), and
\(\|V-V_0\|_F=O(\varepsilon^2)\), with constants independent of width
on the initialization event. Substitution in the displayed formula for
\(M\) proves

\[
\sup_{t\ge0}\|K(t)-K(0)\|_{\rm op}=O(\varepsilon^2).       \tag{11}
\]

For sufficiently small fixed \(\varepsilon>0\), (10)--(11) give an
order-one residual decay rate \(a>0\), and the limiting eigenvalues
\(\alpha<\beta\) of \(K_\infty\) obey, with probability tending to one,

\[
\alpha=1-c+O(\varepsilon^2)+o_{\mathbb P}(1),\qquad
\beta=1+c+O(\varepsilon^2)+o_{\mathbb P}(1),
\qquad 0<\beta/\alpha-1<1/4.                              \tag{12}
\]

The parameter tails from (4), followed by the formula for \(M\), improve
the coefficient convergence to
\(\|K(t)-K_\infty\|=O(\varepsilon^2e^{-at})\). The constants are
width independent. Since \(K(t)\to K_\infty\), for every sufficiently
small \(\eta>0\) the residual additionally satisfies
\(\|r(t)\|=O(e^{-(\alpha-\eta)t})\). Integrating (4) with this
improved bound, and again substituting in \(M\), gives the analogous
improved bound on \(K(t)-K_\infty\).

For either normalized eigenvector \(e_j\) of \(K_\infty\), with
eigenvalue \(\lambda_j\in\{\alpha,\beta\}\), variation of constants
then gives

\[
\frac d{dt}\left[e^{\lambda_jt}e_j^\top r(t)\right]
=-e^{\lambda_jt}e_j^\top[K(t)-K_\infty]r(t).               \tag{13}
\]

The right side is integrable since \(\beta<2\alpha\). Its tail has
order \(e^{-(2\alpha-\eta-\lambda_j)t}\), giving (5), after decreasing
and renaming \(\eta\). Taking \(\varepsilon\) small and the initial
Gram sufficiently close to its limit also makes the integrated correction
in (13) \(O(\varepsilon^3)\): (11) supplies a uniform \(a\) with
\(2a>\beta\). The initial modal coefficients are the nonzero
projections of \(-\varepsilon(2,1)\), up to a perturbation tending to
zero with \(\varepsilon\) and the initial-Gram error. Therefore both
limiting mode amplitudes remain nonzero.

This realizes (5)--(9) on events whose probability tends to one for a
fixed admissible neural problem. It does not yet prove the required
Legendre coefficient estimates for all remainders uniformly in width, or
any statement about the distinct compressed trajectory.

## 4. The sample sum and the output Jacobian do not cancel the tensor

The coefficients in (7) and (9) satisfy the exact identity

\[
\sum_a B_aH_a^\top
=T_\nu\,w_\infty p_\infty^\top,
\qquad
T_\nu=\frac{2c_f^2}{\sqrt m\,c_s\beta}
k^{-1-2\nu}\|v_z\|_2^2>0.                               \tag{14}
\]

Indeed the only sample contraction is

\[
\sum_a z_a(v_z^\top v_a)=\|v_z\|_2^2.
\]

For the two linearly independent inputs above this squared norm is
positive. Also \(w_\infty\ne0\) and \(p_\infty\ne0\), because the
fitted labels are nonzero. Thus (14) is a nonzero matrix.

Define the matrix with the network's normalization

\[
S=\frac1n w_\infty p_\infty^\top.
\]

For the dense histories alone, localize the terms \(B_as^\nu\) and
\(H_as^{1+\nu}\) with a smooth cutoff near the terminal endpoint. Their
contribution to the signed defect primitive

\[
\frac2{mn}\sum_a\int_0^{A_\infty}
[(I-\Pi_q^{A_\infty})b_a]
[(I-\Pi_q^{A_\infty})h_a^{(1)}]^\top\,d\xi
\]

is, by (1) and (14),

\[
-\frac{2T_\nu}{m}C_\nu(A_\infty)
q^{-4-4\nu}S(1+o(1)).                                   \tag{15}
\]

Equation (15) identifies this pair of localized terms exactly. It is not
an assertion that all other pairings in the full histories have already
been bounded or cannot affect a full-primitive asymptotic.

The output derivative with respect to \(V\), at the fitted parameters
and at an arbitrary input \(v\), acts on \(S\) as

\[
D_V f_\infty(v)[S]
=\frac1n w_\infty^\top S U_\infty v
=\frac{\|w_\infty\|_2^2}{n}f_\infty(v).                  \tag{16}
\]

In particular, at either training input the right side is nonzero for
the selected labels. The factor \(\|w_\infty\|^2/n\) is not forced to
vanish as width grows: \(|y_a|\le(\|w_\infty\|/\sqrt n)
(\|h_{\infty,a}^{(2)}\|/\sqrt n)\), and the second factor is uniformly
bounded on the fitting event.

Equations (14) and (16) answer a concrete geometry question. Neither the
sample sum nor projection by the current output Jacobian annihilates this
leading terminal tensor. The claim that gradient structure always cancels
the terminal term at either of those algebraic steps is false.

## 5. Why this is still not a prediction-error counterexample

For the actual order-\(q\) closure, the primitive formula uses that
closure's own histories and its own clock. Equations (5)--(16) used dense
histories. Replacing one by the other is a substantive missing step,
especially near the fitted clock endpoint.

There are four additional issues.

1. The complete histories include the prescribed interior join and all
   higher terminal terms. To obtain a full primitive asymptotic, one must
   control their signed pairings and remainders uniformly in the width and
   the current endpoint. The localized contribution (15) alone is not a
   lower bound for the complete primitive.

2. Even a proved lower bound for the complete parameter primitive would
   not imply a lower bound for the actual output error. The gradient flow
   responds to the forcing over time. Formula (16) concerns its
   instantaneous output image, not the solution of this response equation.

3. In this identity-activation example the two inputs span the input
   space. Both fitted predictors therefore agree on the entire sphere.
   Any output lower bound would have to use an earlier time that may tend
   to infinity with \(q\), and cannot use the fitted output itself.

4. The closure's endpoint residual equation need not be an ordinary
   linear residual equation. Its limiting forward projection error and
   projected backward memory appear in the physical defect. Terms
   proportional to \(\widehat\rho\) can retain a dependence on the
   normalized residual direction. A uniform comparison with the dense
   two-mode expansion must be proved, not assumed.

One formal scale calculation explains why the finite-time response remains
relevant. Suppose a future proof established a uniform transition formula

\[
R_q(A_\infty-s)=q^{-4-4\nu}F(q^2s)+o(q^{-4-4\nu}).        \tag{17}
\]

When \(s\asymp q^{-2}\), the residual clock has
\(\dot s=-\rho\asymp-s\), so differentiating the leading term in (17)
would give a physical forcing of order \(q^{-4-4\nu}\), with no
additional factor \(q^{-2}\). This transition occupies physical time of
order one around a time proportional to \(\log q\). It could therefore
create a transient training-output error even though the fitted error
vanishes. Formula (17), its differentiated remainder, and the nonzero
response are not proved in this note.

The bounded outcome is consequently an obstruction to a particular
cancellation shortcut, and a concrete test case for the unfinished upper
proof. It is not a disproof of sufficiency at
\(q=n^{1/10+o(1)}\), and no such sufficiency theorem is claimed here.
