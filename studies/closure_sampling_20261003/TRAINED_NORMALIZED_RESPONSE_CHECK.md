# Independent reconstruction of the trained first-gate response bound

2026-10-04. **Verdict: PASS for the stated two-hidden-layer, one-training-input
first-gate estimate, including its all-time whole-sphere and physical-time
integrated forms.** No substantive correction to the frozen candidate is
required. This verdict does not establish the upper-layer product, general
training data, arbitrary depth, or an autonomous compression theorem.

The sole scientific input was the complete
TRAINED_NORMALIZED_RESPONSE_ROUTE.md, verified at SHA-256

4784c003ae8e449b945939d38fae4fea188d816f264d4f60c927f10a70bdd923.

This check reconstructs the displayed argument from that source and elementary
identities. No linked input, sibling check, study history, prior-study
source, or new coordinator finding was read or used. The canonical-notation,
neural-network, rigorous-proof, and research-audit instructions already read
remained current. Only this assigned report was written; no experiment,
Git mutation, README edit, or candidate edit was made.

## 1. Setup and exact activation normalization

The reference has width \(n\), two hidden layers, and one unit training
input. An orthogonal change of input coordinates puts that input at
\(e_1\) without changing the independent standard Gaussian law of the
initialized first-weight rows. Write \(A=[a,G]\), with
\(a\in\mathbb R^n\) and \(G\in\mathbb R^{n\times(d-1)}\).
The prediction and loss are

\[
f(v)=n^{-1}w^\top\phi(W\phi(Av)),\qquad
\mathcal L=r^2,\qquad r=f(e_1)-y.
\tag{C1}
\]

Here \(W_{ij}(0)\) are independent \(N(0,1/n)\), independent of \(A(0)\),
and \(w(0)=0\). Vector RMS means
\(\|q\|_{2,n}=\|q\|_2/\sqrt n\).

