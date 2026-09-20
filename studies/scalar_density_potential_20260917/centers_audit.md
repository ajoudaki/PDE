# Cross-audit: antipodal delay and class-center energy bounds

Scope: the frozen Sections 1–5 of `centers_counter.md`, the exact model supplied in the scoped assignment, and the class-center identities supplied by the supervisor. Section 6 of that route is outside this audit. No other research sources, experiments, or external results were used. This is an internal cross-audit, not a promotion review.

Verdict: the mathematical claims in the frozen sections reconstruct correctly. The near-antipodal family proves a diverging delay despite a fixed positive initial descent and a positive definite full initial tangent Gram matrix. It does not prove nonconvergence or subexponential convergence at any fixed admissible dataset. The supplied center-energy bridges are valid and admit a modest sharpening, but they are progress bounds rather than fitting theorems.

## 1. Constants and the exact initial state

Keep the assignment's \(\nu,\tau,\eta,M_0\), with \(M_0>0\). Write

\[
\beta_1^2=\mathbb E b_1^2=\frac{\nu}{\nu+\eta}<1,
\qquad
\beta_2^2=\mathbb E b^2=\frac{\tau}{\tau+\eta}<1.
\]

All expectations defining these constants are population expectations. The constants in the route are

\[
A=M_0\frac{\nu}{\sqrt{\nu+\eta}},\quad
K=\frac{M_0}{\sqrt{\nu+\eta}},\quad
R=\|\tanh(bA)\|_2>0,\quad
s_0=\frac{R^2}{16},
\]

\[
C=(M_0+1)(\sqrt2+1),\qquad
\varepsilon_0=\min\left\{\frac\pi4,\frac1C,\frac{R}{4K}\right\}>0.
\tag{1}
\]

For the family under audit, \(p=(3/8,1/8,1/2)\), equivalently \(q=3/4\), and

\[
v_1=e_1,\quad v_2=(-\cos\varepsilon,-\sin\varepsilon),\quad
v_3=(\sin\varepsilon,\cos\varepsilon),\qquad
0<\varepsilon<\varepsilon_0.
\tag{2}
\]

The pairwise determinants are nonzero: their magnitudes are \(\sin\varepsilon\), \(\cos\varepsilon\), and \(\cos2\varepsilon\). Positive and negative class masses are both \(1/2\).

With \(\theta=(\sin(\varepsilon/2),-\cos(\varepsilon/2))\), the signed margins are

\[
\theta\cdot v_1=\theta\cdot v_2=\sin(\varepsilon/2)>0,
\qquad -\theta\cdot v_3=\cos(3\varepsilon/2)>0.
\]

Thus the stated homogeneous linear separability is correct.

To avoid colliding with the class-center notation below, call the route's Gaussian correlation function \(\mathfrak a\):

\[
\mathfrak a(\rho)=
\frac{\mathbb E[\tanh G\,\tanh(\rho G+\sqrt{1-\rho^2}U)]}
{\sqrt{\nu+\eta}}.
\]

For \(|\rho|<1\), differentiating under the integral on compact subintervals and integrating by parts in the two independent Gaussians gives

\[
\mathfrak a'(\rho)=
\frac{\mathbb E[\operatorname{sech}^2G\,
\operatorname{sech}^2(\rho G+\sqrt{1-\rho^2}U)]}
{\sqrt{\nu+\eta}}\in\left(0,\frac1{\sqrt{\nu+\eta}}\right].
\tag{3}
\]

In detail, differentiating the second tanh produces \(G-\rho U/\sqrt{1-\rho^2}\). The second-derivative terms from the two integrations by parts cancel. Bounded tanh derivatives and Gaussian moments justify both operations. Oddness, continuity up to the endpoints, and \(\mathfrak a(1)=\nu/\sqrt{\nu+\eta}\) follow directly.

Set

\[
B=M_0\mathfrak a(\cos\varepsilon),\qquad
D=M_0\mathfrak a(\sin\varepsilon).
\]

Then \(0<D<B<A\), the initial centers are \((A,-B,D)\), and the exact initial readout velocity is

\[
\dot c_0=\tfrac34H_A-\tfrac14H_B-H_D,
\qquad H_s(b)=\tanh(bs).
\tag{4}
\]

At initialization all \(d_i=0\), so the other two parameter velocities vanish.

## 2. Uniform positive initial descent and the full initial Gram

For \(b\ge0\), \(0\le H_B(b)\le H_A(b)\), hence

