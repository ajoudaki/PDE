# Independent checks of three frozen proof passages

Date: 2026-10-11. Scope: the neutral assignment concerning Huang–Yau Appendix B and Appendix A; Golikov–Yang Setup 3.6 and Appendix K; and Chen–He–Su Appendix B.3. I read the specified passages, their mathematical setup and the dependencies needed below, without reading study history, another review, or another agent's findings. This is a scoped verification, not a complete-paper verdict.

The frozen sources are:

- Huang–Yau, *Dynamics of Deep Neural Networks and Neural Tangent Hierarchy*, [arXiv v1 PDF](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/root/nth_arxiv.pdf), arXiv:1909.08156v1, and the supplied [conference PDF](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/root/nth.pdf).
- Golikov–Yang, *Non-Gaussian Tensor Programs*, supplied [NeurIPS main paper](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/nongaus/neurips-main.pdf) and [appendix](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/nongaus/appendix.pdf). Appendix page references below are printed pages, 14–46.
- Chen–He–Su, *Label-Aware Neural Tangent Kernel: Toward Better Generalization and Local Elasticity*, [arXiv v2 PDF](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/root/lantk.pdf), arXiv:2010.11775v2.

The notation below follows each source. In the NTH and LANTK discussion, $m$ is network width and $n$ is the number of training examples. In the tensor-program discussion, $n$ is vector width. These are different source conventions.

## Conclusions and claim levels

| Passage | Verified finding | Claim level |
|---|---|---|
| NTH (B.25)–(B.29), (B.34) | The passage from first-derivative bounds to higher physical time derivatives omits residual derivatives and differentiates inequalities without justification; the maximum defining $\xi$ need not have those derivatives. | Substantive proof gap. It does not by itself disprove the desired long-time estimate. |
| NTH Corollary A.5 versus §1.3 | A polylogarithmic bound on a Gaussian coordinate cannot have failure probability at most $e^{-m^c}$. | The corollary is false with the paper's literal probability convention. A weaker high-probability convention can repair this particular discrepancy. |
| NTH (A.6) | The full-rank argument needs a nonconstant activation; constant activations are admitted by Assumption 2.1. | False intermediate assertion under the stated assumptions. Nonconstancy or a separate degenerate case repairs this point. |
| Non-Gaussian TP Setup 3.6 / Theorem 3.7 | Existence of each initial scalar's moments at each width does not give uniform integrability. A rare-spike scalar satisfies the written setup and fails even $L^1$ convergence. | Literal all-$L^p$ theorem statement is false under the written assumptions. Uniform moment bounds are a natural correction. |
| Non-Gaussian TP (68)–(69), K.1–K.2 | The proposed reverse recursion misses scalar-to-scalar feedback. A polynomial program gives a nonzero true matrix derivative and zero from the printed formulas. | False intermediate identities for the full Definition 3.1 language; a correct reverse pass with scalar adjoints is available. The universality conclusion is not disproved by this algebra error. |
| LANTK B.3 | The nonzero delta terms use distributional derivatives, whereas classical finite-width ReLU derivatives of order two and higher in the preactivation are zero almost surely. | These are different mathematical objects; their identification would require a separate limiting argument. |
| LANTK term III, pp. 25–27 | The term contains $a_i^2$, so its Gaussian moment is 1, not 3. | Local factor-of-three error: $3m$ should be $m$ for this defined term. |
| LANTK repeated/singular inputs | Gaussian averaging does not automatically define products such as $\delta(u)^2$. Even the whole diagonal fourth kernel can have a divergent smooth-ReLU limit. | Missing domain/regularization specification; this cannot be fixed merely by setting an inverse to a pseudoinverse. |
| LANTK rotation formula, p. 25 | A term is missing in the third coordinate of $Qx_\xi$. | Additional local algebra error, present even for four linearly independent inputs. |

## 1. Huang–Yau NTH

### 1.1 Physical time derivatives are not the recursively generated coefficients

