# Closure order, circle spectra, and the evolving kernel

Status: internally derived theory for this study; not independently reviewed or promoted. Frozen scoped input set and derivation date: 2026-09-14. No training or numerical experiment was run for this report. Static source inspection and source hashing were the only computation.

## Scope and contract

The target is the maintained `pde.observable_solver` with the `tanh-chebyshev-plus-code-v1` initializer, at orders 1, 2, 3, and 5, for two equally weighted circle directions with labels +1 and -1. The observable is the directly evaluated function on the entire circle, its Fourier coefficients, and its difference from the frozen initial kernel at the same order. This report studies the exact real-arithmetic finite population equations and, where explicitly stated, their exact symmetric population-integral counterpart. It does not identify arbitrary-angle or long-time runs with a separately proved neural-population limit.

The allowed scientific inputs were the complete solver, initializer, word grammar, their relevant arithmetic dependency, the notation contract, and the complete code README. No other study, study history, or sibling analysis was read. The current study README was intentionally outside this scoped assignment. Required research and rigorous-math skills were read. No external theorem or scientific source is needed for the derivations below.

Distinct approximation axes must remain distinct: order N; coefficient integration Q; population replay P; numerical precision; training step; circle sampling resolution. A finite circle panel is not a whole-circle certificate. In particular, increasing N at fixed Q and P can increase integration error and conditioning difficulty.

## 1. The exact represented function

Write the unit input as u(theta)=(cos(theta),sin(theta)). At first-population node i let b_i be a column vector in R^{d1}, w_i in R^2, and p_i its probability. At second-population node j let beta_j be a column vector in R^{d2}, c_j a scalar, and rho_j its probability. Both probability vectors sum to one. The trainable matrix is M in R^{d2 x d1}; b, beta and both probability vectors are frozen. The source fields are exactly

\[
 h_i(u)=\tanh(w_i\cdot u),\quad
 a(u)=\sum_i p_i b_i h_i(u),\quad
 z_j(u)=\beta_j^T M a(u),\quad
 H_j(u)=\tanh z_j(u),\quad
 f(u)=\sum_j\rho_j c_j H_j(u).
\]

Thus the circle function class at fixed marks is

\[
\mathcal F_N=\left\{\theta\mapsto
\sum_j\rho_jc_j\tanh\!\left[
\beta_j^TM\sum_i p_i b_i\tanh(w_i\cdot u(\theta))\right]
: w,c,M\text{ finite}\right\}.
\]

This is a parameterized nonlinear family, not a linear Fourier space. More precisely, a training trajectory visits a subset of this representable family, determined by its prescribed initialization and data; no reachability or universal-approximation assertion is being made. The moving w and c are unrestricted characteristic values at nodes, not degree-N expansions in the marks. N controls the frozen feature dictionary used in the middle action.

For a first-population function v define B1* v=E1[b v], and for a coefficient vector q define B2 q=beta^T q. The middle operator is B2 M B1*. Its reverse is B1 M^T B2*. Its rank is at most min(d1,d2), with a potentially smaller effective rank on an invariant trajectory. Operator rank on population functions and Fourier degree on the input circle are different notions.

## 2. What N retains, and what regularization changes

For the requested orders, the raw lower coordinates are

\[
 X=(\tanh G_1,\tanh G_2,\tanh R_1,\tanh R_2),\qquad
 R_k=\sqrt\tau Z_k+\alpha\tanh G_k,
\]

where (G1,G2,Z1,Z2) are independent standard Gaussian coordinates in the exact-integral construction. The upper coordinates are

\[
 Y=(\tanh\Xi_1,\tanh\Xi_2),\qquad \Xi_k=\sqrt v\,\widetilde Z_k,
\]

with independent upper standard Gaussians. The constants are the scalar integrals implemented by `initialize_features`: v=E tanh(G)^2, tau=E tanh(sqrt(v)G)^2, alpha=E[1-tanh(sqrt(v)G)^2]. Finite Q replaces these integrals with its prescribed deterministic rule.

The raw dictionary contains products of Chebyshev polynomials in these coordinates with total degree at most N. Since each degree-k Chebyshev polynomial has nonzero leading coefficient, these products span precisely the multivariate polynomial space of total degree at most N in X or Y. This degree refers to initialized marks, not theta. The counts are binomial(N+4,4) and binomial(N+2,2).

