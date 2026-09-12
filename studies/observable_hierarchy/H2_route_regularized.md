# H2 regularized functional-calculus route

Status: a concrete finite autonomous candidate with a direct convergence argument is given below. Its remaining boundary objection is whether the problem's prohibition of “trajectory replay/history” excludes an autonomous continuous Picard cascade even though it stores no past trajectory, uses no time-indexed forcing, and is restartable from its complete finite state. This report does not silently resolve that interpretation. The construction uses interpolation of nonlinear drift evaluations; it does not project the raw state onto a chosen initialization basis.

Scope: fresh prompt-only theoretical route. Only the required mathematical skills and their research-contract/adversarial-audit references were read. No other research route, repository scientific source, experiment, or external scientific source was consulted. The fixed initialization-word realization and uniform backward-query tail assertions are used exactly as supplied in the assignment.

## 1. Contract and mechanism

Take \(0<T\le 1/200\), \(Y\ge1\), and the canonical initialization \(X_0=(g,0,0)\) in

\[
\mathcal H=L^2(\Omega _1;\mathbb R^2)\times\operatorname{HS}(L^2(\Omega _1),L^2(\Omega _2))\times L^2(\Omega _2).
\]

The component order is \(X=(w,K,c)\); \(A=A_0+K\), with \(\|A_0\|\le2\), and every transpose below is the actual Hilbert-space adjoint. Use the sum norm on \(\mathcal H\). The data law is any separately fixed law in the common neighborhood stated in the assignment.

The proposed mechanism has three independent approximation parameters:

1. Replace only the backward query in the \(w\)-velocity by \(\chi_R(q)=R\tanh(q/R)\).
2. Approximate this capped dynamics by the autonomous cascade \(X_j'=F_R(X_{j-1})\), with all stages initialized at \(X_0\).
3. Compile each nonlinear stage by Bernstein interpolation on a deterministic finite coefficient simplex. Every sampled drift is a fixed initialization-word evaluation, so all \(A_0,A_0^*\) operations occur in the permitted finite source calculation.

The actual runtime state is a finite collection of scalar coefficient vectors. Their equations are autonomous polynomial equations. The source fields are finite functions of finite-dimensional Gaussian marks furnished by the initialization premise. State and mark dimensions grow with order, never with elapsed steps or a time mesh. Law integrals enter through finitely many masses and signed label masses. No future target value is used.

This is not a claim of an efficient hierarchy. Its dimensions grow extremely rapidly.

## 2. Capped dynamics and uniform bounds

For one datum \(a=(u,y)\), write \(F_{R,a}(X)\) for the supplied gradient vector field with

\[
d_1=(1-h_1^2)\chi_R(q),\qquad \chi_R(s)=R\tanh(s/R),
\]

and all other definitions unchanged. In particular, the \(K,c\) velocities still use the actual forward and backward fields. Let \(F_{R,\mu}=\int F_{R,a}\,d\mu(a)\).

Set

\[
\bar B=1+4TY^2,\qquad a_*=2+\bar B.
\]

On the region \(\|c\|_\infty\le Y,\ \|K\|_{\rm HS}\le\bar B\),

\[
|r|\le2Y,\quad \|d_2\|_\infty\le Y,\quad \|q\|_2\le a_*Y.
\]

Because \(|\chi_R(s)|\le |s|\) and \(|\chi_R(s)|\le R\), every single-datum drift satisfies

\[
\|F^c_{R,a}\|_\infty\le4Y,\qquad
\|F^K_{R,a}\|_{\rm HS}\le4Y^2,\qquad
\|F^w_{R,a}\|_2\le4a_*Y^2,\quad
\|F^w_{R,a}\|_\infty\le4YR.
\tag{2.1}
\]

Thus a uniform sum-norm bound is

\[
B=4a_*Y^2+4Y^2+4Y.
\]

For existence, one may temporarily extend the vector field to all of \(\mathcal H\) by pointwise clipping \(c\) to \([-Y,Y]\), and projecting \(K\) to the closed HS ball of radius \(\bar B\), wherever these variables enter the drift. Those two maps are 1-Lipschitz in their Hilbert norms. The extended drift is globally Lipschitz for fixed \(R\), as verified below, and is bounded in \(\mathcal H\). Picard contraction on sufficiently short subintervals therefore constructs its unique global flow. Bounds (2.1) imply

\[
\|c(t)\|_\infty\le4TY<Y,\qquad
\|K(t)\|_{\rm HS}\le4TY^2<\bar B
\]

through \(T\). The auxiliary clips never activate. They are used only for this existence proof, not as operations in the source compiler. The same bounds apply to the uncapped actual flow on this horizon by the corresponding first-exit argument.

For \(X,\widetilde X\) in this region, let \(e=\|X-\widetilde X\|_{\mathcal H}\). At every \(u\in S^1\),

\[
\begin{split}
\|h_1-\widetilde h_1\|_2&\le e,\\
\|h_2-\widetilde h_2\|_2&\le a_*e,\\
\|d_2-\widetilde d_2\|_2&\le(1+2Ya_*)e,\\
\|q-\widetilde q\|_2&\le Qe,\qquad Q=a_*(1+2Ya_*)+Y,\\
|f-\widetilde f|&\le He,\qquad H=1+Ya_*.
\end{split}
\tag{2.2}
\]

For example, split \(Ah_1-\widetilde A\widetilde h_1=A(h_1-\widetilde h_1)+(K-\widetilde K)\widetilde h_1\), using \(\|\widetilde h_1\|_2\le1\). Split \(c(1-h_2^2)-\widetilde c(1-\widetilde h_2^2)\) with the bounded \(c\) factor on the activation difference. No \(L^2\times L^2\to L^2\) multiplication estimate is used.

Since \(\chi_R\) is 1-Lipschitz and bounded by \(R\), an admissible drift Lipschitz constant in the sum norm is

\[
\begin{split}
L_R={}&2Ha_*Y+4Y(2R+Q)\\
&+2HY+4Y(1+2Ya_*+Y)+2H+4Ya_*.
\end{split}
\tag{2.3}
\]

This bound is uniform over the data law and is affine in \(R\).

## 3. Identification of the capped limit with the actual gradient flow

A naive \(L_R\)-Gronwall comparison would multiply a polynomial cap error by \(\exp(CRT)\). That argument does not prove convergence. Instead, use the actual flow's given backward-query tails.

Here is the precise tail form sufficient for the argument: there are constants \(\alpha,M>0\), uniform over the stated law neighborhood, \(t\le T\), and \(u\in S^1\), such that

\[
\mathbb E_1 e^{\alpha|q(t,u)|}\le M.
\tag{3.1}
\]

Uniform subGaussian tails imply (3.1). If “uniform exponential tails” in the supplied premise means a probability tail bound, integrating that bound gives (3.1) with a smaller positive exponent.

If \(\|v\|_\infty\le2\) and \(\|v\|_2\le e\le e^{-1}\), splitting at \(\ell=(4/\alpha)\log(1/e)\) gives

\[
\|qv\|_2\le \ell e+2\|q\mathbf1_{|q|>\ell}\|_2
\le C e(1+\log(1/e)).
\tag{3.2}
\]

The tail term is bounded by a constant times \((1+\ell)e^{-\alpha\ell/2}\), which is at most a constant times \(e^2(1+\log(1/e))\). This proves (3.2) using only the true flow's tail, not a tail estimate for approximate solutions.

Let \(X_R\) be the capped flow and \(X\) the actual flow, coupled on the original two probability spaces. With \(s=1-h_1^2\), the difficult term decomposes exactly as

\[
s_R\chi_R(q_R)-sq
=s_R[\chi_R(q_R)-\chi_R(q)]
 +(s_R-s)q+s_R[\chi_R(q)-q].
\tag{3.3}
\]

The first term has the \(R\)-independent bound (Qe), by (2.2). The middle term is controlled by (3.2), since \(|h_{1,R}-h_1|\le2\) and \(|s_R-s|\le2|h_{1,R}-h_1|\). Finally,

\[
|s-R\tanh(s/R)|\le |s|^3/(3R^2),
\]

because \(x-\tanh x=\int_0^x\tanh^2v\,dv\) for \(x\ge0\). Consequently the last term in (3.3) has uniform \(L^2\) norm at most \(C/R^2\), using the sixth moment supplied by (3.1).

All remaining drift differences obey (2.2) with constants independent of \(R\). Hence

\[
e_R(t)\le C\int_0^t\rho(e_R(s))\,ds+CT/R^2,
\qquad \rho(e)=e(1+\log(1/e))\quad(0<e\le1),
\tag{3.4}
\]

with an increasing continuation of \(\rho\) beyond 1. To see directly that this forces convergence, set \(\eta=CT/R^2\) and \(z(t)=\eta+C\int_0^t\rho(e_R(s))ds\). Then \(e_R\le z\), \(z(0)=\eta\), and \(z'\le C\rho(z)\). While \(z\le1\), separation of variables gives

\[
z(t)\le \exp(1-e^{-Ct})\eta^{e^{-Ct}}.
\tag{3.5}
\]

For large \(R\), this bound remains below 1 on ([0,T]), justifying the interval used to derive it. Thus

\[
\sup_{t\le T}\|X_R(t)-X(t)\|_{\mathcal H}\longrightarrow0.
\tag{3.6}
\]

This identifies the target dynamically, by comparison with the given strong gradient flow. It uses neither temporal analyticity nor uniqueness of a formal moment hierarchy. The schedule \(R_n=n\) needs no access to the trajectory or to numerical values of the tail constants.

## 4. A source dictionary independent of the law

Choose a finite circle grid \(u_i\) with nearest-grid map \(P\) and maximum distance \(\delta\). Let

\[
p_i=\mu(P(u)=u_i),\qquad
m_i=\int_{P(u)=u_i}y\,d\mu,
\qquad
\lambda_{i,\pm}=(p_i\pm m_i/Y)/2.
\tag{4.1}
\]

These weights are nonnegative and sum to one. Since each gradient component is affine in \(y\),

\[
F_{R,\mu}^{\delta}(X)
=\sum_{i,\sigma=\pm1}\lambda_{i,\sigma}F_{R,(u_i,\sigma Y)}(X)
\tag{4.2}
\]

is exactly the law integral with only \(u\) replaced by (P(u)). No label approximation is made in the gradient. The atomic endpoint law need not itself lie in the given neighborhood: its capped drift is globally defined by Section 2, and all comparisons are to the actual original-law flow.

On \(\|w\|_2\le\|g\|_2+BT\), repeated use of (2.2) with \(\|h_1(u)-h_1(v)\|_2\le\|w\|_2|u-v|\) gives

\[
\sup_X\|F_{R,\mu}^{\delta}(X)-F_{R,\mu}(X)\|_{\mathcal H}\le D_R\delta,
\tag{4.3}
\]

where \(D_R\) is computable from \(Y,T,R\) and \(\|g\|_2=\sqrt2\). For example, with \(M_w=\sqrt2+BT\), one may take

\[
D_R=10Y^2a_*^2M_w+8YRM_w+4a_*Y^2
+10Y^2a_*M_w+4Y^2M_w+6Ya_*M_w.
\]

The three groups are respectively the \(w,K,c\) velocity bounds obtained by the same product splitting as (2.2). The additional \(u\) factor in the \(w\)-velocity contributes \(4a_*Y^2\). Only the bounded \(\chi_R\) multiplier produces a term proportional to \(R\).

In the construction below all sample vectors use the fixed atoms \((u_i,\pm Y)\). Thus the dictionary itself is independent of \(\mu\); the only law-dependent runtime constants are the \(\lambda\)'s.

## 5. Autonomous Bernstein compilation of the continuous cascade

Let \(\Delta_m(T)=\{\beta\in\mathbb R^m:\beta_b\ge0,\ \sum_b\beta_b\le T\}\). A stage represents

\[
X_j(\beta_j)=X_0+\sum_{b=1}^{m_j}\beta_{j,b}V_{j,b},
\tag{5.1}
\]

where \(V_{j,b}\in\mathcal H\) are fixed source vectors. There is no raw-state projection in (5.1): the vectors are generated by the nonlinear sampling rule below.

For stage 1, use one vector \(V_{1,a}=F_{R,a}(X_0)\) per input atom and let

\[
\beta'_{1,a}=\lambda_a,\qquad\beta_{1,a}(0)=0.
\]

Suppose stage (j-1) has been constructed. Pick a Bernstein degree \(d_j\). For every multi-index \(k=(k_0,\ldots,k_{m_{j-1}})\) with nonnegative entries summing to \(d_j\), put

\[
\xi_k=T(k_1,\ldots,k_{m_{j-1}})/d_j,
\qquad
V_{j,k,a}=F_{R,a}\bigl(X_{j-1}(\xi_k)\bigr).
\tag{5.2}
\]

These are fixed source vectors, constructed before evolution. For \(\beta\in\Delta_m(T)\), set \(p_b=\beta_b/T\), \(p_0=1-\sum_bp_b\), and

\[
\mathcal B_k(\beta)=\frac{d_j!}{\prod_b k_b!}\prod_{b=0}^{m}p_b^{k_b}.
\]

The finite autonomous equations are

\[
\beta'_{j,k,a}=\lambda_a\mathcal B_k(\beta_{j-1}),
\qquad \beta_{j,k,a}(0)=0.
\tag{5.3}
\]

Every right side is polynomial in the current finite state. On the simplex it is nonnegative, and the sum of all right sides is one. Induction in \(j\) therefore gives

\[
\beta_j(t)\ge0,\qquad \sum_b\beta_{j,b}(t)=t\le T.
\tag{5.4}
\]

All source nodes and all decoded states satisfy the Section 2 bounds: their increments are nonnegative combinations of drift vectors with coefficient sum at most \(T\). This inductively justifies (2.1) for every new source vector and proves \(\|V_{j,b}\|_{\mathcal H}\le B\).

The interpolation error has an elementary probabilistic proof. If \(Z\) is multinomial with \(d\) trials and probabilities \(p_0,\ldots,p_m\), then the Bernstein interpolant is the expectation of the sampled map at (TZ/d). Cauchy–Schwarz gives

\[
\mathbb E\|TZ/d-Tp\|_1\le T\sqrt{(m+1)/d}.
\]

The coefficient-to-state map (5.1) is \(B\)-Lipschitz from \(\ell^1\) to \(\mathcal H\). Hence choosing

\[
d_j\ge(m_{j-1}+1)(L_RBT/\varepsilon)^2
\tag{5.5}
\]

ensures

\[
X_j'(t)=F_{R,\mu}^{\delta}(X_{j-1}(t))+E_j(t),\qquad
\|E_j(t)\|_{\mathcal H}\le\varepsilon.
\tag{5.6}
\]

This is interpolation of entire nonlinear drift evaluations over a known finite coefficient domain. It is not a truncation of moment evolution equations.

## 6. Direct finite-stage error and a deterministic schedule

Let \(X_R\) be the actual capped flow with the original law, and \(e_j(t)=\|X_j(t)-X_R(t)\|_{\mathcal H}\). Equations (4.3) and (5.6) give

\[
e_j(t)\le L_R\int_0^t e_{j-1}(s)ds+(\varepsilon+D_R\delta)t,
\qquad e_0(t)\le Bt.
\]

Repeated integration yields the explicit estimate

\[
\sup_{t\le T}e_J(t)
\le \frac{BT(L_RT)^J}{(J+1)!}
+(\varepsilon+D_R\delta)T e^{L_RT}.
\tag{6.1}
\]

There is no assumption about a Taylor series of the target trajectory: the factorial comes from the volume of nested integration simplices and a Lipschitz estimate.

A universal schedule is:

\[
R_n=n,\qquad
\varepsilon_n=\frac{e^{-L_{R_n}T}}{n(1+T)},\qquad
\delta_n\le\frac{e^{-L_{R_n}T}}{n(1+T)(1+D_{R_n})},
\]

choose \(J_n\) large enough that the first term of (6.1) is at most (1/n), and recursively choose each degree by (5.5). All these choices use only order, fixed structural constants and deterministic source construction; none uses the target trajectory or elapsed computational steps. Combining (6.1) with (3.6) proves

\[
\sup_{t\le T}\|X_{J_n}(t)-X(t)\|_{\mathcal H}\longrightarrow0.
\tag{6.2}
\]

## 7. Why every source is admissible, including transpose reuse

Inductively, a source-node \(w\) is \(g\) plus a finite affine combination of bounded source functions; \(c\) is a finite combination of bounded source functions; and \(K\) is a finite sum of tensors \(\ell\otimes b\) with bounded layer-two and layer-one factors. Therefore, for a bounded fixed node operand \(\phi\),

\[
A\phi=A_0\phi+\sum_s\gamma_s\ell_s\langle b_s,\phi\rangle_1,
\]

and for a bounded fixed node operand \(\psi\),

\[
A^*\psi=A_0^*\psi+\sum_s\gamma_sb_s\langle\ell_s,\psi\rangle_2.
\tag{7.1}
\]

Each new \(A_0\) or \(A_0^*\) call in (5.2) is thus applied to a bounded fixed initialization word. Tanh, affine operations and bounded products construct the other fields. All scalar contractions and residual coefficients are exact expectations of already constructed finite words. There is no circular coefficient definition.

The assignment's finite Gaussian source-law premise therefore supplies a finite common Gaussian-mark representation for every layer's complete finite dictionary, including all reused-adjoint responses. Runtime needs only the finite coefficient equations and precomputed contraction constants. There is no runtime arbitrary-vector operator call and no newly sampled independent transpose.

The tensor and contraction indices label sampled observable source functions. They have no neuron index and are not an original \(n\times n\) middle matrix renamed. The actual \(K\) is represented only by the generated finite source tensors. The construction never samples a representative dense neural network.

## 8. Whole-circle predictions and all separately fixed finite joint words

For any fixed admissible complete word \(W\), its current-state map \(X\mapsto W(X)\) is \(L^2\)-Lipschitz on the above region, with a constant depending on the word. This follows by induction through its syntax:

* affine, sin, cos and tanh operations obey their scalar Lipschitz estimates;
* multiplying two bounded operands costs their two uniform bounds;
* an \(A\) step on bounded \(\phi\) obeys
  \(\|A\phi-\widetilde A\widetilde\phi\|_2\le a_*\|\phi-\widetilde\phi\|_2+\|K-\widetilde K\|_{\rm HS}\|\widetilde\phi\|_2\);
* the \(A^*\) step has the identical adjoint estimate.

This assertion concerns the stated grammar with bounded operands for products and operator steps; it does not assert continuity for unrestricted \(L^2\) products.

At runtime even a readout may not apply \(A_0\) to a new operand. Compile the map

\[
\beta\longmapsto W\left(X_0+\sum_b\beta_bV_{J,b}\right)
\]

by another Bernstein interpolation over \(\Delta_{m_J}(T)\), sampling fixed word values at its nodes. The same proof as (5.5), with the word's Lipschitz constant, makes its \(L^2\) error at most (1/n). Each node readout is another allowed finite initialization word. Input angles and other finite word parameters can be covered by deterministic finite grids, using their \(L^2\) continuity; the angle variable remains a finite-dimensional readout coordinate. For example, \(\|A_0\tanh(g\cdot u)-A_0\tanh(g\cdot v)\|_2\le2\sqrt2|u-v|\).

A single universal hierarchy can exhaust finite word grammars, compact coefficient boxes and their parameter grids. Each separately fixed finite tuple then occurs, with increasingly fine readout approximation, at all sufficiently large orders. All sampled readouts for a given order use their joint finite Gaussian source law, not separate marginal draws.

For a same-layer tuple \(W_1,\ldots,W_k\), couple these source realizations with their defining canonical words. Equation (6.2) and the readout errors give

\[
\sup_{t\le T}W_2\bigl(\operatorname{Law}(\widehat W_{1,n},\ldots,\widehat W_{k,n}),
\operatorname{Law}(W_1(X(t)),\ldots,W_k(X(t)))\bigr)
\le\sup_{t\le T}\left(\sum_{j=1}^k\|\widehat W_{j,n}-W_j(X(t))\|_2^2\right)^{1/2}\to0.
\tag{8.1}
\]

Include initialized words in the same source list to obtain paired initialized/current convergence. Keeping the same source Gaussian marks is essential here. Both \(A\) and \(A^*\) readouts are included by the preceding induction.

The prediction map satisfies, uniformly in \(u\in S^1\),

\[
|f_X(u)-f_{\widetilde X}(u)|\le(1+Ya_*)\|X-\widetilde X\|_{\mathcal H}.
\]

Its parameter dependence is uniformly continuous through \(\|w\|_2\le\sqrt2+BT\). Compiling the prediction readout over coefficient nodes and a circle grid therefore gives

\[
\sup_{t\le T,\ u\in S^1}|\widehat f_n(t,u)-f(t,u)|\to0.
\tag{8.2}
\]

One may compute this readout from finitely many exact scalar source contractions. No law density over raw parameters is retained.

## 9. Adversarial boundary audit and conclusion

**Restartability.** The complete state is \((\beta_1,\ldots,\beta_J)\). Its current values determine every future derivative. Stopping at \(t_0\) and resuming these same equations reproduces its continuation without retaining any function of past time. Bounds hold for the remaining portion of the prescribed horizon. Resetting auxiliary stages from only the final decoded \(X_J(t_0)\) is a different operation, and is not claimed.

**Replay interpretation: major admissibility boundary.** The cascade stages are instantaneous approximations indexed by approximation depth, not snapshots of the past. Their equations and source samples are generated from the model and initialization before training, not from an observed trajectory. Nevertheless the triangular polynomial system has solutions that are finite polynomials in time, and its frozen base stage remains anchored at initialization. If “no trajectory replay” is intended to prohibit *any* initialization-anchored continuous Picard realization, even one with an autonomous restartable full state and no saved past, this witness fails that extra interpretation. The convergence argument remains valid; the admissibility conclusion would not. This issue must be decided explicitly in comparison with the intended contract.

**Raw projection interpretation: boundary requiring precise language.** Decoded states do lie in finite affine spans, as any finite source expansion does. The selection mechanism here is not projection of \(w,K,c\) onto an initialized basis: it is recursively sampled nonlinear functional calculus over deterministic coefficient simplices, with exact generated products and adjoint responses. If the exclusion instead bans *every* finite affine source expansion of raw states, the present witness is excluded. It should not be relabeled to conceal this fact.

**Analyticity and moments.** No temporal analyticity, moment determinacy, Stieltjes representation, or formal hierarchy uniqueness is used. Exact finite joint initialization laws, rather than moment inversion, supply source realizations. Products are estimated with bounded factors, and the single unbounded backward multiplier is handled by (3.2).

**Uniformity.** All source grids, caps, cascade depths and degrees are determined without the target trajectory. Source dictionaries can be independent of the data law through (4.1). The true-flow comparison uses the common neighborhood's supplied uniform tail bound. No uniform claim over arbitrary unbounded word families is made: each fixed finite tuple is handled separately as required.

**Claim ladder.** The fixed finite construction, source provenance, autonomous equations, direct finite-stage error, cap identification and observable error bridges are derived above under the supplied initialization and tail premises. The statement that this is an admissible witness retains the two explicit representation-boundary questions above. No no-go conclusion about other closures follows if this witness is excluded.

The most useful comparison question is therefore narrow: does the intended ban on replay or raw projection exclude this explicitly specified coefficient ODE, despite its model-generated source samples, instantaneous finite auxiliary state, direct identification with the actual gradient flow, and absence of past-time forcing?