Write the prediction residual as $r_\beta(t)=f(x_\beta,\theta_t)-y_\beta$. To avoid confusion with the source's use of $f_t$ for a vector expression, write that expression as $v(t)$, and write its recursively generated coefficients in (B.25)–(B.26) as $v^{[j]}(t)$. Thus the brackets are coefficient labels, not physical time derivatives. Equations (B.25) and (B.26) have the form

\[
\dot v=-\frac1{n\sqrt m}\sum_\beta v^{[1]}_\beta r_\beta,
\qquad
\dot v^{[j]}_{\beta_1\ldots\beta_j}
=-\frac1{n\sqrt m}\sum_\gamma
v^{[j+1]}_{\beta_1\ldots\beta_j\gamma}r_\gamma.
\]

These are legitimate first-derivative identities for the indicated coefficient expressions. If $n^{-1}\sum_\beta r_\beta^2$ is bounded, Cauchy–Schwarz gives (B.27) and (B.28). But differentiating the first identity again gives

\[
\ddot v
=\frac1{n^2m}\sum_{\beta,\gamma}
v^{[2]}_{\beta\gamma}r_\beta r_\gamma
-\frac1{n\sqrt m}\sum_\beta v^{[1]}_\beta\dot r_\beta.
\]

The residual equation in Theorem 2.3 is

\[
\dot r_\beta=-\frac1n\sum_\gamma K^{(2)}_t(x_\beta,x_\gamma)r_\gamma.
\]

Consequently the second term is

\[
\frac1{n^2\sqrt m}\sum_{\beta,\gamma}
v^{[1]}_\beta K^{(2)}_t(x_\beta,x_\gamma)r_\gamma,
\]

and it has only the original explicit factor $m^{-1/2}$. It is absent from the purported iteration in (B.29). Further physical derivatives produce further derivatives of residuals. The higher coefficient $v^{[p+1]}$ does not, by its definition in (B.26), include these contributions.

This is visible in a two-layer linear example. Take one input $x=1$, activation $\sigma(u)=u$, first-layer vector $w\in\mathbb R^m$, readout $a\in\mathbb R^m$, and

\[
f=\frac{a^\top w}{\sqrt m},\qquad
\mathcal L=\frac12(f-y)^2,\qquad r=f-y.
\]

Then

\[
\dot a=-\frac{rw}{\sqrt m},\quad
\dot w=-\frac{ra}{\sqrt m},\quad
\dot r=-Kr,\quad
K=\frac{\|a\|_2^2+\|w\|_2^2}{m},
\]

and therefore

\[
\ddot a=\frac{Kr w}{\sqrt m}+\frac{r^2a}{m}.
\]

Here the replacement coefficients for $a$ are successively $w,a,w,\ldots$. The leading term in the physical second derivative is not the term estimated by replacing twice. For a completely explicit smooth norm example, let $m=2k+1$, $a_1=2$, $a_i=1$ for $i>1$, $w_1=1$, and arrange the remaining entries of $w$ in $(1,-1)$ pairs. Choose $y=2/\sqrt m-1$, so that $r=1$ at this state. Then $K=2+3/m$, the first coordinate uniquely attains $\|a\|_\infty$, and locally

\[
\frac{d^2}{dt^2}\|a\|_\infty
=\frac{2+3/m}{\sqrt m}+\frac2m.
\]

The proposed second-order replacement bound is proportional to $m^{-1}\|a\|_\infty=2/m$, which is smaller by an unbounded factor. This deterministic state is an algebra check of the claimed derivative mechanism, not a claim that this exact state has positive Gaussian probability or that the final random-initialization theorem is false.

There are also two analytic problems independent of the omitted residual term. First, $A(t)\le B(t)$ does not imply $A'(t)\le B'(t)$; (B.29) explicitly obtains its higher derivatives by differentiating an inequality. Second, an infinity norm and the maximum over expressions in (B.24) can switch their maximizing coordinates/expressions. They are locally Lipschitz under suitable bounds but need not be twice differentiable, much less $p+1$ times differentiable. First-order upper Dini derivatives can be used for a norm comparison, but they do not justify the printed high-order comparison or its high-order initial data.

