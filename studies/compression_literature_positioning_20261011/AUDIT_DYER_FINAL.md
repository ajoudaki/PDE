# Independent audit: Dyer and Gur-Ari, final ICLR 2020 paper

Audit date: 2026-10-11. Scope: the complete user-supplied final paper, with one narrowly retrieved primary proof dependency. This is a venue-neutral mathematical audit, not an official conference review or a manuscript-positioning assessment. No prior study reports, other reviewers' findings, manuscript, archived book, or Git history were read. No training or supplementary code was executed.

## Source, coverage, and review format

The supplied source is *Asymptotics of Wide Networks from Feynman Diagrams*, Ethan Dyer and Guy Gur-Ari, marked “Published as a conference paper at ICLR 2020,” 35 pages, PDF creation date 2020-02-15. Its SHA-256 is `5e8c240ae9617c34e88652d7b045560a997ead9d39fce60817fe1b86cc6ec6e9`.

Source: `/home/codex-b/.codex/attachments/324dc578-0297-473c-86c1-13c26ebf62d7/1183_asymptotics_of_wide_networks_f.pdf`. Page references below are the printed PDF page numbers; they coincide with one-based PDF pages.

All pages were read, including references and every appendix. Coverage:

| Pages | Material read | Main verification |
|---|---|---|
| 1–4 | Introduction, model, correlation functions, Conjecture 1, Theorems 1–2, Table 1 | Scaling, fixed quantities, proof/conjecture distinction |
| 5–6 | Gradient flow, Lemma 1, finite-width correction, Figure 1 | Re-derived exact hierarchy and first correction; visually inspected both pages |
| 7–9 | Diagrams, one-layer proof, discussion | Reconstructed combinatorial argument |
| 9–11 | Complete bibliography | Resolved essential ReLU dependency; no recursive literature expansion |
| 11–12 | Appendix A | Initialization experiments and training settings |
| 12–17 | Appendix B | Deep-linear Wick counting, bias extension, component bound |
| 17–21 | Appendix C | ReLU dependency and shallow nonlinear proof; visually inspected pp. 18 and 21 |
| 21–23 | Appendix D | Variance, time-derivative counting, fixed-step SGD |
| 24–26 | E.1–E.2 | NTK concentration, drift, learning-rate dependence |
| 26–29 | E.3 | Hessian decomposition and spectral claims; visually inspected pp. 26–27 and Figure 11 on p. 32 |
| 29–35 | E.4 | Full continuous/discrete expansion; visually inspected all pp. 30–35 |

Text extraction and rendered pages are confined to `data/generated/compression_literature_positioning_20261011/audit_dyer_final/`. This single report combines the evidence log, claim ledger, and review, as explicitly assigned. The required review skill, its severity rubric, rigorous-math skill, and canonical-notation skill with its neural reference were read in full. The public, published-paper status makes this non-confidential; no official scoring form was requested. No submission code was supplied within this audit's scope.

## Scientific assessment

The paper supplies a useful and substantially correct calculus for initialization power counting, rigorous fixed-step results for deep linear networks, and an explicit formal hierarchy that captures the first nonlinear correction to frozen-kernel training. Its correction uses tensors from the **same finite-width initialization**, so it contains more instance-specific information than a deterministic limiting kernel. At fixed training-set size and truncation order, the hierarchy has a number of scalar entries independent of width, although its initial coefficient arrays grow rapidly with sample size and are obtained from the full network.

It does **not** establish a general finite-width, uniform-in-time approximation theorem for nonlinear networks. The main diagram rule is expressly conjectural in general depth/nonlinearity; the time-series interchange is expressly assumed; the displayed remainder estimates have no proved horizon-dependent norm/probability bound. These are substantive limitations on theorem-level use, rather than a reason to deny the formal construction or the restricted proofs.

There are also independently verified errors. The assertion that every non-NTK Hessian eigenvalue in a deep network is \(O(n^{-1})\) is false even for a two-hidden-layer linear network with one training sample. The asserted first-moment Hessian/NTK agreement fails for a smooth one-hidden-layer tanh network. Several discrete-time formulas have indexing or normalization errors that already change the order-\(n^{-1}\) coefficient. A stronger shallow-network comparison with the value of a linear correlation function is false at inputs where that linear correlation vanishes. These findings have different dependencies and severities, detailed below; none invalidates the exact continuous-time hierarchy.

## 1. Actual model, normalization, and quantifiers

To preserve the source's notation, write \(d\) for the number of hidden layers, \(D_{\rm in}\) for input dimension, \(M\) for training-set size, and \(n\) for common hidden width. Thus the source's \(d\) is a depth, not input dimension. In canonical layer notation, \(U=W^{(1)}\in\mathbb R^{n\times D_{\rm in}}\), the source \(W^\ell=W^{(\ell+1)}\in\mathbb R^{n\times n}\), and \(V^\top=W^{(d+1)}\in\mathbb R^{1\times n}\).

For a scalar output and fixed input \(x\in\mathbb R^{D_{\rm in}}\), equation (2), pp. 2–3, is equivalently

\[
h^{(1)}(x)=\sigma(Ux),\qquad
h^{(\ell+1)}(x)=\sigma(n^{-1/2}W^\ell h^{(\ell)}(x)),\qquad
f(x;\theta)=n^{-1/2}V^\top h^{(d)}(x).
\]

