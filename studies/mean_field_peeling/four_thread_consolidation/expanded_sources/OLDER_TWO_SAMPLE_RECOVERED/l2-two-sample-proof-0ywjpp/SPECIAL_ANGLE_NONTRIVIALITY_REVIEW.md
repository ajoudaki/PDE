# Independent isolated adversarial review

Source: `/tmp/l2-two-sample-proof-0ywjpp/SPECIAL_ANGLE_NONTRIVIALITY.md`.

Source length: 340 lines, all read. Source SHA256:

`2a6b4a2226737f64e467a8e478e343b47abab46097fe213a868b071df32cc32f`

This review uses only the specified candidate as mathematical input. A procedural mathematical-proof skill was read. No other project, contract, source, review, or author history was consulted; no experiments, external mathematical sources, or other agents were used. The candidate was not edited. Line references below refer to that candidate.

## Verdict and findings

**The conditional special-angle mathematical implication is sound, subject to one minor correction to the wording of a conditional Gaussian moment bound.** I found no substantive algebraic error, missing substantive hypothesis beyond the explicitly assumed population framework, or failure of the asserted finite-time conclusions. The correction does not change a coefficient, covariance, conclusion, or global premise.

This verdict accepts the existence, actual-operator/adjoint, initialization-law, symmetry, and global Gaussian-plus-bounded-remainder premises as hypotheses. It does not establish their simultaneous realization, a canonical population limit, or a bridge from trained finite networks. It applies only to `C=I` and the stated exact antiparallel reduction. It does not certify a global all-angle positive theorem, and this lemma does not accomplish that theorem.

Required local correction:

- **R1 — Put a conditional expectation around the empirical projection-moment bound, lines 248–251.** The displayed upper bound is a bound on the conditional expectation of the empirical pth moment. It is not an almost-sure bound on the realized empirical pth moment of a Gaussian matrix. The preceding sentence correctly says “conditional mean square”; carrying that qualifier explicitly into the next display repairs the literal statement. The corrected bound and its consequences are verified below. This is a minor probabilistic notation/wording error, not a gap requiring a new hypothesis. If “More generally” was intended to carry the conditional expectation forward, R1 merely makes that intended reading explicit.

Optional improvements:

- **O1 — State the finite matrix dimensions explicitly in Section 4.** The normalization used there is the square, equal-width n-by-n normalization. Writing this once would prevent importing a different aspect-ratio convention. The displayed finite program already has the correct equal-width normalization.
- **O2 — Spell out the last empirical-moment argument in lines 252–257.** In particular, mention the high-probability event on which the inverse first-feature Gram and the regression coefficient are bounded, followed by removal of polynomial cutoffs. The argument works with the stated initialization and needs no stronger convergence premise.
- **O3 — Define the raw loss and feature-clock origin explicitly.** Writing `L=sum_a r_a^2` and `s(0)=0` would make the factors and the expansion's origin immediately checkable. They are already determined by the equations and context.

No other required correction was found. In particular, neither a uniform-in-time positive Gram eigenvalue, a lower bound on the activation derivative, independence of the bounded remainders, nor post-transpose independence of finite neurons is needed.

## 1. Premises, regularity, normalization, and clocks

The two populations remain different Hilbert spaces throughout. The identities involving the hidden matrix use its actual adjoint and the normalized population inner products; no identification of first and second neurons is used.

For `v tensor u`, as defined at line 34,

\[
\|v\otimes u\|_{\rm HS}^2=\|v\|_2^2\|u\|_2^2,
\qquad
\langle v\otimes u,\widetilde v\otimes\widetilde u\rangle_{\rm HS}
=\langle v,\widetilde v\rangle_2\langle u,\widetilde u\rangle_1.
\]

For square finite matrices with normalized empirical inner products this operator is the matrix `v u^T/n`, and the adjoint is the ordinary transpose. Consequently the tensor normalization in the flow and the transpose normalization in Section 4 agree.

Differentiating the forward equations gives

\[
\dot f=-2Kr,\qquad K=K^{(1)}+K^{(2)}+K^{(3)}.
\]

