# Independent audit: Chen (2024), Neural Hilbert Ladders

## Scope, reading record, and verdict

Source: Zhengdao Chen, *Neural Hilbert Ladders: Multi-Layer Neural Networks in Function Space*, JMLR 25 (2024), pp. 1–65, [public primary publication](https://jmlr.org/papers/v25/23-1225.html). Frozen inputs: `data/generated/compression_literature_positioning_20261011/meanfield/chen_2024_nhl.pdf` and `.txt`. The entire paper, references, and Appendices A–E were read. Critical equations on printed pp. 12–15, 52, and 58 were also checked visually against the PDF. Page numbers below are printed page numbers.

This is a source-first independent audit, not a review of the study's manuscript or previous conclusions. No other study report or reviewer finding was used. No training or supplied code was run. The required review/severity, rigorous-proof, and canonical neural-notation instructions were applied; the claim ledger, evidence log, and dependency audit are integrated here in the requested single report. There is no venue score.

The strongest surviving result relevant to compression is a **static approximation theorem**: a function with finite ladder complexity has an approximating width-$m$ network with squared error of order $1/m$, at fixed depth and complexity. Its sampled coefficients depend on the target ladder. It is not a theorem about compressing a particular trained realization, retaining its fluctuations, or evolving a fixed finite state along the original trajectory.

The training result, Theorem 18, claims almost-sure convergence for each fixed finite time under mean-field $1/m$ normalization, independent initialization with centered interior weights/readouts and specific moment restrictions, and smooth activation. It has no stated width rate or endpoint-uniform conclusion. Its intended mechanism is reconstructible, but the printed proof contains incorrect intermediate statements and does not supply the uniform-time estimates needed for its concluding Grönwall argument. The corrected intended theorem is **not disproved** here. The literal main-text dynamics also contain equation errors that must be repaired before interpreting that theorem.

The general nonlinear ladder is not a fixed-dimensional state: its entries are function-space distributions/RKHSs, and its evolution uses two-time correlations. This is a property of the exhibited equations, not an inference from missing terminology. Conversely, finite closure is not impossible in every case: an explicit finite-dimensional closure for the paper's three-layer linear specialization is reconstructed below.

## 1. Exact objects and normalization

The main model is bias-free on a compact input set $\mathcal X\subset\mathbb R^d$. There are $L$ weight layers, $L-1$ hidden layers, common hidden width $m$, and scalar output. With first-layer weights $z_i\in\mathbb R^d$, interior weights $W^{(\ell)}_{ij}\in\mathbb R$, and readout weights $a_i\in\mathbb R$, the model is

\[
h_i^{(1)}(x)=z_i^\top x,\qquad
h_i^{(\ell+1)}(x)=\frac1m\sum_{j=1}^mW^{(\ell)}_{ij}\sigma(h_j^{(\ell)}(x)),\qquad
f_m(x)=\frac1m\sum_{i=1}^ma_i\sigma(h_i^{(L-1)}(x)).
\]

Here $1\leq\ell\leq L-2$. The gradient-flow mobilities corresponding to the intended displayed equations are $m$ for $z_i,a_i$, and $m^2$ for each $W^{(\ell)}_{ij}$. Thus this is not the ordinary $1/\sqrt m$ all-wide parameterization with unchanged learning rates. The initialization *does* use independent edge weights; it is not necessary to replace this paper's initialization by a correlated-neuron construction.

Let $\mathcal C=C(\mathcal X)$. For a probability measure $\mu$ on functions for which the following integrals are finite, define

\[
\kappa_\mu(x,x')=\int\sigma(h(x))\sigma(h(x'))\,\mu(dh),
\]

and let $\mathcal H_\mu$ be its RKHS. A ladder consists of $\mathcal H^{(1)}$, the linear input-function space, and measures $\mu^{(\ell)}\in\mathcal P(\mathcal H^{(\ell)})$ such that $\mathcal H^{(\ell+1)}=\mathcal H_{\mu^{(\ell)}}$. The norm of a law is

\[
\|\mu\|_{\mathcal H,p}=
\left(\int\|h\|_{\mathcal H}^p\,\mu(dh)\right)^{1/p},
\]

with essential supremum at $p=\infty$. The complexity $C_p^{(L)}(f)$ is the infimum of

\[
\|f\|_{\mathcal H^{(L)}}\prod_{\ell=1}^{L-1}
\|\mu^{(\ell)}\|_{\mathcal H^{(\ell)},p}
\]

