# Independent adversarial audit of ACTUAL_CLOCK_RANK_ONE_RESPONSE.md

Verdict: REQUIRED CORRECTION — one local covariance-spectrum statement.

The finite-width spectral theorem, namely candidate equations (1)–(5), passes. The rectangular feature-response estimate in ACTUAL_SQUARED_LOG_RESPONSE.md also passes an independent mathematical verification. The primal bounds and constants used from READOUT_COERCIVITY.md are valid. There is no required change to those estimates, their constants, their quantifiers, or either dependency.

For an unqualified PASS of the complete candidate, correct candidate lines 161–162: the squared response singular values are the **nonzero** eigenvalues of the conditional Gaussian covariance. That ambient covariance also has exactly N-n zero eigenvalues. This is a local precision correction, not a failure of the spectral theorem. A precise replacement appears below.

## Scope and immutable input identification

I read the complete candidate and both permitted dependencies. I independently checked the dependency's calculations rather than accepting a review status. I inspected no parent history, ledgers, previous reviews, numerical experiments, or other mathematical files, including files merely mentioned in the dependencies. The only instruction file read was `/etc/codex/skills/solve-math-rigorously/SKILL.md`, as permitted. No numerical experiments or external sources were used. No candidate or dependency was modified.

The following SHA-256 hashes identify the complete versions audited in this report. After the user's dependency-update notice, I reread the complete current ACTUAL_SQUARED_LOG_RESPONSE.md and independently rechecked its claims. Its computed hash matches the supplied d416464b... hash. The candidate and primal dependency remain unchanged. The current three hashes were checked again before updating this report and agreed with the post-update readings.

