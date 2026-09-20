# Independent internal audit of the rotation obstruction

Date: 2026-09-18. Status: **PASS for the corrected, explicitly scoped theorem and consequences below.** This is an internal mathematical check, not a promotion review or approval.

## Input and isolation

The sole scientific input was the complete `rotation_obstruction.md` in this study. I read the required mathematical-proof and conjecture-audit skills and their applicable audit/contract guidance. I did not read the study README, other scientific files, other reports, prior verdicts, study history, or external scientific sources. No numerical experiments were performed.

Final reviewed input SHA256:

```text
c12e71ce324a4e995b2a7495b17c4fe25b861696f020ed72abbd4c29c7320400
```

The originally supplied input had SHA256:

```text
99ea3acb68af9b0db6a8ef2d1bd18101ce03a32b80a19e1df1abb7a483e6ea1f
```

During this review I reported a missing endpoint assumption in the potential corollary. The supervisor explicitly authorized review of its local correction and an added class-center calculation. I then reread the complete corrected input and checked both edits. The resolved defect is recorded below; this PASS applies to the final hash, not to the original potential statement as literally written.

The review takes the displayed model (3)--(4) as the prescribed dynamics. The derivation of that model from another population system, or its identification with the full canonical dictionary, is outside this input and is not validated here. No additional scientific input is needed for the theorem about the displayed model.

## Claim-specific verdicts

| Claim | Verdict and exact scope |
| --- | --- |
| Hilbert-space gradient identity and finite-time wellposedness | PASS. The displayed field is locally Lipschitz on bounded state balls, with uniform bounds over unit directions. The loss identity prevents finite-time escape and gives unique global forward solutions. |
| Finite-time dependence on the rotation angle | PASS. The stated estimates give a common finite-horizon ball and a Gronwall bound; no uniform infinite-time estimate is needed. |
| Antipodal covariance with fixed probes | PASS. Only the data directions and readout change sign in the transformed solution; the initialization is preserved. |
| One fixed initialized trajectory with loss at least one half for all time | PASS. The nested closed sets of angles are nonempty and compact; the quantifier passage is valid. |
| No initial stall for any rotation under the stated unequal positive weights | PASS. Tanh independence and strict monotonicity of the initial feature exhaust all zero/nonzero and coincident-scale cases. |
| Uniform initial progress over a fixed rotation family | PASS. Constants may depend on the fixed triple and on its fixed value of q. No lower bound uniform over all triples or q is established. |
| Finite fitting state with unchanged marks and M=M0 | PASS. The feature derivative Gram is positive definite; local feature perturbation and an invertible readout Gram give a finite Hilbert-space state fitting every prescribed output. |
| Equilateral separation and nonparallel class centers | PASS. The stated margins and the added determinant are exact. |
| Potential impossibility | PASS after the explicit addition omega(0)=0. It rules out the stated exponentially decaying, loss-controlling potentials on the bad trajectory, including dataset-dependent rates. |
| Nearby delay and conditional divergence of initial potentials | PASS. Delay divergence is unconditional; potential divergence is relative to any nearby successful domain on which the common bounds hold. Nearby successful angles are not proved to exist. |
| Scope limitations and finite exceptional initial-Gram orientations | PASS. The proof does not establish failure at a positive-definite initial readout Gram, positive-measure failure, or failure for a larger dictionary. |

## Mathematical checks

### 1. Functional setting, chain rule, and continuation

The bounded marks and the probability measures make all displayed expectations well defined for w and c in their stated L2 spaces. Since 0<nu,tau<1, the denominators and M0 are finite and M0>0. The initialized state belongs to the Hilbert space, and c0=0 gives f_i(0)=0 and L(0)=sum_i p_i=1.

For a Hilbert-space increment (u,h,m), the feature differential is

