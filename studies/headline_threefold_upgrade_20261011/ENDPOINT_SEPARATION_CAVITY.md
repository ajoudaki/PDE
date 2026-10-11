# Endpoint separation through a trained-neuron cavity response

2026-10-11. Scoped independent first-round derivation. Status: an exact finite-width cavity response is proved below; the requested endpoint lower bound remains open in this route. No computation, experiment, paper change, or Git operation was performed.

The scientific inputs are `paper/compact.tex`, `paper/compact_fitting.tex`, `paper/compact_foundations.tex`, this study's `NONPARALLEL_INITIAL_VARIABILITY.md` and `NONPARALLEL_ENDPOINT_ROUTE.md`, and the authorized `GAUSSIAN_ORACLE_ENDPOINT.md` and `GELU_SILU_PROJECTED_SCALAR.md` in `general_nonlinear_endpoint_lower_20261010`. The rigorous-proof, conjecture-investigation, and canonical-notation instructions, including the neural-network reference, were applied. Other current proof-route notes were not read.

## Contract and result

The target is the actual canonical network

\[
z^{(1)}(v)=W^{(1)}v,\qquad
z^{(\ell)}(v)=W^{(\ell)}h^{(\ell-1)}(v),\qquad
h^{(\ell)}(v)=\phi_\ell(z^{(\ell)}(v)),\qquad
f_n(\sqrt d\,v)=n^{-1}w^\top h^{(L)}(v).
\]

Its loss is \(m^{-1}\sum_a r_a^2\), where \(r_a=f_n(\sqrt d\,v_a)-y_a\), and its physical block mobilities are \((n,1,\ldots,1,n)\). All hidden weights are trained, all initial hidden blocks have the specified Gaussian laws, and \(w(0)=0\). The activations are nonaffine, analytic on the prescribed strip, with bounded strip derivative; their values may be unbounded. The original restriction

\[
0<Y=\|y\|/\sqrt m\le(\gamma/m)\beta^{-30L}
\]

is unchanged. The depth \(L\ge2\), training data, nonzero labels, and test direction are fixed before width grows. Training directions are pairwise nonparallel, and the unit test direction \(v_q\) differs from both signs of every training direction. It may belong to their full linear span.

The desired conclusion is that every confidence \(1-\delta\) admits \(c_\delta>0\) and an eventual width threshold such that two independent fitted runs satisfy

\[
|f_n(\infty,\sqrt d\,v_q)-\widetilde f_n(\infty,\sqrt d\,v_q)|
\ge c_\delta/\sqrt n
\]

with probability at least \(1-\delta\).

The new mechanism examined here is to condition on a network with one top neuron removed, and then insert a **trained** Gaussian neuron. Conditioning on that cavity leaves its omitted incoming row independent even when the input training span is full. The exact linear response of the rest of the network must be retained. At the endpoint it removes the inserted neuron's contribution at all training inputs. At the test, the surviving response is the sum of an explicit kernel projection residual and a tangent-memory term. Neither term can currently be shown to prevent cancellation under the full contract.

This is a different obstruction from the finite-oracle source-span projection: the cavity Gaussian is independent without any test source-span assumption, but the scalar function of that Gaussian is now a compensated nonlinear training response, rather than a fixed weighted activation.

## 1. The cavity and its trained Gaussian probe

Delete one neuron from hidden layer \(L\), including its readout coordinate. Keep the original width \(n\) in every variance, loss-derived factor, and output denominator. Write the retained parameters in Euclidean mobility coordinates as

\[
\xi=\bigl(W^{(1)}/\sqrt n,W^{(2)},\ldots,
W^{(L-1)},W^{(L)}_{-i,:},w_{-i}/\sqrt n\bigr).
\]

The lower feature at a query is \(h_q(\xi):=h^{(L-1)}(v_q)\in\mathbb R^n\). The cavity prediction is

\[
F_q(\xi)=\frac1n w_{-i}^{\top}
\phi_L\bigl(W^{(L)}_{-i,:}h_q(\xi)\bigr).
\]

For training samples write \(F_a=F_{v_a}\), \(r_a=F_a-y_a\), and
\(\mathcal L_c(\xi)=m^{-1}\sum_a r_a^2\). Thus the cavity flow is exactly