The estimates (B.30)–(B.33) bound the recursively generated coefficient $v^{[p+1]}$. Even if those coefficient estimates are accepted, they do not repair the missing relation to physical derivatives. Thus (B.34), and the comparison argument which uses it, are not established by this chain of reasoning. A valid repair would have to retain the time-dependent residual factors—for example in iterated integral estimates—or supply a different differential estimate. I have not proved that such a repair preserves the paper's time scale $m^{p/(2(p+1))}$ up to logarithms. The formal NTH identities themselves are not refuted by this finding.

### 1.2 Corollary A.5 has a strictly weaker attainable tail scale

Section 1.3 defines high probability as probability at least $1-e^{-m^c}$ for some fixed $c>0$. Equation (3.5) puts the unnormalized Gaussian readout $a_0$ in $\mathcal D_0$. Corollary A.5 therefore includes

\[
\|a_0\|_\infty\le B(\log m)^C
\]

for constants $B,C$ independent of width. For nonzero initialization variance $\sigma_a^2$, its failure probability is at least the tail of the first coordinate:

\[
\Pr\{\|a_0\|_\infty>B(\log m)^C\}
\ge\Pr\{|G|>(B/\sigma_a)(\log m)^C\},\qquad G\sim N(0,1).
\]

The elementary Gaussian tail lower bound, obtained by integrating its density on $[u,u+1/u]$ for $u\ge1$, is at least a constant times $u^{-1}e^{-u^2/2-O(1)}$. Its negative logarithm here is $O((\log m)^{2C}+\log\log m)$, which is smaller than $m^c$ for every fixed positive $c$. Hence the probability asserted with that definition is impossible. The supplied conference text repeats the same definition and activation hypotheses.

A suitably large polylogarithmic threshold does give failure probability smaller than every prescribed inverse polynomial; this is enough for polynomial-size union bounds. Replacing the stipulated probability class by that weaker class repairs this particular issue, but does not repair §1.1. The corollary is literally false as written; this calculation alone does not identify every downstream theorem's sharp attainable tail.

### 1.3 The rank assertion (A.6) needs nonconstancy

Assumption 2.1 requires smoothness and bounded derivatives of orders $1,\ldots,2p+1$. It permits $\sigma\equiv0$ and $\sigma\equiv1$. For the latter, all first-layer feature vectors are $m^{-1/2}\mathbf1$; their Gram matrix has rank one regardless of how independent the input vectors are. For the former, the Gram matrix is zero. This contradicts the full-rank assertion preceding (A.6).

For a **nonconstant continuous** activation, the particular argument can be repaired. The distinct-input assumption gives an invertible triangular transformation from $(G_1,\ldots,G_r)$ to the first-layer preactivations $(U_1,\ldots,U_r)$, so their joint density is positive throughout $\mathbb R^r$. If

\[
\sum_{i=1}^r\lambda_i\sigma(U_i)=0\quad\text{almost surely},
\]

continuity and full support make it an identity for every $u\in\mathbb R^r$. Varying one coordinate while keeping the others fixed, and choosing two values where $\sigma$ differs, gives $\lambda_i=0$ for each $i$. Thus the Gram matrix is positive definite under this added nonconstancy hypothesis. Repeated input indices must first be deduplicated; Assumption 2.2 concerns distinct indices. A rank-aware treatment can handle constant activations separately, so this intermediate counterexample does not by itself refute the final kernel estimates for constant networks.

## 2. Non-Gaussian Tensor Programs

### 2.1 The written initial-scalar condition does not imply all-$L^p$ convergence

Definition 3.1 permits nonlinearities to use initial scalars, and Setup 3.3(2) requires those scalars to have almost sure limits as $n\to\infty$. Setup 3.6 adds existence of all their moments, without a uniform-in-width bound. Let $U\sim\operatorname{Unif}(0,1)$ be independent of all matrices and initial Gaussian vectors, and set