\[
\tfrac34H_A(b)-\tfrac14H_B(b)\ge\tfrac12H_A(b).
\]

Oddness gives the corresponding absolute-value estimate on \(b<0\). Also (3) gives

\[
\|H_D\|_2\le D\beta_2
\le K\sin\varepsilon\le K\varepsilon.
\]

The reverse triangle inequality in (4) therefore yields

\[
\|\dot c_0\|_2\ge R/2-K\varepsilon\ge R/4,
\qquad -\dot L(0)\ge R^2/16=s_0.
\tag{5}
\]

There is no missing weight or factor of two in this calculation.

For completeness, let \(Q(s,t)=\mathbb E[H_sH_t]\) for positive arguments. The full initial readout Gram is

\[
G_0=
\begin{pmatrix}
Q(A,A)&-Q(A,B)&Q(A,D)\\
-Q(A,B)&Q(B,B)&-Q(B,D)\\
Q(A,D)&-Q(B,D)&Q(D,D)
\end{pmatrix}.
\tag{6}
\]

It is also the full initial tangent Gram for the output map: derivatives of \(f_i\) with respect to \(M\) and \(w\) contain \(d_i\), which vanish at \(c_0=0\). Thus

\[
\dot f(0)=-2G_0P r(0),\qquad
-\dot L(0)=4y^TPG_0Py=\|\dot c_0\|_2^2.
\tag{7}
\]

For a symmetric weighted convention the matrix is \(P^{1/2}G_0P^{1/2}\); multiplying by the positive diagonal weights preserves positive definiteness.

To check that definiteness directly, suppose \(u_1H_A-u_2H_B+u_3H_D=0\) in \(L^2\). The law of \(b\) has positive density on an interval containing zero, so continuity makes the identity hold throughout that interval. The coefficients of \(b,b^3,b^5\), respectively, give the Vandermonde system with nodes \(A^2,B^2,D^2\) and nonzero column factors \(A,-B,D\). Its determinant is nonzero. Hence \(u=0\), proving \(G_0\succ0\).

Consequently \(c_* =\sum_j(G_0^{-1}y)_jH_j^0\) is a finite-norm exact interpolant with \(w=w_0\), \(M=M_0\). This establishes expressivity at each fixed positive \(\varepsilon\), not bounded conditioning uniformly as \(\varepsilon\downarrow0\) and not convergence of the trained trajectory. No asymptotic eigenvalue claim from the separately appended Section 6 is assessed here.

## 3. Population energy and the first-moment estimates

Let \(\Delta_t=1-L(t)\). The exact dissipation identity and \(c_0=0\), \(\|w_0\|_2=\sqrt2\) imply

\[
\int_0^t\left(\|\dot w_s\|_2^2+\|\dot c_s\|_2^2+|\dot M_s|^2\right)ds
=\Delta_t\le1.
\tag{8}
\]

Bochner integration and Cauchy–Schwarz in time give the sharper component bounds

\[
\|c_t\|_2\le\sqrt{t\Delta_t},\quad
|M_t|\le M_0+\sqrt{t\Delta_t},\quad
\|w_t\|_2\le\sqrt2+\sqrt{t\Delta_t}.
\tag{9}
\]

Replacing \(\Delta_t\) by one yields exactly the bounds used in the route. These estimates require only the population energy, not a pointwise bound on \(w(g)\) or \(c(Z)\).

The first hidden-layer first-moment step is valid because oddness and Lipschitz continuity give

\[
|a_1+a_2|
\le |v_1+v_2|\,\mathbb E_1[|b_1||w|]
\le |v_1+v_2|\,\beta_1\|w\|_2.
\tag{10}
\]

No independence between \(b_1\) and \(w\) is required for the final Cauchy–Schwarz inequality. At the readout,

\[
|H_1+H_2|\le |bM|\,|a_1+a_2|,
\qquad
|f_1+f_2|\le\|c\|_2\beta_2|M|\,|a_1+a_2|.
\tag{11}
\]

Again, no independence between \(c\) and \(b\) is used. Since \(|v_1+v_2|=2\sin(\varepsilon/2)\le\varepsilon\) and \(\beta_1\beta_2<1\), (9)–(11) imply

\[
|f_1(t)+f_2(t)|
\le\varepsilon\sqrt t\,(M_0+\sqrt t)(\sqrt2+\sqrt t).
\tag{12}
\]

The finite-width temptation to assume bounded maximum neuron coordinates is absent; all bounds close in the correct population norms.