\[
\dot\xi=-\nabla\mathcal L_c(\xi)
=-\frac2m\sum_a r_a\nabla F_a.
\tag{1}
\]

On its fitting event the cavity is global, has exponentially decaying residuals, and converges exponentially in these parameters; this is the rectangular-cavity assertion of the supplied fitting lemma. Throughout the finite-width argument below, fix one successful cavity initialization. Its entire path is then deterministic.

Let \(g\sim N(0,I_n)\) be independent of this cavity. Define an incoming row \(u(t)\in\mathbb R^n\) and a readout scalar \(a(t)\) by

\[
\begin{aligned}
u(0)&=g/\sqrt n,&a(0)&=0,\\
\dot a&=-\frac2m\sum_b r_b\phi_L(u^\top h_b),\\
\dot u&=-\frac2{nm}\sum_b r_ba\phi_L'(u^\top h_b)h_b.
\end{aligned}
\tag{2}
\]

The probe trains both its incoming row and its readout, using the cavity's actual evolving features and residuals. It does not feed back into the cavity at this stage. Define its unnormalized contribution at every query by

\[
b_q(t,g):=a(t,g)\phi_L\bigl(u(t,g)^\top h_q(\xi(t))\bigr).
\tag{3}
\]

For fixed width, (2) is global and its parameters converge exponentially. Indeed the fitting tube bounds \(\|h_b\|\), while the linear-growth activation bound gives, with a finite cavity-dependent constant \(C\),

\[
\frac d{dt}\bigl(1+|a|/\sqrt n+\|u\|\bigr)
\le C\rho(t)\bigl(1+|a|/\sqrt n+\|u\|\bigr),
\qquad \rho=\|r\|/\sqrt m.
\]

Use upper derivatives at zeros of the norms. Since \(\int_0^\infty\rho<\infty\), integration bounds the probe parameters. The right-hand sides of (2) are then bounded by a constant times the exponentially decaying \(\rho\), giving convergence with the same type of exponential tail. All constants in this paragraph may depend on width and on the fixed cavity and root. No uniform-in-width moment assertion is inferred.

## 2. Exact finite-time multiplicity derivative

Introduce a real multiplicity parameter \(\mu\). The retained-plus-probe predictor is

\[
F_q(\xi_\mu)+\frac\mu n
a_\mu\phi_L\bigl(u_\mu^\top h_q(\xi_\mu)\bigr).
\tag{4}
\]

The retained coordinates follow Euclidean gradient flow for the squared training loss of (4). The probe equations retain the factors in (2), using the residual of (4). At \(\mu=1\), this is exactly the full width-\(n\) canonical flow. At \(\mu=0\), it is precisely (1)–(2). For positive \(\mu\), the same equations can also be obtained by giving the probe incoming row and readout the multiplicities' compensating mobilities \(1/\mu\) and \(n/\mu\). This family is only a differentiation device; its intermediate members are not substituted for the target network.

For every fixed finite time, ordinary differentiation of this smooth finite-dimensional ODE is justified on a neighborhood of \(\mu=0\). Set

\[
V(t,g):=n\,\partial_\mu\xi_\mu(t)\big|_{\mu=0},
\qquad j_q(t):=\nabla F_q(\xi(t)).
\]

In \(\nabla b_a\), the derivative is with respect to \(\xi\) while holding the current probe values \(u,a\) fixed. Differentiating the retained equation gives exactly

\[
\dot V=-D^2\mathcal L_c(\xi(t))V
-\frac2m\sum_a\bigl(b_a j_a+r_a\nabla b_a\bigr),
\qquad V(0)=0.
\tag{5}
\]

The multiplicity factor in (4) is the reason derivatives of \(u_\mu,a_\mu\) do not occur in the forcing of (5). Those derivatives are multiplied by \(\mu=0\). The derivative of the predictor itself is

\[
I_q(t,g):=
n\,\partial_\mu f_{\mu}(t,\sqrt d\,v_q)\big|_{\mu=0}
=b_q(t,g)+j_q(t)^\top V(t,g).
\tag{6}
\]

Equations (2), (5), and (6) preserve the full training response. Dropping the second term of (6) would change the object being studied.

There is a useful initial check. Since \(a(0)=0\), both \(b_q(0)\) and \(\nabla b_a(0)\) vanish, so \(V(0)=\dot V(0)=0\). Consequently