\[
c_n^1=n\,\mathbf1_{\{U\le1/n\}}.
\]

For every $U>0$, $c_n^1$ eventually vanishes, so $c_n^1\to0$ almost surely. Every finite-width moment exists, but

\[
\mathbb E|c_n^1|^p=n^{p-1}.
\]

Use standard Gaussian matrices of variance $1/n$, a standard Gaussian initial vector $g^1$, and the polynomially smooth nonlinearity $\varphi^2(g^1;c^1)=c^1$. Then $x^2=c_n^1\mathbf1$ and the **computed** scalar $c_n^2=\langle x^2\rangle=c_n^1$, where $\langle x\rangle=n^{-1}\sum_\alpha x_\alpha$. This satisfies the stated assumptions but does not converge to zero in $L^1$, and therefore not in every $L^p$. The example does not merely exploit inclusion of initial scalars in the theorem's wording.

The proof's missing input is visible in Appendix J: Definition J.1(c) discusses bounds $\mathbb E|c^i|^q\le R_q$ for **all widths**, and the induction on p. 33 fixes those bounds. They need not exist under Setup 3.6. A natural corrected assumption is

\[
\sup_n\mathbb E|c_n^i|^q<\infty
\quad\text{for every initial scalar }i\text{ and every finite }q.
\]

Together with almost sure convergence, the $q>p$ bounds give uniform integrability of the $p$-th powers: for $R>0$, $\mathbb E[|c_n^i|^p\mathbf1_{|c_n^i|>R}]\le R^{p-q}\sup_n\mathbb E|c_n^i|^q\to0$. This repairs the initial-scalar obstacle and supplies the moment input used by Appendix J. It is not, on its own, a fresh proof of the rest of Theorem 3.7. Fixed deterministic initial scalars satisfy the correction and are unaffected by this counterexample.

### 2.2 Correct reverse recursion and the missing scalar chain

For one Definition 3.1 iteration, the forward operations are

\[
x^i_\alpha=\varphi^i(g^1_\alpha,\ldots,g^{i-1}_\alpha;c^1,\ldots,c^{i-1}),
\quad g^i=W^ix^i,\quad c^i=\langle x^i\rangle.
\]

The terminal scalar is $c=\langle\psi(g^1,\ldots,g^M;c^1,\ldots,c^M)\rangle$. Preserve Appendix K's notation $x^j_{i;}=\partial_{g^i}\varphi^j$ and $x^j_{;i}=\partial_{c^i}\varphi^j$, evaluated coordinatewise; for $j=M+1$, use derivatives of $\psi$. Introduce the scalar adjoint $q_i=\partial c/\partial c^i$, and vectors $dg^i=n\nabla_{g^i}c$, $dx^i=n\nabla_{x^i}c$, all as reverse-mode adjoints of nodes in the computation graph.

The chain rule gives the following descending recursion:

\[
\begin{aligned}
dg^i&=x^{M+1}_{i;}+\sum_{j=i+1}^M x^j_{i;}\odot dx^j,\\
q_i&=\langle x^{M+1}_{;i}\rangle
+\sum_{j=i+1}^M\langle x^j_{;i}\odot dx^j\rangle,\\
dx^i&=W^{i\top}dg^i+q_i\mathbf1.
\end{aligned}
\]

To verify the last line, the edge $x^i\mapsto g^i$ contributes $W^{i\top}dg^i$, while $x^i\mapsto c^i=n^{-1}\mathbf1^\top x^i$ contributes $q_i\mathbf1$ after multiplying the adjoint by $n$. The other lines sum the direct terminal contribution and every downstream $x^j$ edge. This recursion includes arbitrarily many scalar-feedback edges.

Equation (69) omits $q_i\mathbf1$. Equation (68) inserts some one-scalar-edge terms into $dg^i$, but this does not account for paths through multiple computed scalars. In particular, Proposition K.1's identification of the printed $dx^i$ with the total scaled adjoint is false even for a terminal $\psi=c^M$: the printed $dx^M$ is zero while the true one is $\mathbf1$.

