# Adaptive neural atoms: proved approximation, autonomous reservoir, storage obstruction

This scoped theoretical report uses only the supervisor's canonical model and the required research/math skills. It does not use other studies, external retrieval, experiments, or changes to the scientific book. The target is approximation of the supplied response-memory fields, with sample-count and high-input-dimension efficiency, while retaining the same initialized matrices in forward and transposed operations. Claims about finite moment order are separate from convergence as the moment order increases.

**Conclusion.** Neural source atoms admit a genuine dimension-independent Hilbert approximation estimate, and gradient-flow dissipation supplies their integrated norm bound along the actual training path. A fixed-size online reservoir makes source selection autonomous, with a conditional martingale approximation theorem. However, a deep source atom generally requires a complete frozen network parameter snapshot. The resulting storage is proportional to the number of atoms times the dense network parameter count. This does not establish compressed deep population dynamics. The first-layer forward-memory special case does have cheap ridge atoms; the deep response fields are the unresolved bridge.

## 1. Contract and normalization

Fix finite depth L, width n, moment order q, time horizon T, and a data law μ on (x,y). An empirical law with N samples is allowed. Expectations below mean integration against μ. Write ξ=x/√d and |v|_n=||v||_2/√n for vectors with n components. Let ||v||_{2,n}=(E|v(x,y)|_n²)^(1/2). The approximation metric for collections of fields is the direct-sum Hilbert norm built from these norms. For a finite autonomous approximation, static access to μ or its dataset is an input operation, not a compressed representation of arbitrary labels. Every data pass and any dataset storage must be counted separately from the evolving memory state.

For the training-source bounds assume φ is continuously differentiable with |φ′|≤K, finite initial loss ρ₀²=E r₀², finite input RMS R=(E||ξ||²)^(1/2), and differentiability sufficient for the displayed gradient flow and energy identity. Finite empirical datasets and smooth activations satisfy the integrability part. Define C₁=||W₁⁰ξ||_{2,n}. No target Barron norm, low-rank condition, or coordinate cutoff is assumed. Local Lipschitz claims for the autonomous reservoir require stronger hypotheses specified below, such as bounded inputs/labels and locally Lipschitz φ′.

Atoms must be evaluable finite circuits with explicitly stored real parameters at ordinary numerical precision. A reference to a deleted past memory configuration is not an atom description. The initialized matrices are shared static data and reused exactly, including their transposes. Replacing them by independent draws changes the problem.

## 2. A training-derived source norm bound

Let E(t)=E r_t². The supplied gradient-flow scalings give

\[
\dot E=-\frac{\|\dot W_1\|_F^2}{n}
       -\sum_{\ell=2}^L\|\dot W_\ell\|_F^2
       -\frac{\|\dot w\|_2^2}{n}.
\]

Indeed, differentiating f gives gradients 2E[rδ₁ξᵀ]/n for W₁, 2E[rδℓhℓ₋₁ᵀ]/n for Wℓ, and 2E[rhL]/n for w. The specified flow is negative n times the first/readout gradients and negative the interior gradients. Taking their inner products with their velocities proves the identity.

Consequently ρ(t)≤ρ₀, τ(t)≤1+ρ₀T, and Cauchy–Schwarz in time gives, for 0≤t≤T,

\[
\frac{\|W_1(t)-W_1^0\|_F}{\sqrt n},\quad
\|W_\ell(t)-W_\ell^0\|_F\ (\ell\ge2),\quad
|w(t)-w^0|_n\ \le\rho_0\sqrt T.
\]

Set a=ρ₀√T, Aℓ=||Wℓ⁰||op+a for ℓ≥2, and V=|w⁰|n+a. Define

\[
H_1=|\phi(0)|+K(C_1+aR),\qquad
H_\ell=|\phi(0)|+KA_\ell H_{\ell-1},
\]

\[
D_\ell=VK^{L-\ell+1}\prod_{j=\ell+1}^LA_j.
\]

Then ||hℓ(t)||₂,n≤Hℓ and, pointwise in the data, |δℓ(t,x)|n≤Dℓ. The forward bound uses |φ(z)|n≤|φ(0)|+K|z|n, the operator bounds, and ||(W₁−W₁⁰)ξ||₂,n≤aR. The backward bound starts with |w⊙φ′(zL)|n≤KV and applies ||Wjᵀ||op=||Wj||op at each layer. Therefore

\[
\|\rho h_\ell\|_{2,n}\le\rho H_\ell,
\qquad
\|r\delta_\ell\|_{2,n}\le\rho D_\ell.
\]

For the combined normalized source

\[
g_t=(h_1,\ldots,h_L,(r/\rho)\delta_1,\ldots,(r/\rho)\delta_L),
\]