All entries of the unnormalized parameter vector \(\theta=(U,W^1,\ldots,W^{d-1},V)\) are independent \(N(0,1)\) at initialization. All parameters train. The theoretical main model has no biases; Appendix B.3 adds hidden biases specifically for the linear-network proof. Experiments additionally divide the input by \(\sqrt{D_{\rm in}}\), equation (15), p. 12. This is a constant when the input dimension is fixed and does not change a width exponent.

The MSE loss in Section 3 is the **sum**

\[
\mathcal L(\theta)=\frac12\sum_{a=1}^{M}r_a(\theta)^2,
\qquad r_a(\theta)=f(x_a;\theta)-y_a,
\qquad \dot\theta=-\nabla_\theta\mathcal L.
\]

There is no \(1/M\) in this definition. A mean-loss convention would rescale time or learning rate. The Gram kernel is

\[
\Theta_{ab}(\theta)=\nabla_\theta f(x_a;\theta)^\top\nabla_\theta f(x_b;\theta),
\qquad \dot r=-\Theta(\theta)r.
\]

The width estimates keep depth, inputs, input dimension, derivative order, number of correlation factors, training-set size, labels, learning rate, and discrete step count fixed. They do not provide bounds uniform in any of these quantities. The linear SGD proof allows an arbitrary fixed finite learning rate because it is a finite polynomial expansion; that fact is distinct from stability as the number of steps tends to infinity. In the frozen-kernel discrete dynamics, decay requires the relevant eigenvalues to satisfy \(|1-\eta\lambda|<1\).

## 2. Initialization counting: what survives rigorous reconstruction

For a correlation function with \(m\) derivative-tensor factors, \(n_e\) even connected components and \(n_o\) odd connected components in its contraction graph, Conjecture 1 states

\[
C=O(n^{s_C}),\qquad s_C=n_e+\frac{n_o}{2}-\frac m2.
\]

The paper labels the general result a conjecture prominently on pp. 2–3. General nonlinear depth is not covered by Theorem 1 or Theorem 2.

### 2.1 Deep-linear proof

For a depth-\(d\) linear network, every factor contributes \(n^{-d/2}\). Wick pairing and paired parameter differentiation identify neuron indices. A diagram with \(l\) free neuron-index loops contributes \(n^{l-dm/2}\), up to an input-dependent coefficient. There are finitely many diagrams at fixed \(d,m\) and derivative order.

The crucial bound can be proved without importing any topology from the cited physics paper. Let \(P_0,\ldots,P_d\) be the perfect matchings of the \(m\) network-factor vertices supplied by the \(U,W^1,\ldots,W^{d-1},V\) pairings, including forced derivative edges. Let \(c_\ell\) be the number of components of \(P_{\ell-1}\cup P_\ell\). The double-line loop count is \(l=\sum_{\ell=1}^{d}c_\ell\). Let \(c\) be the number of components in the union of all these matchings.

Initially \(P_0\) has \(m/2\) components. Adding \(P_\ell\) can merge at most \(m/2-c_\ell\) components: the previously accumulated partition is already coarser than the partition into pairs of \(P_{\ell-1}\). Consequently

\[
\frac m2-c\leq\sum_{\ell=1}^{d}\left(\frac m2-c_\ell\right),
\qquad l\leq\frac{(d-1)m}{2}+c.
\]

Thus \(l-dm/2\leq c-m/2\). Every contraction cluster remains inside a diagram component, and every diagram component has an even number of vertices because each edge type forms a matching. Hence \(c\leq n_e+n_o/2\), giving the claimed bound. This validates the high-leverage chain of Theorem 1 independently of the geometric terminology in Appendix B. The bias extension changes the path lengths and normalization per vertex, as equations (26)–(29) record; the component argument retains the same final exponent. The positive normalization exponent in the prose just before Theorem 6 is a typographical sign error; the theorem itself has the correct negative exponent.

### 2.2 Shallow smooth networks

For

\[
f(x)=n^{-1/2}\sum_{i=1}^{n}V_i\sigma(U_i^\top x),
\]

every nonzero term of a derivative tensor has one neuron index. A derivative contraction forces the relevant neuron indices to agree. Within a connected contraction cluster, the number of removed \(V\) factors is even: every contracted \(V\)-derivative removes two. Thus the parity of the remaining \(V\) factors equals the size of that cluster. Integrating the independent centered Gaussian \(V_i\)'s can leave at most \(n_e+n_o/2\) independent neuron sums. Each summand has a width-independent expectation, provided the required Gaussian moments of \(\sigma\) and its derivatives are finite. The factor \(n^{-m/2}\) then gives precisely Conjecture 1's exponent. This is the valid core of Appendix C.2.

Two qualifications are needed (L1):

