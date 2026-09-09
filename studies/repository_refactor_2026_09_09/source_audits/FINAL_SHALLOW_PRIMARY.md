# Complete shallow rate proof and correction records

Exact plaintext from the three operative recovered task17 records.
No historical commands executed.

## Raw line 10282

Message Type: FINAL_ANSWER
Task name: /root
Sender: /root/h1_euler_tp_audit
Payload:
Audit result: the continuous \(H=1,B=1\) limit is rigorously solvable, but not by invoking the fixed-program TP theorem alone.

### 1. Exact reduction and assumptions

Write

\[
\psi(a,u)=a\phi(u),\qquad
g(a,u)=\nabla\psi(a,u)=\bigl(\phi(u),a\phi'(u)\bigr),
\qquad c=2\eta .
\]

The finite-width MSE flow is exactly

\[
\dot\Theta_i^n(t)
=
c\bigl(1-f_n(t)\bigr)g(\Theta_i^n(t)),
\qquad
f_n(t)=\frac1n\sum_{i=1}^n\psi(\Theta_i^n(t)),
\]

where \(\Theta_i^n=(a_i^n,u_i^n)\) and the initial particles are iid \(N(0,I_2)\).

A clean sufficient activation class is

\[
\phi\in C^2(\mathbb R),\qquad
\|\phi'\|_\infty+\|\phi''\|_\infty<\infty .
\]

Then \(\phi\) has at most linear growth and \(g\) is locally Lipschitz with linear growth. This includes affine, linear, tanh, sigmoid, softplus-type activations, and excludes the raw quadratic.

### 2. Exact feature-time solution and mean-field well-posedness

Let \(X_s(a,u)=(A_s,U_s)\) be the global characteristic flow

\[
\frac{dA_s}{ds}=\phi(U_s),
\qquad
\frac{dU_s}{ds}=A_s\phi'(U_s),
\qquad X_0(a,u)=(a,u).
\]

Linear growth gives, for every \(S<\infty\),

\[
\sup_{|s|\le S}|X_s(\xi)|\le C_S(1+|\xi|).
\]

Define the deterministic Gaussian expectation

\[
\mathcal F(s)
=
\mathbb E_{\Xi\sim N(0,I_2)}
\bigl[\psi(X_s(\Xi))\bigr].
\]

Dominated differentiation is valid because

\[
|\psi(X_s(\Xi))|
+
\left|\frac d{ds}\psi(X_s(\Xi))\right|
\le C_S(1+|\Xi|^2),
\]

and hence

\[
\mathcal F'(s)
=
\mathbb E\!\left[
\phi(U_s)^2+A_s^2\phi'(U_s)^2
\right]\ge0.
\]

Also \(\mathcal F(0)=0\). The physical clock is the scalar ODE

\[
\dot s(t)=c\bigl(1-\mathcal F(s(t))\bigr),
\qquad s(0)=0.
\]

Since \(\mathcal F\in C^1\), this ODE is locally uniquely solvable. Monotonicity gives global existence: before the first root of \(\mathcal F(s)=1\),

\[
0\le \dot s(t)\le c,
\]

and a root is an equilibrium that cannot be crossed. Thus

\[
0\le s(t)\le ct
\]

for all \(t\ge0\).

The unique mean-field solution is

\[
\mu_t=(X_{s(t)})_\#N(0,I_2),
\qquad
F(t)=\mathcal F(s(t)).
\]

Uniqueness holds among finite-second-moment McKean–Vlasov solutions: for any such solution, setting

\[
s(t)=c\int_0^t\bigl(1-F(r)\bigr)\,dr
\]

forces every characteristic to be \(X_{s(t)}(\Xi)\), reducing the problem to the unique scalar clock equation.

### 3. Direct finite-width concentration

Define the empirical feature-time function

\[
\mathcal F_n(s)
=
\frac1n\sum_{i=1}^n
\psi\bigl(X_s(\Xi_i)\bigr).
\]

The finite-width flow is exactly

\[
\Theta_i^n(t)=X_{s_n(t)}(\Xi_i),
\qquad
\dot s_n(t)=c\bigl(1-\mathcal F_n(s_n(t))\bigr).
\]

For every \(S<\infty\),

\[
\varepsilon_n(S)
:=
\sup_{|s|\le S}
|\mathcal F_n(s)-\mathcal F(s)|
\longrightarrow0
\quad\text{almost surely}.
\]

This is a uniform strong law: the class
\(s\mapsto\psi(X_s(\Xi))\) has the integrable envelope
\(C_S(1+|\Xi|^2)\) and the same type of envelope for its \(s\)-derivative.

On the deterministic clock range,

\[
|s_n(t)-s(t)|
\le
c\int_0^t
\left[
\varepsilon_n(S)
+L_S|s_n(r)-s(r)|
\right]dr,
\quad
L_S=\sup_{|s|\le S}|\mathcal F'(s)|.
\]

Therefore

\[
\sup_{t\le T}|s_n(t)-s(t)|
\le
cT e^{cL_ST}\varepsilon_n(S),
\]

and consequently

\[
\sup_{t\le T}|f_n(t)-F(t)|\longrightarrow0
\]

almost surely and in every finite \(L^p\). The \(L^p\) upgrade follows from

\[
\sup_{t\le T}|f_n(t)|
\le
\frac1n\sum_i C_T(1+|\Xi_i|^2),
\]

whose moments are uniformly bounded. Hence output and loss variances vanish.

This proves the continuous-time limit directly; TP is unnecessary in this special model.

### 4. The exact valid one-step inequality

For the scalar clock Euler scheme

\[
\sigma_{k+1}^{n,h}
=
\sigma_k^{n,h}
+
hc\bigl[1-\mathcal F_n(\sigma_k^{n,h})\bigr],
\qquad \sigma_0^{n,h}=0,
\]

set

\[
\Delta_k=|\sigma_k^{n,h}-s(kh)|.
\]

Taylor’s theorem for the exact clock and the preceding uniform empirical error give

\[
\boxed{
\Delta_{k+1}
\le
(1+cL_Sh)\Delta_k
+
ch\,\varepsilon_n(S)
+
\frac12M_{s,T}h^2,
}
\]

where

\[
M_{s,T}=\sup_{t\le T}|s''(t)|
\le c^2\sup_{0\le s\le cT}\mathcal F'(s).
\]

This is precisely the desired mesh-scaled inequality, with an actually defined width error that is uniform in \(h\). It implies convergence for every joint sequence \(n\to\infty\), \(h\to0\) for this clock-Euler scheme.

Importantly, \(\varepsilon_n(S)\) comes from a direct uniform empirical-process argument, not from the TP Master Theorem.

### 5. Raw parameter Euler is different

Actual gradient descent is

\[
\Theta_{i,k+1}^{n,h}
=
\Theta_{i,k}^{n,h}
+
hc(1-f_{n,k})g(\Theta_{i,k}^{n,h}).
\]

It is not exactly the clock scheme because

\[
X_\alpha(\theta)
\ne
\theta+\alpha g(\theta).
\]

The difference is the ordinary local Euler defect

\[
X_\alpha(\theta)-\theta-\alpha g(\theta)
=
\int_0^\alpha(\alpha-r)
Dg(X_r(\theta))g(X_r(\theta))\,dr.
\]

After truncating the Gaussian seeds to \(|\Xi_i|\le R\), all reachable states lie in a deterministic compact set, and the correct coupled inequality is

\[
\boxed{
\Delta_{k+1}^{(R)}
\le
(1+C_{T,R}h)\Delta_k^{(R)}
+
C_{T,R}h\,\varepsilon_{n,R}
+
C_{T,R}h^2.
}
\]

Here \(\Delta^{(R)}\) must include the normalized particle discrepancy as well as the clock/output discrepancy.

For the untruncated Gaussian initialization, one cannot simply replace \(C_{T,R}\) by an unproved ordinary-\(L^2\) constant \(C_T\): \(Dg\) contains \(a\phi''(u)\), and \(\max_i|a_i|\sim\sqrt{\log n}\). The rigorous route is cutoff removal. The characteristic Jacobian satisfies an envelope of the form

\[
\|DX_s(\Xi)\|
\le
\exp\!\bigl(C_T(1+|\Xi|)\bigr),
\]

and Gaussian tails give

\[
\rho_T(R)
\lesssim
\left\{
\mathbb E\!\left[
(1+|\Xi|)^m e^{C_T|\Xi|}
\mathbf 1_{\{|\Xi|>R\}}
\right]
\right\}^{1/2}
\longrightarrow0.
\]

Thus the actual estimate is canonically

\[
\sup_{k\le T/h}\Delta_k
\le
C_{T,R}\bigl(\varepsilon_{n,R}+h\bigr)+\rho_T(R),
\]

with limits taken by first fixing \(R\), then sending \(n\to\infty\) and \(h\to0\), and finally \(R\to\infty\). This suffices for arbitrary joint width/mesh sequences once the cutoff estimate is included; the unqualified single-\(C_T\) inequality is not automatically valid in the natural unweighted particle norm.

### 6. What TP itself does and does not give

For fixed \(h>0\) and fixed

\[
K=\lfloor T/h\rfloor,
\]

the Euler trajectory is one finite program. TP gives

\[
\max_{k\le K}|f_{n,k}^h-F_k^h|\to0.
\]

But the theorem is qualitative and program-dependent. It supplies only errors of the form

\[
\varepsilon_{n;h,K}\to0
\]

for each fixed \((h,K)\). It does not supply:

- a rate;
- a single \(\varepsilon_n\) uniform as \(h\downarrow0\);
- control as \(K=T/h\to\infty\);
- the factor \(h\varepsilon_n\);
- a width-uniform stability constant.

Therefore TP alone proves only the ordered limit

\[
\lim_{h\downarrow0}\limsup_{n\to\infty}
\Pr\!\left\{
\max_{k\le T/h}|f_{n,k}^h-F(kh)|>\delta
\right\}=0.
\]

It also yields the existence of a sufficiently slow diagonal \(h_n\downarrow0\), but not convergence along every diagonal.

In \(H=1,B=1\), there are no nontrivial transpose/Onsager issues after collapsing the fixed input to \(u_i\). The direct scalar-clock proof is both stronger and simpler than TP.

### 7. Quadratic boundary

For \(\phi(u)=u^2\), feature time obeys

\[
A'=U^2,\qquad U'=2AU,
\]

with invariant

\[
U^2-2A^2=\text{constant}.
\]

For every initial condition with \(A_0>0\) and \(U_0\ne0\), \(A_s\) blows up in finite positive feature time. Under Gaussian initialization, for every \(s>0\) there is positive probability of explosion before \(s\), and at width \(n\) the earliest explosion time tends to zero because of extreme coordinates. Thus the failure is stronger than merely having a bad Gronwall constant: the proposed conventional mean-field characteristic law is not well posed at any positive feature time.

## Raw line 10296

Message Type: FINAL_ANSWER
Task name: /root
Sender: /root/h1_flow_direct
Payload:
The one-hidden-layer, one-sample continuous-time problem can be resolved directly. Its special structure reduces the interacting \(2n\)-dimensional flow to one random scalar clock.

## 1. Exact finite-width dynamics

Let

\[
f_n(t)=\frac1n\sum_{i=1}^n a_i(t)\phi(g_i(t)),
\qquad
L_n(t)=(f_n(t)-1)^2,
\]

and use μP gradient flow

\[
\dot\theta=-n\eta\nabla_\theta L_n.
\]

With \(c=2\eta\ge 0\), exact differentiation gives

\[
\dot a_i=c(1-f_n)\phi(g_i),
\qquad
\dot g_i=c(1-f_n)a_i\phi'(g_i).
\]

Thus, for

\[
H(a,g)=a\phi(g),
\qquad
V(a,g)=\nabla H(a,g)=\bigl(\phi(g),a\phi'(g)\bigr),
\]

the system is

\[
\dot X_i^n(t)
=
c\left[1-\frac1n\sum_{j=1}^nH(X_j^n(t))\right]V(X_i^n(t)),
\qquad X_i^n=(a_i,g_i).
\]

The signs and μP factors are exact.

## 2. The theorem

Assume

\[
X_i^n(0)=(A_i,G_i)\stackrel{\mathrm{iid}}{\sim}N(0,I_2),
\]

and

\[
\phi\in C^2(\mathbb R),
\qquad
\|\phi'\|_\infty<\infty.
\]

Thus \(\phi\) is allowed to grow linearly. For the simplest quantitative pathwise propagation-of-chaos proof one may additionally assume \(\|\phi\|_\infty<\infty\).

Then, for every fixed \(T<\infty\):

1. The finite-\(n\) particle system has a unique global solution.
2. The McKean–Vlasov gradient flow has a unique global characteristic solution \(\rho_t\).
3. There is a deterministic output \(f(t)\) such that
   \[
   \mathbb E\sup_{0\le t\le T}|f_n(t)-f(t)|^2
   \le \frac{C_T}{n}.
   \]
4. Consequently,
   \[
   \sup_{t\le T}\operatorname{Var}f_n(t)\le \frac{C_T}{n},
   \]
   and
   \[
   \mathbb E[(1-f_n(t))^2]\longrightarrow(1-f(t))^2.
   \]
5. Under bounded \(\phi\), if
   \[
   \bar X_i(t)
   \]
   are independent copies of the nonlinear limiting particle coupled through the same initial variables, then
   \[
   \mathbb E\left[
   \frac1n\sum_{i=1}^n
   \sup_{t\le T}|X_i^n(t)-\bar X_i(t)|^2
   \right]
   \le\frac{C_T}{n}.
   \]

The last estimate implies path-space propagation of chaos for every fixed number of particles.

## 3. Common-clock representation

Let \(\Psi_s\) be the autonomous feature-ascent flow

\[
\frac{d}{ds}\Psi_s(x)=V(\Psi_s(x)),
\qquad
\Psi_0(x)=x.
\]

Since

\[
|\phi(g)|\le |\phi(0)|+\|\phi'\|_\infty|g|,
\qquad
|V(x)|\le C(1+|x|),
\]

and \(V\) is locally Lipschitz, \(\Psi_s(x)\) exists uniquely for every \(s\in\mathbb R\).

Define the random and deterministic feature curves

\[
\mathcal F_n(s)
=
\frac1n\sum_{i=1}^nH\bigl(\Psi_s(X_i^n(0))\bigr),
\]

\[
\mathcal F(s)
=
\mathbb E\!\left[
H\bigl(\Psi_s(X^0)\bigr)
\right],
\qquad X^0\sim N(0,I_2).
\]

Now let

\[
\dot\sigma_n(t)
=
c\left[1-\mathcal F_n(\sigma_n(t))\right],
\qquad
\sigma_n(0)=0.
\]

Then, exactly,

\[
\boxed{
X_i^n(t)=\Psi_{\sigma_n(t)}(X_i^n(0)),
\qquad
f_n(t)=\mathcal F_n(\sigma_n(t)).
}
\]

Indeed, differentiating this representation reproduces the particle ODE.

The limiting clock is

\[
\dot\sigma(t)
=
c\left[1-\mathcal F(\sigma(t))\right],
\qquad
\sigma(0)=0,
\]

and

\[
\boxed{
\rho_t=(\Psi_{\sigma(t)})_\#N(0,I_2),
\qquad
f(t)=\mathcal F(\sigma(t)).
}
\]

Equivalently, if

\[
\Psi_s(A,G)=\bigl(A_s(A,G),G_s(A,G)\bigr),
\]

then

\[
\mathcal F(s)
=
\mathbb E_{A,G}\!\left[
A_s(A,G)\phi\bigl(G_s(A,G)\bigr)
\right].
\]

This is an exact finite-displacement Gaussian expectation, with no Taylor or Hermite approximation.

## 4. Global well-posedness

Along one feature trajectory,

\[
\frac{d}{ds}H(\Psi_s(x))
=
\nabla H(\Psi_s(x))\cdot V(\Psi_s(x))
=
|V(\Psi_s(x))|^2.
\]

Therefore

\[
\mathcal F'(s)
=
\mathcal K(s),
\qquad
\mathcal K(s)
=
\mathbb E\!\left[
\phi(G_s)^2+A_s^2\phi'(G_s)^2
\right]\ge0.
\]

Similarly,

\[
\mathcal F_n'(s)=\mathcal K_n(s)\ge0.
\]

For the limiting residual \(r(t)=1-f(t)\),

\[
\dot r(t)
=
-\mathcal F'(\sigma(t))\dot\sigma(t)
=
-c\,\mathcal K(\sigma(t))r(t).
\]

Because \(\mathcal F(0)=\mathbb E[A\phi(G)]=0\),

\[
r(t)
=
\exp\left(
-c\int_0^t\mathcal K(\sigma(u))\,du
\right),
\]

so

\[
0<r(t)\le1,
\qquad
0\le\sigma(t)\le c t.
\]

The clock cannot explode.

At finite width,

\[
r_n(t)=1-f_n(t)
\]

satisfies exactly

\[
\dot r_n
=
-c\,\mathcal K_n(\sigma_n)r_n,
\]

and hence

\[
|r_n(t)|\le |r_n(0)|,
\qquad
|\sigma_n(t)|\le cT|r_n(0)|.
\]

This proves global finite-width existence as well.

For uniqueness of the mean field, consider any characteristic solution \(X(t)\) and define

\[
\widetilde\sigma(t)
=
\int_0^t c(1-\mathbb EH(X(u)))\,du.
\]

Because the multiplier is scalar,

\[
X(t)=\Psi_{\widetilde\sigma(t)}(X(0)).
\]

Consequently, \(\widetilde\sigma\) must solve the scalar ODE involving \(\mathcal F\). That scalar ODE is locally Lipschitz and has the global bound above, so it is unique. This proves uniqueness of the Lagrangian McKean–Vlasov solution.

The corresponding PDE is

\[
\partial_t\rho_t+
\nabla\cdot
\left[
\rho_t\,c\left(1-\int H\,d\rho_t\right)\nabla H
\right]=0.
\]

It is the Wasserstein gradient flow, with learning-rate factor \(\eta\), of

\[
\mathcal R(\rho)
=
\left(1-\int H\,d\rho\right)^2.
\]

## 5. Uniform empirical-process estimate

For \(x=(a,g)\), define

\[
Y_s(x)=H(\Psi_s(x)),
\qquad
J_s(x)=\frac{d}{ds}Y_s(x)=|V(\Psi_s(x))|^2.
\]

For every fixed \(S\),

\[
\sup_{|s|\le S}|\Psi_s(x)|
\le C_S(1+|x|),
\]

and consequently

\[
\sup_{|s|\le S}\bigl(|Y_s(x)|+|J_s(x)|\bigr)
\le C_S(1+|x|^2).
\]

Let \(P_n\) denote the empirical average and \(P\) expectation. Set

\[
D_{n,S}
=
\sup_{|s|\le S}|(P_n-P)Y_s|.
\]

Since

\[
Y_s=Y_0+\int_0^sJ_r\,dr,
\]

we have

\[
D_{n,S}
\le
|(P_n-P)Y_0|
+
\int_{-S}^{S}|(P_n-P)J_r|\,dr.
\]

Independence gives

\[
\mathbb E|(P_n-P)Y_0|^2
=
\frac{\operatorname{Var}(Y_0)}n
\]

and

\[
\mathbb E|(P_n-P)J_r|^2
=
\frac{\operatorname{Var}(J_r)}n.
\]

Therefore, by Cauchy–Schwarz in \(r\),

\[
\boxed{
\mathbb E D_{n,S}^2\le\frac{C_S}{n}.
}
\]

The fourth-moment identity for a centered iid sample mean,

\[
\mathbb E\left|
\frac1n\sum_{i=1}^n Z_i
\right|^4
=
\frac{\mathbb EZ_1^4}{n^3}
+
\frac{3(n-1)(\mathbb EZ_1^2)^2}{n^3},
\]

and Hölder’s inequality for the \(r\)-integral similarly give

\[
\boxed{
\mathbb E D_{n,S}^4\le\frac{C_S}{n^2}.
}
\]

This is the width-uniform continuum estimate that a fixed-length TP Master Theorem does not itself provide.

## 6. Clock and output convergence

Let

\[
E_n=\{|\mathcal F_n(0)|\le1\}.
\]

On \(E_n\),

\[
|\sigma_n(t)|\le2cT,
\qquad
|\sigma(t)|\le cT.
\]

Take \(S=2cT\), and let

\[
L_S=\sup_{|s|\le S}|\mathcal F'(s)|<\infty.
\]

Then

\[
|\sigma_n(t)-\sigma(t)|
\le
c\int_0^t
\left[
D_{n,S}
+
L_S|\sigma_n(u)-\sigma(u)|
\right]du.
\]

Gronwall yields

\[
\sup_{t\le T}|\sigma_n(t)-\sigma(t)|
\le
cT e^{cL_ST}D_{n,S}.
\]

Hence, on \(E_n\),

\[
\sup_{t\le T}|f_n(t)-f(t)|
\le
\left(1+cTL_Se^{cL_ST}\right)D_{n,S}.
\]

On \(E_n^c\), residual monotonicity gives

\[
|f_n(t)|
\le
1+|r_n(0)|
\le
2+|\mathcal F_n(0)|.
\]

Since \(\mathcal F_n(0)\) is a centered iid sample mean,

\[
\mathbb P(E_n^c)
\le
\mathbb E|\mathcal F_n(0)|^4
=
O(n^{-2}).
\]

Hölder’s inequality therefore controls the complement and proves

\[
\mathbb E\sup_{t\le T}|f_n(t)-f(t)|^2
\le
\frac{C_T}{n}.
\]

Using eighth moments in the same argument gives

\[
\mathbb E\sup_{t\le T}|f_n(t)-f(t)|^4
\le
\frac{C_T}{n^2}.
\]

The latter estimate proves \(L^2\) convergence of the loss and, in particular, vanishing loss variance.

## 7. Quantitative propagation of chaos

Couple

\[
\bar X_i(t)=\Psi_{\sigma(t)}(X_i^n(0)).
\]

These are iid because \(\sigma(t)\) is deterministic. On \(E_n\), for bounded \(\phi\),

\[
\sup_{|s|\le S}|V(\Psi_s(A_i,G_i))|
\le C_S(1+|A_i|).
\]

Thus

\[
\sup_{t\le T}|X_i^n(t)-\bar X_i(t)|
\le
C_S(1+|A_i|)
\sup_{t\le T}|\sigma_n(t)-\sigma(t)|.
\]

Combining \(\mathbb ED_{n,S}^4=O(n^{-2})\) with the bounded empirical Gaussian moments gives

\[
\mathbb E\left[
\frac1n\sum_i
\sup_{t\le T}|X_i^n(t)-\bar X_i(t)|^2
\mathbf 1_{E_n}
\right]
\le\frac{C_T}{n}.
\]

The complement is controlled using the polynomial feature-flow bound valid for bounded \(\phi\) and higher Gaussian moments. Hence

\[
\mathbb E\left[
\frac1n\sum_i
\sup_{t\le T}|X_i^n(t)-\bar X_i(t)|^2
\right]
\le\frac{C_T}{n}.
\]

If only \(\|\phi'\|_\infty<\infty\), then

\[
|\Psi_s(x)|\le C e^{C|s|}(1+|x|).
\]

The output estimate remains unchanged. Pathwise \(L^2\) chaos requires an additional exponential localization argument. Gaussian initialization supplies the necessary subexponential tail for \(A\phi(G)\), so the argument can still be closed for every fixed \(T\), but bounded \(\phi\) avoids this extra tail bookkeeping.

## 8. The proposed one-step inequality

For the feature-exact clock Euler scheme

\[
\widehat\sigma_{n,k+1}
=
\widehat\sigma_{n,k}
+
hc\left[1-\mathcal F_n(\widehat\sigma_{n,k})\right],
\]

let

\[
e_k=|\widehat\sigma_{n,k}-\sigma(kh)|.
\]

Taylor expansion of the deterministic clock gives a uniform local defect \(C_Th^2\). Therefore,

\[
\boxed{
e_{k+1}
\le
(1+hcL_S)e_k
+
hcD_{n,S}
+
C_Th^2.
}
\]

Thus the proposed inequality is valid here with

\[
\varepsilon_n=D_{n,S},
\qquad
\mathbb E\varepsilon_n^2=O(n^{-1}).
\]

Iteration gives

\[
\max_{k\le T/h}e_k
=
O_{L^2}(n^{-1/2}+h).
\]

However, this clock Euler scheme is not literally the raw simultaneous parameter Euler scheme. Raw Euler uses

\[
X_{i,k+1}
=
X_{i,k}
+
hc(1-f_{n,k})V(X_{i,k}),
\]

whereas the feature-exact scheme advances by \(\Psi_{\Delta\sigma}\). Under

\[
\phi,\phi',\phi''\in L^\infty,
\]

a moment-localized variable-step Euler estimate shows that the difference between these two advances is \(O(h^2)\) per step in an empirical moment norm; it therefore contributes precisely another \(C_Th^2\) term. Without that extra estimate, the scalar-clock inequality must not be presented as a literal raw-state TP inequality.

Most importantly, fixed-step TP convergence alone does not furnish \(D_{n,S}\) uniformly when \(T/h\to\infty\). The continuum uniform law of large numbers above is the missing quantitative ingredient.

## 9. Exact controls

For \(\phi(g)\equiv K\),

\[
\mathcal F(s)=K^2s,
\]

so

\[
f(t)=1-e^{-cK^2t}.
\]

For \(\phi(g)=g\),

\[
\Psi_s(a,g)
=
\left(
a\cosh s+g\sinh s,\;
g\cosh s+a\sinh s
\right),
\]

and therefore

\[
\mathcal F(s)=\sinh(2s).
\]

Consequently,

\[
\dot f
=
2c(1-f)\sqrt{1+f^2},
\qquad
\dot f(0)=2c,
\]

which agrees with the one-hidden-layer NTK coefficient \(A_1=2\).

The quadratic activation is excluded because \(\phi'\) is unbounded. Its autonomous feature flow can have finite feature-time blow-up, and Gaussian extreme coordinates can make the relevant stability time shrink with width. Thus its obstruction is structural, not merely an artifact of a loose Gronwall bound.

## Raw line 10320

Yes—but with one important correction to the notes:

The discrete Gronwall calculation is correct conditional on the one-step inequality. However, the fixed-program Tensor Programs theorem does not itself provide an error \(\varepsilon_n\) uniform when the program length \(T/h\) diverges. For the one-hidden-layer model, we can prove that missing uniform estimate directly using an exact scalar “feature clock.”

## 1. Exact finite-width gradient flow

Take

\[
f_n(t)=\frac1n\sum_{i=1}^n a_i(t)\phi(u_i(t)),
\qquad
L_n(t)=(f_n(t)-1)^2,
\]

with \(u_i=w_i^\top x/\sqrt{d_0}\), \(\|x\|^2/d_0=1\), and μP gradient flow

\[
\dot\theta=-n\eta\nabla_\theta L_n.
\]

Set \(c=2\eta\ge0\). Exact differentiation gives

\[
\dot a_i=c(1-f_n)\phi(u_i),
\qquad
\dot u_i=c(1-f_n)a_i\phi'(u_i).
\]

Define

\[
H(a,u)=a\phi(u),
\qquad
V(a,u)=\nabla H(a,u)
=
\bigl(\phi(u),a\phi'(u)\bigr).
\]

Then

\[
\dot X_i^n
=
c\left[1-\frac1n\sum_{j=1}^nH(X_j^n)\right]V(X_i^n),
\qquad
X_i^n=(a_i,u_i).
\]

This is the exact finite-width system.

## 2. Clean theorem

Assume

\[
X_i^n(0)=(A_i,G_i)\overset{\mathrm{iid}}{\sim}N(0,I_2),
\]

and

\[
\phi\in C^2(\mathbb R),
\qquad
\|\phi'\|_\infty+\|\phi''\|_\infty<\infty.
\]

Thus \(\phi\) may grow linearly. This includes constant, affine, linear, tanh, sigmoid, and softplus-type activations.

Then for every fixed \(T<\infty\):

1. The finite-width gradient flow has a unique global solution.
2. The corresponding McKean–Vlasov mean-field flow has a unique global characteristic solution.
3. There is a deterministic output \(f(t)\) such that
   \[
   \mathbb E\sup_{0\le t\le T}|f_n(t)-f(t)|^2
   \le \frac{C_T}{n}.
   \]
4. Consequently,
   \[
   \sup_{t\le T}\operatorname{Var}(f_n(t))
   \le\frac{C_T}{n},
   \]
   and
   \[
   \mathbb E[(1-f_n(t))^2]\longrightarrow(1-f(t))^2.
   \]

No time discretization, Taylor expansion, or Hermite approximation is involved.

## 3. Exact feature-clock reduction

Let \(\Psi_s(a,u)=(A_s,U_s)\) solve the autonomous feature-ascent equations

\[
\frac{dA_s}{ds}=\phi(U_s),
\qquad
\frac{dU_s}{ds}=A_s\phi'(U_s),
\qquad
(A_0,U_0)=(a,u).
\]

Because \(\phi'\) is bounded,

\[
|\phi(u)|\le |\phi(0)|+\|\phi'\|_\infty|u|,
\]

so \(V\) has linear growth. Since \(V\) is also locally Lipschitz, \(\Psi_s\) exists uniquely for every \(s\in\mathbb R\), with

\[
\sup_{|s|\le S}|\Psi_s(x)|
\le C_S(1+|x|).
\]

Define the empirical and population feature curves

\[
\mathcal F_n(s)
=
\frac1n\sum_{i=1}^n
H\!\left(\Psi_s(A_i,G_i)\right),
\]

\[
\mathcal F(s)
=
\mathbb E_{A,G}
\left[
H\!\left(\Psi_s(A,G)\right)
\right].
\]

Now define scalar clocks

\[
\dot s_n(t)
=
c\bigl[1-\mathcal F_n(s_n(t))\bigr],
\qquad
s_n(0)=0,
\]

and

\[
\dot s(t)
=
c\bigl[1-\mathcal F(s(t))\bigr],
\qquad
s(0)=0.
\]

Then, exactly,

\[
X_i^n(t)=\Psi_{s_n(t)}(A_i,G_i),
\qquad
f_n(t)=\mathcal F_n(s_n(t)).
\]

The limiting particle and output are

\[
\bar X(t)=\Psi_{s(t)}(A,G),
\qquad
f(t)=\mathcal F(s(t)).
\]

Thus the exact continuous mean-field answer is the Gaussian expectation

\[
f(t)
=
\mathbb E_{A,G\sim N(0,1)}
\left[
A_{s(t)}(A,G)\,
\phi\!\left(U_{s(t)}(A,G)\right)
\right].
\]

The original \(2n\)-dimensional interaction has reduced to one scalar clock.

## 4. Mean-field well-posedness

Along a feature trajectory,

\[
\frac{d}{ds}H(A_s,U_s)
=
\nabla H(A_s,U_s)\cdot V(A_s,U_s)
=
|V(A_s,U_s)|^2.
\]

Therefore

\[
\mathcal F'(s)
=
\mathbb E\left[
\phi(U_s)^2
+
A_s^2\phi'(U_s)^2
\right]
\ge0.
\]

The differentiation under expectation is valid because, on every bounded \(s\)-interval,

\[
|H(\Psi_s(A,G))|
+
|V(\Psi_s(A,G))|^2
\le C_S(1+A^2+G^2).
\]

Since \(A,G\) are Gaussian, this envelope is integrable.

Let

\[
r(t)=1-f(t)=1-\mathcal F(s(t)).
\]

Then

\[
\dot r(t)
=
-\mathcal F'(s(t))\dot s(t)
=
-c\,\mathcal F'(s(t))r(t).
\]

Because \(\mathcal F(0)=\mathbb E[A\phi(G)]=0\),

\[
r(t)
=
\exp\left(
-c\int_0^t\mathcal F'(s(v))\,dv
\right).
\]

Hence

\[
0<r(t)\le1,
\qquad
0\le s(t)\le ct.
\]

So the clock cannot explode, proving global existence.

Uniqueness is equally direct. Any McKean–Vlasov characteristic solution must have the form

\[
X(t)=\Psi_{\sigma(t)}X(0),
\qquad
\sigma(t)=c\int_0^t
\left[1-\mathbb EH(X(v))\right]dv.
\]

This forces \(\sigma\) to solve the same scalar clock ODE. Since \(\mathcal F\in C^1\), that scalar ODE is locally Lipschitz and unique.

Equivalently, the unique mean-field law is

\[
\mu_t=(\Psi_{s(t)})_\#N(0,I_2),
\]

and it solves

\[
\partial_t\mu_t
+
\nabla_{a,u}\cdot
\left[
c\left(1-\int H\,d\mu_t\right)
V\,\mu_t
\right]
=0.
\]

This proves global well-posedness of the mean-field gradient flow in the characteristic class with finite second moments.

## 5. Uniform continuum law of large numbers

For \(x=(a,u)\), define

\[
Y_s(x)=H(\Psi_sx),
\qquad
J_s(x)=\frac{dY_s(x)}{ds}=|V(\Psi_sx)|^2.
\]

For every fixed \(S\),

\[
\sup_{|s|\le S}
\bigl(
|Y_s(x)|+|J_s(x)|
\bigr)
\le C_S(1+|x|^2).
\]

Let \(P_n\) denote empirical averaging and \(P\) Gaussian expectation, and set

\[
\varepsilon_n(S)
=
\sup_{|s|\le S}|(P_n-P)Y_s|.
\]

Since

\[
Y_s=Y_0+\int_0^sJ_v\,dv,
\]

we obtain

\[
\varepsilon_n(S)
\le
|(P_n-P)Y_0|
+
\int_{-S}^{S}|(P_n-P)J_v|\,dv.
\]

Independence gives

\[
\mathbb E|(P_n-P)Y_0|^2
=
\frac{\operatorname{Var}(Y_0)}n
\]

and

\[
\mathbb E|(P_n-P)J_v|^2
=
\frac{\operatorname{Var}(J_v)}n.
\]

Cauchy–Schwarz in \(v\) therefore gives the width-uniform continuum estimate

\[
\mathbb E[\varepsilon_n(S)^2]
\le\frac{C_S}{n}.
\]

Using fourth moments similarly gives

\[
\mathbb E[\varepsilon_n(S)^4]
\le\frac{C_S}{n^2}.
\]

This is the key estimate that fixed-length TP does not provide.

## 6. Clock and output concentration

On the event \(|\mathcal F_n(0)|\le1\), residual monotonicity gives

\[
|s_n(t)|\le2cT,
\qquad
|s(t)|\le cT.
\]

Take \(S=2cT\) and

\[
L_S=\sup_{|s|\le S}|\mathcal F'(s)|<\infty.
\]

Then

\[
|s_n(t)-s(t)|
\le
c\int_0^t
\left[
\varepsilon_n(S)
+
L_S|s_n(v)-s(v)|
\right]dv.
\]

Gronwall yields

\[
\sup_{t\le T}|s_n(t)-s(t)|
\le
cT e^{cL_ST}\varepsilon_n(S).
\]

Consequently,

\[
\sup_{t\le T}|f_n(t)-f(t)|
\le
\left(1+cTL_Se^{cL_ST}\right)\varepsilon_n(S).
\]

The complementary event has probability \(O(n^{-2})\), because \(\mathcal F_n(0)\) is a centered empirical mean with finite fourth moment. Moreover,

\[
|1-f_n(t)|\le |1-f_n(0)|,
\]

so its contribution is uniformly integrable. Combining the two events proves

\[
\mathbb E\sup_{t\le T}|f_n(t)-f(t)|^2
\le\frac{C_T}{n}.
\]

This establishes continuous-time propagation of chaos for the output and identifies its deterministic limit.

## 7. Your one-step inequality

For the empirical clock Euler scheme

\[
s_{n,k+1}^{h}
=
s_{n,k}^{h}
+
hc\left[
1-\mathcal F_n(s_{n,k}^{h})
\right],
\]

let

\[
\Delta_k
=
|s_{n,k}^{h}-s(kh)|.
\]

Taylor’s theorem gives

\[
s((k+1)h)
=
s(kh)
+
hc[1-\mathcal F(s(kh))]
+
\tau_k,
\]

where

\[
|\tau_k|
\le
\frac12
\sup_{t\le T}|s''(t)|\,h^2
\le C_Th^2,
\]

because

\[
s''(t)
=
-c\,\mathcal F'(s(t))s'(t).
\]

Therefore

\[
\Delta_{k+1}
\le
(1+cL_Sh)\Delta_k
+
ch\,\varepsilon_n(S)
+
C_Th^2.
\]

This is exactly the proposed inequality, with an explicitly defined error satisfying

\[
\mathbb E[\varepsilon_n(S)^2]
\le\frac{C_S}{n}.
\]

Iteration gives

\[
\max_{k\le T/h}\Delta_k
=
O_{L^2}\left(n^{-1/2}+h\right).
\]

Thus the joint width-and-mesh limit is valid for every sequence

\[
n\to\infty,
\qquad
h\to0
\]

for this clock-Euler scheme.

## 8. Raw gradient-descent Euler needs one qualification

The raw simultaneous parameter update is

\[
X_{i,k+1}
=
X_{i,k}
+
hc(1-f_{n,k})V(X_{i,k}).
\]

It is not literally the same as advancing by the exact feature flow:

\[
\Psi_\alpha(x)\neq x+\alpha V(x).
\]

The exact local defect is

\[
\Psi_\alpha(x)-x-\alpha V(x)
=
\int_0^\alpha
(\alpha-r)\,
DV(\Psi_r(x))V(\Psi_r(x))\,dr.
\]

With Gaussian initialization, \(DV\) contains \(a\phi''(u)\), so a pathwise supremum-coordinate stability constant involves \(\max_i|a_i|\sim\sqrt{\log n}\). Therefore the unqualified claim that a deterministic \(C_T\) automatically works in the ordinary sup-coordinate norm is not justified.

The rigorous formulation uses cutoff removal. For seeds \(|(A_i,G_i)|\le R\),

\[
\Delta_{k+1}^{(R)}
\le
(1+C_{T,R}h)\Delta_k^{(R)}
+
C_{T,R}h\,\varepsilon_{n,R}
+
C_{T,R}h^2.
\]

Gaussian tails then give a remainder \(\rho_T(R)\to0\), yielding

\[
\max_{k\le T/h}\Delta_k
\le
C_{T,R}(\varepsilon_{n,R}+h)+\rho_T(R).
\]

Fix \(R\), send \(n\to\infty\) and \(h\to0\), then send \(R\to\infty\). This proves convergence of raw parameter Euler as well, but the cutoff step must not be omitted.

## 9. What TP does and does not prove

For fixed \(h\), the number of steps \(K=T/h\) is finite. The [Tensor Programs IV Master Theorem](https://proceedings.mlr.press/v139/yang21c/yang21c-supp.pdf) therefore proves the width limit for that fixed program.

But its error is program-dependent:

\[
\varepsilon_{n;h,K}\to0
\qquad
\text{for each fixed }(h,K).
\]

It does not provide:

- a rate uniform in \(h\);
- control as \(K=T/h\to\infty\);
- the factor \(h\varepsilon_n\);
- a width-uniform stability constant.

So TP alone gives the ordered limit \(n\to\infty\) first, then \(h\to0\), and possibly a sufficiently slow diagonal. The common-clock uniform law of large numbers is what upgrades this to arbitrary joint width-and-mesh convergence in the one-hidden-layer model.

## 10. The quadratic obstruction is real

For \(\phi(u)=u^2\), feature time satisfies

\[
A'=U^2,
\qquad
U'=2AU,
\]

with invariant

\[
U^2-2A^2=\text{constant}.
\]

On the event

\[
A_0\ge R,
\qquad
U_0^2\ge2A_0^2,
\]

we have

\[
A'\ge2A^2,
\]

so the feature trajectory blows up no later than \(1/(2R)\). This event has positive Gaussian probability for every \(R\). Therefore, for every \(s>0\), a positive portion of the population has already exploded before feature time \(s\).

At width \(n\), the earliest feature blow-up time tends to zero almost surely because of Gaussian extreme coordinates. MSE feedback stops each finite-width physical trajectory before its feature singularity, but creates an initial boundary layer:

\[
f_n(0)\longrightarrow0,
\qquad
f_n(t)\longrightarrow1
\quad\text{for every fixed }t>0.
\]

Hence there is no convergence in \(C([0,T])\) to a classical continuous mean-field flow.

So the quadratic failure is stronger than merely having a poor Gronwall constant: the proposed Gaussian characteristic mean field is not classically well posed at any positive feature time.

In short: the continuous one-hidden-layer theorem is proved under bounded-slope smooth activations, including a quantitative \(O(1/n)\) output variance bound. Your one-step inequality is exactly correct for the feature clock, while raw parameter Euler requires an explicit Gaussian-tail localization. Fixed-program TP alone does not supply the necessary mesh-uniform estimate.
