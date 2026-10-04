# Current result: the cutoff can be removed, but the strict dense width theorem remains open

The requested statement is an all-time \(C_\delta/\sqrt n\) bound between the **original dense finite network** and its **dense population**, including unseen inputs and the fitted endpoint. This investigation has not proved that statement, nor a slower-than-root lower bound. It has proved the cutoff-removal part of the proposed strategy for a nontrivial structured two-layer setting, and population cutoff removal at every fixed depth.

All results below are internal research results. Their dependencies are the current user-authorized manuscript, maintained notation, and this study's complete derivations. No response-memory clipping result or other study is used as a proof dependency. No numerical experiments were run and the manuscript was not edited.

## Exact object and error

The dense model has hidden features \(h^{(\ell)}=\phi_\ell(z^{(\ell)})\), first preactivation \(z^{(1)}=W^{(1)}x/\sqrt d\), deeper preactivations \(z^{(\ell)}=W^{(\ell)}h^{(\ell-1)}\), and output \(f_n=w^\top h^{(L)}/n\). Every hidden matrix evolves by the manuscript's canonical dense update

\[
\dot W^{(\ell)}=-\frac2{mn}\sum_a r_a\delta_a^{(\ell)}h_a^{(\ell-1)\top}
\quad(\ell\ge2).
\]

The first-layer and readout mobilities are \(n\), and the residual \(r_a=f_n(x_a)-y_a\) is excluded from \(\delta_a^{(\ell)}\). Initial hidden entries have variance \(1/n\), first-layer entries variance one, and \(w(0)=0\). There are no response memories or memory clock in this object.

The population is the Gaussian operator flow constructed in the current manuscript with those same normalizations. For a test probability law \(\mu\) with finite second input moment, write

\[
\|F-G\|_*=
\left(\int\sup_{t\ge0}|F(t,x)-G(t,x)|^2\,d\mu(x)\right)^{1/2}.
\]

All fitting and cutoff-removal statements retain a positive limiting initial readout-feature Gram gap and sufficiently small fixed label RMS \(Y\). Their thresholds do not shrink as width or cutoff grows. When \(Y=0\), all the initialized flows are stationary and the comparison error is zero. Statements dividing by the activity bound below concern \(Y>0\).

## 1. Every fixed depth: population cutoff removal

Take a smooth odd cutoff \(\chi_M\) with

\[
\chi_M(u)=u\ (|u|\le M),\quad
|\chi_M(u)|\le\min(|u|,2M),\quad
|\chi_M(u)-\chi_M(v)|\le|u-v|.
\]

In the auxiliary algorithm, clip each backward carrier before multiplying by its activation derivative. Keep the forward pass and readout update unchanged. Denote its finite and population predictors by \(f_{n,M}\) and \(f_{\infty,M}\).

For every fixed depth and the manuscript's activations with bounded Lipschitz derivative, the auxiliary flow fits exponentially with constants and label threshold independent of \(M\). Its population exists uniquely on common initialized operator spaces, and

\[
\|f_{\infty,M}-f_\infty\|_*\le C_\mu e^{-cM^2}.
\tag{1}
\]

The proof compares true derivative responses with clipped update responses explicitly; it does not assume the clipped updates are gradient flow. The hidden part of the residual matrix is \(O(Y^2)\), so the initial readout Gram gap controls its symmetric part. Learning activity \(\int_0^\infty\rho\,dt\) is finite. The Gaussian population tail contributes an integrable error source, and its \(e^{-cM^2}\) decay absorbs the comparison factor \(e^{CM}\).

Proof and reconstruction: [CUTOFF_REMOVAL_ROUTE.md](CUTOFF_REMOVAL_ROUTE.md), [CUTOFF_REMOVAL_CHECK.md](CUTOFF_REMOVAL_CHECK.md).

## 2. Two hidden layers and orthogonal inputs: finite cutoff inactivity

Suppose additionally

\[
L=2,\qquad \frac{x_a^\top x_b}{d}=\mathbf1_{a=b},
\qquad \phi_1=\tanh,
\]

and \(\phi_2\) is bounded with bounded Lipschitz derivative. This includes tanh in both layers and any fixed number \(m\le d\) of orthogonal training inputs, with arbitrary sufficiently small fixed labels.

Let \(\mathcal G_n\) be the initialized fitting event. If
\(k_a^{(1)}=W^{(2)\top}\delta_a^{(2)}\) is the **actual trained finite backward carrier** and \(S=2Y/\kappa\), then

\[
\Pr\left(\mathcal G_n\cap
 \left\{\sup_{t\ge0}\max_{a,i}|k_{a,i}^{(1)}(t)|>M\right\}\right)
\le Cmn e^{-cM^2/S^2}.
\tag{2}
\]