* Smoothness alone does not guarantee those moments. For instance, \(\sigma(u)=e^{u^2}\) with input \(1\) gives an infinite output second moment. The proof needs explicit finite-moment assumptions; tanh and polynomial activations satisfy the needed fixed-order assumptions.
* Equations (47)/(54) strengthen the exponent statement to \(C(\cdot;f_{\rm nonlinear})=O(C(\cdot;f_{\rm linear}))\) at the same inputs. This is false when the comparator vanishes. Take two inputs \(e_1,e_2\in\mathbb R^2\) and \(\sigma(u)=u^2\). Then

  \[
  \mathbb E[f(e_1)f(e_2)]
  =\frac1n\sum_{i=1}^{n}\mathbb E[V_i^2]\mathbb E[U_{i1}^2U_{i2}^2]=1.
  \]

  For any bias-free deep linear network with the stated scaling, the corresponding covariance is \(e_1^\top e_2=0\). Thus the literal comparison would assert \(1=O(0)\). The exponent bound \(O(1)\) remains correct. Replacing the comparison of actual correlation values by the already-established exponent bound repairs the relevant conclusion.

### 2.3 ReLU equal-input proof and its direct citation

Theorem 7, pp. 17–19, concerns identical inputs only and initialization. It does not authorize general-input ReLU training expansions. Appendix E.4 itself acknowledges on p. 33 that nonsmooth activation dynamics need a separate analysis.