with its response coordinates defined as zero when ρ=0, we obtain ||g_t||≤C, where C²=Σℓ(Hℓ²+Dℓ²). Its clock-weighted total source variation is at most C(τ(T)−1)≤Cρ₀T. This bound is obtained along the actual training path, not assumed of an arbitrary target function.

The constants contain initialization norms, depth, input RMS and initial loss; they do not explicitly contain N or d. This statement is conditional on those quantities remaining controlled across the proposed problem family. For independent variance-one Gaussian first-layer entries, E_initialization C₁²=E||ξ||²=R², directly by expanding the quadratic form. No uniform bound for every Gaussian realization is asserted. Interior initial operator norms and the readout norm remain explicit parameters.

This energy calculation applies to the canonical gradient flow. It does not automatically prove the same bounds for a finite-q reconstructed flow or its stochastic approximation.

## 3. Finite neural-atom approximation: what it proves

The elementary Hilbert sampling lemma is sufficient. Suppose F=∫a(θ)ψθ dν(θ) in a Hilbert space, ||ψθ||≤1, and ∫|a|dν=A<∞. For A>0 sample θ₁,…,θM from |a|dν/A and set FM=(A/M)Σm sign(a(θm))ψθm. Independence and zero mean of the centered summands give

\[
\mathbb E\|F_M-F\|^2
=\frac{A^2}{M}\left(\mathbb E\|\operatorname{sign}(a)\psi\|^2-\|F/A\|^2\right)
\le\frac{A^2}{M}.
\]

Thus at least one M-atom approximation has error ≤A/√M. The A=0 case is F=0. This is an approximation result, not a method for locating good atoms without evaluating the relevant sources.

Let the q×q moment matrix A have A_kk=k, A_kj=2j+1 for j<k, and zero entries for j>k, indexing from zero. To avoid confusing it with the scalar variation above, use only the matrix meaning of A below. Define

\[
U(t,s)=\exp[-A\log(\tau(t)/\tau(s))].
\]

For each layer the exact moment equations have the variation-of-constants form

\[
H(t)=U(t,0)e_0h_0+\int_0^t\rho(s)U(t,s)\mathbf1h_s\,ds,
\]

\[
B(t)=U(t,0)B(0)+\int_0^t\rho(s)U(t,s)\mathbf1[(r_s/\rho_s)\delta_s]\,ds.
\]

Take B(0)=0 for the ordinary untrained memory. For fixed q,

\[
C_q=\sup_{0\le v\le1}\|v^A\mathbf1\|_2<\infty.
\]

To see finiteness without an analytic semigroup assumption, A is a finite triangular matrix with distinct diagonal entries 0,…,q−1, hence is diagonalizable; v^A is conjugate to diag(1,v,…,v^{q−1}) and extends continuously to v=0.

Apply the Hilbert lemma to the combined source integral at a fixed t. Its variation is at most Cq C(τ(t)−1), so M full source-circuit atoms give squared expected error at most Cq²C²(τ(t)−1)²/M in all q forward/response moments together, with the initial term retained exactly. This is independent of sample count and input dimension through explicit constants. It makes no rank assertion about a weight matrix. Each atom is vector-valued, and E[g_i(x)g_j(x)ᵀ] may have full rank even for one pair of atoms.

The selected source circuits in this existence argument are from the true training path. Merely writing this representation does not make an autonomous algorithm and does not give a uniform-in-time guarantee. Section 5 gives a separate conditional autonomous construction.

## 4. Cheap first-layer atoms: a sharper special case

For the supplied moment recurrence, the components of U(t,s)1 equal Pk(2τ(s)/τ(t)−1), where Pk is the kth Legendre polynomial. One may verify the identity by differentiating this expression in τ(t), using

\[
2v\frac{d}{dv}P_k(2v-1)
=2kP_k(2v-1)+2\sum_{j<k}(2j+1)P_j(2v-1),
\]

and checking its value 1 at τ(t)=τ(s). Equivalently the identity after division by two is v(d/dv)Pk(2v−1)=kPk(2v−1)+Σj<k(2j+1)Pj(2v−1). The familiar polynomial identity can also be verified from the coefficients of the Legendre polynomials. For −1≤z≤1, |Pk(z)|≤1; one direct proof uses the integral representation Pk(z)=π⁻¹∫₀^π(z+i√(1−z²)cosθ)^k dθ, whose integrand has modulus at most one.

The initial conditions H₀(0)=h₀, Hk(0)=0 for k>0 are equivalent to adding a virtual constant prefix h(u)=h₀ on 0≤u≤1, because ∫₀¹Pk(2u−1)du is one for k=0 and zero otherwise. If h(u)=h_{s(u)} for 1<u≤τ(t), where s(u) is a generalized inverse of the residual clock, then