\[
\dot I_q(0,g)=\frac2m
\phi_L\bigl(g^\top h_q(0)/\sqrt n\bigr)
\sum_a y_a\phi_L\bigl(g^\top h_a(0)/\sqrt n\bigr).
\tag{7}
\]

Whenever the initialized augmented lower-feature Gram is positive definite, this scalar has strictly positive Gaussian variance. To verify this directly, a variance-zero assertion would make
\(\phi_L(z_q)\sum_a y_a\phi_L(z_a)\) constant for every real \((z_1,\ldots,z_m,z_q)\). Choose training values for which the nonzero-label sum is nonzero, and vary \(z_q\), contradicting nonconstancy. The supplied nonparallel initialization theorem provides the required full rank almost surely at adequate finite width. Thus the cavity influence starts with a nondegenerate random derivative. This is not yet an endpoint statement.

## 3. The endpoint response exists and cancels all training contributions

Let \(J(t)\in\mathbb R^{m\times\dim\xi}\) have rows \(j_a(t)^\top\). The Hessian in (5) is

\[
D^2\mathcal L_c
=\frac2mJ^\top J+\frac2m\sum_a r_aD^2F_a.
\tag{8}
\]

All coefficients in (5) converge exponentially at fixed width. This follows from the exponential convergence of \(\xi,u,a\), analyticity of the finite network on the real axis, and compactness of their bounded trajectories. In particular, with a subscript \(\infty\) denoting the limit,

\[
A_\infty:=\frac2mJ_\infty^\top J_\infty,
\qquad
c_\infty:=\frac2mJ_\infty^\top b_\infty
\]

are the limiting linear generator and forcing, where
\(b_\infty=(b_1(\infty),\ldots,b_m(\infty))^\top\).
The readout block of \(J_\infty\) contains the cavity training feature matrix divided by \(\sqrt n\). The fitting Gram bound therefore makes
\(K_\infty:=J_\infty J_\infty^\top\) strictly positive definite.

**Finite-width endpoint-response lemma.** The solution of (5) converges, and

\[
J_\infty V_\infty=-b_\infty.
\tag{9}
\]

**Proof.** Define
\(V_*=-J_\infty^\top K_\infty^{-1}b_\infty\), so
\(A_\infty V_*=-c_\infty\). For \(Z=V-V_*\), equation (5) has the form

\[
\dot Z=-A_\infty Z+E(t)Z+d(t),
\qquad \|E(t)\|+\|d(t)\|\le C e^{-\alpha t}
\]

for fixed finite constants \(C,\alpha>0\). The semigroup of the symmetric positive-semidefinite \(A_\infty\) has norm at most one. Duhamel's formula and the integral Gronwall inequality therefore bound \(Z\) on the whole half-line. Let \(P_0\) be the orthogonal projector onto \(\ker J_\infty\). The derivative
\(P_0\dot Z=P_0(EZ+d)\) is integrable, so \(P_0Z\) converges. On the complementary subspace, all eigenvalues of \(A_\infty\) are positive. Its exponentially stable semigroup convolved with \(EZ+d\), which tends to zero exponentially, tends to zero. Hence \((I-P_0)Z\to0\). It follows that \(V_\infty-V_*\in\ker J_\infty\), proving (9). ∎

This proves the limit of the finite-time multiplicity derivative. It does not assert an unproved interchange of \(\partial_\mu\) and the fitted limit of the full multiplicity family.

By (6) and (9), every training response vanishes:

\[
I_a(\infty,g)=0\qquad(1\le a\le m).
\tag{10}
\]

Thus a nondegenerate random direct term \(b_a\) can be completely removed by the fitted response. Independence of the cavity root and positive variance of that direct term do not establish endpoint variability.

For the test define \(k_q:=J_\infty j_q(\infty)\in\mathbb R^m\). The exact surviving response is

\[
I_q(\infty,g)=b_q(\infty,g)
-k_q^\top K_\infty^{-1}b_\infty(g)
+j_q(\infty)^\top P_0V_\infty(g).
\tag{11}
\]

The final term is an actual history contribution. Integrating the projection of (5), and using (8), gives its explicit convergent formula