The first block is a Gram block with the input Gram included; the second is a Gram of tensor products; the third is a feature Gram. Thus they are positive semidefinite, including the rank-one antiparallel case.

The population expectations in this formulation are scalars, so the residual controls used later are deterministic. The assumed population exchange symmetry gives `f=(g,-g)`. With `r=(g-1)y` and `g=y^T f/2`,

\[
\dot g=\tfrac12y^T(-2Kr)
=(1-g)y^TKy=4(1-g)\kappa.
\]

There is no factor-two error. For the raw loss specified by the flow,

\[
L=\sum_a r_a^2=2(1-g)^2,
\qquad
\dot L=-4r^TKr=-16(1-g)^2\kappa.
\]

This agrees with minus the squared physical parameter speed in the stated metric. When `C=I`, that metric contains two independent first-field norms. In the antiparallel reduction it contains one.

Let `A_T=sup_{t<=T}||W^(2)(t)||_op` and let `U_T` bound the readout in L-infinity. These are finite by hypothesis. Since `|H|<=B` and `0<phi'<=1`,

\[
\|\delta^{(2)}_a\|_2\le U_T,
\quad
\|Q^{(1)}_a\|_2\le A_TU_T,
\quad
\|\delta^{(1)}_a\|_2\le A_TU_T.
\]

These bounds suffice to bound every kernel entry on a finite interval. The phrase “bounded fields” in line 157 need not, and must not, mean bounded preactivations: their tails are unbounded. Therefore the exponent in (6) is finite without an extra bounded-preactivation hypothesis.

The required chain and product rules also follow from the given regularity. A continuously differentiable L2 curve has a pointwise absolutely continuous representative obtained from its velocity integral. Composing it with `phi` gives derivative `phi'(Z) Zdot` in L2. To verify the latter strong derivative directly, use the scalar integral difference quotient and the following fact: if gates are uniformly bounded and converge in probability, multiplying a fixed L2 field by their difference converges to zero in L2. Truncating the fixed field proves the fact. No L2 Frechet differentiability of the nonlinear superposition map is required. The same reasoning and the operator-norm continuity justify differentiating `W^(2)H^(1)` and the readout pairing.

With `s(0)=0` and `ds/dt=4(1-g)`, the feature equations are exactly the gradient flow of the contrast `g` in this raw metric, and

\[
g'=\kappa.
\]

At initialization `g=0`, so `s'(0)=4`; the clock does not remove a singularity or conceal zero hidden physical speeds. A global unbounded range for feature time is neither asserted nor needed.

## 2. First-field tails, positive Gram, and affine-fit distance

For `C=I`, the first equation and `F' phi'=1` give the exact pathwise identity

\[
F(Z^{(1)}_a(t))=F(G_a)-2\int_0^t r_a(u)Q^{(1)}_a(u)\,du.
\]

The polynomial chain rule is legitimate along each absolutely continuous scalar path on a compact interval. After integration, the right side is in L2: `F(G_a)` has finite second moment and the integral is an L2 integral. This proves the claimed L2 identity without assuming that `F` is an L2-smooth map.

For antiparallel inputs, `r_2=-r_1`, `delta^(1)_2=delta^(1)_1`, and `C_12=-1`. Hence

\[
\dot Z^{(1)}_1=-4r_1\phi'(Z^{(1)}_1)Q^{(1)}_1.
\]

The reduced coefficient in line 88 is correct. The second field follows by exact opposition.

Substitution of (2) produces the independent Gaussian integral `I(t)` in (4). Its Gaussianity and independence from `G` follow from the explicitly assumed process properties and the deterministic residual controls. The integrated remainder is bounded by the finite time interval, the residual bound, and `M_T`; no independence of that remainder is used.

For fixed `t`, a finite-variance Gaussian pair has positive probability of lying in some bounded square. Intersect this event with a sufficiently large positive or negative event for `G_a`. Independence ensures positive probability of the intersection. Monotonicity of `F`, together with the bounded remainder, then forces the desired tail of `Z^(1)_a(t)`. This argument also works when the Gaussian integral is degenerate or identically zero.