\[
\frac{H_{1,k,i}(t,x)}{\tau(t)}
=\frac1{\tau(t)}\int_0^{\tau(t)}
P_k(2u/\tau(t)-1)\,
\phi(a_i(u)\cdot x/\sqrt d)\,du.
\]

Here ai(u) is the ith first-layer weight row at the corresponding time, or its initial row on the prefix. For |φ|≤1, including tanh, this is a signed mixture of ridge atoms with total coefficient variation at most one. M shared samples of u approximate each moment with L²(μ) mean-square error ≤1/M; the sum over q moments is ≤q/M. Each atom needs its d-component direction plus its scalar clock coordinate. All moment coefficients are determined by that coordinate and the current clock; they need not be stored independently. Per neuron, full storage is O(Md+M+q), and shared sampling can use the same times for all neurons while storing nMd row entries.

This result avoids a coordinate polynomial/Fourier expansion and has no target regularity assumption. The d entries of an arbitrary ridge direction still have to be stored. It does not approximate B₁ with equally cheap atoms: the source rδ₁ contains the full deep forward and transposed backward computation. A deeper hℓ atom also depends on the preceding layers, so substituting a cheap ridge description is not justified.

## 5. An autonomous fixed-size reservoir

This construction addresses hidden teacher forcing and unbounded accumulation of snapshots. It does not remove the cost of each snapshot.

Fix a self-consistent finite-q closure Fq whose sources are the supplied h and rδ and whose matrices are reconstructed by the supplied formula. Any required first-layer/readout parameter equations must also be included in its state. For example, one completely specified choice keeps current W₁ and w as finite auxiliary states evolved by their supplied gradient equations, reconstructs the interior Wℓ from the q moments, and computes all source circuits from that same current network. The result remains a finite-q approximation of the canonical network; the reservoir theorem compares it to this specified closure, not directly to exact gradient flow.

Keep M slots, initially null. Slot j contains a birth clock uj and a frozen source circuit gj. At rate ρ/τ, independently for each slot conditionally on the current state, replace its contents by uj=τ and the current surrogate source g. When ρ=0 there is no reset and no division is needed. Between resets all gj and uj are frozen. Define the sampled source contribution

\[
Y(t)=\frac{\tau(t)}M\sum_{j=1}^M
\left(\frac{u_j}{\tau(t)}\right)^A\mathbf1\otimes g_j.
\]

Null slots contribute zero regardless of their nominal birth clock. Add the exact initial term U(t,0)e₀h₀ to the H coordinates and any prescribed initial term to B. At t=0 all sampled contributions vanish, so the prescribed initial moments are exact.

Write γ=ρ/τ. Between resets,

\[
\dot Y=\gamma(I-A)Y.
\]

A reset of slot j has increment

\[
\Delta_jY=\frac\tau M
\left(\mathbf1\otimes g- (u_j/\tau)^A\mathbf1\otimes g_j\right).
\]

Summing its conditional mean over all rates gives

\[
\sum_j\frac\rho\tau\Delta_jY
=\rho\mathbf1\otimes g-\gamma Y.
\]

Consequently the full state satisfies the intended closed moment drift exactly, plus a compensated jump martingale:

\[
dS_M=F_q(S_M)dt+d\mathcal M.
\]

The martingale occurs only in the memory coordinates. In particular, the current source is evaluated at SM, not along a hidden exact trajectory. The process restarts from its current clock, auxiliary variables, frozen slot descriptions and fresh randomness. Its expected number of replacements up to a deterministic bound τ* is at most M log τ*, because Σj∫ρ/τ dt=M log τ. There is no increasing bank of retained old snapshots.

For deterministic externally prescribed source paths this is ordinary continuous reservoir sampling: survival of a source born at clock u until clock τ has probability u/τ; each slot has mass 1/τ at null and birth-clock density 1/τ on [1,τ]. In the adaptive scheme these marginal independence claims need not hold. The conditional drift and martingale identities above remain valid and are the appropriate argument.

### Conditional quantitative theorem

Suppose, up to a common stopping time or on an invariant admissible domain, that:

1. the complete finite-q drift Fq is Kq-Lipschitz in a state norm that dominates the memory Hilbert norm;
2. the current and every retained source satisfy ||g||≤C;
3. 1≤τ≤τ*; and
4. evaluation of μ-expectations is exact for this theorem.

The deterministic closure S and the reservoir start at the same state. Since Cq≥||1||₂, every jump is bounded by 2τCqC/M. Thus the predictable quadratic variation in the memory Hilbert norm satisfies

\[
\mathbb E\|\mathcal M(T)\|^2
\le\mathbb E\int_0^T\frac{M\rho}\tau
\frac{4\tau^2C_q^2C^2}{M^2}\,dt
\le\frac{2C_q^2C^2(\tau_*^2-1)}M.
\]