Here is a counterexample which also invalidates the matrix derivative formula when it uses the printed recursion. Take $M_0=1$, a single matrix $A$, initial vector $g^1=v$, and any unused initial scalar. All three iterations use $W^i=A$:

\[
\begin{array}{c|c|c|c}
i&x^i&g^i&c^i\\\hline
2&v&Av&\langle v\rangle\\
3&g^2&Ag^2&\langle g^2\rangle\\
4&c^3\mathbf1&Ac^3\mathbf1&c^3.
\end{array}
\]

Set $\psi=c^4$. Then $c=c^4=\langle Av\rangle$ and

\[
\frac{\partial c}{\partial A_{\alpha\beta}}=\frac{v_\beta}{n}.
\]

The nonzero partial derivatives relevant to the printed backward pass are $x^3_{2;}=\mathbf1$, $x^4_{;3}=\mathbf1$, and $x^5_{;4}=\mathbf1$. Starting from $dx^5=\mathbf1$, (68)–(69) give $dg^4=dx^4=dg^3=dx^3=dg^2=dx^2=0$. The only chain which can transmit the terminal derivative to $g^2$ is $g^2\to c^3\to c^4\to c$; it has two scalar edges. Consequently the printed Proposition K.2 evaluates the matrix derivative as zero. The correct recursion gives $q_4=q_3=1$, $dx^4=dx^3=\mathbf1$, and $dg^2=\mathbf1$, producing the true derivative above.

All nonlinearities in this example are linear. One may take $A$ and $v$ to have exactly the Gaussian distributions required by the setup; the identity failure then occurs almost surely. The error is therefore present in the full Definition 3.1 language, not merely at nonsmooth nonlinearities or exceptional matrix values.

The matrix-gradient identity in K.2 is valid when supplied with the **correct** $dg^i$: sum $n^{-1}(dg^i)_\alpha(x^i)_\beta$ over uses of $A$, with indices transposed for uses of $A^\top$. Correct scalar adjoints can also be represented by further polynomially smooth tensor-program operations. Thus a repair is structurally available, but the printed K.1–K.5 proof chain does not establish it as stated. These calculations do not disprove universality with corrected moment assumptions and a corrected backward construction.

## 3. Chen–He–Su LANTK

### 3.1 Distributional derivatives and ordinary random derivatives differ

The Appendix B.2 model is

\[
f(x)=\frac1{\sqrt m}\sum_{i=1}^m a_i\sigma(w_i^\top x),
\qquad a_i\sim N(0,1),\quad w_i\sim N(0,I_d),
\]

with independent initialization. Appendix B.3 explicitly chooses ReLU and then uses $\sigma''=\delta$ and $\sigma'''=\delta'$. For fixed nonzero inputs and finite width, Gaussian preactivations avoid zero almost surely. On a neighborhood of such an initialization, each activation has a fixed gate, and its classical preactivation derivatives satisfy

\[
\sigma'(u)=\mathbf1_{u>0},\qquad \sigma''(u)=\sigma'''(u)=0.
\]

Mixed derivatives involving both $a_i$ and $w_i$ can still be nonzero; this is not a claim that every higher derivative of the network or kernel vanishes. It is specifically the delta-containing terms in B.3 that do not equal ordinary expectations of these classical finite-width derivative expressions.

The distinction already appears in one dimension. If $G\sim N(0,1)$, then the classical random variable $\sigma''(G)$ is zero almost surely. In contrast,

\[
\left.\frac{d^2}{db^2}\mathbb E\sigma(G+b)\right|_{b=0}
=\frac1{\sqrt{2\pi}}
=\langle\delta,\text{standard Gaussian density}\rangle.
\]

Thus averaging does not permit one to exchange classical second differentiation with expectation here. The appendix is explicitly performing distributional Gaussian pairings. With sufficiently independent input directions these pairings can be defined through independent linear coordinates, or justified through a specified smoothing limit. That is a possible interpretation; it is not the expectation of classical finite-width automatic differentiation. The sentence that Gaussian initialization gives zero mass to the kink justifies the first derivative almost surely and does not justify the subsequent identification with delta derivatives.