When `C=I`, the initial pair has positive probability in every prescribed sufficiently distant quadrant. The same intersection argument therefore yields positive probability in arbitrarily small neighborhoods of each limiting activation corner `(B,B)`, `(B,-B)`, `(-B,B)`, and `(-B,-B)`. Equivalently these corners belong to the closed support. If a fixed linear form vanished almost surely, continuity would make it vanish at the corners. The first two already force both its coefficients to vanish. Thus the uncentered Gram `Gamma_1(t)` is positive definite at every finite time.

In the antiparallel case, writing `h=H^(1)_1(t)`,

\[
\Gamma_1(t)=\|h\|_2^2
\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
\qquad \|h\|_2>0.
\]

It has rank one, exactly as the candidate states. No inverse or positive smallest eigenvalue of this two-by-two matrix is used in that case.

Next, (3) gives positive variance to each `xi_a(t)`. The deterministic bound on `S_a(t)` implies the event inclusion

\[
\{\xi_a(t)>R+M_T\}\subseteq\{Z^{(2)}_a(t)>R\},
\]

and the corresponding negative inclusion. Dependence between `xi` and `S` cannot invalidate either inclusion. Thus both hidden preactivations have both unbounded tails at every finite time, including time zero.

For any of these L2 fields `Z`, the Gram of `1,Z` has determinant `Var(Z)>0`. Their span is a closed two-dimensional subspace. Distance zero from `phi(Z)` would therefore imply an attained affine equality. A nonzero slope is incompatible with bounded `phi(Z)` and unbounded support of `Z`; slope zero contradicts strict monotonicity and nonconstancy of `Z`. The positive squared affine-fit distance in (5) follows for each layer, sample, and finite time. It is a separate positive number at each time; no positive uniform lower bound or limiting claim at infinite time follows or is needed.

## 3. Nonfreezing at every positive physical time

The kernel bound above and `g(0)=0` yield

\[
1-g(t)=\exp\!\left(-4\int_0^t\kappa(u)\,du\right)>0.
\]

Initially the hidden blocks vanish and the readout contrast has positive norm. For `C=I`, independence and nonconstancy of `phi(X_1),phi(X_2)` make its squared norm positive. For antiparallel inputs it is the squared norm of the nonzero single output feature. Kernel continuity makes `g` strictly positive immediately after zero; nonnegativity of the kernel then preserves that strict positivity for all later finite times. Thus `0<g(t)<1` for every `t>0`, not merely near initialization.

The readout field cannot vanish in L2 when `g>0`. Since every gate `phi'(Z^(2)_a)` is strictly positive almost surely, each `delta^(2)_a` is nonzero. Equation (3) then makes each reverse Gaussian source nondegenerate. A bounded remainder cannot cancel a Gaussian's unbounded tails, so each `Q^(1)_a` is nonzero as well.

For orthogonal inputs the first-field velocity is `2(1-g)y_a phi'(Z^(1)_a)Q^(1)_a`; in the antiparallel reduction it is `4(1-g)phi'(Z^(1)_1)Q^(1)_1`. The scalar coefficient and gate are nonzero. Each first preactivation therefore moves, and multiplication by the further strictly positive activation gate proves motion of each first activation. A uniform positive lower bound on a gate is unnecessary for this strict nonzero-norm conclusion.

For the hidden matrix, let `u_a=y_a delta^(2)_a`. Its orthogonal-case squared speed is

\[
4(1-g)^2\,\mathbb E_2[u^T\Gamma_1(t)u]
\ge 4(1-g)^2\lambda_{\min}(\Gamma_1(t))
\sum_a\|\delta^{(2)}_a\|_2^2>0.
\]

This is a pointwise quadratic-form inequality in population 2, followed by expectation, and does not assume independence of the two sample reverse fields. For antiparallel inputs the velocity is the single tensor `4(1-g)delta^(2)_1 tensor H^(1)_1`; both factors have positive norm. The rank-one degeneracy causes no failure.