Set \(a_\phi=\sqrt{\pi\sqrt3/2}\), solely to check the candidate's
activation:
\[
b_0=\sqrt{1-\pi/(2\sqrt3)},\qquad
\phi(x)=b_0+a_\phi\operatorname{erf}(x/\sqrt2).
\tag{C2}
\]
The number under the square root is positive. For a standard normal \(Z\),
\(\Phi(Z)\) is uniform on \((0,1)\), where \(\Phi\) is its distribution
function. Since \(\operatorname{erf}(x/\sqrt2)=2\Phi(x)-1\), the erf term
has mean zero and second moment \(1/3\). Thus
\[
\mathbb E\phi(Z)^2=b_0^2+a_\phi^2/3=1.
\tag{C3}
\]
Differentiation gives
\[
\phi'(x)=S e^{-x^2/2},\qquad
\phi''(x)=-Sxe^{-x^2/2},\qquad S=3^{1/4}.
\]
The maximum of \(|x|e^{-x^2/2}\) is \(e^{-1/2}\). Therefore the candidate's
\[
B=b_0+a_\phi,\qquad T=H=S e^{-1/2}
\]
indeed bound \(|\phi|\), \(|\phi''|\), and \(|x\phi'(x)|\), respectively,
while \(S\) bounds \(|\phi'|\).
Also \(\mathbb E e^{-Z^2}=1/\sqrt3\), so
\(\mathbb E\phi'(Z)^2=S^2/\sqrt3=1\).
The nonzero mean \(b_0\) is retained throughout. No centered-activation
assumption has been inserted.

## 2. Physical gradient factors and the residual clock

At the training input put
\[
h^{(1)}=\phi(a),\qquad z^{(2)}=Wh^{(1)},\qquad
h^{(2)}=\phi(z^{(2)}),\qquad
\delta=\phi'(z^{(2)})\odot w,\qquad b=W^\top\delta.
\]
For \(F=nf(e_1)\) and mobility coordinates
\(\Theta=(A,\sqrt nW,w)\), direct differentiation gives
\[
\nabla_A F=(\phi'(a)\odot b)e_1^\top,\qquad
\nabla_{\sqrt nW}F=\delta h^{(1)\top}/\sqrt n,\qquad
\nabla_wF=h^{(2)}.
\tag{C4}
\]
The original mobilities \((n,1,n)\) are equivalent to
\(\dot\Theta=-2r\nabla_\Theta F\). Consequently
\[
\begin{aligned}
\dot a&=-2r\,\phi'(a)\odot b,&
\dot G&=0,\\
\dot W&=-2r\,\delta h^{(1)\top}/n,&
\dot w&=-2r\,h^{(2)}.
\end{aligned}
\tag{C5}
\]
There is no missing factor of \(n\) in the response or clock.
In particular
\[
\dot r=-2r\,\|\nabla_\Theta F\|_2^2/n=-2\mathcal K r,
\]
where the three gradient blocks in (C4) give exactly
\[
\mathcal K=\|h^{(2)}\|_{2,n}^2
+\|\delta\|_{2,n}^2\|h^{(1)}\|_{2,n}^2
+\|\phi'(a)\odot b\|_{2,n}^2.
\tag{C6}
\]

The transformation \(y\mapsto-y,\ w\mapsto-w\) leaves the \(a,W\) paths
unchanged and negates \(r,\delta,b\), so the restriction \(y=Y>0\) loses
no absolute-value estimate. Then \(r(0)=-Y\) and the scalar equation
keeps \(r<0\) at each finite existence time. The increasing clock
\(\tau(t)=2\int_0^t|r(s)|\,ds\) therefore has positive derivative.
Dividing (C5) by that derivative gives the candidate's three primed
equations. They are clock derivatives, not physical-time derivatives.
The zero-label case is separately stationary.

## 3. Fitting event, strict margins, and global continuation

The initialized event is precisely
\[
\|W(0)\|_{\rm op}\le8,\qquad
\|h^{(2)}(0)\|_{2,n}\ge1/\sqrt2.
\tag{C7}
\]
Let \(K=9\), \(C_2=B^2+K^2S^2\), and
\[
c=\min\{1,(16SB^2)^{-1/2},(64S^2BC_2)^{-1/2}\}.
\tag{C8}
\]
Stop before \(\|W\|_{\rm op}\) reaches \(K\) or
\(\|h^{(2)}\|_{2,n}\) falls to \(1/2\).
Equation (C6) gives \(|r(t)|\le Ye^{-t/2}\) and \(\tau(t)\le4Y\)
on that stopped interval.

Because \(w'=h^{(2)}\) and \(|h_i^{(2)}|\le B\),
\[
\|w\|_\infty\le B\tau,\quad
\|\delta\|_{2,n}\le SB\tau,\quad
\|b\|_{2,n}\le KSB\tau,\quad
\|W'\|_{\rm op}\le SB^2\tau.
\tag{C9}
\]
The exact identity
\[
(z^{(2)})'=\delta\|h^{(1)}\|_{2,n}^2
+W[\phi'(a)^2\odot b]
\]
therefore gives
\(\|(z^{(2)})'\|_{2,n}\le SBC_2\tau\). Integrating yields
\[
\|W-W(0)\|_{\rm op}\le8SB^2Y^2\le1/2,\qquad
\|h^{(2)}-h^{(2)}(0)\|_{2,n}
\le8S^2BC_2Y^2\le1/8.
\tag{C10}
\]
Both margins strictly improve the stops:
\(8+1/2<9\) and \(1/\sqrt2-1/8>1/2\).

For completeness, the unlisted first-weight bound needed for continuation
also follows directly:
\[
\|a'\|_{2,n}\le KS^2B\tau,\qquad
\|a(\tau)-a(0)\|_{2,n}\le\tfrac12KS^2B\tau^2.
\tag{C11}
\]
At each finite width these bounds keep all evolving coordinates bounded.
The activation is smooth, so the finite-dimensional vector field is locally
Lipschitz. The solution extends globally. All clock derivatives have
integrable norms over the finite interval
\([0,\tau(\infty))\), giving limits of \(a,W,w\). The strict bounds
survive at the endpoint, and residual decay gives exact fitting there.
Equation (C11) makes explicit a consequence already sufficient for the
candidate's continuation argument; it changes no hypothesis or constant.

Event (C7) is independent of \(G\) and has probability tending to one.
The bounded first-layer activation gives convergence of its empirical
second moment to (C3). Conditional on that layer, the next preactivations
are independent \(N(0,q_1)\), where
\(q_1=\|h^{(1)}(0)\|_{2,n}^2\to1\). Bounded-variable variance estimates
and continuity of the Gaussian expectation give
\(\|h^{(2)}(0)\|_{2,n}^2\to1\) in probability. For \(W(0)\), the
two \(1/4\)-net argument gives exactly the stated failure bound
\(2\exp[-(8-2\log9)n]\). No conditional law after training is used
in this initialization argument.

## 4. Carrier variation and surviving independence

Differentiating \(b=W^\top\delta\) along the actual clock path gives
\[
b'=W'^\top\delta+W^\top\delta',\qquad
\delta'=\phi'(z^{(2)})\odot h^{(2)}
+\phi''(z^{(2)})\odot(z^{(2)})'\odot w.
\tag{C12}
\]
The second term uses the genuine coordinate bound on \(w\) from (C9).
There is no assumed coordinate bound on \(b\).
Term by term,
\[
\|\delta'\|_{2,n}\le SB+TSB^2C_2\tau^2,\qquad
\|W'^\top\delta\|_{2,n}\le S^2B^3\tau^2.
\]
Hence, with
\[
D=S^2B^3+KTSB^2C_2,\qquad \tau_*=4Y,
\]
the candidate's constants are correct:
\[
B_1=KSB\tau_*,\qquad
V_b=KSB\tau_*+D\tau_*^3/3.
\tag{C13}
\]
They bound \(\sup_\tau\|b(\tau)\|_{2,n}\) and
\(\int_0^{\tau(\infty)}\|b'(\tau)\|_{2,n}\,d\tau\), respectively.

Equations (C5) show that \(G\) never enters the closed training equations
for \(a,W,w\). Conditional on \((a(0),W(0),y)\), uniqueness fixes their
entire path, its limiting clock, and \(b(\tau)\), while \(G\) retains its
independent standard Gaussian entries. The event (C7) is measurable in
these conditioned variables. Thus the conditioning does not select a
Gaussian matrix using its own trajectory-dependent event.

## 5. Exact whole-sphere response and the all-time conditional estimate

For \(\|v\|=\|u\|=1\), direct use of (C4) gives
\[
J^{(1)}(v,u)=Au=a u_1+G u_\perp,\qquad
R^{(1)}(v)=v_1\phi'(a)\odot b.
\tag{C14}
\]
The response uses the gradient of \(nf(e_1)\), exactly as defined in
the candidate. Applying \(|\phi''|\le T\), \(|a_i\phi'(a_i)|\le H\),
\(|v_1|,|u_1|,\|u_\perp\|\le1\), and the Frobenius bound for a matrix
acting on a unit vector gives
\[
\sup_{v,u}
\|\phi''(Av)\odot R^{(1)}(v)\odot J^{(1)}(v,u)\|_{2,n}
\le T[H\|b\|_{2,n}+S\|\operatorname{diag}(b)G\|_F/\sqrt n].
\tag{C15}
\]
The query gate \(\phi''(Av)\) depends on \(G\), but only its deterministic
bound \(T\) is used. No Gaussian independence of that gate is asserted.
The bound is simultaneous over the sphere and all unit directions,
without a discretization.

The clock path has \(b(0)=0\) and integrable derivative, so it extends
absolutely continuously to its endpoint. For each fixed matrix \(G\),
\[
\sup_{\tau\le\tau(\infty)}
\|\operatorname{diag}(b(\tau))G\|_F/\sqrt n
\le\int_0^{\tau(\infty)}
\|\operatorname{diag}(b'(\tau))G\|_F/\sqrt n\,d\tau.
\tag{C16}
\]
Conditionally the interval and integrand coefficients are fixed.
For every such coefficient vector \(q\),
\[
\mathbb E_G[\|\operatorname{diag}(q)G\|_F^2/n]
=(d-1)\|q\|_{2,n}^2.
\tag{C17}
\]
Minkowski's integral inequality in conditional \(L^2(G)\), applied to
the right-hand side of (C16), gives the bound
\(\sqrt{d-1}V_b\). Its hypotheses hold because (C13) bounds the
integral of these \(L^2\) norms. Equivalently, Tonelli and the
two-factor Cauchy--Schwarz inequality give the same result directly.
The continuous supremum is measurable and includes the limiting time.

Markov applied to its square proves, for \(0<\eta<1\), conditional
probability at least \(1-\eta\) of the candidate's bound
\[
\sup_{t\in[0,\infty],\,v,u}
\|\phi''(z^{(1)}(t,v))\odot R^{(1)}(t,v)
\odot J^{(1)}(t,v,u)\|_{2,n}
\le T[HB_1+S\sqrt{d-1}\,V_b/\sqrt\eta].
\tag{C18}
\]
This holds conditional on each training initialization in (C7), up to
the usual null sets of a regular conditional law. Integrating over that
event gives probability at least
\((1-\eta)\Pr(\mathrm{C7})\ge1-\eta-o_n(1)\).
When \(d=1\), \(G\) is empty and the stochastic term is zero.

Substituting \(\tau_*=4Y\) in (C13), and using \(Y^3\le c^2Y\), gives
exactly
\[
C_\eta=4THKSB+
\frac{TS\sqrt{d-1}}{\sqrt\eta}
\left(4KSB+\frac{64}{3}Dc^2\right).
\tag{C19}
\]
Thus the bound is \(C_\eta Y\) with no width-dependent coefficient.
Finally (C5), (C14) give
\(\dot z^{(1)}(v)=-2rR^{(1)}(v)\). Integrating (C18) against
\(2|r|\,dt=d\tau\) proves the physical forcing bound
\[
\int_0^\infty\sup_{v,u}
\|\phi''(z^{(1)})\odot\dot z^{(1)}\odot J^{(1)}\|_{2,n}\,dt
\le4C_\eta Y^2.
\tag{C20}
\]
This is an all-time trained estimate, not a fixed-time Gaussian
expectation subsequently union-bounded over time.

## 6. Remaining identities and exact scope

The candidate's equations for the second-layer quantities reconstruct as
\[
\begin{aligned}
R^{(2)}(v)
&=\delta\langle h^{(1)},h^{(1)}(v)\rangle_n
+v_1W[\phi'(Av)\odot\phi'(a)\odot b],\\
J^{(2)}(v,u)&=W[\phi'(Av)\odot Au].
\end{aligned}
\tag{C21}
\]
The direct \(W\) gradient in (C4) supplies the normalized pairing in
the first line; the \(A\) gradient supplies its second term. Differentiating
the second line in time gives exactly the candidate's three-term tangent
equation. Bound (C18) controls its middle curvature term after multiplication
by \(\|W\|_{\rm op}\le K\). It supplies no separate bound for the product
\(\phi''(z^{(2)}(v))\odot R^{(2)}(v)\odot J^{(2)}(v,u)\).

Separate RMS bounds cannot justify that missing multiplication: two
vectors \(\sqrt n e_1\) have unit RMS, while their componentwise product
has RMS \(\sqrt n\). The candidate appropriately leaves the product of
its two trained images under \(W\) unresolved. Its higher-depth caution is
also correct: differentiating an interior gate produces a backward carrier
in place of the readout \(w\), and (C9) supplies no coordinate bound for
that carrier. Neither statement is an impossibility claim.

For the centered joint Gaussian pair used only in the candidate's final
comparison, write
\(J=(c_J/q)Z+U\), with \(U\) independent of \(Z\) and
\(\mathbb E U^2=v_J-c_J^2/q\). Substitution of
\(\mathbb E e^{-Z^2}=(1+2q)^{-1/2}\) and
\(\mathbb E Z^2e^{-Z^2}=q(1+2q)^{-3/2}\) gives
\[
\mathbb E[\phi'(Z)^2J^2]
=\frac{\sqrt3}{\sqrt{1+2q}}v_J
-\frac{2\sqrt3}{(1+2q)^{3/2}}c_J^2.
\tag{C22}
\]
This includes zero conditional variance of \(U\); only \(q>0\) is needed.
At \(q=1\) it is \(v_J-2c_J^2/3\). Direct differentiation of the finite
empirical tangent energy gives the candidate's equation (30), including
its factor \(-4/m\) after inserting the physical residual force.
The source does not use (C22) for a trained non-Gaussian empirical law
and does not claim a sign for that residual-weighted term.

The reconstructed result is therefore precisely: a fixed explicit
**bounded nonlinear** activation with both Gaussian moments equal to one,
two hidden layers, one training example, sufficiently small explicit label,
all real query directions, all physical times and the fitted endpoint,
with confidence \(1-\eta-o_n(1)\). It does not itself cover general
unbounded activations such as normalized GELU. It validates one needed
mixed product without a neuron maximum or logarithmic width loss.

No source correction is required. The first-weight continuation estimate
(C11) and the conditional-integrability details in Section 5 can be added
for exposition, but the candidate already contains the inequalities from
which they follow. The larger compression and polynomial-depth targets
remain open exactly as the candidate states.