Weighted Cauchy–Schwarz, with \(1/p_1+1/p_2=32/3\), gives

\[
L\ge\frac38(f_1-1)^2+\frac18(f_2-1)^2
\ge\frac3{32}(f_1+f_2-2)^2
\ge\frac3{32}(2-|f_1+f_2|)_+^2.
\tag{13}
\]

Let \(T_\varepsilon=(C\varepsilon)^{-2/3}\). The condition \(\varepsilon\le1/C\) gives \(T_\varepsilon\ge1\). At this time the right side of (12) is at most \(C\varepsilon T_\varepsilon^{3/2}=1\). That right side is increasing in time, so

\[
L(t)\ge3/32\quad(0\le t\le T_\varepsilon).
\tag{14}
\]

The constants and the exponent \(2/3\) therefore follow exactly as claimed.

At the excluded boundary \(\varepsilon=0\), oddness forces \(f_2=-f_1\), and direct completion of the square gives

\[
\tfrac38(F-1)^2+\tfrac18(-F-1)^2
=\tfrac12(F-1/2)^2+\tfrac38.
\]

The initial velocity there is \(\dot c_0=H_A/2\), confirming a moving boundary trajectory with an architectural positive-loss floor. The perturbed proof (14) does not rely on continuity of trajectories in the data.

## 4. Exact implications for exponential bounds

If \(L_\varepsilon(t)\le\exp(-\kappa_\varepsilon t)\) from time zero, (14) implies

\[
\kappa_\varepsilon\le\log(32/3)C^{2/3}\varepsilon^{2/3}.
\tag{15}
\]

With prefactor \(P_\varepsilon\ge1\), the logarithm becomes \(\log(32P_\varepsilon/3)\). Thus (5) alone cannot imply a uniform positive global rate with uniformly bounded prefactor. A diverging onset time remains an alternative for an eventual-exponential theorem.

For the more specific normalization

\[
L_\varepsilon(t)\le[\Phi_0(\text{data}_\varepsilon)e^{-\lambda t}]^\alpha,
\qquad\lambda,\alpha>0\text{ independent of }\varepsilon,
\]

the necessary condition is exactly

\[
\Phi_0(\text{data}_\varepsilon)
\ge(3/32)^{1/\alpha}
\exp[\lambda C^{-2/3}\varepsilon^{-2/3}].
\tag{16}
\]

The factor \(\alpha\) cancels from the exponent after taking the \(\alpha\)-th root; its occurrence only in the leading constant is correct. Formula (16) beats every fixed power of \(1/\varepsilon\). The phrase “essential singularity” in the route describes this necessary superpolynomial growth. Without an analyticity hypothesis on the potential, it should not be read as a complex-analytic classification of its singularity. “At least stretched-exponential blow-up in \(1/\varepsilon\)” states the exact conclusion without that terminology issue.

There is no contradiction with a potential finite at every individual nonparallel dataset and singular at the antipodal boundary. Nor does (14) bound the eventual asymptotic exponent for a fixed dataset. In particular, the argument is not an impossibility theorem for the broader unconditional target.

## 5. Initial-stall classification check

At \(c_0=0\), the full gradient vanishes exactly when \(\sum_i p_i y_i\tanh(bz_i)=0\), where \(z_i=M_0\mathfrak a(v_{i1})\). Grouping nonzero \(z_i\) by their absolute values and applying the first one, two, or three odd Taylor coefficients forces each signed coefficient sum to vanish.

A nonzero group cannot be a singleton. Three pairwise-nonparallel unit vectors cannot have one common nonzero absolute first coordinate, since the possible directions comprise at most two antipodal pairs. Two zero first coordinates are also forbidden by nonparallelness. Thus a stall must have exactly one zero center and a cancelling pair of nonzero centers.

Cancellation requires equal weights. Each positive weight is strictly less than \(1/2\), while the negative weight is \(1/2\), so the cancelling pair is precisely the two positive examples, with \(q=1/2\). Their first coordinates are opposite by strict monotonicity of \(\mathfrak a\). Their second coordinates must be equal because the other possibility makes them antipodal. This gives exactly the stated locus

\[
v_1=(\delta,s),\quad v_2=(-\delta,s),\quad v_3=(0,\sigma),
\quad0<\delta<1,\quad s=\pm\sqrt{1-\delta^2},\quad\sigma=\pm1.
\]

