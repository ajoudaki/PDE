# Isolated adversarial premise-conditional audit

Reviewed file: `/tmp/l3-two-sample-proof-DLuelg/POSITIVE_TIME_MIDDLE_CURVATURE.md`

Verified SHA256:

`9efd5283d35a493982f3a142332536d32a9905eff62cb44ea8793aaf001ea79a`

Verified length: **478 lines**. All line references below refer to this exact version.

This audit read only the specified source. No named dependency, other mathematical/project/history/review file, or external source was read. No experiment was performed and no candidate edit was made. The mathematical checks below use elementary calculations and arguments supplied or developed here; they do not invoke specialized external theorems.

## 1. Verdict and premise boundary

**Verdict: the local distributional and non-Lipschitzness conclusions are supported, conditional on the expressly authorized Section 1 imports. I found no required mathematical correction and no additional unlisted premise needed under that premise boundary.** Several optional clarifications would make the existing proof harder to misread; they are listed separately in Section 11 of this report.

In particular, the proof supports the following statements at every fixed sufficiently small positive feature time:

- A middle preactivation can lie in any prescribed interval of positive length while its reverse query has either arbitrarily large sign, with the stated Gaussian-order probability lower bound.
- On a fixed interval of nonzero activation curvature, the signed middle curvature multiplier has both essentially unbounded tails.
- The full scalar loss has ordinary second derivatives along the specified individual bounded rank-one directions, with both signs unbounded over unit directions.
- Its raw Hilbert gradient therefore cannot be Lipschitz on a neighborhood of the reached state.
- The feature states correspond to deterministic positive local physical times by the stated scalar clock.

This is **not** a certification of the imported finite-Euler construction, its Gaussian source independence, its response coefficients, its local convergence, its scalar-gradient facts, or the global theorem. In particular, this audit does not establish that the imported Gaussian law is the law of an actual initialized/trained network independently of those hypotheses.

The accepted premises actually used are:

1. The actual canonical finite-Euler construction and initialized Gaussian operators described in Section 1, including the separate population spaces and actual adjoints (lines 20–43 and 83–110).
2. The fixed-mesh, fixed-cap law (2), centeredness and independence of the **entire** forward and reverse source groups, deterministic coefficients, the coefficient bounds (3), and covariance identities (4) (lines 88–110).
3. The feature-time equations and raw metric, bounded features and gates, local primal bounds, and the readout bound (lines 43–81).
4. The actual local solution, strong cut removal, fixed-cap mesh convergence, and the requisite joint field/moment convergence (lines 72–77).
5. The imported upper exponential moment for the reverse query at the actual state (lines 105–106).
6. The scalar-gradient interpretation and actual-trajectory sample symmetry (4a), obtained from the imported equivariant construction and deterministic predictor limits (lines 53–55 and 112–130).

Two boundaries are especially important. First, item 1 includes the canonical forward Gaussian initialization used in Section 4 to show that the initial top feature pair has positive-definite Gram matrix. Second, item 6 is a fact about the actual trajectory, not a property of arbitrary deterministic arrays satisfying only (3). The document respects both distinctions.

If one weakened the premise set to the displayed middle-population equations (2)–(4) and their numerical bounds alone, positive initial top-label velocity and actual sample symmetry would need to be supplied separately. That is a different, weaker premise set from the one authorized for this audit; those facts are not additional unlisted premises here.

## 2. Section 3: primal estimates and temporal covariance

### 2.1 A cap-independent estimate can be made explicit

Lines 165–187 contain a genuine derivation from primal bounds. In particular, they do not require temporal regularity of a backward response coefficient or of a cutoff derivative beyond the stated contraction properties.

Here is an explicit choice of finite constants that checks the dependence and the factors from the two samples. Put

\[
T=3/2,\qquad
M_3=10+\tfrac12 e a^2T^2,\qquad
M_2=10+\tfrac12 e^2a^2M_3T^2.
\]

At an Euler node of time \(t_k\), the readout bound gives

\[
\|\delta^{(3)}_{k,a}\|_2\le ea t_k.
\]

For a rank-one Euler increment, the operator norm is bounded by the product of the two population RMS norms. The factor \(1/2\) in the update cancels the sum over the two samples when the same upper bound is used for both. Thus

\[
\|\Delta W^{(3)}_k\|_{\rm op}\le e a^2t_k\Delta.
\]

Since \(\sum_{r<k}t_r\Delta\le T^2/2\), this proves the bound \(M_3\). Next,

\[
\begin{aligned}
\|q^{(2)}_{k,a}\|_2&\le M_3ea t_k,\\
\|\delta^{(2)}_{k,a}\|_2&\le e^2aM_3t_k,\\
\|\Delta W^{(2)}_k\|_{\rm op}&\le e^2a^2M_3t_k\Delta.
\end{aligned}
\]

This proves the bound \(M_2\). Applying the same gate and cutoff estimates to the bottom backward field gives

\[
\|\delta^{(1)}_{k,a}\|_2\le e^3aM_2M_3t_k.
\]