### 3.2 Term III has the wrong readout moment

On p. 25 the defined quantity is

\[
\mathrm{III}=\sum_{i=1}^m a_i^2
\sigma''(w_i^\top x_\alpha)\sigma(w_i^\top x_\beta)
\sigma'(w_i^\top x_\gamma)\sigma'(w_i^\top x_\xi).
\]

Under the appendix's distributional interpretation, independence and $\mathbb E a_i^2=1$ give

\[
\mathbb E\mathrm{III}
=m\,\mathbb E\!\left[
\delta(x_\alpha^\top Z)(x_\beta^\top Z)
\mathbf1_{\{x_\beta^\top Z\ge0,\;x_\gamma^\top Z\ge0,\;x_\xi^\top Z\ge0\}}
\right],\qquad Z\sim N(0,I_d).
\]

The p. 26 and p. 27 formulas instead carry $3m$. The factor 3 belongs to $\mathbb E a_i^4$, relevant to terms IV and V, but not to III. This is visually confirmed in the PDF, not an extraction ambiguity. All displayed $3m$ factors in the evaluation of this defined III should be replaced by $m$.

For example, with the four inputs equal to four orthonormal basis vectors, the distributional scalar integral is

\[
\frac1{\sqrt{2\pi}}\,\mathbb E[G\mathbf1_{G\ge0}]\,\frac14
=\frac1{8\pi}.
\]

Thus the defined term has expectation $m/(8\pi)$, while the printed evaluation gives $3m/(8\pi)$. This is a direct check of the basis term; some prefactors of the full fourth kernel vanish for orthogonal inputs, so this particular example is not asserted to be a nonzero full-kernel discrepancy. Under the classical derivative interpretation, III is instead zero almost surely, as explained above.

### 3.3 Singular data require a separate definition

For the ordinary terms I and II, the Gaussian expectations remain meaningful when input vectors are linearly dependent. Their orthant probability can be computed using any covariance factor of the possibly singular Gram matrix; an inverse of $V$ is unnecessary. Thus singularity alone is not an obstruction to those terms.

The delta terms need more care. For independent $x_\alpha,x_\beta$, $\delta(x_\alpha^\top Z)\delta(x_\beta^\top Z)$ can be interpreted as a Gaussian surface integral on their common zero set. If $x_\beta=x_\alpha\ne0$, this becomes $\delta(u)^2$, which has no ordinary distributional product. A Gaussian integration weight does not define that product. Gates on the same hyperplane as a delta or a delta derivative likewise require a convention or a justified limiting construction. The paper's distinct-index nondegeneracy condition in Assumption A does not eliminate repeated indices in $K^{(4)}(x_\alpha,x_\beta,x_\gamma,x_\xi)$.

This is not merely a removable coordinate denominator. A direct example shows that a natural smooth-ReLU limit of the **whole** diagonal fourth kernel need not be finite. Take $d=1$, $x_\alpha=x_\beta=x_\gamma=x_\xi=1$, and smooth ReLU by

\[
\sigma_\varepsilon(u)=\varepsilon s(u/\varepsilon),\qquad
s(z)=z\Phi(z)+\phi(z),
\]

where $\Phi$ and $\phi$ are the standard Gaussian distribution function and density. This is Gaussian smoothing of ReLU. For one neuron, write $s_0=\sigma_\varepsilon(w)$, $s_1=\sigma_\varepsilon'(w)$, $s_2=\sigma_\varepsilon''(w)$, $s_3=\sigma_\varepsilon'''(w)$. The contributions of this neuron to the second and third kernels are

\[
\frac{s_0^2+a^2s_1^2}{m},\qquad
\frac{4as_0s_1^2+2a^3s_1^2s_2}{m^{3/2}}.
\]

