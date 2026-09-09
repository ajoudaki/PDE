# Independent audit of the complete same-label assembly

Date: 2026-09-06.

## Verdict and scope

**PASS for the modular same-label subtheorem: no blocking mathematical gap was found in the complete assembly and nontriviality supplement, using only the dependencies identified below.**

This verdict includes construction, uniqueness and restart, the raw Hilbert gradient, the all-finite physical clock, nonsymmetric finite GD/GF comparison, the stated observations, and the two-sample nonlinearity/nonfreezing and initial nonlazy conclusions. It is not limited to checking the new comparison formulas.

This is **not a PASS for the full two-label target**. The opposite-label global continuation is not established by these documents. In particular, the response estimate on feature time \([0,3/2]\) does not establish that an opposite-label trajectory reaches its fitting level during that interval. Nor is the present collection a single final self-contained theorem document.

There are no required mathematical repairs to the same-label conclusions at the scope stated here. Two presentation corrections and several precise qualifications are recorded at the end. The calculations below explain the verdict, including the limiting arguments that cannot be replaced by a purely formal gradient calculation.

This audit used no prior review, task history, other agent, experiment, numerical simulation, or external mathematical source. The required procedural skill was read by the reviewer directly.

## 1. Source identity and dependency boundary

The following are SHA-256 hashes of the complete source files. They were checked before the audit and again before writing this review and were unchanged.

| Alias | Source | SHA-256 |
|---|---|---|
| A | /tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_GLOBAL_ASSEMBLY.md | 2ad0d70ec48eb56dc4170c90df1075e02c8d208913e2dd4fcb4f77d2702baa57 |
| N | /tmp/l3-two-sample-proof-DLuelg/SAME_LABEL_NONTRIVIALITY.md | 76124a7552d67304a7e43212b4461ca53c9d79a214af80761f6560012bdf48b6 |
| E | /tmp/l3-two-sample-proof-DLuelg/EXACT_TWO_SAMPLE_REDUCTION.md | 432f98ff185c797901a81f83c72e4217395d0100f0804b0e609b98db83182e60 |
| B | /tmp/l3-two-sample-proof-DLuelg/TWO_SAMPLE_SHORT_RESPONSE_BOOTSTRAP.md | 9305453f933ad30a0e813e4e97942ee9e00490ce726d70142b25c8f67a475170 |
| D | /tmp/l3-standalone-proof-D6AW4s/L3_GLOBAL_SELF_CONTAINED_PROOF.md | bebbb70a8f8da8fd2fa5304fc7af08026e72aef73e20f77f046509f87e63954e |

Procedural source:

- /etc/codex/skills/solve-math-rigorously/SKILL.md, read completely; SHA-256 9be5cb903f8957c5da9e2acfb1302eba4ba45e3ef9d45e30b9740ad7dbc8cff7.

A, N, E, and B were read completely. D was restricted as follows:

- Section 2, lines 165–257: elementary activation/operator bounds, Wasserstein and product convergence, the curve chain rule, and Gronwall.
- Section 3, lines 258–476: finite adaptive Gaussian conditioning, empirical averaging, source/response identities, and singular-Gram removal.
- Section 5, lines 621–791: countable common-space construction, bounded initial actions and actual adjoints, and the fixed-program/fixed-clip approximation framework. The one-input transformed-coordinate equations appearing there were not imported as two-input equations; A and B supply their raw replacements.
- **Only additional section:** Section 7 was inspected, lines 980–1061, because A lines 149–152 explicitly cite its scalar Gaussian-tail calculation. The mathematical fact used from it is exactly lines 1020–1030:
  \[
  \mathbb E e^{q^2/K^2}\le2
  \ \Longrightarrow\
  \mathbb E[q^2\mathbf1_{\{|q|>u\}}]\le4K^2e^{-u^2/(2K^2)},
  \qquad
  \|(|q|-R/2)_+\|_2\le2K e^{-R^2/(16K^2)}.
  \]
  Its short proof is also checked below. No one-input clipping-removal, existence, or uniqueness conclusion from that section is used.

No mathematical content from D Sections 1, 4, 6, or 8–12 was used. In particular, neither a one-input response estimate nor a one-input positivity/nonfreezing theorem substitutes for the corresponding two-input argument.

Line references in this review refer to these hashed versions.

## 2. What the same-label conclusion actually covers

The reconstructed statement fixes the normalized input pair and its correlation \(-1\le\rho<1\), takes the initialization and metric of E lines 11–29, the fixed activation \(1+\arctan(z)/10\), common labels in \(\{-1,1\}\), and physical GD step size \(\eta_n=n^{-2}\).

The population readout starts at zero. The actual finite Gaussian readout is compared to that auxiliary zero-readout initialization; it is not silently set to zero in the original finite system.

The documents establish:

1. A unique uncut raw feature flow on \(0\le s\le3/2\), in the constructed common spaces, with uniqueness against bounded-primal integral solutions and uniqueness on restart.
2. A same-label physical flow at every finite \(t\), obtained from a feature interval ending strictly before its fitting level. Physical uniqueness does not presuppose symmetry of a competitor.
3. Full-sequence convergence in probability on each fixed finite physical horizon for the stated finite-dimensional same-neuron laws and observations, with joint times and both samples. Actual GD and GF also approach each other in the same-width state distance of A.
4. The stated preactivation/feature path laws, all four \(2\times2\) kernel blocks, predictions, loss, and the named backward and hidden-velocity observations.
5. Strict affine-regression error for every marginal preactivation/feature pair at every reached time; nonzero hidden preactivation and feature velocities for both samples at each positive finite physical time; a nonzero \(t^2\) initial feature displacement in each sample/layer; and a nonconstant total kernel.