To check possible cancellation in the second-layer velocity, set `c_a=-2r_a`. The adjoint identity gives

\[
\begin{aligned}
\sum_a c_a\langle\delta^{(2)}_a,\dot Z^{(2)}_a\rangle_2
&=\left\langle\sum_a c_a\delta^{(2)}_a\otimes H^{(1)}_a,
\dot W^{(2)}\right\rangle_{\rm HS}
+\sum_a c_a\langle\delta^{(1)}_a,\dot Z^{(1)}_a\rangle_1\\
&=\|\dot W^{(2)}\|_{\rm HS}^2
+\sum_a\|\dot Z^{(1)}_a\|_2^2
\quad(C=I).
\end{aligned}
\]

For antiparallel inputs the last term before reduction is

\[
(c_1-c_2)\langle\delta^{(1)}_1,\dot Z^{(1)}_1\rangle_1
=\|\dot Z^{(1)}_1\|_2^2,
\]

because `dot Z^(1)_1=(c_1-c_2)delta^(1)_1`. There is exactly one independent first-field squared speed, with no additional factor two. Hence the positive right side precludes simultaneous vanishing of both second preactivation velocities. The assumed sample symmetry gives equal norms in the orthogonal case; exact opposition does so in the antiparallel case. Each individual second preactivation velocity is therefore nonzero. Strictly positive gates transfer this conclusion to each second activation.

Finally, `dot W^(3)=2(1-g)(H^(2)_1-H^(2)_2)`. Vanishing contrast would imply `g=0`, contradicting the preceding strict inequality. The readout moves at every positive time too.

All these arguments work at an arbitrary fixed finite positive time. They do not replace “every positive time” by an almost-everywhere assertion. At zero the hidden speeds are exactly zero because `W^(3)(0)=0`, whereas the readout speed is nonzero. The source keeps this distinction correctly.

## 4. Reused transpose, covariance, and joint empirical convergence

For the square finite program, condition on the initial first coordinates and on `Z=W_0 H`. On the invertible-Gram event, Gaussian row conditioning gives the source's projection decomposition. With an independent standard Gaussian matrix `mathcal G`, the resulting conditional reverse law is

\[
W_0^TD
=H A_n+P_{H^\perp}\mathcal G\Sigma_n^{1/2},
\quad
A_n=\Gamma_n^{-1}(Z^TD/n),
\quad
\Sigma_n=D^TD/n.
\]

The transpose orientation is correct. The limiting row mean is

\[
(h_1,h_2)\,\frac{\mathbb E[XD^T]}m,
\]

whose component `a` is `sum_b B_ab h_b` with `B=E[D X^T]/m`, as in (9).

The residual row covariance is `Sigma=E[D D^T]`, not a covariance with a regression subtraction. Conditioning projects the Gaussian noise across first-population coordinates. That projection has fixed rank and vanishing average size per coordinate; it does not subtract the order-one regression covariance from the limiting same-neuron noise. Finite reverse coordinates remain correlated before taking the empirical limit.

Here are the convergence details and the precise repair for R1. Put `P_H=I-P_(H perp)` and `E_n=P_H mathcal G Sigma_n^(1/2)`. Conditional on the original first coordinates and `Z`,

\[
\mathbb E\!\left[\frac1n\sum_i\|(E_n)_i\|^2\,\middle|\,G,Z\right]
=\frac{\operatorname{rank}(P_H)}n\operatorname{tr}(\Sigma_n)
\le\frac{2\operatorname{tr}(\Sigma_n)}n.
\]

More generally, for each fixed `p>=2`,

\[
\mathbb E\!\left[\frac1n\sum_i\|(E_n)_i\|^p\,\middle|\,G,Z\right]
\le \frac{c_p\|\Sigma_n\|^{p/2}}n
\sum_i(P_H)_{ii}^{p/2}
\le\frac{2c_p\|\Sigma_n\|^{p/2}}n.
\]

