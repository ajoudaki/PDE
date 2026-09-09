# Physical-scope correction: exact diff and provenance

2026-09-07. **UNVERIFIED — root has not promoted the candidate.**

## Immutable source and revised deliverable

The original 882-line source was preserved byte for byte before editing:

- Snapshot: /tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_CANONICAL_MEMORY_TEST.PRE_PHYSICAL_CORRECTION.md
- Snapshot SHA-256: d50d76b61e21d14bc45e73a41c89b763b26c157189af839c88e3073fe482273d
- Revised source: /tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_CANONICAL_MEMORY_TEST.md
- Revised source SHA-256: 7af67979a2734b4b2955e644a5a17b54497e6892c775d53cc175c990db494c3a
- Revised source length: 1012 lines.

The snapshot retains the original incorrect scope language for provenance.
The revised source withdraws that language; the snapshot is not current
contract authority. The exact unified diff below reconstructs the revised
source from the snapshot; this was checked against both complete texts.

## Scope of the correction

1. Constant label forcing is classified as auxiliary fixed-feature-time
   Euler forcing. It is not physical raw GD. The harmonic dependency is
   not used as authority for the physical clock.
2. The raw learning-rate contract remains eta = n^-2. The physical finite
   Euler program uses h c_ka, with c_ka = -2(f_ka-y_a). Distributional sample
   exchange and deterministic population limits give f_k2 = -f_k1 and
   lambda_k = 2h(1-f_k1). Selected residuals remain frozen in formal
   source derivatives.
3. The finite rescaled readout is iid N(0,n^-2), not exactly zero.
   The source supplies fixed-program restoration of its zero population
   root and includes empirical residual feedback. No uniform-in-mesh
   initial-readout restoration or simultaneous width/training-step
   identification is asserted.
4. Support preservation is conditional on nonzero update coefficients
   and absence of cancellation of the first two readout increments.
   The revision includes actual coarse physical examples showing why
   nonzero coefficients alone are insufficient for the old full-support
   formula. It then supplies a bound on all gradient blocks throughout
   each exact raw Euler segment, its joint empirical-average limit, and
   a sufficient mesh condition ensuring strictly positive population
   residuals on every fixed physical horizon. No uniform Hessian is used.
5. The physical two-update calculation uses lambda=2h,
   lambda_1=lambda(1-lambda v_0), and the exact readout
   (2lambda-lambda^2 v_0)d. Its Schur subtraction is
   delta_2-(2-lambda v_0)delta_1. The revision derives the unchanged
   leading innovation 2lambda^3 L^(2) and hence the same limiting
   reverse-memory norm lower bound >361/220 at rho=0.
6. The physical fixed-horizon lower bound uses the residual-positivity
   and initialization/identification bridges just described. It is not
   obtained by changing the clock label of the auxiliary result.
   General uniform covariance-norm upper bounds, full feedback control,
   the simultaneous eta=n^-2 raw training limit, and globalMF remain
   outside the result.

The original three mathematical dependencies were unchanged:

```text
a05a83e0ee5ea13d02a3ef51bb8967d1d3ddb7fd6eed601b4f1fdb4cea85c65a  /tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_UNIFORM_GAUSSIAN_RESPONSE_GAP.md
cb1ccec3a4431815b17ef6a8268c168a5feb5f6fe55b0a7c4a6b155ba7c69fb5  /tmp/l2-two-sample-proof-0ywjpp/HARMONIC_COVARIANCE_RESPONSE_TEST.md
875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603  /tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md
```

No new mathematical dependencies, external imports, experiments, or
subagents were used. All edits used apply_patch. The only writes were
the preserved snapshot, the revised source, and this provenance/diff
note. The first two lines of the following diff use stable filenames;
the complete absolute targets and hashes are recorded above.

## Exact unified diff