The only additional source retrieved was [Hanin and Nica, arXiv:1812.05994v1](https://arxiv.org/html/1812.05994v1), specifically Proposition 2 and its proof in Section 2 (PDF pp. 6–8), accessed 2026-10-11. Their sign-randomization proof supplies the claimed independent-gate representation for fixed-input Jacobians using symmetric weights and nondegenerate preactivations; the affine construction uses atomless random biases to secure the latter. Gaussian weights satisfy symmetry and moments. The audited paper instead uses zero biases. That alteration requires care: with positive probability an entire ReLU layer is inactive, so subsequent preactivations are exactly zero and ordinary Heaviside gates are not independent fair Bernoulli variables. The literal invocation therefore has a hypothesis gap. It is not an unavailable citation.

The following assessment is the audit's own deduction. The bad event for the first layer has probability \(2^{-n}\) at a nonzero fixed input. For fixed depth, successive survival failures are likewise exponentially small. One can plausibly repair the asymptotic proof by treating these events and the zero-gate convention explicitly. In addition, the source proof says it temporarily assumes no derivative contractions, but never supplies the promised extension. A signed orthogonal parameter transformation preserves fully paired derivative contractions, and away from switching surfaces a ReLU network is multilinear; this supplies a direct route to the missing extension. These are localized proof qualifications (L2), not a demonstrated counterexample to the equal-input width exponent. An exact, unconditional independence statement should not be quoted from this passage for the bias-free model.

## 3. From moments to training: precise strength and remaining gap

### 3.1 Second moments do give a probabilistic scale

Lemma 6, p. 21, is sound under Conjecture 1. For a contracted polynomial observable \(F\), its squared integrand has two copies of the cluster graph, so

\[
\mathbb E|F|^2=O(n^{2s_C}).
\]

Therefore \(F=O_{\mathbb P}(n^{s_C})\), meaning that for every \(\varepsilon>0\), some width-independent \(K_\varepsilon\) satisfies \(\mathbb P(|F|>K_\varepsilon n^{s_C})\leq\varepsilon\) at all sufficiently large widths. This is the defensible reading of “typical realizations.” It is not an almost-sure bound for all seeds, a supremum over inputs, or a uniform-in-time estimate.

The output itself remains \(O_{\mathbb P}(1)\) and random as \(n\to\infty\). Thus using the same finite-width \(f(0)\) in an approximation is essential for instance-wise comparison.

### 3.2 Fixed-step linear-network conclusions

For linear activations, \(f\) is polynomial of degree \(d+1\) in the parameters. Its Taylor expansion under one gradient step terminates. With MSE, or another fixed polynomial loss, every update becomes a finite linear combination of contracted derivative products. Adding the corresponding vertices and edges cannot increase the exponent \(s_C\) (Lemma 7). Induction over a fixed number of steps validates Theorem 9. The word “subgraph” in its last proof paragraph has the inclusion backwards, but the intended use of Lemma 7 is unambiguous.

In the difference \(\Theta_{t+1}-\Theta_t\), every nonzero term contains a connected cluster of at least three factors. The exponent is at most \(-1\); the square has exponent at most \(-2\). Finite summation over steps therefore gives Theorem 11's mean \(O(n^{-1})\) and variance \(O(n^{-2})\), and hence

\[
\Theta_t-\Theta_0=O_{\mathbb P}(n^{-1})
\]

for fixed step count, fixed learning rate, fixed inputs and fixed depth. Theorem 10's \(O(n^{-1})\) initialization variance is also supported: subtracting the product of means removes disconnected Wick diagrams, leaving connected four-vertex diagrams. The expectation has a finite expansion in \(1/n\), so it converges; the variance then proves convergence in probability.

Theorem 12's nonlinear-in-learning-rate terms similarly contain at least three connected factors and are suppressed by \(1/n\). It says that a step's leading dependence on its explicit learning-rate factor is linear, with the state at that step held fixed. It does not say that the complete trained output at step \(t\) is globally a linear function of \(\eta\).

These conclusions do not require a stable infinite training horizon. Conversely, they do not establish one: an \(O(n^{-1})\) bound whose constant depends on \(t\) says nothing about \(t=t(n)\to\infty\).

### 3.3 Continuous time and general nonlinear networks

Lemma 1 and Appendix D.2 bound each fixed-order time derivative **at initialization**, for polynomial losses, conditional on the diagram rule. The main text, p. 5, explicitly assumes analyticity in time and an interchange of the Taylor series with the width limit to infer fixed-time behavior. Appendix D.3, p. 23, expressly leaves the infinite-sum argument for general activations to future work. The statement on p. 25 that smooth activations make the model analytic is not valid for general \(C^\infty\) activations; analyticity is a separate assumption.

The distinction matters even for analytic scalar functions. For

\[
g_n(t)=n^{-1}e^{-n}(e^{nt}-1),
\]

every fixed \(k\geq1\) satisfies \(g_n^{(k)}(0)=n^{k-1}e^{-n}=O(n^{-1})\), yet \(g_n(2)\) grows exponentially. This is not a neural-network counterexample. It demonstrates why coefficientwise derivative bounds cannot replace a uniform majorant for the series.

The paper's displayed \(O(n^{-2})\) correction remainders are consequently formal/conditional in the nonlinear continuous-time setting. It supplies no explicit \(T\)-dependent estimate in a specified norm, no width threshold depending on confidence, and no proof that the necessary higher operators remain controlled along the actual trajectory. A proof could use a stopped high-probability event, uniform moment bounds, and stability of the finite hierarchy, but those arguments are absent. M1 is the resulting substantial proof gap if these formulas are used as an unconditional approximation theorem; it is **not** a finding that their formal coefficients are wrong.

## 4. Exact hierarchy, same-seed correction, and finite storage

For fixed inputs, let \(O_1(x;\theta)=f(x;\theta)\) and recursively define

\[
O_s(x_1,\ldots,x_s;\theta)
=\nabla_\theta O_{s-1}(x_1,\ldots,x_{s-1};\theta)^\top
\nabla_\theta f(x_s;\theta),\qquad s\geq2.
\]

This is an explicit scalar function of the current parameters, not merely a named unknown. \(O_2=\Theta\). For smooth gradient flow, chain rule gives the exact identities

\[
\dot O_s(x_1,\ldots,x_s;t)
=-\sum_{a=1}^{M}O_{s+1}(x_1,\ldots,x_s,x_a;t)r_a(t).
\]

The infinite hierarchy is an exact observable representation. Before truncation, it is not a finite autonomous reduction.

For finite truncation index \(q\), retain tensors with \(s\leq2q\), freeze \(O_{2q}\) at initialization, and use these equations for smaller \(s\). This is a finite autonomous polynomial ODE on the training inputs. It is a well-defined approximate model independent of whether its claimed accuracy has been proved. For \(q=1\), it is frozen-kernel dynamics. For \(q=2\), the moving entries are \(f\), \(\Theta\), and \(O_3\); \(O_4\) is fixed. Dense storage counts, ignoring symmetries, are

| Model | Moving scalar entries | Fixed initialization entries |
|---|---:|---:|
| Frozen kernel | \(M\) | \(M^2\) for \(\Theta(0)\), plus initial output/labels |
| Direct fourth-order truncation | \(M+M^2+M^3\) | \(M^4\) for \(O_4(0)\), plus initial moving state |
| General \(2q\) truncation | \(\sum_{s=1}^{2q-1}M^s\) | \(M^{2q}\), plus initial moving state |

The explicit order-\(n^{-1}\) formulas also store the fixed initial arrays \(f(0),\Theta(0),O_3(0),O_4(0)\), totaling \(M+M^2+M^3+M^4\) scalar entries before symmetry reduction. These counts are audit deductions from equations (9)–(12)/(86)–(103), not an efficiency claim made by the authors. They are width-independent for fixed \(M,q\), but not data-size independent. Computing the entries requires the full sampled network and its derivatives; the paper supplies no theorem making that initialization cost independent of width. Discrete-time corrections require additional derivative-contraction tensors of comparable fixed sample order.

To verify the continuous coefficient, define the same-initialization residual trajectory

\[
r^{(0)}(t)=e^{-t\Theta(0)}r(0).
\]

Keeping the formal first correction gives

\[
\begin{aligned}
O_3^{(1)}(x_1,x_2,x_3;t)
&=O_3(x_1,x_2,x_3;0)
-\int_0^t\sum_bO_4(x_1,x_2,x_3,x_b;0)r_b^{(0)}(u)\,du,\\
\Theta^{(1)}_{ab}(t)
&=-\int_0^t\sum_c O_3(x_a,x_b,x_c;0)r_c^{(0)}(u)\,du\\
&\quad+\int_0^t\!\int_0^u\sum_{c,e}
O_4(x_a,x_b,x_c,x_e;0)r_e^{(0)}(v)r_c^{(0)}(u)\,dv\,du,\\
r^{(1)}(t)
&=-\int_0^t e^{-(t-u)\Theta(0)}\Theta^{(1)}(u)r^{(0)}(u)\,du.
\end{aligned}
\]

These agree with equations (11)–(12) and are sound algebraic consequences of the order assignment. Replacing \(O_4(t)\) by \(O_4(0)\), and replacing the residual in correction terms by \(r^{(0)}\), are the first approximations.

The square-moment version of the conjectural counting gives

\[
O_s=O_{\mathbb P}\bigl(n^{-\lfloor(s-1)/2\rfloor}\bigr):
\quad O_1,O_2=O_{\mathbb P}(1),\quad
O_3,O_4=O_{\mathbb P}(n^{-1}),\quad
O_5,O_6=O_{\mathbb P}(n^{-2}).
\]

This explains the truncation pattern. It is not itself the missing uniform-in-time remainder proof.

The baseline \(\Theta(0)\) here is the realized finite-width kernel. Its own fluctuations are generally \(O_{\mathbb P}(n^{-1/2})\), larger than the \(O_{\mathbb P}(n^{-1})\) training drift. Calling the formula “infinite-width evolution” does not remove this finite-width seed dependence. Replacing it by a deterministic limiting kernel would discard a larger correction and require a different comparison statement.

For a fixed finite set of test queries, the required mixed query/training tensors can be included. The training-set arrays alone do not reconstruct a predictor at every new input, the original weights, or its hidden representations. Nothing in this finite-state interpretation establishes an exact compressed neural network with the same architecture-independent input function.

The correction does represent nonzero nonlinear departure from frozen tangent dynamics. Its stated scale tends to zero as \(n\to\infty\) at fixed horizon. It therefore supports perturbative feature evolution in this normalization, not an order-one feature-learning limit or a theorem excluding such limits under different parameterizations, time scales, or learning-rate scalings.

## 5. Discrete-time formulas: verified local errors and correction

The finite-step derivation is structurally useful, but several displayed equations on pp. 33–35 cannot be used as written (L3). In equation (108), the first term lacks \(\eta\), higher Taylor terms lack the appropriate \((-1)^k\), and the differentiated operator is indexed by \(t+1\) instead of the pre-update \(t\). Equation (109) lacks the additive \(y\) if it denotes the output rather than residual. Equation (113) also lacks \(\eta\). More substantively, the sums underlying (115), (119), and (121) are shifted by one step.

Let \(A=I-\eta\Theta_0\), and let \(r_k^{(0)}=A^kr_0\). The correct leading update of the third operator is

\[
O_{3,k+1}^{(1)}-O_{3,k}^{(1)}=-\eta O_{4,0}r_k^{(0)}.
\]

Consequently

\[
O_{3,k}^{(1)}=O_{3,0}-\eta O_{4,0}\sum_{j=0}^{k-1}A^jr_0
=O_{3,0}-O_{4,0}\Theta_0^{-1}(I-A^k)r_0,
\]

where the last form assumes an invertible \(\Theta_0\); the finite sum is always defined. Equation (115) instead includes an extra factor \(A\), corresponding to summing \(j=1,\ldots,k\). The same shift appears in (119). If a first-order output correction satisfies \(r_{k+1}^{(1)}=Ar_k^{(1)}+b_k\), \(r_0^{(1)}=0\), the solution is

\[
r_k^{(1)}=\sum_{j=0}^{k-1}A^{k-1-j}b_j.
\]

This both corrects the bounds in (121) and avoids its unnecessary inverse powers of \(A\), which are undefined at otherwise admissible learning rates where \(A\) is singular.

A concrete exact check makes the order of the error visible. Take one sample \(x=1\), a one-hidden-layer linear network

\[
f=n^{-1/2}v^\top u,\quad r=f-y,\quad
\Theta=n^{-1}(\|u\|^2+\|v\|^2),\quad
O_3=4f/n,\quad O_4=4\Theta/n.
\]

One gradient step gives

\[
u_+=u-\eta rv/\sqrt n,\quad v_+=v-\eta ru/\sqrt n,
\]

so, exactly,

\[
f_+=f-\eta\Theta r+\eta^2r^2f/n,\qquad
\Theta_+=\Theta-4\eta fr/n+\eta^2r^2\Theta/n.
\]

Hence

\[
O_{3,+}=O_3-4\eta\Theta r/n+4\eta^2r^2f/n^2.
\]

At one step equation (115) instead predicts \(O_3-4\eta\Theta(1-\eta\Theta)r/n\). Its error has leading term \(4\eta^2\Theta^2r/n\), generically of order \(n^{-1}\). This is a real error in the displayed first correction, not a correction beyond the retained order. The repair is nevertheless localized: use the pre-update residual and sums starting at zero. It leaves the expansion method intact, which is why the rubric classification is minor rather than fatal or major.

## 6. Hessian claims: two actual counterexamples

For MSE, with \(g_a=\nabla_\theta f(x_a)\), the loss Hessian splits exactly as

\[
H=A+B,\qquad A=\sum_a g_ag_a^\top,
\qquad B=\sum_a r_a\nabla_\theta^2 f(x_a).
\]

The nonzero spectra of \(A\) and the training NTK agree. This exact identity and the relevance of residual-weighted second derivatives survive. The following extrapolations do not (M2).

### 6.1 The first-moment assertion fails for tanh

Equations (78)/(80), p. 27, include the first moment in a purported \(O(n^{-1})\) comparison. Consider one sample \(x=1\) and

\[
f=n^{-1/2}\sum_i v_i\tanh(u_i),\qquad u_i,v_i\stackrel{\rm iid}{\sim}N(0,1).
\]

There are \(2n\) parameters. The parameter-space Laplacian is

\[
\operatorname{Tr}\nabla_\theta^2f=n^{-1/2}\sum_i v_i\tanh''(u_i).
\]

For any fixed label \(y\), independence and centering give

\[
\begin{aligned}
\mathbb E\operatorname{Tr}B
&=\mathbb E\left[(f-y)\operatorname{Tr}\nabla_\theta^2f\right]\\
&=\mathbb E[\tanh(G)\tanh''(G)]\\
&=-2\mathbb E[\tanh^2(G)\operatorname{sech}^2(G)]<0,
\qquad G\sim N(0,1).
\end{aligned}
\]

The result is a nonzero constant independent of width, so

\[
\mathbb E\operatorname{Tr}H-\mathbb E\operatorname{Tr}\Theta
=\mathbb E\operatorname{Tr}B\not=O(n^{-1}).
\]

The source's footnote correctly singles out linear/ReLU networks for \(\operatorname{Tr}B=0\), but does not restrict equations (78)/(80) to those activations. This counterexample uses tanh, an activation in the paper's experiments, with all moments finite. In the contraction graph, the two derivatives of the Laplacian contract within a single tensor; they do not create the three-vertex connected cluster invoked in the surrounding argument. Excluding the first moment or retaining its \(B\) term corrects this particular formula.

### 6.2 Deep networks can have non-NTK eigenvalues of order \(n^{-1/2}\)

Take two hidden linear layers, one-dimensional input \(x=1\), one label \(y=0\), and

\[
f=n^{-1}v^\top Wu,
\qquad u,v\in\mathbb R^n,\quad W\in\mathbb R^{n\times n},
\]

with all entries independent standard Gaussians. This is exactly the paper's depth-two normalization. The NTK has only one eigenvalue, because there is one training sample. Nevertheless, the second-largest loss-Hessian eigenvalue is at least a quantity of order \(n^{-1/2}\).

To prove this, consider the principal submatrix of \(\nabla^2f\) on the \(u\) and \(W\) parameters, excluding \(v\). It is

\[
\begin{pmatrix}0&K^\top\\ K&0\end{pmatrix},
\qquad K(\delta u)=n^{-1}v\,\delta u^\top.
\]

The Frobenius norm gives

\[
\|K(\delta u)\|_F^2=\frac{\|v\|^2}{n^2}\|\delta u\|^2,
\]

so \(K\) has \(n\) singular values equal to \(\|v\|/n\). Multiplying by the residual \(r=f\), this principal submatrix of \(B\) has \(n\) positive eigenvalues equal to \(|f|\|v\|/n\), and \(n\) corresponding negative eigenvalues. The matching principal submatrix of \(A=\nabla f\nabla f^\top\) is positive semidefinite. The min–max principle first for this sum and then for its inclusion in \(H\) therefore gives, for \(n\geq2\),

\[
\lambda_2(H)\geq\frac{|f|\|v\|}{n}.
\]

For completeness, the two uses of min–max require only that adding a positive semidefinite form cannot reduce its second-largest Rayleigh–Ritz value and that restricting a symmetric quadratic form to a coordinate subspace cannot increase that value. Both apply here.

Conditionally on \(u,v\), \(f\) is Gaussian with variance \(\|u\|^2\|v\|^2/n^2\). Thus

\[
\mathbb E\lambda_2(H)
\geq\sqrt{\frac2\pi}\frac{\mathbb E[\|v\|^2\|u\|]}{n^2}
=\sqrt{\frac2\pi}\frac{\mathbb E\|u\|}{n}
\asymp n^{-1/2}.
\]

For a self-contained final comparison, put \(S=\|u\|^2\). Independence of the Gaussian entries gives \(\mathbb ES=n\) and \(\operatorname{Var}S=2n\), so Chebyshev gives \(\mathbb P(S<n/2)\leq8/n\). Therefore \(\mathbb E\|u\|\geq\sqrt{n/2}(1-8/n)\), while Cauchy–Schwarz gives \(\mathbb E\|u\|\leq\sqrt n\). This proves the displayed asymptotic comparison. It contradicts the text below (76), p. 26, that remaining Hessian eigenvalues are \(O(n^{-1})\) for deeper networks. Since the inequality supplies positive eigenvalues, a signed-expectation cancellation cannot rescue the assertion.

The mistaken step is on p. 27: \(\operatorname{Tr}B^2=O(1)\) and parameter dimension \(P=O(n^2)\) imply an RMS over **all** eigenvalues of size \(O(n^{-1})\), not that each eigenvalue has that size. A rank-\(O(n)\) sector with individual eigenvalues \(O(n^{-1/2})\) is compatible with the same trace bound. The empirical RMS plot for one hidden layer and top-eigenvalue plot for a particular nonlinear network do not rule out this mechanism.

This refutes the universal bulk-eigenvalue assertion. It does not by itself refute the empirically observed \(O(n^{-1})\) shift of a separated top NTK eigenvalue; that more specific statement needs a separate perturbation argument. Nor does it affect the hierarchy for \(f\) and \(\Theta\).

## 7. Inverses, late-time extrapolation, and order of limits

Equations (99), (101), and (104) introduce inverse eigenvalues without requiring a positive definite training kernel. Finite-time integrals remain meaningful when the kernel is singular. In particular,

\[
\int_0^t e^{-u\Theta_0}\,du
\]

has eigenvalue \((1-e^{-t\lambda})/\lambda\), continuously extended to \(t\) at \(\lambda=0\). This is the appropriate replacement; simply inserting a pseudoinverse would omit the null-space term. The nested integrals in (11) have analogous regular extensions. A finite asymptotic limit as \(t\to\infty\) needs decay along the driving residual directions, for example strict positivity of \(\Theta_0\). These assumptions are separate from width counting.

Equation (105), p. 32, also uses the original residual as the amplitude of an exponential with the terminal corrected kernel. Even for a scalar kernel, transient kernel motion generally changes the asymptotic amplitude. Here is an exact consistency check using the shallow linear model of Section 5. Gradient flow satisfies

\[
\dot f=-\Theta(f-y),\qquad
\dot\Theta=-4f(f-y)/n.
\]

Write \(k=\Theta(0)\), \(r_0=f(0)-y\), and suppose \(k>0\). The formal first correction from the paper's own equation (11) is

\[
\Theta^{(1)}(t)
=-\frac4{nk}\left[y r_0(1-e^{-kt})+\frac{r_0^2}{2}(1-e^{-2kt})\right].
\]

Consequently

\[
\int_0^t\Theta^{(1)}(u)\,du
=\Theta^{(1)}_\infty t
+\frac4{nk^2}\left[y r_0(1-e^{-kt})+\frac{r_0^2}{4}(1-e^{-2kt})\right].
\]

After resumming the secular rate term, the first-order late-time amplitude therefore contains

\[
\exp\left[-\frac4{nk^2}\left(y r_0+\frac{r_0^2}{4}\right)\right],
\]

which is absent from (105). Thus (105) can suggest a terminal decay rate, but is not generally a first-order relative asymptotic with unchanged amplitude. Read merely as two expressions both converging to \(y\), it is much weaker. This localized extrapolation issue is L4. A uniform approximation on increasing training horizons would additionally have to control the higher-order correction to the decay rate; the finite-time expansion alone does not do that.

## 8. Empirical evidence and reproducibility

Table 1, p. 4, evaluates six correlation functions for three-hidden-layer networks, widths \(2^7\) through \(2^{13}\), and 1,000 Gaussian initializations per width; its random inputs have dimension four. Table 2 repeats with independent Rademacher weights. These are useful checks of selected exponents; agreement cannot prove the universal graph rule. The authors appropriately note nontight upper bounds for some linear/ReLU cases.

Figure 1(a) uses two-class MNIST, 1,000 samples per class, 1,024 steps, learning rate 1, and averages over 100 initializations. The first-correction trajectory plots and Figure 11 use 10 samples per class, learning rate 0.1, and individual randomly selected scalar components from individual runs. Figure 11 visibly agrees closely at width 1,024 and has appreciable deviations in some width-128 curves. This is evidence for predictive usefulness of the perturbative formulas on those trajectories. It is not a norm-wise \(O(n^{-2})\) remainder experiment: there is no width-sweep of residual error, stated confidence level for that error, or comparison over all data/kernel entries. Training accuracy one is weaker than vanishing MSE and does not itself establish an infinite-time interpolation claim.

Figure 9 checks top Hessian/NTK eigenvalue differences for the chosen architectures, while Figure 10's eigenvalue-size plot reports an RMS. Neither checks every remaining deep-network eigenvalue, which is the false universal assertion identified in Section 6.

No experimental reproduction or code-level claim is made here. The supplied object was the paper; no code inventory beyond that assigned source was authorized or performed. Complete source-level reading does not imply numerical reproduction. No data-integrity or ethical concern was found from the supplied material; none is inferred from absent execution.

## 9. Claim ledger

| Claim | Source and evidence | Plausibility | Argument verdict | Dependencies and surviving contribution |
|---|---|---|---|---|
| C1. Contraction clusters control width exponents | Conjecture 1; Theorems 1–2; Appendices B–C; Tables 1–2 | Highly plausible in proved restricted settings; plausible, explicitly conjectural in general nonlinear depth | Deep-linear high-leverage chain checked and sound; shallow exponent sound with finite moments; L1/L2 qualify stronger/proof wording | Supplies useful power counting. General-depth nonlinear applications inherit the conjecture. No independent priority search was undertaken. |
| C2. Kernel drift is \(O(n^{-1})\), and leading discrete steps use the initial NTK | Theorems 9–12; Appendix D; Figure 1(a) | Highly plausible for fixed-step deep-linear polynomial-loss setting; plausible conditionally for smooth nonlinear settings | Finite polynomial proof sound; continuous/nonlinear extension depends on unproved series control (M1) | Stronger drift scale than initialization fluctuation is supported in the restricted theorem. No uniform long-time conclusion follows. |
| C3. First finite-width correction and arbitrary-order hierarchy | Equations (9)–(12), (86)–(103), (106)–(122); Figures 1 and 11 | Highly plausible as a formal fixed-time expansion; general error theorem unsupported by supplied proof | Exact hierarchy and continuous first coefficient checked; remainder conditional (M1); displayed discrete indexing errors (L3) | Same-seed initial tensors produce a finite-width-independent array model for fixed data/order. Fixed storage and coefficient construction remain essential. |
| C4. Hessian spectrum differs from NTK only by claimed individual-eigenvalue scales | Equations (76)–(82); Figures 9–10 | Clearly false for the universal bulk scale and first-moment formula | Verified counterexamples (M2) | Exact \(H=A+B\) decomposition, nonzero-spectrum identity for \(A\), and suitably qualified moment/RMS observations survive. Top-eigenvalue empirical behavior is not refuted by the bulk example. |
| C5. Late-time corrected kernel gives the stated output asymptotic | Equations (104)–(105) | Plausible as a rate heuristic under decay/nondegeneracy; inaccurate as the displayed relative first-order formula | Missing transient amplitude and explicit spectral/horizon assumptions (L4) | Terminal-kernel interpretation can be retained with appropriate amplitude and order-of-limits analysis. |

Novelty assessment is limited to the supplied source. The derivative-contraction diagram calculus and explicit nonlinear first-correction organization are nontrivial constructions on their mathematical merits. The paper itself acknowledges overlap with Huang–Yau's hierarchy (p. 2). This audit did not retrieve that separate work and makes no independent claim about priority, uniqueness, or coverage of all prior reductions.

### Severity triage

| Category | ID | Affected claim | Rationale | Severity |
|---|---|---|---|---|
| Missing approximation proof | M1 | C2/C3 for general nonlinear continuous-time or unrestricted horizons | Requires substantial new uniform moment/series/stability estimates to turn acknowledged formal assumptions into an approximation theorem; restricted results remain reusable | Major concern for unconditional theorem use; explicitly conditional status in the source must be preserved |
| False spectral conclusions | M2 | C4, eqs. (76)–(82) | Exact smooth-network trace counterexample and exact deep-linear bulk-eigenvalue counterexample; repair materially weakens spectral scope while retaining the decomposition/moment program | Major flaw |
| Overstrong shallow comparison / missing moments | L1 | C1, eq. (54) | Comparison with a possibly zero linear correlation is false; finite-moment assumption omitted. Direct exponent bound survives with local corrections | Minor flaw |
| ReLU proof qualifications | L2 | C1, Theorem 7 | Bias-free dead-layer issue in an exact gate-independence invocation and omitted contracted-derivative extension; asymptotic repair is localized and plausible | Minor flaw / limited invocation gap |
| Discrete formula errors | L3 | C3, eqs. (108)–(121) | Missing factors and shifted geometric sums change the retained coefficient, but fixing indices/factors preserves the derivation | Minor flaw |
| Spectral inverses and late-time prefactor | L4 | C5, eqs. (99)–(105) | Finite-time zero-eigenvalue extensions and transient amplitude are omitted; terminal-rate interpretation survives with qualifications | Minor flaw |

No fatal finding is assigned. M2 does not propagate to the training hierarchy. L3 does not propagate to the continuous-time coefficient. M1 controls use of the work as a rigorous nonlinear compression/trajectory theorem, but does not erase the expressly conjectural and formal contributions.

## 10. Questions that would change the assessment

1. Can the authors specify a norm, probability level, compact time interval, activation hypotheses, and proved uniform bound for the \(O(n^{-2})\) remainder in equations (11)–(12)? A finite-step polynomial-network theorem should be distinguished from an infinite-series nonlinear extension.
2. Are the discrete formulas intended to use residuals indexed before or after an update? The one-step shallow-linear calculation above fixes the convention and yields a corrected geometric sum.
3. Is the Hessian statement intended only for RMS eigenvalue size, or for selected separated top eigenvalues? The universal remaining-eigenvalue assertion needs withdrawal or a substantially different hypothesis.
4. Is (105) intended as a decay-rate statement rather than a relative output asymptotic? Its amplitude should reflect transient kernel motion.

## 11. Safe use of the paper for width-asymptotic reduction

The source supports the following precise characterization: it develops diagrammatic power counting, proves important linear-network and restricted nonlinear initialization cases, derives an exact infinite training-observable hierarchy, and constructs explicit formal finite-width corrections based on the realized initialization. At fixed sample set and order, the truncated equations can be represented by finitely many scalar tensors independent of width. The derivation captures a vanishing nonlinear correction to NTK-regime dynamics and is supported by selected finite-width experiments.

It should not be cited as providing a general rigorously controlled nonlinear finite-state compression theorem, a width-independent cost for creating the initial arrays, a uniform guarantee over long training horizons or all inputs, reconstruction of network parameters/features, or an order-one feature-learning limit. The same-seed nature and the \(M^{2q}\)-scale fixed coefficient storage should be stated whenever its finite-state interpretation is used.

Confidence is high in the exact algebra, the two spectral counterexamples, the discrete one-step check, the model/scaling/accounting, and the absence of a supplied quantitative nonlinear remainder theorem after complete reading. Confidence is more limited in the full equal-input ReLU proof until its zero-gate and derivative details are repaired. No empirical curves were reproduced, no broad novelty comparison was attempted, and no claim is made to have disproved the general diagram conjecture.