These follow by applying the NTH recursion $K^{(r+1)}=\nabla K^{(r)}\cdot\nabla f$, with the neuron's gradient $m^{-1/2}(s_0,as_1)$. Differentiating the displayed third-kernel contribution with respect to $(a,w)$ and pairing with this gradient gives the following contribution to $m^2K^{(4)}$:

\[
4s_0^2s_1^2+4a^2s_1^4+14a^2s_0s_1^2s_2
+4a^4s_1^2s_2^2+2a^4s_1^3s_3.
\]

After averaging $a$, the last two terms have coefficients 12 and 6. Put

\[
A=\int_{\mathbb R}\Phi(z)^2\phi(z)^2\,dz>0.
\]

Since $s'=\Phi$, $s''=\phi$, and $s'''=\phi'$, integration by parts yields

\[
\int\Phi^3\phi'=-3\int\Phi^2\phi^2=-3A.
\]

Changing variables $w=\varepsilon z$ in the last two terms therefore gives

\[
\mathbb E K^{(4)}_\varepsilon(1,1,1,1)
=-\frac{6\phi(0)A}{m\varepsilon}+O(m^{-1})
\quad(\varepsilon\downarrow0).
\]

The other terms have bounded expectations; the Gaussian tails justify the stated limit and the integration by parts. In contrast, the classical fixed-gate ReLU calculation gives

\[
K^{(4)}_{\mathrm{classical}}(1,1,1,1)
=\frac4{m^2}\sum_i(a_i^2+w_i^2)\mathbf1_{w_i>0},
\qquad
\mathbb E K^{(4)}_{\mathrm{classical}}=\frac4m.
\]

Thus there is neither automatic equality to the classical kernel nor a universal finite extension obtained merely by smoothing and averaging. The nondegenerate distributional formulas can still be studied on their proper domain, but an application to diagonal/repeated entries must supply additional mathematics or a chosen finite regularization.

### 3.4 Additional algebra error in the rotation used on p. 25

The printed expression for the third coordinate of $Qx_\xi$, after normalization to unit inputs, is missing the contribution from the first coordinates. With the source's triangular coordinates and $v_\alpha=e_1$, preservation of the $\gamma,\xi$ inner product requires

\[
(Qx_\xi)_3
=\frac{\cos\Delta_{\gamma\xi}
-\cos\Delta_{\alpha\gamma}\cos\Delta_{\alpha\xi}
-(Qx_\gamma)_2(Qx_\xi)_2}
{(Qx_\gamma)_3}.
\]

The middle product in the numerator is absent on p. 25. For an explicit full-rank example, take

\[
x_\alpha=e_1,\quad x_\beta=e_2,\quad
x_\gamma=(e_1+e_3)/\sqrt2,\quad
x_\xi=(e_1+e_4)/\sqrt2.
\]

The true $x_\gamma^\top x_\xi$ is $1/2$. The printed construction produces $(Qx_\xi)_3=1/\sqrt2$, $(Qx_\xi)_4=0$, and an inner product of 1 instead. Thus even its assertion that the constructed $V$ is invertible fails for this full-rank example. Correcting the coordinate formula removes this particular error; it does not remove the genuine singular/repeated-input issues above. A covariance-factor construction would avoid this fragile coordinate formula entirely.

## Verification artifacts and limits

Selected PDF pages were rendered under [independent scratch](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/independent) to check the source typography. The NTH derivative example, scalar-feedback example, and a quadrature check of the ReLU smoothing asymptotic are recorded in [checks.json](/home/amir/Codes/PDE/data/generated/mfp_literature_positioning_20261011/independent/checks.json). The conclusions above rest on the displayed algebra and counterexamples, not on numerical experiments.

No complete replacement proof of the NTH long-time bound or of the non-Gaussian master theorem is claimed here. The LANTK findings concern the specified frozen arXiv v2 appendix and its definitions; this report does not establish what code or later versions implement. The direct counterexamples distinguish false written statements from proof gaps and from conclusions which remain plausible under corrected assumptions.