```diff
--- FROZEN_MASK_CANONICAL_MEMORY_TEST.PRE_PHYSICAL_CORRECTION.md
+++ FROZEN_MASK_CANONICAL_MEMORY_TEST.md
@@ -1,705 +1,833 @@
-# Frozen-mask gap and actual canonical L2 learned memories
+# Frozen-mask response and physical raw-GD memories: corrected candidate
 
-2026-09-06. Bounded theoretical research sidecar. No experiments,
-subagents, external mathematical imports, or continuum-limit claims.
+2026-09-07. **UNVERIFIED — not promoted by root.** The derivations below
+are submitted for review; they do not change that status.
 
-## Result and scope
+## Correction and scope
 
-The frozen-mask strict gap **does apply** to the canonical finite-mesh
-Gaussian population program with the specified first activation and top
-arctan, ordinary raw updates, zero initial readout, and every fixed
-\(-1<\rho<1\). Both the independent-root requirement and the
-frozen-coefficient derivative convention can be checked in this program.
+The preceding 882-line version incorrectly identified constant label
+forcing and exact finite-width zero readout with canonical physical raw
+GD. Those identifications are withdrawn. Constant forcing \(\lambda y_a\)
+defines an auxiliary fixed-feature-time Euler program. The harmonic
+dependency's label-clock convention is not physical contract authority.
 
-There is a useful correction to the generic support warning: **both
-actual learned memories preserve the covariance supports** in this
-particular program. At every finite positive mesh, the only linear
-history constraints are the forced startup identities
-\(H^{(1)}_1=H^{(1)}_0\) and \(\delta^{(2)}_0=0\). We prove this below.
-The shifted-activation, antiparallel example in the harmonic dependency
-is not an example for the present activations or correlation range.
+The contract is ordinary physical raw GD with \(\eta=n^{-2}\),
+\(c_{ka}=-2(f_{ka}-y_a)\), and finite rescaled readout
+\(\widetilde W^{(3)}_{0,i}\) iid \(N(0,n^{-2})\). Only its population
+root is zero. For the fixed physical Euler mesh \(h\), exchange symmetry
+gives the deterministic population relation
 
-A new actual-program obstruction nevertheless survives. On the attained
-prefix \(k=0,1,2\), at \(\rho=0\), for every specified \(0<R<1/4\),
+\[
+ f_{k2}=-f_{k1},\qquad h c_{ka}=\lambda_k y_a,\qquad
+ \lambda_k=2h(1-f_{k1}).                                  \tag{C1}
+\]
+
+This revision derives the residual coefficients, restores the finite
+initial readout, and controls gradients along entire physical Euler
+segments. The segment estimate supplies positive population residuals
+on sufficiently fine meshes of any fixed physical horizon, which is
+needed for the full-support assertion.
+
+The two-update obstruction transfers to these physical coefficients:
+at \(\rho=0\), the proposed conclusion remains
 
 \[
- \lim_{\lambda\downarrow0}
- \|M_B\|_{\operatorname{Ran}\Gamma\to\operatorname{Ran}\Sigma}
- >\frac{361}{220}>1.64.                                      \tag{A}
+ \lim_{h\downarrow0}\|M_B^{[0:2]}\|_{\Gamma\to\Sigma}
+       >361/220>1.64.                                    \tag{C2}
 \]
 
-The norms here are exactly the covariance norms of the candidate, on
-their supports. Thus reverse learned memory need not be a contraction
-and does not become small in that norm on a vanishing time horizon.
-This is an attained two-update construction, not an arbitrary matrix
-example. We also obtain exact two-update formulas and finite, strictly
-positive small-step limits for **both** memory norms, at every interior
-correlation.
+The actual second coefficient is
+\(\lambda_1=\lambda(1-\lambda v_0)\), where \(\lambda=2h\).
+The proof subtracts \((2-\lambda v_0)\delta^{(2)}_1\) in the
+Schur complement, not merely \(2\delta^{(2)}_1\).
 
-These results do not settle existence of finite upper bounds for the
-memory norms uniform over all meshes on a fixed horizon. Such bounds
-are neither proved nor disproved here. We give uniform bounds with
-ordinary coordinate/time-weighted Euclidean outputs, and state precisely
-the stronger matrix inequalities still needed. In particular, (A) is
-not a claim that those stronger norms diverge under mesh refinement,
-nor a claim about the full feedback product.
+All identification statements take width to infinity with \(h\) and
+the number of instructions fixed. Physical mesh refinement is a
+subsequent limit where explicitly stated. No simultaneous limit along
+the original width-dependent \(\eta=n^{-2}\) training sequence,
+continuum population flow, or globalMF is identified here. In particular,
+finite-prefix initialization restoration is not claimed uniform in mesh.
+No raw learning rate is replaced by a label coefficient, and no new
+training metric or clock is introduced.
 
-## 1. Exact dependencies and provenance
+## 1. Exact dependencies and preserved source
 
-The following three mathematical dependencies were read in full:
+Only these original mathematical dependencies were consulted, each
+previously read in full. Their hashes were rechecked and are unchanged.
 
-| File | SHA-256 |
+| Dependency | SHA-256 |
 |---|---|
-| `/tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_UNIFORM_GAUSSIAN_RESPONSE_GAP.md` | `a05a83e0ee5ea13d02a3ef51bb8967d1d3ddb7fd6eed601b4f1fdb4cea85c65a` |
-| `/tmp/l2-two-sample-proof-0ywjpp/HARMONIC_COVARIANCE_RESPONSE_TEST.md` | `cb1ccec3a4431815b17ef6a8268c168a5feb5f6fe55b0a7c4a6b155ba7c69fb5` |
-| `/tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md` | `875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603` |
-
-No mathematical files referenced inside those dependencies were read.
-The procedural skill `/etc/codex/skills/investigate-conjectures/SKILL.md`
-was read; its additional reference files were not imported, in accordance
-with the explicit dependency restriction. This is the only deliverable
-written. The candidate's previous UNVERIFIED status is resolved here
-only for the finite-program statements expressly proved below.
-
-We use the supplied raw label-update convention: \(\lambda y_b\) is
-the coefficient of sample \(b\), so \(\lambda=\Delta/2\) when the
-two-sample averaging factor is included in a step denoted by \(\Delta\).
-This is a notation conversion, not a change of learning rates or metric.
-No different loss-dependent forcing, random readout initialization,
-preconditioner, or division by an activation derivative is introduced.
+| /tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_UNIFORM_GAUSSIAN_RESPONSE_GAP.md | a05a83e0ee5ea13d02a3ef51bb8967d1d3ddb7fd6eed601b4f1fdb4cea85c65a |
+| /tmp/l2-two-sample-proof-0ywjpp/HARMONIC_COVARIANCE_RESPONSE_TEST.md | cb1ccec3a4431815b17ef6a8268c168a5feb5f6fe55b0a7c4a6b155ba7c69fb5 |
+| /tmp/l3-two-sample-proof-DLuelg/SOFTPLUS_FIXED_PROGRAM_IDENTIFICATION.md | 875fe50be7d9eb859810504649020ae0005be5f47109ef4f98c0c288cbf5d603 |
+
+Before revision, the entire 882-line source was preserved byte for byte,
+using apply_patch, as
+
+/tmp/l2-two-sample-proof-0ywjpp/FROZEN_MASK_CANONICAL_MEMORY_TEST.PRE_PHYSICAL_CORRECTION.md
+
+SHA-256:
+d50d76b61e21d14bc45e73a41c89b763b26c157189af839c88e3073fe482273d.
+
+Its historical claims and status language remain untouched in that
+snapshot; they are not current conclusions. The companion
+FROZEN_MASK_CANONICAL_MEMORY_TEST.PHYSICAL_CORRECTION_DIFF.md records
+the exact unified diff and revision hashes. The user's correction
+supplies contract authority. No additional mathematical dependency,
+external source, experiment, or subagent was used. The already-used
+procedural /etc/codex/skills/investigate-conjectures/SKILL.md organizes
+scope and status; no further skill reference was imported.
 
-## 2. The actual raw program, all memories, and all formal derivatives
+## 2. Physical equations and exchange symmetry
 
-Write
+Let \(y=(1,-1)^T\), \(Y=\operatorname{diag}(y)\),
 
 \[
  C=\begin{pmatrix}1&\rho\\\rho&1\end{pmatrix},\quad
- y=(1,-1)^T,\quad Y=\operatorname{diag}(y),\quad -1<\rho<1,
+ -1<\rho<1,\quad 0<R<1/4,
 \]
 \[
  \psi(z)=\phi_1'(z)=
- \begin{cases}
- \exp[-1/(1-(z/R)^2)],&|z|<R,\\
- 0,&|z|\ge R,
- \end{cases}
- \qquad \phi_1(z)=\int_0^z\psi(u)\,du,
-\]
-\[
- \beta=\int_0^R\psi(u)\,du,\qquad
- \phi_2(z)=\arctan z,\quad
- p(z)=\phi_2'(z)=\frac1{1+z^2},\quad
- p'(z)=\phi_2''(z)=\frac{-2z}{(1+z^2)^2}.                \tag{1}
-\]
-
-Thus \(|\phi_1|\le\beta\le R/e\), \(0\le\psi\le e^{-1}\),
-and all derivatives of both activations are bounded. The flat extension
-at \(\pm R\) is smooth: each differentiated bump is an exponential
-times a rational power of the distance expression, tending to zero.
+ \begin{cases}e^{-1/(1-(z/R)^2)},&|z|<R,\\0,&|z|\ge R,\end{cases}
+ \quad \phi_1(z)=\int_0^z\psi(u)\,du,\quad
+ \beta=\int_0^R\psi(u)\,du,
+\]
+\[
+ \phi_2(z)=\arctan z,\quad p(z)=\phi_2'(z)=\frac1{1+z^2},
+ \quad p'(z)=\phi_2''(z)=\frac{-2z}{(1+z^2)^2},
+ \quad m=e^{-1},\quad L=\pi/2.                            \tag{1}
+\]
 
-For completeness, the finite-width ordinary raw updates underlying the
-population law are
+All derivatives are bounded; the bump and its derivatives extend
+smoothly by zero. We have \(|\phi_1|\le\beta\le R/e\),
+\(0\le\psi\le m\), \(|\phi_2|\le L\), and \(0<p\le1\).
+
+Write \(w=\widetilde W^{(3)}\) as a column vector and
+\(\langle u,v\rangle_n=n^{-1}u^Tv\). The fixed-physical-mesh raw
+Euler equations in the contract's rescaled coordinates are
 
 \[
  \begin{aligned}
  h^{(1)}_{ka}&=\phi_1(z^{(1)}_{ka}),&
- z^{(2)}_{ka}&=W^{(2)}_k h^{(1)}_{ka},&
+ z^{(2)}_{ka}&=W^{(2)}_kh^{(1)}_{ka},&
  h^{(2)}_{ka}&=\phi_2(z^{(2)}_{ka}),\\
+ f_{n,ka}&=\langle w_k,h^{(2)}_{ka}\rangle_n,&
+ c_{n,ka}&=-2(f_{n,ka}-y_a),\\
  \delta^{(2)}_{ka}&=w_kp(z^{(2)}_{ka}),&
  q^{(1)}_{ka}&=(W^{(2)}_k)^T\delta^{(2)}_{ka},&
  \delta^{(1)}_{ka}&=\psi(z^{(1)}_{ka})q^{(1)}_{ka},\\
  z^{(1)}_{k+1,a}&=z^{(1)}_{ka}
-       +\lambda\sum_b C_{ab}y_b\delta^{(1)}_{kb},\\
+          +h\sum_b C_{ab}c_{n,kb}\delta^{(1)}_{kb},\\
  W^{(2)}_{k+1}&=W^{(2)}_k+
-       \frac\lambda n\sum_b y_b\delta^{(2)}_{kb}(h^{(1)}_{kb})^T,\\
- w_{k+1}&=w_k+\lambda\sum_b y_bh^{(2)}_{kb}.
+        \frac h n\sum_b c_{n,kb}\delta^{(2)}_{kb}(h^{(1)}_{kb})^T,\\
+ w_{k+1}&=w_k+h\sum_b c_{n,kb}h^{(2)}_{kb}.
  \end{aligned}                                                   \tag{2}
 \]
 
-The initialization is the supplied one: iid first-neuron pairs
-\(G\sim N(0,C)\), an independent matrix with iid \(N(0,1/n)\)
-entries, and exactly \(w_0=0\). Products in (2) are coordinatewise
-where appropriate. No caps are present in (2).
+The factors are those of the rescaled raw equations, not a selected
+preconditioner. The raw learning-rate contract \(\eta=n^{-2}\) remains
+unchanged; \(h\) is the physical Euler-mesh parameter of this fixed-program
+comparison. Equation (2) is not obtained by assigning \(\eta\) a new
+value or by making a feature-clock substitution.
+
+The iid first-neuron pairs have law \(N(0,C)\);
+\(W^{(2)}_0\) has iid \(N(0,1/n)\) entries, independently, and
+
+\[
+ w_{0,i}\stackrel{\mathrm{iid}}{\sim}N(0,n^{-2}).          \tag{3}
+\]
+
+Thus finite-width zero backward fields and identical time-zero/time-one
+features are not exact identities. Section 4 restores their population
+versions.
 
-Fix \(k=0,\ldots,N\) and \(\lambda>0\). Set \(i=(k,a)\),
-\(j=(r,b)\), with \(j<i\) meaning \(r<k\). The population law is
+For exchange symmetry, exchange the two initial first-layer sample
+coordinates, leave \(W^{(2)}_0\) unchanged, and send \(w_0\) to \(-w_0\).
+The initialization law is invariant. Induction in (2) sends
+\(z^{(1)}_{ka}\) to \(z^{(1)}_{k,\bar a}\), \(W^{(2)}_k\) to itself,
+\(w_k\) to \(-w_k\), \(f_{n,ka}\) to \(-f_{n,k,\bar a}\),
+and \(c_{n,ka}\) to \(-c_{n,k,\bar a}\).
+Each backward field changes sign and exchanges its sample index.
+The products \(c\delta\) retain their sign in the hidden updates,
+while the readout update changes sign. The exchange-invariant \(C\)
+makes the first update consistent. Once the predictions have
+deterministic fixed-program limits, this distributional symmetry forces
+
+\[
+ f_{k2}=-f_{k1},\quad r_k=1-f_{k1},\quad
+ c_{k1}=2r_k,\quad c_{k2}=-2r_k,\quad \lambda_k=2hr_k.      \tag{4}
+\]
+
+No finite-width pathwise relation \(f_{n,k2}=-f_{n,k1}\) is assumed.
+
+## 3. Population law, complete memories, and formal derivatives
+
+For \(i=(k,a)\), \(j=(r,b)\), write \(j<i\) when \(r<k\).
+The physical population program is
 
 \[
  \begin{aligned}
- Z^{(1)}_{ka}&=G_a+\lambda\sum_{r<k,b}C_{ab}y_b
-              \psi(Z^{(1)}_{rb})Q^{(1)}_{rb},&
+ Z^{(1)}_{ka}&=G_a+\sum_{r<k,b}\lambda_r C_{ab}y_b
+                      \psi(Z^{(1)}_{rb})Q^{(1)}_{rb},&
  H^{(1)}_i&=\phi_1(Z^{(1)}_i),\\
  Z^{(2)}_i&=\xi^{(2)}_i+\sum_{j<i}A_{ij}\delta^{(2)}_j,&
  H^{(2)}_i&=\phi_2(Z^{(2)}_i),\\
- \mathsf W_k&=\lambda\sum_{r<k,b}y_bH^{(2)}_{rb},&
+ \mathsf W_k&=\sum_{r<k,b}\lambda_r y_bH^{(2)}_{rb},&
  \delta^{(2)}_i&=\mathsf W_kp(Z^{(2)}_i),\\
- Q^{(1)}_i&=\zeta^{(1)}_i+\sum_{r\le k,b}B_{i,rb}H^{(1)}_{rb}.
- \end{aligned}                                                   \tag{3}
+ Q^{(1)}_i&=\zeta^{(1)}_i+\sum_{r\le k,b}B_{i,rb}H^{(1)}_{rb},&
+ f_{ka}&=\mathbb E_2[\mathsf W_kH^{(2)}_{ka}].
+ \end{aligned}                                                   \tag{5}
 \]
 
-The independent Gaussian groups are \(G\), \(\zeta^{(1)}\), and
-\(\xi^{(2)}\). Population 1 uses \((G,\zeta^{(1)})\); population 2
-uses \(\xi^{(2)}\). The covariance selections are uncentered query
-second moments:
+Before symmetry, use the selected \(h c_{rb}\) in place of
+\(\lambda_r y_b\). The time-\(k\) prediction is constructed before
+\(c_k\) enters the next update. The independent Gaussian groups are
+\(G\sim N(0,C)\), \(\zeta^{(1)}\), and \(\xi^{(2)}\), with
 
 \[
  \Gamma_{ij}=\mathbb E_1[H^{(1)}_iH^{(1)}_j]
-       =\operatorname{Cov}(\xi^{(2)})_{ij},\qquad
+             =\operatorname{Cov}(\xi^{(2)})_{ij},\qquad
  \Sigma_{ij}=\mathbb E_2[\delta^{(2)}_i\delta^{(2)}_j]
-       =\operatorname{Cov}(\zeta^{(1)})_{ij}.                    \tag{4}
+             =\operatorname{Cov}(\zeta^{(1)})_{ij}.        \tag{6}
+\]
+\[
+ \begin{aligned}
+ S_{ij}&=\mathbb E_1\partial_{\zeta^{(1)}_j}H^{(1)}_i,&
+ (M_A)_{ij}&=\mathbf1_{r<k}\lambda_r\Gamma_{ij}y_b,& A&=S+M_A,\\
+ D_{ij}&=\mathbb E_2\partial_{\xi^{(2)}_j}\delta^{(2)}_i,&
+ (M_B)_{ij}&=\mathbf1_{r<k}\lambda_r\Sigma_{ij}y_b,& B&=D+M_B.
+ \end{aligned}                                                   \tag{7}
 \]
 
-The complete matrices are
+These are uncentered query moments. Unrolling (2) gives the learned
+forward and reverse terms, respectively,
 
 \[
- \begin{aligned}
- S_{ij}&=\mathbb E_1[\partial_{\zeta^{(1)}_j}H^{(1)}_i],&
- (M_A)_{ij}&=\lambda\mathbf1_{r<k}\Gamma_{ij}y_b,& A&=S+M_A,\\
- D_{ij}&=\mathbb E_2[\partial_{\xi^{(2)}_j}\delta^{(2)}_i],&
- (M_B)_{ij}&=\lambda\mathbf1_{r<k}\Sigma_{ij}y_b,& B&=D+M_B.
- \end{aligned}                                                   \tag{5}
+ \sum_{r<k,b}h c_{n,rb}\delta^{(2)}_{rb}
+          \langle h^{(1)}_{rb},h^{(1)}_{ka}\rangle_n,\qquad
+ \sum_{r<k,b}h c_{n,rb}h^{(1)}_{rb}
+          \langle\delta^{(2)}_{rb},\delta^{(2)}_{ka}\rangle_n.
 \]
 
-These memories follow directly by unrolling the trained matrix in (2):
-the forward learned term is
-\(\lambda\sum_{r<k,b}y_b\delta^{(2)}_{rb}
-\langle h^{(1)}_{rb},h^{(1)}_{ka}\rangle_n\), and the reverse term is
-\(\lambda\sum_{r<k,b}y_bh^{(1)}_{rb}
-\langle\delta^{(2)}_{rb},\delta^{(2)}_{ka}\rangle_n\).
-The initial-matrix responses supply exactly \(S\) and \(D\).
-There is no current learned-rank term, but there is a current derivative
-term in \(D\).
-
-Here are explicit recursions specifying every derivative in (5). For a
-formal bottom-source slot \(j\), put
-\(U^{(1)}_{ka,j}=\partial_{\zeta^{(1)}_j}Z^{(1)}_{ka}\) and
-\(V^{(1)}_{ka,j}=\partial_{\zeta^{(1)}_j}Q^{(1)}_{ka}\). Then
+Their coefficients converge jointly with predictions and queries.
+Initial-matrix reuse supplies \(S,D\); neither learned term is omitted.
+
+For a formal reverse slot \(j\), let \(U^{(1)}=\partial_jZ^{(1)}\)
+and \(V^{(1)}=\partial_jQ^{(1)}\). Then
 
 \[
  \begin{aligned}
  U^{(1)}_{0a,j}&=0,\\
  V^{(1)}_{ka,j}&=\mathbf1_{(k,a)=j}
-       +\sum_{r\le k,b}B_{ka,rb}\psi(Z^{(1)}_{rb})U^{(1)}_{rb,j},\\
- U^{(1)}_{k+1,a,j}&=U^{(1)}_{ka,j}
-   +\lambda\sum_b C_{ab}y_b
-       \bigl[\psi'(Z^{(1)}_{kb})Q^{(1)}_{kb}U^{(1)}_{kb,j}
-              +\psi(Z^{(1)}_{kb})V^{(1)}_{kb,j}\bigr],\\
+   +\sum_{r\le k,b}B_{ka,rb}\psi(Z^{(1)}_{rb})U^{(1)}_{rb,j},\\
+ U^{(1)}_{k+1,a,j}&=U^{(1)}_{ka,j}+\lambda_k\sum_b C_{ab}y_b
+ [\psi'(Z^{(1)}_{kb})Q^{(1)}_{kb}U^{(1)}_{kb,j}
+                   +\psi(Z^{(1)}_{kb})V^{(1)}_{kb,j}],\\
  S_{ka,j}&=\mathbb E_1[\psi(Z^{(1)}_{ka})U^{(1)}_{ka,j}].
- \end{aligned}                                                   \tag{6}
+ \end{aligned}                                                   \tag{8}
 \]
 
-For a formal top-source slot \(j\), put
-\(U^{(2)}_{i,j}=\partial_{\xi^{(2)}_j}Z^{(2)}_i\) and
-\(T^{(2)}_{i,j}=\partial_{\xi^{(2)}_j}\delta^{(2)}_i\). Then
+For a formal forward slot \(j\), let \(U^{(2)}=\partial_jZ^{(2)}\)
+and \(T^{(2)}=\partial_j\delta^{(2)}\). Then
 
 \[
  \begin{aligned}
  U^{(2)}_{i,j}&=\mathbf1_{i=j}+\sum_{l<i}A_{il}T^{(2)}_{l,j},\\
- \partial_{\xi^{(2)}_j}\mathsf W_k
-    &=\lambda\sum_{r<k,b}y_bp(Z^{(2)}_{rb})U^{(2)}_{rb,j},\\
- T^{(2)}_{ka,j}&=p(Z^{(2)}_{ka})\partial_{\xi^{(2)}_j}\mathsf W_k
-           +\mathsf W_kp'(Z^{(2)}_{ka})U^{(2)}_{ka,j},\\
- D_{ka,j}&=\mathbb E_2 T^{(2)}_{ka,j}.
- \end{aligned}                                                   \tag{7}
+ \partial_j\mathsf W_k&=\sum_{r<k,b}\lambda_r y_bp(Z^{(2)}_{rb})
+                                                   U^{(2)}_{rb,j},\\
+ T^{(2)}_{ka,j}&=p(Z^{(2)}_{ka})\partial_j\mathsf W_k
+               +\mathsf W_kp'(Z^{(2)}_{ka})U^{(2)}_{ka,j},\\
+ D_{ka,j}&=\mathbb E_2T^{(2)}_{ka,j},\qquad
+ D_{ka,kb}=\mathbf1_{a=b}\mathbb E_2[\mathsf W_kp'(Z^{(2)}_{ka})].
+ \end{aligned}                                                   \tag{9}
 \]
 
-In particular,
+All selected \(f,c,\lambda,A,B,\Gamma,\Sigma\) are frozen in these
+derivatives. In particular no term
+\(\partial\lambda_r=-2h\,\partial f_{r1}\) is inserted.
+That would differentiate statistical selection, a different operation.
+The readout-history derivative in (9) is retained. Formal slots are
+retained even when their covariance is singular. For example, in the
+population,
 
 \[
- D_{ka,kb}=\mathbf1_{a=b}\mathbb E_2[\mathsf W_kp'(Z^{(2)}_{ka})].
-                                                                  \tag{8}
+ \zeta^{(1)}_0=0,\quad \xi^{(2)}_1=\xi^{(2)}_0,\qquad
+ S_{1a,0b}=\lambda_0 C_{ab}y_b\mathbb E[\psi(G_a)\psi(G_b)].
+                                                                  \tag{10}
 \]
 
-Every selected covariance, coefficient, and scalar expectation in
-(3)--(7) is held fixed during differentiation. We differentiate the
-complete earlier coordinate expressions, including the readout history;
-we do not differentiate the statistical operation selecting the
-coefficients. The formal slots remain separate even when their values
-coincide. In particular \(\zeta^{(1)}_0=0\) and
-\(\xi^{(2)}_1=\xi^{(2)}_0\) do not authorize deleting those slots.
-For example, at startup
-
-\[
- S_{1a,0b}=\lambda C_{ab}y_b\mathbb E[\psi(G_a)\psi(G_b)],           \tag{9}
-\]
-
-although the source in that column has zero attained variance. The
-initial readout is held fixed at zero; a derivative with respect to a
-formal readout root is a different direction and is not given a
-zero-cost covariance norm here.
-
-## 3. Why the finite Gaussian rule transfers to these activations
-
-The softplus dependency cannot be invoked by simply substituting
-activation names. In particular, the uncapped bottom map
-\((z,q)\mapsto\psi(z)q\) is not globally Lipschitz:
-its first derivative in \(z\) is \(\psi'(z)q\). The following finite
-argument addresses that issue; it is not a uniform cap-removal theorem.
-
-First, the remaining query maps are bounded or Lipschitz on their
-attained ranges. At every width and in (3),
-
-\[
- |\mathsf W_k|\le\pi\lambda k,\qquad
- |\delta^{(2)}_{ka}|\le\pi\lambda k.                         \tag{10}
-\]
-
-Thus, for a fixed prefix, the map \(w p(z)\) can be given a smooth
-globally Lipschitz extension outside the deterministic attained readout
-interval without changing a single actual value. Both matrix input
-families \(H^{(1)}\) and \(\delta^{(2)}\) have deterministic coordinate
-bounds. The finite rank expansions bound the trained matrix operator
-norm by the initial operator norm plus a deterministic finite sum.
-Consequently all raw and bounded-bottom auxiliary programs have RMS
-bounds depending only on that operator norm and the fixed prefix.
-
-For the identification proof only, replace \(q\) in the bottom update
-by a smooth cutoff \(\tau_L(q)\), equal to \(q\) on \([-L,L]\),
-with \(|\tau_L(q)|\le|q|\), bounded value and first derivative.
-For each fixed \(L\), all required maps are globally Lipschitz, so the
-self-contained conditioning, finite-rank feedback, and singular-Gram
-arguments in the softplus dependency apply with one matrix and the
-checked maps above. No softplus identity is used in those arguments.
-
-At the scalar-law level let \(L\to\infty\) in causal instruction
-order. For every fixed compact set of preceding coefficients,
-\(Q^{(1)}\) is a Gaussian coordinate plus a bounded linear combination
-of bounded features. Bottom coordinate expressions and their formal
-first derivatives have polynomial bounds in the finite Gaussian source
-tuple, uniformly for large cutoff levels. One can choose
-\(\tau_L(q)=L\tau(q/L)\), with uniformly bounded first derivatives.
-Finite induction, Gaussian square-root coupling, and dominated
-convergence therefore give convergence of all selected second moments
-and expected derivatives. The limiting recursion is exactly (3)--(7).
-The induction also bounds its coefficients, and hence the auxiliary
-scalar \(Q^{(1)}\) tails are uniformly Gaussian up to a bounded shift
-for all sufficiently large \(L\).
-
-Here is the needed transfer back to the uncapped finite-width program,
-without assuming its higher coordinate moments. Compare raw and
-cutoff programs with identical initialization. If \(\widetilde q\)
-is a cutoff-program reverse answer, the exceptional product is bounded
-in normalized Euclidean norm, for any fixed \(K>0\), by
+The last quantity need not vanish. These startup identities follow
+after population initialization restoration.
+
+## 4. Fixed-program bridge and restoration of the finite readout
+
+The softplus proof cannot simply be invoked with renamed activations:
+\((z,q)\mapsto\psi(z)q\) is not globally Lipschitz. Its \(z\)
+derivative is \(\psi'(z)q\). The following finite argument checks
+this issue and the actual readout initialization.
+
+Put \(R_{n,k}=\|w_k\|_{n,2}\), \(B_{n,k}=\|W^{(2)}_k\|_{\rm op}\).
+For nonsymmetric finite residuals as well as for the population,
 
 \[
- \begin{aligned}
- \|\psi(z)q-\psi(\widetilde z)\tau_L(\widetilde q)\|_{n,2}
- \le{}& e^{-1}\|q-\widetilde q\|_{n,2}
-   +K\|\psi'\|_\infty\|z-\widetilde z\|_{n,2}\\
- &+2e^{-1}\|\widetilde q\mathbf1_{|\widetilde q|>K}\|_{n,2}
-   +2e^{-1}\|\widetilde q\mathbf1_{|\widetilde q|>L}\|_{n,2}.
- \end{aligned}                                                   \tag{11}
+ |f_{n,ka}|\le LR_{n,k},\quad \sum_a|c_{n,ka}|\le4(1+LR_{n,k}),
+\]
+\[
+ R_{n,k+1}\le R_{n,k}+4hL(1+LR_{n,k}),\quad
+ B_{n,k+1}\le B_{n,k}+4h\beta R_{n,k}(1+LR_{n,k}).          \tag{11}
 \]
 
-This follows by adding and subtracting \(\psi(z)\widetilde q\) and
-\(\psi(\widetilde z)\widetilde q\), then splitting the middle product
-at \(K\). All other differences use bounded gates, the matrix
-operator bound, and the ordinary contraction Cauchy--Schwarz estimate.
-On an event bounding the initial operator norm, finite induction bounds
-the full RMS discrepancy by a polynomial in \(K\), of fixed degree,
-times the finite sum of the tail terms in (11).
+On \(R_{n,0}\le1,\ B_{n,0}\le10\), for all \(kh\le T\), these imply
 
-For fixed \(K,L\), the cutoff identification supplies those empirical
-tail estimates, using continuous upper bounds of the tail indicators.
-After the width limit, let \(L\to\infty\), then \(K\to\infty\).
-The uniform Gaussian tails just established dominate every fixed
-polynomial in \(K\). Finally release the initial-operator bound using
-the elementary Gaussian operator tail proved in the dependency.
-This transfers the finite law and the bounded query second moments to
-the original uncapped program. Only a fixed number of instructions is
-involved; no assertion uniform in the prefix is obtained from (11).
+\[
+ R_{n,k}\le R_T:=(1+1/L)e^{4L^2T}-1/L,\qquad
+ B_{n,k}\le B_T:=10+4\beta T R_T(1+LR_T).                 \tag{12}
+\]
 
-The same conditioning proof explains independence precisely. A new
-Gaussian source is a deterministic linear combination of earlier
-sources of its own orientation and an innovation independent of all
-previous source groups and roots. Thus the entire reverse group
-\(\zeta^{(1)}\) is independent of \(G\), although the actual
-\(Q^{(1)}\) and trained first features are not. The singular-Gram
-transfer preserves this product Gaussian representation. The covariance
-parameters depend on the law of \(G\), not its sampled value.
-The auxiliary cutoffs and query regularizations in this proof leave no
-change to initialization or to the final raw program (2)--(3).
+Iterate the affine first recurrence using
+\((1+4hL^2)^k\le e^{4L^2T}\), then sum the second. Also
 
-## 4. Verified strict gap and its exact boundary
+\[
+ \|w_k\|_\infty\le\|w_0\|_\infty+4TL(1+LR_T).             \tag{13}
+\]
 
-Let \(H\) stack \(H^{(1)}\), and put
+These bounds still hold when the bottom reverse factor alone is
+cut off. The initial event, augmented by \(\|w_0\|_\infty\le1\),
+has probability tending to one: use the Gaussian operator tail proved
+in the dependency and
 
 \[
- \mathcal F=\{|G_1|\ge R,\ |G_2|\ge R\},\qquad
- \alpha=\Pr(\mathcal F^c)
- \le\frac{4R}{\sqrt{2\pi}}<1.                              \tag{12}
+ \Pr(\|w_0\|_\infty>\varepsilon)\le
+       2n e^{-n^2\varepsilon^2/2},\qquad
+ \mathbb E\|w_0\|_{n,2}^2=n^{-2}.                         \tag{14}
 \]
 
-On \(\mathcal F\), both bottom gates vanish. Induction in (3) gives
-\(Z^{(1)}_{ka}=G_a\) and
-\(H^{(1)}_{ka}=\beta\operatorname{sign}(G_a)\) for every formal
-reverse-source value. This uses the full actual \(B=D+M_B\) and
-requires no bound or sign on it.
+For the proof only, replace the bottom \(q\)-factor by
+\(\tau_Q(q)=Q\tau(q/Q)\), equal to \(q\) for \(|q|\le Q\), with
+\(|\tau_Q(q)|\le|q|\) and bounded first derivative uniformly in \(Q\).
+On each bounded-initial-data event, (13) permits a smooth globally
+Lipschitz extension of \(w p(z)\) outside the attained readout interval.
+For fixed \(Q\), all required coordinate maps are globally Lipschitz.
+The prediction contraction and the linear scalar arithmetic
+\(c=-2(f-y)\) are among the dependency's allowed scalar-feedback
+operations. Its conditioning and singular-Gram proof therefore applies
+to this residual-driven fixed graph.
+
+For that fixed cutoff graph, couple (3) with zero initial readout.
+The ordinary RMS/operator-norm induction for Lipschitz maps and
+contractions, (11)--(14), shows that the finite initial discrepancy
+tends to zero at every node. This proves a zero population root, not
+an exactly zero finite readout.
+
+At the scalar level remove \(Q\) in causal order. Readout increments
+are bounded on a fixed prefix. A bottom reverse answer is a Gaussian
+coordinate plus a deterministic linear combination of bounded features.
+Coordinate expressions and their formal first derivatives have
+polynomial bounds in the finite Gaussian tuple, uniformly on compact
+sets of preceding coefficients and uniformly for large \(Q\).
+Gaussian square-root coupling and dominated convergence therefore
+transfer query second moments, residuals, and expected derivatives
+through each finite instruction, including singular covariance cases.
+The resulting law is (5)--(9). This induction also bounds the selected
+coefficients and gives uniformly Gaussian tails up to a bounded shift
+for the cutoff population bottom reverse answers at large \(Q\).
 
-Write \(\zeta^{(1)}=\Sigma^{1/2}Z\) with standard Gaussian \(Z\)
-independent of \(G\). For any vector \(v\), finite-recursion
-polynomial derivative bounds justify Gaussian integration by parts:
+To transfer to the uncapped finite-width law, compare a raw state with
+a cutoff reference state. For a fixed splitting level \(K>0\),
 
 \[
- \mathbb E[Z(v^TH)]=\Sigma^{1/2}S^Tv.
+ \begin{aligned}
+ \|\psi(z)q-\psi(\widetilde z)\tau_Q(\widetilde q)\|_{n,2}
+ \le{}&m\|q-\widetilde q\|_{n,2}
+ +K\|\psi'\|_\infty\|z-\widetilde z\|_{n,2}\\
+ &+2m\|\widetilde q\,\mathbf1_{|\widetilde q|>K}\|_{n,2}
+ +2m\|\widetilde q\,\mathbf1_{|\widetilde q|>Q}\|_{n,2}.
+ \end{aligned}                                                   \tag{15}
+\]
+
+Add and subtract \(\psi(z)\widetilde q\) and
+\(\psi(\widetilde z)\widetilde q\), then split the middle product.
+All other state and residual differences use the finite bounds above
+and contraction Cauchy--Schwarz. Finite induction gives a polynomial
+in \(K\), of fixed degree, times the reference tail errors and initial
+discrepancy. At fixed cutoff the empirical theorem controls the tails
+by continuous upper bounds. Take width first, then \(Q\to\infty\),
+then \(K\to\infty\); the Gaussian reference tails dominate the fixed
+polynomial. This supplies joint prediction and mixed-second-moment
+identification for the displayed fields under the actual initialization
+and uncapped equations, including the first backward fields needed in
+the segment contractions below. RMS comparison and bounded RMS norms
+transfer their pairings by Cauchy--Schwarz.
+No graph-length-uniform assertion is obtained from this argument.
+
+Source independence has a specific origin: conditioning appends each
+Gaussian source as a deterministic combination of older sources in
+its own orientation plus an independent innovation. The full
+\(\zeta^{(1)}\) group consequently remains independent of \(G\).
+Residual feedback selects deterministic population coefficients, not
+coefficients depending on a sampled root. The independent initial
+readout tends to zero. Neither operation destroys that representation.
+Actual reverse answers and trained features need not be independent
+of \(G\).
+
+## 5. Continuous gradient bounds along exact physical Euler segments
+
+Interpolate the actual raw parameter segment
+\(\theta_k(u)=\theta_k+u(\theta_{k+1}-\theta_k)\), \(0\le u\le1\).
+In (2)'s rescaled coordinates, \(z^{(1)},W^{(2)},w\) interpolate
+linearly. Recompute all nonlinear fields at the interpolated parameter:
+in particular \(z^{(2)}(u)=W^{(2)}(u)\phi_1(z^{(1)}(u))\) is not
+a linearly interpolated stored activation.
+
+Convexity of ordinary norms preserves (12) on each entire segment.
+Consequently, at every point of every segment with endpoints in
+\([0,T]\),
+
+\[
+ \|h^{(1)}_a\|_{n,2}\le\beta,\quad
+ \|h^{(2)}_a\|_{n,2}\le L,\quad
+ \|\delta^{(2)}_a\|_{n,2}\le R_T,\quad
+ \|\delta^{(1)}_a\|_{n,2}\le mB_T R_T.                    \tag{16}
 \]
 
-The contribution on \(\mathcal F\) is zero by independence. Testing
-against a unit vector \(u\) and applying Cauchy--Schwarz gives
+The last bound uses \(\delta^{(1)}=\psi(z^{(1)})(W^{(2)})^T
+(wp(z^{(2)}))\); it needs no coordinate bound on \(q^{(1)}\).
+
+The chain rule along this exact parameter segment gives
 
 \[
- |\mathbb E[\mathbf1_{\mathcal F^c}(u^TZ)(v^TH)]|^2
- \le\alpha\mathbb E[\mathbf1_{\mathcal F^c}(v^TH)^2].
+ \frac d{du}f_{n,a}(\theta_k(u))
+       =h\sum_b c_{n,kb}\mathcal K_{n,ab}(u,k),           \tag{17}
+\]
+\[
+ \begin{aligned}
+ \mathcal K_{n,ab}(u,k)
+ ={}&\langle h^{(2)}_a(u),h^{(2)}_{kb}\rangle_n\\
+ &+\langle\delta^{(2)}_a(u),\delta^{(2)}_{kb}\rangle_n
+                 \langle h^{(1)}_a(u),h^{(1)}_{kb}\rangle_n\\
+ &+C_{ab}\langle\delta^{(1)}_a(u),\delta^{(1)}_{kb}\rangle_n.
+ \end{aligned}                                                   \tag{18}
 \]
 
-Taking the supremum over \(u\) proves
+These are the readout, middle-matrix, and shared first-weight gradient
+contractions dictated by (2). The middle term has one \(1/n\) from
+the prediction differential and one from the rank update; the other
+two terms have one normalized neuron pairing. The prediction-gradient
+blocks in these coordinates have ordinary norms bounded respectively
+by \(L/\sqrt n,\ \beta R_T,\ mB_TR_T/\sqrt n\) (Frobenius norms
+for matrices and unit-norm sample inputs). Their update factors are
+already fixed by the raw rescaling in (2); no training metric is chosen
+to obtain the estimate.
+
+Cauchy--Schwarz on the three concatenated gradient blocks, retaining
+the input vectors whose Gram is \(C\), yields
 
 \[
- S\Sigma S^T\preceq
- \alpha\mathbb E[\mathbf1_{\mathcal F^c}HH^T]
- \preceq\alpha\Gamma.                                     \tag{13}
+ |\mathcal K_{n,ab}(u,k)|
+ \le\sqrt{\mathcal K_{n,aa}(u,u)\mathcal K_{n,bb}(k,k)}
+ \le G_T^2,\quad
+ G_T^2:=L^2+(\beta^2+m^2B_T^2)R_T^2.                     \tag{19}
 \]
 
-The top version of the same integration-by-parts calculation gives
-\(D\Gamma D^T\preceq\Sigma\). Define, only on their ranges,
+This is a gradient bound along the whole raw segment. No uniform
+Hessian or sign of the mixed kernel is needed. Integration gives
 
 \[
- \|x\|_V=\|V^{\dagger/2}x\|_2,
- \qquad x\in\operatorname{Ran}V.                           \tag{14}
+ |f_{n,k+1,a}-f_{n,ka}|
+       \le hG_T^2\sum_b|c_{n,kb}|.                      \tag{20}
 \]
 
-These are ordinary finite-dimensional weighted Euclidean norms.
-The inequalities imply the range inclusions for \(S,D\), and
+The passage to the population is joint. For each fixed \(u\), append
+reevaluations at \(\theta_k(u)\) to the finite graph. Unrolling the
+interpolated trained matrix produces finitely many additional queries
+of the same checked type. The scalar law therefore identifies jointly
+both endpoint predictions, the residuals, and every contraction in
+(18). Passing directly in (20) already proves its population version.
+
+One can also pass the integrated identity: the deterministic limiting
+segment contractions \(\mathcal K_{ab}(u,k)\) are continuous in \(u\)
+by finite Gaussian coupling and dominated convergence. For every fixed
+\(u\), the empirical contraction converges in probability. Bound (19)
+on an event of probability tending to one gives a common integrable
+bound. Apply bounded convergence to expected truncated differences
+on that event, then Fubini and Markov; the integral of the differences
+tends to zero in probability. Its complement has vanishing probability.
+This proves
 
 \[
- \|S\|_{\Sigma\to\Gamma}\le\sqrt\alpha,\quad
- \|D\|_{\Gamma\to\Sigma}\le1,\quad
- \max\{\|(I-DS)^{-1}\|_{\Sigma\to\Sigma},
- \|(I-SD)^{-1}\|_{\Gamma\to\Gamma}\}
-       \le\frac1{1-\sqrt\alpha}.                          \tag{15}
+ f_{k+1,a}-f_{ka}
+   =h\int_0^1\sum_b c_{kb}\mathcal K_{ab}(u,k)\,du,\qquad
+ |\mathcal K_{ab}(u,k)|\le G_T^2.                        \tag{21}
 \]
 
-For example, covariance domination annihilates every destination kernel
-vector, giving range inclusion; conjugation by the square roots then
-gives the norm bounds. The inverse bound is the convergent geometric
-series. It is independent of mesh and node count. This argument controls
-the expected derivatives in (5), not mean squares of pathwise
-derivatives, derivatives of coefficient selection, or the full product
-\((D+M_B)(S+M_A)\).
-
-## 5. Exact covariance supports in the attained program
+This is an empirical-average limit for a fixed finite graph, not a
+limit uniform in a growing number of raw training steps.
 
-For every \(N\ge1\) and \(\lambda>0\),
+Using exchange symmetry now gives
 
 \[
- \operatorname{Ran}\Gamma
-    =\{v:\ v_1=v_0\},\qquad
- \operatorname{Ran}\Sigma
-    =\{u:\ u_0=0\}.                                      \tag{16}
+ |f_{k+1,1}-f_{k1}|\le4hG_T^2|r_k|.                     \tag{22}
 \]
 
-Each time block has two coordinates. Later blocks on the right sides
-are unrestricted. At \(N=0\), \(\Gamma\) is positive definite and
-\(\Sigma=0\).
-
-To prove (16), put \(F=\phi_1(G)\) and \(K=\mathbb E[FF^T]\).
-Since the bivariate root has strictly positive density, every saturated
-sign quadrant has positive probability. A linear combination of \(F\)
-vanishing almost surely must vanish on all four such quadrants; hence
-\(K\) is positive definite. Startup gives exactly
+Since \(r_0=1\), for
 
 \[
- \delta^{(2)}_0=Q^{(1)}_0=0,\quad H^{(1)}_1=H^{(1)}_0=F,
- \quad \xi^{(2)}_0=\xi^{(2)}_1=X\sim N(0,K).
+ 0<h\le h_T:=\min\{T,(8G_T^2)^{-1}\},                    \tag{23}
 \]
 
-Let \(d(X)=\arctan X_1-\arctan X_2\), and define
+induction shows, at every node \(kh\le T\),
 
 \[
- g_a(X)=d(X)p(X_a),\qquad J=\mathbb E[gg^T].             \tag{17}
+ r_k\ge(1-4hG_T^2)^k\ge e^{-8G_T^2T}>0,\qquad
+ \lambda_k=2hr_k>0.                                    \tag{24}
 \]
 
-Then \(\delta^{(2)}_1=\lambda g\), and \(J\) is positive definite.
-Indeed \(d\ne0\) off the diagonal, and
-\(c_1p(x_1)+c_2p(x_2)\) cannot vanish on an open dense set unless
-\(c_1=c_2=0\). Use the full density of \(X\) and continuity.
+Here \(\log(1-x)\ge-2x\) for \(0\le x\le1/2\), as follows by
+differentiation. Also \(r_k\le1+LR_T\).
+The constants are independent of mesh and width. This is population
+residual positivity on sufficiently fine physical meshes, not
+finite-width pathwise sample antisymmetry.
 
-We now alternate two induction steps.
+## 6. Frozen mask and the corrected support conditions
 
-1. Suppose the reverse history through time \(k-1\) has no further
-   linear relation. Conditional on its past, \(\zeta^{(1)}_{k-1}\)
-   has a strictly positive definite Gaussian innovation. There is
-   positive probability that both first preactivations at time \(k-1\)
-   lie in \((-R,R)\): start with \(G\) in a smaller interior square,
-   and at each previous step choose the full-support source sufficiently
-   near the value making \(Q^{(1)}\) zero. Continuity and the finite
-   number of steps give a positive-probability neighborhood of these
-   choices. On that event, conditional on \(G\) and all earlier
-   reverse sources, the affine map from the new innovation to
-   \(Z^{(1)}_k\) has invertible linear part
-   \(\lambda C Y\operatorname{diag}(\psi(Z^{(1)}_{k-1}))\).
-   No nonzero linear combination of the two resulting \(\phi_1\)
-   coordinates can be constant on all of \(\mathbb R^2\). Thus no
-   new first-feature relation with the past is possible. The new
-   feature Gram Schur complement is positive definite.
+Let \(H\) stack \(H^{(1)}\),
+\(\mathcal F=\{|G_1|\ge R,\ |G_2|\ge R\}\), and
+\(\alpha=\Pr(\mathcal F^c)\le4R/\sqrt{2\pi}<1\).
+On \(\mathcal F\), both bottom gates stay zero for every formal reverse
+source. All first features equal \(\beta\operatorname{sign}(G_a)\)
+at every node. The candidate's first-program mapping is exact using
+its nonnegative step parameter \(h\) and its coefficient \(c_{kb}\)
+equal to the selected physical residual. Alternatively use
+\(\lambda_k,y_b\) when (24) holds. Zero or negative residuals do not
+obstruct the first mapping or the mask proof.
 
-2. The resulting forward-source innovation at time \(k\ge2\) is
-   positive definite. Conditional on earlier top sources,
-   \(\mathsf W_k\) is fixed and \(Z^{(2)}_k\) has full density.
-   Moreover \(\mathsf W_k\ne0\) almost surely. For \(k=1,2\) it is
-   respectively \(\lambda d\) and \(2\lambda d\). For later times,
-   condition one step earlier: the newest arctan difference is strictly
-   increasing in its first source coordinate, so its sum with the old
-   readout equals zero on a set of conditional measure zero. Since
-   \(c_1p(z_1)+c_2p(z_2)\) is nonconstant for every nonzero \(c\),
-   the current \(\delta^{(2)}_k\) has no linear relation with its
-   past. Its new Gram Schur complement is positive definite.
+Write \(\zeta^{(1)}=\Sigma^{1/2}Z\) with \(Z\) independent of \(G\).
+Polynomial derivative bounds justify Gaussian integration by parts.
+The frozen contribution to \(\mathbb E[Z(v^TH)]\) is zero, and for
+unit \(u\) masked Cauchy--Schwarz gives
+\(|\mathbb E[\mathbf1_{\mathcal F^c}(u^TZ)(v^TH)]|^2
+ \le\alpha\mathbb E[\mathbf1_{\mathcal F^c}(v^TH)^2]\).
+Thus
 
-The base for the first step is \(\Sigma_{11}=\lambda^2J>0\).
-This proves that the reduced feature list
-\((H^{(1)}_0,H^{(1)}_2,\ldots,H^{(1)}_N)\) and reduced backward list
-\((\delta^{(2)}_1,\ldots,\delta^{(2)}_N)\) have positive definite
-uncentered Grams, proving (16).
+\[
+ S\Sigma S^T\preceq
+ \alpha\mathbb E[\mathbf1_{\mathcal F^c}HH^T]\preceq\alpha\Gamma,
+ \qquad D\Gamma D^T\preceq\Sigma.                        \tag{25}
+\]
 
-Now \((M_Au)_0=0\) and
-\((M_Au)_1=\lambda\Gamma_{10}Yu_0=0\) for every supported \(u\).
-Also \((M_Bv)_0=0\) for every \(v\). Therefore
+The top inequality uses the same unmasked Gaussian argument.
+On \(\operatorname{Ran}V\), use the ordinary weighted Euclidean norm
+\(\|x\|_V=\|V^{\dagger/2}x\|_2\). Kernel annihilation and square-root
+conjugation give the supported response bounds and geometric-series
+inverse bounds
 
 \[
- M_A\operatorname{Ran}\Sigma\subseteq\operatorname{Ran}\Gamma,
- \qquad
- M_B\operatorname{Ran}\Gamma\subseteq\operatorname{Ran}\Sigma.
-                                                                  \tag{18}
+ \|S\|_{\Sigma\to\Gamma}\le\sqrt\alpha,\quad
+ \|D\|_{\Gamma\to\Sigma}\le1,\quad
+ \max\{\|(I-DS)^{-1}\|_\Sigma,\|(I-SD)^{-1}\|_\Gamma\}
+       \le(1-\sqrt\alpha)^{-1}.                         \tag{26}
 \]
 
-There is consequently no finite-program support counterexample in this
-interior-correlation family. This conclusion uses the actual activation,
-startup, and source innovations; it does not follow from (13) alone.
+These statements do not bound mean-square pathwise sensitivities or
+the derivative of statistical selection.
+
+For the full-support formula at \(N\ge2\), a sufficient condition is
 
-## 6. Uniform ordinary-output estimates; the stronger question
+\[
+ \lambda_0,\ldots,\lambda_{N-1}\ne0,\qquad
+ \lambda_0+\lambda_1\ne0.                               \tag{27}
+\]
 
-Put \(t_k=\lambda k\), \(f_i=\sqrt{\Gamma_{ii}}\le\beta\),
-\(d_i=\sqrt{\Sigma_{ii}}\le\pi t_k\), and
+For \(N=1\), only \(\lambda_0\ne0\) is needed. Under (27),
 
 \[
- s_k=\lambda\sum_{r<k,b}f_{rb}d_{rb}
-     \le\pi\beta\lambda^2 k(k-1)\le\pi\beta t_k^2.       \tag{19}
+ \operatorname{Ran}\Gamma=\{v:v_1=v_0\},\qquad
+ \operatorname{Ran}\Sigma=\{u:u_0=0\}.                   \tag{28}
 \]
 
-For supported inputs, covariance Cauchy--Schwarz gives
-\(|u_j|\le d_j\|u\|_\Sigma\),
-\(|v_j|\le f_j\|v\|_\Gamma\), and hence the full actual memory bounds
+In particular this holds on every sufficiently fine physical mesh by
+(24), but not on an arbitrary physical mesh.
+
+For the proof let \(F=\phi_1(G)\), \(K=\mathbb E[FF^T]>0\).
+Every saturated sign quadrant has positive probability, proving
+strict positivity. Population startup gives
+\(H^{(1)}_1=H^{(1)}_0=F\) and \(\xi^{(2)}_0=\xi^{(2)}_1=X\sim N(0,K)\).
+Set
 
 \[
- |(M_Au)_i|\le f_i s_k\|u\|_\Sigma,\qquad
- |(M_Bv)_i|\le d_i s_k\|v\|_\Gamma.                      \tag{20}
+ d(X)=\arctan X_1-\arctan X_2,\quad
+ g_a=d(X)p(X_a),\qquad J=\mathbb E[gg^T]>0.               \tag{29}
 \]
 
-Combining them with the strict gap gives
+The last positivity follows since \(d\ne0\) off the diagonal and
+\(c_1p(x_1)+c_2p(x_2)\) cannot vanish on an open dense set unless
+\(c=0\). Hence \(\delta^{(2)}_1=\lambda_0g\) has positive Gram.
+
+Alternate two induction steps. A positive reverse-source innovation at
+time \(k-1\) enters \(Z^{(1)}_k\) with coefficient
+\(\lambda_{k-1}CY\operatorname{diag}(\psi(Z^{(1)}_{k-1}))\).
+Both gates are positive on an event of positive probability: start
+inside the bump and choose each previous full-support source near the
+value making its reverse answer zero. Continuity supplies a neighborhood
+of positive probability for this finite sequence. On that event the
+coefficient is invertible. No nonzero combination of the two resulting
+\(\phi_1\) outputs is constant on all of \(\mathbb R^2\), excluding
+a new feature relation and giving a positive forward innovation.
+
+Conditional on past top sources, the new top preactivation has full
+density. Its readout is nonzero almost surely: at times one and two it
+is \(\lambda_0d\) and \((\lambda_0+\lambda_1)d\); later the newest
+arctan difference has nonzero coefficient \(\lambda_{k-1}\) and is
+strictly monotone in one source coordinate. Fubini excludes zero
+readout with positive probability. Nonconstancy of
+\(c_1p(z_1)+c_2p(z_2)\) then excludes a new backward relation.
+This proves (28).
+
+The extra condition in (27) matters. Section 8 gives \(v_0>0\) and
+\(f_{11}=\lambda_0v_0\). At coarse physical \(h=1/v_0\),
+\(\lambda_0=2/v_0,\ \lambda_1=-\lambda_0\), both nonzero, but
+\(\mathsf W_2=\delta^{(2)}_2=0\). At \(h=1/(2v_0)\), instead,
+\(f_{11}=1,\lambda_1=0\); the symmetric population has zero residual
+and stops. Both create further history relations. Neither is asserted
+to produce memory support leakage.
+
+Under (27), for a supported \(u\),
+\((M_Au)_0=(M_Au)_1=0\), since \(u_0=0\); and
+\((M_Bv)_0=0\) for every \(v\). Thus both full learned memories
+preserve the supports in (28). This support conclusion is made under
+(27), including the sufficiently fine physical meshes (23).
+A generic matrix warning is not an attained counterexample here.
+
+## 7. Uniform ordinary-output bounds in physical time
+
+For any finite selected coefficients define
+\(a_k=\sum_{r<k}|\lambda_r|\),
+\(f_i^\circ=\sqrt{\Gamma_{ii}}\le\beta\), and
+\(d_i^\circ=\sqrt{\Sigma_{ii}}\le\pi a_k\).
+The coefficient total \(a_k\) is used in an estimate; it is not a
+reparametrized trajectory. Then
 
 \[
- |(Au)_i|\le f_i(\sqrt\alpha+s_k)\|u\|_\Sigma,\qquad
- |(Bv)_i|\le d_i(1+s_k)\|v\|_\Gamma.                     \tag{21}
+ s_k=\sum_{r<k,b}|\lambda_r|f_{rb}^\circ d_{rb}^\circ
+ \le2\pi\beta\sum_{r<k}|\lambda_r|a_r\le\pi\beta a_k^2.    \tag{30}
 \]
 
-For \(T=\lambda N\) and
-\(\|z\|_{\lambda,2}^2=\lambda\sum_{k,a}|z_{ka}|^2\), for example,
+Covariance Cauchy--Schwarz gives, on supported inputs,
 
 \[
- \|M_Au\|_{\lambda,2}
- \le\pi\beta^2 T^2\sqrt{2(T+\lambda)}\|u\|_\Sigma,
+ |(M_Au)_i|\le f_i^\circ s_k\|u\|_\Sigma,\quad
+ |(M_Bv)_i|\le d_i^\circ s_k\|v\|_\Gamma,
 \]
 \[
- \|M_Bv\|_{\lambda,2}
- \le\pi^2\beta T^3\sqrt{2(T+\lambda)}\|v\|_\Gamma.       \tag{22}
+ |(Au)_i|\le f_i^\circ(\sqrt\alpha+s_k)\|u\|_\Sigma,\quad
+ |(Bv)_i|\le d_i^\circ(1+s_k)\|v\|_\Gamma.                \tag{31}
 \]
-
-These constants are uniform along \(\lambda=T/N\), \(N\ge1\).
-The outputs include every coordinate; there is no projection discarding
-an output component. Equivalently, applying the row estimates to the
-actual random query inputs gives
-
 \[
- \|(M_A\delta^{(2)})_i\|_{L^2}\le f_i s_k,\quad
- \|(M_BH^{(1)})_i\|_{L^2}\le d_i s_k,
+ \|Z^{(2)}_i\|_{L^2}\le f_i^\circ(1+\sqrt\alpha+s_k),\quad
+ \|Q^{(1)}_i\|_{L^2}\le d_i^\circ(2+s_k).                 \tag{32}
 \]
+
+On physical \(T=Nh\), (4), (11)--(12) imply
+\(a_N\le A_T:=2T(1+LR_T)\). For the ordinary output norm
+\(\|z\|_{h,2}^2=h\sum_{k,a}|z_{ka}|^2\), for example,
+
 \[
- \|Z^{(2)}_i\|_{L^2}\le f_i(1+\sqrt\alpha+s_k),\qquad
- \|Q^{(1)}_i\|_{L^2}\le d_i(2+s_k).                      \tag{23}
+ \|M_Au\|_{h,2}\le\pi\beta^2A_T^2\sqrt{2(T+h)}\|u\|_\Sigma,\quad
+ \|M_Bv\|_{h,2}\le\pi^2\beta A_T^3\sqrt{2(T+h)}\|v\|_\Gamma.
+                                                                  \tag{33}
 \]
 
-The covariance-norm question is stronger. Its exact necessary and
-sufficient formulation is the existence, for every fixed horizon,
-of finite constants independent of mesh such that
+These are physical-mesh bounds, not relabeled constant-feature-time
+bounds. The stronger missing covariance-output inequalities remain
 
 \[
  M_A\Sigma M_A^T\preceq C_A(T)^2\Gamma,\qquad
- M_B\Gamma M_B^T\preceq C_B(T)^2\Sigma.                  \tag{24}
+ M_B\Gamma M_B^T\preceq C_B(T)^2\Sigma                    \tag{34}
 \]
 
-Support preservation proves finiteness at each fixed finite mesh.
-It supplies no uniform lower bound on the reduced Gram Schur
-complements. Neither (13) nor (20)--(23) proves (24). In particular,
-the powers of \(T\) in (22) cannot be carried over to covariance
-output norms. The next calculation gives an actual obstruction to
-precisely that small-time inference.
+uniformly over fine physical meshes. Support preservation makes them
+finite at each fixed admissible mesh, but does not supply uniform
+constants. The obstruction below excludes smallness, not a larger
+finite bound.
 
-## 7. Exact two-update memory norms and their small-step limits
+## 8. Actual physical two-update coefficients and Schur transfer
 
-Keep any \(-1<\rho<1\), and use only the actual prefix \(0,1,2\).
-Keep \(F,K,X,d,g,J\) from (17). Define the deterministic matrices
+Keep any interior \(\rho\) and \(F,K,X,d,g,J\) from (29).
+Exchange symmetry and strict monotonicity of arctan give
 
 \[
- P_{ab}=\mathbb E[p(X_a)p(X_b)],\quad
- t_a=\mathbb E[d(X)p'(X_a)],\quad T_0=PY+\operatorname{diag}(t),
-\]
-\[
- J^{(1)}_{ab}=C_{ab}\mathbb E[\psi(G_a)\psi(G_b)].         \tag{25}
+ v_0:=\mathbb E[d(X)\arctan X_1]
+        =\tfrac12\mathbb E[d(X)^2]>0.                    \tag{35}
 \]
 
-The exact first-return blocks, including the readout derivative and
-the current block, are
+The first population prediction is zero. For \(\lambda=2h\),
+the exact physical values are
 
 \[
- B_{10}=D_{10}=\lambda PY,\qquad
- B_{11}=D_{11}=\lambda\operatorname{diag}(t).
+ \lambda_0=\lambda,\quad \mathsf W_1=\lambda d,\quad
+ f_{11}=\lambda v_0,\quad f_{12}=-\lambda v_0,\quad
+ \mu:=\lambda_1=\lambda(1-\lambda v_0),
+\]
+\[
+ s:=\lambda+\mu=2\lambda-\lambda^2v_0,\quad
+ q_\lambda:=s/\lambda=2-\lambda v_0,\quad \tau:=\lambda\mu.
+                                                                  \tag{36}
 \]
 
-The learned reverse term on these blocks vanishes because
-\(\delta^{(2)}_0=0\). With \(V\sim N(0,J)\) independent of \(G\),
+For sufficiently small \(h>0\), both coefficients are positive.
+Define the fixed startup matrices
 
 \[
- Q^{(1)}_1=\lambda(V+T_0F),\qquad
- Z^{(1)}_2=G+\lambda^2 C Y\operatorname{diag}(\psi(G))(V+T_0F).
-                                                                  \tag{26}
+ P_{ab}=\mathbb E[p(X_a)p(X_b)],\quad
+ t_a=\mathbb E[d(X)p'(X_a)],\quad T_0=PY+\operatorname{diag}(t),\quad
+ J^{(1)}_{ab}=C_{ab}\mathbb E[\psi(G_a)\psi(G_b)].          \tag{37}
 \]
 
-Introduce the actual leading first-feature increment
+The full first-return blocks are
+\(B_{10}=D_{10}=\lambda PY\) and
+\(B_{11}=D_{11}=\lambda\operatorname{diag}(t)\).
+Their learned term vanishes since population \(\delta^{(2)}_0=0\).
+Selection of \(\lambda_1\) adds no formal source derivative.
+For \(V\sim N(0,J)\) independent of \(G\),
 
 \[
- L^{(1)}=\operatorname{diag}(\psi(G))C Y
-               \operatorname{diag}(\psi(G))(V+T_0F).
+ Q^{(1)}_1=\lambda(V+T_0F),\qquad
+ Z^{(1)}_2=G+\tau CY\operatorname{diag}(\psi(G))(V+T_0F).
+                                                                  \tag{38}
 \]
 
-Taylor's formula and bounded derivatives give, in every finite \(L^p\),
+Let
+\(L^{(1)}=\operatorname{diag}(\psi(G))CY
+\operatorname{diag}(\psi(G))(V+T_0F)\).
+Taylor expansion with bounded derivatives proves, in every finite \(L^p\),
 
 \[
- H^{(1)}_2=F+\lambda^2L^{(1)}+O_{L^p}(\lambda^4).         \tag{27}
+ H^{(1)}_2=F+\tau L^{(1)}+O_{L^p}(\tau^2)
+ =F+\lambda^2L^{(1)}-\lambda^3v_0L^{(1)}
+                                      +O_{L^p}(\lambda^4).        \tag{39}
 \]
 
-Let \((X,E)\) be the centered Gaussian pair whose covariance blocks
-are the uncentered Gram blocks of \((F,L^{(1)})\). This is the limit
-of the *actual scaled source increment*
-\((\xi^{(2)}_0,(\xi^{(2)}_2-\xi^{(2)}_0)/\lambda^2)\), not a new
-initialization. Gaussian regression and square-root coupling give
-convergence in every finite \(L^p\). Its conditional innovation
-covariance is
+Thus the leading increment agrees with the auxiliary one; the next
+term is explicitly different.
+
+Let \((X,E)\) be centered Gaussian with covariance blocks the
+uncentered Gram blocks of \((F,L^{(1)})\). Equation (39) and Gaussian
+regression/square-root coupling show convergence in every finite \(L^p\)
+of the actual pair
+\((\xi^{(2)}_0,(\xi^{(2)}_2-\xi^{(2)}_0)/\tau)\) to \((X,E)\).
+The root \(X\) can be held fixed. Its conditional innovation covariance is
 
 \[
  V_1=\mathbb E[L^{(1)}(L^{(1)})^T]
-       -\mathbb E[L^{(1)}F^T]K^{-1}\mathbb E[F(L^{(1)})^T]>0.       \tag{28}
+       -\mathbb E[L^{(1)}F^T]K^{-1}\mathbb E[F(L^{(1)})^T]>0.
+                                                                  \tag{40}
 \]
 
-Strict positivity follows already from the \(V\)-dependent term on
-the event where both root gates are positive: \(J,C\) and both gates
-are nonsingular there. A function of \(F\) cannot cancel that
-independent conditional variation.
+On the event of two positive root gates, the coefficient of the
+independent \(V\) in \(L^{(1)}\) is invertible. Since \(J>0\),
+no function of \(F\) removes that variation, proving strict positivity.
+This scaled-source limit introduces no new initialization.
 
-Equation (6) gives
-\(S_{21}=\lambda J^{(1)}Y+O(\lambda^3)\). Thus, retaining both
-pieces of \(A_{21}\),
+Differentiating (38) with respect to the formal \(\zeta^{(1)}_1\)
+gives \(S_{21}=\mu J^{(1)}Y+O(\mu\tau)\).
+Since \(\Gamma_{21}=K+O(\tau)\),
+\(A_{21}=\mu(J^{(1)}+K)Y+O(\mu\tau)\).
+Using \(\delta^{(2)}_1=\lambda g\) and the zero population time-zero
+backward input,
 
 \[
- A_{21}=\lambda(J^{(1)}+K)Y+O(\lambda^3),\qquad
- Z^{(2)}_2=X+\lambda^2U+o_{L^p}(\lambda^2),
-\]
-\[
- U=E+(J^{(1)}+K)Yg.
+ Z^{(2)}_2=X+\tau U+o_{L^p}(\tau),\qquad
+ U=E+(J^{(1)}+K)Yg.                                    \tag{41}
 \]
 
-Since \(\mathsf W_2=2\lambda d\) exactly, define
+Both pieces of the complete forward coefficient are retained.
+
+The first two top feature pairs are both \(\arctan X\), so
+\(\mathsf W_2=s d\) exactly. Put \(L^{(2)}_a=d(X)p'(X_a)U_a\).
+Bounded derivatives of \(p\) and finite moments in (41) give
 
 \[
- L^{(2)}_a=d(X)p'(X_a)U_a.
+ \delta^{(2)}_2=s g+s\tau L^{(2)}+o_{L^p}(s\tau),
 \]
-
-Then
-
 \[
- \delta^{(2)}_2=2\lambda g+2\lambda^3L^{(2)}
-                         +o_{L^p}(\lambda^3).            \tag{29}
+ \delta^{(2)}_2-q_\lambda\delta^{(2)}_1
+       =s\tau L^{(2)}+o_{L^p}(\lambda^3),\qquad
+ \frac{\delta^{(2)}_2-q_\lambda\delta^{(2)}_1}{\lambda^3}
+                        \longrightarrow 2L^{(2)}.       \tag{42}
 \]
 
+Indeed \(s\tau/\lambda^3\to2\). Subtracting only
+\(2\delta^{(2)}_1\) leaves the larger predictable term
+\(-\lambda^2v_0g\). Equation (42) proves the required physical
+innovation transfer instead of assuming cancellation.
+
 Also
 
 \[
  V_2=\mathbb E[L^{(2)}(L^{(2)})^T]
-       -\mathbb E[L^{(2)}g^T]J^{-1}\mathbb E[g(L^{(2)})^T]>0.       \tag{30}
+       -\mathbb E[L^{(2)}g^T]J^{-1}\mathbb E[g(L^{(2)})^T]>0.
+                                                                  \tag{43}
 \]
 
-Indeed, condition on \(X\). The conditional covariance contributed
-by \(E\) is
-\(\operatorname{diag}(d p'(X))V_1\operatorname{diag}(d p'(X))\),
-which is positive definite almost surely, since \(d\ne0\) and
-\(X_a\ne0\) almost surely. Subtracting a linear function of \(g(X)\)
-cannot remove it.
-
-Here is also an exact, nonasymptotic expression for the two memory
-norms. Write \(\Gamma_{21}=\mathbb E[H^{(1)}_2F^T]\),
-\(\Sigma_{21}=\mathbb E[\delta^{(2)}_2(\delta^{(2)}_1)^T]\), and
+Conditional on \(X\), the covariance from \(E\) is
+\(\operatorname{diag}(dp'(X))V_1\operatorname{diag}(dp'(X))\).
+It is positive definite almost surely since \(d\ne0\) and \(X_a\ne0\)
+almost surely. Subtracting a linear function of \(g(X)\) cannot remove it.
+
+Let
+\(V_{1,h}=\Gamma_{22}-\Gamma_{21}K^{-1}\Gamma_{12}\) and
+\(V_{2,h}=\Sigma_{22}-\Sigma_{21}(\lambda^2J)^{-1}\Sigma_{12}\).
+These are positive for small \(h>0\).
+The exact supported-input actions are
+\((M_Au)_2=\mu\Gamma_{21}Yu_1\) and
+\((M_Bv)_2=\mu\Sigma_{21}Yv_1\), with earlier output blocks zero.
+Block inversion yields
 
 \[
- V_{1,\lambda}=\Gamma_{22}-\Gamma_{21}K^{-1}\Gamma_{12},\qquad
- V_{2,\lambda}=\Sigma_{22}
-                  -\Sigma_{21}(\lambda^2J)^{-1}\Sigma_{12}.
+ \|M_A\|_{\Sigma\to\Gamma}
+  =|\mu|\lambda\|V_{1,h}^{-1/2}\Gamma_{21}YJ^{1/2}\|_{\rm op},\quad
+ \|M_B\|_{\Gamma\to\Sigma}
+  =|\mu|\|V_{2,h}^{-1/2}\Sigma_{21}YK^{1/2}\|_{\rm op}.     \tag{44}
 \]
 
-Both are positive definite by Section 5. The only nonzero action of
-\(M_A\) on supported inputs is
-\((M_Au)_2=\lambda\Gamma_{21}Yu_1\); that of \(M_B\) is
-\((M_Bv)_2=\lambda\Sigma_{21}Yv_1\). Block inversion therefore gives
+Prescribing \(u_1\) has minimum supported-extension cost
+\(u_1^T(\lambda^2J)^{-1}u_1\); prescribe the later input block by
+covariance regression. The analogous cost for \(v_1\) uses \(K\).
+A zero first output block is measured by the inverse destination Schur
+complement. Thus (44) optimizes over attainable supported directions.
+
+A Schur complement of \((a,b)\) is unchanged on replacing \(b\)
+by \(b-La\), for deterministic \(L\): expanding its two
+second-moment terms cancels all terms involving \(L\).
+Applying this with \(L=q_\lambda I\) and (42) proves
 
 \[
- \|M_A\|_{\Sigma\to\Gamma}
-   =\lambda^2\|V_{1,\lambda}^{-1/2}\Gamma_{21}YJ^{1/2}\|_{\rm op},
-\]
-\[
- \|M_B\|_{\Gamma\to\Sigma}
-   =\lambda\|V_{2,\lambda}^{-1/2}\Sigma_{21}YK^{1/2}\|_{\rm op}.
-                                                                  \tag{31}
+ V_{1,h}/\tau^2\to V_1,\quad V_{2,h}/(s\tau)^2\to V_2,\quad
+ \Gamma_{21}\to K,\quad \Sigma_{21}/(s\lambda)\to J.
+                                                                  \tag{45}
 \]
 
-For clarity about support and optimization: after deleting the repeated
-feature block, an output with first block zero has covariance norm
-given by the inverse Schur complement. For a prescribed input block
-\(u_1\), its minimum-norm supported extension has squared norm
-\(u_1^T(\lambda^2J)^{-1}u_1\); the later block is its covariance
-regression extension. The analogous assertion for \(v_1\) uses \(K\).
-Thus (31) optimizes over actually supported vectors, with the correct
-cost of their later components.
-
-Equations (27)--(30) give
-\(V_{1,\lambda}/\lambda^4\to V_1\),
-\(V_{2,\lambda}/(4\lambda^6)\to V_2\),
-\(\Gamma_{21}\to K\), and \(\Sigma_{21}/(2\lambda^2)\to J\).
-Consequently
+In particular \(V_{2,h}/(4\lambda^6)\to V_2\).
+Positive definiteness permits inverse-square-root limits. Since
+\(\tau=\lambda\mu\), (44)--(45) give
 
 \[
- \boxed{
- \begin{aligned}
+ \boxed{\begin{aligned}
  \|M_A\|_{\Sigma\to\Gamma}
-    &\longrightarrow\|V_1^{-1/2}KYJ^{1/2}\|_{\rm op}\in(0,\infty),\\
+   &\to\|V_1^{-1/2}KYJ^{1/2}\|_{\rm op}\in(0,\infty),\\
  \|M_B\|_{\Gamma\to\Sigma}
-    &\longrightarrow\|V_2^{-1/2}JYK^{1/2}\|_{\rm op}\in(0,\infty).
- \end{aligned}}                                                 \tag{32}
+   &\to\|V_2^{-1/2}JYK^{1/2}\|_{\rm op}\in(0,\infty).
+ \end{aligned}}                                                  \tag{46}
 \]
 
-This supplies new actual learned-memory estimates without pretending
-that small matrix entries imply small covariance-norm operators.
+The constants agree with the auxiliary calculation for the proved
+asymptotic reason above, not because its clock equals physical time.
 
-## 8. A quantitative attained obstruction at rho = 0
+## 9. Quantitative physical-prefix obstruction at rho = 0
 
-We now prove (A), with conservative constants and no numerical
-experiment. Set \(\rho=0\). Then \(G_1,G_2\) are independent,
+We now prove (C2), using the physical leading fields of Section 8,
+with conservative constants and no numerical experiment. Set \(\rho=0\).
+Then \(G_1,G_2\) are independent,
 \(K=kI\), and \(X_1,X_2\) are independent \(N(0,k)\). Put
 
 \[
@@ -714,7 +842,7 @@
 \[
  0<k\le\beta^2<\frac1{100},\qquad
  k\ge(1-p_0)\beta^2>\frac45\beta^2,
- \qquad b:=a+k<\frac1{25}.                               \tag{33}
+ \qquad b:=a+k<\frac1{25}.                               \tag{47}
 \]
 
 Here \(J^{(1)}=aI\) and \(U=E+bYg\). Let
@@ -733,10 +861,10 @@
 For the first term use the independent, centered arctan remainders;
 for the second use
 \(\mathbb E[(X_1-X_2)^2(X_1^2+X_2^2)^2]=48k^3\).
-Since \(\|\sqrt2(X_1-X_2)\|_2=2\sqrt{k}\), (33) implies
+Since \(\|\sqrt2(X_1-X_2)\|_2=2\sqrt{k}\), (47) implies
 
 \[
- j_+>\left(\frac{19}{10}\right)^2k=\frac{361}{100}k.       \tag{34}
+ j_+>\left(\frac{19}{10}\right)^2k=\frac{361}{100}k.       \tag{48}
 \]
 
 Next bound the second moment of the actual first-feature increment.
@@ -761,7 +889,7 @@
  \operatorname{tr}\operatorname{Cov}(E)
    =\mathbb E|L^{(1)}|^2
    \le2q_4(3k+\beta^2)
-   \le\frac{17}{2}q_4k<\frac{17}{500}k.                  \tag{35}
+   \le\frac{17}{2}q_4k<\frac{17}{500}k.                  \tag{49}
 \]
 
 Write \(e_+^TL^{(2)}\) as its \(E\) part and its \(bYg\) part.
@@ -777,7 +905,7 @@
 
 \[
  \mathbb E[(X_1-X_2)^2|X|^2|E|^2]
- \le36k^2\mathbb E|E|^2.                                \tag{36}
+ \le36k^2\mathbb E|E|^2.                                \tag{50}
 \]
 
 Here is a direct verification, so no Gaussian moment theorem is being
@@ -790,9 +918,9 @@
 \(36k^2,12k^2,8k^2\); cross terms vanish by parity. These values
 use only \(\mathbb E X_-^2=k\), \(\mathbb E X_-^4=3k^2\), and
 \(\mathbb E X_-^6=15k^3\), obtained by Gaussian integration by parts.
-Summing proves (36).
+Summing proves (50).
 
-By (35)--(36), the \(E\) part has \(L^2\) norm at most
+By (49)--(50), the \(E\) part has \(L^2\) norm at most
 \(\sqrt{306/125}\,k^{3/2}\). For the other part, the scalar function
 \(p'p=-2x/(1+x^2)^3\) has derivative of absolute value at most two.
 Indeed its derivative is \((-2+10x^2)/(1+x^2)^4\); the stated bound
@@ -811,72 +939,74 @@
 \[
  \|e_+^TL^{(2)}\|_{L^2}
  <\left(\sqrt{306/125}+\frac{\sqrt{240}}{25}\right)k^{3/2}
- <\frac{11}{5}k^{3/2}.                                  \tag{37}
+ <\frac{11}{5}k^{3/2}.                                  \tag{51}
 \]
 
-Finally, (30) gives
+Finally, (43) gives
 \(e_+^TV_2e_+\le\mathbb E(e_+^TL^{(2)})^2\), whereas
-\(e_+^TJYKYJe_+=k j_+^2\). Testing the matrix norm in (32) in this
-destination direction and using (34)--(37) yields
+\(e_+^TJYKYJe_+=k j_+^2\). Testing the matrix norm in (46) in this
+destination direction and using (48)--(51) yields
 
 \[
  \|V_2^{-1/2}JYK^{1/2}\|_{\rm op}
  \ge\frac{j_+\sqrt{k}}{\|e_+^TL^{(2)}\|_{L^2}}
- >\frac{361/100}{11/5}=\frac{361}{220}.                   \tag{38}
+ >\frac{361/100}{11/5}=\frac{361}{220}.                   \tag{52}
 \]
 
-This proves (A). In particular, for each fixed allowed \(R\),
+Together with the physical limit (46), this proves (C2).
+In particular, for each fixed allowed \(R\),
 \(\|M_B\|_{\Gamma\to\Sigma}>8/5\) at all sufficiently small
-positive steps on this attained two-update prefix. All directions used
-in (31) and (38) have covariance-supported extensions; no independent
+positive physical steps \(h\) on this attained two-update prefix.
+All directions used
+in (44) and (52) have covariance-supported extensions; no independent
 choice of an impossible time slot is used.
 
-The obstruction also persists inside any fixed-horizon refinement.
-For a longer actual history, test the matrix inequality
-\(M_B\Gamma M_B^T\preceq c^2\Sigma\) on vectors supported in the
-first three time blocks. Causality makes this exactly the corresponding
-inequality for the attained two-update prefix. Therefore the full-history
-memory norm is at least its prefix norm. In particular, for every fixed
-\(T>0\), at \(\rho=0\),
+
+## 10. Physical fixed-horizon consequence and claim status
+
+For each fixed \(R\), (46), (52) imply that the actual physical-prefix
+norm exceeds \(8/5\) at sufficiently small \(h>0\). Its physical horizon
+is \(2h\), not \(2\lambda\).
+
+The full-horizon inference now has a physical bridge. For \(h=T/N\)
+and all sufficiently large \(N\), (23)--(28) ensure positive residuals
+and memory support preservation in the whole physical population history.
+Test the full memory covariance inequality on destination vectors
+supported in times \(0,1,2\). Causality makes it exactly the physical
+prefix inequality (44). The whole-history memory norm is at least the
+prefix norm. Consequently, at \(\rho=0\),
 
 \[
- \liminf_{N\to\infty,\ \lambda=T/N}
+ \liminf_{N\to\infty,\ h=T/N}
  \|M_B^{[0:N]}\|_{\Gamma^{[0:N]}\to\Sigma^{[0:N]}}
- >\frac{361}{220}.                                      \tag{39}
+ \ge\|V_2^{-1/2}JYK^{1/2}\|_{\rm op}>\frac{361}{220}.       \tag{53}
 \]
 
-The strict inequality follows because the prefix norms converge to the
-fixed limit in (38), which is strictly larger than the displayed bound.
-This excludes a mesh-uniform contraction constant for that memory; it
-does not exclude a larger finite mesh-uniform bound.
-
-The feature horizon here is \(2\lambda\downarrow0\). Thus any bound
-of the form \(\|M_B\|\le\varepsilon(T)\), uniform over prefixes
-with horizon at most \(T\), must have
-\(\liminf_{T\downarrow0}\varepsilon(T)\ge361/220\). It cannot be
-a perturbation estimate tending to zero. This does not refute a finite,
-non-small bound in (24), or a different argument controlling the full
-feedback product while retaining cancellation between its terms.
+This step uses the raw-segment positivity proof; it is not a relabeling
+of a constant-feature-time trajectory. It excludes a contraction bound
+for this memory and a bound tending to zero on short physical horizons.
+It does not prove divergence, exclude larger finite bounds in (34),
+or determine cancellation in the full feedback product.
 
-## 9. Research-state update
+Every entry below remains **UNVERIFIED pending root review**.
+References identify supplied derivations, not promotion.
 
-| Claim | Result for the present canonical program |
+| Statement | Corrected scope / derivation |
 |---|---|
-| Correct first/root Gaussian independence and frozen derivative convention | Verified, with uncapped activation-transfer issue addressed in Section 3 |
-| Frozen-mask inequality \(S\Sigma S^T\preceq\alpha\Gamma\) | Proved uniformly in mesh, prefix, and interior correlation; stronger masked inequality retained |
-| Supported inverses for derivative-only \(DS,SD\) | Proved with bound \((1-\sqrt\alpha)^{-1}\) |
-| Actual memories preserve covariance supports | Proved for every finite positive mesh and every \(-1<\rho<1\) |
-| Generic/harmonic support warnings yield a counterexample here | They do not; the exact supports (16) exclude one |
-| Complete memory bounds with ordinary coordinate/time-weighted outputs | Proved uniformly on fixed horizons, (20)--(23) |
-| Actual two-update covariance memory norms | Exact formulas (31); finite positive small-step limits (32) |
-| Reverse memory is a contraction or vanishes on short horizons | Falsified by the attained \(\rho=0\) estimate (38) |
-| Finite covariance-norm upper bounds for both memories uniform over all meshes at a fixed horizon | Open here; exact missing inequalities are (24) |
-| Uniform bound for full feedback, pathwise sensitivity second moments, or cavity-trace time integrals | Not supplied by this result |
-| Full globalMF, continuum construction, or all-time raw-GD convergence | Not claimed |
-
-The candidate therefore closes a genuine derivative-only mesh-uniform
-gap in this activation family. For the actual learned terms, the next
-obligation is quantitative control of the reduced history Gram Schur
-complements in (24), with the non-small reverse-memory effect (38)
-retained. Support leakage is not that obligation in the present
-interior-correlation program.
+| Constant label forcing is canonical physical raw GD | Withdrawn; auxiliary fixed-feature-time only |
+| Exact finite zero readout | Withdrawn; contract iid \(N(0,n^{-2})\), fixed-program population restoration in Section 4 |
+| Physical residual coefficients | \(c=-2(f-y)\); exchange gives (4), with actual feedback included in identification |
+| Formal source responses | Freeze selected residuals; retain readout-history derivatives, (8)--(10) |
+| Frozen-mask gap | Same inequality for every finite physical program, including zero residuals, (25)--(26) |
+| Unconditional all-mesh support formula | Withdrawn; even nonzero coefficients can cancel the first two readout increments |
+| Correct support and memory support preservation | Condition (27), and all sufficiently fine physical meshes by (16)--(24) |
+| Physical two-update obstruction | Exact residual coefficients (36), deterministic Schur subtraction (42), limits (46), bound (52) |
+| Physical fixed-horizon lower bound | Requires and uses Sections 4--6; result (53) |
+| Uniform covariance-norm upper bounds for both memories | Open here; (34) is the missing stronger estimate |
+| Full feedback inverse / mean-square pathwise response | Not controlled here |
+| Simultaneous raw training limit along \(\eta=n^{-2}\), continuum flow, or globalMF | Not identified by these width-first fixed-program arguments |
+
+The old 882-line source is preserved for provenance. This revision
+repairs its clock and initialization scope and supplies the physical
+finite-program derivations required for the memory obstruction.
+It changes no metric, clock, or initialization in the contract.
```