The last inequality uses `0<=P_ii<=1` and `sum_i P_ii=rank(P_H)<=2`. This is the correct reading of lines 250–251. A realized Gaussian empirical moment has unbounded support, so the expectation cannot literally be omitted from this bound. Since `D` is bounded, `Sigma_n` is uniformly bounded in the square program. Markov's inequality therefore makes the removed projection tend to zero in every fixed empirical Lp norm, in probability.

The remaining steps also hold:

1. Elementary averaging for the initially independent Gaussian coordinates gives `Gamma_n -> mI` and all fixed empirical moments of the old first coordinates. Conditional on those coordinates, the rows of `Z` are independent centered Gaussian pairs of covariance `Gamma_n`.
2. Boundedness and continuity of `D` give conditional variance bounds of order `1/n` for `D^TD/n`. For `Z^TD/n`, boundedness of `D` and the Gaussian second moment give the same bound on bounded-Gram events. Thus both empirical quantities converge in probability to the expectations used in (9). This step does not incorrectly treat `ZD` as bounded.
3. Since `m>0`, with probability tending to one `Gamma_n` has a bounded inverse and `A_n` is bounded. Its limit is `E[XD^T]/m`; the covariance limit is `Sigma`.
4. After dropping `E_n`, the added Gaussian rows are conditionally independent while each old first coordinate is held fixed. Conditional averaging for bounded tests, followed by convergence of `A_n,Sigma_n` and the old-coordinate empirical law, gives the joint limit `(G,B phi(G)+eta)` with `eta` independent of `G`. The shared coefficients converge to deterministic limits, so they do not leave a random common environment in this limiting law.
5. On the same high-probability events the mean rows are uniformly bounded, since `H` is bounded. Gaussian moments of the added rows and all fixed empirical moments of `G` control polynomial tails. Truncation therefore extends the bounded-test result to every fixed mixed polynomial moment. The projection can still be discarded for these tests: the difference of a polynomial at `q` and `q+e` is bounded by a constant times `|e|(1+|G|+|q|+|e|)^(k-1)` for some finite degree `k`; Holder's inequality uses the already available empirical moments and the vanishing empirical Lp norms of `e`.

This proves convergence in probability of the asserted joint empirical laws and each fixed polynomial moment. It does not assert almost-sure convergence, independence of reused finite coordinates, or strong convergence of finite matrices on a pre-existing population space. None of those stronger conclusions is used later.

Positive definiteness of `Sigma` in the orthogonal case is also correct. If `v^TD=0` almost surely, continuity and the full support of the Gaussian pair make it zero everywhere. Off the diagonal `x=y`, the common factor `V` is nonzero, leaving `v_1 phi'(x)+v_2 phi'(y)=0`. Fixing `y` and varying `x` through two values with different derivatives forces `v_1=0`; positivity of the derivative then forces `v_2=0`.

For antiparallel inputs one conditions on the single column. The projection rank is one, the regression coefficient is `E[DX]/m`, and the residual scalar variance is `E[D^2]>0`, since `D=phi(X)phi'(X)` is nonzero except on the Gaussian-null event `X=0`. This is a genuine one-column calculation; no singular two-column inverse is taken. In both cases the positive conditional Gaussian variance and `phi'(G_a)>0` give `||phi'(G_a)Q_a||_2>0`.

## 5. Strong initial limits and the full second-order kernel expansion

For `C=I`, the feature equations contain the factor one half:

\[
(W^{(3)})'=V(s),\quad
(Z^{(1)}_a)'=\frac{y_a}{2}\phi'(Z^{(1)}_a)Q^{(1)}_a,\quad
(W^{(2)})'=\frac12\sum_a y_a\delta^{(2)}_a\otimes H^{(1)}_a.
\]

The readout integral first yields `W^(3)(s)/s -> V(0)` strongly in L2. It is also bounded in L-infinity by `B`. Multiplication by the bounded gates gives `delta^(2)_a(s)/s -> D_a`. Operator-norm continuity, including continuity of the adjoint, then gives `Q^(1)_a(s)/s -> Q_a` strongly. The gate multiplication fact established above and continuity of rank-one tensor products in Hilbert–Schmidt norm propagate these limits through all remaining equations.

In particular, the contribution of the initial hidden-matrix derivative to the second preactivation is