The exhaustive word codes 0 and 1 are already-retained constants; codes 2 and 3 are unbounded Gaussian seeds and are not appended. At N=5, codes 4 and 5 append sin(1) and cos(1) on population 1: two redundant constant functions that the syntax intentionally retains.

| N | Retained dimensions (d1,d2) | Odd polynomial dimensions |
|---|---|---|
| 1 | (5,3) | (4,2) |
| 2 | (15,6) | (4,2) |
| 3 | (35,10) | (24,6) |
| 5 | (128,21) | (80,12) |

Let Psi be a raw feature column, G=E[Psi Psi^T], eta=1/[1024(N+1)^2], and L L^T=G+eta I. The normalized features are b=L^{-1}Psi. The population operator B B* has kernel

\[
 b(\omega)^Tb(\omega')
 =\Psi(\omega)^T(G+\eta I)^{-1}\Psi(\omega').
\]

It is a ridge-filtered projection: in a nonzero Gram mode with eigenvalue lambda its nonzero operator eigenvalue is lambda/(lambda+eta). To verify this, diagonalize the real symmetric Gram; in each eigenmode the raw function has squared norm lambda, while its kernel coefficient is 1/(lambda+eta). Consequently the operator is generally not an orthogonal projection. At finite P with normalization computed using Q, the empirical P Gram differs from G_Q; even this same-rule eigenvalue description must then be qualified.

With raw contraction C and D=L2^{-1} C L1^{-T}, the initialized middle action is exactly

\[
v\longmapsto \Psi_2^T(G_2+\eta I)^{-1}
C(G_1+\eta I)^{-1} E_1[\Psi_1v].
\]

This is the concrete information retained by the initializer. The code computes

\[
C=U\,B^T+V\,\Gamma^T,
\]

where U=E[partial_{Xi} Psi2], B=E[Psi1 h^T], V=E[Psi2 tanh(Xi)^T], and Gamma=E[partial_R Psi1], each factor having two columns. Therefore rank(D) <= 4 for every requested order, in exact arithmetic even for the finite integration rule. At N=1 or 2, exact parity below sharpens this to rank(D) <= 2. Larger mark dictionaries can improve the represented functions in these few initial action directions without adding an equal number of action ranks. The evolving M is not constrained to have its initial rank.

## 3. Angular oddness is exact at every order

For any valid state, h_i(-u)=-h_i(u) because tanh is odd. Linearity gives a(-u)=-a(u), then z_j(-u)=-z_j(u), H_j(-u)=-H_j(u), and

\[
f(\theta+\pi)=-f(\theta).
\]

No symmetry of the population rule, data, weights or trajectory is needed. This identity is exact for the mathematical equations and is subject only to ordinary floating evaluation error in a numerical implementation.

Define the complex Fourier coefficient by hat f_k=(2pi)^{-1} integral_0^{2pi} f(theta)e^{-ik theta} dtheta. Splitting the integral at pi and substituting theta=s+pi in its second half gives

\[
\widehat f_k=\frac{1-(-1)^k}{2\pi}
\int_0^\pi f(s)e^{-iks}\,ds.
\]

Thus every even coefficient, including the mean, is zero. Oddness does not restrict the odd coefficients to k<=N or k<=2N+1.

Indeed, at every fixed dictionary in this implementation the constant feature is nonzero at every node. Set every w_i=R(1,0). Then a(u)=v tanh(R cos(theta)) with v=E1 b nonzero: its constant-feature coordinate equals 1/sqrt(1+eta). Choose a positive-weight upper node j0; beta_j0 is nonzero for the same reason. A rank-one M can satisfy beta_j0^T M v=kappa. Set c_j0=1/rho_j0 and every other c_j=0. The representable family consequently contains

\[
F_{R,\kappa}(\theta)=\tanh\bigl(\kappa\tanh(R\cos\theta)\bigr),\qquad R,\kappa>0.
\]

This is never a finite trigonometric polynomial. If it were, its symmetry theta -> -theta would make it a finite cosine sum, hence a polynomial P(cos(theta)) by the Chebyshev identities. Therefore P(x)=tanh(kappa tanh(Rx)) on [-1,1]. Both sides are real analytic on the real line; equality extends along the line because a real analytic function vanishing on an interval has every Taylor coefficient zero there and this identity propagates through overlapping analytic neighborhoods. The right side is bounded and nonconstant on R, whereas a bounded polynomial on R is constant, a contradiction.

Moreover F_{R,kappa} converges pointwise except at two points, and boundedly, to tanh(kappa) sign(cos(theta)) as R tends to infinity. Dominated convergence applies to every Fourier integral because |F|<=1. For positive odd k the limiting cosine coefficient is

\[
\frac{4\tanh\kappa}{\pi k}\sin(k\pi/2)\ne0,
\]

obtained by integrating cos(k theta) on the positive and negative half-circles. Thus any prescribed odd frequency can occur at fixed N. This is a representability result, not a claim that the two-point trajectory reaches these particular states. It is sufficient to reject an architectural Fourier-cutoff interpretation of N.

Every finite state nevertheless gives a real analytic circle function: all real tanh denominators are nonzero, and the finite composition extends holomorphically to some strip |Im(theta)|<delta around the compact real circle. For any narrower closed strip the extension is bounded by a finite M_delta. Shifting the Fourier integral upward or downward according to the sign of k, with the vertical sides canceling by periodicity, gives |hat f_k|<=M_delta exp(-delta|k|). The width delta depends on the entire state, and can shrink as weights grow. There is no state-independent frequency cutoff supplied by N. Smooth spectral decay and finite spectral support must be distinguished.

## 4. Why order 2 is largely redundant: a conditional exact result

This section assumes exact Gaussian integration for both coefficient formation and population evolution, or exact sign-paired integration rules preserving the same parity algebra. It does not assert exact symmetry for the default finite Halton cloud.

The lower involution S1 sends (G,Z) to (-G,-Z); the upper involution S2 sends Xi to -Xi. Both preserve their probability laws, and send every core coordinate X or Y to its negative. A total-degree-k Chebyshev product has parity (-1)^k. Opposite-parity raw Gram entries vanish by changing variables through the involution. Adding eta I preserves this separation. Cholesky normalization therefore mixes features only within their parity class, even though the source ordering interleaves classes: the scalar Cholesky recurrence has zero cross-parity entries by induction on its row and column indices.

Every row of B=E[Psi1 h^T] is zero for an even lower feature, since h is odd. Every row of Gamma=E[partial_R Psi1] is zero for an even lower feature, since differentiating reverses parity. The corresponding facts hold for U and V on the upper population. Hence D has only an odd-to-odd block.

At initialization w(S1 omega)=-w(omega), c=0, and M=D. Consider states with w odd, c odd, and only an odd-to-odd M block. Then h is odd as a function of the lower mark, so a has only odd feature coordinates. The upper preactivation and H are odd upper-mark functions. Put

\[
 d(u)=E_2[\beta c(1-H(u)^2)],\qquad
 q_i(u)=b_i^T M^T d(u).
\]

The vector d has only odd feature coordinates because c is odd and the gate is even. Thus q is odd in the lower mark. The exact velocities are

\[
\dot w_i=-2E_{(u,y)}[(f(u)-y)(1-h_i(u)^2)q_i(u)u],
\]
\[
\dot c_j=-2E_{(u,y)}[(f(u)-y)H_j(u)],\qquad
\dot M=-2E_{(u,y)}[(f(u)-y)d(u)a(u)^T].
\]

They preserve, respectively, odd lower w, odd upper c, and the odd-to-odd M block. Therefore this is an invariant subsystem wherever the exact solution exists. For a sign-paired finite rule, local uniqueness follows from the smooth finite-dimensional vector field, proving preservation from the prescribed initialization. For the exact integral version the assertion is conditional on the solution's existence and uniqueness in a class allowing the displayed expectations; the algebra itself is exact. Simultaneous Heun stages and affine state interpolation also preserve this linear parity structure in exact arithmetic.

N=2 adds only degree-2 even features. At the same ridge and the same joint Gaussian law, its active odd features, normalized active Grams, initial active D, and active vector field are identical to N=1. The even blocks remain inactive. Therefore the two predictions are identical under these matched assumptions.

The maintained ridge is not matched: eta_1=1/4096 and eta_2=1/9216. Also the default deterministic Halton/Box-Muller prefix is not sign-paired. Finite Q can mix odd and even features in its Gram and contraction; finite P can create nonzero even projections of odd functions. These facts can produce N=1 versus N=2 differences without a new exact odd feature channel. They do not imply those differences must be negligible. An uncontrolled numerical difference is inconclusive about the parity mechanism.

The exact active dimension counts are sums over odd degrees: lower 4; 4; 4+20=24; 4+20+56=80, and upper 2; 2; 2+4=6; 2+4+6=12. The two constant tails at N=5 are even and inactive under this same parity assumption.

## 5. N=0 is not the frozen kernel

The maintained API requires positive integer order; `build_dictionary(0)` is rejected. There is no implemented N=0 member to identify with NTK.

A hypothetical constant-only extension of this initializer would have zero feature derivatives, so both terms of C vanish and D=0. With the prescribed M=D=0 and c=0, the upper activation is zero. All three velocities are then zero for every data law. That extension would be a dead zero predictor, not a useful kernel model. This is a mathematical explanation, not a proposal to alter the API.

The legitimate frozen-kernel comparison exists separately at every N: freeze w=g and M=D, while evolving c by the same loss rule. Because f is linear in c at these fixed features, this exactly implements gradient flow with the closure's own initial tangent kernel. N and freezing the tangent kernel are independent approximation choices.

## 6. The exact changing kernel and the initial NTK regime

For any state define s_i(u)=1-h_i(u)^2 and t_j(u)=1-H_j(u)^2, and use a,d,q as above. The derivatives of the prediction are

\[
\frac{\partial f(u)}{\partial c_j}=\rho_j H_j(u),\quad
\frac{\partial f(u)}{\partial M}=d(u)a(u)^T,\quad
\frac{\partial f(u)}{\partial w_i}=p_i q_i(u)s_i(u)u.
\]

Substitution of the displayed velocities, with finite sums interchanged, gives

\[
\dot f(u)=-2E_{(v,y)}[K_t(u,v)(f(v)-y)],
\]

\[
K_t(u,v)=K_c(u,v)+K_M(u,v)+K_w(u,v),
\]
\[
K_c=E_2[H(u)H(v)],\quad
K_M=[d(u)^Td(v)][a(u)^Ta(v)],
\]
\[
K_w=(u\cdot v)E_1[q(u)q(v)s(u)s(v)].
\]

Each is a Gram kernel: use the features sqrt(rho_j)H_j(u), the entries of d(u)a(u)^T, and the vectors sqrt(p_i)q_i(u)s_i(u)u, respectively. Every finite Gram matrix of K is therefore positive semidefinite. For data masses nu_a and residuals r_a the loss derivative is

\[
\dot{\mathcal L}=-4\sum_{a,b}\nu_a\nu_b r_a K_t(u_a,u_b)r_b\le0.
\]

This identity concerns the exact flow; it does not certify loss decrease for an arbitrary Heun step.

At initialization c=0, so d=q=0, K_M=K_w=0 and

\[
K_0(u,v)=E_2[H_0(u)H_0(v)].
\]

Also dot w(0)=dot M(0)=0. Smooth local finite-dimensional evolution gives c(t)=O(t), w(t)-g=O(t^2), M(t)-D=O(t^2), and H_t-H_0=O(t^2), on any fixed finite query panel. Consequently K_t-K_0=O(t^2). If f_F solves the frozen K0 system from zero, subtraction of the two prediction equations yields a linear equation for f-f_F forced by (K_t-K0)r=O(t^2). Integration on a fixed panel, or an elementary finite-dimensional variation-of-constants formula, gives

\[
f_t-f_{F,t}=O(t^3).
\]

This only gives an upper order bound: the cubic coefficient can vanish in a special configuration. Very short training is inherently a weak discriminator of feature learning. Conversely, nonzero movement alone does not prove a meaningful change in the normalized circle shape; movement can largely alter gain or the training clock.

For two training points, dot M is the sum of two outer products and has rank at most two at an instant. Its time integral need not have rank two because both factors move; instantaneous update rank is not a bound on rank(M_t-D).

## 7. Rotation covariance and coordinate anchoring

For an orthogonal 2x2 matrix R, replace every data and query input u by Ru, and every lower vector w and frozen g by Rw and Rg, preserving b, beta, probabilities, M, D and c. Dot products, all fields and predictions are unchanged; the w velocity rotates by R and the other velocities are unchanged. This proves exact covariance of the equations under a simultaneous rotation of the full initialized state and the data. The same algebra holds for reflections and for the Heun map.

Rotating only the training and query directions while regenerating or keeping the original coordinate-anchored dictionary is a different operation. Its equivalence is not guaranteed. In particular the lower N=1 raw span is not closed under a generic rotation. To prove this, the rotated coordinate tanh((G1+G2)/sqrt(2)) is independent of the independent reverse-noise coordinates Z1,Z2. If it were in the span of 1,tanh G1,tanh G2,tanh R1,tanh R2, differentiating with respect to Z1 and Z2 forces the last two coefficients to be zero, since tau>0 and sech^2 is strictly positive. A remaining additive function of G1 and G2 has zero mixed second derivative. The rotated tanh has a mixed derivative that is nonzero on an open set, a contradiction.

Thus the finite mark span itself lacks full rotational closure; finite cubature is an additional possible source of anisotropy. This argument does not prove that a particular trained prediction or kernel has nonzero anisotropy, since contractions can cancel it. The specific size and N dependence of prediction anisotropy remain empirical questions. A complete-state rotation check is an exact implementation check. A fixed-initializer data rotation check measures the practical anchoring effect; it should be repeated after Q/P refinement before attributing it to the finite dictionary.

## 8. What two opposite labels can and cannot diagnose

Let the angles be theta_+=mu-Delta/2 and theta_-=mu+Delta/2, with 0<Delta<pi, equal probabilities, and labels +1,-1. A first harmonic already interpolates these labels:

\[
f(\theta)=-\frac{\sin(\theta-\mu)}{\sin(\Delta/2)}.
\]

Thus close opposite labels do not require high Fourier degree. They can instead create a large-amplitude low-frequency interpolant. Any differentiable interpolant obeys sup|f'|>=2/Delta by integrating its derivative on the short arc, but this slope lower bound is not a bandwidth lower bound. Circle amplitude, off-support overshoot, and normalized spectral energy must accompany slope measurements.

The endpoints have special meanings. At Delta=0, equally weighted conflicting duplicate labels impose loss f(u)^2+1, so the minimum loss is one; from the prescribed zero predictor the data forces cancel exactly. At Delta=pi the architectural identity f(-u)=-f(u) makes the two losses identical, so the entire data gradient equals that from one positively labeled point. The antipodal example is a useful symmetry check but loses the independent two-point interaction.

For intuition only, suppose a frozen kernel is rotation-invariant, K0(u(theta),u(phi))=k(theta-phi). Its two-point Gram has diagonal k(0), off-diagonal k(Delta), and antisymmetric eigenvalue lambda_-=k(0)-k(Delta)>=0. With unhalved equal-mass squared loss, the train predictions are (1-exp(-lambda_- t))(1,-1). For lambda_->0 the full frozen predictor is

\[
f_F(\theta,t)=\frac{1-e^{-\lambda_-t}}{\lambda_-}
\bigl[k(\theta-\theta_+)-k(\theta-\theta_-)\bigr].
\]

This follows by noting that the training residual is -exp(-lambda_-t)(1,-1) and integrating the off-training prediction derivative. It shows why same-clock curves can differ simply by gain; in this symmetric frozen case the normalized circle shape is time-independent. The maintained finite-order kernel need not satisfy the assumed rotation invariance, so the actual frozen control must use its computed Gram, not this formula unless that symmetry is verified.

## 9. Bounded discriminators for the study lead

These are designs, not executed experiments or evidence. The lead should freeze numeric tolerances and a hard compute budget before execution. Thresholds must exceed estimated discretization/integration variability; a failed validity gate is inconclusive.

1. **Fourier-cutoff hypothesis.** Compute the spectrum of N=1 predictions on a doubled circle grid at a preselected nontrivial loss. Resolved odd coefficients above frequency one reject the literal cutoff interpretation; the theory above already rejects it for the represented function class. Zero even coefficients test the architecture/analysis. Nonzero tiny coefficients without aliasing and resolution controls are not evidence.
2. **N=2 parity mechanism.** Compare N=1 and N=2 under the same sign-paired coefficient and population rule and the same ridge, then restore the maintained ridges. Matched parity predicts identical active trajectories up to numerical error; any larger discrepancy falsifies the claimed implementation equivalence or a setup assumption. Separately comparing default Halton rules tests operational differences but cannot identify their cause by itself.
3. **Changing-kernel mechanism.** At each N compare the full trajectory to its own initialized frozen-feature control, both at equal physical time and at equal training loss. Primary shape metrics can be the normalized L2-circle discrepancy and normalized Fourier-energy distribution, accompanied by output amplitude. Also record ||K_t-K0|| and the three kernel blocks. A gain-only explanation remains viable if normalized shape differences vanish under the numerical floor even when same-time outputs differ.
4. **Angle geometry without degeneracy.** Use a small preselected set of separations strictly between 0 and pi, including one acute and one obtuse case; retain endpoints as separate invariance checks. Fix data masses, labels, initial integration rules and all solver settings. Opposite-label two-point results alone cannot establish preference for any particular teacher or true test-risk improvement because no target labels away from support have been supplied.
5. **Anchoring versus invariant geometry.** For a fixed nondegenerate separation, compare a small preselected set of common rotations mu with the initializer held fixed. Measure the discrepancy after rotating predictions back. Use a complete-state rotation as an implementation control, and a Q/P refinement as the numerical-confounding check.

The highest-leverage experimental bottleneck is whether the normalized circle shape changes beyond the own-initialization frozen kernel at matched loss, after numerical refinement. Merely plotting successful training, increased parameter movement, larger high-frequency coefficients in absolute units, or a faster loss curve does not resolve that mechanism.

## Claim status ledger

| Claim | Status and scope | Remaining gap or falsifier |
|---|---|---|
| N indexes mark degree, not theta frequency | Exact from implementation | No convergence-rate conclusion follows |
| All even Fourier modes vanish | Proved for every valid exact state | Numerical violations diagnose evaluation/analysis error |
| No finite odd-frequency cutoff at fixed N | Proved for representable family | Which states are reached remains open |
| N=1/N=2 active equivalence | Exact under sign symmetry and matched ridge | Default Q/P and ridge violate matching assumptions |
| Initial D rank <=4 | Exact algebra for requested fast-core orders | Learned rank is a separate observable |
| N=0 is NTK | False for the maintained API | Use per-N frozen K0 instead |
| Full dynamics have a positive semidefinite changing kernel | Exact flow identity | Size and effect of kernel change are empirical |
| Nonlinear/frozen discrepancy is O(t^3) initially | Proved locally for finite smooth equations | Nonzero leading coefficient is not asserted |
| Complete-state rotation covariance | Proved | Fixed-initializer rotation invariance is different |
| Finite mark spans are rotation-closed | False already at N=1 | Prediction anisotropy can still cancel |
| Larger N gives monotone effective bandwidth or better generalization | Open; unsupported here | Requires controlled data and a stated target off support |

## Frozen source hashes

SHA-256, recorded after reading the complete source contents:

```text
711a648df33e587591d35bd709e3b1c052b1a6f7dc6513afe636b2acf7031605  code/pde/observable_solver.py
6dafe3b5906c8762c7b6e0782c535b0031bbcf206359d384ef0911853ce131d2  code/pde/observable_initialization.py
b12ed6021dfa8b8409b56793c88334d303f4c2cffeb7aa0a2d460311ba3e41b5  code/pde/observable_words.py
2181b9e47e1c765e440feff582b34208651ff4687e19ce8a96db7752402a6edb  code/pde/observable_arithmetic.py
199bb0786f632198a071d220544dd61ad54b24643f07f8232254c75b6f81500b  docs/NOTATION.md
b25c0ad7be0a770881c7ae75446a1718d4217ceec5576bdc14864790daffc91e  code/README.md
```

Implementation anchors: `_fields`, `rhs`, `initialize`, and `evolve` in the solver; `build_dictionary`, `_core_tables`, `_normalize`, and `initialize_features` in the initializer; `decode_word` in the grammar; `gaussian_points` in the arithmetic dependency. No maintained file was edited.