| Role | Exact path | SHA-256 |
| --- | --- | --- |
| Candidate | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_CLOCK_RANK_ONE_RESPONSE.md` | `a94c91daa6e3803daec1498a4710e26dfff829c52b4a817e5ab59795575d3c80` |
| Feature-response dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_SQUARED_LOG_RESPONSE.md` | `d416464bf1b5e4a792bb6937f0f7eec0e5d19cd70ca05816d02f011bf64547f0` |
| Primal dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/READOUT_COERCIVITY.md` | `0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53` |

All line references below refer to these exact versions.

## 1. Exact parameter scaling: PASS

Write c=W^(4), and use the candidate's Euclidean coordinates

\[
\theta=(z^{(1)},\sqrt n W^{(2)},\sqrt n W^{(3)},c),
\qquad N=2n^2+2n.
\]

Differentiating \(nf_n=c^Th^{(3)}\) in these coordinates gives exactly

\[
b=\nabla_\theta(nf_n)
=\left(\delta^{(1)},
\frac{\delta^{(2)}(h^{(1)})^T}{\sqrt n},
\frac{\delta^{(3)}(h^{(2)})^T}{\sqrt n},h^{(3)}\right).
\]

Consequently \(\theta'=b\) is precisely READOUT_COERCIVITY.md equation (1): dividing the second and third coordinate velocities by \(\sqrt n\) produces the original matrix updates with coefficient \(1/n\). Both matrices are trained.

The parameter metric in READOUT_COERCIVITY.md is \(\|d\theta\|_2^2/n\). Gradient descent of \((f_n-1)^2\) in that metric therefore has raw-coordinate velocity \(2(1-f_n)b\), not a velocity missing a factor of n. In particular,

\[
\nabla_\theta f_n=b/n,\qquad
\kappa_n=\frac{\|b\|_2^2}{n}=\frac{df_n}{ds},
\qquad
D[2(1-f_n)b]=2(1-f_n)Db-\frac2n bb^T.
\]

These identities agree across all three documents. The analysis uses the raw first preactivation, without a nonlinear change of first-layer coordinates.

## 2. Independent verification of ACTUAL_SQUARED_LOG_RESPONSE.md: PASS

### 2.1 Full Hessian identity and its explicit Frobenius constant

The activation satisfies \(|\phi|\le a=\pi/2\), \(|\phi'|\le1\), and \(|\phi''|\le2\). Under the stated operator and normalized readout bounds, the first preactivation variation maps in dependency lines 105–123 obey

\[
\|T_1\|_{\rm op}=1,\qquad
\|T_2\|_{\rm op}\le a+M=K_2,\qquad
\|T_3\|_{\rm op}\le a+MK_2=K_3.
\]

For example, \(\|E_2h^{(1)}/\sqrt n\|_2\le a\|E_2\|_{\rm F}\); the other summand of \(T_2\) has norm at most \(M\|u_1\|_2\). The same argument gives the bound on \(T_3\). Thus these are operator bounds on maps from the full hidden parameter space; there is no unaccounted factor from its dimension \(n+2n^2\).

Let \(A=D_x^2[c^Th^{(3)}]\). Direct second differentiation along a straight hidden-parameter line gives

\[
\begin{aligned}
A={}&T_1^T\operatorname{diag}(\phi''(z^{(1)})\odot q^{(1)})T_1\\
&+T_2^T\operatorname{diag}(\phi''(z^{(2)})\odot q^{(2)})T_2\\
&+T_3^T\operatorname{diag}(\phi''(z^{(3)})\odot c)T_3\\
&+S_2^TD_1T_1+T_1^TD_1S_2
 +S_3^TD_2T_2+T_2^TD_2S_3.
\end{aligned}
\]

Here \(D_\ell=\operatorname{diag}(\phi'(z^{(\ell)}))\), and \(S_2,S_3\) are exactly the maps in dependency lines 125–129. To check the cross terms explicitly, the second variations of the two matrix multiplications contain

\[
2E_2D_1u_1/\sqrt n,
\qquad 2E_3D_2T_2u/\sqrt n.
\]

Contracting these with \(\delta^{(2)}\) and \(\delta^{(3)}\) yields the two symmetrized pairs above. The remaining second variations propagate the activation curvatures with coefficients \(q^{(1)},q^{(2)},c\). Thus dependency equation (6) includes all trained-matrix cross terms and all three activation-curvature terms.

The estimates

\[
\|q^{(1)}\|_2\le M^2R\sqrt n,\quad
\|q^{(2)}\|_2\le MR\sqrt n,\quad
\|S_2\|_{\rm op}\le MR,\quad
\|S_3\|_{\rm op}\le R
\]

are valid. The Hessian contributions have the following Frobenius bounds:

| Contribution | Bound |
| --- | --- |
| First activation curvature | \(2M^2R\sqrt n\) |
| Second activation curvature | \(2MK_2^2R\sqrt n\) |
| Third activation curvature | \(2K_3^2R\sqrt n\) |
| Symmetrized \(S_2,T_1\) pair | \(2MR\sqrt n\) |
| Symmetrized \(S_3,T_2\) pair | \(2RK_2\sqrt n\) |
| Hidden/readout off-diagonal blocks | \(\sqrt{2n}K_3\) |

For the first three rows, use \(\|T^TDT\|_{\rm F}\le\|T\|_{\rm op}^2\|D\|_{\rm F}\). For the next two, each unsymmetrized product factors through \(\mathbb R^n\), hence has rank at most n and Frobenius norm at most \(\sqrt n\) times its operator norm. Symmetrization is bounded by the triangle inequality. Finally \(J=D_3T_3\) has rank at most n and norm at most \(K_3\), and

\[
Db=\begin{pmatrix}A&J^T\\J&0\end{pmatrix}.
\]

Summing gives exactly

\[
\|Db\|_{\rm F}\le
\left[2R(M^2+MK_2^2+K_3^2+M+K_2)+\sqrt2K_3\right]\sqrt n.
\]

The stated \(C_B(M,R)\) is therefore correct. No maximum-coordinate bound on the readout or backward fields was used.

### 2.2 Rectangular logarithmic energy, including repeated singular values

Let \(V'=DV\), where D is continuous on a finite interval, and \(V(s_0)^TV(s_0)=I_m\). A square fundamental solution is invertible: solving \(K'=-KD\) with the inverse initial condition gives \((KU)'=0\). Thus V has full column rank throughout the interval.

Set \(G=V^TV>0\), \(Q=VG^{-1/2}\), and

\[
\mathcal E=\frac14\operatorname{Tr}[(\log G)^2]
=\sum_{j=1}^m(\log\sigma_j(V))^2.
\]

The trace differentiation in dependency lines 208–222 is valid even at repeated eigenvalues. One independent justification uses

\[
D\log_G[H]=\int_0^\infty(G+rI)^{-1}H(G+rI)^{-1}\,dr.
\]

On a compact positive definite neighborhood this integral can be differentiated as needed because the integrand is bounded by a constant times \((\lambda_{\min}+r)^{-2}\). In an eigenbasis of G, its diagonal entries are \(H_{jj}/\lambda_j\), including within repeated-eigenvalue blocks. Differentiating the trace square and using cyclicity consequently gives

\[
\mathcal E'=\frac12\operatorname{Tr}[(\log G)G^{-1}G'].
\]

Writing \(D_{\rm sym}=(D+D^T)/2\), one has

\[
G'=2G^{1/2}Q^TD_{\rm sym}QG^{1/2},\qquad
\mathcal E'=\operatorname{Tr}[(\log G)Q^TD_{\rm sym}Q].
\]

There is no commutation assumption on D or its time values in this calculation. Since \(Q^TQ=I_m\), left and right multiplication by Q or \(Q^T\) are Frobenius contractions. Hence

\[
|\mathcal E'|\le2\sqrt{\mathcal E}\,\|D_{\rm sym}\|_{\rm F}.
\]

Integrating the inequality for \(\sqrt{\mathcal E+\varepsilon}\), starting with \(\mathcal E(s_0)=0\), and sending \(\varepsilon\downarrow0\) yields

\[
\sqrt{\mathcal E(s)}\le\int_{s_0}^s\|D_{\rm sym}(u)\|_{\rm F}\,du.
\]

For the actual feature derivative, \(D=Db\) is symmetric and satisfies the verified Hessian bound. Taking \(V=U(\cdot,s_0)E\) proves dependency equation (3) with exactly the displayed constant and normalization. This is a bound for every isometric embedding, not merely for square responses or a chosen fixed subspace.

### 2.3 Remaining claims in the dependency

I also checked the portions not needed to prove the candidate's uniform estimate. Evaluating the four blocks of b gives

\[
\|b\|_2^2/n\le M^4R^2+a^2M^2R^2+a^2R^2+a^2=K_b^2.
\]

Since \(\|bb^T\|_{\rm F}=\|b\|_2^2\) and \(|f_n|\le aR\), dependency equation (9) follows from

\[
\|B_{\rm phys}\|_{\rm F}
\le2(1+aR)C_B\sqrt n+2K_b^2
\le[2(1+aR)C_B+2K_b^2]\sqrt n.
\]

This uses only \(n\ge1\). The resulting finite-duration physical estimate retains the complete clock derivative.

For the trained-increment response \(Z=Y-E\), applying \(\|v-w\|^2\le2\|v\|^2+2\|w\|^2\) to every input yields \(Z^TZ\preceq2Y^TY+2I\). Ordered-eigenvalue monotonicity gives the first inequality of dependency equation (10). The scalar estimate

\[
\log(3+2u^2)\le\log5+2(\log u)_+
\]

and \((x+y)^2\le2x^2+2y^2\) give its constants \(2(\log5)^2\) and 8. The abstract diagonal-generator example is correct and is explicitly not asserted to be a canonical trajectory. The independent Gaussian derivative-probe interpretation in dependency lines 290–303 correctly says **nonzero** covariance eigenvalues.

There is no mathematical dependency here on the other named, uninspected notes: the Hessian and logarithmic arguments needed for this audit are actually supplied in the permitted file.

### 2.4 Current dependency's clarified metric and amplitude scope

The complete revised dependency consistently specifies the raw Euclidean coordinates used above. Its introduction and lines 338–341 make no claim that this spectrum is the spectrum in a transformed first-layer coordinate. This clarification is mathematically appropriate: for a smooth invertible coordinate map H, a transformed flow derivative is \(DH(\theta_t)D\Psi_t(\theta_0)DH(\theta_0)^{-1}\). Such left and right factors do not in general preserve singular values. Neither the dependency's proof nor the candidate requires a comparison with the uninspected transformed-coordinate note.

The revised amplitude disclaimer in lines 327–336 is also accurate in specifying the absence of a **width-uniform normalized** bound. A fixed-width bound does follow from the feature estimate: for a column response over feature duration \(\Delta s\),

\[
\sigma_{\max}(Y_i)\le e^{C_B\sqrt n\,\Delta s},\qquad
\frac1n\operatorname{Tr}(Z_i^TZ_i)
\le 2e^{2C_B\sqrt n\,\Delta s}+2.
\]

This is finite but deteriorates with n. The abstract example gives normalized response trace \((e^{2s\sqrt n}+n-1)/n\) and normalized increment trace \((e^{s\sqrt n}-1)^2/n\), both divergent at every fixed s>0, while satisfying the displayed logarithmic bounds. It demonstrates insufficiency of these inequalities for width-uniform control, not divergence for the actual canonical network. The revised wording distinguishes these statements correctly. The displayed identities, constants, and inequalities in the current complete dependency agree with the independently checked derivations in Sections 2.1–2.3; the inline-math repairs introduce no mathematical change.

## 3. Primal event and explicit constants from READOUT_COERCIVITY.md: PASS

The polynomial estimates in lines 49–76 prevent finite-feature-time escape for every finite initial state: the readout grows at most linearly, the top matrix at most quadratically, and the other matrix and first preactivation have successively polynomial increment bounds. Matrix increments are controlled in Frobenius norm as well as operator norm, which is sufficient for finite-dimensional continuation.

Direct differentiation of the forward equations gives

\[
c''=Hc,\qquad H=D_3A_3D_3\succeq0,
\qquad
\kappa=\|h^{(3)}\|_2^2/n+c^THc/n.
\]

For \(g=\|c\|_2/\sqrt n>0\), \(g'=f/g\) and

\[
g''=\frac{\|c'\|_2^2/n-(g')^2+c^THc/n}{g}\ge0.
\]

The first difference in the numerator is nonnegative by Cauchy–Schwarz. Thus the readout norm is convex wherever nonzero; this is not an unsupported coordinatewise positivity claim.

I checked the small-readout continuation constants, including the possible zero of the readout before the continuation time. In the notation of that dependency, \(\varepsilon\le b s_0/16\), \(Ba s_0^2\le b/8\), and its early-time estimates imply

\[
\sup_{0\le s\le s_0}
\frac{\|h^{(3)}(s)-h^{(3)}(0)\|_2}{\sqrt n}\le\frac{3b}{16},
\]

\[
\frac{\|c(s_0)-s_0h^{(3)}(0)\|_2}{s_0\sqrt n}\le\frac{7b}{48}.
\]

The second inequality implies \(c(s_0)\ne0\). Using the elementary directional inequality in dependency lines 246–252 gives

\[
g'(s_0)\ge b-2\frac{7b}{48}-\frac{3b}{16}=\frac{25b}{48}>\frac b2.
\]

Convexity propagates this positive slope and prevents a subsequent zero of g. Before \(s_0\), the first displayed estimate supplies the feature lower bound directly, without dividing by g. Consequently \(\|h^{(3)}\|_2/\sqrt n\ge b/2\) and \(\kappa\ge b^2/4\) on the entire feature half-line. The zero-readout proof is also valid: its initial right derivative of g is the nonzero initial feature norm and the same convexity prevents a later zero. The excluded zero-feature, zero-readout state is indeed stationary.

For completeness, the fixed constants in the candidate can be made entirely explicit using the dependency's definitions. Let the deterministic Gaussian moments \(m_1,m_2,m_3\) be as in READOUT_COERCIVITY.md lines 354–358, and set

\[
b_0=\sqrt{m_3}/2,\quad
L_3=10+a+a^2/2,\quad
L_2=10+aL_3(1+a/2),
\]

\[
B_0=a^2+L_3^2(a^2+L_2^2),\quad
\tau=\min\{1,\sqrt{b_0/(8aB_0)}\},\quad
\varepsilon_0=\min\{1,b_0\tau/16\}.
\]

All are deterministic and independent of n. The required event is

\[
\mathcal G_n=\left\{
\|W^{(2)}(0)\|_{\rm op},\|W^{(3)}(0)\|_{\rm op}\le10,
\quad\frac{\|h^{(3)}(0)\|_2}{\sqrt n}\ge b_0,
\quad\frac{\|c(0)\|_2}{\sqrt n}\le\varepsilon_0
\right\}.
\]

The initialization proof establishes \(\mathbb P(\mathcal G_n)\to1\). Indeed, conditional Gaussian rows and the boundedness of squared arctan give conditional empirical variances at most \(a^4/n\); continuity of the conditional means propagates the first-layer law of large numbers through both subsequent layers. Every limiting \(m_\ell\) is strictly positive. The two-net Gaussian calculation gives a failure bound \(2\,9^{2n}e^{-nM^2/8}\) per hidden matrix; at M=10 this tends to zero. Finally the normalized squared readout norm has expectation \(n^{-2}\), so its fixed-threshold failure probability tends to zero. No independence between these three events is needed to intersect them.

On this event \(|f_0|\le a\varepsilon_0<1\), \(e_0=1-f_0>0\), and

\[
k_0=b_0^2/4=m_3/16,\qquad
s_*\le4e_0/b_0^2.
\]

The exact action identity and Cauchy–Schwarz give total squared displacement in the dependency's parameter metric at most \(4e_0^2/b_0^2\) up to \(s_*\). Each matrix's Frobenius displacement and the normalized readout displacement are therefore at most \(2e_0/b_0\). Since \(e_0\le1+a\varepsilon_0\), the candidate's choices

\[
M=10+\frac{2(1+a\varepsilon_0)}{b_0},\quad
R=\varepsilon_0+\frac{2(1+a\varepsilon_0)}{b_0},\quad
S_*=\frac{4(1+a\varepsilon_0)}{b_0^2}
\]

are valid on the entire feature interval \([0,s_*]\). These bounds extend to its endpoint by continuity. The constants are conservative but there is no missing width dependence or residual factor.

The remaining primal claims do not introduce a gap: the remaining path-length bound follows from remaining action e(t) and remaining feature length at most e(t)/k_0. The lower-layer bounds use the already proved lower bound on the top feature norm, not an invalid inference from a lower kernel bound alone. The backward-energy estimate then follows from the \(\delta^{(2)}\) term in the exact action and the top-matrix operator bound. None of these statements supplies a population theorem.

## 4. Smooth state-dependent clock and exact rank-one identity: PASS

At any reached finite physical time, the residual is strictly positive. Along a finite physical solution,

\[
\frac{d}{dt}(1-f_n)=-2\kappa_n(1-f_n),
\]

and the coefficient is continuous on every finite interval. The exponential solution of this scalar equation preserves strict positivity at every finite time.

The initial-state differentiation is legitimate in an ordinary open neighborhood, not just on the probabilistic event. One can restrict that neighborhood to \(f_n(\theta)<1\). Along the feature flow \(df_n/ds=\|b\|^2/n\ge0\). Until a zero residual is approached, the scalar clock thus satisfies

\[
0\le s(t,\theta)\le2[1-f_n(\theta)]t.
\]

It cannot cross a zero of its smooth autonomous right side in finite time, by uniqueness. The feature polynomial bounds and this clock bound provide finite solutions on any prescribed finite physical interval for a sufficiently small initial-state neighborhood. Smooth dependence follows from the smooth finite-dimensional equations on that interval. No neighborhood uniform over infinite physical time is required.

Differentiating the composition at fixed physical duration gives exactly

\[
D_\theta\Psi_t(\theta_0)
=D_\theta\Phi_{s(t,\theta_0)}(\theta_0)
 +b(\Psi_t(\theta_0))D_\theta s(t,\theta_0).
\]

For an additional check on the clock derivative and all factors, set \(\alpha(t)=D_\theta s(t,\theta_0)\) and \(F_s=D_\theta\Phi_s(\theta_0)\). Differentiating the scalar clock gives

\[
\alpha'=-\frac2n b^TF_s-2\kappa_n\alpha,
\qquad \alpha(0)=0,
\]

where b and \(\kappa_n\) are evaluated at the reached state. Thus the candidate retains the whole generally nonzero clock derivative. Its outer-product correction has rank at most one, with no assertion of a small norm.

Finite-time feature and physical derivative matrices are invertible by their variational equations. Multiplication by an isometric embedding therefore preserves full column rank. This argument requires neither a globally defined backward flow nor differentiating an event indicator.

## 5. Rectangular singular interlacing and trimmed energy: PASS

For \(P-A=uv^T\), choose the span of right singular vectors k through m of A, of dimension \(m-k+1\). Its intersection with \(\ker v^T\) has dimension at least \(m-k\), and P agrees with A there. The min-max characterization on subspaces of that dimension gives

\[
\sigma_{k+1}(P)\le\sigma_k(A),\qquad 1\le k<m.
\]

Exchanging P and A proves the other interlacing inequality. The proof works for N-by-m matrices; squaring matrices and paying rank two is unnecessary.

For \(2\le j\le m-1\), the two interlacing inequalities imply

\[
\sigma_{j+1}(A)\le\sigma_j(P)\le\sigma_{j-1}(A).
\]

Full column rank makes all logarithms finite. Taking the increasing functions \((\log u)_+\) and, in the reversed inequality, \((-\log u)_+\), then squaring, gives

\[
\begin{aligned}
\sum_{j=2}^{m-1}(\log\sigma_j(P))^2
&\le\sum_{k=1}^{m-2}(\log\sigma_k(A))_+^2
 +\sum_{k=3}^{m}(-\log\sigma_k(A))_+^2\\
&\le\sum_{k=1}^m(\log\sigma_k(A))^2.
\end{aligned}
\]

The last inequality has no missing factor of two: at each shared index, the positive and negative parts sum to the square of that one logarithm. Repeated singular values cause no difficulty.

For m=1 or m=2 the stipulated trimmed sum is zero; the tail-count bound remains valid because at most two singular values exist. For m=3 there is exactly one retained index and the same inequalities apply. This covers n=1 and n=2 column probes, whose trimmed statements are vacuous but correct. The full-state response has m=N and is not vacuous at those widths. At zero duration all response singular values equal one.

## 6. Simultaneous physical times, reached starts, and embeddings: PASS

Fix a single initialization in \(\mathcal G_n\). The scalar clock increases from zero to \(s_*\), and its range at finite times is \([0,s_*)\). For any \(0\le t_0\le t<\infty\), the autonomous feature flow from \(\theta(t_0)\) to \(\theta(t)\) has duration

\[
\Delta s=s(t)-s(t_0)\in[0,s_*]\subset[0,S_*].
\]

Every state on that segment has the same verified M,R bounds. Applying the feature estimate to its derivative times E, followed by the rank-one trimmed inequality, gives

\[
\frac1n\sum_{j=2}^{m-1}
\left(\log\sigma_j(D\Psi_{t-t_0}(\theta(t_0))E)\right)^2
\le C_B(M,R)^2S_*^2.
\]

This is a deterministic implication for every segment and every isometric E on that one path. There is no need for a union bound over uncountably many times, starts, or embeddings, and no assumption that an embedding is independent of the trained path. The embedding is held fixed when evaluating each indicated directional derivative. A reached-start derivative is taken in all ambient directions at that state; it is not restricted to directions tangent to the set of reached states.

With \(C=C_B(M,R)^2S_*^2\), each retained index with \(|\log\sigma_j|\ge r\) contributes at least \(r^2\); adding at most two excluded indices gives candidate equation (5), with its stated constant. The supremum is over finite t only. Neither an invertible infinite-time derivative nor a differentiable endpoint map is used. The probability assertion is \(\mathbb P(\mathcal G_n)\to1\); it does not require a single event simultaneously over every width.

## 7. Required local correction: conditional Gaussian covariance spectrum

Candidate lines 158–162 correctly identify the isometric column embedding

\[
E_i u=(0,0,ue_i^T,0),\qquad E_i^TE_i=I_n.
\]

In original top-matrix entries, the corresponding infinitesimal variation is \(u e_i^T/\sqrt n\). For a standard Gaussian derivative probe g independent of the trained path, put

\[
Y=D\Psi_{t-t_0}(\theta(t_0))E_i.
\]

Conditional on that path, the full raw-coordinate linear response Yg is Gaussian with covariance \(YY^T\). Y is N-by-n and has rank n, so the complete spectrum is

\[
\operatorname{spec}(YY^T)
=\{\sigma_1(Y)^2,\ldots,\sigma_n(Y)^2\}
\cup\{0\text{ with multiplicity }N-n\}.
\]

The current candidate says its covariance eigenvalues are “exactly the squared response singular values,” omitting these zeros. This fails literally already at t=t_0: Y=E_i, its n singular values are all one, and its ambient covariance is a rank-n orthogonal projection with N-n zero eigenvalues. For n=1, that covariance spectrum is \(\{1,0,0,0\}\). This is an exact dimension check, not a numerical experiment.

Minimum required edit: insert **nonzero** before “eigenvalues” at candidate line 162. For maximum precision, replace the relevant sentences with:

> For an independent derivative probe \(g\sim N(0,I_n)\), let \(Y=D\Psi_{t-t_0}(\theta(t_0))E_i\). The corresponding full raw-coordinate linear response is Yg, associated with the infinitesimal top-column perturbation \(g/\sqrt n\). Conditional on the trained trajectory, its covariance is \(YY^T\); its n nonzero eigenvalues are exactly \(\sigma_j(Y)^2\), and its remaining N-n eigenvalues are zero.

The independent-derivative-probe interpretation is already supplied correctly by ACTUAL_SQUARED_LOG_RESPONSE.md lines 296–303, so this is not a missing mathematical hypothesis in that dependency. The assertion concerns the derivative on the actual trained trajectory. It does not claim that a finite nonlinear perturbation has an exactly Gaussian response, or that the already sampled, subsequently trained column is an independent Gaussian conditional on the trajectory.

If the result is expressed directly in terms of the n positive covariance eigenvalues \(\lambda_j=\sigma_j(Y)^2\), then \((\log\lambda_j)^2=4(\log\sigma_j(Y))^2\); the corresponding trimmed covariance-log constant is 4C. The candidate makes no conflicting numerical claim about that conversion. The result is in the stipulated raw-coordinate metric; an additional output projection or parameter rescaling would change the covariance matrix under discussion.

## 8. Scope of the established result

The conclusion is a canonical finite-width response-spectrum estimate in the raw metric, uniform over all finite physical times and all reached starts, after excluding at most the largest and smallest response singular values. The proof controls counts and a trimmed logarithmic energy. It provides no uniform amplitude estimate for the excluded directions and no width-uniform normalized response-trace bound. Even the feature estimate alone allows a singular value exponential in \(\sqrt n\). Projecting the response onto hidden parameters can also destroy the full-column-rank premise. The candidate explicitly acknowledges these limitations and does not claim population continuation, a global population theorem, or exact-GD identification. Its qualitative amplitude disclaimers are assessed in this uniform-estimate sense; they are not a denial that responses are finite at each fixed width and finite duration.

No additional correction is required in these respects. After the local covariance wording correction in Section 7, the complete candidate merits PASS for its stated finite-width spectral result, with both permitted dependencies independently verified as above.

## 9. Final verdict for the complete corrected current candidate: PASS

This section is appended after the user's covariance correction and preserves the preceding review as history. It supersedes the earlier REQUIRED CORRECTION verdict **for the new candidate hash below only**. The earlier verdict remains the assessment of the earlier a94c91da... version.

I reread the complete current ACTUAL_CLOCK_RANK_ONE_RESPONSE.md, lines 1–194, rather than checking only the edited paragraph. Its raw coordinate definitions, clock construction, derivative identity, rectangular interlacing, squared-log inequality, constants, all-time and reached-start quantifiers, and finite-width scope remain correct. Equations (1)–(5) are unchanged. The independently verified current squared-log and primal dependencies retain their hashes below.

| Role | Exact path | Current SHA-256 |
| --- | --- | --- |
| Corrected clock candidate | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_CLOCK_RANK_ONE_RESPONSE.md` | `a3e093852f07d58b474197fd4781dfb69830203a21eda7e788d45af27f28f0bd` |
| Current squared-log dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/ACTUAL_SQUARED_LOG_RESPONSE.md` | `d416464bf1b5e4a792bb6937f0f7eec0e5d19cd70ca05816d02f011bf64547f0` |
| Primal dependency | `/tmp/l3-supervisor-recovery-59x8oL/l3-full-resolution-9nbD4z/READOUT_COERCIVITY.md` | `0bd062da74fbde03d41a125561beee7345915ea6aa0578ed8e7b81d2c9f08c53` |

These current hashes were computed at the complete reread and checked again before appending this verdict; the values agreed. No other review was inspected and none of the candidate/dependency files was modified by this audit.

Current lines 158–169 now define

\[
Y=D\Psi_{t-t_0}(\theta(t_0))E_i,
\qquad g\sim N(0,I_n)
\]

with g independent of the trained trajectory, and explicitly identify Yg as the full raw-coordinate linear response associated with the infinitesimal top-column perturbation \(g/\sqrt n\). Conditional on the trajectory,

\[
\operatorname{Cov}(Yg\mid\text{trajectory})=YY^T.
\]

The finite-time flow derivative is invertible and E_i is an isometry, so Y has exactly n positive singular values. The current text correctly lists their squares as the n nonzero eigenvalues of \(YY^T\) and includes the N-n zero eigenvalues. It also explicitly uses an auxiliary derivative probe, without asserting Gaussian independence of the trained column or an exact Gaussian law for a finite nonlinear perturbation.

This resolves the only required correction identified in Section 7. The exact all-finite-physical-times/all-reached-starts trimmed spectral estimate, its explicit constants, and its separate raw-metric dependency are valid as proved above. No width-uniform normalized trace bound, endpoint derivative, or population closure is inferred.

Final current-hash verdict: **PASS** for ACTUAL_CLOCK_RANK_ONE_RESPONSE.md with SHA-256 `a3e093852f07d58b474197fd4781dfb69830203a21eda7e788d45af27f28f0bd`. No required corrections remain for that version.
