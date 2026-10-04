# Exact loss matching in the actual one-sample dense network

This bounded calculation complements LOSS_MATCHED_VARIATIONS.md. It concerns the canonical dense network itself, not a response-memory closure or a frozen-kernel replacement. Its purpose is to test cancellation, not to claim a width rate.

## 1. Exact path and speed separation

Take one normalized training input \(v=x_1/\sqrt d\), \(\|v\|_2=1\), label \(y>0\), zero initial readout, and the manuscript's dense gradient flow. Use smooth activations for response calculations below. Let \(\theta\) contain all parameter blocks and let \(D\) be the positive block mobility matrix, with first and readout mobilities \(n\) and hidden mobilities one. Define
\[
K_\theta(x,x_1)=\nabla_\theta f_\theta(x)^\top
                         D\nabla_\theta f_\theta(x_1).
\]
On the small-label fitting event, \(K_\theta(x_1,x_1)\) stays bounded below. With \(u=f_\theta(x_1)\),
\[
\dot u=2(y-u)K_\theta(x_1,x_1)>0,\qquad 0\le u<y.
\]
The unique time at training prediction \(u\) is therefore also the unique time at training loss \((y-u)^2\). The parameter curve at that loss satisfies exactly
\[
\frac{d\theta}{du}
 =\frac{D\nabla_\theta f_\theta(x_1)}{K_\theta(x_1,x_1)}.
\tag{1}
\]
The label magnitude no longer occurs in the vector field. It determines how far along this initialized curve training proceeds. This statement is specific to a single scalar residual; it does not apply to several independent residual directions.

For any query \(x\), let \(q(u,x)=f_{\theta(u)}(x)\). Then
\[
\frac{\partial q}{\partial u}(u,x)
 =\frac{K_{\theta(u)}(x,x_1)}{K_{\theta(u)}(x_1,x_1)},\qquad
q(y,x)=\int_0^y
 \frac{K_{\theta(u)}(x,x_1)}{K_{\theta(u)}(x_1,x_1)}\,du.
\tag{2}
\]
The endpoint formula holds when the fitted parameter limit exists, as in the manuscript's fitting regime. It is an exact history identity, not a closed formula for the selected function: its kernel is the actual moving dense tangent kernel.

For a smooth initialization parameter \(\varepsilon\), differentiate the ratio in (2) at fixed \(u\). Writing \(A=K(x,x_1)\), \(B=K(x_1,x_1)\), \(R=A/B\), with derivatives including the variation of the loss-matched state,
\[
\partial_\varepsilon R
 =\frac{\partial_\varepsilon A-R\partial_\varepsilon B}{B},
\quad
\partial_\varepsilon^2R
 =\frac{\partial_\varepsilon^2 A-R\partial_\varepsilon^2 B
       -2(\partial_\varepsilon R)(\partial_\varepsilon B)}{B}.
\tag{3}
\]
Common multiplicative changes in \(A,B\) cancel. Changes in their ratio do not.

## 2. Hidden feedback remains in the loss-matched path

Specialize to two tanh layers. At initialization write
\[
a=W_0^{(1)}v,\quad h=\tanh a,\quad s=\operatorname{sech}^2a,
\quad W=W_0^{(2)},\quad z=Wh,\quad g=\tanh z,
\]
\[
Q=\frac{\|g\|_2^2}{n}>0,\qquad
\psi(z)=\tanh z\odot\operatorname{sech}^2z,\qquad
T=W^\top\psi(z).
\]
Differentiating (1) at \(u=0\), where the stored readout is zero, gives
\[
\left.\frac{dw}{du}\right|_0=\frac gQ,\qquad
\left.\frac{dW^{(1)}}{du}\right|_0
=\left.\frac{dW^{(2)}}{du}\right|_0=0,
\]
\[
\left.\frac{d^2W^{(1)}}{du^2}\right|_0
 =\frac{(s\odot T)v^\top}{Q^2},\qquad
\left.\frac{d^2W^{(2)}}{du^2}\right|_0
 =\frac{\psi(z)h^\top}{nQ^2}.
\tag{4}
\]
Indeed \(d\delta^{(2)}/du|_0=\psi(z)/Q\), and the first response is its transpose return multiplied by \(s\). Every derivative of \(1/K\) multiplying an initially zero hidden velocity drops out. Equivalently divide the exact physical-time accelerations in FIRST_FEEDBACK.md by \(\dot u(0)^2=(2yQ)^2\).