\[
V^{(2)}H^{(1)}_a(0)
=\frac12\sum_b y_bD_b\langle\phi(G_b),\phi(G_a)\rangle_1
=\frac{y_a m}{2}D_a.
\]

The other contribution is `y_a W_0(phi'(G_a)^2 Q_a)/2`. This verifies the complete expression for `v^(2)_a` in (12), with both gate factors present and the sign attached to the correct sample.

Tensor-product inner products and the initial feature Gram `mI` give

\[
d=\frac14\sum_a
\left(\|\phi'(G_a)Q_a\|_2^2+m\|D_a\|_2^2\right)>0.
\]

Using the actual adjoint once more,

\[
y_a\langle D_a,v^{(2)}_a\rangle_2
=\frac12\left(m\|D_a\|_2^2
+\|\phi'(G_a)Q_a\|_2^2\right)>0.
\]

Thus the asserted individual second-layer limits are nonzero; possible cancellation through `W_0` does not defeat them.

For antiparallel inputs, the contrast is the single second activation. The feature gradients have coefficient one, exactly as in (14). The first-field metric has one term and

\[
d=\|\phi'(G_1)Q\|_2^2+m\|D\|_2^2,
\qquad
\langle D,v^{(2)}\rangle_2=d>0.
\]

Neither the half factors from the orthogonal case nor a duplicate first-field norm belongs in this reduced formula.

The hidden block is the sum of the squared hidden feature-gradient speeds in the relevant metric. The strong velocity limits therefore give

\[
\kappa_{\rm hidden}(s)=d s^2+o(s^2).
\]

It remains necessary to include the readout block; the candidate does so correctly. Let `V(s)=(H^(2)_1(s)-H^(2)_2(s))/2`. The L2 chain rule gives

\[
\kappa_{\rm readout}'(s)
=2\langle V(s),V'(s)\rangle_2
=\sum_a y_a\langle V(s)\phi'(Z^{(2)}_a(s)),(Z^{(2)}_a)'(s)\rangle_2.
\]

In the orthogonal case, division by `s` and the strong limits yield

\[
\lim_{s\downarrow0}\frac{\kappa_{\rm readout}'(s)}s
=\sum_a y_a\langle D_a,v^{(2)}_a\rangle_2=2d.
\]

For antiparallel inputs the two sample terms are equal, each equal to `d`, since the second preactivation velocities are opposite and the gates are even. The same limit `2d` results. Integrating `2ds+o(s)` proves

\[
\kappa_{\rm readout}(s)=\kappa_{\rm readout}(0)+d s^2+o(s^2),
\qquad
\kappa(s)=\kappa(0)+2d s^2+o(s^2).
\]

This argument establishes the second-order scalar expansion using strong first nonzero velocity limits. It does not need twice Frechet differentiability of the population activation map. The positive coefficient implies strict increase relative to the initial value for every sufficiently small positive time, and hence nonconstancy of the full raw kernel. It does not imply monotonicity of the kernel at all later times, and the source does not claim that.

As a further exact normalization check, `s(t)=4t+o(t)` implies

\[
\kappa(t)=\kappa(0)+32d\,t^2+o(t^2).
\]

The hidden and readout contributions each have physical-time coefficient `16d`. This confirms both the factor 4 in the clock and the inclusion of the readout term.

## Scope of the accepted conclusion

After the local expectation qualifier in R1, the stated hypotheses imply positive distributional affine-fit distance for each hidden layer and sample at every finite nonnegative time; strictly positive hidden preactivation, hidden activation, hidden-matrix, and readout speeds at every finite positive physical time; and a nonconstant full raw label-direction kernel already near initialization. The zero hidden speeds at initialization are consistent with all three conclusions.

The global representation and existence premises remain hypotheses. This review supplies neither those premises nor an extension beyond the two special input geometries. It gives no certification of the user's ultimately desired global all-angle theorem.

The candidate is unchanged. Its source SHA256 is
`2a6b4a2226737f64e467a8e478e343b47abab46097fe213a868b071df32cc32f`.