\[
Da_i(w)[u]=\mathbb E_g[b_1\phi'(w\cdot v_i)(u\cdot v_i)].
\]

This is a genuine Frechet differential: the pointwise Taylor remainder, integrated against bounded b1, is bounded by a constant times ||u||_2 squared. Its gradient is Lipschitz in w because phi' is Lipschitz. Consequently

\[
Df_i[u,h,m]
=M d_i\,Da_i[u]+\mathbb E_Z[H_i h]+d_i a_i m.
\]

Thus (4) is exactly minus the Hilbert gradient of L, including its factors of two, and (5) follows by the Hilbert-space chain rule. This check does not require an unjustified differentiability claim for a nonlinear map from L2 to L2.

The input's local estimates suffice. On a ball of radius R, a_i, f_i, d_i, H_i and the coefficients multiplying the remaining lower-layer factor are bounded. Differences of H_i are bounded in L-infinity because they depend on w only through the scalar a_i; the boundedness of b2 controls the argument of tanh. Differences of d_i are controlled by the L2 difference of c and the Lipschitz difference of phi'. The displayed L2 estimate for phi'(w dot v_i)v_i then controls the lower-layer equation. Hence the vector field is bounded and Lipschitz on each state ball, uniformly in unit input directions.

Integrating the loss identity yields

\[
\int_0^t\|\dot S(s)\|_{\mathcal H}^2\,ds=1-L(t)\le1,
\qquad
\|S(t)-S_0\|_{\mathcal H}\le\sqrt t.
\]

There is no compactness assumption on Hilbert-space balls. If a maximal forward existence time T* were finite, this bound would keep the solution in a fixed ball. Boundedness of the vector field on that ball makes the solution uniformly Lipschitz in time and Cauchy as t approaches T*. Completeness gives a terminal state; the local contraction argument at that state extends the solution and contradicts maximality. This supplies the continuation step in full.

For rotations, |v_i(theta)-v_i(psi)| is at most |theta-psi|. The common finite-horizon state ball and the local estimates therefore give the stated integral inequality and bound (exp(C_T t)-1)|theta-psi|. Uniform time continuity follows from the field bound on this same ball. Together these facts also justify the joint time-angle continuity used for uniform initial progress.

### 2. Covariance and the single all-time witness

With v_i replaced by -v_i, take the candidate transformed state (w,-c,M). Then a_i and H_i change sign, f_i and r_i do not, and d_i changes sign. In the w equation the signs from d_i and v_i cancel; in the M equation the signs from d_i and a_i cancel; the c equation changes sign. At time zero the candidate has the required same initialization because c0=0. Uniqueness therefore proves (7)--(8) without rotating either frozen probe.

For every fixed finite time, a_3(theta+pi)=-a_3(theta). Continuity gives a zero, including the case where an endpoint already vanishes. At a zero, H_3=f_3=0, so the third sample contributes p3 y3 squared=1/2 to L.

It is essential that the input next uses loss superlevel sets, not zero sets of a_3. Each E_n is nonempty and closed. Loss monotonicity gives E_(n+1) contained in E_n. Compactness of [0,2pi] therefore gives an angle in every E_n. For every real t>=0, selecting an integer n>=max(1,t) gives L(t)>=L(n)>=1/2 at that same angle. This proves one fixed bad dataset and one initialized trajectory. No persistent zero feature, convergent state subsequence, interchange of a long-time limit with theta, or uniform infinite-time continuity is needed.

### 3. Initial feature monotonicity and absence of stalls

Let sigma=sqrt(1-rho squared) and U=rho G1+sigma G2. Differentiating on any compact subinterval of (-1,1) gives an integrable expression proportional to

\[
\mathbb E[\phi(G_1)\phi'(U)(G_1-\rho G_2/\sigma)].
\]

Gaussian integration by parts gives respectively

\[
\mathbb E[G_1\phi(G_1)\phi'(U)]
=\mathbb E[\phi'(G_1)\phi'(U)]
 +\rho\mathbb E[\phi(G_1)\phi''(U)],
\]
\[
\mathbb E[G_2\phi(G_1)\phi'(U)]
=\sigma\mathbb E[\phi(G_1)\phi''(U)].
\]

The second-derivative terms cancel. Tanh has strictly positive derivative at every finite argument, so A'(rho)>0. Bounded convergence gives continuity at both endpoints. Interior strict monotonicity and endpoint continuity imply strict monotonicity on the closed interval. Oddness gives A(0)=0. The formula also covers input directions with negative second coordinate because the Gaussian second coordinate is symmetric.

The law of b2 has positive density throughout the interior of its bounded interval of support. A finite linear combination of the scaled tanh functions which vanishes almost surely therefore vanishes on an open interval by continuity. Real analyticity extends that identity to the real line. Taking the limit at positive infinity first gives the zero sum of coefficients; the smallest exponential tail then isolates its coefficient. Iteration proves the asserted independence for distinct positive scales. Negative scales contribute only a sign.

At initialization only the c component of the velocity can be nonzero. Grouping (11) by the nonzero magnitudes |a_i| exhausts the possible cancellations:

- A group of one cannot cancel because every weight is positive.
- A group of two could cancel only with equal weights. The three stated weights are pairwise unequal when 0<q<1 and q is not 1/2.
- If a group contains all three, its coefficient equation is p1 epsilon1+p2 epsilon2=p3 epsilon3. Since p3=p1+p2 and p1,p2>0, equality forces all three signs to agree. Equal magnitudes then give equal features and, by strict monotonicity of A, equal first coordinates. A circle has at most two distinct points with a specified first coordinate.
- If every feature were zero, every first coordinate would be zero, again permitting at most two distinct circle points.

Configurations with one or two zero features are already covered by the singleton/two-element cases. Pairwise nonparallelity ensures, in particular, the distinctness used here. Hence no rotation is an initial equilibrium. The loss derivative is strictly negative at zero, and monotonicity preserves L(t)<1 at every later positive time.

The minimum kappa over the fixed compact rotation family is positive by continuity. Uniform continuity of the velocity on a short common time-angle rectangle keeps its squared norm at least kappa/2, proving (12). Together with the all-time floor and loss monotonicity, this gives the stated positive loss limit. These constants are not asserted to remain positive uniformly as q approaches 1/2 or as the underlying triple degenerates.

### 4. Finite representability without changing marks

The functions h_j are bounded and belong to the lower-layer L2 space. If a linear combination has zero squared norm, division by b1 is legitimate off g1=0, a Gaussian-null hyperplane. The resulting continuous identity holds everywhere because the Gaussian law has full support.

For each k choose a nonzero vector perpendicular to v_k. Its inner product with every other v_j is nonzero by pairwise nonparallelity in two dimensions. Along the corresponding ray, all the other phi' factors vanish at infinity while the kth is phi'(0)=1. This forces beta_k=0. Thus the Gram K is positive definite.

Differentiating the finite-dimensional perturbation map gives

\[
\left.\frac{\partial a_i(w_z)}{\partial z_j}\right|_{z=0}
=\mathbb E_g[b_1^2\phi'(g\cdot v_i)\phi'(g\cdot v_j)(v_i\cdot v_j)]
=\langle h_i,h_j\rangle=K_{ij}.
\]

Bounded derivatives justify differentiation and continuity of this derivative. The supplied contraction proof then gives an open neighborhood of reachable feature vectors. The forbidden equations a_i=0 and a_i=plus or minus a_j form a finite union of proper hyperplanes, so the neighborhood contains a vector with all three nonzero magnitudes distinct.

At such a vector, M0>0 and the tanh independence make the readout Gram G positive definite. The displayed readout has finite L2 norm and returns exactly G(G inverse)y=y. The constructed w differs from the Gaussian initialization by a bounded perturbation; both marks and M0 remain unchanged. This works for arbitrary finite output vector y, verifying the independence of the three fitting constraints. It proves representability, not accessibility by the prescribed gradient flow or a uniform bound on the fitting norm.

### 5. Geometry and exceptional initial Grams

For the equilateral triple at theta=0, the unit directions are (1,0), (-1/2,sqrt(3)/2), and (-1/2,-sqrt(3)/2). The unit separator -v3 has the stated signed margins 1/2,1/2,1. The class-conditional means in these normalized coordinates are

\[
\mu_+=\tfrac34v_1+\tfrac14v_2=(5/8,\sqrt3/8),
\qquad \mu_-=v_3=(-1/2,-\sqrt3/2).
\]

Their determinant is -sqrt(3)/4. Rotation preserves that determinant. Thus the added nonparallel/nonantiparallel-center statement is correct; its displayed coordinates are conditional class means in normalized input coordinates.

By odd strict monotonicity of A, zero initial features are exactly zero first projections, and equal absolute initial features are exactly equal absolute first projections. For a fixed nonparallel pair, the latter equations say that the first projection of the rotated vector v_i-v_j or v_i+v_j vanishes. These vectors are nonzero, so each equation has finitely many solutions modulo 2pi. The union over all samples and pairs is finite. Outside it, tanh independence makes the initial readout Gram positive definite. The compactness witness is not proved to lie outside that finite exceptional set. The stated caution about almost-everywhere or further-nondegeneracy theorems is therefore necessary and correct.

### 6. Potential and delay consequences; resolved endpoint defect

In the original input, (13) assumed only lim_{s downarrow 0} omega(s)=0. Taken literally, that is insufficient when Phi may equal zero: the state potential Phi identically zero, together with omega(0)=1 and omega(s)=s for s>0, satisfies both original inequalities along the initialized trajectories, because L(t)<=1. It also satisfies the stated punctured right-hand limit. This was a corollary-level logical defect, not a defect in the trajectory theorem.

The final input explicitly adds omega(0)=0. With that addition, a finite nonnegative initial potential and exponential decay imply Phi(S_t) tends to zero, and the comparison tends to zero whether the potential remains positive or reaches zero. This contradicts the all-time floor. Dataset-dependent lambda>0 and comparison functions do not evade the contradiction. The fixed-power comparison already had the required zero value and was valid without this textual correction.

For 0<ell<1/2 and finite T>=0, finite-time angle continuity gives L(T;theta)>ell in a neighborhood of the bad angle. Monotonicity rules out hitting ell at earlier times, and time continuity also rules out an infimum hitting time equal to T while L(T)>ell. With the empty-set infimum understood as infinity, tau_ell(theta)>T. Since the argument holds for each T, it is exactly divergence in the extended sense as theta approaches the bad angle.

On any domain of nearby successful angles carrying the common exponential bound and common power comparison, the same inequality gives

\[
\ell<L(T;\theta)
\le C e^{-\alpha\lambda T}\Phi(S_0;\theta)^\alpha,
\]

which is precisely the claimed lower bound on the initial potential. Its divergence is along that domain; no existence or density of successful angles is established. Allowing a vanishing rate can avoid this particular common-rate lower-bound conclusion, but does not itself construct a successful potential.

## Remaining limitations and final disposition

No unresolved gap was found in the corrected theorem for the displayed scalar flow. The result proves failure despite representability, positive initial progress, pairwise nonparallel inputs, and, in the explicit equilateral family, linear separability and nonparallel class centers. It does not locate the bad angle, prove a positive-measure failure set, ensure positive definiteness of its initial readout Gram, quantify a geometry-independent initial decrease, establish nearby success, or extend to a vector-valued code, adaptive probe, nonzero initial readout, or the full canonical dictionary. Those limitations remain explicit in the input.

The only identified false literal claim was the original endpoint-uncorrected form of (13); the final reviewed input repairs it. The corrected mathematical package passes this isolated internal audit within the stated scope.