Conversely these data do make the gradient vanish. Local uniqueness follows from bounded tanh derivatives and the locally Lipschitz parameter vector field, so their initialized trajectories remain constant. If \(\sigma=-\operatorname{sign}s\), the vector \(\theta=(0,\operatorname{sign}s)\) separates the two classes. The separable-stall observation is therefore correct. The delay family has \(q=3/4\), so it does not approach this stall locus in the weight coordinate.

## 6. Class-center identities and energy bridges

For arbitrary \(q\in(0,1)\), define the feature-space class contrast

\[
h_t=\frac{qH_{1,t}+(1-q)H_{2,t}-H_{3,t}}2
=\sum_i p_i y_iH_{i,t},
\qquad\|f_t\|_p^2=\sum_i p_i f_{i,t}^2.
\]

Expanding the unhalved square loss gives exactly

\[
L_t=\|f_t\|_p^2-2\langle c_t,h_t\rangle+1.
\tag{17}
\]

For a nonstalled initialized flow, the initial derivative is negative because only the readout gradient is active. Continuity and monotonicity imply \(L_t<1\) for every \(t>0\). Equation (8) then gives

\[
\|c_t\|_2^2\le t(1-L_t).
\tag{18}
\]

From (17), \(2\langle c_t,h_t\rangle\ge1-L_t>0\). Combining this with (18) gives the supplied estimate

\[
\|h_t\|_2^2\ge\frac{1-L_t}{4t}.
\tag{19}
\]

Let \(A_0=\mathbb E_1|b_1|\). Since \(|a_i|\le A_0\), \(|\tanh z|\le|z|\), and \(\sum_i p_i=1\),

\[
\|h_t\|_2\le\sum_i p_i\|H_{i,t}\|_2
\le |M_t|A_0\sqrt{\mathbb E b^2}.
\]

Thus the proposed \(M\)-bound is valid, with the second-layer feature moment interpreted as the assignment's \(\mathbb E b^2\):

\[
M_t^2\ge
\frac{1-L_t}{4A_0^2\mathbb E b^2\,t}.
\tag{20}
\]

Also \(M_t>0\) for finite \(t\), since crossing zero would make every output zero and hence \(L=1\), contradicting the strict decrease.

A slightly stronger estimate follows without extra assumptions. Put \(X=\langle c_t,h_t\rangle=\sum_i p_i y_i f_i\). Weighted Cauchy–Schwarz gives \(\|f_t\|_p^2\ge X^2\), so (17) implies \((X-1)^2\le L_t\). Therefore \(X\ge1-\sqrt{L_t}\), and (18) yields

\[
\|h_t\|_2^2
\ge\frac{(1-\sqrt{L_t})^2}{t(1-L_t)}
=\frac{1-\sqrt{L_t}}{t(1+\sqrt{L_t})}.
\tag{21}
\]

Replacing the numerator of (20) accordingly gives

\[
M_t^2\ge
\frac{1-\sqrt{L_t}}
{A_0^2\mathbb E b^2\,t(1+\sqrt{L_t})}.
\tag{22}
\]

These inequalities prevent complete feature-contrast collapse or \(M=0\) at finite positive time. Once a fixed loss improvement has occurred, they also exclude decay of the corresponding norms faster than order \(t^{-1/2}\).

The full finite-energy statement gives a small further asymptotic improvement: \(\|c_t\|_2=o(\sqrt t)\). Indeed, for fixed \(T\) and \(t>T\),

\[
\frac{\|c_t\|_2}{\sqrt t}
\le\frac{\|c_T\|_2}{\sqrt t}
+\left(\int_T^\infty\|\dot c_s\|_2^2\,ds\right)^{1/2}.
\]

Take the upper limit as \(t\to\infty\), then \(T\to\infty\). Since a nonstalled trajectory has a fixed positive loss improvement after any fixed positive time, (17) consequently implies \(\sqrt t\,\|h_t\|_2\to\infty\) and \(\sqrt t\,M_t\to\infty\). These are still compatible with both norms tending to zero more slowly than \(t^{-1/2}\), an unbounded readout of size \(o(\sqrt t)\), and a positive limiting loss. They do not bound the readout uniformly, prove entry below \(p_{\min}\), or force eventual fitting.

## 7. Final disposition

No mathematical repair to the frozen delay proof is required. The only wording refinement is to treat “essential singularity” as the explicit growth bound (16), not as an analytic classification. The audited results rule out rate claims based solely on initial nonstall magnitude and verify useful finite-time center barriers. They leave the trajectory-specific learning and readout-nonescape gap open.