over representing ladders (equivalently, the paper's nested infima through $D_p$). The associated function space is denoted $\mathcal F_p^{(L)}$. For positively 1-homogeneous activation, Theorem 3 identifies these complexities for $p\geq2$, and writes $C^{(L)},\mathcal F^{(L)}$. For a general Lipschitz activation this identification is not asserted, and Theorem 9 specifically needs $p=\infty$.

Two technical setup qualifications: on a compact set not spanning $\mathbb R^d$, the map $z\mapsto(x\mapsto z^\top x)$ is not injective, so the claimed identification with all of $\mathbb R^d$ should be understood using the quotient/minimum representing norm. Also, an arbitrary probability law on $C(\mathcal X)$ need not give a finite kernel; the moment-controlled ladders used below do. Neither issue invalidates the checked approximation construction.

## 2. Static representation and approximation: reconstructed chain

### 2.1 Lemma 6, replacing its external RKHS dependency

The needed feature-space result can be proved directly. Suppose $\int\|h\|_\infty^2\mu(dh)<\infty$ and $\sigma$ is Lipschitz. Define $\Phi(x)\in L^2(\mu)$ by $\Phi(x)(h)=\sigma(h(x))$, and let $E\subset L^2(\mu)$ be the closed span of the vectors $\Phi(x)$. For $\xi\in E$, set

\[
f_\xi(x)=\langle\xi,\Phi(x)\rangle_{L^2(\mu)}.
\]

This map is injective on $E$: a vector giving zero at every $x$ is orthogonal to a dense subset of $E$. Transporting the Hilbert norm makes its image an RKHS with kernel $\langle\Phi(x),\Phi(x')\rangle=\kappa_\mu(x,x')$, hence the image is $\mathcal H_\mu$. If an arbitrary $\xi\in L^2(\mu)$ represents the same function, its orthogonal projection onto $E$ does also, and minimizes the norm. Consequently

\[
f\in\mathcal H_\mu\iff f(x)=\int\xi(h)\sigma(h(x))\mu(dh),
\qquad \|f\|_{\mathcal H_\mu}=\min_{\xi\text{ representing }f}\|\xi\|_2.
\]

This proves exactly the part of Saitoh's RKHS representation result used here; no uninspected external theorem is needed for this step. Separability follows from continuity of the kernel on compact metric $\mathcal X$: kernel sections at a countable dense set span densely. This also permits measurable coefficient choices in Proposition 7 by expressing the minimal coefficient embedding in a countable orthonormal basis. Thus the proof's terse measurability assertion can be filled in for these controlled ladders.

Proposition 7 describes $L-1$ independent random *functions* $H^{(\ell)}\sim\mu^{(\ell)}$, pairwise coefficient functions $\Xi^{(\ell)}(H^{(\ell)},H^{(\ell+1)})$, and a terminal coefficient $A(H^{(L-1)})$, with

\[
H^{(\ell+1)}(x)=\mathbb E[\Xi^{(\ell)}\sigma(H^{(\ell)}(x))\mid H^{(\ell+1)}],
\quad f(x)=\mathbb E[A\sigma(H^{(L-1)}(x))].
\]

The number of displayed random fields is finite, but their laws and pairwise coefficient functions are generally infinite-dimensional objects.

### 2.2 Theorem 8: a finite network gives a ladder

For each hidden layer use the empirical law of its preactivation functions. Applying the preceding representation to a row of weights gives

\[
\|h_i^{(\ell+1)}\|_{\mathcal H^{(\ell+1)}}^2
\leq\frac1m\sum_j|W^{(\ell)}_{ij}|^2,
\qquad
\|f_m\|_{\mathcal H^{(L)}}^2\leq\frac1m\sum_i a_i^2.
\]

Hence $C_p^{(L)}(f_m)\leq\prod_{\ell=1}^LM_{m,p}^{(\ell)}$, where

\[
M_{m,p}^{(1)}=\left(m^{-1}\sum_i\|z_i\|^p\right)^{1/p},\quad
M_{m,p}^{(\ell+1)}=\left[m^{-1}\sum_i
\left(m^{-1}\sum_j|W^{(\ell)}_{ij}|^2\right)^{p/2}\right]^{1/p},\quad
M_{m,p}^{(L)}=\left(m^{-1}\sum_i a_i^2\right)^{1/2}.
\]

This argument, Appendix B.2, is an exact finite-network representation, not a training statement.

### 2.3 Theorem 9: what the $1/m$ bound actually proves

Assume $\sigma(0)=0$, $\sigma$ is $J_\sigma$-Lipschitz, $\nu\in\mathcal P(\mathcal X)$, and $M_\nu=\int\|x\|^2\nu(dx)<\infty$. The claim is that for $f\in\mathcal F_\infty^{(L)}$ there is a width-$m$ network satisfying

\[
\|f_m-f\|_{L^2(\nu)}^2\leq
\frac{(L-1)^2J_\sigma^{2L-2}M_\nu}{m}\bigl(C_\infty^{(L)}(f)\bigr)^2.
\]

Appendix B.3 samples $m$ independent functions from each ladder law, independently between layers, and takes the edge coefficients from the representing functions $\Xi^{(\ell)}$. Shared preceding neurons are retained. Here is the decisive error calculation, rather than an appeal to independent edges.

Write $M_\ell=\|\mu^{(\ell)}\|_{\mathcal H^{(\ell)},\infty}$. Conditional on a sampled target function in layer $\ell+1$, decompose its network approximation error into (i) propagation of previous-layer approximation error and (ii) centered Monte Carlo quadrature error using the exact previous-layer functions. Cauchy–Schwarz and the coefficient norm identity bound the RMS contribution (i) by $J_\sigma M_{\ell+1}e_\ell$, if $e_\ell$ is the uniform conditional $L^2(\nu)$-RMS error at layer $\ell$. The evaluation estimate

\[
|H^{(\ell)}(x)|\leq J_\sigma^{\ell-1}\|x\|\prod_{r=1}^{\ell}M_r
\]

and conditional independence of the exact sampled features bound contribution (ii) by

\[
\frac{J_\sigma^\ell\sqrt{M_\nu}}{\sqrt m}\prod_{r=1}^{\ell+1}M_r.
\]

Minkowski therefore yields

\[
e_1=0,\qquad e_\ell\leq
\frac{(\ell-1)J_\sigma^{\ell-1}\sqrt{M_\nu}}{\sqrt m}\prod_{r=1}^{\ell}M_r.
\]

At the last layer the coefficient only needs its $L^2$ norm $\|f\|_{\mathcal H^{(L)}}$. The same decomposition gives the displayed $(L-1)^2/m$ output bound in expectation over the samples, and hence for at least one realization. This validates the crucial conditional argument in Lemma 30 despite sharing earlier-layer samples. It does not require the approximate neurons within a layer to be mutually independent.

The proof writes an optimizing ladder as if the complexity infimum is attained. Without an attainment argument, the construction directly proves the bound with $C_\infty^{(L)}(f)+\varepsilon$, for every $\varepsilon>0$. The exact no-slack existence statement needs an attainment/closure step; the $1/m$ order and arbitrarily close constants survive without it. This is a local precision issue, not evidence against the approximation mechanism.

Nothing in this construction couples the approximant to a previously trained finite network or bounds the evolution of the approximation error under training. Its weights are obtained from a chosen target representation. The complexity, Lipschitz factor, and depth enter the constant explicitly. A width-independent bound is not a bound independent of the target function or its complexity.

## 3. Training assumptions and exact horizon

Section 7 uses the fixed empirical distribution $\nu_n=n^{-1}\sum_{k=1}^n\delta_{x_k}$, target values $f^*(x_k)$, and continuous-time full-batch gradient flow. Denote the empirical expectation by $\mathbb E_x$, and set

\[
\zeta_t(x)=\partial_{\widehat y}\ell(f_t(x),f^*(x)).
\]

Assumptions 15–17 are:

1. $\sigma$ is differentiable, with bounded Lipschitz derivative $\sigma'$. The activation itself need not be bounded; the identity is allowed. ReLU is excluded.
2. $\partial_{\widehat y}\ell(\widehat y,y)$ is Lipschitz in $\widehat y$. Squared loss is allowed; bounded loss derivative is not imposed here.
3. All initial $W^{(\ell)}_{ij},a_i,z_i$ are independent with respective laws $\rho_W,\rho_a,\rho_z$. Both $\rho_W$ and $\rho_a$ are centered; $\rho_W$ has finite fourth moment, $\rho_z$ finite covariance, and $\rho_a$ is bounded (used as bounded initial readouts). Thus Gaussian interior weights and first-layer vectors can be allowed, but an ordinary nondegenerate Gaussian readout does not meet the bounded-readout hypothesis.

The bias extension is given separately in Appendix B.1 and incorporated into Appendix D, with independently sampled bounded initial biases and an optional bias mobility. It is not the bias-free model silently endowed with diverse hidden random fields.

Theorem 18 states, for each fixed $t\geq0$, almost-sure convergence $f_{m,t}(x)\to f_t(x)$, and convergence of hidden-function laws after each fixed finite evaluation map $h\mapsto(h(x'_1),\dots,h(x'_N))$. The displayed supremum over 1-Lipschitz test functions is a Wasserstein-1 conclusion, stronger than mere weak convergence. It is not convergence in the uniform topology on $C(\mathcal X)$. The theorem does not provide a numerical width rate, a joint time-width scaling, or a uniform-in-$t\in[0,\infty)$ estimate. No fluctuation CLT or seed-dependent retained-state approximation is proved in this result.

The paragraph on inherited two-layer global convergence must retain the assumptions of the cited global-convergence theorems; Assumptions 15–17 alone do not imply global optimization. For example, take $L=2$, $\sigma=\tanh$, squared loss, $\rho_z=\delta_0$, $\rho_a=\delta_0$, and a nonzero constant target. Every parameter gradient is zero and the predictor stays zero. All of 15–17 hold. This is not a counterexample to a correctly qualified imported global-convergence theorem; it prevents reading the paragraph as an unconditional consequence of 15–17.

## 4. Reconstructing the dynamics and separating equation errors

For the intended gradient flow define the unactivated adjoint by $q_i^{(L-1)}=a_i$ and

\[
q_j^{(\ell)}(x)=\frac1m\sum_iW^{(\ell)}_{ij}
q_i^{(\ell+1)}(x)\sigma'(h_i^{(\ell+1)}(x)).
\]

Then direct differentiation of the network gives

\[
\dot z_i=-\mathbb E_x[\zeta_m(x)q_i^{(1)}(x)\sigma'(h_i^{(1)}(x))x],
\quad \dot a_i=-\mathbb E_x[\zeta_m(x)\sigma(h_i^{(L-1)}(x))],
\]

\[
\dot W^{(\ell)}_{ij}=-\mathbb E_x[
\zeta_m(x)q_i^{(\ell+1)}(x)\sigma'(h_i^{(\ell+1)}(x))\sigma(h_j^{(\ell)}(x))].
\]

The main text, p. 12, omits the vector $x$ in $\dot z_i$, and defines terminal $q$ with an extra $\sigma'$, which is then multiplied by another $\sigma'$. These are not valid formulas for the stated gradient flow. Appendix D uses the intended terminal $q=a$.

For the mean-field version let $H_t^{(1)}(x)=Z_t^\top x$, $Q_t^{(L-1)}=A_t$, and let $\Xi_t^{(\ell)}$ describe the learned part of an edge as a function of its endpoint initial labels. Centered independent initial edges have no coherent mean-field component, so $\Xi_0^{(\ell)}=0$. The intended edge equation is

\[
\dot\Xi_t^{(\ell)}=-\mathbb E_x[
\zeta_t(x)Q_t^{(\ell+1)}(x)\sigma'(H_t^{(\ell+1)}(x))\sigma(H_t^{(\ell)}(x))].
\]

The forward conditional expectation uses $\Xi_t^{(\ell)}\sigma(H_t^{(\ell)})$; the backward one must use $\Xi_t^{(\ell)}Q_t^{(\ell+1)}\sigma'(H_t^{(\ell+1)})$. Equation (32), p. 56, omits that last derivative, although the earlier flow-map definitions include it.

Integrating the edge equation and substituting into the forward/backward conditional expectations gives the paper's two-time kernels

\[
\kappa_{t,s}^{(\ell)}(x,x')=\mathbb E[\sigma(H_t^{(\ell)}(x))\sigma(H_s^{(\ell)}(x'))],
\]

\[
\gamma_{t,s}^{(\ell)}(x,x')=\mathbb E[
Q_t^{(\ell)}(x)Q_s^{(\ell)}(x')\sigma'(H_t^{(\ell)}(x))\sigma'(H_s^{(\ell)}(x'))].
\]

For $H^{(1)}$, the boundary kernel is necessarily $\kappa_{t,s}^{(0)}(x,x')=x^\top x'$, not 1 as printed below (13), p. 13. This follows at once by multiplying the equation for $Z_t$ by $x$; it is also the value used below (14), p. 14. The other boundary is $\gamma_{t,s}^{(L)}=1$.

With these corrections, differentiation of the output gives

\[
\dot f_t(x)=-\mathbb E_{x'}[\zeta_t(x')\theta_t(x,x')],\qquad
\theta_t=\sum_{\ell=1}^L\kappa_{t,t}^{(\ell-1)}\gamma_{t,t}^{(\ell)}.
\]

The minus sign is missing in printed (14), the two shallow ODEs on p. 14, and the output/linear-regression equations on p. 15. This was checked visually, not inferred from text extraction. A direct sign check is

\[
\frac{d}{dt}R_n(f_t)=-\frac1{n^2}\sum_{k,r}
\zeta_t(x_k)\theta_t(x_k,x_r)\zeta_t(x_r)\leq0,
\]

because every summand kernel in $\theta_t$ is positive semidefinite (a product of feature Gram kernels). The printed positive sign instead produces ascent. These are consequential transcription errors with explicit local corrections; they do not themselves falsify the intended, corrected learning dynamics.

For $L\geq4$, the bias-free centered model has an especially important special case. If also $\sigma(0)=0$, setting every $H^{(\ell)}=0$ for $\ell\geq2$, every $Q^{(\ell)}=0$ for $\ell<L-1$, and every $\Xi^{(\ell)}=0$ solves the corrected equations for all time, with unchanged $Z,A$. Each edge update has either zero preceding activation or zero following adjoint. Thus the intended unique limit is stationary with output zero. Remark 19 already recognizes deterministic interior fields; this calculation shows why one cannot assume rich all-depth feature learning for this particular bias-free initialization. Random biases or other permitted nondegenerate constructions change that conclusion. For $L=3$, the initial edge update can be nonzero, so the same argument does not apply.

## 5. Finite-width coupling: checked estimate, incorrect steps, and remaining obligation

Appendix D evaluates deterministic mean-field flow maps at the sampled initial labels, producing coupled variables $\widetilde z_i,\widetilde a_i,\widetilde W_{ij}^{(\ell)}$. Crucially, the interior error is

\[
D_W^{(\ell)}(t)=\frac1m\|W_t^{(\ell)}-W_0^{(\ell)}-\widetilde W_t^{(\ell)}\|_F,
\]

not $m^{-1}\|W_t^{(\ell)}-\widetilde W_t^{(\ell)}\|_F$. Individual initial edges need not converge to zero. Their *normalized operator action* vanishes, which is sufficient for forward/backward fields. This is a useful and materially different statement from convergence of all edge entries to deterministic coefficients.

### 5.1 The random-matrix dependency can be replaced

On p. 59 the source invokes the Marchenko–Pastur law to infer a largest-eigenvalue bound. Bulk spectral convergence by itself does not bound an extreme eigenvalue. A suitable extreme-eigenvalue theorem under finite fourth moments would justify the stronger bound used in the prose. The directly cited Bai–Silverstein book's [Chapter 5](https://doi.org/10.1007/978-1-4419-0661-8_5) is specifically about extreme eigenvalues, but its full theorem/proof was not accessible in the checked public publisher interface. No claim of having audited that book's full proof is made.

The weaker fact actually required can instead be established completely. Couple widths by upper-left submatrices of one infinite centered iid array, as is natural for the simultaneous strong-law coupling. Let $v=\mathbb E W_{11}^2$ and $\mu_4=\mathbb E W_{11}^4<\infty$. Expanding the trace and grouping the nonzero index patterns gives

\[
\mathbb E\operatorname{tr}((W_mW_m^\top)^2)
=m^2\mu_4+2m^2(m-1)v^2.
\]

Indeed, the surviving patterns are $i=k,j=l$, $i=k,j\ne l$, and $i\ne k,j=l$ in $\sum_{i,k,j,l}W_{ij}W_{kj}W_{kl}W_{il}$. Therefore

\[
\mathbb E\|W_m/m\|_{\mathrm{op}}^4
\leq\mu_4/m^2+2(m-1)v^2/m^2=O(m^{-1}).
\]

Markov and Borel–Cantelli along $m=2^r$ imply $\|W_{2^r}/2^r\|_{\mathrm{op}}\to0$ almost surely. For $2^r\leq m\leq2^{r+1}$, monotonicity of submatrix operator norms gives

\[
\|W_m/m\|_{\mathrm{op}}
\leq2\|W_{2^{r+1}}/2^{r+1}\|_{\mathrm{op}}\to0.
\]

For any possibly dependent feature vector $u\in\mathbb R^m$, with normalized Euclidean norm $\|u\|_m=m^{-1/2}\|u\|_2$,

\[
\|m^{-1}W_mu\|_m\leq\|W_m/m\|_{\mathrm{op}}\|u\|_m.
\]

Thus this step remains valid for trained features correlated with $W_m$, provided their normalized norms stay controlled. No spectral-edge theorem is needed for the needed vanishing estimate. The nested cross-width coupling is explicit here; the argument does not prove an arbitrary independently resampled triangular-array almost-sure statement.

### 5.2 The Grönwall proof is not complete as printed

The composite error $\Delta_{m,t}$, p. 58, includes parameter, hidden-field, backward-field, and residual errors. Three specific problems occur:

* The assertion $\Delta_{m,0}=0$ is false. For example, with $L=3$, $d=1$, $x=1$, $z_i=1$, centered Rademacher initial $W_{ij}$, centered bounded readouts, and $\sigma=\tanh$, one has $\widetilde h_i^{(2)}(1)=0$ but $h_i^{(2)}(1)=\tanh(1)m^{-1}\sum_jW_{ij}$, generally nonzero. The correct initial statement is an asymptotically small field error, not equality. This example meets the training assumptions.
* In (34), p. 60, an additive quadrature term $o(1+\Delta h+\Delta b)$ becomes $o(\Delta_{m,t})$. A nonzero sampling error cannot be absorbed multiplicatively into an error which can be zero. An additive $o(1)$ must remain.
* The final line on p. 63 differentiates the full $\Delta$ and asserts $d\Delta/dt=O(\Delta)+o(1)$, but the preceding estimates for hidden fields and residuals are algebraic estimates, not derivative estimates. Also, a strong law at each fixed time and each fixed sampled row is not, by itself, a uniform-in-time bound for an average over an increasing number of sampled rows.

These are positive failures of stated steps, not objections based only on omitted exposition. A repair should use only a parameter discrepancy $D_m(t)$ as the differential quantity and establish, on a stopped interval $[0,T]$, estimates of the form

\[
\sup_{s\leq t}\Delta_m(s)\leq C_T\left(\sup_{s\leq t}D_m(s)+e_m(T)\right),
\qquad
D_m(t)\leq D_m(0)+C_T\int_0^t(D_m(s)+e_m(T))\,ds,
\]

where $e_m(T)\to0$ almost surely includes the initial quadrature, normalized initial matrices, and **uniform-time** empirical integration errors. Grönwall then gives $\sup_{t\leq T}D_m(t)\leq(D_m(0)+TC_Te_m(T))e^{TC_T}$, allowing a stopping argument. Establishing $e_m(T)\to0$, suitable moment envelopes, and the needed local flow-map regularity under the exact unbounded-$z,W$ assumptions is the substantive remaining obligation. The source asserts finite-time Lipschitz flow maps but does not prove these uniform estimates. This audit supplies the matrix part and the algebraic repair architecture, not a complete replacement proof of that obligation.

The supremum over Lipschitz test functions also needs a uniform empirical-law argument, not merely a strong law for one $g$. For an iid finite-dimensional random vector with finite first moment, this part can be recovered by truncating outside a large ball, covering the normalized 1-Lipschitz functions on that ball by finitely many uniform approximants, applying the strong law to that finite net, and controlling the tail by the first-moment strong law. This explains the necessary integrability condition and does not by itself close the training-time estimate above.

Proposition 20's empirical kernel convergence similarly needs second-moment control: Wasserstein-1 convergence alone does not imply convergence of $\int\sigma(h(x))\sigma(h(x'))\,d\mu$. An $L^2$ coupling plus uniformly bounded empirical second moments would supply it by Cauchy–Schwarz. Its validity is therefore tied to the repaired coupling estimates, not an automatic consequence of the stated weak-law part of Theorem 18.

Severity: a major proof-certification gap for the presented general training theorem, alongside locally repairable displayed equations. This is not a demonstrated counterexample to the corrected intended finite-time mean-field limit, and does not affect the separately reconstructed static sampling theorem.

## 6. Finite retained state, memory, and a genuine special closure

Equations (12)–(13) use $\kappa_{t,s},\gamma_{t,s}$ over $0\leq s\leq t$. Current preactivation marginals do not specify those two-time correlations or the endpoint coefficient functions. Restricting evaluation to a fixed dataset turns each random field into an $n$-vector, but its law is still a probability distribution on $\mathbb R^n$, not a finite list of scalar state variables. The finite $n\times n$ current kernel governs the instantaneous output derivative; its future evolution is not closed by (14). Remark 21 explicitly attributes the memory to eliminating the edge parameters.

Section 7.1.2 specializes to linear activation. Kernels then have the form $\kappa_{t,s}^{(\ell)}(x,x')=x^\top K_{t,s}^{(\ell)}x'$, and $\gamma_{t,s}^{(\ell)}=c_{t,s}^{(\ell)}$. Equations (15)–(16) are finite matrix/scalar-valued *two-time Volterra equations*. A finite matrix at each pair of times is not in itself a fixed-dimensional Markov state. Nor does writing such memory equations prove that no finite Markov realization exists.

In fact, the following exact closure is available in the $L=3$ bias-free linear specialization. Take independent centered $Z_0,A_0$ with $\mathbb E Z_0Z_0^\top=I_d$, $\mathbb E A_0^2=1$, square loss, and target $f^*(x)=(v^*)^\top x$. Put $\Sigma=n^{-1}\sum_kx_kx_k^\top$. Define a matrix $B_t\in\mathbb R^{d\times d}$, vector $r_t\in\mathbb R^d$, and scalar $\alpha_t$ by

\[
B_0=I_d,\quad r_0=0,\quad\alpha_0=1,\quad
v_t=\alpha_t B_tr_t,\quad g_t=\Sigma(v_t-v^*),
\]

\[
\dot B_t=-\alpha_tg_tr_t^\top,\qquad
\dot r_t=-\alpha_t B_t^\top g_t,\qquad
\dot\alpha_t=-g_t^\top B_tr_t.
\]

Verification: the ansatz $Z_t=B_tZ_0$, $A_t=\alpha_tA_0$, and $\Xi_t(A_0,Z_0)=A_0r_t^\top Z_0$ gives $H_t^{(2)}(x)=A_0x^\top B_tr_t$ and $Q_t^{(1)}=\alpha_tr_t^\top Z_0$. Substitution into all three parameter equations yields precisely the displayed ODEs. The output is $f_t(x)=x^\top v_t$, and direct differentiation gives

\[
\dot v_t=-\left[\alpha_t^2\|r_t\|^2I_d+\alpha_t^2B_tB_t^\top
+(B_tr_t)(B_tr_t)^\top\right]g_t.
\]

This matches the sum of the three tangent-kernel contributions. It is a $d^2+d+1$-scalar autonomous realization, independent of width, for this particular linear limit. It is an independent reconstruction here, not a claim that the paper proves a general nonlinear finite-state closure. It retains a limiting predictor trajectory, not finite-width seed fluctuations or a finite-width trained endpoint. The distinction is essential to a fair positioning statement.

## 7. Additional checked claim defects, confined to their actual impact

### Theorem 10: false activation-scale dependence

The source claims $\widehat{\mathrm{Rad}}_S(B(\mathcal F^{(L)};M))\leq M(\sqrt{2L\log(2J_\sigma)}+1)/\sqrt n$. Appendix C, Lemma 33, p. 52, applies contraction to an exponential test function by putting $J_\sigma$ outside the expectation. Scaling a Lipschitz contraction scales the argument of the exponential, not just its prefactor.

A complete counterexample uses $\sigma(u)=cu$, $\mathcal X=\{1\}\subset\mathbb R$, $L=2$, and $n=1$. A function is a value $v$ on this set. For a first-layer law of second moment $s>0$, the output RKHS norm is $|v|/(c\sqrt s)$, and its multiplier is $\sqrt s$. Hence $C^{(2)}(v)=|v|/c$, and the radius-$M$ ball has empirical Rademacher complexity $cM$. With $c=10$, the claimed upper bound is only $M(\sqrt{4\log20}+1)<4.47M$. Thus Theorem 10 is false for its stated general class of homogeneous activations. The normalized $J_\sigma=1$ case, notably ReLU, is not refuted by this counterexample and supports the usual properly normalized exponential-contraction argument. This defect affects the generalization theorem's activation scaling, not the static approximation bound or the finite-state distinction.

### Corollary 11: missing loss-range control

Lipschitzness in the prediction variable does not control an arbitrary label-dependent offset. Take $n=1$, two equiprobable input points in the unit ball with labels $\pm1$, $f=0$, and $\ell(\widehat y,y)=A\mathbf1_{\{y=1\}}$. The prediction Lipschitz constant is zero, but with probability $1/2$ the empirical risk is zero and the population risk is $A/2$. For $\delta=1/4$ and sufficiently large $A$, the stated confidence term cannot bound that gap. A bounded loss range, or a corresponding range-dependent term, is needed. Again this does not change the representation/approximation theorem.

### Depth-separation scope

The proof of Proposition 13, p. 11, imports a global $\mathbb R^d$ biased pyramid example into the compact-domain bias-free setup without spelling out the change. The function $\max(1-\|x\|_1,0)$ has value 1 at zero and is not realizable by a bias-free ReLU ladder on a domain containing zero. More directly, the unqualified strict inclusion is false for $d=1,\mathcal X=[-1,1]$: every bias-free positively homogeneous deep ReLU network has just two linear slopes, and all such functions already lie in $\mathcal F^{(2)}$. This does not refute a correctly dimension-/domain-/bias-qualified separation theorem. The Ongie and Wojtowytsch external separation arguments were not needed for the relevant finite-state chain and were not independently audited; Proposition 14 remains an externally dependent depth claim, not evidence used in the verdict.

## 8. Evidence and dependency ledger

| Claim | Primary location | Audit coverage | Result/impact |
|---|---|---|---|
| RKHS coefficient representation | Lemma 6, Appendix A | Complete elementary feature-space reconstruction | Survives under stated integrability; replaces needed Saitoh dependency |
| Static coupled-field representation | Proposition 7, Appendix A.4 | Coefficient/norm identity and separable measurable construction checked | Infinite-dimensional fields, not finitely many scalars |
| Finite NN belongs to ladder | Theorem 8, Appendix B.2 | Rowwise coefficient calculation reconstructed | Survives |
| Width-$m$ static approximation | Theorem 9, Lemma 30, Appendix B.3 | Conditional Monte Carlo and RMS recurrence reconstructed | $1/m$ squared-error order survives; exact infimum attainment not supplied |
| General activation Rademacher bound | Theorem 10, Lemma 33 | Exponential contraction step inspected; explicit linear-activation counterexample | False as written for arbitrary $J_\sigma$; ReLU case not refuted |
| Loss confidence bound | Corollary 11 | Label-offset counterexample | Needs a loss-range hypothesis/constant |
| Finite-time trained limit | Theorem 18, Appendix D.1/D.1.1 | Full proof read, parameter coupling/matrix step reconstructed, initial-error counterexample and differential gap isolated | Intended theorem not disproved; full proof not certified under exact assumptions |
| Initial iid matrix disappears in operator action | Appendix D, p. 59; Bai–Silverstein citation | Needed weaker result proved by trace expansion, dyadic Borel–Cantelli | External edge theorem unnecessary under nested coupling |
| Evolving kernel convergence | Proposition 20 | Required $L^2$/moment implication identified | Conditional on completing coupling and second-moment control |
| Non-Markovian nonlinear representation | Equations (12)–(13), Remark 21 | Edge integration and two-time kernel mechanism reconstructed | Explicit memory, no general finite closure |
| Linear specialization | Section 7.1.2, Appendix D.2 | Matrix kernel form read; $L=3$ autonomous realization reconstructed | Genuine restricted finite closure, not nonlinear or fluctuation result |
| Empirical examples | Section 7.2, Figures 2–3 | Full descriptions read; no code execution | Illustrations, not verification of all theorem assumptions |

The empirical ReLU example has nonsmooth activation and Gaussian readouts, both outside Theorem 18's stated assumptions, and uses discrete GD rather than exact gradient flow. This is an explicit theorem/experiment mismatch, not evidence that the illustration is invalid. The linear experiment is likewise not a finite-width error-rate theorem. Theorems from unrelated cited optimization, NTK, or depth-separation literature were not recursively imported to strengthen these conclusions.

## 9. Surviving positioning statement

NHL supplies a functional representation of multilayer networks, a complexity-controlled static sampling approximation, and an intended mean-field description of training using evolving random fields and kernels. The static $1/m$ approximation mechanism withstands reconstruction, up to the precise attainment qualification. The training theorem is fixed-time and uses a specific smooth mean-field model and initialization; its printed proof and formulas need the identified repairs before being treated as fully certified. It provides neither a long-time uniform finite-width coupling nor a seed-fluctuation retention guarantee.

One may accurately say that the general nonlinear formulation retains function-space laws and temporal correlations, whereas special linear models can have a finite-dimensional realization. It would be inaccurate either to equate the general ladder with a fixed finite autonomous state, or to claim that the paper rules out all finite-state reductions. These boundaries follow from checked formulas and explicit constructions, not from absence of a compression theorem alone.