These are second derivatives in training progress, not second initialization sensitivities. They show directly that matching loss removes residual speed while preserving the initialized-matrix return \(T\). Varying (4) still requires derivatives of that return; for example
\[
DT=(DW)^\top\psi(z)
 +W^\top\operatorname{diag}(\psi'(z))
       \{(DW)h+W\operatorname{diag}(s)Da\}.
\tag{5}
\]
There is no algebraic elimination of matrix reuse.

## 3. Actual dense first- and second-response cancellation test

The following explicit initialization tests a proposed algebraic cancellation. It is not a width lower bound or a Gaussian-probability claim. Set \(n=2\), \(W_0^{(2)}=B I_2\) with \(B>0\), first preactivations
\[
a(\varepsilon)=(a_1,a_2+\varepsilon),\qquad a_1,a_2>0,
\]
and \(w(0)=0\) for every \(\varepsilon\). Such preactivation perturbations are realized by perturbing \(W_0^{(1)}\) in the training direction. Put
\[
g(\varepsilon)=(g_1,g_2(\varepsilon)),\quad
g_1=\tanh(B\tanh a_1),\quad
g_2(\varepsilon)=\tanh(B\tanh(a_2+\varepsilon)),\quad
S=g_1^2+g_2(0)^2.
\]
At the common initial loss,
\[
\partial_u w(0;\varepsilon)
  =\frac{2g(\varepsilon)}{\|g(\varepsilon)\|_2^2}.
\]
Let \(P=I-g(0)g(0)^\top/S\) project readout variations perpendicular to the initial training velocity, and let \(e_2=(0,1)\). Holding this base projection fixed, direct differentiation gives
\[
P\partial_\varepsilon\partial_u w(0;0)
 =\frac{2g_2'(0)}S\,Pe_2\ne0,
\tag{6}
\]
\[
P\partial_\varepsilon^2\partial_u w(0;0)
 =\left(\frac{2g_2''(0)}S
           -\frac{8g_2(0)g_2'(0)^2}{S^2}\right)Pe_2\ne0.
\tag{7}
\]
Here \(g_2'(0)>0\) and \(g_2''(0)<0\): tanh has positive first derivative and negative second derivative on the positive half-line, and both arguments in the composition are positive. Also \(Pe_2\ne0\) since \(g_1>0\).

Smooth dependence then gives nonzero transverse first and second initialization responses of \(w(u;\varepsilon)\) at sufficiently small common \(u>0\), with leading terms \(u\) times (6) and (7). The physical initial trajectory velocity has only a readout component parallel to \(g(0)\). Thus these displayed components survive genuine loss matching and removal of that speed direction.

This does not prove harmful amplification or a slow width rate. It excludes a universal cancellation claim already inside the nonlinear canonical dense model, with the zero-readout constraint preserved in the initialization family.

## 4. A conditional same-time transfer, separate from matching loss

For two fitted one-sample curves indexed \(j=1,2\), suppose their tangent speeds \(\gamma_j(u)=K_j(u;x_1,x_1)\) satisfy
\[
0<\lambda\le\gamma_j(u)\le\Lambda,\qquad
\sup_{0\le u\le y}|\gamma_1(u)-\gamma_2(u)|\le\eta\lambda,
\quad 0<\eta\le\tfrac12.
\]
Their hitting times are
\[
t_j(u)=\int_0^u\frac{dv}{2(y-v)\gamma_j(v)}.
\]
The ratio \(\gamma_2/\gamma_1\) belongs to \([1-\eta,1+\eta]\), so
\[
(1-\eta)t_2(u)\le t_1(u)\le(1+\eta)t_2(u).
\]
Inverting these increasing functions yields
\[
u_2(t/(1+\eta))\le u_1(t)\le u_2(t/(1-\eta)).
\]
Since \(u_2'(t)\le2y\Lambda e^{-2\lambda t}\), the difference between these two bounding values is at most
\[
2y\Lambda\frac{2\eta t}{1-\eta^2}
                 e^{-2\lambda t/(1+\eta)}
\le C y(\Lambda/\lambda)\eta
\]
uniformly over all physical time. If in addition the matched query predictions differ by at most \(e_x\) and \(|\partial_u q_2(u,x)|\le B_x\), then
\[
\sup_{t\ge0}|f_1(t,x)-f_2(t,x)|
\le e_x+C B_xy(\Lambda/\lambda)\eta.
\tag{8}
\]
Thus there is no unavoidable late-time clock blowup in this one-sample transfer. Both premises remain quantitative obligations for a finite-to-population comparison. Loss matching alone supplies neither of them.

## Assessment

Pure speed cancels exactly. Transverse first and second responses do not generally cancel, and actual dense hidden feedback survives. This supports investigating weighted transverse sensitivities, but does not turn the existing fixed-control fluctuation estimate into a population rate. All results here are local identities or the explicitly conditional transfer (8).