Constants and strict positive bounds may depend on the fixed input correlation. Hidden velocities vanish initially because the population readout is zero; the nonfreezing assertion is for positive times. No conclusion here asserts a uniform-in-\(t\) finite-width limit on the entire half-line or a positive velocity at the infinite-time fitting endpoint.

## 3. Raw metric, complete state space, and current-state autonomy

### 3.1 Normalization and the degenerate input pair

E lines 39–64 give the correct metric gradients. With
\[
\langle u,v\rangle_n=n^{-1}u^Tv,
\]
the first block is \(\delta^{(1)}_a x_a^T/d\), the middle blocks are \(\delta^{(\ell)}_a(h^{(\ell-1)}_a)^T/n\), and the readout block is \(h^{(3)}_a\). This gives exactly the factors \(C_{ab}\), \(1/n\), and products of two normalized inner products in the kernel entries.

For \(-1<\rho<1\), the population first-pair tangent norm is
\[
\mathbb E[v^TC^{-1}v].
\]
The matrix-gradient norm is Hilbert–Schmidt and the readout norm is \(L^2\). The eigenvalues \(1\pm\rho\) of \(C\) show equivalence of this first-pair norm and the sum of its two \(L^2\) norms for fixed \(\rho\).

At \(\rho=-1\), write the first state as \(Z_2=-Z_1=-Z\). A variation is \((v,-v)\), and its raw squared norm is \(\mathbb E v^2\), not a singular inverse-covariance expression. For \(g=(f_1+f_2)/2\), its first derivative is
\[
\frac12\mathbb E[(\delta^{(1)}_1-\delta^{(1)}_2)v].
\]
Consequently its first raw gradient is
\[
\frac12(\delta^{(1)}_1-\delta^{(1)}_2),
\]
which agrees with the first row of A (2). The second row is its negative. Thus the singular case has both the correct metric and the correct invariant subspace.

### 3.2 Completeness is used in the right norm

For construction, the ambient state space is
\[
L^2(\Omega_1)^2
\times\mathcal B(L^2(\Omega_1),L^2(\Omega_2))
\times\mathcal B(L^2(\Omega_2),L^2(\Omega_3))
\times L^2(\Omega_3),
\]
with A's sum norm; at \(\rho=-1\), take the closed first-pair subspace. Each factor is Banach. Its continuous-path space with the uniform norm is complete.

One must not assert that an affine Hilbert–Schmidt subspace is complete in operator norm. A avoids that error: it first constructs in the full bounded-operator Banach space, then proves convergence of the rank-one integrals in Hilbert–Schmidt norm, A lines 174–177. The latter follows from
\[
\|u\otimes v-\tilde u\otimes\tilde v\|_{\rm HS}
\le \|u-\tilde u\|_2\|v\|_2+
     \|\tilde u\|_2\|v-\tilde v\|_2.
\]
Thus the limiting trained operators are their fixed initial bounded actions plus Hilbert–Schmidt increments. The limiting derivatives are also continuous in this Hilbert norm, by the same rank-one estimate and strong continuity of the backward fields. This supplies the regularity needed for the raw Hilbert chain rule.

### 3.3 The state does not require an additional history variable

D Section 5 constructs the initial actions on equivalence classes of generated coordinates and extends them to all of the respective \(L^2\) spaces. The norm inequality passes on every finite rational combination. Density then gives a bounded operator; passing exact finite transpose pairings gives its actual adjoint.

The entire learned rank-one integral is part of the current operator \(W^{(\ell)}\). The fields in A lines 55–68 use only the current first fields, current operators, and current readout. Source histories describe the laws of finite programs; they are not additional evolving inputs to this vector field.

Replacing D's bottom root by the Gaussian pair changes none of the consistency, density, or operator arguments. A singular within-neuron root covariance is allowed. There is no cross-layer coordinate identification or transpose resampling.

## 4. Finite-program identification and the short response bootstrap

### 4.1 Gaussian conditioning is applicable to these programs

D Section 3 conditions on previous matrix queries. Its residual formula is a conditional Gaussian formula for the unexplored matrix, not an assertion that trained coordinates are independent. Conditional empirical averaging supplies laws of full same-neuron tuples and their second moments.

At fixed caps and fixed finite Euler mesh, every relevant nonlinear coordinate instruction in B can be made globally Lipschitz with bounded first derivatives. In particular:

- The clipped products \(\phi'(Z)\tau_R(q)\) have bounded factors and bounded derivatives.
- The readout has the deterministic pointwise bound \(aS\), so its occurrence in the top product can be smoothly extended outside an interval containing all attained values.
- Learned matrix terms are finite rank-one sums. Their empirical coefficients are scalar contractions that converge, and their restoration is a finite Lipschitz induction.

The two current sample queries are computed before simultaneous parameter updates. Unrolling the matrix updates gives precisely the learned forward coefficient
\[
\frac{\Delta}{2}y_b\mathbb E[H_{ka}H_{rb}]
\]
and learned reverse coefficient
\[
\frac{\Delta}{2}\mathbf1_{\{r<k\}}y_b
\mathbb E[\delta_{ka}\delta_{rb}].
\]
The other terms in B (2) are the initial-action response terms from D Section 3.3. The time ranges \(r<k\) in the forward response and \(r\le k\) in the reverse response are correct.

The singular-Gram argument is essential and present. At fixed added input noise, the limiting Grams are invertible. Finite Lipschitz/operator comparison removes that noise uniformly in width for each fixed program. The causal source recursion and bounded formal derivatives identify its zero-noise limit. This applies both at \(\rho=-1\) and at zero readout.

In particular, B lines 132–140 correctly retain zero-variance source slots. A source equal to zero almost surely may have a nonzero formal reverse-source derivative. Deleting it would not be justified. The displayed derivative convention fixes the coefficients while differentiating; it does not differentiate covariance selection.

### 4.2 The response estimate closes without a current-time circularity

The order in B lines 142–146 is valid:
\[
A^{(2)},\,Z^{(2)},\,A^{(3)},\,Z^{(3)},\,\delta^{(3)},
\,B^{(3)},\,q^{(2)},\,\delta^{(2)},\,B^{(2)}.
\]
Only already bounded \(U_r,V_r\), \(r<k\), are used in the forward sensitivity estimates. The current \(V_k\) is bounded before it is used to bound the current \(U_k\).

The crucial two-sample counts are correct. A single source produces one direct injection, of size at most \(\Delta/20\) in the raw bottom coordinate. Summing two update samples with coefficient \(\Delta/2\) contributes \(\Delta\), not \(2\Delta\). The absolute row sum of \(C/2\) is at most one, including at \(\rho=-1\).

The bottom gate derivative is genuinely present:
\[
|d(\phi'(Z)\tau_R(q))|
\le |q|\,|dZ|/5+|dq|/10.
\]
It is controlled by a Gaussian-source maximum and discrete Gronwall; it is not replaced by the one-input transformed-coordinate cancellation.

For two possibly correlated centered Gaussians,
\[
\mathbb E e^{\lambda\max_a|G_a|}
\le\sum_a\mathbb E e^{\lambda|G_a|}
\le4e^{\lambda^2v/2}.
\]
Time Jensen needs no independence between time slots. This verifies the use of that bound in both sensitivity envelopes.

The resulting constants have the required strict margins:

| Quantity | Bound checked in B | Consequence |
|---|---|---|
| Bottom expected sensitivity envelope | \(<6\) | \(a^2+6/100<3/2\) |
| Middle expected sensitivity envelope | \(<8\) | \(a^2+(3/2)8/100=1333/900<3/2\) |
| Middle sensitivity \(L^2\) norm | \(<7/2\) | Enough for the current bottom-response estimate |
| Current top-response row | \(V_*=3067/3200<1\) | Current \(q^{(2)}\) is controlled before \(U_k\) |
| Current middle-query norm | \(Q_*=24829/19200\) | Source variance and covariance-row control |
| Current bottom-response row | \(71063018523/73728000000<97/100\) | The induction closes |

The learned covariance term in the last estimate is \(S Q_*^2/100\), which at \(S=3/2\) is \(3Q_*^2/200\). The factor used in B (16) is correct.

### 4.3 Both actual cut queries have the claimed envelopes

B proves \(q=\zeta+\beta\), with \(|\beta|\le a\) and \(\operatorname{Var}\zeta\le(7/40)^2\), for each query, sample, cap, and mesh node. Independence of \(\beta\) and \(\zeta\) is not needed:
\[
\mathbb E e^{q^2/16}
\le e^{a^2/8}\mathbb E e^{\zeta^2/8}
\le e^{49/288}(1-49/6400)^{-1/2}<2.
\]
These are the queries of the actual clipped Euler law identified above.

For fixed cap, strong Euler-to-flow convergence gives the query laws at an arbitrary time by using mesh nodes tending to that time. Fatou then gives the same non-strict bound for the cut flow. This is a pointwise-in-time deterministic moment bound with a uniform constant; it does not require one almost-sure convergence event covering all times.

## 5. Fixed clips and the two-cut asymmetric estimate

### 5.1 Fixed-cap construction is legitimate on the constrained path set

A lines 75–83 give width- and cap-independent primal bounds in the proper order: readout, third operator, second operator, then first coordinates. Bounded activations, bounded gates, and \(|\tau_R(q)|\le|q|\) suffice.

The pointwise bound on the zero-initialized reference readout is needed in the top stability estimate. It gives
\[
\|\delta^{(3)}_a(A)-\delta^{(3)}_a(B)\|_2+
\|q^{(2)}_a(A)-q^{(2)}_a(B)\|_2
\le C\,d(A,B),
\]
even when only B's readout is pointwise bounded.

Picard iteration is performed on a closed set of continuous paths with \(|W^{(4)}(s)|\le as\), not on an unrestricted open \(L^2\) ball. The integral readout equation preserves this constraint, and the remaining enlarged norm bounds are preserved on a sufficiently short interval. This is enough for contraction and continuation. General local Lipschitzness on arbitrary \(L^2\) neighborhoods is neither true by this argument nor needed.

The fixed-cap Euler defect and error are therefore uniformly \(O(\Delta^2)\) and \(O(\Delta)\) on the initial operator event. Fixed finite-program convergence is used with the mesh fixed, followed by mesh refinement. There is no appeal to a Gaussian theorem with a number of queries growing with width.

### 5.2 The cap factor is linear, including at the second cut

Let
\[
u_a=\phi'(Z^{(2)}_a)\tau_R(q^{(2)}_a),\qquad
p_a=(W^{(2)})^*u_a.
\]
For the larger-cap state A and smaller-cap state B, the exact scalar split at either gate is
\[
\begin{aligned}
g_A\tau_{R'}(q_A)-g_B\tau_R(q_B)
={}&g_A[\tau_{R'}(q_A)-\tau_{R'}(q_B)]\\
&+(g_A-g_B)\tau_R(q_B)
+g_A[\tau_{R'}(q_B)-\tau_R(q_B)].
\end{aligned}
\]
The first term costs the query difference with coefficient at most \(1/10\), the second costs at most \(2R\) times a gate difference, and the last costs the reference tail only. The last bracket is zero on \(|q_B|\le R\) and is bounded by \(4b_R(q_B)\) elsewhere.

Consequently,
\[
\sum_a\|u_a(A)-u_a(B)\|_2
\le C(1+R)d(A,B)+C\sum_a\|b_R(q^{(2)}_a(B))\|_2.
\]
Reverse multiplication gives
\[
\sum_a\|p_a(A)-p_a(B)\|_2
\le C(1+R)d(A,B)+C\sum_a\|b_R(q^{(2)}_a(B))\|_2.
\]
At the bottom, applying the same split multiplies this entire query-difference bound by the bounded bottom gate. It does **not** multiply it by \(R\). The bottom gate-difference term separately costs \(R\,d(A,B)\). Hence
\[
\|V_{R'}(A)-V_R(B)\|
\le C(1+R)d(A,B)+Ce_R(B).
\]
The constants are independent of \(R'\), including \(R'=\infty\), and no tail condition is imposed on A. The individual sample-gradient blocks satisfy the same type of estimate; the estimate is not dependent on cancellation in their label-weighted sum.

### 5.3 Tail removal, actual velocities, and restart

The extra imported scalar calculation is valid: on \(|q|>u\),
\[
q^2=e^{q^2/K^2}
\bigl(q^2e^{-q^2/(2K^2)}\bigr)e^{-q^2/(2K^2)}
\le e^{q^2/K^2}(2K^2/e)e^{-u^2/(2K^2)}.
\]
Taking expectations gives the stated, slightly looser \(4K^2\) bound. With \(K=4\) and four queries,
\[
e_R(\theta_R(s))\le32e^{-R^2/256}=:\varepsilon_R.
\]

The state discrepancy is bounded by \(C e^{C(1+R)S}\varepsilon_R\). This tends to zero and makes the cut paths uniformly Cauchy in the complete Banach space.

It is also enough to identify the **actual uncut** right-hand side. First \(q^{(2)}(\theta_R)\) converges strongly by top stability. Apply the middle split with A equal to the limiting state and cap \(R'=\infty\) to obtain convergence of the middle delta and \(q^{(1)}\). Apply the bottom split to identify the first raw velocity. The factor \(1+R\) still disappears against the Gaussian decay. The rank-one blocks converge uniformly as well, including in Hilbert–Schmidt norm.

Thus the integral equation passes with its true vector field and yields a \(C^1\) flow, not just a subsequential weak solution. A bounded-primal competitor has the same comparison, with a possibly different fixed constant \(C\). At restart the existing initial error adds another \(e^{CR}\), still absorbed by \(e^{-R^2/256}\). This establishes both initial-value and restart uniqueness in the stated class.

## 6. Symmetry, raw gradient, and the physical inverse clock

### 6.1 Symmetry is not circular

The finite sample-exchange isometry in E fixes the initialization law. The same-label constant-mode Euler and cut-flow fields commute with this transformation. Oddness of the cuts also gives the stated signed version.

Their fixed-program and fixed-cap limits are deterministic empirical laws. Thus equality in law of the finite predictions forces equality of the limiting prediction numbers, and gives sample-exchange symmetry of the limiting same-neuron tuples. Cut removal preserves these properties.

This does not require an already constructed uncut symmetry involution, does not infer pathwise finite residual equality, and does not invoke uncut uniqueness to establish its own premises. The derivative observations inherit exchange symmetry by the same finite-program and strong-product passage.

### 6.2 The scalar predictor is genuinely \(C^1\) in the raw Hilbert metric

For fixed \(B\in L^2\), the remainder estimate in A lines 195–196 follows by cutting \(|B|\) at a finite threshold. On the bounded part use the bounded second derivative of \(\phi\); on the remainder use the Lipschitz bound on \(\phi\) and its linearization. Dividing by \(\|v\|_2\), taking \(v\to0\), then removing the threshold gives a scalar \(o(\|v\|_2)\) remainder.

Expand a prediction from the top downward. Forward perturbations are \(O\) of the parameter perturbation. Terms containing both an operator/readout change and a propagated change are quadratic. The remaining activation remainders pair with fixed \(L^2\) backward factors and are controlled by the preceding scalar estimate. Adjunction gives exactly the raw gradients of E.

Gradient continuity follows by writing a changed gate times a backward factor as the sum of a strong-factor difference and a changed gate multiplying a fixed old factor; truncate the latter. Rank-one gradient blocks then converge in Hilbert–Schmidt norm. The first-block metric is the \(C^{-1}\) metric above, or the one-field metric at \(\rho=-1\).

This argument establishes \(C^1\) scalar predictions without asserting Fréchet differentiability of the nonlinear map \(\phi:L^2\to L^2\).

### 6.3 The clock covers every finite physical time

For labels \(+1,+1\), the uncut field is \(\nabla g\), where \(g=(f_1+f_2)/2\). Its readout gradient is
\[
V=\frac{H^{(3)}_1+H^{(3)}_2}{2}\ge m.
\]
Hence
\[
g'(s)=\|\nabla g\|^2\ge\|V\|_2^2\ge m^2,\qquad g(0)=0.
\]
Since \(m^2(3/2)>1\), the continuous strictly increasing function reaches 1 at a unique \(s_*\le36/25<3/2\). Continuity of the raw gradient on the compact constructed interval also bounds \(g'\) above by a finite \(B\).

For \(s<s_*\),
\[
1-g(s)=\int_s^{s_*}g'(u)\,du\le B(s_*-s).
\]
Therefore \(t(s)=\int_0^s[4(1-g(u))]^{-1}\,du\) diverges at \(s_*\). It has an inverse at every finite \(t\), with
\[
s'(t)=4(1-g(s(t)))>0.
\]
Using the already proved population symmetry,
\[
-\nabla L=2\sum_a(1-f_a)\nabla f_a
=4(1-g)\nabla g.
\]
Thus the time change gives the actual physical gradient flow. Negating the common label and readout gives the other same-label case.

Only a bounded \(C^1\) clock derivative is needed later: \(s''=-4g'(s)s'\) is continuous and bounded on a finite physical horizon. No unproved higher smoothness is necessary.

## 7. Nonsymmetric physical comparison, exact GD, and interpolation

### 7.1 Off-mode forcing is explicitly controlled

Write \(G_a\) for the residual-free raw gradient of \(f_a\), and \(G_{R,a}\) for its cut version. For a physical competitor A and the reference
\[
B(t)=\theta_R(s(t)),\qquad \lambda(t)=4(1-g(s(t))),
\]
the exact decomposition for common positive labels is
\[
\begin{aligned}
F_\infty(A)-B'
={}&2\sum_a(1-f_a(A))[G_a(A)-G_{R,a}(B)]\\
&+2\sum_a[g(s(t))-f_a(A)]G_{R,a}(B).
\end{aligned}
\]
Now split
\[
g-f_a(A)=(f_a(B)-f_a(A))+(g-f_a(B)).
\]
The first difference is Lipschitz in the state distance. The second is a reference prediction error, separately for each sample. It therefore controls the off-mode residual as well as the label-mode residual.

This yields precisely a \(C_T(1+R)d\) comparison term plus reference tails and reference prediction errors. It applies to a nonsymmetric population competitor, proving physical uniqueness and restart; the finite-width version applies to nonsymmetric actual GD/GF.

At finite width the reference is \(B_{n,R}(t)=\theta_{n,R}(s(t))\), using the population clock. There is no assertion that it is the actual finite physical flow. For fixed \(R\), fixed-cap laws and their time modulus give the prediction error (6) and the empirical tail estimate (7). The latter uses the continuous quadratic-growth function \(b_R^2\), not an unjustified empirical exponential-moment bound.

### 7.2 The limiting order and the stopping argument work

The actual readout initialization contributes
\[
\|W^{(4)}_0\|_n=O_{\mathbb P}(n^{-1}),
\]
while the initial first fields and hidden operators are coupled exactly. On a fixed primal stopping set, residuals and all raw gradient norms are uniformly bounded.

For GF, integration gives the comparison directly. For GD, the actual raw state update is exactly Euler with step \(\eta_n\). The reference has local defect \(C_{R,T}\eta_n^2\), using fixed-cap Lipschitzness and the clock regularity above. Thus A (8) has the correct form.

The order is: fix \(R,T\); take \(n\to\infty\); then send \(R\to\infty\). Constants that grow with \(R\) are harmless in the first limit. In the second, every surviving error is bounded by a polynomial or \(e^{cR}\) times \(e^{-R^2/256}\). No cap is being allowed to grow with width inside the finite-program theorem.

The comparison is valid through the first stopped node. That node's incoming raw update has norm at most \(C\eta_n\), because it was computed at the preceding good node. A margin larger than the reference bound then makes a first exit incompatible with the vanishing comparison error. The continuous argument handles GF.

For completeness, finite-dimensional GF exists at all finite times independently of this high-probability argument: \(L'=-\|\nabla L\|_{\rm raw}^2\), so its raw path length on a finite interval is at most \(\sqrt{T L(0)}\). For fixed \(n\), this bounds the parameters in a finite-dimensional norm and permits continuation of the smooth ODE.

### 7.3 Exact interpolation velocities

The actual raw interpolation must not be assigned the instantaneous gradient at an interior point. The following identities spell out the product-rule argument in A lines 285–292.

On a step \([t_k,t_{k+1}]\), put \(r_a^k=f_a(\theta_k)-y_a\), let all superscript-\(k\) deltas/features be evaluated at the node, and set
\[
D_b^k=-2\sum_a C_{ba}r_a^k\delta^{(1),k}_a.
\]
The exact recomputed preactivation velocities inside the linearly interpolated raw-parameter step are
\[
\dot Z^{(1)}_b(t)=D_b^k,
\]
\[
\dot Z^{(2)}_b(t)
=-2\sum_a r_a^k\delta^{(2),k}_a
  \langle H^{(1),k}_a,H^{(1)}_b(t)\rangle_n
+W^{(2)}(t)[\phi'(Z^{(1)}_b(t))D_b^k],
\]
\[
\dot Z^{(3)}_b(t)
=-2\sum_a r_a^k\delta^{(3),k}_a
  \langle H^{(2),k}_a,H^{(2)}_b(t)\rangle_n
+W^{(3)}(t)[\phi'(Z^{(2)}_b(t))\dot Z^{(2)}_b(t)].
\]
Also \(\dot H^{(\ell)}_b(t)=\phi'(Z^{(\ell)}_b(t))\dot Z^{(\ell)}_b(t)\). These are exact; in particular the inner products mix the fixed node feature and the current interpolated feature.

On the stopped bounds, raw vectors and forward fields move \(O(\eta_n)\) in normalized \(L^2\) norm during a step. Therefore their coordinate supremum change is at most \(O(\eta_n\sqrt n)\). A changed gate multiplying a bounded-\(L^2\) velocity is bounded using that supremum change. Applying the displayed formulas in layer order gives an \(O(\eta_n\sqrt n)=O(n^{-3/2})\) discrepancy from the corresponding node velocity formulas.

The same estimate controls neighboring node-gradient formulas: propagate the gate-supremum bound through the top delta, the middle reverse/gate, then the bottom reverse/gate. These contributions add; they do not produce successive factors of \(\sqrt n\). This justifies the right-node and terminal-left conventions as well.

## 8. Observation transfer

A lines 299–339 cover the stated observation classes, with the following distinctions preserved.

First, state-distance comparison and bounded operator norms transfer each fixed finite Lipschitz probe program, in either matrix direction. Same-neuron tuples can include both samples and any fixed finite collection of times.

Second, named uncut deltas and queries are controlled by the two explicit asymmetric splits. There is no inference that an unbounded backward product is Lipschitz merely because its gate is bounded.

Third, for a strongly convergent \(L^2\) factor and a bounded continuous gate converging in probability, the product converges strongly. In the same-width comparison, the corresponding quantitative truncation for a Lipschitz gate is
\[
\|(g(x_n)-g(y_n))v_n\|_n
\le \operatorname{Lip}(g)M\|x_n-y_n\|_n
+2\|g\|_\infty\|v_n\mathbf1_{\{|v_n|>M\}}\|_n.
\]
The reference finite-dimensional \(W_2\) laws control the second term after truncation. Uniformity in time follows from the compact \(L^2\) reference path and fixed-cap time moduli. Repeating this argument in forward layer order covers the hidden velocity formulas. This is also why bare state-norm bounds alone are not the observation proof.

Predictions and losses then follow by contraction. Kernel entries are products of same-population second moments, with the first-layer factor \(C_{ab}\) unchanged. They do not require a joint coordinate pairing between different neuron populations.

For path laws, a scalar absolutely continuous path has
\[
\|z-I_\pi z\|_\infty^2
\le4|\pi|\int_0^T|\dot z|^2.
\]
The hidden forward equations give a uniform bound on the expected/empirical integrated squared velocities from the already bounded raw velocities and operator norms. Apply the displayed inequality in empirical average and expectation. At a fixed mesh, joint time-sample \(W_2\) convergence gives convergence of the interpolated path laws; a triangle inequality and mesh removal then give \(W_2(C([0,T]))\) convergence. Summing the inequality for both coordinates proves the two-sample path assertion. The Lipschitz activation transfers it to feature paths.

This covers the preactivation and feature path claims actually made in A. It should not be enlarged without proof to path laws for every conceivable unbounded probe.

## 9. Every-time two-sample nonlinearity and nonfreezing

### 9.1 Forward pair separation is quantitatively preserved

N lines 24–44 dominate the bottom displacement by
\[
R_1=\frac{\epsilon\Delta}{2}\sum_{r<k,b}(|\zeta^{(1)}_{rb}|+a),
\qquad
\mathbb E R_1<1/5.
\]
This dominator depends only on a source group independent of the Gaussian root pair. Thus
\[
\mathbb P(Z^{(1)}_1\ge1,Z^{(1)}_2\le-1)
\ge(4/5)\mathbb P(G_1\ge2,G_2\le-2)>0.
\]
For \(\rho=-1\), the last probability is exactly \(\mathbb P(G_1\ge2)\), so the singular root causes no loss of strictness.

Together with exchange symmetry and \(H_a\ge m\), this gives positive lower bounds for both eigenvalues of the first feature second-moment matrix:
\[
\lambda_+=\tfrac12\mathbb E(H_1+H_2)^2\ge2m^2,\qquad
\lambda_-=\tfrac12\mathbb E(H_1-H_2)^2\ge d_1/2.
\]

At the middle layer, the displacement dominator depends only on \(\zeta^{(2)}\), independently of the forward source \(\xi^{(2)}\), and has expectation \(483/1600<1/3\). The source pair covariance has eigenvalues in \([c_1,2a^2]\). On the chosen bounded rectangle its Gaussian density is indeed bounded below by
\[
(4\pi a^2)^{-1}\exp(-\|x\|^2/(2c_1)).
\]
This gives the next strictly positive feature-difference bound and the next positive-definite feature Gram.

At the top the deterministic displacement bound is \(63/160<2/5\). A Gaussian rectangle therefore survives regardless of the dependence of this correction on the source. No independence assertion is needed there.

These event lower bounds pass through the mesh and cap limits using closed events: under weak convergence, the limiting probability of a closed set is at least the limsup of the approximating probabilities. The use and direction of that inequality in N are correct. Feature second moments also converge strongly.

### 9.2 Strict affine-regression error holds at every reached time

For every fixed positive tail level, the independent bottom/middle dominator events and the top bounded correction give both positive and negative unbounded tails for each marginal preactivation, uniformly over approximations and the constructed feature interval. Marginal forward Gaussian variances are bounded below by \(m^2\) in layers 2 and 3.

Each limiting \(Z\) is square-integrable and has positive variance. Its best affine error is
\[
\operatorname{Var}(\phi(Z))
-\frac{\operatorname{Cov}(Z,\phi(Z))^2}{\operatorname{Var}(Z)}.
\]
Zero error would make \(\phi(Z)\) affine in \(Z\) almost surely. Unbounded support and bounded \(\phi\) force zero slope, and strict monotonicity would then force \(Z\) to be constant. This contradicts the tails.

Continuity of the relevant moments along the \(L^2\) path, together with positive variance, makes the error continuous and positive. On a compact time interval it has a positive minimum. Uniform empirical second-moment convergence therefore gives the stated finite empirical lower bound. This establishes every-time nonlinearity, not just nonlinearity at initialization.

### 9.3 Backward second-moment matrices are strictly positive definite

At positive feature time, the same-label readout satisfies \(W^{(4)}(s)\ge ms\). The top gate-ratio argument in N lines 133–152 is valid. On one source rectangle,
\[
|\!Z^{(3)}_1|\ge18/5,\quad |\!Z^{(3)}_2|\le1/2,\quad
\delta^{(3)}_1/\delta^{(3)}_2<1/4,\quad
\delta^{(3)}_2\ge b_0>0.
\]
The swapped rectangle reverses the roles. For any unit vector of coefficients, choose the rectangle making its largest coefficient multiply the larger delta. The reverse triangle inequality then gives the uniform lower bound \(3b_0/(4\sqrt2)\) in absolute value. Thus the top-delta second-moment matrix has a strictly positive smallest eigenvalue on each \(s\ge s_0>0\).

At a fixed limiting positive time, its approximating middle reverse-source covariances consequently stay positive definite. Each source has positive probability in all four sufficiently far signed rectangles. Since the response shift is bounded by \(a\), each corresponding closed signed quadrant with \(|q_a|\ge1\) has positive limiting probability.

Multiplying by the strictly positive middle gates preserves the sign on those quadrants. For any proposed nonzero deterministic linear combination of the two middle deltas, choose a quadrant aligned with its coefficient signs. The combination is strictly positive there, so it cannot vanish almost surely. This proves positive definiteness of the middle-delta second-moment matrix.

Its second moment is exactly the next reverse-source covariance. The identical bounded-shift/quadrant argument proves positive definiteness for the bottom deltas. This step is specific to the two-query law and does not import one-input positivity.

### 9.4 Nonzero parameter motion cannot cancel all hidden velocities

Let \(D_\ell\) be the two-delta second-moment matrix at layer \(\ell\). At the first layer,
\[
K_g^{(1)}=\tfrac14\operatorname{tr}(CD_1)>0.
\]
Even at \(\rho=-1\), \(C\) is positive semidefinite with trace two, and \(D_1\) is positive definite. Thus \(\operatorname{tr}(CD_1)\ge2\lambda_{\min}(D_1)>0\).

At layers 2 and 3 the same trace-product argument applies to the positive-definite delta matrix and the positive-semidefinite feature Gram of positive trace. Every hidden parameter block of \(\nabla g\) therefore has positive squared norm.

The exact differentiated forward equations and adjunction give
\[
\frac12\sum_a\mathbb E[\delta^{(j)}_a(Z^{(j)}_a)']
=\sum_{\ell\le j}K_g^{(\ell)}>0.
\]
For layer 2 the propagated term is the layer-1 pairing; for layer 3 it is the layer-2 pairing. Thus this identity also checks possible cancellation between a trained-matrix term and a propagated lower-layer term.

At least one sample velocity must be nonzero at each layer. Exchange symmetry makes the two squared velocity norms equal, so both are nonzero. The strictly positive local gate preserves nonzero feature velocity, and the strictly positive finite-time physical clock preserves both conclusions after time change.

## 10. Initial nonlazy scale and kernel change

N Section 5 has an independent initial positivity argument; it does not infer a nonzero leading coefficient solely from positivity at later times.

The initial top backward pair is \(V_0\phi'(Z^{(3)}_{a,0})\), with \(V_0\ge m\). The initial forward pair is nondegenerate because the lower feature Gram is positive definite, including when the input root is singular. The two gate-ratio rectangles give a positive-definite top-backward second moment.

Condition the initial third matrix on its two forward queries. For a two-column input matrix \(H\) and reverse input pair \(U\), the residual reverse answer has the form
\[
H(H^TH)^{-1}Y^TU+P_{H^\perp}\widetilde W^TU.
\]
The removed projection has fixed rank and vanishing normalized mean-square effect. The residual scalar Gaussian pair has the full covariance \(\lim U^TU/n\), not that covariance minus the response contribution. The old middle fields are independent of this unexplored residual, so the limiting pair is a bounded deterministic linear combination of the two features plus an independent Gaussian pair with this covariance.

At the second matrix, condition also on the independent initial third matrix. The reverse input is then known from that matrix and the second matrix's already observed forward queries; it does not observe the second matrix's remaining residual. The middle reverse input can be truncated and then untruncated in \(L^2\), using its Gaussian-plus-bounded law and the initial operator bound. Conditional empirical averaging gives joint neuron laws throughout. This justifies N lines 230–243, including the unbounded middle reverse input.

Let \(D_0\) be the bounded linearized hidden-forward map to \(V\), and \(B=D_0^*V_0\). The covariance and trace-product arguments give
\[
\Gamma_\ell=\|B_\ell\|_{\rm raw}^2>0
\quad(\ell=1,2,3),\qquad \Gamma=\sum_\ell\Gamma_\ell>0.
\]

Along the actual constructed curve,
\[
W^{(4)}(s)/s\to V_0,\qquad
\alpha'(s)/s\to B,\qquad
\alpha(s)-\alpha(0)=s^2B/2+o(s^2).
\]
Here the adjoint products converge strongly on the displayed directions: start with \(W^{(4)}(s)/s\), then propagate through the bounded operators and bounded gates, truncating fixed \(L^2\) factors as necessary. The linearized forward maps are uniformly bounded and converge strongly on each fixed direction. Operator-norm differentiability of an \(L^2\) activation map is not used.

It follows that \(V'(s)=sD_0B+o(s)\), with
\[
\langle V_0,D_0B\rangle=\|B\|^2=\Gamma.
\]
Consequently the coefficients in N (5) are correct:
\[
K_g^{(4)}(s)=\|V_0\|^2+\Gamma s^2+o(s^2),\qquad
\sum_{\ell=1}^3K_g^{(\ell)}(s)=\Gamma s^2+o(s^2),
\]
\[
K_g(s)=\|V_0\|^2+2\Gamma s^2+o(s^2).
\]
Changing this fixed quadratic form proves that the total \(2\times2\) kernel is nonconstant. It does not require every individual matrix entry to have a nonzero change.

Dividing the hidden pairing identity by \(s^2\) gives a strictly positive leading pairing at every layer. Symmetry makes both sample leading velocity norms nonzero. The curve chain rule and integration give
\[
H^{(\ell)}_a(s)-H^{(\ell)}_a(0)
=\tfrac12s^2\phi'(Z^{(\ell)}_a(0))T^{(\ell)}_a+o(s^2),
\]
with a nonzero \(L^2\) coefficient for every sample/layer. Since \(s(t)=4t+o(t)\), the physical displacement coefficient is \(8\), the readout-mode kernel coefficient is \(16\Gamma\), and the total-mode coefficient is \(32\Gamma\), as stated.

The joint time-field and kernel convergence already proved transfers these strictly nonzero changes, for sufficiently small fixed positive times, to the finite systems. This is a nonlazy conclusion at fixed activation and fixed correlation, without a width-dependent motion coefficient.

## 11. Required corrections and qualifications

### Mathematical corrections

**None identified as necessary for the same-label modular theorem.** In particular, this review does not require a quadratic-cap estimate, a tail assumption on a competing flow, nonsingular root covariance, exact finite residual symmetry, or a new long-feature-time response estimate for the same-label case.

The supplied expansions of the Hilbert metric, physical off-mode comparison, exact raw interpolation velocities, and initial two-query conditioning make explicit why the cited arguments close; they do not add an unproved hypothesis or invoke a new external theorem.

### Presentation corrections

1. **A lines 261–263: replace “bounded smooth population clock” by the regularity actually proved and needed.** A precise replacement is: “the population clock has bounded derivative and bounded continuous second derivative on each finite physical horizon, since \(s'=4(1-g(s))\) and \(s''=-4g'(s)s'\).” The local reference defect follows from this. Infinite differentiability is not established by the \(C^1\) gradient argument and is unnecessary.

2. **A lines 8–19 and 343–347: identify N as the nontriviality component of the complete bundle.** The existing dependency list describes the construction portion, while the remaining-scope paragraph still says that a separate two-sample nontriviality proof is required. That proof is now the hashed N document, and this review has audited it in full. A combined theorem should cite N explicitly or incorporate it, while continuing to state that opposite-label continuation is open.

For a later single theorem document, it would also improve reviewability to include the raw affine Hilbert-space definition and exact interpolation identities displayed above, and to state its observations and quantifiers together. Their present distribution across the allowed modules is not a mathematical failure of this modular assembly.

### Qualifications that must be preserved

- “Every-time nonfreezing” means every positive finite physical time, with both samples and every hidden layer. The population hidden velocity is zero at time zero.
- Gaussian-plus-bounded source representations are justified for the identified cut Euler laws; the limiting conclusions use strong limits and closed-event bounds. They do not assert that trained neuron coordinates become independent Gaussians.
- Construction uses a complete bounded-operator state space and subsequently proves Hilbert–Schmidt increments. One cannot simply substitute operator-norm completeness of an affine Hilbert–Schmidt space.
- Fixed-cap local Lipschitzness is used with the attained pointwise reference-readout constraint. The proof does not establish unrestricted local Lipschitzness of the uncut field on arbitrary \(L^2\) neighborhoods.
- Width is sent to infinity at fixed cap; cap removal comes afterward. The finite physical clock remains the population reference clock, and the actual finite off-mode residual is controlled by forcing.
- Strict positive constants can depend on the fixed correlation, and convergence is on each fixed finite physical horizon.
- A PASS here does not settle any missing opposite-label global argument and does not certify the full original user target.