The Hilbert-valued square-integrable martingale maximal inequality gives E sup_t||M(t)||²≤4E||M(T)||². This is the usual L² maximal inequality applied to the nonnegative submartingale ||M(t)||; its assumptions hold because jump sizes and total integrated rates are bounded as above. Subtracting the integral equations and applying scalar Gronwall to the running supremum yields

\[
\left(\mathbb E\sup_{t\le T}\|S_M(t)-S(t)\|^2\right)^{1/2}
\le\frac{\sqrt8\,e^{K_qT}C_qC\sqrt{\tau_*^2-1}}{\sqrt M}.
\]

For a stopped theorem, both states are stopped at the same admissibility time; a separate exit-probability argument is needed to remove that stopping. The source bound derived in Section 2 applies to exact training and does not by itself supply an invariant domain for either approximate process. Local Lipschitz continuity is plausible under finite n, bounded data and smooth φ, but width-independent constants are not established here. In particular, changes in φ′ multiply backward responses; a normalized second-moment bound alone does not control all such products. This issue must not be hidden in Kq.

This result is at fixed q. It provides neither an estimate of the moment truncation error nor convergence to the original gradient flow as q increases.

## 6. Complete storage, work, and precision audit

Let P=nd+(L−1)n²+n denote the dense parameter count. Store the initial W⁰ matrices once. A frozen source circuit gj contains the parameter values needed to compute its forward activations, its residual, and its backward responses using those same matrices and transposes. One honest representation stores its dense parameter displacement from initialization, costing P numbers per slot, plus its birth clock and residual normalization. Common initialized matrices can be shared exactly.

The total retained parameter storage is therefore O(P+MP+M+q), in addition to any current auxiliary states and data access. During an expectation calculation, one may materialize current matrices and a working set of outputs; these costs are also not zero. Storing per-slot moment coefficients would add O(Mq), but is optional because the coefficients are functions of uj and τ. Storage is independent of empirical sample count in the evolving state and linear in input dimension, but is multiplied by M and remains quadratic in width through each deep snapshot.

A pointer from an old atom to today's memory slots does not freeze yesterday's function. Freezing the entire dependency graph instead can accumulate recursively many ancestors. Materializing the old dense parameters avoids this hidden history, at the stated MP cost. The present theorem proves no cheaper representation of these old parameters.

Likewise, finitely many vector-valued source circuits do not imply a low-rank learned matrix. The reconstructed term E[Bℓ(x)Hℓ₋₁(x)ᵀ] can remain full rank. An n×M coefficient factorization over shared scalar atoms would imply a useful rank bound, but proving that factorization with controlled complexity is an additional problem, not a consequence of source-circuit sampling.

Arbitrary μ-expectations may require complete dataset passes. Finite retained state does not imply sample-count-independent arithmetic. Minibatch expectation errors add a separate stochastic approximation term and require their own variance and stability analysis. Accessing an arbitrary target y is also not a compact encoding of its values: in an empirical problem those labels still belong to the input dataset.

The factor 1/ρ at a reset can be large in numerical representation even though ||(r/ρ)δ|| is bounded. A practical regularization replaces it by 1/max(ρ,η); its response drift error is at most ηD in Hilbert norm per layer, since the changed drift is [ρ/max(ρ,η)]rδ and ||rδ||≤ρD. This incurs a separately propagated O(ηT) source error. No claim of arbitrary-information compression into one real scalar is intended.

## 7. Claim ledger and decisive bottleneck

| Claim | Status | Boundary |
|---|---|---|
| Training dissipation and explicit source bounds | Proved under the stated regularity/integrability assumptions | Exact canonical gradient flow only |
| M-atom Hilbert approximation with error O(M^−1/2) | Proved | Complete source circuits; fixed-time existence |
| First-layer Hk/τ is a bounded-variation ridge mixture | Proved for bounded activation | O(Md) description per neuron; does not cover deep response sources |
| Fixed-size reservoir has the correct finite-q drift plus martingale | Proved | Uses current surrogate sources and explicit frozen descriptions |
| Uniform finite-horizon reservoir approximation | Conditional theorem proved | Requires admissible source bounds, Lipschitz drift, and exact expectations |
| Deep atoms have cheap descriptions | Open | Dense snapshots currently cost P each |
| Small M implies low-rank weight updates | Unsupported | Vector atoms need not yield low-rank cross moments |
| Reservoir converges to full original gradient flow | Open | Requires q-error, admissibility, expectation and stability bridges |

The highest-leverage next obligation is a description theorem for deep response sources: derive, from actual training and exact reuse of W⁰, a scalar or compositional dictionary with controlled parameter count and a source approximation norm that also controls the reconstruction contractions. A theorem only bounding the total mass of a dictionary whose atoms each contain a full past network is insufficient for learned-state compression. The first-layer ridge result supplies a valid special case and a concrete benchmark for what the deeper theorem must improve upon.