For every \(\rho\in[-1,1)\), the sum of the absolute values of a row of \(C\), divided by two, is at most one. Therefore a first-field adjacent increment has RMS at most \(L_1\Delta\), where

\[
L_1=e^3aM_2M_3T.
\]

This also covers \(\rho=-1\); no inverse of the singular input covariance is needed for this coordinate estimate.

For completeness, define

\[
N_2=e^2a^2M_3T,\qquad N_3=ea^2T,
\]

and

\[
F_2=aN_2+M_2eL_1,\qquad
F_3=aN_3+M_3eF_2.
\]

The exact split in lines 178–179 then bounds the adjacent changes of \(Z^{(2)}\) and \(Z^{(3)}\) by \(F_2\Delta\) and \(F_3\Delta\), respectively. Splitting the top delta as in lines 183–184 gives the permissible choice

\[
D=ae+aTcF_3.
\]

All these constants are finite and independent of the mesh and both caps. The bounds use \(|\tau_Q(u)|\le |u|\), not an estimate proportional to the cap.

These formulas are not asserted as sharp constants; they verify that the unspecified constants in Section 3 have the required uniformity. The quoted values \(m,a,e,c\) are safe bounds for the given activation; in particular, \(\phi'=0.1\,\operatorname{sech}\) and \(\phi''=-0.1\,\operatorname{sech}\tanh\).

### 2.2 Passage to the finite Gaussian law

The use of the initial operator-norm event at lines 189–191 is compatible with taking the width limit first, with the mesh and caps fixed. An inequality holding on events of probability tending to one transfers to its deterministic empirical-moment limit. The relevant moment convergence is part of the accepted construction. There is no interchange with a growing number of Euler queries.

The high-probability norm bound used here is also an elementary consequence of the specified Gaussian matrix initialization, rather than a need for a specialized spectral theorem. For example, for an \(n\)-by-\(n\) matrix with entries \(N(0,1/n)\), two \(1/4\)-nets of the unit sphere, each of cardinality at most \(9^n\), give

\[
\Pr\{\|W\|_{\rm op}>10\}
\le 2\,9^{2n}\exp(-25n/2)\longrightarrow0.
\]

Indeed, the operator norm is at most twice the largest bilinear form over these nets, and each such bilinear form has variance \(1/n\). A union bound covers the two initialized hidden matrices. This observation checks that the norm event does not conceal an extra specialized probabilistic premise; it does not verify the imported finite-program limit.

The covariance identity (4), applied to the difference of two coordinates of the same sample, then gives (8) exactly. Zero initial readout implies zero initial reverse source, including in the possibly singular Gaussian law.

### 2.3 Interpolation and centered chaining

Lines 197–200 are correct. On a single mesh cell, a linearly interpolated increment is the appropriate fractional multiple of the node increment. Across several cells, the triangle inequality in Gaussian \(L^2\) adds the elapsed lengths. Thus the same increment constant \(D\) works for all real times in the interpolated array.

The process is centered, continuous, and finite dimensional for each fixed mesh. No infinite-dimensional Gaussian-path existence result is required.

The maximum estimate at lines 212–215 is correct without independence among the entries. If \(M_N=\max_i|G_i|\), each entry is centered and has variance at most \(v^2\), then splitting the tail integral at \(2v^2\log(2N)\) gives

\[
\mathbb E M_N^2
\le 2v^2\bigl(\log(2N)+1\bigr).
\]

At dyadic level \(j\), the resulting \(L^2\) bound is at most a universal constant times

\[
DS\,2^{-j}\sqrt{j+1}.
\]

Its sum is finite. Minkowski's inequality for partial sums and continuity, followed by the elementary nonnegative limit inequality, justify the asserted supremum estimate. The explicit treatment of \(S\) as an endpoint prevents the usual left-dyadic approximation omission at the right endpoint.

Applying the estimate separately to the two samples and bounding the square of their maximum by the sum of their squared suprema costs only a fixed factor. Correlation between samples is harmless.

Finally, orthogonal projection in the Gaussian \(L^2\) space contracts every increment norm. Therefore the centered residual after regression on a scalar obeys the same increment estimate. This is precisely the residual statement used in Section 4; it does not assume that the conditioned, noncentered reverse process itself obeys a centered estimate.

**Section 3 finding:** correct, with uniform constants and no missing chaining or Gaussian-path hypothesis.

## 3. Section 4: nondegeneracy and a reverse-only event

### 3.1 Initial nondegeneracy and the choice of positive time

For \(|\rho|<1\), positive density of the first Gaussian pair and nonconstancy of \(\phi\) imply linear independence of its two feature variables in \(L^2\). For example, a vanishing linear combination would, by continuity and positive density, vanish on all of \(\mathbb R^2\); varying one coordinate forces both coefficients to vanish.

For \(\rho=-1\), write the features as \(1+b(G)\) and \(1-b(G)\). Oddness gives \(\mathbb Eb(G)=0\), and nonconstancy gives \(\mathbb Eb(G)^2>0\). Their uncentered Gram matrix has eigenvalues \(2\) and \(2\mathbb Eb(G)^2\), both positive. In particular, the constant offset prevents the singular centered-feature relation from making this uncentered Gram matrix singular.

The canonical Gaussian forward initialization imported in Section 1 then gives the next Gaussian pair with this Gram matrix as covariance. Repeating the positive-density argument proves positivity of the subsequent feature Grams, including the initial top feature Gram. Consequently

\[
\|V_0\|_2^2
=\tfrac14 y^TK^{(3)}_0y>0
\]

for every sign vector \(y\). This step uses the actual initialization premise, not independence between finite trained neurons.

From the readout equation and strong continuity of the top features,

\[
\frac{W^{(4)}(S)}S
=\frac1S\int_0^S\frac12\sum_a y_aH^{(3)}_a(u)\,du
\longrightarrow V_0\quad\text{in }L^2.
\]

Thus one choice of \(S_0>0\), reduced if necessary to be at most \(3/2\), makes the readout nonzero for **every** \(0<S\le S_0\). Strong continuity also preserves positive definiteness of the first feature Gram. Since \(g(0)=0\), continuity allows \(|g(u)|<1/2\) throughout this interval.


The fields \(Z^{(3)}_a(S)\) are finite almost surely because they belong to \(L^2\). Strict positivity of \(\phi'\) on the real line therefore implies that multiplying a nonzero \(W^{(4)}(S)\) by the gate cannot annihilate it almost surely. This proves (10) for each sample. No uniform positive lower bound on the gate is needed.

### 3.2 Variance quantifiers

For fixed \(S>0\) and sample \(a\), set \(v_a=v_a(S)>0\). Strong cut convergence makes the terminal cut variance at least \(3v_a/4\) for all sufficiently large common caps. For each such cap, sufficiently fine fixed-cap mesh convergence makes the Euler variance at least \(v_a/2\). Therefore the quantifier order in lines 237–242 is valid:

\[
\exists Q_0\ \forall Q\ge Q_0\ \exists M_0(Q)\
\ \forall M\ge M_0(Q):\quad v\in[v_0,v_1],
\]

where \(v_0=v_a/2\) and \(v_1=(eaS)^2\).

Uniformity of \(M_0\) in \(Q\) is unnecessary and is not claimed. These variance thresholds do not depend on the eventual tail threshold \(R\).

### 3.3 Regression, singular support, and the event used for conditioning

Regression on \(X=\zeta_{M,a}\) divides only by \(v>0\). Even if the remaining covariance is singular, the residual vector is jointly Gaussian and has zero cross covariance with \(X\). The Gaussian characteristic function therefore factors, proving independence of the entire residual vector and \(X\).

The coefficient estimate

\[
|c_{k,b}|\le\frac{eaS}{\sqrt{v_0}}
\]

follows directly from Cauchy–Schwarz. The residual starts at zero and satisfies the increment estimate by orthogonal projection. If \(C_{\rm ch}\) denotes a universal constant in (9), one may take

\[
B_0=2C_{\rm ch}DS.
\]

Indeed, the expected squared maximum over both residual paths is at most \(2C_{\rm ch}^2D^2S^2\), so Markov gives (12). Nonzero terminal variance precludes the degenerate case \(DS=0\).

For precision, define the event actually used in Sections 4–5 by

\[
E_R^\sigma=
\{\sigma X\in[R+a+1,R+a+2]\}
\cap\{\max_{k,b}|G_{k,b}|\le B_0\}.
\]

This event is measurable with respect to the **reverse source alone**. Its probability is at least

\[
\frac{1}{2\sqrt{2\pi v_1}}
\exp\!\left[-\frac{(R+a+2)^2}{2v_0}\right],
\]

which has the claimed form uniformly in the relevant caps and meshes. The two factors defining the event are independent. No independence among residual coordinates is used.

On this event a deterministic permissible path bound is

\[
B_R=\frac{eaS}{\sqrt{v_0}}(R+a+2)+B_0.
\]

The coefficient row bound and bounded features give

\[
|q^{(2)}_{k,b}-\zeta_{k,b}|\le a
\]

for every realization of the forward source, including every source variation made subsequently. Hence the terminal signed query is at least \(R+1\), uniformly over those variations.

The wording “reverse source satisfying (14)” at line 276 should be understood through this reverse-only event. The query in (14) is generally not itself a reverse-source coordinate. Lines 270–272 supply the needed universal implication, so the proof does not actually condition on a forward-dependent query event. Naming \(E_R^\sigma\) would be an optional clarity improvement.

**Section 4 finding:** correct. The large terminal reverse value has Gaussian-order cost, and its entire source path is controlled with no mesh-dependent union-bound loss.

## 4. Section 5: forward regression with coefficients frozen

### 4.1 Valid conditional coordinates even for singular Gaussian arrays

By the covariance identity, \(X_f=\xi_{M,a}\) is centered Gaussian with variance in \([m^2,a^2]\). The stated bound

\[
|d_{k,b}|\le a^2/m^2=d_0
\]

is valid, although not sharp. In particular, \(d_{M,a}=1\) and \(F_{M,a}=0\) almost surely and throughout the residual support.

The residual \(F\) is independent of \(X_f\), and the pair is independent of the complete reverse source. Thus the conditional law of \(X_f\), given \(F\) and the reverse source, is its original nondegenerate one-dimensional Gaussian law.

Varying \(x\) while holding \(F\) fixed is legitimate even when the full source covariance is singular. Independence makes the joint support of \((X_f,F)\) the product of \(\mathbb R\) and the residual support. Its image under \((x,F)\mapsto dx+F\) is contained in the original Gaussian support. In particular, the argument does not hold all other forward source coordinates fixed: they vary by their regression coefficients, as they must.

All coefficients and all covariances remain those of the original fixed Euler law. A conditional event under a fixed self-consistent law does not require recomputing that law's coefficients after conditioning. This is the correct use of the “frozen” calculation at lines 108–110 and 303–305.

### 4.2 The recursion is well defined and continuous

There is no hidden implicit-equation issue in (2). At node \(k\), the first equation uses only earlier deltas. It determines both current preactivations and features; the second equation can then use those current features to determine the queries. The last equation determines the current deltas. Each step is continuous.

On \(E_R^\sigma\), bounded features and the row bound give

\[
|q_{k,b}|\le B_R+a,\qquad
|\delta_{k,b}|\le e(B_R+a)
\]

for every \(x\) and every residual value under consideration. No forward residual path bound is needed.

There are two sample terms per past time in the first equation of (2). Therefore its coefficient sum at the terminal node is bounded by

\[
2M\frac{(3/2)\Delta}{2}=\frac32S.
\]

Since the terminal forward residual vanishes, this proves precisely

\[
|Z_{M,a}(x)-x|\le D_R:=\frac32Se(B_R+a).
\]

The factor \(3/2\) and the cancellation of \(F_{M,a}\) in (16) are both correct.

### 4.3 Uniform Lipschitz estimate in the remaining scalar coordinate

For two choices \(x,x'\), bounded \(\phi'\) and the row sum of \(B\) give

\[
|q_{r,b}(x)-q_{r,b}(x')|\le eE_r.
\]

Splitting the gate difference from the cutoff difference yields

\[
|\delta_{r,b}(x)-\delta_{r,b}(x')|
\le\bigl[c(B_R+a)+e^2\bigr]E_r.
\]

Here the gate difference uses \(|\tau_Q(q)|\le|q|\), and the query difference uses the one-Lipschitz property of \(\tau_Q\). This verifies both terms in \(L_R^0\); there is no missing cutoff derivative factor.

Taking the maximum over all earlier nodes preserves the upper bound involving \(\sum_{r<k}E_r\). Direct induction gives

\[
E_k\le d_0|x-x'|(1+\tfrac32\Delta L_R^0)^k
\le d_0e^{(3/2)SL_R^0}|x-x'|.
\]

Thus (18) is correct, uniformly in the entire residual array, the caps, and the meshes. Because \(B_R\) is linear in \(R+1\), the terminal Lipschitz constant grows at most exponentially in \(R+1\).

### 4.4 Placing the terminal coordinate in an interval

The bounded displacement from \(x\) gives the two opposite inequalities at the endpoints chosen in lines 315–316. The intermediate value theorem supplies some \(x_0\) with terminal preactivation \(b\); monotonicity or a nonzero derivative is not required.

The radius

\[
r_R=\min\{1/2,h/(2L_R)\}
\]

ensures that the full closed interval around \(x_0\) maps into \([b-h/2,b+h/2]\). It has length \(2r_R\), lies in the bounded region specified at line 324, and has a lower length bound of the form \(c\exp[-C(R+1)]\).

The Gaussian density lower bound at lines 326–330 is correct: the prefactor uses the largest possible variance, and the exponent uses the smallest possible variance. Multiplying it by \(2r_R\) gives (19), since a linear exponential cost is absorbed into a quadratic cost for \(R\ge1\).

No measurable choice of \(x_0\) is needed. For fixed residual and reverse coordinates the terminal recursion is a continuous function of \(x\), and its preimage of the target closed interval is Borel. That set contains at least one interval with the uniform length and location bounds just proved. Integrating its indicator against the fixed Gaussian density provides a conditional-probability kernel directly.

“Any” conditional value in line 332 can be interpreted using this explicit kernel on the residual support; conditional probabilities in general are only uniquely specified almost surely. This distinction has no effect on (19)–(20).

Finally, integrating the conditional lower bound over \(F\) and over \(E_R^\sigma\) multiplies two uniform lower bounds. It does not assume independence between the evolved query and preactivation. Enlarging the exponent constant after multiplication is legitimate.

**Section 5 finding:** correct. No density for the full Gaussian vector, covariance inverse, bound on the forward residual, monotonicity, or re-solved self-consistency equation is needed.

## 5. Complete dependence and limit quantifiers

The proof has the following permissible order:

1. Fix the input and label configuration and choose one sufficiently small \(S_0>0\).
2. Fix \(S\in(0,S_0]\), a sample, a sign, and a target interval.
3. Choose \(v_0,v_1\) and a sufficiently large-cap threshold \(Q_0\); for each \(Q\ge Q_0\), choose the mesh threshold \(M_0(Q)\).
4. Choose constants in the probability estimates from these fixed quantities, the interval, and the uniform primal constants.
5. For every \(R\ge1\), establish (20) for every such cap and sufficiently fine mesh.
6. With \(R\) fixed, first send \(M\to\infty\) at each fixed cap, then send the cap to infinity.

In particular:

- The probability constants do not depend on \(Q\) or \(M\).
- The variance-based cap and mesh thresholds can be chosen independently of \(R\).
- The proof does not require the cap to exceed the realized query or the tail threshold. The query whose tail is studied is the uncapped query; the cutoff is applied in the delta recursion.
- Constants can depend on the fixed positive time and configuration, and on the chosen interval. There is no lower bound uniform as \(S\downarrow0\) or as a nondegenerate configuration approaches degeneracy.
- Dependence on sample and sign is harmless. There are only finitely many such choices, so one can take the minimum of the positive lower prefactors and the maximum of the exponent constants if a single pair \(c_I,C_I\) is desired for them.
- Establishing the resulting numerical probability inequality for each real \(R\) establishes the universal tail statement. No intersection of uncountably many source events, common source realization across meshes, or exchange of a tail limit with a mesh/cap limit is required.

The width limit underlying the finite Gaussian law is taken separately at each fixed mesh and cap. Nothing here proves or uses a width-growing finite-program assertion.

## 6. Section 6: the closed-set passage and curvature tails

Let

\[
F_R=[b-h/2,b+h/2]\times\{q:\sigma q\ge R+1\}.
\]

This is closed in \(\mathbb R^2\), although it is not compact. For weak convergence of the terminal pair, the inequality needed in lines 352–355 has the correct direction:

\[
\Pr\{X_{\rm limit}\in F_R\}
\ge\limsup_n\Pr\{X_n\in F_R\}.
\]

The displayed continuous approximants \(\max(0,1-j\operatorname{dist}(x,F_R))\) are bounded, dominate the closed-set indicator, and decrease to it. This proves the required inequality directly; neither compactness nor an assertion that the boundary has zero probability is needed.

Both passages are available under the imported joint convergence. Coordinatewise marginal convergence alone would not suffice, but it is not all that Section 1 provides. Strong joint cut convergence is more than sufficient for the second passage. The source regressions and their coefficients need not themselves converge.

The closed inner preactivation interval lies strictly inside the requested interval, and \(\sigma q\ge R+1\) implies the requested strict inequality \(\sigma q>R\). Both buffers are correctly used. Consequently open, closed, bounded, or unbounded target intervals of positive length are covered by selecting a finite closed subinterval of their interior.

For a fixed closed interval \(J\subset(1,2)\), write

\[
\alpha_J=\min_{z\in J}|\phi''(z)|>0.
\]

On this interval \(\phi''<0\). To force a desired sign \(\eta\in\{-1,1\}\) of \(y_a\phi''q\), use query sign \(-\eta y_a\) and query threshold \(R/\alpha_J\). The lower probability estimate remains of Gaussian order after this fixed rescaling. Both localized signed tails therefore have positive probability at every level.

For the upper bound, globally \(|y_a\phi''q|\le c|q|\), so the imported exponential moment gives

\[
\Pr\{|y_a\phi''q|>R\}
\le2\exp[-R^2/(16c^2)].
\]

The same upper bound also bounds a localized tail. If conditional tails given \(Z^{(2)}\in J\) are intended, the joint lower bound implies that this conditioning event has positive probability, and division by its fixed probability gives corresponding conditional estimates.

These statements establish essential unboundedness of both signs and unboundedness of the middle multiplication operator on \(L^2\). They do not supply asymptotically sharp tail constants or independence of the two evolved fields.

**Section 6 finding:** correct, including the direction of the closed-set inequality and both limiting operations.

## 7. Section 7: admissible directions and ordinary second derivatives

### 7.1 The rank-one direction isolates exactly one sample

The first feature Gram \(K\) is positive definite at the chosen state. Its inverse is a finite deterministic matrix. Since the features are bounded, \(B_a\) is bounded. Matrix multiplication gives exactly

\[
\mathbb E B_a^2=1,\qquad
\mathbb E[B_aH^{(1)}_b]=d_a\mathbf1_{a=b},\qquad d_a>0.
\]

For any individual bounded second-population field \(v\) with \(\|v\|_2=1\), the operator \(v\otimes B_a\) has Hilbert–Schmidt norm one. It is an admissible increment in the raw affine Hilbert state space. The singular-input case \(\rho=-1\) causes no problem here, since no first-field variation is taken and \(K\), rather than \(C\), is inverted.

Along this line the first features are fixed, and hence

\[
Z^{(2)}_b(t)=Z^{(2)}_b+t d_av\mathbf1_{a=b}.
\]

Thus the other sample's second field, all its later forward fields, and its predictor are unchanged for the entire line. Formula (21) follows by differentiation and boundedness of the fixed operator \(W^{(3)}\). It does not identify or equate different population spaces.

### 7.2 The intermediate curve is genuinely twice differentiable in \(L^2\)

The distinction between ordinary and Peano second derivatives is material. A second-order expansion of a scalar function by itself would not establish the ordinary derivative of its first derivative. For the present directions, however, the stronger property required in lines 396–399 follows directly from bounded \(v\).

Indeed, with \(z_2=Z^{(2)}_a\),

\[
H^{(2)}_a(t)=\phi(z_2+t d_av)
\]

is a \(C^2\) curve in \(L^2\), with

\[
\begin{aligned}
\frac{d}{dt}H^{(2)}_a(t)&=d_a\phi'(z_2+t d_av)v,\\
\frac{d^2}{dt^2}H^{(2)}_a(t)&=d_a^2\phi''(z_2+t d_av)v^2.
\end{aligned}
\]

The first derivative is controlled in \(L^2\) by a constant times \(|v|\); the second is controlled by a constant times \(v^2\in L^2\). Continuity and the stated derivative bounds justify the difference quotients and continuity of the second derivative by domination. Applying the bounded linear operator \(W^{(3)}\) therefore makes \(z(t)=Z^{(3)}_a(t)\) a \(C^2\) curve in \(L^2\). In particular,

\[
\frac{z'(t)-z'(0)}t\longrightarrow z''(0)
\quad\text{in }L^2.
\]

This establishes the property used at line 398; it is not a new regularity premise. Adding these derivative formulas near lines 389–392 would make that point explicit.

### 7.3 The final scalar pairing has an ordinary second derivative without \(L^4\) control

Freeze \(w=W^{(4)}(S)\). Its bound \(\|w\|_\infty\le aS\) is essential to the stated argument and is already imported. Set

\[
u=z'(0),\qquad b=z''(0),\qquad
A_t=\frac{z(t)-z(0)}t,
\]

and

\[
J_t=\int_0^1\phi''(z(0)+\theta(z(t)-z(0)))\,d\theta.
\]

Then \(A_t\to u\) in \(L^2\), \(|J_t|\le c\), and \(J_t\to\phi''(z(0))\) in probability. Consequently

\[
\|A_tJ_t-u\phi''(z(0))\|_2
\le c\|A_t-u\|_2
+\|u(J_t-\phi''(z(0)))\|_2\longrightarrow0.
\]

For the last limit, first truncate the fixed \(L^2\) variable \(u\). On its bounded part, bounded convergence in probability gives convergence in \(L^2\); on its tail, the square integral is uniformly bounded by a constant times \(\mathbb E[u^2\mathbf1_{|u|>K}]\), which tends to zero. This spells out the product argument in lines 405–407.

The first derivative of the scalar pairing is

\[
\frac{d}{dt}\mathbb E[w\phi(z(t))]
=\mathbb E[w\phi'(z(t))z'(t)].
\]

In its difference quotient, the factor \((z'(t)-u)/t\) converges strongly to \(b\), and the remaining gate difference quotient converges strongly to \(u\phi''(z(0))\), as just proved. Since \(wu\in L^2\), this proves the **ordinary** second derivative

\[
\mathbb E[w\phi'(z(0))b]
+\mathbb E[w\phi''(z(0))u^2].
\]

The second integrand is in \(L^1\) because \(w\) and \(\phi''\) are bounded and \(u\in L^2\). There is no need for \(u\in L^4\), a bounded \(L^2\)-to-\(L^4\) mapping property of \(W^{(3)}\), or twice Fréchet differentiability of the full activation map on \(L^2\).

### 7.4 The Taylor cross remainder is correct but is not a substitute for the preceding argument

For \(z(t)=z(0)+tu+r_t\), the scalar expression comparing the \(r_t\) increment with its linearization at \(z(0)\) is bounded pointwise by

\[
c\bigl(|tu||r_t|+|r_t|^2/2\bigr).
\]

Pairing with bounded \(w\) gives exactly the estimate in lines 412–413. The retained \(|t|\) makes the first term \(O(|t|^3)\) when \(\|r_t\|_2=O(t^2)\), so the claimed \(o(t^2)\) remainder is correct.

The word “Equivalently” at line 409 should not be read as a general equivalence between an ordinary second derivative and a Peano expansion. For example, \(t^4\sin(1/t^2)\), extended by zero at zero, is a \(C^1\) scalar function with a zero second-order Peano coefficient at zero but no ordinary second derivative there: its first derivative divided by \(t\) contains \(-2\cos(1/t^2)\). The present proof avoids this issue because the stronger \(C^2(L^2)\) property was established above and the difference quotient of the scalar first derivative is actually evaluated. Replacing “Equivalently” with “The corresponding Taylor remainder can also be bounded as follows” would be an optional wording improvement.

**Derivative finding:** formula (22) is an ordinary second directional derivative for every displayed individual direction. No unlisted ordinary-second-derivative premise is necessary.

## 8. Section 7: curvature, the full loss, and the gradient contradiction

### 8.1 The curvature formula and bounded remainder

Substituting the two derivatives of \(z(t)\) into the scalar formula gives (22), including its factor \(y_ad_a^2/2\). In the first term, adjunction is legitimate because \(\phi''(Z^{(2)}_a)v^2\in L^2\) and \(\delta^{(3)}_a\in L^2\). Its adjoint image is the actual uncut \(q^{(2)}_a\).

For the second term,

\[
\|W^{(3)}[\phi'(Z^{(2)}_a)v]\|_2
\le\|W^{(3)}\|_{\rm op}e,
\]

so (23) follows exactly. It is uniform over all the unit directions in this class even though their individual \(L^\infty\) norms need not have a common bound.

Let \(T_a=y_a\phi''(Z^{(2)}_a)q^{(2)}_a\). The tail result gives positive probability to \(\{T_a>N\}\) and \(\{T_a<-N\}\) for every sufficiently large \(N\), or to the corresponding events also localized in a fixed curvature interval. The normalized indicators of these events are bounded individual fields of \(L^2\) norm one. Thus

\[
\mathbb E[T_av^2]>N
\quad\text{or}\quad
\mathbb E[T_av^2]<-N,
\]

respectively. Each integral is finite: bounded \(\phi''\), the imported moment bound on \(q\), and individual boundedness of \(v\) suffice. Since \(d_a>0\) is fixed and the other term is uniformly bounded, both signs of (22) are unbounded.

This argument constructs directions in the population Hilbert space. It does not claim a bound on their \(L^\infty\) norms uniform in \(N\), nor that these directions have already been realized or approximated at finite network width.

### 8.2 Uniform control of the squared first derivatives

The imported scalar-gradient framework and primal bounds justify lines 436–439. For the displayed directions one can also check the needed bound directly, without any neighborhood-wide regularity assertion:

\[
Df_a[v\otimes B_a]
=d_a\mathbb E[q^{(2)}_a\phi'(Z^{(2)}_a)v],
\]

so

\[
|Df_a[v\otimes B_a]|
\le d_ae\|q^{(2)}_a\|_2.
\]

The other predictor is constant on this line. This proves the uniform bound on the sum of squared first directional derivatives needed for (24).

### 8.3 Sample symmetry is used only at the base state

Write the full raw direction as \(h=v\otimes B_a\), and use the globally defined scalar functional \(g=\tfrac12\sum_b y_bf_b\). Differentiating the unreduced loss gives

\[
D^2L[h,h]
=2\sum_b(Df_b[h])^2
+2\sum_b(f_b-y_b)D^2f_b[h,h].
\]

At the base state only, (4a) gives \(f_b-y_b=y_b(g-1)\). Therefore

\[
D^2L[h,h]
=2\sum_b(Df_b[h])^2+4(g-1)D^2g[h,h],
\]

which is exactly (24). There is no differentiation of sample symmetry along the perturbation line. Such a differentiation would be unjustified for these sample-isolating directions and would generally produce the wrong squared-first-derivative term. The candidate explicitly avoids it.

Since \(|g|<1/2\), the coefficient \(4(1-g)\) lies between 2 and 6. The uniformly bounded squared-first-derivative term cannot cancel either unbounded sign of \(D^2g\). Consequently \(D^2L\) also has both unbounded signs over the unit directions.

### 8.4 The non-Lipschitzness implication

Suppose the raw gradient of \(L\) were Lipschitz with constant \(L_0\) on a neighborhood of the base state. For any fixed unit direction \(h\) from the displayed class and all sufficiently small nonzero \(t\),

\[
\left|\frac{\langle\nabla L(x+th)-\nabla L(x),h\rangle}{t}\right|
\le L_0.
\]

The ordinary second directional derivative just established is the limit of this quotient. Its magnitude must therefore be at most \(L_0\), contradicting the unbounded directional values. The order of operations is legitimate: take the ordinary derivative separately for each fixed direction, then compare the resulting values over the direction class. No Taylor remainder uniform over the class is needed.

This proves the claimed failure of neighborhood Lipschitzness. In fact, even a common finite Lipschitz bound comparing the base gradient to nearby gradients would give the same contradiction. It does not imply failure of continuity of the gradient, nonexistence of the imported flow, or failure of uniqueness.

**Section 7 finding:** the full-loss conclusion is correct under the stated scalar-gradient premises, with ordinary derivatives and with base-state-only use of symmetry.

## 9. Physical time

At each actual trajectory state, the same symmetry identity gives

\[
-\nabla L
=2(1-g)\sum_a y_a\nabla f_a
=4(1-g)\nabla g.
\]

Since feature time is gradient-ascent time for \(g\), the change of variables in lines 457–459 follows. The bound \(|g(u)|<1/2\) throughout the chosen interval makes the clock continuous and strictly positive. In particular,

\[
S/6\le t(S)\le S/2.
\]

Thus the reached feature states occur at deterministic positive local physical times. This is a local reparametrization of the imported trajectory; it proves neither an exact finite-width samplewise clock nor global physical continuation.

## 10. Additional-premise audit and exact scope

No additional unlisted premise was needed to complete any of the checks above within the authorized Section 1 premise set. In particular, the proof does not require:

- Independence of finite trained neurons, or independence of evolved preactivation and reverse query.
- Independence among time or sample coordinates within either Gaussian source group.
- Nonsingularity or uniformly bounded inverses of full time/sample covariance matrices.
- Convergence of Gaussian source paths, regression coefficients, or covariance inverses as the mesh or cap varies.
- Uniform convergence in the cap of the mesh approximation, or a width-growing Gaussian-program theorem.
- A forward residual supremum bound, monotonicity of the terminal source-to-preactivation map, or an inverse-function theorem.
- Differentiation of deterministic response coefficients, covariance data, or self-consistency equations when conditioning.
- A uniform \(L^\infty\) bound on all test directions, an \(L^4\) bound for their top preactivation derivatives, or a bounded ambient Hessian.
- Sample symmetry away from the actual base state along the test line.
- A uniqueness, restartability, global fitting, or global physical-clock premise for the new local conclusions.

The source's scope limitations at lines 154–161 and 463–478 are appropriate. The tail theorem is local in time and conditional on the exact source construction and local convergence. It demonstrates that fast decay of this activation's derivatives at large preactivation does not bound the trained middle multiplier, because the large reverse query can coexist with a preactivation confined to a fixed ordinary interval of curvature.

It does not establish a universal statement about all activations with rapidly decaying derivatives. A new activation would still need the actual source law, response bounds, local solution, and relevant nondegeneracy. Nor does the result disprove any global response or tail estimate: the Gaussian upper bound used in this document is compatible with essential unboundedness and with local existence.

There is no theorem here on infinite-time behavior, opposite-label global convergence, finite-width Hessian divergence at fixed positive time, or failure of uniqueness. The audit does not elevate any of those statements to a conclusion.

## 11. Required corrections versus optional clarifications

### Required mathematical corrections

**None identified under the authorized premises.** The ordinary-second-derivative step is valid after explicitly deriving the intermediate \(C^2(L^2)\) property from the already stated bounded directions, as done in Section 7.2 of this report. This is a derivation from existing hypotheses, not an extra premise.

### Optional clarifications

1. **Lines 259–276: name the reverse-only event.** Define \(E_R^\sigma\) from (12)–(13), then say “condition on a reverse source in \(E_R^\sigma\).” This removes the possible impression of conditioning on the forward-dependent query in (14). The existing universal statement at lines 270–272 already supplies the required logic.
2. **Lines 389–399: display the first derivative of the intermediate curve.** Add the two \(L^2\) derivative formulas for \(H^{(2)}_a(t)\), making explicit why \((z'(t)-u)/t\to b\). This makes the ordinary-versus-Peano distinction immediately checkable.
3. **Line 409: soften “Equivalently.”** The cross-remainder estimate is correct, but a Peano expansion alone is not equivalent to an ordinary second derivative. Describing it as an additional Taylor-remainder verification would be more precise.
4. **Lines 237–242 and 337–359: display the nested thresholds once.** Writing \(Q\ge Q_0\) followed by \(M\ge M_0(Q)\), and stating that the probability constants are independent of both, would make the cap/mesh quantifiers easier to inspect.
5. **Lines 332–335: specify the conditional kernel if desired.** “For every residual support value, using the explicit independent Gaussian conditional law” would avoid any literal assertion of uniqueness of conditional probabilities at null conditioning points.
6. **Lines 436–439: optionally give the direct first-derivative bound.** The estimate \(|Df_a[v\otimes B_a]|\le d_ae\|q^{(2)}_a\|_2\) proves exactly the bound needed in the loss calculation with minimal reliance on a broader gradient discussion.

None of these optional changes repairs a false conclusion, adds a missing hypothesis, or changes the valid conditional scope. No candidate edits were made.

## 12. Final premise-conditional disposition

For the exact 478-line source with SHA256

`9efd5283d35a493982f3a142332536d32a9905eff62cb44ea8793aaf001ea79a`,

the new local arguments in Sections 3–7 withstand this isolated adversarial audit under the expressly imported actual finite-Euler/Gaussian-program, local-convergence, and scalar-gradient/symmetry premises. The centered chaining, support-respecting frozen-source conditioning, uniform probability estimates, sequential limits, ordinary second directional derivatives, full-loss identity, and local clock are justified within that premise set.

**The imported premises remain uncertified by this report. The global theorem remains outside the audit and is not certified.**