\[
P_0V_\infty=-\frac2m\int_0^\infty\sum_a
\left[
P_0j_a\bigl(j_a^\top V+b_a\bigr)
+r_aP_0\bigl(D^2F_aV+\nabla b_a\bigr)
\right]dt.
\tag{12}
\]

Here \(P_0j_a(t)\to0\) exponentially, and the other factor in its first term is bounded; the second term has exponentially decaying \(r_a\). This verifies convergence without treating the training history as a finite-rank object. Equations (11)–(12) hold for an in-span or an off-span test alike.

The conditional variance used below is well defined. At each fixed successful cavity and width, the probe bound obtained from (2) is at most a constant times \(1+\|g\|\). Thus \(b_a\) and \(\nabla b_a\) have at most quadratic growth in \(g\). The preceding stable/neutral decomposition of (5) then bounds \(V_\infty\), and hence \(I_q(\infty,g)\), by a cavity-dependent constant times \(1+\|g\|^2\). Gaussian fourth moments give square integrability. This again supplies no width-uniform lower bound.

## 4. What this does and does not resolve

The cavity construction resolves one conditioning problem: \(g\) remains an independent standard Gaussian after exposing the whole cavity. It does **not** turn (11) into the scalar projected-Gaussian form of the authorized endpoint proof. The trained quantities \(u,a,V\) all depend on \(g\). Consequently its coefficients cannot be treated as fixed when applying that scalar lemma.

The smallest nondegeneracy question supplied by this construction is whether, for the actual successful random cavities,

\[
\lim_{\eta\downarrow0}\limsup_{n\to\infty}
\Pr\left\{
\operatorname{Var}_{g}\bigl(I_q(\infty,g)\mid\text{cavity}\bigr)<\eta
\right\}=0.
\tag{13}
\]

This statement is **open**, and is not by itself sufficient for the target theorem. It controls an infinitesimal multiplicity response, whereas the actual network inserts a full neuron. A width-accurate insertion or replacement expansion is a separate obligation. The supplied cavity estimates give coordinate and state localization but do not state a remainder small enough to identify the endpoint prediction with an average of these responses at fluctuation scale.

Moreover, one independent inserted neuron contributes at the natural output scale \(n^{-1}\). A lower bound at \(n^{-1/2}\) requires a collective fluctuation argument over order \(n\) roots, or a Gaussian derivative theorem for the full endpoint map. Fixed-count cavity independence does not supply that argument automatically. Nonzero variance alone would also be insufficient for the requested small-ball probability.

A concrete alternative completion package would use the full endpoint map conditioned on the lower-layer initialization, with all top incoming rows represented by standard Gaussian roots. For a smooth extension of
\(G_n=\sqrt n f_n(\infty,\sqrt d\,v_q)\) to those roots, it would suffice to prove a positive conditional variance lower bound, a bounded gradient norm, and a Hessian operator norm tending to zero, on conditioning events of arbitrarily high probability, with any extension error controlled. Section 3 of the supplied projected-scalar module then gives the required Gaussian small-ball bound. None of these uniform derivative and variance bounds for the full fitted endpoint has been established here. The finite-width convergence argument above deliberately does not disguise width-dependent constants as such bounds.

The first-round bottlenecks are therefore:

1. Show that the direct, projection, and tangent-memory terms in (11) cannot cancel for the specified nonparallel test, quantitatively under the original label cap.
2. Transfer that trained-probe response to the actual collective width-scale fluctuation, with a remainder and an anti-concentration argument strong enough for \(n^{-1/2}\).

Initial augmented Gram positivity proves (7)'s variance statement but does not settle the first bottleneck. The real fitting displacement bounds are absolute bounds, whereas the fixed test's initial innovation may be arbitrarily small as its direction approaches a training direction. They provide no relative estimate for the three-term cancellation in (11). Analytic dependence at finite time also does not prevent an influence that is nonconstant initially from vanishing at the fitted limit, as (10) demonstrates inside the exact model.

No counterexample to the requested full-span endpoint theorem is obtained. The route should be recorded as **open, with an exact new response formula**. It should be reopened for expansion only with a concrete noncancellation estimate for (11), a full-insertion fluctuation identity, or corresponding endpoint Gaussian-derivative bounds. Restating initial rank or treating the probe's trained coefficients as fixed does not advance this route.