The top carrier satisfies \(\sup_t\|w(t)\|_\infty\le\|\phi_2\|_\infty S\). Hence, for fixed confidence and a sufficiently large constant,

\[
M(n)=A\sqrt{\log(e+n)}
\quad\Longrightarrow\quad
f_{n,M(n)}(t,x)=f_n(t,x)
\quad\text{for every }t\ge0\text{ and every }x
\tag{3}
\]

except with probability at most \(\delta+\Pr(\mathcal G_n^c)\). Choose \(A\ge1\) also large enough for (1) to be at most \(C_\mu/\sqrt n\). At any fixed confidence, \(\Pr(\mathcal G_n^c)\to0\), as supplied by the manuscript, can be absorbed by taking width sufficiently large. No quantitative population convergence is used to prove (2).

The new finite argument uses the exact coordinate change

\[
p_a=F(z_a^{(1)}),\qquad
F(z)=\frac z2+\frac{\sinh(2z)}4,
\qquad F'(z)=\frac1{\tanh'(z)}.
\]

Orthogonality cancels the first-layer activation derivative in the update of \(p_a\). The resulting equations are uniformly Lipschitz in normalized state differences when driven by a prescribed integrated residual path. The actual residual path may depend on initialization; the proof controls **all** paths with the allowed total variation.

Deleting one first-layer neuron makes the remaining response independent of that neuron's Gaussian matrix column. The effect of deletion on the upper-layer responses is \(O(n^{-1/2})\) in RMS, and its contribution back to the deleted carrier is bounded. A direct Gaussian covering argument over all admissible residual paths then proves (2), including the time supremum. This is a statement about adaptive finite networks, not a population-only tail estimate.

Proof and reconstruction: [FINITE_TAIL_ROUTE.md](FINITE_TAIL_ROUTE.md), [FINITE_TAIL_CHECK.md](FINITE_TAIL_CHECK.md).

## 3. The remaining error is explicit

In the setting of Section 2, choose the above cutoff. With the stated high probability,

\[
\|f_n-f_\infty\|_*
\le
\underbrace{0}_{\text{finite cutoff removal}}
+\underbrace{\|f_{n,M(n)}-f_{\infty,M(n)}\|_*}_{\text{unproved quantitative width comparison}}
+\underbrace{C_\mu/\sqrt n}_{\text{population cutoff removal}}.
\tag{4}
\]

This is a rigorous reduction with two controlled terms. It is not a root-width theorem for the full error.

The missing middle estimate must include both stochastic fluctuations and the difference between the finite-width mean and the population. The manuscript's fixed Gaussian-program limit controls neither at a numerical rate uniform as the time mesh is refined. Even a hypothetical valid bound \(Ce^{CM}/\sqrt n\) for that middle term would yield only \(n^{-1/2+o(1)}\) after substitution; this investigation has not proved that weaker trained dense rate either.

For general data and depth, there is another unresolved step: the finite-network tail bound (2). The coordinate cancellation used above fails for a nondiagonal input Gram, and additional backward layers introduce unbounded carriers into further gates. These are limitations of this proof, not counterexamples to the desired theorem.

## 4. What the bias calculations establish

The first nonlinear forward/adjoint return can be analyzed without an inverse query Gram. Conditional on an independent input vector \(u\), a Gaussian matrix \(W\), and \(z=Wu\), the vector \(W^\top\psi(z)\) is exactly a sample response coefficient times \(u\), plus a projected Gaussian innovation. The coupling error against its correctly centered population counterpart is root width under the moment bounds in the proof. Its second-moment correction is explicitly proportional to \(u_i u_j/n\), hence of order \(1/n\) for the bounded tanh coordinates used here.

For one normalized input and two tanh layers, the third time derivative of the actual dense prediction consequently has \(O(1/n)\) expectation bias and \(O(1/\sqrt n)\) RMS error against its explicit limiting coefficient. Thus the first feedback does **not** force a nonvanishing bias term. Repeated adaptive returns throughout training remain the difficulty.

Derivations: [WIDTH_ROUTE.md](WIDTH_ROUTE.md), [FIRST_FEEDBACK.md](FIRST_FEEDBACK.md). Conditional moment-to-cutoff transfer, requiring only finite-network time-marginal moments instead of time maxima, is in [THREE_ERROR_REASSEMBLY.md](THREE_ERROR_REASSEMBLY.md).

The next decisive result would be a quantitative repeated-query comparison, including expectation bias, with constants uniform over the finite interval of total learning activity. It would complete (4) in the structured case before any extension to general data and depth.
